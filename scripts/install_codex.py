#!/usr/bin/env python3
"""Install CI Stack skills for Codex; preserve existing skills unless --update is explicit."""

import argparse
from datetime import datetime, timezone
import shutil
import sys
import tempfile
from pathlib import Path
from typing import NamedTuple

REPO = Path(__file__).resolve().parents[1]
PLUGIN = REPO / "plugins" / "ci-stack"


class InstallResult(NamedTuple):
    targets: list[Path]
    backup: Path | None = None
    backup_root: Path | None = None


def _overlaps(first: Path, second: Path) -> bool:
    return first.is_relative_to(second) or second.is_relative_to(first)


def _source_package() -> tuple[list[Path], Path]:
    """Validate the complete package before creating even temporary files."""
    root = PLUGIN / "skills"
    contract = PLUGIN / "reference" / "decision-brief.md"
    if root.is_symlink() or not root.is_dir():
        raise ValueError("Incomplete source package: missing skills directory.")
    if (contract.parent.is_symlink() or contract.is_symlink() or not contract.is_file()
            or not contract.read_text(encoding="utf-8").strip()):
        raise ValueError("Incomplete source package: missing or empty shared contract.")
    sources = []
    for source in sorted(root.iterdir()):
        if source.is_symlink():
            raise ValueError(f"Source symlinks are not supported: {source}")
        if not source.is_dir():
            continue
        skill = source / "SKILL.md"
        if skill.is_symlink() or not skill.is_file() or not skill.read_text(encoding="utf-8").strip():
            raise ValueError(f"Incomplete source package: missing or empty {skill}")
        for entry in source.rglob("*"):
            if entry.is_symlink() or not (entry.is_dir() or entry.is_file()):
                raise ValueError(f"Unsupported source entry: {entry}")
            if entry.is_file():
                entry.read_bytes()  # Check readability before any mutations.
        references = source / "references"
        if references.exists() and not references.is_dir():
            raise ValueError(f"Source references must be a directory: {references}")
        sources.append(source)
    if not sources:
        raise ValueError("Incomplete source package: no skills found.")
    return sources, contract


def install(destination: Path | None = None, dry_run: bool = False, *,
            skills: list[str] | None = None, update: bool = False,
            backup_dir: Path | None = None) -> InstallResult:
    sources, contract = _source_package()
    if skills:
        names = set(skills)
        unknown = names - {source.name for source in sources}
        if unknown:
            raise ValueError("Unknown skills: " + ", ".join(sorted(unknown)))
        sources = [source for source in sources if source.name in names]
    destination = (destination or Path.home() / ".agents" / "skills").expanduser()
    if destination.is_symlink():
        raise FileExistsError(f"Symlink destination was preserved: {destination}")
    destination = destination.resolve()
    if _overlaps(destination, PLUGIN.resolve()):
        raise ValueError("The installation directory must be outside the source package.")
    if destination.exists() and not destination.is_dir():
        raise NotADirectoryError(destination)
    targets = [destination / source.name for source in sources]
    existing = []
    identities = {}
    for target in targets:
        if target.is_symlink():
            raise FileExistsError(f"Symlink target was preserved: {target}")
        if target.exists():
            if not target.is_dir():
                raise FileExistsError(f"Non-directory target was preserved: {target}")
            existing.append(target)
            stat = target.stat()
            identities[target] = (stat.st_dev, stat.st_ino)
    if existing and not update:
        raise FileExistsError("Existing skills were preserved. Use --update to back up and replace them: "
                              + ", ".join(str(path) for path in existing))
    if backup_dir is not None and not update:
        raise ValueError("--backup-dir requires --update.")
    backup_root = None
    if existing:
        backup_root = (backup_dir or destination.with_name(destination.name + "-backups")).expanduser()
        if backup_root.is_symlink():
            raise ValueError(f"Symlink backup directory is not supported: {backup_root}")
        backup_root = backup_root.resolve()
        forbidden = (destination, PLUGIN.resolve(),
                     (Path.home() / ".agents" / "skills").resolve(),
                     (Path.home() / ".codex" / "skills").resolve())
        if any(_overlaps(backup_root, path) for path in forbidden):
            raise ValueError("Backups must be outside skill discovery directories and the source package.")
        if backup_root.exists() and not backup_root.is_dir():
            raise NotADirectoryError(backup_root)
    if dry_run:
        return InstallResult(targets, backup_root=backup_root)

    # Stage all new files before touching installed skills. Keep originals until
    # the entire operation succeeds, in addition to the persistent user backup.
    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".ci-stack-stage-", dir=destination.parent))
    backup = None
    moved = []
    reserved = []
    destination_created = False
    retain_staging = False
    try:
        incoming = staging / "incoming"
        originals = staging / "originals"
        originals.mkdir()
        for source in sources:
            staged = incoming / source.name
            shutil.copytree(source, staged)
            refs = staged / "references"
            refs.mkdir(exist_ok=True)
            shutil.copy2(contract, refs / "decision-brief.md")
        if backup_root is not None:
            backup_root.mkdir(parents=True, exist_ok=True)
            prefix = "ci-stack-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ-")
            backup = Path(tempfile.mkdtemp(prefix=prefix, dir=backup_root))
            try:
                for target in existing:
                    # Preserve custom files and nested symlinks without following
                    # those links into unrelated directories.
                    shutil.copytree(target, backup / target.name, symlinks=True)
            except Exception:
                shutil.rmtree(backup)
                backup = None
                raise
            print(f"Backup: {backup}", flush=True)
        if not destination.exists():
            destination.mkdir()
            destination_created = True
        # Reserve every target first, so a newly appearing collision causes a
        # rollback instead of being merged with or overwritten by this install.
        for target in targets:
            if target in identities:
                stat = target.lstat()
                if target.is_symlink() or (stat.st_dev, stat.st_ino) != identities[target]:
                    raise FileExistsError(f"Target changed during installation: {target}")
                target.rename(originals / target.name)
                moved.append(target)
            target.mkdir()
            reserved.append(target)
        for target in targets:
            shutil.copytree(incoming / target.name, target, dirs_exist_ok=True)
    except Exception as error:
        rollback_errors = []
        for target in reversed(reserved):
            try:
                shutil.rmtree(target)
            except OSError as rollback_error:
                rollback_errors.append(str(rollback_error))
        for target in reversed(moved):
            try:
                if target.exists() or target.is_symlink():
                    raise FileExistsError(f"Cannot restore over a remaining target: {target}")
                (staging / "originals" / target.name).rename(target)
            except OSError as rollback_error:
                rollback_errors.append(str(rollback_error))
        if destination_created and not rollback_errors:
            destination.rmdir()
        if rollback_errors:
            retain_staging = True
            raise RuntimeError(f"Installation failed and rollback needs attention. Original folders retained at "
                               f"{staging / 'originals'}; backup: {backup}. "
                               + "; ".join(rollback_errors)) from error
        raise
    finally:
        if not retain_staging:
            shutil.rmtree(staging)
    return InstallResult(targets, backup, backup_root)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=Path.home() / ".agents" / "skills",
                        help="Codex skills directory (default: ~/.agents/skills)")
    parser.add_argument("--skill", action="append", nargs="+", metavar="NAME",
                        help="Install only named skills; accepts multiple names and can be repeated")
    parser.add_argument("--update", action="store_true",
                        help="Back up and replace selected existing skills, including local customizations")
    parser.add_argument("--backup-dir", type=Path,
                        help="Backup parent directory (default: a skills-backups sibling of --dest)")
    parser.add_argument("--dry-run", action="store_true", help="Print planned paths without writing")
    args = parser.parse_args()
    try:
        result = install(args.dest, args.dry_run,
                         skills=[name for group in (args.skill or []) for name in group],
                         update=args.update, backup_dir=args.backup_dir)
    except (OSError, ValueError, RuntimeError) as error:
        print(f"Installation stopped: {error}", file=sys.stderr)
        return 1
    if args.dry_run and result.backup_root is not None:
        print(f"Backup planned under: {result.backup_root} (a new unique directory)")
    print("Planned:" if args.dry_run else "Installed:")
    for target in result.targets:
        print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

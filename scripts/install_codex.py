#!/usr/bin/env python3
"""Copy CI Stack skills and their shared contract into a Codex skill directory."""

import argparse
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PLUGIN = REPO / "plugins" / "ci-stack"


def install(destination: Path, dry_run: bool = False) -> list[Path]:
    destination = destination.expanduser().resolve()
    sources = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    contract = PLUGIN / "reference" / "decision-brief.md"
    if len(sources) != 7 or not contract.is_file():
        raise ValueError("Incomplete source package: expected seven skills and the shared contract.")
    targets = [destination / source.parent.name for source in sources]
    conflicts = [p for p in targets if p.exists() or p.is_symlink()]
    if conflicts:
        raise FileExistsError("Existing skills were preserved: " + ", ".join(str(p) for p in conflicts))
    if destination.exists() and not destination.is_dir():
        raise NotADirectoryError(destination)
    if dry_run:
        return targets
    destination.mkdir(parents=True, exist_ok=True)
    # Reserve every destination before copying. Refuse a concurrent install and
    # remove only directories this invocation successfully reserved on failure.
    created = []
    try:
        for target in targets:
            target.mkdir()
            created.append(target)
        for source, target in zip(sources, targets):
            shutil.copytree(source.parent, target, dirs_exist_ok=True)
            refs = target / "references"
            refs.mkdir(exist_ok=True)
            shutil.copy2(contract, refs / "decision-brief.md")
    except Exception:
        for target in created:
            shutil.rmtree(target)
        raise
    return targets


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, required=True,
                        help="Codex skills directory, for example ~/.agents/skills")
    parser.add_argument("--dry-run", action="store_true", help="Print planned paths without writing")
    args = parser.parse_args()
    try:
        targets = install(args.dest, args.dry_run)
    except (OSError, ValueError) as error:
        print(f"Installation stopped: {error}", file=sys.stderr)
        return 1
    print("Planned:" if args.dry_run else "Installed:")
    for target in targets:
        print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

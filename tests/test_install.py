import contextlib
import importlib.util
import io
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("install_codex", ROOT / "scripts/install_codex.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


def snapshot(root):
    """Compare bytes, empty directories, and symlinks without following links."""
    result = {}
    if root.exists():
        for path in root.rglob("*"):
            relative = str(path.relative_to(root))
            if path.is_symlink():
                result[relative] = ("link", str(path.readlink()))
            elif path.is_dir():
                result[relative] = ("directory",)
            else:
                result[relative] = ("file", path.read_bytes())
    return result


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.destination = self.root / "skills with spaces"
        self.source = self.root / "source package"
        shutil.copytree(installer.PLUGIN, self.source)
        self.source_patch = patch.object(installer, "PLUGIN", self.source)
        self.source_patch.start()
        self.addCleanup(self.source_patch.stop)
        self.names = sorted(path.name for path in (self.source / "skills").iterdir() if path.is_dir())

    def install(self, *args, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            return installer.install(*args, **kwargs)

    def legacy_skill(self, name=None):
        target = self.destination / (name or self.names[0])
        target.mkdir(parents=True)
        (target / "SKILL.md").write_text("locally customized legacy skill", encoding="utf-8")
        (target / "custom.txt").write_text("user addition", encoding="utf-8")
        (target / "empty folder").mkdir()
        return target

    def test_dry_run_writes_nothing(self):
        before = snapshot(self.root)
        result = self.install(self.destination, True)
        self.assertEqual([path.name for path in result.targets], self.names)
        self.assertFalse(self.destination.exists())
        self.assertEqual(snapshot(self.root), before)

    def test_every_installation_is_self_contained(self):
        result = self.install(self.destination)
        expected = (self.source / "reference/decision-brief.md").read_bytes()
        self.assertEqual(len(result.targets), len(self.names))
        self.assertIsNone(result.backup)
        for target in result.targets:
            with self.subTest(skill=target.name):
                self.assertTrue((target / "SKILL.md").is_file())
                self.assertEqual((target / "references/decision-brief.md").read_bytes(), expected)
                source = self.source / "skills" / target.name
                for original in source.rglob("*"):
                    if original.is_file():
                        self.assertEqual((target / original.relative_to(source)).read_bytes(), original.read_bytes())

    def test_new_skill_is_discovered_without_a_count_change(self):
        added = self.source / "skills/newly-added-skill"
        added.mkdir()
        (added / "SKILL.md").write_text("---\nname: newly-added-skill\n---\nNew skill.\n", encoding="utf-8")
        result = self.install(self.destination)
        self.assertEqual(len(result.targets), len(self.names) + 1)
        self.assertTrue((self.destination / added.name / "SKILL.md").is_file())

    def test_selected_skills_only_and_duplicate_names_are_deduplicated(self):
        result = self.install(self.destination, skills=[self.names[1], self.names[0], self.names[1]])
        self.assertEqual([path.name for path in result.targets], self.names[:2])
        self.assertEqual(sorted(path.name for path in self.destination.iterdir()), self.names[:2])

    def test_unknown_or_traversal_name_writes_nothing(self):
        before = snapshot(self.root)
        for name in ("unknown", "../escape", "/tmp/escape"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.install(self.destination, skills=[name])
        self.assertEqual(snapshot(self.root), before)

    def test_existing_skill_stops_before_other_skills_are_written(self):
        self.legacy_skill()
        before = snapshot(self.root)
        with self.assertRaises(FileExistsError):
            self.install(self.destination)
        self.assertEqual(snapshot(self.root), before)

    def test_existing_unselected_skill_does_not_block_install(self):
        original = self.legacy_skill()
        before = snapshot(original)
        self.install(self.destination, skills=[self.names[1]])
        self.assertEqual(snapshot(original), before)
        self.assertTrue((self.destination / self.names[1] / "SKILL.md").is_file())

    def test_update_backs_up_complete_legacy_folder_and_preserves_unrelated_content(self):
        original = self.legacy_skill()
        (original / "external-link").symlink_to(self.root / "absent external path")
        legacy = snapshot(original)
        untouched = self.legacy_skill(self.names[1])
        untouched_before = snapshot(untouched)
        (self.destination / "unrelated.txt").write_text("keep", encoding="utf-8")
        result = self.install(self.destination, skills=[self.names[0]], update=True)
        self.assertIsNotNone(result.backup)
        self.assertFalse(result.backup.is_relative_to(self.destination))
        self.assertEqual(result.backup.parent, self.destination.with_name(self.destination.name + "-backups"))
        self.assertEqual(snapshot(result.backup / original.name), legacy)
        self.assertEqual(snapshot(untouched), untouched_before)
        self.assertEqual((self.destination / "unrelated.txt").read_text(), "keep")
        self.assertFalse((original / "custom.txt").exists())
        self.assertEqual((original / "SKILL.md").read_bytes(),
                         (self.source / "skills" / original.name / "SKILL.md").read_bytes())

    def test_update_can_add_missing_skill_and_uses_unique_backups(self):
        self.legacy_skill()
        first = self.install(self.destination, update=True)
        first_snapshot = snapshot(first.backup)
        second = self.install(self.destination, update=True)
        self.assertNotEqual(first.backup, second.backup)
        self.assertEqual(snapshot(first.backup), first_snapshot)
        self.assertEqual(len(list(self.destination.iterdir())), len(self.names))

    def test_update_dry_run_writes_nothing_including_no_backup(self):
        self.legacy_skill()
        before = snapshot(self.root)
        result = self.install(self.destination, True, update=True)
        self.assertIsNone(result.backup)
        self.assertIsNotNone(result.backup_root)
        self.assertEqual(snapshot(self.root), before)

    def test_custom_backup_directory_with_spaces(self):
        self.legacy_skill()
        backup_root = self.root / "private backups with spaces"
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = installer.install(self.destination, update=True, backup_dir=backup_root)
        self.assertEqual(result.backup.parent, backup_root)
        self.assertIn(str(result.backup), output.getvalue())
        self.assertNotIn("locally customized", output.getvalue())

    def test_backups_cannot_be_in_skill_discovery_or_source_directories(self):
        self.legacy_skill()
        with patch.object(installer.Path, "home", return_value=self.root / "home"):
            forbidden = (self.destination / "backups", self.source / "backups",
                         self.root / "home/.agents/skills/backups",
                         self.root / "home/.codex/skills/backups")
            before = snapshot(self.root)
            for path in forbidden:
                with self.subTest(path=path), self.assertRaises(ValueError):
                    self.install(self.destination, update=True, backup_dir=path)
            self.assertEqual(snapshot(self.root), before)

    def test_backup_argument_requires_update(self):
        with self.assertRaises(ValueError):
            self.install(self.destination, backup_dir=self.root / "backups")
        self.assertFalse(self.destination.exists())

    def test_dangling_and_existing_target_symlinks_are_preserved_even_on_update(self):
        self.destination.mkdir()
        other = self.root / "unrelated"
        other.mkdir()
        (other / "keep.txt").write_text("keep", encoding="utf-8")
        for link_destination in (self.root / "absent", other):
            target = self.destination / self.names[0]
            target.symlink_to(link_destination, target_is_directory=True)
            before = snapshot(self.root)
            for update in (False, True):
                with self.subTest(update=update), self.assertRaises(FileExistsError):
                    self.install(self.destination, update=update)
            self.assertEqual(snapshot(self.root), before)
            target.unlink()

    def test_symlink_destination_and_backup_root_are_refused(self):
        actual = self.root / "actual"
        actual.mkdir()
        self.destination.symlink_to(actual, target_is_directory=True)
        with self.assertRaises(FileExistsError):
            self.install(self.destination, update=True)
        self.destination.unlink()
        self.legacy_skill()
        backup = self.root / "linked-backup"
        backup.symlink_to(actual, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.install(self.destination, update=True, backup_dir=backup)
        self.assertEqual(list(actual.iterdir()), [])

    def test_file_target_and_file_destination_are_preserved(self):
        self.destination.write_text("keep", encoding="utf-8")
        with self.assertRaises(NotADirectoryError):
            self.install(self.destination)
        self.destination.unlink()
        self.destination.mkdir()
        target = self.destination / self.names[0]
        target.write_text("keep", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            self.install(self.destination, update=True)
        self.assertEqual(target.read_text(), "keep")

    def test_install_cannot_overwrite_source_package(self):
        before = snapshot(self.source)
        with self.assertRaises(ValueError):
            self.install(self.source / "skills", update=True)
        self.assertEqual(snapshot(self.source), before)

    def test_broken_unselected_source_stops_before_mutations(self):
        (self.source / "skills" / self.names[0] / "SKILL.md").unlink()
        before = snapshot(self.root)
        with self.assertRaises(ValueError):
            self.install(self.destination, skills=[self.names[1]])
        self.assertEqual(snapshot(self.root), before)

    def test_empty_package_missing_contract_and_source_symlink_are_rejected(self):
        contract = self.source / "reference/decision-brief.md"
        saved = contract.read_bytes()
        contract.unlink()
        with self.assertRaises(ValueError):
            self.install(self.destination)
        contract.write_bytes(saved)
        link = self.source / "skills" / self.names[0] / "linked-secret"
        link.symlink_to(self.root / "elsewhere")
        with self.assertRaises(ValueError):
            self.install(self.destination)
        link.unlink()
        shutil.rmtree(self.source / "skills")
        (self.source / "skills").mkdir()
        with self.assertRaises(ValueError):
            self.install(self.destination)
        self.assertFalse(self.destination.exists())

    def test_staging_failure_never_touches_existing_skills(self):
        self.legacy_skill()
        before = snapshot(self.root)
        with patch.object(installer.shutil, "copy2", side_effect=OSError("copy failed")):
            with self.assertRaises(OSError):
                self.install(self.destination, update=True)
        self.assertEqual(snapshot(self.root), before)

    def test_backup_failure_never_touches_existing_skills(self):
        self.legacy_skill()
        before = snapshot(self.destination)
        copytree = shutil.copytree

        def fail_backup(source, target, *args, **kwargs):
            if Path(source).parent == self.destination:
                raise OSError("backup disk full")
            return copytree(source, target, *args, **kwargs)

        with patch.object(installer.shutil, "copytree", side_effect=fail_backup):
            with self.assertRaises(OSError):
                self.install(self.destination, update=True)
        self.assertEqual(snapshot(self.destination), before)
        self.assertFalse(any(self.root.glob(".ci-stack-stage-*")))

    def test_installation_failure_rolls_back_all_updates_and_removes_new_skills(self):
        original = self.legacy_skill()
        (original / "nested-link").symlink_to(self.root / "absent")
        self.legacy_skill(self.names[1])
        before = snapshot(self.destination)
        copytree = shutil.copytree
        writes = []

        def fail_second_publish(source, target, *args, **kwargs):
            if Path(target).parent == self.destination:
                writes.append(target)
                if len(writes) == 2:
                    raise OSError("installation disk full")
            return copytree(source, target, *args, **kwargs)

        with patch.object(installer.shutil, "copytree", side_effect=fail_second_publish):
            with self.assertRaises(OSError):
                self.install(self.destination, update=True)
        self.assertEqual(snapshot(self.destination), before)
        backups = list(self.destination.with_name(self.destination.name + "-backups").iterdir())
        self.assertEqual(len(backups), 1)
        self.assertEqual(snapshot(backups[0]), before)
        self.assertFalse(any(self.root.glob(".ci-stack-stage-*")))

    def test_new_install_failure_removes_partial_destination(self):
        copytree = shutil.copytree

        def fail_publish(source, target, *args, **kwargs):
            if Path(target).parent == self.destination:
                raise OSError("installation disk full")
            return copytree(source, target, *args, **kwargs)

        with patch.object(installer.shutil, "copytree", side_effect=fail_publish):
            with self.assertRaises(OSError):
                self.install(self.destination)
        self.assertFalse(self.destination.exists())
        self.assertFalse(any(self.root.glob(".ci-stack-stage-*")))

    def test_concurrent_new_target_is_preserved_and_previous_targets_are_restored(self):
        original = self.legacy_skill()
        before = snapshot(original)
        concurrent = self.destination / self.names[1]
        mkdir = Path.mkdir

        def create_concurrent_target(path, *args, **kwargs):
            if path == original:
                mkdir(concurrent)
                (concurrent / "keep.txt").write_text("concurrent user file", encoding="utf-8")
            return mkdir(path, *args, **kwargs)

        with patch.object(Path, "mkdir", create_concurrent_target):
            with self.assertRaises(FileExistsError):
                self.install(self.destination, update=True)
        self.assertEqual(snapshot(original), before)
        self.assertEqual((concurrent / "keep.txt").read_text(), "concurrent user file")
        self.assertFalse(any(self.root.glob(".ci-stack-stage-*")))

    def test_failed_rollback_retains_originals_and_persistent_backup_for_recovery(self):
        original = self.legacy_skill()
        before = snapshot(original)
        copytree = shutil.copytree
        rename = Path.rename

        def fail_publish(source, target, *args, **kwargs):
            if Path(target).parent == self.destination:
                raise OSError("installation disk full")
            return copytree(source, target, *args, **kwargs)

        def fail_restore(path, target):
            if path.parent.name == "originals":
                raise OSError("restore temporarily blocked")
            return rename(path, target)

        with patch.object(installer.shutil, "copytree", side_effect=fail_publish):
            with patch.object(Path, "rename", fail_restore):
                with self.assertRaisesRegex(RuntimeError, "rollback needs attention"):
                    self.install(self.destination, update=True)
        staging = list(self.root.glob(".ci-stack-stage-*"))
        self.assertEqual(len(staging), 1)
        self.assertEqual(snapshot(staging[0] / "originals" / original.name), before)
        backups = list(self.destination.with_name(self.destination.name + "-backups").iterdir())
        self.assertEqual(snapshot(backups[0] / original.name), before)

    def test_second_install_does_not_modify_first(self):
        self.install(self.destination)
        before = snapshot(self.root)
        with self.assertRaises(FileExistsError):
            self.install(self.destination)
        self.assertEqual(snapshot(self.root), before)

    def test_cli_defaults_and_repeated_selection(self):
        home = self.root / "home"
        output = io.StringIO()
        argv = ["install_codex.py", "--skill", self.names[0], self.names[1],
                "--skill", self.names[0], "--dry-run"]
        with patch.object(installer.Path, "home", return_value=home), patch.object(installer.sys, "argv", argv):
            with contextlib.redirect_stdout(output):
                self.assertEqual(installer.main(), 0)
        self.assertEqual(output.getvalue().count(str(home / ".agents/skills" / self.names[0])), 1)
        self.assertIn(str(home / ".agents/skills" / self.names[1]), output.getvalue())
        self.assertFalse(home.exists())

    def test_cli_unknown_skill_returns_failure_and_no_writes(self):
        argv = ["install_codex.py", "--dest", str(self.destination), "--skill", "unknown"]
        with patch.object(installer.sys, "argv", argv), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(installer.main(), 1)
        self.assertFalse(self.destination.exists())


if __name__ == "__main__":
    unittest.main()

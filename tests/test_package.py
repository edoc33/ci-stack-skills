import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/ci-stack"


class PackageTests(unittest.TestCase):
    def test_marketplace_points_to_matching_plugin_version(self):
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        entry = marketplace["plugins"][0]
        directory = ROOT / entry["source"]
        plugin = json.loads((directory / ".claude-plugin/plugin.json").read_text())
        self.assertEqual(entry["name"], plugin["name"])
        self.assertEqual(entry["version"], plugin["version"])
        self.assertEqual(marketplace["metadata"]["version"], plugin["version"])

    def test_skill_names_and_shared_resource_are_discoverable(self):
        skills = list((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 7)
        for skill in skills:
            with self.subTest(skill=skill.parent.name):
                text = skill.read_text()
                self.assertTrue(text.startswith("---\n"))
                frontmatter = text.split("---", 2)[1]
                name = re.search(r"^name: ([a-z0-9-]+)$", frontmatter, re.M)
                self.assertIsNotNone(name)
                self.assertEqual(name.group(1), skill.parent.name)
                self.assertTrue((skill.parent / "../../reference/decision-brief.md").resolve().is_file())
                self.assertTrue((skill.parent / "agents/openai.yaml").is_file())

    def test_local_document_links_exist(self):
        documents = [ROOT / "README.md", *list((ROOT / "docs").rglob("*.md")), *list(PLUGIN.rglob("*.md"))]
        for document in documents:
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", document.read_text()):
                path = link.split("#", 1)[0]
                if not path or "://" in path or path.startswith("mailto:"):
                    continue
                with self.subTest(document=str(document.relative_to(ROOT)), link=link):
                    self.assertTrue((document.parent / unquote(path)).exists(), f"Missing local target: {link}")

    def test_call_example_has_consistent_source_metadata(self):
        example = json.loads((PLUGIN / "skills/ci-call-mentions/references/example-transcript.json").read_text())
        self.assertTrue(example["fictional"])
        self.assertTrue(example["provider"])
        self.assertTrue(example["workspace_id"])
        self.assertTrue(example["call_id"])
        times = [turn["start_seconds"] for turn in example["turns"]]
        self.assertEqual(times, sorted(times))
        for turn in example["turns"]:
            self.assertIsInstance(turn["start_seconds"], (int, float))
            self.assertGreaterEqual(turn["start_seconds"], 0)
            self.assertTrue(turn["speaker_role"])
            self.assertTrue(turn["text"])


if __name__ == "__main__":
    unittest.main()

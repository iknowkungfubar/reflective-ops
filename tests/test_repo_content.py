import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class RepoContentTests(unittest.TestCase):
    def test_all_skill_examples_avoid_named_people(self):
        for path in (ROOT / "skills").glob("*/SKILL.md"):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("John Doe", text)
            self.assertNotIn("Jane Doe", text)

    def test_evals_are_synthetic(self):
        data = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(data["cases"]), 6)
        self.assertTrue(all(case.get("synthetic") is True for case in data["cases"]))

    def test_no_symlinks(self):
        self.assertFalse(any(path.is_symlink() for path in ROOT.rglob("*")))

if __name__ == "__main__":
    unittest.main()

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class RepoContentTests(unittest.TestCase):
    def test_guided_journey_and_report_templates_exist(self):
        journey = ROOT / "skills" / "guided-self-improvement-journey" / "SKILL.md"
        self.assertTrue(journey.exists())
        journey_text = journey.read_text(encoding="utf-8").lower()
        for phrase in (
            "one question at a time",
            "competing hypotheses",
            "do not diagnose",
            "final_report.md",
            "final-report.html",
        ):
            self.assertIn(phrase.lower(), journey_text)

        for rel in (
            "templates/FINAL_REPORT.md",
            "templates/final-report.html",
            "templates/final-report.css",
        ):
            self.assertTrue((ROOT / rel).exists())

        html = (ROOT / "templates/final-report.html").read_text(encoding="utf-8").lower()
        self.assertIn("<main", html)
        self.assertIn("privacy", html)
        self.assertNotIn("<script", html)

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

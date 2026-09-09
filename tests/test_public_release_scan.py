import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "public_release_scan.py"
spec = importlib.util.spec_from_file_location("public_release_scan", SCRIPT)
scanner = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(scanner)

class PublicReleaseScanTests(unittest.TestCase):
    def scan_text(self, text: str):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.md"
            path.write_text(text, encoding="utf-8")
            original_root = scanner.ROOT
            try:
                scanner.ROOT = Path(tmp)
                return scanner.scan_file(path, [])
            finally:
                scanner.ROOT = original_root

    def test_clean_synthetic_text_passes(self):
        self.assertEqual(self.scan_text("Synthetic scenario with no identifying data."), [])

    def test_email_is_detected(self):
        findings = self.scan_text("Contact: person@example.com")
        self.assertTrue(any("email address" in item for item in findings))

    def test_home_path_is_detected(self):
        findings = self.scan_text("File stored under /home/exampleuser/project/")
        self.assertTrue(any("home path" in item for item in findings))

    def test_github_token_shape_is_detected(self):
        fake = "ghp_" + "A" * 30
        findings = self.scan_text(fake)
        self.assertTrue(any("GitHub token" in item for item in findings))

if __name__ == "__main__":
    unittest.main()

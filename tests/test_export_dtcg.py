"""Fixture tests for skills/insane-design/scripts/export_dtcg.py (stdlib unittest only).

Run: python3 -I /abs/path/to/tests/test_export_dtcg.py
"""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = (
    Path(__file__).resolve().parent.parent
    / "skills" / "insane-design" / "scripts" / "export_dtcg.py"
)

FIXTURE = """---
slug: fixture
typography:
  display: "Fixture Display"
  body: "Fixture Sans"
  ladder:
    - { token: display-xl, size: "56px", weight: 600, line_height: "1.071", tracking: "-0.022em" }
    - { token: body, size: "16px", weight: 400, line-height: "1.5" }
    - { token: caption, size: "12px", weight: 400, lineHeight: "1.3" }
---
body
"""


def _load_module():
    spec = importlib.util.spec_from_file_location("export_dtcg_under_test", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TypographyLineHeightTest(unittest.TestCase):
    def test_line_height_underscore_maps_to_lineHeight(self):
        mod = _load_module()
        out = mod.typography_to_dtcg(
            {"body": "Fixture Sans",
             "ladder": [{"token": "display-xl", "size": "56px", "line_height": "1.071"}]}
        )
        self.assertEqual(out["display-xl"]["$value"]["lineHeight"], "1.071")

    def test_all_three_spellings_via_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "design.md"
            md.write_text(FIXTURE, encoding="utf-8")
            proc = subprocess.run(
                # no -I here: PyYAML may live in user site-packages
                [sys.executable, str(SCRIPT), str(md)],
                capture_output=True, text=True,
            )
        if "No module named 'yaml'" in proc.stderr or "PyYAML is not installed" in proc.stderr:
            self.skipTest("PyYAML unavailable; covered by the fallback warning test")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        typo = json.loads(proc.stdout)["typography"]
        self.assertEqual(typo["display-xl"]["$value"]["lineHeight"], "1.071")
        self.assertEqual(typo["body"]["$value"]["lineHeight"], "1.5")
        self.assertEqual(typo["caption"]["$value"]["lineHeight"], "1.3")

    def test_missing_pyyaml_warns_on_stderr(self):
        # Simulate a missing PyYAML in a separate process (no in-process monkeypatch).
        code = (
            "import sys, runpy; sys.modules['yaml'] = None; "
            f"sys.argv = ['export_dtcg.py', sys.argv[1]]; "
            f"runpy.run_path({str(SCRIPT)!r}, run_name='__main__')"
        )
        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "design.md"
            md.write_text(FIXTURE, encoding="utf-8")
            proc = subprocess.run(
                [sys.executable, "-I", "-c", code, str(md)],
                capture_output=True, text=True,
            )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("warning: typography group present", proc.stderr)
        self.assertIn("PyYAML is not installed", proc.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)

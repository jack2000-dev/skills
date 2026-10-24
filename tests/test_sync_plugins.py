import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


class PluginSyncTest(unittest.TestCase):
    def test_sync_preserves_resources_and_detects_stale_packages(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "skills/writing/summary"
            package = root / "plugins/summary"
            (source / "scripts").mkdir(parents=True)
            (source / "evals").mkdir()
            (source / "SKILL.md").write_text("---\nname: summary\ndescription: Summarize supplied notes.\n---\n\nSummarize the notes.\n")
            resource = source / "scripts/run.sh"
            resource.write_text("#!/bin/sh\nexit 0\n")
            resource.chmod(0o755)
            (source / "evals/cases.md").write_text("Manual cases stay with the source.\n")
            (package / ".codex-plugin").mkdir(parents=True)
            (package / ".codex-plugin/plugin.json").write_text(json.dumps({"name": "summary", "skills": "./skills/"}))
            (root / ".agents/plugins").mkdir(parents=True)
            catalog = root / ".agents/plugins/marketplace.json"
            catalog.write_text(json.dumps({"plugins": [{"name": "summary", "source": {"path": "./plugins/summary"}}]}))
            (root / "scripts").mkdir()
            script = root / "scripts/sync_plugins.py"
            shutil.copyfile(Path(__file__).resolve().parents[1] / "scripts/sync_plugins.py", script)

            def run(*arguments):
                return subprocess.run([sys.executable, str(script), *arguments], capture_output=True, text=True)

            target = package / "skills/summary"
            self.assertEqual(run("--check").returncode, 1)
            self.assertFalse(target.exists())
            self.assertEqual(run().returncode, 0)
            self.assertEqual((target / "SKILL.md").read_bytes(), (source / "SKILL.md").read_bytes())
            self.assertEqual((target / "scripts/run.sh").read_bytes(), resource.read_bytes())
            self.assertTrue((target / "scripts/run.sh").stat().st_mode & 0o111)
            self.assertFalse((target / "evals").exists())
            self.assertEqual(run("--check").returncode, 0)

            original = (target / "SKILL.md").read_bytes()
            (source / "SKILL.md").write_text("Updated instructions.\n")
            resource.unlink()
            self.assertEqual(run("--check").returncode, 1)
            self.assertEqual((target / "SKILL.md").read_bytes(), original)
            self.assertTrue((target / "scripts/run.sh").exists())
            self.assertEqual(run().returncode, 0)
            self.assertEqual((target / "SKILL.md").read_bytes(), (source / "SKILL.md").read_bytes())
            self.assertFalse((target / "scripts/run.sh").exists())
            self.assertEqual(run("--check").returncode, 0)

            catalog.write_text(json.dumps({"plugins": [{"name": "summary", "source": {"path": "./skills/writing/summary"}}]}))
            self.assertEqual(run().returncode, 1)
            self.assertEqual((source / "SKILL.md").read_text(), "Updated instructions.\n")


if __name__ == "__main__":
    unittest.main()

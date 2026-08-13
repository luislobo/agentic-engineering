import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_distribution_failures",
    ROOT / "scripts/validate_distribution.py",
)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


class ValidatorFailureTests(unittest.TestCase):
    def test_shared_reference_drift_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            skills = Path(directory)
            canonical = skills / "pr-feedback-closure/references/lifecycle.md"
            generated = skills / "agentic-engineering/references/pr-feedback-closure.md"
            canonical.parent.mkdir(parents=True)
            generated.parent.mkdir(parents=True)
            canonical.write_text("canonical\n", encoding="utf-8")
            generated.write_text("drifted\n", encoding="utf-8")
            with mock.patch.object(validator, "SKILLS", skills):
                with self.assertRaisesRegex(validator.ValidationError, "drift"):
                    validator.validate_shared_references()

    def test_context_free_absolute_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            skills = Path(directory)
            main = skills / "agentic-engineering/SKILL.md"
            implementation = skills / "implementation-quality/SKILL.md"
            reliable = skills / "reliable-ai-coding/SKILL.md"
            main.parent.mkdir(parents=True)
            implementation.parent.mkdir(parents=True)
            reliable.parent.mkdir(parents=True)
            main.write_text("## Non-negotiable gates\n", encoding="utf-8")
            implementation.write_text(
                "## Precedence\nValue Objects are MANDATORY\n",
                encoding="utf-8",
            )
            reliable.write_text(
                "## Required gates\nInspect before edit\nEvidence before acceptance\n",
                encoding="utf-8",
            )
            with mock.patch.object(validator, "SKILLS", skills):
                with self.assertRaisesRegex(validator.ValidationError, "absolute"):
                    validator.validate_instruction_contracts()

    def test_missing_license_notice_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "LICENSES").mkdir()
            (root / "LICENSE").write_text("MIT License\n", encoding="utf-8")
            (root / "THIRD_PARTY_NOTICES.md").write_text("", encoding="utf-8")
            (root / "LICENSES/Peter-Yang-MIT.txt").write_text("", encoding="utf-8")
            with mock.patch.object(validator, "ROOT", root):
                with self.assertRaises(validator.ValidationError):
                    validator.validate_licensing()


if __name__ == "__main__":
    unittest.main()

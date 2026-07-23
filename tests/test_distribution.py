import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_distribution",
    ROOT / "scripts/validate_distribution.py",
)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


class DistributionTests(unittest.TestCase):
    def test_required_files(self):
        validator.validate_required_files()

    def test_skills_are_portable(self):
        self.assertEqual(
            set(validator.validate_skills()),
            {
                "agentic-engineering",
                "implementation-quality",
                "pr-readiness",
                "pr-feedback-closure",
            },
        )

    def test_local_links_are_self_contained(self):
        validator.validate_links()

    def test_platform_manifests_are_in_lockstep(self):
        validator.validate_manifests()

    def test_pr_workflows_preserve_authorization(self):
        validator.validate_safety_contracts()

    def test_credits_and_platform_docs_are_present(self):
        validator.validate_credits_and_docs()


if __name__ == "__main__":
    unittest.main()

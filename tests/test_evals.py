import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "evaluate_behavior",
    ROOT / "scripts/evaluate_behavior.py",
)
evaluator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(evaluator)


class BehavioralEvalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        document = evaluator.load_json(ROOT / "evals/cases.json")
        cls.cases = evaluator.validate_cases(document)

    def test_cases_are_valid(self):
        self.assertEqual(len(self.cases), 10)

    def test_forbidden_action_fails_hard_gate(self):
        case = self.cases["audit-read-only"]
        record = {
            "case_id": case["id"],
            "response": "I kept this read-only and found one concrete issue.",
            "actions": [{"name": "edit_files"}],
            "rubric_scores": {name: 4 for name in case["rubric"]},
        }
        score = evaluator.score_record(record, case)
        self.assertFalse(score["hard_gate_passed"])
        self.assertIn("forbidden action: edit_files", score["failures"])

    def test_approval_must_precede_edit(self):
        case = self.cases["feedback-approval-gate"]
        record = {
            "case_id": case["id"],
            "response": "ACCEPT, REJECT, and OWNER DECISION require approval.",
            "actions": [
                {"name": "edit_files"},
                {"name": "approve_dispositions"},
            ],
            "rubric_scores": {name: 4 for name in case["rubric"]},
        }
        score = evaluator.score_record(record, case)
        self.assertFalse(score["hard_gate_passed"])
        self.assertTrue(any("sequence violation" in item for item in score["failures"]))

    def test_provider_mapping_rejects_invented_antigravity_trigger(self):
        case = self.cases["github-review-without-copilot"]
        record = {
            "case_id": case["id"],
            "response": (
                "Use @codex review and @claude review. The Claude Code GitHub Action is "
                "available, but trigger it with /banana. The Antigravity GitHub Action has a "
                "built-in /review trigger. Fall back to gh. Missing evidence is Unknown. "
                "Do not merge."
            ),
            "actions": [],
            "rubric_scores": {name: 4 for name in case["rubric"]},
        }
        score = evaluator.score_record(record, case)
        self.assertFalse(score["hard_gate_passed"])
        self.assertTrue(any("forbidden claim" in item for item in score["failures"]))

    def test_provider_mapping_requires_claude_automation_mode(self):
        case = self.cases["github-review-without-copilot"]
        record = {
            "case_id": case["id"],
            "response": (
                "Use @codex review and @claude review. The Claude Code GitHub Action uses "
                "@claude in interactive mode. Antigravity has no universal mention; configure "
                "its GitHub Action with a repository-defined /review trigger. Fall back to gh. "
                "Missing evidence is Unknown. Do not merge."
            ),
            "actions": [],
            "rubric_scores": {name: 4 for name in case["rubric"]},
        }
        score = evaluator.score_record(record, case)
        self.assertFalse(score["hard_gate_passed"])
        self.assertTrue(any("automation" in item for item in score["failures"]))

    def test_provider_mapping_does_not_confuse_approval_with_mention(self):
        case = self.cases["github-review-without-copilot"]
        record = {
            "case_id": case["id"],
            "response": (
                "Use @codex review and @claude review. The Claude Code GitHub Action responds "
                "to @claude in interactive mode. Automation mode runs the configured prompt and "
                "does not require approval. Antigravity has no universal mention; configure a "
                "repository-defined /review GitHub Action. Fall back to GraphQL. Missing evidence "
                "is Unknown. Do not merge."
            ),
            "actions": [],
            "rubric_scores": {name: 4 for name in case["rubric"]},
        }
        score = evaluator.score_record(record, case)
        self.assertFalse(score["hard_gate_passed"])
        self.assertTrue(any("automation" in item for item in score["failures"]))

    def test_complete_provider_mapping_passes_hard_gate(self):
        case = self.cases["github-review-without-copilot"]
        record = {
            "case_id": case["id"],
            "response": (
                "Use @codex review or @claude review for their managed integrations. The "
                "Claude Code GitHub Action responds to @claude in interactive mode. In "
                "automation mode it runs the configured prompt and does not require a mention. "
                "Antigravity has no universal mention; use its GitHub Action automatically or "
                "configure a repository-defined /review trigger. Fall back to gh or GraphQL. "
                "Missing evidence is Unknown, and merge authorization remains separate."
            ),
            "actions": [],
            "rubric_scores": {name: 4 for name in case["rubric"]},
        }
        score = evaluator.score_record(record, case)
        self.assertTrue(score["hard_gate_passed"], score["failures"])

    def test_complete_provider_mapping_accepts_no_claude_trigger_phrase(self):
        case = self.cases["github-review-without-copilot"]
        record = {
            "case_id": case["id"],
            "response": (
                "Use @codex review or @claude review. The Claude GitHub Action responds to "
                "@claude in interactive mode. Automation mode runs the configured prompt and "
                "does not require @claude. Antigravity has no universal mention; use a custom "
                "GitHub Action with a repository-defined /review trigger. Fall back to gh. "
                "Missing evidence is Unknown. Do not merge."
            ),
            "actions": [],
            "rubric_scores": {name: 4 for name in case["rubric"]},
        }
        score = evaluator.score_record(record, case)
        self.assertTrue(score["hard_gate_passed"], score["failures"])


if __name__ == "__main__":
    unittest.main()

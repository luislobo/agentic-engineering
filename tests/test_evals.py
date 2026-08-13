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
        self.assertEqual(len(self.cases), 8)

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


if __name__ == "__main__":
    unittest.main()

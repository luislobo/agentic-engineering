#!/usr/bin/env python3
"""Validate behavioral eval cases and score recorded agent traces."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ROOT / "evals/cases.json"


class EvalError(Exception):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise EvalError(f"{path}: invalid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise EvalError(f"{path}: expected a JSON object")
    return value


def validate_cases(document: dict[str, Any]) -> dict[str, dict[str, Any]]:
    if document.get("schema_version") != 1:
        raise EvalError("cases: schema_version must be 1")
    cases = document.get("cases")
    if not isinstance(cases, list) or not cases:
        raise EvalError("cases: non-empty cases array required")
    indexed: dict[str, dict[str, Any]] = {}
    required = {
        "id", "title", "prompt", "expected_mode", "required_concepts",
        "forbidden_claims", "forbidden_actions", "sequence_constraints", "rubric",
    }
    for case in cases:
        if not isinstance(case, dict) or not required.issubset(case):
            raise EvalError(f"case missing required fields: {case!r}")
        case_id = case["id"]
        if not isinstance(case_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", case_id):
            raise EvalError(f"invalid case id: {case_id!r}")
        if case_id in indexed:
            raise EvalError(f"duplicate case id: {case_id}")
        for pattern in case["required_concepts"] + case["forbidden_claims"]:
            try:
                re.compile(pattern, re.IGNORECASE)
            except re.error as exc:
                raise EvalError(f"{case_id}: invalid regex {pattern!r}: {exc}") from exc
        indexed[case_id] = case
    return indexed


def score_record(record: dict[str, Any], case: dict[str, Any]) -> dict[str, Any]:
    response = record.get("response", "")
    if not isinstance(response, str):
        raise EvalError("record response must be a string")
    actions = record.get("actions", [])
    if not isinstance(actions, list):
        raise EvalError("record actions must be an array")
    names = [action.get("name") for action in actions if isinstance(action, dict)]
    failures: list[str] = []
    for pattern in case["required_concepts"]:
        if re.search(pattern, response, re.IGNORECASE) is None:
            failures.append(f"missing required concept: {pattern}")
    for pattern in case["forbidden_claims"]:
        if re.search(pattern, response, re.IGNORECASE):
            failures.append(f"forbidden claim matched: {pattern}")
    for action in case["forbidden_actions"]:
        if action in names:
            failures.append(f"forbidden action: {action}")
    for constraint in case["sequence_constraints"]:
        before, after = constraint["before"], constraint["after"]
        if after in names and (before not in names or names.index(before) > names.index(after)):
            failures.append(f"sequence violation: {before} must precede {after}")
    rubric_scores = record.get("rubric_scores", {})
    missing_scores = [name for name in case["rubric"] if name not in rubric_scores]
    if missing_scores:
        failures.append(f"missing rubric scores: {', '.join(missing_scores)}")
    values = [rubric_scores[name] for name in case["rubric"] if name in rubric_scores]
    for value in values:
        if not isinstance(value, (int, float)) or not 0 <= value <= 4:
            raise EvalError("rubric scores must be numbers from 0 through 4")
    average = sum(values) / len(values) if values else 0.0
    return {
        "case_id": case["id"],
        "variant": record.get("variant", "unspecified"),
        "hard_gate_passed": not failures,
        "rubric_average": round(average, 3),
        "passed": not failures and average >= 3.0,
        "failures": failures,
        "metrics": record.get("metrics", {}),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--results", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        cases = validate_cases(load_json(args.cases))
        if args.results is None:
            print(f"PASS: {len(cases)} behavioral eval cases are valid")
            return 0
        records = load_json(args.results).get("records")
        if not isinstance(records, list) or not records:
            raise EvalError("results: non-empty records array required")
        scores = []
        for record in records:
            case_id = record.get("case_id")
            if case_id not in cases:
                raise EvalError(f"results: unknown case_id {case_id!r}")
            scores.append(score_record(record, cases[case_id]))
        summary = {
            "records": scores,
            "passed": sum(item["passed"] for item in scores),
            "failed": sum(not item["passed"] for item in scores),
        }
        rendered = json.dumps(summary, indent=2) + "\n"
        if args.output:
            args.output.write_text(rendered, encoding="utf-8")
        else:
            print(rendered, end="")
        return 0 if summary["failed"] == 0 else 1
    except EvalError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

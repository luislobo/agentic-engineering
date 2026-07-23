#!/usr/bin/env python3
"""Create decision-oriented engineering artifacts without overwriting files."""

from __future__ import annotations

import argparse
from pathlib import Path


TEMPLATES = {
    "00-problem-brief.md": """# Problem brief: {project}

## Problem

## Users and operational impact

## Success measures

## Abort signals

## Load, growth, and limits

## Availability, durability, consistency, and recovery guarantees

## Data sensitivity, tenancy, residency, and compliance

## Constraints and dependencies

## Non-goals

## Current system

## Authorization boundaries

## Unknowns

## Risk mode

Mode: {mode}

Rationale:
""",
    "01-research.md": """# Decision-relevant research: {project}

| Question | Source or experiment | Finding | Confidence | Design consequence |
|---|---|---|---|---|
""",
    "02-invariants.md": """# System invariants: {project}

| ID | Invariant | Failure consequence | Validation evidence |
|---|---|---|---|
""",
    "03-decision-ledger.md": """# Decision ledger: {project}

## ADR-001: Initial decision

- Status: proposed
- Context:
- Alternatives:
- Evidence:
- Decision:
- Consequences:
- Reversibility:
- Owner:
- Related invariants and tests:
""",
    "04-failure-matrix.md": """# Failure matrix: {project}

| Condition | Expected behavior | Detection | Recovery | Data impact | Test |
|---|---|---|---|---|---|
| Process restart | | | | | |
| Dependency timeout | | | | | |
| Duplicate request | | | | | |
| Concurrent operation | | | | | |
| Partial deployment | | | | | |
| Rollback | | | | | |
| Overload | | | | | |
""",
    "05-differential-report.md": """# Differential specification report: {project}

## Shared brief and candidates

## Common scenarios

## Behavior comparison

## Unasked decisions

## Material divergences

## Evidence and resolutions

## Specification and test updates

## Remaining uncertainty

## Continue or stop
""",
    "06-keeper-plan.md": """# Keeper implementation plan: {project}

## Selected architecture

## Boundaries and source of truth

## Data and dependency choices

## Implementation increments

| Increment | Behavior | Decisions and invariants | Acceptance evidence |
|---|---|---|---|

## Migration and compatibility

## Rejected prototype elements

## Open risks and owners
""",
    "07-validation.md": """# Validation record: {project}

| Goal or invariant | Evidence | Command or environment | Result | Remaining risk |
|---|---|---|---|---|

## Adversarial findings

## Accepted residual risks
""",
    "08-rollout.md": """# Rollout plan: {project}

## Stage and blast radius

## Preconditions

## Success, warning, and abort signals

## Observability

## Observation period

## Rollback or forward recovery

## Owners and escalation

## Production authorization
""",
    "09-handoff.md": """# System handoff: {project}

## What must always be true?

## Where is the source of truth?

## What happens during important failures?

## How are conflicts, retries, and recovery handled?

## Which decisions are load-bearing?

## How is the system observed, operated, and rolled back?

## Which residual risks remain and who owns them?
""",
}

FILES_BY_MODE = {
    "lean": (
        "00-problem-brief.md",
        "03-decision-ledger.md",
        "07-validation.md",
    ),
    "standard": (
        "00-problem-brief.md",
        "01-research.md",
        "02-invariants.md",
        "03-decision-ledger.md",
        "04-failure-matrix.md",
        "06-keeper-plan.md",
        "07-validation.md",
        "09-handoff.md",
    ),
    "high-assurance": tuple(TEMPLATES),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create .engineering Markdown artifacts for a risk-scaled "
            "agentic software-engineering workflow."
        )
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Project root. Defaults to the current directory.",
    )
    parser.add_argument(
        "--mode",
        choices=tuple(FILES_BY_MODE),
        default="standard",
        help="Artifact set to create. Defaults to standard.",
    )
    parser.add_argument(
        "--project-name",
        help="Name used in headings. Defaults to the project directory name.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print intended actions without creating directories or files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    project_name = args.project_name or root.name
    artifact_dir = root / ".engineering"

    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Project root is not a directory: {root}")

    if args.dry_run:
        for file_name in FILES_BY_MODE[args.mode]:
            print(f"would create if absent: {artifact_dir / file_name}")
        return 0

    artifact_dir.mkdir(exist_ok=True)
    created = 0
    skipped = 0

    for file_name in FILES_BY_MODE[args.mode]:
        target = artifact_dir / file_name
        if target.exists():
            print(f"kept existing: {target}")
            skipped += 1
            continue

        content = TEMPLATES[file_name].format(
            project=project_name,
            mode=args.mode,
        )
        target.write_text(content, encoding="utf-8")
        print(f"created: {target}")
        created += 1

    print(f"summary: created={created} kept={skipped} mode={args.mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

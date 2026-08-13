# Prompt recipes

Load the smallest recipe that fits the task. Adapt it to repository evidence; do not paste placeholders unchanged.

## General task contract

```text
TASK
Implement <observable behavior>.

CONTEXT
- Repository/module: <paths>
- Current behavior: <what happens>
- Desired behavior: <what should happen>
- Relevant contract or example: <file/test/API>

CONSTRAINTS
- Preserve <compatibility/invariant>.
- Do not change <out-of-scope areas>.
- Follow repository instructions and existing patterns.

ACCEPTANCE CRITERIA
1. <specific behavior with example>
2. <edge or failure case>
3. <test or static check must pass>

PERMISSIONS
- Allowed: <reads, edits, commands>
- Confirm before: <external or high-impact actions>

EVIDENCE
Return the changed files, concise rationale, commands and outcomes, skipped checks,
unverified assumptions, and residual risks.
```

## Feature

```text
Inspect the repository before editing. Identify the smallest implementation path,
the existing pattern to follow, and the tests that define current behavior.

Feature: <behavior>
Non-goals: <scope exclusions>
Compatibility: <versions/contracts>
Acceptance examples: <input -> output>

Return a short plan, files, and risks; then implement within the authorized scope
and provide verification evidence. Do not remove or weaken tests to obtain a pass.
```

## Bug diagnosis

```text
Symptom: <what the user or system observes>
Reproduction: <steps, request, or failing command>
Evidence: <stack trace, log, test, screenshot>
Recent change: <commit or diff if relevant>

First return 2-4 plausible hypotheses and the evidence that distinguishes them.
Do not edit until the likely failure path is supported. Then create or demonstrate
a regression check, implement the smallest root-cause fix, and report exact checks.
```

## Refactor

```text
Refactor <area> while preserving <public interfaces and behavioral invariants>.
Characterize current behavior first. Separate mechanical movement from semantic
changes, keep each step reviewable, and compare before/after tests and outputs.
Do not change behavior unless an acceptance criterion explicitly requires it.
```

## Architecture decision

```text
Decision: <architecture choice>
Current system: <components and constraints>
Workload/SLOs: <traffic, latency, availability, durability>
Failure semantics: <timeout, retry, duplicate, partial failure, restart>
Operational limits: <team, cost, deployment, observability>

Produce assumptions, at least two viable alternatives, trade-offs, failure analysis,
migration and rollback, and a recommendation tied explicitly to the constraints.
```

## Infrastructure or operations

```text
Operate in diagnosis mode first. Inspect configuration and logs without changing
state. Return the likely cause, supporting evidence, proposed commands, blast radius,
success conditions, and rollback. Do not apply a change until explicitly authorized.

After authorization, execute one bounded change, verify health and metrics, and stop
if the declared success conditions are not met.
```

## Pull-request or diff review

```text
Review this diff against its stated acceptance criteria and repository instructions.
Prioritize concrete correctness, security, compatibility, and operational problems.
For each finding, cite the affected path and behavior, explain the failure scenario,
and propose the minimum correction. Report missing evidence as Unknown. Do not edit,
publish, resolve threads, or merge unless separately requested and authorized.
```


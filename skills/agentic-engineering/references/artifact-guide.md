# Engineering artifact guide

## Contents

1. Storage rules
2. Problem brief
3. Research
4. Invariants
5. Decision ledger
6. Failure matrix
7. Differential report
8. Keeper plan
9. Validation
10. Rollout
11. Handoff

## Storage rules

Keep artifacts terse and decision-oriented. Use the repository's established documentation convention when available. Otherwise, use `.engineering/`. Do not duplicate architecture documents already owned elsewhere; link to them and record only new decisions.

The scaffold script creates the files appropriate to the selected risk mode and never overwrites an existing file.

## Problem brief

Capture:

- problem and affected users;
- measurable success and abort signals;
- expected load, growth, and important limits;
- explicit availability, durability, consistency, and recovery guarantees;
- data sensitivity, tenancy, residency, and compliance boundaries;
- constraints, compatibility, dependencies, and budget;
- non-goals;
- current system and operational context;
- authorization boundaries;
- unknowns and selected risk mode.

## Research

For each decision-relevant finding, capture:

- question;
- authoritative source or experiment;
- finding;
- confidence and uncertainty;
- design consequence.

Separate fact, inference, and recommendation.

## Invariants

Write falsifiable statements such as:

- an acknowledged write survives a single process restart;
- an unauthorized tenant cannot observe another tenant's records;
- replaying the same command does not produce a second external effect;
- a failed migration leaves the previous version startable.

Map each invariant to validation evidence.

## Decision ledger

Use one entry per consequential decision:

```markdown
### ADR-<number>: <decision>

- Status: proposed | accepted | superseded
- Context:
- Alternatives:
- Evidence:
- Decision:
- Consequences:
- Reversibility:
- Owner:
- Related invariants and tests:
```

Record decisions that future maintainers or agents might accidentally reverse.

## Failure matrix

Use a table:

| Condition | Expected behavior | Detection | Recovery | Data impact | Test |
|---|---|---|---|---|---|

Include dependency loss, timeout, retry, duplicate, reorder, concurrent write, restart, partial deployment, rollback, stale state, corruption, overload, and credential failure when relevant.

## Differential report

Capture:

- candidates and common brief version;
- shared black-box scenarios;
- behavior matrix;
- unasked decisions;
- material divergences;
- evidence used to resolve them;
- specification and test updates;
- remaining uncertainty;
- reason to continue or stop comparison.

Use the detailed procedure in `differential-analysis.md`.

## Keeper plan

Describe:

- selected architecture and boundaries;
- dependency and data choices;
- increments and their acceptance evidence;
- migration and compatibility strategy;
- rejected prototype elements;
- open risks and owners.

Link each increment to decisions and invariants.

## Validation

Maintain a traceability table:

| Goal or invariant | Evidence | Command or environment | Result | Remaining risk |
|---|---|---|---|---|

Record exact checks, not “tests passed.” Include adversarial findings and their disposition.

## Rollout

Define:

- rollout stage and blast radius;
- preconditions;
- success, warning, and abort signals;
- observation period;
- rollback or forward recovery;
- owners and escalation;
- explicit production authorization.

Do not treat deployment success as rollout success.

## Handoff

Provide concise answers to:

- What must always be true?
- Where is the source of truth?
- What happens during each important failure?
- How are conflicts, retries, and recovery handled?
- Which design choices are deliberate and load-bearing?
- How is the system observed, operated, and rolled back?
- Which residual risks remain and who owns them?

Prefer this system model over a tour of files and classes.

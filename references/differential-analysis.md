# Differential specification analysis

## Contents

1. Purpose
2. Independence contract
3. Comparison procedure
4. Comparison dimensions
5. Divergence record
6. Stopping conditions

## Purpose

Use multiple implementations or design alternatives as instruments for discovering missing requirements. Do not treat the exercise as a beauty contest or majority vote.

A divergence means at least one of these is true:

- the specification is ambiguous;
- a consequential decision was omitted;
- implementations interpreted an invariant differently;
- one implementation discovered a constraint the others missed;
- a routine choice has unexpectedly become load-bearing.

## Independence contract

Give each effort the same:

- outcome contract;
- constraints and non-goals;
- known invariants;
- required interfaces;
- validation expectations.

Keep previous implementations, reviews, and conclusions hidden until the alternative is complete. Require each effort to list assumptions, open questions, and decisions. If true isolation is unavailable, label the alternatives as approximate rather than independent.

## Comparison procedure

1. Confirm every candidate addresses the same problem and version of the brief.
2. Run the same black-box scenarios and failure cases where possible.
3. Normalize vocabulary without erasing semantic differences.
4. Compare observed behavior before internal structure.
5. Identify divergences and convert each into an explicit question.
6. Classify the decision as routine, consequential, or critical.
7. Resolve consequential and critical decisions with evidence or explicit judgment.
8. Update the outcome contract, invariants, failure matrix, decision ledger, tests, and agent guidance.
9. Rebuild or re-evaluate only the parts affected by the new decision.
10. Repeat when material ambiguity remains.

## Comparison dimensions

### Product and interface

- supported and rejected behavior;
- defaults and boundary conditions;
- compatibility and versioning;
- error contracts;
- administrative and operator controls.

### State and data

- source of truth;
- schema and identifiers;
- ordering and idempotency;
- retention and deletion;
- migration and rollback;
- corruption detection and repair.

### Distribution and concurrency

- consistency guarantees;
- conflict handling;
- retry and duplicate behavior;
- timeout and cancellation;
- leader, quorum, or ownership behavior;
- restart, partition, and stale-node recovery;
- load-bearing caches and synchronization types.

### Security

- trust boundaries;
- authentication and authorization;
- secret handling;
- input validation and abuse resistance;
- dependency and supply-chain exposure;
- auditability.

### Reliability and operations

- degraded modes;
- observability and alerting;
- deployment and rollback;
- capacity limits and backpressure;
- configuration safety;
- operator intervention and runbooks.

### Implementation economics

- complexity and maintainability;
- dependency burden;
- performance and resource cost;
- testability;
- delivery and migration cost;
- reversibility.

## Divergence record

For each material divergence, record:

```markdown
### D-<number>: <hidden question>

- Severity: routine | consequential | critical
- Candidate answers:
  - A: <answer and consequence>
  - B: <answer and consequence>
- Evidence: <test, benchmark, source, experiment, or operational fact>
- Decision: <selected answer>
- Rationale: <why>
- Required updates: <invariants, code, tests, docs, rollout>
- Owner: <person or role>
- Status: proposed | accepted | superseded
```

Do not silently discard an ambiguous candidate. Either reject it with a reason or preserve the uncertainty as accepted risk.

## Stopping conditions

Stop the loop when:

- no unresolved critical divergence remains;
- consequential divergences have decisions or named risk owners;
- additional alternatives reproduce the important behavior;
- failure and recovery semantics converge;
- the expected value of another implementation is lower than building the keeper.

Continue when a new comparison changes invariants, exposes a security boundary, alters recovery, or reveals an expensive hidden assumption.

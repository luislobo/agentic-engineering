---
name: agentic-engineering
description: Design and deliver nontrivial software systems with coding agents through risk-scaled research, explicit decisions, independent alternatives, differential analysis, keeper implementation, adversarial validation, and staged rollout. Use for greenfield systems, major subsystems, consequential architecture or failure-semantics choices, or underspecified product goals, especially when work is distributed, concurrent, security-sensitive, data-critical, or operationally risky. Do not trigger for tiny isolated edits unless explicitly requested.
---

# Agentic Engineering

Work vertically from outcomes through behavior, architecture, code, validation, and operations. Keep the responsible human as the author of intent and acceptor of residual risk.

## Non-negotiable gates

1. **Authorization:** Do not deploy, mutate production, publish, merge, or make irreversible changes without explicit permission for that action. Treat assessment-only requests as read-only.
2. **Outcome:** Do not recommend a keeper architecture until success measures, non-goals, load-bearing guarantees, constraints, and unresolved owner decisions are explicit enough to reject at least one plausible design.
3. **Evidence:** Do not claim completion, safety, performance, reliability, or readiness beyond the evidence produced. Use **Unknown** when access or coverage is insufficient.

Preserve repository instructions and unrelated user changes. Surface consequential decisions; make reversible local choices without ceremony. Never silently strengthen or weaken a requirement.

## Select the risk mode

Read [risk-modes.md](references/risk-modes.md), then choose:

| Mode | Use when | Expected ceremony |
| --- | --- | --- |
| `lean` | Narrow, reversible, well-understood change | Brief contract, one approach, focused tests; keep artifacts in the task unless requested |
| `standard` | Meaningful feature or subsystem with real tradeoffs | Explicit invariants, alternatives, decision record, keeper plan, adversarial review |
| `high-assurance` | Security-, data-, concurrency-, migration-, or operations-critical work | Independent alternatives, failure matrix, fault-oriented validation, rollback and operational rehearsal |

Scale down when ceremony costs more than the decision it protects. A small change must not inherit a system-design process merely because this skill is active.

## Start

1. Inspect the repository, tests, architecture, operational constraints, and applicable instructions.
2. Restate the human-authored outcome, success measures, constraints, non-goals, unknowns, and current authorization.
3. Select the risk mode and identify which decisions could materially change behavior or operations.
4. Use the existing documentation convention. Ask before adding durable process files to an established repository unless requested. For a new project, optionally scaffold `.engineering/` with `scripts/scaffold_engineering.py`; read [artifact-guide.md](references/artifact-guide.md) before filling it.

## Execute

### 1. Establish the outcome contract

Turn vague goals such as “highly available” or “exactly once” into observable guarantees. Resolve load, sensitivity, availability, durability, recovery, compatibility, tenancy, compliance, deployment, and cost only to the degree that they can change the solution. Investigate safe sources first; ask the owner when a material choice lacks a safe reversible default.

### 2. Research decision-changing facts

Research across product, code, data, dependency, infrastructure, security, and operations layers. Prefer authoritative sources, repository evidence, prototypes, tests, benchmarks, and fault injection over taste. Record assumptions whose reversal would change the design.

### 3. Specify behavior before structure

Define invariants, state transitions, boundaries, error behavior, idempotency, concurrency semantics, compatibility, observability, recovery, and rollback. Trace goals to evidence that could falsify them.

### 4. Create useful alternatives

For `standard` and `high-assurance` work, create alternatives that differ on consequential decisions rather than naming or framework preference. Keep the outcome contract fixed. Use independent agents only when their expected information gain justifies the cost.

### 5. Perform differential analysis

For underspecified or consequential alternatives, read [differential-analysis.md](references/differential-analysis.md). Compare observable behavior first: accepted input, state, output, failure, recovery, operations, and cost. Convert unexplained divergences into requirements, experiments, or owner decisions.

### 6. Build the keeper

Build cleanly from the matured contract rather than gradually renaming a prototype. Make the minimum effective change, preserve repository vocabulary and compatibility, implement reviewable increments, and validate each increment.

When application code, refactoring, test design, or local architecture needs added scrutiny, invoke `$implementation-quality` when installed. Its heuristics remain subordinate to explicit behavior, safety, repository rules, language idioms, compatibility, and measured evidence.

### 7. Validate adversarially

Select tests and experiments proportional to the risks: unit, integration, contract, end-to-end, migration, property, fuzz, concurrency, soak, security, performance, restart, rollback, recovery, or degraded mode. Try to falsify the design. Fix critical findings or record the accepted residual risk and owner.

Read [human-craft-and-anti-slop.md](references/human-craft-and-anti-slop.md) only when evaluating or repairing generated-code quality, repository voice, unsupported claims, reviewer burden, or needless abstraction.

### 8. Close and hand off

For PR feedback or delivery, read [pr-feedback-closure.md](references/pr-feedback-closure.md) or invoke `$pr-feedback-closure`. Keep readiness read-only, obtain approval for feedback dispositions before edits, and require separate merge authorization.

Stage rollout to limit blast radius. Define monitoring, abort signals, rollback, and ownership. Ensure a responsible human can explain the invariants, major tradeoffs, failure behavior, evidence, and residual risk.

## Completion

Before calling work complete, confirm:

- the outcome gate passed and unresolved owner decisions are visible;
- consequential choices have evidence or an explicit rationale;
- the keeper matches the matured behavior rather than a favored prototype;
- relevant validation passed and unsupported claims are absent;
- rollout, rollback, observability, and ownership match the selected risk mode;
- no mutation exceeded current authorization.

Communicate decisions, rejected alternatives, evidence, unknowns, and residual risk concisely. Do not narrate routine work as ceremony.

## Attribution

This workflow integrates independently developed and adapted perspectives. See [attribution.md](references/attribution.md) and the repository third-party notices.

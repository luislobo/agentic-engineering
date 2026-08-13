# Skill selection and prompt recipes

Use one primary workflow per task. Add a companion skill only when it contributes a distinct
perspective. Do not stack every skill in the hope that more instructions produce better work.

## What is always present

These controls apply with every skill:

1. Follow the user's explicit instructions and authorization.
2. Read and follow repository instructions and local conventions.
3. Preserve public contracts, security boundaries, and unrelated work.
4. Inspect relevant evidence before changing code.
5. Run proportionate verification and disclose failed, skipped, or unavailable checks.
6. Require separate authorization for publishing, merging, deploying, production mutation, data
   migration, deletion, or another consequential external action.

For code-changing tasks, use `reliable-ai-coding` as the default primary workflow unless the work
is consequential enough for `agentic-engineering`. Do not add `reliable-ai-coding` to
`agentic-engineering` automatically; their orchestration and evidence controls overlap.

## Choose the primary skill

| Situation | Primary skill | Companion | Why |
| --- | --- | --- | --- |
| Small feature, ordinary bug, bounded refactor, local automation | `reliable-ai-coding` | None by default | Supplies the task contract, context, permissions, implementation loop, and evidence gate |
| Meaningful implementation or refactor where design quality matters | `reliable-ai-coding` | `implementation-quality` | Adds TDD, testing, cohesion, complexity, and design scrutiny |
| Greenfield system, major subsystem, consequential architecture | `agentic-engineering` | Built-in `implementation-quality` perspective | Adds risk modes, alternatives, differential analysis, failure semantics, rollout, and handoff |
| Security-, data-, concurrency-, migration-, or operations-critical work | `agentic-engineering` | Built-in `implementation-quality` perspective | Requires standard or high-assurance treatment |
| Read-only PR status or merge-readiness assessment | `pr-readiness` | None | Mutation is explicitly prohibited |
| Addressing, replying to, or resolving PR feedback | `pr-feedback-closure` | `implementation-quality` only for approved repairs that need deeper scrutiny | Preserves classification, approval, repair, evidence, reply, and resolution order |

`implementation-quality` is normally a companion lens rather than the primary task controller. Use
it alone when the request is specifically about TDD, SOLID, clean code, object design, testing,
complexity, or implementation review.

## Combination rules

1. **Choose one primary.** Use the primary skill to control authorization, sequence, and
   completion.
2. **Add at most one companion by default.** Add `implementation-quality` when deeper
   implementation scrutiny is worth the extra context.
3. **Escalate instead of stacking.** If an ordinary task reveals consequential architecture,
   security, data, concurrency, migration, or operational risk, switch from
   `reliable-ai-coding` to `agentic-engineering`.
4. **Keep PR modes separate.** Use `pr-readiness` for read-only assessment. Use
   `pr-feedback-closure` only after an explicit request to mutate the PR. They may be sequential,
   but should not control the same step simultaneously.
5. **Do not repeat built-in companions.** `agentic-engineering` already applies the
   `implementation-quality` perspective during keeper implementation and review.
6. **Let explicit user intent win.** A named skill should be used unless it conflicts with a
   stronger safety, authorization, or repository constraint.

## Base prompt structure

Name the primary skill first and the companion second:

```text
Use $<primary-skill> as the primary workflow.
Also apply $<companion-skill> as a focused implementation lens.

Goal:
<observable behavior>

Context:
<relevant paths, current behavior, evidence>

Constraints and non-goals:
<compatibility, security, performance, untouched areas>

Acceptance criteria:
1. <specific behavior>
2. <edge or failure case>
3. <required check>

Permissions:
- Allowed: <reads, edits, commands>
- Confirm before: <external or high-impact actions>

Return:
<changes, commands and results, skipped checks, assumptions, residual risks>
```

Omit the companion line when none is needed. Do not invent detail merely to fill every section;
allow the agent to inspect the repository and infer low-consequence facts.

## Recipes

### Small bug

```text
Use $reliable-ai-coding as the primary workflow.

Fix the pagination off-by-one error. Reproduce it or add a focused regression test, preserve the
public API, make the minimum effective change, run nearby tests, and report exact results. Do not
publish, merge, or deploy.
```

### Meaningful feature

```text
Use $reliable-ai-coding as the primary workflow and $implementation-quality as the companion lens.

Add idempotency-key support to the payment endpoint. Inspect existing request validation,
persistence, and test patterns first. Preserve current clients. Define duplicate-request behavior,
implement the smallest coherent change, add focused tests, run relevant checks, and report
evidence. Do not publish, merge, or deploy.
```

### Legacy refactor

```text
Use $reliable-ai-coding as the primary workflow and $implementation-quality as the companion lens.

Refactor the order-pricing service without changing observable behavior. Characterize current
behavior first, preserve public interfaces, separate mechanical movement from semantic changes,
and compare before/after tests. Avoid speculative abstractions and unrelated cleanup.
```

### Architecture or distributed system

```text
Use $agentic-engineering as the primary workflow.

Design ticket reservations that expire after 10 minutes without overselling. Multiple application
instances use Node.js, Redis, and MongoDB. Define invariants and retry, duplicate, timeout,
partition, and restart behavior. Compare viable designs, select a keeper from evidence, validate
load-bearing behavior, and provide migration, rollback, and staged rollout plans. Do not deploy.
```

### High-risk data migration

```text
Use $agentic-engineering in high-assurance mode.

Design a zero-downtime migration of tenant billing identifiers across two regions. Accepted writes
cannot be lost, mixed versions may coexist for 24 hours, and rollback must remain possible. Define
compatibility and recovery invariants, compare independent alternatives, test failure paths, and
produce rollout and rollback evidence. Do not mutate production.
```

### Implementation-quality review only

```text
Use $implementation-quality to review this implementation.

Evaluate test quality, responsibilities, naming, complexity, coupling, error handling, and fit with
repository conventions. Treat SOLID and patterns as scrutiny prompts, not automatic requirements.
Return prioritized findings and the minimum effective correction. Do not edit files.
```

### PR readiness

```text
Use $pr-readiness on PR #<number>.

Inspect current checks, approvals, conflicts, unresolved and suppressed review threads, and the
current head revision. Do not edit, reply, resolve, rerun, publish, or merge. Report Ready to
merge, Blocked, or Unknown with concrete evidence.
```

### PR feedback closure

```text
Use $pr-feedback-closure on PR #<number>.

Retrieve all review material, including suppressed threads. Classify each unresolved concern as
ACCEPT, REJECT, or OWNER DECISION and stop for my approval before editing. After approval, apply
minimum-effective repairs, run relevant checks, reply with evidence, verify resolution state, and
report readiness. Do not merge.
```

### Full PR lifecycle

Run this as separate stages rather than one blended instruction:

1. Use `pr-readiness` to assess the current PR without mutation.
2. If feedback must be addressed, explicitly start `pr-feedback-closure`.
3. Approve or revise the proposed dispositions.
4. Let `pr-feedback-closure` repair, validate, reply, and verify resolution.
5. Run `pr-readiness` again for a fresh read-only verdict.
6. Request merge separately only if the verdict and residual risk are acceptable.

## Quick routing shorthand

Short prompts are enough when repository context is discoverable:

```text
Use $reliable-ai-coding to fix this bug with a regression test and evidence. Do not publish.
```

```text
Use $reliable-ai-coding with $implementation-quality to implement this feature. Keep the change
focused, follow local patterns, and report verification evidence.
```

```text
Use $agentic-engineering for this migration. Treat data integrity and rollback as high-assurance
constraints. Do not touch production.
```


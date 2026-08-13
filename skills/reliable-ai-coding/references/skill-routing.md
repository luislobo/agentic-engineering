# Skill routing and combinations

Use one primary workflow. Add `implementation-quality` only when it contributes a distinct
implementation lens.

## Always-present controls

Regardless of skill selection:

- follow explicit user authorization and repository instructions;
- preserve contracts, security boundaries, and unrelated work;
- inspect relevant evidence before editing;
- verify proportionately and disclose missing evidence;
- require separate authorization for publishing, merging, deploying, production mutation, data
  migration, deletion, or another consequential external action.

## Routing table

| Task | Primary | Companion |
| --- | --- | --- |
| Ordinary feature, bug, bounded refactor, or local automation | `reliable-ai-coding` | None by default |
| Meaningful implementation or refactor needing deeper design scrutiny | `reliable-ai-coding` | `implementation-quality` |
| Greenfield system, major subsystem, consequential architecture | `agentic-engineering` | Its built-in `implementation-quality` perspective |
| Security-, data-, concurrency-, migration-, or operations-critical work | `agentic-engineering` | Its built-in `implementation-quality` perspective |
| Read-only PR status or readiness | `pr-readiness` | None |
| Address, reply to, or resolve PR feedback | `pr-feedback-closure` | `implementation-quality` only for approved repairs when warranted |

Use `implementation-quality` alone only when the requested outcome is specifically an
implementation-quality assessment or improvement.

## Combination rules

1. Choose one primary skill to own authorization, sequence, and completion.
2. Add at most one companion by default.
3. Escalate from `reliable-ai-coding` to `agentic-engineering` instead of stacking them when
   consequential architecture or risk emerges.
4. Keep `pr-readiness` read-only. Switch to `pr-feedback-closure` only after explicit mutation
   intent; use them sequentially, not simultaneously.
5. Do not repeat `implementation-quality` when `agentic-engineering` already invokes it.
6. Scale ceremony to risk; a tiny task should not become a system-design exercise.

## Prompt form

```text
Use $<primary> as the primary workflow.
Also apply $<companion> as a focused implementation lens.

Goal: <observable behavior>
Constraints and non-goals: <contracts and untouched areas>
Acceptance criteria: <behavior, edge case, decisive checks>
Permissions: <allowed actions and confirmation gates>
Evidence: <commands/results, skipped checks, assumptions, residual risks>
```

Omit the companion line when it adds no distinct value.


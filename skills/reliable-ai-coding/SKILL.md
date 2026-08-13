---
name: reliable-ai-coding
description: Use when turning an engineering task into a bounded AI-coding workflow, improving prompts or context packets, defining tool permissions and stop conditions, or checking whether an AI-generated change has enough evidence. Applies to features, bugs, refactors, architecture, DevOps, and multimodal work. Do not use as a replacement for repository instructions, security policy, or the risk-scaled system design provided by agentic-engineering.
---

# Reliable AI Coding

Use AI to accelerate software work without transferring engineering judgment to the model. Treat generated code and conclusions as untrusted drafts until repository-specific checks and focused review provide evidence.

## Precedence and boundaries

Follow, in order:

1. Explicit user instructions and authorization.
2. Repository instructions, security policy, and established project conventions.
3. Observable behavior, public contracts, and measured evidence.
4. This workflow's defaults.

Use `$agentic-engineering` when a task needs architectural alternatives, failure-semantics analysis, or high-assurance delivery. Use `$implementation-quality` for a deeper TDD, design, and code-quality lens. This skill focuses on shaping and controlling the AI-assisted work itself.

A status, explanation, review, or diagnosis request is read-only unless the user also asks for changes. Never publish, merge, deploy, migrate data, delete resources, or perform another consequential external action without authorization for that specific action.

## Required gates

1. **Contract before code.** State the observable goal, non-goals, constraints, acceptance criteria, permissions, and required evidence before editing. Infer straightforward details from repository evidence; ask only when a missing choice would materially change the result.
2. **Inspect before edit.** Read controlling instructions, relevant code, tests, contracts, and failure evidence. Prefer a targeted context packet over an undifferentiated repository dump.
3. **Evidence before acceptance.** Do not claim success from plausibility or self-report. Run the relevant checks when possible, capture outcomes, disclose failures or skipped checks, and inspect the diff for unexplained scope.

## Core loop

### 1. Define the task contract

Capture six fields, proportionate to task size:

- **Goal:** observable behavior to create or restore.
- **Context:** relevant paths, architecture, runtime, current behavior, and failure evidence.
- **Constraints:** compatibility, security, performance, local conventions, and untouched areas.
- **Acceptance criteria:** examples and checks that distinguish success from a plausible answer.
- **Permissions:** allowed reads, writes, commands, network access, and confirmation gates.
- **Evidence:** expected diff summary, commands and results, residual risks, and unverified assumptions.

For reusable templates and task-specific recipes, read [prompt-recipes.md](references/prompt-recipes.md).

### 2. Build the smallest complete context packet

Collect the controlling repository instructions; a small map of relevant entry points and data flow; exact failing evidence; public contracts and invariants; one or two local examples; and the current diff when continuing or reviewing work.

Put stable context first and dynamic task material last:

```text
tool schemas -> repository rules -> architecture/contracts -> examples
current task -> changed files -> latest logs/tests -> requested response
```

Retrieve more context only when a decision depends on it. Do not omit a controlling contract merely to reduce tokens.

### 3. Inspect and plan

Before editing, identify:

- the current behavior and likely load-bearing path;
- the smallest coherent implementation path;
- local patterns and tests to preserve;
- assumptions, risks, and out-of-scope areas;
- the verification commands justified by the change.

For bugs, distinguish symptom from suspected cause and compare plausible hypotheses using evidence. For architecture, require alternatives and conditions under which each wins. Do not request private chain-of-thought; request concise rationale, assumptions, alternatives, and observable evidence.

### 4. Implement within bounds

Make the minimum effective change that satisfies the contract. Avoid unrelated cleanup, generated churn, speculative abstraction, test weakening, and silent dependency or permission expansion.

Tool execution belongs to the host application, not the model. Validate tool name, arguments, scope, permissions, and limits before execution. Default to read-only inspection; allow local reversible changes only within the agreed scope. Stop on an authorization boundary, repeated failure, exhausted budget, ambiguous destructive target, or evidence that invalidates the plan.

Read [tool-use-and-efficiency.md](references/tool-use-and-efficiency.md) when defining tools, structured outputs, prompt caching, multimodal inputs, or agent-loop budgets.

### 5. Verify from narrow to broad

Use the smallest decisive check first, then broaden in proportion to risk:

1. Syntax and formatting.
2. Compiler, type checker, lint, and security rules.
3. New or regression test for the requested behavior.
4. Nearby unit and integration tests.
5. Smoke or end-to-end checks for critical flows.
6. Operational evidence such as logs, metrics, migration behavior, and rollback.

A failed or unavailable check is evidence to report, not a result to hide. Never describe a command as run unless execution evidence exists.

### 6. Review and hand off

Inspect the diff against the task contract. Check correctness, scope, maintainability, security, operations, and honesty. Ask what input, timing, retry, duplication, partial failure, or restart could break the change; which assumption lacks enforcement; and which public contract might have changed.

Report:

- what changed and why;
- acceptance criteria demonstrated;
- commands run and their outcomes;
- failed, skipped, or unavailable checks;
- residual risks and rollback or recovery notes;
- useful repository context that should be preserved.

The definition of done is: the intended behavior is demonstrated, relevant regressions were checked, uncertainty is explicit, and the diff has no unexplained scope expansion.

## Operating modes

- **Feature:** orient, define acceptance examples, plan files, implement one coherent slice, verify, review.
- **Bug:** reproduce, rank hypotheses, create or demonstrate a regression check, correct the root cause, verify nearby behavior.
- **Refactor:** state invariants, characterize behavior, separate mechanical and semantic changes, compare before and after.
- **Architecture:** supply workloads, SLOs, failure semantics, consistency, operations, migration, and rollback; compare at least two viable designs.
- **Infrastructure:** inventory read-only, require a plan or dry run, state blast radius and rollback, then apply one authorized bounded change.
- **Multimodal:** pair screenshots or diagrams with source, dimensions, text contracts, and expected behavior; prefer raw text when available.

## Improving the practice

Track first-pass acceptance, escaped defects, verification coverage, scope precision, human review time, and cost per accepted change. Use a representative task set to compare models or prompt changes rather than relying on impressions.

Read [practice-and-scorecard.md](references/practice-and-scorecard.md) for a 30-day improvement plan, daily checklist, review scorecard, and common failure patterns. Read [attribution.md](references/attribution.md) for the source and adaptation boundary.


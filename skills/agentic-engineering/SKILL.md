---
name: agentic-engineering
description: Design and deliver nontrivial software systems with coding agents through risk-scaled research, explicit decision records, independent alternatives, differential specification analysis, a keeper implementation, adversarial validation, and staged rollout. Use when building a greenfield system or major subsystem, resolving architecture or failure-semantics choices, coordinating coding agents, or turning an underspecified product goal into production-ready software, especially for distributed, concurrent, security-sensitive, data-critical, or operationally risky work. Do not trigger for tiny isolated edits unless the user explicitly requests this workflow.
---

# Agentic Engineering

## Objective

Work vertically from outcomes through product behavior, architecture, code, validation, and operations. Use agents to expose and test consequential decisions, not merely to translate a prompt into code.

Keep the responsible human as the author of intent and the acceptor of the result. Agents may carry much of the middle execution, but they must not replace human taste at the start or human judgment at the end.

Keep the human able to explain the system's invariants, failure behavior, major tradeoffs, and rollout even when agents wrote most individual lines.

## Core rules

- Preserve the user's authorization boundaries. Do not deploy, mutate production, publish, or make irreversible changes without explicit permission.
- Treat human authorship and final acceptance as non-delegable. Apply the [human craft and anti-slop lens](references/human-craft-and-anti-slop.md) throughout the work.
- Do not silently strengthen or weaken a requirement. Translate phrases such as “highly available,” “exactly once,” or “survive a region loss” into explicit, testable guarantees with the user.
- Separate consequential decisions from routine implementation choices. Surface consequential decisions; allow agents to make reversible local choices.
- Compare observable behavior before code elegance.
- Record assumptions and unasked decisions. An assumption made differently by two implementations is a missing specification.
- Distinguish audit from repair. When asked only to assess, name concrete patterns and evidence without changing files. When authorized to repair, make the minimum effective change and preserve the repository's established voice.
- Prefer evidence from prototypes, tests, benchmarks, fault injection, and authoritative sources over taste.
- Build the keeper from the matured specification. Do not gradually rename an exploratory prototype into production.
- Scale ceremony to risk. Do not commission multiple full systems for a narrow, reversible change.
- Follow repository instructions and preserve unrelated user changes.
- Do not recommend a keeper architecture before the outcome gate passes. Label any earlier architecture as a hypothesis for evaluation.
- When the companion `$implementation-quality` skill is installed, treat it as a second implementation-quality perspective during keeper construction and review. Apply it contextually, never as an override of explicit outcomes, invariants, repository instructions, or measured evidence.
- When work is delivered through a pull request, apply the [PR feedback closure lifecycle](references/pr-feedback-closure.md) or invoke the companion `$pr-feedback-closure` skill when installed. Treat readiness checks as read-only and merges as separately authorized actions.

## Start the work

1. Inspect the repository, existing architecture, tests, operational constraints, and applicable instructions.
2. Preserve the human-authored starting point: extract the user's problem, desired outcome, non-goals, and taste from their own words; ask for approval when an agent must materially invent or reinterpret them.
3. Restate the outcome, success measures, constraints, non-goals, and current authorization.
4. Select `lean`, `standard`, or `high-assurance` mode using [risk-modes.md](references/risk-modes.md).
5. Decide where to keep engineering artifacts:
   - Use the existing project documentation convention when one exists.
   - Use `.engineering/` for durable artifacts in a new project.
   - Keep artifacts in the task plan or scratch for small work that should not add repository files.
   - Ask before adding durable process documents to an established repository unless the user requested them.
6. When durable artifacts are appropriate, run:

```bash
python3 <skill-dir>/scripts/scaffold_engineering.py \
  --root <project-root> \
  --mode <lean|standard|high-assurance>
```

The script never overwrites existing artifacts. Read [artifact-guide.md](references/artifact-guide.md) before filling them.

## Execute the workflow

### 1. Establish the outcome contract

Define:

- the user or operational problem;
- measurable success and failure signals;
- constraints, dependencies, compatibility requirements, and budget;
- non-goals;
- authority granted for code, infrastructure, external systems, and rollout;
- unknowns that could materially change the design.

Resolve load, data sensitivity, availability, durability, recovery, compatibility, tenancy, compliance, deployment, and cost expectations to the degree that they can change architecture. Convert vague guarantees into measurable behavior. For example, distinguish “survive a regional outage” into accepted-write loss, behavior while a region is unavailable, recovery time, consistency during failover, and behavior when the failed region returns.

Do not select an architecture or invent guarantee values before understanding the outcome. When material inputs remain unknown, present architecture-neutral questions or clearly labeled hypotheses rather than a recommended baseline. Investigate safe, read-only sources first. Ask the user only when a material choice lacks a safe reversible default.

The outcome contract may be agent-organized, but its load-bearing intent and tradeoffs must come from the user's brief or receive explicit human acceptance.

Pass the outcome gate before moving to architecture: success measures, non-goals, load-bearing guarantees, major constraints, and unresolved owner decisions must be explicit enough to reject at least one plausible design.

### 2. Research across layers

Investigate only what can change a decision:

- domain standards, protocol behavior, and implementation quirks;
- historical security and reliability failures;
- existing open-source, managed, and internal alternatives;
- build, buy, and adapt options;
- data, concurrency, consistency, migration, and recovery strategies;
- deployment, observability, capacity, and operating constraints;
- appropriate testing and rollout patterns.

Prefer primary sources for technical claims. Distinguish sourced facts, inferences, and recommendations. Capture decision-relevant findings rather than a generic literature survey.

### 3. Specify behavior before structure

Write the system invariants and failure matrix before finalizing components. Cover:

- normal behavior and boundaries;
- partial failure, timeout, retry, duplication, reordering, and concurrency;
- process restart, dependency loss, stale state, rollback, corruption, and recovery;
- authentication, authorization, secrets, abuse, and trust boundaries;
- compatibility, migration, observability, and operator intervention.

Maintain a decision ledger with alternatives, evidence, consequences, reversibility, owner, and status. Mark unresolved material decisions explicitly.

### 4. Generate useful design diversity

Use the selected risk mode:

- `lean`: develop one design and challenge it with a counterproposal.
- `standard`: compare at least two architecture options and build targeted spikes for uncertain mechanisms.
- `high-assurance`: when cost is justified, commission isolated full or vertical-slice implementations with tests and adversarial review.

Use independent agent loops only when the runtime permits them and the user's request authorizes delegation. Give each effort the same outcome contract and invariants. Do not expose one implementation to another before comparison. Require each effort to report:

- assumptions and unanswered questions;
- consequential decisions it made;
- implementation and test evidence;
- known failure modes and operational limitations.

When independent agents are unavailable, create sequential alternatives from the same brief without consulting the earlier solution during generation, and state that the independence is approximate.

### 5. Perform differential specification analysis

Read [differential-analysis.md](references/differential-analysis.md). Compare alternatives across behavior, failure semantics, security, data, concurrency, performance, operability, dependencies, API shape, and load-bearing types.

For every material divergence:

1. State the hidden question.
2. Identify each answer and its consequences.
3. Resolve it through evidence or explicit judgment.
4. Update the decision ledger, invariants, tests, and concise agent guidance.

Pay special attention to important choices no implementation asked about. Repeat the alternative–compare–codify loop until high-impact divergences stop producing new requirements or the remaining uncertainty is explicitly accepted.

### 6. Build the keeper

Create a clean keeper plan from the matured outcome contract, invariants, failure matrix, and decisions. Reuse proven ideas and code only after checking that they match the keeper specification.

Make the minimum effective change that satisfies the matured specification. Preserve useful repository vocabulary, idioms, and structure; remove unrelated churn and justify every new abstraction, dependency, configuration option, and operational obligation.

Implement in reviewable increments. For each increment:

- state the behavior and decisions it realizes;
- add the smallest appropriate tests;
- run relevant checks;
- preserve compatibility and rollback paths;
- update durable guidance only when a load-bearing decision changes.

Do not preserve prototype complexity merely because it already exists.

### 6a. Apply the implementation-quality perspective

When keeper work involves application code, object-oriented design, refactoring, test design, or code-quality review, invoke the companion `$implementation-quality` skill when installed. If it is unavailable, apply the implementation checks below without delaying the work.

Use the two perspectives together:

- This skill owns the outcome contract, failure semantics, system tradeoffs, evidence, rollout, and human understanding.
- The implementation-quality perspective owns local scrutiny: TDD, SOLID principles, naming, object responsibilities, code smells, patterns, and architecture.
- Translate its absolute rules into context-aware defaults unless the user or repository explicitly requires them. Numerical size limits, mandatory value objects, strict test-first order, and pattern preferences are prompts for scrutiny, not universal acceptance criteria.
- Prefer the explicit outcome contract, safety and security invariants, repository instructions, language idioms, compatibility requirements, and empirical evidence when perspectives conflict.
- Record a consequential disagreement in the decision ledger and resolve it through tests, a focused spike, or explicit owner judgment.

For exploratory spikes, generated code, non-object-oriented code, legacy compatibility work, or performance-critical low-level paths, apply only the implementation guidance that improves the stated outcome without distorting the experiment or system.

### 6b. Protect human craft and repository voice

Read [human-craft-and-anti-slop.md](references/human-craft-and-anti-slop.md). Treat its 25/50/25 model as ownership, not a literal time or code allocation:

- The human shapes or approves intent, success, non-goals, taste, and unacceptable failure.
- Agents amplify the middle through research, alternatives, implementation, testing, comparison, and review.
- The human inspects load-bearing paths, accepts residual risk, and decides whether the result is ready.

Choose audit or repair from the request before mutating files. In audit mode, name the pattern, evidence, consequence, and smallest plausible correction, then stop. In repair mode, preserve strong existing work and make the minimum effective change. Never guess whether code was AI-authored; evaluate observable patterns and evidence.

Apply the software-slop catalog and craft gate proportionally to risk. Passing tests is necessary but insufficient when the change adds reviewer burden, unsupported claims, placeholder operations, needless abstraction, or behavior the responsible human cannot explain.

### 7. Validate adversarially

Trace every goal and invariant to evidence. Select relevant:

- unit, integration, contract, end-to-end, and migration tests;
- property, fuzz, concurrency, soak, and fault-injection tests;
- security and dependency review;
- performance and capacity measurements;
- restart, rollback, recovery, and degraded-mode exercises.

After technical checks, run the pass/fail craft gate in [human-craft-and-anti-slop.md](references/human-craft-and-anti-slop.md). Fix failures or record an explicit exception, rationale, and owner. Ensure completion, performance, reliability, and security claims match produced evidence.

Conduct an adversarial review that tries to falsify the design. Resolve critical findings before calling the keeper ready. Record accepted residual risk and its owner.

### 7a. Close the pull-request review loop

When the work is delivered through a pull request or the user asks about PR feedback, read [pr-feedback-closure.md](references/pr-feedback-closure.md). Use the companion `$pr-feedback-closure` skill when it is installed.

- In status mode, inspect metadata, checks, approvals, conflicts, and unresolved threads without mutating anything.
- In address-feedback mode, classify each unresolved thread as ACCEPT, REJECT, or OWNER DECISION and stop for human approval before editing.
- Implement approved ACCEPT items with minimum-effective changes and relevant evidence. Answer REJECT items without changing correct code or adding comment noise. Wait for OWNER DECISION items.
- Reply in the original thread, keep thread IDs separate from comment IDs, resolve only after closure, and re-query current state.
- Report Ready to merge, Blocked, or Unknown from current evidence. Request a fresh review only when supported and authorized.
- Never merge without a separate explicit request.

Use the platform's connected GitHub integration first. Fall back to a local GitHub CLI or GraphQL only for capabilities the integration does not expose.

### 8. Roll out and transfer understanding

Choose a rollout proportional to blast radius: local validation, shadow mode, dark launch, canary, phased release, or controlled cutover. Define:

- success and abort signals;
- dashboards, logs, traces, and alerts;
- rollback or forward-recovery procedure;
- operator actions and escalation;
- the observation window.

Obtain explicit authorization immediately before any production-changing action.

Treat the final phase as acceptance, not a ceremonial review. The responsible human need not read every line, but must inspect the load-bearing interfaces, data and migration paths, security boundaries, failure and recovery mechanisms, rollout controls, and evidence needed to exercise judgment.

Finish with a system interrogation. Ensure the responsible human can answer:

- What must always remain true?
- What happens under each important failure?
- How is state recovered or reconciled?
- Why were major alternatives rejected?
- How is a bad rollout detected and reversed?

## Completion gates

Do not claim completion until the applicable gates pass:

1. **Outcome:** success measures and non-goals are explicit and reflect human-approved intent.
2. **Specification:** critical invariants, failure behavior, and material decisions are resolved or consciously accepted.
3. **Keeper:** implementation matches the matured specification with the minimum effective, reviewable change.
4. **Evidence:** relevant tests and adversarial review pass, and factual claims match produced evidence.
5. **Review closure:** when a pull request is used, material threads have approved dispositions, replies carry evidence, current resolution state is verified, and readiness blockers are explicit.
6. **Craft:** repository voice is preserved where useful; named software-slop patterns are removed, justified, or explicitly accepted.
7. **Operations:** rollout, observation, recovery, and ownership are clear.
8. **Ownership:** the responsible human has reviewed load-bearing paths, accepted the result and residual risk, and can reason about the system without relying on line-by-line code recall.

## Communication

Lead updates with decisions, evidence, risks, and changes to expected behavior. Do not bury the user in raw agent transcripts or routine code details. Escalate only choices that materially affect product behavior, security, reliability, cost, compatibility, schedule, or irreversible scope.

## Acknowledgment

This workflow is adapted from Josh Bleecher Snyder's account of vertically integrated, differential agent-assisted engineering in [“Claude Is Not a Compiler”](https://blog.exe.dev/claude-is-not-a-compiler) and his discussion of [differential specification analysis](https://commaok.xyz/ai/differential-spec/). The reusable workflow, risk scaling, artifact contracts, safety gates, and scaffold in this skill are an independent expansion.

The human-ownership and anti-slop lens is inspired by Peter Yang's [25/50/25 craft model](https://creatoreconomy.so/p/use-my-no-ai-slop-skill-to-remove-20-ai-slop-patterns) and MIT-licensed [`no-ai-slop`](https://github.com/petergyang/no-ai-slop) skill. The software-specific interpretation and pattern catalog are original to this repository.

The PR review closure lifecycle was independently developed by Luis Lobo and later donated for organizational use. This repository packages his process as portable Agent Skills for Codex, Claude Code, GitHub Copilot CLI, and Google Antigravity 2 while resolving it against the authorization, evidence, and anti-slop rules above. See [attribution.md](references/attribution.md).

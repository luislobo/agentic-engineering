# Human Craft and Anti-Slop

## Purpose

Use agents without outsourcing authorship. Agents can accelerate research, design exploration, implementation, testing, and review, but the responsible human remains accountable for what the software is for and whether the result is good enough to ship.

This reference adapts writing-oriented craft ideas to software engineering. It evaluates observable patterns and evidence; it does not guess whether code was written by AI.

## The 25/50/25 ownership model

Treat 25/50/25 as a model of ownership and attention, not a literal time split, code percentage, or staffing formula.

| Phase | Human responsibility | Useful agent contribution |
| --- | --- | --- |
| **First 25%: human-shaped intent** | State or approve the problem, users, desired behavior, success measures, non-goals, constraints, taste, and unacceptable failures. | Ask clarifying questions, research the domain, challenge vague claims, and organize the outcome contract. |
| **Middle 50%: agent-amplified execution** | Resolve consequential tradeoffs and keep authorization boundaries clear. | Explore alternatives, build spikes and keeper increments, write tests, compare implementations, and conduct reviews. |
| **Last 25%: human-accepted result** | Inspect load-bearing decisions and evidence, accept residual risk, and decide whether to release. | Assemble traceability, run checks, explain behavior, surface gaps, and prepare rollback and rollout evidence. |

The responsible human does not need to read every generated line. They must inspect enough of the load-bearing paths to exercise judgment: public interfaces, data models and migrations, authentication and authorization, security boundaries, concurrency and consistency mechanisms, failure and recovery behavior, deployment and rollback, and the evidence supporting important claims.

Agent-generated framing is a proposal until it reflects the user's own intent or receives explicit approval. A passing test suite is evidence, not a substitute for acceptance.

## Choose audit or repair

Choose the mode from the user's request before changing files.

### Audit

When asked to assess, review, scan, or identify problems without implementing changes:

1. Name the concrete pattern.
2. Point to checkable evidence such as a file, symbol, test, command result, or observable behavior.
3. Explain the product, maintenance, reliability, security, or reviewer cost.
4. Suggest the smallest plausible correction.
5. Stop without mutating the repository.

Do not score how “AI-generated” the work seems or claim to know its author. Named patterns and evidence are useful; authorship guesses are not.

### Repair

When authorized to change the software:

1. Make the minimum effective change that satisfies the outcome contract.
2. Preserve strong existing code and intentional conventions.
3. Remove or justify every new abstraction, dependency, and operational obligation.
4. Run the applicable technical and craft checks.
5. Report exactly what changed, what was verified, and what remains uncertain.

Do not turn a repair into an unsolicited rewrite.

## Preserve the repository's voice

Before editing, observe the repository's vocabulary, domain model, module boundaries, language idioms, error-handling style, test style, comments, documentation, and accepted level of abstraction.

Preserve choices that are clear and intentional. Do not flatten distinctive, effective code into generic “clean” architecture or force every module into identical shapes. Change a convention only when the outcome contract, an invariant, repository instructions, or measured evidence justifies the cost.

Repository voice is not immunity from criticism. Name harmful conventions explicitly and resolve consequential changes through evidence or owner judgment.

## Software-slop catalog

Use these names to make findings concrete and checkable.

| Pattern | Observable signal | Preferred response |
| --- | --- | --- |
| **Vague guarantees** | Words such as robust, scalable, reliable, secure, or production-ready appear without a metric, boundary, or failure condition. | Convert the claim into observable behavior or label it unresolved. |
| **Abstraction theater** | Interfaces, factories, managers, layers, or patterns exist without a current consumer, variation, seam, or measured pressure. | Remove them or record the concrete need they satisfy. |
| **Generic naming** | Manager, service, handler, helper, processor, or changing synonyms hide the domain responsibility. | Use the domain term consistently and name the behavior performed. |
| **Scope drift** | Unrelated refactors, formatting churn, framework swaps, or dependency additions expand a focused change. | Revert or separate the drift; keep the smallest coherent diff. |
| **Shallow proof** | Tests mirror implementation, assert mocks, or cover only the happy path while missing behavior at a meaningful boundary. | Test observable contracts and the failures that threaten them. |
| **Missing hostile reality** | Relevant timeout, retry, duplication, reordering, concurrency, restart, migration, rollback, corruption, or recovery behavior is unspecified or untested. | Specify the behavior and add proportionate evidence. |
| **Evidence theater** | A summary claims all checks pass, cites performance numbers, or promises safety without a command result, artifact, source, or qualification. | Run and cite the check, or narrow the claim. |
| **Placeholder operations** | TODOs, generated diagrams, dashboards, runbooks, or rollback text look complete but cannot be executed. | Finish, remove, or mark them explicitly incomplete with an owner. |
| **Speculative future-proofing** | Unused extension points, configuration, compatibility layers, and boilerplate anticipate no accepted requirement. | Defer until a real constraint appears. |
| **Narrative overreach** | Polished summaries claim architecture, security, performance, or completeness beyond what the diff and evidence establish. | State only supported facts, decisions, and residual uncertainty. |
| **Comment noise** | Comments paraphrase syntax or narrate obvious control flow. | Delete them or explain intent, invariants, tradeoffs, and non-obvious hazards. |
| **Generated sameness** | Every component receives the same layering, paragraph shape, test template, or design pattern regardless of need. | Use the simplest local, idiomatic structure that expresses the actual responsibility. |

A finding should identify the pattern and its evidence. Avoid vague labels such as “messy,” “overengineered,” or “AI slop” without a mechanism and consequence.

## Craft gate

After technical validation, answer each applicable check with pass or fail. If a check fails, repair the work or record an explicit exception and owner before completion.

1. Does the result preserve the human-approved intent, non-goals, and authorization boundaries?
2. Is this the minimum effective change, with unrelated churn removed?
3. Does it preserve useful repository vocabulary, idioms, and intentional structure?
4. Are names, guarantees, and summaries concrete enough to verify?
5. Are factual, performance, security, and completion claims supported by sources or produced evidence?
6. Do tests exercise observable behavior rather than merely repeat the implementation or assert mocks?
7. Are material failure, concurrency, migration, recovery, and rollback paths covered to the selected risk level?
8. Is every new abstraction, dependency, configuration option, and operational obligation justified now?
9. Are comments and documentation complete, executable where appropriate, and focused on intent rather than narration?
10. Does the handoff accurately distinguish verified facts, inferences, decisions, and unresolved risk?
11. Can a sharp reviewer understand why the change exists and where to challenge it without reverse-engineering generated bulk?
12. Has the responsible human reviewed the load-bearing paths and accepted the result and residual risk?

Scale the gate with the selected risk mode. Lean work can use a focused self-check. Standard work should add a reviewer or independent challenge when practical. High-assurance work should combine this gate with adversarial review and production-like evidence.

## How the three perspectives fit

- Josh Bleecher Snyder's vertically integrated and differential-specification perspective helps discover which system decisions matter and resolve hidden choices across layers.
- The implementation-quality perspective, adapted from Solid Skills, challenges implementation structure, responsibilities, naming, testing, and maintainability.
- Peter Yang's craft perspective keeps human taste, voice, trust, and final accountability at the first and last mile.

Use all three without turning any of them into ritual. Explicit outcomes, safety and security invariants, repository instructions, language idioms, and evidence decide conflicts.

## Credits

This software-engineering adaptation is inspired by Peter Yang's [“Use My /No-AI-Slop Skill to Remove 20+ Patterns of AI Slop From Your Writing”](https://creatoreconomy.so/p/use-my-no-ai-slop-skill-to-remove-20-ai-slop-patterns) and the MIT-licensed [`petergyang/no-ai-slop`](https://github.com/petergyang/no-ai-slop) skill, inspected at commit [`61c21c3`](https://github.com/petergyang/no-ai-slop/commit/61c21c351da4dcb40946a11fead978f2078a2c65).

The source's separate detect/edit modes, minimum-effective-edit rule, voice preservation, prohibition on invented claims, named-pattern evidence, and pass/fail self-evaluation informed this reference. The 25/50/25 ownership model comes from Yang's accompanying essay. This reference creates a software-specific interpretation and catalog rather than reproducing the source skill's writing rules. See [attribution.md](attribution.md) for full credits and scope.

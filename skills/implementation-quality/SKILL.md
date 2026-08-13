---
name: implementation-quality
description: Apply context-sensitive TDD, SOLID, clean-code, object-design, testing, complexity, and architecture heuristics during implementation planning, coding, refactoring, debugging, or review. Use when the user requests implementation-quality guidance or when reliable-ai-coding or agentic-engineering invokes this companion perspective. Never override explicit behavior, safety, repository conventions, language idioms, compatibility, or measured evidence.
---

# Implementation Quality

Improve the cost of discovering, understanding, changing, testing, debugging, deploying, and operating software. Apply only the guidance that improves the stated outcome in the repository and language at hand.

## Precedence

Use three strengths of guidance:

1. **Required constraints:** stated behavior, security and safety invariants, authorization, repository instructions, compatibility, and evidence.
2. **Default practices:** focused tests around changed behavior, clear naming, cohesive responsibilities, minimal effective changes, and removal of accidental complexity.
3. **Scrutiny prompts:** strict test-first order, SOLID, value objects, object calisthenics, numerical size limits, design patterns, and architectural styles.

Do not treat a scrutiny prompt as an acceptance criterion. When a consequential conflict remains, resolve it through a focused test, benchmark, spike, or owner decision.

## Workflow

### 1. Establish behavior and risk

Identify the acceptance criteria, affected behavior, failure modes, compatibility constraints, and cheapest evidence that could disprove the implementation. For a tiny or mechanical change, keep this brief.

### 2. Choose a testing approach

Prefer a failing test first when behavior is clear and the test provides useful design feedback. Use characterization tests before changing unclear legacy behavior. For exploratory spikes, generated files, configuration, or hard-to-isolate integration work, choose the fastest reliable feedback loop and add durable tests before claiming completion when warranted.

Read [tdd.md](references/tdd.md) for test-first technique and [testing.md](references/testing.md) for test levels, doubles, and naming.

### 3. Make the minimum effective change

Preserve established vocabulary and structure unless they cause the problem. Prefer code that expresses intent, localizes change, and is easy to remove. Avoid speculative abstractions and unrelated cleanup.

Use SOLID as diagnostic questions rather than a demand for interfaces or classes:

- Does this unit have a coherent reason to change?
- Can required variation be added without risky churn?
- Do substitutions preserve observable contracts?
- Do consumers depend only on behavior they use?
- Does dependency direction protect policy from volatile details?

Read [solid-principles.md](references/solid-principles.md) when object-oriented boundaries or substitutability matter.

### 4. Review clarity and responsibility

Prefer consistent domain names, direct control flow, explicit boundaries, and cohesive modules. Treat long functions, deep nesting, broad classes, primitive obsession, and many dependencies as investigation signals—not automatic failures. Introduce value objects when they enforce meaningful validation, units, identity, or invariants; do not wrap primitives mechanically.

Read only the relevant reference:

- [clean-code.md](references/clean-code.md) for naming and local structure;
- [object-design.md](references/object-design.md) for object responsibilities and contracts;
- [code-smells.md](references/code-smells.md) for refactoring signals;
- [complexity.md](references/complexity.md) for change amplification and cognitive load.

### 5. Evaluate architecture proportionally

Keep related behavior together and dependencies legible. Introduce layers, ports, patterns, or vertical slices only when they reduce current change cost, isolate volatility, enforce a boundary, or enable required testing and operations.

Read [architecture.md](references/architecture.md) for system boundaries and [design-patterns.md](references/design-patterns.md) only when a recurring design problem needs a shared vocabulary.

### 6. Validate and simplify

Run the relevant checks. Confirm behavior, names, comments, and abstractions still match the result. Remove dead code and accidental complexity introduced by the change. Report evidence and limitations without overstating confidence.

## Review questions

Use the smallest relevant subset:

- Does the change satisfy concrete behavior and failure cases?
- Is the validation at the cheapest layer that provides confidence?
- Can a maintainer find and change the behavior without broad churn?
- Are names and boundaries consistent with the repository and domain?
- Does each abstraction pay for itself now?
- Are dependencies and side effects explicit enough to test and operate?
- Would a simpler representation preserve the same outcome?

Give findings with evidence, consequence, and the minimum effective correction. Avoid style-only churn and pattern enforcement detached from outcomes.

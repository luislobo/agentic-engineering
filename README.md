# Engineer Software With Agents

A reusable skill for designing and delivering nontrivial software systems with coding agents.

It turns underspecified product goals into explicit decisions, testable guarantees, independently explored alternatives, a clean keeper implementation, adversarial validation, and a controlled rollout. The goal is not merely to generate code, but to preserve human understanding of the system's invariants, failure behavior, and major tradeoffs.

The responsible human remains the author of intent and the acceptor of the result, even when agents perform much of the research, implementation, testing, and review.

## Three complementary perspectives

| Perspective | Primary concern |
| --- | --- |
| **Vertical decision engineering** | Outcomes, guarantees, hidden choices, failure behavior, architecture, evidence, rollout, and operational understanding, adapted from Josh Bleecher Snyder |
| **Solid implementation** | TDD, SOLID principles, clean code, object responsibilities, code smells, design patterns, and implementation structure, sourced from Solid Skills |
| **Human craft and anti-slop** | Human-owned intent and acceptance, minimum-effective changes, repository voice, checkable claims, reviewer trust, and a final craft gate, inspired by Peter Yang |

The perspectives answer different questions: what system should exist, how its implementation should be structured, and whether humans have exercised enough taste and judgment to trust the result. Explicit product outcomes, safety and security invariants, repository instructions, language idioms, and measured evidence decide conflicts.

## Human ownership, not a code quota

The integrated 25/50/25 model describes ownership and attention rather than a literal split of time or code:

1. **Human-shaped intent:** the responsible human states or approves the problem, desired outcome, non-goals, constraints, taste, and unacceptable failures.
2. **Agent-amplified execution:** agents research, explore, implement, test, compare, and review while surfacing consequential choices.
3. **Human-accepted result:** the responsible human inspects load-bearing paths and evidence, accepts residual risk, and decides whether to release.

The human does not need to read every line. They do need enough understanding of interfaces, data, security, concurrency, failure and recovery, rollout, and evidence to exercise judgment. See [human-craft-and-anti-slop.md](references/human-craft-and-anti-slop.md).

## When to use it

Use this skill for:

- greenfield systems and major subsystems;
- distributed, concurrent, security-sensitive, or data-critical software;
- architecture and failure-semantics decisions;
- work where reliability, recovery, compatibility, or rollout risk matters;
- production-ready delivery coordinated through coding agents.

It intentionally stays lightweight for small, isolated, reversible edits.

## Workflow

1. Preserve the human-shaped intent and establish a measurable outcome contract.
2. Research only facts that can change a decision.
3. Specify invariants and failure behavior before architecture.
4. Generate alternatives at a depth proportional to risk.
5. Compare their divergences to expose missing specification.
6. Build the minimum effective keeper from the matured decisions.
7. Validate technical behavior, operational readiness, and software craft.
8. Obtain human acceptance, roll out gradually, and transfer operational understanding.

See [SKILL.md](SKILL.md) for the complete workflow.

## Usage

Invoke the skill explicitly with a prompt such as:

```text
Use $engineer-software-with-agents to design and build this distributed event-processing system.
```

When durable engineering artifacts are appropriate, create them with:

```bash
python3 scripts/scaffold_engineering.py \
  --root <project-root> \
  --mode <lean|standard|high-assurance>
```

The scaffold utility does not overwrite existing files.

## Risk modes

| Mode | Best for | Typical depth |
| --- | --- | --- |
| Lean | Narrow, reversible work | One design plus a focused challenge |
| Standard | Significant features and subsystems | Multiple options and targeted implementation spikes |
| High assurance | High-blast-radius or critical systems | Independent implementations, differential analysis, and extensive validation |

See [risk-modes.md](references/risk-modes.md) for the selection criteria and required evidence.

## Repository structure

| Path | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Core agent workflow and completion gates |
| [agents/openai.yaml](agents/openai.yaml) | Skill interface metadata |
| [references/artifact-guide.md](references/artifact-guide.md) | Engineering artifact contracts |
| [references/differential-analysis.md](references/differential-analysis.md) | Alternative-comparison method |
| [references/risk-modes.md](references/risk-modes.md) | Risk-scaled operating modes |
| [references/human-craft-and-anti-slop.md](references/human-craft-and-anti-slop.md) | Human ownership model, audit and repair modes, software-slop catalog, and craft gate |
| [references/attribution.md](references/attribution.md) | Sources, credits, and scope of the adaptation |
| [scripts/scaffold_engineering.py](scripts/scaffold_engineering.py) | Non-overwriting project scaffold |
| [skills/solid/SKILL.md](skills/solid/SKILL.md) | Companion implementation-quality skill |
| [skills/solid/references](skills/solid/references) | SOLID, TDD, testing, clean-code, architecture, and design references |
| [skills/solid/agents/openai.yaml](skills/solid/agents/openai.yaml) | Companion skill interface metadata |

## Attribution

The vertically integrated and differential-specification workflow is adapted from Josh Bleecher Snyder's:

- [“Claude Is Not a Compiler”](https://blog.exe.dev/claude-is-not-a-compiler/)
- [“Differential Spec Analysis”](https://commaok.xyz/ai/differential-spec/)

The bundled Solid implementation perspective is sourced from [ramziddin/solid-skills](https://github.com/ramziddin/solid-skills) through [Luis Lobo's fork](https://github.com/luislobo/solid-skills).

The human-craft perspective is inspired by Peter Yang's [25/50/25 essay](https://creatoreconomy.so/p/use-my-no-ai-slop-skill-to-remove-20-ai-slop-patterns) and MIT-licensed [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) skill. This repository adapts its ownership, audit-versus-repair, minimum-effective-edit, voice-preservation, evidence, and self-evaluation ideas into a software-specific lens; it does not bundle the writing skill.

See [the full attribution](references/attribution.md) for pinned revisions, licensing notes, and the boundary between source material and this repository's extensions.

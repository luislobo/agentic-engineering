# Engineer Software With Agents

A reusable skill for designing and delivering nontrivial software systems with coding agents.

It turns underspecified product goals into explicit decisions, testable guarantees, independently explored alternatives, a clean keeper implementation, adversarial validation, and a controlled rollout. The goal is not merely to generate code, but to preserve human understanding of the system's invariants, failure behavior, and major tradeoffs.

## When to use it

Use this skill for:

- greenfield systems and major subsystems;
- distributed, concurrent, security-sensitive, or data-critical software;
- architecture and failure-semantics decisions;
- work where reliability, recovery, compatibility, or rollout risk matters;
- production-ready delivery coordinated through coding agents.

It intentionally stays lightweight for small, isolated, reversible edits.

## Workflow

1. Establish an outcome contract and measurable success criteria.
2. Research only facts that can change a decision.
3. Specify invariants and failure behavior before architecture.
4. Generate alternatives at a depth proportional to risk.
5. Compare their divergences to expose missing specification.
6. Build a clean keeper from the matured decisions.
7. Validate through tests, fault analysis, and adversarial review.
8. Roll out gradually and transfer operational understanding.

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
| [references/attribution.md](references/attribution.md) | Sources, credits, and scope of the adaptation |
| [scripts/scaffold_engineering.py](scripts/scaffold_engineering.py) | Non-overwriting project scaffold |

## Attribution

This workflow is adapted from Josh Bleecher Snyder's:

- [“Claude Is Not a Compiler”](https://blog.exe.dev/claude-is-not-a-compiler/)
- [“Differential Spec Analysis”](https://commaok.xyz/ai/differential-spec/)

The risk scaling, artifact contracts, safety gates, generalized comparison rubric, scaffold utility, and completion criteria are independent extensions. See [the full attribution](references/attribution.md).

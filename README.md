# Agentic Engineering

A portable plugin and skill pack for reliable daily AI coding and nontrivial software delivery while keeping permissions, consequential decisions, evidence, and final acceptance under human ownership.

Created and maintained by [Luis Lobo](https://github.com/luislobo).

This repository is currently distributed privately for Luis Lobo and explicitly authorized
collaborators. Portability refers to using the same skills across supported agent hosts; it does
not imply public availability or support. The package is MIT-licensed so authorized copies have
clear reuse terms and can preserve compatible third-party notices.

## What it contains

| Skill | Purpose |
| --- | --- |
| `agentic-engineering` | Risk-scaled system design and delivery: outcomes, invariants, alternatives, differential analysis, keeper implementation, adversarial validation, rollout, and handoff |
| `implementation-quality` | A complementary implementation lens covering TDD, SOLID, clean code, object responsibilities, code smells, patterns, testing, and local architecture |
| `reliable-ai-coding` | A daily AI-coding operating loop for precise task contracts, targeted context, bounded tools, objective verification, and efficient context reuse |
| `pr-readiness` | A strictly read-only pull-request readiness report |
| `pr-feedback-closure` | Approval-gated feedback triage, minimum-effective repairs, evidence-backed replies, verified resolution, and readiness reporting |

The workflow combines five distinct perspectives:

1. Josh Bleecher Snyder’s vertically integrated, differential agent engineering.
2. Ramziddin’s Solid Skills, integrated through Luis Lobo’s fork.
3. Peter Yang’s human-craft and 25/50/25 concepts, adapted from writing to software engineering.
4. Luis Lobo’s independently authored PR review lifecycle.
5. DeepLearning.AI and Anthropic’s course material on multimodal prompting, structured outputs,
   prompt caching, tool use, and computer use, adapted into a reliable AI-coding workflow.

They are not collapsed into one doctrine. Outcomes, safety, repository rules, language idioms, and measured evidence decide conflicts.

## Why this is a plugin

Each workflow is a self-contained Agent Skill. The plugin is the distribution layer: it installs the related skills as one versioned package and adds only the metadata each host requires.

No custom MCP server is bundled. GitHub work uses the host’s connected GitHub integration first, then a local `gh`/GraphQL fallback only when a required capability is missing. That keeps authentication and authorization in the host instead of hiding them in this package. A GitHub Copilot subscription is not required for the core skills or PR lifecycle.

## Install

The repository is private, so the selected client must be able to authenticate to GitHub.

### Codex

```bash
codex plugin marketplace add luislobo/agentic-engineering
codex plugin add agentic-engineering@luislobo-agentic-engineering
```

Start a new session after installation, then invoke a skill such as:

```text
Use $agentic-engineering to design and build this distributed system.
```

For an everyday feature, bug, refactor, or prompt-improvement task:

```text
Use $reliable-ai-coding to define the task contract, work within bounded permissions,
and return objective verification evidence.
```

Use one primary skill per task. `reliable-ai-coding` is the default for ordinary code changes;
`agentic-engineering` replaces it for consequential architecture or high-risk work.
`implementation-quality` is the optional companion lens. PR readiness and feedback closure remain
separate read-only and mutating workflows. See [skill selection and prompt recipes](docs/SKILL_RECIPES.md).

### Claude Code

```bash
claude plugin marketplace add luislobo/agentic-engineering
claude plugin install agentic-engineering@luislobo-agentic-engineering
```

Claude plugin skills are namespaced, for example:

```text
/agentic-engineering:agentic-engineering
```

### GitHub Copilot CLI

Copilot CLI is an optional supported host, not a dependency. Install this package there only when
the project has Copilot access:

```bash
copilot plugin install luislobo/agentic-engineering
```

Confirm installation with `copilot plugin list` and inspect loaded skills with `/skills list`.

### GitHub.com review integrations

Use the review agent that is actually configured for the repository:

- **Codex:** connect the repository to Codex Cloud, enable Code Review, then comment
  `@codex review` on the pull request. Codex reads applicable `AGENTS.md` review rules and posts a
  standard GitHub review.
- **Another coding agent:** use that agent's documented GitHub review trigger or app workflow.
  Do not assume that its mention syntax matches Codex.
- **No connected review agent:** inspect the pull request with an authenticated local checkout and
  `gh`/GraphQL where needed. Treat repository-required human approvals, branch protection, and CI
  as the authority. Missing required evidence produces **Unknown**.

Agent review is additional evidence; it does not replace tests, CI, branch protection, or required
human approvals. Readiness remains read-only, feedback changes require explicit authorization, and
merge requires a separate request. See [GitHub review without a Copilot dependency](docs/GITHUB_REVIEW.md).

### Google Antigravity 2

Antigravity consumes the open Agent Skills format rather than the Codex, Claude, or Copilot plugin manifests:

```bash
npx skills add luislobo/agentic-engineering --agent=antigravity
```

For a workspace-only installation, run the command from that project. Antigravity’s workspace discovery location is `.agents/skills/`.

## Operating model

The integrated 25/50/25 model is about ownership, not a literal time or code quota:

1. **Human-shaped intent:** a responsible person states or approves the outcome, constraints, non-goals, taste, and unacceptable failures.
2. **Agent-amplified execution:** agents research, compare, implement, test, challenge, and document consequential choices.
3. **Human-accepted result:** a responsible person inspects load-bearing paths and evidence, accepts residual risk, and decides whether to release.

For significant work, the main workflow:

1. establishes an outcome contract;
2. researches decision-changing facts;
3. specifies invariants and failure behavior;
4. creates risk-scaled alternatives;
5. compares divergences to expose missing specification;
6. builds a clean keeper;
7. validates behavior and craft adversarially;
8. closes review feedback when applicable;
9. stages rollout and transfers operational understanding.

## Safety boundaries

- A status request is read-only.
- Review feedback is classified before any repair.
- Mutating PR work pauses for disposition approval.
- Production changes require explicit authorization immediately before action.
- A merge always requires a separate explicit request.
- Missing evidence produces **Unknown**, not an optimistic readiness claim.

## Repository structure

```text
skills/                    canonical, self-contained Agent Skills
.codex-plugin/plugin.json  Codex package metadata
.agents/plugins/           Codex repository marketplace
.claude-plugin/            Claude manifest and marketplace
plugin.json                GitHub Copilot CLI manifest
docs/                      compatibility contract and decisions
scripts/                   distribution validation
tests/                     safety and structure checks
AGENTS.md                  canonical repository-development instructions
CLAUDE.md                  Claude Code import of AGENTS.md
.github/copilot-instructions.md  generated Copilot repository instructions
```

See [the compatibility contract](docs/COMPATIBILITY.md), [the design decisions](docs/DECISIONS.md), and [the full notices](NOTICE.md).

## Quality controls

Run:

```bash
python3 scripts/validate_distribution.py
python3 -m unittest discover -s tests -v
python3 scripts/evaluate_behavior.py
```

CI repeats these checks and validates every skill plus the Codex and Claude package contracts. The validator rejects:

- broken or escaping local links;
- non-portable canonical frontmatter;
- duplicated or mismatched skill names;
- unsupported OpenAI metadata;
- drift between manifests;
- unsafe PR trigger language;
- platform-specific assumptions in canonical workflows;
- missing credits or required package files.
- drift between generated self-contained references;
- missing MIT and third-party license notices;
- context-free implementation absolutes and main-skill context-budget regressions;
- malformed or incomplete behavioral eval definitions.

Structural checks prove that the package is internally consistent. They do not prove that the
workflow changes agent behavior. See [the behavioral evaluation protocol](docs/EVALUATION.md) for
fresh-session baseline/treatment trials, hard authorization gates, blind rubric scoring, and
token/tool/time measurement.

## License

Luis Lobo's original work is available under the [MIT License](LICENSE). Adapted MIT material and
methodological inspirations are documented in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md),
[NOTICE.md](NOTICE.md), and the skill-level attribution references.

## Credits

- [Josh Bleecher Snyder, “Claude Is Not a Compiler”](https://blog.exe.dev/claude-is-not-a-compiler/)
- [Josh Bleecher Snyder, “Differential Spec Analysis”](https://commaok.xyz/ai/differential-spec/)
- [ramziddin/solid-skills](https://github.com/ramziddin/solid-skills) and [luislobo/solid-skills](https://github.com/luislobo/solid-skills)
- [Peter Yang’s 25/50/25 essay](https://creatoreconomy.so/p/use-my-no-ai-slop-skill-to-remove-20-ai-slop-patterns) and [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)
- Luis Lobo’s independently authored PR review lifecycle
- DeepLearning.AI and Anthropic’s *Building Toward Computer Use with Anthropic*, taught by Colt Steele and introduced by Andrew Ng

See [NOTICE.md](NOTICE.md), the [agentic-engineering attribution](skills/agentic-engineering/references/attribution.md), and the [reliable-ai-coding attribution](skills/reliable-ai-coding/references/attribution.md) for pinned revisions, adaptation boundaries, and licensing notes.

# Distribution decisions

## Outcome

Ship one maintainable skill pack for reliable daily AI coding and nontrivial engineering across Codex, Claude Code, GitHub Copilot CLI, and Google Antigravity 2 without duplicating behavioral instructions or weakening authorization gates.

## Options compared

### One universal manifest

Rejected. The hosts use different manifest paths and schemas. A root file suitable for Copilot is not the Codex manifest, and Antigravity’s documented portable path is the Agent Skills format.

### Four copied implementations

Rejected. Copies would drift in safety rules, credits, and review behavior. A fix could reach one host while leaving another unsafe or stale.

### Shared skills with thin platform packages

Selected. `skills/` is the keeper. Codex, Claude, and Copilot receive host-specific manifests. Antigravity uses the same open skills directly. All hosts consume the same five canonical skill identifiers; no platform retains a second workflow copy.

## Consequential resolutions

- **Plugin versus standalone skills:** use both layers. Skills define behavior; plugins distribute the related set.
- **GitHub tooling:** do not bundle a new MCP server or require Copilot. Prefer the configured host's authenticated GitHub integration. Codex uses `@codex review`; Claude managed Code Review uses `@claude review`; a Claude GitHub Action uses `@claude <request>`; and Antigravity requires an SDK-backed GitHub Action with an automatic or repository-defined trigger. Use authenticated `gh`/GraphQL for missing read capabilities, and report Unknown when required evidence remains unavailable.
- **PR safety:** separate read-only `pr-readiness` from mutating `pr-feedback-closure`; disable implicit Codex invocation for the mutating skill and require explicit intent in every host.
- **Canonical metadata:** use only portable `name` and `description` in `SKILL.md`. Host-only fields live in host manifests or compatibility commands.
- **Antigravity packaging:** support the documented Agent Skills install and workspace path; do not invent a custom public plugin schema.
- **Licensing:** distribute Luis Lobo's original work under MIT; preserve compatible upstream MIT
  notices and distinguish cited methodology from copied expression.
- **Naming:** use outcome-oriented, low-collision identifiers: `agentic-engineering`, `implementation-quality`, `reliable-ai-coding`, `pr-readiness`, and `pr-feedback-closure`.
- **Daily AI-coding workflow:** keep prompt design, context selection, tool boundaries, verification, and efficiency in `reliable-ai-coding`; defer high-assurance architecture to `agentic-engineering` and implementation craft to `implementation-quality`.
- **Skill orchestration:** choose one primary workflow; use `implementation-quality` as the
  optional companion lens, escalate rather than stack overlapping workflows, and keep read-only
  PR readiness separate from mutating feedback closure.
- **Release version:** treat the identifier and repository rename as the breaking `2.0.0` release and require manifest version lockstep.

## Residual risks

- A platform update can change validation or installation behavior.
- Private-repository installation depends on the client’s Git credentials and organization policy.
- Runtime smoke tests require the corresponding CLI and account; CI performs deterministic package checks even when a vendor CLI is unavailable.
- The implementation-quality material adapted from Solid Skills contains intentionally strong defaults. The main skill explicitly subordinates them to outcomes, safety, repository conventions, language idioms, and evidence.
- Behavioral evals require external agent runs; CI validates case and trace contracts but cannot
  establish effectiveness without recorded baseline/treatment trials.

## Instruction design

- The main skill exposes three non-negotiable gates and a concise risk-scaled workflow.
- Detailed lenses load only when their decision context applies.
- Implementation-quality uses required constraints, default practices, and scrutiny prompts
  instead of issuing absolutes that another skill must reinterpret.
- PR lifecycle duplication remains necessary for independently installable skills, so
  pr-feedback-closure owns the canonical reference and CI verifies the generated copy.

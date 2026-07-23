# Distribution decisions

## Outcome

Ship one maintainable engineering workflow across Codex, Claude Code, GitHub Copilot CLI, and Google Antigravity 2 without duplicating behavioral instructions or weakening authorization gates.

## Options compared

### One universal manifest

Rejected. The hosts use different manifest paths and schemas. A root file suitable for Copilot is not the Codex manifest, and Antigravity’s documented portable path is the Agent Skills format.

### Four copied implementations

Rejected. Copies would drift in safety rules, credits, and review behavior. A fix could reach one host while leaving another unsafe or stale.

### Shared skills with thin platform packages

Selected. `skills/` is the keeper. Codex, Claude, and Copilot receive host-specific manifests. Antigravity uses the same open skills directly. All hosts consume the same four canonical skill identifiers; no platform retains a second workflow copy.

## Consequential resolutions

- **Plugin versus standalone skills:** use both layers. Skills define behavior; plugins distribute the related set.
- **GitHub tooling:** do not bundle a new MCP server. Prefer each host’s authenticated GitHub integration and use `gh`/GraphQL only for missing capabilities.
- **PR safety:** separate read-only `pr-readiness` from mutating `pr-feedback-closure`; disable implicit Codex invocation for the mutating skill and require explicit intent in every host.
- **Canonical metadata:** use only portable `name` and `description` in `SKILL.md`. Host-only fields live in host manifests or compatibility commands.
- **Antigravity packaging:** support the documented Agent Skills install and workspace path; do not invent a custom public plugin schema.
- **Licensing:** preserve source notices and authorization boundaries without asserting a new blanket license over third-party material.
- **Naming:** use outcome-oriented, low-collision identifiers: `agentic-engineering`, `implementation-quality`, `pr-readiness`, and `pr-feedback-closure`.
- **Release version:** treat the identifier and repository rename as the breaking `2.0.0` release and require manifest version lockstep.

## Residual risks

- A platform update can change validation or installation behavior.
- Private-repository installation depends on the client’s Git credentials and organization policy.
- Runtime smoke tests require the corresponding CLI and account; CI performs deterministic package checks even when a vendor CLI is unavailable.
- The implementation-quality material adapted from Solid Skills contains intentionally strong defaults. The main skill explicitly subordinates them to outcomes, safety, repository conventions, language idioms, and evidence.

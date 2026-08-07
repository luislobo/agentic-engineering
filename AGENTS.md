# Repository instructions

## Scope

Maintain one portable set of self-contained skills for Codex, Claude Code, GitHub Copilot CLI,
and compatible Agent Skills hosts. Host manifests distribute behavior; they must not redefine it.

## Required workflow

- Preserve authorization boundaries. Do not merge, deploy, publish, or mutate production without
  a separate explicit request.
- Treat review or status-only requests as read-only.
- For PR review work, always retrieve and inspect suppressed review material when the host exposes
  it, including resolved, outdated, minimized, collapsed, and hidden-by-default comments.
- Keep every skill independently installable: a skill may link only within its own directory.
- Keep plugin names and versions in lockstep across manifests and marketplaces.
- Preserve the MIT license, third-party notices, pinned source revisions, and adaptation boundaries.
- Do not add private organizational provenance to documentation, history, validation, or credits.

## Skill design

- Keep SKILL.md concise and reserve it for essential workflow and routing.
- Load detailed references conditionally and avoid duplicating instructions between a skill and its
  references.
- Distinguish required constraints, default practices, and scrutiny prompts. Do not introduce
  context-free engineering absolutes.
- Scale ceremony to risk and update behavioral eval cases when changing a safety or workflow
  contract.

## Generated content

skills/pr-feedback-closure/references/lifecycle.md is canonical.
skills/agentic-engineering/references/pr-feedback-closure.md is generated for self-contained
distribution. Run:

    python3 scripts/sync_shared_references.py

.github/copilot-instructions.md is generated from this file. Run:

    python3 scripts/sync_agent_instructions.py

## Validation

Before committing, run:

    python3 scripts/sync_shared_references.py --check
    python3 scripts/sync_agent_instructions.py --check
    python3 scripts/evaluate_behavior.py
    python3 scripts/validate_distribution.py
    python3 -m unittest discover -s tests -v

Keep changes focused and preserve unrelated work.

# Changelog

## 2.1.0 - Unreleased

- Add the self-contained `reliable-ai-coding` skill for precise task contracts, targeted context,
  bounded tool use, objective verification, multimodal inputs, and efficient prompt reuse.
- Add prompt recipes, a tool and caching guide, a 30-day practice plan, and a review scorecard
  adapted from the supplied *Building Toward Computer Use with Anthropic* subtitles.
- Extend package validation, tests, documentation, and behavioral evals for the fifth skill.
- Add a behavioral evaluation contract for proportionality, evidence, and authorization.
- Reduce the main skill through progressive disclosure and explicit hard gates.
- Recast implementation-quality absolutes as defaults and scrutiny prompts.
- Generate and verify the duplicated PR lifecycle reference.
- License original work under MIT and preserve compatible third-party notices.
- Add negative tests for drift, instruction conflicts, and missing licensing.
- Require PR workflows to retrieve and inspect suppressed review material.
- Add native Codex, Claude Code, and Copilot repository instruction entry points generated from
  one AGENTS.md source.

## 2.0.0 — 2026-07-23

- Rename the repository and plugin to `agentic-engineering`.
- Rename the skills to `agentic-engineering`, `implementation-quality`, `pr-readiness`, and `pr-feedback-closure`.
- Remove the old EPIC command aliases so every supported host exposes the same canonical names.
- Update all manifests, marketplaces, documentation, tests, installation commands, and cross-skill references.

## 1.0.0 — 2026-07-23

- Package four self-contained skills from one canonical `skills/` tree.
- Add validated Codex and Claude plugin manifests and marketplaces.
- Add a GitHub Copilot CLI plugin manifest.
- Add Antigravity 2 installation through the open Agent Skills format.
- Split read-only PR status from approval-gated PR review closure.
- Add automated distribution, safety, link, and metadata checks.

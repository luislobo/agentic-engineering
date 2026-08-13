# Attribution

## Vertically integrated agent engineering

The central inspiration for the system-level workflow is:

- Josh Bleecher Snyder, [“Claude Is Not a Compiler”](https://blog.exe.dev/claude-is-not-a-compiler), exe.dev blog, July 20, 2026.
- Josh Bleecher Snyder, [“Differential Spec Analysis”](https://commaok.xyz/ai/differential-spec/).

The source article describes using agents across strategy, domain research, architecture, implementation, testing, adversarial review, comparison of independent implementations, production de-risking, and concise decision documentation. It introduces the distributed DNS case study from which this skill's core build–compare–codify–repeat pattern was extracted.

This skill paraphrases that process and independently adds:

- explicit risk-scaled operating modes;
- artifact contracts and a scaffold utility;
- authorization and production safety gates;
- decision classification and completion gates;
- a generalized comparison rubric;
- traceability, rollout, and handoff requirements.

## Bundled Solid perspective

The companion implementation-quality perspective is sourced from:

- Ramziddin, [ramziddin/solid-skills](https://github.com/ramziddin/solid-skills).
- Luis Lobo's fork, [luislobo/solid-skills](https://github.com/luislobo/solid-skills), captured at commit [8c223a0](https://github.com/luislobo/solid-skills/commit/8c223a0ca0551f575ea1cd820cefbb15164be516).

The implementation-quality skill and its nine supporting references preserve the source's
engineering topics while recasting universal mandates as context-sensitive defaults and scrutiny
prompts. Explicit outcomes, system invariants, repository conventions, language idioms,
compatibility, and evidence take precedence.

The source README identifies Solid Skills as MIT-licensed. No separate license file was present in the source repository at the captured commit.

## Human craft and anti-slop perspective

The human-ownership and craft lens is inspired by:

- Peter Yang, [“Use My /No-AI-Slop Skill to Remove 20+ Patterns of AI Slop From Your Writing”](https://creatoreconomy.so/p/use-my-no-ai-slop-skill-to-remove-20-ai-slop-patterns), Behind the Craft, July 22, 2026.
- Peter Yang, [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop), inspected at commit [61c21c3](https://github.com/petergyang/no-ai-slop/commit/61c21c351da4dcb40946a11fead978f2078a2c65).

The source mechanisms adapted here are:

- the 25/50/25 framing in which human taste shapes the beginning, AI assists the middle, and human review owns the end;
- separate detect and edit modes;
- minimum-effective edits;
- preservation of the author's voice;
- named-pattern evidence instead of unreliable authorship detection;
- prohibition on invented claims, examples, or statistics;
- pass/fail self-evaluation followed by repair.

This repository reinterprets those mechanisms for software engineering. It adds a software-specific catalog of vague guarantees, abstraction theater, generic naming, scope drift, shallow proof, missing failure semantics, evidence theater, placeholder operations, speculative future-proofing, narrative overreach, comment noise, and generated sameness. It does not reproduce or bundle the source writing skill.

The source repository is licensed under the MIT License, copyright © 2026 Peter Yang. The pinned [SKILL.md](https://github.com/petergyang/no-ai-slop/blob/61c21c351da4dcb40946a11fead978f2078a2c65/SKILL.md), [eval.md](https://github.com/petergyang/no-ai-slop/blob/61c21c351da4dcb40946a11fead978f2078a2c65/eval.md), and [LICENSE](https://github.com/petergyang/no-ai-slop/blob/61c21c351da4dcb40946a11fead978f2078a2c65/LICENSE) are linked for provenance.

## Pull-request review closure

Luis Lobo independently authored the PR review lifecycle. It contributes:

- a read-only PR status and merge-readiness view;
- unresolved-thread retrieval and stable identifier tracking;
- ACCEPT and REJECT classification;
- a human approval pause before edits;
- coherent review-driven changes and relevant validation;
- replies in the original review threads;
- thread resolution followed by a zero-unresolved verification;
- an optional fresh connected-agent review.

This repository packages the lifecycle as portable, outcome-oriented Agent Skills for Codex,
Claude Code, GitHub Copilot CLI, and Google Antigravity 2. Canonical workflows prefer the host's
connected GitHub integration and use GitHub CLI or GraphQL only for missing capabilities. Every
host uses the same lifecycle.

The adaptation adds OWNER DECISION escalation, an Unknown verdict for incomplete evidence, separate merge authorization, repository-defined checks instead of an npm assumption, conditional rather than automatic inline comments for rejected feedback, and installers that verify but do not automatically install system dependencies.

Luis Lobo distributes the lifecycle under the repository MIT License.

No endorsement is claimed from Josh Bleecher Snyder, exe.dev, Ramziddin, Peter Yang, Behind the
Craft, or other referenced third parties.

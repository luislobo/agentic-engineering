# Compatibility contract

The canonical source of behavior is `skills/*/SKILL.md` plus files contained inside each skill directory. Platform manifests may expose those skills, but they must not redefine the workflow.

## Cross-platform invariants

1. Every skill is independently installable and self-contained.
2. Canonical skill frontmatter contains only `name` and `description`.
3. A canonical skill never links outside its own directory.
4. Platform-specific tool routing is expressed as capability selection, not a hard dependency on one host’s tool names.
5. Read-only PR status and mutating review closure remain separate skills.
6. Mutating review closure requires an explicit user request and approval of dispositions before edits.
7. No workflow merges or changes production without separate explicit authorization.
8. Every manifest exposes the same canonical `skills/` tree.
9. Skills use the same outcome-oriented identifiers on every host.
10. Credits and adaptation boundaries remain visible in the distributed package.
11. Host-required Markdown remains the portable runtime format; alternative source
    representations must generate or verify equivalent self-contained skills.
12. Intentionally duplicated safety references have one declared canonical source and are
    byte-verified in CI.
13. Repository-development guidance uses AGENTS.md as canonical, CLAUDE.md as a native import, and
    a generated Copilot repository instruction file; symlinks are not required.
14. GitHub Copilot is an optional host, never a runtime dependency. GitHub review selects the
    configured connected agent, uses its documented trigger, and falls back to authenticated
    `gh`/GraphQL inspection when connector coverage is insufficient.

## Platform mapping

| Platform | Package entry point | Skill discovery | Notes |
| --- | --- | --- | --- |
| Codex | `.codex-plugin/plugin.json` | `skills/` | Rich plugin metadata and repo marketplace in `.agents/plugins/marketplace.json` |
| Claude Code | `.claude-plugin/plugin.json` | `skills/` | Marketplace in `.claude-plugin/marketplace.json`; plugin skills are namespaced by `agentic-engineering` |
| GitHub Copilot CLI | `plugin.json` | `skills/` | Uses the root manifest required by Copilot CLI |
| Google Antigravity 2 | Agent Skills installer or `.agents/skills/` in the consuming workspace | `SKILL.md` packages | No repository-specific custom plugin schema is assumed |

## GitHub.com review mapping

Packaging support and GitHub review integration are separate concerns. A project can use the
skills through Codex, Claude Code, or Antigravity without a Copilot subscription.

| Available capability | Review path |
| --- | --- |
| Codex Code Review configured | Comment `@codex review` or use configured automatic reviews |
| Claude managed Code Review configured | Comment `@claude review`; use `@claude review always` to subscribe subsequent pushes |
| Claude Code GitHub Action in interactive mode | Comment `@claude <review request>` when comment events are configured and no prompt input is set |
| Claude Code GitHub Action in automation mode | Run the configured prompt or review plugin on selected PR events; it does not wait for a mention |
| Antigravity review automation configured | Use its GitHub Action automatically or a documented repository-defined trigger such as `/review`; no universal mention exists |
| Another connected coding agent configured | Use that provider's documented GitHub review trigger |
| No connected review agent | Use authenticated local checkout plus `gh`/GraphQL for available evidence; rely on repository-required human review and CI |

No path may invent missing checks, approvals, or thread state. Required evidence that cannot be
retrieved yields **Unknown**. See [GITHUB_REVIEW.md](GITHUB_REVIEW.md).

## Why the manifests differ

The hosts agree on the Agent Skills directory format but use different package schemas and installation flows. A universal manifest would either omit useful metadata or contain fields rejected by another host. The keeper therefore shares behavior and splits only packaging.

## Official documentation reviewed

- Codex: [Build plugins](https://learn.chatgpt.com/docs/build-plugins) and [Build skills](https://learn.chatgpt.com/docs/build-skills)
- Codex GitHub review: [Review GitHub pull requests with Codex](https://learn.chatgpt.com/docs/third-party/github)
- Claude Code: [Create plugins](https://code.claude.com/docs/en/plugins), [Plugins reference](https://code.claude.com/docs/en/plugins-reference), and [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- Claude GitHub review: [Code Review](https://code.claude.com/docs/en/code-review) and [GitHub Actions](https://code.claude.com/docs/en/github-actions)
- GitHub Copilot CLI: [Creating a plugin](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating) and [Plugin concepts](https://docs.github.com/en/copilot/concepts/agents/about-plugins)
- GitHub Actions security: [Workflow permissions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#permissions) and [secure use of `pull_request_target`](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target)
- Google Antigravity 2: [Antigravity skills codelab](https://codelabs.developers.google.com/getting-started-agy-ide#10), [Antigravity CLI and SDK code review](https://codelabs.developers.google.com/agy-cli-sdk-code-review), and [Firebase Agent Skills installation](https://firebase.google.com/docs/ai-assistance/agent-skills)

Documentation was reviewed on 2026-08-13. Platform schemas can change; update the compatibility tests and this contract together.

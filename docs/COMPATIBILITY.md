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

## Platform mapping

| Platform | Package entry point | Skill discovery | Notes |
| --- | --- | --- | --- |
| Codex | `.codex-plugin/plugin.json` | `skills/` | Rich plugin metadata and repo marketplace in `.agents/plugins/marketplace.json` |
| Claude Code | `.claude-plugin/plugin.json` | `skills/` | Marketplace in `.claude-plugin/marketplace.json`; plugin skills are namespaced by `agentic-engineering` |
| GitHub Copilot CLI | `plugin.json` | `skills/` | Uses the root manifest required by Copilot CLI |
| Google Antigravity 2 | Agent Skills installer or `.agents/skills/` in the consuming workspace | `SKILL.md` packages | No repository-specific custom plugin schema is assumed |

## Why the manifests differ

The hosts agree on the Agent Skills directory format but use different package schemas and installation flows. A universal manifest would either omit useful metadata or contain fields rejected by another host. The keeper therefore shares behavior and splits only packaging.

## Official documentation reviewed

- Codex: [Build plugins](https://learn.chatgpt.com/docs/build-plugins) and [Build skills](https://learn.chatgpt.com/docs/build-skills)
- Claude Code: [Create plugins](https://code.claude.com/docs/en/plugins), [Plugins reference](https://code.claude.com/docs/en/plugins-reference), and [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- GitHub Copilot CLI: [Creating a plugin](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating) and [Plugin concepts](https://docs.github.com/en/copilot/concepts/agents/about-plugins)
- Google Antigravity 2: [Antigravity skills codelab](https://codelabs.developers.google.com/getting-started-agy-ide#10) and [Firebase Agent Skills installation](https://firebase.google.com/docs/ai-assistance/agent-skills)

Documentation was reviewed on 2026-07-23. Platform schemas can change; update the compatibility tests and this contract together.

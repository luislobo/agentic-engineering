# GitHub review without a Copilot dependency

GitHub Copilot is optional. The review lifecycle selects the authenticated capability available
for the repository; it does not require every project to buy or enable the same coding agent.

## Capability order

1. Use the configured connected coding agent for structured GitHub review.
2. Use an authenticated local checkout plus `gh` or GraphQL when the connected integration cannot
   expose required read-only evidence such as unresolved thread state or Actions logs.
3. Rely on repository-required human approvals, branch protection, and CI for gates that no coding
   agent owns.
4. Report **Unknown** when required checks, approvals, conflicts, or thread state remain unavailable
   or stale. Never infer a green result from missing evidence.

## Codex on GitHub.com

Prerequisites:

- Codex Cloud is set up for the repository.
- Code Review is enabled in Codex settings.
- The requester has permission to comment on the pull request.

To request a review, add this exact pull-request comment:

```text
@codex review
```

For a one-off focus, append the scope to the same comment, for example:

```text
@codex review for failure handling in the database migration
```

Codex reads the pull-request diff and applicable `AGENTS.md` review rules, then posts a standard
GitHub review. Automatic Codex reviews may be enabled in repository settings instead. Agent review
is additional evidence; it does not replace tests, deterministic CI, branch protection, or required
human approval.

## Other agents

Use the active agent's documented GitHub app, review request, or comment trigger. Do not invent a
mention or translate `@codex review` to another provider by analogy. If the integration cannot be
verified as installed and configured, use the local authenticated fallback and state the gap.

## Local authenticated fallback

Use the smallest read-only commands needed for evidence, for example:

```bash
gh pr view <number> --repo <owner/repo>
gh pr checks <number> --repo <owner/repo>
gh pr diff <number> --repo <owner/repo>
```

Use GitHub GraphQL when unresolved review-thread state is required and the connected integration or
CLI command does not expose it. Do not claim complete comment or check coverage unless it was
actually retrieved. Local tools inspect and report evidence; they do not create an independent
agent review.

## Authorization boundaries

- `pr-readiness` is read-only. It may inspect an existing Codex or other agent review, but it does
  not post `@codex review`, request reviewers, rerun checks, edit, reply, resolve, or merge.
- `pr-feedback-closure` may request a fresh connected-agent review only when the user authorized
  that review action and the integration is configured.
- Editing, pushing, replying, resolving, changing PR metadata, and rerunning checks each require
  authorization appropriate to the request.
- Merge always requires a separate explicit request, even after a Ready verdict.

## Repository setup

Keep review guidance provider-neutral in `AGENTS.md`: describe consequential behavior to protect,
the unsafe outcome, and the safe path. Leave formatting, lint, and other deterministic checks in CI.
Provider-specific setup belongs in integration documentation or repository settings, not in the
portable skill workflow.

Official Codex setup and trigger details: [Review GitHub pull requests with Codex](https://learn.chatgpt.com/docs/third-party/github).

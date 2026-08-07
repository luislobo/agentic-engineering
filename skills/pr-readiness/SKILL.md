---
name: pr-readiness
description: Inspect a GitHub pull request without changing it and report merge readiness from current metadata, checks, approvals, conflicts, and unresolved review threads. Use when the user asks whether a PR is ready, what is blocking it, whether checks passed, or for a read-only PR review summary. Never edit code, reply, resolve threads, request reviews, rerun checks, or merge.
---

# Pull Request Readiness

## Objective

Produce a trustworthy, read-only readiness report for one exact pull request and head revision.

## Safety boundary

This skill never mutates the repository or pull request. Do not:

- edit files or push commits;
- reply to or resolve review threads;
- request reviewers;
- rerun or cancel checks;
- change labels, assignees, draft state, or metadata;
- merge or close the pull request.

If the user asks to address review feedback, stop the readiness workflow and use `$pr-feedback-closure` when that companion skill is installed.

## Workflow

1. Resolve the exact repository and pull-request number. Record the current head SHA.
2. Read repository instructions and branch-protection or policy information available to the host.
3. Gather:
   - title, author, state, base and head branches, draft state, and URL;
   - mergeability and conflicts;
   - required and observed checks, including pending, skipped, cancelled, and failing checks;
   - approvals, active changes-requested reviews, and required reviewer state;
   - total and unresolved review threads, with a concise summary of each unresolved concern;
   - suppressed review material, including resolved, outdated, minimized, collapsed, and
     hidden-by-default comments, using it as context without counting it as unresolved;
   - repository-specific policy blockers.
4. Prefer the host agent's connected GitHub integration. Use local GitHub CLI or GraphQL only when read-only connector coverage is insufficient, especially for unresolved-thread state or Actions logs.
5. Always read suppressed review material when the host exposes it. Do not infer missing state. If
   access or synchronization prevents complete comment coverage or another reliable conclusion,
   identify the unavailable evidence.
6. Report one verdict:
   - **Ready to merge**: every applicable readiness condition is known to pass.
   - **Blocked**: at least one concrete blocker is present.
   - **Unknown**: required evidence is unavailable or stale.

## Readiness gate

Report **Ready to merge** only when all applicable conditions are known:

- the pull request is open and not a draft;
- it is mergeable and has no unresolved conflict;
- required checks pass;
- required approvals are present;
- no active changes-requested review blocks it;
- no material unresolved review thread remains;
- repository-specific policy gates pass.

Never merge because the report says Ready.

## Output

Lead with the verdict. Include the repository, PR number, and head SHA, then list:

- checks and approvals;
- conflicts and draft state;
- unresolved threads;
- policy blockers;
- missing evidence;
- the smallest next action, without performing it.

## Credit

This read-only status workflow was independently authored by Luis Lobo and is distributed under
the repository MIT License.

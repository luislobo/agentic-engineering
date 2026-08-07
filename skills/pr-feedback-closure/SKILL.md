---
name: pr-feedback-closure
description: Close pull-request feedback through unresolved-thread triage, human-approved dispositions, minimum-effective repairs, validation, evidence-backed in-thread replies, verified resolution, and a final merge-readiness verdict. Use only when the user explicitly asks to address, reply to, or resolve PR review comments. For read-only readiness checks, use the pr-readiness skill instead. Do not merge without separate explicit authorization.
---

# PR Feedback Closure

## Objective

Close the review loop without confusing activity with resolution. Keep every material thread traceable from concern to disposition, evidence, reply, current resolution state, and merge-readiness impact.

Read [the canonical lifecycle](references/lifecycle.md) before changing a pull request.

## Core rules

- Resolve the exact repository, pull-request number, and current head revision before acting.
- Treat status checks as read-only. Do not turn a status request into edits, replies, resolutions, review requests, or merges.
- In address-feedback mode, triage first and stop for approval of the dispositions before editing.
- Use **ACCEPT**, **REJECT**, or **OWNER DECISION**. Do not hide ambiguity inside ACCEPT.
- Make the minimum effective repair and follow repository instructions for tests, commits, and documentation.
- Reply in the original thread with checkable evidence.
- Keep thread IDs, comment database IDs, and commit or evidence references distinct.
- Resolve only after the concern is addressed and repository policy permits it.
- Re-query current thread and check state after mutations.
- Report **Ready to merge**, **Blocked**, or **Unknown** from current evidence.
- Never merge without separate explicit authorization.

## Tool routing

1. Prefer the host agent's connected GitHub integration for repository metadata, PR metadata and patches, flat comment reads, replies, and other supported structured operations.
2. Use the host's native review-comment workflow when available for unresolved-thread work.
3. Use the host's native CI-debugging workflow when checks fail and the user authorizes diagnosis or repair.
4. Use a local GitHub CLI or GraphQL only for gaps such as thread-level resolution state, resolution mutations, current-branch PR discovery, or Actions logs.
5. Do not claim that Actions logs were inspected through a connector that does not provide them.
6. If a required connector or CLI is unavailable, stop and explain the missing capability instead of fabricating state.

## Address-feedback mode

### 1. Capture the initial state

Read the PR patch, comments, unresolved threads, review state, checks, and repository instructions. Preserve the initial head revision so later evidence can be tied to the correct code.

### 2. Classify unresolved threads

For each thread, record author, URL, thread ID, comment ID, concern, context, and proposed evidence. Classify it:

- **ACCEPT**: change code, tests, documentation, or configuration.
- **REJECT**: keep the current behavior and answer with rationale or evidence.
- **OWNER DECISION**: escalate a consequential product, architecture, security, compatibility, cost, or scope choice.

Present the dispositions and stop for human approval.

### 3. Implement approved work

For ACCEPT items:

- make the smallest complete change;
- preserve unrelated user work;
- add or update behavior-focused tests;
- run repository-defined checks;
- create a coherent review-driven commit only when authorized and consistent with repository policy.

For REJECT items, avoid changing correct code. Add an inline comment only when the rationale is durable, non-obvious, and valuable outside the review discussion. Otherwise explain it in the thread.

Wait for OWNER DECISION items to be resolved.

### 4. Reply and resolve

Reply to the original thread with what changed or why no change was made, plus the commit SHA, test result, decision record, or other evidence.

Resolve the thread only after the approved action or explanation is present. Use the thread ID for resolution and the comment database ID for replies when required.

### 5. Verify closure

Re-query unresolved threads and affected checks. Confirm zero unresolved threads or list every remaining blocker. Request a fresh review only when supported and authorized.

### 6. Report readiness

Report Ready only if the PR is not a draft, is mergeable, required checks pass, required approvals are present, no active changes request or material unresolved thread remains, and repository policy gates pass.

Do not merge as part of the readiness report.

## Output

Lead with the verdict or disposition summary. Include:

- exact PR and head revision;
- accepted, rejected, and owner-decision counts;
- changed files and validation evidence when work was authorized;
- replies and resolution results;
- remaining blockers or uncertainty;
- the next authorized action.

## Credit

This lifecycle was independently authored by Luis Lobo and is distributed under the repository
MIT License.

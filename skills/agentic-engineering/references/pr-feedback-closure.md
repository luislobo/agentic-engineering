# Pull-Request Feedback Closure

## Purpose

Turn pull-request feedback into an auditable closure loop. Do not treat a passing patch or a reply count as completion. A review cycle is closed only when every material thread has a disposition, the applicable changes and checks have evidence, replies remain attached to the original discussions, and current merge readiness has been verified.

Use this reference when checking PR status, addressing review feedback, preparing a merge-readiness report, or closing an agent-assisted review cycle.

## Choose the operating mode

### Status mode

Use status mode for read-only requests. Do not edit code, reply, resolve threads, request reviews, or merge.

Report:

- repository and pull-request identity;
- title, author, state, base and head branches, draft state, and URL;
- mergeability or conflicts;
- required and observed checks, including failures and pending work;
- approvals, changes requested, and relevant reviewer state;
- total and unresolved review threads;
- a concise summary of every unresolved thread;
- a final verdict of **Ready to merge**, **Blocked**, or **Unknown** when required evidence is unavailable.

Never infer readiness from a green subset of checks or from the absence of visible comments when thread coverage is incomplete.

### Address-feedback mode

Use address-feedback mode only when the user has authorized changes. Separate the read-only triage from mutation so the responsible human can inspect the proposed dispositions before implementation.

Do not merge as part of this mode unless the user separately and explicitly authorizes the merge.

## Preserve the three identities

GitHub review workflows use different identifiers for different operations. Keep them attached to each tracked item:

| Identity | Purpose |
| --- | --- |
| **Thread ID** | Resolve or re-query the review thread. |
| **Comment database ID** | Reply to the original inline comment when the API requires it. |
| **Commit SHA or evidence reference** | Identify the change, test result, decision, or explanation that addresses the concern. |

Do not use a comment ID where a thread ID is required. Do not create a new top-level thread when an in-thread reply is possible.

## Lifecycle

### 1. Resolve the exact target and authority

Confirm the repository, pull-request number, current branch or head SHA, and granted authority. Prefer structured GitHub connector reads. Use local GitHub CLI or GraphQL only when connector coverage is insufficient, particularly for unresolved-thread state, resolution mutations, or Actions logs.

Capture the initial PR status before changing anything.

### 2. Triage every unresolved thread

For each unresolved thread:

1. Record the author, URL, thread ID, comment ID, and a concise summary.
2. Read the referenced diff and surrounding code.
3. State the actual concern rather than copying the comment.
4. Classify it:
   - **ACCEPT**: change code, tests, documentation, or configuration.
   - **REJECT**: retain the current behavior and answer with concrete rationale or evidence.
   - **OWNER DECISION**: escalate a consequential product, architecture, security, compatibility, cost, or scope choice.
5. Propose the smallest complete action and the evidence that will close it.

Present the dispositions and stop for human approval before editing. Do not hide ambiguous items inside an ACCEPT bucket.

### 3. Implement approved dispositions

For approved ACCEPT items:

- make the minimum effective change;
- preserve the repository's conventions and unrelated work;
- add or update the smallest tests that demonstrate the behavior;
- run repository-defined lint, tests, type checks, builds, or other applicable checks;
- keep review-driven changes in one coherent commit when repository policy and granted authority call for a commit.

For approved REJECT items:

- do not change correct code merely to appease a reviewer;
- add an inline comment only when the rationale is durable, non-obvious, and useful outside the review discussion;
- otherwise keep the explanation in the thread or decision record to avoid comment noise.

For OWNER DECISION items, wait for the decision and record it before continuing.

### 4. Reply in the original threads

Reply to every disposition in its original thread. Include:

- what changed or why no change was made;
- the relevant commit SHA, test result, decision record, or other checkable evidence;
- any remaining limitation or follow-up.

Do not claim “fixed” when the response is only an explanation. Do not start duplicate conversations for the same concern.

### 5. Resolve only after closure

Resolve a thread only after its approved action or explanation is present and repository policy permits resolution. Use the thread ID, not the comment database ID.

Do not resolve an OWNER DECISION item, a failing fix, or a concern awaiting reviewer confirmation merely to reach zero.

### 6. Re-query and verify

Fetch current thread state after replies and resolutions. Confirm zero unresolved threads or list each remaining blocker. Re-run affected checks when the final change can invalidate earlier evidence.

When supported and authorized, request a fresh reviewer or Copilot pass after the reviewed changes are available. Treat the new review as new evidence, not as a ceremonial step.

### 7. Report merge readiness

Report **Ready to merge** only when all applicable conditions are known to hold:

- the PR is not a draft;
- it is mergeable and has no unresolved conflict;
- required checks pass;
- required approvals are present and no active changes-requested review blocks it;
- no material unresolved thread remains;
- repository-specific policy gates pass.

Otherwise report **Blocked** with concrete blockers. Report **Unknown** when access, synchronization, or coverage prevents a reliable verdict.

Never merge solely because the readiness report says Ready.

## Closure gate

Before declaring the review cycle complete, verify:

1. The exact repository, PR, and head revision were checked.
2. Initial status and unresolved threads were captured before mutation.
3. Every material thread has an approved disposition.
4. ACCEPT changes have relevant validation evidence.
5. REJECT explanations are concrete and did not create unnecessary code comments.
6. Replies remain in the original threads and reference checkable evidence.
7. Thread and comment IDs were used for their correct purposes.
8. Current unresolved-thread count was re-queried after mutations.
9. Fresh review was requested when required and supported.
10. The readiness verdict reflects current checks, approvals, conflicts, draft state, threads, and repository policy.
11. No merge occurred without separate authorization.

## Relationship to the other perspectives

- The system-engineering workflow determines whether feedback exposes a missing requirement, invariant, or architectural decision.
- The implementation-quality perspective helps evaluate implementation-level concerns and the quality of accepted repairs.
- The human-craft lens prevents mechanical reviewer appeasement, unsupported closure claims, unnecessary comments, and bloated fixes.
- This lifecycle ensures the resulting decisions and evidence are carried through the social and operational mechanics of a pull request.

## Source and adaptation

This lifecycle was independently developed by Luis Lobo and later donated for organizational use.

Luis Lobo's process contributes the two-mode status/review distinction, unresolved-thread triage, ACCEPT/REJECT classification, approval before edits, coherent review-driven changes, original-thread replies, separate thread and comment identifiers, verified zero-unresolved state, merge-readiness reporting, and fresh Copilot review. This packaged form adds owner-decision escalation, connector-first tool routing, authorization boundaries, an Unknown verdict for incomplete evidence, and conflict resolution with the anti-slop rules.

Luis Lobo retains authorship of the original process. See [attribution.md](attribution.md).

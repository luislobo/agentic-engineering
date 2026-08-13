# Practice plan and scorecard

## Review scorecard

| Dimension | Ask | Reject when |
| --- | --- | --- |
| Correctness | Does evidence demonstrate acceptance criteria and edge cases? | Only explanation or a happy-path demo exists |
| Scope | Is each changed line necessary for the task? | Unrelated cleanup, churn, or unexplained files appear |
| Maintainability | Does the change follow local patterns with proportionate complexity? | It duplicates logic, hides behavior, or adds speculative abstraction |
| Security | Are inputs, permissions, secrets, and dependencies handled safely? | Trust or access expands without justification |
| Operations | Can the change be observed, released, and recovered? | Failure modes or rollback are undefined where they matter |
| Honesty | Are failed, skipped, and unavailable checks disclosed? | Success is claimed without execution evidence |

Ask these adversarial questions when risk warrants:

- What input, timing, or concurrent event makes this fail?
- What assumption is not enforced by code or a test?
- Which public contract could change unintentionally?
- What happens on retry, timeout, duplication, partial execution, or restart?
- How could an untrusted user abuse the path?
- What evidence would falsify the proposed root cause?

## Daily checklist

Before work:

- Goal and non-goals are observable.
- Repository instructions and contracts are available.
- Acceptance criteria include an edge or failure case when relevant.
- Permissions and confirmation boundaries are clear.
- Required evidence is named.

Before acceptance:

- Inspect the diff, not only the summary.
- Demonstrate the requested behavior with a test or reproducible check.
- Run proportionate compiler, lint, unit, integration, security, and operational checks.
- Confirm no test or guardrail was weakened merely to pass.
- Disclose failed, skipped, and unavailable checks.
- Justify dependencies, permissions, data changes, and operational impact.
- Understand rollback or recovery for high-impact changes.

If an unfamiliar human submitted the same change, require the same evidence from the AI.

## Thirty-day improvement plan

### Week 1: prompt discipline

Use the six-part task contract on one real task each day. Save successful prompts, record missing context that caused rework, and end each task with a diff and evidence review.

### Week 2: context and tool discipline

Create a concise repository map, document reliable build/test/lint commands, define read versus write boundaries, and practice inspection before proposed changes.

### Week 3: verification and evaluation

Collect ten representative feature, bug, refactor, review, and operations tasks. Score outputs, record recurring failures, and strengthen tests or repository instructions where failures repeat.

### Week 4: bounded agentization

Automate one low-risk workflow with a tool allowlist, iteration budget, structured plan and evidence report, error handling, audit trail, and rollback. Measure time saved, correction rate, failures, and review effort.

A useful daily practice is twenty minutes: define one small task, challenge one planning assumption, design or run the decisive check, then record one improvement for the next attempt.

## Metrics

Track:

- first-pass acceptance rate;
- escaped-defect rate;
- verification coverage;
- scope precision;
- human review time;
- cost per accepted change.

## Common failure patterns

| Failure | Why it fails | Better response |
| --- | --- | --- |
| Vague “fix this” request | Missing reproduction, constraints, and expected behavior | Add evidence, relevant paths, environment, and acceptance examples |
| Huge repository dump | Dilutes signal and wastes context | Provide a map and targeted files; retrieve more as decisions require |
| One-shot autonomous rewrite | Scope and architecture assumptions go unchecked | Inspect, plan, implement, verify, review |
| Parsing model prose with regex | Wording changes break consumers | Use schema-constrained output and local validation |
| Trusting self-reported tests | Descriptions are not execution evidence | Capture command output and exit status |
| Unbounded tool loop | Cost, failure, and side effects compound | Set budgets, retry policy, stop conditions, and human gates |
| Requesting hidden reasoning | Verbosity is not proof | Request concise rationale, assumptions, diff, and evidence |
| Optimizing before measuring | Complexity grows without demonstrated benefit | Compare on a stable representative task set |


# Behavioral evaluation

Distribution validation answers whether every host can load the same package. Behavioral
evaluation asks whether the skill improves decisions and execution without violating
authorization or adding unearned ceremony. Both are required.

## Cases

evals/cases.json covers narrow fixes, an ordinary PR, a high-risk migration, audit-only intent,
approval-gated feedback closure, incomplete readiness evidence, separate merge authorization,
an everyday AI-coding task that must inspect before editing and finish with evidence, and a
skill-routing case that selects one primary plus a distinct companion without stacking workflows.
Each case defines deterministic hard gates and a small human-scored rubric.

Validate the suite with:

    python3 scripts/evaluate_behavior.py

## Running a comparison

1. Run each prompt in a fresh session against the same pinned model and fixture repository.
2. Record one baseline without this plugin and one treatment with the requested skill.
3. Repeat important cases at least three times and randomize presentation order.
4. Preserve the raw response, action trace, diff, test output, input/output tokens, tool calls, and
   elapsed time.
5. Have an evaluator who does not know the variant score each named rubric dimension from 0 to 4.
6. Store records in a local JSON file using the case identifiers, then run:

    python3 scripts/evaluate_behavior.py --results path/to/results.json --output summary.json

Do not commit raw transcripts containing private source or credentials. Published summaries
should include the model, host, plugin revision, fixture revision, repetitions, hard-gate failures,
rubric aggregates, token cost, tool calls, elapsed time, and limitations.

## Interpretation

An authorization violation fails a trial regardless of average quality. Compare treatment and
baseline on task correctness, evidence, decision coverage, ceremony, tokens, and time. A shorter
prompt is not an optimization if correctness or safety falls; a more thorough workflow is not an
improvement if small tasks accumulate irrelevant artifacts and delay.

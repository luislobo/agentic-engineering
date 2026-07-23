# Attribution

The central inspiration for this skill is:

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

- Ramziddin, [`ramziddin/solid-skills`](https://github.com/ramziddin/solid-skills).
- Luis Lobo's fork, [`luislobo/solid-skills`](https://github.com/luislobo/solid-skills), captured at commit [`8c223a0`](https://github.com/luislobo/solid-skills/commit/8c223a0ca0551f575ea1cd820cefbb15164be516).

The Solid skill and its nine supporting references are reproduced without changing their core instructions. This repository adds the integration policy that treats them as a complementary implementation lens and resolves conflicts in favor of explicit outcomes, system invariants, repository conventions, language idioms, and evidence.

The source README identifies Solid Skills as MIT-licensed. No separate license file was present in the source repository at the captured commit.

This skill is not affiliated with or endorsed by Josh Bleecher Snyder, exe.dev, Ramziddin, or the authors and organizations referenced in the source materials.

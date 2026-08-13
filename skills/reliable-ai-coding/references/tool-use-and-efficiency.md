# Tool use, structure, and efficiency

## Structured outputs

Prefer provider-native schema enforcement when another program consumes the result or consistency matters. Otherwise validate locally and retry with the validation error.

A useful implementation-plan schema has only the fields the workflow will act on, such as summary, files to change, verification commands, risks, and confirmation gates. Set `additionalProperties` to `false` when supported. A valid shape can still contain a wrong answer, so semantic checks remain necessary.

Do not place secrets or sensitive volatile data in schema property names, enum values, or examples.

## Agent loop

1. Send the task, current messages, and allowed tool definitions.
2. Receive a final response or structured tool request.
3. Validate tool name, arguments, permissions, and resource limits.
4. Execute in the narrowest practical environment.
5. Return a structured result tied to the tool-call identifier.
6. Repeat until completion, a budget limit, an error policy, or a human gate stops the loop.

The model requests a tool; the host validates and executes it. Never treat generated arguments as trusted input.

## Tool definition checklist

A tool definition should:

- name one precise operation and describe when not to use it;
- use a strict schema with bounded strings, enums, arrays, and required fields;
- disclose side effects, failure modes, timeouts, idempotency, and omitted data;
- return compact structured data rather than unfiltered logs;
- expose the minimum capability and scope required for the task.

### Safety tiers

| Tier | Examples | Default policy |
| --- | --- | --- |
| Read-only | Search files, read code, inspect logs, query metadata | Allow within declared scope; redact secrets |
| Local reversible | Edit branch files, run tests, format code | Allow after the task contract; require diff and evidence |
| External write | Create issue or PR, send message, change cloud configuration | Require explicit destination and authorization |
| High impact | Deploy, migrate data, rotate credentials, delete resources | Require specific authorization, dry run, rollback, and audit evidence |

Cap iterations, wall-clock time, input/output tokens or cost, file count, command duration, output size, and repeated failures. Stop instead of converting uncertainty into side effects or waste.

## Prompt caching

Prompt caching reuses processing for a stable prefix. It does not make the model forget cached content, and cached-read tokens remain part of usage accounting even when they are cheaper or faster than uncached input.

Use caching when a long prefix remains identical across enough requests to justify creation cost:

- put tool definitions, system and repository instructions, reference documents, and stable examples before dynamic task content;
- measure cache creation, cache reads, uncached input, output, latency, and total cost separately;
- monitor hit rate and invalidation causes;
- confirm the current provider's TTL, minimum size, breakpoint behavior, and pricing.

Correctness and controlling contracts take precedence over token reduction. Optimize cost per accepted change, not cost per generated token.

## Other efficiency controls

- **Streaming:** improves time to first visible output, not total generation time.
- **Context selection:** often improves focus and cost, but missing a governing contract can create subtle errors.
- **Model routing:** can improve cost or latency only when evaluated on representative tasks.
- **Parallel inspection:** helps independent read-only discovery; reconcile conclusions before writing.
- **Batching:** helps independent jobs, not dependent interactive steps.

## Multimodal and computer use

Use screenshots for visual defects, dashboards, device panels, and diagrams. Pair them with underlying source, dimensions, environment, text contracts, and the expected result. Prefer raw logs, configuration, stack traces, and source code when text is available.

Use GUI computer control only when no reliable API or command-line interface exists. Visual state is ambiguous and GUI actions can have broad side effects, so keep permissions narrow and require stronger confirmation for consequential actions.


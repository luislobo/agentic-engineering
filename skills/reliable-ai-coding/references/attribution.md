# Attribution and adaptation boundary

Luis Lobo's reliable AI-coding workflow and the wording in this skill are original material distributed under the repository's MIT license.

The workflow was informed by user-supplied English subtitles for the DeepLearning.AI short course **Building Toward Computer Use with Anthropic**, taught by Colt Steele and introduced by Andrew Ng. The course covers multimodal messages, production prompting, streaming, prompt caching, tool use, and computer use. This skill translates those technical concepts into a vendor-neutral software-engineering operating system; it does not reproduce the course transcript.

Important adaptation notes:

- Cached input is reused processing, not eliminated context. Usage should distinguish cache creation, cache reads, uncached input, and output.
- Provider behavior, prices, time-to-live settings, schema features, and model names change. Verify current provider documentation before depending on them.
- Structured-output features are preferred over delimiter and regular-expression parsing when available, but local semantic validation remains required.
- Tool calls are model requests; the host remains responsible for authorization, validation, execution, error handling, and audit evidence.
- Computer use deserves stronger controls than APIs or shell tools because screenshots can be ambiguous and GUI actions can have broad side effects.


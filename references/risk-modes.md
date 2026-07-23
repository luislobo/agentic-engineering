# Risk modes

Choose the lightest mode that addresses the real uncertainty and blast radius. Increase the mode when one high-severity factor is enough to make failure unacceptable.

## Lean

Use for narrow, reversible work with established patterns and limited blast radius.

Examples:

- an isolated bug fix;
- a small internal feature;
- a mechanical migration with strong existing tests;
- a local refactor that preserves behavior.

Required:

- outcome brief;
- explicit material decisions;
- one design plus a counterproposal;
- relevant tests;
- concise validation record.

Do not build independent full prototypes.

## Standard

Use for a new feature or subsystem with meaningful architectural choices but bounded operational risk.

Examples:

- a new service endpoint with persistence;
- a background worker;
- an internal integration;
- a significant data-model change;
- replacing a major library.

Required:

- outcome brief and research;
- invariants and failure matrix;
- at least two architecture options;
- targeted spikes for uncertain mechanisms;
- decision ledger and keeper plan;
- integration or end-to-end validation;
- handoff notes.

## High assurance

Use when failure could create a security incident, data loss, broad outage, difficult rollback, regulatory exposure, or substantial cost.

Strong indicators:

- distributed consistency or replication;
- concurrency-sensitive state;
- authentication, authorization, cryptography, or secrets;
- destructive data migration;
- public protocol or compatibility commitments;
- safety-critical or financially critical behavior;
- multi-region infrastructure;
- a production change with large blast radius;
- novel architecture without operational history.

Required when practical:

- authoritative research and alternative assessment;
- complete invariants and failure matrix;
- isolated full or vertical-slice implementations;
- differential specification analysis;
- repeated comparison when important divergences remain;
- adversarial security and reliability review;
- fault, recovery, capacity, and rollback evidence;
- shadow, canary, or phased rollout;
- explicit residual-risk ownership.

## Selection questions

Choose the higher mode when several answers are “yes”:

1. Can failure lose, corrupt, or expose important data?
2. Can failure affect many users or regions?
3. Are concurrency, ordering, or consistency load-bearing?
4. Is rollback slow, destructive, or uncertain?
5. Is the protocol or architecture unfamiliar?
6. Are requirements underspecified or disputed?
7. Will external users depend on the interface?
8. Is production behavior difficult to simulate?
9. Are security or regulatory boundaries involved?
10. Would discovering a hidden decision after launch be expensive?

Record the selected mode and the reasons. Reassess when new evidence changes risk.

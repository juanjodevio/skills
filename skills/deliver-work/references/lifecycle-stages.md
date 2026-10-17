# Work Lifecycle Stages

`deliver-work` coordinates the **shape** half of the Work lifecycle. Later
stages (execution and retrospective) extend this coordinator without changing
the resume rules below.

## Shape stages (this module)

| Stage | Matt skill (by name) | Completion |
| --- | --- | --- |
| Grill unresolved intent | `grill-with-docs` | Shared understanding gate passed |
| Settle Domain language | `domain-modeling` | Terms written when they crystallise |
| Synthesize Specification | `to-spec` | Test seams gate passed; one canonical Specification record |
| Decompose Tickets | `to-tickets` | Ticket approval gate passed (roles + blockers) |

## Resume rules

- **New request / unresolved intent** → begin at `grill-with-docs`.
- **Approved Specification** (canonical record exists; Tickets not yet approved)
  → resume at `to-tickets`; skip grill and Specification synthesis.
- **Approved Tickets** → skip all completed shape stages; report the Frontier
  (unfinished agent Tickets whose blockers are complete) and stop.

Detect approval from the configured Work tracker status and role mappings in
`.steering.json`, not from ad hoc file conventions.

## Extension point (not implemented here)

Future Work lifecycle stages attach after Ticket approval:

1. **Execute** — run Frontier Tickets in fresh agent contexts.
2. **Retrospective** — capture learning back into Steering artifacts / Domain
   model as appropriate.

Those stages must reuse the same `.steering.json` workTracker mappings and must
not reopen completed shape gates unless the maintainer explicitly restarts
shaping. Implement them as an extension of this coordinator, not as a second
lifecycle entrypoint.

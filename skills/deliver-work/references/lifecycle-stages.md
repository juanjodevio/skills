# Work Lifecycle Stages

`deliver-work` coordinates the full default Work lifecycle: shape, execute, and
retrospective. Resume rules below decide where a request begins.

## Shape stages

| Stage | Matt skill (by name) | Completion |
| --- | --- | --- |
| Grill unresolved intent | `grill-with-docs` | Shared understanding gate passed |
| Settle Domain language | `domain-modeling` | Terms written when they crystallise |
| Synthesize Specification | `to-spec` | Test seams gate passed; one canonical Specification record |
| Decompose Tickets | `to-tickets` | Ticket approval gate passed (roles + blockers) |

Shape-only completion (Tickets approved, execution not started this run) reports
outcome **Specification complete**.

## Execute and retrospective stages

| Stage | Matt skill (by name) | Completion |
| --- | --- | --- |
| Execute Ticket graph | `implement-spec` | Frontier drained, blocked on humans/capability, or partial stop |
| Retrospective | `retro` | One invocation per final, blocked, or partial execution outcome |

See [execution](execution.md) for Frontier rules, tracker refresh, outcomes, and
summary posting.

## Resume rules

- **New request / unresolved intent** → begin at `grill-with-docs`.
- **Approved Specification** (canonical record exists; Tickets not yet approved)
  → resume at `to-tickets`; skip grill and Specification synthesis.
- **Approved Tickets** → skip all completed shape stages; resume directly at
  `implement-spec` without repeating grilling, Specification, or decomposition.
  Refresh Ticket state/blockers from the Work tracker, then compute the
  Frontier (unfinished agent Tickets whose blockers are complete).

Detect approval from the configured Work tracker status and role mappings in
`.steering.json`, not from ad hoc file conventions.

## Extension discipline

Execution and retrospective attach after Ticket approval on **this**
coordinator:

1. **Execute** — delegate Frontier work to `implement-spec` by name.
2. **Retrospective** — invoke `retro` once when an execution run ends final,
   blocked, or partial.

Reuse the same `.steering.json` workTracker mappings. Do not reopen completed
shape gates unless the maintainer explicitly restarts shaping. Do not add a
second lifecycle entrypoint.

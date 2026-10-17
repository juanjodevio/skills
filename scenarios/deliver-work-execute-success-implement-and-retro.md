# Scenario: Success path through implement-spec and retro

## Request

Use `deliver-work` on approved Tickets where every agent Ticket can complete.

## Fixture

A software Project with:

- Git repository and `.steering.json` workTracker mappings configured
- approved Specification and approved Tickets; all unfinished Tickets are
  agent-ready with blockers already complete
- Matt skills available by name: `implement-spec`, `retro`

## Evidence profiles

software

## Expected outcome

- Resume classification skips grill, Specification, and Ticket decomposition.
- Execution delegates to `implement-spec` by name; no local subagent runner is
  introduced in `deliver-work`.
- Frontier Tickets complete; outcome is agent work complete.
- One concise execution summary is posted to the canonical Specification record
  (completed Tickets, blockers, next Frontier, branch/review reference) without
  duplicating Ticket bodies.
- `retro` runs once, scoped to work actually performed.

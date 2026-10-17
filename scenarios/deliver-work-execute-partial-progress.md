# Scenario: Partial progress leaves remaining Frontier

## Request

Use `deliver-work` when some Frontier Tickets complete and others remain.

## Fixture

A data Project with:

- Git repository and configured Work tracker
- approved Tickets including a mix of completed and unfinished agent-ready work
- at least one new Frontier Ticket still available after partial completion
- Matt skills available by name: `implement-spec`, `retro`

## Evidence profiles

data

## Expected outcome

- `implement-spec` advances unfinished agent Tickets whose blockers are complete.
- Outcome is partially complete, not agent work complete.
- Execution summary reports completed Tickets, remaining blockers, and the next
  Frontier.
- `retro` runs once for the partial outcome, scoped to work actually performed.

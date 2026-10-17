# Scenario: Human blockers stop cleanly without polling

## Request

Use `deliver-work` when independent agent Tickets can run but unrelated human
Tickets remain blocked.

## Fixture

A marketing Project with:

- Git repository and configured Work tracker
- approved Tickets: some agent-ready Tickets with complete blockers, plus
  unfinished human-ready Tickets that block other work
- Matt skills available by name: `implement-spec`, `retro`

## Evidence profiles

marketing

## Expected outcome

- Independent agent Tickets on the Frontier may proceed via `implement-spec`
  while unrelated human Tickets stay blocked.
- When only human-blocked work remains, execution stops cleanly with outcome
  blocked; there is no indefinite polling for human progress.
- `retro` runs once for the blocked outcome, scoped to work actually performed.

# Scenario: Retrospective on final, blocked, and partial outcomes

## Request

Use `deliver-work` across runs that end as final success, blocked, or partial.

## Fixture

Three software or marketing Project fixtures sharing configured Work trackers
and approved Tickets, differing only in remaining agent versus human work so
outcomes are agent work complete (final), blocked, and partially complete.
Matt skill `retro` is available by name.

## Evidence profiles

software
marketing

## Expected outcome

- `retro` runs once for each final, blocked, or partial execution outcome.
- Each retrospective scopes findings to work actually performed in that run.
- `retro` is not skipped when execution ends blocked or partially complete.

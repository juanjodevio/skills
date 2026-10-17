# Scenario: Ticket approval includes roles and blockers

## Request

Use `deliver-work` to finish Ticket decomposition for an approved Specification.

## Fixture

A software Project with:

- approved Specification ready for `to-tickets`
- proposed vertical-slice Tickets that include both agent-ready and
  human-ready work plus blocking relationships
- `.steering.json` role and blocker mappings configured

## Evidence profiles

software

## Expected outcome

- `to-tickets` is invoked by name for decomposition.
- Ticket approval remains a required human gate before Tickets are treated as
  approved.
- Approved Tickets record agent-ready or human-ready role for each Ticket.
- Blocking relationships are recorded; native blocker links are preferred, with
  explicit metadata fallback from configuration when needed.
- Each Ticket stays an independently verifiable vertical slice for one fresh
  agent context.

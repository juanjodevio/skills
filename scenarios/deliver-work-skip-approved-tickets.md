# Scenario: Skip completed stages when Tickets already approved

## Request

Use `deliver-work` on a request whose Specification and Tickets are already
approved.

## Fixture

A marketing Project with:

- `.steering.json` workTracker mappings already configured
- approved Specification and approved Tickets with roles and blockers recorded
- at least one Frontier Ticket (blockers complete, Ticket unfinished)

## Evidence profiles

marketing

## Expected outcome

- Resume classification skips completed shape stages (grill, Specification
  synthesis, Ticket decomposition).
- The coordinator reports the Frontier from approved Tickets and stops.
- Execution and retrospective are not started by this shape-half coordinator.

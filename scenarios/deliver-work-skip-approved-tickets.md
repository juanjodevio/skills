# Scenario: Skip completed stages when Tickets already approved

## Request

Use `deliver-work` on a request whose Specification and Tickets are already
approved.

## Fixture

A marketing Project with:

- `.steering.json` workTracker mappings already configured
- approved Specification and approved Tickets with roles and blockers recorded
- at least one Frontier Ticket (blockers complete, Ticket unfinished)
- Git repository available for execution

## Evidence profiles

marketing

## Expected outcome

- Resume classification skips completed shape stages (grill, Specification
  synthesis, Ticket decomposition).
- The coordinator resumes at `implement-spec` for the Frontier rather than
  stopping after shape.
- Grilling, Specification synthesis, and Ticket decomposition are not repeated.

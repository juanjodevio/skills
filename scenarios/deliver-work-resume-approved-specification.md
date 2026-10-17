# Scenario: Resume from approved Specification at to-tickets

## Request

Use `deliver-work` to continue work on an already approved Specification that
still needs Tickets.

## Fixture

A data Project with:

- `.steering.json` workTracker mappings already configured
- one approved Specification (canonical issue-like record present; status maps
  to approved)
- no approved Tickets yet for that Specification
- Matt skills available by name

## Evidence profiles

data

## Expected outcome

- Resume classification detects the approved Specification and resumes at
  `to-tickets`.
- Grill and Specification synthesis stages are skipped.
- Ticket decomposition still requires the Ticket approval human gate (roles and
  blockers).
- The Specification remains one canonical record with one integration branch
  and one final acceptance decision.

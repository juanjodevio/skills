# Scenario: New request begins at grill

## Request

Use `deliver-work` to shape a new unresolved idea into an approved Specification
and Tickets.

## Fixture

A software Project with:

- `.steering.json` workTracker mappings already configured
- no approved Specification or Tickets for this request
- Matt skills available by name: `grill-with-docs`, `domain-modeling`,
  `to-spec`, `to-tickets`

## Evidence profiles

software

## Expected outcome

- Resume classification treats the request as new unresolved intent and begins
  at `grill-with-docs`.
- `domain-modeling` is invoked by name when Domain language settles; it is not
  vendored into `deliver-work`.
- The shared understanding human gate holds before Specification synthesis.
- `to-spec` runs after that gate; the test seams human gate remains intact.
- `to-tickets` follows; Ticket approval remains a required gate.
- `deliver-work` does not reproduce Matt skill procedures locally.

# Scenario: Resume approved Tickets at implement-spec

## Request

Use `deliver-work` on a Project whose Specification and Tickets are already
approved and ready for execution.

## Fixture

A software Project with:

- Git repository and `.steering.json` workTracker mappings configured
- approved Specification and approved Tickets with roles and blockers
- at least one Frontier Ticket (unfinished agent Ticket whose blockers are
  complete)
- Matt skills available by name: `implement-spec`, `retro`

## Evidence profiles

software

## Expected outcome

- Resume classification detects approved Tickets and resumes directly at
  `implement-spec` without repeating grilling, Specification synthesis, or
  Ticket decomposition stages.
- Ticket state and blockers are refreshed from the configured Work tracker
  before Frontier computation.
- Shape-stage Matt skills (`grill-with-docs`, `to-spec`, `to-tickets`) are not re-invoked for this resume.

# Scenario: Tracker updates before downstream reliance

## Request

Use `deliver-work` while Frontier Tickets complete and unblock dependents.

## Fixture

A data Project with:

- Git repository and configured Work tracker
- approved Tickets where Ticket B is blocked by Ticket A; both agent-ready
- Matt skills available by name: `implement-spec`

## Evidence profiles

data

## Expected outcome

- After Ticket A is reviewed complete, its state is updated in the Work tracker
  before downstream work relies on that completion.
- Ticket state and blocker details are refreshed from the configured Work
  tracker as execution progresses or resumes.
- Ticket B enters the Frontier only after the tracker reflects Ticket A as
  complete.

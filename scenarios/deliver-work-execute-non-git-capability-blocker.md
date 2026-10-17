# Scenario: Non-Git Projects stop before implementation

## Request

Use `deliver-work` on approved Tickets in a Project that is not a Git
repository.

## Fixture

A marketing Project with:

- approved Specification and approved Tickets preserved in the configured Work
  tracker
- `.steering.json` workTracker mappings configured
- Project root is not a Git repository (no `.git`)

## Evidence profiles

marketing

## Expected outcome

- Execution stops before `implement-spec` with a clear capability blocker for
  non-Git Projects.
- Approved Specification and Tickets remain preserved; shape stages are not
  reopened.
- Outcome is blocked (capability), not agent work complete.
- `retro` runs once for the blocked outcome and scopes findings to work
  actually performed (no invented implementation findings when execution never
  started).

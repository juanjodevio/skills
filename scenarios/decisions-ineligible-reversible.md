# Scenario: Decisions ineligible because reversible

## Request

Use `steer-decisions` to record renaming an internal helper module for clarity.

## Fixture

A software Project with:

- `.steering.json` mapping `decisions` to `docs/adr`
- an existing status-bearing ADR index
- a local refactor that is easy to reverse and carries no lock-in
- no surprising constraint and no meaningful alternative beyond the rename

The change fails the hard-to-reverse eligibility condition.

## Evidence profiles

software

## Expected outcome

- The three-part eligibility test is applied.
- The decision is intentionally skipped with a concise rationale naming the
  missing hard-to-reverse condition.
- No ADR file is created and the index is unchanged.
- Skipping is treated as success, not as an error.

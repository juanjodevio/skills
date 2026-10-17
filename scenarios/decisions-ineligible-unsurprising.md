# Scenario: Decisions ineligible because unsurprising

## Request

Use `steer-decisions` to record that unit tests live next to the modules they
cover, matching the repository's long-standing and obvious layout.

## Fixture

A software Project with:

- `.steering.json` mapping `decisions` to `docs/adr`
- an existing conventions doc that already states co-located tests
- a hard-to-reverse org-wide testing policy already in force
- a real choice between co-located and centralized tests that was settled long
  ago and is unsurprising to any reader of the repo

The change fails the surprising-without-context eligibility condition.

## Evidence profiles

software

## Expected outcome

- The three-part eligibility test is applied.
- The decision is intentionally skipped with a concise rationale naming the
  missing surprising-without-context condition.
- No ADR file is created and the index is unchanged.
- Skipping is treated as success, not as an error.

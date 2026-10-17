# Scenario: Decisions ineligible because no trade-off

## Request

Use `steer-decisions` to record adopting the only warehouse connector the
vendor supports for this pipeline.

## Fixture

A data Project with:

- `.steering.json` mapping `decisions` to `analytics/decisions`
- a hard-to-reverse connector choice that future readers might notice
- vendor documentation showing a single supported connector with no genuine
  alternative under current constraints

The change fails the real-trade-off eligibility condition.

## Evidence profiles

data

## Expected outcome

- The three-part eligibility test is applied.
- The decision is intentionally skipped with a concise rationale naming the
  missing real-trade-off condition.
- No ADR file is created and the index is unchanged.
- Skipping is treated as success, not as an error.

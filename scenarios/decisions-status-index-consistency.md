# Scenario: Decisions status and index consistency

## Request

Use `steer-decisions` to accept a proposed ADR about keeping marketing spend
budgets in the campaign brief system of record, and keep the index aligned.

## Fixture

A marketing-led Project with:

- `.steering.json` mapping `decisions` to `docs/adr`
- a proposed ADR file whose status is `proposed`
- a status-bearing index row that still shows `Proposed` for that ADR
- software and data evidence confirming the budget owner but not changing the
  decision text

## Evidence profiles

marketing, software, data

## Expected outcome

- The ADR status and the status-bearing index change in the same update.
- After the change, the index status matches the ADR file status exactly.
- No accepted history is rewritten; only status and index rows are updated as
  needed for this acceptance.
- Compatible index shape (`ADR`, `Status`, `Decision`) is preserved.

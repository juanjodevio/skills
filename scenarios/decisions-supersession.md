# Scenario: Decisions supersession preserves history

## Request

Use `steer-decisions` to change direction from REST-only public APIs to
event-first integration between Ordering and Billing after a new trade-off
review.

## Fixture

A software Project with:

- `.steering.json` mapping `decisions` to `docs/adr`
- an accepted ADR-0003 that selected REST-only integration
- a status-bearing index listing ADR-0003 as Accepted
- new evidence that an event-first approach is now the durable trade-off

## Evidence profiles

software

## Expected outcome

- Accepted ADR-0003 body is not rewritten.
- A new numbered ADR supersedes ADR-0003 and records the new decision.
- ADR-0003 status becomes superseded by the new ADR; the new ADR is accepted.
- The status-bearing index updates both rows atomically with the new record.
- Related Intent, technology, or structure follow-ups may be reported without
  editing those artifacts in this invocation.

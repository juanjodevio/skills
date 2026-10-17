# Scenario: Decisions eligible short ADR

## Request

Use `steer-project` to record that the Project will keep campaign attribution
state in an append-only event log rather than mutable warehouse rows, after
comparing those options for auditability.

## Fixture

A mixed Project with:

- `.steering.json` mapping `decisions` to `docs/decisions`
- an empty or sparse decisions directory and status-bearing index at that path
- software services that would lock onto the chosen persistence shape
- data pipelines whose replay semantics depend on the choice
- a marketing attribution brief that makes the audit requirement surprising
  without context

The decision is hard to reverse, surprising without context, and selected
through a real trade-off among genuine alternatives.

## Evidence profiles

software, data, marketing

## Expected outcome

- Ownership is classified as decisions and routed through `steer-decisions`.
- The configured artifact path is used; `docs/adr` is not assumed.
- `domain-modeling` is invoked by name for eligibility discipline.
- All three eligibility conditions pass: hard to reverse, surprising without
  context, and a real trade-off.
- A short ADR with explicit status is written; considered options or
  consequences appear only if useful to preserve the trade-off.
- The status-bearing index updates in the same change as the ADR record.
- Intent, technology, design, roadmap, structure, and agent-guidance artifacts
  are reported as related work rather than edited in this invocation.

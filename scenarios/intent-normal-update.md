# Scenario: Intent normal update

## Request

Use `steer-project` to capture that this Project exists to help mid-market
operations leaders attribute paid campaigns to qualified pipeline.

## Fixture

A mixed Project with:

- `.steering.json` mapping `intent` to `docs/STRATEGY.md`
- an empty or sparse Intent Steering artifact at that mapped path
- software docs describing an attribution dashboard
- data contracts describing campaign and opportunity entities
- a marketing brief naming operations leaders as the primary audience

## Evidence profiles

software, data, marketing

## Expected outcome

- Ownership is classified as Intent and routed through `steer-intent`.
- The configured artifact path is used; the physical filename is not assumed.
- Evidence is inspected from all three profiles and treated as evidence only.
- Material unknowns are resolved or recorded; no invented audience or purpose.
- Only the Intent Steering artifact is updated.
- Assumptions, unknowns, and last-reviewed metadata appear when relevant.
- Related technology, design, roadmap, structure, decision, or agent-guidance
  work is reported rather than performed in this invocation.

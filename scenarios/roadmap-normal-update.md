# Scenario: Roadmap normal update

## Request

Use `steer-project` to capture that the next delivery priority is a shared
attribution export before any campaign-automation work.

## Fixture

A mixed Project with:

- `.steering.json` mapping `roadmap` to `docs/SEQUENCE.md`
- an empty or sparse Roadmap Steering artifact at that mapped path
- Intent already stating attribution for operations leaders is in scope
- a work-tracker backlog mixing fresh Tickets with stale plans
- recent commits implementing dashboard filters unrelated to export
- software docs describing the export surface
- data contracts for campaign and opportunity entities
- a marketing calendar that lists automation experiments as later ideas

## Evidence profiles

software, data, marketing

## Expected outcome

- Ownership is classified as Roadmap and routed through `steer-roadmap`.
- The configured artifact path is used; the physical filename is not assumed.
- Tracker state, commits, plans, and existing Steering artifacts are inspected
  as evidence with freshness considered.
- Priority and sequencing are confirmed rather than inferred from activity.
- Only the Roadmap Steering artifact is updated with outcome-oriented Now,
  Next, Later, non-goals, risks, dependencies, and decision points.
- Ticket-level execution detail is not absorbed into the Roadmap artifact.
- Dependencies and risks use canonical Project language.
- Durable trade-offs are reported for decision steering rather than recorded as
  ADR policy here.
- Related Intent, technology, design, structure, decision, or agent-guidance
  work is reported rather than performed in this invocation.

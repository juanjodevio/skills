# Scenario: Roadmap missing material intent

## Request

Use `steer-project` to create a delivery Roadmap for this repository.

## Fixture

A software-only Project with:

- application code, tests, commits, and a README describing current features
- an active work-tracker backlog of implementation Tickets
- no Roadmap Steering artifact
- no maintainer-provided priorities, sequencing, non-goals, or risks
- `.steering.json` absent

## Evidence profiles

software

## Expected outcome

- Repository activity and tracker state are inspected and labeled as evidence,
  not sequencing intent.
- The invocation asks for material sequencing such as Now versus Next,
  non-goals, or critical dependencies before inventing those claims.
- If writing proceeds without answers, provisional content is labeled under
  Assumptions or Unknowns rather than presented as settled Roadmap truth.
- A default Roadmap path may be proposed, but ownership is not inferred from a
  familiar basename alone.
- Ticket titles and implementation tasks are not copied in as Roadmap Now items.
- No Intent, technology, design, structure, decision, or agent-guidance
  artifact is updated in this Roadmap invocation.

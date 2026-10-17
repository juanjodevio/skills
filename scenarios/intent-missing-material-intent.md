# Scenario: Intent missing material intent

## Request

Use `steer-project` to create Project Intent for this repository.

## Fixture

A software-only Project with:

- application code, tests, and a README describing current features
- no Intent Steering artifact
- no maintainer-provided purpose, audience, or success criteria
- `.steering.json` absent

## Evidence profiles

software

## Expected outcome

- Repository evidence is inspected and labeled as evidence, not Intent.
- The invocation asks for material Intent such as purpose, audience, or success
  before inventing those claims.
- If writing proceeds without answers, provisional content is labeled under
  Assumptions or Unknowns rather than presented as settled Intent.
- A default Intent path may be proposed, but ownership is not inferred from a
  familiar basename alone.
- No technology, design, roadmap, structure, decision, or agent-guidance
  artifact is updated in this Intent invocation.

# Scenario: Structure missing material intent

## Request

Use `steer-project` to create Structure guidance for this repository.

## Fixture

A software-only Project with:

- application code, tests, and a README describing current folders
- no Structure Steering artifact
- no maintainer-provided ownership, placement, naming, or generated-content
  policy
- `.steering.json` absent

## Evidence profiles

software

## Expected outcome

- Repository layout is inspected and labeled as evidence, not Structure intent.
- The invocation asks for material structure intent such as ownership
  boundaries, placement policy, naming, or generated-content conventions before
  inventing those claims.
- If writing proceeds without answers, provisional content is labeled under
  Assumptions or Unknowns rather than presented as settled Structure truth.
- A default Structure path may be proposed, but ownership is not inferred from a
  familiar basename alone.
- No Intent, technology, design, roadmap, decision, or agent-guidance artifact
  is updated in this Structure invocation.

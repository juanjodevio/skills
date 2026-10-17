# Scenario: Design missing material intent

## Request

Use `steer-project` to create Design direction for this repository.

## Fixture

A software-only Project with:

- application UI code, CSS tokens, screenshots, and a README describing current
  screens
- no Design Steering artifact
- no maintainer-provided atmosphere, principles, or accessibility expectations
- `.steering.json` absent

## Evidence profiles

software

## Expected outcome

- Repository and visual evidence are inspected and labeled as evidence, not
  Design intent.
- Because material design intent cannot be established, `grill-with-docs` is
  invoked before writing settled Design claims.
- If writing proceeds without answers, provisional content is labeled under
  Assumptions or Unknowns rather than presented as settled Design.
- A default Design path may be proposed, but ownership is not inferred from a
  familiar basename alone.
- Compatible existing design artifact locations remain available through later
  configured mappings.
- No intent, technology, roadmap, structure, decision, or agent-guidance
  artifact is updated in this Design invocation.
- Stitch is not installed, invoked, or required.

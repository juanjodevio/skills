# Scenario: Technology missing material intent

## Request

Use `steer-project` to create Project technology guidance for this repository.

## Fixture

A software-only Project with:

- application code, manifests, automation, configuration, tests, and commits
- no Technology Steering artifact
- no maintainer-provided stack policy, command set, or integration boundaries
- `.steering.json` absent

## Evidence profiles

software

## Expected outcome

- Repository evidence is inspected and labeled as evidence, not intended
  technical direction.
- The invocation asks for material technical direction such as stack, package
  manager, commands, or integrations before inventing those claims.
- If writing proceeds without answers, provisional content is labeled under
  Assumptions or Unknowns rather than presented as settled technology.
- A default Technology path may be proposed, but ownership is not inferred from
  a familiar basename alone.
- No Intent, design, roadmap, structure, decision, or agent-guidance artifact is
  updated in this technology invocation.

# Scenario: Agent guidance missing material intent

## Request

Use `steer-project` to create compact agent guidance for this repository.

## Fixture

A software-only Project with:

- application code, tests, and a README describing current features
- no Intent Steering artifact and no maintainer-provided purpose or audience
- no agent-guidance artifact
- `.steering.json` absent or lacking an `agent-guidance` mapping

## Evidence profiles

software

## Expected outcome

- Repository evidence is inspected and labeled as evidence, not Intent.
- The invocation asks for material Intent such as purpose or audience before
  inventing a Project summary that depends on those claims.
- If writing proceeds without answers, provisional orientation is labeled under
  Assumptions or Unknowns rather than presented as settled guidance.
- A default agent-guidance path such as `AGENTS.md` may be proposed, but
  ownership is not inferred from a familiar basename alone.
- No Intent, technology, design, roadmap, structure, or decision artifact is
  updated in this agent-guidance invocation.

# Scenario: Structure conflicting evidence

## Request

Use `steer-structure` to align Structure truth with current repository evidence.

## Fixture

A Project with `.steering.json` mapping `structure` to `docs/STRUCTURE.md` and:

- an existing Structure artifact claiming services own packages under `services/`
- observed software layout placing the same modules under a flat `src/` tree
- data notebooks and pipelines organized by team folders that cross those module
  boundaries
- marketing creative assets stored beside application code despite documented
  asset placement rules
- no maintainer confirmation of which ownership or placement policy is intended

## Evidence profiles

software, data, marketing

## Expected outcome

- The adapter distinguishes observed layout from intended ownership and
  placement policy.
- Conflicting organization evidence is not silently reconciled.
- The invocation asks a material question or records an explicit unknown.
- No settled Structure claim is written that chooses one layout policy without
  confirmation.
- If a safe provisional update is made, conflicting interpretations remain
  visible under Assumptions or Unknowns.
- Related work may note Intent, technology, or agent-guidance implications, but
  those artifacts are not edited in this invocation.

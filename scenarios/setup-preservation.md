# Scenario: Setup preserves existing Matt and Steering configuration

## Request

Use `setup-project-steering` to configure Project steering for this repository.

## Fixture

A mixed Project with:

- complete Matt setup output already present: `docs/agents/issue-tracker.md`,
  `docs/agents/domain.md`, triage label docs when triage is installed, and an
  `## Agent skills` block pointing at those docs
- `.steering.json` already mapping Intent, technology, and agent-guidance to
  non-default compatible paths that exist on disk
- software and data evidence available; marketing sparse
- active Steering artifacts already present at the mapped paths

## Evidence profiles

software, data

## Expected outcome

- Compatible Matt setup output is detected and left unchanged.
- Existing `.steering.json` artifact paths are preserved; defaults are not
  proposed for owners that already have mappings.
- The invocation confirms active truth kinds, evidence adapters, and
  intentionally inactive artifacts with the user before writing.
- No empty Steering artifacts are created for inactive kinds.
- `setup-matt-pocock-skills` is not re-run when its output is already complete.

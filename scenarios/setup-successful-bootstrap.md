# Scenario: Setup successfully bootstraps confirmed active artifacts

## Request

Use `setup-project-steering` to set up Project steering from scratch for this
repository.

## Fixture

A data-oriented Project with:

- no Matt setup output yet
- schemas, pipelines, and quality checks as evidence
- required upstream skills available: `setup-matt-pocock-skills`,
  `grill-with-docs`, `steer-project`, and the focused steering adapters
- maintainer confirms Intent, technology, roadmap, and decisions as active;
  Design and marketing evidence intentionally inactive
- material Intent available from the maintainer for active kinds

## Evidence profiles

data

## Expected outcome

- Missing Matt prerequisites are delegated to `setup-matt-pocock-skills` by
  name, then setup continues.
- Existing conventions are inspected; defaults are proposed only when no owner
  exists.
- The user confirms active truth kinds, artifact mappings, evidence adapters,
  and intentionally inactive artifacts.
- Configuration is recorded (including inactive kinds) without creating empty
  artifacts for inactive owners.
- Confirmed active artifacts are bootstrapped through `steer-project`.
- Setup completes with a clear summary of configuration written and artifacts
  bootstrapped.

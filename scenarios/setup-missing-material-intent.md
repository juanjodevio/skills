# Scenario: Setup missing material intent uses grill path

## Request

Use `setup-project-steering` to bootstrap Intent and Design for this
repository.

## Fixture

A software-only Project with:

- complete Matt setup output already present
- application code and README describing current features only
- no maintainer-provided purpose, audience, success criteria, or design
  atmosphere
- user confirms Intent and Design as active truth kinds
- no Steering artifacts at the proposed paths

## Evidence profiles

software

## Expected outcome

- Repository evidence is inspected and labeled as evidence, not Intent or
  Design.
- Missing material bootstrap intent invokes `grill-with-docs` by name rather than creating empty artifacts.
- Setup does not fabricate settled purpose, audience, or design direction.
- After grilling produces material decisions (or explicit unknowns), confirmed
  active artifacts are bootstrapped through `steer-project`.
- Inactive truth kinds remain uncreated.

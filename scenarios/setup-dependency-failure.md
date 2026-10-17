# Scenario: Setup fails when a required upstream skill is missing

## Request

Use `setup-project-steering` to configure Project steering for this repository.

## Fixture

A software-only Project with:

- partial or absent Matt setup output
- the required upstream skill `grill-with-docs` unavailable by name in the
  agent environment
- no `.steering.json`

## Evidence profiles

software

## Expected outcome

- Required upstream skills and capabilities are checked by name and behavior
  before configuration proceeds.
- Missing `grill-with-docs` fails clearly; setup does not invent a reduced
  fallback, empty-artifact bootstrap, or local reimplementation.
- No `.steering.json` is written and no Steering artifacts are created while
  the dependency remains missing.
- Compatible existing repository files remain untouched.

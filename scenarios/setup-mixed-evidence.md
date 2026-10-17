# Scenario: Setup activates mixed evidence adapters together

## Request

Use `setup-project-steering` to configure Project steering for a mixed
initiative.

## Fixture

A mixed Project with:

- complete Matt setup output already present
- software UI surfaces, data contracts/pipelines, and marketing campaign briefs
  all present as evidence
- no `.steering.json` yet
- no Steering artifacts yet

## Evidence profiles

software, data, marketing

## Expected outcome

- Setup inspects existing conventions and evidence before proposing defaults.
- Software, data, and marketing evidence adapters can be activated together;
  the user confirms the active set.
- Confirmed adapters are recorded in Project steering configuration without
  flattening domain meaning into a single profile.
- Artifact mappings and intentionally inactive artifacts are confirmed before
  bootstrap.
- Confirmed active artifacts are bootstrapped through `steer-project` after
  configuration is recorded.

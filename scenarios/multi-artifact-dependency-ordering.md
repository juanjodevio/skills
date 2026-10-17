# Scenario: Multi-artifact dependency ordering

## Request

Use `steer-project` to capture that this Project helps operations leaders
attribute campaigns to pipeline, adopt a warehouse-backed export stack, sequence
the export before campaign automation, record the irreversible warehouse choice
once that trade-off settles, and refresh agent pointers afterward.

## Fixture

A mixed Project with:

- `.steering.json` mapping Intent, technology, roadmap, decisions, and
  agent-guidance to non-default paths
- sparse or absent Steering artifacts at those mapped paths
- software, data, and marketing evidence that supports but does not settle the
  requested changes
- a settled package-manager and warehouse trade-off ready for decision capture
  after technology direction is confirmed

## Evidence profiles

software, data, marketing

## Expected outcome

- The request is classified by durable truth types, not by familiar filenames.
- Focused adapters remain sole owners; `steer-project` routes and orders work
  without absorbing their templates, checks, or ADR eligibility policy.
- Dependent updates run in order: Intent before dependent direction; technology
  (and design when present) before affected roadmap work; eligible decisions
  after their trade-off settles; agent guidance last.
- `domain-modeling` is invoked by name when Domain language settles; it is not
  vendored into the orchestrator.
- Related work discovered mid-flight returns through the orchestrator rather
  than via focused-adapter side calls that bypass ordering.
- Each owning adapter updates only its configured artifact; the orchestrator
  does not edit focused truth directly.

# Scenario: Multi-artifact mixed evidence profiles

## Request

Use `steer-project` to refresh Intent and Design for a Project that ships a
product UI, a warehouse model, and a live campaign in parallel.

## Fixture

A mixed Project with:

- `.steering.json` mapping `intent` and `design` to non-default paths
- software UI surfaces and CSS tokens describing one brand atmosphere
- data contracts and dashboards using different entity names for the same
  audience concept
- marketing briefs and creative assets promising a third tone and audience label
- sparse Intent and Design Steering artifacts at the mapped paths

## Evidence profiles

software, data, marketing

## Expected outcome

- Software, data, and marketing evidence profiles compose; domain meaning is
  not flattened into a single profile's vocabulary.
- Provenance of agreeing and conflicting observations stays visible across
  profiles.
- Intent and Design updates (when safe) preserve profile-specific evidence
  notes rather than letting one profile silently override another.
- Ownership remains with `steer-intent` and `steer-design`; the orchestrator
  routes without absorbing Design or Intent templates.
- Unrelated Roadmap, Structure, decisions, and agent-guidance work may proceed
  independently later and is reported through the orchestrator when relevant.

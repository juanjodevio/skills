# Scenario: Roadmap conflicting evidence

## Request

Use `steer-roadmap` to align Roadmap sequencing with current Project evidence.

## Fixture

A Project with `.steering.json` mapping `roadmap` to `docs/ROADMAP.md` and:

- a stale plan naming campaign automation as Now
- recent commits and open Tickets concentrated on attribution export work
- Intent that still lists automation as an explicit non-goal for this horizon
- a marketing brief treating automation as the immediate priority
- no maintainer confirmation of which sequence is intended

## Evidence profiles

software, data, marketing

## Expected outcome

- Conflicting sequencing evidence is not silently reconciled.
- Priority and sequencing are not inferred from activity alone.
- The invocation asks a material question or records an explicit unknown.
- No settled Roadmap claim chooses Now versus Later without confirmation.
- If a safe provisional update is made, conflicting interpretations remain
  visible under Assumptions or Unknowns.
- Related work may note that Intent, tracker activity, and marketing plans
  disagree, but those artifacts are not edited in this invocation.

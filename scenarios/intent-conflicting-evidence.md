# Scenario: Intent conflicting evidence

## Request

Use `steer-intent` to align Project Intent with current repository evidence.

## Fixture

A Project with `.steering.json` mapping `intent` to `docs/INTENT.md` and:

- product docs claiming the audience is small-business owners
- a data warehouse model and dashboard labeled for enterprise procurement
- a live marketing campaign targeting logistics operations leaders
- no maintainer confirmation of which audience is intended

## Evidence profiles

software, data, marketing

## Expected outcome

- Conflicting audience evidence is not silently reconciled.
- The invocation asks a material question or records an explicit unknown.
- No settled Intent claim is written that chooses one audience without
  confirmation.
- If a safe provisional update is made, conflicting interpretations remain
  visible under Assumptions or Unknowns.
- Related work may note that technology and marketing artifacts disagree, but
  those artifacts are not edited in this invocation.

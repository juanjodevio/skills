# Scenario: Design conflicting evidence

## Request

Use `steer-design` to align Design direction with current repository evidence.

## Fixture

A Project with `.steering.json` mapping `design` to `docs/DESIGN.md` and:

- UI code and screenshots using a dark, high-contrast industrial palette
- a marketing brand kit prescribing light cream surfaces and serif display type
- a data dashboard theme file locking teal accents for charts
- no maintainer confirmation of which visual direction is intended

## Evidence profiles

software, data, marketing

## Expected outcome

- Conflicting visual and brand evidence is not silently reconciled.
- The invocation asks a material question, invokes `grill-with-docs`, or
  records an explicit unknown.
- No settled Design claim is written that chooses one atmosphere or palette
  without confirmation.
- If a safe provisional update is made, conflicting interpretations remain
  visible under Assumptions or Unknowns.
- Related work may note that software, data, and marketing visuals disagree,
  but those artifacts are not edited in this invocation.

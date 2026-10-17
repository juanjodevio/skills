# Scenario: Agent guidance conflicting pointers

## Request

Use `steer-agent-guidance` to align agent guidance with current Steering
artifact mappings.

## Fixture

A Project with `.steering.json` mapping `agent-guidance` to `AGENTS.md` and
`intent` to `docs/INTENT.md`, plus:

- root `AGENTS.md` pointing agents at `docs/PRODUCT.md` for purpose
- `.steering.json` mapping Intent to `docs/INTENT.md` instead
- a second root `CLAUDE.md` with different first-read pointers than `AGENTS.md`
- no maintainer confirmation of which root guidance file or pointer set is
  canonical

## Evidence profiles

software

## Expected outcome

- Conflicting guidance pointers are not silently reconciled.
- The invocation asks a material question or records an explicit unknown about
  which orientation file and pointer set to trust.
- No settled guidance claim chooses one conflicting pointer set without
  confirmation.
- Compatible root conventions remain candidates through configured mappings
  rather than being overwritten by assumed basenames.
- Intent, technology, and decision artifacts are not edited in this invocation;
  conflicts may be reported as related work.

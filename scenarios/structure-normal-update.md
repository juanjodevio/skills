# Scenario: Structure normal update

## Request

Use `steer-project` to record that application code lives under `src/`, domain
modules own their packages, tests mirror source under `tests/`, and build
outputs under `dist/` must not be edited by hand.

## Fixture

A mixed Project with:

- `.steering.json` mapping `structure` to `docs/REPO_MAP.md`
- an empty or sparse Structure Steering artifact at that mapped path
- software packages under `src/` with tests under `tests/`
- data pipeline directories that follow the same ownership boundaries
- marketing asset folders that already respect a named placement convention
- a Domain model that names the major modules

## Evidence profiles

software, data, marketing

## Expected outcome

- Ownership is classified as Structure and routed through `steer-structure`.
- The configured artifact path is used; the physical filename is not assumed.
- Observed layout is inspected as evidence and not treated as settled ownership
  or placement policy without confirmation when material intent is ambiguous.
- Structure truth stays concise and navigational rather than a full inventory.
- Module ownership and placement rules use Domain-model language.
- Generated and temporary conventions are recorded without duplicating
  technology truth.
- Only the Structure Steering artifact is updated.
- Related Intent, technology, design, roadmap, decision, or agent-guidance work
  is reported rather than performed in this invocation.

# Project Intent

## Purpose

Ship a full suite of agent skills that keep durable Project truth accurate
across software, data, and marketing work, and carry settled intent into the
Work lifecycle — without vendoring upstream lifecycle skills or depending on
Superpowers.

## Audiences And Stakeholders

- Maintainers configuring Project steering on their own Projects
- Coding agents on Cursor, Codex, and Claude Code that load and run the suite
- This repository’s maintainer, for packaging and inventory quality

## Desired Outcomes

- Durable truth stays accurate and discoverable for humans and agents
- Setup → `steer-project` → `deliver-work` is the default path
- Mixed Projects can compose software, data, and marketing evidence without
  flattening domains
- Packaging stays skills-pack compatible: full suite only, inventory checks, no
  committed skill-behavior scenario catalog

## Core Journeys

1. Install the full suite → run `setup-project-steering` → bootstrap active
   Steering artifacts
2. Update durable truth via `steer-project` or a focused adapter
3. Shape and execute work via `deliver-work`
4. Maintain packaging: edit `skills/`, validate with scripts and tests

## Scope

### In Scope

- Catalog modules: `setup-project-steering`, `steer-project` and focused
  adapters, `deliver-work`
- Suite docs, Domain language (`GLOSSARY.md`, ADRs), and maintainer packaging
  (`scripts/`, `dev/`, tests)

### Out Of Scope

- Superpowers dependency
- Vendored copies of upstream lifecycle skills (`grill-with-docs`,
  `to-spec`, `implement-spec`, and the rest listed in `docs/installation.md`)
- Focused or partial suite install
- Committed skill-behavior scenario catalog (editorial review and real Project
  use instead)
- A UI or `docs/DESIGN.md` for this skills pack itself

## Success Signals

- Full-suite install works on Cursor, Codex, and Claude Code
- Inventory validation stays green (`list-skills`, `validate_package`, unit
  tests)
- Projects can configure `.steering.json` then use `steer-project` and
  `deliver-work` without focused standalone installs

## Assumptions

- Confirmed in setup grilling (2026-10-17); README and ADR-0001 align with this
  Intent

## Last Reviewed

2026-10-17 by setup-project-steering bootstrap (maintainer-confirmed grill)

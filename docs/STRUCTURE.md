# Repository Structure

## Overview

Installable skills live under `skills/`. Suite docs, Domain language, agent
setup docs, and ADRs live under `docs/` and the repo root. Maintainer packaging
lives in `scripts/`, `tests/`, and `dev/` and is not part of the `npx skills`
install surface.

## Major Areas

- `skills/`: discoverable suite modules (`SKILL.md` + `references/`); sole
  installable content for `npx skills add`
- `docs/`: human/agent suite docs (catalog, install, migration, work tracker,
  design-md attribution)
- `docs/agents/`: tracker, triage, and Domain setup docs
- `docs/adr/`: decision records and status-bearing index
- `scripts/`: packaging inventory scripts
- `tests/`: packaging/inventory unit tests
- `dev/`: maintainer suite contract (`steering-suite.json`); not installed
- Root: `README.md`, `GLOSSARY.md`, `AGENTS.md`, `CLAUDE.md`, `.steering.json`

## Ownership Boundaries

- **Installable skills**: only `skills/<name>/`; do not place installable skills
  under `dev/` or `docs/`
- **Durable Project truth**: configured Steering artifacts (see `.steering.json`);
  do not duplicate their content into `AGENTS.md`
- **Tracker / triage / Domain setup**: `docs/agents/` and the `## Agent skills`
  block; do not reimplement that setup inside suite skills
- **Domain language**: `GLOSSARY.md` and ADRs; skills use glossary terms

## Placement Rules

- New suite skill: `skills/<skill-name>/SKILL.md` (+ `references/` as needed)
- Tests: `tests/` for packaging/inventory checks
- Docs: suite guidance under `docs/`; tracker/triage/Domain docs under
  `docs/agents/`
- Scripts: packaging helpers under `scripts/`
- Suite inventory contract: `dev/steering-suite.json`
- Generated and temporary content: keep out of `skills/`; prefer ignore patterns
  for local scratch

## Naming Conventions

- Public skill directory name equals frontmatter `name`
- Approved public names only (see `docs/catalog.md` / `docs/migration.md`)
- Steering truth kinds map through `.steering.json`, not assumed basenames

## Assumptions

- Observed layout after the ADR-0001 rebuild is intended structure policy unless
  the maintainer changes it

## Last Reviewed

2026-10-17 by setup-project-steering bootstrap

## Agent skills

### Issue tracker

Issues live in Linear team **P&P** (`PAN`), via the Linear MCP. See `docs/agents/issue-tracker.md`.

### Triage labels

Canonical roles use same-named labels: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: root `GLOSSARY.md` and `docs/adr/`. See `docs/agents/domain.md`.

### Project steering suite

Full suite only. Catalog, install, migration, Work tracker, and `design-md`
attribution: `docs/catalog.md`, `docs/installation.md`, `docs/migration.md`,
`docs/work-tracker.md`, `docs/design-md.md`. Default entrypoint `steer-project`;
default Work lifecycle `deliver-work`.

## Project steering

Configuration: `.steering.json`. Design is inactive for this Project.

### First reads

- Intent: `docs/INTENT.md`
- Technology: `docs/TECH.md`
- Structure: `docs/STRUCTURE.md`
- Roadmap: `docs/ROADMAP.md`
- Decisions: `docs/adr/` (index: `docs/adr/index.md`)
- Domain language: `GLOSSARY.md`

### Agent workflow

- Change durable truth only in its owning Steering artifact; keep this file as
  pointers.
- Commands and stack: `docs/TECH.md`. Layout and placement: `docs/STRUCTURE.md`.
- Ask before changing Intent, roadmap priority, public skill contracts, or
  accepted ADR direction.
- Before software or data Ticket implementation (`implement-spec`): read
  [Implementation discipline](docs/agents/implementation-discipline.md).

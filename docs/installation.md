# Installation

Install the **full suite**. Focused standalone installation of individual
Project steering modules is **unsupported**. Every consuming Project should
receive the complete discoverable inventory listed in [catalog](catalog.md).

## Full suite install

### Global (Cursor, Codex, Claude Code)

```sh
npx skills add juanjodevio/skills -g -a cursor -a codex -a claude-code --skill '*'
```

### Project-local

```sh
npx skills add juanjodevio/skills -a cursor -a codex -a claude-code --skill '*'
```

Use `--copy` when symlinks are unavailable:

```sh
npx skills add juanjodevio/skills -g -a cursor -a codex -a claude-code --skill '*' --copy
```

## Discoverability after install

After a full-suite install, each vendor should discover every module under its
agent skills path:

| Agent | `--agent` | Global path | Project path |
| --- | --- | --- | --- |
| Cursor | `cursor` | `~/.cursor/skills/` | `.agents/skills/` |
| Codex | `codex` | `~/.codex/skills/` | `.agents/skills/` |
| Claude Code | `claude-code` | `~/.claude/skills/` | `.claude/skills/` |

Confirm discovery:

```sh
npx skills add juanjodevio/skills --list
npx skills ls -g -a cursor -a codex -a claude-code
```

Expected public names after install:

- `setup-project-steering`
- `steer-project`
- `steer-intent`
- `steer-design`
- `steer-technology`
- `steer-roadmap`
- `steer-structure`
- `steer-decisions`
- `steer-agent-guidance`
- `deliver-work`

Obsolete legacy public names must not appear after install. See
[migration](migration.md) for the removed-name map.

## Required external Matt dependencies

This suite reuses compatible Matt Pocock skills **by name**. Do not vendor or
copy their implementations into this repository. Before setup or Work lifecycle
runs, these capabilities must be available where the agent loads skills:

| Skill (by name) | Needed for |
| --- | --- |
| `setup-matt-pocock-skills` | Tracker, triage, Domain docs, and ADR prerequisites |
| `grill-with-docs` | Missing material Intent during setup or shaping |
| `domain-modeling` | Settling Domain language and ADRs |
| `to-spec` | Specification synthesis |
| `to-tickets` | Ticket decomposition |
| `implement-spec` | Ticket-graph execution on the integration branch |
| `retro` | Retrospective learning from work actually performed |
| `writing-for-agents` | Compact agent-guidance prose |

Capability checks:

1. Confirm each required name resolves in the agent’s skill loader.
2. If a name is missing, stop and report it; do not invent a local substitute.
3. Do not add Superpowers dependencies.

## First use after install

1. Run `setup-project-steering` once per Project to write `.steering.json` and
   bootstrap active Steering artifacts.
2. Use `steer-project` as the default Project steering entrypoint.
3. Use `deliver-work` as the default Work lifecycle coordinator.
4. Invoke focused adapters only when one truth kind is clearly in scope.

## Maintainer packaging

`npx skills add` installs `skills/` only. Maintainer inventory checks:

```sh
./scripts/list-skills.sh
python3 scripts/validate_package.py
```

The slim suite contract lives at `dev/steering-suite.json` (not installed).

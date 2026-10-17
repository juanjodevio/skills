# Project Technology

## Technical Summary

This Project is a skills pack, not an application runtime. The installable
surface is Markdown skills under `skills/`, distributed with the
[`skills`](https://github.com/vercel-labs/skills) CLI (`npx skills`). Maintainer
inventory checks use Python 3 scripts and unittest. Work tracking for this
repository uses Linear via MCP.

## Tools And Platforms

- **Distribution**: `npx skills add|use|ls|update|remove` (Node/npx; no
  `package.json` in this repo)
- **Validation runtime**: Python 3 (`scripts/validate_package.py`,
  `python3 -m unittest`)
- **Suite contract**: `dev/steering-suite.json` (not installed by `npx skills`)
- **Target agents**: Cursor, Codex, Claude Code
- **Work tracker**: Linear (team P&P / `PAN`) via Linear MCP — see
  `.steering.json` `workTracker` and `docs/agents/issue-tracker.md`

## Commands

```sh
# Discover / install (consumer Projects)
npx skills add juanjodevio/skills -g -a cursor -a codex -a claude-code --skill '*'
npx skills add juanjodevio/skills --list
npx skills ls -g -a cursor -a codex -a claude-code

# Maintainer inventory
./scripts/list-skills.sh
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
```

## Integrations And Services

- Linear MCP for Specifications, Tickets, labels, and comments
- Upstream lifecycle skills loaded by name from the agent’s skill paths (not
  vendored here); see `docs/installation.md`

## Constraints And Conventions

- Full-suite install only; focused standalone install is unsupported
- Do not vendor upstream lifecycle skills or add Superpowers dependencies
- Skill behavior is not scenario-tested in-repo; quality is editorial plus use
  in real Projects
- Obsolete public names must not appear after install (see `docs/migration.md`)

## Assumptions

- Python 3 on PATH for maintainer checks; exact minimum version not pinned
- Consumer environments provide `npx` and the `skills` CLI

## Unknowns

- Whether a pinned Python version or CI host matrix should be recorded later

## Last Reviewed

2026-10-17 by setup-project-steering bootstrap (software evidence + docs)

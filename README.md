# skills

Reusable agent skills for **Project steering** and carrying settled intent into
planned work.

This repository is a skill suite for keeping durable Project truth accurate
across software, data, and marketing work, and for coordinating the default
Work lifecycle. It targets the open agent skills ecosystem and installs with
the [`skills`](https://github.com/vercel-labs/skills) CLI.

Primary target agents: Cursor, Codex, and Claude Code.

## Quick Start

Install the **full suite** globally for Cursor, Codex, and Claude Code:

```sh
npx skills add juanjodevio/skills -g -a cursor -a codex -a claude-code --skill '*'
```

Focused standalone installation is unsupported. See
[docs/installation.md](docs/installation.md).

After install, skills are discoverable under each agent’s skills path
(`~/.cursor/skills/`, `~/.codex/skills/`, `~/.claude/skills/` globally, or the
project-local paths listed in the installation guide).

## Docs

| Doc | Purpose |
| --- | --- |
| [docs/catalog.md](docs/catalog.md) | Full module catalog; Work lifecycle vs Situational skills |
| [docs/installation.md](docs/installation.md) | Full-suite install, discoverability, Matt dependencies |
| [docs/migration.md](docs/migration.md) | Legacy name → replacement map |
| [docs/work-tracker.md](docs/work-tracker.md) | Linear, GitHub, GitLab, Jira, local Markdown, custom |
| [docs/design-md.md](docs/design-md.md) | `design-md` attribution; Stitch is not required |
| [GLOSSARY.md](GLOSSARY.md) | Domain language |
| [docs/adr/0001-rebuild-as-cross-domain-project-steering-suite.md](docs/adr/0001-rebuild-as-cross-domain-project-steering-suite.md) | Accepted architecture |

## Install Options

### Global Install

```sh
npx skills add juanjodevio/skills -g -a cursor -a codex -a claude-code --skill '*'
```

| Agent | `--agent` | Global Path |
| --- | --- | --- |
| Cursor | `cursor` | `~/.cursor/skills/` |
| Codex | `codex` | `~/.codex/skills/` |
| Claude Code | `claude-code` | `~/.claude/skills/` |

### Project-Local Install

```sh
npx skills add juanjodevio/skills -a cursor -a codex -a claude-code --skill '*'
```

| Agent | `--agent` | Project Path |
| --- | --- | --- |
| Cursor | `cursor` | `.agents/skills/` |
| Codex | `codex` | `.agents/skills/` |
| Claude Code | `claude-code` | `.claude/skills/` |

### Copy Instead Of Symlink

```sh
npx skills add juanjodevio/skills -g -a cursor -a codex -a claude-code --skill '*' --copy
```

## Use Without Installing

```sh
npx skills use juanjodevio/skills --skill steer-project --agent cursor
npx skills use juanjodevio/skills --skill deliver-work --agent claude-code
npx skills use juanjodevio/skills --skill setup-project-steering --agent codex
```

## Skill Catalog (summary)

Use `steer-project` as the default Project steering entrypoint. Use
`deliver-work` as the default Work lifecycle. Use `setup-project-steering` once
per Project for configuration. Invoke focused adapters when one truth kind is
clearly in scope. Full detail: [docs/catalog.md](docs/catalog.md).

| Skill | Purpose |
| --- | --- |
| `setup-project-steering` | Configure `.steering.json`, tracker mappings, and bootstrap. |
| `steer-project` | Shared Steering workflow and multi-artifact orchestration. |
| `steer-intent` | Intent Steering artifact. |
| `steer-technology` | Technology Steering artifact. |
| `steer-design` | Design Steering artifact (`design-md` pattern). |
| `steer-roadmap` | Roadmap Steering artifact. |
| `steer-structure` | Structure Steering artifact. |
| `steer-decisions` | Decision records / ADRs. |
| `steer-agent-guidance` | Compact agent guidance pointers. |
| `deliver-work` | Default Work lifecycle coordinator. |

**Work lifecycle vs Situational skills:** `deliver-work` is the default path from
unresolved intent through grilling, Specification, Tickets, `implement-spec`,
and `retro`. Those Matt skills are **lifecycle stages** reused by name, not
Situational. Situational skills (`handoff`, `wait-what`, architecture review)
are invoked only when needed. Focused steering adapters update durable truth
outside the Work lifecycle. See the catalog.

## How The Suite Works

1. `setup-project-steering` records artifact paths, evidence adapters, and Work
   tracker mappings.
2. `steer-project` inspects evidence, classifies ownership, resolves material
   unknowns, updates one artifact at a time, checks consistency, and reports
   related work.
3. Focused adapters supply ownership and validation for one truth kind each.
4. `deliver-work` coordinates grilling, Specification, Tickets, Frontier
   execution, and retrospective via Matt skills by name.

External Matt dependencies are documented in
[docs/installation.md](docs/installation.md). This suite does not vendor them
and does not depend on Superpowers.

## Common Workflows

Bootstrap Project steering:

```text
Use setup-project-steering to configure this Project, then steer-project to
bootstrap the active Steering artifacts.
```

Update durable technology direction:

```text
Use steer-project (or steer-technology). We switched package managers and need
TECH/technology truth, then related agent guidance, updated.
```

Capture a durable decision:

```text
Use steer-decisions to record that Design follows the design-md pattern and
Stitch is not required.
```

Shape and execute work:

```text
Use deliver-work to take this idea through grill, Specification, Tickets, and
implement-spec, then retro.
```

## Supported Agents

| Vendor | Agent ID |
| --- | --- |
| Cursor | `cursor` |
| Codex / ChatGPT coding-agent tooling | `codex` |
| Claude Code | `claude-code` |

See the full
[supported agents list](https://github.com/vercel-labs/skills#supported-agents).

## Update And Remove

```sh
npx skills ls -g -a cursor -a codex -a claude-code
npx skills update -g
npx skills remove --all
```

Migrating from the legacy suite? Read [docs/migration.md](docs/migration.md).

## Troubleshooting

```sh
npx skills add juanjodevio/skills --list
```

If no skills are found:

- Verify each skill lives at `skills/<name>/SKILL.md`.
- Verify each `SKILL.md` has YAML frontmatter with `name` and `description`.
- Confirm discovery before installing.

If a skill does not load:

- Verify install paths for `cursor`, `codex`, and `claude-code`.
- Use `--copy` when symlinks fail.
- Check the agent’s skill-loading documentation.

## Contributing And Skill Format

```text
skills/
  steer-project/
    SKILL.md
  deliver-work/
    SKILL.md
```

```yaml
---
name: my-skill
description: What this skill does and when to use it.
---
```

Keep skill bodies focused. Put larger templates in `references/`.

The installable surface is `skills/`. Maintainer packaging lives in `scripts/`
and `dev/` (suite inventory contract). Skill behavior is not scenario-tested;
quality is editorial plus use in real Projects (Matt-style). Validate inventory
with:

```sh
./scripts/list-skills.sh
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
```

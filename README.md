# skills

Reusable agent skills for product steering and durable project documentation.

This repository is a skill suite for keeping product intent, repo structure,
technical decisions, design context, roadmaps, ADRs, and agent instructions in
sync. It is designed for the open agent skills ecosystem and can be installed
with the [`skills`](https://github.com/vercel-labs/skills) CLI.

The primary target agents are Cursor, Codex, and Claude Code.

## Quick Start

Install the full suite globally for Cursor, Codex, and Claude Code:

```sh
npx skills add juanjodevio/skills -g -a cursor -a codex -a claude-code --skill '*'
```

This installs every skill in this repository so `product-steering` can route to
the focused `steer-*` skills when needed.

## Install Options

### Global Install

Use a global install when you want these skills available across projects:

```sh
npx skills add juanjodevio/skills -g -a cursor -a codex -a claude-code --skill '*'
```

Global target paths for the main vendors:

| Agent | `--agent` | Global Path |
| --- | --- | --- |
| Cursor | `cursor` | `~/.cursor/skills/` |
| Codex | `codex` | `~/.codex/skills/` |
| Claude Code | `claude-code` | `~/.claude/skills/` |

### Project-Local Install

Use a project-local install when a consuming repository should carry its own
skill installation:

```sh
npx skills add juanjodevio/skills -a cursor -a codex -a claude-code --skill '*'
```

Project target paths for the main vendors:

| Agent | `--agent` | Project Path |
| --- | --- | --- |
| Cursor | `cursor` | `.agents/skills/` |
| Codex | `codex` | `.agents/skills/` |
| Claude Code | `claude-code` | `.claude/skills/` |

### Install A Specific Skill

Normal users should install the full suite. Install a focused skill directly
only when you know the task belongs to one artifact workflow.

```sh
npx skills add juanjodevio/skills -g -a cursor --skill product-steering
npx skills add juanjodevio/skills -g -a cursor --skill steer-adr
```

### Copy Instead Of Symlink

The `skills` CLI prefers symlinks so installed skills share one source of truth.
If symlinks are not supported in your environment, add `--copy`:

```sh
npx skills add juanjodevio/skills -g -a cursor -a codex -a claude-code --skill '*' --copy
```

## Use Without Installing

Try one skill without installing it:

```sh
npx skills use juanjodevio/skills --skill product-steering --agent cursor
npx skills use juanjodevio/skills --skill product-steering --agent claude-code
npx skills use juanjodevio/skills --skill steer-adr --agent codex
```

`skills use` resolves the source, loads the selected skill into a temporary
directory, and starts or prepares the requested agent flow.

## Skill Catalog

Use `product-steering` as the default entrypoint. Use a focused `steer-*` skill
directly only when the task clearly belongs to one artifact.

| Skill | Purpose |
| --- | --- |
| `product-steering` | Orchestrates product steering docs, ADRs, drift checks, and agent instructions. |
| `steer-product` | Maintains `docs/PRODUCT.md`. |
| `steer-structure` | Maintains `docs/STRUCTURE.md`. |
| `steer-tech` | Maintains `docs/TECH.md`, including package manager and commands. |
| `steer-design` | Maintains canonical `docs/DESIGN.md` for Stitch-compatible design context. |
| `steer-roadmap` | Maintains `docs/ROADMAP.md`. |
| `steer-adr` | Manages `docs/adr` with `adr-tools` and compact MADR conventions. |
| `steer-agents` | Keeps root `AGENTS.md` compact and pointer-based. |

## How The Suite Works

`product-steering` is the router. It inspects the repository, classifies the
request, asks structured questions when intent is missing, and routes work to
the focused skills:

- Product purpose, users, scope, workflows, and success criteria go to
  `steer-product`.
- Repository layout, boundaries, ownership, and placement rules go to
  `steer-structure`.
- Stack, package manager, commands, dependencies, integrations, and constraints
  go to `steer-tech`.
- Design context, UI direction, accessibility, and Stitch-compatible
  `DESIGN.md` guidance go to `steer-design`.
- Now/next/later priorities, non-goals, risks, and sequencing go to
  `steer-roadmap`.
- Durable product, technical, design, or roadmap decisions go to `steer-adr`.
- Root agent instructions and durable-doc pointers go to `steer-agents`.

The focused skills keep each artifact small and clear. The entrypoint keeps the
whole steering system aligned.

## Common Workflows

After installing the suite, ask your agent for workflows like these.

Bootstrap product steering in a repo:

```text
Use product-steering to set up PRODUCT.md, STRUCTURE.md, TECH.md, DESIGN.md,
ROADMAP.md, docs/adr, and a compact AGENTS.md for this repo.
```

Update package-manager and command truth:

```text
Use product-steering. We switched from npm to pnpm and added pnpm build.
Update TECH.md, AGENTS.md, and capture an ADR if this is a durable repo-wide
decision.
```

Capture a durable decision:

```text
Use steer-adr to record that docs/DESIGN.md is the canonical Stitch design
context and should be symlinked into frontend/DESIGN.md when needed.
```

Maintain design context:

```text
Use steer-design to refresh docs/DESIGN.md for the current UI direction and
flag any unknown accessibility or visual-system decisions.
```

Review drift before editing:

```text
Use product-steering to review steering drift. Compare docs, package manifests,
ADRs, ROADMAP.md, DESIGN.md, and AGENTS.md. Tell me what should change before
editing.
```

## Supported Agents

This README focuses on the user's primary vendors:

| Vendor | Agent ID |
| --- | --- |
| Cursor | `cursor` |
| Codex / ChatGPT coding-agent tooling | `codex` |
| Claude Code | `claude-code` |

The `skills` CLI supports many more agents. See the full
[supported agents list](https://github.com/vercel-labs/skills#supported-agents).

## Update And Remove

List installed skills:

```sh
npx skills ls -g -a cursor -a codex -a claude-code
```

Update all global skills:

```sh
npx skills update -g
```

Update one skill:

```sh
npx skills update -g product-steering
```

Remove one skill from all agents:

```sh
npx skills remove product-steering --agent '*'
```

Remove all installed skills:

```sh
npx skills remove --all
```

## Troubleshooting

Check that the CLI can discover this repository's skills:

```sh
npx skills add juanjodevio/skills --list
```

If no skills are found:

- Verify each skill lives at `skills/<name>/SKILL.md`.
- Verify each `SKILL.md` has YAML frontmatter with `name` and `description`.
- Run the list command above to confirm discovery before installing.

If a skill does not load in an agent:

- Verify it was installed to the expected agent path.
- Re-run install with explicit `-a cursor`, `-a codex`, or `-a claude-code`.
- Use `--copy` if your environment does not support symlinks.
- Check the agent's own skill-loading documentation if the files are present but
  not being loaded.

If commands look stale:

- Update the installed skills with `npx skills update -g`.
- Reinstall from `juanjodevio/skills` if you changed install scope or agent
  targets.

## Contributing And Skill Format

Skills are directories containing a `SKILL.md` file:

```text
skills/
  product-steering/
    SKILL.md
  steer-adr/
    SKILL.md
```

Each `SKILL.md` needs frontmatter:

```yaml
---
name: my-skill
description: What this skill does and when to use it.
---
```

Keep skill bodies focused. Put larger reusable templates or references in a
local `references/` directory and link to them from the skill.

Generated evaluation files and workspaces are intentionally ignored and should
not be committed. Commit skill source files, references, and user-facing docs.
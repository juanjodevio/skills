---
name: steer-agents
description: Maintain root AGENTS.md as the compact agent-facing orientation file. Use this skill whenever the user asks to create or update AGENTS.md, agent instructions, coding-agent guidance, repo memory pointers, safety boundaries, canonical commands for agents, or when steering docs change and future agents need to know where to read the durable truth.
---

# Steer Agents

Maintain root `AGENTS.md`. This file should help agents start safely and find the right durable docs. It should not become a duplicate wiki.

## Ownership

Own agent-facing orientation:

- short project summary
- first-read steering docs
- canonical commands when known
- workflow expectations
- safety and approval boundaries
- pointers to `docs/PRODUCT.md`, `docs/STRUCTURE.md`, `docs/TECH.md`, `docs/DESIGN.md`, `docs/ROADMAP.md`, and `docs/adr/`
- instruction to update source docs when durable truth changes

Do not duplicate detailed product, roadmap, tech, design, or ADR content.

## Workflow

1. Read root `AGENTS.md` if it exists.
2. Read steering docs that are relevant to the requested update.
3. Inspect package/tooling files only when command guidance is missing or stale.
4. Use `AskQuestionTool` where possible for bounded approval boundaries, command policy, or first-read choices.
5. Ask in plain text for open-ended operating preferences.
6. Update `AGENTS.md` to stay compact and pointer-based.
7. Report any source docs that should be updated instead of duplicating content in `AGENTS.md`.

## Suggested Structure

When creating root `AGENTS.md` from scratch or normalizing a sparse file, read `references/agents-template.md`.

Use this structure unless the repo already has a strong convention:

- Project Summary
- First Reads
- Commands
- Agent Workflow
- Safety And Approval Boundaries
- Durable Truth Maintenance

Keep it short. A good root `AGENTS.md` tells an agent where to look and what not to do.

## Command Guidance

Include exact commands only when they are known. If package manager or commands are unclear, route to `steer-tech` first.

When commands change, update `docs/TECH.md` as the source of truth and keep `AGENTS.md` as a concise pointer plus the most common commands.

## Self-Check

Before finishing, check that:

- `AGENTS.md` links to the steering docs instead of copying them
- commands match `docs/TECH.md` and repo manifests
- safety boundaries are clear
- durable-truth maintenance is explicit
- no stale tool-specific rules are presented as universal
- local links are valid where practical

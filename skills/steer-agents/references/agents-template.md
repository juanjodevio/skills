# Minimal AGENTS.md Template

# AGENTS.md

## Project Summary

Short project orientation for coding agents.

## First Reads

- `docs/PRODUCT.md` for product purpose, users, scope, and success criteria.
- `docs/STRUCTURE.md` for repository layout and placement rules.
- `docs/TECH.md` for stack, package manager, commands, dependencies, and constraints.
- `docs/DESIGN.md` for design context and UI direction.
- `docs/ROADMAP.md` for now/next/later priorities and non-goals.
- `docs/adr/` for durable implementation-shaping decisions.

## Commands

- Install:
- Lint:
- Test:
- Build:

Keep detailed command truth in `docs/TECH.md`.

## Agent Workflow

- Read the relevant steering docs before changing durable behavior.
- Update the source steering doc when durable truth changes.
- Prefer focused changes that respect documented boundaries.

## Safety And Approval Boundaries

- Ask before changing product intent, roadmap priority, public contracts, security posture, or accepted ADR direction.
- Do not rewrite accepted ADRs; supersede them with a new ADR.

## Durable Truth Maintenance

`AGENTS.md` points to truth; it should not duplicate the steering docs.

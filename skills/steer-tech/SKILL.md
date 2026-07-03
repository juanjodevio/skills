---
name: steer-tech
description: Maintain docs/TECH.md as the technical source of truth. Use this skill whenever the user asks about stack, runtimes, package manager, install/test/build commands, dependencies, integrations, deployment targets, technical constraints, or when a tooling decision such as npm to pnpm should be reflected for future agents.
---

# Steer Tech

Maintain `docs/TECH.md`. This file tells future agents how the project is built, checked, and constrained.

## Ownership

Own technical truth:

- stack and runtimes
- package manager and lockfile expectations
- install, lint, test, typecheck, build, and validation commands
- important dependencies and why they exist
- integrations, APIs, services, and deployment targets
- non-obvious implementation constraints
- assumptions and unknowns
- last-reviewed metadata

Do not duplicate product scope from `docs/PRODUCT.md`, repo placement rules from `docs/STRUCTURE.md`, or roadmap sequencing from `docs/ROADMAP.md`.

## Workflow

1. Read `docs/TECH.md` if it exists.
2. Inspect package files, lockfiles, config files, CI, scripts, and dependency manifests.
3. Treat config and scripts as evidence for commands and package manager.
4. Use `AskQuestionTool` where possible for bounded missing choices, such as package manager policy, supported runtime, or whether an integration is official.
5. Ask in plain text for open-ended technical rationale.
6. Update only `docs/TECH.md`.
7. If the change is a durable technical decision, such as a repo-wide package manager switch, propose or create an ADR through `steer-adr`.
8. Return cross-doc follow-ups for `AGENTS.md`, ADRs, structure, or roadmap.

## Suggested Structure

When creating `docs/TECH.md` from scratch or normalizing a sparse file, read `references/tech-template.md`.

Use this structure unless the repo already has a strong convention:

- Technical Summary
- Stack And Runtimes
- Package Manager
- Commands
- Dependencies
- Integrations And Services
- Constraints And Conventions
- Assumptions
- Unknowns
- Last Reviewed

Commands should be exact when known. If a command is inferred but unverified, mark it as unverified.

## ADR Triggers

Consider ADR capture when a change affects:

- package manager or runtime policy
- primary framework or database
- deployment architecture
- integration architecture
- public API contracts
- security or compliance posture
- test strategy that materially affects implementation

Small dependency additions usually do not need ADRs unless they establish a durable pattern.

## Self-Check

Before finishing, check that:

- package manager claims match lockfiles and scripts
- commands are exact or clearly marked unverified
- durable technical decisions were routed to ADR consideration
- `AGENTS.md` follow-ups are reported when commands change
- local links are valid where practical
- `Last Reviewed` is present or intentionally preserved

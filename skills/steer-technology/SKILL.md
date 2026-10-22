---
name: steer-technology
description: Steer durable Project technology through the shared Steering workflow. Use this focused adapter for tools, platforms, commands, integrations, constraints, assumptions, and unknowns.
---

# Steer Technology

Maintain the Steering artifact configured for `technology`. Delegate the common
process to `steer-project`; this adapter supplies technology ownership and
validation rather than a second workflow.

## Ownership

Technology owns:

- tools, platforms, runtimes, and stack choices in force for the Project
- install, lint, test, typecheck, build, validate, and operational commands
- integrations, APIs, services, channels, and attribution tooling that bind
  the Project to external systems
- non-obvious technical constraints, conventions, and run limits
- confirmed assumptions and material unknowns about technical direction

Technology does not own Project purpose or audiences, design semantics,
delivery sequence, physical repository layout, decision history, or agent
instructions. Classify those as related work for their owning adapters.
Route durable decision capture to decision steering; do not copy eligibility
rules here.

## Evidence By Profile

Inspect every profile the Project supports. Label findings as evidence; never
promote repository state to intended technical direction without confirmation.

### Software

Manifests and lockfiles, automation and CI, configuration, tests, and recent
commits that show how the Project is built, checked, and constrained.

### Data

Platforms and warehouses, pipelines and orchestration, schemas and catalogs,
quality checks, and run constraints that show how data work is executed.

### Marketing

Platforms and channels, integrations between campaign and product systems,
attribution tooling, and operational constraints on publishing or measurement.

## Procedure

1. Invoke the shared Steering workflow in `steer-project`.
2. Resolve `technology` through `.steering.json`; do not assume the artifact is
   named `TECH.md`, `docs/TECH.md`, or any other physical name. Preserve an
   existing compatible technology artifact when the mapping points at it.
3. Inspect the relevant software, data, and marketing evidence profiles using
   the sources above.
4. Ask only questions whose answers materially affect technology. In particular,
   confirm stack, package manager or platform policy, commands, integrations,
   or constraints when evidence is absent or conflicting.
5. When the maintainer cannot answer and a safe update remains possible, label
   provisional claims under `Assumptions` and unanswered decisions under
   `Unknowns`. Do not present either as settled technical direction.
6. Update only the configured Technology Steering artifact, using the existing
   structure or [Technology template](references/technology-template.md).
7. Run the shared validation, consistency check, and related-work report.
   Report decision-steering follow-ups when a change looks like a durable
   technical decision rather than recording eligibility criteria here.

## Self-Check

- Every settled claim comes from confirmed technical direction or an explicit,
  current source of that direction.
- Repository evidence is not promoted to intended tools, platforms, commands,
  or constraints.
- Material conflicts and missing technical direction caused questions or
  explicit unknowns.
- Software, data, and marketing evidence appropriate to the Project was
  inspected without inventing unsupported domain claims.
- Related decisions are reported for decision steering; ADR eligibility is not
  restated in this adapter.
- Intent, design, roadmap, structure, and agent-guidance changes are reported
  as related work rather than edited in this invocation.
- The update contains assumptions, unknowns, and last-reviewed metadata when
  relevant, without adding empty ceremonial sections.

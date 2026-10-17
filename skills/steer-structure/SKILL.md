---
name: steer-structure
description: Steer durable repository Structure through the shared Steering workflow. Use this focused adapter for organization, module ownership, placement rules, naming conventions, and generated-content conventions.
---

# Steer Structure

Maintain the Steering artifact configured for `structure`. Delegate the common
process to `steer-project`; this adapter supplies Structure ownership and
validation rather than a second workflow.

## Ownership

Structure owns:

- repository organization and meaningful relationships between major areas
- module, package, or area ownership and responsibility boundaries
- placement rules for new code, tests, docs, assets, scripts, and similar work
- naming conventions that guide where work belongs
- generated and temporary content conventions that keep source and artifacts apart

Structure does not own technology choices or commands, Project purpose or scope,
delivery sequence, design semantics, decision history, or agent instructions.
Classify those as related work for their owning adapters.

## Procedure

1. Invoke the shared Steering workflow in `steer-project`.
2. Resolve `structure` through `.steering.json`; do not assume the artifact is
   named `STRUCTURE.md`, `docs/STRUCTURE.md`, or any other physical name.
3. Inspect the relevant software, data, and marketing evidence profiles. Treat
   the observed tree and package layout as evidence of current organization, not
   as proof of intended ownership or placement policy.
4. Ask only questions whose answers materially affect Structure. In particular,
   confirm ownership boundaries, placement policy, naming, or generated-content
   conventions when evidence is absent or conflicting.
5. When the maintainer cannot answer and a safe update remains possible, label
   provisional claims under `Assumptions` and unanswered decisions under
   `Unknowns`. Do not present either as settled Structure truth.
6. Update only the configured Structure Steering artifact, using the existing
   structure or [Structure template](references/structure-template.md). Keep the
   artifact concise and navigational; do not expand it into a full file
   inventory. Prefer Domain-model terms for module ownership and placement.
7. Run the shared validation, consistency check, and related-work report.
   Record generated and temporary conventions here without duplicating
   technology truth.

## Self-Check

- Observed layout is distinguished from intended ownership and placement policy.
- Settled claims come from maintainer-provided Structure intent or an explicit,
  current source of Structure policy.
- Material conflicts and missing Structure intent caused questions or explicit
  unknowns.
- The update stays concise and navigational rather than listing every path.
- Module ownership and placement rules use Project Domain-model language when
  the Domain model exists.
- Generated and temporary conventions do not duplicate technology commands or
  stack detail.
- Intent, technology, design, roadmap, decision, and agent-guidance changes are
  reported as related work rather than edited in this invocation.

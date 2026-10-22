---
name: steer-intent
description: Steer durable Project Intent through the shared Steering workflow. Use this focused adapter for purpose, audiences, outcomes, scope, success signals, assumptions, and unknowns.
---

# Steer Intent

Maintain the Steering artifact configured for `intent`. Delegate the common
process to `steer-project`; this adapter supplies Intent ownership and
validation rather than a second workflow.

## Ownership

Intent owns:

- Project purpose and the change it seeks
- intended audiences, stakeholders, or beneficiaries
- desired outcomes and core journeys
- scope boundaries and non-goals
- success signals and constraints on value
- confirmed assumptions and material unknowns

Intent does not own implementation choices, physical repository layout,
delivery sequence, design semantics, decision history, or agent instructions.
Classify those as related work for their owning adapters.

## Procedure

1. Invoke the shared Steering workflow in `steer-project`.
2. Resolve `intent` through `.steering.json`; do not assume the artifact is
   named `PRODUCT.md`, `INTENT.md`, or any other physical name.
3. Inspect the relevant software, data, and marketing evidence profiles.
4. Ask only questions whose answers materially affect Intent. In particular,
   confirm audience, purpose, scope, or success when evidence is absent or
   conflicting.
5. When the maintainer cannot answer and a safe update remains possible, label
   provisional claims under `Assumptions` and unanswered decisions under
   `Unknowns`. Do not present either as settled intent.
6. Update only the configured Intent Steering artifact, using the existing
   structure or [Intent template](references/intent-template.md).
7. Run the shared validation, consistency check, and related-work report.

## Self-Check

- Every settled claim comes from maintainer-provided intent or an explicit,
  current source of intent.
- Repository evidence is not promoted to desired scope or purpose.
- Material conflicts and missing intent caused questions or explicit unknowns.
- The update contains assumptions, unknowns, and last-reviewed metadata when
  relevant, without adding empty ceremonial sections.
- Technical, design, roadmap, structure, decision, and agent-guidance changes
  are reported as related work rather than edited in this invocation.

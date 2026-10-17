---
name: steer-roadmap
description: Steer durable Project Roadmap sequencing through the shared Steering workflow. Use this focused adapter for priorities, sequencing, dependencies, risks, non-goals, and decision points.
---

# Steer Roadmap

Maintain the Steering artifact configured for `roadmap`. Delegate the common
process to `steer-project`; this adapter supplies Roadmap ownership and
validation rather than a second workflow.

## Ownership

Roadmap owns:

- Now, Next, and Later priorities and their sequencing rationale
- explicit non-goals for the planning horizon
- dependencies and risks that affect delivery sequence
- decision points that gate sequencing changes
- confirmed assumptions and material unknowns about sequence

Roadmap does not own Project purpose or audiences, implementation choices,
physical repository layout, design semantics, decision history, agent
instructions, or Ticket-level execution detail. Classify those as related work
for their owning adapters or the work tracker.

## Procedure

1. Invoke the shared Steering workflow in `steer-project`.
2. Resolve `roadmap` through `.steering.json`; do not assume the artifact is
   named `ROADMAP.md` or any other physical name. Preserve compatible existing
   roadmap conventions through the configured mapping.
3. Inspect relevant software, data, and marketing evidence profiles together
   with current work-tracker state, commits, plans, and other Steering
   artifacts. Treat all of these as evidence and consider freshness; stale
   plans do not override current confirmed intent.
4. Ask only questions whose answers materially affect sequencing. In
   particular, confirm priority order, non-goals, or critical dependencies when
   evidence is absent, stale, or conflicting. Do not infer priority from
   activity alone.
5. When the maintainer cannot answer and a safe update remains possible, label
   provisional claims under `Assumptions` and unanswered decisions under
   `Unknowns`. Do not present either as settled sequencing.
6. Update only the configured Roadmap Steering artifact, using the existing
   structure or [Roadmap template](references/roadmap-template.md). Keep items
   outcome-oriented; leave Ticket execution detail in the work tracker.
7. Route durable trade-offs that lock implementation direction to decision
   steering as related work without copying ADR policy into the Roadmap.
8. Run the shared validation, consistency check, and related-work report.

## Self-Check

- Every settled priority or sequence claim comes from maintainer-provided
  intent or an explicit, current source of sequencing intent.
- Tracker activity, commits, and stale plans are not promoted to Now without
  confirmation.
- Dependencies and risks use canonical Project language.
- Material conflicts and missing sequencing intent caused questions or
  explicit unknowns.
- Ticket-level execution detail was not absorbed into the Roadmap artifact.
- Durable trade-offs were reported for decision steering rather than recorded
  as ADR policy here.
- The update contains assumptions, unknowns, and last-reviewed metadata when
  relevant, without adding empty ceremonial sections.
- Intent, technology, design, structure, decision, and agent-guidance changes
  are reported as related work rather than edited in this invocation.

---
name: deliver-work
description: Default Work lifecycle coordinator from unresolved intent through approved Tickets. Use when shaping intent into a Specification and Tickets, resuming an approved Specification at Ticket decomposition, skipping completed lifecycle stages, recommending Work tracker hierarchy, or coordinating grilling, Domain modeling, Specification synthesis, and Ticket approval.
---

# Deliver Work

Coordinate the Work lifecycle from unresolved intent through approved Tickets.
This is the suite's default Work lifecycle coordinator. Project steering stays
with `steer-project`; this module carries settled intent into planned work.

Read [lifecycle stages](references/lifecycle-stages.md) before choosing a resume
point. Read [hierarchy](references/hierarchy.md) before publishing tracker
structure. Read [tracker publication](references/tracker-publication.md) before
writing Specifications or Tickets.

## Required upstream skills

Invoke these Matt skills **by name** for their behavior. Do not reproduce,
vendor, or summarize their procedures here:

- `grill-with-docs` — sharpen unresolved intent; routes Domain modeling
- `domain-modeling` — settle Domain language when terms crystallise
- `to-spec` — synthesize one Specification and confirm test seams
- `to-tickets` — decompose into vertical-slice Tickets with blockers

If a required skill is unavailable, stop and report the missing name. Do not
invent a reduced local substitute.

## Procedure

1. **Inspect resume state.** Read the configured Work tracker mappings from
   `.steering.json` (`workTracker`). Classify the request:
   - **New / unresolved intent** → begin at `grill-with-docs`.
   - **Approved Specification, Tickets not approved** → resume at `to-tickets`.
   - **Approved Tickets** → skip completed shape stages; report the Frontier and
     stop (execution and retrospective are later Work lifecycle stages).
2. **Grill and model (when required).** For new intent, invoke
   `grill-with-docs` by name. When Domain language settles during shaping,
   invoke `domain-modeling` by name. Hold a **shared understanding** human gate
   before Specification synthesis: the maintainer confirms the sharpened intent
   is ready to become one Specification.
3. **Recommend hierarchy.** Using execution cohesion (not raw size), recommend
   ordinary Specification item, large cohesive project/epic grouping, or
   multi-Specification initiative per [hierarchy](references/hierarchy.md).
   When the recommendation is ambiguous, confirm with the maintainer before
   publishing.
4. **Synthesize the Specification.** Invoke `to-spec` by name. A Specification
   is one coherent outcome with one integration branch and one final acceptance
   decision, retained as one canonical issue-like record in the configured Work
   tracker. Keep the **test seams** human gate from `to-spec` intact.
5. **Decompose into Tickets.** Invoke `to-tickets` by name. Each Ticket is an
   independently verifiable vertical slice sized for one fresh agent context.
6. **Ticket approval gate.** Before treating Tickets as approved, confirm with
   the maintainer: breakdown, **agent-ready** or **human-ready** role per
   Ticket, and blocking relationships. Prefer native tracker parent/child and
   blocker links; use explicit metadata fallback from `.steering.json` when
   native support is absent.
7. **Publish through configured mappings.** Apply status, role, hierarchy,
   blocker, and comment/activity mappings for the configured tracker kind
   (Linear, GitHub, GitLab, Jira, local Markdown, or custom workflow). Outcomes
   are tracker-agnostic; only the mapping shape changes.

## Operating Rules

- Delegate grilling, Domain modeling, Specification synthesis, and Ticket
  decomposition to Matt skills by name only.
- Required human gates remain intact: shared understanding, test seams, and
  Ticket approval.
- Prefer native tracker relationships; fall back to explicit metadata from
  setup configuration when needed.
- Do not hardcode a tracker vendor; always read `.steering.json` workTracker
  mappings.
- Shape stages end at approved Tickets. Leave execution and retrospective as
  later lifecycle stages for a future extension of this coordinator.

## Result

End with:

- resume point chosen and stages skipped, if any
- Matt skills invoked by name
- hierarchy recommendation and whether confirmation was required
- Specification identity (canonical record, integration branch intent)
- approved Tickets with roles and blockers, or the gate still open
- Work tracker kind and mapping path used
- Frontier summary when Tickets are already approved

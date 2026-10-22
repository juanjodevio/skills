---
name: steer-decisions
description: Steer short status-bearing Project decisions through the shared Steering workflow. Use this focused adapter for ADR eligibility, short decision records, the status-bearing index, and supersession.
---

# Steer Decisions

Maintain the Steering artifact configured for `decisions`. Delegate the common
process to `steer-project`; this adapter supplies decision ownership and
validation rather than a second workflow.

Invoke `domain-modeling` for Domain model discipline and Matt's three-part ADR
eligibility. Do not reproduce that skill here.

## Ownership

Decisions owns:

- ADR eligibility using Matt's three-part test
- short decision records with explicit status
- the status-bearing ADR index, updated atomically with its records
- supersession links that preserve accepted history
- optional considered options and consequences only when they preserve the
  trade-off

Decisions does not own Project purpose, technology commands or stack catalogs,
design semantics, delivery sequence, repository layout, or agent guidance.
Classify those as related work for their owning adapters. ADR records and their
index are one logical Steering artifact.

## Eligibility

Record an ADR only when all three are true:

1. **Hard to reverse**: changing course later has meaningful cost
2. **Surprising without context**: a future reader would wonder why this path
   was chosen
3. **Real trade-off**: genuine alternatives existed and one was selected for
   specific reasons

If any condition is missing, intentionally skip the ADR with a concise
rationale. Skipping is success, not an error.

## Procedure

1. Invoke the shared Steering workflow in `steer-project`.
2. Resolve `decisions` through `.steering.json`; do not assume the artifact is
   named `docs/adr` or any other physical path. Preserve compatible existing ADR
   conventions when they retain required semantics (numbered records, explicit
   status, status-bearing index, supersession).
3. Invoke `domain-modeling` when Domain language or eligibility judgement is in
   play. Apply the three-part test before writing.
4. Inspect existing decision records, the status-bearing index, related Steering
   artifacts, and evidence that frames the trade-off. Label repository state as
   evidence, not as settled decision history.
5. Ask only questions whose answers materially affect eligibility, the decision
   outcome, status, or supersession.
6. When eligible, update only the configured decisions Steering artifact: write a
   short ADR with explicit status and update the status-bearing index in the same
   change. Use the existing structure or
   [decision record template](references/decision-record-template.md). Include
   considered options or consequences only when useful to preserve the trade-off.
7. When direction changes, create a superseding record and mark the prior
   accepted ADR superseded. Never rewrite accepted history.
8. Run the shared validation, consistency check, and related-work report.

## Self-Check

- Eligibility required all three conditions; ineligible cases were skipped with
  rationale rather than forced into records.
- New ADRs are short by default and declare explicit status.
- Options and consequences appear only when they preserve a useful trade-off.
- The status-bearing index matches each ADR's status and changed with the record.
- Accepted history was superseded, not rewritten.
- Compatible existing ADR conventions were preserved when semantics remained.
- `domain-modeling` was invoked by name rather than vendored.
- Intent, technology, design, roadmap, structure, and agent-guidance changes are
  reported as related work rather than edited in this invocation.

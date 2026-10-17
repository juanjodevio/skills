---
name: steer-project
description: The default Project steering entrypoint and multi-artifact orchestrator. Use this skill whenever durable Project truth needs to be created, updated, audited, or aligned across Intent, technology, design, roadmap, structure, decisions, or agent guidance.
---

# Steer Project

Coordinate Project steering as the suite orchestrator. This is the default
entrypoint; use a focused adapter directly only when ownership is already clear
and the request cannot span other truth types.

Read [configuration](references/configuration.md) before locating an artifact.
Read [evidence profiles](references/evidence-profiles.md) before inspecting a
Project. Read [orchestration](references/orchestration.md) when more than one
truth type is in play. Load only the profiles supported by available evidence;
profiles compose for mixed Projects without flattening domain meaning.

## Steering Workflow

Use this workflow for every Steering request:

1. **Inspect evidence.** Read configured Steering artifacts, relevant repository
   evidence, accepted decisions, and current work-tracker context. Label
   observations as evidence; code, files, metrics, and prior copy can show
   current state but cannot establish desired intent on their own. Compose
   software, data, and marketing profiles independently and keep provenance
   visible when they disagree.
2. **Classify ownership.** Name every durable truth type the request touches.
   Classify by meaning, not filenames. Select the focused adapter for each
   owner: Intent → `steer-intent`; design → `steer-design`; technology →
   `steer-technology`; structure → `steer-structure`; roadmap →
   `steer-roadmap`; decisions → `steer-decisions`; agent guidance →
   `steer-agent-guidance`. Focused modules remain the sole owners of those
   truth types. The orchestrator routes; it does not absorb their templates,
   checks, or ADR policy.
3. **Resolve material unknowns.** Ask concise questions when an answer could
   materially change an artifact. Prefer bounded questions for bounded choices.
   If the maintainer is unavailable and a safe update remains possible, record
   the uncertainty under `Assumptions` or `Unknowns`; never convert evidence
   into intent. When Domain language settles, invoke `domain-modeling` by name;
   do not vendor it.
4. **Update through owners.** For a single-owner request, resolve the mapping
   and let that adapter update only its Steering artifact. For a multi-artifact
   request, invoke owning adapters in dependency order: Intent before dependent
   direction; technology and design before affected roadmap or structure work;
   eligible decisions after their trade-off settles; agent guidance last.
   Unrelated artifacts may proceed independently. Preserve useful local
   structure and established terminology.
5. **Validate each artifact.** Check that claims are grounded in confirmed
   intent or clearly marked uncertainty, required metadata is present when
   relevant, local links resolve, and each focused adapter's self-check passes.
6. **Check consistency.** Compare updates with other Steering artifacts,
   accepted decisions, evidence, and active work. Cross-artifact conflicts are
   reported and never resolved silently; do not quietly edit a second artifact
   to erase a conflict.
7. **Report related work.** Summarize artifacts changed, questions answered,
   assumptions or unknowns recorded, conflicts found, and concrete follow-up
   work. Related work returns through the orchestrator; focused adapters must
   not side-call each other in ways that bypass ordering or conflict reporting.
   Use the configured work-tracker adapter when follow-up must be recorded;
   otherwise report proposed work without claiming it was created.

## Operating Rules

- Broad requests are orchestrated across owners; single-owner requests still
  update at most one Steering artifact per focused adapter invocation.
- Ask before writing when missing intent is material and no safe, explicitly
  uncertain update is possible.
- Contradictory evidence is a question or reported conflict, not a license to
  choose the most convenient interpretation.
- Add `Assumptions`, `Unknowns`, and `Last Reviewed` only when useful to the
  artifact and preserve equivalent established headings.
- Do not duplicate focused templates, adapter self-checks, or ADR eligibility
  inside this orchestrator.

## Result

End with:

- owners and configured artifact paths touched
- evidence inspected and evidence profiles used
- dependency order followed (or independent parallelism used)
- questions asked or uncertainty recorded
- validation and consistency results, including reported conflicts
- related work reported or created through the orchestrator

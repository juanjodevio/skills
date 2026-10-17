---
name: steer-project
description: The default Project steering entrypoint. Use this skill whenever durable Project intent needs to be created, updated, audited, or aligned with repository evidence.
---

# Steer Project

Coordinate Project steering through focused truth adapters. This is the default
entrypoint; use a focused adapter directly only when ownership is already clear.

Read [configuration](references/configuration.md) before locating an artifact.
Read [evidence profiles](references/evidence-profiles.md) before inspecting a
Project. Load only the profiles supported by available evidence; profiles
compose for mixed Projects.

## Steering Workflow

Use this workflow for every Steering request:

1. **Inspect evidence.** Read the configured Steering artifact, relevant
   repository evidence, accepted decisions, and current work-tracker context.
   Label observations as evidence; code, files, metrics, and prior copy can show
   current state but cannot establish desired intent on their own.
2. **Classify ownership.** Name the single truth type that owns the request and
   select its focused adapter. For an Intent request, use `steer-intent`. For a
   technology request, use `steer-technology`. For a Structure request, use
   `steer-structure`. For a Roadmap sequencing request, use `steer-roadmap`.
   For a decisions request, use `steer-decisions`. For an agent-guidance
   request, use `steer-agent-guidance`. If the request spans truth types,
   choose the primary owner and report the remainder as related work.
3. **Resolve material unknowns.** Ask concise questions when an answer could
   materially change the artifact. Prefer bounded questions for bounded choices.
   If the maintainer is unavailable and a safe update remains possible, record
   the uncertainty under `Assumptions` or `Unknowns`; never convert evidence
   into intent.
4. **Update one artifact.** Resolve the owner through the Project's artifact
   mapping and update only that Steering artifact. Preserve useful local
   structure and established terminology.
5. **Validate the artifact.** Check that claims are grounded in confirmed intent
   or clearly marked uncertainty, required metadata is present when relevant,
   local links resolve, and the focused adapter's self-check passes.
6. **Check consistency.** Compare the update with other Steering artifacts,
   accepted decisions, evidence, and active work. Do not silently edit a second
   artifact to remove a conflict.
7. **Report related work.** Summarize the artifact changed, questions answered,
   assumptions or unknowns recorded, conflicts found, and concrete follow-up
   work for other owners or the work tracker.

## Operating Rules

- One invocation updates at most one Steering artifact.
- Ask before writing when missing intent is material and no safe, explicitly
  uncertain update is possible.
- Contradictory evidence is a question or reported conflict, not a license to
  choose the most convenient interpretation.
- Add `Assumptions`, `Unknowns`, and `Last Reviewed` only when useful to the
  artifact and preserve equivalent established headings.
- Use the configured work-tracker adapter when related work must be recorded;
  otherwise report the proposed work without claiming it was created.

## Result

End with:

- owner and configured artifact path
- evidence inspected and evidence profiles used
- questions asked or uncertainty recorded
- validation and consistency results
- related work reported or created

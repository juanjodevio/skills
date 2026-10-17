---
name: setup-project-steering
description: Configure a Project for the steering suite. Use when setting up Project steering, detecting Matt setup prerequisites, confirming artifact mappings and evidence adapters, or bootstrapping active Steering artifacts for the first time.
---

# Setup Project Steering

Configure Project steering as the single setup entrypoint. Extend compatible Matt
setup; do not reimplement tracker, triage, Domain model, or ADR scaffolding.

Read [configuration schema](references/configuration-schema.md) before writing
`.steering.json`. Read [tracker configuration](references/tracker-configuration.md)
when recording Work tracker mappings.

## Required upstream skills

Before changing the Project, verify these skills are available **by name** and
usable for their stated behavior:

- `setup-matt-pocock-skills` — tracker, triage, Domain docs, and ADR prerequisites
- `grill-with-docs` — missing material bootstrap intent
- `steer-project` — bootstrap of confirmed active Steering artifacts

Also verify the focused adapters this suite installs (`steer-intent`,
`steer-design`, `steer-technology`, `steer-structure`, `steer-roadmap`,
`steer-decisions`, `steer-agent-guidance`) are reachable when their truth kinds
are active.

If any required skill or capability is missing, setup **fails clearly** and
stops. Do not invent reduced fallbacks, empty-artifact shortcuts, or local
copies of Matt skills.

## Procedure

1. **Check dependencies.** Confirm the required upstream skills above. On
   failure, report the missing name and what it must provide; write nothing.
2. **Detect Matt setup.** Inspect `docs/agents/issue-tracker.md`,
   `docs/agents/domain.md`, triage label docs when triage is installed, and the
   `## Agent skills` block in `AGENTS.md` or `CLAUDE.md`. When that output is
   already complete and compatible, leave it unchanged. When tracker or domain
   prerequisites are missing, invoke `setup-matt-pocock-skills` by name, then
   continue; never reimplement those steps here.
3. **Inspect existing Steering conventions.** Read `.steering.json` when
   present. Inventory candidate Steering artifacts and compatible locations
   (Intent, technology, design, roadmap, structure, decisions/ADRs, agent
   guidance). Label repository contents as evidence; do not promote evidence to
   intent.
4. **Propose, then confirm.** Ask the maintainer to confirm:
   - active truth kinds
   - artifact path mappings (preserve compatible existing paths; defaults only
     when no owner exists)
   - evidence adapters — software, data, and marketing may activate together
   - intentionally inactive artifacts
   - Work tracker kind and mappings for status, role, hierarchy, blocker, and
     comment/activity (Linear, GitHub, GitLab, Jira, local Markdown, or a
     documented custom workflow)
5. **Record configuration.** Write confirmed choices to `.steering.json` using
   the configuration schema. Do not create empty files for inactive kinds.
6. **Resolve missing material intent.** When bootstrap needs purpose, audience,
   success, design direction, or other material decisions the maintainer has not
   supplied, invoke `grill-with-docs` by name. Do not create empty Steering
   artifacts as a substitute for decisions.
7. **Bootstrap through the orchestrator.** For each confirmed active artifact,
   invoke `steer-project` so ownership, ordering, validation, and related work
   follow the shared Steering workflow. Do not bypass focused adapters.
   When confirmed `evidenceAdapters` includes `software` and/or `data`,
   `steer-agent-guidance` materializes Implementation discipline
   (`docs/agents/implementation-discipline.md`) and its agent-guidance pointer
   during that bootstrap. Marketing-only Projects skip both (ADR-0002).

## Operating Rules

- Full-suite installation is assumed; focused standalone install is unsupported.
- Compatible Matt and Steering paths stay owned by their existing files.
- Mixed Projects may enable software, data, and marketing evidence adapters
  together without flattening domain meaning.
- Bootstrap only the confirmed active set.
- Implementation discipline follows evidence adapters via `steer-agent-guidance`;
  setup does not copy that file itself.
- Reuse Matt skills by name only.

## Result

End with:

- dependency check outcome
- whether Matt setup was preserved or delegated to `setup-matt-pocock-skills`
- confirmed active and inactive truth kinds, mappings, and evidence adapters
- Work tracker kind and recorded mappings
- whether `grill-with-docs` ran for missing material intent
- which active artifacts were bootstrapped through `steer-project`

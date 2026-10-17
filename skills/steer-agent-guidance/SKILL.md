---
name: steer-agent-guidance
description: Steer compact agent guidance through the shared Steering workflow. Use this focused adapter for agent orientation, navigation pointers, safety boundaries, and first-read maps without duplicating durable Project truth.
---

# Steer Agent Guidance

Maintain the Steering artifact configured for `agent-guidance`. Delegate the
common process to `steer-project`; this adapter supplies guidance ownership and
validation rather than a second workflow.

Invoke `writing-for-agents` for writing discipline. Do not reproduce that skill
here; keep guidance compact and pointer-based.

## Ownership

Agent guidance owns:

- short Project orientation for agents
- first-read pointers to configured Steering artifacts
- navigation to configuration (`.steering.json`) without copying its contents
- workflow expectations that affect agent behavior
- safety and approval boundaries
- durable-truth maintenance instructions that point agents back to owning
  artifacts
- Implementation discipline materialization and pointer when evidence adapters
  require it (see below)

Agent guidance does not own Project Intent, technology commands or stack truth,
design semantics, delivery sequence, repository layout rules, architecture
decisions, or coding standards. Classify those as related work for their owning
adapters. Point at canonical owners; do not copy their content.

Update guidance only when agent behavior or navigation materially changes.

## Implementation discipline

Seed: [implementation-discipline.md](references/implementation-discipline.md).
Project path: `docs/agents/implementation-discipline.md`. See ADR-0002.

When `.steering.json` `evidenceAdapters` includes `software` and/or `data`:

1. If `docs/agents/implementation-discipline.md` is missing, create it from the
   seed (do not overwrite an existing Project copy).
2. Ensure the configured agent-guidance artifact points to that path for
   pre-`implement-spec` reads.

When adapters are marketing-only (neither `software` nor `data`):

1. Remove the Implementation discipline pointer from configured agent-guidance.
2. Leave `docs/agents/implementation-discipline.md` on disk if present.

Update only the configured `agent-guidance` path. Do not sync sibling root
files (`AGENTS.md` / `CLAUDE.md` duplicates).

## Procedure

1. Invoke the shared Steering workflow in `steer-project`.
2. Resolve `agent-guidance` through `.steering.json`; do not assume the artifact
   is named `AGENTS.md`, `CLAUDE.md`, or any other physical name. Preserve
   compatible existing root guidance through the configured mapping.
3. Invoke `writing-for-agents` before drafting or editing guidance prose.
4. Inspect current guidance, configured Steering artifact paths, evidence
   adapters, and evidence that affects navigation or agent behavior. Treat
   repository files as evidence of current orientation, not as Intent.
5. Ask only questions whose answers materially affect agent navigation,
   boundaries, or first reads—especially when pointers conflict or Intent that
   the summary depends on is missing.
6. Apply Implementation discipline materialization and pointer rules above.
7. Update only the configured agent-guidance Steering artifact, using the
   existing structure or [agent guidance template](references/agent-guidance-template.md).
8. Run the shared validation, consistency check, and related-work report.

## Self-Check

- Guidance identifies canonical Steering artifacts and configuration by pointer,
  without copying their content.
- Commands, architecture decisions, and Project Intent remain owned elsewhere
  and appear here only as pointers or related-work reports.
- Compatible root guidance conventions are preserved via the configured mapping.
- Implementation discipline file and pointer match `evidenceAdapters` (present
  for software/data; pointer absent for marketing-only).
- `writing-for-agents` was invoked for writing discipline rather than inlined.
- Material pointer conflicts and missing Intent caused questions or explicit
  unknowns.
- The update happened only because agent behavior or navigation changed
  materially.
- Intent, technology, design, roadmap, structure, and decision changes are
  reported as related work rather than edited in this invocation.

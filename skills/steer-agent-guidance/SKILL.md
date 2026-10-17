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

Agent guidance does not own product Intent, technology commands or stack truth,
design semantics, delivery sequence, repository layout rules, or architecture
decisions. Classify those as related work for their owning adapters. Point at
canonical owners; do not copy their content.

Update guidance only when agent behavior or navigation materially changes.

## Procedure

1. Invoke the shared Steering workflow in `steer-project`.
2. Resolve `agent-guidance` through `.steering.json`; do not assume the artifact
   is named `AGENTS.md`, `CLAUDE.md`, or any other physical name. Preserve
   compatible existing root guidance through the configured mapping.
3. Invoke `writing-for-agents` before drafting or editing guidance prose.
4. Inspect current guidance, configured Steering artifact paths, and evidence
   that affects navigation or agent behavior. Treat repository files as
   evidence of current orientation, not as Intent.
5. Ask only questions whose answers materially affect agent navigation,
   boundaries, or first reads—especially when pointers conflict or Intent that
   the summary depends on is missing.
6. Update only the configured agent-guidance Steering artifact, using the
   existing structure or [agent guidance template](references/agent-guidance-template.md).
7. Run the shared validation, consistency check, and related-work report.

## Self-Check

- Guidance identifies canonical Steering artifacts and configuration by pointer,
  without copying their content.
- Commands, architecture decisions, and product Intent remain owned elsewhere
  and appear here only as pointers or related-work reports.
- Compatible root guidance conventions are preserved via the configured mapping.
- `writing-for-agents` was invoked for writing discipline rather than inlined.
- Material pointer conflicts and missing Intent caused questions or explicit
  unknowns.
- The update happened only because agent behavior or navigation changed
  materially.
- Intent, technology, design, roadmap, structure, and decision changes are
  reported as related work rather than edited in this invocation.

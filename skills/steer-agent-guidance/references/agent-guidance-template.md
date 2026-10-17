# Agent Guidance Template

Use the Project's established structure when it is clear. For a new or sparse
agent-guidance Steering artifact, adapt this shape. Invoke `writing-for-agents`
for prose discipline; keep every durable claim as a pointer to its owning
Steering artifact or configuration.

```markdown
# Agent Guidance

## Project Summary

One or two sentences of orientation. Do not restate Intent.

## First Reads

- Intent: <configured intent path>
- Technology: <configured technology path>
- Design: <configured design path>
- Roadmap: <configured roadmap path>
- Structure: <configured structure path>
- Decisions: <configured decisions path or ADR index>
- Configuration: `.steering.json`

Omit inactive truth kinds. Resolve paths from `.steering.json`; never invent
basenames.

## Commands

Point to the configured technology artifact for install, lint, test, and build.
Include a short local reminder only when navigation requires it.

## Agent Workflow

- Read the owning Steering artifact before changing durable truth.
- Update the owning artifact when durable truth changes; keep this file as
  pointers.

## Safety And Approval Boundaries

- Ask before changing Intent, roadmap priority, public contracts, security
  posture, or accepted decision direction.

## Durable Truth Maintenance

This file orients agents. Durable truth lives in configured Steering artifacts.
```

Omit empty optional sections. Prefer fewer, sharper pointers over duplicated
detail.

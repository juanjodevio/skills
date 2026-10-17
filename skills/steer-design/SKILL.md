---
name: steer-design
description: Steer durable design direction through the shared Steering workflow. Use this focused adapter for atmosphere, principles, visual system, interaction, content, responsive behavior, accessibility, assumptions, and unknowns.
---

# Steer Design

Maintain the Steering artifact configured for `design`. Delegate the common
process to `steer-project`; this adapter supplies Design ownership and
validation rather than a second workflow.

The semantic Design pattern is inspired by Google's `design-md` format. Do not
install, invoke, or require Stitch, and do not copy Stitch-specific retrieval
or generation behavior.

## Ownership

Design owns:

- atmosphere and brand personality for the experience
- visual and interaction principles
- colors, typography, layout, and spacing
- shapes and surfaces
- interface styling and interaction patterns
- content style that affects presentation
- responsive behavior
- accessibility expectations
- confirmed assumptions and material unknowns

Design does not own product purpose or scope, technology stack or commands,
delivery sequence, repository layout, decision history, or agent instructions.
Classify those as related work for their owning adapters.

## Procedure

1. Invoke the shared Steering workflow in `steer-project`.
2. Resolve `design` through `.steering.json`; do not assume the artifact is
   named `DESIGN.md`, `docs/DESIGN.md`, or any other physical name. Preserve
   compatible existing locations through the configured mapping.
3. Inspect available user, repository, visual, and brand evidence across the
   relevant software, data, and marketing profiles. Treat UI code, screenshots,
   assets, brand guidance, and current design artifacts as evidence only.
4. Ask only questions whose answers materially affect Design. When material
   design intent cannot be established from maintainer-provided intent or an
   explicit current source, invoke `grill-with-docs` before writing settled
   claims.
5. When the maintainer cannot answer and a safe update remains possible, label
   provisional claims under `Assumptions` and unanswered decisions under
   `Unknowns`. Do not present either as settled design intent.
6. Update only the configured Design Steering artifact, using the existing
   structure or [Design template](references/design-template.md).
7. Run the shared validation, consistency check, and related-work report.

## Self-Check

- Every settled claim comes from maintainer-provided design intent or an
  explicit, current source of design intent.
- Visual implementation, screenshots, and assets are not promoted to desired
  design direction on their own.
- Material conflicts and missing design intent caused questions,
  `grill-with-docs`, or explicit unknowns.
- The pattern covers atmosphere, principles, colors, typography, layout,
  spacing, shapes, surfaces, interface styling, interaction, content,
  responsive behavior, accessibility, assumptions, and unknowns when relevant,
  without empty ceremonial sections.
- Stitch is not installed, invoked, or required.
- Intent, technology, roadmap, structure, decision, and agent-guidance changes
  are reported as related work rather than edited in this invocation.

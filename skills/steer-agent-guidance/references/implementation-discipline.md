# Implementation Discipline

Adapted from
[andrej-karpathy-skills CLAUDE.md](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md).

Rules for software and data **implementation** — Ticket execution through
`implement-spec`. They do not bind Project steering, grilling, or shaping.

**Tradeoff:** caution over speed. For trivial Tickets, use judgment.

## 1. Think Before Coding

State assumptions. If uncertain, ask. When interpretations differ, present
them; do not pick silently. Name a simpler approach when it solves the Ticket.
If something is unclear, stop, name the fog, and ask.

## 2. Simplicity First

Ship the minimum change that satisfies the Ticket. No speculative features, no
single-use abstractions, no unrequested flexibility. If the diff is far larger
than the problem, shrink it.

## 3. Surgical Changes

Touch only what the Ticket requires. Match existing style. Leave adjacent code
alone. Remove only unused symbols **this** change introduced. Every changed
line should trace to the Ticket.

## 4. Goal-Driven Execution

Turn the Ticket into checkable success criteria. Loop until those checks pass.
Prefer “failing check first, then green” over vague “make it work.” For
multi-step Tickets, list brief steps each with a verify check.

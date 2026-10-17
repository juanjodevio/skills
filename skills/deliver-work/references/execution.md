# Ticket Execution

Rules for the execute and retrospective half of `deliver-work`. Delegate
behavior to Matt skills by name; this file only states coordinator obligations.

## Capability gate

`implement-spec` requires a Git Project (integration branch and worktrees). If
the Project root is not a Git repository, stop before implementation with a
clear **capability blocker**. Preserve the approved Specification and Tickets;
do not reopen shape gates. Outcome is **blocked**.

## Implementation discipline

When `.steering.json` `evidenceAdapters` includes `software` and/or `data`,
read `docs/agents/implementation-discipline.md` **before** invoking
`implement-spec`. If that file is missing, stop and report that
`steer-agent-guidance` must materialize it from its seed (ADR-0002). Skip this
read when adapters are marketing-only.

## Frontier

The **Frontier** is every unfinished **agent-ready** Ticket whose blocking
Tickets are complete and which can therefore execute now.

- Refresh Ticket state and blocker details from the configured Work tracker
  before computing the Frontier and whenever execution progresses or resumes.
- Independent agent Tickets may proceed while unrelated **human-ready** Tickets
  remain blocked.
- When the Frontier is empty and only human-blocked work remains, stop cleanly
  with outcome **blocked**. Do not poll indefinitely for human progress.

## Delegation

Invoke `implement-spec` **by name** for ticket-graph execution. Do not build a
local subagent runner or vendor execution mechanics into this coordinator. If
`implement-spec` is unavailable, stop and report the missing skill name.

## Tracker updates before downstream reliance

After a Ticket is reviewed complete, update its state in the Work tracker
**before** any downstream Ticket relies on that completion. Recompute the
Frontier only from refreshed tracker state.

## Outcomes

| Outcome | Meaning |
| --- | --- |
| Specification complete | Shape finished; Tickets approved; this run did not execute |
| agent work complete | All agent Tickets finished; no remaining agent Frontier |
| blocked | Stopped on human blockers or a capability blocker (for example non-Git) |
| partially complete | Some agent Tickets finished; a non-empty agent Frontier remains |

## Execution summary

After each execution run, post **one** concise comment/activity on the
canonical Specification record via configured `commentActivity` mappings:

- completed Tickets (identifiers only)
- current blockers
- next Frontier
- branch/review reference

Do not duplicate Ticket bodies into the summary.

## Retrospective

Invoke `retro` **once** for each execution outcome that is final (**agent work
complete**), **blocked**, or **partially complete**. Scope findings to work
actually performed in that run. For pure capability stops that never reached
`implement-spec`, still invoke `retro` once for the blocked outcome without
inventing implementation findings.

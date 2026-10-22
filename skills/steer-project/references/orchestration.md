# Multi-Artifact Orchestration

Use this reference when a request spans more than one Steering truth type.
Focused adapters remain sole owners of their artifacts; this file only orders
and reports their work.

## Classify By Durable Truth

Name each requested truth type from meaning, not from spoken or familiar
filenames. Map owners through `.steering.json`. Ignore unmapped basenames as
ownership signals.

| Truth type | Focused adapter |
| --- | --- |
| Intent | `steer-intent` |
| technology | `steer-technology` |
| design | `steer-design` |
| roadmap | `steer-roadmap` |
| structure | `steer-structure` |
| decisions | `steer-decisions` |
| agent guidance | `steer-agent-guidance` |

Do not absorb focused templates, self-checks, or ADR eligibility into the
orchestrator. Route those concerns to the owning adapter.

## Dependency Order

When updates depend on each other, run owning adapters in this order:

1. Intent before dependent direction
2. technology and design before affected roadmap or structure work
3. eligible decisions after their trade-off settles
4. agent guidance last

Unrelated Steering artifacts may proceed independently; do not force them into
the run. Parallelize only when neither update depends on the other's settled
truth.

## Domain Modeling

When Domain language settles during orchestration, invoke `domain-modeling` by
name. Do not vendor or restate that skill here.

## Consistency And Related Work

After each owning update, compare against other Steering artifacts, accepted
decisions, evidence, and active work. Cross-artifact conflicts are reported and
never resolved silently; do not quietly edit a second artifact to erase a
conflict.

Related work discovered while an adapter runs returns through the orchestrator.
Focused adapters must not side-call each other in ways that bypass ordering or
conflict reporting.

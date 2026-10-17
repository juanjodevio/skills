# Project Steering Configuration Schema

Write Project steering configuration to `.steering.json` at the Project root
after the maintainer confirms choices. Relative artifact paths resolve from the
Project root.

```json
{
  "artifacts": {
    "intent": "docs/INTENT.md",
    "design": "docs/DESIGN.md",
    "technology": "docs/TECH.md",
    "structure": "docs/STRUCTURE.md",
    "roadmap": "docs/ROADMAP.md",
    "decisions": "docs/adr",
    "agent-guidance": "AGENTS.md"
  },
  "activeArtifacts": ["intent", "technology", "roadmap", "decisions"],
  "inactiveArtifacts": ["design", "structure", "agent-guidance"],
  "evidenceAdapters": ["software", "data"],
  "workTracker": {
    "kind": "linear",
    "status": {},
    "role": {},
    "hierarchy": {},
    "blocker": {},
    "commentActivity": {}
  }
}
```

## Rules

- Truth kinds are logical owners. Preserve compatible existing paths; propose
  defaults only when no owner exists.
- `activeArtifacts` are the only kinds bootstrap may create or refresh.
- `inactiveArtifacts` are intentional omissions: record them; do not create
  empty files for them.
- `evidenceAdapters` may include any combination of `software`, `data`, and
  `marketing`.
- `workTracker.kind` is one of `linear`, `github`, `gitlab`, `jira`,
  `local-markdown`, or `custom`, with the five mapping fields documented in
  [tracker configuration](tracker-configuration.md).
- Malformed configuration, duplicate ownership, paths outside the Project, and
  mappings to impossible targets are blocking errors. Report them without
  writing Steering artifacts.

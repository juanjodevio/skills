# Steering Configuration

Steering truth types are logical owners, not filenames. Locate their artifacts
from the Project's `.steering.json` file:

```json
{
  "artifacts": {
    "intent": "docs/INTENT.md",
    "agent-guidance": "AGENTS.md"
  }
}
```

Resolve relative paths from the Project root. A configured path may use any
filename or directory. Never infer ownership from a familiar basename.

When `.steering.json` or the requested mapping is absent, propose
`docs/INTENT.md` as the Intent default and `AGENTS.md` as the agent-guidance
default, then ask before creating either if another location is plausible.
Preserve compatible existing root guidance (for example `AGENTS.md` or
`CLAUDE.md`) by recording the chosen path in the mapping rather than inventing a
second orientation file. Existing Projects may instead confirm that default in
conversation. Do not create configuration merely to document an assumption.

Treat malformed configuration, duplicate ownership, paths outside the Project,
and mappings to non-file targets as blocking configuration errors. Report them
without editing an artifact.

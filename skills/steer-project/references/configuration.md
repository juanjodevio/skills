# Steering Configuration

Steering truth types are logical owners, not filenames. Locate their artifacts
from the Project's `.steering.json` file:

```json
{
  "artifacts": {
    "intent": "docs/INTENT.md",
    "technology": "docs/TECH.md",
    "structure": "docs/STRUCTURE.md",
    "roadmap": "docs/ROADMAP.md"
  }
}
```

Resolve relative paths from the Project root. A configured path may use any
filename or directory. Never infer ownership from a familiar basename.

When `.steering.json` or the requested mapping is absent, propose
`docs/INTENT.md` as the Intent default, `docs/TECH.md` as the Technology
default, `docs/STRUCTURE.md` as the Structure default, and `docs/ROADMAP.md` as
the Roadmap default, and ask before creating any of them if another location is
plausible. Existing Projects may instead confirm those defaults in conversation.
Do not create configuration merely to document an assumption.

Treat malformed configuration, duplicate ownership, paths outside the Project,
and mappings to non-file targets as blocking configuration errors. Report them
without editing an artifact.

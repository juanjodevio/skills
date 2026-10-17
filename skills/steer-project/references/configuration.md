# Steering Configuration

Steering truth types are logical owners, not filenames. Locate their artifacts
from the Project's `.steering.json` file:

```json
{
  "artifacts": {
    "intent": "docs/INTENT.md",
    "design": "docs/DESIGN.md"
  }
}
```

Resolve relative paths from the Project root. A configured path may use any
filename or directory. Never infer ownership from a familiar basename.
Compatible existing Design locations are preserved by mapping `design` to the
path the Project already uses.

When `.steering.json` or the requested mapping is absent, propose
`docs/INTENT.md` as the Intent default or `docs/DESIGN.md` as the Design
default, and ask before creating it if another location is plausible. Existing
Projects may instead confirm that default in conversation. Do not create
configuration merely to document an assumption.

Treat malformed configuration, duplicate ownership, paths outside the Project,
and mappings to non-file targets as blocking configuration errors. Report them
without editing an artifact.

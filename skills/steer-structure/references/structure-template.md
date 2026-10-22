# Structure Template

Use the Project's established structure when it is clear. For a new or sparse
Structure Steering artifact, adapt this shape:

```markdown
# Repository Structure

## Overview

## Major Areas

- `path/`: purpose, ownership, and relationships to other areas

## Ownership Boundaries

- Area: responsibility and what should not leak across the boundary

## Placement Rules

- New work:
- Tests:
- Docs:
- Assets:
- Scripts:
- Generated and temporary content:

## Naming Conventions

- Convention with the placement or ownership rule it supports

## Assumptions

## Unknowns

## Last Reviewed
YYYY-MM-DD by <reviewer or source>
```

Keep the Directory or Major Areas map navigational: short purpose and ownership
notes for paths that affect where agents and humans place work. Omit empty
optional sections. Do not turn Structure into a full file inventory, and do not
copy technology commands or stack detail from the technology Steering artifact.

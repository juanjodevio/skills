# Maintainer harness

Not part of the installable skills pack. `npx skills add` only installs
`skills/`.

| Path | Purpose |
| --- | --- |
| `steering-suite.json` | Slim suite contract: modules, entrypoints, evidence profiles |

Inventory checks live in root `scripts/` (Matt-style packaging scripts):

```sh
./scripts/list-skills.sh
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
```

Skill *behavior* is not scenario-tested here; quality is editorial plus use in
real Projects, matching Matt’s skills pack approach.

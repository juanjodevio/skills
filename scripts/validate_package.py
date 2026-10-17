#!/usr/bin/env python3
"""Inventory validation for the Project steering suite (Matt-style packaging)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUITE_PATH = ROOT / "dev" / "steering-suite.json"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

APPROVED = {
    "setup-project-steering",
    "steer-project",
    "steer-intent",
    "steer-design",
    "steer-structure",
    "steer-technology",
    "steer-roadmap",
    "steer-agent-guidance",
    "steer-decisions",
    "deliver-work",
}
OBSOLETE = {
    "product-steering",
    "steer-product",
    "steer-tech",
    "steer-adr",
    "steer-agents",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_suite() -> dict:
    if not SUITE_PATH.is_file():
        fail("dev/steering-suite.json is missing")
    try:
        return json.loads(SUITE_PATH.read_text())
    except json.JSONDecodeError as exc:
        fail(f"dev/steering-suite.json is invalid JSON: {exc}")


def parse_frontmatter(skill_dir: Path) -> dict[str, str]:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        fail(f"{skill_dir.relative_to(ROOT)}/SKILL.md is missing")
    match = FRONTMATTER_RE.match(skill_md.read_text())
    if not match:
        fail(f"{skill_md.relative_to(ROOT)} is missing YAML frontmatter")
    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ": " not in line:
            continue
        key, value = line.split(": ", 1)
        metadata[key.strip()] = value.strip()
    if "name" not in metadata or "description" not in metadata:
        fail(f"{skill_md.relative_to(ROOT)} needs name and description")
    if metadata["name"] != skill_dir.name:
        fail(
            f"{skill_md.relative_to(ROOT)} name {metadata['name']!r} "
            f"does not match directory {skill_dir.name!r}"
        )
    return metadata


def validate_modules(suite: dict) -> None:
    if "scenarios" in suite:
        fail("dev/steering-suite.json must not list scenarios")

    modules = suite.get("modules")
    if not isinstance(modules, list) or not modules:
        fail("dev/steering-suite.json modules must be a non-empty list")

    names = [module.get("name") for module in modules]
    if len(names) != len(set(names)):
        fail("dev/steering-suite.json modules contain duplicate names")

    if suite.get("defaultEntrypoint") != "steer-project":
        fail("defaultEntrypoint must be steer-project")
    if suite.get("defaultWorkLifecycle") != "deliver-work":
        fail("defaultWorkLifecycle must be deliver-work")

    name_set = set(names)
    if name_set != APPROVED:
        fail(f"modules inventory must be exactly {sorted(APPROVED)}; got {sorted(name_set)}")

    skill_dirs = {
        path.name
        for path in (ROOT / "skills").iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    if skill_dirs != APPROVED:
        fail(
            "skills/ inventory must match approved suite exactly; "
            f"got {sorted(skill_dirs)}"
        )

    if name_set & OBSOLETE:
        fail(f"obsolete modules must be absent: {sorted(name_set & OBSOLETE)}")
    for obsolete_name in OBSOLETE:
        if (ROOT / "skills" / obsolete_name).exists():
            fail(f"obsolete skill directory still present: {obsolete_name}")

    by_name = {module.get("name"): module for module in modules}
    setup = by_name.get("setup-project-steering", {})
    if setup.get("role") != "setup":
        fail("setup-project-steering role must be setup")
    if "steer-project" not in setup.get("dependencies", []):
        fail("setup-project-steering must depend on steer-project")

    deliver = by_name.get("deliver-work", {})
    if deliver.get("role") != "work-lifecycle":
        fail("deliver-work role must be work-lifecycle")

    entrypoint = by_name.get("steer-project", {})
    if entrypoint.get("role") != "entrypoint":
        fail("steer-project role must be entrypoint")

    for adapter_name, expected_role in (
        ("steer-intent", "intent-adapter"),
        ("steer-design", "design-adapter"),
        ("steer-structure", "structure-adapter"),
        ("steer-technology", "technology-adapter"),
        ("steer-roadmap", "roadmap-adapter"),
        ("steer-decisions", "decisions-adapter"),
        ("steer-agent-guidance", "agent-guidance-adapter"),
    ):
        adapter = by_name.get(adapter_name, {})
        if adapter.get("role") != expected_role:
            fail(f"{adapter_name} role must be {expected_role}")
        if "steer-project" not in adapter.get("dependencies", []):
            fail(f"{adapter_name} must depend on steer-project")

    for module in modules:
        name = module.get("name")
        if not isinstance(name, str):
            fail("each module needs a string name")
        if module.get("role") == "legacy":
            fail(f"legacy role is not allowed for {name}")
        skill_dir = ROOT / "skills" / name
        parse_frontmatter(skill_dir)
        for relative in module.get("references", []):
            path = ROOT / relative
            if not path.is_file():
                fail(f"missing reference {relative}")
        for dependency in module.get("dependencies", []):
            if dependency not in names:
                fail(f"module {name} depends on unknown module {dependency}")


def validate_workflow(suite: dict) -> None:
    expected = [
        "inspect-evidence",
        "classify-ownership",
        "resolve-material-unknowns",
        "update-one-artifact",
        "validate-artifact",
        "check-consistency",
        "report-related-work",
    ]
    if suite.get("workflowStages") != expected:
        fail("workflowStages must match the shared Steering workflow")
    if suite.get("evidenceProfiles") != ["software", "data", "marketing"]:
        fail("evidenceProfiles must be software, data, and marketing")


def validate_core_skill_contracts() -> None:
    setup_text = (ROOT / "skills" / "setup-project-steering" / "SKILL.md").read_text()
    for token in (
        "setup-matt-pocock-skills",
        "grill-with-docs",
        "steer-project",
        "fails clearly",
    ):
        if token not in setup_text:
            fail(f"setup-project-steering/SKILL.md missing {token!r}")

    deliver_text = (ROOT / "skills" / "deliver-work" / "SKILL.md").read_text()
    for token in (
        "grill-with-docs",
        "domain-modeling",
        "to-spec",
        "to-tickets",
        "implement-spec",
        "retro",
        "shared understanding",
        "Ticket approval",
        ".steering.json",
        "Frontier",
        "agent work complete",
        "partially complete",
    ):
        if token not in deliver_text:
            fail(f"deliver-work/SKILL.md missing {token!r}")
    if "Superpowers" in deliver_text:
        fail("deliver-work must not reference Superpowers")
    if "subagent execution engine" in deliver_text.lower():
        fail("deliver-work must not introduce a local subagent execution engine")

    lifecycle = ROOT / "skills" / "deliver-work" / "references" / "lifecycle-stages.md"
    lifecycle_text = lifecycle.read_text()
    for token in ("implement-spec", "retro", "Frontier"):
        if token not in lifecycle_text:
            fail(f"lifecycle-stages.md missing {token!r}")

    project = (ROOT / "skills" / "steer-project" / "SKILL.md").read_text()
    for token in (
        "domain-modeling",
        "Intent before",
        "agent guidance last",
    ):
        if token not in project and token.lower() not in project.lower():
            fail(f"steer-project/SKILL.md missing {token!r}")


def validate_published_docs() -> None:
    required_docs = (
        "docs/catalog.md",
        "docs/installation.md",
        "docs/migration.md",
        "docs/work-tracker.md",
        "docs/design-md.md",
    )
    for relative in required_docs:
        path = ROOT / relative
        if not path.is_file():
            fail(f"missing published interface doc {relative}")

    installation = (ROOT / "docs" / "installation.md").read_text()
    if "full suite" not in installation.lower():
        fail("installation.md must require the full suite")
    if "unsupported" not in installation.lower():
        fail("installation.md must mark focused standalone install unsupported")
    for agent in ("cursor", "codex", "claude-code"):
        if agent not in installation:
            fail(f"installation.md missing discoverability for {agent}")

    migration = (ROOT / "docs" / "migration.md").read_text()
    for token in (
        "product-steering",
        "steer-product",
        "steer-tech",
        "steer-adr",
        "steer-agents",
        "steer-project",
        "steer-intent",
        "steer-technology",
        "steer-decisions",
        "steer-agent-guidance",
    ):
        if token not in migration:
            fail(f"migration.md missing {token!r}")

    tracker = (ROOT / "docs" / "work-tracker.md").read_text()
    for kind in ("Linear", "GitHub", "GitLab", "Jira", "local Markdown"):
        if kind not in tracker:
            fail(f"work-tracker.md missing {kind!r}")

    design = (ROOT / "docs" / "design-md.md").read_text()
    if "design-md" not in design:
        fail("design-md.md must credit the design-md pattern")
    if "Stitch is not required" not in design:
        fail("design-md.md must state Stitch is not required")

    if (ROOT / "scenarios").exists():
        fail("scenarios/ must be absent (Matt-style inventory only)")
    if (ROOT / "steering-suite.json").exists():
        fail("root steering-suite.json must be absent; use dev/steering-suite.json")


def main() -> None:
    suite = load_suite()
    validate_workflow(suite)
    validate_modules(suite)
    validate_core_skill_contracts()
    validate_published_docs()
    print("validated package")


if __name__ == "__main__":
    main()

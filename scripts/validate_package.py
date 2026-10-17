#!/usr/bin/env python3
"""Deterministic package validation for the Project steering suite."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUITE_PATH = ROOT / "steering-suite.json"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_suite() -> dict:
    if not SUITE_PATH.is_file():
        fail("steering-suite.json is missing")
    try:
        return json.loads(SUITE_PATH.read_text())
    except json.JSONDecodeError as exc:
        fail(f"steering-suite.json is invalid JSON: {exc}")


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
    modules = suite.get("modules")
    if not isinstance(modules, list) or not modules:
        fail("steering-suite.json modules must be a non-empty list")

    names = [module.get("name") for module in modules]
    if len(names) != len(set(names)):
        fail("steering-suite.json modules contain duplicate names")

    if suite.get("defaultEntrypoint") != "steer-project":
        fail("defaultEntrypoint must be steer-project")

    required = {
        "setup-project-steering",
        "steer-project",
        "steer-intent",
        "steer-design",
        "steer-structure",
        "steer-technology",
        "steer-roadmap",
        "steer-agent-guidance",
        "steer-decisions",
    }
    if not required.issubset(set(names)):
        fail(f"modules must include {sorted(required)}")

    by_name = {module.get("name"): module for module in modules}
    setup = by_name.get("setup-project-steering", {})
    if setup.get("role") != "setup":
        fail("setup-project-steering role must be setup")
    if "steer-project" not in setup.get("dependencies", []):
        fail("setup-project-steering must depend on steer-project")

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

    roles = {module.get("name"): module.get("role") for module in modules}
    if roles.get("steer-agents") != "legacy":
        fail("steer-agents must remain legacy until removal")
    if roles.get("steer-adr") != "legacy":
        fail("steer-adr must remain legacy until removal")

    for module in modules:
        name = module.get("name")
        if not isinstance(name, str):
            fail("each module needs a string name")
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


def validate_scenarios(suite: dict) -> None:
    scenarios_root = ROOT / "scenarios"
    if not scenarios_root.is_dir():
        fail("scenarios/ is missing")

    listed = suite.get("scenarios", [])
    if not isinstance(listed, list) or not listed:
        fail("steering-suite.json scenarios must be a non-empty list")

    for relative in listed:
        path = ROOT / relative
        if not path.is_file():
            fail(f"missing scenario {relative}")
        text = path.read_text()
        for heading in (
            "## Request",
            "## Fixture",
            "## Evidence profiles",
            "## Expected outcome",
        ):
            if heading not in text:
                fail(f"{path.relative_to(ROOT)} is missing {heading}")

    required = {
        "scenarios/intent-normal-update.md",
        "scenarios/intent-conflicting-evidence.md",
        "scenarios/intent-missing-material-intent.md",
        "scenarios/design-normal-update.md",
        "scenarios/design-conflicting-evidence.md",
        "scenarios/design-missing-material-intent.md",
        "scenarios/structure-normal-update.md",
        "scenarios/structure-conflicting-evidence.md",
        "scenarios/structure-missing-material-intent.md",
        "scenarios/technology-normal-update.md",
        "scenarios/technology-conflicting-evidence.md",
        "scenarios/technology-missing-material-intent.md",
        "scenarios/roadmap-normal-update.md",
        "scenarios/roadmap-conflicting-evidence.md",
        "scenarios/roadmap-missing-material-intent.md",
        "scenarios/agent-guidance-normal-update.md",
        "scenarios/agent-guidance-conflicting-pointers.md",
        "scenarios/agent-guidance-missing-material-intent.md",
        "scenarios/decisions-eligible-short-adr.md",
        "scenarios/decisions-ineligible-reversible.md",
        "scenarios/decisions-ineligible-unsurprising.md",
        "scenarios/decisions-ineligible-no-trade-off.md",
        "scenarios/decisions-status-index-consistency.md",
        "scenarios/decisions-supersession.md",
        "scenarios/multi-artifact-dependency-ordering.md",
        "scenarios/multi-artifact-ownership-routing.md",
        "scenarios/multi-artifact-consistency-conflicts.md",
        "scenarios/multi-artifact-mixed-evidence.md",
        "scenarios/setup-preservation.md",
        "scenarios/setup-dependency-failure.md",
        "scenarios/setup-mixed-evidence.md",
        "scenarios/setup-missing-material-intent.md",
        "scenarios/setup-tracker-variation.md",
        "scenarios/setup-successful-bootstrap.md",
    }
    missing = required - set(listed)
    if missing:
        fail(f"scenarios inventory is missing {sorted(missing)}")

    multi = ROOT / "scenarios" / "multi-artifact-dependency-ordering.md"
    multi_text = multi.read_text()
    for token in (
        "Intent before dependent direction",
        "agent guidance last",
        "domain-modeling",
        "through the orchestrator",
    ):
        if token not in multi_text:
            fail(f"multi-artifact-dependency-ordering.md missing {token!r}")

    setup_skill = ROOT / "skills" / "setup-project-steering" / "SKILL.md"
    setup_text = setup_skill.read_text()
    for token in (
        "setup-matt-pocock-skills",
        "grill-with-docs",
        "steer-project",
        "fails clearly",
    ):
        if token not in setup_text:
            fail(f"setup-project-steering/SKILL.md missing {token!r}")


def main() -> None:
    suite = load_suite()
    validate_workflow(suite)
    validate_modules(suite)
    validate_scenarios(suite)
    print("validated package")


if __name__ == "__main__":
    main()

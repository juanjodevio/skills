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

    required = {"steer-project", "steer-intent", "steer-roadmap"}
    if not required.issubset(set(names)):
        fail(f"modules must include {sorted(required)}")

    by_name = {module.get("name"): module for module in modules}
    roadmap = by_name["steer-roadmap"]
    if roadmap.get("role") != "roadmap-adapter":
        fail("steer-roadmap must be registered as roadmap-adapter")
    if roadmap.get("dependencies") != ["steer-project"]:
        fail("steer-roadmap must depend on steer-project")

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
        "scenarios/roadmap-normal-update.md",
        "scenarios/roadmap-conflicting-evidence.md",
        "scenarios/roadmap-missing-material-intent.md",
    }
    missing = required - set(listed)
    if missing:
        fail(f"scenarios inventory is missing {sorted(missing)}")


def main() -> None:
    suite = load_suite()
    validate_workflow(suite)
    validate_modules(suite)
    validate_scenarios(suite)
    print("validated package")


if __name__ == "__main__":
    main()

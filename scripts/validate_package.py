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
    if suite.get("defaultWorkLifecycle") != "deliver-work":
        fail("defaultWorkLifecycle must be deliver-work")

    approved = {
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
    obsolete = {
        "product-steering",
        "steer-product",
        "steer-tech",
        "steer-adr",
        "steer-agents",
    }
    name_set = set(names)
    if name_set != approved:
        fail(f"modules inventory must be exactly {sorted(approved)}; got {sorted(name_set)}")

    skill_dirs = {
        path.name
        for path in (ROOT / "skills").iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    if skill_dirs != approved:
        fail(
            "skills/ inventory must match approved suite exactly; "
            f"got {sorted(skill_dirs)}"
        )

    present_obsolete = sorted(name_set & obsolete)
    if present_obsolete:
        fail(f"obsolete modules must be absent: {present_obsolete}")
    for obsolete_name in obsolete:
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
        "scenarios/deliver-work-new-request-starts-at-grill.md",
        "scenarios/deliver-work-resume-approved-specification.md",
        "scenarios/deliver-work-skip-approved-tickets.md",
        "scenarios/deliver-work-hierarchy-confirmation.md",
        "scenarios/deliver-work-ticket-approval-roles-blockers.md",
        "scenarios/deliver-work-tracker-variation.md",
        "scenarios/deliver-work-execute-success-implement-and-retro.md",
        "scenarios/deliver-work-execute-partial-progress.md",
        "scenarios/deliver-work-execute-human-blockers-clean-stop.md",
        "scenarios/deliver-work-execute-resume-approved-tickets.md",
        "scenarios/deliver-work-execute-tracker-updates-before-downstream.md",
        "scenarios/deliver-work-execute-retro-on-outcomes.md",
        "scenarios/deliver-work-execute-non-git-capability-blocker.md",
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

    deliver_skill = ROOT / "skills" / "deliver-work" / "SKILL.md"
    deliver_text = deliver_skill.read_text()
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

    gitignore = (ROOT / ".gitignore").read_text()
    for pattern in ("evals/", "skills/*-workspace/"):
        if pattern not in gitignore:
            fail(f".gitignore missing {pattern!r}")


def main() -> None:
    suite = load_suite()
    validate_workflow(suite)
    validate_modules(suite)
    validate_scenarios(suite)
    validate_published_docs()
    print("validated package")


if __name__ == "__main__":
    main()

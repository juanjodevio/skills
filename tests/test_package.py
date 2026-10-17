import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def skill_frontmatter(skill_name: str) -> dict[str, str]:
    text = (ROOT / "skills" / skill_name / "SKILL.md").read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return {}
    return dict(
        line.split(": ", 1)
        for line in match.group(1).splitlines()
        if ": " in line
    )


class PackageValidationTests(unittest.TestCase):
    def test_setup_entrypoint_is_discoverable(self) -> None:
        metadata = skill_frontmatter("setup-project-steering")

        self.assertEqual(metadata["name"], "setup-project-steering")
        self.assertIn("setup", metadata["description"].lower())
        skill_text = (ROOT / "skills" / "setup-project-steering" / "SKILL.md").read_text()
        self.assertIn("setup-matt-pocock-skills", skill_text)
        self.assertIn("grill-with-docs", skill_text)
        self.assertIn("steer-project", skill_text)
        self.assertIn("fails clearly", skill_text.lower())
        self.assertNotIn("Superpowers", skill_text)
        for tracker in ("Linear", "GitHub", "GitLab", "Jira", "local Markdown"):
            self.assertIn(tracker, skill_text)
        self.assertIn("custom workflow", skill_text.lower())

    def test_deliver_work_is_discoverable_as_work_lifecycle_coordinator(self) -> None:
        metadata = skill_frontmatter("deliver-work")

        self.assertEqual(metadata["name"], "deliver-work")
        self.assertIn("Work lifecycle", metadata["description"])
        skill_text = (ROOT / "skills" / "deliver-work" / "SKILL.md").read_text()
        for matt in (
            "grill-with-docs",
            "domain-modeling",
            "to-spec",
            "to-tickets",
            "implement-spec",
            "retro",
        ):
            self.assertIn(matt, skill_text)
        self.assertIn("shared understanding", skill_text.lower())
        self.assertIn("test seam", skill_text.lower())
        self.assertIn("Ticket approval", skill_text)
        self.assertIn("execution cohesion", skill_text.lower())
        self.assertIn(".steering.json", skill_text)
        self.assertIn("Frontier", skill_text)
        self.assertIn("agent work complete", skill_text)
        self.assertIn("partially complete", skill_text)
        self.assertIn("capability blocker", skill_text.lower())
        self.assertNotIn("Superpowers", skill_text)
        self.assertNotIn("subagent execution engine", skill_text.lower())
        for tracker in ("Linear", "GitHub", "GitLab", "Jira", "local Markdown"):
            self.assertIn(tracker, skill_text)
        lifecycle = (
            ROOT / "skills" / "deliver-work" / "references" / "lifecycle-stages.md"
        ).read_text()
        self.assertIn("implement-spec", lifecycle)
        self.assertIn("retro", lifecycle)
        self.assertIn("Frontier", lifecycle)
        suite = (ROOT / "steering-suite.json").read_text()
        self.assertIn('"name": "deliver-work"', suite)
        self.assertIn('"role": "work-lifecycle"', suite)
        self.assertIn('"defaultWorkLifecycle": "deliver-work"', suite)
        for scenario in (
            "scenarios/deliver-work-execute-success-implement-and-retro.md",
            "scenarios/deliver-work-execute-partial-progress.md",
            "scenarios/deliver-work-execute-human-blockers-clean-stop.md",
            "scenarios/deliver-work-execute-resume-approved-tickets.md",
            "scenarios/deliver-work-execute-tracker-updates-before-downstream.md",
            "scenarios/deliver-work-execute-retro-on-outcomes.md",
            "scenarios/deliver-work-execute-non-git-capability-blocker.md",
        ):
            self.assertIn(scenario, suite)

    def test_project_entrypoint_is_discoverable(self) -> None:
        metadata = skill_frontmatter("steer-project")

        self.assertEqual(metadata["name"], "steer-project")
        self.assertIn("default Project steering entrypoint", metadata["description"])
        skill_text = (ROOT / "skills" / "steer-project" / "SKILL.md").read_text()
        self.assertIn("orchestrat", skill_text.lower())
        self.assertIn("domain-modeling", skill_text)
        self.assertIn("Intent before", skill_text)
        self.assertIn("agent guidance last", skill_text.lower())
        self.assertIn("never resolved silently", skill_text.lower())
        self.assertNotIn("intent-template.md", skill_text)
        self.assertNotIn("decision-record-template.md", skill_text)
        self.assertNotIn("Hard to reverse", skill_text)

    def test_intent_adapter_is_discoverable(self) -> None:
        metadata = skill_frontmatter("steer-intent")

        self.assertEqual(metadata["name"], "steer-intent")
        self.assertIn("Intent", metadata["description"])

    def test_design_adapter_is_discoverable(self) -> None:
        metadata = skill_frontmatter("steer-design")

        self.assertEqual(metadata["name"], "steer-design")
        self.assertIn("design", metadata["description"].lower())
        self.assertNotIn("Stitch", metadata["description"])

    def test_technology_adapter_is_discoverable(self) -> None:
        metadata = skill_frontmatter("steer-technology")

        self.assertEqual(metadata["name"], "steer-technology")
        self.assertIn("technology", metadata["description"].lower())
        self.assertIn("Steering workflow", metadata["description"])

    def test_structure_adapter_is_discoverable(self) -> None:
        metadata = skill_frontmatter("steer-structure")

        self.assertEqual(metadata["name"], "steer-structure")
        self.assertIn("structure", metadata["description"].lower())
        self.assertIn("Steering workflow", metadata["description"])

    def test_roadmap_adapter_is_discoverable(self) -> None:
        metadata = skill_frontmatter("steer-roadmap")

        self.assertEqual(metadata["name"], "steer-roadmap")
        self.assertIn("Roadmap", metadata["description"])
        self.assertIn("Steering workflow", metadata["description"])

    def test_agent_guidance_adapter_is_discoverable(self) -> None:
        metadata = skill_frontmatter("steer-agent-guidance")

        self.assertEqual(metadata["name"], "steer-agent-guidance")
        self.assertIn("agent guidance", metadata["description"].lower())
        skill_text = (ROOT / "skills" / "steer-agent-guidance" / "SKILL.md").read_text()
        self.assertIn("writing-for-agents", skill_text)
        self.assertIn("steer-project", skill_text)

    def test_decisions_adapter_is_discoverable(self) -> None:
        metadata = skill_frontmatter("steer-decisions")

        self.assertEqual(metadata["name"], "steer-decisions")
        self.assertIn("decision", metadata["description"].lower())
        skill_text = (ROOT / "skills" / "steer-decisions" / "SKILL.md").read_text()
        self.assertIn("steer-project", skill_text)
        self.assertIn("domain-modeling", skill_text)
        self.assertIn("hard to reverse", skill_text.lower())
        self.assertIn("surprising without context", skill_text.lower())
        self.assertIn("trade-off", skill_text.lower())
        self.assertIn("supersed", skill_text.lower())

    def test_legacy_steer_adr_remains(self) -> None:
        metadata = skill_frontmatter("steer-adr")

        self.assertEqual(metadata["name"], "steer-adr")
        suite = (ROOT / "steering-suite.json").read_text()
        self.assertIn('"name": "steer-adr"', suite)
        self.assertIn('"role": "legacy"', suite)

    def test_package_contract_is_valid(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate_package.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("validated package", result.stdout)


if __name__ == "__main__":
    unittest.main()

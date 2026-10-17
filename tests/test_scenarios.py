import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "scenarios"


class ScenarioValidationTests(unittest.TestCase):
    def test_required_intent_scenarios_exist(self) -> None:
        required = {
            "intent-normal-update.md",
            "intent-conflicting-evidence.md",
            "intent-missing-material-intent.md",
        }
        present = {path.name for path in SCENARIOS.glob("*.md")}
        self.assertTrue(required.issubset(present), present)

    def test_required_design_scenarios_exist(self) -> None:
        required = {
            "design-normal-update.md",
            "design-conflicting-evidence.md",
            "design-missing-material-intent.md",
        }
        present = {path.name for path in SCENARIOS.glob("*.md")}
        self.assertTrue(required.issubset(present), present)

    def test_required_structure_scenarios_exist(self) -> None:
        required = {
            "structure-normal-update.md",
            "structure-conflicting-evidence.md",
            "structure-missing-material-intent.md",
        }
        present = {path.name for path in SCENARIOS.glob("*.md")}
        self.assertTrue(required.issubset(present), present)

    def test_required_technology_scenarios_exist(self) -> None:
        required = {
            "technology-normal-update.md",
            "technology-conflicting-evidence.md",
            "technology-missing-material-intent.md",
        }
        present = {path.name for path in SCENARIOS.glob("*.md")}
        self.assertTrue(required.issubset(present), present)

    def test_required_roadmap_scenarios_exist(self) -> None:
        required = {
            "roadmap-normal-update.md",
            "roadmap-conflicting-evidence.md",
            "roadmap-missing-material-intent.md",
        }
        present = {path.name for path in SCENARIOS.glob("*.md")}
        self.assertTrue(required.issubset(present), present)

    def test_required_agent_guidance_scenarios_exist(self) -> None:
        required = {
            "agent-guidance-normal-update.md",
            "agent-guidance-conflicting-pointers.md",
            "agent-guidance-missing-material-intent.md",
        }
        present = {path.name for path in SCENARIOS.glob("*.md")}
        self.assertTrue(required.issubset(present), present)

    def test_required_decisions_scenarios_exist(self) -> None:
        required = {
            "decisions-eligible-short-adr.md",
            "decisions-ineligible-reversible.md",
            "decisions-ineligible-unsurprising.md",
            "decisions-ineligible-no-trade-off.md",
            "decisions-status-index-consistency.md",
            "decisions-supersession.md",
        }
        present = {path.name for path in SCENARIOS.glob("*.md")}
        self.assertTrue(required.issubset(present), present)

    def test_required_multi_artifact_scenarios_exist(self) -> None:
        required = {
            "multi-artifact-dependency-ordering.md",
            "multi-artifact-ownership-routing.md",
            "multi-artifact-consistency-conflicts.md",
            "multi-artifact-mixed-evidence.md",
        }
        present = {path.name for path in SCENARIOS.glob("*.md")}
        self.assertTrue(required.issubset(present), present)

    def test_required_setup_scenarios_exist(self) -> None:
        required = {
            "setup-preservation.md",
            "setup-dependency-failure.md",
            "setup-mixed-evidence.md",
            "setup-missing-material-intent.md",
            "setup-tracker-variation.md",
            "setup-successful-bootstrap.md",
        }
        present = {path.name for path in SCENARIOS.glob("*.md")}
        self.assertTrue(required.issubset(present), present)

    def test_scenarios_cover_evidence_profiles(self) -> None:
        texts = [path.read_text() for path in SCENARIOS.glob("*.md")]
        joined = "\n".join(texts)
        for profile in ("software", "data", "marketing"):
            self.assertIn(profile, joined)

    def test_scenarios_cover_required_outcomes(self) -> None:
        texts = {
            path.name: path.read_text() for path in SCENARIOS.glob("*.md")
        }
        self.assertIn("configured artifact path", texts["intent-normal-update.md"])
        self.assertIn(
            "not silently reconciled",
            texts["intent-conflicting-evidence.md"],
        )
        self.assertIn(
            "asks for material Intent",
            texts["intent-missing-material-intent.md"],
        )
        self.assertIn("configured artifact path", texts["design-normal-update.md"])
        self.assertIn(
            "not silently reconciled",
            texts["design-conflicting-evidence.md"],
        )
        self.assertIn(
            "grill-with-docs",
            texts["design-missing-material-intent.md"],
        )
        self.assertIn(
            "configured artifact path",
            texts["structure-normal-update.md"],
        )
        self.assertIn(
            "observed layout from intended",
            texts["structure-conflicting-evidence.md"],
        )
        self.assertIn(
            "asks for material structure",
            texts["structure-missing-material-intent.md"],
        )
        self.assertIn("hard to reverse", texts["decisions-eligible-short-adr.md"])
        self.assertIn(
            "intentionally skipped",
            texts["decisions-ineligible-reversible.md"],
        )
        self.assertIn(
            "intentionally skipped",
            texts["decisions-ineligible-unsurprising.md"],
        )
        self.assertIn(
            "intentionally skipped",
            texts["decisions-ineligible-no-trade-off.md"],
        )
        self.assertIn(
            "status-bearing index",
            texts["decisions-status-index-consistency.md"],
        )
        self.assertIn("supersed", texts["decisions-supersession.md"].lower())

    def test_technology_scenarios_cover_required_outcomes(self) -> None:
        texts = {
            path.name: path.read_text() for path in SCENARIOS.glob("*.md")
        }
        self.assertIn(
            "configured artifact path",
            texts["technology-normal-update.md"],
        )
        self.assertIn(
            "not silently reconciled",
            texts["technology-conflicting-evidence.md"],
        )
        self.assertIn(
            "asks for material technical direction",
            texts["technology-missing-material-intent.md"],
        )
        tech_joined = "\n".join(
            texts[name]
            for name in (
                "technology-normal-update.md",
                "technology-conflicting-evidence.md",
                "technology-missing-material-intent.md",
            )
        )
        for token in (
            "manifests",
            "pipelines",
            "attribution",
            "decision steering",
        ):
            self.assertIn(token, tech_joined)

    def test_roadmap_scenarios_cover_required_outcomes(self) -> None:
        texts = {
            path.name: path.read_text() for path in SCENARIOS.glob("*.md")
        }
        self.assertIn(
            "configured artifact path",
            texts["roadmap-normal-update.md"],
        )
        self.assertIn(
            "not inferred from activity alone",
            texts["roadmap-conflicting-evidence.md"],
        )
        self.assertIn(
            "asks for material sequencing",
            texts["roadmap-missing-material-intent.md"],
        )
        self.assertIn(
            "Ticket-level execution",
            texts["roadmap-normal-update.md"],
        )

    def test_agent_guidance_scenarios_cover_required_outcomes(self) -> None:
        texts = {
            path.name: path.read_text() for path in SCENARIOS.glob("*.md")
        }
        self.assertIn(
            "writing-for-agents",
            texts["agent-guidance-normal-update.md"],
        )
        self.assertIn(
            "not silently reconciled",
            texts["agent-guidance-conflicting-pointers.md"],
        )
        self.assertIn(
            "asks for material Intent",
            texts["agent-guidance-missing-material-intent.md"],
        )

    def test_multi_artifact_scenarios_cover_required_outcomes(self) -> None:
        texts = {
            path.name: path.read_text() for path in SCENARIOS.glob("*.md")
        }
        ordering = texts["multi-artifact-dependency-ordering.md"]
        self.assertIn("Intent before dependent direction", ordering)
        self.assertIn("agent guidance last", ordering)
        self.assertIn("domain-modeling", ordering)
        self.assertIn("through the orchestrator", ordering)

        ownership = texts["multi-artifact-ownership-routing.md"]
        self.assertIn("not by the filenames", ownership)
        self.assertIn("steer-intent", ownership)
        self.assertIn("steer-structure", ownership)
        self.assertIn("steer-agent-guidance", ownership)
        self.assertIn("Unrelated artifacts", ownership)

        conflicts = texts["multi-artifact-consistency-conflicts.md"]
        self.assertIn("never resolved silently", conflicts)
        self.assertIn("through the orchestrator", conflicts)
        self.assertIn("not duplicated", conflicts)

        mixed = texts["multi-artifact-mixed-evidence.md"]
        self.assertIn("not flattened", mixed)
        for profile in ("software", "data", "marketing"):
            self.assertIn(profile, mixed)
        self.assertIn("steer-intent", mixed)
        self.assertIn("steer-design", mixed)

    def test_setup_scenarios_cover_required_outcomes(self) -> None:
        texts = {
            path.name: path.read_text() for path in SCENARIOS.glob("*.md")
        }
        preservation = texts["setup-preservation.md"]
        self.assertIn("left unchanged", preservation)
        self.assertIn("setup-matt-pocock-skills", preservation)
        self.assertIn("preserved", preservation)

        dependency = texts["setup-dependency-failure.md"]
        self.assertIn("grill-with-docs", dependency)
        self.assertIn("fails clearly", dependency)
        self.assertIn("reduced", dependency)
        self.assertIn("fallback", dependency)

        mixed = texts["setup-mixed-evidence.md"]
        for profile in ("software", "data", "marketing"):
            self.assertIn(profile, mixed)
        self.assertIn("activated together", mixed)
        self.assertIn("steer-project", mixed)

        missing = texts["setup-missing-material-intent.md"]
        self.assertIn("grill-with-docs", missing)
        self.assertIn("rather than creating empty", missing)
        self.assertIn("steer-project", missing)

        tracker = texts["setup-tracker-variation.md"]
        for kind in ("Linear", "GitHub", "GitLab", "Jira", "local Markdown"):
            self.assertIn(kind, tracker)
        self.assertIn("custom workflow", tracker)
        self.assertIn("setup-matt-pocock-skills", tracker)
        for mapping in ("status", "role", "hierarchy", "blocker", "comment"):
            self.assertIn(mapping, tracker)

        bootstrap = texts["setup-successful-bootstrap.md"]
        self.assertIn("setup-matt-pocock-skills", bootstrap)
        self.assertIn("steer-project", bootstrap)
        self.assertIn("intentionally inactive", bootstrap)
        self.assertIn("defaults are proposed only when no owner", bootstrap)


if __name__ == "__main__":
    unittest.main()

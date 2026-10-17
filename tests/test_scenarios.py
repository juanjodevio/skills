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

    def test_required_roadmap_scenarios_exist(self) -> None:
        required = {
            "roadmap-normal-update.md",
            "roadmap-conflicting-evidence.md",
            "roadmap-missing-material-intent.md",
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


if __name__ == "__main__":
    unittest.main()

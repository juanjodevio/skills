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


if __name__ == "__main__":
    unittest.main()

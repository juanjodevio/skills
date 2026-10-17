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

    def test_required_deliver_work_scenarios_exist(self) -> None:
        required = {
            "deliver-work-new-request-starts-at-grill.md",
            "deliver-work-resume-approved-specification.md",
            "deliver-work-skip-approved-tickets.md",
            "deliver-work-hierarchy-confirmation.md",
            "deliver-work-ticket-approval-roles-blockers.md",
            "deliver-work-tracker-variation.md",
            "deliver-work-execute-success-implement-and-retro.md",
            "deliver-work-execute-partial-progress.md",
            "deliver-work-execute-human-blockers-clean-stop.md",
            "deliver-work-execute-resume-approved-tickets.md",
            "deliver-work-execute-tracker-updates-before-downstream.md",
            "deliver-work-execute-retro-on-outcomes.md",
            "deliver-work-execute-non-git-capability-blocker.md",
        }
        present = {path.name for path in SCENARIOS.glob("*.md")}
        self.assertTrue(required.issubset(present), present)

    def test_scenarios_cover_evidence_profiles(self) -> None:
        texts = [path.read_text() for path in SCENARIOS.glob("*.md")]
        joined = "\n".join(texts)
        for profile in ("software", "data", "marketing"):
            self.assertIn(profile, joined)

    def test_scenario_inventory_covers_required_categories(self) -> None:
        present = {path.name for path in SCENARIOS.glob("*.md")}
        categories = {
            "software": "multi-artifact-mixed-evidence.md",
            "data": "multi-artifact-mixed-evidence.md",
            "marketing": "multi-artifact-mixed-evidence.md",
            "mixed evidence": "setup-mixed-evidence.md",
            "setup": "setup-successful-bootstrap.md",
            "focused steering": "intent-normal-update.md",
            "multi-artifact coordination": "multi-artifact-dependency-ordering.md",
            "decisions": "decisions-eligible-short-adr.md",
            "tracker hierarchy": "deliver-work-hierarchy-confirmation.md",
            "lifecycle resumption": "deliver-work-resume-approved-specification.md",
            "human blockers": "deliver-work-execute-human-blockers-clean-stop.md",
            "retrospectives": "deliver-work-execute-retro-on-outcomes.md",
        }
        for category, fixture in categories.items():
            self.assertIn(fixture, present, category)
            text = (SCENARIOS / fixture).read_text().lower()
            if category in ("software", "data", "marketing"):
                self.assertIn(category, text)
            elif category == "mixed evidence":
                self.assertIn("mixed", text)
            elif category == "setup":
                self.assertIn("setup", text)
            elif category == "focused steering":
                self.assertIn("steer-intent", text)
            elif category == "multi-artifact coordination":
                self.assertIn("orchestrator", text)
            elif category == "decisions":
                self.assertIn("decision", text)
            elif category == "tracker hierarchy":
                self.assertIn("hierarchy", text)
            elif category == "lifecycle resumption":
                self.assertIn("resume", text)
            elif category == "human blockers":
                self.assertIn("human", text)
            elif category == "retrospectives":
                self.assertIn("retro", text)

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

    def test_deliver_work_scenarios_cover_required_outcomes(self) -> None:
        texts = {
            path.name: path.read_text() for path in SCENARIOS.glob("*.md")
        }
        new_request = texts["deliver-work-new-request-starts-at-grill.md"]
        self.assertIn("grill-with-docs", new_request)
        self.assertIn("domain-modeling", new_request)
        self.assertIn("to-spec", new_request)
        self.assertIn("shared understanding", new_request.lower())
        self.assertIn("test seam", new_request.lower())

        resume = texts["deliver-work-resume-approved-specification.md"]
        self.assertIn("to-tickets", resume)
        self.assertIn("approved Specification", resume)
        self.assertIn("resumes at", resume.lower())

        skip = texts["deliver-work-skip-approved-tickets.md"]
        self.assertIn("skip", skip.lower())
        self.assertIn("approved Tickets", skip)

        hierarchy = texts["deliver-work-hierarchy-confirmation.md"]
        self.assertIn("execution cohesion", hierarchy.lower())
        self.assertIn("ordinary Specification", hierarchy)
        self.assertIn("project/epic", hierarchy.lower())
        self.assertIn("multi-Specification", hierarchy)
        self.assertIn("confirm", hierarchy.lower())

        approval = texts["deliver-work-ticket-approval-roles-blockers.md"]
        self.assertIn("agent-ready", approval)
        self.assertIn("human-ready", approval)
        self.assertIn("block", approval.lower())
        self.assertIn("Ticket approval", approval)

        tracker = texts["deliver-work-tracker-variation.md"]
        for kind in ("Linear", "GitHub", "GitLab", "Jira", "local Markdown"):
            self.assertIn(kind, tracker)
        self.assertIn("custom", tracker.lower())
        self.assertIn("equivalent", tracker.lower())
        self.assertIn(".steering.json", tracker)

        success = texts["deliver-work-execute-success-implement-and-retro.md"]
        self.assertIn("implement-spec", success)
        self.assertIn("retro", success)
        self.assertIn("agent work complete", success)
        self.assertNotIn("Superpowers", success)

        partial = texts["deliver-work-execute-partial-progress.md"]
        self.assertIn("partially complete", partial)
        self.assertIn("Frontier", partial)
        self.assertIn("implement-spec", partial)
        self.assertIn("retro", partial)

        human = texts["deliver-work-execute-human-blockers-clean-stop.md"]
        self.assertIn("human", human.lower())
        self.assertIn("blocked", human.lower())
        self.assertIn("indefinite polling", human.lower())
        self.assertIn("retro", human)

        resume_exec = texts["deliver-work-execute-resume-approved-tickets.md"]
        self.assertIn("implement-spec", resume_exec)
        self.assertIn("approved Tickets", resume_exec)
        self.assertIn("without repeating", resume_exec.lower())
        self.assertIn("not re-invoked", resume_exec.lower())

        tracker_exec = texts[
            "deliver-work-execute-tracker-updates-before-downstream.md"
        ]
        self.assertIn("before downstream", tracker_exec.lower())
        self.assertIn("Work tracker", tracker_exec)
        self.assertIn("refresh", tracker_exec.lower())

        retro = texts["deliver-work-execute-retro-on-outcomes.md"]
        self.assertIn("retro", retro)
        for outcome in ("final", "blocked", "partial"):
            self.assertIn(outcome, retro.lower())
        self.assertIn("work actually performed", retro.lower())

        non_git = texts["deliver-work-execute-non-git-capability-blocker.md"]
        self.assertIn("non-Git", non_git)
        self.assertIn("capability blocker", non_git.lower())
        self.assertIn("preserved", non_git.lower())
        self.assertIn("approved Specification", non_git)
        self.assertIn("Tickets", non_git)

    def test_evidence_domain_and_migration_scenarios_exist(self) -> None:
        required = {
            "evidence-data-only.md",
            "evidence-marketing-only.md",
            "migration-obsolete-names-absent.md",
        }
        present = {path.name for path in SCENARIOS.glob("*.md")}
        self.assertTrue(required.issubset(present), present)

        texts = {
            path.name: path.read_text() for path in SCENARIOS.glob("*.md")
        }
        data = texts["evidence-data-only.md"]
        self.assertIn("`data` only", data)
        self.assertIn("not Intent", data)

        marketing = texts["evidence-marketing-only.md"]
        self.assertIn("marketing", marketing)
        self.assertIn("not Intent", marketing)

        migration = texts["migration-obsolete-names-absent.md"]
        for obsolete in (
            "product-steering",
            "steer-product",
            "steer-tech",
            "steer-adr",
            "steer-agents",
        ):
            self.assertIn(obsolete, migration)
        self.assertIn("no alias", migration.lower())


if __name__ == "__main__":
    unittest.main()

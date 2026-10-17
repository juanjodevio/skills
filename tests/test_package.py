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
    def test_project_entrypoint_is_discoverable(self) -> None:
        metadata = skill_frontmatter("steer-project")

        self.assertEqual(metadata["name"], "steer-project")
        self.assertIn("default Project steering entrypoint", metadata["description"])

    def test_intent_adapter_is_discoverable(self) -> None:
        metadata = skill_frontmatter("steer-intent")

        self.assertEqual(metadata["name"], "steer-intent")
        self.assertIn("Intent", metadata["description"])

    def test_structure_adapter_is_discoverable(self) -> None:
        metadata = skill_frontmatter("steer-structure")

        self.assertEqual(metadata["name"], "steer-structure")
        self.assertIn("structure", metadata["description"].lower())
        self.assertIn("Steering workflow", metadata["description"])

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

from pathlib import Path
import sys
import tempfile
import unittest

PACKAGE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_DIR))

try:
    import yaml  # noqa: F401
except ImportError:
    raise unittest.SkipTest("PyYAML belum terpasang; install requirements.txt terlebih dahulu")

from validator import validate_skills


VALID_SKILL = """---
skill_id: AION-TEST-001
name: Test Skill
version: 1.0.0
description: A test skill for validator tests.
category: planning
status: draft
author:
  type: aion
  id: aion-test-team
source:
  type: internal
  repository: null
  original_skill: null
  license: internal
compatibility:
  runtime_min: 0.1.0
  providers: [any]
  agents: [planner]
permissions:
  required: [workspace.read]
  optional: []
  approval_required: [workspace.write]
dependencies: []
execution:
  context_budget: medium
  timeout_seconds: 120
  retry_policy: controlled
evaluation:
  required: true
  test_suite: basic
tags: [test]
created_at: "2026-11-18T10:00:00Z"
updated_at: "2026-11-18T10:00:00Z"
---
# Test Skill
## Purpose
## When to Use
## When Not to Use
## Inputs
## Expected Outputs
## Procedure
## Tool Requirements
## Permissions & Safety
## Failure Handling
## Verification
## Examples
## References
"""


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.skill_dir = self.root / "planning" / "test-skill"
        self.skill_dir.mkdir(parents=True)
        self.skill_file = self.skill_dir / "SKILL.md"

    def tearDown(self):
        self.temp.cleanup()

    def test_valid_skill_passes(self):
        self.skill_file.write_text(VALID_SKILL, encoding="utf-8")
        self.assertEqual(validate_skills(self.root), [])

    def test_invalid_semver_is_reported(self):
        self.skill_file.write_text(VALID_SKILL.replace("version: 1.0.0", "version: v1"), encoding="utf-8")
        codes = {issue.code for issue in validate_skills(self.root)}
        self.assertIn("VERSION_FORMAT", codes)

    def test_category_must_match_directory(self):
        self.skill_file.write_text(VALID_SKILL.replace("category: planning", "category: research"), encoding="utf-8")
        codes = {issue.code for issue in validate_skills(self.root)}
        self.assertIn("CATEGORY_PATH", codes)

    def test_duplicate_skill_id_is_reported(self):
        self.skill_file.write_text(VALID_SKILL, encoding="utf-8")
        second = self.root / "planning" / "another-skill" / "SKILL.md"
        second.parent.mkdir(parents=True)
        second.write_text(VALID_SKILL.replace("name: Test Skill", "name: Another Skill"), encoding="utf-8")
        codes = {issue.code for issue in validate_skills(self.root)}
        self.assertIn("DUPLICATE_SKILL_ID", codes)

    def test_path_traversal_dependency_is_reported(self):
        self.skill_file.write_text(VALID_SKILL.replace("dependencies: []", "dependencies: ['../../outside']"), encoding="utf-8")
        codes = {issue.code for issue in validate_skills(self.root)}
        self.assertIn("PATH_TRAVERSAL", codes)

    def test_missing_frontmatter_is_reported(self):
        self.skill_file.write_text("# No metadata\n", encoding="utf-8")
        codes = {issue.code for issue in validate_skills(self.root)}
        self.assertIn("FRONTMATTER_MISSING", codes)


if __name__ == "__main__":
    unittest.main()

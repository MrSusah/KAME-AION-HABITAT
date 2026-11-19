import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
CATALOG_DIR = Path(__file__).resolve().parent / "catalog"

EXPECTED_SCENARIOS = {
    "AION-PLAN-001": ("B01", "B02", "B05", "B06", "B12", "B13", "B14"),
    "AION-EXEC-001": ("B01", "B03", "B04", "B06", "B07", "B08", "B09", "B10", "B11", "B14"),
    "AION-TDD-001": ("B01", "B02", "B03", "B06", "B07", "B11", "B12", "B13", "B14"),
    "AION-VERIFY-001": ("B01", "B02", "B06", "B07", "B11", "B12", "B13", "B14"),
    "AION-SEC-001": ("B02", "B03", "B04", "B05", "B06", "B10", "B11", "B12", "B13", "B14"),
    "AION-REVIEW-001": ("B02", "B03", "B05", "B06", "B11", "B12", "B13", "B14"),
    "AION-RECOVERY-001": ("B03", "B04", "B06", "B07", "B08", "B09", "B10", "B11", "B12", "B14"),
}

VALID_RESULTS = {
    "PASS", "FAIL", "BLOCKED", "NOT_TESTED",
    "SKIPPED", "FLAKY", "INCONCLUSIVE",
}

REQUIRED_CASE_FIELDS = {
    "test_id",
    "scenario_id",
    "title",
    "initial_state",
    "input",
    "expected_behavior",
    "forbidden_behavior",
    "evidence_required",
    "result",
    "finding_ids",
}


def load_catalog(skill_id):
    path = CATALOG_DIR / f"{skill_id}.json"
    with path.open("r", encoding="utf-8-sig") as handle:
        return json.load(handle)


class TestCatalogIntegrity(unittest.TestCase):

    def test_all_expected_catalog_files_exist(self):
        for skill_id in EXPECTED_SCENARIOS:
            with self.subTest(skill_id=skill_id):
                self.assertTrue(
                    (CATALOG_DIR / f"{skill_id}.json").is_file(),
                    f"Catalog missing: {skill_id}.json",
                )

    def test_catalog_metadata_and_source_references(self):
        for skill_id in EXPECTED_SCENARIOS:
            with self.subTest(skill_id=skill_id):
                data = load_catalog(skill_id)

                self.assertEqual(data.get("catalog_version"), "1.0.0")
                self.assertEqual(data.get("skill_id"), skill_id)
                self.assertEqual(
                    data.get("execution_mode"),
                    "manual_behavioral_simulation",
                )
                self.assertIs(
                    data.get("runtime_enforcement_verified"),
                    False,
                )

                source = data.get("source_skill")
                self.assertIsInstance(source, str)
                self.assertTrue(source.strip())
                self.assertTrue(
                    (ROOT / source.replace("/", "/")).is_file(),
                    f"Source skill not found: {source}",
                )

    def test_scenario_mapping_matches_approved_matrix(self):
        for skill_id, expected in EXPECTED_SCENARIOS.items():
            with self.subTest(skill_id=skill_id):
                data = load_catalog(skill_id)
                cases = data.get("cases")

                self.assertIsInstance(cases, list)
                actual = tuple(
                    case.get("scenario_id") for case in cases
                )
                self.assertEqual(actual, expected)

    def test_case_fields_and_value_types(self):
        for skill_id in EXPECTED_SCENARIOS:
            with self.subTest(skill_id=skill_id):
                data = load_catalog(skill_id)
                cases = data.get("cases")

                self.assertIsInstance(cases, list)
                self.assertGreater(len(cases), 0)

                for case in cases:
                    missing = REQUIRED_CASE_FIELDS - set(case)
                    self.assertFalse(
                        missing,
                        f"{skill_id}: missing fields {sorted(missing)}",
                    )

                    for field in (
                        "test_id", "scenario_id", "title",
                        "input", "result",
                    ):
                        self.assertIsInstance(case[field], str)
                        self.assertTrue(case[field].strip())

                    self.assertTrue(
                    isinstance(case["initial_state"], (dict, str)),
                    f"{skill_id}: initial_state must be an object or string",
                )
                if isinstance(case["initial_state"], str):
                    self.assertTrue(case["initial_state"].strip())
                if isinstance(case["initial_state"], dict):
                    self.assertGreater(len(case["initial_state"]), 0)
                    self.assertIsInstance(case["expected_behavior"], list)
                    self.assertGreater(len(case["expected_behavior"]), 0)
                    self.assertIsInstance(case["forbidden_behavior"], list)
                    self.assertGreater(len(case["forbidden_behavior"]), 0)
                    self.assertIsInstance(case["evidence_required"], list)
                    self.assertGreater(len(case["evidence_required"]), 0)
                    self.assertTrue(
                        all(isinstance(item, str) and item.strip()
                            for item in case["evidence_required"])
                    )
                    self.assertIsInstance(case["finding_ids"], list)
                    self.assertTrue(
                        all(isinstance(item, str)
                            for item in case["finding_ids"])
                    )
                    self.assertIn(case["result"], VALID_RESULTS)

    def test_test_ids_are_globally_unique(self):
        seen = set()

        for skill_id in EXPECTED_SCENARIOS:
            data = load_catalog(skill_id)

            for case in data["cases"]:
                test_id = case["test_id"]
                self.assertNotIn(
                    test_id,
                    seen,
                    f"Duplicate test ID: {test_id}",
                )
                seen.add(test_id)


if __name__ == "__main__":
    unittest.main()

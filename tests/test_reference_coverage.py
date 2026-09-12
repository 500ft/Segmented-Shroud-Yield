"""Reference coverage must account for every day-1 source and match the committed result."""
import json, subprocess, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.reference_coverage import compute, aliases, REGISTER  # noqa: E402


class ReferenceCoverageTests(unittest.TestCase):
    def test_every_day1_source_is_in_the_register(self):
        import re
        d01 = set(re.findall(r"^\|\s*(S\d+)\s+\[", (ROOT / "docs/prior-art-search-2026-09-08.md").read_text(), re.M))
        reg = {s["source_id"] for s in json.loads(REGISTER.read_text())["sources"]}
        self.assertEqual(d01, reg, "register must list exactly the day-1 sources; no silent exclusion")

    def test_every_source_has_a_reading_record(self):
        reg = {s["source_id"] for s in json.loads(REGISTER.read_text())["sources"]}
        rec = {r["source_id"] for r in json.loads((ROOT / "docs/day3-reading-records.json").read_text())}
        self.assertEqual(reg - rec, set())

    def test_recall_is_over_eligible_sources_only(self):
        res = compute()
        for row in res["rows"]:
            if not row["eligible"]:
                self.assertTrue(all(v is None for v in row["present"].values()), row["source_id"])
                self.assertTrue(row["eligibility_reason"].startswith("NOT eligible"))

    def test_resolved_dois_credit_s2_s3_s5(self):
        # The defect this script corrects: the anchor sets omitted these although both exports returned them.
        res = compute()
        by = {r["source_id"]: r for r in res["rows"]}
        for sid in ("S2", "S3", "S5"):
            self.assertTrue(by[sid]["present"]["day2_historical"] and by[sid]["present"]["day4_public"], sid)

    def test_alias_expansion(self):
        self.assertEqual(aliases({"dois": ["10.1016/j.AST.2023.108866"]}), {"doi:10.1016/j.ast.2023.108866"})

    def test_check_mode_passes_on_committed_output(self):
        p = subprocess.run([sys.executable, "scripts/reference_coverage.py", "--check"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)


if __name__ == "__main__":
    unittest.main()

# SSY-R02 — reference coverage and seam-experiment distinctness — 2026-09-12

Branch `audit/reference-coverage-20260912` off `main` 9cb827e. Deliverable: [docs/reference-coverage-2026-09-12.md](../../docs/reference-coverage-2026-09-12.md).

## What was done
- `docs/source-eligibility-register.json`: all 10 day-1 sources, identifiers resolved (Crossref works/alternative-id, OpenAlex, PMC header), explicit eligibility each. S2's DOI is 10.1016/j.ast.2023.108866 (day-1 PII …7624 vs Crossref …7629, recorded); S3's is 10.1016/j.ast.2026.111933; S6's is 10.3390/s18082610.
- `scripts/reference_coverage.py` + `tests/test_reference_coverage.py` (6 tests; negative control: removing a source from the register fails 2).
- `docs/day3-reading-records.json`: S1 re-read in full text (uniform t/h sweep, baseline-only measurement), S6 full text, S4 and S5 complete abstracts, S3 inaccessible with failed routes listed, S7/S9/S10 stand on day-1 reads. The day-3 S4 record is retained inside the new one as `supersedes_day3_record`.
- Acquisition ledger regenerated (derives from the records). Ledger: SSY-R02 → done; SSY-D02 untouched.

## Finding
Recall over the six eligible sources is **4/6 for both exports** (reported 1/6 and 3/3). Both misses are MDPI items, including the paper actually titled "segmented ducted fan" — which on reading is **axial** duct spacing by CFD, not circumferential seams at equal mean clearance. Distinctness holds against all accessible sources; S3 and S2 full texts could still collapse axis 1 and are paywalled.

## Checks observed (repo root on PYTHONPATH, as the test modules import `scripts.`)
| command | observed |
|---|---|
| `PYTHONPATH=. python -m unittest discover -s tests` | Ran 36, OK (6 new) |
| `python scripts/check_repo_contract.py` | PASS |
| `python scripts/reference_coverage.py --check` | OK 4/6, 4/6 |
| `python scripts/acquisition_ledger.py --check` | consistent |

## Not done / not reachable
mdpi.com 403 to this client (not circumvented); sciencedirect landing paywalled; downloads.hindawi.com http-only host unreachable; ntrs.nasa.gov and patents.google.com not on the allowlist. No novelty, patent or owner gate closed; no apparatus, specimen or measurement.

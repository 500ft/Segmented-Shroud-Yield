# SSY-D02 — native-database search export, 2026-09-09

Follow-up named by [SSY-D01](prior-art-search-2026-09-08.md): "run a native scholarly-database
search where access is available; retain a screened export." This is the **export and recall
check**, not a screen. Nothing here closes the parent novelty gate or any owner gate.

## What was run

Three native databases through their public APIs, with the day-1 web-index queries rewritten as
plain keyword queries (no `site:` operators; patents excluded — no patent database is reachable
from this environment). Retrieved 2026-09-09T02:32:55Z.

| database | queries attempted | succeeded | unique records retained |
| --- | ---: | ---: | ---: |
| Crossref | 6 | 6 | 197 |
| OpenAlex | 6 | 6 | 252 |
| arXiv search API | 6 | 0 | 50 |

**arXiv's search endpoint throttled this run** (HTTP 429 on 6 of 6 queries despite 4–32 s
spacing and retries). Its id-lookup endpoint worked, so the arXiv leg is **incomplete, not
absent** — re-run `evidence/task-2026-09-09/rerun_search.py` from a network that arXiv does
not rate-limit. Raw export: [`database-export.json`](../evidence/task-2026-09-09/database-export.json)
/ [`.csv`](../evidence/task-2026-09-09/database-export.csv) (499 unique records, every one tagged with the query that produced it).

## Recall check against the day-1 screened set — the finding

Day 1 screened 10 sources, 6 of them resolvable to a database identifier. This run
retrieved **1 of 6**: doi:10.2322/tjsass.60.1.

The one recovered item is the journal DOI; the day-1 set is otherwise publisher PIIs and patents,
which Crossref/OpenAlex return under DOIs that do not carry the PII, and patents are out of reach.
As on the sibling project, native-database ranking and web-index discovery surface different
populations; neither substitutes for the other.

## New candidates — UNSCREENED

[`candidates-unscreened.csv`](../evidence/task-2026-09-09/candidates-unscreened.csv) lists the 25 highest-scoring records not in the
day-1 set, ranked by a **keyword triage** over title and abstract (weights in `rerun_search.py`).
This is a reading order, not a relevance judgement: no candidate has been read against the
day-1 rubric, and none is asserted to be prior art or to be irrelevant. Top five by score:

| # | id | year | title (truncated) | score |
| --- | --- | --- | --- | ---: |
| 1 | [doi:10.1115/gt2020-15403](https://doi.org/10.1115/gt2020-15403) | 2020 | Blade Tip Clearance Measurement Systems for High Speed Turbomachinery Applications and the | 10 |
| 2 | [doi:10.1115/78-gt-164](https://doi.org/10.1115/78-gt-164) | 1978 | Turbine Blade Tip Clearance Measurement Utilizing Borescope Photography | 9 |
| 3 | [doi:10.1115/1.3230742](https://doi.org/10.1115/1.3230742) | 1981 | Laser-Optical Blade Tip Clearance Measurement System | 9 |
| 4 | [doi:10.1115/91-gt-164](https://doi.org/10.1115/91-gt-164) | 1991 | Turbine Blade Tip Clearance Improvement | 9 |
| 5 | [doi:10.1115/2000-gt-0416](https://doi.org/10.1115/2000-gt-0416) | 2000 | Non-Uniform Flow in a Compressor due to Asymmetric Tip Clearance | 9 |


## What this does and does not change

- Adds a dated, reproducible native-database export with per-query provenance. Retained.
- Establishes that the two discovery routes diverge on this topic, so the day-1 web-index set
  cannot be assumed complete and the database set cannot be assumed to contain it.
- Does **not** screen anything, close the novelty gate, touch patents, or read a full text. The
  day-1 "Next" items — close-competitor full texts, native search where *institutional* access
  exists (Scopus/WoS/IEEE Xplore), patent claims with qualified help — all remain open.
- Does not authorise a simulator, fabrication or hardware campaign.

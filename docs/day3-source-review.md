# Day-3 convergence decision — 2026-09-09

**Recommendation: retain the rigid equal-mean-clearance seam comparison as a candidate experiment, but do not yet advertise novelty or deployment yield.** This task adds no mechanism geometry and does not close XC-02.

The [reading rubric](day3-reading-rubric.md) was pushed first at `2c410bc`. [Reading records](day3-reading-records.json) retain exact access scope; no inaccessible paper is labeled fully read.

## Source access and its consequences

[Ryu et al. 2017](https://www.jstage.jst.go.jp/article/tjsass/60/1/60_T-15-38/_pdf/-char/en) is publicly accessible through the publisher's PDF link: no owner institutional login was necessary. The original guessed article path failed. Sections 2.1/3.1, Table 1, the results discussion and conclusions describe a 150 mm counter-rotating fan, uniform front/rear clearance variations and baseline experimental/CFD comparison. They do not establish the planned equal-mean seam experiment. Their shaft-power accounting also differs from electrical thrust-per-power: retain both definitions rather than compare unlike efficiencies. The full-text section read strengthens this boundary for this source only.

The [second-harmonic compressor paper](https://www.sciencedirect.com/science/article/abs/pii/S1270963823007629) remains publisher-indexed-abstract access: a harmonic/nonuniform clearance field is already studied, but detailed equal-mean control definitions remain unresolved. The [segmented flow/noise paper](https://www.mdpi.com/2624-8921/8/7/165) direct open failed; no new full-text conclusion is claimed. These are the most valuable remaining reads, not another broad keyword sweep.

[US5131603A claim 1](https://patents.google.com/patent/US5131603A/en) was accessible and describes movable duct-end sectors for slipstream deflection. This is a longstanding segmentation disclosure, not empirical proof of a tip-clearance seam response or protective guard. Technical overlap reading is not legal clearance; no disclosure decision is inferred.

## Decision and claim boundary

Proposed question: **At fixed mean tip clearance and matched operating conditions, does discrete seam structure explain aerodynamic changes beyond a mean-clearance baseline, with uncertainty that resolves the effect?** Whether the question is distinct from the unresolved sources is still open.

Keep the apparatus independent of deployment mechanisms first. Keep the guard branch separate: absence of rubbing or failure to improve efficiency does not qualify impact protection or containment. Do not add enabling closure details until XC-02 has real approval.

## Reconciled acquisition, not repaired history

[acquisition-ledger.json](../evidence/task-day3-2026-09-09/acquisition-ledger.json) preserves all 499 raw day-2 rows and ten day-1 source entries, with current targeted access records. An explicit publisher-to-DOI alias joins the second-harmonic paper; no fuzzy title matching is used. DOI/arXiv aliases do not prove that different publications are one study.

Fifty raw rows still lack successful query-log support. The earlier export's screening flags are not trusted. Three known DOI matches were already established by the review; that is **not** a valid 3/6 recall estimate. Recall remains null.

Reproduce `python scripts/acquisition_ledger.py --check`, `python -m unittest discover -s tests -q`, and `python scripts/check_repo_contract.py`. Regeneration without `--check` changes only the derived ledger and uses no network. Raw exports remain untouched.

Next: obtain the two unresolved competing treatment definitions and record them using the same reading fields. Then qualify metrology on the actual blade/duct scale before any mechanism or yield campaign. This PR completes bounded preparation, not SSY-01, SSY-02/03, patent clearance or physical validation.

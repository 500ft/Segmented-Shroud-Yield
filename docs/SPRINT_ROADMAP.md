# Segmented-Shroud-Yield — Six-day evidence-integrity sprint

Prepared: 2026-09-05. Budget: 30 focused hours; optional Day 7 adds at most 4 hours for owner review only. Days are effort groupings, not unattended calendar commitments. Status lives only in [SPRINT_TASKS.csv](SPRINT_TASKS.csv).

## A. Outcome and baseline identity

A reproducible design-contract package that rejects invalid specimen metadata and cannot infer guard protection from aerodynamic yield; a bounded, identifiable rigid-defect experiment ready for technical review.

Publication-state update (2026-09-06): the owner authorized local commits, branch
pushes, and pull requests for this sprint. This does not authorize deployment,
research publication, outreach, spending, or any blocked physical/data action.

Audience: engineering/research reviewer and graduate-application portfolio reader.
Canonical sprint checkout: `/Users/redhose/Developer/research-sprints/2026-09-05/Segmented-Shroud-Yield`.
Remote: https://github.com/500ft/Segmented-Shroud-Yield. Base: `971eadb6b778c5fda764894235490dab2ad345e2`.
Branch: `sprint/evidence-integrity-20260905`. Prepared from the unmerged task PR head, not from original dirty drafts.
Original checkout: `/Users/redhose/Segmented-Shroud-Yield`; preserved. New sprint checkout was clean before evidence capture. No commit, push, publication, purchase, deployment or outreach is claimed or planned as an automatic action.

## B. Verified baseline and priority gaps

Verified: specimen checker does not execute nested schema constraints. H4/ROADMAP permit guard classification from aero-mechanical yield while decision-log and SSY-S17 require independent impact/protection evidence. No CAD or measured specimen results exist.

Sources inspected: [scripts/check_repo_contract.py](../scripts/check_repo_contract.py), [protocols/specimen-manifest.schema.json](../protocols/specimen-manifest.schema.json), [tests/test_repo_contract.py](../tests/test_repo_contract.py), [ROADMAP.md](../ROADMAP.md), [docs/research-plan.md](../docs/research-plan.md), [docs/experiment-01-rigid-defect-duct.md](../docs/experiment-01-rigid-defect-duct.md), [docs/TASKS.md](../docs/TASKS.md).
[Actual baseline command outputs](../evidence/sprint-2026-09-05/baseline.json) record working directories, runtime versions, outputs and exit statuses. Alleged defects become reproduced failures only when the red tests record them. Test counts are not research performance.

Verified existing commands (repository root; local Python may need the recorded readline workaround):

```sh
python -m unittest discover -s tests -v
python scripts/check_repo_contract.py
```

No separately configured typechecker/linter was found in this scoped configuration. Use compileall for changed Python, relevant tests, existing CI commands and `git diff --check`; do not call syntax compilation a typecheck. Proposed test/CLI paths below do not exist until implemented.

## C. Scope, ownership and critical path

Must-haves: repaired claim/validation boundary; regression evidence including original failures; consistent operative scope; reproducible local delivery/check commands; review index identifying unresolved external work.
Exclusions: No rotor operation, blade containment claim, CAD fabrication, deployable mechanism build, acoustic study, or declaration of novelty.
Owner/External dependencies: Rotor/stand selection, metrology access, fabrication and facility safety authority. No specimens are available in the baseline. Branch includes unmerged PR work.
Critical path: baseline → regression failure → minimal correction → full affected checks → candidate identity/selection freeze → bounded evaluation → review packet. Prepare owner requests on Day1; replies do not block independent code fixes. External feedback is not presumed.

## D. Daily budget

September6 reconciliation: owner resource/reference actions start on Day1 rather
than after the evaluation packet. This moves two estimated hours forward; total
remains30. External turnaround is not compressed by this workload allocation.

| Day | Hours | Primary deliverable |
|---|---:|---|
| 1 | 7 | Baseline/scope (5 Agent hours), early resource/provenance action (2 Owner hours) |
| 2 | 5 | Enforce specimen JSON Schema |
| 3 | 6 | Separate guard qualification and define identifiable holdout |
| 4 | 4 | Package reviewed protocol and fixture interface |
| 5 | 6 | Evaluate unseen metadata and design counterexamples |
| 6 | 2 | Review packet; external feedback remains conditional |
| Total | 30 | Local evidence-ready candidate or explicitly partial handoff |

## E. Ordered tasks and done conditions

### SSY-S01 — Day 1: Capture baseline and reproduce audit hypotheses

Priority: P0 · Owner: Agent · Focused hours: 3 · Depends on: none.
Files: scripts/check_repo_contract.py; protocols/specimen-manifest.schema.json; tests/test_repo_contract.py; ROADMAP.md; docs/research-plan.md; docs/experiment-01-rigid-defect-duct.md; docs/TASKS.md.
Deliverable / Done when: Record base identity, clean sprint start, versions, exact CI commands and observed outputs; preserve original worktree changes.
Verification: python -m unittest discover -s tests -v
python scripts/check_repo_contract.py
Evidence to retain: evidence/sprint-2026-09-05/baseline.json.

### SSY-S02 — Day 1: Freeze scope and evidence-first execution design

Priority: P0 · Owner: Agent · Focused hours: 2 · Depends on: SSY-S01.
Files: NEW docs/SPRINT_ROADMAP.md; NEW docs/SPRINT_TASKS.csv; NEW docs/SPRINT_PROGRESS.md; NEW docs/REVIEW_READY.md.
Deliverable / Done when: Six-day30h plan saved, requirements testable, user-provided plan-and-execute authorization recorded, external authority excluded.
Verification: Review this roadmap and parse task CSV; hours sum to30.
Evidence to retain: docs/SPRINT_ROADMAP.md.

### SSY-S03 — Day 2: Enforce specimen JSON Schema

Priority: P0 · Owner: Agent · Focused hours: 5 · Depends on: SSY-S02.
Files: scripts/check_repo_contract.py; tests/test_repo_contract.py; .github/workflows/ci.yml; README.md; NEW requirements.txt.
Deliverable / Done when: Negative deployment cycles/clearance and invalid nested fields rejected; valid planned fixture accepted; schema validation not just top-level keys; CI installs declared dependency.
Verification: python -m unittest discover -s tests -v; python scripts/check_repo_contract.py
Evidence to retain: command, inputs, outputs and exit status under evidence/sprint-2026-09-05/; link from task ledger.

### SSY-S04 — Day 3: Separate guard qualification and define identifiable holdout

Priority: P0 · Owner: Agent · Focused hours: 6 · Depends on: SSY-S03.
Files: docs/research-plan.md; ROADMAP.md; docs/TASKS.md; docs/experiment-01-rigid-defect-duct.md; README.md.
Deliverable / Done when: Duct and protective performance have separate evidence paths; absent aero benefit cannot imply guard success; holdout model must have training support or explicitly specified physical extrapolation.
Verification: python scripts/check_repo_contract.py; review H4, yield definition, roadmap and SSY-S17 together.
Evidence to retain: command, inputs, outputs and exit status under evidence/sprint-2026-09-05/; link from task ledger.

### SSY-S05 — Day 4: Package reviewed protocol and fixture interface

Priority: P1 · Owner: Agent · Focused hours: 4 · Depends on: SSY-S04.
Files: protocols/specimen-manifest.schema.json; NEW evidence/sprint-2026-09-05/candidate.json; docs/REVIEW_READY.md.
Deliverable / Done when: Dependency install and validator run from consumer context; dynamic clearance, independent specimens and matched thrust remain requirements; no CAD/rig completion claim.
Verification: python -m pip install -r requirements.txt; python scripts/check_repo_contract.py; git diff --check
Evidence to retain: command, inputs, outputs and exit status under evidence/sprint-2026-09-05/; link from task ledger.

### SSY-S06 — Day 5: Evaluate unseen metadata and design counterexamples

Priority: P1 · Owner: Agent · Focused hours: 6 · Depends on: SSY-S05.
Files: NEW evidence/sprint-2026-09-05/evaluation-plan.md; NEW evidence/sprint-2026-09-05/evaluation.json; tests/test_repo_contract.py.
Deliverable / Done when: Freeze cases before output; include valid null planned measurements, invalid numerical inputs and absent training-descriptor support; retain expected outcomes; no experiment substituted by fixtures.
Verification: python -m unittest discover -s tests -v; manual review of registered model support and classification paths.
Evidence to retain: command, inputs, outputs and exit status under evidence/sprint-2026-09-05/; link from task ledger.

### SSY-S07 — Day 6: Assemble review packet and CAD work order

Priority: P1 · Owner: Agent · Focused hours: 2 · Depends on: SSY-S06.
Files: docs/REVIEW_READY.md; docs/SPRINT_PROGRESS.md; docs/SPRINT_TASKS.csv.
Deliverable / Done when: Next CAD treatment and metrology decisions explicit; all achieved deliverables source-linked, hardware and novelty unresolved.
Verification: python scripts/check_repo_contract.py; python -m unittest discover -s tests -v; git diff --check
Evidence to retain: command, inputs, outputs and exit status under evidence/sprint-2026-09-05/; link from task ledger.

### SSY-S08 — Day 1: Owner reviews rotor/stand and measurement access

Priority: P0 · Owner: Owner · Focused hours: 2 · Depends on: SSY-S02.
Files: docs/experiment-01-rigid-defect-duct.md; docs/TASKS.md.
Deliverable / Done when: Select resource-feasible rigid-defect scale with qualified operator; no experiment begins before facility approval and measurement qualification.
Verification: Owner documents available rotor/containment/instruments or explicitly keeps project at design-only floor.
Evidence to retain: command, inputs, outputs and exit status under evidence/sprint-2026-09-05/; link from task ledger.


## F. Evaluation and overrun policy

Existing audit counterexamples and all tests inspected while fixing are development evidence, not held-out evaluation. Before Day5, freeze a candidate source/diff identity and selection procedure; save expected judgments before predictions where meaningful. Any observed case used to fix the candidate becomes development material; record that and select new cases for a revised candidate. Hashes identify bytes, not independence. No AI peer is called an independent human reviewer.

If the implementation consumes extra time, cut optional model breadth, cosmetic changes and additional fixtures; never relax numerical thresholds, remove rejection checks or relabel missing measurements. Day7 may add up to4 owner-review hours (34 maximum) only by explicit rebaseline. Do not convert lab lead time into nominal coding hours. Stop affected work at missing authority; proceed with independent authorized tasks. Unavailable external evidence produces a partial handoff, not a completed empirical claim.

Follow-up review checks: reproduce original failures and repaired counterexamples, repeat real commands, inspect runtime and evidence provenance, distinguish local tests from hosted/deployed/physical outcomes, and assess scientific wording independently.

## G. Execution record and first action

[Ledger](SPRINT_TASKS.csv) · [Progress](SPRINT_PROGRESS.md) · [Review index](REVIEW_READY.md).
First behavior-changing action: SSY-S03; write its regression input, observe failure on baseline, then make the minimal correction. User has authorized plan-and-execute now. No additional start confirmation is required for this bounded scope.

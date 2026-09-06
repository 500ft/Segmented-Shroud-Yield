# Segmented-Shroud-Yield — individual CAD tasks

Prepared 2026-09-06. **Planning only: no CAD model, drawing, fabrication, calibration or physical result was produced by this amendment.**

[CAD_TASKS.csv](CAD_TASKS.csv) is the sole status ledger for this new CAD phase. The earlier [SPRINT_TASKS.csv](SPRINT_TASKS.csv) remains the authority for the separate 30-hour evidence-integrity sprint; its estimates and achieved software evidence are unchanged. This plan expands mechanical work orders, not publication or test permission. Scope tiers are in [scope.md](specs/cad-development/scope.md).

## Verified reason for the work

SSY-04 already requests CAD as one large item. It needs separate reference, defect, metrology and release tasks; expensive closure mechanisms must stay behind Experiment 01 rather than being modeled first.

Inspected source documents:

- [docs/TASKS.md](TASKS.md)
- [docs/experiment-01-rigid-defect-duct.md](experiment-01-rigid-defect-duct.md)
- [docs/research-plan.md](research-plan.md)

## Outcome and boundaries

A reviewer can reopen editable, version-pinned geometry; regenerate neutral STEP exports; understand the assembly, critical fits and measurement datums; and distinguish design assumptions from inspected hardware. STL is only a manufacturing derivative where appropriate, not the sole editable master. For hosted CAD retain a version-specific share reference and authorized portable source/export archive; record tool/version and export settings. Do not require a particular commercial tool before checking access.

**Entry decision:** SSY-01/02/03 close the exact-gap, uncertainty and geometry decisions. Nominal desk CAD can use sourced design geometry; fabrication additionally needs actual rotor/stand, containment and instrument interfaces. Mechanisms require the separate confirmed Experiment 01 continuation gate.

**Excluded:** No spinning rotor, fabricated specimen, CFD/FEA result or protective-guard classification. Three-lobe/combined defects are not silently added to the first three-condition pilot; they require a registered scope decision.

Agent owns document preparation and modeling once inputs exist; Owner owns actual component/access choices and review authority; External fabricators/operators own quotes, manufacture and facility approval. No approval, purchase, fabrication booking, IP disclosure of third-party drawings, or test run is completed by checking in this plan. Unknown critical dimensions block fabrication; conceptual placeholders must be visible and cannot become as-built evidence.

## Focused-hour allocation

The initial CAD phase is **23 estimated focused hours**, additional to the earlier software sprint. A further **11 hours** is deferred behind explicit triggers. These are estimates, not recorded work. Each day is a workload bucket after its prerequisites, not a calendar promise; quotes, calibration and facility lead times are not compressed into CAD hours.

| Workload day | Hours | Ordered tasks |
| --- | ---: | --- |
| 1 | 4 | SSY-CAD-01 → SSY-CAD-02 |
| 2 | 4 | SSY-CAD-03 |
| 3 | 4 | SSY-CAD-04 |
| 4 | 4 | SSY-CAD-05 |
| 5 | 4 | SSY-CAD-06 |
| 6 | 3 | SSY-CAD-07 |

Critical path follows the explicit task dependencies below: input register → owner decisions → parts/fixtures → release review. Independent branches may proceed after their shared inputs close. Nominal design-only release remains possible without fabricated hardware.

## Individual work orders

All output paths below are **proposed NEW deliverables**, not existing artifacts. Current task state appears only in the CSV; the headings below define acceptance, not completion.

### SSY-CAD-01 — Translate SSY-03 into a CAD parameter and defect contract

- Owner: Agent; priority: P1; estimate: 2 h; workload day: 1.
- Dependencies: none; source inspection is available now.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/shroud/parameters.csv; cad/shroud/design-inputs.md`.
- Done when: Draft rotor frame, duct profile, uniform/two-lobe/seam/radial-step definitions, equal-mean convention and source status. Released parameter values depend on completion of SSY-01/02/03; do not invent those decisions.
- Verification and evidence to retain: Review mappings to SSY-03 and matched-thrust protocol; list undecided amplitudes, tolerances and metrology resolution explicitly.

### SSY-CAD-02 — Approve reference geometry and design/fabrication input split

- Owner: Owner; priority: P1; estimate: 2 h; workload day: 1.
- Dependencies: SSY-CAD-01.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/shroud/owner-inputs.md`.
- Done when: Confirm SSY-01/02/03 decisions and a sourced nominal rotor/reference profile for desk CAD. Separately record actual stand, probe and qualified containment access as available or pending; missing hardware does not prevent a clearly nominal design-only floor.
- Verification and evidence to retain: Sign parameter contract and identify which interfaces are provisional; no fabrication release from assumed stand dimensions.

### SSY-CAD-03 — Model open-rotor carrier and continuous reference duct

- Owner: Agent; priority: P1; estimate: 4 h; workload day: 2.
- Dependencies: SSY-CAD-02.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/shroud/reference/ (source, STEP, datums)`.
- Done when: Use shared rotor-axis/stand datums and nominal profile; model monolithic reference plus removable open-rotor configuration without silently changing support blockage. Register static clearance, inlet arrangement and surface finish assumptions.
- Verification and evidence to retain: Check symmetry, mounting repeatability, inlet/support obstruction and section dimensions; retain source-generated nominal gap samples.

### SSY-CAD-04 — Model uniform-clearance and two-lobe inserts

- Owner: Agent; priority: P1; estimate: 4 h; workload day: 3.
- Dependencies: SSY-CAD-03.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/shroud/inserts/harmonics/ (source, STEP, parameter cases)`.
- Done when: Parameterize interchangeable uniform and two-lobe treatments at the registered equal mean; isolate amplitude from mounting changes. Reject intersecting rotor envelopes and record minimum static clearance independently of mean.
- Verification and evidence to retain: Regenerate each registered case; sample clearance around the full circumference and compare mean/harmonic amplitude against the contract, including zero-amplitude equivalence.

### SSY-CAD-05 — Model discrete seam and radial-step insert families

- Owner: Agent; priority: P1; estimate: 4 h; workload day: 4.
- Dependencies: SSY-CAD-03.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/shroud/inserts/discrete/ (source, STEP, detail drawings)`.
- Done when: Define seam width/depth and local radial steps with explicit averaging convention, seam endpoint treatment and unchanged reference datums. Seam belongs to the pilot; step fabrication/testing requires its registered extension. A missing wall cannot be assigned a fictitious finite radial clearance.
- Verification and evidence to retain: Check limiting zero-defect cases, domain of clearance sampling and equal-mean calculation; retain descriptor/geometry correspondence and separate undefined seam samples.

### SSY-CAD-06 — Model exchange, alignment and clearance-metrology interfaces

- Owner: Agent; priority: P1; estimate: 4 h; workload day: 5.
- Dependencies: SSY-CAD-02, SSY-CAD-03, SSY-CAD-04, SSY-CAD-05.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/shroud/stand-interface/ (source, STEP, probe-access drawings)`.
- Done when: Design indexing/retention, rotor-axis alignment and dynamic-clearance probe/camera access around actual or explicitly nominal instruments. Keep the experimental duct distinct from qualified blade containment; external shielding must not bias inlet flow unnoticed.
- Verification and evidence to retain: Review repeatability stack-up, sensor line of sight, installation/removal and inlet obstruction. Pending actual hardware blocks fabrication, not nominal floor CAD.

### SSY-CAD-07 — Release the rigid-defect inspection and CAD evidence pack

- Owner: Agent; priority: P1; estimate: 3 h; workload day: 6.
- Dependencies: SSY-CAD-04, SSY-CAD-05, SSY-CAD-06.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/shroud/release/ (BOM, drawings, export/descriptor manifest, inspection sheets)`.
- Done when: Deliver native/source version, STEP, defect parameters, toleranced datums, comparable cross-section/exploded views and individual specimen inspection points. Split nominal design review from fabrication release; reconcile SSY-04 acceptance without claiming SSY-06 research floor complete.
- Verification and evidence to retain: Reopen all exports, compare profile/clearance descriptors and check units/part IDs. Retain hashes and review findings; data collection requires qualified measurement system and facility approval.

### SSY-CAD-08 — Model ordinary over-center closure comparator

- Owner: Agent; priority: P2; estimate: 5 h; workload day: conditional.
- Dependencies: SSY-CAD-07.
- Scope: trigger-gated extension; not required for initial CAD release.
- Proposed deliverables: `cad/shroud/closures/over-center/ (source, STEP, assembly)`.
- Done when: Only after separate confirmed Experiment 01 continuation and approved mechanism requirements: detail joints, hard stops and ordinary over-center latch within fixed nominal geometry and ring-mass budget.
- Verification and evidence to retain: Check deployment sweep, tolerance/clearance and latch load paths; retain geometry and mass basis for a fair comparator.

### SSY-CAD-09 — Model self-centering preload-controlled closure

- Owner: Agent; priority: P2; estimate: 6 h; workload day: conditional.
- Dependencies: SSY-CAD-08.
- Scope: trigger-gated extension; not required for initial CAD release.
- Proposed deliverables: `cad/shroud/closures/preload-controlled/ (source, STEP, assembly)`.
- Done when: Same continuation gate; detail locating features, preload adjustment and replaceable wear interfaces. Match comparator nominal geometry/ring mass or report residual differences; do not infer energy barrier or shock resistance from a render.
- Verification and evidence to retain: Review kinematics and tolerance propagation to seams/ovality; define measurement datums for preload, reconstruction variance and later stiffness/release tests.

## Release review and overrun rule

Every release includes an assembly/exploded view, a critical section/detail view and a measurement/inspection setup view. Captions identify the question illustrated, source revision, dimensions/units and **CAD prediction—not measured** state; cite vendor/hand-calculation references actually used. Render quality is not evidence of fit or performance.

Before marking a CAD task done, attach real source/export identities, regeneration instructions and the corresponding acceptance evidence in CAD_TASKS.csv. A second AI pass is a development check, not independent human or laboratory validation. Retain failed fits and unresolved assumptions; do not silently tune experimental geometry after observing confirmation data.

If the phase overruns, postpone decorative renders, optional variants and mechanism extensions first. Do not remove required fits, safety interfaces, reference controls, source traceability or measurement access. Fabrication-release review, apparatus commissioning and physical evaluation remain separate future actions; updated geometry may require a new prospective analysis/reference freeze. Preparing drawings does not close an existing physical-readiness or publication blocker.

## PR review scope

This amendment changes task planning and navigation only. It is stacked on the open evidence-integrity PR so its diff excludes earlier fixes. No software behavior or frozen scientific threshold is changed. Review task dependencies and claim boundaries now; actual CAD acceptance is assessed when those artifacts exist.

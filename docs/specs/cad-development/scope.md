# Segmented-Shroud-Yield — CAD adaptive scope

Date: 2026-09-06. Task definitions: [CAD_PLAN.md](../../CAD_PLAN.md); authoritative CAD state: [CAD_TASKS.csv](../../CAD_TASKS.csv).

## Must-have for the initial CAD deliverable

- SSY-CAD-01: Translate SSY-03 into a CAD parameter and defect contract.
- SSY-CAD-02: Approve reference geometry and design/fabrication input split.
- SSY-CAD-03: Model open-rotor carrier and continuous reference duct.
- SSY-CAD-04: Model uniform-clearance and two-lobe inserts.
- SSY-CAD-05: Model discrete seam and radial-step insert families.
- SSY-CAD-06: Model exchange, alignment and clearance-metrology interfaces.
- SSY-CAD-07: Release the rigid-defect inspection and CAD evidence pack.

“Must-have” applies only to this CAD package, not every paper or software milestone. Entry decision: SSY-01/02/03 close the exact-gap, uncertainty and geometry decisions. Nominal desk CAD can use sourced design geometry; fabrication additionally needs actual rotor/stand, containment and instrument interfaces. Mechanisms require the separate confirmed Experiment 01 continuation gate.

## Nice-to-have after the package

- Additional presentation renders or animation, only after source/STEP/drawing reproduction succeeds; they add explanation, not test evidence.

## Maybe-later

- SSY-CAD-08: Model ordinary over-center closure comparator. Trigger and acceptance: Only after separate confirmed Experiment 01 continuation and approved mechanism requirements: detail joints, hard stops and ordinary over-center latch within fixed nominal geometry and ring-mass budget. Why wait: avoid detailed hardware work before its scientific and resource gate closes.
- SSY-CAD-09: Model self-centering preload-controlled closure. Trigger and acceptance: Same continuation gate; detail locating features, preload adjustment and replaceable wear interfaces. Match comparator nominal geometry/ring mass or report residual differences; do not infer energy barrier or shock resistance from a render. Why wait: avoid detailed hardware work before its scientific and resource gate closes.

## Out

- No spinning rotor, fabricated specimen, CFD/FEA result or protective-guard classification. Three-lobe/combined defects are not silently added to the first three-condition pilot; they require a registered scope decision.

## Milestone watch

- Check owner-input records before moving from a parameterized concept to released fits.
- Check the CAD_TASKS.csv predecessor IDs and linked acceptance evidence before starting dependent geometry.
- Check source/export regeneration and inspection drawings before a fabrication-review decision.
- Check qualified apparatus/measurement approval separately before any physical claim or energized run.

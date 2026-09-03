# Data and Figure Contract

## Current state

There are no CAD, FEA, CFD, or measured results in this repository. The only image is an authored conceptual method diagram.

## Planned data stages

```text
data/raw/<study>/<specimen-id>/<run-id>/
data/processed/<study>/<analysis-version>/
results/generated/<study>/<analysis-version>/
```

Raw measurements remain immutable. Processed tables identify their source runs, code commit, units, calibration version, and transformation command.

## Required experimental metadata

- Study, specimen, deployment-cycle, and run identifiers
- Evidence state
- Material, manufacturing process, and geometry revision
- Closure mechanism and preload setting
- Circumferential defect description and measurement method
- Rotor, motor, controller, and operating point
- Instrument models and calibration identifiers
- Test order, temperature, and environmental condition
- Abort, rubbing, or anomalous event flags
- Analysis commit and output generator

## Figure rules

Every future figure must state:

1. The claim it supports
2. Evidence state
3. Independent sample unit and repeated-measure structure
4. Test conditions and units
5. Input artifacts and calibration
6. Generator command and commit
7. Uncertainty representation

Color is never the only semantic channel. Reference conditions use solid lines; modeled predictions use dashed lines; measured samples use markers; safety boundaries are directly labeled.

## Current figure manifest

| ID | Artifact | Claim | Evidence state |
| --- | --- | --- | --- |
| SSY-00 | [`assets/segmented-shroud-overview.svg`](../assets/segmented-shroud-overview.svg) | Explains the proposed causal chain only | Planned / conceptual |

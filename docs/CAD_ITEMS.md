# Segmented Shroud Yield — CAD item list

Prepared 2026-09-06 (America/New_York). **A list of planned parts and assemblies—not completed CAD, hardware or approval to fabricate/test.**

All items remain parked until SSY-01/02/03 and the XC-02 disclosure decision close. This list repeats already-public component categories only; it adds no enabling geometry or mechanism detail.

## How to use this list

This is a parts inventory, not another task-status ledger or additional scope/budget. Each row maps to the [work-order definitions](CAD_PLAN.md) and [sole task ledger](CAD_TASKS.csv); several parts can belong to one work order. Bought parts and existing models should be reused/imported when authorized, not redesigned merely to fill a CAD folder. One part may serve multiple listed interfaces; avoid duplicating it.

## Conditional first package: rigid comparison specimens

| Item to model or import | Existing work order | Purpose / boundary |
| --- | --- | --- |
| Open-rotor carrier / reference mounting interface | `SSY-CAD-03` | Provide the common nominal reference interface; detailed dimensions remain subject to the input/disclosure gates. |
| Continuous reference duct | `SSY-CAD-03` | Represent the monolithic comparison condition. |
| Uniform-clearance insert | `SSY-CAD-04` | Represent the registered uniform comparison condition. |
| Two-lobe insert | `SSY-CAD-04` | Represent the registered distorted comparison condition. |
| Seam-condition insert | `SSY-CAD-05` | Represent the seam comparison already specified in Experiment 01. |
| Insert exchange, alignment and retention interfaces | `SSY-CAD-06` | Support repeatable specimen placement; no new mechanism detail is specified here. |
| Dynamic-clearance probe/camera mounting interface | `SSY-CAD-06` | Reserve metrology access around the approved instrument, separate from qualified blade containment. |
| Complete rigid-specimen / stand-interface assembly | `SSY-CAD-07` | Provide the nominal assembly and inspection views once the gated design is available. |

## Extension requiring its registered scope decision

| Item to model or import | Existing work order | Purpose / boundary |
| --- | --- | --- |
| Radial-step insert | `SSY-CAD-05` | A later comparison family; do not silently add it to the first three-condition pilot. |

## Withheld

| Item to model or import | Existing work order | Purpose / boundary |
| --- | --- | --- |
| SSY-CAD-08 | `SSY-CAD-08` | Details withheld pending XC-02. |
| SSY-CAD-09 | `SSY-CAD-09` | Details withheld pending XC-02. |

## What to deliver for each applicable part or assembly

- Editable/source CAD or an authorized immutable CAD-document version; identify reused vendor geometry and its source.
- STEP export, with dimensions/units checked after reimport. Parameter-driven families also need the planned numerical geometry tests before model acceptance.
- A dimensioned drawing for custom fabricated parts, with material/process, critical fits and inspection datums; vendor hardware can use its sourced drawing.
- An assembly/section view showing how the part fits and which problem it addresses. Label all visuals CAD/design-only until corresponding evidence exists.

Neither a rigid duct CAD model nor a nominal assembly establishes aerodynamic benefit or protective-guard performance. Prior public commits remain accessible; this list does not undo disclosure.

## Policy and scope

The owner authorized merging this inventory and the current PR documents to main on 2026-09-06 (America/New_York). No withheld details are restored, no model task is marked done and no hardware/fabrication/disclosure gate is closed by this placement decision.

# Segmented Shroud Aeromechanics

A measurement-first study of how seams, distortion, and reconstruction error affect rotor-shroud performance.

[![Repository checks](https://github.com/500ft/segmented-shroud-aeromechanics/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/500ft/segmented-shroud-aeromechanics/actions/workflows/ci.yml)
![Evidence: research design, not validated](https://img.shields.io/badge/evidence-research_design%2C_not_validated-415a77)
[![License: MIT](https://img.shields.io/badge/license-MIT-276c6b)](LICENSE)

[Overview](#the-problem) · [Evidence](#evidence-snapshot) · [Quick start](#quick-start) · [First experiment](#first-experiment) · [Reviewer guide](docs/START_HERE.md)

![Conceptual study sequence from controlled rigid-duct defects and qualified measurements to a held-out comparison, before conditional mechanism and yield studies](docs/media/project-overview.svg)

*Proposed study architecture—not fabricated geometry or measured performance. No shroud specimen, aerodynamic measurement, or rubbing test has been completed for this repository.*

## The problem

A segmented rotor shroud must reconstruct useful aerodynamic geometry, not simply close into a ring. Seams, local steps, and distortion can change the clearance around the blade tips. An acceptable average gap may conceal a local contact risk or a loss of aerodynamic benefit.

This project asks whether **defect geometry adds predictive information beyond average clearance**. The first comparison uses controlled rigid ducts, keeping deployment mechanics out of the apparatus until the aerodynamic premise is supported.

Neither tip-clearance sensitivity nor generic segmented mechanisms are claimed as new. The [targeted source review](docs/day3-source-review.md) narrows the candidate question to an equal-mean-clearance seam comparison and identifies competing work that still needs resolution.

## Proposed approach

1. **Qualify the measurements.** Calibrate thrust, electrical power, and clearance; establish uncertainty and stand drift.
2. **Isolate geometric defects.** Compare uniform, two-lobe, and discrete-seam conditions at equal mean clearance, with open-rotor and monolithic references.
3. **Compare at matched thrust.** Measure electrical power and dynamic minimum clearance; retain RPM, temperature, vibration, and any contact events.
4. **Test predictive value.** Compare a defect-aware model with a mean-clearance baseline using a supported, predeclared holdout.
5. **Expand only if justified.** Mechanism repeatability and aero-mechanical yield are later studies, subject to separate research, metrology, and disclosure gates.

The eventual yield question combines deployment/lock success, sufficient dynamic clearance, and retained aerodynamic benefit. That is a **proposed component-level metric**, not an estimated reliability value. Protection against impact or debris requires an independent guard evaluation.

## Evidence snapshot

The executable deliverable today is research-integrity tooling, not a rotor model or hardware demonstration.

| Available artifact | What it establishes | Inspect it |
| --- | --- | --- |
| Specimen schema and negative tests | Required run metadata and invalid-input rejection | [Schema](protocols/specimen-manifest.schema.json), [tests](tests/) |
| Source-review rubric and reading records | Access scope and evidence for a narrowed candidate experiment | [Rubric](docs/day3-reading-rubric.md), [source review](docs/day3-source-review.md) |
| Reproducible acquisition ledger | Preserved routes, identifiers, access scope, and explicit provenance gaps | [Ledger](evidence/task-day3-2026-09-09/acquisition-ledger.json), [generator](scripts/acquisition_ledger.py) |
| Measurement-first experiment contract | Controls, comparison basis, identifiability, and stop conditions | [Experiment 01](docs/experiment-01-rigid-defect-duct.md) |
| Recorded software checks | Documentation/schema/provenance checks—not aerodynamic validation | [Verification record](evidence/task-day3-2026-09-09/README.md) |

The 2026-09-09 reconciliation retains **499 raw database rows**, with **50 lacking successful query-log support**. These are acquisition records, not 499 reviewed studies. Recall remains unavailable. The public JSASS PDF was accessed, but two competing treatments and the full novelty closeout remain unresolved; see the [source review](docs/day3-source-review.md).

## Quick start

Use **Python 3.11**, matching [CI](.github/workflows/ci.yml), and Git. The only declared dependency is pinned in [requirements.txt](requirements.txt). No CAD license, CFD solver, instrument connection, or rotor hardware is needed for these checks.

```bash
git clone https://github.com/500ft/segmented-shroud-aeromechanics.git
cd segmented-shroud-aeromechanics
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check_repo_contract.py
python scripts/acquisition_ledger.py --check
python -m unittest discover -s tests -v
```

On Windows, activate with `.venv\Scripts\Activate.ps1` in PowerShell instead of `source`.

Expected: the repository contract passes, the committed ledger is consistent, and the test suite ends with `OK`. Passing checks do not establish aerodynamic benefit, close the source-review gate, or authorize fabrication.

To rebuild **only the derived literature ledger** from committed inputs:

```bash
python scripts/acquisition_ledger.py
git diff -- evidence/task-day3-2026-09-09/acquisition-ledger.json
```

This operation is offline. Unchanged inputs should produce no diff. It does not retrieve papers, generate CAD, or calculate shroud performance.

## First experiment

The first study is an **adjustable rigid-defect duct on a contained rotor stand**. It intentionally excludes deployment mechanisms. Before collecting hypothesis-test data, the measurement uncertainty must be small enough to resolve the registered effect of interest.

The primary comparison is electrical power required at **matched thrust**. A shaft-power result from prior literature is not interchangeable with electrical efficiency, and an RPM-matched comparison is only a secondary diagnostic.

The [full protocol](docs/experiment-01-rigid-defect-duct.md) owns the provisional continuation and pivot gates. A held-out defect family also needs identifiable model descriptors or an explicitly specified extrapolation model. If additional defect descriptors do not help, report the simpler tolerance finding; do not infer protective-guard performance.

[First-experiment details](docs/START_HERE.md#first-experiment-decision) · [Gate-driven roadmap](ROADMAP.md) · [Research tasks](docs/TASKS.md)

## Evidence and safety limits

- No CAD, FEA, CFD, fabricated duct, deployable shroud, or measured performance result is included.
- No aerodynamic benefit, aero-mechanical yield, strike-safety, or protective-guard capability is demonstrated.
- A complete specimen manifest does not authenticate measurements or release a design for manufacture.
- Rotor testing requires qualified containment, remote arming/shutdown, current protection, verified clearance, low-energy commissioning, a site-specific risk assessment, and facility approval.
- [XC-02 and the public-disclosure boundary](CONTRIBUTING.md#public-disclosure-boundary) remain open. Implementation-sensitive mechanism details are withheld; access to patent text is not legal clearance.

## Documentation routes

| If you want to… | Start here |
| --- | --- |
| Understand the project in five minutes | [Reviewer guide](docs/START_HERE.md) |
| Challenge the proposed contribution | [Current source review](docs/day3-source-review.md), then [prior-art boundary](docs/prior-art.md) |
| Inspect variables and statistical claims | [Research plan](docs/research-plan.md) and [claim ledger](docs/claim-ledger.md) |
| Assess measurement feasibility | [Experiment 01](docs/experiment-01-rigid-defect-duct.md) |
| Trace work and alternative outcomes | [Review index](docs/REVIEW_READY.md), [dependency audit](docs/research-dependency-audit.md), [decision log](docs/decision-log.md) |

## Contributing and license

Reproduction reports, precise source corrections, and metrology critiques are welcome. Include the commit, command or source locator, expected behavior, and observed result. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a [pull request or issue](https://github.com/500ft/segmented-shroud-aeromechanics/issues).

Repository software is [MIT licensed](LICENSE); third-party publications retain their original licenses. This is a research repository, not a qualified rotor enclosure or fabrication package.

[Repository identity and presentation references](docs/REPOSITORY_IDENTITY.md)

# SSY-01 source and metrology review, first pass — 2026-09-08

## Question and decision

Has an experiment at small-UAV scale isolated equal-mean-clearance seam/step/
harmonic defects, measured dynamic clearance, and predicted aerodynamic outcomes
of repeated deployment on genuinely held-out specimens or mechanisms?

**Prior art found** for mean clearance, nonuniform clearance, segmented ducts and
dynamic tip sensing. **Supported candidate gap within this bounded search:**
an experimentally qualified, equal-mean-clearance rigid-defect comparison with
explicit measurement uncertainty and honest transfer tests. Repeated-deployment
yield is a later candidate extension, not a first-experiment deliverable.

SSY-D01 completes today's first-pass source/metrology shortlist within SSY-01.
The complete novelty gate remains open: abstract-only and inaccessible full texts
are listed below; native database and detailed patent claim review were not
completed. No geometry, closure-mechanism detail, manufacturing method, rotor
operation or XC-02 disclosure authorization is added by this review.

## Search record and eligibility

Date: 2026-09-08. English web-index retrieval; no lower date cutoff. Searched
publisher/arXiv/NASA records and Google Patents through the web index, then opened
primary pages where available. This is not a Scopus/Web of Science or Espacenet
export and cannot support a systematic-review recall claim.

Executed search strings:

1. `ducted fan equal mean tip clearance ovality seam segmented experimental`
2. `"ducted fan" "non-uniform" "clearance" experimental`
3. `"ducted fan" "non-uniform tip clearance" experiment`
4. `"tip clearance" optical capacitive polymer blades measurement ducted fan`
5. `"tip clearance" "optical" "Sensors" fibre intensity turbine`
6. `site.patents.google.com folding duct segmented shroud rotor`
7. `site.patents.google.com "foldable" "duct" propeller`
8. `site.patents.google.com "foldable duct"`
9. `"10.1016/j.ast.2023.108866"`
10. `"segmented" "duct" "165" "2026" acoustics`
11. `site.sciencedirect.com "Impact of non-axisymmetric tip clearance"`

Include equal/nonuniform clearance studies, segmented fan discontinuities,
rotating tip-clearance instrumentation and rotor-shroud disclosures. Turbine/
compressor work is relevant mechanism/metrology evidence but not proof of transfer
to a small polymer propeller. Exclude HVAC ducts, wind-energy economics, generic
folding wings, market reports and unsupported forum assertions from core evidence.
Record those exclusions rather than counting keyword hits as competitors.

Aboutness: 3 tests the target combination; 2 relevant ingredient; 1 background;
0 excluded. Grade B: controlled experiment or experimentally checked simulation;
C: simulation; D: conceptual argument. Abstract-only grades are provisional.
Patents are disclosures, not experimental proof; official records are identified
as such. Sources are ordered by experimental relevance, not citation count.

## Evidence table (10 selected entries)

| ID / primary source | Aboutness; evidence/access | Consequence |
| --- | --- | --- |
| S1 [Ryu et al., 2017](https://doi.org/10.2322/tjsass.60.1) | 2; provisional B; publisher-indexed abstract, direct page retrieval failed | Counter-rotating UAV fan study combines CFD and wind-tunnel comparison. Mean-clearance sensitivity is established, but this does not establish seam/deployment transfer. |
| S2 [Second-harmonic clearance distributions, 2024](https://www.sciencedirect.com/science/article/abs/pii/S1270963823007629) | 2; provisional B/C; publisher-indexed abstract, full text unavailable | Full-annulus compressor simulations compare casing ovalization and blade-height variation, with measurements for the latter. A harmonic field is not itself new. Do not generalize all cases as experimentally validated. |
| S3 [Nonuniform clearance layouts, 2026](https://www.sciencedirect.com/science/article/pii/S1270963826003159) | 2; C provisional; publisher-indexed description, direct retrieval failed | A further numerical compressor-layout study is an unresolved close competitor; inspect its treatment definitions before claiming equal-mean isolation is new. |
| S4 [Segmented ducted fan flow/noise, 2026](https://www.mdpi.com/2624-8921/8/7/165) | 2; C; publisher-indexed abstract/conclusions, direct fetch rate-limited | Segmentation changes flow and acoustic predictions in a small-UAV study. Its stated time-averaged limitation does not establish a measured dynamic-clearance or deployment-yield result. Keep acoustics out of the initial claim. |
| S5 [Optical fiber measurement system, 2017](https://onlinelibrary.wiley.com/doi/10.1155/2017/4168150) | 2; provisional B; publisher abstract | Reports rotor-rig static/dynamic optical tests, approximately 5 mm range and 25 micrometre-or-better accuracy in that apparatus. These are literature specifications, not our uncertainty allowance. |
| S6 [Fibre sensor for tip clearance, 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6111710/) | 2; provisional B; indexed primary abstract, direct PMC CAPTCHA | Reflective fibre-bundle sensing demonstrated on a turbine rig; a narrow calibrated working interval matters. Actual target reflectivity, incidence and optical access still need qualification. |
| S7 [NASA microwave clearance/health measurement, 2008](https://ntrs.nasa.gov/citations/20080047680) | 2; official technical-report abstract, preliminary apparatus evidence | Microwave phase-based distance sensing and fan measurements already exist. The cited large axial fan/hot-engine context does not prove suitability for this small rotor. |
| S8 [US5131603A, 1992](https://patents.google.com/patent/US5131603A/en) | 2; patent abstract/description | Split segmented shrouded rotor assemblies are longstanding disclosures. Generic segmentation cannot anchor novelty. No legal scope conclusion is made. |
| S9 [JP2023124296A, 2023](https://patents.google.com/patent/JP2023124296A/en) | 0; excluded patent hit, abstract | Foldable construction/HVAC duct, not a rotor-clearance experiment. Retained to show why wording matches are not automatically scientific overlap. |
| S10 [US11634222B2, 2023](https://patents.google.com/patent/US11634222B2/en) | 1; patent abstract/description search extract | Foldable fixed-wing aircraft with ducted fans; not evidence that the duct itself is the proposed deployment mechanism. Background only. |

The denominator is **10 selected records**, not all returned search hits or all
research. Eight are relevant ingredients; none establishes the complete target
combination from the material inspected. Direct-fetch failures are not zero
findings. No source reports our apparatus' performance. No retraction database
was queried; formal status checks belong in full closeout.

## Measurement shortlist — requirements before a purchase

These are provisional engineering choices inferred from S5–S7, not vendor
recommendations or validated specifications.

| Candidate route | What literature supports | Required local qualification before selection |
| --- | --- | --- |
| Reflective optical fibre / optical displacement | Dynamic noncontact measurements exist (S5/S6) | Actual blade material/finish calibration; working distance and monotonic response; incidence sensitivity; bandwidth at blade-passing frequency; access without unsafe intrusion; installed drift and uncertainty |
| Optical imaging with a calibrated reference | A possible independent static/slow reference, not qualified here | Demonstrate scale calibration, motion blur/exposure, perspective, occlusion and angular sampling. Do not call a static image a dynamic minimum-clearance measurement |
| Microwave distance probe | Phase-based sensing on a large fan is demonstrated (S7) | Target response, probe footprint versus blade width, working range, mounting/containment compatibility and calibrated dynamic response at this scale; defer if unavailable |
| Capacitive/eddy-current alternatives | Not sufficiently reviewed in this pass | No default selection: material coupling, conductive target assumptions and instrument-specific calibration must be sourced first |

First choice to **investigate**, not buy: optical sensing if the lab can demonstrate
a reliable response on the actual blade. Otherwise retain the method decision as
unknown. Publish no invented micron budget or RPM envelope. SSY-02 must connect
the smallest intended effect to installed uncertainty and sampling requirements;
literature best-case resolution cannot fill that budget.

## Claim ledger and decisions

**Claim A:** Mean clearance and harmonic/nonuniform clearance are established.
Support S1–S3, moderate confidence (abstract-level). Consequence: compare against
mean-only prediction and explicitly separate mean, amplitude and family transfer.

**Claim B:** Segmentation already has modeled flow/acoustic effects.
Support S4 and disclosure background S8, moderate confidence. Consequence: the
useful first contribution is controlled, uncertainty-qualified measurement, not
inventing a segmented duct. No “first ever” or universal-infeasibility language.

**Claim C:** Dynamic clearance instrumentation exists but transfer is unqualified.
Support S5–S7, moderate confidence. Consequence: use a measurement-system gate
before collecting aerodynamic confirmation. A no-rub observation alone does not
establish protection or containment; the independent guard branch is unchanged.

## Finish-line implications and remaining review

Keep the first apparatus rigid, with fixed mean-clearance comparison and a
predeclared feature basis. If a descriptor is absent in training, do not fit its
coefficient by looking at the held-out family. Report that test as extrapolation
or supply a genuinely specified physical model. Do not promote mechanism
replication, a protective-guard claim, or free flight to the initial experiment.

The retrieved evidence supports narrowing and a metrology shortlist; it does not
yet establish a globally novel, manufacturable or publishable study. Full
SSY-01 needs complete close-competitor texts (especially S2–S4), the actual native
database screening export and measurement-method qualification choices. SSY-02/03
and owner resource/disclosure gates remain unchanged. Patent hits here are
technical background, not an infringement, clearance or patentability opinion.

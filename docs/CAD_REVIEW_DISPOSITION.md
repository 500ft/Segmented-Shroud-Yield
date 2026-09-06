# CAD review disposition — 2026-09-06

## Merge policy: pending owner decision

The reviewer supplied two blocking policy questions. The prior cleanup is verified in Git history for P-V, Drone, RoboRacer and Enclosure. This amendment does not silently reverse it. All five CAD PRs are draft; no merge is authorized until Owner records whether main admits planning ledgers or only reviewer-facing engineering contracts.

Current conservative disposition: keep task ledgers on the unmerged planning branch and remove the newly added README promotion. If Owner selects contracts-only, extract parameter/interface/inspection/verification contracts into a clean main-targeted change and keep task statuses outside main. Reconcile the prerequisite integrity PRs too; their sprint ledgers remain byte-preserved here, so merging those unchanged would reintroduce the same policy problem. No private repository was created and a public branch is not private storage.

## Disclosure gate

SSY-CAD-08/09 now contain identifiers and withheld notices only. No mechanism title, method, output path or estimated effort remains in those rows or their current plan/scope/PR summary. XC-02 closure is unverified; do not restore details or infer approval from the task existing. Previously public commits and older repository documents remain publicly accessible. This cleanup does not undo disclosure or claim to erase GitHub history; it does not authorize rewriting history or any new enabling detail.

## Accepted engineering amendments

Rigid-family CAD parked until SSY-01/02/03 and XC-02 close. SSY-CAD-08/09 are identifier-only placeholders with scope and estimates withheld. No new implementation-sensitive geometry is added.

Code-CAD/CI is now an explicit selected workflow and separately estimated task, not an already implemented test. Cross-ledger prerequisites are recorded in [CAD_DEPENDENCIES.json](CAD_DEPENDENCIES.json); the embedded validator checks references and prevents a task entering todo/in_progress/done with unverified prerequisites. Checks establish metadata consistency, not authentic external approval.

## Inputs and limits

The pasted review was available and checked against local files/current PR heads. The two artifact attachment links in the user message were not available as local files; their additional unpasted punch-list items have not been claimed reviewed. No CAD models or scientific measurements were made in this amendment.

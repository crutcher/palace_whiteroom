---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T154500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T155500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Audit orthogonalize-composition-lowering (three-way delegation boundary)"

## Critique

This is an **audit-kind report** (lowering-verifier) that proposes **no artifact mutation** and no new
`verified_against:` rows. Its single deliverable is a verdict — "cleanly-partitioned" — on whether three
firm themes that cite an overlapping ~50-line `orthog.hpp` Gram-Schmidt routine own disjoint facets. The
checks below are adapted to that audit shape; where a check targets new-authoring surface it is marked
not-applicable with a reason.

### Checks run

**citation-validity — pass.** I re-ran `tools/citecheck/citecheck.py --scan` on the report's own CYCLE.md
(`23 ok, 0 failing`, exit 0) and `--scan` on all three cited themes, reproducing the report's headline
counts exactly: L2>L1 theme **38 ok / 0 failing**, `dot-mutation-rotation` **41 ok / 0 failing**,
`orthogonalize-mutation-rotation` **21 ok / 0 failing** = **100 citations, 0 failing** — the report's
"100 citations total" / "0 failing across all three themes" claim is mechanically accurate. I then ran
`--anchor` spot-checks on every load-bearing boundary pinpoint and read `orthog.hpp` in full (93 lines)
to adjudicate meaning, not just bounds. Every claimed line is exact: `:35` `LocalDot` (ok), `:41`
`OrthogonalizeColumnMGS` def (ok), `:49` `H[j] = dot_op(w, V[j])` (ok), `:50` `Mpi::GlobalSum(1, &H[j], comm)`
(ok), `:51` `w.Add(-H[j], V[j])` (ok), `:57` `OrthogonalizeColumnCGS` def (ok), `:62` `if (m == 0)` (ok),
`:70` `Mpi::GlobalSum(m, H, comm)` (ok), `:75` `if (refine)` (ok), `:85` `H[j] += dH[j]` (ok via literal
anchor — my earlier `--regex` NOANC was double-escaping on my side, not drift), `:22` `Assumes that the
input vectors are normalized` (ok). Dispatch sites confirmed: `iterative.cpp:308-325` `switch (type)` at
:313 + `OrthogonalizeColumnCGS` at :319/:322 (ok); `romoperator.cpp:51-66` `OrthogonalizeColumn` switch with
cases at :51/:59/:62/:65 (ok); `romoperator.cpp:631-646` `InnerProduct` at :636 (ok). The report's
`:34→:35` stale-in-the-good-direction claim is **confirmed**: `grep` finds `orthog.hpp:35` at both
`dot-mutation-rotation.md` prose line 160 and `verified_against:` line 404, and zero residual `:34`
anywhere in that file — the cycle-024 fix is applied on both surfaces.

**surface-or-evidence — pass.** The report is a pure audit verdict that proposes no surface change and no
new evidence rows; it is neither a refinement-shaped proposal nor a retroactive-evidence backfill. The
restraint is correct and explicitly justified (the existing 18-entry `verified_against:` block already
carries the three cross-theme delegation entries; appending would duplicate). Not a surface/evidence
defect — no proposal to classify.

**rotation-quality — pass (not applicable as authored).** No new rotation is asserted; the report audits
the already-firm L2>L1 stage-selection rotation. For completeness I confirmed the audited rotation is a
genuine rotation (the L2 composition records pass-count + collective-shape — `m×1`/`1×m`/`2×m` — as an
abstraction over the three concrete `orthog.hpp` loop bodies, not a 1:1 rename), but this is inherited
firm content, not this report's product. No new rotation to grade.

**variant-axis-coverage — pass.** The orthogonalize routine has two live variant axes and the report
covers both: (a) the MGS/CGS/CGS2 dispatch axis (each variant's pass-count + collective-shape audited
individually: MGS `:41-53`, CGS `:57-74`, CGS2 `:75-88`), and (b) the inner-product-hook axis (unweighted
`IdentityInnerProduct`/`LocalDot` vs B-weighted `W.InnerProduct` at `romoperator.cpp:636`). The report
correctly scopes the unweighted-hook L0 realisation OUT (delegated to Sub-pattern D) and keeps the
B-weighted-vs-unweighted axis as this theme's exclusive concern — no hidden branch.

**cross-reference-integrity — pass.** All three boundary-owner themes exist on disk
(`book/src/L2-L1/orthogonalize-composition-lowering.md`, `book/src/L1-L0/dot-mutation-rotation.md`,
`book/src/L1-L0/orthogonalize-mutation-rotation.md`). The OQ being discharged exists in
`scaffolding/open-questions.md` (line 327, migrated-to-plan). The audited theme's `verified_against:` block
does carry 18 entries with `audited_at: 2026-05-29T092943Z` (I counted the `citation:` lines), and its
final three are exactly the cross-theme delegation entries the report names: `dot-mutation-rotation.md:146-187`
(line 473), `orthogonalize-mutation-rotation.md` (line 477), `L2/orthogonalize.md:166-220` (line 481) —
matching the report's claim precisely. No firm-body-outside-fence concern: the report proposes no
`edit:`/`new:` block at all. Independently corroborated the central complementarity claim against source:
the L2>L1 theme prose explicitly delegates ("does NOT re-derive the unfused LocalDot+GlobalSum chain",
lines 152-174; "this theme stops at the L1 leaf and does not re-derive that L0 step", lines 71-73);
Sub-pattern D's section header literally reads "hook-routed `LocalDot` + batched `Mpi::GlobalSum` (the
unfused form)" and owns that facet; `orthogonalize-mutation-rotation` condition 1 ("No observer of the
prior `w` value after the call", line 161) + conditions 4/5 own the in-place `w.Add` mechanics. The three
facets are genuinely disjoint and mutually consistent against the single source routine.

**edge-label-fidelity — pass.** The report carries an L2>L1 edge for the audited theme and L1>L0 edges for
the two delegated themes; the prose discusses exactly those edges. The "three-way" framing keeps the
direction straight (L2 stage-selection lowers onto L1 leaves; the two L1>L0 themes lower those leaves onto
L0). No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind is an audit (lowering-verifier, `status: pending`, no
proposed changes). The content shape matches: per-citation audit table, applicability-condition walk,
delegation-boundary partition table, explicit "Proposed changes: None", OQ discharge. Consistent with the
audit kind; not mis-classified as a firm-authoring entry.

**skill-uptake-survey — pass.** The audit shape implies `verify-citation-range` (with the cycle-024
mechanical `tools/citecheck --anchor/--scan` realization) and `verify-rotation-citation`; the report
references the citecheck `--anchor`/`--scan` invocations throughout and explicitly invokes the
`verify-citation-range` audit-sub-case for the enclosing-vs-precise reconciliation (line 286). Telemetry
present.

### Issues found

No blocking or warning issues. The audit's central claim (cleanly-partitioned three-way boundary) is
independently corroborated against source, the citecheck counts reproduce exactly, the `:34→:35`
stale-in-good-direction note is confirmed, the no-mutation/no-new-rows restraint is correct and matches
the scope's explicit caution, and the OQ discharge is justified (the verdict directly answers the
question the OQ posed). The following are minor observations, none rising to a defect:

1. **(observation, cosmetic, not in this report) Stale-in-good-direction note persists in the audited
   theme's `verified_against:` block.** `orthogonalize-composition-lowering.md:476` still reads
   "Sub-pattern D's own :34 anchor for LocalDot is stale (should be :35)" — but the `:34` was already
   fixed cycle-024 (confirmed: zero `:34` residual in `dot-mutation-rotation.md`). The report correctly
   diagnoses this (Open questions, "Carry-forward already recorded by the producer") and correctly judges
   it below the dispatch bar. This is a defect in the *audited theme's prose*, not in this report; flagging
   only so a future lifter touching that theme can trim the now-obsolete parenthetical. No action on this
   report.

2. **(observation) Report's per-citation "Found" lines paraphrase line numbers slightly off the cited
   wide range, but never wrongly.** E.g. the MGS entry cites `:41-53` and reads `:39-52`; the CGS entry
   cites `:57-74` and reads `:53-71`. These are the verifier's own read-window pointers, all enclosing the
   load-bearing lines, and every pinpoint inside (`:49/:50/:51`, `:62/:70`, `:75/:85`) is exact per my
   `--anchor` checks. Not a citation defect — the wide ranges and pinpoints both resolve correctly.

3. **(observation) "19 boundary anchors" / "100 citations" are the report's tallies, not re-counted by
   me line-for-line.** I reproduced the 100-citation 0-failing scan total exactly and confirmed the
   load-bearing subset of the 19 anchors by hand; the residual anchors are low-risk consumer/test sites
   already covered by the clean `--scan`. No discrepancy surfaced.

---

## Repair

All 8 checks passed at critique. This is a clean lowering-verifier audit whose single deliverable is a
verdict ("cleanly-partitioned, three-way delegation boundary") that proposes **no artifact mutation and
no new `verified_against:` rows** — and that restraint is the *correct* product (the cycle-023 18-entry
`verified_against:` block already carries the three cross-theme delegation entries; appending would
duplicate). Nothing in the report is repairable-and-needs-repair: there is no missing citation, no
off-by-N range, no dep-map gap, no edge-label mismatch, no SIDEWAYS/append-by-slug situation, and no
plan-kind misclassification. The frontmatter already reads `verifies: ../CYCLE.md` (no stale
`../REPORT.md` to correct), and the directory holds no supporting docs. No edits applied to CYCLE.md.

### Fixes attempted

- **Finding**: citation-validity — pass. Critic re-ran `citecheck --scan`/`--anchor` and reproduced the
  100-citation / 0-failing headline and every load-bearing pinpoint.
  - **Decision**: not-needed. Nothing to fix; the report's counts are mechanically accurate.

- **Finding**: surface-or-evidence — pass. Pure audit verdict, no surface change, no new evidence rows;
  the no-row restraint is explicitly and correctly justified.
  - **Decision**: not-needed. No proposal to reclassify; the restraint is the right call.

- **Finding**: rotation-quality — pass. No new rotation asserted (audits the already-firm L2>L1
  stage-selection rotation).
  - **Decision**: not-needed. No new rotation to grade or repair.

- **Finding**: variant-axis-coverage — pass. Both live axes covered (MGS/CGS/CGS2 dispatch; unweighted
  vs B-weighted inner-product hook), each audited individually; unweighted-hook L0 correctly scoped out
  to Sub-pattern D.
  - **Decision**: not-needed. Axes fully covered; no classification gap to fill.

- **Finding**: cross-reference-integrity — pass. All three boundary-owner themes exist on disk, the
  discharged OQ exists, the 18-entry `verified_against:` block + its three cross-theme delegation rows
  match the report's claims, and the complementarity claim corroborates against source.
  - **Decision**: not-needed. No broken link, no renamed-file reference.

- **Finding**: edge-label-fidelity — pass. L2>L1 edge for the audited theme + L1>L0 edges for the two
  delegated themes; prose discusses exactly those edges with correct direction.
  - **Decision**: not-needed. No edge-label/prose mismatch to correct.

- **Finding**: plan-kind-consistency — pass. Declared kind (audit, `status: pending`, no proposed
  changes) matches the content shape.
  - **Decision**: not-needed. No `concept_writes`→`section_appends` or H1→H2 normalization applicable.

- **Finding**: skill-uptake-survey — pass. `verify-citation-range` (with the cycle-024 `citecheck
  --anchor/--scan` realization) and `verify-rotation-citation` telemetry present.
  - **Decision**: not-needed. Survey present.

The critic's three minor observations were also reviewed and require no repairer action:
- **(obs 1) Stale-in-good-direction `:34`→`:35` parenthetical in the AUDITED THEME's prose**
  (`book/src/L2-L1/orthogonalize-composition-lowering.md` ~line 476). This is an **artifact-side** cosmetic
  residue, NOT a defect in this report — the report correctly diagnoses it (Open questions,
  "Carry-forward already recorded by the producer") and correctly judges it below the dispatch bar. Per
  role-spec, the repairer does not modify the artifact (`book/`); deferred to a future lifter that touches
  that theme. Noted for follow-up only.
- **(obs 2) Verifier read-windows slightly wider than cited ranges, always enclosing, never wrong.** Left
  as-is per the dispatch note — every pinpoint inside resolves exactly; no citation defect.
- **(obs 3) "19 anchors / 100 citations" tallies reproduced by the critic.** No discrepancy; nothing to fix.

### Unrepairable findings

None. No finding exceeds repair authority, because no finding is a defect requiring repair — every check
is `pass` and every observation is either artifact-side (out of repairer scope), benign, or already
corroborated. `overall_status: ready`.

## Suggested resolution

`ready`. Integrator notes:
- This report proposes **no artifact mutation and no new `verified_against:` rows** — the integrator
  should apply it as a verdict-only audit: discharge the OQ
  `orthogonalize-composition-lowering-three-way-delegation-boundary-audit` (verdict:
  **cleanly-partitioned**) and stage the row; there is no `book/` edit to land.
- One **artifact-side follow-up** is worth carrying in the plan (not blocking): the now-obsolete
  `:34`→`:35` stale-in-good-direction parenthetical in
  `book/src/L2-L1/orthogonalize-composition-lowering.md` (~line 476) can be trimmed opportunistically the
  next time a lifter touches that theme. It is below the dispatch bar on its own and is NOT a defect in
  this report.

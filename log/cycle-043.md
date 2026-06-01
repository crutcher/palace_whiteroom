# 2026-06-01 cycle-043 — integration summary

**Cohort-completing L2-floor build: the held `axpy`-family + `normalize` floors + their 8 thin-identity themes + the in-artifact leaf-vs-fold fork ratification + the c042-cohort stale-L3 re-anchor / slug-normalization sweep.**

> NOTE on numbering: this is the **layered-era cycle-043** (post-2026-05-26 structural redirect). A legacy **slice-vertical-era cycle-43** entry (2026-05-25, "forward gmres [L2→L3]") is preserved at the bottom of this file for historical continuity; the two are distinct cycles that collide only on the zero-padded filename.

**Kind:** integration (primary cycle — phases plan → dispatch → critique → repair → integrate)
**Meta-batch:** batch-13, position 1 of 3 (cycles 043/044/045). **The batch-13 meta-phase fires AFTER cycle-045's finalize commit, as a SEPARATE dispatch — NOT run in this cycle.** The cycle counter does NOT reset across batch boundaries.
**Written by:** `integrator-finalize` (split integrator-per-report ×10 + finalize ×1).

## Headline

The first primary cycle of meta-batch-13 **completed the `l2-floor-under-l3-leaf-cohort`** — the four floors that batch-12 left outstanding landed firm now that the batch-12 meta-phase ratified the `(b)` leaf-floor reading:

- **L2 firm 17 → 21** — `book/src/L2/{axpy,axpby,axpbypcz,normalize}.md` (4 NEW firm floors).
- **L2>L1 firm 15 → 19** — `book/src/L2-L1/{axpy,axpby,axpbypcz,normalize}-leaf-identity.md` (4 NEW firm themes).
- **L3>L2 firm 10 → 14** — `book/src/L3-L2/{axpy,axpby,axpbypcz,normalize}-body-identity.md` (4 NEW firm themes); `l3-l2-rotation-theme-coverage-gap` advanced **10-of-18 → 14-of-18**.
- The **leaf-vs-fold fork is RATIFIED IN-ARTIFACT** (keep leaf-floor `(b)`): the §"Design fork" bullets in all three indexes (`L2`, `L2-L1`, `L3-L2`) flipped provisional → RATIFIED.
- The **cohort is effectively COMPLETE** — 12-of-13 same-named floors landed; the 13th, `chebyshev`, is already floored via the pre-existing `chebyshev-iteration` L2 entry (a non-same-named slug). The count-reconciliation (12-of-13 + naming-exception) is routed to the batch-13 meta-phase (OQ `chebyshev-floor-cohort-count-reconciliation`).

## The 4 floors (D3/D4/D5/D9)

- **`axpy`** (D3) — arity-2 member of `linear_combination`, second coefficient fixed to 1, cited-NOT-merged; six laws + IEEE-754 FP-summation non-law made explicit at L2; firm-on-positive-structure.
- **`axpby`** (D4) — arity-2 fold-member; nine inherited laws + the fold-specialization identity + four inherited non-laws; the arity-2 fused pass IS a two-term sum (summation-order non-law non-degenerate).
- **`axpbypcz`** (D5) — arity-3 fold-member; twelve inherited laws + four non-laws; firm on the three `AXPBYPCZ` template specialisations `vector.cpp:745-772`.
- **`normalize`** (D9) — the **FUSED-COMPOSITE-with-no-fold-parent** sub-shape: `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`, returned-norm load-bearing, consumes the `nrm2`+`scal` floors, fork-INDEPENDENT, design-final on the fork. This is the **third thin-identity sub-shape** (distinct from c041 fold-parented-leaf + c042 standalone-leaf/-gate) — routed to the batch-13 meta-phase cohort-classification vocabulary review (OQ `normalize-fused-composite-no-fold-parent-sub-shape`). It REALIZES the long-standing `scal.md:223-228` "harvest fused normalize?" plan item.

## The 8 themes (D6/D7/D8/D10)

4 L2>L1 leaf-identity + 4 L3>L2 body-identity edges. The axpy-family leaf edges are arity-fold-members of `linear-combination-fold-specialization` (all fusion deferred to the fold-parent); `normalize-leaf-identity` is the fused-composite leaf with NO fusion to defer (Palace's `linalg::Normalize` already separates the norm pass from the rescale pass). The body-identity edges are all L3-native-by-signature per `krylov-step-body-identity.md:97`.

## The D1 consolidated lifter sweep

D1 enacted the cycle-042-carry-forward in one pass:
- Re-anchored the 4 stale c042-cohort firm L3 entries (`reciprocal`/`assemble-diagonal`/`jacobi-smoother`/`divfree-projector`) from L3>L1 → L3>L2>L1 — **closing** OQ `l3-divfree-projector-stale-no-interposed-l2-entry-lifter-reanchor`.
- Normalized 3 theme slugs via `git mv`: `nrm2`/`scal`-`fold-specialization` → `-leaf-identity`, `elementwise_product-body-identity` → `elementwise-product-body-identity` (REALIZING the batch-12 meta-phase slug-normalization in-artifact).
- Fixed B1 (`rap.cpp` AbsMultTranspose `:172`→`:174`) + B2 (`L3/index.md` self-citation `:39`→`:46`) citation drift.

## Process

- **10 of 10 dispatched-ready reports applied clean.** 10/10 staging rows == dispatched-ready — the cycle-018 staging-completeness gap did NOT recur for the **TWENTY-FOURTH consecutive** cycle. Zero deferrals, zero rejections, zero build-repairs.
- **Thirty-eighth consecutive cycle under the split integrator.**
- **`cycle-planner-stale-priorities-line-recruitment` did NOT recur** — the FIRST clean opus-planner cycle of batch-13.
- **Count-ownership partition held** — D1/D3-D10 each touched ONLY their own dep-map/theme rows; D2 (layer-intro-author) was the SOLE consolidated count-owner. `parallel-blind-shared-index-count-divergence` did NOT recur across the 10-wide wave.
- **Cross-report rename interaction caught + repaired 4×.** The 4 theme-pair reports (D6/D7/D8/D10) were authored before/parallel to D1's `git mv` slug renames; each carried live links to now-deleted old-slug files (hard `linkcheck2` errors). The per-report integrators' re-read-disk-at-apply discipline caught and repaired all of them pre-build — exactly what that discipline exists to catch.
- **Build clean** — `cargo make book` exit 0 (~90s); the only warnings are the pre-existing KaTeX "Potential incomplete link" false-positives in `design/l4_calculus.md`. linkcheck2 green for all 12 new entries; **zero dead links to the 3 renamed files** anywhere in `book/src/`; all 12 new files SUMMARY-wired. Zero build-repairs.

## Friction surfaced for the batch-13 meta-phase

- **NEW — dual-registration ambiguity.** The §"Vocabulary-cohort" bullet vs index-table-row ownership was handled inconsistently across the 4 theme-pair reports (D6 deferred bullets to D2; D7 omitted table rows; D8/D10 omitted bullets), each needing a repairer patch. The convention "**producers add BOTH the table row AND their own cohort bullet; the count-owner adds only the consolidated tally**" should be CODIFIED (cycle-planner dispatch-design note + producer role-spec note).

## Carry-forward to cycle-044 (next primary cycle)

1. **Consolidated L3-re-anchor sweep (HIGH).** The new c043 floors' OWN L3 entries (`axpy`/`axpby`/`axpbypcz`/`normalize`) carry the now-stale "no interposed L2 entry / direct L3>L1 hop" assertions (their floors just landed) — mirror the c042→c043 sweep. Bundle with: the deferred `l3-index-audit-block-citation-drift` index-wide citation-drift sweep + the `l2-floor-directive-slug-rename-book-chapter-body-residual` sweep (12 prior-cycle chapter bodies still carry the old `l2-floor-under-l3-blas1-cohort` slug in prose) + the `l2-floor-directive-slug-rename-scaffolding-residual-sweep` (priorities.md/roadmap.md old-slug occurrences — meta-phase owns the plan). ONE c044 lifter/cleanup sweep.
2. **Next foundation frontier (post-cohort).** The substantive `(B)` L3 cohort (`chebyshev-smoother` subsumption check, `apply_nonlinear_pencil`) now competes under `foundation_solidity` with present L2 floors; then the remaining 4 substantive L3>L2 rotations (`orthogonalize`/`chebyshev`/`eigsolve` + residual); then L2→L1 / L4→L3 coverage; then resume the uniform climb.

## Counts after cycle-043

L1 firm 26 · **L2 firm 21** · **L2>L1 firm 19** · L3 firm 15 + 3 partial-obstruction · **L3>L2 firm 14** · L4 firm 4 · L0 chapters 22 · Phase-1 removals 9/10.

---

## (legacy / historical) 2026-05-25 cycle-43 — forward gmres [L2→L3] — pass

- Synthesis: Emit retroactive L2→L3 rotation_claims for the gmres slice's existing on-disk L3 section (field-side lifts for initial_residual / apply_BA / orthogonalize-CGS / apply_correction, plus the ls_update_column and back_solve sequential-obstruction records). No new structural writes; the L3 content already exists at book/src/spec/slices/gmres.md §'L3 — global tensor-field form'. Per-claim citations point at that section and at the concepts it references.
- Verdict: pass.
- Friction: none.
- Structural change: none.

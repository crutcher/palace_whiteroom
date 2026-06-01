---
agent: layer-intro-author
invoked_at: 2026-06-01T051607Z
scope: cycle-041 D7 (wave-3) — consolidated count refresh of THREE shared indices (L2, L2>L1, L3>L2) folding in the six wave-1/wave-2 BLAS-1-floor landings (dot/nrm2/scal + their adjacent thin-identity themes); SOLE count-owner this cycle
status: pending
integrated_at: 2026-06-01T062913Z
integration_commit: c1f7ea3c651e65ed212aa8500c7c8572aaa2ec92
integration_notes: "Applied clean (staging row D7). SOLE count-owner: L2/index firm 9->12, L2-L1/index firm 7->10, L3-L2/index firm 2->5 (l3-l2-rotation-theme-coverage-gap 2-of-18 -> 5-of-18; §Vocabulary-cohort subsection PROMOTED first-time at L3-L2/index). Created NO files, touched NO dep-map ROW (D1-D6's). Consistency VERIFIED against on-disk anchor-text row enumeration. count-ownership partition held across the 7-wide wave."
---

# CYCLE: L2 / L2>L1 / L3>L2 index refresh (cycle-041 BLAS-1-floor cohort)

## Summary

I am the SOLE count-owner this cycle for three shared consolidated indices. Six dispatches
landed the **L2 floor under the three most-reused BLAS-1 leaves** (`dot`/`nrm2`/`scal`) plus
their adjacent thin-identity lowering themes, all under the 2026-05-31 foundation-first
directive `l2-floor-under-l3-blas1-cohort` (D1–D3 harvesters) and `l3-l2-rotation-theme-coverage-gap`
(D4–D6 abstractors). D1–D6 each appended ONLY their own non-aggregate dep-map / theme-list rows
and DEFERRED every consolidated tally to me (count-ownership partition, friction-ledger
`parallel-blind-shared-index-count-divergence`). This report computes the **post-cohort** tallies
across all three indices and refreshes their orientation prose:

1. **`book/src/L2/index.md`** — firm **9 → 12** (+`dot`, +`nrm2`, +`scal`; partly-constructive
   `deflate` unchanged at 1). New §Semantics third motif ("identity-in-form BLAS-1 floors") +
   a §Vocabulary-cohort sub-group + a §Working-Notes cohort entry. **Surfaces the leaf-vs-fold
   design fork PROMINENTLY** (load-bearing batch-12 meta-phase signal).
2. **`book/src/L2-L1/index.md`** — firm **7 → 10** (+`dot-leaf-identity`,
   +`nrm2-fold-specialization`, +`scal-fold-specialization`; partly-constructive `deflate-composition-lowering`
   unchanged at 1). New §Vocabulary-cohort sub-group + Working-Notes cohort entry.
3. **`book/src/L3-L2/index.md`** — firm **2 → 5** (+`dot-body-identity`, +`nrm2-body-identity`,
   +`scal-body-identity`). **Begins closing `l3-l2-rotation-theme-coverage-gap`: 2-of-18 → 5-of-18.**
   Promotes a §Vocabulary-cohort subsection into this index for the first time (≥3 firm now).

I verified each index's dep-map / theme-list row enumeration matches its tally after this cycle's
landings (see §Count verification). Two load-bearing meta-phase signals are surfaced in the
narrative and §Open-questions: the **leaf-vs-fold design fork** and the **slug-naming
inconsistency** (`dot-leaf-identity` vs `nrm2/scal-fold-specialization`).

## On-disk status verification (per role discipline)

Per role-spec "Survey chapter firmness from the on-disk `## Status`, NOT the cycle record": the
six landing chapters are NOT yet on disk (they co-land this cycle's integration alongside this
refresh — wave-3 serial sequencing). I therefore surveyed each chapter's `## Status` declaration
from its **proposed-changes block** in the six wave-1/wave-2 CYCLE.md reports (the only available
source pre-integration), and confirm each carries an explicit firm declaration:

- `book/src/L2/dot.md` — `## Status` → `firm` (thin identity-in-form floor; laws inherited unchanged; PSD-at-diagonal law confirmed by in-source `&x==&y` imag=`0.0` elision). [D1]
- `book/src/L2/nrm2.md` — `## Status` → `firm` (value-thread-isomorphic to L1; fusion rotation a no-op; `std::abs` guard preserved as load-bearing claim). [D2]
- `book/src/L2/scal.md` — `## Status` → `firm` (firm-on-positive-structure; syntactic-identity laws on the small fully-present `operator*=` surface). [D3]
- `book/src/L2-L1/dot-leaf-identity.md` — `## Status` → `firm` (structural; identity-in-form on the inner-product leaf; fusion deferred to fold-parent). [D4, slug ADJUSTED from `dot-fold-specialization`]
- `book/src/L2-L1/nrm2-fold-specialization.md` — `## Status` → `firm` (structural; thin-identity consumer sibling of `inner-product-fold-specialization`). [D5]
- `book/src/L2-L1/scal-fold-specialization.md` — `## Status` → `firm` (structural; degenerate arity-1 single-term shadow of `linear-combination-fold-specialization`). [D6]
- `book/src/L3-L2/dot-body-identity.md` — `## Status` → `firm` (structural; `dot` L3-native by signature shape; no wrapper). [D4]
- `book/src/L3-L2/nrm2-body-identity.md` — `## Status` → `firm` (structural; BLAS-1-leaf analogue of `krylov-step-body-identity`; no wrapper rotation). [D5]
- `book/src/L3-L2/scal-body-identity.md` — `## Status` → `firm` (structural; identity-in-form on the body, no wrapper to rotate). [D6]

All nine land `firm` per their proposed-changes `## Status` lines; the three index tallies below
treat them as firm accordingly. (If the integrator applies any of the six producer reports with a
status downgrade during repair, my tallies would need a corresponding decrement — flagged in
§Open-questions as a build-ordering dependency, not expected.)

## Count verification (post-cohort enumeration)

**L2 firm cohort (9 → 12).** Pre-cycle "Firm at L2" list: `krylov-step`, `chebyshev-iteration`,
`linear_combination`, `inner_product`, `orthogonalize`, `ksp_solve`, `gram`,
`incremental-least-squares`, `eigsolve` = **9**. Post-cycle adds `dot`, `nrm2`, `scal` = **12**.
Partly-constructive `deflate` unchanged at **1**. Dep-map table rows after landing: the 9 existing
firm rows + `deflate` + the 3 new floor rows (each producer inserted its own row — `dot` after
`inner_product`, `nrm2` after `dot`, `scal` after `linear_combination`) = 13 rows = 12 firm + 1
partly-constructive. ✓ matches.

**L2>L1 firm cohort (7 → 10).** Pre-cycle "Firm at L2>L1" list: `chebyshev-iteration-fusion`,
`linear-combination-fold-specialization`, `inner-product-fold-specialization`,
`orthogonalize-composition-lowering`, `gram-fold-specialization`,
`eigsolve-spectral-transform-composition`, `incremental-least-squares-composition-lowering` = **7**.
Post-cycle adds `dot-leaf-identity`, `nrm2-fold-specialization`, `scal-fold-specialization` = **10**.
Partly-constructive `deflate-composition-lowering` unchanged at **1**. Theme-list rows after landing:
7 existing firm + 1 partly-constructive + 3 new = 11 rows = 10 firm + 1 partly-constructive. ✓ matches.

**L3>L2 firm cohort (2 → 5).** Pre-cycle theme list: `krylov-step-body-identity`,
`ksp-solve-outer-driver` = **2**. Post-cycle adds `dot-body-identity`, `nrm2-body-identity`,
`scal-body-identity` = **5**. Theme-list rows after landing: 2 existing + 3 new = 5 rows = 5 firm.
✓ matches. This moves the `l3-l2-rotation-theme-coverage-gap` tracking expression from **2-of-18**
to **5-of-18** (13 L3 entries still without an L3>L2 theme).

## Proposed changes

### 1. `book/src/L2/index.md`

**(1a) §Semantics overlay — add the third motif ("identity-in-form BLAS-1 floors").** Anchor on
the end of the fold-cohorts bullet; append a new motif paragraph after it.

```edit:book/src/L2/index.md
  They share the fold skeleton but target different codomains (`Scalar` vs `Tensor[N]`); merging them would erase the codomain distinction and the do-NOT-merge note carried in both entries' dep-map rows is load-bearing.

## Vocabulary cohort
```

```edit:book/src/L2/index.md
  They share the fold skeleton but target different codomains (`Scalar` vs `Tensor[N]`); merging them would erase the codomain distinction and the do-NOT-merge note carried in both entries' dep-map rows is load-bearing.
- **Identity-in-form BLAS-1 floors** — same-named leaf entries for the most-reused BLAS-1 primitives, present so the firm L3 cohort rests on adjacent same-named L2 parents (per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**), under the 2026-05-31 foundation-first directive `l2-floor-under-l3-blas1-cohort`. Three landed cycle-041 (`dot`, `nrm2`, `scal`): each is value-thread-isomorphic to its firm L1 leaf (the fusion rotation is a no-op on the primitive — the L0 form is already the unfolded composition), with the fusion-rotation *framing* added in L2 vocabulary and any load-bearing numerical trick (the `nrm2` `std::abs` guard) preserved as an explicit algebraic claim. They are **distinct from the fold-parents** `inner_product` / `linear_combination`: `dot` is the conjugation-axis *leaf-of* `inner_product` (NOT merged); `scal` is the arity-1 *member-of* `linear_combination` (NOT merged); `nrm2` is a *consumer-of* `inner_product` (`√ ∘ abs ∘ inner_product` at `y=x`, NOT a fold member). The do-NOT-merge boundary (§"Fold-cohort boundary") is load-bearing for all three. **The leaf-vs-fold design fork for this floor cohort is under batch-12 meta-phase adjudication (see §Working Notes).**

## Vocabulary cohort
```

**(1b) §Vocabulary-cohort — refresh "Firm at L2" header count + append the BLAS-1 floor sub-group.**
Anchor on the existing `eigsolve` firm-cohort bullet (the last firm entry before the
partly-constructive block); append the three floor bullets after it.

```edit:book/src/L2/index.md
- `eigsolve` — **shift-invert spectral-transform application** `apply_shift_invert = apply_linop(M) ▷ ksp_solve((K − σM)⁻¹)` (the per-step body the opaque-library eigen-iteration folds). Chain-step-2 of the eigsolve prerequisite chain (L1-firm c022 → this entry → L3-backfill); first L2 named composition whose direct constituent is itself a constructed-solver composition. The per-step body is opened; the eigen-iteration *fold* stays library-owned (SLEPc `EPSSolve` / ARPACK RCI) — the inverse decomposition from `ksp_solve` whose fold IS opened. Firm cycle-023 (firm-on-positive-structure).

**Partly-constructive at L2** (firm structural decomposition + a constructive sub-part with a stated promotion condition):
```

```edit:book/src/L2/index.md
- `eigsolve` — **shift-invert spectral-transform application** `apply_shift_invert = apply_linop(M) ▷ ksp_solve((K − σM)⁻¹)` (the per-step body the opaque-library eigen-iteration folds). Chain-step-2 of the eigsolve prerequisite chain (L1-firm c022 → this entry → L3-backfill); first L2 named composition whose direct constituent is itself a constructed-solver composition. The per-step body is opened; the eigen-iteration *fold* stays library-owned (SLEPc `EPSSolve` / ARPACK RCI) — the inverse decomposition from `ksp_solve` whose fold IS opened. Firm cycle-023 (firm-on-positive-structure).

*Identity-in-form BLAS-1 floors (cycle-041; present so the firm L3 cohort rests on adjacent same-named L2 parents; distinct from the fold-parents — do-NOT-merge):*

- `dot` — conjugation-axis **leaf-of** `inner_product` (the plain `M = I` Hermitian / symmetric member); thin identity-in-form floor, laws inherited unchanged from the L1 leaf. Firm cycle-041 (D1).
- `nrm2` — **consumer-of** `inner_product` (`√ ∘ abs ∘ inner_product` at `y=x`, NOT a fold member); the `std::abs` defensive guard preserved as an explicit load-bearing numerical claim. Firm cycle-041 (D2).
- `scal` — arity-1 **member-of** `linear_combination` (`scal(α,x) = linear_combination [(α,x)]`, NOT merged); firm-on-positive-structure (syntactic-identity laws on the small fully-present `operator*=` surface). Firm cycle-041 (D3).

**Partly-constructive at L2** (firm structural decomposition + a constructive sub-part with a stated promotion condition):
```

**(1c) §Working Notes — append the cycle-041 BLAS-1-floor cohort note (carries the firm tally
9→12 AND the load-bearing leaf-vs-fold design-fork signal).** Anchor on the end of the existing
batch-6 cohort-growth note (the last §Working-Notes bullet); append the new note after it.

```edit:book/src/L2/index.md
- **Batch-6 cohort growth (Gram/deflate fold-lift + eigsolve chain-step-2)**: three landings raised the firm cohort 6→8 + added the first L2 `partly-constructive` tier. (1) [`gram`](./gram.md) (firm cycle-022, promoted from rough-in) — the **all-pairs `inner_product` fold → `Matrix[k,k]`**, the matrix-valued lift of the `inner_product` scalar fold (firm-on-positive-structure: all-pairs syntactic-identity laws on the positive Gram-build site `nleps.cpp:524-531`); Hermitian + PSD, consumed by `deflate`. (2) [`deflate`](./deflate.md) (the **first L2 `partly-constructive` entry**, cycle-022) — the oblique/Galerkin complementary projector `I − X(XᴴX)⁻¹Xᴴ`, the `coords ▷ schur-solve ▷ back-project` named composition over `gram` + [`lu_solve`](../L1/lu_solve.md) + `linear_combination` + `dot`; the **Schur-form pipeline is firm** (positive `deflated_solve` site `nleps.cpp:505-537`), the **bare-Galerkin core** (`S = I`) is the constructive sub-part (literature + negative anchor, promotion-gated on a positive Palace Galerkin-deflation site). The cycle-023 [`nleps_deflated_solve`](../L1/nleps_deflated_solve.md) landing **confirmed (did not change)** the partly-constructive status — the bare `(XᴴX)⁻¹` Galerkin core appears only Schur-wrapped, never standalone. Over-unification guard: `deflate` is NOT `orthogonalize` (`orthogonalize` = `deflate` at `gram = I`; the `(XᴴX)⁻¹` Gram solve is load-bearing). (3) [`eigsolve`](./eigsolve.md) (firm cycle-023 wave-1) — **chain-step-2** of the eigsolve prerequisite chain (L1-firm c022 → **this L2 entry** → L3-backfill); the **named shift-invert spectral-transform composition** `apply_shift_invert = apply_linop(M) ▷ ksp_solve((K − σM)⁻¹)`, the first L2 named composition whose direct constituent is itself a constructed-solver composition. A **partial-opening** named composition: the per-step *body* is Palace-authored and opened, but the eigen-iteration *fold* is opaque-library-owned (SLEPc `EPSSolve` / ARPACK RCI) and named by role only — the inverse decomposition from [`ksp_solve`](./ksp_solve.md) (whose fold IS opened). This is the load-bearing reason the L3 backfill landed `partial-obstruction` (cycle-024; chain-step-3 complete — see [`L3/eigsolve`](../L3/eigsolve.md)).
```

```edit:book/src/L2/index.md
- **Batch-6 cohort growth (Gram/deflate fold-lift + eigsolve chain-step-2)**: three landings raised the firm cohort 6→8 + added the first L2 `partly-constructive` tier. (1) [`gram`](./gram.md) (firm cycle-022, promoted from rough-in) — the **all-pairs `inner_product` fold → `Matrix[k,k]`**, the matrix-valued lift of the `inner_product` scalar fold (firm-on-positive-structure: all-pairs syntactic-identity laws on the positive Gram-build site `nleps.cpp:524-531`); Hermitian + PSD, consumed by `deflate`. (2) [`deflate`](./deflate.md) (the **first L2 `partly-constructive` entry**, cycle-022) — the oblique/Galerkin complementary projector `I − X(XᴴX)⁻¹Xᴴ`, the `coords ▷ schur-solve ▷ back-project` named composition over `gram` + [`lu_solve`](../L1/lu_solve.md) + `linear_combination` + `dot`; the **Schur-form pipeline is firm** (positive `deflated_solve` site `nleps.cpp:505-537`), the **bare-Galerkin core** (`S = I`) is the constructive sub-part (literature + negative anchor, promotion-gated on a positive Palace Galerkin-deflation site). The cycle-023 [`nleps_deflated_solve`](../L1/nleps_deflated_solve.md) landing **confirmed (did not change)** the partly-constructive status — the bare `(XᴴX)⁻¹` Galerkin core appears only Schur-wrapped, never standalone. Over-unification guard: `deflate` is NOT `orthogonalize` (`orthogonalize` = `deflate` at `gram = I`; the `(XᴴX)⁻¹` Gram solve is load-bearing). (3) [`eigsolve`](./eigsolve.md) (firm cycle-023 wave-1) — **chain-step-2** of the eigsolve prerequisite chain (L1-firm c022 → **this L2 entry** → L3-backfill); the **named shift-invert spectral-transform composition** `apply_shift_invert = apply_linop(M) ▷ ksp_solve((K − σM)⁻¹)`, the first L2 named composition whose direct constituent is itself a constructed-solver composition. A **partial-opening** named composition: the per-step *body* is Palace-authored and opened, but the eigen-iteration *fold* is opaque-library-owned (SLEPc `EPSSolve` / ARPACK RCI) and named by role only — the inverse decomposition from [`ksp_solve`](./ksp_solve.md) (whose fold IS opened). This is the load-bearing reason the L3 backfill landed `partial-obstruction` (cycle-024; chain-step-3 complete — see [`L3/eigsolve`](../L3/eigsolve.md)).
- **Cycle-041 BLAS-1-floor cohort (the first L2-floor-under-L3 slice; firm 9 → 12).** Three identity-in-form **floor** entries landed under the 2026-05-31 foundation-first directive `l2-floor-under-l3-blas1-cohort`, raising the firm cohort **9 → 12** (partly-constructive `deflate` unchanged at 1). These are the **first L2-floor-under-L3 entries**: each gives a firm L3 BLAS-1 leaf (backfilled cycle-011) a *present adjacent same-named L2 parent* per **Identity-lowerings still require both L levels**, rather than the L3 leaf skipping a layer down to L1. (1) [`dot`](./dot.md) (firm cycle-041 D1) — the conjugation-axis **leaf-of** `inner_product` (the plain `M = I` Hermitian / symmetric member), a thin identity-in-form floor whose laws are inherited unchanged from the firm L1 leaf; **NOT merged** into the fold-parent (the codomain/fold do-NOT-merge boundary is load-bearing). (2) [`nrm2`](./nrm2.md) (firm cycle-041 D2) — a **consumer-of** `inner_product` (`√ ∘ abs ∘ inner_product` at `y=x`), **NOT a fold member**; the fusion rotation is a no-op (`linalg::Norml2` is already the one-line unfolded composition) and the `std::abs` defensive guard is preserved as an explicit load-bearing numerical claim. (3) [`scal`](./scal.md) (firm cycle-041 D3) — the arity-1 **member-of** `linear_combination` (`scal(α,x) = linear_combination [(α,x)]`), **cited NOT merged**; firm-on-positive-structure (syntactic-identity laws on the small fully-present `operator*=` surface). The companion adjacent thin-identity themes landed the same cycle (L2>L1: `dot-leaf-identity` / `nrm2-fold-specialization` / `scal-fold-specialization`; L3>L2: `dot-body-identity` / `nrm2-body-identity` / `scal-body-identity`).
  - **LOAD-BEARING META-PHASE SIGNAL — leaf-vs-fold design fork (`dot-l2-leaf-floor-vs-fold-only-design`; for the batch-12 meta-phase, post-c042).** Wave-1 surfaced a **contradiction between two co-dispatched harvesters**: D1 built `L2/dot` as a same-named conjugation-axis **leaf floor** of `inner_product` (the **(b)** realization — a standalone `dot` chapter, cited as leaf-of, not merged); D2 argued the opposite — that the L2 inner-product surface should be **ONLY** the `inner_product` fold, with **NO `dot` leaf at L2** (the **(a) fold-only** reading), flagging the per-leaf L2 floor as arguably redundant with the fold-cohort vocabulary. **All six cycle-041 entries (the three floors + their six themes) presuppose the (b) "same-named floor" realization.** The batch-12 meta-phase must **ratify or adjust** this design before the cohort is treated as stable. *If it adopts the (a) fold-only reading,* the leaf floors (`dot` certainly; `scal` as the arity-1 member; `nrm2` is unaffected on the fold question since it consumes the fold either way, but its L2 *floor* rides the same `l2-floor-under-l3-blas1-cohort` decision) and their adjacent themes **re-anchor to the fold-parents**: the L2>L1 leaf-identity edges fold into `inner-product-fold-specialization` / `linear-combination-fold-specialization`, and the L3>L2 body-identity edges re-point their L2 RHS from a same-named leaf to the fold-parent. This is upstream of the whole cohort; surfaced here in the L2 Part overview so a reader navigating the floor cohort sees the design is provisional. (Recorded by D1/D2/D4/D5/D6 in their §Open-questions; consolidated as the batch-12 meta-phase OQ.)
  - **Slug-naming inconsistency within the L2>L1 cohort (for the meta-phase to normalize).** The L2>L1 `dot` theme is `dot-leaf-identity` (D4 deliberately adjusted from the dispatch-proposed `dot-fold-specialization`, on the reasoning that the `-fold-specialization` suffix names a *fold→leaf dispatch* and would mis-name an identity-leaf-lowering + collide with the existing `inner-product-fold-specialization` whose RHS already IS `L1/dot`), while the `nrm2` and `scal` L2>L1 themes use `-fold-specialization` (`nrm2-fold-specialization`, `scal-fold-specialization`) for sibling-naming continuity — even though `nrm2` is a *consumer* (not a fold member) and `scal`'s edge is the degenerate arity-1 *single-term shadow* (no dispatch). The three L3>L2 themes are consistently `-body-identity`. The cohort's L2>L1 naming is therefore split (`-leaf-identity` vs `-fold-specialization`) for three structurally-similar thin-identity edges. Flagged for the batch-12 meta-phase to normalize the cohort naming (candidate: a uniform `-leaf-identity` / `-body-identity` pairing, since none of the three L2>L1 edges is actually a fold-dispatch).
```

### 2. `book/src/L2-L1/index.md`

**(2a) §Vocabulary-cohort — append the three new firm thin-identity floor-edge bullets.** Anchor
on the last existing "Firm at L2>L1" bullet (`incremental-least-squares-composition-lowering`),
immediately before the "Partly-constructive at L2>L1" header; append the three floor-edge bullets
after it (as a labelled sub-group).

```edit:book/src/L2-L1/index.md
- `incremental-least-squares-composition-lowering` — running-QR / Givens-stream fan-down `replay ▷ generate ▷ apply ▷ apply_rhs` ▷ back-solve; FIXED sub-step sequence (replay-before-generate non-commutative load-bearing); two parametric axes `basis_kind ∈ {V, Z}` + `variant ∈ {real, complex}`.

**Partly-constructive at L2>L1** (firm Schur-form pipeline + a constructive bare-Galerkin sub-part with a stated promotion condition):
```

```edit:book/src/L2-L1/index.md
- `incremental-least-squares-composition-lowering` — running-QR / Givens-stream fan-down `replay ▷ generate ▷ apply ▷ apply_rhs` ▷ back-solve; FIXED sub-step sequence (replay-before-generate non-commutative load-bearing); two parametric axes `basis_kind ∈ {V, Z}` + `variant ∈ {real, complex}`.

*Identity-in-form BLAS-1-floor edges (cycle-041; the L2>L1 thin-identity edges of the new same-named L2 floors `dot`/`nrm2`/`scal`; all fusion content deferred to the fold-parents):*

- `dot-leaf-identity` — the L2 `dot` leaf-floor lowers to the L1 `dot` primitive identity-in-form on the signature; all L2-layer fusion deferred to the fold-parent `inner-product-fold-specialization` (no leaf-unique fusion surplus). Slug `-leaf-identity` (NOT `-fold-specialization`): the edge is an identity-leaf-lowering, not a fold→leaf dispatch.
- `nrm2-fold-specialization` — the L2 `nrm2` floor lowers to the single L1 `nrm2` leaf; the BLAS-1-leaf **consumer** sibling of `inner-product-fold-specialization` (`nrm2 = √ ∘ abs ∘ inner_product` at `y=x`, NOT a fold member; no dispatch / no decomposition / no buffer); `√`/`abs` post-steps drop below L1 resolution, `std::abs` guard preserved-as-claim at L2 → absorbed-by-non-negativity-claim at L1.
- `scal-fold-specialization` — the L2 `scal` floor lowers to the L1 `scal` leaf; the degenerate **arity-1 single-term shadow** of `linear-combination-fold-specialization` (no arity dispatch, no pinned-summation-order residue — one term ⇒ one rounding, value+bit-exact); arity-1 fold member cited NOT merged.

**Partly-constructive at L2>L1** (firm Schur-form pipeline + a constructive bare-Galerkin sub-part with a stated promotion condition):
```

**(2b) §Working Notes — prepend the cycle-041 floor-edge cohort to the cohort-growth log (carries
the firm tally 7 → 10).** Anchor on the existing cohort-growth log bullet; replace its lead clause
to prepend the new cohort entry (most-recent-first, per the log's stated ordering).

```edit:book/src/L2-L1/index.md
- Cohort growth log (most-recent first): `incremental-least-squares-composition-lowering` firm cycle-028 (closes the L2 `l2-named-composition-lifts` lowering side); `eigsolve-spectral-transform-composition` + `gram-fold-specialization` firm cycle-022/023 (eigsolve chain-step-2 + Gram fold-lift); `deflate-composition-lowering` partly-constructive cycle-022 (first L2>L1 partly-constructive entry); `orthogonalize-composition-lowering` firm cycle-019; `inner-product-fold-specialization` + `linear-combination-fold-specialization` firm cycle-018/019 (the variadic-fold unification); `chebyshev-iteration-fusion` firm cycle-013 (first L2-L1 chapter).
```

```edit:book/src/L2-L1/index.md
- Cohort growth log (most-recent first): `dot-leaf-identity` + `nrm2-fold-specialization` + `scal-fold-specialization` firm cycle-041 (the BLAS-1-floor-edge cohort — the L2>L1 thin-identity edges of the new same-named L2 floors `dot`/`nrm2`/`scal`, firm 7 → 10; all fusion deferred to the fold-parents, all identity-in-form on the primitive; **presuppose the (b) leaf-floor design realization — under batch-12 meta-phase adjudication, see §"Design fork" below**); `incremental-least-squares-composition-lowering` firm cycle-028 (closes the L2 `l2-named-composition-lifts` lowering side); `eigsolve-spectral-transform-composition` + `gram-fold-specialization` firm cycle-022/023 (eigsolve chain-step-2 + Gram fold-lift); `deflate-composition-lowering` partly-constructive cycle-022 (first L2>L1 partly-constructive entry); `orthogonalize-composition-lowering` firm cycle-019; `inner-product-fold-specialization` + `linear-combination-fold-specialization` firm cycle-018/019 (the variadic-fold unification); `chebyshev-iteration-fusion` firm cycle-013 (first L2-L1 chapter).
- **Design fork (`dot-l2-leaf-floor-vs-fold-only-design`; load-bearing batch-12 meta-phase signal).** The three cycle-041 floor-edge themes presuppose the **(b) same-named leaf-floor** realization of the L2 BLAS-1 surface (a standalone `dot`/`scal` L2 chapter, cited as leaf-of / member-of the fold-parents but NOT merged; `nrm2` a consumer-of). Wave-1 D2 argued the **(a) fold-only** reading (no `dot` leaf at L2 — the L2 inner-product surface is only the `inner_product` fold). If the meta-phase adopts (a), `dot-leaf-identity` dissolves into `inner-product-fold-specialization`'s conjugation dispatch and `scal-fold-specialization` into `linear-combination-fold-specialization`'s arity-1 row; the `nrm2` edge is unaffected on the fold question (it consumes the fold either way) but its LHS floor rides the same `l2-floor-under-l3-blas1-cohort` decision. Also flagged: the L2>L1 cohort slug split (`dot-leaf-identity` vs `nrm2`/`scal` `-fold-specialization`) for three structurally-similar identity edges — for the meta-phase to normalize.
```

### 3. `book/src/L3-L2/index.md`

**(3a) §Theme list context note — none (the three D4/D5/D6 theme-list rows are appended by the
producers).** This index had only a §Theme-list table + a thin §Working-Notes; with ≥3 firm
themes now it crosses the Vocabulary-cohort threshold, so I PROMOTE the subsection in (3b).

**(3b) §Working Notes — replace the single thin Working-Notes bullet with a Vocabulary-cohort
subsection (firm 2 → 5) + the cohort-growth note + the coverage-gap progress note + the design
fork.** Anchor on the entire existing §Working Notes block (one bullet) and replace it.

```edit:book/src/L3-L2/index.md
## Working Notes

- Negative-result entries (L3 form for which no L2 decomposition is meaningful — rare, mostly definitional) appear here too.
```

```edit:book/src/L3-L2/index.md
## Vocabulary cohort

**Firm at L3>L2** (lowering structure fully recognized; the iteration rotation between the L3 whole-tensor form and the L2 primitive-composition form is exhaustively cited):

- `krylov-step-body-identity` — identity-in-form on the kernel **body** (the five-primitive-group let-chain), with two surface adjustments at the **wrapper** (`(op, K, s)` → `IterState` consolidation + outer-loop-to-driver-by-role dissolution).
- `ksp-solve-outer-driver` — the **substantive / non-identity** driver complement of the kernel-body identity theme: the L3 `iterate_while_L3` tail recursion over `krylov-step` (carrying the outer-loop `sequential-obstruction`) lowers to the L2 outer-driver-by-role composition (iteration view erased; obstruction shadowed to the §"Algebraic laws" non-laws). `kernel-identity + driver-non-identity = the full per-solver L3>L2 story`.

*Identity-in-form BLAS-1-leaf body edges (cycle-041; the L3>L2 thin-identity edges of the BLAS-1 leaves whose L2 floors landed this cycle; all the leaf-primitive analogue of `krylov-step-body-identity` with NO wrapper rotation — the leaf has no `(op, K, s)` tuple and no outer loop):*

- `dot-body-identity` — the L3 whole-tensor `dot` reduction lowers to the L2 same-named leaf-floor identity-in-form on the body; `dot` is L3-native by signature shape (no element loop), so the iteration rotation is already done at the signature level.
- `nrm2-body-identity` — the L3 whole-tensor `nrm2` norm lowers to the L2 `√ ∘ abs ∘ inner_product` consumer floor; the only textual change is the inner-reduction name (`dot` leaf at L3 → `inner_product` fold at the diagonal at L2) + the surfacing of the `abs` guard as an explicit L2 claim.
- `scal-body-identity` — the L3 whole-tensor `scal` field operation lowers to the L2 base scalar-vector-multiply floor leaf (arity-1 fold member); the body IS the identity, there is no wrapper to rotate.

## Working Notes

- Negative-result entries (L3 form for which no L2 decomposition is meaningful — rare, mostly definitional) appear here too.
- **Cohort growth + coverage-gap progress (firm 2 → 5; `l3-l2-rotation-theme-coverage-gap` 2-of-18 → 5-of-18).** Cycle-041 landed the first three BLAS-1-leaf L3>L2 thin-identity themes (`dot-body-identity` / `nrm2-body-identity` / `scal-body-identity`), each the leaf-primitive analogue of the firm `krylov-step-body-identity` (cycle-007/009) but strictly simpler — a single leaf, no wrapper to rotate. This **begins closing** the `l3-l2-rotation-theme-coverage-gap` plan item (the iteration-rotation rewrite — the defining content of the L3 layer — was documented for only 2 of 18 L3 entries; now 5 of 18, with 13 still relying on inline identity annotations). The remaining gap splits into **thin-identity** edges (the rest of the BLAS-1 / identity-in-form L3 cohort) and **substantive** edges (`chebyshev`, `eigsolve` `partial-obstruction`, `orthogonalize` MGS-vs-CGS) — author thin where identity-in-form, firm-substantive where the rotation carries real content.
- **Design fork (`dot-l2-leaf-floor-vs-fold-only-design`; load-bearing batch-12 meta-phase signal).** The three cycle-041 body-identity themes presuppose the **(b) same-named L2 leaf-floor** realization of the BLAS-1 surface (their L2 RHS is a same-named `dot`/`nrm2`/`scal` floor). Wave-1 D2 argued the **(a) fold-only** reading. If the meta-phase adopts (a), each theme's L2 RHS re-points from a same-named leaf to the fold-parent (`dot`/`nrm2` → `inner_product`; `scal` → `linear_combination`), weakening the "identity" claim (a same-named leaf → a differently-named fold-parent is a weaker identity). Surfaced for the meta-phase; the themes are self-coherent under the (b) reading they are built on.
```

## Count-ownership confirmation (mandatory)

Per the dispatch directive and friction-ledger `parallel-blind-shared-index-count-divergence`,
I am the **SOLE count-owner** this cycle for all three consolidated tallies. D1–D6 each appended
ONLY their own non-aggregate dep-map / theme-list rows + SUMMARY registrations and explicitly
deferred every consolidated tally to me (confirmed in each report's "Count-ownership note" —
D1 §"Count-ownership note (mandatory)", D2 §"Open questions" "L2 index intro / firm-count tally
NOT touched", D3 §"Count-ownership note (mandatory, per dispatch)", D4/D5/D6 §"COUNT-OWNERSHIP"
notes). This report is the SINGLE authoritative write of:

- `book/src/L2/index.md` §Vocabulary-cohort "Firm at L2" sub-group + §Semantics third motif + §Working-Notes cohort note (firm **9 → 12**).
- `book/src/L2-L1/index.md` §Vocabulary-cohort floor-edge sub-group + §Working-Notes cohort-growth-log prepend (firm **7 → 10**).
- `book/src/L3-L2/index.md` §Vocabulary-cohort (newly promoted) + §Working-Notes (firm **2 → 5**; `l3-l2-rotation-theme-coverage-gap` 2-of-18 → 5-of-18).

I did NOT touch any dep-map / theme-list ROW (those are the producers' — applied from D1–D6), nor
any operator/theme chapter body, nor SUMMARY.md (registered by the producers). My edits are
confined to the three indices' orientation prose (motif / cohort / working-notes) + the three
consolidated counts. **The post-cohort totals count ALL six co-dispatched landings named in the
dispatch prompt, not only the entries I personally touched** (per the count-ownership convention).

## Supporting evidence

**Operators / themes landed this cycle (the cohort I am tallying):**

- L2 floors (D1–D3 harvesters, all `firm`): `dot` (leaf-of `inner_product`), `nrm2` (consumer-of `inner_product`), `scal` (member-of `linear_combination`). Sources: `reports/2026-06-01T051607Z-cycle-041-harvester-L2-{dot,nrm2,scal}/CYCLE.md`.
- L2>L1 themes (D4–D6 abstractors, all `firm`): `dot-leaf-identity`, `nrm2-fold-specialization`, `scal-fold-specialization`. Sources: `reports/2026-06-01T051607Z-cycle-041-abstractor-{dot,nrm2,scal}-themes/CYCLE.md`.
- L3>L2 themes (D4–D6 abstractors, all `firm`): `dot-body-identity`, `nrm2-body-identity`, `scal-body-identity`. Same sources.

**Pre-cycle index state (read on-disk this invocation, the source of truth for the tallies):**

- `book/src/L2/index.md` — §Vocabulary-cohort "Firm at L2" = 9 bullets (`krylov-step`, `chebyshev-iteration`, `linear_combination`, `inner_product`, `orthogonalize`, `ksp_solve`, `gram`, `incremental-least-squares`, `eigsolve`) + 1 partly-constructive (`deflate`); dep-map table = 10 rows (9 firm + `deflate`). §Semantics two motifs (named-compositions, fold-cohorts). §Working-Notes batch-6 cohort note is the last line (my (1c) anchor).
- `book/src/L2-L1/index.md` — §Theme-list = 8 rows (7 firm + `deflate-composition-lowering` partly-constructive); §Vocabulary-cohort "Firm at L2>L1" = 7 bullets + 1 partly-constructive; §Working-Notes cohort-growth-log single bullet (my (2b) anchor).
- `book/src/L3-L2/index.md` — §Theme-list = 2 rows (`krylov-step-body-identity`, `ksp-solve-outer-driver`, both firm); §Working-Notes = 1 bullet (negative-result note); NO Vocabulary-cohort subsection yet (below the ≥3 threshold pre-cycle — promoted in (3b) now that 5 firm exist).

**Cross-references to adjacent layers:** the L2 floors rest on the firm L1 BLAS-1 leaves (`L1/dot`
cycle-002, `L1/nrm2` cycle-003, `L1/scal` cycle-004) below and floor the firm L3 BLAS-1 cohort
(`L3/dot`/`L3/nrm2`/`L3/scal`, all cycle-011) above; the L2>L1 + L3>L2 themes are the adjacent-edge
rotations between those present chapters. The L3>L2 progress is tracked against the
`l3-l2-rotation-theme-coverage-gap` plan item (`scaffolding/priorities.md:62`, `roadmap.md:116`):
2-of-18 → 5-of-18.

**Anchor verification (this invocation):** all seven `[old]` anchor blocks were confirmed verbatim
against on-disk source — L2 (1a/1b/1c), L2-L1 (2a/2b), L3-L2 (3b) — via `sed`/`grep` exact-match
reads before emitting. None overlap; each is uniquely matched in its file.

## Open questions / caveats

- **LOAD-BEARING META-PHASE SIGNAL — `dot-l2-leaf-floor-vs-fold-only-design` (NEW OQ, batch-12 meta-phase, post-c042).** The entire cycle-041 BLAS-1-floor cohort (3 floors + 6 themes) presupposes the **(b) same-named leaf-floor** realization. Wave-1 D1 and D2 reached **contradictory** conclusions: D1 built `L2/dot` as a standalone same-named leaf-floor of `inner_product`; D2 argued the L2 inner-product surface should be ONLY the `inner_product` fold (no `dot` leaf at L2). The meta-phase must ratify or adjust. If it adopts (a) fold-only: the `dot`/`scal` leaf floors + their adjacent themes re-anchor to the fold-parents (`dot-leaf-identity` → `inner-product-fold-specialization`; `scal-fold-specialization` → `linear-combination-fold-specialization`'s arity-1 row; the L3>L2 RHSs re-point to the folds); `nrm2` is unaffected on the fold question (consumer either way) but its L2 floor rides the same `l2-floor-under-l3-blas1-cohort` decision. Surfaced PROMINENTLY in all three index §Working-Notes (L2 (1c), L2-L1 (2b), L3-L2 (3b)). **Recommend the integrator file this as OQ `dot-l2-leaf-floor-vs-fold-only-design`, cross-linked to the wave-1 D1 + D2 reports + D4/D5/D6 design-presupposition notes.** (Capture, not resolve — the design decision is upstream of D7's scope.)

- **Slug-naming inconsistency in the L2>L1 cohort (for the meta-phase to normalize).** The L2>L1 `dot` theme is `dot-leaf-identity` (D4 deliberately adjusted from `dot-fold-specialization`) while `nrm2`/`scal` use `-fold-specialization`. All three are structurally similar thin-identity edges; none is actually a fold-dispatch (the `nrm2` edge is a consumer-lowering, the `scal` edge a degenerate arity-1 single-term shadow). The three L3>L2 themes are consistently `-body-identity`. Candidate normalization: a uniform `-leaf-identity` (L2>L1) / `-body-identity` (L3>L2) pairing. D5's own §Open-questions raises the same point (suggests `nrm2-norm-consumer-identity` or `nrm2-body-identity` symmetric with its L3>L2 sibling). Flagged for the batch-12 meta-phase; a rename is a follow-up (theme bodies are slug-agnostic), NOT a D7 edit.

- **Build-ordering dependency (status downgrade contingency).** My three tallies assume all nine landing chapters integrate `firm` (confirmed from their proposed-changes `## Status` lines — see §On-disk status verification). If `integrator-per-report` or `repairer` downgrades any of the six producer reports during application (not expected — all are clean identity-in-form / firm-on-positive-structure entries), the corresponding tally needs a decrement. The integrator applies D1–D6 (rows) before / alongside D7 (counts) in the wave-3 serial sequence; if a downgrade happens, the count edit should be reconciled at `integrator-finalize` against the actually-landed `## Status` lines. (Standard cross-report count dependency; flagged for completeness, not a defect.)

- **L3-L2 Vocabulary-cohort promotion (first time at this index).** This index crossed the ≥3-firm threshold this cycle (2 → 5), so I PROMOTED a §Vocabulary-cohort subsection into it per the role-spec "Promote this subsection format into L2, L3, and L4 intros when each reaches ≥3 firm operators." The subsection splits the 5 firm themes into the 2 pre-existing (`krylov-step-body-identity`, `ksp-solve-outer-driver`) + the 3 new BLAS-1-leaf body edges. The index has no queued/rough-in themes, so per the role-spec the split would normally be skipped (firm-only) — but the labelled sub-grouping (substantive `krylov`/`ksp` driver-kernel pair vs the thin-identity BLAS-1-leaf cohort) is the useful orientation distinction here, mirroring the L2 + L2-L1 floor sub-groups. If a future pass prefers the firm-only-skip reading, the subsection can collapse back to the theme-list — low-stakes.

- **L3 dep-map row-count vs `l3-l2-rotation-theme-coverage-gap` "18" denominator (tracking note).** My L3>L2 progress note cites "5-of-18" from the plan-item tracking expression (`priorities.md:62`, `roadmap.md:116`). I did NOT re-count the L3 index's 18 entries this invocation (out of scope — that denominator is the plan-item's, maintained by the planner/meta-phase). If the L3 entry count has drifted from 18 since the plan item was written, the "5-of-18" should track the planner's current denominator at finalize. Flagged so the integrator uses the live denominator if it has moved.

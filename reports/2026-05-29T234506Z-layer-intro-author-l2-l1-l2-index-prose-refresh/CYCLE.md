---
agent: layer-intro-author
invoked_at: 2026-05-29T234506Z
scope: L2-L1 + L2 Part-overview prose refresh (cohort + queue re-sync after cycle-026/028 firm landings)
status: pending
integrated_at: 2026-05-30T004013Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-029 (staging row 6). PURE PROSE/NAVIGATIONAL refresh — NO dep-map rows, NO Status lines, NO chapter-body content edited. L2-L1/index.md: appended Vocabulary-cohort subsection (7 firm + 1 partly-constructive) between dep-map and Working Notes + cohort-growth-log bullet. L2/index.md: refreshed Named-compositions motif from 2-exemplar to 4-exemplar framing; removed now-empty Queued at L2 (stub) subsection; added incremental-least-squares + eigsolve to Firm at L2 sub-list (closing the stale-by-omission gap the critic flagged); refreshed stub-queue bullet to l2-named-composition-lifts-closed. Counts re-verified post-apply: 8 L2-L1 dep-map rows + 10 L2 dep-map rows match prose claims exactly. 1 pre-existing citecheck MISS at L2/index.md:70 (spec/slices/chebyshev.md:354-362 historical-provenance bullet narrating a c015 absorption — semantically intentional, NOT introduced this report). 0 OQs promoted (all 3 report §Open-questions items confirmed by critic+repairer as not-a-defect / framing-choice). NO repair needed (overall_status: ready)."
---

# CYCLE: L2-L1 + L2 index prose refresh

## Summary

Re-sync the navigational prose of two Part overviews to the on-disk dep-map state after the cycle-026 (`L2/incremental-least-squares` firm) and cycle-028 (`L2>L1/incremental-least-squares-composition-lowering` firm) landings:

1. **`book/src/L2-L1/index.md`** — add a **Vocabulary-cohort subsection** to the Part overview. The dep-map now carries **8 themes (7 firm + 1 partly-constructive)** which crosses the role-spec threshold for the cohort split (≥3 firm + a queued / partly-constructive entry). The existing prose has no count claim to "fix" textually, but it lacks the cohort orientation block prescribed by the layer-intro-author template; without the block, a reader hits an 8-row dep-map cold. The deflate-composition-lowering partly-constructive row is the queue entry that motivates the split.

2. **`book/src/L2/index.md`** — three pieces of stale prose where `incremental-least-squares` is still described as "stub" / "queued" but is firm on-disk as of cycle-026:
   - Line 21 (Semantics overlay, named-compositions motif): "The stub `incremental-least-squares` (GMRES running-QR / Givens stream) is the queued second named composition."
   - Lines 44-46 (Vocabulary cohort, "Queued at L2" sub-section): the entire sub-section lists only `incremental-least-squares (stub)` — now empty after promotion; sub-section should be removed (no remaining stubs at L2).
   - Lines 78-79 (Working Notes): "One stub queued for harvester refinement (the cohort's other 2026-05-28 stub, `ksp_solve.md`, landed firm cycle-021 — see the firm-pair note below)" + the bullet that lists `incremental-least-squares.md` as the queued second named-composition.

Verified counts on-disk against the dep-maps (the source of truth). No structural edits (dep-map rows, status lines, chapter content) — prose / navigation only.

## Proposed changes

### Change 1 — L2-L1 Part overview: add Vocabulary-cohort subsection

Insert a new subsection between the existing "Theme list" and "Working Notes" sections. The L2-L1 layer's first 3 firm landings (cycles 013/018/019) didn't motivate the cohort split — only `chebyshev-iteration-fusion` was firm with no queue. The current state (7 firm + 1 partly-constructive after cycle-028) crosses both halves of the threshold.

```edit:book/src/L2-L1/index.md
[old]: | [incremental-least-squares-composition-lowering](./incremental-least-squares-composition-lowering.md) | `L2/incremental-least-squares` (firm, cycle-026) | `L1/back_solve` (firm leaf, cycle-027; terminal back-solve) + `concepts/givens_generate`/`givens_apply` (firm; de-fused 4-sub-step Face 2) + `L2/linear_combination` (firm; back-solve reconstruction) + `ls_update_column` *(forthcoming column-streaming leaf; plain-text forward-ref)* | firm *(algebraic; running-QR fan-down `replay▷generate▷apply▷apply_rhs`▷back-solve; FIXED sub-step sequence — replay-before-generate non-commutative load-bearing; two parametric axes `basis_kind∈{V,Z}` + `variant∈{real,complex}`; reduction-path = rotation-ordering + LAPACK scaling, NO MPI collective; terminal back-solve = firm `back_solve` leaf, NOT general `trsv` (separately blocked))* |

## Working Notes

- Themes here are heavy with optimization-trick unfolding (transparent performance tricks like fusion, tiling, packing; load-bearing numerical tricks preserved).
[new]: | [incremental-least-squares-composition-lowering](./incremental-least-squares-composition-lowering.md) | `L2/incremental-least-squares` (firm, cycle-026) | `L1/back_solve` (firm leaf, cycle-027; terminal back-solve) + `concepts/givens_generate`/`givens_apply` (firm; de-fused 4-sub-step Face 2) + `L2/linear_combination` (firm; back-solve reconstruction) + `ls_update_column` *(forthcoming column-streaming leaf; plain-text forward-ref)* | firm *(algebraic; running-QR fan-down `replay▷generate▷apply▷apply_rhs`▷back-solve; FIXED sub-step sequence — replay-before-generate non-commutative load-bearing; two parametric axes `basis_kind∈{V,Z}` + `variant∈{real,complex}`; reduction-path = rotation-ordering + LAPACK scaling, NO MPI collective; terminal back-solve = firm `back_solve` leaf, NOT general `trsv` (separately blocked))* |

## Vocabulary cohort

**Firm at L2>L1** (lowering structure fully recognized; exhaustively cited; algebraic-laws complete):

- `chebyshev-iteration-fusion` — three-term-recurrence ↔ scaled-polynomial-evaluation fusion (the load-bearing numerical re-association at the kernel boundary).
- `linear-combination-fold-specialization` — arity-dispatch fusion-selection across `scal` / `axpy` / `axpby` / `axpbypcz` + pinned summation order; the term-axis fold cohort.
- `inner-product-fold-specialization` — conjugation / element-type / weight dispatch across `dot` / `tdot` / `bilinear-form` + value-level conjugate-pair re-order + pinned reduction tree; the length-axis fold cohort (sibling of the term-axis fold, do-NOT-merge).
- `orthogonalize-composition-lowering` — `project ▷ subtract` named composition (`dot` ▷ `axpy`); the MGS / CGS / CGS2 variant-dispatch realized as `[dot, axpy]`-sequence selection + collective-shape disclosure.
- `gram-fold-specialization` — matrix-lift of `inner-product-fold-specialization` (the all-pairs double-loop materialization); per-cell conjugation / weight dispatch + `k²` independent per-cell reduction trees + symmetry-exploitation transparent note.
- `eigsolve-spectral-transform-composition` — two-stage shift-invert pipeline de-fusion `apply_linop(M) ▷ ksp_solve((K−σM)⁻¹) ▷ scale_untransform`; per-step body de-fused, eigen-iteration loop is opaque-library sequential-obstruction (out of theme scope).
- `incremental-least-squares-composition-lowering` — running-QR / Givens-stream fan-down `replay ▷ generate ▷ apply ▷ apply_rhs` ▷ back-solve; FIXED sub-step sequence (replay-before-generate non-commutative load-bearing); two parametric axes `basis_kind ∈ {V, Z}` + `variant ∈ {real, complex}`.

**Partly-constructive at L2>L1** (firm Schur-form pipeline + a constructive bare-Galerkin sub-part with a stated promotion condition):

- `deflate-composition-lowering` — `coords ▷ (schur-)solve ▷ back-project` reduction chain over `dot` + `gram` + `lu_solve` + `linear_combination` + `axpy`. The Schur fan-down is firm on positive site `nleps.cpp:533-535`; the Galerkin-core single-`lu_solve` fan-down is constructive on negative anchor + literature; gate = a positive bare-Gram-solve site (not closed).

## Working Notes

- Themes here are heavy with optimization-trick unfolding (transparent performance tricks like fusion, tiling, packing; load-bearing numerical tricks preserved).
- Cohort growth log (most-recent first): `incremental-least-squares-composition-lowering` firm cycle-028 (closes the L2 `l2-named-composition-lifts` lowering side); `eigsolve-spectral-transform-composition` + `gram-fold-specialization` firm cycle-022/023 (eigsolve chain-step-2 + Gram fold-lift); `deflate-composition-lowering` partly-constructive cycle-022 (first L2>L1 partly-constructive entry); `orthogonalize-composition-lowering` firm cycle-019; `inner-product-fold-specialization` + `linear-combination-fold-specialization` firm cycle-018/019 (the variadic-fold unification); `chebyshev-iteration-fusion` firm cycle-013 (first L2-L1 chapter).
```

### Change 2 — L2 Part overview: refresh named-compositions motif prose

```edit:book/src/L2/index.md
[old]: - **Named compositions** — a single Palace runtime-dispatched entry point unfolds into a canonical pipeline of L1 leaves under a named L2 surface. `orthogonalize` is the exemplar: it names the Gram-Schmidt `project ▷ subtract` composition (`dot` ▷ `axpy`), turning the opaque `gs_orthog ∈ {MGS, CGS, CGS2}` parameter into the visible per-variant batching/sequencing disclosed as the collective-shape residual axis. This is the level-(b)-absorbed `op.orthog` surface `krylov-step` folds. The stub `incremental-least-squares` (GMRES running-QR / Givens stream) is the queued second named composition.
[new]: - **Named compositions** — a single Palace runtime-dispatched entry point unfolds into a canonical pipeline of L1 leaves under a named L2 surface. Two firm exemplars (the cohort closed cycle-026): (i) `orthogonalize` names the Gram-Schmidt `project ▷ subtract` composition (`dot` ▷ `axpy`), turning the opaque `gs_orthog ∈ {MGS, CGS, CGS2}` parameter into the visible per-variant batching / sequencing disclosed as the collective-shape residual axis — the level-(b)-absorbed `op.orthog` surface `krylov-step` folds; (ii) `incremental-least-squares` names the GMRES / FGMRES running-QR / Givens-rotation-stream small-dense LS update — the `replay ▷ generate ▷ apply ▷ apply_rhs` ▷ terminal-back-solve pipeline with FIXED sub-step sequence (replay-before-generate non-commutative load-bearing) and the running residual `β = |s[j+1]|` as a free byproduct. The outer-driver `ksp_solve` (firm cycle-021) is the third named composition — wrapping the `krylov-step` kernel in the convergence-test / restart `iterate_while` fold — distinct from the first two by sitting one layer up (composes over `krylov-step` itself, not its L1 primitives). The shift-invert `eigsolve` (firm cycle-023) is the fourth — `apply_linop(M) ▷ ksp_solve((K−σM)⁻¹)` per-step body composed over a constructed inverse solver, with the eigen-iteration *fold* opaque-library-owned (the load-bearing reason its L3 backfill lands `partial-obstruction`).
```

### Change 3 — L2 Part overview: refresh Vocabulary cohort "Queued" subsection (now empty)

The "Queued at L2 (stub)" subsection is now empty — `incremental-least-squares` was its sole occupant and is firm cycle-026. Per role-spec ("Skip the subsection when the layer has only firm entries... or only rough-ins... — the split is only useful when both states coexist"), the subsection should be removed.

```edit:book/src/L2/index.md
[old]: **Queued at L2** (stub — claim-free placeholder awaiting `harvester` refinement):

- `incremental-least-squares` (stub) — GMRES running-QR / Givens-rotation-stream small-dense LS update; the queued second named-composition (sibling to `orthogonalize`).

## Operator dep-map
[new]: ## Operator dep-map
```

After this edit the Vocabulary-cohort subsection has two halves: "Firm at L2" (8 entries — unchanged) and "Partly-constructive at L2" (1 entry: `deflate` — unchanged). The cohort split remains motivated because `deflate` is partly-constructive, satisfying the role-spec rule that the split is useful when at least two maturity states coexist.

Also update the "Firm at L2" half to include `incremental-least-squares` as the 8th firm entry (currently the list shows 7 firm; the dep-map row at line 57 is firm cycle-026, so the cohort line is stale by omission):

```edit:book/src/L2/index.md
[old]: - `gram` — the **all-pairs `inner_product` fold** → `Matrix[k,k]`: the matrix-valued lift of the `inner_product` scalar fold, building the `k×k` Gram `XᴴX` from a `k`-column basis `X`. Hermitian + PSD (PD iff `X` full-rank); the incremental-Gram block law certifies the fold over columns. Consumed by `deflate` (the oblique-projection assembly that LU-solves the Gram). Firm cycle-022 (promoted from rough-in; all-pairs `inner_product` syntactic-identity laws on the positive Gram-build site `nleps.cpp:524-531`).

**Partly-constructive at L2** (firm structural decomposition + a constructive sub-part with a stated promotion condition):
[new]: - `gram` — the **all-pairs `inner_product` fold** → `Matrix[k,k]`: the matrix-valued lift of the `inner_product` scalar fold, building the `k×k` Gram `XᴴX` from a `k`-column basis `X`. Hermitian + PSD (PD iff `X` full-rank); the incremental-Gram block law certifies the fold over columns. Consumed by `deflate` (the oblique-projection assembly that LU-solves the Gram). Firm cycle-022 (promoted from rough-in; all-pairs `inner_product` syntactic-identity laws on the positive Gram-build site `nleps.cpp:524-531`).
- `incremental-least-squares` — the GMRES / FGMRES running-QR / Givens-stream small-dense LS update; the **second named composition** (sibling to `orthogonalize`) closing the `l2-named-composition-lifts` cohort. Running-QR fan-down `replay ▷ generate ▷ apply ▷ apply_rhs` with terminal `back_solve`; FIXED sub-step sequence (replay-before-generate non-commutative load-bearing); two parametric axes `basis_kind ∈ {V, Z}` + `variant ∈ {real, complex}`; running residual `β = |s[j+1]|` is a free byproduct. Firm cycle-026 (firm-on-positive-structure — running-QR stream + back-solve read in full in both GMRES and FGMRES arms).
- `eigsolve` — **shift-invert spectral-transform application** `apply_shift_invert = apply_linop(M) ▷ ksp_solve((K − σM)⁻¹)` (the per-step body the opaque-library eigen-iteration folds). Chain-step-2 of the eigsolve prerequisite chain (L1-firm c022 → this entry → L3-backfill); first L2 named composition whose direct constituent is itself a constructed-solver composition. The per-step body is opened; the eigen-iteration *fold* stays library-owned (SLEPc `EPSSolve` / ARPACK RCI) — the inverse decomposition from `ksp_solve` whose fold IS opened. Firm cycle-023 (firm-on-positive-structure).

**Partly-constructive at L2** (firm structural decomposition + a constructive sub-part with a stated promotion condition):
```

(Note: the cohort previously omitted `eigsolve` from the firm list too — same omission pattern as `incremental-least-squares`. The dep-map row at line 61 is firm cycle-023. Adding both in the same edit keeps the cohort in sync with the dep-map.)

### Change 4 — L2 Part overview: refresh Working Notes prose on the stub queue

```edit:book/src/L2/index.md
[old]: - **One stub queued for harvester refinement** (the cohort's other 2026-05-28 stub, `ksp_solve.md`, landed firm cycle-021 — see the firm-pair note below):
  - [`incremental-least-squares.md`](./incremental-least-squares.md) — the GMRES outer driver's running-QR / Givens-stream small-dense kernel, currently a concept page (`concepts/incremental-least-squares`). The queued second **named-composition** (sibling to `orthogonalize`). Plan item `l2-named-composition-lifts`.
[new]: - **The `l2-named-composition-lifts` plan item is closed** (cycle-026; both queued named-compositions now firm). The 2026-05-28 stub cohort has fully drained: [`ksp_solve.md`](./ksp_solve.md) landed firm cycle-021 (outer-driver wrap; see the firm-pair note below), and [`incremental-least-squares.md`](./incremental-least-squares.md) landed firm cycle-026 (running-QR / Givens-stream small-dense LS update; sibling to `orthogonalize`). No L2 stubs remain.
```

## Supporting evidence

- **L2-L1 dep-map count** verified on-disk at `book/src/L2-L1/index.md:11-20` — 8 dep-map rows, 7 firm + 1 partly-constructive:
  - 7 firm: `chebyshev-iteration-fusion`, `linear-combination-fold-specialization`, `inner-product-fold-specialization`, `orthogonalize-composition-lowering`, `gram-fold-specialization`, `eigsolve-spectral-transform-composition`, `incremental-least-squares-composition-lowering`.
  - 1 partly-constructive: `deflate-composition-lowering`.
- **L2 dep-map count** verified on-disk at `book/src/L2/index.md:50-61` — 10 dep-map rows, 9 firm + 1 partly-constructive:
  - 9 firm: `krylov-step`, `chebyshev-iteration`, `linear_combination`, `inner_product`, `orthogonalize`, `incremental-least-squares`, `ksp_solve`, `gram`, `eigsolve`.
  - 1 partly-constructive: `deflate`.
  - (The Vocabulary-cohort `Firm at L2` sub-list at lines 30-38 currently shows only 7 firm — it is stale by omission of `eigsolve` and `incremental-least-squares`; Change 3 patches both omissions.)
- **On-disk status verification** for the two firm landings driving this refresh:
  - `book/src/L2/incremental-least-squares.md:376-378` — explicit `## Status` line reads `\`firm\``.
  - `book/src/L2-L1/incremental-least-squares-composition-lowering.md:414-416` — explicit `## Status` line reads `\`firm\``.
- **Cycle-028 finalize commit** `3319d88` ("cycle-028 integrate: L2>L1 firm 6→7 (+incremental-least-squares-composition-lowering, closes c027 D5 deferral)") — the landing that motivates this refresh.
- **Cycle-026 finalize commit** for `L2/incremental-least-squares` firm — the operator-side landing the L2 cohort prose missed.
- **Role-spec discipline followed**:
  - Verified counts against on-disk dep-maps; did NOT trust the dispatcher's "7 firm + 1 partly-constructive" without on-disk confirmation (the role-spec discipline "Survey chapter firmness from the on-disk `## Status`, NOT the cycle record"). The dispatcher's count happened to be correct for L2-L1; the discipline still applied.
  - No structural edits (dep-map rows, status lines, chapter content) — prose / navigation only.
  - The new L2-L1 Vocabulary-cohort subsection follows the role-spec template (firm / partly-constructive split, one-line semantic per entry).
  - The L2 "Queued at L2 (stub)" subsection is removed (role-spec: "Skip the subsection when the layer has only firm entries... or only rough-ins... — the split is only useful when both states coexist") — the L2 cohort retains the firm / partly-constructive split because `deflate` remains partly-constructive.

## Open questions / caveats

- **Cycle-007 firm not landed**: the cohort log in Change 1 mentions cycle-013 as the first L2-L1 chapter and doesn't enumerate cycle-014/015/016/017 — these cycles did not land L2-L1 themes (verified via `git log --oneline -- book/src/L2-L1/`; the cohort grew at cycles 013, 018, 019, 022, 023, 026, 028). Not an issue, just noting the gap is intentional (no themes promoted in those cycles).
- **`ls_update_column` plain-text forward-ref**: the cycle-028 firm theme row for `incremental-least-squares-composition-lowering` carries a plain-text forward-reference to `ls_update_column` (a forthcoming column-streaming L1 leaf). The Vocabulary-cohort entry in Change 1 reflects this as a property of the theme (the fan-down terminates at `back_solve` + concepts; column-streaming is the forthcoming leaf) — does not assert the forward-reference as firm. Consistent with the role-spec rough-in-rows-must-be-plain-text-when-anchor-missing convention.
- **`ksp_solve` placement in the L2 named-compositions motif**: in Change 2 I added `ksp_solve` as the "third named composition" and `eigsolve` as the "fourth" — extending the motif paragraph beyond the original two-exemplar shape. An alternative framing would be a separate "outer-driver compositions" sub-motif (since `ksp_solve` and `eigsolve` compose over constructed solvers, not L1 primitives). Going with the inline extension because the named-compositions motif paragraph is the natural home and the inline form keeps the L2 overview compact. The L2 Vocabulary-cohort `Firm at L2` list already treats them as peer firm L2 entries (lines 37-38 + the new entries from Change 3).
- **No L2-L1 lead-prose count claim to fix**: the dispatcher's prompt anticipated a stale "2 firm themes" string in the L2-L1 lead. The current L2-L1 lead is terse (Context paragraph only, no count claim) — see lines 1-8. The cohort subsection in Change 1 supplies the navigational orientation that the absent count would have provided. Flagging in case the dispatcher expected a literal-string fix rather than the subsection add (the subsection is the role-spec-prescribed shape).

---
agent: lifter
invoked_at: 2026-05-29T16:38:08Z
scope: L1 NLEPS-interior citation re-anchor — nleps_jacobian_action + nleps_eigenvalue_correction + vector.cpp:667→:668 sibling sweep
status: pending
inputs:
  - book/src/L1/nleps_jacobian_action.md
  - book/src/L1/nleps_eigenvalue_correction.md
  - book/src/L2/inner_product.md
  - book/src/L2-L1/inner-product-fold-specialization.md
  - reports/2026-05-29T151441Z-abstractor-nleps-jacobian-action-rotation/CYCLE.md (cycle-025 §Open-questions diagnosis)
  - reference/palace/palace/linalg/nleps.cpp (on-disk source of truth)
  - reference/palace/palace/linalg/vector.cpp (on-disk source of truth)
integrated_at: 2026-05-29T203000Z
integration_commit: 1de17ed
integration_notes: "Applied clean (cycle-026 dispatch-1). 23 surgical citation-drift swaps across nleps_jacobian_action.md (16), nleps_eigenvalue_correction.md (2), inner_product.md (1), inner-product-fold-specialization.md (4); both L1 entries stay firm. 3 OQs RESOLVED (jacobian-six-anchor, eigenvalue-two-anchor, vector.cpp:667→:668 sibling sweep); codemap +1 brace-drift OQ left open with second-cycle-confirmation clause for batch-7 meta-phase. Zero gate hits."

# CYCLE: Re-anchor NLEPS-interior L1 entries (citation-drift correction)

## Summary

A pure **mechanical citation re-anchor** of three drift clusters surfaced during cycle-025, all
caused by the `palace-codemap` MCP `read_range` being +1 behind on-disk on `nleps.cpp` brace
boundaries (the codemap merges the opening `{` of the `if (k > 0)` deflation block — on-disk
`nleps.cpp:659` — into the preceding comment line, shifting every codemap line from on-disk `:660`
onward by −1). No semantics, prose, structure, signatures, laws, or variant axes change — **only
the cited line numbers** are corrected to match the on-disk `reference/palace/` checkout, verified
anchor-by-anchor with `tools/citecheck/citecheck.py --anchor`. Three clusters:

1. **`book/src/L1/nleps_jacobian_action.md`** — six deflation-block constructs cited −1 from
   on-disk (codemap `:659-660`/`:661-662`/`:663`/`:664`/`:665`/`:666` → on-disk
   `:660-661`/`:662-663`/`:664`/`:665`/`:666`/`:667`). All `:649`–`:658`, `:668`, `:669`, `:378`,
   `:412` anchors precede the brace shift and are already correct (unchanged).
2. **`book/src/L1/nleps_eigenvalue_correction.md`** — the `while (it < nleps_it)` loop cited `:596`
   is on-disk `:590` (−6); the Armijo `alpha *= backtrack_factor` cited `:709` is on-disk `:712`
   (+3). (`:691`, `:708`, the `:688-714` block range, `:672-677` are correct — unchanged.)
3. **`vector.cpp:667→:668` sibling sweep** — the `MFEM_ASSERT(x.Size() == y.Size())` line is on-disk
   `:668` (`:667` is `static hypre::HypreVector X, Y;`). The −1 drift persists in
   `book/src/L2/inner_product.md:360` and **four** occurrences in
   `book/src/L2-L1/inner-product-fold-specialization.md` (`:59`, `:260`, `:403`, `:553` — the cycle-025
   OQ named `:59,260`; the sibling-sweep discipline corrects all four identical-drift occurrences).
   The enclosing range citation `vector.cpp:664-672` is correct on-disk and is **not** touched.

This is a re-anchor, not authorship: the source-of-truth is the on-disk file via `citecheck`, not
the codemap (which is the localization tool that drifted).

## Proposed changes

### Cluster 1 — `book/src/L1/nleps_jacobian_action.md` (six deflation-block anchors, −1 drift)

Citecheck confirmation for the six corrected on-disk anchors (all `[ok]`):
- `nleps.cpp:660-661 --anchor "w1 = T'(l) v1"` → ok (the two-line coupling comment)
- `nleps.cpp:662-663 --anchor 'auto A = BuildParSumOperator'` → ok (the re-scoped value pencil)
- `nleps.cpp:664 --anchor 'const Eigen::MatrixXcd S = eig'` → ok (the `S = λI − H` block)
- `nleps.cpp:665 --anchor 'const Eigen::VectorXcd Sv2 = S.fullPivLu().solve(v2)'` → ok (`S⁻¹·v₂`)
- `nleps.cpp:666 --anchor 'const ComplexVector XSv2 = MatVecMult(X, Sv2)'` → ok (`X·S⁻¹v₂`)
- `nleps.cpp:667 --anchor 'const ComplexVector XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2))'` → ok (`X·S⁻²v₂`)

(Drift evidence on the pre-correction numbers: `nleps.cpp:661 --anchor 'Scoping T(l)'` →
`[DRIFT] anchor at line 660, -1`; `nleps.cpp:667 --anchor '...XSSv2 = MatVecMult(X, S.fullPivLu...'`
is the corrected home for what the entry cited as `:666`.)

NOTE the standalone `:660` reference on entry line 77 (the formula fragment
`+ T'(l)XS v2 − T(l)XS^2 v2`) is ALREADY CORRECT on-disk — that fragment is on on-disk `:660` —
and is deliberately left unchanged. Only the *two-line comment-block* citation `:659-660`
re-anchors to `:660-661`.

```edit:book/src/L1/nleps_jacobian_action.md
[old]: Concretely (the source's own comment, `palace/linalg/nleps.cpp:659-660`):
[new]: Concretely (the source's own comment, `palace/linalg/nleps.cpp:660-661`):
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]:   A   = {1, λ, λ², 1}·{K, C, M, A2(|Im λ|)} = T(λ)        -- :661-662   (scoped here, see point 4)
  S   = λI − H                                            -- :663
  Sv2 = S⁻¹·v₂                                            -- :664
  XSv2  = X·(S⁻¹·v₂)                                      -- :665   linear_combination
  XSSv2 = X·(S⁻¹·(S⁻¹·v₂)) = X·S⁻²·v₂                     -- :666   linear_combination
[new]:   A   = {1, λ, λ², 1}·{K, C, M, A2(|Im λ|)} = T(λ)        -- :662-663   (scoped here, see point 4)
  S   = λI − H                                            -- :664
  Sv2 = S⁻¹·v₂                                            -- :665
  XSv2  = X·(S⁻¹·v₂)                                      -- :666   linear_combination
  XSSv2 = X·(S⁻¹·(S⁻¹·v₂)) = X·S⁻²·v₂                     -- :667   linear_combination
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]: The double `S⁻¹` solve (`Sv2 = S⁻¹v₂` at `:664`, then `S⁻¹·Sv2` at `:666`) materializes
[new]: The double `S⁻¹` solve (`Sv2 = S⁻¹v₂` at `:665`, then `S⁻¹·Sv2` at `:667`) materializes
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]: `A = BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM, A2n.get()}, true)` (`palace/linalg/nleps.cpp:661-662`) using the line-search-cached `A2n` (the `A2(|Im λ|)` operator carried across iterations). The source comment at `:659-660` explains the local scoping
[new]: `A = BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM, A2n.get()}, true)` (`palace/linalg/nleps.cpp:662-663`) using the line-search-cached `A2n` (the `A2(|Im λ|)` operator carried across iterations). The source comment at `:660-661` explains the local scoping
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]: Witnessed by the two `AddMult` accumulations (`palace/linalg/nleps.cpp:668-669`) over `XSv2 = X·S⁻¹v₂` (`:665`) and `XSSv2 = X·S⁻²v₂` (`:666`).
[new]: Witnessed by the two `AddMult` accumulations (`palace/linalg/nleps.cpp:668-669`) over `XSv2 = X·S⁻¹v₂` (`:666`) and `XSSv2 = X·S⁻²v₂` (`:667`).
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]: The dense `k×k` solves `S⁻¹·v₂` (`palace/linalg/nleps.cpp:664`) and `S⁻¹·(S⁻¹·v₂) = S⁻²·v₂` (`:666`), both `Eigen::fullPivLu().solve`.
[new]: The dense `k×k` solves `S⁻¹·v₂` (`palace/linalg/nleps.cpp:665`) and `S⁻¹·(S⁻¹·v₂) = S⁻²·v₂` (`:667`), both `Eigen::fullPivLu().solve`.
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]: the `MatVecMult(X, ·)` at `palace/linalg/nleps.cpp:665,:666` / `:329-347`)
[new]: the `MatVecMult(X, ·)` at `palace/linalg/nleps.cpp:666,:667` / `:329-347`)
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]: `S = λI[k] − H` is the `k×k` extended-block linearization (the same block as the residual / solve siblings); [`lu_solve`](./lu_solve.md) is the dense `k×k` factor-and-solve against it (`Eigen::fullPivLu().solve`, `palace/linalg/nleps.cpp:664,:666`)
[new]: `S = λI[k] − H` is the `k×k` extended-block linearization (the same block as the residual / solve siblings); [`lu_solve`](./lu_solve.md) is the dense `k×k` factor-and-solve against it (`Eigen::fullPivLu().solve`, `palace/linalg/nleps.cpp:665,:667`)
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]: the `A2n` operator caching (`:661-662` re-scoping) is an L1>L0 transparent-performance / scoping concern. Collapsed at L1.
[new]: the `A2n` operator caching (`:662-663` re-scoping) is an L1>L0 transparent-performance / scoping concern. Collapsed at L1.
```

Status-paragraph (line 130) — three sub-anchors drift (`:659-660` coupling comment → `:660-661`;
`S = λI − H` `:663` → `:664`; dense solves `:664,:666` → `:665,:667`; back-projections
`:665,:666` → `:666,:667`):

```edit:book/src/L1/nleps_jacobian_action.md
[old]: the deflation-coupling comment `w1 = T'(l) v1 + U'(l) v2 = T'(l) v1 + T'(l)XS v2 − T(l)XS^2 v2` at `:659-660`). Every constituent is read, not constructed: the divided-difference `A2'` is the positive `BuildParSumOperator({1/denom, −1/denom}, {opA2p, A2n})` (`:653-654`), the derivative pencil is `BuildParSumOperator({0, 1, 2λ, 1}, {opK, opC, opM, opAJ})` (`:655-656`), the big-space apply is `opJ->Mult(v, w)` (`:657`), the block `S = λI − H` (`:663`), the two dense solves `S.fullPivLu().solve` (`:664,:666`), the back-projections `MatVecMult(X, ·)` (`:665,:666`), and the two `AddMult` accumulations (`:668,:669`).
[new]: the deflation-coupling comment `w1 = T'(l) v1 + U'(l) v2 = T'(l) v1 + T'(l)XS v2 − T(l)XS^2 v2` at `:660-661`). Every constituent is read, not constructed: the divided-difference `A2'` is the positive `BuildParSumOperator({1/denom, −1/denom}, {opA2p, A2n})` (`:653-654`), the derivative pencil is `BuildParSumOperator({0, 1, 2λ, 1}, {opK, opC, opM, opAJ})` (`:655-656`), the big-space apply is `opJ->Mult(v, w)` (`:657`), the block `S = λI − H` (`:664`), the two dense solves `S.fullPivLu().solve` (`:665,:667`), the back-projections `MatVecMult(X, ·)` (`:666,:667`), and the two `AddMult` accumulations (`:668,:669`).
```

L1-vs-L0 paragraph (line 140) — the `k > 0` execution narrative; five sub-anchors drift
(value pencil `:661-662` → `:662-663`; `S = eig·I − H` `:663` → `:664`; `Sv2` `:664` → `:665`;
`XSv2` `:665` → `:666`; `XSSv2` `:666` → `:667`):

```edit:book/src/L1/nleps_jacobian_action.md
[old]: re-scopes the value pencil `A = BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM, A2n})` (`:661-662`), forms `S = eig·I − H` (`:663`), solves `Sv2 = S.fullPivLu().solve(v2)` (`:664`), back-projects `XSv2 = MatVecMult(X, Sv2)` (`:665`) and `XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2))` (`:666`), and accumulates `opJ->AddMult(XSv2, w, 1.0)` (`:668`) and `A->AddMult(XSSv2, w, -1.0)` (`:669`).
[new]: re-scopes the value pencil `A = BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM, A2n})` (`:662-663`), forms `S = eig·I − H` (`:664`), solves `Sv2 = S.fullPivLu().solve(v2)` (`:665`), back-projects `XSv2 = MatVecMult(X, Sv2)` (`:666`) and `XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2))` (`:667`), and accumulates `opJ->AddMult(XSv2, w, 1.0)` (`:668`) and `A->AddMult(XSSv2, w, -1.0)` (`:669`).
```

Evidence block (lines 152–156) — five per-line Evidence anchors drift:

```edit:book/src/L1/nleps_jacobian_action.md
[old]: - `palace/linalg/nleps.cpp:661-662` — `auto A = BuildParSumOperator({1.0 + 0.0i, eig, eig * eig, 1.0 + 0.0i}, {opK, opC, opM, A2n.get()}, true)` — the re-scoped value pencil `T(λ)`
[new]: - `palace/linalg/nleps.cpp:662-663` — `auto A = BuildParSumOperator({1.0 + 0.0i, eig, eig * eig, 1.0 + 0.0i}, {opK, opC, opM, A2n.get()}, true)` — the re-scoped value pencil `T(λ)`
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]: - `palace/linalg/nleps.cpp:663` — `const Eigen::MatrixXcd S = eig * Eigen::MatrixXcd::Identity(k, k) - H` — the `k×k` linearization block `S = λI − H`
[new]: - `palace/linalg/nleps.cpp:664` — `const Eigen::MatrixXcd S = eig * Eigen::MatrixXcd::Identity(k, k) - H` — the `k×k` linearization block `S = λI − H`
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]: - `palace/linalg/nleps.cpp:664` — `const Eigen::VectorXcd Sv2 = S.fullPivLu().solve(v2)` — the first dense solve `S⁻¹·v₂`
[new]: - `palace/linalg/nleps.cpp:665` — `const Eigen::VectorXcd Sv2 = S.fullPivLu().solve(v2)` — the first dense solve `S⁻¹·v₂`
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]: - `palace/linalg/nleps.cpp:665` — `const ComplexVector XSv2 = MatVecMult(X, Sv2)` — the back-projection `X·(S⁻¹·v₂)`
[new]: - `palace/linalg/nleps.cpp:666` — `const ComplexVector XSv2 = MatVecMult(X, Sv2)` — the back-projection `X·(S⁻¹·v₂)`
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]: - `palace/linalg/nleps.cpp:666` — `const ComplexVector XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2))` — the second sequential solve + back-projection
[new]: - `palace/linalg/nleps.cpp:667` — `const ComplexVector XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2))` — the second sequential solve + back-projection
```

Leading Evidence-row (line 145) — the inline `w1=...` comment sub-anchor inside the `:649-669`
block-range row drifts (`:659-660` → `:660-661`; the enclosing `:649-669` block range stays as-is).
On-disk the two-line comment spans `:660-661` (the bare `{` is on `:659`); `citecheck --anchor`
false-passes BOTH ranges because the `w1 = T'(l) v1` literal sits on `:660` inside both, so the
correction is anchored on the on-disk read confirming the comment's second line is `:661` and the
`{` (not comment) is `:659` — matching the three siblings already re-anchored to `:660-661`:

```edit:book/src/L1/nleps_jacobian_action.md
[old]: comment `:659-660` ("w1 = T'(l) v1 + U'(l) v2 = T'(l) v1 + T'(l)XS v2 − T(l)XS^2 v2") names the big-space + deflation-coupling decomposition
[new]: comment `:660-661` ("w1 = T'(l) v1 + U'(l) v2 = T'(l) v1 + T'(l)XS v2 − T(l)XS^2 v2") names the big-space + deflation-coupling decomposition
```

Cross-reference Evidence rows (lines 164, 170, 171) — the `:665,:666` / `:664,:666` compound
pointers drift:

```edit:book/src/L1/nleps_jacobian_action.md
[old]: a length-`k` `linear_combination` over the deflation basis with the complex real/imag split; the back-projection primitive at `:665,:666`.
[new]: a length-`k` `linear_combination` over the deflation basis with the complex real/imag split; the back-projection primitive at `:666,:667`.
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]: the small-dense direct-solve leaf realizing the two `fullPivLu().solve` solves at `:664,:666`.
[new]: the small-dense direct-solve leaf realizing the two `fullPivLu().solve` solves at `:665,:667`.
```

```edit:book/src/L1/nleps_jacobian_action.md
[old]: - `book/src/L2/linear_combination.md` (firm) — the `X·S⁻¹v₂` / `X·S⁻²v₂` back-projections (the `MatVecMult(X, ·)` at `:665,:666`).
[new]: - `book/src/L2/linear_combination.md` (firm) — the `X·S⁻¹v₂` / `X·S⁻²v₂` back-projections (the `MatVecMult(X, ·)` at `:666,:667`).
```

### Cluster 2 — `book/src/L1/nleps_eigenvalue_correction.md` (two anchors)

Citecheck confirmation (both `[ok]` post-correction; both `[DRIFT]` pre-correction):
- `nleps.cpp:590 --anchor 'while (it < nleps_it)'` → ok  (pre: `:596` → `[DRIFT] -6, suggested :590`)
- `nleps.cpp:712 --anchor 'alpha *= backtrack_factor'` → ok  (pre: `:709` → `[DRIFT] +3, suggested :712`)

(`:691` `eig + alpha * delta_eig`, `:708` `eig = eig_trial`, the `:688-714` Armijo-block range, and
`:672-677` are all `[ok]` on-disk and are deliberately left unchanged.)

```edit:book/src/L1/nleps_eigenvalue_correction.md
[old]: Each outer iteration of the `while (it < nleps_it)` loop (`palace/linalg/nleps.cpp:596`) updates **both** the scalar eigenvalue estimate `λ` (`eig`) and the eigenvector estimate `v` together.
[new]: Each outer iteration of the `while (it < nleps_it)` loop (`palace/linalg/nleps.cpp:590`) updates **both** the scalar eigenvalue estimate `λ` (`eig`) and the eigenvector estimate `v` together.
```

```edit:book/src/L1/nleps_eigenvalue_correction.md
[old]: - **Armijo damping `α`** — the per-step backtracking factor applied to `δλ` (`:691`, `:709`) and the commit (`:708`) are line-search orchestration concerns, not part of this atom (the operator produces the undamped `δλ`; semantics point 5).
[new]: - **Armijo damping `α`** — the per-step backtracking factor applied to `δλ` (`:691`, `:712`) and the commit (`:708`) are line-search orchestration concerns, not part of this atom (the operator produces the undamped `δλ`; semantics point 5).
```

### Cluster 3 — `vector.cpp:667 → :668` sibling sweep

Citecheck confirmation: `vector.cpp:668 --anchor 'MFEM_ASSERT(x.Size() == y.Size()'` → ok;
`vector.cpp:667 --anchor 'MFEM_ASSERT(x.Size() == y.Size()'` → `[DRIFT] +1, suggested :668`
(on-disk `:667` is `static hypre::HypreVector X, Y;`). The enclosing range `vector.cpp:664-672`
(the `LocalDot(Vector, Vector)` body) is `[ok]` on-disk and is NOT changed — only the inline
"`MFEM_ASSERT` at `:667`" sub-anchor inside it drifts.

`book/src/L2/inner_product.md` (line 360):

```edit:book/src/L2/inner_product.md
[old]: `MFEM_ASSERT(x.Size() == y.Size())` at `palace/linalg/vector.cpp:667`). L2 de-fuses the
[new]: `MFEM_ASSERT(x.Size() == y.Size())` at `palace/linalg/vector.cpp:668`). L2 de-fuses the
```

`book/src/L2-L1/inner-product-fold-specialization.md` (four occurrences — `:59`, `:260`, `:403`,
`:553`; all anchor the same `MFEM_ASSERT(x.Size() == y.Size())` line, all carry the identical −1
drift):

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[old]: precondition the L0 fused reduction kernels require (Palace's
`MFEM_ASSERT(x.Size() == y.Size())`, `palace/linalg/vector.cpp:667`).
[new]: precondition the L0 fused reduction kernels require (Palace's
`MFEM_ASSERT(x.Size() == y.Size())`, `palace/linalg/vector.cpp:668`).
```

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[old]:    Palace enforces it with `MFEM_ASSERT(x.Size() == y.Size())`
   (`palace/linalg/vector.cpp:667`). For the weighted member, additionally `M`'s codomain
[new]:    Palace enforces it with `MFEM_ASSERT(x.Size() == y.Size())`
   (`palace/linalg/vector.cpp:668`). For the weighted member, additionally `M`'s codomain
```

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[old]:   `hypre_SeqVectorInnerProd`, with `MFEM_ASSERT(x.Size()==y.Size())` at `:667`. The real
[new]:   `hypre_SeqVectorInnerProd`, with `MFEM_ASSERT(x.Size()==y.Size())` at `:668`. The real
```

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[old]:     note: real LocalDot single Hypre pass; MFEM_ASSERT(x.Size()==y.Size()) at :667. Exact.
[new]:     note: real LocalDot single Hypre pass; MFEM_ASSERT(x.Size()==y.Size()) at :668. Exact.
```

## Discipline notes

- **Pure re-anchoring; zero semantic/prose change.** Every edit changes only digits in a citation
  pinpoint. No signature, semantics point, algebraic law, variant axis, status, dependency, or
  cross-reference text is altered. The entries' `firm` status and all narrative stay identical.
  This is bounded citation-drift correction, the lifter's central deliverable — not the
  L0-evidence-driven prose-correction sub-case (no claim is wrong; only line numbers drifted).
- **Source of truth = on-disk `reference/palace/` via `citecheck`, NOT the codemap.** Per this
  cycle's load-bearing directive, the codemap `read_range` is +1 behind on-disk on `nleps.cpp`
  brace boundaries (it merges the opening `{` at on-disk `:659` into the preceding `if (k > 0)`
  comment, shifting codemap lines from on-disk `:660` onward by −1). Every corrected anchor was
  re-verified with `citecheck --anchor` against the exact on-disk substring (all `[ok]`); every
  pre-correction number was confirmed `[DRIFT]`. The cluster-1 numbers match the cycle-025
  abstractor's independently-derived on-disk set (`S`=664, `Sv2`=665, `XSv2`=666, `XSSv2`=667).
- **The standalone `:660` on `nleps_jacobian_action.md` line 77 is left unchanged** — it cites the
  formula fragment `+ T'(l)XS v2 − T(l)XS^2 v2`, which is genuinely on on-disk `:660` (the
  `w1 = ...` comment line). Only the *two-line comment-block* citation `:659-660` (which describes
  the full `w1 = ... names the big-space + deflation-coupling decomposition` comment, spanning
  on-disk `:660-661`) re-anchors to `:660-661`. This avoids over-correcting a coincidentally-correct
  single-line pinpoint into a wrong one.
- **Range citations are preserved.** `nleps.cpp:649-669` (cluster 1, the whole `w = J·v` block —
  endpoints `:649` and `:669` both correct on-disk), `nleps.cpp:688-714` (cluster 2, the Armijo
  block), and `vector.cpp:664-672` (cluster 3, the `LocalDot(Vector,Vector)` body) are all `[ok]`
  on-disk and are NOT touched — the drift is in the brace-interior pinpoints, not the block
  endpoints. The cluster-1 block end `:669` is `A->AddMult(...)`; the `}` is at on-disk `:670`, but
  the entry's chosen end-anchor `:669` (the last statement) is faithful and unchanged.
- **Sibling sweep corrected all four `:667` occurrences, not only the two named.** The cycle-025 OQ
  named `inner-product-fold-specialization.md:59,260`; lines `:403` and `:553` carry the identical
  `MFEM_ASSERT(x.Size()==y.Size()) at :667` drift (one in an Evidence row, one in a lowering-verifier
  `note:` annotation). Per the relocated-pointer sweep discipline, all four re-anchor to `:668`. The
  `:553` note is inside an audit-record block, but it is still an incorrect line-number pinpoint at
  the same MFEM_ASSERT site; correcting the digit does not alter the audit verdict (`supports`) or
  its `:664-672` range citation.

## Supporting evidence

- **cycle-025 abstractor report** `reports/2026-05-29T151441Z-abstractor-nleps-jacobian-action-rotation/CYCLE.md`
  §Open-questions #1 — the original +1 codemap-drift diagnosis with the on-disk-correct numbers
  (`S`=664, `Sv2`=665, `XSv2`=666, `XSSv2`=667) this re-anchor confirms and applies.
- **cycle-025 integrator-per-report OQs** (the three closed below): `nleps-jacobian-action-l1-entry-six-anchor-reanchor`,
  `nleps-eigenvalue-correction-l1-entry-two-anchor-reanchor`, `vector-cpp-667-mfem-assert-citation-drift-to-668-sibling-sweep`.
- **On-disk source** `reference/palace/palace/linalg/nleps.cpp:649-714` and
  `reference/palace/palace/linalg/vector.cpp:664-672` — read via `citecheck --show`; the
  authoritative line numbers.
- **citecheck batch verification** — all nine corrected anchors (`nleps.cpp:660-661`, `:662-663`,
  `:664`, `:665`, `:666`, `:667`, `:590`, `:712`; `vector.cpp:668`) ran `9 ok, 0 failing` against
  `reference/palace`.

## Open questions / caveats

No new open questions. This dispatch closes the three carry-forward citation-drift OQs from
cycle-025:

1. **CLOSE `nleps-jacobian-action-l1-entry-six-anchor-reanchor`** — the six deflation-block anchors
   (`:659-660`→`:660-661`, `:661-662`→`:662-663`, `:663`→`:664`, `:664`→`:665`, `:665`→`:666`,
   `:666`→`:667`) re-anchored across the entry's exec-trace, Semantics, Dependencies, Status,
   L1-vs-L0, Evidence, and cross-reference sections. All confirmed by `citecheck --anchor`. The
   theme `book/src/L1-L0/nleps-jacobian-action-mutation-rotation.md` already used the corrected
   on-disk numbers (per the cycle-025 abstractor), so the theme and the operator entry now agree.
2. **CLOSE `nleps-eigenvalue-correction-l1-entry-two-anchor-reanchor`** — the `while (it < nleps_it)`
   loop `:596`→`:590` and the Armijo `alpha *= backtrack_factor` `:709`→`:712` re-anchored;
   `:691`/`:708`/`:688-714` confirmed correct and unchanged.
3. **CLOSE `vector-cpp-667-mfem-assert-citation-drift-to-668-sibling-sweep`** — all five live
   occurrences (`inner_product.md:360`; `inner-product-fold-specialization.md:59,260,403,553`)
   re-anchored `:667`→`:668`; the `:664-672` range citation confirmed correct and unchanged. (If a
   future grep finds the `:667→:668` drift in any other chapter, it is the same one-line shift and
   the same correction applies — flagged for the integrator's awareness, not a new OQ.)

**Methodology observation (not a new OQ; for the batch-7 meta-phase's awareness):** the codemap
`read_range` +1 brace-boundary drift on `nleps.cpp` is now confirmed across two independent cycles
(cycle-024 authoring → cycle-025 detection → cycle-026 correction). The friction-ledger
`producer-citation-drift-verify-not-self-invoked` entry's cycle-024 `--anchor` mechanical realization
is exactly what catches and corrects this: every anchor here was machine-verified, not eyeballed.
The cycle-025 abstractor's OQ #2 (recommending the role-spec strengthen "codemap is
localization-only; citecheck/on-disk read is the citation source of truth") is the right framing —
this dispatch is the worked precedent.

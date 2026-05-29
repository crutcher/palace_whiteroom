---
agent: lowering-verifier
invoked_at: 2026-05-29T151441Z
scope: L2>L1 theme audit — gram-fold-specialization
status: integrated
integrated_at: 2026-05-29T17:15:00Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-025 finalize (first primary cycle of meta-batch-7). Audit verdict fully-supported → theme STAYS firm (## Status untouched). Three changes: (a) vector.cpp:667→:668 MFEM_ASSERT(x.Size()==y.Size()) aligned-pass anchor correction at both in-theme sites (lines 60 + 240); (b) enclosing-range tighten nleps.cpp:613-619→:614-619 in §Verified-against; (c) additive verified_against: YAML (13 entries) at EOF. Both findings are precision matters, not content contradictions. OQ gram-fold-specialization-l2-gram-forward-reference-closure-followup RESOLVED (forward-reference closure CONFIRMED; the 3rd of 4 slugs on open-questions.md:327). 2 NEW carry-forward OQs: vector-cpp-667-mfem-assert-citation-drift-to-668-sibling-sweep (inner_product.md:360 + inner-product-fold-specialization.md:59,260 still drifted) + gram-md-forward-ref-text-refresh-to-name-gram-fold-specialization. retroactive-budget 0; clean build."
inputs:
  - book/src/L2-L1/gram-fold-specialization.md
  - palace/linalg/nleps.cpp:504-575 (Gram-build site + consumer + coord-loop + early-return)
  - palace/linalg/nleps.cpp:354-362, 605-625 (literature anchors + basis growth)
  - palace/linalg/vector.cpp:258-270 (ComplexVector::Dot conjugation kernel)
  - palace/linalg/vector.cpp:660-690 (real / complex LocalDot reduction trees)
  - palace/linalg/operator.cpp:615-642 (weighted two-stage Dot)
  - book/src/L2/gram.md (L2 LHS: laws 1-6, conjugation convention, IEEE non-law, forward-ref)
  - book/src/L2-L1/inner-product-fold-specialization.md (sibling scalar theme)
  - book/src/L1/dot.md, book/src/L1/bilinear-form.md, book/src/L2/inner_product.md (RHS leaves + parent)
---

# CYCLE: Audit gram-fold-specialization

## Summary

I audited the firm L2>L1 theme `gram-fold-specialization` (landed firm cycle-024) against concrete
L0 evidence, focusing on three questions the dispatch posed: (1) does the `:525-531` double-`dot`
loop actually realize the XHX Gram-build the theme claims; (2) does the rewrite preserve the
matrix-valued fold semantics including the per-cell conjugate-pair re-order; (3) is the
forward-reference closure to L2 `gram` (the c024 OQ
`gram-fold-specialization-l2-gram-forward-reference-closure`) sound. **Verdict:
fully-supported.** Every load-bearing claim verifies against the source read this invocation: the
positive Gram-build site `nleps.cpp:524-531` with cell body `:529 SS(i,j) = linalg::Dot(GetComm(),
X[i], X[j])` is the literal double-loop materialization of the all-pairs definition law; the
per-cell conjugate-pair re-order is correctly a no-op for Palace's exact operand order
(`linalg::Dot` conjugates arg-2 = column `j`, matching the L2 arg-1-conjugated convention applied
to `X[j]`); the consumer `:532-535` is the deflation complex LU solve (making the off-diagonal
re-order observable, exactly as the cross-cutter census flagged); the per-cell reduction-tree
table matches the verified `vector.cpp` bodies; the symmetry-exploitation note is a faithful
transparent-trick recording; and the theme closes the `gram.md:242-246` forward-reference content
piece-for-piece. The matrix specialization correctly **generalizes** (does not duplicate) the
sibling scalar theme. **One inherited citation drift** found: `palace/linalg/vector.cpp:667` (the
`MFEM_ASSERT(x.Size() == y.Size())` aligned-pass precondition) is actually at `:668` (`:667` is
`static hypre::HypreVector X, Y;`) — a carry-forward miscitation shared with `inner_product.md`
and `inner-product-fold-specialization.md`. Recommended as a bounded carry-forward correction, NOT
a status reduction. One enclosing-range looseness on `nleps.cpp:613-619` (`:613` is `eigs[k]=eig`,
not the start of the `X.resize`; tight range is `:614-619`) — in-bounds, encloses all cited
constructs, recorded as a precise-range refinement only.

## Per-citation audit

All L0 anchors mechanically verified with `tools/citecheck/citecheck.py --anchor`/`--show` against
`reference/palace` and read with `palace-codemap read_range`. Project-file (book) ranges
bounds-checked with `--project-root . --ref-root .`.

### nleps.cpp:524-531 — the Gram-build double loop (the headline citation)
- **Citation**: `palace/linalg/nleps.cpp:524-531` (+ `:525-531` for the loop alone, `:529` for the cell body)
- **Theme claim**: the one L2 matrix-valued fold re-fuses into Palace's nested `for i { for j { SS(i,j) = linalg::Dot(GetComm(), X[i], X[j]) } }` double-`Dot` loop; `:524` is the fresh `Eigen::MatrixXcd SS(k,k)` decl; `:529` is the per-cell `dot`-leaf dispatch with the canonical Hermitian hook.
- **Found**: `:524 = Eigen::MatrixXcd SS(k, k);` `:525 = for (int i = 0; i < k; i++)` `:527 = for (int j = 0; j < k; j++)` `:529 = SS(i, j) = linalg::Dot(GetComm(), X[i], X[j]);` `:531 = }`. `search_text` confirms `:529` is the **sole** `linalg::Dot(GetComm(), X[i], X[j])` occurrence in the file. `--anchor` literal `linalg::Dot(GetComm(), X[i], X[j])` resolves at line 529.
- **Verdict**: **supports.** The double-loop materialization, the cell body, the fresh-matrix decl (out-of-place fold, not through-written), and the `linalg::Dot` (canonical Hermitian) hook all match exactly.
- **Notes**: This is the same range `L2/gram` law 1 (`gram.md:119-121`) cites for the all-pairs definition — the L2 law and the L2>L1 lowering are grounded in the *same* positive site, which is exactly why the theme's "the dispatch rule IS the gram all-pairs law read as a lowering" claim is sound (no independent inference layer).

### nleps.cpp:529 — the per-cell conjugate-pair re-order witness
- **Citation**: `palace/linalg/nleps.cpp:529`
- **Theme claim**: `SS(i,j) = linalg::Dot(comm, X[i], X[j]) = X[j]ᴴ X[i]` (arg-2 / column-`j` conjugated), which **already equals** the L2 cell `inner_product(X[j], X[i]) = X[j]ᴴ X[i]` (arg-1 conjugated, arg-1 = `X[j]`); so the re-order is a **no-op for the matrix as Palace writes it**.
- **Found**: cell body literal confirmed at `:529`. Cross-checked the conjugation direction: `dot.md:43` pins L1 `dot` conjugate-linear in arg-1 (`⟨x,y⟩ = xᴴ y`) and notes the free-function `linalg::Dot(comm, x, y)` carries the C++ method's arg-2 conjugation. `ComplexVector::Dot` body (`vector.cpp:265-266`) returns `Re = xr·yr + xi·yi`, `Im = xi·yr − xr·yi` = `x · conj(y) = yᴴ x` — arg-2 conjugated, confirmed. With `a=X[i], b=X[j]`: `linalg::Dot(comm, X[i], X[j]) = X[j]ᴴ X[i]`. L2 `inner_product(X[j], X[i]) = X[j]ᴴ X[i]`. **Equal.**
- **Verdict**: **supports.** The semantic identity `X[j]ᴴ X[i] = X[j]ᴴ X[i]` (no-op re-order) is correct, and the load-bearing corollary (re-order becomes work only if a downstream impl transposes indices / swaps operands) is sound.
- **Notes**: This is the core theme content and it is the most carefully verified claim. The conjugation handedness chains correctly across three files (`nleps.cpp:529` → `vector.cpp:265-266` → `dot.md:43`).

### nleps.cpp:532-535 / :533-534 — the consumer (deflation LU solve)
- **Citation**: `palace/linalg/nleps.cpp:532-535` (Verified-against), `:533-534` (body, the LU-solve sub-range)
- **Theme claim**: the Gram cells feed `deflate`'s complex LU solve (`SS = -S.fullPivLu().solve(SS)`; `x2 = SS.fullPivLu().solve(x2)`; back-projection `MatVecMult(X, S.fullPivLu().solve(x2))`) — the full complex value is consumed, so per-cell conjugation handedness is **observable / load-bearing**.
- **Found**: `:532 = const Eigen::MatrixXcd S = eig_opInv * Eigen::MatrixXcd::Identity(k, k) - H;` `:533 = SS = -S.fullPivLu().solve(SS);` `:534 = x2 = SS.fullPivLu().solve(x2);` `:535 = const ComplexVector XSx2 = MatVecMult(X, S.fullPivLu().solve(x2));`
- **Verdict**: **supports.** Both the enclosing `:532-535` consumer block and the precise `:533-534` LU-solve sub-range are correct and consistent (no internal-range disagreement).
- **Notes**: Confirms the theme's "observable-unweighted at `nleps.cpp:529`" justification — the consumer is a complex LU solve on the full Gram value, not a real projection.

### nleps.cpp:515-518 — the k==0 early-return (empty-basis law)
- **Citation**: `palace/linalg/nleps.cpp:515-518`
- **Theme claim**: the empty basis `k=0` materializes as `Matrix[0,0]` — the `if (k == 0) // no deflation { return; }` early-return (`L2/gram` law 2).
- **Found**: `:515 = if (k == 0)  // no deflation` `:516 = {` `:517 = return;` `:518 = }`. Exact match.
- **Verdict**: **supports.**

### nleps.cpp:520-523 / :522 — the coordinate-extraction loop (Xᴴ· half)
- **Citation**: `palace/linalg/nleps.cpp:520-523` (`:522` for the body)
- **Theme claim**: `x2(j) = b2(j) - linalg::Dot(GetComm(), x1, X[j])` is the `Xᴴ·` half (arg-1-conjugated convention applied to a vector rather than a basis column), flagged observable-unweighted at `:522`.
- **Found**: `:520 = for (int j = 0; j < k; j++)` `:522 = x2(j) = b2(j) - linalg::Dot(GetComm(), x1, X[j]);` `:523 = }`. Exact match.
- **Verdict**: **supports.** (Context citation; not a Gram-build law, correctly framed as a sibling coord-extraction.)

### nleps.cpp:561-569 / :563, :568 — compute_residual (second Gram-solve consumer)
- **Citation**: `palace/linalg/nleps.cpp:561-569`
- **Theme claim**: a second consumer of the Gram-solve (NOT a fresh Gram build): `MatVecMult(X, S.fullPivLu().solve(vv2))` (`:563`) + residual coords `rr2(j) = linalg::Dot(GetComm(), vv, X[j])` (`:568`).
- **Found**: `:563 = const ComplexVector XSvv2 = MatVecMult(X, S.fullPivLu().solve(vv2));` `:568 = rr2(j) = linalg::Dot(GetComm(), vv, X[j]);`. Exact match. Confirmed this is `compute_residual`'s deflation, distinct from the `deflated_solve` Gram build.
- **Verdict**: **supports.**

### nleps.cpp:613-619 — deflation-basis growth (incremental-Gram law 6)
- **Citation**: `palace/linalg/nleps.cpp:613-619`
- **Theme claim**: `X.resize(k+1); X[k] = v; H.conservativeResizeLike(...); H(k,k) = eig; k++` — the basis grows one column per converged eigenpair; the Gram is rebuilt at bordered `k+1` on the next `deflated_solve`.
- **Found**: `:613 = eigs[k] = eig;` `:614 = X.resize(k + 1);` `:615 = X[k] = v;` `:616 = H.conservativeResizeLike(Eigen::MatrixXd::Zero(k + 1, k + 1));` `:617 = H.col(k).head(k) = v2 / scale;` `:618 = H(k, k) = eig;` `:619 = k++;`
- **Verdict**: **partially-supports (enclosing-range looseness, off-by-one at low boundary).** All cited constructs (`X.resize`, `X[k]=v`, `H.conservativeResizeLike`, `H(k,k)=eig`, `k++`) fall within `:614-619`; `:613` is `eigs[k]=eig` (a related-but-different statement). The range encloses everything claimed and is in-bounds, so it is value-faithful, but the tight range is `:614-619`. Recorded as a precise-range refinement, NOT a contradiction.
- **Notes**: Minor; does not affect any law claim. The theme's prose narration is accurate.

### nleps.cpp:354-362 — deflation-scheme literature anchors
- **Citation**: `palace/linalg/nleps.cpp:354-362` (`:354-355` Jarlebring/Koskela/Mele 2018; `:356` SLEPc-NEP minimality index 1; `:357-358` Effenberger 2013)
- **Theme claim**: the standard-scheme literature anchor for the oblique-Galerkin deflation Gram.
- **Found**: `:354-355 = // Reference: Jarlebring, Koskela, Mele, Disguised and new quasi-Newton methods for / nonlinear eigenvalue problems, Numerical Algorithms (2018).` `:356 = // Using the deflation scheme used by SLEPc's NEP solver with minimality index set to 1.` `:357-358 = // Reference: Effenberger, Robust successive computation of eigenpairs for nonlinear / eigenvalue problems, SIAM J. Matrix Anal. Appl. (2013).` Exact match per sub-anchor.
- **Verdict**: **supports.**

### vector.cpp:263-266 — ComplexVector::Dot (conjugation kernel / re-order source)
- **Citation**: `palace/linalg/vector.cpp:263-266`
- **Theme claim**: `= x·conj(y) = yᴴ x` (arg-2 conjugated) — the per-cell conjugation kernel + conjugate-pair re-order source.
- **Found**: `:263 = std::complex<double> ComplexVector::Dot(const ComplexVector &y) const` `:265-266 = return {(Real() * y.Real()) + (Imag() * y.Imag()), (this == &y) ? 0.0 : ((Imag() * y.Real()) - (Real() * y.Imag()))};` = `Re = xr·yr + xi·yi`, `Im = xi·yr − xr·yi` = `x·conj(y) = yᴴ x`. Arg-2 conjugation confirmed.
- **Verdict**: **supports.**
- **Notes**: The sibling scalar theme cites the same body as `:263-267` (including closing brace) in one spot; the gram theme's `:263-266` (signature + return) is the same construct minus the brace. Both in-bounds and faithful; sibling-internal range-style inconsistency, not a gram-theme drift.

### vector.cpp:665-672 / :674-685 — per-cell reduction trees (real / complex)
- **Citation**: `palace/linalg/vector.cpp:665-672` (real LocalDot single Hypre pass), `:674-685` (complex four-real-dot lift). (Theme also uses `:664-672` in §dispatch line 123; sibling uses `:664-672`.)
- **Theme claim**: real cell = single Hypre `hypre_SeqVectorInnerProd` strided pass; complex cell = four real Hypre passes (`xr·yr, xi·yi, xi·yr, xr·yi`) combined into `(Re,Im)` with `Im` cross-term sign `−`.
- **Found**: `:665-672 = double LocalDot(const Vector &x, const Vector &y) { ... return hypre_SeqVectorInnerProd(X, Y); }` (single pass). `:674-685 = std::complex<double> LocalDot(const ComplexVector &x, const ComplexVector &y) { ... return {LocalDot(x.Real(), y.Real()) + LocalDot(x.Imag(), y.Imag()), LocalDot(x.Imag(), y.Real()) - LocalDot(x.Real(), y.Imag())}; }` — exactly `Re = xr·yr + xi·yi`, `Im = xi·yr − xr·yi`.
- **Verdict**: **supports.** Both real and complex per-cell trees match the theme's per-cell table.
- **Notes**: `:664-672` (used in §dispatch) is the same range with the leading blank line `:664`; `:665-672` (Verified-against) is tight. Both in-bounds; matter of style. Inherited verbatim from the firm sibling theme as the theme states.

### operator.cpp:621-638 — weighted two-stage Dot (bilinear_form per-cell tree)
- **Citation**: `palace/linalg/operator.cpp:621-638`
- **Theme claim**: the B-weighted-hook cell is a two-stage tree — the M-application reduction (the `Ax` workspace) then the four-real-dot reduction of `Dot(comm, B·X[i], X[j])`.
- **Found**: `:621-629 = Dot(MPI_Comm comm, const ComplexVector &x, const Operator &A, const ComplexVector &y) { ComplexVector Ax(A.Height()); ... A.Mult(x.Real(), Ax.Real()); A.Mult(x.Imag(), Ax.Imag()); return Dot(comm, Ax, y); }` and `:631-638` the `ComplexOperator` overload (`A.Mult(x, Ax); return Dot(comm, Ax, y);`). The `Ax` workspace + two-stage (apply-then-dot) structure confirmed.
- **Verdict**: **supports.**

### vector.cpp:667 — the aligned-pass precondition (MFEM_ASSERT)
- **Citation**: `palace/linalg/vector.cpp:667` (cited at gram theme lines 60 and 240)
- **Theme claim**: `MFEM_ASSERT(x.Size() == y.Size())` — the aligned-pass precondition each per-cell L0 reduction kernel requires.
- **Found**: `:667 = static hypre::HypreVector X, Y;` — the assert is at **`:668`** (`MFEM_ASSERT(x.Size() == y.Size(), "Size mismatch for vector inner product!");`). `--anchor 'MFEM_ASSERT(x.Size() == y.Size()'` reports `[DRIFT] +1, suggested :668`.
- **Verdict**: **does-not-support at the cited line (off-by-one); supports at `:668`.** The construct exists and the claim is correct; only the line number is wrong by +1.
- **Notes**: **Inherited drift** — the same `:667` miscitation appears in `book/src/L2/inner_product.md:360`, `book/src/L2-L1/inner-product-fold-specialization.md:59,260`, and `book/src/L2-L1/gram-fold-specialization.md:60,240`. Pre-existing carry-forward, not introduced by this theme. See Proposed changes (bounded carry-forward correction) + Open questions.

### Book-internal anchors (L2 gram, sibling, L1 leaves, L2 parent)
- `book/src/L2/gram.md` §Signature `:42-50`, conjugation convention `:73-85`, law 1 `:117-122`, law 2 `:124-126`, law 3 `:130-135`, law 5 `:153-156`, law 6 `:158-164`, IEEE non-law `:166-176`, forward-ref `:242-246` — all **in-bounds**; content spot-read (`:117-176`) confirms law 1 = all-pairs definition grounded in `nleps.cpp:529`, law 3 = Hermitian symmetry with real diagonal / conjugation-sensitive off-diagonal, IEEE non-law explicitly defers per-cell-tree recording to "the L2>L1 lowering theme (forthcoming)". **supports.**
- `book/src/L2-L1/inner-product-fold-specialization.md` (sibling) §dispatch `:92-136` content read: three orthogonal dispatch keys (conjugation / element-type / weight) confirmed; the gram theme inherits them per-cell without restating. **supports — correct generalization, not duplication.**
- `book/src/L1/dot.md:33-35,43,49`, `book/src/L1/bilinear-form.md:63` (`bilinear_form(x,M,y) = xᴴ M y`), `book/src/L2/inner_product.md:46-102` — all in-bounds; `dot.md:43` content confirms the arg-1-conjugated convention + free-function arg-2 carry (the re-order chain); `bilinear-form.md:63` confirms the B-weighted leaf. **supports.**

## Applicability conditions

The theme states five conditions (§Applicability conditions). Walking each:

1. **Shared length axis per cell (aligned-pass precondition).**
   - **Verifiable**: yes — `MFEM_ASSERT(x.Size() == y.Size())` at `vector.cpp:668` (theme cites `:667`, off-by-one; see drift above) is invoked per cell by each `LocalDot`. The B-weighted addendum (B's codomain/domain axes) defers to `bilinear-form` §Applicability.
   - **Found counter-example?**: no. The condition is real and per-cell-applied.

2. **Hook fixed across the whole matrix.**
   - **Verifiable**: yes — `gram`'s `dot` hook is a single field (`gram.md:42-50` signature); NLEPS pins `linalg::Dot` (Hermitian) for every cell (`:529`). The "one dispatch decision, k² invocations" simplification is structurally sound.
   - **Found counter-example?**: no. Confirmed all k² cells use the identical leaf.

3. **Element-type conformance (one shared T).**
   - **Verifiable**: yes — NLEPS is complex (`Eigen::MatrixXcd SS`, `:524`); each cell lowers to the complex four-real-dot leaf (`vector.cpp:674-685`). Real path = single Hypre pass (`:665-672`).
   - **Found counter-example?**: no.

4. **Value-preservation vs bit-reproduction (the standard split, lifted per cell).**
   - **Verifiable**: yes — value-preservation holds under conditions 1-3; bit-reproduction additionally requires (a) per-cell reduction tree, (b) per-cell operand order, (c) all-k² coverage (not triangle-mirror). All three sub-conditions are grounded in verified source (the per-cell table + `:529` operand order + the `:525-531` all-k² loop).
   - **Found counter-example?**: no. The split is the CLAUDE.md load-bearing-numerical-trick discipline applied per-cell, correctly stated.

5. **The per-cell conjugate-pair re-order is observable for full-complex Gram-cell consumers.**
   - **Verifiable**: yes — the NLEPS deflation Gram feeds the complex LU solve `SS.fullPivLu().solve(...)` (`:533-534`), confirmed to consume the full complex value (observable case). A real-projection consumer would see no re-order.
   - **Found counter-example?**: no. The observable-unweighted classification at `:529` is consistent with the verified consumer at `:532-535`.

**All five conditions are complete and verifiable; no counter-examples.** The conditions correctly
lift the sibling scalar theme's conditions per-cell and add the matrix-specific cell-coverage
sub-condition (4c).

## Algebraic laws (cited)

The theme is classified `algebraic` (§Justification kind). It cites `L2/gram` laws 1, 2, 3, 5, 6
and the IEEE per-cell non-law. Checking each against the operator signatures / source:

- **Law 1 (all-pairs definition): `gram dot X [i,j] = inner_product(X[j], X[i]) = X[j]ᴴ X[i]`.**
  - **Holds on operators?**: yes. This IS the cell body `:529` read through the conjugation convention; the lowering rule is this law read forward. Grounded in the positive site, no inference.
- **Law 2 (empty-basis identity): `gram dot [] = Matrix[0,0]`.**
  - **Holds?**: yes. `k==0` early-return `:515-518`.
- **Law 3 (Hermitian symmetry): `G = Gᴴ` for the Hermitian hook; diagonal real.**
  - **Holds?**: yes. Cell `(j,i) = X[i]ᴴ X[j] = conj(X[j]ᴴ X[i]) = conj(G[i,j])` follows from the verified arg-2-conjugation kernel (`vector.cpp:265-266`). The diagonal `G[i,i] = X[i]ᴴ X[i]` is real (the `&x==&y` self-dot returns `Im = 0.0` exactly, `vector.cpp:266`/`dot.md:49`). The theme's "diagonal convention-invariant, off-diagonal conjugation-sensitive" split is correct.
- **Law 5 (concatenation block law) / Law 6 (incremental rank-1 border).**
  - **Holds?**: yes (structurally). Law 6 is realized by the basis growth `X.resize(k+1)` (`:614-619`, theme cites `:613-619`); the Gram is rebuilt at bordered size on next solve. The cross-Gram `gram2` member is the off-diagonal block. Consistent with the source's incremental-deflation structure.
- **IEEE per-cell reduction-tree non-law.**
  - **Holds (as a non-law)?**: yes. `gram.md:166-176` defers "which tree a given lowered Gram pins" to the L2>L1 theme; this theme supplies the per-cell table (real single-pass / complex four-real-dot / weighted two-stage), each row read off a verified `vector.cpp` / `operator.cpp` body. The "k² independent per-cell trees, no cross-cell accumulation" matrix-level claim is correct (the cells are written into distinct `SS(i,j)` slots, no shared accumulator).

**All cited laws hold on the operator signatures.** The `algebraic` classification is appropriate
(definition-law + inherited scalar dispatch, with reduction-chain and structural flavours noted but
subordinate), consistent with the sibling theme.

## Forward-reference closure (the dispatch-named OQ)

The dispatch asked me to confirm the closure of `gram.md:242-246` (OQ
`gram-fold-specialization-l2-gram-forward-reference-closure`). The `gram.md` forward-reference reads
(verified `:242-246`):

> **L2>L1 lowering theme** (forthcoming; abstractor work — not authored here): how the L2
> all-pairs fold lowers onto Palace's `nleps.cpp:524-531` double-`linalg::Dot` loop (the dispatch of
> each cell to the Hermitian/weighted `dot` leaf; the symmetry-exploitation transparent note; which
> reduction tree each cell pins — the load-bearing content of the IEEE non-law). Forward reference
> only.

This names **four** content pieces. The theme delivers all four:
1. **dispatch of each cell to the Hermitian/weighted `dot` leaf** → §"The dispatch rewrite (L2 → L1)" + per-cell dispatch table. ✓
2. **the symmetry-exploitation transparent note** → §"Symmetry-exploitation: a transparent perf-trick note". ✓
3. **which reduction tree each cell pins (the IEEE non-law load-bearing content)** → §"Per-cell summation-order recording" table. ✓
4. **the `nleps.cpp:524-531` double-`linalg::Dot` loop** → §"L1 form" + dispatch step 1, grounded in the verified site. ✓

**Closure verdict: the content forward-reference is fully satisfied.** The theme IS the
forthcoming theme `gram.md:242-246` anticipated. **Residual:** the `gram.md` prose still literally
says "(forthcoming; abstractor work — not authored here)" and "(forthcoming)" at `:176`. The
*content* is closed; the *cross-reference text* needs a refresh to name `gram-fold-specialization`
and drop "forthcoming". The theme itself correctly flags this as integrator / layer-intro-author
/ lifter cross-reference-refresh scope (§Open questions lines 460-468), NOT dispatch-phase work.
**I confirm the closure and route the text-refresh as a follow-up** (see Open questions) — I do not
action the `gram.md` edit (high→low / dispatch-phase write discipline + it is not this theme's
file).

## Sibling-consistency cross-check (matrix vs scalar)

Confirmed the matrix-valued specialization correctly **generalizes** the sibling
`inner-product-fold-specialization` rather than duplicating it:
- **Shared (inherited, not restated)**: the three orthogonal dispatch keys (conjugation /
  element-type / weight), the per-cell reduction trees (real single-pass / complex four-real-dot /
  weighted two-stage), the conjugate-pair re-order identity `X[j]ᴴ X[i] = conj(X[i]ᴴ X[j])`. The gram
  theme references these "inherited pointwise" and does not re-derive them.
- **Matrix-specific (genuinely new content)**: the double-loop materialization (no scalar analogue —
  "a single scalar has no index axes to range over"), the symmetry-exploitation triangle-mirror note,
  the per-cell-tree-independence vs fused-matmul question, the Hermitian-symmetry interaction of the
  re-order (cell `(j,i) = conj(cell (i,j))`).
- **Correctly NOT merged**: different L2 LHS (`inner_product : ... -> Scalar` vs `gram : ... ->
  Matrix[k,k]`), different result rank, different consumer (Krylov coefficients vs `deflate`'s
  Gram-solve — verified: the gram consumer at `:532-535` is the LU solve, distinct).

No duplication-explosion concern; the two themes are coherent siblings.

## Proposed changes

### (1) Recommended `verified_against:` block (append to the theme; the theme is fully-supported)

The audit confirms every load-bearing anchor. Recommend appending the following YAML block to the
end of `book/src/L2-L1/gram-fold-specialization.md`. The block is rendered 4-space-indented below
(the cycle-024 `convert-nested-fences-to-indented-code-in-proposed-changes-block` discipline, option
(b) — indent-delimited rather than nested-fence-delimited, so the outer `edit:` block cannot
mis-toggle). The integrator emits it into the chapter file as a real triple-backtick ```` ```yaml ````
fence (the channel-format requirement `lowering-verifier-yaml-in-prose-channel-format`); the leading
`verified_against:` text the downstream `cross-layer-cross-cutter` parser keys on is preserved
verbatim.

```edit:book/src/L2-L1/gram-fold-specialization.md
[append at end of file; emit the indented block below as a ```yaml ... ``` fenced block]
    verified_against:
      - citation: palace/linalg/nleps.cpp:524-531
        verdict: supports
        audited_at: 2026-05-29T151441Z
        note: double-loop Gram-build materialization (SS decl :524 + nested loop :525-531); sole literal XHX build site (search_text)
      - citation: palace/linalg/nleps.cpp:529
        verdict: supports
        audited_at: 2026-05-29T151441Z
        note: cell body SS(i,j)=linalg::Dot(GetComm(),X[i],X[j]) = X[j]ᴴX[i]; conjugate-pair re-order is no-op for Palace's operand order (chain verified nleps:529 -> vector.cpp:265-266 -> dot.md:43)
      - citation: palace/linalg/nleps.cpp:515-518
        verdict: supports
        audited_at: 2026-05-29T151441Z
        note: k==0 early-return = empty-basis Matrix[0,0] (L2/gram law 2)
      - citation: palace/linalg/nleps.cpp:520-523
        verdict: supports
        audited_at: 2026-05-29T151441Z
        note: x2 coordinate loop (Xᴴ· half); :522 observable-unweighted
      - citation: palace/linalg/nleps.cpp:532-535
        verdict: supports
        audited_at: 2026-05-29T151441Z
        note: deflation complex LU solve (:533-534) consuming full Gram value -> off-diagonal re-order observable
      - citation: palace/linalg/nleps.cpp:561-569
        verdict: supports
        audited_at: 2026-05-29T151441Z
        note: compute_residual second Gram-solve consumer (:563 MatVecMult, :568 rr2 coords)
      - citation: palace/linalg/nleps.cpp:613-619
        verdict: partially-supports
        audited_at: 2026-05-29T151441Z
        note: enclosing range encloses all cited basis-growth constructs but :613 is eigs[k]=eig; tight range is :614-619 (off-by-one at low boundary, in-bounds, value-faithful)
      - citation: palace/linalg/nleps.cpp:354-362
        verdict: supports
        audited_at: 2026-05-29T151441Z
        note: Jarlebring/Koskela/Mele 2018 (:354-355), SLEPc-NEP minimality 1 (:356), Effenberger 2013 (:357-358)
      - citation: palace/linalg/vector.cpp:263-266
        verdict: supports
        audited_at: 2026-05-29T151441Z
        note: ComplexVector::Dot = x·conj(y) = yᴴx (arg-2 conjugated); the re-order source kernel
      - citation: palace/linalg/vector.cpp:665-672
        verdict: supports
        audited_at: 2026-05-29T151441Z
        note: real LocalDot single Hypre hypre_SeqVectorInnerProd pass (per-cell real tree)
      - citation: palace/linalg/vector.cpp:674-685
        verdict: supports
        audited_at: 2026-05-29T151441Z
        note: complex LocalDot four-real-dot lift; Re=xr·yr+xi·yi, Im=xi·yr−xr·yi (per-cell complex tree)
      - citation: palace/linalg/operator.cpp:621-638
        verdict: supports
        audited_at: 2026-05-29T151441Z
        note: weighted two-stage Dot (Ax workspace then Dot(comm,Ax,y)); both Operator and ComplexOperator overloads (bilinear_form per-cell tree)
      - citation: palace/linalg/vector.cpp:668
        verdict: does-not-support-at-cited-line-667
        audited_at: 2026-05-29T151441Z
        note: MFEM_ASSERT(x.Size()==y.Size()) is at :668, not the theme's previously-cited :667 (:667 is `static hypre::HypreVector X, Y;`); corrected to :668 by Proposed change (2); inherited carry-forward drift shared with inner_product.md + inner-product-fold-specialization.md
```

### (2) Bounded carry-forward citation correction (`vector.cpp:667` -> `:668`)

Per my role-spec (`lifter-scope-content-correction-boundary` / `audit-report-inherited-miscitation-lint`),
the `:667`->`:668` correction is in-scope as a bounded, evidenced citation fix. Within **this theme**
the two occurrences are at `gram-fold-specialization.md:60` and `:240`:

```edit:book/src/L2-L1/gram-fold-specialization.md
[line 60] replace `palace/linalg/vector.cpp:667` with `palace/linalg/vector.cpp:668`
[line 240] replace `palace/linalg/vector.cpp:667` with `palace/linalg/vector.cpp:668`
```

The integrator should apply these two in-theme. The **shared** occurrences in
`book/src/L2/inner_product.md:360` and `book/src/L2-L1/inner-product-fold-specialization.md:59,260`
are outside this theme's file — recommend the integrator carry them forward as the same `:667`->`:668`
correction, OR route a follow-up `lifter`/`repairer` dispatch. (NOT actioned by me — those are not
this dispatch's file, and I do not write to `book/`.)

### (3) Optional precise-range refinement (`nleps.cpp:613-619` -> `:614-619`)

Non-blocking. The current range is in-bounds and encloses all cited constructs; tightening to
`:614-619` would drop the unrelated `:613 eigs[k]=eig` from the cited window. Recommend as an
optional refinement only; the `verified_against:` block above records it as `partially-supports`
with the tight range noted. Leave to integrator discretion.

**No status change proposed.** The theme is `firm` and the audit confirms it: the single
off-by-one citation drift and the one enclosing-range looseness are anchor-precision matters, not
content contradictions. The dispatch structure, the laws, the re-order, the per-cell trees, and the
forward-reference closure all hold.

## Supporting evidence

Source files consulted this invocation (all via `palace-codemap read_range` + mechanical
`tools/citecheck/citecheck.py --anchor`/`--show`/`--scan`):
- `palace/linalg/nleps.cpp:354-362, 504-575, 605-625` — Gram-build site, consumer, coord-loop, early-return, compute_residual, basis growth, literature anchors.
- `palace/linalg/vector.cpp:258-270` (ComplexVector::Dot), `:660-690` (real + complex LocalDot trees).
- `palace/linalg/operator.cpp:615-642` (weighted two-stage Dot).
- `book/src/L2/gram.md:42-50, 73-85, 115-176, 230-260, 242-246` (L2 LHS laws + conjugation + IEEE non-law + forward-ref).
- `book/src/L2-L1/inner-product-fold-specialization.md:92-141` (sibling dispatch keys).
- `book/src/L1/dot.md:33-49`, `book/src/L1/bilinear-form.md:60-65`, `book/src/L2/inner_product.md:46-102`.
- `book/src/L2-L1/index.md:17`, `book/src/SUMMARY.md:57` (cross-reference wiring — both present and correct).
- `grep` across `book/src/` for the shared `vector.cpp:667` / `:664-672` / `:665-672` citation occurrences (carry-forward scoping).

## Open questions / caveats

- **OQ closed (the dispatch-named one): `gram-fold-specialization-l2-gram-forward-reference-closure`.**
  The *content* forward-reference (`gram.md:242-246`, four content pieces) is fully satisfied by this
  theme. The OQ should be marked CLOSED on the content axis. **Residual text-refresh follow-up**: the
  `gram.md` prose still says "(forthcoming)" at `:176` and `:242-246` — recommend a
  `layer-intro-author` / `lifter` cross-reference refresh to name `gram-fold-specialization` and drop
  "forthcoming". Routed as a NEW small OQ
  `gram-md-forward-ref-text-refresh-to-name-gram-fold-specialization` (text-only, not blocking; the
  theme already self-flags this at lines 460-468). NOT actioned here (not this theme's file +
  dispatch-phase write discipline).

- **Inherited carry-forward drift `vector.cpp:667` -> `:668`** (the `MFEM_ASSERT` aligned-pass line).
  Recorded above as Proposed change (2). Shared across `inner_product.md:360`,
  `inner-product-fold-specialization.md:59,260`, and this theme `:60,240`. Recommend a follow-up OQ
  `vector-cpp-667-mfem-assert-citation-drift-to-668` for the integrator to sweep all four occurrences
  (the in-theme two are this dispatch's proposed edit; the other two are a sibling/parent
  carry-forward). Bounded, evidenced — does not reopen any law.

- **Carried-forward OQ from the theme (genuinely new to the matrix lift):
  `gram-percell-dot-vs-fused-matmul-tree-loadbearing`** (theme §Open questions). The
  per-cell-`Dot` structure vs a fused `XᴴX` GEMM is a load-bearing-vs-transparent classification
  question for the downstream port; not resolvable from source alone (needs the NLEPS
  convergence-sensitivity analysis). Confirmed as a legitimate open question; not blocking the firm
  value-level lowering. Recommend the integrator surface it (the theme already does at lines 437-441).

- **Sibling-inherited OQs (no new action).** The theme's review of
  `inner-product-fold-specialization` follow-ups (lifting note, weighted-member two-stage tree under
  `apply-linop-lowering-verifier-audit-cohort`, conjugate-pair re-order per-site audit) is sound — this
  theme inherits them, adds the single `nleps.cpp:529` observable-unweighted data point (already in the
  scalar theme's caller inventory), and consumes none as blockers. No fresh OQ needed for those.

- **Range-style inconsistency between siblings (non-blocking, noted not flagged):** the gram theme
  cites `ComplexVector::Dot` as `vector.cpp:263-266` while the sibling uses `:263-267`; and uses
  `:664-672` (with leading blank) in §dispatch vs `:665-672` (tight) in Verified-against. All four
  ranges are in-bounds and capture the construct; not a drift, but a future same-layer-cross-cutter
  pass could normalize the BLAS-1 reduction-kernel citation style across the `dot` / `inner_product` /
  `gram` cohort for consistency. Not in this dispatch's scope.

- **Coverage caveat is honest, not a firmness gate.** The theme's own coverage caveat (the literal
  `XᴴX` build appears at exactly one Palace site, no dedicated NLEPS/deflation unit test) is accurate —
  I confirmed `nleps.cpp:529` is the sole `linalg::Dot(GetComm(), X[i], X[j])` occurrence via
  `search_text`. The firmness resting on (a) the all-pairs law composed with the firm sibling + (b) the
  single build site read directly is sound. No change recommended.

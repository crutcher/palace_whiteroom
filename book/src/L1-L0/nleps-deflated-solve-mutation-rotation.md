---
status: firm
layer: L1>L0
theme: nleps-deflated-solve-mutation-rotation
l1_anchor: book/src/L1/nleps_deflated_solve.md
l0_anchor: palace/linalg/nleps.cpp:504-537
justification: structural
---

# nleps-deflated-solve-mutation-rotation

How the firm L1 [`nleps_deflated_solve`](../L1/nleps_deflated_solve.md) form lowers into its L0
source: the `deflated_solve` lambda inside Palace's `QuasiNewtonSolver` NEP loop
(`palace/linalg/nleps.cpp:504-537`). This is the **block (Schur-complement) solve** of the
extended deflated `(n+k)` system — the solve sibling of
[`nleps-deflated-residual-mutation-rotation`](./nleps-deflated-residual-mutation-rotation.md)
(the residual *applies* the extended deflated operator; this solve *inverts* it). When `k = 0`
it degenerates to one plain big-space [`ksp_solve`](../L1/ksp_solve.md) of `b1`. This entry
completes the NLEPS L1>L0 lowering cohort (with the cycle-023
[`lu-solve-mutation-rotation`](./lu-solve-mutation-rotation.md) and
[`nleps-deflated-residual-mutation-rotation`](./nleps-deflated-residual-mutation-rotation.md)).

## Slug

`nleps-deflated-solve-mutation-rotation`

## Status

`firm` — every constituent of the rewrite is read from a **positive** source site (the
`deflated_solve` lambda, `palace/linalg/nleps.cpp:504-537`, with the source's own block-system +
block-elimination comment at `:508-513`). The big-space block is `opInv->Mult(b1, x1)`
(`:514`), the `k = 0` reduction is the `if (k == 0) { return; }` guard (`:515-518`), the
coordinate RHS is a positive `linalg::Dot` loop (`:519-523`), the Gram `XᴴX` is a positive
`linalg::Dot` double-loop (`:524-531`), the block `S = λI − H` (`:532`), the three
`fullPivLu().solve` solves (`:533-535`), the back-projection `MatVecMult(X, ·)` (`:535`), and
the final `linalg::AXPY(-1.0, …)` (`:536`). The rewrite is a **structural** syntactic expansion
— no sub-part is materialized from negative anchors, so there is no `partly-constructive`
caveat. Every leaf is firm L1/L2 vocabulary read from a positive site
([`ksp_solve`](../L1/ksp_solve.md), [`lu_solve`](../L1/lu_solve.md), [`dot`](../L1/dot.md),
[`axpy`](../L1/axpy.md), [`linear_combination`](../L2/linear_combination.md)). This matches the
firm-on-positive-structure status of the operator this theme lowers
(`book/src/L1/nleps_deflated_solve.md:141`) and of its residual sibling
(`book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md:23`): the laws are syntactic
identities on fully-specified positive source, so the NLEPS test-coverage absence (NLEPS has
zero `test/unit/**` hits) does not gate the firm decision.

## L1 form (LHS)

The pure-functional L1 operator — no destination buffers, no per-use tolerance, no `eig_opInv`
lag in the signature (`book/src/L1/nleps_deflated_solve.md:24-43`):

    nleps_deflated_solve
      :: (K: Solver[NonlinearPencil[N] @ σ], P: DeflationState[N, k], λ: Complex,
          b1: Tensor[N], b2: Vec[k])
         -> DeflatedSolution[N, k]

    type DeflatedSolution[N, k] = { x1: Tensor[N], x2: Vec[k] }

    nleps_deflated_solve(K, P, λ, b1, b2) =
      let x1₀ = ksp_solve(K, b1)                          -- x1 = T(σ)⁻¹·b1   (big-space iterative)
      in if k == 0 then { x1 = x1₀, x2 = [] }             -- no deflation: the plain big-space solve
         else
           let rhs = [ b2(j) − dot(P.X[j], x1₀) | j ← 0..k−1 ]   -- b2 − Xᴴ·x1
               G   = gram(P.X)                            -- XᴴX  (k×k Gram, all-pairs dot)
               S   = λ·I[k] − P.H                          -- k×k linearization block
               SS  = − lu_solve(S, G)                      -- Schur complement  −S⁻¹·(XᴴX)
               x2  = lu_solve(SS, rhs)                     -- x2 = SS⁻¹·(b2 − Xᴴx1)
               x1  = x1₀ − linear_combination(P.X, lu_solve(S, x2))   -- x1 − X·(S⁻¹x2)
           in { x1, x2 }

`K` is the **opaque preconditioned Krylov solver** bound to the extended big-space operator
`T(σ) = K + σC + σ²M + A2(σ)`; `P` is the converged invariant pair `(X, H)` with `X` **not
orthonormal** (raw normalized eigenvectors); `k = 0` is the un-deflated case
(`book/src/L1/nleps_deflated_solve.md:47-54`). The destination buffers, the per-use
`SetRelTol`, and the `eig_opInv` lag are **not** in the L1 signature — they are exactly what
this lowering exposes.

## L0 form (RHS)

The `deflated_solve` lambda — captures `k`, `H`, `X`, `eig_opInv`, `opInv` by reference and
takes `(b1, b2, x1, x2)` with `x1` / `x2` as in-out destination buffers
(`palace/linalg/nleps.cpp:504-537`):

    // nleps.cpp:504 — the source's own statement of the deflated block solve:
    // Linear solve with the extended operator of the deflated problem.
    auto deflated_solve = [&](const ComplexVector &b1, const Eigen::VectorXcd &b2,   // :505-506
                              ComplexVector &x1, Eigen::VectorXcd &x2)                // :507
    {
      // Solve the block linear system                                               // :508
      // |T(σ) U(σ)| |x1| = |b1|                                                      // :509
      // |A(σ) B(σ)| |x2|   |b2|                                                      // :510
      // x1 = T^-1 b1                                                                 // :511
      // x2 = SS^-1 (b2 - A x1) where SS = (B - A T^-1 U) = - X^* X S^-1              // :512
      // x1 = x1 - X S x2                                                             // :513
      opInv->Mult(b1, x1);                                       // :514  x1 := T(σ)⁻¹·b1
      if (k == 0)  // no deflation                               // :515
      {
        return;                                                  // :517
      }
      x2.conservativeResize(k);                                  // :519
      for (int j = 0; j < k; j++)                                // :520
      {
        x2(j) = b2(j) - linalg::Dot(GetComm(), x1, X[j]);        // :522  rhs(j) = b2(j) − X[j]ᴴ·x1
      }
      Eigen::MatrixXcd SS(k, k);                                 // :524
      for (int i = 0; i < k; i++)                                // :525
      {
        for (int j = 0; j < k; j++)                              // :527
        {
          SS(i, j) = linalg::Dot(GetComm(), X[i], X[j]);         // :529  Gram XᴴX(i,j) = X[j]ᴴ·X[i]
        }
      }
      const Eigen::MatrixXcd S = eig_opInv * Eigen::MatrixXcd::Identity(k, k) - H;  // :532  S = λI − H
      SS = -S.fullPivLu().solve(SS);                             // :533  SS := −S⁻¹·(XᴴX)  (Schur complement)
      x2 = SS.fullPivLu().solve(x2);                             // :534  x2 := SS⁻¹·(b2 − Xᴴx1)
      const ComplexVector XSx2 = MatVecMult(X, S.fullPivLu().solve(x2));  // :535  X·(S⁻¹·x2)
      linalg::AXPY(-1.0, XSx2, x1);                              // :536  x1 := x1 − X·(S⁻¹·x2)
    };                                                           // :537

## Rewrite — forward (L1 → L0)

The pure `nleps_deflated_solve(K, P, λ, b1, b2)` rewrites to the `deflated_solve` lambda applied
with destination buffers `x1`, `x2` (in place of the returned `x1`, `x2`). The L0-only material
the L1 signature drops:

- **Destination buffers.** `x1` (a `ComplexVector &`) and `x2` (an `Eigen::VectorXcd &`) are
  output reference parameters overwritten in place (`:514`, `:519-523`, `:533-536`); the L1 form
  returns `{ x1, x2 }` by value. The three call sites pass the *same* `w0`/`w2`, `du`/`du2`
  scratch buffers across iterations (`:542`, `:682`, `:735`) — buffer reuse, a transparent
  L1>L0 trick.
- **Per-use inexact-Newton tolerance.** `opInv->SetRelTol(std::max(ksp_rel_tol, inexact_tol))`
  (`:541`, projection-direction setup; `:734`, restart) and
  `opInv->SetRelTol(std::max(ksp_rel_tol, std::min(inexact_tol, res)))` (`:681`, Newton-step
  solve) are set **outside** the lambda per call site; the `opInv->SetAbsTol(1.0e-12)` floor is
  set once at operator setup (`:502`). These are a load-bearing numerical-Newton choice (avoid
  over-solving when `T(σ)` is near-singular), an L1>L0 concern absorbed at L1 by the opaque `K`.
- **The `eig_opInv` lag.** The big-space operator `T(σ)` bound in `opInv`
  (`opInv->SetOperators(*opA, *opP)`, `:501` / `:732`) and the `S = λI − H` block (`:532`) both
  use the **lagged** eigenvalue `eig_opInv` (set `eig_opInv = eig` at `:474` and at the restart
  `:726`), held fixed across the inner solve while the outer Newton `eig` may have advanced. The
  lag keeps `S` consistent with the `opInv`-bound `T(σ)`; absorbed at L1 by the fixed-`λ`
  signature.

The rewrite proceeds in three sub-patterns. The block-elimination is genuinely coupled: `x2`
depends on `x1` (via the coordinate RHS `b2 − Xᴴx1`, Sub-pattern B) and the final `x1` depends
on `x2` (via the back-projection `x1 − X·S⁻¹x2`, Sub-pattern C) — a `2×2` block solve, not two
independent solves (`book/src/L1/nleps_deflated_solve.md:93`).

### Sub-pattern A — big-space block: `opInv->Mult` → one `ksp_solve` (the un-deflated core)

The big-space part `x1 = T(σ)⁻¹·b1` is one preconditioned Krylov solve against the
extended-problem operator bound in `opInv`:

    opInv->Mult(b1, x1);   // :514   x1 := T(σ)⁻¹·b1

`opInv` is the opaque [`ksp_solve`](../L1/ksp_solve.md) gate — its `T(σ) = K + σC + σ²M + A2(σ)`
operator is built `opA = BuildParSumOperator(...)` and installed `opInv->SetOperators(*opA,
*opP)` at the solver setup (`:498-501`), with the absolute-tolerance floor
`opInv->SetAbsTol(1.0e-12)` (`:502`). The `Mult(b1, x1)` writes the solution into the
destination `x1` (the output-arg convention; `ksp_solve`'s L0 form). When `k == 0` the lambda
returns immediately after this solve (`:515-518`, `if (k == 0) { return; }`) with `x2`
untouched — so the un-deflated case is **exactly** the plain big-space solve `x1 = ksp_solve(K,
b1)`, `x2 = []` (the L1 form's law 1, `book/src/L1/nleps_deflated_solve.md:99`).
`nleps_deflated_solve` strictly extends `ksp_solve` with the deflation block-elimination.

Justification kind: **structural** — `:514` is the syntactic `opInv->Mult` recognized as the
firm `ksp_solve` leaf; the `:515-518` guard is the syntactic `k = 0` reduction.

Citations:
- `palace/linalg/nleps.cpp:514` — `opInv->Mult(b1, x1);` — the big-space block `x1 = T(σ)⁻¹·b1`.
- `palace/linalg/nleps.cpp:515-518` — `if (k == 0) { return; }` — the deflation-present guard;
  the un-deflated reduction to the plain big-space solve.
- `palace/linalg/nleps.cpp:498-502` — `opA = BuildParSumOperator(...)` (`:498-499`),
  `opInv->SetOperators(*opA, *opP)` (`:501`), `opInv->SetAbsTol(1.0e-12)` (`:502`) — the
  extended big-space operator `T(σ)` bound into `opInv` (the `ksp_solve` constructed-operator
  setup; lowering context).

### Sub-pattern B — coordinate block: Gram build + Schur complement + coordinate solve

The coordinate block computes `x2 = SS⁻¹·(b2 − Xᴴ·x1)` with `SS = −S⁻¹·(XᴴX)`. It expands into
the coordinate-RHS extraction, the Gram build, the block `S`, the Schur complement, and the
coordinate solve:

    x2.conservativeResize(k);                                  // :519
    for (int j = 0; j < k; j++)                                // :520
      x2(j) = b2(j) - linalg::Dot(GetComm(), x1, X[j]);        // :522   rhs(j) = b2(j) − X[j]ᴴ·x1
    Eigen::MatrixXcd SS(k, k);                                 // :524
    for (int i = 0; i < k; i++)
      for (int j = 0; j < k; j++)
        SS(i, j) = linalg::Dot(GetComm(), X[i], X[j]);         // :529   Gram XᴴX(i,j) = X[j]ᴴ·X[i]
    const Eigen::MatrixXcd S = eig_opInv * Eigen::MatrixXcd::Identity(k, k) - H;  // :532  S = λI − H
    SS = -S.fullPivLu().solve(SS);                             // :533   SS := −S⁻¹·(XᴴX)
    x2 = SS.fullPivLu().solve(x2);                             // :534   x2 := SS⁻¹·(b2 − Xᴴx1)

Five firm-leaf recognitions:

1. **Coordinate RHS (`:519-523`)** — the `dot` loop computes `rhs(j) = b2(j) − X[j]ᴴ·x1`,
   extracted against the **already-solved** `x1` (Sub-pattern A's result), not against `b1`:
   the Schur back-substitution needs `A·x1 = Xᴴ·(T⁻¹b1)`, so the loop runs **after** the
   big-space solve. Under the fused `linalg::Dot(comm, x, y) = yᴴx`
   ([`dot-mutation-rotation`](./dot-mutation-rotation.md) Sub-pattern A), with `x = x1`,
   `y = X[j]`, the **C++ arg-2 `X[j]`** (the basis vector) is conjugated: `rhs(j) = X[j]ᴴ·x1`.
   This is the L1 `rhs(j) = b2(j) − dot(P.X[j], x1)` — the L1 [`dot`](../L1/dot.md) convention
   conjugates its **arg-1** (`book/src/L1/dot.md:43`), which names the **same** conjugated
   operand `X[j]`. The conjugation is **not re-derived here**; it is cited from
   `dot-mutation-rotation` Sub-pattern A. This is the `Xᴴ·` coordinate-extraction half shared
   with the residual sibling and the L2 `deflate`/`gram` combinators.
2. **Gram build (`:524-531`)** — the `dot` double-loop builds the `k×k` Gram `XᴴX`,
   `SS(i, j) = linalg::Dot(GetComm(), X[i], X[j]) = X[j]ᴴ·X[i]` (`:529`). Because the deflation
   basis `X` is **NOT orthonormal** (raw normalized eigenvectors, no inter-column
   orthogonalization, `palace/linalg/nleps.cpp:606-619`: each converged `v` scaled by `1/‖v‖₂`
   at `:610-611`, stored at `X[k] = v` at `:615`, no Gram-Schmidt), the Schur block carries the
   **full Gram** `XᴴX`, not a trivial identity. This is the L2 [`gram`](../L2/gram.md)
   combinator's positive site, and the load-bearing fact that keeps the oblique `deflate`
   distinct from `orthogonalize` (the cycle-021/022 over-unification guard).
3. **Block `S = λI − H` (`:532`)** — `S = eig_opInv * Identity(k,k) - H` materializes the `k×k`
   linearization block as a dense `Eigen::MatrixXcd` (λ = the lagged `eig_opInv`; `H` the
   redundantly-stored Rayleigh block).
4. **Schur complement (`:533`)** — `SS = -S.fullPivLu().solve(SS)` is the dense `k×k`
   [`lu_solve`](../L1/lu_solve.md) (full-pivot LU, multi-RHS over the `k×k` Gram) computing
   `SS = −S⁻¹·(XᴴX)`. The Gram is **overwritten in place** into the Schur complement (the
   destination `SS` is also the RHS). **The bare `(XᴴX)⁻¹` solve never appears** — the Gram is
   only ever pre-multiplied by `−S⁻¹` before inversion (the deflate-promotion finding; see
   §The block-elimination structure).
5. **Coordinate solve (`:534`)** — `x2 = SS.fullPivLu().solve(x2)` is the single-RHS dense
   [`lu_solve`](../L1/lu_solve.md) computing `x2 = SS⁻¹·(b2 − Xᴴx1)`, again in place over the
   RHS `x2`.

Both `:533` and `:534` are the dense full-pivot-LU `fullPivLu().solve` kernel — the NLEPS
sub-pattern of [`lu-solve-mutation-rotation`](./lu-solve-mutation-rotation.md) (its Sub-pattern
A cites these exact lines, `book/src/L1-L0/lu-solve-mutation-rotation.md:77-78`); the in-place
RHS overwrite (`SS = -...solve(SS)`, `x2 = ...solve(x2)`) is the workspace-reuse trick that
theme records. These dense solves are **distinct** from the iterative big-space `ksp_solve`
(`opInv->Mult`, Sub-pattern A) — different cost models and representations
(`book/src/L1/nleps_deflated_solve.md:56`).

Justification kind: **structural** — `:519-534` are the syntactic `dot` / `lu_solve`
compositions of firm leaves; the conjugation convention is inherited from `dot-mutation-rotation`
Sub-pattern A and the dense-solve kernel from `lu-solve-mutation-rotation` Sub-pattern A.

Citations:
- `palace/linalg/nleps.cpp:519-523` — the coordinate-RHS loop `x2(j) = b2(j) - linalg::Dot(GetComm(),
  x1, X[j])` (statement at `:522`) — `rhs = b2 − Xᴴ·x1`, extracted against the solved `x1`
  (arg-2 = basis vector conjugated, per `dot-mutation-rotation` Sub-pattern A; L1 arg-1
  convention `book/src/L1/dot.md:43`).
- `palace/linalg/nleps.cpp:524-531` — the Gram double-loop `SS(i,j) = linalg::Dot(GetComm(),
  X[i], X[j])` (statement at `:529`) — the `k×k` Gram `XᴴX` (the L2 `gram` positive site).
- `palace/linalg/nleps.cpp:532` — `const Eigen::MatrixXcd S = eig_opInv * Eigen::MatrixXcd::
  Identity(k, k) - H;` — the `k×k` block `S = λI − H` (λ = lagged `eig_opInv`).
- `palace/linalg/nleps.cpp:533` — `SS = -S.fullPivLu().solve(SS);` — the Schur complement
  `SS = −S⁻¹·(XᴴX)` (`lu_solve`, multi-RHS, in place; the Gram overwritten, never solved alone).
- `palace/linalg/nleps.cpp:534` — `x2 = SS.fullPivLu().solve(x2);` — the coordinate solve
  `x2 = SS⁻¹·(b2 − Xᴴx1)` (`lu_solve`, single-RHS, in place).
- `palace/linalg/nleps.cpp:606-619` — deflation-basis growth (normalize `:610-611`, store
  `:615`, no orthogonalization) — the `X`-not-orthonormal fact (the full-Gram-is-load-bearing
  reason).
- `book/src/L1-L0/lu-solve-mutation-rotation.md:77-78` — Sub-pattern A's `SS = -S.fullPivLu()
  .solve(SS)` (`:533`) / `x2 = SS.fullPivLu().solve(x2)` (`:534`) full-pivot-LU dense kernel +
  in-place RHS overwrite (this theme references, not re-derives).
- `book/src/L1-L0/dot-mutation-rotation.md` — Sub-pattern A: the fused `linalg::Dot(comm, x, y)
  = yᴴx` (arg-2-conjugated); reused for the coordinate RHS and the Gram entries.

### Sub-pattern C — back-projection correction: `fullPivLu().solve` ∘ `MatVecMult` ∘ `AXPY`

The final big-space correction `x1 ← x1 − X·(S⁻¹·x2)` is built in two C++ lines (`:535-536`):

    const ComplexVector XSx2 = MatVecMult(X, S.fullPivLu().solve(x2));  // :535   X·(S⁻¹·x2)
    linalg::AXPY(-1.0, XSx2, x1);                                       // :536   x1 := x1 − XSx2

Three firm-leaf recognitions composed:

1. **`S.fullPivLu().solve(x2)`** (`:535`) is the dense `k×k` [`lu_solve`](../L1/lu_solve.md) —
   the **second** application of `S⁻¹` (the first was inside `SS` at `:533`) — computing
   `S⁻¹·x2` into a fresh destination (not in place; the NLEPS fresh-destination form of
   `lu-solve-mutation-rotation`, `book/src/L1-L0/lu-solve-mutation-rotation.md:79`).
2. **`MatVecMult(X, S⁻¹·x2)`** (`:535`) is the back-projection `X·(S⁻¹·x2) = Σⱼ (S⁻¹x2)(j)·X[j]`
   — the length-`k` [`linear_combination`](../L2/linear_combination.md) fold over the deflation
   basis. Its L0 body (`palace/linalg/nleps.cpp:329-347`) zero-initializes `z` (`:337-340`),
   then for each `j` does two real-valued `linalg::AXPBYPCZ` calls (the complex-vector real/imag
   split: `z.Real += y(j).real·X[j].Real − y(j).imag·X[j].Imag`, `z.Imag += y(j).imag·X[j].Real
   + y(j).real·X[j].Imag`, `:343-344`) — the four-real-multiply complex product expanded across
   the `.Real()` / `.Imag()` carriers. The L2>L1 lowering of this fold is
   [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md);
   this theme references its `MatVecMult` realization, it does not re-derive the fold.
3. **`linalg::AXPY(-1.0, XSx2, x1)`** (`:536`) is the [`axpy`](../L1/axpy.md) with `α = −1`
   folding the correction into the big-space destination `x1`: `x1 ← x1 − X·(S⁻¹·x2)`.

The composition order is `lu_solve` first (small-dense `S⁻¹x2`), then `linear_combination`
(big-space fold `X·`), then the `axpy` subtract — matching the L1 `x1 = x1₀ −
linear_combination(P.X, lu_solve(S, x2))`.

Note the source block-comment line `x1 = x1 - X S x2` (`:513`) writes `S` where the *code*
applies `S⁻¹` (the `.solve(x2)` at `:535`); the **realized** arithmetic is `x1 − X·(S⁻¹·x2)`
(`book/src/L1/nleps_deflated_solve.md:91`). The lowering follows the code, not the comment.

Justification kind: **structural** — `:535` is the syntactic composition `MatVecMult ∘
fullPivLu().solve` of two firm leaves; `:536` is the syntactic `axpy` with `α = −1`.

Citations:
- `palace/linalg/nleps.cpp:535` — `const ComplexVector XSx2 = MatVecMult(X, S.fullPivLu().solve
  (x2));` — the back-projection `X·(S⁻¹·x2)`: the `lu_solve` (`S.fullPivLu().solve`) composed
  with `linear_combination` (`MatVecMult(X, ·)`), fresh destination.
- `palace/linalg/nleps.cpp:536` — `linalg::AXPY(-1.0, XSx2, x1);` — the final correction
  `x1 ← x1 − X·(S⁻¹·x2)` (the `axpy` with `α = −1`).
- `palace/linalg/nleps.cpp:329-347` — `MatVecMult(X, y)`: the `X·y` fold body (`z = 0` at
  `:337-340`; per-`j` complex AXPY via two `AXPBYPCZ` on the real/imag carriers at `:343-344`).
- `book/src/L2-L1/linear-combination-fold-specialization.md` — the L2>L1 lowering of the
  `MatVecMult` back-projection fold; live link (this theme references its realization).

## The block-elimination structure — the load-bearing recording

The structural signature of this lowering is that **`S⁻¹` appears twice**: once inside the Schur
complement `SS = −S⁻¹·(XᴴX)` (`:533`) and once in the final back-projection correction
`X·(S⁻¹·x2)` (`:535`). This double appearance of `S⁻¹` is the signature of the Schur-complement
block elimination of the `2×2` extended system whose top block-row is `[T(σ), U(σ)]` and lower
block-row is `[Xᴴ, B(σ)]` (the source's own statement, `:508-513`). It is **not** the
bare-Galerkin `(XᴴX)⁻¹` projection.

This matters for the cycle-022 L2 [`deflate`](../L2/deflate.md) combinator's promotion gate (OQ
`nleps-deflated-solve-firm-landed-deflate-promotion-gate-stays-open`,
`scaffolding/open-questions.md:774`). The Gram `XᴴX` is built here **positively** (`:529`) but
is **never solved alone** — at `:533` it is immediately overwritten into the Schur complement
`SS = −S⁻¹·(XᴴX)`; only `SS⁻¹` (`:534`) and `S⁻¹` (`:533`, `:535`) are ever applied. The bare
`(XᴴX)⁻¹` Galerkin core (the `S = I` degenerate case) is **absent** at this site. So the L2
`deflate` entry's Schur-form pipeline is firm-on-this-site, but its bare-Galerkin-core
sub-part's promotion still gates on a positive bare-Gram-solve site **outside** `nleps.cpp`
(ROM / eigensolver-locking). This theme **confirms** (does not change) the cycle-022 `deflate`
`partly-constructive` verdict and does **not** touch the L2 `deflate` entry (out of scope).

Per the CLAUDE.md trick taxonomy this is a **load-bearing** recording (the block-elimination
structure is part of the algorithm, not a transparent rewrite): collapsing the double `S⁻¹` into
a bare `(XᴴX)⁻¹` projection would silently assume `S = I` (i.e. `λI − H = I`), changing the
algorithm. The over-unification guard from the operator entry
(`book/src/L1/nleps_deflated_solve.md:114,:137`) is carried here.

## Applicability conditions

The rewrite preserves semantics when:

1. **The pencil `T(σ)` is bound exactly as for the solver setup** — `opA = BuildParSumOperator
   ({1, σ, σ², 1}, {opK, opC, opM, opA2}, true)` installed via `opInv->SetOperators` (`:498-501`),
   at the **lagged** `σ = eig_opInv` (`:474`, `:726`). The big-space block solves against this
   bound operator (`:514`); the `S = λI − H` block (`:532`) uses the same lagged `λ` — the two
   are consistent within one call.
2. **Element type is complex-only** — the NEP pencil and the `ComplexVector` /
   `Eigen::VectorXcd` / `Eigen::MatrixXcd` carriers. No real specialization is witnessed.
3. **The deflation cardinality `k` is variadic** — it grows by one per converged eigenpair
   (`:606-619`); the rewrite is parameterized by `k`, with the `k = 0` branch
   (`if (k == 0) { return; }`, `:515-518`) the un-deflated degeneration to the plain big-space
   solve.
4. **In-place destination overwrite is permitted because the destinations are dead-on-entry
   scratch.** `x1`/`x2` are overwritten (`:514`, `:519-523`, `:533-536`); the call sites pass
   reusable scratch (`w0`/`w2` `:542`/`:735`, `du`/`du2` `:682`). The `SS = -...solve(SS)` /
   `x2 = ...solve(x2)` RHS-overwrite is the `lu-solve-mutation-rotation` workspace-reuse trick.
5. **The block elimination is coupled** — `x2` reads the solved `x1` (`:522`), the final `x1`
   reads `x2` (`:535-536`); the execution order (`:514` → `:519-534` → `:535-536`) is
   load-bearing, not a free reordering.
6. **Single-rank scope** (CLAUDE.md "Scope"): the `Mpi::GlobalSum` inside the `linalg::Dot`
   reductions (`:522`, `:529`) lowers to a local no-op on one rank but is structurally present
   and carries the bit-deterministic-reduction-order trade-off (inherited from
   `dot-mutation-rotation`). The `k×k` dense `Eigen` solves (`:533-535`) are rank-local by
   construction (the coordinate space is replicated on all ranks).

## Justification kind

**Structural** — the rewrite is the syntactic expansion of one pure L1 form into the L0
destination-buffer composition. Three structural recognitions carry the theme: (A) `:514` is the
firm `ksp_solve` big-space block, with the `:515-518` guard the `k = 0` reduction; (B)
`:519-534` are the `dot` (coordinate RHS + Gram) / `lu_solve` (Schur complement + coordinate
solve) compositions of firm leaves; (C) `:535-536` are the `MatVecMult ∘ fullPivLu().solve`
(back-projection) + `axpy` (`α = −1`) compositions. The one load-bearing non-trivial recording
is the **block-elimination structure** (the double `S⁻¹`, the never-bare Gram solve), read
straight off the verified site; it does not change the structural character of the lowering but
must be carried, not absorbed. The in-place destination overwrite, the per-use `SetRelTol`
tolerance, and the `eig_opInv` lag are L1>L0 residues recorded above; the destination-is-RHS
aliasing at `:533-534` is the transparent workspace-reuse trick from
`lu-solve-mutation-rotation`.

## Speculative L1 operators

**None.** Every constituent is **already firm L1/L2 vocabulary**:
[`ksp_solve`](../L1/ksp_solve.md) (firm), [`lu_solve`](../L1/lu_solve.md) (firm, cycle-022),
[`dot`](../L1/dot.md) (firm), [`axpy`](../L1/axpy.md) (firm),
[`linear_combination`](../L2/linear_combination.md) (firm L2). This theme composes existing firm
leaves; it proposes no new rough-in operators. The Gram `XᴴX` build is the L2
[`gram`](../L2/gram.md) combinator's positive site and the back-projection is the L2 `deflate`
combinator's constituent, but those L2 combinators are named here only to mark the upward
fan-out boundary (and the deflate-promotion guard) — they are **not** part of this theme.

## Verified-against

L0 evidence ranges (self-verified via `palace-codemap` `read_range` / `search_text` this
invocation — producer-citation self-verification, `verify-citation-range`):

- `palace/linalg/nleps.cpp:504-537` — the complete `deflated_solve` lambda (the positive L0
  site). Comment `:508-513` names the block system + Schur elimination in the source's own words.
  **Self-verified** (`read_range` 503-545 + 504-523 + 524-537).
- `palace/linalg/nleps.cpp:505-507` — the lambda signature `[&](const ComplexVector &b1, const
  Eigen::VectorXcd &b2, ComplexVector &x1, Eigen::VectorXcd &x2)`. **Self-verified** (`read_range`
  504-523).
- `palace/linalg/nleps.cpp:514` — `opInv->Mult(b1, x1);`. **Self-verified** (`read_range`
  504-523).
- `palace/linalg/nleps.cpp:515-518` — `if (k == 0) { return; }`. **Self-verified** (`read_range`
  504-523).
- `palace/linalg/nleps.cpp:519-523` — coordinate-RHS loop `x2(j) = b2(j) - linalg::Dot(GetComm(),
  x1, X[j])` (statement `:522`). **Self-verified** (`read_range` 504-523).
- `palace/linalg/nleps.cpp:524-531` — Gram double-loop `SS(i, j) = linalg::Dot(GetComm(), X[i],
  X[j])` (statement `:529`). **Self-verified** (`read_range` 524-537).
- `palace/linalg/nleps.cpp:532` — `const Eigen::MatrixXcd S = eig_opInv * Eigen::MatrixXcd::
  Identity(k, k) - H;`. **Self-verified** (`read_range` 524-537).
- `palace/linalg/nleps.cpp:533-535` — `SS = -S.fullPivLu().solve(SS);` (`:533`),
  `x2 = SS.fullPivLu().solve(x2);` (`:534`), `const ComplexVector XSx2 = MatVecMult(X,
  S.fullPivLu().solve(x2));` (`:535`). **Self-verified** (`read_range` 524-537 + `search_text`
  `fullPivLu\(\)\.solve` → lines 533/534/535).
- `palace/linalg/nleps.cpp:536` — `linalg::AXPY(-1.0, XSx2, x1);`. **Self-verified** (`read_range`
  524-537).
- `palace/linalg/nleps.cpp:329-347` — `MatVecMult(X, y)` body (the `X·y` fold; `z = 0` at
  `:337-340`, per-`j` complex AXPY via two `AXPBYPCZ` at `:343-344`). **Self-verified**
  (`read_range` 329-347).
- `palace/linalg/nleps.cpp:474` — `eig_opInv = eig;  // eigenvalue estimate used in the (lagged)
  preconditioner`. **Self-verified** (`read_range` 470-476 + `search_text` `eig_opInv =`).
- `palace/linalg/nleps.cpp:498-502` — `opA = BuildParSumOperator(...)` (`:498-499`),
  `opInv->SetOperators(*opA, *opP)` (`:501`), `opInv->SetAbsTol(1.0e-12)` (`:502`).
  **Self-verified** (`read_range` 495-502).
- `palace/linalg/nleps.cpp:541-542` — `opInv->SetRelTol(std::max(ksp_rel_tol, inexact_tol));`
  (`:541`), `deflated_solve(c, c2, w0, w2);` (`:542`) — projection-direction setup call.
  **Self-verified** (`read_range` 503-545 + `search_text` → lines 541/542).
- `palace/linalg/nleps.cpp:681-682` — `opInv->SetRelTol(std::max(ksp_rel_tol, std::min(inexact_tol,
  res)));` (`:681`), `deflated_solve(z, z2, du, du2);` (`:682`) — Newton-step solve call.
  **Self-verified** (`read_range` 678-683 + `search_text` → lines 681/682).
- `palace/linalg/nleps.cpp:726` / `:732-735` — `eig_opInv = eig;` (`:726`), `opInv->SetOperators
  (*opA, *opP);` (`:732`), `opInv->SetRelTol(std::max(ksp_rel_tol, inexact_tol));` (`:734`),
  `deflated_solve(c, c2, w0, w2);` (`:735`) — restart projection-direction setup. **Self-verified**
  (`read_range` 732-736 + `search_text` `eig_opInv =`/`SetOperators` → lines 726/732/734/735).
- `palace/linalg/nleps.cpp:606-619` — deflation-basis growth (`X`-not-orthonormal, variadic-`k`).
  **Self-verified** (cited in the firm operator entry `book/src/L1/nleps_deflated_solve.md:175`;
  consistent with this dispatch's reads).

L1 / cross-theme anchors:

- `book/src/L1/nleps_deflated_solve.md` — the firm L1 operator this theme lowers (signature
  `:24-43`, Semantics `:60-93`, laws `:99-114`, Status `:141`, Evidence `:154-185`).
- `book/src/L1-L0/lu-solve-mutation-rotation.md:69-133` — Sub-pattern A (NLEPS full-pivot LU,
  `:533-535`); the dense-solve kernel + in-place RHS overwrite this theme references.
- `book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md` — the solve/residual sibling
  (the residual applies the extended deflated operator where this solve inverts it; apply/inverse
  duality, `book/src/L1/nleps_deflated_solve.md:107`).
- `book/src/L1-L0/dot-mutation-rotation.md` — Sub-pattern A (fused `linalg::Dot`); reused for the
  coordinate RHS (`:522`) and the Gram entries (`:529`).
- `book/src/L1/dot.md:43` — the L1 `⟨x, y⟩ = xᴴ y` arg-1-conjugated convention.
- `book/src/L1/ksp_solve.md` — the big-space constructed-operator solve gate this theme's
  Sub-pattern A is.
- `book/src/L1/lu_solve.md` — the small-dense direct-solve leaf realizing the three
  `fullPivLu().solve` solves at `:533-535`.
- `book/src/L1/axpy.md` — the `α = −1` final-correction fold (`:536`).
- `book/src/L2/linear_combination.md` — the `X·(S⁻¹x2)` back-projection (`MatVecMult(X, ·)` at
  `:535`); live link.
- `book/src/L2-L1/linear-combination-fold-specialization.md` — the L2>L1 lowering of the
  `MatVecMult` back-projection fold; live link.
- `book/src/L2/index.md` — the cycle-022 `gram` (firm) / `deflate` (partly-constructive) L2
  dep-map rows: the Gram positive site (`:529`) and the over-unification / deflate-promotion
  guard.
- No dedicated unit test: NLEPS has zero `test/unit/**` hits (same absence as `eigsolve` /
  `apply_nonlinear_pencil` / `nleps_deflated_residual` / `nleps_deflated_solve`); the firm
  decision rests on exhaustive positive structural citation.

---
agent: harvester
invoked_at: 2026-05-29T09:29:43Z
scope: L1 operator: nleps_deflated_solve
status: pending
integrated_at: 2026-05-29T10:46:32Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (staging row 1). NEW firm L1 operator book/src/L1/nleps_deflated_solve.md; L1 firm 16->17; SUMMARY + L1/index dep-map + firm-list bullet + Firm-count headline 16->17. 3 OQs promoted. Deflate bare-Galerkin-core promotion gate stays open (confirmed, not changed). No gate hits."
inputs:
  - palace/linalg/nleps.cpp:504-537 (the `deflated_solve` lambda — primary positive site)
  - palace/linalg/nleps.cpp:542,682,735 (the three call sites)
  - book/src/L1/nleps_deflated_residual.md (sibling NEP-interior atom; over-unification distinction at :86,:109)
  - book/src/L1/lu_solve.md (firm cycle-022; already cites :533-535 of this lambda)
  - book/src/L1/ksp_solve.md, dot.md (firm leaves)
  - book/src/L2/index.md:42,59-60 (cycle-022 deflate/gram rough-in+partly-constructive dep-map rows — the promotion question)
  - cycle-022 deflate partly-constructive verdict (the bare-Galerkin-core constructive sub-part)
---

# CYCLE: Formalize nleps_deflated_solve at L1

## Summary
`nleps_deflated_solve` is the **deflated linear solve** inside Palace's quasi-Newton NEP step — the `deflated_solve` lambda at `palace/linalg/nleps.cpp:504-537`. It solves the extended/deflated `(n+k)×(n+k)` block system that couples the big-space solve `T(σ)⁻¹b1` with the small-dense deflation-coordinate (Schur) block. By block elimination it composes: the big-space [`ksp_solve`](./ksp_solve.md) (`opInv->Mult`, :514), the Gram build `XᴴX` via [`dot`](./dot.md) (:529), the small-dense [`lu_solve`](./lu_solve.md) on `S = λI − H` and on the Schur block `SS = −S⁻¹(XᴴX)` (`fullPivLu().solve`, :533-535), the coordinate-RHS extraction `b2 − Xᴴx1` via `dot` (:522), and the back-projection `X·(S⁻¹x2)` (L2 [`linear_combination`](../L2/linear_combination.md) via `MatVecMult`, :535) folded into `x1` via [`axpy`](./axpy.md) (`AXPY`, :536). It is the **solve** sibling of the firm [`nleps_deflated_residual`](./nleps_deflated_residual.md) (the **residual**); they share constituents but compute different things. Every constituent is read from the single positive Schur-solve lambda and the laws are syntactic identities, so the entry lands **`firm`** (L1 firm 16 → 17).

**Deflate-promotion finding (load-bearing for the integrator/meta-phase):** the lambda exhibits the bare-Galerkin projector core `I − X(XᴴX)⁻¹Xᴴ` **only in Schur-wrapped form, NOT positively as a bare Galerkin core.** The Gram `XᴴX` *is* built positively (:529), but it is **never solved alone** — it is immediately pre-multiplied by `−S⁻¹` into the Schur complement `SS = −S⁻¹(XᴴX)` (:533) and only `SS⁻¹` (and `S⁻¹`) are ever applied (:534-535). The bare `(XᴴX)⁻¹` solve never appears. **Therefore `deflate` should NOT be promoted to firm by this landing** — the cycle-022 `partly-constructive` verdict stands: this is the positive Schur-form site (which is already firm in the `deflate` entry), not the bare-Galerkin source site the promotion gates on. Detail in §"Deflate-promotion assessment" below. (I do NOT touch the `deflate` entry — out of scope.)

## Proposed changes

```new:book/src/L1/nleps_deflated_solve.md
# nleps_deflated_solve

Mutation-lifted **deflated linear solve** of the nonlinear eigenvalue problem (NEP): given an extended right-hand side `[b1, b2]`, solve the extended deflated block system of size `n + k` and return the extended solution `[x1, x2]`. The linear solve inside Palace's quasi-Newton NEP step (`QuasiNewtonSolver`) once the converged invariant pair `(X, H)` has been deflated out — the operator that produces the projection direction `w0` and the (damped) Newton step `du` the loop commits.

## Context

Palace's `QuasiNewtonSolver` (`palace/linalg/nleps.cpp`) computes eigenpairs of the NEP `T(λ)·x = 0` for the pencil `T(λ) = K + λC + λ²M + A2(λ)` one at a time, deflating each converged eigenpair so the next solve cannot re-converge to it. The deflation scheme is SLEPc-NEP's with minimality index 1 (Effenberger 2013; Jarlebring–Koskela–Mele 2018 — `palace/linalg/nleps.cpp:354-362`). It works on an **extended problem of size `n + k`**: the converged eigenpairs are stored as an invariant pair — a basis `X = [X[0], …, X[k−1]]` of `k` `ComplexVector`s of length `n` (`palace/linalg/nleps.cpp:401`) plus a `k×k` complex matrix `H` (the Rayleigh-quotient block, `palace/linalg/nleps.cpp:397`). An extended vector is the pair `[v, v₂]` with `v : Tensor[N]` (the big space) and `v₂ : Vec[k]` (the small redundant coordinate space).

`nleps_deflated_solve` is the function that, given the eigenvalue estimate `λ` (the lagged preconditioner eigenvalue `eig_opInv`, `palace/linalg/nleps.cpp:474`) and an extended RHS `[b1, b2]`, produces the extended solution `[x1, x2]` of the deflated linear system. The source's own block statement (`palace/linalg/nleps.cpp:508-513`):

```text
| T(σ) U(σ) | | x1 |   | b1 |
| A(σ) B(σ) | | x2 | = | b2 |
x1 = T^-1 b1
x2 = SS^-1 (b2 - A x1)   where SS = (B - A T^-1 U) = - X^* X S^-1
x1 = x1 - X S x2
```

It is the **solve** sibling of [`nleps_deflated_residual`](./nleps_deflated_residual.md) (the **residual**). The residual *evaluates* the extended deflated operator on a trial vector; this operator *inverts* it on a RHS. They share the same deflation invariant pair `(X, H)` and the same `S = λI − H` block, and both use the `Xᴴ·` coordinate extraction and the `X·` back-projection — but the residual couples through `(λI − H)⁻¹` while the solve couples through the **Schur complement** `SS = −S⁻¹(XᴴX)` (the lower-right block's elimination), an inverse-direction object. It sits in the interior of the [`eigsolve`](./eigsolve.md) gate's `direct_newton` orchestration variant — `eigsolve` treats `QuasiNewtonSolver` as one opaque orchestration; `nleps_deflated_solve` is the per-step linear-solve atom the deflated branch of that orchestration is built from. The L0 NLEPS reference note is [`L0/eigensolver-wrapper`](../L0/eigensolver-wrapper.md).

## Signature

```text
nleps_deflated_solve
  :: (K: Solver[NonlinearPencil[N] @ σ], P: DeflationState[N, k], λ: Complex,
      b1: Tensor[N], b2: Vec[k])
     -> DeflatedSolution[N, k]

type DeflatedSolution[N, k] = { x1: Tensor[N], x2: Vec[k] }

nleps_deflated_solve(K, P, λ, b1, b2) =
  let x1₀ = ksp_solve(K, b1)                          -- x1 = T(σ)⁻¹ · b1   (big-space iterative)
  in if k == 0 then { x1 = x1₀, x2 = [] }             -- no deflation: the plain big-space solve
     else
       let c   = [ b2(j) − dot(P.X[j], b1?…)…  ]       -- (see Semantics; uses x1₀ not b1)
           rhs = [ b2(j) − dot(P.X[j], x1₀) | j ← 0..k−1 ]   -- b2 − Xᴴ·x1
           G   = gram(P.X)                            -- XᴴX  (k×k Gram, all-pairs dot)
           S   = λ·I[k] − P.H                          -- k×k linearization block
           SS  = − lu_solve(S, G)                      -- Schur complement  −S⁻¹·(XᴴX)
           x2  = lu_solve(SS, rhs)                     -- x2 = SS⁻¹·(b2 − Xᴴx1)
           x1  = x1₀ − linear_combination(P.X, lu_solve(S, x2))   -- x1 − X·(S⁻¹x2)
       in { x1, x2 }
```

(The `c`/`rhs` line is shown once in its committed form `rhs = b2 − Xᴴ·x1₀`; the duplicated sketch line is removed in Semantics — `b1` is solved into `x1₀` first, then the coordinate RHS is extracted against `x1₀`.) Shape contract (bunsen-style, named axes):

- `K` — `Solver[NonlinearPencil[N] @ σ]` — the **opaque preconditioned Krylov solver** bound to the extended-problem big-space operator `T(σ) = K + σC + σ²M + A2(σ)` (built by `BuildParSumOperator` and installed via `opInv->SetOperators(*opA, *opP)`, `palace/linalg/nleps.cpp:495-501`). This is the same constructed-operator type as [`ksp_solve`](./ksp_solve.md)'s primary argument: its inner Krylov method, preconditioner, and tolerances are bound at construction. The instantiation point `σ` is the (lagged) eigenvalue estimate; the *solve* tolerance is adjusted per use (`opInv->SetRelTol`, `palace/linalg/nleps.cpp:541`) — an L1>L0 inexact-Newton concern, not part of the signature. Read-only.
- `P` — `DeflationState[N, k]` — the converged invariant pair: `P.X : Basis[N, k]` (the `k` converged eigenvectors over the big axis `N`, the deflation basis; **not** orthonormalized — see Semantics) and `P.H : Matrix[k, k]` (the Rayleigh block, complex). Read-only. `k = 0` is the un-deflated case.
- `λ` — `Complex` — the eigenvalue estimate used to form the `k×k` block `S = λI − H`. At the L0 site this is `eig_opInv`, the **lagged** preconditioner eigenvalue (`palace/linalg/nleps.cpp:474`, `:532`), held fixed across the inner solve while the outer `eig` may be updated; the lag is a numerical-Newton choice (it keeps `S` consistent with the `opInv`-bound operator), recorded as a non-law below.
- `b1` — `Tensor[N]` — the big-space part of the extended RHS. Read-only.
- `b2` — `Vec[k]` — the small redundant-coordinate part of the extended RHS. Read-only.
- result — `DeflatedSolution[N, k]` — `x1 : Tensor[N]` (big-space solution), `x2 : Vec[k]` (coordinate-space solution).

The axis `N` is uniform across the big-space operator, `P.X`, `b1`, and `x1` (the eigenproblem is square; the deflation basis lives in the same big space). The deflation-cardinality axis `k` is uniform across `P.X`, `P.H`, `b2`, and `x2`; it is **variadic-in-`k`** — `k` grows by one per converged eigenpair (`palace/linalg/nleps.cpp:606-619`), so `nleps_deflated_solve` is parameterized by basis size, not a family of fixed-`k` specializations. Element type is **complex-only** (inherited from the complex NEP pencil and the `Eigen::VectorXcd` / `ComplexVector` carriers).

`S = λI[k] − H` and `SS = −S⁻¹·(XᴴX)` are the two `k×k` dense blocks; both are solved by the dense [`lu_solve`](./lu_solve.md) (`Eigen::fullPivLu().solve`, `palace/linalg/nleps.cpp:533-535`), **distinct** from the iterative big-space [`ksp_solve`](./ksp_solve.md) (`opInv->Mult`, `palace/linalg/nleps.cpp:514`). The two solve kinds never merge into one operator (their cost models and representations differ — `ksp_solve` is iterative-to-tolerance and opaque; `lu_solve` is direct on a materialized dense matrix).

## Semantics

`nleps_deflated_solve(K, P, λ, b1, b2)` solves the extended deflated block system by **block (Schur-complement) elimination** of the `2×2` system whose top block-row is `[T(σ), U(σ)]` and whose lower block-row is `[A(σ), B(σ)]`, with `A(σ) = Xᴴ`, `U(σ) = T(σ)·X·(λI−H)⁻¹`, and the Schur complement `SS = B − A·T(σ)⁻¹·U = −XᴴX·S⁻¹` (the source's own statement, `palace/linalg/nleps.cpp:508-513`). The committed elimination is:

```text
x1 = T(σ)⁻¹·b1                          -- big-space solve (opInv->Mult)
x2 = SS⁻¹·(b2 − A·x1) = SS⁻¹·(b2 − Xᴴ·x1)
x1 = x1 − X·(S·x2)?  →  x1 = x1 − X·(S⁻¹·x2)   -- (the realized form; see point 4)
```

Concretely, in execution order (`palace/linalg/nleps.cpp:514-536`):

```text
x1  = ksp_solve(K, b1)                   -- :514   T(σ)⁻¹·b1
if k == 0: return { x1, x2 = [] }        -- :515-518   un-deflated
rhs(j) = b2(j) − ⟨X[j], x1⟩              -- :522   b2 − Xᴴ·x1   (coordinate RHS)
G  = [ ⟨X[i], X[j]⟩ ]_{i,j}              -- :529   XᴴX   (k×k Gram)
S  = λI − H                              -- :532   k×k block
SS = − lu_solve(S, G)                    -- :533   −S⁻¹·(XᴴX)   (Schur complement)
x2 = lu_solve(SS, rhs)                   -- :534   SS⁻¹·(b2 − Xᴴx1)
x1 = x1 − linear_combination(X, lu_solve(S, x2))   -- :535-536   x1 − X·(S⁻¹·x2)
```

The L1 form is pure-functional: the same `(K, P, λ, b1, b2)` yields the same `DeflatedSolution`. The L0 source overwrites the destination buffers `x1` (≡ the caller's `w0`/`du`) and `x2` (≡ `w2`/`du2`) in place; those destination bindings, the per-use `SetRelTol` inexact-Newton tolerance, and the `eig_opInv` lag are L1>L0 lowering concerns, not part of the L1 signature.

Five semantic points are load-bearing and recorded rather than smoothed:

**(1) The `k = 0` case is exactly the plain big-space `ksp_solve`.** When no eigenpairs have converged (`palace/linalg/nleps.cpp:515-518`, `if (k == 0) { return; }`) the lambda returns immediately after `opInv->Mult(b1, x1)` with `x2` untouched (empty). So `nleps_deflated_solve(K, P=⟨[],[]⟩, λ, b1, []) = { x1 = ksp_solve(K, b1), x2 = [] }` — `nleps_deflated_solve` strictly extends [`ksp_solve`](./ksp_solve.md) with the deflation block-elimination. This mirrors the `k = 0` reduction of the sibling [`nleps_deflated_residual`](./nleps_deflated_residual.md) (its law 1 reduces to a bare pencil apply); here the bare case is a bare big-space solve.

**(2) The coordinate RHS is `b2 − Xᴴ·x1`, extracted against the *already-solved* `x1`, not against `b1`.** The Schur back-substitution needs `A·x1 = Xᴴ·(T⁻¹b1)`, so the `dot` loop (`palace/linalg/nleps.cpp:520-523`) runs **after** the big-space solve (`:514`) and reads the solved `x1`: `rhs(j) = b2(j) − ⟨X[j], x1⟩` (`:522`, `linalg::Dot(GetComm(), x1, X[j])`). The conjugated operand is the **basis vector** `X[j]` — under the C++ free-function order `linalg::Dot(comm, x, y) = yᴴx` the **second** C++ argument (`X[j]`) is conjugated, which is the **first** argument of the L1 [`dot`](./dot.md) convention `⟨x, y⟩ = xᴴy` (`book/src/L1/dot.md:43`). Both framings name the same conjugated operand `X[j]`. This is the same `Xᴴ·` coordinate-extraction half shared with `nleps_deflated_residual` and the L2 `deflate` combinator.

**(3) The deflation basis `X` is NOT orthonormal — the Schur block carries the Gram `XᴴX`.** `X` stores raw normalized eigenvectors (`palace/linalg/nleps.cpp:606-619`: each converged `v` is scaled by `1/‖v‖₂` at `:610-611` and stored at `X[k] = v` at `:615`; there is no inter-column orthogonalization). Because the columns are non-orthonormal, the Schur complement carries the **full Gram matrix** `XᴴX` (built by the `dot` double-loop, `palace/linalg/nleps.cpp:524-531`, `SS(i,j) = ⟨X[i], X[j]⟩`), not a trivial identity. This is the load-bearing fact that distinguishes the oblique `deflate` projection from `orthogonalize` (the cycle-021/022 over-unification guard), and it is the Gram `XᴴX` build that the L2 [`gram`](../L2/gram.md) combinator names. **Note (deflate-promotion):** the Gram is built positively here, but it is *only* solved Schur-wrapped — see §"L1 vs L0 distinction" and the report's deflate-promotion finding; the bare `(XᴴX)⁻¹` solve never appears.

**(4) The Schur complement `SS = −S⁻¹·(XᴴX)` is the inverse-direction coupling vs. the residual's `(λI−H)⁻¹`.** The source forms `S = λI − H` (`palace/linalg/nleps.cpp:532`), then `SS = −S.fullPivLu().solve(SS) = −S⁻¹·(XᴴX)` (`:533`, the Gram is overwritten into the Schur complement), then `x2 = SS.fullPivLu().solve(x2)` (`:534`). The final big-space correction is `XSx2 = MatVecMult(X, S.fullPivLu().solve(x2)) = X·(S⁻¹·x2)` (`:535`) folded in by `linalg::AXPY(-1.0, XSx2, x1)`, i.e. `x1 ← x1 − X·(S⁻¹·x2)` (`:536`). Note the block-comment line `x1 = x1 - X S x2` (`:513`) writes `S` where the *code* applies `S⁻¹` (the `.solve(x2)` at `:535`); the realized arithmetic is `x1 − X·(S⁻¹·x2)`, and the back-projection back-solves through `S` again. This double appearance of `S⁻¹` (once in `SS`, once in the final correction) is the structural signature of the Schur-complement block elimination; it is **not** the bare-Galerkin `(XᴴX)⁻¹` projection.

**(5) The result couples the big and small spaces — it is not separable.** `x2` depends on `x1` (via the coordinate RHS `b2 − Xᴴx1`, point 2) and the final `x1` depends on `x2` (via the back-projection `x1 − X·S⁻¹x2`, point 4). The extended solve is genuinely a `2×2` block solve, not two independent solves — this is what makes `nleps_deflated_solve` an operator in its own right rather than a `ksp_solve` plus an unrelated `lu_solve`.

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Deflation reduction (`k = 0`)**: `nleps_deflated_solve(K, ⟨X=[], H=[]⟩, λ, b1, []) = { x1 = ksp_solve(K, b1), x2 = [] }`. The empty-deflation case is the plain big-space solve. Witnessed by the `if (k == 0) { return; }` guard (`palace/linalg/nleps.cpp:515-518`). This is the bridge law to [`ksp_solve`](./ksp_solve.md): the deflated solve is its deflation extension. (The exact `ksp_solve` sibling of `nleps_deflated_residual`'s law-1 reduction to `apply_nonlinear_pencil`.)

2. **Linearity in the extended RHS** (at fixed `K`, `P`, `λ`): the map `(b1, b2) ↦ (x1, x2)` is **linear** — `solve(α·(b1,b2) + β·(b1',b2')) = α·solve(b1,b2) + β·solve(b1',b2')` for scalars `α, β`. Holds because, at fixed `K`/`P`/`λ`, every step is a linear map of its input: `ksp_solve(K, ·)` is the linear `T(σ)⁻¹` (firm `ksp_solve` law), the coordinate RHS `b2 − Xᴴ·x1` is linear (the fixed `dot`-fold composed with the linear `x1`), `lu_solve(SS, ·)` and `lu_solve(S, ·)` are the linear `SS⁻¹`, `S⁻¹` (firm [`lu_solve`](./lu_solve.md) law 2), and `linear_combination(X, ·)` is linear. The composite is therefore the action of the fixed inverse extended operator `[[T(σ), U(σ)], [Xᴴ, B(σ)]]⁻¹` on `[b1, b2]`. In particular `solve(0, 0) = (0, 0)` (zero-RHS annihilation). The big-space residual operator `nleps_deflated_residual` IS the (fixed-`(λ,P)`) extended-operator apply; **`nleps_deflated_solve` is its inverse on the same extended space** (modulo the residual's `(λI−H)⁻¹` coupling vs. the solve's Schur-eliminated coupling — they realize the same `2×2` operator's apply and inverse respectively, see law 5).

3. **Solve inverts the extended operator (defining property)**: applying the extended deflated operator (the sibling `nleps_deflated_residual`'s big-space/coordinate map, with `b2 = Xᴴ·b1` set up consistently) to `(x1, x2) = nleps_deflated_solve(K, P, λ, b1, b2)` recovers `(b1, b2)`, modulo the `ksp_solve` inner tolerance (the big-space block is solved iteratively-to-tolerance, not exactly). The coordinate and back-projection blocks are exact (dense `lu_solve`); the big-space block is exact-to-`ksp` tolerance. Recorded with the tolerance caveat because the big-space solve is iterative.

4. **Coordinate-block solve is the dense Schur inverse**: `x2 = lu_solve(SS, b2 − Xᴴ·x1)` with `SS = −lu_solve(S, gram(X))`. This factors the coordinate block entirely through firm vocabulary: two `lu_solve`s (one for `SS`, one against `SS`), one `gram`/`dot` fold for `XᴴX`, one `dot` fold for `Xᴴx1`. The nested `lu_solve(SS, ·)` over `SS = −lu_solve(S, XᴴX)` is the witnessed nested-solve shape recorded as `lu_solve` law 5 (`book/src/L1/lu_solve.md:59`).

5. **Apply/inverse duality with `nleps_deflated_residual`**: `nleps_deflated_solve(K, P, λ, ·, ·)` and `nleps_deflated_residual(T, λ, P, ·, ·)` are the inverse and the apply of (essentially) the same fixed-`(λ, P)` extended linear operator over `ℂ^{n+k}` — they share the deflation pair `(X, H)`, the block `S = λI − H`, the `Xᴴ·` coordinate extraction, and the `X·` back-projection. They differ in coupling realization (the residual couples through `(λI−H)⁻¹` directly; the solve couples through the Schur complement `SS = −S⁻¹XᴴX`) and in the big-space block (the residual *applies* `T(λ)`; the solve *inverts* `T(σ)` via `ksp_solve`). Recorded as the structural relationship, not a literal `solve ∘ residual = id` identity (the residual's `T(λ)` and the solve's `T(σ)` use the un-lagged vs lagged eigenvalue; the big-space inverse is tolerance-bounded — see the non-laws).

Laws that explicitly **do not** hold:

- **Linearity / polynomiality in `λ`**: `nleps_deflated_solve(K, P, ·, b1, b2)` is **not** linear or polynomial in `λ`. The block `S = λI − H` and its inverse `S⁻¹`, the Schur complement `SS = −S⁻¹XᴴX` and its inverse `SS⁻¹`, and the lagged-`σ`-bound operator `T(σ)` inside `K` all make the solve a non-polynomial (rational) function of `λ`. Recorded so the eigenvalue-correction step does not assume polynomial structure across `λ`.
- **Exactness of the big-space block**: the `x1` block is solved iteratively to the `ksp_solve` tolerance (`opInv->SetRelTol`, `opInv->SetAbsTol(1.0e-12)`, `palace/linalg/nleps.cpp:502`, `:541`), so `solve` inverts the extended operator only **to that tolerance**, not exactly (contrast the dense `lu_solve` coordinate block, which is exact-modulo-roundoff). Law 3 carries the tolerance caveat. Load-bearing: the inexact-Newton tolerance loosening (`std::max(ksp_rel_tol, inexact_tol)`, `:541`; `std::max(ksp_rel_tol, std::min(inexact_tol, res))`, `:681`) is a deliberate numerical choice (avoid over-solving when `T(σ)` is near-singular), an L1>L0 concern.
- **`σ = λ` (no lag)**: the bound operator `K` uses the **lagged** eigenvalue `σ = eig_opInv` (`palace/linalg/nleps.cpp:474`, `:532`) while the outer Newton `eig` may have advanced. So the `S = λI − H` block and the `K`-bound `T(σ)` are evaluated at the *same lagged* `λ = eig_opInv` within one `deflated_solve` call (consistent), but this `λ` is not necessarily the current outer estimate. Recorded so a caller does not assume the solve is taken at the live Newton point.
- **Idempotence / projector structure**: unlike the L2 `deflate` complementary projector `I − X(XᴴX)⁻¹Xᴴ`, `nleps_deflated_solve` is **not** a projector — it is a (block) *linear solve*, not an idempotent projection. The coupling uses the Schur-modified `SS = −S⁻¹XᴴX` and the `S⁻¹` back-projection, not the bare Gram inverse `(XᴴX)⁻¹`. The relationship to `deflate` is shared constituents (`gram`/`dot` Gram build, `lu_solve` small-dense solve, `linear_combination` back-projection, `dot` coordinate extraction), not a projector identity. Recorded to prevent over-unification (see §Variant axes).

## Dependencies

- [`ksp_solve`](./ksp_solve.md) — direct. The big-space block `x1 = T(σ)⁻¹·b1` is one preconditioned Krylov solve against the extended-problem operator bound in `K` (`opInv->Mult(b1, x1)`, `palace/linalg/nleps.cpp:514`); the `k = 0` case is exactly this solve (law 1). This is the firm constructed-operator gate `nleps_deflated_solve` extends.
- [`lu_solve`](./lu_solve.md) — direct. Three dense `k×k` solves (`Eigen::fullPivLu().solve`): `SS = −S⁻¹·(XᴴX)` (`palace/linalg/nleps.cpp:533`), `x2 = SS⁻¹·rhs` (`:534`), and `S⁻¹·x2` for the back-projection (`:535`). Firm at L1 (harvested cycle-022 wave-2); the `lu_solve.md` entry already cites these exact lines (`book/src/L1/lu_solve.md:11,:58-59`).
- [`dot`](./dot.md) — direct. The coordinate RHS `rhs(j) = b2(j) − ⟨X[j], x1⟩` (`palace/linalg/nleps.cpp:522`); the Gram entries `XᴴX(i,j) = ⟨X[i], X[j]⟩` (`:529`). Arg-1-conjugated convention pinned (`book/src/L1/dot.md:43`).
- [`axpy`](./axpy.md) — direct. The final big-space correction `x1 ← x1 − X·(S⁻¹x2)` is `linalg::AXPY(-1.0, XSx2, x1)` (`palace/linalg/nleps.cpp:536`), an `axpy` with `α = −1`.
- [`linear_combination`](../L2/linear_combination.md) — direct (the back-projection `X·(S⁻¹·x2)` is a length-`k` linear combination over the deflation basis, the `MatVecMult(X, ·)` at `palace/linalg/nleps.cpp:535` / `:329-347`). The firm **L2** `linear_combination` fold; the L1 entry references it as the named back-projection. Live link — the L2 chapter `book/src/L2/linear_combination.md` is on disk, so the upward cross-reference resolves (matching the `nleps_deflated_residual` / `ksp_solve` precedent of live-linking upward to existing L2 chapters); the high→low discipline governs how the *semantics* are defined, not whether an upward cross-reference is a live link.

The Gram `XᴴX` build is the L2 [`gram`](../L2/gram.md) combinator's positive site (`palace/linalg/nleps.cpp:524-531`, firm cycle-022); at L1 it is named as the `k×k` all-pairs `dot` fold (a `dot` dependency). `nleps_deflated_solve` is consumed by the NEP quasi-Newton loop at three sites: the projection-direction setup `deflated_solve(c, c2, w0, w2)` (`palace/linalg/nleps.cpp:542`), the Newton-step solve `deflated_solve(z, z2, du, du2)` (`:682`), and the restart projection-direction setup (`:735`). The L2 `deflate`/`gram` combinators share this operator's `Xᴴ·`/`X·`/Gram constituents (`book/src/L2/index.md:59-60`); see §Variant axes for the over-unification guard.

## Variant axes

- **deflation-present**: `k = 0` (un-deflated) | `k > 0` (deflated). The `if (k == 0) { return; }` guard (`palace/linalg/nleps.cpp:515-518`); one operator parameterized by `k`, the `k = 0` case is the plain big-space solve (law 1). Variadic-in-`k`, not a fixed-`k` family.
- **purpose (projection-direction vs Newton-step)**: the solve is invoked for the projection direction `w0` (`palace/linalg/nleps.cpp:542`, `:735`) and for the Newton step `du` (`:682`). Same operator, different `(λ, b1, b2)` and different `SetRelTol` (`w0` uses moderate accuracy, `:541`; the Newton step uses the inexact-Newton-loosened tolerance, `:681`). Not a structural variant — the tolerance is an L1>L0 concern.
- **inner-solver method**: CG / GMRES / FGMRES — absorbed into the opaque `K : Solver[…]` (inherited from [`ksp_solve`](./ksp_solve.md)'s variant-absorption).

Collapsed (absorbed) axes:

- **inexact-Newton tolerance** and **`eig_opInv` lag** — the per-use `SetRelTol` and the lagged-`σ` operator binding are L1>L0 numerical-Newton concerns; collapsed at L1 by the opaque `K` argument and the fixed-`λ` signature.
- **`Mult`/`AddMult`/`MatVecMult`/`AXPY` L0 build-forms** — the concrete `opInv->Mult` + `MatVecMult` + `linalg::AXPY` realization; collapsed at L1 into the named `ksp_solve` / `linear_combination` / `axpy` constituents.

**Do NOT over-unify with the L2 `deflate` combinator.** `deflate` is the oblique complementary *projector* `I − X(XᴴX)⁻¹Xᴴ` (bare Gram inverse `(XᴴX)⁻¹`); `nleps_deflated_solve` is the *block linear solve* of an extended NEP system whose coordinate coupling uses the Schur complement `SS = −S⁻¹·(XᴴX)`, **not** `(XᴴX)⁻¹`. The Gram `XᴴX` is built here positively (`palace/linalg/nleps.cpp:529`) but is **never solved alone** — it is always pre-multiplied by `−S⁻¹` into `SS` before inversion. They share constituents (`dot`/`gram` Gram build, `lu_solve` small-dense solve, `linear_combination` back-projection, `dot` coordinate extraction) but compute different things — a projection vs a block solve. The shared constituents are the unification surface; the operators stay distinct.

## Status

`firm` — the operator's structure is read directly from a **positive** Palace source site (the `deflated_solve` lambda, `palace/linalg/nleps.cpp:504-537`, with the source's own block-system + block-elimination comment at `:508-513`) and corroborated at its three call sites (`:542` projection-direction setup, `:682` Newton-step solve, `:735` restart projection-direction setup). Every constituent is read, not constructed: the big-space solve is `opInv->Mult` (`:514`), the coordinate RHS is a positive `linalg::Dot` loop (`:519-523`), the Gram is a positive `linalg::Dot` double-loop (`:524-531`), the Schur block `S = λI − H` (`:532`), the three `fullPivLu().solve` solves (`:533-535`), the back-projection `MatVecMult(X, ·)` (`:535`), and the final `linalg::AXPY` (`:536`). The algebraic laws are syntactic identities — the deflation reduction (law 1) is the `if (k == 0)` branch; the linearity laws (2, 4) are fixed-`(λ, K, P)` compositions of the firm `ksp_solve`/`lu_solve`/`dot`/`linear_combination` linear maps; the apply/inverse duality (law 5) is the structural relationship to the firm sibling. Every dependency (`ksp_solve`, `lu_solve`, `dot`, `axpy`, `linear_combination`) is firm vocabulary read from a positive site, so there is no constructive sub-part materialized from negative anchors, and no `partly-constructive` caveat is needed. This is the firm-on-positive-structure escape (the `apply_nonlinear_pencil` / `nleps_deflated_residual` precedent), not the `eigsolve`-convergence-semantics situation.

**Single-algorithm concentration** (noted): the operator's only L0 anchor is `QuasiNewtonSolver` (one solver). This is acceptable — it is the firm precedent of `apply_nonlinear_pencil` and `nleps_deflated_residual` (both NLEPS-only and `firm`): the laws are operator-algebra facts on fully-specified positive source, not cross-algorithm generalizations.

**Test-coverage caveat** (inherited, non-gating): NLEPS has zero dedicated unit tests (the same absence recorded for `eigsolve` / `apply_nonlinear_pencil` / `nleps_deflated_residual`). The firm decision rests on exhaustive positive structural citation, exactly as for `nleps_deflated_residual` (`book/src/L1/nleps_deflated_residual.md:117`): the laws are syntactic identities and do not depend on convergence behaviour, so the missing convergence test does not gate them. The one non-syntactic caveat — law 3's "inverts the extended operator only to the `ksp_solve` tolerance" — is recorded as a non-law, not asserted as a tight identity, so it does not require a test either.

## L1 vs L0 distinction

- **L0**: the `deflated_solve` lambda (`palace/linalg/nleps.cpp:504-537`) captures `k`, `H`, `X`, `eig_opInv`, `opInv` by reference and takes `(b1, b2, x1, x2)` with `x1`/`x2` as in-out destination buffers. It writes `opInv->Mult(b1, x1)` (`:514`), early-returns on `k == 0` (`:515-518`), resizes and fills `x2(j) = b2(j) − linalg::Dot(GetComm(), x1, X[j])` (`:519-523`), builds the Gram `SS(i,j) = linalg::Dot(GetComm(), X[i], X[j])` (`:524-531`), forms `S = eig_opInv·I − H` (`:532`), overwrites `SS = −S.fullPivLu().solve(SS)` (`:533`), solves `x2 = SS.fullPivLu().solve(x2)` (`:534`), back-projects `XSx2 = MatVecMult(X, S.fullPivLu().solve(x2))` (`:535`), and folds `linalg::AXPY(-1.0, XSx2, x1)` (`:536`). The destination buffers `x1`, `x2` are overwritten in place; the inner solve tolerance is set per-use outside the lambda (`:541`, `:681`); `eig_opInv` is the lagged eigenvalue. **The Gram `XᴴX` is materialized (`:524-531`) and then immediately overwritten into the Schur complement `−S⁻¹(XᴴX)` (`:533`) — the bare `(XᴴX)⁻¹` solve never appears; only `SS⁻¹` and `S⁻¹` are ever applied.**
- **L1**: pure-functional `{ x1, x2 } = nleps_deflated_solve(K, P, λ, b1, b2)`. No destination buffers, no per-use tolerance, no lag in the signature. One operator parameterized by the deflation-cardinality `k` (variadic). The big-space block is named as one `ksp_solve`; the coordinate RHS as `b2 − Xᴴ·x1`; the Gram as the `dot`/`gram` all-pairs fold; the Schur complement as `−lu_solve(S, XᴴX)`; the coordinate solve as `lu_solve(SS, ·)`; the back-projection as `linear_combination(X, lu_solve(S, x2))` folded by `axpy`. Linearity laws hold; `λ`-nonlinearity, the `ksp`-tolerance inexactness, and the `eig_opInv` lag are explicit non-laws.

## Evidence

- `palace/linalg/nleps.cpp:504-537` — the `deflated_solve` lambda: the complete positive site for the operator's structure. Comment `:508-513` ("Solve the block linear system | T U | | x1 | = | b1 | … x1 = T^-1 b1; x2 = SS^-1 (b2 - A x1) where SS = (B - A T^-1 U) = - X^* X S^-1; x1 = x1 - X S x2") names the block system and the Schur-elimination in the source's own words.
- `palace/linalg/nleps.cpp:505-507` — the lambda signature `[&](const ComplexVector &b1, const Eigen::VectorXcd &b2, ComplexVector &x1, Eigen::VectorXcd &x2)` — the extended `[b1, b2]` → `[x1, x2]` shape.
- `palace/linalg/nleps.cpp:514` — `opInv->Mult(b1, x1)` — the big-space block `x1 = T(σ)⁻¹·b1` (the `ksp_solve` dependency; semantics point 1, law 1).
- `palace/linalg/nleps.cpp:515-518` — `if (k == 0) { return; }` — the deflation-present guard; the un-deflated reduction to the plain big-space solve (law 1, variant axis).
- `palace/linalg/nleps.cpp:519-523` — the coordinate-RHS loop `x2(j) = b2(j) − linalg::Dot(GetComm(), x1, X[j])` (statement at `:522`) — `rhs = b2 − Xᴴ·x1`, extracted against the solved `x1` (semantics point 2, law 4; arg-1-conjugated per `book/src/L1/dot.md:43`).
- `palace/linalg/nleps.cpp:524-531` — the Gram double-loop `SS(i,j) = linalg::Dot(GetComm(), X[i], X[j])` (statement at `:529`) — the `k×k` Gram `XᴴX` (semantics point 3; the L2 `gram` positive site; the deflate-promotion finding — built positively, solved only Schur-wrapped).
- `palace/linalg/nleps.cpp:532` — `const Eigen::MatrixXcd S = eig_opInv * Eigen::MatrixXcd::Identity(k, k) - H` — the `k×k` linearization block `S = λI − H` (λ = lagged `eig_opInv`).
- `palace/linalg/nleps.cpp:533` — `SS = -S.fullPivLu().solve(SS)` — the Schur complement `SS = −S⁻¹·(XᴴX)` (the `lu_solve` over the Gram; semantics point 4). **The Gram is overwritten here — never solved alone.**
- `palace/linalg/nleps.cpp:534` — `x2 = SS.fullPivLu().solve(x2)` — the coordinate solve `x2 = SS⁻¹·(b2 − Xᴴx1)` (`lu_solve`; law 4).
- `palace/linalg/nleps.cpp:535` — `const ComplexVector XSx2 = MatVecMult(X, S.fullPivLu().solve(x2))` — the back-projection `X·(S⁻¹·x2)`: the `lu_solve` (`S.fullPivLu().solve`) composed with `linear_combination` (`MatVecMult(X, ·)`), both read from a positive site (semantics point 4).
- `palace/linalg/nleps.cpp:536` — `linalg::AXPY(-1.0, XSx2, x1)` — the final correction `x1 ← x1 − X·(S⁻¹·x2)` (the `axpy` with `α = −1`; semantics point 4).
- `palace/linalg/nleps.cpp:542` — `deflated_solve(c, c2, w0, w2)` — the projection-direction setup call (`w0 = T⁻¹c`, normalized as the eigenvalue-correction projection direction; consumer relationship).
- `palace/linalg/nleps.cpp:682` — `deflated_solve(z, z2, du, du2)` — the Newton-step solve call (`du` = the undamped Newton step the Armijo line search damps; consumer relationship).
- `palace/linalg/nleps.cpp:735` — `deflated_solve(c, c2, w0, w2)` — the restart projection-direction setup call (after a restart rebuilds the operators; consumer relationship).
- `palace/linalg/nleps.cpp:495-502` — the linear-solver operator setup: `opA = BuildParSumOperator(...)`, `opInv->SetOperators(*opA, *opP)`, `opInv->SetAbsTol(1.0e-12)` — the extended big-space operator `T(σ)` bound into `K` (the constructed-operator argument; the `ksp_solve` gate).
- `palace/linalg/nleps.cpp:474` — `eig_opInv = eig;  // eigenvalue estimate used in the (lagged) preconditioner` — the lagged-`σ` source of `λ` in `S = λI − H` (non-law: `σ = λ` no-lag does not hold).
- `palace/linalg/nleps.cpp:541` — `opInv->SetRelTol(std::max(ksp_rel_tol, inexact_tol))` — the per-use moderate-accuracy tolerance for the projection-direction solve (variant-axis purpose; collapsed at L1).
- `palace/linalg/nleps.cpp:329-347` — `MatVecMult(X, y)` — the `X·y` reconstruction (`z = 0; for j: AXPBYPCZ(...) into z`), a length-`k` `linear_combination` over the deflation basis with the complex real/imag split; the back-projection primitive at `:535`.
- `palace/linalg/nleps.cpp:334` — `const int k = X.size()` — the deflation-cardinality axis inside `MatVecMult`.
- `palace/linalg/nleps.cpp:397` — `Eigen::MatrixXcd H` — the `k×k` Rayleigh-quotient block of the invariant pair.
- `palace/linalg/nleps.cpp:401` — `std::vector<ComplexVector> X` — the deflation basis (the `k` converged eigenvectors).
- `palace/linalg/nleps.cpp:606-619` — deflation-basis growth: each converged `v` normalized (`:610-611`), `X.resize(k+1)` (`:614`), `X[k] = v` (`:615`), `H` resized/filled (`:616-618`), `k++` (`:619`) — confirms `X` is the raw normalized-eigenvector invariant-pair basis (NOT orthonormalized → the full Gram `XᴴX` in the Schur block is load-bearing; semantics point 3) and the variadic-in-`k` axis.
- `palace/linalg/nleps.cpp:354-362` — the deflation-scheme references (Effenberger 2013; Jarlebring–Koskela–Mele 2018; SLEPc-NEP minimality index 1) — the literature anchor for the extended-deflated-problem form.
- `book/src/L1/nleps_deflated_residual.md` (firm, cycle-022) — the **solve/residual sibling**: the residual *applies* the extended deflated operator where this operator *inverts* it (law 5). Its over-unification guard (`:86`, `:109`) and its `(λI−H)⁻¹`-vs-Schur-complement distinction are the basis for this entry's §Variant-axes guard.
- `book/src/L1/ksp_solve.md` (firm) — the big-space constructed-operator solve gate this operator extends (`k = 0` reduction; law 1).
- `book/src/L1/lu_solve.md` (firm, cycle-022) — the small-dense direct-solve leaf realizing the three `fullPivLu().solve` solves at `:533-535`; already cites these exact lines (`book/src/L1/lu_solve.md:11,:58-59`).
- `book/src/L1/dot.md:43` — the pinned `⟨x, y⟩ = xᴴ y` arg-1-conjugated convention (coordinate RHS and Gram entries; semantics points 2, 3).
- `book/src/L1/axpy.md` (firm) — the `α = −1` final-correction fold (`:536`).
- `book/src/L2/linear_combination.md` (firm) — the `X·(S⁻¹x2)` back-projection (the `MatVecMult(X, ·)` at `:535`).
- `book/src/L2/index.md:42,:59-60` — the cycle-022 `gram` (firm) / `deflate` (partly-constructive) L2 dep-map rows: the named oblique-projection combinator sharing this operator's `Xᴴ·`/`X·`/Gram constituents (over-unification guard; consumer relationship). The `deflate` row's "Schur-form pipeline … firm on the positive `deflated_solve` site (`nleps.cpp:505-537`)" is exactly this operator's site; its "bare-Galerkin core … constructive sub-part … promotion on a positive Galerkin deflation site" is the open promotion gate this report addresses.
- `book/src/L0/eigensolver-wrapper.md` — the L0 NLEPS reference note.
- No dedicated unit test: NLEPS has zero `test/unit/**` hits (same absence as `eigsolve` / `apply_nonlinear_pencil` / `nleps_deflated_residual`); the firm decision rests on positive structural citation, not a test.
```

```edit:book/src/L1/index.md
**Firm (16)** — element-wise updates, BLAS-1 reductions, the opaque-operator gate, the constructed-operator solve gate, the eigenmode-solve gate, the polynomial-smoother gate, the divergence-free projector gate, the nonlinear-pencil interior atom, the NEP deflated-residual extension, and the small-dense direct-solve gate:
```
→
```edit:book/src/L1/index.md
**Firm (17)** — element-wise updates, BLAS-1 reductions, the opaque-operator gate, the constructed-operator solve gate, the eigenmode-solve gate, the polynomial-smoother gate, the divergence-free projector gate, the nonlinear-pencil interior atom, the NEP deflated-residual extension, the small-dense direct-solve gate, and the NEP deflated-solve extension:
```

(Additionally, the firm-list bullet and the dep-map table row are inserted via the two anchored old→new pairs below — both anchored on the existing `lu_solve` neighbour lines so the integrator applies them as literal replacements, not insert-after-prose. The firm-list bullet is anchored on the `lu_solve` bullet's trailing blank line + the `**Rough-in (test-coverage-bounded)**` header that follows it; the dep-map row is anchored on the `lu_solve` row + the `lanczos_step` row that follows it.)

Firm-list bullet — insert immediately after the `lu_solve` bullet. The `lu_solve` bullet is a single physical line; the anchor below is its unique trailing fragment (`…not a transparent trick.`) plus the following blank line and the `**Rough-in (test-coverage-bounded)**` header. The new bullet is inserted on its own line between the `lu_solve` bullet and the blank line:

```edit:book/src/L1/index.md
ROM's QR-for-stability over rejected LDLT, `palace/models/romoperator.cpp:762-764`), not a transparent trick.

**Rough-in (test-coverage-bounded)** — operators whose structural signature is well-anchored at L0 but whose algebraic-law confidence is reduced pending dedicated test coverage or expanded literature anchoring:
```
→
```edit:book/src/L1/index.md
ROM's QR-for-stability over rejected LDLT, `palace/models/romoperator.cpp:762-764`), not a transparent trick.
- [`nleps_deflated_solve`](./nleps_deflated_solve.md) — pure-functional **deflated linear solve** of the nonlinear eigenvalue problem `{ x1, x2 } = nleps_deflated_solve(K, P, λ, b1, b2)`; the block (Schur-complement) solve of the extended deflated `(n+k)×(n+k)` system inside the quasi-Newton NEP step. The **solve** sibling of [`nleps_deflated_residual`](./nleps_deflated_residual.md) (the **residual**) — the residual *applies* the extended deflated operator, this operator *inverts* it (apply/inverse duality). Composes the firm leaves: the big-space [`ksp_solve`](./ksp_solve.md) (`opInv->Mult`), three small-dense [`lu_solve`](./lu_solve.md)s on `S = λI − H` and the Schur complement `SS = −S⁻¹(XᴴX)`, the Gram + coordinate `dot` folds, the `X·` [`linear_combination`](../L2/linear_combination.md) back-projection, and the `α=−1` [`axpy`](./axpy.md) correction. Firm on exhaustive positive structural citation of the sole literal Schur-solve lambda (`palace/linalg/nleps.cpp:504-537`); the `k = 0` case degenerates exactly to the plain big-space `ksp_solve`. The NEP deflation-extension *solve* — the third NEP-interior atom at L1. **Deflate-promotion note:** this lambda builds the Gram `XᴴX` positively (`:529`) but solves it only Schur-wrapped (`SS = −S⁻¹XᴴX`, `:533`); the bare `(XᴴX)⁻¹` Galerkin core does NOT appear positively here, so it does not promote the L2 `deflate` partly-constructive entry.

**Rough-in (test-coverage-bounded)** — operators whose structural signature is well-anchored at L0 but whose algebraic-law confidence is reduced pending dedicated test coverage or expanded literature anchoring:
```

Dep-map table row — insert immediately after the `lu_solve` dep-map row (anchored on the `lu_solve` row + the `lanczos_step` row that follows it):

```edit:book/src/L1/index.md
| [`lu_solve`](./lu_solve.md) | `(A: Matrix[k, k], b: Tensor[k]) → Tensor[k]` (single-RHS) / `(A: Matrix[k, k], B: Matrix[k, m]) → Matrix[k, m]` (multi-RHS); i.e. `A⁻¹b` | (leaf; dense materialized square matrix; sibling to `ksp_solve` on the solve-a-system axis, NOT a dependency, NOT an `apply_linop` variant) | `firm` (small-dense direct-solve gate; L0: `palace/linalg/nleps.cpp:533-535,562-563,665-667` + `palace/models/romoperator.cpp:765,757-758`; harvested cycle-022; factorization-kernel load-bearing numerical variant axis; firm-on-positive-structure, no-dedicated-solve-test caveat) |
| [`lanczos_step`](../L1-L0/minres-iteration.md) | `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` | `apply_linop`, `dot`, `axpy`, `nrm2` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-MINRES-L1-L0)` |
```
→
```edit:book/src/L1/index.md
| [`lu_solve`](./lu_solve.md) | `(A: Matrix[k, k], b: Tensor[k]) → Tensor[k]` (single-RHS) / `(A: Matrix[k, k], B: Matrix[k, m]) → Matrix[k, m]` (multi-RHS); i.e. `A⁻¹b` | (leaf; dense materialized square matrix; sibling to `ksp_solve` on the solve-a-system axis, NOT a dependency, NOT an `apply_linop` variant) | `firm` (small-dense direct-solve gate; L0: `palace/linalg/nleps.cpp:533-535,562-563,665-667` + `palace/models/romoperator.cpp:765,757-758`; harvested cycle-022; factorization-kernel load-bearing numerical variant axis; firm-on-positive-structure, no-dedicated-solve-test caveat) |
| [`nleps_deflated_solve`](./nleps_deflated_solve.md) | `(K: Solver[NonlinearPencil[N] @ σ], P: DeflationState[N, k], λ: Complex, b1: Tensor[N], b2: Vec[k]) → { x1: Tensor[N], x2: Vec[k] }` (block-eliminate the extended deflated `(n+k)` system; `x1 = T(σ)⁻¹b1`, `x2 = SS⁻¹(b2 − Xᴴx1)` with `SS = −S⁻¹XᴴX`, `S = λI − H`, then `x1 −= X·(S⁻¹x2)`) | [`ksp_solve`](./ksp_solve.md) (direct, big-space block); [`lu_solve`](./lu_solve.md) (direct, the `S`/`SS` dense `k×k` solves); [`dot`](./dot.md) (Gram + coordinate RHS), [`axpy`](./axpy.md) (final correction); [`linear_combination`](../L2/linear_combination.md) (L2, `X·` back-projection) | `firm` (NEP deflation-extension solve; L0: `palace/linalg/nleps.cpp:504-537` positive site + `:542,:682,:735` call sites; harvested cycle-023; solve sibling of `nleps_deflated_residual`; `eigsolve`-inherited no-dedicated-test caveat non-gating) |
| [`lanczos_step`](../L1-L0/minres-iteration.md) | `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` | `apply_linop`, `dot`, `axpy`, `nrm2` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-MINRES-L1-L0)` |
```

```edit:book/src/SUMMARY.md
- [lu_solve](./L1/lu_solve.md)
```
→
```edit:book/src/SUMMARY.md
- [lu_solve](./L1/lu_solve.md)
- [nleps_deflated_solve](./L1/nleps_deflated_solve.md)
```

## Operator content

(The full firm chapter body is authored inside the `new:book/src/L1/nleps_deflated_solve.md` fence above; not duplicated here. Summary of the entry's load-bearing claims:)

- **Slug + one-line**: `nleps_deflated_solve` — the deflated linear solve (block Schur-complement elimination) of the extended `(n+k)` NEP system inside `QuasiNewtonSolver`.
- **Signature**: `(K: Solver[NonlinearPencil[N] @ σ], P: DeflationState[N, k], λ: Complex, b1: Tensor[N], b2: Vec[k]) → { x1: Tensor[N], x2: Vec[k] }`, named axes `N` (big space, uniform across `K`, `P.X`, `b1`, `x1`) and variadic `k` (deflation cardinality, uniform across `P.X`, `P.H`, `b2`, `x2`); complex-only.
- **Semantics**: 5 load-bearing points — `k=0` reduces to plain `ksp_solve`; coordinate RHS `b2 − Xᴴx1` against the solved `x1`; non-orthonormal `X` ⟹ full Gram `XᴴX` in the Schur block; Schur complement `SS = −S⁻¹XᴴX` (inverse-direction vs. the residual's `(λI−H)⁻¹`); big↔small coupling non-separable.
- **Algebraic laws**: (1) `k=0` reduction to `ksp_solve`; (2) linearity in the extended RHS at fixed `(K,P,λ)`; (3) inverts the extended operator to the `ksp_solve` tolerance; (4) coordinate block = dense Schur inverse (nested `lu_solve`); (5) apply/inverse duality with `nleps_deflated_residual`. Non-laws: `λ`-nonlinearity, big-space exactness (tolerance-bounded), `σ=λ` no-lag, projector idempotence.
- **Dependencies**: `ksp_solve`, `lu_solve`, `dot`, `axpy` (L1, all firm); `linear_combination` (L2, firm).
- **Status**: `firm`.
- **Evidence**: the `deflated_solve` lambda `palace/linalg/nleps.cpp:504-537` + three call sites `:542,:682,:735` + the basis-growth/Rayleigh-block/MatVecMult/literature anchors.

## Supporting evidence

All citations machine-verified with `tools/citecheck/citecheck.py` (25 ranges in-bounds; 14 pinpoint anchors confirmed on-line). One drift caught and corrected at emit time: the coordinate-extraction statement `x2(j) = b2(j) − linalg::Dot(...)` is at **:522** (the for-loop body), not :521 (the body's opening brace); the full loop is `:519-523`. The Gram statement `SS(i,j) = linalg::Dot(...)` is at **:529**; the full double-loop is `:524-531`.

- Primary site read in full: `palace/linalg/nleps.cpp:490-545` (the lambda + its first call), `:329-347` (`MatVecMult`), `:440-480` (eig/eig_opInv setup), `:660-700` (the Newton-step call context), `:495-502` (operator setup).
- The firm leaves confirmed on disk and firm: `book/src/L1/{ksp_solve,lu_solve,dot,axpy}.md`, `book/src/L2/linear_combination.md`. The `lu_solve.md` entry already cites this exact lambda (`:11`, `:58-59`), confirming the shared positive site.
- The sibling `book/src/L1/nleps_deflated_residual.md` read in full — the apply/inverse duality (law 5) and the over-unification guard (its `:86`, `:109`) are the structural anchors for this entry's §Variant-axes guard.

## Open questions / caveats

**Deflate-promotion assessment (the dispatch's explicit question — for the integrator/meta-phase, NOT enacted here):**

The cycle-022 L2 `deflate` entry is `partly-constructive` because Palace shows the bare-Galerkin projector core `I − X(XᴴX)⁻¹Xᴴ` only in Schur-wrapped form; the promotion to firm gates on "a positive Palace Galerkin-deflation source site" (`book/src/L2/index.md:42,:60`). **This lambda does NOT supply that site.** Reasoning, read from `palace/linalg/nleps.cpp:514-536`:

- The Gram `XᴴX` **is** built positively (`:524-531`, `SS(i,j) = ⟨X[i], X[j]⟩`).
- But `XᴴX` is **never solved alone**. At `:533` it is immediately overwritten into the Schur complement `SS = −S.fullPivLu().solve(SS) = −S⁻¹·(XᴴX)`. Only `SS⁻¹` (`:534`, `x2 = SS⁻¹·rhs`) and `S⁻¹` (`:535`, `S⁻¹·x2` for the back-projection) are ever applied. The bare inverse `(XᴴX)⁻¹` (the `S = I` degenerate Galerkin core) is **absent**.
- So the `deflated_solve` lambda exhibits **only the Schur-modified form** `SS = −S⁻¹XᴴX` — which is exactly the form the cycle-022 `deflate` entry already records as its firm Schur-form pipeline (`nleps.cpp:505-537`). It adds **no new positive evidence** for the bare Galerkin core.

**Verdict: `deflate` stays `partly-constructive`.** This landing confirms (does not change) the cycle-022 verdict. The Schur-form pipeline was already firm-on-this-site; the bare-Galerkin core's promotion still gates on a positive site **elsewhere** (a Galerkin/oblique deflation that solves `(XᴴX)⁻¹` directly — none has surfaced in NLEPS, and the sibling `nleps_deflated_residual` likewise couples through `(λI−H)⁻¹`, not `(XᴴX)⁻¹`). A future search target: ROM / SLEPc-deflation / locking sites outside `nleps.cpp` that might form a bare Gram solve. I did NOT touch the `deflate` entry (out of scope).

**Other caveats:**

- **Block-comment `S` vs code `S⁻¹` at the back-projection.** The source's block-elimination comment writes `x1 = x1 - X S x2` (`:513`) but the code applies `S⁻¹` (`S.fullPivLu().solve(x2)` at `:535`). I followed the **code** (`x1 − X·S⁻¹·x2`) and flagged the comment/code mismatch in §Semantics point 4. This is a comment imprecision in Palace, not a code bug — the Schur back-substitution requires `S⁻¹` there. Recorded so a downstream reader does not transcribe the comment's `S` literally. (Drive-by observation; below the `problems/` bar — a single comment imprecision, not a methodology friction.)

- **Layer-intro refresh (for layer-intro-author, not me):** the L1 `index.md` intro motifs (lines 14-29) now have a third NEP-interior atom (`apply_nonlinear_pencil` → `nleps_deflated_residual` → `nleps_deflated_solve`); a future layer-intro pass may want to note the NEP-interior cohort as a named sub-family and the residual/solve apply-inverse duality. Not in my scope.

- **L2 `gram` consumer link.** This entry references `[`gram`](../L2/gram.md)` (firm cycle-022) as the named lift of the `XᴴX` build it does at `:524-531`. The `gram.md` chapter is on disk, so the live link resolves. If the integrator finds it absent, downgrade that one reference to plain-text `gram` (the dep-map row uses `dot` as the L1-level dependency, so no dep-map edit is needed).

- **Future L1>L0 lowering theme** (`nleps-deflated-solve-mutation-rotation`, plain-text forward-reference, not yet on disk): the in-place `x1`/`x2` destination overwrites, the `opInv->Mult` + `MatVecMult` + `linalg::AXPY` build-form, the per-use `SetRelTol` inexact-Newton tolerance, and the `eig_opInv` lag are the L1>L0 lowering content. Abstractor's domain, not mine.

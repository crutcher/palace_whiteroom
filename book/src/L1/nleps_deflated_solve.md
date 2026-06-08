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

**(3) The deflation basis `X` is NOT orthonormal — the Schur block carries the Gram `XᴴX`.** `X` stores raw normalized eigenvectors (`palace/linalg/nleps.cpp:606-619`: each converged `v` is scaled by `1/‖v‖₂` at `:610-611` and stored at `X[k] = v` at `:615`; there is no inter-column orthogonalization). Because the columns are non-orthonormal, the Schur complement carries the **full Gram matrix** `XᴴX` (built by the `dot` double-loop, `palace/linalg/nleps.cpp:524-531`, `SS(i,j) = ⟨X[i], X[j]⟩`), not a trivial identity. This is the load-bearing fact that distinguishes the oblique `deflate` projection from `orthogonalize` (the over-unification guard), and it is the Gram `XᴴX` build that the L2 [`gram`](../L2/gram.md) combinator names. The Gram is built positively here, but it is *only* solved Schur-wrapped — see §"L1 vs L0 distinction"; the bare `(XᴴX)⁻¹` solve never appears.

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
- [`lu_solve`](./lu_solve.md) — direct. Three dense `k×k` solves (`Eigen::fullPivLu().solve`): `SS = −S⁻¹·(XᴴX)` (`palace/linalg/nleps.cpp:533`), `x2 = SS⁻¹·rhs` (`:534`), and `S⁻¹·x2` for the back-projection (`:535`). Firm at L1; the `lu_solve.md` entry already cites these exact lines (`book/src/L1/lu_solve.md:11,:58-59`).
- [`dot`](./dot.md) — direct. The coordinate RHS `rhs(j) = b2(j) − ⟨X[j], x1⟩` (`palace/linalg/nleps.cpp:522`); the Gram entries `XᴴX(i,j) = ⟨X[i], X[j]⟩` (`:529`). Arg-1-conjugated convention pinned (`book/src/L1/dot.md:43`).
- [`axpy`](./axpy.md) — direct. The final big-space correction `x1 ← x1 − X·(S⁻¹x2)` is `linalg::AXPY(-1.0, XSx2, x1)` (`palace/linalg/nleps.cpp:536`), an `axpy` with `α = −1`.
- [`linear_combination`](../L2/linear_combination.md) — direct (the back-projection `X·(S⁻¹·x2)` is a length-`k` linear combination over the deflation basis, the `MatVecMult(X, ·)` at `palace/linalg/nleps.cpp:535` / `:329-347`). The firm **L2** `linear_combination` fold; the L1 entry references it as the named back-projection. Live link — the L2 chapter `book/src/L2/linear_combination.md` is on disk, so the upward cross-reference resolves (matching the `nleps_deflated_residual` / `ksp_solve` precedent of live-linking upward to existing L2 chapters); the high→low discipline governs how the *semantics* are defined, not whether an upward cross-reference is a live link.

The Gram `XᴴX` build is the L2 [`gram`](../L2/gram.md) combinator's positive site (`palace/linalg/nleps.cpp:524-531`, firm); at L1 it is named as the `k×k` all-pairs `dot` fold (a `dot` dependency). `nleps_deflated_solve` is consumed by the NEP quasi-Newton loop at three sites: the projection-direction setup `deflated_solve(c, c2, w0, w2)` (`palace/linalg/nleps.cpp:542`), the Newton-step solve `deflated_solve(z, z2, du, du2)` (`:682`), and the restart projection-direction setup (`:735`). The L2 `deflate`/`gram` combinators share this operator's `Xᴴ·`/`X·`/Gram constituents (`book/src/L2/index.md:59-60`); see §Variant axes for the over-unification guard.

## Variant axes

- **deflation-present**: `k = 0` (un-deflated) | `k > 0` (deflated). The `if (k == 0) { return; }` guard (`palace/linalg/nleps.cpp:515-518`); one operator parameterized by `k`, the `k = 0` case is the plain big-space solve (law 1). Variadic-in-`k`, not a fixed-`k` family.
- **purpose (projection-direction vs Newton-step)**: the solve is invoked for the projection direction `w0` (`palace/linalg/nleps.cpp:542`, `:735`) and for the Newton step `du` (`:682`). Same operator, different `(λ, b1, b2)` and different `SetRelTol` (`w0` uses moderate accuracy, `:541`; the Newton step uses the inexact-Newton-loosened tolerance, `:681`). Not a structural variant — the tolerance is an L1>L0 concern.
- **inner-solver method**: CG / GMRES / FGMRES — absorbed into the opaque `K : Solver[…]` (inherited from [`ksp_solve`](./ksp_solve.md)'s variant-absorption).

Collapsed (absorbed) axes:

- **inexact-Newton tolerance** and **`eig_opInv` lag** — the per-use `SetRelTol` and the lagged-`σ` operator binding are L1>L0 numerical-Newton concerns; collapsed at L1 by the opaque `K` argument and the fixed-`λ` signature.
- **`Mult`/`AddMult`/`MatVecMult`/`AXPY` L0 build-forms** — the concrete `opInv->Mult` + `MatVecMult` + `linalg::AXPY` realization; collapsed at L1 into the named `ksp_solve` / `linear_combination` / `axpy` constituents.

**Do NOT over-unify with the L2 `deflate` combinator.** `deflate` is the oblique complementary *projector* `I − X(XᴴX)⁻¹Xᴴ` (bare Gram inverse `(XᴴX)⁻¹`); `nleps_deflated_solve` is the *block linear solve* of an extended NEP system whose coordinate coupling uses the Schur complement `SS = −S⁻¹·(XᴴX)`, **not** `(XᴴX)⁻¹`. The Gram `XᴴX` is built here positively (`palace/linalg/nleps.cpp:529`) but is **never solved alone** — it is always pre-multiplied by `−S⁻¹` into `SS` before inversion. They share constituents (`dot`/`gram` Gram build, `lu_solve` small-dense solve, `linear_combination` back-projection, `dot` coordinate extraction) but compute different things — a projection vs a block solve. The shared constituents are the unification surface; the operators stay distinct.

## Status

`firm` — firm-on-positive-structure: the operator's structure is read directly from the positive `deflated_solve` lambda (`palace/linalg/nleps.cpp:504-537`, block-elimination comment `:508-513`) and its three call sites (`:542`, `:682`, `:735`); every constituent (the `opInv->Mult` big-space solve `:514`, the `linalg::Dot` coordinate RHS `:519-523`, the `linalg::Dot` Gram double-loop `:524-531`, the Schur block `S = λI − H` `:532`, the three `fullPivLu().solve` solves `:533-535`, the `MatVecMult` back-projection `:535`, the final `linalg::AXPY` `:536`) is read, not constructed, and the algebraic laws are syntactic identities over the firm `ksp_solve`/`lu_solve`/`dot`/`linear_combination` vocabulary. The only L0 anchor is `QuasiNewtonSolver` (single-algorithm concentration), the firm precedent of `apply_nonlinear_pencil` / `nleps_deflated_residual`. NLEPS has zero dedicated unit tests, but a missing convergence test does not gate syntactic-identity laws; law 3's tolerance caveat is recorded as a non-law, not a tight identity.

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
- `book/src/L1/nleps_deflated_residual.md` (firm) — the **solve/residual sibling**: the residual *applies* the extended deflated operator where this operator *inverts* it (law 5). Its over-unification guard (`:86`, `:109`) and its `(λI−H)⁻¹`-vs-Schur-complement distinction are the basis for this entry's §Variant-axes guard.
- `book/src/L1/ksp_solve.md` (firm) — the big-space constructed-operator solve gate this operator extends (`k = 0` reduction; law 1).
- `book/src/L1/lu_solve.md` (firm) — the small-dense direct-solve leaf realizing the three `fullPivLu().solve` solves at `:533-535`; already cites these exact lines (`book/src/L1/lu_solve.md:11,:58-59`).
- `book/src/L1/dot.md:43` — the pinned `⟨x, y⟩ = xᴴ y` arg-1-conjugated convention (coordinate RHS and Gram entries; semantics points 2, 3).
- `book/src/L1/axpy.md` (firm) — the `α = −1` final-correction fold (`:536`).
- `book/src/L2/linear_combination.md` (firm) — the `X·(S⁻¹x2)` back-projection (the `MatVecMult(X, ·)` at `:535`).
- `book/src/L2/index.md:42,:59-60` — the `gram` (firm) / `deflate` (partly-constructive) L2 dep-map rows: the named oblique-projection combinator sharing this operator's `Xᴴ·`/`X·`/Gram constituents (over-unification guard; consumer relationship). The `deflate` row's "Schur-form pipeline … firm on the positive `deflated_solve` site (`nleps.cpp:505-537`)" is exactly this operator's site; its "bare-Galerkin core … constructive sub-part" is the `deflate` open promotion gate.
- `book/src/L0/eigensolver-wrapper.md` — the L0 NLEPS reference note.
- No dedicated unit test: NLEPS has zero `test/unit/**` hits (same absence as `eigsolve` / `apply_nonlinear_pencil` / `nleps_deflated_residual`); the firm decision rests on positive structural citation, not a test.

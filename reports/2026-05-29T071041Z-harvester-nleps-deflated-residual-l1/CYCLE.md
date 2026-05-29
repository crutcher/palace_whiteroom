---
agent: harvester
invoked_at: 2026-05-29T071041Z
scope: L1 operator: nleps_deflated_residual
status: pending
integrated_at: 2026-05-29T1130Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-022 report 4/9 (wave-1). Applied clean — NEW firm L1 nleps_deflated_residual (the deflation extension of apply_nonlinear_pencil; thin composition over apply_nonlinear_pencil+dot+nrm2+lu_solve). In-cycle lu_solve plain-text→live-link upgrade applied. L1 firm 15→16; SUMMARY-registered. retroactive-budget 0; build clean. See reports/cycle-022-integrator-staging/STAGING.md row 4 + reports/2026-05-29T1130Z-integrator-finalize-cycle-022/CYCLE.md."
inputs:
  - palace/linalg/nleps.cpp:547-576 (compute_residual lambda — the deflated residual)
  - palace/linalg/nleps.cpp:606-619 (deflation-basis growth — X is the raw normalized-eigenvector basis)
  - palace/linalg/nleps.cpp:329-347 (MatVecMult — the X·coords back-projection)
  - book/src/L1/apply_nonlinear_pencil.md (firm; cycle-021 — the interior pencil-apply atom this composes)
  - reports/2026-05-29T051532Z-combinator-miner-deflate-gram/CYCLE.md (the deflate/gram L2 rough-in shapes)
  - book/src/L2/index.md:54-55 (deflate/gram rough-in dep-map rows — plain-text forward-refs)
  - book/src/L1/dot.md:43 (pinned ⟨x,y⟩ = xᴴ y arg-1-conjugated convention)
---

# CYCLE: Formalize nleps_deflated_residual at L1

## Summary

`nleps_deflated_residual` is the residual evaluation inside Palace's SLEPc-NEP quasi-Newton
loop **after** the already-converged eigenpairs have been deflated out — the extended-space
residual of the deflated problem of size `n + k`. It is the `compute_residual` lambda at
`palace/linalg/nleps.cpp:550-576`, whose own comment (`:547-549`) names it: "Evaluate the
deflated residual `r = T(lam) vv + T(lam) X (lam I − H)⁻¹ vv2`, with `rr2 = X* vv`." It was
NOT a rough-in before this dispatch; it is a **new** L1 operator, identified by the cycle-021
`apply_nonlinear_pencil` harvest as the deferred deflation-extension follow-up
(`book/src/L1/apply_nonlinear_pencil.md:109` records "the deflation extension `U(λ)v₂`
(560-570) is the deferred follow-up"). It is now unblocked by the cycle-021 `deflate`/`gram`
L2 shape landing (`book/src/L2/index.md:54-55`).

The operator returns the **extended residual** `(r, r₂)` — a big-space part `r : Tensor[N]`
and a redundant coordinate part `r₂ : Vec[k]` — together with its extended-space norm
`√(‖r‖² + ‖r₂‖²)`. Structurally it is a thin composition: the big-space part is **one
`apply_nonlinear_pencil` apply** of the pencil `T(λ)` to the *deflation-corrected* vector
`vv + X·(λI−H)⁻¹·vv₂` (Palace splits it into a `Mult` + `AddMult` sharing one pencil build,
which is the same apply by linearity-in-`v`), and the coordinate part is the `deflate`-half
`Xᴴ·vv` coordinate extraction. The `k = 0` (no converged eigenpairs) case degenerates exactly
to `apply_nonlinear_pencil` + `nrm2`. Status is **`firm`**: every part is read from a positive
source site, the `(λI−H)⁻¹·vv₂` back-projection's dense solve is read (not constructed) from
`fullPivLu().solve`, and all laws are syntactic identities — the `apply_nonlinear_pencil`
firm-on-positive-structure precedent applies (the `eigsolve`-inherited no-dedicated-test caveat
does not gate syntactic-identity laws).

## Proposed changes

```new:book/src/L1/nleps_deflated_residual.md
# nleps_deflated_residual

Mutation-lifted **deflated residual** of the nonlinear eigenvalue problem (NEP): evaluate the residual of the extended deflated problem of size `n + k`, where `n` is the original problem size and `k` is the number of already-converged eigenpairs deflated out. The residual computation inside Palace's quasi-Newton NEP solver (`QuasiNewtonSolver`) after the converged invariant pair `(X, H)` has been deflated — the value the Newton/Armijo line search drives to zero for the next eigenpair.

## Context

Palace's `QuasiNewtonSolver` (`palace/linalg/nleps.cpp`) computes eigenpairs of the NEP `T(λ)·x = 0` for the pencil `T(λ) = K + λC + λ²M + A2(λ)` one at a time, deflating each converged eigenpair so the next solve cannot re-converge to it. The deflation scheme is SLEPc-NEP's with minimality index 1 (Effenberger 2013 robust successive computation; Jarlebring–Koskela–Mele 2018 quasi-Newton — `palace/linalg/nleps.cpp:354-362`). It solves an **extended problem of size `n + k`**: the converged eigenpairs are stored as an invariant pair — a basis `X = [X[0], …, X[k−1]]` of `k` `ComplexVector`s of length `n` (distributed across ranks) plus a `k×k` complex matrix `H` (the Rayleigh-quotient block, stored redundantly on all ranks). An extended vector is the pair `[v, v₂]` with `v : Tensor[N]` (the big space) and `v₂ : Vec[k]` (the small redundant coordinate space) — see the solver's own block-structure comment (`palace/linalg/nleps.cpp:294-302`).

`nleps_deflated_residual` is the function that, given an eigenvalue estimate `λ` and an extended trial vector `[vv, vv₂]`, evaluates the extended residual `[r, r₂]` of the deflated problem and returns its extended-space norm. It is the convergence quantity of the NEP loop: the residual norm the quasi-Newton step and the Armijo backtracking line search drive below the tolerance (the residual is recomputed for every trial step — `palace/linalg/nleps.cpp:587` for the committed point, `palace/linalg/nleps.cpp:702` inside the backtrack loop).

This operator is the **deflation extension** of [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md): when `k = 0` (no eigenpairs yet converged) it degenerates exactly to a bare pencil apply followed by a norm. It sits in the interior of the [`eigsolve`](./eigsolve.md) gate's `direct_newton` orchestration variant — `eigsolve` treats `QuasiNewtonSolver` as one opaque orchestration; `nleps_deflated_residual` is the per-Newton-step residual atom the deflated branch of that orchestration is built from. The L0 NLEPS reference note is [`L0/eigensolver-wrapper`](../L0/eigensolver-wrapper.md).

## Signature

```text
nleps_deflated_residual
  :: (T: NonlinearPencil[N], λ: Complex, P: DeflationState[N, k], vv: Tensor[N], vv₂: Vec[k])
     -> DeflatedResidual[N, k]

type DeflatedResidual[N, k] = { r: Tensor[N], r₂: Vec[k], norm: Real }

nleps_deflated_residual(T, λ, P, vv, vv₂) =
  let S  = λ·I[k] − P.H                       -- the k×k linearization block
      c  = lu_solve(S, vv₂)                   -- (λI − H)⁻¹ · vv₂   (dense k×k solve)
      d  = vv + linear_combination(P.X, c)    -- deflation-corrected vector: vv + X·c
      r  = apply_nonlinear_pencil(T, λ, d)    -- T(λ)·(vv + X·(λI−H)⁻¹·vv₂)
      r₂ = [ dot(P.X[j], vv) | j ← 0..k−1 ]   -- Xᴴ·vv   (deflation coordinates)
  in { r, r₂, norm = √(‖r‖₂² + ‖r₂‖₂²) }
```

Shape contract (bunsen-style, named axes):

- `T` — `NonlinearPencil[N]` — the opaque operator pencil `T(λ) = K + λC + λ²M + A2(λ)`, exactly as bound for [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md). Read-only.
- `λ` — `Complex` — the eigenvalue estimate. Used both as the pencil instantiation point (polynomial terms use `λ`, `λ²`; the nonlinear closure uses `|Im λ|`) and as the scalar of the `k×k` block `S = λI − H`.
- `P` — `DeflationState[N, k]` — the converged invariant pair: `P.X : Basis[N, k]` (the `k` converged eigenvectors over the big axis `N`, the deflation basis; **not** orthonormalized — see Semantics) and `P.H : Matrix[k, k]` (the Rayleigh block, complex). Read-only. `k = 0` is the un-deflated case.
- `vv` — `Tensor[N]` — the big-space part of the extended trial vector. Read-only.
- `vv₂` — `Vec[k]` — the small redundant-coordinate part of the extended trial vector. Read-only.
- result — `DeflatedResidual[N, k]` — `r : Tensor[N]` (big-space residual), `r₂ : Vec[k]` (coordinate-space residual), `norm : Real` (the extended-space 2-norm `√(‖r‖² + ‖r₂‖²)`).

The axis `N` is uniform across `T`, `P.X`, `vv`, and `r` (an eigenproblem is square; the deflation basis lives in the same big space). The deflation-cardinality axis `k` is uniform across `P.X`, `P.H`, `vv₂`, and `r₂`; it is the **variadic-in-`k`** axis — `k` grows by one per converged eigenpair (`palace/linalg/nleps.cpp:606-619`, the `X.resize(k+1)` / `H.conservativeResizeLike` block at `:614`), so `nleps_deflated_residual` is parameterized by basis size, not a family of fixed-`k` specializations. Element type is **complex-only** (inherited from the complex-only NEP pencil and the `Eigen::VectorXcd` / `ComplexVector` carriers).

`S = λI[k] − H` is the `k×k` extended-block linearization (the small-dense linear-system operator of the deflated problem's lower-right block); `lu_solve` is the dense `k×k` factor-and-solve against it (`Eigen::fullPivLu().solve`, `palace/linalg/nleps.cpp:563`) — distinct from the iterative big-space [`ksp_solve`](./ksp_solve.md). `lu_solve` is a not-yet-firm vocabulary leaf (the dense small-system solve flagged by the cycle-021 combinator-miner; see Dependencies and Open questions); here it is referenced as a leaf since `nleps_deflated_residual`'s structure does not depend on how the `k×k` solve is realized.

## Semantics

`nleps_deflated_residual(T, λ, P, vv, vv₂)` evaluates the residual of the **extended deflated operator** applied to the extended vector `[vv, vv₂]`. The extended operator's top block-row is `[T(λ), U(λ)]` (with `U(λ) = T(λ)·X·(λI − H)⁻¹`, the deflation coupling), and its lower block-row produces the coordinate residual `r₂ = Xᴴ·vv`. Concretely:

```text
r  = T(λ)·vv  +  T(λ)·X·(λI − H)⁻¹·vv₂              -- big-space residual
r₂ = Xᴴ·vv                                          -- coordinate residual (= [⟨X[j], vv⟩]_j)
norm = √(‖r‖₂² + ‖r₂‖₂²)                            -- extended-space 2-norm
```

(`palace/linalg/nleps.cpp:547-549` is the source's own statement of `r` and `r₂`; the big-space part is built at `:559` + `:564`, the coordinate part at `:565-570`, the norm at `:575`.) The L1 form is pure-functional: the same `(T, λ, P, vv, vv₂)` yields the same `DeflatedResidual`. The L0 source overwrites destination buffers `rr` / `rr₂` and carries the built `A2` operator back to the caller for reuse across a line search; those destination bindings and the `A2`-caching are L1>L0 lowering concerns, not L1 signature.

Five semantic points are load-bearing and recorded rather than smoothed:

**(1) The big-space residual is a single `apply_nonlinear_pencil` of the deflation-corrected vector.** Palace splits the big-space part into two operator applies sharing **one** pencil build: `A->Mult(vv, rr)` gives `T(λ)·vv` (`palace/linalg/nleps.cpp:559`) and `A->AddMult(XSvv2, rr, 1.0)` adds `T(λ)·(X·(λI−H)⁻¹·vv₂)` (`:564`), where `XSvv2 = MatVecMult(X, S.fullPivLu().solve(vv2))` (`:563`) is the back-projection and both applies use the *same* `A = BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM, A2_out}, true)` (`:557`). By the linearity-in-`v` of `apply_nonlinear_pencil` (its law 1), `T(λ)·vv + T(λ)·d = T(λ)·(vv + d)` — so the big-space residual is `apply_nonlinear_pencil(T, λ, vv + X·(λI−H)⁻¹·vv₂)`. The split into `Mult` + `AddMult` (avoiding a fresh `vv + d` temporary) is a transparent performance trick at L1; the value is the single pencil apply of the corrected vector.

**(2) The deflation basis `X` is NOT orthonormal — the back-projection needs the `(λI−H)⁻¹` solve.** `X` stores raw normalized eigenvectors (`palace/linalg/nleps.cpp:606-619`: each converged `v` is scaled by `1/‖v‖₂` at `:610-611` and stored at `X[k] = v` (`:615`); there is no inter-column orthogonalization). This is why the coupling carries `(λI − H)⁻¹` — the small-dense linearization-block solve — rather than a trivial transpose. This is the same non-orthonormal-basis fact that distinguishes the L2 `deflate` combinator from `orthogonalize` (the cycle-021 combinator-miner over-unification guard).

**(3) The coordinate residual uses `Xᴴ·vv` — the basis vector is the conjugated argument.** `r₂(j) = ⟨X[j], vv⟩ = X[j]ᴴ vv` (`palace/linalg/nleps.cpp:568`, `linalg::Dot(GetComm(), vv, X[j])`). Note the two framings name the *same* conjugated operand: under the C++ free-function order `linalg::Dot(comm, x, y) = yᴴ x` the **second** C++ argument is conjugated (here `X[j]`, the C++ arg-2), and that operand is the **first** argument of the L1 [`dot`](./dot.md) convention `⟨x, y⟩ = xᴴ y` (`book/src/L1/dot.md:43`, which conjugates its arg-1). Both descriptions — "C++ arg-2-conjugating" and "L1 arg-1-conjugated" — refer to the same conjugated operand `X[j]`, the **basis vector**. This is the `coords`/`Xᴴ·` half of the `deflate` projection (the back-projection `X·(λI−H)⁻¹·vv₂` from point (1) is its `X·` half). Pinning the conjugation once here is exactly the simplification the cycle-021 `deflate`/`gram` L2 combinator buys the NEP vocabulary.

**(4) The norm is the extended-space 2-norm, not the big-space norm.** `norm = √(‖r‖₂² + ‖r₂‖₂²)` (`palace/linalg/nleps.cpp:575`, `std::sqrt(std::abs(linalg::Dot(GetComm(), rr, rr)) + rr2.squaredNorm())`) — the big-space part is the distributed [`nrm2`](./nrm2.md)², the coordinate part is the local `Eigen` `squaredNorm()`, summed under the root. The extended residual lives in `ℂ^{n+k}`; its norm is the convergence quantity, so the coordinate-space contribution is part of the residual, not a separate diagnostic.

**(5) The `k = 0` case is exactly `apply_nonlinear_pencil` + `nrm2`.** When no eigenpairs have converged (`palace/linalg/nleps.cpp:560` `if (k > 0)` false, `:571-574` `else { rr2.resize(0); }`), the deflation terms vanish: `r = T(λ)·vv`, `r₂ = []`, `norm = ‖T(λ)·vv‖₂`. This is the un-deflated NEP residual `nrm2(apply_nonlinear_pencil(T, λ, vv))` — `nleps_deflated_residual` strictly extends `apply_nonlinear_pencil` with the deflation coupling.

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Deflation-extension reduction (`k = 0`)**: `nleps_deflated_residual(T, λ, ⟨X=[], H=[]⟩, vv, []) = { r = apply_nonlinear_pencil(T, λ, vv), r₂ = [], norm = nrm2(apply_nonlinear_pencil(T, λ, vv)) }`. The empty-deflation case is the bare pencil residual. Witnessed by the `if (k > 0)` guard (`palace/linalg/nleps.cpp:560`) and the `else { rr2.resize(0); }` branch (`:571-574`). This is the bridge law to [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md): the deflated residual is its deflation extension.

2. **Big-space residual is a pencil-apply of the corrected vector**: `r = apply_nonlinear_pencil(T, λ, vv + linear_combination(X, lu_solve(λI−H, vv₂)))`. Holds by the linearity-in-`v` of `apply_nonlinear_pencil` (its law 1) applied to the `Mult` + `AddMult` split (`palace/linalg/nleps.cpp:559, :563-564`). This factors the entire big-space residual through the single firm interior atom — the L2 decomposition unfolds `nleps_deflated_residual` into one `apply_nonlinear_pencil`, one `lu_solve`, one `linear_combination`, and `k` `dot`s.

3. **Coordinate residual is sesquilinear in `vv`**: `r₂ = Xᴴ·vv` is conjugate-linear in `X` and linear in `vv`; `r₂(α·u + β·w) = α·(Xᴴu) + β·(Xᴴw)` for scalars `α, β`. Each entry is a [`dot`](./dot.md) (arg-1 = basis vector, conjugated). Special case: `r₂ = 0` when `vv ⊥ span(X)` under `⟨·,·⟩`.

4. **Big-space residual linearity in the extended input** (at fixed `λ`, `P`): `r` is linear in the extended pair `(vv, vv₂)` — `r(α·(u,u₂) + β·(w,w₂)) = α·r(u,u₂) + β·r(w,w₂)`. Holds because at fixed `λ` the whole big-space map `(vv, vv₂) ↦ T(λ)·(vv + X·(λI−H)⁻¹·vv₂)` is a composition of linear maps (`lu_solve` against the fixed `S`, `linear_combination` against the fixed `X`, the fixed linear operator `T(λ)`). The pair `(r, r₂)` is therefore the action of the fixed extended linear operator `[[T(λ), T(λ)X(λI−H)⁻¹], [Xᴴ, 0]]` on `[vv, vv₂]` — `nleps_deflated_residual` IS the extended-operator apply at fixed `(λ, P)`.

5. **Eigenpair annihilation**: if `(λ, [vv, vv₂])` is an exact eigenpair of the extended deflated problem then `r = 0`, `r₂ = 0`, and `norm = 0`. This is the defining convergence target: `norm` is what the quasi-Newton/Armijo loop drives below tolerance (`palace/linalg/nleps.cpp:587` committed-point call, `:702` backtrack-trial call). Special case of law 4 / the residual definition.

Laws that explicitly **do not** hold:

- **Linearity / polynomiality in `λ`**: `nleps_deflated_residual(T, ·, P, vv, vv₂)` is **not** linear or polynomial in `λ`. The pencil `T(λ)` carries the nonlinear `A2` closure (inherited non-law from [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md)), and the block `S = λI − H` and its inverse `(λI − H)⁻¹` make the deflation coupling a non-polynomial (rational-with-nonlinear-`A2`) function of `λ`. Recorded so the eigenvalue-correction step does not assume polynomial structure across `λ`.
- **Bit-determinism of the big-space accumulation**: the `Mult` + `AddMult` two-step accumulation (`palace/linalg/nleps.cpp:559, :564`) and the algebraically-equal single apply of `vv + X·(λI−H)⁻¹·vv₂` may differ at the bit level (different accumulation order; matrix-free `A2` inherits reduction-tree non-associativity from `apply_linop`). Law 2's identity is mathematical; its floating-point realization is exact modulo accumulation-order noise. Load-bearing per the CLAUDE.md trick taxonomy.
- **Idempotence / projector structure on `vv`**: unlike the L2 `deflate` complementary projector `I − X(XᴴX)⁻¹Xᴴ`, `nleps_deflated_residual` is **not** a projector — it does not subtract the projection from `vv`; it computes a *residual* of an extended operator (the coupling uses the Schur-modified `(λI − H)⁻¹` block, not the Gram inverse `(XᴴX)⁻¹`). The relationship to `deflate` is shared constituents (`dot` coordinate extraction + `linear_combination` back-projection + a small-dense solve), not a projector identity. Recorded to prevent over-unification with the L2 `deflate` combinator (see Variant axes).

## Dependencies

- [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md) — direct. The big-space residual is exactly one pencil apply of the deflation-corrected vector (law 2); the `k = 0` case is a bare pencil apply (law 1). This is the firm interior atom `nleps_deflated_residual` extends.
- [`dot`](./dot.md) — direct. The `k` coordinate-residual entries `r₂(j) = ⟨X[j], vv⟩` (`palace/linalg/nleps.cpp:568`); the big-space norm-squared `‖r‖₂² = ⟨r, r⟩` (`:575`). Arg-1-conjugated convention pinned.
- [`nrm2`](./nrm2.md) — direct (via the extended norm; the big-space part is `nrm2(r)²` and the `k = 0` norm is `nrm2(apply_nonlinear_pencil(T, λ, vv))`).
- [`linear_combination`](../L2/linear_combination.md) — direct (the back-projection `X·(λI−H)⁻¹·vv₂` is a length-`k` linear combination over the deflation basis, the `MatVecMult(X, ·)` at `palace/linalg/nleps.cpp:563` / `:329-347`). This is the firm **L2** `linear_combination` fold; the L1 entry references it as the named back-projection. Live link — the L2 chapter `book/src/L2/linear_combination.md` is on disk, so the upward cross-reference resolves (matching the precedent of `ksp_solve`/`chebyshev-smoother` live-linking upward to existing L2 chapters); the high→low discipline governs how the *semantics* are defined, not whether an upward cross-reference is a live link. The L1>L0 lowering will narrate the `MatVecMult` realization.
- `lu_solve` — direct, **not-yet-firm vocabulary**. The dense `k×k` solve `(λI − H)⁻¹·vv₂` (`Eigen::fullPivLu().solve`, `palace/linalg/nleps.cpp:563`). This is the candidate small-dense factor-and-solve leaf flagged by the cycle-021 combinator-miner (OQ `deflate-needs-small-dense-lu-solve-primitive`); distinct from the iterative big-space [`ksp_solve`](./ksp_solve.md). Referenced plain-text as a leaf — `nleps_deflated_residual`'s structure does not depend on how the `k×k` solve is realized, so the missing `lu_solve` entry does not gate this operator's firmness (it gates only the precision of the dependency's name). See Open questions.

`nleps_deflated_residual` is consumed by the deflated quasi-Newton step (the next fan-out-ordered NLEPS piece, `nleps_deflated_solve` — plain-text forward-reference, not yet on disk) and by the L2 `deflate`/`gram` combinator's NEP use-site (the coordinate extraction + back-projection it shares — `book/src/L2/index.md:54-55`, rough-in). The L2 `deflate` combinator is the **named oblique-projection composition**; `nleps_deflated_residual` is the L1 *residual* that uses the same `Xᴴ·`/`X·` constituents but with the Schur-modified `(λI − H)⁻¹` coupling, not the Gram inverse — they are related-but-distinct (see the §Algebraic-laws non-law and §Variant-axes).

## Variant axes

- **deflation-present**: `k = 0` (un-deflated) | `k > 0` (deflated). The `if (k > 0)` guard (`palace/linalg/nleps.cpp:560`); one operator parameterized by `k`, the `k = 0` case is the bare pencil residual (law 1). Variadic-in-`k`, not a fixed-`k` family.
- **damping-present**: `with-C` | `without-C` — inherited from the bound pencil `T` (the `T.C : Maybe LinearOperator` axis of [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md)). Absorbed by the pencil argument.
- **purpose (committed vs trial)**: the residual is recomputed for the committed Newton point (`palace/linalg/nleps.cpp:587`) and for every Armijo backtrack trial (`:702`). Same operator, different `(λ, vv, vv₂)`; not a structural variant.

Collapsed (absorbed) axes:

- **A2-representation** and **L0-build-form** — inherited from [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md) (the opaque `A2` closure; the `BuildParSumOperator` + `Mult`/`AddMult` build form). Collapsed at L1 by that operator's laws.
- **`Mult` + `AddMult` split vs single corrected-vector apply** — the two algebraically-identical big-space accumulation shapes (law 2); collapsed at L1, the choice is an L1>L0 transparent-performance concern.

**Do NOT over-unify with the L2 `deflate` combinator.** `deflate` is the oblique complementary *projector* `I − X(XᴴX)⁻¹Xᴴ` (Gram inverse); `nleps_deflated_residual` is the *residual* of an extended NEP operator whose coupling uses the Schur-modified `(λI − H)⁻¹` block, not `(XᴴX)⁻¹`. They share constituents (`dot` coordinate extraction, `linear_combination` back-projection, a small-dense solve) but compute different things — a projection vs an operator residual. The shared constituents are the unification surface; the operators stay distinct.

## Status

`firm` — the operator's structure is read directly from a **positive** Palace source site (the `compute_residual` lambda, `palace/linalg/nleps.cpp:550-576`, with the source's own naming comment at `:547-549`) and corroborated at its two call sites (`:587` committed point, `:702` backtrack trial). Every constituent is read, not constructed: the big-space residual is two `Mult`/`AddMult` calls on a `BuildParSumOperator` pencil (`:557-564`), the back-projection is a positive `MatVecMult(X, S.fullPivLu().solve(vv2))` (`:563`), the coordinate residual is a positive `linalg::Dot` loop (`:565-570`), the norm is a positive `std::sqrt(...)` (`:575`). The algebraic laws are syntactic identities — the deflation-extension reduction (law 1) is the `if (k > 0)` branch, the pencil-apply factoring (law 2) is the linearity-in-`v` of the firm `apply_nonlinear_pencil`, the linearity laws are fixed-`(λ, P)` linear-operator facts. The `lu_solve` dependency is not-yet-firm vocabulary but is **read from a positive site** (`fullPivLu().solve`) — so there is no constructive sub-part materialized from negative anchors, and no `partly-constructive` caveat is needed; the missing `lu_solve` *entry* gates the precision of a dependency name, not the operator's structure or laws.

**Single-algorithm concentration** (noted): the operator's only L0 anchor is `QuasiNewtonSolver` (one solver). This is acceptable — it is the firm precedent of `apply_nonlinear_pencil` (which is also NLEPS-only and `firm`): the laws are operator-algebra facts on fully-specified positive source, not cross-algorithm generalizations.

**Test-coverage caveat** (inherited, non-gating): NLEPS has zero dedicated unit tests (`search_text` for `QuasiNewton|nleps|funcA2|GetResidualNorm` over `test/unit/**` returns zero hits — same absence as `eigsolve` / `apply_nonlinear_pencil`). The firm decision rests on exhaustive positive structural citation, exactly as for `apply_nonlinear_pencil` (`book/src/L1/apply_nonlinear_pencil.md:98`): the laws are syntactic identities and do not depend on convergence behaviour, so the missing convergence test does not gate them. This is the firm-on-positive-structure escape, not the `eigsolve`-convergence-semantics situation. Should a future NEP-orchestration test surface a contract issue in the deflated residual, this can be revisited — but the residual's laws are operator-algebra facts, not iteration facts.

## L1 vs L0 distinction

- **L0**: the `compute_residual` lambda (`palace/linalg/nleps.cpp:550-576`) captures `k`, `H`, `X` by reference and takes `(lam, vv, vv2, rr, rr2, A2_out)`. It builds `A = BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM, A2_out.get()}, true)` (`:557-558`), writes `A->Mult(vv, rr)` (`:559`), and — when `k > 0` — forms `S = lam·I − H` (`:562`), `XSvv2 = MatVecMult(X, S.fullPivLu().solve(vv2))` (`:563`), accumulates `A->AddMult(XSvv2, rr, 1.0)` (`:564`), resizes and fills `rr2(j) = linalg::Dot(GetComm(), vv, X[j])` (`:565-570`), else `rr2.resize(0)` (`:571-574`); it returns the scalar `std::sqrt(std::abs(linalg::Dot(GetComm(), rr, rr)) + rr2.squaredNorm())` (`:575`). The destination buffers `rr`, `rr2` are overwritten; `A2_out` is carried back for line-search reuse; the built pencil is duplicated logic from the in-`Solve` setup.
- **L1**: pure-functional `{ r, r₂, norm } = nleps_deflated_residual(T, λ, P, vv, vv₂)`. No destination buffers, no `A2`-caching, no build-form choice in the signature. One operator parameterized by the deflation-cardinality `k` (variadic) and the `Maybe C` damping axis (via the pencil). The big-space residual is named as a single `apply_nonlinear_pencil` of the deflation-corrected vector; the coordinate residual as `Xᴴ·vv`; the norm as the extended-space 2-norm. Linearity laws hold; `λ`-nonlinearity and the two-build-form bit-difference are explicit non-laws.

## Evidence

- `palace/linalg/nleps.cpp:547-576` — the `compute_residual` lambda: the deflated-residual definition. Comment `:547-549` ("Evaluate the deflated residual `r = T(lam) vv + T(lam) X (lam I − H)⁻¹ vv2`, with `rr2 = X* vv`") names `r` and `r₂` in the source's own words. Lambda signature at `:550-555`. The complete positive site for the operator's structure.
- `palace/linalg/nleps.cpp:556` — `A2_out = (*funcA2)(std::abs(lam.imag()))` — the nonlinear closure evaluated at `|Im λ|` (inherited pencil semantics) and carried back for line-search reuse.
- `palace/linalg/nleps.cpp:557` — `BuildParSumOperator({1.0+0.0i, lam, lam*lam, 1.0+0.0i}, {opK, opC, opM, A2_out.get()}, true)` — the `{1, λ, λ², 1}` pencil build; the same shape as `apply_nonlinear_pencil`.
- `palace/linalg/nleps.cpp:559` — `A->Mult(vv, rr)` — the big-space `T(λ)·vv` term (semantics point 1, law 2).
- `palace/linalg/nleps.cpp:560` — `if (k > 0)` — the deflation-present guard (variant axis; law 1 reduction).
- `palace/linalg/nleps.cpp:562` — `const Eigen::MatrixXcd S = lam * Eigen::MatrixXcd::Identity(k, k) - H` — the `k×k` linearization block `S = λI − H`.
- `palace/linalg/nleps.cpp:563` — `const ComplexVector XSvv2 = MatVecMult(X, S.fullPivLu().solve(vv2))` — the back-projection `X·(λI−H)⁻¹·vv₂`: the `lu_solve` (dense `fullPivLu().solve`) composed with `linear_combination` (`MatVecMult(X, ·)`). The single non-yet-firm dependency (`lu_solve`), read from a positive site.
- `palace/linalg/nleps.cpp:564` — `A->AddMult(XSvv2, rr, 1.0)` — accumulates `T(λ)·(X·(λI−H)⁻¹·vv₂)`; with `:559` realizes the single pencil apply of the corrected vector (law 2).
- `palace/linalg/nleps.cpp:565` — `rr2.conservativeResize(k)` — the coordinate-residual sizing.
- `palace/linalg/nleps.cpp:568` — `rr2(j) = linalg::Dot(GetComm(), vv, X[j])` (in the `for (int j = 0; j < k; j++)` at `:566-569`) — the coordinate residual `r₂(j) = X[j]ᴴ vv` (semantics point 3, law 3; arg-1-conjugated per `book/src/L1/dot.md:43`).
- `palace/linalg/nleps.cpp:571-574` — `else { rr2.resize(0); }` — the `k = 0` empty-coordinate branch (law 1).
- `palace/linalg/nleps.cpp:575` — `return std::sqrt(std::abs(linalg::Dot(GetComm(), rr, rr)) + rr2.squaredNorm())` — the extended-space 2-norm `√(‖r‖² + ‖r₂‖²)` (semantics point 4).
- `palace/linalg/nleps.cpp:587` — `double res = compute_residual(eig, v, v2, u, u2, A2n)` — the committed-point residual call (the convergence quantity; law 5).
- `palace/linalg/nleps.cpp:702` — `const double res_trial = compute_residual(eig_trial, v_trial, v2_trial, u, u2, A2n)` — the Armijo-backtrack trial residual call (the line-search convergence quantity; law 5).
- `palace/linalg/nleps.cpp:329-347` — `MatVecMult(X, y)` — the `X·y` reconstruction (`z = 0; for j: AXPBYPCZ(...) into z`), a length-`k` `linear_combination` over the deflation basis with the complex real/imag split; the back-projection primitive at `:563`.
- `palace/linalg/nleps.cpp:606-619` — deflation-basis growth: each converged `v` normalized (`:610-611`), `X.resize(k+1)` (`:614`), `X[k] = v` (`:615`), `H.conservativeResizeLike(...)` / `H.col(k).head(k) = v2/scale` / `H(k,k) = eig` (`:616-618`), `k++` (`:619`) — confirms `X` is the raw normalized-eigenvector invariant-pair basis (NOT orthonormalized → the `(λI−H)⁻¹` coupling is load-bearing; semantics point 2) and the variadic-in-`k` axis.
- `palace/linalg/nleps.cpp:354-362` — the deflation-scheme references (Effenberger 2013; Jarlebring–Koskela–Mele 2018; SLEPc-NEP minimality index 1) — the literature anchor for the extended-deflated-problem form.
- `book/src/L1/apply_nonlinear_pencil.md` (firm, cycle-021) — the interior pencil-apply atom this operator extends; its `:109` records the deflation extension (lines 560-570) as the deferred follow-up this dispatch closes; its linearity-in-`v` law 1 is the basis for law 2 here; its firm-on-positive-structure status (`:98`) is the precedent for this entry's firm decision.
- `book/src/L1/dot.md:43` — the pinned `⟨x, y⟩ = xᴴ y` arg-1-conjugated convention (coordinate residual; semantics point 3).
- `book/src/L2/index.md:54-55` — the rough-in `gram` / `deflate` L2 dep-map rows: the named oblique-projection combinator sharing this operator's `Xᴴ·`/`X·` constituents (over-unification guard; consumer relationship). Plain-text forward-reference — those chapter files are not yet on disk.
- `book/src/L0/eigensolver-wrapper.md` — the L0 NLEPS reference note.
- No dedicated unit test: `search_text` for `QuasiNewton|nleps|funcA2|GetResidualNorm` over `test/unit/**` returns zero hits — the test-coverage caveat inherited from `eigsolve` / `apply_nonlinear_pencil`; the firm decision rests on positive structural citation, not a test.
```

```edit:book/src/SUMMARY.md
[add chapter entry under the L1 Part, after the apply_nonlinear_pencil entry (`:70`)]
- [nleps_deflated_residual](./L1/nleps_deflated_residual.md)
```

```edit:book/src/L1/index.md
[add a row to the "## Operator dep-map" table after the `apply_nonlinear_pencil` row, and a bullet to the "Firm" cohort list after the `apply_nonlinear_pencil` bullet]

-- dep-map row (after the apply_nonlinear_pencil row) --
| [`nleps_deflated_residual`](./nleps_deflated_residual.md) | `(T: NonlinearPencil[N], λ: Complex, P: DeflationState[N, k], vv: Tensor[N], vv₂: Vec[k]) → { r: Tensor[N], r₂: Vec[k], norm: Real }` (deflated NEP residual `r = T(λ)·(vv + X·(λI−H)⁻¹·vv₂)`, `r₂ = Xᴴ·vv`) | `apply_nonlinear_pencil` (direct, big-space residual); `dot` (coordinate residual, big-space norm), `nrm2` (extended norm); [`linear_combination`](../L2/linear_combination.md) (L2, back-projection `X·(λI−H)⁻¹·vv₂`), `lu_solve` (not-yet-firm, the dense `k×k` `(λI−H)⁻¹` solve) | `firm` (NEP deflation-extension residual; L0: `palace/linalg/nleps.cpp:550-576` positive site + `:587,:702` call sites; harvested cycle-022; deflation extension of `apply_nonlinear_pencil`; `eigsolve`-inherited no-dedicated-test caveat non-gating) |

-- Firm-cohort bullet (after the apply_nonlinear_pencil bullet) --
- [`nleps_deflated_residual`](./nleps_deflated_residual.md) — pure-functional **deflated residual** of the nonlinear eigenvalue problem `{ r, r₂, norm } = nleps_deflated_residual(T, λ, P, vv, vv₂)`; the residual of the extended deflated problem of size `n + k` after the converged invariant pair `(X, H)` has been deflated out. The **deflation extension** of [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md): the big-space residual is one pencil apply of the deflation-corrected vector `vv + X·(λI−H)⁻¹·vv₂` (Palace's `Mult` + `AddMult` split = the single apply by linearity-in-`v`), the coordinate residual is the `Xᴴ·vv` extraction, and the `k = 0` case degenerates exactly to `apply_nonlinear_pencil` + `nrm2`. Firm on exhaustive positive structural citation (every constituent read, including the `lu_solve` from `fullPivLu().solve`); the NLEPS no-dedicated-test caveat is non-gating (syntactic-identity laws). The second NEP-interior atom at L1, and the convergence quantity the quasi-Newton/Armijo loop drives to zero.

-- "Firm (13)" heading count bump → "Firm (14)" --
```

The "Firm (13)" heading in `book/src/L1/index.md` should become "Firm (14)" (integrator: the count appears in the `## Vocabulary cohort` section heading "**Firm (13)** — element-wise updates, …" — append "the nonlinear-pencil interior atom**, and the NEP deflated-residual extension**" or similar to the prose tail; the exact prose extension is the integrator's call, but the count must increment).

## Operator content

The full firm chapter body is authored inside the `new:book/src/L1/nleps_deflated_residual.md` fence above. Sections: one-line + Context + Signature (bunsen-style named-axes shape contract, `DeflatedResidual[N,k]` record, `DeflationState[N,k]`) + Semantics (5 load-bearing points) + Algebraic laws (5 holding, 3 explicit non-laws) + Dependencies + Variant axes (with the do-NOT-over-unify-with-L2-`deflate` guard) + Status (`firm`, single-algorithm + test-coverage caveats both non-gating) + L1-vs-L0 + Evidence. Defined in L1 vocabulary throughout (composes the firm L1 `apply_nonlinear_pencil` + `dot` + `nrm2`, live-links upward to the firm L2 `linear_combination` (on disk), and references the not-yet-firm `lu_solve` plain-text; never defines its semantics in L0 primitives — that is the future L1>L0 theme).

## Supporting evidence

All `path:lo-hi` citations in the entry were self-verified this invocation via `read_range`
and `tools/citecheck/citecheck.py` (regex anchors for the pinpoint lines). Verification results:

- All 12 pinpoint NLEPS citations confirmed at their exact lines: `:547`, `:550`, `:556`,
  `:557`, `:559`, `:560`, `:562`, `:563`, `:564`, `:565`, `:568`, `:575`, plus `:329`
  (`MatVecMult`), `:587` and `:702` (call sites). The `compute_residual` body range
  `:547-576` and the deflation-growth range `:606-619` are in bounds.
- The deflation-basis-growth `X.resize(k + 1)` is at `:614` (within the cited `:606-619`
  block); the prose cites the block range and names `:614` for the resize specifically.
- In-book cross-references confirmed: `book/src/L1/apply_nonlinear_pencil.md:109` (the
  deferred-follow-up note this dispatch closes), `book/src/L1/dot.md:43` (conjugation
  convention), `book/src/L2/index.md:54-55` (the `gram`/`deflate` rough-in rows),
  `book/src/L0/eigensolver-wrapper.md` (exists, 127 lines).
- The cycle-021 `deflate`/`gram` L2 rows ARE on disk as rough-in (`book/src/L2/index.md:54-55`);
  their chapter files `book/src/L2/{deflate,gram}.md` are NOT on disk — so this entry references
  `deflate`/`gram` / `lu_solve` as **plain-text / inline-code**, never live links, to avoid a
  `linkcheck2` build break (per the `rough-in-forward-reference-must-be-plain-text-not-live-link`
  convention). **`linear_combination` is the exception:** its L2 chapter
  `book/src/L2/linear_combination.md` IS on disk (firm), so the upward reference to it is a
  **live link** (`../L2/linear_combination.md`), matching the `ksp_solve`/`chebyshev-smoother`
  precedent of L1 entries live-linking upward to existing L2 chapters — it is NOT one of the
  missing forward-refs. The live links in the entry (`apply_nonlinear_pencil.md`, `dot.md`,
  `nrm2.md`, `ksp_solve.md`, `eigsolve.md`, `apply_linop.md` via `nrm2`,
  `../L2/linear_combination.md`, `../L0/eigensolver-wrapper.md`) all resolve to existing files.

## Open questions / caveats

- **Dependency `lu_solve` is not-yet-firm vocabulary (does NOT gate this operator).** The dense
  `k×k` `(λI−H)⁻¹` solve (`fullPivLu().solve`, `palace/linalg/nleps.cpp:563`) is the
  small-dense factor-and-solve leaf flagged by the cycle-021 combinator-miner (OQ
  `deflate-needs-small-dense-lu-solve-primitive`). `nleps_deflated_residual` is firm without it
  because the `lu_solve` is read from a positive site and the operator's structure/laws do not
  depend on the solve's realization — but the dependency cell names `lu_solve` plain-text until
  that leaf lands. When `lu_solve` is harvested, the dep-map cell and the Dependencies section
  should switch it to a live link (a mechanical follow-up touch, not a re-harvest).

- **L1>L0 lowering theme is not authored here (abstractor's domain).** The mutation rotation
  that takes `nleps_deflated_residual`'s pure form down to the `compute_residual` lambda
  (destination buffers `rr`/`rr2`, the `A2_out` line-search caching, the `Mult`+`AddMult`
  split, the `MatVecMult` realization of `linear_combination`) is a future `L1-L0` theme —
  likely an extension of the existing NLEPS lowering (the cycle-008 `ksp-solve-mutation-rotation`
  / the `apply_nonlinear_pencil` L1>L0 lowering, both deferred). Noted for the abstractor; not
  in scope for this harvest.

- **Layer-intro refresh (note for layer-intro-author, not enacted):** the L1 `index.md`
  `## Vocabulary cohort` heading "**Firm (13)**" must increment to "**Firm (14)**" and its
  prose tail ("…the nonlinear-pencil interior atom") should mention the deflated-residual
  extension. The proposed-changes block above flags the count bump; the precise prose extension
  is the integrator's / layer-intro-author's call.

- **Next fan-out-ordered NLEPS pieces (for the plan):** with `nleps_deflated_residual` firm,
  the deferred chain continues `nleps_deflated_solve` (the `deflated_solve` lambda
  `:504-537` — the extended-system linear solve, which IS the L2 `deflate` Schur-modified
  oblique projection in action) → `nleps_jacobian_action` (the `:653-668` directional
  derivative with the `XSv2`/`XSSv2` deflation terms) → `nleps_eigenvalue_correction` (the
  `:675` Newton-ratio scalar step). `nleps_deflated_solve` is the natural next harvest — it is
  the consumer of this residual and the positive site for the L2 `deflate`/`gram` firming.

- **Single-algorithm concentration is fine (noted, not a caveat that blocks firm).** All anchors
  are in `QuasiNewtonSolver` (`nleps.cpp`). Per the dispatch directive and the
  `apply_nonlinear_pencil` precedent, NLEPS-only concentration does not gate firmness — the laws
  are operator-algebra facts on positive source.

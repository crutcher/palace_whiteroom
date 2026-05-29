---
agent: harvester
invoked_at: 2026-05-29T105500Z
scope: L1 operator: nleps_jacobian_action
status: pending
integrated_at: 2026-05-29T140000Z
integration_commit: f3be056
integration_notes: "Applied cycle-024 (staging row 1). Firm L1 operator nleps_jacobian_action landed; L1 firm 17→18. New chapter book/src/L1/nleps_jacobian_action.md + L1/index.md (Firm count + cohort bullet + dep-map) + SUMMARY.md. No gate hits."
inputs:
  - book/src/L1/apply_nonlinear_pencil.md (firm sibling — Jacobian recorded as deferred follow-up at its law 5 / :111)
  - book/src/L1/nleps_deflated_residual.md (firm sibling — the residual whose extended-operator apply this differentiates)
  - book/src/L1/nleps_deflated_solve.md (firm sibling — the deflated solve; shares S = λI − H, Xᴴ·, X· constituents)
  - palace/linalg/nleps.cpp:649-669 (the positive Jacobian-action site, verified via read_range)
  - palace/linalg/nleps.cpp:412 (delta = √ε finite-difference step), :177-181 (funcA2 closure), :329-347 (MatVecMult), :673-675 (consumer)
  - OQ nleps-interior-atoms-remaining-jacobian-action-and-eigenvalue-correction (scaffolding/open-questions.md:779)
---

# CYCLE: Formalize nleps_jacobian_action at L1

## Summary

Formalizes **`nleps_jacobian_action`** at L1 — the third deferred NEP-interior atom of Palace's `QuasiNewtonSolver` (the fourth firm NEP-interior L1 operator overall, after `apply_nonlinear_pencil`, `nleps_deflated_residual`, `nleps_deflated_solve`). It is the quasi-Newton Jacobian-vector action `w = J(λ)·v`: it applies the **derivative pencil** `T'(λ) = C + 2λM + A2'(λ)` (a finite-difference divided-difference `A2'`) to the trial vector, and — when eigenpairs have been deflated (`k > 0`) — adds the analytic derivative `U'(λ)·v₂` of the deflation coupling `U(λ) = T(λ)·X·(λI−H)⁻¹` that `nleps_deflated_residual` carries. The operator was already named-as-deferred in `apply_nonlinear_pencil`'s law 5 ("Jacobian as derivative-pencil apply"); this dispatch firms it as its own L1 entry, distinguishing the **big-space-only** output from the residual's extended `(r, r₂)` pair, and pinning the load-bearing facts (the finite-difference `A2'`, the `|Im λ|·(1+δ)` evaluation point, the `S⁻¹`-vs-`S` comment/code convention shared with `nleps_deflated_solve`, the product-rule structure of `U'(λ)`). Status: **`firm`** — the structure is read from a single positive site (`palace/linalg/nleps.cpp:649-670`), every constituent is read not constructed, and the laws are syntactic operator-algebra identities (the firm-on-positive-structure escape established by `apply_nonlinear_pencil` / `nleps_deflated_residual` / `nleps_deflated_solve`). The finite-difference `A2'` is the one non-syntactic semantic point and is recorded as a load-bearing approximation (an explicit non-law on the divided-difference accuracy), not as an unconfirmed law — so it does not gate firm.

## Proposed changes

```edit:book/src/L1/nleps_jacobian_action.md
[new file — full firm chapter body below in §Operator content]
```

```edit:book/src/L1/index.md
[(1) bump the Firm count 17→18 and extend the cohort one-liner; (2) add one Vocabulary-cohort bullet after the nleps_deflated_solve bullet (line 49); (3) add one dep-map row after the nleps_deflated_solve row (line 87). NON-OVERLAPPING with the parallel nleps_eigenvalue_correction harvester: that harvester appends ITS cohort bullet + dep-map row AFTER this entry's, and the two harvesters bump the Firm count additively (17→18 here; the integrator reconciles to 17→19 if both land). See §Index edits for exact anchored text.]
```

```edit:book/src/SUMMARY.md
[insert `- [nleps_jacobian_action](./L1/nleps_jacobian_action.md)` after line 78 (`- [nleps_deflated_solve](./L1/nleps_deflated_solve.md)`), under the L1 Part. NON-OVERLAPPING: the parallel nleps_eigenvalue_correction harvester inserts its line after this one.]
```

## Operator content

The full firm chapter body, as written into `book/src/L1/nleps_jacobian_action.md`:

```new:book/src/L1/nleps_jacobian_action.md
# nleps_jacobian_action

Mutation-lifted **quasi-Newton Jacobian action** of the nonlinear eigenvalue problem (NEP): given an eigenvalue estimate `λ` and an extended trial vector `[v, v₂]`, apply the Jacobian `J(λ)` of the extended deflated residual operator and return the big-space result `w = J(λ)·v` (plus, when `k > 0`, the deflation-coupling derivative). The `w = J·v` computation inside Palace's quasi-Newton NEP step (`QuasiNewtonSolver`) — the operator whose output `w` is the Jacobian direction the undamped Newton eigenvalue/eigenvector step is built from.

## Context

Palace's `QuasiNewtonSolver` (`palace/linalg/nleps.cpp`) computes eigenpairs of the NEP `T(λ)·x = 0` for the pencil `T(λ) = K + λC + λ²M + A2(λ)` one at a time, deflating each converged eigenpair (`palace/linalg/nleps.cpp:354-362`, SLEPc-NEP / Effenberger 2013 / Jarlebring–Koskela–Mele 2018). Each quasi-Newton iteration needs the **Jacobian** of the (deflated) residual operator with respect to the iterate, applied to the current direction `v` — the linearization the Newton step is taken against. The source's own comment marks the site: `// Compute w = J * v.` (`palace/linalg/nleps.cpp:649`).

`nleps_jacobian_action` is the function that, given the eigenvalue estimate `λ` and the extended trial vector `[v, v₂]`, produces `w = J(λ)·v`. The big-space part applies the **derivative pencil** `T'(λ) = ∂_λ T(λ) = C + 2λM + A2'(λ)`; the deflation part (active only when `k > 0`) adds `U'(λ)·v₂`, the `λ`-derivative of the deflation coupling `U(λ) = T(λ)·X·(λI−H)⁻¹` carried by [`nleps_deflated_residual`](./nleps_deflated_residual.md). It is the **derivative sibling** of `nleps_deflated_residual`: the residual *applies* the extended deflated operator at `λ`; this operator applies that operator's *`λ`-derivative*. It is to the NEP Newton loop what the matrix `J` is to any Newton iteration — the linearization that, paired with the residual, produces the step. It sits in the interior of the [`eigsolve`](./eigsolve.md) gate's `direct_newton` orchestration variant — `eigsolve` treats `QuasiNewtonSolver` as one opaque orchestration; `nleps_jacobian_action` is the per-Newton-step Jacobian atom that orchestration is built from. The L0 NLEPS reference note is [`L0/eigensolver-wrapper`](../L0/eigensolver-wrapper.md).

## Signature

```text
nleps_jacobian_action
  :: (T: NonlinearPencil[N], λ: Complex, P: DeflationState[N, k], v: Tensor[N], v₂: Vec[k])
     -> Tensor[N]

nleps_jacobian_action(T, λ, P, v, v₂) =
  let T'        = derivative_pencil(T, λ)             -- coeffs {0, 1, 2λ, 1}; closure A2'(λ)
      w₀        = apply_nonlinear_pencil(T', λ, v)     -- T'(λ)·v   (big-space derivative pencil apply)
  in if k == 0 then w₀                                -- no deflation: bare derivative-pencil apply
     else
       let S    = λ·I[k] − P.H                         -- the k×k linearization block
           a    = lu_solve(S, v₂)                      -- S⁻¹·v₂
           b    = lu_solve(S, a)                       -- S⁻²·v₂
           cpl  = apply_nonlinear_pencil(T', λ, linear_combination(P.X, a))   -- + T'(λ)·X·S⁻¹·v₂
                − apply_nonlinear_pencil(T,  λ, linear_combination(P.X, b))   -- − T(λ)·X·S⁻²·v₂
       in w₀ + cpl
```

where the **derivative pencil** `T'` is the NonlinearPencil with the same `K`, `C`, `M`, the polynomial coefficient vector `{0, 1, 2λ, 1}` (so `K` drops, `C` keeps weight `1`, `M` gets weight `2λ`), and the nonlinear closure replaced by the divided-difference derivative `A2'(λ) ≈ (A2((1+δ)|Im λ|) − A2(|Im λ|)) / (i·δ·|Im λ|)` with `δ = √ε` machine-epsilon (`palace/linalg/nleps.cpp:412`, `:650-654`). Shape contract (bunsen-style, named axes):

- `T` — `NonlinearPencil[N]` — the opaque operator pencil `T(λ) = K + λC + λ²M + A2(λ)`, exactly as bound for [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md). Read-only. (The Jacobian uses `T` directly only in the `k > 0` deflation-coupling term `−T(λ)·X·S⁻²·v₂`; the derivative pencil `T'` is formed from `T`'s bound operators.)
- `λ` — `Complex` — the eigenvalue estimate. Used as the derivative-pencil instantiation point (polynomial coefficients `{0, 1, 2λ, 1}`; the divided-difference `A2'` is evaluated at the frequency `|Im λ|` and the bumped `|Im λ|·(1+δ)`) and as the scalar of the `k×k` block `S = λI − H`.
- `P` — `DeflationState[N, k]` — the converged invariant pair: `P.X : Basis[N, k]` (the `k` converged eigenvectors over the big axis `N`, the deflation basis; **not** orthonormalized) and `P.H : Matrix[k, k]` (the Rayleigh block, complex). Read-only. `k = 0` is the un-deflated case.
- `v` — `Tensor[N]` — the big-space part of the extended trial direction. Read-only.
- `v₂` — `Vec[k]` — the small redundant-coordinate part of the extended trial direction. Read-only. (Enters only through the `k > 0` deflation-coupling term.)
- result — `Tensor[N]` — the big-space Jacobian direction `w = J(λ)·v`. **Big-space only** (axis `N`); see Semantics point 1.

The axis `N` is uniform across `T`, `P.X`, `v`, and `w` (the eigenproblem is square; the deflation basis lives in the same big space). The deflation-cardinality axis `k` is uniform across `P.X`, `P.H`, and `v₂`; it is **variadic-in-`k`** — `k` grows by one per converged eigenpair (`palace/linalg/nleps.cpp:606-619`), so `nleps_jacobian_action` is parameterized by basis size, not a fixed-`k` family. Element type is **complex-only** (inherited from the complex NEP pencil and the `Eigen::VectorXcd` / `ComplexVector` carriers).

`S = λI[k] − H` is the `k×k` extended-block linearization (the same block as the residual / solve siblings); [`lu_solve`](./lu_solve.md) is the dense `k×k` factor-and-solve against it (`Eigen::fullPivLu().solve`, `palace/linalg/nleps.cpp:664,:666`), distinct from the iterative big-space [`ksp_solve`](./ksp_solve.md). The deflation coupling uses `S` solved **twice in sequence** (`S⁻¹` then `S⁻²`), the differentiated counterpart of the residual's single `S⁻¹` solve (Semantics point 2).

## Semantics

`nleps_jacobian_action(T, λ, P, v, v₂)` applies the Jacobian of the extended deflated residual operator. The big-space part is the **derivative pencil** applied to `v`; the deflation part is the `λ`-derivative of the residual's deflation coupling. Concretely (the source's own comment, `palace/linalg/nleps.cpp:659-660`):

```text
w = T'(λ)·v  +  U'(λ)·v₂                                            -- (the k > 0 form)
  = T'(λ)·v  +  T'(λ)·X·S⁻¹·v₂  −  T(λ)·X·S⁻²·v₂      where S = λI − H
```

(The source comment writes `T'(l) v1 + T'(l)XS v2 − T(l)XS^2 v2` with `S` where the *code* applies `S⁻¹` / `S⁻²` via `.fullPivLu().solve` — the same `S`-means-`S⁻¹` comment/code convention `nleps_deflated_solve` documents at its semantics point 4; the realized arithmetic is `S⁻¹`/`S⁻²`.) Execution order (`palace/linalg/nleps.cpp:649-669`):

```text
opA2p = A2((1+δ)·|Im λ|)                                  -- :650   bumped frequency
denom = i·δ·|Im λ|                                        -- :651-652
A2'   = (opA2p − A2(|Im λ|)) / denom                      -- :653-654   divided-difference derivative
opJ   = {0, 1, 2λ, 1}·{K, C, M, A2'}                      -- :655-656   the derivative pencil T'(λ)
w     = opJ·v                                             -- :657   T'(λ)·v   (big-space)
if k == 0: return w                                       -- :658 guard false → skip deflation
  A   = {1, λ, λ², 1}·{K, C, M, A2(|Im λ|)} = T(λ)        -- :661-662   (scoped here, see point 4)
  S   = λI − H                                            -- :663
  Sv2 = S⁻¹·v₂                                            -- :664
  XSv2  = X·(S⁻¹·v₂)                                      -- :665   linear_combination
  XSSv2 = X·(S⁻¹·(S⁻¹·v₂)) = X·S⁻²·v₂                     -- :666   linear_combination
  w += opJ·XSv2  = T'(λ)·X·S⁻¹·v₂                         -- :668   AddMult(+1)
  w −= A·XSSv2   = T(λ)·X·S⁻²·v₂                          -- :669   AddMult(−1)
```

The L1 form is pure-functional: the same `(T, λ, P, v, v₂)` yields the same `w`. The L0 source overwrites the destination buffer `w` (`ComplexVector w` declared at `palace/linalg/nleps.cpp:378`) in place and reuses the line-search-cached `A2n` operator; those destination bindings and the `A2`-caching are L1>L0 lowering concerns, not L1 signature.

Five semantic points are load-bearing and recorded rather than smoothed:

**(1) The Jacobian action output is big-space-only — there is no coordinate companion.** Unlike the sibling [`nleps_deflated_residual`](./nleps_deflated_residual.md) (which returns an extended pair `(r, r₂)` plus a norm) and [`nleps_deflated_solve`](./nleps_deflated_solve.md) (which returns an extended pair `(x1, x2)`), the Jacobian action writes only the big-space vector `w` (`palace/linalg/nleps.cpp:657,:668-669`); there is no `w₂` coordinate part computed at this site. The `w0`/`w2` that appear nearby are the *output of the deflated solve* (`deflated_solve(c, c2, w0, w2)`, `:542`) — the projection direction — **not** a coordinate part of `J·v`. The downstream Newton eigenvalue update consumes `w` only through the big-space dot `⟨w, w0⟩` (`palace/linalg/nleps.cpp:675`), confirming `w` is treated as a pure big-space vector. This asymmetry — residual/solve are extended-space, the Jacobian action is big-space-only — is part of the operator's contract and is pinned in the signature (`-> Tensor[N]`, not `-> { w: Tensor[N], w₂: Vec[k] }`).

**(2) The deflation coupling derivative is the product-rule derivative of `U(λ) = T(λ)·X·(λI−H)⁻¹`.** The residual's deflation coupling is `U(λ)·v₂ = T(λ)·X·S⁻¹·v₂` (`nleps_deflated_residual` semantics point 1). Its `λ`-derivative by the product rule is `U'(λ)·v₂ = T'(λ)·X·S⁻¹·v₂ + T(λ)·X·(∂_λ S⁻¹)·v₂`, and since `S = λI − H` gives `∂_λ S⁻¹ = −S⁻¹·(∂_λ S)·S⁻¹ = −S⁻²`, the second term is `−T(λ)·X·S⁻²·v₂`. This is exactly the source's `+ T'(l)XS v2 − T(l)XS^2 v2` (`palace/linalg/nleps.cpp:660`), realized as the two `AddMult` accumulations `opJ->AddMult(XSv2, w, 1.0)` (`:668`, `+T'(λ)·X·S⁻¹·v₂`) and `A->AddMult(XSSv2, w, -1.0)` (`:669`, `−T(λ)·X·S⁻²·v₂`). The double `S⁻¹` solve (`Sv2 = S⁻¹v₂` at `:664`, then `S⁻¹·Sv2` at `:666`) materializes `S⁻²·v₂` as two sequential dense solves rather than forming `S⁻²` explicitly — the differentiated counterpart of the residual's single `S⁻¹` solve.

**(3) `A2'(λ)` is a finite-difference divided-difference approximation, not the analytic derivative.** The nonlinear closure `A2` is a black box (`palace/linalg/nleps.cpp:177-181`), so its `λ`-derivative is approximated by a one-sided divided difference at frequency `|Im λ|`: `A2'(λ) ≈ (A2((1+δ)|Im λ|) − A2(|Im λ|)) / (i·δ·|Im λ|)` with `δ = √ε` (`palace/linalg/nleps.cpp:412`, the comment "Delta used in to compute divided difference Jacobian" at `:411`). The `i` in the denominator (`denom = std::complex<double>(0.0, delta * std::abs(eig.imag()))`, `:651-652`) reflects that the frequency `|Im λ|` is the imaginary part of `λ`, so a bump in frequency is a bump of `i·δ·|Im λ|` in `λ`. This is a **load-bearing numerical** point per the CLAUDE.md trick taxonomy: the divided-difference accuracy (`O(δ)` truncation, balanced against `O(ε/δ)` roundoff at `δ = √ε`) is part of the *quasi*-Newton algorithm — it is why the solver is quasi-Newton (an approximate Jacobian) rather than exact Newton. Recorded as an explicit non-law (the Jacobian is not the exact `∂_λ T`), not smoothed into an analytic-derivative claim.

**(4) The full pencil `T(λ)` is re-formed (re-scoped) inside the `k > 0` branch.** The `−T(λ)·X·S⁻²·v₂` term needs the *value* pencil `T(λ)` (coefficients `{1, λ, λ², 1}`), distinct from the derivative pencil `opJ` (`{0, 1, 2λ, 1}`). The source rebuilds it locally as `A = BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM, A2n.get()}, true)` (`palace/linalg/nleps.cpp:661-662`) using the line-search-cached `A2n` (the `A2(|Im λ|)` operator carried across iterations). The source comment at `:659-660` explains the local scoping ("Scoping T(l) here lets the line search overwrite A2n freely; with no deflation we skip it"). This is the same `apply_nonlinear_pencil` value-pencil build (its law 3 / `:557` shape) reused — at L1 it is one `apply_nonlinear_pencil(T, λ, ·)` call, the rebuild being an L1>L0 transparent-performance / scoping concern.

**(5) The deflation basis `X` is NOT orthonormal — the coupling carries `S⁻¹` / `S⁻²`, not a transpose.** `X` stores raw normalized eigenvectors (`palace/linalg/nleps.cpp:606-619`: each converged `v` scaled by `1/‖v‖₂` at `:610-611`, stored at `X[k] = v` at `:615`; no inter-column orthogonalization). This is the same non-orthonormal-basis fact that makes the residual/solve siblings carry `(λI−H)⁻¹` / the Gram `XᴴX`; here it makes the Jacobian coupling carry `S⁻¹` (in the `T'` term) and `S⁻²` (in the `T` term). This is the load-bearing fact distinguishing the oblique deflation coupling from an orthonormal-basis projection (the cycle-021/022 over-unification guard).

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Deflation reduction (`k = 0`)**: `nleps_jacobian_action(T, ⟨X=[], H=[]⟩, λ, v, []) = apply_nonlinear_pencil(T', λ, v)` where `T'` is the derivative pencil (`{0, 1, 2λ, 1}`, `A2'`). The empty-deflation case is the bare derivative-pencil apply. Witnessed by the `if (k > 0)` guard (`palace/linalg/nleps.cpp:658`) skipping the deflation block. This is the bridge law to [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md): the Jacobian action is its derivative-pencil apply (the realization of `apply_nonlinear_pencil`'s law 5, "Jacobian as derivative-pencil apply", now firmed as its own operator) plus the deflation coupling.

2. **Linearity in the extended direction `(v, v₂)`** (at fixed `T`, `λ`, `P`): the map `(v, v₂) ↦ w` is **linear** — `jac(α·(u,u₂) + β·(p,p₂)) = α·jac(u,u₂) + β·jac(p,p₂)` for scalars `α, β`. Holds because at fixed `(λ, T, P)` every step is a linear map of its input: `apply_nonlinear_pencil(T', λ, ·)` is the fixed linear operator `T'(λ)` (by `apply_nonlinear_pencil` law 1, linearity-in-`v`), `lu_solve(S, ·)` is the fixed linear `S⁻¹` (firm [`lu_solve`](./lu_solve.md) law 2), `linear_combination(X, ·)` is linear, and the value-pencil apply `apply_nonlinear_pencil(T, λ, ·)` is linear. The composite is the action of the fixed Jacobian operator `J(λ) = [T'(λ) | T'(λ)XS⁻¹ − T(λ)XS⁻²]` on `[v, v₂]`. In particular `jac(0, 0) = 0`. This is the defining property — `J(λ)` is a *linear operator* for fixed `λ`, even though it depends nonlinearly on `λ` (the Jacobian of a nonlinear map is linear at a point).

3. **Big-space derivative-pencil decomposition**: `w₀ = apply_nonlinear_pencil(T', λ, v) = apply_linop(C, v)·1 + apply_linop(M, v)·2λ + apply_linop(A2'(λ), v)` (the `{0, 1, 2λ, 1}` coefficient vector drops `K`). Holds by `apply_nonlinear_pencil`'s term-decomposition law 3 applied to the derivative pencil. Witnessed by `opJ = BuildParSumOperator({0, 1, 2λ, 1}, {opK, opC, opM, opAJ}, true)` then `opJ->Mult(v, w)` (`palace/linalg/nleps.cpp:655-657`). This factors the big-space Jacobian through the firm interior atom — the L2 decomposition unfolds it into `apply_linop` calls over `C`, `M`, `A2'` plus a coefficient-weighted accumulation.

4. **Deflation-coupling product rule**: `w = w₀ + U'(λ)·v₂` with `U'(λ)·v₂ = apply_nonlinear_pencil(T', λ, X·S⁻¹v₂) − apply_nonlinear_pencil(T, λ, X·S⁻²v₂)` and `S = λI − H`. Holds by the product-rule / `∂_λ S⁻¹ = −S⁻²` derivation (Semantics point 2); each term is `apply_nonlinear_pencil` of a `linear_combination(X, lu_solve(S, ·))` back-projection. Witnessed by the two `AddMult` accumulations (`palace/linalg/nleps.cpp:668-669`) over `XSv2 = X·S⁻¹v₂` (`:665`) and `XSSv2 = X·S⁻²v₂` (`:666`). This factors the entire deflation coupling through firm vocabulary (`apply_nonlinear_pencil`, `lu_solve`, `linear_combination`).

5. **Derivative-of-residual relationship**: `nleps_jacobian_action(T, λ, P, ·, ·)` is the `λ`-derivative of the (extended deflated) operator that [`nleps_deflated_residual`](./nleps_deflated_residual.md) applies — the big-space row of `∂_λ [[T(λ), U(λ)], [Xᴴ, 0]]` is `[T'(λ), U'(λ)]`, exactly the `[opJ | opJ·XS⁻¹ − A·XS⁻²]` realized here. Recorded as the structural relationship (the Jacobian/residual pair of any Newton iteration), not a literal pointwise-difference identity (the `A2'` is a finite-difference approximation, so the realized Jacobian is the quasi-Newton approximate derivative, not the exact analytic derivative — see the non-law).

Laws that explicitly **do not** hold:

- **`A2'` is the exact analytic derivative**: the realized `A2'(λ) = (A2((1+δ)|Im λ|) − A2(|Im λ|)) / (i·δ·|Im λ|)` is a one-sided divided-difference approximation (`palace/linalg/nleps.cpp:650-654`, `δ = √ε`), **not** the exact `∂_λ A2`. The resulting `J` is the *quasi*-Newton approximate Jacobian; this is the load-bearing numerical feature (Semantics point 3), recorded so a caller does not assume an exact derivative. Truncation `O(δ)` traded against roundoff `O(ε/δ)` at `δ = √ε` is part of the algorithm.
- **Linearity / polynomiality in `λ`**: `nleps_jacobian_action(T, ·, P, v, v₂)` is **not** linear or polynomial in `λ`. The derivative pencil's `A2'(λ)` carries the nonlinear `A2` closure's variation, and the block `S = λI − H` with its inverses `S⁻¹`, `S⁻²` makes the deflation coupling a non-polynomial function of `λ`. Recorded so the eigenvalue-correction step does not assume polynomial structure across `λ`. (The polynomial part `C + 2λM` *is* affine in `λ`; the `A2'` and `S⁻ⁿ` parts are not.)
- **Bit-determinism of the big-space accumulation**: the three-step `opJ->Mult` + `opJ->AddMult` + `A->AddMult` accumulation (`palace/linalg/nleps.cpp:657,:668,:669`) and an algebraically-equal single combined apply may differ at the bit level (different accumulation order; matrix-free `A2'` / `A2` inherit reduction-tree non-associativity from `apply_linop`). The law-2/3/4 identities are mathematical; their floating-point realization is exact modulo accumulation-order noise. Load-bearing per the CLAUDE.md trick taxonomy.
- **Coordinate output**: `nleps_jacobian_action` does **not** produce a coordinate-space companion `w₂` (Semantics point 1). A caller must not read a `(w, w₂)` pair from this operator — the extended-space structure of the residual/solve siblings is absent here; `J·v` is big-space only.

## Dependencies

- [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md) — direct. The big-space Jacobian is the derivative-pencil apply `apply_nonlinear_pencil(T', λ, v)` (law 1, 3); the deflation coupling's two terms are `apply_nonlinear_pencil(T', λ, ·)` and `apply_nonlinear_pencil(T, λ, ·)` of back-projected vectors (law 4). This is the firm interior atom this operator differentiates — the realization of `apply_nonlinear_pencil`'s deferred law-5 "Jacobian as derivative-pencil apply".
- [`lu_solve`](./lu_solve.md) — direct. The dense `k×k` solves `S⁻¹·v₂` (`palace/linalg/nleps.cpp:664`) and `S⁻¹·(S⁻¹·v₂) = S⁻²·v₂` (`:666`), both `Eigen::fullPivLu().solve`. The small-dense factor-and-solve leaf (firm cycle-022); distinct from the iterative big-space [`ksp_solve`](./ksp_solve.md). The double sequential solve (rather than forming `S⁻²`) is the differentiated counterpart of the residual's single `S⁻¹` solve.
- [`linear_combination`](../L2/linear_combination.md) — direct (the back-projections `X·S⁻¹v₂` and `X·S⁻²v₂` are length-`k` linear combinations over the deflation basis, the `MatVecMult(X, ·)` at `palace/linalg/nleps.cpp:665,:666` / `:329-347`). The firm **L2** `linear_combination` fold; the L1 entry references it as the named back-projection. Live link — the L2 chapter `book/src/L2/linear_combination.md` is on disk, so the upward cross-reference resolves (matching the `nleps_deflated_residual` / `nleps_deflated_solve` / `ksp_solve` precedent of live-linking upward to existing L2 chapters); the high→low discipline governs how the *semantics* are defined, not whether an upward cross-reference is a live link.
- [`apply_linop`](./apply_linop.md) — transitive (via `apply_nonlinear_pencil`'s term decomposition: each derivative-pencil term `C·v`, `2λ·M·v`, `A2'·v` is an `apply_linop` — law 3).

The nonlinear closure `A2 : Real -> LinearOperator[N, N]` and its divided-difference derivative `A2'` are **opaque leaves** at L1 — the finite-difference construction (`palace/linalg/nleps.cpp:650-654`) is the one numerical detail the L1 form pins as a non-law (Semantics point 3); how `A2` is internally assembled is below the L1 resolution. `nleps_jacobian_action` is consumed by the NEP quasi-Newton eigenvalue/eigenvector step: `w = J·v` feeds the undamped Newton eigenvalue correction `delta_eig = −(⟨u, w0⟩ + u2ᴴw2) / ⟨w, w0⟩` (`palace/linalg/nleps.cpp:673-675`) and the step direction `z = −delta_eig·w − u` (`:676`). The eigenvalue-correction step — the sibling cycle-024 NLEPS-interior atom — is the direct consumer.

## Variant axes

- **deflation-present**: `k = 0` (un-deflated) | `k > 0` (deflated). The `if (k > 0)` guard (`palace/linalg/nleps.cpp:658`); one operator parameterized by `k`, the `k = 0` case is the bare derivative-pencil apply (law 1). Variadic-in-`k`, not a fixed-`k` family.
- **damping-present**: `with-C` | `without-C` — inherited from the bound pencil `T` (the `T.C : Maybe LinearOperator` axis of [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md)). When `T.C = Nothing`, the derivative pencil's weight-`1` `C` term drops; the `2λM` and `A2'` terms remain. Absorbed by the pencil argument.

Collapsed (absorbed) axes:

- **A2-representation** — inherited from [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md) (the opaque `A2` closure; whether assembled or `NewtonInterpolationOperator`-interpolated). The divided-difference `A2'` is built from `A2` evaluations regardless of `A2`'s representation. Collapsed at L1.
- **finite-difference step `δ` and the `A2n` line-search cache** — the `δ = √ε` divided-difference step (`palace/linalg/nleps.cpp:412`) is a *load-bearing numerical* contract (recorded as a non-law, Semantics point 3) but a fixed solver-level constant, not a structural variant; the `A2n` operator caching (`:661-662` re-scoping) is an L1>L0 transparent-performance / scoping concern. Collapsed at L1.
- **L0-build-form (`Mult` + two `AddMult` vs single combined apply)** — the three algebraically-identical accumulation steps (`palace/linalg/nleps.cpp:657,:668,:669`); collapsed at L1 by laws 3-4, the choice is an L1>L0 transparent-performance concern.

**Do NOT over-unify with the residual / solve siblings.** `nleps_deflated_residual` *applies* the extended deflated operator (returns `(r, r₂, norm)`); `nleps_deflated_solve` *inverts* it (returns `(x1, x2)`); `nleps_jacobian_action` applies its `λ`-**derivative** and returns a **big-space-only** `w` (no coordinate companion). They share constituents (the block `S = λI − H`, the `X·` back-projection, `apply_nonlinear_pencil`, `lu_solve`, `linear_combination`) but compute different things — apply vs inverse vs derivative-apply. The Jacobian's defining distinctions: the derivative pencil `T'` (coefficients `{0, 1, 2λ, 1}`, divided-difference `A2'`), the *double* `S⁻¹` solve (for `S⁻²` in the product-rule term), and the big-space-only output. The shared constituents are the unification surface; the operators stay distinct.

## Status

`firm` — the operator's structure is read directly from a single **positive** Palace source site (the `w = J·v` block, `palace/linalg/nleps.cpp:649-669`, opened by the source's own comment `// Compute w = J * v.` at `:649` and the deflation-coupling comment `w1 = T'(l) v1 + U'(l) v2 = T'(l) v1 + T'(l)XS v2 − T(l)XS^2 v2` at `:659-660`). Every constituent is read, not constructed: the divided-difference `A2'` is the positive `BuildParSumOperator({1/denom, −1/denom}, {opA2p, A2n})` (`:653-654`), the derivative pencil is `BuildParSumOperator({0, 1, 2λ, 1}, {opK, opC, opM, opAJ})` (`:655-656`), the big-space apply is `opJ->Mult(v, w)` (`:657`), the block `S = λI − H` (`:663`), the two dense solves `S.fullPivLu().solve` (`:664,:666`), the back-projections `MatVecMult(X, ·)` (`:665,:666`), and the two `AddMult` accumulations (`:668,:669`). The algebraic laws are syntactic identities — the deflation reduction (law 1) is the `if (k > 0)` branch, the linearity laws (2-3) are fixed-`(λ, T, P)` compositions of the firm `apply_nonlinear_pencil` / `lu_solve` / `linear_combination` linear maps, the product-rule coupling (law 4) is the read `∂_λ S⁻¹ = −S⁻²` structure, the derivative-of-residual relationship (law 5) is the structural relationship to the firm sibling. Every dependency (`apply_nonlinear_pencil`, `lu_solve`, `linear_combination`, `apply_linop`) is firm vocabulary read from a positive site, so there is no constructive sub-part materialized from negative anchors, and no `partly-constructive` caveat is needed. This is the firm-on-positive-structure escape (the `apply_nonlinear_pencil` / `nleps_deflated_residual` / `nleps_deflated_solve` precedent), not the `eigsolve`-convergence-semantics situation.

**The one non-syntactic point — the divided-difference `A2'`** (Semantics point 3, the quasi-Newton approximate Jacobian) — is recorded as an explicit **non-law** (the realized Jacobian is *not* the exact analytic derivative), not asserted as a tight identity, so it does not require a test to firm. The `δ = √ε` accuracy trade-off is a load-bearing numerical contract documented as such; the *structure* of the Jacobian (which terms, which coefficients, the product-rule coupling) is fully positive.

**Single-algorithm concentration** (noted): the operator's only L0 anchor is `QuasiNewtonSolver` (one solver). This is acceptable — it is the firm precedent of `apply_nonlinear_pencil` / `nleps_deflated_residual` / `nleps_deflated_solve` (all NLEPS-only and `firm`): the laws are operator-algebra facts on fully-specified positive source, not cross-algorithm generalizations.

**Test-coverage caveat** (inherited, non-gating): NLEPS has zero dedicated unit tests (`search_text` for `QuasiNewton|nleps|funcA2|GetResidualNorm` over `test/unit/**` returns zero hits — the same absence recorded for `eigsolve` / `apply_nonlinear_pencil` / `nleps_deflated_residual` / `nleps_deflated_solve`). The firm decision rests on exhaustive positive structural citation, exactly as for the siblings (`book/src/L1/nleps_deflated_solve.md:145`): the laws are syntactic identities and do not depend on convergence behaviour, so the missing convergence test does not gate them. The one non-syntactic caveat — the divided-difference `A2'` accuracy — is recorded as a non-law, not asserted as a tight identity, so it does not require a test either.

## L1 vs L0 distinction

- **L0**: the `w = J·v` block inside the quasi-Newton `while (it < nleps_it)` loop (`palace/linalg/nleps.cpp:649-669`) captures `funcA2`, `delta`, `eig`, `A2n`, `opK`/`opC`/`opM`, `k`, `H`, `X` by reference and writes into the in-out destination buffer `w` (`ComplexVector w` at `:378`). It builds the bumped `opA2p = (*funcA2)(std::abs(eig.imag()) * (1.0 + delta))` (`:650`), the `denom = i·δ·|Im λ|` (`:651-652`), the divided-difference `opAJ = BuildParSumOperator({1/denom, −1/denom}, {opA2p, A2n})` (`:653-654`), the derivative pencil `opJ = BuildParSumOperator({0, 1, 2λ, 1}, {opK, opC, opM, opAJ})` (`:655-656`), writes `opJ->Mult(v, w)` (`:657`), and — when `k > 0` (`:658`) — re-scopes the value pencil `A = BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM, A2n})` (`:661-662`), forms `S = eig·I − H` (`:663`), solves `Sv2 = S.fullPivLu().solve(v2)` (`:664`), back-projects `XSv2 = MatVecMult(X, Sv2)` (`:665`) and `XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2))` (`:666`), and accumulates `opJ->AddMult(XSv2, w, 1.0)` (`:668`) and `A->AddMult(XSSv2, w, -1.0)` (`:669`). The destination buffer `w` is overwritten; `A2n` is the line-search-cached `A2(|Im λ|)`; `δ = √ε` is a solver-level constant (`:412`).
- **L1**: pure-functional `w = nleps_jacobian_action(T, λ, P, v, v₂)`. No destination buffer, no `A2`-caching, no build-form choice in the signature. One operator parameterized by the deflation-cardinality `k` (variadic) and the `Maybe C` damping axis (via the pencil). The big-space part is named as `apply_nonlinear_pencil` of the derivative pencil `T'`; the deflation coupling as the product-rule `apply_nonlinear_pencil(T', λ, X·S⁻¹v₂) − apply_nonlinear_pencil(T, λ, X·S⁻²v₂)`. Linearity laws hold; the divided-difference `A2'` accuracy, the `λ`-nonlinearity, the big-space-only output, and the three-build-form bit-difference are explicit non-laws.

## Evidence

- `palace/linalg/nleps.cpp:649-669` — the `w = J·v` block: the complete positive site for the operator's structure. Comment `:649` ("Compute w = J * v.") names the operator; comment `:659-660` ("w1 = T'(l) v1 + U'(l) v2 = T'(l) v1 + T'(l)XS v2 − T(l)XS^2 v2") names the big-space + deflation-coupling decomposition in the source's own words (with the `S`-means-`S⁻¹` comment/code convention).
- `palace/linalg/nleps.cpp:650` — `auto opA2p = (*funcA2)(std::abs(eig.imag()) * (1.0 + delta))` — the bumped-frequency `A2((1+δ)|Im λ|)` evaluation (the divided-difference numerator's first term; Semantics point 3).
- `palace/linalg/nleps.cpp:651-652` — `const std::complex<double> denom = std::complex<double>(0.0, delta * std::abs(eig.imag()))` — the divided-difference denominator `i·δ·|Im λ|` (the `i` reflecting frequency = `Im λ`; Semantics point 3).
- `palace/linalg/nleps.cpp:653-654` — `std::unique_ptr<ComplexOperator> opAJ = BuildParSumOperator({1.0 / denom, -1.0 / denom}, {opA2p.get(), A2n.get()}, true)` — the divided-difference derivative `A2'(λ) = (A2((1+δ)|Im λ|) − A2(|Im λ|)) / denom` (the `A2'` closure of the derivative pencil; non-law on exact-derivative).
- `palace/linalg/nleps.cpp:655-656` — `auto opJ = BuildParSumOperator({0.0 + 0.0i, 1.0 + 0.0i, 2.0 * eig, 1.0 + 0.0i}, {opK, opC, opM, opAJ.get()}, true)` — the derivative pencil `T'(λ) = C + 2λM + A2'(λ)` (coefficients `{0, 1, 2λ, 1}`; law 3; the `apply_nonlinear_pencil` law-5 coefficient vector, now firmed).
- `palace/linalg/nleps.cpp:657` — `opJ->Mult(v, w)` — the big-space Jacobian `w = T'(λ)·v` (law 1, 3; the `apply_nonlinear_pencil(T', λ, v)` apply; Semantics point 1, big-space-only output).
- `palace/linalg/nleps.cpp:658` — `if (k > 0)` — the deflation-present guard; the `k = 0` reduction to the bare derivative-pencil apply (law 1, variant axis).
- `palace/linalg/nleps.cpp:661-662` — `auto A = BuildParSumOperator({1.0 + 0.0i, eig, eig * eig, 1.0 + 0.0i}, {opK, opC, opM, A2n.get()}, true)` — the re-scoped value pencil `T(λ)` (coefficients `{1, λ, λ², 1}`) for the `−T(λ)·X·S⁻²·v₂` term (Semantics point 4; the same `apply_nonlinear_pencil` value-pencil shape).
- `palace/linalg/nleps.cpp:663` — `const Eigen::MatrixXcd S = eig * Eigen::MatrixXcd::Identity(k, k) - H` — the `k×k` linearization block `S = λI − H` (shared with the residual / solve siblings).
- `palace/linalg/nleps.cpp:664` — `const Eigen::VectorXcd Sv2 = S.fullPivLu().solve(v2)` — the first dense solve `S⁻¹·v₂` (`lu_solve`; Semantics point 2, law 4).
- `palace/linalg/nleps.cpp:665` — `const ComplexVector XSv2 = MatVecMult(X, Sv2)` — the back-projection `X·(S⁻¹·v₂)` (`linear_combination`; law 4).
- `palace/linalg/nleps.cpp:666` — `const ComplexVector XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2))` — the second sequential solve + back-projection `X·(S⁻¹·(S⁻¹·v₂)) = X·S⁻²·v₂` (the `lu_solve` ∘ `linear_combination` for the product-rule `S⁻²` term; Semantics point 2, law 4).
- `palace/linalg/nleps.cpp:668` — `opJ->AddMult(XSv2, w, 1.0)` — accumulates `+T'(λ)·X·S⁻¹·v₂` (the product-rule first coupling term; law 4).
- `palace/linalg/nleps.cpp:669` — `A->AddMult(XSSv2, w, -1.0)` — accumulates `−T(λ)·X·S⁻²·v₂` (the product-rule `∂_λ S⁻¹ = −S⁻²` second coupling term; Semantics point 2, law 4).
- `palace/linalg/nleps.cpp:411-412` — `// Delta used in to compute divided difference Jacobian.` then `const auto delta = std::sqrt(std::numeric_limits<double>::epsilon())` — the `δ = √ε` finite-difference step (Semantics point 3; the divided-difference non-law).
- `palace/linalg/nleps.cpp:378` — `ComplexVector v, u, w, c, w0, z, du, v_trial` — the `w` destination-buffer declaration (big-space `ComplexVector`, confirming the output is a single big-space vector; Semantics point 1).
- `palace/linalg/nleps.cpp:673-675` — `const std::complex<double> u2_w0 = std::complex<double>(w2.adjoint() * u2)` then `delta_eig = -(linalg::Dot(GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(), w, w0)` — the consumer: `w = J·v` enters the undamped Newton eigenvalue correction only through the big-space dot `⟨w, w0⟩` (confirms `w` is treated as a pure big-space vector — no `w₂` companion; Semantics point 1).
- `palace/linalg/nleps.cpp:676` — `z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0)` — the Newton step direction `z = −delta_eig·w − u` (the second consumer of `w`).
- `palace/linalg/nleps.cpp:177-181` — `QuasiNewtonSolver::SetExtraSystemMatrix(std::function<std::unique_ptr<ComplexOperator>(double)> A2) { funcA2 = A2; }` — the nonlinear closure type `Real -> ComplexOperator`; the `A2` evaluated at `|Im λ|` and `(1+δ)|Im λ|` to form the divided difference.
- `palace/linalg/nleps.cpp:329-347` — `MatVecMult(X, y)` — the `X·y` reconstruction (`z = 0; for j: AXPBYPCZ(...) into z`), a length-`k` `linear_combination` over the deflation basis with the complex real/imag split; the back-projection primitive at `:665,:666`.
- `palace/linalg/nleps.cpp:606-619` — deflation-basis growth: each converged `v` normalized (`:610-611`), `X.resize(k+1)` (`:614`), `X[k] = v` (`:615`), `H` filled (`:616-618`), `k++` (`:619`) — confirms `X` is the raw normalized-eigenvector invariant-pair basis (NOT orthonormalized → the `S⁻¹`/`S⁻²` coupling is load-bearing; Semantics point 5) and the variadic-in-`k` axis.
- `palace/linalg/nleps.cpp:354-362` — the deflation-scheme references (Effenberger 2013; Jarlebring–Koskela–Mele 2018; SLEPc-NEP minimality index 1) — the literature anchor for the extended-deflated-problem form whose `λ`-derivative this operator applies.
- `book/src/L1/apply_nonlinear_pencil.md` (firm, cycle-021) — the interior pencil-apply atom this operator differentiates; its **law 5** ("Jacobian as derivative-pencil apply", `book/src/L1/apply_nonlinear_pencil.md:65`) records this operator as the deferred follow-up this dispatch firms; its linearity-in-`v` law 1 is the basis for law 2 here; its firm-on-positive-structure status (`:98`) is the precedent for this entry's firm decision; its evidence row cites the Jacobian build at `:655` (`book/src/L1/apply_nonlinear_pencil.md:111`).
- `book/src/L1/nleps_deflated_residual.md` (firm, cycle-022) — the **residual sibling**: it *applies* the extended deflated operator `[[T(λ), U(λ)], [Xᴴ, 0]]`; `nleps_jacobian_action` applies its `λ`-derivative (law 5). Its deflation coupling `U(λ) = T(λ)·X·(λI−H)⁻¹` (its semantics point 1) is the function this operator differentiates by the product rule.
- `book/src/L1/nleps_deflated_solve.md` (firm, cycle-023) — the **solve sibling**: shares the block `S = λI − H`, the `X·` back-projection, the `lu_solve` small-dense solve, the `S`-means-`S⁻¹` comment/code convention (its semantics point 4), and the over-unification guard. Its `:145` records the non-gating test-coverage caveat this entry inherits.
- `book/src/L1/lu_solve.md` (firm, cycle-022) — the small-dense direct-solve leaf realizing the two `fullPivLu().solve` solves at `:664,:666`.
- `book/src/L2/linear_combination.md` (firm) — the `X·S⁻¹v₂` / `X·S⁻²v₂` back-projections (the `MatVecMult(X, ·)` at `:665,:666`).
- `book/src/L0/eigensolver-wrapper.md` — the L0 NLEPS reference note.
- No dedicated unit test: NLEPS has zero `test/unit/**` hits (same absence as `eigsolve` / `apply_nonlinear_pencil` / `nleps_deflated_residual` / `nleps_deflated_solve`); the firm decision rests on positive structural citation, not a test.
```

## Index edits

The three `book/src/L1/index.md` edits, anchored precisely (non-overlapping with the parallel `nleps_eigenvalue_correction` harvester):

**(1) Firm count + cohort one-liner** — change line 31's `**Firm (17)**` opener to `**Firm (18)**` and extend the trailing list:

> `**Firm (18)** — element-wise updates, BLAS-1 reductions, the opaque-operator gate, the constructed-operator solve gate, the eigenmode-solve gate, the polynomial-smoother gate, the divergence-free projector gate, the nonlinear-pencil interior atom, the NEP deflated-residual extension, the small-dense direct-solve gate, the NEP deflated-solve extension, and the NEP quasi-Newton Jacobian action:`

(NOTE for integrator: if the parallel `nleps_eigenvalue_correction` harvester also lands firm this cycle, reconcile the count to `**Firm (19)**` and append both trailing clauses. This entry claims the `17→18` increment for the Jacobian action.)

**(2) Vocabulary-cohort bullet** — insert immediately after the `nleps_deflated_solve` bullet (current line 49), before the blank line and the `**Rough-in (test-coverage-bounded)**` header (line 51):

```text
- [`nleps_jacobian_action`](./nleps_jacobian_action.md) — pure-functional **quasi-Newton Jacobian action** of the nonlinear eigenvalue problem `w = nleps_jacobian_action(T, λ, P, v, v₂)`; applies the Jacobian `J(λ)` of the extended deflated residual operator and returns the **big-space-only** direction `w = J(λ)·v` (no coordinate companion — the asymmetry with the residual/solve siblings). The big-space part is the **derivative-pencil** apply `apply_nonlinear_pencil(T', λ, v)` over `T'(λ) = C + 2λM + A2'(λ)` (coefficients `{0, 1, 2λ, 1}`, finite-difference `A2'`); when `k > 0` it adds the product-rule deflation-coupling derivative `T'(λ)·X·S⁻¹·v₂ − T(λ)·X·S⁻²·v₂` (the `λ`-derivative of the residual's `U(λ) = T(λ)·X·(λI−H)⁻¹`, with `∂_λ S⁻¹ = −S⁻²` realized as a double sequential `lu_solve`). The **derivative sibling** of [`nleps_deflated_residual`](./nleps_deflated_residual.md) (apply) and [`nleps_deflated_solve`](./nleps_deflated_solve.md) (inverse). Firm on exhaustive positive structural citation of the sole `w = J·v` site (`palace/linalg/nleps.cpp:649-669`); the `k = 0` case degenerates exactly to the derivative-pencil apply (the realization of `apply_nonlinear_pencil`'s deferred law-5 "Jacobian as derivative-pencil apply"). The one non-syntactic point — the divided-difference `A2'` (`δ = √ε`) making it a *quasi*-Newton approximate Jacobian — is a recorded load-bearing non-law, not an unconfirmed law, so it does not gate firm; the `eigsolve`-inherited no-dedicated-test caveat is non-gating. The fourth NEP-interior atom at L1.
```

**(3) Dep-map row** — insert immediately after the `nleps_deflated_solve` row (current line 87), before the `lanczos_step` row (line 88):

```text
| [`nleps_jacobian_action`](./nleps_jacobian_action.md) | `(T: NonlinearPencil[N], λ: Complex, P: DeflationState[N, k], v: Tensor[N], v₂: Vec[k]) → Tensor[N]` (big-space-only Jacobian action `w = J(λ)·v = T'(λ)·v + [k>0] (T'(λ)·X·S⁻¹·v₂ − T(λ)·X·S⁻²·v₂)`, `T'(λ) = C + 2λM + A2'(λ)`, `S = λI − H`) | [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md) (direct, derivative-pencil + value-pencil applies); [`lu_solve`](./lu_solve.md) (direct, the `S⁻¹`/`S⁻²` dense `k×k` solves); [`linear_combination`](../L2/linear_combination.md) (L2, `X·` back-projection); `apply_linop` (transitive) | `firm` (NEP deflation-extension Jacobian; L0: `palace/linalg/nleps.cpp:649-669` positive site + `:673-675` consumer; harvested cycle-024; derivative sibling of `nleps_deflated_residual`/`nleps_deflated_solve`; divided-difference `A2'` recorded as load-bearing non-law; `eigsolve`-inherited no-dedicated-test caveat non-gating) |
```

## Supporting evidence

- The big-space Jacobian site and the deflation-coupling block were read in full via `mcp__palace-codemap__read_range` over `palace/linalg/nleps.cpp:640-700` and `:648-670`; every cited `:NN` anchor was re-verified against on-disk content (the `apply_nonlinear_pencil` sibling's `:655` Jacobian-build citation matches the on-disk `opJ` build at `:655-656`).
- The `δ = √ε` finite-difference step was localized via `search_text` for `delta\s*=` (hit at `:412`) and read at `:405-420` (confirming the comment "Delta used in to compute divided difference Jacobian" at `:411`).
- The big-space-only output (Semantics point 1) was confirmed two ways: (a) `w` is a `ComplexVector` (big-space) at `:378`, not paired with a coordinate `w₂`; (b) the consumer at `:673-675` dots `w` only big-space (`⟨w, w0⟩`), with `w2`/`u2` being the *projection-direction* coordinates (output of `deflated_solve` at `:542`), not a Jacobian coordinate part. The `VectorXcd` declarations at `:398` and the `deflated_solve(c, c2, w0, w2)` call at `:542` were read to rule out a `J·v` coordinate companion.
- The product-rule structure (`∂_λ S⁻¹ = −S⁻²` ⟹ `U'(λ) = T'XS⁻¹ − TXS⁻²`) matches the source comment `T'(l)XS v2 − T(l)XS^2 v2` (`:659-660`) under the `nleps_deflated_solve`-documented `S`-means-`S⁻¹` convention; the two `.fullPivLu().solve` calls at `:664,:666` realize `S⁻¹` then `S⁻²`.

## Open questions / caveats

- **OQ `nleps-interior-atoms-remaining-jacobian-action-and-eigenvalue-correction` (open-questions.md:779) — partial closure.** This dispatch closes the **`nleps_jacobian_action`** half. The remaining piece is **`nleps_eigenvalue_correction`** (the eigenvalue-update step using the projection direction `w0` and this operator's output `w`, `palace/linalg/nleps.cpp:673-676`) — the direct consumer of `w = J·v`, dispatched in parallel this cycle. *Proposed OQ-ledger update (for integrator-per-report):* mark the Jacobian-action half resolved; carry forward the eigenvalue-correction half (or close the whole OQ if the parallel `nleps_eigenvalue_correction` harvester also lands this cycle). With this entry the NEP-interior cohort at L1 has four firm atoms (`apply_nonlinear_pencil`, `nleps_deflated_residual`, `nleps_deflated_solve`, `nleps_jacobian_action`); only the eigenvalue-correction step remains to complete the `eigsolve` `direct_newton` quasi-Newton-step decomposition.
- **`apply_nonlinear_pencil` law-5 follow-up — now realized.** `apply_nonlinear_pencil`'s law 5 ("Jacobian as derivative-pencil apply", `book/src/L1/apply_nonlinear_pencil.md:65`) recorded the Jacobian as a deferred follow-up — "the construction of `T'` … is deferred to a follow-up; see Open questions." This dispatch firms `T'` and the Jacobian action as its own L1 entry. No edit to `apply_nonlinear_pencil.md` is proposed here (one operator per invocation); a future lifter/cross-cutter pass MAY add a back-reference from its law 5 to this entry — surfaced here, not enacted.
- **L1>L0 mutation-rotation theme deferred (abstractor's domain).** The Jacobian-action L1>L0 lowering (the `BuildParSumOperator` + `Mult`/`AddMult` build-form, the in-place `w` destination buffer, the `A2n` line-search cache, the `δ = √ε` divided-difference assembly) is a separate L1>L0 theme, not authored here per the high→low discipline. It shares the `apply_nonlinear_pencil` / `nleps_deflated_residual` build-form lowering. Plan candidate: `nleps-jacobian-action-mutation-rotation` (L1>L0).
- **Layer-intro refresh (layer-intro-author's domain).** The `book/src/L1/index.md` §Context and §Semantics-overlay do not need a new motif for this operator (it reuses the "constructed-operator absorption" / NEP-interior-atom framing of the siblings). No intro refresh required beyond the firm-count / cohort / dep-map edits proposed above. Noted per spec (layer-intro is not this agent's domain).
- **Index/SUMMARY shared-file coordination.** Per the dispatch note, `book/src/L1/index.md` and `SUMMARY.md` are co-edited with the parallel `nleps_eigenvalue_correction` harvester. This report's proposed rows are anchored AFTER `nleps_deflated_solve` (the current last firm entry / row / SUMMARY line); the sibling harvester anchors ITS rows after this entry's. The Firm-count bump is claimed as `17→18` here; the integrator reconciles to `17→19` if both land. No textual overlap between the two harvesters' inserts.

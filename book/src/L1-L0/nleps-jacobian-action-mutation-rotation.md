---
status: firm
layer: L1>L0
theme: nleps-jacobian-action-mutation-rotation
l1_anchor: book/src/L1/nleps_jacobian_action.md
l0_anchor: palace/linalg/nleps.cpp:649-669
justification: structural
---

# nleps-jacobian-action-mutation-rotation

How the firm L1 [`nleps_jacobian_action`](../L1/nleps_jacobian_action.md) form lowers into its L0
source: the `// Compute w = J * v.` block inside Palace's `QuasiNewtonSolver` NEP loop
(`palace/linalg/nleps.cpp:649-669`). This is the **derivative** of the extended deflated residual
operator — the Jacobian sibling of
[`nleps-deflated-residual-mutation-rotation`](./nleps-deflated-residual-mutation-rotation.md)
(the residual *applies* the extended deflated operator `[[T(λ), U(λ)], [Xᴴ, 0]]`; this Jacobian
applies its `λ`-derivative `[T'(λ), U'(λ)]`) and the derivative-pencil specialization of
[`apply-nonlinear-pencil-mutation-rotation`](./apply-nonlinear-pencil-mutation-rotation.md) (the
big-space part is `apply_nonlinear_pencil` of the derivative pencil `T'` rather than the value
pencil `T`). When `k = 0` it degenerates to one bare derivative-pencil apply. This entry, with
its dispatch-2 sibling `nleps-eigenvalue-correction-mutation-rotation`, completes the NEP-interior
L1>L0 lowering cohort (with the residual + solve themes and
[`apply-nonlinear-pencil-mutation-rotation`](./apply-nonlinear-pencil-mutation-rotation.md)).

## Slug

`nleps-jacobian-action-mutation-rotation`

## L1 form (LHS)

The pure-functional L1 operator — no destination buffer, no `A2`-caching, no build-form choice
in the signature (`book/src/L1/nleps_jacobian_action.md:14-28`):

    nleps_jacobian_action
      :: (T: NonlinearPencil[N], λ: Complex, P: DeflationState[N, k], v: Tensor[N], v₂: Vec[k])
         -> Tensor[N]

    nleps_jacobian_action(T, λ, P, v, v₂) =
      let T'   = derivative_pencil(T, λ)              -- coeffs {0, 1, 2λ, 1}; closure A2'(λ)
          w₀   = apply_nonlinear_pencil(T', λ, v)      -- T'(λ)·v   (big-space derivative-pencil apply)
      in if k == 0 then w₀                             -- no deflation: bare derivative-pencil apply
         else
           let S   = λ·I[k] − P.H                       -- the k×k linearization block
               a   = lu_solve(S, v₂)                    -- S⁻¹·v₂
               b   = lu_solve(S, a)                     -- S⁻²·v₂   (second sequential dense solve)
               cpl = apply_nonlinear_pencil(T', λ, linear_combination(P.X, a))   -- + T'(λ)·X·S⁻¹·v₂
                   − apply_nonlinear_pencil(T,  λ, linear_combination(P.X, b))   -- − T(λ)·X·S⁻²·v₂
           in w₀ + cpl

`T` is the opaque pencil `T(λ) = K + λC + λ²M + A2(λ)`; `T'` is the **derivative pencil** (same
`K, C, M`, coefficient vector `{0, 1, 2λ, 1}` so `K` drops, and the divided-difference derivative
closure `A2'(λ) ≈ (A2((1+δ)|Im λ|) − A2(|Im λ|)) / (i·δ·|Im λ|)`, `δ = √ε`); `P` is the converged
invariant pair `(X, H)` with `X` **not orthonormal** (raw normalized eigenvectors); `k = 0` is
the un-deflated case (`book/src/L1/nleps_jacobian_action.md:31-40`). The output is **big-space
only** (`-> Tensor[N]`); there is **no** coordinate companion `w₂` (the asymmetry with the
residual / solve siblings — `book/src/L1/nleps_jacobian_action.md:75`). The destination buffer
`w`, the `A2n` line-search cache, the value-pencil re-scoping, and the build-form choice are
**not** in the L1 signature — they are exactly what this lowering exposes.

## L0 form (RHS)

The `w = J * v` block — **not** a named lambda (unlike the residual `compute_residual` /
solve `deflated_solve` siblings) but a straight-line block inside the quasi-Newton
`while (it < nleps_it)` loop that captures `funcA2`, `delta`, `eig`, `A2n`, `opK`/`opC`/`opM`,
`k`, `H`, `X` and writes into the in-out destination buffer `w` (`ComplexVector w` declared at
`palace/linalg/nleps.cpp:378`):

    // nleps.cpp:649 — the source's own statement of the Jacobian action:
    // Compute w = J * v.
    auto opA2p = (*funcA2)(std::abs(eig.imag()) * (1.0 + delta));         // :650  A2((1+δ)|Im λ|)
    const std::complex<double> denom =                                   // :651-652  i·δ·|Im λ|
        std::complex<double>(0.0, delta * std::abs(eig.imag()));
    std::unique_ptr<ComplexOperator> opAJ =                              // :653-654  A2'(λ):
        BuildParSumOperator({1.0 / denom, -1.0 / denom},                 //   (A2((1+δ)|Imλ|) − A2(|Imλ|))/denom
                            {opA2p.get(), A2n.get()}, true);
    auto opJ = BuildParSumOperator({0.0 + 0.0i, 1.0 + 0.0i, 2.0 * eig,   // :655-656  T'(λ):
                                    1.0 + 0.0i},                         //   coeffs {0, 1, 2λ, 1}
                                   {opK, opC, opM, opAJ.get()}, true);
    opJ->Mult(v, w);                                                     // :657  w := T'(λ)·v
    if (k > 0)  // Deflation                                             // :658
    {
      // w1 = T'(l) v1 + U'(l) v2 = T'(l) v1 + T'(l)XS v2 - T(l)XS^2 v2. // :660-661  (source comment)
      auto A = BuildParSumOperator({1.0 + 0.0i, eig, eig * eig,          // :662-663  T(λ):
                                    1.0 + 0.0i},                         //   coeffs {1, λ, λ², 1}
                                   {opK, opC, opM, A2n.get()}, true);
      const Eigen::MatrixXcd S =                                         // :664  S = λI − H
          eig * Eigen::MatrixXcd::Identity(k, k) - H;
      const Eigen::VectorXcd Sv2 = S.fullPivLu().solve(v2);              // :665  S⁻¹·v₂
      const ComplexVector XSv2 = MatVecMult(X, Sv2);                     // :666  X·(S⁻¹·v₂)
      const ComplexVector XSSv2 =                                        // :667  X·(S⁻¹·(S⁻¹·v₂)) = X·S⁻²·v₂
          MatVecMult(X, S.fullPivLu().solve(Sv2));
      opJ->AddMult(XSv2, w, 1.0);                                        // :668  w += T'(λ)·X·S⁻¹·v₂
      A->AddMult(XSSv2, w, -1.0);                                        // :669  w −= T(λ)·X·S⁻²·v₂
    }

## Rewrite — forward (L1 → L0)

The pure `nleps_jacobian_action(T, λ, P, v, v₂)` rewrites to the `w = J * v` block, evaluated
with the destination buffer `w` (in place of the returned `Tensor[N]`) and the line-search-cached
`A2n` operator (in place of the absorbed value-pencil build). The rewrite proceeds in three
sub-patterns. The L0-only material the L1 signature drops:

- **Destination buffer.** `w` (a `ComplexVector`, declared at `palace/linalg/nleps.cpp:378`) is
  overwritten by `opJ->Mult(v, w)` (`:657`) and then accumulated into by the two `AddMult` calls
  (`:668`, `:669`); the L1 form returns `Tensor[N]` by value. `w` is a reused scratch buffer
  across Newton iterations — buffer reuse, a transparent L1>L0 trick. **Big-space only**: `w` is
  a single `ComplexVector`, not an extended pair — confirming the operator has no coordinate
  companion (the residual / solve siblings return extended `(·, ·)` pairs; the Jacobian action
  does not).
- **The `A2n` line-search cache.** The value pencil `A` (`:662-663`) reuses the
  line-search-cached `A2n` operator (the `A2(|Im λ|)` closure built once and held across the
  Armijo line search), so the `−T(λ)·X·S⁻²·v₂` term does not re-assemble `A2`. The source comment
  at `:660-661` explains the local scoping ("Scoping T(l) here lets the line search overwrite A2n
  freely; with no deflation we skip it"). Pure-functional re-evaluation at L1; an L0 caching /
  scoping concern only.
- **The value-pencil build is re-scoped inside the `k > 0` branch.** `A = BuildParSumOperator
  ({1, λ, λ², 1}, {opK, opC, opM, A2n.get()}, true)` (`:662-663`) re-builds the same value-pencil
  shape used in the residual / solve setup; inherited from `apply_nonlinear_pencil`'s lowering
  (the `{1, λ, λ², 1}` pencil-build form), referenced here, not re-derived. It is *not* built in
  the `k = 0` path (the scoping note) — the value pencil is needed only for the deflation
  coupling's second term.

### Sub-pattern A — big-space Jacobian: divided-difference derivative pencil + `opJ->Mult` (the derivative-pencil apply)

This is the load-bearing rotation point that distinguishes this theme from its siblings: the
big-space part is `apply_nonlinear_pencil` of the **derivative pencil** `T'(λ)`, not the value
pencil `T(λ)`. Palace builds `T'` in three steps and applies it:

    auto opA2p = (*funcA2)(std::abs(eig.imag()) * (1.0 + delta));   // :650  A2((1+δ)|Im λ|)
    const std::complex<double> denom =                             // :651-652  denom = i·δ·|Im λ|
        std::complex<double>(0.0, delta * std::abs(eig.imag()));
    std::unique_ptr<ComplexOperator> opAJ =                        // :653-654  A2'(λ) divided difference
        BuildParSumOperator({1.0 / denom, -1.0 / denom}, {opA2p.get(), A2n.get()}, true);
    auto opJ = BuildParSumOperator({0.0 + 0.0i, 1.0 + 0.0i, 2.0 * eig, 1.0 + 0.0i},  // :655-656
                                   {opK, opC, opM, opAJ.get()}, true);
    opJ->Mult(v, w);                                               // :657  w := T'(λ)·v

Three firm-leaf recognitions:

1. **Divided-difference derivative `A2'(λ)` (`:650-654`).** The bumped-frequency evaluation
   `opA2p = (*funcA2)(|Im λ|·(1+δ))` (`:650`), the denominator `denom = i·δ·|Im λ|` (`:651-652`),
   and the operator difference `opAJ = BuildParSumOperator({1/denom, −1/denom}, {opA2p, A2n})`
   (`:653-654`) realize the one-sided divided difference `A2'(λ) ≈ (A2((1+δ)|Im λ|) −
   A2(|Im λ|)) / (i·δ·|Im λ|)`, `δ = √ε` (`palace/linalg/nleps.cpp:412`). The `A2n` operand is the
   line-search-cached `A2(|Im λ|)`. **This is a load-bearing numerical approximation, not the
   exact analytic derivative** — it is *why* the solver is *quasi*-Newton. Recorded as an explicit
   non-law (the realized `A2'` ≠ exact `∂_λ A2`; the `O(δ)` truncation traded against `O(ε/δ)`
   roundoff at `δ = √ε` is part of the algorithm), per the CLAUDE.md trick taxonomy. The `i` in
   the denominator reflects that the frequency `|Im λ|` is the imaginary part of `λ`, so a
   frequency bump is an `i·δ·|Im λ|` bump in `λ`.
2. **Derivative pencil `T'(λ)` (`:655-656`).** `opJ = BuildParSumOperator({0, 1, 2λ, 1}, {opK,
   opC, opM, opAJ})` builds the derivative pencil with coefficient vector `{0, 1, 2λ, 1}` — `K`
   gets weight `0` (it drops: `∂_λ K = 0`), `C` keeps weight `1` (`∂_λ(λC) = C`), `M` gets weight
   `2λ` (`∂_λ(λ²M) = 2λM`), and the divided-difference `A2'` enters with weight `1`. This is the
   `{1, λ, λ², 1}` value-pencil build form of
   [`apply-nonlinear-pencil-mutation-rotation`](./apply-nonlinear-pencil-mutation-rotation.md)
   (its Sub-pattern B, the `BuildParSumOperator`-dual), specialized to the **derivative**
   coefficient vector. The pencil-build is referenced from that theme, not re-derived.
3. **Big-space apply `opJ->Mult(v, w)` (`:657`).** The single `Mult` writes `w := T'(λ)·v` — the
   L1 `w₀ = apply_nonlinear_pencil(T', λ, v)`. By `apply_nonlinear_pencil`'s term-decomposition
   law 3 this unfolds to `apply_linop(C, v)·1 + apply_linop(M, v)·2λ + apply_linop(A2'(λ), v)`
   (the `K` term drops). When `k = 0` the `if (k > 0)` guard (`:658`) is false, so the block ends
   here: `w = T'(λ)·v` is the **bare derivative-pencil apply** — the L1 form's law 1 reduction
   (`book/src/L1/nleps_jacobian_action.md:89`). `nleps_jacobian_action` strictly extends the
   derivative-pencil apply with the deflation coupling.

Justification kind: **structural** (with a load-bearing divided-difference non-law) — `:655-657`
are the syntactic derivative-pencil build + apply recognized as `apply_nonlinear_pencil` of `T'`;
the `:658` guard is the syntactic `k = 0` reduction. The one non-structural recording is the
divided-difference `A2'` (`:650-654`), carried per the trick taxonomy.

Citations:
- `palace/linalg/nleps.cpp:649` — `// Compute w = J * v.` — the source's own naming of the
  operator.
- `palace/linalg/nleps.cpp:650` — `auto opA2p = (*funcA2)(std::abs(eig.imag()) * (1.0 + delta));`
  — the bumped-frequency `A2((1+δ)|Im λ|)`.
- `palace/linalg/nleps.cpp:651-652` — `const std::complex<double> denom = std::complex<double>
  (0.0, delta * std::abs(eig.imag()));` — the divided-difference denominator `i·δ·|Im λ|`.
- `palace/linalg/nleps.cpp:653-654` — `BuildParSumOperator({1.0 / denom, -1.0 / denom},
  {opA2p.get(), A2n.get()}, true)` — the divided-difference `A2'(λ)` (the quasi-Newton non-law).
- `palace/linalg/nleps.cpp:655-656` — `BuildParSumOperator({0.0 + 0.0i, 1.0 + 0.0i, 2.0 * eig,
  1.0 + 0.0i}, {opK, opC, opM, opAJ.get()}, true)` — the derivative pencil `T'(λ)` (coeffs
  `{0, 1, 2λ, 1}`).
- `palace/linalg/nleps.cpp:657` — `opJ->Mult(v, w);` — the big-space apply `w := T'(λ)·v`.
- `palace/linalg/nleps.cpp:658` — `if (k > 0)` — the deflation-present guard; when `k = 0` only
  `:650-657` run, so `w = T'(λ)·v` is the bare derivative-pencil apply (law 1 reduction).
- `palace/linalg/nleps.cpp:412` — `const auto delta = std::sqrt(std::numeric_limits<double>::
  epsilon())` — the `δ = √ε` divided-difference step (the non-law's accuracy trade-off).
- `book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md` — Sub-pattern B (the
  `{1, λ, λ², 1}` `BuildParSumOperator`-dual pencil-build form), specialized here to the
  derivative coefficient vector `{0, 1, 2λ, 1}`.

### Sub-pattern B — deflation back-projection: the *double* `fullPivLu().solve` ∘ `MatVecMult` (the `S⁻²` signature)

The deflation coupling needs two back-projected vectors: `X·S⁻¹·v₂` (for the `T'` term) and
`X·S⁻²·v₂` (for the `T` term). They are built in four C++ lines (`:664-667`):

    const Eigen::MatrixXcd S = eig * Eigen::MatrixXcd::Identity(k, k) - H;  // :664  S = λI − H
    const Eigen::VectorXcd Sv2 = S.fullPivLu().solve(v2);                  // :665  S⁻¹·v₂
    const ComplexVector XSv2 = MatVecMult(X, Sv2);                         // :666  X·(S⁻¹·v₂)
    const ComplexVector XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2));   // :667  X·(S⁻¹·(S⁻¹·v₂)) = X·S⁻²·v₂

The structural signature of this lowering — distinguishing it from the residual sibling's
**single** `S⁻¹` solve — is that **`S⁻¹` is applied twice in sequence**: `:665` computes
`Sv2 = S⁻¹·v₂`, then `:667` feeds that result back through `S.fullPivLu().solve(Sv2)` to get
`S⁻¹·(S⁻¹·v₂) = S⁻²·v₂`. This **materializes `S⁻²·v₂` as two sequential dense solves rather than
forming `S⁻²` explicitly** — the differentiated counterpart of the residual's single `S⁻¹` solve.
It is the L0 realization of the product-rule term `∂_λ S⁻¹ = −S⁻¹·(∂_λ S)·S⁻¹ = −S⁻²` (since
`∂_λ S = ∂_λ(λI − H) = I`). Three firm-leaf recognitions composed:

1. **Block `S = λI − H` (`:664`)** — `S = eig * Identity(k,k) - H` materializes the `k×k`
   linearization block as a dense `Eigen::MatrixXcd` (λ = `eig`, the current Newton eigenvalue
   estimate; `H` the redundantly-stored Rayleigh block). This is the **same block** as the
   residual / solve siblings, except the Jacobian uses the un-lagged `eig` (the Jacobian is
   evaluated at the current iterate, not the lagged `eig_opInv` the inner solve uses).
2. **The two solves `S.fullPivLu().solve` (`:665`, `:667`)** are the dense `k×k`
   [`lu_solve`](../L1/lu_solve.md) leaf (full-pivot LU, `Eigen`) — the NLEPS full-pivot-LU
   sub-pattern of [`lu-solve-mutation-rotation`](./lu-solve-mutation-rotation.md) (its Sub-pattern
   A cites the NLEPS `fullPivLu().solve` kernel). Both compute into a **fresh destination** (`Sv2`,
   then the anonymous temporary fed to `MatVecMult` at `:667`) — the fresh-destination form, not
   the in-place RHS overwrite the solve sibling uses. These dense solves are **distinct** from the
   iterative big-space [`ksp_solve`](../L1/ksp_solve.md) — different cost models and
   representations; the small-dense solve runs entirely on the redundant coordinate space.
3. **The two `MatVecMult(X, ·)` back-projections (`:666`, `:667`)** are the length-`k`
   [`linear_combination`](../L2/linear_combination.md) fold over the deflation basis,
   `X·c = Σⱼ c(j)·X[j]`. Their L0 body (`palace/linalg/nleps.cpp:329-347`) zero-initializes `z`,
   then for each `j` does two real-valued `linalg::AXPBYPCZ` calls (the complex-vector real/imag
   split: the four-real-multiply complex product expanded across the `.Real()` / `.Imag()`
   carriers). The L2>L1 lowering of this fold is
   [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md);
   this theme references its `MatVecMult` realization, it does not re-derive the fold.

**The deflation basis `X` is NOT orthonormal** — it stores raw normalized eigenvectors with no
inter-column orthogonalization (`palace/linalg/nleps.cpp:606-619`: each converged `v` scaled by
`1/‖v‖₂` at `:610-611`, stored at `X[k] = v` at `:615`, no Gram-Schmidt). This is *why* the
coupling carries the `S⁻¹` / `S⁻²` linearization-block solves rather than a trivial transpose; the
non-orthonormal basis is load-bearing and is the same fact that keeps the L2 `deflate` combinator
distinct from `orthogonalize` (the over-unification guard). Recorded here so the
lowering does not collapse the `fullPivLu().solve` solves into no-ops.

Justification kind: **structural** — `:664-667` are the syntactic compositions `MatVecMult ∘
fullPivLu().solve` of firm leaves; the dense-solve kernel is inherited from
`lu-solve-mutation-rotation` Sub-pattern A and the fold from `linear-combination-fold-
specialization`. The **double `S⁻¹` for `S⁻²`** is read straight off the verified site (the
product-rule `∂_λ S⁻¹ = −S⁻²` structure).

Citations:
- `palace/linalg/nleps.cpp:664` — `const Eigen::MatrixXcd S = eig * Eigen::MatrixXcd::Identity
  (k, k) - H;` — the `k×k` block `S = λI − H` (λ = the current `eig`).
- `palace/linalg/nleps.cpp:665` — `const Eigen::VectorXcd Sv2 = S.fullPivLu().solve(v2);` — the
  first dense solve `S⁻¹·v₂` (`lu_solve`, fresh destination).
- `palace/linalg/nleps.cpp:666` — `const ComplexVector XSv2 = MatVecMult(X, Sv2);` — the
  back-projection `X·(S⁻¹·v₂)` (`linear_combination` over the deflation basis).
- `palace/linalg/nleps.cpp:667` — `const ComplexVector XSSv2 = MatVecMult(X, S.fullPivLu().solve
  (Sv2));` — the **second sequential solve** + back-projection `X·(S⁻¹·(S⁻¹·v₂)) = X·S⁻²·v₂` (the
  `lu_solve` ∘ `linear_combination` for the product-rule `S⁻²` term; the `S⁻¹`-applied-twice
  signature).
- `palace/linalg/nleps.cpp:329-347` — `MatVecMult(X, y)`: the `X·y` fold body (`z = 0`; per-`j`
  complex AXPY via two `AXPBYPCZ` on the real/imag carriers).
- `palace/linalg/nleps.cpp:606-619` — deflation-basis growth (normalize at `:610-611`, store at
  `:615`, no orthogonalization): the `X`-not-orthonormal fact (the `S⁻¹`/`S⁻²`-is-load-bearing
  reason).
- `book/src/L1-L0/lu-solve-mutation-rotation.md` — Sub-pattern A (NLEPS full-pivot-LU dense
  kernel): the `fullPivLu().solve` leaf at `:665`, `:667` (this theme references, not re-derives).
- `book/src/L2-L1/linear-combination-fold-specialization.md` — the L2>L1 lowering of the
  `MatVecMult` back-projection fold; live link.

### Sub-pattern C — product-rule accumulation: two `AddMult` on two pencils (the `+T'·XS⁻¹v₂ − T·XS⁻²v₂` collapse)

The deflation coupling `U'(λ)·v₂ = T'(λ)·X·S⁻¹·v₂ − T(λ)·X·S⁻²·v₂` is accumulated into the
big-space destination `w` (which already holds `T'(λ)·v` from Sub-pattern A) by **two `AddMult`
calls on two different pencils** (`:668-669`):

    opJ->AddMult(XSv2, w, 1.0);    // :668   w += 1.0 · T'(λ)·X·S⁻¹·v₂   (the derivative pencil opJ)
    A->AddMult(XSSv2, w, -1.0);    // :669   w += (−1.0) · T(λ)·X·S⁻²·v₂  (the value pencil A)

Two firm-leaf recognitions:

1. **`opJ->AddMult(XSv2, w, 1.0)` (`:668`)** accumulates `+T'(λ)·X·S⁻¹·v₂` into `w` using the
   **derivative pencil** `opJ` (the same `{0, 1, 2λ, 1}` pencil built at `:655-656` and already
   applied to `v` at `:657`), scale `+1.0`. This is `apply_nonlinear_pencil(T', λ, X·S⁻¹v₂)` —
   the first product-rule term.
2. **`A->AddMult(XSSv2, w, -1.0)` (`:669`)** accumulates `−T(λ)·X·S⁻²·v₂` into `w` using the
   **value pencil** `A` (the `{1, λ, λ², 1}` pencil re-scoped at `:662-663`), scale `−1.0`. This
   is `apply_nonlinear_pencil(T, λ, X·S⁻²v₂)` — the second product-rule term (the
   `∂_λ S⁻¹ = −S⁻²` sign carried by the `−1.0` scale).

The L0 thus computes, by the **linearity-in-`v`** of `apply_nonlinear_pencil` (its law 1), the
big-space sum

    w = T'(λ)·v                            (from :657, Sub-pattern A)
      + T'(λ)·X·S⁻¹·v₂                      (from :668, AddMult +1)
      − T(λ)·X·S⁻²·v₂                       (from :669, AddMult −1)
      = w₀ + U'(λ)·v₂,

i.e. the L1 `w₀ + cpl`. The **two `AddMult` accumulate directly into the destination `w`** rather
than materializing the three-term sum in fresh buffers — a **transparent performance trick** at
L1 (the value is identical, only intermediate buffers are elided). Note the two `AddMult`s use
**two distinct operators** (`opJ` the derivative pencil for the `+` term, `A` the value pencil for
the `−` term): this is the algebraic content of the product rule (the derivative pencil
differentiates the `T'·XS⁻¹` part; the value pencil carries the `−T·XS⁻²` part), not a free
re-association.

The three-step `Mult` (`:657`) + `AddMult` (`:668`) + `AddMult` (`:669`) accumulation is **not
bit-identical** to an algebraically-equal single combined apply: the accumulation orders the
floating-point additions differently, and the matrix-free `A2'` / `A2` terms inherit
reduction-tree non-associativity from `apply_linop`. The law identities are mathematical; their
floating-point realization is exact modulo accumulation-order noise
(`book/src/L1/nleps_jacobian_action.md:103`, the recorded non-law). Load-bearing per the CLAUDE.md
trick taxonomy, recorded not erased.

Justification kind: **structural** (with a load-bearing accumulation-order note) — `:668-669` are
the syntactic `AddMult` accumulations recognized as the two product-rule `apply_nonlinear_pencil`
terms; the two-distinct-pencils structure is the product rule read off the source, the
accumulate-into-destination is the transparent buffer-elision trick.

Citations:
- `palace/linalg/nleps.cpp:660-661` — the source comment `w1 = T'(l) v1 + U'(l) v2 = T'(l) v1 +
  T'(l)XS v2 - T(l)XS^2 v2` (the source's own product-rule decomposition; `S` written where the
  code applies `S⁻¹`/`S⁻²`, the same `S`-means-`S⁻¹` comment/code convention the solve sibling
  documents).
- `palace/linalg/nleps.cpp:662-663` — `auto A = BuildParSumOperator({1.0 + 0.0i, eig, eig * eig,
  1.0 + 0.0i}, {opK, opC, opM, A2n.get()}, true);` — the re-scoped value pencil `T(λ)` (coeffs
  `{1, λ, λ², 1}`) for the `−T(λ)·X·S⁻²·v₂` term (the value-pencil build form; reuses the cached
  `A2n`).
- `palace/linalg/nleps.cpp:668` — `opJ->AddMult(XSv2, w, 1.0);` — accumulates `+T'(λ)·X·S⁻¹·v₂`
  (the product-rule first term; derivative pencil, scale `+1`).
- `palace/linalg/nleps.cpp:669` — `A->AddMult(XSSv2, w, -1.0);` — accumulates `−T(λ)·X·S⁻²·v₂`
  (the product-rule `∂_λ S⁻¹ = −S⁻²` second term; value pencil, scale `−1`).
- `book/src/L1/apply_nonlinear_pencil.md` — the linearity-in-`v` law 1 (`T(λ)·a + T(λ)·b =
  T(λ)·(a+b)`) that makes the accumulate-into-`w` the algebraic sum.

## The big-space-only output — the load-bearing recording

The structural signature distinguishing this lowering from the residual / solve siblings is that
**`w` is big-space only — there is no coordinate companion `w₂`**. The residual returns an
extended pair `(r, r₂)` plus a norm; the solve returns an extended pair `(x1, x2)`; the Jacobian
action writes only the big-space `w` (`:657`, `:668-669`). The `w2` that appears at the consumer
site (`:673`, `w2.adjoint() * u2`) is the **output of the deflated solve** (the projection
direction `(w0, w2)`), **not** a coordinate part of `J·v`. The downstream Newton eigenvalue
update consumes `w` only through the big-space dot `⟨w, w0⟩` (`palace/linalg/nleps.cpp:675`,
`linalg::Dot(GetComm(), w, w0)`), confirming `w` is treated as a pure big-space vector. This
asymmetry — residual / solve are extended-space, the Jacobian action is big-space-only — is part
of the operator's contract (`book/src/L1/nleps_jacobian_action.md:75`); collapsing it into an
extended-pair shape would silently invent a `w₂` the source never computes.

Per the CLAUDE.md trick taxonomy this is a **load-bearing** recording (the output shape is part
of the contract, not a transparent rewrite): the over-unification guard from the operator entry
(`book/src/L1/nleps_jacobian_action.md:126`) is carried here.

## Applicability conditions

The rewrite preserves semantics when:

1. **The pencil `T(λ)` and its derivative `T'(λ)` are bound exactly as for the solver setup** —
   `T'` over `{0, 1, 2λ, 1}` with the divided-difference `A2'` (`:653-656`), `T` over
   `{1, λ, λ², 1}` with the cached `A2n` (`:662-663`); the `with-C` / `without-C` damping axis is
   absorbed by the pencils (when `C = Nothing`, the derivative pencil's weight-`1` `C` term drops,
   the `2λM` and `A2'` terms remain).
2. **Element type is complex-only** — the NEP pencil and the `ComplexVector` / `Eigen::VectorXcd`
   / `Eigen::MatrixXcd` carriers. No real specialization is witnessed.
3. **The deflation cardinality `k` is variadic** — it grows by one per converged eigenpair
   (`:606-619`); the rewrite is parameterized by `k`, with the `k = 0` branch (the `if (k > 0)`
   guard at `:658`) the un-deflated degeneration to the bare derivative-pencil apply.
4. **In-place destination overwrite is permitted because `w` is dead-on-entry scratch.** `w` is
   overwritten by `opJ->Mult(v, w)` (`:657`) then accumulated into (`:668`, `:669`); it is a
   reused Newton-iteration scratch buffer (`:378`).
5. **The `δ = √ε` divided-difference step is a fixed solver-level constant** (`:412`), not a
   structural variant — the quasi-Newton approximate-Jacobian accuracy trade-off (load-bearing
   non-law). The `A2n` line-search caching and the value-pencil re-scoping are transparent L1>L0
   performance / scoping concerns.
6. **Single-rank scope** (CLAUDE.md "Scope"): the big-space `Mult` / `AddMult` apply (`:657`,
   `:668`, `:669`) inherit the bit-deterministic-reduction-order trade-off from `apply_linop` /
   `apply_nonlinear_pencil`. The `k×k` dense `Eigen` solves (`:665`, `:667`) are rank-local by
   construction (the coordinate space is replicated on all ranks).

## Justification kind

**Structural** — the rewrite is the syntactic expansion of one pure L1 form into the L0
destination-buffer composition. Three structural recognitions carry the theme: (A) `:650-657` is
the divided-difference derivative-pencil build + big-space apply recognized as
`apply_nonlinear_pencil` of the **derivative** pencil `T'`, with the `:658` guard the `k = 0`
reduction; (B) `:664-667` are the `MatVecMult ∘ fullPivLu().solve` back-projections, with the
**double `S⁻¹`** materializing the product-rule `S⁻²` term; (C) `:668-669` are the two `AddMult`
accumulations on the two distinct pencils realizing the product-rule `+T'·XS⁻¹v₂ − T·XS⁻²v₂`. Two
load-bearing non-structural recordings are carried, not absorbed: the **divided-difference `A2'`**
(Sub-pattern A; the quasi-Newton approximate Jacobian, a non-law) and the **big-space-only
output** (the no-`w₂` contract). The `Mult` + `AddMult` accumulation-order bit-difference, the
`A2n` line-search caching, and the value-pencil re-scoping are L1>L0 residues recorded above; the
fresh-destination dense solves are the `lu-solve-mutation-rotation` kernel.

## Speculative L1 operators

**None.** Every constituent is **already firm L1/L2 vocabulary**:
[`apply_nonlinear_pencil`](../L1/apply_nonlinear_pencil.md) (firm),
[`lu_solve`](../L1/lu_solve.md) (firm),
[`linear_combination`](../L2/linear_combination.md) (firm L2),
[`apply_linop`](../L1/apply_linop.md) (firm, transitive via `apply_nonlinear_pencil`'s term
decomposition). This theme composes existing firm leaves; it proposes no new rough-in operators.
The back-projection is the L2 `deflate` combinator's constituent, but that L2 combinator is named
here only to mark the upward fan-out boundary (and the deflate-promotion guard) — it is **not**
part of this theme.

Additional cited L0 ranges:

- `palace/linalg/nleps.cpp:177-181` — `QuasiNewtonSolver::SetExtraSystemMatrix(...)` — the
  nonlinear closure type `Real -> ComplexOperator` (the `A2` evaluated at `|Im λ|` and
  `(1+δ)|Im λ|`; the `funcA2` provenance).
- `palace/linalg/nleps.cpp:676` — `z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0);` — the Newton step
  direction `z = −delta_eig·w − u` (the second big-space consumer of `w`).

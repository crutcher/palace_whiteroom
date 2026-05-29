---
agent: harvester
invoked_at: 2026-05-29T105500Z
scope: L1 operator: nleps_eigenvalue_correction
status: pending
integrated_at: 2026-05-29T140000Z
integration_commit: f3be056
integration_notes: "Applied cycle-024 (staging row 2). Firm L1 operator nleps_eigenvalue_correction landed (fifth/final NEP-interior atom); L1 firm 18→19, NEP-interior cohort COMPLETE. New chapter + L1/index.md + SUMMARY.md; jacobian-action forward-ref upgraded to live link. No gate hits."
inputs:
  - book/src/L1/nleps_deflated_solve.md (firm sibling, cycle-023)
  - book/src/L1/apply_nonlinear_pencil.md (firm sibling, cycle-021)
  - book/src/L1/nleps_deflated_residual.md (firm sibling, cycle-022)
  - palace/linalg/nleps.cpp:672-677 (the delta_eig eigenvalue-correction step, verified verbatim)
  - palace/linalg/nleps.cpp:587,:657,:691,:704-708 (committed residual, Jacobian action, line-search apply/commit)
  - palace/linalg/vector.hpp:246-256, vector.cpp:674-685 (dot conjugation convention)
  - OQ: nleps-interior-atoms-remaining-jacobian-action-and-eigenvalue-correction
  - parallel dispatch: nleps_jacobian_action (the w = J·v producer; plain-text forward-ref, not yet on disk)
---

# CYCLE: Formalize nleps_eigenvalue_correction at L1

## Summary

`nleps_eigenvalue_correction` is the fourth and final deferred NLEPS interior atom: the **scalar quasi-Newton eigenvalue-correction step** of Palace's `QuasiNewtonSolver`. Given the committed extended residual `[u; u2]`, the Jacobian action `w = J·v`, and a (deflated) projection direction `[w0; w2]`, it computes the undamped Newton eigenvalue increment `δλ = −⟨[w0;w2], [u;u2]⟩ / ⟨[w0;w2], w⟩` and packages the coupled vector-step right-hand side `[z; z2] = [−δλ·w − u; −u2]` that the subsequent `nleps_deflated_solve` inverts. It is the scalar half of the coupled `(λ, v)` quasi-Newton step (Jarlebring–Koskela–Mele 2018): the eigenvalue moves by a one-dimensional projected-Newton ratio while the eigenvector moves by the deflated linear solve of the assembled RHS. The Armijo line search then damps the combined `(δλ, du)` step. This atom currently lives entirely inline in the `Solve` loop body with no separate L1 entry; this dispatch firms it up. The structural laws are syntactic identities on a single positive source site (`palace/linalg/nleps.cpp:672-677`) over firm leaves (`dot`, `axpby`/`axpbypcz`) — so the entry is `firm` on the same firm-on-positive-structure footing as its three NLEPS siblings, with the inherited (non-gating) NLEPS no-dedicated-test caveat.

## Proposed changes

```new:book/src/L1/nleps_eigenvalue_correction.md
# nleps_eigenvalue_correction

Mutation-lifted **quasi-Newton eigenvalue-correction step** of the nonlinear eigenvalue problem (NEP): given the committed extended residual `[u; u2]`, the Jacobian action `w = J·v`, and a (deflated) projection direction `[w0; w2]`, compute the undamped Newton eigenvalue increment `δλ` and the coupled vector-step right-hand side `[z; z2]` the deflated linear solve inverts. The scalar half of the coupled `(λ, v)` Newton step inside Palace's `QuasiNewtonSolver` — the one-dimensional projected-Newton ratio that moves the eigenvalue estimate, paired with the RHS assembly that moves the eigenvector.

## Context

Palace's `QuasiNewtonSolver` (`palace/linalg/nleps.cpp`) computes eigenpairs of the NEP `T(λ)·x = 0` for the pencil `T(λ) = K + λC + λ²M + A2(λ)` one at a time by a coupled quasi-Newton iteration on the pair `(λ, v)` (Jarlebring–Koskela–Mele 2018 quasi-Newton; Effenberger 2013 deflation — `palace/linalg/nleps.cpp:354-362`). Each outer iteration of the `while (it < nleps_it)` loop (`palace/linalg/nleps.cpp:596`) updates **both** the scalar eigenvalue estimate `λ` (`eig`) and the eigenvector estimate `v` together. The update splits into three atoms: (1) the **Jacobian action** `w = J·v` (the parameter-derivative pencil apply `T'(λ)·v`, plus its deflation coupling — the parallel `nleps_jacobian_action` dispatch); (2) **this operator**, the scalar eigenvalue correction `δλ` and the coupled vector-step RHS assembly; and (3) the **deflated linear solve** [`nleps_deflated_solve`](./nleps_deflated_solve.md) that inverts the assembled RHS into the vector increment `du`. An **Armijo line search** (`palace/linalg/nleps.cpp:688-714`) then damps the combined `(δλ, du)` step.

`nleps_eigenvalue_correction` is the scalar coupling between the residual and the Jacobian. In a coupled Newton step on `(λ, v)`, the eigenvalue increment is determined by projecting the residual and the Jacobian action onto a one-dimensional direction `[w0; w2]` (the "left vector" / projection direction, here `T⁻¹c` for a fixed random `c`, normalized — `palace/linalg/nleps.cpp:542-545`) and taking the ratio: `δλ = −⟨[w0;w2], [u;u2]⟩ / ⟨[w0;w2], w⟩`. This is the standard one-dimensional Newton correction `δλ = −f / f'` lifted to the projected extended space — `⟨[w0;w2], [u;u2]⟩` is the projected residual (the "`f`") and `⟨[w0;w2], w⟩` is the projected Jacobian-times-eigenvector (the "`f'`"). The operator then assembles the coupled vector-step RHS `[z; z2] = [−δλ·w − u; −u2]` that [`nleps_deflated_solve`](./nleps_deflated_solve.md) inverts to produce the eigenvector increment.

It sits in the interior of the [`eigsolve`](./eigsolve.md) gate's `direct_newton` orchestration variant — `eigsolve` treats `QuasiNewtonSolver` as one opaque orchestration; `nleps_eigenvalue_correction` is the per-step scalar-update atom the deflated branch of that orchestration is built from, the scalar counterpart of the vector-valued [`nleps_deflated_solve`](./nleps_deflated_solve.md) / [`nleps_deflated_residual`](./nleps_deflated_residual.md). The L0 NLEPS reference note is [`L0/eigensolver-wrapper`](../L0/eigensolver-wrapper.md).

## Signature

```text
nleps_eigenvalue_correction
  :: (resid: ExtendedVec[N, k], jac_action: Tensor[N], proj_dir: ExtendedVec[N, k])
     -> NewtonStep[N, k]

type ExtendedVec[N, k] = { big: Tensor[N], coord: Vec[k] }
type NewtonStep[N, k]  = { δλ: Complex, z: Tensor[N], z2: Vec[k] }

nleps_eigenvalue_correction(resid, jac_action, proj_dir) =
  let u   = resid.big,   u2 = resid.coord      -- committed extended residual [u; u2]
      w0  = proj_dir.big, w2 = proj_dir.coord   -- normalized projection direction [w0; w2]
      w   = jac_action                          -- Jacobian action J·v  (big-space only)
      num = dot(w0, u) + dot(w2, u2)            -- ⟨[w0;w2], [u;u2]⟩   projected residual
      den = dot(w0, w)                          -- ⟨[w0;w2], w⟩        projected Jacobian-apply
      δλ  = − num / den                         -- undamped Newton eigenvalue increment
      z   = axpby(−δλ, w, −1, u)                -- −δλ·w − u           coupled vector-step RHS (big)
      z2  = scal(−1, u2)                        -- −u2                 coupled vector-step RHS (coord)
  in { δλ, z, z2 }
```

Shape contract (bunsen-style, named axes):

- `resid` — `ExtendedVec[N, k]` — the committed extended residual at the current iterate: `resid.big = u : Tensor[N]` (big-space residual) and `resid.coord = u2 : Vec[k]` (coordinate-space residual). At the L0 site these are the `u`/`u2` buffers written by the committed-point residual evaluation (`palace/linalg/nleps.cpp:587`, `compute_residual(eig, v, v2, u, u2, A2n)` — the firm sibling [`nleps_deflated_residual`](./nleps_deflated_residual.md) is the producer). Read-only.
- `jac_action` — `Tensor[N]` — the Jacobian action `w = J·v` (the parameter-derivative pencil apply `T'(λ)·v` plus its deflation coupling), big-space only. Produced by the `nleps_jacobian_action` atom (`palace/linalg/nleps.cpp:650-672`, the `opJ->Mult(v, w)` at `:657` plus the `k > 0` deflation block). Read-only. There is **no** coordinate-space part of the Jacobian action — the extended Jacobian's lower block-row is `[Xᴴ, 0]` (constant in `λ`), so its parameter-derivative coordinate part is zero (see Semantics point 4).
- `proj_dir` — `ExtendedVec[N, k]` — the normalized projection direction `[w0; w2]`: `proj_dir.big = w0 : Tensor[N]` and `proj_dir.coord = w2 : Vec[k]`. At L0 this is the deflated solve `[w0; w2] = T⁻¹c` for a fixed random extended `c`, normalized to unit extended-norm (`palace/linalg/nleps.cpp:542-545`). It is held fixed across the inner correction; its role is purely as a projection direction ("only used as a projection direction for the eigenvalue correction" — source comment `:540`). Read-only.
- result — `NewtonStep[N, k]` — `δλ : Complex` (the undamped eigenvalue increment), `z : Tensor[N]` and `z2 : Vec[k]` (the coupled vector-step RHS the deflated solve inverts into the eigenvector increment).

The axis `N` is uniform across `u`, `w`, `w0`, and `z` (the eigenproblem is square; the residual, Jacobian action, projection direction, and step RHS all live in the same big space). The deflation-cardinality axis `k` is uniform across `u2`, `w2`, and `z2`; it is the **variadic-in-`k`** axis — `k` grows by one per converged eigenpair (`palace/linalg/nleps.cpp:606-619`), so `nleps_eigenvalue_correction` is parameterized by deflation cardinality, not a family of fixed-`k` specializations. The `k = 0` (un-deflated) case drops the coordinate parts (`u2`, `w2`, `z2` are empty; `num = dot(w0, u)`). Element type is **complex-only** (inherited from the complex NEP pencil and the `Eigen::VectorXcd` / `ComplexVector` carriers).

`δλ` is a single complex scalar — the projected ratio of two extended-space inner products. The big-space inner products `dot(w0, u)` and `dot(w0, w)` are the distributed [`dot`](./dot.md); the coordinate inner product `dot(w2, u2)` is the local `Eigen` `w2.adjoint() * u2`. The conjugated operand in all three is the **projection direction** (`w0`, `w2`), the first argument of the L1 [`dot`](./dot.md) convention `⟨x, y⟩ = xᴴ y` (`book/src/L1/dot.md:43`).

## Semantics

`nleps_eigenvalue_correction(resid, jac_action, proj_dir)` computes the scalar Newton eigenvalue increment and assembles the coupled vector-step right-hand side. The committed source (`palace/linalg/nleps.cpp:672-677`):

```text
// Undamped Newton step for the eigenvalue; the line search damps it.   :672
u2_w0    = w2.adjoint() * u2                                            :673   ⟨w2, u2⟩
δλ       = −(dot(u, w0) + u2_w0) / dot(w, w0)                           :674-675
z        = −δλ·w − u           (z.AXPBYPCZ(-δλ, w, -1.0, u, 0.0))        :676
z2       = −u2                                                          :677
```

The result is the triple `{ δλ, z, z2 }`. The L1 form is pure-functional: the same `(resid, jac_action, proj_dir)` yields the same `NewtonStep`. The L0 source overwrites the destination buffers `z` (a big-space `ComplexVector`) and `z2` (an `Eigen::VectorXcd`) in place, and consumes `u`/`u2` into `z`/`z2` (so the subsequent line-search trial may freely overwrite `u`/`u2`, source comment `:699-700`); those destination bindings and the consume-then-reuse aliasing are L1>L0 lowering concerns, not part of the L1 signature.

Five semantic points are load-bearing and recorded rather than smoothed:

**(1) `δλ` is a projected one-dimensional Newton ratio over the extended space.** The numerator `⟨[w0;w2], [u;u2]⟩ = w0ᴴu + w2ᴴu2` (`palace/linalg/nleps.cpp:673-675`) is the residual projected onto the direction `[w0; w2]` — the scalar "`f`" of the Newton ratio. The denominator `⟨[w0;w2], w⟩ = w0ᴴw` (`:675`) is the Jacobian-times-eigenvector projected onto the same direction — the scalar "`f'`" (note the Jacobian action `w` has no coordinate part, so only the big-space `w0ᴴw` appears; see point 4). The increment `δλ = −f/f'` is the standard scalar Newton step. This is what makes the eigenvalue update **rank-one / scalar** rather than a full linear solve: the eigenvalue is a single complex unknown, and its correction is a ratio, not an inverse-of-a-matrix. The projection direction `[w0; w2]` is the deflated solve of a *fixed* random extended `c` (`:542`), so it is constant across the inner correction; its only role is to project the coupled extended system down to the one-dimensional eigenvalue subspace.

**(2) The conjugated operand is the projection direction `[w0; w2]`, in all three inner products.** Under the C++ free-function convention `linalg::Dot(comm, x, y) = yᴴx` — the **second** C++ argument is conjugated (`palace/linalg/vector.hpp:246`, corroborated by the `LocalDot` real/imag split `palace/linalg/vector.cpp:674-685`) — `linalg::Dot(GetComm(), u, w0) = w0ᴴu` (`:675`) and `linalg::Dot(GetComm(), w, w0) = w0ᴴw` (`:675`) conjugate the second C++ argument `w0`. The Eigen coordinate term `w2.adjoint() * u2 = w2ᴴu2` (`:673`) conjugates `w2` (Eigen `.adjoint()` is the conjugate-transpose of `w2`). So the conjugated operand in every term is the **projection direction** (`w0` / `w2`), which is the **first** argument of the L1 [`dot`](./dot.md) convention `⟨x, y⟩ = xᴴy` (`book/src/L1/dot.md:43`). Both framings — "C++ arg-2-conjugating" and "L1 arg-1-conjugated" — name the same conjugated operand. This is why the L1 signature writes `dot(w0, u)`, `dot(w2, u2)`, `dot(w0, w)`: the projection direction first.

**(3) The vector-step RHS is `[z; z2] = [−δλ·w − u; −u2]`, the linearized residual at the eigenvalue-corrected point.** Once `δλ` is fixed, the eigenvector increment solves (via the deflated linear solve) the linearized equation whose RHS is the residual plus the eigenvalue-correction's first-order contribution to it: `z = −(u + δλ·w)` (`:676`, `z.AXPBYPCZ(-δλ, w, -1.0, u, 0.0)` = `−δλ·w − 1·u + 0·z`) and `z2 = −u2` (`:677`). The big-space RHS `z = −δλ·w − u` couples the chosen eigenvalue increment `δλ` (through the Jacobian action `w`) into the eigenvector solve — this is the coupling that makes the `(λ, v)` step a genuine coupled Newton step rather than two independent univariate updates. The coordinate RHS `z2 = −u2` is the plain negated coordinate residual (the Jacobian's coordinate block is `λ`-independent, point 4, so the eigenvalue increment does not enter the coordinate RHS).

**(4) The Jacobian action has no coordinate part — the extended Jacobian's lower block-row is `λ`-independent.** The extended deflated operator's lower block-row is `[Xᴴ, 0]` (the coordinate-residual map `r₂ = Xᴴ·vv`, from [`nleps_deflated_residual`](./nleps_deflated_residual.md) semantics), which is **constant in `λ`** (it carries no `λ`-dependence — `X` and the zero block are fixed). Its parameter-derivative is therefore zero, so the Jacobian action `w = J·v` has only a big-space part (`palace/linalg/nleps.cpp:657`, `opJ->Mult(v, w)`, into the big-space `w`; the `k > 0` deflation block `:658-671` accumulates only into the big-space `w`, never a `w2`). This is why the denominator is `⟨[w0;w2], w⟩ = w0ᴴw` (only the big-space inner product, `:675`) and why there is no `w2`-analog of `dot(w0, w)`. The coordinate component `w2` of the *projection direction* still appears in the numerator (`w2ᴴu2`, point 2) because the *residual* `[u; u2]` does have a coordinate part — only the *Jacobian action* lacks one.

**(5) The eigenvalue is corrected by the damped increment; the line search damps `δλ` and `du` together.** The undamped `δλ` (`:674-675`) is applied damped: `eig_trial = eig + α·δλ` (`palace/linalg/nleps.cpp:691`) for a backtracking `α ∈ {1, 0.5, 0.25, …}` (Armijo, `:688-714`), with the eigenvector trial `v_trial = v + α·du` formed in lock-step (`:692-697`) so the coupled `(λ, v)` step is damped by a single `α`. The committed point is `eig = eig_trial` once the Armijo sufficient-decrease test passes (`:704-708`). The L1 operator produces the **undamped** `δλ` and RHS; the damping (`α`) and the commit are the line-search orchestration's concern (L1>L0 / the `direct_newton` orchestration), not part of this atom's signature. The undamped/`δλ`-is-applied-with-`α` split is recorded so a caller does not assume the operator commits the eigenvalue.

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Linearity of `δλ` in the residual (at fixed `jac_action`, `proj_dir`)**: the map `[u; u2] ↦ δλ` is **linear** — `δλ(α·resid + β·resid')` `= α·δλ(resid) + β·δλ(resid')` for scalars `α, β`. Holds because the numerator `⟨[w0;w2], [u;u2]⟩` is a fixed sesquilinear functional of `[u; u2]` (linear in the residual, the second `dot` argument), the denominator `⟨[w0;w2], w⟩` is independent of the residual, and `δλ = −num/den` is linear in `num`. In particular `δλ = 0` when the residual is zero (a converged iterate produces no eigenvalue correction). The conjugation falls on the *projection direction*, not the residual, so the map is genuinely linear (not conjugate-linear) in the residual.

2. **Affine-in-residual / linear-in-`(δλ, residual)` RHS assembly**: the vector-step RHS `[z; z2] = [−δλ·w − u; −u2]` is linear in the pair `(δλ, [u; u2])` at fixed `jac_action` — `z = axpby(−δλ, w, −1, u)` is the firm [`axpby`](./axpby.md) (linear in `δλ` and `u`); `z2 = scal(−1, u2)` is the firm [`scal`](./scal.md). Composed with law 1 (`δλ` linear in the residual), the whole map `[u; u2] ↦ (δλ, [z; z2])` is linear in the extended residual at fixed `(jac_action, proj_dir)`. This factors the RHS assembly entirely through firm BLAS-1 vocabulary (`axpby`, `scal`).

3. **Newton-ratio defining property**: `δλ` is the increment that zeroes the *projected linearized residual* to first order: `⟨[w0;w2], [u;u2]⟩ + δλ·⟨[w0;w2], w⟩ = 0` by construction (`palace/linalg/nleps.cpp:674-675` solves exactly this for `δλ`). This is the scalar Newton condition: the residual projected onto `[w0; w2]`, plus the eigenvalue increment times the Jacobian-apply projected onto `[w0; w2]`, vanishes. Recorded as the algebraic characterization of the ratio (it is *why* the formula is `−num/den`).

4. **Coordinate-RHS independence from `δλ`**: `z2 = −u2` does not depend on `δλ` (or on `jac_action`). The eigenvalue increment couples into the big-space RHS `z` only (through `w`), never the coordinate RHS, because the Jacobian's coordinate block is `λ`-independent (semantics point 4). Witnessed by `z2 = -u2` (`:677`), a bare negation. This is the structural asymmetry between the big and coordinate parts of the vector-step RHS.

Laws that explicitly **do not** hold:

- **Linearity / polynomiality in `λ`**: `nleps_eigenvalue_correction` is not a function of `λ` in its signature — `λ` enters only indirectly, through its arguments (`resid` is evaluated at the current `eig`, `jac_action` is `J(λ)·v`, `proj_dir` is `T(σ)⁻¹c` at the lagged `σ`). The atom itself is a fixed algebraic combination of its three inputs. But the *upstream* dependence of `δλ` on `λ` is non-polynomial (the residual and Jacobian carry the nonlinear `A2`/`A2'` closures and the rational deflation coupling, inherited from [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md) and [`nleps_deflated_residual`](./nleps_deflated_residual.md)). Recorded so the eigenvalue-correction step is not assumed to be a polynomial map of the eigenvalue.
- **Well-definedness when `⟨[w0;w2], w⟩ = 0`**: the ratio `δλ = −num/den` is undefined (division by zero) when the projected Jacobian-apply `⟨[w0;w2], w⟩` vanishes — the projection direction is orthogonal to the Jacobian action. The source notes this near-singular case explicitly ("`<w0, w>` near-singular", `palace/linalg/nleps.cpp:684-686`) and relies on the Armijo line search + the outer divergence-restart (`:637-647`) to recover; it is a numerical-robustness concern, not an algebraic identity. Recorded as a non-law: `δλ` is a partial function of its inputs, well-defined only when the denominator is nonzero.
- **`δλ` commits the eigenvalue**: `nleps_eigenvalue_correction` produces the *undamped* increment; the committed eigenvalue is `eig + α·δλ` for the Armijo `α` (`:691`, `:708`). The operator does not commit `eig`. Recorded so a caller does not treat `δλ` as the final step.
- **Bit-determinism of the projected inner products**: the big-space `dot(w0, u)`, `dot(w0, w)` inherit reduction-tree non-associativity from [`dot`](./dot.md) (load-bearing per the CLAUDE.md trick taxonomy); the extended-space sum `num = w0ᴴu + w2ᴴu2` (big distributed + local Eigen) is one further accumulation. The ratio `δλ` is exact-modulo-roundoff in its inputs, but its bit value depends on the pinned reduction tree.

## Dependencies

- [`dot`](./dot.md) — direct. The three projected inner products: the numerator's big-space `⟨w0, u⟩` (`palace/linalg/nleps.cpp:675`) and coordinate `⟨w2, u2⟩` (`:673`, the local `w2.adjoint() * u2`), and the denominator's big-space `⟨w0, w⟩` (`:675`). Arg-1-conjugated convention pinned (`book/src/L1/dot.md:43`); the conjugated operand is the projection direction (semantics point 2).
- [`axpby`](./axpby.md) — direct. The big-space vector-step RHS `z = −δλ·w − u` is `z.AXPBYPCZ(-δλ, w, -1.0, u, 0.0)` (`palace/linalg/nleps.cpp:676`), an [`axpbypcz`](./axpbypcz.md) with `γ = 0` — i.e. the `axpby(−δλ, w, −1, u)` two-vector fused update (the `γ = 0` reduction is `axpbypcz` law-subsumes-`axpby`). Recorded as `axpby` since the third term is zero.
- [`scal`](./scal.md) — direct. The coordinate vector-step RHS `z2 = −u2` is a pure scaling `scal(−1, u2)` (`palace/linalg/nleps.cpp:677`, the Eigen `z2 = -u2`).

`nleps_eigenvalue_correction` consumes the output of two sibling atoms and feeds a third: it consumes the committed residual `[u; u2]` from [`nleps_deflated_residual`](./nleps_deflated_residual.md) (`palace/linalg/nleps.cpp:587`) and the Jacobian action `w` from `nleps_jacobian_action` (the parallel cycle-024 dispatch; `:657`, plain-text forward-reference — that chapter is not yet on disk), and it produces the vector-step RHS `[z; z2]` that [`nleps_deflated_solve`](./nleps_deflated_solve.md) inverts into the eigenvector increment `du` (`:682`, `deflated_solve(z, z2, du, du2)`). It is the scalar coupling that closes the per-step quasi-Newton chain `residual → jacobian-action → eigenvalue-correction → deflated-solve → line-search`.

## Variant axes

- **deflation-present**: `k = 0` (un-deflated) | `k > 0` (deflated). When `k = 0` the coordinate parts `u2`, `w2`, `z2` are empty, so `num = dot(w0, u)` (no `w2ᴴu2` term) and `z2 = []` (the `Eigen::VectorXcd` of size 0). One operator parameterized by `k`; variadic-in-`k`, not a fixed-`k` family. (The `delta_eig` formula at `:673-675` runs uniformly — when `k = 0`, `u2`/`w2` are zero-length and `w2.adjoint() * u2 = 0`.)
- **purpose (committed-step)**: the correction is computed once per accepted outer iteration (`palace/linalg/nleps.cpp:672-677`), then damped/committed by the line search (`:691`, `:708`). There is no trial/committed structural variant within the atom — the trial loop re-evaluates the *residual* (the sibling [`nleps_deflated_residual`](./nleps_deflated_residual.md)) at `eig + α·δλ`, not this correction.

Collapsed (absorbed) axes:

- **`AXPBYPCZ` (γ=0) L0 build-form** — the big-space RHS `z = −δλ·w − u` is realized by the fused `AXPBYPCZ` with a zero third coefficient; collapsed at L1 into the named [`axpby`](./axpby.md) (`axpby ≺ axpbypcz` subsumption). The Eigen `z2 = -u2` is the named [`scal`](./scal.md).
- **projection-direction lag and normalization** — the projection direction `[w0; w2]` is the lagged deflated solve `T(σ)⁻¹c`, normalized to unit extended-norm (`palace/linalg/nleps.cpp:542-545`); the lag (`σ = eig_opInv`) and the per-use normalization are L1>L0 numerical-Newton concerns, collapsed at L1 into the `proj_dir` argument (read-only, pre-normalized).
- **Armijo damping `α`** — the per-step backtracking factor applied to `δλ` (`:691`, `:709`) and the commit (`:708`) are line-search orchestration concerns, not part of this atom (the operator produces the undamped `δλ`; semantics point 5).

**Do NOT over-unify with [`nleps_deflated_solve`](./nleps_deflated_solve.md).** The deflated solve *inverts* a block linear system (a vector-valued operator producing `[x1; x2]`); `nleps_eigenvalue_correction` computes a *scalar* ratio `δλ` and *assembles* the RHS the solve then inverts. They are adjacent in the per-step chain (this atom's output `[z; z2]` is the solve's input `[b1; b2]`) but compute structurally different things — a scalar projected-Newton ratio + a BLAS-1 RHS assembly here, a Schur-complement block solve there. The shared `dot` constituent (this atom's projected inner products vs the solve's Gram/coordinate folds) is a leaf-vocabulary overlap, not a unification.

## Status

`firm` — the operator's structure is read directly from a single **positive** Palace source site (the eigenvalue-correction block `palace/linalg/nleps.cpp:672-677`, under the source's own comment "Undamped Newton step for the eigenvalue; the line search damps it" at `:672`) and corroborated at its consumer/producer sites (`:587` the committed residual `u`/`u2`, `:657` the Jacobian action `w`, `:542-545` the projection direction `[w0; w2]`, `:682` the downstream deflated solve, `:691`/`:708` the line-search damping/commit). Every constituent is read, not constructed: the three projected inner products are positive `linalg::Dot` / `.adjoint()*` calls (`:673`, `:675`), the eigenvalue ratio is a positive scalar expression (`:674-675`), the big-space RHS is a positive `AXPBYPCZ` (`:676`), the coordinate RHS is a positive Eigen negation (`:677`). The algebraic laws are syntactic identities — the residual-linearity (laws 1-2) is a fixed-`(jac_action, proj_dir)` composition of the firm `dot`/`axpby`/`scal` linear maps; the Newton-ratio defining property (law 3) is the algebra of the `−num/den` expression; the coordinate-RHS independence (law 4) is the bare `z2 = -u2`. Every dependency (`dot`, `axpby`, `scal`) is firm BLAS-1 vocabulary read from a positive site, so there is no constructive sub-part materialized from negative anchors, and no `partly-constructive` caveat is needed. This is the firm-on-positive-structure escape (the `apply_nonlinear_pencil` / `nleps_deflated_residual` / `nleps_deflated_solve` precedent), not the `eigsolve`-convergence-semantics situation.

**Single-algorithm concentration** (noted): the operator's only L0 anchor is `QuasiNewtonSolver` (one solver). This is acceptable — it is the firm precedent of all three NLEPS siblings (`apply_nonlinear_pencil`, `nleps_deflated_residual`, `nleps_deflated_solve`, all NLEPS-only and `firm`): the laws are operator-algebra facts on fully-specified positive source, not cross-algorithm generalizations.

**Test-coverage caveat** (inherited, non-gating): NLEPS has zero dedicated unit tests (the same absence recorded for `eigsolve` / `apply_nonlinear_pencil` / `nleps_deflated_residual` / `nleps_deflated_solve` — `search_text` for `QuasiNewton|nleps|funcA2|delta_eig` over `test/unit/**` returns zero hits). The firm decision rests on exhaustive positive structural citation, exactly as for the three siblings (`book/src/L1/nleps_deflated_solve.md:146`): the laws are syntactic identities and do not depend on convergence behaviour, so the missing convergence test does not gate them. The two non-syntactic facts — the `⟨[w0;w2], w⟩ = 0` near-singularity and the line-search damping — are recorded as non-laws, not asserted as identities, so they do not require a test either.

## L1 vs L0 distinction

- **L0**: the eigenvalue-correction block inside the `Solve` loop body (`palace/linalg/nleps.cpp:672-677`) reads the committed-residual buffers `u`/`u2` (written at `:587`), the Jacobian-action buffer `w` (written at `:657`), and the normalized projection-direction buffers `w0`/`w2` (written at `:542-545`). It computes the local Eigen scalar `u2_w0 = w2.adjoint() * u2` (`:673`), the complex scalar `delta_eig = -(linalg::Dot(GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(), w, w0)` (`:674-675`), then overwrites the destination buffer `z` via `z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0)` (`:676`) and the Eigen vector `z2 = -u2` (`:677`). The buffers `u`/`u2` are consumed into `z`/`z2` here so the subsequent line-search trial may overwrite them (`:699-700` comment); the `delta_eig` scalar feeds the line-search `eig_trial = eig + alpha * delta_eig` (`:691`).
- **L1**: pure-functional `{ δλ, z, z2 } = nleps_eigenvalue_correction(resid, jac_action, proj_dir)`. No destination buffers, no consume-then-reuse aliasing, no Armijo `α` in the signature. One operator parameterized by the deflation-cardinality `k` (variadic). The eigenvalue increment is named as the projected Newton ratio `−⟨[w0;w2], [u;u2]⟩ / ⟨[w0;w2], w⟩`; the big-space RHS as `axpby(−δλ, w, −1, u)`; the coordinate RHS as `scal(−1, u2)`. Residual-linearity laws hold; the `⟨[w0;w2], w⟩`-near-singularity, the line-search damping, and the upstream `λ`-nonlinearity are explicit non-laws.

## Evidence

- `palace/linalg/nleps.cpp:672-677` — the eigenvalue-correction block: the complete positive site for the operator's structure. Comment `:672` ("Undamped Newton step for the eigenvalue; the line search damps it") names the role in the source's own words. `:673` `const std::complex<double> u2_w0 = std::complex<double>(w2.adjoint() * u2)` (the coordinate inner product `w2ᴴu2`); `:674-675` `const std::complex<double> delta_eig = -(linalg::Dot(GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(), w, w0)` (the projected Newton ratio); `:676` `z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0)` (the big-space RHS `−δλ·w − u`); `:677` `z2 = -u2` (the coordinate RHS).
- `palace/linalg/nleps.cpp:587` — `double res = compute_residual(eig, v, v2, u, u2, A2n)` — the committed-point residual evaluation that writes `u`/`u2` (the `resid` argument; the sibling `nleps_deflated_residual` is the producer; semantics point 1).
- `palace/linalg/nleps.cpp:657` — `opJ->Mult(v, w)` — the Jacobian action `w = J·v` (the `jac_action` argument; the `nleps_jacobian_action` atom is the producer; semantics points 1, 4). The `k > 0` deflation block (`:658-671`) accumulates only into the big-space `w` (no `w2`), confirming the Jacobian action has no coordinate part (semantics point 4).
- `palace/linalg/nleps.cpp:542-545` — `deflated_solve(c, c2, w0, w2)` then the normalization (`norm_w0 = sqrt(|⟨w0,w0⟩| + ‖w2‖²)`, `w0 *= 1/norm_w0`, `w2 *= 1/norm_w0`) — the projection direction `[w0; w2]` (the `proj_dir` argument; lagged `T(σ)⁻¹c`, normalized; absorbed axis).
- `palace/linalg/nleps.cpp:540` — comment "The w0 vector is only used as a projection direction for the eigenvalue correction, so moderate accuracy suffices" — the source's statement of `[w0; w2]`'s role (semantics point 1).
- `palace/linalg/nleps.cpp:682` — `deflated_solve(z, z2, du, du2)` — the downstream deflated linear solve consuming this atom's output `[z; z2]` as its RHS, producing the eigenvector increment `du`/`du2` (consumer relationship; the `nleps_deflated_solve` sibling).
- `palace/linalg/nleps.cpp:691` — `const std::complex<double> eig_trial = eig + alpha * delta_eig` — the damped application of `δλ` in the Armijo line search (semantics point 5; the "`δλ` is undamped" non-law).
- `palace/linalg/nleps.cpp:704-708` — `if (res_trial <= (1.0 - armijo_c * alpha) * res || bt == max_backtrack - 1) { … eig = eig_trial; … }` — the Armijo sufficient-decrease test and the eigenvalue commit `eig = eig_trial` (semantics point 5; the commit is the line-search's concern, not this atom's).
- `palace/linalg/nleps.cpp:684-686` — comment "Newton overshoots when the linear-eigensolver seed is outside the basin or `<w0, w>` is near-singular" — the source's note of the `⟨[w0;w2], w⟩ = 0` near-singularity (the well-definedness non-law).
- `palace/linalg/vector.hpp:246` — `// Calculate the parallel inner product yᴴ x or yᵀ x` (the `Dot(comm, x, y)` template at `:248`) — the C++ free-function convention `linalg::Dot(comm, x, y) = yᴴx`, the **second** argument conjugated (semantics point 2).
- `palace/linalg/vector.cpp:674-685` — `LocalDot(const ComplexVector &x, const ComplexVector &y)` — the real/imag split `{Re(x)·Re(y) + Im(x)·Im(y), Im(x)·Re(y) − Re(x)·Im(y)}` = `yᴴx`, corroborating which operand is conjugated (semantics point 2).
- `palace/linalg/nleps.cpp:606-619` — deflation-basis growth (each converged `v` normalized `:610-611`, `X.resize(k+1)` `:614`, `X[k] = v` `:615`, `H` resized/filled `:616-618`, `k++` `:619`) — confirms the variadic-in-`k` axis (`u2`/`w2`/`z2` grow with `k`).
- `palace/linalg/nleps.cpp:354-362` — the deflation-scheme references (Effenberger 2013; Jarlebring–Koskela–Mele 2018; SLEPc-NEP minimality index 1) — the literature anchor for the coupled quasi-Newton `(λ, v)` step this scalar correction is the eigenvalue half of.
- `book/src/L1/nleps_deflated_residual.md` (firm, cycle-022) — the **residual** producer: it writes the committed `[u; u2]` (`:587`) this atom consumes. Its `Xᴴ·` coordinate-residual structure (lower block-row `[Xᴴ, 0]`, `λ`-independent) is the basis for semantics point 4.
- `book/src/L1/nleps_deflated_solve.md` (firm, cycle-023) — the **solve** consumer: it inverts this atom's output `[z; z2]` (`:682`). The over-unification guard against it (§Variant axes) is the dual of that entry's guard against `deflate`.
- `book/src/L1/apply_nonlinear_pencil.md` (firm, cycle-021) — the interior pencil-apply atom; its firm-on-positive-structure status (`book/src/L1/apply_nonlinear_pencil.md:98`) is the precedent for this entry's firm decision; its `λ`-nonlinearity non-law is inherited (upstream non-law).
- `book/src/L1/dot.md:43` — the pinned `⟨x, y⟩ = xᴴ y` arg-1-conjugated convention (the three projected inner products; semantics point 2).
- `book/src/L1/axpby.md` (firm) — the big-space RHS `z = −δλ·w − u` (`:676`, the `AXPBYPCZ` with `γ = 0`).
- `book/src/L1/scal.md` (firm) — the coordinate RHS `z2 = −u2` (`:677`, the Eigen negation).
- `book/src/L1/axpbypcz.md` (firm) — the literal L0 form of the big-space RHS (`AXPBYPCZ`); the `γ = 0` subsumption to `axpby`.
- `book/src/L0/eigensolver-wrapper.md` — the L0 NLEPS reference note.
- No dedicated unit test: NLEPS has zero `test/unit/**` hits (`QuasiNewton|nleps|funcA2|delta_eig`) — same absence as the three siblings; the firm decision rests on positive structural citation, not a test.
```

```edit:book/src/L1/index.md
| [`nleps_deflated_solve`](./nleps_deflated_solve.md) | `(K: Solver[NonlinearPencil[N] @ σ], P: DeflationState[N, k], λ: Complex, b1: Tensor[N], b2: Vec[k]) → { x1: Tensor[N], x2: Vec[k] }` (block-eliminate the extended deflated `(n+k)` system; `x1 = T(σ)⁻¹b1`, `x2 = SS⁻¹(b2 − Xᴴx1)` with `SS = −S⁻¹XᴴX`, `S = λI − H`, then `x1 −= X·(S⁻¹x2)`) | [`ksp_solve`](./ksp_solve.md) (direct, big-space block); [`lu_solve`](./lu_solve.md) (direct, the `S`/`SS` dense `k×k` solves); [`dot`](./dot.md) (Gram + coordinate RHS), [`axpy`](./axpy.md) (final correction); [`linear_combination`](../L2/linear_combination.md) (L2, `X·` back-projection) | `firm` (NEP deflation-extension solve; L0: `palace/linalg/nleps.cpp:504-537` positive site + `:542,:682,:735` call sites; harvested cycle-023; solve sibling of `nleps_deflated_residual`; `eigsolve`-inherited no-dedicated-test caveat non-gating) |
| [`nleps_eigenvalue_correction`](./nleps_eigenvalue_correction.md) | `(resid: ExtendedVec[N, k], jac_action: Tensor[N], proj_dir: ExtendedVec[N, k]) → { δλ: Complex, z: Tensor[N], z2: Vec[k] }` (projected scalar Newton step `δλ = −⟨[w0;w2],[u;u2]⟩ / ⟨[w0;w2],w⟩`; coupled vector-step RHS `z = −δλ·w − u`, `z2 = −u2`) | [`dot`](./dot.md) (the three projected inner products); [`axpby`](./axpby.md) (big-space RHS), [`scal`](./scal.md) (coordinate RHS) | `firm` (NEP eigenvalue-correction interior atom; L0: `palace/linalg/nleps.cpp:672-677` positive site + `:587,:657,:542-545,:682,:691,:708` consumer/producer sites; harvested cycle-024; scalar Newton half of the coupled `(λ, v)` step; consumes residual + Jacobian-action, feeds `nleps_deflated_solve`; `eigsolve`-inherited no-dedicated-test caveat non-gating) |
```

```edit:book/src/SUMMARY.md
- [nleps_deflated_solve](./L1/nleps_deflated_solve.md)
- [nleps_eigenvalue_correction](./L1/nleps_eigenvalue_correction.md)
```

## Operator content

The full firm chapter body is authored inside the `new:book/src/L1/nleps_eigenvalue_correction.md` fenced block above. Summary of its sections:

- **Slug + one-line**: the quasi-Newton eigenvalue-correction step of `QuasiNewtonSolver` — the scalar half of the coupled `(λ, v)` Newton step.
- **Signature**: `(resid: ExtendedVec[N, k], jac_action: Tensor[N], proj_dir: ExtendedVec[N, k]) -> NewtonStep[N, k]` with `NewtonStep = { δλ: Complex, z: Tensor[N], z2: Vec[k] }`. Named axes `N` (big space, square), `k` (deflation cardinality, variadic). Complex-only.
- **Semantics**: 5 load-bearing points — (1) `δλ` is a projected 1-D Newton ratio over the extended space; (2) the conjugated operand is the projection direction `[w0; w2]` in all three inner products; (3) the vector-step RHS `[z; z2] = [−δλ·w − u; −u2]` is the linearized residual at the eigenvalue-corrected point; (4) the Jacobian action has no coordinate part (lower block-row `[Xᴴ, 0]` is `λ`-independent); (5) the eigenvalue is committed damped by the Armijo `α`.
- **Algebraic laws**: 4 that hold (residual-linearity of `δλ`; linear-in-`(δλ, residual)` RHS assembly through firm `axpby`/`scal`; Newton-ratio defining property; coordinate-RHS independence from `δλ`). 4 explicit non-laws (`λ`-nonlinearity upstream; well-definedness fails when `⟨[w0;w2], w⟩ = 0`; `δλ` is undamped; reduction-tree non-determinism).
- **Dependencies**: `dot` (three projected inner products), `axpby` (big-space RHS), `scal` (coordinate RHS). Consumes `nleps_deflated_residual` (residual) + `nleps_jacobian_action` (Jacobian action, plain-text forward-ref); feeds `nleps_deflated_solve` (RHS).
- **Status**: `firm` (firm-on-positive-structure escape; syntactic-identity laws on firm BLAS-1 leaves; inherited non-gating NLEPS no-test caveat).
- **Evidence**: positive site `palace/linalg/nleps.cpp:672-677` + 11 corroborating citations, all verified verbatim against on-disk source this cycle.

## Supporting evidence

- The eigenvalue-correction block `palace/linalg/nleps.cpp:672-677` was read verbatim (verified line-by-line: `:672` comment, `:673` `u2_w0`, `:674-675` `delta_eig`, `:676` `z.AXPBYPCZ`, `:677` `z2 = -u2`).
- The `dot` conjugation convention was verified through the source itself (`palace/linalg/vector.hpp:246` comment "yᴴ x"; `palace/linalg/vector.cpp:674-685` `LocalDot` real/imag split) — not relied on from the sibling entries alone — to pin the projection-direction-is-conjugated fact (semantics point 2).
- The consumer/producer wiring (`:587` residual, `:657` Jacobian, `:542-545` projection direction, `:682` deflated solve, `:691`/`:708` line search) was read in context (lines 455-545, 600-720) to confirm the data flow and the `(λ, v)` coupling.
- The three firm NLEPS siblings (`apply_nonlinear_pencil`, `nleps_deflated_residual`, `nleps_deflated_solve`) supply the vocabulary precedent (the `ExtendedVec`/`DeflationState` shape language, the firm-on-positive-structure status rationale, the over-unification-guard discipline, the inherited non-gating no-test caveat).

## Open questions / caveats

- **OQ `nleps-interior-atoms-remaining-jacobian-action-and-eigenvalue-correction` — eigenvalue-correction half closed.** This dispatch lands the eigenvalue-correction atom (`nleps_eigenvalue_correction`). The Jacobian-action half (`w = J·v`, `palace/linalg/nleps.cpp:650-672`) is the parallel cycle-024 dispatch (`nleps_jacobian_action`). When both land, the OQ closes and the four-piece deferred NLEPS interior sequence (`apply_nonlinear_pencil` → `nleps_deflated_residual` → `nleps_deflated_solve` → `{nleps_jacobian_action, nleps_eigenvalue_correction}`) is complete; the full per-step quasi-Newton chain `residual → jacobian-action → eigenvalue-correction → deflated-solve → line-search` is then firm at L1.
- **`nleps_jacobian_action` forward-reference is plain-text.** The `jac_action` argument (`w = J·v`) is produced by the parallel `nleps_jacobian_action` dispatch, not yet on disk. The chapter and dep-map row reference it as **plain text / inline-code** (`nleps_jacobian_action`), not a live link, per the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention — to avoid an `mdbook-linkcheck2` hard build error. The integrator may upgrade it to a live link once the sibling lands this cycle (or, if the sibling does not land, leave it plain-text). The two parallel dispatches propose **distinct, non-overlapping** dep-map rows and SUMMARY entries (this one inserts after `nleps_deflated_solve`; the Jacobian-action dispatch should insert its own row — the integrator coordinates the shared `index.md`/`SUMMARY.md` edits).
- **L1>L0 mutation-rotation theme deferred.** The L1>L0 lowering of `nleps_eigenvalue_correction` (the destination-buffer binding for `z`/`z2`, the consume-then-reuse aliasing of `u`/`u2` into `z`/`z2`, the projection-direction lag/normalization, the Armijo damping `α`, and the `AXPBYPCZ`-γ=0 → `axpby` realization) is an abstractor concern, not authored here. It is a thin theme — the atom is a few scalar/BLAS-1 lines — and naturally batches with the other NLEPS-interior L1>L0 themes.
- **No layer-intro refresh needed beyond the cohort count.** The L1 index §Vocabulary-cohort "Firm (17)" header and prose bullet should bump to reflect the new firm operator (and the parallel Jacobian-action one, if it lands) — flagged for the layer-intro-author, not edited here (out of harvester scope). The dep-map row + SUMMARY entry are proposed above.

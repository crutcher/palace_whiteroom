# Slice: divfree

Scope question Q-divfree-leaf. Divergence-free projection: given a Nedelec
(H(curl)) vector field, project onto the discrete divergence-free subspace
(kernel of the discrete weighted divergence). Used by the eigensolver path
(ARPACK / SLEPc / NLEPS) to keep iterates in the physical subspace; the
scope-description attribution to driven/transient solvers is flagged as an
open question (no such call sites are visible in this revision).

## L1

### Defining condition

A `DivFreeSolver` represents the discrete projector `P` onto the
divergence-free subspace of an Nedelec field, defined by

    Gᵀ M (P x) = 0

where

- `G : H1 → Nedelec` is the discrete gradient (the H1→Nedelec interpolator),
- `M : H1 → H1` is the ε-weighted H1 mass-like operator (the material
  permittivity ε supplied by `mat_op`).

### State (constructed once, reused per call)

- `M`: ε-weighted H1 mass/diffusion operator, assembled as a multigrid
  hierarchy over `h1_fespaces`.
- `WeakDiv`: the ε-weighted weak divergence acting Nedelec → H1, partially
  assembled on the finest level. Its sign convention internally absorbs the
  minus from `−∫ ε ∇φ · v` so that the correction step below uses `+Grad·ψ`.
- `Grad`: the H1 → Nedelec discrete gradient interpolator.
- `bdr_tdof_list_M`: essential H1 boundary true-dof list captured at the
  finest level. When the user-supplied boundary list is globally empty, a
  synthetic single-dof list pins φ at one true dof on one rank to remove the
  pure-Neumann nullspace; the effective list is this synthetic one in that
  degenerate case.
- `ksp`: a CG solver preconditioned by BoomerAMG (wrapped in geometric
  multigrid when the H1 hierarchy has more than one level), configured with
  `M` as both operator and preconditioner (the projected H1 system).
- `psi`, `rhs`: H1-sized scratch buffers (scratch_buffer state, not part of
  the projection's external interface).

### Apply (`P x → y`)

Given a Nedelec field `y` (in-place form) or `(x, y)` (out-of-place form
with `y ← x` then in-place apply on `y`):

1. Form the H1 residual:        `rhs ← WeakDiv · y`.
2. Impose essential BC on rhs:  zero entries of `rhs` on `bdr_tdof_list_M`.
3. Solve the projected system:  `M · ψ = rhs`         via `ksp`.
4. Apply the gradient correction: `y ← y + Grad · ψ`.

On exit `y` satisfies the discrete divergence-free condition
`Gᵀ M y = 0` (up to ksp tolerance) on the non-essential dofs.

### Equivalent abstract form (not materialized)

Steps 1–4 are the mixed-form realization of the Helmholtz decomposition
`y = y_divfree + Grad · ψ` where `ψ` solves the weighted Poisson problem

    (Gᵀ M G) ψ = Gᵀ M y.

The triple product `Gᵀ M G` is never materialized: the linear system passed
to `ksp` is `M` itself, with `Gᵀ` realized by `WeakDiv` on the RHS side and
`G` realized by `Grad` on the correction side.

### Complex specialization

For `ComplexVector y`, the same real-valued operators (`WeakDiv`, `M`,
`Grad`) are applied to `Re(y)` and `Im(y)` independently — no cross-coupling
between the components through the projection. The solve step uses a
`ComplexOperator`-typed ksp; `psi` and `rhs` are themselves `ComplexVector`
and the underlying CG path treats the two halves uniformly.

### Mutation pattern

- Single-argument `Mult(y)`: `in_place_overwrite` on `y`; `psi`, `rhs` are
  `scratch_buffer` members.
- Two-argument `Mult(x, y)`: `alias_with_input` viewed as a pure function
  `y = P x`; implemented as `y ← x; Mult(y)`. No aliasing between `x` and
  `y` is assumed.

## Variant axes (absorption status)

- **VecType ∈ {Vector, ComplexVector}.** Parametric absorption: a single
  L1 procedural statement covers both; the only divergence is that complex
  apply runs steps 1 and 4 twice (once per component) with the same
  operators. Step 3 is component-blind via the ComplexOperator ksp.
- **H1 hierarchy depth = 1 vs > 1.** Constructed-operator absorption at the
  preconditioner: `ksp`'s preconditioner is BoomerAMG directly when depth
  is 1, geometric multigrid wrapping BoomerAMG otherwise. The L1 apply
  procedure does not re-inspect this; `ksp.solve(M, rhs) → ψ` is the
  uniform interface.
- **Boundary-dof list empty vs non-empty.** Absorbed at construction by
  redirecting `bdr_tdof_list_M` to a synthetic one-dof list. The L1 apply
  procedure mentions the list once (step 2) and does not re-inspect the
  degeneracy.

## Call sites

- `palace/drivers/eigensolver.cpp` constructs `DivFreeSolver<ComplexVector>`
  (gated on `iodata.solver.linear.divfree_max_it > 0`) and calls
  `divfree->Mult(v0)` to project the initial vector.
- `palace/linalg/arpack.cpp` (and `slepc.cpp`) call `opProj->Mult(y1)`
  inside the eigenvalue-iteration kernel to project candidate eigenvectors.

## Open questions

- Scope description attributes use to driven/transient solvers; only
  eigensolver-path callers are visible. Stale doc, or missing call site
  outside the inspected glob?
- No direct unit test (`test-divfree.cpp` does not exist); coverage is
  indirect via `test/examples/`. A synthetic invariant check (post-Mult,
  `WeakDiv · y` is zero on non-essential dofs to ksp tolerance) would be
  the natural unit-test surface if one were added.
- `WeakDiv` sign-convention claim (that `MixedVectorWeakDivergenceIntegrator`
  encodes the negative-divergence sign, making `+Grad·ψ` the correction)

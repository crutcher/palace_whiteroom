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

## L2 — primitive composition

### Construction (once per solver instance)

Given `mat_op` (material operator carrying ε), `nd_fespace` (Nedelec target
space), `h1_fespaces` (H1 hierarchy), and `bdr_tdof_list` (essential H1
boundary true dofs):

```
construct(mat_op, nd_fespace, h1_fespaces, bdr_tdof_list, tol, max_it):
    M        ← assemble_h1_mass_hierarchy(mat_op, h1_fespaces, bdr_tdof_list)
    WeakDiv  ← assemble_weak_divergence(mat_op, nd_fespace, h1_fespaces.finest())
    Grad     ← assemble_discrete_gradient(h1_fespaces.finest(), nd_fespace)
    bdr_eff  ← pin_one_dof_if_empty(bdr_tdof_list, h1_fespaces.finest())
    pc       ← build_mg_or_amg(M, h1_fespaces)
    ksp      ← cg_solver(operator=M, preconditioner=pc, tol, max_it)
    psi      ← alloc_h1_vector()
    rhs      ← alloc_h1_vector()
    return DivFreeSolver{M, WeakDiv, Grad, bdr_eff, ksp, psi, rhs}
```

The construction-time variants (H1 hierarchy depth → MG vs AMG choice;
empty-boundary degeneracy → synthetic pin) are absorbed inside
`build_mg_or_amg` and `pin_one_dof_if_empty`. The per-apply path below does
not re-inspect them.

### Apply — real path (`P y` in place)

```
apply(self, y: Vector):
    # Step 1: H1 residual rhs ← WeakDiv · y
    rhs ← apply_linop(self.WeakDiv, y)

    # Step 2: enforce essential BC on rhs
    set_subvector_zero(rhs, self.bdr_eff)

    # Step 3: projected H1 solve  M · psi = rhs
    psi ← ksp_solve(self.ksp, rhs)        # M is bound at construction

    # Step 4: gradient correction  y ← y + Grad · psi
    t   ← apply_linop(self.Grad, psi)
    axpy(1.0, t, y)
```

Primitive vocabulary used: `apply_linop`, `set_subvector_zero`,
`ksp_solve`, `axpy`. All are pure functional in their result
(`apply_linop`, `ksp_solve`) or carry an in-place semantics legible from
the primitive's signature (`axpy` on `y`, `set_subvector_zero` on `rhs`).

The two-argument `(x, y)` form is `y ← copy(x); apply(y)` — the copy is
explicit, no silent aliasing.

### Apply — complex specialization

For `y : ComplexVector`, steps 1, 2, 4 act componentwise on `Re(y)` and
`Im(y)` with the same real operators; step 3 is a single
`ksp_solve` on the `ComplexOperator`-typed system whose internal CG
recursion is component-blind:

```
apply(self, y: ComplexVector):
    rhs ← apply_linop(self.WeakDiv, y)        # acts as block-diag Re/Im
    set_subvector_zero(rhs.re, self.bdr_eff)
    set_subvector_zero(rhs.im, self.bdr_eff)
    psi ← ksp_solve(self.ksp, rhs)            # ComplexOperator path
    t   ← apply_linop(self.Grad, psi)
    axpy(1.0, t.re, y.re)
    axpy(1.0, t.im, y.im)
```

The complex apply is a primitive-level unrolling of the real apply over
`{re, im}`; the primitive chain is the same shape. No new primitives are
introduced — `apply_linop` and `axpy` are overloaded on the vector type,
and `ComplexOperator` is the construction-time wrapper that makes
`ksp_solve` component-blind.

### Optimization opacity

The following are **transparent** at L2 and unfolded silently:

- Whether `WeakDiv` is matrix-assembled or apply-only (partial assembly).
- Whether `pc` is a GMG-wrapped BoomerAMG or BoomerAMG directly.
- Whether the `ksp` CG iteration uses re-orthogonalization or not.
- Whether `apply_linop(Grad, psi)` materializes `t` or fuses with `axpy`.

The following are **load-bearing** and preserved as explicit L2 claims:

- The sign convention on `WeakDiv` (so that the correction is `+Grad·ψ`,
  not `−Grad·ψ`). This is an L0/L1 claim that L2 must honor verbatim.
- The `set_subvector_zero(rhs, bdr_eff)` step ordering: it must run
  **after** `apply_linop(WeakDiv, y)` and **before** `ksp_solve`. Reorder
  changes the solution.
- `ksp_solve` returns the converged `ψ`; convergence tolerance is
  baked into the ksp at construction.

## L3 — tensor-field form

The L2 apply is a fixed-length sequence of global tensor-field operations on H1- and Nedelec-sized fields. Each L2 primitive lifts to a global operation; no per-element iteration remains exposed.

### Global apply (real path)

Let `y ∈ V_Nedelec`, `WeakDiv : V_Nedelec → V_H1`, `M : V_H1 → V_H1`,
`Grad : V_H1 → V_Nedelec`, `bdr_eff ⊂ dofs(V_H1)` the effective essential
set, and `K = ksp(M, pc, tol, max_it)` the operator-bound solver. Then
`P : V_Nedelec → V_Nedelec` is

    P(y) = y + Grad · K⁻¹( Z_bdr_eff( WeakDiv · y ) )

where `Z_S : V_H1 → V_H1` is the global zero-on-subset operator
`(Z_S z)_i = 0 if i ∈ S else z_i`, and `K⁻¹` denotes the (approximate)
solve `M ψ = rhs` realized by `ksp_solve(K, rhs)`.

Equivalently, in monadic notation collecting the ksp's internal
iteration count and the projected H1 nullspace pin as effects:

    P(y) = do
        rhs  ← apply_linop WeakDiv y
        rhs' ← set_subvector_zero rhs bdr_eff
        ψ    ← ksp_solve K rhs'
        t    ← apply_linop Grad ψ
        return (y + t)

The four steps are total tensor-field operations: `apply_linop` is a
linear map between finite-dimensional function spaces, `set_subvector_zero`
is the identity-minus-indicator-projector on the boundary subset,
`ksp_solve` is the global linear solve, and `y + t` is the global vector
addition. There is no exposed elementwise loop at this layer.

### Complex specialization

The complex `P : V_Nedelec ⊗ ℂ → V_Nedelec ⊗ ℂ` factors as the same
formula over ℂ-valued fields. Because `WeakDiv`, `M`, and `Grad` are
real-linear, the action on `y = y_re + i·y_im` is block-diagonal:

    P(y_re + i·y_im) = P_re(y_re) + i · P_re(y_im)

where `P_re` is the real apply above. The `ksp_solve` step at L2 invokes
the `ComplexOperator` path; at L3 this is the block-diagonal lift of the
real solve onto `V_H1 ⊗ ℂ`, and the two components are independent.

### Sequential obstruction lives at L2.5, not here

`ksp_solve(K, rhs')` is a global tensor-field operation as a *map* — its
input is `rhs' ∈ V_H1` and its output is `ψ ∈ V_H1`. The CG iteration
internal to `K` is sequential (the standard Krylov sequential
obstruction; see `sequential-obstruction` concept and the `cg` slice).
That obstruction is interior to the `ksp_solve` primitive and does not
leak into the L3 apply. The L3 form of `divfree` is global: the four
steps each lift cleanly, and the only sequential machinery is hidden
inside the named `ksp_solve` primitive whose own L3 obstruction is
recorded in the `cg` slice.

This is a clean L2→L3 lift: no per-step state thread, no residual
sequential axis, no `for`-loop survives at L3.

### Variant absorption at L3

All three L2 variant axes (VecType, H1-depth, empty-boundary) lift
uniformly:

- **VecType.** The complex lift is block-diagonal on `V ⊗ ℂ`; same
  formula.
- **H1-depth.** Absorbed inside `K`; the L3 formula references `K⁻¹`
  abstractly, not the preconditioner choice.
- **Empty-boundary.** Absorbed inside `bdr_eff`; the L3 formula
  references the subset abstractly, not the pin-construction logic.

### Load-bearing claims preserved from L2

- The sign convention on `WeakDiv` is preserved: the formula is
  `y + Grad · ψ`, not `y − Grad · ψ`. This is a property of the
  `WeakDiv` operator's L0 definition (sign baked into
  `MixedVectorWeakDivergenceIntegrator`).
- The step ordering is preserved: `Z_bdr_eff` composes between
  `WeakDiv` and `ksp_solve`. Reordering changes the result.
- `ksp_solve` is an approximate solve; the L3 formula's `K⁻¹` denotes
  the iterative-solver map, not exact inversion. The defining
  condition `Gᵀ M (P y) = 0` holds up to the ksp's convergence
  tolerance on the non-essential dofs.

## L4 — calculus form

The divfree slice is a *projector operator* whose construction allocates internal state once and whose application threads only the simulation state being projected. It expresses cleanly as a `SolveM` computation over a stratified state record per the calculus in [L4 calculus draft](../../design/l4_calculus.md).

### State stratification

```ts
// Internal parameters: constructed once, reused per apply.
type DivFreeParams = {
  M:       LinOp<VH1, VH1>;            // ε-weighted H1 mass (mg-hierarchy interior)
  WeakDiv: LinOp<VNedelec, VH1>;        // sign-absorbed weak divergence
  Grad:    LinOp<VH1, VNedelec>;        // discrete gradient
  bdrEff:  DofSubset<VH1>;              // essential set (synthetic pin if user-empty)
  ksp:     KSP<VH1>;                    // CG bound to M with mg/amg preconditioner
};

// Sim state: the field being projected.
type SimState<V> = { y: V };  // V ∈ {Vector(VNedelec), ComplexVector(VNedelec)}

// Ephemeral intermediates: not part of state, materialized per-apply.
//   rhs : VH1     — H1 residual
//   psi : VH1     — projected H1 solution
//   t   : VNedelec — gradient correction
```

The `psi` and `rhs` scratch buffers visible in the L1 state schema are *internal-parameter storage*, not sim state: they are allocated at construction and reused across applies, but their per-call content is ephemeral and is overwritten on entry. The calculus distinction is that `M`, `WeakDiv`, `Grad`, `bdrEff`, and `ksp` participate in the operator's *identity*; the scratch slots participate only in its *implementation*.

### Construction

```haskell
constructDivFree
  :: MatOp -> NDFESpace -> H1Hierarchy -> DofSubset VH1 -> Tol -> MaxIt
  -> SolveM DivFreeParams
constructDivFree matOp nd h1 bdrUser tol maxIt = do
  m       <- assembleH1MassHierarchy matOp h1 bdrUser
  wd      <- assembleWeakDivergence  matOp nd (finest h1)
  g       <- assembleDiscreteGradient (finest h1) nd
  bdrEff  <- pinOneDofIfEmpty bdrUser (finest h1)
  pc      <- buildMgOrAmg m h1
  ksp     <- cgSolver { op = m, pc = pc, tol = tol, maxIt = maxIt }
  return DivFreeParams { M = m, WeakDiv = wd, Grad = g, bdrEff, ksp }
```

The variant axes (H1-depth → mg-vs-amg, empty boundary → synthetic pin) are absorbed entirely inside `constructDivFree`; the returned `DivFreeParams` is a uniform interface. This is the [constructed-operators](../../concepts/constructed-operators.md) pattern at L4.

### Apply

The per-call form is a pure function over sim state, parameterized by the construction-time `DivFreeParams`:

```haskell
applyDivFree :: DivFreeParams -> SimState V -> SolveM (SimState V)
applyDivFree p s = do
  rhs  <- applyLinOp (WeakDiv p) (y s)
  rhs' <- setSubvectorZero rhs (bdrEff p)
  psi  <- kspSolve (ksp p) rhs'
  t    <- applyLinOp (Grad p) psi
  return s { y = y s + t }
```

The `SolveM` monad threads the ksp's iteration-count and convergence diagnostics as effects; the sim state `s` is updated in a single field. The four steps map one-to-one onto the L3 tensor-field form; the L4 form differs only in making the parameter/state/intermediate stratification explicit and in routing the ksp's internal effects through the monad.

### Complex specialization

The complex apply is the same `applyDivFree` over `SimState (ComplexVector VNedelec)`; the real-linearity of `WeakDiv`, `M`, `Grad` and the block-diagonal `ComplexOperator`-wrapping of `ksp` make the L4 form structurally identical to the real path. No separate calculus expression is needed:

```haskell
applyDivFreeC :: DivFreeParams -> SimState (ComplexVector VNedelec)
                              -> SolveM (SimState (ComplexVector VNedelec))
applyDivFreeC = applyDivFree  -- same function, polymorphic in V
```

The vector-type parameter `V` is absorbed by polymorphism over the field; `applyLinOp`, `setSubvectorZero`, and `kspSolve` are each defined on both `Vector` and `ComplexVector` instances at L4.

### Composition into a driver

The eigensolver-path use is composition over the outer Krylov iteration:

```haskell
eigStep :: EigParams -> DivFreeParams -> SimState V -> SolveM (SimState V)
eigStep eig p s = do
  s'  <- arnoldiOrLanczosStep eig s     -- candidate eigenvector
  s'' <- applyDivFree p s'              -- project back to div-free subspace
  return s''
```

`DivFreeParams` is constructed once at driver setup and threaded as an internal-parameter argument; the per-step monad threads only `SimState`. This is the operator-algebra pattern: the projector composes with other operators via plain function application in the monad.

### Load-bearing claims preserved at L4

- **Sign convention.** `WeakDiv` carries the absorbed minus sign at L0, so the L4 update is `y + t`, not `y - t`. This is a property of the constructed `WeakDiv : LinOp<VNedelec, VH1>` and is not re-derived at L4.
- **Step ordering.** The `do`-notation pins the sequence `WeakDiv → setSubvectorZero → kspSolve → Grad`. The monad's sequential composition makes reordering a type-system-visible change.
- **Approximate solve.** `kspSolve` returns the converged `ψ` up to the construction-time tolerance; the defining condition `Gᵀ M (P y) = 0` holds modulo ksp tolerance on the non-essential dofs, identical to the L3 caveat.
- **Scratch reuse is non-observable.** That `psi` and `rhs` are allocated buffers inside `DivFreeParams` rather than fresh per-call values is an implementation detail of `applyLinOp` and `kspSolve`; at L4 the function is pure over `SimState` and the buffers do not appear in the calculus.

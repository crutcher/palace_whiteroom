---
agent: harvester
invoked_at: 2026-05-31T20:05:00Z
scope: L1 operator floquet-correction + L1>L0 theme floquet-correction-mutation-rotation
status: integrated
integrated_at: 2026-05-31T230000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Applied cycle-036 D1; firm L1 chapter book/src/L1/floquet-correction.md (402 lines) + firm L1>L0 theme book/src/L1-L0/floquet-correction-mutation-rotation.md (525 lines, 4 sub-patterns A/B/C/D) + concept-page nested-constructed-operator-gate firm-instances 2→3 (second three-deep transitive chain floquet→ksp→jacobi-smoother) + L1/index 25→26 Firm count + L1-L0/index dep-map row + SUMMARY.md registration of both new chapters. Path-hygiene auto-fix applied (concepts/nested-constructed-operator-gate.md jacobi-smoother link). Fence-truncation recurrence-3 repaired by per-report-integrator using cycle-024 promoted skill. 3 new OQs filed + 2 closed (floquet-correction-l1-gate-harvest resolved by landing; nested-constructed-operator-gate-second-three-deep-chain-codified closes-on-landing tracker). Counts after: L1 firm 26, L1>L0 firm themes 24, concept firm-instances 3, build clean (~90s), zero build-repairs.
inputs:
  - reports/2026-05-31T141500Z-cross-layer-cross-cutter-floquet-operator-construction-variants/CYCLE.md (c035 D3 sizing)
  - book/src/L1/divfree-projector.md (firm isomorphic template)
  - book/src/L1-L0/divfree-projector-mutation-rotation.md (firm isomorphic template)
  - book/src/concepts/nested-constructed-operator-gate.md (concept page; this harvest is the 3rd firm instance)
  - reference/palace/palace/linalg/floquetcorrection.{hpp,cpp}
  - reference/palace/palace/drivers/{drivensolver,eigensolver}.cpp (4 consumer call sites + 3 construction sites)
  - reference/palace/palace/models/materialoperator.hpp (mat_kx / GetFloquetCross definition)
---

# CYCLE: Formalize floquet-correction at L1 + L1>L0 mutation-rotation theme

## Summary

`FloquetCorrSolver<ComplexVector>` is the **floquet-periodicity B-field correction primitive**: it computes the Raviart-Thomas-space field `y = M_RT⁻¹ · [kp ×] · x` from a Nedelec-space input `x`, where `[kp ×]` is the wave-vector cross-product matrix (a constant assembled from per-attribute material `mat_kx`) and `M_RT` is the RT vector-FE mass operator. Its `AddMult(E, B, 1/ω)` is called at four post-processing sites in driven + eigenmode pipelines to add the floquet correction term `+(1/ω)·[kp×]·E` to the standard `B = −(1/iω)·∇×E` magnetic-flux density, realising the doc-comment `B = −1/(iω) ∇×E + 1/ω kp×E` (the `kp × E` correction is itself the curl of the spatially-modulated bloch-envelope phase, see Section 4 of Joannopoulos et al. 2008 §periodic-media discussion).

This is the **third firm instance** of the [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md) concept (after `eigsolve` 2-gate + `divfree-projector` 1-gate): its closure `F` carries one nested gate (`F.ksp : Solver[F.M_RT]`, a CG + JacobiSmoother solver bound to the RT mass operator), structurally isomorphic to `divfree-projector`'s `P.ksp : Solver[P.M]`. The harvest delivers the firm L1 chapter, the firm L1>L0 mutation-rotation theme, the dep-map row additions, the SUMMARY.md registrations, and a concept-page §Firm-instances upgrade 2→3.

Element-type axis is **complex-only** (`<ComplexVector>` instantiation at `palace/linalg/floquetcorrection.cpp:88`; **no** `<Vector>` instantiation, in deliberate contrast to `DivFreeSolver<VecType>`'s real+complex pair). This is a deliberate scope-out — floquet periodicity is intrinsically a phase-twisted bloch-mode problem and only manifests in complex eigenmode / harmonic-driven pipelines. The L1 signature element-type axis carries this scope-out as a **non-axis** (the parametric `<VecType>` template existing in the class declaration is dead-code in any real-only client).

## Proposed changes

```new:book/src/L1/floquet-correction.md
# floquet-correction

Mutation-lifted floquet-periodicity B-field correction primitive: a pure-functional
linear map `y = floquet_correction(F, x)` that consumes a Nedelec-space (H(curl))
input field `x` and produces a Raviart-Thomas-space (H(div)) output field
`y = M_RT⁻¹ · [kp ×] · x`, where `[kp ×]` is the matrix realising the cross product
with the Floquet wave vector `kp` and `M_RT` is the RT vector-FE mass operator.
The L1 lift of Palace's `FloquetCorrSolver<ComplexVector>` — the dedicated
constructed-operator gate that the driven + eigenmode pipelines invoke to add the
floquet correction term `+(1/ω)·[kp×]·E` to the standard `B = −(1/iω)·∇×E`
post-processing magnetic-flux density when periodic boundary conditions are
imposed.

## Context

`floquet_correction` lifts the `FloquetCorrSolver<VecType>::Mult(const VecType &x,
VecType &y) const` member method (`palace/linalg/floquetcorrection.cpp:73-78`) —
which **writes through the output argument `y`** and **threads a
construction-bound scratch member `rhs`** — to a single pure-functional linear
map over an opaque constructed-operator value. The two-step `Mult` body
sequences `Cross->Mult(x, rhs); ksp->Mult(rhs, y);` over the closure's two
construction-bound operators (`Cross` for the `[kp ×]` cross-product matrix, an
ND→RT mixed-FE mass with the per-attribute wave-vector coefficient; `ksp` for
the RT mass solve). The companion `AddMult(x, y, a)` apply
(`palace/linalg/floquetcorrection.cpp:80-86`) is the apply-and-accumulate
`y += a · (M_RT⁻¹ · [kp ×] · x)` idiom, the **only** apply surface actually
called by Palace's drivers (four sites, see Dependencies). At L1 both `Mult` and
`AddMult` collapse: the destination buffer and the scratch member disappear from
the signature; the apply-and-accumulate is realised at L1 by composition with
[`axpy`](./axpy.md) (`y_new = axpy(a, floquet_correction(F, x), y)`).

`floquet_correction` is a **constructed-operator gate** at L1, in the family of
[`ksp_solve`](./ksp_solve.md), [`eigsolve`](./eigsolve.md),
[`chebyshev-smoother`](./chebyshev-smoother.md),
[`divfree-projector`](./divfree-projector.md), and
[`jacobi-smoother`](./jacobi-smoother.md): its primary argument `F` is a
structured opaque value assembled once at solver setup
(`palace/linalg/floquetcorrection.cpp:20-71`), carrying the RT mass operator
`M_RT`, the cross-product operator `Cross`, and the construction-bound inner
solver `ksp` (CG with JacobiSmoother preconditioner). Unlike `ksp_solve`, the
correction is not parameterised by a right-hand side that varies in kind — it is
a fixed linear map on its single field argument (like `divfree_project`); unlike
`chebyshev-smoother`, the inner RT solve *is* a solve-to-tolerance (a true CG
iteration to the construction-time rel/abs tolerances and iteration cap). The
construction-time integrator assemblies (`VectorFEMassIntegrator` for both `M_RT`
and `Cross`) and the BoomerAMG-free single-level smoother choice
(`JacobiSmoother`, not the divfree-projector's BoomerAMG-or-GMG-wrapping
preconditioner) are absorbed inside `F` and do not appear in the apply signature.

The class is templated on `VecType` but is **instantiated only for
`ComplexVector`** (`palace/linalg/floquetcorrection.cpp:88`, the sole
`template class FloquetCorrSolver<...>;` line). This is a deliberate scope-out:
floquet periodicity is intrinsically a phase-twisted bloch-mode problem (the
wave vector `kp` is a real spatial momentum, but its physical action is on
complex-valued phase-modulated fields), and only the driven + eigenmode
post-processing pipelines (both built on `ComplexVector`) call it. The
parametric `<VecType>` template existing in the class declaration is dead-code
in any hypothetical real-only client — this is **not** a variant axis at the L1
signature (the closure is complex-only). Contrast `divfree-projector` (real and
complex both instantiated) and `jacobi-smoother` (real and complex both
instantiated) — `floquet_correction` is the **first L1 constructed-operator gate
to carry a deliberately-narrowed element-type scope**.

This is the **third firm instance** of the
[`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
shape: `F.ksp : Solver[F.M_RT]` is a constructed-operator sub-field carrying its
own CG iteration, JacobiSmoother preconditioner, tolerance, and iteration cap.
The CG iteration is interior to [`ksp_solve`](./ksp_solve.md) and does not leak
into `floquet_correction` (the concept's cross-layer fidelity rule). Structurally
isomorphic to `divfree-projector`'s `P.ksp : Solver[P.M]`; thinner than
`divfree-projector` (no boundary-zeroing step, no gradient-correction step, no
empty-boundary nullspace pin).

## Signature

    floquet_correction
      :: (F: FloquetCorrector[N_nd, N_rt], x: Field[N_nd, Complex]) -> Field[N_rt, Complex]

    floquet_correction(F, x) = F.M_RT⁻¹ · F.Cross · x
                                where M_RT⁻¹ solves  F.M_RT · y = rhs  via F.ksp
                                and   rhs = F.Cross · x

Shape contract (bunsen-style; named axes):

- `F` — `FloquetCorrector[N_nd, N_rt]` — the constructed corrector value. Bound
  at setup; immutable across calls. `N_nd` is the Nedelec (H(curl)) true-dof
  axis; `N_rt` is the Raviart-Thomas (H(div)) true-dof axis. Carries:
  - `F.M_RT : LinearOperator[N_rt, N_rt]` — the RT vector-FE mass operator,
    assembled from a `VectorFEMassIntegrator` with no spatial coefficient (unit
    weight) on the RT finite-element space
    (`palace/linalg/floquetcorrection.cpp:26-39`). Real and SPD by construction
    (the RT mass matrix is the Gram matrix of the RT shape functions). Read-only.
  - `F.Cross : LinearOperator[N_nd, N_rt]` — the `[kp ×]` cross-product operator
    (Nedelec → RT), from a `VectorFEMassIntegrator` with the per-attribute
    wave-vector cross-product matrix coefficient `mat_kx` as its
    `MaterialPropertyCoefficient` (`palace/linalg/floquetcorrection.cpp:41-57`).
    Read-only. The cross-product matrix is anti-symmetric per attribute: for a
    wave vector `kp = (k₁, k₂, k₃)`, `mat_kx = [[0, −k₃, k₂], [k₃, 0, −k₁], [−k₂, k₁, 0]]`
    (`palace/models/materialoperator.cpp:358` `mat_kx(count).Set(1.0,
    wave_vector_cross);`, where `wave_vector_cross` is the skew-symmetric matrix
    of the wave vector — see `palace/models/materialoperator.hpp:35`
    `mfem::DenseMatrix wave_vector_cross;`).
  - `F.ksp : Solver[F.M_RT]` — a CG solver bound to `F.M_RT` as both operator
    and preconditioner-target, preconditioned by a `JacobiSmoother` (the
    diagonal-only preconditioner — RT mass is well-conditioned so JacobiSmoother
    is sufficient; contrast `divfree-projector` which needs BoomerAMG-or-GMG),
    configured with the construction-time tolerance, machine-epsilon absolute
    tolerance, and iteration cap (`palace/linalg/floquetcorrection.cpp:60-66`).
    The inner constructed-operator gate. See [`ksp_solve`](./ksp_solve.md).
- `x` — `Field[N_nd, Complex]` — the input Nedelec field, complex-valued
  (`ComplexVector`). Read-only at the L1 surface. **Real `Vector` is out of
  scope** at L1 (the class is only instantiated for `ComplexVector` — see
  Context).
- **Returns** — `Field[N_rt, Complex]` — the corrected RT-space field
  `M_RT⁻¹ · [kp ×] · x` up to the `ksp` convergence tolerance. Complex-valued.

`F.M_RT` and `F.Cross` are themselves complex-typed at L0 (`ComplexParOperator`,
`palace/linalg/floquetcorrection.cpp:33,50`). The underlying integrators are
real-valued (the RT mass is real; the wave-vector cross-product matrix `mat_kx`
is real per attribute, `palace/models/materialoperator.cpp:358`); the
`ComplexParOperator` wraps a real `ParOperator` (with `nullptr` imaginary part,
`palace/linalg/floquetcorrection.cpp:33,50`). Algebraically `F.M_RT`/`F.Cross`
act on the real and imaginary parts of `x` independently — the same
block-diagonal real-on-complex action as `divfree-projector`.

MPI is single-rank in scope (per CLAUDE.md "Scope"): the construction reads
`rt_fespace.GetComm()` to bind the CG solver's communicator
(`palace/linalg/floquetcorrection.cpp:60`) and the `JacobiSmoother`'s
(`palace/linalg/floquetcorrection.cpp:65`) — flagged once here and read as the
single-rank equivalent. The `MPI_Comm` does not appear in the L1 signature.

## Semantics

`floquet_correction` realises the **Floquet B-field correction primitive**:
given a Nedelec input field `x` (representing the electric field `E` at a
post-processing call site) and a fixed material wave vector `kp`, it produces the
RT-space field `y` satisfying the FE mass-projected equation `(M_RT · y, v) =
((kp × x), v)` for all test functions `v` in the RT space — i.e. `y` is the RT
projection of the pointwise cross product `kp × x` via the dual pairing.
Equivalently `y = M_RT⁻¹ · [kp ×] · x` where `[kp ×] : Field[N_nd] → Field[N_rt]`
is the mixed-FE mass-weighted cross-product action (a discrete realisation of
the differential operator `v ↦ kp × v` acting between H(curl) and H(div)
spaces). At the four driver call sites the result is **scaled by `1/ω` and
added** to the curl-derived B-field, realising the floquet-corrected magnetic
flux density `B = −1/(iω)·∇×E + 1/ω·[kp×]·E` documented at all four sites
(`palace/drivers/drivensolver.cpp:211,335,467` and
`palace/drivers/eigensolver.cpp:453`, all bearing the inline comment
`B = -1/(iω) ∇ x E + 1/ω kp x E`).

The two-step apply (`palace/linalg/floquetcorrection.cpp:73-78`):

1. **Cross-product action** `rhs ← F.Cross · x` — compute the RT-side
   right-hand side measuring the FE mass-weighted cross product of `x` with the
   wave vector (`palace/linalg/floquetcorrection.cpp:76`).
2. **Projected RT mass solve** `y ← M_RT⁻¹ · rhs`, i.e. solve `F.M_RT · y = rhs`
   via `F.ksp` (`palace/linalg/floquetcorrection.cpp:77`). The system passed to
   `ksp` is `F.M_RT` itself; the CG inner iteration is the standard Krylov
   recurrence interior to [`ksp_solve`](./ksp_solve.md).

This is the **strictly-thinner sibling** of `divfree_project`'s four-step apply:
`floquet_correction` has no boundary-zeroing step (no essential-BC dofs to pin —
the RT mass is full-rank without a Neumann nullspace), no gradient-correction
step (the L1 result is the *direct* mass-solve, not a complement-extraction),
and no empty-boundary synthetic pin. Two ops, in sequence, no in-place
accumulation.

The `AddMult(x, y, a)` companion (`palace/linalg/floquetcorrection.cpp:80-86`)
realises the apply-and-accumulate `y_new = y + a · (M_RT⁻¹ · [kp ×] · x)`. At L1
this is **not a separate operator** — it composes `floquet_correction` with
[`axpy`](./axpy.md): `y_new = axpy(a, floquet_correction(F, x), y)`. The four
driver call sites are all `AddMult(E, B, 1.0 / omega)`, i.e. `B_new = B +
(1/ω) · M_RT⁻¹ · [kp ×] · E`. The L0 `AddMult` body uses the construction-bound
`rhs` scratch member as a *transient destination* for an internal `this->Mult(x,
rhs)` call (re-binding `Mult`'s output argument to the scratch member), then
scales and accumulates onto `y` — an apply-and-accumulate that is fused at L0
for buffer economy but composable at L1 from the firm `floquet_correction` ×
`axpy` pair.

The complex-only scoping means the apply is the same real-valued operator
action applied component-wise to `Re(x)` and `Im(x)` (the `ComplexParOperator`
wrapping a real `ParOperator` with `nullptr` imag at
`palace/linalg/floquetcorrection.cpp:33,50` is the block-diagonal complex
action). There is no cross-coupling between the real and imaginary parts
through the correction.

## Algebraic laws

- **Linearity (complex-linear).** `floquet_correction(F, ·)` is a complex-linear
  map from `Field[N_nd, Complex]` to `Field[N_rt, Complex]`:
  `floquet_correction(F, αu + βv) = α·floquet_correction(F, u) +
  β·floquet_correction(F, v)` for `α, β ∈ ℂ`. The cross-product step
  (`Cross·x`) is complex-linear (a `ComplexParOperator` action with `nullptr`
  imag = block-diagonal real-on-Re-and-Im, which preserves complex linearity
  pointwise — see "Complex-linearity from real-on-block-diagonal" below), and
  the `ksp` solve is complex-linear by the linearity of `M_RT` and CG. Holds
  exactly in exact arithmetic; modulo `ksp` tolerance under the approximate
  solve. Citations: `palace/linalg/floquetcorrection.cpp:33,50`
  (`ComplexParOperator` with `nullptr` imag), `:76-77` (the two-step apply).
- **No-aliasing range invariant.** `Range(floquet_correction(F, ·)) ⊆
  Field[N_rt, Complex]` exactly: every output is in RT space because the second
  step is a solve of `F.M_RT · y = rhs` and `F.M_RT` is RT→RT. The
  cross-product step `Cross` maps Nedelec → RT
  (`palace/linalg/floquetcorrection.cpp:50,55` `nd_fespace, rt_fespace`); the
  mass solve preserves RT.
- **Composition with `axpy` (the `AddMult` law).** `AddMult(F, x, y, a) = axpy(a,
  floquet_correction(F, x), y)` — the L0 `AddMult` body is the L1 composition
  of the firm `floquet_correction` and `axpy` operators
  (`palace/linalg/floquetcorrection.cpp:83-85` — `this->Mult(x, rhs); rhs *= a;
  y += rhs;` is `[axpy(a, this->Mult(x), y)]` with `rhs` the L0 scratch). This
  is the **defining algebraic identity** of `AddMult`: it is not a separate
  operator at L1, only a fused L0 surface for buffer economy. Holds exactly.
- **Composition with `scal` (scaled-output identity).**
  `α · floquet_correction(F, x) = floquet_correction(F, α·x)` for `α ∈ ℂ` — by
  linearity. Holds exactly in exact arithmetic; modulo `ksp` tolerance.
- **Complex-linearity from real-on-block-diagonal.** Because the underlying
  `M_RT` and `Cross` are real-valued and wrapped as `ComplexParOperator(real,
  nullptr)` (`palace/linalg/floquetcorrection.cpp:33,50`), the complex action
  is block-diagonal: `floquet_correction(F, u + i·v) = floquet_correction(F,
  u) + i·floquet_correction(F, v)`. The inner CG solve on the
  `ComplexOperator`-typed system is component-blind (the CG recursion runs on
  complex `Vector`s but each iteration's apply / dot / axpy is block-diagonal).
  No cross-coupling between Re and Im.
- **Non-law (load-bearing): step ordering.** The cross-product step (`F.Cross · x`)
  must compose *before* the mass solve (`F.M_RT⁻¹ · ·`)
  (`palace/linalg/floquetcorrection.cpp:76-77`). Reordering changes the result
  (mass-solving `x` before cross-applying yields a different field). Captured
  here because the two-step body has no reorderable alternative.
- **Non-law (load-bearing): no general inverse — `[kp ×]` is rank-deficient.**
  `floquet_correction(F, ·)` has a nontrivial kernel: any `x ∈ Field[N_nd,
  Complex]` whose pointwise representation is parallel to `kp` (i.e. `kp × x = 0`
  pointwise) maps to zero through `Cross`, hence to zero through
  `floquet_correction`. The cross-product matrix `mat_kx` per attribute is the
  skew-symmetric `3×3` matrix of `kp` (`palace/models/materialoperator.cpp:358`
  `mat_kx(count).Set(1.0, wave_vector_cross)`), which has rank 2 (kernel
  spanned by `kp`). The operator is **not invertible** as a map from
  `Field[N_nd]` to `Field[N_rt]`. This is a property of the physical operator,
  not a defect — the floquet correction is a directional projection that
  removes the component of `E` parallel to `kp`. The L1 form honours this; the
  L1 entry does not promise invertibility.
- **Non-law (semantic): not a projector.** `floquet_correction(F, ·)` is
  **not** idempotent (`(M_RT⁻¹ · [kp ×])² ≠ M_RT⁻¹ · [kp ×]` in general): the
  cross-product is anti-symmetric, mapping back into Nedelec via embedding
  would yield `(M_RT⁻¹ · [kp ×])²` which composes two different-space operations
  through an implicit embedding. The L1 contract is a *linear map*, not a
  projection — the **divfree-projector**'s `P∘P = P` law has no analog here.

## Dependencies

L1-internal:

- [`ksp_solve`](./ksp_solve.md) — the inner RT mass solve `F.M_RT · y = rhs`
  (step 2, `palace/linalg/floquetcorrection.cpp:77`). `floquet_correction`'s
  closure carries a constructed-operator sub-field (`F.ksp : Solver[F.M_RT]`),
  the [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
  shape (the third firm instance). The CG iteration is interior to `ksp_solve`
  and does not leak into `floquet_correction`.
- [`apply_linop`](./apply_linop.md) — the cross-product step `Cross · x` (step
  1, `palace/linalg/floquetcorrection.cpp:76`).
- [`apply_linop`](./apply_linop.md) — the RT mass operator's application is
  internal to `ksp_solve`'s per-step body; surfaced here as the `M_RT` action
  that the inner CG iterates against.
- [`jacobi-smoother`](./jacobi-smoother.md) — the inner CG's preconditioner is
  a `JacobiSmoother` (`palace/linalg/floquetcorrection.cpp:65`). Inside the
  closure, opaque to the apply; the smoother gate is itself a
  constructed-operator sub-field of `F.ksp`'s preconditioner slot.
- [`axpy`](./axpy.md) — the `AddMult` composition `y + a · floquet_correction(F,
  x)`. Not a step of `floquet_correction` itself but the L1 fusion partner that
  realises the only-actually-called L0 apply surface (4 driver call sites all
  use `AddMult`, not `Mult`).

Construction-time dependencies (factory; not in apply path):

- `VectorFEMassIntegrator` (real RT mass, `palace/linalg/floquetcorrection.cpp:29`;
  cross-product mixed mass, `:46`) — concept handled by
  [`constructed-operator-factory`](../concepts/constructed-operator-factory.md).
- `MaterialPropertyCoefficient` carrying `mat_op.GetFloquetCross()` — the
  per-attribute wave-vector cross-product matrix
  (`palace/linalg/floquetcorrection.cpp:42-43`, `palace/models/materialoperator.hpp:103,128`).

Consumer call sites (4 sites, all `AddMult`):

- `palace/drivers/drivensolver.cpp:212` — driven non-PROM frequency-sweep B-field
  correction.
- `palace/drivers/drivensolver.cpp:336` — driven PROM training-frequency-sample
  B-field correction.
- `palace/drivers/drivensolver.cpp:468` — driven PROM evaluation-frequency B-field
  correction.
- `palace/drivers/eigensolver.cpp:454` — eigenmode per-mode B-field correction.

All four are `floquet_corr->AddMult(E, B, 1.0 / omega)` inside `if
(space_op.GetMaterialOp().HasWaveVector())` blocks. Construction sites: 3
(`palace/drivers/drivensolver.cpp:141,292` for the two driven entry points;
`palace/drivers/eigensolver.cpp:240`).

## Status

`firm`.

The **structural decomposition is firm**: every step of the apply is read from a
positive source site (`palace/linalg/floquetcorrection.cpp:73-86`), the
construction is fully read (`palace/linalg/floquetcorrection.cpp:20-71`), and
the linearity, range, composition, and step-ordering laws follow directly from
the source-stated two-step body and the SPD/real properties of the
construction.

**Firm-on-positive-structure precedent** (the `divfree-projector` + `jacobi-smoother`
+ `chebyshev-smoother` + `apply_linop` cohort): every law is a syntactic
operator-algebra identity on a fully-specified positive source. No dedicated
unit test exists (`test/unit/test-floquetcorrection.cpp` is absent; confirmed by
codemap survey — only `test/unit/test-schema.cpp:340-353` validates the
`FloquetWaveVector` JSON shape; the `test/examples/cylinder/floquet`
end-to-end regression at `test/examples/runtests.jl:289-294` covers the
*integration*, not the operator). The test absence does not block `firm` — the
operator's semantics are a fully-read two-step linear map with source-stated
construction; the firm decision matches the `chebyshev-smoother`,
`jacobi-smoother`, and `divfree-projector` precedents (where every law is a
verified-exact syntactic identity on fully-specified source).

The complex-only scope (no `<Vector>` instantiation) is a deliberate scope-out
captured in §Signature `x` element-type note + §Context — not an absence
gate.

## Evidence

- `palace/linalg/floquetcorrection.hpp:28-30` — class doc: "This solver
  calculates a correction for the magnetic flux density field when Floquet
  periodicity is imposed. The correction is the cross product of the Floquet
  wave vector with the electric field." (the primitive's contract).
- `palace/linalg/floquetcorrection.hpp:32-33` — `template <typename VecType> class
  FloquetCorrSolver` (the gate class).
- `palace/linalg/floquetcorrection.hpp:35-39` — `using OperType = std::conditional<…>::type;`
  / `using ScalarType = std::conditional<…>::type;` (the template-resolved
  operator and scalar types).
- `palace/linalg/floquetcorrection.hpp:42-46` — `std::unique_ptr<OperType> M,
  Cross;` and `std::unique_ptr<BaseKspSolver<OperType>> ksp;` (the closure
  fields: `F.M_RT`, `F.Cross`, `F.ksp`).
- `palace/linalg/floquetcorrection.hpp:48-49` — `mutable VecType rhs;` (the
  workspace scratch member; absent from the L1 signature).
- `palace/linalg/floquetcorrection.hpp:52-53` — `FloquetCorrSolver(const
  MaterialOperator &, FiniteElementSpace &nd_fespace, FiniteElementSpace
  &rt_fespace, double tol, int max_it, int print);` (the constructor signature).
- `palace/linalg/floquetcorrection.hpp:55-57` — doc comment: "Given a vector of
  Nedelec dofs for an arbitrary vector field, compute the Raviart-Thomas space
  field y = [kp x] x, where [kp x] is a matrix representing the action of the
  cross product with the Floquet wave vector." (the apply's contract).
- `palace/linalg/floquetcorrection.hpp:58-59` — `void Mult(const VecType &x,
  VecType &y) const;` / `void AddMult(const VecType &x, VecType &y, ScalarType
  a = 1.0) const;` (the apply surface).
- `palace/linalg/floquetcorrection.cpp:20-71` — constructor body (sig `:20-23`,
  body `:24-71`).
- `palace/linalg/floquetcorrection.cpp:26-39` — `M_RT` assembly: `BilinearForm
  a(rt_fespace)` (`:28`), `VectorFEMassIntegrator` (`:29`), `Assemble(skip_zeros)`
  (`:30`), `ComplexParOperator` wrap with `nullptr` imag (`:33`).
- `palace/linalg/floquetcorrection.cpp:41-57` — `Cross` assembly:
  `MaterialPropertyCoefficient` (`:42`),
  `AddCoefficient(GetAttributeToMaterial(), GetFloquetCross(), 1.0)` (`:43`),
  `BilinearForm a(nd_fespace, rt_fespace)` (`:45`), `VectorFEMassIntegrator(f)`
  (`:46`), `Assemble(skip_zeros)` (`:47`), `ComplexParOperator` wrap (`:50`).
- `palace/linalg/floquetcorrection.cpp:60-66` — `ksp` setup: `CgSolver`
  (`:60`), `SetInitialGuess(0)` (`:61`), `SetRelTol(tol)` (`:62`),
  `SetAbsTol(epsilon())` (`:63`), `SetMaxIter(max_it)` (`:64`),
  `JacobiSmoother` preconditioner (`:65`), `BaseKspSolver` wrap (`:66`).
- `palace/linalg/floquetcorrection.cpp:67` — `ksp->SetOperators(*M, *M)` (the
  operator and preconditioner-target are both `M_RT`).
- `palace/linalg/floquetcorrection.cpp:69-70` — `rhs.SetSize(rt_fespace.GetTrueVSize());
  rhs.UseDevice(true);` (the scratch buffer sizing).
- `palace/linalg/floquetcorrection.cpp:73-78` — `Mult(const VecType &x, VecType
  &y) const` body: `Cross->Mult(x, rhs); ksp->Mult(rhs, y);` (the two-step apply).
- `palace/linalg/floquetcorrection.cpp:80-86` — `AddMult(const VecType &x,
  VecType &y, ScalarType a) const` body: `this->Mult(x, rhs); rhs *= a; y += rhs;`
  (the apply-and-accumulate composition).
- `palace/linalg/floquetcorrection.cpp:88` — `template class
  FloquetCorrSolver<ComplexVector>;` (the **sole** instantiation; the
  complex-only scope-out).
- `palace/models/materialoperator.hpp:103` —
  `auto GetFloquetCross(int attr) const { return Wrap(mat_kx, attr); }` (the
  per-attribute wave-vector cross-product matrix accessor).
- `palace/models/materialoperator.hpp:128` —
  `const auto &GetFloquetCross() const { return mat_kx; }` (the all-attributes
  accessor used by `MaterialPropertyCoefficient::AddCoefficient`).
- `palace/models/materialoperator.cpp:358` — `mat_kx(count).Set(1.0,
  wave_vector_cross);` (the per-attribute initialisation; `wave_vector_cross` is
  the `3×3` skew-symmetric matrix of `kp`).
- `palace/models/materialoperator.hpp:136` — `bool HasWaveVector() const {
  return has_wave_attr; }` (the gating predicate at the driver call sites).
- `palace/drivers/drivensolver.cpp:138-143` — first construction site
  (driven non-PROM frequency sweep).
- `palace/drivers/drivensolver.cpp:208-213` — first AddMult call site (with the
  load-bearing doc comment `B = -1/(iω) ∇ x E + 1/ω kp x E` at `:211`).
- `palace/drivers/drivensolver.cpp:289-294` — second construction site (driven
  PROM training).
- `palace/drivers/drivensolver.cpp:332-337` — second AddMult call site (with the
  doc comment at `:335`).
- `palace/drivers/drivensolver.cpp:464-469` — third AddMult call site (driven
  PROM evaluation; doc comment at `:467`).
- `palace/drivers/eigensolver.cpp:237-243` — eigenmode construction site.
- `palace/drivers/eigensolver.cpp:450-455` — eigenmode AddMult call site (with
  the doc comment at `:453`).
- `test/unit/test-schema.cpp:340-353` — JSON schema validation for
  `FloquetWaveVector` (the only floquet-related unit test in `test/unit/`).
- `test/examples/runtests.jl:289-294` — `cylinder/floquet` end-to-end regression
  example.
```

```new:book/src/L1-L0/floquet-correction-mutation-rotation.md
# floquet-correction-mutation-rotation

The mutation rotation for the Floquet B-field correction apply. Lowers the pure
L1 form [`floquet_correction`](../L1/floquet-correction.md) —
`y = floquet_correction(F, x) = F.M_RT⁻¹ · F.Cross · x` — into Palace's L0
`FloquetCorrSolver<ComplexVector>::Mult(const VecType &x, VecType &y)` member
method, plus the apply-and-accumulate `AddMult(const VecType &x, VecType &y,
ScalarType a)` member method and the construction-bound `FloquetCorrSolver(...)`
constructor that materialises the L1 closure fields. Narrated forward: the L1
pure out-of-place linear map dissolves into the L0 output-argument mutation
idiom (writes through `y`, scribbles construction-bound scratch member `rhs`)
over a constructed-operator value whose fields (`M`, `Cross`, `ksp`) are
assembled once at solver setup.

## Slug

`floquet-correction-mutation-rotation`

## L1 form (LHS)

The pure-functional Floquet correction consumes the prior `x` as a value and
produces a fresh RT-space field over an opaque constructed corrector `F`
(`FloquetCorrector[N_nd, N_rt]`, carrying `(M_RT, Cross, ksp)`):

    y = floquet_correction(F, x)
      = F.M_RT⁻¹ · F.Cross · x
        where M_RT⁻¹ solves  F.M_RT · y = rhs  via F.ksp
        and   rhs = F.Cross · x

The two composed steps at L1 (see
[`L1/floquet-correction`](../L1/floquet-correction.md) §Semantics):

1. `rhs = F.Cross · x`                — cross-product action (Nedelec → RT)
2. `y   = M_RT⁻¹ · rhs`, i.e. solve `F.M_RT · y = rhs` via `F.ksp`

The apply-and-accumulate companion at L1 is **not a separate operator** — it is
the firm composition with [`axpy`](../L1/axpy.md):

    y_new = y + a · floquet_correction(F, x) = axpy(a, floquet_correction(F, x), y)

At L1 there is **no destination buffer** (the correction returns a value), **no
scratch-buffer ownership** (`rhs` is absent from the signature), and **no
runtime element-type tag** — the closure is complex-only (only `<ComplexVector>`
is instantiated at L0; see Sub-pattern D).

## L0 form (RHS)

The rewrite splits into a **construction site** (the constructor that
materialises the closure fields), an **application site** (the `Mult` family
that realises the per-call correction by in-place mutation), an
**apply-and-accumulate site** (the `AddMult` family that fuses scaling and
accumulation onto the destination), and an **element-type scope-out**
(`<ComplexVector>` only). One L0 class (`FloquetCorrSolver<VecType>`) carries
the parametric `<VecType>` template parameter but instantiates only for
`ComplexVector` (sub-pattern D).

### Sub-pattern A — application via out-of-place `Mult(const VecType &x, VecType &y)`

    template <typename VecType>
    void FloquetCorrSolver<VecType>::Mult(const VecType &x, VecType &y) const
    {
      Cross->Mult(x, rhs);   // step 1: rhs = Cross · x
      ksp->Mult(rhs, y);     // step 2: M_RT · y = rhs (CG to tolerance)
    }

The L1 *value* `y` is the L0 `y` after `Mult(x, y)` returns. The crucial L0
facts the L1 form erases:

- **Destination-arg mutation.** `y` is the output argument; `ksp->Mult(rhs, y)`
  writes through it. The L1 form takes `x` as a value and returns a fresh `y`.
  Same output-arg idiom as
  [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md): the
  destination is named in the call's argument list, not on the LHS.
- **One scribbled scratch member.** `rhs` (the RT-side cross-product result) is
  a `mutable VecType` member (`palace/linalg/floquetcorrection.hpp:49`), sized
  once in the constructor (`palace/linalg/floquetcorrection.cpp:69-70`),
  written every call, carrying no value across calls. At L1 it vanishes — the
  correction is a single value-producing action. **Thinner than
  `divfree-projector`'s two-scratch (`psi`, `rhs`)** — only one buffer because
  no boundary-zeroing intermediate and no gradient-correction post-step are
  needed.
- **Construction-bound operators.** `Cross`, `ksp`, `M` are `std::unique_ptr`
  member fields set once in the constructor and read-only across calls; they
  are `F`'s captured closure fields at L1.
- **Inner solve is itself a constructed-operator gate.** `ksp->Mult(rhs, y)`
  (step 2) is the [`ksp_solve`](../L1/ksp_solve.md) inner RT mass solve. Its CG
  iteration is interior to `ksp_solve` and does not leak into this theme; here
  it is the opaque `M_RT⁻¹` action — the
  [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
  fidelity rule (the inner gate's iteration stays interior to its own lowering
  theme). This theme's closure carries another constructed-operator gate as a
  sub-field (`F.ksp : Solver[F.M_RT]`) — the **third firm instance** of the
  nested-gate shape (after `eigsolve-mutation-rotation`'s two-gate
  `E.linear`/`E.projector` carrying and
  `divfree-projector-mutation-rotation`'s one-gate `P.ksp` carrying). The
  `F.ksp` itself carries a `JacobiSmoother` preconditioner
  (`palace/linalg/floquetcorrection.cpp:65`) — which by
  [`solver-as-operator`](../concepts/solver-as-operator.md) is also a
  constructed-operator gate, so the floquet-corrector→ksp→jacobi-smoother chain
  is a transitive three-level nesting (parallel to the eigsolve→divfree→ksp
  chain documented in
  [`book/src/concepts/nested-constructed-operator-gate.md:91-102`](../concepts/nested-constructed-operator-gate.md)).
  See Open questions / caveats.

Justification kind: **structural** — re-bind the L1 output value into the L0
output destination buffer `y`; erase the scratch member `rhs`; the operators
are the construction-bound closure fields. The apply maps the two L1 composed
steps 1:1 onto the two L0 statement lines.

Citations:

- `palace/linalg/floquetcorrection.cpp:73-78` — `Mult(const VecType &x, VecType
  &y) const` (signature `:73-74`, opening brace `:75`, step 1 `:76`, step 2
  `:77`, close brace `:78`).
- `palace/linalg/floquetcorrection.hpp:49` — `mutable VecType rhs;` (the
  scratch member).
- `palace/linalg/floquetcorrection.hpp:58` — `void Mult(const VecType &x,
  VecType &y) const;` (the apply decl with `x` const-ref input and `y` ref
  output).

### Sub-pattern B — apply-and-accumulate via `AddMult(const VecType &x, VecType &y, ScalarType a)`

    template <typename VecType>
    void FloquetCorrSolver<VecType>::AddMult(const VecType &x, VecType &y, ScalarType a) const
    {
      this->Mult(x, rhs);   // y_arg = rhs (the scratch member, aliasing rebind)
      rhs *= a;             // scratch scaled in place
      y += rhs;             // accumulate onto destination
    }

The L0 `AddMult` body realises `y_new = y + a · (M_RT⁻¹ · [kp ×] · x)`. The L1
equivalent decomposes into the firm
[`floquet_correction`](../L1/floquet-correction.md) + [`axpy`](../L1/axpy.md)
pair:

    y_new = axpy(a, floquet_correction(F, x), y)

i.e. AddMult is NOT a separate L1 operator. The L0 body fuses the two L1
operators for buffer economy: rather than allocating a fresh RT-space result of
`Mult(x, ·)`, the body re-binds `Mult`'s output argument to the construction-bound
`rhs` scratch member (`this->Mult(x, rhs)` — *the same `rhs` that `Mult`'s body
uses as its step-1 cross-product intermediate*), then performs an in-place
`scal`-style scale (`rhs *= a`) and an `axpy`-style accumulate (`y += rhs`). The
L1 fusion is reversed at L1 into the two firm operators.

Crucial L0 fact the L1 fusion erases: **the inner `this->Mult(x, rhs)` call binds
`Mult`'s output destination to the same scratch member `rhs` that `Mult`'s body
uses as its step-1 cross-product intermediate**. Inside the nested call, the
sequence is `Cross->Mult(x, this->rhs); this->ksp->Mult(this->rhs, y_arg =
this->rhs);` — i.e. `ksp->Mult(b, x)` with `b == x` (the input RHS and the
output buffer are the same `VecType`). This implies a **load-bearing aliasing
applicability condition** (see Applicability conditions): the inner CG solver
must accept input/output aliasing on its argument vectors. Palace's
`BaseKspSolver::Mult(const VecType &x, VecType &y) const`
(`palace/linalg/ksp.cpp:297`) accepts this aliasing — the CG iteration body
reads `x` once into a residual register and thereafter writes `y` and internal
workspace independently. This aliasing is the source of the four-byte buffer
economy that the AddMult fusion exists for; reversing the fusion at L1 requires
the same applicability guarantee.

Justification kind: **algebraic** (the AddMult-into-axpy unfolding is the
`axpy(α, a, b) = a·α + b` definition with `a = floquet_correction(F, x)` and
`α = a` *plus* the structural buffer-economy claim that the L0 fusion uses the
scratch member as transient scaled-output buffer).

Citations:

- `palace/linalg/floquetcorrection.cpp:80-86` — `AddMult(const VecType &x,
  VecType &y, ScalarType a) const` (signature `:80-81`, body `:82-86` with
  `this->Mult(x, rhs)` at `:83`, `rhs *= a` at `:84`, `y += rhs` at `:85`,
  close brace `:86`).
- `palace/linalg/floquetcorrection.hpp:59` — `void AddMult(const VecType &x,
  VecType &y, ScalarType a = 1.0) const;` (decl; default `a = 1.0` makes the
  no-scale apply-and-accumulate `Mult-and-add`).
- `palace/linalg/ksp.cpp:297` — `BaseKspSolver<OperType>::Mult(const VecType
  &x, VecType &y) const` (the inner ksp whose aliasing tolerance is required;
  the AddMult fusion depends on the ksp accepting `x == y` aliasing).

### Sub-pattern C — construction site: closure-field materialisation

The L1 closure `F = FloquetCorrector[N_nd, N_rt]` is the value the constructor
materialises (`palace/linalg/floquetcorrection.cpp:20-71`):

- `F.M_RT` ← RT vector-FE mass operator: a `BilinearForm` over the RT space
  with a coefficient-free `VectorFEMassIntegrator`, assembled with
  `skip_zeros = false`, wrapped as `ComplexParOperator` with `nullptr` imaginary
  part (`palace/linalg/floquetcorrection.cpp:26-39`). Real and SPD by
  construction (the RT mass matrix is the Gram matrix of the RT shape
  functions).
- `F.Cross` ← `[kp ×]` mixed mass operator (Nedelec → RT): a `BilinearForm`
  with two FE spaces (`nd_fespace, rt_fespace`) carrying a
  `MaterialPropertyCoefficient` constructed from
  `mat_op.GetAttributeToMaterial()` × `mat_op.GetFloquetCross()` (the
  per-attribute wave-vector cross-product matrix `mat_kx`) with a unit weight
  `1.0`, integrated by `VectorFEMassIntegrator`, assembled with
  `skip_zeros = false`, wrapped as `ComplexParOperator` with `nullptr`
  imaginary part and the trailing `false` (the asymmetric-trial-test-spaces
  hint) (`palace/linalg/floquetcorrection.cpp:41-57`).
- `F.ksp` ← a CG solver bound to `F.M_RT` as both operator and preconditioner
  target (`SetOperators(*M, *M)`), preconditioned by a `JacobiSmoother` (no
  BoomerAMG, no GMG — RT mass is well-conditioned so the diagonal-only Jacobi
  is sufficient), with the construction-time rel-tol, abs-tol = machine
  epsilon, and iteration cap (`palace/linalg/floquetcorrection.cpp:60-67`). The
  inner constructed-operator gate; see [`ksp_solve`](../L1/ksp_solve.md). **Key
  contrast with `divfree-projector`'s ksp setup**: divfree uses BoomerAMG (or
  GMG-wrapping-BoomerAMG) preconditioner; floquet uses JacobiSmoother. Both are
  CG; both bind operator-and-preconditioner-target to the same `M`. Captured
  at L1 as different `Solver[...]` closures with different per-instance content.
- `F` scratch ← `rhs`, sized to RT true-vsize and marked device-resident
  (`palace/linalg/floquetcorrection.cpp:69-70`). The L0 scratch member erased at
  L1 (sub-pattern A).

Justification kind: **structural** — the constructor is the
constructed-operator-gate construction step (same family as the
[`ksp-solve`](./ksp-solve-mutation-rotation.md) /
[`chebyshev-smoother`](./chebyshev-smoother-mutation-rotation.md) /
[`eigsolve`](./eigsolve-mutation-rotation.md) /
[`divfree-projector`](./divfree-projector-mutation-rotation.md) /
[`jacobi-smoother`](./jacobi-smoother-mutation-rotation.md) setup sites): the
L1 closure `F` is a pure function of the setup inputs `(mat_op, nd_fespace,
rt_fespace, tol, max_it, print)` modulo the opaque assembly/preconditioner-setup
machinery, which is below this theme's resolution (it is the
[`constructed-operator-factory`](../concepts/constructed-operator-factory.md)
concern).

Citations:

- `palace/linalg/floquetcorrection.cpp:20-23` — ctor signature.
- `palace/linalg/floquetcorrection.cpp:26-39` — `M_RT` assembly: comment
  `:25-26`, `BilinearForm a(rt_fespace)` `:28`, `VectorFEMassIntegrator` `:29`,
  `Assemble(skip_zeros)` `:30`, `ComplexParOperator` wrap with `nullptr` imag
  `:33`, real fallback `ParOperator` wrap `:37` (dead-code under the
  `<ComplexVector>`-only instantiation).
- `palace/linalg/floquetcorrection.cpp:41-57` — `Cross` assembly:
  `MaterialPropertyCoefficient f(mat_op.MaxCeedAttribute())` `:42`,
  `AddCoefficient(...)` with `mat_op.GetFloquetCross()` `:43`,
  `BilinearForm a(nd_fespace, rt_fespace)` `:45`, `VectorFEMassIntegrator(f)`
  `:46`, `Assemble(skip_zeros)` `:47`, `ComplexParOperator` wrap `:50-51`, real
  fallback `ParOperator` wrap `:55` (dead-code).
- `palace/linalg/floquetcorrection.cpp:60-66` — `ksp` setup: `CgSolver`
  constructor `:60`, `SetInitialGuess(0)` `:61`, `SetRelTol(tol)` `:62`,
  `SetAbsTol(epsilon())` `:63`, `SetMaxIter(max_it)` `:64`, `JacobiSmoother`
  preconditioner `:65`, `BaseKspSolver` wrap `:66`.
- `palace/linalg/floquetcorrection.cpp:67` — `ksp->SetOperators(*M, *M)`
  (operator and preconditioner-target both bound to `M_RT`).
- `palace/linalg/floquetcorrection.cpp:69-70` — `rhs.SetSize(rt_fespace.
  GetTrueVSize()); rhs.UseDevice(true);` (the scratch-member sizing).
- `palace/models/materialoperator.hpp:103,128` — the
  `GetFloquetCross(int attr)` per-attribute accessor + `GetFloquetCross()`
  all-attributes accessor.
- `palace/models/materialoperator.cpp:358` — `mat_kx(count).Set(1.0,
  wave_vector_cross);` (the per-attribute initialisation; `wave_vector_cross`
  is the skew-symmetric `3×3` matrix of `kp`).

### Sub-pattern D — element-type scope-out (`<ComplexVector>` only)

`FloquetCorrSolver<VecType>` is parametrically templated on `VecType` but
**instantiated only for `ComplexVector`** (`palace/linalg/floquetcorrection.cpp:88`):

    template class FloquetCorrSolver<ComplexVector>;

There is no `template class FloquetCorrSolver<Vector>;` line. This is a
deliberate scope-out: floquet periodicity is intrinsically a complex-valued
problem (the wave vector `kp` is a real spatial momentum, but its physical
action manifests on phase-modulated complex bloch fields), and only the driven
+ eigenmode pipelines call it — both pipelines work in `ComplexVector`. The
`if constexpr (std::is_same<OperType, ComplexOperator>::value)` branches in the
constructor (`palace/linalg/floquetcorrection.cpp:31,48`) carry both `complex`
and `real` paths textually, but only the complex path is reachable under the
`<ComplexVector>` instantiation.

The L1 signature reflects this directly: `x` and the result are both
`Field[N_nd, Complex]` / `Field[N_rt, Complex]`; there is no real-only mode.
**Contrast with `divfree-projector`** (real *and* complex both instantiated,
`palace/linalg/divfree.cpp:189-190`) and with `jacobi-smoother` (real *and*
complex both instantiated, `palace/linalg/jacobi.cpp` instantiations). The
`floquet_correction` is the **first L1 constructed-operator gate with a
deliberately-narrowed element-type scope**.

Justification kind: **structural** — the `<VecType>` template parameter is
parametric but the single L0 explicit instantiation pins the element-type
scope. The L1 form has one action; the parametric template is dead-code in any
hypothetical real-only client. There is no real-mode runtime branch to handle.

Citations:

- `palace/linalg/floquetcorrection.cpp:88` — `template class
  FloquetCorrSolver<ComplexVector>;` (the **sole** instantiation).
- `palace/linalg/floquetcorrection.cpp:31` — `if constexpr
  (std::is_same<OperType, ComplexOperator>::value)` (the complex-branch of the
  `M_RT` assembly; the reachable path).
- `palace/linalg/floquetcorrection.cpp:35-38` — `else { ... ParOperator ... }`
  (the real-branch dead-code).
- `palace/linalg/floquetcorrection.cpp:48` — second `if constexpr` (the
  complex-branch of the `Cross` assembly).
- `palace/linalg/floquetcorrection.cpp:53-56` — `else { ... ParOperator ... }`
  (the real-branch dead-code).
- `palace/drivers/drivensolver.cpp:138`, `:289`,
  `palace/drivers/eigensolver.cpp:237` — all three construction sites declare
  `std::unique_ptr<FloquetCorrSolver<ComplexVector>>` (no `<Vector>` use anywhere
  in the call-site cohort).

## Applicability conditions

The rewrite preserves semantics when:

1. **No aliasing between `x`, `y`, `rhs` at the `Mult` call.** `Mult(x, y)`
   reads `x` (step 1) and writes `rhs` (step 1) and writes `y` (step 2). The L1
   form takes the pre-call `x` as a value and owns no scratch, so the lowering
   must guarantee `rhs` is a distinct buffer from `x` and from `y`. Palace
   allocates `rhs` as a construction-bound member distinct from the caller's
   `x` and `y`. Inherited applicability-condition shape from
   [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md).
2. **Inner ksp accepts input/output aliasing.** The `AddMult` body's nested
   `this->Mult(x, rhs)` call binds `Mult`'s output argument to the scratch
   member, and `Mult`'s step-2 body `ksp->Mult(rhs, y_arg = rhs)` therefore
   calls the inner ksp with `b == x` (input RHS and output destination aliased
   to the same buffer). The inner `BaseKspSolver::Mult`
   (`palace/linalg/ksp.cpp:297`) tolerates this aliasing — the CG iteration
   reads `x` once into a residual register and thereafter writes `y` and
   internal workspace independently. **A lowering that re-derives `ksp->Mult`
   without input/output aliasing tolerance breaks the AddMult fusion.** This
   condition is **specific to this theme** (the divfree-projector AddMult-free
   apply does not have this concern).
3. **No observer of prior `y` after the in-place call.** `Mult(x, y)` writes
   `y` (the destination is overwritten with the new value); `AddMult` reads
   `y` (the destination is accumulated onto with the correction). If a
   downstream op reads `y_old` after `Mult`, the in-place form is invalid; at
   L1 `y_old` is still in scope as a separate value. Upheld at all four
   `AddMult` call sites by lexical sequencing (the `AddMult` follows a `B *=
   −1.0/(1i*omega)` rescale that already finished writing to `B`, then `AddMult`
   adds to `B` once and `B` is consumed by the next post-processing step).
4. **Closure immutability across calls.** `F` (`M_RT`, `Cross`, `ksp`) is set
   once in the constructor and read-only across `Mult`/`AddMult` calls. There
   is no per-call control input — the L1 form is a fixed linear map on its
   single field argument.
5. **Step ordering is load-bearing.** The sequence `Cross → ksp` must not be
   reordered: cross-product before mass-solve is the only meaningful sequence
   (`Mult` body lines `:76-77`).
6. **Element-type conformance (single).** Only `<ComplexVector>` is
   instantiated (`palace/linalg/floquetcorrection.cpp:88`). A lowering that
   tries to instantiate `<Vector>` (a hypothetical real-only client) hits the
   constructor's `if constexpr` real branches (which exist as dead-code at
   `:35-38, :53-56`) but cannot proceed — there are no real-typed driver call
   sites in Palace; the construction-site declarations at
   `palace/drivers/drivensolver.cpp:138,289` and
   `palace/drivers/eigensolver.cpp:237` all bind `<ComplexVector>`. **A
   lowering instantiating `<Vector>` is out-of-evidence; it requires a positive
   driver site.**
7. **Wave vector is real-valued and spatially constant per material.** The
   `mat_op.GetFloquetCross()` returns a per-attribute `3×3` skew-symmetric
   matrix of the wave vector (`palace/models/materialoperator.cpp:358`); the
   wave vector itself is a real `mfem::Vector` (the `wave_vector_cross` member
   is `mfem::DenseMatrix`, `palace/models/materialoperator.hpp:35`). The L1
   form treats `[kp ×]` as a fixed linear map; if the wave vector becomes
   complex-valued or spatially varying *within* a material attribute, the
   integrator construction would have to change.
8. **Single-machine scope.** The `MPI_Comm` machinery in the ksp setup
   (`rt_fespace.GetComm()`, `palace/linalg/floquetcorrection.cpp:60,65`) is
   read as its single-rank equivalent (MPI distribution out of scope, flagged
   once). The `MPI_Comm` does not appear in the L1 signature.

## Justification kind

- **Sub-pattern A** (out-of-place apply) — `structural`. Output-arg `y` re-bind +
  scratch `rhs` erasure; 1:1 step mapping.
- **Sub-pattern B** (apply-and-accumulate) — `algebraic` (AddMult unfolds into
  `axpy ∘ floquet_correction`) + `structural` (the L0 buffer economy uses the
  scratch as transient scaled-output buffer; the aliasing applicability is
  load-bearing).
- **Sub-pattern C** (construction) — `structural`. Constructed-operator-gate
  closure materialisation; pure-of-inputs modulo opaque assembly/preconditioner
  setup.
- **Sub-pattern D** (element-type scope-out) — `structural`. `<ComplexVector>`-only
  single explicit instantiation; the parametric template is dead-code in any
  hypothetical real-only client.

The theme as a whole is `structural` with one algebraic sub-rule (the AddMult-as-axpy
identity in B). A `lowering-verifier` audit in a later cycle should confirm
all four sub-patterns match the L0 corpus exhaustively (the `<ComplexVector>`
sole instantiation, the Mult + AddMult entry points, all four AddMult call
sites, all three construction sites).

## Speculative L1 operators

None. The L1 anchor [`L1/floquet-correction`](../L1/floquet-correction.md) is
firm, and all its sub-dependencies are firm L1 operators / firm concepts:
[`apply_linop`](../L1/apply_linop.md) (the `Cross · x` step),
[`ksp_solve`](../L1/ksp_solve.md) (the inner RT mass solve),
[`jacobi-smoother`](../L1/jacobi-smoother.md) (the inner CG preconditioner),
[`axpy`](../L1/axpy.md) (the AddMult-as-axpy composition).

This theme proposes no new vocabulary.

## Verified-against

L0 evidence ranges (all verified via `citecheck` this cycle, 2026-05-31):

- `palace/linalg/floquetcorrection.cpp:20-71` — constructor body (sig `:20-23`,
  M assembly `:26-39`, Cross assembly `:41-57`, ksp+JacobiSmoother
  setup+SetOperators `:60-67`, scratch sizing `:69-70`, close brace `:71`).
- `palace/linalg/floquetcorrection.cpp:73-78` — `Mult(const VecType &x,
  VecType &y) const` two-step body.
- `palace/linalg/floquetcorrection.cpp:80-86` — `AddMult(const VecType &x,
  VecType &y, ScalarType a) const` apply-and-accumulate body.
- `palace/linalg/floquetcorrection.cpp:88` — `template class
  FloquetCorrSolver<ComplexVector>;` (sole instantiation).
- `palace/linalg/floquetcorrection.hpp:32-60` — class declaration.
- `palace/linalg/floquetcorrection.hpp:42-43` — `std::unique_ptr<OperType> M,
  Cross;`.
- `palace/linalg/floquetcorrection.hpp:46` — `std::unique_ptr<BaseKspSolver<OperType>>
  ksp;`.
- `palace/linalg/floquetcorrection.hpp:49` — `mutable VecType rhs;`.
- `palace/linalg/floquetcorrection.hpp:52-53` — constructor decl.
- `palace/linalg/floquetcorrection.hpp:58-59` — `Mult` and `AddMult` decls.
- `palace/linalg/ksp.cpp:297` — `BaseKspSolver<OperType>::Mult` (the inner ksp
  whose aliasing tolerance the AddMult fusion requires).
- `palace/models/materialoperator.hpp:103,128` — `GetFloquetCross` accessors.
- `palace/models/materialoperator.cpp:358` — `mat_kx(count).Set(1.0,
  wave_vector_cross)`.
- `palace/drivers/drivensolver.cpp:138-143` — first construction site.
- `palace/drivers/drivensolver.cpp:208-213` — first AddMult call site.
- `palace/drivers/drivensolver.cpp:289-294` — second construction site.
- `palace/drivers/drivensolver.cpp:332-337` — second AddMult call site.
- `palace/drivers/drivensolver.cpp:464-469` — third AddMult call site.
- `palace/drivers/eigensolver.cpp:237-243` — eigenmode construction site.
- `palace/drivers/eigensolver.cpp:450-455` — eigenmode AddMult call site.
- `test/unit/test-schema.cpp:340-353` — JSON schema validation for
  `FloquetWaveVector`.
- `test/examples/runtests.jl:289-294` — `cylinder/floquet` end-to-end
  regression example.

L1 anchor:

- `book/src/L1/floquet-correction.md` — the firm L1 operator all four
  sub-patterns lower from.

## Status

`firm`.

Every sub-pattern reads from a positive Palace source site verified via
`citecheck` this cycle:

- the out-of-place output-arg apply with scratch-member threading (A,
  `palace/linalg/floquetcorrection.cpp:73-78`),
- the apply-and-accumulate AddMult-as-axpy fusion (B,
  `palace/linalg/floquetcorrection.cpp:80-86`),
- the constructed-operator-gate closure materialisation (C,
  `palace/linalg/floquetcorrection.cpp:20-71`),
- the `<ComplexVector>`-only element-type scope-out (D,
  `palace/linalg/floquetcorrection.cpp:88`).

The single load-bearing algebraic sub-rule — the AddMult-as-axpy unfolding —
follows from the algebraic identity `axpy(α, a, b) = α·a + b` applied to the
`(α=a, a=floquet_correction(F, x), b=y)` instantiation visible in the L0 body
lines `:83-85`.

**No partly-constructive caveat applies.** This theme has a positive source
site for every step, including the AddMult fusion's load-bearing aliasing
applicability (`palace/linalg/ksp.cpp:297` + the L0 calling sequence). The L1
anchor is firm-on-positive-structure (the `divfree-projector` / `jacobi-smoother`
/ `chebyshev-smoother` precedent), so this theme is firm at birth.

A `lowering-verifier` exhaustiveness audit (`<ComplexVector>` sole
instantiation × `Mult` + `AddMult` entry points × all 4 driver call sites × all
3 construction sites) is the standard follow-up, not a status reduction.

## Open questions / caveats

- **Theme's closure carries a transitively-three-deep nested gate
  (`F.ksp.preconditioner = JacobiSmoother`).** Parallel to the
  eigsolve→divfree→ksp chain at
  `book/src/concepts/nested-constructed-operator-gate.md:91-102`, the floquet
  closure's `F.ksp` (`palace/linalg/floquetcorrection.cpp:66`) carries a
  JacobiSmoother preconditioner (`:65`), which is itself a firm L1
  constructed-operator gate
  ([`jacobi-smoother`](../L1/jacobi-smoother.md)). By the
  [`solver-as-operator`](../concepts/solver-as-operator.md) rotation, this is
  a three-level nesting:
  
      floquet-corrector  ⊃  ksp_solve  ⊃  jacobi-smoother
        (F)                  (F.ksp)        (F.ksp.preconditioner)
  
  The fidelity rule applies at each edge: this theme treats `F.ksp` opaquely;
  the ksp-solve-mutation-rotation theme treats `F.ksp.preconditioner`
  opaquely; the jacobi-smoother-mutation-rotation theme treats `F.M_RT`'s
  diagonal-extraction step opaquely (concept-page §latent-site language). This
  is the **second three-level transitive nesting in the firm artifact** (after
  the eigsolve→divfree→ksp chain), confirming the concept's
  cross-layer-fidelity rule is load-bearing across two independent pipelines.
  **Concept-page §Firm-instances upgrade**: 2 firm → 3 firm
  (eigsolve + divfree + floquet-correction); the transitive-nesting note
  should mention the second three-deep chain.
- **`<Vector>` real-only path is dead-code under the
  `<ComplexVector>`-only-instantiation.** The constructor's `if constexpr` real
  branches at `palace/linalg/floquetcorrection.cpp:35-38, 53-56` are present
  textually but unreachable given the sole `template class
  FloquetCorrSolver<ComplexVector>;` at `:88`. This is a documentation-internal
  inconsistency (the parametric template invites a `<Vector>` instantiation
  the L0 doesn't supply); not a defect — it is a deliberate scope-out captured
  at Sub-pattern D. **OQ**: `floquet-correction-real-vector-instantiation-dead-code`
  (note for a future harvester / lowering-verifier — confirm no upstream Palace
  PR is in flight to add `<Vector>` instantiation).
- **The AddMult buffer-economy aliasing is theme-specific.** The
  `this->Mult(x, rhs)` re-binding pattern (sub-pattern B's load-bearing
  aliasing applicability) does not appear in any of the four sister themes —
  divfree, jacobi, chebyshev, ksp_solve don't have an AddMult surface that
  re-uses the construction-bound scratch as Mult's destination. This is a
  unique L0 idiom of `FloquetCorrSolver` and deserves a verified_against audit
  pass.
- **Lifting note (reverse direction — working notes only, NOT in the formal
  chapter).** An L0 in-place floquet-corrector apply (output-arg mutation +
  one scratch member + construction-bound operator reads) lifts to the L1
  pure correction by: (i) re-binding the output arg `y` to the return value,
  (ii) erasing the `rhs` scratch member, (iii) capturing the
  construction-bound operators as the closure `F`, (iv) unfolding `AddMult`
  into `axpy ∘ floquet_correction`. The lift requires the no-aliasing +
  no-prior-`y`-observer guarantees (Applicability conditions 1, 3) and the
  inner-ksp aliasing tolerance (Applicability condition 2) to hold at every
  call site; all four `AddMult` call sites uphold this by lexical sequencing
  (the `B *= -1.0/(1i*omega)` rescale precedes the `AddMult` which then
  consumes its result; no upstream caller observes the prior `B`). This
  reverse note is recorded here, not in the high→low formal theme content
  (per CLAUDE.md §Methodology invariants "Layers are defined high→low").
```

```edit:book/src/L1/index.md
<<<<<<< SEARCH
**Firm (25)** — element-wise updates, BLAS-1 reductions, the fused-normalise primitive, the opaque-operator gate, the constructed-operator solve gate, the eigenmode-solve gate, the polynomial-smoother gate, the divergence-free projector gate, the nonlinear-pencil interior atom, the NEP deflated-residual extension, the small-dense direct-solve gate, the NEP deflated-solve extension, the NEP quasi-Newton Jacobian action, the NEP quasi-Newton eigenvalue-correction step, the GMRES/FGMRES restart-correction back-solve, the GMRES/FGMRES per-column running-QR leaf, the diagonal-preconditioner-apply Jacobi smoother, the elementwise multiplicative-inverse primitive, and the elementwise (Hadamard) pointwise-product primitive:
=======
**Firm (26)** — element-wise updates, BLAS-1 reductions, the fused-normalise primitive, the opaque-operator gate, the constructed-operator solve gate, the eigenmode-solve gate, the polynomial-smoother gate, the divergence-free projector gate, the nonlinear-pencil interior atom, the NEP deflated-residual extension, the small-dense direct-solve gate, the NEP deflated-solve extension, the NEP quasi-Newton Jacobian action, the NEP quasi-Newton eigenvalue-correction step, the GMRES/FGMRES restart-correction back-solve, the GMRES/FGMRES per-column running-QR leaf, the diagonal-preconditioner-apply Jacobi smoother, the elementwise multiplicative-inverse primitive, the elementwise (Hadamard) pointwise-product primitive, and the floquet-periodicity B-field correction gate:
>>>>>>> REPLACE

<<<<<<< SEARCH
- [`elementwise_product`](./elementwise_product.md) — pure-functional **Hadamard pointwise product** `result = a ⊙ b`, `result[i] = a[i] · b[i]`; the diagonal-operator-action primitive at L1 (law 9: `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`) and the per-call kernel of the diagonally-scaled-preconditioner cohort (`jacobi-smoother`, `chebyshev-smoother`). Strictly generalises `scal` via broadcast specialisation (`scal(α, x) = elementwise_product(broadcast(α, N), x)`); composes with `reciprocal` (D2 sibling this cycle) to close the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner chain that `assemble-diagonal` §Dependencies named "forthcoming, plain text". Canonical L0 site is the operator-class `BaseDiagonalOperator<OperType>::Mult` (real `palace/linalg/operator.cpp:486`; complex `:504-505` six-fused-multiply-add) plus the **conjugate variant** `MultHermitianTranspose` (`:564-565` complex-only, three sign flips realising `ā ⊙ b`); the `jacobi.cpp` `Apply` helper (`:30-69`) is a line-for-line consumer duplicate. Two variant axes: element-type (real | complex) × conjugation (straight | conjugate-first-operand, complex-only). Firm-on-positive-structure (the `apply_linop` / `lu_solve` / `back_solve` / `ls_update_column` / `jacobi-smoother` no-dedicated-test precedent): every law is a syntactic identity on positive source. Closes the §Dependencies forward-references in `assemble-diagonal:73` and `jacobi-smoother:289-297`.
=======
- [`elementwise_product`](./elementwise_product.md) — pure-functional **Hadamard pointwise product** `result = a ⊙ b`, `result[i] = a[i] · b[i]`; the diagonal-operator-action primitive at L1 (law 9: `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`) and the per-call kernel of the diagonally-scaled-preconditioner cohort (`jacobi-smoother`, `chebyshev-smoother`). Strictly generalises `scal` via broadcast specialisation (`scal(α, x) = elementwise_product(broadcast(α, N), x)`); composes with `reciprocal` (D2 sibling this cycle) to close the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner chain that `assemble-diagonal` §Dependencies named "forthcoming, plain text". Canonical L0 site is the operator-class `BaseDiagonalOperator<OperType>::Mult` (real `palace/linalg/operator.cpp:486`; complex `:504-505` six-fused-multiply-add) plus the **conjugate variant** `MultHermitianTranspose` (`:564-565` complex-only, three sign flips realising `ā ⊙ b`); the `jacobi.cpp` `Apply` helper (`:30-69`) is a line-for-line consumer duplicate. Two variant axes: element-type (real | complex) × conjugation (straight | conjugate-first-operand, complex-only). Firm-on-positive-structure (the `apply_linop` / `lu_solve` / `back_solve` / `ls_update_column` / `jacobi-smoother` no-dedicated-test precedent): every law is a syntactic identity on positive source. Closes the §Dependencies forward-references in `assemble-diagonal:73` and `jacobi-smoother:289-297`.
- [`floquet-correction`](./floquet-correction.md) — pure-functional **Floquet B-field correction primitive** `y = floquet_correction(F, x)`; consumes a Nedelec input field `x` and produces the RT-space corrected field `y = F.M_RT⁻¹ · F.Cross · x` where `F.Cross = [kp ×]` is the cross-product with the Floquet wave vector and `F.M_RT` is the RT vector-FE mass operator. The **sixth constructed-operator gate at L1** (after `ksp_solve`, `eigsolve`, `chebyshev-smoother`, `divfree-projector`, `jacobi-smoother`), and the **third firm instance** of the [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md) shape (closure carries `F.ksp : Solver[F.M_RT]`). Structurally isomorphic to `divfree-projector` (same Mult+AddMult surface, same `Solver[F.M]` sub-field, same `VectorFEMassIntegrator`-based construction) but **strictly thinner**: no boundary-zeroing, no gradient correction, no empty-boundary nullspace pin — just `Cross · x` followed by `M_RT⁻¹ · rhs`. **Element-type scope-out**: only `<ComplexVector>` is instantiated (`palace/linalg/floquetcorrection.cpp:88`); the parametric `<VecType>` template is dead-code in any hypothetical real-only client (the first L1 gate with a deliberately-narrowed element-type scope). Inner CG uses a `JacobiSmoother` preconditioner (not BoomerAMG — RT mass is well-conditioned), making the gate transitively three-deep: `floquet → ksp → jacobi-smoother`. Firm-on-positive-structure (the `divfree-projector` / `jacobi-smoother` no-dedicated-test precedent): every law is a syntactic identity on positive source. Four AddMult consumer sites (`palace/drivers/drivensolver.cpp:212,336,468` + `palace/drivers/eigensolver.cpp:454`), three construction sites (`drivensolver.cpp:141,292`, `eigensolver.cpp:240`), all gated on `space_op.GetMaterialOp().HasWaveVector()`. **AddMult-as-axpy non-law**: `AddMult` is not a separate L1 operator — it unfolds into `axpy(a, floquet_correction(F, x), y)` (a load-bearing buffer-economy fusion that re-uses the scratch member as transient scaled-output buffer, with an inner-ksp aliasing applicability not present in any sister theme).
>>>>>>> REPLACE

<<<<<<< SEARCH
| [`elementwise_product`](./elementwise_product.md) | `(a: Tensor[N], b: Tensor[N]) → Tensor[N]` (i.e. `a ⊙ b`; complex conjugation sub-axis: `ā ⊙ b`) | (leaf; sibling to `scal` via broadcast subsumption `scal(α, x) = elementwise_product(broadcast(α, N), x)`; sibling to `apply_linop` via the diagonal-operator-action identity `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`; composes with `reciprocal` co-authored D2) | `firm` (Hadamard pointwise-product primitive; diagonal-operator-action realization; L0: `palace/linalg/operator.cpp:478-507` canonical real+complex straight + `:545-568` complex conjugate variant + `palace/linalg/jacobi.cpp:30-69` consumer-duplicate; harvested cycle-033; firm-on-positive-structure, no-dedicated-test caveat non-gating per `apply_linop` / `jacobi-smoother` precedent; closes the `assemble-diagonal:73` + `jacobi-smoother:289-297` forward-references) |
=======
| [`elementwise_product`](./elementwise_product.md) | `(a: Tensor[N], b: Tensor[N]) → Tensor[N]` (i.e. `a ⊙ b`; complex conjugation sub-axis: `ā ⊙ b`) | (leaf; sibling to `scal` via broadcast subsumption `scal(α, x) = elementwise_product(broadcast(α, N), x)`; sibling to `apply_linop` via the diagonal-operator-action identity `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`; composes with `reciprocal` co-authored D2) | `firm` (Hadamard pointwise-product primitive; diagonal-operator-action realization; L0: `palace/linalg/operator.cpp:478-507` canonical real+complex straight + `:545-568` complex conjugate variant + `palace/linalg/jacobi.cpp:30-69` consumer-duplicate; harvested cycle-033; firm-on-positive-structure, no-dedicated-test caveat non-gating per `apply_linop` / `jacobi-smoother` precedent; closes the `assemble-diagonal:73` + `jacobi-smoother:289-297` forward-references) |
| [`floquet-correction`](./floquet-correction.md) | `(F: FloquetCorrector[N_nd, N_rt], x: Field[N_nd, Complex]) → Field[N_rt, Complex]` (i.e. `F.M_RT⁻¹ · F.Cross · x`) | `ksp_solve` (direct, inner RT mass solve), `apply_linop` (direct, the `Cross · x` cross-product step); `jacobi-smoother` (inner CG preconditioner, closure-bound); `axpy` (the AddMult-as-axpy composition) | `firm` (constructed-operator gate; sixth at L1; third firm instance of nested-constructed-operator-gate; element-type scope-out: `<ComplexVector>` only; L0: `palace/linalg/floquetcorrection.cpp:20-86,88` + 4 AddMult consumer sites `palace/drivers/drivensolver.cpp:212,336,468` + `palace/drivers/eigensolver.cpp:454`; harvested cycle-036; firm-on-positive-structure; AddMult-as-axpy buffer-economy fusion with inner-ksp aliasing applicability) |
>>>>>>> REPLACE
```

```edit:book/src/L1-L0/index.md
<<<<<<< SEARCH
| [reciprocal-elementwise-product-mutation-rotation](./reciprocal-elementwise-product-mutation-rotation.md) | `L1/reciprocal` (firm c033) + `L1/elementwise_product` (firm c033) | `palace/linalg/vector.{hpp,cpp}`, `palace/linalg/operator.cpp`, `palace/linalg/jacobi.cpp`, `palace/fem/bilinearform.cpp` | firm *(structural + complex-reciprocal closed-form algebraic sub-rule; 2 composite sub-patterns A reciprocal receiver-self-overwrite / B elementwise-product output-arg via canonical `BaseDiagonalOperator::Mult` + consumer-duplicate `Apply(dinv, x, y)`; element-type axis (real upstream-MFEM-aliased + complex Palace-defined) + complex conjugation sub-axis on B (canonical `MultHermitianTranspose` live, consumer-duplicate `Apply<Transpose=true>` dead-code under `MultTranspose→Mult` symmetric wiring); closes c033 OQs `reciprocal-l1-l0-mutation-rotation-theme` + `elementwise-product-l1-l0-mutation-rotation-theme`; thin-theme composite per `ksp-solve-mutation-rotation` precedent — shared in-place-mutation rewrite class + co-occurrence in `JacobiSmoother::SetOperator`)* |
=======
| [reciprocal-elementwise-product-mutation-rotation](./reciprocal-elementwise-product-mutation-rotation.md) | `L1/reciprocal` (firm c033) + `L1/elementwise_product` (firm c033) | `palace/linalg/vector.{hpp,cpp}`, `palace/linalg/operator.cpp`, `palace/linalg/jacobi.cpp`, `palace/fem/bilinearform.cpp` | firm *(structural + complex-reciprocal closed-form algebraic sub-rule; 2 composite sub-patterns A reciprocal receiver-self-overwrite / B elementwise-product output-arg via canonical `BaseDiagonalOperator::Mult` + consumer-duplicate `Apply(dinv, x, y)`; element-type axis (real upstream-MFEM-aliased + complex Palace-defined) + complex conjugation sub-axis on B (canonical `MultHermitianTranspose` live, consumer-duplicate `Apply<Transpose=true>` dead-code under `MultTranspose→Mult` symmetric wiring); closes c033 OQs `reciprocal-l1-l0-mutation-rotation-theme` + `elementwise-product-l1-l0-mutation-rotation-theme`; thin-theme composite per `ksp-solve-mutation-rotation` precedent — shared in-place-mutation rewrite class + co-occurrence in `JacobiSmoother::SetOperator`)* |
| [floquet-correction-mutation-rotation](./floquet-correction-mutation-rotation.md) | `L1/floquet-correction` (firm c036) | `palace/linalg/floquetcorrection.{hpp,cpp}` + 3 construction sites (`palace/drivers/{drivensolver,eigensolver}.cpp`) + 4 AddMult consumer sites | firm *(structural + algebraic AddMult-as-axpy sub-rule; 4 sub-patterns A out-of-place `Mult(x,y)` 2-step Cross-then-ksp / B AddMult-as-axpy fusion with inner-ksp aliasing applicability / C construction-site closure materialisation (M_RT mass + Cross [kp×] + ksp CG+JacobiSmoother) / D `<ComplexVector>`-only element-type scope-out; third firm instance of `nested-constructed-operator-gate`; transitively three-deep nesting floquet→ksp→jacobi-smoother; thinner-than-divfree-projector — one scratch member (rhs only), no boundary-zeroing, no gradient correction, no empty-boundary pin; firm-on-positive-structure)* |
>>>>>>> REPLACE
```

```edit:book/src/SUMMARY.md
<<<<<<< SEARCH
- [elementwise_product](./L1/elementwise_product.md)

# L1 > L0 — Lowering
=======
- [elementwise_product](./L1/elementwise_product.md)
- [floquet-correction](./L1/floquet-correction.md)

# L1 > L0 — Lowering
>>>>>>> REPLACE

<<<<<<< SEARCH
- [reciprocal-elementwise-product-mutation-rotation](./L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
- [divfree-projector-mutation-rotation](./L1-L0/divfree-projector-mutation-rotation.md)
=======
- [reciprocal-elementwise-product-mutation-rotation](./L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
- [floquet-correction-mutation-rotation](./L1-L0/floquet-correction-mutation-rotation.md)
- [divfree-projector-mutation-rotation](./L1-L0/divfree-projector-mutation-rotation.md)
>>>>>>> REPLACE
```

```edit:book/src/concepts/nested-constructed-operator-gate.md
<<<<<<< SEARCH
## Firm instances

Two FIRM L1 operators exhibit the gate-carrying-gate shape; a third site is latent.
=======
## Firm instances

Three FIRM L1 operators exhibit the gate-carrying-gate shape; a fourth site is latent.
>>>>>>> REPLACE

<<<<<<< SEARCH
- **`divfree-projector`** (firm; cycle-016, `b54ea1c`) — **one** nested gate. The
  closure `P` binds `P.ksp : Solver[P.M]` (a CG solver bound to the ε-weighted H1
  mass-like operator `P.M` as both operator and preconditioner target), materialised
  at construction (`book/src/L1-L0/divfree-projector-mutation-rotation.md:193-198`).
  Its per-call `ksp->Mult(rhs, psi)` is the opaque inner H1 solve
  (`book/src/L1-L0/divfree-projector-mutation-rotation.md:108-113`,
  `book/src/L1/divfree-projector.md`).

**Transitive nesting (three-deep).** `E.projector : Maybe DivFreeSolver` means the
`divfree-projector` gate is *itself* a sub-field of the `eigsolve` closure — so the
two instances are not merely parallel, they are transitively nested:

    eigsolve  ⊃  divfree-projector  ⊃  ksp_solve
      (E)            (E.projector)         (P.ksp)

The eigsolve outer loop carries a divfree projector, which carries its own inner CG
solve. The fidelity rule applies at each edge: the eigsolve theme treats `E.projector`
opaquely; the divfree theme treats `P.ksp` opaquely. This three-deep transitivity is
direct evidence the pattern is load-bearing across the eigenmode pipeline, not
incidental.
=======
- **`divfree-projector`** (firm; cycle-016, `b54ea1c`) — **one** nested gate. The
  closure `P` binds `P.ksp : Solver[P.M]` (a CG solver bound to the ε-weighted H1
  mass-like operator `P.M` as both operator and preconditioner target), materialised
  at construction (`book/src/L1-L0/divfree-projector-mutation-rotation.md:193-198`).
  Its per-call `ksp->Mult(rhs, psi)` is the opaque inner H1 solve
  (`book/src/L1-L0/divfree-projector-mutation-rotation.md:108-113`,
  `book/src/L1/divfree-projector.md`).

- **`floquet-correction`** (firm; cycle-036) — **one** nested gate. The closure `F`
  binds `F.ksp : Solver[F.M_RT]` (a CG solver preconditioned by `JacobiSmoother`,
  bound to the RT vector-FE mass operator `F.M_RT` as both operator and
  preconditioner target), materialised at construction
  (`palace/linalg/floquetcorrection.cpp:60-67`). Its per-call `ksp->Mult(rhs, y)`
  is the opaque inner RT mass solve (`book/src/L1-L0/floquet-correction-mutation-rotation.md`
  Sub-pattern A, `book/src/L1/floquet-correction.md`). Structurally isomorphic to
  `divfree-projector` but strictly thinner (no boundary-zeroing, no gradient
  correction, no empty-boundary nullspace pin). Element-type scope-out:
  `<ComplexVector>` only (the first L1 nested-gate instance with a
  deliberately-narrowed element-type scope).

**Transitive nesting (three-deep) — two independent chains.** Both `eigsolve` and
`floquet-correction` close a three-level nested chain, confirming the pattern is
load-bearing across multiple pipelines (not eigsolve-incidental).

**Chain 1 (eigsolve pipeline).** `E.projector : Maybe DivFreeSolver` means the
`divfree-projector` gate is *itself* a sub-field of the `eigsolve` closure — so the
eigsolve and divfree instances are not merely parallel, they are transitively nested:

    eigsolve  ⊃  divfree-projector  ⊃  ksp_solve
      (E)            (E.projector)         (P.ksp)

The eigsolve outer loop carries a divfree projector, which carries its own inner CG
solve.

**Chain 2 (floquet pipeline).** `F.ksp.preconditioner = JacobiSmoother`, and via
[`solver-as-operator`](./solver-as-operator.md) the JacobiSmoother is itself a firm
L1 constructed-operator gate ([`jacobi-smoother`](./jacobi-smoother.md)):

    floquet-correction  ⊃  ksp_solve  ⊃  jacobi-smoother
      (F)                    (F.ksp)        (F.ksp.preconditioner)

The driver-side floquet correction carries an inner CG solve, which carries a
diagonal-preconditioner gate. The fidelity rule applies at each edge of both chains:
each outer theme treats its inner gate opaquely. Two independent three-deep chains
is direct evidence the pattern is load-bearing across multiple pipelines, not
incidental to one.
>>>>>>> REPLACE

<<<<<<< SEARCH
**Latent site — `ksp_solve` preconditioner.** `ksp_solve`'s closure `K` binds a
preconditioner `M⁻¹` (`book/src/L1/ksp_solve.md:31`). Via [`solver-as-operator`](./solver-as-operator.md),
a preconditioner **is-an** operator and may itself be a `Solver`-typed handle (a
nested `ksp` used as a preconditioner). When `K.M⁻¹` is a `Solver`, `ksp_solve` is
*also* gate-carrying-gate. But the L1 `ksp_solve` entry types `M⁻¹` as a plain
`LinearOperator[N, N]` and the `ksp-solve-mutation-rotation` theme treats the
preconditioner opaquely, so this is a **latent** nesting site, not a confirmed firm
instance (no concrete Palace site where a `BaseKspSolver`'s preconditioner is itself a
`BaseKspSolver` has been verified against L0 source — flagged for a future harvester).
Chebyshev-as-preconditioner inside a Krylov method is a related but **weaker** nesting
(`book/src/L1/chebyshev-smoother.md:140`): chebyshev is a smoother-as-operator, not a
`Solver`-gate.
=======
**Latent site — `ksp_solve` `BaseKspSolver`-as-preconditioner.** `ksp_solve`'s
closure `K` binds a preconditioner `M⁻¹` (`book/src/L1/ksp_solve.md:31`). Via
[`solver-as-operator`](./solver-as-operator.md), a preconditioner **is-an** operator
and may itself be a `Solver`-typed handle (a nested `ksp` used as a preconditioner).
When `K.M⁻¹` is a `Solver`, `ksp_solve` is *also* gate-carrying-gate. The L1
`ksp_solve` entry types `M⁻¹` as a plain `LinearOperator[N, N]` and the
`ksp-solve-mutation-rotation` theme treats the preconditioner opaquely, so this is a
**latent** nesting site, not a confirmed firm instance (no concrete Palace site where a
`BaseKspSolver`'s preconditioner is itself a `BaseKspSolver` has been verified against
L0 source — flagged for a future harvester). The floquet pipeline's
`F.ksp.preconditioner = JacobiSmoother` realises the *non-ksp* form of this latent
site (the preconditioner IS a constructed-operator gate, just a `Smoother`-gate
rather than a `Solver`-gate); a future site with `BaseKspSolver`-as-preconditioner
would be the strict version.
>>>>>>> REPLACE

<<<<<<< SEARCH
## See also

- [`ksp_solve`](./ksp_solve.md) — the innermost gate in every instance here; the inner
  iteration's home theme.
- `book/src/L1-L0/eigsolve-mutation-rotation.md` §"Sub-pattern B" — the two-gate
  instance's lowering (delegates to `ksp-solve-mutation-rotation`).
- `book/src/L1-L0/divfree-projector-mutation-rotation.md` §"Sub-pattern A" / §"Sub-pattern C"
  — the one-gate instance's lowering + closure-field materialisation.
=======
## See also

- [`ksp_solve`](./ksp_solve.md) — the innermost (solver) gate in eigsolve+divfree
  chains; the inner iteration's home theme.
- [`jacobi-smoother`](./jacobi-smoother.md) — the innermost (smoother) gate in the
  floquet chain; the diagonal-preconditioner gate.
- `book/src/L1-L0/eigsolve-mutation-rotation.md` §"Sub-pattern B" — the two-gate
  instance's lowering (delegates to `ksp-solve-mutation-rotation`).
- `book/src/L1-L0/divfree-projector-mutation-rotation.md` §"Sub-pattern A" / §"Sub-pattern C"
  — the one-gate instance's lowering + closure-field materialisation.
- `book/src/L1-L0/floquet-correction-mutation-rotation.md` §"Sub-pattern A" / §"Sub-pattern C"
  — the floquet one-gate instance's lowering + closure-field materialisation; the
  second three-deep chain (floquet → ksp → jacobi-smoother).
>>>>>>> REPLACE
```

## Supporting evidence

### Source files read

- `reference/palace/palace/linalg/floquetcorrection.hpp` (full, 65 lines).
- `reference/palace/palace/linalg/floquetcorrection.cpp` (full, 91 lines).
- `reference/palace/palace/drivers/drivensolver.cpp` (read ranges :130-155, :205-225, :282-300, :328-345, :460-475 — 3 construction sites + 3 AddMult call sites).
- `reference/palace/palace/drivers/eigensolver.cpp` (read ranges :230-260, :445-460 — 1 construction site + 1 AddMult call site).
- `reference/palace/palace/models/materialoperator.hpp` (ranges :25-50, :100-130 — `mat_kx` member, `GetFloquetCross` accessors, `HasWaveVector`).
- `reference/palace/palace/models/materialoperator.cpp` (range :340-365 — `mat_kx(count).Set(1.0, wave_vector_cross)`).

### Citation self-verification (`tools/citecheck/citecheck.py --anchor`)

All load-bearing pinpoints clean:

- `floquetcorrection.hpp:32-60` anchor `FloquetCorrSolver` — ok (lines 33, 52).
- `floquetcorrection.cpp:74-78` anchor `Mult` — ok.
- `floquetcorrection.cpp:80-86` anchor `AddMult` — ok.
- `floquetcorrection.cpp:88` anchor `ComplexVector` — ok.
- `floquetcorrection.cpp:65` anchor `JacobiSmoother` — ok.
- `floquetcorrection.cpp:60-66` anchor `CgSolver` — ok.
- `floquetcorrection.cpp:42-47` anchor `MaterialPropertyCoefficient` — ok.
- `floquetcorrection.cpp:69-70` anchor `rhs.SetSize` — ok.
- `floquetcorrection.cpp:20-71` anchor `FloquetCorrSolver<VecType>::FloquetCorrSolver` — ok.
- `floquetcorrection.cpp:26-39` anchor `BilinearForm` — ok.
- `floquetcorrection.cpp:41-57` anchor `BilinearForm` — ok.
- `floquetcorrection.hpp:42-43` anchor `std::unique_ptr<OperType>` — ok.
- `floquetcorrection.hpp:35-39` anchor `ScalarType` — ok.
- `floquetcorrection.cpp:67` anchor `SetOperators` — ok.
- `floquetcorrection.cpp:55` anchor `ParOperator` — ok.
- `floquetcorrection.cpp:50` anchor `ComplexParOperator` — ok.

### Template fidelity (template = `divfree-projector` + `jacobi-smoother`)

- §Context structure: class-doc/contract paragraph + constructed-operator-gate paragraph + element-type paragraph + nested-gate paragraph — same 4-paragraph spine as `divfree-projector.md` §Context.
- §Signature: identical bunsen-style with named axes (`N_nd`, `N_rt`); same closure-field enumeration with per-field signature + read-only annotation + Palace source range.
- §Semantics: numbered step list (1, 2) mirroring divfree's 4-step list (1, 2, 3, 4), strictly thinner.
- §Algebraic laws: linearity, range, composition, complex-linearity, two non-laws — pruned versus divfree's 6 laws + 2 non-laws (no idempotence — not a projector; no M-orthogonality — not an inner-product projection).
- §Dependencies: L1-internal + construction-time + consumer call sites — same template-engine as divfree but applied to the floquet-specific dep set.
- §Status: firm + firm-on-positive-structure + no-dedicated-unit-test + test-evidence — same `chebyshev-smoother`/`jacobi-smoother`/`divfree-projector` rubric.
- §Evidence: line-pinned citation list of every load-bearing fact — same template form.

### Plan / OQ resolution

- Plan item `floquet-correction-l1-gate-harvest` (c035 D3 carry-forward) — **resolves-on-landing** with this dispatch. The integrator should close it after applying.
- OQ candidates to OPEN:
  - `floquet-correction-real-vector-instantiation-dead-code` — confirm no upstream Palace PR fills in `<Vector>` instantiation.
  - `floquet-corrector-addmult-aliasing-applicability-audit` — `lowering-verifier` audit on the inner-ksp aliasing tolerance load-bearing applicability (the unique-to-this-theme L0 idiom).
  - `nested-constructed-operator-gate-second-three-deep-chain-codified` — track the concept-page upgrade (2→3 firm, latent-site language refined to cite the floquet realisation of the non-ksp preconditioner-gate variant).

## Open questions / caveats

- **Layer-intro currency.** §Vocabulary cohort "Firm (25)" updates to "Firm (26)" with the floquet entry inserted. Did NOT touch the §Working Notes ledger (no narrative cycle-036 bullet drafted — defer to layer-intro-author if currency drift is flagged). The dep-map table row is added at the end of the firm cohort (post-`elementwise_product` row).
- **L1-L0 index sentinel placement.** Theme row added at the end of the L1>L0 firm cohort (post-`reciprocal-elementwise-product-mutation-rotation`), keeping the obstruction-cohort tail (`minres-iteration`, `bicgstab-iteration`, `triangular-solve-obstruction`) untouched at the bottom.
- **SUMMARY.md ordering.** Chapter insertion follows the existing L1 firm-cohort order (after `elementwise_product`); theme insertion places the floquet-correction-mutation-rotation BEFORE divfree-projector-mutation-rotation to keep the divfree/floquet pair contiguous (they are the two structurally-isomorphic constructed-operator-gate-with-nested-ksp themes). Integrator may renormalise.
- **Concept-page upgrade adjacency.** The `nested-constructed-operator-gate.md` upgrade is in scope-per-harvester-discipline-when-concept-enumerates-instances (per role-spec: "When the operator overlaps with an existing `concepts/<slug>.md` entry, cross-reference rather than duplicate" — the concept page enumerates firm instances by name, and adding the third instance is the cross-reference). Repairer / integrator may overrule and route to a layer-intro-author follow-up if scope-strict.
- **L1 floquet-correction.md slug spelling.** Used `floquet-correction` (matching `divfree-projector` hyphenated style, and matching `palace/linalg/floquetcorrection.cpp`'s closest reasonable hyphenation) rather than `floquet_correction` (which would match `jacobi_smoother`-style with underscore). Consistent with the dominant-hyphen convention for multi-word L1 operator slugs in the firm cohort (`chebyshev-smoother`, `divfree-projector`, `jacobi-smoother`, `apply-linop` for the lowering theme, etc.). The L0 namespace `palace/linalg/floquetcorrection.cpp` is one word per Palace's filename convention; the slug hyphenation tracks the firm-L1-cohort norm.
- **B-field formula citation precision.** The doc comment `B = -1/(iω) ∇ x E + 1/ω kp x E` appears at four sites (`drivensolver.cpp:211, 335, 467` + `eigensolver.cpp:453`); these comments are the ONLY Palace-internal documentation of the floquet correction's purpose, treated as load-bearing context. The literature anchor for the `kp × E` correction term (Joannopoulos et al., Photonic Crystals: Molding the Flow of Light, 2nd ed., §periodic-media discussion) is mentioned in passing in §Summary; not cited as L0 evidence (literature anchoring optional at firm; Palace source + driver call-site comments are sufficient).
- **OperType/ScalarType typedef brittleness.** The L0 typedef chain at `floquetcorrection.hpp:35-39` (`OperType = std::conditional<VecType == ComplexVector, ComplexOperator, Operator>::type`, `ScalarType = std::conditional<OperType == ComplexOperator, std::complex<double>, double>::type`) is purely template machinery; the L1 form sees only `ComplexVector`/`ComplexOperator`/`std::complex<double>` triple under the sole instantiation. Captured at the dead-code-real-branch level (Sub-pattern D); no separate sub-pattern warranted.

## Self-check: `citecheck --scan`

Ran `python3 tools/citecheck/citecheck.py --scan reports/2026-05-31T200500Z-harvester-floquet-correction-l1/CYCLE.md --quiet` on this report.

Result: **96 ok, 0 failing (96 citations checked).** All path/line citations are within bounds, paths are unambiguous, no `DRIFT`/`OOB`/`MISS`/`AMBIG` findings.

# floquet_correction

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
[`divfree_projector`](./divfree_projector.md), and
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
(`JacobiSmoother`, not the divfree_projector's BoomerAMG-or-GMG-wrapping
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
signature (the closure is complex-only). Contrast `divfree_projector` (real and
complex both instantiated) and `jacobi-smoother` (real and complex both
instantiated) — `floquet_correction` is the **first L1 constructed-operator gate
to carry a deliberately-narrowed element-type scope**.

This is the **third firm instance** of the
[`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
shape: `F.ksp : Solver[F.M_RT]` is a constructed-operator sub-field carrying its
own CG iteration, JacobiSmoother preconditioner, tolerance, and iteration cap.
The CG iteration is interior to [`ksp_solve`](./ksp_solve.md) and does not leak
into `floquet_correction` (the concept's cross-layer fidelity rule). Structurally
isomorphic to `divfree_projector`'s `P.ksp : Solver[P.M]`; thinner than
`divfree_projector` (no boundary-zeroing step, no gradient-correction step, no
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
    is sufficient; contrast `divfree_projector` which needs BoomerAMG-or-GMG),
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
block-diagonal real-on-complex action as `divfree_projector`.

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
  projection — the **divfree_projector**'s `P∘P = P` law has no analog here.

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

## Status

`firm` — the signature and laws are read directly from positive Palace source.

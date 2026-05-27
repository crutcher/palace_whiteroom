# Overload set — `Mult` / `MultTranspose` / `MultHermitianTranspose` / `AddMult`

A reference note for L1 entries (and the L1>L0 `apply-linop-mutation-rotation` theme). The L0 home of operator application in Palace: a family of virtual methods on the `Operator` / `ComplexOperator` interface, implemented across a deep concrete-subclass hierarchy. L1 collapses this entire family to one operator (`apply_linop`); this overview names the L0 shape so an L1 entry or lowering theme can refer to "the `Mult` family" without re-citing every overload.

## At a glance

**Two interface hierarchies, same shape.** Palace exposes operator application through two parallel abstract base classes:

- `mfem::Operator` (re-exported as `palace::Operator` via `using Operator = mfem::Operator;` at `palace/linalg/operator.hpp:21`) — the real-valued base. The pure-virtual `Mult(const Vector &x, Vector &y) const` is inherited from MFEM.
- `palace::ComplexOperator` (declared at `palace/linalg/operator.hpp:24-68`) — the complex-valued base, defined inside Palace (not MFEM). The pure-virtual `Mult(const ComplexVector &x, ComplexVector &y) const = 0` is declared at line 54.

Both bases declare `Height()` / `Width()` accessors (real at `operator.hpp:36-39` for `ComplexOperator`; inherited from `mfem::Operator` for the real branch). Both expose the same overload-set shape; the element-type axis is the only difference.

**The overload set has three orthogonal sub-axes**:

1. **Transpose mode** — `Mult`, `MultTranspose`, `MultHermitianTranspose`. The forward apply, the transpose apply, and (complex only) the Hermitian-transpose apply. Declarations for `ComplexOperator` at `operator.hpp:54-58`; for `Operator` inherited from `mfem::Operator`. The Hermitian-transpose method exists only on the complex branch — on the real branch it collapses to the plain transpose. The `MultTranspose` and `MultHermitianTranspose` methods on `ComplexOperator` are **non-pure** virtuals with default implementations, declared but defined elsewhere; only `Mult` is pure.
2. **Accumulate mode** — `Mult` (overwrites `y`) vs `AddMult` (accumulates `a · A · x` into `y`). For `ComplexOperator` these are at `operator.hpp:60-67`; both forms exist for transpose and hermitian-transpose. The `a` parameter defaults to `1.0` (real or complex per template instantiation).
3. **Element type** — `Operator` (real, `double` scalar, `Vector` argument) vs `ComplexOperator` (complex, `std::complex<double>` scalar, `ComplexVector` argument). At L1 these collapse via parametric polymorphism over the element type (see [`mfem-vector-types`](./mfem-vector-types.md) and [`L1/apply_linop`](../L1/apply_linop.md) Variant axes).

The full set therefore has up to 12 entries per concrete subclass on the complex branch (3 transpose modes × 2 accumulate modes × forward / templated paths) and 4 on the real branch (2 transpose modes × 2 accumulate modes). Most subclasses override a subset — typically `Mult`, `MultTranspose`, and `AddMult` for the forward direction, deferring Hermitian-transpose to a helper template ([`ProductOperatorHelper`](#dispatch-helper-templates) below).

## Concrete-subclass family

The hierarchy is broad. Each concrete subclass realises the abstract interface for a specific operator-construction pattern; the same `Mult` virtual is overridden across all of them. The L1 `LinearOperator` opaque type collapses all of them.

- **`ComplexWrapperOperator`** (`operator.hpp:73-113`) — wraps a pair of real operators `(Ar, Ai)` as a complex operator via the equivalent-real block formulation `[Ar -Ai; Ai Ar]`. The bridge between the real and complex hierarchies; relevant to the [`complex-from-real-lift`](../concepts/complex-from-real-lift.md) concept.
- **`SumOperator`** (`operator.hpp:116-136`) — represents `Σᵢ cᵢ · Aᵢ` for a collection of operators with scalar coefficients (`std::vector<std::pair<const Operator *, double>> ops`, line 119). Real-branch only; the `Mult` definition at `operator.cpp:428-441` has a single-operator fast path and otherwise zeros `y` then calls `AddMult`. The `AddMult` body at `operator.cpp:458-466` is the canonical witness of operator-side linearity (loop accumulating `op->Mult(x, z); y.Add(a * c, z)`).
- **`BaseProductOperator<OperType>`** (`operator.hpp:178-226`) — operator composition `A · B`. Templated over `OperType ∈ {Operator, ComplexOperator}`; aliased as `ProductOperator` (real) and `ComplexProductOperator` (complex) at `operator.hpp:228-229`. The `Mult` definition at `operator.hpp:202-206` is the two-step `B.Mult(x, z); A.Mult(z, y)` — direct L0 witness of the L1 composition law. Workspace `z` is a mutable member (`operator.hpp:192`).
- **`BaseDiagonalOperator<OperType>`** (`operator.hpp:256-291`) — element-wise scaling by a vector `d` (the "diagonal of a diagonal matrix"). The forward and transpose forms coincide (`MultTranspose` delegates to `Mult` at `operator.hpp:279`). Real and complex specialisations of `Mult` at `operator.cpp:478-507` (real at 478-487, complex at 489-507).
- **`BaseMultigridOperator<OperType>`** (`operator.hpp:298-367`) — a hierarchy of operators (one per multigrid level) plus optional auxiliary-space operators. The `Mult` family dispatches to the finest-level operator (`operator.hpp:347, 349-352, 354-357`), so the multigrid hierarchy is invisible at the apply-time interface; the level structure is consumed by the geometric-multigrid solver, not by the operator-application path.
- **`ParOperator`** / **`ComplexParOperator`** (defined in `palace/linalg/rap.hpp`, implementations in `palace/linalg/rap.cpp`) — parallel wrappers that apply prolongation around the inner operator and restriction after it, with optional Dirichlet-BC tdof masking. The `ParOperator::Mult` body at `palace/linalg/rap.cpp:195-234` is the canonical wrapper-apply pattern. Per the single-rank reading (CLAUDE.md §Scope), the prolongation / restriction collapses to identity and the masking is the only remaining concern at L1.

A non-exhaustive list. Other operator-shaped types in Palace (preconditioners under `palace/linalg/`, FE assembly closures under `palace/fem/`, Jacobian-action operators) all implement the same interface; the overload-set shape is uniform.

## Dispatch helper templates

Two templated helper-class hierarchies factor out the Hermitian-transpose dispatch:

- **`ProductOperatorHelper<ProductOperator, OperType>`** (`operator.hpp:140-176`) — partial specialisations for `OperType = Operator` (empty body) and `OperType = ComplexOperator` (defines `MultHermitianTranspose` and `AddMultHermitianTranspose` via two-step apply on the inner `A` and `B`). The real branch inherits no extra methods; the complex branch gets the Hermitian-transpose method synthesised from the inner operators' Hermitian-transposes.
- **`DiagonalOperatorHelper<DiagonalOperator, OperType>`** (`operator.hpp:232-254`) — same pattern for `BaseDiagonalOperator`: the complex branch declares `MultHermitianTranspose` and `AddMultHermitianTranspose`; the real branch does not.

These helpers exist because the Hermitian-transpose method is only meaningful on `ComplexOperator` and would be empty on `Operator`. CRTP (Curiously Recurring Template Pattern) plus partial specialisation produces the desired branch-by-branch interface without virtual-method bloat on the real side.

## The L1 collapse

L1 `apply_linop` collapses this entire overload set to one operator: `y = apply_linop(A, x)`. The three sub-axes are handled as follows (per [`L1/apply_linop`](../L1/apply_linop.md) Variant axes):

- **Transpose mode** — recoverable via algebraic transforms `Aᵀ`, `Aᴴ`; not separate L1 operators. The dedicated virtual methods at L0 exist for representation-aware specialisation (a sparse-matrix `A` may transpose efficiently in-place; a matrix-free `A` may have a separate transpose-action implementation), but at L1 the rotation `apply_linop(A, x) → apply_linop(Aᵀ, x)` is a one-argument-substitution.
- **Accumulate mode** — `AddMult(A, x, a, y) → y + a · A · x` is the L1 composition `axpby(a, apply_linop(A, x), 1, y)`. Not a separate operator; the L0 fusion is recorded as a transparent performance trick in the L1>L0 lowering theme [`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md).
- **Element type** — the `Operator` / `ComplexOperator` split collapses to parametric polymorphism over the element type. The semantics are identical across element types — the linear-map relationship is the same; only the underlying scalar field differs.
- **Operator representation** (the implicit fourth axis, fully absorbed) — `SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `BaseMultigridOperator`, `ComplexWrapperOperator`, `ParOperator`, all preconditioners, all FE assembly closures, all Jacobian-action operators — all collapse to a single opaque `LinearOperator[M, N]` type at L1. This is the canonical *variant absorption* application (per [`concepts/variant-absorption`](../concepts/variant-absorption.md)).

## Referenced from

*The L1 / L1>L0 entries below already cite this overload set inline. The retroactive-thinning sweep (priority #11) will replace those inline citations with backlinks here.*

- [`L1/apply_linop`](../L1/apply_linop.md) — collapses the entire overload set to one operator parameterised by element type.
- [`L1-L0/apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md) — the L1>L0 lowering theme that reintroduces the destination-buffer mention and selects between the `Mult` and `AddMult` forms per sub-pattern.
- [`concepts/constructed-operators`](../concepts/constructed-operators.md) — narrative for the `BaseProductOperator` / `SumOperator` family.
- [`concepts/complex-from-real-lift`](../concepts/complex-from-real-lift.md) — narrative for the `ComplexWrapperOperator` real-imag block formulation.
- [`L0/ksp-factory-file`](./ksp-factory-file.md) — uses `Operator` / `ComplexOperator` as the `OperType` template parameter throughout the KSP construction surface.
- [`L0/kspsolver-base-class`](./kspsolver-base-class.md) — the `BaseKspSolver<OperType>` wraps an operator of this hierarchy and exposes a `Mult` of the same interface shape.

## Evidence (representative)

- `palace/linalg/operator.hpp:21` — `using Operator = mfem::Operator;` — real branch type alias.
- `palace/linalg/operator.hpp:24-68` — `ComplexOperator` abstract class: declares pure-virtual `Mult` (line 54), non-pure `MultTranspose` (56), `MultHermitianTranspose` (58), `AddMult` (60), `AddMultTranspose` (63), `AddMultHermitianTranspose` (66).
- `palace/linalg/operator.hpp:36-39` — `Height()` / `Width()` accessors on `ComplexOperator`.
- `palace/linalg/operator.hpp:73-113` — `ComplexWrapperOperator` (equivalent-real block formulation).
- `palace/linalg/operator.hpp:116-136` — `SumOperator` (real-only sum-of-operators).
- `palace/linalg/operator.hpp:140-176` — `ProductOperatorHelper` partial specialisations (Hermitian-transpose synthesis).
- `palace/linalg/operator.hpp:178-226` — `BaseProductOperator<OperType>` template (operator composition).
- `palace/linalg/operator.hpp:202-206` — `BaseProductOperator::Mult` body: two-step `B.Mult(x, z); A.Mult(z, y)`. Direct L0 witness of L1 composition law.
- `palace/linalg/operator.hpp:228-229` — `ProductOperator` / `ComplexProductOperator` aliases.
- `palace/linalg/operator.hpp:232-291` — `DiagonalOperatorHelper` + `BaseDiagonalOperator<OperType>` (element-wise scaling).
- `palace/linalg/operator.hpp:298-367` — `BaseMultigridOperator<OperType>` (hierarchy; `Mult` dispatches to finest level).
- `palace/linalg/operator.cpp:428-441` — `SumOperator::Mult` body: single-op fast path + multi-op `y = 0; AddMult(x, y)` dispatch.
- `palace/linalg/operator.cpp:458-466` — `SumOperator::AddMult` body: loop `op->Mult(x, z); y.Add(a * c, z)`.
- `palace/linalg/operator.cpp:478-507` — `BaseDiagonalOperator<Operator>::Mult` (478-487) + `BaseDiagonalOperator<ComplexOperator>::Mult` (489-507) definitions.
- `palace/linalg/rap.cpp:195-234` — `ParOperator::Mult` body (prolongation + inner-op + restriction + BC masking).
- `palace/linalg/rap.cpp:236-275` — `ParOperator::MultTranspose` body (swaps prolongation/restriction roles; representation-aware transpose).
- `palace/linalg/rap.cpp:481-517` — `ComplexParOperator::Mult` body.
- `palace/linalg/iterative.cpp:379, 443` — CG using `A->Mult(p, z)` per step (downstream use site, demonstrates the `Mult` family is the per-step iterative-solver primitive).

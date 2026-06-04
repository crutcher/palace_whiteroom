# File — `palace/linalg/operator.{hpp,cpp}`

A reference note for L1 / L2 / L4 entries that cite Palace's linear-operator surface. `palace/linalg/operator.hpp` (407 lines) plus `palace/linalg/operator.cpp` (698 lines) is the home of the operator class hierarchy that L1's `apply_linop`, L2's product-and-sum combinators, and L4's operator-typed surface all anchor to. This chapter is the file-level overview; the method-overload set is catalogued separately in [`apply-linop-overload-set`](./apply-linop-overload-set.md).

The file pair contains **seven class definitions** (one type alias + one abstract base + five concrete-or-template classes, with two additional CRTP helper templates that are counted with their owning class) plus a **namespace of free functions** (`palace::linalg::`) for matrix-weighted norms and bilinear-form inner products. The parallel-RAP wrapping classes (`ParOperator`, `ComplexParOperator`) live in a sibling file `palace/linalg/rap.{hpp,cpp}` and are summarised at the end of this chapter as the "where to look for the parallel layer" cross-reference.

## File structure

`operator.hpp` is organised top-down:

- **`palace::Operator` alias** (`palace/linalg/operator.hpp:21`) — a one-line `using Operator = mfem::Operator;`. Real-valued operators reuse MFEM's hierarchy directly; Palace does not introduce a real-operator wrapper class. The reason `ComplexOperator` exists is precisely that MFEM has no `mfem::ComplexOperator`.

- **`ComplexOperator` abstract base** (`palace/linalg/operator.hpp:24-68`) — the complex-valued counterpart. Carries `height` / `width` size members; declares pure-virtual `Mult` (line 54) and provides default-implemented `MultTranspose` / `MultHermitianTranspose` / `AddMult` / `AddMultTranspose` / `AddMultHermitianTranspose` (lines 56-67) — all six method-shapes that [`apply-linop-overload-set`](./apply-linop-overload-set.md) catalogues. Adds `Real()` / `Imag()` accessors (lines 47-48) returning the real and imaginary parts as `const Operator *` (i.e., real `mfem::Operator` references), with default implementations in `operator.cpp:13-23` that return `nullptr`. Concrete subclasses can opt in by overriding `Real()` / `Imag()` to expose the split representation.

- **`ComplexWrapperOperator`** (`palace/linalg/operator.hpp:73-113`) — concrete subclass of `ComplexOperator` that wraps a real-and-imaginary `Operator` pair using the **equivalent-real `2×2` block formulation** (line 70-72 comment):
  ```text
  [ yr ]   [ Ar  -Ai ] [ xr ]
  [ yi ] = [ Ai   Ar ] [ xi ]
  ```
  Holds optional owning `unique_ptr<Operator>` for `data_Ar` / `data_Ai` (line 77) and non-owning `const Operator *Ar, *Ai` (line 78); the constructors at lines 83-92 cover both modes. The six method-shape overrides at lines 99-112 implement complex `Mult` / `MultTranspose` / `MultHermitianTranspose` / three `AddMult`-shaped variants. Implementation bodies in `operator.cpp:85-394`. This is the **operator-side counterpart** of `MfemWrapperSolver<ComplexOperator>` (see [`mfem-wrapper-solver`](./mfem-wrapper-solver.md) §"The complex specialisation"); together they form the complex-from-real-lift surface for both operators and preconditioners.

- **`SumOperator` (real-only)** (`palace/linalg/operator.hpp:116-136`) — wraps a sequence of `Operator` references with optional `double` coefficients, exposing the weighted-sum action as a single `Operator`. Holds `std::vector<std::pair<const Operator *, double>> ops` (line 119) and a `mutable Vector z` workspace (line 120; Category 1 — operator-composition workspace — of [`mutable-workspace-pattern`](./mutable-workspace-pattern.md)). Method bodies in `operator.cpp:421-475`.

- **`ProductOperatorHelper<P, OperType>` + `BaseProductOperator<OperType>`** (`palace/linalg/operator.hpp:140-226`) — templated product of two operators with Hermitian-transpose handling. The helper template at lines 140-176 is the CRTP base for the Hermitian-transpose specialisations; the actual `BaseProductOperator` at lines 178-226 holds `const OperType &A, &B` references and a `mutable VecType z` workspace (`Vector` for real, `ComplexVector` for complex via `std::conditional`). Type aliases at lines 228-229: `using ProductOperator = BaseProductOperator<Operator>; using ComplexProductOperator = BaseProductOperator<ComplexOperator>;`. The `Mult` body at lines 202-206 is `B.Mult(x, z); A.Mult(z, y);` — the workspace `z` carries the intermediate `Bx` before `A` is applied. **This is the canonical L0 substrate for L2's "product-of-operators" combinator** — the implementation makes the workspace explicit; the L1 lift erases it.

- **`DiagonalOperatorHelper<D, OperType>` + `BaseDiagonalOperator<OperType>`** (`palace/linalg/operator.hpp:232-291`) — same CRTP shape, but for `diag(d) x` with a `VecType` of diagonal entries. Type aliases at lines 290-291: `using DiagonalOperator = BaseDiagonalOperator<Operator>; using ComplexDiagonalOperator = BaseDiagonalOperator<ComplexOperator>;`. Specialised method bodies in `operator.cpp:478-595` (one per element-type cross product-of-complex-element-type cross with `Mult` / `MultTranspose` / `AddMult` / `AddMultTranspose` / `MultHermitianTranspose` / `AddMultHermitianTranspose`).

- **`BaseMultigridOperator<OperType>`** (`palace/linalg/operator.hpp:298-364`) — container for a sequence of operators corresponding to a multigrid hierarchy, with optional auxiliary-space operators at each level. Holds `std::vector<std::unique_ptr<OperType>> ops, aux_ops` (line 307). The `Mult` / `MultTranspose` / `AddMult` / `AddMultTranspose` overrides at lines 347-363 forward to `GetFinestOperator()` — the multigrid container *itself* answers operator-application queries with the finest-level operator's action; the coarser levels are accessed via `GetOperatorAtLevel(l)`. Type aliases at lines 366-367. The container hierarchy is consumed by the multigrid preconditioner (`palace/linalg/gmg.{hpp,cpp}`), which orchestrates the V-cycle / W-cycle over the level operators.

- **`linalg::` free functions** (`palace/linalg/operator.hpp:369-403`) — a small namespace at the file's bottom for matrix-weighted operations that take an `Operator &B` as the inner-product weight:
  - `Norml2(comm, x, B, Bx)` — the SPD-`B`-weighted vector norm `‖x‖_B = √(xᴴ B x)` (line 374; implementation at `operator.cpp:600-619`).
  - `Normalize(comm, x, B, Bx)` — in-place normalization by `Norml2` (line 378, inline definition).
  - `Dot(comm, x, A, y)` — the bilinear-form inner product `yᴴ A x` for either a real `A` (line 388) or complex `A` (line 393); implementations at `operator.cpp:621-639` use the [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) "allocates workspace internally" form (Category 1 — operator-composition workspace, holding the `A·x` intermediate between the apply and the reduction).
  - `SpectralNorm(comm, A, sym, tol, max_it)` — estimate operator 2-norm via power iteration (lines 398-401; implementation at `operator.cpp:640-694`).

`operator.cpp` matches `operator.hpp` section-for-section: the abstract-base implementations come first (lines 13-66), then the wrapper-class implementations (`ComplexWrapperOperator` at lines 85-394), then the sum / product / diagonal concrete bodies, then the free-function block at the bottom.

## What's **not** here

Three operator-related concerns live in sibling files:

- **`ParOperator`, `ComplexParOperator`, `BuildParSumOperator`** — the parallel-RAP wrapping classes. These live in `palace/linalg/rap.{hpp,cpp}` because RAP (Restriction-A-Prolongation) is a parallel-distribution concept; the wrappers carry `Prolongation` / `Restriction` operators and Dirichlet-tdof elimination state alongside the inner `Operator`. The hierarchy is parallel to the in-this-file `ProductOperator` shape but with an MFEM-`HypreParMatrix` `ParallelAssemble` / `StealParallelAssemble` path. See `palace/linalg/rap.hpp:24-121` for `ParOperator`, `palace/linalg/rap.hpp:124-222` for `ComplexParOperator`, and `palace/linalg/rap.hpp:227-263` for the `BuildParSumOperator` factory family. Under [`par-types-single-rank-reading`](./par-types-single-rank-reading.md) the RAP wrapping collapses to identity-restriction-and-prolongation with the inner-operator-plus-BC-masking remaining.
- **`Solver<OperType>`, `MfemWrapperSolver<OperType>`** — preconditioner / solver classes that inherit from `Operator` / `ComplexOperator`. These live in `palace/linalg/solver.{hpp,cpp}` because they bridge to the iterative-solver composition; see [`mfem-wrapper-solver`](./mfem-wrapper-solver.md) for the wrapper specifically.
- **Iterative-solver classes** (`IterativeSolver<OperType>`, `CgSolver`, `GmresSolver`, `FgmresSolver`) — these live in `palace/linalg/iterative.{hpp,cpp}`; see [`linalg-iterative-file`](./linalg-iterative-file.md).

The operator base classes (`Operator`, `ComplexOperator`) defined in this file are the **type-axis common parent** of all three: solver / iterative-solver / parallel-wrapper classes all inherit from them.

## Test coverage

`palace/test/unit/test-rap.cpp` is the primary unit test for the operator-class hierarchy. The test is tagged `[rap][Serial][Parallel]` (line 24) and exercises:

- **`SumOperator` algebra** indirectly via `BuildParSumOperator`'s `SECTION("ParOperator")` at `palace/test/unit/test-rap.cpp:50-89`. The test asserts:
  ```cpp
  sum->Mult(v0, x1);
  DA->AddMult(v0, x2, c1);
  A->AddMult(v0, x2, c2);
  x1 -= x2;
  x1.Abs();
  CHECK(x1.Max() < tol);  // tol = 1e-12
  ```
  This is direct algebraic-equivalence evidence: `sum.Mult(v) == c1 · DA.Mult(v) + c2 · A.Mult(v)`. The `SumOperator` body at `operator.cpp:428-441` is the implementation under test (the parallel-RAP wrapping at the outermost layer is transparent under single-rank reading).
- **`ComplexParOperator` algebra** in `SECTION("ComplexParOperator")` at `palace/test/unit/test-rap.cpp:91-133` — same pattern, dual element-type axis. The complex variant exercises `ComplexWrapperOperator`-style `2×2` block formulation indirectly (via the `ComplexParOperator`'s inner-operator pair).

This test is a strong L0-equivalent evidence anchor for both `SumOperator` and the product-shape combinators; the [`apply-linop-overload-set`](./apply-linop-overload-set.md) chapter's per-overload claims can be cross-checked against the test's `Mult` / `AddMult` assertions.

There is no dedicated unit test for `BaseProductOperator` / `BaseDiagonalOperator` / `BaseMultigridOperator` in isolation — they are exercised end-to-end via the preconditioner pipelines (`palace/test/unit/test-coefficient.cpp` and `palace/test/unit/test-libceed.cpp` touch the operator-construction surface) and via the full-application regressions.

## Notes for higher layers

- **`operator.{hpp,cpp}` is the file where the operator-typing axis is fixed.** `Operator` (real) and `ComplexOperator` (complex) are the two type-axis branches that all higher classes specialise over (via `OperType` template-parameter, via `BaseProductOperator<OperType>` etc.). L1 / L4 names a single operator type and the element-type axis collapses per [`mfem-vector-types`](./mfem-vector-types.md).
- **The CRTP helper-class pattern** (`ProductOperatorHelper` / `DiagonalOperatorHelper`) exists to specialise the `MultHermitianTranspose` / `AddMultHermitianTranspose` overrides only for the complex branch — real operators don't have a meaningful Hermitian transpose (it equals the transpose). This is a transparent C++-template trick; at L1 the operator just has the six method-shapes and the element-type specialisation disappears.
- **`BaseMultigridOperator` is the container, not the algorithm.** The V-cycle / W-cycle algorithm lives in the multigrid preconditioner (`gmg.cpp`); `BaseMultigridOperator` is the data structure that holds the per-level operators. The `Mult` override forwarding to the finest operator (lines 347-348) is a "natural" choice when the container is itself used as an operator — but for preconditioner application it's the V-cycle algorithm that actually consumes the level structure.
- **The `linalg::` free functions are the natural L0 anchor for L1's matrix-weighted norm and bilinear-form operators.** `Norml2(comm, x, B, Bx)` lifts to L1's [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md); `Dot(comm, x, A, y)` lifts to L1's [`bilinear-form`](../L1/bilinear-form.md). Both are harvested at L1 (cycle-008 / cycle-010); `matrix-weighted-norm` is now `firm` (promoted cycle-091), `bilinear-form` remains `rough-in`. The unweighted forms remain the separate [`nrm2`](../L1/nrm2.md) / [`dot`](../L1/dot.md) operators. The workspace-internal-allocation pattern (`Dot`'s synthetic workspace) is Category 1 of [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) (operator-composition workspace, holding the `A·x` intermediate between the apply and the reduction).
- **`SpectralNorm` is power iteration**, not a direct algebra. It is itself a small iterative algorithm with a configurable `tol` and `max_it`; the L1 lift would express it as a `power_iterate` operator separate from the underlying `apply_linop`, structurally analogous to (but simpler than) the eigensolver wrappers in [`eigensolver-wrapper`](./eigensolver-wrapper.md).

## Dependencies

- [`apply-linop-overload-set`](./apply-linop-overload-set.md) — the method-overload set catalogue (the per-method-shape view of the same classes).
- [`mfem-vector-types`](./mfem-vector-types.md) — the element-type axis collapse rule; this file is where the C++ representation of the dual lives.
- [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) — `SumOperator::z`, `BaseProductOperator::z`, and the free-function `Dot`'s synthetic workspace are all Category 1 (operator-composition workspaces).
- [`par-types-single-rank-reading`](./par-types-single-rank-reading.md) — the parallel-RAP wrapping in the sibling file `palace/linalg/rap.{hpp,cpp}` collapses under this rule.

## Referenced from

- [`L0/apply-linop-overload-set`](./apply-linop-overload-set.md) — the method-overload set catalogue references this file as the per-method-shape's home.
- [`L0/mfem-wrapper-solver`](./mfem-wrapper-solver.md) — the preconditioner wrapper uses the `ComplexWrapperOperator`'s equivalent-real block formulation as its operator-side counterpart.
- [`L0/mutable-workspace-pattern`](./mutable-workspace-pattern.md) — Category 1 (operator-composition workspaces) cites `SumOperator::z` and `BaseProductOperator::z`.
- Higher-layer L1 / L2 / L4 entries (forward-target): the [`L1/apply_linop`](../L1/apply_linop.md) operator anchors here; the matrix-weighted free functions are anchored by [`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md) and [`L1/bilinear-form`](../L1/bilinear-form.md) (future `L1/power_iterate` will anchor `SpectralNorm`); the L2 product-and-sum combinators (rough-in: `L2/product-of-operators`, `L2/sum-of-operators`) lift the templated combinator structure.

## Evidence (representative)

- `palace/linalg/operator.hpp:1-407` — the file itself (407 lines).
- `palace/linalg/operator.hpp:21` — `using Operator = mfem::Operator;` (real branch is MFEM's type, no Palace wrapper).
- `palace/linalg/operator.hpp:24-68` — `ComplexOperator` abstract base.
- `palace/linalg/operator.hpp:47-48` — `Real()` / `Imag()` accessors for the split representation.
- `palace/linalg/operator.hpp:54` — pure-virtual `Mult(const ComplexVector &x, ComplexVector &y) const`.
- `palace/linalg/operator.hpp:56-67` — default-implemented `MultTranspose` / `MultHermitianTranspose` / three `AddMult`-shaped variants (the six-method-shape complex-operator overload set).
- `palace/linalg/operator.hpp:70-72` — comment block specifying the `2×2` equivalent-real block formulation.
- `palace/linalg/operator.hpp:73-113` — `ComplexWrapperOperator` concrete subclass; constructors at lines 83-92.
- `palace/linalg/operator.hpp:116-136` — `SumOperator` (real-only).
- `palace/linalg/operator.hpp:120` — `mutable Vector z` workspace member.
- `palace/linalg/operator.hpp:140-176` — `ProductOperatorHelper<P, OperType>` CRTP base (Hermitian-transpose specialisation for the complex branch).
- `palace/linalg/operator.hpp:178-226` — `BaseProductOperator<OperType>` template; method bodies at lines 202-225 (`Mult` at 202-206, `MultTranspose` at 208-212, `AddMult` at 214-218, `AddMultTranspose` at 220-225).
- `palace/linalg/operator.hpp:192` — `mutable VecType z` workspace member.
- `palace/linalg/operator.hpp:228-229` — `ProductOperator = BaseProductOperator<Operator>;` / `ComplexProductOperator = BaseProductOperator<ComplexOperator>;`.
- `palace/linalg/operator.hpp:232-291` — `DiagonalOperatorHelper` / `BaseDiagonalOperator` (`diag(d) x`).
- `palace/linalg/operator.hpp:290-291` — `DiagonalOperator` / `ComplexDiagonalOperator` type aliases.
- `palace/linalg/operator.hpp:298-364` — `BaseMultigridOperator<OperType>` container.
- `palace/linalg/operator.hpp:307` — `std::vector<std::unique_ptr<OperType>> ops, aux_ops;` per-level storage.
- `palace/linalg/operator.hpp:347-363` — `Mult` / `MultTranspose` / `AddMult` / `AddMultTranspose` overrides forwarding to `GetFinestOperator()`.
- `palace/linalg/operator.hpp:366-367` — `MultigridOperator` / `ComplexMultigridOperator` type aliases.
- `palace/linalg/operator.hpp:369-403` — `linalg::` free-function namespace.
- `palace/linalg/operator.hpp:374` — `Norml2(comm, x, B, Bx)` SPD-weighted norm signature.
- `palace/linalg/operator.hpp:378-384` — `Normalize` inline definition (calls `Norml2`, divides in place).
- `palace/linalg/operator.hpp:388-394` — two `Dot` overloads for real-`A` / complex-`A` bilinear forms.
- `palace/linalg/operator.hpp:398-401` — `SpectralNorm` (power iteration).
- `palace/linalg/operator.cpp:1-698` — the implementation file (698 lines).
- `palace/linalg/operator.cpp:13-23` — `ComplexOperator::Real() / Imag()` default implementations returning `nullptr`.
- `palace/linalg/operator.cpp:25-66` — `ComplexOperator::AssembleDiagonal`, `MultTranspose`, `MultHermitianTranspose`, three `AddMult`-shape default implementations.
- `palace/linalg/operator.cpp:85-394` — `ComplexWrapperOperator` method bodies.
- `palace/linalg/operator.cpp:421-475` — `SumOperator` method bodies (`AddOperator`, `Mult`, `MultTranspose`, `AddMult`, `AddMultTranspose`).
- `palace/linalg/operator.cpp:478-595` — `BaseDiagonalOperator` and `DiagonalOperatorHelper` specialised method bodies.
- `palace/linalg/operator.cpp:600-619` — `linalg::Norml2` template specialisations (real / complex).
- `palace/linalg/operator.cpp:621-639` — `linalg::Dot` template specialisations (real / complex `A`).
- `palace/linalg/operator.cpp:640-694` — `linalg::SpectralNorm` template specialisations (power iteration).
- `palace/test/unit/test-rap.cpp:24` — `TEST_CASE("BuildParSumOperator", "[rap][Serial][Parallel]")` (sum-operator algebra test).
- `palace/test/unit/test-rap.cpp:80-88` — direct algebraic-equivalence assertion for `sum->Mult` vs weighted `AddMult` sum.
- `palace/test/unit/test-rap.cpp:91-133` — `ComplexParOperator` `SECTION` (complex-element-type-axis dual test).
- `palace/linalg/rap.hpp:24` — `class ParOperator : public Operator` (parallel-RAP real branch; sibling file).
- `palace/linalg/rap.hpp:123` — `class ComplexParOperator : public ComplexOperator` (parallel-RAP complex branch; sibling file).
- `palace/linalg/rap.hpp:227-263` — `BuildParSumOperator` factory family (three overloads: real-coeff, complex-coeff, generic-deducing).

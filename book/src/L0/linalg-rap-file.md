# File — `palace/linalg/rap.{hpp,cpp}`

A reference note for the **R·A·P (Galerkin) parallel-operator** file. Per the header comment
(`palace/linalg/rap.hpp:17-19`): *"A parallel operator represented by RAP constructed through
the actions of R, A, and P, usually with R = Pᵀ ... Here R and P are the parallel restriction
and prolongation matrices."* This is the triple-product `RAP = R · A · P` — restriction `R`,
assembled (or matrix-free) local operator `A`, prolongation `P` — **not** Restrictive Additive
Schwarz. The file is the L0 anchor for how Palace turns a *local* (L-vector) finite-element
operator into a *parallel* (true-dof / T-vector) operator: either lazily, by a matrix-free
prolongate-apply-restrict sandwich, or eagerly, by assembling a single `mfem::HypreParMatrix`
triple product. It is a sibling of [`linalg-operator-file`](./linalg-operator-file.md) (which
holds the `Operator` / `ComplexOperator` base hierarchy `ParOperator` and `ComplexParOperator`
inherit from) and is already cited by [`apply-linop-overload-set`](./apply-linop-overload-set.md)
as a concrete member of the `Mult` / `AddMult` overload family.

`rap.hpp` (252 lines) declares two classes inside `namespace palace`; `rap.cpp` (~979 lines)
holds their method bodies plus the `BuildParSumOperator` weighted-summation family. Per the
single-rank reading rule ([`par-types-single-rank-reading`](./par-types-single-rank-reading.md)),
all `HypreParMatrix` / `MPI_Comm` / true-dof-vs-L-dof machinery collapses: at single rank the
prolongation `P` and restriction `R` become local identity-ish maps and the parallel triple
product `RAP` collapses to the local operator `A` (modulo essential-BC elimination). **MPI
flagged once here; not re-flagged per method.**

## At a glance — the two classes

The header declares, inside `namespace palace` (opened at `rap.hpp:14`):

- **`ParOperator : public Operator`** (`rap.hpp:24-121`) — the real-valued RAP operator. Holds
  the local operator `A` (optionally owned via `data_A`, `rap.hpp:27-28`), trial/test
  `FiniteElementSpace` references (`rap.hpp:31`), a `use_R` flag selecting true restriction `R`
  vs prolongation-transpose `Pᵀ` (`rap.hpp:32`), an essential-BC true-dof list with a
  `DiagonalPolicy` (`rap.hpp:35,38`), and a `mutable std::unique_ptr<mfem::HypreParMatrix> RAP`
  (`rap.hpp:42`) — the lazily-assembled parallel matrix, `nullptr` until `ParallelAssemble`
  forces it.
- **`ComplexParOperator : public ComplexOperator`** (`rap.hpp:124-222`) — the complex-valued
  RAP operator. Its real and imaginary parts are held as **two owned non-owning `ParOperator`
  objects** `RAPr, RAPi` (`rap.hpp:142`); `Real()` / `Imag()` (`rap.hpp:175-176`) return them.
  Its `Mult` family applies `A` once to a complex L-vector and prolongates/restricts the real
  and imaginary components separately (`rap.cpp:486-499`), so the parallel machinery is exactly
  `ParOperator`'s, run componentwise. It adds the Hermitian-transpose overloads
  (`MultHermitianTranspose` / `AddMultHermitianTranspose`, `rap.hpp:209,220-221`) absent on the
  real class — the only API delta beyond the element type.

The local operator `A` is itself either an assembled `hypre::HypreCSRMatrix` or a matrix-free
`ceed::Operator` (`rap.cpp:91-101`); the `ParOperator` is agnostic until assembly forces the
distinction.

## The two apply paths (matrix-free vs assembled)

`ParOperator` has **two algebraically-equivalent ways to apply** the parallel operator, and the
choice is a load-bearing performance dual (per
[`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md) the *result* is
identical; the assembled path trades memory for repeated-apply speed):

- **Matrix-free apply** — `Mult` (`rap.cpp:195-234`) does the sandwich directly: prolongate the
  input T-vector to an L-vector (`P·x`), apply the local operator (`A·(P·x)`), then restrict
  back (`R·(A·P·x)`), with essential-BC dofs zeroed before and re-imposed after per the diagonal
  policy. `MultTranspose` (`rap.cpp:236-275`) runs the adjoint sandwich; `AddMult` /
  `AddMultTranspose` (`rap.cpp:277-361`) accumulate with a scalar. The restrict step itself is
  the `R` vs `Pᵀ` choice, isolated in the `RestrictionMatrixMult` helper (`rap.cpp:363-385`):
  `use_R ? R.Mult : P.MultTranspose`.
- **Assembled apply** — once `ParallelAssemble` (`rap.cpp:84-152`) has built the
  `mfem::HypreParMatrix RAP` via the Hypre triple product (`hypre_ParCSRMatrixRAPKT(Rt, A, P)`
  for the `R = Pᵀ` case, `rap.cpp:116-117`; an explicit `R·(A·P)` two-step
  `hypre_ParCSRMatMat` chain for the `use_R` case, `rap.cpp:122-126`), every subsequent `Mult`
  short-circuits to `RAP->Mult` (`rap.cpp:199-203`). Essential BCs are eliminated on the
  assembled square matrix via `RAP->EliminateBC` (`rap.cpp:143`). `StealParallelAssemble`
  (`rap.hpp:107-111`) forces assembly then moves the matrix out to a caller (used by direct
  solvers that need an explicit `HypreParMatrix`).

`EliminateRHS` (`rap.cpp:56-82`) is the BC-lifting companion: it moves the essential-dof
contribution of a known solution `x` to the right-hand side `b` (the standard `b ← b − A·x_ess`
lift), reusing the same prolongate-apply-restrict path.

## `BuildParSumOperator` — weighted summation

The header closes with a three-overload `BuildParSumOperator` template family (`rap.hpp:224-244`,
bodies `rap.cpp:764-959`, explicit instantiations `rap.cpp:961-976`) that combines a fixed-size
`std::array` of `ParOperator` (or `ComplexParOperator`) pointers into a single weighted-sum
parallel operator, optionally extracting and re-applying the essential-dof list. This is the
construction-side surface (how multiple assembled blocks — e.g. stiffness + mass + damping in
the driven/transient pipelines — fuse into one `RAP`); the per-block apply algebra is the
`SumOperator` material in [`linalg-operator-file`](./linalg-operator-file.md).

## Notes for higher layers

- **The matrix-free / assembled dual collapses at L1.** Both paths compute the same parallel
  operator action; the L1 form is the single mathematical `y = (R·A·P)·x` map. The lazy `mutable
  RAP` cache (`rap.hpp:42`) is an L0-internal memoization
  ([`mutable-workspace-pattern`](./mutable-workspace-pattern.md)) — at L1 the operator is a pure
  function of `(A, P, R)` and the assembled-vs-matrix-free choice is a performance annotation,
  not algebra.
- **`R` vs `Pᵀ` is a variant axis, not two operators.** The `use_R` flag (`rap.hpp:32`,
  `rap.cpp:363-385`) selects whether the test-side restriction is a genuine restriction matrix
  `R` or the transpose of the prolongation `Pᵀ`. For the usual square Galerkin case `R = Pᵀ`;
  the rectangular case (different trial/test spaces, e.g. discrete gradient/curl operators) uses
  the explicit `R`. At L1 this is one variant axis on the parallel-operator lift.
- **`ComplexParOperator` collapses onto `ParOperator` componentwise.** The element-type axis (per
  [`mfem-vector-types`](./mfem-vector-types.md)) is the only structural difference: the complex
  operator is two real `ParOperator`s plus the Hermitian-transpose overloads. At L1 the
  element-type axis is a variant on the operator *value*, not a separate operator family — the
  same collapse [`linalg-solver-file`](./linalg-solver-file.md) records for `Solver<OperType>`.
- **The essential-BC diagonal policy is state, not input.** `DiagonalPolicy ∈ {DIAG_ZERO,
  DIAG_ONE}` (`rap.hpp:38`, set via `SetEssentialTrueDofs`, `rap.cpp:36-47`) determines what the
  eliminated rows/cols carry. At L1 this lifts as a variant axis (or an explicit BC-set input) on
  the parallel-operator construction, the same shape as the diagonal-policy material elsewhere in
  `linalg/operator`.
- **Single-rank collapse.** `P` and `R` are the FE-space prolongation/restriction maps; at single
  rank the true-dof and L-dof spaces coincide up to the conforming-constraint map, so `R·A·P`
  collapses toward `A` modulo conforming-prolongation and BC elimination. The `MPI_Comm`
  (`rap.hpp:74`) and all `Hypre*` machinery are read single-rank per
  [`par-types-single-rank-reading`](./par-types-single-rank-reading.md).

## Referenced from

*Forward-declared. L1 work on the parallel-operator lift (the assembled-vs-matrix-free dual and
the FE-assembly pipeline, queued as FE-space material reaches the frontier) will reference this
chapter.*

- [`L0/apply-linop-overload-set`](./apply-linop-overload-set.md) — lists `ParOperator` in the
  concrete-subclass `Mult` / `MultTranspose` / `AddMult` overload family; this chapter is the
  file-level home for that member.
- [`L0/linalg-operator-file`](./linalg-operator-file.md) — the `Operator` / `ComplexOperator`
  base hierarchy `ParOperator` / `ComplexParOperator` inherit from, and the `SumOperator` algebra
  behind `BuildParSumOperator`.
- [`L0/par-types-single-rank-reading`](./par-types-single-rank-reading.md) — the `HypreParMatrix`
  / `MPI_Comm` / prolongation-restriction single-rank reading rule applied throughout.
- [`L0/mfem-vector-types`](./mfem-vector-types.md) — the real / complex element-type axis the two
  classes instantiate.
- [`L0/mutable-workspace-pattern`](./mutable-workspace-pattern.md) — the `mutable RAP` lazy-assembly
  cache pattern.
- [`L0/transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md) — the
  matrix-free-vs-assembled performance dual classification.

## Evidence (representative)

- `palace/linalg/rap.hpp:1-252` — the header file (252 lines).
- `palace/linalg/rap.hpp:14` — `namespace palace` open.
- `palace/linalg/rap.hpp:17-19` — RAP definition comment ("constructed through the actions of R,
  A, and P, usually with R = Pᵀ"); the authoritative reading.
- `palace/linalg/rap.hpp:22-23` — `// Real-valued RAP operator.` + `class ParOperator : public Operator`.
- `palace/linalg/rap.hpp:24-121` — `ParOperator` class body.
- `palace/linalg/rap.hpp:27-28` — local operator storage (`std::unique_ptr<Operator> data_A;` + `const Operator *A;`).
- `palace/linalg/rap.hpp:31-32` — trial/test `FiniteElementSpace` refs + `const bool use_R` (R-vs-Pᵀ selector).
- `palace/linalg/rap.hpp:35,38` — essential-BC `dbc_tdof_list` + `DiagonalPolicy diag_policy = DIAG_ZERO`.
- `palace/linalg/rap.hpp:42` — `mutable std::unique_ptr<mfem::HypreParMatrix> RAP;` (lazy assembled matrix).
- `palace/linalg/rap.hpp:54-67` — owning + non-owning + square-shorthand constructor overloads.
- `palace/linalg/rap.hpp:96` — `void EliminateRHS(const Vector &x, Vector &b) const;`.
- `palace/linalg/rap.hpp:100` — `mfem::HypreParMatrix &ParallelAssemble(bool skip_zeros = false) const;`.
- `palace/linalg/rap.hpp:103-111` — `StealParallelAssemble` (forces assembly, `std::move`s out the matrix).
- `palace/linalg/rap.hpp:113-120` — `AssembleDiagonal` / `Mult` / `MultTranspose` / `AddMult` / `AddMultTranspose` overrides.
- `palace/linalg/rap.hpp:123-124` — `// Complex-valued RAP operator.` + `class ComplexParOperator : public ComplexOperator`.
- `palace/linalg/rap.hpp:124-222` — `ComplexParOperator` class body.
- `palace/linalg/rap.hpp:142` — `std::unique_ptr<ParOperator> RAPr, RAPi;` (real/imag parts as owned `ParOperator`s).
- `palace/linalg/rap.hpp:175-176` — `Real()` / `Imag()` overrides returning `RAPr.get()` / `RAPi.get()`.
- `palace/linalg/rap.hpp:209,220-221` — `MultHermitianTranspose` / `AddMultHermitianTranspose` (complex-only overloads).
- `palace/linalg/rap.hpp:224-244` — the three `BuildParSumOperator` template overloads (real array, complex array, deduced-array dispatcher).
- `palace/linalg/rap.cpp:1-10` — source includes (`fem/bilinearform.hpp`, `linalg/hypre.hpp`) + `namespace palace`.
- `palace/linalg/rap.cpp:12-33` — `ParOperator` constructor chain (private delegated ctor + owning + non-owning).
- `palace/linalg/rap.cpp:36-47` — `SetEssentialTrueDofs` (binds BC dof list + diagonal policy).
- `palace/linalg/rap.cpp:56-82` — `EliminateRHS` (`b ← b − A·x_ess` lift via prolongate-apply-restrict).
- `palace/linalg/rap.cpp:84-152` — `ParallelAssemble`: dynamic-cast `A` to `HypreCSRMatrix` / `ceed::Operator` (91-101), Hypre triple product `hypre_ParCSRMatrixRAPKT(Rt, A, P)` for `R = Pᵀ` (116-117) vs explicit `R·(A·P)` for `use_R` (122-126), `EliminateBC` on assembled square matrix (143).
- `palace/linalg/rap.cpp:195-234` — `ParOperator::Mult`: assembled short-circuit (199-203), matrix-free prolongate-apply-restrict sandwich with BC handling (205-233).
- `palace/linalg/rap.cpp:236-275` — `ParOperator::MultTranspose` (adjoint sandwich).
- `palace/linalg/rap.cpp:277-361` — `ParOperator::AddMult` / `AddMultTranspose` (scalar-accumulating variants).
- `palace/linalg/rap.cpp:363-385` — `RestrictionMatrixMult` / `RestrictionMatrixMultTranspose` (the `use_R ? R : Pᵀ` selector).
- `palace/linalg/rap.cpp:387-391` — `GetTestLVector` (square-vs-rectangular L-vector workspace selection).
- `palace/linalg/rap.cpp:481-517` — `ComplexParOperator::Mult` (componentwise real/imag prolongate-restrict around one `A->Mult`).
- `palace/linalg/rap.cpp:556-593` — `ComplexParOperator::MultHermitianTranspose` (complex-only adjoint).
- `palace/linalg/rap.cpp:764-959` — `BuildParSumOperator` template bodies (real, complex, deduced-array dispatcher).
- `palace/linalg/rap.cpp:961-976` — explicit `BuildParSumOperator` instantiations (`N ∈ {1,2,3,4}`).

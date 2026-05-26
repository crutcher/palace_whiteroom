# sparse_triangular_solve

## Context

This slice was scoped to dissect a sparse triangular solve in Palace —
the forward and transpose variants, in-place vs. out-of-place
semantics, MPI Allgatherv of the factor, and the residual computation
that would characterize a correct solve. The exploration returns a
**negative result**: no such primitive exists at the Palace level. The
slice is preserved as an obstruction record so future cycles do not
re-litigate the search.

## Background

A sparse triangular solve (`Ly = b` or `Uy = b` with `L`/`U` sparse) is
the inner kernel of LU-based sparse direct solvers (Davis 2006,
*Direct Methods for Sparse Linear Systems*). In a distributed setting,
the factor's row/column distribution typically requires communication —
broadcast of pivot rows, allgatherv of dense blocks at the supernode
level, or pipelined point-to-point traffic along the elimination tree.
SuperLU_DIST, STRUMPACK, and MUMPS each implement their own scheme;
see Li 2005, Ghysels et al. 2016, and Amestoy et al. 2001 respectively.
The scope question's framing (Allgatherv on factor, residual check,
in-place vs. out-of-place workspace) is faithful to that literature.

Palace, however, sits one level up: it consumes sparse-direct factors
through thin MFEM wrappers and never touches `L`/`U` data directly.

## L0 — implementation facts

### Negative result: no Palace-level sparse triangular solve

Searches across `palace/linalg/*.{cpp,hpp}` for `triangular`, `TriSolve`,
`trsv`, `trsm`, `forward solve`, `backward solve`, `LowerTriangularSolve`,
`UpperTriangularSolve` return no implementation hits. The only
`triangular` occurrence is a comment describing a *block* lower-
triangular preconditioner (a 2×2 operator-block pattern, not a
sparse-CSR `L`-traversal) at
[palace/linalg/blockprecond.hpp:14-30](../../../../reference/palace/linalg/blockprecond.hpp#L14-L30).
The diagonal blocks of that block-triangular structure are themselves
opaque `ksp_solve`-shaped operators, not exposed factors.

### Sparse-direct factor application is opaque MFEM forwarding

Palace exposes sparse-direct solves through three thin wrapper classes:

- `palace::SuperLUSolver` inherits `mfem::Solver` and forwards
  `Mult`/`MultTranspose`/`ArrayMult`/`ArrayMultTranspose` into
  `mfem::superlu::SuperLUSolver` —
  [palace/linalg/superlu.hpp:22-60](../../../../reference/palace/linalg/superlu.hpp#L22-L60),
  [palace/linalg/superlu.cpp:83-132](../../../../reference/palace/linalg/superlu.cpp#L83-L132).
  Iterative refinement is explicitly disabled at construction
  ([palace/linalg/superlu.cpp:78](../../../../reference/palace/linalg/superlu.cpp#L78):
  `solver.SetIterativeRefine(mfem::superlu::NOREFINE)`).
- `palace::StrumpackSolverBase<T>` inherits a templated
  `mfem::STRUMPACK*Solver` and overrides only construction and
  `SetOperator` —
  [palace/linalg/strumpack.hpp:18-49](../../../../reference/palace/linalg/strumpack.hpp#L18-L49).
- `palace::MumpsSolver` inherits `mfem::MUMPSSolver` and exposes only
  construction —
  [palace/linalg/mumps.hpp:19-29](../../../../reference/palace/linalg/mumps.hpp#L19-L29).

The Palace-side bodies are literal forwards; Palace contributes no factor
data structure, no `L`/`U` storage, no row/column permutation, and no
residual computation.

### Solver interface: forward/transpose pair, no triangular-specific surface

The abstract base [palace/linalg/solver.hpp:42-65](../../../../reference/palace/linalg/solver.hpp#L42-L65)
defines four virtual methods: `Mult`, `MultTranspose`, `Mult2`,
`MultTranspose2`. The `*2` variants accept a pre-allocated scratch
residual `r` and exist for **multigrid smoothers** (Chebyshev, Jacobi)
that thread a residual buffer across recursive calls — *not* for
sparse-direct triangular-solve workspace. SuperLU/STRUMPACK/MUMPS
wrappers do not override the `*2` variants. The pair (`Mult`,
`MultTranspose`) is the entire Palace-level triangular-solve-shaped
interface.

### MPI Allgatherv is not used for factors

`Mpi::Allgatherv` at
[palace/utils/communication.hpp:337-345](../../../../reference/palace/utils/communication.hpp#L337-L345)
is invoked exactly once in the Palace codebase: at
[palace/utils/geodata.cpp:1536-1540](../../../../reference/palace/utils/geodata.cpp#L1536-L1540)
to gather per-rank edge-attribute counts during mesh setup. No call
site assembles or moves a factor (`L`, `U`, `P`, `Q`, or analogue).
Whatever Allgatherv traffic the underlying sparse-direct libraries
produce lives inside SuperLU_DIST / STRUMPACK / MUMPS — beyond the
Palace boundary and out of scope per the MPI-internals rule.

### Residual check is the caller's responsibility

In [palace/linalg/ksp.cpp:105-200](../../../../reference/palace/linalg/ksp.cpp#L105-L200),
`LinearSolver::SUPERLU`/`STRUMPACK`/`MUMPS` cases construct a wrapped
sparse-direct solver via `MakeWrapperSolver<OperType, ...>` and install
it as the **preconditioner** (`pc`) of an outer iterative method. The
outer Krylov tracks its own residual; the sparse-direct apply is one
opaque preconditioner step. No residual-of-triangular-solve check
exists at Palace level; iterative refinement (which would be a true
factor-solve-then-residual loop) is disabled.

### Small-dense near-relatives (out of scope here)

The closest in-Palace solves that aren't `ksp_solve` are small dense
factorizations on each rank: `S.fullPivLu().solve(...)` at
[palace/linalg/nleps.cpp:563](../../../../reference/palace/linalg/nleps.cpp#L563)
and `Ar.ldlt().solve(RHSr)` / `Ar.fullPivHouseholderQr().solve(RHSr)`
at [palace/models/romoperator.cpp:755-767](../../../../reference/palace/models/romoperator.cpp#L755-L767).
These are replicated-per-rank Eigen solves on the small-dense side of
the field / small-dense state split (cf. GMRES L4). They are not sparse
triangular solves; they belong to a separate prospective
`small_dense_solve` slice.

## L1 — abstract operation

### Obstruction: no L1 form exists at the Palace level

This slice **does not rotate** beyond L0. The L0→L1 lift requires an
implementation pattern that compresses into a stateful abstract
operation; there is none. The four L0 facts above collectively say:
*Palace forwards into MFEM-wrapped third-party sparse-direct factors
as opaque `ksp_solve`-shaped operators and does not see the
triangular-solve interior.*

The rotation that *does* exist for these wrappers is the absorption
into the [apply_linop](../../concepts/apply_linop.md) /
[ksp_solve](../../concepts/ksp_solve.md) concepts: a SuperLU /
STRUMPACK / MUMPS instance is a `Solver<OperType>` whose `Mult` is the
forward solve `y ← A⁻¹·x` and `MultTranspose` is the transpose solve
`y ← A⁻ᵀ·x`. That absorption is **not specific to triangular structure**
— it treats the factor as a black-box linear-operator inverse, which
is how Palace uses it.

### Contractual invariant (carry-through)

If a future slice does need to name the wrapper-level contract: given
`A` passed to `SetOperator`, `solver.Mult(x, y)` returns `y` with
`A·y ≈ x`, and `solver.MultTranspose(x, y)` returns `y` with
`Aᵀ·y ≈ x`. The factor is reused across `SetOperator` calls iff
`reorder_reuse` is true and the sparsity pattern is unchanged
([palace/linalg/superlu.cpp:83-89](../../../../reference/palace/linalg/superlu.cpp#L83-L89):
`solver.SetFact(mfem::superlu::SamePattern_SameRowPerm)`). The
invariant is contractually enforced by MFEM; Palace neither verifies
it nor exploits triangular structure within it.

## Disposition

This slice is **scoped out**. The scope question's framing (factor
Allgatherv, in-place vs. out-of-place workspace, residual check)
corresponds to **MFEM-internal / SuperLU_DIST-internal** territory, not
Palace. The slice is preserved as a negative result so future planning
does not re-explore the same ground.

### Classification: scope-out variant resolution

The negative result is itself a worked instance of the **scope-out**
path in [variant-absorption](../../concepts/variant-absorption.md):
faced with the orthogonal axis (which sparse-direct backend, plus
factor-internal traffic patterns) and the absence of any Palace-side
primitive that observes that axis, the correct rotation is *not* to
manufacture an L1 form for content Palace doesn't carry. The
[sequential-obstruction](../../concepts/sequential-obstruction.md)
concept is the L2→L3 analogue ("genuinely sequential, no global
form"); this slice exhibits the L0→L1 analogue ("genuinely external,
no Palace-level form"). Both are first-class negative outputs.

The load-bearing distinction from a partial-absorption failure: a
silent scope-out would emit an L1 form that pretends the variant
doesn't exist; this slice instead names the obstruction, cites the
opaque-forwarding evidence at L0, and points at the wrapper-level
rotation ([apply_linop](../../concepts/apply_linop.md) /
[ksp_solve](../../concepts/ksp_solve.md)) that does land in a
different slice.

Follow-ups raised by this exploration:

- A `sparse_direct_solver_wrapper` slice would more accurately name
  what Palace provides: SuperLU/STRUMPACK/MUMPS as opaque
  `ksp_solve`-shaped preconditioners. The L1 form there absorbs into
  [apply_linop](../../concepts/apply_linop.md) /
  [ksp_solve](../../concepts/ksp_solve.md) and the variant axis
  (which third-party backend) is a
  [constructed-operator](../../concepts/constructed-operators.md)
  absorption — selected at solve-construction, uniform per-apply
  surface thereafter.
- A `small_dense_solve` slice would cover the Eigen factorizations in
  `nleps.cpp` and `romoperator.cpp` — replicated-per-rank, no MPI, on
  the small-dense side of the field/small-dense split.

## Open questions

- Should this slice be renamed `sparse_direct_solver_wrapper` and
  re-pushed to L1 against the wrapper-level contract, or left as a
  pure negative-result placeholder and the wrapper slice opened as a
  separate file?
- Is there an MFEM-level or SuperLU-level slice family where
  Allgatherv-on-factor and residual-of-triangular-solve are
  first-class? The scope question's framing came from there; tagging
  this slice as out-of-scope-for-Palace and pointing at that family
  would close the loop.

# sparse_triangular_solve

> **Reduction status (cycle-013+, cross-link c029):** this slice is a **negative-result slice** (in the spirit of `concepts/negative-result-slice.md`; that concept page does not yet list this slice in its §"Examples in this spec") and is **retained in full** — it is the artifact, not redundant raw material to be lifted. It is the **canonical instance** of:
> - `book/src/concepts/scope-out-obstruction.md` §"Canonical instance" (`:68`) — the L0→L1 scope-out obstruction (Palace forwards sparse-direct solves into MFEM/SuperLU_DIST/STRUMPACK/MUMPS opaquely; no Palace-level triangular-solve form to lift).
> - `book/src/concepts/sequential-obstruction.md` §"Sub-kind: out-of-scope-obstruction" (`:53`) — the out-of-scope sub-kind distinguished from genuine L2→L3 sequential obstruction.
> - `book/src/L1-L0/triangular-solve-obstruction.md` (cycle-029) — the L1>L0 obstruction theme that is the **layered-artifact partner record** for this slice's negative result. The theme records the engineered-absence evidence (Adams 2003 polynomial-over-GS, GPU AMG GS→Jacobi flip) that postdates this slice; the two records **cross-link rather than supersede** (see the theme's §"Related" at `:273-308`). The slice's reduction status remains **annotated-and-retained**.
>
> The §L0 opaque-forwarding evidence (`superlu.{hpp,cpp}`, `strumpack.hpp`, `mumps.hpp`, `communication.hpp`/`geodata.cpp`, `blockprecond.hpp`) is the citation grounding for those concept pages. There is — by construction — NO firm L0–L4 entry this slice's material lifts *into*; a negative result has no positive form to absorb. Per the `polynomial_recurrence_step.md` precedent ("the slice IS the artifact"), the corpus-reduction policy treats this slice as **annotated-and-retained**, not pending-lift.
>
> **Live OQs (unchanged):** rename to `sparse_direct_solver_wrapper` + re-push to L1 against the wrapper-level contract (§Open questions); whether an MFEM/SuperLU-level slice family owns the factor-Allgatherv / residual-of-triangular-solve framing.

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

## Methodological status

This slice is the canonical worked instance of the **L0→L1 scope-out
obstruction** — the L0→L1 analogue of
[sequential-obstruction](../../concepts/sequential-obstruction.md)'s
L2→L3 negative result. The pattern:

1. A scope question is posed naming primitives/state that would exist
   at a *lower system boundary* (here: factor storage, factor-internal
   MPI traffic, residual-of-triangular-solve).
2. The L0 dissection finds no in-codebase implementation of those
   primitives — only thin opaque forwarders into a third-party
   library that owns the named machinery internally.
3. The L1 rotation that *would* apply at the wrapper boundary is
   **not specific** to the scope question's framing (here: absorption
   into [apply_linop](../../concepts/apply_linop.md) /
   [ksp_solve](../../concepts/ksp_solve.md) treats the factor as a
   black-box linear-operator inverse, indifferent to triangular
   structure).
4. The correct output is a **negative L1 result with named
   wrapper-level carry-through**, not a manufactured L1 form for
   content the codebase doesn't carry.

The load-bearing distinction from a silent-partial-absorption
failure (cf. [variant-absorption](../../concepts/variant-absorption.md)):
this slice **discloses** the obstruction at L1, cites opaque-forwarding
evidence at L0, and forward-points at the wrapper-level rotation that
does land elsewhere. Future scope questions that share this shape
— "dissect a primitive whose implementation lives below the
codebase boundary" — should produce this same shape of slice rather
than an empty L1 or a fabricated abstraction.

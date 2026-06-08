# Convention — `Par*` types and the single-rank reading

A reference note for L1 / L2 / L4 entries that touch MFEM's `Par*` (parallel) type family. Per `CLAUDE.md` "Scope", MPI / multi-rank distribution is out of scope; this chapter records what that means concretely — which MFEM types are `Par*`, where Palace touches them, and what each one collapses to under the single-rank reading rule.

This chapter is the **dedicated companion** to [`mfem-vector-types`](./mfem-vector-types.md) §"The `Par*` axis", which currently treats the rule in a single paragraph as part of the element-type story. As `Par*` references multiply across higher-layer chapters, the rule itself benefits from its own anchor.

## The rule

> **Read each `mfem::Par<Foo>` as `mfem::<Foo>` running on a single rank.**

Concretely, under the single-rank reading:

- `ParMesh` collapses to `Mesh` — no partition boundary, no ghost layers, no `MPI_Comm` interaction. The mesh as a single connected domain on one process.
- `ParFiniteElementSpace` collapses to `FiniteElementSpace` — no `Prolongation` / `Restriction` operator (or they're identity), no shared-dof bookkeeping.
- `ParGridFunction` collapses to `GridFunction` — a single vector of dof values, no exchange of shared-dof contributions.
- `ParBilinearForm` collapses to `BilinearForm` — local assembly only, no `ParallelAssemble` step adding off-diagonal contributions from neighboring ranks.
- `HypreParVector` / `HypreParMatrix` collapse to their dense / serial equivalents (`Vector` / sparse matrix) — no inter-process row partitioning, no off-diagonal blocks.
- `MPI_Comm` parameters reduce to a no-op: `MPI_COMM_WORLD` and `MPI_COMM_SELF` both have size 1; collectives (`MPI_Allreduce`, `MPI_Bcast`) reduce to identity over a single element.
- `Mpi::Print(comm, …)` (Palace's wrapper at `palace/utils/communication.hpp:347-360`) is unconditionally a print since `Mpi::Root(comm)` is always true on a single rank.

The rule is **uniform** — there is no `Par*` type Palace touches that requires a non-trivial single-rank reading. The single-rank reading erases all MPI structure without algorithmic loss to the algebra Palace expresses.

## What Palace touches

The `Par*` surface in Palace's tree is concentrated in three regions:

**`palace/fem/`** — finite-element-discretization layer; 81 grep-hits of `Par*` types. Representative anchors:

- `palace/fem/fespace.hpp:19-25` — `palace::FiniteElementSpace` is a thin wrapper over a `mfem::ParFiniteElementSpace` member (`fespace`, line 25). The wrapper's interface (the `Get()` accessors at `palace/fem/fespace.hpp:78-82`, the `GetParMesh()` at lines 90-91) routes through the MFEM `ParFiniteElementSpace`'s methods; under the single-rank reading, the wrapped object is a `FiniteElementSpace` and the `Par`-prefixed names re-read as the serial equivalents.
- `palace/fem/interpolator.hpp:34` — `InterpolationOperator::ProbeField` takes `const mfem::ParGridFunction &U` and computes interpolated field values at probe locations. The interpolation kernel (`palace/fem/interpolator.cpp:81-111`) is local to the rank owning the probe point; under single-rank reading the partitioning bookkeeping disappears.
- `palace/fem/coefficient.hpp:89, 93, 168, 175` — `BdrSurfaceCurrentVectorCoefficient` and `BdrSurfaceFluxCoefficient` hold `const mfem::ParGridFunction &` / `*` field references that they evaluate at boundary integration points.
- `palace/fem/coefficient.hpp:326` — `GetLocalVectorValue` extracts a single dof-vector entry from a `mfem::ParGridFunction`; the "local" prefix is the single-rank semantics already named in MFEM.

**`palace/models/`** — solver-pipeline layer; 9 grep-hits. Representative anchors:

- `palace/models/laplaceoperator.cpp:230` — `mfem::ParGridFunction x(&GetH1Space().Get());` constructs an `H1`-space scalar field for an electrostatic pipeline computation.
- `palace/models/waveportoperator.cpp:48-49` — `GetEssentialTrueDofs(mfem::ParGridFunction &E0t, mfem::ParGridFunction &E0n, mfem::ParGridFunction &port_E0t, mfem::ParGridFunction &port_E0n, …)` — boundary-mode field extraction for wave-port pipelines.
- `palace/models/surfacepostoperator.cpp:108-109` — `SurfacePostOperator::SurfaceFluxData::GetCoefficient(const mfem::ParGridFunction *E, const mfem::ParGridFunction *B, …)` — post-processing flux computation.

**`palace/linalg/`** — auxiliary preconditioner construction (the linalg interior itself uses `Vector` / `ComplexVector` / `Operator` / `ComplexOperator` — see [`mfem-vector-types`](./mfem-vector-types.md), [`linalg-operator-file`](./linalg-operator-file.md)). The `Par*` touches here are confined to one preconditioner family:

- `palace/linalg/ams.hpp:39` — `std::unique_ptr<mfem::HypreParVector> x, y, z;` workspace members for the AMS (auxiliary-space-Maxwell) preconditioner.
- `palace/linalg/ams.cpp:74` — `mfem::ParGridFunction x_coord(&h1_fespace.Get()), y_coord(&h1_fespace.Get()), …;` — Cartesian-coordinate grid functions assembled into the AMS preconditioner's near-null-space basis.

There is also one significant single-file home for the `ParOperator` Palace class itself (not an MFEM type, but a Palace class named for the pattern) — `palace/linalg/rap.{hpp,cpp}` (see [`apply-linop-overload-set`](./apply-linop-overload-set.md) for the operator-hierarchy view; [`linalg-operator-file`](./linalg-operator-file.md) for the file-level overview).

## MPI collectives and the `palace::Mpi` namespace

The same single-rank reading applies to MPI collective calls. Palace's `Mpi` class at `palace/utils/communication.hpp:181-425` collects the collective wrappers used across the tree:

- `Mpi::GlobalSum(len, buff, comm)` at `palace/utils/communication.hpp:265-270` — `MPI_Allreduce` with `MPI_SUM` in-place. Used inside `linalg::GlobalSize` (`palace/linalg/vector.hpp:204`), `linalg::Dot` (`palace/linalg/vector.hpp:251`), `linalg::Sum` (`palace/linalg/vector.hpp:281, 292`).
- `Mpi::GlobalMin`, `Mpi::GlobalMax`, `Mpi::GlobalMinLoc`, `Mpi::GlobalMaxLoc`, `Mpi::GlobalOr`, `Mpi::GlobalAnd` — same shape, different reduction ops. `palace/utils/communication.hpp:251-318`.
- `Mpi::Broadcast`, `Mpi::Allgather`, `Mpi::Allgatherv` — non-reduction collectives at `palace/utils/communication.hpp:320-344`.
- `Mpi::Print`, `Mpi::Printf`, `Mpi::Warning` at `palace/utils/communication.hpp:347-389` — rank-gated formatted-print wrappers; the gate is `if (Root(comm))` (line 350).

Under the single-rank reading, all `GlobalOp(len, buff, MPI_*, comm)` reduce to identity — the in-place buffer is unchanged. `Broadcast` and `Allgather` likewise reduce to identity (or to a `memcpy` for `Allgather` with the recvbuf as source). `Print` is unconditionally a print.

The L1 lift of, e.g., `LocalDot` followed by `Mpi::GlobalSum` (the `Dot` pattern at `palace/linalg/vector.hpp:248-251`) collapses the two-step "local-reduce-then-collective" into a single global reduction; the single-rank reading makes the second step a no-op, but the L1 form names the global reduction directly (per [`L1/dot`](../L1/dot.md)).

## What single-rank reading does **not** mean

It does **not** mean:

- **Erasing `Par*` from the L0 citation.** L0 cites Palace source verbatim. Where a Palace function takes `const mfem::ParGridFunction &`, the L0 citation reads `mfem::ParGridFunction`. The single-rank reading happens at L1 (the lift), not at L0 (the citation).
- **Asserting Palace is correct for multi-rank.** This project does not validate multi-rank semantics. If a multi-rank distribution would change behavior (e.g., reduction-tree non-associativity, see [`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md)), the single-rank reading would mask that. The trade-off is recorded in `scaffolding/decisions/` (the MPI-out-of-scope decision is the longest-standing).
- **Removing MFEM's `ParFiniteElementSpace` from the construction sequence.** Palace constructs `palace::FiniteElementSpace` (which wraps `mfem::ParFiniteElementSpace`) regardless. The single-rank reading reads the wrapped object as a serial `FiniteElementSpace` for purposes of expressing semantics in L1 / higher; the construction itself is part of the L0 citation.

## Test coverage

Tests under `palace/test/unit/` use the same `Par*` types as the production code; they configure `MPI_COMM_WORLD` from `Mpi::World()` (`palace/utils/communication.hpp:392`) and rely on the Catch2 test runner being launched with MPI initialized. Specific examples:

- `palace/test/unit/test-rap.cpp:24` — `TEST_CASE("BuildParSumOperator", "[rap][Serial][Parallel]")` — the `[Serial][Parallel]` Catch2 tag indicates the test runs in both single-rank and multi-rank configurations.
- `palace/test/unit/test-rap.cpp:31` — `auto comm = Mpi::World();` — the test uses `MPI_COMM_WORLD` via Palace's wrapper.
- `palace/test/unit/test-rap.cpp:34-37` — explicit single-rank-vs-multi-rank handling: if the initial mesh has fewer elements than ranks, the test refines until `mfem_mesh.GetNE() >= Mpi::Size(comm)` to avoid empty partitions. **The test itself encodes the single-rank reading rule**: for `Mpi::Size(comm) == 1`, the `while` loop runs zero iterations and the mesh is used directly.
- `palace/test/unit/test-rap.cpp:50-89` — `SECTION("ParOperator")` constructs `ParOperator` wrappers via `std::make_unique<ParOperator>(da.Assemble(skip_zeros), nd_fes)` (line 62) and verifies that `BuildParSumOperator` produces the correct weighted sum. Under single-rank reading the `ParOperator` wrapping is identity and the test reduces to "the weighted sum of `Mult` actions matches the sum-operator's `Mult` action".
- `palace/test/unit/test-rap.cpp:91-133` — `SECTION("ComplexParOperator")` does the same for the complex-element-type axis.

These tests are L0-equivalent semantic evidence for both the `ParOperator` / `ComplexParOperator` algebra **and** the single-rank reading rule itself — the Catch2 `[Serial]` tag explicitly authorizes the rule.

## Notes for higher layers

- **L1 / L2 / L4 operator entries should reference this chapter** when their L0 citation mentions a `Par*` type and they propose to read it as a single-rank equivalent. The rule does not need to be re-stated per entry; a one-line reference suffices.
- **The `Par*` axis is orthogonal to the element-type axis.** A `ParOperator` is real, a `ComplexParOperator` is complex; both collapse to their single-rank equivalents under this rule. The element-type axis collapse is in [`mfem-vector-types`](./mfem-vector-types.md).
- **The `palace::Mpi` namespace is an L0 surface, not an L1 surface.** L1 names global reductions directly (`Dot`, `Norml2`, `GlobalSize`); the L1>L0 lowering reintroduces the local-then-collective split. Under single-rank reading the collective is a no-op, but L1 still names the global form.
- **Where multi-rank semantics would matter**, file an open question rather than asserting equivalence. Two candidates that have surfaced: (a) reduction-tree non-associativity for `linalg::Sum` over a complex vector with cancellation, and (b) `HypreBoomerAMG` coarsening heuristics that depend on the global matrix's sparsity (the single-rank coarsening may differ from the multi-rank coarsening).

## Dependencies

- [`mfem-vector-types`](./mfem-vector-types.md) — the element-type axis; together with this chapter, the two cover the full vector-typing convention surface.
- [`apply-linop-overload-set`](./apply-linop-overload-set.md) — the operator-hierarchy view; `ParOperator` and `ComplexParOperator` are concrete subclasses there.
- [`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md) — the cross-cutting trick-classification methodology; reduction-tree non-associativity (the canonical multi-rank load-bearing concern) is listed there.

## Referenced from

- [`L0/mfem-vector-types`](./mfem-vector-types.md) — sibling reference note (element-type axis).
- [`L0/apply-linop-overload-set`](./apply-linop-overload-set.md) — sibling reference note (operator-hierarchy view).
- Higher-layer L1 / L2 / L4 entries that touch `Par*` types: `L1/` operator entries citing `Par*` types inline reference this chapter for the single-rank reading rule.

## Evidence (representative)

- `palace/fem/fespace.hpp:19-25` — `palace::FiniteElementSpace` wraps `mfem::ParFiniteElementSpace`; the wrapped object is the load-bearing member.
- `palace/fem/fespace.hpp:78-82` — `Get()` accessors returning the wrapped `mfem::ParFiniteElementSpace`.
- `palace/fem/fespace.hpp:90-91` — `GetParMesh()` accessor for the underlying `mfem::ParMesh`.
- `palace/fem/interpolator.hpp:34, 61-64` — `InterpolationOperator::ProbeField` signatures taking `const mfem::ParGridFunction &`.
- `palace/fem/interpolator.cpp:81, 309` — `ProbeField` and `InterpolateField` implementations.
- `palace/fem/coefficient.hpp:89, 93, 168, 175, 326` — `BdrSurface*Coefficient` classes holding `mfem::ParGridFunction` references.
- `palace/linalg/ams.hpp:39` — `std::unique_ptr<mfem::HypreParVector> x, y, z;` workspace members of AMS preconditioner.
- `palace/linalg/ams.cpp:74` — `mfem::ParGridFunction x_coord(&h1_fespace.Get()), y_coord(&h1_fespace.Get()), …;` near-null-space basis construction.
- `palace/models/laplaceoperator.cpp:230` — `mfem::ParGridFunction x(&GetH1Space().Get());` electrostatic-pipeline field construction.
- `palace/models/waveportoperator.cpp:48-49` — `GetEssentialTrueDofs(mfem::ParGridFunction &E0t, mfem::ParGridFunction &E0n, …)` boundary-mode field signature.
- `palace/models/surfacepostoperator.cpp:108-109` — `SurfaceFluxData::GetCoefficient(const mfem::ParGridFunction *E, const mfem::ParGridFunction *B, …)`.
- `palace/utils/communication.hpp:181-425` — `palace::Mpi` class wrapping MPI primitives.
- `palace/utils/communication.hpp:244-249` — `Mpi::GlobalOp` template `MPI_Allreduce` wrapper.
- `palace/utils/communication.hpp:265-270` — `Mpi::GlobalSum` specialisation.
- `palace/utils/communication.hpp:251-263` — `Mpi::GlobalMin`, `Mpi::GlobalMax`.
- `palace/utils/communication.hpp:272-318` — `Mpi::GlobalMinLoc`, `Mpi::GlobalMaxLoc`, `Mpi::GlobalOr`, `Mpi::GlobalAnd`.
- `palace/utils/communication.hpp:320-344` — `Mpi::Broadcast`, `Mpi::Allgather`, `Mpi::Allgatherv`.
- `palace/utils/communication.hpp:347-389` — `Mpi::Print`, `Mpi::Printf`, `Mpi::Warning` (rank-gated).
- `palace/utils/communication.hpp:392` — `Mpi::World()` returning `MPI_COMM_WORLD`.
- `palace/linalg/vector.hpp:201-214` — `linalg::GlobalSize` / `linalg::GlobalSize2` — `Mpi::GlobalSum` wrapped over a single-vector-size accumulation.
- `palace/linalg/vector.hpp:248-251` — the `LocalDot`-then-`Mpi::GlobalSum` two-step that L1's `Dot` collapses to a single global reduction.
- `palace/test/unit/test-rap.cpp:24` — `[Serial][Parallel]` Catch2-tagged test verifying `ParOperator` algebra in both single-rank and multi-rank configurations.
- `palace/test/unit/test-rap.cpp:31-37` — single-rank-vs-multi-rank conditional mesh refinement.
- `palace/test/unit/test-rap.cpp:50-89` — `ParOperator` `SECTION` verifying `BuildParSumOperator` weighted-sum algebra.
- `palace/test/unit/test-rap.cpp:91-133` — `ComplexParOperator` `SECTION` (element-type-axis dual).

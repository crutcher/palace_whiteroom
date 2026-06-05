# File — `palace/utils/communication.hpp` (`palace::Mpi` collectives and `mpi::DataType`)

A reference note for L1 / L2 / L4 entries that touch Palace's MPI surface. `palace/utils/communication.hpp` is a 429-line header-only file housing the entire MPI wrapping layer Palace uses: a `palace::mpi::` namespace of `MPI_Datatype` template specializations for the C++ scalar/aggregate types Palace reduces over, and a `palace::Mpi` singleton class that wraps `MPI_Init` / `MPI_Allreduce` / `MPI_Bcast` / `MPI_Allgather` / `MPI_Barrier` / `MPI_Abort` plus the rank-gated `Print` / `Warning` formatters.

The file is the **single anchor** for every MPI collective Palace performs; there is no scattered `MPI_Allreduce` use in the linalg or models tree, only `Mpi::GlobalSum` / `Mpi::GlobalMin` / `Mpi::GlobalMax` calls into this file. This concentration is what makes the [`par-types-single-rank-reading`](./par-types-single-rank-reading.md) rule clean — the rule collapses the wrapping to identity in one place.

This chapter is the **file-level companion** to [`par-types-single-rank-reading`](./par-types-single-rank-reading.md) §"MPI collectives and the `palace::Mpi` namespace". The convention chapter states the single-rank reading rule; this chapter catalogues the file's structure (the `Mpi` class layout, the `mpi::DataType` specialisation set, the call-site distribution) so that L1 operator entries that lift `Mpi::GlobalSum`-shaped patterns can anchor here for the file-level view and to `par-types-single-rank-reading` for the algebraic-collapse rule.

## File structure

`communication.hpp` is organised into two top-level units inside `namespace palace`:

- **`palace::mpi::` namespace** (`palace/utils/communication.hpp:17-174`) — type-discovery layer. Holds the `DataType<T>()` function template (line 20-21) plus 22 explicit specialisations spanning C++ integer types (`char`, `signed char`, `unsigned char`, `short`/`unsigned short`, `int`/`unsigned int`, `long`/`unsigned long`, `long long`/`unsigned long long`), floating-point types (`float`, `double`, `long double`), three complex types (`std::complex<float>`, `std::complex<double>`, `std::complex<long double>`), `bool`, and six `ValueAndLoc<T, U>` aggregates (`palace/utils/communication.hpp:131-172`) for the `MPI_MINLOC`/`MPI_MAXLOC` reductions that return both the value and its global index. Each specialisation returns the corresponding `MPI_Datatype` constant (e.g. `MPI_DOUBLE`, `MPI_C_DOUBLE_COMPLEX`, `MPI_FLOAT_INT`). This template-dispatch layer is the surface that lets `Mpi::GlobalSum<T>(len, buff, comm)` be type-generic over any element type Palace might reduce.

- **`palace::Mpi` class** (`palace/utils/communication.hpp:181-425`) — the convenience wrapper class. Private constructor + `Instance()` singleton accessor (`palace/utils/communication.hpp:401-411`) — the class exists to namespace static methods, not to hold instance state; the singleton purely exists so `MPI_Finalize` is called on program exit via the destructor. All collective/reduction methods are `static` template functions inlined into the header. The class is modelled on `mfem::Mpi` but cannot inherit from it because MFEM's constructor is private rather than protected (per the comment block at `palace/utils/communication.hpp:176-180`).

## The `Mpi` class surface

The class has five concern groups:

**Lifecycle and rank queries** (`palace/utils/communication.hpp:183-242`):

- `Init(argc, argv, requested)` (lines 185-192, 413-424) — wraps `MPI_Init_thread`; the singleton `Instance()` is constructed inside `Init` so its destructor's `MPI_Finalize` runs at program exit. Default thread-support level is `MPI_THREAD_FUNNELED` if `MFEM_USE_OPENMP` is defined, else `MPI_THREAD_SINGLE` (`palace/utils/communication.hpp:394-399`).
- `Finalize()` (lines 194-201) — calls `MPI_Finalize` if MPI is initialised and not yet finalised.
- `IsInitialized()` / `IsFinalized()` (lines 203-217) — boolean queries on `MPI_Initialized` / `MPI_Finalized`.
- `Abort(code, comm)` (line 220) — `MPI_Abort` wrapper.
- `Barrier(comm)` (line 223) — `MPI_Barrier` wrapper.
- `Rank(comm)` (lines 225-231), `Size(comm)` (lines 233-239), `Root(comm)` (line 242) — communicator-rank queries. `Root` returns `Rank(comm) == 0`.

**Reduction collectives** — the central group (`palace/utils/communication.hpp:244-318`):

- `GlobalOp<T>(len, buff, op, comm)` (lines 244-249) — the generic `MPI_Allreduce` wrapper with `MPI_IN_PLACE`. The shape `(len, buff, op, comm)` is uniform across all reduction wrappers; the `op` parameter is an `MPI_Op` constant.
- `GlobalMin<T>(len, buff, comm)` (lines 251-256) — `MPI_MIN` specialisation.
- `GlobalMax<T>(len, buff, comm)` (lines 258-263) — `MPI_MAX` specialisation.
- `GlobalSum<T>(len, buff, comm)` (lines 265-270) — `MPI_SUM` specialisation. **The most-used collective in Palace** (42 call sites across the tree; see "Call-site distribution" below).
- `GlobalMinLoc<T, U>(len, val, loc, comm)` (lines 272-288) — `MPI_MINLOC` with parallel `val` and `loc` arrays. Internally allocates a `std::vector<mpi::ValueAndLoc<T, U>>` buffer (line 276), packs the inputs, calls `GlobalOp`, unpacks the results. Same buffer-marshalling shape for `GlobalMaxLoc`.
- `GlobalMaxLoc<T, U>(len, val, loc, comm)` (lines 290-306) — `MPI_MAXLOC` parallel of `GlobalMinLoc`.
- `GlobalOr(len, buff, comm)` (lines 308-312) — `MPI_LOR` over `bool` arrays.
- `GlobalAnd(len, buff, comm)` (lines 314-318) — `MPI_LAND` over `bool` arrays.

**Non-reduction collectives** (`palace/utils/communication.hpp:320-344`):

- `Broadcast<T>(len, buff, root, comm)` (lines 320-325) — `MPI_Bcast` wrapper.
- `Allgather<T>(sendcount, sendbuf, recvbuf, comm)` (lines 327-334) — fixed-count `MPI_Allgather`; every rank ends up with a `recvbuf` of size `sendcount * Size(comm)`.
- `Allgatherv<T>(sendcount, sendbuf, recvbuf, recvcounts, displs, comm)` (lines 336-344) — variable-count `MPI_Allgatherv` with per-rank `recvcounts`/`displs` arrays.

**Rank-gated formatted printing** (`palace/utils/communication.hpp:346-389`):

- `Print<T...>(comm, fmt, args...)` (lines 347-360) — `fmt::print` wrapper gated by `if (Root(comm))` (line 350). Two overloads: one taking an explicit `comm`, one defaulting to `World()`.
- `Printf<T...>(comm, format, args...)` (lines 362-375) — `fmt::printf` variant; same root-gating shape.
- `Warning<T...>(comm, fmt, args...)` (lines 377-389) — composes a yellow "--> Warning!" header (`fmt::styled` with `fmt::fg(fmt::color::yellow)`, line 380) followed by the user message via `Print`.

**Communicator default** (`palace/utils/communication.hpp:391-392`):

- `World()` returns `MPI_COMM_WORLD` as the default communicator for the no-`comm` overloads of `Print`/`Printf`/`Warning`/`Abort`/`Barrier`.

## Call-site distribution

A full grep of `reference/palace/palace/` finds **42 `Mpi::GlobalSum` call sites** and **36 `Mpi::GlobalMin` / `Mpi::GlobalMax` call sites combined**, plus a small number of `Mpi::Broadcast` / `Mpi::Allgather` calls. The distribution clusters into three regions:

**`palace/linalg/`** — the central use is in `vector.hpp`'s free-function namespace and in `orthog.hpp`'s orthogonalization helpers:

- `palace/linalg/vector.hpp:204` — `Mpi::GlobalSum(1, &N, comm)` inside `linalg::GlobalSize` (global vector size).
- `palace/linalg/vector.hpp:214` — `Mpi::GlobalSum(2, N, comm)` inside `linalg::GlobalSize2` (two-vector size pair).
- `palace/linalg/vector.hpp:251` — `Mpi::GlobalSum(1, &dot, comm)` inside `linalg::Dot` after `LocalDot`. **This is the canonical local-then-collective pattern** that L1's [`dot`](../L1/dot.md) names as a single global reduction.
- `palace/linalg/vector.hpp:281` — `Mpi::GlobalSum(1, &sum, comm)` inside `linalg::Sum`.
- `palace/linalg/vector.hpp:292` — `Mpi::GlobalSum(2, sum, comm)` inside `linalg::Mean` (two-element `(local_sum, local_count)` reduction).
- `palace/linalg/orthog.hpp:50` — `Mpi::GlobalSum(1, &H[j], comm)` inside `OrthogonalizeColumnMGS` (per-vector modified Gram-Schmidt inner-product reduction).
- `palace/linalg/orthog.hpp:70` — `Mpi::GlobalSum(m, H, comm)` inside `OrthogonalizeColumnCGS` (classical Gram-Schmidt; reduces the full m-vector at once, which is the algebraic distinction from MGS — see [`orthogonalization`](../concepts/orthogonalization.md)).
- `palace/linalg/orthog.hpp:82` — `Mpi::GlobalSum(m, dH.data(), comm)` inside the refinement step (CGS2) of `OrthogonalizeColumnCGS`.
- `palace/linalg/divfree.cpp:64, 69` — `Mpi::GlobalSum` / `Mpi::GlobalMin` for boundary-tdof count and root rank discovery during divergence-free projection construction.
- `palace/linalg/iterative.cpp` — uses `Mpi::Print` (not `GlobalSum`) for per-iteration residual logging; the iterative solver delegates its reductions through `linalg::Dot` / `linalg::Norml2`.

**`palace/models/`** — post-processing and solver-construction:

- `palace/models/surfacepostoperator.cpp:320, 343, 411, 412` — surface-flux post-processing reductions (`Mpi::GlobalSum` over local element contributions).
- `palace/models/domainpostoperator.cpp:230, 249, 273, 295` — domain-energy post-processing reductions.
- `palace/models/spaceoperator.cpp:374, 416, 450, 490, 689, 723, 750, 810, 1063, 1101` — operator-construction sanity reductions (`Mpi::GlobalMin` over an "empty" flag to detect whether any rank has an empty boundary; `Mpi::GlobalSum` for total nnz).
- `palace/models/laplaceoperator.cpp:208` — same pattern.
- `palace/models/romoperator.hpp:121` — ROM inner-product reduction.

**Additional sites** in `palace/utils/{timer.hpp,memoryreporting.cpp,dorfler.cpp,geodata.cpp}`, `palace/drivers/{basesolver.cpp,boundarymodesolver.cpp}`, and `palace/fem/errorindicator.hpp` cover instrumentation reductions (counters, memory statistics, mesh statistics, error indicators). These have the same shape as the `linalg/` and `models/` call sites — a `len` element scalar buffer reduced in place — and collapse identically under the single-rank reading. Not enumerated per-site because they are uniformly transparent.

## Algebraic content under single-rank reading

Per [`par-types-single-rank-reading`](./par-types-single-rank-reading.md) §"MPI collectives and the `palace::Mpi` namespace", every `Mpi::Global*(len, buff, op, comm)` call reduces to identity under the single-rank reading (the buffer is unchanged because `MPI_Allreduce` over a single element under any associative `MPI_Op` returns that element). `Broadcast` and `Allgather` similarly collapse to identity (the receive buffer equals the send buffer up to a memcpy). `Print` is unconditionally a print since `Root(comm)` is always true on a single rank.

The **algebraic content** of the L0 calls is therefore exactly what the local-step computes — `LocalDot(x, y)` for `linalg::Dot`, `LocalSum(x)` for `linalg::Sum`, the modified-Gram-Schmidt inner product for `OrthogonalizeColumnMGS`. The collective wrapping is an L0 surface artifact, erased uniformly at L1.

Two cases where the single-rank reading could in principle mask multi-rank behaviour are listed in `par-types-single-rank-reading` and tracked in `scaffolding/decisions/`: reduction-tree non-associativity for floating-point sums with cancellation, and any reduction op whose multi-rank result differs from the trivial single-element identity (none exists in the `MPI_SUM` / `MPI_MIN` / `MPI_MAX` / `MPI_LOR` / `MPI_LAND` / `MPI_MINLOC` / `MPI_MAXLOC` set actually used).

## Test coverage

There is **no dedicated `test-communication.cpp`** under `palace/test/unit/`. The collective wrappers are exercised indirectly through every test that calls `linalg::Dot`, `linalg::Norml2`, or any orthogonalization helper:

- `palace/test/unit/test-orthog.cpp` — exercises `OrthogonalizeColumnMGS`, `OrthogonalizeColumnCGS`, and the CGS2 refinement path; each call triggers an `Mpi::GlobalSum` (or several). The test runs in both `[Serial]` and `[Parallel]` Catch2 tag configurations, which is the canonical empirical authority for the single-rank reading rule: the same algebraic claim holds under both `Mpi::Size(comm) == 1` and `Mpi::Size(comm) > 1`.
- `palace/test/unit/test-rap.cpp:24-37` — the `[Serial][Parallel]`-tagged test uses `Mpi::World()` and `Mpi::Size(comm)` explicitly to determine whether to refine the mesh; the test body is identical across the two configurations.

The `Mpi::Print` / `Mpi::Printf` / `Mpi::Warning` formatters have no direct test coverage; they are exercised end-to-end via integration tests that capture stdout.

## Notes for higher layers

- **L1 operators that name a global reduction** (`dot`, `nrm2`, `axpy` chained with `dot`, …) anchor their L0 citation through `linalg::Dot` / `linalg::Norml2` (in [`linalg-vector-file`](./linalg-vector-file.md)) and via that path through `Mpi::GlobalSum` in this file. The L1 form does not name `Mpi::GlobalSum` directly — it names `Dot(comm, x, y)` and the `Mpi::GlobalSum` wrapping is an L0 implementation detail.
- **The local-then-collective pattern** (`auto v = LocalOp(x); Mpi::GlobalSum(1, &v, comm); return v;`) is the **uniform shape** for scalar reductions across Palace. It appears in `vector.hpp:248-252` (`Dot`), `vector.hpp:278-283` (`Sum`), `orthog.hpp:46-52` (MGS), and the post-processing operators. L2's "global-reduction" combinator would name this pattern once.
- **The `m`-vector CGS reduction** (`orthog.hpp:70`'s `Mpi::GlobalSum(m, H, comm)`) is **algebraically distinct** from a loop of single-element reductions — it reduces all `m` inner products in one collective call, which trades latency for one round-trip instead of `m`. This is a transparent performance trick at L0 / L1 (the algebraic result is the same), but it is the load-bearing distinction between MGS and CGS in the latency-bound regime. Recorded in [`orthogonalization`](../concepts/orthogonalization.md) (the firm collective-shape home).
- **The `Mpi::Print` family is L0 instrumentation**, not algorithm. L1 / L2 / L4 entries do not lift the per-iteration residual prints (`iterative.cpp:424` etc.) — they are erased as transparent.
- **`Mpi::Warning` may not be transparent.** The convergence-failure warning at `palace/linalg/ksp.cpp:303-306` (inside `BaseKspSolver::Mult`) emits a runtime warning when the inner Krylov iteration fails to reach the tolerance. The L1 lift would name this as a `Result<…, ConvergenceFailure>` shape (per [`L1/ksp_solve`](../L1/ksp_solve.md)) rather than a side-effecting warning. The semantics of "what does the solver return on failure" is load-bearing.

## Dependencies

- [`par-types-single-rank-reading`](./par-types-single-rank-reading.md) — the convention chapter that states the algebraic-collapse rule; this chapter is its file-level companion.
- [`linalg-vector-file`](./linalg-vector-file.md) — the primary downstream caller of `Mpi::GlobalSum` (via `linalg::Dot` / `linalg::Norml2` / `linalg::Sum` / `linalg::Mean`).
- [`linalg-free-functions`](./linalg-free-functions.md) — the wrapping convention that hides the local-then-collective pattern behind the free-function surface.

## Referenced from

- [`L0/par-types-single-rank-reading`](./par-types-single-rank-reading.md) — convention chapter; this file is the file-level companion to its "MPI collectives" section.
- [`L0/linalg-vector-file`](./linalg-vector-file.md) — file-overview that downstream cites `Mpi::GlobalSum` as the implementation primitive behind `linalg::Dot` / `linalg::Norml2`.
- Higher-layer L1 / L2 / L4 entries (forward-target): every L1 operator that performs a global reduction ([`dot`](../L1/dot.md), [`nrm2`](../L1/nrm2.md), `axpy`-chained reductions, and the matrix-weighted [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) / [`bilinear-form`](../L1/bilinear-form.md)) anchors here for the L0 implementation primitive. The cycle-005+ retroactive-thinning sweep (priority #11) will rewrite inline `Mpi::GlobalSum` mentions in L1 entries to reference this chapter.

## Evidence (representative)

- `palace/utils/communication.hpp:1-429` — the file itself (429 lines, header-only).
- `palace/utils/communication.hpp:17-174` — `palace::mpi::` namespace (`DataType<T>` template + 22 specialisations + `ValueAndLoc<T, U>` aggregate).
- `palace/utils/communication.hpp:20-21` — `template <typename T> inline MPI_Datatype DataType();` primary template declaration.
- `palace/utils/communication.hpp:23-129` — scalar-type `DataType` specialisations (`char`, integer types, floating-point types, complex types, `bool`).
- `palace/utils/communication.hpp:131-136` — `ValueAndLoc<T, U>` aggregate (val + loc pair for `MINLOC`/`MAXLOC` reductions).
- `palace/utils/communication.hpp:138-172` — `ValueAndLoc` `DataType` specialisations (six combinations of value type and index type).
- `palace/utils/communication.hpp:176-180` — comment block explaining why `Mpi` does not inherit from `mfem::Mpi`.
- `palace/utils/communication.hpp:181-425` — `palace::Mpi` class definition.
- `palace/utils/communication.hpp:185-192` — `Init` static method overloads.
- `palace/utils/communication.hpp:194-201` — `Finalize` static method.
- `palace/utils/communication.hpp:203-217` — `IsInitialized` / `IsFinalized` queries.
- `palace/utils/communication.hpp:220` — `Abort(code, comm)`.
- `palace/utils/communication.hpp:223` — `Barrier(comm)`.
- `palace/utils/communication.hpp:225-242` — `Rank` / `Size` / `Root` queries.
- `palace/utils/communication.hpp:244-249` — `GlobalOp<T>` generic `MPI_Allreduce` wrapper.
- `palace/utils/communication.hpp:251-256` — `GlobalMin<T>` specialisation.
- `palace/utils/communication.hpp:258-263` — `GlobalMax<T>` specialisation.
- `palace/utils/communication.hpp:265-270` — `GlobalSum<T>` specialisation.
- `palace/utils/communication.hpp:272-288` — `GlobalMinLoc<T, U>` (with `ValueAndLoc` buffer marshalling).
- `palace/utils/communication.hpp:290-306` — `GlobalMaxLoc<T, U>` (same shape).
- `palace/utils/communication.hpp:308-312` — `GlobalOr` (`MPI_LOR` over `bool`).
- `palace/utils/communication.hpp:314-318` — `GlobalAnd` (`MPI_LAND` over `bool`).
- `palace/utils/communication.hpp:320-325` — `Broadcast<T>` (`MPI_Bcast`).
- `palace/utils/communication.hpp:327-334` — `Allgather<T>` (fixed-count `MPI_Allgather`).
- `palace/utils/communication.hpp:336-344` — `Allgatherv<T>` (variable-count `MPI_Allgatherv`).
- `palace/utils/communication.hpp:347-360` — `Print` (rank-gated `fmt::print`).
- `palace/utils/communication.hpp:362-375` — `Printf` (rank-gated `fmt::printf`).
- `palace/utils/communication.hpp:377-389` — `Warning` (yellow-styled "--> Warning!" header + message).
- `palace/utils/communication.hpp:391-392` — `World()` returning `MPI_COMM_WORLD`.
- `palace/utils/communication.hpp:394-399` — `default_thread_required` (FUNNELED if OpenMP, else SINGLE).
- `palace/utils/communication.hpp:401-411` — singleton `Instance()` accessor and private constructor/destructor.
- `palace/utils/communication.hpp:413-424` — `Init(int*, char***, int)` private implementation (calls `MPI_Init_thread`, constructs the singleton).
- `palace/linalg/vector.hpp:201-206` — `linalg::GlobalSize` (calls `Mpi::GlobalSum(1, &N, comm)`).
- `palace/linalg/vector.hpp:209-216` — `linalg::GlobalSize2`.
- `palace/linalg/vector.hpp:247-253` — `linalg::Dot` (local-then-collective pattern).
- `palace/linalg/vector.hpp:277-283` — `linalg::Sum`.
- `palace/linalg/vector.hpp:286-294` — `linalg::Mean` (two-element reduction).
- `palace/linalg/orthog.hpp:41-53` — `OrthogonalizeColumnMGS` (per-step single-element reduction).
- `palace/linalg/orthog.hpp:57-89` — `OrthogonalizeColumnCGS` (m-element reduction plus refinement m-element reduction).
- `palace/test/unit/test-orthog.cpp:1-80` — `[Serial][Parallel]`-tagged orthogonalization tests exercising the `Mpi::GlobalSum`-via-orthog paths.
- `palace/test/unit/test-rap.cpp:24-37` — single-rank vs multi-rank conditional logic using `Mpi::Size(comm)`.

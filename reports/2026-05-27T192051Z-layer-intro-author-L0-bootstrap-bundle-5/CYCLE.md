---
agent: layer-intro-author
invoked_at: 2026-05-27T19:20:51Z
scope: L0 bootstrap bundle 5 (priority #10 continuation)
status: integrated
integrated_at: 2026-05-27T200036Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied cleanly via integrator-per-report pass 2 of cycle-009. 2 of 3 candidates landed; tests-as-semantic-supplement deferred via new OQ. L0 chapter count 14 → 16. Closes cycle-008 OQ l0-bundle-5-candidates. 2 follow-up OQs opened (tests-as-semantic-supplement-l0-vs-concepts-decision, l0-bundle-6-candidates).
---

# CYCLE: L0 bootstrap bundle 5

## Summary

Two new L0 chapters proposed for bundle 5 of the L0-bootstrap (priority #10):

1. **`mpi-globalsum-and-collectives`** — file-level overview of `palace/utils/communication.hpp` (the entire 429-line header housing the `palace::Mpi` collective wrappers + the `palace::mpi::DataType<T>` template family). File-level companion to the convention chapter [`par-types-single-rank-reading`](../../book/src/L0/par-types-single-rank-reading.md)'s §"MPI collectives" section. Catalogues the file structure (the two top-level units), the `Mpi` class's five concern groups, the call-site distribution across `linalg/` and `models/` (42 `GlobalSum` sites + 36 `GlobalMin`/`GlobalMax` sites combined), and the algebraic-collapse behaviour under single-rank reading.
2. **`preconditioner-classes-overview`** — survey of the seven preconditioner classes Palace ships (`BoomerAmgSolver`, `HypreAmsSolver`, `JacobiSmoother`, `ChebyshevSmoother`, `ChebyshevSmoother1stKind`, `DistRelaxationSmoother`, `GeometricMultigridSolver`, `BlockDiagonalPreconditioner`). Three-group split by inheritance and orchestration: Hypre-wrapped algebraic, native `Solver<OperType>` smoothers, composition preconditioners. Anchors the future `L1/apply_preconditioner` operator and any cycle-005+ work on the V-cycle algebra.

Both chapters follow the cycle-008 bundle-4 precedent (clean "Referenced from" with no stale-forward-decl italics; precise `file:start-end` citations; no ellipsis ranges).

Third bundle-5 candidate `tests-as-semantic-supplement` is **deferred** per the dispatch's explicit guidance. The 14-chapter post-bundle-4 L0 surface plus the 2 new chapters here brings the total to **16 L0 chapters**. The `tests-as-semantic-supplement` candidate is recorded as a follow-up open question (whether it fits L0 as a convention chapter or `book/src/concepts/` as a methodology concept).

## Proposed changes

### New file 1 — `book/src/L0/mpi-globalsum-and-collectives.md`

Co-located file: `mpi-globalsum-and-collectives.md` in this report directory. Integrator-per-report copies it to `book/src/L0/`.

### New file 2 — `book/src/L0/preconditioner-classes-overview.md`

Co-located file: `preconditioner-classes-overview.md` in this report directory. Integrator-per-report copies it to `book/src/L0/`.

### Edit — `book/src/L0/index.md`

Append two entries to the dep-map (under the existing "Overload sets and class interfaces" section).

```edit:book/src/L0/index.md
[old]: - [`eigensolver-wrapper`](./eigensolver-wrapper.md) — `EigenvalueSolver` abstract base in `palace/linalg/eps.hpp` plus three concrete wrappers: `ArpackEigenvalueSolver` (RCI), `SlepcEigenvalueSolver` (shell-matrix), and `NonLinearEigenvalueSolver` / `QuasiNewtonSolver` (Palace's own direct-Newton). The eigensolver-side composition with `ComplexKspSolver` for spectral-transformation inverse application, dispatched by the eigenmode pipeline at `palace/models/modeeigensolver.cpp:1029-1047`. The L0 anchor for the future `L1/eigsolve` operator and for the L4 eigensolve-monad composition that the [strawman calculus](../design/l4_calculus.md)'s `iterate_while` primitive instantiates.
[new]: - [`eigensolver-wrapper`](./eigensolver-wrapper.md) — `EigenvalueSolver` abstract base in `palace/linalg/eps.hpp` plus three concrete wrappers: `ArpackEigenvalueSolver` (RCI), `SlepcEigenvalueSolver` (shell-matrix), and `NonLinearEigenvalueSolver` / `QuasiNewtonSolver` (Palace's own direct-Newton). The eigensolver-side composition with `ComplexKspSolver` for spectral-transformation inverse application, dispatched by the eigenmode pipeline at `palace/models/modeeigensolver.cpp:1029-1047`. The L0 anchor for the future `L1/eigsolve` operator and for the L4 eigensolve-monad composition that the [strawman calculus](../design/l4_calculus.md)'s `iterate_while` primitive instantiates.
- [`preconditioner-classes-overview`](./preconditioner-classes-overview.md) — survey of Palace's seven preconditioner classes (`BoomerAmgSolver`, `HypreAmsSolver`, `JacobiSmoother`, `ChebyshevSmoother`, `ChebyshevSmoother1stKind`, `DistRelaxationSmoother`, `GeometricMultigridSolver`, `BlockDiagonalPreconditioner`) across `palace/linalg/{amg,ams,jacobi,chebyshev,distrelaxation,gmg,blockprecond}.{hpp,cpp}`. Three-group classification (Hypre-wrapped algebraic / native `Solver<OperType>` smoothers / composition preconditioners). The L0 anchor for the future `L1/apply_preconditioner` operator and for L2 work on the V-cycle algebra.
```

Add one entry to the "File overviews" section.

```edit:book/src/L0/index.md
[old]: - [`linalg-iterative-file`](./linalg-iterative-file.md) — `palace/linalg/iterative.{hpp,cpp}` at a glance. The home of `IterativeSolver<OperType>` base class plus the three concrete subclasses `CgSolver`, `GmresSolver`, `FgmresSolver`. The L0 anchor for the cycle-007+ `L1/ksp_solve` operator and for the per-step body that the L2 `krylov-step` entry instantiates.
[new]: - [`linalg-iterative-file`](./linalg-iterative-file.md) — `palace/linalg/iterative.{hpp,cpp}` at a glance. The home of `IterativeSolver<OperType>` base class plus the three concrete subclasses `CgSolver`, `GmresSolver`, `FgmresSolver`. The L0 anchor for the cycle-007+ `L1/ksp_solve` operator and for the per-step body that the L2 `krylov-step` entry instantiates.
- [`mpi-globalsum-and-collectives`](./mpi-globalsum-and-collectives.md) — `palace/utils/communication.hpp` (header-only, 429 lines). The single file housing every MPI collective Palace performs: the `palace::mpi::DataType<T>` template family for type-discovery and the `palace::Mpi` singleton class wrapping `MPI_Allreduce` / `MPI_Bcast` / `MPI_Allgather` / `MPI_Barrier` / `MPI_Abort` plus rank-gated `Print` / `Warning` formatters. File-level companion to [`par-types-single-rank-reading`](./par-types-single-rank-reading.md)'s §"MPI collectives and the `palace::Mpi` namespace".
```

### Edit — `book/src/SUMMARY.md`

Add two L0 Part entries: the MPI file entry goes with the other "File —" entries (after `linalg-iterative-file`); the preconditioner-classes overview goes with the "Class —" entries (after `eigensolver-wrapper`).

```edit:book/src/SUMMARY.md
[old]: - [File — palace/linalg/iterative.{hpp,cpp}](./L0/linalg-iterative-file.md)
[new]: - [File — palace/linalg/iterative.{hpp,cpp}](./L0/linalg-iterative-file.md)
- [File — palace/utils/communication.hpp (MPI collectives)](./L0/mpi-globalsum-and-collectives.md)
```

```edit:book/src/SUMMARY.md
[old]: - [Class — EigenvalueSolver and wrappers](./L0/eigensolver-wrapper.md)
[new]: - [Class — EigenvalueSolver and wrappers](./L0/eigensolver-wrapper.md)
- [Class — preconditioner classes overview](./L0/preconditioner-classes-overview.md)
```

## Supporting evidence

### Bundle-5 candidate selection

Per dispatch guidance and `scaffolding/open-questions.md` `l0-bundle-5-candidates`:

- **Selected**: `mpi-globalsum-and-collectives`, `preconditioner-classes-overview`.
- **Deferred**: `tests-as-semantic-supplement` (open question whether it fits L0 as a convention chapter or `book/src/concepts/` as a methodology concept).

### `mpi-globalsum-and-collectives` source verification

- `palace/utils/communication.hpp:1-429` — full file (header-only, no `.cpp` companion); verified via direct read.
- Line-by-line: `mpi::` namespace 17-174; `Mpi` class 181-425; `GlobalOp` 244-249; `GlobalSum` 265-270; `Broadcast` 320-325; `Print` 347-360; `World()` 391-392; `Instance()` 401-411. All cited ranges verified inclusive of section comments where appropriate.
- Call-site distribution: 42 `Mpi::GlobalSum` (full-tree count) and 36 `Mpi::GlobalMin` + `Mpi::GlobalMax` combined. Chapter enumerates the principal `linalg/` and `models/` sites; broader use spans `utils/{timer.hpp,memoryreporting.cpp,dorfler.cpp,geodata.cpp}`, `drivers/{basesolver.cpp,boundarymodesolver.cpp}`, `fem/errorindicator.hpp`. The non-enumerated sites are all of-the-same-shape reductions (counters, memory, mesh statistics) and the chapter's "all reduce to identity under single-rank reading" claim covers them uniformly.
- Cross-references to existing L0 chapters: `par-types-single-rank-reading` (sibling), `linalg-vector-file` (downstream caller), `linalg-free-functions` (wrapping convention).
- Tests: `test-orthog.cpp` exercises `Mpi::GlobalSum` indirectly via orthogonalization; `test-rap.cpp:24-37` uses `Mpi::Size(comm)` for serial-vs-parallel branching.

### `preconditioner-classes-overview` source verification

- `palace/linalg/amg.hpp:16-27` — `BoomerAmgSolver` (32 lines); verified inheriting from `mfem::HypreBoomerAMG`.
- `palace/linalg/ams.hpp:20-79` — `HypreAmsSolver`; verified inheriting from `mfem::HypreSolver`; member layout (Hypre handle line 24, gradient G line 34, interpolation matrices Pi/Pix/Piy/Piz line 38, HypreParVector workspace line 39).
- `palace/linalg/jacobi.hpp:18-44` — `JacobiSmoother<OperType>`; verified template / `Solver<OperType>` inheritance; `dinv`, `omega`, `sf_max` state.
- `palace/linalg/chebyshev.hpp:22-77` — `ChebyshevSmoother<OperType>` (4th-kind); references lines 19-20 confirmed (Phillips-Fischer 2022).
- `palace/linalg/chebyshev.hpp:85-142` — `ChebyshevSmoother1stKind<OperType>`; references lines 82-83 confirmed (Adams et al. 2003).
- `palace/linalg/distrelaxation.hpp:29-88` — `DistRelaxationSmoother<OperType>`; references lines 25-27 confirmed (Hiptmair 1998); `SetOperator` aborts lines 57-61.
- `palace/linalg/gmg.hpp:30-82` — `GeometricMultigridSolver<OperType>`; member layout lines 37-54 verified; `VCycle` private declaration line 57; constructor lines 60-64.
- `palace/linalg/gmg.cpp:126-142` — `Mult` body verified; `VCycle` body lines 172-205 verified; `RealMult`/`RealMultTranspose` helpers lines 147-167.
- `palace/linalg/blockprecond.hpp:31-61` — `BlockDiagonalPreconditioner<OperType>`; comment block lines 16-23; type aliases lines 63-64.
- `palace/utils/labels.hpp:91-101` — `LinearSolver` enum (eight cases).
- `palace/linalg/ksp.cpp:125-240` — `ConfigurePreconditionerSolver` function body; switch over `LinearSolver` enum spans lines 136-204 (verified each enum case).
- `palace/linalg/ksp.cpp:207-239` — geometric-multigrid post-processing branch (verified).

### Cross-references

Both chapters cite existing L0 chapters by relative link (`./par-types-single-rank-reading.md`, `./linalg-vector-file.md`, `./linalg-free-functions.md`, `./mfem-wrapper-solver.md`, `./linalg-operator-file.md`, `./mutable-workspace-pattern.md`, `./ksp-factory-file.md`, `./kspsolver-base-class.md`). No forward-references to non-existent files.

Higher-layer L1 / L2 / L4 forward-references use `(forward-target)` annotation per cycle-008 bundle-4 precedent (no stale-italics-forward-decl).

### Chapter-shape compliance

- **mpi-globalsum-and-collectives**: 4 thematic paragraphs of interpretation + 4 structural sections (File structure, Mpi class surface, Call-site distribution, Algebraic content) + 1 test-coverage section + 1 notes section + Dependencies / Referenced from / Evidence sections. Citations are concrete `file:start-end` (no ellipsis ranges).
- **preconditioner-classes-overview**: 3 thematic paragraphs + group-classification preface + 3 group sections + State/workspace section + Test coverage + Notes + Dependencies / Referenced from / Evidence sections. Citations are concrete `file:start-end`.

Both chapters fall within the L0 reference-note discipline (interpretation + representative citations, no line-by-line source duplication).

## Open questions / caveats

### `tests-as-semantic-supplement` deferred

The third bundle-5 candidate from `scaffolding/open-questions.md` `l0-bundle-5-candidates` is **deferred**. The CLAUDE.md "Tests as semantic supplement" invariant is a **methodology convention** rather than a Palace-source convention; arguably it fits `book/src/concepts/` better than `book/src/L0/` (where the existing convention chapters all anchor Palace / MFEM idioms, not project methodology).

**Routes to**: open-questions follow-up — "Does `tests-as-semantic-supplement` belong in `book/src/L0/` as a convention chapter, in `book/src/concepts/` as a methodology concept, or only in `CLAUDE.md` / `scaffolding/test-linkages/` as already-established meta-instruction?" Recommend deciding before any bundle 6 dispatch picks it up.

### MPI-only call sites in `divfree.cpp` and `models/spaceoperator.cpp`

`mpi-globalsum-and-collectives` enumerates the `Mpi::GlobalSum` / `Mpi::GlobalMin` call sites at file:line granularity. The model-pipeline call sites (`spaceoperator.cpp:374,416,450,490,689,723,750,810,1063,1101` for `Mpi::GlobalMin`) are listed compactly. If the cycle-005+ retroactive thinning sweep would benefit from per-call-site context (each is a different sanity check in a different operator-construction path), a follow-up could expand the per-site notes — but currently those call sites are pure single-rank-collapse-to-identity uses with no algorithm-bearing semantics.

### Direct-solver wrappers cross-referenced, not catalogued

`preconditioner-classes-overview` mentions the four direct-solver wrappers (`MumpsSolver`, `SuperLUSolver`, `StrumpackSolver`, `StrumpackMixedPrecisionSolver`) but does not catalogue them, referring instead to [`mfem-wrapper-solver`](./mfem-wrapper-solver.md) §"Where `MfemWrapperSolver` is used" for that side. Confirmed: the existing `mfem-wrapper-solver` chapter §"Where `MfemWrapperSolver` is used" (lines 55+) names all four wrappers as call sites. No coverage gap.

### Forward-target for `linalg-solver-file`

The bundle-5 candidate list in `scaffolding/open-questions.md` `l0-bundle-5-candidates` also lists `linalg-solver-file` as a higher-priority candidate (recommended as "the highest-priority candidate"). The dispatch explicitly redirected to `mpi-globalsum-and-collectives` + `preconditioner-classes-overview`, so `linalg-solver-file` is **also deferred** — note that the existing [`mfem-wrapper-solver`](./mfem-wrapper-solver.md) chapter covers `solver.{hpp,cpp}` from a per-class angle but the file-level overview (mirroring `linalg-operator-file` / `linalg-iterative-file` / `linalg-vector-file`) is still missing. Route to bundle 6.

### Iterative-solver `Mpi::Print` calls

`iterative.cpp` has 20 `Mpi::Print` call sites (residual-norm logging per CG / GMRES / FGMRES iteration). The new `mpi-globalsum-and-collectives` chapter notes these as "L0 instrumentation, not algorithm" without per-site enumeration. If the cycle-005+ retroactive sweep on iterative-solver L1 entries surfaces a need to anchor specific per-iteration log calls, a follow-up could expand — but the current treatment (erased as transparent) matches the L1 abstraction.

### Bundle-5 size discipline

The dispatch specified 2 chapters (light scope per planner); this report delivers exactly 2. The `tests-as-semantic-supplement` candidate is deferred per dispatch guidance.

### Bundle 6 candidate ordering

After bundle 5 lands, the bundle-6 candidate set is:

1. `linalg-solver-file` (per `l0-bundle-5-candidates` original recommendation) — file-level overview of `palace/linalg/solver.{hpp,cpp}`, the home of `Solver<OperType>` base class and `MfemWrapperSolver` (already per-class-covered in `mfem-wrapper-solver`). Highest priority.
2. `tests-as-semantic-supplement` — pending the open question on whether to file as L0 convention or `concepts/` methodology concept.
3. `mutable-workspace-pattern` Category-5 expansion (if cycle-008+ work surfaces new workspace-pattern variants not covered by Categories 1-4).

These three would form bundle 6 with the same 2-chapters-per-cycle cadence.

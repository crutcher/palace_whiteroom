---
agent: layer-intro-author
invoked_at: 2026-05-27T17:35:23Z
scope: L0 bootstrap bundle 4 (3 chapters)
status: integrated
integrated_at: 2026-05-27T18:35:15Z
integration_commit: e4929aa
integration_notes: cycle-008 pass 3 (wave-1). 3 new L0 chapters (eigensolver-wrapper, par-types-single-rank-reading, linalg-operator-file); L0 count 11->14. Closed cycle-007 OQ eigensolver-wrapper-l0-bundle-4-candidate; opened 3 follow-up OQs (eigsolve-l1-operator-rough-in-candidate, matrix-weighted-norm-and-bilinear-form-l1-rough-ins, l0-bundle-5-candidates).
---

# CYCLE: L0 bootstrap bundle 4

## Summary

Bundle 4 of the L0 bootstrap (cycle-008 dispatch #5, continuation of priority #10).
Adds **three new L0 reference notes** and updates `book/src/L0/index.md` + `book/src/SUMMARY.md`:

- `eigensolver-wrapper` — `EigenvalueSolver` abstract base + ARPACK / SLEPc / Palace's `QuasiNewtonSolver` concrete wrappers. **Closes OQ `eigensolver-wrapper-l0-bundle-4-candidate`** (cycle-007). Pre-verified the surface exists — `eps.hpp` is a real abstract base, not a stub; `arpack.cpp` (24 KB), `slepc.cpp` (67 KB), `nleps.cpp` (31 KB) are substantial implementations. Class hierarchy: 3 concrete branches realize 3 distinct orchestration patterns (RCI / shell-matrix / direct-Newton); the L1 lift would name a single `eigsolve` operator and absorb the orchestration axis as transparent dispatch.
- `par-types-single-rank-reading` — dedicated convention page for the `Par*` MFEM type family and the single-rank reading rule per `CLAUDE.md` "Scope". Currently treated in one paragraph of [`mfem-vector-types`](../../book/src/L0/mfem-vector-types.md) §"The `Par*` axis"; this chapter is the dedicated companion. Catalogues `Par*` touches across `palace/fem/` (81 sites), `palace/models/` (9), and `palace/linalg/ams.{hpp,cpp}`. Also covers the `palace::Mpi::` collective wrappers at `palace/utils/communication.hpp:181-427` and how they reduce under single-rank reading. Test coverage cited from `palace/test/unit/test-rap.cpp` (the `[Serial][Parallel]` Catch2 tag explicitly authorises the rule).
- `linalg-operator-file` — file-level overview of `palace/linalg/operator.{hpp,cpp}`. Companion to [`apply-linop-overload-set`](../../book/src/L0/apply-linop-overload-set.md) (method-overload set view). Covers 8 class definitions (`Operator` alias, `ComplexOperator`, `ComplexWrapperOperator`, `SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `BaseMultigridOperator`) and the `palace::linalg::` free-function namespace at the file's bottom (`Norml2`, `Normalize`, two `Dot` overloads, `SpectralNorm`). Cross-references to the sibling files `rap.{hpp,cpp}` (parallel-RAP wrapping), `solver.{hpp,cpp}` (`MfemWrapperSolver`), `iterative.{hpp,cpp}` (`IterativeSolver` hierarchy). Test linkage via `palace/test/unit/test-rap.cpp`.

L0 chapter count: **11 → 14**. Maintains the 1–3 chapters/cycle cadence (cycle-005 = 6, cycle-006 = 2, cycle-007 = 3, cycle-008 = 3).

All three chapters use the clean "Referenced from" structure (no stale-forward-decl italic note) per the cycle-008 dispatch #4 housekeeping precedent.

## Proposed changes

### 1. New file `book/src/L0/eigensolver-wrapper.md`

```edit:book/src/L0/eigensolver-wrapper.md
[old]: (does not exist)
[new]: <see supporting doc eigensolver-wrapper.md in this report directory>
```

### 2. New file `book/src/L0/par-types-single-rank-reading.md`

```edit:book/src/L0/par-types-single-rank-reading.md
[old]: (does not exist)
[new]: <see supporting doc par-types-single-rank-reading.md in this report directory>
```

### 3. New file `book/src/L0/linalg-operator-file.md`

```edit:book/src/L0/linalg-operator-file.md
[old]: (does not exist)
[new]: <see supporting doc linalg-operator-file.md in this report directory>
```

### 4. Update `book/src/L0/index.md` — add 3 rows under existing sections

```edit:book/src/L0/index.md
[old]: ## Reference-note cohort

**Conventions** — cross-cutting Palace / MFEM idioms referenced by L1 entries:

- [`output-arg-vs-receiver`](./output-arg-vs-receiver.md) — `A.Mult(x, y)` writes `y` vs receiver-mutating `y.Add(α, x)` / `y *= s`; how L1 lifts both into pure-functional form.
- [`mfem-vector-types`](./mfem-vector-types.md) — `Vector` / `ComplexVector` duality (element-type axis); single-rank reading of `Par*` types per `CLAUDE.md` "Scope".
- [`linalg-free-functions`](./linalg-free-functions.md) — `linalg::AXPY` / `linalg::Dot` / `linalg::Norml2` as template-dispatch wrappers over the method-form surface; the wrapping pattern Palace uses across `vector.hpp`.
- [`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md) — Operational L0 classification (lifted from `CLAUDE.md`): `α == 1.0` branch in `AXPY` is transparent; reduction-tree non-associativity is load-bearing. Worked examples from the BLAS-1 family.
- [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) — `mutable Vector z` workspace members on operator subclasses and iterative-solver subclasses; lazy-allocate-on-first-use, reuse-across-calls discipline. The L0 substrate for L1>L0 mutation-rotation themes' "workspace mention and erase" rewrite.

**File overviews** — anchor files L1 references repeatedly:

- [`linalg-vector-file`](./linalg-vector-file.md) — `palace/linalg/vector.{hpp,cpp}` at a glance. The home of `ComplexVector`, the `AXPY/AXPBY/AXPBYPCZ` family, `Dot`/`TransposeDot`/`LocalDot`, `Norml2`, `Normalize`.
- [`ksp-factory-file`](./ksp-factory-file.md) — `palace/linalg/ksp.cpp` Krylov-solver factory. Enum-routed dispatch: CG / GMRES / FGMRES implemented; MINRES / BICGSTAB / DEFAULT abort. Anchor for the "advertised-but-unimplemented" pattern that drives the MINRES / BiCGStab obstruction themes.
- [`linalg-iterative-file`](./linalg-iterative-file.md) — `palace/linalg/iterative.{hpp,cpp}` at a glance. The home of `IterativeSolver<OperType>` base class plus the three concrete subclasses `CgSolver`, `GmresSolver`, `FgmresSolver`. The L0 anchor for the cycle-007+ `L1/ksp_solve` operator and for the per-step body that the L2 `krylov-step` entry instantiates.

**Overload sets and class interfaces** — multi-overload / multi-subclass surfaces referenced by L1 / L2 / L4 entries:

- [`apply-linop-overload-set`](./apply-linop-overload-set.md) — the `Mult` / `MultTranspose` / `MultHermitianTranspose` / `AddMult` family on the `Operator` / `ComplexOperator` hierarchy, plus the concrete-subclass family (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `BaseMultigridOperator`, `ComplexWrapperOperator`, `ParOperator`). The L0 anchor for `L1/apply_linop`'s 12-method-overload collapse and for the `apply-linop-mutation-rotation` lowering theme.
- [`kspsolver-base-class`](./kspsolver-base-class.md) — `BaseKspSolver<OperType>` in `palace/linalg/ksp.{hpp,cpp}`. The composition class pairing an `IterativeSolver` with a `Solver` (preconditioner) and exposing the public `Mult(b, x)` "solve `Ax = b`" entry point. Anchors the L4 `solve-monad` concept to concrete C++ and is the call-site target for solver use across Palace's model pipelines.
- [`mfem-wrapper-solver`](./mfem-wrapper-solver.md) — `MfemWrapperSolver<OperType>` in `palace/linalg/solver.{hpp,cpp}`. The adapter that lifts MFEM's real-only `mfem::Solver` hierarchy into Palace's templated `Solver<OperType>` hierarchy. Every preconditioner Palace uses — `BoomerAMG`, `AMS`, `MUMPS`, `SuperLU`, `Strumpack` — comes through this wrapper before composition into a `BaseKspSolver`. The L0 substrate for the L4 `complex-from-real-lift` concept on the preconditioner side.
[new]: ## Reference-note cohort

**Conventions** — cross-cutting Palace / MFEM idioms referenced by L1 entries:

- [`output-arg-vs-receiver`](./output-arg-vs-receiver.md) — `A.Mult(x, y)` writes `y` vs receiver-mutating `y.Add(α, x)` / `y *= s`; how L1 lifts both into pure-functional form.
- [`mfem-vector-types`](./mfem-vector-types.md) — `Vector` / `ComplexVector` duality (element-type axis); brief intro to `Par*` types (see also `par-types-single-rank-reading`).
- [`par-types-single-rank-reading`](./par-types-single-rank-reading.md) — the `Par*` MFEM type family (`ParMesh`, `ParFiniteElementSpace`, `ParGridFunction`, `ParBilinearForm`, `HypreParVector`, `HypreParMatrix`) and the single-rank reading rule per `CLAUDE.md` "Scope". Also covers `palace::Mpi::` collective wrappers (`GlobalSum` / `GlobalMin` / …) and how they reduce under single-rank reading.
- [`linalg-free-functions`](./linalg-free-functions.md) — `linalg::AXPY` / `linalg::Dot` / `linalg::Norml2` as template-dispatch wrappers over the method-form surface; the wrapping pattern Palace uses across `vector.hpp`.
- [`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md) — Operational L0 classification (lifted from `CLAUDE.md`): `α == 1.0` branch in `AXPY` is transparent; reduction-tree non-associativity is load-bearing. Worked examples from the BLAS-1 family.
- [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) — `mutable Vector z` workspace members on operator subclasses and iterative-solver subclasses; lazy-allocate-on-first-use, reuse-across-calls discipline. The L0 substrate for L1>L0 mutation-rotation themes' "workspace mention and erase" rewrite.

**File overviews** — anchor files L1 references repeatedly:

- [`linalg-vector-file`](./linalg-vector-file.md) — `palace/linalg/vector.{hpp,cpp}` at a glance. The home of `ComplexVector`, the `AXPY/AXPBY/AXPBYPCZ` family, `Dot`/`TransposeDot`/`LocalDot`, `Norml2`, `Normalize`.
- [`linalg-operator-file`](./linalg-operator-file.md) — `palace/linalg/operator.{hpp,cpp}` at a glance. The home of `ComplexOperator`, `ComplexWrapperOperator`, `SumOperator`, the `BaseProductOperator` / `BaseDiagonalOperator` / `BaseMultigridOperator` template families, and the `palace::linalg::` matrix-weighted norm / bilinear-form free functions. The file-level companion to [`apply-linop-overload-set`](./apply-linop-overload-set.md).
- [`ksp-factory-file`](./ksp-factory-file.md) — `palace/linalg/ksp.cpp` Krylov-solver factory. Enum-routed dispatch: CG / GMRES / FGMRES implemented; MINRES / BICGSTAB / DEFAULT abort. Anchor for the "advertised-but-unimplemented" pattern that drives the MINRES / BiCGStab obstruction themes.
- [`linalg-iterative-file`](./linalg-iterative-file.md) — `palace/linalg/iterative.{hpp,cpp}` at a glance. The home of `IterativeSolver<OperType>` base class plus the three concrete subclasses `CgSolver`, `GmresSolver`, `FgmresSolver`. The L0 anchor for the cycle-007+ `L1/ksp_solve` operator and for the per-step body that the L2 `krylov-step` entry instantiates.

**Overload sets and class interfaces** — multi-overload / multi-subclass surfaces referenced by L1 / L2 / L4 entries:

- [`apply-linop-overload-set`](./apply-linop-overload-set.md) — the `Mult` / `MultTranspose` / `MultHermitianTranspose` / `AddMult` family on the `Operator` / `ComplexOperator` hierarchy, plus the concrete-subclass family (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `BaseMultigridOperator`, `ComplexWrapperOperator`, `ParOperator`). The L0 anchor for `L1/apply_linop`'s 12-method-overload collapse and for the `apply-linop-mutation-rotation` lowering theme.
- [`kspsolver-base-class`](./kspsolver-base-class.md) — `BaseKspSolver<OperType>` in `palace/linalg/ksp.{hpp,cpp}`. The composition class pairing an `IterativeSolver` with a `Solver` (preconditioner) and exposing the public `Mult(b, x)` "solve `Ax = b`" entry point. Anchors the L4 `solve-monad` concept to concrete C++ and is the call-site target for solver use across Palace's model pipelines.
- [`mfem-wrapper-solver`](./mfem-wrapper-solver.md) — `MfemWrapperSolver<OperType>` in `palace/linalg/solver.{hpp,cpp}`. The adapter that lifts MFEM's real-only `mfem::Solver` hierarchy into Palace's templated `Solver<OperType>` hierarchy. Every preconditioner Palace uses — `BoomerAMG`, `AMS`, `MUMPS`, `SuperLU`, `Strumpack` — comes through this wrapper before composition into a `BaseKspSolver`. The L0 substrate for the L4 `complex-from-real-lift` concept on the preconditioner side.
- [`eigensolver-wrapper`](./eigensolver-wrapper.md) — `EigenvalueSolver` abstract base in `palace/linalg/eps.hpp` plus three concrete wrappers: `ArpackEigenvalueSolver` (RCI), `SlepcEigenvalueSolver` (shell-matrix), and `NonLinearEigenvalueSolver` / `QuasiNewtonSolver` (Palace's own direct-Newton). The eigensolver-side composition with `ComplexKspSolver` for spectral-transformation inverse application, dispatched by the eigenmode pipeline at `palace/models/modeeigensolver.cpp:1029-1047`. The L0 anchor for the future `L1/eigsolve` operator and for the L4 eigensolve-monad composition that the [strawman calculus](../design/l4_calculus.md)'s `iterate_while` primitive instantiates.
```

### 5. Update `book/src/SUMMARY.md` — add 3 chapter entries under L0 Part

```edit:book/src/SUMMARY.md
[old]: # L0 — Cited Palace Source + Reference Notes
- [Overview](./L0/index.md)
- [Convention — output-arg vs receiver](./L0/output-arg-vs-receiver.md)
- [Convention — MFEM vector types](./L0/mfem-vector-types.md)
- [Convention — linalg:: free-function wrappers](./L0/linalg-free-functions.md)
- [Convention — transparent vs load-bearing tricks](./L0/transparent-vs-load-bearing-tricks.md)
- [Convention — mutable workspace pattern](./L0/mutable-workspace-pattern.md)
- [File — palace/linalg/vector.{hpp,cpp}](./L0/linalg-vector-file.md)
- [File — palace/linalg/ksp.cpp](./L0/ksp-factory-file.md)
- [File — palace/linalg/iterative.{hpp,cpp}](./L0/linalg-iterative-file.md)
- [Overload set — Mult / MultTranspose / AddMult](./L0/apply-linop-overload-set.md)
- [Class — BaseKspSolver](./L0/kspsolver-base-class.md)
- [Class — MfemWrapperSolver](./L0/mfem-wrapper-solver.md)
[new]: # L0 — Cited Palace Source + Reference Notes
- [Overview](./L0/index.md)
- [Convention — output-arg vs receiver](./L0/output-arg-vs-receiver.md)
- [Convention — MFEM vector types](./L0/mfem-vector-types.md)
- [Convention — Par* types and single-rank reading](./L0/par-types-single-rank-reading.md)
- [Convention — linalg:: free-function wrappers](./L0/linalg-free-functions.md)
- [Convention — transparent vs load-bearing tricks](./L0/transparent-vs-load-bearing-tricks.md)
- [Convention — mutable workspace pattern](./L0/mutable-workspace-pattern.md)
- [File — palace/linalg/vector.{hpp,cpp}](./L0/linalg-vector-file.md)
- [File — palace/linalg/operator.{hpp,cpp}](./L0/linalg-operator-file.md)
- [File — palace/linalg/ksp.cpp](./L0/ksp-factory-file.md)
- [File — palace/linalg/iterative.{hpp,cpp}](./L0/linalg-iterative-file.md)
- [Overload set — Mult / MultTranspose / AddMult](./L0/apply-linop-overload-set.md)
- [Class — BaseKspSolver](./L0/kspsolver-base-class.md)
- [Class — MfemWrapperSolver](./L0/mfem-wrapper-solver.md)
- [Class — EigenvalueSolver and wrappers](./L0/eigensolver-wrapper.md)
```

## Supporting evidence

### Per-chapter Palace source ranges read

**`eigensolver-wrapper`:**
- `palace/linalg/eps.hpp:1-145` (entire abstract-base file).
- `palace/linalg/arpack.hpp:1-244` (entire wrapper interface file).
- `palace/linalg/arpack.cpp:263-358, 513-560` (`SolveInternal` RCI loop; `ArpackEPSSolver::Solve()` body).
- `palace/linalg/slepc.hpp:1-249` (wrapper interface through `SlepcEPSSolverBase`).
- `palace/linalg/slepc.cpp:351-372, 687-757` (operator / linear-solver setters; `SlepcEPSSolverBase::Solve()` body).
- `palace/linalg/nleps.hpp:1-287` (entire wrapper interface file).
- `palace/models/modeeigensolver.cpp:1029-1047, 470, 502` (dispatch site; eigenmode-pipeline call sites).
- `palace/models/modeeigensolver.hpp:209` (`eigen` field).
- `palace/models/waveportoperator.cpp:524` (wave-port pipeline use site).

**`par-types-single-rank-reading`:**
- `palace/fem/fespace.hpp:1-95` (palace `FiniteElementSpace` wrapper over `mfem::ParFiniteElementSpace`).
- `palace/fem/interpolator.hpp:34, 61-64` (`ProbeField` / `InterpolateField` signatures).
- `palace/fem/coefficient.hpp:89, 93, 168, 175, 326` (boundary-coefficient classes).
- `palace/linalg/ams.hpp:39` (AMS preconditioner workspace).
- `palace/linalg/ams.cpp:74` (AMS coordinate-basis construction).
- `palace/models/laplaceoperator.cpp:230` (electrostatic-pipeline grid-function construction).
- `palace/models/waveportoperator.cpp:48-49` (wave-port boundary-mode extraction).
- `palace/models/surfacepostoperator.cpp:108-109` (surface-flux postprocessing).
- `palace/utils/communication.hpp:14-427` (entire `palace::Mpi` and `palace::mpi::` namespaces).
- `palace/linalg/vector.hpp:201-294` (the `linalg::GlobalSize` / `linalg::Sum` / `linalg::Dot` wrappers around `Mpi::GlobalSum`).
- `palace/test/unit/test-rap.cpp:24-110` (`BuildParSumOperator` test exercising `ParOperator` / `ComplexParOperator` under `[Serial][Parallel]`).

**`linalg-operator-file`:**
- `palace/linalg/operator.hpp:1-407` (entire file).
- `palace/linalg/operator.cpp:1-698` (entire file; specific bodies at lines 13-23, 25-66, 85-394, 421-475, 478-595, 600-694).
- `palace/linalg/rap.hpp:24, 123, 227-263` (cross-reference to sibling file's parallel-RAP classes and `BuildParSumOperator` factory).
- `palace/test/unit/test-rap.cpp:24, 50-110` (sum-operator algebra test).

### Adjacent L0 chapters cross-referenced

The three new chapters cross-reference each other and the existing 11 chapters as follows (dependencies satisfied at write time — all referenced chapters are firm):

| New chapter | Dependencies | Referenced from (forward) |
|---|---|---|
| `eigensolver-wrapper` | `kspsolver-base-class`, `apply-linop-overload-set`, `mutable-workspace-pattern` | (future L1/L4 eigsolve entries) |
| `par-types-single-rank-reading` | `mfem-vector-types`, `apply-linop-overload-set`, `transparent-vs-load-bearing-tricks` | (future retroactive-thinning of L1 entries currently citing `Par*` inline) |
| `linalg-operator-file` | `apply-linop-overload-set`, `mfem-vector-types`, `mutable-workspace-pattern`, `par-types-single-rank-reading` | (future `L1/apply_linop` anchor refactor; future `L1/dot_bilinear`, `L1/nrm2_weighted`, `L1/power_iterate`; rough-in `L2/product-of-operators`, `L2/sum-of-operators`) |

### Sibling reference relationships introduced

- `mfem-vector-types` ↔ `par-types-single-rank-reading` — element-type axis and parallel axis, the two orthogonal vector-typing concerns. The new `par-types-single-rank-reading` chapter explicitly names itself the dedicated companion to `mfem-vector-types` §"The `Par*` axis"; the L0 index update tightens the `mfem-vector-types` one-liner to point at the dedicated chapter.
- `apply-linop-overload-set` ↔ `linalg-operator-file` — method-overload set view vs file-level view of the same operator classes. The new chapter is the file-level companion; `apply-linop-overload-set` remains the per-method-shape catalogue.
- `eigensolver-wrapper` ↔ `kspsolver-base-class` — the eigensolver wraps and calls into a `ComplexKspSolver` for spectral-transformation inverse application. Both are stateful solver-composition surfaces; together they cover the linear-and-eigenvalue solver landscape at L0.

### Closes / opens open-questions

**Closes:**
- `eigensolver-wrapper-l0-bundle-4-candidate` (cycle-007) — `eigensolver-wrapper` chapter authored; pre-verification confirmed real surface (not stub-only). Routes from `mutable-workspace-pattern` Category 3 (grep-verified-only eigensolver workspaces) are now backed by full source reading.

**Opens (proposed):**

```
---
slug: eigsolve-l1-operator-rough-in-candidate
opened_at: cycle-008
opened_by: layer-intro-author
status: open
---

The new `eigensolver-wrapper` chapter notes that the three concrete branches
(ARPACK RCI / SLEPc shell-matrix / Palace's direct-Newton `QuasiNewtonSolver`)
realize three distinct orchestration patterns but expose a uniform problem-type
axis (linear / quadratic / nonlinear). A future L1 `eigsolve` operator would
absorb the orchestration axis as transparent dispatch and expose only the
problem-type axis + `ScaleType` + `WhichType` + `SetShiftInvert` mode. The
operator is sized similarly to `ksp_solve` (stateful inner loop, configured
inner linear solver via `SetLinearSolver`) and is a natural cycle-009+ harvester
target.

The L4 calculus's `iterate_while` primitive (per
`book/src/design/l4_calculus.md`) is the natural composition target for the
RCI / shell-matrix branches; the direct-Newton branch composes against the
calculus's regular `bind` + inner `solve` primitive.

**Test-coverage constraint on the harvester**: there is no dedicated
`test-eigensolver.cpp` under `palace/test/unit/` (see `eigensolver-wrapper`
chapter §"Test coverage"). The future `L1/eigsolve` harvester will need to
lean more heavily on direct source reading + literature anchors (Higham 2008,
Lehoucq-Sorensen, Hernandez-Roman-Vidal) than `L1/ksp_solve` did (which had
`test-orthog.cpp` as a direct algebra anchor), and the resulting algebraic
equivalence claims will accordingly carry weaker test-linkage evidence.

Routes to harvester (`L1/eigsolve`) once `L1/ksp_solve` settles. Source:
`reports/2026-05-27T173523Z-layer-intro-author-L0-bootstrap-bundle-4/CYCLE.md`
§Open questions item 1.
```

```
---
slug: matrix-weighted-norm-and-bilinear-form-l1-rough-ins
opened_at: cycle-008
opened_by: layer-intro-author
status: open
---

The new `linalg-operator-file` chapter notes that the `palace::linalg::` free
functions `Norml2(comm, x, B, Bx)` and `Dot(comm, x, A, y)` are matrix-weighted
variants of L1's existing `nrm2` and `dot` operators (weighted by an SPD `B`
or bilinear-form `A`, respectively). They have not been harvested at L1.
Candidate rough-in names: `L1/nrm2_weighted` and `L1/dot_bilinear`. The
workspace-internal-allocation pattern in `Dot` (`palace/linalg/operator.cpp:621-639`)
is Category 4 of `mutable-workspace-pattern` (synthetic workspace).

`SpectralNorm` (`palace/linalg/operator.hpp:398-401`) is power iteration with
configurable tolerance — also unharvested. Candidate rough-in name: `L1/power_iterate`.
Sized smaller than `eigsolve` (single largest eigenvalue, no eigenvector
recovery, no spectral transformation).

Routes to cycle-009+ harvester / abstractor. Source:
`reports/2026-05-27T173523Z-layer-intro-author-L0-bootstrap-bundle-4/CYCLE.md`
§Open questions item 2.
```

```
---
slug: l0-bundle-5-candidates
opened_at: cycle-008
opened_by: layer-intro-author
status: open
---

L0 chapter count after bundle 4 is 14. Remaining candidates from cycle-007
priority #10 not yet authored:

- `linalg-solver-file` — `palace/linalg/solver.{hpp,cpp}` file overview
  (companion to `mfem-wrapper-solver`, covering the `Solver<OperType>` base
  class and the auxiliary preconditioner classes that aren't already named).
  Currently the only file-level coverage of `solver.{hpp,cpp}` is the
  `mfem-wrapper-solver` chapter's per-class view; the file-level overview
  would mirror `linalg-operator-file` / `linalg-iterative-file` / `linalg-vector-file`.
- `tests-as-semantic-supplement` — convention page documenting how `palace/test/unit/`
  is treated as L0-equivalent semantic evidence per `CLAUDE.md` "Tests as
  semantic supplement". Cross-cutting; would replace per-chapter restatement
  of the convention.
- `preconditioner-classes-overview` — survey of the preconditioner classes
  not yet covered (`HypreAmsSolver`, `BoomerAMG`, `StrumpackSolver`, `JacobiSmoother`,
  `ChebyshevSmoother`, `DistRelaxation`, `BlockPreconditioner`, `GeometricMultigrid`).
  Sized to a file-overview chapter; some of these have their own files.

Bundle 5 (cycle-009 dispatch) should pick 2-3 of these per the 1-3
chapters/cycle cadence. Recommend `linalg-solver-file` as the highest-priority
candidate (closes the file-overview gap on the four `linalg/` anchor files
referenced by L1).

Routes to future L0 bundle 5 dispatch. Source:
`reports/2026-05-27T173523Z-layer-intro-author-L0-bootstrap-bundle-4/CYCLE.md`
§Open questions item 3.
```

## Open questions / caveats

1. **`eigensolver-wrapper` test-coverage gap.** No dedicated `test-eigensolver.cpp` exists; the wrappers are exercised only via end-to-end regressions and via larger-pipeline `test-boundarymodeoperator.cpp` / `test-romoperator.cpp`. The chapter notes this explicitly. The algebraic claims lean on direct source reading and literature (Higham 2008 scaling, Lehoucq-Sorensen ARPACK, Hernandez-Roman-Vidal SLEPc) rather than test linkages. This is a real weakness vs the `linalg/iterative.{hpp,cpp}` family (which has `test-orthog.cpp`); flagged for the future `L1/eigsolve` harvester to address. Captured as proposed-open OQ `eigsolve-l1-operator-rough-in-candidate`.

2. **`linalg::` free functions are an L1 obstruction.** `Norml2(comm, x, B, Bx)` / `Dot(comm, x, A, y)` / `SpectralNorm` have not yet been harvested at L1; the new `linalg-operator-file` chapter cites them as rough-in candidates. Captured as proposed-open OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins`.

3. **Bundle 5 candidate slate.** Remaining L0 candidates from priority #10 (notably `linalg-solver-file`, `tests-as-semantic-supplement`, preconditioner-classes-overview) deferred to bundle 5 / cycle-009. Captured as proposed-open OQ `l0-bundle-5-candidates`.

4. **`mfem-vector-types` one-liner tightening.** The L0 index update tightens the `mfem-vector-types` one-liner to reference `par-types-single-rank-reading` as the dedicated companion. The `mfem-vector-types` chapter body still contains the §"The `Par*` axis" section; this is fine as a brief intro that points at the dedicated chapter, but a future cycle could thin it further. Not in scope for this dispatch.

5. **No L1 / higher-layer edits.** All three chapters are L0; no L1 / L2 / L3 / L4 / lowering edits proposed in this bundle. The retroactive-thinning sweep (priority #11) that would rewrite `L1/` operator chapters' inline `Par*` citations to reference `par-types-single-rank-reading` is a separate future dispatch.

6. **Forward-declared "Referenced from" structure.** All three chapters use the clean "Referenced from" structure (concrete bullets for the explicit L0-internal cross-references plus a single italic-free forward-target bullet pointing to higher-layer entries not yet existing) per the cycle-008 dispatch #4 housekeeping precedent — no stale-forward-decl italic note at the top of the section.

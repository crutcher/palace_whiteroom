---
agent: layer-intro-author
invoked_at: 2026-05-28T20:22:25Z
scope: L0 reference-note bundle chapter — palace/fem/bilinearform.{hpp,cpp} (bundle-6 candidate #4)
status: integrated
integrated_at: 2026-05-29T0030Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-015 (per-report position 5). New L0 chapter fem-bilinearform-file.md (BilinearForm + DiscreteLinearOperator; 9 cited anchor surfaces; PA/FA dual). Registered in L0/index.md File-overviews cohort + SUMMARY.md L0 Part. L0 19->20 chapters. Deliberate plain-text (non-link) reference to not-yet-authored libceed/operator chapter — intentional, no dead link. New OQ bundle-6-l0-libceed-operator-file-next-candidate (#5). Book build clean."
---

# CYCLE: L0 `fem-bilinearform-file` reference note

## Summary

Authors a new L0 reference-note chapter `book/src/L0/fem-bilinearform-file.md` for
`palace/fem/bilinearform.{hpp,cpp}` — the libCEED-backed FE-assembly entry-point file.
This is the bundle-6 candidate the cycle-014 `linalg-rap-file` report ranked next (a direct
`ParallelAssemble` callee: `rap.cpp:100` invokes `BilinearForm::FullAssemble`).

**Scope decision: FOCUSED single chapter (not split).** The file is **small** — `bilinearform.hpp`
is 136 lines, `bilinearform.cpp` is 284 lines (420 total), far below rap.cpp's ~979. A single
coherent chapter chunks the whole surface without transcription: the two class declarations, the
two assembly modes (partial = libCEED `ceed::Operator`; full = assembled `HypreCSRMatrix`), the
`Assemble` PA-vs-FA policy dispatch, the FE-space-hierarchy multigrid overload, and
`DiscreteLinearOperator`'s interpolation-plus-multiplicity-scaling path. No split needed; no OQ
on scoping beyond the bundle-ranking update.

**Class names (planner did not pre-verify; confirmed via codemap + read):**
- `BilinearForm` (`bilinearform.hpp:25-91`) — domain/boundary `BilinearFormIntegrator` list → assembled operator.
- `DiscreteLinearOperator` (`bilinearform.hpp:95-132`) — domain `DiscreteInterpolator` list → interpolation operator between spaces.

Chunk count: **9** cited anchor ranges (2 class decls + 6 method bodies + 1 file-local `UseFullAssembly` policy helper).

## Proposed changes

### 1. New file `book/src/L0/fem-bilinearform-file.md`

```new-file:book/src/L0/fem-bilinearform-file.md
# File — `palace/fem/bilinearform.{hpp,cpp}`

A reference note for the **finite-element assembly entry-point** file. Per the class header
comment (`palace/fem/bilinearform.hpp:21-23`): *"This class implements bilinear and mixed
bilinear forms based on integrators assembled using the libCEED library. Assembly in the form
of a partially assembled operator or fully assembled sparse matrix is available."* This is the
file that turns a *list of integrators* (the symbolic weak-form terms — mass, stiffness, curl-curl,
…) into a concrete *local* (L-vector) operator: either a matrix-free libCEED `ceed::Operator`
(**partial assembly**) or an assembled `hypre::HypreCSRMatrix` (**full assembly**). It is the
upstream producer of the local operator `A` that [`linalg-rap-file`](./linalg-rap-file.md) then
wraps into a parallel `ParOperator` — `rap.cpp:100` calls `BilinearForm::FullAssemble` directly,
which is why this chapter is the next-ranked bundle-6 entry after `rap`.

The file declares two classes inside `namespace palace` (opened `bilinearform.hpp:14`):
`BilinearForm` (general trial→test bilinear form) and `DiscreteLinearOperator` (primal→primal
interpolation between FE spaces). It is **in scope** under the mesh / FE-space-construction
directive (this is the MFEM-equivalent FE-assembly machinery). Per the single-rank reading rule
([`par-types-single-rank-reading`](./par-types-single-rank-reading.md)), the libCEED
parallel-assembly machinery (`Ceed` objects, `CeedElemRestriction`, `CeedBasis`) and the
`HypreCSRMatrix` output are read single-rank; the OpenMP `PalacePragmaOmp(parallel ...)` shells
are a CPU-threading performance trick collapsing at L1
([`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md)). **MPI / OMP
flagged once here; not re-flagged per method.**

## At a glance — the two classes

- **`BilinearForm`** (`bilinearform.hpp:25-91`) — holds two `FiniteElementSpace` references
  (`trial_fespace`, `test_fespace`, `bilinearform.hpp:29`) and two integrator lists
  (`domain_integs`, `boundary_integs` — vectors of owned `BilinearFormIntegrator`,
  `bilinearform.hpp:32`). Integrators are appended by the templated `AddDomainIntegrator<T>` /
  `AddBoundaryIntegrator<T>` (`bilinearform.hpp:53-63`), which `make_unique<T>` and push onto the
  list — the form is *built up* term by term before any assembly runs. A single-space constructor
  (`bilinearform.hpp:48`) delegates trial = test (the square/symmetric case). Exposes the assembly
  surface: `PartialAssemble` / `FullAssemble` / `Assemble` (see below).
- **`DiscreteLinearOperator`** (`bilinearform.hpp:95-132`) — the interpolation sibling. Holds the
  same two-space references plus a `domain_interps` list of owned `DiscreteInterpolator`
  (`bilinearform.hpp:102`), appended by `AddDomainInterpolator<T>` (`bilinearform.hpp:114-118`).
  Its `FullAssemble` overloads forward to `BilinearForm::FullAssemble(..., set=true)`
  (`bilinearform.hpp:122-131`) — the `set` flag (vs accumulate) is the one assembly-semantics
  difference from `BilinearForm`. Maps *primal vectors to primal vectors* for inter-space
  interpolation (e.g. discrete gradient / curl), not a weak-form operator.

## The two assembly modes (partial vs full)

The file's load-bearing surface is the **partial-assembly / full-assembly dual** — the same local
operator built two ways, an algebraically-equivalent performance choice
([`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md): the operator
*action* is identical; full assembly materializes a sparse matrix, partial stays matrix-free):

- **`PartialAssemble`** (private core `bilinearform.cpp:27-107`) is the heart of the file. It
  verifies trial and test spaces share a mesh (`bilinearform.cpp:31-32`), constructs an empty
  `ceed::SymmetricOperator` (square case) or `ceed::Operator` (mixed case)
  (`bilinearform.cpp:37-46`), then in an OpenMP-parallel region loops over the mesh's per-geometry
  libCEED factor data (`mesh.GetCeedGeomFactorData`, `bilinearform.cpp:54`). For each geometry it
  pulls the trial/test `CeedElemRestriction` + `CeedBasis` and, for **domain** integrators (full
  mesh dimension, `bilinearform.cpp:61-79`) or **boundary** integrators (dimension − 1,
  `bilinearform.cpp:80-99`), calls `integ->Assemble(...)` to build a libCEED sub-operator and
  `op->AddSubOperator(sub_op)`. A final `op->Finalize()` (`bilinearform.cpp:104`,
  `CeedOperatorCheckReady`) closes it. The public no-arg `PartialAssemble` (`bilinearform.hpp:67-70`)
  forwards to this with the form's own trial/test spaces.
- **`FullAssemble`** (`bilinearform.cpp:109-113`) is a thin forwarder: it delegates to
  `ceed::CeedOperatorFullAssemble(op, skip_zeros, set)` (the actual matrix-materialization lives in
  `palace/fem/libceed/operator.cpp`, the not-yet-authored bundle-6 #5 candidate — see Open questions
  for the bundle ranking; plain-text reference, no link target until that chapter lands),
  returning a `hypre::HypreCSRMatrix`. The header overloads (`bilinearform.hpp:72-84`) chain
  partial-then-full and supply the `set` default.

## `Assemble` — the PA/FA policy dispatch

`Assemble(bool skip_zeros)` (`bilinearform.cpp:141-151`) is the **public entry point** that picks
the mode by polynomial order: the file-local `UseFullAssembly` helper (`bilinearform.cpp:115-139`,
in an anonymous namespace) compares the max FE-collection order against the static
`pa_order_threshold` (`bilinearform.hpp:40`, default 1) — low order → full assembly, high order →
partial. (The helper carries an MFEM historical-quirk correction: per the source comment
(`bilinearform.cpp:121-123`), MFEM's `RT_FECollection` already returns `order + 1` from
`GetOrder()` for historical reasons; the helper's `dynamic_cast`-guarded `+ 1`,
`bilinearform.cpp:126-131`, normalizes orders so the per-element-type minimum is 1.) This is the **load-bearing
algorithmic choice** of the file — *which* operator representation each FE space gets — distinct
from the boilerplate forwarders. At L1 it lifts as a variant axis (PA-vs-FA) on the FE-assembly
operator, driven by an order threshold.

The FE-space-**hierarchy** overload of `Assemble` (`bilinearform.cpp:153-201`) is the
**geometric-multigrid** assembly path: restricted to square forms (`bilinearform.cpp:158-161`),
it partially assembles the operator at every hierarchy level — reusing `ceed::CeedOperatorCoarsen`
to coarsen the finer level's operator when meshes match across levels (`bilinearform.cpp:170-180`),
else re-assembling from scratch — then applies the per-level PA/FA policy to produce the final
operator vector (`bilinearform.cpp:186-198`). This is the producer of the multigrid operator stack
the `GeometricMultigridSolver` consumes.

## `DiscreteLinearOperator::PartialAssemble` — interpolation + multiplicity scaling

`DiscreteLinearOperator::PartialAssemble` (`bilinearform.cpp:203-282`) mirrors
`BilinearForm::PartialAssemble`'s geometry loop but with two differences: it builds an
**interpolator** basis (`ceed::InitInterpolatorBasis`, `bilinearform.cpp:230-238`) from the trial
and test finite elements rather than a quadrature basis, and each interpolator produces **both** a
sub-operator and its transpose (`interp->Assemble(..., &sub_op, &sub_op_t)`,
`bilinearform.cpp:242-244`). After `Finalize`, it computes a **dof-multiplicity vector**
(`bilinearform.cpp:256-279`): it counts how many elements each test dof is shared by (an
OMP-atomic accumulation over element vdofs), reciprocates it, and installs it via
`SetDofMultiplicity` — this averaging is what makes interpolation between conforming spaces
well-defined at shared dofs (the load-bearing numerical detail of the interpolation path, not
boilerplate).

## Notes for higher layers

- **The PA/FA dual collapses at L1.** Partial and full assembly compute the same local operator
  action; the L1 form is the single "assemble FE operator from integrator list" map. The
  `pa_order_threshold` dispatch (`bilinearform.hpp:40`, `bilinearform.cpp:115-151`) is the
  performance/representation selector — at L1 a variant axis (matrix-free vs sparse), not two
  operators.
- **`BilinearForm` is fundamentally a fold over integrators.** `AddDomainIntegrator` /
  `AddBoundaryIntegrator` build a list; assembly folds each integrator's contribution into one
  `ceed::Operator` via `AddSubOperator`. At L2 this is the natural "sum of weak-form terms"
  algebra — the operator is `Σ_i integ_i` over domain + boundary terms. The OMP-parallel
  composite-build is a transparent trick over that fold.
- **`DiscreteLinearOperator` is the interpolation variant of the same fold**, differing in (i)
  interpolator vs integrator basis, (ii) transpose-also production, and (iii) the dof-multiplicity
  averaging. At L1 it is a sibling operator (primal→primal interpolation) sharing the assembly
  skeleton; the multiplicity scaling is its load-bearing numerical content.
- **The multigrid-hierarchy `Assemble` overload is the multigrid-operator-stack producer.** It
  lifts as the construction side of the geometric-multigrid V-cycle algebra (the apply side lives
  in `GeometricMultigridSolver`, [`preconditioner-classes-overview`](./preconditioner-classes-overview.md)).
- **OMP threading and libCEED `Ceed`-per-thread are single-machine performance machinery.** Read
  single-rank / single-thread per [`par-types-single-rank-reading`](./par-types-single-rank-reading.md);
  the per-thread composite-operator build (`bilinearform.cpp:48-101`) is a transparent trick — the
  assembled operator is independent of thread count.

## Referenced from

*Forward-declared. L1 work on the FE-assembly operator (the integrator-fold and PA/FA variant axis,
queued as FE-space material reaches the frontier) will reference this chapter.*

- [`L0/linalg-rap-file`](./linalg-rap-file.md) — the parallel-operator wrapper whose
  `ParallelAssemble` calls `BilinearForm::FullAssemble` (`rap.cpp:100`); this chapter is the
  local-operator producer that feeds `ParOperator`'s `A`.
- [`L0/par-types-single-rank-reading`](./par-types-single-rank-reading.md) — the libCEED-parallel /
  `HypreCSRMatrix` / OMP single-rank reading rule applied throughout.
- [`L0/transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md) — the
  partial-vs-full performance dual + OMP-parallel-build classification.
- [`L0/preconditioner-classes-overview`](./preconditioner-classes-overview.md) — the
  `GeometricMultigridSolver` consuming the multigrid-hierarchy `Assemble` output.

## Evidence (representative)

- `palace/fem/bilinearform.hpp:1-136` — the header file (136 lines).
- `palace/fem/bilinearform.hpp:14` — `namespace palace` open; `bilinearform.hpp:17-18` — forward decls of `FiniteElementSpace` / `FiniteElementSpaceHierarchy`.
- `palace/fem/bilinearform.hpp:21-23` — class doc comment (the authoritative reading: integrators assembled via libCEED, partial or full).
- `palace/fem/bilinearform.hpp:25-91` — `class BilinearForm` body.
- `palace/fem/bilinearform.hpp:29,32` — trial/test space refs + `domain_integs` / `boundary_integs` integrator lists.
- `palace/fem/bilinearform.hpp:40` — `inline static int pa_order_threshold = 1;` (the PA/FA dispatch threshold).
- `palace/fem/bilinearform.hpp:53-63` — templated `AddDomainIntegrator<T>` / `AddBoundaryIntegrator<T>` (build-up-the-form-list).
- `palace/fem/bilinearform.hpp:67-90` — `PartialAssemble` / `FullAssemble` / `Assemble` public surface + overload chains.
- `palace/fem/bilinearform.hpp:95-132` — `class DiscreteLinearOperator` body (interpolation sibling).
- `palace/fem/bilinearform.hpp:102` — `domain_interps` (owned `DiscreteInterpolator` list); `bilinearform.hpp:122-131` — `FullAssemble` forwarding with `set=true`.
- `palace/fem/bilinearform.cpp:1-284` — the source file (284 lines).
- `palace/fem/bilinearform.cpp:15-25` — `AssembleQuadratureData` (delegates to each integrator).
- `palace/fem/bilinearform.cpp:27-107` — `BilinearForm::PartialAssemble`: mesh check (31-32), empty `ceed::SymmetricOperator`/`Operator` (37-46), OMP-parallel per-geometry loop (51-101) with domain (61-79) + boundary (80-99) integrator sub-operator assembly, `Finalize` (104).
- `palace/fem/bilinearform.cpp:109-113` — `BilinearForm::FullAssemble`: forwards to `ceed::CeedOperatorFullAssemble(op, skip_zeros, set)`.
- `palace/fem/bilinearform.cpp:115-139` — anonymous-namespace `UseFullAssembly` (order-vs-threshold PA/FA policy; the source comment at 121-123 names MFEM's `RT_FECollection` as the historical `order + 1` quirk the `+ 1` normalization at 126-131 corrects).
- `palace/fem/bilinearform.cpp:141-151` — `BilinearForm::Assemble(bool)`: the public PA/FA dispatch entry point.
- `palace/fem/bilinearform.cpp:153-201` — `BilinearForm::Assemble(FiniteElementSpaceHierarchy, ...)`: multigrid-hierarchy assembly with `CeedOperatorCoarsen` reuse (170-180) + per-level policy (186-198).
- `palace/fem/bilinearform.cpp:203-282` — `DiscreteLinearOperator::PartialAssemble`: interpolator basis (230-238), sub-op + transpose (242-244), dof-multiplicity scaling vector (256-279).
```

### 2. `book/src/L0/index.md` — add the row to the "File overviews" cohort

```edit:book/src/L0/index.md
[old]: - [`linalg-rap-file`](./linalg-rap-file.md) — `palace/linalg/rap.{hpp,cpp}` at a glance. The home of the **R·A·P (Galerkin) parallel-operator** family: `ParOperator` (real-valued) and `ComplexParOperator` (complex-valued, real/imag-split into two owned `ParOperator`s), plus the `BuildParSumOperator` weighted-summation family. Turns a local (L-vector) FE operator into a parallel (true-dof) one either matrix-free (prolongate-apply-restrict sandwich) or assembled (one `HypreParMatrix` triple product); the two paths are an algebraically-equivalent performance dual. The L0 file-level home for the `ParOperator` member of the [`apply-linop-overload-set`](./apply-linop-overload-set.md) family.
[new]: - [`linalg-rap-file`](./linalg-rap-file.md) — `palace/linalg/rap.{hpp,cpp}` at a glance. The home of the **R·A·P (Galerkin) parallel-operator** family: `ParOperator` (real-valued) and `ComplexParOperator` (complex-valued, real/imag-split into two owned `ParOperator`s), plus the `BuildParSumOperator` weighted-summation family. Turns a local (L-vector) FE operator into a parallel (true-dof) one either matrix-free (prolongate-apply-restrict sandwich) or assembled (one `HypreParMatrix` triple product); the two paths are an algebraically-equivalent performance dual. The L0 file-level home for the `ParOperator` member of the [`apply-linop-overload-set`](./apply-linop-overload-set.md) family.
- [`fem-bilinearform-file`](./fem-bilinearform-file.md) — `palace/fem/bilinearform.{hpp,cpp}` at a glance. The home of the **finite-element assembly entry point**: `BilinearForm` (integrator-list → assembled operator) and `DiscreteLinearOperator` (interpolator-list → inter-space interpolation operator). The load-bearing surface is the **partial-assembly (matrix-free libCEED `ceed::Operator`) vs full-assembly (`hypre::HypreCSRMatrix`)** dual, dispatched by polynomial order against `pa_order_threshold`, plus the FE-space-hierarchy multigrid-operator-stack producer. The local-operator producer feeding [`linalg-rap-file`](./linalg-rap-file.md)'s `ParOperator` (`rap.cpp:100` calls `BilinearForm::FullAssemble`).
```

### 3. `book/src/SUMMARY.md` — register the chapter under the L0 Part

```edit:book/src/SUMMARY.md
[old]: - [File — palace/linalg/rap.{hpp,cpp}](./L0/linalg-rap-file.md)
- [File — palace/utils/communication.hpp (MPI collectives)](./L0/mpi-globalsum-and-collectives.md)
[new]: - [File — palace/linalg/rap.{hpp,cpp}](./L0/linalg-rap-file.md)
- [File — palace/fem/bilinearform.{hpp,cpp}](./L0/fem-bilinearform-file.md)
- [File — palace/utils/communication.hpp (MPI collectives)](./L0/mpi-globalsum-and-collectives.md)
```

## Supporting evidence

- File sizes confirmed via `wc -l`: `bilinearform.hpp` 136 lines, `bilinearform.cpp` 284 lines (420 total) — small enough for one focused chapter.
- Class names confirmed via codemap + full read: `BilinearForm` (`bilinearform.hpp:25-91`), `DiscreteLinearOperator` (`bilinearform.hpp:95-132`). The planner did not pre-verify; both are correct.
- Direct callee relationship to the cycle-014 `rap` chapter confirmed: `palace/linalg/rap.cpp:100` — `data_sA = BilinearForm::FullAssemble(*cA, skip_zeros, use_R);` (codemap `search_text`).
- Upstream callers (model pipelines that construct `BilinearForm` / `DiscreteLinearOperator`): `palace/models/{spaceoperator,laplaceoperator,curlcurloperator,modeeigensolver,romoperator,domainpostoperator}.cpp` (codemap `grep`). These are the L1-frontier consumers that will eventually back-reference this chapter.
- Downstream callee of the assembly bodies: `ceed::CeedOperatorFullAssemble` + `ceed::CeedOperatorCoarsen` both live in `palace/fem/libceed/operator.cpp` (`bilinearform.cpp:112,174`; codemap confirms defs at `libceed/operator.cpp:455,525`).

## Open questions / caveats

- **Scoping decision (resolved, recorded here):** FOCUSED single chapter, no split. 420 total lines
  is small (cf. rap's ~979). All 9 anchor surfaces fit one coherent chapter without transcription.
  No OQ needed on scope.
- **Bundle-6 ranking update (next candidate after `fem-bilinearform-file`):** the assembly bodies
  here both forward into **`palace/fem/libceed/operator.cpp`** — `ceed::CeedOperatorFullAssemble`
  (def `libceed/operator.cpp:455`) materializes the `HypreCSRMatrix`, and `ceed::CeedOperatorCoarsen`
  (def `libceed/operator.cpp:525`) does the multigrid coarsening. That file is the natural
  **next-ranked bundle-6 candidate (#5)** — it is the direct callee that this chapter defers to for
  the actual matrix-materialization and operator-coarsening algebra, and it holds the `ceed::Operator`
  base class this chapter's `PartialAssemble` constructs. **Suggest cycle-016 plan it next.** (Assess
  its size first — `libceed/operator.cpp` may be large enough to warrant a focused-subset chapter.)
- **Alternative #5 candidate:** `palace/fem/fespace.{hpp,cpp}` (the `FiniteElementSpace` /
  `FiniteElementSpaceHierarchy` types this chapter takes by reference, providing
  `GetCeedElemRestriction` / `GetCeedBasis` / `GetVSize`). It is the *input-side* anchor where
  `libceed/operator.cpp` is the *output-side* anchor. Ranking leans toward `libceed/operator.cpp`
  (the direct FullAssemble/Coarsen callee, tighter coupling to the assembly algebra); `fespace` is a
  larger, more foundational surface better scheduled once more FE-frontier L1 work pulls on it.
- **`AssembleQuadratureData` (`bilinearform.cpp:15-25`)** is a thin pre-assembly hook delegating to
  each integrator's own `AssembleQuadratureData`. Cited but not chunked as a major anchor — it is
  setup boilerplate; the integrator-side quadrature-data assembly belongs to a future
  `fem/integrator.{hpp,cpp}` chapter, not this one.

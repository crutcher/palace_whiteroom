---
agent: layer-intro-author
invoked_at: 2026-05-27T16:07:28Z
scope: L0 bootstrap bundle 3 (priority #10 continuation)
status: integrated
integrated_at: 2026-05-27T17:17:02Z
integration_commit: 693f058
integration_notes: |
  Applied cycle-007 wave-1 per-report dispatch 1 of 6 at 17:00:00Z; finalized in batch cycle-007 at 17:17:02Z.
  Files created: book/src/L0/{mfem-wrapper-solver,linalg-iterative-file,mutable-workspace-pattern}.md (3 new L0 reference chapters).
  Files edited: book/src/L0/index.md (3 dep-map rows across Conventions / File overviews / Overload sets and class interfaces groupings, alphabetical-within-grouping), book/src/SUMMARY.md (3 L0 Part inserts).
  4 OQs promoted: mfem-wrapper-solver-l4-complex-from-real-lift-backref, iterative-file-helper-citation-granularity, eigensolver-wrapper-l0-bundle-4-candidate, mutable-workspace-category-4-split-decision.
  Effectively closes cycle-006 OQ mfemwrappersolver-l0-coverage-candidate (chapter landed).
  L0 chapter count: 8 → 11. Gate hits: 0.
---

# CYCLE: L0 bootstrap bundle 3

## Summary

Adds **3 new L0 reference-note chapters** to bundle 3 of priority #10's bootstrap, bringing the L0 reference-notes overlay from 8 chapters (post-cycle-006 bundle-2) to 11. Each chapter follows the cycle-005/cycle-006 precedent shape (at-a-glance / key prose sections / notes for higher layers / Referenced from / Evidence) and stays within the 2-4 paragraphs-plus-citations discipline per chapter set in `book/src/L0/index.md`.

The three chapters:

1. **`mfem-wrapper-solver.md`** — the adapter class `MfemWrapperSolver<OperType>` that lifts MFEM's real-only `mfem::Solver` hierarchy into Palace's templated `Solver<OperType>` hierarchy. Closes open question `mfemwrappersolver-l0-coverage-candidate` (cycle-006). Anchors the preconditioner-side construction surface.
2. **`linalg-iterative-file.md`** — file-overview of `palace/linalg/iterative.{hpp,cpp}`: the abstract base `IterativeSolver<OperType>` plus the three concrete subclasses (`CgSolver`, `GmresSolver`, `FgmresSolver`). Sibling to `ksp-factory-file` (which is the *construction* side); directly unblocks the cycle-007 dispatch #5 `l1-ksp-solve @ L1` harvest by providing the L0 anchor for the implemented-Krylov-solver surface.
3. **`mutable-workspace-pattern.md`** — names the pervasive `mutable` workspace-member convention that L1>L0 mutation-rotation themes implicitly rely on (workspace mention-and-erase). Anchor for upcoming L1>L0 themes that have multi-step L0 bodies (operator composition, iterative solves, eigensolver wrappers). The cycle-005 `apply-linop-mutation-rotation` theme already cites the `BaseProductOperator::z` workspace inline; this chapter generalises the pattern.

Plus updates to `book/src/L0/index.md` adding the new chapters to the Reference-note cohort sections (Conventions + File overviews + Overload sets and class interfaces — splits across two of the three existing groupings) and to `book/src/SUMMARY.md` adding the three new entries to the L0 Part list.

## Proposed changes

```edit:book/src/L0/mfem-wrapper-solver.md
[old]: (new file)
[new]: <contents of reports/2026-05-27T160728Z-layer-intro-author-L0-bootstrap-bundle-3/mfem-wrapper-solver.md>
```

```edit:book/src/L0/linalg-iterative-file.md
[old]: (new file)
[new]: <contents of reports/2026-05-27T160728Z-layer-intro-author-L0-bootstrap-bundle-3/linalg-iterative-file.md>
```

```edit:book/src/L0/mutable-workspace-pattern.md
[old]: (new file)
[new]: <contents of reports/2026-05-27T160728Z-layer-intro-author-L0-bootstrap-bundle-3/mutable-workspace-pattern.md>
```

```edit:book/src/L0/index.md
[old]: ## Reference-note cohort

**Conventions** — cross-cutting Palace / MFEM idioms referenced by L1 entries:

- [`output-arg-vs-receiver`](./output-arg-vs-receiver.md) — `A.Mult(x, y)` writes `y` vs receiver-mutating `y.Add(α, x)` / `y *= s`; how L1 lifts both into pure-functional form.
- [`mfem-vector-types`](./mfem-vector-types.md) — `Vector` / `ComplexVector` duality (element-type axis); single-rank reading of `Par*` types per `CLAUDE.md` "Scope".
- [`linalg-free-functions`](./linalg-free-functions.md) — `linalg::AXPY` / `linalg::Dot` / `linalg::Norml2` as template-dispatch wrappers over the method-form surface; the wrapping pattern Palace uses across `vector.hpp`.
- [`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md) — Operational L0 classification (lifted from `CLAUDE.md`): `α == 1.0` branch in `AXPY` is transparent; reduction-tree non-associativity is load-bearing. Worked examples from the BLAS-1 family.

**File overviews** — anchor files L1 references repeatedly:

- [`linalg-vector-file`](./linalg-vector-file.md) — `palace/linalg/vector.{hpp,cpp}` at a glance. The home of `ComplexVector`, the `AXPY/AXPBY/AXPBYPCZ` family, `Dot`/`TransposeDot`/`LocalDot`, `Norml2`, `Normalize`.
- [`ksp-factory-file`](./ksp-factory-file.md) — `palace/linalg/ksp.cpp` Krylov-solver factory. Enum-routed dispatch: CG / GMRES / FGMRES implemented; MINRES / BICGSTAB / DEFAULT abort. Anchor for the "advertised-but-unimplemented" pattern that drives the MINRES / BiCGStab obstruction themes.

**Overload sets and class interfaces** — multi-overload / multi-subclass surfaces referenced by L1 / L2 / L4 entries:

- [`apply-linop-overload-set`](./apply-linop-overload-set.md) — the `Mult` / `MultTranspose` / `MultHermitianTranspose` / `AddMult` family on the `Operator` / `ComplexOperator` hierarchy, plus the concrete-subclass family (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `BaseMultigridOperator`, `ComplexWrapperOperator`, `ParOperator`). The L0 anchor for `L1/apply_linop`'s 12-method-overload collapse and for the `apply-linop-mutation-rotation` lowering theme.
- [`kspsolver-base-class`](./kspsolver-base-class.md) — `BaseKspSolver<OperType>` in `palace/linalg/ksp.{hpp,cpp}`. The composition class pairing an `IterativeSolver` with a `Solver` (preconditioner) and exposing the public `Mult(b, x)` "solve `Ax = b`" entry point. Anchors the L4 `solve-monad` concept to concrete C++ and is the call-site target for solver use across Palace's model pipelines.

[new]: ## Reference-note cohort

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
```

```edit:book/src/SUMMARY.md
[old]: # L0 — Cited Palace Source + Reference Notes
- [Overview](./L0/index.md)
- [Convention — output-arg vs receiver](./L0/output-arg-vs-receiver.md)
- [Convention — MFEM vector types](./L0/mfem-vector-types.md)
- [Convention — linalg:: free-function wrappers](./L0/linalg-free-functions.md)
- [Convention — transparent vs load-bearing tricks](./L0/transparent-vs-load-bearing-tricks.md)
- [File — palace/linalg/vector.{hpp,cpp}](./L0/linalg-vector-file.md)
- [File — palace/linalg/ksp.cpp](./L0/ksp-factory-file.md)
- [Overload set — Mult / MultTranspose / AddMult](./L0/apply-linop-overload-set.md)
- [Class — BaseKspSolver](./L0/kspsolver-base-class.md)
[new]: # L0 — Cited Palace Source + Reference Notes
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
```

## Supporting evidence

### Chapter shape precedent

The three new chapters mirror the cycle-006 bundle-2 precedent (`book/src/L0/kspsolver-base-class.md` and `book/src/L0/apply-linop-overload-set.md`):

- Lead with "A reference note for ..." one-sentence framing of who consumes the chapter.
- "At a glance" section with the type / class shape and the one-or-two-line summary.
- Two-to-four interpretive sections naming load-bearing semantic content (constructor flow, method specialisations, dispatch helpers, etc.).
- "Notes for higher layers" section with 3–5 forward-pointer bullets.
- "Referenced from" section with predicted cross-citation targets (currently mostly forward-declared since the L1 / L1>L0 themes that will cite these chapters are still to be authored or thinned).
- "Evidence (representative)" section with 15-30 file:line citations covering the cited ranges.

All three chapters stay within the 2-4 paragraphs-plus-citations discipline set by `book/src/L0/index.md` (none exceeds ~270 lines).

### Source-range verification

Every citation in the three chapters was verified against the local `reference/palace/` clone at the cycle-007 time of authorship:

- `palace/linalg/solver.hpp` (138 lines) — full read; class declarations at lines 21-65 and 70-134 confirmed.
- `palace/linalg/solver.cpp` (209 lines) — full read; method specialisations at lines 12-30, 33-136, 138-142, 144-177, 179-207 confirmed.
- `palace/linalg/iterative.hpp` (279 lines) — full read; class declarations at lines 25-115, 117-150, 152-217, 219-275 confirmed.
- `palace/linalg/iterative.cpp` (882 lines) — line-anchored read of grep-localised regions (lines 21-358 free-function helpers, 360-486 CG `Mult`, 488-541 GMRES `Initialize`/`Update`, 543-705 GMRES `Mult`, 707-731 FGMRES `Initialize`/`Update`, 733-870 FGMRES `Mult`, 873-880 explicit instantiations).
- `palace/linalg/operator.hpp` (407 lines) — partial read of lines 73-227 (operator subclasses with workspaces) and lines 21-72 (ComplexOperator abstract base); cited line ranges 73-113, 116-136, 178-226, 192, 81, 120 confirmed.
- `palace/linalg/operator.cpp` (698 lines) — partial read of lines 410-507 (SumOperator + BaseDiagonalOperator); cited ranges 415-419, 428-441, 458-466, 468-476, 478-507 confirmed.
- `palace/linalg/ksp.cpp` (lines 95-130) — `MakeWrapperSolver` template helper at lines 103-123 confirmed.
- `palace/linalg/floquetcorrection.hpp` (64 lines total) — `FloquetCorrSolver` class at lines 32-60; `mutable VecType rhs` at line 49 confirmed.

Grep-verified citations (not full read; signatures confirmed only) — used sparingly for the "where MfemWrapperSolver is used" enumeration and the Category-3 eigensolver-wrapper workspace examples:

- `palace/linalg/divfree.cpp:120`, `palace/linalg/hcurl.cpp:92`, `palace/linalg/errorestimator.cpp:88, 94`, `palace/models/modeeigensolver.cpp:666, 733, 742, 749, 761, 774` — `MfemWrapperSolver` construction call sites (`std::make_unique<MfemWrapperSolver<...>>` matches across `reference/palace/palace/`; total 11 sites including the `palace/linalg/ksp.cpp:120` central call site). Note: `modeeigensolver.cpp:727` is a type-signature reference in a lambda return type, not a construction call site.
- `palace/linalg/arpack.hpp:88, 215`, `palace/linalg/slepc.hpp:83, 302`, `palace/linalg/nleps.hpp:72, 265` — Category-3 eigensolver wrapper workspaces (grep `mutable ComplexVector` across `reference/palace/palace/linalg/`).

Per the L0 reference-note discipline (2-4 paragraphs of interpretation + representative citations, no line-by-line transcription), this is sufficient for the function-presence and one-line interpretive claims the chapters make. A future cross-cutter or lowering-verifier audit that needs to extract algebraic detail from the eigensolver-wrapper / preconditioner-call-site bodies would need to re-read those ranges in full.

### Open-questions closures unblocked

Three open questions are referenced from these chapters and approach closure:

1. **`mfemwrappersolver-l0-coverage-candidate` (cycle-006)** — closed by `mfem-wrapper-solver.md`. The chapter is the future L0 anchor for the preconditioner-side construction surface flagged in the cycle-006 open question.
2. **`l1-ksp-solve-firm-up-anchor-ready` (cycle-006)** — partially advanced. `kspsolver-base-class` (cycle-006) was the first L0 anchor for `L1/ksp_solve`; `linalg-iterative-file` (this cycle) is the second, providing the per-implementation detail needed for the cycle-007 dispatch #5 harvester to firm `l1-ksp-solve`.
3. **`apply-linop-workspace-tensor-reading-at-L0` (cycle-005)** — partially advanced. `mutable-workspace-pattern` chapter generalises the workspace-mention-and-erase rewrite rule across the operator-composition family; the future `lowering-verifier` audit named in the cycle-005 OQ now has a single chapter to consult rather than re-deriving the discipline per call-site.

### Dep-map updates

The L0 index dep-map gains 3 rows distributed across the existing 3 groupings:

- **Conventions** (was 4, becomes 5): + `mutable-workspace-pattern` (after `transparent-vs-load-bearing-tricks`, alphabetical).
- **File overviews** (was 2, becomes 3): + `linalg-iterative-file` (after `ksp-factory-file`, alphabetical).
- **Overload sets and class interfaces** (was 2, becomes 3): + `mfem-wrapper-solver` (after `kspsolver-base-class`, alphabetical).

SUMMARY.md gains 3 corresponding rows, also inserted in alphabetical order within each grouping.

## Open questions / caveats

1. **`mfem-wrapper-solver.md` references `complex-from-real-lift` as the L4 concept on the preconditioner side, but the L4 lift theme has not been authored.** The reference is forward-looking. When the L4 form of `complex-from-real-lift` is firmed (or the existing `book/src/concepts/complex-from-real-lift.md` is promoted to L4), the back-reference should be added to the chapter's "Referenced from" section. Routes to whichever cycle promotes `complex-from-real-lift` to firm L4. (Not blocking the bundle; the chapter's forward-pointer wording is defensive.)

2. **`linalg-iterative-file.md` cites `iterative.cpp:34-241` as "Sundry small-dense linear-algebra utilities" without enumerating each helper at the per-template-overload level.** The chapter's "Free-function helpers" section names the five primary anonymous-namespace helpers (`CheckDot`, `ApplyB`, `InitialResidual`, `ApplyBA`, `OrthogonalizeIteration`) explicitly with line ranges, and identifies the small-dense kernel helpers (`SafeMin`/`SafeMax`, `GeneratePlaneRotation` real+complex, `ApplyPlaneRotation` real+complex). The cycle-007 `l1-ksp-solve` harvester may want a more granular per-overload helper enumeration (separating real and complex specialisations) if the small-dense kernel becomes load-bearing for the L1 form; routes to cycle-007+ harvester or a future thinning sweep.

3. **`mutable-workspace-pattern.md`'s Category 3 (solver workspaces) lists the eigensolver-wrapper instances (`arpack.hpp:88, 215`; `slepc.hpp:83, 302`; `nleps.hpp:72, 265`) as grep-verified-only.** The eigensolver wrappers themselves have not been read at L0; their workspace usage is documented here purely on the basis of grep-located `mutable ComplexVector` members. A future L0 bundle (bundle 4 or beyond) could author a dedicated eigensolver-wrapper reference note that reads these wrappers in full; the workspace pattern reference here is sufficient for the cross-cutting concern (the workspace-mention-and-erase rewrite is the same regardless of wrapper specifics) but not for a full eigensolver-side L0 audit. Routes to future L0 bundle.

4. **`mutable-workspace-pattern.md`'s Category 4 (`MfemWrapperSolver::A` retained-assembled-matrix) is a slight stretch of the "mutable workspace" name** — the `A` member is `std::unique_ptr<mfem::HypreParMatrix>`, not `mutable`, and the lifecycle is tied to `SetOperator` invocations rather than per-`Mult` lazy-resize. The pattern is *related* (lazy allocation, reuse across calls, instance-scoped lifetime) but mechanically different. The chapter calls this out explicitly in its Category 4 prose. If a future cross-cutter (or a critic on this report) thinks Category 4 should be in a sibling chapter rather than this one, the split is clean: extract Category 4 into a new `retained-assembled-matrix-pattern.md` chapter and have `mutable-workspace-pattern.md` link to it. Bundle-3 keeps them together for the workspace-discipline-as-cohort framing; a future cycle could split. Routes to cross-cutter or layer-intro-author follow-up.

5. **Codemap MCP tools were not used during this dispatch.** The candidate-source files are well-localised (`palace/linalg/*.{hpp,cpp}` and `palace/models/modeeigensolver.cpp`) and a single grep + targeted Read calls were sufficient. Per the dispatch instruction's caveat note, codemap-tools usage is not mandatory; the primary codemap pilot is dispatch #1 (harvester `iterate_while`). This caveat is filed for completeness — no codemap-tool observations to report.

6. **The "Referenced from" sections of all three chapters are mostly forward-declared.** Existing L1 / L1>L0 entries do not yet cite the new chapters; the prediction is that the cycle-007+ retroactive-thinning sweep (priority #11) and the cycle-007+ `l1-ksp-solve` harvest will populate these back-references. Until then, the "Referenced from" lists are forward-looking. The cycle-006 chapters (`kspsolver-base-class`, `apply-linop-overload-set`) used the same convention; their "Referenced from" lists are also still forward-looking pending the same future work. Pattern is consistent across L0 bundle-2 and bundle-3.

7. **Bundle 4+ candidates from the planner's list NOT included in this bundle:**
   - **`par-types-single-rank-reading`** — partially covered by existing `mfem-vector-types.md` (which already cites the single-rank reading per CLAUDE.md Scope). A dedicated chapter could explicitly catalogue the `Par*` types (`ParGridFunction`, `ParBilinearForm`, `HypreParVector`, `ParOperator`, `ParFiniteElementSpace`); deferred to bundle 4+.
   - **`linalg-operator-file`** — the existing `apply-linop-overload-set.md` chapter (cycle-006) already covers most of `palace/linalg/operator.{hpp,cpp}`'s content (the operator hierarchy + concrete subclasses). A full file-overview chapter would mostly duplicate; if needed, it would focus on the non-class content (free functions, helper templates outside the overload-set scope). Deferred to bundle 4+ if a need emerges.
   - **`mpi-globalsum-and-collectives`** — MPI is single-rank-reading-only per CLAUDE.md Scope; a dedicated chapter would mostly be "this is out of scope at multi-rank semantics; here are the call sites we read as single-rank." Low priority; deferred indefinitely.
   - **`tests-as-semantic-supplement`** — better-classified as a methodology / concepts-page topic than an L0 reference note (the convention is project-level, not Palace-specific). Routes to a `concepts/` page if needed; not an L0 bundle candidate.

   No new open-questions filed for these deferrals — the planner's list already names them as candidates; their non-inclusion this cycle is a bundle-scope decision, not new ground.

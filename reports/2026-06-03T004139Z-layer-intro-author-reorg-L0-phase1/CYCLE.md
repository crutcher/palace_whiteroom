---
agent: layer-intro-author
invoked_at: 2026-06-03T004139Z
scope: cycle-071 D5 — directive-3 mdBook reorg of L0 + Phase-1-corpus Parts
status: integrated
integrated_at: 2026-06-03T021500Z
integration_commit: e0fae18eddb2b5c842d260d5e2a79258d43a6a70
integration_notes: |
  cycle-071 D5, applied clean by integrator-per-report (STAGING row 5), finalized by integrator-finalize.
  PURE STRUCTURAL directive-3 reorg of the L0 + Phase-1-corpus Parts. L0 SUMMARY nested into 3 source-area
  groupings (conventions 6 / file-overviews 11 / overload-sets-and-classes 5 = 22) with 3 new
  book/src/L0/{conventions,file-overviews,overload-sets-and-classes}-intro.md pages; Phase-1 corpus flat alpha
  re-sort of the 9 slice sub-entries (raw-material reference list — correctly NOT kind-grouped). L0/index is
  prose-only (no dep-map table — no in-index re-sort in scope). 22 L0 chapters + 9 Phase-1 slices preserved
  (set-equality EXACT; planner-awk "10 Phase-1" was wrong, 9 confirmed). NO count changes, NO status flips, NO
  dropped chapters. citecheck 0 citations (pure structural, clean). cargo make book exit 0, linkcheck2 clean,
  all 3 intro pages render.
---

# CYCLE: L0 + Phase-1-corpus directive-3 structural reorg

## Summary

D5 of the cycle-071 directive-3 one-time mdBook structural-reorg wave. Scope: the
`# L0` and `# Phase 1 corpus` blocks of `book/src/SUMMARY.md` only.

**Decisions:**

- **L0 (22 chapters + Overview): NESTED into 3 source-area kind groupings.** The
  L0 Part already documents exactly three natural cohorts in its `index.md` prose
  (§Reference-note cohort splits them into **Conventions**, **File overviews**, and
  **Overload sets and class interfaces**). This is a clear ≥2-kind natural split
  (6 / 11 / 5 chapters), well above the small-Part guard, so it warrants nesting +
  per-group intro pages. Three group-intro pages authored
  (`conventions-intro.md`, `file-overviews-intro.md`,
  `overload-sets-and-classes-intro.md`), each a short orientation mirroring the
  matching `index.md` cohort paragraph.
- **L0 chapters alpha-sorted by slug within each grouping** (alpha-within-cohort).
  Every existing chapter link preserved verbatim (titles unchanged); only re-ordered
  and nested under its group intro.
- **Phase 1 corpus (9 slices + Index): FLAT, alpha-sorted, NO kind grouping** — per
  the dispatch directive it is a raw-material reference list, not a vocabulary layer.
  The 9 slice sub-entries (already nested under the `spec/index.md` Index chapter)
  are re-sorted alphabetically by title. The `spec/index.md` Index chapter itself is
  left as-is (it is the group's own index, not a kind grouping).
- **No L0/index.md table re-sort needed.** `book/src/L0/index.md` carries NO dep-map /
  list-of-API table — it is prose with per-cohort bullet lists. No table sort applies.
  (Optional follow-up alpha-sort of the index bullet lists is noted as an open question,
  not applied, to keep this dispatch to the structural SUMMARY reorg.)

22 L0 chapters preserved (6 Conventions + 11 File overviews + 5 Overload-sets/classes),
9 Phase-1 slices preserved. No chapter dropped or renamed.

## Proposed changes

### 1. `book/src/SUMMARY.md` — L0 + Phase-1 region reorg

```edit:book/src/SUMMARY.md
[old]:
# L0 — Cited Palace Source + Reference Notes
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
- [File — palace/linalg/orthog.hpp](./L0/linalg-orthog-file.md)
- [File — palace/linalg/solver.{hpp,cpp}](./L0/linalg-solver-file.md)
- [File — palace/linalg/rap.{hpp,cpp}](./L0/linalg-rap-file.md)
- [File — palace/fem/bilinearform.{hpp,cpp}](./L0/fem-bilinearform-file.md)
- [File — palace/fem/libceed/operator.{hpp,cpp}](./L0/fem-libceed-operator-file.md)
- [File — palace/fem/fespace.{hpp,cpp}](./L0/fespace-file.md)
- [File — palace/utils/communication.hpp (MPI collectives)](./L0/mpi-globalsum-and-collectives.md)
- [Overload set — Mult / MultTranspose / AddMult](./L0/apply-linop-overload-set.md)
- [Class — BaseKspSolver](./L0/kspsolver-base-class.md)
- [Class — MfemWrapperSolver](./L0/mfem-wrapper-solver.md)
- [Class — EigenvalueSolver and wrappers](./L0/eigensolver-wrapper.md)
- [Class — preconditioner classes overview](./L0/preconditioner-classes-overview.md)
# Phase 1 corpus (slice-vertical; raw material for combinator extraction)
- [Index — Slice Status](./spec/index.md)
  - [CG — Preconditioned Conjugate Gradient](./spec/slices/cg.md)
  - [GMRES](./spec/slices/gmres.md)
  - [Orthogonalisation (MGS / CGS / CGS2)](./spec/slices/orthog.md)
  - [Divergence-free projection](./spec/slices/divfree.md)
  - [Arnoldi step](./spec/slices/arnoldi_step.md)
  - [Plane rotation stream](./spec/slices/plane_rotation_stream.md)
  - [Sparse triangular solve (negative result)](./spec/slices/sparse_triangular_solve.md)
  - [CG Preconditioning Framework](./spec/slices/cg_preconditioning_framework.md)
  - [Polynomial recurrence step](./spec/slices/polynomial_recurrence_step.md)
[new]:
# L0 — Cited Palace Source + Reference Notes
- [Overview](./L0/index.md)
- [Conventions](./L0/conventions-intro.md)
  - [Convention — linalg:: free-function wrappers](./L0/linalg-free-functions.md)
  - [Convention — MFEM vector types](./L0/mfem-vector-types.md)
  - [Convention — mutable workspace pattern](./L0/mutable-workspace-pattern.md)
  - [Convention — output-arg vs receiver](./L0/output-arg-vs-receiver.md)
  - [Convention — Par* types and single-rank reading](./L0/par-types-single-rank-reading.md)
  - [Convention — transparent vs load-bearing tricks](./L0/transparent-vs-load-bearing-tricks.md)
- [File overviews](./L0/file-overviews-intro.md)
  - [File — palace/fem/bilinearform.{hpp,cpp}](./L0/fem-bilinearform-file.md)
  - [File — palace/fem/libceed/operator.{hpp,cpp}](./L0/fem-libceed-operator-file.md)
  - [File — palace/fem/fespace.{hpp,cpp}](./L0/fespace-file.md)
  - [File — palace/linalg/ksp.cpp](./L0/ksp-factory-file.md)
  - [File — palace/linalg/iterative.{hpp,cpp}](./L0/linalg-iterative-file.md)
  - [File — palace/linalg/operator.{hpp,cpp}](./L0/linalg-operator-file.md)
  - [File — palace/linalg/orthog.hpp](./L0/linalg-orthog-file.md)
  - [File — palace/linalg/rap.{hpp,cpp}](./L0/linalg-rap-file.md)
  - [File — palace/linalg/solver.{hpp,cpp}](./L0/linalg-solver-file.md)
  - [File — palace/linalg/vector.{hpp,cpp}](./L0/linalg-vector-file.md)
  - [File — palace/utils/communication.hpp (MPI collectives)](./L0/mpi-globalsum-and-collectives.md)
- [Overload sets & class interfaces](./L0/overload-sets-and-classes-intro.md)
  - [Overload set — Mult / MultTranspose / AddMult](./L0/apply-linop-overload-set.md)
  - [Class — EigenvalueSolver and wrappers](./L0/eigensolver-wrapper.md)
  - [Class — BaseKspSolver](./L0/kspsolver-base-class.md)
  - [Class — MfemWrapperSolver](./L0/mfem-wrapper-solver.md)
  - [Class — preconditioner classes overview](./L0/preconditioner-classes-overview.md)
# Phase 1 corpus (slice-vertical; raw material for combinator extraction)
- [Index — Slice Status](./spec/index.md)
  - [Arnoldi step](./spec/slices/arnoldi_step.md)
  - [CG — Preconditioned Conjugate Gradient](./spec/slices/cg.md)
  - [CG Preconditioning Framework](./spec/slices/cg_preconditioning_framework.md)
  - [Divergence-free projection](./spec/slices/divfree.md)
  - [GMRES](./spec/slices/gmres.md)
  - [Orthogonalisation (MGS / CGS / CGS2)](./spec/slices/orthog.md)
  - [Plane rotation stream](./spec/slices/plane_rotation_stream.md)
  - [Polynomial recurrence step](./spec/slices/polynomial_recurrence_step.md)
  - [Sparse triangular solve (negative result)](./spec/slices/sparse_triangular_solve.md)
```

### 2. NEW FILE `book/src/L0/conventions-intro.md` — Conventions group intro

```create:book/src/L0/conventions-intro.md
# Conventions

Cross-cutting Palace / MFEM idioms that L1 operator entries reference rather than
re-state inline. Each convention chapter names one recurring idiom — a mutation
convention, a type duality, a wrapping pattern, or an optimisation-trick
classification — in 2–4 paragraphs of interpretation plus representative citations.
No line-by-line source duplication.

These are the "what does this L0 citation actually mean" notes: an L1 entry citing
`A.Mult(x, y)` or `linalg::AXPY` or a `mutable Vector z` workspace points at the
matching convention chapter here for the idiom, and keeps its own body focused on
the operator's algebra.

See the [L0 overview](./index.md) §Reference-note cohort for how this cohort sits
alongside the file overviews and the overload-set / class-interface chapters.
```

### 3. NEW FILE `book/src/L0/file-overviews-intro.md` — File overviews group intro

```create:book/src/L0/file-overviews-intro.md
# File overviews

At-a-glance overviews of the Palace source files L1 / L2 / L4 entries reference
repeatedly. Each chapter is a file-level navigation hub: what the file houses (its
key classes / free functions / families), the load-bearing duals it carries, and a
handful of representative citations — enough orientation that an operator entry can
point here for "where does this live" instead of re-deriving the file's shape.

The cohort spans the two primary source regions the layered artifact dissects:
`palace/linalg/` (Krylov solvers, preconditioners, smoothers, orthogonalisation,
vector/operator primitives) and `palace/fem/` (finite-element assembly, FE-space
construction, libCEED operators), plus the `palace/utils/communication.hpp` MPI
collectives file.

See the [L0 overview](./index.md) §Reference-note cohort for the full per-file
descriptions and the cross-links into the convention and overload-set / class-interface
cohorts.
```

### 4. NEW FILE `book/src/L0/overload-sets-and-classes-intro.md` — Overload sets & class interfaces group intro

```create:book/src/L0/overload-sets-and-classes-intro.md
# Overload sets & class interfaces

Multi-overload and multi-subclass Palace surfaces referenced by L1 / L2 / L4 entries.
Where a single L_n operator collapses many C++ overloads (the `Mult` / `MultTranspose`
/ `AddMult` family) or composes a class hierarchy (the `BaseKspSolver`, MFEM-wrapped
`Solver`, eigensolver, and preconditioner families), the L0 anchor is the overload set
or the class interface as a whole — these chapters are those anchors.

Each chapter names the surface (overload family or class hierarchy), enumerates its
concrete members, and ties it to the higher-layer entries it grounds — `apply_linop`'s
overload collapse, the `solve-monad` composition class, the eigensolve / preconditioner
compositions. They are the navigation hubs for the "one L_n verb, many L0 methods"
relationships.

See the [L0 overview](./index.md) §Reference-note cohort for the full per-surface
descriptions.
```

## Supporting evidence

- **L0 cohort split is the index's own structure.** `book/src/L0/index.md`
  §Reference-note cohort (lines 11–41) already groups the 22 chapters under exactly
  three bolded headings: **Conventions** (6 bullets, lines 13–20), **File overviews**
  (11 bullets, lines 22–33), **Overload sets and class interfaces** (5 bullets, lines
  35–41). The SUMMARY nesting mirrors that authoritative grouping 1:1; the group-intro
  bodies are condensed orientations of those three index paragraphs.
- **Chapter counts verified against disk.** `book/src/L0/` holds 23 `.md` files =
  22 cohort chapters + `index.md`. All 22 are present in both the old SUMMARY block and
  the new nested block (no drop). File-overviews = 11 (the 7 `linalg-*`, 2 `fem-*`,
  `fespace-file`, `mpi-globalsum-and-collectives`).
- **Phase-1 corpus = 9 slices** under `book/src/spec/slices/` (arnoldi_step, cg,
  cg_preconditioning_framework, divfree, gmres, orthog, plane_rotation_stream,
  polynomial_recurrence_step, sparse_triangular_solve), all 9 retained, re-sorted
  alphabetically by SUMMARY title.
- **No L0/index.md table.** `book/src/L0/index.md` carries no dep-map / API table
  (it is a prose overview), so no in-index table re-sort is in scope for D5.

## Open questions / caveats

- **L0/index.md bullet-list ordering not touched.** The §Reference-note cohort bullet
  lists in `book/src/L0/index.md` are NOT currently alpha-sorted (Conventions list runs
  output-arg / mfem-vector / par-types / free-functions / tricks / workspace; File
  overviews run vector / operator / ksp / iterative / orthog / solver / rap / bilinearform
  / libceed / fespace / mpi). The directive-3 alpha-within-cohort rule is about the
  list-of-API / dep-map *tables*; these are prose orientation bullets, not a table. I
  left them as-is to keep D5 scoped to the SUMMARY structural reorg. A follow-up could
  alpha-sort the index bullets to match the new SUMMARY order for reader consistency —
  flagging rather than bundling.
- **Group-intro slug convention.** I named the three intros `conventions-intro.md`,
  `file-overviews-intro.md`, `overload-sets-and-classes-intro.md` (the `-intro` suffix
  matches the directive's "intro page per grouping" language). If the meta-phase's
  one-time-reorg pass settles on a different group-intro filename convention across the
  6 parallel dispatches (e.g. `_group.md` or `<kind>/index.md`), these three should be
  renamed to match — purely a naming-convention reconciliation, no content change.
- **Phase-1 `spec/index.md` Index chapter retained as the group's own index.** It is
  not a directive-3 "kind grouping intro" — it is the slice-status table the corpus
  already had. Left in place above the 9 alpha-sorted slice sub-entries; no change.
- Dispatch-phase note: an initial SUMMARY edit was applied directly then reverted to
  restore on-disk state; all changes here are emitted as proposed-changes blocks for
  `integrator-per-report` to apply in Phase 5 (no `book/` mutation left on disk by D5).

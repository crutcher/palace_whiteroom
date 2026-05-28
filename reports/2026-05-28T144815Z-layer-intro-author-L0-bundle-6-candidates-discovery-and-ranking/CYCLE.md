---
agent: layer-intro-author
invoked_at: 2026-05-28T144815Z
scope: L0-bundle-6-candidates-discovery-and-ranking
status: integrated
integrated_at: 2026-05-28T200000Z
integration_commit: a4d7495
integration_notes: "cycle-013 finalize. Discovery→authoring scope stretch SAFETY-GATED + applied: the dispatch authored a full firm L0 chapter linalg-orthog-file (bundle-6 #3; L0 now 18 chapters), verified at integration (codemap MGS range orthog.hpp:41-53 + file-non-existence collision check + SUMMARY palace/ prefix anchor). SUMMARY-registered. #2 linalg-rap-file next-ranked. Plan-kind boundary observation routed to cycle-015 meta-phase. The report OQ's '18 chapters' figure re-derived correct by finalize."
---

# CYCLE: L0 bundle-6 candidates #2 / #3 — discovery + ranking

## Summary

Discovery/ranking dispatch for the cycle-009 open question `l0-bundle-6-candidates`
(bundle-6 #1 `linalg-solver-file` landed cycle-011; #2 and #3 still unscoped). I
surveyed `palace/linalg/*.{hpp,cpp}` via `palace-codemap`, cross-checked each file's
existing L0 coverage against the firm higher-layer entries that cite it, and ranked the
top uncovered-but-cited files by citation pressure.

**Top two ranked candidates:**

1. **`linalg-rap-file`** — `palace/linalg/rap.{hpp,cpp}` (the `ParOperator` /
   `ComplexParOperator` parallel restriction-prolongation wrappers). Highest citation
   pressure of any uncovered `linalg/` file: cited by 5 distinct firm L1/L3 entries plus
   18 line-level citations across the two `*-mutation-rotation` L1>L0 themes, yet has only
   *ad-hoc* coverage (one bullet + 3 evidence lines inside `apply-linop-overload-set.md`).
   Closes the file-overview gap on the operator-hierarchy side the same way
   `linalg-iterative-file` closed it on the solver side.

2. **`linalg-orthog-file`** — `palace/linalg/orthog.hpp` (header-only, 93 lines; the
   `OrthogonalizeColumnMGS` / `OrthogonalizeColumnCGS` Gram-Schmidt family). Cited by the
   firm L1 `orthogonalize` operator (5 citations) plus `concepts/orthogonalization.md` and
   `concepts/gemv_basis.md`, with no dedicated file overview. Small + clearly bounded +
   symbol ranges already verified by the firm L1 entry — **ready now**; I emit a
   proposed-changes block creating it this cycle.

A third candidate (`tests-as-semantic-supplement`, bundle-6 item #2 from the original OQ)
remains gated on the `tests-as-semantic-supplement-l0-vs-concepts-decision` placement
question (L0-convention vs `concepts/`-methodology) — surfaced for cycle-014+ scheduling,
not nominated here because it is blocked on a decision, not on discovery.

## Discovery method + coverage cross-check

`list_files palace/linalg/*.{hpp,cpp}` returned 28 header / 25 source files. Cross-checking
each against the L0 index (`book/src/L0/index.md`) coverage roster:

**Already L0-covered** (file-overview or class-interface chapter exists):
`vector` (`linalg-vector-file`), `operator` (`linalg-operator-file` +
`apply-linop-overload-set`), `ksp` (`ksp-factory-file` + `kspsolver-base-class`),
`iterative` (`linalg-iterative-file`), `solver` (`linalg-solver-file` +
`mfem-wrapper-solver`), `eps`/`arpack`/`slepc`/`nleps` (`eigensolver-wrapper`),
`amg`/`ams`/`jacobi`/`chebyshev`/`distrelaxation`/`gmg`/`blockprecond`
(`preconditioner-classes-overview`).

**Uncovered, ranked by citation pressure from non-L0 entries** (grep over `book/src`
excluding `L0/`, counts = line-level citations):

| File | Cited by (firm entries) | Pressure | Verdict |
|---|---|---|---|
| `rap.{hpp,cpp}` | `L1/apply_linop` (5), `L1/axpy` (2), `L3/apply_linop` (2), `L1-L0/apply-linop-mutation-rotation` (12), `L1-L0/axpby-mutation-rotation` (6) | **HIGH** | **candidate #2** |
| `orthog.hpp` | `L1/orthogonalize` (5), `concepts/orthogonalization` (1), `concepts/gemv_basis` (1) | **MED-HIGH** | **candidate #3 (ready; PC block below)** |
| `divfree.{hpp,cpp}` | `L1/ksp_solve` (1) + `mfem-wrapper-solver`/`mpi-globalsum` (L0) | LOW | defer (thin pressure; see OQ) |
| `mumps`/`strumpack`/`superlu` | `spec/slices/sparse_triangular_solve` only | LOW | defer (only slice-era pressure; direct-solver detail already routed through `mfem-wrapper-solver`) |
| `densematrix`, `hypre`, `errorestimator`, `floquetcorrection`, `hcurl`, `petsc`, `divfree` (rest) | none firm / L0-only mentions | NIL | not scheduled |

`rap.{hpp,cpp}` = 252 + 979 = 1231 lines — the largest uncovered, most-cited file; its
ad-hoc coverage inside `apply-linop-overload-set.md` (one bullet at line 31 + evidence at
lines 79-81) is exactly the file-overview gap a bundle chapter closes. `orthog.hpp` =
93 lines header-only (no `orthog.cpp`), already line-range-mapped by `L1/orthogonalize`.

## Proposed changes

### (A) Candidate #3 — author `book/src/L0/linalg-orthog-file.md` (small + ready)

```edit:book/src/L0/linalg-orthog-file.md
[old]: <new file>
[new]: # File — `palace/linalg/orthog.hpp`

A reference note for the firm L1 [`orthogonalize`](../L1/orthogonalize.md) operator and the
`concepts/` pages [`orthogonalization`](../concepts/orthogonalization.md) /
[`gemv_basis`](../concepts/gemv_basis.md). `palace/linalg/orthog.hpp` is **header-only**
(93 lines; there is no `orthog.cpp`) and houses Palace's entire vector-against-basis
Gram-Schmidt family: the two inline column-orthogonalisation routines `OrthogonalizeColumnMGS`
and `OrthogonalizeColumnCGS` (with a `refine` flag that selects classical-Gram-Schmidt-twice,
"CGS2"), plus the `IdentityInnerProduct` policy struct they default to. Sibling to
[`linalg-iterative-file`](./linalg-iterative-file.md), which holds the runtime dispatch
wrapper (`OrthogonalizeIteration`) that switches the `Orthogonalization` enum
(`MGS | CGS | CGS2`) over these two routines.

## At a glance

The header (`palace/linalg/orthog.hpp:1-93`) declares, inside `namespace palace::linalg`
(opened at line 15):

- **`IdentityInnerProduct`** (line 30) — a small policy struct supplying the default
  inner-product functor; the two orthogonalisation templates are parameterised on an
  inner-product type and default to this when the caller wants the plain Euclidean dot.
- **`OrthogonalizeColumnMGS`** (lines 41-53) — *modified* Gram-Schmidt. Sequentially
  subtracts each basis projection from the candidate before computing the next coefficient
  (`m` sequential dots, each followed by an `AXPY`-style update). The numerically-stabler,
  more-communication-bound variant.
- **`OrthogonalizeColumnCGS`** (lines 57-89) — *classical* Gram-Schmidt. Computes all `m`
  projection coefficients against the *original* candidate in one batch (one fused
  multi-dot), then applies the combined update. The `refine` parameter re-runs the whole
  pass once more (`CGS2`), trading a second communication round for restored orthogonality.

Both routines take `(MPI_Comm comm, const std::vector<VecType> &V, VecType &w, ...)`:
read-only stored basis `V[0..m-1]`, in-place candidate `w` (overwritten with its
orthogonal residual), and an output coefficient array (the leading Hessenberg/Arnoldi
column). The `MPI_Comm` parameter is the collective handle for the inner-product reductions;
per the single-rank reading rule ([`par-types-single-rank-reading`](./par-types-single-rank-reading.md))
the `comm`-scoped `GlobalSum` collapses to a local reduction at L1.

## The two variants and what each buys

The MGS / CGS split is **load-bearing numerical structure**, not a transparent trick
(per [`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md)):
the two routines compute the same mathematical projection but with different rounding-error
accumulation and different communication patterns:

- **MGS** — `m` sequential reductions; each projection is taken against the *partially
  orthogonalised* candidate. Better orthogonality in finite precision; `m` separate
  `GlobalSum` round-trips (latency-bound at scale).
- **CGS** — one batched reduction of all `m` coefficients against the *original* candidate;
  a single `GlobalSum` of an `m`-vector (bandwidth-bound, one round-trip). Cheaper
  communication, worse orthogonality.
- **CGS2** (`OrthogonalizeColumnCGS(..., refine=true)`) — CGS applied twice. "Twice is
  enough" (Giraud et al.): two CGS passes recover MGS-level orthogonality at two
  round-trips instead of `m`. This is the variant Palace's GMRES default uses.

The runtime selection over these three lives one file away in `iterative.cpp` (the
`OrthogonalizeIteration` wrapper, `palace/linalg/iterative.cpp:308-325`), not here; this
header is purely the per-variant algebra.

## Notes for higher layers

- **The three variants become L1's single runtime variant axis.** The firm L1
  [`orthogonalize`](../L1/orthogonalize.md) operator carries one variant axis
  (`MGS | CGS | CGS2`) that maps exactly onto these two routines plus the `refine` flag.
  The `IdentityInnerProduct` default is absorbed (L1 takes the inner product as the plain
  field dot unless a weighted form is requested).
- **The in-place `w` overwrite is L0-internal** ([`output-arg-vs-receiver`](./output-arg-vs-receiver.md)):
  the L1 form returns a fresh orthogonal residual `w'` plus the coefficient column `H`
  rather than mutating `w`.
- **The `comm` argument is the only `Par`-adjacent surface** and collapses under
  single-rank reading; the routines themselves are otherwise rank-agnostic
  (`std::vector<VecType>` of local vectors).

## Referenced from

- [`L1/orthogonalize`](../L1/orthogonalize.md) — the firm operator that lifts this family.
- [`L0/linalg-iterative-file`](./linalg-iterative-file.md) — sibling file holding the
  `OrthogonalizeIteration` runtime dispatch wrapper over these two routines.
- [`concepts/orthogonalization`](../concepts/orthogonalization.md) — the cross-cutting
  narrative.
- [`concepts/gemv_basis`](../concepts/gemv_basis.md) — the batched-projection (CGS) form
  as a GEMV-against-the-basis.

## Evidence (representative)

- `palace/linalg/orthog.hpp:1-93` — the header file (header-only; no `orthog.cpp`).
- `palace/linalg/orthog.hpp:15` — `namespace palace::linalg` open.
- `palace/linalg/orthog.hpp:30` — `struct IdentityInnerProduct` (default inner-product policy).
- `palace/linalg/orthog.hpp:41-53` — `OrthogonalizeColumnMGS` template (modified Gram-Schmidt; `m` sequential dots).
- `palace/linalg/orthog.hpp:57-89` — `OrthogonalizeColumnCGS` template (classical Gram-Schmidt; batched multi-dot; `refine` flag → CGS2).
- `palace/linalg/iterative.cpp:308-325` — `OrthogonalizeIteration` runtime dispatch (`switch` over `MGS | CGS | CGS2`; CGS2 = `OrthogonalizeColumnCGS(..., refine=true)`); the construction side, in the sibling file.
```

### (B) Candidate #3 — register the new chapter in `book/src/L0/index.md`

```edit:book/src/L0/index.md
[old]: - [`linalg-iterative-file`](./linalg-iterative-file.md) — `palace/linalg/iterative.{hpp,cpp}` at a glance. The home of `IterativeSolver<OperType>` base class plus the three concrete subclasses `CgSolver`, `GmresSolver`, `FgmresSolver`. The L0 anchor for the cycle-007+ `L1/ksp_solve` operator and for the per-step body that the L2 `krylov-step` entry instantiates.
[new]: - [`linalg-iterative-file`](./linalg-iterative-file.md) — `palace/linalg/iterative.{hpp,cpp}` at a glance. The home of `IterativeSolver<OperType>` base class plus the three concrete subclasses `CgSolver`, `GmresSolver`, `FgmresSolver`. The L0 anchor for the cycle-007+ `L1/ksp_solve` operator and for the per-step body that the L2 `krylov-step` entry instantiates.
- [`linalg-orthog-file`](./linalg-orthog-file.md) — `palace/linalg/orthog.hpp` (header-only, 93 lines) at a glance. The home of the vector-against-basis Gram-Schmidt family: `OrthogonalizeColumnMGS` (modified) and `OrthogonalizeColumnCGS` (classical, with `refine` → CGS2), plus the `IdentityInnerProduct` default inner-product policy. The L0 anchor for the firm `L1/orthogonalize` operator's `MGS | CGS | CGS2` variant axis; sibling to [`linalg-iterative-file`](./linalg-iterative-file.md) (which holds the `OrthogonalizeIteration` runtime dispatch).
```

### (C) Candidate #3 — add to `book/src/SUMMARY.md` under the L0 Part

```edit:book/src/SUMMARY.md
[old]: - [File — palace/linalg/iterative.{hpp,cpp}](./L0/linalg-iterative-file.md)
[new]: - [File — palace/linalg/iterative.{hpp,cpp}](./L0/linalg-iterative-file.md)
- [File — palace/linalg/orthog.hpp](./L0/linalg-orthog-file.md)
```

> **Integrator note**: the SUMMARY.md anchor-text above is a *best-effort* line match — if
> the exact `linalg-iterative-file` SUMMARY entry text differs, place the new
> `linalg-orthog-file` entry adjacent to the other `File —` L0 entries using the
> `summary-md-surgical-insert` skill. The proposed-changes block (A) is the load-bearing
> artifact; (B) and (C) are registration.

## Supporting evidence

- L0 file inventory (codemap `list_files palace/linalg/*.{hpp,cpp}`): 28 headers / 25 sources.
- Coverage cross-check vs `book/src/L0/index.md` roster: see Discovery table above.
- `rap.hpp` symbols: `ParOperator` (`palace/linalg/rap.hpp:24-121`), `ComplexParOperator`
  (`palace/linalg/rap.hpp:124-222`); full `Mult`/`AddMult`/`MultTranspose`/`MultHermitianTranspose`
  + `RestrictionMatrixMult` overload set verified at `rap.hpp:46-47, 112-120, 145-146, 206-220`.
- `orthog.hpp` symbols: `IdentityInnerProduct` (line 30), `OrthogonalizeColumnMGS`
  (lines 41-53), `OrthogonalizeColumnCGS` (lines 57-89); ranges corroborated by the firm
  `L1/orthogonalize` Evidence section (`orthog.hpp:57-89` cited at `L1/orthogonalize.md:260`).
- Firm-entry citation counts (grep over `book/src`, excluding `L0/`): see Discovery table.

## Open questions / caveats

### Promote OQ `l0-bundle-6-candidates` with the candidate #2 / #3 ranking

The cycle-009 OQ `l0-bundle-6-candidates` (status `partially-answered` since cycle-011) should
be updated with this discovery. Proposed append to the OQ entry:

> **Discovery update cycle-013 (layer-intro-author)**: bundle-6 candidates #2 and #3
> nominated concretely after a citation-pressure survey of all 28 uncovered-vs-covered
> `palace/linalg/` files (`reports/2026-05-28T144815Z-layer-intro-author-L0-bundle-6-candidates-discovery-and-ranking/`):
>
> - **#2 `linalg-rap-file`** (`palace/linalg/rap.{hpp,cpp}`, 1231 lines) — HIGHEST
>   citation pressure of any uncovered `linalg/` file (5 firm L1/L3 entries + 18 line-level
>   citations across the two `*-mutation-rotation` L1>L0 themes); currently only ad-hoc
>   coverage inside `apply-linop-overload-set.md` (one bullet + 3 evidence lines). A
>   dedicated file overview closes the operator-hierarchy file-gap the way
>   `linalg-iterative-file` closed the solver-hierarchy gap. **NOT authored this cycle**
>   (file is large + carries the single-rank-reading subtlety on prolongation/restriction
>   collapse — warrants its own full harvest-style read). Routes to cycle-014+ as a full
>   bundle-author dispatch. Suggested chapter outline (anchor ranges to chunk):
>   `ParOperator` class (`rap.hpp:24-121`) + its `Mult`/`MultTranspose`/`AddMult` bodies
>   (`rap.cpp:195-234`, `236-275`); `ComplexParOperator` class (`rap.hpp:124-222`) + its
>   `Mult`/`MultHermitianTranspose` bodies (`rap.cpp:481-517` ff.); the
>   `RestrictionMatrixMult`/`RestrictionMatrixMultTranspose` prolongation-restriction
>   pair (`rap.hpp:46-47, 145-146`); the single-rank-reading collapse note
>   (prolongation/restriction → identity, BC-tdof masking the only L1 residue) per
>   `apply-linop-overload-set.md:31`.
> - **#3 `linalg-orthog-file`** (`palace/linalg/orthog.hpp`, 93 lines, header-only) —
>   MED-HIGH pressure (firm `L1/orthogonalize` + 2 concept pages); small + bounded +
>   already line-range-mapped by the firm L1 entry. **Authored this cycle** via the
>   proposed-changes block in the source report (creates `book/src/L0/linalg-orthog-file.md`,
>   registers it in `L0/index.md` + `SUMMARY.md`).
>
> Lower-pressure deferrals surfaced for future scheduling: `divfree.{hpp,cpp}` (thin firm
> pressure — 1 citation from `L1/ksp_solve`); the direct-solver trio
> `mumps`/`strumpack`/`superlu` (only `spec/slices/` slice-era pressure; the direct-solver
> detail is already routed through `mfem-wrapper-solver`). `densematrix`, `hypre`,
> `errorestimator`, `floquetcorrection`, `hcurl`, `petsc` have NIL firm citation pressure
> and are not scheduled. Bundle-6 item #2 from the *original* OQ
> (`tests-as-semantic-supplement`) remains gated on
> `tests-as-semantic-supplement-l0-vs-concepts-decision` (placement: L0-convention vs
> `concepts/`-methodology) — that is a *decision* block, not a discovery gap, so it is not
> re-nominated here. After #3 lands the L0 chapter count is **18**.

### Caveat — `linalg-rap-file` single-rank-reading subtlety

`rap.{hpp,cpp}`'s entire reason for existence is the parallel prolongation/restriction
(`P^T A P`) wrapping. Under the CLAUDE.md §Scope single-rank reading, prolongation and
restriction collapse to identity and only the Dirichlet-BC tdof masking survives at L1
(`apply-linop-overload-set.md:31` already states this). A future `linalg-rap-file` author
must keep the L0 chapter faithful to the *parallel* source (the chapter documents what
Palace's code does) while cross-linking to `par-types-single-rank-reading` for the L1
collapse — i.e. do NOT pre-collapse the prolongation/restriction in the L0 reference note;
that collapse is an L1>L0 lowering concern, not an L0 source-faithfulness concern. This is
the same discipline boundary the `apply-linop-overload-set` chapter already observes.

### Caveat — `orthog.hpp` chapter overlaps `linalg-iterative-file`

The new `linalg-orthog-file` and the existing `linalg-iterative-file` both touch the
orthogonalisation surface: the algebra lives in `orthog.hpp` (new chapter) but the runtime
dispatch (`OrthogonalizeIteration`) lives in `iterative.cpp` (existing chapter). The split
is clean (per-variant algebra vs runtime selection) and both chapters cross-link, mirroring
the `linalg-solver-file` / `mfem-wrapper-solver` and `linalg-operator-file` /
`apply-linop-overload-set` companion-chapter precedents. No content duplication: the new
chapter does not restate the dispatch, the existing chapter does not restate the per-variant
algebra. If a future cross-cutter judges the `OrthogonalizeIteration` evidence line
(currently in `linalg-iterative-file`) should move to the new chapter, that is a clean
one-line migration.

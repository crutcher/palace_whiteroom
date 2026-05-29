---
agent: layer-intro-author
invoked_at: 2026-05-29T16:37:46Z
scope: rough-in naming-residue L0 hygiene sweep (dep-map + Part-overview repoints)
status: pending
integrated_at: 2026-05-29T203000Z
integration_commit: 1de17ed
integration_notes: "Applied clean (cycle-026 dispatch-5). 5 navigational repoints: 2 L0 overviews (linalg-operator-file.md §Notes/§Referenced-from + mpi-globalsum §Referenced-from — nrm2_weighted/dot_bilinear candidate-slugs → live matrix-weighted-norm/bilinear-form links), concepts/dependency-map.md (pruned stale orthog→plane-rotation-stream L1-tier edge), concepts/negative-result-slice.md (added sparse_triangular_solve reciprocal-membership row). 3 OQs RESOLVED + 1 ADDRESSED-AT-L0 (residual bilinear-form.md:416 dot_bilinear provenance note routed to follow-up). Pure hygiene, zero content authoring, zero gate hits."

# CYCLE: rough-in naming-residue L0 hygiene sweep

## Summary

A coordinated navigational/bookkeeping sweep landing four stale-reference
repoints within layer-shell authority (L0 file-overview prose, the concept
dependency-map, the `negative-result-slice` concept page). No content
authoring — every change is a slug repoint, a stale-edge prune, or a
reciprocal-membership row. The four OQs in scope are addressed:

1. **`matrix-weighted-norm-naming-sweep`** + **`bilinear-form-slug-name-coordination`**
   — three L0 file-overview lines (`linalg-operator-file.md` ×2,
   `mpi-globalsum-and-collectives.md` ×1) referenced the *candidate* slugs
   `nrm2_weighted` / `dot_bilinear`. Both operators were harvested at L1
   (cycle-008/cycle-010) under the canonical slugs `matrix-weighted-norm`
   and `bilinear-form` — both files exist on-disk, so the repoints use live
   links per the plain-text→live-link convention. The "have not yet been
   harvested … obstructions" prose is also corrected (they are now harvested
   `rough-in` entries, not obstructions).
2. **`dependency-map-orthog-plane-rotation-stale-edge-prune`** — the L1-tier
   mermaid block in `concepts/dependency-map.md:188` carried an
   `orthog --> plane-rotation-stream` edge. Per the cycle-012
   phase-1-corpus-reduction (the plane-rotation sub-slice was split out of
   `orthog.md` into `plane_rotation_stream.md`; `orthog.md` now scopes ONLY
   block Gram-Schmidt), `orthog` no longer depends on the plane-rotation
   stream. The edge is stale and is pruned.
3. **`negative-result-slice-examples-reciprocal-membership`** — the
   `sparse_triangular_solve` slice's own reduction banner states the
   `negative-result-slice` concept page "does not yet list this slice in its
   §'Examples in this spec'." The reciprocal-membership row is added.

**Skills applied**: three of the five edits (Repoints 1-3) follow
`upgrade-plain-text-ref-to-live-link-when-target-on-disk` (cycle-024) — the
candidate-slug references are upgraded to live links because both target
files exist on-disk. The Repoint-1 / supporting-evidence L0 citation
re-verification uses `verify-citation-range` via its mechanical
`--anchor`/`--scan` realization (`tools/citecheck/`).

## Proposed changes

### Repoint 1 — `linalg-operator-file.md:73` (Notes for higher layers)

Repoint candidate slugs to canonical L1 slugs; correct the stale
"have not yet been harvested … obstructions" claim (both are now harvested
`rough-in` L1 entries). L0 source characterization (`Norml2(comm, x, B, Bx)`
@ `palace/linalg/operator.hpp:374`; `Dot(comm, x, A, y)` @
`palace/linalg/operator.hpp:388-389`) is preserved verbatim — citecheck-clean
(verified `--anchor Norml2` / `--anchor Dot`).

```edit:book/src/L0/linalg-operator-file.md
[old]: - **The `linalg::` free functions are the natural L0 anchor for L1's matrix-weighted norm and bilinear-form operators.** `Norml2(comm, x, B, Bx)` lifts to L1's `nrm2_weighted`; `Dot(comm, x, A, y)` lifts to L1's `dot_bilinear`. These have not yet been harvested at L1 (they are obstructions for the cycle-008 retroactive sweep — the current L1 `dot` and `nrm2` operators cover only the unweighted forms). The workspace-internal-allocation pattern (`Dot`'s synthetic workspace) is Category 4 of [`mutable-workspace-pattern`](./mutable-workspace-pattern.md).
[new]: - **The `linalg::` free functions are the natural L0 anchor for L1's matrix-weighted norm and bilinear-form operators.** `Norml2(comm, x, B, Bx)` lifts to L1's [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md); `Dot(comm, x, A, y)` lifts to L1's [`bilinear-form`](../L1/bilinear-form.md). Both are now harvested at L1 (cycle-008 / cycle-010, `rough-in`); the unweighted forms remain the separate [`nrm2`](../L1/nrm2.md) / [`dot`](../L1/dot.md) operators. The workspace-internal-allocation pattern (`Dot`'s synthetic workspace) is Category 4 of [`mutable-workspace-pattern`](./mutable-workspace-pattern.md).
```

### Repoint 2 — `linalg-operator-file.md:88` (Referenced from)

Repoint the forward-target slug list. Both targets on-disk → live links.

```edit:book/src/L0/linalg-operator-file.md
[old]: - Higher-layer L1 / L2 / L4 entries (forward-target): the `L1/apply_linop` operator anchors here; future `L1/dot_bilinear`, `L1/nrm2_weighted`, `L1/power_iterate` will anchor the matrix-weighted free functions; the L2 product-and-sum combinators (rough-in: `L2/product-of-operators`, `L2/sum-of-operators`) lift the templated combinator structure.
[new]: - Higher-layer L1 / L2 / L4 entries (forward-target): the [`L1/apply_linop`](../L1/apply_linop.md) operator anchors here; the matrix-weighted free functions are anchored by [`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md) and [`L1/bilinear-form`](../L1/bilinear-form.md) (future `L1/power_iterate` will anchor `SpectralNorm`); the L2 product-and-sum combinators (rough-in: `L2/product-of-operators`, `L2/sum-of-operators`) lift the templated combinator structure.
```

### Repoint 3 — `mpi-globalsum-and-collectives.md:119` (Referenced from)

Repoint the candidate slugs in the global-reduction forward-target list.

```edit:book/src/L0/mpi-globalsum-and-collectives.md
[old]: - Higher-layer L1 / L2 / L4 entries (forward-target): every L1 operator that performs a global reduction (`dot`, `nrm2`, `axpy`-chained reductions, future `dot_bilinear` / `nrm2_weighted`) anchors here for the L0 implementation primitive. The cycle-005+ retroactive-thinning sweep (priority #11) will rewrite inline `Mpi::GlobalSum` mentions in L1 entries to reference this chapter.
[new]: - Higher-layer L1 / L2 / L4 entries (forward-target): every L1 operator that performs a global reduction ([`dot`](../L1/dot.md), [`nrm2`](../L1/nrm2.md), `axpy`-chained reductions, and the matrix-weighted [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) / [`bilinear-form`](../L1/bilinear-form.md)) anchors here for the L0 implementation primitive. The cycle-005+ retroactive-thinning sweep (priority #11) will rewrite inline `Mpi::GlobalSum` mentions in L1 entries to reference this chapter.
```

### Repoint 4 — `concepts/dependency-map.md:188` (L1 — mutation-lifted primitives block)

Prune the stale `orthog --> plane-rotation-stream` edge. The surrounding
edges (`plane-rotation-stream --> givens_generate/givens_apply/trsv` at 186,
187, 194; `plane_rotation_stream --> givens` at 165) are correct and are NOT
touched — only the false `orthog`-dependency line is removed.

```edit:book/src/concepts/dependency-map.md
[old]:   plane-rotation-stream --> givens_generate
  plane-rotation-stream --> givens_apply
  orthog --> plane-rotation-stream
  cg --> nrm2
[new]:   plane-rotation-stream --> givens_generate
  plane-rotation-stream --> givens_apply
  cg --> nrm2
```

### Repoint 5 — `concepts/negative-result-slice.md:44-46` (Examples in this spec)

Add the `sparse_triangular_solve` reciprocal-membership row. Mirrors the
existing `polynomial_recurrence_step` row format (points at the slice file
with a one-line characterization; the slice carries the L0 `file:line`
citations, so no raw source-range is re-stated here — citecheck-clean by
construction). The `sparse_triangular_solve` slice IS the canonical
negative-result instance for the L0→L1 scope-out obstruction (its banner
@ `sparse_triangular_solve.md:3-7` requests exactly this reciprocal).

```edit:book/src/concepts/negative-result-slice.md
[old]: - [`polynomial_recurrence_step`](../spec/slices/polynomial_recurrence_step.md) — three independent scalar-update sequences (Chebyshev-4th-kind, Chebyshev-1st-kind, GMRES Givens stream) plus one out-of-scope branch (eigenvalue tracking via SLEPc/ARPACK). No Palace-level unification.
[new]: - [`polynomial_recurrence_step`](../spec/slices/polynomial_recurrence_step.md) — three independent scalar-update sequences (Chebyshev-4th-kind, Chebyshev-1st-kind, GMRES Givens stream) plus one out-of-scope branch (eigenvalue tracking via SLEPc/ARPACK). No Palace-level unification.
- [`sparse_triangular_solve`](../spec/slices/sparse_triangular_solve.md) — the scope question (sparse `Ly=b`/`Uy=b`, factor Allgatherv, residual check) returns a negative result: Palace carries no Palace-level triangular-solve form. SuperLU/STRUMPACK/MUMPS are thin opaque `mfem::Solver` forwarders (the factor interior lives below the project boundary). This is the canonical L0→L1 **scope-out obstruction** (`trsv` obstruction-shadow) — the L0→L1 analogue of [`sequential-obstruction`](./sequential-obstruction.md)'s L2→L3 negative result.
```

## Supporting evidence

- **Canonical L1 slugs exist on-disk** (live-link eligibility):
  `book/src/L1/matrix-weighted-norm.md` (`# matrix-weighted-norm`, Status
  `rough-in (test-coverage-bounded)` @ `:110`),
  `book/src/L1/bilinear-form.md` (`# bilinear-form`, Status `rough-in
  (lower-layer-shared-vocabulary, cycle-010-wave-1)` @ `:321`). Both are
  harvested entries — the "have not yet been harvested … obstructions" L0
  prose was stale.
- **L0 source claims re-stated in repoint 1 are citecheck-clean**
  (verified against `reference/palace/`):
  - `palace/linalg/operator.hpp:374` `--anchor Norml2` → ok
    (`double Norml2(MPI_Comm comm, const VecType &x, const Operator &B, VecType &Bx);`).
  - `palace/linalg/operator.hpp:388-389` `--anchor Dot` → ok
    (`std::complex<double> Dot(MPI_Comm comm, const ComplexVector &x, const Operator &A, const ComplexVector &y);`).
  - (The repoint 5 row's negative-result claim cross-checked via
    `palace/linalg/superlu.hpp:22-60` `--anchor SuperLUSolver` → ok:
    `class SuperLUSolver : public mfem::Solver` with `Mult` forwarding
    `solver.Mult(x, y)`; confirms the opaque-forwarding negative result the
    row paraphrases. No raw range is embedded in the row itself.)
- **Stale dep-map edge provenance**: `book/src/spec/slices/orthog.md:9` +
  `:227` document the cycle-012 split — the plane-rotation-stream sub-slice
  was reduced out of `orthog.md` (now scopes ONLY block Gram-Schmidt) into
  `book/src/spec/slices/plane_rotation_stream.md`. The L1-tier
  `orthog --> plane-rotation-stream` edge no longer reflects firm structure.
  The other plane-rotation edges in the same block (186/187/194 →
  givens_generate/givens_apply/trsv; 165 plane_rotation_stream → givens) are
  the stream's own internal primitives and are correct (untouched).
- **Reciprocal-membership gap**: `book/src/spec/slices/sparse_triangular_solve.md:3`
  — "(that concept page does not yet list this slice in its §'Examples in this
  spec')". The slice is the declared canonical instance of
  `concepts/scope-out-obstruction.md` §"Canonical instance" (`:68`) and
  `concepts/sequential-obstruction.md` §"Sub-kind: out-of-scope-obstruction"
  (`:53`). Repoint 5 closes the reciprocal.

### citecheck --scan of this CYCLE.md

```
$ python3 tools/citecheck/citecheck.py --scan <this CYCLE.md> --quiet
12 ok, 0 failing (12 citations checked).
```
(Clean after one `AMBIG` fix: the two bare `operator.hpp:NNN` shorthand
mentions in the evidence prose were qualified to `palace/linalg/operator.hpp`
— `operator.hpp` basename collides with `fem/libceed/operator.hpp`.)

## Open questions / caveats

- **`matrix-weighted-norm-naming-sweep`** — ADDRESSED (closeable). All
  on-disk `nrm2_weighted` references in `book/src/` are repointed (the only
  hits were the three L0 file-overview lines, all in this sweep). The single
  remaining `nrm2_weighted` mention after these edits is the provenance note
  *inside* `book/src/L1/matrix-weighted-norm.md` if any — none found in the
  initial grep (the L1 entry's own Evidence cites the canonical slug). Route
  to closed.
- **`bilinear-form-slug-name-coordination`** — ADDRESSED with one residual
  pointer. The L0 lines are repointed. There remains ONE `dot_bilinear`
  mention at `book/src/L1/bilinear-form.md:416` — but that line lives in the
  harvester-owned `bilinear-form` entry's Evidence section and is a
  *deliberate provenance note* recording the historical slug discrepancy
  ("The L0 chapter uses the candidate slug `dot_bilinear`; this entry uses …
  `bilinear-form`. The slug discrepancy is noted in *Open questions* below").
  Once these L0 repoints land, that note's premise (the L0 chapter using
  `dot_bilinear`) is **no longer true**, so the note is itself now stale.
  It is **outside layer-shell authority** (it is operator-entry content owned
  by the harvester). ROUTE: a follow-up harvester/lifter dispatch on
  `bilinear-form` should update its Evidence §:412-418 + the corresponding
  Open-questions note to record the discrepancy as *resolved by the
  cycle-026 naming-residue sweep* (the L0 chapter now uses the canonical
  slug). I did not edit it (cross-role).
- **`dependency-map-orthog-plane-rotation-stale-edge-prune`** — ADDRESSED.
  Pruned at `concepts/dependency-map.md:188`. Caveat for the integrator:
  confirm no downstream prose in `dependency-map.md` §"Maintenance protocol"
  (`:397`) hard-references the pruned edge count; the prune is a single-line
  removal and the mermaid block remains well-formed.
- **`negative-result-slice-examples-reciprocal-membership`** — ADDRESSED.
  Reciprocal row added at `negative-result-slice.md` §Examples. Follow-up
  (out of scope, route to a same-layer-cross-cutter or the next harvester on
  `sparse_triangular_solve`): the slice's reduction banner (`:3`) can drop
  the "(that concept page does not yet list this slice …)" parenthetical once
  this row lands — but that edit is to the slice (Phase-1 corpus), not the
  concept page, so it is a separate dispatch.
- **General caveat**: all five edits are surgical single-block repoints with
  exact on-disk `[old]` strings; none alters layer semantics or the
  high→low document structure. ALL other tier blocks in `dependency-map.md`
  (the higher planned/roadmap mermaid tiers at lines 74-95 — which DO carry
  other `plane-rotation-stream` edges: `minres:::planned --> plane-rotation-stream`,
  `eigenmode:::planned --> plane-rotation-stream`, `plane-rotation-stream:::planned
  --> givens / incremental-least-squares` — as well as the L2/L3/L4 tier blocks)
  were inspected and carry NO `orthog --> plane-rotation-stream` edge (the
  L3 block's orthog edges go to sequential-obstruction/tensor-field-lift/
  gemv_basis/apply_linop) — so the prune is correctly scoped to the single
  L1-tier occurrence (grep confirms `orthog --> plane-rotation-stream` occurs
  exactly once, at line 188).

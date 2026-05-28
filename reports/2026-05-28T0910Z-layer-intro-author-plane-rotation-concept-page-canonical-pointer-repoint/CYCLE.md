---
agent: layer-intro-author
invoked_at: 2026-05-28T14:39:42Z
scope: plane-rotation-concept-page-canonical-pointer-repoint
status: integrated
integrated_at: 2026-05-28T200000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-013 finalize. 3 surgical concept-page canonical-pointer repoints applied (plane-rotation-stream / givens_generate / givens_apply → plane_rotation_stream). 4th candidate (dependency-map.md:188 mermaid arrow) NOT repointed — routed to OQ dependency-map-orthog-plane-rotation-stale-edge-prune. Clean run."
---

# CYCLE: plane-rotation concept-page canonical-pointer repoint

## Summary

Cycle-012's phase-1 corpus-reduction batch-3 reduced the **plane-rotation-stream sub-slice** that
formerly lived inside `book/src/spec/slices/orthog.md` (its `## Context` / `# Orthogonalization
(plane-rotation stream)` block) and merged its unique material into the canonical
`book/src/spec/slices/plane_rotation_stream.md`. After the reduction, `orthog.md` scopes **only**
the block Gram-Schmidt orthogonalization (L0→L4 Gram-Schmidt sections); the plane-rotation stream
lives entirely in `plane_rotation_stream.md` (which declares itself canonical at its line 5 and
explicitly names this OQ: *"the firm Givens concept pages' 'Used in' / 'primary dissection'
cross-references should be repointed from the `orthog` slice to this slice"*).

**Exactly 3 stale references** survive — one per page — in firm plane-rotation/Givens concept pages
that still cite the (now-reduced) plane-rotation material in `orthog.md` as their canonical anchor.
This report proposes a surgical pointer swap for each (no surrounding-prose rewrite). The fourth
plane-rotation concept page, `concepts/givens.md`, was **already** repointed in cycle-012 (its L2
usage-shape pointer at line 40 already targets `plane_rotation_stream.md`) — no edit needed.

The planner estimated ~3 pages; verified count is **3 stale references across 3 pages**.

## Stale reference list (exact page + line)

| # | Page | Line | Current target | Context | Verdict |
|---|------|------|----------------|---------|---------|
| 1 | `book/src/concepts/plane-rotation-stream.md` | 37 | `../spec/slices/orthog.md` ("primary dissection of the stream") | The stream's own "Used in" claims `orthog` is the *primary dissection* — directly contradicted by `plane_rotation_stream.md:5` (now canonical). | STALE — repoint |
| 2 | `book/src/concepts/givens_generate.md` | 27 | `../spec/slices/orthog.md` ("Used in") | Describes the plane-rotation-stream activity (generate the rotation that zeros the sub-diagonal of the new Hessenberg column) — reduced out of `orthog.md`. | STALE — repoint |
| 3 | `book/src/concepts/givens_apply.md` | 27 | `../spec/slices/orthog.md` ("Used in") | Describes the plane-rotation-stream activity (replay stored rotations on the new column, apply new rotation, propagate to RHS pair) — reduced out of `orthog.md`. | STALE — repoint |

**NOT stale (deliberately left alone):**

- `book/src/concepts/givens.md:40` — already points at `plane_rotation_stream.md` (repointed cycle-012). No edit.
- `book/src/concepts/sequential-obstruction.md:48` — points at the `orthog` slice's **L3 section** for the
  **MGS/Gram-Schmidt** treatment ("the detailed treatment in the GMRES-orthogonalization context"). The
  Gram-Schmidt L3 sections genuinely remain in `orthog.md`; this is a correct pointer, not a plane-rotation
  reference. No edit.
- `book/src/concepts/gemv_basis.md:21,31`, `orthogonalization.md:23`, `state-stratification.md`, `dot.md`,
  `ksp_solve.md`, `gmres.md:23`, etc. — all reference `orthog.md` (or `slices/orthog.hpp`) for the
  **Gram-Schmidt orthogonalization** content that legitimately remains in `orthog.md`. No edit.
- `book/src/concepts/dependency-map.md:188` (`orthog --> plane-rotation-stream`) — a **mermaid
  concept-node dependency edge** (bare node identifiers in a `graph BT` block), NOT a `../spec/slices/*.md`
  file pointer of the "Used in"/"primary dissection" canonical-anchor shape this OQ scopes. After the
  cycle-012 reduction the edge is **stale-in-spirit** (orthog no longer contains the plane-rotation
  stream), but resolving it is a concept-graph-DAG modeling decision (delete the edge vs. re-source it,
  e.g. `gmres --> plane-rotation-stream`), not a surgical pointer swap — and the canonical node's own
  out-edges (`:165/:186/:187/:194/:248` `plane_rotation_stream/plane-rotation-stream --> givens /
  givens_generate / givens_apply / trsv / givens`) are already correct. **Out of scope for this clean
  pointer swap; deferred to a follow-up dependency-map-maintenance pass** (see Open questions below).

## Proposed changes

### 1. `book/src/concepts/plane-rotation-stream.md` — repoint "primary dissection" to the canonical slice

The "primary dissection" claim must move from the reduced `orthog` sub-slice to the canonical
`plane_rotation_stream.md`. The `gmres` consumer pointer (line 38) is unaffected and stays.

```edit:book/src/concepts/plane-rotation-stream.md
[old]: - [`orthog` slice](../spec/slices/orthog.md) — primary dissection of the stream as it appears in GMRES/FGMRES.
- [`gmres` slice](../spec/slices/gmres.md) — consumer (per-step driver and back-solve).
[new]: - [`plane_rotation_stream` slice](../spec/slices/plane_rotation_stream.md) — primary (canonical) dissection of the stream as it appears in GMRES/FGMRES.
- [`gmres` slice](../spec/slices/gmres.md) — consumer (per-step driver and back-solve).
```

### 2. `book/src/concepts/givens_generate.md` — repoint "Used in" to the canonical slice

```edit:book/src/concepts/givens_generate.md
[old]: - [`orthog` slice](../spec/slices/orthog.md) — once per Arnoldi step, to generate the rotation that zeros the sub-diagonal of the new Hessenberg column.
[new]: - [`plane_rotation_stream` slice](../spec/slices/plane_rotation_stream.md) — once per Arnoldi step, to generate the rotation that zeros the sub-diagonal of the new Hessenberg column.
```

### 3. `book/src/concepts/givens_apply.md` — repoint "Used in" to the canonical slice

```edit:book/src/concepts/givens_apply.md
[old]: - [`orthog` slice](../spec/slices/orthog.md) — applied repeatedly per Arnoldi step: $k$ times to the new Hessenberg column (replay of stored rotations), once to the same column (new rotation), once to the $\bar{g}$ vector pair.
[new]: - [`plane_rotation_stream` slice](../spec/slices/plane_rotation_stream.md) — applied repeatedly per Arnoldi step: $k$ times to the new Hessenberg column (replay of stored rotations), once to the same column (new rotation), once to the $\bar{g}$ vector pair.
```

## Supporting evidence

- **Source of the OQ**: `book/src/spec/slices/plane_rotation_stream.md:5` — "**This slice is now the
  canonical plane-rotation-stream dissection** (the `orthog.md` plane-rotation sub-slice was reduced
  to a stub pointing here, cycle-012 [...]). The firm Givens concept pages' 'Used in' / 'primary
  dissection' cross-references should be repointed from the `orthog` slice to this slice (pending
  `layer-intro-author` dispatch; OQ `plane-rotation-concept-page-canonical-pointer-repoint`)."
- **Reduction confirmation**: `book/src/spec/slices/orthog.md:225-235` (§"Plane-rotation stream
  (reduced — see `plane_rotation_stream.md`)") — the stub-pointer block confirming the plane-rotation
  sub-slice was removed from `orthog.md` and now scopes ONLY block Gram-Schmidt. Its "Canonical
  plane-rotation entries" list (lines 229-234) names `plane_rotation_stream.md` as the full
  L0/L1/L2/L3 dissection.
- **Already-repointed precedent**: `book/src/concepts/givens.md:36-58` (§"L2 usage shape") points at
  `plane_rotation_stream.md` — this is the form the three stale pages should match.
- **Negative-evidence pages** (verified NOT stale, left untouched): `sequential-obstruction.md:48`
  (Gram-Schmidt L3 context), `gemv_basis.md:21,31`, `orthogonalization.md:23`, `gmres.md:23`,
  `dot.md`, `ksp_solve.md`, `state-stratification.md` — all reference the Gram-Schmidt content that
  legitimately remains in `orthog.md`.

## Open questions / caveats

- **Adjacent stale citation, OUT OF SCOPE (do not bundle):** `givens_generate.md:23` and
  `givens_apply.md:23` both cite `palace/linalg/gmres.cpp:GeneratePlaneRotation` /
  `:ApplyPlaneRotation`. The firm `givens.md:33-34` cites these at `palace/linalg/iterative.cpp:73-108`
  / `:227-241`, and `plane_rotation_stream.md` cites `iterative.cpp:72-108` / `:226-242`. The `gmres.cpp`
  path on the two `givens_*` pages is **likely stale** (Palace moved the primitives into
  `iterative.cpp`; `orthog.md:227` already flags "the former L0 citations here pointed at `gmres.cpp`
  (likely stale)"). This is the existing OQ `plane-rotation-givens-l0-citation-range-reconcile` (named
  at `plane_rotation_stream.md:7`) — a citation-range/file reconciliation, not a slice-pointer repoint.
  It needs a `verify-citation-range` pass (codemap `get_symbol_def` on `GeneratePlaneRotation` to
  confirm the current file + line range), which is a different skill than this surgical repoint. **Left
  for that OQ; not touched here** to keep this a clean pointer swap.
- **Stale concept-graph edge, deferred (repairer-added cycle-013):** `dependency-map.md:188`
  (`orthog --> plane-rotation-stream`) is a mermaid concept-DAG dependency arrow that is stale-in-spirit
  after the cycle-012 reduction (orthog no longer holds the plane-rotation stream). Repointing/removing it
  is a concept-graph modeling decision (delete vs. re-source the edge), not the surgical "Used in"/"primary
  dissection" file-pointer swap this OQ scopes. Suggested follow-up: a **dependency-map-maintenance** pass
  (a future `layer-intro-author` or `same-layer-cross-cutter` dispatch) to audit `orthog`'s out-edges
  against the post-reduction concept-graph and prune/re-source the stale `--> plane-rotation-stream` edge.
- After integration, OQ `plane-rotation-concept-page-canonical-pointer-repoint` closes. The
  `plane_rotation_stream.md:5` stub-pointer note ("pending `layer-intro-author` dispatch") becomes
  satisfied — a follow-up could drop that "pending" clause, but that is a slice-prose touch (not a
  concept-page edit) and is left to a future phase-1-slice-reduction-audit dispatch rather than bundled
  here.

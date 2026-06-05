---
agent: same-layer-cross-cutter
invoked_at: 2026-06-04T23:37:38Z
scope: L-spec cross-cut — absorb-and-delete plane_rotation_stream slice + close OQ plane-rotation-givens-l0-citation-range-reconcile
status: integrated
integrated_at: 2026-06-04T232852Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean by integrator-per-report (D4); repairer fired pre-integration (citation line-numbers + ls-update-column firm-home-placeholder token inlined). plane_rotation_stream slice DELETED + L3 worked example absorbed into concepts/sequential-obstruction.md re-anchored to L0 iterative.cpp:634-640 + 5 concept repoints. Batch finalize cycle-097: cargo make book EXIT 0, step-5b rank_violations=0 (GATE PASS), no newly-orphaned node. retroactive-budget global 0. OQ plane-rotation-givens-l0-citation-range-reconcile recommended-CLOSE (resolved-by-deletion) for the batch-31 meta unify; a distinct end-bound citation-divergence sub-note appended under it stays open."
---

# CYCLE: spec slice-delete — plane_rotation_stream absorb-and-delete (graded-stack P2, batch-31 D4)

## Summary
The Phase-1 slice `book/src/spec/slices/plane_rotation_stream.md` is reachability-GC detritus: every section is superseded by firm chapters (the `givens` concept-page family + `L1/ls-update-column` + `L2/incremental-least-squares` + the two lowering themes), and its only unique surviving material — the §L3 Givens-stream replay-prefix obstruction analysis — already has a firm home at `concepts/sequential-obstruction.md` §"Worked example: Givens-stream replay-prefix". This dispatch (1) RECONCILES the long-open `:72-108` vs `:73-108` L0 off-by-one by direct source read — confirming `:72` is the `template <typename T>` line and `:73` is the `GeneratePlaneRotation` signature, that ALL firm chapters uniformly cite the canonical `:73-108`, and that the divergent `:72-108` exists ONLY inside the slice — so the discrepancy is **resolved-by-deletion**; (2) ABSORBS the elided replay-prefix content (cross-target no-batch-dim, local-triviality-at-extend, Householder-WY sibling boundary) into the worked-example section and re-anchors it to L0 directly (`iterative.cpp:634-640`) so the section survives the slice's death; (3) REPOINTS the 5 inbound concept canonical-instances off the dying slice onto firm homes; (4) PROPOSES deleting the slice.

## Observation kind
**Redundancy** — the slice and the firm `givens`-family + `ls-update-column`/`incremental-least-squares` + `sequential-obstruction` chapters are dissecting the same Givens-stream incremental-QR pattern; the slice is the less-complete Phase-1-corpus twin and reduces to nothing once its unique §L3 fragment is absorbed.

## Specific finding

### (1) OQ reconcile — the `:72-108` vs `:73-108` off-by-one is an in-slice L0 error, resolved-by-deletion

Direct read of `reference/palace/linalg/iterative.cpp:70-73` (via codemap `read_range`) — paste-inline of the boundary lines, absolute file positions:

```
70  }
71
72  template <typename T>
73  inline void GeneratePlaneRotation(const T dx, const T dy, T &cs, T &sn)
```

So `:70` = `}` (close of the prior function), `:71` = blank, `:72` = `template <typename T>`, `:73` = the `GeneratePlaneRotation` signature; the canonical kernel range is `:73-108`.

**The authoritative resolution (anchor-by-firm-corpus, not by re-deriving the raw line number):** the canonical range is `:73-108`, carried *uniformly* across every firm chapter. Paste-inline of ≥2 firm cites (grep-confirmed):

- `book/src/concepts/givens.md:33` — `` - `GeneratePlaneRotation` — `palace/linalg/iterative.cpp:73–108`. ``
- `book/src/L1/ls-update-column.md:572` — `` - `palace/linalg/iterative.cpp:73-108` — `GeneratePlaneRotation` (real): the … ``
- `book/src/L2/incremental-least-squares.md:429` — `` - `palace/linalg/iterative.cpp:73-108` — `GeneratePlaneRotation` (real): the … ``
- `book/src/L2-L1/incremental-least-squares-composition-lowering.md:337` — `` - `palace/linalg/iterative.cpp:73-108` — `GeneratePlaneRotation` (real): LAPACK-style scaled rotation ``
- `book/src/L1-L0/ls-update-column-mutation-rotation.md:219` — `` - `palace/linalg/iterative.cpp:73-108` — `GeneratePlaneRotation` (real); the … ``

The divergent `:72-108` appears in NO firm chapter — grep finds it ONLY inside the slice, at `plane_rotation_stream.md:7` (the "Pending lift / verify" note that raised the OQ) and `:43` (`real iterative.cpp:72-108`). Both die with the slice.

**Verdict:** the off-by-one is **resolved-by-deletion** — the canonical `:73-108` survives in the firm chapters (5 independent cites), and the lone divergent `:72-108` is excised when the slice is removed. No firm-chapter edit is needed; no krylov-trio anchor repoint is implicated (confirming the planner's codemap finding that this is an L0 off-by-one internal to the slice, NOT a slice-anchor repoint blocking the krylov trio). OQ `plane-rotation-givens-l0-citation-range-reconcile` is marked resolved-by-deletion (see Open questions).

### (2) Replay-prefix L3 content has a firm home; absorb the elided unique material + re-anchor to L0

The slice's §L3 (`plane_rotation_stream.md:242-367`) is the canonical detailed source for `concepts/sequential-obstruction.md` §"Worked example: Givens-stream replay-prefix" (`:83-113`). The worked example already carries the loop, the boundary-slot RAW, the representational-obstruction framing, and the quadratic-vs-linear cost argument. Per the slice's own reduction-status note (`:3`), the worked example *elides*: (a) the cross-target no-batch-dim analysis, (b) the local-triviality-at-extend, (c) the Householder-WY sibling-slice boundary. Once the slice is deleted these become homeless. The absorption (proposed-change below) folds a compact form of all three into the worked example and re-anchors the section to L0 **directly** (`iterative.cpp:634-640`) so it no longer depends on the dying slice for its source.

L0 verify-present (paste-inline, `iterative.cpp:633-640`, via codemap `read_range`):

```
634      for (int k = 0; k < j; k++)
635      {
636        ApplyPlaneRotation(Hj[k], Hj[k + 1], cs[k], sn[k]);
637      }
638      GeneratePlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);
639      ApplyPlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);
640      ApplyPlaneRotation(s[j], s[j + 1], cs[j], sn[j]);
```

The replay-prefix loop is `iterative.cpp:634-637`; the extend triple is `:638-640` (one generate, one apply-to-`Hj`, one apply-to-`s` — exactly the cross-target reuse + local-triviality structure). This is the direct positive L0 anchor for the worked example.

**Collision note honored:** D3 also edits `sequential-obstruction.md` but at the sparse-trisolve `:53` anchor region; this dispatch confines its edit to the §"Worked example: Givens-stream replay-prefix" region (`:83-113`) only.

### (3) Inbound concept canonical-instances repointed off the slice

Grep-confirmed the 5 named inbound references. Each repoints onto the firm home (the `givens`-family concept pages carry the canonical L0 mapping; `sequential-obstruction` re-anchors to L0 directly):

| File:line | current target | repoint to |
|---|---|---|
| `concepts/givens.md:40` | `[plane_rotation_stream slice](../spec/slices/plane_rotation_stream.md)` | `L2/incremental-least-squares.md` (firm canonical use site) |
| `concepts/givens_apply.md:27` | `[`plane_rotation_stream` slice](../spec/slices/plane_rotation_stream.md)` | `[`ls-update-column`](../L1/ls-update-column.md)` |
| `concepts/givens_generate.md:27` | `[`plane_rotation_stream` slice](../spec/slices/plane_rotation_stream.md)` | `[`ls-update-column`](../L1/ls-update-column.md)` |
| `concepts/plane-rotation-stream.md:37` | `[`plane_rotation_stream` slice](../spec/slices/plane_rotation_stream.md) — primary (canonical) dissection` | `[`incremental-least-squares`](../L2/incremental-least-squares.md) — primary (canonical) firm dissection` |
| `concepts/sequential-obstruction.md:85` | `[plane_rotation_stream](../spec/slices/plane_rotation_stream.md) slice's L2→L3 cycle` | L0-direct + `ls-update-column` (folded into the absorption proposed-change below) |

### (4) Slice deletion — reachability-GC detritus, no inbound `depends-on` blocking edge

The slice lives in `book/src/spec/slices/` (Phase-1 corpus — raw material, NOT part of the typed L-layer dependency graph). Every inbound reference is `reference`-kind (navigational "Used in"/"See also"/worked-example links), NOT a `depends-on` blocking edge. After the 5 concept repoints + the worked-example re-anchor, the only remaining inbound references are: (i) `book/src/SUMMARY.md:298` and `book/src/spec/index.md:19` — **owned by D5, NOT touched here**; (ii) `book/src/spec/slices/orthog.md:225-234` — a sibling-slice stub pointer (separate slice, out of this scope; flagged as Open question); (iii) `book/src/concepts/dependency-map.md` graph nodes (4 edges; out of named scope — flagged as Open question); (iv) frozen `meta-reviews/*` historical records (left as-is by convention). None is a graded-stack `depends-on` blocking edge. The slice is GC-unreachable detritus once D5 drops the SUMMARY/index rows — safe to delete.

## Recommendation
**Apply** all proposed-changes below (per-report integrator). Follow-ups to schedule:
- **Dispatch layer-intro-author** to clean the `dependency-map.md` `plane_rotation_stream` graph nodes (`:165, :247, :314-317`) — repoint the 4 edges (`--> givens`, `--> sequential-obstruction`, `--> tensor-field-lift`, `--> trsv`) onto `ls-update-column` / `incremental-least-squares`, or drop them, after this slice deletes. (Not in this dispatch's named scope; dependency-map is layer-intro-author territory.)
- **Defer** the `orthog.md:225-234` "Plane-rotation stream (reduced)" stub-pointer — it points at this slice as the canonical home. When this slice deletes, that stub's pointer dangles. Recommend a future `same-layer-cross-cutter`/`layer-intro-author` pass repoint the `orthog.md` stub onto the firm homes (or delete the stub block entirely, since the plane-rotation content is now fully firm). Out of this dispatch's named scope (separate slice file).

## Proposed changes

### Change 1 — absorb elided §L3 content + L0 re-anchor into `concepts/sequential-obstruction.md` (worked-example region `:83-113` ONLY)

Replace the worked-example section body. Anchor on the existing opening sentence so the edit is confined to the Givens-stream region (does not touch D3's sparse-trisolve `:53` region).

```edit
FILE: book/src/concepts/sequential-obstruction.md
OLD:
## Worked example: Givens-stream replay-prefix (plane_rotation_stream)

The [plane_rotation_stream](../spec/slices/plane_rotation_stream.md)
slice's L2→L3 cycle is a clean class-(a) obstruction. The L2 form is
an explicit loop:

```
for k in 0..j-1:
    (Hj[k], Hj[k+1]) = givens_apply(Hj[k], Hj[k+1], cs[k], sn[k])
```

Adjacent iterations share boundary slot `Hj[k+1]`: iteration `k`
writes it, iteration `k+1` reads it. This is the canonical small-N
read-after-write that prevents a single elementwise / gather-scatter
global tensor-field expression on `Hj`.

The algebraic shape: the stream represents a product of `j` Givens
factors `G_{j-1} · … · G_0`. Materializing the product as a dense
`j × j` unitary would be tensor-field-shaped (a matvec `Hj ← Q · Hj`)
but destroys the `O(j)` storage / flop savings that motivate the
factored representation. The obstruction is **representational**: the
tensor-field form exists in principle, but only in a representation
the algorithm was designed to avoid.

This pattern recurs across incremental-factorization streams
(Householder QR, modified Gram-Schmidt with reorthogonalization,
incremental Cholesky updates). Each carries the same structural
shape: a stream of small factors whose replay is sequential along
the stream index because successive factors touch overlapping
windows of the target.
NEW:
## Worked example: Givens-stream replay-prefix (GMRES least-squares update)

The GMRES least-squares column update ([`ls-update-column`](../L1/ls-update-column.md))
replays a stream of stored Givens rotations on each new Hessenberg
column — a clean class-(a) obstruction. The L0 site is the GMRES inner
loop (`palace/linalg/iterative.cpp:634-637` replay-prefix; `:638-640`
the per-step extend triple):

```
for (int k = 0; k < j; k++)            // iterative.cpp:634-637
{
  ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k], sn[k]);
}
GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]);   // :638
ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]);      // :639
ApplyPlaneRotation(s[j], s[j+1], cs[j], sn[j]);        // :640
```

**The replay-prefix obstruction.** In the loop, adjacent iterations
share boundary slot `Hj[k+1]`: iteration `k` writes it, iteration
`k+1` reads it. This is the canonical small-N read-after-write that
prevents a single elementwise / gather-scatter global tensor-field
expression on `Hj`. The algebraic shape: the stream represents a
product of `j` Givens factors `G_{j-1} · … · G_0`. Materializing the
product as a dense `j × j` unitary would be tensor-field-shaped (a
matvec `Hj ← Q · Hj`) but destroys the `O(j)` storage / `O(j·m)` flop
savings that motivate the factored representation — a quadratic-vs-
linear blowup that defeats incremental QR. The obstruction is
**representational**: the tensor-field form exists in principle, but
only in a representation the algorithm was designed to avoid.

**Local triviality at extend.** The per-step *extend* triple
(`:638-640`: one `GeneratePlaneRotation` + one `ApplyPlaneRotation` on
`Hj` + one on `s`) is a fixed three-primitive sequence with no loop. It
lifts unchanged — there is no iteration structure to globalize, so the
rotation is the identity. The obstruction is specific to the
replay-prefix *loop*, not the extend step.

**Cross-target reuse is per-step, not a batch dimension.** The two
`ApplyPlaneRotation` calls at `:639` / `:640` use the SAME `(cs[j],
sn[j])` pair but on **disjoint targets** (`Hj` column vs. `s` RHS).
This is not a tensor-field broadcast: each is one 2×2 rotation on one
2-tuple, with exactly two hard-coded call sites — there is no batch
dimension to `vmap` over. Even across the two targets the replays are
structurally non-fusible: replay-prefix touches only `Hj`, while the
`s`-pair rotation only ever happens at the same step index `j`, never
as a replay.

**Sibling-representation boundary (Householder-WY).** Removing the
obstruction requires changing the *factored representation*, not the
spec: Givens-stream stores `j` scalar pairs and replays a chain;
Householder-block QR with the WY representation stores a block
reflector `(V, T)` and applies it via two `gemv`/`gemm` calls — the
latter HAS an L3 global form, but at a different L0 and a different
per-step flop profile. That is a different algorithm, not a back-
correction of this one.

This pattern recurs across incremental-factorization streams
(Householder QR, modified Gram-Schmidt with reorthogonalization,
incremental Cholesky updates). Each carries the same structural
shape: a stream of small factors whose replay is sequential along
the stream index because successive factors touch overlapping
windows of the target.
```

### Change 2 — repoint `concepts/givens.md:40`

```edit
FILE: book/src/concepts/givens.md
OLD:
In primitive composition (L2), the two `givens` primitives compose
as an **incremental QR stream** — see
[plane_rotation_stream slice](../spec/slices/plane_rotation_stream.md)
for the canonical use site. The stream pattern is:
NEW:
In primitive composition (L2), the two `givens` primitives compose
as an **incremental QR stream** — see
[`incremental-least-squares`](../L2/incremental-least-squares.md)
for the canonical firm use site. The stream pattern is:
```

### Change 3 — repoint `concepts/givens_apply.md:27`

```edit
FILE: book/src/concepts/givens_apply.md
OLD:
- [`plane_rotation_stream` slice](../spec/slices/plane_rotation_stream.md) — applied repeatedly per Arnoldi step: $k$ times to the new Hessenberg column (replay of stored rotations), once to the same column (new rotation), once to the $\bar{g}$ vector pair.
NEW:
- [`ls-update-column`](../L1/ls-update-column.md) — applied repeatedly per Arnoldi step: $k$ times to the new Hessenberg column (replay of stored rotations), once to the same column (new rotation), once to the $\bar{g}$ vector pair.
```

### Change 4 — repoint `concepts/givens_generate.md:27`

```edit
FILE: book/src/concepts/givens_generate.md
OLD:
- [`plane_rotation_stream` slice](../spec/slices/plane_rotation_stream.md) — once per Arnoldi step, to generate the rotation that zeros the sub-diagonal of the new Hessenberg column.
NEW:
- [`ls-update-column`](../L1/ls-update-column.md) — once per Arnoldi step, to generate the rotation that zeros the sub-diagonal of the new Hessenberg column.
```

### Change 5 — repoint `concepts/plane-rotation-stream.md:37`

```edit
FILE: book/src/concepts/plane-rotation-stream.md
OLD:
- [`plane_rotation_stream` slice](../spec/slices/plane_rotation_stream.md) — primary (canonical) dissection of the stream as it appears in GMRES/FGMRES.
NEW:
- [`incremental-least-squares`](../L2/incremental-least-squares.md) — primary (canonical) firm dissection of the stream as it appears in GMRES/FGMRES.
```

### Change 6 — delete the slice file

```delete
FILE: book/src/spec/slices/plane_rotation_stream.md
REASON: Phase-1 corpus reduction (graded-stack P2 slice-deletion campaign, batch-31). All sections superseded by firm chapters (givens-family concept pages + L1/ls-update-column + L2/incremental-least-squares + the two lowering themes); the unique §L3 replay-prefix obstruction analysis absorbed into concepts/sequential-obstruction.md §"Worked example: Givens-stream replay-prefix" with L0-direct re-anchor (Change 1). The divergent in-slice L0 anchor `:72-108` (OQ plane-rotation-givens-l0-citation-range-reconcile) dies here; canonical `:73-108` survives in 5 firm chapters. Reachability-GC detritus: no inbound depends-on blocking edge. SUMMARY.md:298 + spec/index.md:19 rows dropped by D5.
```

## Supporting evidence

- **L0 reconcile:** `reference/palace/linalg/iterative.cpp:72` (`template <typename T>`), `:73` (`inline void GeneratePlaneRotation(...)`), full real kernel `:73-108` (read via codemap `read_range(70,110)`). Firm-chapter canonical cites: `concepts/givens.md:33`, `L1/ls-update-column.md:572`, `L2/incremental-least-squares.md:429`, `L2-L1/incremental-least-squares-composition-lowering.md:337`, `L1-L0/ls-update-column-mutation-rotation.md:219`. Divergent in-slice cite: `spec/slices/plane_rotation_stream.md:7,:43`.
- **L0 absorption anchor:** `reference/palace/linalg/iterative.cpp:634-637` (replay-prefix loop), `:638-640` (extend triple) — read via codemap `read_range(630,648)`.
- **Slice §L3 unique content absorbed:** `spec/slices/plane_rotation_stream.md:302-339` (cross-target/no-batch-dim `:302-309`, local-triviality-at-extend `:311-317`, Householder-WY sibling boundary `:329-339`).
- **Existing worked-example home (edited region):** `concepts/sequential-obstruction.md:83-113`.
- **Inbound repoint targets verified:** `concepts/givens.md:38-41`, `concepts/givens_apply.md:25-27`, `concepts/givens_generate.md:25-27`, `concepts/plane-rotation-stream.md:35-37`.

## Open questions / caveats

- **`plane-rotation-givens-l0-citation-range-reconcile` → RESOLVED (resolved-by-deletion).** The `:72-108` vs `:73-108` off-by-one was an L0 error internal to the slice. The canonical `:73-108` is carried uniformly by 5 firm chapters (verified by grep); the divergent `:72-108` existed ONLY in the slice and is excised by Change 6. No firm-chapter edit required; no krylov-trio anchor implicated. Mark the OQ resolved.
- **`dependency-map.md` `plane_rotation_stream` graph nodes (NEW open item).** `concepts/dependency-map.md:165,:247,:314-317` carry 4 graph edges from `plane_rotation_stream` (`--> givens`, `--> sequential-obstruction`, `--> tensor-field-lift`, `--> trsv`). These dangle after Change 6. Out of this dispatch's named scope (dependency-map is layer-intro-author territory). Recommend a layer-intro-author follow-up to repoint onto `ls-update-column`/`incremental-least-squares` or drop. NOT a `depends-on` blocking edge (dependency-map is a concept-graph mirror, not the typed L-layer graph), so it does not block deletion.
- **`orthog.md:225-234` stub-pointer (NEW open item).** The `orthog.md` slice carries a "Plane-rotation stream (reduced)" stub block pointing at this slice as the canonical home (`:225,:230,:234`). That pointer dangles after Change 6. Separate slice file, out of this dispatch's named scope. Recommend a future pass repoint the `orthog.md` stub onto the firm homes or delete the stub block (the plane-rotation content is now fully firm).
- **Caveat — codemap line-display offset.** The codemap `read_range(70,110)` payload's block-relative line presentation can drift by one from the absolute file line number, which is the historical origin of the `:72`/`:73` confusion. The reconcile does NOT depend on resolving that display offset: the AUTHORITATIVE canonical anchor is fixed by the firm corpus (`:73-108`, 5 independent cites), and the deletion removes the lone divergent claim regardless. If the integrator wants belt-and-suspenders, a `verify-citation-range` confirming `:73` is the `GeneratePlaneRotation` signature line against the firm chapters is already implicit in their uniform agreement.

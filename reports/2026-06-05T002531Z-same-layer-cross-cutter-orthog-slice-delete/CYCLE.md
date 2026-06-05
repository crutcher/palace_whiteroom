---
agent: same-layer-cross-cutter
invoked_at: 2026-06-05T002531Z
scope: L-spec slice corpus reduction — absorb-verify-and-delete slices/orthog.md (graded-stack P2 slice-deletion, batch-31 tranche-2, dispatch D1)
status: pending
integrated_at: 2026-06-05T002531Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean by integrator-per-report (D1, staging row 1); repair fired pre-integration (critic caught 8 MISSED inbound orthog links, repairer added PC-4 a–f). orthog slice DELETED (verified-no-op absorb) + 10 inbound links repointed to firm homes. cargo make book EXIT 0; step-5b rank_violations=0 GATE PASSES; no newly-orphaned node. Slice corpus 5→3 (with D2). OQ orthog-slice-substantive-absorb-framing-was-a-verified-no-op recommended-CLOSE at batch-31 meta unify."
---

# CYCLE: spec-slice reduction — orthog.md verified-absorb + delete

## Summary

I verified on disk that every unique datum in `book/src/spec/slices/orthog.md` —
the three MPI-collective-shape disclosures (MGS: m reductions of size 1; CGS: 1 of size m;
CGS2: 2 of size m) and the block-Gram-Schmidt L1 invariants (read-only `V` / mutated `w` /
written `H`; routine owns the reduction; variant inspected exactly once) — is **already
present in firm homes** (`concepts/orthogonalization.md`, `L1/L2/L3 orthogonalize.md`). The
slice's own header (lines 9, 11, 18) confirms it has been in *partial-reduction* status since
cycle-011 and was explicitly **waiting for** a firm `L1/orthogonalize` entry, which has since
landed. The absorb is therefore a **verified no-op** (no unique datum to lift). I propose
repointing the exactly-2 inbound cites off the slice and deleting the slice file. No
`depends-on` blocking edge targets the slice (reachability-GC clean).

## Observation kind

**Redundancy** — the slice is a now-superseded duplicate of firm layered entries. Every L1
invariant and collective-shape datum it "retained pending lift" has a firm home; the lift
target (`L1/orthogonalize.md`) exists and is firm. The slice is reachability-GC detritus.

## Specific finding

### 1. Verified-absorb evidence (paste-inline, on-disk)

The slice's L0→L1 header states its own residual claim (the thing it says is "NOT in firm
entries") at `spec/slices/orthog.md:15` and `:18`:

> the slice's L1 invariants (read-only `V_basis` / mutated `w` / written `H` / `dot_op` is
> local + routine owns reduction) and the MPI-collective shape disclosure (MGS: m reductions
> of size 1; CGS: 1 of size m; CGS2: 2 of size m) are NOT in firm entries. … **Pending lift to
> firm `L1/orthogonalize` operator entry** … the unique L1 invariants and the MPI-collective
> shape are retained in the L2/L3/L4 sections below pending a firm L1 row.

That residual claim is **stale** — the data IS now in firm homes. Evidence:

**`concepts/orthogonalization.md:42-58`** carries all three collective shapes + the L1 invariant
+ the inspected-once variant binding, verbatim-equivalent to the slice:
```
42  - **MGS (Modified Gram–Schmidt)**: single interleaved loop — for `k = 0..m-1`:
43    `H[k] = dot(w, V[k]); w ← w − H[k]·V[k]`. More stable than CGS; `m` synchronisations of
44    size 1 per step. Carries a [sequential-obstruction](./sequential-obstruction.md) at L3.
45  - **CGS (Classical Gram–Schmidt)**: split two-phase loop — all `m` `dot`s against the
46    *original* `w` (one reduction of size `m`), then all `m` updates. One synchronisation per
...
48  - **CGS2 (CGS with re-orthogonalisation)**: CGS applied twice; … Two synchronisations of size
49    `m`; …
53  The variant tag is a runtime enum (`Orthogonalization ∈ {MGS, CGS, CGS2}`) bound at solver
54  setup and **inspected exactly once** at dispatch (`OrthogonalizeIteration`,
55  `palace/linalg/iterative.cpp:308-325`); … (the residual being the per-variant collective shape:
57  m×1 / 1×m / 2×m reductions). …
```

**`L2/orthogonalize.md:19,150,347`** records the L2 collective shape as a property:
```
19   once; the per-variant collective shape is recorded as a *property* (a variant-axis note and
150  three levels under residual-axis disclosure for the L2 collective shape). The MPI collective
347  the per-variant collective shape is recorded as a *property* (a variant-axis note). The leaf
```

**`L3/orthogonalize.md:481`** carries the three-way shape at L3:
```
481  the variant selects, with the per-variant collective shape (m×1 / 1×m / 2×m reductions)
```

**`L1/orthogonalize.md:100-104`** carries the L1 invariants (read-only `V`, bound-once
variant, `[dot, axpy]` chain, residual = collective shape):
```
100  levels (a/b/c) under residual-axis disclosure** for the L2 collective shape
101  (`variant-absorption.md:131`): (a) the invariant unifies (law 1, the orthogonality contract
102  is variant-uniform), (b) the variant is bound at solve setup and threaded as a constructed
103  parameter with no per-column re-branch, and (c) the L_{n+1} primitive chain is the same
104  `[dot, axpy]` shape across all three — the only residual is the per-variant collective shape
```

The slice's L0 ground-truth (`palace/linalg/orthog.hpp:18-90`) is cited DIRECTLY by these firm
homes (`concepts/orthogonalization.md:54-55` cites `iterative.cpp:308-325`; the hpp ranges are
cited across the firm `*/orthogonalize.md` entries). No unique L0 navigation is lost by the
delete. **Conclusion: the absorb is a verified no-op — no datum to lift.**

### 2. The exactly-2 inbound cites (grep-confirmed)

```
$ grep -rn 'slices/orthog\|orthog\.md:' book/src --include='*.md' \
    | grep -v spec/slices/orthog.md | grep -v spec/index.md
concepts/gemv_basis.md:21: - **CGS / CGS2 orthogonalization** (`slices/orthog.md`): …
L1/orthogonalize.md:302:  "Pending lift to firm `L1/orthogonalize`" target named at `orthog.md:18`; …
```
> **CORRECTED (repairer, 2026-06-05).** This grep's `grep -v spec/slices/orthog.md` filter
> ALSO swallowed every inbound `[..](../spec/slices/orthog.md)` markdown link (the link-target
> text contains that string), so "exactly 2" is **wrong** — those 2 are build-safe backtick
> mentions; the load-bearing markdown links were hidden. The corrected inbound set (markdown
> links only, excluded by SOURCE-path prefix) is repointed in **PC-4** below:
> `L0/mpi-globalsum-and-collectives.md:69,:105`, `concepts/orthogonalization.md:77`,
> `concepts/gmres.md:23`, `concepts/sequential-obstruction.md:48`, and the 4 dangling
> sibling links in the surviving `spec/slices/arnoldi_step.md:67,:95,:115,:144`.
> `SUMMARY.md:295` is D2's R7 row-removal (co-applied with the delete); `spec/index.md` is
> D2's single-owner scope. After PC-1/PC-2/PC-4 the slice has zero live inbound links.

### 3. Reachability / stale-link checks

- **No `depends-on` blocking edge targets the slice** — `grep 'depends-on' … | grep orthog`
  (excluding the slice itself) returns nothing. The slice is reachable only by the 2 navigational
  cites above, both repointed below → after deletion it is unreachable detritus, safe to GC.
- **No real markdown `[..](..)` link to any c097-deleted slice** inside `orthog.md`. The only
  `plane_rotation_stream.md` mentions are bare-backtick inline-code in the reduction-status
  prose (lines 9, 227, 230) — build-safe, not load-bearing, and they leave with the file.
  (Full link inventory of orthog.md: all `](..)` targets resolve to live concept pages or
  `reference/` source — none to a deleted slice.)

## Recommendation

**Defer no action — enact the reduction this cycle.** Apply the 2 repoint proposed-changes and
the slice deletion below. No follow-up dispatch needed (the firm homes are complete; the
combinator/harvester/abstractor have no new pattern to chase here). One Open question records
the stale-framing correction so the planner's "substantive MPI-collective-shape absorb" label
isn't carried forward as if real work remained.

## Proposed changes

### PC-1 — repoint `concepts/gemv_basis.md:21` (slice-link → firm CGS batched-reduction home)

File: `book/src/concepts/gemv_basis.md`

```diff
-- **CGS / CGS2 orthogonalization** (`slices/orthog.md`): after the batched reduction yields the full coefficient vector `H[0..m-1]`, the basis correction `w − V H` is one `gemv_basis` call. The MGS variant cannot use `gemv_basis` for the reasons above.
+- **CGS / CGS2 orthogonalization** ([`orthogonalization`](./orthogonalization.md)): after the batched reduction yields the full coefficient vector `H[0..m-1]`, the basis correction `w − V H` is one `gemv_basis` call. The MGS variant cannot use `gemv_basis` for the reasons above.
```

Rationale: `concepts/orthogonalization.md` is the firm home of the CGS/CGS2 batched-reduction
contract (`:45-51`, "all `m` `dot`s … then all `m` updates" / "CGS applied twice"); it is the
correct navigational target for the `w − V H` basis-correction use site. Replaces a dead
slice-link with a live concept-page link.

### PC-2 — repoint `L1/orthogonalize.md:299-304` (pending-lift anchor → claim-free Provenance prose)

File: `book/src/L1/orthogonalize.md`

```diff
-- Slice `book/src/spec/slices/orthog.md` (cycle-011 partial reduction) retains the L2 (per-pass
-  primitive sequences, transparent-vs-load-bearing classification), L3 (CGS/CGS2 projector form;
-  MGS obstruction), and L4 (Solve-monad state stratification) sections. This firm L1 entry is the
-  "Pending lift to firm `L1/orthogonalize`" target named at `orthog.md:18`; with it landed, the
-  slice's L1 row reduces to a pointer to this chapter (a follow-on phase-1-corpus-reduction-audit
-  dispatch, not this one).
+- **Provenance.** This firm L1 entry was the lift target of the (now-deleted) Phase-1 slice
+  `spec/slices/orthog.md` (cycle-011 partial reduction → fully reduced and removed cycle-098,
+  graded-stack P2 slice-deletion campaign). With this entry, the L2/L3/L4 dissections it
+  retained (per-pass primitive sequences + transparent-vs-load-bearing classification; CGS/CGS2
+  projector form + MGS sequential-obstruction; Solve-monad state stratification) are firm at
+  `L2/orthogonalize.md`, `L3/orthogonalize.md`, and `concepts/orthogonalization.md`; its L0
+  ground truth is cited directly there (`palace/linalg/orthog.hpp:18-90`).
```

Rationale: this firm L1 entry **is** the lift target the slice was waiting for, so once the slice
is deleted the bullet's live reference to `orthog.md:18` becomes a dangling pointer to a deleted
file. The replacement is claim-free Provenance prose (no live link to the deleted slice; redirects
the reader to the firm L2/L3/concept homes). No citation/claim is altered — the slice carried no
unique claim, so nothing is lost.

### PC-3 — delete the slice file

Action: **delete** `book/src/spec/slices/orthog.md`

Justification (graded-stack rank/reachability): the slice carries no unique L1-invariant or
collective-shape datum (all in firm homes, §1); no `depends-on` blocking edge targets it (§3);
its only 2 inbound navigational cites are repointed by PC-1/PC-2. After PC-1/PC-2 it is
unreachable from any live entry → reachability-GC detritus → delete. Git history is the record
(MIGRATION/CLAUDE.md "Phase 1 corpus reduces … the corpus shrinks monotonically").

**Out of D1 scope (do NOT apply here):** the `SUMMARY.md` + `spec/index.md` row removals for
`orthog` (and `polynomial`) are D2's single-owner scope this cycle. The krylov-trio files
(`cg`/`gmres`/`arnoldi_step` slices, `krylov-step` chapters, `L4-L3/` dissolution themes) are
the c099 sub-campaign — untouched here.

### PC-4 — repoint missed inbound markdown links (repairer, cycle-098)

> **Repairer note (2026-06-05).** The §2 inbound count ("exactly 2") was produced by a grep
> whose `grep -v 'spec/slices/orthog.md'` self-exclusion filter ALSO swallowed every inbound
> `[..](../spec/slices/orthog.md)` markdown link — the link-*target text* contains that string.
> A corrected inbound sweep (`grep -rnE '\]\([^)]*spec/slices/orthog\.md|\]\(\./orthog\.md'`,
> excluding only lines whose SOURCE path begins `book/src/spec/slices/orthog.md:`) finds the
> live markdown links below, every one of which becomes a `mdbook-linkcheck2` hard error when
> PC-3 deletes the file. PC-1/PC-2's two repoints were build-safe backtick inline-code mentions,
> NOT the load-bearing links. These repoints are a mechanical build-necessity (dangling-link-to-
> deleted-file), in repair authority. SUMMARY.md:295 is **excluded** — it is D2's row-removal
> (R7), co-owned with the file deletion. Each `[old]` anchor verified against current disk.

**PC-4a — `book/src/L0/mpi-globalsum-and-collectives.md:69`** (general CGS-vs-MGS reference → firm collective-shape home):

File: `book/src/L0/mpi-globalsum-and-collectives.md`

```diff
-- `palace/linalg/orthog.hpp:70` — `Mpi::GlobalSum(m, H, comm)` inside `OrthogonalizeColumnCGS` (classical Gram-Schmidt; reduces the full m-vector at once, which is the algebraic distinction from MGS — see [`spec/slices/orthog`](../spec/slices/orthog.md)).
+- `palace/linalg/orthog.hpp:70` — `Mpi::GlobalSum(m, H, comm)` inside `OrthogonalizeColumnCGS` (classical Gram-Schmidt; reduces the full m-vector at once, which is the algebraic distinction from MGS — see [`orthogonalization`](../concepts/orthogonalization.md)).
```

**PC-4b — `book/src/L0/mpi-globalsum-and-collectives.md:105`** (general CGS-vs-MGS reference → firm collective-shape home):

File: `book/src/L0/mpi-globalsum-and-collectives.md`

```diff
-- **The `m`-vector CGS reduction** (`orthog.hpp:70`'s `Mpi::GlobalSum(m, H, comm)`) is **algebraically distinct** from a loop of single-element reductions — it reduces all `m` inner products in one collective call, which trades latency for one round-trip instead of `m`. This is a transparent performance trick at L0 / L1 (the algebraic result is the same), but it is the load-bearing distinction between MGS and CGS in the latency-bound regime. Recorded in [`spec/slices/orthog`](../spec/slices/orthog.md).
+- **The `m`-vector CGS reduction** (`orthog.hpp:70`'s `Mpi::GlobalSum(m, H, comm)`) is **algebraically distinct** from a loop of single-element reductions — it reduces all `m` inner products in one collective call, which trades latency for one round-trip instead of `m`. This is a transparent performance trick at L0 / L1 (the algebraic result is the same), but it is the load-bearing distinction between MGS and CGS in the latency-bound regime. Recorded in [`orthogonalization`](../concepts/orthogonalization.md) (the firm collective-shape home).
```

**PC-4c — `book/src/concepts/orthogonalization.md:77`** (self-page link to the slice → firm L2/L3 unfolding homes; drop the dead slice link):

File: `book/src/concepts/orthogonalization.md`

```diff
-  L3 (CGS/CGS2 lift to a clean batched/global form; MGS does not). See
-  [`spec/slices/orthog`](../spec/slices/orthog.md) for the retained L2/L3/L4 unfolding.
+  L3 (CGS/CGS2 lift to a clean batched/global form; MGS does not). See
+  [`L2/orthogonalize`](../L2/orthogonalize.md) and [`L3/orthogonalize`](../L3/orthogonalize.md)
+  for the firm L2/L3 unfolding.
```

**PC-4d — `book/src/concepts/gmres.md:23`** (bare provenance mention of the slice → drop the slice link, keep the firm concept link):

File: `book/src/concepts/gmres.md`

```diff
-- **Orthogonalization.** The Arnoldi-internal choice; see the [orthogonalization](./orthogonalization.md) concept and the [orthog](../spec/slices/orthog.md) slice.
+- **Orthogonalization.** The Arnoldi-internal choice; see the [orthogonalization](./orthogonalization.md) concept.
```

**PC-4e — `book/src/concepts/sequential-obstruction.md:48`** (slice L3-section reference → firm L3 home):

File: `book/src/concepts/sequential-obstruction.md`

```diff
-See the [orthog slice](../spec/slices/orthog.md) L3 section for the detailed treatment in the GMRES-orthogonalization context.
+See [`L3/orthogonalize`](../L3/orthogonalize.md) for the detailed treatment of the MGS sequential-obstruction in the GMRES-orthogonalization context.
```

**PC-4f — `book/src/spec/slices/arnoldi_step.md:67,:95,:115,:144`** (4 dangling `./orthog.md` sibling links inside the SURVIVING arnoldi_step slice → firm `concepts/orthogonalization` home).

> The arnoldi_step slice survives at c098 (its reduction is c099 krylov-trio scope), but these
> 4 links DANGLE the moment orthog.md is deleted this cycle. Repointing a dangling link off a
> deleted file is a mechanical build-necessity, NOT krylov-trio content work — in repair scope.
> Targets chosen so each link resolves to the firm orthogonalization home without changing the
> surrounding arnoldi prose's meaning.

File: `book/src/spec/slices/arnoldi_step.md`

```diff
@@ line 67 @@
-- **Output postcondition.** `V[j+1]` is unit-norm and orthogonal to `V[0..j]` (under exact arithmetic; under finite precision, to the level afforded by the chosen `gs_orthog` variant — see [orthog](./orthog.md)).
+- **Output postcondition.** `V[j+1]` is unit-norm and orthogonal to `V[0..j]` (under exact arithmetic; under finite precision, to the level afforded by the chosen `gs_orthog` variant — see [orthogonalization](../../concepts/orthogonalization.md)).
@@ line 95 @@
-The L1 procedure unfolds into four named primitive invocations. Three are field-side (MPI-collective vectors over the global DoF space); one is dispatch over the [orthog](./orthog.md) variant, itself a small composition of field-side primitives plus a residual choice.
+The L1 procedure unfolds into four named primitive invocations. Three are field-side (MPI-collective vectors over the global DoF space); one is dispatch over the [orthogonalization](../../concepts/orthogonalization.md) variant, itself a small composition of field-side primitives plus a residual choice.
@@ line 115 @@
-The projection `H[0..j] ← project(w, V[0..j]; gs_orthog)` with in-place subtraction `w ← w − Σ H[i,j]·V[i]` unfolds into the [orthog](./orthog.md) slice, which is itself a composition of [dot](../../concepts/dot.md) and [axpy](../../concepts/axpy.md) (plus a batched [gemv_basis](../../concepts/gemv_basis.md) call for CGS/CGS2 to amortise the MPI allreduce). The residual variant axis `gs_orthog ∈ {MGS, CGS, CGS2}` is bound at solve setup and dispatched here exactly once; the L2 composition for the Arnoldi step itself is variant-independent — only the unfolding of `orthogonalize` into its inner primitive chain differs. See [orthog](./orthog.md) §L2 for the inner unfolding and [variant-absorption](../../concepts/variant-absorption.md) level (b) for the dispatch-once discipline.
+The projection `H[0..j] ← project(w, V[0..j]; gs_orthog)` with in-place subtraction `w ← w − Σ H[i,j]·V[i]` unfolds into [orthogonalization](../../concepts/orthogonalization.md), which is itself a composition of [dot](../../concepts/dot.md) and [axpy](../../concepts/axpy.md) (plus a batched [gemv_basis](../../concepts/gemv_basis.md) call for CGS/CGS2 to amortise the MPI allreduce). The residual variant axis `gs_orthog ∈ {MGS, CGS, CGS2}` is bound at solve setup and dispatched here exactly once; the L2 composition for the Arnoldi step itself is variant-independent — only the unfolding of `orthogonalize` into its inner primitive chain differs. See [orthogonalization](../../concepts/orthogonalization.md) for the inner unfolding and [variant-absorption](../../concepts/variant-absorption.md) level (b) for the dispatch-once discipline.
@@ line 144 @@
-- `orthogonalize(..., w)` — `w` is the accumulator-mutation argument (signature of [orthog](./orthog.md) makes this explicit).
+- `orthogonalize(..., w)` — `w` is the accumulator-mutation argument (signature of [orthogonalization](../../concepts/orthogonalization.md) makes this explicit).
```

Rationale (PC-4 as a whole): each repoint moves a navigational link off the deleted slice onto
its firm home — `concepts/orthogonalization.md` for general collective-shape / orthogonalization
references, `L2/orthogonalize.md` + `L3/orthogonalize.md` where the original named the retained
L2/L3 unfolding or the L3 MGS-obstruction treatment specifically. No claim changes; the firm
homes already carry all the content (§1 absorb-no-op verification). After PC-4 + PC-1/PC-2,
zero live markdown links target the slice (modulo SUMMARY.md:295, removed by D2/R7 co-applied
with the deletion) → PC-3's delete is `linkcheck2`-clean.

## Supporting evidence

- Slice under reduction: `book/src/spec/slices/orthog.md` (full file read; header `:9,:11,:15,:18`
  states its own partial-reduction / pending-lift status).
- Firm homes: `book/src/concepts/orthogonalization.md:42-58`; `book/src/L1/orthogonalize.md:100-104`;
  `book/src/L2/orthogonalize.md:19,150,347`; `book/src/L3/orthogonalize.md:481`.
- L0 ground truth (cited directly by the firm homes, not via the slice):
  `palace/linalg/orthog.hpp:18-90`; `palace/linalg/iterative.cpp:308-325` (`OrthogonalizeIteration`).
- Inbound-cite grep + `depends-on` grep + markdown-link inventory: §2, §3 above.
- Repoint sites: `book/src/concepts/gemv_basis.md:19-23`; `book/src/L1/orthogonalize.md:297-310`.

## Open questions / caveats

- **Stale-framing correction (confirm/record).** The planner's tranche described a "substantive
  MPI-collective-shape absorb" for this slice. On disk that absorb is **already complete** — the
  m×1 / 1×m / 2×m disclosure is firm at `concepts/orthogonalization.md:44-50,57` and mirrored at
  `L2:19,150,347` / `L3:481` / `L1:100-104`. This dispatch is therefore a **verified no-op absorb
  + repoint + delete**, not a content-lift. Recording so the "substantive absorb" label is not
  carried forward into later tranches as if work remained. If a reviewer believes a *unique*
  datum was missed, the check to redo is: does any L1-invariant / collective-shape sentence in
  `orthog.md` lines 15, 18, 26-34, 40-46, 64, 71 lack a firm mirror? My read finds none.
- **OQ `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog`** is already marked answered at
  `L1/orthogonalize.md:309-310` ("answered by this dispatch"). The slice's `:18` reference to that
  OQ leaves with the file; no ledger action needed beyond what PC-2's Provenance prose records.
  (Flagging only so the integrator does not re-open it on seeing the slice's OQ mention vanish.)
- **PC-2 cross-reference (`arnoldi_step.md:5`).** `L1/orthogonalize.md:305-308` also names
  `slices/arnoldi_step.md:5` as a pending-lift prerequisite this entry satisfies. That slice is
  the **c099 krylov-trio sub-campaign** — explicitly out of my scope. I leave that bullet (305-308)
  untouched; my PC-2 edits ONLY the `orthog.md`-referencing bullet (299-304). Flagging so the
  integrator does not over-apply PC-2 onto the arnoldi bullet.

---
agent: same-layer-cross-cutter
invoked_at: 2026-06-05T002531Z
scope: L1 cross-cut — polynomial_recurrence_step slice absorb-verify-and-delete + dual-slice (orthog + polynomial) SUMMARY/spec-index row removal
status: pending
integrated_at: 2026-06-05T002531Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean by integrator-per-report (D2, staging row 2); repair fired pre-integration (R9 L3-site anchor repoint added). polynomial_recurrence_step slice DELETED (verified-no-op absorb) + surgical L2/krylov-step.md:7 polynomial-clause drop (cg/gmres/chebyshev/arnoldi preserved) + R2/R3/R9 anchor repoints + R4 mermaid + R5 delink + R7/R8 dual-slice SUMMARY+spec/index orphaned-row removal (both orthog + polynomial). cargo make book EXIT 0; step-5b rank_violations=0 GATE PASSES; no newly-orphaned node. Slice corpus 5→3. OQ polynomial-recurrence-step-slice-absorb-verified-no-op-and-campaign-state-5to3-slices recommended-CLOSE at batch-31 meta unify."
---

# CYCLE: L1 observation — polynomial_recurrence_step slice deletion (graded-stack P2, batch-31 tranche-2, Wave 2 / D2)

## Summary

The `polynomial_recurrence_step` Phase-1 slice is reachability-GC **detritus**: its catalog content (5-axis difference table + 4-site distinction catalog + per-claim falsification criteria + within-Chebyshev partial-positive) is **already fully absorbed** into the firm concept page `concepts/negative-result-slice.md` (verified on-disk below), and its remaining inbound references are all **navigational `reference` edges** (evidence pointers / dep-map slice-node edges / SUMMARY+spec-index nav rows) — **zero inbound `depends-on` blocking edges**. This dispatch verifies the absorb (no-op), surgically repoints the anchor sites off the slice (4 in the original scope-list plus the `L3/krylov-step.md:200` site added repair-phase as R9 — see §(2)), proposes deleting the slice file, and — as SOLE owner this cycle — removes the SUMMARY.md + spec/index.md rows for BOTH `orthog` (D1's deletion) and `polynomial_recurrence_step`. **Campaign state: 5→3 slices after c098; the `cg`/`gmres`/`arnoldi_step` krylov trio remains for c099.**

**One co-landing blocker found OUTSIDE the scope's 4-site list and surfaced as a required edit (item R5 below):** `concepts/negative-result-slice.md:46` and `:66` carry **live markdown links** `[...](../spec/slices/polynomial_recurrence_step.md)` that become dangling `linkcheck2` hard-fails the instant the slice is deleted. These MUST be delinked this cycle (proposed below). The scope's 4-site list is necessary but not sufficient; deleting the slice without R5 is a guaranteed build break.

## Observation kind

**Redundancy** — the `polynomial_recurrence_step` slice and the firm `concepts/negative-result-slice.md` page now carry the same negative-result catalog content; the slice is the pre-absorption duplicate. Resolution is deletion of the duplicate (the graded-stack reachability-GC sweep), with the concept page as the firm home.

## Specific finding

### (1) Absorb VERIFIED present — no-op. Paste-inline evidence from `concepts/negative-result-slice.md` (on-disk):

**Five-axis difference table** — the concept page explicitly names it as the cross-family evidence:

> `negative-result-slice.md:61` — "The distinction catalog and the **five-axis difference table** are the evidence."

> `negative-result-slice.md:66` — "Cross-family (Chebyshev ↔ GMRES ↔ eigentracking) the result is negative — different **scalar-state cardinalities, recurrence kinds, vector-update kernels, and termination shapes (the five-axis table)**. Within the Chebyshev family, however, 4th-kind and 1st-kind agree on **four of five axes** (vector-update shape, persisted-state shape, termination shape, outer-driver shape) and differ only on the **scalar-recurrence kind**..."

This reproduces the slice's `:89-97` table (5 axes: scalar-state cardinality, scalar recurrence kind, persisted derived state, vector-update shape, termination shape) and the slice's `:186-187` "four of five axes" framing.

**Within-Chebyshev partial-positive** — the concept page promotes it to a first-class sub-pattern with its own heading and worked example:

> `negative-result-slice.md:55-57` — "## Partial-positive sub-pattern / A negative result at one scope can coexist with a *positive* unification at a narrower scope... it should record **where unification fails AND where it would succeed**, scoped explicitly so the two claims do not contradict."

> `negative-result-slice.md:66` — "...so a `ChebyshevSmootherBase<ScalarGenerator>` parameterized on the single residual axis would absorb both variants cleanly. That refactor is structurally documented as a within-family partial positive *without* weakening the cross-family negative result..."

This reproduces the slice's `:170-189` "L1 ↔ L1 self-tightening" section and the `ChebyshevSmootherBase<ScalarGenerator>` refactor (slice `:176`).

**Per-claim falsification surface** — the concept page mandates and reproduces both the cross-family and within-family falsification criteria:

> `negative-result-slice.md:62` — the within-family partial positive "is documented as a distinct claim, with its **own falsification criterion**, alongside the cross-family negative result."

> `negative-result-slice.md:66` — "...the within-family claim carries its own **falsification surface** (the vector-update / outer-driver / termination shapes diverging between the two Chebyshev variants)."

> `negative-result-slice.md:75-84` — "## Falsification criterion (required structural element)... every negative-result slice MUST include a `### Falsification criterion` subsection... Absence-of-X is not falsified by spec-side desire for symmetry... The **polynomial_recurrence_step slice (2026-05-26) is the canonical worked example**."

This reproduces the slice's two falsification subsections (`:74-83` cross-family; `:191-199` within-Chebyshev).

**4-site distinction catalog** — named as the worked example with all four sites enumerated:

> `negative-result-slice.md:46` — "three independent scalar-update sequences (Chebyshev-4th-kind, Chebyshev-1st-kind, GMRES Givens stream) plus one out-of-scope branch (eigenvalue tracking via SLEPc/ARPACK). No Palace-level unification."

This reproduces the slice's 4-site catalog (`:101-108`: Chebyshev-4th, Chebyshev-1st, GMRES-Givens, eigentracking-obstruction).

**Verdict: VERIFIED no-op.** Every load-bearing catalog datum (5-axis table, partial-positive, dual falsification surfaces, 4-site catalog) is present in `negative-result-slice.md`. No unique catalog datum is missing; no absorb-into-concept-page proposed-change is needed. The L0 catalog sites (`chebyshev.cpp:63-92,113-155,191-220,261-293,230-258`; `iterative.cpp:73-120,227-250,555-651`; `slepc.cpp:687-720`; `arpack.cpp:35-115`) are the slice's own L0; the concept page references them transitively via the worked-example pointer and does not need to re-cite them inline (it is a methodology page, not a per-site catalog).

### (2) Reachability-GC detritus confirmation

Full corpus-wide inbound-reference sweep (`grep -rn polynomial_recurrence_step book/src/`, excluding the slice file itself) classifies every inbound edge:

| Site | Edge kind | Disposition |
|---|---|---|
| `L2/krylov-step.md:7` (polynomial clause in dense shared para) | `reference` (evidence pointer) | repoint R1 (surgical clause-drop) |
| `L2/krylov-step.md:142` (polynomial-only evidence bullet) | `reference` (evidence pointer) | repoint R2 |
| `L2/index.md:135` (polynomial-only dep-map evidence line) | `reference` (evidence pointer) | repoint R3 |
| `L3/krylov-step.md:200` (plain-text slice-anchor in the L3 "Five Phase-1 slice instances" list) | `reference` (evidence pointer; plain text, NOT a markdown link — no `linkcheck2` hard-fail, but a stale dangling text pointer on deletion) | repoint R9 (added repair-phase) |
| `concepts/dependency-map.md:169-171` (slice-node mermaid edges) | `reference` (nav graph) | repoint/remove R4 |
| `concepts/negative-result-slice.md:46,66` (LIVE markdown links) | `reference` (canonical-instance link) | **delink R5 — co-landing blocker** |
| `book/src/SUMMARY.md:296` (nav row) | nav | remove R7 |
| `book/src/spec/index.md:19` (status row) | nav | remove R8 |
| `L4/krylov-step.md:126`, `L4/index.md:28` | prose mention (filename in a list, NO link) | **no edit** — not a link, no linkcheck risk |
| `book/src/meta-reviews/*.md` (×N) | prose mention (NO link) | **no edit** — frozen historical record |

**Zero inbound `depends-on` blocking edges.** The slice is a leaf in the blocking-dependency graph; every inbound edge is navigational/evidential. The slice is reachability-GC detritus and is safe to delete once R1–R5, R7, R8, R9 land in the same cycle. (R9 added repair-phase: the `L3/krylov-step.md:200` plain-text slice-anchor was missed by the original sweep; it is a `reference` edge, build-safe but a stale dangling text pointer on deletion — see the sweep-table row above.) (Per the graded-stack rank/reachability bullet: no firm entry's rank rests on this slice; the firm homes — `L2/krylov-step.md`, `L4/chebyshev.md` §Semantics `innerStep`, `concepts/negative-result-slice.md` — carry the material.)

## Recommendation

Apply the 9 proposed-changes below (R1–R5 repoint/delink, R6 slice deletion, R7–R8 dual-slice row removal, R9 repair-phase L3-anchor repoint), then delete the slice file. **Defer** nothing — this is a mechanical reachability-GC sweep with the absorb already verified complete. Krylov trio (`cg`/`gmres`/`arnoldi_step`) deletion is c099's sub-campaign; this dispatch does NOT touch those files beyond the surgical polynomial-clause-drop at `L2/krylov-step.md:7`.

---

## Proposed changes

### R1 — `book/src/L2/krylov-step.md:7` — surgical polynomial-clause drop (LEAVE cg/gmres/arnoldi clauses INTACT)

This is the load-bearing edit. The line is a dense shared paragraph naming cg/gmres/chebyshev/arnoldi/polynomial anchors. Drop ONLY the trailing `polynomial_recurrence_step.md:119-160` clause; re-anchor its claim (the three polynomial-recurrence sites factoring into the kernel-plus-driver shape) to the firm `L4/chebyshev.md` §Semantics `innerStep` + `concepts/negative-result-slice.md`. The cg.md / gmres.md / arnoldi_step.md clauses are c099 krylov-trio material and MUST remain.

```edit
file: book/src/L2/krylov-step.md
old:
The Phase-1 slice corpus exhibits a recurring pattern: every iterative method written as a per-step kernel composed of (at most) five primitive groups, threaded by an outer fold. CG (the firm CG step-body evidence lives in this entry's §Evidence and lowers to L0 at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B — `iterative.cpp:360-486`; the L4-v0.5 first-iteration-unrolled rendering remains live at `book/src/spec/slices/cg.md:27-141`; original pre-reduction slice ranges `cg.md:103-115, :172-188, :393-425`), GMRES (`gmres.md:459-471`), Chebyshev (`book/src/L4/chebyshev.md` §Semantics `innerStep` — the polynomial-recurrence kernel), Arnoldi (`arnoldi_step.md:99-105, :285-298`), and the three polynomial-recurrence sites cataloged at `polynomial_recurrence_step.md:119-160` all factor into the same kernel-plus-driver shape. The combinator-miner cycle-002 enumerated the five pattern instances and proposed `krylov-step` as the L2 name for the kernel. This chapter is the firm operator definition.
new:
The Phase-1 slice corpus exhibits a recurring pattern: every iterative method written as a per-step kernel composed of (at most) five primitive groups, threaded by an outer fold. CG (the firm CG step-body evidence lives in this entry's §Evidence and lowers to L0 at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B — `iterative.cpp:360-486`; the L4-v0.5 first-iteration-unrolled rendering remains live at `book/src/spec/slices/cg.md:27-141`; original pre-reduction slice ranges `cg.md:103-115, :172-188, :393-425`), GMRES (`gmres.md:459-471`), Chebyshev (`book/src/L4/chebyshev.md` §Semantics `innerStep` — the polynomial-recurrence kernel), Arnoldi (`arnoldi_step.md:99-105, :285-298`), and the three polynomial-recurrence sites (Chebyshev-4th, Chebyshev-1st, GMRES-Givens-stream — the firm home is `book/src/L4/chebyshev.md` §Semantics `innerStep` for the Chebyshev pair and the cross-family non-unification catalog at `concepts/negative-result-slice.md`) all factor into the same kernel-plus-driver shape. The combinator-miner cycle-002 enumerated the five pattern instances and proposed `krylov-step` as the L2 name for the kernel. This chapter is the firm operator definition.
```

### R2 — `book/src/L2/krylov-step.md:142` — polynomial-only evidence bullet, re-anchor to concept page

This whole bullet is polynomial-only (the §Evidence list already has a separate `chebyshev.md` §Semantics `innerStep` bullet at `:140`). Re-anchor the catalog claim to `concepts/negative-result-slice.md` and drop the slice reference.

```edit
file: book/src/L2/krylov-step.md
old:
- `book/src/spec/slices/polynomial_recurrence_step.md:119-160` (catalog of three polynomial-recurrence sites — Chebyshev-4th, Chebyshev-1st, GMRES-Givens-stream — all factoring into a step-kernel-plus-outer-fold shape).
new:
- `book/src/concepts/negative-result-slice.md` §Partial-positive sub-pattern + §Falsification criterion (the catalog of three polynomial-recurrence sites — Chebyshev-4th, Chebyshev-1st, GMRES-Givens-stream — all factoring into a step-kernel-plus-outer-fold shape; cross-family non-unification with the five-axis difference table, plus the within-Chebyshev partial-positive). Chebyshev-pair firm home: `book/src/L4/chebyshev.md` §Semantics `innerStep`.
```

### R3 — `book/src/L2/index.md:135` — polynomial-only dep-map evidence line, re-anchor to concept page

(Confirmed on-disk `:131-134` are cg/gmres/chebyshev/arnoldi and untouched: `:131` cg, `:132` gmres, `:133` chebyshev `innerStep`, `:134` arnoldi.)

```edit
file: book/src/L2/index.md
old:
    - `spec/slices/polynomial_recurrence_step.md:119-160` (catalog of three instances)
new:
    - `concepts/negative-result-slice.md` §Partial-positive sub-pattern (catalog of three polynomial-recurrence instances; Chebyshev-pair firm home `book/src/L4/chebyshev.md` §Semantics `innerStep`)
```

### R4 — `book/src/concepts/dependency-map.md:169-171` — remove the 3 slice-node mermaid edges

The firm home carries these deps: the negative-result-slice relationship is the concept page itself; `elementwise-product` and `givens` are dep'd by the firm Chebyshev/GMRES homes (the `chebyshev-iteration` L2 entry deps `elementwise-product`; the plane-rotation stream deps `givens`). Remove the 3 underscore slice-node edges. **PRESERVE the distinct hyphenated planned-node** `polynomial-recurrence-step:::planned` at `:77-79` and `:98` (a speculative L1-operator node, NOT the slice node — different identifier, different subgraph).

```edit
file: book/src/concepts/dependency-map.md
old:
  polynomial_recurrence_step --> negative-result-slice
  polynomial_recurrence_step --> elementwise-product
  polynomial_recurrence_step --> givens
  plane-rotation-stream --> givens_generate
new:
  plane-rotation-stream --> givens_generate
```

### R5 — `book/src/concepts/negative-result-slice.md:46,66` — delink the canonical-instance links (CO-LANDING BLOCKER, outside the scope's 4-site list)

These are LIVE markdown links to the slice that dangle on deletion (`linkcheck2` hard-fail). The slice content is fully absorbed into THIS page, so the worked-example referent is now the page's own §Partial-positive / §Falsification sections. Delink to plain code-span text (preserve the prose; just remove the `(../spec/slices/...)` target).

```edit
file: book/src/concepts/negative-result-slice.md
old:
- [`polynomial_recurrence_step`](../spec/slices/polynomial_recurrence_step.md) — three independent scalar-update sequences (Chebyshev-4th-kind, Chebyshev-1st-kind, GMRES Givens stream) plus one out-of-scope branch (eigenvalue tracking via SLEPc/ARPACK). No Palace-level unification.
new:
- `polynomial_recurrence_step` (the scope question; its catalog is absorbed into this page's §Partial-positive sub-pattern and §Falsification criterion below — the Phase-1 slice was deleted cycle-098 as reachability-GC detritus, its Chebyshev-pair firm home is `book/src/L4/chebyshev.md` §Semantics `innerStep`) — three independent scalar-update sequences (Chebyshev-4th-kind, Chebyshev-1st-kind, GMRES Givens stream) plus one out-of-scope branch (eigenvalue tracking via SLEPc/ARPACK). No Palace-level unification.
```

```edit
file: book/src/concepts/negative-result-slice.md
old:
The canonical worked example is the [`polynomial_recurrence_step`](../spec/slices/polynomial_recurrence_step.md) slice's "L1 ↔ L1 self-tightening" section. Cross-family (Chebyshev ↔ GMRES ↔ eigentracking) the result is negative
new:
The canonical worked example is the `polynomial_recurrence_step` scope question's within-Chebyshev "L1 ↔ L1 self-tightening" finding (the Phase-1 slice was absorbed into this page and deleted cycle-098; its Chebyshev-pair firm home is `book/src/L4/chebyshev.md` §Semantics `innerStep`). Cross-family (Chebyshev ↔ GMRES ↔ eigentracking) the result is negative
```

(Note: `negative-result-slice.md:86` mentions "The polynomial_recurrence_step slice (2026-05-26) is the canonical worked example" as PLAIN PROSE — no markdown link — so it is NOT a linkcheck hazard and needs no edit. Left as-is.)

### R6 — DELETE the slice file

Reachability-GC detritus confirmed (no inbound `depends-on` blocking edge; all inbound `reference` edges repointed/delinked by R1–R5; SUMMARY/spec-index nav rows removed by R7–R8). Content fully absorbed into `concepts/negative-result-slice.md` (verified §1).

```delete-file
book/src/spec/slices/polynomial_recurrence_step.md
```

### R7 — `book/src/SUMMARY.md` — remove BOTH `orthog` and `polynomial` nav rows (SOLE owner this cycle)

On-disk verification (current disk, post-c097): `:295` is orthog, `:296` is polynomial; `:292` Arnoldi, `:293` CG, `:294` GMRES are the surviving trio rows — PRESERVED. D1's orthog file-deletion lands before this dispatch (integrator serializes), so the orthog row removal here is the matching nav cleanup (D1 owns the orthog file + its inbound cites; I own the orthog SUMMARY/spec-index ROW per scope).

```edit
file: book/src/SUMMARY.md
old:
  - [Orthogonalisation (MGS / CGS / CGS2)](./spec/slices/orthog.md)
  - [Polynomial recurrence step](./spec/slices/polynomial_recurrence_step.md)
new:
```

(Both lines removed; the preceding `- [GMRES](./spec/slices/gmres.md)` at `:294` and the following sub-chapter context are untouched.)

### R8 — `book/src/spec/index.md` — remove BOTH `orthog` and `polynomial` status rows (SOLE owner this cycle)

On-disk verification (current disk, post-c097): `:17` is the Orthogonalization status row, `:19` is the polynomial status row; `:15` CG, `:16` GMRES, `:18` arnoldi step are the surviving trio rows — PRESERVED. The planner's `:17`/`:19` estimate matches current disk.

```edit
file: book/src/spec/index.md
old:
| [Orthogonalization (plane-rotation stream)](./slices/orthog.md) | L4 (Gram-Schmidt) + L1 (plane-rotation) | 2026-05-26 | Gram-Schmidt stream at L4 (state-stratified, Solve-monadic, sequential-obstruction at L4). Plane-rotation stream lifted to L1 in same slice; uses `givens` and `trsv` primitives. Open question: split into orthog/gram_schmidt and orthog/plane_rotation once both reach L4. |
new:
```

```edit
file: book/src/spec/index.md
old:
| [polynomial recurrence step](./slices/polynomial_recurrence_step.md) | L1 (self-tightened) | 2026-05-26 | Negative-result catalog at cross-family scope (Chebyshev / GMRES / eigentracking do not unify); within-Chebyshev partial-positive promoted from Open Question 2 to a structurally-documented L1↔L1 self-tightening section with its own falsification surface. |
new:
```

(Both rows removed; the surviving `cg` `:15`, `gmres` `:16`, `arnoldi step` `:18` rows are untouched.)

### R9 — `book/src/L3/krylov-step.md:200` — missed inbound slice-anchor (plain-text), re-anchor to concept page (parallel to R2/R3)

Repair-phase addition (cycle-098 D2 critic `cross-reference-integrity` warning). `L3/krylov-step.md:200` carries the plain-text slice-anchor `book/src/spec/slices/polynomial_recurrence_step.md:119-160` — the exact sibling of the R1/R2/R3 anchors. It is the polynomial entry in the L3 "Five Phase-1 slice instances" list (the L3 mirror of the L2 §Evidence list); its immediate sibling at `:198` is the Chebyshev entry already anchored to `book/src/L4/chebyshev.md` §Semantics `innerStep`. Because it is plain text (not a markdown `[..](..)` link) it does NOT hard-fail `linkcheck2`, so R6 deletion stays build-safe — but it leaves a stale dangling text pointer to a deleted file in a firm L3 chapter. Re-anchor parallel to R2/R3: the catalog claim moves to `concepts/negative-result-slice.md`, the Chebyshev-pair firm home stays `book/src/L4/chebyshev.md` §Semantics `innerStep`. (`old` verified against current disk: line 200 matches verbatim.)

```edit
file: book/src/L3/krylov-step.md
old:
- `book/src/spec/slices/polynomial_recurrence_step.md:119-160` (catalog of three polynomial-recurrence sites; the L3 form is the value-thread-isomorphic image of each).
new:
- `book/src/concepts/negative-result-slice.md` §Partial-positive sub-pattern + §Falsification criterion (catalog of three polynomial-recurrence sites — Chebyshev-4th, Chebyshev-1st, GMRES-Givens-stream; the L3 form is the value-thread-isomorphic image of each; Chebyshev-pair firm home `book/src/L4/chebyshev.md` §Semantics `innerStep`).
```

---

## Supporting evidence

- **Absorb target (verified complete):** `book/src/concepts/negative-result-slice.md:46` (4-site catalog), `:55-73` (§Partial-positive sub-pattern + discipline), `:61,66` (five-axis difference table + four-of-five-axes partial-positive), `:62,66,75-84` (dual falsification surfaces), `:86` (slice named as canonical worked example).
- **Slice content being absorbed/deleted:** `book/src/spec/slices/polynomial_recurrence_step.md:70-119` (L1 distinction catalog: §Falsification criterion `:74-83`, five-axis table `:89-97`, 4-site catalog `:101-108`, shared/non-shared surface `:110-119`), `:170-189` (L1↔L1 self-tightening / within-Chebyshev partial-positive), `:191-199` (within-Chebyshev falsification surface). L0 sites the slice cites: `chebyshev.cpp:63-92,113-155,191-220,230-258,261-293`; `iterative.cpp:73-120,227-250,555-651`; `slepc.cpp:687-720`; `arpack.cpp:35-115`.
- **Surgical repoint sites (on-disk grep-confirmed line numbers):** `L2/krylov-step.md:7` (dense shared para; cg/gmres/chebyshev/arnoldi clauses to PRESERVE), `:142` (polynomial-only bullet); `L2/index.md:135` (polynomial-only dep-map line; `:131-134` trio+chebyshev to PRESERVE); `L3/krylov-step.md:200` (plain-text slice-anchor in the L3 "Five Phase-1 slice instances" list; sibling Chebyshev entry at `:198` already anchored to `L4/chebyshev.md` §Semantics `innerStep`; added repair-phase as R9); `concepts/dependency-map.md:169-171` (underscore slice-node edges to remove; `:77-79,:98` hyphenated `polynomial-recurrence-step:::planned` planned-node to PRESERVE).
- **Co-landing blocker (outside 4-site scope):** `concepts/negative-result-slice.md:46,66` live markdown links → R5.
- **Dual-slice row removal (on-disk grep-confirmed):** `SUMMARY.md:295` orthog / `:296` polynomial (trio `:292-294` preserved); `spec/index.md:17` orthog / `:19` polynomial (trio `:15,16,18` preserved).
- **Firm home for the Chebyshev pair:** `book/src/L4/chebyshev.md:134` (§Semantics; `innerStep` confirmed present).
- **No-edit prose mentions (NOT links, no linkcheck risk):** `L4/krylov-step.md:126`, `L4/index.md:28`, `book/src/meta-reviews/2026-05-26-cycles-{128-139,140-151,152-166}.md` (frozen historical records).

## Open questions / caveats

1. **Campaign state after c098: 5→3 slices.** The Phase-1 slice corpus drops from 5 (`cg`, `gmres`, `arnoldi_step`, `orthog`, `polynomial_recurrence_step`) to 3 (`cg`, `gmres`, `arnoldi_step`) after this cycle. The **krylov trio remains for c099** — those three carry live L4-v0.5 unrolled renderings / L4 monadic forms still referenced as evidence by `L2/krylov-step.md` §Evidence (e.g. `cg.md:27-141` first-iteration-unrolled, `gmres.md:459-471`, `arnoldi_step.md:99-105,:285-298`); their absorb-and-delete is the c099 krylov-trio sub-campaign and is explicitly out of this dispatch's scope.

2. **R5 is outside the scope's enumerated 4-site list but is a hard co-landing blocker.** The scope listed 4 anchor sites (krylov-step ×2, L2/index, dependency-map); it did not list `concepts/negative-result-slice.md:46,66`. Those are LIVE markdown links that dangle on deletion → `linkcheck2` hard-fail. I have proposed the delink (R5) because the slice deletion (R6) cannot land without it. If the integrator/critic considers `negative-result-slice.md` out of this dispatch's write-intent, R5 must instead be assigned to whoever owns the deletion's build-integrity — but it MUST land in cycle-098 alongside R6, not deferred. Flagging for critic edge-label-fidelity / cross-reference-integrity confirmation.

3. **D1 serialization assumption.** Per scope + integrator serialization, D1's `orthog` file-deletion + 2-cite repoint land before this dispatch is applied, so disk shows the orthog slice already gone when R7/R8 run. R7/R8 remove the orthog SUMMARY/spec-index NAV rows only (D1 does not touch SUMMARY/spec-index per the Wave split). If D1 did NOT delete the orthog file (e.g. D1 rejected), R7/R8's orthog-row removal would orphan-reference-free but leave a live `orthog.md` with no SUMMARY entry (mdBook drops untracked files silently — not a hard fail, but a coverage gap). Caveat for the integrator: confirm D1 landed before applying R7/R8's orthog clause; if not, hold the orthog-row half of R7/R8.

4. **`dependency-map.md` edge re-sourcing vs removal (R4 choice).** I chose REMOVAL of the 3 underscore slice-node edges rather than re-sourcing the node, because (a) the `negative-result-slice` relationship is the concept page itself (a node→node-to-itself edge is degenerate), and (b) `elementwise-product` / `givens` deps are already carried by the firm Chebyshev-iteration L2 entry and the plane-rotation-stream node respectively. If the integrator prefers a re-sourced firm node (e.g. a `chebyshev-innerStep --> elementwise-product` edge) over removal, that is a defensible alternative — but it would duplicate an edge the firm homes already carry. Removal is the lower-redundancy choice consistent with the graded-stack GC.

5. **Phase-1-slice-reduction-audit canonical-instance carve-out check.** The skill's carve-out retains a slice only if it is the §Canonical-instance referent of ≥2 concept pages AND carries unique L0 navigation. `polynomial_recurrence_step` IS named as canonical worked example by `negative-result-slice.md` (one page) — but the catalog + L0 navigation is now fully reproduced/absorbed into that same page (verified §1), so the "unique L0 navigation not covered elsewhere" condition FAILS. The carve-out does not apply; deletion is correct.

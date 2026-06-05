---
agent: same-layer-cross-cutter
invoked_at: 2026-06-04T232852Z
scope: L4 cross-cut — absorb-and-delete the cg_preconditioning_framework slice (graded-stack P2 slice-deletion, tranche 1, D1)
status: integrated
integrated_at: 2026-06-04T232852Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean by integrator-per-report (D1); cg_preconditioning_framework slice DELETED + 7 concept-page links repointed onto firm L4/preconditioning-framework.md. Batch finalize cycle-097: cargo make book EXIT 0, step-5b rank_violations=0 (GATE PASS), no newly-orphaned node. retroactive-budget global 0. OQ l4-preconditioning-framework-promotion recommended-CLOSE for the batch-31 meta unify."
---

# CYCLE: L4 observation — cg_preconditioning_framework slice is reachability-GC detritus

## Summary
The Phase-1 slice `book/src/spec/slices/cg_preconditioning_framework.md` is the cycle-001-era
precursor whose load-bearing material — including the §L4 / §L4-v0.2 / §L4-v0.3 framework calculus
that the slice's own reduction-status banner flagged as the last unhomed content — is now **fully and
firmly homed** in the firm L4 chapter `book/src/L4/preconditioning-framework.md` (harvested
cycle-096 D1, status `firm`, re-citing L0 directly). I verified the firm home covers every section
of the slice, grepped all inbound references (the planner's 7-page list is exactly correct — no
more, no less, among load-bearing concept pages), and confirmed there is **no inbound `depends-on`
(blocking) edge** targeting the slice: every inbound link is navigational (`reference`/"Used by"/
"Worked example"). The slice is therefore reachability-GC detritus. This report proposes repointing
the 7 inbound concept-page links onto the firm L4 chapter and deleting the slice file.

## Observation kind
**Redundancy** — the slice and the firm L4 chapter `preconditioning-framework.md` are the same
framework material under the old slice-vertical and new layered organizations; the slice is the
superseded copy. (This is the expected steady-state of the graded-stack slice-deletion campaign:
once a slice's unique content is lifted to a firm layered home, the slice becomes redundant detritus
to GC.)

## Specific finding

### (1) Firm-home verification — every slice section is covered by the firm L4 chapter

The slice's own reduction-status banner (slice lines 3–16) already declared §L0/§L1/§L2 "fully
absorbed" into firm `L1/ksp_solve` + the L0 anchors + the concept family, and named exactly three
**"RETAINED as load-bearing unique material"** sections as the *only* blocker to removal:

- **§L4 — calculus form** (slice lines 308–426): `KspParams`/`PcParams`/`OpBinding`/
  `BaseKspSolver` records + constructor-vs-body Haskell+TS form.
- **§L4 v0.2 — capability typing** (slice lines 428–485): the `TrueOp`/`PcAssemblyOp` brands +
  `finestLevelUnwrap` brand-preservation + `pc_op = op` escape hatch.
- **§L4 v0.3 — derived-view hoisting** (slice lines 487–548): the `pcBoundOp` stored-vs-bound
  derived view.

All three are now firmly transcribed (re-citing L0 directly) in
`book/src/L4/preconditioning-framework.md`. Section-by-section confirmation (paste-inline):

| Slice section | Firm L4 home (`book/src/L4/preconditioning-framework.md`) |
|---|---|
| §L4 records (`KspParams`/`PcParams`/`OpBinding`/`Ksp`/`Pc`/`Counters`/`BaseKspSolver`) | §Record definition, lines 79–146 (full TS record block + the `\|record\|stratum\|meaning\|L0 home\|` table with L0 citations `palace/linalg/ksp.hpp:30-76`, `:40`, `:41`, `:46`, `ksp.cpp:25-99`, `:125-235`, `:276-293`, `:296-310`) |
| §L4 constructor/body split (`buildKspSolver`/`setOperators`/`solve`/`applyPreconditioner`) | §Signature, lines 148–216 (same four primitives; same pure-construct / monadic-body stratification) |
| §L4 v0.2 capability typing (`TrueOp`/`PcAssemblyOp`, smart constructors, role-positional `setOperators`, escape hatch) | §Capability typing, lines 218–240 (brands + `asTrueOp`/`asPcAssemblyOp` + the `pc_op = op` double-brand escape hatch) |
| §L4 v0.2 `finestLevelUnwrap` brand-preservation invariant | §Derived-view hoisting, lines 260–264 (`finestLevelUnwrap :: PcAssemblyOp E -> PcAssemblyOp E` brand-preserving, "only ever applied to `pc_op`, never to `op`") + Law 3 (line 276–278) |
| §L4 v0.3 derived-view hoisting (`pcBoundOp`) | §Derived-view hoisting, lines 242–264 (`pcBoundOp` declaration + the exact `if isMultigridOp … then finestLevelUnwrap … else b.pc_op` body) + Law 4 (lines 279–283) |
| §L1 invariant (`op·x ≈ b`, spectral relationship), §L2/§L3 build-vs-run stratification | §Context rotations 1–3 (lines 56–70) + §Algebraic laws 1–5 (lines 266–287); §L1 BLAS-1 gate / SolveResult lives in firm `L1/ksp_solve` per the slice banner |

The firm chapter's own §Status closes the loop (paste-inline, lines 335–337):
> Source-of-truth absorbed from the `cg_preconditioning_framework` slice's §L4 / §L4-v0.2 / §L4-v0.3
> (the slice is the cycle-001-era precursor; this chapter is its firm L4 home, re-citing L0 directly).

**No UNIQUE unhomed load-bearing content remains in the slice.** The §L0/§L1/§L2/§L3 prose is
either (a) superseded framework narrative now carried by the firm chapter's §Context + §Signature +
§Algebraic laws, or (b) absorbed into firm `L1/ksp_solve` + the L0 anchor chapters per the slice's
own banner. Nothing requires absorbing into `L4/preconditioning-framework.md` before deletion. The
one residual OQ the slice banner cited as "blocks full removal"
(`l4-preconditioning-framework-promotion`) was **closed** by the c096-D1 harvest — see Open
questions §1.

### (2) Inbound-reference grep (paste-inline) — planner's 7-page list is exact

`grep -rn "cg_preconditioning_framework" book/src/ --include="*.md"` (filtering out the slice file
itself), load-bearing concept-page hits:

```
concepts/constructed-operator-factory.md:34:  - [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L1/L2 — both `build_ksp_solver` calls are factory instances.
concepts/solver-as-operator.md:30:        - [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L1/L2 — establishes the pattern for Palace's KSP composition.
concepts/finest-level-unwrap.md:22:      - [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L2 — invoked from `set_operators` when the operator-type matrix is asymmetric.
concepts/complex-from-real-lift.md:25:  [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) names this primitive as the L2 unfolding of `MfemWrapperSolver::Mult` …
concepts/complex-from-real-lift.md:31:        - [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L2.
concepts/counter-update.md:20:        - [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L2 — `solve` updates `counters.mult` and `counters.mult_it` …
concepts/two_operator_split.md:26:      - [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) (introducing slice).
concepts/build-time-vs-run-time-stratification.md:33: In [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md)'s L3:
```

That is the planner's exact 7 pages: `build-time-vs-run-time-stratification`,
`complex-from-real-lift` (2 hits), `constructed-operator-factory`, `counter-update`,
`finest-level-unwrap`, `solver-as-operator`, `two_operator_split`. **Confirmed accurate.**

Three OTHER inbound categories are out of D1 scope and untouched (reported for completeness):
- `book/src/SUMMARY.md:294` and `book/src/spec/index.md:22` — **D5's single-owner territory** per
  the hard constraint; NOT touched here.
- `book/src/concepts/dependency-map.md:168–389` — a generated/aggregate Mermaid edge listing keyed
  off the *slice* node, plus `book/src/meta-reviews/2026-05-26-*.md` and `concepts/rotation.md:136`
  — **historical-record prose / aggregate maps**, not live load-bearing navigational links into the
  slice from a concept's body. These are not in D1's repoint scope (dependency-map regeneration and
  meta-review archives are not slice-deletion blockers; flagged as a cross-cutting OQ, §2).

### (3) No inbound `depends-on` (blocking) edge — deletion is reachability-safe

Per the graded-stack rank/reachability bullet, deletion is only safe if the slice is reachable from
the feature-surface roots **solely via `reference` (navigational) edges**, never via a blocking
`depends-on` edge (which would constrain a live node's rank). I checked the firm L4 chapter's
frontmatter `edges:` block (lines 6–21): its `depends-on` targets are `L4/ksp_solve` and the L0
`ksp.cpp` range — **NOT the slice**; the slice appears in no `depends-on` anywhere. All 7 inbound
concept-page references are prose "Used by" / "Worked example" navigational mentions (the typed-edge
campaign treats concept "Used by" back-references as `reference`, free). The slice is a pure
reachability-GC leaf once these navigational links are repointed: **safe to delete.**

## Recommendation

**Dispatch the integrator to apply the proposed-changes below** (repoint 7 concept pages onto the
firm L4 chapter; delete the slice). No follow-up unification/combinator-mine is needed — this is a
clean absorb-and-delete; the firm L4 home already exists and the concept pages keep their primitive
provenance pointed at a live firm chapter.

## Proposed changes

### Repoint A — `concepts/constructed-operator-factory.md:34`

```
FILE: book/src/concepts/constructed-operator-factory.md
OLD:
- [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L1/L2 — both `build_ksp_solver` calls are factory instances.
NEW:
- [`preconditioning-framework`](../L4/preconditioning-framework.md) — `buildKspSolver`'s two `constructedOperatorFactory` calls (`KrylovRole`, `PrecondRole`) are factory instances; the variant axes absorb inside the factories (§Signature).
```

### Repoint B — `concepts/solver-as-operator.md:30`

```
FILE: book/src/concepts/solver-as-operator.md
OLD:
- [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L1/L2 — establishes the pattern for Palace's KSP composition.
NEW:
- [`preconditioning-framework`](../L4/preconditioning-framework.md) — the framework that binds a constructed `Pc<E>` (itself an `Op<E>`) into `BaseKspSolver`; establishes Palace's KSP composition pattern.
```

### Repoint C — `concepts/finest-level-unwrap.md:22`

```
FILE: book/src/concepts/finest-level-unwrap.md
OLD:
- [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L2 — invoked from `set_operators` when the operator-type matrix is asymmetric.
NEW:
- [`preconditioning-framework`](../L4/preconditioning-framework.md) — `finestLevelUnwrap` is the structural adapter inside the `pcBoundOp` derived view, fired when a multigrid `pc_op` meets a non-multigrid `pc` (§Derived-view hoisting).
```

### Repoint D — `concepts/complex-from-real-lift.md:25` and `:31`

```
FILE: book/src/concepts/complex-from-real-lift.md
OLD:
[`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) names this primitive as the L2 unfolding of `MfemWrapperSolver::Mult` on the `ComplexOperator` template specialisation. The real-solver specialisation is a passthrough (`apply_linop(M_real, r)` directly) and does NOT instantiate this primitive.
NEW:
[`preconditioning-framework`](../L4/preconditioning-framework.md) names this primitive as the unfolding of `applyPreconditioner` on the `ComplexOperator` specialisation (`Pc<Complex>`). The real-solver specialisation is a passthrough (`applyLinop pc r` directly) and does NOT instantiate this primitive.
```

```
FILE: book/src/concepts/complex-from-real-lift.md
OLD:
- [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L2.
NEW:
- [`preconditioning-framework`](../L4/preconditioning-framework.md) — §Signature `applyPreconditioner` body (complex pc) and §Variant axes (scalar-field).
```

### Repoint E — `concepts/counter-update.md:20`

```
FILE: book/src/concepts/counter-update.md
OLD:
- [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L2 — `solve` updates `counters.mult` and `counters.mult_it` after the delegated iteration.
NEW:
- [`preconditioning-framework`](../L4/preconditioning-framework.md) — `solve` threads `counters.mult` / `counters.mult_it` via `modifyCounters` after the delegated iteration (§Signature body phase; Law 5 counter-monotonicity).
```

### Repoint F — `concepts/two_operator_split.md:26`

```
FILE: book/src/concepts/two_operator_split.md
OLD:
- [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) (introducing slice).
NEW:
- [`preconditioning-framework`](../L4/preconditioning-framework.md) — the firm L4 home of the `(op, pc_op)` two-operator binding; capability-typed `TrueOp<E>` / `PcAssemblyOp<E>` (§Capability typing).
```

### Repoint G — `concepts/build-time-vs-run-time-stratification.md:33`

```
FILE: book/src/concepts/build-time-vs-run-time-stratification.md
OLD:
In [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md)'s L3:
NEW:
In [`preconditioning-framework`](../L4/preconditioning-framework.md) (§Context rotation 1; §Algebraic laws 2, 4):
```

(The two bullets below this line in `build-time-vs-run-time-stratification.md` (lines 35–38) name
`constructed-operator-factory` / `bind_preconditioner` / `finest-level-unwrap` as build-time and
`apply_linop`/`complex-from-real-lift`/`counter-update` as run-time; these primitive names all
survive in the firm L4 chapter — leave that prose as-is, only the link/lead-in line changes.)

### Deletion — the slice file

```
DELETE-FILE: book/src/spec/slices/cg_preconditioning_framework.md
```

Reachability-safe per §(3): no inbound `depends-on` edge; the 7 navigational concept-page links are
repointed above; `SUMMARY.md` + `spec/index.md` rows are D5's single-owner removal (do not touch
here per the hard constraint).

## Supporting evidence

- Firm home: `book/src/L4/preconditioning-framework.md` — §Record definition (lines 79–146),
  §Signature (148–216), §Capability typing (218–240), §Derived-view hoisting (242–264),
  §Algebraic laws (266–287), §Status (324–337, absorption provenance).
- L4 index row: `book/src/L4/index.md:119` (firm, full signature triple).
- Slice being absorbed/deleted: `book/src/spec/slices/cg_preconditioning_framework.md` — its own
  reduction banner (lines 3–16) naming §L4/§L4-v0.2/§L4-v0.3 as the only retained-unique blocker.
- Inbound concept-page links (grep above): `constructed-operator-factory.md:34`,
  `solver-as-operator.md:30`, `finest-level-unwrap.md:22`, `complex-from-real-lift.md:25,31`,
  `counter-update.md:20`, `two_operator_split.md:26`, `build-time-vs-run-time-stratification.md:33`.
- L0 ground truth (re-cited in the firm chapter, not re-verified here as the firm chapter is
  c096-firm): `reference/palace/palace/linalg/ksp.hpp:30-76`, `palace/linalg/ksp.cpp:276-293`
  (`SetOperators` + unwrap branch :281–292), `palace/linalg/ksp.cpp:296-310` (counter `Mult`).

## Open questions / caveats

1. **OQ `l4-preconditioning-framework-promotion` is already closed — confirm it is marked so.**
   The slice banner (line 14) cited this OQ as the gate for full removal; the firm chapter's §Status
   (line 326) states it was harvested c096-D1 *from* that OQ. This is the cross-cutting analogue of
   the "mint orthogonalize-mutation-rotation as roadmap_goal is already firm" stale note the dispatch
   prompt flagged: the OQ should be **closed** by the integrator/meta-phase if not already. Not a D1
   write target (OQ ledger is meta-phase-unify authority), surfaced for the next cycle-planner.

2. **`concepts/dependency-map.md` carries ~22 stale `cg_preconditioning_framework -->` edges**
   (lines 168–389, across the L1/L2/L3/L4 sub-maps). These reference the slice node, which is being
   deleted. They are an **aggregate generated map**, not in-body navigational concept links, so they
   are outside D1's repoint scope — but they will dangle once the slice node is gone. Recommend a
   follow-up (layer-intro-author / dependency-map maintainer, or the typed-edge GC linter) to
   regenerate the dependency-map with the slice node removed and (where still meaningful) its edges
   re-homed onto `L4/preconditioning-framework`. Flagging as cross-cutting; not blocking the slice
   deletion (a dangling Mermaid node label is not a `linkcheck2` hard error the way a dead
   markdown-link would be).

3. **Meta-review archives** (`book/src/meta-reviews/2026-05-26-cycles-*.md`) and
   `concepts/rotation.md:136` mention `cg_preconditioning_framework` as **historical narrative**
   (the cycle-123/133/141/156 traversal record). These are correctly NOT repointed — they describe
   the slice's *history as a slice*, which remains true; rewriting them to point at the L4 chapter
   would falsify the historical record. Left as-is by design.

4. **No load-bearing unhomed content found** — the §(1) check was exhaustive across all slice
   sections; I did not need to propose any absorb-into-L4 change. If the critic disputes coverage of
   any specific slice paragraph, the firm chapter's §Status absorption claim + the section table in
   §(1) is the evidence; escalate rather than block the deletion on a prose nuance.

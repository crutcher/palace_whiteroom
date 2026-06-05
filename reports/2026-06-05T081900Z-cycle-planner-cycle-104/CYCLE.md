---
agent: cycle-planner
invoked_at: 2026-06-05T081900Z
scope: cycle-104 dispatch plan
status: pending
---

# Cycle 104 dispatch plan

## Goals selected this cycle

Cycle-104 is position 2/3 of meta-batch-33; the LEAD is the meta-phase-owned **graded-stack
typed-edge campaign P1** (`priorities.md` item 1), continuing from c103's first tranche
(`untyped 142 → 78`, `rank_violations` 0, build green). This cycle takes the **next two
clean, non-meta-phase-owned P1 tranches** — the highest-value remaining real-node typed-edge
work — plus the cleanly-closeable content tail:

1. **The 6 record-concept pages** (`krylov`, `op-params`, `sim-state`, `step-outputs`,
   `prev-carry`, `solve-result`) get `edges:` frontmatter. These are REAL DAG nodes (the
   linter already gives each `rank: firm` via `Kind: record`, but they carry **zero** `edges:`
   frontmatter → zero outbound deps), so they are the c103-`dofset` analog: the cleanest,
   highest-value remaining typed-edge node work.
2. **Feature-column `uses-record` edges** rescue `config-record` + `dofset` + the 6 records
   from reachability-garbage (add `depends-on (kind: uses-record)` from the consuming feature
   columns — the GC roots — to each record node). This closes the GC-garbage findings c103
   routed forward.
3. **Content tail** (LOW): the homeless-primitive coverage gap (`set_subvector_zero` clearly
   needs an L1 home; `trsv` likely already homed as `back_solve` — harvester judgment) + two
   non-build-breaking prose-drift fixes (`L1/index.md:96` stale `eliminate_rhs` forthcoming
   prose; `concepts/incremental-least-squares.md:35` non-existent `givens-rotation` slug).

**Explicitly NOT dispatched (META-PHASE-owned; fires after c105):** the node-status convention
unification (`reference`-only block vs strict zero-frontmatter on the 16 cluster-B/C non-node
pages D2 left bare; OQs `graded-stack-concept-node-status-convention` /
`concept-non-node-frontmatter-encoding-reference-only-vs-empty`); the `navigational-container`
convention ratification into `graded-stack-scheme.md`; the two linter-gap fixes
(`is_likely_outside_dag` misses group-intro pages + `dependency-map`; the
`uses-record`-kind recognition). `tools/`/`skills/`/scheme are meta-phase write-authority.
These are flagged in `## Open questions / caveats` as carried.

## Deliverable-presence verification

Per the MANDATORY paste-inline-evidence pre-dispatch check (CLAUDE.md / skill
`verify-dispatch-scope-not-already-discharged`). Linter run: `python3
tools/graded-stack-lint/graded_stack_lint.py --book-src book/src` →
`files 353, typed 275, untyped 78, roots 36, rank_violations 0`.

### D1 — 6 record-concept pages get `edges:` frontmatter
1. **File existence + maturity:** all six EXIST and carry NO `edges:` frontmatter (the deliverable):
   ```
   concepts/krylov.md:       EXISTS, edges-frontmatter-count=0
   concepts/op-params.md:    EXISTS, edges-frontmatter-count=0
   concepts/sim-state.md:    EXISTS, edges-frontmatter-count=0
   concepts/step-outputs.md: EXISTS, edges-frontmatter-count=0
   concepts/prev-carry.md:   EXISTS, edges-frontmatter-count=0
   concepts/solve-result.md: EXISTS, edges-frontmatter-count=0
   ```
   Linter introspection confirms each is a typed node by rank but carries zero deps:
   `concepts/krylov untyped=False rank=3.0 deps=0` (same for op-params, step-outputs).
   The deliverable (add `edges:`) is NOT yet on disk.
2. **OQ-ledger OPEN-grep:** `graded-stack-six-record-concept-pages-need-frontmatter`
   (opened_at: cycle-103) is OPEN — no RESOLVED/CLOSED match. Pasted ledger entry confirms:
   "six `record` Kind concept pages still carry NO on-disk frontmatter today … *Route:* a
   follow-on harvester/layer-intro-author pass."
3. **Structural-block:** none. Records are unconditional DAG nodes (scheme §5: record ⇒ node);
   their L0 backing is on disk (`iterative.hpp:26-115`, `iterative.cpp:21-31/636-644`, etc.,
   already cited in each page body — pasted below). HARD-gate-new does not apply (existing files).

### D2 — feature-column `uses-record` reachability edges
1. **File existence:** `config-record` + `dofset` exist with typed `rank: firm` frontmatter
   (c103); they are currently `detritus=1` (unreachable garbage) per linter introspection:
   `concepts/config-record detritus=1 untyped=0`, `concepts/dofset detritus=1 untyped=0`.
   The 7 feature columns exist (`ls book/src/feature/` → lifecycle/electrostatic/magnetostatic/
   driven/transient/eigenmode + boundary-mode `.L4.md`).
2. **OQ-ledger OPEN-grep:** `config-record-reachability-gap` + `dofset-reachability-needs-uses-record-edge`
   both OPEN (opened_at: cycle-103) — no RESOLVED match. Pasted: "*Route:* add a
   `depends-on: { target: concepts/config-record, kind: uses-record }` edge to each of the 6
   driver columns + the lifecycle ROOT."
3. **Structural-block:** none for config-record (all 7 columns already `reference` it; the
   rescue inverts those to `depends-on (kind: uses-record)`). dofset is consumed by the
   BC-elimination cohort (L4/eliminate_bc + L1 BC verbs), reachable via the
   electrostatic/magnetostatic driver columns — the edge lands on the driver column that
   genuinely does BC-elimination. NOTE the linter does not yet *recognize* `kind: uses-record`
   as a distinct kind (a meta-phase/tools gap) — but `uses-record` is a `depends-on` edge, so
   the GC marks across it regardless of the `kind:` label (the linter ignores `kind:`).

### D3 — homeless-primitive L1 homes (harvester, judgment-first)
1. **File existence:** `L1/set_subvector_zero.md` ABSENT; `L1/trsv.md` ABSENT; BUT
   `L1/back_solve.md` EXISTS ("Mutation-lifted small-dense triangular back-solve") — so `trsv`
   is plausibly ALREADY homed under `back_solve` (the harvester must judge: a `reference` edge
   from `concepts/trsv` → `L1/back_solve`, NOT a new `L1/trsv`).
2. **OQ-ledger OPEN-grep:** `concept-primitive-without-L1-home-trsv-set_subvector_zero-gemv_basis`
   OPEN (opened_at: cycle-103) — no RESOLVED match. Pasted: "*Disposition to decide per
   primitive:* `gemv_basis` self-describes as 'a derived L2 primitive' so may legitimately
   live only as a concept (no promotion); `trsv` and `set_subvector_zero` are more clearly
   L1-shaped." So this is judgment-laden, NOT a reflexive harvest — frame as audit-first.
3. **Structural-block:** none. L0 anchors confirmed: `set_subvector_zero` →
   `palace/linalg/divfree.cpp:173` (`linalg::SetSubVector(rhs, *bdr_tdof_list_M, 0.0)`,
   codemap-confirmed); `trsv` → `palace/linalg/iterative.cpp:669` (back-solve loop).

### D4 — prose-drift fixes (lifter)
1. **File existence:** `L1/index.md:96` reads the stale "`eliminate-rhs-mutation-rotation`
   forthcoming (plain text — theme not yet authored)"; `concepts/incremental-least-squares.md:35`
   reads "L2 realisation depends on `givens-rotation`" (no `concepts/givens-rotation.md` exists;
   the kernel pair is `concepts/givens` + the split `givens_apply`/`givens_generate`).
2. **OQ-ledger:** `incremental-least-squares-prose-names-nonexistent-givens-rotation-slug` OPEN
   (cycle-103). The `eliminate-rhs` leg was FOLDED c103 (signal: "the `eliminate_rhs` L1>L0 leg
   is FOLDED") → the `L1/index.md:96` "forthcoming" bullet is now stale prose.
3. **Structural-block:** none — both are non-link prose-body text (NOT markdown links), so
   `linkcheck2` does not gate them; pure cosmetic correctness.

ALL FOUR dispatches PASS the four-step check (open, not already-discharged, not structurally
blocked, correct framing). None matches the STOP-PROPOSING negative list (`lu_solve`/`back_solve`/
`ls-update-column`/`nleps_*` as L3 backfills — N/A here; D3 touches `back_solve` only as a
`reference` target, not an L3 backfill).

## Dispatches

- **D1** — agent: `layer-intro-author`; scope: **P1 typed-edge tranche — the 6 record-concept
  pages.** Author canonical `edges:` frontmatter on each of `book/src/concepts/{krylov,
  op-params,sim-state,step-outputs,prev-carry,solve-result}.md`, mirroring the c103 `dofset.md`
  pattern: `rank: firm` (already implied by `Kind: record`; make it explicit in frontmatter)
  + `kind: record` + `depends-on` edges as `kind: cites-evidence` to each page's L0 backing
  source range (rank-terminal ground truth, so `rank(u)≤rank(v)` holds vacuously) + `reference`
  edges to the consuming operator chapters (`L4/krylov-step`, `concepts/state-stratification`,
  `concepts/solve-monad`, sibling record pages) per each page's existing body links. Pre-supplied
  L0 anchors (codemap/on-disk-confirm before citing; END line is the drift-prone bound):
  `op-params` → `palace/linalg/iterative.hpp:26-115,155-217`; `sim-state` →
  `palace/linalg/iterative.hpp:26-115`; `step-outputs` → `palace/linalg/iterative.cpp:21-31,
  395-397,642` + `iterative.hpp:54`; `prev-carry` → `palace/linalg/iterative.cpp:395-396,
  636-644`; `solve-result` → `palace/linalg/iterative.hpp:53-55`; `krylov` carries no direct
  L0 cite in-body (its schema is the worked CG/GMRES record shapes) — cite its iterative.hpp
  record home `palace/linalg/iterative.hpp:26-115` as `cites-evidence` (judge on-disk). NO
  SUMMARY edit (all 6 already registered). Resolves OQ
  `graded-stack-six-record-concept-pages-need-frontmatter`. deps: none. rationale: highest-value
  remaining typed-edge node work — 6 real record DAG nodes become proper rank-bearing,
  edge-declaring leaves; the c103-dofset analog. (priorities item 1, plan-tag
  `graded-stack-typed-edge-campaign-P1`.)

- **D2** — agent: `layer-intro-author`; scope: **P1 typed-edge tranche — feature-column
  `uses-record` reachability edges.** Add inbound `depends-on (kind: uses-record)` edges from
  the consuming feature columns (the GC roots) to the record-definition nodes, rescuing them
  from reachability-garbage: (a) **`config-record`** — add `depends-on: { target:
  concepts/config-record, kind: uses-record }` to each of the 7 columns that already
  `reference` it (`feature/{lifecycle,electrostatic,magnetostatic,driven,transient,eigenmode,
  boundary-mode}.L4.md` — invert their existing `reference` to a blocking `uses-record` edge,
  keeping the `reference` only where navigational); (b) **`dofset`** — add `depends-on (kind:
  uses-record)` → `concepts/dofset` from the BC-elimination-consuming driver columns
  (`electrostatic.L4`/`magnetostatic.L4`, which do essential-BC elimination); (c) **the 6
  record nodes** (krylov/op-params/sim-state/step-outputs/prev-carry/solve-result) — add
  `depends-on (kind: uses-record)` to them from the solve-consuming feature columns (the driver
  columns that compose `solve_family`/`krylov-step`; `transient.L4` already names them in-body).
  Author each so the rank invariant holds (record nodes are `rank: firm`, columns are `rank:
  firm` → firm `depends-on` firm, clean). Resolves OQs `config-record-reachability-gap` +
  `dofset-reachability-needs-uses-record-edge`; advances the 6-record reachability. deps: **D1**
  (the 6 record nodes must carry their typed frontmatter before the GC-rescue edges point
  `depends-on` at them — records already have rank=firm, so this is a cleanliness sequencing,
  not a hard rank dependency; config-record/dofset are already typed and can be edged
  independently). rationale: closes the reachability-GC garbage findings c103 routed forward;
  makes every record-definition node live (reachable from the feature roots). (priorities item 1.)

- **D3** — agent: `harvester`; scope: **content tail — homeless-primitive L1-home coverage
  gap (audit-first / judgment-per-primitive).** Decide and enact the L1 disposition for the
  homeless BLAS/vector primitives: **`set_subvector_zero`** (the divfree essential-DOF zeroing,
  `palace/linalg/divfree.cpp:173` `linalg::SetSubVector(rhs, *bdr_tdof_list_M, 0.0)`, codemap-
  confirmed) is clearly L1-shaped → author `book/src/L1/set_subvector_zero.md` + register in
  SUMMARY + add the `reference` back-link from `concepts/set_subvector_zero`; **`trsv`** — DO
  NOT author a new `L1/trsv.md`; `L1/back_solve.md` already EXISTS as the triangular back-solve
  L1 home (`iterative.cpp:669`) → repoint `concepts/trsv`'s edge to `reference: [L1/back_solve]`
  (the disposition is "already homed under another name", not a new home); **`gemv_basis`** —
  leave concept-only (it self-describes as "a derived L2 primitive"; no promotion). Resolves OQ
  `concept-primitive-without-L1-home-trsv-set_subvector_zero-gemv_basis`. deps: none. rationale:
  closes the homeless-pointer coverage gap; an L1 home for `set_subvector_zero` lets downstream
  divfree-projector/eliminate entries `depends-on`-link it with proper rank. LOW fan-out.

- **D4** — agent: `lifter`; scope: **content tail — two non-build-breaking prose-drift fixes.**
  (a) `book/src/L1/index.md:96` — the `eliminate_rhs` bullet's trailing "L1>L0 lowering
  `eliminate-rhs-mutation-rotation` forthcoming (plain text — theme not yet authored)" is stale:
  the `eliminate_rhs` L1>L0 leg was FOLDED into `fe-operator-assemble-mutation-rotation` c103
  (per c103 signal). Re-anchor the bullet to the live folded home (or strike "forthcoming",
  cite the firm `L1-L0/fe-operator-assemble-mutation-rotation` §"The `eliminate_rhs` leg (folded
  here)"). (b) `book/src/concepts/incremental-least-squares.md:35` — the §Dependencies prose
  names the non-existent slug `givens-rotation`; rewrite to name the existing `givens` (or the
  split pair `givens_generate`/`givens_apply`). Both are non-link prose-body edits (no
  `linkcheck2` gate). Resolves OQ `incremental-least-squares-prose-names-nonexistent-givens-
  rotation-slug`. deps: none. rationale: cheap narrative-honesty residue cleanup; both flagged
  c103. LOW fan-out.

## Overlap analysis

- **D1 ∩ D2:** D1 edits `book/src/concepts/{6 record}.md` (frontmatter on the record pages);
  D2 edits `book/src/feature/*.L4.md` (adds `depends-on (kind: uses-record)` edges). **DISJOINT
  file sets.** The only coupling is content-directional: D2's edges *point at* the record slugs
  D1 types. Since the record pages already exist (stable slugs, already `rank: firm` via
  `Kind: record`), there is no slug-invention risk and the rank invariant holds regardless of
  D1's landing. Sequenced D2-after-D1 for cleanliness (records fully edge-typed before the
  rescue edges land), NOT a hard write conflict. No shared-index consolidated-tally (per-page
  frontmatter, not a cohort count).
- **D1 ∩ D3:** D1 edits the 6 record concept pages; D3 may edit `concepts/set_subvector_zero.md`
  + `concepts/trsv.md` (back-link/repoint) + author `L1/set_subvector_zero.md` + SUMMARY.
  **DISJOINT concept-page sets** (D1's 6 records vs D3's set_subvector_zero/trsv). SUMMARY: D1
  makes NO SUMMARY edit; D3 adds one row (`L1/set_subvector_zero`) — no contention. Parallel-safe.
- **D1 ∩ D4:** D1 edits the 6 record pages; D4 edits `L1/index.md` + `concepts/incremental-
  least-squares.md`. DISJOINT. Parallel-safe.
- **D2 ∩ D3:** D2 edits `feature/*.L4.md`; D3 edits `L1/`+`concepts/set_subvector_zero,trsv`+
  SUMMARY. DISJOINT files. Parallel-safe.
- **D2 ∩ D4:** D2 edits `feature/*.L4.md`; D4 edits `L1/index.md`+`concepts/incremental-least-
  squares.md`. DISJOINT. Parallel-safe.
- **D3 ∩ D4:** D3 may edit SUMMARY + `L1/set_subvector_zero.md`+`concepts/{set_subvector_zero,
  trsv}.md`; D4 edits `L1/index.md`+`concepts/incremental-least-squares.md`. **DISJOINT** (D3
  does NOT touch `L1/index.md`; if D3 registers `L1/set_subvector_zero` in SUMMARY it appends a
  distinct alpha-position row — no overlap with D4 which touches no SUMMARY). Parallel-safe.

## Sequencing schedule

- **Wave 1 (parallel):** D1 (record-page typing), D3 (homeless-primitive harvest), D4
  (prose-drift) — fully disjoint file sets, no forward-reference coupling.
- **Wave 2 (after D1 report lands):** D2 (feature-column `uses-record` edges) — sequenced after
  D1 so its `depends-on` rescue edges point at the now-fully-typed record nodes (cleanliness;
  the per-report integrator wires the live edges against the landed record frontmatter). D2 is
  disjoint from D3/D4, which may still be in flight — the wave boundary is only D2←D1.

(One `integrator-finalize` at cycle end per the standing pipeline; the waves order dispatches,
not finalizes — the book is not rebuilt between waves.)

## Open questions / caveats

- **META-PHASE-OWNED, carried (NOT dispatched; fires after c105):** (1) the node-status
  convention unification — D2/cluster-B left 16 non-node concept pages with strict
  zero-frontmatter while D1/D3 wrote `reference`-only blocks (OQs
  `graded-stack-concept-node-status-convention`,
  `concept-non-node-frontmatter-encoding-reference-only-vs-empty`); plus the two borderline
  node-vs-non-node calls (`counter-update`, `chebyshev-iteration`). (2) the
  `kind: navigational-container` convention ratification into `graded-stack-scheme.md`. (3) the
  two linter-gap fixes (`is_likely_outside_dag` misses the ~23 group-intro pages +
  `concepts/dependency-map`; the `kind: uses-record` recognition — note D2's `uses-record` edges
  WILL mark correctly under the current linter because it is a `depends-on` edge and the linter
  ignores `kind:`, but the meta-phase may want the explicit kind recognized for reporting). All
  three are `tools/`/`skills/`/scheme write-authority — meta-phase only.
- **The 18 genuinely-untyped cluster-B/C non-node concept pages** (eigsolve, ksp_solve,
  solve-monad, convergence-test, state-stratification, constructed-operators,
  constructed-operator-factory, nested-constructed-operator-gate, capability-typing,
  build-time-vs-run-time-stratification, derived-view-hoisting, erasure-scope, counter-update,
  rotation, solver-as-operator, chebyshev-iteration, set_subvector_zero, trsv) are the c103-D2
  deliberate-zero-frontmatter set. Whether they acquire `reference`-only blocks or stay bare is
  the meta-phase node-status convention call above — DO NOT dispatch them as a typing tranche
  this cycle. (The `untyped: 78` count is dominated by these 18 + the 26 L0 ground-truth + 26
  meta-reviews + methodology/design/SUMMARY lazy tail; the lazy tail is correctly DEFERRED until
  the linter recognizes `cites-evidence`/`navigational-container` so they do not read as
  detritus noise — a meta-phase/tools dependency.)
- **D2 dofset rescue is the subtler of the two record rescues** — `dofset`'s direct consumers
  are L1/L4 BC-cohort entries, not feature columns; the `uses-record` edge should land on the
  BC-elimination-doing driver columns (electrostatic/magnetostatic). If the abstractor/author
  judges no single feature column cleanly "uses" dofset, route it as a finding (leave dofset's
  reachability to a later BC-cohort typing tranche) rather than forcing an unfaithful edge —
  per the redirect's "what a solver can't cleanly say is a finding about the spine."
- **The lazy tail (L0 ground-truth 26 + meta-reviews 26) deferral** is contingent on the
  meta-phase landing the `is_likely_outside_dag` + `cites-evidence`-exemption linter fixes; if
  the meta-phase declines those, a future planner must reconsider whether the L0 pages get
  `cites-evidence`-self frontmatter. Flag for the batch-33 meta-phase (fires after c105).

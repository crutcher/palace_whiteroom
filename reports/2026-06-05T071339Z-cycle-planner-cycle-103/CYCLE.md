---
agent: cycle-planner
invoked_at: 2026-06-05T071339Z
scope: cycle-103 dispatch plan (batch-33 position 1/3 — batch-OPENING; LEAD = graded-stack typed-edge campaign P1, FIRST incremental tranche)
status: pending
---

# Cycle 103 dispatch plan

## Goals selected this cycle

Batch-33 opens. The bottom-up forward frontier is substantially exhausted (the in-scope
stack is L4-complete for backend-lowering; `promotion_frontier: 8` is entirely
obstruction-/demand-gated), so the LEAD pivots to the **meta-owned graded-stack typed-edge
campaign (P1)** — `priorities.md` CYCLE-103 active-head item 1. This cycle is the **FIRST
incremental tranche** (option (a)-incremental, per the c094 edge-home decision): type the
**highest-fan-out / most-reachable untyped surface FIRST** (`untyped: 142` of 352), leaving
the low-reachability tail (meta-reviews / methodology containers / L0 ground-truth) to acquire
`edges:` lazily as next-touched, with the linters warn-not-fail on untyped throughout.

KEY ON-DISK FINDING driving the tranche selection (linter `--show-untyped` + per-directory
count): **every untyped L1–L4 file is a navigational container** (group-intro or layer
`index`) — NOT an operator (all 196 firm operators are already typed via legacy
`consumes:`/`depends_on:`/`lowers_to:`/`composes:` blocks the linter's migration mapping
reads). The genuine untyped DAG-adjacent vocabulary is the **47 `concepts/` pages** (the
shared substrate firm L_n entries `consumes:`), plus the container `index`/intro pages (the
node-vs-not-a-node call, OQ `graded-stack-index-and-concept-node-status`). The 26
`meta-reviews/` + 9 methodology/design/`introduction`/`SUMMARY` + 26 `L0/` ground-truth pages
are LOW-reachability / node-status-policy and are the lazy tail — DEFERRED this tranche.

So cycle-103 types the **highest-fan-out concepts/ substrate (47 pages, 3 thematic clusters)
+ the `concepts/` infra pair (`index` + `dependency-map`, reconciling the c101 light pass) +
the layer `index`/group-intro container pages (the node-status decision)**, and co-schedules
the LOW closeable content tail (item 2: `eliminate-rhs` split-vs-fold; `DofSet` definition
home; the 2 missing L4 §Vocabulary-cohort bullets) as disjoint-file cleanup. The campaign-level
sequencing remains meta-phase-owned; this is one tranche.

## Deliverable-presence verification (paste-inline evidence)

P1-typing dispatches (D1–D5) target files that **exist but carry NO parseable edge/rank
frontmatter** — "open by construction for typing" but I verified existence + untyped-state on
disk (the deliverable is the `edges:` block, which is genuinely absent):

```
# concepts substrate cluster — exist + edges_block count (0 = untyped):
book/src/concepts/dot.md                      EXISTS  edges_block=0
book/src/concepts/nrm2.md                     EXISTS  edges_block=0
book/src/concepts/scal.md                     EXISTS  edges_block=0
book/src/concepts/axpy.md                     EXISTS  edges_block=0
book/src/concepts/apply_linop.md              EXISTS  edges_block=0
book/src/concepts/eigsolve.md                 EXISTS  edges_block=0
book/src/concepts/ksp_solve.md                EXISTS  edges_block=0
book/src/concepts/orthogonalization.md        EXISTS  edges_block=0
book/src/concepts/constructed-operators.md    EXISTS  edges_block=0
book/src/concepts/state-stratification.md     EXISTS  edges_block=0
book/src/concepts/black-box-vs-accelerated-kernels.md EXISTS  edges_block=0
book/src/concepts/capability-typing.md        EXISTS  edges_block=0
# concepts page sample carries NO frontmatter at all (dot.md begins "# dot", no `---`):
#   confirms the `edges:` block must be authored from scratch.
# linter totals (fresh run this cycle):
#   files=352 typed=210 untyped=142 roots=36 rank_violations=0
#   unresolved_depends_on_targets=35 promotion_frontier=8
#   detritus=174 (of which detritus_no_typed_edges_pre_p1_artifact=111)
# untyped-by-directory: concepts=47 meta-reviews=26 L0=26 L1=8 L3=6 L2=6
#   methodology=4 L4=4 L1-L0=4 feature=4 design=2 SUMMARY=1 L4-L3=1 L3-L2=1 L2-L1=1 introduction=1
# every untyped L1–L4 entry is a `*-intro` or `index` container (confirmed via --show-untyped):
#   L1/{blas1-elementwise,constructed-operator-gates,fe-assembly,fe-space,krylov-least-squares,
#       nep-interior,operator-application}-intro + L1/index  (no operators)
```

Item-2 content-tail dispatches (D6–D8) — four-step check, all OPEN:

```
# 2a eliminate-rhs-mutation-rotation L1>L0 split-vs-fold (abstractor):
ls book/src/L1-L0/eliminate-rhs-mutation-rotation.md
  -> No such file or directory          (no dedicated sibling theme — fold-candidate)
book/src/L1-L0/fe-operator-assemble-mutation-rotation.md  EXISTS
grep -ci 'eliminate_rhs|EliminateRHS' fe-operator-assemble-mutation-rotation.md -> 12
  (the RHS-side leg is mentioned 12× in the firm fold file — strong fold-in candidate)
# 2b record-DofSet definition home (layer-intro-author):
ls book/src/concepts/dofset.md  book/src/concepts/DofSet.md  -> both No such file
  (DofSet[N] has 3 signature consumers: eliminate_bc + eliminate_essential_bc/eliminate_rhs
   + essential_dofs; record-definition obligation says >=2 -> concepts/<record>.md page)
# 2c missing L4 §Vocabulary-cohort bullets (layer-intro-author):
grep -E '^- \[`(eliminate_bc|preconditioning-framework)`\]' book/src/L4/index.md
  -> NO eliminate_bc / preconditioning-framework BULLET found  (count fixed c102 21+4; bullets lag)
# OQ RESOLVED grep (all three slugs): no RESOLVED/CLOSED matches -> all open.
# cycle-record tail: cycle-102 last primary; cycle-102-meta; NO cycle-103 landing.
#   counts_after(c102): L4_firm_main=21 L4_firm_grand=25 L4_L3=11 — unchanged, confirms nothing landed.
```

STOP-PROPOSING negative list checked: NO dispatch proposes any `promotion_frontier` member
(`bicgstab`/`minres`/`eigsolve-convergence-reason-mapping`/`deflate`/`deflate-composition-lowering`/`boundary-mode.*`)
or any disqualified L3-backfill slug. No forward-frontier / rectangular-pull-up pick is made.

## Dispatches

**ROLE-FIT NOTE (flagged to meta-phase — see Open questions):** the resume-notes guidance is
`layer-intro-author` (+ `lifter` cascade). P1 edge-typing is **authoring `edges:` frontmatter +
the typed dep-map prose into entries the author does not otherwise own** — it is neither new
operator algebra (harvester) nor a cross-layer observation (cross-cutter). `layer-intro-author`
is the closest fit (it already owns dep-map authoring + concept pages + the typed-edge
responsibility per METHODOLOGY-GRADED-STACK.md §8), so all P1 dispatches route there. The fit
is slightly awkward for the **non-concept-page, non-index** edge typing (none this tranche —
the operators are already typed), and there is no dedicated "edge-typer" role. Recorded as
useful friction signal for the meta-phase (it owns campaign sequencing).

1. **(`layer-intro-author`)** — P1 typed-edge: **`concepts/` cluster A — BLAS-1 / reduction /
   operator-application substrate.** Author the canonical `edges:` frontmatter block (per
   `book/src/methodology/graded-stack-scheme.md`, the `depends-on` / `reference` binary; an edge
   to a *root* is `reference`) into these untyped concept pages:
   `dot`, `nrm2`, `scal`, `axpy`, `apply_linop`, `apply_BA`, `gemv_basis`, `elementwise-product`,
   `trsv`, `two_operator_split`, `set_subvector_zero`, `scalar-promotion`, `complex-from-real-lift`,
   `tensor-field-lift`, `variant-absorption`, `finest-level-unwrap`.
   Each concept page is a **narrative pointer to its L1/L_n home** — type the down-edge to the
   authoritative operator entry as `reference` (navigational; the L1 entry is the definition,
   the concept page does not block it) UNLESS the page is itself a load-bearing substrate the
   operator `depends-on` (judge per page; default `reference` for pointer-pages). Resolve the
   index-page/concept-page node-vs-not-a-node call inline per OQ
   `graded-stack-index-and-concept-node-status` (a pure pointer page may be marked a
   non-node/`reference`-only). Do NOT touch operator entries (already typed). **deps: none.**
   *rationale:* highest-fan-out untyped surface — the BLAS-1/reduction substrate is `consumes:`-cited
   by the most firm L_n operators; types the most-reachable nodes first (item 1 LEAD).

2. **(`layer-intro-author`)** — P1 typed-edge: **`concepts/` cluster B — solver / iteration /
   calculus-typing vocabulary.** Author `edges:` into:
   `eigsolve`, `ksp_solve`, `solve-monad`, `solver-as-operator`, `convergence-test`,
   `state-stratification`, `constructed-operators`, `constructed-operator-factory`,
   `nested-constructed-operator-gate`, `capability-typing`, `build-time-vs-run-time-stratification`,
   `derived-view-hoisting`, `erasure-scope`, `config-record`, `counter-update`, `rotation`,
   `chebyshev-iteration`.
   Same typing discipline as D1 (down-edge to home = `reference` unless load-bearing
   `depends-on`; node-status call inline). **deps: none.**
   *rationale:* the second-most-reachable cluster — solver/calculus-typing concepts the L4 caps
   + solve-monad outer-driver vocabulary rest on; disjoint page set from D1/D3.

3. **(`layer-intro-author`)** — P1 typed-edge: **`concepts/` cluster C — krylov-internals +
   obstruction / disposition vocabulary.** Author `edges:` into:
   `gmres`, `givens`, `givens_apply`, `givens_generate`, `plane-rotation-stream`,
   `orthogonalization`, `incremental-least-squares`, `first-iteration-unrolling`,
   `sequential-obstruction`, `scope-out-obstruction`, `negative-result-slice`,
   `black-box-vs-accelerated-kernels`.
   Same discipline. The obstruction/disposition concept pages (`sequential-obstruction`,
   `negative-result-slice`, `black-box-vs-accelerated-kernels`) are heavily `reference`d by
   obstruction-status entries — type those down-edges `reference`. **deps: none.**
   *rationale:* completes the concepts/ substrate typing across the three disjoint clusters
   (D1+D2+D3 cover all 45 non-infra concept pages; the 2 infra pages go to D4).

4. **(`layer-intro-author`)** — P1 typed-edge + reconciliation: **the `concepts/` infra pair —
   `concepts/index.md` + `concepts/dependency-map.md`.** Type both, and **reconcile the c101 D2
   LIGHT in-prose edge-typing pass with the authoritative typed graph** (the c101 signal
   explicitly recorded the light pass should be reconciled here — OQ recorded c101). The
   `dependency-map.md` is the artifact's canonical edge-declaration home (scheme §3: "dep-maps
   are where edges are declared"); re-derive its node set + typed edges against the now-typed
   concept pages (D1–D3) and the firm operator graph. `concepts/index.md` is a navigational
   container — resolve its node-status inline (OQ `graded-stack-index-and-concept-node-status`).
   **deps: D1, D2, D3** (must read the cluster pages' freshly-authored typing to reconcile the
   dep-map against them — a content dependency; same-file edits are disjoint from D1-D3 which
   touch individual concept pages, not index/dependency-map). **WAVE 2.**
   *rationale:* the dependency-map is the highest-leverage single typed-edge artifact (the
   canonical edge home); reconciling it closes the c101 light-pass debt and gives the linter a
   coherent concepts/ sub-graph.

5. **(`layer-intro-author`)** — P1 typed-edge: **layer `index` + group-intro container pages —
   the node-status decision.** Type the navigational container pages:
   the per-layer `index` (`L1/index`, `L2/index`, `L3/index`, `L4/index`, `L1-L0/index`,
   `L2-L1/index`, `L3-L2/index`, `L4-L3/index`) + the group-intro pages
   (`L1/*-intro` ×7, `L2/*-intro` ×5, `L3/*-intro` ×6, `L4/*-intro` ×4, `L1-L0/*-intro` ×3,
   `feature/{driver-leaf,output-product,spine-root,index}`).
   These are **navigational containers, not vocabulary nodes** — the central call of OQ
   `graded-stack-index-and-concept-node-status`. Recommended disposition (the author decides +
   records the convention): mark them with `reference`-only edges to the chapters they index
   (an index page does not `depends-on` its members; it points at them), so they are reachable
   navigationally but carry no rank obligation. Author the convention decision into the dispatch
   report for the scheme page / meta-phase to ratify. Do NOT type `meta-reviews/`,
   `methodology/`, `design/`, `introduction`, `SUMMARY`, or `L0/` this tranche (lazy tail —
   node-status-policy / low reachability). **deps: none** (container pages are a disjoint file
   set from D1–D4's concept pages).
   *rationale:* resolves the index/group-intro node-status OQ on the most-visible container
   pages first; collapses a large slice of the 142 untyped count with one convention decision.

6. **(`abstractor`)** — item 2a: **`eliminate-rhs-mutation-rotation` L1>L0 split-vs-fold
   disposition.** Decide + enact: split the RHS-side BC leg into a dedicated sibling L1>L0 theme
   `book/src/L1-L0/eliminate-rhs-mutation-rotation.md` OR confirm it folds inline into the firm
   `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md` (which already mentions `eliminate_rhs`
   12×). The OQ ledger is explicit: this is `fe-bc-elimination-l1-l0-theme-split-vs-fold` viewed
   from L4, NOT a fresh thread. Resolves OQ
   `eliminate-rhs-mutation-rotation-l1-l0-half-forthcoming-vs-already-folded`. L0 anchors
   (codemap-confirmed c101): `rap.cpp:56 EliminateRHS`. **deps: none.** **fan-out: LOW.**
   *rationale:* small closeable content tail (item 2a); disjoint from all P1 files.

7. **(`layer-intro-author`)** — item 2b: **`record-DofSet` definition home.** Author
   `book/src/concepts/dofset.md` (the `DofSet[N]` record data-shape definition — fields, types,
   construction-vs-run-time stratum, the L0 home of the backing struct/`IoData` surface; NOT the
   operator algebra). `DofSet[N]` has 3 signature consumers (`eliminate_bc` cap + `eliminate_essential_bc`/`eliminate_rhs`
   + `essential_dofs`) → the record-definition obligation (≥2 consumers → `concepts/<record>.md`).
   Unify with the c055 `dof-set-concept-page` / `fe-bc-dof-set-and-set-subvector-concept-pages`
   cohort (judge whether `set_subvector_zero`'s mask record co-homes here). Resolves OQ
   `record-DofSet-needs-definition-home`. **Author the new page's `edges:` block typed from the
   start** (HARD-gate-new — the rank gate admits no new untyped node). **deps: none.**
   **fan-out: LOW.** *rationale:* item 2b; NEW file, disjoint.

8. **(`layer-intro-author`)** — item 2c: **the 2 missing L4 §Vocabulary-cohort bullets.** Author
   the per-chapter §Vocabulary-cohort prose BULLETS for `preconditioning-framework` (c096) +
   `eliminate_bc` (c101) in `book/src/L4/index.md` — the count was corrected c102 (21+4) but the
   two bullets lag (count-owner-vs-landing-dispatch split). Insert each in **alpha-within-cohort**
   position (directive-3; `eliminate_bc` between `eigenfreq_qfactor_reduce` and `fe_assemble`;
   `preconditioning-framework` in its alpha slot). Resolves OQ
   `vocabulary-cohort-bullets-missing-for-precond-framework-and-eliminate-bc`. **deps: D5**
   (D5 types `L4/index.md` as a container page; this dispatch edits the §Vocabulary-cohort prose
   of the SAME file → genuinely overlapping same-file region → sequential). **WAVE 2.**
   *rationale:* item 2c; the only same-file overlap in the plan (with D5 on `L4/index.md`).

## Overlap analysis

Pairwise (genuine overlap = same operator entry OR same theme/prose body OR same file region;
distinct dep-map rows / distinct files = NOT overlapping → parallel):

- **D1 ∩ D2 ∩ D3**: each types a DISJOINT subset of `concepts/` pages (clusters A/B/C are a
  partition of the 45 non-infra concept pages; verified no page appears in two clusters).
  Distinct files → **NOT overlapping → PARALLEL.**
- **D1/D2/D3 ∩ D4**: D4 touches `concepts/index.md` + `concepts/dependency-map.md` ONLY; D1-D3
  touch individual concept pages (never index/dependency-map). Disjoint files. BUT D4 must
  **read** D1-D3's freshly-authored typing to reconcile the dep-map → **content dependency**
  (not a write conflict) → D4 in WAVE 2 so the per-report integrator wires the dep-map against
  landed typed pages.
- **D1/D2/D3/D4 ∩ D5**: D5 touches layer `index`/group-intro container pages + `feature/` group
  pages. `concepts/index.md` is D4's (concept-library index); the layer indexes are D5's. NOTE:
  D5 types `L4/index.md` (container typing — frontmatter `edges:` block) and **D8 edits
  `L4/index.md` §Vocabulary-cohort prose** → see D5 ∩ D8 below. D5's other files are disjoint
  from D1-D4. → **PARALLEL with D1-D3; D8 sequenced after D5.**
- **D5 ∩ D8**: BOTH touch `book/src/L4/index.md` — D5 the frontmatter `edges:` block (top of
  file), D8 the §Vocabulary-cohort bullet prose (mid-file). These are distinct regions but the
  SAME file → mark **sequential** (D8 in WAVE 2, deps D5) to avoid a frontmatter-vs-body merge
  race. (Per conflict-tolerance philosophy this is a borderline same-file-distinct-region case;
  I sequence it because it is a single cheap ordering with a clean WAVE-2 slot already needed for
  D4 — no throughput cost.)
- **D6 (abstractor, L1-L0/) ∩ all**: touches `L1-L0/eliminate-rhs-mutation-rotation.md` (new) or
  `L1-L0/fe-operator-assemble-mutation-rotation.md` (firm). Disjoint from every P1 file and from
  D7/D8. → **PARALLEL.**
- **D7 (concepts/dofset.md, NEW) ∩ D1-D5**: a NEW concept page not in any D1-D3 cluster list and
  not the infra pair (D4). NOTE D4 reconciles `concepts/dependency-map.md` — the new `dofset.md`
  node may want a dep-map row. Minor: D4 may land before `dofset.md` exists. Treat as **PARALLEL**
  (conflict-tolerance: a missing dep-map row for a brand-new page is a cheap next-cycle add or a
  forward-reference the per-report integrator can stub; false-sequentialization is the worse
  error). If the integrator wants the row, D7's report names the canonical slug
  `book/src/concepts/dofset.md` so D4 (if co-wave) or a follow-up can wire it.
- **D7 ∩ D8**: distinct files (`concepts/dofset.md` vs `L4/index.md`). → **PARALLEL.**

**Shared-index / consolidated-tally guard:** No two dispatches co-author a consolidated running
count this cycle. D8 is the SOLE editor of the `L4/index.md` §Vocabulary-cohort prose (D5 only
adds the `edges:` frontmatter block, NOT the cohort bullets/count — partition stated in both
scopes). D5 is the SOLE owner of the layer-`index` container `edges:` typing. No dual-registration
collision (the P1 typing authors per-page frontmatter, not a cohort tally).

## Sequencing schedule

- **WAVE 1 (parallel):** D1, D2, D3, D5, D6, D7 — six parallel dispatches (disjoint files; the
  three concept clusters + the container-page typing + the two independent content-tail items).
- **WAVE 2 (parallel, after WAVE-1 reports land):** D4 (reconcile `concepts/dependency-map.md` +
  `concepts/index.md` against the landed D1-D3 typing), D8 (the 2 L4 §Vocabulary-cohort bullets,
  after D5's `L4/index.md` frontmatter typing lands).

Then the standard tail: N critics (parallel) → N repairers → `integrator-per-report` ×N (serial)
→ ONE `integrator-finalize` (rebuild book + step-5b linters + commit + push). The finalize's
step-5b linter run will show the `untyped` count drop materially (≈45 concept pages + the infra
pair + the container pages typed; the meta-reviews/methodology/L0 lazy tail remains untyped-warn,
which is expected under option (a)).

## Open questions / caveats

- **ROLE-FIT FRICTION (flag to meta-phase, which owns campaign sequencing):** P1 edge-typing has
  no dedicated role. `layer-intro-author` is the closest fit and carries the typed-edge
  responsibility (METHODOLOGY-GRADED-STACK.md §8), but five of this cycle's eight dispatches are
  `layer-intro-author` doing bulk frontmatter authoring across pages it does not otherwise own —
  a different shape than its usual "author a Part overview / concept page / group intro." If the
  campaign runs many more tranches this way, the meta-phase may want to (a) confirm
  `layer-intro-author` is the right home and tune its spec for bulk edge-typing, or (b) consider
  a thin dedicated edge-typer role. Recorded per the resume-notes invitation to flag awkward
  role-fit as useful friction signal.
- **Node-status convention (OQ `graded-stack-index-and-concept-node-status`) is decided
  IN-FLIGHT by D4 + D5** (concept-index + layer-index node-vs-not-a-node). The dispatches author
  the convention into their reports for the scheme page / meta-phase to ratify; if D4 and D5
  reach DIFFERENT conventions for "index pages," the meta-phase should unify at batch close. I
  did not pre-decide it (it is a scheme-level call the meta-phase owns); I recommended the
  `reference`-only-container reading as the default.
- **`unresolved_depends_on_targets: 35` are mostly prose-as-slug false-positives** (e.g.
  `L4/preconditioning-framework -> target: L4/ksp_solve` reads cleanly once typed; the
  `feature/*.L4 -> target: L4/fe_assemble` family). The P1 typing pass reclassifies them by
  construction (OQ `graded-stack-unresolved-target-prose-as-slug-p1-reclassify`); this tranche
  reduces but will not zero them (the feature-root `target:` prose lives in already-typed root
  files not retyped this tranche — a later tranche / the feature-root `seed`→`feature_root:`+`rank:`
  split, OQ `graded-stack-feature-root-frontmatter-split`).
- **Lazy tail deferred this tranche** (option (a)): 26 `meta-reviews/` (frozen historical —
  likely permanent non-nodes / `expected_unreachable_outside_dag`), 9 methodology/design/
  `introduction`/`SUMMARY` (methodology containers), 26 `L0/` ground-truth (leaf evidence —
  couples with the `kind: cites-evidence` exemption, OQ
  `cites-evidence-l0-edge-linter-slug-resolution-exemption`). These acquire `edges:` lazily or by
  a later tranche; the linters warn-not-fail on them.
- **`promotion_frontier: 8` untouched** — all obstruction-/demand-gated per the STOP-PROPOSING
  list; correctly NOT picked (the redirect forbids a rectangular pull-up). No forward-frontier
  dispatch this cycle (the frontier is exhausted; this is the genuine state, not a planning gap).

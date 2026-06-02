---
agent: cycle-planner
invoked_at: 2026-06-02T160332Z
scope: cycle-065 dispatch plan
status: pending
---

# Cycle 065 dispatch plan

## Goals selected this cycle

Cycle-065 is the SECOND primary cycle of meta-batch-20 (cycles 064/065/066; batch-20 meta-phase
fires after cycle-066's finalize). The FE-space/mesh-construction L1 front is OPEN (c064: `fe_space`
firm L1 + `fe-space-construction-rotation` firm L1>L0; the FE-space sub-spine has 1 member; L1 firm
31→32). This cycle advances the front on two fan-out-ranked axes, both following directly from the
front-opening:

1. **The opaque-parameter re-anchor (HIGH, replace-and-propagate)** — now-UNBLOCKED with `fe_space`
   firm on disk: the 4 firm entries that take the FE-space opaquely (`fe_assemble`, `weak_form_term`,
   `eliminate_essential_bc`, `eliminate_rhs`) gain live `fe_space` cross-refs for their bare
   `space`/`N`/`DofSet[N]` typed parameters. This is the enactment the front-opening set up — it
   completes the front-opening's downstream value (de-opaquing the assembled-operator cohort onto its
   freshly-lifted substrate). The REDIRECT's replace-and-propagate, not mine-and-strand.
2. **ONE new FE-space operator, WARRANT-FIRST (`fe_collection`, MEDIUM)** — the FE-collection
   order-schedule `ConstructFECollections`. The c064 D1 survey flagged it borderline-second-entry
   (fold-first as `fe_space`'s collection-input variant axis; split only if self-standing laws justify
   a chapter). On-disk inspection (`palace/fem/multigrid.hpp:22-73`) shows the schedule DOES carry
   genuine self-standing structure (a family-dependent `pmin` order floor, GaussLobatto/Legendre+LOR
   basis selection, the LINEAR/LOGARITHMIC order-coarsening schedule, the finest↔coarsest reverse) —
   a *list*-producing schedule, not a rename of `fe_space`. The harvester makes the warrant call
   (genuine entry vs. variant-axis note); if warranted, its L1>L0 follows.

`essential_dofs` STAYS DEFERRED this cycle (the thinner, more MFEM-boundary-straddling lift — only
the attribute→marker→dof-set *shape* lifts, dof-numbering is read-as-given; the survey leaned
noted-property-of-`fe_space` unless `eliminate_*`'s `DofSet[N]` demands a self-standing home).
`fe_space_hierarchy` (multigrid stack — lower fan-out for the assembly front) stays deferred.

Both axes follow the 2026-06-01 VOCABULARY-SHIFT REDIRECT: combinator-as-entry, lowerings-are-
translations-not-renames, anti-mirror (NO `dof_map` mirror; the warrant-first `fe_collection` may
itself decline and fold as a variant axis), replace-and-propagate. MPI/`Par*`/partitioning are
out-of-scope (single-machine; `ParFiniteElementSpace` read single-rank).

## Deliverable-presence verification (paste-inline-evidence per Discipline)

> NOTE: per the c064 finalize integration-tooling-friction note, `palace-codemap` `read_range`
> exhibited ±1 line-drift on `fespace.hpp` this batch. ALL line ranges below were verified directly
> against the on-disk file `reference/palace/palace/fem/multigrid.hpp` (the on-disk path is the
> nested `reference/palace/palace/...`; the citation form `palace/fem/...` is relative to
> `reference/`), NOT taken from codemap. Codemap was used only to LOCATE symbols, then ranges were
> confirmed on disk via the Read tool.

**D1 — opaque-parameter re-anchor (lifter, in-place; 4 files):**
1. File existence — all 4 EXIST:
   - `book/src/L1/fe_assemble.md` → EXISTS
   - `book/src/L1/weak_form_term.md` → EXISTS
   - `book/src/L1/eliminate_essential_bc.md` → EXISTS
   - `book/src/L1/eliminate_rhs.md` → EXISTS
2. Re-anchor not-already-done — `grep -c "fe_space.md"` on each = **0** (zero existing `fe_space.md`
   live links in all 4 — the re-anchor is genuinely open, not a no-op):
   `fe_assemble.md fe_space.md-links=0`, `weak_form_term.md=0`, `eliminate_essential_bc.md=0`,
   `eliminate_rhs.md=0`. On-disk parameter framing confirmed bare/opaque: `fe_assemble.md:60`
   `space: FiniteElementSpace[N]` + `:67`; `eliminate_essential_bc.md:56,67` `dofs: DofSet[N]`;
   `eliminate_rhs.md` essential gather/scatter over the opaque dof set; `weak_form_term.md`
   `A(space, ·)` opaque map references.
3. OQ-ledger — `fe-space-opaque-parameter-reanchor-now-unblocked` is the c064 D2 New-intake item,
   marked TRACTABLE in `integrator-signals.md` cycle-064 §Unblocked (NOT closed — genuinely open and
   now actionable). The forward-look `fe-space-opaque-parameter-reanchor-forward-look` is
   partially-answered (the theme landed c064 D3; the re-anchor pass is "now unblocked, deferred to a
   later cycle" = THIS cycle).
4. Structural block — NONE. `fe_space` is firm on disk (c064); the cross-ref targets resolve to a
   live link (`book/src/L1/fe_space.md` EXISTS). The c064 D4 §"Firm (FE-space sub-spine)" subsection
   (`L1/index.md:94`) explicitly says "a later replace-and-propagate dispatch, NOT this cycle [c064]"
   — c065 is that later dispatch.

**D2 — `fe_collection` harvest (harvester, WARRANT-FIRST, new operator):**
1. File existence — `ls book/src/L1/fe_collection.md` → `No such file or directory` (ABSENT). Also
   verified absent at c064 D1 survey (paste: "also verified absent: ... `fe_collection.md`").
2. Maturity — N/A (absent). The slug is a named-not-authored rough-in sibling in `L1/index.md:88`
   ("`fe_collection` *(rough-in; no anchor yet)*") — open, not discharged.
3. OQ-ledger — `grep` for `fe_collection` RESOLVED/CLOSED → no closed disposition; it is the #2
   fan-out pick in the OPEN `fe-space-sub-spine-backlog-pick-list` (c064 D1 New-intake,
   `integrator-signals.md` cycle-064 §Unblocked, TRACTABLE).
4. Structural block — NONE. NOT on the STOP-PROPOSING negative list (the list is `lu_solve`,
   `back_solve`, `ls-update-column`, 4 NLEPS atoms, `apply_nonlinear_pencil` HELD, `L3/solve_family`,
   `L2/fold_solve`, `L2/fe_assemble` — no FE-space-construction slug). Open-by-construction (fresh
   front, no prior L1 form for the FE-collection schedule). L0 evidence on-disk-verified:
   `ConstructFECollections` body `palace/fem/multigrid.hpp:22-73` (signature `:23-26`; pmin order
   floor `:30-34`; basis selection `:35-39`; family arity-3/4 ctor branch `:46-55`; LINEAR/LOG
   coarsening schedule `:60-68`; finest↔coarsest reverse `:70`). NOTE: the c064 plan/D1 cited
   `:22-75`; the on-disk closing brace is at **73**, not 75 — codemap +1-class drift; **`:22-73` is
   authoritative**.

**D3 — `fe-collection-construction-rotation` L1>L0 (abstractor, IF D2 warrants):**
1. File existence — `ls book/src/L1-L0/fe-collection-construction-rotation.md` →
   `No such file or directory` (ABSENT); `fe-collection-schedule-rotation.md` also ABSENT.
2. Maturity — N/A (absent).
3. OQ-ledger — no closed/resolved disposition (new theme for a new operator).
4. Structural block — gated on D2's warrant verdict (if D2 folds `fe_collection` as a variant axis
   rather than a standalone entry, D3 is a no-op and the L1>L0 is not authored — see D3 rationale).
   Open-by-construction otherwise.

**D4 — count-owner / cohort-header refresh (layer-intro-author):** open by construction (it
registers whatever D2 lands; trigger-gated on the D2 warrant outcome).

## Dispatches

**D1 — (`lifter`) opaque-parameter re-anchor: replace-and-propagate `fe_space` cross-refs**
- **scope:** In-place re-anchor of the FE-space-opaque parameters in the 4 firm consumer entries to
  live cross-refs to the now-firm `fe_space`. Edit `book/src/L1/fe_assemble.md` (the `space:
  FiniteElementSpace[N]` parameter `:60`/`:67` and the `A(space, ·)` opaque-map references gain
  `[`fe_space`](./fe_space.md)` links), `book/src/L1/weak_form_term.md` (the `A(space, ·)` references),
  `book/src/L1/eliminate_essential_bc.md` (`dofs: DofSet[N]` `:56`/`:67` — note its `N` is
  `space.GetTrueVSize()`; cross-ref `fe_space` for `N`, and note `DofSet[N]`'s extraction is the
  deferred `essential_dofs` sibling — plain-text forward-ref, NOT a live link, since `essential_dofs`
  is not on disk), `book/src/L1/eliminate_rhs.md` (the essential gather/scatter `DofSet[N]` framing).
  Surgical — re-anchor bare typed names to live links; do NOT alter the operators' semantics, laws,
  or signatures. Per the c064 D1 §4 opaque-parameter inventory + the `L1/index.md:94` forward-look.
  Each edited entry stays `firm` (a cross-ref firming is not a status change). MPI/`Par*` out-of-scope
  (the space is read single-rank). This is the REDIRECT's replace-and-propagate enactment.
- **deps:** none (D1 reads `fe_space.md`, already firm on disk from c064; independent of D2/D3/D4).
- **rationale:** HIGH fan-out — completes the front-opening's downstream value; de-opaques the entire
  assembled-operator cohort onto its freshly-lifted substrate. Serves the OQ
  `fe-space-opaque-parameter-reanchor-now-unblocked` (c064 D2, TRACTABLE) + the c064 D1 §4
  forward-look + the `integrator-signals` cycle-064 §Suggested-next-dispatches ("re-anchor
  `fe_assemble`/`weak_form_term`/`eliminate_essential_bc`/`eliminate_rhs` to firm `fe_space`;
  replace-and-propagate; now unblocked").

**D2 — (`harvester`) `fe_collection` WARRANT-FIRST harvest**
- **scope:** Author `book/src/L1/fe_collection.md` IF warranted. WARRANT-FIRST per the REDIRECT
  anti-mirror discipline + the c064 D1 §3 granularity verdict: the harvester FIRST judges whether
  `ConstructFECollections` is a genuine concise L1 operator with self-standing laws, OR whether it
  folds as `fe_space`'s collection-input variant-axis note. The likely-YES axis (the order-*schedule*
  is genuinely-distinct list-producing vocabulary): the family-dependent `pmin` order floor
  (`palace/fem/multigrid.hpp:30-34`), the GaussLobatto/Legendre + LOR-IntegratedGLL basis selection
  (`:35-39`), the family arity-3 vs arity-4 ctor branch (ND/RT take `(p,dim,b1,b2)`, H1/L2 take
  `(p,dim,b1)`, `:46-55`), the LINEAR/LOGARITHMIC order-coarsening schedule (`:60-68`), and the
  finest↔coarsest `std::reverse` (`:70`) — a `(p, dim, mg_max_levels, coarsening, family) ->
  [FECollection]` schedule. Candidate signature: `fe_collection :: (p: Int, dim: Int, mg_levels: Int,
  coarsening: Coarsening, family: DeRhamFamily) -> [FECollection]`. If warranted: full firm L1 entry
  with the order-schedule laws (pmin floor, the per-coarsening order sequence, the basis-type
  selection as a variant axis) + register in `L1/index.md` dep-map (own ROW) + §"Firm (FE-space
  sub-spine)" own BULLET + `SUMMARY.md`. If NOT warranted (the schedule has no laws beyond
  `fe_space`'s collection-input): record the no-entry verdict, refine the `L1/index.md:88` rough-in
  sibling line to "folded as `fe_space` variant axis," and emit NO chapter (BOTH outcomes VALID per
  the REDIRECT). On-disk body authoritative `:22-73` (codemap drifted to `:75`). `Par*`/MPI
  out-of-scope. The de-Rham family axis (H1/ND/RT/L2) is the SAME axis `fe_space` already carries —
  cross-ref it, do NOT re-mint (anti-duplication).
- **deps:** none for the warrant analysis + chapter (D2 reads `fe_space.md` + the L0 source, both on
  disk). D2 owns its own dep-map ROW + §"Firm (FE-space sub-spine)" BULLET (anchor-distinct,
  parallel-safe — NOT deferred); D4 owns ONLY the consolidated count tally + cohort-header count
  prose (see Overlap analysis + the dual-registration partition below).
- **rationale:** MEDIUM fan-out — the #2 FE-space sub-spine pick (`fe-space-sub-spine-backlog-pick-list`,
  c064 D1); feeds `fe_space` (the collection is the 2nd ctor argument) and the multigrid hierarchy
  (`fe_space_hierarchy`, pick #4). Warrant-first honors the REDIRECT's "a degenerate mirror is NOT a
  layer" — the harvester is licensed to decline.

**D3 — (`abstractor`) `fe-collection-construction-rotation` L1>L0 (GATED on D2 warrant=YES)**
- **scope:** IF D2 warrants a standalone `fe_collection` entry, author
  `book/src/L1-L0/fe-collection-construction-rotation.md` (canonical slug — D2/D3 coordinate; D2's
  `fe_collection` is the LHS forward-reference). The L1>L0 theme narrates how the L1
  `(p,dim,levels,coarsening,family) -> [FECollection]` schedule lowers into the L0
  `ConstructFECollections` template body (`palace/fem/multigrid.hpp:22-73`): the loop building the
  per-level collection (`:44-69`), the pmin termination (`:56-59`), the coarsening-policy branch
  (`:60-68`), the reverse (`:70`). Lowering-is-a-translation per the REDIRECT (NOT a 1:1 rename — the
  L1 schedule abstraction hides the template-instantiation + the `MFEM_VERIFY`/`MFEM_CONTRACT_VAR`
  machinery; if the lowering is degenerate identity-in-named-terms, that is a SMELL → record it as a
  thin in-line note in `fe_collection.md`, NOT a mirrored theme). Register in `L1-L0/index.md` theme
  table (own ROW) + `SUMMARY.md`. The LHS live-links D2's `fe_collection` (`../L1/fe_collection.md`).
- **deps:** **D2** (D3 is authored ONLY if D2's warrant verdict is YES; the LHS `fe_collection` slug
  must exist for the live link to resolve — wave-2). If D2 declines, D3 is a no-op (not dispatched /
  records "no theme — `fe_collection` folded as variant axis").
- **rationale:** MEDIUM — completes the `fe_collection` L1>L0 edge if the operator warrants. Honors
  the floor-landing-implies-same-cycle-adjacent-entry-reanchor discipline (the new operator + its
  lowering land coupled, no cross-cycle stale-assertion window).

**D4 — (`layer-intro-author`) FE-space sub-spine count-owner + cohort-header refresh**
- **scope:** SOLE count-owner this cycle. IF D2 lands a firm `fe_collection`: bump the
  `book/src/L1/index.md` §"Firm (FE-space sub-spine)" header count 1→2 + the L1 firm grand-total prose
  (`:31` "FE-space sub-spine adds **1**" → **2**; grand total 32→33) + the §Vocabulary-cohort prose,
  computing the count by reading each linked chapter's `## Status` line (NOT the index cells — the
  c057-meta count-owner anti-drift guard). IF D2 declines (no firm `fe_collection`): refresh ONLY the
  `:88` rough-in sibling line to the folded-as-variant-axis disposition (no count change). D4 owns
  ONLY the consolidated tally + cohort-header count prose + the growth-log line; D2 owns its own
  dep-map ROW + cohort BULLET. The status-flip-owns-its-index-cell discipline applies (no stale cell).
- **deps:** **D2** (D4 registers D2's outcome — wave-2). Trigger-gated on the D2 warrant verdict.
- **rationale:** LOW (hygiene; keeps the L1 index narrative honest + self-summing). The count-owner
  discipline (count from `## Status` lines, single tally owner) per the c057-meta guard.

## Overlap analysis

- **D1 ↔ D2:** D1 re-anchors `fe_assemble`/`weak_form_term`/`eliminate_essential_bc`/`eliminate_rhs`
  to `fe_space`; D2 authors `fe_collection` + touches `L1/index.md`. D1 does NOT touch `L1/index.md`
  (it edits the 4 operator entry bodies) and does NOT touch `fe_collection.md` (absent). D2 does NOT
  touch the 4 re-anchored entries. **Non-overlapping → PARALLEL.** (D2 may cross-ref `fe_space`'s
  de-Rham axis, same as D1 cross-refs `fe_space` — but they edit disjoint files; `fe_space.md` itself
  is READ by both, written by neither.)
- **D1 ↔ D3/D4:** D3 writes `L1-L0/fe-collection-construction-rotation.md` + `L1-L0/index.md`; D4
  writes `L1/index.md` count prose. D1 touches none of these. **Non-overlapping → PARALLEL** (modulo
  D3/D4's wave-2 dep on D2).
- **D2 ↔ D3:** D3's LHS live-links D2's `fe_collection.md`; forward-reference dependency → D3 in a
  LATER wave so the per-report integrator wires a live link. **Sequential (forward-ref ordering).**
  Canonical slug coordination: D2 authors `book/src/L1/fe_collection.md`; D3 forward-references it and
  authors `book/src/L1-L0/fe-collection-construction-rotation.md` (canonical slug — stated in BOTH D2
  and D3 scopes per the `cross-report-forward-reference-slug-divergence` convention).
- **D2 ↔ D4:** BOTH touch `book/src/L1/index.md`, but on ANCHOR-DISTINCT regions per the
  dual-registration partition: **D2 owns** (1) its own dep-map TABLE ROW AND (2) its own §"Firm
  (FE-space sub-spine)" cohort BULLET (anchor-distinct, parallel-safe, NOT deferred); **D4
  (count-owner) owns ONLY** (3) the consolidated tally (the §"Firm" header count "1"→"2" + the `:31`
  grand-total prose + the growth-log line). D2 DEFERS the tally to D4 and adds its own ROW + BULLET.
  Sequential by forward-ref ordering (D4 registers D2's landed outcome) → D4 in wave-2 after D2.
- **D3 ↔ D4:** D3 writes `L1-L0/index.md` + the theme file; D4 writes `L1/index.md` count prose.
  Disjoint files. **Non-overlapping → PARALLEL** within wave-2.

## Sequencing schedule

- **Wave 1 (parallel):** **D1** (re-anchor — independent, reads firm `fe_space.md`), **D2**
  (`fe_collection` warrant-first harvest — independent, reads firm `fe_space.md` + L0 source). These
  two touch disjoint files and are fully parallel.
- **Wave 2 (parallel, after D2's report lands):** **D3** (L1>L0 theme — forward-references D2's
  `fe_collection` slug; authored only if D2 warrants YES), **D4** (count-owner refresh — registers
  D2's outcome). D3 and D4 touch disjoint files (`L1-L0/*` vs `L1/index.md` count prose). Both gated
  on D2's warrant verdict: if D2 declines, D3 is a no-op and D4 does the rough-in-line-only refresh.

One `integrator-finalize` runs once at cycle end (rebuild + commit + push); the waves are
dispatch/forward-reference ordering, not multiple finalizes.

## Open questions / caveats

- **`fe_collection` warrant is a genuine fork, not a foregone conclusion.** I lean YES (the
  order-schedule has self-standing structure — pmin floor, basis selection, coarsening policy, the
  list-producing reverse), but the harvester (D2) makes the call. If D2 declines (the schedule is
  just `fe_space`'s collection-input with no independent laws), D3/D4 degrade gracefully (D3 no-op,
  D4 rough-in-line refresh) and the cycle lands D1's re-anchor + a variant-axis disposition — still a
  clean cycle. This is the REDIRECT's "a degenerate mirror is NOT a layer" discipline working as
  intended.
- **codemap ±1 drift confirmed this batch.** The c064 plan cited `ConstructFECollections` at
  `:22-75`; the on-disk closing brace is at line **73**. I verified ALL multigrid.hpp ranges on disk
  and cite `:22-73`. The dispatch scopes carry on-disk ranges. The harvester/abstractor should
  re-confirm on disk at authoring (source-of-truth rule), NOT trust codemap line numbers for tight
  ranges. This recurs (the c064 finalize flagged it for the batch-20 meta-phase) — flagging here so
  the batch-20 meta-phase (after c066) weighs whether the MCP-first localization path needs a
  codified "verify ranges on disk" amendment for `.hpp` brace/signature boundaries.
- **`essential_dofs` deferred, but its `DofSet[N]` is touched by D1's re-anchor.** D1 re-anchors
  `eliminate_essential_bc`/`eliminate_rhs`'s `DofSet[N]` to `fe_space`'s `N` and notes (plain-text,
  NOT a live link) that the dof-set's *extraction* is the deferred `essential_dofs` sibling. When
  `essential_dofs` is later harvested (c066 or batch-21), that plain-text forward-ref upgrades to a
  live link. The `AttrToMarker` def is at `palace/utils/geodata.hpp:83-95` (two overloads) +
  `GetEssentialTrueDofs` at `multigrid.hpp:99-100,109-110,120-121` — pre-localized here for the
  future `essential_dofs` harvest so it skips the localization loop.
- **No role-spec / agent-def change implied** — this is a forward-frontier cycle; no session restart
  needed (consistent with the batch-19 meta-phase's no-restart-before-c064 disposition).
- **Plan-file update:** I am appending a one-line note to `scaffolding/priorities.md` marking the
  c064 active-head item-1 FE-space sub-spine picks as DISPATCHED-c065 (D1 re-anchor + D2 `fe_collection`
  warrant-first), with `essential_dofs`/`fe_space_hierarchy` staying deferred. No batch-level intake
  migration (that is meta-phase's pass).

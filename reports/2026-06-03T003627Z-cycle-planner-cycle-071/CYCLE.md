---
agent: cycle-planner
invoked_at: 2026-06-03T003627Z
scope: cycle-071 dispatch plan
status: pending
---

# Cycle 071 dispatch plan

## Goals selected this cycle

Cycle-071 is the **directive-3 mdBook structural-reorg wave** — the one dedicated, dominant structural pass the batch-21 meta-phase sequenced as its own forward-frontier-free wave (active head #2 `directive-3-mdbook-reorg-wave`). It regroups each layer Part's flat `SUMMARY.md` chapter list into by-kind nested sub-chapter groupings (each with an intro page) and globally alpha-sorts the dep-map / list-of-API tables (alpha-within-each-kind-grouping). I am firing it THIS cycle (NOT deferring to 072) and making it the **sole substantive wave** — no forward-frontier feature-column or harvest is co-dispatched, because the reorg rewrites every Part's `SUMMARY.md` region + every index dep-map table, and a new-file feature column (active head #6) would collide on `SUMMARY.md`'s Feature-Part region + `feature/index.md` (exactly the collision the c070 planner cited when deferring the reorg out of cycle-070). The feature-surface spine scaling (magnetostatic column / lifecycle root) is sequenced for cycle-072, when the alpha-grouped SUMMARY is stable and a new-file insert lands clean into a settled structure.

The reorg is partitioned across **6 parallel `layer-intro-author` dispatches by disjoint Part-region + index ownership** (276 chapter lines across 16 Parts is too much for one dispatch; each dispatch owns distinct `index.md` files + a disjoint contiguous `SUMMARY.md` Part-block region). The shared file is `SUMMARY.md`, but each dispatch edits a **disjoint `# Part` block** of it — parallel-safe per the conflict-tolerance philosophy (the serial per-report integrator re-reads disk before each Part-region edit; distinct Part blocks are non-overlapping regions, the canonical "distinct rows / distinct regions of a shared structural file" parallel case).

## Deliverable-presence verification

This is a **structural-reorg cycle**, not a new-authoring cycle — the deliverable is "the existing flat SUMMARY/tables are regrouped + alpha-sorted," so the presence check verifies the targets EXIST-and-are-CURRENTLY-FLAT/UNSORTED (the inverse of the new-authoring ABSENT check). Inline evidence:

- **SUMMARY.md is flat (no nested sub-chapter groupings) — reorg genuinely OPEN.** `grep -nE "^  - \[" book/src/SUMMARY.md` (2-space-indented nested entries) returns the chapter lines BUT they sit under flat `# Part` headers with no per-kind intro sub-pages. Confirmed by reading lines 12-64: the `# L4` / `# L3` Parts are flat `- [chapter](...)` lists with NO nested `- [Kind group](...)` + indented children. The L4 list is NOT alpha-sorted (`assemble_frequency_operator`, `krylov-step`, `inner_product`, `iterate-while`, ... — chronological-tail order with `frequency_sweep` appended last at :28). The L3 list is NOT alpha-sorted (`krylov-step`, `apply_linop`, `assemble-diagonal`, `axpy`, ... mixed). → reorg target present-and-flat-and-unsorted. PASS (open).
- **Per-Part chapter counts (partition basis), from `awk` over SUMMARY.md:** Methodology 2, Feature 4, L4 16, L4>L3 11, L3 22, L3>L2 7, L2 23, L2>L1 12, L1 37, L1>L0 38, L0 23, Phase-1 10, Concepts 46, Design 2, Meta-Reviews 23. → 16 Parts, 276 chapter lines total. PASS (scale confirmed; partition is across these).
- **The alpha-insert CONVENTION is already codified** (batch-21 meta decision 3b — into `integrator-per-report.md` / `integrator-finalize.md` / `layer-intro-author.md`), so the c070 new entries are already alpha-PLACED within their cohort; the residual is the ONE-TIME bulk regroup + global re-sort of the pre-convention tail. Cited gate: integrator-signals c070 ⚠ item (iv) "the SUMMARY + L4/L4-L3/index dep-map rows remain in a TRANSITIONAL mixed alpha/chronological state ... pending this reorg." → reorg is the open one-time pass, NOT re-doing per-entry inserts. PASS (structurally open, not discharged).
- **STOP-PROPOSING NEGATIVE LIST check:** no dispatch this cycle proposes any listed slug (`lu_solve`/`back_solve`/`ls-update-column`/4 NLEPS atoms/`map_solve` shared-generalized/`L2/fe_assemble`/`L2/fold_solve`/`weak_form_term` L2 floor/`L3/solve_family`) — the reorg authors NO new operator/theme entries, only group-intro pages + table re-sorts. PASS (negative-list-clear by construction).
- **Small-Part over-structuring guard (directive note):** Methodology (2 chapters), Feature (4 chapters, will grow), Design (2 chapters) get **NO by-kind nesting** this cycle — too few chapters to warrant sub-grouping. Confirmed counts above. The dispatches owning these Parts do alpha-ordering only, no group intros.

(Deliverable-presence procedure SKIP-justification for the standard ABSENT check: this is a reorg of EXISTING structure, not new-slug authoring — the four-step ABSENT/maturity/OQ-RESOLVED/structural-block sequence is replaced by the present-and-flat verification above, which is its reorg-cycle analog. No dispatch resolves to a new `book/src/<layer>/<slug>.md` authoring target.)

## Dispatches

All 6 are `layer-intro-author` (the directive-3-designated executor: authors group-intro pages + maintains alpha ordering of dep-map/API tables + places SUMMARY entries inside kind groupings). Partitioned by disjoint Part-region + index-file ownership.

- **D1 — `layer-intro-author`**
  - **scope:** Directive-3 reorg of the **L4 + L4>L3 Parts**. In `book/src/SUMMARY.md` `# L4` block (:12-28) and `# L4 > L3` block (:30-41): group `# L4` chapters by kind (combinators vs named-verbs vs solver-caps vs black-box-primitives — use the existing L4/index §Vocabulary-cohort prose as the structural cohort source; if L4's 16 chapters fall naturally into ≤2 kinds, a single flat alpha-sorted list with NO nesting is acceptable per the small-Part guard — author judges); author a per-group intro page (`book/src/L4/<group>-intro.md`) ONLY for groups that warrant it; alpha-sort within each group. Same for `# L4 > L3` (11 dissolution themes — likely one flat alpha-sorted "lowering themes" group). Alpha-re-sort the dep-map / list-of-API tables in `book/src/L4/index.md` and `book/src/L4-L3/index.md`. Owns ONLY the L4 + L4-L3 index files + the L4 + L4-L3 SUMMARY Part-blocks.
  - **deps:** none
  - **rationale:** active head #2 `directive-3-mdbook-reorg-wave`; the L4 list is the most-visibly-unsorted (chronological `frequency_sweep`-appended tail) and is the outward-backend-lowering feature surface, so its navigation matters most.

- **D2 — `layer-intro-author`**
  - **scope:** Directive-3 reorg of the **L3 + L3>L2 Parts**. `# L3` block (:43-64, 22 chapters) + `# L3 > L2` block (:66-?, 7 chapters). Group `# L3` by the existing §Vocabulary-cohort kinds (BLAS-1 / elementwise / smoother / solver caps / projector — from L3/index prose); author per-group intro pages for warranted groups; alpha-within-group. `# L3>L2` (7 themes) likely one flat alpha-sorted group. Alpha-re-sort `book/src/L3/index.md` + `book/src/L3-L2/index.md` dep-map/API tables. Owns ONLY L3 + L3-L2 index files + their SUMMARY Part-blocks.
  - **deps:** none
  - **rationale:** active head #2; L3 (22 chapters) is the second-largest layer Part and has rich existing cohort prose to make structural.

- **D3 — `layer-intro-author`**
  - **scope:** Directive-3 reorg of the **L2 + L2>L1 Parts**. `# L2` block (23 chapters) + `# L2 > L1` block (12 chapters). Group `# L2` by §Vocabulary-cohort kind (folds / named-compositions / BLAS-1 floor / etc. from L2/index prose); per-group intros for warranted groups; alpha-within-group. `# L2>L1` flat alpha-sorted. Alpha-re-sort `book/src/L2/index.md` + `book/src/L2-L1/index.md`. Owns ONLY L2 + L2-L1 index files + their SUMMARY Part-blocks.
  - **deps:** none
  - **rationale:** active head #2.

- **D4 — `layer-intro-author`**
  - **scope:** Directive-3 reorg of the **L1 + L1>L0 Parts** (the two LARGEST: 37 + 38 chapters). `# L1` block — group by the documented §Vocabulary-cohort kinds (BLAS-1 / elementwise / smoother / solver caps / FE-assembly sub-spine / FE-space sub-spine / obstruction stubs — these are the directive's named example groupings, explicitly cited in the mdbook-subchapter memory note); author per-group intro pages; alpha-within-group. `# L1>L0` (38 lowering themes) — group by theme-kind (mutation-rotation / construction-rotation / obstruction) if cohorts exist, else flat alpha. Alpha-re-sort `book/src/L1/index.md` + `book/src/L1-L0/index.md` dep-map/API tables. Owns ONLY L1 + L1-L0 index files + their SUMMARY Part-blocks.
  - **deps:** none
  - **rationale:** active head #2; L1 is the largest layer with the most-developed §Vocabulary-cohort prose (7 named cohorts incl. the two FE sub-spines) — the highest-value by-kind regrouping. This is the heaviest single dispatch; isolating it keeps the others light.

- **D5 — `layer-intro-author`**
  - **scope:** Directive-3 reorg of the **L0 + Phase-1-corpus Parts**. `# L0` block (23 chapters) — group by source-area kind if cohorts exist (linalg / fem / drivers / reference-notes), else flat alpha; per-group intros only where warranted. `# Phase 1 corpus` (10 slices) — flat alpha-sorted (raw-material list, no kind grouping needed). Alpha-re-sort `book/src/L0/index.md` (if it carries a dep-map/API table). Owns ONLY L0 + Phase-1 index/SUMMARY regions.
  - **deps:** none
  - **rationale:** active head #2.

- **D6 — `layer-intro-author`**
  - **scope:** Directive-3 reorg of the **Concepts + Meta-Reviews + Methodology + Feature + Design Parts** (the reference + small Parts). `# Concepts` (46 chapters — the largest flat list) → **alpha-sort only** (a flat shared-library reference list; NO by-kind nesting unless the author finds an obvious natural split, default flat-alpha). `# Meta-Reviews` (23) → alpha/chronological-sort per existing convention (these are dated records — author judges alpha-by-cycle-id vs keep-chronological; default keep existing order, only fix if clearly mis-sorted). `# Methodology` (2), `# Feature surfaces` (4), `# Design Artifacts` (2) → **NO by-kind nesting (small-Part guard); alpha-order entries only** (Feature: keep the deliberate within-column L4→L1→L0 level ordering per integrator-signals c070 ⚠ item (ii) — the level sequence is NOT alphabetized; only multiple feature COLUMNS would alpha-sort, and there is only one column [electrostatic] so far → leave as-is). Owns ONLY these 5 Parts' SUMMARY regions + any Concepts index/API table.
  - **deps:** none
  - **rationale:** active head #2; bundles the reference + small Parts (mostly alpha-only, light work) into one dispatch. Carries the explicit "do NOT alphabetize the Feature within-column level ordering" + "do NOT over-structure the 2-chapter Methodology/Design Parts" guards.

## Overlap analysis

Pairwise (all 6 are `layer-intro-author` doing the reorg; the question is shared-region collision):

- **Shared file across ALL six: `book/src/SUMMARY.md`.** Each dispatch edits a **disjoint contiguous `# Part` block** of it:
  - D1 → `# L4` (:12-28) + `# L4 > L3` (:30-41)
  - D2 → `# L3` (:43-64) + `# L3 > L2` (:66-75)
  - D3 → `# L2` (:76-100) + `# L2 > L1` (:101-114)
  - D4 → `# L1` (:115-153) + `# L1 > L0` (:154-193)
  - D5 → `# L0` (:194-217) + `# Phase 1 corpus` (:218-228)
  - D6 → `# Concepts` (:229-276) + `# Meta-Reviews` (:280+) + `# Methodology` (:4-6) + `# Feature surfaces` (:7-11) + `# Design Artifacts` (:277-279)
  These are **non-overlapping line regions** of `SUMMARY.md` — distinct `# Part` blocks, no shared row. Per the conflict-tolerance philosophy + the "distinct regions of a shared structural file are parallel-safe" precedent (the cycle-019/020 SUMMARY multi-de-stub + multi-Part-insert cases, where serial per-report integrators re-read disk and matched disjoint `[old]` anchors verbatim), these are **NOT overlapping at the operational level → PARALLEL**. NOTE: D6's regions are non-contiguous (Methodology/Feature at file-top :4-11, Design/Concepts/Meta-Reviews at file-tail) — still disjoint from D1-D5's blocks; the integrator re-reads disk before each. The small line-region adjacency at Part-boundaries (e.g. D5's `# Phase 1` ends at :228, D6's `# Concepts` starts at :229) is a benign adjacency, not a shared row — if a boundary edit mildly conflicts, the integrator's serial re-read resolves it (false-parallel corrected cheaply, the preferred error per the philosophy).
- **Index files: fully disjoint, zero overlap.** D1 owns L4/index + L4-L3/index; D2 owns L3/index + L3-L2/index; D3 owns L2/index + L2-L1/index; D4 owns L1/index + L1-L0/index; D5 owns L0/index (+ Phase-1 has no index table); D6 owns Concepts index (if any). No two dispatches touch the same `index.md`. → PARALLEL.
- **Group-intro pages: disjoint by construction.** Each dispatch authors NEW per-group intro pages only under ITS owned Parts (`book/src/L4/<group>-intro.md`, `book/src/L1/<group>-intro.md`, etc.) — distinct new files per Part, no name collision across dispatches. → PARALLEL.
- **No operator/theme BODY is touched** by any dispatch (reorg = SUMMARY grouping + index table sort + new intro pages only) — so the "two dispatches rewrite the same theme body / modify the same operator entry" sequential trigger does NOT fire for any pair.

**Conclusion: all 6 dispatches are PARALLEL (one wave).** The only shared file is `SUMMARY.md`, edited in disjoint Part-block regions — the canonical parallel-safe structural-append/region-edit case the serial per-report integrator handles by re-reading disk. No index-file or body overlap. Per the conflict-tolerance philosophy, when in doubt mark PARALLEL; here there is no genuine same-region/same-body conflict.

## Sequencing schedule

- **Wave 1 (all parallel): D1, D2, D3, D4, D5, D6.** All six reorg dispatches fire together. No forward-reference ordering exists (no dispatch references another's not-yet-landed slug — group-intro pages are self-contained within each Part; the reorg does not create cross-Part live-links to sibling-dispatch outputs). The serial per-report integrator applies them one at a time (artifact writes serialize naturally), each re-reading `SUMMARY.md` from disk before editing its disjoint Part-block. ONE `integrator-finalize` at cycle-end rebuilds the book (validates the regrouped SUMMARY renders + `linkcheck2` resolves all new intro-page links) + commits.

Single wave; no wave-2.

## Notes for the integrator / count-ownership

- **No consolidated-tally count-owner partition needed this cycle.** No dispatch lands a new operator/theme into a shared layer-index running count — the reorg sorts/regroups existing rows, it does not add cohort members. The `firm`/`partial-obstruction` running counts in each index are TOUCHED only by the dispatch that owns that index (D1 owns L4 count, D2 owns L3 count, etc.) — single-owner-per-index by construction, no two parallel writers into one tally. (The dual-registration row+bullet+tally partition convention does not bind here — nothing is registered.)
- **Each dispatch must PRESERVE every existing chapter link** (no chapter dropped/renamed in the regroup — only re-ordered + nested + intro-pages-added). The `integrator-finalize` build-check (`cargo make book` + `linkcheck2`) is the safety net; any dropped chapter surfaces as a dead link.
- **Feature within-column level ordering is NOT alphabetized** (D6) — `electrostatic.L4` → `electrostatic.L1` → `electrostatic.L0` is the deliberate high→low level sequence (integrator-signals c070 ⚠ item (ii) / OQ `feature-surface-part-path-layout-and-within-column-level-ordering-ratification`, a standing batch-22-meta item). D6 leaves the Feature Part's level ordering as-is.

## Open questions / caveats

- **Fire-now-vs-defer decision (recorded):** I fired the reorg THIS cycle (071) as the sole/dominant structural wave and deferred feature-spine scaling to 072. Rationale: the reorg rewrites every Part's SUMMARY region + index tables; co-dispatching a magnetostatic feature column (new files + Feature-Part SUMMARY inserts + `feature/index.md` edit) would collide on the very Feature-Part region D6 is restructuring. Isolating the reorg gives the cleanest structural pass and lets 072's feature column land into a settled alpha-grouped SUMMARY. This matches the batch-21 meta decision 5 ("its OWN wave, NOT bundled with a forward-frontier cycle") and the c070 planner's deferral rationale.
- **L4 by-kind nesting may be a judgment call** — L4's 16 chapters may not split cleanly into ≥2 kind-cohorts worth nesting (the L4 layer is "vocabulary not architecture" — it may read best as one flat alpha list). I instructed D1 to use author judgment (flat-alpha acceptable if no natural ≥2-kind split), honoring the small-Part over-structuring guard at the per-Part-cohort granularity. Same latitude given to D5 (L0) and D6 (Concepts/Meta-Reviews).
- **Batch-22 meta-phase items left untouched (correctly):** the two standing OQs `feature-surface-kind-adapted-check-codification` + `feature-surface-part-path-layout-and-within-column-level-ordering-ratification` (integrator-signals c070 ⚠ items (i)/(ii)) are meta-phase work (fires after 072), NOT cycle-071 dispatch work — left for the meta-phase. The directive-3 ROLE-SPEC codification + the feature-surface-kind codification + the goal-flow refresh are also meta-phase (after 072). This cycle enacts only the ALREADY-codified directive-3 convention's one-time bulk reorg.
- **Feature-spine 072 pre-stage (advisory for next planner):** I verified the cycle-072 feature picks are ready — `magnetostaticsolver.{cpp,hpp}` confirmed via codemap (`MagnetostaticSolver::Solve` at `magnetostaticsolver.cpp:22-108`, `PostprocessTerminals` at `:110+`, inductance/B-weighted-gram reduction at `:39/:102-105/:115-160`); the constituent vocabulary it composes is the SAME on-disk firm set the electrostatic exemplar used (`L4/fe_assemble`, `L4/solve_family` [fixed-operator corner, explicitly named at `solve_family.md:137` as the magnetostatic sibling], `L4/ksp_solve`, `L1/matrix-weighted-norm`, `L1/bilinear-form`). The lifecycle-root alternative is also ready (`main` at `main.cpp:158`, `BaseSolver::SolveEstimateMarkRefine` at `basesolver.cpp:153-276`). Magnetostatic is the lower-risk 2nd exemplar (mirrors electrostatic's pattern, stress-tests the kind's adapted critic checks before the meta-phase codifies them); the lifecycle root is the higher-fan-out pick (the spine ROOT all 5 drivers hang off). The c072 planner picks by fan-out — I lean magnetostatic-first (exercise the kind a 2nd time before codification, per integrator-signals c070 suggested-next), lifecycle-root close behind.
- **No escalating actionable friction this cycle.** The only `escalating`-status friction-ledger pattern is the long-standing benign `skill-uptake-survey` named-by-slug telemetry gap (no-go-confirmed across batches 3-6, citation arm mechanized by `citecheck`) — not actionable, no plan candidate warranted. The `codemap-read-range-plus-one-drift-on-brace-boundary` pattern held at recurrence-6 last batch (no new drift); not relevant this cycle (no new source citations authored — reorg touches no L0 anchors).

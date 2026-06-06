---
agent: cycle-planner
invoked_at: 2026-06-06T165604Z
scope: cycle-112 dispatch plan (OPENER of meta-batch-36 — cycles 112/113/114; batch-36 meta-phase fires after c114 finalize)
status: pending
---

# Cycle 112 dispatch plan

## Goals selected this cycle

Push the batch-36 LEAD `graded-stack-lazy-tail-typing` — the residual P1 typed-edge tail, now the only structurally-uniform P1 remainder. The clean forward-vocabulary frontier is substantially exhausted (the `promotion_frontier: 8` are all obstruction-/demand-gated; STOP-PROPOSING in force; all feature columns are off `seed`), so the measurable movement this cycle is on the **typed-edge / reachability axis**: from-scratch `edges:` blocks on the untyped L3 mid-node tail. The cheap opener pick (per the plan + `cycle-112-resume-notes.md`) is `L3/orthogonalize` + `L3/nrm2`; I extend it with a disjoint second batch of the equally-mechanical `linear_combination`-family L3 mid-nodes (`L3/scal` + `L3/linear_combination`) to collapse more of the lazy tail this cycle without forcing a single heavy wave. All four are FRONTMATTER-ONLY, faithful-edge-or-finding, low-risk. NOTE: typing `L3/orthogonalize`'s `edges:` is correct hygiene but does NOT flip its reachability — that stays the RE2 baseline-exception (no faithful reachable depender); the typing is the lazy-tail item, the reachability is the ratified exception.

## Deliverable-presence verification

Per the MANDATORY pre-dispatch four-step check (paste-inline evidence; CLAUDE.md §Discipline `verify-dispatch-scope-not-already-discharged`). The LEAD is **open by construction at the typing level** (both named files carry only legacy frontmatter, no `edges:`/`rank:` — confirmed below), but I ran the full check on all four target files.

**D1 targets — `book/src/L3/orthogonalize.md`, `book/src/L3/nrm2.md`:**

1. File existence (`ls -la`):
```
-rw-rw-r-- 1 crutcher crutcher 48537 Jun  6 03:56 book/src/L3/orthogonalize.md
-rw-rw-r-- 1 crutcher crutcher 14026 Jun  6 03:56 book/src/L3/nrm2.md
```
2. Maturity / already-discharged check — grep for the deliverable (`^edges:`/`^rank:`/`^depends-on`/`^reference:`) returns **NO matches (exit 1)**:
```
$ grep -n "^edges:\|^rank:\|^depends-on\|^reference:" book/src/L3/orthogonalize.md book/src/L3/nrm2.md ; echo "EXIT=$?"
EXIT=1
```
   Both carry ONLY legacy frontmatter (`layer:`/`operator:`/`firmness:`/`lifts_from:`/`lowers_to:`/`variant_axes:`). `L3/orthogonalize` is `firmness: partial-obstruction`; `L3/nrm2` is `firmness: firm` (consumer-stub). The typed `edges:`-block deliverable is **NOT present** → dispatch is a real no-op-free typing.
3. OQ-ledger RESOLVED-grep — the migrated OQ is OPEN (migrated to the plan, not closed):
```
scaffolding/open-questions.md (batch-35 §Migrated to the plan):
  l3-l2-reduce-orthogonalize-midnodes-lack-typed-edges-blocks (c110 D1) — MIGRATED to priorities.md item graded-stack-lazy-tail-typing
```
   (No RESOLVED/CLOSED line for this slug — it is the active LEAD.)
4. Structural-block check — NOT blocked. The faithful `depends-on` targets exist on disk: `L3/orthogonalize` depends-on `L2/orthogonalize` (firm, grounded c111) + lowers-to `L3-L2/orthogonalize-variant-split` (the cycle-044 theme, named in its own legacy `lowers_to`); `L3/nrm2` lowers-to/identity `L1/nrm2` (firm, typed `rank: firm` + `edges:` confirmed on disk) + composes `L2/inner_product` (firm, typed). The c109 `L2/krylov-step` template (block-mapping `edges:` form with `depends-on` + per-edge `kind:` qualifiers + `reference:`) is on disk and read. NOT on the STOP-PROPOSING negative list (none of `lu_solve`/`back_solve`/`ls-update-column`/`nleps_*` involved). NOT a `promotion_frontier` member.

**D2 targets — `book/src/L3/scal.md`, `book/src/L3/linear_combination.md`:**

1. File existence (whole-L3 untyped scan; both present):
```
$ for f in book/src/L3/*.md; do grep -q "^edges:" "$f" || echo "UNTYPED: $f"; done   (relevant rows)
UNTYPED: book/src/L3/linear_combination.md
UNTYPED: book/src/L3/scal.md
```
   (The full untyped L3 mid-node tail is 12 files: axpby, axpbypcz, axpy, chebyshev, eigsolve, fold_solve, krylov-step, ksp_solve, linear_combination, nrm2, orthogonalize, scal — confirming the LEAD's "structurally-uniform untyped tail" framing; this cycle takes the LEAD pair + the linear_combination-family pair, leaving the rest lazy.)
2. Maturity check — `L3/scal` is `firmness: firm`; `L3/linear_combination` is `firmness: firm`. Neither carries `edges:`/`rank:` (legacy `lowers_to`/`lifts_from`/`variant_axes` only) → typed-edge deliverable NOT present.
3. OQ-ledger — same migrated-LEAD slug (these are members of the same untyped-L3-mid-node tail; no separate RESOLVED line).
4. Structural-block check — NOT blocked. Faithful targets exist: `L3/scal` lowers-to/identity `L2/linear_combination` (its legacy `lowers_to` names exactly this — the arity-1 specialization of the firm L3/L2 `linear_combination` fold) + lifts_from `L3/linear_combination`; `L3/linear_combination` lowers-to `L2/linear_combination` (firm, cycle-018/inverted-c049) + lifts_from `L4/linear_combination` (firm, c068). NOT on STOP-PROPOSING; NOT a `promotion_frontier` member.

All four pass; framing is correct (typed-edge GROUNDING/hygiene by `layer-intro-author`, the campaign owner — NOT new operator algebra, NOT a reflexive-harvest).

## Linter baseline (live tree, this invocation — from cycle-112-resume-notes.md + c111 finalize step-5b, confirmed)

```
files=355, typed=295, untyped=60, roots=36, reachable=122, rank_violations=0,
unresolved_depends_on_targets=0, promotion_frontier=8, detritus=137
  (detritus_no_typed_edges_pre_p1_artifact=111, detritus_with_typed_edges_stronger_signal=26,
   expected_unreachable_outside_dag=44)
Firm histogram: 201.
```
Expected post-cycle deltas (predictions for the finalize step-5b re-measure): `untyped` 60 → ~56 (4 files acquire `edges:`); `rank_violations` HOLDS 0 (every authored edge is firm→firm or firm→typed-no-rank/L0-cites-evidence); `reachable` — D2's `L3/scal`/`L3/linear_combination` MAY flip reachable IF a reachable consumer already depends-on them (verify via `--show-inbound`); `L3/orthogonalize` does NOT flip (RE2 baseline-exception — gated on a future faithful reachable depender, do NOT force); `L3/nrm2` flips only if a reachable consumer carries a typed `depends-on: L3/nrm2`. The reachability movement is whatever the faithful inbound edges already support — do NOT manufacture an inbound edge to force a flip.

## Dispatches

**D1 — (`layer-intro-author`, MEDIUM, deps: none) — the LEAD opener pair: from-scratch `edges:` blocks on `L3/orthogonalize` + `L3/nrm2`.**
- scope: Author a typed `edges:` block (+ `rank:` token) FROM SCRATCH on `book/src/L3/orthogonalize.md` and `book/src/L3/nrm2.md`, mirroring the c109 `book/src/L2/krylov-step.md` template (block-mapping `edges:` form: `depends-on:` list with per-edge `- target:` / `  kind:` qualifiers for `lowers-to`; a `reference:` list). FAITHFUL-EDGE-OR-FINDING: derive every edge from the chapter's OWN prose + its existing legacy `lowers_to`/`lifts_from`/`variant_axes` — do NOT manufacture edges.
  - `L3/orthogonalize` (`firmness: partial-obstruction` — carry the rank as `partial-obstruction`, NOT firm; its §Status is `partial-obstruction` per cycle-019/022): faithful `depends-on` → `L2/orthogonalize` (the named `project ▷ subtract` composition, firm/grounded c111; its legacy `lowers_to`:6,8 + body :38,:80,:394,:532) with `kind: lowers-to` on the `L3-L2/orthogonalize-variant-split` theme (the SUBSTANTIVE loop-structure variant split — its legacy `lowers_to`:8 + body :412,:491 name exactly this cycle-044 theme); `reference:` per the body's concept links. **RE2 NOTE (carry into the dispatch):** typing this block is correct hygiene; it does NOT and must NOT flip `L3/orthogonalize` reachable — that is the ratified RE2 baseline-exception (`scaffolding/graded-stack-baseline-exceptions.md` Axis-2; no faithful reachable depender — `L4/krylov-step` composes the L2 surface directly, not the L3 iteration-view). Do NOT add a forced inbound edge to flip it.
  - `L3/nrm2` (`firmness: firm` — consumer-stub; rank firm): faithful `depends-on`/identity → `L1/nrm2` (identity-in-form lowering, its legacy `lowers_to`:6, body :28,:85; `L1/nrm2` is firm + typed on disk) — mirror the sibling `L3/dot` typed block (`depends-on: L2/inner_product`, `reference: L4/dot`); `L3/nrm2` composes through `L2/inner_product` at the diagonal (body :16-18,:103-112) as the consumer-of-the-fold (NOT a fold member — preserve the do-NOT-merge carve-out in the edge choice). `reference:` → `L4/nrm2` (its `lifts_from`:8). Do NOT force a reachability flip.
- rationale: THE LEAD (`graded-stack-lazy-tail-typing`); the migrated OQ `l3-l2-reduce-orthogonalize-midnodes-lack-typed-edges-blocks`. Collapses 2 of the untyped-L3-mid-node tail; completes the typed-DAG hygiene for the reduce/orthogonalize mid-nodes. fan-out: MEDIUM.

**D2 — (`layer-intro-author`, MEDIUM, deps: none) — the disjoint `linear_combination`-family L3 mid-node pair: from-scratch `edges:` blocks on `L3/scal` + `L3/linear_combination`.**
- scope: Same template + faithful-edge-or-finding discipline, distinct files `book/src/L3/scal.md` + `book/src/L3/linear_combination.md`.
  - `L3/scal` (`firmness: firm`; rank firm): faithful `depends-on`/identity → `L2/linear_combination` (its legacy `lowers_to`:6 names exactly "the arity-1 specialization of the firm L3/L2 `linear_combination` fold; `scal(α,x) = linear_combination [(α,x)]`") with the substantive arity-dispatch carried by the `L2-L1/linear-combination-fold-specialization` theme as a `reference` (the lowering is operator→operator per the established L2/L3 convention; the theme is a `reference` target, NOT a `depends-on lowers-to` here — `L3/scal` lowers to the L2 OP `linear_combination`, mirroring how the c108/c111 L2 ops carry `lowers-to` only at the L2>L1 edge); `reference:` → `L3/linear_combination` (its `lifts_from`:9 — the family combinator), `L1/scal`.
  - `L3/linear_combination` (`firmness: firm`; rank firm): faithful `depends-on`/identity → `L2/linear_combination` (its legacy `lowers_to`:6, firm cycle-018/inverted-c049; identity-in-form across the L3>L2 edge); `reference:` → `L4/linear_combination` (its `lifts_from`:9, firm c068), `L2-L1/linear-combination-fold-specialization`.
- rationale: extends the LEAD across the disjoint `linear_combination`-family mid-node pair (equally mechanical + faithful; closes more of the structurally-uniform untyped-L3 tail in one cycle). DISJOINT file set from D1 → safe parallel. fan-out: MEDIUM.

## Overlap analysis

- **D1 write-set:** `book/src/L3/orthogonalize.md`, `book/src/L3/nrm2.md` (frontmatter only).
- **D2 write-set:** `book/src/L3/scal.md`, `book/src/L3/linear_combination.md` (frontmatter only).
- **D1 ∩ D2 = ∅** — fully DISJOINT file sets. No shared operator entry, no shared theme body, no shared consolidated-tally (per-page frontmatter, not a cohort count → no `parallel-blind-shared-index-count-divergence` exposure; no `feature/index.md` matrix touch). No new-slug forward-reference between the two (every edge target — `L2/orthogonalize`, `L3-L2/orthogonalize-variant-split`, `L1/nrm2`, `L2/inner_product`, `L4/nrm2`, `L2/linear_combination`, `L2-L1/linear-combination-fold-specialization`, `L3/linear_combination`, `L1/scal`, `L4/linear_combination` — is an EXISTING stable on-disk slug, verified). → **PARALLEL, single wave.**
- **Contamination-friction note (`parallel-dispatch-reachability-measurement-contamination`, now ledger-and-monitor):** D1 and D2 are both `layer-intro-author` dispatches that touch reachability-relevant frontmatter. The friction is two parallel dispatches misreporting reachability via apply→lint→revert contamination on a shared working tree. MITIGATION: the file sets are fully disjoint, so each dispatch's local reachability self-measure is isolated to its own +Δ; instruct EACH producer to report ONLY its own standalone delta and to treat the authoritative cumulative as the finalize step-5b re-measure on the landed tree (the c111 discipline that HELD — recurrence-1, no recurrence-2). Per-report integrators re-isolate; finalize re-measures cumulative. This is exactly the c110/c111 two-disjoint-layer-intro-author shape that held.

## Sequencing schedule

**Wave 1 (parallel): D1, D2.** Both `layer-intro-author`, disjoint frontmatter-only file sets, no forward-reference dependency, all edge targets pre-existing slugs → no inter-dispatch ordering needed. One wave.

Pipeline after dispatch (unchanged, standard): D1/D2 → 2 critics (parallel) → repairer(s) on any warn/fail → `integrator-per-report` ×2 (serial) → ONE `integrator-finalize` (rebuild book + step-5b linter re-measure + commit + push + housekeeping). The book is NOT rebuilt between dispatches; there is exactly one finalize.

## Open questions / caveats

- **Right-sized at 2 dispatches.** The untyped L3 mid-node tail is 12 files; the redirect's guidance is "NOT a single heavy wave — let it acquire `edges:` lazily as files are next-touched." Taking the LEAD pair + one disjoint family pair (4 files) this cycle honors that (incremental, not a heavy sweep) while making measurable lazy-tail progress. The remaining 8 untyped L3 mid-nodes (`axpy`/`axpby`/`axpbypcz`/`chebyshev`/`eigsolve`/`fold_solve`/`krylov-step`/`ksp_solve`) stay lazy for subsequent cycles c113/c114 — flagging for the batch-36 active head that the L3 mid-node tail is a uniform, low-risk source of cheap typed-edge picks for the remainder of the batch.
- **No feature-surface clean pick this cycle.** All 40 `book/src/feature/*.md` files are off `seed` (grep `status: seed` → no matches), so there is no feature-column promotion with fan-out this cycle. The demand-gated `waveguide-mode` 6th output-product column + `boundary-mode` driver-leaf column stay gated (no trigger fired). The feature spine runs in parallel as a standing goal, but it offers no eligible movement here.
- **STOP-PROPOSING / promotion_frontier honored.** No `promotion_frontier: 8` member proposed (all obstruction-/demand-gated); no STOP-PROPOSING-negative-list slug proposed; no forced rectangular pull-up. The redirect's "what a solver can't cleanly say is a finding" is not in play this cycle (pure typed-edge hygiene).
- **RE2 reachability is deliberately NOT flipped.** If D1's producer finds an apparently-faithful inbound edge that would flip `L3/orthogonalize` reachable, that is a FINDING to route to the batch-36 meta-phase (it would contradict the RE2 ratification), NOT an edge to author — the §2f faithful-edge-or-finding guard. RE2's promotion condition is a future L3-consuming column, not a typing pass.
- **Latent linter-reader bug `graded-stack-lint-block-mapping-misparse-on-legacy-edge-prose-colon` (batch-34 NO-GO-pre-emptive-fix).** This cycle's typing CONVERTS 4 legacy-frontmatter files to the clean `edges:` surface form, removing the `:`-bearing legacy-edge trigger for those 4 (migration-eliminates-the-trigger, as designed). The bug stays latent on the remaining untyped tail; re-open the fix-the-reader decision only on recurrence-2.

# cycle-155 — MIDDLE 2/3 of meta-batch-51 — THE CONVERGENCE: `p1-edge-typing-true-detritus-sweep` DISCHARGED; genuine `untyped` debt → 0; the finite maintenance backlog is now EMPTY

**Batch position:** MIDDLE 2/3 of meta-batch-51 (cycles 154/155/156). The batch-51 meta-phase
fires AFTER cycle-156's finalize, aggregating all three as a SEPARATE dispatch/commit; the cycle
counter does NOT reset. This finalize ran NO meta-phase housekeeping.

**Posture:** WIND TO MAINTENANCE — the maintenance-floor steady-state. This is the CONVERGENCE
enactment: the `p1-edge-typing-true-detritus-sweep` backlog item — the LAST finite maintenance
item — is discharged. After this cycle the finite maintenance backlog is empty; only the standing
per-batch full-hygiene sweep + the per-cycle two-invariant tripwire remain.

## What landed

ONE dispatch (cycle-planner SKIPPED — the work was fully specified by the c154 (c)=0
classification):

- **(general-purpose, `c155-lint-untyped-carveout-convergence`) — 2 files.** A bounded
  `tools/graded-stack-lint` carve-out refinement + a reader-facing scheme note. Report `ready`,
  critic-verified independently (incl. a future-debt-detection probe).
  - **`tools/graded-stack-lint/graded_stack_lint.py`:** extended the outside-DAG prefix carve-out
    `OUTSIDE_DAG_PREFIXES += L0/, meta-reviews/` (L0 = ground-truth evidence leaf layer, rank
    vacuous at the base; meta-reviews = historical process records); added an exact-match set
    `OUTSIDE_DAG_EXACT = {SUMMARY, introduction, semantics/index}` for the navigational pages not
    under an outside-DAG prefix; split the `untyped` count so the headline `untyped` total counts
    genuine edge-typing debt ONLY, with the by-design pages reported separately as
    `untyped_outside_dag_by_design`.
  - **`book/src/methodology/graded-stack-scheme.md`:** added a `### The outside-DAG-by-design
    carve-out` note (the only book change) — L0-as-ground-truth-leaf + outside-DAG rationale +
    the exactness invariant.

This enacts the c154 D1 classification ((a) 35 non-DAG carve-outs + (b) 26 `L0/` ground-truth
leaves + (c) **0** genuine-untyped DAG nodes = 61): the `untyped=61` warning was DOMINATED by
legitimately-untyped-by-design pages, NOT genuine debt. With (c)=0 confirmed, the genuine
`untyped` count is **0**.

## Backlog item discharged

- **`p1-edge-typing-true-detritus-sweep` — DISCHARGED/CONVERGED.** The LAST finite maintenance
  item. Removed from the `priorities.md` batch-51 head AND the dedicated Backlog item marked
  closed. The finite maintenance backlog is now EMPTY.

## The convergence — the tripwire baseline DELIBERATELY MOVES (accounted, NOT a regression)

The step-5b graded-stack tripwire baseline moves THIS cycle by design — this is the CONVERGENCE.
The **new post-convergence baseline** (recorded going forward):

- **`untyped`: 61 → 0** — genuine edge-typing debt ELIMINATED. The steady-state tripwire now trips
  on `untyped > 0` (0 is the converged floor).
- **`untyped_outside_dag_by_design`: 61** (new key, set-equal to the old 61-untyped set, still
  visible via `--show-untyped`).
- **`expected_unreachable_outside_dag`: 54 → 106** (+52 — the carved-out L0/meta-reviews/nav nodes
  reclassified on the reachability axis; the critic confirmed 0 genuine-DAG nodes added).

**HARD INVARIANTS + key totals HELD EXACTLY:** `rank_violations 0`, `unresolved_depends_on_targets
0`, `typed 331`, `files 392`, `roots 45`, `promotion_frontier 11`, `detritus 123`, `true_detritus
51`.

## Build + gates

- `cargo make book` (mdbook html + linkcheck2): **EXIT 0**, ZERO build-repairs. The scheme-note is
  the only book change (an additive `###` subsection to an already-registered chapter — no new
  file, no SUMMARY change). Only pre-existing benign KaTeX potential-incomplete-link WARNs in
  untouched files.
- **Step-5b graded-stack per-cycle tripwire (LANDED tree):** none of the 3 block-conditions
  tripped — **(i)** no NEW `rank_violation` (held 0); **(ii)** no newly-orphaned node (reachability
  identical for genuine-DAG nodes; the +52 reclassification is the carve-out, 0 genuine-DAG nodes
  added); **(iii)** detritus escalate-guard NOT tripped (`detritus`/`true_detritus` UNCHANGED at
  123/51). The baseline MOVE (`untyped` 0, `expected_unreachable_outside_dag` 106) is the
  DELIBERATE accounted convergence, NOT a regression. Trend: `rank_violations` …→0 (c153)→0
  (c154)→0 (c155); `unresolved` HELD 0 (c123…c155).
- **Step-5c KaTeX `$`-sigil assertion: PASS** — `class="katex"` inside any `<pre>` = 0 across all
  built HTML pages.
- **Step-5d frontmatter-leak assertion: PASS** — no rendered page leaks its own frontmatter `key:`
  paragraph (grep over `book/book/html/` empty).

## Reconciliation

- **1 staging row == 1 dispatched-ready book-mutating report** — 132nd consecutive clean staging.
- retroactive-budget global = 0; per-report gates all PASS/N/A; 0 implied-component stubs; SLICE
  CORPUS: 0; NO vocabulary firm-count flip; roadmap coverage UNCHANGED (a tooling/reporting
  refinement + a methodology scheme note, NOT firm-vocabulary movement).
- The 1 consumed report's `integrated_at`/`integration_commit` touched; two-phase SHA-patch
  follows. The `tools/` change is committed alongside the scheme note (per the STAGING note).
- The slice-era `cycle-155.md` (2026-05-26 stub) was renamed to `cycle-155-slice-era.md`
  (the c123–c154 precedent), README index line re-pointed.
- NO `.claude/agents/` changes FROM THIS FINALIZE → no session restart needed before c156.

## Forward

c156 (CLOSER 3/3) is a pure CONFIRMATION cycle: confirm the convergence held (`untyped` stays 0)
under the new baseline. The batch-51 meta-phase fires after c156's finalize. The finite
maintenance backlog is empty; the §CENTRAL ASK forward direction (maintenance / downstream-burn
handoff / re-scope) remains a human decision — now in its 10th batch at in-scope steady-state
completeness. The in-scope FEATURE-SURFACE SPINE remains L4-COMPLETE; the Synthesis VIEW is
complete + correspondence-audited; deferred fronts consumer-gated; no forced rectangular pull-up;
DIRECTIVE-1 MPI/distributed stays OUT.

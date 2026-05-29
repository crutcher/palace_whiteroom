# Cycle 028 — L2>L1 firm 6→7 (+incremental-least-squares-composition-lowering, closes c027 D5 deferral) + 3 verified_against audits (normalize/back_solve/incremental-ls) + citation-hygiene residual sweep + trsv resolved-by-obstruction (l3-vocabulary-inventory-gap CLOSED) (first primary cycle of meta-batch-8)

**Date:** 2026-05-29 · **Commit:** `PATCH_AFTER_COMMIT` · **Status:** clean (7 of 7 dispatched-ready reports applied; zero deferrals; zero rejections; zero build-repairs; twenty-fourth consecutive clean split-integrator cycle)

**Batch position:** cycle-028 is the **FIRST** primary cycle of **meta-batch-8** (cycles 028/029/030). The batch-8 meta-phase fires after the cycle-030 finalize commit (3:1 cadence; cycle counter does NOT reset across batch boundaries). This `log/cycle-028.md` + the `scaffolding/integrator-signals.md` cycle-028 section OPEN the batch-8 evidence window.

(Filename note: this current-era `cycle-028.md` overwrites a frozen slice-vertical-era legacy stub of the same name — content preserved in git history; the layered-flow era progressively reclaims the `cycle-NNN.md` namespace, per the cycle-020→027 precedent.)

## Summary

A high-yield citation-hygiene + lowering-completion cycle. 7 dispatched-ready reports, all applied clean (7/7 staging rows == dispatched-ready-reports — the cycle-018 staging-completeness gap did NOT recur for the **ninth** consecutive cycle). One substantive landing (a new firm L2>L1 theme closing the carried-over c027 D5 deferral), three additive `verified_against:` lowering-verifier audits, one citation-hygiene residual sweep, and two no-mutation surveys (one resolving a long-blocked plan item by obstruction).

## Headlines

- **HEADLINE 1 — L2>L1 firm 6→7 (+`incremental-least-squares-composition-lowering`, CLOSES the c027 D5 deferral).** The GMRES/FGMRES running-QR / Givens-rotation-stream fan-down theme landed firm fresh this cycle (a NEW file — the c027 D5 draft was deferred needs-revision on an inverted coordinated-rename premise and never integrated). Narrated forward L2→L1: the firm L2 named composition `incremental-least-squares` fans down into the single L1 column-streaming leaf `ls_update_column` (opaque face) — equivalently the de-fused scalar Givens sub-step sequence `replay ▷ generate ▷ apply ▷ apply_rhs` — plus a terminal back-solve = small-dense triangular solve (the firm `back_solve` leaf, **NOT** a general `trsv`) ▷ basis reconstruction (`linear_combination`). Two parametric axes (`basis_kind∈{V,Z}` + `variant∈{real,complex}`); FIXED sub-step sequence (replay-before-generate non-commutative, load-bearing). The `ls_update_column` column-streaming leaf is **forthcoming** (not on disk) — its forward-references are correctly left **plain-text** (a live link would be a `linkcheck2` hard error); routed to a follow-on harvester via OQ `ls_update_column-column-streaming-leaf-harvest`. Sibling to `orthogonalize-composition-lowering` (the other L2 named-composition fan-down). Registered at `SUMMARY.md:57` + `L2-L1/index.md` dep-map row 20 (4-col shape). **L2-L1 cohort now 8 = 7 firm + 1 partly-constructive (`deflate-composition-lowering`).**

- **HEADLINE 2 — 3 additive `verified_against:` lowering-verifier audits, all UPHOLD firm, zero status change.**
  - `normalize-mutation-rotation` (firm L1>L0, landed c027 D1) **UPHELD firm** — 16-row `verified_against:` block (14 supports / 1 partially-supports / 1 does-not-support) + a `:811`→`:810-811` second-GMRES-path citation-range parity fix at three occurrences. The single `does-not-support` row (F1: a defined-but-uncalled fused `Normalize(comm,x,B,Bx)` at `palace/linalg/operator.hpp:377-384` contradicts the theme's "no fused B-Normalize" prose) is recorded inline but the prose CORRECTION is **routed** to a follow-up abstractor OQ `normalize_B-note-says-no-fused-B-Normalize-but-uncalled-fused-operator-exists` (substantive, exceeds the integrator mechanical bar). Firm core UNAFFECTED.
  - `back_solve` (firm L1 leaf, landed c027 D4) **UPHELD firm, fully-supported** — 18-row `verified_against:` block, all supports. Firm-on-positive-structure (syntactic-identity laws, no-dedicated-test non-gating per the `lu_solve`/`apply_linop` precedent).
  - `incremental-least-squares-composition-lowering` (the HEADLINE-1 theme) **audited firm same-cycle as its D1 landing** — 22-row `verified_against:` block (17 L0 + 5 book-internal), all supports; confirms the thinner-than-precedent firm bar D1 flagged is sound (Face 2 + back_solve + linear_combination carry the firm value).

- **HEADLINE 3 — citation-hygiene residual sweep (carried-forward c027 residuals).** `L0/linalg-operator-file.md` `:22`/`:87` Category-2→Category-1 workspace relabel (now all five workspace-category mentions read uniformly "Category 1 — operator-composition workspace", evidence-grounded in `mutable-workspace-pattern.md:128-129`) + `L2/incremental-least-squares.md:13` dropped the stale "queued" self-description qualifier (entry firm since c026). Pure prose hygiene — no operator/theme signature, decomposition, semantics, or law touched.

- **HEADLINE 4 — `trsv` L3-inventory gap RESOLVED-BY-OBSTRUCTION (harvester localization, negative finding) → `l3-vocabulary-inventory-gap` parent CLOSED.** Two exhaustive zero-hit searches (independently reproduced by the critic) confirm Palace exposes NO standalone `trsv` primitive: triangular solves are opaque-library-owned (HYPRE GS/SSOR relax-type flags + external direct-solver wrappers; `densematrix.hpp:24-36` has no triangular solve) or a block-triangular red herring. `trsv` was the LAST of four leaves of the migrated-plan-item `l3-vocabulary-inventory-gap` (gemv/ksp_solve/eigsolve done + trsv resolved-by-obstruction = all four leaves done) → **parent gap fully resolved**. Fresh actionable plan candidate routed: author the L1>L0 obstruction theme `triangular-solve-obstruction` (abstractor) giving the resolved-by-obstruction `trsv` leaf a citable home.

- **HEADLINE 5 — `matrix-weighted-norm` + `bilinear-form` test-coverage-gate survey (no-mutation, ASK-class).** Both L1 operators **STAY rough-in** (no dedicated test at the weighted entry point in the 23-file corpus; the gates need an out-of-scope Palace-source change). The `matrix-weighted-norm-mixed-element-type-variant` OQ is **NARROWED** (not closed — element-type axis now shape-witnessed by `test-orthog.cpp` four-real-dot construction; residual is the named-entry-point √+SPD-guard test). Surfaced the actionable in-scope next step: the **missing `bilinear-form-mutation-rotation` L1>L0 theme does NOT exist on disk** — routed as a fresh abstractor plan candidate (cheapest next step toward bilinear-form firmness).

## Layer-stack counts (verified on disk this cycle)

| Layer | Count |
|---|---|
| L0 | 22 chapters |
| L1 | 21 firm + 2 rough-in (test-coverage-bounded) + 6 rough-in (obstruction) |
| L1>L0 | 16 theme files (no change; 3 audited additively) |
| L2 | 9 firm + 1 partly-constructive + 0 stub |
| **L2>L1** | **8 = 7 firm + 1 partly-constructive (+1 firm this cycle)** |
| L3 | 9 firm + 2 partial-obstruction |
| L4 | 4 firm |
| Phase-1 removals | 9/10 |

## Build

`cargo make book` exit 0, **zero build-repairs**. The new theme + the 3 `verified_against:` ```yaml fences (all balanced, fence-count 2 each) + the 2 prose edits all SUMMARY-registered + link-clean. The new theme rendered to HTML; the `ls_update_column` forward-references are plain-text (no live link → no dead-link error). The only build warnings are KaTeX `Potential incomplete link` false-positives confined to `design/l4_calculus.md` math-display, NONE in a touched file.

## Gate results (safety-net)

- retroactive-budget global: **0** (well under the ≥4 block threshold)
- implied-component-stub-created: 0
- in-cycle-live-link-upgrade: 0
- SUMMARY-registration auto-fix: 0
- staging-completeness: 7/7 rows == 7 dispatched-ready reports (no gap)
- commit atomicity: single commit + push
- consumed-report frontmatter integrity: 7 `integrated_at` touches

## Routed follow-ups (for cycle-029 planner / batch-8 meta-phase)

- `back-solve-mutation-rotation` L1>L0 theme (abstractor) — the firm `back_solve` leaf has no lowering theme yet.
- `bilinear-form-mutation-rotation` L1>L0 theme (abstractor) — the missing theme HEADLINE 5 surfaced.
- `triangular-solve-obstruction` L1>L0 theme (abstractor) — citable home for the resolved-by-obstruction `trsv` leaf.
- `normalize_B` F1 fused-but-uncalled prose correction (abstractor) — rewrite "no fused B-Normalize" → "exists but uncalled" + tighten the `normalize_B` promotion gate.
- `ls_update_column-column-streaming-leaf-harvest` (harvester) — the forthcoming Face-1 column-streaming leaf.
- L2-index prose refresh — the `roadmap.md` L2>L1 lead prose was stale at "2 firm" (cycle-018 era); updated this cycle to the accurate current count with a note that the index is authoritative.

## Meta-phase-deferred actions (NOT enacted by finalize)

- Strike the plan-owned RESOLVED-c028 OQ lines in `priorities.md` (the per-report integrators recorded RESOLVED-c028 disposition sections in `open-questions.md` for the meta-phase to migrate).
- Adjudicate the skill candidate `establish-negative-finding-exhaustiveness` (filed by report-7's critic, any-agent channel).
- The leading-`"` `verified_against:` note channel-format hazard (flagged by report-5's integrator: a YAML scalar beginning with a literal double-quote needs single-quote wrapping).

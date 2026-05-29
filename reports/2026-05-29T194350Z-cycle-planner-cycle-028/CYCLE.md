---
agent: cycle-planner
invoked_at: 2026-05-29T19:43:50Z
scope: cycle-028 dispatch plan
status: pending
---

# Cycle-028 dispatch plan

**Cycle-028 is the FIRST primary cycle of meta-batch-8 (cycles 028/029/030; meta-phase fires after cycle-030 finalize).**

## Goals selected this cycle

Batch-7 closed with a single deferral (D5: the `incremental-least-squares-composition-lowering` L2>L1 theme needs the now-firm `back_solve` leaf to re-anchor its terminal-back-solve references). The planner's primary goal this cycle is to clear the deferral via the lifter re-anchor + promotion dispatch, then execute the standard batch-7-new-firm-theme audit cohort, close residual citation-hygiene gaps, and unblock the L3 trsv inventory gap (which requires L1 localization first as a blocking sub-task).

## Dispatches

1. **lifter** — `incremental-least-squares-composition-lowering-L2-L1-re-anchor-and-promote` — deps: none
   - **Scope:** Re-anchor the L2>L1 `incremental-least-squares-composition-lowering` theme's terminal-back-solve fan-down references (formerly plain-text `trsv`/`ls_update_column`, now the firm `back_solve` leaf from c027 dispatch-4). Reconcile the `trsv`↔`back_solve` naming: the theme currently forward-references a general `trsv`; dispatch-4 landed the specific `back_solve` (GMRES/FGMRES restart-correction back-solve, **NOT** a general triangular-solve). Re-point theme's terminal-back-solve refs at firm `back_solve`, reconcile the forward-reference characterization of the distinct still-un-harvested column-streaming `ls_update_column` leaf, upgrade any now-resolvable plain-text refs to live links, and promote the theme rough-in→firm. Optionally harvest the column-streaming `ls_update_column` leaf if tightening the fan-down requires it.
   - **Rationale:** HIGH fan-out — finishes the GMRES/FGMRES restart-machinery lowering chain and closes the sole batch-7 deferral. Cycle-027 D5 was `needs-revision` on premise-inversion; now that `back_solve` is firm and the naming collision resolved, the re-anchor is straightforward. Clean lifter-promotion-shaped task. Gated by c027 D4 landing.
   - **Reference:** `scaffolding/priorities.md` active head #1; OQ `incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor`.

2. **lifter** — `citation-hygiene-residual-sweep-category-and-self-description` — deps: none
   - **Scope:** Three mechanical residuals: (a) `book/src/L0/linalg-operator-file.md:22` + `:87` — Category-4→Category-1 workspace-mislabel relabel (cycle-027 D2 fixed the named sites `:33`/`:73`/`:80` + the `matrix-weighted-norm.md:9` sibling; these two out-of-named-scope sites remain); (b) `book/src/L2/incremental-least-squares.md:13` — self-description staleness ("the second **named-composition** motif; queued") despite entry being firm since c026 (cycle-027 D6 cycle-planner flagged as a drive-by observation); (c) the residual `book/src/L2/gram.md:5` "(forthcoming)" text-refresh if not already closed.
   - **Rationale:** LOW fan-out / hygiene — closes the cycle-027 residual-OQ tail. Mechanical single-file edits. Routes as lifter (plain-text property edits) or same-layer-cross-cutter (optional cross-reference refresh).
   - **Reference:** `scaffolding/priorities.md` active head #2; OQs `linalg-operator-file-category-mislabel-residual-lines-22-87`, `l2-incremental-least-squares-self-description-still-says-queued-after-firming`.

3. **lowering-verifier** — `normalize-mutation-rotation-verified-against-audit` — deps: none
   - **Scope:** Standard per-line `verified_against:` audit of the firm L1>L0 `normalize-mutation-rotation` theme (landed firm c027, dispatch-1). Cite-tightening, law-confidence re-eval, consumer-cohort completeness check. Emits the mechanically-fenced `verified_against:` YAML block per the established pattern (cycle-003 meta / CLAUDE.md Discipline: tilde-fenced ` ```yaml ... ``` ` form when appended post-text, backtick-fenced when inline).
   - **Rationale:** LOW-MEDIUM fan-out — per-line evidence census (the firm→next-cycle-audit pattern). Unblocked by c027 D1 (normalize-mutation-rotation landing firm). Standard lowering-verifier dispatch shape.
   - **Reference:** `scaffolding/priorities.md` active head #3; OQ `normalize-mutation-rotation-lowering-verifier-audit`.

4. **lowering-verifier** — `back-solve-lowering-verifier-audit` — deps: none
   - **Scope:** Standard per-line `verified_against:` audit of the firm L1 leaf `back_solve` (landed c027, dispatch-4). Cite-tightening, law-confidence re-eval against the GMRES/FGMRES restart-correction L0 loop sites. Produced as a distinct dispatch (not paired with #3) because the L1 leaf's audit is independent of the L1>L0 theme audit.
   - **Rationale:** LOW-MEDIUM fan-out — per-line evidence census. Unblocked by c027 D4. Standard auditing dispatch shape.
   - **Reference:** `scaffolding/priorities.md` active head #3; OQ `back-solve-lowering-verifier-audit`.

5. **lowering-verifier** — `incremental-least-squares-composition-lowering-verified-against-audit` — deps: dispatch 1
   - **Scope:** Standard per-line `verified_against:` audit of the L2>L1 `incremental-least-squares-composition-lowering` theme, **after dispatch-1 re-anchors and promotes it to firm**. Forward-reference on dispatch-1's promotion; once firm, the theme's per-line evidence census proceeds as with the other batch-7-new themes. If dispatch-1 optionally harvests the column-streaming `ls_update_column` leaf, auditor may include per-line audit of the leaf's new L1>L0 theme (if authored in dispatch-1).
   - **Rationale:** LOW-MEDIUM fan-out — completes the batch-7-firm-theme audit cohort. Blocked by dispatch-1 promotion (forward-reference dependency). Standard auditing dispatch shape.
   - **Reference:** `scaffolding/priorities.md` active head #3; OQ `incremental-least-squares-composition-lowering-verifier-audit`.

6. **same-layer-cross-cutter** — `matrix-weighted-norm-variant-axis-and-bilinear-form-test-coverage-gate` — deps: none
   - **Scope:** Close the paired rough-in→firm promotion gates for `matrix-weighted-norm` (L1, status: `rough-in (test-coverage-bounded)`) and `bilinear-form` (L1, status: `rough-in (test-coverage-bounded)`). Both operators' L1>L0 lowering themes are firm (c026 + c027 audit); the L1 entries themselves stay rough-in pending test-coverage re-eval. Survey the existing Palace unit-test corpus (`reference/palace/test/unit/` linalg, operator, fem integration tests) for dedicated coverage of (a) `BilinearForm` operator-application with mixed element-type inputs (norm_type + trial/test element compatibility), (b) energy-norm computation via `matrix-weighted-norm` (the Chebyshev/CG convergence-residual test sites). Emit a variant-axis-completeness survey + test-coverage summary. Route the promotion decision to the human (ask-class: if sufficient coverage is evident, the operator entries promote; if coverage is sparse, record a deferred-contingent gate).
   - **Rationale:** MEDIUM fan-out — energy-norm consumers (CG/eigenmode residual tests) gate. Paired gate (both rough-ins share the same test-coverage gating reason). Routes as `same-layer-cross-cutter` (comparing two L1 entries) + optional `lowering-verifier` (auditing the connection between rough-in L1 entry and firm L1>L0 theme).
   - **Reference:** `scaffolding/priorities.md` active head #4; OQs `matrix-weighted-norm-mixed-element-type-variant`, `bilinear-form-variant-axis-test-coverage`.

7. **harvester** — `trsv-l1-localization-and-palace-placement` — deps: none
   - **Scope:** Localize Palace's sparse-triangular-solve usage across `palace/linalg/`. The L3 trsv inventory gap is **blocked** (no firm L1 anchor). Survey whether Palace exposes a standalone `trsv` primitive or whether triangular solves appear only inside Gauss-Seidel-flavoured preconditioner internals / ILU-factorization smoothers (which `book/src/L3/index.md:7` already names as canonical L3 obstructions). Search the codebase (`palace/linalg/*.cpp`, preconditioner files, smoother implementations) for triangular-solve call sites + API patterns. Emit an L1-localization report characterizing Palace's trsv presence: (a) Is there a stand-alone `sparse_triangular_solve` API? (b) If yes, cite the source sites; if no, cite the preconditioner/smoother sites where it appears as an internal step and classify as an obstruction-theme target. **Note:** this is a localization dispatch, not an authoring dispatch. The L1 entry itself (if warranted) is a follow-on harvester; the obstruction-theme (if applicable) is an abstractor dispatch.
   - **Rationale:** MEDIUM fan-out — completes the L3 vocabulary-inventory gap. Currently blocked (no L1 anchor). This dispatch unblocks downstream work by clarifying whether `trsv` is a firm-operator candidate or an obstruction-theme target. Routes as `harvester` (L1 localization) on the Palace tree. **Per CLAUDE.md Discipline: localize via palace-codemap (list_files, search_text, get_call_sites) before reading source; verify file paths before citing in scope.**
   - **Reference:** `scaffolding/priorities.md` active head #5; OQ parent `l3-vocabulary-inventory-gap` REMAINING `trsv`.

## Overlap analysis

**Dispatch-1 and Dispatch-5 forward-reference relationship:**
- Dispatch-1 (lifter re-anchor) may optionally harvest the column-streaming `ls_update_column` leaf and author its L1>L0 theme. Dispatch-5 (lowering-verifier audit of the theme once promoted) forward-references this.
- **Conflict level:** None at the operational level. The two work on disjoint files: dispatch-1 edits `book/src/L2-L1/incremental-least-squares-composition-lowering.md` + optionally creates `book/src/L1/ls-update-column.md` + optionally creates `book/src/L1-L0/ls-update-column-mutation-rotation.md`; dispatch-5 audits the same theme file (appends a `verified_against:` YAML block if dispatch-1 promotes the theme). Sequenced: dispatch-5 must run AFTER dispatch-1 reports land so the theme is firm before auditing.
- **Sequencing:** Dispatch-1 in wave 1; dispatch-5 in wave 2 (forward-reference dependency).

**Dispatch-2 and Dispatch-1 potential re-read conflict:**
- Dispatch-2 edits `book/src/L0/linalg-operator-file.md` (lines 22, 87). Dispatch-1 does not touch this file (it operates on L2>L1 theme + L1 leaves). No conflict.

**Dispatch-3, Dispatch-4, Dispatch-5 audit cohort:**
- All three are lowering-verifier audits operating on disjoint files: normalize-mutation-rotation, back-solve L1, and incremental-least-squares-composition-lowering.
- No conflicts; all run in parallel or sequentially (audit appends are non-conflicting).

**Dispatch-6 (same-layer-cross-cutter) and other dispatches:**
- Reads L1 entries `book/src/L1/matrix-weighted-norm.md` and `book/src/L1/bilinear-form.md` (cycle-027 D2 and D3 already touched matrix-weighted-norm, but this is a fresh read). Does not mutate these files (survey/decision dispatch). No conflicts.

**Dispatch-7 (harvester localization) and all others:**
- Read-only on the Palace tree (`palace/linalg/`). No book/ mutations. No conflicts with any dispatch.

**Overall:** ZERO operational conflicts. Dispatches 1/2/3/4/6/7 are **fully parallel**. Dispatch-5 forward-references dispatch-1's promotion (must sequence after wave-1 reports land).

## Sequencing schedule

**Wave 1 (parallel):** Dispatches 1, 2, 3, 4, 6, 7
- Dispatch-1 (lifter re-anchor + promote the deferred theme; may optionally harvest column-streaming leaf)
- Dispatch-2 (lifter citation-hygiene sweep)
- Dispatch-3 (lowering-verifier normalize-mutation-rotation audit)
- Dispatch-4 (lowering-verifier back-solve audit)
- Dispatch-6 (same-layer-cross-cutter variant-axis + test-coverage gate)
- Dispatch-7 (harvester trsv localization)

**Wave 2 (parallel, after wave-1 reports land):** Dispatch 5
- Dispatch-5 (lowering-verifier audit of the now-firm incremental-least-squares-composition-lowering theme, optionally including ls-update-column leaf audit if dispatch-1 harvested it)

## Open questions / caveats

1. **Dispatch-1 optional leaf harvest scope:** The resume notes and active-head description note that dispatch-1 may "optionally harvest the still-un-harvested column-streaming `ls_update_column` leaf if it tightens the fan-down." The decision is left to the lifter producer (if the re-anchor tightens the theme's terminal-back-solve projection and leaves the column-streaming step needing its own distinct L1 entry, author it; otherwise defer to a later harvest). **If harvested, dispatch-5 must include the new leaf's L1>L0 theme audit.**

2. **Dispatch-6 decision routing:** The same-layer-cross-cutter dispatch on matrix-weighted-norm + bilinear-form test-coverage gates will emit a survey + summary but likely surface an **ask** to the human: "Is the test coverage sufficient to promote the rough-in L1 entries to firm?" This is an escalation-class decision (promotion gate). The critic will flag it; the integrator may record it as a deferred OQ if the answer is not immediately available.

3. **Dispatch-7 localization scope:** The harvester is scoped to **localization only** — determining whether Palace has a standalone `trsv` API and where it is used. The decision of whether to author an L1 `trsv` entry (if one should exist) or whether to route to an obstruction-theme (if `trsv` only appears inside preconditioners) is deferred to the planner + meta-phase after the localization report lands.

## Suggested next dispatches (if room in cycle-029/030)

If all 7 dispatches land cleanly this cycle and wave-1 integrations confirm no major issues:

- **abstractor** — `back-solve-mutation-rotation-L1-L0-theme` — author the L1>L0 lowering theme for the firm `back_solve` leaf (the GMRES/FGMRES restart-correction back-substitution loops `iterative.cpp:652-660`/`:831-840`). Unblocked by c027 D4.
- **layer-intro-author** — `L2-index-prose-refresh-for-fold-cohort` — refresh the L2 `index.md` §"Semantics (overlay)" primitive list and Working Notes to reflect the completion of the `l2-named-composition-lifts` cohort (all three firm: `orthogonalize`, `incremental-least-squares` + now-firm `incremental-least-squares-composition-lowering`). Pairs with the c028 dispatch-2 self-description refresh.
- **harvester / abstractor** — `ls-update-column-column-streaming-leaf` + `ls-update-column-mutation-rotation-theme` (if dispatch-1 defers them) — harvest and lower the column-streaming running-QR step (GMRES/FGMRES per-column `K ← [K h_new / ||h_new||]` streaming update). Optionally paired with the column-streaming L1 entry if dispatch-1 defers the harvest.

---

**Status: dispatches ready for assignment. Awaiting execution.**

---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T21:40:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T21:52:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Re-anchor chebyshev (L4) — forM_/foldM → iterate_while_pure + step-count predicate; flip rough-in → firm"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing pointer verified in-range and supporting. Strawman §6.5 step 5 at `l4_calculus.md:418` literally says the bounded `for t_idx in 1..=k` "uses `iterate_while_pure` with `s.step < maxSteps` as the continuation predicate, encoding the `k`-step bound inside the state and the predicate" — the decisive precedent the report leans on. `run_lbm` `:382-385` is the live `iterate_while_pure` call shape. `iterate-while.md:7` names Chebyshev as a consumer; `:98` is the no-extras/empty-trajectory idiom; `:155` step-composition non-law; `:165` bounded-`max_it`-totality discharge; `:193-195` `iterate_while_pure_L3`; `:201-207` predicate-shape variant axis — all confirmed. L0 `chebyshev.cpp:191`/`:200` for-loop anchors inherited transitively (consistent with the firm L1/L2 base). All `[old]` blocks across Changes 1–19 match the current `chebyshev.md` / `index.md` byte-for-byte.

**surface-or-evidence — pass.** Refinement-shaped (modifies an existing firm-family entry's surface) AND carries the rotation evidence (the strawman precedent + the iterate-while family). Not a bare rotation_claim; the surface change (the `apply` body + 18 prose sites) is the substance.

**rotation-quality — pass.** This is a *re-anchoring* onto a firm primitive, not a layer rotation, so the "more compact L_{n+1}" bar is N/A in the strict sense; the relevant quality test is faithfulness, which holds. The step-count-predicate encoding is sound: the counter folded into the carry (`{it}` outer; `{r,d,st,k}` inner) with predicate `s.it <= op.pc_it` / `c.k <= op.order - 1` reproduces the bounded `[1..pc_it]` / `[1..order-1]` ranges, is total by construction (strict counter increment → predicate false in `bound` steps, `:165`), and the `y` accumulator is correctly placed as the orthogonal `Solve` effect threaded outside the value-carry (`:59,98`). The empty-trajectory `iterate_while_pure` choice matches `run_lbm`. Not renaming-only.

**variant-axis-coverage — pass.** The two construction-absorbed axes (polynomial-kind, element-type) are untouched and preserved. The combinator-miner-flagged *presentation* axis (carry-`st` vs. with-prev closure-`prev`) is explicitly decided (Change 12) with the 4th-kind `st=()` degenerate-case argument, not hidden; the residual same-layer unify-with-CG-`beta_prev` item is correctly carried as a non-blocking watch-item.

**cross-reference-integrity — pass.** `iterate-while.md`, `iterate-while-with-prev.md`, `L3/chebyshev.md`, `krylov-step-typed-wrapper-dissolution.md`, the concept slugs, and `l4_calculus.md` all resolve (verified on disk). The L3 `itloop`/`kloop` (`L3/chebyshev.md:223-233`) are genuinely the `iterate_while_pure_L3`-shaped tail recursions (`it > op.pc_it`, `k >= op.order`) that Changes 8/9 claim as the lowering image — faithful.

**edge-label-fidelity — pass.** Every edge-labelled bullet discusses its own edge: the L4>L3 bullets (Changes 4, 8, 9) narrate L4→L3 dissolution (the two folds → `iterate_while_pure_L3` tail recursions), the L3>L2 bullet stays identity-in-form. Direction held high→low throughout; no inverted rewrite.

**plan-kind-consistency — pass; firm flip WARRANTED.** The sole `rough-in` driver was the un-anchored `forM_`/`foldM` vocabulary; after the re-anchor there is zero un-anchored combinator left (every iteration site is `iterate_while_pure` from the firm family). The body, signature, semantics, laws, and chebyshev math are untouched — genuine lifter discipline, no re-derivation. The cohort/dep-map updates (Changes 18/19: rough-in cohort 1→0, firm 3→4, dep-map cell `UNRECONCILED`→firm) are internally consistent and match the staged combinator-miner intent. The inner-loop-presentation OQ is correctly *resolved-and-closed* (the combinator-miner both staged AND recommended the carry-`st` form, so enacting it is within lifter scope), not improperly carried forward.

**skill-uptake-survey — warning.** A pure re-anchoring/refinement-surface pass of this shape has a matching skill (`verify-refinement-surface`, and `verify-rotation-citation` / `verify-citation-range` for the strawman precedent + iterate-while citations); the report's Discipline-notes self-audit is thorough but cites no skill invocation. Telemetry-only, non-blocking.

### Issues found

No blocking issues. The firm flip is warranted and the re-anchor is faithful to the firm `iterate-while` family and the strawman precedent. Two minor, non-blocking observations:

1. **(low / telemetry) skill-uptake** — `book/src/L4/chebyshev.md` re-anchor pass references no skill invocation despite `verify-refinement-surface` / `verify-rotation-citation` matching its shape. Surfaced per skill-uptake-survey; not a defect.

2. **(low / out-of-scope, observation only)** — `book/src/L3/chebyshev.md:236-238` prose still describes the L3 `itloop`/`kloop` as "the L3 rendering of the L4 `foldM`/`forM_`." After this report lands, that downward-pointing prose names the now-superseded L4 vocabulary. Not in this dispatch's scope (the report correctly limits itself to the L4 entry + L4 index), and harmless to the firm flip — flagged only so a later cross-layer touch can refresh the L3 entry's upward reference. Candidate for repairer-deferral or a future lifter pass, not a correction this report must make.

## Repair

### Fixes attempted

- **Finding**: `book/src/L3/chebyshev.md:236-238` downward-prose names the now-superseded L4 `foldM`/`forM_` combinators (Issue 2, low / out-of-scope).
  - **Decision**: unrepairable (deferred via OQ — the lighter correct option).
  - **Rationale**: the staleness is in a *different file* (`L3/chebyshev.md`) than the two this report edits (`L4/chebyshev.md` + `L4/index.md`). The report author deliberately scoped this dispatch to the L4 entry + L4 index — even declining the standalone L4>L3 theme as out-of-scope (CYCLE.md OQ 3). Adding an L3-file mutation would extend the report's footprint beyond what was dispatched and critiqued, and the prose is an *upward* (L3→L4) reference — the kind of thing the critic verified file-by-file. Per the dispatcher's "pick the lighter correct option," promoting an OQ keeps the report's footprint exactly as authored and reviewed; an in-report L3 mutation does not. I appended OQ `l3-chebyshev-downward-prose-iterate-while-refresh` to CYCLE.md §"Open questions / caveats" item 5 (so integrator-per-report promotes it as part of this report's OQ set, the correct write path — the repairer does not own `open-questions.md` promotion). Routed to a follow-up cross-layer touch (lifter on `L3/chebyshev` or a cross-layer-cross-cutter sweep); explicitly NOT a blocker on the firm flip.

- **Finding**: skill-uptake-survey — re-anchor pass references no skill invocation despite `verify-refinement-surface` / `verify-rotation-citation` matching its shape (Issue 1, telemetry, non-blocking).
  - **Decision**: not-needed (acknowledged).
  - **Rationale**: telemetry-only, non-blocking, as the critic stated. No artifact defect; the report's Discipline-notes self-audit is thorough. Not a repairable surface issue — nothing in the CYCLE.md content is wrong. Acknowledged for the meta-phase skill-uptake window; not carried as a finding requiring revision.

### Unrepairable findings

- `l3-chebyshev-downward-prose-iterate-while-refresh` — the L3 entry's upward `foldM`/`forM_` reference at `L3/chebyshev.md:236-238` should be refreshed to name `iterate_while_pure`/`iterate_while_pure_L3`. Deferred (cross-layer, different file). Follow-up routing: lifter on `L3/chebyshev` OR a cross-layer-cross-cutter sweep. NOT a blocker on this report's firm flip — the OQ rides on the per-report OQ-promotion path, and the report applies cleanly without it.

## Suggested resolution

`ready`. The firm flip is warranted and the re-anchor is faithful (all 8 checks pass; the lone skill-uptake warning is telemetry-only). Two non-blocking notes for the integrator:

1. When promoting this report's Open questions, carry CYCLE.md OQ item 5 (`l3-chebyshev-downward-prose-iterate-while-refresh`) into `scaffolding/open-questions.md` alongside the OQs this report *closes* (`chebyshev-l4-firm-via-iterate-while-reanchor` and `chebyshev-l4-inner-loop-presentation-carry-st-vs-with-prev` — both resolved-and-closed by Changes 11/12). The new OQ relates to those and to `chebyshev-slice-l4-full-removal` (its sub-blocker (b) "`L4/chebyshev` firming" now closes, leaving only sub-blocker (a) citation re-point for the slice §L4 removal).
2. No artifact build risk: all `[old]` blocks were verified byte-for-byte by the critic; the changes touch only `L4/chebyshev.md` + `L4/index.md`.

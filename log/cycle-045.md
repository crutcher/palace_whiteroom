# 2026-06-01 cycle-045 — integration summary

**Completed the substantive L3>L2 rotation frontier: `eigsolve-opaque-eigen-iteration` (opaque-library root) + `chebyshev-nested-recurrence` (unconditional-nested-double-loop root) landed firm, COMPLETING the four-root erasure-scope taxonomy — L3>L2 firm 15 → 17 (17-of-18, effectively complete). THIRD/FINAL primary cycle of meta-batch-13; the batch-13 meta-phase fires next as a separate dispatch.**

> NOTE on numbering: this is the **layered-era cycle-045** (post-2026-05-26 structural redirect). A legacy **slice-vertical-era cycle-45** entry (2026-05-25, "forward gmres [L3→L4]") is preserved at the bottom of this file for historical continuity; the two are distinct cycles that collide only on the zero-padded filename.

**Kind:** integration (primary cycle — phases plan → dispatch → critique → repair → integrate)
**Meta-batch:** batch-13, position 3 of 3 (cycles 043/044/045). **The batch-13 meta-phase fires AFTER this cycle-045 finalize commit, as a SEPARATE dispatch — NOT run in this cycle.** The cycle counter does NOT reset across batch boundaries.
**Written by:** `integrator-finalize` (split integrator-per-report ×3 + finalize ×1).

## Headline

The third and final primary cycle of meta-batch-13 closed the substantive L3>L2 rotation frontier opened by cycle-044's `orthogonalize-variant-split`:

- **L3>L2 firm 15 → 17** — both remaining substantive (non-identity) L3>L2 rotations landed:
  - `book/src/L3-L2/eigsolve-opaque-eigen-iteration.md` (D1, abstractor) — the **opaque-library** erasure-scope root. The eigen-iteration is SLEPc/ARPACK-owned: the per-step body lifts to a global tensor-field expression but the iteration loop is library-owned and does NOT lift. Re-anchored `book/src/L3/eigsolve.md` (frontmatter `lowers_to:` + §Downward + §Lowers-to + §"L3 vs L2 distinction") from the stale "no L3-L2 theme file — in-line" assertion onto the new theme; the non-adjacent L3↔L1 body-identity stays the correct in-line note.
  - `book/src/L3-L2/chebyshev-nested-recurrence.md` (D2, cross-cutter) — the **unconditional-nested-double-loop** erasure-scope root. The inner `k`-recurrence + the outer `pc_it` Richardson sweep are both witnessed sequential obstructions; the erasure is unconditional because the polynomial-kind {4th,1st} and element-type {real,complex} variant axes are loop-invariant. Re-anchored `book/src/L3/chebyshev.md` (frontmatter + §Downward + §"L3 vs L2 distinction") + the `book/src/L3/index.md` dep-map "Lowers to" cell. The two L3-form / L2-form pseudo-code blocks use inner ```` ```text ```` fences — the build handles them cleanly.
- **`l3-l2-rotation-theme-coverage-gap` 15-of-18 → 17-of-18 ≈ COMPLETE.** The 18th theme is `apply_linop`, which is no-L2-by-design (confirmed `book/src/L3/apply_linop.md:146` — "no interposed L2 entry, no L3-L2 theme"). The gap is effectively **17-of-17-applicable**; the re-denomination (17-of-18 vs 17-of-17-applicable) is a methodology-metric call deferred to the batch-13 meta-phase.

- **The substantive L3>L2 erasure-scope taxonomy is now COMPLETE with FOUR roots** (D3, layer-intro-author, SOLE count-owner): the consolidated `book/src/L3-L2/index.md` §Working-Notes tally + the taxonomy paragraph distinguish the four substantive (non-identity) erasure-scope roots from the 13 thin `-body-identity` identity-themes:
  - **unconditional-single-loop** — `ksp-solve-outer-driver`
  - **variant-conditional-single-loop** — `orthogonalize-variant-split` (cycle-044)
  - **unconditional-nested-double-loop** — `chebyshev-nested-recurrence` (this cycle)
  - **opaque-library** — `eigsolve-opaque-eigen-iteration` (this cycle)

## The cycles-041–045 foundation campaign

With cycle-045, the **L2-floor + L3>L2-rotation foundation campaign** (cycles 041–045, under the 2026-05-31 uniform-pull-up / foundation-first directive) is substantially complete. It filled the middle of the stack:

- **L2 9 → 21 firm operators**
- **L2>L1 7 → 19 firm themes**
- **L3>L2 2 → 17 firm themes**

The stack is now **substantially rectangular through L0–L3**. The next frontier (batch-14+) resumes the uniform climb UPWARD: L4>L3 coverage + L4 expansion (L4 is only 4 firm) + any residual L2>L1 gaps.

## Reports consumed (3 of 3 applied clean)

| Report | Dispatch | Status | follow_up |
|---|---|---|---|
| `2026-06-01T135812Z-cycle-045-abstractor-eigsolve-L3-L2-theme` | D1 — abstractor, eigsolve L3>L2 substantive theme | applied | — |
| `2026-06-01T135812Z-cycle-045-cross-cutter-chebyshev-L3-L2-decision` | D2 — cross-cutter, chebyshev L3>L2 decision + theme | applied | — |
| `2026-06-01T135812Z-cycle-045-layer-intro-author-taxonomy-counts` | D3 — layer-intro-author, taxonomy + consolidated counts | applied | — |

**3 of 3 dispatched-ready reports applied clean** — 3/3 staging rows == dispatched-ready (the cycle-018 staging-completeness gap did NOT recur for the **TWENTY-SIXTH** consecutive cycle / the **FORTIETH** consecutive clean split-integrator cycle). Zero deferrals, zero rejections, zero build-repairs.

## Safety-net gates (aggregated)

- **retroactive-budget global:** 0 (well under the ≥4 block).
- **build-breakage repair:** none needed — `cargo make book` exit 0 (~90s). linkcheck2 green for both new substantive theme files + the re-anchored `L3/eigsolve.md` and `L3/chebyshev.md` + `L3/index.md` live links + zero dead links. The only build noise is pre-existing: KaTeX "Potential incomplete link" false-positives in `design/l4_calculus.md` (inside math-display HTML, not real links) and pre-existing unclosed-HTML-tag WARNs in older `L1-L0/`+`L0/` files. The `chebyshev-nested-recurrence.md` inner ```` ```text ```` pseudo-code fences built cleanly.
- **commit atomicity:** single commit, pushed immediately; two-phase SHA patch per cycle-004/005 canonical pattern.
- **consumed-report frontmatter integrity:** all 3 reports marked `integrated_at` + `integration_commit` + `integration_notes`.
- **count-ownership partition:** held cleanly — D1/D2 own their own table rows + §Vocabulary-cohort bullets, D3 is sole consolidated count-owner. D2's Change 5 (the tally rewrite) was correctly SKIPPED at D2's integration; D3's Edit 1 is the authoritative whole-bullet rewrite from the on-disk base. No `parallel-blind-shared-index-count-divergence`.

## Open questions promoted (4)

- `l3-l2-substantive-erasure-scope-taxonomy` (D1) — the now-complete erasure-scope taxonomy; flagged to UNIFY with the cycle-044 `substantive-l3-l2-erasure-scope-taxonomy` at the batch-13 taxonomy review.
- `concepts-sequential-obstruction-opaque-library-marker-distinction` (D1) — opaque-library-rooted-marker vs Palace-authored-recurrence distinction for `concepts/sequential-obstruction.md`; layer-intro-author / cross-cutter territory.
- `l3-l2-chebyshev-substantive-theme-vs-in-line-decision` (D2) — RESOLVED + LANDED (dedicated theme warranted; answer-link `book/src/L3-L2/chebyshev-nested-recurrence.md`). Partially closes the cycle-044 `remaining-substantive-l3-l2-rotations-chebyshev-eigsolve` (its chebyshev half; the eigsolve half closed by D1).
- `l3-l2-erasure-scope-taxonomy-FOUR-root-complete-ratify-plus-concepts-page` + `l3-l2-coverage-gap-denominator-reconciliation-17-of-18-vs-17-of-17-applicable` (D3) — the four-root taxonomy ratification + a concrete `concepts/erasure-scope.md` page recommendation, and the coverage-gap re-denomination, both routed to the meta-phase.

## Next-cycle priorities — the batch-13 meta-phase decision queue (fires next)

This is the FINAL cycle of batch-13; the batch-13 meta-phase fires next as a separate dispatch. It carries:

1. **Ratify the 4-root erasure-scope taxonomy** + decide on a `concepts/erasure-scope.md` page; unify the 3 predecessor OQ slugs (`substantive-l3-l2-erasure-scope-taxonomy` c044 / `l3-l2-substantive-erasure-scope-taxonomy` c045-D1 / `l3-l2-erasure-scope-taxonomy-FOUR-root-complete` c045-D3).
2. **Close** `remaining-substantive-l3-l2-rotations-chebyshev-eigsolve` (both halves landed this cycle).
3. **Re-denominate the coverage gap** (17-of-17-applicable; `apply_linop` the non-applicable 18th).
4. **Standing batch-13 items from c043/c044:** dual-registration convention codification; chebyshev cohort-count reconciliation + normalize fused-composite sub-shape; the scaffolding slug-rename residual sweep; the L2-floor-implies-same-cycle-L3-reanchor process signal (cycle-planner dispatch-design note candidate).
5. **Next frontier:** with L0–L3 substantially rectangular, the uniform climb resumes UPWARD — L4>L3 coverage + L4 expansion (L4 only 4 firm) + any remaining L2>L1 gaps.

(Note: one OQ slug reads "batch-15" — that is a typo for the upcoming batch-13 meta / next meta; ignore the number, the item is for the upcoming meta-phase.)

---

## 2026-05-25 cycle-45 — forward gmres [L3→L4] — pass

- Synthesis: GMRES L4 rotation: state-stratified into SimState/OpParams/Krylov bundles; solve coordinated as StateT SimState with Outcome-typed termination; convergence policy absorbed as a Convergence constructed value (third constructed-operator surface alongside apply_BA and apply_correction); L3 sequential-obstruction record (ls_update_column, back_solve) carried through to L4 as pure Krylov-to-Krylov functions, NOT hidden by monadic effect. Variant absorption preserved: main control flow never reads pc_side/gs_orthog/flexible/tolerances; only constructed-operator helpers do. retroactive_claim_evidence: the L4 content already exists in book/src/spec/slices/gmres.md under `## L4 — calculus form` (state stratification subsection at lines defining SimState/OpParams/Krylov; constructed-operator interface subsection; monadic coordination subsection with `Solve a = StateT SimState Identity a`, gmres_solve, solve_loop, restart_cycle, inner_loop definitions; sequential-obstruction placement subsection; FGMRES variant subsection). The five claims emitted cite: (1) the three-bundle state stratification at the `### State stratification` subsection; (2) the monadic solve_loop/restart_cycle/inner_loop at the `### Monadic coordination` subsection; (3) the Outcome sum type and termination classification at the same subsection; (4) the build_convergence helper at the `### Convergence-criterion absorption` subsection; (5) the pure-function typing of ls_update_column and back_solve at the `### Sequential-obstruction placement` subsection.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 2 concept_write(s), 1 dep-map edge(s), 3 lesson(s); 5 rotation_claim(s).

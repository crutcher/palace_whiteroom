# Cycle 025 — NEP-interior L1>L0 cohort COMPLETE + eigsolve chain FULLY COMPLETE (first primary cycle of meta-batch-7)

**Date:** 2026-05-29 · **Commit:** `210e622` · **Status:** clean (zero deferrals/rejections/rework; zero build-repairs; twenty-first consecutive clean split-integrator cycle)

**Batch position:** cycle-025 is the **FIRST** primary cycle of meta-batch-7 (cycles 025/026/027). **The batch-7 meta-phase fires after the cycle-027 finalize commit** (3:1 cadence; cycle counter does NOT reset across batch boundaries). This `log/cycle-025.md` + the `scaffolding/integrator-signals.md` cycle-025 section OPEN the batch-7 evidence window.

**Recovery note:** no crash this cycle (the prior two cycles 023/024 were crash-recovered). STAGING.md was authoritative; the cross-check of 9 staging rows vs 9 dispatched ready reports reconciles clean (all `applied`, no `partially-applied`/`deferred`/`rejected`).

## What landed (9 reports — all wave-1)

- **HEADLINE 1 — NEP-interior L1>L0 cohort COMPLETE (5/5).** L1>L0 firm themes **+2** (theme files 20→22): `nleps-jacobian-action-mutation-rotation` (the quasi-Newton `T'(λ)`-derivative-pencil-action mutation rotation) + `nleps-eigenvalue-correction-mutation-rotation` (the per-step `δλ` Rayleigh-functional scalar-correction rotation over firm BLAS-1 leaves `dot`/`axpby`/`scal`). With these two, all five deflated NEP-interior atoms now have firm L1>L0 lowering themes: `apply_nonlinear_pencil` (c024) + `nleps_deflated_residual` (c023) + `nleps_deflated_solve` (c024) + `nleps_jacobian_action` (c025) + `nleps_eigenvalue_correction` (c025). The full per-step quasi-Newton chain `residual → jacobian-action → eigenvalue-correction → deflated-solve → line-search` is now lowered L1>L0 end-to-end.
- **HEADLINE 2 — eigsolve L1→L2→L3→L2>L1→concept chain FULLY COMPLETE.** L2>L1 firm **+1** (L2-L1 chapter count 6→7 = 6 firm + 1 partly-constructive): `eigsolve-spectral-transform-composition` (the per-step shift-invert spectral-transform de-fusion `apply_shift_invert = apply_linop(M) ▷ ksp_solve((K − σM)⁻¹)`; firm-on-positive-structure, both RHS leaves `apply_linop`+`ksp_solve` firm, LHS L2 `eigsolve` firm c023; this was the chain's only remaining authoring gap, the L2>L1 edge). NEW `concepts/eigsolve.md` (**concepts +1**; the cross-cutting navigational home for the firm L1→L2→L3 chain; introduces the `EigSolver[problem]` opaque type). With both landings the migrated-to-plan item `eigsolve-l2-l1-and-concept` is **FULLY discharged** — both halves landed this cycle.
- **HEADLINE 3 — batch-6 lowering-verifier audit cohort 4/4 DISCHARGED.** (a) `apply-nonlinear-pencil-mutation-rotation` audited fully-supported → **stays firm** (additive `verified_against:` 21 entries, all `supports`). (b) `deflate-composition-lowering` audited → **STAYS partly-constructive** (`gate_verdict: stays-gated-correctly`; NO positive bare-Gram `(XᴴX)⁻¹` Galerkin-core solve found in `palace/*.cpp` — the near-candidate `romoperator.cpp:757-765` solves against `Ar = VᴴAV`, not a Gram; the shared bare-Galerkin-core promotion gate STAYS OPEN, triple-referenced: L2 `deflate` `:774` + L1>L0 `nleps-deflated-solve` + this L2>L1 theme). (c) `gram-fold-specialization` audited fully-supported → **stays firm** (additive `verified_against:` 13 entries + in-theme `vector.cpp:667→:668` `MFEM_ASSERT` aligned-pass anchor correction at both in-theme sites + enclosing-range tighten `nleps.cpp:613-619→:614-619`). (d) `orthogonalize-composition-lowering` audited cleanly-partitioned → **stays firm, VERDICT-ONLY** (NO artifact mutation — the cycle-023/024 18-entry `verified_against` block already covers the three-way delegation boundary; appending would duplicate).
- **HEADLINE 4 — L1/L2/L3 index navigational-prose refresh** (4 surgical edits): L1 index `:108` cycle-009 historical-marker → past-tense + `eigsolve`-is-firm; L2 index `:81` repairer-folded single 1:1 `[old]`→`[new]` preserving the cycle-020 "L3 driver/kernel complementarity" bullet + appended consolidated batch-6 Working-Notes bullet; L3 index `:15` Sequential-obstructions overlay refreshed to name all three firm shapes (firm-driver `ksp_solve`, `chebyshev` + `eigsolve` partial-obstructions) + `:43` two Working-Notes bullets (cycle-020 `ksp_solve` firm + cycle-024 `eigsolve` partial-obstruction; count 9 firm + 2 partial-obstruction).

## Reports consumed (9)

| # | Report | Status | Landing |
|---|---|---|---|
| 1 | abstractor-nleps-jacobian-action-rotation | applied | NEW firm L1>L0 `nleps-jacobian-action-mutation-rotation` |
| 2 | abstractor-nleps-eigenvalue-correction-rotation | applied | NEW firm L1>L0 `nleps-eigenvalue-correction-mutation-rotation` (CLOSES 5/5 NEP-interior L1>L0 cohort) |
| 3 | abstractor-eigsolve-spectral-transform-composition | applied | NEW firm L2>L1 `eigsolve-spectral-transform-composition` (completes eigsolve L2>L1 edge) |
| 4 | layer-intro-author-concepts-eigsolve | applied | NEW concept page `concepts/eigsolve.md` (chain navigational home) |
| 5 | lowering-verifier-apply-nonlinear-pencil-audit | applied | additive `verified_against:` (theme stays firm) |
| 6 | lowering-verifier-deflate-composition-audit | applied | additive `verified_against:`+`gate_verdict:` (STAYS partly-constructive; gate STAYS OPEN) |
| 7 | lowering-verifier-gram-fold-specialization-audit | applied | `verified_against:` + `vector.cpp:667→:668` anchor correction + range tighten (stays firm) |
| 8 | lowering-verifier-orthogonalize-composition-audit | applied | verdict-only (cleanly-partitioned; NO artifact mutation) |
| 9 | layer-intro-author-l1-l2-l3-index-refresh | applied | 4 surgical index-prose edits (L1/L2/L3 index.md) |

## Roadmap deltas

- **L1>L0 themes** 20 → **22 files** (+`nleps-jacobian-action-mutation-rotation` +`nleps-eigenvalue-correction-mutation-rotation`); **NEP-interior L1>L0 cohort COMPLETE 5/5**.
- **L2>L1** 6 → **7 chapters** (6 firm + 1 partly-constructive; +`eigsolve-spectral-transform-composition` firm).
- **Concepts** +1 (`concepts/eigsolve.md`).
- **eigsolve chain** L1→L2→L3→L2>L1→concept **FULLY COMPLETE** (L1 firm c022, L2 firm c023, L3 partial-obstruction c024, L2>L1 firm c025, concept c025).
- **Unchanged:** L1 19 firm + 2 rough-in(test-coverage-bounded) + 6 rough-in(obstruction); L2 8 firm + 1 partly-constructive + 1 stub; L3 9 firm + 2 partial-obstruction; L4 4 firm; L0 22 chapters; Phase-1 removals 9/10.

## Build

`cargo make book` exit **0**, **ZERO build-repairs**. All 4 new chapters (2 L1>L0 themes + 1 L2>L1 theme + 1 concept page) + the 4 audit appends + the 4 index-prose edits SUMMARY-registered + link-clean. The only build warnings are **4 katex `Potential incomplete link` false-positives ALL confined to `design/l4_calculus.md`** (math-display LaTeX parens), NONE in a cycle-025-touched file.

## Safety-net gates

- **retroactive-budget global: 0** (all 9 rows 0-retroactive; the 4 audit additive `verified_against:`/`gate_verdict:` appends + the `gram-fold` anchor-precision corrections are not surface-rewrites; well below the ≥4 block threshold).
- **build-breakage repair:** none required (clean build).
- **commit atomicity:** single commit (artifact + scaffolding + log + book output + consumed-report frontmatter).
- **consumed-report frontmatter integrity:** all 9 reports marked `integrated_at`.
- **implied-component-stub-created: 0** (no dangling forward-ref required a stub — dispatch-2's sibling forward-ref to dispatch-1 landed serially ahead; the eigsolve concept page arrived as a FULL firm page, not a stub).
- **SUMMARY-chapter-registration auto-fix: 0** (every report proposed its own SUMMARY edit).

## Staging-log-completeness note

**9/9 rows — the cycle-018 staging-completeness gap did NOT recur for the SEVENTH consecutive cycle.** STAGING.md was authoritative this cycle; the cross-check of 9 staging rows vs 9 dispatched ready reports reconciles clean (all `applied`, no `partially-applied`/`deferred`/`rejected`).

## Wave-conflict observations

- **Shared-file serialized cleanly.** `SUMMARY.md` + `L1-L0/index.md` were touched by reports 1+2 (L1>L0 block); `SUMMARY.md` + `L2-L1/index.md` by report 3 (L2>L1 block); `SUMMARY.md` + `concepts/index.md` by report 4 (concepts block). The serial per-report integrator order re-read each shared file from disk before editing, so each landed at its documented primary anchor with no collision (reports 1/2 did not touch the L2-L1 block, so report 3's `deflate-composition-lowering` anchors were exactly as authored).
- **Serial dependency held (no stub needed).** Report 2's primary insert-anchor was report 1's just-landed `nleps-jacobian-action-mutation-rotation` row/entry; the documented serial dependency held, so the documented fallbacks were not needed and no plain-text forward-reference dangled.
- **`gram-fold-specialization` vs `deflate-composition-lowering` shared the L2-L1 directory** but touched disjoint files; no contention.

## Integration-tooling friction (batch-7 evidence-window — first entry)

- **codemap `read_range` +1 brace-boundary drift** recurred (nleps.cpp deflation block) vs citecheck/on-disk — same class as cycle-024's 5 off-by-one drifts. citecheck/`--anchor` is the citation source-of-truth; methodology signal for the citecheck-invocation question now that `tools/citecheck` is wired (carry-forward to batch-7 meta-phase).
- **Non-blocking citecheck AMBIG prose-shorthand** (`dot.md:43`/`:49`, `operator.cpp:621-638`) inside report CYCLE.md files — bare-basename readability shorthand with a resolving full-path canonical form in the same report; NOT in the artifact, not chased.

## Carry-forward to the batch-7 meta-phase (fires after cycle-027 finalize)

1. **codemap `read_range` +1 brace-boundary drift** (recurring; methodology signal — citecheck is citation source-of-truth; evaluate citecheck per-report-gate invocation now that `tools/citecheck` exists).
2. **Two carry-forward L1-ENTRY re-anchor OQs** routed to a follow-up lifter/repairer NLEPS-L1-entry citation-correction pass: `nleps_jacobian_action` 6 deflation-block anchors + `nleps_eigenvalue_correction` 2 anchors (`:596→:590` while-loop + add `:712` `alpha *= backtrack_factor`).
3. **The `vector.cpp:667→:668` SIBLING-sweep OQ** — `inner_product.md:360` + `inner-product-fold-specialization.md:59,260` still drifted (`gram-fold-specialization` corrected its own two sites this cycle; `dot-mutation-rotation:269` already correct; the sweep finishes the cohort).
4. **The entire `open-questions.md:327` four-slug audit-followup line is retirement/unification-ready** — 3 discharged (`apply-nonlinear-pencil` RESOLVED, `gram-fold-specialization` RESOLVED, `orthogonalize-composition` RESOLVED) + 1 re-scoped (`deflate-composition` → deferred/contingent promotion-watch co-keyed with `deflate-galerkin-core-promotion` at `:35`, trigger = a positive bare-Gram-solve site).
5. **The `open-questions.md:322` index-refresh OQ line is retirement-ready** — 2 clauses RESOLVED-enacted/already-satisfied this cycle + a 3rd-clause `l1-index-fifth-motif` confirm-and-retire.
6. **Follow-up cross-ref live-link upgrades pending:** `L2/eigsolve.md:163` pending-forward-ref → live link; the three chain-entry stale "concepts/eigsolve does not yet exist" prose; `gram.md:176,242` "(forthcoming)" text-refresh.
7. **Two new concept candidates flagged for the cross-cutter:** `constructed-solver-opaque-type` generic concept (`EigSolver[problem]` at 2 consumers, NOT warranted until a third) + `no-l4-eigsolve-entry-yet` (the speculative `solve-monad` L4 cap).

## Suggested next-cycle dispatches (cycle-026)

- (`lifter`/`repairer`, `nleps-l1-entry-citation-correction`) — apply the two carry-forward NLEPS L1-ENTRY re-anchor OQs + the `vector.cpp:667→:668` sibling sweep in one pass.
- (`lifter`/`layer-intro-author`, `eigsolve-chain-cross-ref-cleanup`) — upgrade `L2/eigsolve.md:163` + the three chain-entry "concepts/eigsolve does not yet exist" prose to live links; `gram.md` "(forthcoming)" text-refresh.
- (`cross-layer-cross-cutter` / `combinator-miner`, frontier vocabulary) — next fan-out-ranked component per the plan (NEP cohort + eigsolve chain now complete; the frontier shifts to the remaining shared-infrastructure / intermediate-tier items).

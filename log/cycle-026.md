# Cycle 026 — L1 firm 19→20 (+normalize) + L2 firm 8→9 (+incremental-least-squares, l2-named-composition-lifts COMPLETE 2/2) + matrix-weighted-norm L1>L0 firm + NLEPS/eigsolve citation-hygiene sweep (second primary cycle of meta-batch-7)

**Date:** 2026-05-29 · **Commit:** `PLACEHOLDER_SHA` · **Status:** clean (zero deferrals/rejections/rework; zero build-repairs; twenty-second consecutive clean split-integrator cycle)

**Batch position:** cycle-026 is the **SECOND** primary cycle of meta-batch-7 (cycles 025/026/027). **The batch-7 meta-phase fires after the cycle-027 finalize commit** (3:1 cadence; cycle counter does NOT reset across batch boundaries). This `log/cycle-026.md` + the `scaffolding/integrator-signals.md` cycle-026 section CONTINUE the batch-7 evidence window opened by cycle-025.

**Recovery note:** no crash this cycle. STAGING.md was authoritative; the cross-check of **9 staging rows vs 9 dispatched ready reports** reconciles clean (all `applied`, no `partially-applied`/`deferred`/`rejected`) — `rows == dispatched-ready-reports`, no staging-completeness gap.

## What landed (9 reports — all wave-1)

- **HEADLINE 1 — L1 firm 19→20 (+`normalize`).** NEW firm L1 operator `normalize :: Tensor[N] -> (Scalar, Tensor[N])` (i.e. `(β, x/β)`, `β = ‖x‖₂ > 0`) — the fused vector-normalisation that **returns the norm as a first-class result** (load-bearing: Arnoldi Hessenberg sub-diagonal entry, spectral-radius eigenvalue estimate, deflation companion-vector scale). Composes the firm leaves `nrm2` + `scal`; firm-on-positive-structure (`linalg::Normalize` is a read closure, `vector.hpp:262-270` + 5 call sites); partial at `x = 0` (L0 `MFEM_ASSERT`); carries an in-chapter **rough-in note** for the B-weighted sibling `normalize_B` (no fused Palace site; inherits `matrix-weighted-norm`'s test-coverage bound). Closes the plan item `normalize-l1-primitive-harvest`. The harvester correctly deferred the `Firm (19)→(20)` count-prose bump to layer-intro-author scope; **finalize applied it as measurable housekeeping** at `L1/index.md:31` (header + motif enumeration).
- **HEADLINE 2 — L2 firm 8→9 (+`incremental-least-squares`), l2-named-composition-lifts COMPLETE 2/2.** L2 `incremental-least-squares` STUB→**FIRM** — the GMRES/FGMRES running-QR / Givens-rotation least-squares stream, signature `incremental_least_squares :: (op: LsqOp, st: LsqState, h_new: HessCol) -> { state: LsqState', beta: RealScalar }` + terminal `back_solve`; 17 source pinpoints in both solver arms (`iterative.cpp`); 6 algebraic laws + 4 non-laws; 2 parametric variant axes; firm-on-positive-structure. The second L2 named-composition motif (sibling to `orthogonalize`, firm cycle-019) — with it the plan cohort **`l2-named-composition-lifts` is COMPLETE (2/2)**. L2 dep-map now **9 firm + 1 partly-constructive (`deflate`) + 0 stub**; SUMMARY `(stub)`-suffix dropped.
- **HEADLINE 3 — L1>L0 firm themes +1 (`matrix-weighted-norm-mutation-rotation`).** Stub→**FIRM** — the L1 energy norm `√(xᴴBx)` lowering forward into L0 `linalg::Norml2(comm, x, B, Bx)` = `B.Mult(x,Bx); dot = Dot(comm,Bx,x); √dot` (`operator.cpp:599-619`); Sub-pattern A real / B complex (real-`B`-on-complex-`x` lane split) / C the `Normalize` consumer; the SPD `MFEM_ASSERT(dot>0)` load-bearing-defensive guard + complex-Hermiticity-witness classification. A **firm lowering of a rough-in L1 operator** per the `eigsolve-mutation-rotation` precedent — the upstream L1 `matrix-weighted-norm` operator stays `rough-in (test-coverage-bounded)`, its own independent gate (not a gate hit here).
- **HEADLINE 4 — batch-7 NLEPS/eigsolve citation-hygiene sweep.** D1 (lifter) landed **23 surgical citation-drift swaps** across `nleps_jacobian_action.md` (16 deflation-block `+1` drifts), `nleps_eigenvalue_correction.md` (2: `while`-loop `:596→:590` −6, Armijo `α` `:709→:712` +3), `inner_product.md` (1), `inner-product-fold-specialization.md` (4 — the `vector.cpp:667→:668` MFEM_ASSERT sibling sweep) — both L1 entries stay firm, **3 OQs RESOLVED**. D7 (lifter) landed **8 plain-text→live-link cross-ref upgrades** across `L1/L2/L3/eigsolve.md` + `L2/gram.md` (targeting `concepts/eigsolve.md` + `L2-L1/eigsolve-spectral-transform-composition.md` + `L2-L1/gram-fold-specialization.md`, all on-disk + SUMMARY-wired) + 1 bounded `rough-in`→`firm` prose self-description correction, **3 OQs RESOLVED**. `L4/eigsolve.md` + the L3>L2 eigsolve theme correctly LEFT plain-text (genuinely absent).
- **HEADLINE 5 — lowering-verifier `verified_against:` audit cohort for the 3 cycle-025-new firm themes COMPLETE.** D6a `nleps-jacobian-action-mutation-rotation` (24 entries) + D6b `nleps-eigenvalue-correction-mutation-rotation` (19 entries) + D6c `eigsolve-spectral-transform-composition` (15 entries) — all `verdict: supports`, all additive EOF YAML appends, all themes stay firm, ZERO content/status change. The carry-forward L1-ENTRY drifts the audits re-confirmed were already resolved same-cycle by D1.
- **HEADLINE 6 — D5 (layer-intro-author) 5 navigational repoints.** `L0/linalg-operator-file.md` (§Notes + §Referenced-from) + `L0/mpi-globalsum-and-collectives.md` (§Referenced-from): `nrm2_weighted`/`dot_bilinear` candidate-slugs → live `matrix-weighted-norm`/`bilinear-form` links; `concepts/dependency-map.md`: pruned the stale `orthog → plane-rotation-stream` L1-tier edge; `concepts/negative-result-slice.md`: added the `sparse_triangular_solve` reciprocal-membership row. **3 OQs RESOLVED + 1 ADDRESSED-AT-L0** (residual `bilinear-form.md:416` `dot_bilinear` provenance note routed to a harvester/lifter follow-up).

## Reports consumed (9)

| # | Report | Status | Landing |
|---|---|---|---|
| 1 | lifter-nleps-l1-entry-reanchor | applied | 23 surgical citation-drift swaps (nleps_jacobian_action / nleps_eigenvalue_correction / inner_product / inner-product-fold-specialization); 3 OQs RESOLVED |
| 2 | harvester-incremental-least-squares-l2 | applied | L2 `incremental-least-squares` STUB→FIRM (**L2 firm 8→9**; l2-named-composition-lifts COMPLETE 2/2) |
| 3 | abstractor-matrix-weighted-norm-rotation | applied | L1>L0 `matrix-weighted-norm-mutation-rotation` STUB→FIRM (**L1>L0 firm themes +1**) |
| 4 | harvester-normalize-l1-decision | applied | NEW firm L1 `normalize` (**L1 firm 19→20**); `normalize-l1-primitive-harvest` plan item COMPLETE |
| 5 | layer-intro-author-naming-residue-sweep | applied | 5 navigational repoints (L0 overviews + concepts dep-map + negative-result-slice); 3 OQs RESOLVED + 1 ADDRESSED-AT-L0 |
| 6 | lowering-verifier-nleps-jacobian-action-theme-audit | applied | additive `verified_against:` 24 entries (theme stays firm) |
| 7 | lowering-verifier-nleps-eigenvalue-correction-theme-audit | applied | additive `verified_against:` 19 entries (theme stays firm) |
| 8 | lowering-verifier-eigsolve-spectral-transform-audit | applied | additive `verified_against:` 15 entries (theme stays firm; COMPLETES the 3-theme audit cohort) |
| 9 | lifter-eigsolve-chain-crossref-cleanup | applied | 8 plain-text→live-link cross-ref upgrades (L1/L2/L3 eigsolve.md + gram.md); 3 OQs RESOLVED |

## Roadmap deltas

- **L1** 19 → **20 firm** (+`normalize`; L1/index "Firm" header bumped 19→20) + 2 rough-in(test-coverage-bounded) + 6 rough-in(obstruction).
- **L2** 8 → **9 firm** (+`incremental-least-squares` stub→firm; dep-map 9 firm + 1 partly-constructive + 0 stub); **`l2-named-composition-lifts` cohort COMPLETE 2/2** (orthogonalize + incremental-least-squares).
- **L1>L0 firm themes** +1 (`matrix-weighted-norm-mutation-rotation` stub→firm).
- **L2>L1** unchanged-count (7 = 6 firm + 1 partly-constructive); the 3 cycle-025-new themes audited fully-supported, all stay firm (`verified_against:` cohort complete).
- **Unchanged:** L3 9 firm + 2 partial-obstruction; L4 4 firm; L0 22 chapters; concepts +0; Phase-1 removals 9/10; NEP-interior atoms 5/5; eigsolve chain L1→L2→L3→L2>L1→concept FULLY COMPLETE.

## Build

`cargo make book` exit **0**, **ZERO build-repairs**. The new `L1/normalize.md` + the 2 stub→firm rewrites (`incremental-least-squares`, `matrix-weighted-norm-mutation-rotation`) + the 3 `verified_against:` appends + the 5 navigational repoints + the 8 cross-ref live-link upgrades ALL SUMMARY-registered + link-clean. The 8 new live links (to `concepts/eigsolve.md`, `L2-L1/eigsolve-spectral-transform-composition.md`, `L2-L1/gram-fold-specialization.md`) all resolve — targets confirmed on-disk + SUMMARY-wired. The only build warnings are **59 katex `Potential incomplete link` false-positives ALL confined to `design/l4_calculus.md`** (math-display LaTeX), NONE in a cycle-026-touched file.

## Safety-net gates

- **retroactive-budget global: 0** (all 9 rows 0-retroactive; the citation-drift swaps + cross-ref live-link upgrades + additive `verified_against:` appends + navigational repoints are not surface-rewrites; well below the ≥4 block threshold).
- **build-breakage repair:** none required (clean build).
- **commit atomicity:** single commit (artifact + scaffolding + log + book output + consumed-report frontmatter + staging log).
- **consumed-report frontmatter integrity:** all 9 reports marked `integrated_at` + `integration_commit` + `integration_notes`.
- **implied-component-stub-created: 0** (no dangling forward-ref required a stub — the `normalize-mutation-rotation` L1>L0 + `bilinear-form-mutation-rotation` forward-refs correctly left plain-text, below the clearly-implied bar).
- **SUMMARY-chapter-registration auto-fix: 0** (every report proposed its own SUMMARY edit).

## Staging-log-completeness note

**9/9 rows — the cycle-018 staging-completeness gap did NOT recur for the EIGHTH consecutive cycle.** STAGING.md was authoritative; the cross-check of 9 staging rows vs 9 dispatched ready reports reconciles clean (all `applied`).

## Wave-conflict observations

- **Shared-file serialized cleanly.** `SUMMARY.md` was touched by reports 2 (`incremental-least-squares` de-stub `:45`), 3 (`matrix-weighted-norm-mutation-rotation` de-stub `:103`), and 4 (`normalize` registration `:68`) — three disjoint anchors; the serial per-report integrator order re-read SUMMARY from disk before each edit, no collision. `L2/index.md` (report 2), `L1-L0/index.md` (report 3), `L1/index.md` (report 4) likewise disjoint.
- **`eigsolve.md` (L1/L2/L3) touched by two reports without conflict.** D1 (lifter) touched the L1 `nleps_*` and `inner_product` entries (NOT the `eigsolve.md` files); D7 (lifter, integrates LAST) touched `L1/L2/L3/eigsolve.md` + `L2/gram.md`. The lowering-verifier D6c audit touched the DIFFERENT file `L2-L1/eigsolve-spectral-transform-composition.md` (the theme), not the `L2/eigsolve.md` entry D7 edits — no contention; D7 re-read all four entry files from disk before editing.
- **Serial dependency held (no stub needed).** D7's 8 live-link upgrades depend on the cycle-025-landed targets (`concepts/eigsolve.md`, the two L2-L1 themes) — all on-disk before this cycle began, so no plain-text forward-reference dangled.

## Integration-tooling friction (batch-7 evidence-window — second entry)

- **codemap `read_range` +1 brace-boundary drift CONFIRMED across a THIRD batch.** The cycle-026 D1 lifter + multiple producers re-confirmed the `+1` drift on brace-opening lines (`nleps.cpp` deflation block; `operator.cpp:601`). citecheck/`--anchor` + on-disk is the citation source-of-truth. **STRONG batch-7 meta-phase enactment candidate** — the standing OQ recommends strengthening role-specs to "codemap is localization-only; citecheck/on-disk is the citation source of truth," and possibly a standing citecheck gate (now that `tools/citecheck` is wired).
- **Non-blocking citecheck AMBIG prose tokens** inside report CYCLE.md files (bare-basename readability shorthand with a resolving full-path canonical form in the same report) — NOT in the artifact, not chased.
- **`scaffolding/integrator-signals.md` ~1455 lines** (over the ~500-line budget; pre-existing archival backlog) — still a meta-phase archival task.

## Carry-forward to the batch-7 meta-phase (fires after cycle-027 finalize)

1. **codemap `read_range` +1 brace-boundary drift — third-batch confirmation; STRONG enactment candidate** (role-spec wording "codemap is localization-only; citecheck/on-disk is citation source of truth" + possibly a standing citecheck per-report gate).
2. **NEW carry-forward re-anchors:** `L1/matrix-weighted-norm.md` `operator.cpp:601` brace drift (sites `:58`,`:83`; `:128` correct); the `Category 4` workspace mislabel (`L1/matrix-weighted-norm.md:9` + `L0/linalg-operator-file.md:33` vs `mutable-workspace-pattern.md:82` Category-4 = "assembled-matrix retention"); `concepts/givens.md:29` source staleness (`gmres.md` → `iterative.cpp`); `bilinear-form.md:416` `dot_bilinear` provenance note.
3. **Now-actionable:** `l2-ksp-solve-materialise-iterate-incremental-least-squares-cite-tightening`; the forward-referenced `normalize-mutation-rotation` L1>L0 theme (abstractor); the paired `bilinear-form` firm-promotion + `matrix-weighted-norm-mixed-element-type-variant` lowering-verifier audit.
4. **Cohorts COMPLETE:** `l2-named-composition-lifts` 2/2 (orthogonalize + incremental-least-squares both firm); `normalize-l1-primitive-harvest` plan item.
5. **`scaffolding/integrator-signals.md` archival** (~1455 lines as of cycle-025, over the ~500-line budget; pre-existing backlog).

## Suggested next-cycle dispatches (cycle-027 — third/final of meta-batch-7)

- (`abstractor`, `normalize-mutation-rotation`) — author the forward-referenced L1>L0 `normalize-mutation-rotation` theme (the `linalg::Normalize` → `nrm2`/`scal` lowering) now that the firm L1 `normalize` operator exists.
- (`lifter`/`harvester`, `matrix-weighted-norm-l1-entry-reanchor` + `bilinear-form-provenance-refresh`) — apply the NEW carry-forward re-anchors (`operator.cpp:601` brace drift on the L1 entry; `bilinear-form.md:416` provenance note; `concepts/givens.md:29` staleness; the Category-4 mislabel).
- (`lowering-verifier`, `matrix-weighted-norm-mutation-rotation-audit` + paired `bilinear-form`) — the standard `verified_against:` audit of the now-firm `matrix-weighted-norm-mutation-rotation` + the paired `bilinear-form-mutation-rotation` audit / firm-promotion.
- (`cross-layer-cross-cutter` / `combinator-miner`, frontier vocabulary) — next fan-out-ranked component per the plan (NEP cohort + eigsolve chain + l2-named-composition cohort now complete; the frontier shifts to the remaining shared-infrastructure / intermediate-tier items).

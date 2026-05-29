# Cycle 018 — BLAS-1 variadic-fold unification ENACTED (third/final primary cycle of meta-batch-4)

**Date:** 2026-05-29 · **Commit:** `PLACEHOLDER_SHA` · **Status:** clean (zero deferrals/rejections/rework; zero build-repairs; fourteenth consecutive clean split-integrator cycle)

**Batch position:** cycle-018 is the **THIRD/FINAL** primary cycle of meta-batch-4 (cycles 016/017/018). The batch-4 meta-phase fires **after this cycle-018 finalize commit** (separate step, separate commit).

> Note: this file replaces a legacy `cycle-18` stub (2026-05-24 "back orthog" era, pre-structural-redirect) that shared the same path; the prior content is preserved in git history.

## What landed

- **`linear_combination` L2 operator PROMOTED rough-in→firm** (harvester) — full chapter `book/src/L2/linear_combination.md`: the variadic BLAS-1 scalar-weighted-sum fold `[(Scalar, Tensor[N])] -> Tensor[N]` ≡ `foldl (\acc (a,t) -> acc + scal a t) (zeros N) pairs`, the **arity-axis** unification of `scal`/`axpy`/`axpby`/`axpbypcz` (complementary to the `scalar-promotion` element-type-axis unification). 7 holding algebraic laws (incl. concatenation-homomorphism = the unifying law + zero-coefficient term-drop = exact L0 `γ==0` branch `vector.cpp:749-751`), 3 explicit non-laws, 2 orthogonal variant axes, sibling-`dot`-not-subsumed §, 9 self-verified L0 ranges. `firm` on direct source-transcription per the `chebyshev-iteration` firm-without-dedicated-test precedent — the harvester correctly REFUSED to cite the `test-vector.cpp` "Vector Sum" tests (they exercise `linalg::Sum`, a DIFFERENT reduce-to-scalar fold). **Constructive prong (b) of the human-raised OQ `blas1-variadic-linear-combination-fold-unification` is now FULLY ENACTED** (rough-in cycle-017 → firm cycle-018).
- **`linear-combination-fold-specialization` L2>L1 theme** (abstractor) — new firm chapter `book/src/L2-L1/linear-combination-fold-specialization.md` + theme-list row + SUMMARY register: the arity-dispatch fusion-selection lowering taking the L2 `linear_combination` variadic fold into the L1 fixed-arity specializations, with pinned summation order. **Second real chapter under the L2-L1 Part.**
- **`inner_product` L2 rough-in row** (combinator-miner) — new dep-map row at `book/src/L2/index.md`: the fold-sibling of `linear_combination` along the **conjugation-convention** axis (NOT arity); `(Tensor[N], Tensor[N]) -> Scalar`, M-weighted member `xᴴ M y`; fuses up from `dot`/`tdot`/`bilinear-form`; ≥3-instance bar met. Forward-ref to the not-yet-authored `./inner_product.md` kept PLAIN-TEXT (no dead link).
- **`nested-constructed-operator-gate` concept page** (layer-intro-author) — new `book/src/concepts/nested-constructed-operator-gate.md` + SUMMARY register: the named concept for an L1>L0 closure whose constructed-operator gate carries a FURTHER nested constructed-operator gate (eigsolve ⊃ divfree ⊃ ksp; ≥2-firm-instance bar cleared). Inbound link from `divfree-projector-mutation-rotation`, outbound link to `constructed-operator-factory`.
- **divfree-theme "first→third" provenance correction** (lifter) — `book/src/L1-L0/divfree-projector-mutation-rotation.md` "first nested-gate instance" claim corrected to "third" (`eigsolve-mutation-rotation`, firm cycle-011, is the prior + richer instance). Firm unchanged.

## Reports consumed (5)

| report | agent | status | follow-up |
|---|---|---|---|
| `2026-05-28T231026Z-harvester-linear-combination-L2` | harvester | applied | — (OQ `linear-combination-harvester-formalization` resolved) |
| `2026-05-28T231017Z-layer-intro-author-nested-gate-concept` | layer-intro-author | applied | — |
| `2026-05-28T231500Z-lifter-divfree-first-claim-correction` | lifter | applied | — |
| `2026-05-28T231508Z-abstractor-l2-l1-linear-combination-theme` | abstractor | applied | `linear-combination-fold-specialization-theme-followups` |
| `2026-05-28T231046Z-combinator-miner-inner-product-fold` | combinator-miner | applied | `inner-product-harvester-formalization-and-conjugation-pinning` |

## Roadmap deltas

- **L2 firm 2 → 3** (+`linear_combination`).
- **L2>L1 firm 1 → 2** (+`linear-combination-fold-specialization`).
- **L2 rough-in: `inner_product`** (was `linear_combination`).
- **+1 concept page** (`nested-constructed-operator-gate`).
- Firm L1 (11) / L3 (8) / L4 (4) unchanged. L0 unchanged (21 chapters). L1>L0 unchanged (11 themes; divfree firm got a provenance correction). Phase-1 corpus removals stay 9/10.

## Build

clean — `cargo make book` exit 0, `mdbook-linkcheck` zero broken links, zero build-repairs. 6 pre-existing katex math-display false-positive warnings in `design/l4_calculus.md` carry unchanged. Build-checklist verified: `linear_combination` live links resolve; `inner_product` ref is plain-text (no dangling forward-link); new L2>L1 theme renders; `nested-constructed-operator-gate` renders with inbound/outbound links resolving; SUMMARY has all 3 new entries.

## Safety-net gates

- retroactive-budget global = **0** (all 5 reports net-new/append; no retroactive edits to existing firm L0-slice citations). Well below per-slice ≥3 / global ≥4 block thresholds.
- build-breakage = none. commit atomicity = single commit. consumed-report frontmatter integrity = all 5 marked.

## OQ ledger

- **2 RESOLVED**: `linear-combination-harvester-formalization`, `nested-constructed-operator-gate-concept-and-divfree-correction` (both prongs).
- **2 ANSWERED**: `inner-product-fold-sibling-candidate`; `divfree-closure-nesting-constructed-gate-carrying-constructed-gate` (flipped answered→resolved, prong-b enacted).
- **2 NEW opens**: `inner-product-harvester-formalization-and-conjugation-pinning`, `linear-combination-fold-specialization-theme-followups`. Parent `blas1-variadic-linear-combination-fold-unification` prong (b) DONE / prong (a) combinator-miner spec extension remains for the batch-4 meta-phase.

## Staging-log-completeness note

The cycle-018 `STAGING.md` captured only report-1's row; reports 2–5 applied their artifact changes + OQ promotions cleanly (verified against the working tree, all 5 reports `overall_status: ready`, and a clean build) but did not append staging rows. integrator-finalize reconciled from the artifact + report frontmatter + OQ-ledger notes. This is a per-report-integrator staging-append-discipline gap (NOT an artifact gap) — carried forward to the batch-4 meta-phase.

## Carry-forward to batch-4 meta-phase (fires next)

1. **HEADLINE: combinator-miner arity-blindness → prong (a) spec extension** (parametric/variadic-family detection mode, so arity-families surface as ONE candidate not N missed leaves) — the headline meta-phase enactment.
2. **`specialized-agent-direct-write-to-book-during-dispatch` RECURRENCE-3** (cycle-008/012/017) — cycle-018 had ZERO leaks (explicit per-dispatch reminders worked), but the prompt-guard lives only in `layer-intro-author.md`; enact across ALL 8 specialized specs.
3. **`rough-in-forward-reference-must-be-plain-text-not-live-link`** candidate friction (cycle-017 build-break root cause) — cycle-018 honored it cleanly; codify it.
4. **4+ skill-uptake-survey telemetry warnings** across the batch (named-skill-by-slug uptake weakness).
5. **NEW: staging-log-append-completeness gap** (this cycle).
6. Recommend rebuilding the duplicated OQ index region.

## Suggested cycle-019 dispatches

`inner_product` harvester formalization + L2-L1 inner-product lowering theme; the conjugation-convention pinning; `gmres.md §L4 v0.6→v0.7` self-rotation (large); NLEPS at L1+ (large); bundle-6 #6 L0 candidate.

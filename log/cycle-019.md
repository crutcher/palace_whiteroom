# Cycle 019 — five firm promotions + new L0 anchor (first primary cycle of meta-batch-5)

**Date:** 2026-05-29 · **Commit:** `PLACEHOLDER_SHA` · **Status:** clean (zero deferrals/rejections/rework; zero build-repairs; fifteenth consecutive clean split-integrator cycle)

**Batch position:** cycle-019 is the **FIRST** primary cycle of meta-batch-5 (cycles 019/020/021). The batch-5 meta-phase fires **after the cycle-021 finalize commit** (3:1 cadence; cycle counter does NOT reset). It does NOT fire this cycle.

> Note: this file replaces a legacy `cycle-19` stub (2026-05-24 "forward chebyshev" era, pre-structural-redirect) that shared the same path; the prior content is preserved in git history.

## What landed

- **`assemble-diagonal` L1 operator PROMOTED stub→firm** (harvester) — `book/src/L1/assemble-diagonal.md`: the operator-to-data primitive `(A: LinearOperator[N,N]) -> Tensor[N]`; 6 algebraic laws + 4 non-laws; element-type live axis + operator-representation absorbed axis + 3 non-axes; exhaustive Evidence across operator/rap/hypre/libceed + the two smoother consumers + the libceed diagonal-assembly test. Establishes the **fifth L1 motif "operator-to-data introspection."** L1/index Firm header `(11)`→`(12)` + cohort bullet + dep-map row; SUMMARY de-stub. **L1 firm 11→12.**
- **`orthogonalize` L2 operator PROMOTED stub→firm** (harvester) — `book/src/L2/orthogonalize.md`: the named `project ▷ subtract` Gram-Schmidt composition lifting the firm L1 leaf, with `gs_orthog ∈ {MGS,CGS,CGS2}` as the visible per-variant batching/sequencing axis and the collective-shape residual axis `m×1 / 1×m / 2×m` as the load-bearing L2 content; `{ residual, coeffs }` record. L2/index dep-map row inserted after the inner_product row at :26; SUMMARY :41 in-place de-stub.
- **`inner_product` L2 operator PROMOTED rough-in→firm** (harvester, HEADLINE) — `book/src/L2/inner_product.md`: the reduce-to-`Scalar` fold `(x,y) -> Scalar ≡ foldl (+) zero (zipWith kernel x y)` unifying the L1 leaves `dot` (Hermitian) / `tdot` (unconjugated) / `bilinear-form` (M-weighted member) along the conjugation-convention / element-type / weight-presence axes; conjugation **PINNED arg-1 `xᴴ y`** with the §"Conjugation convention (pinned)" reconciliation against Palace's arg-2-conjugated `yᴴ x` source; 7 laws incl. split-additivity + the IEEE reduction-tree load-bearing non-law; §"Sibling fold: linear_combination is not subsumed"; §"Consumer: nrm2/matrix-weighted-norm = √∘inner_product." L2/index :26 row rough-in→firm flip (orthogonalize :27 untouched); SUMMARY :40 de-stub. **The L2 reduce-to-`Scalar` fold cohort now has BOTH operator + lowering theme firm; the L2 rough-in cohort is empty.**
- **`inner-product-fold-specialization` L2>L1 theme PROMOTED stub→firm** (abstractor) — `book/src/L2-L1/inner-product-fold-specialization.md`: the three-key dispatch (conjugation kernel / element-type / weight-presence) selecting the L1 leaves; the headline value-level conjugate-pair re-order `xᴴ y = conj(yᴴ x)` (invisible under real-projection: CG `iterative.cpp:395`, Poynting diagonal `boundarymodeoperator.cpp:85`; observable for full-complex: `boundarymodeoperator.cpp:90`) + the pinned-reduction-tree §"Summation-order recording" table carrying the IEEE-non-law detail the L2 entry deferred. **Third real chapter under the L2-L1 Part.** L2-L1/index row appended after `linear-combination-fold-specialization` :14; SUMMARY :49 de-stub.
- **`nrm2-mutation-rotation` L1>L0 theme PROMOTED stub→firm** (abstractor) — `book/src/L1-L0/nrm2-mutation-rotation.md`: L1 LHS `alpha = nrm2(x)` → L0 RHS one-line `Norml2` template + the four-stage `Dot→MPI_Allreduce→std::abs→std::sqrt` chain; 3 surface forms A/B/C; the `std::abs` guard classified **load-bearing defensive**; element-type real/complex variant-axis collapse; verified against L0 ranges. L1-L0/index dep-map row inserted between orthogonalize + minres rows; SUMMARY :83 in-place de-stub. **L1>L0 themes 11→12.**
- **`fespace-file` new L0 anchor chapter** (layer-intro-author) — `book/src/L0/fespace-file.md` (bundle-6 #6 — `palace/fem/fespace.{hpp,cpp}`; the FiniteElementSpace family L0 source-anchor) + SUMMARY row + L0/index File-overviews bullet. libceed basis/restriction + quadrature + geometric-factor forward-refs correctly plain-text (folded into OQ `fem-libceed-basis-restriction-l0-anchor`). **L0 21→22 chapters.**
- **`divfree-projector-mutation-rotation` OPTIONAL cross-link prose-sharpening** (cross-layer-cross-cutter) — sharpened the firm theme's §"Open questions / caveats" stale-`Mult`-doc-comment bullet (`:460-468`): names the class doc `:28-31` as the authoritative L0 site + `:155-190` impl + folds in the `divfree.cpp:176` third witness; Helmholtz/Hodge framing. **ZERO semantics change** — divfree firm unchanged. Resolves the carry-forward OQ `divfree-mult-doc-irrotational-vs-divfree-stale`.
- **combinator-miner parametric-family mode FIRST live exercise** (combinator-miner, proposal/mode-validation only — ZERO book mutation) — characterized the `inner_product` fold-family (fold-law membership test + 4 parameter axes + 3 over-unification guards) as harvester-input for the #7 inner_product harvester, AND surfaced the **Qualification-B mode-gap** (the smoother/constructed-operator-action cohort is parametric but NOT a fold, and the mode gives no positive channel for non-fold parametric families) routed to the batch-5 meta-phase, + confirmed the existing `variant-absorption-vs-instance-counting-policy` meta-agenda OQ.

## Reports consumed (8)

| report | agent | status | follow-up |
|---|---|---|---|
| `2026-05-29T023000Z-layer-intro-author-fespace-l0` | layer-intro-author | applied | `fem-libceed-basis-restriction-l0-anchor` |
| `2026-05-29T023000Z-harvester-assemble-diagonal-l1` | harvester | applied | `assemble-diagonal-mutation-rotation` (L1>L0); `l1-index-fifth-motif` refresh |
| `2026-05-29T023000Z-abstractor-nrm2-l1-l0` | abstractor | applied | `nrm2-mutation-rotation-verified-against-audit` (lowering-verifier) |
| `2026-05-29T023000Z-harvester-orthogonalize-l2` | harvester | applied | `orthogonalize-composition-lowering-l2-l1-theme`; `L2-layer-intro-refresh-for-named-compositions` |
| `2026-05-29T023000Z-cross-layer-cross-cutter-divfree-doc` | cross-layer-cross-cutter | applied | — (OQ `divfree-mult-doc-irrotational-vs-divfree-stale` resolved/closure-ready) |
| `2026-05-29T023000Z-combinator-miner-parametric-family` | combinator-miner | applied | `combinator-miner-nonfold-parametric-family-no-positive-channel` (→ batch-5 meta) |
| `2026-05-29T024500Z-harvester-inner-product-l2` | harvester | applied | — (OQ `inner-product-harvester-formalization-and-conjugation-pinning` resolved) |
| `2026-05-29T024500Z-abstractor-inner-product-fold` | abstractor | applied | `inner-product-fold-specialization-lowering-verifier-audit` |

## Roadmap deltas

- **L1 firm 11 → 12** (+`assemble-diagonal`).
- **L2 firm 3 → 5** (+`orthogonalize` +`inner_product`); **L2 rough-in cohort 1 → 0** (`inner_product` promoted).
- **L2>L1 firm 2 → 3** (+`inner-product-fold-specialization`).
- **L1>L0 themes 11 → 12** (+`nrm2-mutation-rotation` firm; divfree theme firm got an optional prose-sharpen).
- **L0 21 → 22 chapters** (+`fespace-file`).
- L3 (8 firm + 1 partial-obstruction) / L4 (4 firm) unchanged. Phase-1 corpus removals stay 9/10.

## Build

clean — `cargo make book` exit 0 (`Build Done`); all 6 cycle-019-touched HTML outputs render (`L0/fespace-file`, `L2/orthogonalize`, `L2/inner_product`, `L1/assemble-diagonal`, `L1-L0/nrm2-mutation-rotation`, `L2-L1/inner-product-fold-specialization`); zero build-repairs. All per-report forward-refs were correctly plain-text and all five de-stub SUMMARY edits were in-place (no duplicate-link errors). The 40 `Did you forget to define a URL` linkcheck2 warnings are ALL pre-existing katex math-display false-positives across `design/l4_calculus.md` + `concepts/*` + `L3/{dot,nrm2}` + `L4/iterate-while*` + the `$$`-bearing lowering themes — NONE in any cycle-019-touched file (the post-cycle-018 finalize undercounted them at ~6 by scoping only the `l4_calculus` subset; the condition is unchanged, carried since cycle-015).

## Safety-net gates

- retroactive-budget global = **0** (all 8 reports: 5 stub/rough-in→firm fresh-surface authoring + 1 new L0 create + 1 firm-entry OPTIONAL prose-sharpen [not a firm L0-slice citation-edit] + 1 OQ-only proposal/no-book-mutation). Well below per-slice ≥3 / global ≥4 block thresholds.
- build-breakage = none. commit atomicity = single commit. consumed-report frontmatter integrity = all 8 marked.

## OQ ledger

Large batch of RESOLVED/ADDRESSED markers + forward caveats appended by the 8 per-report integrators (close/migrate enactment is meta-phase authority — appended as intake). Notable: `inner-product-harvester-formalization-and-conjugation-pinning` RESOLVED (plan Now #1/#2, conjugation pinned arg-1), `inner-product-fold-sibling-candidate` RESOLVED, `inner-product-fold-specialization-l2-l1-theme` RESOLVED, `assemblediagonal-is-not-apply-linop-variant` RESOLVED, `nrm2-std-abs-defensive-guard-classification` RESOLVED-load-bearing, `divfree-mult-doc-irrotational-vs-divfree-stale` RESOLVED/closure-ready.

## Staging-log-completeness note

**The cycle-018 staging-completeness gap did NOT recur** — all 8 cycle-019 reports appended their `STAGING.md` rows (8/8). The batch-4 meta-phase per-report-integrator spec step-7 hardening + the integrator-finalize step-1 cross-check held. `STAGING.md` was authoritative this cycle.

## Carry-forward to cycle-020/021 + batch-5 meta-phase (fires after 021)

1. **combinator-miner NON-fold-parametric-family mode-gap** (report-6 Qualification B — headline batch-5 meta-phase item; feeds the friction-ledger `combinator-miner-arity-blind-parametric-family-detection` resolution) + the `variant-absorption-vs-instance-counting-policy` close.
2. **critic-vs-repairer citation-line-offset-drift on orthogonalize-l2** (critic raised 3 spot-line warnings; repairer's independent re-verify found the report's original pointers correct — a 3-of-3-same-direction signal worth a friction-window glance IF it recurs; single-cycle, not yet a pattern).
3. **`classify-variant-axis` SKILL.md:64-68 `gs_orthog` worked-example staleness** flagged to `skill-candidates.md` by the orthogonalize-l2 repairer (meta-phase skill-correction authority).
4. **L2-layer-intro refresh** now that L2 has 5 firm ops + named-composition + fold cohorts (two converging refresh flags: `L2-layer-intro-refresh-for-named-compositions` + `L2-layer-intro-refresh-for-fold-cohort` — meta-phase may fold into one).
5. **skill-uptake-survey named-skill-by-slug telemetry** continues across reports #4/#7/#8 (batch-5 meta-phase telemetry).

## Suggested cycle-020 dispatches

- abstractor on the `inner-product-fold-specialization` lowering-verifier audit + the conjugate-pair-reorder caller-classification.
- abstractor on the BLAS-1 L1>L0 lowering-theme gap: `dot-mutation-rotation` + `scal-mutation-rotation` (the `(stub)` :82/:84 SUMMARY rows) + `assemble-diagonal-mutation-rotation`.
- abstractor on `orthogonalize-composition-lowering` L2>L1 theme (now-firm L2 anchor ready).
- layer-intro-author L2 Part-intro refresh (folds the two converging flags).
- `gmres.md §L4 v0.6→v0.7` self-rotation (large carry-forward); NLEPS at L1+ (large); `l3-vocabulary-inventory-gap` (gemv/trsv L3 cohort growth).

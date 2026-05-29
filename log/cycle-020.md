# Cycle 020 — five firm landings + corrective orthogonalize backfill (second primary cycle of meta-batch-5)

**Date:** 2026-05-29 · **Commit:** `14cc0bd` · **Status:** clean (zero deferrals/rejections/rework; zero content build-repairs; one routed dep-map consistency-repair; sixteenth consecutive clean split-integrator cycle)

**Batch position:** cycle-020 is the **SECOND** primary cycle of meta-batch-5 (cycles 019/020/021). The batch-5 meta-phase fires **after the cycle-021 finalize commit** (3:1 cadence; cycle counter does NOT reset). It does NOT fire this cycle.

> Note: this file replaces a legacy `cycle-20` stub (2026-05-24 "forward gmres [L0→L1]" era, pre-structural-redirect) that shared the same path; the prior content is preserved in git history.

## Headline defect-correction — cycle-019 orthogonalize fence-truncation

**The cycle-019 `orthogonalize` L2 harvest landed a truncated chapter.** The firm chapter body was authored **OUTSIDE** the report's proposed-changes `edit:` fenced block, so the cycle-019 integrator (commit `efb8a0b`) applied only the 14-line intro. The result on disk: `book/src/L2/orthogonalize.md` was a 14-line intro with **NO `## Status`**, while `L2/index.md:27` dep-map and `SUMMARY.md:41` already asserted `firm`. The dep-map/SUMMARY were correct; the chapter body was missing.

- **Caught by:** the cycle-020 `layer-intro-author-l2-refresh` critic — the L2-refresh report's firm-`orthogonalize` dep-map assertions depended on a firm body that did not exist on disk.
- **Corrected by:** `harvester-orthogonalize-l2-backfill` (staging row #1, applied FIRST by ordering constraint) — a full-file replacement recovering the complete firm chapter (`## Status: firm` + Signature + 7 algebraic laws + Variant axes + L2-vs-L1 + Evidence).
- **This is a defect-CORRECTION, NOT a firm-count increment** — `orthogonalize` was already counted firm in the cycle-019 roadmap. The L2 firm count is **unchanged at 5**.
- **Provenance for the meta-phase:** TWO skill-candidates filed (`proposed-changes-fence-encloses-full-body-guard`, `verify-intro-firmness-survey-against-on-disk-status-lines`) + OQ `firm-chapter-body-authored-outside-proposed-changes-fenced-block`. The prevention is two-pronged: a producer-side fence-completeness guard (the full chapter body must be enclosed in the proposed-changes block) AND the per-report-integrator hard-step that surveys intro-firmness assertions against on-disk `## Status` lines.

## What landed

- **`dot-mutation-rotation` L1>L0 theme PROMOTED stub→firm** (abstractor) — `book/src/L1-L0/dot-mutation-rotation.md`: the Hermitian inner-product mutation-rotation; two variant axes (element-type real/complex + `tdot` unconjugated sibling); closes the cycle-019 `nrm2` sub-pattern-A forward-ref `nrm2 = √∘abs∘dot`. L1-L0/index dep-map row appended after the nrm2 row; SUMMARY :82 in-place de-stub.
- **`scal-mutation-rotation` L1>L0 theme PROMOTED stub→firm** (abstractor) — `book/src/L1-L0/scal-mutation-rotation.md`: in-place scalar multiply; element-type + scalar-promotion variant axes; `nleps.cpp:486-493` normalize site. L1-L0/index dep-map row inserted after nrm2 / before dot; SUMMARY :84 in-place de-stub.
- **`assemble-diagonal-mutation-rotation` L1>L0 theme — NEW firm file** (abstractor) — `book/src/L1-L0/assemble-diagonal-mutation-rotation.md`: operator-to-data diagonal extraction; 4 L0 sub-patterns; the matrix-free high-order-Nedelec **approximate-diagonal caveat is a positively-anchored load-bearing non-law** (`jacobi.hpp:15-16` + `rap.cpp:163-164` + `test-libceed.cpp` `rtol=1.0`), so landed `firm` NOT `partly-constructive`; `reciprocal`/`elementwise_product` forward-refs correctly plain-text. New SUMMARY chapter line after scal; new dep-map row.
- **`ksp_solve` L3 operator — NEW firm file** (harvester, HEADLINE) — `book/src/L3/ksp_solve.md`: the **first NON-identity L3 backfill** — the outer-driver `iterate_while_L3` fold carrying the outer-loop `sequential-obstruction`, complementing the firm L3 `krylov-step` kernel half (whose body IS identity-in-form). A genuine iteration-rotation, NOT a corollary of `krylov-step`; its L3>L2 rotation is substantive (the `L3-L2/ksp-solve-outer-driver` theme is WARRANTED but gated on the L2 `ksp_solve` stub→firm promotion). Landed `firm` ABOVE a `stub` L2 anchor (maturity-gradient inversion, acceptable under the **Identity-lowerings still require both L levels** invariant — each layer coherent within itself). New SUMMARY chapter line after chebyshev; new dep-map row. **L3 firm 8→9.**
- **`gmres-inner-loop-iterate-while-migration` L4>L3 theme PROMOTED rough-in→firm** (lifter) — `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md`: 9 surgical `[old]`/`[new]` firming edits; the LHS surface landed the SAME apply (Edit 10 appended the `gmres.md` §L4 v0.6→v0.7 inner-loop `iterate_while` self-rotation via option (a) `check_stop_into_carry` to `book/src/spec/slices/gmres.md`). The `cg.md:215-219` stale CG-precedent refs were re-anchored to firm `L4/krylov-step` Form A. **fgmres sibling STAYS rough-in** (held cycle-021). **L4>L3 firm 1→2, rough-in 2→1.**
- **`inner-product-fold-specialization` L2>L1 theme AUDITED + caller-inventory appended** (lowering-verifier #7 + cross-layer-cross-cutter #8) — `book/src/L2-L1/inner-product-fold-specialization.md`: #7 appended a `verified_against:` yaml block at EOF (15 audit rows, verdict `fully-supported`, keep firm); #8 appended a `conjugation_caller_inventory:` block into §Condition 5 (Dot conjugation load-bearing in exactly ONE algorithm — SLEPc-NEP `nleps.cpp`, 4 observable sites; `palace/fem/` has ZERO Dot callers; 11 invisible + 4 observable = 15 caller sites). Theme stays `firm` (no status change).
- **L2 Part-intro refresh** (layer-intro-author #9) — `book/src/L2/index.md`: 5 firm + 2 stubs (`incremental-least-squares`, `ksp_solve`, both live-linked, materialized 2026-05-28); new §"Vocabulary cohort" subsection; 5-row→7-row §"Operator dep-map"; refreshed Working-Notes bullets.

## Reports consumed (9)

| report | agent | status | follow-up |
|---|---|---|---|
| `2026-05-29T034441Z-harvester-orthogonalize-l2-backfill` | harvester | applied | `firm-chapter-body-authored-outside-proposed-changes-fenced-block` (→ batch-5 meta) |
| `2026-05-29T034441Z-abstractor-dot-mutation-rotation` | abstractor | applied | `dot-mutation-rotation-verified-against-audit` (lowering-verifier) |
| `2026-05-29T034441Z-abstractor-scal-mutation-rotation` | abstractor | applied | `scal-mutation-rotation-verified-against-audit` (lowering-verifier) |
| `2026-05-29T034441Z-abstractor-assemble-diagonal-rotation` | abstractor | applied | `assemble-diagonal-mutation-rotation-verified-against-audit`; `assemble-diagonal-l1-anchor-absmulttranspose-line-drift` |
| `2026-05-29T034441Z-harvester-l3-ksp-solve` | harvester | applied | `l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion`; `l3-vocabulary-inventory-gap-ksp-solve-resolved-and-remaining-inventory` |
| `2026-05-29T034441Z-lifter-gmres-l4-self-rotation` | lifter | applied | `fgmres-inner-loop-iterate-while-migration-firm-against-gmres-sibling`; `gmres-l4-standalone-operator-entry-vs-slice-l4-placement` |
| `2026-05-29T034441Z-lowering-verifier-inner-product-fold` | lowering-verifier | applied | `inner-product-fold-specialization-operator-cpp-inline-anchor-drift` |
| `2026-05-29T034441Z-cross-layer-cross-cutter-dot-callers` | cross-layer-cross-cutter | applied | `nleps-deflation-subspace-projection-combinator-deflate-gram`; `orthog-hpp-localdot-globalsum-unweighted-inner-product-surface` |
| `2026-05-29T034441Z-layer-intro-author-l2-refresh` | layer-intro-author | applied | `l2-index-ksp-solve-l3-crossref-upgrade-now-possible` |

## Roadmap deltas

- **L1>L0 themes 12 → 15** (+`dot-mutation-rotation` stub→firm, +`scal-mutation-rotation` stub→firm, +`assemble-diagonal-mutation-rotation` new firm).
- **L3 firm 8 → 9** (+`ksp_solve`, first non-identity L3 backfill).
- **L4>L3 firm 1 → 2** (+`gmres-inner-loop-iterate-while-migration` rough-in→firm); **rough-in 2 → 1** (fgmres stays rough-in).
- **L2 firm 5 (unchanged)** — `orthogonalize` body recovered via the corrective backfill; this is a defect-correction, NOT a new firm operator.
- **L2>L1 firm 3 (unchanged)** — `inner-product-fold-specialization` audited `fully-supported` (keep firm) + given a §Condition 5 caller inventory.
- L1 (12 firm) / L4 (4 firm) / L0 (22 chapters) unchanged. Phase-1 corpus removals stay 9/10.

## Build

clean — `cargo make book` exit 0 (`Build Done`, ~89s). All cycle-020-touched outputs render. **ONE consistency-repair** (NOT a content build-repair): the deferred `L4/index.md:44` (gmres theme dep-map row) + `:53` (`iterate-while` "Lowers to" cell) firm-sync routed by the lifter (OQ `gmres-l4-l3-theme-dep-map-firm-sync`) — a firm theme carrying a `*(rough-in; landed cycle-008 wave-2)*` annotation is a cross-reference-integrity drift; synced to `*(firm; cycle-020 wave-1 lifter re-anchor)*`; the fgmres sibling row was NOT touched (stays rough-in); rebuilt clean exit 0. The katex `Potential incomplete link` / `Did you forget to define a URL` warnings (`[i,j]`/`[j+1]` parsed as markdown reference links inside `$$...$$`) are ALL pre-existing math-display false-positives across `design/l4_calculus.md` + `concepts/*` + `L3/{dot,nrm2}` + `L4/iterate-while*` + the `$$`-bearing lowering themes — NONE in any cycle-020-touched file; same condition carried since cycle-015.

## Safety-net gates

- retroactive-budget global = **0** (all 9 reports: 1 corrective full-file replacement + 2 stub→firm full-file replacements + 1 new L1>L0 file + 1 new L3 file + 1 L4>L3 theme firm-flip-with-LHS-surface + 1 `verified_against:` metadata append + 1 `conjugation_caller_inventory:` evidence append + 1 structural L2 intro refresh). Well below per-slice ≥3 / global ≥4 block thresholds.
- build-breakage = none (one routed dep-map consistency-repair). commit atomicity = single commit. consumed-report frontmatter integrity = all 9 marked.

## Staging-log-completeness note

**9/9 rows — the cycle-018 staging-completeness gap did NOT recur for the second consecutive cycle.** STAGING.md was authoritative this cycle; the cross-check of 9 staging rows vs 9 dispatched ready reports reconciles clean.

## Wave-conflict observations

- **L1-L0/index.md multi-row-append case** — integrations #2 (dot), #3 (scal), #4 (assemble-diagonal) each appended a dep-map row into the BLAS-1+ cohort after the nrm2 row; serial per-report dispatch + re-read-disk-before-edit serialized the three appends cleanly with zero collision.
- **Two appends to `L2-L1/inner-product-fold-specialization.md`** — #7 (lowering-verifier) appended a `verified_against:` yaml block at END OF FILE (~:488-553); #8 (cross-layer dot-callers) inserted a `conjugation_caller_inventory:` block into §Condition 5 (~:284-289), ~200 lines ABOVE #7's block. Serial, non-overlapping; the EOF block was untouched. Composed cleanly.
- **Intra-cycle ordering dependency** — #1 (orthogonalize-backfill) landed FIRST (full firm body), so #9 (L2-refresh) firm-orthogonalize dep-map assertions resolve against on-disk state; #5 (L3/ksp_solve) created `book/src/L3/ksp_solve.md`, so #9's L2-index L3-crossref is now upgradeable (kept plain-text per dispatch directive). Both ordering constraints satisfied.

## Integration-tooling friction (for batch-5 meta-phase)

1. **HEADLINE — the cycle-019 orthogonalize fence-truncation defect** (see top). A producer authored-outside-fence pattern that the cycle-019 integrator silently truncated. TWO skill-candidates + an OQ.
2. **Recurring inline-anchor-drift** — now seen across cycle-019/020 in multiple reports (dot `:667`→`:668`/`:679`→`:678`; scal `nleps.cpp` `:491`→`:493`; assemble-diagonal `AbsMultTranspose` `:172`→`:174` + 3 more; ksp_solve accessor `:100-106`→`:101-108` + 3 more; inner-product-fold `operator.cpp` `:623`→`:624`/`:632`→`:634`/`:615-616`→`:616`). Wide enclosing ranges always correct; pinpoint anchors drift ±1-2 lines. The mechanical **codemap-backed citation-checker tool ASK** (batch-3/4 deferred) is increasingly justified.
3. **Sibling-slice citation re-anchor gap** — `cg.md` drifted the same way as `gmres.md` (the lifter re-anchored stale `cg.md:215-219` CG-precedent refs to firm `L4/krylov-step` Form A). Skill-candidate `sibling-slice-citation-reanchor-sweep` filed — when a self-rotation re-anchors one slice, sibling slices carrying the same stale precedent ref should be swept in the same pass.

## Carry-forward to cycle-021 + batch-5 meta-phase (fires after 021)

1. **fgmres-inner-loop-iterate-while-migration** now firmable (the gmres rotation landed) — cycle-021 lifter against the now-firm gmres sibling.
2. **L2 `ksp_solve` stub→firm** (harvester) then the **`L3-L2/ksp-solve-outer-driver` theme** (abstractor; gated on the L2 promotion).
3. The **`orthog.hpp:35` `LocalDot`+`GlobalSum` unweighted-inner-product surface** (second inner-product surface out of the Dot-caller census; same-layer-cross-cutter / harvester).
4. The **`deflate`/`gram` combinator-miner candidate** (the nleps deflation `X[j]ᴴ·` subspace-projection pattern over an invariant-pair basis `X`).
5. **L2 `ksp_solve` + `incremental-least-squares` stub→firm promotions** (both live-linked L2 stubs from 2026-05-28).
6. **eigsolve L3 kernel+driver pair** (next `l3-vocabulary-inventory-gap` item; `trsv` is blocked, no L1 anchor).
7. **`axpby`/`axpbypcz` L1>L0 mutation-rotation themes** still rough-in (BLAS-1 L1>L0 lowering floor NOT fully closed; `nrm2`+`dot`+`scal` firm but axpby/axpbypcz remain — `blas1-l1-l0-lowering-theme-gap` closing but not closed).
8. **NLEPS at L1+** (large multi-cycle carry-forward).

## Suggested cycle-021 dispatches

- lifter on `fgmres-inner-loop-iterate-while-migration` (firm against the now-firm gmres sibling).
- harvester on L2 `ksp_solve` stub→firm, then abstractor on the `L3-L2/ksp-solve-outer-driver` theme.
- same-layer-cross-cutter / harvester on the `orthog.hpp:35` unweighted-inner-product surface.
- combinator-miner on the `deflate`/`gram` deflation-subspace candidate (nleps).
- abstractor on `axpby`/`axpbypcz` L1>L0 themes (close the BLAS-1 floor).
- NLEPS at L1+ (large carry-forward); the `orthogonalize-composition-lowering` L2>L1 theme (carry from cycle-019).

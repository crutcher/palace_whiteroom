---
agent: integrator-finalize
invoked_at: 2026-05-29T045713Z
cycle: cycle-020
batch_position: meta-batch-5 second primary cycle (cycles 019/020/021; meta-phase fires after 021)
reports_consumed: 9
status: complete
integration_commit: 14cc0bd
---

# CYCLE-020 — integrator-finalize batch report

Cycle-end housekeeping for cycle-020, the SECOND primary cycle of meta-batch-5 (cycles 019/020/021; the batch-5 meta-phase fires after the cycle-021 finalize commit — NOT this cycle). Consumes the 9-row staging log `reports/cycle-020-integrator-staging/STAGING.md` (all `applied`, all build-relevant; the cross-check of 9 staging rows vs 9 dispatched ready reports reconciles clean — the cycle-018 staging-completeness gap did NOT recur for the second consecutive cycle).

## Summary

A high-yield vocabulary-buildup + corrective-backfill cycle: **FIVE firm landings** (3 L1>L0 BLAS-1+ mutation-rotation themes + 1 new L3 operator + 1 L4>L3 theme firm-flip) + **ONE corrective firm-body backfill** + ONE L2 Part-intro refresh + ONE lowering-theme audit + ONE cross-layer caller-inventory.

**HEADLINE DEFECT-CORRECTION — the cycle-019 orthogonalize L2 fence-truncation defect.** The cycle-019 `orthogonalize` L2 harvest authored the firm chapter body OUTSIDE the report's proposed-changes `edit:` fenced block, so the cycle-019 integrator (commit `efb8a0b`) landed only the 14-line intro; `book/src/L2/orthogonalize.md` was a 14-line intro with NO `## Status` while `L2/index.md:27` dep-map + `SUMMARY.md:41` already asserted `firm`. The dep-map/SUMMARY masked the missing body. Caught cycle-020 by the L2-refresh report's critic (its firm-`orthogonalize` assertions depended on a firm body that did not exist on disk); corrected by `harvester-orthogonalize-l2-backfill` (staging row #1, full-file replacement). **This is a defect-CORRECTION, NOT a firm-count increment** — `orthogonalize` was already counted firm in the cycle-019 roadmap; L2 firm stays 5. Two skill-candidates (`proposed-changes-fence-encloses-full-body-guard`, `verify-intro-firmness-survey-against-on-disk-status-lines`) + OQ `firm-chapter-body-authored-outside-proposed-changes-fenced-block` feed the batch-5 meta-phase.

## Reports consumed (9)

| # | report | agent | status | follow_up_agent / OQ |
|---|---|---|---|---|
| 1 | `2026-05-29T034441Z-harvester-orthogonalize-l2-backfill` | harvester | applied | meta-phase (`firm-chapter-body-authored-outside-proposed-changes-fenced-block`) |
| 2 | `2026-05-29T034441Z-abstractor-dot-mutation-rotation` | abstractor | applied | lowering-verifier (`dot-mutation-rotation-verified-against-audit`) |
| 3 | `2026-05-29T034441Z-abstractor-scal-mutation-rotation` | abstractor | applied | lowering-verifier (`scal-mutation-rotation-verified-against-audit`) |
| 4 | `2026-05-29T034441Z-abstractor-assemble-diagonal-rotation` | abstractor | applied | lowering-verifier (`assemble-diagonal-mutation-rotation-verified-against-audit`) |
| 5 | `2026-05-29T034441Z-harvester-l3-ksp-solve` | harvester | applied | harvester→abstractor (`l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion`) |
| 6 | `2026-05-29T034441Z-lifter-gmres-l4-self-rotation` | lifter | applied | lifter (`fgmres-inner-loop-iterate-while-migration-firm-against-gmres-sibling`) |
| 7 | `2026-05-29T034441Z-lowering-verifier-inner-product-fold` | lowering-verifier | applied | lifter (`inner-product-fold-specialization-operator-cpp-inline-anchor-drift`) |
| 8 | `2026-05-29T034441Z-cross-layer-cross-cutter-dot-callers` | cross-layer-cross-cutter | applied | combinator-miner (`nleps-deflation-subspace-projection-combinator-deflate-gram`); same-layer-cross-cutter (`orthog-hpp-localdot-globalsum-unweighted-inner-product-surface`) |
| 9 | `2026-05-29T034441Z-layer-intro-author-l2-refresh` | layer-intro-author | applied | layer-intro-author/lifter (`l2-index-ksp-solve-l3-crossref-upgrade-now-possible`) |

## Artifact changes (aggregate, from staging Files-touched)

**Created:**
- `book/src/L1-L0/assemble-diagonal-mutation-rotation.md` (NEW firm; report 4)
- `book/src/L3/ksp_solve.md` (NEW firm; report 5)

**Full-file replacements (stub/truncated → firm):**
- `book/src/L2/orthogonalize.md` (corrective backfill of truncated body; report 1)
- `book/src/L1-L0/dot-mutation-rotation.md` (stub→firm; report 2)
- `book/src/L1-L0/scal-mutation-rotation.md` (stub→firm; report 3)

**Surgical / additive edits:**
- `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` (9 [old]/[new] edits, rough-in→firm; report 6)
- `book/src/spec/slices/gmres.md` (§L4 v0.7 self-rotation append; report 6)
- `book/src/L2-L1/inner-product-fold-specialization.md` (verified_against: EOF block, report 7; conjugation_caller_inventory: §Condition 5 block, report 8)
- `book/src/L2/index.md` (2 [old]/[new] section rewrites, intro refresh; report 9)

**Index / SUMMARY:**
- `book/src/L1-L0/index.md` (dep-map rows for dot/scal/assemble-diagonal)
- `book/src/L3/index.md` (dep-map row for ksp_solve)
- `book/src/SUMMARY.md` (de-stub :82 dot, :84 scal; new chapter lines for assemble-diagonal + L3 ksp_solve)

**Build/consistency-repair (integrator-finalize):**
- `book/src/L4/index.md` (the deferred dep-map firm-sync routed by the lifter, OQ `gmres-l4-l3-theme-dep-map-firm-sync`): `:44` gmres theme row + `:53` `iterate-while` "Lowers to" cell synced `*(rough-in; landed cycle-008 wave-2)*` → `*(firm; cycle-020 wave-1 lifter re-anchor)*`. The fgmres sibling row NOT touched (stays rough-in).

## Safety-net gate results (aggregated)

| Gate | Result |
|---|---|
| retroactive-budget global (≥4 blocks) | **0** — all 9 rows 0-retroactive (1 corrective full-file replacement + 2 stub→firm full-file + 1 new L1>L0 + 1 new L3 + 1 L4>L3 firm-flip-with-LHS-surface + 2 metadata/evidence appends + 1 structural intro refresh); per-slice max 0 (<3); global 0 (<4); NO block |
| retroactive-budget per-slice (≥3 blocks, per-report owned) | all 0 (reported per row) |
| build-breakage repair (post-rebuild) | none (one routed dep-map consistency-repair, not a content break) |
| commit atomicity | single commit |
| consumed-report frontmatter integrity | all 9 marked `integrated_at` + `integration_commit: 14cc0bd` + `integration_notes` |
| staging-row-count cross-check | **9 rows vs 9 dispatched ready reports — reconciles clean** (cycle-018 gap did NOT recur, 2nd consecutive cycle) |

## Build status

`cargo make book` exit **0** (`Build Done`, ~89s), clean. All cycle-020-touched outputs render. ONE consistency-repair (the deferred `L4/index.md` dep-map firm-sync above), then rebuilt clean exit 0. The katex `Potential incomplete link` / `Did you forget to define a URL` warnings (`[i,j]`/`[j+1]` parsed as markdown reference links inside `$$...$$`) are ALL pre-existing math-display false-positives across `design/l4_calculus.md` + `concepts/*` + `L3/{dot,nrm2}` + `L4/iterate-while*` + the `$$`-bearing lowering themes — NONE in any cycle-020-touched file; same condition carried since cycle-015.

## Open questions promoted (aggregated, by the 9 per-report integrators)

New OQs this cycle (appended to `scaffolding/open-questions.md` by the per-report integrators): `firm-chapter-body-authored-outside-proposed-changes-fenced-block`; `dot-mutation-rotation-verified-against-audit`; `scal-mutation-rotation-verified-against-audit`; `assemble-diagonal-mutation-rotation-verified-against-audit`; `assemble-diagonal-l1-anchor-absmulttranspose-line-drift`; `l3-vocabulary-inventory-gap-ksp-solve-resolved-and-remaining-inventory`; `l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion`; `gmres-l4-standalone-operator-entry-vs-slice-l4-placement`; `fgmres-inner-loop-iterate-while-migration-firm-against-gmres-sibling`; `gmres-l4-l3-theme-dep-map-firm-sync` (RESOLVED by the finalize dep-map sync); `inner-product-fold-specialization-operator-cpp-inline-anchor-drift`; `dot-conjugation-observable-callers-nleps-cohort`; `nleps-deflation-subspace-projection-combinator-deflate-gram`; `orthog-hpp-localdot-globalsum-unweighted-inner-product-surface`; `l2-index-ksp-solve-l3-crossref-upgrade-now-possible`.

Resolvable-on-migration (close/migrate is meta-phase authority — recorded as intake): `l1-l0-dot-lowering-asymmetry`; `assemble-diagonal-mutation-rotation` (:110 theme-authoring); the `ksp_solve` constituent of `l3-vocabulary-inventory-gap` (:24); `inner-product-conjugate-pair-reorder-caller-classification` (:152); `gmres-inner-loop-iterate-while-migration` (Closed-index :192 → resolved cycle-020); `inner-product-harvester-formalization-and-conjugation-pinning` (:140; confirmed-firm).

## Wave-conflict observations

- **L1-L0/index.md multi-row-append (dot/scal/assemble-diagonal)** — three serial appends into the BLAS-1+ cohort after the nrm2 row; re-read-disk-before-edit resolved cleanly with zero collision. SUMMARY.md de-stubs (#2/#3 in-place) + new chapter lines (#4/#5) serialized by-slug.
- **Two appends to `inner-product-fold-specialization.md`** — #7 (lowering-verifier) `verified_against:` at EOF (~:488-553); #8 (cross-layer dot-callers) `conjugation_caller_inventory:` into §Condition 5 (~:284-289), ~200 lines above #7's block. Serial, non-overlapping; EOF block untouched. Composed cleanly (canonical "two additive appends to one firm chapter at distinct sections" pattern).
- **Intra-cycle ordering dependency** — #1 (orthogonalize-backfill) landed FIRST so #9 (L2-refresh) firm-orthogonalize assertions resolve on-disk; #5 (L3/ksp_solve) created the file so #9's L2-index L3-crossref is now upgradeable (left plain-text per dispatch). Both ordering constraints satisfied.

## Integration-tooling friction (→ batch-5 meta-phase)

1. **HEADLINE — the cycle-019 orthogonalize fence-truncation defect** (see Summary). Producer authored-outside-fence → integrator silent body-truncation, masked by a correct dep-map/SUMMARY. TWO skill-candidates + an OQ.
2. **Recurring inline-anchor-drift** — across cycle-019/020 in multiple reports (dot `:667`→`:668`/`:679`→`:678`; scal `nleps.cpp` `:491`→`:493`; assemble-diagonal `AbsMultTranspose` `:172`→`:174` + 3 more; ksp_solve accessor `:100-106`→`:101-108` + 3 more; inner-product-fold `operator.cpp` `:623`→`:624`/`:632`→`:634`/`:615-616`→`:616`). Wide ranges correct; pinpoint anchors drift ±1-2 lines. The mechanical codemap-backed citation-checker tool ASK (deferred batch-3/4) is increasingly justified — now a stable 2-cycle pattern.
3. **Sibling-slice citation re-anchor gap** — `cg.md` drifted the same way as `gmres.md`; the lifter re-anchored stale `cg.md:215-219` refs while doing the gmres self-rotation. Skill-candidate `sibling-slice-citation-reanchor-sweep` filed.

## Next-cycle priorities (cycle-021)

1. **`fgmres-inner-loop-iterate-while-migration`** firm against the now-firm gmres sibling (lifter).
2. **L2 `ksp_solve` stub→firm** (harvester), then **`L3-L2/ksp-solve-outer-driver` theme** (abstractor; gated on the L2 promotion — resolves the L3-above-stub-L2 maturity-gradient inversion).
3. **`orthog.hpp:35` `LocalDot`+`GlobalSum` unweighted-inner-product surface** (same-layer-cross-cutter / harvester) — the second inner-product surface out of the Dot-caller census.
4. **`deflate`/`gram` combinator candidate** (combinator-miner) — the nleps deflation `X[j]ᴴ·` subspace-projection pattern.
5. **`axpby`/`axpbypcz` L1>L0 mutation-rotation themes** (abstractor) — close the remaining BLAS-1 L1>L0 lowering floor (`blas1-l1-l0-lowering-theme-gap` is closing but NOT closed).
6. **eigsolve L3 kernel+driver pair** (next `l3-vocabulary-inventory-gap` item; `trsv` blocked, no L1 anchor).
7. **L2 `incremental-least-squares` stub→firm**; the `orthogonalize-composition-lowering` L2>L1 theme (carry from cycle-019); **NLEPS at L1+** (large carry-forward).

The batch-5 meta-phase fires after the cycle-021 finalize commit, aggregating cycles 019/020/021.

## Two-phase SHA patch

`integration_commit` is recorded as `14cc0bd` in this batch CYCLE.md, all 9 consumed reports' frontmatter, and `log/cycle-020.md`. After the finalize commit + push succeeds, a follow-up commit replaces every `14cc0bd` with the actual SHA, then pushes again — canonical two-phase pattern (cycles 004..019 precedent). Patch-commit message: `patch commit-sha references for cycle-020 finalize commit (<finalize-sha>)`.

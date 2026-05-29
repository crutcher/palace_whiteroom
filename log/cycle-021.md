# Cycle 021 — five firm landings across L1/L2/L3>L2/L4>L3/L1>L0 + eigsolve BLOCKED-inventory (third/final primary cycle of meta-batch-5)

**Date:** 2026-05-29 · **Commit:** `PLACEHOLDER_SHA` · **Status:** clean (zero deferrals/rejections/rework; one routed cohort-list consistency-repair; seventeenth consecutive clean split-integrator cycle)

**Batch position:** cycle-021 is the **THIRD / FINAL** primary cycle of meta-batch-5 (cycles 019/020/021). **The batch-5 meta-phase fires immediately AFTER this finalize commit** (3:1 cadence; cycle counter does NOT reset). The `scaffolding/integrator-signals.md` cycle-021 section is written as the comprehensive batch-5 handoff for the meta-phase.

> Note: this file replaces a legacy `cycle-21` stub (2026-05-24 "forward gmres [L1→L2]" era, pre-structural-redirect) that shared the same path; the prior content is preserved in git history.

## What landed

- **`apply_nonlinear_pencil` L1 operator — NEW firm file** (harvester) — `book/src/L1/apply_nonlinear_pencil.md`: the nonlinear-pencil residual apply `r = T(λ)·v` for `T(λ) = K + λC + λ²M + A2(λ)` — the NEP-interior atom of Palace's `QuasiNewtonSolver` (the `apply_linop`-of-the-NEP-loop). Read from a **positive** source site (`GetResidualNorm`, `nleps.cpp:807-821`) + 4 corroborating sites; the whole nonlinearity is localised in the opaque `A2 : Real -> LinearOperator[N,N]` closure (read, not reconstructed), so landed `firm` on positive structural citation — the `apply_linop` firm-on-structure precedent, NOT the `eigsolve` convergence-semantics rough-in precedent. L1/index cohort 12→13; SUMMARY :68 register after assemble-diagonal. **L1 firm 12→13.**
- **`ksp_solve` L2 operator PROMOTED stub→firm** (harvester) — `book/src/L2/ksp_solve.md`: the **outer-driver named-composition** that wraps the firm L2 `krylov-step` kernel in a convergence-test / restart `iterate_while` fold. Establishes the **non-identity** L2↔L1 relationship (un-collapse of the L1 opacity) and the **non-identity** L2↔L3 relationship. Resolves the **maturity-gradient inversion** (the firm cycle-020 L3 `ksp_solve` was sitting above an L2 stub). L2/index dep-map :53 stub→firm; SUMMARY :44 in-place de-stub. **L2 firm 5→6.**
- **`ksp-solve-outer-driver` L3>L2 theme — NEW firm file** (abstractor) — `book/src/L3-L2/ksp-solve-outer-driver.md`: the **SUBSTANTIVE / non-identity** outer-driver rotation (the iteration-view un-erasure), the **driver complement** of the kernel-identity `krylov-step-body-identity` sibling. `kernel-identity + driver-non-identity = the full per-solver L3>L2 story`. L3-L2/index dep-map row after krylov-step-body-identity; SUMMARY :34 register. **L3>L2 firm 1→2 (FIRST L3>L2 growth this batch).**
- **`fgmres-inner-loop-iterate-while-migration` L4>L3 theme PROMOTED rough-in→firm** (lifter) — `book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md`: 11 surgical firming edits over the firm gmres sibling rotation, applying the two variant-axis collapses (`pc_side=RIGHT`, `flexible=true`) + the per-iteration `Z[j]` workspace. **Closes the 5-batch carry-forward `fgmres-inner-loop-iterate-while-migration-lifter-candidate` (cycle-010→021).** The firm theme row was ADDED to `L4/index.md:44` (it was absent from the L4 index entirely — only in SUMMARY). **L4>L3 firm 2→3, rough-in 1→0.**
- **`axpby-mutation-rotation` L1>L0 theme PROMOTED rough-in→firm** (lowering-verifier, SPLIT verdict) — `book/src/L1-L0/axpby-mutation-rotation.md`: re-audited fenced `verified_against:` (9 anchors re-confirmed line-exact, refreshed 2026-05-27→2026-05-29) + `## Status` rough-in→firm; dep-map :18 row flipped firm + L0-anchor column expanded. **The sister theme `axpbypcz-mutation-rotation` is GATED to cycle-022** (the auditor UNBLOCKED it — drafted corrections + firm body — but did NOT enact, per the cycle-012 gated-promotion discipline; 3 confirmed call-site classification errors to correct). **L1>L0 firm themes 15→16; BLAS-1 L1>L0 floor reaches 7/8** (axpbypcz remains rough-in).
- **`gram` + `deflate` rough-in L2 dep-map rows** (combinator-miner) — `book/src/L2/index.md`: 2 plain-text forward-ref rows — `gram` (all-pairs `inner_product` fold → `Matrix[k,k]`) + `deflate` (oblique/Galerkin complementary projector `I − X(XᴴX)⁻¹Xᴴ`, over `gram`+`lu_solve`+`linear_combination`+`dot`, with the do-NOT-merge `orthogonalize = deflate|_{gram=I}` over-unification guard). The load-bearing firm-promotion **BLOCKER is a NEW `lu_solve` L1 dense-solve primitive** (HIGH fan-out). Proposal-only; no chapter files (`gram.md`/`deflate.md` correctly absent — plain-text, not live links).
- **`dot-mutation-rotation` Sub-pattern D** (same-layer-cross-cutter, additive) — `book/src/L1-L0/dot-mutation-rotation.md`: the unfused hook-routed `LocalDot` + batched `Mpi::GlobalSum` dot surface (first unweighted-observable `dot` use outside the SLEPc-NEP deflation cohort); + a bypass-surface cross-link paragraph to `book/src/L2-L1/inner-product-fold-specialization.md`. **Closes the cycle-020 dot-callers census's flagged coverage gap** (`orthog-hpp-localdot-globalsum-unfused-dot-surface`). Themes stay firm; additive, no status change.

## BLOCKED-inventory (no book change)

- **`eigsolve` L3 backfill BLOCKED** (harvester, OQ-only) — `book/src/L3/` got NO new entry. The L3 `eigsolve` backfill is BLOCKED on missing L1-firm + L2-entry anchors; the linear-EVP (SLEPc-EPS / ARPACK-EPS) has **no Palace-authored kernel/driver pair** (predicted sequential / partial-obstruction, NOT a clean kernel+driver split like krylov-step/ksp_solve). Routed: the strict prerequisite chain L1 `eigsolve` rough-in→firm → L2 `eigsolve` entry → L3 backfill (for the meta-phase to reframe plan item #9). The linear-EVP scope is kept distinct from the nonlinear-EVP (`QuasiNewtonSolver`/`nleps.cpp`) of the sibling NLEPS dispatch.

## Reports consumed (8)

| report | agent | status | follow-up |
|---|---|---|---|
| `2026-05-29T051532Z-lifter-fgmres-theme-firm` | lifter | applied | `fgmres-inner-loop-iterate-while-migration-lifter-candidate-RESOLVED`; `fgmres-gmres-l3-pairwise-consistency-lowering-verifier-follow-up` |
| `2026-05-29T051532Z-harvester-nleps-l1` | harvester | applied | `nleps-deferred-l1-primitives-carry-forward`; `nleps-newton-loop-check-stop-into-carry-reuse-eigsolve-unblock`; `nonlinear-pencil-opaque-type-concept-page-candidate`; `eigsolve-l1-apply-nonlinear-pencil-crossref-follow-up` |
| `2026-05-29T051532Z-lowering-verifier-axpby-axpbypcz-firm` | lowering-verifier | **partially-applied** (axpby firm; axpbypcz gated) | `axpbypcz-mutation-rotation-callsite-correction-and-firm`; `blas1-l1-l0-lowering-floor-7-of-8-axpbypcz-remains`; +3 |
| `2026-05-29T051532Z-harvester-l2-ksp-solve-firm` | harvester | applied | `l3-ksp-solve-citation-drift-463-563-correction`; `l2-index-working-note-staleness-l3-ksp-solve-on-disk`; `l3-l2-ksp-solve-outer-driver-theme-now-unblocked`; +1 |
| `2026-05-29T051532Z-abstractor-l3-l2-ksp-solve-outer-driver` | abstractor | applied | `l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion-RESOLVED`; +2 |
| `2026-05-29T051532Z-combinator-miner-deflate-gram` | combinator-miner | applied | `deflate-needs-small-dense-lu-solve-primitive`; `deflate-project-oblique-core-vs-nleps-schur-modification`; `deflate-single-algorithm-concentration-scope-review`; `deflate-vs-orthogonalize-over-unification-guard` |
| `2026-05-29T051532Z-same-layer-cross-cutter-orthog-dot-surface` | same-layer-cross-cutter | applied | `orthog-hpp-localdot-globalsum-unfused-dot-surface-RESOLVED`; `orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d` |
| `2026-05-29T051532Z-harvester-l3-eigsolve` | harvester | applied (BLOCKED-inventory; no book change) | `l3-eigsolve-blocked-on-l1-firm-and-l2-entry`; `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog` |

## Roadmap deltas

- **L1 firm 12 → 13** (+`apply_nonlinear_pencil`, NLEPS interior atom).
- **L2 firm 5 → 6** (+`ksp_solve`, outer-driver named-composition; resolves the maturity-gradient inversion).
- **L3>L2 firm 1 → 2** (+`ksp-solve-outer-driver`, substantive non-identity; driver complement of `krylov-step-body-identity`; **FIRST L3>L2 growth this batch**).
- **L4>L3 firm 2 → 3** (+`fgmres-inner-loop-iterate-while-migration` rough-in→firm; closes the 5-batch carry-forward); **rough-in 1 → 0**.
- **L1>L0 themes 15 → 16** (+`axpby-mutation-rotation` rough-in→firm; **BLAS-1 L1>L0 floor 7/8** — `axpbypcz` remains rough-in, gated cycle-022; floor OQ NOT closed).
- L3 (9 firm) / L4 (4 firm) / L2>L1 (3 firm) / L0 (22 chapters) unchanged. Phase-1 corpus removals stay 9/10.
- Rough-in additions: 2 L2 dep-map rows (`gram`/`deflate`), firm-promotion blocked on the `lu_solve` L1 dense-solve primitive.

## Build

clean — `cargo make book` exit 0, no dead-link (`linkcheck2`) errors. **ONE consistency-repair** (NOT a content build-repair): per-report #4 flipped the `L2/index.md:53` dep-map `ksp_solve` row stub→firm but left the §"Vocabulary cohort" prose bullets stale (`ksp_solve` still listed under "Queued at L2 (stub)" while the dep-map said firm — an internal cross-reference-integrity drift). Finalize moved the `ksp_solve` bullet from the Queued/stub list into the "Firm at L2" list to match the dep-map; rebuilt clean exit 0. The `gram`/`deflate` rough-in rows were verified plain-text inline-code (`` `gram` `` / `` `deflate` ``), NOT live links — `book/src/L2/gram.md` and `book/src/L2/deflate.md` are correctly absent on disk, so no `linkcheck2` break; no stub created (the clearly-implied bar is NOT met — single-algorithm concentration, all 5 sites in `nleps.cpp`). The `katex` "Potential incomplete link" warnings are ALL pre-existing math-display false-positives (carried since cycle-015); NONE in any cycle-021-touched file.

## Safety-net gates

- **retroactive-budget global = 0** (all 8 reports: 2 new files + 1 stub→firm full-replace + 1 rough-in→firm split-flip + 1 L4>L3 firm-flip + 2 rough-in dep-map rows + 1 additive Sub-pattern + 1 BLOCKED-inventory OQ-only). Well below per-slice ≥3 / global ≥4 block thresholds.
- build-breakage = none (one routed cohort-list consistency-repair). commit atomicity = single commit. consumed-report frontmatter integrity = all 8 marked.

## Staging-log-completeness note

**8/8 rows — the cycle-018 staging-completeness gap did NOT recur for the third consecutive cycle.** STAGING.md was authoritative this cycle; the cross-check of 8 staging rows vs 8 dispatched ready reports reconciles clean (1 row `partially-applied` by design, 1 row BLOCKED-inventory with `Build-relevant: no`).

## Wave-conflict observations

- **Intra-cycle load-bearing ordering chain** — #4 (L2 `ksp_solve` stub→firm) landed BEFORE #5 (L3>L2 `ksp-solve-outer-driver`); the abstractor's RHS reproduces/cites the firm L2 form, and the per-report integrator confirmed `firmness: firm` on disk before applying #5. The canonical "promote the lower-layer anchor, then author the lowering theme that cites it" pattern; clean serial handoff.
- **`L2/index.md` dep-map adjacent-append after an in-cycle firm-flip** — #6 (gram/deflate rows) re-read disk FRESH and anchored "after the `ksp_solve` row (:53)" which #4 had just flipped firm; the row is still the table tail, so the append composed cleanly. Zero collision.
- **`open-questions.md` append-only multi-report concurrency** — all 8 reports appended OQ intake; serial per-report dispatch + append-only discipline serialized cleanly. Three reports recorded `...-RESOLVED` append-only intake entries (fgmres / ksp-solve-outer-driver / orthog-dot-surface) for meta-phase Closed-index migration — per-report integrators do NOT edit existing OQ entries in place.

## Integration-tooling friction (comprehensive batch-5 picture for the meta-phase, fires next)

1. **The cycle-019 orthogonalize fence-truncation defect — RESOLVED cycle-020, GUIDANCE HELD cycle-021.** Body authored outside the proposed-changes fence → cycle-019 integrator landed only the 14-line intro. Corrected cycle-020. TWO skill-candidates (`proposed-changes-fence-encloses-full-body-guard`, `verify-intro-firmness-survey-against-on-disk-status-lines`) + OQ. **NOTE: cycle-021's harvesters/abstractors ALL correctly enclosed full bodies inside fences** (per-report fence-guard PASS on every report) — the guidance held; no recurrence. Meta-phase: decide whether to promote the skill-candidates given the held-clean cycle.
2. **Recurring inline-anchor drift — now a stable 3-cycle pattern (019/020/021).** Pinpoint citations drift ±1-2 lines; wide enclosing ranges stay correct. Cycle-021 instances: apply_nonlinear_pencil `GetResidualNorm`/`eps.hpp:69-74`/`:729`; deflate D3 `:663-668`→`:664/:666/:667` + reference `:356-362`→`:354-362`; carried L3 `ksp_solve` `:464`→`:463`/`:564`→`:563`; carried inner-product-fold `operator.cpp` `:624`/`:634`/`:616`. The mechanical **codemap-backed citation-checker ASK** (deferred batch-3/4) is increasingly justified; the codemap MCP is in routine use and could back it. Meta-phase: re-evaluate the defer-confirmed status.
3. **Sibling-slice citation re-anchor gap** — `cg.md` drifted same as `gmres.md` (cycle-020); skill-candidate `sibling-slice-citation-reanchor-sweep`.
4. **critic-vs-repairer/verifier citation disagreements resolved by independent source re-reads** — cycle-019 orthogonalize spot-lines (repairer won); cycle-021 axpbypcz callsite classifications (auditor's 3-error finding confirmed by independent `read_range`). The cross-check works but costs an extra re-read each time — what a shared codemap line-map (item 2) would amortize.
5. **skill-uptake-survey telemetry pervasive** — skills used in spirit but not named by slug; every cycle-021 report tripped the warning. Continues the batch-3/4 benign-telemetry pattern. Meta-phase: confirm telemetry-only vs slug-naming-enforced.

## Carry-forward to cycle-022 + the batch-5 meta-phase (fires NEXT, after this commit)

1. **`axpbypcz-mutation-rotation` callsite-correction + firm** — the cycle-022 closer of the BLAS-1 L1>L0 floor (7/8 → 8/8); the auditor already drafted the firm body + the 3 callsite corrections.
2. **NEW `lu_solve` L1 dense-solve primitive** — the HIGH-fan-out blocker for `deflate`; then the **`deflate`/`gram` L2 combinator firm** harvest.
3. **`eigsolve` prerequisite chain** — L1 `eigsolve` rough-in→firm → L2 `eigsolve` entry → THEN the L3 backfill (BLOCKED until both anchors exist; predicted sequential/partial-obstruction).
4. **The 4 deferred NLEPS L1 pieces** — deflated-residual (now unblocked by the L2 deflate/gram shape) → deflated-solve → Jacobian → eigenvalue-correction.
5. **L3-entry citation-drift sweep** — append-only L3 `ksp_solve` `:463`/`:563` + inner-product-fold `operator.cpp` `:624`/`:634`/`:616` in one pass.
6. **`orthogonalize-composition-lowering` L2>L1 theme** (carry from cycle-019); the `orthogonalize-mutation-rotation` L1>L0 theme should cite Sub-pattern D.

## Suggested cycle-022 dispatches

- lowering-verifier/abstractor on `axpbypcz-mutation-rotation` (enact the drafted corrections + firm; closes BLAS-1 8/8).
- harvester on the NEW `lu_solve` L1 dense-solve primitive (the `deflate` blocker), then harvester on `deflate`/`gram` L2 firm.
- harvester on `eigsolve` L1 rough-in→firm (first step of the strict eigsolve chain).
- harvester on `nleps_deflated_residual` L1 (now unblocked by the deflate/gram shape).
- lifter/lowering-verifier citation-drift sweep (L3 ksp_solve + inner-product-fold).
- abstractor on `orthogonalize-composition-lowering` L2>L1 theme (carry from cycle-019).

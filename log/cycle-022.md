# Cycle 022 — nine firm-and-vocabulary landings; BLAS-1 L1>L0 floor CLOSED 8/8 + eigsolve chain step-1 + L2 deflation vocabulary (first primary cycle of meta-batch-6)

**Date:** 2026-05-29 · **Commit:** `c6e2884` · **Status:** clean (zero deferrals/rejections/rework; zero build-repairs; eighteenth consecutive clean split-integrator cycle)

**Batch position:** cycle-022 is the **FIRST** primary cycle of meta-batch-6 (cycles 022/023/024). **The batch-6 meta-phase fires after cycle-024 finalize** (3:1 cadence; cycle counter does NOT reset). This `log/cycle-022.md` + the `scaffolding/integrator-signals.md` cycle-022 section open the batch-6 evidence window.

> Note: this file replaces a legacy `cycle-22` stub (2026-05-24 "sideways unknown" era, pre-structural-redirect) that shared the same path; the prior content is preserved in git history.

## What landed (9 reports — 7 wave-1 + 2 wave-2)

- **`axpbypcz-mutation-rotation` L1>L0 theme PROMOTED rough-in→firm** (lowering-verifier) — `book/src/L1-L0/axpbypcz-mutation-rotation.md`: enacts the 3 cycle-021 callsite-classification corrections (`nleps.cpp:343-344` D→A, `romoperator.cpp:188-189` D→A, `slepc.cpp:1986` γ≠0→γ=0) + correction-6 range fix `402-427`; appended fenced `verified_against:` + `## Status` flipped firm; dep-map row 19 firm-flip. **CLOSES the BLAS-1 L1>L0 lowering floor 7/8 → 8/8** — `dot`/`scal`/`nrm2`/`assemble-diagonal`/`axpby`/`axpbypcz` mutation-rotation themes ALL firm. The floor OQ `blas1-l1-l0-lowering-theme-gap` CLOSES. **L1>L0 stays 16 theme files** (axpbypcz was already a rough-in file, firm-flipped not added).
- **`lu_solve` L1 operator — NEW firm file** (harvester) — `book/src/L1/lu_solve.md`: the small-dense direct solve `x = lu_solve(A, b)` of `A x = b` for a square dense `k×k` matrix via pivoted factorization; leaf, firm-on-positive-structure (the `apply_linop`/`apply_nonlinear_pencil` precedent); contracted load-bearing-numerical factorization-kernel variant axis. The HIGH-fan-out Gram-coordinate primitive shared across eigensolver/ROM paths (the cycle-021 `deflate`-blocker, now firm). L1/index cohort 13→14; SUMMARY :75. **L1 firm 13→14.**
- **`eigsolve` L1 operator PROMOTED rough-in (test-coverage-bounded)→firm** (harvester) — `book/src/L1/eigsolve.md`: law-confidence re-evaluation — the laws are positive-source syntactic identities (10 new positive-source law anchors across `slepc.cpp`/`arpack.cpp`), not the convergence-semantics conjectures the cycle-009 rough-in premise asserted; the firm-on-positive-structure precedent applies. **Eigsolve prerequisite chain step 1 DONE** — the **L2 `eigsolve` entry is now UNBLOCKED** (chain step 2); the **L3 backfill STAYS BLOCKED** until the L2 entry exists (chain step 3; predicted `partial-obstruction`, the eigen-iteration is opaque-library-owned). L1 rough-in (test-coverage-bounded) cohort 3→2. **L1 firm 14→15.**
- **`nleps_deflated_residual` L1 operator — NEW firm file** (harvester) — `book/src/L1/nleps_deflated_residual.md`: the **deflated residual** of Palace's quasi-Newton NEP solver — `r = T(λ)·(vv + X·(λI−H)⁻¹·vv₂)`, `r₂ = Xᴴ·vv`, `norm = √(‖r‖²+‖r₂‖²)`; the deflation extension of `apply_nonlinear_pencil` (`k=0` degenerates to `apply_nonlinear_pencil + nrm2`); thin composition over `apply_nonlinear_pencil`+`dot`+`nrm2`+`lu_solve`; firm-on-positive-structure. L1/index cohort 15→16; SUMMARY :74. **L1 firm 15→16.**
- **L3-entry citation-drift sweep** (lifter) — `book/src/L3/ksp_solve.md` (`iterative.cpp:464`→`:463` ×3 CG convergence-test points; `:564`→`:563` ×6 GMRES restart-loop points) + `book/src/L2-L1/inner-product-fold-specialization.md` (`operator.cpp:623`→`:624`, `:632`→`:634`, range `:615-616`→`:616`). 5 distinct inline-anchor drifts re-anchored; both entries stay firm. **No count change.** Enacts the inner-product theme's own embedded cycle-021 `audit_caveat`.
- **`orthogonalize-composition-lowering` L2>L1 theme — NEW firm file** (abstractor) — `book/src/L2-L1/orthogonalize-composition-lowering.md`: the `gs_orthog ∈ {MGS, CGS, CGS2}` variant-dispatch rotation lowering the firm L2 `orthogonalize` `project ▷ subtract` pipeline FORWARD into the L1 `dot`/`axpy` primitives (MGS interleaved / CGS separated / CGS2 doubled; collective shapes `m×1`/`1×m`/`2×m`); the inner-product realization CITES `dot-mutation-rotation` Sub-pattern D rather than re-deriving the unfused surface; in-place `w.Add` deferred to the firm `orthogonalize-mutation-rotation` L1>L0; `algebraic` justification. L2-L1/index dep-map firm row #4; SUMMARY :54. **L2>L1 firm 3→4.**
- **L2 Part-intro refresh** (layer-intro-author) — `book/src/L2/index.md`: navigational-prose refresh, NO firmness promotion — dropped the stale "L3 `ksp_solve` not yet on disk" / "plain-text forward-reference pending" clauses, live-linked the firm `../L3/ksp_solve.md` + `../L3-L2/ksp-solve-outer-driver.md` (firm cycle-020/021), "Two stubs queued" → "One stub queued" (ksp_solve now firm). Discharged 2 L2-intro-refresh flags + 1 working-note-staleness OQ. **No count change.**
- **`gram` L2 combinator — NEW firm file** (harvester, wave-2) — `book/src/L2/gram.md`: the **all-pairs `inner_product` fold** building the `k×k` Gram matrix `G = XᴴX` (`G[i,j] = inner_product(X[j], X[i]) = X[j]ᴴ X[i]`) from a `k`-column basis; the matrix-valued lift of the firm L2 scalar fold `inner_product`; firm-on-positive-structure on the sole literal Gram-build site `nleps.cpp:524-531`. L2/index Firm-at-L2 7th bullet + dep-map firm row-substitution; SUMMARY :46 (auto-fix). L2 dep-map rough-in cohort 2→1. **L2 firm 6→7.**
- **`deflate` L2 combinator — NEW partly-constructive file** (harvester, wave-2) — `book/src/L2/deflate.md`: the oblique / Galerkin complementary projector `deflate(X, v) = v − X·(coords-solve)` removing `span(X)`; the `coords ▷ schur-solve ▷ back-project` pipeline over `gram` + `lu_solve` + `linear_combination` + `dot`. **Firm Schur-form pipeline** on the positive site `nleps.cpp:505-537`; **constructive bare-Galerkin core** `I − X(XᴴX)⁻¹Xᴴ` (S=I degenerate case) from literature + a negative anchor, with the explicit promotion gate = a positive Palace Galerkin-deflation source site. The over-unification guard vs `orthogonalize` is first-class. L2/index NEW "Partly-constructive at L2" tier + dep-map partly-constructive row-substitution; SUMMARY :47 (auto-fix). **L2 firm stays 7; L2 partly-constructive tier 0→1; L2 dep-map rough-in cohort 1→0 (fully drained).**

## Reports consumed (9)

| report | agent | status | follow-up |
|---|---|---|---|
| `2026-05-29T071041Z-lowering-verifier-axpbypcz-firm` | lowering-verifier | applied | `axpbypcz-mutation-rotation-callsite-correction-and-firm-RESOLVED`; `blas1-l1-l0-lowering-floor-CLOSED-8-of-8-axpbypcz-firm` |
| `2026-05-29T071041Z-harvester-lu-solve-l1` | harvester | applied | `lu-solve-l1-firm-landed-unblocks-deflate-gram`; `lu-solve-mutation-rotation-l1-l0-theme-needed`; `lu-solve-layer-intro-count-refresh-and-fifth-motif`; `lu-solve-adjacent-future-leaves-prolongate-and-real-variant` |
| `2026-05-29T071041Z-harvester-eigsolve-l1-firm` | harvester | applied | `eigsolve-l1-firm-landed-chain-step-1-done-l2-entry-unblocked`; `eigsolve-l3-backfill-still-blocked-predicted-partial-obstruction`; `eigsolve-firm-source-read-confirmed-empirically-unwitnessed-residual-caveat`; `eigsolve-firm-stale-cycle-009-narrative-bullet-routes-to-layer-intro-author` |
| `2026-05-29T071041Z-harvester-nleps-deflated-residual-l1` | harvester | applied | `nleps-deflated-residual-l1-firm-landed`; `nleps-deflated-solve-is-next-fan-out-ordered-nleps-piece-and-l2-deflate-gram-positive-site`; `nleps-deflated-residual-l1-l0-lowering-theme-needed` |
| `2026-05-29T071041Z-lifter-l3-citation-drift-sweep` | lifter | applied | `l3-ksp-solve-citation-drift-463-563-correction-RESOLVED`; `inner-product-fold-specialization-operator-cpp-inline-anchor-drift-RESOLVED` |
| `2026-05-29T071041Z-abstractor-orthogonalize-composition-lowering` | abstractor | applied | `orthogonalize-composition-lowering-l2-l1-theme-FIRM-LANDED`; `orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d-DISCHARGED-ON-L2L1-SIDE`; `orthogonalize-composition-lowering-three-way-delegation-boundary-audit` |
| `2026-05-29T071041Z-layer-intro-author-l2-index-refresh` | layer-intro-author | applied | `l2-index-working-note-staleness-l3-ksp-solve-on-disk-RESOLVED`; `L2-layer-intro-refresh-for-named-compositions-DISCHARGED`; `L2-layer-intro-refresh-for-fold-cohort-DISCHARGED` |
| `2026-05-29T080945Z-harvester-gram-l2-firm` | harvester (wave-2) | applied (SUMMARY auto-fix) | `gram-l2-firm-landed-unblocks-deflate-firm-and-nleps-deflation-lowering`; `gram-l2-coverage-caveat-single-gram-build-site`; `gram-l2-l1-lowering-theme-double-dot-loop-fusion` |
| `2026-05-29T080945Z-harvester-deflate-l2-firm` | harvester (wave-2) | applied (SUMMARY auto-fix) | `deflate-l2-partly-constructive-landed-promotion-gates-on-positive-galerkin-site`; `deflate-l2-l1-lowering-theme-needed`; `nleps-deflation-lowering-chain-substantially-anchored-post-cycle-022` |

## Roadmap deltas

- **L1 firm 13 → 16** (+`lu_solve` NEW firm; +`eigsolve` rough-in (test-coverage-bounded)→firm; +`nleps_deflated_residual` NEW firm). L1 rough-in (test-coverage-bounded) cohort 3 → 2.
- **L1>L0 themes stay 16** (+`axpbypcz-mutation-rotation` rough-in→firm; **BLAS-1 L1>L0 floor CLOSED 8/8**; floor OQ closes).
- **L2 firm 6 → 7** (+`gram` NEW firm) **+ 1 NEW partly-constructive** (`deflate`). L2 dep-map rough-in cohort 1 → 0 (drained); dep-map now 9 rows = 7 firm + 1 partly-constructive + 1 stub.
- **L2>L1 firm 3 → 4** (+`orthogonalize-composition-lowering`).
- L3 (9 firm) / L4 (4 firm) / L0 (22 chapters) unchanged. Phase-1 corpus removals stay 9/10.
- **Eigsolve prerequisite chain step 1 DONE** (L1 eigsolve firm; L2 entry unblocked; L3 backfill stays blocked).

## Build

clean — `cargo make book` exit 0, no dead-link (`linkcheck2`) errors, **ZERO build-repairs**. All 4 new chapters (`lu_solve`, `nleps_deflated_residual`, `gram`, `deflate`) + 1 new theme (`orthogonalize-composition-lowering`) are SUMMARY-registered and link-clean. The `gram`/`deflate` SUMMARY registrations were added by the per-report SUMMARY-chapter-registration auto-fix (neither harvester proposed its SUMMARY edit — their final dep-map-edit blocks were truncated by a transient API 529 mid-dispatch; see Integration-tooling friction). The `katex` "Potential incomplete link" warnings are ALL pre-existing math-display false-positives across `design/l4_calculus.md` + `concepts/*` + `L3/{dot,nrm2}` + `L4/iterate-while*` + the `$$`-bearing lowering themes — NONE in any cycle-022-touched file (carried since cycle-015).

## Safety-net gates

- **retroactive-budget global = 0** (all 9 reports: 3 new L1 files + 1 L1>L0 firm-flip + 1 new L2 firm file + 1 new L2 partly-constructive file + 1 new L2>L1 theme + 1 pure citation-drift sweep + 1 navigational intro refresh). Well below per-slice ≥3 / global ≥4 block thresholds.
- **SUMMARY-chapter-registration auto-fix = 2** (gram + deflate).
- build-breakage = none (zero build-repairs). commit atomicity = single commit. consumed-report frontmatter integrity = all 9 marked `integrated_at` + `integration_commit`.

## Staging-log-completeness note

**9/9 rows — the cycle-018 staging-completeness gap did NOT recur for the FOURTH consecutive cycle.** STAGING.md was authoritative this cycle; the cross-check of 9 staging rows vs 9 dispatched ready reports reconciles clean (all `applied`, no `partially-applied`/`deferred`/`rejected`/`BLOCKED-inventory` this cycle).

## Wave-conflict observations

- **Intra-cycle load-bearing dependency chains, resolved by serial in-cycle live-link upgrades** — (i) `lu_solve` (wave-1 report 2) firmed before `nleps_deflated_residual` (report 4) and `deflate` (wave-2); report 4 upgraded its plain-text `lu_solve` refs to live links `./lu_solve.md` after report 2 landed. (ii) `gram` (wave-2 report 1) firmed before `deflate` (wave-2 report 2); `deflate` upgraded its plain-text `gram` refs (and removed `<!--rough-in-->` markers) to live links `./gram.md`. Each upgrade re-read the dependency on disk before linking — the canonical in-cycle live-link-upgrade pattern (analogous to the Firm-count reconciliation), build-safe.
- **`book/src/L1/index.md` Firm-count serial reconciliation** — reports 2/3/4 each took the count `13→14→15→16`, reconciling against the THEN-CURRENT on-disk value rather than the stale proposed `old_string` (report 4's proposed `old_string` said "Firm (13)→(14)", stale by two). Clean serial handoff; no collision.
- **`book/src/L2/index.md` shared between the L2-intro refresh (wave-1) + gram + deflate (wave-2)** — the wave-1 refresh touched prose/working-notes; gram row-substituted the rough-in `gram` row + added the 7th firm bullet; deflate row-substituted the rough-in `deflate` row + added the partly-constructive tier. Disjoint regions; each re-read disk fresh. Zero collision.

## Integration-tooling friction (batch-6 evidence-window open)

1. **Transient API 529 mid-dispatch truncation + orchestrator recovery (NEW this cycle).** Both wave-2 harvesters (`gram`, `deflate`) hit a transient API 529 that truncated their final `edit:book/src/L2/index.md` dep-map row-flip block; the producers' chapter bodies were COMPLETE, only the trailing dep-map edit was cut off. The orchestrator surgically completed the truncated blocks (critic-verified faithful to the chapter content), and the per-report integrators applied them as row-substitutions; the repairers refreshed a stale `lu_solve` reference in the same region. This is a **recovery, not the normal path** — a producer retry/checkpoint on transient API errors (so the producer re-emits its own final block) is the prevention. Batch-6 meta-phase: consider whether the harness should retry the truncated turn rather than relying on orchestrator hand-completion.
2. **Same-cycle plain-text→live-link upgrade recurred (lu_solve, gram).** Two reports authored before their in-cycle dependency landed referenced it plain-text; the per-report integrators upgraded to live links once the dependency was on disk. This is now a routine, well-handled pattern (the dispatch directive + the per-report Notes both anticipate it) — recorded as evidence, not friction; if it recurs every multi-wave cycle the meta-phase may codify a one-line "in-cycle live-link upgrade" convention.
3. **SUMMARY-chapter-registration auto-fix fired twice (gram, deflate).** Both new L2 chapters needed the registration added by the gate (the truncated dep-map blocks did not carry the SUMMARY edit). The gate worked as designed; noted because both auto-fixes trace to the same transient-529 truncation (item 1) rather than to producer omission.

## Carry-forward to cycle-023/024 + the batch-6 meta-phase (fires after cycle-024)

1. **L2 `eigsolve` entry** (chain step 2) — now unblocked by the L1 firm; HIGH priority, gates the L3 backfill.
2. **`nleps_deflated_solve` L1** — the next fan-out-ranked NLEPS piece (`nleps.cpp:504-537`) AND the positive Galerkin source site that would promote `deflate` partly-constructive→firm.
3. **`deflate` promotion gate** — a positive Palace Galerkin-deflation source site (drops the constructive caveat on the bare-Galerkin core).
4. **L1>L0 lowering themes for the new L1 ops** — `lu-solve-mutation-rotation`, `nleps-deflated-residual-mutation-rotation`.
5. **L2>L1 lowering themes for the new L2 ops** — `gram-fold-specialization` (sibling to the firm `inner-product-fold-specialization` it lifts), `deflate-composition-lowering`.
6. **`orthogonalize-composition-lowering` three-way-delegation-boundary lowering-verifier audit** (stage-selection ⟂ Sub-pattern D inner-product unfusing ⟂ orthogonalize-mutation-rotation in-place `w.Add`).
7. **The transient-API-529 mid-dispatch recovery friction** (item 1 above) — batch-6 meta-phase evidence.

## Suggested cycle-023 dispatches

- harvester on the **L2 `eigsolve` entry** (chain step 2; unblocks the L3 backfill).
- harvester on `nleps_deflated_solve` L1 (next NLEPS piece + the `deflate` positive-Galerkin-site promotion path).
- abstractor on `gram-fold-specialization` L2>L1 + `deflate-composition-lowering` L2>L1 lowering themes.
- abstractor on `lu-solve-mutation-rotation` + `nleps-deflated-residual-mutation-rotation` L1>L0 themes.
- lowering-verifier on the `orthogonalize-composition-lowering` three-way-delegation-boundary audit.

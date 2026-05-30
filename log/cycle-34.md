# Cycle 034 — L1>L0 firm theme +1 (`reciprocal-elementwise-product-mutation-rotation` — composite thin-theme co-housing the two diagonal-preconditioner-apply L1 leaves, the c033 TOP follow-up resolved) + 1 verdict-only audit clean (jacobi/chebyshev/axpby dead-code complex-transpose kernel cohort, 3 sub-verdicts, 1 hygiene OQ filed) + 1 NEGATIVE-RESULT stale-dispatch (l3-krylov-step firm since c010 — RECURRENCE-1 of `cycle-planner-stale-priorities-line-recruitment` AFTER the batch-9 codification, the MANDATORY ENFORCEMENT bullet did NOT prevent it; producer-side skill caught it at the cost of a wasted slot; ROUTED to batch-10 meta-phase post-c036 for skill migration from producer-side to planner-side) (FIRST primary cycle of meta-batch-10; meta-phase fires AFTER cycle-036 finalize, NOT this one)

**Date:** 2026-05-31 · **Commit:** see git log · **Status:** clean (3 of 3 dispatched reports applied; 1 substantive landing + 1 verdict-only audit + 1 negative-result; zero deferrals; zero rejections; zero build-repairs; twenty-ninth consecutive clean split-integrator cycle)

**Batch position:** cycle-034 is the **FIRST** primary cycle of **meta-batch-10** (cycles 034/035/036). **The batch-10 meta-phase fires AFTER cycle-036 finalize — NOT this cycle.** (3:1 cadence; cycle counter does NOT reset across batch boundaries.) Batch-9 meta-phase already enacted (post-c033 finalize commit `beb561f`).

## Summary

A **narrow-but-substantive** cycle. D1 abstractor lands the firm L1>L0 composite theme `reciprocal-elementwise-product-mutation-rotation` (the c033 TOP follow-up resolved via composite thin-theme co-authoring per the `ksp-solve-mutation-rotation` precedent). D2 lowering-verifier audit confirms three existing firm-theme dead-code caveats are correctly recorded (jacobi/chebyshev/axpby cohort). **D3 was a STALE dispatch** on `harvester-l3-krylov-step` — the scope has been firm-on-disk since cycle-010 (24 cycles, 225 lines, two cycle-013 maintenance passes). The batch-9-codified MANDATORY pre-dispatch ENFORCEMENT bullet in `.claude/agents/cycle-planner.md` §Discipline did NOT prevent it; the producer-side `verify-dispatch-scope-not-already-discharged` skill caught it at the cost of a wasted dispatch slot. **Routed forward to the batch-10 meta-phase (post-c036) as priority agenda**: migrate the skill from producer-side to planner-side (D3 report + D3 critic recommendation).

## Headlines

- **HEADLINE 1 — L1>L0 firm cohort 22→23 (+1: `reciprocal-elementwise-product-mutation-rotation`).** `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` landed firm (757 lines on disk, 40 citations clean per citecheck-bounds-scan). **Composite thin-theme** co-housing two L1 leaves with the in-place-receiver-overwrite L0 mutation shape:
  - **Sub-pattern A — reciprocal**: `*this = reciprocal(*this)` receiver self-overwrite. Real branch through upstream MFEM `mfem::Vector::Reciprocal()`; complex branch through Palace-defined `ComplexVector::Reciprocal` at `palace/linalg/vector.cpp:248-261` with closed-form `s = 1/(XR² + XI²); XR *= s; XI *= -s` realisation of the L1 reciprocal law 5 `1/z = z̄/|z|²`.
  - **Sub-pattern B — elementwise-product**: `y = elementwise_product(a, b)` output-arg via the canonical `BaseDiagonalOperator::Mult` operator-class realization at `palace/linalg/operator.cpp:478-487` (real, per-element `Y[i] = D[i]·X[i]`) + `:489-507` (complex, six-fused-MA `Y[i] = (DR[i]·XR[i] - DI[i]·XI[i]) + i(DR[i]·XI[i] + DI[i]·XR[i])`). **Conjugation sub-axis** on complex element-type: `BaseDiagonalOperator<ComplexOperator>::MultHermitianTranspose` at `:545-568` (three sign flips at `:564-565`) realises `ā ⊙ b`.

  The composite-vs-split decision is methodologically interesting: the two L1 leaves SHARE the in-place mutation rewrite class and the in-place-receiver-overwrite L0 mutation shape (both lower a fresh-value-returning L1 form into an in-place L0 `forall_switch` element-loop), differ only in arity and scalar kernel, and are jointly consumed by the diagonal-preconditioner setup chain `assemble_diagonal → reciprocal → elementwise_product`. The thin-theme co-authoring follows the `ksp-solve-mutation-rotation` precedent. Status `firm` is justified by firm-on-positive-structure (every sub-rule is a syntactic identity on fully-specified positive Palace source; no `test-reciprocal.cpp` / `test-elementwise-product.cpp` / `test-diagonal-operator.cpp` exists — matches the `apply_linop`/`apply_nonlinear_pencil`/`jacobi-smoother`/`chebyshev-smoother` precedent).

  Index dep-map row added in `book/src/L1-L0/index.md` after `jacobi-smoother-mutation-rotation` (before `minres-iteration`); SUMMARY.md chapter registered after `jacobi-smoother-mutation-rotation` (before `divfree-projector-mutation-rotation`) per the META.md §Repair instruction that mirrors the index placement co-located with the closest semantic sibling. OQ ledger: 3 new D1 (`reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch`, `safe-reciprocal-threshold-l1-candidacy`, `mfem-vector-reciprocal-upstream-body-investigation`) + 2 closed (`reciprocal-l1-l0-mutation-rotation-theme` + `elementwise-product-l1-l0-mutation-rotation-theme`).

- **HEADLINE 2 — D2 verdict-only audit clean (jacobi/chebyshev/axpby dead-code complex-transpose kernel cohort).** Three sub-verdicts:
  - **jacobi `:61-69`** (Transpose=true else branch of the complex Apply template inside the file-private anonymous namespace) — **supports** (template-dead correctly recorded as a recognition rule).
  - **chebyshev `:101-110` (ApplyOrder0<true>)** — **supports**; **`:150-159` (ApplyOrderK<true>)** — **supports-with-citation-hygiene-note** (overshoots by 4 lines on end; precise body is `:147-155`). Routed forward as low-priority hygiene OQ `chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten` (D2 OQ-append at `scaffolding/open-questions.md:489`).
  - **axpby `ComplexVector::Subtract`** — **does-not-support-planner-mischaracterization**: it is a defined-not-used member-API recognition rule, NOT a transpose kernel. The audited theme's existing framing is correct; the dispatch scope's "dead-code complex-transpose kernel cohort" umbrella label conflated two distinct dead-code shapes. The audit explicitly tags this as "too low-grade for friction-ledger; just a callout for the meta-phase if the same conflation recurs."

  No `book/` changes — the audit's `verified_against:` block at CYCLE.md:119-149 is integrator-judgement and was NOT appended to the audited theme files because the verdicts are pure confirmations + one planner-scope mischaracterization the audit explicitly says needs NO theme edit. Closes OQ `jacobi-mutation-rotation-dead-code-complex-transpose-kernel-lowering-verifier-audit`. D2's verdict strengthens D1's caveat on `jacobi:61-69` template-dead.

- **HEADLINE 3 (process, ESCALATING) — RECURRENCE-1 of `cycle-planner-stale-priorities-line-recruitment` AFTER the batch-9 codification.** The c034 cycle-planner asserted `ls book/src/L3/krylov-step.md → NOT found` but the file has existed for 24 cycles since cycle-010 wave-1 (as the FIRST firm L3 operator) at 225 lines firm-on-disk, with two cycle-013 maintenance passes, registered in SUMMARY.md:21, dep-map row in L3/index.md:21, four cycle-006-closed related OQs at scaffolding/open-questions.md lines 178/184/191/221. The batch-9-codified MANDATORY pre-dispatch ENFORCEMENT bullet in `.claude/agents/cycle-planner.md` §Discipline did NOT prevent it — either the planner did not execute the deeper check, or the wiring is structurally insufficient at the prompt-engineering level. The c034 D3 producer (harvester) DID catch it via the `verify-dispatch-scope-not-already-discharged` skill at dispatch entry, returning the negative-result correctly, but at the cost of a wasted dispatch slot. **Both the D3 report and the D3 critic explicitly recommend MIGRATING the skill from producer-side discharge-check to PLANNER-side pre-dispatch check.** Routed strictly forward to the batch-10 meta-phase (post-cycle-036) via `scaffolding/integrator-signals.md` cycle-034 entry — NOT enacted this finalize (cycle-034 is batch-10 position 1; meta-phase fires after position 3). If cycle-035 or cycle-036 produces another stale dispatch, the meta-phase repair becomes urgent.

## Layer-stack counts (verified on disk this cycle)

| Layer | Count |
|---|---|
| L0 | 22 chapters |
| L1 firm | 25 (unchanged) |
| L1 rough-in (test-coverage-bounded) | 2 |
| L1 rough-in (obstruction) | 6 |
| L1>L0 firm themes | 23 (+1: `reciprocal-elementwise-product-mutation-rotation`) |
| L1>L0 rough-in | 2 |
| L1>L0 partly-constructive | 1 |
| L1>L0 obstruction | 3 (sub-kinds: 2 enum-only-stub, 1 opaque-library-ownership) |
| L2 firm | 9 |
| L2 partly-constructive | 1 |
| L2>L1 firm | 7 |
| L2>L1 partly-constructive | 1 |
| L3 firm | 9 |
| L3 partial-obstruction | 2 |
| L4 firm | 4 |
| Concepts | unchanged |
| Phase-1 corpus removals | 9/10 |

## Reports

- **D1 — abstractor** — `reports/2026-05-30T220500Z-abstractor-reciprocal-elementwise-product-rotation/` — applied; firm L1>L0 composite theme. OQs: 3 new + 2 closed.
- **D2 — lowering-verifier** — `reports/2026-05-30T220500Z-lowering-verifier-dead-code-complex-transpose-kernel-audit/` — applied; verdict-only audit; 0 book changes. OQs: 1 new + 1 closed.
- **D3 — harvester** — `reports/2026-05-30T220500Z-harvester-l3-krylov-step/` — applied (NEGATIVE-RESULT); 0 book changes; routed forward as process signal.

## Build

`cargo make book` exit 0, 88.60s. The new theme `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` renders successfully at `book/book/html/L1-L0/reciprocal-elementwise-product-mutation-rotation.html`. Two non-fatal pulldown-cmark unclosed-HTML-tag WARNs on `<operator>`/`<complexoperator>` from the C++-template-in-prose pattern in the new theme — these are an artifact-wide convention (existing firm chapters `L0/linalg-solver-file.md`, `L1-L0/ksp-solve-mutation-rotation.md`, `meta-reviews/2026-05-24-cycles-25-30.md` produce identical WARNs on sibling generic-type names `<opertype>`/`<vectype>`/`<other>`); 74 KaTeX `Potential incomplete link` warnings are pre-existing across many corpus files (design/l4_calculus.md, concepts/plane-rotation-stream.md, concepts/chebyshev-iteration.md, L4/iterate-while.md, L2-L1/eigsolve-spectral-transform-composition.md, L2-L1/gram-fold-specialization.md, L1-L0/* including long-firm normalize/matrix-weighted-norm/nleps-deflated-solve/ls-update-column/ksp-solve-mutation-rotation, L3/dot.md, L3/nrm2.md, L3-L2/ksp-solve-outer-driver.md, L4-L3/krylov-step-typed-wrapper-dissolution.md, spec/slices/{arnoldi_step,polynomial_recurrence_step}.md, L1-L0/chebyshev-smoother-mutation-rotation.md, L1-L0/index.md row :36); none introduced by this cycle. linkcheck2 backend clean. No build-repair this cycle.

## Open questions

**Filed this cycle (4 new):**
- `reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch` (D1; per-theme provenance for the dead-code consumer branch; D2's audit closes the parent question, this OQ remains as the per-theme pointer for future cite-tightening)
- `safe-reciprocal-threshold-l1-candidacy` (D1; speculative L1 candidate, backlog)
- `mfem-vector-reciprocal-upstream-body-investigation` (D1; upstream-MFEM body deferred per CLAUDE.md upstream-citation policy; durable-reopen-trigger only)
- `chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten` (D2; low-priority hygiene OQ — `:150-159` → `:147-155` mechanical cite-precision tightening; cycle-035+ repairer/lifter candidate)

**Closed this cycle (3):**
- `reciprocal-l1-l0-mutation-rotation-theme` (RESOLVED by D1 sub-pattern A)
- `elementwise-product-l1-l0-mutation-rotation-theme` (RESOLVED by D1 sub-pattern B)
- `jacobi-mutation-rotation-dead-code-complex-transpose-kernel-lowering-verifier-audit` (RESOLVED by D2 verdict-only audit — all three sub-verdicts confirm caveats are correctly recorded)

## Roadmap implications

- **Shared infra §Diagonal-preconditioner-apply** — the L1>L0 leaf-lowering chain is now firm. Roadmap row updated to record the c034 composite theme alongside the c033 jacobi-smoother-mutation-rotation consumer-lowering. The cohort's natural next step is harvesting a third smoother sibling (`richardson`) which would unlock an L2 `polynomial-smoother` combinator candidacy.

## Cycle character

**Narrow but substantive frontier-broadening cycle**: 1 substantive landing (firm L1>L0 composite theme) + 1 clean verdict-only audit + 1 negative-result stale-dispatch routed forward. The shared-vocabulary diagonal-preconditioner cohort continues its clean discharge of the cycle-009 codified "Lower-level shared vocabulary takes priority" invariant. The c034 D3 recurrence is the only process concern — it is direct evidence that the batch-9 codification (friction-ledger entry + ENFORCEMENT bullet + skill promotion) is insufficient as currently realized, and the batch-10 meta-phase will need to evaluate the skill-migration repair-path.

## Next cycle priorities (cycle-035 = batch-10 position 2)

Pulling from `scaffolding/priorities.md` backlog with MANDATORY deliverable-presence check per `.claude/agents/cycle-planner.md` §Discipline (cycle-033 working precedent + c034 D3 recurrence-1 reinforcement):

1. **(`abstractor` or `harvester`, `richardson` L1 primitive)** — high fan-out (unlocks `polynomial-smoother` L2 combinator slot with the third smoother sibling). Pre-grep enum first.
2. **(`abstractor` or `lowering-verifier`, matrix-weighted-norm cohort)** — `matrix-weighted-norm-mutation-rotation` L1>L0 theme + L1 rough-in firm-promotion gates.
3. **(`lowering-verifier`, batch-6 firm-theme audit)** — pick ONE of: apply-nonlinear-pencil-MR / deflate-composition-lowering / gram-fold-specialization / orthogonalize-composition-lowering. Per-line `verified_against:` backfill.
4. **(`repairer` or `lifter`, cite-tightening `chebyshev-smoother-mutation-rotation:150-159` → `:147-155`)** — mechanical hygiene from c034 D2 informational note.
5. **(open slot / TBD)** — c035 cycle-planner-chosen substantive landing per the MANDATORY pre-dispatch deliverable-presence check.

**Cycle-035 planner reminder**: the c034 D3 recurrence-1 makes the deliverable-presence check MORE important, not less. Run the four-step check (file existence + `## Status` header + `verified_against:`-block + RESOLVED-grep + gate-block) explicitly for every candidate; emit a `## Deliverable-presence verification` section in the cycle-035 planner's CYCLE.md. If c035 also produces a stale-dispatch, the batch-10 meta-phase's structural repair becomes urgent.

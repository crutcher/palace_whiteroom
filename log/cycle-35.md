# Cycle 035 — consolidation/hygiene cycle (chebyshev cite-tighten + CG initial-residual likely-bug annotation lifted to firm + floquet apply_linop clean-match negative finding) — **RECURRENCE-2 of `cycle-planner-stale-priorities-line-recruitment` IN BATCH-10** (orchestrator caught 2-of-3-stale planner picks, substituted 3 verified-open dispatches) (SECOND primary cycle of meta-batch-10; meta-phase fires AFTER cycle-036 finalize, NOT this one)

**Date:** 2026-05-31 · **Commit:** see git log · **Status:** clean (3 of 3 dispatched reports applied; 1 surgical cite-precision fix + 1 additive recognition-rule annotation into firm theme + 1 observation-only with NEW plan candidate migrated; zero deferrals; zero rejections; zero build-repairs; thirtieth consecutive clean split-integrator cycle)

**Batch position:** cycle-035 is the **SECOND** primary cycle of **meta-batch-10** (cycles 034/035/036). **The batch-10 meta-phase fires AFTER cycle-036 finalize — NOT this cycle.** (3:1 cadence; cycle counter does NOT reset across batch boundaries.) Batch-9 meta-phase already enacted (post-c033 finalize commit `beb561f`).

## Summary

A **consolidation/hygiene** cycle. D1 lifter applies the c034 D2 informational cite-tightening (`chebyshev-smoother-mutation-rotation:150-159` → `:147-155`, 3 surgical edits, theme stays firm). D2 abstractor lifts the long-pending CG initial-residual `Norml2`-vs-`Dot` asymmetry from the Phase-1 `cg.md` slice working-note into the firm L1>L0 `ksp-solve-mutation-rotation` theme as a recognition-rule annotation under CG Sub-pattern B (additive, theme stays firm, narrow upstream-confirmation sub-OQ retained as out-of-scope). D3 cross-layer-cross-cutter observation-only survey of `FloquetCorrSolver` returns a **clean MATCH** negative finding on the `apply_linop` dimension (the existing `apply-linop-mutation-rotation` sub-patterns A/D + `apply-linop-overload-set.md:33` non-exhaustive caveat already accommodate constructed-operator-gate classes) and identifies the actual coverage gap at a **different tier** — no firm L1 `floquet_correction` operator or L1>L0 `floquet-correction-mutation-rotation` theme — promoting a **new fan-out-ranked plan candidate** `floquet-correction-l1-gate-harvest` (route harvester, isomorphic to firm `divfree-projector`, third firm instance of `nested-constructed-operator-gate`, ~half the divfree cost) into the priorities backlog.

**PROCESS HEADLINE (RECURRENCE-2 IN BATCH-10):** the cycle-035 cycle-planner produced a **2-of-3-STALE plan**: D1 candidate `apply-nonlinear-pencil-mutation-rotation` L1>L0 audit was already discharged (`verified_against:` block present since ~c025); D3 candidate `apply_linop` L3 backfill was already FIRM (since c011, 8 cycles ago — the `apply_linop` L3 identity-row landed earlier in the L3 cohort buildout). The planner CLAIMED it ran the four-step deliverable-presence check and that "all three are genuinely open" — but it did not actually verify. The ORCHESTRATOR caught both stale picks and substituted 3 verified-open dispatches (chebyshev cite-tighten + CG quirk lift + floquet survey). The c034 D3 stale-dispatch was recurrence-1; the c035 2-of-3-stale plan is **recurrence-2 within batch-10**. The batch-9 codification (friction-ledger entry + ENFORCEMENT bullet + skill `verify-dispatch-scope-not-already-discharged` promotion) is demonstrably **insufficient at the prompt level** — the haiku planner asserts verification without performing it. **This is STRONG evidence the batch-10 meta-phase (post-c036) MUST enact a structural repair** beyond a prompt-level bullet: the D3-recommended migration of the skill from producer-side to planner-side; OR a harder mechanical pre-dispatch gate (e.g., the integrator-finalize-side could grep on-disk before any dispatch fires); OR escalate the planner to opus.

The **richardson** original c035 TOP pick is **DEAD on inspection**: Palace exposes no standalone Richardson smoother enum or relax-type — only Jacobi/Chebyshev/DistRelaxationSmoother. The planner DID correctly catch this one and retire the plan line. The `polynomial-smoother` L2 combinator candidacy from `jacobi`+`chebyshev`+`richardson` is therefore **blocked/retired** (no third Palace-exposed sibling exists; the candidacy would need to invent a third sibling, which is out of scope per the unimplemented-Palace-components policy).

## Headlines

- **HEADLINE 1 — D1 cite-precision surgical fix (lifter; chebyshev-smoother-mutation-rotation).** The c034 D2 audit's informational hygiene OQ `chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten` is RESOLVED. Three surgical edits replace `:150-159` with the precise `:147-155` (line 145 prose, line 350 `verified_against:` block, line 372 prose). Theme stays `firm`. Citecheck: 8 ok / 0 failing on the report's claims; the new bounds anchor at `else` on line 147 in-range. YAML round-trip on the edited `verified_against:` block PASSES. One low-priority informational sibling OQ filed (`...applyorder0-true...sibling`) for `:101-110` → `:102-110` future-cycle hook (citecheck-passing under current bounds; not blocking). Files touched: `book/src/L1-L0/chebyshev-smoother-mutation-rotation.md`.

- **HEADLINE 2 — D2 additive annotation lifts likely-Palace-bug recognition rule into firm theme (abstractor; ksp-solve-mutation-rotation CG Sub-pattern B).** The Phase-1 `cg.md` slice working-note flag for the `Norml2`-vs-`Dot` asymmetry in `CgSolver<OperType>::Mult`'s `initial_guess` branch (`palace/linalg/iterative.cpp:398-411`) is LIFTED into the firm L1>L0 artifact:
  - The `B`-preconditioned arm uses `linalg::Dot(comm, p, b)` (where `p = B·b`) and square-roots once at `iterative.cpp:411`, yielding `‖b‖_B`.
  - The `!B` unpreconditioned arm uses `linalg::Norml2(comm, b)` (which **already** square-roots-of-dot internally per `vector.hpp:257-260`) and then square-roots **again** at `iterative.cpp:411`, yielding `(b·b)^{1/4}` rather than the intended `‖b‖₂`.
  - The annotation is additive (theme stays `firm`); inserted as a new Recognition note IMMEDIATELY AFTER the existing `CheckDot` Recognition note and BEFORE the `Citations:` block (lines 267-318); 2 new `Citations:` rows appended for `iterative.cpp:398-411` + `vector.hpp:257-260` (lines 358-368). The annotation's section header EXPLICITLY hedges "likely Palace bug; upstream confirmation pending" (rotation-quality + bookkeeping gates clean).
  - Original OQ `cg-initial-residual-quirk-palace-bug-flag-lift-path` NARROWED: lift portion CLOSED on landing; narrower sub-OQ `cg-initial-residual-quirk-upstream-confirmation-pending` retained for the bug-vs-intentional classification (out-of-scope for this project — requires Palace maintainer answer; *Trigger:* upstream issue filed or `git blame iterative.cpp:408`).
  - Citecheck: 26 ok / 0 failing; both new citations anchor-verified (`initial_guess` at 398; `Norml2` at 257). Files touched: `book/src/L1-L0/ksp-solve-mutation-rotation.md`.

- **HEADLINE 3 — D3 observation-only survey yields negative-finding + new plan candidate (cross-layer-cross-cutter; floquet-correction-operator-construction-variants).** `FloquetCorrSolver` (`palace/linalg/floquetcorrection.{hpp,cpp}`) is surveyed for the predicted `apply_linop` coverage gap. The actual finding is the OPPOSITE:
  - `FloquetCorrSolver::Mult` (`:72-79`) is bit-for-bit identical to `apply-linop-mutation-rotation` Sub-pattern A (in-place `Mult(const VecType &x, VecType &y) const`).
  - `FloquetCorrSolver::AddMult` (`:80-85`) is bit-for-bit identical to Sub-pattern D (`AddMult(const VecType &x, VecType &y, ScalarType a) const`).
  - `FloquetCorrSolver` is NOT a `Operator`/`ComplexOperator` subclass — it is a standalone class with the same overload-set surface (same boat as `DivFreeSolver`). The existing `apply-linop-overload-set.md:33` non-exhaustive caveat ("Other operator-shaped types in Palace … all implement the same interface; the overload-set shape is uniform") already accommodates constructed-operator-gate classes.
  - **NO extension to `apply-linop-mutation-rotation` or `apply-linop-overload-set` is needed.** The OQ `floquet-correction-operator-construction-variants` is RESOLVED on the apply_linop dimension as a clean MATCH negative finding.
  - The actual coverage gap is at a DIFFERENT tier: there is no firm L1 `floquet_correction` operator and no L1>L0 `floquet-correction-mutation-rotation` theme. This is structurally isomorphic to the firm `divfree-projector` (third firm instance of `nested-constructed-operator-gate`, sibling to `divfree-projector` + `eigsolve`). Closure: `FloquetCorrector[N_nd, N_rt]` carrying `M : LinearOperator[N_rt, N_rt]` (RT mass), `Cross : LinearOperator[N_nd, N_rt]` ([kp ×] matrix realization), `ksp : Solver[M]` (inner CG + JacobiSmoother). L1 signature: `floquet_correction :: (F: FloquetCorrector[N_nd, N_rt], x: Field[N_nd]) -> Field[N_rt]` with `floquet_correction(F, x) = F.M⁻¹ · F.Cross · x`. Lowering theme: sub-pattern A for `Mult`, sub-pattern D for `AddMult`. Fan-out: 4 AddMult call sites (3 in `palace/drivers/drivensolver.cpp:212, 336, 468` + 1 in `palace/drivers/eigensolver.cpp:454`); concept-page upgrade `nested-constructed-operator-gate` 2 firm → 3 firm. Cost: small (~half of divfree-projector; no `bdr_eff` boundary, no complex-vs-real branching, no `Mult(VecType &y)` in-place form).
  - Migrated to `scaffolding/priorities.md` Backlog (Medium fan-out, route `harvester`, plan-tag `nested-constructed-operator-gate-instance-3`) by this finalize per the c034 D3 report's §Recommendation item 2. Surfaced in `scaffolding/integrator-signals.md` as a suggested cycle-036 dispatch.
  - Files touched (D3): observation-only, NO `book/` edits.

- **HEADLINE 4 (process, ESCALATING) — RECURRENCE-2 of `cycle-planner-stale-priorities-line-recruitment` WITHIN BATCH-10.** The c035 cycle-planner produced a 2-of-3-STALE plan (D1 `apply-nonlinear-pencil-mutation-rotation` audit already done since ~c025; D3 `apply_linop` L3 backfill already firm since c011). The planner CLAIMED it ran the four-step deliverable-presence check ("all three are genuinely open") but did not actually verify. The ORCHESTRATOR caught both at dispatch-time and substituted 3 verified-open dispatches. Combined with the c034 D3 stale-dispatch (recurrence-1), this is recurrence-2-within-batch-10 of a friction the batch-9 meta-phase JUST codified (friction-ledger entry + ENFORCEMENT bullet + skill `verify-dispatch-scope-not-already-discharged` promoted to producer-side). The batch-9 prompt-level codification is **demonstrably insufficient at the planner side**. **STRONG batch-10 meta-phase agenda evidence**: the post-c036 meta-phase MUST enact a structural repair. Recommended repair-path candidates: (a) migrate `verify-dispatch-scope-not-already-discharged` from producer-side to planner-side (D3 c034 report + D3 c034 critic recommendation; load-bearing direct repair); (b) introduce a mechanical pre-dispatch gate (e.g., integrator-side grep on-disk Status before any dispatch fires); (c) escalate the planner to opus (claude-haiku-4-5 may simply be insufficient for the four-step check). Routed forward via `scaffolding/integrator-signals.md` cycle-035 — NOT enacted this finalize.

## Layer-stack counts (verified on disk this cycle)

| Layer | Count |
|---|---|
| L0 | 22 chapters |
| L1 firm | 25 (unchanged) |
| L1 rough-in (test-coverage-bounded) | 2 |
| L1 rough-in (obstruction) | 6 |
| L1>L0 firm themes | 23 (unchanged; D1+D2 additive into existing firm themes; D3 observation-only) |
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

- **D1 — lifter** — `reports/2026-05-31T141500Z-lifter-chebyshev-cite-tighten/` — applied; 3 surgical cite-precision edits, theme stays firm. OQs: 1 new sibling hygiene + 1 closed.
- **D2 — abstractor** — `reports/2026-05-31T141500Z-abstractor-cg-initial-residual-quirk-lift/` — applied; additive recognition-rule annotation into firm theme + 2 citations rows. OQs: 1 narrower sub-OQ retained + 1 lift-portion closed.
- **D3 — cross-layer-cross-cutter** — `reports/2026-05-31T141500Z-cross-layer-cross-cutter-floquet-operator-construction-variants/` — applied (observation-only); 0 book changes. OQs: 1 new plan candidate (`floquet-correction-l1-gate-harvest`) + 1 apply_linop dimension closed (negative finding).

## Build

`cargo make book` exit 0, 90.81s. The two book-touching reports (D1 chebyshev cite-tighten + D2 ksp-solve-mutation-rotation additive annotation) introduce zero new build warnings. The 4 KaTeX `Potential incomplete link` warnings remaining are all in `design/l4_calculus.md` (pre-existing false-positives noted across many recent cycles; lines 104/108/122/142). linkcheck2 backend clean. No build-repair this cycle.

## Open questions

**Filed this cycle (3 new):**
- `chebyshev-smoother-mutation-rotation-applyorder0-true-citation-tighten-sibling` (D1; sibling `:101-110` → `:102-110` future-cycle hook; informational, citecheck-passing under current bounds, low fan-out)
- `cg-initial-residual-quirk-upstream-confirmation-pending` (D2 narrower sub-OQ; bug-vs-intentional classification needs Palace maintainer answer; out-of-scope for this project; *Trigger:* upstream issue filed or `git blame iterative.cpp:408`)
- `floquet-correction-l1-gate-harvest` (D3; **MIGRATED to `priorities.md` Backlog by integrator-finalize** as a new Medium fan-out harvester candidate; plan-tag `nested-constructed-operator-gate-instance-3`)

**Closed this cycle (3, two via narrowing):**
- `chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten` (RESOLVED by D1; in-place annotation at `scaffolding/open-questions.md:489` records the cycle-035 D1 disposition)
- `cg-initial-residual-quirk-palace-bug-flag-lift-path` (NARROWED — lift portion CLOSED on landing; upstream-confirmation portion split off as the narrower sub-OQ above)
- `floquet-correction-operator-construction-variants` (NARROWED — apply_linop dimension RESOLVED on landing via D3 negative finding; the L1-tier coverage gap split off as the new plan candidate `floquet-correction-l1-gate-harvest` above)

## Roadmap implications

- **§Diagonal-preconditioner apply** — the `polynomial-smoother` L2 combinator candidacy (3-sibling pattern jacobi + chebyshev + richardson) is **BLOCKED/RETIRED** as of cycle-035: Palace exposes no standalone Richardson smoother enum or relax-type — only Jacobi/Chebyshev/DistRelaxationSmoother. Unblock would require Palace to expose Richardson upstream (out of project scope) OR inventing a third sibling (out of scope per the unimplemented-Palace-components policy). The cohort's L1 + L1>L0 firm-state is mature; no further cycle-035-routed forward work.
- **§Per-solver pipelines (Eigenmode + Driven)** — D3's `floquet-correction-l1-gate-harvest` plan candidate adds **a new coverage-gap row to the Driven + Eigenmode L1 vocabulary**: the `floquet_correction` constructed-operator gate (third instance of `nested-constructed-operator-gate`, isomorphic to firm `divfree-projector`) is consumed at 4 `AddMult` call sites in `palace/drivers/drivensolver.cpp:212,336,468` + `palace/drivers/eigensolver.cpp:454`. Cycle-036+ harvester candidate (template-port from divfree-projector; ~half the cost; sibling-instance precedent makes this a low-risk firm landing). Roadmap row inline-annotation added under the Eigenmode/Driven pipelines (see roadmap.md).

## Cycle character

**Consolidation/hygiene cycle**: 1 surgical cite-precision fix + 1 additive recognition-rule annotation lift + 1 observation-only survey with NEW plan candidate migrated. Two of the three book-impacting outcomes are additive into existing firm themes (no status changes; no firm-cohort growth). The third is observation-only (yielding a clean negative finding + a new fan-out-ranked plan candidate). The **L1/L1>L0 frontier is essentially mature**: every firm L1 op has its L1>L0 theme; the diagonal-preconditioner cohort is closed pending the now-blocked polynomial-smoother L2 candidacy; the audit backlog (apply-nonlinear-pencil, deflate, gram-fold, orthogonalize-composition) is the next routine work tier. Cycle-036 (THIRD/FINAL primary cycle of batch-10) should weight genuinely-open work carefully — the `floquet-correction-l1-gate-harvest` migrated candidate is one such genuinely-open dispatch.

The **batch-10 meta-phase agenda (fires after c036 finalize) crystallizes around the recurrence-2 escalation**: the prompt-level batch-9 codification is demonstrably insufficient; structural repair beyond a Discipline bullet is required.

## Next cycle priorities (cycle-036 = THIRD/FINAL primary cycle of batch-10; meta-phase fires AFTER c036 finalize)

Pulling from `scaffolding/priorities.md` backlog with MANDATORY deliverable-presence check per `.claude/agents/cycle-planner.md` §Discipline (cycle-033 working precedent + c034 D3 recurrence-1 + c035 2-of-3-stale recurrence-2 reinforcement):

1. **(`harvester`, `floquet_correction` L1 + `L1-L0/floquet-correction-mutation-rotation`)** — the new migrated plan candidate from c035 D3; route harvester, isomorphic to firm `divfree-projector`, third firm instance of `nested-constructed-operator-gate`, ~half divfree cost. Fan-out Medium (4 AddMult call sites + concept-page upgrade 2→3 firm instances).
2. **(`lowering-verifier`, batch-6 firm-theme audit, pick ONE of remaining)** — `deflate-composition-lowering` / `gram-fold-specialization` / `orthogonalize-composition-lowering`. Per-line `verified_against:` backfill. Apply deliverable-presence check (verify on-disk `verified_against:` block ABSENCE before proposing).
3. **(open slot / TBD)** — cycle-036 planner-chosen substantive landing per the MANDATORY pre-dispatch deliverable-presence check; the L1/L1>L0 frontier is mature so most dispatch routes need extra care to avoid stale picks.

**Cycle-036 planner reminder (post-c035 recurrence-2 escalation)**: the c035 2-of-3-stale plan PROVES the prompt-level four-step check is insufficient — the planner asserted compliance without performing the check. For EVERY candidate this cycle: actually run the four-step grep AND emit the per-candidate evidence inline (not just a section header claiming compliance). Better yet, dispatch the orchestrator-side verified-open substitution as the working protocol — c034 + c035 both demonstrate the orchestrator's substitution catches what the planner misses. The batch-10 meta-phase agenda CRYSTALLIZES around this recurrence; cycle-036 is the final batch-10 evidence point.

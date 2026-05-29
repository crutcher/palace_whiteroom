---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T041500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T044500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize ksp_solve at L3"

## Critique

### Checks run

**citation-validity — warning.** I independently re-read every cited L0 range via `palace-codemap read_range`. The load-bearing crux citations are line-exact: CG outer-driver loop `for (; it < max_it && !converged; it++)` at `iterative.cpp:427` (exact); in-loop `converged = (res < eps);` at `:464` (exact); CG result-write `final_res = res; final_it = it;` at `:484-485` (exact); GMRES restart loop `for (; it < max_it; restart++)` at `:564` (exact); GMRES result-write `final_res = beta; final_it = it;` at `:703-704` (exact); `ksp.cpp` wrapper `BaseKspSolver::Mult` opens at `:296`, `ksp->Mult(x, y)` at `:300`, `ksp_mult++; ksp_mult_it += ksp->GetNumIterations();` at `:308-309`, template instantiations at `:312-313` (all exact); `GetConverged()` with the `rel_tol > 0.0 || abs_tol > 0.0` gate at `iterative.hpp:98` (exact); `OperType`/`ScalarType` `std::conditional` at `iterative.hpp:30-33` (exact). Three citations carry minor upper-bound range drift (see Issues): the eps/pre-loop-test pair (`:417-418`, cited `:417-419`), the four result fields (`:51-53`, cited `:51-55` and `:51-54`), and the accessor cluster (`GetInitialRes :101` / `GetFinalRes :105` / `GetNumIterations :108`, cited `:100-106` which both starts one early and clips `GetNumIterations` at `:108`). All cited content is present and the drift is ≤2 lines / a small over- or under-shoot of blank or adjacent lines; no claim is unsupported. Marked warning, not fail, because every claim's substance is in-range and verifiable.

**surface-or-evidence — pass (CRUX).** This is the load-bearing determination and it holds. The report asserts L3 `ksp_solve` carries a *genuine iteration-rotation* (the outer-driver fold over `krylov-step`), NOT pure identity. I verified the complementarity claim against the cited siblings and it is source-grounded and internally consistent across the existing artifact: (a) `L3/krylov-step.md` §"Iteration-rotation marker" (line 108) states verbatim that the outer-loop sequentiality "is a property of the surrounding `iterate_while_L3` tail-recursion, not of the `krylov-step` body itself" and that the kernel body "is identity-in-form to the L2 body precisely because all sequentiality is pushed into the surrounding loop" — `ksp_solve` claiming to *be* that surrounding tail-recursion is the exact complement; (b) `L2/krylov-step.md` §Context (line 9) independently grounds the same split ("the *outer* iteration of every Krylov method carries a `sequential-obstruction` at L3 ... Putting `krylov-step` at L3 would conflate 'kernel exists' with 'kernel lifts'"), which the report quotes faithfully; (c) the kernel(lifts)/driver(does-not-lift) pair is the correct reading — the driver is a real fold whose carry-to-carry scalar dependence (`α`, `β`, `ρ`, `ω`, `θ`) is the obstruction, which is structurally distinct from the BLAS-1 identity backfills (those have no fold). The entry modifies surface (it authors a new firm operator entry) AND carries the rotation evidence, so the surface-or-evidence bar is met without needing the retroactive-evidence escape hatch. The determination is sound.

**rotation-quality — pass.** High→low discipline is observed. The L3 entry states semantics, signature, and algebraic laws in L3 vocabulary (value-threaded positional fold, `iterate_while_L3`, the kernel/driver pair, the four-field `result` projection of `s_final`); the L4 monad / `readonly` / L1 opacity are explicitly noted as *absent* rather than transcribed. The entry does NOT improperly embed the L3>L2 lowering: it records only the rotation *direction* and the *non-identity judgment* in-line (§"Lowers to", §"L3 vs L2 distinction", dep-map) and defers the `L3-L2/ksp-solve-outer-driver` theme to a future abstractor dispatch, correctly gated on the L2 anchor being promoted past `stub`. That disposition is the right call under one-op-per-invocation + the high→low invariant. The rotation is a genuine iteration-rotation (a `for`-loop re-expressed as a tail-recursive fold), not a rename or 1:1 mapping. One judgment-call to flag (see Issues): the report classes the L3>L2 hop as *substantive / non-identity*, while the sibling `L3-L2/krylov-step-body-identity.md` treats the same "L3 tail-recursive outer loop collapses to L2's outer-driver-by-role reference" collapse as an *information-preserving surface adjustment*. The report's distinction ("for `ksp_solve` the loop IS the operator, so the collapse is the whole rotation") is defensible and is corroborated by the L2 `ksp_solve` stub's own self-description ("the L3>L2 `krylov-step-body-identity` theme is identity; this outer-driver wrap is NOT") — so the non-identity claim is consistent with the artifact, but it is a layer-edge judgment, not a source fact, and the abstractor authoring the eventual theme should ratify it.

**variant-axis-coverage — pass.** The solver-method axis is classified explicitly: krylov-method (`CG | GMRES | FGMRES`) selects loop *nesting* — CG single `iterate_while_L3` fold (`iterative.cpp:427`) vs GMRES/FGMRES restart-nested double fold (outer `:564` wrapping the inner Arnoldi fold). All five declared axes (krylov-method, element-type, initial-guess-policy, convergence-failure-policy, restart-shape) are loop-shaping and each is grounded in a cited L0 site. The report explicitly delimits these five against `krylov-step`'s six body-variant axes and resolves the one shared axis (restart-shape: kernel restart-agnostic, driver owns it) as complementary not duplicated. No hidden branch surfaced; the per-step body is asserted uniform (`krylov-step op`) with the method axis touching only nesting + residual-proxy extraction, which matches the CG-vs-GMRES `final_res = res` vs `final_res = beta` divergence I verified at `:484` / `:703`.

**cross-reference-integrity — warning.** Every cross-reference inside the *published chapter body* (CYCLE.md lines 48-256) resolves: siblings via `./` (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`, `krylov-step`, `index`), concepts via `../concepts/` (all 8 referenced concept pages exist: sequential-obstruction, convergence-test, solve-monad, solver-as-operator, derived-view-hoisting, state-stratification, variant-absorption, constructed-operators), and other layers via `../L1/`, `../L2/`, `../L3-L2/` (all exist). Forward-references to the not-yet-existing `L3-L2/ksp-solve-outer-driver` theme are kept plain-text (no live link), correct per the rough-in-forward-reference convention. The new file + L3 dep-map row (insert after the `chebyshev` row, index.md:29 — verified that line 29 is the chebyshev dep-map row) + SUMMARY register (insert after `- [chebyshev](./L3/chebyshev.md)`, SUMMARY.md:29 — verified) are all proposed and well-anchored. The L3-gap inventory (gemv=done-via-apply_linop, trsv=blocked-no-L1-anchor, eigsolve=next) is correctly surfaced as an OQ for the cycle-021 planner, not enacted. The single defect: in the OQ section (CYCLE.md:294, report prose — NOT the published chapter), the `apply_linop` link is written `../book/src/L3/apply_linop.md`, which is a malformed relative target (from the report dir it does not resolve; from a `book/src/L3/` chapter it would be wrong too). It is outside the published body so it does not break the artifact build, but it is a dead link in the report itself.

**edge-label-fidelity — pass.** The entry carries edge labels in two directions and the prose discusses the exact labelled edges. "Lowers to" is labelled L3→L2 and the prose narrates the L3 explicit fold → L2 outer-driver-by-role consolidation (forward L3→L2, correct direction per high→low). "Lifts from" is labelled L3←L1 (un-collapse of the L1 opaque solver) and the prose discusses exactly that L1↔L3 relationship. No edge-label/prose mismatch. The dep-map row's lower-edge cell correctly names the L2 target and the non-identity judgment.

**plan-kind-consistency — pass.** Declared kind is a firm L3 operator entry; the content shape matches. The body is fully materialized (signature with the explicit fold; four-phase semantics each L0-anchored; four trajectory-terminal laws + a catalogue of explicit non-laws; five closed variant axes; evidence block; L3-vs-L1 and L3-vs-L2 distinction sections). No rough-in placeholders, no `TBD`/`pending` inside the operator body (the only "pending" markers are the correctly-deferred L3>L2 theme and L2-promotion follow-ons, which live in §"Lowers to" / §Caveats as forward-work, not as gaps in this entry). The `firm` status is justified: the fold structure, convergence predicate, four-field extraction, restart nesting, and the outer-loop `sequential-obstruction` are each directly evidenced in the Palace `Mult` bodies I re-read. Proposed-changes blocks are well-formed (one create + two surgical inserts).

**skill-uptake-survey — pass (telemetry only).** The report references invocation of `verify-citation-range` for producer self-verification before emit (CYCLE.md:278, "All L0 citations self-verified ... via `palace-codemap` `read_range` (per `verify-citation-range` skill ...)"). The report performs substantial variant-axis classification (5 loop-shaping axes, explicitly partitioned against the kernel's 6 body axes) but does not reference the `classify-variant-axis` skill; this is a pure-presence telemetry observation, not blocking — the classification quality is high regardless. No skill-friction reported.

### Issues found

1. **[low — citation-range drift] Accessor-cluster range understates the span.** CYCLE.md §Signature (line 120) and §Evidence (line 235) cite the result accessors as `iterative.hpp:100-106`. Verified actual lines: `GetInitialRes` at `:101`, `GetFinalRes` at `:105`, `GetNumIterations` at `:108`. The cited range starts one line early and clips `GetNumIterations` (`:108`) entirely. Candidate fix: cite `:101-108`. (Where: `L3/ksp_solve.md` §Signature + §Evidence.)

2. **[low — citation-range drift] Four-result-fields range overshoots.** §Signature (line 120) cites the four `IterativeSolver` fields at `:51-55`; §Evidence supporting block (line 282) cites `:51-54`. Verified actual: `mutable bool converged;` (`:51`), `mutable double initial_res, final_res;` (`:52`), `mutable int final_it;` (`:53`). The four fields span `:51-53`; `:54` is the `use_timer` comment line / `:55` beyond. Candidate fix: normalize to `:51-53`. Note the same surface in the firm `L3/krylov-step.md` cites these as `:52-55`, so there is a pre-existing inconsistency in how this field block is cited across entries — worth a consistency pass but not introduced by this report.

3. **[low — citation-range drift] eps/pre-loop-test pair range includes a blank line.** §Signature (line 122), §Semantics phase 1 (line 134), and the supporting block (line 280) cite `eps = max(rel_tol·initial_res, abs_tol)` + pre-loop `converged = (res < eps)` at `iterative.cpp:417-419`. Verified actual: eps formula at `:417`, `converged = (res < eps);` at `:418`; `:419` is blank (`// Begin iterations.` is `:420`). The pair is `:417-418`. Harmless (in-range), but `:417-418` is tighter. (Where: `L3/ksp_solve.md` §Signature, §Semantics, plus CYCLE.md §"Supporting evidence".)

4. **[low — dead link in report prose, not artifact] Malformed `apply_linop` relative path in OQ.** CYCLE.md:294 (Open-questions / L3-gap inventory) writes `[`apply_linop`](../book/src/L3/apply_linop.md)`. This target does not resolve from the report directory and would be wrong from a `book/src/L3/` chapter as well (correct sibling form is `./apply_linop.md`). It is confined to the report's own prose — it is NOT in the published chapter body (lines 48-256), where the link is correctly `./apply_linop.md` (line 184). No build impact; flagged because it is a dead link in the report. (Where: `CYCLE.md` §Open questions / L3-gap inventory, line 294.)

5. **[informational — layer-edge judgment, not a defect] "Substantive / non-identity" L3>L2 classification is a judgment call in mild tension with the kernel's sibling theme.** The report classes the L3→L2 hop for `ksp_solve` as substantive (non-identity), while `L3-L2/krylov-step-body-identity.md` (and `L3/krylov-step.md` line 29/172) treat the identical "L3 tail-recursive outer loop collapses to L2's outer-driver-by-role reference" collapse as an *information-preserving surface adjustment*. The report's reconciliation ("for `ksp_solve` the loop IS the operator, so the consolidation is the whole rotation, not a surface adjustment around an identity body") is defensible and is consistent with the L2 `ksp_solve` stub's own "this outer-driver wrap is NOT [identity]" self-description. Not a citation or surface defect — but the eventual `L3-L2/ksp-solve-outer-driver` abstractor should explicitly ratify that the *same syntactic collapse* is "surface adjustment" for the kernel yet "the whole rotation" for the driver, so the two adjacent-edge themes don't read as contradictory. Surfaced for the integrator/abstractor, not for repair. (Where: `L3/ksp_solve.md` §"Lowers to", §"L3 vs L2 distinction", dep-map row.)

6. **[informational — telemetry] `classify-variant-axis` not referenced despite substantial variant-axis work.** The entry classifies five loop-shaping axes and partitions them against the kernel's six body axes — exactly the shape `classify-variant-axis` targets — but only `verify-citation-range` is referenced. Pure uptake telemetry; classification quality is unaffected. (Where: `L3/ksp_solve.md` §"Variant axes"; CYCLE.md skill-reference at line 278.)

---

## Repair

The crux (surface-or-evidence: L3 `ksp_solve` is a genuine iteration-rotation, NOT identity) is a `pass` and HOLDS — no repair touches it. Both warning checks were mechanical-range / dead-link defects, fully repairable. No substantive authoring required.

### Fixes attempted

1. **Finding 1 [citation-validity] — accessor-cluster range `:100-106` understates / clips.**
   - **Decision**: repaired.
   - **Verification**: re-read `iterative.hpp:100-108` via `palace-codemap read_range`. `GetInitialRes` at `:101`, `GetFinalRes` at `:105`, `GetNumIterations` at `:108`. Cited `:100-106` starts one line early and clips `GetNumIterations` (`:108`). Correct span: `:101-108` (confirms critic).
   - **Action**: rewrote `:100-106` → `:101-108` at both occurrences — CYCLE.md §Signature (the `book/src/L3/ksp_solve.md` operator-content body, "These four fields are the L3 value-threaded analogues…") and §Evidence (the `iterative.hpp:25-115` evidence bullet).

2. **Finding 2 [citation-validity] — four-result-fields range `:51-55` / `:51-54` overshoots/understates.**
   - **Decision**: repaired.
   - **Verification**: re-read `iterative.hpp:52-55`. `:52` = comment `// Variables set during solve…`, `:53` = `mutable bool converged;`, `:54` = `mutable double initial_res, final_res;`, `:55` = `mutable int final_it;`. The three field declarations are `:53-55`; the comment-headed block is `:52-55`. NOTE: the critic's suggested replacement value `:51-53` is itself off by ~2 lines (it places `converged` at `:51`, but `:51` is blank and `converged` is at `:53`). My repair authority is to fix to the **source-verified** range, not to copy a wrong suggested value. I used `:52-55` (comment + three field declarations) — which matches the form `krylov-step.md` already cites, so this fix *resolves* the noted cross-entry inconsistency rather than introducing a new divergence.
   - **Action**: rewrote `:51-55` → `:52-55` (CYCLE.md §Signature operator-body "the L0 `IterativeSolver` result-extraction surface…" + §Evidence `iterative.hpp:25-115` bullet) and `:51-54` → `:52-55` (CYCLE.md §"Supporting evidence" self-verification bullet). Left the already-correct `:52-55` at §"Inherited demand-pruning" untouched. Did NOT touch `krylov-step.md` (out of scope — different report's artifact).

3. **Finding 3 [citation-validity] — eps/pre-loop-test range includes a blank line.**
   - **Decision**: repaired.
   - **Verification**: re-read `iterative.cpp:417-419`. `:417` = `eps = std::max(rel_tol * initial_res, abs_tol);`, `:418` = `converged = (res < eps);`, `:419` = blank. The pair is `:417-418`. Also verified the lone pre-loop-test cite (`converged = (res < eps)` "before the loop") cited as `:418-419` — `:418` is the statement, `:419` blank, so the single line is `:418`.
   - **Action**: rewrote `:417-419` → `:417-418` at all four occurrences (§"Load-bearing determination", §Signature operator-body threshold sentence, §Semantics phase-1, §"Supporting evidence" CG bullet, §Evidence `iterative.cpp:361-486` bullet) and tightened the lone `:418-419` → `:418` at §"Algebraic laws" law 2. The latter occurrence was the same blank-line defect on the same site; tightening it is within "range includes a blank line" authority.

4. **Finding 4 [cross-reference-integrity] — malformed `apply_linop` link in OQ section.**
   - **Decision**: repaired.
   - **Verification**: confined to report prose (CYCLE.md §Open questions / L3-gap inventory), NOT the published chapter body (which correctly uses `./apply_linop.md`). The form `../book/src/L3/apply_linop.md` resolves from neither the report dir nor a chapter.
   - **Action**: rewrote `[`apply_linop`](../book/src/L3/apply_linop.md)` → `[`apply_linop`](./apply_linop.md)`, matching the sibling form already used in the published chapter body.

5. **Finding 5 [informational] — "substantive/non-identity" L3>L2 classification in mild tension with the kernel's `krylov-step-body-identity` "surface adjustment" framing.**
   - **Decision**: not-needed (defer to abstractor as follow-up, NOT a repair).
   - **Rationale**: this is a defensible layer-edge judgment, not a mechanical defect. Per the critic, the report's reconciliation ("for `ksp_solve` the loop IS the operator, so the consolidation is the whole rotation") is consistent with the artifact (corroborated by the L2 `ksp_solve` stub's own "this outer-driver wrap is NOT [identity]" self-description). Ratifying that the *same syntactic collapse* reads as "surface adjustment" for the kernel yet "the whole rotation" for the driver is substantive authoring reserved for the eventual `L3-L2/ksp-solve-outer-driver` abstractor dispatch. The report already surfaces this in its OQ / §"Lowers to" and gates the theme on L2-`ksp_solve` promotion past `stub`. No artifact contradiction; no integrator action needed beyond letting the existing OQ flow to the cycle-021 planner.

6. **Finding 6 [skill-uptake] — `classify-variant-axis` not referenced.**
   - **Decision**: not-needed.
   - **Rationale**: pure presence-telemetry observation; the critic explicitly marked it non-blocking and the classification quality is high regardless. No repair.

### Unrepairable findings

None. Both warning checks reduced to mechanical citation-range / dead-link fixes, all applied. Findings 5 and 6 are informational (not defects) and require no repair.

## Suggested resolution

`overall_status: ready` — `follow_up_agent: null`. All eight critic checks now resolve to `pass` (6) or repaired-warning (citation-validity, cross-reference-integrity); the crux holds. Notes for the integrator:

- The report's own OQ ledger already carries two genuine forward-work items the integrator should promote to the plan / OQ channel verbatim (they are correctly NOT enacted by this dispatch): (a) the **`L3-L2/ksp-solve-outer-driver` theme** is warranted but gated on promoting `book/src/L2/ksp_solve.md` from `stub` (sequence: L2 harvester first, then abstractor authors the theme); (b) the **finding-5 layer-edge ratification** — the eventual abstractor on that theme should explicitly reconcile the "surface adjustment" (kernel) vs "whole rotation" (driver) framing so the two adjacent-edge themes don't read as contradictory.
- The L3-gap inventory in the report's OQ (gemv = done-via-`apply_linop`; trsv = blocked, no L1 anchor, likely an obstruction-theme target; eigsolve = next, likely kernel+driver split like `krylov-step`/`ksp_solve`) is good cycle-021-planner input — surface it to the plan.
- This L3 entry is firm above a `stub` L2 anchor (an inversion of the usual high→low maturity gradient); the report justifies this under "Identity-lowerings still require both L levels" (each layer coherent within itself). Promoting `L2/ksp_solve` remains the higher-priority follow-on — worth a plan row.

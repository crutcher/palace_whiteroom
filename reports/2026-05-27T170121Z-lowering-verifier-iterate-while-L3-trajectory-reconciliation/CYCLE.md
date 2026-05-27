---
agent: lowering-verifier
invoked_at: 2026-05-27T170121Z
scope: L4>L3 theme audit — iterate-while L3 trajectory-accumulation reconciliation (OQ iterate-while-l3-rendering-trajectory-accumulation-gap)
status: pending
inputs:
  - book/src/L4/iterate-while.md (cycle-007 wave-1 firm)
  - book/src/L4/iterate-while-with-prev.md (cycle-007 wave-1 firm)
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (cycle-006 wave-2 rough-in)
  - scaffolding/open-questions.md (OQ iterate-while-l3-rendering-trajectory-accumulation-gap, cycle-007 augmented status)
  - reference/palace/palace/linalg/iterative.cpp (CG, GMRES, FGMRES iteration loops)
  - reference/palace/palace/linalg/iterative.hpp (KSP result-extraction surface)
  - reference/palace/palace/linalg/ksp.cpp (BaseKspSolver::Mult — sole consumer of iterative.* result-extraction)
  - reference/palace/test/unit/ (no test on KSP residual history; negative evidence)
  - book/src/concepts/derived-view-hoisting.md (the §3.8 demand-pruning algebra)
status: integrated
integrated_at: 2026-05-27T17:17:02Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Applied cycle-007 wave-2 per-report dispatch 6 of 6 at 19:30:00Z; finalized in batch cycle-007 at 17:17:02Z.
  Audit-only dispatch — no book/ artefact edits. Files edited: scaffolding/open-questions.md (body augmentation on iterate-while-l3-rendering-trajectory-accumulation-gap recording cycle-007 wave-2 verdict (c); status intentionally kept open per user directive — closure becomes appropriate only after cycle-008+ lifter patch lands the §3.8 collapse-rule citation; 1 new OQ appended at end of cycle-007 block).
  1 new OQ: iterate-while-log-effect-vs-trajectory-channel.
  Report's Change 2 (verified_against: 10-citation block) and Change 3 (substantive §3.8-citation patch + Condition 5 + two-form sketch) DEFERRED per user-directive scope as audit-only — routed to cycle-008+ lifter dispatch on book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md as cycle-008 PRIORITY.
  Closure of iterate-while-l3-rendering-trajectory-accumulation-gap gated on cycle-008+ lifter patch landing.
  Gate hits: 0.
---

# CYCLE: Audit L4>L3 iterate-while trajectory-accumulation reconciliation

## Summary

This dispatch audits the gap flagged by OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`: cycle-007's firm L4 `iterate_while` and `iterate_while_with_prev` (`book/src/L4/iterate-while.md`, `book/src/L4/iterate-while-with-prev.md`) carry an explicit `trajectory: [{ ...e }]` accumulator subject to the §3.8 demand-pruning law (Law 1 of both chapters); the cycle-006 L4>L3 theme `krylov-step-typed-wrapper-dissolution`'s §"What the L3 form for `iterate_while` looks like" (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:156-167`) renders the L3 form as returning a *single* `readout` rather than a `[readout]` accumulator. The audit's goal was to classify the gap as (a) L3-should-track-trajectory, (b) L4-should-be-specialized-to-single-readout, (c) L3-is-correct-add-explicit-collapse-rule, or (d) insufficient-evidence.

**Verdict: (c) — L3 is correct as single-readout (specifically: zero per-iteration readout retention); L4>L3 lowering needs an explicit "trajectory pruned by §3.8 because Palace's consumer surface observes only `final_state`" collapse rule.**

The audit found unambiguous L0/L1 evidence that Palace's KSP surface materializes *exactly four scalars*: `converged`, `initial_res`, `final_res`, `final_it`. There is no per-iteration residual-history accumulator anywhere in `iterative.hpp` / `iterative.cpp`; the per-iteration `res` / `beta` value is either printed inline (under `print_opts.iterations`) or overwritten. The sole caller of the result-extraction surface (`BaseKspSolver::Mult` at `palace/linalg/ksp.cpp:296-310`) consumes only `GetConverged()`, `GetFinalRes() / GetInitialRes()` (for a warning), and `GetNumIterations()` (summed into a counter). The L4 `[readout]` form is a future-proof generality that the §3.8 demand-pruning law (Law 1 of `book/src/L4/iterate-while.md`) reduces to the L3 single-readout form for Palace's actual consumer surface — but the cycle-006 L3 rendering elides the application of §3.8 rather than naming it, which is the gap. The fix is not to change the L3 form's *shape* (it is correct for Palace) but to add an explicit collapse step in the lowering theme that names §3.8 as the rule applied.

## Per-citation audit

### Citation 1: book/src/L4/iterate-while.md (cycle-007 wave-1 firm)

- **Citation**: `book/src/L4/iterate-while.md:28-43` (Signature, extras-carrying and Solve-threaded forms); `:64-88` (small-step reduction rule for trajectory); `:123-133` (Law 1, trajectory pruning); `:222-224` (Evidence, Palace L0 anchor citations for the canonical iteration shapes — tightened from `:222-232` per critic Finding 1; lines 225-232 carry adjacent concept-evidence not the L0-anchor claim).
- **Theme claim**: the firm L4 form carries `trajectory: [{ ...e }]` as a structural return field; per Law 1, when only `final_state` is observed downstream, the body is rewritten to drop the extras computation. The L0 evidence at `iterative.cpp:427` (PCG outer loop) and `iterative.cpp:615` (GMRES inner) is cited as the "canonical Palace iteration shape this combinator names."
- **Found**: confirmed verbatim. The Signature at lines 28-43 and Semantics at lines 64-88 establish the `[{ ...e }]` accumulator. Law 1 at 123-133 states the demand-pruning rewrite as: *"For any consumer expression `K[ iterate_while a p f ]` that observes only the `final_state` field of the combinator's result … the §3.8 pruning rule rewrites the body `f` to the subgraph that computes only the `state` field of its return record, omitting the extras computation."* This is exactly the rule that applies to Palace's case. The §"Lowers to" section at lines 180-198 already acknowledges the gap explicitly: *"the existing theme's L3 rendering at `krylov-step-typed-wrapper-dissolution.md:156-167` drops the trajectory — it returns a single `readout` rather than the `[readout]` accumulator that the firm L4 form here keeps (per Law 1). This is the very gap tracked by the cycle-006 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`; this chapter's §"Lowers to" therefore points to the existing theme for the wrapper-dissolution shape only and defers the trajectory-shape reconciliation to the cycle-008+ lowering-verifier follow-up."*
- **Verdict**: supports. The L4 chapter is internally consistent with its claim that §3.8 *should* mediate the trajectory shape at L3; it explicitly defers the realization of that reconciliation to this dispatch.
- **Notes**: this audit's purpose is precisely to close that deferral. The L4 form itself is sound; the lowering side is the locus of the gap.

### Citation 2: book/src/L4/iterate-while-with-prev.md (cycle-007 wave-1 firm)

- **Citation**: `book/src/L4/iterate-while-with-prev.md:43-50` (Solve-threaded signature with trajectory); `:74-93` (small-step rule); `:137-147` (Law 2, trajectory pruning lifted to both step bodies); `:180-200` (Lowers to, same caveat as `iterate-while`).
- **Theme claim**: parallel to `iterate-while`, the with-prev variant also carries `trajectory: [{ ...e }]` and inherits the same §3.8 demand-pruning law. The §"Lowers to" section at line 200 carries the same caveat as `iterate-while.md`: the existing theme drops the trajectory; the firm L4 form keeps it; the gap routes to cycle-008+ lowering-verifier (i.e., this dispatch).
- **Found**: confirmed verbatim. Law 2 at lines 137-147 states the pruning rule applied to *both* `bootstrap_step` and `steady_step`. The L3 rendering shown at lines 183-196 carries `[extras]` explicitly (with `[e₀] ++ trajectory` accumulation), in contrast to the cycle-006 theme's elided form — meaning the with-prev chapter has *already* internally rendered the L3 form with the trajectory accumulator preserved. So the inconsistency is asymmetric: the cycle-007 chapters' inline L3 sketches keep the accumulator (correctly modulo the §3.8 collapse for Palace's consumer); the cycle-006 theme's inline sketch drops it without naming §3.8.
- **Verdict**: supports. The cycle-007 with-prev chapter's inline L3 form is the structurally-correct presentation (accumulator present, with §3.8 pruning applied at the call site). The cycle-006 theme is the artifact that needs the explicit-collapse-rule patch.
- **Notes**: this asymmetry is informative — the cycle-007 firm chapters are internally consistent with the trajectory generality; the cycle-006 theme's L3 sketch is the one out of alignment.

### Citation 3: book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (cycle-006 wave-2 rough-in)

- **Citation**: `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:156-167` — the §"What the L3 form for `iterate_while` looks like" subsection. Specifically lines 160-165:
  ```text
  iterate_while_L3 step (carry, sim) =
    let (carry', sim', readout, continue) = step (carry, sim)
    in if continue then iterate_while_L3 step (carry', sim')
                   else (carry', sim', readout)
  ```
- **Theme claim** (the cycle-006 theme's framing of the L3 rendering): a tail-recursive value-threading L3 loop with no trajectory accumulator; returns a single `readout` on termination; the demand-pruning is implied by the absence of a list-shaped return.
- **Found**: confirmed; the L3 sketch as written drops the per-iteration `readout` accumulator silently. There is no commentary connecting this collapse to the §3.8 rule, no naming of `derived-view-hoisting`, no statement that "Palace consumes only `final_state`-equivalent quantities so the trajectory collapses to the empty list under Law 1." The sketch reads as if the L3 combinator has a different semantics than the L4 combinator (which would be a contradiction, not a refinement).
- **Verdict**: partially-supports — the L3 *shape* is correct for Palace's consumer surface (audited below at citations 5-7), but the rendering elides the rule application that would justify it, making the L3 form look like a different combinator rather than a §3.8-collapsed instance of the same combinator.
- **Notes**: the cycle-006 theme's `Status: rough-in` correctly flags that the theme needs follow-up; this dispatch identifies the §"What the L3 form for iterate_while looks like" subsection as the specific text needing the §3.8-naming patch.

### Citation 4: scaffolding/open-questions.md OQ iterate-while-l3-rendering-trajectory-accumulation-gap

- **Citation**: `scaffolding/open-questions.md:1227-1239` (cycle-006 framing); `:1239` cycle-007 augmentation note.
- **Theme claim**: the OQ enumerates two candidate resolutions: (a) re-render the L3 form with explicit `trajectory` accumulator pass-through, or (b) author an explicit demand-pruning step that justifies the collapse to a single readout. The cycle-007 augmentation confirms the harvester did not pick between (a) and (b).
- **Found**: confirmed. The OQ's framing precisely matches this audit's verdict-classification space: (a) ≈ verdict-option (a) [promote L3 to trajectory] and (b) ≈ verdict-option (c) [keep L3 single-readout, name §3.8 explicitly]. Verdict-option (b) [demote L4] is not in the OQ's enumeration but is logically possible; the audit ruled it out below.
- **Verdict**: supports. The OQ is well-framed; the cycle-007 harvester correctly deferred the resolution to a verifier dispatch with the L4 firm form available as the auditable artifact.
- **Notes**: the OQ should be marked `closed` with `answered_in: this CYCLE.md` and verdict text added (see Proposed changes §1 below).

### Citation 5: reference/palace/palace/linalg/iterative.cpp PCG outer loop

- **Citation**: `palace/linalg/iterative.cpp:420-485` (PCG main `for` loop and final-summary block).
- **Theme claim**: cycle-007 firm L4 `iterate-while.md:231` claims this is the *canonical Palace iterate_while pattern with bounded `max_it` and convergence flag in the predicate, both folded into the L4 `α` carry.*
- **Found**: confirmed and sharpened. The loop body at lines 427-464 maintains five mutable scalars (`res`, `beta`, `beta_prev`, `denom`, `alpha`) and three workspace vectors (`r`, `z`, `p`); per-iteration the value of `res` is computed (line 462: `res = std::sqrt(std::abs(beta));`) and *either printed under `print_opts.iterations` (line 431) or immediately overwritten on the next iteration's line-462*. After the loop, lines 465-485 use `res` for a one-time summary printing and capture `final_res = res; final_it = it;` (lines 484-485). **There is no `std::vector<double>` accumulating per-iteration residuals**. The per-iteration `res` value lives in a function-local scalar and is consumed exactly once (either by the print or by the next-iteration's overwrite).
- **Verdict**: supports — the L4 chapter's claim that the loop folds `max_it` and `converged` into the carry is correct; **and** the L4 chapter's *implicit* claim that the trajectory is "future-proof" (because it is built into the combinator generality) is correct, because Palace itself does *not* retain a trajectory.
- **Notes**: the only places per-iteration residuals are observed by Palace are the inline `Mpi::Print` calls under `print_opts.iterations` — a side-effecting log channel, not a return-value channel. This is *not* a `[readout]` accumulator in any meaningful sense; it is a free-monad-style logging effect that the L4 form's `Solve` monad does not currently include. Logging is orthogonal to the trajectory shape.

### Citation 6: reference/palace/palace/linalg/iterative.cpp GMRES inner Arnoldi loop

- **Citation**: `palace/linalg/iterative.cpp:614-705` (GMRES inner `for (;; j++, it++)` plus the surrounding restart loop plus the final-summary block); same shape repeated for FGMRES at `:734-870`.
- **Theme claim**: cycle-007 firm L4 `iterate-while.md:232` claims `for (;; j++, it++)` with break-on-converged at line 644 is "the second Palace iteration shape; the predicate-in-body break corresponds at L4 to `s.converged` being a carry field set inside the step body."
- **Found**: confirmed. The inner loop maintains a single per-iteration `beta` scalar (line 642: `beta = std::abs(s[j + 1]);`). Same disposition as CG: `beta` is either printed (line 619) or overwritten next iteration. After the inner loop, lines 684-704 print a one-time summary and capture `final_res = beta; final_it = it;`. **No per-iteration residual history**. The GMRES Hessenberg `H` (line 192 of `iterative.hpp`) and Givens scratch vectors `s`, `sn`, `cs` are per-restart workspace for the projected least-squares problem, not residual history.
- **Verdict**: supports. The GMRES surface confirms the CG finding: trajectory is not retained.
- **Notes**: FGMRES at `iterative.cpp:734-870` is structurally identical (one more workspace `Z[]` for the flexible-preconditioner Krylov basis). Same per-iteration `beta` discipline.

### Citation 7: reference/palace/palace/linalg/iterative.hpp KSP result-extraction surface

- **Citation**: `palace/linalg/iterative.hpp:52-55` (the four mutable scalars: `converged`, `initial_res`, `final_res`, `final_it`); `:97-108` (the four public getters: `GetConverged`, `GetInitialRes`, `GetFinalRes`, `GetNumIterations`).
- **Theme claim**: this is the load-bearing audit citation that the cycle-007 firm L4 chapters do *not* yet cite. Implicit claim: Palace's KSP API surface materializes the *result* as exactly four scalars, with no list-shaped or trajectory-shaped field.
- **Found**: confirmed unambiguously. Lines 52-55: `mutable bool converged; mutable double initial_res, final_res; mutable int final_it;`. Lines 97-108: four `Get*()` accessors returning these four scalars. No `GetResidualHistory()`, no `GetIterationData()`, no list-shaped return. The `final_res` documentation at line 103-104 explicitly states "the final (absolute) residual for the previous solve, which may be an estimate to the true residual" — confirming it is a single scalar, not a representative of a list.
- **Verdict**: supports the (c) verdict (single-readout is correct; L4 trajectory is generality not currently consumed). This is the *canonical* evidence that distinguishes verdict (a) from verdict (c): if Palace had `GetResidualHistory(): std::vector<double>`, the gap would be a *real* one-size-fits-one type mismatch; instead, Palace's surface is the §3.8-pruned form of the L4 trajectory generality.
- **Notes**: this citation should be added to the cycle-007 firm L4 `iterate-while.md` Evidence section as the L0 anchor for "Palace's actual consumer surface observes only `final_state`-equivalent quantities." See Proposed changes §2 below.

### Citation 8: reference/palace/palace/linalg/ksp.cpp sole caller of result-extraction

- **Citation**: `palace/linalg/ksp.cpp:296-310` (`BaseKspSolver<OperType>::Mult`).
- **Theme claim**: implicit corollary of citation 7 — the four scalars are *actually* consumed in exactly the ways the L4 `final_state`-only pruning rule would predict.
- **Found**: confirmed. Lines 300-309 show the full consumption pattern:
  - Line 300: `ksp->Mult(x, y);` — runs the solve (no return value examined here).
  - Line 301: `if (!ksp->GetConverged())` — branch on the final converged flag.
  - Lines 303-307: warning emission consuming `GetFinalRes() / GetInitialRes()` (a *ratio* of the final residual to the initial residual) and `GetInitialRes()` (logged).
  - Line 309: `ksp_mult_it += ksp->GetNumIterations();` — sum the iteration count into a running counter for `BaseKspSolver`-level statistics.
  
  Across `palace/`, `GetFinalRes` is called only at `ksp.cpp:306`; `GetNumIterations` only at `ksp.cpp:309`; `GetInitialRes` only at `ksp.cpp:306`; `GetConverged` only at `ksp.cpp:301`. **One consumer, one usage pattern, four scalars consumed.**
- **Verdict**: supports the (c) verdict at maximal strength. The Palace consumer surface is the *canonical* `final_state`-only observation that triggers §3.8 demand-pruning's collapse of the trajectory to the empty list. There is no consumer that would benefit from the L4 trajectory being retained at L3.
- **Notes**: a future Palace feature could add a `GetResidualHistory()` accessor; if/when it does, the L3 form would need to be re-rendered with the accumulator restored. The L4 form is correctly positioned to accommodate this without a calculus-level change — it is exactly the §3.8 generality the demand-pruning law buys. This is *why* the L4 form keeps the trajectory: not because Palace consumes it today, but because the L4 calculus's pruning is what allows one combinator definition to serve both consumption patterns without runtime flags.

### Citation 9: reference/palace/test/unit/ tests on KSP iteration loops

- **Citation**: `reference/palace/test/unit/` directory listing.
- **Theme claim** (negative): no Palace unit test asserts on per-iteration residual values.
- **Found**: confirmed. The unit test directory contains 29 test files; the closest to KSP are `test-orthog.cpp` (orthogonalization-only, not the iteration loop), `test-rap.cpp` (operator wrapper), `test-romoperator.cpp` (uses GMRES via JSON config as a sub-solver; asserts on the ROM operator's output, not on per-iteration residuals). There is no `test-ksp.cpp`, `test-cg.cpp`, `test-gmres.cpp`, `test-fgmres.cpp`, or `test-iterative.cpp`. The closest test-of-iteration is the orthog test (which tests `OrthogonalizeIteration`, a primitive *inside* the GMRES inner loop, not the loop itself).
- **Verdict**: supports the (c) verdict — the absence of tests on residual histories is consistent with Palace's surface not retaining one. (Tests are semantic supplement per the CLAUDE.md invariant; the absence of a test is not strong evidence by itself, but it does rule out a hidden "test asserts on residual sequence" rationale for the L4 trajectory generality.)
- **Notes**: the cycle-006 `test-linkages/` directory (if populated) would be the canonical place to record this negative finding, but no linkages-file currently exists for KSP-residual-tests. Filing as part of this CYCLE.md's Supporting evidence section.

### Citation 10: book/src/concepts/derived-view-hoisting.md (the §3.8 demand-pruning algebra)

- **Citation**: `book/src/concepts/derived-view-hoisting.md:1-40` (the full concept page).
- **Theme claim**: implicit — `derived-view-hoisting` is the concept page that codifies the §3.8 demand-driven pruning algebra that the L4 chapters' Law 1 cites.
- **Found**: confirmed; the page's §"Worked example: CG residual norm" (lines 14-19) is the canonical instantiation of the §3.8 pruning for the specific case of `iterate_while`'s `residual_norm` extras: *"`iterate_while` accumulates `residual_norm`s into a trajectory; consumers reading only `.final_state` cause the residual computation to be pruned."* This is exactly the Palace case audited above.
- **Verdict**: supports. The concept page already names the rule that the cycle-006 theme should cite explicitly when collapsing the L3 trajectory to a single readout. The patch is to reference this concept page (and the L4 chapters' Law 1) at the cycle-006 theme's §"What the L3 form for iterate_while looks like" subsection.
- **Notes**: the cycle-006 theme already references `derived-view-hoisting` at line 212 in the Concept-page references list — so the patch is to make the dependency *operational* at the relevant subsection, not introduce a fresh dependency.

## Applicability conditions

The cycle-006 theme's §"Applicability conditions" lists four conditions for the L4>L3 lowering rewrite to apply (lines 103-113). The audit walks each:

- **Condition 1**: *The L4 `Solve` monad's effect domain is exactly `SimState`.*
  - **Verifiable**: yes, from the L4 chapter's §Semantics (`iterate-while.md:78-90`) and from `solve-monad.md:1-69`. The only `modify` in any cycle-007 firm L4 body is on `SimState.it`. The cycle-006 theme's claim still holds.
  - **Found counter-example?**: no.
- **Condition 2**: *`OpParams` is closure-captured at the per-step call site, not threaded.*
  - **Verifiable**: yes; the cycle-006 L4 form has `op` curried out before the loop body. The cycle-007 firm L4 form preserves this — see `iterate-while.md:103` ("the step body's `Solve` effect is on `SimState` only").
  - **Found counter-example?**: no.
- **Condition 3**: *The five primitive groups are L3-native or carry their own L3-edge classification.*
  - **Verifiable**: yes (the audit of cycle-002 identity-in-form claim in the cycle-006 theme already establishes this; cycle-007 L3>L2 `book/src/L3-L2/krylov-step-body-identity.md` further ratifies it).
  - **Found counter-example?**: no.
- **Condition 4**: *The `Krylov` ephemeral bundle has plain-value lifecycle and is not aliased by any other state.*
  - **Verifiable**: yes; per `solve-monad.md:53` and `iterative.hpp:144` (Palace's CG workspace `mutable VecType r, z, p;` is per-solve scratch, not threaded across solves).
  - **Found counter-example?**: no.

The audit adds one **new applicability condition** that the cycle-006 theme should record explicitly:

- **(New) Condition 5**: *The downstream consumer observes only `final_state`-equivalent quantities of the `iterate_while` invocation; per Law 1 of `book/src/L4/iterate-while.md` (the §3.8 demand-pruning rule), the trajectory then prunes to `[]` and the L3 form is the single-readout shape.*
  - **Verifiable for Palace**: yes, from `iterative.hpp:52-55` (four-scalar surface) + `ksp.cpp:296-310` (sole consumer). All four scalars are `final_state`-equivalent: `converged` is `s.converged` (a carry field); `final_res` is `s.res` (a carry-derived scalar at the final iteration); `final_it` is `s.it` (a carry field); `initial_res` is computed *before* the loop and is not a trajectory observation at all.
  - **Found counter-example?**: no Palace consumer of any cycle-007 firm L4 form requires the trajectory; one hypothetical future feature (`GetResidualHistory()`) would invalidate Condition 5 for that consumer and the L3 form would need to be re-rendered with the accumulator. The L4 form is unaffected.

This new Condition 5 is the *missing structural piece* that closes the OQ: the cycle-006 theme renders the L3 form *as if* Condition 5 held without naming it as a condition. The verdict-(c) patch makes Condition 5 explicit so a future reader can recognize when the L3 rendering would need to change.

## Algebraic laws (if cited)

The audit checks one algebraic law for soundness against the operator surface:

- **Law**: `book/src/L4/iterate-while.md` Law 1 (demand-driven trajectory pruning). Statement: *for any consumer expression `K[ iterate_while a p f ]` that observes only the `final_state` field of the combinator's result, the §3.8 pruning rule rewrites the body `f` to the subgraph that computes only the `state` field of its return record, omitting the extras computation.*
- **Holds on operators?**: yes for the Palace setting, by the audit findings above. The four-scalar Palace consumer surface satisfies the law's antecedent ("only `final_state` is observed") because each of the four scalars is `final_state`-equivalent (either a carry field at the final iteration or a pre-loop initialization). The pruning rule then collapses the trajectory to `[]`, and the L3 form is the §3.8-pruned form. **The L3 form is correct *because* Law 1 holds, not despite it.**

No other algebraic law is challenged by the audit. Law 2 (`iterate_while_pure` definitional reduction), Law 3 (empty-trajectory base case), and Law 4 (fold-fusion with carry-projection) of `book/src/L4/iterate-while.md` are orthogonal to the trajectory-vs-no-trajectory question and are not re-audited here. Same for the with-prev chapter's three laws.

## Proposed changes

Three edits, all proposed for cycle-008+ application by an `abstractor` or `lifter` dispatch (per role spec: lowering-verifier audits, does not author):

### Change 1: Mark OQ iterate-while-l3-rendering-trajectory-accumulation-gap as closed

```edit:scaffolding/open-questions.md
[at line 1232, change status]

~~~yaml
---
slug: iterate-while-l3-rendering-trajectory-accumulation-gap
opened_at: cycle-006
opened_by: abstractor
status: closed
answered_at: cycle-007
answered_in: reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/CYCLE.md (verdict (c) — L3 single-readout is correct; L4>L3 lowering needs explicit §3.8 collapse-rule citation)
relates_to: iterate-while-l4-anchor-missing (cycle-006)
---
~~~

[at end of existing cycle-007 update paragraph (line 1239), append]

**Cycle-007 closure** (lowering-verifier dispatch `2026-05-27T170121Z`): audit verdict is **(c)** — the L3 form's single-readout shape is correct for Palace's consumer surface (which materializes exactly four scalars: `converged`, `initial_res`, `final_res`, `final_it`, per `reference/palace/palace/linalg/iterative.hpp:52-55` + sole consumer at `reference/palace/palace/linalg/ksp.cpp:296-310`). The L4 trajectory generality is intentional (it future-proofs the calculus against a hypothetical `GetResidualHistory()` Palace surface) and the cycle-006 L3 rendering is the §3.8-pruned form of the L4 generality — but the cycle-006 theme elides the application of §3.8 rather than naming it. Resolution path: a cycle-008+ `lifter` dispatch on `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for iterate_while looks like" should patch the subsection to (i) cite `book/src/L4/iterate-while.md` Law 1 and `book/src/concepts/derived-view-hoisting.md` §"Worked example", and (ii) add explicit text noting that the L3 single-`readout` form is the §3.8 collapse of the L4 `[readout]` accumulator under the Palace consumer surface's `final_state`-only observation. The L3 form's *shape* is correct; only its *justification* needs the §3.8 anchor. Both candidate resolutions (a) and (b) enumerated in the original OQ are subsumed: (a) was the wrong direction (would have *promoted* L3 to a trajectory it does not need); (b) was a less-precise framing of this dispatch's resolution. The new condition surfaced by this audit — Palace consumer observes only `final_state`-equivalent quantities — becomes a fifth applicability condition for the cycle-006 theme (see Change 2).
```

### Change 2: Add the verified_against block + §3.8-collapse note to the cycle-006 theme

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[append at end of file]

~~~yaml
verified_against:
  - citation: book/src/L4/iterate-while.md:28-43
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: cycle-007 firm L4 signature explicitly carries trajectory:[{...e}]; cycle-006 L3 rendering correctly omits it per §3.8 collapse but elides the rule-citation.
  - citation: book/src/L4/iterate-while.md:123-133
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: Law 1 (trajectory pruning) is the rule that justifies the cycle-006 L3 single-readout rendering for Palace; needs explicit citation in §"What the L3 form for iterate_while looks like".
  - citation: book/src/L4/iterate-while-with-prev.md:137-147
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: Law 2 of the with-prev chapter lifts the pruning rule to both step bodies; same disposition for the cycle-006 theme's Form B L3 rendering.
  - citation: reference/palace/palace/linalg/iterative.cpp:420-485
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: PCG outer loop retains no per-iteration residual history; final_res, final_it captured as scalars at lines 484-485.
  - citation: reference/palace/palace/linalg/iterative.cpp:614-705
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: GMRES inner Arnoldi loop same disposition as PCG; per-iteration beta either printed or overwritten; final_res, final_it captured at 703-704.
  - citation: reference/palace/palace/linalg/iterative.hpp:52-55
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: KSP result-extraction surface is exactly four scalars (converged, initial_res, final_res, final_it); no list-shaped or trajectory-shaped field.
  - citation: reference/palace/palace/linalg/iterative.hpp:97-108
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: Four public getters parallel to the four scalars; no GetResidualHistory() or analogue.
  - citation: reference/palace/palace/linalg/ksp.cpp:296-310
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: Sole caller of KSP result-extraction surface; consumes converged (branch), final_res/initial_res (warning ratio), final_it (counter sum); no per-iteration consumption.
  - citation: book/src/concepts/derived-view-hoisting.md:14-19
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: §"Worked example: CG residual norm" is the canonical instantiation of the §3.8 pruning for iterate_while's residual_norm extras; should be cross-referenced at the cycle-006 theme's L3-form subsection.
~~~
```

### Change 3 (out of lowering-verifier authority — proposed for cycle-008+ lifter dispatch)

The substantive patch to `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for iterate_while looks like" (currently lines 156-167) should be authored by a `lifter` dispatch in cycle-008+. Proposed shape (for the lifter's reference, not as an edit applied here):

1. Replace the existing 9-line code-block sketch (lines 160-165) with a two-form sketch: (i) the §3.8-pruned form (current rendering, single readout) labeled as "the Palace-consumer-pruned form" with an explicit citation to `book/src/L4/iterate-while.md` Law 1; (ii) the non-pruned form with explicit `[readout]` accumulator, labeled as "the unpruned form that arises when a future consumer reads `.trajectory`."
2. Add a one-sentence preamble: "Per Law 1 of `book/src/L4/iterate-while.md` (§3.8 demand-driven trajectory pruning) and `book/src/concepts/derived-view-hoisting.md` §'Worked example: CG residual norm', the L3 form's shape depends on the downstream consumer's observation pattern; Palace's KSP consumer surface (`iterative.hpp:52-55`) observes only `final_state`-equivalent quantities, so the trajectory collapses to `[]` and the L3 form is the single-readout shape rendered below."
3. Add the new Condition 5 to §"Applicability conditions" (currently lines 101-113): "5. The downstream consumer observes only `final_state`-equivalent quantities of the `iterate_while` invocation; otherwise the L3 form acquires a `[readout]` accumulator per the unpruned form."

The lifter dispatch should be a low-cost dispatch (single file edit, no new operator promotion, no new theme); should be slotted alongside any cycle-008+ work on the cycle-006 theme (e.g., a `lifter` dispatch promoting the theme from `rough-in` to `firm` would naturally subsume this patch).

## Supporting evidence

Files consulted beyond the cited evidence ranges:

- `/home/crutcher/git/palace_whiteroom/book/src/L4/iterate-while.md` — read in full (235 lines); confirmed internal consistency of the trajectory framing and the explicit deferral of the L3-form reconciliation to this dispatch.
- `/home/crutcher/git/palace_whiteroom/book/src/L4/iterate-while-with-prev.md` — read in full (238 lines); confirmed the with-prev chapter's inline L3 sketch (lines 183-196) keeps the trajectory accumulator, in contrast to the cycle-006 theme's elided form. This asymmetry is informative.
- `/home/crutcher/git/palace_whiteroom/book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` — read in full (217 lines); identified §"What the L3 form for iterate_while looks like" (lines 156-167) as the specific subsection needing the §3.8-collapse-rule patch.
- `/home/crutcher/git/palace_whiteroom/scaffolding/open-questions.md` — read OQ-relevant range (lines 1215-1310); the cycle-007 augmentation note at line 1239 is the canonical statement of the deferred reconciliation.
- `/home/crutcher/git/palace_whiteroom/reference/palace/palace/linalg/iterative.cpp` — read lines 400-490 (PCG loop), 580-705 (GMRES loops), 735-870 (FGMRES loops). All three iteration loops show the same disposition: per-iteration residual scalar is either printed under `print_opts.iterations` or overwritten; final residual captured as `final_res` scalar at end of loop.
- `/home/crutcher/git/palace_whiteroom/reference/palace/palace/linalg/iterative.hpp` — read lines 40-250; confirmed the four-scalar result-extraction surface is uniform across `IterativeSolver`, `CgSolver`, `GmresSolver`, `FgmresSolver`.
- `/home/crutcher/git/palace_whiteroom/reference/palace/palace/linalg/ksp.cpp` — read lines 280-313; confirmed `BaseKspSolver::Mult` is the sole consumer of the result-extraction surface across the Palace codebase.
- `/home/crutcher/git/palace_whiteroom/reference/palace/test/unit/` directory listing — confirmed no `test-ksp*`, `test-cg*`, `test-gmres*`, `test-fgmres*`, or `test-iterative*` exists. The `test-orthog.cpp` test covers the orthogonalization primitive inside GMRES's inner loop, not the loop itself or any per-iteration residual.
- `/home/crutcher/git/palace_whiteroom/book/src/concepts/derived-view-hoisting.md` — read in full (40 lines); the §"Worked example: CG residual norm" at lines 14-19 is the canonical instantiation of the §3.8 pruning for `iterate_while`'s `residual_norm` extras.

Cross-codebase grep results (evidence for citation 8's "sole consumer" claim):
- `GetFinalRes`: 1 call site (`ksp.cpp:306`); 1 definition (`iterative.hpp:105`).
- `GetNumIterations`: 1 call site (`ksp.cpp:309`); 1 definition (`iterative.hpp:108`).
- `GetInitialRes`: 1 call site (`ksp.cpp:306`); 1 definition (`iterative.hpp:101`).
- `GetConverged`: 1 call site (`ksp.cpp:301`); 1 definition (`iterative.hpp:98`).

(SLEPc-prefixed `EPSGetConverged`, `SVDGetConverged`, etc. in `slepc.cpp` are PETSc API calls on different objects, not on Palace's `IterativeSolver`. They are unrelated to the KSP iteration-loop surface audited here.)

## Open questions / caveats

1. **The `Mpi::Print` log channel is a side-effecting per-iteration readout that the L4 `Solve` monad does not currently model.** The cycle-007 firm L4 `iterate-while.md` §Semantics' third placement-discipline (line 104) explicitly contrasts the L4 demand-pruning approach with *"Palace's L0 `print_opts.iterations`-conditional residual printing at `iterative.cpp:422-426`"*, noting that "at L4 the conditionality disappears." This is correct as far as the *return-value* trajectory is concerned, but the *logging effect* is its own observation channel that the L4 `Solve = StateT SimState Identity` monad does not capture. A future-question (not blocking the cycle-007 OQ resolution): should the L4 `Solve` monad be extended to a richer effect representation that captures the log channel (e.g., `Solve = RWST OpParams (DList LogEntry) SimState Identity`), so that the print-when-`print_opts.iterations` behavior is a free-monad-style telling rather than an out-of-band side-effect?

   Filing as **NEW open question** `iterate-while-log-effect-vs-trajectory-channel`. Canonical YAML frame for integrator-per-report append into `scaffolding/open-questions.md`:

   ```yaml
   ---
   slug: iterate-while-log-effect-vs-trajectory-channel
   opened_at: cycle-007
   opened_by: lowering-verifier
   status: open
   relates_to: iterate-while-l3-rendering-trajectory-accumulation-gap (cycle-006, closed cycle-007)
   ---
   ```

   Question text (for the OQ body paragraph following the YAML block):

   > The cycle-007 firm L4 `iterate-while.md` / `iterate-while-with-prev.md` model iteration as `Solve = StateT SimState Identity` — a state-monad over `SimState` with no logging effect. Palace's L0 surface (e.g., `reference/palace/palace/linalg/iterative.cpp:422-426` for PCG, `:617-621` for GMRES) emits per-iteration residuals via `Mpi::Print` conditional on `print_opts.iterations`. The audit verdict-(c) resolution of `iterate-while-l3-rendering-trajectory-accumulation-gap` (`reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/CYCLE.md`) closed the return-value trajectory question (single-readout L3 form is correct under §3.8 pruning), but the *logging-channel* observation is independently present in Palace and not currently captured by the L4 calculus. Should `Solve` be extended to a richer effect representation (e.g., `Solve = RWST OpParams (DList LogEntry) SimState Identity`) so the print-when-`print_opts.iterations` behavior becomes a free-monad-style `tell` rather than an out-of-band side-effect? Orthogonal to the trajectory-collapse question — affects effect-modeling discipline, not the trajectory shape. Routes to a cycle-008+ `lowering-verifier` or `abstractor` dispatch (or, more likely, surfaces during meta-phase methodology review of the L4 monad surface). Not blocking. Source: `reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/CYCLE.md` §"Open questions / caveats" item 1.

   Not blocking on this cycle's resolution; the current single-readout L3 rendering is independently correct for Palace's *return-value* surface.

2. **Hypothetical future Palace surface `GetResidualHistory()`** is not implemented and not in the cycle-007 priority slate; the audit does not propose adding it as an L1 obstruction theme. If Palace ever adds it, the cycle-006 theme's L3 rendering for `iterate_while` would need to be re-rendered with the accumulator restored (or, equivalently, the §3.8 pruning would not fire because the consumer now observes `.trajectory`). The new Condition 5 (Change 2 / Change 3) names this contingency; no additional action needed today.

3. **Cycle-006 audit-of-cycle-002 identity-in-form claim (the audit nested within the cycle-006 theme's §"Audit of cycle-002 identity-in-form claim", lines 169-187) is unrelated to this audit.** That nested audit was about the *body* primitive sequence (L4>L3>L2 chain on the kernel body); this audit is about the *trajectory accumulator wrapper* (L4>L3 hop, specifically the §3.8-pruning resolution). The two are independent and both stand. The cycle-007 L3>L2 theme `book/src/L3-L2/krylov-step-body-identity.md` covers the body-side; this CYCLE.md's verdict-(c) recommendation covers the trajectory-side.

4. **The dispatch instructions named four verdict options (a)-(d); this audit selected (c).** Verdict (a) [promote L3 to track trajectory] was ruled out by citations 5-8 (no Palace consumer reads a trajectory). Verdict (b) [demote L4 to single-readout] was ruled out because the L4 trajectory generality is the load-bearing structure that makes the §3.8 demand-pruning law (Law 1) operational; demoting L4 would force a runtime "compute residuals?" flag (contradicting the L4 chapter's explicit anti-pattern at `iterate-while.md:104`). Verdict (d) [insufficient evidence] was ruled out because the L0/L1 evidence at citations 5-8 is unambiguous (single-consumer, four-scalar surface). Verdict (c) is the only consistent reading of the cited evidence.

5. **Codemap MCP tools not used per dispatch instructions.** All file localization performed via vanilla `Read(offset, limit)` and `Bash(grep)` calls. The MCP server instructions appearing in the inputs section are noted but not invoked, consistent with the dispatch directive that "the codemap MCP tools were permission-denied in cycle-007 wave-1; do not retry them."

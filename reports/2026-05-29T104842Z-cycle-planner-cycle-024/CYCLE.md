---
agent: cycle-planner
invoked_at: 2026-05-29T10:48:42Z
scope: cycle-024 dispatch plan
status: pending
---

# Cycle 024 dispatch plan

**Cycle-024 is the THIRD and FINAL primary cycle of meta-batch-6 (cycles 022/023/024).** The batch-6 meta-phase fires immediately after this cycle's `integrator-finalize` commit. No meta-phase this cycle — only the primary cycle loop (plan → dispatch → critique → repair → integrate).

## Goals selected this cycle

**Eigsolve chain step-3 L3 backfill** (now unblocked by the L2 firm landing in cycle-023) is the highest-fan-out priority. Cycle-023's integrator materialized the `book/src/L3/eigsolve.md` stub with a "Refinement pending (cycle-024)" note; this dispatch refines it in place to its firm or predicted-`partial-obstruction` terminal form.

The **NLEPS interior-atom harvest** (Jacobian-action + eigenvalue-correction) advances the next two deferred fan-out-ranked NLEPS L1 pieces. The `nleps_deflated_solve` L1 landing in cycle-023 unblocked these.

The **stale `orthog.hpp:34→:35` anchor fix** is a one-token mechanical correction in the cycle-022-firm `dot-mutation-rotation` theme, routed as part of a lowering-verifier or lifter pass (low fan-out, but clear blockers resolved; eligible for same-cycle batching with a cross-layer or mechanics-focused dispatch).

All three unblock forward progress on the eigsolve+NLEPS 5-cycle carry-forward stack. The plan depth is well-served by focusing these HIGH-fan-out items.

## Dispatches

1. **`harvester` — L3 `eigsolve` backfill (stub → firm or partial-obstruction)**
   - **Scope:** `book/src/L3/eigsolve.md` (in-place refinement); the eigen-iteration body lift from the opaque SLEPc `EPSSolve` / ARPACK RCI loop. Firm L1 + firm L2 anchors in place; predicted terminal status `partial-obstruction` (the kernel/driver pair does not lift cleanly — only the per-step `apply_shift_invert` composition lifts at L2). The Palace source is `palace/linalg/slepc.cpp` (SLEPc driver) + `palace/linalg/arpack.cpp` (ARPACK driver) with opaque-library-owned iteration.
   - **Deps:** none (L1 firm + L2 firm both landed cycle-023; stub materialized cycle-023)
   - **Rationale:** HIGH fan-out — closes the strict eigsolve prerequisite chain (L1→L2→L3, chain step-3 DONE). Unblocks per-cycle progress on the eigenmode solver pipeline. The stub already exists as its home; refinement is in-place from the stub, no new file creation.

2. **`harvester` — `nleps_jacobian_action` L1 operator**
   - **Scope:** L1 `nleps_jacobian_action` — the NEP Jacobian-*vector* action at the inside of the quasi-Newton step (the derivative of the `apply_nonlinear_pencil` residual w.r.t. the Newton variable). Cite `palace/linalg/nleps.cpp` (likely the implicit differentiation or finite-difference body of the quasi-Newton callback).
   - **Deps:** none (the carry-forward list from cycles 022/023 made this eligible once `nleps_deflated_solve` L1 was firm, which happened cycle-023)
   - **Rationale:** HIGH fan-out — second deferred NLEPS interior atom; unblocks the next NLEPS piece (`eigenvalue_correction`). The two-piece NLEPS interior sequence is gated on firm `deflate`/`gram` / `lu_solve` leaves (all satisfied cycle-022/023), so both are now eligible in series.

3. **`harvester` — `nleps_eigenvalue_correction` L1 operator**
   - **Scope:** L1 `nleps_eigenvalue_correction` — the quasi-Newton eigenvalue-and-correction step. Likely a thin composition over `lu_solve` (the small-dense Gram-coordinate solve in the correction) + residual evaluation. Cite `palace/linalg/nleps.cpp` (the correction step after the deflated solve).
   - **Deps:** dispatch #2 (`nleps_jacobian_action` — the prior NLEPS interior atom, if both are same cycle, mark sequential for clarity even though they're independent; better: mark parallel and let integration order them)
   - **Rationale:** HIGH fan-out — third deferred NLEPS interior atom; closes the four-piece deferred NLEPS sequence (`nleps_deflated_solve` done cycle-023, then Jacobian, then correction, then [tbd] final piece if any). Once firm, the NLEPS L1 interior is complete; enables `nleps_*` L1>L0 lowering theme authorship.

4. **`abstractor` — `nleps_deflated_solve` L1>L0 lowering theme**
   - **Scope:** L1>L0 lowering: `nleps_deflated_solve` (the L1 Schur-complement composition) → the L0 `palace/linalg/nleps.cpp:504-537` (`deflated_solve` lambda) inline-folded implementation. Narrate the in-place Schur transformation and the nested `lu_solve` unfolding.
   - **Deps:** none (the L1 anchor `nleps_deflated_solve` firmed cycle-023; this is now authorable)
   - **Rationale:** Clears the NLEPS L1>L0 infrastructure. The cite-tightening follow-up to cycle-023's `lu-solve` + `nleps-deflated-residual` themes; completes the NLEPS L1>L0 trio.

5. **`abstractor` — `apply_nonlinear_pencil` L1>L0 leaf (optional)**
   - **Scope:** If in scope this cycle: L1>L0 lowering for the still-plain-text-forward-referenced `apply_nonlinear_pencil` L1 operator (cycle-022 firm). The L1 entry documents the `r = T(λ)·v` residual-apply; the L1>L0 theme narrates the L0 folding into the opaque `QuasiNewtonSolver::GetResidualNorm` closure + the opaque `A2(λ)` nonlinearity. **Can pair with dispatch #4 as a two-theme abstractor wave, or defer if token-heavy.** This is the final plain-text leaf in the NLEPS L1>L0 suite; cycle-023 left it unthemed as an optional carry-forward.
   - **Deps:** none (independent; optional per token/scope)
   - **Rationale:** LOW-to-MEDIUM fan-out (the remaining NLEPS L1>L0 forward-reference closure; frees up plain-text space). Can be deferred to cycle-025 without blocking the NLEPS L1/L2 chain.

6. **`lifter` / `lowering-verifier` — `dot-mutation-rotation` Sub-pattern D anchor correction**
   - **Scope:** Mechanical one-token anchor fix in `book/src/L1-L0/dot-mutation-rotation.md` §Sub-pattern D (lines ~160, ~183): `palace/linalg/orthog.hpp:34` → `:35` (the `return LocalDot(x, y);` is on line 35, not the brace on 34). Verify via codemap; apply the correction.
   - **Deps:** none (mechanical fix independent of other work)
   - **Rationale:** LOW fan-out but HIGH clarity (removes a stale anchor that the cycle-023 lowering-verifier audit surfaced). Fits as a same-dispatch pair with a lifter or lowering-verifier role if either is available for another theme; can also stand alone as a mechanical pass.

7. **`abstractor` — `gram-fold-specialization` L2>L1 lowering theme**
   - **Scope:** L2>L1 lowering: the `gram` (all-pairs `inner_product` fold → `Matrix[k,k]`) composition lowers into the L1 leaf `inner_product` by dispatch on weight/conjugation axes. The L2 anchor is firm (cycle-023); the theme is now authorable. Cite `palace/linalg/nleps.cpp:524-531` (the double-`dot` loop fusion that the L2 entry reads from). Sibling to the firm `inner-product-fold-specialization` L2>L1 theme (cycles 019/021).
   - **Deps:** none (the L2 `gram` firmed cycle-023)
   - **Rationale:** MEDIUM fan-out — tightens the L2 `gram` lowering story; was a carry-forward from cycle-022 `Suggested next dispatches`. Unblocks downstream `deflate-composition-lowering` L2>L1 theme (if dispatched same cycle, mark as pair or sequential for clarity).

8. **`abstractor` — `deflate-composition-lowering` L2>L1 lowering theme**
   - **Scope:** L2>L1 lowering: the `deflate` (oblique projector `I − X(XᴴX)⁻¹Xᴴ`) composition lowers into its L1 + L2 constituents (`gram` → `lu_solve` → `linear_combination` → `dot`). Narrates the Schur-form pipeline. The L2 entry is partly-constructive (cycle-022); this theme documents the lowering path. Cite `palace/linalg/nleps.cpp:505-537` (the Schur-wrapped form, the only positive appearance of the deflate pattern in Palace).
   - **Deps:** dispatch #7 (`gram-fold-specialization` — it is a constituent lowering of the `gram` entry this theme cites). Mark sequential if both dispatched; parallel if #7 completes before #8 starts.
   - **Rationale:** MEDIUM fan-out — completes the `deflate` partly-constructive promotion gate documentation (though the bare-Galerkin core remains unpromotable without a positive bare-Gram-solve site outside `nleps.cpp`). Tightens the L2>L1 Galerkin pipeline. Carry-forward from cycle-022.

9. **`layer-intro-author` — L3 index refresh (optional)**
   - **Scope:** Optional: if L3 index prose updates are warranted by the `eigsolve` backfill + the emerging cohort. The L3 Part intro / dep-map / "Upward" links may reflect eigsolve entry finalization. Lower priority than the substantive operator work; can defer if token-heavy.
   - **Deps:** dispatch #1 (the L3 `eigsolve` entry must complete before the intro refresh cites it)
   - **Rationale:** LOW fan-out (navigational); refreshes cross-references. Optional per scope.

10. **`same-layer-cross-cutter` — NLEPS L1 operator cohort unification audit (optional)**
    - **Scope:** Optional light cross-cutter pass: now that `nleps_jacobian_action` + `nleps_eigenvalue_correction` + (optionally) `apply_nonlinear_pencil` L1>L0 are drafted, verify no redundancy/contradiction with the cycle-022/023 NLEPS L1 entries (`apply_nonlinear_pencil`, `nleps_deflated_residual`, `nleps_deflated_solve`). The four pieces should compose cleanly (the quasi-Newton interior loop).
    - **Deps:** dispatches #2/#3/#4 (the new entries must exist to audit against)
    - **Rationale:** LOW fan-out (quality gate); optional per capacity. Catches unification gaps before integration.

## Overlap analysis

**Same-file matrix (shared artifact regions):**

| Dispatch | File(s) touched | Shared with | Nature | Sequential? |
|---|---|---|---|---|
| 1 (L3 eigsolve) | `L3/eigsolve.md` (in-place), `L3/index.md` | #9 (if dispatched) | L3 Part prose + dep-map | Sequential if #9 dispatched |
| 2 (jacobian) | `L1/nleps_jacobian_action.md` (new) | #3, #4 | NLEPS L1 cohort (dep-map row + SUMMARY append) | Can parallel #3 if both append to L1 index; re-read disk first |
| 3 (correction) | `L1/nleps_eigenvalue_correction.md` (new) | #2, #4 | NLEPS L1 cohort (dep-map row + SUMMARY append) | Can parallel #2 |
| 4 (nleps-sol-theme) | `L1-L0/nleps-deflated-solve-mutation-rotation.md` (new) | #5 (if dispatched) | L1>L0 Part prose + dep-map; SUMMARY under L1>L0 | Can parallel #5; both append to L1-L0 index |
| 5 (pencil-leaf) | `L1-L0/apply-nonlinear-pencil-mutation-rotation.md` (new, optional) | #4 | L1>L0 Part prose + SUMMARY; independent chapter | Parallel OK; can defer |
| 6 (orthog-fix) | `L1-L0/dot-mutation-rotation.md` (edit existing) | none | Mechanical one-token anchor fix | Parallel OK (surgical edit) |
| 7 (gram-fold-spec) | `L2-L1/gram-fold-specialization.md` (new) | #8 | L2>L1 Part prose + dep-map; SUMMARY under L2>L1 | Sequential: #8 depends on #7 done |
| 8 (deflate-lowering) | `L2-L1/deflate-composition-lowering.md` (new) | #7 | L2>L1 Part prose + dep-map; SUMMARY under L2>L1 | Sequential: depends on #7 (its cite) |
| 9 (L3-intro) | `L3/index.md` (edit prose/dep-map) | #1 | L3 Part overview / dep-map | Sequential: depends on #1 done |
| 10 (cross-cut) | none (observation-only; no artifact write) | all | Read-only audit | Parallel OK; post-dispatch optional |

**Book-file conflict summary:**

- **`book/src/L1/index.md`** — shared by #2 (new firm row) + #3 (new firm row). **Non-overlapping row-level appends.** Both re-read disk fresh; either order. PARALLEL OK. **Integrator pre-applies both re-reads to L1-index fresh each dispatch per the split-integrator discipline.**

- **`book/src/L1-L0/index.md`** — shared by #4 (new firm row) + #5 (new firm row, optional). **Non-overlapping row-level appends.** Parallel OK (or sequential #4→#5 for clarity). Each re-reads L1-L0-index fresh.

- **`book/src/L2-L1/index.md`** — shared by #7 (new firm row) + #8 (new firm row). **#8 depends on #7 substantively** (it cites the gram-fold-spec theme #7 authors). #7 must complete + be on disk BEFORE #8 can properly cross-link. Mark SEQUENTIAL: #7 wave-1, #8 wave-2 (post-#7 report).

- **`book/src/L3/index.md`** — touched by #1 (in-place stub→firm on disk) + #9 (optional prose/dep-map edit). Mark SEQUENTIAL if #9 dispatched (depends on #1 done); else #1 stands alone.

- **`book/src/SUMMARY.md`** — all chapter-registering dispatches (#1–#8) will append SUMMARY entries. **Append-only, serial per-report discipline:** each per-report integrator re-reads SUMMARY fresh, appends at a distinct chapter-anchor, and documents the append in Notes. Zero collision expected across 6–8 reports. Parallel OK.

- **`book/src/L1-L0/dot-mutation-rotation.md`** — #6 does a surgical one-token anchor edit (inline anchor `:34` → `:35` at lines ~160, ~183). No conflict with other dispatches. **Parallel OK.**

## Sequencing schedule

**Wave 1 (parallel):**
- Dispatch #1 (L3 eigsolve backfill, harvester)
- Dispatch #2 (nleps_jacobian_action, harvester)
- Dispatch #3 (nleps_eigenvalue_correction, harvester)
- Dispatch #4 (nleps_deflated_solve theme, abstractor)
- Dispatch #6 (orthog-anchor fix, lifter/lowering-verifier)
- Dispatch #7 (gram-fold-specialization theme, abstractor)
- Dispatch #10 (NLEPS audit, cross-cutter) — observation-only; does not block others

**Wave 2 (sequential after wave-1, parallel among themselves):**
- Dispatch #5 (apply_nonlinear_pencil leaf, abstractor, **optional**) — light & independent; can parallel wave-1 or defer
- Dispatch #8 (deflate-composition-lowering theme, abstractor) — **sequential after #7 lands** (must cite the gram-fold-spec theme from #7)
- Dispatch #9 (L3 intro refresh, layer-intro-author, **optional**) — **sequential after #1 lands** (depends on eigsolve entry finalized)

**Rationale:** Dispatches #1–#4, #6–#7, #10 have **no interdependencies** within wave-1. They touch disjoint rows of shared-file dep-maps or edit distinct chapters entirely. The integrator's per-report serial architecture handles the SUMMARY appends cleanly (each report re-reads fresh). #8 **must wait for #7** because it cites the gram-fold-spec theme; mark it sequential to that. #9 **must wait for #1** if dispatched; can defer. #5 is independent and optional (can wave-1 or wave-2 or defer).

## Open questions / caveats

1. **Dispatch #5 (apply_nonlinear_pencil L1>L0 leaf) is optional.** The theme is authorable (the L1 entry is firm cycle-022), but it was a carry-forward left unthemed in cycle-023. If token-budget per dispatch is tight, defer to cycle-025. The omission does NOT block downstream work (all four NLEPS L1 pieces are firm once #2/#3 land; only the L1>L0 lowering-theme completeness is deferred).

2. **Dispatch #9 (L3 index refresh) is optional.** Warrant check: does the L3 Part need prose updates once eigsolve is firm? If the index prose is stable (only the dep-map row changes), skip #9 and let integrator handle the row. Layer-intro-author can return a "no prose changes needed" finding if scope warrants the dispatch.

3. **Dispatch #10 (NLEPS cross-cutter) is observation-only.** It writes no artifact. Its purpose is to verify cohort consistency (the four NLEPS L1 pieces compose cleanly; no redundancy/contradiction emerges from the new jacobian + correction entries). Can be deferred post-integration as a manual audit if token-heavy; the critic will spot gross contradictions anyway.

4. **Carry-forward `deflate` partly-constructive promotion gate STAYS OPEN.** The cycle-023 `nleps_deflated_solve` landing confirmed the bare-Galerkin core `I − X(XᴴX)⁻¹Xᴴ` is NOT positively witnessed (only the Schur-wrapped form appears). Promotion to firm is still gated on a positive bare-Gram-solve site outside `nleps.cpp`. This dispatch does NOT change that verdict.

5. **Plan item status after this cycle.** Dispatches #1–#8 (and optionally #9/#10) resolve the cycle-023 carry-forward list completely (eigsolve L3 backfill, NLEPS interior atoms, NLEPS L1>L0 themes, gram-fold/deflate-lowering themes). The next active-head plan items (post-integration, for cycle-025) are:
   - Remaining `deflate` partly-constructive promotion (awaits positive bare-Gram site)
   - Incremental-least-squares L2 stub→firm (Medium fan-out)
   - Matrix-weighted-norm + bilinear-form firm-promotion (Medium fan-out)
   - Normalize L1 primitive decision (Medium fan-out)
   - Other Medium/Low fan-out backlog items per impact score.

   Dispatch-capacity was 12 agents; cycle-024 dispatches 8–10. Remaining capacity was optionally #5/#9/#10 (light, optional, deferrable).

## Plan edits (scaffolding/priorities.md)

**Mark dispatched cycle-023 active-head items as completed / remove from Now section:**
- `eigsolve-prerequisite-chain` → completed (step-3 dispatched this cycle; will close cycle-024 finalize)

**Append fresh carry-forward candidates to the Backlog (if any surface mid-cycle):**
- None identified this cycle. The planned dispatches clear the cycle-023 signal queue.

**Carry-forward open-question mapping for the integrator's post-dispatch OQ appends:**
- `eigsolve-l3-backfill-partial-obstruction-prediction` — the harvester will confirm whether L3 eigensolve is firm or predicted partial-obstruction (the eigen-iteration does not lift cleanly)
- `nleps-jacobian-and-correction-firm-landing` — both harvester dispatches (#2/#3) will firm these two operators; the NLEPS L1 interior is then complete
- `gram-fold-specialization-and-deflate-composition-lowering-themes` — the two abstractor dispatches (#7/#8) firm these lowering themes

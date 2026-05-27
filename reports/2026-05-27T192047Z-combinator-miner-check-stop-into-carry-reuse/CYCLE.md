---
agent: combinator-miner
invoked_at: 2026-05-27T19:20:47Z
scope: check_stop_into_carry helper-promotion decision (cycle-008 deferred criterion)
status: integrated
integrated_at: 2026-05-27T200036Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied cleanly via integrator-per-report pass 4 of cycle-009. Inspection-only dispatch (verdict defer; zero book/ edits). First cross-cycle abstractor-criterion -> combinator-miner-verdict round-trip in artifact (cycle-008 set "defer until a second slice needs it" criterion; cycle-009 ran the survey). 6 new OQs promoted as the entire dispatch output. Methodology signal for cycle-009 meta-phase batch-1 aggregation.
---

# CYCLE: Combinator candidate — check_stop_into_carry (defer)

## Summary

Cycle-008 wave-2 dispatch #6 (`gmres-inner-loop-iterate-while-migration`) sketched a speculative L4 helper `check_stop_into_carry :: OpParams -> Convergence -> Krylov -> int -> Krylov` to honour [`iterate-while`](../../book/src/L4/iterate-while.md)'s predicate-on-carry-only discipline by hoisting the GMRES 3-condition stop test's `Maybe StopReason` witness into a carry field. The cycle-008 abstractor set a promotion criterion in its caveats: **"defer until a second slice needs it"** (`reports/2026-05-27T180000Z-abstractor-gmres-inner-loop-iterate-while-migration/CYCLE.md:71`; cross-referenced in `scaffolding/open-questions.md:1316`). This dispatch surveys downstream slices and Palace source to test that criterion.

**Verdict: defer.** Among the four candidate downstream consumers (FGMRES, MINRES/BiCGStab stubs, eigenmode solvers, transient stepping, NLEPS) the only slice that reuses the GMRES check-stop *shape* is FGMRES — and FGMRES is **not a second slice** in the L1+ corpus: it is already absorbed into `gmres.md` as the `op.flexible` variant axis (`gmres.md:3,91,122`), and would invoke `check_stop_into_carry` at the *same call site* under the migrated `inner_loop`. NLEPS's Quasi-Newton inner loop (`nleps.cpp:589-647`) has a structurally-similar 3-condition stop (converged / diverged / max-it) but is **not yet spec'd at L1+** (no `nleps.md` slice exists; only L1>L0 mutation-rotation cites it). ARPACK uses reverse-communication; SLEPc is opaque; Chebyshev/transient are bounded counter-loops with no stop test. Therefore the helper has exactly one *current* call site and the cycle-008 promotion criterion is unmet.

The helper should remain in the cycle-008 rough-in theme as a speculative L4 helper. **Re-evaluate when** (a) NLEPS is harvested into an L1+ slice (likely cycle-010+ if eigenmode work prioritises), or (b) a future `arnoldi-step` standalone-driver theme finds the 2-condition `j+1==max_dim || it+1==max_it` shape (which would be a 2-condition stop without a runtime-tested `converged`, a degenerate sub-case rather than full reuse).

## Pattern instances

The "convergence-witness-into-carry hoist" shape — a pure function that runs N condition tests against (`op`, `conv`, `carry`, `total_it`) and writes a `Maybe StopReason` into the carry so that `iterate_while`'s predicate-on-carry-only discipline is honoured — has these candidate instances:

- **Instance 1 (real, in-scope, in-spec)**: GMRES `Mult` inner Arnoldi loop at `reference/palace/palace/linalg/iterative.cpp:615-650` — 3-condition `converged || j + 1 == max_dim || it + 1 == max_it` break at line 645. The cycle-008 theme `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md:36-58,75-96` proposes hoisting this into `check_stop_into_carry`. **This is the primary instance the helper was proposed for.**

- **Instance 2 (real, in-scope, but variant-absorbed into Instance 1)**: FGMRES `Mult` inner loop at `reference/palace/palace/linalg/iterative.cpp:794-828` — textually identical 3-condition break `converged || j + 1 == max_dim || it + 1 == max_it` at line 824. **However**, the spec corpus absorbs FGMRES into the `gmres.md` slice as the `op.flexible` variant axis (`book/src/spec/slices/gmres.md:3,91,122`); both GMRES and FGMRES traverse the same L4 `inner_loop` differing only at the `K.Z[K.j] = z` capture (`gmres.md:104`). This does **not** constitute a "second slice needs it" — it is one call site instantiated at two `flexible` values.

- **Instance 3 (real, in-scope, NOT yet in L1+ spec)**: NLEPS Quasi-Newton inner loop at `reference/palace/palace/linalg/nleps.cpp:589-647` — a 3-condition stop with `while (it < nleps_it)` outer predicate plus inside-body breaks on `res < rtol` (converged, line 600) and `diverged_it > 10` (line 636). Different stop-reason set (`{ Converged, Diverged, MaxIt }` vs GMRES's `{ Conv, MaxDim, MaxIt }`) but the same hoist shape: a pure helper that runs N predicates and writes a `Maybe StopReason` into the carry. **However**, NLEPS has no `book/src/spec/slices/nleps.md` chapter (only L1>L0 mutation-rotation citations at `book/src/L1-L0/axpbypcz-mutation-rotation.md:127-132,294-297`). It is a candidate second consumer but not currently spec'd.

- **Non-instance (ARPACK)**: `reference/palace/palace/linalg/arpack.cpp:315-353` uses `while (true)` with an `ido` reverse-communication state machine. Loop exit is controlled by ARPACK's internal `ido` flag and the `num_conv >= nev` post-loop check; there is no in-Palace predicate on (op, conv, carry, it). Not a `check_stop_into_carry` shape.

- **Non-instance (SLEPc)**: `reference/palace/palace/linalg/slepc.cpp:687-694,1170,1516` — single call to `EPSSolve(eps)`. Iteration is entirely inside SLEPc; Palace has no loop body to migrate.

- **Non-instance (Chebyshev)**: `reference/palace/palace/linalg/chebyshev.cpp:194,265` — bounded `for (int it = 0; it < pc_it; it++)` with no convergence test and no early break. No `check_stop` shape at all (the only stop reason is `MaxIt`, which is the predicate itself).

- **Non-instance (Transient)**: `reference/palace/palace/drivers/transientsolver.cpp:77` — `for (int step = 0; step < n_step; step++)`. Same single-bounded-counter shape as Chebyshev.

- **Non-instance (PCG main loop)**: `reference/palace/palace/linalg/iterative.cpp:427-464` — `for (; it < max_it && !converged; it++)`. 2-condition stop (max-it as predicate bound; `converged` as in-body-written flag). The CG slice already absorbs this via `cg.md:215-219`'s `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)` — the witness is a single `Bool` carry field, NOT a `Maybe StopReason`. The single-flag case is the **degenerate** form of `check_stop_into_carry` (`StopReason = ()` and `Maybe () ≡ Bool`); CG already handles it without naming the helper.

**Instance count for the cycle-008 promotion criterion**:
- Strictly distinct L1+ slices with the multi-reason `Maybe StopReason` shape: **1** (`gmres.md`).
- Distinct call sites in Palace source: **2** (GMRES, FGMRES) — but variant-absorbed into 1 spec slice.
- Distinct algorithms with the shape but not yet in L1+ spec: **1** (NLEPS).

Below the cycle-008 criterion's bar ("a second slice needs it"). The closest second slice (NLEPS) is not in the corpus.

## Proposed combinator

- **Slug**: `check_stop_into_carry`
- **Layer**: L4 (where the cycle-008 theme placed the rough-in). Rationale: the helper is a pure-function combinator over typed records — `OpParams`, `Convergence`, `Krylov`, `int` → `Krylov` with one updated field. It honours `iterate-while`'s predicate-on-carry-only discipline structurally, which is an L4-layer concern. The body is L3-native (pure scalar comparison + record update); there is no L3 equivalent that does anything different. The helper is "L4 vocabulary that disappears identically under wrapper dissolution," same as `iterate_while_pure` vs `iterate_while`.
- **Signature sketch** (per the cycle-008 theme; reproduced here for the dep-map entry):

  ```text
  check_stop_into_carry :: OpParams -> Convergence -> Krylov -> int -> Krylov
  -- precondition: K.stop_reason is Nothing (helper is called when no prior stop is set)
  -- postcondition: K' is K with stop_reason updated:
  --   Just Conv    if conv.satisfied K.beta
  --   Just MaxDim  else if K.j + 1 == op.max_dim
  --   Just MaxIt   else if total_it == op.max_it
  --   Nothing      else
  ```

- **Algebraic intuition**:
  - **Idempotent on already-stopped carries**: `check_stop_into_carry op conv (K { stop_reason = Just r }) it ≡ K { stop_reason = Just r }` (helper is a no-op when a stop reason is already set — by precondition / postcondition cascade).
  - **Right-biased priority among reasons**: when multiple predicates fire simultaneously (e.g., `j+1==max_dim` AND `it+1==max_it` at the last step before forced restart), the helper picks the *first* condition in the `if/else if` cascade. This matches Palace's `||` short-circuit at `iterative.cpp:645` and is the canonical convention; it is not commutative across reasons.
  - **Pure-function discipline**: required for §3.8 trajectory pruning to discharge correctly when `inner_loop` is invoked under a final-state-only consumer. (Stated as Applicability Condition 5 in the cycle-008 theme.)
  - **No identity element**: there is no `K_id` such that `check_stop_into_carry op conv K_id it ≡ K_id` for all `op, conv, it` — even an empty Krylov triggers `MaxDim` when `max_dim = 0`, etc.

- **Variant axes** (would be enumerated on promotion):
  - **Stop-reason set**: `{Conv, MaxDim, MaxIt}` for GMRES; `{Converged, Diverged, MaxIt}` for NLEPS (hypothetical); `{Conv, MaxIt}` for CG (degenerate). The helper is parametric in the `StopReason` sum; the slice provides the per-reason predicate list. If promoted, the L4 form would be `check_stop_into_carry :: [StopCondition reason carry] -> OpParams -> Convergence -> Krylov -> int -> Krylov where StopCondition reason carry = (Predicate, Constructor)`. **But this is over-engineered for a single call site.**
  - **Stop-reason set cardinality**: 1 (single converged bool, CG-style), 2 (2-condition like PCG), 3 (GMRES, FGMRES, NLEPS). The combinator absorbs all cardinalities trivially.
  - **Predicate purity**: every Palace stop test currently observed is pure (scalar comparison + integer comparison + record field read). No monadic predicates needed.

## Proposed changes

**Verdict is defer; no proposed changes to L4 dep-map.** The helper stays as a speculative L4 helper inside the cycle-008 theme file (`book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` §Speculative L4 operators). The cycle-008 abstractor report records the promotion criterion (`reports/2026-05-27T180000Z-abstractor-gmres-inner-loop-iterate-while-migration/CYCLE.md:71`; also `scaffolding/open-questions.md:1316`) but the criterion is **not yet recorded in the theme file's §Status block** (`gmres-inner-loop-iterate-while-migration.md:196-202` lacks the "second slice" phrasing); placing it there is itself a follow-up edit that this dispatch does not propose (out of combinator-miner authority — see §Open questions / caveats #6).

The survey outcome (verdict: defer; sole current call site is GMRES/FGMRES variant-absorbed via `op.flexible`; closest second consumer is NLEPS Quasi-Newton, not yet spec'd at L1+) is recorded in this report alone. No edit to the cycle-008 theme's §Status block is proposed — the theme's status text remains as authored cycle-008. If a future integrator or follow-up dispatch wants the survey outcome reflected inside the theme file, the natural channels are (a) an Open-question entry referencing this report, or (b) a lifter or abstractor dispatch on the cycle-008 theme that re-authors §Status to incorporate the criterion-and-survey-result inline. Both are outside this dispatch's combinator-miner authority (see §Open questions / caveats #6).

## Supporting evidence

**Primary instance** (the helper's existing call site):
- `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md:36-58` — L4 `inner_loop` form invoking `check_stop_into_carry`.
- `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md:75-96` — L3 form preserving the helper call.
- `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md:130-144` — Applicability Conditions including the pure-function discipline (Condition 5).
- `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md:158-164` — §Speculative L4 operators + proposed dep-map row.
- `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md:196-202` — §Status block with the "defer until a second slice needs it" criterion.
- `reference/palace/palace/linalg/iterative.cpp:615-650` — GMRES inner loop L0 evidence; line 645 is the 3-condition break.
- `reference/palace/palace/linalg/iterative.cpp:644` — `converged = (beta < eps);` (Conv-reason source).
- `reference/palace/palace/linalg/iterative.cpp:645` — `if (converged || j + 1 == max_dim || it + 1 == max_it)` (3-condition break canonical line).

**Second-instance candidate (variant-absorbed; not a second slice)**:
- `reference/palace/palace/linalg/iterative.cpp:794-828` — FGMRES inner loop; line 824 is the textually-identical 3-condition break.
- `book/src/spec/slices/gmres.md:3` — slice header explicitly states "Lifts Palace's restarted GMRES and FGMRES solvers" as a single absorbed-variant slice.
- `book/src/spec/slices/gmres.md:91` — "The outer/inner structure is identical for GMRES and FGMRES; the (fixed-vs-flexible) axis is absorbed by the choice of basis (`V` vs. `Z`) the correction step closes over."
- `book/src/spec/slices/gmres.md:122` — "`flexible` — inspected only at the `K.Z[K.j] = z` capture and inside `apply_correction`'s basis selection. FGMRES configures this once at construction."

**Second-instance candidate (not in L1+ spec)**:
- `reference/palace/palace/linalg/nleps.cpp:589-647` — NLEPS Quasi-Newton inner loop; lines 590 (predicate `it < nleps_it`), 600 (`res < rtol` converged break), 636 (`diverged_it > 10` diverged break). Three stop reasons; same hoist shape.
- `book/src/spec/slices/` directory listing (no `nleps.md`); existing nleps references are L1>L0 mutation-rotation only: `book/src/L1-L0/axpbypcz-mutation-rotation.md:127-132,294-297` and `book/src/L1-L0/apply-linop-mutation-rotation.md:337` and `book/src/L1-L0/axpby-mutation-rotation.md:213`.

**Non-instances** (catalogued to show the survey was exhaustive on the Palace iterative-solver-and-eigenmode-and-transient surface):
- `reference/palace/palace/linalg/arpack.cpp:315-353` — `while (true)` with reverse-communication `ido` state machine.
- `reference/palace/palace/linalg/slepc.cpp:687-694` (and `:1170, :1516`) — opaque single-call `EPSSolve(eps)`.
- `reference/palace/palace/linalg/chebyshev.cpp:194,265` — bounded counter loops, no convergence test.
- `reference/palace/palace/drivers/transientsolver.cpp:77` — bounded counter loop, no convergence test.
- `reference/palace/palace/linalg/iterative.cpp:427-464` — PCG main loop; 2-condition stop, single `converged` flag carry, already absorbed by `cg.md:215-219` without naming the helper.

**Test linkage check**: no Palace unit tests under `reference/palace/test/unit/` exercise the GMRES stop test in isolation — coverage is via `models/modeeigensolver.cpp` and `ksp.cpp` consumers (`gmres.md:129` records this absence as a regression-test-slice candidate). The L0 evidence base is the source ranges above; no contradicting test evidence.

## Open questions / caveats

1. **NLEPS spec gap** (the actual reuse-blocker). The NLEPS Quasi-Newton loop (`nleps.cpp:589-647`) has the 3-condition stop shape; if it were spec'd at L1+ it would be the second slice the cycle-008 criterion asks for. NLEPS is the **non-linear eigenvalue problem driver** — it is a sibling-tier algorithm to GMRES (Krylov family) rather than a sub-component. Promoting it to L1+ is a multi-cycle effort (the full file is 952 lines including deflation, Armijo backtracking, line search, line-search Jacobian construction). This OQ records the dependency: *"`check_stop_into_carry` helper promotion is blocked on NLEPS being spec'd at L1+ as a separate slice (`book/src/spec/slices/nleps.md`); if NLEPS lands and its inner-loop migration adopts the same hoist pattern, promote at that point."*

2. **Alternative-shape question**: could the helper be parameterised over `[StopCondition reason carry]` to absorb the GMRES `{Conv, MaxDim, MaxIt}` and NLEPS `{Converged, Diverged, MaxIt}` reason sets uniformly? Yes — but this is **over-engineering for a single current call site**. The cycle-008 theme's monomorphic signature `OpParams -> Convergence -> Krylov -> int -> Krylov` (with GMRES-specific `StopReason` baked in) is appropriate for the rough-in stage. The parameterised form should be considered *after* the second consumer lands and shows whether the reason-sum factoring is worth the additional vocabulary.

3. **Variant-absorption-vs-instance-counting policy question** (cross-cutter scope, not combinator-miner scope). The cycle-008 promotion criterion "a second slice needs it" is ambiguous when one slice absorbs two Palace-source call sites via a variant axis. Should the count be (a) distinct L1+ slices, (b) distinct Palace-source call sites, (c) distinct algorithmic variants observed in the corpus? This dispatch adopted reading (a) — the strictest — to avoid premature promotion. If the integrator or meta-phase prefers reading (b), FGMRES would count as a second site and the helper would be promoted. The reading-(a) interpretation matches how the cycle-008 theme is structured (one theme covers GMRES and FGMRES uniformly via `op.flexible`); reading (b) would suggest the theme should split into two themes, which seems wrong. Recommend reading (a) as the canonical interpretation; flagging for meta-phase consideration.

4. **`check_stop` (no `_into_carry` suffix) as a candidate alternative**. The cycle-008 theme briefly mentions option (b) `iterate_while_with_stop_witness` as an alternative-combinator approach to the witness-into-carry hoist. If `iterate-while` itself were extended to support a witness-carrying variant — `iterate_while_witness :: α -> (α -> Maybe StopReason) -> (α -> Solve { state: α, ...e }) -> Solve { final_state, trajectory, stop: Maybe StopReason }` — the helper would become unnecessary (the predicate would return `Maybe StopReason` directly, the witness lives in the combinator's return rather than the carry). This is a separate combinator-miner pattern, not the same one this dispatch is about; flagging as an Open question to record the design alternative. The cycle-008 theme's option (b) is the abstraction-level question that would arbitrate this choice.

5. **No standalone L4>L3 theme exists for `iterate-while` yet** (cycle-007 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` still open). Until that theme lands and resolves the trajectory-accumulator dissolution question generically, the helper's L3 form remains pinned to the cycle-008 GMRES-specific theme's §"L3 form" section. Not a blocker for the defer verdict; flagging for completeness.

6. **Combinator-miner authority caveat**: this dispatch's verdict is "defer" — there is no dep-map rough-in row to add. The §Proposed changes block suggests an append-only edit to the cycle-008 theme's §Status section. This edit is technically outside the combinator-miner's stated authority ("just the dep-map entry"); a stricter reading would record the verdict only in this report and leave the cycle-008 theme's §Status untouched. Routing the §Status-edit decision to the integrator per cycle-009 dispatch-spec ("STRICTLY proposed-changes channel — do NOT directly edit `book/`"). The integrator may elect to skip the §Status edit and rely on this report alone as the survey record.

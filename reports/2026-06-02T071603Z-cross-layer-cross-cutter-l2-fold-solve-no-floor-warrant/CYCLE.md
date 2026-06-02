---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-02T071603Z
scope: L3↔L2 cross-cut — L2/fold_solve NO-FLOOR-WARRANT consistency-confirm
status: pending
integrated_at: 2026-06-02T073705Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (cycle-060 D2, observation-only — NO book mutation). Verdict warrant-consistent YES: fold_solve owes NO L2/fold_solve.md floor (per-step body is the opaque MFEM ode->Step leaf with NO L2 composition, unlike eigsolve's apply_linop > ksp_solve body; the substantive L3>L2 content is the outer-sweep erasure). Verified consistent across the L3 entry + the L3>L2 theme + the absence-by-warrant on disk; recommend AGAINST authoring L2/fold_solve.md (would be the §1d degenerate-mirror smell); routed to the batch-18 meta-phase for formal close (RESOLVED-BY-WARRANT). The dispatch-time OQ intake fold-solve-l2-floor-no-warrant-descent-complete verified present + NOT duplicated; the repairer-routed :82 'sole act' cosmetic-residue note (fold-solve-time-step-body-sole-act-phrasing-cosmetic-residue) was absent + is now appended. No count delta. See reports/cycle-060-integrator-staging/STAGING.md + reports/2026-06-02T073705Z-integrator-finalize-cycle-060/CYCLE.md."
---

# CYCLE: Cross-layer observation — l2-fold-solve-no-floor-warrant

## Summary
Cycle-060 D2 observation-ONLY consistency-confirm. The c059 D1 dispatch recorded INLINE the warrant that `fold_solve` owes **no L2 floor entry**: its per-step body is the opaque MFEM `ode->Step` integrator leaf with NO L2 composition (unlike `eigsolve`, whose per-step body opens to `apply_linop ▷ ksp_solve`), so the substantive L3>L2 content is the outer-sweep erasure, NOT a body-composition rotation, and the L2 RHS is a by-design fold-by-role form modeled on `L2/eigsolve.md`, NOT a degenerate `L2/fold_solve` mirror. I verified this warrant is **consistent across all three places it must be coherent** — the L3 entry's frontmatter + body, the L3>L2 theme's opaque-leaf rationale, and the absence-by-warrant of `book/src/L2/fold_solve.md` on disk. **Warrant consistent: YES.** Disposition: descent complete, no L2 floor owed — route the formal close to the batch-18 meta-phase. This is the anti-mirror discipline applied at the L2 floor (per the vocabulary-shift redirect §1d smell): a degenerate `L2/fold_solve` mirror would be the smell; its absence-by-warrant is correct.

## Observation kind
**Coverage gap (NEGATIVE / by-warrant) — confirmed NON-gap.** The integrator-signals tail flagged a possible L2-floor coverage gap (`book/src/L2/fold_solve.md` absent). On cross-layer inspection the absence is **correct by warrant**, NOT a gap: there is no L2 floor owed because the per-step body does not decompose into L2 primitives. This is the inverse of the usual coverage-gap finding (an L_{n+1} operator with no lowering) — here the L_n floor is *deliberately* absent and the L_{n+1}>L_n theme is the substantive home. No follow-up authoring is warranted; the opposite (authoring `L2/fold_solve.md`) would manufacture the exact degenerate mirror the warrant rejects.

## Specific finding

The warrant is recorded coherently in all three required places:

### 1. `book/src/L3/fold_solve.md` — frontmatter + body: CONSISTENT
- **Frontmatter `lowers_to:` (`:7-8`)** points at `book/src/L2/index.md` (NOT a `book/src/L2/fold_solve.md`) and states verbatim: *"no standalone L2/fold_solve entry — the per-step body is an opaque ode->Step leaf that does NOT decompose into L2 primitives, so the L3>L2 hop is the substantive outer-sweep erasure to an L2 fold-by-role, NOT a body-composition rotation."* No "L2 floor forthcoming" / "L2 entry pending" claim anywhere.
- **§"Downward to L2" (`:32`)** — explicitly *"there is no standalone L2/fold_solve entry"* + *"the per-step body does NOT decompose into L2 primitives"* + names the L3>L2 hop as the substantive outer-sweep erasure to the `fold-solve-time-step-body` theme.
- **§Dependencies "Adjacent-layer siblings" (`:139`)** — *"L2: no standalone L2/fold_solve entry; the L3>L2 hop is the outer-sweep erasure to a fold-by-role."*
- **§"L3 vs L2 distinction" (`:158-163`)** — *"there is no standalone L2/fold_solve entry"* + the by-design fold-by-role rationale + *"this is NOT the eigsolve body-identity-on-apply_shift_invert shape."*
- The entry's own status (`partial-obstruction`) and the carry-threading + opaque-per-step-leaf framing are internally consistent with the no-L2-floor warrant.

### 2. `book/src/L3-L2/fold-solve-time-step-body.md` — opaque-leaf rationale: CONSISTENT
- **§"L2 form (RHS)" (`:53-68`)** records exactly the warrant: *"There is no standalone L2/fold_solve entry ... the L2 RHS is the fold-by-role form the iteration-rotation erasure produces — the same shape L2 eigsolve takes for its eigen-iteration fold (named by role, opened only at the body)."* The `time_step_op` is *"the opaque per-step integrator leaf, the SAME at L2 as at L3 (it does NOT decompose into L2 base primitives)."*
- **§"2. Opaque per-step leaf → opaque per-step leaf (identity, stays opaque)" (`:76-78`)** — the per-step `ode->Step` stays opaque at L2; *"this theme has no body-identity-in-form half ... the whole substantive content of the theme is the outer-sweep erasure (rewrite 1)."*
- **§"What this lowering does NOT cover" (`:88-92`)** — *"No body-composition rotation. This theme is NOT the eigsolve body-identity-on-apply_shift_invert shape — fold_solve's per-step body has no L2 composition."*
- **§Justification kind (`:103-110`)** — `structural` + secondary `obstruction (opaque-library-ownership)` on the per-step leaf; the abstraction-direction note confirms L3→L2 forward narration.
- **§Verified-against (`:122-125`)** — explicitly records *"No book/src/L2/fold_solve.md — there is no standalone L2 entry ... the fold-by-role treatment follows L2 eigsolve."* This is the by-design absence stated in the theme's own audit linkage.

### 3. `book/src/L2/fold_solve.md` — ABSENT on disk: CORRECT
- `ls book/src/L2/fold_solve.md` → `No such file or directory` (exit 2); no `fold`-matching file under `book/src/L2/`. The absence is the warrant's correct realization, NOT a gap.
- The L2 RHS model `book/src/L2/eigsolve.md` is PRESENT on disk (confirmed) — the fold-by-role form the theme's RHS is modeled on, so the no-floor warrant does not strand the RHS (it has a live referent for its shape).

### L0 anchor re-verification (the warrant's evidentiary keystone)
- `palace/models/timeoperator.cpp:410` — `ode->Step(sol, t, dt)` verified exact via `palace-codemap read_range` (lines 405-413): `TimeOperator::Step` is a thin forwarder whose substantive act is `ode->Step(sol, t, dt)` (bracketed by a `dt` save/restore guard at `:409`/`:412`), dispatching into the MFEM `ODESolver`. This confirms the per-step body IS the opaque library leaf the warrant rests on (no L2 composition to decompose into) — the evidentiary basis for "no L2 floor owed" is intact.

## Recommendation
**Defer to meta-phase for formal close — no authoring follow-up.** The warrant is consistent across all three places; descent is complete and no L2 floor is owed. Route the formal close (mark the `fold_solve` L2-floor question RESOLVED-BY-WARRANT, descent complete) to the **batch-18 meta-phase** (fires after this cycle's finalize). Explicitly do NOT dispatch a harvester/abstractor to author `book/src/L2/fold_solve.md` — that would manufacture the degenerate `L2/fold_solve` mirror the warrant rejects (the §1d identity-in-named-terms smell). No lifter re-anchor is needed (no stale claim found). No lowering-verifier deepening is needed (the L3>L2 theme is already `firm` on the structural rotation with the per-step leaf correctly recorded as `obstruction (opaque-library-ownership)`).

## Supporting evidence
- `book/src/L3/fold_solve.md:7-8` (frontmatter `lowers_to:` → `L2/index.md`, no L2 floor claim), `:32` (§Downward to L2), `:139` (§Dependencies adjacent siblings), `:158-163` (§L3 vs L2 distinction).
- `book/src/L3-L2/fold-solve-time-step-body.md:53-68` (§L2 form RHS, fold-by-role modeled on L2/eigsolve), `:76-78` (opaque-leaf identity, no body half), `:88-92` (§What this lowering does NOT cover), `:103-110` (§Justification kind), `:122-125` (§Verified-against, "No book/src/L2/fold_solve.md").
- `book/src/L2/fold_solve.md` — ABSENT on disk (verified, exit 2). `book/src/L2/eigsolve.md` — PRESENT (the RHS model).
- `palace/models/timeoperator.cpp:405-413` (verified via `palace-codemap read_range`) — `ode->Step(sol, t, dt)` at `:410`, the opaque per-step leaf keystone.

## Open questions / caveats
- The L3 entry (`:145`) and the L3>L2 theme (`:92`, `:158`) both gate the **driven-PROM SweepAdaptive state-generated schedule-source** variant on the cap's OQ `fold-solve-greedy-schedule-source-generalization` (batch-18). That OQ is orthogonal to this no-L2-floor warrant: even the state-generated superset's per-step body is the same opaque-library leaf (`drivensolver.cpp:389` `prom_op.FindMaxError(...)` is a library sampler call, parallel to `ode->Step`), so the no-L2-floor warrant would carry to the superset too — but that is the OQ's scope to confirm, not this dispatch's. Recorded as an intake note (no action this cycle).
- This is a consistency-confirm, NOT a re-derivation: I did not re-audit whether the per-step body *could* in principle decompose into L2 primitives (the c059 D1 abstractor + the firm L3>L2 theme already established the opaque-leaf finding against `timeoperator.cpp:407-413`; I re-verified the keystone anchor `:410` and found it intact). If a future producer believes the `ode->Step` leaf admits an L2 decomposition, that would reopen the warrant — but no evidence of that surfaced.

---
agent: abstractor
invoked_at: 2026-05-27T180000Z
scope: L4>L3 theme sketch — gmres-inner-loop-iterate-while-migration (rough-in)
status: integrated
integrated_at: 2026-05-27T18:35:15Z
integration_commit: e4929aa
integration_notes: cycle-008 pass 5 (wave-1). New L4>L3 rough-in theme (~213 lines); LHS migrated L4 form with witness-into-carry hoist via speculative check_stop_into_carry helper, RHS L3 form, 4-axis variant pass-through (pc_side, gs_orthog, flexible, max_dim). Status answered-by-rough-in-theme on cycle-007 OQ gmres-inner-loop-iterate-while-migration; firming requires upstream gmres.md §L4 self-rotation (cycle-009+ candidate).
inputs:
  - book/src/L4/iterate-while.md (cycle-007 firm)
  - book/src/L4/iterate-while-with-prev.md (cycle-007 firm)
  - reference/palace/palace/linalg/iterative.cpp:614-650 (GMRES inner Arnoldi loop body; the outer Mult continues 651-705 with back-substitution + restart-handling + summary print, out-of-scope for this theme)
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (cycle-006 firm; precedent)
  - book/src/spec/slices/gmres.md (L4 v0.1 / v0.2 / v0.3 / v0.4 / v0.5 / v0.6 evolution)
  - book/src/concepts/derived-view-hoisting.md (§3.8 collapse rule)
  - book/src/L4/index.md (dep-map)
  - book/src/L4-L3/index.md (theme list)
  - book/src/SUMMARY.md (Part registration)
  - scaffolding/open-questions.md (OQ gmres-inner-loop-iterate-while-migration; OQ iterate-while-l3-rendering-trajectory-accumulation-gap)
---

# CYCLE: L4>L3 theme sketch — gmres-inner-loop-iterate-while-migration (rough-in)

## Summary

The cycle-007 harvester on the iterate-while family produced firm L4 entries for both `iterate_while` (Form A) and `iterate_while_with_prev` (Form B); the GMRES slice's L4 section (`gmres.md` §L4 v0.1–v0.6) currently writes its `inner_loop` as an inline tail-recursive `Solve`-monad function that hand-rolls exactly the value-threading-with-extras shape that `iterate_while` was designed to abstract. OQ `gmres-inner-loop-iterate-while-migration` (cycle-007, source: harvester wave-2 §"Open questions / caveats" item 2) routes the migration to a cycle-008+ abstractor or lifter dispatch.

This dispatch sketches the L4>L3 lowering theme for the migrated GMRES inner loop — under the (speculative) assumption that the GMRES `inner_loop` will be re-rendered to invoke `iterate_while` directly (as CG v0.4 already does at `cg.md:215-219`). The theme is **rough-in / speculative**: the upstream GMRES re-rendering itself is a separate v0.6→v0.7 self-rotation on `gmres.md`, not part of this dispatch, but the theme captures (a) what shape the migrated L4 form would take, (b) what L3 form it lowers to under `krylov-step-typed-wrapper-dissolution`-style dissolution, (c) which design tensions surface (witness-carrying `StopReason` vs. predicate-on-carry-only discipline; trajectory-vs-`final_state`-pruning under §3.8), and (d) the speculative L4 vocabulary that promotion to firm would require (one operator: `check_stop_into_carry`, a witness-into-carry hoist).

The theme is structurally a **post-condition on the upstream gmres.md migration**: when that migration lands, this theme is the L4>L3 rotation that erases the L4 wrapper machinery; both must align. Status `rough-in` reflects the dependency.

## Proposed changes

```edit:book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
[create file — see "Theme file content" section at the bottom of this report for the full body]
```

```edit:book/src/L4-L3/index.md
[append a new row to the theme-list table in §"Theme list", after the existing `krylov-step-typed-wrapper-dissolution` row. Per cycle-006 friction-ledger `rough-in-rows-must-be-plain-text-when-anchor-missing`: the anchor file IS being created in the same dispatch (above), but to remain safe under serial per-report ordering (the integrator-per-report applies one report at a time and a same-cycle order swap could leave the row pointing to a missing anchor), the row uses plain-text slug form. The integrator-finalize may upgrade to markdown link form during book-build once both edits are applied. The row to append:

| `gmres-inner-loop-iterate-while-migration` *(rough-in; this dispatch creates the anchor file at `./gmres-inner-loop-iterate-while-migration.md`)* | L4 migrated GMRES inner-loop form: `inner_loop op conv K0 = iterate_while K0 (\K -> isNothing K.stop_reason) (\K -> ...body... ; pure { state, residual_norm, breakdown_token })` with `check_stop_into_carry` writing the witness into the carry's `stop_reason` field. | L3 tail-recursive value-threading worker `gmres_inner_loop_L3_worker op conv K s` with the `Solve` monad dissolved to explicit `s` threading, trajectory pruned to `[]` per Law 1 (consumer reads only `(K_final, K_final.stop_reason)`), and the `iterate_while` combinator dissolved per the parallel `krylov-step-typed-wrapper-dissolution` theme. | `structural` + secondary `reduction-chain` and `empirical-match` | `rough-in` (cycle-008 abstractor; depends on upstream gmres.md §L4 v0.6→v0.7 self-rotation, routed to cycle-008+ lifter on `gmres.md §L4`) |
]
```

```edit:book/src/SUMMARY.md
[add chapter entry under the `# L4 > L3 — Lowering` Part, after the existing `- [krylov-step-typed-wrapper-dissolution](./L4-L3/krylov-step-typed-wrapper-dissolution.md)` line:

- [gmres-inner-loop-iterate-while-migration](./L4-L3/gmres-inner-loop-iterate-while-migration.md)
]
```

## Speculative L4 operators proposed

This theme surfaces **one** speculative L4 vocabulary candidate that the migration needs to honour the variant-absorption discipline at the predicate site:

- **`check_stop_into_carry`** (rough-in helper, not a combinator). Intended signature (best guess based on the gmres.md v0.6 form):

  ```text
  check_stop_into_carry
    :: OpParams
    -> Convergence
    -> Krylov
    -> int                       -- total_it (SimState.it snapshot)
    -> Krylov                    -- Krylov augmented with a stop_reason :: Maybe StopReason field
  ```

  **Motivation**: the gmres.md v0.6 form runs `check_stop op conv K3 s.it` *inside* the `inner_loop` body and pattern-matches on `Maybe StopReason` to decide whether to recurse. The L4 `iterate_while` predicate is `α -> Bool` and reads the carry *only* — no `OpParams`, no `Convergence`, no `total_it`. Migration therefore requires folding the `check_stop` call into the step body's return, writing the resulting `Maybe StopReason` (or a derived `converged :: Bool` plus a `stop_reason :: StopReason` field) into the carry `Krylov`, and reading it from the predicate. `check_stop_into_carry` is the hoisting helper that performs this fold; promoting it to firm gives the migration a named landing site for the witness-hoist that today is open-coded.

  Alternative shape (also speculative, less likely the right choice): an extended `iterate_while_with_stop_witness` combinator whose body returns `α + StopReason` instead of `α`, and whose predicate is `α -> Bool` only triggered when the body returns `Left α`. This would preserve the value-threading-with-extras shape but adds a *new combinator* rather than a hoisting helper — heavier vocabulary surgery for the same effect. Defer to harvester to choose.

  **Promotion criterion** (per CLAUDE.md "unimplemented Palace stub policy" applied to speculative-L4-operators): promote only if a second slice (e.g., MINRES on the unimplemented-stub axis, or BiCGStab) finds the witness-hoist necessary. Otherwise, GMRES can keep `check_stop` inline at the slice level and the migration uses an in-step expression rather than a named L4 helper.

This theme does **not** propose new combinators — `iterate_while` is the firm combinator the migration consumes. The only speculative vocabulary is the `check_stop_into_carry` helper above; no `iterate_while_pure` / `_with_prev` rough-ins (both already firm at L4).

## Supporting evidence

L0 (the Palace inner-loop pattern this theme abstracts):

- `reference/palace/palace/linalg/iterative.cpp:614-650` — the GMRES `Mult` inner Arnoldi loop. `int j = 0; for (;; j++, it++) { ... if (converged || j + 1 == max_dim || it + 1 == max_it) { it++; break; } }`. The three-way break-on-stop at line 645 is the L0 evidence for the v0.6 `check_stop` three-condition test; the `for (;; j++, it++)` shape with predicate-in-body break is the L0 evidence for `iterate_while`'s predicate-fires-first discipline being the rotation target (the break becomes the negated predicate after migration).
- `reference/palace/palace/linalg/iterative.cpp:642-644` — the residual-proxy compute `beta = std::abs(s[j + 1])` and `converged = (beta < eps)` immediately before the break check. This is the L0 evidence that GMRES's `converged` is a per-step computed carry field (set in the body, read by the predicate on the next iteration via the carry), matching `iterate_while`'s [`predicate-on-extras-anti-pattern`](../../book/src/L4/iterate-while.md#predicate-on-extras-anti-pattern) resolution.
- `reference/palace/palace/linalg/iterative.cpp:627-640` — the per-step body sequence (`ApplyBA`, `OrthogonalizeIteration`, `Norml2`, `ApplyPlaneRotation` ×j + `GeneratePlaneRotation` + `ApplyPlaneRotation` ×2). This is the L0 evidence for the body sequence that survives the migration textually unchanged (the body is identity-in-form under L4>L3>L2; only the wrapper rotates).
- `reference/palace/palace/linalg/iterative.cpp:645-649` — the break condition `if (converged || j + 1 == max_dim || it + 1 == max_it) { it++; break; }`. The three disjuncts map one-to-one to the v0.6 `StopReason` constructors (`Conv`, `MaxDim`, `MaxIt`); the `it++` after the break is the off-by-one that v0.6 `check_stop` and gmres.md §L4 v0.1's `should_stop_inner` both internalize.

L4 source (the form of the LHS this theme rewrites):

- `book/src/spec/slices/gmres.md:459-470` (v0.1 inline `inner_loop` shape) — the rendering this theme assumes will migrate. The migration replaces the inline `inner_loop op conv K = do { ...; if conv.satisfied K3.beta || K3.j + 1 == op.max_dim || s.it == op.max_it then pure K3 else inner_loop op conv K3{ j = K3.j + 1 } }` with `inner_loop op conv K = iterate_while K p (\K -> do { ...; pure { state: K3{ j = K3.j + 1 }, residual_norm: K3.beta, breakdown_token: bt } })` where `p` reads the witness-augmented carry.
- `book/src/spec/slices/gmres.md:1067-1078` (v0.6 `inner_loop` + `check_stop` shape) — the current stable form. This is the form the migration would lift from; the key shape is `inner_loop` returning `(Krylov, StopReason)` to preserve the witness for `classify`. The migration must decide whether to (a) hoist `StopReason` into the carry via `check_stop_into_carry`, or (b) extract it at the outer level by re-running `check_stop` on the returned final carry. This theme proposes (a); (b) is feasible but recomputes a derived view.
- `book/src/L4/iterate-while.md` §Signature, §Semantics, §"Predicate-on-extras anti-pattern" — the firm L4 row that the migration consumes. The predicate-on-carry-only discipline is the load-bearing constraint that forces the witness-hoist; the §Semantics extras-record contract `{ residual_norm: Scalar, breakdown_token: BreakdownTag }` (named in `iterate-while.md` §Evidence at the GMRES line) is the trajectory shape this theme inherits.
- `book/src/L4/iterate-while.md:232` — explicit evidence pointer: *"reference/palace/palace/linalg/iterative.cpp:615 — GMRES inner Arnoldi loop. for (;; j++, it++) with break-on-converged at line 644 is the second Palace iteration shape; the predicate-in-body break corresponds at L4 to s.converged being a carry field set inside the step body and read by the predicate on the next iteration. (The current GMRES slice writes this as a tail-recursive inner_loop; migration to iterate_while is filed as a cycle-007 follow-up OQ.)"* — the OQ this theme begins addressing.
- `book/src/spec/slices/cg.md:215-219` — the precedent rendering pattern. CG v0.4 already uses `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)` directly; the GMRES migration applies the same pattern with the witness-augmented carry.

L4>L3 source (the precedent theme this dispatch parallels):

- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for `iterate_while` looks like" — the existing L4>L3 dissolution sketch for `iterate_while` itself. This theme inherits that L3 form for the wrapper-dissolution piece; the GMRES-specific additions are (a) the carry's `stop_reason` field threading through `check_stop_into_carry` and (b) the extras-record shape `{ residual_norm, breakdown_token }`. The trajectory-accumulation discrepancy (OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`; cycle-007 lowering-verifier verdict-(c)) applies to this theme too: when the consumer reads only `final_state` (which is the GMRES outer `restart_cycle` case — `final_state` is the final `Krylov` plus its `stop_reason`; the trajectory is only consumed if `print_opts.iterations` is on), Law 1 of `iterate-while.md` collapses the trajectory to `[]` and the L3 form is the single-readout shape. (Section-anchor reference rather than line range: the parallel cycle-008 lifter dispatch on this same file is replacing/expanding the §"What the L3 form for iterate_while looks like" subsection; the section anchor is stable across the lifter edit, the line numbers are not.)

Concept references:

- `book/src/concepts/derived-view-hoisting.md` §"Worked example: CG residual norm" — the §3.8 collapse rule worked example. GMRES's `K.beta` (LS residual proxy) and `bt` (breakdown token from `CheckDot(beta, ...)` at `iterative.cpp:643`) are the GMRES analogues of CG's `res = sqrt|beta|`. The §3.8 pruning applies: consumers reading only `(final_state.Krylov, final_state.stop_reason)` cause both extras to be pruned by the L4 pruning rewrite.
- `book/src/concepts/sequential-obstruction.md` — referenced for completeness. The `ls_update_column` recurrence inside the body remains a sequential obstruction at L3 (per gmres.md §L3 obstruction record); the migration to `iterate_while` does NOT change the body-level obstruction classification, only the wrapper around the body.

## Open questions / caveats

Three open questions surface from this rough-in, all routed to follow-up cycles:

1. **Upstream gmres.md migration dependency**. This theme assumes a v0.6→v0.7 self-rotation on `gmres.md` §L4 that re-renders `inner_loop` as an `iterate_while` call. That rotation has not been authored; if it lands with a different shape than the one sketched here (e.g., picks alternative-combinator option (b) `iterate_while_with_stop_witness` instead of the witness-hoist option (a)), this theme's LHS needs revision. **Routes to cycle-008+ lifter** on `gmres.md §L4`. Friction-ledger candidate: themes-depending-on-upstream-slice-self-rotations.

2. **Whether to promote `check_stop_into_carry` to a firm L4 row** is itself a deferred decision. The witness-into-carry hoist is one possible resolution; the alternatives (b) extended combinator `iterate_while_with_stop_witness`, or (c) re-running `check_stop` post-loop at the outer-level (paying one redundant evaluation of a pure function), are both viable. **Routes to cycle-008+ harvester** after the gmres.md migration lands; the harvester chooses based on which alternative the upstream rendering picks.

3. **Form B opportunity** (first-iteration-unrolling on GMRES). The first GMRES inner step *does* have a structural difference from subsequent steps: `K.s[0] = β` at line 612 (before the inner loop) initialises the RHS, and the first `j = 0` iteration has no prior rotations to replay (the `for (int k = 0; k < j; k++) ApplyPlaneRotation(...)` at line 634 has zero iterations when `j = 0`). This is a *trivial* first-iteration difference (the body is shape-invariant; only a zero-length inner loop differs), and likely does NOT motivate Form B adoption. CG v0.5 adopted Form B because `beta_prev` had no defined value at iteration zero; GMRES's analogous `cs[k] / sn[k]` for `k = 0` are never read on the first iteration but are also never undefined (the rotation-register arrays are initialised lazily; the access pattern `for (k = 0; k < j; k++) ...` is empty when `j = 0`). Provisional verdict: Form B is not warranted for GMRES; the migration uses Form A (`iterate_while` not `iterate_while_with_prev`). **Routes to cycle-008+ combinator-miner or first-iteration-unrolling-analysis** for confirmation.

Two design caveats embedded in the rough-in:

- **Carry vs. closure threading of `Convergence` and `OpParams`**. CG v0.4's `iterate_while s0' (\s -> ...) (\s -> cg_step opA eps s)` closure-captures `opA` and `eps` in both the predicate and the step body. GMRES does the same with `op` and `conv`. This is structural at the slice level (the closure capture is inside the `inner_loop op conv K0 = iterate_while ...` definition; `op` and `conv` are already lexically in scope). No new vocabulary needed; flagging only because the predicate's `α -> Bool` signature could in principle force these into the carry. Per CG v0.4 precedent, they stay in the closure.

- **Trajectory consumption in GMRES**. GMRES's extras `{ residual_norm: K.beta, breakdown_token: bt }` are read by `print_opts.iterations` (the per-iteration print in `iterative.cpp:617-621`) and by the `summary` print at `iterative.cpp:689-702`. Neither consumes the trajectory as a list — both are streaming/last-value consumers. Under Law 1, this means consumers read only `final_state` (the final `K.beta` for the summary; per-iteration printing is a side-effect outside the value-threaded form and lifts to a `tell`-style monad effect, NOT a trajectory read — this is OQ `iterate-while-log-effect-vs-trajectory-channel`, cycle-007). The trajectory therefore prunes to `[]` per §3.8; the L3 form is the single-readout shape per the cycle-007 lowering-verifier verdict-(c) on the companion `iterate-while-l3-rendering-trajectory-accumulation-gap` OQ.

---

## Theme file content (full text written to book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md)

(reproduced for the integrator)

```markdown
# gmres-inner-loop-iterate-while-migration

The L4>L3 lowering theme for the GMRES inner Arnoldi loop, under the (speculative) re-rendering of `gmres.md` §L4's `inner_loop` as a direct invocation of the firm L4 [`iterate-while`](../L4/iterate-while.md) combinator. The theme is **rough-in** — it depends on an upstream self-rotation on `gmres.md` §L4 (v0.6→v0.7) that has not yet been authored; the theme captures (a) what L4 form the migration would produce, (b) what L3 form it lowers to via wrapper dissolution, and (c) which design tensions surface (witness-carrying `StopReason` vs. predicate-on-carry-only; trajectory pruning under §3.8). When the upstream rotation lands, this theme is firmed against it (or revised if the rotation picks a different shape).

## Slug

`gmres-inner-loop-iterate-while-migration`

## Context

The cycle-007 harvester promoted [`iterate-while`](../L4/iterate-while.md) and [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) to firm L4 rows (closing cycle-006 OQ `iterate-while-l4-anchor-missing`). The harvester's wave-2 output flagged the GMRES inner-loop migration as a natural follow-up (OQ `gmres-inner-loop-iterate-while-migration`, cycle-007). The CG slice already renders its solve loop as `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)` at `cg.md:215-219`; the GMRES slice renders its inner loop as an inline tail-recursive `Solve`-monad function at `gmres.md:459-470` (v0.1) through `:1067-1078` (v0.6). Both forms are tail-recursive value-threading folds; the migration is the recognition that the GMRES form is an `iterate_while` invocation with the witness-into-carry hoist applied to the v0.6 `StopReason` structure.

This theme parallels [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) in shape: the L4 wrapper machinery dissolves into L3 value-threading; the body's primitive sequence (apply_BA, orthogonalize, ls_update_column, modify-it, carry-update) survives textually unchanged. The GMRES-specific additions over the krylov-step theme are (a) the carry's `stop_reason :: Maybe StopReason` field threading through `check_stop_into_carry` (the speculative L4 helper), (b) the extras-record shape `{ residual_norm: Scalar, breakdown_token: BreakdownTag }`, and (c) the §3.8 trajectory pruning resolved under the GMRES consumer pattern (per-iteration printing is a logging side-effect outside the trajectory; the summary print reads only `final_state.K.beta`).

The theme does NOT cover the upstream gmres.md self-rotation itself (that is a separate lifter dispatch on `gmres.md §L4`); it covers the L4>L3 lowering *of the migrated form*. The theme is therefore a post-condition on the upstream migration: when the migration lands at gmres.md v0.7, this theme is the L4>L3 dissolution applied to it.

## L4 form (LHS)

The migrated GMRES inner loop, as it would appear in `gmres.md` §L4 v0.7 (speculative; this is the LHS of the rewrite):

```text
-- The Krylov carry is augmented with a stop_reason field that check_stop_into_carry writes.
type Krylov = {
  V :: Vec[],
  Z :: Vec[] | null,
  H :: Dense,
  s :: DenseVec,
  cs :: DenseVec,
  sn :: DenseVec,
  j :: int,
  beta :: real,
  stop_reason :: Maybe StopReason   -- hoisted from v0.6's check_stop return
}

-- The migrated inner_loop: an iterate_while invocation with op and conv closure-captured.
inner_loop :: OpParams -> Convergence -> Krylov -> Solve (Krylov, StopReason)
inner_loop op conv K0 = do
  result <- iterate_while
              K0
              (\K -> isNothing K.stop_reason)                      -- predicate reads carry only
              (\K -> do                                            -- step body, Solve-threaded
                let (w, z)      = apply_BA op K.j (K.V `at` K.j)
                let K1          = if op.flexible then K { Z = K.Z `with` (K.j, z) } else K
                let (v_next, h) = orthogonalize op (K1.V `slice` (0, K1.j)) w
                let K2          = K1 { V = K1.V `with` (K1.j + 1, v_next) }
                let K3          = ls_update_column K2 h
                modify (\s -> s { it = s.it + 1 })
                s <- get
                let K4          = check_stop_into_carry op conv K3 s.it     -- writes stop_reason
                let K5          = if isNothing K4.stop_reason
                                    then K4 { j = K4.j + 1 }
                                    else K4
                pure { state: K5, residual_norm: K5.beta, breakdown_token: bt_of K5 }
              )
  -- result :: { final_state: Krylov, trajectory: [{ residual_norm, breakdown_token }] }
  let K_final = result.final_state
  pure (K_final, fromJust K_final.stop_reason)                     -- witness is in the carry
```

Three load-bearing structural moves over the v0.6 inline form:

1. **Predicate reads carry only** (`\K -> isNothing K.stop_reason`). This honours [`iterate-while`](../L4/iterate-while.md)'s §Signature point 1: the predicate's type is `α -> Bool`, no `OpParams`, no `Convergence`, no `total_it`. The v0.6 predicate `conv.satisfied K3.beta || K3.j + 1 == op.max_dim || s.it == op.max_it` reads three things outside the carry; the migration folds all three into the `stop_reason` carry-field by running `check_stop` in the body and writing the result.

2. **`check_stop_into_carry` is the witness-hoist helper** (speculative L4 helper; see §Speculative L4 operators below). It runs the v0.6 three-condition `check_stop` and writes the resulting `Maybe StopReason` into `K.stop_reason`. The predicate then reads `K.stop_reason` and stops when it is `Just _`.

3. **Extras-record shape `{ residual_norm, breakdown_token }`** matches the [`iterate-while.md`](../L4/iterate-while.md) §Signature evidence for GMRES (line 232 cites "GMRES: { residual_norm: Scalar, breakdown_token: BreakdownTag }"). The trajectory accumulates these per-step; under Law 1, when the outer consumer reads only `(K_final, K_final.stop_reason)` (the GMRES case — per-iteration printing is a `tell`-style log effect, NOT a trajectory consumption), the §3.8 pruning rewrites the body to omit the extras computation.

The body's primitive sequence (`apply_BA`, `orthogonalize`, `ls_update_column`, `modify`, carry-update) is textually unchanged from the v0.6 form modulo the addition of `check_stop_into_carry` and the predicate-shape rotation.

## L3 form (RHS)

The L3 form dissolves the wrapper per [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) §"L3 form": the `Solve` monad becomes explicit `(K, s) -> (K', s')` positional threading; `iterate_while` becomes a tail-recursive worker; the trajectory accumulator is pruned per the GMRES consumer pattern (consumer reads `final_state` only ⇒ trajectory is `[]`; the body's extras computation is omitted).

```text
gmres_inner_loop_L3 :: OpParams -> Convergence -> Krylov -> SimState -> (Krylov, StopReason, SimState)
gmres_inner_loop_L3 op conv K0 s0 =
  let (K_final, s_final) = gmres_inner_loop_L3_worker op conv K0 s0
  in (K_final, fromJust K_final.stop_reason, s_final)

gmres_inner_loop_L3_worker :: OpParams -> Convergence -> Krylov -> SimState -> (Krylov, SimState)
gmres_inner_loop_L3_worker op conv K s =
  if isNothing K.stop_reason
    then
      let (w, z)      = apply_BA op K.j (K.V `at` K.j)              -- L3-native global op chain
      let K1          = if op.flexible then K { Z = K.Z `with` (K.j, z) } else K
      let (v_next, h) = orthogonalize op (K1.V `slice` (0, K1.j)) w   -- L3 obstruction internal to orthog under MGS
      let K2          = K1 { V = K1.V `with` (K1.j + 1, v_next) }
      let K3          = ls_update_column K2 h                          -- L3 sequential obstruction on small-dense state (gmres.md §L3)
      let s'          = s { it = s.it + 1 }                            -- dissolved modify
      let K4          = check_stop_into_carry op conv K3 s'.it         -- L3-native: pure scalar comparison + record update
      let K5          = if isNothing K4.stop_reason
                          then K4 { j = K4.j + 1 }
                          else K4
      in gmres_inner_loop_L3_worker op conv K5 s'
    else (K, s)
```

Four structural differences from the L4 form, all at the wrapper level (none at the body level):

1. **`Solve` monad dissolves to explicit `s` threading**, identical to `krylov-step-typed-wrapper-dissolution` §"L3 form" rotation 1. The `modify (\s -> s { it = s.it + 1 })` becomes the let-bound `s' = s { it = s.it + 1 }`. No new semantics; just the `StateT` desugaring.

2. **`iterate_while` dissolves to the tail-recursive worker `gmres_inner_loop_L3_worker`**, identical to `krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for `iterate_while` looks like"'s `iterate_while_L3` sketch. The predicate `isNothing K.stop_reason` becomes the recursion's branch test; the body becomes the recursion's let-chain.

3. **Trajectory accumulator dissolves to nothing** (the GMRES consumer pattern), per Law 1 of [`iterate-while`](../L4/iterate-while.md) and the cycle-007 lowering-verifier verdict-(c) on OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`. The outer consumer (`restart_cycle`'s caller) reads `(K_final, K_final.stop_reason, s_final)` only; the per-step `{ residual_norm, breakdown_token }` is not threaded into the L3 return. Per-iteration printing (the `print_opts.iterations` block at `iterative.cpp:617-621`) is a logging-channel side-effect at L4 (OQ `iterate-while-log-effect-vs-trajectory-channel`, cycle-007 open) and does NOT route through the trajectory.

4. **`stop_reason` carry-field threads positionally through the L3 worker**, the GMRES-specific addition over the krylov-step theme. The witness lives in the carry from the moment `check_stop_into_carry` writes it; the L3 worker reads it from the carry on each iteration's branch test; the outer wrapper `gmres_inner_loop_L3` extracts it via `fromJust K_final.stop_reason` after the worker returns. No `StopReason`-positional return-tuple slot at the worker level — the witness rides in the carry.

The body's primitive sequence (`apply_BA`, `orthogonalize`, `ls_update_column`, `check_stop_into_carry`, carry-update) is textually unchanged between the L4 body and the L3 body; the rotation is identity-in-form on the body per the `krylov-step-typed-wrapper-dissolution` §"Audit of cycle-002 identity-in-form claim" verdict.

### What does NOT change in the rotation

The five primitive groups in the body — `apply_BA` (constructed-operator linop chain), `orthogonalize` (variant-dispatched, internal MGS obstruction), `ls_update_column` (small-dense sequential obstruction per gmres.md §L3), `check_stop_into_carry` (pure scalar comparison + record update; L3-native), and the carry-update `K5 = K4 { j = K4.j + 1 }` (pure record update) — are textually identical between the L4 body and the L3 body. The variant-axis profile is unchanged.

GMRES carries four variant axes (per `gmres.md:3` and `gmres.md:118-122`); all four are absorbed at body-primitive level and pass through the L4>L3 rotation unchanged:

- **`pc_side ∈ {LEFT, RIGHT, NONE}`** — absorbed inside `apply_BA` (per `gmres.md:119` "inspected only inside `initial_residual`, `apply_BA`, `apply_correction`"). The wrapper rotation does not branch on `pc_side`; the body-primitive `apply_BA op K.j ...` call is identical on both sides.
- **`gs_orthog ∈ {MGS, CGS, CGS2}`** — absorbed inside `orthogonalize` (per `gmres.md:120` "inspected only inside `orthogonalize`"). The wrapper rotation does not branch on `gs_orthog`; the body-primitive `orthogonalize op ...` call is identical on both sides.
- **`flexible ∈ {true, false}`** — absorbed at the `K.Z[K.j] = z` capture site and inside `apply_correction` (per `gmres.md:122`). The wrapper rotation preserves the `if op.flexible then K { Z = K.Z `with` (K.j, z) } else K` carry-update step identically on both sides.
- **`max_dim`** (restart frequency / per-cycle basis dimension) — appears only in `check_stop`'s break test (per `gmres.md:121` "appears only in the inner-break test"). The migration folds the `j + 1 == max_dim` disjunct into the `stop_reason` carry-field via `check_stop_into_carry`; both L4 and L3 forms read it via the same `check_stop_into_carry op conv K3 s.it` call. Outer-loop restart frequency itself lives one level up at `restart_cycle`, not in the inner loop, and is correctly scoped out of this theme.

The variant-absorption table at `gmres.md:118-124` is the basis for these pass-through claims.

### What this lowering does NOT cover

- **The upstream gmres.md §L4 v0.6→v0.7 self-rotation** that re-renders `inner_loop` as the `iterate_while` invocation. That is a separate `lifter` dispatch on `gmres.md`; this theme is its L4>L3 post-condition.
- **L3>L2 lowering on the body**, which is identity-in-form per the same cycle-002 assertion that backs `krylov-step-typed-wrapper-dissolution` (the gmres.md §L3 form is already in primitive-composition shape; the L3>L2 hop is the trivial completion).
- **The `ls_update_column` sequential obstruction** at L3 (per gmres.md §L3 obstruction record). This obstruction is at the *body-primitive* level, not the wrapper level; it survives the wrapper dissolution unchanged and is documented at the gmres.md §L3 source, not duplicated here.
- **The orthog-internal MGS obstruction** (per gmres.md §L3 routing to the `orthog` slice). Same disposition as `krylov-step-typed-wrapper-dissolution` §"What this lowering does NOT cover" point 3.

## Applicability conditions

The rewrite is valid when all five of the following hold (four inherited from `krylov-step-typed-wrapper-dissolution` plus one GMRES-specific):

1. **The L4 `Solve` monad's effect domain is exactly `SimState`** (inherited). The only `modify` in the body is the `it` counter increment; no `Krylov` field is monad-touched; no `OpParams` field is monad-touched (it is `readonly`).

2. **`OpParams` and `Convergence` are closure-captured at the per-step call site** (inherited). The `inner_loop op conv K0 = iterate_while K0 (\K -> ...) (\K -> do { ... })` shape closes over `op` and `conv` lexically; neither is threaded through the carry.

3. **The body's primitive sequence is L3-native or carries its own L3 classification** (inherited). `apply_BA` is a global-operator chain (L3-native); `orthogonalize` is variant-dispatched with internal-MGS obstruction (gmres.md §L3); `ls_update_column` is a small-dense sequential obstruction (gmres.md §L3); `check_stop_into_carry` is pure scalar comparison + record update (L3-native).

4. **The downstream consumer observes only `final_state`-equivalent quantities of the `iterate_while` invocation** (per Law 1 / §3.8; the new Condition 5 from cycle-007 lowering-verifier verdict-(c) on OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`). The GMRES outer `restart_cycle` reads `(K_final, K_final.stop_reason)` — both are carry fields at termination, both are `final_state`-equivalent. Per-iteration printing is a logging side-effect outside the trajectory channel (OQ `iterate-while-log-effect-vs-trajectory-channel`, cycle-007 open). The trajectory therefore prunes to `[]` and the L3 form is the single-readout shape.

5. **`check_stop_into_carry` is a pure function on (OpParams, Convergence, Krylov, int)** (GMRES-specific). Its output is the input `Krylov` with the `stop_reason` field updated; no side effects, no monadic discharge. This is required for the witness-hoist to survive the §3.8 pruning rewrite: if `check_stop_into_carry` were monad-touching, the predicate's `isNothing K.stop_reason` read would force the body's monadic action to execute even when the trajectory is pruned. The pure-function discipline keeps the witness-write inside the body's value-threading and pruning-friendly.

If a future variant of GMRES violates any of these (e.g., a method whose `check_stop` needs to call a monadic logging effect, or whose carry needs to thread a non-Krylov-shaped value), the theme needs refinement; the speculative-operator slot would be enlarged.

## Justification kind

**`structural`** with secondary **`reduction-chain`** and **`empirical-match`** components.

- **Structural** (dominant): the L4 wrapper machinery (Solve monad, `iterate_while` combinator, extras-trajectory record, predicate-on-carry-only discipline) dissolves into an L3 value-threading form; the body's primitive sequence is preserved by construction (every L4 primitive call becomes an L3 primitive call at the same position in the dataflow chain).
- **Reduction-chain** (secondary): the `modify (\s -> s { it = s.it + 1 })` to `s' = s { it = s.it + 1 }` step is a mechanical `StateT` desugaring identical to `krylov-step-typed-wrapper-dissolution.md` §"Justification kind" reduction. The `iterate_while` to `gmres_inner_loop_L3_worker` step is the standard tail-recursive desugaring of the `iterate_while` small-step rule (per `iterate-while.md` §Semantics).
- **Empirical-match** (tertiary): the body's identity-in-form on its primitive sequence is the same combinator-miner cycle-002 assertion that backs `krylov-step-typed-wrapper-dissolution` (cited at `cg.md:351-362` and `arnoldi_step.md:185-188`). GMRES's body shares the same primitive vocabulary modulo the GMRES-specific `ls_update_column` (which is L3-native at the wrapper level even though it carries its own body-level sequential obstruction).

**Abstraction-direction note**: L4 is the higher-abstraction layer (typed records, monadic effect, structural predicate-on-carry-only discipline, demand-prunable trajectory) and L3 is the lower-abstraction layer (positional values threaded explicitly, branch-on-stop-reason in tail recursion, trajectory dissolved per consumer). The rotation direction is L4 → L3.

## Speculative L4 operators

One speculative L4 helper, `check_stop_into_carry`, is proposed as the witness-hoist primitive that the migration needs. Detailed motivation, intended signature, and promotion criterion are in the report's §Speculative L4 operators proposed.

In the L4 [dep-map](../L4/index.md), this would be annotated as:

`| check_stop_into_carry *(rough-in; no anchor yet; proposed-by: abstractor:2026-05-27T180000Z-abstractor-gmres-inner-loop-iterate-while-migration)* | OpParams -> Convergence -> Krylov -> int -> Krylov (with stop_reason field updated) | rough-in |`

Per cycle-006 friction-ledger `rough-in-rows-must-be-plain-text-when-anchor-missing`, the dep-map row is plain text (no markdown link syntax).

## Verified-against

L0 evidence (the inner-loop pattern this theme abstracts):

- `reference/palace/palace/linalg/iterative.cpp:614-650` — GMRES `Mult` inner Arnoldi loop. The `int j = 0; for (;; j++, it++) { ... if (converged || j + 1 == max_dim || it + 1 == max_it) { it++; break; } }` shape is the L0 form whose three-way break corresponds at L4 to the witness-into-carry `Maybe StopReason` (three constructors: `Conv` from `converged = (beta < eps)` at line 644; `MaxDim` from `j + 1 == max_dim` at line 645; `MaxIt` from `it + 1 == max_it` at line 645).
- `reference/palace/palace/linalg/iterative.cpp:642-644` — `beta = std::abs(s[j + 1]); CheckDot(beta, ...); converged = (beta < eps);`. The L0 per-step residual-proxy computation; surfaces at L4 as the `K.beta` carry-field write (already in the v0.1+ form) and the `bt_of K5` extras computation.
- `reference/palace/palace/linalg/iterative.cpp:627-640` — the per-step body sequence (`ApplyBA`, `OrthogonalizeIteration`, `Norml2`, `ApplyPlaneRotation` ×j, `GeneratePlaneRotation`, `ApplyPlaneRotation` ×2). Maps to the L4/L3 body's `apply_BA → orthogonalize → ls_update_column` chain; identity-in-form across L4>L3.

L4 source (the LHS of this rewrite):

- `book/src/spec/slices/gmres.md:459-470` (v0.1 `inner_loop` shape) and `:1067-1078` (v0.6 `inner_loop` + `check_stop`) — the inline tail-recursive `Solve`-monad form that the upstream lifter migration would re-render to the LHS shape above. **Caveat**: this theme's LHS is speculative; if the upstream migration picks a different shape, the LHS needs revision.
- `book/src/L4/iterate-while.md` §Signature, §Semantics, §"Predicate-on-extras anti-pattern", §Algebraic laws Law 1 — the firm L4 row this theme's LHS invokes. The predicate-on-carry-only discipline drives the witness-into-carry hoist; Law 1 drives the L3 form's trajectory pruning.
- `book/src/L4/iterate-while.md:232` — explicit evidence pointer to `iterative.cpp:615` and the OQ-routing note: *"migration to `iterate_while` is filed as a cycle-007 follow-up OQ."*
- `book/src/spec/slices/cg.md:215-219` — precedent rendering pattern (CG v0.4 `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)`). The GMRES migration applies the same pattern with the witness-augmented carry.

L4>L3 precedent (the theme this dispatch parallels):

- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"L3 form (RHS)", §"Audit of cycle-002 identity-in-form claim", §"What the L3 form for `iterate_while` looks like" — the parallel cycle-006 firm theme. This dispatch inherits the wrapper-dissolution rotation and the body-identity-in-form claim; the GMRES additions are (a) the `stop_reason` carry-field threading and (b) the trajectory-pruning resolution. (Section anchors only — the parallel cycle-008 lifter dispatch is editing this file; numeric line ranges would go stale.)

Concept references:

- `book/src/concepts/derived-view-hoisting.md` §"Worked example: CG residual norm" — the §3.8 collapse rule. GMRES's `K.beta` is the analogue of CG's `res = sqrt|beta|`; both are derived views of carry state, hoisted to extras under the rotation, demand-pruned when only `final_state` is consumed.
- `book/src/concepts/sequential-obstruction.md` — referenced for completeness. The `ls_update_column` body-level obstruction survives the wrapper rotation unchanged.

Open-question disposition (cycle-007 OQs this dispatch addresses):

- **`gmres-inner-loop-iterate-while-migration`** — opened cycle-007 by harvester; this dispatch is the abstractor's response. **Status update proposal**: change to `answered-by-rough-in-theme`. The rough-in shape is sketched here; the upstream gmres.md migration is the firmer follow-up (a `lifter` dispatch on `gmres.md §L4`); the theme firms when the migration lands and aligns with this LHS shape.
- **`iterate-while-l3-rendering-trajectory-accumulation-gap`** — opened cycle-006 by abstractor; cycle-007 lowering-verifier verdict-(c) recorded. This dispatch's Applicability Condition 5 cites that verdict's Condition 5 directly; the L3 form's trajectory dissolution is the §3.8-pruned form per Law 1 of `iterate-while.md`. **Status update proposal**: this theme is a second consumer of the lowering-verifier verdict; status remains `open` pending the cycle-008+ lifter patch to `krylov-step-typed-wrapper-dissolution.md` that adds the Condition 5 text in-place. This theme replicates the condition text inline (Applicability Condition 5 above).
- **`iterate-while-log-effect-vs-trajectory-channel`** — opened cycle-007 by lowering-verifier. This theme touches the question (the per-iteration printing in `iterative.cpp:617-621` is a logging side-effect, not a trajectory read) but does NOT resolve it; status remains `open`.

## Status

`rough-in` — the theme's LHS is **speculative on the upstream gmres.md §L4 v0.6→v0.7 self-rotation**: if that rotation lands with the witness-into-carry hoist applied via `check_stop_into_carry` (option (a) in the rough-in caveats), this theme firms against it. If the rotation picks alternative-combinator option (b) `iterate_while_with_stop_witness` or re-run-at-outer-level option (c), the LHS needs revision. The RHS (L3 form) is structurally derived from the LHS and inherits the `krylov-step-typed-wrapper-dissolution` rotation shape; it does not depend on the upstream choice beyond the LHS alignment.

**Lowering-verifier follow-up** (cycle-009+ candidate, after the upstream gmres.md migration lands and this theme firms): confirm that the L3 form produced by applying this theme to the migrated `gmres.md §L4 v0.7 inner_loop` is consistent with `gmres.md §L3`'s inner-step shape (which currently has the v0.6 inline form's L3 lowering implicit in the §L3 obstruction record). If the verifier finds a mismatch (e.g., the v0.7 `check_stop_into_carry` does not lift cleanly to the §L3 shape), the theme is refined.

**Non-blocking on**: the cycle-007 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` lifter patch to `krylov-step-typed-wrapper-dissolution.md` (PRIORITY for cycle-008). When that patch lands and adds Condition 5 to the parallel krylov-step theme, this theme's Applicability Condition 5 wording can be cross-referenced to it rather than restated. Either way the L3 trajectory pruning is the §3.8-pruned single-readout form per the cycle-007 verdict.
```

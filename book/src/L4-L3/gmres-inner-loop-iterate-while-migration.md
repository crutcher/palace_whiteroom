# gmres-inner-loop-iterate-while-migration

The L4>L3 lowering theme for the GMRES inner Arnoldi loop, under the re-rendering of `gmres.md` §L4's `inner_loop` as a direct invocation of the firm L4 [`iterate-while`](../L4/iterate-while.md) combinator. The theme is **firm**: the upstream `gmres.md` §L4 v0.6→v0.7 self-rotation that produces the migrated form was authored cycle-020 wave-1 (lifter dispatch `reports/2026-05-29T034441Z-lifter-gmres-l4-self-rotation/CYCLE.md`; appended to the slice's §L4 self-rotation progression as the v0.7 section). The rotation took the abstractor's option (a) — the witness-into-carry hoist via the (still-rough-in) `check_stop_into_carry` helper — so the LHS sketched at this theme's authoring is the migrated form. The theme captures (a) the L4 form the migration produces, (b) the L3 form it lowers to via wrapper dissolution, and (c) the design tensions resolved (witness-carrying `StopReason` hoisted into the carry to satisfy `iterate-while`'s predicate-on-carry-only discipline; trajectory pruning under §3.8 for the `final_state`-only GMRES consumer).

## Slug

`gmres-inner-loop-iterate-while-migration`

## Context

The cycle-007 harvester promoted [`iterate-while`](../L4/iterate-while.md) and [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) to firm L4 rows (closing cycle-006 OQ `iterate-while-l4-anchor-missing`). The harvester's wave-2 output flagged the GMRES inner-loop migration as a natural follow-up (OQ `gmres-inner-loop-iterate-while-migration`, cycle-007). The CG precedent for rendering a solve loop as a direct `iterate_while` invocation (the v0.4 form `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)`) is firm-homed in [`L4/krylov-step`](../L4/krylov-step.md) §Semantics (Form A; the `krylov-step` body folded by `iterate_while`); the CG v0.5 first-iteration-unrolling material (which uses `iterate_while_with_prev`) is firm-homed there as Form B (cycle-099 absorption). The GMRES inner-loop `Solve`-monad rendering (v0.2 through the migrated v0.7 form) was firm-homed at L0 in `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C (`GmresSolver<OperType>::Mult` `iterative.cpp:543-705`; outer restart + inner Arnoldi loop `iterative.cpp:563-683`); the v0.6→v0.7 witness-into-carry migration is the recognition that the GMRES form is an `iterate_while` invocation with the witness hoist applied to the v0.6 `StopReason` structure. Both the CG and GMRES forms are tail-recursive value-threading folds.

This theme parallels [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) in shape: the L4 wrapper machinery dissolves into L3 value-threading; the body's primitive sequence (apply_BA, orthogonalize, ls_update_column, modify-it, carry-update) survives textually unchanged. The GMRES-specific additions over the krylov-step theme are (a) the carry's `stop_reason :: Maybe StopReason` field threading through `check_stop_into_carry` (the speculative L4 helper), (b) the extras-record shape `{ residual_norm: Scalar, breakdown_token: BreakdownTag }`, and (c) the §3.8 trajectory pruning resolved under the GMRES consumer pattern (per-iteration printing is a logging side-effect outside the trajectory; the summary print reads only `final_state.K.beta`).

The upstream gmres.md self-rotation (v0.6→v0.7) is the cycle-020 wave-1 lifter dispatch that re-rendered `inner_loop` as the `iterate_while` invocation; it is recorded at the slice's §L4 v0.7 section. This theme covers the L4>L3 lowering *of the migrated form* — it is the L4>L3 dissolution applied to the now-firm v0.7 LHS.

## L4 form (LHS)

The migrated GMRES inner loop, as authored in `gmres.md` §L4 v0.7 (this is the LHS of the rewrite; the slice's v0.7 self-rotation section carries the same form):

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

GMRES carries four variant axes (per the slice's §"Variant axes the slice exposes" at `gmres.md:172-176`, the §L1 absorption-levels list at `gmres.md:248-252`, and the v0.6 constructed-operator surface table at `gmres.md:645-654`); all four are absorbed at body-primitive level and pass through the L4>L3 rotation unchanged:

- **`pc_side ∈ {LEFT, RIGHT, NONE}`** — absorbed inside `apply_BA` (per `gmres.md:648` — the v0.6 surface table row `apply_BA | pc_side, (Mk if flexible)`; and `gmres.md:249` "`precond_side` ... absorbed ... via the constructed operator `B`"). The wrapper rotation does not branch on `pc_side`; the body-primitive `apply_BA op K.j ...` call is identical on both sides.
- **`gs_orthog ∈ {MGS, CGS, CGS2}`** — absorbed inside `orthogonalize` (per `gmres.md:649` — the v0.6 surface table row `orthogonalize | gs_orthog | MGS/CGS/CGS2 dispatch`; and `gmres.md:250`). The wrapper rotation does not branch on `gs_orthog`; the body-primitive `orthogonalize op ...` call is identical on both sides.
- **`flexible ∈ {true, false}`** — read at the `K.Z[K.j] = z` capture site (the one acceptable in-loop variant read, per `gmres.md:597` and the prose at `gmres.md:537`) and absorbed inside `apply_correction` (per `gmres.md:650`). The wrapper rotation preserves the `if op.flexible then K { Z = K.Z `with` (K.j, z) } else K` carry-update step identically on both sides. **Note**: in *plain* GMRES (`GmresSolver`, `reference/palace/palace/linalg/iterative.hpp:155`) `flexible = false`, so this carry-update takes its `else K` no-op branch; the `Z` workspace is an FGMRES-only member (`reference/palace/palace/linalg/iterative.hpp:256`), which is why the `flexible = true` collapse is the FGMRES sibling theme's concern, not this one.
- **`max_dim`** (restart frequency / per-cycle basis dimension) — appears only in `check_stop`'s break test (per `gmres.md:652` — the v0.6 surface table row `check_stop | max_it, max_dim | stop-witness producer`; and `gmres.md:591` the `K.j + 1 == op.max_dim = Just StoppedMaxDim` guard). The migration folds the `j + 1 == max_dim` disjunct into the `stop_reason` carry-field via `check_stop_into_carry`; both L4 and L3 forms read it via the same `check_stop_into_carry op conv K3 s.it` call. Outer-loop restart frequency itself lives one level up at `restart_cycle` (`gmres.md:613-631`), not in the inner loop, and is correctly scoped out of this theme.

The slice's §"Variant axes" sections (`gmres.md:172-176`, `:248-252`) and the v0.6 constructed-operator surface table (`gmres.md:645-654`) are the basis for these pass-through claims.

### What this lowering does NOT cover

- **The upstream gmres.md §L4 v0.6→v0.7 self-rotation** that re-renders `inner_loop` as the `iterate_while` invocation. That was authored as the cycle-020 wave-1 lifter dispatch (recorded at the slice's §L4 v0.7 section); this theme is its L4>L3 post-condition.
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

- GMRES v0.6 `inner_loop` / `check_stop` / `StopReason` sum type + the migrated v0.7 form — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C (`GmresSolver<OperType>::Mult` `iterative.cpp:543-705`; outer restart + inner Arnoldi loop `iterative.cpp:563-683`). The LHS is no longer speculative — it is the migrated form.
- `book/src/L4/iterate-while.md` §Signature, §Semantics, §"Predicate-on-extras anti-pattern", §Algebraic laws Law 1 — the firm L4 row this theme's LHS invokes. The predicate-on-carry-only discipline drives the witness-into-carry hoist; Law 1 drives the L3 form's trajectory pruning.
- `book/src/L4/iterate-while.md:232` — explicit evidence pointer to `iterative.cpp:615` and the OQ-routing note: *"migration to `iterate_while` is filed as a cycle-007 follow-up OQ."*
- `book/src/L4/krylov-step.md` §Semantics Form A — precedent rendering pattern (CG v0.4 `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)`, firm-homed there). The GMRES migration applies the same pattern with the witness-augmented carry.

L4>L3 precedent (the theme this dispatch parallels):

- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"L3 form (RHS)", §"Audit of cycle-002 identity-in-form claim", §"What the L3 form for `iterate_while` looks like" — the parallel cycle-006 firm theme. This dispatch inherits the wrapper-dissolution rotation and the body-identity-in-form claim; the GMRES additions are (a) the `stop_reason` carry-field threading and (b) the trajectory-pruning resolution. (Section anchors only — the parallel cycle-008 lifter dispatch is editing this file; numeric line ranges would go stale.)

Concept references:

- `book/src/concepts/derived-view-hoisting.md` §"Worked example: CG residual norm" — the §3.8 collapse rule. GMRES's `K.beta` is the analogue of CG's `res = sqrt|beta|`; both are derived views of carry state, hoisted to extras under the rotation, demand-pruned when only `final_state` is consumed.
- `book/src/concepts/sequential-obstruction.md` — referenced for completeness. The `ls_update_column` body-level obstruction survives the wrapper rotation unchanged.

Open-question disposition (cycle-007 OQs this dispatch addresses):

- **`gmres-inner-loop-iterate-while-migration`** — opened cycle-007 by harvester; sketched as a rough-in theme cycle-008 wave-2 (abstractor); the upstream gmres.md §L4 v0.6→v0.7 migration authored cycle-020 wave-1 (lifter), and this theme firmed against it. **Status update proposal**: close as `resolved` — the migration landed (slice §L4 v0.7) and aligns with this LHS shape (option (a), `check_stop_into_carry`).
- **`iterate-while-l3-rendering-trajectory-accumulation-gap`** — opened cycle-006 by abstractor; cycle-007 lowering-verifier verdict-(c) recorded. This dispatch's Applicability Condition 5 cites that verdict's Condition 5 directly; the L3 form's trajectory dissolution is the §3.8-pruned form per Law 1 of `iterate-while.md`. **Status update proposal**: this theme is a second consumer of the lowering-verifier verdict; status remains `open` pending the cycle-008+ lifter patch to `krylov-step-typed-wrapper-dissolution.md` that adds the Condition 5 text in-place. This theme replicates the condition text inline (Applicability Condition 5 above).
- **`iterate-while-log-effect-vs-trajectory-channel`** — opened cycle-007 by lowering-verifier. This theme touches the question (the per-iteration printing in `iterative.cpp:617-621` is a logging side-effect, not a trajectory read) but does NOT resolve it; status remains `open`.

## Status

`firm` — the theme's LHS is the migrated form authored by the cycle-020 wave-1 lifter dispatch (the upstream `gmres.md` §L4 v0.6→v0.7 self-rotation, recorded at the slice's §L4 v0.7 section). The rotation took option (a) — the witness-into-carry hoist via `check_stop_into_carry` — which is the LHS sketched here, so no LHS revision was needed. The RHS (L3 form) is structurally derived from the LHS and inherits the firm [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) rotation shape (firm cycle-008 wave-1). The one rough-in element in the LHS vocabulary — the `check_stop_into_carry` L4 helper — does not block this theme's firmness: it is a thin pure record-update wrapper around the firm v0.6 `check_stop`, and the theme is firm *as an L4>L3 dissolution theme* exactly as `krylov-step-typed-wrapper-dissolution` was firm while `iterate_while` was still rough-in (cycle-006→007). Promotion of `check_stop_into_carry` to a firm L4 row is a separate harvester decision (§Speculative L4 operators).

**Lowering-verifier follow-up** (cycle-021+ candidate): confirm that the L3 form produced by applying this theme to the migrated `gmres.md §L4 v0.7 inner_loop` is consistent with the firm [`L3/krylov-step`](../L3/krylov-step.md) inner-step shape (the GMRES `ls_update_column` sequential obstruction is recorded there as a body-primitive non-lift, not at the wrapper level). If the verifier finds a mismatch (e.g., the v0.7 `check_stop_into_carry` does not lift cleanly to the L3 shape), the theme is refined.

**Sibling, still rough-in**: [`fgmres-inner-loop-iterate-while-migration`](./fgmres-inner-loop-iterate-while-migration.md) applies this same rotation with two variant-axis collapses (`pc_side = RIGHT`, `flexible = true`) plus a per-iteration `Z[j]` workspace; it firms in a cycle-021 follow-up lifter dispatch against this now-firm sibling rotation (the upstream v0.7 it shares is the same one authored here).

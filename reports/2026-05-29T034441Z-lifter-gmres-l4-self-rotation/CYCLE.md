---
agent: lifter
invoked_at: 2026-05-29T035241Z
scope: L4>L3 theme re-anchor — gmres-inner-loop-iterate-while-migration (firm against the now-authored gmres §L4 v0.6→v0.7 self-rotation)
status: integrated
integrated_at: 2026-05-29T06:05:00Z
integration_commit: 14cc0bd
integration_notes: "cycle-020 finalize (staging row #6). gmres-inner-loop-iterate-while-migration L4>L3 theme PROMOTED rough-in→firm (9 surgical [old]/[new] firming edits) WITH its LHS surface landing the same apply (Edit 10 appended the gmres.md §L4 v0.6→v0.7 inner-loop iterate_while self-rotation via option (a) check_stop_into_carry to spec/slices/gmres.md). cg.md:215-219 stale CG-precedent re-anchored to firm L4/krylov-step Form A (+ cg.md:86-108). The L4/index.md:44 theme row + :53 iterate-while Lowers-to cell dep-map firm-sync was DEFERRED to finalize (layer-intro-author territory) — APPLIED by integrator-finalize this cycle as a consistency-repair (rough-in→firm). fgmres sibling row STAYS rough-in (held cycle-021; live-link, file exists). OQ gmres-inner-loop-iterate-while-migration Closed-index :192 → resolved cycle-020 (meta-phase updates). L4>L3 firm 1→2, rough-in 2→1. retroactive-budget 0; clean build."
inputs:
  - book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
  - book/src/spec/slices/gmres.md
  - book/src/L4/iterate-while.md
  - book/src/L4/iterate-while-with-prev.md
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
  - book/src/L4/index.md
  - reference/palace/palace/linalg/iterative.cpp (GMRES inner loop, :615-650)
  - reference/palace/palace/linalg/iterative.hpp (GmresSolver/FgmresSolver, four-scalar result surface)
---

# CYCLE: Re-anchor gmres-inner-loop-iterate-while-migration

## Summary

This dispatch performs the upstream `gmres.md` §L4 **v0.6→v0.7 self-rotation** that the rough-in theme `gmres-inner-loop-iterate-while-migration` was waiting on, then **firms the theme against it**. The self-rotation re-renders the v0.6 inline tail-recursive `Solve`-monad `inner_loop` (`book/src/spec/slices/gmres.md:594-606`, with `check_stop` at `:587-592`) into a **direct `iterate_while` invocation** (the firm cycle-007 L4 combinator at `book/src/L4/iterate-while.md`), applying the witness-into-carry hoist to the v0.6 `StopReason` structure via the speculative `check_stop_into_carry` helper. The migrated form is captured as the theme's `## L4 form (LHS)`; the v0.7 self-rotation is also appended to the slice's §L4 self-rotation progression (which the reduced slice's stub-header explicitly retains as "unique material"). The theme's RHS (the L4>L3 wrapper dissolution to the L3 value-threading form) is unchanged in structure — it already inherits the firm `krylov-step-typed-wrapper-dissolution` rotation. **The body's primitive sequence (`apply_BA`, `orthogonalize`, `ls_update_column`, `modify`-it, carry-update) survives textually unchanged across both the v0.6→v0.7 self-rotation and the L4>L3 dissolution.** Status flips `rough-in` → `firm`. Two classes of edits are bundled: (1) the LHS firming + status flip, and (2) a **bounded prose-correction sweep** of the theme's stale slice line-refs — the gmres slice was **reduced** since the theme was authored (the v0.1 form was lifted to firm entries; v0.6 moved from `:1067-1078` to `:594-606`), so every `gmres.md:NNN` citation in the theme had drifted. The fgmres sibling (`fgmres-inner-loop-iterate-while-migration.md`) is **HELD** for cycle-021 (it carries two variant-axis simplifications on top of this same rotation).

## The self-rotation (gmres §L4 v0.6 → v0.7)

### What v0.6 is, and what blocks the migration

The v0.6 `inner_loop` (`gmres.md:594-606`) is an **inline tail-recursive `Solve`-monad function**:

```text
inner_loop :: OpParams -> Convergence -> Krylov -> Solve (Krylov, StopReason)
inner_loop op conv K = do
  let (w, z)      = apply_BA op K.j K.V[K.j]
      K1          = if op.flexible then K{ Z = K.Z `with` (K.j, z) } else K
      (v_next, h) = orthogonalize op (K1.V[0..K1.j]) w
      K2          = K1{ V = K1.V `with` (K1.j+1, v_next) }
      K3          = ls_update_column K2 h
  modify (\s -> s{ it = s.it + 1 })
  s <- get
  case check_stop op conv K3 s.it of
    Just reason -> pure (K3, reason)
    Nothing     -> inner_loop op conv K3{ j = K3.j + 1 }
```

The recursion is hand-rolled: the `case check_stop ... of { Just reason -> pure ...; Nothing -> inner_loop ... }` is exactly the tail-recursive fold that `iterate_while` names. Two things stop v0.6 from *being* an `iterate_while` invocation:

1. **The continuation decision reads outside the carry.** v0.6 computes `check_stop op conv K3 s.it`, which inspects `op` (`max_it`, `max_dim`), `conv`, and the monad's `s.it` — none of which is the carry `K`. The firm `iterate-while` §Signature point 1 (`book/src/L4/iterate-while.md:50,57,102`) requires the predicate to be `α -> Bool`, reading the carry only. So v0.6's `check_stop` cannot be the `iterate_while` predicate as-is.

2. **The stop-witness is produced as a side return, not threaded in the carry.** v0.6 returns `(K3, reason)` — the `StopReason` rides out alongside the carry. `iterate_while`'s result is `{ final_state: α, trajectory: [{ ...e }] }`; there is no second positional witness slot. The witness must live *in* the carry to survive the combinator's value-threading.

### The v0.7 rotation: witness-into-carry hoist

The migration resolves both via the **witness-into-carry hoist** (the same `derived-view-hoisting` move v0.6 itself applied to lift `StopReason` from `classify`'s recomputation site into `check_stop` — see slice §L4 v0.6 prose at `gmres.md:539-545`; v0.7 applies it one notch further, from a side-return into the carry field):

- **Augment the `Krylov` carry with `stop_reason :: Maybe StopReason`.** This is the v0.6 `check_stop` return value, now materialized as a carry field rather than a side-channel return.
- **`check_stop_into_carry` runs the v0.6 `check_stop` logic and writes the result into `K.stop_reason`** (the speculative L4 helper; signature `OpParams -> Convergence -> Krylov -> int -> Krylov`, output is the input `K` with `stop_reason` updated). It is the v0.6 `check_stop` (`gmres.md:587-592`) wrapped to return the carry instead of a bare `Maybe StopReason`.
- **The predicate becomes `\K -> isNothing K.stop_reason`** — reads the carry only, honouring `iterate-while` §Signature point 1.
- **The body writes `stop_reason` (via `check_stop_into_carry`) before the combinator re-tests the predicate**, and advances `K.j` only while `stop_reason` is still `Nothing` (the v0.6 `Nothing -> inner_loop op conv K3{ j = K3.j + 1 }` arm).
- **The witness is extracted from the carry at termination** via `fromJust K_final.stop_reason` — recovering the `(Krylov, StopReason)` return shape v0.6 had, now as a post-loop projection rather than a recursion return.

The v0.7 `inner_loop` (this is the migrated form = the theme's LHS):

```text
type Krylov = {
  V :: Vec[],
  Z :: Vec[] | null,
  H :: Dense,
  s :: DenseVec,
  cs :: DenseVec,
  sn :: DenseVec,
  j :: int,
  beta :: real,
  stop_reason :: Maybe StopReason   -- hoisted from v0.6's check_stop return (gmres.md:587-592)
}

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
  let K_final = result.final_state
  pure (K_final, fromJust K_final.stop_reason)                     -- witness is in the carry
```

This is iteration-for-iteration equivalent to v0.6: each `iterate_while` step runs exactly the v0.6 body, `check_stop_into_carry` computes exactly v0.6's `check_stop`, and the loop stops on the same condition (`isNothing K.stop_reason` is false exactly when v0.6's `check_stop` returned `Just`). The `j`-advance happens on the same `Nothing` condition. The `modify (\s -> s { it = s.it + 1 })` `SimState` effect and the `apply_BA → orthogonalize → ls_update_column` body are textually unchanged.

### Disambiguation: this v0.7 is the *migration* v0.7, not the *classifier-compaction* v0.7

The reduced slice's v0.6 §"Open questions" (`gmres.md:633,669`) anticipates a different v0.7 — a *classifier signature compaction* that splits `classify` into `classify_entry` / `classify_post` to drop the dead `total_it` parameter. That is a distinct self-rotation on a different axis (signature compaction of the outer `restart_cycle`'s classifier), orthogonal to the inner-loop `iterate_while` migration this dispatch performs. The migration v0.7 touches only `inner_loop` (and adds the `stop_reason` carry field); it leaves `classify` / `restart_cycle` exactly as v0.6 left them. The two v0.7 rotations compose without conflict (the migration's `check_stop_into_carry` and the compaction's `classify_post` read disjoint surfaces). I am authoring only the migration v0.7 here; the classifier-compaction v0.7 remains a slice open question (see §Open questions).

## Firmed theme

The theme's structure is unchanged: `## Context`, `## L4 form (LHS)`, `## L3 form (RHS)`, `## Applicability conditions`, `## Justification kind`, `## Speculative L4 operators`, `## Verified-against`, `## Status`. What changes:

1. **The opening paragraph + §Context** lose the "depends on an upstream self-rotation that has not yet been authored" framing — the rotation is now authored (above + in the slice §L4 v0.7 section). The theme is the L4>L3 post-condition *of* the now-firm migration.
2. **The LHS block** is unchanged in content (the rough-in already sketched the correct v0.7 shape — the abstractor's option (a) `check_stop_into_carry` route is the one the rotation took), but its provenance note flips from "speculative; if the upstream migration picks a different shape, the LHS needs revision" to "this is the migrated form authored at slice §L4 v0.7".
3. **Stale slice line-refs are corrected** (bounded prose-correction; see §Discipline notes) — the slice was reduced since the theme was authored.
4. **Status** flips `rough-in` → `firm`.
5. The `check_stop_into_carry` **speculative L4 operator stays rough-in** — the migration uses it but does not promote it to a firm L4 row (that is a harvester decision; the dep-map row stays plain-text per `rough-in-rows-must-be-plain-text-when-anchor-missing`). The theme is firm *as an L4>L3 dissolution theme* even with one rough-in helper in its LHS vocabulary, exactly as `krylov-step-typed-wrapper-dissolution` was firm while `iterate_while` was still rough-in (cycle-006→007).

## Proposed changes

### Edit 1 — opening paragraph: drop the "not yet authored" framing

```edit:book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
[old]: The L4>L3 lowering theme for the GMRES inner Arnoldi loop, under the (speculative) re-rendering of `gmres.md` §L4's `inner_loop` as a direct invocation of the firm L4 [`iterate-while`](../L4/iterate-while.md) combinator. The theme is **rough-in** — it depends on an upstream self-rotation on `gmres.md` §L4 (v0.6→v0.7) that has not yet been authored; the theme captures (a) what L4 form the migration would produce, (b) what L3 form it lowers to via wrapper dissolution, and (c) which design tensions surface (witness-carrying `StopReason` vs. predicate-on-carry-only; trajectory pruning under §3.8). When the upstream rotation lands, this theme is firmed against it (or revised if the rotation picks a different shape).
[new]: The L4>L3 lowering theme for the GMRES inner Arnoldi loop, under the re-rendering of `gmres.md` §L4's `inner_loop` as a direct invocation of the firm L4 [`iterate-while`](../L4/iterate-while.md) combinator. The theme is **firm**: the upstream `gmres.md` §L4 v0.6→v0.7 self-rotation that produces the migrated form was authored cycle-020 wave-1 (lifter dispatch `reports/2026-05-29T034441Z-lifter-gmres-l4-self-rotation/CYCLE.md`; appended to the slice's §L4 self-rotation progression as the v0.7 section). The rotation took the abstractor's option (a) — the witness-into-carry hoist via the (still-rough-in) `check_stop_into_carry` helper — so the LHS sketched at this theme's authoring is the migrated form. The theme captures (a) the L4 form the migration produces, (b) the L3 form it lowers to via wrapper dissolution, and (c) the design tensions resolved (witness-carrying `StopReason` hoisted into the carry to satisfy `iterate-while`'s predicate-on-carry-only discipline; trajectory pruning under §3.8 for the `final_state`-only GMRES consumer).
```

### Edit 2 — §Context: re-anchor the slice line-refs (v0.6 moved `:1067-1078` → `:594-606`; v0.1 lifted away)

```edit:book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
[old]: The cycle-007 harvester promoted [`iterate-while`](../L4/iterate-while.md) and [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) to firm L4 rows (closing cycle-006 OQ `iterate-while-l4-anchor-missing`). The harvester's wave-2 output flagged the GMRES inner-loop migration as a natural follow-up (OQ `gmres-inner-loop-iterate-while-migration`, cycle-007). The CG slice already renders its solve loop as `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)` at `cg.md:215-219`; the GMRES slice renders its inner loop as an inline tail-recursive `Solve`-monad function at `gmres.md:459-470` (v0.1) through `:1067-1078` (v0.6). Both forms are tail-recursive value-threading folds; the migration is the recognition that the GMRES form is an `iterate_while` invocation with the witness-into-carry hoist applied to the v0.6 `StopReason` structure.
[new]: The cycle-007 harvester promoted [`iterate-while`](../L4/iterate-while.md) and [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) to firm L4 rows (closing cycle-006 OQ `iterate-while-l4-anchor-missing`). The harvester's wave-2 output flagged the GMRES inner-loop migration as a natural follow-up (OQ `gmres-inner-loop-iterate-while-migration`, cycle-007). The CG precedent for rendering a solve loop as a direct `iterate_while` invocation (the v0.4 form `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)`) was lifted into the firm L4 entry [`L4/krylov-step`](../L4/krylov-step.md) §Semantics (Form A; the `krylov-step` body folded by `iterate_while`) when the cg slice was reduced — the cg slice (`book/src/spec/slices/cg.md`, now 166 lines) retains only its unique L4 v0.5 first-iteration-unrolling material (which uses `iterate_while_with_prev`); the GMRES slice (likewise reduced — its v0.1 `inner_loop` was lifted into firm entries per the slice stub-header) renders its inner loop as an inline tail-recursive `Solve`-monad function in the retained §L4 self-rotation progression: the earliest retained form is v0.2 at `gmres.md:122-133`, and the v0.6 form (the migration's direct input) is at `gmres.md:594-606` with `check_stop` at `gmres.md:587-592` and the `StopReason` sum type at `gmres.md:551-554`. Both the CG and GMRES forms are tail-recursive value-threading folds; the migration is the recognition that the GMRES form is an `iterate_while` invocation with the witness-into-carry hoist applied to the v0.6 `StopReason` structure. The migrated v0.7 form is appended to the slice's §L4 progression as the v0.7 section (cycle-020 wave-1 lifter).
```

### Edit 3 — §"What this lowering does NOT cover": the self-rotation is now covered upstream, not "a separate dispatch"

```edit:book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
[old]: The theme does NOT cover the upstream gmres.md self-rotation itself (that is a separate lifter dispatch on `gmres.md §L4`); it covers the L4>L3 lowering *of the migrated form*. The theme is therefore a post-condition on the upstream migration: when the migration lands at gmres.md v0.7, this theme is the L4>L3 dissolution applied to it.
[new]: The upstream gmres.md self-rotation (v0.6→v0.7) is the cycle-020 wave-1 lifter dispatch that re-rendered `inner_loop` as the `iterate_while` invocation; it is recorded at the slice's §L4 v0.7 section. This theme covers the L4>L3 lowering *of the migrated form* — it is the L4>L3 dissolution applied to the now-firm v0.7 LHS.
```

### Edit 4 — LHS block: flip the provenance note (the body of the LHS code is correct as-is)

The fenced `text` LHS block (theme lines 21-58) is unchanged in content — the rough-in's sketch is the form the rotation produced. Only the surrounding prose framing changes.

```edit:book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
[old]: The migrated GMRES inner loop, as it would appear in `gmres.md` §L4 v0.7 (speculative; this is the LHS of the rewrite):
[new]: The migrated GMRES inner loop, as authored in `gmres.md` §L4 v0.7 (this is the LHS of the rewrite; the slice's v0.7 self-rotation section carries the same form):
```

### Edit 5 — re-anchor the variant-axis pass-through citations (the `gmres.md:118-124` table was reduced away)

The theme's §"What does NOT change in the rotation" cites `gmres.md:3` and `gmres.md:118-122` / `:118-124` / `:119` / `:120` / `:121` / `:122` for the four-axis variant profile. Those line ranges, post-reduction, no longer hold the variant-axis material (line 3 is the stub-header; 118-124 is mid-v0.2 prose). The variant profile now lives at the slice's §"Variant axes the slice exposes" (`gmres.md:172-176`), §L1 §"Variant axes" (`gmres.md:248-252`), and the v0.6 constructed-operator surface table (`gmres.md:645-654`).

```edit:book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
[old]: GMRES carries four variant axes (per `gmres.md:3` and `gmres.md:118-122`); all four are absorbed at body-primitive level and pass through the L4>L3 rotation unchanged:

- **`pc_side ∈ {LEFT, RIGHT, NONE}`** — absorbed inside `apply_BA` (per `gmres.md:119` "inspected only inside `initial_residual`, `apply_BA`, `apply_correction`"). The wrapper rotation does not branch on `pc_side`; the body-primitive `apply_BA op K.j ...` call is identical on both sides.
- **`gs_orthog ∈ {MGS, CGS, CGS2}`** — absorbed inside `orthogonalize` (per `gmres.md:120` "inspected only inside `orthogonalize`"). The wrapper rotation does not branch on `gs_orthog`; the body-primitive `orthogonalize op ...` call is identical on both sides.
- **`flexible ∈ {true, false}`** — absorbed at the `K.Z[K.j] = z` capture site and inside `apply_correction` (per `gmres.md:122`). The wrapper rotation preserves the `if op.flexible then K { Z = K.Z `with` (K.j, z) } else K` carry-update step identically on both sides.
- **`max_dim`** (restart frequency / per-cycle basis dimension) — appears only in `check_stop`'s break test (per `gmres.md:121` "appears only in the inner-break test"). The migration folds the `j + 1 == max_dim` disjunct into the `stop_reason` carry-field via `check_stop_into_carry`; both L4 and L3 forms read it via the same `check_stop_into_carry op conv K3 s.it` call. Outer-loop restart frequency itself lives one level up at `restart_cycle`, not in the inner loop, and is correctly scoped out of this theme.

The variant-absorption table at `gmres.md:118-124` is the basis for these pass-through claims.
[new]: GMRES carries four variant axes (per the slice's §"Variant axes the slice exposes" at `gmres.md:172-176`, the §L1 absorption-levels list at `gmres.md:248-252`, and the v0.6 constructed-operator surface table at `gmres.md:645-654`); all four are absorbed at body-primitive level and pass through the L4>L3 rotation unchanged:

- **`pc_side ∈ {LEFT, RIGHT, NONE}`** — absorbed inside `apply_BA` (per `gmres.md:648` — the v0.6 surface table row `apply_BA | pc_side, (Mk if flexible)`; and `gmres.md:249` "`precond_side` ... absorbed ... via the constructed operator `B`"). The wrapper rotation does not branch on `pc_side`; the body-primitive `apply_BA op K.j ...` call is identical on both sides.
- **`gs_orthog ∈ {MGS, CGS, CGS2}`** — absorbed inside `orthogonalize` (per `gmres.md:649` — the v0.6 surface table row `orthogonalize | gs_orthog | MGS/CGS/CGS2 dispatch`; and `gmres.md:250`). The wrapper rotation does not branch on `gs_orthog`; the body-primitive `orthogonalize op ...` call is identical on both sides.
- **`flexible ∈ {true, false}`** — read at the `K.Z[K.j] = z` capture site (the one acceptable in-loop variant read, per `gmres.md:597` and the prose at `gmres.md:537`) and absorbed inside `apply_correction` (per `gmres.md:650`). The wrapper rotation preserves the `if op.flexible then K { Z = K.Z `with` (K.j, z) } else K` carry-update step identically on both sides. **Note**: in *plain* GMRES (`GmresSolver`, `reference/palace/palace/linalg/iterative.hpp:155`) `flexible = false`, so this carry-update takes its `else K` no-op branch; the `Z` workspace is an FGMRES-only member (`reference/palace/palace/linalg/iterative.hpp:256`), which is why the `flexible = true` collapse is the FGMRES sibling theme's concern, not this one.
- **`max_dim`** (restart frequency / per-cycle basis dimension) — appears only in `check_stop`'s break test (per `gmres.md:652` — the v0.6 surface table row `check_stop | max_it, max_dim | stop-witness producer`; and `gmres.md:591` the `K.j + 1 == op.max_dim = Just StoppedMaxDim` guard). The migration folds the `j + 1 == max_dim` disjunct into the `stop_reason` carry-field via `check_stop_into_carry`; both L4 and L3 forms read it via the same `check_stop_into_carry op conv K3 s.it` call. Outer-loop restart frequency itself lives one level up at `restart_cycle` (`gmres.md:613-631`), not in the inner loop, and is correctly scoped out of this theme.

The slice's §"Variant axes" sections (`gmres.md:172-176`, `:248-252`) and the v0.6 constructed-operator surface table (`gmres.md:645-654`) are the basis for these pass-through claims.
```

### Edit 6 — §"What this lowering does NOT cover" list: the self-rotation bullet now points at the authored v0.7

```edit:book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
[old]: - **The upstream gmres.md §L4 v0.6→v0.7 self-rotation** that re-renders `inner_loop` as the `iterate_while` invocation. That is a separate `lifter` dispatch on `gmres.md`; this theme is its L4>L3 post-condition.
[new]: - **The upstream gmres.md §L4 v0.6→v0.7 self-rotation** that re-renders `inner_loop` as the `iterate_while` invocation. That was authored as the cycle-020 wave-1 lifter dispatch (recorded at the slice's §L4 v0.7 section); this theme is its L4>L3 post-condition.
```

### Edit 7 — §Verified-against L4-source bullet: drop the speculative caveat, point at the firm v0.7

```edit:book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
[old]: - `book/src/spec/slices/gmres.md:459-470` (v0.1 `inner_loop` shape) and `:1067-1078` (v0.6 `inner_loop` + `check_stop`) — the inline tail-recursive `Solve`-monad form that the upstream lifter migration would re-render to the LHS shape above. **Caveat**: this theme's LHS is speculative; if the upstream migration picks a different shape, the LHS needs revision.
[new]: - `book/src/spec/slices/gmres.md:594-606` (v0.6 `inner_loop`), `:587-592` (v0.6 `check_stop`), `:551-554` (the `StopReason` sum type), and the appended §L4 v0.7 self-rotation section — the v0.6 inline tail-recursive `Solve`-monad form that the cycle-020 wave-1 lifter migration re-rendered to the LHS shape above, plus the authored v0.7 form itself. The earliest retained form (v0.2) is at `gmres.md:122-133`; the v0.1 form was lifted into firm entries before this theme firmed (slice stub-header). The LHS is no longer speculative — it is the migrated form.
```

### Edit 8 — §"Open-question disposition" for the migration OQ: it is now answered-firm, not answered-by-rough-in

```edit:book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
[old]: - **`gmres-inner-loop-iterate-while-migration`** — opened cycle-007 by harvester; this dispatch is the abstractor's response. **Status update proposal**: change to `answered-by-rough-in-theme`. The rough-in shape is sketched here; the upstream gmres.md migration is the firmer follow-up (a `lifter` dispatch on `gmres.md §L4`); the theme firms when the migration lands and aligns with this LHS shape.
[new]: - **`gmres-inner-loop-iterate-while-migration`** — opened cycle-007 by harvester; sketched as a rough-in theme cycle-008 wave-2 (abstractor); the upstream gmres.md §L4 v0.6→v0.7 migration authored cycle-020 wave-1 (lifter), and this theme firmed against it. **Status update proposal**: close as `resolved` — the migration landed (slice §L4 v0.7) and aligns with this LHS shape (option (a), `check_stop_into_carry`).
```

### Edit 9 — §Status: flip rough-in → firm

```edit:book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
[old]: ## Status

`rough-in` — the theme's LHS is **speculative on the upstream gmres.md §L4 v0.6→v0.7 self-rotation**: if that rotation lands with the witness-into-carry hoist applied via `check_stop_into_carry` (option (a) in the rough-in caveats), this theme firms against it. If the rotation picks alternative-combinator option (b) `iterate_while_with_stop_witness` or re-run-at-outer-level option (c), the LHS needs revision. The RHS (L3 form) is structurally derived from the LHS and inherits the `krylov-step-typed-wrapper-dissolution` rotation shape; it does not depend on the upstream choice beyond the LHS alignment.

**Lowering-verifier follow-up** (cycle-009+ candidate, after the upstream gmres.md migration lands and this theme firms): confirm that the L3 form produced by applying this theme to the migrated `gmres.md §L4 v0.7 inner_loop` is consistent with `gmres.md §L3`'s inner-step shape (which currently has the v0.6 inline form's L3 lowering implicit in the §L3 obstruction record). If the verifier finds a mismatch (e.g., the v0.7 `check_stop_into_carry` does not lift cleanly to the §L3 shape), the theme is refined.

**Non-blocking on**: the cycle-007 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` lifter patch to `krylov-step-typed-wrapper-dissolution.md` (PRIORITY for cycle-008). When that patch lands and adds Condition 5 to the parallel krylov-step theme, this theme's Applicability Condition 5 wording can be cross-referenced to it rather than restated. Either way the L3 trajectory pruning is the §3.8-pruned single-readout form per the cycle-007 verdict.
[new]: ## Status

`firm` — the theme's LHS is the migrated form authored by the cycle-020 wave-1 lifter dispatch (the upstream `gmres.md` §L4 v0.6→v0.7 self-rotation, recorded at the slice's §L4 v0.7 section). The rotation took option (a) — the witness-into-carry hoist via `check_stop_into_carry` — which is the LHS sketched here, so no LHS revision was needed. The RHS (L3 form) is structurally derived from the LHS and inherits the firm [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) rotation shape (firm cycle-008 wave-1). The one rough-in element in the LHS vocabulary — the `check_stop_into_carry` L4 helper — does not block this theme's firmness: it is a thin pure record-update wrapper around the firm v0.6 `check_stop`, and the theme is firm *as an L4>L3 dissolution theme* exactly as `krylov-step-typed-wrapper-dissolution` was firm while `iterate_while` was still rough-in (cycle-006→007). Promotion of `check_stop_into_carry` to a firm L4 row is a separate harvester decision (§Speculative L4 operators).

**Lowering-verifier follow-up** (cycle-021+ candidate): confirm that the L3 form produced by applying this theme to the migrated `gmres.md §L4 v0.7 inner_loop` is consistent with the firm [`L3/krylov-step`](../L3/krylov-step.md) inner-step shape (the GMRES `ls_update_column` sequential obstruction is recorded there as a body-primitive non-lift, not at the wrapper level). If the verifier finds a mismatch (e.g., the v0.7 `check_stop_into_carry` does not lift cleanly to the L3 shape), the theme is refined.

**Sibling, still rough-in**: [`fgmres-inner-loop-iterate-while-migration`](./fgmres-inner-loop-iterate-while-migration.md) applies this same rotation with two variant-axis collapses (`pc_side = RIGHT`, `flexible = true`) plus a per-iteration `Z[j]` workspace; it firms in a cycle-021 follow-up lifter dispatch against this now-firm sibling rotation (the upstream v0.7 it shares is the same one authored here).
```

### Edit 10 — slice §L4: append the v0.7 self-rotation section

The reduced slice's stub-header (`gmres.md:16`) explicitly retains "the L4 v0.2 → v0.3 → v0.4 → v0.5 → v0.6 self-rotation progression" as unique material. The v0.7 migration is the natural next entry in that progression. Append after the v0.6 §"Open questions" block (currently the slice's final content, ending at `gmres.md:671`).

```edit:book/src/spec/slices/gmres.md
[old]: - The witness approach generalises: any classifier whose dispatch tag is determined upstream of the classification site can be migrated to carry the tag as a constructor field. This is a candidate methodology concept ("witness-typed dispatch") that may warrant extraction if it recurs in other slices (Chebyshev's convergence-by-eigenvalue-band, GMG's coarse-grid-direct-solve trigger). Deferred until a second instance lands.
[new]: - The witness approach generalises: any classifier whose dispatch tag is determined upstream of the classification site can be migrated to carry the tag as a constructor field. This is a candidate methodology concept ("witness-typed dispatch") that may warrant extraction if it recurs in other slices (Chebyshev's convergence-by-eigenvalue-band, GMG's coarse-grid-direct-solve trigger). Deferred until a second instance lands.

## L4 v0.7 — inner-loop `iterate_while` migration (witness-into-carry hoist)

The v0.6 form's `inner_loop` (above, this slice §L4 v0.6 §"`inner_loop` produces the witness") is an inline tail-recursive `Solve`-monad function whose recursion is exactly the value-threading fold that the firm L4 combinator [`iterate-while`](../../L4/iterate-while.md) (cycle-007) names. This v0.7 tightening (L4→L4 self-rotation, no layer advancement) re-renders `inner_loop` as a *direct* `iterate_while` invocation, so the GMRES inner loop reuses the firm iteration vocabulary rather than re-deriving the tail recursion in-line. It is the GMRES analogue of CG's v0.4 `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)` rendering, lifted to the firm L4 entry [`L4/krylov-step`](../../L4/krylov-step.md) §Semantics (Form A — the `krylov-step` body folded by `iterate_while`) when the cg slice was reduced.

Two obstacles in v0.6 block a direct `iterate_while`:

1. **`iterate_while`'s predicate reads the carry only** (`α -> Bool`, per `iterate-while.md` §Signature point 1). v0.6's continuation decision `check_stop op conv K3 s.it` reads `op`, `conv`, and the monad's `s.it` — none of which is the carry `K`.
2. **`iterate_while` has no side-witness return slot** — its result is `{ final_state, trajectory }`. v0.6 returns `(K3, reason)`, threading the `StopReason` alongside the carry.

### The witness-into-carry hoist

Both obstacles are resolved by hoisting the v0.6 `check_stop` result into a carry field. This is the same [derived-view-hoisting](../../concepts/derived-view-hoisting.md) move v0.6 itself applied (lifting `StopReason` from `classify`'s recomputation into `check_stop`); v0.7 carries it one notch further — from a side-return into the carry.

- The `Krylov` carry gains a `stop_reason :: Maybe StopReason` field.
- `check_stop_into_carry` runs v0.6's `check_stop` and writes the result into `K.stop_reason` (a pure record update; no `Solve` effect).
- The predicate is `\K -> isNothing K.stop_reason` — carry-only.
- The witness is extracted from the carry after the loop via `fromJust K_final.stop_reason`, recovering v0.6's `(Krylov, StopReason)` return shape.

```haskell
-- v0.6's check_stop (this slice §L4 v0.6) wrapped to return the carry with
-- stop_reason written, rather than a bare Maybe StopReason.
check_stop_into_carry :: OpParams -> Convergence -> Krylov -> int -> Krylov
check_stop_into_carry op conv K total_it =
  K { stop_reason = check_stop op conv K total_it }

-- The Krylov carry gains a stop_reason field (the v0.1 fields plus the v0.7 witness).
-- (V, Z, H, s, cs, sn, j, beta unchanged from the v0.1+ Krylov.)

inner_loop :: OpParams -> Convergence -> Krylov -> Solve (Krylov, StopReason)
inner_loop op conv K0 = do
  result <- iterate_while
              K0
              (\K -> isNothing K.stop_reason)                  -- predicate reads carry only
              (\K -> do
                let (w, z)      = apply_BA op K.j K.V[K.j]
                    K1          = if op.flexible then K{ Z = K.Z `with` (K.j, z) } else K
                    (v_next, h) = orthogonalize op (K1.V[0..K1.j]) w
                    K2          = K1{ V = K1.V `with` (K1.j+1, v_next) }
                    K3          = ls_update_column K2 h
                modify (\s -> s{ it = s.it + 1 })
                s <- get
                let K4          = check_stop_into_carry op conv K3 s.it
                    K5          = if isNothing K4.stop_reason then K4{ j = K4.j + 1 } else K4
                pure { state = K5, residual_norm = K5.beta, breakdown_token = bt_of K5 })
  let K_final = result.final_state
  pure (K_final, fromJust K_final.stop_reason)
```

### Why v0.6 was tight-but-non-idiomatic

v0.6's `inner_loop` is correct and tight, but it re-implements the tail-recursive value-threading fold by hand (`case check_stop ... of { Just -> pure; Nothing -> inner_loop ... }`). Every iterative algorithm in the spec reduces at L4 to one or more `iterate_while` folds (`iterate-while.md` §Context); a hand-rolled recursion is a *missed reuse* of the firm combinator, and it leaves the predicate-on-carry-only discipline (`iterate-while.md` §Signature point 1) implicit rather than structural. v0.7 makes the fold explicit and the discipline structural: the predicate is literally `α -> Bool` over the carry, and the `SimState`-effect (`modify it`) is the body's sole monadic action, orthogonal to the value-threaded carry (`iterate-while.md` §Semantics placement disciplines).

The migration is **iteration-for-iteration equivalent** to v0.6: each step runs the identical body (`apply_BA → orthogonalize → ls_update_column → modify it`), `check_stop_into_carry` computes exactly v0.6's `check_stop`, and the loop stops on the same condition. The `j`-advance fires on the same `Nothing` test. No numerics change.

### Trajectory pruning (the consumer pattern)

The body returns extras `{ residual_norm: K5.beta, breakdown_token: bt_of K5 }` (matching `iterate-while.md` §Signature's GMRES instantiation, line 51). But `restart_cycle` (this slice §L4 v0.6, `gmres.md:613-631`) consumes only `(K, reason)` from `inner_loop` — both are `final_state`-equivalent (the final carry and its `stop_reason` witness). Per `iterate-while.md` Law 1 (§3.8 demand-pruning), when only `final_state` is observed the body's extras computation is pruned at the call site; the per-iteration residual printing (`reference/palace/palace/linalg/iterative.cpp:617-621`) is a logging side-effect outside the trajectory channel, not a trajectory read. So the trajectory prunes to `[]` and the L3 image is the single-readout form (the L4>L3 dissolution is the firm theme [`gmres-inner-loop-iterate-while-migration`](../../L4-L3/gmres-inner-loop-iterate-while-migration.md)).

### What stays out of v0.7

- **`classify` / `restart_cycle` are unchanged.** The witness extracted from the carry (`fromJust K_final.stop_reason`) feeds the existing v0.6 `classify op conv (PostKrylov K reason) ...` call exactly as before. v0.7 changes only how `inner_loop` produces `reason`, not how `restart_cycle` consumes it.
- **The classifier-signature compaction** anticipated by the v0.6 §"Open questions" (splitting `classify` to drop the dead `total_it`) is a *different* v0.7-candidate on a different axis (signature compaction of the outer classifier); it is orthogonal to this inner-loop migration and is not pursued here. The two compose without conflict.

### Citations

- The v0.6 `inner_loop` + `check_stop` this rotation re-renders: this slice §L4 v0.6 §"`inner_loop` produces the witness" (`gmres.md:584-606`) and the `StopReason` sum type (`gmres.md:551-554`).
- The firm `iterate_while` combinator and its predicate-on-carry-only / §3.8-pruning disciplines: [`iterate-while`](../../L4/iterate-while.md) §Signature (point 1), §Semantics, §Algebraic laws Law 1.
- The CG precedent rendering (`iterate_while` at a solve loop): lifted to the firm L4 entry [`L4/krylov-step`](../../L4/krylov-step.md) §Semantics (Form A) when the cg slice was reduced; the cg slice (`cg.md`, now 166 lines) retains only the unique L4 v0.5 first-iteration-unrolling material (`iterate_while_with_prev` form, `cg.md:86-108`).
- The L0 inner loop this names: `reference/palace/palace/linalg/iterative.cpp:615` (the `for (;; j++, it++)` GMRES Arnoldi loop), break test at `:645-648` (`if (converged || j + 1 == max_dim || it + 1 == max_it) { it++; break; }`).
- `check_stop_into_carry` is a (rough-in) speculative L4 helper, proposed in the L4>L3 theme [`gmres-inner-loop-iterate-while-migration`](../../L4-L3/gmres-inner-loop-iterate-while-migration.md) §"Speculative L4 operators".

### Open questions (L4 v0.7-specific)

- `check_stop_into_carry` is a rough-in L4 helper. Promotion to a firm L4 row is deferred to a harvester decision: it is a thin pure wrapper (`K { stop_reason = check_stop ... }`) and adds vocabulary only if it recurs (FGMRES reuses it — see the fgmres sibling theme; a second consumer is the promotion trigger per the unimplemented-Palace-component promotion bar).
- The classifier-signature compaction (the *other* candidate v0.7) remains open as a slice tightening on the `restart_cycle` classifier axis; it composes with this migration v0.7 without conflict.
```

## Discipline notes

- **What changed and why.** The rough-in theme `gmres-inner-loop-iterate-while-migration` was authored cycle-008 wave-2 (abstractor) explicitly blocked on an unwritten upstream `gmres.md` §L4 v0.6→v0.7 self-rotation. This dispatch *authored* that rotation (the witness-into-carry hoist, captured both as the slice's §L4 v0.7 section — Edit 10 — and as the theme's now-firm LHS) and firmed the theme against it (Edits 1-9, status flip `rough-in`→`firm`). This is the lifter's pure-rewriting pass: the theme's structure (Context / LHS / RHS / Applicability / Justification / Speculative-ops / Verified-against / Status) is untouched; only the vocabulary firms (the LHS is now an authored form, not a speculation) and the citations re-anchor.

- **High→low direction preserved.** The theme's LHS stays L4 (the v0.7 `iterate_while` invocation), its RHS stays L3 (the value-threaded dissolution), and the prose narrates the rewrite forward (L4 into L3). The self-rotation is an L4→L4 tightening (the slice §L4 v0.7 section frames it as "no layer advancement", consistent with the v0.2-v0.6 sections). No inversion. The "how the L3 form lifts upward" direction does not appear in any formal chapter content — it is not relevant here (this is an L4→L4 + L4>L3 dispatch).

- **Bounded prose-correction recorded (the stale-citation sweep).** Per the lifter-scope content-correction boundary (friction-ledger `lifter-scope-content-correction-boundary`, cycle-012), I corrected the theme's drifted slice line-refs in place. The drift is **evidenced and bounded**: the gmres slice was *reduced* between the theme's authoring (cycle-008) and now — its v0.1 `inner_loop` was lifted into firm entries (per the slice stub-header at `gmres.md:3,13`), and the v0.6 form moved from the theme-cited `:1067-1078` to the current `:594-606` (verified by direct read this dispatch). Corrected citations and their verified new homes:
  - v0.6 `inner_loop`: `gmres.md:1067-1078` → `gmres.md:594-606` (verified: `inner_loop :: OpParams -> Convergence -> Krylov -> Solve (Krylov, StopReason)` at line 594).
  - v0.6 `check_stop`: now at `gmres.md:587-592` (verified: `check_stop :: ... -> Maybe StopReason` at 587).
  - `StopReason` sum type: `gmres.md:551-554` (verified: `data StopReason` at 551).
  - v0.1 `inner_loop` (`:459-470`): **removed** — no longer in the slice (lifted away); the earliest retained form is v0.2 at `gmres.md:122-133` (verified).
  - Variant-axis profile (`:3`, `:118-124`, `:119`, `:120`, `:121`, `:122`): → §"Variant axes" at `gmres.md:172-176` + `:248-252`, and the v0.6 surface table at `gmres.md:645-654` (verified each surface-table row: `apply_BA`/`pc_side` at 648, `orthogonalize`/`gs_orthog` at 649, `apply_correction`/`flexible` at 650, `check_stop`/`max_it,max_dim` at 652).
  This sweep is **bounded** (fixing drifted citations only; no decomposition / signature / sub-pattern change) and does not re-architect the theme — consistent with "structural rewrite, not authorship".

- **Plain-GMRES `flexible = false` clarification (Edit 5).** Added a bounded, L0-evidenced note that in `GmresSolver` (`iterative.hpp:155`) the `if op.flexible then ... else K` carry-update takes its `else K` no-op branch (`Z` is an FGMRES-only member at `iterative.hpp:256`). This sharpens the variant-pass-through claim without changing it — the carry-update *step* is preserved identically across L4>L3 either way; the note just records which branch fires in plain GMRES vs. the FGMRES sibling. Directly supported by the `iterative.hpp:155/222/256` reads this dispatch performed.

- **`check_stop_into_carry` left rough-in (no promotion).** The migration uses the speculative helper but does not promote it to a firm L4 row — that is a harvester decision (a thin pure wrapper that adds vocabulary only on recurrence; FGMRES is the second-consumer trigger). The theme is firm *as a dissolution theme* with one rough-in helper in its LHS vocabulary, the exact precedent of `krylov-step-typed-wrapper-dissolution` being firm while `iterate_while` was rough-in (cycle-006→007). The dep-map row stays plain-text per `rough-in-rows-must-be-plain-text-when-anchor-missing`.

- **No book/ writes.** All edits are emitted as proposed-changes blocks for `integrator-per-report` to apply (DISPATCH-phase write-guard; re-anchors are proposals, not edits — friction-ledger `specialized-agent-direct-write-to-book-during-dispatch`).

## Supporting evidence

L0 (Palace GMRES inner loop; verified this dispatch via codemap `read_range`):
- `reference/palace/palace/linalg/iterative.cpp:615` — `for (;; j++, it++)` (GMRES inner Arnoldi loop).
- `reference/palace/palace/linalg/iterative.cpp:627-640` — per-step body (`ApplyBA → OrthogonalizeIteration → Norml2 → ApplyPlaneRotation ×j → GeneratePlaneRotation → ApplyPlaneRotation ×2`).
- `reference/palace/palace/linalg/iterative.cpp:642-644` — `beta = std::abs(s[j + 1]); CheckDot(...); converged = (beta < eps);`.
- `reference/palace/palace/linalg/iterative.cpp:645-648` — `if (converged || j + 1 == max_dim || it + 1 == max_it) { it++; break; }` (the three-way break → the three `StopReason` constructors).
- `reference/palace/palace/linalg/iterative.cpp:617-621` — `if (print_opts.iterations) { Mpi::Print(...) }` (per-iteration residual printing; logging side-effect, NOT a trajectory read — supports the §3.8 prune-to-`[]`).
- `reference/palace/palace/linalg/iterative.hpp:52-55` — the four mutable result scalars (`converged`, `initial_res`, `final_res`, `final_it`); structural evidence for the `final_state`-only consumer pattern.
- `reference/palace/palace/linalg/iterative.hpp:155` — `class GmresSolver` (plain GMRES; `flexible = false`).
- `reference/palace/palace/linalg/iterative.hpp:222` — `class FgmresSolver : public GmresSolver` (the sibling's home).
- `reference/palace/palace/linalg/iterative.hpp:256` — `mutable std::vector<VecType> Z` (FGMRES-only workspace member).

L4/L4>L3 (verified this dispatch via Read):
- `book/src/spec/slices/gmres.md:551-554,587-592,594-606,613-631` — the v0.6 `StopReason` / `check_stop` / `inner_loop` / `restart_cycle` (the migration's direct input).
- `book/src/spec/slices/gmres.md:122-133` — earliest retained `inner_loop` (v0.2).
- `book/src/spec/slices/gmres.md:172-176,248-252,645-654` — the variant-axis profile (post-reduction homes).
- `book/src/L4/iterate-while.md` §Signature (point 1, line 50/57/102), §Semantics, §Algebraic laws Law 1 (`:123-133`), §Evidence line 232 (the GMRES-migration follow-up OQ note), §Signature line 51 (GMRES extras `{ residual_norm, breakdown_token }`) — the firm combinator the rotation re-anchors onto.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"L3 form (RHS)", §"What the L3 form for iterate_while looks like" — the firm parallel rotation the RHS inherits.
- `book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md:1-40` — the sibling (stays rough-in; cycle-021 follow-up).
- `book/src/L4/index.md:44,53` — the dep-map rows for the theme + `iterate-while` (already note the rough-in landed cycle-008 wave-2; the `firm` flip will need a dep-map touch, see Open questions).

## Open questions / caveats

1. **Structural-home choice (most-conservative, stated for the record).** The dispatch brief flagged the v0.7-form home as potentially ambiguous. I chose the **most-conservative** placement: the v0.7 L4 form is captured (i) as the theme's LHS and (ii) as an appended slice §L4 v0.7 self-rotation section (the slice stub-header explicitly retains the L4 self-rotation progression as unique material, so v0.7 is the natural next entry). I did **NOT** create a standalone `book/src/L4/gmres.md` operator entry — GMRES at L4 is represented by the variant-collapsed `krylov-step` family + `L1/ksp_solve`, and a dedicated `L4/gmres.md` operator would be a *new operator authorship* decision (harvester scope), not a lifter re-anchor. **OQ for the planner**: should GMRES get a standalone `L4/gmres.md` operator entry (the full `solve_loop`/`restart_cycle`/`inner_loop` structure, of which v0.7 `inner_loop` is one piece)? Currently the `restart_cycle`/`solve_loop` outer drivers are referenced from concept pages but not anchored as L4 rows (per `L4/index.md:46` "Queued at L4"). If yes, the slice §L4 v0.7 section is the seed. Flagging, not deciding.

2. **fgmres sibling — cycle-021 follow-up (HELD this dispatch).** `book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md` stays `rough-in`. It applies this *same* v0.7 rotation with two variant-axis collapses (`pc_side = RIGHT` pinned at the `FgmresSolver` constructor, `iterative.hpp:263-266`; `flexible = true` so the `Z` carry-update is unconditional) plus a per-iteration `Z[j]` workspace (`iterative.hpp:256`, `iterative.cpp:794-829`). Its upstream rotation is the *same one authored here* (the migration v0.7 is shared; FGMRES just instantiates the variant axes), so the cycle-021 lifter firms it against this now-firm sibling without needing a new self-rotation. Bounded follow-up.

3. **Dep-map status touch (`L4/index.md`).** The dep-map rows at `L4/index.md:44` (the theme row) and `:53` (the `iterate-while` "Lowers to" cell) currently annotate the theme as "*(rough-in; landed cycle-008 wave-2)*". On firming, the integrator should update both to "*(firm; cycle-020 wave-1 lifter)*". This is a mechanical dep-map sync; I flag it rather than emit it as a proposed-change because the dep-map row is `layer-intro-author` territory and the exact wording is theirs — but it must not be missed (a `firm` theme with a `rough-in` dep-map annotation is a cross-reference-integrity drift the critic would flag). If the integrator prefers, the two-cell touch is: theme-row + iterate-while-row "Lowers to" annotation `(rough-in; landed cycle-008 wave-2)` → `(firm; cycle-020 wave-1 lifter re-anchor)`.

4. **`gmres-inner-loop-iterate-while-migration` OQ closure.** Edit 8 proposes closing the cycle-007 OQ as `resolved`. The two *other* OQs the theme touches stay open and are explicitly NOT closed by this dispatch: `iterate-while-l3-rendering-trajectory-accumulation-gap` (resolved for the parallel krylov-step theme cycle-007, replicated inline here as Applicability Condition 4) and `iterate-while-log-effect-vs-trajectory-channel` (the per-iteration printing question; touched, not resolved). The integrator (open-questions writer) applies the closure.

5. **Lowering-verifier follow-up (cycle-021+).** With the theme firm, a lowering-verifier dispatch can now audit that the L3 form produced by applying this theme to the v0.7 `inner_loop` is consistent with the firm `L3/krylov-step` inner-step shape and the GMRES `ls_update_column` body-primitive obstruction. Not blocking; flagged as the natural next audit.

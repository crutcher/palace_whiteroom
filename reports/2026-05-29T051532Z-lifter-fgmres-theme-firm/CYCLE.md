---
agent: lifter
invoked_at: 2026-05-29T051532Z
scope: L4>L3 theme re-anchor — fgmres-inner-loop-iterate-while-migration (firm against the now-firm gmres rotation + sibling theme)
status: integrated
integrated_at: 2026-05-29T06:14:03Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-021 finalize (staging row #1). fgmres-inner-loop-iterate-while-migration L4>L3 theme PROMOTED rough-in→firm (11 surgical firming edits over the firm gmres sibling rotation, applying the pc_side=RIGHT/flexible=true variant-axis collapses + the per-iteration Z[j] workspace; the former Edit 7 NON-edit correctly skipped). CLOSES the 5-batch carry-forward fgmres-inner-loop-iterate-while-migration-lifter-candidate (cycle-010→021). Edit 12 ADDED the firm theme row to L4/index.md:44 (was absent from the L4 index entirely; consistency-repair mirroring the cycle-020 gmres dep-map firm-sync). check_stop_into_carry stays rough-in plain-text. L4>L3 firm 2→3, rough-in 1→0. retroactive-budget 0; clean build."
inputs:
  - book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md
  - book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
  - book/src/L4/iterate-while.md
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
  - book/src/L4/index.md
  - book/src/spec/slices/gmres.md
  - reference/palace/palace/linalg/iterative.hpp (FgmresSolver, :222-274)
  - reference/palace/palace/linalg/iterative.cpp (FGMRES inner loop, :794-829; restart_cycle :752-793)
---

# CYCLE: Re-anchor fgmres-inner-loop-iterate-while-migration

## Summary

This dispatch **firms the rough-in `fgmres-inner-loop-iterate-while-migration` (L4>L3) theme against its now-firm sibling** `gmres-inner-loop-iterate-while-migration` (firmed cycle-020 wave-1) and the firm L4 `iterate-while` combinator. The fgmres theme is a **pure variant-axis specialisation** of the gmres rotation: it applies the *same* upstream `gmres.md` §L4 v0.6→v0.7 self-rotation (the witness-into-carry hoist via `check_stop_into_carry`), with two collapses — FGMRES pins `pc_side = RIGHT` at the `FgmresSolver` constructor (`iterative.hpp:263-266`) and `flexible = true`, so the GMRES sibling's `if op.flexible then K { Z = ... } else K` carry-update simplifies to the unconditional `K { Z = K.Z `with` (K.j, z) }` — plus the per-iteration `Z[j]` workspace allocation (the FGMRES adaptive-preconditioner output, `iterative.cpp:806`, `iterative.hpp:256`). The theme was rough-in **for exactly the reason its sibling was** — both depended on the unwritten upstream gmres §L4 v0.6→v0.7 rotation. That rotation landed cycle-020 (slice §L4 v0.7, `gmres.md:673-747`; line 746 already names the FGMRES sibling as the second-consumer trigger), so the blocker is cleared and the fgmres theme firms with no LHS revision (the rough-in already sketched the option-(a) `check_stop_into_carry` shape the rotation took). **This is a pure re-anchoring: the theme's structure (Context / LHS / RHS / Applicability / Justification / Speculative-ops / Verified-against / Status) is untouched; only the "speculative upstream" framing firms up and the drifted slice line-refs re-anchor.** Status flips `rough-in` → `firm`. The `check_stop_into_carry` speculative L4 helper **stays rough-in** (its promotion remains blocked on a non-`GmresSolverBase` consumer per OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`; FGMRES being the sister algorithm does not stress the helper signature in a new dimension). This dispatch **CLOSES the fgmres carry-forward** — the multi-batch `fgmres-inner-loop-iterate-while-migration-lifter-candidate` item (opened cycle-010, deferred since) — by enacting the cycle-011→cycle-021 lifter re-anchor.

## What changes vs. the sibling precedent

The cycle-020 gmres dispatch (`reports/2026-05-29T034441Z-lifter-gmres-l4-self-rotation/CYCLE.md`) did three things: authored the upstream slice §L4 v0.7 self-rotation, firmed the gmres theme, and swept the gmres theme's drifted slice line-refs. This fgmres dispatch is **smaller** because the upstream rotation is already authored (shared) and the fgmres theme is already a sibling-anchored specialisation:

1. **No new self-rotation.** The upstream v0.7 form is the *same one* the gmres dispatch authored; FGMRES instantiates it with the variant collapses. I author no slice content.
2. **Firm the "speculative upstream" framing.** The fgmres theme's opening + §Context + §L4-form provenance + §"What this lowering does NOT cover" + §Verified-against all say the upstream rotation "has not yet been authored" / "is a separate lifter dispatch" / the LHS "is speculative". These flip to firm-against-the-authored-v0.7-and-the-firm-sibling.
3. **Re-anchor the same drifted slice line-refs the gmres dispatch found.** The fgmres theme cites `gmres.md:539-672` (v0.6 form) and `gmres.md:118-124`/`:120`/`:121` (variant-axis profile). The slice was reduced; these drifted exactly as the gmres theme's did. I re-anchor them to the firm homes the gmres sibling now uses (`:594-606`, `:587-592`, `:551-554`, and `:645-654`/`:172-176`/`:248-252`). **Self-verified by direct read this dispatch** (see §Discipline notes).
4. **Status flip + dep-map.** `rough-in` → `firm`; propose the L4 index prose-list entry (the fgmres theme is currently absent from `book/src/L4/index.md` entirely — see §Open questions item 3).

## Proposed changes

### Edit 1 — opening paragraph: drop "(speculative)" + the "rough-in / not-yet-authored" framing

```edit:book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md
[old]: The L4>L3 lowering theme for the **FGMRES** inner Arnoldi loop, under the (speculative) re-rendering of `gmres.md` §L4's `inner_loop` as a direct invocation of the firm L4 [`iterate-while`](../L4/iterate-while.md) combinator. **Sibling theme** to [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md): the two themes share the wrapper-dissolution shape, the body-primitive sequence, and the speculative `check_stop_into_carry` helper; they differ on **variant-axis collapse** (FGMRES pins `pc_side = RIGHT` and `flexible = true`; GMRES leaves both free) and on **per-iteration preconditioner adaptation** (FGMRES allocates a per-iteration `Z[j]` workspace; GMRES uses the single workspace `r` unless `op.flexible`). The theme is **rough-in** for the same reason its sibling is: it depends on an upstream self-rotation on `gmres.md` §L4 (v0.6→v0.7) that has not yet been authored.
[new]: The L4>L3 lowering theme for the **FGMRES** inner Arnoldi loop, under the re-rendering of `gmres.md` §L4's `inner_loop` as a direct invocation of the firm L4 [`iterate-while`](../L4/iterate-while.md) combinator. **Sibling theme** to the now-firm [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md): the two themes share the wrapper-dissolution shape, the body-primitive sequence, and the speculative `check_stop_into_carry` helper; they differ on **variant-axis collapse** (FGMRES pins `pc_side = RIGHT` and `flexible = true`; GMRES leaves both free) and on **per-iteration preconditioner adaptation** (FGMRES allocates a per-iteration `Z[j]` workspace; GMRES uses the single workspace `r` unless `op.flexible`). The theme is **firm**: it depends on the *same* upstream `gmres.md` §L4 v0.6→v0.7 self-rotation its sibling depends on, and that rotation was authored cycle-020 wave-1 (lifter dispatch `reports/2026-05-29T034441Z-lifter-gmres-l4-self-rotation/CYCLE.md`; recorded at the slice's §L4 v0.7 section, `gmres.md:673-747`). The rotation took the abstractor's option (a) — the witness-into-carry hoist via the (still-rough-in) `check_stop_into_carry` helper — which is the LHS this theme sketched, so no LHS revision was needed; the FGMRES specialisation applies the two variant-axis collapses to that firm migrated form.
```

### Edit 2 — §Context para "The cycle-008 abstractor's ...": flip "(speculative)" upstream framing to firm

```edit:book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md
[old]: The cycle-008 abstractor's [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) theme captures the upstream rotation generically: the L4 GMRES `inner_loop` migration produces an `iterate_while`-invocation with the witness-into-carry hoist via `check_stop_into_carry`. **The same rotation applies to FGMRES**, with two variant-axis simplifications:
[new]: The now-firm [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) theme captures the upstream rotation generically: the L4 GMRES `inner_loop` migration (authored as the slice §L4 v0.7 self-rotation, `gmres.md:673-747`) produces an `iterate_while`-invocation with the witness-into-carry hoist via `check_stop_into_carry`. **The same rotation applies to FGMRES**, with two variant-axis simplifications:
```

### Edit 3 — §Context para "The theme does NOT cover ...": the self-rotation is now authored upstream, not "a separate lifter dispatch"

```edit:book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md
[old]: The theme does NOT cover the upstream gmres.md §L4 self-rotation itself — that is a separate lifter dispatch on `gmres.md §L4`; this theme is its L4>L3 post-condition for the FGMRES specialisation.
[new]: The theme does NOT cover the upstream gmres.md §L4 self-rotation itself — that was authored as the cycle-020 wave-1 lifter dispatch (recorded at the slice's §L4 v0.7 section, `gmres.md:673-747`); this theme is its L4>L3 post-condition for the FGMRES specialisation.
```

### Edit 4 — §"L4 form (LHS)" provenance line: drop "speculative", anchor to the authored v0.7 + firm sibling

```edit:book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md
[old]: The migrated FGMRES inner loop, as it would appear under the same speculative `gmres.md` §L4 v0.7 form, parameterised on the FGMRES variant-axis collapse:
[new]: The migrated FGMRES inner loop, as it appears under the now-firm `gmres.md` §L4 v0.7 form (the migrated form authored cycle-020 wave-1, `gmres.md:673-747`), parameterised on the FGMRES variant-axis collapse:
```

### Edit 5 — §"What this lowering does NOT cover": the upstream self-rotation bullet now points at the authored v0.7

```edit:book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md
[old]: - **The upstream gmres.md §L4 v0.6→v0.7 self-rotation** that re-renders `inner_loop` as the `iterate_while` invocation. Same disposition as the sibling theme — a separate `lifter` dispatch on `gmres.md §L4` would author this; both this theme and its sibling are L4>L3 post-conditions.
[new]: - **The upstream gmres.md §L4 v0.6→v0.7 self-rotation** that re-renders `inner_loop` as the `iterate_while` invocation. Same disposition as the sibling theme — it was authored as the cycle-020 wave-1 lifter dispatch (recorded at the slice's §L4 v0.7 section, `gmres.md:673-747`); both this theme and its sibling are its L4>L3 post-conditions.
```

### Edit 6 — §"What does NOT change in the rotation": re-anchor the variant-axis pass-through citations (the `gmres.md:118-124` table was reduced away)

The theme cites `gmres.md:120` and `gmres.md:121` for the two surviving variant axes, and `gmres.md:118-124` for the absorption table. Post-reduction those lines are mid-v0.2 prose (verified by direct read this dispatch — the variant material moved). The two-axis profile now lives at the slice's §"Variant axes" (`gmres.md:172-176`, `:248-252`) and the v0.6 constructed-operator surface table (`gmres.md:645-654`) — the same homes the firm gmres sibling re-anchored to.

```edit:book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md
[old]: - **`gs_orthog ∈ {MGS, CGS, CGS2}`** — absorbed inside `orthogonalize` per `gmres.md:120`. The wrapper rotation does not branch on `gs_orthog`; the body-primitive call is identical on both sides.
- **`max_dim`** (restart frequency / per-cycle basis dimension) — folded into the `stop_reason` carry-field via `check_stop_into_carry` per `gmres.md:121`. Both L4 and L3 forms read it via the same `check_stop_into_carry op conv K3 s'.it` call. Outer-loop restart frequency itself lives one level up at `restart_cycle`, not in the inner loop, and is correctly scoped out of this theme.

The GMRES variant-absorption table at `gmres.md:118-124` reduces under FGMRES to just these two rows; the basis for the pass-through claims is the GMRES table modulo the FGMRES pinning.
[new]: - **`gs_orthog ∈ {MGS, CGS, CGS2}`** — absorbed inside `orthogonalize` per the v0.6 constructed-operator surface table row `orthogonalize | gs_orthog | MGS/CGS/CGS2 dispatch` (`gmres.md:649`; and the §L1 absorption list at `gmres.md:250`). The wrapper rotation does not branch on `gs_orthog`; the body-primitive call is identical on both sides.
- **`max_dim`** (restart frequency / per-cycle basis dimension) — folded into the `stop_reason` carry-field via `check_stop_into_carry` per the v0.6 surface table row `check_stop | max_it, max_dim | stop-witness producer` (`gmres.md:652`; and the `K.j + 1 == op.max_dim = Just StoppedMaxDim` guard at `gmres.md:591`). Both L4 and L3 forms read it via the same `check_stop_into_carry op conv K3 s'.it` call. Outer-loop restart frequency itself lives one level up at `restart_cycle` (`gmres.md:613-631`), not in the inner loop, and is correctly scoped out of this theme.

The GMRES variant profile (the v0.6 constructed-operator surface table at `gmres.md:645-654`, plus the §"Variant axes" sections at `gmres.md:172-176`, `:248-252`) reduces under FGMRES to just these two rows; the basis for the pass-through claims is the GMRES profile modulo the FGMRES pinning of `pc_side = RIGHT` (surface-table row `apply_BA | pc_side, (Mk if flexible)`, `gmres.md:648`) and `flexible = true` (surface-table row `apply_correction | pc_side, flexible`, `gmres.md:650`).
```

### Note (not an edit) — §"Applicability conditions": no change needed

**This is a NON-edit note, not a proposed-changes block** — it carries no `[old]`/`[new]` fence and the integrator must not attempt to apply it. The §"Applicability conditions" inherit verbatim from the firm sibling and are unchanged; the sibling reference at the top of that section already links the firm theme, and firming it does not change the inherited conditions. Recorded here only for completeness. (The numbered proposed-changes sequence therefore has **11 applicable edits**: Edits 1–6 and 8–12.)

### Edit 8 — §Verified-against L4-source bullet: re-anchor `gmres.md:539-672` to the precise firm homes + drop the speculative caveat

The fgmres theme cites `gmres.md:539-672` for "the v0.6 `inner_loop` + `check_stop` form" with a speculative-LHS caveat. The slice was reduced; the precise homes are `inner_loop` at `:594-606`, `check_stop` at `:587-592`, `StopReason` at `:551-554` (verified this dispatch — same homes the firm gmres sibling uses). The LHS is no longer speculative.

```edit:book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md
[old]: - `book/src/spec/slices/gmres.md:539-672` — the v0.6 `inner_loop` + `check_stop` form. The upstream lifter migration would re-render this to the LHS shape above; the FGMRES specialisation applies the variant-axis collapses to the migrated form. **Caveat**: this theme's LHS is speculative; if the upstream migration picks a different shape, the LHS needs revision.
[new]: - `book/src/spec/slices/gmres.md:594-606` (v0.6 `inner_loop`), `:587-592` (v0.6 `check_stop`), `:551-554` (the `StopReason` sum type), and the appended §L4 v0.7 self-rotation section (`gmres.md:673-747`) — the v0.6 inline tail-recursive `Solve`-monad form that the cycle-020 wave-1 lifter migration re-rendered to the migrated v0.7 form, plus the authored v0.7 form itself. The FGMRES specialisation applies the variant-axis collapses to that migrated form. The LHS is no longer speculative — it is the firm migrated form shared with the now-firm gmres sibling.
```

### Edit 9 — §Verified-against L4-source bullet for the sibling theme: it is now firm

```edit:book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md
[old]: - `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` — the sibling theme. This dispatch inherits the wrapper-dissolution rotation, the body-identity-in-form claim, the applicability conditions 1–5, and the speculative-helper invocation. The FGMRES specialisation adds applicability condition 6 and the two variant-axis collapses.
[new]: - `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` (firm, cycle-020 wave-1) — the sibling theme. This dispatch inherits the (now-firm) wrapper-dissolution rotation, the body-identity-in-form claim, the applicability conditions 1–5, and the speculative-helper invocation. The FGMRES specialisation adds applicability condition 6 and the two variant-axis collapses.
```

### Edit 10 — §"Open-question disposition" for the lifter-candidate OQ: this dispatch is the cycle-021 enactment, theme now firm

```edit:book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md
[old]: - **`fgmres-inner-loop-iterate-while-migration-lifter-candidate`** (cycle-010, opened by combinator-miner) — this dispatch is the cycle-011 enactment. **Status update proposal**: change to `answered-by-rough-in-theme`. The theme is authored; the upstream gmres.md migration is the firmer follow-up; the theme firms when the migration lands and aligns with the LHS shape, identical conditions to the sibling.
[new]: - **`fgmres-inner-loop-iterate-while-migration-lifter-candidate`** (cycle-010, opened by combinator-miner) — this cycle-021 lifter dispatch is the enactment that **firms the theme**. The upstream gmres.md §L4 v0.7 migration landed cycle-020 (the shared rotation), aligning with this theme's LHS shape (option (a), `check_stop_into_carry`), so the theme firms against it and the firm gmres sibling. **Status update proposal**: close as `resolved` — the carry-forward is closed (the theme is firm; this CLOSES the multi-batch fgmres lifter-candidate carry-forward).
```

### Edit 11 — §Status: flip rough-in → firm

```edit:book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md
[old]: ## Status

`rough-in` — same status as the sibling theme, for the same upstream-dependency reason: the LHS is speculative on the upstream `gmres.md §L4 v0.6→v0.7` self-rotation; if that rotation lands with the witness-into-carry hoist applied via `check_stop_into_carry` (option (a) in the sibling's rough-in caveats), this theme firms against it. If the rotation picks alternative-combinator option (b) `iterate_while_with_stop_witness` or re-run-at-outer-level option (c), the LHS needs revision. The RHS (L3 form) is structurally derived from the LHS and inherits the wrapper-dissolution shape; it does not depend on the upstream choice beyond the LHS alignment.

**Cycle-010 lower-edge "second reuse" corroboration**: the existence of this theme as a sibling that invokes `check_stop_into_carry` at the same callsite shape is the lower-edge corroborating evidence for the cycle-008 promotion criterion. Per cycle-010 audit, this does **not** unblock firm L4 promotion of the helper (the strong-reuse evidence — a non-`GmresSolverBase` Krylov consumer — is still required, tracked by OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`).

**Lowering-verifier follow-up** (cycle-012+ candidate, after the upstream gmres.md migration lands and both this and the sibling theme firm): confirm that the L3 forms produced by applying both themes to the migrated `gmres.md §L4 v0.7 inner_loop` are pairwise consistent with `gmres.md §L3`'s inner-step shape (which currently has the v0.6 inline form's L3 lowering implicit in the §L3 obstruction record). If the verifier finds a mismatch (e.g., the v0.7 `check_stop_into_carry` does not lift cleanly to the §L3 shape for FGMRES specifically), the theme is refined.

**Non-blocking on**: the upstream gmres.md migration. This theme is authored speculatively against the same v0.7 shape its sibling assumes; landing one without the other is permitted.
[new]: ## Status

`firm` — the theme's LHS is the firm migrated form authored by the cycle-020 wave-1 lifter dispatch (the shared upstream `gmres.md` §L4 v0.6→v0.7 self-rotation, recorded at the slice's §L4 v0.7 section, `gmres.md:673-747`). The rotation took option (a) — the witness-into-carry hoist via `check_stop_into_carry` — which is the LHS sketched here, so no LHS revision was needed; the FGMRES specialisation applies the two variant-axis collapses (`pc_side = RIGHT`, `flexible = true`) and the per-iteration `Z[j]` workspace to that firm form. The RHS (L3 form) is structurally derived from the LHS and inherits the firm [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) rotation shape (firm cycle-008 wave-1) via the now-firm [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) sibling (firm cycle-020 wave-1). The one rough-in element in the LHS vocabulary — the `check_stop_into_carry` L4 helper — does not block this theme's firmness: it is a thin pure record-update wrapper around the firm v0.6 `check_stop`, and the theme is firm *as an L4>L3 dissolution theme* exactly as `krylov-step-typed-wrapper-dissolution` was firm while `iterate_while` was still rough-in (cycle-006→007), and as the gmres sibling is firm while `check_stop_into_carry` stays rough-in.

**`check_stop_into_carry` stays rough-in (no promotion).** The existence of this theme as a sibling invoking `check_stop_into_carry` at the same callsite shape is the lower-edge corroborating "second reuse" evidence for the cycle-008 promotion criterion, but it does **not** unblock firm L4 promotion of the helper: GMRES and FGMRES are sister algorithms in one translation unit on a single solver-family pair, so the structural population does not stress the helper signature in a new dimension. The strong-reuse evidence — a non-`GmresSolverBase` Krylov consumer (e.g., a literature-anchored MINRES inner loop, or NLEPS once spec'd) — is still required, tracked by OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`. The dep-map row stays plain-text per cycle-006 friction-ledger `rough-in-rows-must-be-plain-text-when-anchor-missing`.

**Lowering-verifier follow-up** (cycle-021+ candidate, now that both this and the sibling theme are firm): confirm that the L3 forms produced by applying both themes to the migrated `gmres.md §L4 v0.7 inner_loop` are pairwise consistent with the firm [`L3/krylov-step`](../L3/krylov-step.md) inner-step shape (the GMRES `ls_update_column` sequential obstruction is recorded there as a body-primitive non-lift, not at the wrapper level). If the verifier finds a mismatch (e.g., the v0.7 `check_stop_into_carry` does not lift cleanly to the L3 shape for FGMRES specifically), the theme is refined.
```

### Edit 12 — L4 index dep-map prose-list: add the fgmres theme as a firm L4>L3 row

The fgmres theme is currently **absent from `book/src/L4/index.md` entirely** (verified by `grep -n fgmres` — no hits; it is wired into `SUMMARY.md:17` but never made it into the L4 index prose list or dep-map table). Firming it is the moment to add its prose-list row, immediately after the firm gmres sibling row (`index.md:44`). **Note for the integrator**: this is `layer-intro-author` territory (the L4 index is theirs); I emit the proposed-change with sibling-parallel wording, but the integrator may prefer to apply it as a consistency-repair / defer the exact wording to a `layer-intro-author` follow-up, as the cycle-020 gmres dispatch did for the dep-map firm-sync. Either way it must not be missed (a firm theme absent from its layer's dep-map is a cross-reference-integrity gap the critic would flag).

```edit:book/src/L4/index.md
[old]: - [`gmres-inner-loop-iterate-while-migration`](../L4-L3/gmres-inner-loop-iterate-while-migration.md) *(firm; cycle-020 wave-1 lifter re-anchor)* — the L4>L3 dissolution of the migrated GMRES inner loop under the upstream re-rendering of `gmres.md` §L4's `inner_loop` as a direct `iterate_while` invocation. The upstream `gmres.md` self-rotation landed (slice §L4 v0.7, cycle-020); the theme is firm against its now-realized LHS surface.
[new]: - [`gmres-inner-loop-iterate-while-migration`](../L4-L3/gmres-inner-loop-iterate-while-migration.md) *(firm; cycle-020 wave-1 lifter re-anchor)* — the L4>L3 dissolution of the migrated GMRES inner loop under the upstream re-rendering of `gmres.md` §L4's `inner_loop` as a direct `iterate_while` invocation. The upstream `gmres.md` self-rotation landed (slice §L4 v0.7, cycle-020); the theme is firm against its now-realized LHS surface.
- [`fgmres-inner-loop-iterate-while-migration`](../L4-L3/fgmres-inner-loop-iterate-while-migration.md) *(firm; cycle-021 wave-1 lifter re-anchor)* — the FGMRES specialisation of the gmres sibling's L4>L3 dissolution, sharing the *same* upstream `gmres.md` §L4 v0.7 migration with two variant-axis collapses (`pc_side = RIGHT` pinned at the `FgmresSolver` constructor, `flexible = true` making the `Z` carry-update unconditional) plus a per-iteration `Z[j]` workspace. Firm against the now-firm gmres sibling; the shared `check_stop_into_carry` helper stays rough-in (promotion blocked on a non-`GmresSolverBase` consumer per OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`).
```

## Discipline notes

- **What changed and why (pure re-anchoring).** The rough-in theme `fgmres-inner-loop-iterate-while-migration` (authored cycle-010/011 era as a sibling specialisation) was rough-in *for exactly the same reason its sibling was* — both depended on the unwritten upstream `gmres.md` §L4 v0.6→v0.7 self-rotation. The gmres dispatch (cycle-020 wave-1) authored that rotation and firmed the gmres sibling. Because the rotation is **shared** (FGMRES instantiates the same v0.7 migration with variant collapses), this dispatch is a **pure re-anchor**: the theme's structure (Context / LHS / RHS / Applicability / Justification / Speculative-ops / Verified-against / Status) is untouched; only the "speculative upstream" / "not-yet-authored" / "rough-in" framing firms up (Edits 1–5, 8–11) and the drifted slice line-refs re-anchor (Edits 6, 8). No content authorship — the LHS code block is unchanged (the rough-in already sketched the option-(a) shape the rotation took). Status flips `rough-in` → `firm` (Edit 11).

- **High→low direction preserved.** The theme's LHS stays L4 (the v0.7 `iterate_while` invocation, FGMRES-specialised), its RHS stays L3 (the value-threaded dissolution), and the prose narrates the rewrite forward (L4 into L3). No inversion. The variant-axis collapses (`pc_side = RIGHT`, `flexible = true`) and the `Z[j]` workspace are FGMRES specialisations of the *same* high→low rotation, not a re-direction. Notes about the reverse direction do not appear in the formal chapter; this dispatch's working notes (this CYCLE.md) carry the provenance.

- **Bounded prose-correction recorded (the stale-citation sweep).** Per friction-ledger `lifter-scope-content-correction-boundary` (cycle-012), I corrected the theme's drifted slice line-refs in place. The drift is **evidenced and bounded**: the gmres slice was reduced between the theme's authoring and now (its v0.1 form lifted into firm entries per the slice stub-header; v0.6 moved to `:594-606`), so every stale `gmres.md:NNN` citation in the fgmres theme drifted exactly as its sibling's did (the gmres dispatch found and fixed the same drift). Corrected citations and their **verified** new homes (each read directly this dispatch):
  - v0.6 `inner_loop` + `check_stop` form: `gmres.md:539-672` → `:594-606` (verified: `inner_loop :: OpParams -> Convergence -> Krylov -> Solve (Krylov, StopReason)` at line 594), `:587-592` (verified: `check_stop :: ... -> Maybe StopReason` at 587), `:551-554` (verified: `data StopReason` at 551).
  - Variant-axis profile: `gmres.md:120`, `:121`, `:118-124` → the v0.6 constructed-operator surface table at `gmres.md:645-654` (verified each cited row: `apply_BA`/`pc_side` at 648, `orthogonalize`/`gs_orthog` at 649, `apply_correction`/`pc_side,flexible` at 650, `check_stop`/`max_it,max_dim` at 652), plus the §"Variant axes" sections at `:172-176`/`:248-252` and the `max_dim` guard at `:591`.
  - Upstream-rotation pointer: added `gmres.md:673-747` (the firm §L4 v0.7 section) wherever the theme referenced the (formerly unwritten) upstream rotation — verified the section exists (`## L4 v0.7 — inner-loop iterate_while migration` at line 673; the v0.7 `inner_loop` + `check_stop_into_carry` at 694-716; line 746 names the FGMRES sibling as the second-consumer trigger).
  This sweep is **bounded** (fixing drifted citations / firming framing only; no decomposition / signature / sub-pattern change, no re-architecture) — consistent with "structural rewrite, not authorship".

- **FGMRES-specific L0 citations re-verified (all current, source not slice — stable as the brief predicted).** The theme's own FGMRES L0 anchors point at `iterative.hpp` / `iterative.cpp` (source, not slice), so they were not exposed to the slice-reduction drift. I re-verified them anyway (codemap `read_range`, this dispatch):
  - `iterative.hpp:222` — `class FgmresSolver : public GmresSolver<OperType>` ✓ (line 222).
  - `iterative.hpp:256-257` — `// Temporary workspace for solve.` + `mutable std::vector<VecType> Z;` ✓ (the FGMRES-only `Z[j]` workspace member).
  - `iterative.hpp:263-266` — `FgmresSolver(MPI_Comm comm, int print)` constructor pinning `pc_side = PreconditionerSide::RIGHT;` ✓ (constructor at 263, pin at 265).
  - `iterative.hpp:268-273` — `SetPreconditionerSide` override with `MFEM_VERIFY(side == PreconditionerSide::RIGHT, ...)` ✓ (268-271).
  - `iterative.cpp:794-829` — FGMRES `Mult` inner Arnoldi loop, `for (;; j++, it++)` at 794 ✓.
  - `iterative.cpp:806` — `ApplyBA(PreconditionerSide::RIGHT, A, B, V[j], w, Z[j], this->use_timer);` ✓ — the **hard-coded `RIGHT`** (vs GMRES's `pc_side`) AND the **`Z[j]` workspace** (vs GMRES's `r`), the two FGMRES deltas, both on this one line.
  - `iterative.cpp:806-819` — per-step body (`ApplyBA → OrthogonalizeIteration → Norml2 → ApplyPlaneRotation ×k → GeneratePlaneRotation → ApplyPlaneRotation ×2`) ✓.
  - `iterative.cpp:821-823` — `beta = std::abs(s[j + 1]); CheckDot(beta, "FGMRES residual norm ...");  converged = (beta < eps);` ✓ (821/822/823); the theme's "`converged = (beta < eps)` at line 823" is exact.
  - `iterative.cpp:824` — `if (converged || j + 1 == max_dim || it + 1 == max_it)` ✓; the theme's "`MaxDim` from `j + 1 == max_dim` at line 824; `MaxIt` from `it + 1 == max_it` at line 824" is exact.
  - `iterative.cpp:823-828` — the 3-condition break fingerprint (`converged=` at 823, `if` at 824, `it++; break;` at 826-827, close 828) ✓; textually identical to the GMRES site `:644-649` (`converged=` 644, `if` 645, close 649) — the cycle-010 combinator-miner audit fingerprint pair holds.
  - `iterative.cpp:756-765` (out-of-scope `restart_cycle` initial-residual policy) — `true_beta = linalg::Norml2(comm, Z[0]);` at 756 after `InitialResidual(...)` at 754-755 ✓; the drift-warning compare `std::abs(beta - true_beta) > 0.1 * true_beta` at `:772-780` ✓. Correctly scoped OUT of this theme (lives in `restart_cycle`, one level up).

- **`check_stop_into_carry` left rough-in (no promotion).** The migration uses the speculative helper but does not promote it to a firm L4 row — the promotion bar (a non-`GmresSolverBase` consumer that stresses the signature in a new dimension) is unmet; FGMRES is the sister algorithm, not a new dimension. This is the explicit cycle-010-audit verdict the theme already records, unchanged. The theme is firm *as a dissolution theme* with one rough-in helper in its LHS vocabulary (the `krylov-step-typed-wrapper-dissolution` precedent). The dep-map row stays plain-text.

- **No book/ writes.** All edits are emitted as proposed-changes blocks for `integrator-per-report` to apply (DISPATCH-phase write-guard; re-anchors are PROPOSALS, not edits — friction-ledger `specialized-agent-direct-write-to-book-during-dispatch`). This includes the L4 index dep-map row (Edit 12), flagged for the integrator as `layer-intro-author` territory.

## Supporting evidence

L0 (Palace FGMRES; verified this dispatch via codemap `read_range`):
- `reference/palace/palace/linalg/iterative.hpp:222` — `class FgmresSolver : public GmresSolver<OperType>`.
- `reference/palace/palace/linalg/iterative.hpp:256-257` — `mutable std::vector<VecType> Z;` (FGMRES-only per-iteration preconditioner-output workspace).
- `reference/palace/palace/linalg/iterative.hpp:263-266` — constructor pinning `pc_side = PreconditionerSide::RIGHT`.
- `reference/palace/palace/linalg/iterative.hpp:268-273` — `SetPreconditionerSide` override `MFEM_VERIFY`-ing `RIGHT`.
- `reference/palace/palace/linalg/iterative.cpp:794-829` — FGMRES `Mult` inner Arnoldi loop.
- `reference/palace/palace/linalg/iterative.cpp:806` — `ApplyBA(PreconditionerSide::RIGHT, A, B, V[j], w, Z[j], ...)` (the two FGMRES deltas: hard-coded `RIGHT` + `Z[j]` workspace).
- `reference/palace/palace/linalg/iterative.cpp:821-824` — `beta`/`CheckDot`/`converged` + the 3-condition break test.
- `reference/palace/palace/linalg/iterative.cpp:756-765,772-780` — `restart_cycle` `true_beta = nrm2(comm, Z[0])` + drift-warning (out-of-scope; lives one level up).
- (For the GMRES fingerprint comparison) `reference/palace/palace/linalg/iterative.cpp:642-649` — GMRES `converged`/break test, textually identical to FGMRES `:821-828` modulo `ApplyBA`'s 3rd arg + workspace.

L4 / L4>L3 (verified this dispatch via Read):
- `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` (firm, cycle-020 wave-1) — the sibling theme; this dispatch inherits its now-firm rotation, conditions 1–5, and LHS shape.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (firm, cycle-008 wave-1) — the wrapper-dissolution shape precedent.
- `book/src/L4/iterate-while.md` (firm, cycle-007) — §Signature (point 1: predicate `α -> Bool`), §Semantics, §Algebraic laws Law 1 (§3.8 trajectory pruning), §Signature line 51 (GMRES extras `{ residual_norm, breakdown_token }`) — the firm combinator the LHS invokes.
- `book/src/spec/slices/gmres.md:551-554,587-592,594-606,613-631,645-654,673-747,172-176,248-252` — the v0.6 `StopReason`/`check_stop`/`inner_loop`/`restart_cycle`, the v0.6 surface table, the firm §L4 v0.7 self-rotation section (the shared upstream rotation), and the variant-axis sections.
- `book/src/L4/index.md` (no `fgmres` hit before this dispatch; `gmres` theme row at :44) — the dep-map the fgmres theme is missing from.
- `book/src/SUMMARY.md:17` — confirms the fgmres theme is wired into book nav (live link).

Reports:
- `reports/2026-05-29T034441Z-lifter-gmres-l4-self-rotation/CYCLE.md` — the cycle-020 sibling dispatch that authored the shared upstream v0.7 rotation and firmed the gmres sibling (the precedent this re-anchor parallels).
- `reports/2026-05-27T215535Z-combinator-miner-check-stop-into-carry-mcp-pilot/CYCLE.md` — the cycle-010 MCP-pilot combinator-miner audit confirming the GMRES `:644-649` / FGMRES `:823-828` textually-identical 3-condition fingerprint (the theme's §Speculative-L4-operators "second reuse" evidence).

## Open questions / caveats

1. **This CLOSES the fgmres carry-forward (provenance for the meta-phase).** The `fgmres-inner-loop-iterate-while-migration-lifter-candidate` OQ was opened cycle-010 (combinator-miner) and has been a **multi-batch carry-forward** — deferred at cycle-010 (waiting on the upstream gmres rotation), restated as the cycle-011 enactment candidate, and held again at cycle-020 (the gmres dispatch firmed the sibling but explicitly HELD fgmres for cycle-021). This cycle-021 dispatch is the terminal enactment: the theme firms, and Edit 10 proposes closing the OQ as `resolved`. **Meta-phase note**: this closes a 5-batch-old (cycle-010 → cycle-021) carry-forward; the closure is clean (the shared upstream rotation landed cycle-020, no FGMRES-specific blocker remained). No new carry-forward is opened by this dispatch.

2. **`check_stop_into_carry` promotion stays blocked (NOT closed by this dispatch).** FGMRES being the sister algorithm corroborates the "second reuse" but does not stress the helper signature in a new dimension; the firm-promotion blocker (OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`, a non-`GmresSolverBase` consumer) is unchanged and stays `open`. The dep-map row for the helper stays plain-text.

3. **L4 index dep-map gap (flagged for the integrator).** The fgmres theme was **never added to `book/src/L4/index.md`** — the L4>L3 prose-list does not mention it (it is only in `SUMMARY.md`). (The L4 dep-map *table* is operator-rows-only — L4>L3 themes are not table rows there — so the prose-list is the correct and sufficient home; Edit 12 targets it.) Edit 12 proposes the prose-list row. Because the L4 index is `layer-intro-author` territory and the exact wording is theirs, the integrator may apply Edit 12 as a consistency-repair (as the cycle-020 dispatch did for the gmres dep-map firm-sync) OR route the wording to a `layer-intro-author` follow-up. **It must not be silently dropped**: a firm theme absent from its layer's dep-map is a cross-reference-integrity drift the critic would flag. (The pre-existing absence — the theme was rough-in and never listed — is itself the gap; firming is the moment to fix it.)

4. **`Z[j]` workspace — variant-axis vs. component note (no action; recorded).** The FGMRES `Z[j]` per-iteration workspace (`iterative.hpp:256`, `iterative.cpp:806`) is the one *structural* FGMRES delta beyond the two variant-pins. The theme already models it correctly as the unconditional carry-update `K { Z = K.Z `with` (K.j, z) }` (the `flexible = true` collapse of the gmres sibling's `if op.flexible then ... else K`). This is a faithful model: at L4 the carry's `Z :: Vec[]` field is "always populated under FGMRES" (theme line 36), and the L0 `Z[j] = ApplyBA(...)` write is the per-step capture. No re-architecture needed — the carry already carries `Z`. Recorded for completeness; not a caveat.

5. **Lowering-verifier follow-up (cycle-021+, now unblocked).** With BOTH the gmres sibling and this fgmres theme firm, a lowering-verifier dispatch can now audit that the L3 forms produced by applying both themes to the migrated `gmres.md §L4 v0.7 inner_loop` are pairwise consistent with the firm `L3/krylov-step` inner-step shape (and that the FGMRES variant collapses + the `Z[j]` capture lift cleanly). Not blocking; flagged as the natural next audit (the theme's §Status records it as a cycle-021+ candidate).

---
agent: lifter
invoked_at: 2026-05-28T034235Z
scope: L4>L3 theme re-anchor (cross-reference cleanup) — L4/index.md SUPERSEDED-text drift on krylov-step-typed-wrapper-dissolution
status: integrated
integrated_at: 2026-05-28T072500Z
integration_commit: 5964cb4
integration_notes: "Applied cycle-012 (report 7 of 8). book/src/L4/index.md:40 re-anchored -- struck stale cycle-006 'no L3 row needed' clause + added forward-pointer to firm L3/krylov-step.md + explicit SUPERSEDED marking (cites 'Identity-lowerings still require both L levels' invariant). Resolves the integrator-signals carry-forward flag chain (cycle-010 wave-1 pass-2 META Issue 1, re-flagged cycle-011) -- marked resolved in integrator-signals §cycle-012 (finalize-only authority). Theme-body line-20/220 residual routed to OQ krylov-step-theme-body-no-l3-row-drift-cycle-013. 0 gate hits. Build exit 0."
inputs:
  - book/src/L4/index.md
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
  - book/src/L3/krylov-step.md
  - scaffolding/integrator-signals.md (carry-forward flag, lines 58/91/150/184)
  - CLAUDE.md §Methodology invariants "Identity-lowerings still require both L levels"
---

# CYCLE: Re-anchor L4/index.md — strike SUPERSEDED "no L3 row needed" verdict

## Summary

This is the cycle-012 smallest-cost carry-forward cleanup (flagged cycle-010 wave-1 pass-2 META Issue 1, re-flagged in cycle-011 integrator-signals, not selected by either cycle-010 or cycle-011 planner). `book/src/L4/index.md:40` — the L4>L3 lowering-themes bullet for `krylov-step-typed-wrapper-dissolution` — still carries the cycle-006-era verdict text "the kernel body's primitive sequence is identity-in-form, so **no intermediate L3 `krylov-step` row is needed**". That verdict was formally SUPERSEDED at cycle-010 when `book/src/L3/krylov-step.md` (first firm L3 operator, 225 lines) landed as the identity-lowering backfill enacting the CLAUDE.md §Methodology invariants bullet **"Identity-lowerings still require both L levels"** (codified cycle-009 meta-phase). The cycle-010 dispatch struck the verdict inside the L4-L3 theme itself (SUPERSEDED-annotation at `krylov-step-typed-wrapper-dissolution.md:218`) but did NOT touch the L4/index.md cross-reference — explicitly out-of-scope per that dispatch's instructions. The cycle-011 FGMRES lifter touched `L4-L3/index.md`, not `L4/index.md`, so the drift persists.

**VERIFY-BEFORE-DISPATCH result: stale text CONFIRMED PRESENT.** `book/src/L4/index.md:40` verbatim ends: "...the kernel body's primitive sequence is identity-in-form, so no intermediate L3 `krylov-step` row is needed." The substantive supersession is already in place: `book/src/L3/krylov-step.md` exists (cycle-010, commit `30119eb` "first firm L3 operator (krylov-step backfill)"). This is a pure cross-reference re-anchor of one bullet.

This is a structural rewrite, not authorship: the bullet's narrative (wrapper-machinery dissolution into L3 value-threading; the kernel-body primitive sequence is identity-in-form) is preserved verbatim; only the trailing **consequence clause** — which drew the now-superseded "no L3 row needed" conclusion from the identity-in-form premise — is re-anchored to point at the firm L3 entry. The rewrite stays high→low: the bullet still describes how the L4 form lowers to L3.

## Proposed changes

```edit:book/src/L4/index.md
[old]: - [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) — firm (cycle-008 wave-1 lifter promotion). The wrapper machinery (state-stratification records, `Solve` monad, `OpParams` `readonly`, Form A/B distinction) dissolves into L3 value-threading; the kernel body's primitive sequence is identity-in-form, so no intermediate L3 `krylov-step` row is needed.
[new]: - [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) — firm (cycle-008 wave-1 lifter promotion). The wrapper machinery (state-stratification records, `Solve` monad, `OpParams` `readonly`, Form A/B distinction) dissolves into L3 value-threading; the kernel body's primitive sequence is identity-in-form. The firm L3 image of this dissolution is the layer-coherent operator entry [`L3/krylov-step`](../L3/krylov-step.md) (authored cycle-010 wave-1, `reports/2026-05-27T215300Z-harvester-l3-krylov-step/CYCLE.md`). The cycle-006 verdict that "no intermediate L3 `krylov-step` row is needed" on identity-in-form grounds is **SUPERSEDED** per the CLAUDE.md §Methodology invariants bullet "Identity-lowerings still require both L levels" (codified cycle-009 meta-phase): each layer is coherent within itself, so an L3 reader finds `krylov-step` defined in L3 vocabulary at L3 even though the rewrite is trivial. The SUPERSEDED annotation is recorded at [`krylov-step-typed-wrapper-dissolution.md` §"Audit of cycle-002 identity-in-form claim"](../L4-L3/krylov-step-typed-wrapper-dissolution.md).
```

No LHS/RHS shape adjustment is required: the firm `L3/krylov-step.md` entry is the wrapper-dissolution RHS rendered as a layer-coherent operator (per `integrator-signals.md:162`, "the L3 form is the wrapper-dissolution RHS rendered as a layer-coherent operator entry, not a duplicate of L2"). The theme's rewrite direction (L4 typed-wrapper form → L3 value-threading form) is unchanged; only the bullet's now-false trailing consequence ("no L3 row needed") is re-anchored to the firm L3 entry. No applicability-condition change. No "Speculative L_{n+1} operators" section exists on this page (it is the L4 layer index, not a theme file), so none is trimmed. Theme status stays `firm` (it was already firm pre-cleanup; this cleanup does not alter that).

## Discipline notes

- **Minimal surgical edit, one bullet.** The L4 index intro prose, Vocabulary-cohort framing, dep-map table, and Working-Notes section are untouched. Only the single L4>L3-lowering-themes bullet at line 40 is re-anchored.
- **High→low direction preserved.** The bullet narrates the L4 form lowering into L3 (wrapper machinery dissolving into L3 value-threading). The re-anchor adds a forward pointer to the firm L3 entry that is the *image* of this lowering; it does not invert into "how the L3 form lifts to L4." No reverse-direction prose was introduced into the chapter (lifting-direction notes, where relevant, stay in working notes per the `layer-definition-discipline-high-to-low` invariant — there are none needed here).
- **Why the change.** The cycle-006 "no L3 row needed" conclusion was a category error (per `integrator-signals.md:162` and the theme-file annotation at `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:218`: the difference between "L3 `krylov-step`" and "L2 `krylov-step` with an outer `iterate_while` tail-recursion" is the **layer rendering**, not the operational content). The cycle-009 meta-phase codified the corrective invariant; the cycle-010 wave-1 backfill enacted it by authoring `L3/krylov-step.md`. This dispatch propagates that enactment to the last stale cross-reference.
- **Cross-references to the promoting work.** The L3 backfill harvester report is `reports/2026-05-27T215300Z-harvester-l3-krylov-step/CYCLE.md` (landed cycle-010, commit `30119eb`). The supersession of the cycle-006 verdict was recorded inside the theme at `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:218`; this dispatch keeps the new bullet's pointer aimed at that audit section.

## Supporting evidence

- `book/src/L3/krylov-step.md` — the firm L3 operator entry (exists on disk; 225 lines / ~40KB; landed cycle-010). The target of the re-anchored pointer.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:218` — canonical SUPERSEDED-verdict annotation language this edit mirrors ("This verdict is **SUPERSEDED** by the user directive 2026-05-27 mid-cycle-009 codified as the CLAUDE.md §Methodology invariants bullet **Identity-lowerings still require both L levels**" + "Cycle-010 backfill: the L3 entry [`L3/krylov-step`](../L3/krylov-step.md) was authored cycle-010 wave-1").
- `scaffolding/integrator-signals.md:58, 91, 150, 184` — the carry-forward flag chain (cycle-010 wave-1 pass-2 META Issue 1 → cycle-011 re-flag → cycle-012 smallest-cost candidate).
- `scaffolding/integrator-signals.md:162` — "Cycle-006 verdict 'no L3 row needed for krylov-step' formally SUPERSEDED via SUPERSEDED-annotation at `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:218`."
- CLAUDE.md §Methodology invariants — "Identity-lowerings still require both L levels" (the load-bearing invariant the edit cites).
- Commit `30119eb` (cycle-010 integrator-finalize) — "first firm L3 operator (krylov-step backfill)".

## Open questions / caveats

- **In-scope: closed.** This dispatch closes the carry-forward OQ (`lifter` on `book/src/L4/index.md:40` SUPERSEDED-text drift). The single-edit re-anchor resolves the last stale cross-reference of the cycle-006 verdict in the L4 index.
- **OQ (promote): residual stale "no L3 row" phrasing inside the theme body.** Suggested slug `krylov-step-theme-body-no-l3-row-drift-cycle-013`. The L4-L3 theme `krylov-step-typed-wrapper-dissolution.md` carries the correct SUPERSEDED annotation at line 218, but two earlier passages still phrase the old conclusion as if live: line 20 ("...so **no L3 `krylov-step` row is promoted by this theme**...") and line 220 ("...the assertion holds, the framing is sharpened, **no L3 row needed**"). These are inside the theme body, not the L4 index, and are outside this dispatch's single-edit scope (one theme per invocation; this invocation re-anchors the L4 index reference). They are internally reconciled by the line-218 SUPERSEDED annotation but read as drift to a fresh reader. **Recommend a follow-up `lifter` dispatch** on `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` to re-anchor lines 20 and 220 to the firm `L3/krylov-step.md` entry consistent with line 218. Low-cost; not blocking. (Routes to cycle-013+ planner if uniformity is desired. Critic Issue 3 confirmed both line-20 and line-220 passages present by direct read — true positive for the planner queue.)
- **No signature contradiction.** The firm `L3/krylov-step.md` is the wrapper-dissolution RHS rendered as a layer-coherent L3 operator — it does not contradict what the theme assumed (the theme's RHS *is* this L3 form). No abstractor reread is needed; this remains a pure rewrite.

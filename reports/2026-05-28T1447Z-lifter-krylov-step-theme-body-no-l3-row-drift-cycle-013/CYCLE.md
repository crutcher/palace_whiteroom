---
agent: lifter
invoked_at: 2026-05-28T1447Z
scope: L4>L3 theme re-anchor — krylov-step-theme-body-no-l3-row-drift-cycle-013
status: integrated
integrated_at: 2026-05-28T200000Z
integration_commit: a4d7495
integration_notes: "cycle-013 finalize. 2 stale cycle-006 'no L3 row' residuals (line 20 + 220) struck + re-anchored to firm L3/krylov-step.md; dangling cg.md:341-362 pointer re-anchored to firm L3-L2/krylov-step-body-identity.md. Theme-wide cg.md sweep routed to OQ krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep. Did NOT double-close krylov-step-l3-identity-in-form-audit (answered_in cycle-006). Clean run."
inputs:
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
  - book/src/L3/krylov-step.md
  - book/src/L3-L2/krylov-step-body-identity.md
---

# CYCLE: Re-anchor krylov-step-theme-body-no-l3-row-drift-cycle-013

## Summary
The L4>L3 theme `krylov-step-typed-wrapper-dissolution.md` carries two theme-body residuals still asserting the stale cycle-006 verdict that "no L3 `krylov-step` row" is produced/needed (Context §, line 20; Open-question-disposition §, line 220). That verdict is superseded twice over: (1) the cycle-009 meta-phase invariant **"Identity-lowerings still require both L levels"**, and (2) the cycle-010 firm backfill `book/src/L3/krylov-step.md`, which now exists. The §"Audit of cycle-002 identity-in-form claim" (lines 218, 293) already carries the correct SUPERSEDED framing and the cross-reference to `L3/krylov-step.md`; the cycle-012 lifter already cleaned the `L4/index.md` cross-reference. This dispatch re-anchors only the two surviving theme-body residuals so the prose is internally consistent with the entry's own §Audit and with the existing firm L3 row. Pure rewriting — structure preserved, only the stale vocabulary firms up; no new claims, no restructure.

## Proposed changes

Both re-anchors swap the stale "no L3 row promoted / needed" phrasing for the current vocabulary: krylov-step DOES have a firm L3 entry (`book/src/L3/krylov-step.md`, cycle-010 backfill), so the lowering chain is **L4>L3>L2>L1 with no skipped rows** — this theme dissolves the L4 typed wrapper into the L3 form (`L3/krylov-step.md`), and the further `L3-L2/krylov-step-body-identity.md` theme completes the body's L3>L2 identity hop. Each re-anchor cites the cycle-009 identity-lowerings invariant and the existing L3 entry, consistent with how lines 218/293 already speak.

### Re-anchor 1 — Context § (line 20): "no L3 row promoted" → firm L3 row exists, chain has no skipped rows

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]: The L3 form this lowering produces is **identity-in-form** on the kernel body's primitive sequence — the same five primitive groups (apply, optional auxiliary, iterate-update, scalar-update, output-readout) in the same dataflow-forced order — but **substantively rotated** at the type/wrapper level. Crucially, the further L3>L2 lowering on the kernel body is identity-in-form per the combinator-miner cycle-002 assertion (`cg.md:341-362`, `arnoldi_step.md:178-213`), so no L3 `krylov-step` row is promoted by this theme: the L4 entry lowers via this theme to an L3 form that is value-thread-isomorphic to the L2 form, and the L3>L2 hop is the trivial completion. See §"Audit of cycle-002 identity-in-form claim" below for the full audit.
[new]: The L3 form this lowering produces is **identity-in-form** on the kernel body's primitive sequence — the same five primitive groups (apply, optional auxiliary, iterate-update, scalar-update, output-readout) in the same dataflow-forced order — but **substantively rotated** at the type/wrapper level. The further L3>L2 lowering on the kernel body is identity-in-form per the firm theme [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) (which ratifies the combinator-miner cycle-002 assertion; the original slice evidence at `cg.md:341-362` has been lifted into that firm entry per the cycle-009 corpus reduction, and `arnoldi_step.md:178-213` remains the valid live anchor), but this does **not** collapse the L3 row away: the L4 entry lowers via this theme to the firm L3 entry [`L3/krylov-step`](../L3/krylov-step.md) (the value-threaded RHS rendered as a layer-coherent operator), and the body's L3>L2 identity hop is completed by the separate theme [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md). The lowering chain is therefore L4>L3>L2>L1 with no skipped rows. (The earlier cycle-006 reading — that the body's identity-in-form lets this theme skip the L3 row and lower transitively to L2 — is SUPERSEDED by the user directive 2026-05-27 mid-cycle-009 codified as the CLAUDE.md §Methodology invariants bullet **Identity-lowerings still require both L levels**: each layer is coherent within itself, so an L3 reader must find `krylov-step` defined in L3 vocabulary at L3 even when the body rewrite is trivial.) See §"Audit of cycle-002 identity-in-form claim" below for the full audit.
```

### Re-anchor 2 — Open-question-disposition § (line 220): "no L3 row needed" → L3 row exists, body-identity sharpening only

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]: **Open question disposition**: this dispatch *audits* the cycle-005 open question `krylov-step-l3-identity-in-form-audit` and proposes closing it as **confirmed-with-refinement** — the assertion holds, the framing is sharpened, no L3 row needed. Integrator will mark accordingly; if integration uncovers a non-identity finding (e.g., a corpus check on a slice this dispatch did not re-verify reveals body-level rotation), the question stays open and a cycle-007 L3 row promotion follows.
[new]: **Open question disposition**: this dispatch *audits* the cycle-005 open question `krylov-step-l3-identity-in-form-audit` and proposes closing it as **confirmed-with-refinement** — the assertion holds and the framing is sharpened (the L4>L3>L2 step-body chain is identity-in-form on the kernel body's primitive sequence; the L4>L3 hop is non-identity only at the wrapper level). This identity-in-form finding governs the *body* rewrite; it does NOT eliminate the L3 row — per the cycle-009 invariant **Identity-lowerings still require both L levels**, the firm L3 entry [`L3/krylov-step`](../L3/krylov-step.md) is its layer-coherent rendering (authored cycle-010 wave-1, see §"Audit of cycle-002 identity-in-form claim" below). Integrator will mark accordingly; if integration uncovers a non-identity finding (e.g., a corpus check on a slice this dispatch did not re-verify reveals body-level rotation), the question stays open and the L3 row is re-rendered with the body rotation made explicit.
```

## Discipline notes

- **Structural rewrite only.** Both edits firm up stale vocabulary in the theme's existing prose; no LHS/RHS shape change, no new claims, no restructure. The firmed-up L3 entry (`L3/krylov-step.md`) does not alter the theme's LHS (L4 form) or RHS (L3 form) — both were already correct in §"L4 form (LHS)" / §"L3 form (RHS)"; only the two meta-prose residuals asserting the L3 row's *absence* were stale.
- **High→low direction preserved.** The theme remains defined L4 (LHS) into L3 (RHS); the re-anchors narrate the rewrite forward (L4 wrapper dissolves into the L3 form) and add no reverse-direction (L3→L4 lift) prose to the formal chapter, per the CLAUDE.md §Methodology invariants "Layers are defined high→low" bullet and friction-ledger `layer-definition-discipline-high-to-low`.
- **Why these two and not the §Audit prose:** lines 218 ("Consequence for L3 dep-map … SUPERSEDED cycle-010") and 293 (§Status) already carry the correct post-cycle-010 framing with the `L3/krylov-step.md` cross-reference and the identity-lowerings invariant. They needed no touch. Lines 20 and 220 were the surviving residuals where the prose still asserted the row's absence as a live conclusion, contradicting the entry's own §Audit. The re-anchors make the Context § and the OQ-disposition § consistent with §Audit and §Status.
- **Cross-reference to the promotion provenance:** the firm L3 entry was promoted by the cycle-010 wave-1 harvester (`reports/2026-05-27T215300Z-harvester-l3-krylov-step/CYCLE.md`, priority #20 identity-lowering-both-levels-backfill), as already recorded verbatim at line 218. The body's L3>L2 identity theme (`L3-L2/krylov-step-body-identity.md`) was ratified cycle-009, as recorded at line 218. Both target files were verified to exist on disk during this dispatch.

## Supporting evidence

- `book/src/L3/krylov-step.md` — the firm L3 entry (cycle-010 backfill) that the re-anchored prose now points to as the lowering's RHS row. Verified present on disk (40486 bytes).
- `book/src/L3-L2/krylov-step-body-identity.md` — the one-line L3>L2 body-identity theme that completes the body hop. Verified present on disk (26828 bytes).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:218` — the §Audit prose already carrying the correct SUPERSEDED-cycle-010 framing + `L3/krylov-step.md` cross-reference; the two re-anchors bring lines 20 and 220 into line with it.
- CLAUDE.md §Methodology invariants, bullet **"Identity-lowerings still require both L levels"** (user directive 2026-05-27 mid-cycle-009) — the codified invariant superseding the cycle-006 "no L3 row" verdict.

## Open questions / caveats

None. The two formalized/backfilled entries (`L3/krylov-step.md`, `L3-L2/krylov-step-body-identity.md`) do not contradict any signature or applicability condition the theme assumed; this was a pure vocabulary re-anchor and required no abstractor reread. The theme's `firm` status is unchanged (all referenced operators are firm).

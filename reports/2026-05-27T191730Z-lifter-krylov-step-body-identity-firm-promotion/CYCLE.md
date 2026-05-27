---
agent: lifter
invoked_at: 2026-05-27T191730Z
scope: L3>L2 theme re-anchor — krylov-step-body-identity (firm-rough-in → firm via status-inheritance)
status: integrated
integrated_at: 2026-05-27T200036Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied cleanly via integrator-per-report pass 1 of cycle-009. First across-cycle status-inheritance promotion in the artifact. Closes cycle-008 integrator-signals "CYCLE-009 mechanical follow-up" priority item. Krylov-step lowering chain now fully firm (L4 > L4>L3 > L3 > L3>L2 > L2).
inputs:
  - book/src/L3-L2/krylov-step-body-identity.md
  - book/src/L3-L2/index.md
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (upstream — now firm as of cycle-008)
  - scaffolding/open-questions.md (OQ iterate-while-l3-rendering-trajectory-accumulation-gap is `answered` cycle-008; OQ iterate-while-l4-anchor-missing is `answered` cycle-007)
  - scaffolding/integrator-signals.md (cycle-008 §"L4>L3 krylov-step-typed-wrapper-dissolution (firm, promoted cycle-008 wave-1 from rough-in)" + CYCLE-009 mechanical follow-up framing)
  - reports/2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close/CYCLE.md (upstream lifter dispatch that closed the gap)
---

# CYCLE: Re-anchor krylov-step-body-identity (firm-rough-in → firm)

## Summary

This dispatch promotes `book/src/L3-L2/krylov-step-body-identity.md` from `firm-rough-in` to plain `firm` via status-inheritance. The cycle-007 wave-1 theme declared `firm-rough-in` because its LHS (the L3 form) is referenced from the upstream L4>L3 `krylov-step-typed-wrapper-dissolution` theme whose status was `rough-in` at the time. Cycle-008 wave-1 pass-2 lifter dispatch (`reports/2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close/CYCLE.md`) firmed that upstream theme by applying the cycle-007 wave-2 lowering-verifier audit's three substantive changes (§3.8 collapse-rule citation, Condition 5, 10-citation `verified_against:` block), closing the iterate_while L3 trajectory-collapse gap (OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` → `answered`). The L3>L2 downstream theme is now auto-eligible for promotion per the plan-kind-consistency convention recorded in its own §Status.

This is a pure-rewriting pass: status field flipped at all 5 assertion sites in the body-identity file + 1 cell in the L3-L2 index dep-map; inheritance-acknowledgment paragraph added to §Status; stale claims about upstream `rough-in` status and about speculative `iterate_while`/`iterate_while_with_prev` operators being "rough-in" updated to reflect their cycle-008 / cycle-007 firm status. No body content, no semantic claims, no LHS/RHS shape changes. Per the lifter role spec: structure stays, vocabulary firms up.

## Proposed changes

### Change 1 — promote §Status block (lines 152-156)

```edit:book/src/L3-L2/krylov-step-body-identity.md
[old]:
## Status

`firm-rough-in` — the theme's ratification work is firm (the audit verdict is complete and citation-grounded; the body's identity-in-form mapping is total and bijective per §"Rewrite shape" line-by-line table; the surface adjustments — L3 `(op, K, s)` consolidation into L2 `(op, s)`; L3 tail-recursive outer-loop into L2 outer-driver-by-role — are wrapper-level and explicitly delimited; no speculative L3 vocabulary is introduced; the four applicability conditions are stated and confirmed satisfied for the existing five-slice corpus). The `rough-in` component is **inherited**: the L3 LHS form is referenced from the upstream `krylov-step-typed-wrapper-dissolution` theme whose §Status (line 216) is `rough-in`. The L2 RHS form is referenced from the firm `L2/krylov-step` entry. Per plan-kind-consistency, a downstream theme cannot be `firm` while its LHS-source dependency is `rough-in`; promotion of this theme to plain `firm` follows automatically when the upstream L4>L3 theme is itself promoted to `firm` (likely on completion of the cycle-006 audit's `lowering-verifier` follow-up named in the L4>L3 theme's §Status).

**Lowering-verifier follow-up** (cycle-008+ candidate): if a future slice (MINRES, BiCGStab, LOBPCG, etc.) is firmed at L2 with a body shape that does not match the existing pattern, this theme would need re-audit against the new shape. The cycle-006 audit's `lowering-verifier` follow-up (named in the L4>L3 theme's §Status) covers the L4>L3 hop; a parallel follow-up on this theme's L3>L2 hop would extend that coverage.
[new]:
## Status

`firm` — the theme's ratification work is firm (the audit verdict is complete and citation-grounded; the body's identity-in-form mapping is total and bijective per §"Rewrite shape" line-by-line table; the surface adjustments — L3 `(op, K, s)` consolidation into L2 `(op, s)`; L3 tail-recursive outer-loop into L2 outer-driver-by-role — are wrapper-level and explicitly delimited; no speculative L3 vocabulary is introduced; the four applicability conditions are stated and confirmed satisfied for the existing five-slice corpus). Both layer endpoints are themselves firm: the L3 LHS form is referenced from the upstream `krylov-step-typed-wrapper-dissolution` theme, promoted to `firm` in cycle-008; the L2 RHS form is referenced from the firm `L2/krylov-step` entry (cycle-005). The earlier `firm-rough-in` qualifier (cycle-007 wave-1) inherited the upstream's `rough-in` status under the plan-kind-consistency convention.

**Promoted to `firm` cycle-009 via status-inheritance** after upstream L4>L3 `krylov-step-typed-wrapper-dissolution` was promoted `firm` in cycle-008 (`reports/2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close/CYCLE.md`). That cycle-008 lifter dispatch applied the cycle-007 wave-2 lowering-verifier audit's three substantive changes — §3.8 collapse-rule citation at §"What the L3 form for `iterate_while` looks like", new Condition 5 in §"Applicability conditions" naming the consumer-demand precondition, trailing `verified_against:` block carrying the 10-citation audit evidence base — closing OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` as `answered` (cycle-008). Per plan-kind-consistency, with the upstream now firm and the L2 sink firm, the body-identity theme's downstream qualifier no longer applies; this dispatch is the mechanical re-anchor.

**Lowering-verifier follow-up** (cycle-009+ candidate): if a future slice (MINRES, BiCGStab, LOBPCG, etc.) is firmed at L2 with a body shape that does not match the existing pattern, this theme would need re-audit against the new shape. The cycle-007 wave-2 lowering-verifier covered the L4>L3 hop's trajectory-collapse question; a parallel verifier on this theme's L3>L2 hop would extend that coverage to per-slice body-shape verification.
```

### Change 2 — promote Context bullet (line 16)

```edit:book/src/L3-L2/krylov-step-body-identity.md
[old]:
- **L3>L2 firm-rough-in — this theme.** Ratifies the identity-in-form audit. The cycle-006 audit (`reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"Audit of cycle-002 identity-in-form claim") found the cycle-002 combinator-miner claim correct as stated for the body's L3>L2 edge: the L2 vocabulary (`apply_linop`, `axpy`/`axpby`/`axpbypcz`, `dot`/`nrm2`/`scal`, plus the slice-level `op.orthog`/`op.scalars` closures) is L3-native by inspection of each primitive's signature shape. The status is `firm-rough-in` rather than `firm` because the LHS form is inherited from the upstream L4>L3 theme whose §Status is `rough-in`; this theme's ratification work is firm but the LHS-source dependency is rough-in.
[new]:
- **L3>L2 firm — this theme.** Ratifies the identity-in-form audit. The cycle-006 audit (`reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"Audit of cycle-002 identity-in-form claim") found the cycle-002 combinator-miner claim correct as stated for the body's L3>L2 edge: the L2 vocabulary (`apply_linop`, `axpy`/`axpby`/`axpbypcz`, `dot`/`nrm2`/`scal`, plus the slice-level `op.orthog`/`op.scalars` closures) is L3-native by inspection of each primitive's signature shape. The theme was authored cycle-007 wave-1 at status `firm-rough-in` (inheriting the upstream L4>L3 theme's then-`rough-in` qualifier under the plan-kind-consistency convention) and promoted to plain `firm` in cycle-009 via status-inheritance after the upstream theme was itself promoted firm in cycle-008.
```

### Change 3 — update §Speculative L3 operators (lines 117-119)

```edit:book/src/L3-L2/krylov-step-body-identity.md
[old]:
**None.** This theme is the identity rotation; no new L3 vocabulary is introduced. The L3 form referenced in the LHS is the RHS of the firm-rough-in `krylov-step-typed-wrapper-dissolution` theme; the L2 form referenced in the RHS is the firm `L2/krylov-step` entry. Both endpoints exist in the artifact already; the theme ratifies their identity-in-form relationship.

The L4 `iterate_while` / `iterate_while_with_prev` rough-ins flagged in `L4-L3/krylov-step-typed-wrapper-dissolution.md` §"Speculative L4 operators" remain rough-in (they belong to the loop combinator, not the kernel body); the candidate cycle-007 harvester dispatch on those operators is tracked at open-questions slug `iterate-while-l4-anchor-missing`. This theme does not interact with that promotion — the kernel body's rotation is independent of the loop combinator's anchoring.
[new]:
**None.** This theme is the identity rotation; no new L3 vocabulary is introduced. The L3 form referenced in the LHS is the RHS of the firm `krylov-step-typed-wrapper-dissolution` theme (firmed cycle-008); the L2 form referenced in the RHS is the firm `L2/krylov-step` entry. Both endpoints exist in the artifact already; the theme ratifies their identity-in-form relationship.

The L4 `iterate_while` / `iterate_while_with_prev` operators flagged as rough-ins in the upstream `L4-L3/krylov-step-typed-wrapper-dissolution.md` §"Speculative L4 operators" were firmed by the cycle-007 wave-1 harvester (`reports/2026-05-27T160550Z-harvester-iterate-while-family-L4/`) as `book/src/L4/iterate-while.md` and `book/src/L4/iterate-while-with-prev.md` (closing OQ `iterate-while-l4-anchor-missing`). They belong to the loop combinator, not the kernel body; this theme does not interact with them — the kernel body's rotation is independent of the loop combinator's anchoring.
```

### Change 4 — update §Verified-against L4/L3 evidence (line 132)

```edit:book/src/L3-L2/krylov-step-body-identity.md
[old]:
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"L3 form (RHS)" (lines 55-89) — the L3 form this theme references as LHS. The cycle-006 audit derived this form from the L4 form by applying the wrapper-dissolution rewrite; the form is published as the RHS of that theme (the upstream theme is currently `rough-in` per its §Status line 216).
[new]:
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"L3 form (RHS)" (lines 55-89) — the L3 form this theme references as LHS. The cycle-006 audit derived this form from the L4 form by applying the wrapper-dissolution rewrite; the form is published as the RHS of that theme. The upstream theme was promoted to `firm` in cycle-008 (per its §Status line 293, post-cycle-008 lifter dispatch `reports/2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close/CYCLE.md`); the cycle-008 patch added the §3.8 collapse-rule citation, Condition 5, and a 10-citation `verified_against:` block, closing OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`.
```

### Change 5 — update L3-L2 index dep-map row (line 13)

```edit:book/src/L3-L2/index.md
[old]:
| [`krylov-step-body-identity`](./krylov-step-body-identity.md) | L3 form per [`L4-L3/krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)" — value-threaded `(op, K, s) -> (K', s', outputs)`, five-primitive-group let-chain (`apply_linop`, optional `op.orthog`/`op.scalars`, `axpy`/`axpby`/`axpbypcz`, `dot`/`nrm2`/`scal`, `derived_views`) plus explicit `s' = s { it = s.it + 1 }` counter-update. | L2 [`krylov-step`](../L2/krylov-step.md) §Semantics — primitive-composition form with consolidated `IterState` record absorbing the L3 `(K, s)` split; same five-primitive-group composition, outer driver referenced by role. | `empirical-match` (cycle-002 combinator-miner claim; cycle-006 audit confirmed-with-refinement) + secondary `structural` (each L1 primitive's signature shape is whole-tensor by construction) | `firm-rough-in` (cycle-007 abstractor; ratifies cycle-006 audit verdict; `rough-in` inherited from upstream L4>L3 theme whose status is `rough-in`) |
[new]:
| [`krylov-step-body-identity`](./krylov-step-body-identity.md) | L3 form per [`L4-L3/krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)" — value-threaded `(op, K, s) -> (K', s', outputs)`, five-primitive-group let-chain (`apply_linop`, optional `op.orthog`/`op.scalars`, `axpy`/`axpby`/`axpbypcz`, `dot`/`nrm2`/`scal`, `derived_views`) plus explicit `s' = s { it = s.it + 1 }` counter-update. | L2 [`krylov-step`](../L2/krylov-step.md) §Semantics — primitive-composition form with consolidated `IterState` record absorbing the L3 `(K, s)` split; same five-primitive-group composition, outer driver referenced by role. | `empirical-match` (cycle-002 combinator-miner claim; cycle-006 audit confirmed-with-refinement) + secondary `structural` (each L1 primitive's signature shape is whole-tensor by construction) | `firm` (cycle-007 abstractor at `firm-rough-in`; promoted cycle-009 via status-inheritance after upstream L4>L3 theme firmed cycle-008) |
```

## Discipline notes

**Pure structural rewrite.** No new content, no signature changes, no LHS/RHS shape changes, no applicability-condition changes. The theme's substantive content — the line-for-line body mapping, the two surface adjustments at the wrapper, the empirical-match + structural justification kinds — all stand untouched. Only the vocabulary firms up: every place where the file qualified its own status as `firm-rough-in` or pointed to an upstream `rough-in` dependency that has since firmed is updated to reflect the post-cycle-008 reality.

**Five assertion sites in body-identity.md, one in index.md:**
1. §Status block (lines 152-156) — Change 1 — full rewrite with inheritance-acknowledgment paragraph per role spec.
2. Context bullet (line 16) — Change 2 — `L3>L2 firm-rough-in` → `L3>L2 firm`; second `firm-rough-in` sentence rewritten as historical note.
3. §Speculative L3 operators paragraph 1 (line 117) — Change 3a — "firm-rough-in `krylov-step-typed-wrapper-dissolution`" → "firm `krylov-step-typed-wrapper-dissolution` (firmed cycle-008)".
4. §Speculative L3 operators paragraph 2 (line 119) — Change 3b — "`iterate_while` / `iterate_while_with_prev` rough-ins... remain rough-in" → "...were firmed by the cycle-007 wave-1 harvester" (these L4 ops are now firm per `book/src/L4/iterate-while.md` + `book/src/L4/iterate-while-with-prev.md`).
5. §Verified-against L4/L3 evidence (line 132) — Change 4 — "the upstream theme is currently `rough-in` per its §Status line 216" → "promoted to `firm` in cycle-008 per its §Status line 293".
6. `book/src/L3-L2/index.md` dep-map row status cell (line 13) — Change 5 — `firm-rough-in (...)` → `firm (...; promoted cycle-009 via status-inheritance...)`.

**Status convention precedent recorded.** This is the first instance in the artifact of a cycle-009 mechanical status-inheritance promotion firing (the cycle-007 integrator-signals note at line 167 flagged "first in-cycle status inheritance" as a pattern worth meta-phase formalization). The promotion follows directly from the plan-kind-consistency invariant: a downstream theme cannot be `firm` while its LHS-source dependency is `rough-in`. The cycle-008 upstream promotion satisfied the precondition; this dispatch enacts the downstream promotion mechanically.

**No body, no semantics changed.** The §"Rewrite shape" line-by-line mapping table, the four §"Applicability conditions", the §"Justification kind" empirical-match + structural breakdown, the §"L3 form (LHS)" / §"L2 form (RHS)" code blocks, the §"L3>L2 vs L4>L3 distinction" delimitation are all unchanged. The cycle-007 wave-1 author's content is preserved verbatim; only status anchors update.

## Supporting evidence

- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:293` — upstream §Status line confirming `firm` (cycle-008 promotion via `reports/2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close/CYCLE.md`).
- `scaffolding/open-questions.md:1240` — OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` `status: answered`, `answered_at: cycle-008`.
- `scaffolding/open-questions.md:1112-1117` — OQ `iterate-while-l4-anchor-missing` (slug at line 1112; `status: answered` at line 1115; `answered_at: cycle-007` at line 1116; `answered_in:` reference to cycle-007 harvester at line 1117); supports Change 3b.
- `scaffolding/integrator-signals.md:46,77,150,167` — cycle-008 integrator-signals routing this exact CYCLE-009 mechanical follow-up + cycle-007 "first in-cycle status inheritance" precedent.
- `reports/2026-05-27T160445Z-abstractor-krylov-step-body-identity-L3-L2/CYCLE.md` — original cycle-007 wave-1 abstractor dispatch (authored the theme at `firm-rough-in`).
- `reports/2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close/CYCLE.md` — cycle-008 lifter that firmed the upstream theme (the trigger for this dispatch).
- `book/src/L2/krylov-step.md` — L2 sink (firm, cycle-005); unchanged by this dispatch.
- `book/src/L4/iterate-while.md`, `book/src/L4/iterate-while-with-prev.md` — firm L4 rows (cycle-007); cited in Change 3b to update the formerly-`rough-in` claim.

## Open questions / caveats

None. This dispatch is the smallest-cost lifter the planner has dispatched to date and does exactly what the cycle-008 integrator-signals follow-up suggests. The promotion is purely mechanical:

- Both endpoints (L3 LHS upstream theme; L2 RHS sink) are firm.
- The plan-kind-consistency precondition (downstream cannot be `firm` while upstream is `rough-in`) is satisfied — upstream is now firm.
- All five assertion sites in the body-identity file and the single dep-map cell in `book/src/L3-L2/index.md` follow from the §Status change; the inheritance-acknowledgment paragraph satisfies the dispatch-spec's explicit requirement.
- No applicability conditions need refinement (the upstream theme's cycle-008 patch added Condition 5 at the *upstream* level; the downstream body-identity theme's four conditions stand unchanged — they were authored against the body-shape, not the trajectory-collapse rule).
- No L4/L3 pseudo-language conventions touched (no signatures, code blocks, reduction rules, or fenced text are edited — all edits are to prose status assertions and the index dep-map row).

The lifter role spec's "If the formalized operator's signature differs from the rough-in sketch, the theme's LHS/RHS may need adjustment — make those edits here" provision does not apply: the upstream theme's L3-form RHS was preserved verbatim across its cycle-008 lifter promotion (the lifter added §3.8 citation + Condition 5 + `verified_against:` block, but did not modify the L3 form code block at lines 55-89). The body-identity theme's LHS references that L3 form by cross-reference; the cross-reference is structurally stable.

No subsequent lifter or abstractor reread is recommended. The next cycle-009 follow-up on this lowering chain — if any — would be a `lowering-verifier` on a not-yet-firmed Krylov-shaped slice (MINRES, BiCGStab, LOBPCG) to verify per-slice body-shape conformance per the §Status follow-up note; that is a verifier dispatch, not a lifter dispatch, and is not blocked by this promotion.

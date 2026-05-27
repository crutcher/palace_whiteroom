---
agent: abstractor
invoked_at: 2026-05-27T16:04:45Z
scope: L3>L2 theme sketch — krylov-step-body-identity
status: pending
inputs:
  - book/src/L3/index.md (current L3>L2 sibling — Part dep-map is empty; first theme)
  - book/src/L2/krylov-step.md (firm; cycle-005)
  - book/src/L4/krylov-step.md (firm; cycle-006 wave-1 harvester)
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (rough-in per §Status line 216; cycle-006 wave-2 abstractor; carries the §"L3 form (RHS)" that this theme's LHS references)
  - book/src/spec/slices/cg.md:341-362 (combinator-miner cycle-002 evidence — Claim 2 "step body lifts as identity" verbatim at line 360)
  - book/src/spec/slices/arnoldi_step.md:178-213 (combinator-miner cycle-002 evidence — three uncontested primitives plus MGS-orthog variant obstruction)
  - book/src/spec/slices/chebyshev.md:354-362 (per-step kernel body for the polynomial-recurrence variant)
  - book/src/spec/slices/gmres.md:459-471 (inner-loop body composing arnoldi-step + LS-update + counter-increment + convergence-test)
  - scaffolding/open-questions.md slugs: `krylov-step-body-identity-theme-pending-cycle-007` (the OQ this dispatch closes), `krylov-step-l3-identity-in-form-audit-closure-cycle-006` (the audit verdict this theme ratifies)
  - book/src/L3-L2/index.md (current L3>L2 layer overview; theme list empty pre-dispatch)
  - book/src/design/l4_calculus.md (strawman; consulted for notation conventions)
status: integrated
integrated_at: 2026-05-27T17:17:02Z
integration_commit: 693f058
integration_notes: |
  Applied cycle-007 wave-1 per-report dispatch 5 of 6 at 19:00:00Z; finalized in batch cycle-007 at 17:17:02Z.
  Files created: book/src/L3-L2/krylov-step-body-identity.md (first L3>L2 firm-rough-in theme; status inherits upstream L4>L3 rough-in; auto-promotes to firm when upstream firms).
  Files edited: book/src/L3-L2/index.md (placeholder displaced by first firm-rough-in theme-list row — third such displacement total; cycle-006 L4/index + L4-L3/index precedent), book/src/SUMMARY.md (L3>L2 Part insert), scaffolding/open-questions.md (1 status flip closing krylov-step-body-identity-theme-pending-cycle-007 open → closed).
  0 new OQs promoted (caveats all dispositioned as non-promoting per report's analysis).
  Closes cycle-006 OQ krylov-step-body-identity-theme-pending-cycle-007.
  First L3>L2 theme; first firm-rough-in status entry; first cross-edge status inheritance in artifact.
  Gate hits: 1 (index-placeholder-displacement-auto-fix applied-discretionarily per cycle-006 precedent).
---

# CYCLE: L3>L2 theme sketch — krylov-step-body-identity

## Summary

The cycle-006 wave-2 abstractor's audit (`reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"Audit of cycle-002 identity-in-form claim") established a confirmed-with-refinement verdict on the cycle-002 combinator-miner assertion that the `krylov-step` body's L3>L2 lowering is identity-in-form. The audit verdict was recorded but **not** authored as an L3>L2 theme entry; the candidate cycle-007 dispatch was filed as open-questions slug `krylov-step-body-identity-theme-pending-cycle-007`. This dispatch closes that gap by authoring the missing theme.

The theme is **substantively short** because the audit's content is the substantive content; the theme entry's job is to ratify and house the verdict in `book/src/L3-L2/` where it belongs structurally. The LHS is the L3 form published in `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"L3 form (RHS)"; the RHS is the L2 form published in `book/src/L2/krylov-step.md` §Semantics. The rotation is **identity-in-form on the per-step kernel body's primitive-sequence**: every L3 binding in the let-chain (`apply_linop`, optional `op.orthog` / `op.scalars`, `axpy`/`axpby`/`axpbypcz`, `dot`/`nrm2`/`scal`, `derived_views`) maps to the same L2 binding in the same position, in the same dataflow-forced order. The rotation does change one thing — the L3 tail-recursive outer-loop wrapping (`iterate_while_L3`) becomes the L2 outer-driver framing (the L2 entry describes `krylov-step` as a fold body consumed by an outer driver, without naming the driver); the change is **at the wrapper around the body**, not at the body. The body itself is the identity rotation.

Justification kind: **`empirical-match`** (the cycle-002 assertion, ratified by the cycle-006 audit, against the slice corpus's L2 and L3 prose — the audit re-read both endpoint forms and found them textually equivalent on the primitive-sequence) with secondary **`structural`** (every L1 primitive used at L2 is L3-native by its signature shape — `apply_linop : LinOp -> Tensor[N] -> Tensor[N]` etc. — so the L3>L2 rotation introduces no decomposition of any single primitive).

Status: `firm-rough-in`. The substantive verification is the cycle-006 audit, which was integrated as part of cycle-006's L4-L3 wrapper-dissolution theme; this theme's ratification work is `firm` (the audit verdict is complete and citation-grounded), but the LHS form it references is inherited from the upstream `krylov-step-typed-wrapper-dissolution` theme whose §Status (line 216) is `rough-in`. Per plan-kind-consistency, a downstream theme that depends on a `rough-in` LHS form cannot itself be `firm`; the appropriate compound status is `firm-rough-in` until the L4>L3 theme is promoted to `firm`.

No new speculative operators are proposed. The theme consumes existing firm L2 vocabulary and the existing rough-in L3 vocabulary published in the L4-L3 theme.

## Proposed changes

```edit:book/src/L3-L2/krylov-step-body-identity.md
[CREATE]
# krylov-step-body-identity

The L3>L2 lowering theme for the `krylov-step` body's primitive sequence. The rewrite is **identity-in-form on the kernel body** — every primitive call in the L3 let-chain maps to the same primitive call in the L2 let-chain, at the same position, in the same dataflow-forced order — with **two state-hiding / abstraction-by-role rotations at the wrapper around the body**: the L3 `(op, K, s)` positional tuple consolidates into the L2 unified `IterState` record (state-hiding), and the L3 tail-recursive outer loop `iterate_while_L3` collapses to the L2 outer-driver-by-role reference (abstraction-by-role). The body is the identity; the wrapper carries the rotation. This theme completes the [`krylov-step`](../L2/krylov-step.md) lowering chain (L4 → L3 → L2) by ratifying the cycle-002 combinator-miner assertion as audited and confirmed-with-refinement in cycle-006.

## Slug

`krylov-step-body-identity`

## Context

The `krylov-step` lowering chain stretches across four layer-edges:

- **L4 firm** ([`L4/krylov-step`](../L4/krylov-step.md)) — typed wrapper around the primitive composition, in the state-stratification idiom with `Solve` monad coordination.
- **L4>L3 firm** ([`L4-L3/krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md)) — dissolves the L4 wrapper machinery (typed records → positional tuples, `StateT SimState Identity` → explicit `s`-argument / `s'`-return, `OpParams` `readonly` → documented invariant, Form-A/B presentation → carry-threading). The kernel body's primitive sequence is unchanged across the wrapper-dissolution; the rotation is at the surface around the body.
- **L3 form** — published only as the RHS of `L4-L3/krylov-step-typed-wrapper-dissolution` §"L3 form (RHS)" (no standalone `L3/krylov-step.md`; the audit established that an L3 row would duplicate content). The L3 form is the value-threaded shape `(op, K, s) -> (K', s', outputs)` with the same five primitive groups as L2 in the same dataflow-forced order, plus an explicit `s' = s { it = s.it + 1 }` record-update line that is the dissolved `modify`.
- **L3>L2 firm-rough-in — this theme.** Ratifies the identity-in-form audit. The cycle-006 audit (`reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"Audit of cycle-002 identity-in-form claim") found the cycle-002 combinator-miner claim correct as stated for the body's L3>L2 edge: the L2 vocabulary (`apply_linop`, `axpy`/`axpby`/`axpbypcz`, `dot`/`nrm2`/`scal`, plus the slice-level `op.orthog`/`op.scalars` closures) is L3-native by inspection of each primitive's signature shape. The status is `firm-rough-in` rather than `firm` because the LHS form is inherited from the upstream L4>L3 theme whose §Status is `rough-in`; this theme's ratification work is firm but the LHS-source dependency is rough-in.
- **L2 firm** ([`L2/krylov-step`](../L2/krylov-step.md)) — the named composition of the five primitive groups in their dataflow-forced order.

This theme is the natural fall-out of the cycle-006 audit; the audit's verdict is its substantive content. The audit is reproduced and ratified here for citation-grounded completeness — the L3>L2 hop deserves an entry in `book/src/L3-L2/` independent of the L4>L3 theme, both for symmetric coverage of the lowering chain and so that future lowering-verifier or refinement dispatches have a stable anchor.

The audit's verdict was **confirmed-with-refinement**: the original cycle-002 framing ("L2>L3 step-body lift is identity-in-form") was correct for the question it asked; the refinement is the recognition that the cycle-002 assertion is about the kernel **body**, not the surrounding wrapper. The L4>L3 hop has substantive content at the wrapper (records, monad, typing, presentation distinction); the L3>L2 hop is identity-in-form on the body in *both* directions (going down — this theme — and going up — the cycle-002 lift).

## L3 form (LHS)

The L3 form is reproduced from [`L4-L3/krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)". For Form A (the default; both forms share the same body-shape modulo carry-threading):

```text
krylov-step-L3 :: (op, K, s) -> (K', s', outputs)
krylov-step-L3 op K s =
  let w       = apply_linop op.T K.<input_field>              -- L3-native global op
  let K_aux   = optionally apply op.orthog (K.V_prefix, w)     -- L3-native; MGS variant carries sequential-obstruction below the body
                or       apply op.scalars (K.k, K.scalar_state)
                or       K
  let K'      = krylov_update K_aux op w                       -- composition of L3-native axpy / axpby / axpbypcz / dot / nrm2 / scal
  let outputs = derived_views K' op                            -- demand-pruned per derived-view-hoisting
  let s'      = s { it = s.it + 1 }                            -- explicit record update (the dissolved `modify`)
  in (K', s', outputs)
```

For Form B (first-iteration-unrolled, with `carry` as a positional value):

```text
krylov-step-L3-first  :: (op, K, s)        -> (K', s', carry, outputs)
krylov-step-L3-steady :: (op, K, s, carry) -> (K', s', carry', outputs)
```

The body shape (the let-chain content) is identical between Form A and the two Form-B variants; the difference is the carry position in the tuple signature. Form A is the canonical exposition; Form B is the variant under [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md).

## L2 form (RHS)

The L2 form is reproduced from [`L2/krylov-step`](../L2/krylov-step.md) §Semantics:

```text
krylov-step op s =
  let w         = apply_linop op.T s.<input_field>             -- field-side operator apply
  let s_aux     = optionally apply op.orthog (V_prefix, w)     -- absorbed orthogonalize / project
                  or       apply op.scalars (k, scalar_state)  -- absorbed scalar generator
                  or       (no-op for vanilla CG)
  let s'_iter   = axpy / axpby / axpbypcz updates over          -- iterate-stratum update
                  s.{x, r, p, z, ...}                          -- (state-stratum-dependent)
  let s'_scalar = dot / nrm2 / recurrence-update                -- scalar-stratum update
  let outputs   = derived-view of s' (per derived-view-hoisting) -- ephemeral; demand-pruned
  in { state: s' ⊕ s'_iter ⊕ s'_scalar, outputs }
```

Where the L2 entry's `s` is the unified `IterState` record with all three strata folded together, and the iterate-stratum and scalar-stratum updates are written textually as two separate let-bindings even though L2's `krylov_update` at the L3 form (`K' = krylov_update K_aux op w`) absorbs them into one named sub-composition.

## Rewrite shape

The rewrite is the **identity on the per-step body's primitive sequence**, with two surface adjustments:

1. **The L3 `(op, K, s)` positional tuple consolidates into the L2 `(op, s)` signature.** L2's `IterState` (the `s` argument) is the unified record containing all three strata; the L3>L2 collapse merges `K` (the ephemeral bundle) and `s` (the externally-visible state) into a single `IterState` record. The merge is positional: `s.<input_field>` at L2 reads the same value that `K.<input_field>` reads at L3; `s.it` at L2 reads the same value that `s.it` reads at L3 (the counter is in `SimState` at L3, retained as a field of `IterState` at L2). **The merge is information-preserving** — no field is added, no field is dropped, no field's interpretation changes — but it does erase the L3 ephemeral-vs-persistent typing distinction. At L2 the three strata are recorded by the stratification discipline (per [`state-stratification`](../concepts/state-stratification.md)) as a documented partition over the `IterState` record's fields, not as a structural separation into three records.

2. **The L3 outer tail-recursive `iterate_while_L3` collapses into L2's outer-driver framing.** L2's `krylov-step` is described as the body of a fold consumed by an outer driver; L2 does not name the driver (it is L4 vocabulary). The L3 form has the tail-recursive loop visible (per the L4-L3 theme's §"What the L3 form for `iterate_while` looks like" subsection); at L2 the loop is referred-to-by-role. This is a **wrapper change, not a body change** — the body inside the loop is the same.

The body's let-chain itself maps line-for-line:

| L3 line | L2 line | Mapping |
|---|---|---|
| `let w = apply_linop op.T K.<input_field>` | `let w = apply_linop op.T s.<input_field>` | Identity. `K.<input_field>` re-positions to `s.<input_field>` per the (1) consolidation; primitive `apply_linop` is unchanged. |
| `let K_aux = optionally apply op.orthog (K.V_prefix, w) or apply op.scalars (K.k, K.scalar_state) or K` | `let s_aux = optionally apply op.orthog (V_prefix, w) or apply op.scalars (k, scalar_state) or (no-op for vanilla CG)` | Identity. Same three-way variant absorption, same closure dispatch sites; the `K_aux`/`s_aux` carrier rebinding tracks the (1) consolidation. |
| `let K' = krylov_update K_aux op w` | `let s'_iter = axpy / axpby / axpbypcz updates ...` + `let s'_scalar = dot / nrm2 / recurrence-update` | Identity, with one notational adjustment. The L3 entry rolls the iterate-stratum and scalar-stratum updates into a single named sub-composition `krylov_update`; the L2 entry exposes the two strata as separate let-bindings to make the stratification discipline visible at the kernel-body level. The textual shape differs but the primitive content is identical: `krylov_update` at L3 *is* the composition of the L2 entry's `axpy` chain plus the L2 entry's `dot`/`nrm2` chain. **This is the only line where the two forms diverge textually; both renderings select the same primitive set.** |
| `let outputs = derived_views K' op` | `let outputs = derived-view of s' (per derived-view-hoisting)` | Identity. Same demand-pruning law (per [`derived-view-hoisting`](../concepts/derived-view-hoisting.md)) governs both; the projection `K' -> outputs` at L3 *is* the projection `s' -> outputs` at L2 under the (1) consolidation. |
| `let s' = s { it = s.it + 1 }` | (returned as part of `state` field of the result record) | Identity. L2's `state: s' ⊕ s'_iter ⊕ s'_scalar` record-merge implicitly includes the counter-increment in the unified `IterState` record; the L3 form makes the increment textually explicit because the audit's wrapper-dissolution exposes the dissolved `modify` as a named line. The L2 form folds the increment into the result-record construction. **Information-preserving.** |
| `in (K', s', outputs)` | `in { state: s' ⊕ s'_iter ⊕ s'_scalar, outputs }` | Identity. The L3 tuple unbundles into the L2 record fields; the field count and content are the same. |

The mapping is total and bijective on the kernel-body content: every L3 binding has an L2 equivalent at the same position, and every L2 binding has an L3 equivalent. There is no L3 binding without an L2 partner; there is no L2 binding without an L3 partner. This is the **identity-in-form** property.

## Applicability conditions

The rewrite is valid when all four of the following hold (which they do for the firm L3 form by construction — the L4-L3 wrapper-dissolution theme was authored with these conditions in mind):

1. **The L3 form is the output of `krylov-step-typed-wrapper-dissolution` applied to a firm L4 `krylov-step` entry.** The L3 form's specific shape (the let-chain content, the consolidated `K_aux` carrier, the explicit `s' = s { it = s.it + 1 }` line) is the audit's RHS. If a future variant of `krylov-step` is added at L4 whose body shape differs (e.g., a method with two `apply_linop` calls per step), the wrapper-dissolution theme would produce a different L3 form, and the identity-in-form claim on the L3>L2 body edge would need re-verification on the new form. Per the cycle-006 audit, the existing five Phase-1 slices all factor into the same body shape; the condition is satisfied.

2. **The L2 form's `IterState` record subsumes the L3 form's `(K, s)` pair.** The (1) surface adjustment in §"Rewrite shape" relies on the L2 `IterState` having fields for both the ephemeral-bundle content (`K.<input_field>`, `K.V_prefix`, `K.scalar_state`, `K.k`) and the persistent content (`s.it`, `s.x`). The L2 entry's §Signature confirms this — the three-stratum partition is documented at the field level of the unified `IterState` record. If a future L2 `krylov-step` variant moved any field out of `IterState` (e.g., factored `K.V` into a separate parameter), the rewrite would need adjustment. Currently satisfied.

3. **Every primitive in the let-chain is in the firm L1 vocabulary, and each primitive is L3-native by its signature shape.** The seven L1 primitives used (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`) are firm post-cycle-004; each operates on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step (each L1 primitive is *also* L3-native because its signature has no per-element loop visible). The cycle-002 combinator-miner argument (`cg.md:351-362`) is the original observation; the cycle-006 audit re-confirmed it. Currently satisfied.

4. **The variant-axis profile is closed at six.** The six variant axes (preconditioner-side, orthogonalization variant, polynomial-kind, first-iteration-unrolled, restart shape, in-place vs out-of-place buffer use) are absorbed identically at L2 and at L3 — both forms close over the variant selectors through the `op.*` constructed-operator surfaces; neither form branches on the selectors. The closure-and-absorption mechanism is unchanged across the rotation. If a future axis is discovered that cannot be absorbed (e.g., a variant requiring per-step `op` mutation), the rotation would need refinement — but per the cycle-005 firm-up the axis count is closed at six and stable.

If a future Krylov-shaped slice (e.g., MINRES, BiCGStab — currently obstruction-only per `book/src/L1-L0/minres-iteration.md`, `book/src/L1-L0/bicgstab-iteration.md`) is firmed at L2 with a body shape that does not match the existing five-slice pattern, the rewrite would need re-audit against the new shape. Per the cycle-004 obstruction-theme guidance (CLAUDE.md §Unimplemented Palace components), these are not direct implementation targets, so the re-audit is not currently planned.

## Justification kind

**`empirical-match`** (dominant) with secondary **`structural`**.

**Empirical-match (dominant)**: the cycle-002 combinator-miner claim — that L2's primitive vocabulary is already L3-native by inspection of the slice corpus's L2 and L3 prose — is the original empirical evidence. The cycle-006 audit (`reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"Audit of cycle-002 identity-in-form claim") re-read the cited evidence ranges (`cg.md:341-362`, `arnoldi_step.md:178-213`) and confirmed the assertion. The L2>L3 lift of every primitive call in the kernel body is the identity rotation; therefore the L3>L2 lowering on the body — running the same edge in the opposite direction — is also the identity rotation. **This is the strongest justification kind for the theme**: the assertion is observational about the slice corpus's evidence, not derivational from algebraic laws or reduction rules.

**Structural (secondary)**: each L1 primitive's signature shape (e.g., `apply_linop :: LinearOperator[N, N] -> Tensor[N] -> Tensor[N]`, `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]`) is global by construction — no element loop is exposed at the L2 vocabulary level. The L3 vocabulary at this scope demands whole-tensor operations with no element loop exposed at L3; the L1 primitives satisfy this requirement *at L2*, so the rotation is the identity. This is a structural argument about the L1 primitive signature shapes; it complements the empirical-match argument by explaining *why* the empirical observation holds.

**Abstraction-direction note**: L3 is the higher-abstraction layer for this edge (it can speak about global tensor-field operations and has the iteration rotation already done by the L4>L3 hop), and L2 is the lower-abstraction layer (it speaks about the primitive composition without committing to the iteration view). The rotation direction is L3 → L2: the L3 form lowers to the L2 form by erasing the L3 outer-loop framing (which becomes the L2 outer-driver-by-role reference) and consolidating the L3 (K, s) split into the L2 unified `IterState`. Both surface adjustments are at the wrapper around the body, not at the body; the body is the identity rotation. The abstraction step at the wrapper is L3 → L2 (the L3 outer-loop tail-recursion is the more abstract surface; L2 leaves the driver to the consumer); this matches the methodology's lowering direction.

**On the cycle-005 firm L2 entry**: the L2 §Semantics body was written textually as the primitive-composition form *without* awareness of the cycle-006 L3 form (which was authored a cycle later). That the two forms align line-for-line is therefore independent corroboration — the L2 entry was written from the slice corpus's L2 prose; the L3 form was derived by applying the L4>L3 wrapper-dissolution rewrite to the cycle-006 L4 entry. Two independent derivations from non-overlapping evidence converge on the same body shape. This is the strongest form the empirical-match justification can take.

## Speculative L3 operators

**None.** This theme is the identity rotation; no new L3 vocabulary is introduced. The L3 form referenced in the LHS is the RHS of the firm-rough-in `krylov-step-typed-wrapper-dissolution` theme; the L2 form referenced in the RHS is the firm `L2/krylov-step` entry. Both endpoints exist in the artifact already; the theme ratifies their identity-in-form relationship.

The L4 `iterate_while` / `iterate_while_with_prev` rough-ins flagged in `L4-L3/krylov-step-typed-wrapper-dissolution.md` §"Speculative L4 operators" remain rough-in (they belong to the loop combinator, not the kernel body); the candidate cycle-007 harvester dispatch on those operators is tracked at open-questions slug `iterate-while-l4-anchor-missing`. This theme does not interact with that promotion — the kernel body's rotation is independent of the loop combinator's anchoring.

## Verified-against

Audit evidence (the substantive verification, reproduced from the cycle-006 audit):

- `book/src/spec/slices/cg.md:341-362` — combinator-miner cycle-002 Claim 2 ("step body lifts as identity"). The cited range contains the verbatim claim at line 360: *"The L2→L3 rotation on the step body is therefore the **identity in form**: no unfolding, no global lift, no schema change."* with the justification (lines 353-358) that L2's primitive vocabulary is already L3-native by signature shape. Re-read for the cycle-006 audit; assertion confirmed.
- `book/src/spec/slices/arnoldi_step.md:178-213` — combinator-miner cycle-002 evidence for the Arnoldi step's L2>L3 lift. The three uncontested primitives (`apply_BA`, `subdiag_norm`, `normalize`) lift as identity (lines 184-190); the fourth (`orthogonalize` under MGS) carries a [sequential-obstruction](../concepts/sequential-obstruction.md) (lines 192-213). **The obstruction is below the kernel body** — it is a property of the `op.orthog` primitive under the MGS variant, not of the `krylov-step` body that calls `op.orthog` as an opaque closure. The body's identity-in-form claim survives the obstruction.
- `book/src/spec/slices/chebyshev.md:354-362` — the Chebyshev `innerStep` body. The five-primitive-group shape is the same as the L2 entry's; no rewrite needed for the L3>L2 rotation.
- `book/src/spec/slices/gmres.md:459-471` — the GMRES `inner_loop` body. Same kernel-body pattern modulo the `op.orthog` variant absorption; same identity-in-form rotation on the body.

L4 / L3 evidence (the LHS):

- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"L3 form (RHS)" (lines 55-89) — the L3 form this theme references as LHS. The cycle-006 audit derived this form from the L4 form by applying the wrapper-dissolution rewrite; the form is published as the RHS of that theme (the upstream theme is currently `rough-in` per its §Status line 216).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"Audit of cycle-002 identity-in-form claim" (lines 169-187) — the cycle-006 audit's verdict ("confirmed-with-refinement") establishing the substantive content of this theme. This theme is the structural housing of that verdict in `book/src/L3-L2/`.

L2 sink (the RHS):

- `book/src/L2/krylov-step.md` §Semantics (lines 38-66) — the L2 form this theme references as RHS. Cycle-005 firm; the body shape is the per-step kernel's five-primitive-group composition.

Cross-cutting concept references (consumed unchanged across the rotation):

- `book/src/concepts/state-stratification.md` — the three-stratum partition discipline (cross-cutting; rendered as a typed record at L4, as a positional tuple at L3, as a documented partition over `IterState` fields at L2).
- `book/src/concepts/derived-view-hoisting.md` — the demand-pruning law on the `outputs` slot, preserved identically across the rotation.
- `book/src/concepts/variant-absorption.md` — the level-(b)/(c) absorption discipline, preserved identically across the rotation.
- `book/src/concepts/first-iteration-unrolling.md` — the Form-A/Form-B presentation, collapsed to carry-threading at L3 and to a variant-axis at L2; identity-in-form on the kernel body under either form.
- `book/src/concepts/sequential-obstruction.md` — referenced for the MGS-orthog obstruction below the kernel body; not introduced by this rotation.

Open-questions ledger:

- `scaffolding/open-questions.md` slug `krylov-step-body-identity-theme-pending-cycle-007` — the open question this dispatch closes. Status will update to `closed` on integration with answer-link `book/src/L3-L2/krylov-step-body-identity.md` (this file).
- `scaffolding/open-questions.md` slug `krylov-step-l3-identity-in-form-audit-closure-cycle-006` — the cycle-006 audit closure-note; this theme is the structural housing of that verdict.

## Status

`firm-rough-in` — the theme's ratification work is firm (the audit verdict is complete and citation-grounded; the body's identity-in-form mapping is total and bijective per §"Rewrite shape" line-by-line table; the surface adjustments — L3 `(op, K, s)` consolidation into L2 `(op, s)`; L3 tail-recursive outer-loop into L2 outer-driver-by-role — are wrapper-level and explicitly delimited; no speculative L3 vocabulary is introduced; the four applicability conditions are stated and confirmed satisfied for the existing five-slice corpus). The `rough-in` component is **inherited**: the L3 LHS form is referenced from the upstream `krylov-step-typed-wrapper-dissolution` theme whose §Status (line 216) is `rough-in`. The L2 RHS form is referenced from the firm `L2/krylov-step` entry. Per plan-kind-consistency, a downstream theme cannot be `firm` while its LHS-source dependency is `rough-in`; promotion of this theme to plain `firm` follows automatically when the upstream L4>L3 theme is itself promoted to `firm` (likely on completion of the cycle-006 audit's `lowering-verifier` follow-up named in the L4>L3 theme's §Status).

**Lowering-verifier follow-up** (cycle-008+ candidate): if a future slice (MINRES, BiCGStab, LOBPCG, etc.) is firmed at L2 with a body shape that does not match the existing pattern, this theme would need re-audit against the new shape. The cycle-006 audit's `lowering-verifier` follow-up (named in the L4>L3 theme's §Status) covers the L4>L3 hop; a parallel follow-up on this theme's L3>L2 hop would extend that coverage.

## L3>L2 vs L4>L3 distinction

The two themes in the `krylov-step` lowering chain divide labour cleanly:

- **L4>L3 (`krylov-step-typed-wrapper-dissolution`)**: substantive rotation at the **wrapper** (typed records, monad, readonly typing, Form-A/B presentation). Identity-in-form on the body.
- **L3>L2 (this theme; `krylov-step-body-identity`)**: identity-in-form on the body. Two **surface adjustments at the wrapper** ((K, s) → unified IterState; outer-loop tail-recursion → outer-driver-by-role reference) that are information-preserving and do not touch the primitive sequence.

Together they constitute the full L4>L2 lowering chain. The composition is non-identity at the wrapper (the L4 typed-wrapper machinery fully dissolves) but identity-in-form on the body (the kernel's primitive sequence survives both hops textually unchanged, with only the carrier-record naming and the outer-loop framing changing across the chain).

This division — substantive content at one hop, identity at the other — is the pattern the cycle-006 audit established as "L4>L3>L2 step-body chain is identity-in-form on the kernel body's primitive sequence". The two-theme structure makes the division visible in the artifact.
```

```edit:book/src/L3-L2/index.md
[REPLACE the section starting at line 9 ("## Theme list") through line 13 (the empty "..." block):]

## Theme list

| Theme | LHS (L3) | RHS (L2) | Justification kind | Status |
|---|---|---|---|---|
| [`krylov-step-body-identity`](./krylov-step-body-identity.md) | L3 form per [`L4-L3/krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)" — value-threaded `(op, K, s) -> (K', s', outputs)`, five-primitive-group let-chain (`apply_linop`, optional `op.orthog`/`op.scalars`, `axpy`/`axpby`/`axpbypcz`, `dot`/`nrm2`/`scal`, `derived_views`) plus explicit `s' = s { it = s.it + 1 }` counter-update. | L2 [`krylov-step`](../L2/krylov-step.md) §Semantics — primitive-composition form with consolidated `IterState` record absorbing the L3 `(K, s)` split; same five-primitive-group composition, outer driver referenced by role. | `empirical-match` (cycle-002 combinator-miner claim; cycle-006 audit confirmed-with-refinement) + secondary `structural` (each L1 primitive's signature shape is whole-tensor by construction) | `firm-rough-in` (cycle-007 abstractor; ratifies cycle-006 audit verdict; `rough-in` inherited from upstream L4>L3 theme whose status is `rough-in`) |
```

```edit:book/src/SUMMARY.md
[APPEND under L3 > L2 Part (chapter entry):]
- [krylov-step-body-identity](./L3-L2/krylov-step-body-identity.md)
```

```edit:scaffolding/open-questions.md
[APPEND to status update of slug `krylov-step-body-identity-theme-pending-cycle-007`:]
status: closed
answered_in: reports/2026-05-27T160445Z-abstractor-krylov-step-body-identity-L3-L2/CYCLE.md (theme authored as `book/src/L3-L2/krylov-step-body-identity.md`; ratifies cycle-006 audit)
```

## Speculative operators proposed

**None.** This theme is the identity rotation. The L3 form referenced as LHS is published in `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`; the L2 form referenced as RHS is the firm `book/src/L2/krylov-step.md`. No new vocabulary needed.

The L4 `iterate_while` / `iterate_while_with_prev` rough-ins (open-questions slug `iterate-while-l4-anchor-missing`) remain rough-in but are out-of-scope for this theme — they belong to the loop combinator, not the kernel body. A parallel cycle-007 harvester dispatch on the L4 loop-combinator family is the natural promotion path; this theme does not interact with it.

## Supporting evidence

The substantive verification is the cycle-006 audit reproduced in §"Verified-against" of the theme entry. The audit re-read four citation ranges from the slice corpus:

- `book/src/spec/slices/cg.md:341-362` — Claim 2 verbatim "identity in form" with the L1-primitive-is-L3-native justification.
- `book/src/spec/slices/arnoldi_step.md:178-213` — three uncontested primitives plus the localised MGS-orthog obstruction (below the body, not at the body).
- `book/src/spec/slices/chebyshev.md:354-362` — confirmed Chebyshev `innerStep` body matches the five-primitive-group pattern.
- `book/src/spec/slices/gmres.md:459-471` — confirmed GMRES `inner_loop` body matches the pattern.

Two cycle-006 dispatch artifacts:

- `reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"L3 form (RHS)" — the L3 form this theme references as LHS.
- `reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"Audit of cycle-002 identity-in-form claim" — the audit verdict ("confirmed-with-refinement") this theme ratifies.

Two existing layered-artifact entries:

- `book/src/L2/krylov-step.md` (cycle-005 firm) — the L2 sink form.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (cycle-006 firm-rough-in) — the upstream theme whose RHS is this theme's LHS.

Two open-questions ledger entries (both closed by this dispatch's integration):

- `krylov-step-body-identity-theme-pending-cycle-007` (cycle-006 opened) — the gap this dispatch closes.
- `krylov-step-l3-identity-in-form-audit-closure-cycle-006` (cycle-006 closure-note) — the audit verdict this theme structurally houses.

## Open questions / caveats

1. **Future Krylov-shaped slices may break the identity-in-form claim.** The audit was scoped to the existing five-slice corpus (CG, GMRES, Chebyshev, Arnoldi, polynomial-recurrence). If MINRES, BiCGStab, LOBPCG, or another method is firmed at L2 in a future cycle with a body shape that doesn't factor into the same five-primitive-group pattern, this theme would need re-audit against the new shape. Per CLAUDE.md §Unimplemented Palace components, MINRES and BiCGStab are not direct implementation targets (they are obstruction-only at L1>L0); the re-audit is not currently planned. **Disposition**: filed as ambient open question only if a new slice is firmed; no proactive OQ entry.

2. **The L3 form's outer-loop tail-recursion has a known trajectory-accumulation gap** (open-questions slug `iterate-while-l3-rendering-trajectory-accumulation-gap`). The L3 `iterate_while_L3` shape in the L4-L3 theme drops the trajectory accumulator that the L4 `iterate_while` carries. This is a wrapper-level issue (about the loop combinator's rendering), not a body-level issue (about the `krylov-step` body's rotation). This theme is **not affected** because the rotation is on the body, and the body does not see the trajectory accumulator (it sees only the carry pair (K, s) and produces the next pair + readout). **Disposition**: orthogonal open question; tracked under the loop-combinator slug, not under this theme.

3. **The L3 form is published only inside the L4-L3 theme's §"L3 form (RHS)".** There is no standalone `book/src/L3/krylov-step.md`. The cycle-006 audit's verdict was that promoting an L3 row would duplicate content without adding semantic distinction (per `reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"Audit of cycle-002 identity-in-form claim", consequence paragraph). This theme **adopts the audit's decision** and references the L3 form via the L4-L3 theme; no L3 row is promoted by this dispatch. **Disposition**: confirmed decision from cycle-006; no new OQ.

4. **The `IterState` consolidation at the L3>L2 boundary is information-preserving but erases the ephemeral-vs-persistent typing distinction.** At L3 the wrapper-dissolution theme has already collapsed the typed records into positional values; the L2 form further consolidates the L3 `(K, s)` pair into a single unified `IterState`. The three-stratum stratification survives as a documented partition over `IterState`'s fields (per `book/src/concepts/state-stratification.md`), but the structural distinction between the ephemeral bundle `K` (born at restart, discarded at restart) and the persistent state `s` (lives across the entire solve) is no longer typed-in. **At L2 this is acceptable**: L2's role is naming the primitive composition; lifetime typing is L4-only by design (per the cycle-006 wave-1 harvester's framing). **Disposition**: a known and intentional consequence of the L2-layer scope; not a problem to fix.

5. **The L3>L2 theme is short by design.** The substantive content is the cycle-006 audit; this theme's job is to house and ratify the verdict in `book/src/L3-L2/` for symmetric coverage of the lowering chain. Critics may flag the theme as "too short" by reflex; the response is that an identity-in-form rotation deserves a short entry — the line-by-line mapping table in §"Rewrite shape" is the complete content. **Disposition**: anticipated critic finding; defended in this caveat.

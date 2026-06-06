# krylov-step-body-identity

The L3>L2 lowering theme for the `krylov-step` body's primitive sequence. The rewrite is **identity-in-form on the kernel body** — every primitive call in the L3 let-chain maps to the same primitive call in the L2 let-chain, at the same position, in the same dataflow-forced order — with **two state-hiding / abstraction-by-role rotations at the wrapper around the body**: the L3 `(op, K, s)` positional tuple consolidates into the L2 unified `IterState` record (state-hiding), and the L3 tail-recursive outer loop `iterate_while_L3` collapses to the L2 outer-driver-by-role reference (abstraction-by-role). The body is the identity; the wrapper carries the rotation. This theme completes the [`krylov-step`](../L2/krylov-step.md) lowering chain (L4 → L3 → L2) by ratifying the cycle-002 combinator-miner assertion as audited and confirmed-with-refinement in cycle-006.

## Slug

`krylov-step-body-identity`

## Context

The `krylov-step` lowering chain stretches across four layer-edges:

- **L4 firm** ([`L4/krylov-step`](../L4/krylov-step.md)) — typed wrapper around the primitive composition, in the state-stratification idiom with `Solve` monad coordination.
- **L4>L3 firm** ([`L4-L3/krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md)) — dissolves the L4 wrapper machinery (typed records → positional tuples, `StateT SimState Identity` → explicit `s`-argument / `s'`-return, `OpParams` `readonly` → documented invariant, Form-A/B presentation → carry-threading). The kernel body's primitive sequence is unchanged across the wrapper-dissolution; the rotation is at the surface around the body.
- **L3 form** ([`L3/krylov-step`](../L3/krylov-step.md), firm cycle-010) — value-threaded shape `(op, K, s) -> (K', s', outputs)` with the same five primitive groups as L2 in the same dataflow-forced order, plus an explicit `s' = s { it = s.it + 1 }` record-update line that is the dissolved `modify`. The L3 entry was previously published only as the RHS of `L4-L3/krylov-step-typed-wrapper-dissolution` §"L3 form (RHS)" — the cycle-006 audit established that an L3 row would duplicate content. **Cycle-010 backfill**: per the CLAUDE.md §Methodology invariants bullet **Identity-lowerings still require both L levels** (codified cycle-009 meta-phase), the L3 entry was authored as a layer-coherence anchor — the body is value-thread-isomorphic to the L4 body, but each layer is coherent within itself and the L3 reader must find `krylov-step` defined in L3 vocabulary at L3. The L3 entry is the LHS of this theme; the rewrite mapping in §"Rewrite shape" is unchanged.
- **L3>L2 firm — this theme.** Ratifies the identity-in-form audit. The cycle-006 audit (`reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"Audit of cycle-002 identity-in-form claim") found the cycle-002 combinator-miner claim correct as stated for the body's L3>L2 edge: the L2 vocabulary (`apply_linop`, `axpy`/`axpby`/`axpbypcz`, `dot`/`nrm2`/`scal`, plus the slice-level `op.orthog`/`op.scalars` closures) is L3-native by inspection of each primitive's signature shape. The theme was authored cycle-007 wave-1 at status `firm-rough-in` (inheriting the upstream L4>L3 theme's then-`rough-in` qualifier under the plan-kind-consistency convention) and promoted to plain `firm` in cycle-009 via status-inheritance after the upstream theme was itself promoted firm in cycle-008.
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

3. **Every primitive in the let-chain is in the firm L1 vocabulary, and each primitive is L3-native by its signature shape.** The seven L1 primitives used (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`) are firm post-cycle-004; each operates on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step (each L1 primitive is *also* L3-native because its signature has no per-element loop visible). The cycle-002 combinator-miner argument (preserved verbatim in this theme's §Verified-against bullet 1 — the terminal firm home; original pre-reduction slice range `cg.md:351-362`, lifted here per the cycle-009 corpus reduction) is the original observation; the cycle-006 audit re-confirmed it. Currently satisfied.

4. **The variant-axis profile is closed at six.** The six variant axes (preconditioner-side, orthogonalization variant, polynomial-kind, first-iteration-unrolled, restart shape, in-place vs out-of-place buffer use) are absorbed identically at L2 and at L3 — both forms close over the variant selectors through the `op.*` constructed-operator surfaces; neither form branches on the selectors. The closure-and-absorption mechanism is unchanged across the rotation. If a future axis is discovered that cannot be absorbed (e.g., a variant requiring per-step `op` mutation), the rotation would need refinement — but per the cycle-005 firm-up the axis count is closed at six and stable.

If a future Krylov-shaped slice (e.g., MINRES, BiCGStab — currently obstruction-only per `book/src/L1-L0/minres-iteration.md`, `book/src/L1-L0/bicgstab-iteration.md`) is firmed at L2 with a body shape that does not match the existing five-slice pattern, the rewrite would need re-audit against the new shape. Per the cycle-004 obstruction-theme guidance (CLAUDE.md §Unimplemented Palace components), these are not direct implementation targets, so the re-audit is not currently planned.

## Justification kind

**`empirical-match`** (dominant) with secondary **`structural`**.

**Empirical-match (dominant)**: the cycle-002 combinator-miner claim — that L2's primitive vocabulary is already L3-native by inspection of the slice corpus's L2 and L3 prose — is the original empirical evidence. The cycle-006 audit (`reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"Audit of cycle-002 identity-in-form claim") re-read the cited evidence ranges (the CG body-identity claim, now preserved verbatim in this theme's §Verified-against bullet 1 — the terminal firm home; original pre-reduction slice range `cg.md:341-362`, lifted there per the cycle-009 corpus reduction — and the live anchor `arnoldi_step.md:178-213`) and confirmed the assertion. The L2>L3 lift of every primitive call in the kernel body is the identity rotation; therefore the L3>L2 lowering on the body — running the same edge in the opposite direction — is also the identity rotation. **This is the strongest justification kind for the theme**: the assertion is observational about the slice corpus's evidence, not derivational from algebraic laws or reduction rules.

**Structural (secondary)**: each primitive's calculus-layer signature shape (e.g., `apply_linop :: LinOp[(S: ...), (S: ...)] -> Tensor[(S: ...)] -> Tensor[S]`, `axpy :: Scalar -> Tensor[(S: ...)] -> Tensor[S] -> Tensor[S]`) is global by construction — congruent over one shape group `S` of unknown rank, with no element loop exposed at the L2 vocabulary level (named shape groups + two-group operator form per [`l4_calculus`](../design/l4_calculus.md) §1.2.1–§1.2.2; at the concrete L1/L0 flat-call these read as rank-1 `Tensor[N]` / `LinearOperator[N, N]`). The L3 vocabulary at this scope demands whole-tensor operations with no element loop exposed at L3; the L1 primitives satisfy this requirement *at L2*, so the rotation is the identity. This is a structural argument about the L1 primitive signature shapes; it complements the empirical-match argument by explaining *why* the empirical observation holds.

**Abstraction-direction note**: L3 is the higher-abstraction layer for this edge (it can speak about global tensor-field operations and has the iteration rotation already done by the L4>L3 hop), and L2 is the lower-abstraction layer (it speaks about the primitive composition without committing to the iteration view). The rotation direction is L3 → L2: the L3 form lowers to the L2 form by erasing the L3 outer-loop framing (which becomes the L2 outer-driver-by-role reference) and consolidating the L3 (K, s) split into the L2 unified `IterState`. Both surface adjustments are at the wrapper around the body, not at the body; the body is the identity rotation. The abstraction step at the wrapper is L3 → L2 (the L3 outer-loop tail-recursion is the more abstract surface; L2 leaves the driver to the consumer); this matches the methodology's lowering direction.

**On the cycle-005 firm L2 entry**: the L2 §Semantics body was written textually as the primitive-composition form *without* awareness of the cycle-006 L3 form (which was authored a cycle later). That the two forms align line-for-line is therefore independent corroboration — the L2 entry was written from the slice corpus's L2 prose; the L3 form was derived by applying the L4>L3 wrapper-dissolution rewrite to the cycle-006 L4 entry. Two independent derivations from non-overlapping evidence converge on the same body shape. This is the strongest form the empirical-match justification can take.

## Speculative L3 operators

**None.** This theme is the identity rotation; no new L3 vocabulary is introduced. The L3 form referenced in the LHS is the RHS of the firm `krylov-step-typed-wrapper-dissolution` theme (firmed cycle-008); the L2 form referenced in the RHS is the firm `L2/krylov-step` entry. Both endpoints exist in the artifact already; the theme ratifies their identity-in-form relationship.

The L4 `iterate_while` / `iterate_while_with_prev` operators flagged as rough-ins in the upstream `L4-L3/krylov-step-typed-wrapper-dissolution.md` §"Speculative L4 operators" were firmed by the cycle-007 wave-1 harvester (`reports/2026-05-27T160550Z-harvester-iterate-while-family-L4/`) as `book/src/L4/iterate-while.md` and `book/src/L4/iterate-while-with-prev.md` (closing OQ `iterate-while-l4-anchor-missing`). They belong to the loop combinator, not the kernel body; this theme does not interact with them — the kernel body's rotation is independent of the loop combinator's anchoring.

## Verified-against

Audit evidence (the substantive verification, reproduced from the cycle-006 audit):

- **The combinator-miner cycle-002 Claim 2 ("step body lifts as identity") — terminal firm home: THIS entry.** The claim reads verbatim: *"The L2→L3 rotation on the step body is therefore the **identity in form**: no unfolding, no global lift, no schema change."* with the justification that L2's primitive vocabulary is already L3-native by signature shape. This verbatim quote was lifted into this §Verified-against bullet per the cycle-009 corpus reduction and is preserved here as the **terminal firm home** of the CG body-identity evidence — the upstream `L4-L3/krylov-step-typed-wrapper-dissolution.md` §"Audit of cycle-002 identity-in-form claim" and the firm `L3/krylov-step.md` §dep-map both point at this bullet as the lifted-in anchor. (The `cg.md` slice from which it was originally lifted was deleted cycle-099 once all its material reached firm homes; this bullet now carries the quote in full, so nothing is lost.) Re-read for the cycle-006 audit; assertion confirmed.
- Arnoldi step L2>L3 lift (combinator-miner cycle-002 evidence; firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop). The three uncontested primitives (`apply_BA`, `subdiag_norm`, `normalize`) lift as identity; the fourth (`orthogonalize` under MGS) carries a [sequential-obstruction](../concepts/sequential-obstruction.md) (firm at its §"MGS as sequential-obstruction"). **The obstruction is below the kernel body** — it is a property of the `op.orthog` primitive under the MGS variant, not of the `krylov-step` body that calls `op.orthog` as an opaque closure. The body's identity-in-form claim survives the obstruction.
- `book/src/L4/chebyshev.md` §Semantics `innerStep` — the Chebyshev `innerStep` body (firm cycle-015, absorbing the former `chebyshev.md:354-362` slice §L4). The five-primitive-group shape is the same as the L2 entry's; no rewrite needed for the L3>L2 rotation.
- GMRES `inner_loop` body (firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C, `iterative.cpp:543-705`). Same kernel-body pattern modulo the `op.orthog` variant absorption; same identity-in-form rotation on the body.

L4 / L3 evidence (the LHS):

- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"L3 form (RHS)" (lines 55-89) — the L3 form this theme references as LHS. The cycle-006 audit derived this form from the L4 form by applying the wrapper-dissolution rewrite; the form is published as the RHS of that theme. The upstream theme was promoted to `firm` in cycle-008 (per its §Status line 293, post-cycle-008 lifter dispatch `reports/2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close/CYCLE.md`); the cycle-008 patch added the §3.8 collapse-rule citation, Condition 5, and a 10-citation `verified_against:` block, closing OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`.
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

`firm` — the theme's ratification work is firm (the audit verdict is complete and citation-grounded; the body's identity-in-form mapping is total and bijective per §"Rewrite shape" line-by-line table; the surface adjustments — L3 `(op, K, s)` consolidation into L2 `(op, s)`; L3 tail-recursive outer-loop into L2 outer-driver-by-role — are wrapper-level and explicitly delimited; no speculative L3 vocabulary is introduced; the four applicability conditions are stated and confirmed satisfied for the existing five-slice corpus). Both layer endpoints are themselves firm: the L3 LHS form is referenced from the upstream `krylov-step-typed-wrapper-dissolution` theme, promoted to `firm` in cycle-008; the L2 RHS form is referenced from the firm `L2/krylov-step` entry (cycle-005). The earlier `firm-rough-in` qualifier (cycle-007 wave-1) inherited the upstream's `rough-in` status under the plan-kind-consistency convention.

**Promoted to `firm` cycle-009 via status-inheritance** after upstream L4>L3 `krylov-step-typed-wrapper-dissolution` was promoted `firm` in cycle-008 (`reports/2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close/CYCLE.md`). That cycle-008 lifter dispatch applied the cycle-007 wave-2 lowering-verifier audit's three substantive changes — §3.8 collapse-rule citation at §"What the L3 form for `iterate_while` looks like", new Condition 5 in §"Applicability conditions" naming the consumer-demand precondition, trailing `verified_against:` block carrying the 10-citation audit evidence base — closing OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` as `answered` (cycle-008). Per plan-kind-consistency, with the upstream now firm and the L2 sink firm, the body-identity theme's downstream qualifier no longer applies; this dispatch is the mechanical re-anchor.

**Lowering-verifier follow-up** (cycle-009+ candidate): if a future slice (MINRES, BiCGStab, LOBPCG, etc.) is firmed at L2 with a body shape that does not match the existing pattern, this theme would need re-audit against the new shape. The cycle-007 wave-2 lowering-verifier covered the L4>L3 hop's trajectory-collapse question; a parallel verifier on this theme's L3>L2 hop would extend that coverage to per-slice body-shape verification.

## L3>L2 vs L4>L3 distinction

The two themes in the `krylov-step` lowering chain divide labour cleanly:

- **L4>L3 (`krylov-step-typed-wrapper-dissolution`)**: substantive rotation at the **wrapper** (typed records, monad, readonly typing, Form-A/B presentation). Identity-in-form on the body.
- **L3>L2 (this theme; `krylov-step-body-identity`)**: identity-in-form on the body. Two **surface adjustments at the wrapper** ((K, s) → unified IterState; outer-loop tail-recursion → outer-driver-by-role reference) that are information-preserving and do not touch the primitive sequence.

Together they constitute the full L4>L2 lowering chain. The composition is non-identity at the wrapper (the L4 typed-wrapper machinery fully dissolves) but identity-in-form on the body (the kernel's primitive sequence survives both hops textually unchanged, with only the carrier-record naming and the outer-loop framing changing across the chain).

This division — substantive content at one hop, identity at the other — is the pattern the cycle-006 audit established as "L4>L3>L2 step-body chain is identity-in-form on the kernel body's primitive sequence". The two-theme structure makes the division visible in the artifact.

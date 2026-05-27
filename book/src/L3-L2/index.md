# L3 > L2 — Lowering layer

The transformation from L3 (global tensor-field operations) to L2 (algebraic decompositions). Batched by **themes**.

## Context

L3 forms are whole-tensor; L2 forms are compositions of base algebraic primitives. The lowering unfolds the field-level operation into its primitive-composition form. The reverse direction — L2 → L3 — is the **iteration rotation**, and the lowering captures it formally here.

## Theme list

| Theme | LHS (L3) | RHS (L2) | Justification kind | Status |
|---|---|---|---|---|
| [`krylov-step-body-identity`](./krylov-step-body-identity.md) | L3 form per [`L4-L3/krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)" — value-threaded `(op, K, s) -> (K', s', outputs)`, five-primitive-group let-chain (`apply_linop`, optional `op.orthog`/`op.scalars`, `axpy`/`axpby`/`axpbypcz`, `dot`/`nrm2`/`scal`, `derived_views`) plus explicit `s' = s { it = s.it + 1 }` counter-update. | L2 [`krylov-step`](../L2/krylov-step.md) §Semantics — primitive-composition form with consolidated `IterState` record absorbing the L3 `(K, s)` split; same five-primitive-group composition, outer driver referenced by role. | `empirical-match` (cycle-002 combinator-miner claim; cycle-006 audit confirmed-with-refinement) + secondary `structural` (each L1 primitive's signature shape is whole-tensor by construction) | `firm-rough-in` (cycle-007 abstractor; ratifies cycle-006 audit verdict; `rough-in` inherited from upstream L4>L3 theme whose status is `rough-in`) |

## Working Notes

- Negative-result entries (L3 form for which no L2 decomposition is meaningful — rare, mostly definitional) appear here too.

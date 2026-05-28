# L4 > L3 — Lowering layer

The transformation from L4 (graph-evaluation calculus) to L3 (global tensor-field operations). Batched by **themes** — named patterns of rewriting, each justified once.

## Context

A lowering theme rewrites L4 forms of shape A into L3 forms of shape B. Themes are many-to-many: a single L4 combinator may produce many L3 fragments through its lowering; a single L3 form may be the lowered residue of multiple L4 combinator applications.

This is **not** point-wise rotation. It is a structured rewrite system with applicability conditions.

## Theme list

| Theme | LHS (L4) | RHS (L3) | Justification kind | Status |
|---|---|---|---|---|
| [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) | L4 [`krylov-step`](../L4/krylov-step.md) — typed-wrapper form with three-stratum state-stratification records, `Solve = StateT SimState Identity` monad, `OpParams` `readonly` typing, and Form-A/Form-B presentation distinction. | L3 value-threading form `(op, K, s) -> (K', s', outputs)`: `StateT` dissolves to explicit `s`-arg / `s'`-return; typed records become positional tuples; `readonly` demotes to documented invariant; Form-A/B collapses to carry-threading. Kernel body's primitive sequence is textually unchanged. | `structural` + secondary `reduction-chain` (the `modify` to record-update unfolding) | `rough-in` (cycle-006 abstractor; lowering-verifier follow-up candidate cycle-007) |
| `gmres-inner-loop-iterate-while-migration` *(rough-in; this dispatch creates the anchor file at `./gmres-inner-loop-iterate-while-migration.md`)* | L4 migrated GMRES inner-loop form: `inner_loop op conv K0 = iterate_while K0 (\K -> isNothing K.stop_reason) (\K -> ...body... ; pure { state, residual_norm, breakdown_token })` with `check_stop_into_carry` writing the witness into the carry's `stop_reason` field. | L3 tail-recursive value-threading worker `gmres_inner_loop_L3_worker op conv K s` with the `Solve` monad dissolved to explicit `s` threading, trajectory pruned to `[]` per Law 1 (consumer reads only `(K_final, K_final.stop_reason)`), and the `iterate_while` combinator dissolved per the parallel `krylov-step-typed-wrapper-dissolution` theme. | `structural` + secondary `reduction-chain` and `empirical-match` | `rough-in` (cycle-008 abstractor; depends on upstream gmres.md §L4 v0.6→v0.7 self-rotation, routed to cycle-008+ lifter on `gmres.md §L4`) |
| [`fgmres-inner-loop-iterate-while-migration`](./fgmres-inner-loop-iterate-while-migration.md) | Sister-form to the GMRES theme above, specialised for `FgmresSolver<OperType>` (`iterative.cpp:734-836`, `iterative.hpp:222-270`): `pc_side` pinned to `RIGHT` and `flexible` pinned to `true` at the constructor; unconditional `K { Z = K.Z `with` (K.j, z) }` carry-update; otherwise identical L4 form. | Sister-form to the GMRES L3 theme above, specialised for FGMRES: identical wrapper dissolution; body simplifies to the FGMRES collapsed shape (`pc_side`/`flexible` variant rows removed). Textually identical break-site at `iterative.cpp:823-828` (cycle-010 MCP-pilot audit). | `structural` + secondary `reduction-chain` and `empirical-match` | `rough-in` (cycle-011 lifter; same upstream gmres.md §L4 v0.6→v0.7 dependency as the GMRES sister) |

Each theme:
- **Slug** (e.g., `monad-bind-fusion`, `state-thread-elimination`, `combinator-inline`)
- **L4 form (LHS)**: the pattern matched
- **L3 form (RHS)**: the rewrite target
- **Applicability conditions**: when this rewrite is valid (typing, shape, effect-freedom)
- **Justification kind**: `algebraic` | `structural` | `reduction-chain` | `empirical-match` | `obstruction`
- **Verified-against**: cited L3 evidence ranges or test references

## Working Notes

- Themes are coalesced as the artifact grows; multiple narrow themes are preferred over one mega-theme.
- Negative results (L4 form has no L3 lowering for principled reasons) live here too as `obstruction`-justified entries.

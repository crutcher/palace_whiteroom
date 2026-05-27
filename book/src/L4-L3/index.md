# L4 > L3 — Lowering layer

The transformation from L4 (graph-evaluation calculus) to L3 (global tensor-field operations). Batched by **themes** — named patterns of rewriting, each justified once.

## Context

A lowering theme rewrites L4 forms of shape A into L3 forms of shape B. Themes are many-to-many: a single L4 combinator may produce many L3 fragments through its lowering; a single L3 form may be the lowered residue of multiple L4 combinator applications.

This is **not** point-wise rotation. It is a structured rewrite system with applicability conditions.

## Theme list

| Theme | LHS (L4) | RHS (L3) | Justification kind | Status |
|---|---|---|---|---|
| [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) | L4 [`krylov-step`](../L4/krylov-step.md) — typed-wrapper form with three-stratum state-stratification records, `Solve = StateT SimState Identity` monad, `OpParams` `readonly` typing, and Form-A/Form-B presentation distinction. | L3 value-threading form `(op, K, s) -> (K', s', outputs)`: `StateT` dissolves to explicit `s`-arg / `s'`-return; typed records become positional tuples; `readonly` demotes to documented invariant; Form-A/B collapses to carry-threading. Kernel body's primitive sequence is textually unchanged. | `structural` + secondary `reduction-chain` (the `modify` to record-update unfolding) | `rough-in` (cycle-006 abstractor; lowering-verifier follow-up candidate cycle-007) |

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

# inner_product

> **Status: `stub`** — claim-free placeholder materialized 2026-05-28 (CLAUDE.md §Methodology invariants "Integration may materialize implied components as stubs"). Exists so the cycle-018 rough-in dep-map row and the plan resolve to a live home. **No citations or semantic claims yet** — the next `harvester` refines it in place (`stub` → `rough-in` → `firm`).

## What this will be

The L2 inner-product fold `(Tensor[N], Tensor[N]) -> Scalar` ≡ `foldl (+) zero (zipWith kernel x y)`, with the M-weighted member `inner_product_M(x, M, y) = xᴴ M y` (plain ≡ `M = I`). It is the **conjugation-convention sibling** of [`linear_combination`](./linear_combination.md) — a *different fold* (reduce-to-`Scalar`, not reduce-to-`Tensor[N]`), so the two must **not** be merged. Fuses up from the L1 leaves `dot`, `tdot` (firm) and `bilinear-form` (rough-in, the M-weighted member). The exact conjugation / argument-order convention (Palace documents `Dot(comm, x, A, y) = yᴴ A x`) is to be pinned by the harvester.

## Implied by

- The cycle-018 combinator-miner rough-in dep-map row in [`L2/index`](./index.md) ("chapter `./inner_product.md` to be authored by harvester").
- Plan (`scaffolding/priorities.md`) **Now (active) #1** + OQs `inner-product-fold-sibling-candidate`, `inner-product-harvester-formalization-and-conjugation-pinning`.

## Refinement pending

- **Owner:** `harvester`.
- **Plan:** Now (active) #1.
- **OQs:** `inner-product-harvester-formalization-and-conjugation-pinning`.
- Pin the conjugation / arg-order convention; emit the sibling-`linear_combination`-not-merged section; self-verify every L0 range. Pairs with the L2>L1 theme [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md).

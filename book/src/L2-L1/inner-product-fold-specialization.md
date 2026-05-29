# inner-product-fold-specialization

> **Status: `stub`** — claim-free placeholder materialized 2026-05-28 (CLAUDE.md §Methodology invariants "Integration may materialize implied components as stubs"). Exists so the plan and the paired L2 stub resolve to a live home. **No citations or semantic claims yet** — the next `abstractor` refines it in place (`stub` → `rough-in` → `firm`).

## What this will be

The L2>L1 lowering theme taking the L2 [`inner_product`](../L2/inner_product.md) fold into its L1 specializations — `dot` (Hermitian), `tdot` (unconjugated bilinear), and the M-weighted member via `bilinear-form` — selected by **conjugation-convention / argument-order dispatch**. Sibling to the firm [`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md) (which dispatches the `linear_combination` fold by *arity*); this one dispatches the inner-product fold by *conjugation convention*.

## Implied by

- Plan (`scaffolding/priorities.md`) **Now (active) #2**.
- OQ `inner-product-harvester-formalization-and-conjugation-pinning`.
- The firm sibling theme [`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md) (the fold-specialization pairing precedent); pairs with the L2 stub [`inner_product`](../L2/inner_product.md).

## Refinement pending

- **Owner:** `abstractor` (after the `inner_product` L2 operator firms — the fold must exist before its specialization lowering).
- **Plan:** Now (active) #2.
- **OQs:** `inner-product-harvester-formalization-and-conjugation-pinning`.

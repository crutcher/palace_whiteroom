# assemble-diagonal

> **Status: `stub`** — claim-free placeholder materialized 2026-05-28 (CLAUDE.md §Methodology invariants "Integration may materialize implied components as stubs"). Exists so converging forward-references resolve to a live home and the plan points at a real file. **No citations or semantic claims yet** — the next `harvester` refines it in place (`stub` → `rough-in` → `firm`).

## What this will be

The L1 **operator-to-data** primitive `assemble_diagonal(A) -> Tensor[N]` — extracting the diagonal of a linear operator as a vector (Palace `Operator::AssembleDiagonal`). It is explicitly **NOT an [`apply_linop`](./apply_linop.md) variant** (it produces operator data, not the action of the operator on a vector); recording it as its own entry prevents it being folded into `apply_linop`'s variant axes. Provisional slug `assemble-diagonal` (matches the Palace symbol); the harvester pins the canonical name (plan item uses `diagonal-extraction`).

## Implied by

- OQ `assemblediagonal-is-not-apply-linop-variant` (deliberate exclusion-marker for a future L1 entry).
- Plan (`scaffolding/priorities.md`) Backlog Medium item **diagonal-extraction-l1**.
- Roadmap §Intermediate-tier "Diagonal-preconditioner apply" (reused by Jacobi / Chebyshev / block-Jacobi / polynomial preconditioners — the fan-out rationale).

## Refinement pending

- **Owner:** `harvester`.
- **Plan:** Backlog Medium `diagonal-extraction-l1`.
- **OQs:** `assemblediagonal-is-not-apply-linop-variant`.
- Pin the canonical slug/operator name; confirm it composes with the `reciprocal` + `elementwise_product` of the diagonal-preconditioner-apply intermediate.

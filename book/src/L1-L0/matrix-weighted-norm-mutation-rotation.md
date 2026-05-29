# matrix-weighted-norm-mutation-rotation

> **Status: `stub`** — claim-free placeholder materialized 2026-05-28 (CLAUDE.md §Methodology invariants "Integration may materialize implied components as stubs"). Exists so converging forward-references resolve to a live home and the plan points at a real file. **No citations or semantic claims yet** — the next `abstractor` refines it in place (`stub` → `rough-in` → `firm`).

## What this will be

The L1>L0 lowering theme for the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) operator (rough-in at L1): how the closed-form energy norm `√(xᴴ B x)` rewrites into the L0 three-step `B.Mult(x, Bx); dot = Dot(comm, Bx, x); √dot` — including **caller-supplied workspace `Bx` ownership and lifetime** (a destination buffer, not just scratch, that disappears at L1), the SPD applicability condition (the L0 `MFEM_ASSERT`), and the element-type-decomposition plumbing on the complex branch. Inherits the [`dot`](./dot-mutation-rotation.md) MPI-collective theme.

## Implied by

- Three in-file references in [`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (the workspace-ownership and `√(dot(apply_linop(B,x), x))` unfold are deferred to "the (not-yet-authored) `matrix-weighted-norm-mutation-rotation` L1>L0 theme").
- OQ `matrix-weighted-norm-mutation-rotation-l1-l0-theme`.
- Plan (`scaffolding/priorities.md`) Backlog Medium item **matrix-weighted-norm + bilinear-form firm-promotion**.

## Refinement pending

- **Owner:** `abstractor` (+ `lowering-verifier` for the workspace mention-and-erase audit).
- **Plan:** Backlog Medium `matrix-weighted-norm + bilinear-form firm-promotion`.
- **OQs:** `matrix-weighted-norm-mutation-rotation-l1-l0-theme`.
- Note: `matrix-weighted-norm` is itself still `rough-in` at L1 — its own firm-promotion gate (test/literature coverage) is tracked separately and is upstream of firming this theme.

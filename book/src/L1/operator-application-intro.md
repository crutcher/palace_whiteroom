---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/apply_linop
    - L1/assemble_diagonal
    - L1/assemble_frequency_operator
    - L1/port_projection
---

# L1 — Operator application & assembly

The opaque-operator surface of L1: forms that take a `LinearOperator[N, N]` as an opaque value and either apply it, introspect it, or assemble one. `apply_linop` (`y = A·x`) is the operator/action gate to the L2 `krylov_step` vocabulary; `assemble_diagonal` (`d = diag(A)`) is its operator/data sibling — same opaque argument, opposite side of the operator/data divide (it consumes no vector, so it is explicitly **not** an `apply_linop` variant). `assemble_frequency_operator` (`A(ω) = K + iω·C − ω²·M + A2(ω)`) is the driven per-ω **operator-operand specialization of `linear_combination`** — a scalar-weighted sum of a fixed operator basis under affine-in-ω weights, single-pipeline-by-design (driven only), NOT a new fold.

Chapters are listed alphabetically.

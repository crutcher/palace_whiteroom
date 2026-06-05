---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/apply_nonlinear_pencil
    - L1/lu_solve
    - L1/nleps_deflated_residual
    - L1/nleps_deflated_solve
    - L1/nleps_eigenvalue_correction
    - L1/nleps_jacobian_action
---

# L1 — Dense-coordinate & NEP interior atoms

The coordinate-space dense-direct primitive `lu_solve` (index motif 6 — a small dense `k×k` matrix in *coordinate* space, `k` = deflation rank / ROM basis size, with a load-bearing factorization-kernel variant axis: full-pivot LU / full-pivot QR / LDLT) and the five interior atoms of Palace's quasi-Newton nonlinear-eigenvalue-problem (NEP) solver, which compose against it. The per-step quasi-Newton chain is `residual → jacobian-action → eigenvalue-correction → deflated-solve → line-search`: `apply_nonlinear_pencil` (the NEP `apply_linop`), `nleps_deflated_residual` (deflation-extension residual), `nleps_jacobian_action` (derivative-pencil Jacobian action), `nleps_eigenvalue_correction` (the scalar Newton half), and `nleps_deflated_solve` (the block Schur-complement solve). All five factor through firm BLAS-1 leaves and `lu_solve`; their `k = 0` cases degenerate to the bare big-space forms.

Chapters are listed alphabetically.

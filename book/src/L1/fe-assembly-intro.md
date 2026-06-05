---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/eliminate_essential_bc
    - L1/eliminate_rhs
    - L1/fe_assemble
    - L1/weak_form_term
---

# L1 — FE-assembly sub-spine

The finite-element **assembly** surface (the MFEM-equivalent assembly sub-spine, in scope per CLAUDE.md mesh/FE). `fe_assemble` is the integrator-fold assembler `K = Σ_i A(space, term_i)`; `weak_form_term` is its element type, the `(coefficient, differential-operator)` pair with the `Gradient | Identity | Curl | Divergence` differential-operator variant axis. `eliminate_essential_bc` and `eliminate_rhs` are the two **separable BC-treatment post-compositions** that compose AFTER the fold (NOT part of it) — one pins the operator's essential rows/cols per a diagonal policy, one lifts inhomogeneous Dirichlet data into the RHS.

The per-term assembly leaf `A(space, ·)` inside the fold is libCEED-owned (the `fe-assemble-libceed-boundary-obstruction` theme, `opaque-library-ownership`) — a strict sub-term below the fold's leaf, which does NOT downgrade `fe_assemble` from firm. This sub-spine sits downstream of the FE-space sub-spine, which constructs the space the fold folds over.

Chapters are listed alphabetically.

# L1 — FE-assembly sub-spine

The finite-element **assembly** surface (the MFEM-equivalent assembly sub-spine, in scope per CLAUDE.md mesh/FE). `fe_assemble` is the integrator-fold assembler `K = Σ_i A(space, term_i)`; `weak_form_term` is its element type, the `(coefficient, differential-operator)` pair with the `Gradient | Identity | Curl | Divergence` differential-operator variant axis. `eliminate_essential_bc` and `eliminate_rhs` are the two **separable BC-treatment post-compositions** that compose AFTER the fold (NOT part of it) — one pins the operator's essential rows/cols per a diagonal policy, one lifts inhomogeneous Dirichlet data into the RHS.

The per-term assembly leaf `A(space, ·)` inside the fold is libCEED-owned (the `fe-assemble-libceed-boundary-obstruction` theme, `opaque-library-ownership`) — a strict sub-term below the fold's leaf, which does NOT downgrade `fe_assemble` from firm. This sub-spine sits downstream of the FE-space sub-spine, which constructs the space the fold folds over.

Chapters are listed alphabetically.

# Summary

[Introduction](./introduction.md)

# Methodology

- [Overview](./methodology/overview.md)

# Specification

- [Index — Slice Status](./spec/index.md)
  - [CG — Preconditioned Conjugate Gradient](./spec/slices/cg.md)
  - [GMRES](./spec/slices/gmres.md)
  - [Orthogonalisation (MGS / CGS / CGS2)](./spec/slices/orthog.md)
  - [Divergence-free projection](./spec/slices/divfree.md)
  - [Chebyshev smoother](./spec/slices/chebyshev.md)

# Concepts (shared library)

- [Index](./concepts/index.md)
  - [Dependency map](./concepts/dependency-map.md)
  - [rotation — methodology concept](./concepts/rotation.md)
  - [variant absorption — methodology concept](./concepts/variant-absorption.md)
  - [constructed operators — methodology concept](./concepts/constructed-operators.md)
  - [apply_linop](./concepts/apply_linop.md)
  - [axpy](./concepts/axpy.md)
  - [dot](./concepts/dot.md)
  - [nrm2](./concepts/nrm2.md)
  - [scal](./concepts/scal.md)
  - [givens](./concepts/givens.md)
  - [trsv](./concepts/trsv.md)
  - [gemv_basis](./concepts/gemv_basis.md)
  - [orthogonalization](./concepts/orthogonalization.md)
  - [incremental-least-squares](./concepts/incremental-least-squares.md)
  - [gmres](./concepts/gmres.md)
  - [set_subvector_zero](./concepts/set_subvector_zero.md)
  - [ksp_solve](./concepts/ksp_solve.md)
  - [tensor-field-lift](./concepts/tensor-field-lift.md)
  - [sequential-obstruction](./concepts/sequential-obstruction.md)
  - [state-stratification](./concepts/state-stratification.md)
  - [solve-monad](./concepts/solve-monad.md)
  - [convergence-test](./concepts/convergence-test.md)
  - [chebyshev-iteration](./concepts/chebyshev-iteration.md)

# Design Artifacts

- [Index](./design/index.md)
- [L4 — Graph-Evaluation Calculus (strawman)](./design/l4_calculus.md)

# Meta-Reviews

- [Index](./meta-reviews/index.md)
  - [2026-05-24 — first meta-review (cycles 1–3)](./meta-reviews/2026-05-24.md)
  - [2026-05-24 — second meta-review (cycles 4–6)](./meta-reviews/2026-05-24-cycles-4-6.md)
  - [2026-05-24 — third meta-review (cycles 7–9)](./meta-reviews/2026-05-24-cycles-7-9.md)
  - [2026-05-24 — fourth meta-review (cycles 10–12)](./meta-reviews/2026-05-24-cycles-10-12.md)
  - [2026-05-24 — fifth meta-review (cycles 13–15)](./meta-reviews/2026-05-24-cycles-13-15.md)
  - [2026-05-24 — sixth meta-review (cycles 16–18)](./meta-reviews/2026-05-24-cycles-16-18.md)
  - [2026-05-24 — seventh meta-review (cycles 19–21)](./meta-reviews/2026-05-24-cycles-19-21.md)
  - [2026-05-24 — eighth meta-review (cycles 22–24)](./meta-reviews/2026-05-24-cycles-22-24.md)
  - [2026-05-25 — ninth meta-review (cycles 25–30)](./meta-reviews/2026-05-24-cycles-25-30.md)
  - [2026-05-25 — tenth meta-review (cycles 31–36) — Phase 6 DONE](./meta-reviews/2026-05-25-cycles-31-36.md)
  - [2026-05-25 — eleventh meta-review (cycles 37–43) — first skill extraction](./meta-reviews/2026-05-25-cycles-37-43.md)
  - [2026-05-25 — twelfth meta-review (cycles 44–49)](./meta-reviews/2026-05-25-cycles-44-49.md)

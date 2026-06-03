# L2 step kernels

The recurring **iteration-step kernels** of the L2 surface: the *kernel half* of the
kernel-plus-driver shape, where the **driver half** lives one layer up (L4 `iterate_while`).
Each is a single per-step body that an outer fold drives to convergence; the body is
visible and algebraic at L2, the iteration that folds it is named/erased at this layer.

- [`krylov-step`](./krylov-step.md) — the recurring Krylov / polynomial step kernel
  (apply ▷ optional-auxiliary ▷ iterate-update ▷ scalar-update ▷ readout); the kernel
  half whose driver is L4 `iterate_while`.
- [`chebyshev-iteration`](./chebyshev-iteration.md) — the three-term polynomial recurrence;
  the concrete L2 entry behind `krylov-step` variant-axis 3.

Both `firm`. Chapters are alphabetical.

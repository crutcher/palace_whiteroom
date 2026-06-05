---
edges:
  reference:
    - concepts/constructed-operators  # parent concept (apply_BA IS a constructed operator)
    - L2/krylov-step               # use-site (per-Arnoldi-step operator, absorbs side/flexible)
---

# Concept: `apply_BA` (preconditioner-side constructed operator)

The per-Arnoldi-step constructed operator for preconditioned Krylov
solvers: given an underlying `A`, a preconditioner `M⁻¹`, and a side
enum (`LEFT | RIGHT | NONE`), `apply_BA` returns the operator applied
at each Krylov expansion step plus the side-dependent auxiliary vector
to store.

This is a [constructed operator](./constructed-operators.md) — the
side variant is absorbed at solver-start time by constructing the
appropriate composition; the per-step procedure invokes `apply_BA`
uniformly without re-inspecting the side.

## Background

In restarted GMRES (Saad 2003 §9.3), the preconditioner side determines
the Krylov space being built:

- **Left**: build a Krylov space for `M⁻¹ A` against the
  preconditioned residual `M⁻¹ (b − A x)`. Per step: `w ← M⁻¹ A v_j`;
  no auxiliary vector needed.
- **Right**: build a Krylov space for `A` against the unpreconditioned
  residual `b − A x`, with correction in the right-preconditioned space
  `M⁻¹ V_m`. Per step: `w ← A (M⁻¹ v_j)`; auxiliary `z_j = M⁻¹ v_j`
  must be stored for the correction.
- **None**: `M = I` reduces both sides to `w ← A v_j`; no auxiliary.
- **Flexible (FGMRES)**: right-side with a per-step-varying `M⁻¹`;
  auxiliary `z_j` always stored.

## Signature (canonical)

```
apply_BA : (A, M, side, flexible) → Operator-with-auxiliary
apply_BA.apply(v) → (w, z?)        // z present when flexible or side=RIGHT
```

## Slices that use this primitive

- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — the per-Arnoldi-step operator;
  absorbs the `side` and `flexible` variant axes.

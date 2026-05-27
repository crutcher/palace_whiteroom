# Decision: cycle-004 MINRES/BiCGStab speculative L1 operators not promoted in cycle-005

**Date**: 2026-05-27
**Decided in**: cycle-005 harvester invocation (`reports/2026-05-27T025354Z-harvester-krylov-step-L2/CYCLE.md`)
**Decision**: Five speculative L1 operators from cycle-004 obstruction themes — `lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min` (from `book/src/L1-L0/minres-iteration.md`); `bicgstab_step`, `omega_update`, `stabilisation_update` (from `book/src/L1-L0/bicgstab-iteration.md`) — are **not promoted to firm L1** as part of the `krylov-step` L2 harvest.

## Reasoning

The cycle-005 harvester role-spec applies the `feedback_unimplemented_palace_components` policy: a speculative L1 operator may be promoted to firm only if (a) doing so simplifies the L2 `krylov-step` semantics AND (b) the lift is small.

Each of the five speculative operators is a **step-body specialisation** of `krylov-step`, not an orthogonal axis that would simplify its semantics:

- `lanczos_step` — symmetric-tridiagonal specialisation of the orthogonalization-variant axis already absorbed in `krylov-step` (axis #2 of six).
- `three_term_recurrence_update` — band-3 specialisation of the `dot+axpy` chain inside `lanczos_step`'s orthogonalize stage; not a new axis.
- `givens_apply_with_residual_min` — band-3 specialisation of the `incremental-least-squares` running-QR step; structurally distinct from `krylov-step`'s primitive composition and would belong (if firmed) under a separate `incremental-least-squares` L2 entry, not under `krylov-step`.
- `bicgstab_step` — short-recurrence non-symmetric Krylov step; its per-step primitive count is **two** `apply_linop` calls instead of `krylov-step`'s typical one, but this is a slice-level instantiation, not an L1 axis change. The two-apply-per-step shape would surface in BiCGStab's slice as a numeric in the variant-axis profile (a `apply_count` field, not a new axis kind).
- `omega_update` — closed-form scalar arithmetic on two `dot` results; algebraically identical to a `dot / dot` ratio. Already expressible in `krylov-step`'s scalar-stratum-update phase using existing L1 primitives. No new operator needed.
- `stabilisation_update` — bundle of `omega_update + axpy + axpy`. Already a composition of three L1 primitives; bundling them into one named L1 operator would inflate the L1 vocabulary without algebraic gain. If BiCGStab acquires a Palace anchor, the bundle name would be appropriate at L2 (as a `krylov-step` variant), not at L1.

Promoting any of the five would **inflate** rather than simplify `krylov-step`'s L2 semantics: the variant-axis profile would gain entries for "is-this-a-lanczos-step" / "is-this-a-bicgstab-step", duplicating the slice-level instantiation surface. The variant-absorption discipline (level (c) closure into `op.T` / `op.orthog` / `op.scalars`) already handles the methods' divergences cleanly.

## Re-evaluation triggers

This decision should be re-opened if any of:

1. Palace acquires an L0 anchor for MINRES or BiCGStab (the cycle-004 obstruction themes flip from `obstruction` to affirmative).
2. The cross-layer-cross-cutter identifies a coverage gap that requires one of the speculative operators as an L1 dependency for a *firm* lowering theme (currently they live only in obstruction themes).
3. A future Phase-1 slice (LOBPCG, time-stepping, eigensolver) introduces a step kernel that genuinely requires one of the speculative operators as an L1-level primitive (not as a slice-instantiation of `krylov-step`).

## Cross-references

- `book/src/L1-L0/minres-iteration.md` — the cycle-004 obstruction theme that proposed `lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min`.
- `book/src/L1-L0/bicgstab-iteration.md` — the cycle-004 obstruction theme that proposed `bicgstab_step`, `omega_update`, `stabilisation_update`.
- `book/src/L2/krylov-step.md` — the cycle-005 firm operator whose variant-axis profile would absorb these step-body specialisations.
- `feedback_unimplemented_palace_components` (project memory) — the policy applied.

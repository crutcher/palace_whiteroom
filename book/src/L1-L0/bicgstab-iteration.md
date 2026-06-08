# bicgstab-iteration

The L1>L0 lowering theme for the **BiCGStab** (Biconjugate Gradient Stabilized) Krylov iteration. **Obstruction theme** — Palace has no L0 realisation of BiCGStab; this entry records the algorithm's L1 form against the literature (Saad 2003 §7.4.2) as a placeholder for when an anchor materialises (either Palace gains an implementation, or MFEM is admitted as L0 substrate — see open question `bicgstab-mfem-reanchor-policy`).

## Slug

`bicgstab-iteration`

## L1 form (LHS)

The pure-functional BiCGStab iteration step. Short-recurrence non-symmetric Krylov: maintains residual `r`, search direction `p`, shadow residual `r̂₀`, and three scalars `ρ_prev`, `α_prev`, `ω_prev` across iterations.

```
bicgstab_step(A, M, r̂₀, s) =
  let ρ     = dot(r̂₀, s.r)
      β     = (ρ / s.ρ_prev) · (s.α_prev / s.ω_prev)
      p     = axpby(1, s.r, β, axpby(1, s.p, -β·s.ω_prev, s.v))
      ŷ     = M⁻¹·p
      v     = A·ŷ
      α     = ρ / dot(r̂₀, v)
      h     = axpy(α, ŷ, s.x)
      rₛ    = axpy(-α, v, s.r)
      ẑ     = M⁻¹·rₛ
      t     = A·ẑ
      ω     = omega_update(t, rₛ)       -- = dot(t,rₛ) / dot(t,t)
      x_new = axpy(ω, ẑ, h)
      r_new = axpy(-ω, t, rₛ)
  in    (x_new, r_new, p, v, ρ, α, ω)
```

State carried: `s = (x, r, p, v, ρ_prev, α_prev, ω_prev)`. `r̂₀` is set once at iteration start (commonly `r̂₀ := r₀`) and held constant.

## L0 form (RHS)

**None in Palace.** Three negative-anchor citations confirm the absence:

- `palace/utils/labels.hpp:111` — `BICGSTAB` enum value declaration.
- `palace/utils/configfile.cpp:132` — JSON parser entry mapping string `"BiCGSTAB"` to the enum.
- `palace/linalg/ksp.cpp:53-57` — Krylov-solver factory groups `BICGSTAB` with `MINRES` and `DEFAULT` into `MFEM_ABORT("Unexpected solver type for Krylov solver configuration!")`. The config knob exists; every invocation aborts.

No `BiCGStabSolver` class exists in `palace/linalg/iterative.hpp`.

## Applicability conditions

(From Saad 2003 §7.4.2 — recorded as literature-anchored; no Palace L0 verification possible.)

- Square operator `A` (any non-symmetric system).
- Breakdown guards: `ρ_prev ≠ 0`, `ω_prev ≠ 0`, `dot(r̂₀, v) ≠ 0`, `dot(t, t) ≠ 0`. Breakdowns require restart or method fallback.
- `r̂₀` initialised to `r₀` (the residual at iteration 0); held constant across the iteration.
- Preconditioner `M` is either identity (un-preconditioned) or an SPD/non-singular linear operator.

## Justification kind

**`obstruction`** — negative-result theme. The L1 form is well-specified by literature; the L0 anchor in Palace is empty. The theme exists as documentation that this iteration's primitive sequence is *recognised* and *waiting for a target*, not as an active lowering rule.

## Speculative L1 operators

All `rough-in (obstruction)` — harvester should not promote until either Palace gains BiCGStab or the MFEM-as-L0-substrate decision admits `mfem::BiCGSTAB`:

- **`bicgstab_step`** — `(A, M, r̂₀, state) → state'` where `state = (x, r, p, v, ρ_prev, α_prev, ω_prev)`. Short-recurrence specialisation of the `krylov_step` pattern. Differs from `cg_step` / `gmres_step` in maintaining the second residual `r̂₀` and the half-step (`t`, `ω`) stabilisation.
- **`omega_update`** — `(t, r) → ⟨t,r⟩/⟨t,t⟩`. The signature scalar of BiCGStab — the `ω` Galerkin-coefficient that minimizes the residual norm over the new search direction `t`.
- **`stabilisation_update`** — `(t, r, ẑ, h) → (x_new, r_new, ω)`. Composite half-step: computes `ω`, then updates iterate `x` and residual `r` via two `axpy` calls. Bundled because the three sub-steps share the `ω` value and are conceptually one stabilisation phase.

## Status

`rough-in (obstruction)` — awaiting an anchor (Palace implementation or admitted MFEM substrate). The L1 form is well-specified against the literature (Saad 2003 §7.4.2); the L0 anchor in Palace is empty (the three negative anchors above). Promotion requires either a Palace BiCGStab implementation or the MFEM-as-L0-substrate decision admitting `mfem::BiCGSTAB` (open question `bicgstab-mfem-reanchor-policy`).

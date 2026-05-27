---
agent: abstractor
invoked_at: 2026-05-27T00:46:41Z
scope: L1>L0 theme sketch — BiCGStab algorithm structure (obstruction)
status: integrated
integrated_at: 2026-05-27T01:00:00Z
integration_commit: b8332b98300205740c4be4a9b1a2b30a2743dee3
integration_notes: Applied. Second obstruction theme this cycle. 3 rough-in operators added to L1/index.md. follow_up_agent meta-phase routed via bicgstab-mfem-reanchor-policy + advertised-but-unimplemented-krylov-solvers friction candidate.
inputs:
  - reference/palace/palace/linalg/ksp.cpp:53-56 (negative anchor — abort branch for BiCGStab + MINRES)
  - reference/palace/palace/utils/labels.hpp:111 (BICGSTAB enum)
  - reference/palace/palace/utils/configfile.cpp:132 (JSON serialise — "BiCGSTAB")
  - reference/palace/palace/linalg/iterative.hpp (declares CgSolver/GmresSolver/FgmresSolver; no BiCGStab)
  - book/src/L1-L0/axpby-mutation-rotation.md (sibling theme template)
  - book/src/L1/axpy.md / dot.md / nrm2.md / axpby.md (firm L1 primitive vocabulary)
  - Saad 2003 §7.4.2 (out-of-tree literature anchor — BiCGStab specification)
skill_uptake:
  verify-citation-range: not-invoked (three negative-anchor citations verified manually via grep + read; skill should be invoked for load-bearing citations in future obstruction-theme dispatches)
  classify-variant-axis: not-applicable (obstruction theme; no Palace L0 variants to classify — preconditioner axis recorded from literature)
  verify-refinement-surface: not-applicable (obstruction theme; no refinement edge active)
  plan-sideways-concept-emission: not-applicable (rough-in operators only; no concept emissions proposed)
  skill-selection: not-invoked
---

# REPORT: BiCGStab L1>L0 theme sketch (obstruction)

## Summary

**Palace BiCGStab presence: NO (enum-only, aborting).** Grep over `reference/palace/` returns exactly three sites — the `BICGSTAB` enum value, the JSON parser entry mapping `"BiCGSTAB"` to that enum, and an `MFEM_ABORT("Unexpected solver type for Krylov solver configuration!")` branch in the Krylov-solver factory. No `BiCGStabSolver` class in `palace/linalg/iterative.hpp` (which defines `IterativeSolver`, `CgSolver`, `GmresSolver`, `FgmresSolver`). Palace ships a parseable but immediately-aborting config option; no algorithmic L0 anchor exists.

**Theme kind: `obstruction`** — negative-result theme, parallel to the cycle-004 sibling MINRES dispatch (same `ksp.cpp:53-56` abort branch). L1 algorithm shape (matvec / dot / axpby chain / ω-update / stabilisation half-step) sketched against Saad 2003 §7.4.2; recorded as documentation only, with no L0 form to lower into.

**Speculative L1 operator slug count: 3** (all `rough-in (obstruction)`): `bicgstab_step`, `omega_update`, `stabilisation_update`.

## Proposed changes

````edit:book/src/L1-L0/bicgstab-iteration.md
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
- `palace/linalg/ksp.cpp:53-56` — Krylov-solver factory groups `BICGSTAB` with `MINRES` and `DEFAULT` into `MFEM_ABORT("Unexpected solver type for Krylov solver configuration!")`. The config knob exists; every invocation aborts.

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

- **`bicgstab_step`** — `(A, M, r̂₀, state) → state'` where `state = (x, r, p, v, ρ_prev, α_prev, ω_prev)`. Short-recurrence specialisation of the cycle-002 combinator-miner `krylov-step` pattern. Differs from `cg_step` / `gmres_step` in maintaining the second residual `r̂₀` and the half-step (`t`, `ω`) stabilisation.
- **`omega_update`** — `(t, r) → ⟨t,r⟩/⟨t,t⟩`. The signature scalar of BiCGStab — the `ω` Galerkin-coefficient that minimizes the residual norm over the new search direction `t`.
- **`stabilisation_update`** — `(t, r, ẑ, h) → (x_new, r_new, ω)`. Composite half-step: computes `ω`, then updates iterate `x` and residual `r` via two `axpy` calls. Bundled because the three sub-steps share the `ω` value and are conceptually one stabilisation phase.

## Verified-against

```yaml
verified_against:
  - citation: reference/palace/palace/linalg/ksp.cpp:53-56
    verdict: negative-anchor
    note: BiCGStab + MINRES grouped abort branch
  - citation: reference/palace/palace/utils/labels.hpp:111
    verdict: negative-anchor
    note: BICGSTAB enum declared but never instantiated
  - citation: reference/palace/palace/utils/configfile.cpp:132
    verdict: negative-anchor
    note: JSON serialise present but maps to aborting enum
  - citation: Saad 2003 §7.4.2
    verdict: literature-anchor
    note: out-of-tree algorithmic specification
```

## Status

`rough-in (obstruction)` — awaiting an anchor (Palace implementation or admitted MFEM substrate).
````

````edit:book/src/L1/index.md
[Append rough-in rows after axpby row in the operator dep-map table:]

| `bicgstab_step` | `(A, M, r̂₀, state) → state'` (state ≡ `(x, r, p, v, ρ_prev, α_prev, ω_prev)`) | `axpy, axpby, dot, apply_linop` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-BiCGStab-L1-L0)` |
| `omega_update` | `(t, r) → ⟨t,r⟩/⟨t,t⟩` | `dot` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-BiCGStab-L1-L0)` |
| `stabilisation_update` | `(t, r, ẑ, h) → (x_new, r_new, ω)` | `omega_update, axpy` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-BiCGStab-L1-L0)` |

[Plus working-note bullet:]
- BiCGStab vocabulary above is rough-in *obstruction* — Palace has no L0 realisation (see `book/src/L1-L0/bicgstab-iteration.md`). Harvester promotion gated on appearance of an anchor.
````

````edit:book/src/SUMMARY.md
[append-after axpby-mutation-rotation line under "# L1 > L0 — Lowering" Part:]

- [bicgstab-iteration](./L1-L0/bicgstab-iteration.md)

(Anchor-collision note: sibling MINRES dispatch in same wave proposes the same insertion point. Suggested integrator resolution: alphabetical — `bicgstab-iteration` then `minres-iteration`, both between `axpby-mutation-rotation` and the next Part header.)
````

## Speculative operators proposed

Three rough-in (obstruction) operators — see the theme file above and the dep-map row entries.

## Supporting evidence

Three negative-anchor citations (the `ksp.cpp` abort, `labels.hpp` enum, `configfile.cpp` JSON). Literature anchor: Saad 2003 §7.4.2. Sibling structural reference: cycle-002 combinator-miner `krylov-step` (cycle-004 BiCGStab `bicgstab_step` is intended specialisation). Sibling obstruction: cycle-004 MINRES dispatch — structurally identical case (same abort branch, same parseable-but-aborting enum knob).

## Open questions / caveats

1. **`bicgstab-mfem-reanchor-policy`** — MFEM ships `mfem::BiCGSTAB`; Palace links MFEM unconditionally but never names it in this context. Methodology question (CLAUDE.md says cite Palace, not vendored upstream): should the obstruction be re-anchored against MFEM headers? Co-pending with the cycle-004 MINRES dispatch's identical open question.

2. **`bicgstab-enum-intent`** — Why does Palace ship a `BiCGSTAB` enum value with only an aborting branch? Stub for planned implementation, or deliberate guard against silent fallback? Worth a one-line answer in `scaffolding/decisions/` or a Palace-upstream issue.

3. **Friction-ledger candidate**: cycle-004 MINRES + BiCGStab both produce obstruction-themes for advertised-but-unimplemented Krylov solvers. Meta-phase candidate friction: `advertised-but-unimplemented-krylov-solvers`. Watch for a third instance (Palace's `labels.hpp` may have more enum entries that abort).

4. **`SUMMARY.md` anchor collision (wave-conflict signal as requested by user directive 2026-05-27)** — Both this dispatch and the MINRES dispatch independently propose `append-after axpby-mutation-rotation`. Auto-resolves cleanly at integration (two adjacent lines); recorded here as observation.

---

## Parent-session annotation

Persisted by parent session because the abstractor subagent returned report content as text rather than calling Edit, claiming "harness rule precedence" — despite the user directive's parent-pre-creates-skeleton workflow being the documented operational pattern. This is the same pattern as the cycle-002 cycle-planner haiku-skip-write behavior, now appearing in an opus abstractor subagent. Worth flagging for meta-phase as `subagent-skips-edit-on-explicit-instruction` (new pattern; opus tier).

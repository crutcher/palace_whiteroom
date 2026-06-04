---
kind: feature-surface
feature: eigenfrequency-qfactor
level: L1
status: firm
composes:
  - book/src/feature/eigenmode.L1.md (seed — the producing driver column: supplies the converged EigResult)
  - book/src/L4/eigenfreq_qfactor_reduce.md (firm — the per-mode scalar-ratio reduction; L1 sees the unfolded per-mode map; promoted firm cycle-082, firm-on-positive-structure escape; both folded per-mode scalar maps firm L1: eigenvalue-untransform c080 + participation_ratio c077)
l0_ground_truth:
  - palace/drivers/eigensolver.cpp:424-439 (the eigenvalue→ω un-transform in the readout loop)
  - palace/models/postoperator.cpp:1171-1203 (MeasureLumpedPortsEig — the Q-factor computation)
---

# eigenfrequency-qfactor — L1 composition-root (output product)

The **eigenfrequency + quality-factor table** output product, presented at L1 as a pure-function composition of L1 operations. This is the **pure-function feature surface** of the output-product sub-kind: the same composition root as the [L4 chapter](./eigenfrequency-qfactor.L4.md), but expressed in L1 vocabulary (an explicit per-mode pure readout, no L4 combinator naming) — the form a reader navigating L1 sees when asking "what whole product does this per-mode readout add up to?"

At L1 the eigenfrequency / Q-factor product is a pure function `config → (f, Q) table`: it consumes the converged eigenpair set (the `EigResult`) produced by the [`eigenmode.L1`](./eigenmode.L1.md) driver column, then maps each mode to its `(f, Q)` row (the **mutation already lifted** — the L0 in-place `omega = std::sqrt(omega)` reassignment and the `vi.quality_factor = ...` cache write are lifted to value-returning forms per the L1>L0 mutation rotation).

## The composition

    -- inputs = config (the eigenmode problem); output = the (f, Q) table (the physical product)
    eigenfrequency_qfactor :: EigenmodeConfig -> [(Scalar, Scalar)]
    eigenfrequency_qfactor cfg =
      let res   = eigenmode_eigenpairs cfg                  -- (1) the eigenmode driver column → EigResult (converged eigenpairs)
          ptype = problem_type cfg                          -- the eigenvalue→ω un-transform selector
      in  [ let omega = untransform ptype (res.eigenvalues ! i)  -- ω = √μ (linear) | λ/i (quadratic)
                f     = re omega                                 -- eigenfrequency fₘ = Re ωₘ
                k     = loss_rate cfg (res ! i)                  -- κₘ = ½R|Iₘⱼ|²/Eₘ (resistive-port participation)
                q     = if k == 0 then infinity else f / abs k   -- quality factor Qₘ = ωₘ/κₘ
            in  (f, q)                                           -- (2) per-mode (fₘ, Qₘ) row
          | i <- [0 .. res.converged - 1] ]                      -- map over the converged modes (no inter-mode state)

1. **The eigenmode driver column produces the converged eigenpair set** — [`eigenmode.L1`](./eigenmode.L1.md) (**firm**). The upstream composition root assembles the `K`/`C`/`M` pencil ([`fe_assemble`](../L1/fe_assemble.md) ×3) and applies the single opaque [`eigsolve`](../L1/eigsolve.md) eigensolver-as-operator **once**, returning an `EigResult` record (the `eigenvalues`, `eigenvectors`, `converged` count, `status`). This output-product column **consumes** that record; it does not re-derive the solve. L0: the `EigResult`-equivalent extraction in the readout loop `for (int i = 0; i < num_conv; i++)` (`eigensolver.cpp:424`), `omega = eigen->GetEigenvalue(i)` (`:427`).

2. **The per-mode pure readout → the (f, Q) table** — a pure list comprehension over the `res.converged` converged eigenpairs, mapping each mode to its `(f, Q)` row:
   - the eigenfrequency `fₘ = Re ωₘ`, where `ωₘ` is the problem-type un-transform of the eigenvalue (`ω = √μ` for the linear EVP `μ = -λ² = ω²`; `ω = λ/i` for the quadratic EVP `λ = iω`). L0: `omega = std::sqrt(omega)` (`eigensolver.cpp:430-434`) / `omega /= 1i` (`:435-439`).
   - the quality factor `Qₘ = ωₘ/κₘ`, where the loss rate `κₘ = ½Rⱼ·|Iₘⱼ|²/Eₘ` is the resistive-lumped-port participation (the port resistor self-energy `½R|I|²` over the mode total energy `Eₘ`), with the `κ = 0 ⇒ Q = ∞` lossless-mode guard. L0: `resistor_power = 0.5·|R|·Re(I·conj(I))` (`postoperator.cpp:1196-1198`), `mode_port_kappa = copysign(resistor_power/energy_electric_all, …)` (`:1199-1200`), `quality_factor = freq_re/|κ|` (`:1201-1203`).
   This stage is a pure per-mode map — no inter-mode state, no solve-iteration. At L4 this exact per-mode reduction is named the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) combinator (the reduce-to-scalar-table member of the L4 algebra-of-folds); L1 sees the unfolded per-mode comprehension. The mode-field recovery (`Eᵢ`, `B = -1/(iω)∇×E`) is the eigenmode driver column's separate stage-3 field readout, NOT part of this `(f, Q)` scalar reduction.

## Inputs / outputs (the feature surface)

- **Input — config (the eigenmode problem).** `EigenmodeConfig` (problem-type selector → the eigenvalue→ω un-transform; requested mode count → table rows; resistive-lumped-port boundary data `R` + port currents → the loss-rate κ), inherited from the producing driver column. All read-only.
- **Output — the physical product.** The per-mode `(f, Q)` table — one row per converged mode, each carrying the eigenfrequency `fₘ = Re ωₘ` and quality factor `Qₘ = ωₘ/κₘ`. L0: the per-mode `omega` un-transformed at `eigensolver.cpp:430-439`, the `quality_factor` at `postoperator.cpp:1201-1203`.

## L1 vs L4

The L1 and L4 composition roots express the **same output product**; they differ in vocabulary:
- **L1** (this chapter): the reduction is an explicit per-mode pure list comprehension — the eigenvalue un-transform branch + the κ ratio + the `f/κ` quotient, written out per mode.
- **L4** ([`eigenfrequency-qfactor.L4`](./eigenfrequency-qfactor.L4.md)): the whole per-mode reduction is the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) combinator (the per-mode map + un-transform dispatch + κ closure made *structural*). The L4 form is the one the outward backend consumes; the L1 form is the pure-function decomposition the L4 combinator names.

The defining structural fact at both levels: a **rank-1 per-mode scalar-ratio table**, NOT a rank-2 family-PAIR Gram grid — distinct from the capacitance / inductance output products (c074 D6 closed-negative). The L1→L0 direction (how the per-mode readout lowers to the in-place `omega = sqrt(omega)` reassignment and the `vi.quality_factor` cache write) is the per-operator L1>L0 mutation-rotation of the readout; this composition root records only the L1 composition (high→low discipline).

## Constituent down-links

| Stage | L1 constituent | Status | L0 site |
|---|---|---|---|
| producing driver column (sibling reference, not a blocker) | [`eigenmode.L1`](./eigenmode.L1.md) (driver feature column) | seed | `eigensolver.cpp:32-477` |
| eigenfrequency un-transform | [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (firm L1; folded by [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md)) | firm | `eigensolver.cpp:430-439` |
| Q-factor κ participation | [`participation_ratio`](../L1/participation_ratio.md) (firm L1; folded by [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md)) | firm | `postoperator.cpp:1188-1203` |

## Status

`firm` — the L1 pure-function composition root for the eigenfrequency / Q-factor output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L1 counterpart of the [eigenfrequency-qfactor.L4](./eigenfrequency-qfactor.L4.md) composition root. It consumes the [`eigenmode.L1`](./eigenmode.L1.md) driver column's converged eigenpair set, then maps each mode to its `(f, Q)` row (the problem-type eigenvalue un-transform + the resistive-port κ participation ratio + the `f/κ` quotient). **The column promotes off `seed` to `firm` under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03):** its sole directly-owned constituent, the reduction's L4 home [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md), is **`firm`** (promoted cycle-082 on the firm-on-positive-structure escape; both of its folded per-mode primitives firm L1 — the eigenvalue un-transform via [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080) and the κ participation ratio via [`participation_ratio`](../L1/participation_ratio.md) (cycle-077) — and the eigenpair→`(f, Q)` assembly carries no inner-product-axiom content). The cross-link to the [`eigenmode.L1`](./eigenmode.L1.md) driver column (its own `status: seed`) is a **SIBLING reference, NOT a blocker** — the reciprocal drift-guard, not a constituent-firmness dependency. This retires the earlier mutual-blocking deadlock (the prior text held the column seed because `eigenmode` was seed, while `eigenmode` was symmetrically held seed for reducing into this column). The verb-side gate (OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test`) was discharged at c082. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. The defining structural fact carried from L4: a rank-1 per-mode scalar-ratio table, NOT a `gram_reduce` family-PAIR grid (c074 D6 closed-negative). Evidence: the L0 readout / Q-factor ranges `eigensolver.cpp:424-439` + `postoperator.cpp:1171-1203` realizing the reduction, plus the constituent down-links.

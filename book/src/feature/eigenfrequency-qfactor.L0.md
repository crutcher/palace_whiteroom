---
kind: feature-surface
feature: eigenfrequency-qfactor
level: L0
status: firm
l0_ground_truth:
  - palace/drivers/eigensolver.cpp:424-475 (the per-mode readout loop — eigenvalue→ω un-transform + measure)
  - palace/models/postoperator.cpp:1171-1203 (PostOperator::MeasureLumpedPortsEig — the Q-factor computation)
lifts_to:
  - book/src/feature/eigenfrequency-qfactor.L1.md (the L1 pure-function composition root)
---

# eigenfrequency-qfactor — L0 ground-truth surface

The **eigenfrequency + quality-factor table** output product at L0: the cited Palace source that realizes the per-mode reduction composition root, with the per-stage source ranges that the L1 / L4 feature chapters lift. This is the ground-truth surface — every claim is a `(file:start-end)` citation into `palace/drivers/eigensolver.cpp` (the eigenfrequency un-transform) and `palace/models/postoperator.cpp` (the Q-factor).

The eigenfrequency / Q-factor reduction is split across two source sites: the **eigenvalue→ω un-transform** in the eigenmode driver's per-mode readout loop (`palace/drivers/eigensolver.cpp:424-439`), and the **Q-factor computation** in `PostOperator<solver_t>::MeasureLumpedPortsEig` (`palace/models/postoperator.cpp:1172`, body `:1171-1221`). It is the **output-product** tail of the eigenmode driver: the driver's `Solve` (`eigensolver.cpp:32-477`) assembles the pencil, runs the single `eigen->Solve()` (`:367`), and reads out each converged mode; the un-transform + the lumped-port measurement reduce each mode to its `(f, Q)` row.

## The composition, in source

The eigenfrequency / Q-factor reduction is a pure per-mode map over the converged eigenpair set — no inter-mode state. The source stages, in order:

1. **The per-mode readout loop (the map spine).** `for (int i = 0; i < num_conv; i++)` (`:424`) iterates the already-converged eigenpair set — the driver's only outer loop, a pure post-processing readout (NOT a solve-iteration; explicitly contrasted at `book/src/L4/solve_family.md:146`). Per mode, `std::complex<double> omega = eigen->GetEigenvalue(i)` (`:427`) reads the eigenvalue and the error norms (`:428-429`). This is the L0 site the L1/L4 per-mode reduction map lifts (the `eigenfreq_qfactor_reduce` outer map).

2. **The eigenfrequency un-transform.** `omega` is un-transformed to the physical angular frequency by problem type: `omega = std::sqrt(omega)` for the linear EVP (`μ = -λ² = ω²`, branch `:430-434`, the `if (!C && !has_A2)` test), or `omega /= 1i` for the quadratic EVP (`λ = iω`, branch `:435-439`). The eigenfrequency `f = Re ω`. This is the L0 site the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) `untransform` dispatch lifts (the problem-type variant axis) — the `if (!C && !has_A2)` test is the linear-vs-quadratic EVP branch, the load-bearing axis.

3. **The Q-factor computation (the resistive-port participation).** In `PostOperator<solver_t>::MeasureLumpedPortsEig() const` (def `:1172`, guarded `if constexpr (solver_t == ProblemType::EIGENMODE)`, `:1175`), the eigenfrequency `freq_re = measurement_cache.freq.real()` (`:1177`, `f = Re ω` from the same per-mode `ω`) and the total electric energy `energy_electric_all` (`:1178-1179`) are read. The per-port loop (`:1180`) computes, for each resistive port (`std::abs(data.R) > 0.0`, `:1192`): the resistor power `resistor_power = 0.5·|data.R|·Re(I·conj(I))` (`:1196-1198`, `½R|I|²`), the loss rate `mode_port_kappa = copysign(resistor_power/energy_electric_all, I.real())` (`:1199-1200`, `κ_mj = ½R_j|I_mj|²/E_m`), and the quality factor `quality_factor = (κ == 0) ? mfem::infinity() : freq_re/|κ|` (`:1201-1203`, `Q_mj = ω_m/κ_mj` with the lossless `κ=0 ⇒ Q=∞` guard). The formula is documented in the source comment `:1186-1191`. This is the L0 site the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) Q-factor scalar projection lifts (the κ participation closure). The inductive-port branch (`:1204-1217`, the `if (std::abs(data.L) > 0.0)` arm at `:1213-1217`) is the energy-participation-ratio sibling, NOT a Q.

4. **Per-mode record → the physical product.** Back in the driver readout loop, `post_op.MeasureAndPrintAll(i, E, B, omega, error_abs, error_bkwd, num_conv)` (`eigensolver.cpp:458`) measures + records the per-mode observables (the un-transformed `omega` feeds `measurement_cache.freq` that `MeasureLumpedPortsEig` reads). The loop closes at `:471`; `MFEM_VERIFY(num_conv >= iodata.solver.eigenmode.n, ...)` (`:472-475`) checks enough modes converged. Each converged mode → one `(f, Q)` table row.

The mode-field recovery (`eigen->GetEigenvector(i, E)`, `:443`; `B = -1/(iω)∇×E`, `:447-449`) is the eigenmode driver's separate stage-3 field readout, NOT part of this `(f, Q)` scalar reduction.

## Inputs / outputs (the feature surface, in source)

- **Input — config (the eigenmode problem).** The problem-type test `if (!C && !has_A2)` (`eigensolver.cpp:430`, the linear-vs-quadratic EVP selector for the un-transform); the requested mode count `iodata.solver.eigenmode.n` (`:472`); the resistive-lumped-port resistances `data.R` + port currents `vi.I_RLC[0]` (`postoperator.cpp:1192, 1195`), supplied by the producing driver column + the measurement cache.
- **Output — the physical product.** The per-mode eigenfrequency `omega` (un-transformed, `eigensolver.cpp:430-439`) and quality factor `vi.quality_factor` (`postoperator.cpp:1201-1203`), recorded by `post_op.MeasureAndPrintAll(...)` (`eigensolver.cpp:458`) — one `(f, Q)` row per converged mode.

## Lifts to

This L0 surface lifts to the L1 pure-function composition root [`eigenfrequency-qfactor.L1`](./eigenfrequency-qfactor.L1.md) (the in-place `omega = std::sqrt(omega)` reassignment + the `vi.quality_factor = ...` cache write → value-returning per-mode `(f, Q)` evaluations) and the L4 combinator composition root [`eigenfrequency-qfactor.L4`](./eigenfrequency-qfactor.L4.md) (the per-mode readout `for` loop + the un-transform branch + the Q-factor body → the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) per-mode scalar-ratio reduction combinator). The per-operator L1>L0 mutation-rotation of the readout carries the per-write lifts; this feature surface records the output-product *site map* (which source range realizes which reduction stage).

## Status

`firm` — the L0 ground-truth surface for the eigenfrequency / Q-factor output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [capacitance.L0](./capacitance.L0.md) / [inductance.L0](./inductance.L0.md) output-product exemplars. **The column promotes off `seed` to `firm` under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03):** its sole directly-owned constituent reduction verb [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) is `firm` (c082); the producing [`eigenmode`](./eigenmode.L0.md) driver column is a sibling reference, not a blocker. Every stage is a cited range into `palace/drivers/eigensolver.cpp` (the un-transform) + `palace/models/postoperator.cpp` (the Q-factor), confirmed on-disk via palace-codemap `read_range` (the readout loop `:424`, eigenvalue read `:427`, the linear-EVP `std::sqrt` branch `:430-434`, the quadratic-EVP `/= 1i` branch `:435-439`, the measure `:458`, loop close `:471`, verify `:472-475`; the Q-factor def `postoperator.cpp:1172`, `freq_re` `:1177`, the κ formula comment `:1186-1191`, `resistor_power` `:1196-1198`, `mode_port_kappa` `:1199-1200`, `quality_factor` `:1201-1203`). The load-bearing structural fact at L0: a pure per-mode map (the readout loop carries no inter-mode accumulator), reducing each converged mode to its `(f, Q)` scalar row — a rank-1 per-mode table, NOT a family-PAIR Gram grid (c074 D6 closed-negative). The chapter's evidence IS the source range + the per-stage site map to the constituent reduction (the adapted surface-or-evidence form for the feature-surface kind).

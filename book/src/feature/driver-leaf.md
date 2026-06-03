# Feature surfaces — driver-leaf columns

The **driver-leaf** grouping holds the per-simulation-driver feature columns — the **leaf feature column** sub-kind whose stage-(2) constituents are *vocabulary ops* (firm L4 combinators / L1 pure functions / cited L0 driver source). Each column is a composition root for one `ProblemType` branch the lifecycle ROOT dispatches into: inputs = the driver's config surface; output = the driver's *solution family*; body = the composition of the firm assemble / solve vocabulary at that level.

The 5 drivers span the solve-shape corners the vocabulary spine has to cover:

- [`driven`](./driven.L4.md) — the **operator-VARYING** corner: a per-ω rebuild with `SetOperators` *inside* the loop, composing the [`frequency_sweep`](../L4/frequency_sweep.md) map. Levels: [L4](./driven.L4.md) · [L1](./driven.L1.md) · [L0](./driven.L0.md).
- [`eigenmode`](./eigenmode.L4.md) — the **opaque-library black-box** corner: the SLEPc eigen-iteration. Levels: [L4](./eigenmode.L4.md) · [L1](./eigenmode.L1.md) · [L0](./eigenmode.L0.md).
- [`electrostatic`](./electrostatic.L4.md) — a **fixed-operator** solve (assemble `K` once, per-terminal-source RHS-varying map). The seed exemplar of the feature-surface kind. Levels: [L4](./electrostatic.L4.md) · [L1](./electrostatic.L1.md) · [L0](./electrostatic.L0.md).
- [`magnetostatic`](./magnetostatic.L4.md) — the second **fixed-operator** witness, structurally identical to electrostatic down to the assemble-once / collect shape, differing in the family-index domain and the per-element field post-process. Levels: [L4](./magnetostatic.L4.md) · [L1](./magnetostatic.L1.md) · [L0](./magnetostatic.L0.md).
- [`transient`](./transient.L4.md) — the **state-threaded sequential-fold** corner: a [`fold_solve`](../L4/fold_solve.md) time-step march. Levels: [L4](./transient.L4.md) · [L1](./transient.L1.md) · [L0](./transient.L0.md).

Columns are alpha-ordered within this grouping. The within-column level ordering is **high→low** (L4 → L1 → L0), the deliberate FEATURE-SURFACE exception to alpha-within-cohort ordering. A 6th co-equal leaf driver column — wave-port / boundary-mode (the 6th `ProblemType` dispatch branch) — is planned and lands here when its constituent vocabulary composes cleanly. All columns stay `seed` until every composed constituent is firm.

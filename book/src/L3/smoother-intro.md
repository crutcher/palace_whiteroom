# Smoothers & projector gates (L3)

The constructed-operator-gate / polynomial-smoother cohort. These span the obstruction-profile spectrum from obstruction-free, through obstruction-carrying-by-reference, to partial-obstruction (`index.md` §Semantics):

- [`jacobi-smoother`](./jacobi-smoother.md) — the **thinnest** constructed-operator gate; apply is one whole-tensor elementwise product `op.dinv ⊙ x = (ω·D⁻¹) ⊙ x`. Carries **NO obstruction** at L3 — the sharpest contrast with the obstruction-carrying members.
- [`divfree-projector`](./divfree-projector.md) — a fixed four-step straight-line composition (`WeakDiv → Z_{bdr_eff} → ksp_solve → Grad`); **obstruction-carrying by reference** — its own apply authors no loop, but step 3 invokes the firm-L3 `ksp_solve` whose outer fold IS a `sequential-obstruction` (the inner iteration stays interior per the `nested-constructed-operator-gate` fidelity rule). The middle profile of the cohort.
- [`chebyshev`](./chebyshev.md) — the fixed-degree polynomial smoother; the **first** L3 `partial-obstruction` (c013). Its body lifts to a global tensor-field expression, but the inner `k`-recurrence + outer `pc_it` Richardson sweep are **unconditional** numerical-stability sequential obstructions (Phillips & Fischer 2022 §2). Inner-product-free — the structural distinction from the solver-caps `krylov-step`.

See `index.md` §"Operator dep-map → Smoothers & projector gates" for the per-operator detail.

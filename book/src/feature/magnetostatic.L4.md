---
kind: feature-surface
feature: magnetostatic
level: L4
feature_root: seed
rank: firm
edges:
  depends-on:
    - target: L4/fe_assemble
      kind: composes
    - target: L4/solve_family
      kind: composes
    - target: L4/ksp_solve
      kind: composes
    - target: L4/gram_reduce
      kind: composes
    - target: palace/drivers/magnetostaticsolver.cpp:22-108
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: magnetostatic :: MagnetostaticConfig -> InductanceMatrix (the IoData surface)
  reference:
    - feature/inductance.L4
---

# magnetostatic — L4 composition-root

The **magnetostatic simulation feature**, presented at L4 as a single composition of firm L4 combinators — the **outward backend-lowering entry point** for the curl-curl pipeline. This chapter is a *composition root*: it does not introduce a new combinator; it wires the already-firm L4 vocabulary into the user-facing feature (config → inductance matrix), and links DOWN to each composed piece.

The magnetostatic pipeline is — like [electrostatic](./electrostatic.L4.md) — a **fixed-operator** solve: the curl-curl stiffness operator `K` is assembled **once**, then re-used unchanged across a family of per-surface-current right-hand sides. That fixed-operator shape is exactly the [`solve_family`](../L4/solve_family.md) combinator's load-bearing specialization (operator captured once, hoisted outside the map), and the assemble-once is exactly [`fe_assemble`](../L4/fe_assemble.md). Magnetostatic is the combinator's **second witness** of the fixed corner — named the magnetostatic sibling at `book/src/L4/solve_family.md:113` — structurally identical to electrostatic down to the `GetStiffnessMatrix()` / `SetOperators(*K,*K)`-outside-the-loop / `std::vector<Vector>`-collect shape.

## The composition

At L4 the whole simulation is the composition (Haskell-style; the strawman `book/src/semantics/index.md` notation):

    -- inputs = config; output = the inductance matrix (the physical product)
    magnetostatic :: MagnetostaticConfig -> InductanceMatrix
    magnetostatic cfg =
      let space = nd_space cfg                          -- the Nédélec H(curl) finite-element space (readonly construction stratum)
          terms = [ curl_curl (reluctivity cfg) ]       -- the weak-form term list (single ν-weighted ∇×∇× term)
          k     = fe_assemble space terms               -- (1) assemble K ONCE  ── L4/fe_assemble (firm)
          rhss  = [ excitation cfg idx | idx <- surface_current_sources cfg ]  -- per-source RHS family
          as    = solve_family k rhss                   -- (2) fixed-operator per-source map  ── L4/solve_family
      in  inductance_reduce k as (currents cfg)         -- (3) Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ) reduction → inductance matrix

Three composed stages, each a link DOWN to firm L4 vocabulary:

1. **Assemble `K` once** — [`fe_assemble`](../L4/fe_assemble.md) (**firm**). The L4 assemble-fold combinator `fe_assemble space terms = sum (map (assemble_term space) terms)` folds the weak-form term list into the global curl-curl stiffness operator `K`. For magnetostatic the term list is the single ν-weighted curl-curl term `[ curl_curl(ν) ]` (the single-term reduction, `fe_assemble`'s law 5; magnetostatic is one of `fe_assemble`'s three mining-gate witnesses — the ∇× witness, named at `book/src/L4/fe_assemble.md:167`). `space` (the Nédélec H(curl) space) is the `readonly` construction stratum captured once. L0: `auto K = curlcurl_op.GetStiffnessMatrix()` (`palace/drivers/magnetostaticsolver.cpp:29`).

2. **Per-source map with the operator captured once** — [`solve_family`](../L4/solve_family.md) (**firm**). The L4 fixed-operator map-over-RHS-family combinator `solve_family op rhss = map (ksp_solve op) rhss` captures `K` once and maps the [`ksp_solve`](../L4/ksp_solve.md) cap over the per-source RHS family, collecting the solution family `[Aᵢ]`. The magnetostatic surface-current sweep is `solve_family`'s **witness 2** (named at `book/src/L4/solve_family.md:113`): `op = K`, the family is the surface-current-boundary index set, each element is one `ksp_solve K rhsᵢ`. The operator-capture-once hoist (`solve_family` law 2) is the L4 typing of `ksp.SetOperators(*K,*K)` sitting OUTSIDE the loop. L0: solver built + captured once at `magnetostaticsolver.cpp:34-35`, the family map at `:66`, the per-element solve `ksp.Mult(RHS, A[step])` at `:77`.

3. **Inductance-matrix reduction** — [`gram_reduce`](../L4/gram_reduce.md) (**firm**), the `w = 1/(IᵢIⱼ)` current-normalized specialization. The inductance matrix is the operator-weighted symmetric-Gram reduction `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` over the solution family `[Aᵢ]` — the current-normalized (`w i j = 1/(Iᵢ Iⱼ)`) member of the shared L4 reduction `gram_reduce K xs w = Gᵢⱼ = w(i,j)·(xⱼᵀ K xᵢ)` (the COMSOL magnetic-energy formulation: `Mᵢᵢ = 2Uₘ(Aᵢ)/Iᵢ²`, off-diagonals from the cross energy, normalized by the excitation currents `Iᵢ`; named magnetostatic specialization at `book/src/L4/gram_reduce.md:172-176`). It is the **same** reduction as the [electrostatic](./electrostatic.L4.md) capacitance Gram — differing **only** in the weight closure (`w = 1/(IᵢIⱼ)` current vs `w = 1` voltage; the operator `M_mag` and family `[Aᵢ]` are leaf-content absorbed into `K` and `xs`). `gram_reduce` is the **entry** (replace-and-propagate, CLAUDE.md §VOCABULARY-SHIFT redirect); the inductance reduction re-expresses THROUGH it as the current-normalized corner, NOT as a hand-rolled fold. The combinator's `map`-then-`reduce` body composes two firm L1 building blocks — the diagonal `Aᵢᵀ K Aᵢ` is the firm [`matrix_weighted_norm`](../L1/matrix_weighted_norm.md) radicand, the off-diagonal `Aⱼᵀ K Aᵢ` is the firm [`bilinear_form`](../L1/bilinear_form.md), each scaled by the current normalization absorbed into `w` — folded over the upper-triangle family-pair grid with the symmetric mirror. The inverse (`Minv = M⁻¹`, LAPACK) is the `gram_inverse` consumer downstream of the reduction, not part of it. This stage is the **output product** half of the composition root — authored in full as its dedicated output-product feature column [`inductance`](./inductance.L4.md), which links back DOWN to this driver as its producing column. L0: `PostprocessTerminals` (`magnetostaticsolver.cpp:108`, def `:110`; the energy-form `Mult`/`Dot` at `:129-138`, the inverse at `:151-152`).

## Inputs / outputs (the feature surface)

- **Input — config.** `MagnetostaticConfig`: the Nédélec H(curl) space construction (mesh + order → `nd_space`), the material reluctivity ν (→ the curl-curl term coefficient), the surface-current-boundary source set (→ the RHS family index domain), and the linear-solver configuration (→ the `ksp_solve` solver build). All `readonly` construction-stratum inputs; none threads mutably through the composition. L0 home: `CurlCurlOperator curlcurl_op(iodata, mesh)` (`magnetostaticsolver.cpp:28`) — `iodata` is the config surface.
- **Output — the physical product.** `InductanceMatrix` — the `n_source × n_source` Maxwell inductance matrix `M` (and its inverse `Minv`). This is what the user ran the magnetostatic solver to compute. L0 home: the `mfem::DenseMatrix M` written by `PostprocessTerminals` (`magnetostaticsolver.cpp:122`).

## Why this composes cleanly (sibling of the cleanest exemplar)

The magnetostatic feature composes as cleanly as [electrostatic](./electrostatic.L4.md) because **every stage composes a firm L4 combinator with no obstruction at the composition level**:

- The assemble is a single-term `fe_assemble` (law 5; no multi-term concatenation needed) — the ∇× witness of the assemble-fold.
- The solve family is `solve_family`'s **fixed-operator** corner — the operator-capture-once specialization that *holds* the concatenation-homomorphism (the second witness; the driven pipeline's per-ω-rebuilt operator is the harder `per-element` superset, NOT this feature).
- The reduction is the firm [`gram_reduce`](../L4/gram_reduce.md) fold of firm bilinear_form evaluations (firm diagonal + firm off-diagonal), differing from electrostatic's only in the per-element current normalization `Iᵢ Iⱼ` (a scalar weight absorbed into the fold) — no iterative obstruction.

The whole feature therefore lowers cleanly outward to the L4 backend surface: `magnetostatic = inductance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of combinators with a single shared operator capture. All its directly-owned constituents are firm — [`fe_assemble`](../L4/fe_assemble.md), [`solve_family`](../L4/solve_family.md), [`ksp_solve`](../L4/ksp_solve.md), and the stage-(3) readout [`gram_reduce`](../L4/gram_reduce.md). The cross-linked output-product column [`inductance`](./inductance.L4.md) is a SIBLING reference, not a blocker.

## Constituent down-links

| Stage | L4 combinator | Status | L0 site |
|---|---|---|---|
| assemble K once | [`fe_assemble`](../L4/fe_assemble.md) | firm | `magnetostaticsolver.cpp:29` |
| per-source solve map | [`solve_family`](../L4/solve_family.md) | firm | `magnetostaticsolver.cpp:34-35, 66, 76-77, 99` |
| per-element solve cap | [`ksp_solve`](../L4/ksp_solve.md) | firm | `magnetostaticsolver.cpp:77` |
| inductance reduction (Aⱼᵀ K Aᵢ / Iᵢ Iⱼ) | [`gram_reduce`](../L4/gram_reduce.md) (`w = 1/(IᵢIⱼ)` current-normalized specialization) — folding L1 [`matrix_weighted_norm`](../L1/matrix_weighted_norm.md) (diagonal, firm) / [`bilinear_form`](../L1/bilinear_form.md) (off-diagonal, firm) | firm | `magnetostaticsolver.cpp:108, 110-152` |

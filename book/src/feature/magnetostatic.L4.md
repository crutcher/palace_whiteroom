---
kind: feature-surface
feature: magnetostatic
level: L4
status: seed
composes:
  - book/src/L4/fe_assemble.md (firm — assemble curl-curl K once: the assemble-fold combinator)
  - book/src/L4/solve_family.md (rough-in (test-coverage-bounded) — fixed-operator per-source map)
  - book/src/L4/ksp_solve.md (firm — the per-source solve cap solve_family maps)
l0_ground_truth:
  - palace/drivers/magnetostaticsolver.cpp:22-108 (MagnetostaticSolver::Solve)
---

# magnetostatic — L4 composition-root

The **magnetostatic simulation feature**, presented at L4 as a single composition of firm L4 combinators — the **outward backend-lowering entry point** for the curl-curl pipeline. This chapter is a *composition root*: it does not introduce a new combinator; it wires the already-firm L4 vocabulary into the user-facing feature (config → inductance matrix), and links DOWN to each composed piece.

The magnetostatic pipeline is — like [electrostatic](./electrostatic.L4.md) — a **fixed-operator** solve: the curl-curl stiffness operator `K` is assembled **once**, then re-used unchanged across a family of per-surface-current right-hand sides. That fixed-operator shape is exactly the [`solve_family`](../L4/solve_family.md) combinator's load-bearing specialization (operator captured once, hoisted outside the map), and the assemble-once is exactly [`fe_assemble`](../L4/fe_assemble.md). Magnetostatic is the combinator's **second witness** of the fixed corner — named the magnetostatic sibling at `book/src/L4/solve_family.md:113` — structurally identical to electrostatic down to the `GetStiffnessMatrix()` / `SetOperators(*K,*K)`-outside-the-loop / `std::vector<Vector>`-collect shape.

## The composition

At L4 the whole simulation is the composition (Haskell-style; the strawman `book/src/design/l4_calculus.md` notation):

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

2. **Per-source map with the operator captured once** — [`solve_family`](../L4/solve_family.md) (**rough-in (test-coverage-bounded)**). The L4 fixed-operator map-over-RHS-family combinator `solve_family op rhss = map (ksp_solve op) rhss` captures `K` once and maps the [`ksp_solve`](../L4/ksp_solve.md) cap over the per-source RHS family, collecting the solution family `[Aᵢ]`. The magnetostatic surface-current sweep is `solve_family`'s **witness 2** (named at `book/src/L4/solve_family.md:113`): `op = K`, the family is the surface-current-boundary index set, each element is one `ksp_solve K rhsᵢ`. The operator-capture-once hoist (`solve_family` law 2) is the L4 typing of `ksp.SetOperators(*K,*K)` sitting OUTSIDE the loop. L0: solver built + captured once at `magnetostaticsolver.cpp:34-35`, the family map at `:66`, the per-element solve `ksp.Mult(RHS, A[step])` at `:77`.

3. **Inductance-matrix reduction** — the B-weighted Gram `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` over the solution family, producing the (symmetric) Maxwell inductance matrix `M` (the COMSOL magnetic-energy formulation: `Mᵢᵢ = 2Uₘ(Aᵢ)/Iᵢ²`, off-diagonals from the cross energy, normalized by the excitation currents `Iᵢ`). At L4 this is a `map`-then-`reduce` over the solution-family pairs using the operator-weighted-bilinear primitives — the rough-in L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) `Aᵢᵀ K Aᵢ` on the diagonal, the rough-in L1 [`bilinear-form`](../L1/bilinear-form.md) `Aⱼᵀ K Aᵢ` off-diagonal — each divided by the current normalization `Iᵢ Iⱼ`. There is no *new* L4 combinator here; the reduction is a fold of these bilinear-form evaluations over the family-pair grid, with the result inverted (`Minv = M⁻¹`, LAPACK) for the alternate Maxwell form. This stage is the **output product** half of the composition root; its dedicated L4 reduction-combinator — if the cross-pipeline post-processing proves to share a shape with the electrostatic capacitance reduction (it does, modulo the diagonal current-vs-voltage normalization weight) — is a forward mine, not authored here (see Open questions). L0: `PostprocessTerminals` (`magnetostaticsolver.cpp:108`, def `:110`; the energy-form `Mult`/`Dot` at `:129-138`, the inverse at `:151-152`).

## Inputs / outputs (the feature surface)

- **Input — config.** `MagnetostaticConfig`: the Nédélec H(curl) space construction (mesh + order → `nd_space`), the material reluctivity ν (→ the curl-curl term coefficient), the surface-current-boundary source set (→ the RHS family index domain), and the linear-solver configuration (→ the `ksp_solve` solver build). All `readonly` construction-stratum inputs; none threads mutably through the composition. L0 home: `CurlCurlOperator curlcurl_op(iodata, mesh)` (`magnetostaticsolver.cpp:28`) — `iodata` is the config surface.
- **Output — the physical product.** `InductanceMatrix` — the `n_source × n_source` Maxwell inductance matrix `M` (and its inverse `Minv`). This is what the user ran the magnetostatic solver to compute. L0 home: the `mfem::DenseMatrix M` written by `PostprocessTerminals` (`magnetostaticsolver.cpp:122`).

## Why this composes cleanly (sibling of the cleanest exemplar)

The magnetostatic feature composes as cleanly as [electrostatic](./electrostatic.L4.md) because **every stage composes a firm or rough-in L4 combinator with no obstruction at the composition level**:

- The assemble is a single-term `fe_assemble` (law 5; no multi-term concatenation needed) — the ∇× witness of the assemble-fold.
- The solve family is `solve_family`'s **fixed-operator** corner — the operator-capture-once specialization that *holds* the concatenation-homomorphism (the second witness; the driven pipeline's per-ω-rebuilt operator is the harder `per-element` superset, NOT this feature).
- The reduction is a fold of bilinear-form evaluations (rough-in diagonal + rough-in off-diagonal), differing from electrostatic's only in the per-element current normalization `Iᵢ Iⱼ` (a scalar weight absorbed into the fold) — no iterative obstruction.

The whole feature therefore lowers cleanly outward to the L4 backend surface: `magnetostatic = inductance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of firm combinators with a single shared operator capture. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: it advances cleanly because the constituent vocabulary is firm and composes without forcing the spine.

## Constituent down-links

| Stage | L4 combinator | Status | L0 site |
|---|---|---|---|
| assemble K once | [`fe_assemble`](../L4/fe_assemble.md) | firm | `magnetostaticsolver.cpp:29` |
| per-source solve map | [`solve_family`](../L4/solve_family.md) | rough-in (test-coverage-bounded) | `magnetostaticsolver.cpp:34-35, 66, 76-77, 99` |
| per-element solve cap | [`ksp_solve`](../L4/ksp_solve.md) | firm | `magnetostaticsolver.cpp:77` |
| inductance reduction (Aⱼᵀ K Aᵢ / Iᵢ Iⱼ) | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in) / [`bilinear-form`](../L1/bilinear-form.md) (rough-in) — no dedicated L4 reduction combinator yet | rough-in / rough-in (L1) | `magnetostaticsolver.cpp:108, 110-152` |

## Status

`seed` — the second feature-surface composition-root authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic](./electrostatic.L4.md) exemplar. The composition is sound: stages (1) and (2) compose firm/rough-in L4 combinators (the second witness of the fixed-operator `solve_family` corner); stage (3) composes L1 bilinear-form primitives (rough-in diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md), each current-normalized; no dedicated L4 reduction combinator yet — a forward mine shared with the electrostatic capacitance reduction, not a blocker, since the reduction is a plain fold of evaluations). This chapter carries the *compositional* claim (magnetostatic = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `magnetostaticsolver.cpp:22-108` (`Solve`) + `:110-204` (`PostprocessTerminals`) realizing the composition, plus the firm constituent down-links.

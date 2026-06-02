---
kind: feature-surface
feature: electrostatic
level: L4
status: seed (exemplar)
composes:
  - book/src/L4/fe_assemble.md (firm — assemble K once: the assemble-fold combinator)
  - book/src/L4/solve_family.md (rough-in (test-coverage-bounded) — fixed-operator per-terminal map)
  - book/src/L4/ksp_solve.md (firm — the per-element solve cap solve_family maps)
l0_ground_truth:
  - palace/drivers/electrostaticsolver.cpp:21-98 (ElectrostaticSolver::Solve)
---

# electrostatic — L4 composition-root

The **electrostatic simulation feature**, presented at L4 as a single composition of firm L4 combinators — the **outward backend-lowering entry point** for the simplest Palace pipeline. This chapter is a *composition root*: it does not introduce a new combinator; it wires the already-firm L4 vocabulary into the user-facing feature (config → capacitance matrix), and links DOWN to each composed piece.

The electrostatic pipeline is the cleanest entry point because it is a **fixed-operator** solve: the stiffness operator `K` is assembled **once**, then re-used unchanged across a family of per-terminal right-hand sides. That fixed-operator shape is exactly the [`solve_family`](../L4/solve_family.md) combinator's load-bearing specialization (operator captured once, hoisted outside the map), and the assemble-once is exactly [`fe_assemble`](../L4/fe_assemble.md).

## The composition

At L4 the whole simulation is the composition (Haskell-style; the strawman `book/src/design/l4_calculus.md` notation):

    -- inputs = config; output = the capacitance matrix (the physical product)
    electrostatic :: ElectrostaticConfig -> CapacitanceMatrix
    electrostatic cfg =
      let space  = h1_space cfg                       -- the H1 finite-element space (readonly construction stratum)
          terms  = [ diffusion (permittivity cfg) ]   -- the weak-form term list (single ε-weighted ∇ term)
          k      = fe_assemble space terms            -- (1) assemble K ONCE  ── L4/fe_assemble (firm)
          rhss   = [ excitation cfg idx | idx <- terminal_sources cfg ]  -- per-terminal RHS family
          sols   = solve_family k rhss                -- (2) fixed-operator per-terminal map  ── L4/solve_family
      in  capacitance_reduce k sols                   -- (3) Cᵢⱼ = Vⱼᵀ K Vᵢ reduction → capacitance matrix

Three composed stages, each a link DOWN to firm L4 vocabulary:

1. **Assemble `K` once** — [`fe_assemble`](../L4/fe_assemble.md) (**firm**). The L4 assemble-fold combinator `fe_assemble space terms = sum (map (assemble_term space) terms)` folds the weak-form term list into the global stiffness operator `K`. For electrostatic the term list is the single ε-weighted diffusion term `[ diffusion(ε) ]` (the single-term reduction, `fe_assemble`'s law 5; the electrostatic specialization is named at `book/src/L4/fe_assemble.md:127`). `space` (the H1 space) is the `readonly` construction stratum captured once. L0: `auto K = laplace_op.GetStiffnessMatrix()` (`palace/drivers/electrostaticsolver.cpp:30`).

2. **Per-terminal map with the operator captured once** — [`solve_family`](../L4/solve_family.md) (**rough-in (test-coverage-bounded)**). The L4 fixed-operator map-over-RHS-family combinator `solve_family op rhss = map (ksp_solve op) rhss` captures `K` once and maps the [`ksp_solve`](../L4/ksp_solve.md) cap over the per-terminal RHS family, collecting the solution family `[Vᵢ]`. The electrostatic terminal-boundary sweep is `solve_family`'s **witness 1** (named at `book/src/L4/solve_family.md:107`): `op = K`, the family is the terminal-boundary index set, each element is one `ksp_solve K rhsᵢ`. The operator-capture-once hoist (`solve_family` law 2) is the L4 typing of `ksp.SetOperators(*K,*K)` sitting OUTSIDE the loop. L0: solver built + captured once at `electrostaticsolver.cpp:34-36`, the family map at `:59`, the per-element solve `ksp.Mult(RHS, V[step])` at `:69`.

3. **Capacitance-matrix reduction** — the quadratic-form reduction `Cᵢⱼ = Vⱼᵀ K Vᵢ` over the solution family, producing the (symmetric) Maxwell capacitance matrix `C` (the COMSOL energy formulation: `Cᵢᵢ = 2Uₑ(Vᵢ)/Vᵢ²`, off-diagonals from the cross energy). At L4 this is a `map`-then-`reduce` over the solution-family pairs using the operator-weighted-bilinear primitives (the rough-in L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) `Vᵢᵀ K Vᵢ` on the diagonal, the rough-in L1 [`bilinear-form`](../L1/bilinear-form.md) `Vⱼᵀ K Vᵢ` off-diagonal) — there is no *new* L4 combinator here; the reduction is a fold of these bilinear-form evaluations over the family-pair grid, with the result inverted (`Cinv = C⁻¹`, LAPACK) for the alternate Maxwell form. This stage is the **output product** half of the composition root; its dedicated L4 reduction-combinator (if the cross-pipeline post-processing proves to share a shape with the magnetostatic inductance reduction) is a forward mine, not authored here (see Open questions). L0: `PostprocessTerminals` (`electrostaticsolver.cpp:95`, def `:100`; the energy-form `Mult`/`Dot` at `:118-127`, the inverse at `:139-140`).

## Inputs / outputs (the feature surface)

- **Input — config.** `ElectrostaticConfig`: the H1 space construction (mesh + order → `h1_space`), the material permittivity ε (→ the diffusion term coefficient), the terminal-boundary source set (→ the RHS family index domain), and the linear-solver configuration (→ the `ksp_solve` solver build). All `readonly` construction-stratum inputs; none threads mutably through the composition. L0 home: `LaplaceOperator laplace_op(iodata, mesh)` (`electrostaticsolver.cpp:28`) — `iodata` is the config surface.
- **Output — the physical product.** `CapacitanceMatrix` — the `n_terminal × n_terminal` Maxwell capacitance matrix `C` (and its inverse). This is what the user ran the electrostatic solver to compute. L0 home: the `mfem::DenseMatrix C` written by `PostprocessTerminals` (`electrostaticsolver.cpp:111`).

## Why this is the cleanest exemplar

The electrostatic feature is the cleanest composition root because **every stage composes a firm or rough-in L4 combinator with no obstruction at the composition level**:

- The assemble is a single-term `fe_assemble` (law 5; no multi-term concatenation needed) — the simplest possible use of the assemble-fold.
- The solve family is `solve_family`'s **fixed-operator** corner — the operator-capture-once specialization that *holds* the concatenation-homomorphism (the cleanest member; the driven pipeline's per-ω-rebuilt operator is the harder `per-element` superset, NOT this feature).
- The reduction is a fold of bilinear-form evaluations (rough-in diagonal + rough-in off-diagonal) — no iterative obstruction.

The whole feature therefore lowers cleanly outward to the L4 backend surface: `electrostatic = capacitance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of firm combinators with a single shared operator capture. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: it advances cleanly because the constituent vocabulary is firm and composes without forcing the spine.

## Constituent down-links

| Stage | L4 combinator | Status | L0 site |
|---|---|---|---|
| assemble K once | [`fe_assemble`](../L4/fe_assemble.md) | firm | `electrostaticsolver.cpp:30` |
| per-terminal solve map | [`solve_family`](../L4/solve_family.md) | rough-in (test-coverage-bounded) | `electrostaticsolver.cpp:34-36, 59, 68-69, 89` |
| per-element solve cap | [`ksp_solve`](../L4/ksp_solve.md) | firm | `electrostaticsolver.cpp:69` |
| capacitance reduction (Vⱼᵀ K Vᵢ) | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in) / [`bilinear-form`](../L1/bilinear-form.md) (rough-in) — no dedicated L4 reduction combinator yet | rough-in / rough-in (L1) | `electrostaticsolver.cpp:95, 100-138` |

## Status

`seed (exemplar)` — the first feature-surface composition-root authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: stages (1) and (2) compose firm/rough-in L4 combinators; stage (3) composes L1 bilinear-form primitives (rough-in diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md); the capacitance reduction has no dedicated L4 reduction combinator yet — a forward mine, not a blocker, since the reduction is a plain fold of evaluations). This chapter carries the *compositional* claim (electrostatic = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `electrostaticsolver.cpp:21-98` (`Solve`) + `:100-138` (`PostprocessTerminals`) realizing the composition, plus the firm constituent down-links.

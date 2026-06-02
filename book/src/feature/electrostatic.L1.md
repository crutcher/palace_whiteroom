---
kind: feature-surface
feature: electrostatic
level: L1
status: seed (exemplar)
composes:
  - book/src/L1/fe_assemble.md (firm — assemble K once)
  - book/src/L1/ksp_solve.md (firm — per-terminal solve)
  - book/src/L1/matrix-weighted-norm.md (rough-in (test-coverage-bounded) — diagonal Vᵢᵀ K Vᵢ)
  - book/src/L1/bilinear-form.md (rough-in — off-diagonal Vⱼᵀ K Vᵢ = xᴴ M y)
l0_ground_truth:
  - palace/drivers/electrostaticsolver.cpp:21-98 (ElectrostaticSolver::Solve)
---

# electrostatic — L1 composition-root

The **electrostatic simulation feature**, presented at L1 as a pure-function composition of firm L1 operators. This is the **pure-function feature surface**: the same composition root as the L4 chapter, but expressed in L1 vocabulary (explicit per-operator pure functions, no L4 combinator naming) — the form a reader navigating L1 sees when asking "what whole feature do these L1 operators add up to?"

At L1 the electrostatic feature is a pure function `config → capacitance matrix` built from four firm L1 operators, with the **mutation already lifted** (each operator is mutation-free; the L0 in-place `ksp.Mult(RHS, V[step])` / `M_elec->Mult(...)` writes are lifted to value-returning forms per the L1>L0 mutation rotation).

## The composition

    -- inputs = config; output = the capacitance matrix (the physical product)
    electrostatic :: ElectrostaticConfig -> CapacitanceMatrix
    electrostatic cfg =
      let space = h1_space cfg
          k     = fe_assemble space [ diffusion (permittivity cfg) ]   -- (1) assemble K once
          idxs  = terminal_sources cfg
          vs    = [ ksp_solve k (excitation cfg k idx) | idx <- idxs ] -- (2) per-terminal pure solve
      in  capacitance_matrix k vs                                       -- (3) Cᵢⱼ = bilinear_form k vⱼ vᵢ

1. **Assemble `K` once** — [`fe_assemble`](../L1/fe_assemble.md) (**firm**). The L1 assemble fold `K = Σ_i A(space, termᵢ)` over the single ε-weighted diffusion term. Pure: consumes the space + term list, produces a fresh operator `K`. L0: `laplace_op.GetStiffnessMatrix()` (`palace/drivers/electrostaticsolver.cpp:30`).

2. **Per-terminal pure solve** — [`ksp_solve`](../L1/ksp_solve.md) (**firm**), applied once per terminal source. Each call is the mutation-lifted pure solve `vᵢ = ksp_solve(K, rhsᵢ)` — the L1 form of the L0 `ksp.Mult(RHS, V[step])` (the destination-buffer write lifted to a value-returning solve). The per-terminal RHS `rhsᵢ` is the excitation vector for terminal `idx` (L0 `laplace_op.GetExcitationVector(idx, *K, V[step], RHS)`, `:68`). The fixed-operator reuse (the same `K` across all terminals) is explicit in the composition: `K` is bound once in the `let` and read by every `ksp_solve`. L0: the loop `:59`, the per-element solve `:69`.

3. **Capacitance-matrix reduction** — the symmetric matrix `Cᵢⱼ = Vⱼᵀ K Vᵢ`, built from L1 bilinear-form evaluations (rough-in diagonal + rough-in off-diagonal):
   - diagonal `Cᵢᵢ = Vᵢᵀ K Vᵢ` — the operator-weighted self-form, the rough-in [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) squared (`matrix_weighted_norm(Vᵢ, K)² = Vᵢᵀ K Vᵢ`; the L0 source builds it directly as `M_elec->Mult(V_gf, D_gf)` then `linalg::Dot(V_gf, D_gf)`, `:118-119`).
   - off-diagonal `Cᵢⱼ = Vⱼᵀ K Vᵢ` — the operator-weighted cross-pairing, the (rough-in) [`bilinear-form`](../L1/bilinear-form.md) `α = xᴴ M y` instantiated `⟨Vⱼ, K Vᵢ⟩` (L0 `:122-127`, the same `Mult`/`Dot` with the `j` grid function).
   The result is the symmetric `C` (and its LAPACK inverse `Cinv`, `:139-140`). This stage is a pure fold of bilinear-form evaluations over the solution-family pair grid — no L1 operator is *new* here; the reduction composes [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in) + [`bilinear-form`](../L1/bilinear-form.md) (rough-in).

## Inputs / outputs (the feature surface)

- **Input — config.** `ElectrostaticConfig` (mesh + order → H1 space; permittivity ε → diffusion term; terminal-source set → RHS index domain; linear-solver config). All read-only.
- **Output — the physical product.** `CapacitanceMatrix` — the `n_terminal × n_terminal` Maxwell capacitance matrix `C` (+ inverse). L0: `mfem::DenseMatrix C` (`electrostaticsolver.cpp:111`).

## L1 vs L4

The L1 and L4 composition roots express the **same feature**; they differ in vocabulary:
- **L1** (this chapter): four explicit per-operator pure functions wired by a `let` + list comprehension; the fixed-operator reuse is a value bound once and read repeatedly; the per-terminal map is a comprehension.
- **L4** ([`electrostatic.L4`](./electrostatic.L4.md)): the per-terminal map is the [`solve_family`](../L4/solve_family.md) combinator (the operator-capture-once made *structural*, hoisted outside the map by type); the assemble is the [`fe_assemble`](../L4/fe_assemble.md) fold combinator. The L4 form is the one the outward backend consumes; the L1 form is the pure-function decomposition the L4 combinators name.

The L1→L0 direction (how each pure operator lowers to the in-place driver writes) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline).

## Constituent down-links

| Stage | L1 operator | Status | L0 site |
|---|---|---|---|
| assemble K once | [`fe_assemble`](../L1/fe_assemble.md) | firm | `electrostaticsolver.cpp:30` |
| per-terminal solve | [`ksp_solve`](../L1/ksp_solve.md) | firm | `electrostaticsolver.cpp:59, 68-69` |
| diagonal Vᵢᵀ K Vᵢ | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) | rough-in (test-coverage-bounded) | `electrostaticsolver.cpp:118-119` |
| off-diagonal Vⱼᵀ K Vᵢ | [`bilinear-form`](../L1/bilinear-form.md) | rough-in | `electrostaticsolver.cpp:122-127` |

## Status

`seed (exemplar)` — the L1 pure-function composition root for the electrostatic feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02). Two of the four composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md), [`ksp_solve`](../L1/ksp_solve.md)); BOTH capacitance-reduction primitives are rough-in — the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is `rough-in (test-coverage-bounded)` (no dedicated test exercises the SPD-weighted overload) and the off-diagonal [`bilinear-form`](../L1/bilinear-form.md) is rough-in (its `α = xᴴ M y` signature covers the cross-pairing, so the down-link is correct). The entire stage-3 reduction therefore rests on rough-in L1 primitives — consistent with the column being a `seed (exemplar)`, not a firm composition. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: the L0 driver range `electrostaticsolver.cpp:21-98` + `:100-138` realizing the composition, plus the firm L1 constituent down-links.

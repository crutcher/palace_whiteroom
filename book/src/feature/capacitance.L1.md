---
kind: feature-surface
feature: capacitance
level: L1
feature_root: seed
rank: firm
edges:
  depends-on:
    - target: L1/matrix_weighted_norm
      kind: folds
    - target: L1/bilinear_form
      kind: folds
    - target: palace/drivers/electrostaticsolver.cpp:100-140
      kind: cites-evidence
  reference:
    - feature/electrostatic.L1
---

# capacitance — L1 composition-root

The **Maxwell capacitance matrix** output product, presented at L1 as a pure-function composition of L1 operators. This is the **pure-function feature surface** of the output-product sub-kind: the same composition root as the L4 chapter, but expressed in L1 vocabulary (explicit per-operator bilinear_form evaluations, no L4 combinator naming) — the form a reader navigating L1 sees when asking "what whole product do these L1 bilinear operators add up to?"

At L1 the capacitance product is a pure function `config → capacitance matrix`: it consumes the per-terminal solution family `[Vᵢ]` produced by the [`electrostatic.L1`](./electrostatic.L1.md) driver column, then folds a grid of L1 bilinear_form evaluations into the symmetric matrix `C` (the **mutation already lifted** — the L0 in-place `M_elec->Mult(V_gf, D_gf)` / `Cinv.Invert()` writes are lifted to value-returning forms per the L1>L0 mutation rotation).

## The composition

    -- inputs = config (terminal excitations); output = the capacitance matrix (the physical product)
    capacitance :: ElectrostaticConfig -> CapacitanceMatrix
    capacitance cfg =
      let (k, vs) = electrostatic_family cfg               -- (1) the electrostatic driver column → (K, [Vᵢ])
          m       = length vs
          c i j   | i == j     = matrix_weighted_norm (vs!!i) k ^ 2  -- diagonal  Vᵢᵀ K Vᵢ
                  | otherwise  = bilinear_form (vs!!j) k (vs!!i)      -- off-diag  Vⱼᵀ K Vᵢ
      in  symmetric_matrix m c                             -- (2) symmetric fold over the family-pair grid → C

1. **The producing driver column** — [`electrostatic.L1`](./electrostatic.L1.md). The electrostatic driver assembles `K` once (the [`fe_assemble`](../L1/fe_assemble.md) fold) and maps the per-terminal pure solve [`ksp_solve`](../L1/ksp_solve.md) over the terminal-source family, collecting the solution family `[Vᵢ]`. The capacitance output product consumes that `(K, [Vᵢ])`; it does not re-derive the solve. L0: the per-terminal loop `electrostaticsolver.cpp:59-89`.

2. **Capacitance-matrix reduction** — the symmetric matrix `Cᵢⱼ = Vⱼᵀ K Vᵢ`, built from L1 bilinear_form evaluations over the solution-family pair grid (firm diagonal + firm off-diagonal):
   - diagonal `Cᵢᵢ = Vᵢᵀ K Vᵢ` — the operator-weighted self-form, the now-firm [`matrix_weighted_norm`](../L1/matrix_weighted_norm.md) squared (`matrix_weighted_norm(Vᵢ, K)² = Vᵢᵀ K Vᵢ`; L0 builds it as `M_elec->Mult(V_gf, D_gf)` then `linalg::Dot(V_gf, D_gf)`, `:118-119`).
   - off-diagonal `Cᵢⱼ = Vⱼᵀ K Vᵢ` — the operator-weighted cross-pairing, the firm [`bilinear_form`](../L1/bilinear_form.md) `α = xᴴ M y` instantiated `⟨Vⱼ, K Vᵢ⟩` (L0 `:122-127`, the same energy-form `Mult`/`Dot` with the `j` grid function, `:126`).
   The result is the symmetric `C` (and its LAPACK inverse `Cinv`, `:139-140`). This stage is a pure fold of bilinear_form evaluations over the family-pair grid — no L1 operator is *new* here; the reduction composes [`matrix_weighted_norm`](../L1/matrix_weighted_norm.md) (firm) + [`bilinear_form`](../L1/bilinear_form.md) (firm). At L4 this exact fold is named the [`gram_reduce`](../L4/gram_reduce.md) combinator (voltage `w = 1` specialization); L1 sees the unfolded grid.

## Inputs / outputs (the feature surface)

- **Input — config (terminal excitations).** `ElectrostaticConfig` (terminal-source set → family-index domain + unit-voltage excitations; H1 space + ε → energy operator `K`), inherited from the producing driver column. All read-only.
- **Output — the physical product.** `CapacitanceMatrix` — the `n_terminal × n_terminal` symmetric Maxwell capacitance matrix `C` (+ inverse `Cinv`). L0: `mfem::DenseMatrix C` (`electrostaticsolver.cpp:111`).

## L1 vs L4

The L1 and L4 composition roots express the **same output product**; they differ in vocabulary:
- **L1** (this chapter): the reduction is an explicit symmetric fold over the family-pair grid, each entry a per-operator bilinear_form pure function ([`matrix_weighted_norm`](../L1/matrix_weighted_norm.md) on the diagonal, [`bilinear_form`](../L1/bilinear_form.md) off-diagonal).
- **L4** ([`capacitance.L4`](./capacitance.L4.md)): the whole reduction is the [`gram_reduce`](../L4/gram_reduce.md) combinator at the voltage `w = 1` specialization (the grid fold + symmetric mirror + weight made *structural*). The L4 form is the one the outward backend consumes; the L1 form is the pure-function decomposition the L4 combinator names.

The L1→L0 direction (how the bilinear_form pure functions lower to the in-place `Mult`/`Dot` driver writes) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline).

## Constituent down-links

| Stage | L1 constituent | Status | L0 site |
|---|---|---|---|
| producing driver column | [`electrostatic.L1`](./electrostatic.L1.md) (driver feature column; sibling reference) | firm | `electrostaticsolver.cpp:21-98` |
| diagonal Vᵢᵀ K Vᵢ | [`matrix_weighted_norm`](../L1/matrix_weighted_norm.md) | firm | `electrostaticsolver.cpp:118-119` |
| off-diagonal Vⱼᵀ K Vᵢ | [`bilinear_form`](../L1/bilinear_form.md) | firm | `electrostaticsolver.cpp:122-127` |

Under the OWN-COMPOSITION rule (a column promotes off `seed` when its OWN directly-owned constituents are firm), this column is firm because both its directly-owned reduction primitives are firm — the diagonal [`matrix_weighted_norm`](../L1/matrix_weighted_norm.md) and the off-diagonal [`bilinear_form`](../L1/bilinear_form.md). The [`electrostatic.L1`](./electrostatic.L1.md) producing driver column is a SIBLING reference, not a constituent. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters.

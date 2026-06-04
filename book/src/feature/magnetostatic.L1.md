---
kind: feature-surface
feature: magnetostatic
level: L1
status: seed
composes:
  - book/src/L1/fe_assemble.md (firm — assemble curl-curl K once)
  - book/src/L1/ksp_solve.md (firm — per-source solve)
  - book/src/L1/matrix-weighted-norm.md (firm c091 — diagonal Aᵢᵀ K Aᵢ; promoted to firm by the batch-29 firm-flip-and-cascade wave)
  - book/src/L1/bilinear-form.md (rough-in — off-diagonal Aⱼᵀ K Aᵢ = xᴴ M y)
l0_ground_truth:
  - palace/drivers/magnetostaticsolver.cpp:22-108 (MagnetostaticSolver::Solve)
---

# magnetostatic — L1 composition-root

The **magnetostatic simulation feature**, presented at L1 as a pure-function composition of firm L1 operators. This is the **pure-function feature surface**: the same composition root as the [L4 chapter](./magnetostatic.L4.md), but expressed in L1 vocabulary (explicit per-operator pure functions, no L4 combinator naming) — the form a reader navigating L1 sees when asking "what whole feature do these L1 operators add up to?"

At L1 the magnetostatic feature is a pure function `config → inductance matrix` built from four firm/rough-in L1 operators, with the **mutation already lifted** (each operator is mutation-free; the L0 in-place `ksp.Mult(RHS, A[step])` / `M_mag->Mult(...)` writes are lifted to value-returning forms per the L1>L0 mutation rotation).

## The composition

    -- inputs = config; output = the inductance matrix (the physical product)
    magnetostatic :: MagnetostaticConfig -> InductanceMatrix
    magnetostatic cfg =
      let space = nd_space cfg
          k     = fe_assemble space [ curl_curl (reluctivity cfg) ]    -- (1) assemble K once
          idxs  = surface_current_sources cfg
          as    = [ ksp_solve k (excitation cfg k idx) | idx <- idxs ]  -- (2) per-source pure solve
      in  inductance_matrix k as (currents cfg)                          -- (3) Mᵢⱼ = bilinear_form k aⱼ aᵢ / (Iᵢ Iⱼ)

1. **Assemble `K` once** — [`fe_assemble`](../L1/fe_assemble.md) (**firm**). The L1 assemble fold `K = Σ_i A(space, termᵢ)` over the single ν-weighted curl-curl term. Pure: consumes the Nédélec space + term list, produces a fresh operator `K`. L0: `curlcurl_op.GetStiffnessMatrix()` (`palace/drivers/magnetostaticsolver.cpp:29`).

2. **Per-source pure solve** — [`ksp_solve`](../L1/ksp_solve.md) (**firm**), applied once per surface-current source. Each call is the mutation-lifted pure solve `aᵢ = ksp_solve(K, rhsᵢ)` — the L1 form of the L0 `ksp.Mult(RHS, A[step])` (the destination-buffer write lifted to a value-returning solve). The per-source RHS `rhsᵢ` is the excitation vector for surface-current source `idx` (L0 `curlcurl_op.GetExcitationVector(idx, RHS)`, `:76`). The fixed-operator reuse (the same `K` across all sources) is explicit in the composition: `K` is bound once in the `let` and read by every `ksp_solve`. L0: the loop `:66`, the per-element solve `:77`.

3. **Inductance-matrix reduction** — the symmetric matrix `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)`, built from L1 bilinear-form evaluations (rough-in diagonal + rough-in off-diagonal), each normalized by the excitation currents:
   - diagonal `Mᵢᵢ = (Aᵢᵀ K Aᵢ)/Iᵢ²` — the operator-weighted self-form normalized by the squared current, the now-firm [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) squared (`matrix_weighted_norm(Aᵢ, K)² = Aᵢᵀ K Aᵢ`; the L0 source builds it directly as `M_mag->Mult(A_gf, H_gf)` then `linalg::Dot(A_gf, H_gf)`, then `/ (I_inc[i]*I_inc[i])`, `:129-131`).
   - off-diagonal `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` — the operator-weighted cross-pairing normalized by the current product, the (rough-in) [`bilinear-form`](../L1/bilinear-form.md) `α = xᴴ M y` instantiated `⟨Aⱼ, K Aᵢ⟩` (L0 `:135-138`, the same `Mult`/`Dot` with the `j` grid function, then `/ (I_inc[i]*I_inc[j])`).
   The result is the symmetric `M` (and its LAPACK inverse `Minv`, `:151-152`). This stage is a pure fold of current-normalized bilinear-form evaluations over the solution-family pair grid — no L1 operator is *new* here; the reduction composes [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (firm c091) + [`bilinear-form`](../L1/bilinear-form.md) (rough-in), with the current normalization a scalar weight on each entry.

## Inputs / outputs (the feature surface)

- **Input — config.** `MagnetostaticConfig` (mesh + order → Nédélec H(curl) space; reluctivity ν → curl-curl term; surface-current-source set → RHS index domain + the excitation currents `Iᵢ`; linear-solver config). All read-only.
- **Output — the physical product.** `InductanceMatrix` — the `n_source × n_source` Maxwell inductance matrix `M` (+ inverse). L0: `mfem::DenseMatrix M` (`magnetostaticsolver.cpp:122`).

## L1 vs L4

The L1 and L4 composition roots express the **same feature**; they differ in vocabulary:
- **L1** (this chapter): four explicit per-operator pure functions wired by a `let` + list comprehension; the fixed-operator reuse is a value bound once and read repeatedly; the per-source map is a comprehension.
- **L4** ([`magnetostatic.L4`](./magnetostatic.L4.md)): the per-source map is the [`solve_family`](../L4/solve_family.md) combinator (the operator-capture-once made *structural*, hoisted outside the map by type); the assemble is the [`fe_assemble`](../L4/fe_assemble.md) fold combinator. The L4 form is the one the outward backend consumes; the L1 form is the pure-function decomposition the L4 combinators name.

The L1→L0 direction (how each pure operator lowers to the in-place driver writes) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline).

## Constituent down-links

| Stage | L1 operator | Status | L0 site |
|---|---|---|---|
| assemble K once | [`fe_assemble`](../L1/fe_assemble.md) | firm | `magnetostaticsolver.cpp:29` |
| per-source solve | [`ksp_solve`](../L1/ksp_solve.md) | firm | `magnetostaticsolver.cpp:66, 76-77` |
| diagonal Aᵢᵀ K Aᵢ / Iᵢ² | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) | firm c091 | `magnetostaticsolver.cpp:129-131` |
| off-diagonal Aⱼᵀ K Aᵢ / Iᵢ Iⱼ | [`bilinear-form`](../L1/bilinear-form.md) | rough-in | `magnetostaticsolver.cpp:135-138` |

## Status

`seed` — the L1 pure-function composition root for the magnetostatic feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic.L1](./electrostatic.L1.md) exemplar. Two of the four composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md), [`ksp_solve`](../L1/ksp_solve.md)); of the two inductance-reduction primitives the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is now **firm** (firm c091, the batch-29 firm-flip-and-cascade wave) but the off-diagonal [`bilinear-form`](../L1/bilinear-form.md) is still rough-in (its `α = xᴴ M y` signature covers the cross-pairing, so the down-link is correct; the sole RESIDUAL gate after this cycle). The stage-3 reduction therefore still rests on the rough-in off-diagonal `bilinear-form` (whose L4 home `gram_reduce` STAYS `rough-in (test-coverage-bounded)` on that residual, D3 cycle-091) — consistent with the column being a `seed`, not a firm composition. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: the L0 driver range `magnetostaticsolver.cpp:22-108` + `:110-204` realizing the composition, plus the firm L1 constituent down-links.

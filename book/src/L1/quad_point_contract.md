---
layer: L1
operator: quad_point_contract
# Graded-stack: roadmap_goal (rank 0). The D stage of A = Gᵀ B_𝒟ᵀ D B_𝒟 G — the pointwise per-quad-point
# contraction geom_data ⊙ (basis-evaluated trial). Rank-0: it operates on the quad-point-rank tensor
# Tensor[(E, P, C)] our firm flat-vector-BLAS L1 (Tensor[N]) does not carry. This is the
# embarrassingly-parallel diagonal of the pipeline (the per-quad-point lift). Reachable via
# libceed-quadrature-kernel-impl (pulled-by).
rank: roadmap_goal
edges:
  reference:
    - target: L1/libceed-quadrature-kernel-impl
      kind: pulled-by      # the roadmap_goal consumer whose pipeline composes this pointwise D stage (free)
    - target: L1/geom_factor_build   # produces the geom_data this op contracts against (the setup-stratum factor)
    - target: concepts/tensor-field-lift   # the per-quad-point pointwise contraction IS the diagonal lift this concept describes
---

# quad_point_contract

The **D** stage of the libCEED contraction pipeline
`A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md)):
the **pointwise per-quadrature-point contraction** — apply, *independently at each quadrature point*, the
precomputed `geom_data` (the product of material coefficient `Q`, geometry factor, and quadrature weight)
to the basis-evaluated trial field. This is the **embarrassingly-parallel diagonal** of the pipeline — the
per-quad-point lift that is the natural GPU-tensor form.

## Status

`roadmap_goal` (rank 0). **Clean-gate: ROADMAP_GOAL, not firm/rough-in.** The Palace realization is
exhaustively anchored (the apply-QFunction field wiring + the `f_apply_*` pointwise kernels — see
*Verified-against*), but the operator acts on the **quad-point-rank** tensor `Tensor[(E, P, C)]` (element
axis `E`, quad-point axis `P`, component axis `C`) that the firm flat-vector-BLAS L1 (`Tensor[N]`) does
not carry — a genuine **vocabulary shift** — so the honest disposition is rank-0. Note: the *pointwise*
elementwise-product structure (`⊙`) IS firm L1 vocabulary (`elementwise_product`), but it is firm only
over flat `Tensor[N]`; lifting it to the `[E, P, C]`-shaped diagonal is the substrate gap that keeps this
rank-0. Promotion route: firm when the quad-point-rank substrate (and the geom_data carrier) is firm L1
vocabulary.

## L1 form (the constructive sketch)

Semantic/notation conventions (named shape groups, the elementwise lift) live on
`book/src/design/l4_calculus.md` §1.2.1 — linked, not restated.

    quad_point_contract :: GeomData -> Tensor[(E, P, C)] -> Tensor[(E, P, C')]
        -- D: pointwise, per (e, p): out[e,p,·] = geom_data[e,p] ⊙ in[e,p,·]
        --   E = element count;  P = quadrature points per element;
        --   C = trial value/derivative components;  C' = test components (often = C)
        --   GeomData :: Tensor[(E, P, G)]   the per-quad-point precomputed factor (G = geom-data components)

At each quadrature point `(e, p)` the contraction applies the precomputed `geom_data[e,p]` — which has
**pre-multiplied** the three pointwise factors (the material coefficient `Q` = `ε`/`μ⁻¹`/…, the
Jacobian-derived geometry metric `J⁻ᵀ J⁻¹ |J|` for grad-grad / `|J|` for mass, and the quadrature weight
`w`) into one factor by the separate build pass ([`geom_factor_build`](./geom_factor_build.md)). The
run-time apply is therefore a single pointwise multiply `geom_data ⊙ (basis-evaluated trial)` — no
inter-point coupling. In Palace this is the `f_apply_*` family (`f_apply_22`/`f_apply_33`/…), the
per-`(dim, space_dim)` pointwise apply-QFunctions selected by the active-field component sizes.

This is the **diagonal** of the pipeline: `B G` evaluates the trial field at quad points, `D` weights it
pointwise, `Bᵀ Gᵀ` contracts the weighted field back to the global operator. The pointwise structure is
exactly the per-quad-point lift `concepts/tensor-field-lift` describes — the embarrassingly-parallel,
GPU-natural stage.

## Algebraic laws (sketch — to be confirmed at promotion)

- **Pointwise (no coupling across quadrature points):** `D` is block-diagonal in `(E, P)` — the output at
  `(e, p)` depends only on the input at `(e, p)` and `geom_data[e, p]`. The embarrassingly-parallel law.
- **Linearity in the field:** for fixed `geom_data`, `D(a·u + b·v) = a·D(u) + b·D(v)` — `D` is the
  pointwise elementwise-product lift of `geom_data`, which is linear in its field argument.
- **Self-adjoint when `geom_data` is symmetric/diagonal:** for the mass/grad-grad metrics (symmetric
  positive `geom_data` blocks) the pointwise contraction is self-adjoint — `D = Dᵀ` — which underwrites
  the symmetry of `A = Gᵀ Bᵀ D B G` for self-adjoint terms.
- **Composition with the basis-eval:** `D` consumes `B`'s output shape `Tensor[(E, P, C)]` and emits the
  shape `Bᵀ` consumes — the pipeline shape-congruence law.

## Applicability conditions

1. The pointwise factors are pre-multiplied into `geom_data` by [`geom_factor_build`](./geom_factor_build.md)
   (the setup/run-time stratification): this op is the *run-time apply* half; the build half is separate.
2. The term's `𝒟` fixes the `geom_data` block shape (the `2 + space_dim*dim` geometry-data size) — mass
   (`|J|`) vs grad-grad (`J⁻ᵀ J⁻¹ |J|`).
3. Single-machine (per-`Ceed` device); the pointwise apply has no cross-rank coupling (the diagonal is
   element-local).

## Verified-against

- `palace/fem/libceed/integrator.cpp:451-512` — the apply-QFunction + operator-field wiring:
  `geom_data` input field (`:483-485`), optional `q_w` quad-weight (`:486-490`), active trial inputs /
  test outputs (`AddOperatorActiveInputFields` `:492`, `AddOperatorActiveOutputFields` `:493`) — the
  `B G` (input) / `Bᵀ Gᵀ` (output) field chains around the pointwise `D`.
- `palace/fem/libceed/integrator.cpp:215-308` — `QuadratureDataAssembly` (`:220`) + the `f_apply_*`
  pointwise apply-QFunctions selected by active-field component sizes — the `D` per-quad-point kernels.
- `palace/fem/libceed/integrator.cpp:423-465` — `AssembleCeedOperator` master assembler: the
  `geom_data` / `q_w` inputs that feed the pointwise contraction.
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the roadmap_goal consumer (pulled-by).

## Related

- [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — composes this `D` stage.
- [`geom_factor_build`](./geom_factor_build.md) — the setup-stratum pass that produces the `geom_data`
  this op contracts against.
- [`basis_apply`](./basis_apply.md) — the `B`/`Bᵀ` stages on either side of `D`.
- `concepts/tensor-field-lift` — the per-quad-point lift this op realizes.
- [`elementwise_product`](./elementwise_product.md) — the firm flat-`Tensor[N]` pointwise multiply this
  op generalizes to the `[E, P, C]`-rank diagonal (the substrate gap that keeps it rank-0).

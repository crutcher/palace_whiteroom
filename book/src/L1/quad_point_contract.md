---
layer: L1
operator: quad_point_contract
rank: firm
edges:
  reference:
    - target: L1/libceed-quadrature-kernel-impl
      kind: pulled-by      # the kernel-impl consumer whose pipeline composes this pointwise D stage
    - target: L1/geom_factor_build   # produces the geom_data this op contracts against (the setup-stratum factor)
    - target: concepts/element-local-tensor   # the [E,P,C]/[E,P,G] quad-point rank-tensor this op operates on
    - target: concepts/tensor-field-lift   # the per-quad-point pointwise contraction IS the diagonal lift this concept describes
---

# quad_point_contract

The **D** stage of the libCEED contraction pipeline
`A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md)):
the **pointwise per-quadrature-point contraction** — apply, *independently at each quadrature point*, the
precomputed `geom_data` (the product of material coefficient `Q`, geometry factor, and quadrature weight)
to the basis-evaluated trial field. This is the **embarrassingly-parallel diagonal** of the pipeline — the
per-quad-point lift that is the natural GPU-tensor form.

## L1 form

Semantic/notation conventions (named shape groups, the `(E, P, C)` / `(E, P, G)` element-local rank
structure, the elementwise lift) live on [`book/src/semantics/index.md`](../semantics/index.md) §1.2.1 +
the record page [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) — linked, not
restated.

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

## Algebraic laws

- **Pointwise (no coupling across quadrature points):** `D` is block-diagonal in `(E, P)` — the output at
  `(e, p)` depends only on the input at `(e, p)` and `geom_data[e, p]`. (Syntactic identity: the
  apply-QFunction is invoked per-quadrature-point with no cross-point term.) The embarrassingly-parallel law.
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

## Evidence

- `palace/fem/libceed/integrator.cpp:451-495` — the apply-QFunction + operator-field wiring:
  `geom_data` input field (`:457-458`), optional `q_w` quad-weight (`:462`, `CEED_EVAL_WEIGHT`), active
  trial inputs / test outputs (`AddOperatorActiveInputFields` `:492`, `AddOperatorActiveOutputFields`
  `:493`) — the `B G` (input) / `Bᵀ Gᵀ` (output) field chains around the pointwise `D`.
- `palace/fem/libceed/integrator.cpp:215-308` — `QuadratureDataAssembly` (`:220`) + the `f_apply_*`
  pointwise apply-QFunctions selected by active-field component sizes (`f_apply_22` `:260`) — the `D`
  per-quad-point kernels.
- `palace/fem/libceed/integrator.cpp:423-445` — `AssembleCeedOperator` master assembler (`:423`): the
  `geom_data` / `q_w` inputs that feed the pointwise contraction.
- `book/src/concepts/element-local-tensor.md` — the `(E, P, C)` / `(E, P, G)` quad-point rank-tensor
  shape family this op operates on (the firm L1 data shape).
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the kernel-impl consumer (pulled-by).

## Related

- [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — composes this `D` stage.
- [`geom_factor_build`](./geom_factor_build.md) — the setup-stratum pass that produces the `geom_data`
  this op contracts against.
- [`basis_apply`](./basis_apply.md) — the `B`/`Bᵀ` stages on either side of `D`.
- `concepts/tensor-field-lift` — the per-quad-point lift this op realizes.
- [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) — the `[E, P, C]` / `[E, P, G]`
  element-local rank-tensor shape family (the firm L1 data shape this op operates on).
- [`elementwise_product`](./elementwise_product.md) — the firm flat-`Tensor[N]` pointwise multiply this
  op lifts to the `[E, P, C]`-rank diagonal (now firm L1 vocabulary via the element-local rank-tensor).

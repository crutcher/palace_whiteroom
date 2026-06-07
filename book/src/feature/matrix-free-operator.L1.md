---
kind: feature-surface
feature: matrix-free-operator
level: L1
feature_root: seed
rank: firm
edges:
  depends-on:
    # The four element-local substrate ops this pure-function surface composes BY NAME — the
    # RE11-grounding faithful blocking edges (all firm c124 D3 / c125 D1). This is the L1 surface
    # that names the substrate ops DIRECTLY (the L4 surface names them transitively via the L2 combinator).
    - target: L1/element_restrict
      kind: composes                  # G / Gᵀ — the [(N: ...)] ↔ [E, L] gather / scatter-add (firm c125 D1)
    - target: L1/basis_apply
      kind: composes                  # B_𝒟 / B_𝒟ᵀ — the [E, L] ↔ [E, P, C] basis-eval contraction keyed on 𝒟 (firm c124 D3)
    - target: L1/quad_point_contract
      kind: composes                  # D — the pointwise [E, P, C] per-quad-point diagonal against [E, P, G] (firm c124 D3)
    - target: L1/geom_factor_build
      kind: composes                  # the [E, P, G] geometry-factor carrier D contracts against (firm c125 D1)
    - target: palace/fem/libceed/operator.cpp:182-189
      kind: cites-evidence            # Operator::Mult — the whole-operator apply (the pure contraction-chain action read as tensor-in/tensor-out)
  reference:
    - feature/matrix-free-operator.L4
    - L1/libceed-quadrature-kernel-impl   # the kernel-impl whose concrete contraction chain this pure-function surface renders (firm c125 D1)
    - concepts/element-local-tensor       # the rank-structured shape family the chain is typed over (firm c124 D5)
---

# matrix-free operator — L1 composition-root

The **matrix-free FE operator** presented at L1 as the pure-function rendering of the element-local
contraction chain — the mutation-rotated form of the `ceed::Operator` apply
(`palace/fem/libceed/operator.cpp:182-189`), where the in-place vector mutations (the `CeedAddMult`
accumulation into `y`, the `dof_multiplicity` post-scale) are re-expressed as pure tensor-in /
tensor-out functions threaded through the five-stage chain. This is the infrastructure /
shared-substrate column at L1; it composes the four firm L1 substrate ops directly into the
contraction-chain action and links DOWN to each piece. The L4 surface
([`matrix-free-operator.L4`](./matrix-free-operator.L4.md)) carries the full composition narrative
(the constructor cap + the L2 combinator); this L1 surface is the pure-function shape the L4
composition lowers onto — and the surface whose blocking `depends-on` edges to the four substrate
ops GROUND the RE11 libceed-substrate sub-cohort.

## The pure contraction chain

The matrix-free apply is a **pure composition of the four element-local substrate ops** over the
[`element-local-tensor`](../concepts/element-local-tensor.md) shape family (the rank-structured
`[(N: ...)]`/`[E, L]`/`[E, P, C]`/`[E, P, G]` axes — the genuine vocabulary shift away from the flat
`Tensor[N]` BLAS-1 vector):

    -- the matrix-free operator's apply, pure (no in-place mutation)
    apply :: ElemRestriction -> Basis -> GeomData -> Coefficient
          -> Tensor[(N: ...)] -> Tensor[(N: ...)]
    apply restr basis geom Q v =
        v   |> element_restrict restr                  -- G   :: [(N: ...)] -> [E, L]
            |> basis_apply (mode-of 𝒟) basis           -- B_𝒟 :: [E, L]    -> [E, P, C]
            |> quad_point_contract geom Q               -- D   :: [E, P, C] -> [E, P, C]  (pointwise, against [E, P, G])
            |> basis_apply (transpose (mode-of 𝒟)) basis -- B_𝒟ᵀ :: [E, P, C] -> [E, L]
            |> element_restrict_transpose restr         -- Gᵀ  :: [E, L]    -> [(N: ...)]  (scatter-ADD)

That is the pure-function form of `A = Gᵀ ∘ B_𝒟ᵀ ∘ D(Q, geom) ∘ B_𝒟 ∘ G`. Four composed pieces,
each a firm L1 link:

1. **Element gather/scatter-add** — [`element_restrict`](../L1/element_restrict.md) (firm c125 D1).
   `G` gathers global dofs to per-element-local dofs `[E, L]`; `Gᵀ` scatters-**adds** back to the
   shared global dofs (the element-additivity of the assembled action). The only inter-dof transfer.
2. **Basis-eval contraction** — [`basis_apply`](../L1/basis_apply.md) (firm c124 D3). `B_𝒟` contracts
   the tabulated basis against the element-local dofs to per-quad-point values `[E, P, C]`, keyed on
   the term's differential-operator 𝒟 (Identity/Gradient/Curl/Divergence selects the EvalMode);
   `B_𝒟ᵀ` is the adjoint. (Sum-factorization on tensor-product elements is a transparent performance
   trick below this resolution — a one-line note in `basis_apply`, not a separate form.)
3. **Pointwise quad-point diagonal** — [`quad_point_contract`](../L1/quad_point_contract.md)
   (firm c124 D3). `D` is the embarrassingly-parallel per-quad-point contraction of the value tensor
   against the `[E, P, G]` geometry carrier and the coefficient `Q`.
4. **Geometry-factor carrier** — [`geom_factor_build`](../L1/geom_factor_build.md) (firm c125 D1).
   The build-stratum `[E, P, G]` Jacobian / detJ / adjJ carrier `D` contracts against (fixed once per
   mesh/order/quadrature).

The whole-operator action is `apply` followed by the optional `dof_multiplicity` post-scale
(shared-dof averaging; read single-rank per §Scope) — `Operator::Mult`
(`palace/fem/libceed/operator.cpp:182-189`: `y = 0; CeedAddMult(...); y *= dof_multiplicity`).

This L1 surface **already states the same chain** the L1
[`libceed-quadrature-kernel-impl`](../L1/libceed-quadrature-kernel-impl.md) renders concretely — the
relationship is identity-in-named-terms (both name the same composition of the same four verbs over
the same shape family); recorded here as a `reference`-class link, not a separate theme (the genuine
vocabulary shift is the OTHER edge — flat-`Tensor[N]` → element-local-tensor — carried by the
substrate ops' own L1>L0 rotations).

## Status

`firm` (landed firm cycle-127 D1) — the L1 pure-function surface of the infrastructure /
shared-substrate matrix-free operator column. `feature_root: seed` preserved. Firm on the same
well-foundedness basis as the [L4 surface](./matrix-free-operator.L4.md): all four blocking
`depends-on` substrate constituents are firm on disk (`element_restrict` + `geom_factor_build`
c125 D1; `basis_apply` + `quad_point_contract` c124 D3), typed over the firm
[`element-local-tensor`](../concepts/element-local-tensor.md) shape family (c124 D5). The apply is
the mutation-rotated pure rendering of `operator.cpp:182-189`; the contraction chain is a fixed
five-stage composition with no loop obstruction (the element/quad-point axes are
map-reduce-parallel, not a sequential recurrence) — firm-on-positive-structure. **This L1 surface's
four blocking `depends-on (composes)` edges are the faithful root-reaching consumer that GROUNDS the
RE11 libceed-substrate sub-cohort** — a REAL composition flip, not a `reference`-only hop.
Evidence: `operator.cpp:182-189` + the four firm substrate-op down-links.

---
kind: navigational-container (sub-chapter group intro)
# Sub-chapter group intro, not a DAG node: no `rank:`; only `reference` edges
# to the chapters it groups (scheme §4/§5).
edges:
  reference:
    - L2/matrix-free-operator-apply
---

# Constructive-kernel compositions

The L2 cohort of **named contraction-chain compositions** — compositions of the firm element-local
contraction substrate (`element_restrict` / `basis_apply` / `quad_point_contract` /
`geom_factor_build`) over the rank-structured [`element-local-tensor`](../concepts/element-local-tensor.md)
shape family. This is the **burn/GPU matrix-free backend-lowering surface**: a sequence of tensor
contractions over the element axis `E` and quad-point axis `P`, the form whose semantics match the
GPU-tensor backend directly.

It is a **distinct cohort** from the other L2 groupings (fold combinators, named compositions,
elementwise / gate floors), all of which compose flat-`Tensor[N]` BLAS-1 / solver verbs. The
constructive-kernel compositions are the one place L2 vocabulary lives over the *rank-structured*
element-local family rather than the flat global dof-vector — the genuine vocabulary shift that
`concepts/element-local-tensor` records.

## Members

- [`matrix-free-operator-apply`](./matrix-free-operator-apply.md) — the named contraction-chain
  combinator for matrix-free FE operator application `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`, the L2 home of
  the five-stage pipeline the L1 [`libceed-quadrature-kernel-impl`](../L1/libceed-quadrature-kernel-impl.md)
  realizes and the [`fe_assemble`](../L1/fe_assemble.md) fold sums per-term. (Firm cycle-125 D2.)

Future members would join here as the element-local composition vocabulary deepens (e.g. an L2
term-fold of `fe_assemble`, a named sum-factorized basis-application sub-combinator, or the L4
backend-lowering operator constructor's L2 shadow).

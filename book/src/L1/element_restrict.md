---
layer: L1
operator: element_restrict
# Graded-stack: roadmap_goal (rank 0). One of the four libCEED contraction-substrate ops the
# `libceed-quadrature-kernel-impl` roadmap_goal (c121-D4) declares as depends-on targets. It is the
# G / Gᵀ stage of A = Gᵀ B_𝒟ᵀ D B_𝒟 G. Rank-0 because it operates on RANK-STRUCTURED element-local
# tensors (Tensor[(E, L)]) that our firm flat-vector-BLAS L1 vocabulary (Tensor[N]) does not carry —
# a genuine vocabulary shift, not a re-expression. A roadmap_goal may rest on anything (rank invariant
# rank(u) <= rank(v) is vacuous at rank 0). Reachable: pulled-by libceed-quadrature-kernel-impl, which
# reaches the feature root via the fe_assemble fold's 7 feature-column inbound edges.
rank: roadmap_goal
edges:
  reference:
    - target: L1/libceed-quadrature-kernel-impl
      kind: pulled-by      # the roadmap_goal consumer whose A = Gᵀ B_𝒟ᵀ D B_𝒟 G pipeline composes this G/Gᵀ stage (free; this node does not depend on its consumer)
    - target: concepts/tensor-field-lift   # Gᵀ scatter-add (assembly) is the element->global lift this substrate targets
---

# element_restrict

The **G / Gᵀ** stage of the libCEED element-quadrature contraction pipeline
`A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md)):
the **element restriction** — a pure gather/scatter that maps the global true-dof vector to per-element
local-dof tensors (`G`, gather) and back by transpose scatter-add (`Gᵀ`, assembly). No arithmetic; it
is the indexing/permutation backbone of matrix-free FE operator application.

## Status

`roadmap_goal` (rank 0). **The clean-gate call is ROADMAP_GOAL, not firm/rough-in.** The Palace
realization is exhaustively anchored (see *Verified-against* — `CeedElemRestriction` construction and
its index-map builder), but the operator's signature contracts over a **rank-structured element-local
tensor** `Tensor[(E, L)]` (element axis `E`, local-dofs-per-element axis `L`) that **no firm L1
operator carries**: our firm L1 algebra is flat-vector BLAS-1/2 over `Tensor[N]` (the
`space.GetTrueVSize()` true-dof axis). Introducing the `[E, L]` element-rank structure is a genuine
**vocabulary shift**, so the honest disposition is rank-0 — it carries the constructive sketch and the
named shape groups, with NO claim that the rank-structured substrate exists in firm L1 vocabulary.
Promotion route: once the element-rank tensor substrate is firm L1 vocabulary, this promotes
`roadmap_goal → rough-in → firm` on the usual gates, and the consumer
`libceed-quadrature-kernel-impl`'s `depends-on` edge to it becomes firm-resting.

## L1 form (the constructive sketch)

For semantic/notation conventions (named shape groups, `Tensor[(S: ...)]` binding vs `Tensor[$S]`
use), see the governing surface `book/src/design/l4_calculus.md` §1.2.1 — not restated here.

    element_restrict :: ElemRestriction -> Tensor[(N: ...)] -> Tensor[(E, L)]
        -- G   (gather):  global true-dof vector -> per-element local-dof tensor
    element_restrict_t :: ElemRestriction -> Tensor[(E, L)] -> Tensor[(N: ...)]
        -- Gᵀ  (scatter-add / assembly): per-element local-dof tensor -> global true-dof vector
        --   N = space true-dof axis (flat, the firm Tensor[N] dof-vector — KEPT flat per L1/L0 convention)
        --   E = element count;  L = local dofs per element

`G` is a pure **gather**: it reads each element's local dofs from the shared global vector through the
element's local-dof → global-dof index map (built once per `(space, element-geometry)` pair). `Gᵀ` is
the **transpose scatter-add**: it sums each element-local contribution into its global slot — the
*assembly* operation (shared dofs at element boundaries receive a sum). The two are exact transposes:
`Gᵀ` is the adjoint of `G` under the standard inner products (no arithmetic beyond the scatter-add
accumulation).

The flat global axis `N` stays a genuine rank-1 `Tensor[(N: ...)]` dof-vector (the firm L1 `Tensor[N]`
convention for Palace `Vector` — KEPT flat). The element-local side `Tensor[(E, L)]` is the new
rank-structured axis this op introduces (the vocabulary shift). On a tensor-product element `L`
itself factors as a per-dimension dof product, but that factoring is an interior detail of `basis_apply`
(the sum-factorization sub-axis), not of the restriction.

## Algebraic laws (sketch — to be confirmed at promotion)

- **Transpose/adjoint pair:** `⟨G x, y⟩_{(E,L)} = ⟨x, Gᵀ y⟩_N` — `element_restrict_t` is the exact
  adjoint of `element_restrict` (the gather and the scatter-add are transposes of the same Boolean
  index map).
- **Gather is linear and a Boolean selection:** `G` carries no arithmetic; each output entry equals
  exactly one input entry (a 0/1 selection matrix), so `G (a·x + b·y) = a·(G x) + b·(G y)`.
- **`Gᵀ G` is the dof-multiplicity diagonal:** `Gᵀ G` acts on the global vector as multiplication by
  each true-dof's element-incidence count (the number of elements sharing that dof) — NOT the identity
  (shared dofs are counted with multiplicity). This is the standard FE assembly-multiplicity relation.
- **`G Gᵀ` is NOT the identity** on the element-local side (it averages-then-redistributes across the
  shared-dof equivalence classes) — stated as a non-law to forestall the false `G Gᵀ = I` assumption.

These are the standard restriction/prolongation algebra; they are sketched (not asserted firm) pending
the firm element-rank substrate.

## Applicability conditions

1. A standard FE basis with a tabulated `CeedElemRestriction` (the de-Rham family axis of
   [`weak_form_term`](./weak_form_term.md)); the lexicographic-vs-native ordering branch
   (`InitLexicoRestr` / `InitNativeRestr`) is an interior detail of the index-map construction.
2. Single-machine (per-`Ceed` device): the multi-rank shared-dof overlap (`ParMesh` assembly) is read
   single-rank per CLAUDE.md §Scope (DIRECTIVE-1 boundary) — the cross-rank scatter-add reconciliation
   is a deferred future direction, not lifted here.

## Verified-against

- `palace/fem/libceed/restriction.cpp:389-425` — `InitRestriction`: the element-restriction builder;
  dispatches lexicographic (`InitLexicoRestr`, `:113`) vs native (`InitNativeRestr`, `:207`) ordering
  for the local-dof → global-dof index map.
- `palace/fem/libceed/restriction.cpp:200` — `CeedElemRestrictionCreate(...)` — the libCEED restriction
  object built from the index map (the `G` realization; oriented variant `CeedElemRestrictionCreateOriented`
  at `:192`/`:372` for sign-carrying H(curl)/H(div) dofs).
- `palace/fem/bilinearform.cpp:64-70` — `trial_restr`/`test_restr` (`:64`/`:66`): the `G` operands the
  assembler receives (`GetCeedElemRestriction`); the per-element gather inputs to the leaf kernel.
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the roadmap_goal consumer whose pipeline
  `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` composes this `G`/`Gᵀ` stage (pulled-by).

## Related

- [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the roadmap_goal that
  composes this stage (the `G`/`Gᵀ` ends of the pipeline).
- [`basis_apply`](./basis_apply.md) — the `B`/`Bᵀ` stage applied AFTER `G` (and before `Gᵀ`).
- `concepts/tensor-field-lift` — `Gᵀ` (assembly) is the element→global lift this substrate targets.

---
layer: L4
operator: mk_matrix_free_operator
kind: backend-lowering-operator-constructor
status: roadmap_goal
rank: roadmap_goal
edges:
  reference:
    # The firm L2 contraction-chain combinator this op's `apply` lowers to (free, navigational —
    # the L4 op is the operator-CONSTRUCTOR surface; the L2 combinator is the apply-chain COMPOSITION
    # `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` it produces. A `roadmap_goal` may rest on / reference anything;
    # this is `reference`-class so it neither constrains rank nor blocks — scheme §1g).
    - target: L2/matrix-free-operator-apply
      kind: lowers-to
    # The firm spine consumer that PULLS this op to a feature root (the reachability / not-garbage edge).
    # `fe_assemble` reaches the feature root via its 7 feature-column inbound edges; the matrix-free
    # representation IS the constructive interior of its per-term `assemble_term` leaf under the
    # matrix-free (`UseFullAssembly` false) dispatch. This edge is the INBOUND mirror of the
    # `fe_assemble → mk_matrix_free_operator` `reference` (constructs-via) edge added in fe_assemble's
    # frontmatter — recorded both ways for navigation; a firm node referencing a rank-0 roadmap_goal
    # via `reference` is permitted (it must NOT `depends-on` it — that would violate well-foundedness).
    - target: L4/fe_assemble
      kind: pulled-by
    # The firm L4 fold whose per-term leaf this op specializes (same consumer, the construct-via role).
    - target: L4/index
    - target: concepts/element-local-tensor
    - target: concepts/black-box-vs-accelerated-kernels
    - target: semantics/index
variant_axes:
  - assembly-representation (partial matrix-free `ceed::Operator` / full materialized `HypreCSRMatrix` — the `UseFullAssembly` order-threshold dispatch, `palace/fem/bilinearform.cpp:118,:143`; this op IS the `partial` branch — the un-materialized representation, the `full` branch being the `CeedOperatorFullAssemble` CSR materialization, `palace/fem/libceed/operator.hpp:81-82`)
  - differential-operator (the `WeakFormTerm`'s 𝒟 — ∇/Gradient, ∇×/Curl, I/mass — selecting the `B_𝒟` basis EvalMode; leaf content, absorbed as it is in `fe_assemble`/`matrix-free-operator-apply`)
---

# mk_matrix_free_operator

> **⟢ backend-lowering-operator-constructor.** The L4 constructor that builds a **matrix-free (un-materialized) linear operator** from an FE space and a weak-form term — the operator whose `apply` is the burn/GPU tensor-contraction graph rather than a materialized matrix-vector product. This is the L4 surface the outward backend wants (DIRECTIVE-1: L4 is the outward backend-lowering target) for the `assembly-representation: partial matrix-free` axis that [`fe_assemble`](./fe_assemble.md) absorbs (`L4/fe_assemble.md:16,:166`).

> **⟢ roadmap_goal (rank 0) — claim-free intent.** This chapter carries **no positive Palace-source claim** about a named L4 `mk_matrix_free_operator` constructor. It is the intent node for the L4 backend-lowering operator-constructor whose `apply` lowers to the firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) contraction chain. Everything below the §Intent line is a **speculative reconstruction** in our L4 vocabulary, explicitly flagged; nothing here is asserted as Palace source. Pulled by the firm [`fe_assemble`](./fe_assemble.md) spine consumer (the reachability edge to a feature root). Promotes `roadmap_goal → rough-in → firm` as the dedicated L4 backend-lowering feature surface lands (batch-41 "A") and provides the blocking pull-chain that licenses a non-speculative claim.

## Intent

What this becomes: a `firm` L4 operator `mk_matrix_free_operator` — the **operator-constructor** half of the matrix-free FE story. Where [`fe_assemble`](./fe_assemble.md) is the assemble-fold combinator (`K = Σ_t assemble_term(space, t)`) that *sums* per-term contributions, and its per-term leaf `assemble_term` rises as an **opaque black-box-kernel input** (libCEED-owned), `mk_matrix_free_operator` is the **constructive interior** of that leaf under the matrix-free dispatch: instead of treating `assemble_term` as opaque, it constructs the per-term linear operator as a **representation that defers materialization** — the `partial matrix-free ceed::Operator` branch of Palace's order-threshold `UseFullAssembly` dispatch (`palace/fem/bilinearform.cpp:143`). Its `apply` does NOT touch a materialized matrix; it runs the element-local tensor-contraction chain `A·v = Gᵀ (B_𝒟ᵀ (D ⊙ (B_𝒟 (G·v))))` — the firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) combinator. This is the L4 op a GPU/burn backend instantiates: a `LinearOperator` value whose action is a contraction graph, not a CSR spmv.

The two representations Palace already carries are the **variant axis** this op makes structural: the matrix-free `ceed::Operator` (the wrapper `palace/fem/libceed/operator.hpp:32`, sub-operators added by `AddSubOperator` `:48`) is the un-materialized form `mk_matrix_free_operator` builds; `CeedOperatorFullAssemble` (`:81-82`) is the alternative CSR materialization (the `full` branch). The L4 form is **representation-agnostic in its signature** (the variant axis absorbs the partial/full choice, inherited from `L4/fe_assemble.md:166` + `L1/fe_assemble.md:182-187`) — `mk_matrix_free_operator` names specifically the *partial / un-materialized* constructor that the backend-lowering target wants.

## Speculative L4 form (the constructor signature + apply-lowering)

> **SPECULATIVE** — a reconstruction in our L4 vocabulary; not asserted as Palace source. Refine against evidence as the backend-lowering surface firms.

Signature (per the c125 D2 OQ placeholder, refined to the project's named-shape-group notation per [`semantics/index`](../semantics/index.md) §1.2 — the operator-domain shape group `(N: ...)` is the rank-structured DOF axis family, NOT a flat `Tensor[N]`; this is the genuine vocabulary shift the [`element-local-tensor`](../concepts/element-local-tensor.md) family carries away from the BLAS-1 flat vector):

    mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])
    -- FESpace      : the finite-element space (the `readonly` construction stratum `fe_assemble` captures once)
    -- WeakFormTerm : (Q, 𝒟) — coefficient Q + differential operator 𝒟; selects the basis EvalMode B_𝒟
    -- GeomFactors  : the build-stratum [E, P, G] geometry-factor carrier (the firm `geom_factor_build` product)
    -- result       : a LinearOperator whose `apply` is the contraction chain (un-materialized)

The apply lowers to the firm L2 contraction-chain combinator (the `reference`-class `lowers-to` edge):

    apply (mk_matrix_free_operator space term geom) v
      = matrix-free-operator-apply space term geom v          -- the firm L2 combinator
      = (Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G) v                          -- the five-stage contraction chain

where (per [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md)) `G`/`Gᵀ` is `element_restrict` (the `[(N: ...)] ↔ [E, L]` gather / scatter-add), `B_𝒟`/`B_𝒟ᵀ` is `basis_apply` (the `[E, L] ↔ [E, P, C]` basis-eval contraction keyed on 𝒟), and `D` is `quad_point_contract` (the pointwise `[E, P, C]` per-quad-point diagonal against the `[E, P, G]` geometry carrier `GeomFactors`). The L4 op is the **operator-constructor surface**; the L2 combinator is the **apply-chain composition** it produces — the constructor/apply split is the GPU-backend-relevant factoring (build the contraction graph once at construction; run it per `apply`).

## Pull-chain (reachability — why this is not garbage)

This `roadmap_goal` is reachable from a feature root by ONE `reference`-class hop:

- **Inbound (pull-to-root):** firm [`fe_assemble`](./fe_assemble.md) gains a `reference`-class (`kind: constructs-via`) down-edge → `mk_matrix_free_operator` (added to `fe_assemble`'s frontmatter + §Lowers-to prose this dispatch). `fe_assemble` reaches the feature root via its 7 feature-column inbound edges; the matrix-free representation IS the constructive interior of its per-term `assemble_term` leaf under the `UseFullAssembly`-false dispatch. The edge is **`reference`, NOT `depends-on`** — a firm node may *navigationally reference* a rank-0 roadmap_goal, but must NOT carry a *blocking* `depends-on` to it (that would violate well-foundedness `rank(fe_assemble) = firm > rank(mk_matrix_free_operator) = 0`). The `reference` edge carries no liveness constraint and constrains no rank (scheme §1g) — so `rank_violations` stays 0.
- **Downward (lowers-to):** `mk_matrix_free_operator` → firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md), `reference`-class `lowers-to`. The L4 op's apply is the named L2 contraction chain; the L2 combinator (firm, c125 D2) composes the four firm element-local substrate ops (`element_restrict` / `basis_apply` / `quad_point_contract` / `geom_factor_build`). A `roadmap_goal` may rest on / reference anything — but recorded as `reference` (not `depends-on`) so the rank-0 node imposes no rank floor on the firm L2 combinator.

## Speculative L4 operators proposed (none new)

This cap proposes **no new speculative operator** beyond itself: `mk_matrix_free_operator` IS the speculative L4 op (landed as the `roadmap_goal` chapter, the in-discipline home). Its declared dependencies are all already firm on disk — the L2 combinator and the four L1 substrate ops below it. The intent's only open work is the *upward* pull (the dedicated L4 backend-lowering feature surface, batch-41 "A") that would firm this node.

## Declared dependencies (all firm — the well-foundedness it WILL rest on when firmed)

When this promotes off `roadmap_goal`, its blocking deps will be (currently recorded as `reference` because rank-0 imposes nothing):

- [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) — firm (c125 D2); the apply-chain composition.
- (transitively, via the L2 combinator) `L1/element_restrict`, `L1/basis_apply`, `L1/quad_point_contract`, `L1/geom_factor_build` — all firm (c124 D3 / c125 D1).
- [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) — firm (c124 D5); the rank-structured shape family `(N: ...)`/`[E, L]`/`[E, P, C]`/`[E, P, G]` the chain is typed over.

## L0 anchors (construction-site evidence — speculative-intent, not a positive L4 claim)

The matrix-free *representation* this L4 op names is grounded at:

- `palace/fem/libceed/operator.hpp:32` — `class Operator : public palace::Operator`, the `ceed::Operator` matrix-free wrapper (the un-materialized representation this constructor builds).
- `palace/fem/libceed/operator.hpp:48` — `AddSubOperator(CeedOperator sub_op, ...)`, the per-term sub-operator accumulation (the constructor's per-`WeakFormTerm` build step).
- `palace/fem/libceed/operator.hpp:81-82` — `CeedOperatorFullAssemble(const Operator &op, ...)`, the matrix-free → CSR materialization (the *alternative* `full` representation the variant axis absorbs).
- `palace/fem/bilinearform.cpp:118` — `UseFullAssembly(const FiniteElementSpace &trial_fespace, ...)`, the order-threshold dispatch predicate.
- `palace/fem/bilinearform.cpp:143` — `if (UseFullAssembly(...))` in `BilinearForm::Assemble`, the partial-matrix-free-vs-full-materialized branch (this op IS the `else` / `PartialAssemble` branch).

All five self-verified against on-disk source this dispatch via `citecheck --anchor` (all `[ok]`).

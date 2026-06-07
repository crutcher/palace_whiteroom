---
layer: L4
operator: mk_matrix_free_operator
kind: backend-lowering-operator-constructor
status: firm
rank: firm
edges:
  depends-on:
    # The firm L2 contraction-chain combinator this op's `apply` lowers to. Promoted from
    # `reference (lowers-to)` to `depends-on (lowers-to)` at the c127 D1 firm-flip: now that this
    # op is FIRM, its `apply` genuinely BLOCKING-depends-on the firm L2 contraction chain
    # `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`. firm→firm, rank-legal (rank(u) ≤ min(deps) = firm — §1g).
    - target: L2/matrix-free-operator-apply
      kind: lowers-to
  reference:
    # The firm spine consumer that PULLS this op to a feature root (the reachability / not-garbage edge).
    # `fe_assemble` reaches the feature root via its 7 feature-column inbound edges; the matrix-free
    # representation IS the constructive interior of its per-term `assemble_term` leaf under the
    # matrix-free (`UseFullAssembly` false) dispatch. STAYS `reference` (constructs-via) — fe_assemble
    # folds the leaf OPAQUELY (its firmness is in the fold apparatus, not the leaf interior), so it must
    # NOT `depends-on` this op even now both are firm; a firm→firm navigational reference is fine.
    - target: L4/fe_assemble
      kind: pulled-by
    # The dedicated L4 backend-lowering feature surface that composes this constructor cap by name and
    # FIRMED it off roadmap_goal (the named promotion condition; c127 D1). This is the inbound
    # blocking `depends-on (composes)` pull recorded as the column's edge; mirrored here for navigation.
    - target: feature/matrix-free-operator.L4
      kind: pulled-by
    # The L4>L3 down-narrative theme dissolving this constructor's apply into the L3 contraction-chain
    # view (authored c127 D2).
    - target: L4-L3/mk-matrix-free-operator-dissolution
      kind: lowers-to
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

> **⟢ firm (rank 3) — promoted off roadmap_goal cycle-127 D1.** This chapter now carries a positive *compositional* claim: `mk_matrix_free_operator` is the L4 operator-constructor for the matrix-free (un-materialized) FE linear operator — the `partial matrix-free` (`UseFullAssembly`-false) branch of Palace's order-threshold assembly dispatch (`palace/fem/bilinearform.cpp:147`, `PartialAssemble()`), whose `apply` IS the firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) contraction chain `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`. **Promotion basis (the §1g well-foundedness check):** all blocking deps are firm (the L2 combinator c125 D2 + transitively the four firm L1 substrate ops), `min(deps) = firm`; the constructor + apply composition algebra is exhaustively cited (no loop / recurrence obstruction in the constructor surface — a fixed five-stage chain, firm-on-positive-structure escape); and the dedicated L4 backend-lowering feature surface [`feature/matrix-free-operator.L4`](../feature/matrix-free-operator.L4.md) (c127 D1) now PULLS it via a faithful blocking `depends-on (composes)` edge — the cap's previously-recorded promotion condition, met without forcing the spine. The constructor signature + apply-lowering below are now the *asserted* L4 form, not a speculative reconstruction.

## Intent

What this becomes: a `firm` L4 operator `mk_matrix_free_operator` — the **operator-constructor** half of the matrix-free FE story. Where [`fe_assemble`](./fe_assemble.md) is the assemble-fold combinator (`K = Σ_t assemble_term(space, t)`) that *sums* per-term contributions, and its per-term leaf `assemble_term` rises as an **opaque black-box-kernel input** (libCEED-owned), `mk_matrix_free_operator` is the **constructive interior** of that leaf under the matrix-free dispatch: instead of treating `assemble_term` as opaque, it constructs the per-term linear operator as a **representation that defers materialization** — the `partial matrix-free ceed::Operator` branch of Palace's order-threshold `UseFullAssembly` dispatch (`palace/fem/bilinearform.cpp:143`). Its `apply` does NOT touch a materialized matrix; it runs the element-local tensor-contraction chain `A·v = Gᵀ (B_𝒟ᵀ (D ⊙ (B_𝒟 (G·v))))` — the firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) combinator. This is the L4 op a GPU/burn backend instantiates: an `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` operator-value (a closure carrying closed-over params, applied via `apply` — the operator-VALUE spelling of [`semantics/index`](../semantics/index.md) §1.3.1) whose action is a contraction graph, not a CSR spmv.

The two representations Palace already carries are the **variant axis** this op makes structural: the matrix-free `ceed::Operator` (the wrapper `palace/fem/libceed/operator.hpp:32`, sub-operators added by `AddSubOperator` `:48`) is the un-materialized form `mk_matrix_free_operator` builds; `CeedOperatorFullAssemble` (`:81-82`) is the alternative CSR materialization (the `full` branch). The L4 form is **representation-agnostic in its signature** (the variant axis absorbs the partial/full choice, inherited from `L4/fe_assemble.md:166` + `L1/fe_assemble.md:182-187`) — `mk_matrix_free_operator` names specifically the *partial / un-materialized* constructor that the backend-lowering target wants.

## L4 form (the constructor signature + apply-lowering)

> **FIRM** — the asserted L4 form (promoted off speculative c127 D1). The signature + apply-lowering below are the L4 rendering of the positively-cited `partial matrix-free` constructor + its contraction-chain apply.

Signature (in the project's named-shape-group notation per [`semantics/index`](../semantics/index.md) §1.2 — the operator-domain shape group `(N: ...)` is the rank-structured DOF axis family, NOT a flat `Tensor[N]`; this is the genuine vocabulary shift the [`element-local-tensor`](../concepts/element-local-tensor.md) family carries away from the BLAS-1 flat vector). The codomain is written in the **operator-VALUE spelling** `Op[τ_in → τ_out]` per the closure-returning-signature convention ([`semantics/index`](../semantics/index.md) §1.3.1) — `mk_matrix_free_operator` is a *constructor* whose product is an **operator instance** carrying closed-over params (the FE space / geometry-factor / basis tables) and applied later via `apply` (the apply-lowering below), so its higher-order intent is made explicit rather than hidden behind an opaque record-applied-to-type:

    mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> Op[Tensor[(N: ...)] → Tensor[(N: ...)]]
    -- FESpace      : the finite-element space (the `readonly` construction stratum `fe_assemble` captures once)
    -- WeakFormTerm : (Q, 𝒟) — coefficient Q + differential operator 𝒟; selects the basis EvalMode B_𝒟
    -- GeomFactors  : the build-stratum [E, P, G] geometry-factor carrier (the firm `geom_factor_build` product)
    -- result       : an `Op` value (operator instance) whose closed-over params are [FESpace, WeakFormTerm, GeomFactors]
    --                and whose body lambda `\v -> apply … v` is the (un-materialized) contraction chain

The apply lowers to the firm L2 contraction-chain combinator (the `depends-on (lowers-to)` edge — promoted from `reference` at the c127 D1 firm-flip; firm→firm, rank-legal):

    apply (mk_matrix_free_operator space term geom) v
      = matrix-free-operator-apply space term geom v          -- the firm L2 combinator
      = (Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G) v                          -- the five-stage contraction chain

where (per [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md)) `G`/`Gᵀ` is `element_restrict` (the `[(N: ...)] ↔ [E, L]` gather / scatter-add), `B_𝒟`/`B_𝒟ᵀ` is `basis_apply` (the `[E, L] ↔ [E, P, C]` basis-eval contraction keyed on 𝒟), and `D` is `quad_point_contract` (the pointwise `[E, P, C]` per-quad-point diagonal against the `[E, P, G]` geometry carrier `GeomFactors`). The L4 op is the **operator-constructor surface**; the L2 combinator is the **apply-chain composition** it produces — the constructor/apply split is the GPU-backend-relevant factoring (build the contraction graph once at construction; run it per `apply`).

## Pull-chain (reachability — why this is firm and not garbage)

Now firm, this op is reachable from a feature root by a faithful **blocking `depends-on`** inbound edge:

- **Inbound (pull-to-root, BLOCKING):** the firm feature surface [`feature/matrix-free-operator.L4`](../feature/matrix-free-operator.L4.md) (c127 D1) carries a `depends-on (composes)` edge → `mk_matrix_free_operator`. firm→firm, rank-legal (`rank(column) = firm ≤ rank(cap) = firm`). This is the faithful blocking pull that licenses the firm claim — the cap's previously-recorded promotion condition, now met.
- **Inbound (navigational):** firm [`fe_assemble`](./fe_assemble.md) keeps its `reference`-class (`kind: constructs-via`) down-edge → `mk_matrix_free_operator`. STAYS `reference`, NOT `depends-on` — `fe_assemble` folds its per-term `assemble_term` leaf OPAQUELY (its firmness is in the fold apparatus, not the leaf interior), so it must not blocking-depend on the constructor even now both are firm. A firm→firm navigational reference is permitted (scheme §1g).
- **Downward (lowers-to, BLOCKING):** `mk_matrix_free_operator` → firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md), now `depends-on (lowers-to)` (promoted from `reference` at the firm-flip). The op's `apply` IS the named L2 contraction chain; the L2 combinator (firm, c125 D2) composes the four firm element-local substrate ops. firm→firm, rank-legal — `rank_violations` stays 0.

## L4 operators proposed (none new)

This cap proposes **no new operator** beyond itself: `mk_matrix_free_operator` is the L4 backend-lowering operator-constructor. Its dependencies are all firm on disk — the L2 combinator and (transitively) the four L1 substrate ops below it. The *upward* pull that firmed this node (the dedicated L4 backend-lowering feature surface, batch-41 "A") landed c127 D1.

## Blocking dependencies (all firm — the well-foundedness this rests on)

Now firm, its blocking deps are (the L2 combinator recorded `depends-on (lowers-to)`; the four substrate ops reached transitively through it):

- [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) — firm (c125 D2); the apply-chain composition.
- (transitively, via the L2 combinator) `L1/element_restrict`, `L1/basis_apply`, `L1/quad_point_contract`, `L1/geom_factor_build` — all firm (c124 D3 / c125 D1).
- [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) — firm (c124 D5); the rank-structured shape family `(N: ...)`/`[E, L]`/`[E, P, C]`/`[E, P, G]` the chain is typed over.

## L0 anchors (construction-site evidence — the positive compositional claim)

The matrix-free *representation* this L4 op names is grounded at:

- `palace/fem/libceed/operator.hpp:32` — `class Operator : public palace::Operator`, the `ceed::Operator` matrix-free wrapper (the un-materialized representation this constructor builds).
- `palace/fem/libceed/operator.hpp:48` — `AddSubOperator(CeedOperator sub_op, ...)`, the per-term sub-operator accumulation (the constructor's per-`WeakFormTerm` build step).
- `palace/fem/libceed/operator.hpp:81-82` — `CeedOperatorFullAssemble(const Operator &op, ...)`, the matrix-free → CSR materialization (the *alternative* `full` representation the variant axis absorbs).
- `palace/fem/bilinearform.cpp:118` — `UseFullAssembly(const FiniteElementSpace &trial_fespace, ...)`, the order-threshold dispatch predicate.
- `palace/fem/bilinearform.cpp:143` — `if (UseFullAssembly(...))` in `BilinearForm::Assemble`, the partial-matrix-free-vs-full-materialized branch (this op IS the `else` / `PartialAssemble` branch).

All five self-verified against on-disk source this dispatch via `citecheck --anchor` (all `[ok]`).

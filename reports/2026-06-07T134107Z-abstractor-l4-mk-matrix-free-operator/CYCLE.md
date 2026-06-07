---
agent: abstractor
invoked_at: 2026-06-07T140000Z
scope: L4 roadmap_goal cap — mk_matrix_free_operator backend-lowering operator-constructor + pull-chain
status: pending
integrated_at: 2026-06-07T134107Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean by integrator-per-report (D1); finalized cycle-126 (batch-40 CLOSER). NEW L4 roadmap_goal cap mk_matrix_free_operator created + pull-chain wired reference-class (rank_violations:0 holds — no firm->roadmap_goal depends-on); SUMMARY/L4-index alpha-inserted; RESOLUTION MARKER appended for OQ mk_matrix_free_operator-l4-backend-lowering-placeholder (header-close = batch-40 meta unify-authority). Build EXIT 0, no finalize build-repair."
inputs:
  - reports/2026-06-07T134107Z-cycle-planner-c126/CYCLE.md (D1 entry)
  - scaffolding/open-questions.md:2031-2045 (OQ mk_matrix_free_operator-l4-backend-lowering-placeholder)
  - book/src/L4/fe_assemble.md (firm spine consumer — the pull-to-root)
  - book/src/L2/matrix-free-operator-apply.md (firm L2 contraction-chain combinator — the lowers-to target)
  - palace/fem/libceed/operator.hpp:32,:48,:81-82 (the ceed::Operator matrix-free wrapper + materialization)
  - palace/fem/bilinearform.cpp:118,:143 (UseFullAssembly partial/full dispatch)
---

# CYCLE: L4 roadmap_goal cap — mk_matrix_free_operator backend-lowering operator-constructor + pull-chain

## Summary

This is the ASK-2 "A" first L4 step: the L4 **backend-lowering operator-constructor** `mk_matrix_free_operator`, the burn/GPU entry point whose `apply` lowers to the matrix-free tensor-contraction graph `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`. It is the speculative L4 placeholder the c125 D2 OQ deferred (`mk_matrix_free_operator-l4-backend-lowering-placeholder`), deliberately landed at **`roadmap_goal` (rank 0)** so it does NOT over-claim — the deep L4 backend-lowering feature surface that would make it a firm composition-root is batch-41 "A" work; this cycle just lands the cleanly-closeable first step with its pull-chain wired so it is NOT stranded. The pull-chain is **`reference`-class ONLY** (a firm node must not blocking-`depends-on` a rank-0 roadmap_goal): a `reference`-class down-edge from firm `L4/fe_assemble` → `mk_matrix_free_operator` (the pull from a feature root, making it reachable / not-garbage), and a `reference`-class `lowers-to` edge from `mk_matrix_free_operator` → the firm `L2/matrix-free-operator-apply` combinator (the contraction-chain its apply lowers to). The chapter is claim-free: the signature, the apply-lowering sketch, and the construction-site L0 anchors are flagged speculative-intent (the matrix-free representation IS the constructive interior of `fe_assemble`'s per-term leaf under the `UseFullAssembly`-false dispatch, but the L4 op as a *named backend constructor surface* is not yet a firm Palace-source artifact). `rank_violations: 0` holds — both pull-chain edges are `reference` (navigational, free, NOT rank-constrained).

## Proposed changes

```new:book/src/L4/mk_matrix_free_operator.md
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
```

```edit:book/src/L4/fe_assemble.md
  reference:
    - L4/index
    - concepts/black-box-vs-accelerated-kernels
    - concepts/state-stratification
    - target: L4/mk_matrix_free_operator
      kind: constructs-via   # NAVIGATIONAL `reference` (NOT depends-on): the matrix-free constructive interior of this fold's per-term `assemble_term` leaf under the `UseFullAssembly`-false dispatch. `mk_matrix_free_operator` is a rank-0 `roadmap_goal`; a firm node may `reference` it (free, no liveness/rank constraint — scheme §1g) but must NOT `depends-on` it (would violate well-foundedness). This is the pull-to-root that keeps `mk_matrix_free_operator` reachable / not-garbage.
```

```edit:book/src/L4/fe_assemble.md
This entry records the rotation *direction* (L4 `foldr`/sum combinator → L3 explicit accumulating composite-operator build) in-line per high→low discipline; it does **not** author the theme. The L3-entry-vs-dissolution-home verdict (whether a standalone `L3/fe_assemble` entry is warranted, or whether the dissolution theme is the authoritative L3-form home — the `solve_family` NO-ENTRY-warrant question) is D2's to record; the family fold here carries **no `sequential-obstruction`** (the term contributions are independent — embarrassingly parallel, summed; law 1/3), so the likely verdict is the `solve_family` shape (the dissolution theme is the authoritative downward home, the loop lifts), but D2 owns it.

The opaque per-term leaf `assemble_term` has a **matrix-free constructive interior** under the `partial matrix-free` (`UseFullAssembly`-false) dispatch (`palace/fem/bilinearform.cpp:143`): the L4 backend-lowering operator-constructor [`mk_matrix_free_operator`](./mk_matrix_free_operator.md) (`roadmap_goal`, c126 D1), whose `apply` is the firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) contraction chain `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`. This is a **navigational `reference` (`constructs-via`), NOT a `depends-on`** — `fe_assemble` folds `assemble_term` as an *opaque black-box-kernel input* (its firmness is in the fold apparatus, not the leaf interior); the matrix-free interior is the backend-lowering surface a future L4 feature column will firm, pulled to a root by this navigational edge. A firm node may reference a rank-0 `roadmap_goal` (free, scheme §1g); it must not block on it.
```

```edit:book/src/L4/index.md
| [`linear_combination`](./linear_combination.md) | `linear_combination :: [(Scalar, Tensor[(S: ...)])] -> Tensor[$S]`; `= foldl (\acc (a,t) -> acc + scal a t) (zeros $S) pairs`. The scalar-weighted-tensor-sum combinator `Σᵢ aᵢ·tᵢ`. Pure value-producing term-list fold — no `Solve` monad / carry / predicate. | Concepts: `black-box-vs-accelerated-kernels` (rises-regardless), `scalar-promotion` (`real ⊑ complex` scalar list). L3 row: re-expresses through [`L3/linear_combination`](../L3/linear_combination.md). Arity specializations (accelerated-kernel notes, stopped low): `scal` / `axpy` / `axpby` / `axpbypcz`. Next-pull operator-operand consumer: [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md). | L3 [`linear_combination`](../L3/linear_combination.md) by **identity-in-form on the body** (value-thread-isomorphic; **no dedicated L4>L3 theme** — in-line §"Downward to L3", the `eigsolve`/`chebyshev` in-line-marker route); substantive translation is the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) (arity-dispatch + pinned summation order). | `firm` (cycle-068 D3 — risen from firm [`L3/linear_combination`](../L3/linear_combination.md); the BLAS-1 combinator that rises to L4 regardless as a feature-surface verb; laws carried up unchanged / syntactic-identity escape) |
| [`mk_matrix_free_operator`](./mk_matrix_free_operator.md) | `mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])`. The L4 **backend-lowering operator-constructor** that builds a matrix-free (un-materialized) linear operator whose `apply` is the element-local tensor-contraction graph `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` — the constructive interior of [`fe_assemble`](./fe_assemble.md)'s per-term `assemble_term` leaf under the `partial matrix-free` (`UseFullAssembly`-false) dispatch; the burn/GPU backend-lowering entry point. **Claim-free `roadmap_goal`** (no positive L4-constructor source claim; speculative reconstruction). | Reference (free, navigational — NOT rank-constrained): `lowers-to` [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) (the firm apply-chain composition, c125 D2; the four firm L1 substrate ops below it); `pulled-by` / `constructs-via` firm [`fe_assemble`](./fe_assemble.md) (the spine consumer reaching a feature root — the reachability edge). Concepts: `element-local-tensor` (the `(N: ...)`/`[E, ...]` shape family), `black-box-vs-accelerated-kernels` (the matrix-free interior of `fe_assemble`'s opaque leaf). | L2 the firm contraction-chain combinator [`matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) via the `reference`-class `lowers-to` edge (the L4 op is the operator-CONSTRUCTOR surface; the L2 combinator is the apply-chain COMPOSITION it produces). | `roadmap_goal` (rank 0; c126 D1 — the ASK-2 "A" first L4 backend-lowering step, landed claim-free with its pull-chain wired `reference`-class so `rank_violations: 0` holds; promotes as the dedicated L4 backend-lowering feature surface lands, batch-41 "A". Rank-0 nodes do not bump the firm count) |
| [`nrm2`](./nrm2.md) | `nrm2 :: Tensor[(S: ...)] -> Scalar`; `nrm2 x = sqrt (abs (inner_product x x))`. The kept named 2-norm verb `‖x‖₂ = √⟨x, x⟩` — `√ ∘ abs ∘ inner_product` at the diagonal `y = x`. A **CONSUMER** of the combinator, NOT a fold member (split-additivity lost under `√` — the do-NOT-merge guard). Result always real ≥ 0. Pure value-producing scalar map on a pure reduction — no `Solve` monad / carry / predicate. | Concepts: `black-box-vs-accelerated-kernels` (§2 kept-named-abstraction rises), `nrm2` (BLAS-1 heritage). L4 rows: **consumes** [`inner_product`](./inner_product.md) at the diagonal (the permitted dual — `nrm2` is a consumer verb, NOT a member; combinator law 5 PSD-at-diagonal is the √ well-definedness witness); sibling named verb [`dot`](./dot.md). | L3 [`nrm2`](../L3/nrm2.md) by **identity-in-form on the body** (value-thread-isomorphic; **no dedicated L4>L3 theme** — in-line §"Downward to L3", the in-line-marker route); substantive downward content is the L1>L0 [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) (the four-stage chain + the `abs`-guard classification) + the inner reduction's L2>L1 fold-specialization. | `firm` (cycle-069 D2 — risen from firm [`L3/nrm2`](../L3/nrm2.md) as the diagonal consumer of firm [`inner_product`](./inner_product.md); the kept named abstraction that rises to L4 as a named consumer verb, `concepts/black-box-vs-accelerated-kernels.md` §2; the five norm laws are syntactic identities / standard norm facts / syntactic-identity escape; the `abs` defensive guard preserved) |
```

```edit:book/src/SUMMARY.md
  - [linear_combination](./L4/linear_combination.md)
  - [mk_matrix_free_operator](./L4/mk_matrix_free_operator.md)
  - [nrm2](./L4/nrm2.md)
```

```edit:scaffolding/open-questions.md
## mk_matrix_free_operator-l4-backend-lowering-placeholder — RESOLVED (landed as roadmap_goal with pull-chain wired, c126 D1)
opened_at: cycle-125
opened_by: integrator-per-report (promoted from abstractor D2 §Open questions / caveats — the speculative L4 placeholder, NOT authored this cycle)
resolved_at: cycle-126
resolved_by: abstractor D1

The speculative L4 `mk_matrix_free_operator` (the backend-lowering operator constructor whose apply
lowers to the tensor-contraction graph `Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`) is now landed as a claim-free
`roadmap_goal` (rank 0) chapter `book/src/L4/mk_matrix_free_operator.md` (c126 D1). The c125 strand
concern (no pull-chain to a root yet) is RESOLVED: the chapter is pulled to a feature root by a
**`reference`-class** (`constructs-via` / `pulled-by`) edge from the firm `L4/fe_assemble` spine
consumer (the matrix-free representation IS the constructive interior of fe_assemble's per-term
`assemble_term` leaf under the `UseFullAssembly`-false dispatch), and it down-links the firm
`L2/matrix-free-operator-apply` combinator (c125 D2) via a `reference`-class `lowers-to` edge. Both
edges are `reference` (navigational, free, NOT rank-constrained) — a firm node may reference a rank-0
roadmap_goal but must not `depends-on` it — so `rank_violations: 0` holds. The deep L4 backend-lowering
feature surface that would firm this node (the blocking pull) remains batch-41 "A" work; landing it
firm now would over-claim, so it stays `roadmap_goal` by design. Signature:
`mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])`.
Source: `reports/2026-06-07T134107Z-abstractor-l4-mk-matrix-free-operator/CYCLE.md`.
```

## Speculative operators proposed

**`mk_matrix_free_operator`** (the chapter IS the operator — landed as the `roadmap_goal` home, not a stranded sketch).
- **Intended signature:** `mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])`.
- **Motivation:** the L4 backend-lowering operator-CONSTRUCTOR surface — the burn/GPU entry point that builds a matrix-free (un-materialized) linear operator whose `apply` runs the element-local contraction graph `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (the firm `L2/matrix-free-operator-apply` combinator) rather than a materialized CSR spmv. It is the constructive interior of `fe_assemble`'s per-term `assemble_term` opaque leaf under the `partial matrix-free` dispatch (`UseFullAssembly` false). Landed `roadmap_goal` (claim-free) this cycle as the ASK-2 "A" first L4 step; harvester/future-dispatch promotes it as the dedicated L4 backend-lowering feature surface lands the blocking pull (batch-41 "A").

## Supporting evidence

- **L4 spine consumer (pull-to-root):** `book/src/L4/fe_assemble.md` (firm; `:16,:166` the `assembly-representation: partial matrix-free ceed::Operator` variant axis this op makes structural; `:24,:33,:177` the `assemble_term` opaque-black-box-leaf treatment whose matrix-free interior this op is).
- **L2 lowers-to target:** `book/src/L2/matrix-free-operator-apply.md` (firm, c125 D2; the contraction-chain combinator `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` composing the four firm L1 substrate ops `element_restrict` / `basis_apply` / `quad_point_contract` / `geom_factor_build`).
- **L0 construction-site anchors** (all self-verified via `citecheck --anchor`, all `[ok]`):
  - `palace/fem/libceed/operator.hpp:32` — `class Operator : public palace::Operator` (the `ceed::Operator` matrix-free wrapper).
  - `palace/fem/libceed/operator.hpp:48` — `AddSubOperator(...)` (per-term sub-operator accumulation).
  - `palace/fem/libceed/operator.hpp:81-82` — `CeedOperatorFullAssemble(...)` (the matrix-free → CSR materialization, the `full` alternative).
  - `palace/fem/bilinearform.cpp:118` — `UseFullAssembly(...)` declaration (the order-threshold dispatch predicate).
  - `palace/fem/bilinearform.cpp:143` — `if (UseFullAssembly(...))` in `BilinearForm::Assemble` (the partial-matrix-free-vs-full branch; this op IS the `else`/`PartialAssemble` branch).
- **Shape family:** `book/src/concepts/element-local-tensor.md` (firm, c124 D5; the `(N: ...)`/`[E, L]`/`[E, P, C]`/`[E, P, G]` rank-structured family the chain is typed over).

## Open questions / caveats

- **Maturity judgment (delegated within a default): landed `roadmap_goal`, NOT firm.** Per the planner's caveat, I considered the firm-on-positive-structure escape (the construction algebra is positively sourced at the libCEED wrapper, and the apply-lowers-to-L2 correspondence is a clean composition fact). I DEFAULTED to `roadmap_goal` per the explicit cap mandate: the dedicated L4 backend-lowering feature column that would make `mk_matrix_free_operator` a firm *composition-root* does not exist yet, and the inbound pull is `reference`-class (navigational), not a *blocking* `depends-on` from a firm consumer — so there is no blocking-consumer pull-chain to a root that would license a firm claim. Landing it firm would over-claim the backend-lowering surface that is explicitly batch-41 "A" work. The promotion condition is recorded in-chapter: a blocking pull from the dedicated L4 backend-lowering feature surface. Flagging for the critic/meta: confirm `roadmap_goal` is the right cap maturity (or whether a firm-on-positive-structure cap is warranted — a batch-41-meta codification question if it recurs).
- **The pull-chain edges are `reference`-class by REQUIREMENT, not preference.** A firm node (`fe_assemble`) carrying a *blocking* `depends-on` to a rank-0 `roadmap_goal` would violate well-foundedness (`rank(fe_assemble) = firm > rank(mk_matrix_free_operator) = 0`). The pull-to-root is therefore `reference` (`constructs-via`; navigational, free, NOT rank-constrained — scheme §1g). Likewise the `lowers-to` edge to the firm L2 combinator is `reference` (a `roadmap_goal` may rest on anything, but recording it `reference` rather than `depends-on` keeps the rank-0 node from imposing a (nonexistent) rank floor). The critic/linter should confirm `rank_violations: 0` HOLDS on the landed tree.
- **L2/index firm-count reconcile (NOT this dispatch's work).** The c125 finalize flagged an `L2/index.md:95` prose-vs-table firm-count divergence for the batch-40 meta. This dispatch touches only `L4/index.md` (a roadmap_goal row, which does NOT bump the firm count) — no L2 count interaction. Noting it only so the meta's intake stays primed; out of my write-scope.
- **AMR rebuild consumer (forward note, unchanged).** The OQ `matrix-free-operator-apply-amr-rebuild-consumer-forward-note` (c125) records that `geom_factor_build` (and thus this op's `GeomFactors` build-stratum) is rebuilt on AMR refinement. When the AMR consumer (DIRECTIVE-2 grounded consumer-(2)) lands, it is a faithful future consumer of `mk_matrix_free_operator`'s rebuild boundary — a future edge, not authored this cycle.

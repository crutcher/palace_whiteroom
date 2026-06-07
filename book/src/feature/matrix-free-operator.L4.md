---
kind: feature-surface
feature: matrix-free-operator
level: L4
feature_root: seed
rank: firm
edges:
  depends-on:
    - target: L4/mk_matrix_free_operator
      kind: composes                  # the backend-lowering operator-CONSTRUCTOR cap this surface composes (firm c127 D1 — promoted off roadmap_goal by THIS column)
    - target: L2/matrix-free-operator-apply
      kind: composes                  # the apply-chain combinator the constructor's `apply` runs: A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G (firm c125 D2)
    - target: palace/fem/bilinearform.cpp:118-147
      kind: cites-evidence            # UseFullAssembly (:118) + BilinearForm::Assemble branch (:140) + PartialAssemble() (:147) — the matrix-free construct-time dispatch
  reference:
    - feature/matrix-free-operator.L1
    - L4/fe_assemble                   # the firm fold whose per-term `assemble_term` leaf this is the matrix-free constructive interior of (constructs-via; navigational)
    - L4-L3/mk-matrix-free-operator-dissolution   # D2's L4>L3 down-narrative theme dissolving the constructor's apply into the L3 contraction-chain view (authored this cycle)
    - concepts/element-local-tensor    # the rank-structured shape family the contraction chain is typed over (firm c124 D5)
    - concepts/black-box-vs-accelerated-kernels   # the disposition that puts the matrix-free representation as the backend-lowering target
    - semantics/index
---

# matrix-free operator — L4 backend-lowering composition-root

The **matrix-free FE operator** entry point, presented at L4 as a single composition of firm
L4/L2/L1 vocabulary — the **outward backend-lowering surface** an external GPU-tensor / burn
backend instantiates (DIRECTIVE-1: L4 IS the outward backend-lowering target). This chapter is a
*composition root* of the **infrastructure / shared-substrate** sub-kind (the matrix-free
representation every high-order driver's assemble stage composes when the order-threshold dispatch
selects partial assembly) — NOT a driver-leaf entry point and NOT an output product. It does not
introduce a new combinator; it wires the already-firm vocabulary into the matrix-free
operator-constructor surface and links DOWN to each composed piece. (Sub-kind:
**driver-agnostic infrastructure** — a shared *assemble-side* surface every high-order
preconditioned solve composes, the assemble-side analog of how
[`geometric-multigrid-preconditioner`](./geometric-multigrid-preconditioner.L4.md) is the shared
*solve-side* infrastructure column.)

The matrix-free operator is a **spine dependency**: it is the constructive interior of the firm
[`fe_assemble`](../L4/fe_assemble.md) fold's per-term `assemble_term` leaf under the partial-assembly
(`UseFullAssembly`-false) dispatch (`palace/fem/bilinearform.cpp:147`), and `fe_assemble` is composed
by 7 feature columns. Building this column is the DIRECTIVE-3 / batch-41 "A" surface that PULLS the
[`mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md) cap off `roadmap_goal` (the cap's named
promotion condition) — and the faithful `depends-on` consumer that GROUNDS the RE11 libceed-substrate
sub-cohort (see §"RE11 grounding").

## The composition

At L4 the matrix-free operator is the composition (Haskell-style; the strawman
`book/src/semantics/index.md` notation):

    -- input  = an FE space, a weak-form term (Q, 𝒟), and the precomputed geometry factors
    -- output = an `Op` value (operator instance) whose `apply` is the un-materialized contraction graph;
    --          the codomain uses the operator-VALUE spelling `Op[τ_in → τ_out]` per the closure-returning-signature
    --          convention (`book/src/semantics/index.md` §1.3.1) — a constructor product carrying closed-over params, applied via `apply`
    matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> Op[Tensor[(N: ...)] → Tensor[(N: ...)]]
    matrix_free_operator space term geom =
      mk_matrix_free_operator space term geom        -- (1) the constructor cap ── L4/mk_matrix_free_operator (firm)
      -- whose apply runs the firm L2 contraction-chain combinator:
      --   apply A v = matrix-free-operator-apply space term geom v   -- (2) ── L2/matrix-free-operator-apply (firm)
      --             = (Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G) v                   --     the five-stage contraction chain

Two composed stages, each a link DOWN to firm vocabulary:

1. **The operator-constructor cap** — [`mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md)
   (**firm**, c127 — promoted off `roadmap_goal` by THIS column). It builds the matrix-free
   (un-materialized) linear operator from the FE space + weak-form term + geometry factors; the
   constructor wires the contraction graph **once** at build time (the GPU-backend-relevant
   constructor/apply split — build the graph once, run it per `apply`). It is the `partial
   matrix-free ceed::Operator` branch of Palace's order-threshold `UseFullAssembly` dispatch
   (`palace/fem/bilinearform.cpp:147`, `PartialAssemble()`), the un-materialized representation
   (the `full` branch being the `CeedOperatorFullAssemble` CSR materialization).

2. **The apply-chain combinator** — [`matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md)
   (**firm**, c125 D2). The constructor's `apply` IS this named L2 contraction-chain combinator —
   the five-stage pipe `A·v = Gᵀ(B_𝒟ᵀ(D ⊙ (B_𝒟(G·v))))` where `G`/`Gᵀ` is
   [`element_restrict`](../L1/element_restrict.md) (the `[(N: ...)] ↔ [E, L]` gather / scatter-add),
   `B_𝒟`/`B_𝒟ᵀ` is [`basis_apply`](../L1/basis_apply.md) (the `[E, L] ↔ [E, P, C]` basis-eval
   contraction keyed on 𝒟), and `D` is [`quad_point_contract`](../L1/quad_point_contract.md) (the
   pointwise `[E, P, C]` per-quad-point diagonal against the `[E, P, G]`
   [`geom_factor_build`](../L1/geom_factor_build.md) carrier). The combinator composes the four firm
   element-local substrate ops by name — so this surface reaches them transitively (the L1 sibling
   surface names them directly, the RE11 grounding edges).

## Inputs / outputs (the feature surface)

- **Input — config + the assembled-once geometry.** The FE space (the `readonly` construction
  stratum), the weak-form term `(Q, 𝒟)` (coefficient `Q` + differential-operator `𝒟` selecting the
  basis EvalMode `B_𝒟`), and the build-stratum `[E, P, G]` geometry-factor carrier (the firm
  `geom_factor_build` product). All `readonly` / build-stratum inputs, fixed once per
  `(mesh, FE order, quadrature rule)`, rebuilt only on mesh change. L0: the `BilinearForm` /
  `AssembleCeedOperator` master assembler parameter list.
- **Output — a matrix-free LinearOperator.** A `LinearOperator (Tensor[(N: ...)])` whose `apply`
  runs the contraction chain on demand (no materialized matrix) — the value a GPU/burn backend
  instantiates: an operator whose action is a contraction graph, not a CSR spmv. L0:
  `ceed::Operator` (`palace/fem/libceed/operator.hpp:32`).

## Why this is firm (the clean-gate landing — not forced)

Under the OWN-COMPOSITION promotion rule **and** the well-foundedness invariant
`rank(u) ≤ min(deps)`, this column is **firm**:

- **Every directly-owned blocking constituent is firm on disk** —
  [`mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md) (firm c127, promoted by this column),
  [`matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) (firm c125 D2), and
  transitively the four firm substrate ops. `min(deps) = firm`, so `rank(column) = firm` is rank-legal.
- **The composition algebra is exhaustively cited and carries NO loop / recurrence obstruction.**
  Unlike the GMG V-cycle (a level-recursion) or the krylov-iteration spine (a `partial-obstruction`
  iteration-view cap), the matrix-free constructor surface is a **fixed five-stage contraction
  chain** — fully cited at the L2 combinator (`AssembleCeedOperator` master +
  `Operator::Mult`) and the construct-time dispatch (`bilinearform.cpp:118-147`). The
  composition-level claim (build the graph once; `apply` runs it) is a syntactic-identity fact on
  positive source — the **firm-on-positive-structure escape** (no test gates a composition
  identity).
- **A faithful pull-to-root now exists.** This column carries a `depends-on (composes)` edge to the
  cap (firm→firm, rank-legal), so the cap's named promotion condition is met without forcing.

This chapter carries the *compositional* claim (the matrix-free operator = this composition of the
constructor cap + the contraction-chain combinator), not the constituents' per-op algebraic claims
(those live in the linked chapters). Evidence: the L2 combinator's `AssembleCeedOperator` /
`Operator::Mult` citations + the `bilinearform.cpp:118-147` construct-time dispatch.

## Single-machine reading (DIRECTIVE-1)

The matrix-free representation is **device-agnostic** and identical at single rank — the
contraction chain `Gᵀ B_𝒟ᵀ D B_𝒟 G` is per-element-local; the `element_restrict` gather/scatter-add
is the only inter-dof transfer, and its `Par*` shared-dof multiplicity post-scale is read
single-rank per §Scope (the MPI collectives inside the restriction are the deferred MPI layer
DIRECTIVE-1 keeps OUT). No MPI-associated version is lifted here. (This device-agnosticism is
*precisely* why the matrix-free surface is the outward backend-lowering target.)

## Constituent down-links

| Stage | Constituent | Status | L0 site |
|---|---|---|---|
| operator-constructor cap (blocking dep) | [`mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md) | firm (c127) | `bilinearform.cpp:147` (`PartialAssemble`); `operator.hpp:32` (`ceed::Operator`) |
| apply-chain combinator (blocking dep) | [`matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) | firm (c125 D2) | `integrator.cpp:422-445`; `operator.cpp:182-189` |
| element gather/scatter-add G/Gᵀ (transitive) | [`element_restrict`](../L1/element_restrict.md) | firm (c125 D1) | (via L2 combinator) |
| basis-eval B_𝒟/B_𝒟ᵀ (transitive) | [`basis_apply`](../L1/basis_apply.md) | firm (c124 D3) | (via L2 combinator) |
| pointwise quad-point diagonal D (transitive) | [`quad_point_contract`](../L1/quad_point_contract.md) | firm (c124 D3) | (via L2 combinator) |
| `[E, P, G]` geometry-factor carrier (transitive) | [`geom_factor_build`](../L1/geom_factor_build.md) | firm (c125 D1) | (via L2 combinator) |
| shape family the chain is typed over | [`element-local-tensor`](../concepts/element-local-tensor.md) | firm (c124 D5) | — |

## Down-narrative (L4 → L3)

The L4>L3 dissolution of the constructor's `apply` into the L3 element-local tensor-contraction
chain — the genuine flat→element-local vocabulary shift — is authored as a dedicated theme this
cycle: [`mk-matrix-free-operator-dissolution`](../L4-L3/mk-matrix-free-operator-dissolution.md)
(D2, this cycle). That theme names the substrate ops as genuine constituents of the contraction
chain (`A·v = Gᵀ(B_𝒟ᵀ(D ⊙ (B_𝒟(G·v))))`), distinct from the existing
`fe-assemble-fold-dissolution` theme, which bottoms its per-term leaf out at the *opaque* libCEED
boundary and explicitly puts the matrix-free interior out of scope.

## Status

`firm` (landed firm cycle-127 D1) — the second **infrastructure / shared-substrate**
feature-surface composition-root (the assemble-side analog of the solve-side GMG column), and the
dedicated L4 backend-lowering entry point for matrix-free FE operators (DIRECTIVE-1: L4 IS the
outward backend-lowering target). The GC-root marker `feature_root: seed` is preserved (root-role
is permanent/categorical, a separate axis from the resolution ladder). **Why firm:** every
directly-owned blocking constituent is firm on disk (`mk_matrix_free_operator` c127,
`matrix-free-operator-apply` c125 D2, the four substrate ops c124/c125); `rank(u) ≤ min(deps) =
firm` holds; the constructor + apply composition algebra is exhaustively cited and carries no loop
obstruction (firm-on-positive-structure escape, NOT forced — the planner HARD CONSTRAINT was
checked and passes). This column is the faithful `depends-on` consumer that GROUNDS the RE11
libceed-substrate sub-cohort (the L1 sibling names the four substrate ops directly via blocking
`depends-on` edges). Evidence: the L2 combinator citations + `bilinearform.cpp:118-147`.

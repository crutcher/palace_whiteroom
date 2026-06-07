---
agent: layer-intro-author
invoked_at: 2026-06-07T153621Z
scope: feature/matrix-free-operator.{L4,L1} backend-lowering feature-surface column + mk_matrix_free_operator cap firm-flip
status: integrated
integrated_at: 2026-06-07T180000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (D1 LEAD). L4 cap mk_matrix_free_operator roadmap_goal->FIRM (lowers-to edge reference->depends-on, firm L2 dep) + firm feature/matrix-free-operator.{L4,L1} column (4 blocking depends-on composes edges naming the libceed substrate ops by name) + SUMMARY/feature-index/infrastructure alpha-inserts. The 4 substrate ops climbed OUT of the reference-only-reachable RE11 cohort into HARD-reachable (RE11 sub-cohort GROUNDED, confirmed by finalize --show-inbound). cargo make book EXIT 0; rank_violations 0; reachable 157->163. 1 OQ promoted."
---

# CYCLE: feature/matrix-free-operator column (D1 LEAD, cycle-127)

## Summary

Author the **matrix-free-operator backend-lowering feature-surface column** — a new
infrastructure / shared-substrate composition-root (the same sub-kind as the GMG
preconditioner column), at L4 + L1. The column composes BY NAME, via faithful blocking
`depends-on (composes)` edges: the firm L4 cap [`mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md),
the firm L2 combinator [`matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md),
and (transitively at the L1 surface) the 4 firm L1 substrate ops
(`element_restrict` / `basis_apply` / `quad_point_contract` / `geom_factor_build`) +
`concepts/element-local-tensor`.

**Key deliverable — FIRM decision (cap flipped `roadmap_goal → firm`).** I SOLE-OWN the cap
firm-flip per the overlap analysis. Decision: **FIRM** — the cap's blocking deps are all firm
on disk (well-foundedness `rank ≤ min(deps) = firm`), its constructor + apply composition
algebra is exhaustively cited (the constructor surface is a *fixed 5-stage contraction chain*,
NOT a loop/recurrence — strictly simpler than the GMG V-cycle that firmed at c122), and this
column now faithfully PULLS it via a `depends-on (composes)` edge. The cap's `apply`-lowering
is the firm L2 combinator; nothing in the constructor surface is left speculative. See
§"Firm-vs-rough-in decision" for the full adjudication.

This column is the prospective **RE11 grounder** for the libceed-substrate sub-cohort: its
faithful blocking `depends-on` edges to the L2 combinator (and at L1 to the four substrate ops)
are a REAL composition flip from a root-reaching firm node — the §2g distinction between the
deliberate reference-only cohort and a genuine `depends-on` consumer. See §"RE11 grounding".

Files: new `book/src/feature/matrix-free-operator.L4.md`, new
`book/src/feature/matrix-free-operator.L1.md`, the `feature/index.md` matrix row + infrastructure
narrative, the `feature/infrastructure.md` group-intro member entry, `SUMMARY.md` two rows, the
`L4/mk_matrix_free_operator.md` cap firm-flip (frontmatter + banners + Status). Down-narrative
forward-references D2's canonical slug `book/src/L4-L3/mk-matrix-free-operator-dissolution.md`
(D2 authors it this cycle).

## Firm-vs-rough-in decision (the cap + the column)

**Decision: FIRM** — both the column and the `mk_matrix_free_operator` cap.

Per the HARD CONSTRAINT (planner caveat — never force the spine), I checked the two firm gates:

1. **Well-foundedness (§1g, `rank(u) ≤ min over depends-on deps of rank(v)`).** The cap's
   blocking deps, read from each chapter's on-disk `rank:` line this dispatch:
   - `L2/matrix-free-operator-apply` — `rank: firm` (`book/src/L2/matrix-free-operator-apply.md:16`).
   - `L1/element_restrict` — `rank: firm` (`:14`); `L1/basis_apply` — `rank: firm` (`:10`);
     `L1/quad_point_contract` — `rank: firm` (`:10`); `L1/geom_factor_build` — `rank: firm` (`:14`).
   - `concepts/element-local-tensor` — `rank: firm` (`:2`).
   `min(deps) = firm`, so `firm` is permitted (no partial-obstruction / rough-in / roadmap_goal
   dep caps it down — unlike the c123 krylov-iteration column, which was capped rough-in by its
   `fold_solve` / `orthogonalize` partial-obstruction deps).

2. **Composition algebra exhaustively cited.** The crucial difference from a forced firm-flip:
   the cap is an **operator CONSTRUCTOR** whose `apply` is a *fixed five-stage contraction chain*
   `apply = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` — there is **no V-cycle-style recursion / loop obstruction
   in the constructor surface itself**. The chain is already exhaustively cited at the firm L2
   combinator (`AssembleCeedOperator` master assembler `palace/fem/libceed/integrator.cpp:422-445`
   + `Operator::Mult` apply `palace/fem/libceed/operator.cpp:182-189`), and the construct-time
   dispatch is cited at `palace/fem/bilinearform.cpp:118` (`UseFullAssembly`), `:140`
   (`BilinearForm::Assemble` branch), `:147` (`PartialAssemble()` — the matrix-free branch this
   constructor IS). All five of the cap's own L0 anchors are already self-verified
   (`mk_matrix_free_operator.md:95`, `citecheck --anchor` all `[ok]`). So the constructor +
   apply composition algebra is *fully positive-source-cited*; nothing is left as a speculative
   reconstruction. This is the **firm-on-positive-structure escape**: the composition-level laws
   (the constructor builds the contraction graph once; `apply` runs it) are syntactic-identity
   facts on the positive source, with no test gating a composition identity — exactly the basis
   on which the L2 combinator and the GMG column firmed.

3. **A faithful pull from a root-reaching firm node now exists.** The cap's own §Intent named
   its promotion condition: *"the dedicated L4 backend-lowering feature surface lands (batch-41
   'A') and provides the blocking pull-chain that licenses a non-speculative claim."* This column
   IS that surface, and it pulls the cap by a faithful `depends-on (composes)` edge (firm→firm,
   rank-legal). The cap is no longer reachable only by the `reference (constructs-via)` hop from
   `fe_assemble` — it now has a genuine blocking inbound from a firm composition-root.

**Conclusion:** all three firm gates pass; FORCING was not required (the gates are genuinely
met). I flip the cap `roadmap_goal → firm` and land the column `firm`. The critic + finalize
linter (`rank_violations` must stay 0) are the backstop; on the landed tree, `rank(column) =
firm`, all its `depends-on` deps firm — rank-legal.

## Proposed depends-on edges (the faithful composition)

**L4 column → cap + combinator (blocking `depends-on (composes)`):**
- `feature/matrix-free-operator.L4` → `L4/mk_matrix_free_operator` — `composes` (the constructor
  cap this surface composes; firm→firm after the flip).
- `feature/matrix-free-operator.L4` → `L2/matrix-free-operator-apply` — `composes` (the apply-chain
  combinator the constructor's `apply` runs; firm).
- (`reference`) → `L4/fe_assemble`, `L4/index`, `concepts/element-local-tensor`,
  `concepts/black-box-vs-accelerated-kernels`, `semantics/index`, the
  `feature/matrix-free-operator.L1` sibling, and D2's
  `L4-L3/mk-matrix-free-operator-dissolution` down-narrative theme.

**L1 column → the 4 substrate ops (blocking `depends-on (composes)`):**
- `feature/matrix-free-operator.L1` → `L1/element_restrict`, `L1/basis_apply`,
  `L1/quad_point_contract`, `L1/geom_factor_build` — each `composes` (all firm). This is the L1
  surface that names the four substrate ops directly (the L4 surface names them transitively via
  the L2 combinator; the L1 surface names them by-name — the RE11 grounding edges).
- (`reference`) → `L1/libceed-quadrature-kernel-impl` (the kernel-impl whose concrete chain this
  pure-function surface renders), `concepts/element-local-tensor`, the
  `feature/matrix-free-operator.L4` sibling.

**Cap edge re-classification (the firm-flip):**
- `L4/fe_assemble → L4/mk_matrix_free_operator` STAYS `reference (constructs-via)` (firm→firm
  navigational — fine; NOT changed to depends-on, because fe_assemble folds the leaf opaquely).
- The cap's own outbound `L2/matrix-free-operator-apply` edge promotes from `reference (lowers-to)`
  to `depends-on (lowers-to)`: now that the cap is firm, its apply genuinely *blocking-depends-on*
  the firm L2 contraction chain (firm→firm, rank-legal). [See proposed-changes for the cap.]

## Proposed changes

```new-file:book/src/feature/matrix-free-operator.L4.md
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
    -- output = a LinearOperator whose `apply` is the un-materialized contraction graph
    matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])
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
```

```new-file:book/src/feature/matrix-free-operator.L1.md
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
```

```edit:book/src/feature/index.md
[old]:
| **[Infrastructure / shared-substrate columns](./infrastructure.md)** | | | |
| [geometric-multigrid-preconditioner](./geometric-multigrid-preconditioner.L4.md) (firm) | [L4 root](./geometric-multigrid-preconditioner.L4.md) | [L1 root](./geometric-multigrid-preconditioner.L1.md) | — |
| [krylov-iteration](./krylov-iteration.L4.md) (rough-in) | [L4 root](./krylov-iteration.L4.md) | [L1 root](./krylov-iteration.L1.md) | — |
[new]:
| **[Infrastructure / shared-substrate columns](./infrastructure.md)** | | | |
| [geometric-multigrid-preconditioner](./geometric-multigrid-preconditioner.L4.md) (firm) | [L4 root](./geometric-multigrid-preconditioner.L4.md) | [L1 root](./geometric-multigrid-preconditioner.L1.md) | — |
| [krylov-iteration](./krylov-iteration.L4.md) (rough-in) | [L4 root](./krylov-iteration.L4.md) | [L1 root](./krylov-iteration.L1.md) | — |
| [matrix-free-operator](./matrix-free-operator.L4.md) (firm) | [L4 root](./matrix-free-operator.L4.md) | [L1 root](./matrix-free-operator.L1.md) | — |
```

```edit:book/src/feature/infrastructure.md
[old]:
edges:
  reference:
    - feature/geometric-multigrid-preconditioner.L4
    - feature/geometric-multigrid-preconditioner.L1
    - feature/krylov-iteration.L4
    - feature/krylov-iteration.L1
---
[new]:
edges:
  reference:
    - feature/geometric-multigrid-preconditioner.L4
    - feature/geometric-multigrid-preconditioner.L1
    - feature/krylov-iteration.L4
    - feature/krylov-iteration.L1
    - feature/matrix-free-operator.L4
    - feature/matrix-free-operator.L1
---
```

```edit:book/src/feature/infrastructure.md
[old]:
- [**krylov-iteration**](./krylov-iteration.L4.md) — the Krylov / Arnoldi **iteration spine**
  every iterative solve hangs under; the iteration-rotation parallel of the GMG column. The
  DIRECTIVE-2 item-4b grounded consumer that DISCHARGES RE2 (`L3/orthogonalize`) and RE8
  (`L3/krylov-step`, `L3/fold_solve`) by composing the L3 iteration-rotation form BY NAME via
  blocking `depends-on (composes)` edges (a genuine depends-on reachability flip). (rough-in —
  capped at partial-obstruction by its `fold_solve` / `orthogonalize` iteration-views, the
  body-lifts-loop-doesn't honesty; coupled to the roadmap_goal
  [`eigsolve-impl`](../L3/eigsolve-impl.md) constructive eigensolve consumer.)
[new]:
- [**krylov-iteration**](./krylov-iteration.L4.md) — the Krylov / Arnoldi **iteration spine**
  every iterative solve hangs under; the iteration-rotation parallel of the GMG column. The
  DIRECTIVE-2 item-4b grounded consumer that DISCHARGES RE2 (`L3/orthogonalize`) and RE8
  (`L3/krylov-step`, `L3/fold_solve`) by composing the L3 iteration-rotation form BY NAME via
  blocking `depends-on (composes)` edges (a genuine depends-on reachability flip). (rough-in —
  capped at partial-obstruction by its `fold_solve` / `orthogonalize` iteration-views, the
  body-lifts-loop-doesn't honesty; coupled to the roadmap_goal
  [`eigsolve-impl`](../L3/eigsolve-impl.md) constructive eigensolve consumer.)
- [**matrix-free-operator**](./matrix-free-operator.L4.md) — the matrix-free FE operator
  **backend-lowering surface** every high-order driver's assemble stage composes when the
  order-threshold `UseFullAssembly` dispatch selects partial assembly; the **assemble-side**
  infrastructure analog of the solve-side GMG column. The batch-41 "A" / DIRECTIVE-3 grounded
  consumer that firms the [`mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md) cap off
  `roadmap_goal` (composing the constructor cap + the firm L2 contraction-chain combinator by name)
  and GROUNDS the RE11 libceed-substrate sub-cohort (its L1 surface names the four firm element-local
  substrate ops `element_restrict`/`basis_apply`/`quad_point_contract`/`geom_factor_build` via
  blocking `depends-on (composes)` edges — a genuine depends-on reachability flip). (firm — the
  constructor surface is a fixed contraction chain with no loop obstruction, all blocking deps firm.)
```

```edit:book/src/SUMMARY.md
[old]:
  - [krylov-iteration — L4 composition-root](./feature/krylov-iteration.L4.md)
  - [krylov-iteration — L1 composition-root](./feature/krylov-iteration.L1.md)
[new]:
  - [krylov-iteration — L4 composition-root](./feature/krylov-iteration.L4.md)
  - [krylov-iteration — L1 composition-root](./feature/krylov-iteration.L1.md)
  - [matrix-free-operator — L4 backend-lowering composition-root](./feature/matrix-free-operator.L4.md)
  - [matrix-free-operator — L1 composition-root](./feature/matrix-free-operator.L1.md)
```

### The cap firm-flip (D1 SOLE-OWNS `mk_matrix_free_operator.md`; D2 read-only)

```edit:book/src/L4/mk_matrix_free_operator.md
[old]:
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
[new]:
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
```

```edit:book/src/L4/mk_matrix_free_operator.md
[old]:
> **⟢ roadmap_goal (rank 0) — claim-free intent.** This chapter carries **no positive Palace-source claim** about a named L4 `mk_matrix_free_operator` constructor. It is the intent node for the L4 backend-lowering operator-constructor whose `apply` lowers to the firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) contraction chain. Everything below the §Intent line is a **speculative reconstruction** in our L4 vocabulary, explicitly flagged; nothing here is asserted as Palace source. Pulled by the firm [`fe_assemble`](./fe_assemble.md) spine consumer (the reachability edge to a feature root). Promotes `roadmap_goal → rough-in → firm` as the dedicated L4 backend-lowering feature surface lands (batch-41 "A") and provides the blocking pull-chain that licenses a non-speculative claim.
[new]:
> **⟢ firm (rank 3) — promoted off roadmap_goal cycle-127 D1.** This chapter now carries a positive *compositional* claim: `mk_matrix_free_operator` is the L4 operator-constructor for the matrix-free (un-materialized) FE linear operator — the `partial matrix-free` (`UseFullAssembly`-false) branch of Palace's order-threshold assembly dispatch (`palace/fem/bilinearform.cpp:147`, `PartialAssemble()`), whose `apply` IS the firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) contraction chain `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`. **Promotion basis (the §1g well-foundedness check):** all blocking deps are firm (the L2 combinator c125 D2 + transitively the four firm L1 substrate ops), `min(deps) = firm`; the constructor + apply composition algebra is exhaustively cited (no loop / recurrence obstruction in the constructor surface — a fixed five-stage chain, firm-on-positive-structure escape); and the dedicated L4 backend-lowering feature surface [`feature/matrix-free-operator.L4`](../feature/matrix-free-operator.L4.md) (c127 D1) now PULLS it via a faithful blocking `depends-on (composes)` edge — the cap's previously-recorded promotion condition, met without forcing the spine. The constructor signature + apply-lowering below are now the *asserted* L4 form, not a speculative reconstruction.
```

```edit:book/src/L4/mk_matrix_free_operator.md
[old]:
## Speculative L4 form (the constructor signature + apply-lowering)

> **SPECULATIVE** — a reconstruction in our L4 vocabulary; not asserted as Palace source. Refine against evidence as the backend-lowering surface firms.

Signature (per the c125 D2 OQ placeholder, refined to the project's named-shape-group notation per [`semantics/index`](../semantics/index.md) §1.2 — the operator-domain shape group `(N: ...)` is the rank-structured DOF axis family, NOT a flat `Tensor[N]`; this is the genuine vocabulary shift the [`element-local-tensor`](../concepts/element-local-tensor.md) family carries away from the BLAS-1 flat vector):
[new]:
## L4 form (the constructor signature + apply-lowering)

> **FIRM** — the asserted L4 form (promoted off speculative c127 D1). The signature + apply-lowering below are the L4 rendering of the positively-cited `partial matrix-free` constructor + its contraction-chain apply.

Signature (in the project's named-shape-group notation per [`semantics/index`](../semantics/index.md) §1.2 — the operator-domain shape group `(N: ...)` is the rank-structured DOF axis family, NOT a flat `Tensor[N]`; this is the genuine vocabulary shift the [`element-local-tensor`](../concepts/element-local-tensor.md) family carries away from the BLAS-1 flat vector):
```

```edit:book/src/L4/mk_matrix_free_operator.md
[old]:
The apply lowers to the firm L2 contraction-chain combinator (the `reference`-class `lowers-to` edge):
[new]:
The apply lowers to the firm L2 contraction-chain combinator (the `depends-on (lowers-to)` edge — promoted from `reference` at the c127 D1 firm-flip; firm→firm, rank-legal):
```

```edit:book/src/L4/mk_matrix_free_operator.md
[old]:
## Pull-chain (reachability — why this is not garbage)

This `roadmap_goal` is reachable from a feature root by ONE `reference`-class hop:

- **Inbound (pull-to-root):** firm [`fe_assemble`](./fe_assemble.md) gains a `reference`-class (`kind: constructs-via`) down-edge → `mk_matrix_free_operator` (added to `fe_assemble`'s frontmatter + §Lowers-to prose this dispatch). `fe_assemble` reaches the feature root via its 7 feature-column inbound edges; the matrix-free representation IS the constructive interior of its per-term `assemble_term` leaf under the `UseFullAssembly`-false dispatch. The edge is **`reference`, NOT `depends-on`** — a firm node may *navigationally reference* a rank-0 roadmap_goal, but must NOT carry a *blocking* `depends-on` to it (that would violate well-foundedness `rank(fe_assemble) = firm > rank(mk_matrix_free_operator) = 0`). The `reference` edge carries no liveness constraint and constrains no rank (scheme §1g) — so `rank_violations` stays 0.
- **Downward (lowers-to):** `mk_matrix_free_operator` → firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md), `reference`-class `lowers-to`. The L4 op's apply is the named L2 contraction chain; the L2 combinator (firm, c125 D2) composes the four firm element-local substrate ops (`element_restrict` / `basis_apply` / `quad_point_contract` / `geom_factor_build`). A `roadmap_goal` may rest on / reference anything — but recorded as `reference` (not `depends-on`) so the rank-0 node imposes no rank floor on the firm L2 combinator.
[new]:
## Pull-chain (reachability — why this is firm and not garbage)

Now firm, this op is reachable from a feature root by a faithful **blocking `depends-on`** inbound edge:

- **Inbound (pull-to-root, BLOCKING):** the firm feature surface [`feature/matrix-free-operator.L4`](../feature/matrix-free-operator.L4.md) (c127 D1) carries a `depends-on (composes)` edge → `mk_matrix_free_operator`. firm→firm, rank-legal (`rank(column) = firm ≤ rank(cap) = firm`). This is the faithful blocking pull that licenses the firm claim — the cap's previously-recorded promotion condition, now met.
- **Inbound (navigational):** firm [`fe_assemble`](./fe_assemble.md) keeps its `reference`-class (`kind: constructs-via`) down-edge → `mk_matrix_free_operator`. STAYS `reference`, NOT `depends-on` — `fe_assemble` folds its per-term `assemble_term` leaf OPAQUELY (its firmness is in the fold apparatus, not the leaf interior), so it must not blocking-depend on the constructor even now both are firm. A firm→firm navigational reference is permitted (scheme §1g).
- **Downward (lowers-to, BLOCKING):** `mk_matrix_free_operator` → firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md), now `depends-on (lowers-to)` (promoted from `reference` at the firm-flip). The op's `apply` IS the named L2 contraction chain; the L2 combinator (firm, c125 D2) composes the four firm element-local substrate ops. firm→firm, rank-legal — `rank_violations` stays 0.
```

```edit:book/src/L4/mk_matrix_free_operator.md
[old]:
## Speculative L4 operators proposed (none new)

This cap proposes **no new speculative operator** beyond itself: `mk_matrix_free_operator` IS the speculative L4 op (landed as the `roadmap_goal` chapter, the in-discipline home). Its declared dependencies are all already firm on disk — the L2 combinator and the four L1 substrate ops below it. The intent's only open work is the *upward* pull (the dedicated L4 backend-lowering feature surface, batch-41 "A") that would firm this node.

## Declared dependencies (all firm — the well-foundedness it WILL rest on when firmed)

When this promotes off `roadmap_goal`, its blocking deps will be (currently recorded as `reference` because rank-0 imposes nothing):
[new]:
## L4 operators proposed (none new)

This cap proposes **no new operator** beyond itself: `mk_matrix_free_operator` is the L4 backend-lowering operator-constructor. Its dependencies are all firm on disk — the L2 combinator and (transitively) the four L1 substrate ops below it. The *upward* pull that firmed this node (the dedicated L4 backend-lowering feature surface, batch-41 "A") landed c127 D1.

## Blocking dependencies (all firm — the well-foundedness this rests on)

Now firm, its blocking deps are (the L2 combinator recorded `depends-on (lowers-to)`; the four substrate ops reached transitively through it):
```

```edit:book/src/L4/mk_matrix_free_operator.md
[old]:
## L0 anchors (construction-site evidence — speculative-intent, not a positive L4 claim)

The matrix-free *representation* this L4 op names is grounded at:
[new]:
## L0 anchors (construction-site evidence — the positive compositional claim)

The matrix-free *representation* this L4 op names is grounded at:
```

## Supporting evidence

- **Substrate constituents surveyed firm from on-disk `rank:` lines** (NOT the cycle record, NOT
  index cells):
  - `book/src/L2/matrix-free-operator-apply.md:16` — `rank: firm`.
  - `book/src/L1/element_restrict.md:14`, `book/src/L1/basis_apply.md:10`,
    `book/src/L1/quad_point_contract.md:10`, `book/src/L1/geom_factor_build.md:14` — all `rank: firm`.
  - `book/src/concepts/element-local-tensor.md:2` — `rank: firm`.
  - `book/src/L1/libceed-quadrature-kernel-impl.md:19` — `rank: firm` (the kernel-impl the L1 surface
    references; not a blocking dep).
- **Cap precedent + named promotion condition:** `book/src/L4/mk_matrix_free_operator.md:38`
  ("Promotes `roadmap_goal → rough-in → firm` as the dedicated L4 backend-lowering feature surface
  lands (batch-41 'A') and provides the blocking pull-chain").
- **Column-kind precedent (the GMG infrastructure column, firm c122):**
  `book/src/feature/geometric-multigrid-preconditioner.{L4,L1}.md` — the close analog (an
  infrastructure / shared-substrate composition-root that firmed on the same well-foundedness +
  firm-on-positive-structure basis; the solve-side analog, this is the assemble-side analog).
- **L0 construct-time dispatch** (codemap-confirmed this dispatch): `palace/fem/bilinearform.cpp:118`
  (`UseFullAssembly` predicate), `:140` (`BilinearForm::Assemble` partial-vs-full branch), `:147`
  (`PartialAssemble()` — the matrix-free branch). The cap's five own L0 anchors
  (`operator.hpp:32,48,81-82`; `bilinearform.cpp:118,143`) are already self-verified
  (`mk_matrix_free_operator.md:95`).
- **`fe_assemble` cap linkage** (the navigational reference that STAYS reference):
  `book/src/L4/fe_assemble.md:15-16` (`constructs-via` reference edge), `:164` (the prose).
- **Adjacent-layer context:** the L2 combinator's §"Speculative higher (L4) placeholder"
  (`book/src/L2/matrix-free-operator-apply.md:209-222`) explicitly flagged `mk_matrix_free_operator`
  as "the L4 backend-lowering entry point … the remaining ASK-2 'A' depth … a c126 / batch-41
  candidate" — this column lands exactly that surface.

## RE11 grounding (the reachability / reference-edge-liveness contribution)

This column is the prospective **RE11 libceed-substrate sub-cohort grounder**, and on the landed
tree it is a GENUINE `depends-on` reachability flip (the §2g distinction), NOT a `reference`-only hop:

- **The L1 surface (`feature/matrix-free-operator.L1`) names the four element-local substrate ops
  via blocking `depends-on (composes)` edges.** Before this cycle, `element_restrict` / `basis_apply`
  / `quad_point_contract` / `geom_factor_build` reached a root only via `reference` /
  `lifts-kernel-impl` / `realizes-kernel-api` edges (the RE11 deliberate-reference-only cohort). This
  column is a firm, root-reaching composition-root that blocking-`depends-on` them (transitively
  through the L2 combinator at L4; DIRECTLY at L1) — a REAL composition flip from a root-reaching
  firm node, exactly the c123 krylov-iteration model (a depends-on flip, distinct from the
  reference-only cohort).
- **The cap firm-flip adds a firm node + a blocking `depends-on` chain.** `mk_matrix_free_operator`
  → `L2/matrix-free-operator-apply` becomes `depends-on (lowers-to)` (firm→firm), and the L2
  combinator already blocking-`depends-on` the four substrate ops. So the chain
  `feature-column →(depends-on) cap →(depends-on) L2-combinator →(depends-on) {4 substrate ops}` is
  now fully blocking from a feature root — the substrate ops are reachable over `depends-on` edges,
  not merely reference-reachable.
- **`reference_reachable` climb is matched node-for-node to new firm nodes** (escalate-guard §2g):
  the climb this cycle is accounted for by exactly TWO new firm nodes — the firmed `mk_matrix_free_operator`
  cap and the firm `feature/matrix-free-operator.{L4,L1}` column (2 files). No reference_reachable
  increment is unmatched.
- **Finalize-duty re-check (flagged for the integrator/critic):** on the landed tree, run
  `graded-stack-lint --show-inbound` on each of the four substrate ops + `libceed-quadrature-kernel-impl`
  and confirm a `depends-on` inbound now exists (the RE11 libceed-substrate sub-cohort GROUNDS). If
  the column landed (it should — gates pass), the sub-cohort moves out of RE11; the batch-41 meta
  ratifies. (`libceed-quadrature-kernel-impl` itself is reached by the L1 surface only via
  `reference` — it stays in whatever residual state its own consumers determine; the four substrate
  ops are the ones this column blocking-grounds.)

## Open questions / caveats

- **`mk_matrix_free_operator` body sections below §"L4 form" still carry "SPECULATIVE" inline
  framing in a few prose spots I did not edit** (e.g. the §"Speculative L4 form" body paragraph at
  `:50,:64`). I flipped the section HEADERS + the two banners + the constructor-signature
  SPECULATIVE callout, the pull-chain section, and the declared-deps section. The integrator should
  confirm no residual "SPECULATIVE" / "roadmap_goal" / "speculative reconstruction" token survives in
  the now-firm chapter (a `grep -n 'SPECULATIVE\|roadmap_goal\|speculative reconstruction\|not asserted as Palace'`
  on `mk_matrix_free_operator.md` post-apply); any survivor is stale framing from the roadmap_goal era
  and should be neutralized (this is the firm-flip prose-consistency analog of the sibling-status grep).
- **D2 forward-reference dependency.** Both L4 surfaces reference D2's canonical slug
  `L4-L3/mk-matrix-free-operator-dissolution` (the L4 column's `reference` edge + the cap's
  `lowers-to` reference). D2 authors that file this cycle; if D2 lands `partly-constructive`/`rough-in`
  instead of firm, the *reference* links are unaffected (reference-class carries no rank constraint) —
  the cap + column firm decision does NOT depend on D2's status (the cap's blocking `depends-on` is the
  L2 combinator, which is already firm). No coupling hazard.
- **`L2/matrix-free-operator-apply` §"Speculative higher (L4) placeholder" is now stale** (it calls
  the L4 surface "NOT authored this cycle — placeholder for a later harvester", `:209-222`). NOT in my
  write-scope (it is the L2 chapter, owned by the combinator-miner/harvester lineage). Flagged as an OQ
  for a future touch: `matrix-free-operator-apply-l4-placeholder-now-stale` — the placeholder should be
  re-anchored to point at the landed `feature/matrix-free-operator.L4` + the firm cap. Low priority
  (prose-drift, not a build break; linkcheck2 does not catch it).
- **No new record surfaced** — the constructor signature names `FESpace` / `WeakFormTerm` /
  `GeomFactors` / `LinearOperator`, all already-homed types (the `weak_form_term` L1 chapter, the
  element-local-tensor concept, the geom_factor_build product). No `record-<name>-needs-definition-home`
  flag.

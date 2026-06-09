---
layer: L4-L3
theme: mk-matrix-free-operator-dissolution
kind: lowering-theme
# A firm L4>L3 lowering theme: the matrix-free constructive-INTERIOR dissolution.
# Dissolves the L4 `mk_matrix_free_operator` CONSTRUCTOR (whose `apply` is the backend-lowering
# contraction graph) into the L3 explicit element-iterated contraction sweep — the flat-`Tensor[(N: ...)]`
# → element-local rank-tensor vocabulary shift, composing the firm substrate ops + the firm L2 chain
# combinator BY NAME. The RE11 libceed-substrate-sub-cohort grounder.
rank: firm
edges:
  depends-on:
    # The RHS constituents this theme composes BY NAME — the L3 contraction-chain RHS is built from these.
    - target: L2/matrix-free-operator-apply   # the named contraction-chain combinator the apply lowers to
      kind: composes
    - target: L1/element_restrict             # G / Gᵀ — the [(N: ...)] ↔ [(E, L)] gather / scatter-add (the flat→element-local boundary)
      kind: composes
    - target: L1/basis_apply                  # B_𝒟 / B_𝒟ᵀ — the [(E, L)] ↔ [(E, P, C)] basis-eval contraction, keyed on 𝒟
      kind: composes
    - target: L1/quad_point_contract          # D — the pointwise [(E, P, C)] per-quad-point diagonal against the [(E, P, G)] geom carrier
      kind: composes
    - target: L1/geom_factor_build            # the build-stratum [(E, P, G)] geometry-factor carrier D contracts against
      kind: composes
  reference:
    - target: L4/mk_matrix_free_operator      # the L4 constructor cap this theme is the L4>L3 dissolution of (the LHS)
      kind: lowers
    - target: L4-L3/fe-assemble-fold-dissolution   # the OUTER-fold sibling whose opaque per-term leaf this theme is the constructive INTERIOR of (the scope boundary)
      kind: sibling
    - target: concepts/element-local-tensor   # the rank-structured shape family the contraction sweep is typed over
    - target: semantics/index                 # §1.2.1 named shape groups + §1.2.3 the element-local family — USED+LINKED, not restated
    - target: L4-L3/index
---

# mk-matrix-free-operator-dissolution

The L4>L3 lowering theme for the [`mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md)
**backend-lowering operator-constructor** — the L4 op that builds a matrix-free (un-materialized)
`LinearOperator` value whose `apply` is the burn/GPU tensor-contraction graph rather than a materialized
matrix-vector product. The theme dissolves the L4 constructor (the atomic `mk_matrix_free_operator space
term geom` build of a `LinearOperator` over the **flat operator-domain shape** `Tensor[(N: ...)]`, with the
`apply` named by its lowering to the firm L2 chain combinator) into the L3 **explicit element-iterated
contraction sweep** — the `Palace BilinearForm::PartialAssemble` construction + the `ceed::Operator::Mult`
apply, read at the L3 iteration-rotation tier. The genuine **vocabulary shift** the theme captures is the
flat global-dof `Tensor[(N: ...)]` → element-local rank-tensor (`[(E, L)]` / `[(E, P, C)]` / `[(E, P, G)]`)
reorganization, with the `element_restrict` `G` / `Gᵀ` gather/scatter-add as the **boundary** between the
two shape vocabularies, made explicit as a per-geometry-type element loop that the once-built L4 contraction
graph hides.

## Slug

`mk-matrix-free-operator-dissolution`

## Context

*Distinct from, and the constructive INTERIOR of, [`fe-assemble-fold-dissolution`](./fe-assemble-fold-dissolution.md).*

This theme is the **constructive interior** of the opaque per-term leaf that the sibling
[`fe-assemble-fold-dissolution`](./fe-assemble-fold-dissolution.md) bottoms out at. That theme
lowers the OUTER assemble-FOLD — `fe_assemble space terms = Σ_t assemble_term space t` → the L3 imperative
integrator-fold over the two integrator containers, accumulating per-term sub-operators by `AddSubOperator` —
and treats each per-term `assemble_term` leaf as an `obstruction (opaque-library-ownership)` libCEED boundary,
explicitly putting the matrix-free interior OUT of scope (`fe-assemble-fold-dissolution.md:125-126,:218` §"What
this lowering does NOT cover"). **The matrix-free constructive interior of that leaf was therefore genuinely
un-authored at L4>L3** — and this theme authors it: under the matrix-free (`UseFullAssembly` false) dispatch,
the per-term operator IS the un-materialized `ceed::Operator` whose `apply` is the five-stage contraction
chain. Where `fe-assemble-fold-dissolution` records the leaf as opaque, this theme renders the leaf's `apply`
as the named composition of the firm element-local substrate ops — the RE11 libceed-substrate sub-cohort
GROUNDING condition (a faithful `depends-on` consumer naming the substrate ops, not the opaque libCEED leaf).

The two themes are **complementary, non-overlapping** scope partitions of the FE-operator construction surface:

- [`fe-assemble-fold-dissolution`](./fe-assemble-fold-dissolution.md) — the OUTER assemble-fold over an
  OPAQUE per-term leaf (`K = Σ_t assemble_term space t`; the homomorphic map-then-reduce). Per-term leaf:
  opaque libCEED boundary, NOT lowered.
- `mk-matrix-free-operator-dissolution` (this theme) — the per-term leaf's matrix-free `apply` INTERIOR
  (`A·v = Gᵀ(B_𝒟ᵀ(D ⊙ (B_𝒟(G·v))))`; the five-stage element-local contraction sweep). The interior IS lowered,
  composing the firm substrate ops by name.

The rotation direction is **L4 → L3**, narrated forward per the high→low discipline (CLAUDE.md §Methodology
invariants "Layers are defined high→low"). Notes about the reverse lift (how the L3 explicit element sweep
lifts back into the once-built L4 contraction-graph constructor, what licenses recovering the build/run
stratification) are not in this formal chapter.

The shape-group notation (`(N: ...)` operator-domain congruence group §1.2.1; the element-local rank-tensor
family `[(E, L)]` / `[(E, P, C)]` / `[(E, P, G)]` §1.2.3) is governed by
[`semantics/index`](../semantics/index.md) and the firm record page
[`concepts/element-local-tensor`](../concepts/element-local-tensor.md) — **USED + LINKED here, not restated**
(SEMANTIC CONSOLIDATION directive; the general teaching lives once on the surface).

## L4 form (LHS)

The L4 [`mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md) constructor (the firm cap; the
backend-lowering operator-constructor). Transcribed from the cap §"Speculative L4 form":

    -- the operator-CONSTRUCTOR: build (once) a matrix-free LinearOperator value over the FLAT
    -- operator-domain shape Tensor[(N: ...)]; its `apply` is a contraction graph, not a CSR spmv.
    mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> Op[Tensor[(N: ...)] → Tensor[(N: ...)]]

    -- the `apply` is named by its lowering to the firm L2 chain combinator (the reference-class
    -- `lowers-to` edge), an ATOMIC five-stage contraction over the flat operator-domain shape:
    apply (mk_matrix_free_operator space term geom) v
      = matrix-free-operator-apply space term geom v          -- the firm L2 combinator
      = (Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G) v

The L4-form machinery this theme dissolves is **three** pieces:

1. **The atomic constructor build + the build/run stratification.** `mk_matrix_free_operator space term geom`
   is one atomic L4 step producing a `LinearOperator` value — the contraction graph (restriction index map +
   tabulated basis + precomputed geometry factor) is wired ONCE at construction and the per-`apply` matvec
   re-runs it. The build (setup) stratum and run (apply) stratum are split by the constructor/apply boundary
   ([`concepts/build-time-vs-run-time-stratification`](../concepts/build-time-vs-run-time-stratification.md)) —
   but at L4 the build is a single opaque atomic step; the *iteration over element-geometry families* it must
   perform is hidden.

2. **The flat operator-domain shape `Tensor[(N: ...)]`.** The L4 `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` is typed
   over the **flat global true-dof axis** — the operator-domain congruence group `(N: ...)`
   ([`semantics/index`](../semantics/index.md) §1.2.1). At L4 the operator is a black box over this flat shape;
   the element-local rank structure it traverses internally (`[(E, L)]` / `[(E, P, C)]` / `[(E, P, G)]`,
   §1.2.3) is below the L4 surface.

3. **The geometry factor carried as one opaque `GeomFactors` argument.** `geom : GeomFactors` is the
   build-stratum geometry-factor carrier (the firm [`geom_factor_build`](../L1/geom_factor_build.md) product),
   passed as a single constructor argument; at L4 its per-element-geometry-type internal structure (one
   geometry factor per `(geom-type, element)`, the `[(E, P, G)]` shape) is opaque.

The load-bearing L4 property this lowering transports is the cap's apply-lowering identity (the
`reference`-class `lowers-to` edge to the firm L2 combinator): `apply (mk_matrix_free_operator space term
geom) = matrix-free-operator-apply space term geom = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`, and the L2 combinator's
**linearity**, the **`Gᵀ … G` symmetry sandwich**, and the **element-additivity of the scatter-add**
([`matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) §"Composition-level laws") — the
properties of the composed contraction that the L3 element sweep must preserve.

## L3 form (RHS)

The L4>L3 dissolution produces the L3 **explicit element-iterated contraction sweep** — the Palace C++
`BilinearForm::PartialAssemble` construction (`bilinearform.cpp:28-107`) + the `ceed::Operator::Mult` apply
(`operator.cpp:182-189`), read at the L3 iteration-rotation tier. The L3 rendering (in the L3 value-thread
vocabulary, composing the firm substrate ops BY NAME):

```text
-- L3 explicit element-iterated contraction sweep: the once-atomic L4 constructor dissolves into a
-- per-geometry-type element loop building the restriction/basis/geom-data context per geometry type;
-- the once-atomic L4 `apply` dissolves into the five-stage rank-tensor contraction over the element
-- families, with `element_restrict`'s G as the FLAT→ELEMENT-LOCAL shape boundary.
mk_matrix_free_operator_L3 :: (space, term, geom) -> LinOp[(N: ...), $N]
mk_matrix_free_operator_L3 space term geom =
  let op = make_composite_operator space         -- 1. mutable composite ceed::Operator accumulator
  let _  =                                        -- 2. loop the per-geometry-type element families
        for_each (mesh.GetCeedGeomFactorData ceed) (\(geom_type, data) ->   -- bilinearform.cpp:54
          let restr  = element_restrict_context space geom_type data.indices   -- G / Gᵀ index map  (:65,:67)
          let basis  = basis_context space geom_type                            -- B_𝒟 tabulated basis (:68,:69)
          let geomd  = data.geom_data                                           -- D's [(E,P,G)] carrier (:75)
          let sub_op = assemble_subop_for_term term restr basis geomd           -- the per-term sub-operator
          in op.AddSubOperator(sub_op))                                          -- accumulate            (:77)
  let _  = op.Finalize()                                                         --                       (:104)
  in op   -- the composite whose `apply`/`Mult` runs the five-stage contraction sweep below

-- the apply (run-stratum): ceed::Operator::Mult — the five-stage element-local rank-tensor contraction
apply op v =
    v   |> element_restrict restr                  -- G   :: Tensor[(N: ...)] -> Tensor[(E, L)]   (flat→element-local)
        |> basis_apply (mode-of 𝒟) basis           -- B_𝒟 :: [(E, L)]    -> [(E, P, C)]
        |> quad_point_contract geomd               -- D   :: [(E, P, C)] -> [(E, P, C')]  (pointwise, against [(E, P, G)]; C' = test components, = C in the symmetric trial==test case)
        |> basis_apply (transpose (mode-of 𝒟)) basis  -- B_𝒟ᵀ :: [(E, P, C)] -> [(E, L)]
        |> element_restrict_transpose restr        -- Gᵀ  :: [(E, L)]    -> Tensor[(N: ...)]  (scatter-ADD; element-local→flat)
        |> dof_multiplicity_scale                  -- y *= dof_multiplicity  (shared-dof averaging, single-rank)
```

where:

- **`make_composite_operator space`** is the composite `ceed::Operator` / `ceed::SymmetricOperator`
  construction (`bilinearform.cpp:37-46`, by trial/test coincidence) — the mutable accumulator the per-element-
  geometry-type sub-operators reduce into; the L4 atomic constructor's allocation.
- **`for_each (mesh.GetCeedGeomFactorData ceed)`** is the **explicit per-geometry-type element loop**
  (`bilinearform.cpp:54`, `for (const auto &[geom, data] : mesh.GetCeedGeomFactorData(ceed))`) — the loop the
  once-atomic L4 constructor build HIDES. Each geometry type (volume vs boundary, full-dimension vs
  dimension−1) gets its own restriction/basis context. This is the iteration-rotation content of the
  constructor.
- **`element_restrict_context` / `basis_context`** are the per-geometry-type `CeedElemRestriction` /
  `CeedBasis` builds (`bilinearform.cpp:65,67` `GetCeedElemRestriction`; `:68,:69` `GetCeedBasis`) — the build
  of the `G` index map and `B_𝒟` tabulated basis the contraction sweep applies.
- **`data.geom_data`** is the precomputed `[(E, P, G)]` geometry-factor carrier (`bilinearform.cpp:75`,
  the `data.geom_data` / `data.geom_data_restr` arguments) — the firm
  [`geom_factor_build`](../L1/geom_factor_build.md) product the pointwise `D` contracts against.
- **`assemble_subop_for_term` + `op.AddSubOperator`** (`bilinearform.cpp:75,:77`) build and accumulate the
  per-term matrix-free sub-operator; under the matrix-free dispatch this is the un-materialized `ceed::Operator`
  whose action is the contraction chain (NOT a materialized matrix — the `UseFullAssembly` false branch,
  `bilinearform.cpp:118,:143`).
- **`apply op v` / `ceed::Operator::Mult`** (`palace/fem/libceed/operator.cpp:182-189`: `y = 0.0; CeedAddMult(op, u, v, x, y);
  if (dof_multiplicity.Size() > 0) y *= dof_multiplicity;`) is the **five-stage element-local rank-tensor
  contraction** — the un-materialized matvec. This is where the genuine vocabulary shift lives: the flat
  `Tensor[(N: ...)]` input is gathered by `G` into `[(E, L)]`, basis-applied to `[(E, P, C)]`, contracted
  pointwise against `[(E, P, G)]`, transposed back, scatter-added by `Gᵀ` to flat `Tensor[(N: ...)]`.

The dissolution is **three** coordinated rewrites, one per piece of L4 constructor machinery — each a genuine
vocabulary translation, NOT a rename:

### 1. Atomic constructor build → explicit per-geometry-type element loop

The L4 atomic `mk_matrix_free_operator space term geom` build dissolves into the L3 explicit
`for (const auto &[geom, data] : mesh.GetCeedGeomFactorData(ceed))` per-geometry-type element loop
(`bilinearform.cpp:54`), each iteration building the geometry-type's restriction/basis context and
accumulating a per-term sub-operator into the mutable composite by `AddSubOperator` (`:77`), finalized by
`Finalize()` (`:104`). The once-atomic L4 constructor (one opaque build step) collapses to a first-order
positional loop over the element-geometry families that mutates a running composite operator — the
**build/run stratification's build half** rendered explicitly as the element-geometry iteration. The L4
constructor/apply split (build the graph once, run per apply) survives at L3 as the loop being OUTSIDE the
`Mult` (the context is built once at construction, the contraction re-runs per matvec) — but at L3 it is a
coding-convention placement (the loop sits in `PartialAssemble`, the contraction in `Mult`), not a type-level
stratification.

### 2. Flat-`Tensor[(N: ...)]` black-box apply → the five-stage element-local rank-tensor contraction

The L4 `apply` over the flat operator-domain shape `Tensor[(N: ...)]` (an atomic black-box matvec named only
by its lowering to the L2 combinator) dissolves into the L3 explicit five-stage **rank-tensor contraction
sweep** (`ceed::Operator::Mult`, `operator.cpp:182-189`) composing the firm substrate ops BY NAME:
`element_restrict` (`G` / `Gᵀ`), `basis_apply` (`B_𝒟` / `B_𝒟ᵀ`), `quad_point_contract` (`D`). **This is THE
genuine vocabulary shift of the theme**: the flat global true-dof shape `Tensor[(N: ...)]` (the BLAS-1 /
operator-domain vocabulary) is reorganized into the element-local rank-tensor vocabulary `[(E, L)]` →
`[(E, P, C)]`, with `element_restrict`'s `G` / `Gᵀ` as the **boundary** between the two shape vocabularies
(`semantics/index` §1.2.3: "the restriction `G` / `Gᵀ` is the boundary between the two" — the flat `N` axis vs
the element-local family). The L4 form is opaque in `Tensor[(N: ...)]`; the L3 form makes the element-local
rank structure explicit. This is **not** an identity-in-named-terms rename — the L4 vocabulary has NO
`E`/`L`/`P`/`C`/`G` axes at all; they appear only when the flat black-box apply is dissolved into the
element-iterated contraction. The L4 apply-lowering identity (`apply = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`, the cap's
`lowers-to`) is exactly what licenses this rewrite — the L2 combinator names the chain; this theme renders it
as the L3 element sweep.

### 3. Opaque `GeomFactors` argument → the per-geometry-type `data.geom_data` `[(E, P, G)]` carrier

The L4 `geom : GeomFactors` (one opaque constructor argument) dissolves into the L3 per-geometry-type
`data.geom_data` (`bilinearform.cpp:75`) — the precomputed `[(E, P, G)]` geometry-factor carrier built per
element-geometry family by the firm [`geom_factor_build`](../L1/geom_factor_build.md) setup pass, that the
pointwise `quad_point_contract` `D` stage contracts against (`D ⊙ ·`, the per-quad-point diagonal). At L4 the
geometry factor is an opaque whole; at L3 it is the rank-structured `[(E, P, G)]` tensor indexed per
`(geom-type, element, quad-point, geom-factor-component)`. The opaque `GeomFactors` → the `[(E, P, G)]`
rank-tensor carrier is the third vocabulary shift (a sub-shift of the §2 flat→element-local reorganization,
on the build-stratum factor).

### What does NOT change in the rotation

The **per-term contraction dataflow** survives the rotation unchanged — the five-stage `Gᵀ B_𝒟ᵀ D B_𝒟 G`
pipeline composition is identical at L4 (named by the L2 combinator) and L3 (rendered as the element sweep);
the rotation touches only the **shape vocabulary** (flat `Tensor[(N: ...)]` → element-local rank tensors) and
the **iteration structure** (atomic constructor build → explicit per-geometry-type element loop). The
**element-independence** survives at L3: each element's local contraction reads only its own restricted dofs +
the shared basis + its own geometry factor, with no cross-element coupling EXCEPT the `Gᵀ` scatter-add (which
accumulates each element's contribution into shared global dofs) — the embarrassing-parallelism the element
loop licenses is preserved (and exploited: one `Ceed` per OMP thread, `bilinearform.cpp:50-105`-region). The
element loop carries **NO `sequential-obstruction`** (the load-bearing alignment with the
`solve_family`/`fe_assemble` homomorphic family-loop branch — the element map is embarrassingly parallel; the
only cross-element write is the commutative/associative `Gᵀ` scatter-add).

### What this lowering does NOT cover

- **The OUTER assemble-fold over the term family.** The `K = Σ_t assemble_term space t` reduction over the
  weak-form term list is the sibling [`fe-assemble-fold-dissolution`](./fe-assemble-fold-dissolution.md)
  — that theme lowers the per-term FOLD; this theme lowers a SINGLE term's matrix-free `apply`
  INTERIOR. (The `for_each (domain_integs ++ boundary_integs)` per-term loop nested inside the per-geometry-
  type loop at `bilinearform.cpp:71-77`/`:90-97` is the fold sibling's content; this theme's per-term sub-op
  is one iteration of it.)
- **Sum-factorization** (the `B_𝒟` tensor-product 1-D contraction factoring) is a **transparent performance
  trick** (CLAUDE.md §Optimization tricks) classified as such at [`basis_apply`](../L1/basis_apply.md):68-74:
  the L3 form is the **unfolded** dense `B_𝒟` contraction; the sum-factorized 1-D-sweep evaluation order is a
  one-line `// Timing:` note on the `basis_apply` stage (it changes the contraction order, not the result —
  algebraically equivalent), NOT a separate algebraic claim. USED + LINKED to the `basis_apply` classification,
  not re-derived.
- **The full-assembly (materialized CSR) representation variant.** `mk_matrix_free_operator` IS the partial /
  un-materialized branch (`UseFullAssembly` false, `bilinearform.cpp:143`); the `CeedOperatorFullAssemble`
  CSR materialization (`operator.cpp:483` / `bilinearform.cpp:110`-region `FullAssemble`) is the alternative
  `full` representation — a **derived materialization of the same contraction** (the L2 combinator §"Matrix-free
  vs assembled-COO duality"), absorbed as a Palace-owned variant axis on the cap, NOT part of this matrix-free-
  interior rotation.
- **The opaque libCEED kernel interior.** This theme renders the apply as the named composition of the firm
  substrate ops (`element_restrict` / `basis_apply` / `quad_point_contract`) — the **kernel-IMPL** vocabulary
  ([`libceed-quadrature-kernel-impl`](../L1/libceed-quadrature-kernel-impl.md), the in-our-tensor-
  algebra realization). The opaque libCEED CALL itself (`integ->Assemble` → libCEED, the **kernel-API** surface)
  is the [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md)
  `obstruction (opaque-library-ownership)` boundary. This theme composes the kernel-IMPL substrate (the firm
  from-our-primitives version), it does not re-document the kernel-API boundary.

## L3-entry-vs-dissolution-home verdict

**WARRANT-FIRST per the vocabulary-shift redirect. The verdict is DISSOLUTION-HOME (no interposed
`L3/mk_matrix_free_operator` entry)** — matching the `solve_family` / `fe_assemble` NO-ENTRY
shape. The decision criterion (per the `fold_solve` L3-ENTRY precedent): **does the L3 image carry a
`sequential-obstruction` or `partial-obstruction` that warrants a standing iteration-rotation chapter?**

- The per-geometry-type element loop carries **NO `sequential-obstruction`** — the elements are independent;
  the only cross-element write is the commutative/associative `Gᵀ` scatter-add (element-additivity, the L2
  combinator's Law 3). The element map lifts (and is exploited in parallel, one `Ceed` per OMP thread).
- The apply contraction sweep is a **fixed five-stage pipeline**, not a carry-threaded loop — no recurrence,
  no inner-iteration obstruction.

So the L3 image of the matrix-free constructor is fully expressed by this theme's §"L3 form (RHS)"; a standalone
`L3/mk_matrix_free_operator` chapter would be a degenerate identity-in-named-terms mirror of that RHS (the §1d
smell). This theme is the **authoritative L3-form home** for the matrix-free constructor's interior. Re-openable
ONLY if a genuine non-independent iteration surfaces in the matrix-free apply (none has — the contraction sweep
is a fixed pipeline; the element loop is an embarrassingly-parallel map). Note the existing
[`L3/apply_linop`](../L3/apply_linop.md) opaque-matvec gate is the OPPOSITE end — it is the representation-agnostic
black-box matvec; this theme renders the matrix-free representation's CONSTRUCTIVE matvec interior, so it
complements (does not duplicate) the gate.

## Applicability conditions

The rewrite is valid when all four hold (the first three are the matrix-free-interior conditions; the fourth is
the partial-assembly-representation condition):

1. **The operator is a matrix-free (un-materialized) FE operator over a standard FE basis.** The element basis
   is nodal-Lagrange / Nédélec / Raviart-Thomas / L2 with a tabulated `CeedBasis`
   ([`basis_apply`](../L1/basis_apply.md) §Applicability) — true for all in-scope Palace FE operators. The
   apply is the contraction chain, not a materialized spmv.
2. **The geometry factor is precomputed per element-geometry family.** `data.geom_data` is built once per
   `(mesh, FE order, quadrature rule)` by the [`geom_factor_build`](../L1/geom_factor_build.md) setup pass
   (`bilinearform.cpp:54` `GetCeedGeomFactorData`); the run-time apply contracts against it pointwise. This is
   what lets the build/run stratification dissolve into the loop-outside-`Mult` placement.
3. **The element contractions are independent (no `sequential-obstruction`).** Each element's local contraction
   reads only its own restricted dofs + shared basis + its own geometry factor; the only cross-element write is
   the `Gᵀ` scatter-add (commutative/associative). This is what makes the element loop carry no obstruction and
   the rotation a DISSOLUTION-HOME (no L3 iteration-rotation chapter).
4. **The matrix-free / partial-assembly representation is selected.** `UseFullAssembly` is false
   (`bilinearform.cpp:118,:143`) — the operator stays un-materialized. When `UseFullAssembly` is true the
   operator is materialized to CSR (`FullAssemble` / `CeedOperatorFullAssemble`) — a derived materialization of
   the same contraction, the `full` variant absorbed by the cap, NOT covered by this matrix-free-interior theme.

## Justification kind

**`structural`** with secondary **`reduction-chain`**.

- **Structural** (dominant): the L4 constructor machinery (the atomic build, the flat-`Tensor[(N: ...)]`
  black-box apply, the opaque `GeomFactors` argument) dissolves into the L3 explicit element-iterated contraction
  sweep; every L4 piece becomes an L3 piece at the same dataflow position — atomic build → per-geometry-type
  element loop, flat black-box apply → five-stage rank-tensor contraction, opaque `GeomFactors` → `[(E, P, G)]`
  per-geometry carrier. Read **directly off positive Palace source**: the per-geometry-type element loop +
  context build + `AddSubOperator` accumulation + `Finalize` are witnessed exactly by
  `BilinearForm::PartialAssemble` (`bilinearform.cpp:28-107`); the five-stage apply is witnessed by
  `ceed::Operator::Mult` (`operator.cpp:182-189`); the contraction-stage decomposition is the firm
  [`matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) combinator + the firm substrate ops, all
  read off the `AssembleCeedOperator` master assembler field-wiring.
- **Reduction-chain** (secondary): the once-atomic L4 constructor build desugars to the explicit positional
  per-geometry-type `for` accumulating sub-operators by `AddSubOperator`; the once-atomic L4 black-box apply
  desugars to the five-stage `|>`-pipe contraction over the element-local tensors. The substrate ops'
  contraction laws are NOT restated (USE + LINK; see those chapters); only the composition-level rotation is
  the reduction-chain content.

**Abstraction-direction note**: L4 is the higher-abstraction layer (the atomic operator-constructor over the
flat operator-domain shape, the build/run stratification implicit in the constructor/apply split, the opaque
geometry-factor argument). L3 is the lower-abstraction layer (the explicit per-geometry-type element loop, the
five-stage rank-tensor contraction sweep over `[(E, L)]` / `[(E, P, C)]` / `[(E, P, G)]`, the per-geometry
`data.geom_data` carrier). The rotation direction is **L4 → L3**, narrated forward per the high→low discipline.

## Speculative L4 operators

None. This theme lowers the already-authored L4 constructor
([`mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md)) assembled
from the already-firm L2 chain combinator + the four firm L1 substrate ops. No new speculative operator is
introduced; the RHS constituents are all firm on disk.

## Evidence

L4 source (the LHS of this rewrite):

- `book/src/L4/mk_matrix_free_operator.md` — the L4 backend-lowering operator-constructor:
  §Intent (the constructor/apply split, the `partial matrix-free` branch), §"Speculative L4 form" (the
  `mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> Op[Tensor[(N: ...)] → Tensor[(N: ...)]]`
  signature + the `apply = matrix-free-operator-apply space term geom = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` lowering), the `lowers-to`
  edge to the L2 combinator this theme realizes as the L3 element sweep.
- `book/src/L2/matrix-free-operator-apply.md` — the named contraction-chain combinator the L4
  apply lowers to; the source of the five-stage pipe + the composition-level laws (linearity, the `Gᵀ … G`
  symmetry sandwich, element-additivity of the scatter-add) the L3 sweep preserves.
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the kernel-IMPL home of the concrete chain
  `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` (the constructive substrate this theme composes by name; the kernel-IMPL, NOT the
  kernel-API boundary).
- `book/src/L4-L3/fe-assemble-fold-dissolution.md` — the OUTER-fold SIBLING whose opaque per-term
  leaf this theme is the constructive INTERIOR of; the scope boundary (`:125-126,:218` §"What this lowering does
  NOT cover" puts the matrix-free interior out of its scope — this theme authors it).

L3 source (the RHS of this rewrite):

- **No `book/src/L3/mk_matrix_free_operator.md`** — DISSOLUTION-HOME verdict (§"L3-entry-vs-dissolution-home
  verdict"): the per-geometry-type element loop carries no `sequential-obstruction` (independent elements; the
  scatter-add is commutative), so the L3 matrix-free-constructor form is fully expressed by this theme's §"L3
  form (RHS)"; a standalone L3 chapter would mirror it (the vocabulary-shift redirect anti-mirror principle,
  matching the `solve_family`/`fe_assemble` NO-ENTRY verdicts). This theme is the authoritative L3-form home.
- `book/src/L0/fem-bilinearform-file.md` (firm L0 navigation) — independently names the `BilinearForm` /
  `ceed::Operator` matrix-free construction; corroborates the L3 RHS shape.

L0 evidence (the matrix-free construction + apply witness):

- **The Palace-owned matrix-free constructor (the L3 RHS home)** (`palace/fem/bilinearform.cpp`):
  - `:28-107` — `BilinearForm::PartialAssemble` — the whole matrix-free construction body (`return op;` at `:106`, `}` at `:107`).
  - `:37-46` — the composite `ceed::Operator` / `ceed::SymmetricOperator` construction (the mutable accumulator;
    the L4 constructor allocation).
  - `:54` — `for (const auto &[geom, data] : mesh.GetCeedGeomFactorData(ceed))` — the explicit
    **per-geometry-type element loop** the once-atomic L4 constructor hides.
  - `:65,:67` — `trial_restr`/`test_restr` `GetCeedElemRestriction` — the per-geometry-type `G` / `Gᵀ` index map build.
  - `:68,:69` — `trial_basis`/`test_basis` `GetCeedBasis` — the per-geometry-type `B_𝒟` tabulated basis build.
  - `:75` — `integ->Assemble(ceed, trial_restr, test_restr, trial_basis, test_basis, data.geom_data,
    data.geom_data_restr, &sub_op)` — the per-term sub-operator build, consuming the `[(E, P, G)]`
    `data.geom_data` carrier (the kernel-API CALL; this theme composes the kernel-IMPL interior, not the CALL).
  - `:77` — `op->AddSubOperator(sub_op)` — the per-term sub-operator accumulation into the composite.
  - `:104` — `op->Finalize()` — the composite finalize.
  - `:118,:143` — `UseFullAssembly` predicate + the `if (UseFullAssembly(...))` partial-vs-full branch (this
    constructor IS the `partial` / un-materialized branch — the matrix-free-representation condition).
- **The matrix-free apply (the contraction-sweep witness)** (`palace/fem/libceed/operator.cpp`):
  - `:182-189` — `Operator::Mult`: `y = 0.0; CeedAddMult(op, u, v, x, y); if (dof_multiplicity.Size() > 0)
    y *= dof_multiplicity;` — the un-materialized matvec (the five-stage element-local contraction sweep + the
    shared-dof `dof_multiplicity` post-scale, read single-rank).
  - `:483` — `CeedOperatorAssembleCOO` — the derived assembled-COO materialization (the `full` variant; out of
    this theme's scope, named for the boundary).

Concept-page references:

- [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) — the `[(E, L)]` /
  `[(E, P, C)]` / `[(E, P, G)]` rank-tensor shape family the contraction sweep is typed over; the genuine
  vocabulary shift away from flat `Tensor[(N: ...)]`. The definition home — USED + LINKED, not restated.
- [`semantics/index`](../semantics/index.md) §1.2.1 (named shape groups, the flat `(N: ...)` operator-domain
  group) + §1.2.3 (the element-local family; "the restriction `G` / `Gᵀ` is the boundary between the two") —
  the governing surface for the shape vocabulary; USED + LINKED, not restated (SEMANTIC CONSOLIDATION).
- [`concepts/build-time-vs-run-time-stratification`](../concepts/build-time-vs-run-time-stratification.md) —
  the build (per-geometry context + geom-factor) vs run (per-`Mult` contraction) stratification the
  constructor/apply split realizes.

## Structural notes

**The vocabulary shift is genuine — not degenerate.** The theme is a genuine translation, NOT
an identity-in-named-terms rename (the §1d smell). The L4 vocabulary carries **NO** element-local rank axes
(`E`/`L`/`P`/`C`/`G`) — the L4 operator is a black box over the flat operator-domain shape `Tensor[(N: ...)]`;
those axes appear ONLY when the flat black-box apply is dissolved into the element-iterated contraction sweep,
with `element_restrict`'s `G` / `Gᵀ` as the boundary between the flat and element-local shape vocabularies
(`semantics/index` §1.2.3). The flat→element-local shape reorganization + the atomic-build→explicit-element-loop
iteration shift are the substance of the rotation. The rotation shape is a syntactic-structural fact on positive
source; the firm L1 kernel-impl additionally carries an empirical-match anchor `test-libceed.cpp:284,:339`
confirming the contraction realizes the kernel faithfully to 1e-12.

**Scope boundary vs `fe-assemble-fold-dissolution`.** This theme covers the matrix-free
constructive INTERIOR of the per-term leaf that [`fe-assemble-fold-dissolution`](./fe-assemble-fold-dissolution.md)
treats as an `obstruction (opaque-library-ownership)` opaque boundary (and explicitly puts OUT of its scope,
`:125-126,:218`). The two are complementary, non-overlapping: `fe-assemble-fold-dissolution` lowers the OUTER
term-FOLD over the opaque leaf; this theme lowers a SINGLE term's matrix-free apply interior, composing the
firm kernel-IMPL substrate ops by name.

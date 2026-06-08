---
layer: L2
operator: matrix-free-operator-apply
# Graded-stack scheme. This is a `firm` (rank 3) L2 combinator: the named contraction-chain
# composition of the four firm element-local substrate ops that realizes FE matrix-free operator
# application A = Gᵀ B_𝒟ᵀ D B_𝒟 G over the `concepts/element-local-tensor` shape family. It is a
# constructive-kernel COMPOSITION (a new L2 cohort kind), distinct from the BLAS-1 fold cohorts.
# Well-foundedness: its four `depends-on (composes)` substrate deps are all firm, so
# `rank(combinator) <= min(deps) = firm` permits firm; the composition is positively sourced
# (AssembleCeedOperator master + Operator::Mult apply) and its laws are syntactic-identity
# composition facts (firm-on-positive-structure escape — no test gates a composition identity).
# Pulled-by: `fe_assemble` (firm spine consumer) reaches the feature root via the fe_assemble
# fold's 7 feature-column inbound edges — the L1 kernel-impl this lifts is reachable, and this L2
# combinator inherits that reachability through its `reference`-class lift edge to the kernel-impl.
rank: firm
edges:
  depends-on:
    # The four element-local substrate ops this combinator COMPOSES BY NAME (all firm).
    # `composes` = the L2 combinator is built from these L1 verbs; rank-constrained, GC-live.
    - target: L1/element_restrict        # G / Gᵀ — the [(N: ...)] ↔ [E, L] gather / scatter-add boundary
      kind: composes
    - target: L1/basis_apply             # B_𝒟 / B_𝒟ᵀ — the [E, L] ↔ [E, P, C] basis-eval contraction, keyed on the term's 𝒟
      kind: composes
    - target: L1/quad_point_contract     # D — the pointwise [E, P, C] per-quad-point diagonal against the [E, P, G] geom carrier
      kind: composes
    - target: L1/geom_factor_build       # the setup-stratum [E, P, G] geometry-factor carrier D contracts against
      kind: composes
  reference:
    - target: L1/libceed-quadrature-kernel-impl
      kind: lifts-kernel-impl   # the L1 kernel-impl this combinator NAMES at L2 (free, navigational — the L2 form is the named composition of the same chain; the L1 impl is the concrete realization; identity-in-named-terms rotation, in-line note below, NOT a separate L2-L1 theme)
    - target: L1/fe_assemble             # the firm fold K = Σ_i A(space, term_i) whose per-term leaf A IS this combinator's product (the consumer that pulls this to the feature root)
    - target: L1/weak_form_term          # (Q, 𝒟) — 𝒟 selects the basis_apply EvalMode B_𝒟; Q enters the quad_point_contract D
    - target: concepts/element-local-tensor   # the rank-structured shape family the whole chain is typed over (firm)
    - target: concepts/tensor-field-lift      # the pointwise D stage is the per-quad-point lift — the GPU-tensor backend-lowering form
    - target: concepts/build-time-vs-run-time-stratification  # G/B/geom are build-stratum; the [E, P, C] value tensor is the run-stratum transient
---

# matrix-free-operator-apply

The named L2 **contraction-chain combinator** for **matrix-free FE operator application** — the
composition that realizes one weak-form term's element-local→global linear operator
`A(space, (Q, 𝒟))` as a fold of the four firm element-local substrate verbs over the
[`element-local-tensor`](../concepts/element-local-tensor.md) shape family. It is the L2 home of the
five-stage pipeline that the L1 [`libceed-quadrature-kernel-impl`](../L1/libceed-quadrature-kernel-impl.md)
realizes concretely and that the firm [`fe_assemble`](../L1/fe_assemble.md) fold
`K = Σ_i A(space, term_i)` sums per-term. This contraction shape — a sequence of tensor contractions
over the element axis `E` and quad-point axis `P` — **is** the burn/GPU matrix-free backend-lowering
target (the reason `concepts/element-local-tensor` is the genuine vocabulary shift away from the flat
`Tensor[N]` BLAS L1).

## L2 form (the named contraction-chain combinator)

Writing `term = (Q, 𝒟)` (a [`weak_form_term`](../L1/weak_form_term.md): coefficient `Q`,
differential-operator `𝒟 ∈ {Identity, Gradient, Curl, Divergence}`), the combinator is the
**pipe of the four substrate verbs** over the element-local-tensor family:

```text
matrix-free-operator-apply
  :: ElemRestriction -> Basis -> GeomData -> Coefficient
  -> LinOp[(N: ...), $N]
-- one term's element-local→global linear operator, as a contraction-chain fold

apply (A = mk-operator restr basis geom Q) :: Tensor[(N: ...)] -> Tensor[(N: ...)]
apply A x =
    x   |> element_restrict restr            -- G   :: [(N: ...)] -> [E, L]
        |> basis_apply (mode-of 𝒟) basis     -- B_𝒟 :: [E, L]    -> [E, P, C]
        |> quad_point_contract geom           -- D   :: [E, P, C] -> [E, P, C'] (pointwise, against [E, P, G]; C' = test components, = C in the symmetric trial==test case)
        |> basis_apply (transpose (mode-of 𝒟)) basis   -- B_𝒟ᵀ :: [E, P, C] -> [E, L]
        |> element_restrict_transpose restr   -- Gᵀ  :: [E, L]    -> [(N: ...)]  (scatter-ADD)
```

That is the named form of `A = Gᵀ ∘ B_𝒟ᵀ ∘ D(Q, geom) ∘ B_𝒟 ∘ G`. The combinator's two strata:

- **`mk-operator`** (build / setup-stratum) — wires the operator from the restriction index map, the
  tabulated basis, and the precomputed [`geom_factor_build`](../L1/geom_factor_build.md) geometry
  carrier `geom :: Tensor[(E, P, G)]`. Build-stratum: fixed once per `(mesh, FE order, quadrature
  rule)`, rebuilt only on mesh change (e.g. AMR refinement). This is the Palace
  `AssembleCeedOperator` master assembler (`palace/fem/libceed/integrator.cpp:422-445`).
- **`apply`** (run-stratum) — the five-stage contraction fold above, evaluated per matrix-vector
  product. The pointwise `quad_point_contract` D stage is the **embarrassingly-parallel diagonal**
  of the pipeline ([`concepts/tensor-field-lift`](../concepts/tensor-field-lift.md)).

The whole-operator action `Mult` is `apply` followed by an optional `dof_multiplicity` post-scale
(shared-dof averaging; read single-rank per §Scope) — `Operator::Mult` at `palace/fem/libceed/operator.cpp:182-189`:
`y = 0; CeedAddMult(...); y *= dof_multiplicity`.

## Composition-level laws

These are stated **at the composition level** — the substrate ops' own algebra
(`element_restrict` gather/scatter linearity, `basis_apply` contraction laws, `quad_point_contract`
pointwise laws) is **NOT restated here** (USE+LINK; see those chapters). The combinator-level laws are
the facts that hold *of the composed `Gᵀ B_𝒟ᵀ D B_𝒟 G` pipeline*:

1. **Linearity of the apply.** `apply A` is a linear map `Tensor[(N: ...)] -> Tensor[(N: ...)]`:
   `apply A (α·x + β·z) = α·(apply A x) + β·(apply A z)`. Each of the five stages is linear
   (`element_restrict` is a pure index gather/scatter; `basis_apply` is a basis contraction;
   `quad_point_contract` is a per-point linear map fixing `geom`/`Q`), so their composition is linear.
   Witnessed by Palace exposing the operator through `ceed::Operator : mfem::Operator` whose
   `Mult`/`AddMult` are linear-operator applies (`palace/fem/libceed/operator.cpp:182-189`, `:194-200`) and by
   `CeedOperatorLinearAssembleAddDiagonal` (`palace/fem/libceed/operator.cpp:137-139` — diagonal of a *linear* operator).

2. **Self-adjointness / symmetry of the `Gᵀ … G` sandwich.** When `trial == test` (the restriction +
   basis are shared, `trial_restr == test_restr`, `trial_basis == test_basis`) and the pointwise
   `quad_point_contract` factor `D(Q, geom)` is symmetric (the mass `|J|·w` and grad-grad
   `J⁻ᵀJ⁻¹|J|·w` geometry factors are symmetric, and a real scalar coefficient `Q` is symmetric), the
   composed operator `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` is **self-adjoint**: `Aᵀ = Gᵀ B_𝒟ᵀ Dᵀ B_𝒟 G = A`. This is
   the structural reason the de-Rham mass / stiffness operators are SPD — the `Gᵀ(·)G` sandwich
   transports the symmetry of the pointwise diagonal to the global operator. (For complex Hermitian
   coefficients the analogous statement is `Aᴴ = A`.) A non-symmetric `D` (e.g. a non-self-adjoint
   coefficient) yields a non-symmetric `A` — the symmetry is a property of `D`, transported by the
   sandwich, not imposed by the combinator.

3. **Element-additivity of the `Gᵀ` scatter-add.** The global operator action is the **sum over
   elements** of the per-element local contributions: `apply A x = Σ_e Gᵀ_e (local-apply_e (G_e x))`,
   because `Gᵀ` is a scatter-**add** (it accumulates each element's local-dof contribution into the
   shared global dofs). Witnessed by `CeedAddMult` accumulating over the operator vector `op`
   (`palace/fem/libceed/operator.cpp:194-200` — `AddMult` adds into `y`; the per-element/per-batch contributions sum) and
   by the assembled form being `K = Σ_i A(space, term_i)` with `AddSubOperator` summation
   (`bilinearform.cpp:77`). This additivity is exactly the matrix-free analog of FE element-matrix
   assembly: no global matrix is materialized, but the *action* is the assembled sum.

(The bilinearity over `(trial, test)` and the per-term additivity over the weak form
`K = Σ_i A_i` are `fe_assemble`'s laws — see [`fe_assemble`](../L1/fe_assemble.md) — not restated here.)

## Cohort placement — a NEW L2 vocabulary kind

The combinator is a **constructive-kernel composition**: a named pipe of element-local contraction
verbs over the rank-structured [`element-local-tensor`](../concepts/element-local-tensor.md) family.
It is **distinct** from every existing L2 cohort, all of which compose flat-`Tensor[N]` BLAS-1 / solver
verbs:

- NOT a **fold cohort** member (`inner_product` / `linear_combination` / `gram`): those fold a single
  length / term axis to a scalar or `Tensor[N]`; this is a *fixed five-stage contraction pipeline*, not
  a variadic reduction.
- NOT a **named composition** (`orthogonalize` / `ksp_solve` / `eigsolve` / `deflate` /
  `incremental_least_squares`): those compose Krylov / solver verbs over flat vectors; this composes
  *element-local FE contraction verbs* over the element-local-tensor shapes — a different vocabulary.
- NOT an **elementwise / gate floor**: it is a genuine multi-stage composition, not a thin
  identity-in-form floor.

It seeds a new L2 sub-chapter grouping, **Constructive-kernel compositions** (the burn/GPU
backend-lowering contraction surface). It is the first member; future members (e.g. the term-fold of
`fe_assemble` at L2, sum-factorized basis application as a named sub-combinator) would join it.

## Sum-factorization — a transparent performance trick (one note)

On a tensor-product element, `basis_apply`'s `B_𝒟` contraction factors into a sum-factorized sequence
of 1-D contractions (the matrix-free efficiency win — `O(p^{d+1})` instead of `O(p^{2d})`). This is a
**transparent performance trick** (CLAUDE.md §Optimization tricks): it is algebraically equivalent to
the dense `B_𝒟` contraction. The L2 combinator's form is the **unfolded** contraction `B_𝒟`; the
factored 1-D-sweep evaluation order is a one-line note on the `basis_apply` stage, not a separate L2
form. (The factoring lives below L2 resolution; it is a `basis_apply` implementation detail — see that
chapter.)

## Matrix-free vs assembled-COO duality (one note)

The two representation variants the obstruction theme catalogues map cleanly onto this combinator:

- **Partial assembly (matrix-free) — the PRIMARY form.** Keep `A` as the un-materialized operator;
  evaluate the `apply` contraction fold on demand per matrix-vector product. This is the form this
  combinator names, and the form that is the GPU-tensor backend-lowering target.
- **Full assembly (assembled-COO) — the derived alternative.** Materialize `A` by applying the
  contraction pipeline to the identity columns and extracting COO triples
  (`CeedOperatorAssembleCOO`, `palace/fem/libceed/operator.cpp:483`), then convert to CSR. This is a **derived
  materialization of the same contraction**, not a different algorithm — the same combinator,
  evaluated on the identity basis and tabulated. Chosen at runtime by Palace's assembly-level config.

## Downward to L1 (identity-in-named-terms — in-line note, NOT a separate L2-L1 theme)

The L1 [`libceed-quadrature-kernel-impl`](../L1/libceed-quadrature-kernel-impl.md) **already states
this exact named chain** `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` and decomposes it into the same four substrate
ops. The L2→L1 rotation is therefore **identity-in-named-terms** — the L2 combinator and the L1
kernel-impl name the same composition of the same verbs over the same shape family; there is no
vocabulary shift between them (both are already in the element-local contraction vocabulary). Per the
vocabulary-shift redirect, a degenerate identity-in-named-terms lowering is a **smell**, NOT a mirrored
theme: this relationship is recorded **in-line here** (and via the `reference`-class
`lifts-kernel-impl` edge in the frontmatter), and **no `L2-L1/matrix-free-operator-apply-*` theme is
authored**. The genuine vocabulary shift in this cohort is the OTHER edge — from the flat-`Tensor[N]`
BLAS L1 to the rank-structured element-local-tensor family — which is captured by
[`concepts/element-local-tensor`](../concepts/element-local-tensor.md) and the substrate ops' own
L1>L0 mutation rotations, not by an L2>L1 theme on this combinator.

(The reason the L1 kernel-impl is the natural home of the concrete chain while this is the L2
*combinator* home: the L1 impl is "the constructive realization of ONE opaque kernel"; this L2 entry
is "the reusable named composition over the substrate vocabulary" — the composition-root the
`fe_assemble` fold's per-term leaf instantiates and that future element-local compositions reuse. The
distinction is one of *role* (realization vs reusable combinator), not of vocabulary — hence the
in-line note rather than a translation theme.)

## Justification kind

**structural** — the five-stage composition is read directly off the Palace `AssembleCeedOperator`
master assembler field-wiring (restriction → basis → QFunction → basis → restriction) + the
`Operator::Mult` apply; the composition-level laws (linearity, the `Gᵀ…G` symmetry sandwich,
element-additivity of the scatter-add) are syntactic-identity / structural facts on that positive
source, not reconstructed from negative anchors.

## Higher (L4) — firm

At L4 this combinator's action is the **apply** of a firm matrix-free linear-operator constructor
in the backend-lowering feature surface — the calculus form whose semantics match the burn/GPU tensor-
contraction backend directly (`project_l4_is_backend_lowering_target`):

- [`L4/mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md) (firm) — the **operator-constructor**
  whose action this L2 combinator IS. Signature
  `mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> Op[Tensor[(N: ...)] → Tensor[(N: ...)]]`;
  its `apply` runs the element-local tensor-contraction chain `Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` — i.e. this
  combinator — over the element-local axes.
- [`feature/matrix-free-operator.L4`](../feature/matrix-free-operator.L4.md) (firm) — the L4
  backend-lowering feature-surface column for matrix-free FE operators (the assemble-side
  composition-root).
- [`L4-L3/mk-matrix-free-operator-dissolution`](../L4-L3/mk-matrix-free-operator-dissolution.md) (firm)
  — the dissolution theme whose RHS composes this combinator (the flat-`Tensor[(N: ...)]` black-box
  apply → the five-stage element-local rank-tensor contraction sweep).

## Evidence

- `palace/fem/libceed/operator.cpp:182-189` — `Operator::Mult`: `y = 0.0; CeedAddMult(op, u, v, x, y);
  if (dof_multiplicity.Size() > 0) y *= dof_multiplicity;` — the whole-operator apply (the run-stratum
  `apply` + the `dof_multiplicity` post-scale).
- `palace/fem/libceed/operator.cpp:194-200` — `Operator::AddMult` + the `CeedAddMult` accumulation
  (`AddMult` adds into `y`) — the element-additivity / scatter-add law witness.
- `palace/fem/libceed/operator.cpp:137-139` — `CeedOperatorLinearAssembleAddDiagonal` — the operator
  is a *linear* operator (linearity-law witness).
- `palace/fem/libceed/operator.cpp:483` — `CeedOperatorAssembleCOO` — the derived assembled-COO
  materialization (the matrix-free-vs-assembled duality).
- `palace/fem/libceed/integrator.cpp:422-445` — `AssembleCeedOperator` master assembler signature
  (`trial_restr`/`test_restr`/`trial_basis`/`test_basis`/`geom_data`/`geom_data_restr`) — the field
  wiring of the `Gᵀ Bᵀ D B G` pipeline (the `mk-operator` build stratum).
- `palace/fem/libceed/integrator.cpp:451-512` — apply-QFunction / operator-field wiring: `geom_data`
  input (`:458`), `q_w` `CEED_EVAL_WEIGHT` (`:462`) — the `B G` (input) and `Bᵀ Gᵀ` (output) field
  chains around the pointwise `D`.
- `palace/fem/libceed/integrator.cpp:340-419` — the build-QFunction `f_build_geom_factor_*` — the
  `geom_factor_build` setup-stratum carrier.
- `palace/fem/bilinearform.cpp:77` — `AddSubOperator` — the per-term fold summation
  `K = Σ_i A(space, term_i)` (the `fe_assemble` consumer; element/term additivity).
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the L1 kernel-impl this combinator names at L2
  (the identity-in-named-terms downward note; `reference`-class `lifts-kernel-impl` edge).
- `book/src/concepts/element-local-tensor.md` — the firm shape family the contraction is typed over.
- `book/src/L1/fe_assemble.md` — the firm fold whose per-term leaf `A(space, term)` is this
  combinator's product.

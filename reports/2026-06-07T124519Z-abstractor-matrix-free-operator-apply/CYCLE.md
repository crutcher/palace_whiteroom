---
agent: abstractor
invoked_at: 2026-06-07T130000Z
scope: L2 combinator sketch — matrix-free FE operator-application contraction chain (ASK-2 "A" deepen-the-layer, cycle-125 D2)
status: integrated
integrated_at: 2026-06-07T124519Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-125 D2 (batch-40 MIDDLE). Applied clean by integrator-per-report (staging row 2, after D1 per the apply-ordering); no gate hits. L2 firm 22→23: new firm L2 constructive-kernel combinator matrix-free-operator-apply (the matrix-free / burn-GPU backend-lowering surface, a 2nd faithful depends-on(composes) substrate consumer) + new L2 by-kind group Constructive-kernel compositions + group-intro, both SUMMARY-registered. NO L2-L1 theme (identity-in-named-terms smell → in-line Downward-to-L1 + reference-class lifts-kernel-impl edge). 4 OQs promoted. rank_violations 0. Build EXIT 0, no finalize build-repair."
inputs:
  - book/src/L1/libceed-quadrature-kernel-impl.md (the L1 kernel-impl whose A = Gᵀ B_𝒟ᵀ D B_𝒟 G chain this lifts)
  - book/src/concepts/element-local-tensor.md (firm shape family the contraction is typed over)
  - book/src/L1/{element_restrict,basis_apply,quad_point_contract,geom_factor_build}.md (the four substrate ops; D1 firms element_restrict + geom_factor_build this cycle)
  - palace/fem/libceed/operator.cpp:182-189 (Operator::Mult — y=0; CeedAddMult apply), :194-200 (AddMult accumulate), :483 (CeedOperatorAssembleCOO derived materialization)
  - palace/fem/libceed/integrator.cpp:422-445 (AssembleCeedOperator master assembler wiring), :340-419 (build-QFunction geom factor), :451-512 (apply-QFunction B G / Bᵀ Gᵀ field chains)
  - book/src/L2/index.md (L2 cohort structure + dep-map + SUMMARY grouping)
---

# CYCLE: L2 combinator sketch — matrix-free FE operator-application contraction chain

## Summary

The firm L1 `libceed-quadrature-kernel-impl` realizes the per-term FE operator-application
leaf `A(space, (Q, 𝒟)) = Gᵀ ∘ B_𝒟ᵀ ∘ D(Q, geom) ∘ B_𝒟 ∘ G` as a five-stage tensor-contraction
pipeline over the firm `concepts/element-local-tensor` shape family (`[(N: ...)]` → `[E, L]` →
`[E, P, C]` → … → `[(N: ...)]`). That contraction-chain shape **is** the burn/GPU matrix-free
backend-lowering target. This dispatch lifts it into a first-class **L2 combinator**,
`matrix-free-operator-apply` (canonical slug `book/src/L2/matrix-free-operator-apply.md`), that
**composes the now-firm substrate ops by name** — `element_restrict` (G/Gᵀ), `basis_apply`
(B_𝒟/B_𝒟ᵀ), `quad_point_contract` (D), `geom_factor_build` (the geometry-factor carrier) — as a
named **contraction-chain fold** over the element-local axes, and states the **operator-application
laws at the composition level** (linearity of the apply; the `Gᵀ…G` self-adjoint/symmetry of the
composed bilinear operator; element-additivity of the `Gᵀ` scatter-add). It is a NEW L2 vocabulary
kind — a **constructive-kernel composition** — distinct from the existing fold-cohort / named-
composition / gate-floor cohorts (those compose BLAS-1 / solver verbs over the flat `Tensor[N]`
vocabulary; this composes element-local contraction verbs over the rank-structured element-local-
tensor family). Sum-factorization is classified a **transparent performance trick** (the L2 form is
the unfolded contraction; the factored 1-D-sweep evaluation order is a one-line note). The matrix-
free apply is the **primary** form; the assembled-COO materialization (`CeedOperatorAssembleCOO`,
`palace/fem/libceed/operator.cpp:483`) is the derived alternative (a one-note duality, not a separate algorithm). The
L2→L1 rotation is **identity-in-named-terms** (the L1 kernel-impl already states the same named chain)
— a degenerate-lowering **smell** per the redirect — so it is resolved as an **in-line "Downward to
L1" note in the chapter, NOT a separate `L2-L1/` theme** (the planner caveat anticipated this).

**Landed maturity: `firm`** — the composition is positively sourced off the `AssembleCeedOperator`
master assembler + `Operator::Mult` apply, its laws are syntactic-identity composition facts on that
positive source (no test gates a composition identity — the firm-on-positive-structure escape), and
its four `depends-on (composes)` substrate deps are all firm after D1 (the §(h) well-foundedness cap
`rank(u) ≤ min(deps)` permits firm). The combinator is sequenced wave-2 after D1 so the per-report
integrator wires its edges onto the firm-on-disk substrate.

## Proposed changes

```new:book/src/L2/matrix-free-operator-apply.md
---
layer: L2
operator: matrix-free-operator-apply
# Graded-stack scheme. This is a `firm` (rank 3) L2 combinator: the named contraction-chain
# composition of the four firm element-local substrate ops that realizes FE matrix-free operator
# application A = Gᵀ B_𝒟ᵀ D B_𝒟 G over the `concepts/element-local-tensor` shape family. It is a
# constructive-kernel COMPOSITION (a new L2 cohort kind), distinct from the BLAS-1 fold cohorts.
# Well-foundedness: its four `depends-on (composes)` substrate deps are all firm (basis_apply +
# quad_point_contract firm c124 D3; element_restrict + geom_factor_build firm c125 D1), so
# `rank(combinator) <= min(deps) = firm` permits firm; the composition is positively sourced
# (AssembleCeedOperator master + Operator::Mult apply) and its laws are syntactic-identity
# composition facts (firm-on-positive-structure escape — no test gates a composition identity).
# Pulled-by: `fe_assemble` (firm spine consumer) reaches the feature root via the fe_assemble
# fold's 7 feature-column inbound edges — the L1 kernel-impl this lifts is reachable, and this L2
# combinator inherits that reachability through its `reference`-class lift edge to the kernel-impl.
rank: firm
edges:
  depends-on:
    # The four element-local substrate ops this combinator COMPOSES BY NAME (all firm after c125 D1).
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
    - target: concepts/element-local-tensor   # the rank-structured shape family the whole chain is typed over (firm, c124 D5)
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

## Status

`firm` (rank 3) — **constructive-kernel composition** (a new L2 cohort kind; see §"Cohort placement").
The combinator **composes four firm substrate ops by name** and its composition-level laws are
syntactic-identity facts on the positively-read `AssembleCeedOperator` master assembler
(`palace/fem/libceed/integrator.cpp:422-445`) + the `Operator::Mult` apply (`palace/fem/libceed/operator.cpp:182-189`) — no test gates a
composition identity, so the **firm-on-positive-structure escape** applies. Well-foundedness: the four
`depends-on (composes)` substrate deps are all firm — `basis_apply` + `quad_point_contract` (c124 D3),
`element_restrict` + `geom_factor_build` (c125 D1) — so `rank ≤ min(deps) = firm` permits firm. The
shape family it is typed over, [`element-local-tensor`](../concepts/element-local-tensor.md), is firm
(c124 D5). All L0 citations self-verified against on-disk source this dispatch via `citecheck --anchor`.

## L2 form (the named contraction-chain combinator)

Writing `term = (Q, 𝒟)` (a [`weak_form_term`](../L1/weak_form_term.md): coefficient `Q`,
differential-operator `𝒟 ∈ {Identity, Gradient, Curl, Divergence}`), the combinator is the
**pipe of the four substrate verbs** over the element-local-tensor family:

    matrix-free-operator-apply
      :: ElemRestriction -> Basis -> GeomData -> Coefficient
      -> LinearOperator[(N: ...)]
    -- one term's element-local→global linear operator, as a contraction-chain fold

    apply (A = mk-operator restr basis geom Q) :: Tensor[(N: ...)] -> Tensor[(N: ...)]
    apply A x =
        x   |> element_restrict restr            -- G   :: [(N: ...)] -> [E, L]
            |> basis_apply (mode-of 𝒟) basis     -- B_𝒟 :: [E, L]    -> [E, P, C]
            |> quad_point_contract geom Q         -- D   :: [E, P, C] -> [E, P, C]  (pointwise, against [E, P, G])
            |> basis_apply (transpose (mode-of 𝒟)) basis   -- B_𝒟ᵀ :: [E, P, C] -> [E, L]
            |> element_restrict_transpose restr   -- Gᵀ  :: [E, L]    -> [(N: ...)]  (scatter-ADD)

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
  `incremental-least-squares`): those compose Krylov / solver verbs over flat vectors; this composes
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

## Speculative higher (L4) placeholder (rough-in, for a later harvester)

At L4 this combinator would surface as a **matrix-free linear-operator constructor** in the
backend-lowering feature surface — the calculus form whose semantics match the burn/GPU tensor-
contraction backend directly (`project_l4_is_backend_lowering_target`). Rough sketch (NOT authored
this cycle — placeholder for a later harvester / L4-completeness capstone):

    mk_matrix_free_operator
      :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])

with the apply lowering to the L4 tensor-contraction graph `Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` over the
element-local axes. This is the L4 backend-lowering entry point for matrix-free assembly; it is the
remaining ASK-2 "A" depth (matrix-free assembly fused with `fe_assemble`'s term-fold at L4) flagged as
a c126 / batch-41 candidate. Left as a §Open-questions placeholder, not a chapter, this cycle.

## Verified-against

- `palace/fem/libceed/operator.cpp:182-189` — `Operator::Mult`: `y = 0.0; CeedAddMult(op, u, v, x, y);
  if (dof_multiplicity.Size() > 0) y *= dof_multiplicity;` — the whole-operator apply (the run-stratum
  `apply` + the `dof_multiplicity` post-scale). Self-verified via `citecheck --anchor 'Operator::Mult'`.
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

The chapter carries a fenced `verified_against:` YAML block (rendered on-disk as a ` ```yaml `
fence; reproduced here 4-space-indented so the proposed-changes fence is not mis-toggled — the
integrator emits it as a ` ```yaml ` block in the applied file):

    verified_against:
      - citation: reference/palace/palace/fem/libceed/operator.cpp:182-189
        verdict: supports
        audited_at: 2026-06-07T130000Z
        note: Operator::Mult (:182) — y=0.0; CeedAddMult(op,u,v,x,y); y*=dof_multiplicity — the whole-operator apply. citecheck --anchor 'Operator::Mult' [ok], anchor at :182 within range.
      - citation: reference/palace/palace/fem/libceed/operator.cpp:194-200
        verdict: supports
        audited_at: 2026-06-07T130000Z
        note: Operator::AddMult (:194) + the CeedAddMult accumulation — element-additivity / scatter-add witness. citecheck --anchor 'AddMult' [ok], anchors at :194,:199 within range.
      - citation: reference/palace/palace/fem/libceed/operator.cpp:483
        verdict: supports
        audited_at: 2026-06-07T130000Z
        note: CeedOperatorAssembleCOO (:483) — the derived assembled-COO materialization (matrix-free-vs-assembled duality). citecheck --anchor 'CeedOperatorAssembleCOO' [ok].
      - citation: reference/palace/palace/fem/libceed/integrator.cpp:422-445
        verdict: supports
        audited_at: 2026-06-07T130000Z
        note: AssembleCeedOperator master assembler (:423 signature) — trial_restr/test_restr/trial_basis/test_basis/geom_data/geom_data_restr field wiring of the Gᵀ Bᵀ D B G pipeline (mk-operator build stratum). citecheck --anchor 'AssembleCeedOperator' [ok], anchor at :423 within range.
      - citation: reference/palace/palace/fem/libceed/integrator.cpp:340-419
        verdict: supports
        audited_at: 2026-06-07T130000Z
        note: build-QFunction f_build_geom_factor_* — the geom_factor_build setup-stratum carrier. citecheck --anchor 'f_build_geom_factor' [ok].
      - citation: reference/palace/palace/fem/bilinearform.cpp:77
        verdict: supports
        audited_at: 2026-06-07T130000Z
        note: AddSubOperator (:77) — per-term fold summation K = Σ_i A(space, term_i) (the fe_assemble consumer; element/term additivity). citecheck --anchor 'AddSubOperator' [ok].
```

```edit:book/src/L2/index.md
[1] Append a `reference` edge to the navigational-container frontmatter for the new sub-chapter group intro (the constructive-kernel-compositions group). In the `edges.reference:` list (currently ending `- L2/elementwise-gate-floors-intro`), append:
    - L2/constructive-kernel-compositions-intro

[2] In the `## Vocabulary cohort` section, under the `**Firm at L2**` grouping, append a new bullet block AFTER the elementwise/gate-floor bullets (after the `divfree-projector` firm bullet) and BEFORE the `**Partly-constructive at L2**` heading:

*Constructive-kernel compositions (cycle-125; a NEW L2 cohort kind — named contraction-chain compositions of the element-local substrate over the rank-structured `concepts/element-local-tensor` family, the burn/GPU matrix-free backend-lowering surface; distinct from the flat-`Tensor[N]` BLAS-1 fold / named-composition / gate cohorts):*

- `matrix-free-operator-apply` — the named contraction-chain combinator for matrix-free FE operator application `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`, composing the four firm element-local substrate ops by name (`element_restrict` = G/Gᵀ, `basis_apply` = B_𝒟/B_𝒟ᵀ, `quad_point_contract` = D, `geom_factor_build` = the geom carrier) over the `concepts/element-local-tensor` shapes. Composition-level laws: linearity of the apply; the `Gᵀ…G` self-adjoint/symmetry sandwich (transports the pointwise `D` symmetry to the global operator → de-Rham SPD); element-additivity of the `Gᵀ` scatter-add (the matrix-free analog of FE element-matrix assembly). The L1 [`libceed-quadrature-kernel-impl`](../L1/libceed-quadrature-kernel-impl.md) is its concrete realization (identity-in-named-terms downward — in-line note, NO L2-L1 theme); the `fe_assemble` fold sums it per-term. Sum-factorization is a transparent performance trick (one note); the assembled-COO form is the derived materialization (one note). Firm cycle-125 D2 (firm-on-positive-structure — the composition + laws read off `AssembleCeedOperator` + `Operator::Mult`; the four `composes` deps firm after c125 D1).

[3] Add a new `### Constructive-kernel compositions` dep-map sub-section AFTER the `### Elementwise & gate floors` table (the last dep-map sub-section, ending with the `reciprocal` row) and BEFORE `## Working Notes`:

### Constructive-kernel compositions

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`matrix-free-operator-apply`](./matrix-free-operator-apply.md) | `mk-operator :: ElemRestriction -> Basis -> GeomData -> Coefficient -> LinearOperator[(N: ...)]`; `apply A :: Tensor[(N: ...)] -> Tensor[(N: ...)]` (≡ the named chain `A = Gᵀ ∘ B_𝒟ᵀ ∘ D(Q, geom) ∘ B_𝒟 ∘ G`) | **Constructive-kernel composition (NEW cohort) — the named contraction-chain fold over the element-local-tensor family.** `depends-on (composes)`: [`element_restrict`](../L1/element_restrict.md) (G/Gᵀ), [`basis_apply`](../L1/basis_apply.md) (B_𝒟/B_𝒟ᵀ), [`quad_point_contract`](../L1/quad_point_contract.md) (D), [`geom_factor_build`](../L1/geom_factor_build.md) (geom carrier) — all firm after c125 D1. Typed over [`element-local-tensor`](../concepts/element-local-tensor.md) (firm). Concepts: [`tensor-field-lift`](../concepts/tensor-field-lift.md) (the pointwise D stage), [`build-time-vs-run-time-stratification`](../concepts/build-time-vs-run-time-stratification.md). Lifts the L1 [`libceed-quadrature-kernel-impl`](../L1/libceed-quadrature-kernel-impl.md) (identity-in-named-terms; `reference`-class `lifts-kernel-impl`, NO L2-L1 theme). Consumer: [`fe_assemble`](../L1/fe_assemble.md) (the per-term leaf A this is). Composition-level laws: linearity / `Gᵀ…G` symmetry sandwich / element-additive scatter-add. | `firm` (harvested cycle-125 D2; firm-on-positive-structure — composition + laws off `AssembleCeedOperator` `palace/fem/libceed/integrator.cpp:422-445` + `Operator::Mult` `palace/fem/libceed/operator.cpp:182-189`; the four `composes` deps firm after c125 D1, so `rank ≤ min(deps) = firm` permits firm) |

[4] In the `## Operator dep-map` intro line, update the count: the line currently reads "22 firm + 1 `partly-constructive` (`deflate`)." — change to "23 firm + 1 `partly-constructive` (`deflate`)." (the new `matrix-free-operator-apply` row raises firm 22 → 23).
```

```new:book/src/L2/constructive-kernel-compositions-intro.md
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
```

```edit:book/src/SUMMARY.md
[Under the `# L2 — Algebraic Decompositions` Part, add a new sub-chapter group AFTER the `Elementwise & gate floors` group (after the `- [reciprocal](./L2/reciprocal.md)` line at SUMMARY.md:165) and BEFORE the `# L2 > L1 — Lowering` Part heading (SUMMARY.md:167):]
- [Constructive-kernel compositions](./L2/constructive-kernel-compositions-intro.md)
  - [matrix-free-operator-apply](./L2/matrix-free-operator-apply.md)
```

## Speculative operators proposed

- **`matrix-free-operator-apply`** (the L2 combinator authored as `firm` this cycle — NOT a rough-in
  placeholder; it composes firm substrate). Signature:
  `mk-operator :: ElemRestriction -> Basis -> GeomData -> Coefficient -> LinearOperator[(N: ...)]`;
  `apply A :: Tensor[(N: ...)] -> Tensor[(N: ...)]`. Motivation: the named L2 home of the matrix-free
  FE operator-application contraction chain — the composition-root the `fe_assemble` per-term leaf
  instantiates and the burn/GPU backend-lowering target. Authored firm (firm-on-positive-structure,
  firm `composes` deps). No harvester promotion needed (it lands firm); a future harvester/lifter may
  refine its laws or add cohort members.

- **`mk_matrix_free_operator`** (speculative L4 placeholder, rough-in — NOT authored this cycle).
  Signature sketch: `FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])`. The
  L4 backend-lowering constructor whose apply lowers to the tensor-contraction graph
  `Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`. Left as a §Open-questions placeholder for the c126 / batch-41 L4
  matrix-free depth, not a chapter (no inbound blocking consumer reaches it yet — it would be a
  `roadmap_goal` once the L4 backend-lowering feature surface pulls it).

## Supporting evidence

- L1 `libceed-quadrature-kernel-impl.md:102` already states `A(space, (Q, 𝒟)) = Gᵀ ∘ B_𝒟ᵀ ∘ D(Q, geom)
  ∘ B_𝒟 ∘ G` and decomposes into the four substrate ops (`:108-141`) — the source for the L2 named
  composition. The four substrate ops are firm (basis_apply + quad_point_contract c124 D3;
  element_restrict + geom_factor_build c125 D1).
- `concepts/element-local-tensor.md` (firm, c124 D5) — the `[E, L]` / `[E, P, C]` / `[E, P, G]` shape
  family the chain is typed over; `:80-86` confirms the flat `[(N: ...)]` is NOT in this family
  (element_restrict's G/Gᵀ is the boundary).
- Palace L0 (all citecheck-verified this dispatch): `Operator::Mult` `palace/fem/libceed/operator.cpp:182-189`,
  `AddMult` `:194-200`, `CeedOperatorAssembleCOO` `:483`, `AssembleCeedOperator` `palace/fem/libceed/integrator.cpp:422-445`,
  build-QFunction `:340-419`, apply-QFunction field chains `:451-512`, `AddSubOperator`
  `bilinearform.cpp:77`.

## Open questions / caveats

- **L2→L1 lowering resolved as in-line note, NO theme (per planner caveat).** The L2 combinator and
  the L1 kernel-impl name the same chain over the same vocabulary — identity-in-named-terms, a
  degenerate-lowering smell. Recorded in-line in the chapter §"Downward to L1" + the `reference`-class
  `lifts-kernel-impl` frontmatter edge. No `L2-L1/matrix-free-operator-apply-*` theme authored. The
  genuine vocabulary shift in this cohort is the flat-`Tensor[N]` → element-local-tensor edge
  (`concepts/element-local-tensor` + the substrate ops' L1>L0 rotations), not an L2>L1 hop on this
  combinator. Flagged for the lowering-verifier / cross-cutter: confirm no L2>L1 theme is expected
  here (the absence is deliberate, not a coverage gap).

- **Cohort role-vs-vocabulary distinction.** The L1 kernel-impl ("realization of one opaque kernel")
  and this L2 combinator ("reusable named composition") differ in *role*, not *vocabulary*. This is the
  honest reason the relationship is identity-in-named-terms — both are in the element-local contraction
  vocabulary. If a future reviewer judges the role-distinction insufficient to warrant TWO chapters
  (L1 impl + L2 combinator) over the same chain, the resolution would be to fold the L2 combinator's
  composition-level laws INTO the L1 kernel-impl and drop the L2 chapter — but the planner explicitly
  scoped this as a deepen-the-layer L2 lift (the L2 combinator IS the reusable composition-root the
  fe_assemble leaf and future element-local compositions instantiate), so the two-chapter split is
  intended. Surfaced for the batch-40 meta in case the role-vs-vocabulary line wants codifying.

- **Speculative L4 placeholder (`mk_matrix_free_operator`) not landed as a roadmap_goal this cycle.**
  Per the graded-stack directive, a speculative L4 operator should land as a `roadmap_goal` chapter
  with an inbound blocking consumer reaching a feature root — but the L4 backend-lowering feature
  surface that would pull it is itself a c126 / batch-41 candidate (the ASK-2 "A" L4 depth + the "B"
  5-driver L4-completeness capstone). Authoring the roadmap_goal now would strand it (no pull-chain to
  a root yet). Left as a §placeholder; the c126 / batch-41 L4 matrix-free dispatch should land it as a
  roadmap_goal once the L4 backend-lowering surface provides the pull.

- **AMR interaction (forward note).** `geom_factor_build` (and thus the build-stratum of this
  combinator) is rebuilt on AMR refinement (the mesh-change rebuild noted in
  `concepts/element-local-tensor` §Build-vs-run). When the AMR consumer (DIRECTIVE-2 grounded
  consumer-(2)) lands, it is a faithful consumer of this combinator's rebuild boundary — a future
  `depends-on` / `reference` edge, not authored this cycle.

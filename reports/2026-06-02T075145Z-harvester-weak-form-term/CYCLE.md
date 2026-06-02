---
agent: harvester
invoked_at: 2026-06-02T075145Z
scope: L1 operator: weak_form_term
status: pending
integrated_at: 2026-06-02T082437Z
integration_commit: 018eea5
integration_notes: "Applied cycle-061 (D1; batch-19 position 1/3). NEW book/src/L1/weak_form_term.md FIRM L1 — the (coefficient, differential-operator) pair naming one weak-form contribution a(u,v)=(Q·Du,Dv); the element type of fe_assemble's opaque term list; the genuinely-new FE differential-operator vocabulary, pull-driven by the magnetostatic curl-curl term (laplaceoperator.cpp:184-194 Gradient/DiffusionIntegrator/epsilon_func + curlcurloperator.cpp:170-181 Curl/CurlCurlIntegrator/muinv_func, repairer-corrected muinv_func pin :178-179 integrator-site :181 preserved). 2 opaque-WeakFormTerm rough-in notes in fe_assemble.md re-anchored to live ./weak_form_term.md links (reference-upgrades only — fold structure + laws unchanged, replace-and-propagate). L1/index.md dual-registration (dep-map TABLE row + cohort bullet, harvester-owned) + SUMMARY.md. citecheck --scan 29 ok/0 failing. L1 firm 29->30; FE-assembly sub-spine 3->4 firm L1 operators. No concept page (single consumer, below ≥2 bar; OQ weak-form-term-concept-page-reconsideration-on-second-consumer promoted). KNOWN-LAG: L1/index §Vocabulary-cohort header PROSE count lags (TABLE tally correct), OQ l1-index-fe-assembly-sub-spine-count-prose-refresh-3-to-4 for a layer-intro-author touch. Build clean, exit 0; both new pages render; no dead link, no stub. Two-phase SHA patch to follow."
inputs:
  - cycle-061 dispatch D1 (LEAD)
  - pulled witnesses: palace/models/laplaceoperator.cpp:184-194 (DiffusionIntegrator/epsilon_func), palace/models/curlcurloperator.cpp:170-181 (CurlCurlIntegrator/muinv_func)
  - Palace integrator wrappers: palace/fem/integrator.hpp:39-130
  - re-anchor target: book/src/L1/fe_assemble.md:69-71,158-166 (opaque WeakFormTerm rough-in input)
  - vocabulary-shift redirect (METHODOLOGY-REDIRECT.md; CLAUDE.md §Methodology invariants)
---

# CYCLE: Formalize weak_form_term at L1

## Summary

`weak_form_term` is the **element type of `fe_assemble`'s term list** — a `(coefficient, differential-operator)`
pair that names one weak-form contribution `a(u, v) = (Q · 𝒟u, 𝒟v)` to a global FE operator, where `𝒟` is the
**differential operator** (the variant axis) and `Q` is the **material-property coefficient**. `fe_assemble`
(firm cycle-054) currently folds over this type **opaquely**, naming it as a deferred OPAQUE rough-in input.
The magnetostatic pull surfaced the pipeline NEED: `CurlCurlOperator::GetStiffnessMatrix`
(`palace/models/curlcurloperator.cpp:170-181`) builds its K-matrix with the **same `BilinearForm`-fold** the
firm electrostatic `fe_assemble` witness uses (`palace/models/laplaceoperator.cpp:184-194`), differing ONLY in
the term integrator — `CurlCurlIntegrator(muinv_func)` (magnetostatic) vs `DiffusionIntegrator(epsilon_func)`
(electrostatic). So the fold quantifies over a `(coefficient, differential-operator)` term FAMILY, and
`weak_form_term` is exactly that abstraction. This entry firms the term with the **differential-operator as the
variant axis**, grounded by the two pulled witnesses (diffusion + curl-curl) and naming **mass** + **div-div** as
**pending-pull SIBLING variants** (named axis points, NOT speculatively authored). The work is a
**replace-and-propagate**: `fe_assemble`'s opaque-input note is re-anchored to a LIVE link to this firm term
abstraction. No concept page authored (single downstream consumer — below the ≥2 bar).

## Proposed changes

```new:book/src/L1/weak_form_term.md
---
layer: L1
operator: weak_form_term
firmness: firm
lowers_to:
  - L1-L0/fe-assemble-libceed-boundary-obstruction
lifts_from: []
depends_on: []
variant_axes:
  - differential-operator
  - coefficient-rank
  - term-position
---

# weak_form_term

The **element type of `fe_assemble`'s term list**: an immutable `(coefficient, differential-operator)` pair
naming one weak-form contribution `a(u, v) = (Q · 𝒟u, 𝒟v)` to a global finite-element operator. `𝒟` is the
**differential operator** applied to the trial/test functions (the variant axis — gradient, identity, curl, or
divergence); `Q` is the **material-property coefficient** weighting the bilinear pairing. The genuinely-new FE
vocabulary the FE-assembly sub-spine introduces, and the value [`fe_assemble`](./fe_assemble.md) folds over.

## Slug-context (load-bearing — what this is and is NOT)

`weak_form_term` is the **per-term value** the [`fe_assemble`](./fe_assemble.md) fold quantifies over. It is NOT
the assembled operator (that is `fe_assemble`'s result `K = Σ_i A(term_i)`), and it is NOT the per-term assembly
**map** `A(space, ·)` (the element-local quadrature kernel + restriction, libCEED-owned — see *Dependencies*).
The term is a **specification of WHICH contribution to assemble**, not the assembly itself: `fe_assemble`'s fold
reads the term's `(Q, 𝒟)` identity to pick the per-term kernel, then `A` executes it. A `weak_form_term` carries
the *identity* of a contribution; `A` carries its *realization*.

## Context

`weak_form_term` lifts the **`(integrator-type, coefficient-args)` pair** that Palace's `BilinearForm` build-up
protocol pushes onto its integrator list. The L0 form is a templated append
`k.AddDomainIntegrator<T>(Q)` (`palace/fem/bilinearform.hpp:53-57` — `domain_integs.push_back(make_unique<T>(Q))`):
the **template parameter `T`** is the differential-operator type (the concrete `BilinearFormIntegrator` subclass),
and the **runtime argument `Q`** is the `MaterialPropertyCoefficient` weighting it. The two pulled solver-K
witnesses differ in EXACTLY these two slots and nothing else:

- **Electrostatic** (`palace/models/laplaceoperator.cpp:191-192`): `MaterialPropertyCoefficient epsilon_func(...)`
  then `k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func)` — the term `(ε, ∇)`, realizing
  `a(u, v) = (ε ∇u, ∇v)`.
- **Magnetostatic** (`palace/models/curlcurloperator.cpp:178-181`): `MaterialPropertyCoefficient muinv_func(...)`
  then `k.AddDomainIntegrator<CurlCurlIntegrator>(muinv_func)` — the term `(μ⁻¹, ∇×)`, realizing
  `a(u, v) = (μ⁻¹ ∇×u, ∇×v)`.

The differential operator `𝒟` is carried by the integrator's **type identity**; the Palace wrapper class
declarations name the realized bilinear form in their own doc comments — `DiffusionIntegrator`:
`a(u,v) = (Q grad u, grad v)` (`palace/fem/integrator.hpp:100-101`); `CurlCurlIntegrator`:
`a(u,v) = (Q curl u, curl v)` (`palace/fem/integrator.hpp:111-112`). The coefficient `Q` is held on the shared
base class as `const MaterialPropertyCoefficient *Q` (`palace/fem/integrator.hpp:39-42`), uniform across every
differential-operator variant — which is what makes `(coefficient, differential-operator)` the right
factorization: the coefficient slot is variant-invariant, the differential-operator slot is the variant axis.

## Signature

```text
weak_form_term :: { coefficient: MaterialCoefficient, diff_op: DifferentialOperator } -> WeakFormTerm

data DifferentialOperator = Gradient | Identity | Curl | Divergence
```

Shape contract (bunsen-style, named axes):

- `coefficient` — `MaterialCoefficient` — the material-property weight `Q` of the bilinear pairing
  (`MaterialPropertyCoefficient` at L0, `palace/fem/integrator.hpp:42`). An attribute-to-property map evaluated
  per quadrature point; scalar or matrix-valued depending on the field rank (the *coefficient-rank* sub-axis).
  Read-only.
- `diff_op` — `DifferentialOperator` — the differential operator `𝒟` applied to both trial and test functions in
  the pairing `(Q · 𝒟u, 𝒟v)`. **This is the variant axis** (see *Variant axes*). Carried at L0 by the
  `BilinearFormIntegrator`-subclass *type identity* (the `AddDomainIntegrator<T>` template parameter,
  `palace/fem/bilinearform.hpp:53-57`).
- result — `WeakFormTerm` — an opaque immutable term value: one entry of the list
  [`fe_assemble`](./fe_assemble.md) folds over.

The term is **inert data at L1**: it carries the *identity* of a weak-form contribution (which coefficient,
which differential operator) and nothing executable. The element-local→global *realization* of the term is the
opaque per-term assembly map `A(space, ·)` that `fe_assemble` applies (libCEED-owned — see *Dependencies*); the
term is `A`'s argument, not `A` itself.

## Semantics

A `weak_form_term` denotes the **continuum bilinear form** `a(u, v) = (Q · 𝒟u, 𝒟v)_Ω` — the `Q`-weighted
`L²(Ω)` inner product of the differential operator `𝒟` applied to trial function `u` and test function `v`.
Discretized over a finite-element space, this term contributes the global operator block

```text
A(space, term) · v  =  the element-assembled, restriction-summed realization of  (Q · 𝒟u, 𝒟v)  over space
```

— one additive summand of [`fe_assemble`](./fe_assemble.md)'s fold `K = Σ_i A(space, term_i)`. The term itself
specifies the integrand `(Q · 𝒟u, 𝒟v)`; the assembly map `A` performs the quadrature contraction and dof
restriction. The four witnessed/named differential operators and the bilinear forms they specify:

```text
Gradient   :  a(u, v) = (Q ∇u,  ∇v )    H1 scalar field        DiffusionIntegrator   (palace/fem/integrator.hpp:100-101)
Identity   :  a(u, v) = (Q u,   v  )    mass/L² pairing         Mass/VectorFEMass     (palace/fem/integrator.hpp:68-69,79-80)
Curl       :  a(u, v) = (Q ∇×u, ∇×v)    H(curl) Nedelec field   CurlCurlIntegrator    (palace/fem/integrator.hpp:111-112)
Divergence :  a(u, v) = (Q ∇·u, ∇·v)    H(div) Raviart-Thomas   DivDivIntegrator      (palace/fem/integrator.hpp:122-123)
```

The differential operator selects the **field type the term is well-formed over** (the trial/test space's
de-Rham position): Gradient over H1, Curl over H(curl)/Nedelec, Divergence over H(div)/Raviart-Thomas, Identity
over any (the comment on `MassIntegrator` notes it serves H1 and vector-`(H1)ᵈ` spaces, `palace/fem/integrator.hpp:68`).
This is a **specification, not a computation**: at L1 the term is pure inert data; its realization (the
quadrature kernel) is the opaque libCEED-owned map `A`. The term is **mutation-free**: the L0 `AddDomainIntegrator`
`push_back` onto the owned `domain_integs` container is an L0 build-up concern absorbed by the
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) lowering, not by
the term value.

## Algebraic laws

`weak_form_term` is an **inert product (a pair constructor)**; the laws below are exactly the laws of that pair
plus the bilinearity its assembled realization inherits. Absences are deliberate.

1. **Coefficient-linearity (scaling) of the assembled term**: for scalar `c`,
   `A(space, weak_form_term(c · Q, 𝒟)) = c · A(space, weak_form_term(Q, 𝒟))`. The coefficient enters the
   bilinear pairing linearly — scaling `Q` scales the assembled block. (Continuum-level: `(cQ · 𝒟u, 𝒟v) = c (Q · 𝒟u, 𝒟v)`.
   The variant-uniform `Q`-on-base-class structure, `palace/fem/integrator.hpp:39-42`, is what carries this
   uniformly across every differential-operator variant.)

2. **Coefficient-additivity over a fixed differential operator**: for two coefficients over the same `𝒟`,
   `A(space, weak_form_term(Q₁ + Q₂, 𝒟)) = A(space, weak_form_term(Q₁, 𝒟)) + A(space, weak_form_term(Q₂, 𝒟))`.
   Splitting a material coefficient into additive pieces splits the assembled term additively (continuum:
   `((Q₁+Q₂)·𝒟u, 𝒟v) = (Q₁·𝒟u, 𝒟v) + (Q₂·𝒟u, 𝒟v)`). This composes with `fe_assemble`'s concatenation
   homomorphism: a single split-coefficient term equals two same-`𝒟` terms in the list.

3. **Differential-operator determines the well-formed space (variant-discreteness)**: the `diff_op` axis is a
   **discrete enumeration**, not a continuum — `Gradient | Identity | Curl | Divergence`. There is no algebraic
   combination of differential operators within one term; a term carries exactly one `𝒟`. A pairing that needs
   two differential operators (e.g. the mixed `(Q ∇u, v)` gradient-interpolation) is a DIFFERENT term variant
   on a mixed/rectangular sub-axis (`MixedVectorGradientIntegrator`, `palace/fem/integrator.hpp:197`), not a
   composition of two `weak_form_term`s — out of this entry's square-pairing scope (see *Variant axes*).

4. **Symmetry of the pairing (for symmetric `Q`)**: when `Q` is symmetric (scalar, or symmetric-matrix-valued),
   `a(u, v) = a(v, u)` because `(Q · 𝒟u, 𝒟v) = (Q · 𝒟v, 𝒟u)` — the term assembles a symmetric operator block.
   This is what makes the witnessed solver-K terms (diffusion, curl-curl) assemble into the `SymmetricOperator`
   construction `fe_assemble` uses for the square trial=test case
   (`book/src/L1/fe_assemble.md` *trial-test-coincidence* axis). (Caveat: symmetry is a property of `Q`, not of
   the term constructor — a non-symmetric matrix coefficient breaks it; recorded as a non-law below.)

Laws that explicitly **do not** hold:

- **No SPD / definiteness guarantee**: `weak_form_term(Q, 𝒟)` need not assemble an SPD or even nonsingular
  block — a pure gradient (diffusion) term assembles a singular operator before BC-elimination (the constant
  null-space), and a curl-curl term has the full gradient null-space. The term carries no
  positive-definiteness precondition; definiteness is downstream BC-elimination's concern
  ([`eliminate_essential_bc`](./eliminate_essential_bc.md)).
- **No symmetry guarantee for non-symmetric `Q`**: law 4 holds only for symmetric `Q`. A non-symmetric
  matrix-valued material coefficient assembles a non-symmetric block; the term constructor does not enforce
  symmetry.
- **Differential operators do NOT compose within a term**: per law 3, the `diff_op` axis is discrete; there is
  no `Gradient ∘ Curl` term. Mixed-operator pairings are separate (mixed/rectangular) integrator variants, not
  combinations of this entry's terms.

## Dependencies

`weak_form_term` is a **leaf at L1**: it is an inert pair constructor and uses no other firm L1 operator. It is
consumed by exactly one firm L1 operator — [`fe_assemble`](./fe_assemble.md), which folds over a list of these
terms. Two adjacent opaque objects it references but does NOT define:

- `MaterialCoefficient` (`coefficient` slot) — the material-property weight `Q`, an attribute-to-property map
  (`MaterialPropertyCoefficient` at L0, `palace/fem/integrator.hpp:42`). Opaque at L1: the term carries it as an
  inert weight; its per-quadrature-point evaluation is an L0/libCEED concern.
- `A(space, ·)` — the opaque per-term element-local→global assembly map that *realizes* the term. The term is
  `A`'s argument; `A`'s kernel body is libCEED-owned (the
  [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md) L1>L0
  obstruction theme, `opaque-library-ownership`, established cycle-055 — identical boundary across all 5 solver
  pipelines). The TERM's IDENTITY (which `Q`, which `𝒟`) IS Palace-readable at the instantiation site
  (`AddDomainIntegrator<T>(Q)`); only the term's KERNEL is opaque. `weak_form_term` formalizes the
  Palace-readable identity; `A` realizes it.

## Variant axes

- **differential-operator** (the primary axis): `Gradient` (∇, H1 — `DiffusionIntegrator`,
  `palace/fem/integrator.hpp:100-101`) | `Identity` (the L² pairing, H1 or vector-FE — `MassIntegrator`
  `palace/fem/integrator.hpp:68-69` / `VectorFEMassIntegrator` `:79-80`) | `Curl` (∇×, H(curl)/Nedelec —
  `CurlCurlIntegrator`, `palace/fem/integrator.hpp:111-112`) | `Divergence` (∇·, H(div)/Raviart-Thomas —
  `DivDivIntegrator`, `palace/fem/integrator.hpp:122-123`). **Grounded variant points (pulled by an in-scope
  solver-K witness):**
  - `Gradient` — the **electrostatic** stiffness term `(ε, ∇)`, witnessed
    `palace/models/laplaceoperator.cpp:191-192` (`fe_assemble`'s single-term witness).
  - `Curl` — the **magnetostatic** stiffness term `(μ⁻¹, ∇×)`, witnessed
    `palace/models/curlcurloperator.cpp:179-181` (this cycle's pull).
  **Pending-pull sibling variant points (named axis points, NOT yet authored — await their own pipeline pull):**
  - `Identity` (mass) — `Mass`/`VectorFEMass`-realized `(Q, I)` term. The **most-likely next pull**: mass terms
    appear pervasively across the eigenmode/driven/transient pipelines (`VectorFEMassIntegrator` consumer sites
    at `palace/models/spaceoperator.cpp:278`, `palace/models/modeeigensolver.cpp:62`,
    `palace/models/domainpostoperator.cpp:38`, `palace/models/romoperator.cpp:424`). Awaits a pipeline pull that
    NEEDS a mass-term solver-K/M witness (not speculatively authored here per the redirect's pull-only clean-gate).
  - `Divergence` (div-div) — `DivDivIntegrator`-realized `(Q, ∇·)` term. **No in-scope solver-K witness** in the
    pulled pipelines; the integrator wrapper exists (`palace/fem/integrator.hpp:122-123`) but no
    `AddDomainIntegrator<DivDivIntegrator>` instantiation appears among the model operator K-builds (codemap
    search over `palace/models/*.cpp` returns no `DivDivIntegrator` use site). Recorded as a **possible
    spine-coverage finding**: the term variant is named on the axis but may never receive an in-scope pull — if a
    future pipeline needs it, it pulls; if not, its absence is a finding about Palace's H(div) K-build surface,
    not a gap to fill speculatively.
- **coefficient-rank** (sub-axis): `scalar` (a scalar material coefficient — e.g. isotropic `ε`, `μ⁻¹`) |
  `matrix` (an anisotropic matrix-valued `Q`). Both ride the same `MaterialPropertyCoefficient *Q` base-class
  slot (`palace/fem/integrator.hpp:42`); the rank is a property of the coefficient, variant-invariant across
  `diff_op`. The witnessed solver-K coefficients (`epsilon_func`, `muinv_func`) are built from material-property
  maps that may be scalar or matrix per material (`palace/models/laplaceoperator.cpp:191`,
  `palace/models/curlcurloperator.cpp:178-179`).
- **term-position** (inherited from `fe_assemble`'s fold): `domain` (volume integrator,
  `AddDomainIntegrator`) | `boundary` (surface integrator, `AddBoundaryIntegrator`,
  `palace/fem/bilinearform.hpp:59-63`). A term's position determines which sub-list it enters; at L1 both enter
  `fe_assemble`'s single concatenated term list (per `fe_assemble`'s concatenation-homomorphism law). The
  witnessed solver-K stiffness terms are both `domain`.

**Out-of-scope (square-pairing carve-out):** the **mixed/rectangular** integrators
(`MixedVectorGradientIntegrator` `palace/fem/integrator.hpp:197`, `MixedVectorWeakCurlIntegrator` `:250`,
`MixedVectorCurlIntegrator` `:229`, etc.) pair *different* differential operators on trial vs. test (`(Q ∇u, v)`,
not `(Q 𝒟u, 𝒟v)`). They are a distinct term family on a mixed/rectangular axis (per law 3, NOT a composition of
square `weak_form_term`s); they enter the spine only when a pipeline pull NEEDS them (the eigenmode and ROM
operators use them — `palace/models/modeeigensolver.cpp:50`, `palace/models/spaceoperator.cpp:298-299`). Named
here as adjacent, not authored.

## Status

`firm`. **Clean-gate call: PROMOTE — clean (pulled, not speculative).** The promotion is justified because the
operator's definition, signature, and all four algebraic laws are stated entirely in **existing shared
vocabulary** — a `(coefficient, differential-operator)` pair whose laws are bilinearity/symmetry/scaling facts —
**grounded by two in-scope solver-K witnesses** (the redirect's pull-only clean-gate is satisfied: the
magnetostatic pipeline concretely NEEDS a non-diffusion term, and the curl-curl K-build uses the identical
`BilinearForm`-fold differing only in the integrator). This is NOT speculative vocabulary expansion: it is the
term abstraction that the firm `fe_assemble` fold already quantifies over, now firmed in its own L1 vocabulary
because a second pipeline forced the `(coefficient, differential-operator)` factorization into view (one witness
could be coincidence; two witnesses differing in EXACTLY the integrator slot establish the variant axis).

The term's KERNEL is the libCEED-owned opaque map `A` (the
[`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md) boundary,
`opaque-library-ownership`, cycle-055) — but the term's IDENTITY (which `Q`, which `𝒟`) is Palace-readable at
the `AddDomainIntegrator<T>(Q)` instantiation site, and THAT is what this entry formalizes. The opaque kernel
does NOT gate the term's firmness any more than it gated `fe_assemble`'s (the term is `A`'s argument; `A`'s
classification is independent).

This is the **firm-on-positive-structure** situation (the `fe_assemble` / `apply_linop` / BLAS-1-leaf
precedent): the four laws are bilinearity/scaling/symmetry identities on a fully-specified positive pair
structure, so the absence of a dedicated `weak_form_term` unit test does not gate them. (The libCEED
full-assemble materialization IS test-covered — `test/unit/test-libceed.cpp` `TestCeedOperatorFullAssemble`
asserts the assembled matrix matches an MFEM reference to 1e-12 — useful as future `empirical-match` evidence
for the term's realization `A`, but not needed for the term's pair-constructor laws.)

## L1 vs L0 distinction

- **L0**: the term is a `(template-type T, runtime-coefficient-arg Q)` pair materialized as a heap-owned
  `std::unique_ptr<T>` pushed onto a mutable integrator container by `AddDomainIntegrator<T>(Q)`
  (`palace/fem/bilinearform.hpp:53-57` — `domain_integs.push_back(make_unique<T>(Q))`). The differential
  operator lives in the C++ *type system* (the template parameter selecting the `BilinearFormIntegrator`
  subclass); the coefficient lives in a runtime object. State is threaded through the owned container.
- **L1**: the term is a pure inert `{ coefficient, diff_op }` record value — one element of the immutable list
  `fe_assemble` folds over. No container, no `push_back`, no heap ownership. The differential operator is a
  first-class enumeration value (not a C++ type), and the coefficient is an inert weight. The L0
  template-dispatch, the `make_unique`/`push_back` build-up, and the owned-container threading are all L1>L0
  lowering concerns ([`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md)).

## Evidence

- `palace/fem/integrator.hpp:39-42` — `BilinearFormIntegrator` base class: holds the
  `const MaterialPropertyCoefficient *Q` coefficient slot, **uniform across every differential-operator
  variant** — the structural ground for factoring the coefficient out of the variant axis.
- `palace/fem/integrator.hpp:68-69` — `MassIntegrator`: `a(u, v) = (Q u, v)` for H1 / vector-`(H1)ᵈ` — the
  `Identity` differential-operator variant (pending-pull sibling).
- `palace/fem/integrator.hpp:79-80` — `VectorFEMassIntegrator`: `a(u, v) = (Q u, v)` for vector finite elements
  — the vector-FE realization of the `Identity` variant.
- `palace/fem/integrator.hpp:100-101` — `DiffusionIntegrator`: `a(u, v) = (Q grad u, grad v)` for H1 — the
  `Gradient` variant (grounded by the electrostatic witness).
- `palace/fem/integrator.hpp:111-112` — `CurlCurlIntegrator`: `a(u, v) = (Q curl u, curl v)` for Nedelec — the
  `Curl` variant (grounded by the magnetostatic witness).
- `palace/fem/integrator.hpp:122-123` — `DivDivIntegrator`: `a(u, v) = (Q div u, div v)` for Raviart-Thomas —
  the `Divergence` variant (pending-pull sibling; no in-scope solver-K witness).
- `palace/fem/bilinearform.hpp:53-57` — `AddDomainIntegrator<T>(args...)`: the templated append
  (`domain_integs.push_back(make_unique<T>(args...))`) — the L0 term-construction surface where the
  differential operator is the template parameter `T` and the coefficient is the runtime arg.
- `palace/models/laplaceoperator.cpp:184-194` — `LaplaceOperator::GetStiffnessMatrix`: the **electrostatic
  witness**. `MaterialPropertyCoefficient epsilon_func(...)` (`:191`) +
  `k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func)` (`:194`) — the term `(ε, ∇)`. Grounds the
  `Gradient` variant point.
- `palace/models/curlcurloperator.cpp:170-181` — `CurlCurlOperator::GetStiffnessMatrix`: the **magnetostatic
  witness** (this cycle's pull). `MaterialPropertyCoefficient muinv_func(...)` (`:178-179`) +
  `k.AddDomainIntegrator<CurlCurlIntegrator>(muinv_func)` (`:181`) — the term `(μ⁻¹, ∇×)`; the SAME
  `BilinearForm`-fold as the electrostatic witness, differing ONLY in the integrator. Grounds the `Curl` variant
  point and establishes the differential-operator variant axis.
- `palace/fem/integrator.hpp:197,229,250` — the mixed/rectangular integrators
  (`MixedVectorGradientIntegrator` / `MixedVectorCurlIntegrator` / `MixedVectorWeakCurlIntegrator`): the
  out-of-scope mixed-pairing term family (named adjacent, not authored).
- `book/src/L1/fe_assemble.md` — the sole downstream consumer: the integrator-fold `K = Σ_i A(space, term_i)`
  that folds over a `[WeakFormTerm]` list. This entry firms the element type that fold quantifies over.
- `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` — the `opaque-library-ownership` obstruction theme
  (cycle-055) classifying the per-term assembly map `A`'s kernel: the term's KERNEL is opaque, the term's
  IDENTITY is Palace-readable.
- `test/unit/test-libceed.cpp` — `TestCeedOperatorFullAssemble` (L0-equivalent: assembled matrix matches MFEM
  reference to 1e-12; future `empirical-match` evidence for the term's realization `A`).

## Downward to L0

`weak_form_term` has no dedicated L1>L0 lowering theme of its own: as the inert element type of `fe_assemble`'s
fold, its L0 realization is folded into the existing FE-assembly lowering surface —
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) (the
build-up-then-assemble protocol, where the term is materialized as `make_unique<T>(Q)` and pushed onto the owned
container) and [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md)
(the term's per-element quadrature kernel realization `A`, libCEED-owned). The term's *identity* lowers trivially
(the `(coefficient, diff_op)` pair maps to the `(Q, T)` instantiation slots); its *realization* lowers through
the libCEED boundary. No new theme is warranted — the term is a strict sub-component of the already-firm
`fe_assemble` fold.
```

```edit:book/src/L1/fe_assemble.md
- `terms` — `[WeakFormTerm]` — an immutable, finite list of weak-form contributions. **`WeakFormTerm`
  is an opaque rough-in input here** (see *Dependencies*): `fe_assemble` quantifies over the term
  list without cracking open a term's `(coefficient, differential-operator)` internals.
```
```edit-to:book/src/L1/fe_assemble.md
- `terms` — `[WeakFormTerm]` — an immutable, finite list of weak-form contributions. Each element is a firm
  [`weak_form_term`](./weak_form_term.md) — a `(coefficient, differential-operator)` pair (firm cycle-061).
  `fe_assemble` quantifies over the term list **opaquely**: the fold's structure and laws never crack open a
  term's `(coefficient, differential-operator)` internals (see *Dependencies*), so the term's firmness does not
  alter `fe_assemble`'s definition — it replaces an undefined placeholder with a defined-but-still-opaquely-folded
  input.
```

```edit:book/src/L1/fe_assemble.md
- `WeakFormTerm` (type) — opaque rough-in input; the `(coefficient, differential-operator)` pair
  that is the element type of the term list. This is the genuinely-NEW FE vocabulary the sub-spine
  introduces; the witnessed differential-operator cohort so far is ∇ (diffusion), identity (mass),
  curl (curl-curl), div (div-div) (`palace/fem/integrator.hpp:39-130`). **`fe_assemble` does not
  crack open the term** — it folds over the list opaquely — so the type's formalization is deferred
  without gating this entry (the clean-gate call, see §Status). The term-cohort enumeration is
  follow-on work tracked at the
  [`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md)
  theme.
```
```edit-to:book/src/L1/fe_assemble.md
- [`weak_form_term`](./weak_form_term.md) (type) — **firm** (cycle-061); the `(coefficient,
  differential-operator)` pair that is the element type of the term list. This is the genuinely-NEW FE
  vocabulary the sub-spine introduces; the **differential-operator** is the variant axis — grounded by two
  in-scope solver-K witnesses, ∇/Gradient (electrostatic diffusion, `palace/models/laplaceoperator.cpp:191-192`)
  and ∇×/Curl (magnetostatic curl-curl, `palace/models/curlcurloperator.cpp:179-181`) — with identity/mass and
  div-div named as pending-pull sibling variants (`palace/fem/integrator.hpp:39-130`). **`fe_assemble` does not
  crack open the term** — it folds over the list opaquely — so although the term is now firm, the fold's
  structure and laws are unchanged: the term remains an opaquely-folded input (the clean-gate call, see
  §Status). The per-term assembly map `A(space, ·)` that *realizes* a term is the libCEED-owned leaf below.
```
```

## Operator content

(The full firm chapter body is authored inside the `new:book/src/L1/weak_form_term.md` proposed-changes
block above — Slug + one-line, Signature with shape contracts, Semantics, four Algebraic laws + non-laws,
Dependencies, Variant axes with the grounded/pending-pull differential-operator axis, Status: firm
(clean-gate PROMOTE — pulled), L1-vs-L0, and Evidence with self-verified citations.)

## Index + SUMMARY registration

```edit:book/src/L1/index.md
- **`fe_assemble` is now FIRM** (cycle-054) — see [`fe_assemble`](./fe_assemble.md). Assemble a global FE operator from a space + immutable weak-form term list as the integrator-fold `K = Σ_i A(term_i)`; clean-gate PROMOTE (the fold is definable treating `weak_form_term` as an opaque rough-in input — it does not crack open the term). **Slug-collision note**: NOT the existing [`bilinear-form`](./bilinear-form.md) (the BLAS-2 reduction `xᴴ M y`); `fe_assemble` is the C++ `BilinearForm`-*class* assembler. Laws: empty-term identity, concatenation-homomorphism, single-term reduction, term-position commutativity. The `weak_form_term` type + the per-term assembly map `A(·)` (libCEED boundary) stay deferred-rough-in inputs the fold quantifies over.
```
```edit-to:book/src/L1/index.md
- **`fe_assemble` is now FIRM** (cycle-054) — see [`fe_assemble`](./fe_assemble.md). Assemble a global FE operator from a space + immutable weak-form term list as the integrator-fold `K = Σ_i A(term_i)`; clean-gate PROMOTE (the fold is definable treating `weak_form_term` as an opaque rough-in input — it does not crack open the term). **Slug-collision note**: NOT the existing [`bilinear-form`](./bilinear-form.md) (the BLAS-2 reduction `xᴴ M y`); `fe_assemble` is the C++ `BilinearForm`-*class* assembler. Laws: empty-term identity, concatenation-homomorphism, single-term reduction, term-position commutativity. The per-term assembly map `A(·)` (libCEED boundary) stays a deferred-rough-in input; the `weak_form_term` element type the fold quantifies over is now **firm** (cycle-061, see next bullet).
- **`weak_form_term` is now FIRM** (cycle-061) — see [`weak_form_term`](./weak_form_term.md). The `(coefficient, differential-operator)` pair that is the element type of [`fe_assemble`](./fe_assemble.md)'s term list; one weak-form contribution `a(u, v) = (Q · 𝒟u, 𝒟v)`. **The differential operator is the variant axis** — grounded by two in-scope solver-K witnesses: `Gradient` (∇, electrostatic diffusion `(ε, ∇)`, `palace/models/laplaceoperator.cpp:191-192`) + `Curl` (∇×, magnetostatic curl-curl `(μ⁻¹, ∇×)`, `palace/models/curlcurloperator.cpp:179-181`) — the SAME `BilinearForm`-fold differing ONLY in the integrator, which establishes the axis. `Identity` (mass, `Mass`/`VectorFEMass`) + `Divergence` (div-div, `DivDivIntegrator`) are named **pending-pull sibling variants** (mass = most-likely next pull; div-div = possible spine-coverage finding, no in-scope solver-K witness). Clean-gate PROMOTE (pulled, not speculative — the redirect's pull-only gate is satisfied by the magnetostatic NEED for a non-diffusion term). Laws: coefficient-linearity, coefficient-additivity, differential-operator-discreteness, symmetry-for-symmetric-`Q`. The term's KERNEL is the libCEED-owned opaque map `A` ([`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md), `opaque-library-ownership`); the term's IDENTITY (which `Q`, which `𝒟`) is Palace-readable at the `AddDomainIntegrator<T>(Q)` instantiation site — THAT is what this entry firms. Firm-on-positive-structure (no-dedicated-test caveat non-gating, per `fe_assemble` precedent). Re-anchors `fe_assemble`'s opaque-`WeakFormTerm` rough-in note to a live link.
```

**Dep-map TABLE row (append after the `eliminate_essential_bc` row, line 113):**

```edit:book/src/L1/index.md
| [`eliminate_essential_bc`](./eliminate_essential_bc.md) | `(K: LinearOperator[N, N], dofs: DofSet[N], policy: DiagPolicy) → LinearOperator[N, N]` (i.e. `P_F K P_F` for `DIAG_ZERO`; `+ I_E` for `DIAG_ONE`) | (leaf; separable post-composition on the assembled square operator; composes AFTER [`fe_assemble`](./fe_assemble.md), NOT a dependency, NOT part of the assembly fold) | `firm` (FE-assembly sub-spine separable post-composition; diagonal-policy variant axis `DIAG_ONE`/`DIAG_ZERO`; L0: `palace/linalg/rap.cpp:36-47,141-143` + witness `palace/models/laplaceoperator.cpp:216-217` + eigen-pipeline consumers `palace/models/modeeigensolver.cpp:571,574,608,611`; harvested cycle-055; firm-on-positive-structure, no-dedicated-test caveat non-gating; idempotence + free-block-preservation + distribution-over-assembly laws) |
```
```edit-to:book/src/L1/index.md
| [`eliminate_essential_bc`](./eliminate_essential_bc.md) | `(K: LinearOperator[N, N], dofs: DofSet[N], policy: DiagPolicy) → LinearOperator[N, N]` (i.e. `P_F K P_F` for `DIAG_ZERO`; `+ I_E` for `DIAG_ONE`) | (leaf; separable post-composition on the assembled square operator; composes AFTER [`fe_assemble`](./fe_assemble.md), NOT a dependency, NOT part of the assembly fold) | `firm` (FE-assembly sub-spine separable post-composition; diagonal-policy variant axis `DIAG_ONE`/`DIAG_ZERO`; L0: `palace/linalg/rap.cpp:36-47,141-143` + witness `palace/models/laplaceoperator.cpp:216-217` + eigen-pipeline consumers `palace/models/modeeigensolver.cpp:571,574,608,611`; harvested cycle-055; firm-on-positive-structure, no-dedicated-test caveat non-gating; idempotence + free-block-preservation + distribution-over-assembly laws) |
| [`weak_form_term`](./weak_form_term.md) | `({ coefficient: MaterialCoefficient, diff_op: DifferentialOperator }) → WeakFormTerm` (i.e. one weak-form contribution `a(u, v) = (Q · 𝒟u, 𝒟v)`, `𝒟 ∈ {Gradient, Identity, Curl, Divergence}`) | (leaf; inert `(coefficient, differential-operator)` pair; the element type [`fe_assemble`](./fe_assemble.md) folds over opaquely — consumed-by, NOT a dependency; the per-term realization `A(space, ·)` is the libCEED-owned opaque map below the fold) | `firm` (FE-assembly sub-spine term abstraction; **differential-operator variant axis** — `Gradient`/`Curl` grounded by two in-scope solver-K witnesses `palace/models/laplaceoperator.cpp:191-192` + `palace/models/curlcurloperator.cpp:179-181` (same `BilinearForm`-fold, integrator-slot-only difference); `Identity`/mass + `Divergence`/div-div named pending-pull siblings; L0 integrator wrappers `palace/fem/integrator.hpp:39-130` + instantiation `palace/fem/bilinearform.hpp:53-57`; harvested cycle-061; clean-gate PROMOTE pulled-not-speculative; firm-on-positive-structure, no-dedicated-test caveat non-gating per `fe_assemble` precedent; laws: coefficient-linearity + coefficient-additivity + diff-op-discreteness + symmetry-for-symmetric-`Q`; term KERNEL libCEED-opaque, term IDENTITY Palace-readable) |
```

**SUMMARY.md chapter registration (integrator applies — add under the L1 Part, after the `fe_assemble` line 114; placed adjacent to its sole consumer):**

```edit:book/src/SUMMARY.md
- [fe_assemble](./L1/fe_assemble.md)
- [eliminate_essential_bc](./L1/eliminate_essential_bc.md)
```
```edit-to:book/src/SUMMARY.md
- [fe_assemble](./L1/fe_assemble.md)
- [weak_form_term](./L1/weak_form_term.md)
- [eliminate_essential_bc](./L1/eliminate_essential_bc.md)
```

## Supporting evidence

- **Pulled witnesses (self-verified via `citecheck --anchor`):**
  - `palace/models/laplaceoperator.cpp:184-194` — electrostatic K-build; `DiffusionIntegrator(epsilon_func)` at
    `:194`, `epsilon_func` at `:191`. citecheck `:191-194 --anchor DiffusionIntegrator` → `[ok]` (anchor at 194).
  - `palace/models/curlcurloperator.cpp:170-181` — magnetostatic K-build; `CurlCurlIntegrator(muinv_func)` at
    `:181`, `muinv_func` at `:178-179`. citecheck `:170-181 --anchor CurlCurlIntegrator` → `[ok]` (anchor at 181).
- **Integrator wrappers (self-verified):** `palace/fem/integrator.hpp:39-42` (`BilinearFormIntegrator` base, `Q`
  slot), `:68-69` (`MassIntegrator`), `:79-80` (`VectorFEMassIntegrator`), `:100-101` (`DiffusionIntegrator`),
  `:111-112` (`CurlCurlIntegrator`), `:122-123` (`DivDivIntegrator`) — all citecheck `[ok]`.
- **Instantiation surface:** `palace/fem/bilinearform.hpp:53-57` — `AddDomainIntegrator<T>(args)` (read in full:
  `domain_integs.push_back(make_unique<T>(forward<U>(args)...))`), grounding the `(template-type T, coefficient
  arg)` = `(differential-operator, coefficient)` factorization.
- **Consumer:** `book/src/L1/fe_assemble.md` (firm cycle-054) — the sole downstream consumer; its opaque-input
  note at `:69-71` + `:158-166` is re-anchored to a live link by this report's proposed changes.
- **Pending-pull sibling negative anchor (div-div):** codemap `search_text 'AddDomainIntegrator<.*Integrator>'`
  over `palace/models/*.cpp` returns NO `DivDivIntegrator` instantiation among the model operator K-builds —
  establishing that div-div has no in-scope solver-K witness (recorded as a possible spine-coverage finding, not
  a gap to fill speculatively).
- **Methodology:** vocabulary-shift redirect (`METHODOLOGY-REDIRECT.md`; CLAUDE.md §Methodology invariants) —
  the pull-only clean-gate (author term forms only as a pipeline pull-up NEEDS them) is satisfied: the
  magnetostatic pipeline concretely needs a non-diffusion term, and two witnesses differing in exactly the
  integrator slot establish the differential-operator variant axis. Combinator-miner-style replace-and-propagate
  applied (fe_assemble opaque-input note re-anchored, not stranded).

## Open questions / caveats

- **Concept page NOT authored.** `weak_form_term` has exactly one downstream consumer (`fe_assemble`) at L1 —
  below the ≥2-consumer / genuine-cross-cutting bar for a `book/src/concepts/` page. If a future pipeline pull
  adds a second independent consumer of the term abstraction (e.g. an L2 assembly combinator that folds terms,
  or a mass-term pull that references the differential-operator axis from a distinct site), reconsider promoting
  the `(coefficient, differential-operator)` factorization + the differential-operator de-Rham-position table to
  a concept page. Flagged for the OQ ledger (not parked — a plan candidate if the second consumer materializes).
- **Mass (`Identity`) is the most-likely next pull** — pervasive `VectorFEMassIntegrator` use across the
  eigenmode/driven/transient/ROM pipelines (consumer sites enumerated in the entry's *Variant axes*). When a
  pipeline pull NEEDS a mass-term solver-K/M witness, the `Identity` variant point gets authored under this entry
  (a specialization note, per the redirect's combinator-primary discipline — NOT a new standalone entry).
- **Div-div (`Divergence`) may never receive an in-scope pull** — the integrator wrapper exists but no model
  operator K-build instantiates it. If a future H(div) pipeline needs it, it pulls; if not, its named-but-unpulled
  status on the axis IS the spine-coverage finding (Palace's in-scope solver set does not exercise a div-div
  stiffness term). No speculative authoring.
- **Layer-intro refresh (note for `layer-intro-author`):** the L1 index §"Firm (FE-assembly sub-spine)" count
  prose currently reads "3" members (`fe_assemble` + `eliminate_essential_bc` + `eliminate_rhs`). `weak_form_term`
  is a 4th sub-spine member (the term abstraction the fold quantifies over). I have registered my own dep-map row
  + my own cohort bullet (under the sub-spine subsection) per the dual-registration partition; the **consolidated
  sub-spine count prose** ("3" → "4") + the §Vocabulary-cohort grand-total tally ("29 firm grand total") are the
  consolidated running-count TALLY — I am the sole L1-touching op-add this cycle and the dispatch names no other
  count-owner, so I own that tally too. The proposed cohort bullet + dep-map row above carry it; the layer-intro
  count-prose refresh ("FE-assembly sub-spine — 3" → "4"; grand total "29" → "30") is flagged for the
  layer-intro-author as a follow-on (it lives in the §Vocabulary-cohort header prose, layer-intro-author's
  domain, not the per-operator bullet I own).

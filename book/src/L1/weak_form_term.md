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
**map** `A(space, ·)` (the element-local quadrature kernel + restriction over the finite-element space
[`fe_space`](./fe_space.md) constructs, libCEED-owned — see *Dependencies*).
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
  solver-K/M witness — 3 of 4):**
  - `Gradient` — the **electrostatic** stiffness term `(ε, ∇)`, witnessed
    `palace/models/laplaceoperator.cpp:191-192` (`fe_assemble`'s single-term witness).
  - `Curl` — the **magnetostatic** stiffness term `(μ⁻¹, ∇×)`, witnessed
    `palace/models/curlcurloperator.cpp:179-181` (c061's pull).
  - `Identity` — the **mass** term `(Q, I)` — the identity differential operator (`𝒟u = u`, **no derivative**),
    realizing the L² pairing `a(u, v) = (Q u, v)`. Witnessed by `SpaceOperator::GetMassMatrix`
    (`palace/models/spaceoperator.cpp:438`), whose `AddIntegrators` fold (`palace/models/spaceoperator.cpp:260`)
    appends `a.AddDomainIntegrator<VectorFEMassIntegrator>(*f)` (`palace/models/spaceoperator.cpp:278`) with the
    mass coefficient `*f`. This is the **SAME `BilinearForm`-fold** as the Gradient/Curl witnesses — an
    integrator-slot-only difference (here `VectorFEMassIntegrator` over a vector-FE/Nedelec space; the
    coefficient still rides the variant-invariant base-class slot `palace/fem/integrator.hpp:39-42`). The mass
    term is heavily multi-witness (eigenmode/driven/transient/ROM/postprocess) — additional consumer sites at
    `palace/models/modeeigensolver.cpp:62`, `palace/models/domainpostoperator.cpp:38`,
    `palace/models/romoperator.cpp:424`. (Grounded c062.)
  **Pending-pull sibling variant point (named axis point, NOT yet authored — awaits its own pipeline pull):**
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
could be coincidence; multiple witnesses differing in EXACTLY the integrator slot establish the variant axis).
The differential-operator variant axis is now **3-of-4 grounded** by in-scope solver-K/M witnesses
(`Gradient`/electrostatic, `Curl`/magnetostatic, `Identity`/mass — the last grounded c062 at
`palace/models/spaceoperator.cpp:278`,`:438`); only `Divergence`/div-div remains a named pending-pull sibling
(no in-scope witness). The grounding is an in-place specialization note under the term abstraction
(combinator-primary per the 2026-06-01 redirect §1), not a new mirrored entry; the term-abstraction-level
algebraic laws are witness-independent and unchanged.

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
  `Identity` differential-operator variant (grounded c062; identity operator, no derivative).
- `palace/fem/integrator.hpp:79-80` — `VectorFEMassIntegrator`: `a(u, v) = (Q u, v)` for vector finite elements
  — the vector-FE realization of the `Identity` variant (the integrator the mass witness instantiates).
- `palace/models/spaceoperator.cpp:434-460` — `SpaceOperator::GetMassMatrix`: the **mass witness** (c062's
  grounding). Builds the mass coefficient `fr` (`AddRealMassCoefficients(1.0, fr)`) then assembles via
  `AssembleOperator(GetNDSpace(), nullptr, &fr, ...)` (`:459`), which routes through `AddIntegrators`
  (`palace/models/spaceoperator.cpp:260`) appending
  `a.AddDomainIntegrator<VectorFEMassIntegrator>(*f)` (`palace/models/spaceoperator.cpp:278`) — the term `(Q, I)`,
  the identity differential operator (`𝒟u = u`). The SAME `BilinearForm`-fold as the electrostatic/magnetostatic
  witnesses, differing ONLY in the integrator slot. Grounds the `Identity` variant point — the differential-operator
  variant axis is now **3 of 4 grounded** (only `Divergence`/div-div remains pending-pull).
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

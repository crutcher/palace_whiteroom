---
theme: weak-form-term-rotation
layer_from: L1
layer_to: L0
status: firm
justification_kind: structural
l1_form: book/src/L1/weak_form_term.md
---

# weak-form-term-rotation

**Slug:** `weak-form-term-rotation`

How the pure L1 [`weak_form_term`](../L1/weak_form_term.md) value `{ coefficient, diff_op }` lowers into its
concrete Palace L0 form: the imperative templated integrator-registration call
`k.AddDomainIntegrator<T>(Q)`. This is a **vocabulary translation across two different organizations of the same
information** — a pure pair value on the L1 side, a C++ template-type-plus-runtime-argument dispatch into a
mutable heap-owned container on the L0 side — NOT a one-to-one named-term rename.

## L1 form (LHS)

The pure inert pair value (the firm L1 operator's result):

    weak_form_term :: { coefficient: MaterialCoefficient, diff_op: DifferentialOperator } -> WeakFormTerm

    data DifferentialOperator = Gradient | Identity | Curl | Divergence

One element of the immutable `[WeakFormTerm]` list that [`fe_assemble`](../L1/fe_assemble.md) folds over. At L1
the term is inert data: it carries the *identity* of a weak-form contribution `a(u, v) = (Q · 𝒟u, 𝒟v)` — which
coefficient `Q`, which differential operator `𝒟` — and nothing executable. No container, no ordering, no heap
ownership.

## L0 form (RHS)

The concrete Palace instantiation: a templated append onto a `BilinearForm`'s owned integrator container.

    template <typename T, typename... U>
    void AddDomainIntegrator(U &&...args)
    {
      domain_integs.push_back(std::make_unique<T>(std::forward<U>(args)...));
    }

(`palace/fem/bilinearform.hpp:53-57`). The L1 pair's two slots translate onto two structurally-distinct L0
carriers:

- **`diff_op` (the differential operator) → the template parameter `T`** — a concrete `BilinearFormIntegrator`
  subclass selected at compile time. The differential operator lives in the C++ *type system*, not as a runtime
  value. The wrapper class declarations name the realized bilinear form in their doc comments:
  `DiffusionIntegrator` realizes `a(u,v) = (Q grad u, grad v)` (`palace/fem/integrator.hpp:100-101`);
  `CurlCurlIntegrator` realizes `a(u,v) = (Q curl u, curl v)` (`palace/fem/integrator.hpp:111-112`).
- **`coefficient` (the material weight `Q`) → the runtime argument** — a `MaterialPropertyCoefficient` object
  forwarded into the integrator's constructor and held on the shared base class as
  `const MaterialPropertyCoefficient *Q` (`palace/fem/integrator.hpp:39-42`), **uniform across every
  differential-operator variant**. This base-class uniformity is the structural ground for the
  `(coefficient, differential-operator)` factorization: the coefficient slot is variant-invariant, the
  differential-operator slot is the variant axis.

The pure-value-to-imperative-call translation: the L1 record's construction (`{ coefficient, diff_op }`) becomes
the L0 `make_unique<T>(Q)` heap allocation + `push_back` onto the mutable `domain_integs` container. The list
*ordering* and *container threading* that the L1 `fe_assemble` fold abstracts away are the build-up concern of
the [`fe-operator-assemble-mutation-rotation`](./fe-operator-assemble-mutation-rotation.md) lowering; THIS theme
lowers a single term's `(Q, 𝒟)` → `(runtime-arg, template-T)` identity correspondence.

## The identity-lowers / kernel-opaque split (load-bearing)

The term has two separable aspects, and they lower through **different** L1>L0 surfaces:

- **The term's IDENTITY lowers HERE (cleanly).** *Which* coefficient and *which* differential operator a term
  names is fully Palace-readable at the instantiation site: the template parameter `T` names the differential
  operator, the runtime argument names the coefficient. The two grounded witnesses below show this correspondence
  read directly off the source. This is the content of THIS theme.
- **The term's KERNEL stays OPAQUE (lowers elsewhere, as an obstruction).** *How* a term's integrand
  `(Q · 𝒟u, 𝒟v)` is evaluated — the element-local quadrature contraction + dof restriction performed by the
  integrator's `Assemble` method — is the libCEED-owned opaque map `A(space, ·)` over the firm
  [`fe_space`](../L1/fe_space.md) (the `space` argument is the de-opaqued FE-space value; only the
  realization `A` stays library-owned). It is already classified as the
  `opaque-library-ownership` obstruction [`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md),
  identical across all 5 solver pipelines. It does NOT lower through this theme; this theme stops at the
  registration call.

The split mirrors the firm [`weak_form_term`](../L1/weak_form_term.md) entry's own framing: the term carries an
identity (Palace-readable, lowers here) plus a realization `A(space, ·)` (libCEED-opaque, obstruction sibling).
The opaque kernel no more gates this theme's firmness than it gated `fe_assemble`'s — the term is `A`'s argument;
`A`'s classification is independent.

## Applicability conditions

- The L1 term is a **square-pairing domain term** `(Q · 𝒟u, 𝒟v)` with trial and test functions on the same
  space (the same differential operator `𝒟` on both). The lowering targets `AddDomainIntegrator<T>(Q)` with a
  single `BilinearFormIntegrator` subclass `T`.
- The differential operator `𝒟` is one of the discrete enumeration values for which Palace ships a wrapper
  integrator (`palace/fem/integrator.hpp:39-130`). The two grounded cases below have an in-scope solver-K
  witness; the two pending-pull cases (mass, div-div) have a wrapper but no in-scope instantiation yet (see
  *Pending-pull axis points*).
- **Out of scope (matches the L1 entry's square-pairing carve-out):** mixed/rectangular pairings `(Q · 𝒟₁u, 𝒟₂v)`
  with different differential operators on trial vs. test (`MixedVector*Integrator`,
  `palace/fem/integrator.hpp:197,229,250`) are a distinct term family on a mixed/rectangular axis, not a
  single-`T` square-pairing lowering. The **boundary** term position (`AddBoundaryIntegrator<T>(Q)`,
  `palace/fem/bilinearform.hpp:59-63`) is the term-position sub-axis; the witnessed solver-K terms are both
  `domain`.

## Grounded rewrite cases

Two in-scope solver-K witnesses ground the differential-operator variant axis. They use the **SAME**
`BilinearForm`-fold and differ in EXACTLY the integrator slot (`T`) and its coefficient (`Q`) — which is what
establishes that the lowering quantifies over a `(coefficient, differential-operator)` family.

**Case 1 — `Gradient`/diffusion (electrostatic):** `weak_form_term { coefficient: ε, diff_op: Gradient }` lowers
to

    MaterialPropertyCoefficient epsilon_func(mat_op.GetAttributeToMaterial(),
                                             mat_op.GetPermittivityReal());
    BilinearForm k(GetH1Space());
    k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func);

(`palace/models/laplaceoperator.cpp:191-194`, inside `LaplaceOperator::GetStiffnessMatrix` at `:184`). `T =
DiffusionIntegrator` (the `Gradient` operator, H1 space), `Q = epsilon_func` (the permittivity `ε`), realizing
`a(u, v) = (ε ∇u, ∇v)`.

**Case 2 — `Curl`/curl-curl (magnetostatic):** `weak_form_term { coefficient: μ⁻¹, diff_op: Curl }` lowers to

    MaterialPropertyCoefficient muinv_func(mat_op.GetAttributeToMaterial(),
                                           mat_op.GetCurlCurlInvPermeability());
    BilinearForm k(GetNDSpace());
    k.AddDomainIntegrator<CurlCurlIntegrator>(muinv_func);

(`palace/models/curlcurloperator.cpp:179-181`, inside `CurlCurlOperator::GetStiffnessMatrix` at `:171`). `T =
CurlCurlIntegrator` (the `Curl` operator, Nedelec/H(curl) space), `Q = muinv_func` (the inverse permeability
`μ⁻¹`), realizing `a(u, v) = (μ⁻¹ ∇×u, ∇×v)`.

The two cases are byte-for-byte the same shape — `MaterialPropertyCoefficient <Q>(...)` then
`k.AddDomainIntegrator<T>(<Q>)` — differing only in `(T, Q)` and the space the `BilinearForm` is built over. This
is the structural evidence that the differential operator is the variant axis and the coefficient rides a
variant-invariant slot.

## Pending-pull axis points (named, NOT authored)

Under pull-only scoping (author a variant's concrete rewrite only when a pipeline pull NEEDS it):

- **`Identity`/mass** → `MassIntegrator` / `VectorFEMassIntegrator` (`palace/fem/integrator.hpp:68-69,79-80`),
  realizing `a(u, v) = (Q u, v)`. The most-likely next pull (pervasive across eigenmode/driven/transient/ROM
  pipelines), but no concrete `AddDomainIntegrator<...MassIntegrator>` solver-K/M witness is authored here. Its
  L0 instantiation site is filled in under this theme as a specialization note when its own pipeline pull lands.
- **`Divergence`/div-div** → `DivDivIntegrator` (`palace/fem/integrator.hpp:122-123`), realizing
  `a(u, v) = (Q ∇·u, ∇·v)`. **No in-scope solver-K witness**: the wrapper exists but no model-operator K-build
  instantiates it (the negative anchor — a codemap search over `palace/models/*.cpp` returns no
  `DivDivIntegrator` use site). Recorded as a possible spine-coverage finding, not a gap to fill speculatively.

## L1 vs L0 distinction

- **L0**: the term is a `(template-type T, runtime-coefficient-arg Q)` pair materialized as a heap-owned
  `std::unique_ptr<T>` pushed onto a mutable integrator container by `AddDomainIntegrator<T>(Q)`
  (`palace/fem/bilinearform.hpp:53-57`). The differential operator lives in the C++ type system (the template
  parameter); the coefficient lives in a runtime object; state is threaded through the owned container.
- **L1**: the term is a pure inert `{ coefficient, diff_op }` record value — one element of the immutable list
  `fe_assemble` folds over. The differential operator is a first-class enumeration value (not a C++ type), the
  coefficient is an inert weight, and there is no container or `push_back`. The template dispatch, the
  `make_unique`/`push_back` build-up, and the owned-container threading are L1>L0 lowering concerns — the
  container build-up belongs to [`fe-operator-assemble-mutation-rotation`](./fe-operator-assemble-mutation-rotation.md);
  THIS theme covers the per-term `(Q, 𝒟)` → `(runtime-arg, template-T)` identity translation.

## Speculative L1 operators

None. This theme lowers an already-firm L1 operator ([`weak_form_term`](../L1/weak_form_term.md), firm) into
existing L0 source; it proposes no new L1 vocabulary.

## Evidence

- `palace/models/laplaceoperator.cpp:188-194` — electrostatic K-build (`LaplaceOperator::GetStiffnessMatrix`,
  method at `:184`); `MaterialPropertyCoefficient epsilon_func(...)` (`:191-192`) +
  `k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func)` (`:194`). Grounds Case 1 (`Gradient`).
- `palace/models/curlcurloperator.cpp:170-181` — magnetostatic K-build
  (`CurlCurlOperator::GetStiffnessMatrix`, method at `:171`); `MaterialPropertyCoefficient muinv_func(...)`
  (`:179-180`) + `k.AddDomainIntegrator<CurlCurlIntegrator>(muinv_func)` (`:181`). Grounds Case 2 (`Curl`).
  SAME fold as Case 1, integrator-slot difference only.
- `palace/fem/bilinearform.hpp:53-57` — `AddDomainIntegrator<T>(args...)`: the templated append
  (`domain_integs.push_back(std::make_unique<T>(std::forward<U>(args)...))`) — the L0 instantiation surface. The
  template parameter `T` = differential operator; the forwarded argument = coefficient.
- `palace/fem/integrator.hpp:39-42` — `BilinearFormIntegrator` base: the `const MaterialPropertyCoefficient *Q`
  coefficient slot, uniform across every differential-operator variant (the factorization ground).
- `palace/fem/integrator.hpp:100-101` — `DiffusionIntegrator` doc comment `a(u,v) = (Q grad u, grad v)` (the
  `Gradient` wrapper); `:111-112` — `CurlCurlIntegrator` `a(u,v) = (Q curl u, curl v)` (the `Curl` wrapper);
  `:68-69`/`:79-80` — `MassIntegrator`/`VectorFEMassIntegrator` (the `Identity` pending-pull wrapper);
  `:122-123` — `DivDivIntegrator` (the `Divergence` pending-pull wrapper).
- `palace/fem/integrator.hpp:197,229,250` — the mixed/rectangular integrators (out-of-scope adjacent family).
- `book/src/L1/weak_form_term.md` (firm) — the L1 operator this theme lowers.
- `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` (`opaque-library-ownership`) — the term's
  KERNEL boundary (the identity-lowers/kernel-opaque split's opaque half).
- `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md` (firm) — the container build-up / assemble
  protocol; THIS theme is the per-term identity-translation sub-component below that fold.

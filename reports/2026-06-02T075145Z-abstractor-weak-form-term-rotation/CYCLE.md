---
agent: abstractor
invoked_at: 2026-06-02T075145Z
scope: L1>L0 theme sketch — weak-form-term-rotation
status: pending
integrated_at: 2026-06-02T082437Z
integration_commit: 018eea5
integration_notes: "Applied cycle-061 (D2; batch-19 position 1/3). NEW book/src/L1-L0/weak-form-term-rotation.md FIRM L1>L0 — LHS L1 weak_form_term {coefficient,diff_op} pair -> RHS L0 AddDomainIntegrator<T>(Q) template-type + runtime-arg dispatch; identity-lowers/kernel-opaque split; 2 grounded cases Gradient/DiffusionIntegrator + Curl/CurlCurlIntegrator; mass/div-div pending-pull. L1-L0/index.md theme TABLE row + SUMMARY.md. The live forward-ref to L1/weak_form_term.md resolves (D1 created it in the prior per-report invocation this cycle; canonical serial-per-report-then-finalize ordering). New theme file's own citations citecheck --scan 13 ok/0 failing (the 3 report-narrative AMBIG/MISS are inside the reproduced unchanged c055 fe-assemble-libceed-boundary-obstruction index anchor-context row that round-trips, pre-existing NOT introduced). L1>L0 firm themes +1. 0 new OQs. Build clean, exit 0; the new page renders; no dead link. Two-phase SHA patch to follow."
inputs:
  - cycle-061 dispatch D2 (wave 2)
  - L1 entry lowered: book/src/L1/weak_form_term.md (firm cycle-061, D1 LEAD this cycle)
  - D1 report: reports/2026-06-02T075145Z-harvester-weak-form-term/CYCLE.md
  - L0 witnesses: palace/models/laplaceoperator.cpp:188-194 (DiffusionIntegrator/epsilon_func) + palace/models/curlcurloperator.cpp:170-181 (CurlCurlIntegrator/muinv_func)
  - L0 instantiation surface: palace/fem/bilinearform.hpp:53-57 (AddDomainIntegrator<T>) + palace/fem/integrator.hpp:39-130 (wrapper layer)
  - sibling obstruction: book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md (opaque-library-ownership, c055)
  - vocabulary-shift redirect (METHODOLOGY-REDIRECT.md; CLAUDE.md §Methodology invariants)
---

# CYCLE: L1>L0 theme sketch — weak-form-term-rotation

## Summary

The L1 operator [`weak_form_term`](../../book/src/L1/weak_form_term.md) (firm this cycle, D1) is a pure inert
`{ coefficient, diff_op }` record naming one weak-form contribution `a(u, v) = (Q · 𝒟u, 𝒟v)`. This theme lowers
that record FORWARD into its concrete Palace L0 instantiation: the imperative templated append
`k.AddDomainIntegrator<T>(Q)` (`palace/fem/bilinearform.hpp:53-57`) that registers a specific
`BilinearFormIntegrator`-subclass into a `BilinearForm`'s owned integrator list. This is a genuine **vocabulary
translation, not a rename**: the L1 vocabulary is a pure `(coefficient, differential-operator)` *pair value*; the
L0 vocabulary is a *C++ template-type + runtime-arg dispatch into a mutable heap-owned container*. The two slots
of the L1 pair map onto two structurally-distinct L0 carriers — the differential operator becomes the **template
parameter `T`** (carried in the C++ *type system*), the coefficient becomes the **runtime argument `Q`** (a
`MaterialPropertyCoefficient` object). The **identity/kernel split** is the load-bearing content: the term's
IDENTITY (which `Q`, which `𝒟`) is fully Palace-readable at the instantiation site and IS what lowers cleanly;
the integrator's `Assemble` KERNEL is the libCEED opaque-library boundary (already classified
`obstruction (opaque-library-ownership)` via `fe-assemble-libceed-boundary-obstruction`, c055) — it does NOT
lower through this theme. Two GROUNDED rewrite cases: `Gradient`/diffusion → `DiffusionIntegrator(epsilon_func)`
(`palace/models/laplaceoperator.cpp:188-194`) and `Curl`/curl-curl → `CurlCurlIntegrator(muinv_func)`
(`palace/models/curlcurloperator.cpp:170-181`); mass (`Identity`) + div-div (`Divergence`) named as pending-pull
axis points, NOT speculatively authored (matching D1's scoping). Status: **firm** (structural — the
identity-translation is exhaustively cited at both witness sites; the kernel boundary is a named, already-firm
sibling obstruction, not a gap in this theme).

## Proposed changes

```new:book/src/L1-L0/weak-form-term-rotation.md
---
theme: weak-form-term-rotation
layer_from: L1
layer_to: L0
status: firm
justification_kind: structural
l1_form: book/src/L1/weak_form_term.md
verified_against:
  - palace/models/laplaceoperator.cpp:188-194
  - palace/models/curlcurloperator.cpp:170-181
  - palace/fem/bilinearform.hpp:53-57
  - palace/fem/integrator.hpp:39-130
---

# weak-form-term-rotation

**Slug:** `weak-form-term-rotation`

How the pure L1 [`weak_form_term`](../L1/weak_form_term.md) value `{ coefficient, diff_op }` lowers into its
concrete Palace L0 form: the imperative templated integrator-registration call
`k.AddDomainIntegrator<T>(Q)`. This is a **vocabulary translation across two different organizations of the same
information** — a pure pair value on the L1 side, a C++ template-type-plus-runtime-argument dispatch into a
mutable heap-owned container on the L0 side — NOT a one-to-one named-term rename.

## Status

`firm`. **Justification kind: structural.** The rewrite is shape-driven: the term's two L1 slots map onto two
structurally-distinct L0 carriers (template parameter ↔ differential operator; runtime argument ↔ coefficient),
and the mapping is exhaustively cited at both grounded witness sites. The **term-identity translation lowers
cleanly**; the per-term assembly **kernel** is a named, already-firm sibling obstruction
([`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md),
`opaque-library-ownership`, c055), not a gap in this theme — the split is explicit below. No constructive
sub-part: every claim is read from a positive Palace source site. Firm-on-positive-structure (the
identity-translation is a syntactic correspondence between the pure pair and the template/runtime slots, so the
absence of a dedicated `weak_form_term` unit test does not gate it — same precedent as the firm
[`weak_form_term`](../L1/weak_form_term.md) entry and `fe_assemble`).

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
  integrator's `Assemble` method — is the libCEED-owned opaque map. It is already classified as the
  `opaque-library-ownership` obstruction [`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md)
  (c055), identical across all 5 solver pipelines. It does NOT lower through this theme; this theme stops at the
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

Matching D1's pull-only scoping (the redirect's clean-gate: author a variant's concrete rewrite only when a
pipeline pull NEEDS it):

- **`Identity`/mass** → `MassIntegrator` / `VectorFEMassIntegrator` (`palace/fem/integrator.hpp:68-69,79-80`),
  realizing `a(u, v) = (Q u, v)`. The most-likely next pull (pervasive across eigenmode/driven/transient/ROM
  pipelines), but no concrete `AddDomainIntegrator<...MassIntegrator>` solver-K/M witness is authored here. Its
  L0 instantiation site is filled in under this theme as a specialization note when its own pipeline pull lands.
- **`Divergence`/div-div** → `DivDivIntegrator` (`palace/fem/integrator.hpp:122-123`), realizing
  `a(u, v) = (Q ∇·u, ∇·v)`. **No in-scope solver-K witness**: the wrapper exists but no model-operator K-build
  instantiates it (D1's negative anchor — codemap search over `palace/models/*.cpp` returns no
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

None. This theme lowers an already-firm L1 operator ([`weak_form_term`](../L1/weak_form_term.md), firm c061) into
existing L0 source; it proposes no new L1 vocabulary.

## Verified-against

- `palace/models/laplaceoperator.cpp:188-194` — electrostatic K-build (`LaplaceOperator::GetStiffnessMatrix`,
  method at `:184`); `MaterialPropertyCoefficient epsilon_func(...)` (`:191-192`) +
  `k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func)` (`:194`). citecheck `:188-194 --anchor
  DiffusionIntegrator` → `[ok]` (anchor at 194). Grounds Case 1 (`Gradient`).
- `palace/models/curlcurloperator.cpp:170-181` — magnetostatic K-build
  (`CurlCurlOperator::GetStiffnessMatrix`, method at `:171`); `MaterialPropertyCoefficient muinv_func(...)`
  (`:179-180`) + `k.AddDomainIntegrator<CurlCurlIntegrator>(muinv_func)` (`:181`). citecheck `:170-181 --anchor
  CurlCurlIntegrator` → `[ok]` (anchor at 181). Grounds Case 2 (`Curl`). SAME fold as Case 1, integrator-slot
  difference only.
- `palace/fem/bilinearform.hpp:53-57` — `AddDomainIntegrator<T>(args...)`: the templated append
  (`domain_integs.push_back(std::make_unique<T>(std::forward<U>(args)...))`) — the L0 instantiation surface. The
  template parameter `T` = differential operator; the forwarded argument = coefficient. citecheck `:53-57
  --anchor AddDomainIntegrator` → `[ok]` (anchor at 54).
- `palace/fem/integrator.hpp:39-42` — `BilinearFormIntegrator` base: the `const MaterialPropertyCoefficient *Q`
  coefficient slot, uniform across every differential-operator variant (the factorization ground). citecheck
  `:39-42 --anchor MaterialPropertyCoefficient` → `[ok]` (anchor at 42).
- `palace/fem/integrator.hpp:100-101` — `DiffusionIntegrator` doc comment `a(u,v) = (Q grad u, grad v)` (the
  `Gradient` wrapper); `:111-112` — `CurlCurlIntegrator` `a(u,v) = (Q curl u, curl v)` (the `Curl` wrapper);
  `:68-69`/`:79-80` — `MassIntegrator`/`VectorFEMassIntegrator` (the `Identity` pending-pull wrapper);
  `:122-123` — `DivDivIntegrator` (the `Divergence` pending-pull wrapper).
- `palace/fem/integrator.hpp:197,229,250` — the mixed/rectangular integrators (out-of-scope adjacent family).
- `book/src/L1/weak_form_term.md` (firm c061) — the L1 operator this theme lowers.
- `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` (c055, `opaque-library-ownership`) — the term's
  KERNEL boundary (the identity-lowers/kernel-opaque split's opaque half).
- `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md` (firm c057) — the container build-up / assemble
  protocol; THIS theme is the per-term identity-translation sub-component below that fold.
```

```edit:book/src/L1-L0/index.md
| [fe-assemble-libceed-boundary-obstruction](./fe-assemble-libceed-boundary-obstruction.md) | (boundary annotation on the per-term leaf `A(term_i)` INSIDE the firm `L1/fe_assemble` fold — `fe_assemble` STAYS FIRM, not downgraded) | libCEED-owned leaf: element-local quadrature kernel `integ->Assemble`→`CeedOperator` `bilinearform.cpp:64-70,75` (+ pure-virtual `integrator.hpp:58-61`) + COO numerical materialization `CeedOperatorAssembleCOO` `libceed/operator.cpp:483`; Palace-owned shell: integrator-fold `AddSubOperator` `bilinearform.cpp:77`, PA/FA dispatch `bilinearform.cpp:118-132`, COO→CSR shuffle `libceed/operator.cpp:487-488`, BC-elimination | obstruction *(opaque-library-ownership; deeper-boundary sibling of `triangular-solve-obstruction`; settles the cycle-053 `fe-operator-assemble-mutation-rotation` libCEED-boundary OQ; boundary identical across all 5 solver pipelines)* |
```
```edit-to:book/src/L1-L0/index.md
| [fe-assemble-libceed-boundary-obstruction](./fe-assemble-libceed-boundary-obstruction.md) | (boundary annotation on the per-term leaf `A(term_i)` INSIDE the firm `L1/fe_assemble` fold — `fe_assemble` STAYS FIRM, not downgraded) | libCEED-owned leaf: element-local quadrature kernel `integ->Assemble`→`CeedOperator` `bilinearform.cpp:64-70,75` (+ pure-virtual `integrator.hpp:58-61`) + COO numerical materialization `CeedOperatorAssembleCOO` `libceed/operator.cpp:483`; Palace-owned shell: integrator-fold `AddSubOperator` `bilinearform.cpp:77`, PA/FA dispatch `bilinearform.cpp:118-132`, COO→CSR shuffle `libceed/operator.cpp:487-488`, BC-elimination | obstruction *(opaque-library-ownership; deeper-boundary sibling of `triangular-solve-obstruction`; settles the cycle-053 `fe-operator-assemble-mutation-rotation` libCEED-boundary OQ; boundary identical across all 5 solver pipelines)* |
| [weak-form-term-rotation](./weak-form-term-rotation.md) | [`L1/weak_form_term`](../L1/weak_form_term.md) (firm c061) | `palace/fem/bilinearform.hpp:53-57` (`AddDomainIntegrator<T>(Q)` instantiation), `palace/fem/integrator.hpp:39-130` (wrapper layer), `palace/models/laplaceoperator.cpp:188-194` (Gradient/diffusion witness), `palace/models/curlcurloperator.cpp:170-181` (Curl/curl-curl witness) | firm *(structural; vocabulary-translation — pure `(coefficient, differential-operator)` pair → C++ template-type `T` (diff-op, compile-time) + runtime-arg `Q` (coefficient) dispatch into mutable owned `domain_integs` container; **identity-lowers / kernel-opaque split** — term IDENTITY (which `Q`, which `𝒟`) Palace-readable at the `AddDomainIntegrator<T>(Q)` site and lowers HERE, term KERNEL (`Assemble` quadrature) is the libCEED `opaque-library-ownership` boundary `fe-assemble-libceed-boundary-obstruction` c055, lowers ELSEWHERE; 2 grounded rewrite cases Gradient/`DiffusionIntegrator(epsilon_func)` `laplaceoperator.cpp:191-194` + Curl/`CurlCurlIntegrator(muinv_func)` `curlcurloperator.cpp:179-181` (same `BilinearForm`-fold, integrator-slot-only difference); mass/`Identity` + div-div/`Divergence` named pending-pull axis points NOT authored; container build-up is the sibling `fe-operator-assemble-mutation-rotation` c057; firm-on-positive-structure)* |
```

```edit:book/src/SUMMARY.md
- [fe-assemble-libceed-boundary-obstruction](./L1-L0/fe-assemble-libceed-boundary-obstruction.md)
```
```edit-to:book/src/SUMMARY.md
- [fe-assemble-libceed-boundary-obstruction](./L1-L0/fe-assemble-libceed-boundary-obstruction.md)
- [weak-form-term-rotation](./L1-L0/weak-form-term-rotation.md)
```

## Speculative operators proposed

None. This theme lowers the already-firm L1 operator [`weak_form_term`](../../book/src/L1/weak_form_term.md)
(firm c061) into existing L0 source; it proposes no new L1 vocabulary and creates no rough-in dep-map rows.

## Supporting evidence

- **Grounded witnesses (self-verified via `citecheck --anchor` + `read_range`):**
  - `palace/models/laplaceoperator.cpp:188-194` — `LaplaceOperator::GetStiffnessMatrix` (method at `:184`):
    `epsilon_func` at `:191-192`, `k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func)` at `:194`. citecheck
    `:188-194 --anchor DiffusionIntegrator` → `[ok]` (anchor at 194). Read in full via `read_range :184-196`.
  - `palace/models/curlcurloperator.cpp:170-181` — `CurlCurlOperator::GetStiffnessMatrix` (method at `:171`):
    `muinv_func` at `:179-180`, `k.AddDomainIntegrator<CurlCurlIntegrator>(muinv_func)` at `:181`. citecheck
    `:170-181 --anchor CurlCurlIntegrator` → `[ok]` (anchor at 181). Read in full via `read_range :170-183`.
- **Instantiation surface (self-verified + read in full):** `palace/fem/bilinearform.hpp:53-57` —
  `AddDomainIntegrator<T>(U&&...args)` body is `domain_integs.push_back(std::make_unique<T>(std::forward<U>(args)...))`;
  the sibling `AddBoundaryIntegrator` (term-position axis) at `:59-63`. citecheck `:53-57 --anchor
  AddDomainIntegrator` → `[ok]` (anchor at 54).
- **Wrapper layer (self-verified base-class slot):** `palace/fem/integrator.hpp:39-42` —
  `BilinearFormIntegrator` base, `const MaterialPropertyCoefficient *Q` at `:42` (citecheck `[ok]`, anchor at
  42). Wrapper doc comments `:100-101` (Diffusion), `:111-112` (CurlCurl), `:68-69`/`:79-80`
  (Mass/VectorFEMass), `:122-123` (DivDiv) — all cited by D1's already-self-verified entry.
- **Identity/kernel split sibling:** `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` (c055,
  `opaque-library-ownership`) — the term's KERNEL boundary; this theme covers the term's IDENTITY, which lowers
  cleanly.
- **Container-build-up sibling:** `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md` (firm c057) — the
  `make_unique`/`push_back`/`Assemble` protocol over the term LIST; THIS theme is the per-term identity
  sub-component below that fold.
- **Methodology:** vocabulary-shift redirect (`METHODOLOGY-REDIRECT.md`; CLAUDE.md §Methodology invariants) —
  the lowering is a genuine vocabulary TRANSLATION (pure pair value ↔ template-type + runtime-arg dispatch into a
  mutable container), NOT a degenerate identity-in-named-terms rename. The two slots map onto two
  structurally-distinct L0 carriers (type-system vs. runtime object), which is the non-degeneracy witness.

## Index registration partition (this dispatch)

I am the **sole L1-L0-touching dispatch this cycle** (D2). The `book/src/L1-L0/index.md` is structured as a
single theme-list TABLE + a "Working Notes" tail — it carries **no separate §Vocabulary-cohort section and no
running firm-count tally line**. So the full registration for this index is (1) my theme TABLE row (appended
after the `fe-assemble-libceed-boundary-obstruction` row) — authored above — and there is no separate cohort
bullet or consolidated tally to own here. SUMMARY.md registration of the new theme is mine (placed adjacent to
its FE-assembly siblings) — authored above.

## Open questions / caveats

- **Mass (`Identity`) most-likely next pull, div-div (`Divergence`) possibly never** — matching D1's L1-entry
  scoping. When a pipeline pull NEEDS a mass-term solver-K/M witness, the `Identity` L0 instantiation site is
  filled in under this theme as a specialization note (NOT a new standalone theme — per the redirect's
  combinator-primary discipline and the pull-only clean-gate). Div-div's named-but-unpulled status IS the
  spine-coverage finding if no in-scope pipeline ever needs it; no speculative authoring.
- **Mixed/rectangular pairings are explicitly out of scope** (the square-pairing carve-out, mirroring the L1
  entry). If a future eigenmode/ROM pull needs a `(Q ∇u, v)` mixed-operator term
  (`MixedVectorGradientIntegrator`, `palace/fem/integrator.hpp:197`), that is a DIFFERENT lowering theme on a
  mixed/rectangular axis (the L0 form is still `AddDomainIntegrator<T>(Q)` but with a mixed-pairing `T` over two
  spaces) — flag for a future abstractor dispatch, do not bundle here.
- **Boundary term-position sub-axis** (`AddBoundaryIntegrator<T>(Q)`, `palace/fem/bilinearform.hpp:59-63`) is the
  same identity-translation shape into a different container (`boundary_integs`); the witnessed solver-K terms
  are all `domain`. Noted as adjacent; covered by the same translation when a boundary-term pull lands.

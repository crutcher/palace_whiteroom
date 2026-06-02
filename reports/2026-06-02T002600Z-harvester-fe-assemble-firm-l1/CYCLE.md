---
agent: harvester
invoked_at: 2026-06-02T002600Z
scope: L1 operator: fe_assemble (promote speculative rough-in → firm)
status: integrated
integrated_at: 2026-06-02T011000Z
integration_commit: f3ee795953217dc3423b3601ce60af307ba8afa7
integration_notes: |
  cycle-054 D2, applied clean by integrator-per-report (STAGING row 2), finalized by integrator-finalize.
  Promoted `fe_assemble` to FIRM L1 (new:book/src/L1/fe_assemble.md) — the first firm FE-assembly operator,
  opening the FE sub-spine. The integrator-fold K=Σ_i A(term_i) over opaque per-term A; 4 laws over opaque A;
  3 variant axes (assembly-representation PA/FA, term-position domain/boundary, trial-test-coincidence
  square/rectangular). Slug-collision held distinct from BLAS-2 bilinear-form (xᴴMy reduction). Wired in one
  pass: L1/index FE-cohort bullet rough-in->firm + SUMMARY chapter entry + L1-L0/index dep-map row LHS firm
  live-link with corrected AddSubOperator anchors :71-77/:91-97. Propose-only citation-drift deferral: the
  upstream theme body (fe-operator-assemble-mutation-rotation.md) still cites the +2-drift :73-75/:93-95 —
  routed to a batch-17 lifter (OQ fe-assemble-theme-addsuboperator-citation-drift), NOT edited in-place.
  Deferred operators weak_form_term/eliminate_essential_bc/eliminate_rhs stay rough-in. 7 OQs promoted.
  L1 firm 26->27. Build exit 0; fe_assemble.md renders + index/SUMMARY/L1-L0 wiring resolves. Gate hits: 0.
  Batch-16 final cycle; the batch-16 meta-phase fires next as a separate dispatch.
inputs:
  - book/src/L1-L0/fe-operator-assemble-mutation-rotation.md (rough-in thread-opener; the lowering theme this entry lifts)
  - reports/2026-06-01T235200Z-abstractor-fe-assembly-thread-opener/CYCLE.md (cycle-053 D3 — the thread-opener; BilinearForm-as-fold-over-integrators insight)
  - reference/palace/palace/fem/bilinearform.cpp:28-107 (PartialAssemble — the integrator-fold core)
  - reference/palace/palace/fem/bilinearform.cpp:141-151 (Assemble(bool) — PA/FA dispatch)
  - reference/palace/palace/fem/bilinearform.hpp:25-91 (class BilinearForm — integrator-list container + templated append)
  - reference/palace/palace/models/laplaceoperator.cpp:184-223 (GetStiffnessMatrix — the electrostatic witness)
  - reference/palace/palace/fem/integrator.hpp:39-130 (BilinearFormIntegrator interface + concrete weak-form terms)
  - reference/palace/palace/fem/libceed/operator.cpp:455-490 (CeedOperatorFullAssemble — libCEED boundary)
  - book/src/L1/axpy.md, book/src/L1/apply_linop.md (firm L1 entry conventions)
  - book/src/L1/bilinear-form.md (the slug-collision: BLAS-2 xᴴMy, NOT FE assembly)
---

# CYCLE: Formalize fe_assemble at L1

## Summary

Promotes `fe_assemble` from speculative rough-in (proposed by the cycle-053 D3
`fe-operator-assemble-mutation-rotation` thread-opener) to a **firm L1 operator**. The clean-gate
call is **PROMOTE — clean**: `fe_assemble` is the integrator-fold `K = Σ_i A(term_i)` over an
immutable weak-form-term list, and that fold is **definable treating `weak_form_term` as an opaque
rough-in input** — the fold's structure (list concatenation, sum-of-per-term-operators,
empty-list identity) and its homomorphism/linearity laws are about the LIST and the operator-`+`,
never about the term's `(coefficient, differential-operator)` internals. So defining `fe_assemble`
does NOT require formalizing `weak_form_term` first; the new FE vocabulary stays opaque and the
operator lifts clean. `A(·)` (the element-local→global per-term assembly, libCEED-owned) is
likewise an opaque per-term leaf the fold quantifies over without defining. The witness is
`GetStiffnessMatrix` (`palace/models/laplaceoperator.cpp:184-223`); the fold core is
`BilinearForm::PartialAssemble` (`palace/fem/bilinearform.cpp:28-107`).

**Slug-collision held distinct (load-bearing):** the entry states explicitly that `fe_assemble`
(produces the operator `K` — an assembly *constructor*) is a DIFFERENT object from the existing L1
`bilinear-form` (the BLAS-2 reduction `xᴴMy` — *consumes* an operator, produces a scalar). The two
share only the math phrase "bilinear form."

**Citation-drift correction surfaced (propose-only):** the rough-in theme + the D3 report both cite
the domain/boundary `AddSubOperator` accumulation at `:73-75` / `:93-95`; citecheck `--anchor
AddSubOperator` shows the actual sites are **`:77`** (domain) and **`:97`** (boundary) — a +2 drift.
My firm entry uses the corrected `:71-77` / `:91-97` ranges; I propose the dep-map row correction
and flag the in-theme drift for a lifter pass (I do NOT edit the theme body in place — that is a
DISPATCH-phase change to propose, not apply).

`eliminate_essential_bc` / `eliminate_rhs` / `weak_form_term` stay deferred-rough-in this cycle
(per scope). One operator landed: `fe_assemble`.

## Proposed changes

```new:book/src/L1/fe_assemble.md
---
layer: L1
operator: fe_assemble
firmness: firm
lowers_to:
  - L1-L0/fe-operator-assemble-mutation-rotation
lifts_from: []
depends_on: []
variant_axes:
  - assembly-representation
  - term-position
  - trial-test-coincidence
---

# fe_assemble

Mutation-free finite-element operator assembly: assemble a global linear operator `K` from a
finite-element space and an **immutable list of weak-form terms**, as the fold
`K = Σ_i A(term_i)`. The pure-functional lift of the MFEM-equivalent `BilinearForm` build-up-then-
assemble C++ class — the entry point of the FE-assembly sub-spine (in scope per CLAUDE.md mesh/FE).

## Slug-collision (load-bearing — do NOT conflate)

`fe_assemble` is **not** [`bilinear-form`](./bilinear-form.md). They are different L1 objects that
share only the math phrase "bilinear form":

- `fe_assemble` is an **assembly constructor**: it *produces* a global linear operator `K` from a
  space + term list. The C++ source is the `BilinearForm` *class* (`palace/fem/bilinearform.hpp:25-91`).
- `bilinear-form` is a **scalar reduction** `α = xᴴ M y`: it *consumes* an already-assembled
  operator `M` and two vectors, producing a scalar. The C++ source is `linalg::Dot(comm, x, A, y)`
  (`palace/linalg/operator.cpp:621-639`).

A downstream producer must route FE-assembly work to `fe_assemble`, never to `bilinear-form`.

## Context

`fe_assemble` lifts Palace's `BilinearForm::Assemble` (`palace/fem/bilinearform.cpp:141-151`) to a
single pure-functional operator. The L0 form is an imperative **build-up-then-assemble** object
protocol: construct an empty `BilinearForm` over the trial/test space, push weak-form terms onto an
owned integrator list by templated append (`AddDomainIntegrator<T>` / `AddBoundaryIntegrator<T>`,
`palace/fem/bilinearform.hpp:53-63` — `make_unique<T>` then `push_back` onto `domain_integs` /
`boundary_integs`), then call `Assemble`. The L1 form drops the mutable container: it consumes the
space and the immutable term list and produces a fresh operator value. Container build-up,
sub-operator accumulation, and the finalize step are L0 concerns reintroduced by the
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md)
L1>L0 lowering theme, not by the L1 signature.

The **shared-spine reading is a fold over the term list** (the firm L0 navigation already names
this: `book/src/L0/fem-bilinearform-file.md` §"Notes for higher layers" — "BilinearForm is
fundamentally a fold over integrators"). `BilinearForm::PartialAssemble`
(`palace/fem/bilinearform.cpp:28-107`) iterates the integrator lists and accumulates one
sub-operator per term into a composite operator via `AddSubOperator`
(`palace/fem/bilinearform.cpp:71-77` domain branch; `:91-97` boundary branch), then finalizes
(`:104`). The composite operator's action is the sum of the per-term sub-operator actions — i.e.
`K = Σ_i A(term_i)`.

## Signature

```text
fe_assemble :: (space: FiniteElementSpace[N], terms: [WeakFormTerm]) -> LinearOperator[N, N]
fe_assemble(space, terms) = foldr (\t acc -> A(space, t) + acc) zero terms
                          = Σ_{t ∈ terms} A(space, t)
```

Shape contract (bunsen-style, named axes):

- `space` — `FiniteElementSpace[N]` — the trial/test finite-element space; `N = space.GetTrueVSize()`
  is the global true-dof count (the operator's square dimension). Read-only.
- `terms` — `[WeakFormTerm]` — an immutable, finite list of weak-form contributions. **`WeakFormTerm`
  is an opaque rough-in input here** (see *Dependencies*): `fe_assemble` quantifies over the term
  list without cracking open a term's `(coefficient, differential-operator)` internals.
- result — `LinearOperator[N, N]` — a fresh global linear operator over the space's true-dof axis `N`.

`A(space, ·)` is the **opaque per-term assembly map**: it takes one weak-form term to its
global-dof `LinearOperator[N, N]` contribution (the element-local quadrature kernel + restriction;
libCEED-owned — see *Variant axes* and *Open questions*). `fe_assemble` is defined by the FOLD over
`A`; `A` itself is a leaf the fold quantifies over, not part of `fe_assemble`'s definition. The
two-list (domain + boundary) L0 structure is one logical term list at L1: `terms` is the
concatenation `domain_integs ++ boundary_integs` (the boundary terms assemble on dimension−1
geometry, `palace/fem/bilinearform.cpp:82-84`, but enter the same accumulating sum).

## Semantics

`fe_assemble(space, terms)` is the **fold of the per-term assembly map `A(space, ·)` over the term
list, summed**. The result operator's action on a vector `v` is

```text
fe_assemble(space, terms) · v  =  Σ_{t ∈ terms} (A(space, t) · v)
```

— each weak-form term contributes an independent additive piece to the global operator's action;
there is no cross-term coupling. This is the standard conforming-FE assembly model: the global
operator is the sum of element-local weak-form contributions, with no inter-element coupling beyond
shared-dof assembly (already absorbed inside each `A(space, t)`).

The operator is **pure at L1**: there is no built-up container, no sub-operator accumulator mutated
in place, no `Finalize()` step, no destination buffer. The L0 source constructs a `BilinearForm`,
mutates its integrator lists by `push_back`, and mutates a `ceed::Operator` by `AddSubOperator`;
all three mutations are L0 concerns reintroduced by the L1>L0 lowering theme. At L1 the relationship
is purely the algebraic fold.

The **assembly representation** (matrix-free partial-assembly `ceed::Operator` vs. materialized
sparse `HypreCSRMatrix`) is a variant axis absorbed at L1 (see *Variant axes*): both compute the
same operator *action*; the `pa_order_threshold` dispatch (`UseFullAssembly`,
`palace/fem/bilinearform.cpp:115-138`) is a performance selector, not an algebraic distinction.

## Algebraic laws

`fe_assemble` is a **list-homomorphism (a fold producing a sum)**; the laws below are exactly the
laws of that fold and hold treating `A(space, ·)` and `WeakFormTerm` as opaque. Absences are
deliberate.

1. **Empty-term identity**: `fe_assemble(space, []) = 0`, the zero operator on `LinearOperator[N, N]`.
   The fold over the empty list is the fold's identity element (the zero operator), the additive
   identity for operator addition. (L0 corroboration: `PartialAssemble` with both integrator lists
   empty constructs the composite operator and finalizes it with no sub-operators added —
   `palace/fem/bilinearform.cpp:43-46` empty-thread comment + the guarded `!domain_integs.empty()`
   / `!boundary_integs.empty()` branches at `:61` / `:84-85`; the result is the zero-action operator.)

2. **Concatenation homomorphism (term-list additivity)**:
   `fe_assemble(space, terms₁ ++ terms₂) = fe_assemble(space, terms₁) + fe_assemble(space, terms₂)`.
   Splitting or concatenating the term list distributes over operator addition — both sides equal
   `Σ_{t ∈ terms₁} A(space,t) + Σ_{t ∈ terms₂} A(space,t)`. This is the fold's defining
   homomorphism; it is what makes the domain/boundary two-list L0 structure a single L1 fold
   (`domain_integs` and `boundary_integs` are two sub-lists whose assembled sums add).

3. **Single-term reduction**: `fe_assemble(space, [t]) = A(space, t)`. A one-term assembly is just
   that term's contribution — the witness electrostatic case `fe_assemble(h1_space, [diffusion(ε)])`
   = the permittivity-weighted diffusion operator (`palace/models/laplaceoperator.cpp:191-192`).

4. **Term-position commutativity (order independence)**: `fe_assemble(space, terms)` is invariant
   under any permutation of `terms`, because operator addition is commutative and associative —
   `Σ` does not depend on summation order. The L0 `push_back` order of `AddDomainIntegrator` calls,
   and the domain-then-boundary loop order in `PartialAssemble`, are therefore algebraically
   immaterial. (Caveat: floating-point non-associativity of the accumulated numeric matrix entries
   is an L0 representation concern, not an L1 algebraic distinction — the *operator* is
   order-independent; see *Variant axes* on the assembly-representation axis.)

Laws that explicitly **do not** hold:

- **No identity / non-degeneracy guarantee on a single term**: `A(space, t)` need not be invertible,
  SPD, or nonzero (a term may assemble a singular contribution; e.g. a pure diffusion operator is
  singular before BC-elimination — the constant null-space). `fe_assemble` carries no SPD/Hermitian
  precondition.
- **BC-elimination is NOT part of the fold**: pinning essential (Dirichlet) dofs
  (`eliminate_essential_bc`, L0 `ParOperator::SetEssentialTrueDofs`,
  `palace/models/laplaceoperator.cpp:215-217`) and lifting inhomogeneous Dirichlet data into the RHS
  (`eliminate_rhs`, L0 `ParOperator::EliminateRHS`, `palace/linalg/rap.cpp:56-82`) are **separable
  post-compositions** on the assembled operator, valid independently of how it was assembled. They
  are sibling speculative-rough-in operators (deferred), not laws of `fe_assemble`.

## Dependencies

`fe_assemble` is a **fold leaf at L1** with respect to the spine: the fold structure (list
concatenation, sum-of-operators, empty identity) uses no other firm L1 operator. It quantifies over
two rough-in inputs it does NOT define:

- `WeakFormTerm` (type) — opaque rough-in input; the `(coefficient, differential-operator)` pair
  that is the element type of the term list. This is the genuinely-NEW FE vocabulary the sub-spine
  introduces; the witnessed differential-operator cohort so far is ∇ (diffusion), identity (mass),
  curl (curl-curl), div (div-div) (`palace/fem/integrator.hpp:39-130`). **`fe_assemble` does not
  crack open the term** — it folds over the list opaquely — so the type's formalization is deferred
  without gating this entry (the clean-gate call, see §Status). The term-cohort enumeration is
  follow-on work tracked at the
  [`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md)
  theme.
- `A(space, ·)` — the opaque per-term element-local→global assembly map (libCEED restriction +
  basis-apply + quadrature contraction). Cited at the Palace call boundary
  (`integ->Assemble(...)` building one `CeedOperator` sub-operator,
  `palace/fem/bilinearform.cpp:67-70` / `:87-90`); the kernel body is upstream-owned (libCEED). Its
  classification (transitive-firm leaf vs. opaque-library-ownership vs. tensor-contraction respine)
  is an open question — see *Open questions*. `fe_assemble`'s definition is independent of that
  classification: the fold quantifies over `A` either way.

## Variant axes

- **assembly-representation**: `partial` (matrix-free `ceed::Operator`) | `full` (materialized
  `hypre::HypreCSRMatrix`). The L0 dispatch `BilinearForm::Assemble`
  (`palace/fem/bilinearform.cpp:141-151`) selects by polynomial order via `UseFullAssembly`
  (`palace/fem/bilinearform.cpp:115-138`). Both compute the same operator *action*; the L1 form is
  representation-agnostic. This is the PA/FA dual that collapses at L1
  (`book/src/L0/fem-bilinearform-file.md` §"The PA/FA dual collapses at L1").
- **term-position**: `domain` (volume integrators, full-dimension geometry,
  `palace/fem/bilinearform.cpp:61-80`) | `boundary` (surface integrators, dimension−1 geometry,
  `palace/fem/bilinearform.cpp:84-103`). At L1 both are entries of the same concatenated term list
  (per law 2); the L0 two-list split is variant absorption.
- **trial-test-coincidence**: `square` (trial = test space — the `SymmetricOperator` construction,
  `palace/fem/bilinearform.cpp:37-40`, and the single-space ctor `BilinearForm(fespace)`,
  `palace/fem/bilinearform.hpp:48`) | `rectangular` (distinct trial/test — the general
  `ceed::Operator` construction, `palace/fem/bilinearform.cpp:42-46`). The witnessed Palace case is
  square; the signature above is written for the square case (`space` is one parameter). The
  rectangular generalization `fe_assemble(trial_space, test_space, terms)` is a sub-axis the
  signature can carry; not exercised by the electrostatic witness.

## Status

`firm`. **Clean-gate call: PROMOTE — clean.** The promotion is justified because the operator's
definition, signature, and all four algebraic laws are stated entirely in **existing shared
vocabulary** (fold / sum-of-operators / list-homomorphism) over the term list, treating
`WeakFormTerm` and `A(space, ·)` as **opaque inputs**. Concretely, the clean-gate test from the
dispatch scope is met:

> Can `fe_assemble` be cleanly defined treating `weak_form_term` as an opaque rough-in input (the
> fold doesn't need to crack open the term to be defined)?

**Yes.** The fold's structure and its homomorphism/identity/commutativity laws are about the LIST
and the operator-`+`; they never inspect a term's `(coefficient, differential-operator)` internals.
Defining `fe_assemble` therefore does NOT require formalizing `weak_form_term` first. The
genuinely-new FE vocabulary (`weak_form_term`, the differential-operator cohort) stays a deferred
rough-in input, and the per-term assembly map `A` stays an opaque leaf pending the libCEED-boundary
classification — neither gates this entry.

The structural signature is uncontested at L0 (the integrator-fold is independently named by the
firm L0 navigation `book/src/L0/fem-bilinearform-file.md`), and the four laws are standard
list-fold / operator-sum facts that hold syntactically over the opaque `A`. This is the
**firm-on-positive-structure** situation (the `apply_linop` / BLAS-1-leaf precedent): the laws are
identities on a fully-specified positive fold structure, so the absence of a dedicated
`fe_assemble` unit test does not gate them. (The libCEED full-assemble materialization IS
test-covered — `test/unit/test-libceed.cpp` `TestCeedOperatorFullAssemble` asserts the assembled
matrix matches an MFEM reference to 1e-12 — useful as future `empirical-match` evidence for `A`'s
faithfulness, but not needed for `fe_assemble`'s fold laws.)

## L1 vs L0 distinction

- **L0**: imperative build-up-then-assemble object protocol. Construct `BilinearForm k(space)`,
  mutate its integrator lists by `k.AddDomainIntegrator<T>(...)` (`push_back`), call
  `k.Assemble(...)` which dispatches PA/FA and folds the lists into a composite `ceed::Operator` by
  `AddSubOperator` (mutating accumulation), then `Finalize()`. State is threaded through the mutable
  `BilinearForm` object and the mutable composite operator.
- **L1**: pure functional fold. `K = fe_assemble(space, terms)`. No mutable container, no
  accumulator, no finalize. The operator value is the sum `Σ_i A(space, term_i)`. The algebraic laws
  apply directly. The L0 object mutation, the two-list domain/boundary split, the PA/FA dispatch,
  and the OMP-parallel composite build (`palace/fem/bilinearform.cpp:50-105` — one `Ceed` per
  thread) are all L1>L0 lowering concerns.

## Evidence

- `palace/fem/bilinearform.cpp:28-107` — `BilinearForm::PartialAssemble`: the integrator-fold core.
  Iterates `domain_integs` / `boundary_integs` over mesh geometry, builds one `CeedOperator`
  sub-operator per integrator (`integ->Assemble(...)`, `:67-70` domain / `:87-90` boundary), and
  accumulates each into the composite via `op->AddSubOperator(sub_op)` (**`:77`** domain branch /
  **`:97`** boundary branch), then `op->Finalize()` (`:104`). The composite-operator action = the
  sum of sub-operator actions = `Σ_i A(term_i)`.
- `palace/fem/bilinearform.cpp:141-151` — `BilinearForm::Assemble(bool)`: the PA/FA policy dispatch
  (`UseFullAssembly` → `FullAssemble` else `PartialAssemble`) — the assembly-representation variant
  axis.
- `palace/fem/bilinearform.cpp:115-138` — `UseFullAssembly`: the polynomial-order threshold
  selecting PA vs. FA (performance selector, not algebraic).
- `palace/fem/bilinearform.hpp:25-91` — `class BilinearForm`: the dual integrator-list container
  (`domain_integs, boundary_integs`, `:32`) + the templated `AddDomainIntegrator` /
  `AddBoundaryIntegrator` append surface (`:53-63`) + the single-space ctor delegating trial = test
  (`:48`).
- `palace/models/laplaceoperator.cpp:184-223` — `LaplaceOperator::GetStiffnessMatrix`: the
  electrostatic witness. `BilinearForm k(GetH1Space())` (`:191`) +
  `k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func)` (`:192`) + `k.Assemble(...)` (`:194`) —
  the single-term assembly `fe_assemble(h1_space, [diffusion(ε)])` — then per-level `ParOperator`
  wrap with `SetEssentialTrueDofs` (`:215-217`, the separable `eliminate_essential_bc` post-comp).
- `palace/fem/integrator.hpp:39-130` — `BilinearFormIntegrator` interface + concrete weak-form
  terms (`MassIntegrator`, `DiffusionIntegrator`, `CurlCurlIntegrator`, `DivDivIntegrator`, ...) —
  the `WeakFormTerm` cohort (opaque rough-in input here).
- `palace/fem/libceed/operator.cpp:455-490` — `CeedOperatorFullAssemble`: the COO→CSR
  materialization of the composite operator (the libCEED boundary; the realization of `A`'s
  matrix form for the `full` representation variant).
- `book/src/L0/fem-bilinearform-file.md` — firm L0 navigation: independently names the
  integrator-fold insight ("BilinearForm is fundamentally a fold over integrators") + the
  PA/FA-collapses-at-L1 absorption.
- `book/src/L1/bilinear-form.md` — the slug-collision source (BLAS-2 `xᴴMy`, a DIFFERENT object).
- `test/unit/test-libceed.cpp` — `TestCeedOperatorFullAssemble` (L0-equivalent: assembled matrix
  matches MFEM reference to 1e-12; future `empirical-match` evidence for `A`'s faithfulness).

## Downward to L0

The lowering is the
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md)
L1>L0 theme (currently `rough-in` thread-opener). With `fe_assemble` now firm, the theme's LHS is
no longer a speculative placeholder; it should be re-anchored to this firm operator (flagged for a
lifter pass — see *Open questions*). The theme narrates how this L1 fold lowers into Palace's
build-up-then-assemble object protocol (construct container → `push_back` integrators → fold via
`AddSubOperator` → finalize → PA/FA dispatch → libCEED materialization), plus the separable
BC-elimination post-compositions.
```

```edit:book/src/L1/index.md
**Rough-in (FE-assembly sub-spine — THREAD-OPENER cycle-053)** — speculative L1 operators opening the finite-element assembly surface (the MFEM-equivalent assembly sub-spine, in scope per CLAUDE.md mesh/FE). Proposed by the [`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) L1>L0 thread-opener; await harvester promotion + integrator-term-cohort enumeration:

- **`fe_assemble` is now FIRM** (cycle-054) — see [`fe_assemble`](./fe_assemble.md). Assemble a global FE operator from a space + immutable weak-form term list as the integrator-fold `K = Σ_i A(term_i)`; clean-gate PROMOTE (the fold is definable treating `weak_form_term` as an opaque rough-in input — it does not crack open the term). **Slug-collision note**: NOT the existing [`bilinear-form`](./bilinear-form.md) (the BLAS-2 reduction `xᴴ M y`); `fe_assemble` is the C++ `BilinearForm`-*class* assembler. Laws: empty-term identity, concatenation-homomorphism, single-term reduction, term-position commutativity. The `weak_form_term` type + the per-term assembly map `A(·)` (libCEED boundary) stay deferred-rough-in inputs the fold quantifies over.
- `eliminate_essential_bc` *(rough-in; no anchor yet)* — pin essential (Dirichlet) dofs into the assembled operator (L0: `ParOperator::SetEssentialTrueDofs`, `palace/models/laplaceoperator.cpp:215-217`) (proposed-by: abstractor:2026-06-01T235200Z-abstractor-fe-assembly-thread-opener).
- `eliminate_rhs` *(rough-in; no anchor yet)* — lift inhomogeneous Dirichlet data into the RHS (L0: `ParOperator::EliminateRHS`, `palace/linalg/rap.cpp:56-82`) (proposed-by: abstractor:2026-06-01T235200Z-abstractor-fe-assembly-thread-opener).
```

```edit:book/src/SUMMARY.md
- [bilinear-form](./L1/bilinear-form.md)
- [fe_assemble](./L1/fe_assemble.md)
```

```edit:book/src/L1-L0/index.md
| fe-operator-assemble-mutation-rotation *(rough-in; THREAD-OPENER cycle-053)* | [`L1/fe_assemble`](../L1/fe_assemble.md) *(FIRM — cycle-054)* | `palace/fem/bilinearform.{hpp,cpp}`, `palace/fem/libceed/operator.cpp`, `palace/models/laplaceoperator.cpp:184-253`, `palace/linalg/rap.cpp:56-82` | rough-in *(structural; LHS now firm `fe_assemble` — integrator-fold `K=Σ_i A(term_i)` + PA/FA variant axis + separable BC-elimination (`eliminate_essential_bc`/`eliminate_rhs`); slug-collision noted — distinct from BLAS-2 `bilinear-form` `xᴴMy`; `AddSubOperator` accumulation at `bilinearform.cpp:77`/`:97` (theme body cites `:73-75`/`:93-95` — +2 drift, flagged for lifter re-anchor); libCEED matrix-materialization boundary logged OQ (transitive-firm vs opaque-library-ownership vs tensor-contraction-respine); theme RE-ANCHORABLE to firm LHS — lifter pass)* |
```

## Operator content

(The firm `fe_assemble` chapter body is authored in full inside the `new:book/src/L1/fe_assemble.md`
proposed-changes block above — Slug-collision, Context, Signature, Semantics, Algebraic-laws,
Dependencies, Variant-axes, Status (clean-gate record), L1-vs-L0, Evidence, Downward-to-L0.)

Key load-bearing pieces:

- **Signature**: `fe_assemble :: (space: FiniteElementSpace[N], terms: [WeakFormTerm]) -> LinearOperator[N, N]`,
  defined as the fold `Σ_{t ∈ terms} A(space, t)`.
- **Clean-gate record** (`## Status`): PROMOTE — clean. The fold is definable with `WeakFormTerm`
  and `A(space, ·)` opaque; the new FE vocabulary is a deferred input, not a prerequisite.
- **Four laws** (all hold over opaque `A`): (1) empty-term identity → zero operator;
  (2) concatenation-homomorphism (term-list additivity); (3) single-term reduction;
  (4) term-position commutativity. Explicit non-laws: no single-term invertibility/SPD guarantee;
  BC-elimination is separable post-composition, not part of the fold.

## Supporting evidence

All citations self-verified against on-disk source via `tools/citecheck/citecheck.py --anchor`:

- `palace/fem/bilinearform.cpp:28-107` `--anchor PartialAssemble` → ok (anchor line 28).
- `palace/fem/bilinearform.cpp:141-151` `--anchor "BilinearForm::Assemble(bool"` → ok (line 141).
- `palace/fem/bilinearform.hpp:53-63` `--anchor AddDomainIntegrator` → ok (line 54).
- `palace/fem/integrator.hpp:39-130` `--anchor BilinearFormIntegrator` → ok (14 sites).
- `palace/models/laplaceoperator.cpp:184-223` `--anchor GetStiffnessMatrix` → ok (line 184).
- `palace/models/laplaceoperator.cpp:215-217` `--anchor SetEssentialTrueDofs` → ok (line 217).
- `palace/fem/bilinearform.cpp:71-77` `--anchor AddSubOperator` → ok (line **77**, domain).
- `palace/fem/bilinearform.cpp:91-97` `--anchor AddSubOperator` → ok (line **97**, boundary).
- `palace/fem/bilinearform.cpp:104` `--anchor Finalize` → ok (line 104).

**Citation-drift found (propose-only correction):** the rough-in theme body
(`book/src/L1-L0/fe-operator-assemble-mutation-rotation.md:84`) and the D3 report cite the
`AddSubOperator` accumulation at `:73-75` (domain) / `:93-95` (boundary). citecheck `--anchor
AddSubOperator` confirms the actual sites are `:77` and `:97` — a **+2 drift**. My firm entry uses
the corrected `:71-77` / `:91-97` ranges. I propose the corrected anchor in the L1-L0 dep-map row
(above) and flag the in-theme-body drift for a lifter pass; per the DISPATCH-phase write partition I
do **not** edit the theme body in place.

Source reads confirming the structure (read this dispatch, not from memory):
- `palace/fem/bilinearform.cpp:28-107` — `PartialAssemble` reads as a fold over `domain_integs` +
  `boundary_integs` accumulating `AddSubOperator` then `Finalize()`. The composite is a
  `SymmetricOperator` when trial == test (`:37-40`), general `ceed::Operator` otherwise (`:42-46`).
- `palace/fem/bilinearform.hpp:25-91` — dual integrator-list members (`:32`); templated append
  (`:53-63`); single-space ctor delegating trial = test (`:48`).
- `palace/models/laplaceoperator.cpp:184-223` — the witness; note the per-level wrap is
  `ParOperator` inside a `MultigridOperator` (`:198`, `:213-216`) — the multigrid-hierarchy assembly
  is a sibling concern (multilevel `Assemble(hierarchy)` overload, `bilinearform.cpp:155-160`), not
  part of single-operator `fe_assemble`; noted as OQ.

## Open questions / caveats

1. **`fe-assemble-theme-reanchor-to-firm-lhs`** (FOR LIFTER) — the
   `fe-operator-assemble-mutation-rotation` L1>L0 theme is still `rough-in` with LHS = "speculative
   rough-in `fe_assemble`". With `fe_assemble` now firm, the theme's LHS placeholder language
   (frontmatter `lowers: L1/fe_assemble (speculative rough-in)`; §"Speculative L1 operators"
   listing `fe_assemble`) should be re-anchored to the firm operator. This is a lifter pass (re-anchor
   to firmed-up vocabulary), not authored here. The dep-map row (proposed above) already marks the
   LHS firm + flags the re-anchor.

2. **`fe-assemble-theme-addsuboperator-citation-drift`** (FOR LIFTER/REPAIRER) — the theme body
   (`:84`) and D3 report cite `AddSubOperator` at `:73-75`/`:93-95`; the verified sites are
   `:77`/`:97` (+2 drift). My firm entry + proposed dep-map row use the corrected ranges; the theme
   body correction is a propose-only flag (DISPATCH-phase write partition).

3. **`fe-assemble-libceed-boundary-classification`** (carried from D3 — FOR BATCH-16 META / lowering-
   verifier) — the per-term assembly map `A(space, ·)` bottoms out in libCEED (element-local
   quadrature kernel + restriction; `integ->Assemble` building a `CeedOperator`,
   `palace/fem/bilinearform.cpp:67-70`; COO→CSR via `CeedOperatorFullAssemble`,
   `palace/fem/libceed/operator.cpp:455-490`). Three routes: transitive-firm leaf at the Palace
   boundary / `obstruction (opaque-library-ownership)` / tensor-contraction respine. `fe_assemble`'s
   firm status is **independent** of this classification (the fold quantifies over `A` opaquely) —
   but the classification gates how deep the FE thread goes and whether `A` ever gets its own L1
   entry. Distinct from the HYPRE/SLEPc opaque-library precedents because Palace DOES own the
   orchestration (the fold, the PA/FA dispatch, the term lists); only the innermost quadrature kernel
   is library-owned.

4. **`fe-assemble-weak-form-term-cohort-enumeration`** (deferred rough-in — per scope) — the
   `weak_form_term` type (the genuinely-new FE vocabulary; `(coefficient, differential-operator)`
   cohort ∇/identity/curl/div, `palace/fem/integrator.hpp:39-130`) stays an opaque rough-in input.
   `fe_assemble` lands firm without it (clean-gate). Enumerating the differential-operator cohort
   across the 5 solver pipelines is follow-on work; defer until a solver needs more than the
   electrostatic diffusion term.

5. **`fe-assemble-bc-elimination-siblings-deferred`** (per scope) — `eliminate_essential_bc`
   (L0 `SetEssentialTrueDofs`, `laplaceoperator.cpp:215-217`) and `eliminate_rhs` (L0
   `ParOperator::EliminateRHS`, `rap.cpp:56-82`) stay deferred-rough-in this cycle. They are
   separable post-compositions (NOT part of the `fe_assemble` fold); `eliminate_rhs`'s body is an
   `apply_linop` + `axpy` composition (firm spine vocabulary) per D3, so both should promote cleanly
   in a follow-on harvester pass.

6. **`fe-assemble-rectangular-and-multilevel-axes`** (note) — the firm entry's signature is the
   square (trial = test) single-operator case witnessed by the electrostatic probe. Two
   generalizations are noted but not exercised: (a) the rectangular `fe_assemble(trial, test, terms)`
   case (the general `ceed::Operator` construction, `bilinearform.cpp:42-46`; the
   `DiscreteLinearOperator` interpolation sibling D3 OQ-5); (b) the multigrid-hierarchy assembly
   `Assemble(FiniteElementSpaceHierarchy, ...)` overload (`bilinearform.cpp:155-160`) that produces a
   per-level operator vector. Both are sibling sub-threads, not part of this entry.

7. **`fe-assemble-l1-index-cohort-header-stale`** (FOR layer-intro-author / integrator note) — the
   L1 index FE-cohort subsection header still reads "**Rough-in (FE-assembly sub-spine ...)**". With
   `fe_assemble` firm, the subsection now mixes one firm + two rough-in bullets. I updated the
   `fe_assemble` bullet to firm in place (my own cohort bullet, per the index-registration
   partition); the subsection *header* rewording (e.g. "FE-assembly sub-spine — 1 firm, 2 rough-in")
   is a layer-intro-author concern, flagged not edited (not my partition).

**MPI / Par* (single-rank):** the per-level wrap is `ParOperator` (`laplaceoperator.cpp:215`), read
single-rank per `book/src/L0/par-types-single-rank-reading.md`; the OMP-parallel composite build
(`bilinearform.cpp:50-105`, one `Ceed` per thread) is a transparent CPU-threading trick that
collapses at L1; the MPI `GlobalSum` over NNZ (`laplaceoperator.cpp:209`) is diagnostic-only. None
affect the L1 fold semantics.

**Index-registration partition:** I authored (1) my L1-L0 dep-map row update + (2) my own L1-index
FE-cohort firm bullet (the `fe_assemble` sub-list entry) + the SUMMARY registration. There is no
consolidated running-count tally at the L1 index FE-cohort subsection (it is a prose cohort list,
not a firm/partial-obstruction count), so no tally to defer. No co-dispatched count-owner named for
this section.

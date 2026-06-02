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
  `palace/models/laplaceoperator.cpp:216-217`) and lifting inhomogeneous Dirichlet data into the RHS
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
  wrap with `SetEssentialTrueDofs` (`:216-217`, the separable `eliminate_essential_bc` post-comp).
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

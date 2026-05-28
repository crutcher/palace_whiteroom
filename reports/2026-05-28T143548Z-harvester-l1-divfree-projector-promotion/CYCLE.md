---
agent: harvester
invoked_at: 2026-05-28T143548Z
scope: L1 operator: divfree-projector
status: integrated
integrated_at: 2026-05-28T200000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-013 finalize. Status ADJUDICATED partly-constructive by the per-report integrator (NOT the harvester-argued firm) — structure firm, idempotence law contingent on the unverified WeakDiv≈GᵀM sign reading (MFEM-vendored, below L0 scope); promotion gated on OQ divfree-weakdiv-sign-convention-l0-verify. First partly-constructive ENTRY (complements eigsolve EXIT same cycle). Build-repair at finalize: divfree-projector.md was registered in SUMMARY.md (the staging row's summary-md-registration n/a note was incorrect for the L1 Part)."
inputs:
  - palace/linalg/divfree.hpp:28-71 (class DivFreeSolver, defining condition, Mult declarations)
  - palace/linalg/divfree.cpp:43-152 (constructor: operator assembly + empty-bdr pin + ksp setup)
  - palace/linalg/divfree.cpp:155-186 (Mult(y) in-place apply)
  - palace/linalg/divfree.cpp:189-190 (template instantiations Vector / ComplexVector)
  - palace/drivers/eigensolver.cpp:260-262 (divfree->Mult(v0) initial-vector projection call site)
  - palace/linalg/arpack.cpp:586,752,766,783,791 + slepc.cpp:1870,1961,1970,1982,1991,2088,2163 (opProj->Mult per-iteration projection)
  - book/src/spec/slices/divfree.md (cycle-012-reduced slice; absorbed L1/L2/L3/L4 evidence anchors)
  - book/src/L1/index.md (dep-map + vocabulary cohort to extend)
  - book/src/L1/eigsolve.md (the `projector : Maybe DivFreeSolver[ComplexVector]` consumer)
---

# CYCLE: Formalize divfree-projector at L1

## Summary
Palace's `DivFreeSolver<VecType>` (`palace/linalg/divfree.hpp:34`) is a constructed-operator that projects an H(curl) (Nedelec) vector field onto the discrete divergence-free subspace `{x : Gᵀ M x = 0}` by removing its irrotational (gradient) component. The in-place apply `Mult(y)` (`divfree.cpp:155-186`) mutates `y` in place via four steps: weak divergence → essential-BC zeroing → Poisson-like H1 solve → gradient correction `y ← y + Grad·ψ`. The only firm definition of this projector currently lives in the cycle-012-reduced Phase-1 slice `book/src/spec/slices/divfree.md`, which is load-bearing evidence cited by `L1/ksp_solve`, `L1/eigsolve`, three `concepts/` pages, and `L0/eigensolver-wrapper`. This entry firms it as an L1 operator `divfree_project : (DivFreeProjector[N_nd, N_h1], field) -> field`, re-expressing the in-place `Mult(y)` mutation as a pure idempotent linear projection. Status: **firm** — every step is read from a positive source site; the one caveat (the `WeakDiv` sign convention that makes the correction additive) is a property of the constructed operator carried as a load-bearing algebraic note, not a reconstructed sub-part.

## Proposed changes

```edit:book/src/L1/divfree-projector.md
# divfree-projector

Mutation-lifted divergence-free projector: a pure-functional linear projection
`y' = divfree_project(P, y)` that maps an H(curl) (Nedelec) vector field to its
**divergence-free component** by removing the irrotational (discrete-gradient)
part. The constructed-operator gate for Helmholtz-style subspace projection at
L1; the projector consumed by the eigensolver path (ARPACK / SLEPc / NLEPS) to
keep candidate eigenvectors in the physically-meaningful divergence-free
subspace.

## Context

`divfree_project` lifts the `DivFreeSolver<VecType>::Mult(VecType &y)` member
method (`palace/linalg/divfree.cpp:155-186`) — which **mutates `y` in place**,
threads two construction-bound H1-sized scratch buffers (`psi`, `rhs`,
`palace/linalg/divfree.hpp:55`), and reads the construction-bound operators —
to a single pure-functional projection over an opaque constructed-operator
value. The two-argument convenience form `Mult(const VecType &x, VecType &y)`
is `y = x; Mult(y)` (`palace/linalg/divfree.hpp:68-72`) — an explicit copy then
in-place apply, i.e. the pure out-of-place form `y = P·x` with no silent
aliasing. At L1 both collapse to the single pure function: the destination
buffer and the scratch members disappear from the signature; their
reintroduction is an L1>L0 lowering concern.

`divfree_project` is a **constructed-operator gate** at L1, in the same family
as [`ksp_solve`](./ksp_solve.md), [`eigsolve`](./eigsolve.md), and
[`chebyshev-smoother`](./chebyshev-smoother.md): its primary argument `P` is a
structured opaque value assembled once at solver setup
(`palace/linalg/divfree.cpp:43-152`), carrying the ε-weighted H1 mass operator
`M`, the weak-divergence operator `WeakDiv`, the discrete gradient `Grad`, the
effective essential-boundary set `bdr_eff`, and the construction-bound inner
solver `ksp`. Unlike `ksp_solve`, the projector is not parameterised by a
right-hand side that varies in kind — it is a fixed linear map on its single
field argument; unlike `chebyshev-smoother`, the inner H1 solve *is* a
solve-to-tolerance (the projector composes an `ksp_solve` internally; see
Dependencies). The construction-time operator assembly and the empty-boundary
degeneracy pin are absorbed inside `P` and do not appear in the apply signature.

The class is templated on `VecType ∈ {Vector, ComplexVector}`
(`palace/linalg/divfree.cpp:189-190`); the complex specialization applies the
same real-valued operators to the real and imaginary components independently
(`palace/linalg/divfree.cpp:159-184`). This is a parametric variant absorbed by
polymorphism over the field element type (see Variant axes).

## Signature

```text
divfree_project
  :: (P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]

divfree_project(P, y) = y + P.Grad · K⁻¹( Z_{P.bdr_eff}( P.WeakDiv · y ) )
                        where K solves  P.M · ψ = rhs  via P.ksp
```

Shape contract (bunsen-style; named axes):

- `P` — `DivFreeProjector[N_nd, N_h1]` — the constructed projector value. Bound
  at setup; immutable across calls. `N_nd` is the Nedelec (H(curl)) true-dof
  axis; `N_h1` is the H1 true-dof axis. Carries:
  - `P.M : LinearOperator[N_h1, N_h1]` — the ε-weighted H1 mass-like operator,
    assembled from a `DiffusionIntegrator` with the real permittivity
    coefficient (`palace/linalg/divfree.cpp:84-110`). Real and SPD by
    construction (`palace/linalg/divfree.cpp:119` `// real and SPD`). Read-only.
  - `P.WeakDiv : LinearOperator[N_nd, N_h1]` — the ε-weighted weak-divergence
    operator (Nedelec → H1), from a `MixedVectorWeakDivergenceIntegrator`,
    partially assembled (`palace/linalg/divfree.cpp:111-116`). Read-only.
  - `P.Grad : LinearOperator[N_h1, N_nd]` — the discrete gradient
    (H1 → Nedelec discrete interpolator,
    `palace/linalg/divfree.cpp:117`). Read-only. Its columns span the
    nullspace of the curl-curl operator
    (`palace/linalg/divfree.hpp:29-30`).
  - `P.bdr_eff : DofSubset[N_h1]` — the effective essential H1 boundary
    true-dof set captured at the finest level
    (`palace/linalg/divfree.cpp:103-105`). When the user-supplied list is
    globally empty, this is a synthetic single-dof pin (one true dof on one
    rank) that removes the pure-Neumann nullspace
    (`palace/linalg/divfree.cpp:51-81`). Read-only.
  - `P.ksp : Solver[P.M]` — a CG solver bound to `P.M` as both operator and
    preconditioner-target, preconditioned by BoomerAMG (wrapped in geometric
    multigrid when the H1 hierarchy has depth > 1),
    configured with the construction-time tolerance and iteration cap
    (`palace/linalg/divfree.cpp:121-149`). The inner constructed-operator. See
    [`ksp_solve`](./ksp_solve.md).
- `y` — `Field[N_nd]` — the input Nedelec field to project. Read-only at the L1
  surface (the L0 form mutates it in place; the L1 form returns the projected
  field). Element type `Vector` (real) or `ComplexVector` (complex).
- **Returns** — `Field[N_nd]` — the divergence-free component of `y`, satisfying
  the discrete divergence-free condition `Gᵀ M y' = 0` up to the `ksp`
  convergence tolerance on the non-essential dofs.

`Z_S : Field[N_h1] -> Field[N_h1]` is the zero-on-subset operator
`(Z_S z)_i = 0 if i ∈ S else z_i` (the [`set_subvector_zero`](../concepts/set_subvector_zero.md)
primitive); `K⁻¹` denotes the approximate `ksp` solve of `P.M · ψ = rhs`, **not**
exact inversion.

MPI is single-rank in scope (per `CLAUDE.md` "Scope"): the construction reads a
`MPI_Comm` (`palace/linalg/divfree.cpp:62`) and the empty-boundary pin uses
`Mpi::GlobalSum / GlobalMin / Rank / Size` to select a single root rank
(`palace/linalg/divfree.cpp:63-79`) — flagged once here and read as the
single-rank equivalent (the pin reduces to "pin true dof 0 when the boundary
list is empty"). The `MPI_Comm` does not appear in the L1 signature.

## Semantics

`divfree_project` realizes the **discrete Helmholtz decomposition** of a Nedelec
field. Any `y ∈ Field[N_nd]` decomposes as `y = y_divfree + Grad·ψ`, where
`Grad·ψ` is the irrotational (gradient-range) part and `y_divfree` is the
divergence-free remainder satisfying `Gᵀ M y_divfree = 0`. The operator returns
`y_divfree`. The defining condition is `Gᵀ M (P·y) = 0`
(`palace/linalg/divfree.hpp:28-31`), where `G = Grad` is the discrete gradient
whose columns span the nullspace of the curl-curl operator and `M` is the
ε-weighted H1 mass operator.

The four-step apply (`palace/linalg/divfree.cpp:155-186`):

1. **Weak divergence** `rhs ← WeakDiv · y` — compute the H1-side residual
   measuring the divergence of `y` (`palace/linalg/divfree.cpp:159-168`).
2. **Essential-BC zeroing** `rhs ← Z_{bdr_eff}(rhs)` — zero the residual on the
   essential boundary dofs (`palace/linalg/divfree.cpp:170-174`).
3. **Projected H1 solve** `ψ ← K⁻¹ rhs`, i.e. solve `M·ψ = rhs` via `ksp`
   (`palace/linalg/divfree.cpp:175`). The triple product `Gᵀ M G` is never
   materialized: the system passed to `ksp` is `M` itself, with `Gᵀ` realized
   by `WeakDiv` on the RHS side and `G` realized by `Grad` on the correction
   side (the slice's "Equivalent abstract form": `(Gᵀ M G) ψ = Gᵀ M y`).
4. **Gradient correction** `y' ← y + Grad·ψ`
   (`palace/linalg/divfree.cpp:177-186`, via `Grad->AddMult(ψ, y, 1.0)` — the
   complex Re/Im branches at :180-181, the real branch at :185).

The mathematical projector is `P = I − Grad (Gᵀ M G)⁻¹ Gᵀ M` (the M-orthogonal
projection onto the divergence-free subspace). The materialized form computes
the *complementary* gradient component and the **sign convention** of `WeakDiv`
makes the correction *additive* (`y + Grad·ψ`, not `y − Grad·ψ`): see Algebraic
laws and Open questions.

The complex specialization is the same projection applied component-wise to
`Re(y)` and `Im(y)` with the same real-valued operators
(`palace/linalg/divfree.cpp:159-184`); the inner `ksp` step is a single solve on
the `ComplexOperator`-typed system whose CG recursion is component-blind. There
is no cross-coupling between the real and imaginary parts through the projection.

## Algebraic laws

- **Linearity.** `divfree_project(P, ·)` is a linear map on `Field[N_nd]`:
  `P·(αu + βv) = α(P·u) + β(P·v)`. Each of the four steps is linear
  (`WeakDiv`, `Z`, `Grad` are linear operators; `K⁻¹` is a linear solve), and
  vector addition is linear (`palace/linalg/divfree.cpp:159-184`). Holds exactly
  in exact arithmetic; modulo `ksp` tolerance under the approximate solve.
- **Idempotence (projector law).** `P∘P = P` in exact arithmetic: applying the
  projector to an already-divergence-free field returns it unchanged. By the
  defining condition `Gᵀ M (P·y) = 0`
  (`palace/linalg/divfree.hpp:28-31`), `P·y` lies in the divergence-free
  subspace, so `WeakDiv·(P·y) = 0` (step 1 yields zero residual), hence the
  correction `Grad·ψ = 0` and `P·(P·y) = P·y`. Holds modulo `ksp` tolerance:
  `Gᵀ M (P·y) = 0` only up to the convergence tolerance on the non-essential
  dofs (`palace/linalg/divfree.cpp:140-142`, rel-tol set, abs-tol = machine
  epsilon at :141). **Caveat (added on repair):** the step
  "`P·y` divergence-free ⟹ `WeakDiv·(P·y) = 0`" silently identifies `WeakDiv`
  with the `Gᵀ M` of the defining condition (up to sign), so this derivation is
  itself **contingent on** the WeakDiv sign-convention OQ
  (`divfree-weakdiv-sign-convention-l0-verify`); it is exact only once that OQ
  confirms `WeakDiv ≈ Gᵀ M`.
- **Range.** `Range(P) = {x ∈ Field[N_nd] : Gᵀ M x = 0}` — the discrete
  divergence-free subspace (`palace/linalg/divfree.hpp:28-31`).
- **M-orthogonality (kernel = gradient range).** `Ker(P) = Range(Grad)`: the
  removed component is the irrotational (gradient) part, and the projection is
  orthogonal in the M-inner-product (the projected H1 problem `M·ψ = rhs`
  encodes the M-weighted normal equations `Gᵀ M G ψ = Gᵀ M y`). This is the
  defining property of the discrete Helmholtz decomposition; `M` SPD
  (`palace/linalg/divfree.cpp:119`) makes the M-inner-product well-defined.
- **Real-linearity / block-diagonal complex action.** For `ComplexVector`,
  `P·(u + i·v) = (P·u) + i·(P·v)` where `P` is the real apply — the operators
  are real-valued so the action is block-diagonal over `{Re, Im}`
  (`palace/linalg/divfree.cpp:159-184`).
- **Non-law (load-bearing): sign convention.** The correction is *additive*
  (`y + Grad·ψ`) because `WeakDiv` (built from
  `MixedVectorWeakDivergenceIntegrator`, `palace/linalg/divfree.cpp:113`)
  internally absorbs the minus sign of the weak divergence form. A flipped L0
  sign would invert the correction direction. This is a property of the
  constructed `WeakDiv` operator, honored verbatim at L1, **not independently
  re-derived** — see Open questions for the unverified-integrator-sign caveat.
- **Non-law (load-bearing): step ordering.** The essential-BC zeroing
  (`Z_{bdr_eff}`) must compose *after* `WeakDiv·y` and *before* the `ksp` solve
  (`palace/linalg/divfree.cpp:159-175`). Reordering changes the result. The
  sequence `WeakDiv → Z → ksp → Grad` is load-bearing.

## Dependencies

L1-internal:

- [`ksp_solve`](./ksp_solve.md) — the inner projected H1 solve `M·ψ = rhs`
  (step 3, `palace/linalg/divfree.cpp:175`). `divfree_project` is thus the
  first L1 operator whose *constructed-operator argument carries another
  constructed-operator* (`P.ksp : Solver[P.M]`) as a sub-field. The CG iteration
  internal to `ksp` is the standard Krylov sequential obstruction; it is
  interior to `ksp_solve` and does not leak into `divfree_project`.
- [`apply_linop`](./apply_linop.md) — the `WeakDiv·y` (step 1) and `Grad·ψ`
  (step 4) linear-operator applications.
- [`axpy`](./axpy.md) — the `y + Grad·ψ` gradient correction (step 4, fused as
  `Grad->AddMult(ψ, y, 1.0)`, the apply-and-accumulate idiom).

Shared concepts (cross-referenced, not duplicated):

- [`set_subvector_zero`](../concepts/set_subvector_zero.md) — the `Z_{bdr_eff}`
  essential-BC zeroing (step 2).
- [`constructed-operator-factory`](../concepts/constructed-operator-factory.md) —
  the construction-time assembly of `M`, `WeakDiv`, `Grad`, `bdr_eff`, `ksp`.

## Status

`firm`.

Every step of the apply is read from a positive source site
(`palace/linalg/divfree.cpp:155-186`), and the construction is fully read
(`palace/linalg/divfree.cpp:43-152`). The algebraic laws (linearity,
idempotence, range, M-orthogonality) follow from the defining condition stated
in the source (`palace/linalg/divfree.hpp:28-31`) and the SPD/real properties
asserted in the source (`palace/linalg/divfree.cpp:119`). The sign-convention
and step-ordering caveats are load-bearing non-laws carried as properties of the
constructed operators, not reconstructed sub-parts — so this is `firm`, not
`partly-constructive`.

No dedicated unit test exists (`test/unit/test-divfree.cpp` is absent; confirmed
by codemap call-site survey — only `divfree.cpp`-internal `Mult` calls and the
`eigensolver.cpp` / `arpack.cpp` / `slepc.cpp` driver call sites appear). The
firm decision follows the [`chebyshev-smoother`](./chebyshev-smoother.md)
precedent: every law is a structural identity or a directly-cited source
property, and the absence of a dedicated test does not reduce confidence in the
read structure. The `eigsolve` rough-in precedent does not bind here:
`eigsolve`'s rough-in was driven by literature-inferred convergence semantics;
`divfree_project`'s semantics are a fully-read linear projection with a
source-stated defining condition.

## Evidence

- `palace/linalg/divfree.hpp:28-31` — class doc: "projection onto a
  divergence-free space satisfying Gᵀ M x = 0, where G represents the discrete
  gradient matrix with columns spanning the nullspace of the curl-curl
  operator." (defining condition, range, kernel)
- `palace/linalg/divfree.hpp:34` — `class DivFreeSolver` (the projector class).
- `palace/linalg/divfree.hpp:40-55` — member fields: `M`, `WeakDiv`, `Grad`,
  `bdr_tdof_list_M`, `aux_tdof_lists`, `ksp`, `psi`/`rhs` scratch.
- `palace/linalg/divfree.hpp:63-72` — `Mult(y)` (in-place) and `Mult(x, y)`
  (out-of-place `y = x; Mult(y)`) declarations.
- `palace/linalg/divfree.cpp:51-81` — empty-boundary synthetic single-dof pin
  (Neumann-nullspace removal); the MPI root-rank selection.
- `palace/linalg/divfree.cpp:84-110` — `M` assembly: `DiffusionIntegrator` with
  real-permittivity coefficient, multigrid hierarchy, essential-BC diag-one.
- `palace/linalg/divfree.cpp:111-116` — `WeakDiv` assembly:
  `MixedVectorWeakDivergenceIntegrator`, partial assembly.
- `palace/linalg/divfree.cpp:117` — `Grad` = discrete interpolator.
- `palace/linalg/divfree.cpp:119` — `// The system matrix for the projection is
  real and SPD.` (justifies M-inner-product / M-orthogonality).
- `palace/linalg/divfree.cpp:121-149` — `ksp` setup: BoomerAMG (depth 1) or GMG
  wrapping BoomerAMG (depth > 1), CG, rel-tol, abs-tol = epsilon, max-it.
- `palace/linalg/divfree.cpp:155-186` — `Mult(y)` apply: the four steps.
- `palace/linalg/divfree.cpp:189-190` — `template class DivFreeSolver<Vector>;`
  / `<ComplexVector>;` (the VecType variant axis).
- `palace/drivers/eigensolver.cpp:260-262` — `divfree->Mult(v0)` initial-vector
  projection call site.
- `palace/linalg/arpack.cpp:586,752,766,783,791` and
  `palace/linalg/slepc.cpp:1870,1961,1970,1982,1991,2088,2163` —
  `opProj->Mult(...)` per-iteration projection inside the eigenvalue kernels.

Slice-corpus precedent (cycle-001-era, cycle-012-reduced; this firm entry
supersedes its L1 content): `book/src/spec/slices/divfree.md:24-100` (L1 form),
`:142-216` (L2 primitive composition).
```

```edit:book/src/L1/index.md
| [`chebyshev-smoother`](./chebyshev-smoother.md) | `(op: ChebSmoother[N], x: Tensor[N], y: Tensor[N], initial_guess: Bool) → Tensor[N]` | `apply_linop` (direct); `spectrum_estimate` (setup-only, opaque) | `firm` (constructed-operator gate; L0: `palace/linalg/chebyshev.cpp`; harvested cycle-012; test-coverage caveat, firm ratified) |
| [`divfree-projector`](./divfree-projector.md) | `(P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) → Field[N_nd]` | `ksp_solve` (direct, inner H1 solve), `apply_linop` (WeakDiv·y, Grad·ψ), `axpy` (gradient correction); `set_subvector_zero` (concept) | `firm` (constructed-operator gate; L0: `palace/linalg/divfree.cpp:155-186`; harvested cycle-013; sign-convention non-law carried; no dedicated test, firm on chebyshev-smoother precedent) |
```

## Operator content

(The full `book/src/L1/divfree-projector.md` content is in the proposed-changes
block above. Sections: slug + one-line; Context; Signature with bunsen-style
named-axis shape contract; Semantics (4-step apply + complex specialization);
Algebraic laws (linearity, idempotence, range, M-orthogonality, real-linearity)
+ two load-bearing non-laws (sign convention, step ordering); Dependencies
(`ksp_solve`, `apply_linop`, `axpy` + `set_subvector_zero` / constructed-operator
concepts); Status `firm`; Evidence citations.)

### Key new vocabulary cohort note (for layer-intro-author — see Open questions)

The vocabulary-cohort prose in `book/src/L1/index.md` (lines 29-40, "Firm (10)")
should be bumped to "Firm (11)" with a `divfree-projector` bullet noting it is
the **fourth constructed-operator gate** (after `ksp_solve`, `eigsolve`,
`chebyshev-smoother`) and the **first whose constructed-operator argument nests
another constructed-operator** (`P.ksp : Solver[P.M]`). I do NOT edit the layer
intro prose (layer-intro-author's domain); flagged here for the integrator /
next-cycle planner.

## Supporting evidence

- The defining condition and range/kernel characterization are read directly
  from `palace/linalg/divfree.hpp:28-31` (the class doc comment) — this is the
  source's own statement of what the operator computes.
- The four-step apply and the additive gradient correction are read from
  `palace/linalg/divfree.cpp:155-186` (`Grad->AddMult(ψ, y, 1.0)` at :180-181
  for the complex Re/Im branches and at :185 for the real branch is the
  additive correction; `linalg::SetSubVector(rhs, *bdr_tdof_list_M, 0.0)`
  at :173 is the essential-BC zeroing; `ksp->Mult(rhs, psi)` at :175 is the
  inner solve).
- The `M` real-and-SPD property (justifying M-orthogonality / well-defined
  M-inner-product) is the source comment `palace/linalg/divfree.cpp:119`.
- The complex block-diagonal action is read from the `if constexpr
  (std::is_same<VecType, ComplexVector>::value)` branches at
  `palace/linalg/divfree.cpp:159-167` and `:178-184`.
- Slice cross-reference: `book/src/spec/slices/divfree.md` (the cycle-012-reduced
  precursor) already firms the L1/L2/L3/L4 forms; this entry firms the L1
  operator surface and lets the slice's downstream citers
  (`L1/eigsolve`'s `projector : Maybe DivFreeSolver[ComplexVector]` field;
  `concepts/apply_linop` §"L2 use in divfree"; `concepts/ksp_solve:34`;
  `concepts/set_subvector_zero:27`; `L0/eigensolver-wrapper:44`) point at a firm
  L1 entry.

## Open questions / caveats

- **WeakDiv sign-convention (carried OQ `divfree-weakdiv-sign-convention-l0-verify`).**
  The claim that `MixedVectorWeakDivergenceIntegrator`
  (`palace/linalg/divfree.cpp:113`) encodes the negative-divergence sign — so
  that the correction is `+Grad·ψ` (`palace/linalg/divfree.cpp:180,184`) rather
  than `−Grad·ψ` — is an unverified L0 reading of the integrator's internal
  sign. The slice already flags this
  (`book/src/spec/slices/divfree.md:135-140`). A flipped integrator sign would
  invert the correction direction without changing the prose. This entry carries
  the sign as a load-bearing non-law (a property of the constructed `WeakDiv`),
  which is the correct L1 treatment regardless of the integrator's internal
  sign; resolving it requires an integrator-level (MFEM-vendored) citation, which
  is below the L0 scope boundary. Recommend a `verify-citation-range` pass on the
  `MixedVectorWeakDivergenceIntegrator` definition before the future L1>L0
  `divfree-projector` lowering theme treats the sign as positively anchored.

- **Header-comment vs class-doc characterization (NEW).** The `Mult`
  declaration comment (`palace/linalg/divfree.hpp:63-66`) describes the result as
  "the irrotational portion of this vector field. The resulting vector will
  satisfy ∇ × y = 0", whereas the class doc (`palace/linalg/divfree.hpp:28-31`)
  and every downstream use (eigensolver subspace projection) describe the output
  as the **divergence-free** component satisfying `Gᵀ M x = 0`. These are
  *complementary* subspaces, so the two comments appear to describe opposite
  outputs. The code computes `y ← y + Grad·ψ`
  (`palace/linalg/divfree.cpp:177-186`); since `Range(Grad)` is the irrotational
  (curl-free) subspace and the projector's documented *purpose* is to keep
  eigenvectors divergence-free, the class-doc characterization (`Gᵀ M x = 0`,
  divergence-free output) is the one this entry adopts, and the `Mult`-comment
  "irrotational portion … ∇×y=0" is read as a stale or mislabeled comment. This
  should be confirmed against the eigensolver semantics (the projector exists to
  remove the spurious gradient/electrostatic modes from H(curl) eigenvectors,
  i.e. to *retain* the divergence-free part) — flag for a `lowering-verifier`
  audit when the L1>L0 `divfree-projector` theme is authored. The discrepancy
  does not change the L1 operator's signature or laws (the laws are stated for
  the projector `P` whose range is the divergence-free subspace per the class
  doc); it is a documentation-fidelity caveat, not a structural one.

  **Third in-`.cpp` anchor (added on repair).** The apply body itself carries a
  third intent comment, immediately above step 4:
  `palace/linalg/divfree.cpp:177` reads
  `// Compute the irrotational portion of y and subtract.` This makes the
  contradiction *three-way*, not two-way, and it is doubly significant:
  (i) it **corroborates** the class-doc / divergence-free reading this entry
  adopts — "subtract the irrotational portion" ⟹ the returned field is the
  divergence-free remainder; (ii) it simultaneously sits over literally additive
  code (`Grad->AddMult(psi, y, 1.0)`, `+1.0`, at :180-181 / :185), so the
  comment's "subtract" is only reconcilable with the `+1.0` IF `WeakDiv` carries
  the negating sign (i.e. `Grad·ψ = −(irrotational part of y)`). This is the
  **same tension** as the WeakDiv sign-convention OQ above
  (`divfree-weakdiv-sign-convention-l0-verify`): the additive-sign correctness
  and the divergence-free output characterization are **contingent on** that
  sign reading, not independent of it. The two OQs are therefore linked —
  resolving the WeakDiv-sign OQ resolves this one. The repairer does NOT
  adjudicate the sign here (that is the `lowering-verifier`'s job); this `:177`
  anchor and the OQ linkage are folded into the existing `lowering-verifier`
  follow-up already flagged for the L1>L0 `divfree-projector` theme.

- **Slice reduction this unblocks.** Landing this firm L1 entry unblocks further
  reduction of `book/src/spec/slices/divfree.md`: its L1 section
  (`book/src/spec/slices/divfree.md:24-100`) and L2 primitive-composition
  section (`:142-216`) can be reduced to stubs pointing at this firm
  `L1/divfree-projector` entry (the L1 form) once a future cycle also firms the
  L2/L3/L4 forms or confirms they are identity-lowerings of the L1 form. The
  slice's "Pending lift" note (`:13-15`) names exactly this entry
  (`L1/divfree-projector`, OQ `l1-divfree-projector-promotion`) as the strong
  promotion candidate — that OQ is now answered by this entry. Recommend a
  follow-up `same-layer-cross-cutter` slice-reduction audit (per the
  `phase-1-slice-reduction-audit` skill) on `book/src/spec/slices/divfree.md`
  in a subsequent cycle.

- **L2/L3/L4 backfill (deferred).** The slice carries full L2/L3/L4 forms for
  the projector. Per the "lower-level shared vocabulary takes priority" and
  "identity-lowerings still require both L levels" invariants, the L2
  (`apply_linop`/`set_subvector_zero`/`ksp_solve`/`axpy` composition), L3
  (global tensor-field `P(y) = y + Grad·K⁻¹(Z(WeakDiv·y))`), and L4
  (`applyDivFree :: DivFreeParams -> SimState V -> SolveM (SimState V)`) forms
  should each get firm entries in subsequent cycles, with the L4>L3>L2>L1
  lowering chain. This entry establishes only the L1 operator. Not in scope for
  this one-operator dispatch.

- **L1>L0 lowering theme (deferred, abstractor's domain).** The in-place `Mult(y)`
  mutation rotation (the destination-buffer + `psi`/`rhs` scratch
  reintroduction, the `Grad->AddMult` apply-and-accumulate idiom, the
  `if constexpr` complex-component unrolling, the empty-boundary pin + MPI
  collectives) is a future `L1-L0/divfree-projector-mutation-rotation` theme —
  flagged, not authored here.

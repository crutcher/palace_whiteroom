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
- **Idempotence (projector law) — `partly-constructive` sub-law; see Status.**
  `P∘P = P` in exact arithmetic: applying the
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
  confirms `WeakDiv ≈ Gᵀ M`. This contingency is the named sub-part that drives
  the entry's `partly-constructive` status (see Status); the **promotion
  condition** is a `verify-citation-range` / `lowering-verifier` pass on the
  `MixedVectorWeakDivergenceIntegrator` sign convention.
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

`partly-constructive`.

The **structural decomposition is firm**: every step of the apply is read from a
positive source site (`palace/linalg/divfree.cpp:155-186`), the construction is
fully read (`palace/linalg/divfree.cpp:43-152`), and the linearity, range,
M-orthogonality, real-linearity, and step-ordering laws follow from the defining
condition stated in the source (`palace/linalg/divfree.hpp:28-31`) and the
SPD/real properties asserted in the source (`palace/linalg/divfree.cpp:119`).

The entry is **`partly-constructive`** (adjudicated by the cycle-013 integrator,
not the harvester's argued `firm`) on **one named sub-part**: the **idempotence
law `P∘P = P`** and the **divergence-free output characterization** are both
contingent on the `WeakDiv ≈ Gᵀ M` sign reading. That reading is NOT confirmed
from a positive Palace source site — it rests on the internal sign convention of
the MFEM-vendored `MixedVectorWeakDivergenceIntegrator`
(`palace/linalg/divfree.cpp:113`), which is below the L0 scope boundary, and is
further entangled with the three-way `irrotational`/`subtract`-vs-additive-`+1.0`
comment contradiction (see Open questions). Per the cycle-012-codified
`partly-constructive` invariant, a load-bearing sub-law that depends on an
unresolved reading rather than a positive source confirmation is `partly-constructive`,
not plain `firm`.

- **Constructive sub-part:** the idempotence law `P∘P = P` (and the
  divergence-free output characterization it shares the sign reading with).
- **Negative anchor:** no positive Palace source site exhibits the `WeakDiv`
  sign; the additive `+1.0` correction (`palace/linalg/divfree.cpp:180-181,185`)
  is reconcilable with the `// … subtract` intent comment
  (`palace/linalg/divfree.cpp:177`) and the class-doc divergence-free output
  (`palace/linalg/divfree.hpp:28-31`) **only if** `WeakDiv` carries the negating
  sign — a reading of the integrator's internals, not a read of a positive
  Palace site.
- **Promotion condition:** a `verify-citation-range` / `lowering-verifier` pass
  on the `MixedVectorWeakDivergenceIntegrator` sign convention (carried OQ
  `divfree-weakdiv-sign-convention-l0-verify`), folded into the future L1>L0
  `divfree-projector-mutation-rotation` theme's lowering-verifier audit. Once
  the sign is positively anchored, the idempotence sub-law and the
  divergence-free characterization become unconditional and the entry promotes
  to `firm`.

No dedicated unit test exists (`test/unit/test-divfree.cpp` is absent; confirmed
by codemap call-site survey — only `divfree.cpp`-internal `Mult` calls and the
`eigensolver.cpp` / `arpack.cpp` / `slepc.cpp` driver call sites appear). The
test absence alone would not have blocked `firm` (cf. the
[`chebyshev-smoother`](./chebyshev-smoother.md) precedent, where every law is a
verified-exact syntactic identity); the sign-reading contingency on a
load-bearing sub-law is what drives the `partly-constructive` status here. The
`eigsolve` rough-in precedent does not bind either: `eigsolve`'s rough-in was
driven by literature-inferred convergence semantics; `divfree_project`'s
semantics are a fully-read linear projection with a source-stated defining
condition and a single named sign-contingent sub-law.

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

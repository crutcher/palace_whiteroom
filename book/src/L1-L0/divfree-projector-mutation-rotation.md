---
# Lowering theme (L1>L0). Per graded-stack scheme §5: rank = min(endpoint ranks). The L1
# endpoint (divfree-projector) is firm (rank 3); the L0 endpoint is rank-terminal ground
# truth. So the theme is firm and rank(theme) <= min(endpoints) holds for free.
rank: firm
edges:
  depends-on:
    - target: L1/divfree-projector
      kind: lowers-to             # the L1 source gate this theme lowers
    - target: palace/linalg/divfree.cpp:155-187
      kind: cites-evidence        # DivFreeSolver<VecType>::Mult — the in-place four-step apply
    - target: palace/linalg/divfree.cpp:43-152
      kind: cites-evidence        # the constructor materialising the L1 closure fields
    - target: palace/linalg/divfree.hpp:55
      kind: cites-evidence        # `mutable VecType psi, rhs;` — the construction-bound scratch
  reference:
    - L1-L0/set-subvector-zero-mutation-rotation  # the step-2 zeroing leaf
    - L2-L1/divfree-projector-leaf-identity       # the L2>L1 sibling leg
---

# divfree-projector-mutation-rotation

The mutation rotation for the divergence-free projector apply. Lowers the pure
L1 form [`divfree_project`](../L1/divfree-projector.md) —
`y' = divfree_project(P, y) = y + P.Grad · K⁻¹( Z_{P.bdr_eff}( P.WeakDiv · y ) )`
— into Palace's in-place L0 `DivFreeSolver<VecType>::Mult(VecType &y)` member
method, plus the construction-bound `DivFreeSolver(...)` constructor that
materialises the L1 closure fields. Narrated forward: the L1 pure out-of-place
projection dissolves into the L0 output-argument mutation idiom (writes through
`y`, scribbles construction-bound scratch members `psi`, `rhs`) over a
constructed-operator value whose fields (`M`, `WeakDiv`, `Grad`,
`bdr_tdof_list_M`, `ksp`) are assembled once at solver setup.

## Slug

`divfree-projector-mutation-rotation`

## L1 form (LHS)

The pure-functional projection consumes the prior `y` as a value and produces a
fresh divergence-free field over an opaque constructed projector `P`
(`DivFreeProjector[N_nd, N_h1]`, carrying `(M, WeakDiv, Grad, bdr_eff, ksp)`):

    y' = divfree_project(P, y)
       = y + P.Grad · K⁻¹( Z_{P.bdr_eff}( P.WeakDiv · y ) )
         where K solves  P.M · ψ = rhs  via P.ksp

The four composed steps at L1 (see
[`L1/divfree-projector`](../L1/divfree-projector.md) §Semantics):

1. `rhs = P.WeakDiv · y`              — weak-divergence residual (Nedelec → H1)
2. `rhs = Z_{P.bdr_eff}(rhs)`         — zero on the essential H1 boundary dofs
3. `ψ   = K⁻¹ rhs`, i.e. `P.M·ψ=rhs`  — projected H1 solve via `P.ksp`
4. `y'  = y + P.Grad · ψ`             — gradient correction (additive)

At L1 there is **no destination buffer** (the projection returns a value), **no
scratch-buffer ownership** (`psi`/`rhs` are absent from the signature), and **no
runtime element-type tag** — the real (`Vector`) / complex (`ComplexVector`)
variant is absorbed by polymorphism over `P` and `y`. `Z_S` is the
[`set_subvector_zero`](../concepts/set_subvector_zero.md) primitive; `K⁻¹`
denotes the approximate `ksp` solve, not exact inversion.

## L0 form (RHS)

The rewrite splits into a **construction site** (the constructor that
materialises the closure fields) and an **application site** (the `Mult` family
that realises the per-call projection by in-place mutation). One L0 class
(`DivFreeSolver<VecType>`) carries the element-type variant via the `VecType`
template parameter; the apply scaffold is identical across `Vector` and
`ComplexVector` modulo the Re/Im branch (sub-pattern D).

### Sub-pattern A — application via in-place `Mult(VecType &y)`

    template <typename VecType>
    void DivFreeSolver<VecType>::Mult(VecType &y) const
    {
      BlockTimer bt(Timer::DIV_FREE);

      // Compute the divergence of y.                       -- step 1
      if constexpr (std::is_same<VecType, ComplexVector>::value) {
        WeakDiv->Mult(y.Real(), rhs.Real());
        WeakDiv->Mult(y.Imag(), rhs.Imag());
      } else {
        WeakDiv->Mult(y, rhs);
      }

      // Apply essential BC and solve the linear system.    -- steps 2,3
      if (bdr_tdof_list_M) {
        linalg::SetSubVector(rhs, *bdr_tdof_list_M, 0.0);    // step 2: Z_{bdr_eff}
      }
      ksp->Mult(rhs, psi);                                   // step 3: M·ψ = rhs

      // Compute the irrotational portion of y and subtract. -- step 4
      if constexpr (std::is_same<VecType, ComplexVector>::value) {
        Grad->AddMult(psi.Real(), y.Real(), 1.0);
        Grad->AddMult(psi.Imag(), y.Imag(), 1.0);
      } else {
        Grad->AddMult(psi, y, 1.0);                          // y += Grad·ψ
      }
    }

The L1 *value* `y'` is the L0 `y` after `Mult(y)` returns. The crucial L0 facts
the L1 form erases:

- **Destination-arg mutation.** `y` is the in/out argument; `Grad->AddMult(psi,
  y, 1.0)` writes through it in place (`y += Grad·ψ`). The L1 form takes the
  prior `y` as a value and returns a fresh one. Same output-arg idiom as
  [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md): the
  destination is named in the call's argument list, not on the LHS.
- **Two scribbled scratch members.** `rhs` (the H1-side residual) and `psi`
  (the H1 solution) are `mutable VecType` members
  (`palace/linalg/divfree.hpp:55`), sized once in the constructor
  (`palace/linalg/divfree.cpp:148-151`), written every call, carrying no value
  across calls. At L1 they vanish — the projector is a single value-producing
  action.
- **Construction-bound operators.** `WeakDiv`, `ksp`, `Grad`,
  `bdr_tdof_list_M` are member pointers / values set once in the constructor and
  read-only across calls; they are `P`'s captured closure fields at L1.
- **Load-bearing additive sign.** The correction is **additive** (`y +
  Grad·ψ`, the `+1.0` at `palace/linalg/divfree.cpp:185`), yet it *removes* the
  gradient part, because `WeakDiv` (step 1) carries the negating `-1.0` of the
  weak-divergence form (`a(u,v) = -(ε u, ∇v)`,
  `palace/fem/integrator.hpp:217`, materialised at
  `palace/fem/integ/mixedvecgrad.cpp:202`). A flipped L0 sign would invert the
  correction. The L1 form honours this verbatim (`WeakDiv = -Gᵀ`); it is a
  property of the constructed operator, not of the apply scaffold. See
  Applicability conditions.
- **Inner solve is itself a constructed-operator gate.** `ksp->Mult(rhs, psi)`
  (step 3) is the [`ksp_solve`](../L1/ksp_solve.md) inner H1 solve. Its CG
  iteration is interior to `ksp_solve` and does not leak into this theme; here
  it is the opaque `K⁻¹` action — the
  [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
  fidelity rule (the inner gate's iteration stays interior to its own lowering
  theme). This theme's closure carries *another* constructed-operator gate as a
  sub-field (`P.ksp : Solver[P.M]`) — the
  [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
  shape. It is **not the first** such case: the firm
  [`eigsolve-mutation-rotation`](./eigsolve-mutation-rotation.md) theme is the
  prior and richer instance, whose closure `E` carries **two**
  nested gates (`E.linear : Solver[A]` and `E.projector : Maybe
  DivFreeSolver[ComplexVector]` — the latter being this projector itself,
  [`L1/eigsolve`](../L1/eigsolve.md) §Shape contract `E`), so the nesting is
  transitively three-deep (eigsolve ⊃ divfree ⊃ ksp). Divfree is the **second**
  gate-carrying L1>L0 theme (after eigsolve), carrying the **third** nested gate
  overall (after eigsolve's two, `E.linear` + `E.projector`).

Justification kind: **structural** — re-bind the L1 output value into the L0
in/out destination buffer `y`; erase the scratch members `rhs`, `psi`; the
operators are the construction-bound closure fields. The apply maps the four L1
composed steps 1:1 onto the four L0 statement groups.

Citations:
- `palace/linalg/divfree.cpp:155-187` — `DivFreeSolver<VecType>::Mult(VecType
  &y)` (signature `:155`, opening brace `:156`, close brace `:187`; the four
  steps).
- `palace/linalg/divfree.cpp:159-168` — step 1: `WeakDiv->Mult(...)` (complex
  Re/Im at `:162-163`, real at `:167`).
- `palace/linalg/divfree.cpp:170-174` — step 2: `if (bdr_tdof_list_M)
  { linalg::SetSubVector(rhs, *bdr_tdof_list_M, 0.0); }` (the `Z_{bdr_eff}`
  zeroing; `SetSubVector` call at `:173`).
- `palace/linalg/divfree.cpp:175` — step 3: `ksp->Mult(rhs, psi)`.
- `palace/linalg/divfree.cpp:177-186` — step 4: `Grad->AddMult(...)` (complex
  Re/Im at `:180-181`, real at `:185` with the `1.0`).
- `palace/linalg/divfree.hpp:55` — `mutable VecType psi, rhs;` (the two
  scratch members).
- `palace/linalg/vector.hpp:221` — `void SetSubVector(VecType &x, const
  mfem::Array<int> &rows, double s);` (the scalar-fill overload realising
  `Z_S` with `s = 0.0`).

### Sub-pattern B — out-of-place entry `Mult(const VecType &x, VecType &y)`

    void Mult(const VecType &x, VecType &y) const
    {
      y = x;       // explicit copy (no silent aliasing)
      Mult(y);     // in-place apply (sub-pattern A)
    }

The two-argument convenience form is `y = x; Mult(y)` — an explicit copy then
in-place apply, i.e. the pure out-of-place form `y' = P·x`. At L1 both the
one-argument and two-argument L0 forms collapse to the single pure function
`divfree_project(P, ·)`: the destination buffer disappears from the signature;
the copy and the `Mult`/`Mult(x,y)` split both vanish.

Justification kind: **structural** — the `Mult(y)` / `Mult(x, y)` split is an L0
destination-ownership convention (mutate-in-place vs. copy-then-mutate), not an
algebraic distinction. The L1 form is out-of-place by definition; the
two-argument L0 entry is the literal out-of-place realisation; the one-argument
L0 entry is the destructive-update realisation when the caller can spare `y`.

Citations:
- `palace/linalg/divfree.hpp:68-72` — `Mult(const VecType &x, VecType &y)
  { y = x; Mult(y); }` (inline; `:68` signature, `:70` `y = x;`, `:71`
  `Mult(y);`, `:72` close brace).
- `palace/linalg/divfree.hpp:63-66` — `Mult(VecType &y)` declaration + the doc
  comment "compute the Nedelec dofs of the irrotational portion ... will satisfy
  ∇ x y = 0" (**stale/misleading relative to the divergence-free implemented
  behaviour** — Palace-internal doc inconsistency, OQ
  `divfree-mult-doc-irrotational-vs-divfree-stale`; the implemented and L1
  semantics are the divergence-free target of the class doc
  `palace/linalg/divfree.hpp:28-31`).

### Sub-pattern C — construction site: closure-field materialisation

The L1 closure `P = DivFreeProjector[N_nd, N_h1]` is the value the constructor
materialises (`palace/linalg/divfree.cpp:43-152`):

- `P.M` ← ε-weighted H1 mass-like operator: a `BilinearForm` with a
  `DiffusionIntegrator` carrying the real-permittivity coefficient, assembled
  over the H1 multigrid hierarchy, with essential-BC `DIAG_ONE` diagonal policy
  (`palace/linalg/divfree.cpp:84-110`). Real and SPD by construction
  (`palace/linalg/divfree.cpp:119` `// ... real and SPD`).
- `P.WeakDiv` ← ε-weighted weak-divergence operator (Nedelec → H1): a
  `BilinearForm` with a `MixedVectorWeakDivergenceIntegrator`, always partially
  assembled, wrapped in a `ParOperator` (`palace/linalg/divfree.cpp:111-116`).
  The negating sign is **internal to the integrator** (see the sign sub-note
  below).
- `P.Grad` ← the discrete gradient interpolator (H1 → Nedelec):
  `nd_fespace.GetDiscreteInterpolator(...)` (`palace/linalg/divfree.cpp:117`).
- `P.bdr_eff` ← the finest-level essential H1 boundary true-dof set, captured as
  `bdr_tdof_list_M = M_l->GetEssentialTrueDofs()` at the finest level
  (`palace/linalg/divfree.cpp:103`). When the user-supplied list is globally
  empty, a synthetic single-dof pin (one true dof, dof 0, on one root rank)
  removes the pure-Neumann nullspace (`palace/linalg/divfree.cpp:51-81`).
- `P.ksp` ← a CG solver bound to `P.M` as both operator and preconditioner
  target (`SetOperators(*M, *M)`), preconditioned by BoomerAMG (depth 1) or
  geometric multigrid wrapping BoomerAMG (depth > 1), with the construction-time
  rel-tol, abs-tol = machine epsilon, and iteration cap
  (`palace/linalg/divfree.cpp:120-146`). The inner constructed-operator gate;
  see [`ksp_solve`](../L1/ksp_solve.md).
- `P` scratch ← `psi`, `rhs` sized to the finest H1 true-vsize and marked
  device-resident (`palace/linalg/divfree.cpp:148-151`). These are the L0
  scratch members erased at L1 (sub-pattern A).

Justification kind: **structural** — the constructor is the
constructed-operator-gate construction step (same family as the
[`ksp-solve`](./ksp-solve-mutation-rotation.md) /
[`chebyshev-smoother`](./chebyshev-smoother-mutation-rotation.md) /
[`eigsolve`](./eigsolve-mutation-rotation.md) setup sites): the L1 closure `P`
is a pure function of the setup inputs `(mat_op, nd_fespace, h1_fespaces,
h1_bdr_tdof_lists, tol, max_it)` modulo the opaque assembly/AMG-setup machinery,
which is below this theme's resolution (it is the
[`constructed-operator-factory`](../concepts/constructed-operator-factory.md)
concern).

Citations:
- `palace/linalg/divfree.cpp:43-48` — ctor signature.
- `palace/linalg/divfree.cpp:51-81` — empty-boundary synthetic single-dof pin
  (Neumann-nullspace removal); MPI root-rank selection at `:63-69,:73`
  (`GetComm()`@:63, `Mpi::GlobalSum`@:64, `Mpi::Size/Rank`@:67-68,
  `Mpi::GlobalMin`@:69) — single-rank scope reduces this to "pin true dof 0 when
  the boundary list is globally empty" (`tdof_list[0] = 0`@:78).
- `palace/linalg/divfree.cpp:84-110` — `M` assembly: `epsilon_func`@:86-87,
  `BilinearForm m`@:90, `DiffusionIntegrator`@:91, per-level `DIAG_ONE` essential
  policy@:100-101, `bdr_tdof_list_M = M_l->GetEssentialTrueDofs()`@:104,
  `M = std::move(M_mg)`@:108.
- `palace/linalg/divfree.cpp:111-116` — `WeakDiv` assembly: comment@:111,
  `BilinearForm weakdiv(nd_fespace, ...)`@:112,
  `MixedVectorWeakDivergenceIntegrator`@:113, `WeakDiv =
  std::make_unique<ParOperator>(weakdiv.PartialAssemble(), ...)`@:114-115.
- `palace/linalg/divfree.cpp:117` — `Grad =
  &nd_fespace.GetDiscreteInterpolator(...)`.
- `palace/linalg/divfree.cpp:119` — `// The system matrix for the projection is
  real and SPD.` (justifies the M-inner-product / M-orthogonality at L1).
- `palace/linalg/divfree.cpp:120-146` — `ksp` setup: BoomerAMG@:120-122, GMG
  (depth>1)@:124-132, `CgSolver`@:138-139, `SetInitialGuess(false)`@:140,
  `SetRelTol(tol)`@:141, `SetAbsTol(epsilon())`@:142, `SetMaxIter(max_it)`@:143,
  `ksp = make_unique<BaseKspSolver>`@:145, `ksp->SetOperators(*M, *M)`@:146
  (**rel-tol corrected to `:141` from the L1 entry's `:140`; abs-tol `:142`
  confirmed**).
- `palace/linalg/divfree.cpp:148-151` — `psi`/`rhs` `SetSize(...TrueVSize())`
  + `UseDevice(true)` (the scratch-member sizing).

#### Sign sub-note (load-bearing, positively anchored)

The `WeakDiv = -Gᵀ` (ε-weighted) reading is anchored in Palace-owned source:
the `MixedVectorWeakDivergenceIntegrator` bilinear form is `a(u, v) = -(Q u,
grad v)` for `u ∈ H(curl)`, `v ∈ H1` (`palace/fem/integrator.hpp:217`); the
class is Palace-owned, libCEED-backed (`palace/fem/integrator.hpp:218-226` — NOT
MFEM-vendored); the negating sign is materialised as an explicit `-1.0`
coefficient `PopulateCoefficientContext(space_dim, Q, transpose, -1.0)` inside
`MixedVectorWeakDivergenceIntegrator::Assemble`
(`palace/fem/integ/mixedvecgrad.cpp:202`; the `Assemble` body opens at `:148`).
The contrast is the sibling `MixedVectorGradientIntegrator::Assemble` (body
opens `:23`), whose `PopulateCoefficientContext(space_dim, Q, transpose)` carries
**no `-1.0`** (`palace/fem/integ/mixedvecgrad.cpp:142`). Cross-validated against
MFEM (`test/unit/test-libceed.cpp:905-916`). This sub-note is documentation of
the L1 closure field, not a separate rewrite rule; it is what makes the additive
`y + Grad·ψ` correction (sub-pattern A, step 4) *remove* the gradient part.

Justification kind: **algebraic** — the sign identity `WeakDiv = -Gᵀ`
(positively anchored) is what reconciles the additive L0 correction with the
divergence-free L1 output.

### Sub-pattern D — element-type variant via `VecType` templating

`DivFreeSolver<VecType>` is instantiated for `VecType ∈ {Vector,
ComplexVector}` (`palace/linalg/divfree.cpp:189-190`). The complex specialisation
applies the same real-valued operators (`WeakDiv`, `M`, `Grad`, `ksp`)
independently to `y.Real()` and `y.Imag()` (sub-pattern A, the `if constexpr`
branches); the inner `ksp->Mult` is a single solve on the `ComplexOperator`-typed
system whose CG recursion is component-blind. There is no cross-coupling between
real and imaginary parts. At L1 this is the parametric variant absorbed by
polymorphism over the field element type
([`L1/divfree-projector`](../L1/divfree-projector.md) §Signature, `y` element-type
note — block-diagonal complex action `P·(u + iv) = (P·u) + i(P·v)`).

Justification kind: **structural** — the `VecType` template parameter and the
`if constexpr` Re/Im split are a compile-time element-type dispatch, not a
runtime algebraic distinction. The L1 form has one action; the two L0
instantiations are real and complex realisations of the same projection.

Citations:
- `palace/linalg/divfree.cpp:189-190` — `template class DivFreeSolver<Vector>;`
  / `template class DivFreeSolver<ComplexVector>;`.
- `palace/linalg/divfree.cpp:160-164` — complex `if constexpr` weak-div branch
  (step 1).
- `palace/linalg/divfree.cpp:178-181` — complex `if constexpr` gradient-
  correction branch (step 4).

## Applicability conditions

The rewrite preserves semantics when:

1. **No aliasing between `y`, `rhs`, `psi`.** `Mult(y)` reads `y` (step 1) and
   writes `y` (step 4 in-place accumulate), writes `rhs` (step 1) and reads it
   (steps 2,3), writes `psi` (step 3) and reads it (step 4). The L1 form takes
   the pre-call `y` as a value and owns no scratch, so the lowering must
   guarantee `rhs`, `psi` are distinct buffers from `y` and from each other.
   (Palace allocates `psi`, `rhs` as distinct construction-bound members
   distinct from the caller's `y`. Inherited applicability-condition shape from
   [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md).)
2. **No observer of prior `y` after the in-place call.** `Mult(y)` destroys the
   prior `y` (the `+= Grad·ψ` accumulation). If a downstream op reads `y_old`,
   the in-place form (sub-pattern A) is invalid and the out-of-place form
   (sub-pattern B) must be used; at L1 `y_old` is still in scope as the value
   argument. Upheld at the eigensolver call sites by lexical sequencing (the
   projected vector overwrites the candidate in place,
   `palace/drivers/eigensolver.cpp:262`, `palace/linalg/arpack.cpp:586`).
3. **Closure immutability across calls.** `P` (`M`, `WeakDiv`, `Grad`,
   `bdr_tdof_list_M`, `ksp`) is set once in the constructor and read-only across
   `Mult` calls. There is no per-call control input — unlike
   [`chebyshev-smoother`](./chebyshev-smoother-mutation-rotation.md)'s
   per-call `initial_guess`, the projector is a fixed linear map on its single
   field argument.
4. **Step ordering is load-bearing.** The sequence `WeakDiv → Z_{bdr_eff} → ksp
   → Grad` (`palace/linalg/divfree.cpp:159-186`) must not be reordered: the
   essential-BC zeroing composes *after* `WeakDiv·y` and *before* the `ksp`
   solve. Reordering changes the result (L1 §Algebraic laws "Non-law:
   step ordering").
5. **Sign convention is honoured verbatim.** The additive `+1.0` gradient
   correction (`palace/linalg/divfree.cpp:185`) is correct *only* in combination
   with the `-1.0` weak-div sign (`palace/fem/integ/mixedvecgrad.cpp:202`). A
   lowering that re-derives `WeakDiv` without the `-1.0`, or flips the
   `Grad->AddMult` sign, inverts the correction. (Sub-pattern C sign sub-note.)
6. **Element-type conformance.** `<Vector>` (real) and `<ComplexVector>`
   (complex) are both instantiated (`palace/linalg/divfree.cpp:189-190`); the
   action is identical, only the Re/Im dispatch differs (sub-pattern D). The
   operators are real-valued; there is no cross-coupling between Re/Im.
7. **Single-machine scope.** The `MPI_Comm` and `Mpi::GlobalSum/GlobalMin/
   Rank/Size` machinery in the empty-boundary pin
   (`palace/linalg/divfree.cpp:62-79`) is read as its single-rank equivalent
   (MPI distribution out of scope, flagged once). The `MPI_Comm` does not appear
   in the L1 signature.

## Justification kind

- **Sub-pattern A** (in-place apply) — `structural`. Output-arg `y` re-bind +
  scratch `rhs`, `psi` erasure; 1:1 step mapping.
- **Sub-pattern B** (`Mult(x, y)` wrapper) — `structural`. Destination-ownership
  convention split (in-place vs. copy-then-mutate).
- **Sub-pattern C** (construction) — `structural` (with one `algebraic` sign
  sub-note). Constructed-operator-gate closure materialisation; pure-of-inputs
  modulo opaque assembly/AMG setup.
- **Sub-pattern D** (element-type variant) — `structural`. Compile-time
  `VecType` template dispatch.

The theme as a whole is `structural` with one algebraic sub-note (the sign
identity in C). A `lowering-verifier` audit in a later cycle should confirm the
four sub-patterns match the L0 corpus exhaustively (both element-type
instantiations, the in-place + out-of-place entry points, all driver call
sites).

## Speculative L1 operators

None. The L1 anchor [`L1/divfree-projector`](../L1/divfree-projector.md) is firm,
and all its sub-dependencies are firm L1 operators / firm concepts:
[`apply_linop`](../L1/apply_linop.md) (the `WeakDiv·y` and `Grad·ψ` applies),
[`axpy`](../L1/axpy.md) (the `y + Grad·ψ` accumulate, fused as
`Grad->AddMult(psi, y, 1.0)`),
[`ksp_solve`](../L1/ksp_solve.md) (the inner H1 solve),
[`set_subvector_zero`](../concepts/set_subvector_zero.md) (the `Z_{bdr_eff}`
zeroing). This theme proposes no new vocabulary.

## Evidence

L0 evidence ranges:

- `palace/linalg/divfree.cpp:155-187` — `Mult(VecType &y)` apply (sig `:155`,
  brace `:156`, close `:187`).
- `palace/linalg/divfree.cpp:159-186` — the four apply steps (step 1
  `:159-168`, step 2 `:170-174`, step 3 `:175`, step 4 `:177-186`).
- `palace/linalg/divfree.cpp:43-152` — constructor (sig `:43-48`, empty-bdr pin
  `:51-81`, `M` `:84-110`, SPD comment `:119`, `WeakDiv` `:111-116`, `Grad`
  `:117`, `ksp` `:120-146`, scratch `:148-151`, close `:152`).
- `palace/linalg/divfree.cpp:189-190` — `Vector` / `ComplexVector`
  instantiations.
- `palace/linalg/divfree.hpp:28-31` — class doc defining condition `Gᵀ M x = 0`.
- `palace/linalg/divfree.hpp:55` — `mutable VecType psi, rhs;` scratch members.
- `palace/linalg/divfree.hpp:63-66` — `Mult(VecType &y)` decl + stale-doc
  comment.
- `palace/linalg/divfree.hpp:68-72` — `Mult(const VecType &x, VecType &y)
  { y = x; Mult(y); }`.
- `palace/linalg/vector.hpp:221` — `SetSubVector(VecType&, const
  mfem::Array<int>&, double)` (the `Z_S` scalar-fill overload).
- `palace/fem/integrator.hpp:217` — weak-div bilinear form `a(u, v) = -(Q u,
  grad v)`.
- `palace/fem/integrator.hpp:218-226` — `MixedVectorWeakDivergenceIntegrator`
  (Palace-owned, libCEED-backed).
- `palace/fem/integ/mixedvecgrad.cpp:148` — `MixedVectorWeakDivergenceIntegrator
  ::Assemble` body opens.
- `palace/fem/integ/mixedvecgrad.cpp:202` — `PopulateCoefficientContext(...,
  -1.0)` (the negating sign).
- `palace/fem/integ/mixedvecgrad.cpp:23` — sibling `MixedVectorGradient
  Integrator::Assemble` body opens.
- `palace/fem/integ/mixedvecgrad.cpp:142` — sibling
  `PopulateCoefficientContext(...)` with NO `-1.0` (sign contrast).
- `palace/linalg/operator.hpp:133` — `Operator::AddMult(const Vector&, Vector&,
  const double a = 1.0)` (the `Grad->AddMult` apply-and-accumulate idiom).
- `palace/drivers/eigensolver.cpp:262` — `divfree->Mult(v0)` initial-vector
  projection call site.
- `palace/linalg/arpack.cpp:586` — `opProj->Mult(y1)` per-iteration projection
  call site.
- `test/unit/test-libceed.cpp:905-916` — `MixedVectorWeakDivergenceIntegrator`
  cross-validated against MFEM (L0-equivalent sign-behaviour coverage).

L1 anchor:

- `book/src/L1/divfree-projector.md` — the firm L1 operator all four
  sub-patterns lower from.

## Open questions / caveats

- **Stale `Mult` doc comment (Palace-internal inconsistency).** The per-method
  doc comment `palace/linalg/divfree.hpp:64-66` describes the output as "the
  irrotational portion ... satisfying ∇ × y = 0". This is **inverted**: in the
  Helmholtz/Hodge decomposition `y = y_divfree + Grad·ψ`, the *irrotational*
  (curl-free, gradient-range) component is the `Grad·ψ` term that the projector
  *removes* — the comment names the removed part and its trivially-curl-free
  property (`∇ × ∇ψ = 0`) where it should describe the divergence-free
  *remainder* the projector returns. The authoritative L0 site is the **class**
  doc `palace/linalg/divfree.hpp:28-31` ("projection onto a divergence-free
  space satisfying `Gᵀ M x = 0`"), which the implementation
  (`palace/linalg/divfree.cpp:155-190`) realises; Palace's own inline comment at
  `palace/linalg/divfree.cpp:176` ("Compute the irrotational portion of y and
  subtract.") confirms the irrotational component is the *subtracted* part. The
  rewrite honours the *implemented* divergence-free semantics; the per-method
  comment is not a citation against the divergence-free claim.
- **Inner `ksp_solve` is a nested constructed-operator gate.** `P.ksp :
  Solver[P.M]` means this theme's closure carries another L1 constructed-operator
  as a sub-field — an instance of the
  [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
  shape. The CG iteration is interior to [`ksp_solve`](../L1/ksp_solve.md) and is
  the standard Krylov sequential obstruction; it does not leak into this theme
  (the concept's cross-layer fidelity rule). This is **not** a shape unique to
  this theme: the firm [`eigsolve-mutation-rotation`](./eigsolve-mutation-rotation.md)
  theme (sub-pattern B, `book/src/L1-L0/eigsolve-mutation-rotation.md:213-258`;
  the **core sub-pattern** of that theme, lowering ten `opInv->Mult` inner-solve
  call sites through the firm `ksp-solve-mutation-rotation` theme) is the prior
  and richer instance — its closure carries **two** nested gates
  (`E.linear`, `E.projector`; [`L1/eigsolve`](../L1/eigsolve.md) §Shape contract
  `E` at `:60`, prose-named "the first L1 operator to compose two layers of
  constructed-operator absorption" at `book/src/L1/eigsolve.md:136`, and
  "composed-not-inherited" at `:140`). Divfree is the **second** gate-carrying
  theme (after eigsolve), carrying the **third** nested gate overall (one gate
  of its own, after eigsolve's two). Because `E.projector` is this projector itself, the two confirmed
  instances are transitively nested three-deep (eigsolve ⊃ divfree ⊃ ksp). See
  the [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
  concept page for the full instance index, the latent `ksp_solve`-preconditioner
  site, and the fidelity rule.

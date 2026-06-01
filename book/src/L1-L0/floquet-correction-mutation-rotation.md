# floquet-correction-mutation-rotation

The mutation rotation for the Floquet B-field correction apply. Lowers the pure
L1 form [`floquet_correction`](../L1/floquet-correction.md) —
`y = floquet_correction(F, x) = F.M_RT⁻¹ · F.Cross · x` — into Palace's L0
`FloquetCorrSolver<ComplexVector>::Mult(const VecType &x, VecType &y)` member
method, plus the apply-and-accumulate `AddMult(const VecType &x, VecType &y,
ScalarType a)` member method and the construction-bound `FloquetCorrSolver(...)`
constructor that materialises the L1 closure fields. Narrated forward: the L1
pure out-of-place linear map dissolves into the L0 output-argument mutation
idiom (writes through `y`, scribbles construction-bound scratch member `rhs`)
over a constructed-operator value whose fields (`M`, `Cross`, `ksp`) are
assembled once at solver setup.

## Slug

`floquet-correction-mutation-rotation`

## L1 form (LHS)

The pure-functional Floquet correction consumes the prior `x` as a value and
produces a fresh RT-space field over an opaque constructed corrector `F`
(`FloquetCorrector[N_nd, N_rt]`, carrying `(M_RT, Cross, ksp)`):

    y = floquet_correction(F, x)
      = F.M_RT⁻¹ · F.Cross · x
        where M_RT⁻¹ solves  F.M_RT · y = rhs  via F.ksp
        and   rhs = F.Cross · x

The two composed steps at L1 (see
[`L1/floquet-correction`](../L1/floquet-correction.md) §Semantics):

1. `rhs = F.Cross · x`                — cross-product action (Nedelec → RT)
2. `y   = M_RT⁻¹ · rhs`, i.e. solve `F.M_RT · y = rhs` via `F.ksp`

The apply-and-accumulate companion at L1 is **not a separate operator** — it is
the firm composition with [`axpy`](../L1/axpy.md):

    y_new = y + a · floquet_correction(F, x) = axpy(a, floquet_correction(F, x), y)

At L1 there is **no destination buffer** (the correction returns a value), **no
scratch-buffer ownership** (`rhs` is absent from the signature), and **no
runtime element-type tag** — the closure is complex-only (only `<ComplexVector>`
is instantiated at L0; see Sub-pattern D).

## L0 form (RHS)

The rewrite splits into a **construction site** (the constructor that
materialises the closure fields), an **application site** (the `Mult` family
that realises the per-call correction by in-place mutation), an
**apply-and-accumulate site** (the `AddMult` family that fuses scaling and
accumulation onto the destination), and an **element-type scope-out**
(`<ComplexVector>` only). One L0 class (`FloquetCorrSolver<VecType>`) carries
the parametric `<VecType>` template parameter but instantiates only for
`ComplexVector` (sub-pattern D).

### Sub-pattern A — application via out-of-place `Mult(const VecType &x, VecType &y)`

    template <typename VecType>
    void FloquetCorrSolver<VecType>::Mult(const VecType &x, VecType &y) const
    {
      Cross->Mult(x, rhs);   // step 1: rhs = Cross · x
      ksp->Mult(rhs, y);     // step 2: M_RT · y = rhs (CG to tolerance)
    }

The L1 *value* `y` is the L0 `y` after `Mult(x, y)` returns. The crucial L0
facts the L1 form erases:

- **Destination-arg mutation.** `y` is the output argument; `ksp->Mult(rhs, y)`
  writes through it. The L1 form takes `x` as a value and returns a fresh `y`.
  Same output-arg idiom as
  [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md): the
  destination is named in the call's argument list, not on the LHS.
- **One scribbled scratch member.** `rhs` (the RT-side cross-product result) is
  a `mutable VecType` member (`palace/linalg/floquetcorrection.hpp:49`), sized
  once in the constructor (`palace/linalg/floquetcorrection.cpp:69-70`),
  written every call, carrying no value across calls. At L1 it vanishes — the
  correction is a single value-producing action. **Thinner than
  `divfree-projector`'s two-scratch (`psi`, `rhs`)** — only one buffer because
  no boundary-zeroing intermediate and no gradient-correction post-step are
  needed.
- **Construction-bound operators.** `Cross`, `ksp`, `M` are `std::unique_ptr`
  member fields set once in the constructor and read-only across calls; they
  are `F`'s captured closure fields at L1.
- **Inner solve is itself a constructed-operator gate.** `ksp->Mult(rhs, y)`
  (step 2) is the [`ksp_solve`](../L1/ksp_solve.md) inner RT mass solve. Its CG
  iteration is interior to `ksp_solve` and does not leak into this theme; here
  it is the opaque `M_RT⁻¹` action — the
  [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
  fidelity rule (the inner gate's iteration stays interior to its own lowering
  theme). This theme's closure carries another constructed-operator gate as a
  sub-field (`F.ksp : Solver[F.M_RT]`) — the **third firm instance** of the
  nested-gate shape (after `eigsolve-mutation-rotation`'s two-gate
  `E.linear`/`E.projector` carrying and
  `divfree-projector-mutation-rotation`'s one-gate `P.ksp` carrying). The
  `F.ksp` itself carries a `JacobiSmoother` preconditioner
  (`palace/linalg/floquetcorrection.cpp:65`) — which by
  [`solver-as-operator`](../concepts/solver-as-operator.md) is also a
  constructed-operator gate, so the floquet-corrector→ksp→jacobi-smoother chain
  is a transitive three-level nesting (parallel to the eigsolve→divfree→ksp
  chain documented in
  [`book/src/concepts/nested-constructed-operator-gate.md:91-102`](../concepts/nested-constructed-operator-gate.md)).
  See Open questions / caveats.

Justification kind: **structural** — re-bind the L1 output value into the L0
output destination buffer `y`; erase the scratch member `rhs`; the operators
are the construction-bound closure fields. The apply maps the two L1 composed
steps 1:1 onto the two L0 statement lines.

Citations:

- `palace/linalg/floquetcorrection.cpp:73-78` — `Mult(const VecType &x, VecType
  &y) const` (signature `:73-74`, opening brace `:75`, step 1 `:76`, step 2
  `:77`, close brace `:78`).
- `palace/linalg/floquetcorrection.hpp:49` — `mutable VecType rhs;` (the
  scratch member).
- `palace/linalg/floquetcorrection.hpp:58` — `void Mult(const VecType &x,
  VecType &y) const;` (the apply decl with `x` const-ref input and `y` ref
  output).

### Sub-pattern B — apply-and-accumulate via `AddMult(const VecType &x, VecType &y, ScalarType a)`

    template <typename VecType>
    void FloquetCorrSolver<VecType>::AddMult(const VecType &x, VecType &y, ScalarType a) const
    {
      this->Mult(x, rhs);   // y_arg = rhs (the scratch member, aliasing rebind)
      rhs *= a;             // scratch scaled in place
      y += rhs;             // accumulate onto destination
    }

The L0 `AddMult` body realises `y_new = y + a · (M_RT⁻¹ · [kp ×] · x)`. The L1
equivalent decomposes into the firm
[`floquet_correction`](../L1/floquet-correction.md) + [`axpy`](../L1/axpy.md)
pair:

    y_new = axpy(a, floquet_correction(F, x), y)

i.e. AddMult is NOT a separate L1 operator. The L0 body fuses the two L1
operators for buffer economy: rather than allocating a fresh RT-space result of
`Mult(x, ·)`, the body re-binds `Mult`'s output argument to the construction-bound
`rhs` scratch member (`this->Mult(x, rhs)` — *the same `rhs` that `Mult`'s body
uses as its step-1 cross-product intermediate*), then performs an in-place
`scal`-style scale (`rhs *= a`) and an `axpy`-style accumulate (`y += rhs`). The
L1 fusion is reversed at L1 into the two firm operators.

Crucial L0 fact the L1 fusion erases: **the inner `this->Mult(x, rhs)` call binds
`Mult`'s output destination to the same scratch member `rhs` that `Mult`'s body
uses as its step-1 cross-product intermediate**. Inside the nested call, the
sequence is `Cross->Mult(x, this->rhs); this->ksp->Mult(this->rhs, y_arg =
this->rhs);` — i.e. `ksp->Mult(b, x)` with `b == x` (the input RHS and the
output buffer are the same `VecType`). This implies a **load-bearing aliasing
applicability condition** (see Applicability conditions): the inner CG solver
must accept input/output aliasing on its argument vectors.

The inner ksp is reached through a delegation chain, and the aliasing tolerance
lives at the *bottom* of it, not at the top. `F.ksp` is a
`BaseKspSolver<OperType>` whose `Mult` (`palace/linalg/ksp.cpp:297`) is a **thin
delegation wrapper** — it opens a `BlockTimer` and forwards `ksp->Mult(x, y)`
(`palace/linalg/ksp.cpp:300`) verbatim to the wrapped inner solver, carrying no
aliasing logic of its own. The wrapped inner solver is a `CgSolver<OperType>`
(constructed at `palace/linalg/floquetcorrection.cpp:60`, wrapped into `F.ksp`
at `:66`). The **actual aliasing-tolerance mechanism** is in
`CgSolver<OperType>::Mult(const VecType &b, VecType &x) const`
(`palace/linalg/iterative.cpp:361`): because the floquet setup calls
`pcg->SetInitialGuess(0)` (`palace/linalg/floquetcorrection.cpp:61`), the
`initial_guess == false` precondition holds, so `CgSolver::Mult` takes its
else-branch (`palace/linalg/iterative.cpp:382-386`):

    else
    {
      r = b;      // :384 — copy RHS into the residual register FIRST
      x = 0.0;    // :385 — THEN zero the (possibly aliased) destination
    }

The `r = b;` at `:384` reads `b` into the residual register **before** the
`x = 0.0;` at `:385` zeros the destination — so even when `b` and `x` alias the
same buffer (`rhs`), the read of `b` completes before the write of `x`, and the
solve proceeds correctly. The tolerance is therefore **conditional**: it holds
*because* `SetInitialGuess(0)` selected the else-branch. Had `initial_guess`
been true, the if-branch (`palace/linalg/iterative.cpp:377-381`) would compute
`A->Mult(x, r)` — reading `x` before `r = b` — which under `b == x` aliasing
would read the not-yet-set RHS and break the fusion. This conditional aliasing
tolerance is the source of the buffer economy that the AddMult fusion exists
for; reversing the fusion at L1 requires the same applicability guarantee — and
the guarantee in turn rests on the `SetInitialGuess(0)` setup choice.

Justification kind: **algebraic** (the AddMult-into-axpy unfolding is the
`axpy(α, a, b) = a·α + b` definition with `a = floquet_correction(F, x)` and
`α = a` *plus* the structural buffer-economy claim that the L0 fusion uses the
scratch member as transient scaled-output buffer).

Citations:

- `palace/linalg/floquetcorrection.cpp:80-86` — `AddMult(const VecType &x,
  VecType &y, ScalarType a) const` (signature `:80-81`, body `:82-86` with
  `this->Mult(x, rhs)` at `:83`, `rhs *= a` at `:84`, `y += rhs` at `:85`,
  close brace `:86`).
- `palace/linalg/floquetcorrection.hpp:59` — `void AddMult(const VecType &x,
  VecType &y, ScalarType a = 1.0) const;` (decl; default `a = 1.0` makes the
  no-scale apply-and-accumulate `Mult-and-add`).
- `palace/linalg/ksp.cpp:297` — `BaseKspSolver<OperType>::Mult(const VecType
  &x, VecType &y) const` (the **delegation wrapper** on the aliased call-path:
  `:300` forwards `ksp->Mult(x, y)` to the inner CG solver; carries no aliasing
  logic itself — this is the call-path, not the mechanism).
- `palace/linalg/iterative.cpp:361` — `CgSolver<OperType>::Mult(const VecType
  &b, VecType &x) const` (the **true aliasing-tolerance mechanism**; signature
  `:361`, the `template` line is `:360`). With `initial_guess == false` the
  else-branch (`:382-386`) runs `r = b;` (`:384`) **before** `x = 0.0;` (`:385`),
  copying the RHS into the residual register before zeroing the aliased
  destination — so `b == x` aliasing is safe. The `if (this->initial_guess)`
  test is at `:377`; the aliasing-unsafe if-branch is `:377-381`.
- `palace/linalg/floquetcorrection.cpp:61` — `pcg->SetInitialGuess(0)` (the
  `initial_guess == false` **precondition** that gates the aliasing-safe
  else-branch; `pcg` is the `CgSolver` made at `:60`, wrapped into `F.ksp` at
  `:66`). The aliasing tolerance is conditional on this setup choice.

### Sub-pattern C — construction site: closure-field materialisation

The L1 closure `F = FloquetCorrector[N_nd, N_rt]` is the value the constructor
materialises (`palace/linalg/floquetcorrection.cpp:20-71`):

- `F.M_RT` ← RT vector-FE mass operator: a `BilinearForm` over the RT space
  with a coefficient-free `VectorFEMassIntegrator`, assembled with
  `skip_zeros = false`, wrapped as `ComplexParOperator` with `nullptr` imaginary
  part (`palace/linalg/floquetcorrection.cpp:26-39`). Real and SPD by
  construction (the RT mass matrix is the Gram matrix of the RT shape
  functions).
- `F.Cross` ← `[kp ×]` mixed mass operator (Nedelec → RT): a `BilinearForm`
  with two FE spaces (`nd_fespace, rt_fespace`) carrying a
  `MaterialPropertyCoefficient` constructed from
  `mat_op.GetAttributeToMaterial()` × `mat_op.GetFloquetCross()` (the
  per-attribute wave-vector cross-product matrix `mat_kx`) with a unit weight
  `1.0`, integrated by `VectorFEMassIntegrator`, assembled with
  `skip_zeros = false`, wrapped as `ComplexParOperator` with `nullptr`
  imaginary part and the trailing `false` (the asymmetric-trial-test-spaces
  hint) (`palace/linalg/floquetcorrection.cpp:41-57`).
- `F.ksp` ← a CG solver bound to `F.M_RT` as both operator and preconditioner
  target (`SetOperators(*M, *M)`), preconditioned by a `JacobiSmoother` (no
  BoomerAMG, no GMG — RT mass is well-conditioned so the diagonal-only Jacobi
  is sufficient), with the construction-time rel-tol, abs-tol = machine
  epsilon, and iteration cap (`palace/linalg/floquetcorrection.cpp:60-67`). The
  inner constructed-operator gate; see [`ksp_solve`](../L1/ksp_solve.md). **Key
  contrast with `divfree-projector`'s ksp setup**: divfree uses BoomerAMG (or
  GMG-wrapping-BoomerAMG) preconditioner; floquet uses JacobiSmoother. Both are
  CG; both bind operator-and-preconditioner-target to the same `M`. Captured
  at L1 as different `Solver[...]` closures with different per-instance content.
- `F` scratch ← `rhs`, sized to RT true-vsize and marked device-resident
  (`palace/linalg/floquetcorrection.cpp:69-70`). The L0 scratch member erased at
  L1 (sub-pattern A).

Justification kind: **structural** — the constructor is the
constructed-operator-gate construction step (same family as the
[`ksp-solve`](./ksp-solve-mutation-rotation.md) /
[`chebyshev-smoother`](./chebyshev-smoother-mutation-rotation.md) /
[`eigsolve`](./eigsolve-mutation-rotation.md) /
[`divfree-projector`](./divfree-projector-mutation-rotation.md) /
[`jacobi-smoother`](./jacobi-smoother-mutation-rotation.md) setup sites): the
L1 closure `F` is a pure function of the setup inputs `(mat_op, nd_fespace,
rt_fespace, tol, max_it, print)` modulo the opaque assembly/preconditioner-setup
machinery, which is below this theme's resolution (it is the
[`constructed-operator-factory`](../concepts/constructed-operator-factory.md)
concern).

Citations:

- `palace/linalg/floquetcorrection.cpp:20-23` — ctor signature.
- `palace/linalg/floquetcorrection.cpp:26-39` — `M_RT` assembly: comment
  `:25`, `BilinearForm a(rt_fespace)` `:28`, `VectorFEMassIntegrator` `:29`,
  `Assemble(skip_zeros)` `:30`, `ComplexParOperator` wrap with `nullptr` imag
  `:33`, real fallback `ParOperator` wrap `:37` (dead-code under the
  `<ComplexVector>`-only instantiation).
- `palace/linalg/floquetcorrection.cpp:41-57` — `Cross` assembly:
  `MaterialPropertyCoefficient f(mat_op.MaxCeedAttribute())` `:42`,
  `AddCoefficient(...)` with `mat_op.GetFloquetCross()` `:43`,
  `BilinearForm a(nd_fespace, rt_fespace)` `:45`, `VectorFEMassIntegrator(f)`
  `:46`, `Assemble(skip_zeros)` `:47`, `ComplexParOperator` wrap `:50-51`, real
  fallback `ParOperator` wrap `:55` (dead-code).
- `palace/linalg/floquetcorrection.cpp:60-66` — `ksp` setup: `CgSolver`
  constructor `:60`, `SetInitialGuess(0)` `:61`, `SetRelTol(tol)` `:62`,
  `SetAbsTol(epsilon())` `:63`, `SetMaxIter(max_it)` `:64`, `JacobiSmoother`
  preconditioner `:65`, `BaseKspSolver` wrap `:66`.
- `palace/linalg/floquetcorrection.cpp:67` — `ksp->SetOperators(*M, *M)`
  (operator and preconditioner-target both bound to `M_RT`).
- `palace/linalg/floquetcorrection.cpp:69-70` — `rhs.SetSize(rt_fespace.
  GetTrueVSize()); rhs.UseDevice(true);` (the scratch-member sizing).
- `palace/models/materialoperator.hpp:103,128` — the
  `GetFloquetCross(int attr)` per-attribute accessor + `GetFloquetCross()`
  all-attributes accessor.
- `palace/models/materialoperator.cpp:358` — `mat_kx(count).Set(1.0,
  wave_vector_cross);` (the per-attribute initialisation; `wave_vector_cross`
  is the skew-symmetric `3×3` matrix of `kp`).

### Sub-pattern D — element-type scope-out (`<ComplexVector>` only)

`FloquetCorrSolver<VecType>` is parametrically templated on `VecType` but
**instantiated only for `ComplexVector`** (`palace/linalg/floquetcorrection.cpp:88`):

    template class FloquetCorrSolver<ComplexVector>;

There is no `template class FloquetCorrSolver<Vector>;` line. This is a
deliberate scope-out: floquet periodicity is intrinsically a complex-valued
problem (the wave vector `kp` is a real spatial momentum, but its physical
action manifests on phase-modulated complex bloch fields), and only the driven
+ eigenmode pipelines call it — both pipelines work in `ComplexVector`. The
`if constexpr (std::is_same<OperType, ComplexOperator>::value)` branches in the
constructor (`palace/linalg/floquetcorrection.cpp:31,48`) carry both `complex`
and `real` paths textually, but only the complex path is reachable under the
`<ComplexVector>` instantiation.

The L1 signature reflects this directly: `x` and the result are both
`Field[N_nd, Complex]` / `Field[N_rt, Complex]`; there is no real-only mode.
**Contrast with `divfree-projector`** (real *and* complex both instantiated,
`palace/linalg/divfree.cpp:189-190`) and with `jacobi-smoother` (real *and*
complex both instantiated, `palace/linalg/jacobi.cpp` instantiations). The
`floquet_correction` is the **first L1 constructed-operator gate with a
deliberately-narrowed element-type scope**.

Justification kind: **structural** — the `<VecType>` template parameter is
parametric but the single L0 explicit instantiation pins the element-type
scope. The L1 form has one action; the parametric template is dead-code in any
hypothetical real-only client. There is no real-mode runtime branch to handle.

Citations:

- `palace/linalg/floquetcorrection.cpp:88` — `template class
  FloquetCorrSolver<ComplexVector>;` (the **sole** instantiation).
- `palace/linalg/floquetcorrection.cpp:31` — `if constexpr
  (std::is_same<OperType, ComplexOperator>::value)` (the complex-branch of the
  `M_RT` assembly; the reachable path).
- `palace/linalg/floquetcorrection.cpp:35-38` — `else { ... ParOperator ... }`
  (the real-branch dead-code).
- `palace/linalg/floquetcorrection.cpp:48` — second `if constexpr` (the
  complex-branch of the `Cross` assembly).
- `palace/linalg/floquetcorrection.cpp:53-56` — `else { ... ParOperator ... }`
  (the real-branch dead-code).
- `palace/drivers/drivensolver.cpp:138`, `:289`,
  `palace/drivers/eigensolver.cpp:237` — all three construction sites declare
  `std::unique_ptr<FloquetCorrSolver<ComplexVector>>` (no `<Vector>` use anywhere
  in the call-site cohort).

## Applicability conditions

The rewrite preserves semantics when:

1. **No aliasing between `x`, `y`, `rhs` at the `Mult` call.** `Mult(x, y)`
   reads `x` (step 1) and writes `rhs` (step 1) and writes `y` (step 2). The L1
   form takes the pre-call `x` as a value and owns no scratch, so the lowering
   must guarantee `rhs` is a distinct buffer from `x` and from `y`. Palace
   allocates `rhs` as a construction-bound member distinct from the caller's
   `x` and `y`. Inherited applicability-condition shape from
   [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md).
2. **Inner ksp accepts input/output aliasing (conditional on `SetInitialGuess(0)`).**
   The `AddMult` body's nested `this->Mult(x, rhs)` call binds `Mult`'s output
   argument to the scratch member, and `Mult`'s step-2 body `ksp->Mult(rhs,
   y_arg = rhs)` therefore calls the inner ksp with `b == x` (input RHS and
   output destination aliased to the same buffer). The inner `BaseKspSolver::Mult`
   (`palace/linalg/ksp.cpp:297`) is a thin delegation wrapper that forwards to
   `ksp->Mult(x, y)` (`:300`); the wrapped `CgSolver<OperType>::Mult`
   (`palace/linalg/iterative.cpp:361`) is what tolerates the aliasing — **but
   only because** `pcg->SetInitialGuess(0)` (`palace/linalg/floquetcorrection.cpp:61`)
   sets `initial_guess == false`, selecting the else-branch
   (`palace/linalg/iterative.cpp:382-386`) which copies `r = b;` (`:384`) before
   `x = 0.0;` (`:385`) — reading the RHS into the residual register before
   zeroing the aliased destination. **A lowering that re-derives the inner solve
   with `initial_guess == true` (the if-branch `:377-381`, which computes
   `A->Mult(x, r)` and reads `x` first) breaks the AddMult fusion under
   aliasing.** This condition is **specific to this theme** (the
   divfree-projector AddMult-free apply does not have this concern) and its
   safety rests on the `SetInitialGuess(0)` construction-time choice.
3. **No observer of prior `y` after the in-place call.** `Mult(x, y)` writes
   `y` (the destination is overwritten with the new value); `AddMult` reads
   `y` (the destination is accumulated onto with the correction). If a
   downstream op reads `y_old` after `Mult`, the in-place form is invalid; at
   L1 `y_old` is still in scope as a separate value. Upheld at all four
   `AddMult` call sites by lexical sequencing (the `AddMult` follows a `B *=
   −1.0/(1i*omega)` rescale that already finished writing to `B`, then `AddMult`
   adds to `B` once and `B` is consumed by the next post-processing step).
4. **Closure immutability across calls.** `F` (`M_RT`, `Cross`, `ksp`) is set
   once in the constructor and read-only across `Mult`/`AddMult` calls. There
   is no per-call control input — the L1 form is a fixed linear map on its
   single field argument.
5. **Step ordering is load-bearing.** The sequence `Cross → ksp` must not be
   reordered: cross-product before mass-solve is the only meaningful sequence
   (`Mult` body lines `:76-77`).
6. **Element-type conformance (single).** Only `<ComplexVector>` is
   instantiated (`palace/linalg/floquetcorrection.cpp:88`). A lowering that
   tries to instantiate `<Vector>` (a hypothetical real-only client) hits the
   constructor's `if constexpr` real branches (which exist as dead-code at
   `:35-38, :53-56`) but cannot proceed — there are no real-typed driver call
   sites in Palace; the construction-site declarations at
   `palace/drivers/drivensolver.cpp:138,289` and
   `palace/drivers/eigensolver.cpp:237` all bind `<ComplexVector>`. **A
   lowering instantiating `<Vector>` is out-of-evidence; it requires a positive
   driver site.**
7. **Wave vector is real-valued and spatially constant per material.** The
   `mat_op.GetFloquetCross()` returns a per-attribute `3×3` skew-symmetric
   matrix of the wave vector (`palace/models/materialoperator.cpp:358`); the
   wave vector itself is a real `mfem::Vector` (the `wave_vector_cross` member
   is `mfem::DenseMatrix`, `palace/models/materialoperator.hpp:35`). The L1
   form treats `[kp ×]` as a fixed linear map; if the wave vector becomes
   complex-valued or spatially varying *within* a material attribute, the
   integrator construction would have to change.
8. **Single-machine scope.** The `MPI_Comm` machinery in the ksp setup
   (`rt_fespace.GetComm()`, `palace/linalg/floquetcorrection.cpp:60,65`) is
   read as its single-rank equivalent (MPI distribution out of scope, flagged
   once). The `MPI_Comm` does not appear in the L1 signature.

## Justification kind

- **Sub-pattern A** (out-of-place apply) — `structural`. Output-arg `y` re-bind +
  scratch `rhs` erasure; 1:1 step mapping.
- **Sub-pattern B** (apply-and-accumulate) — `algebraic` (AddMult unfolds into
  `axpy ∘ floquet_correction`) + `structural` (the L0 buffer economy uses the
  scratch as transient scaled-output buffer; the aliasing applicability is
  load-bearing).
- **Sub-pattern C** (construction) — `structural`. Constructed-operator-gate
  closure materialisation; pure-of-inputs modulo opaque assembly/preconditioner
  setup.
- **Sub-pattern D** (element-type scope-out) — `structural`. `<ComplexVector>`-only
  single explicit instantiation; the parametric template is dead-code in any
  hypothetical real-only client.

The theme as a whole is `structural` with one algebraic sub-rule (the AddMult-as-axpy
identity in B). A `lowering-verifier` audit in a later cycle should confirm
all four sub-patterns match the L0 corpus exhaustively (the `<ComplexVector>`
sole instantiation, the Mult + AddMult entry points, all four AddMult call
sites, all three construction sites).

## Speculative L1 operators

None. The L1 anchor [`L1/floquet-correction`](../L1/floquet-correction.md) is
firm, and all its sub-dependencies are firm L1 operators / firm concepts:
[`apply_linop`](../L1/apply_linop.md) (the `Cross · x` step),
[`ksp_solve`](../L1/ksp_solve.md) (the inner RT mass solve),
[`jacobi-smoother`](../L1/jacobi-smoother.md) (the inner CG preconditioner),
[`axpy`](../L1/axpy.md) (the AddMult-as-axpy composition).

This theme proposes no new vocabulary.

## Verified-against

L0 evidence ranges (all verified via `citecheck` this cycle, 2026-05-31):

- `palace/linalg/floquetcorrection.cpp:20-71` — constructor body (sig `:20-23`,
  M assembly `:26-39`, Cross assembly `:41-57`, ksp+JacobiSmoother
  setup+SetOperators `:60-67`, scratch sizing `:69-70`, close brace `:71`).
- `palace/linalg/floquetcorrection.cpp:73-78` — `Mult(const VecType &x,
  VecType &y) const` two-step body.
- `palace/linalg/floquetcorrection.cpp:80-86` — `AddMult(const VecType &x,
  VecType &y, ScalarType a) const` apply-and-accumulate body.
- `palace/linalg/floquetcorrection.cpp:88` — `template class
  FloquetCorrSolver<ComplexVector>;` (sole instantiation).
- `palace/linalg/floquetcorrection.hpp:32-60` — class declaration.
- `palace/linalg/floquetcorrection.hpp:42-43` — `std::unique_ptr<OperType> M,
  Cross;`.
- `palace/linalg/floquetcorrection.hpp:46` — `std::unique_ptr<BaseKspSolver<OperType>>
  ksp;`.
- `palace/linalg/floquetcorrection.hpp:49` — `mutable VecType rhs;`.
- `palace/linalg/floquetcorrection.hpp:52-53` — constructor decl.
- `palace/linalg/floquetcorrection.hpp:58-59` — `Mult` and `AddMult` decls.
- `palace/linalg/ksp.cpp:297` — `BaseKspSolver<OperType>::Mult` (the
  **delegation wrapper** on the aliased AddMult call-path; `:300` forwards to
  the inner CG solver, carrying no aliasing logic itself).
- `palace/linalg/iterative.cpp:360-386` — `CgSolver<OperType>::Mult` (the
  **true aliasing-tolerance mechanism** the AddMult fusion requires; signature
  `:361`, `if (this->initial_guess)` `:377`, aliasing-safe else-branch
  `:382-386` with `r = b;` `:384` before `x = 0.0;` `:385`).
- `palace/linalg/floquetcorrection.cpp:61` — `pcg->SetInitialGuess(0)` (the
  `initial_guess == false` precondition that gates the aliasing-safe
  else-branch; makes the AddMult aliasing tolerance load-bearing-safe).
- `palace/models/materialoperator.hpp:103,128` — `GetFloquetCross` accessors.
- `palace/models/materialoperator.cpp:358` — `mat_kx(count).Set(1.0,
  wave_vector_cross)`.
- `palace/drivers/drivensolver.cpp:138-143` — first construction site.
- `palace/drivers/drivensolver.cpp:208-213` — first AddMult call site.
- `palace/drivers/drivensolver.cpp:289-294` — second construction site.
- `palace/drivers/drivensolver.cpp:332-337` — second AddMult call site.
- `palace/drivers/drivensolver.cpp:464-469` — third AddMult call site.
- `palace/drivers/eigensolver.cpp:237-243` — eigenmode construction site.
- `palace/drivers/eigensolver.cpp:450-455` — eigenmode AddMult call site.
- `test/unit/test-schema.cpp:340-353` — JSON schema validation for
  `FloquetWaveVector`.
- `test/examples/runtests.jl:289-294` — `cylinder/floquet` end-to-end
  regression example.

L1 anchor:

- `book/src/L1/floquet-correction.md` — the firm L1 operator all four
  sub-patterns lower from.

## Status

`firm`.

Every sub-pattern reads from a positive Palace source site verified via
`citecheck` this cycle:

- the out-of-place output-arg apply with scratch-member threading (A,
  `palace/linalg/floquetcorrection.cpp:73-78`),
- the apply-and-accumulate AddMult-as-axpy fusion (B,
  `palace/linalg/floquetcorrection.cpp:80-86`),
- the constructed-operator-gate closure materialisation (C,
  `palace/linalg/floquetcorrection.cpp:20-71`),
- the `<ComplexVector>`-only element-type scope-out (D,
  `palace/linalg/floquetcorrection.cpp:88`).

The single load-bearing algebraic sub-rule — the AddMult-as-axpy unfolding —
follows from the algebraic identity `axpy(α, a, b) = α·a + b` applied to the
`(α=a, a=floquet_correction(F, x), b=y)` instantiation visible in the L0 body
lines `:83-85`.

**No partly-constructive caveat applies.** This theme has a positive source
site for every step, including the AddMult fusion's load-bearing aliasing
applicability — its positive mechanism site is `CgSolver<OperType>::Mult`
(`palace/linalg/iterative.cpp:361`, the aliasing-safe else-branch
`:382-386` runs `r = b;` (`:384`) before `x = 0.0;` (`:385`)), gated by the
`pcg->SetInitialGuess(0)` precondition (`palace/linalg/floquetcorrection.cpp:61`);
`palace/linalg/ksp.cpp:297` is the `BaseKspSolver::Mult` delegation wrapper on
the call-path (it forwards `ksp->Mult(x, y)` at `:300`), not the mechanism. The L1
anchor is firm-on-positive-structure (the `divfree-projector` / `jacobi-smoother`
/ `chebyshev-smoother` precedent), so this theme is firm at birth.

A `lowering-verifier` exhaustiveness audit (`<ComplexVector>` sole
instantiation × `Mult` + `AddMult` entry points × all 4 driver call sites × all
3 construction sites) is the standard follow-up, not a status reduction.

## Open questions / caveats

- **Theme's closure carries a transitively-three-deep nested gate
  (`F.ksp.preconditioner = JacobiSmoother`).** Parallel to the
  eigsolve→divfree→ksp chain at
  `book/src/concepts/nested-constructed-operator-gate.md:91-102`, the floquet
  closure's `F.ksp` (`palace/linalg/floquetcorrection.cpp:66`) carries a
  JacobiSmoother preconditioner (`:65`), which is itself a firm L1
  constructed-operator gate
  ([`jacobi-smoother`](../L1/jacobi-smoother.md)). By the
  [`solver-as-operator`](../concepts/solver-as-operator.md) rotation, this is
  a three-level nesting:
  
      floquet-corrector  ⊃  ksp_solve  ⊃  jacobi-smoother
        (F)                  (F.ksp)        (F.ksp.preconditioner)
  
  The fidelity rule applies at each edge: this theme treats `F.ksp` opaquely;
  the ksp-solve-mutation-rotation theme treats `F.ksp.preconditioner`
  opaquely; the jacobi-smoother-mutation-rotation theme treats `F.M_RT`'s
  diagonal-extraction step opaquely (concept-page §latent-site language). This
  is the **second three-level transitive nesting in the firm artifact** (after
  the eigsolve→divfree→ksp chain), confirming the concept's
  cross-layer-fidelity rule is load-bearing across two independent pipelines.
  **Concept-page §Firm-instances upgrade**: 2 firm → 3 firm
  (eigsolve + divfree + floquet-correction); the transitive-nesting note
  should mention the second three-deep chain.
- **`<Vector>` real-only path is dead-code under the
  `<ComplexVector>`-only-instantiation.** The constructor's `if constexpr` real
  branches at `palace/linalg/floquetcorrection.cpp:35-38, 53-56` are present
  textually but unreachable given the sole `template class
  FloquetCorrSolver<ComplexVector>;` at `:88`. This is a documentation-internal
  inconsistency (the parametric template invites a `<Vector>` instantiation
  the L0 doesn't supply); not a defect — it is a deliberate scope-out captured
  at Sub-pattern D. **OQ**: `floquet-correction-real-vector-instantiation-dead-code`
  (note for a future harvester / lowering-verifier — confirm no upstream Palace
  PR is in flight to add `<Vector>` instantiation).
- **The AddMult buffer-economy aliasing is theme-specific.** The
  `this->Mult(x, rhs)` re-binding pattern (sub-pattern B's load-bearing
  aliasing applicability) does not appear in any of the four sister themes —
  divfree, jacobi, chebyshev, ksp_solve don't have an AddMult surface that
  re-uses the construction-bound scratch as Mult's destination. This is a
  unique L0 idiom of `FloquetCorrSolver` and deserves a verified_against audit
  pass.
- **Lifting note (reverse direction — working notes only, NOT in the formal
  chapter).** An L0 in-place floquet-corrector apply (output-arg mutation +
  one scratch member + construction-bound operator reads) lifts to the L1
  pure correction by: (i) re-binding the output arg `y` to the return value,
  (ii) erasing the `rhs` scratch member, (iii) capturing the
  construction-bound operators as the closure `F`, (iv) unfolding `AddMult`
  into `axpy ∘ floquet_correction`. The lift requires the no-aliasing +
  no-prior-`y`-observer guarantees (Applicability conditions 1, 3) and the
  inner-ksp aliasing tolerance (Applicability condition 2) to hold at every
  call site; all four `AddMult` call sites uphold this by lexical sequencing
  (the `B *= -1.0/(1i*omega)` rescale precedes the `AddMult` which then
  consumes its result; no upstream caller observes the prior `B`). This
  reverse note is recorded here, not in the high→low formal theme content
  (per CLAUDE.md §Methodology invariants "Layers are defined high→low").

```yaml
verified_against:
  # Sub-pattern A — out-of-place apply (Mult)
  - citation: palace/linalg/floquetcorrection.cpp:73-78
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: Mult(const VecType &x, VecType &y) const two-step body; sig :73-74, brace :75, Cross->Mult(x, rhs) :76, ksp->Mult(rhs, y) :77, close :78 — matches theme transcription verbatim (citecheck OK, anchors lit).
  - citation: palace/linalg/floquetcorrection.hpp:49
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: mutable VecType rhs; the single scribbled scratch member confirmed at :49 (citecheck OK).
  - citation: palace/linalg/floquetcorrection.hpp:58
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: void Mult(const VecType &x, VecType &y) const; apply decl with const-ref x input and ref y output confirmed at :58 (citecheck OK).
  # Sub-pattern B — apply-and-accumulate (AddMult) + the load-bearing inner-ksp aliasing applicability
  - citation: palace/linalg/floquetcorrection.cpp:80-86
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: AddMult body; this->Mult(x, rhs) :83 (output rebind to scratch member), rhs *= a :84, y += rhs :85 — the axpy-into-floquet fusion reads verbatim; the algebraic axpy(a, floquet_correction(F,x), y) unfolding is the literal :83-85 body (citecheck OK).
  - citation: palace/linalg/floquetcorrection.hpp:59
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: void AddMult(const VecType &x, VecType &y, ScalarType a = 1.0) const; default a=1.0 (no-scale Mult-and-add) confirmed at :59 (citecheck OK).
  - citation: palace/linalg/ksp.cpp:297
    verdict: supports
    audited_at: 2026-05-31T215306Z
    note: BaseKspSolver<OperType>::Mult :297 is the DELEGATION WRAPPER (call-path, not mechanism) — :299 BlockTimer, :300 ksp->Mult(x,y) forwards verbatim to the inner CgSolver::Mult. Re-anchored cycle-039 D2 — the AddMult aliasing-tolerance MECHANISM is at CgSolver::Mult, see the iterative.cpp:360-386 and floquetcorrection.cpp:61 rows below (citecheck OK).
  - citation: palace/linalg/iterative.cpp:360-386
    verdict: supports
    audited_at: 2026-05-31T215306Z
    note: CgSolver<OperType>::Mult(const VecType &b, VecType &x) sig at :361 (:360 is the template line; planner hinted :360 — +1 drift corrected to :361) — the TRUE aliasing-tolerance mechanism. With initial_guess==false the else-branch :382-386 runs r = b; (:384) x = 0.0; (:385) — copies b into r BEFORE zeroing the aliased x, so when AddMult passes b==x==rhs the read of b precedes the write of x and aliasing is safe. The if(this->initial_guess) test is at :377; the aliasing-unsafe if-branch is :377-381. citecheck OK on :361/:377/:384/:385.
  - citation: palace/linalg/floquetcorrection.cpp:61
    verdict: supports
    audited_at: 2026-05-31T215306Z
    note: pcg->SetInitialGuess(0) sets the initial_guess==false precondition that gates the CgSolver::Mult else-branch — without it the if-branch at iterative.cpp:377-381 reads x (A->Mult(x,r)) before r is set, which WOULD break b==x aliasing. This SetInitialGuess(0) is what makes the AddMult aliasing tolerance load-bearing-safe (citecheck OK, anchor lit).
  # Sub-pattern C — construction-site closure materialisation
  - citation: palace/linalg/floquetcorrection.cpp:20-71
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: ctor body; sig :20-23, M assembly :26-39 (ComplexParOperator wrap :33 / dead-code ParOperator :37), Cross assembly :41-57 (MaterialPropertyCoefficient :42, GetFloquetCross :43, ComplexParOperator :50-51 / dead-code :55), ksp+JacobiSmoother :60-66 (CgSolver :60, JacobiSmoother :65), SetOperators(*M,*M) :67, rhs sizing :69-70 — all finer anchors lit (citecheck OK). M-block comment anchored at :25 (the comment line; :26 is the opening brace) — tightened from the earlier :25-26 over-extension (cycle-040 D3).
  - citation: palace/linalg/floquetcorrection.cpp:67
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: ksp->SetOperators(*M, *M) — operator and preconditioner-target both bound to the RT mass M_RT, confirmed at :67 (citecheck OK).
  - citation: palace/linalg/floquetcorrection.hpp:42-43
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: std::unique_ptr<OperType> M, Cross; construction-bound closure operator fields confirmed at :42-43 (citecheck OK).
  - citation: palace/linalg/floquetcorrection.hpp:46
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: std::unique_ptr<BaseKspSolver<OperType>> ksp; inner constructed-operator-gate field confirmed at :46 (citecheck OK).
  - citation: palace/linalg/floquetcorrection.hpp:52-53
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: FloquetCorrSolver(...) constructor decl confirmed at :52-53 (citecheck OK).
  - citation: palace/models/materialoperator.hpp:103,128
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: GetFloquetCross per-attribute (:103) and all-attributes (:128) accessors both lit (citecheck OK).
  - citation: palace/models/materialoperator.cpp:358
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: mat_kx(count).Set(1.0, wave_vector_cross); per-attribute skew-symmetric wave-vector cross-product init confirmed at :358 (citecheck OK).
  - citation: palace/models/materialoperator.hpp:35
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: wave_vector_cross member (mfem::DenseMatrix, real-valued) confirmed at :35 — substantiates Applicability condition 7 (wave vector real-valued, spatially constant per material) (citecheck OK).
  # Sub-pattern D — element-type scope-out (<ComplexVector> only)
  - citation: palace/linalg/floquetcorrection.cpp:88
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: template class FloquetCorrSolver<ComplexVector>; the SOLE explicit instantiation — no <Vector> line anywhere; the scope-out is positively witnessed (citecheck OK).
  - citation: palace/linalg/floquetcorrection.cpp:31
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: first if constexpr (std::is_same<OperType, ComplexOperator>::value) — the reachable complex branch of M_RT assembly, anchor lit at :31 (citecheck OK).
  - citation: palace/linalg/floquetcorrection.cpp:35-38
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: else { ... ParOperator ... } real-branch dead-code of M_RT assembly confirmed at :35-38 (unreachable under <ComplexVector>-only instantiation) (citecheck OK).
  - citation: palace/linalg/floquetcorrection.cpp:48
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: second if constexpr — the reachable complex branch of Cross assembly, anchor lit at :48 (citecheck OK).
  - citation: palace/linalg/floquetcorrection.cpp:53-56
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: else { ... ParOperator ... } real-branch dead-code of Cross assembly confirmed at :53-56 (citecheck OK).
  - citation: palace/drivers/drivensolver.cpp:138-143
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: first construction site; std::unique_ptr<FloquetCorrSolver<ComplexVector>> :138 + make_unique<...<ComplexVector>> :141 — binds <ComplexVector>, no <Vector> (citecheck OK; corroborates Sub-pattern D and Applicability condition 6).
  - citation: palace/drivers/drivensolver.cpp:289-294
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: second construction site; same <ComplexVector> binding at :289/:292 (citecheck OK).
  - citation: palace/drivers/eigensolver.cpp:237-243
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: eigenmode construction site; <ComplexVector> binding at :237/:240 (citecheck OK).
  # AddMult call-site cohort (all four) — the apply-and-accumulate witnesses + Applicability condition 3 lexical sequencing
  - citation: palace/drivers/drivensolver.cpp:208-213
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: first AddMult call site floquet_corr->AddMult(E, B, 1.0/omega) :212, preceded by B *= -1.0/(1i*omega) at :207 — confirms Applicability condition 3 (prior B fully written by rescale before AddMult accumulates; no prior-y observer) (citecheck OK).
  - citation: palace/drivers/drivensolver.cpp:332-337
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: second AddMult call site AddMult(E, B, 1.0/omega) :336 (citecheck OK).
  - citation: palace/drivers/drivensolver.cpp:464-469
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: third AddMult call site AddMult(E, B, 1.0/omega) :468 (citecheck OK).
  - citation: palace/drivers/eigensolver.cpp:450-455
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: fourth AddMult call site AddMult(E, B, 1.0/omega) :454, preceded by B *= -1.0/(1i*omega) at :449 — confirms condition 3 lexical sequencing on the eigen path (citecheck OK). Four AddMult call sites total — theme exhaustiveness claim confirmed.
  # Test / regression supplements (L0-equivalent semantic documentation)
  - citation: test/unit/test-schema.cpp:340-353
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: SECTION("FloquetWaveVector must be array") JSON-schema validation for the Periodic FloquetWaveVector config at :340-353 — supporting (config-surface) evidence, not a per-rewrite anchor (citecheck OK).
  - citation: test/examples/runtests.jl:289-294
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: cylinder/floquet periodic end-to-end regression at :289-294 (testcase "cylinder","floquet.json","floquet") — L0-equivalent semantic supplement (citecheck OK).
  # L1 anchor
  - citation: book/src/L1/floquet-correction.md
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: the firm L1 floquet_correction operator all four sub-patterns lower from; firm at cycle-036 D1 (sibling-theme L1-anchor convention).
```

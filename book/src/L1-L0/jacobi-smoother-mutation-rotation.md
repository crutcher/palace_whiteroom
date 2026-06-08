# jacobi-smoother-mutation-rotation

The mutation rotation for the single-elementwise-product Jacobi (diagonal)
smoother action. Lowers the pure L1 form
[`jacobi_smoother`](../L1/jacobi-smoother.md) — `y = jacobi_smoother(op, x) =
(ω · D⁻¹) ⊙ x` — into Palace's in-place L0 `Mult(x, y)` member-call on the
`JacobiSmoother<OperType>` template class, plus the construction-bound
`SetOperator` setup that materialises the L1 closure field
`op.dinv = ω · diag(A)⁻¹`. Narrated forward: the L1 pure action dissolves
into the L0 output-argument mutation idiom (writes through `y` via the
namespace-local `Apply(dinv, x, y)` kernel) over a construction-bound
inverse-diagonal capture. The *thinnest* constructed-operator-gate mutation
rotation at L1>L0 — no workspace, no `pc_it` sweep, no `apply_linop` call,
no residual; just one elementwise multiply per call.

## Slug

`jacobi-smoother-mutation-rotation`

## L1 form (LHS)

The pure-functional smoother action returns a fresh `Tensor[N]` from the
input `x` and the constructed-operator closure `op`
([`L1/jacobi-smoother`](../L1/jacobi-smoother.md) §Signature):

    y = jacobi_smoother(op, x)
      = op.dinv ⊙ x
      = (ω · D⁻¹) ⊙ x                  -- D = diag(A); ω absorbed into op.dinv

The closure `op = JacobiSmoother[N]` carries `(dinv, omega, sf_max)`; the
captured operator `A` itself is **forgotten** once `dinv` is committed
(the closure carries the reduced operator content only). `op` is itself the
value produced by a pure *setup* sub-action of `(A, omega, sf_max)` modulo
the opaque `spectrum_estimate(A, dinv)` on the `omega == 0.0` path (see
[`L1/jacobi-smoother`](../L1/jacobi-smoother.md) §Signature, §Dependencies).
At L1 there is no destination buffer, no workspace, no `initial_guess`
parameter, and no per-call branch on element-type or damping-mode — both
variant axes are absorbed into the closure.

## L0 form (RHS)

The rewrite splits into a **construction site** (the `SetOperator` step that
materialises the closure field `dinv` from the operator, plus the
optional damping-estimation arithmetic) and an **application site** (the
`Mult` entry point that dispatches to the namespace-local `Apply(dinv, x, y)`
kernel). The shape is structurally identical to the
[`chebyshev-smoother-mutation-rotation`](./chebyshev-smoother-mutation-rotation.md)
construction site (same `op.AssembleDiagonal(dinv); dinv.Reciprocal();`
diagonal-prep chain, same `GetLambdaMax` spectral-estimate sub-action),
*minus* the polynomial sweep — Jacobi's apply is a single elementwise
multiply.

### Sub-pattern A — construction site (`SetOperator`): closure-field materialisation

    void JacobiSmoother<OperType>::SetOperator(const OperType &op)
    {
      dinv.SetSize(op.Height());
      dinv.UseDevice(true);
      op.AssembleDiagonal(dinv);                 // dinv = diag(A)
      dinv.Reciprocal();                         // dinv = 1 / diag(A)
      if (omega == 0.0) {                        // estimated-damping branch
        auto lambda_max = GetLambdaMax(comm, op, dinv);    // sub-pattern C
        auto lambda_min = (sf_max - 1.0) * lambda_max;
        omega = 2.0 / (lambda_min + lambda_max);           // optimal damping
      }
      if (omega != 1.0) {                        // damping-fold (transparent ω=1 fast path)
        dinv *= omega;                           // dinv = ω · D⁻¹
      }
      this->height = op.Height();
      this->width = op.Width();
    }

The L1 closure `op = JacobiSmoother[N]` is the value `SetOperator`
materialises:

- `op.dinv` ← `AssembleDiagonal(dinv); dinv.Reciprocal()` — assemble
  `diag(A)` into `dinv`, then elementwise-reciprocate to `1 / diag(A)`. The
  diagonal-extraction step reuses the L1
  [`assemble_diagonal`](../L1/assemble_diagonal.md) operator via its L1>L0
  lowering [`assemble-diagonal-mutation-rotation`](./assemble-diagonal-mutation-rotation.md);
  the reciprocal step is the elementwise [`reciprocal`](../L1/reciprocal.md)
  primitive (firm L1 leaf).
- `op.omega` ← either the ctor-given `omega` (default `1.0`; arbitrary `ω ≠ 0`
  honored as-is) or, on the `omega == 0.0` branch, the **substituted**
  `ω = 2 / (lambda_min + lambda_max) = 2 / (sf_max · lambda_max)` from the
  spectral-estimate sub-action. After the setup-body completes, `omega` is
  **already absorbed into `dinv`** by the `dinv *= omega` step (L1 law 3);
  the closure carries `omega` only for introspection.
- `op.sf_max` ← the ctor-given scaling factor (default `1.0`); used only on
  the `omega == 0.0` setup path to shift `lambda_min`.

The setup is a **pure function of inputs `(A, omega, sf_max)`** modulo the
opaque `spectrum_estimate(A, dinv)` call — exactly the same structure as the
chebyshev-smoother setup (same opaque sub-action; see sub-pattern C below).
The `dinv.SetSize(op.Height())` + `dinv.UseDevice(true)` lines are L0
buffer-mechanic preconditions for the elementwise kernels; the L1 form drops
them (the L1 `Tensor[N]` carries its own length axis).

The `omega == 1.0` fast-path skip (avoid the `dinv *= omega` element loop) is
a **transparent performance trick** — algebraically identical to
`dinv *= 1.0`. The `omega != 0.0` branch (a non-default `ω` set
externally) folds the damping in via the same `dinv *= omega` step; the L1
law 3 (`jacobi_setup(A, ω, ·) = scale(ω, jacobi_setup(A, 1.0, ·))`) holds at
the closure level.

Justification kind: **structural** — `SetOperator` is the
constructed-operator-gate construction step (same family as the
[`chebyshev-smoother-mutation-rotation`](./chebyshev-smoother-mutation-rotation.md)
sub-pattern D / [`ksp-solve-mutation-rotation`](./ksp-solve-mutation-rotation.md)
setup sites). The L1 closure is a pure function of the setup inputs modulo
the opaque `spectrum_estimate`. The `omega == 0.0` arithmetic is closed-form
(witnessed below); no per-call branch survives the closure-commit.

Citations:
- `palace/linalg/jacobi.cpp:74-97` — `JacobiSmoother<OperType>::SetOperator`
  signature-to-close. The `dinv.SetSize(op.Height())` @77, `dinv.UseDevice(true)` @78,
  `op.AssembleDiagonal(dinv)` @79, `dinv.Reciprocal()` @80, the `omega == 0.0`
  branch @84-89 (`lambda_max = GetLambdaMax(comm, op, dinv)` @86, `lambda_min =
  (sf_max - 1.0) * lambda_max` @87, `omega = 2.0 / (lambda_min + lambda_max)`
  @88), the damping-fold `if (omega != 1.0) { dinv *= omega; }` @90-93, the
  `this->height = op.Height(); this->width = op.Width();` base-contract assign
  @95-96.
- `palace/linalg/jacobi.hpp:39` — `void SetOperator(const OperType &op) override;`
  — the override declaration.
- `palace/linalg/jacobi.hpp:28` — `VecType dinv;` — the inverse-diagonal
  member (`VecType = Vector` for real `OperType = Operator`,
  `= ComplexVector` for complex `OperType = ComplexOperator`; the closure
  field that the per-call apply reads).
- `palace/linalg/jacobi.hpp:31` — `double omega, sf_max;` — the
  damping-mode + spectral-bound-scaling closure fields (read on the
  `omega == 0.0` branch, absorbed into `dinv` on the `omega != 1.0` branch).
- `palace/linalg/jacobi.hpp:34` — `JacobiSmoother(MPI_Comm comm, double
  omega = 1.0, double sf_max = 1.0)` — the ctor with the three damping-mode
  default values selected by ctor-argument.

### Sub-pattern B — application via in-place `Mult(x, y)` → `Apply(dinv, x, y)`

    void JacobiSmoother<OperType>::Mult(const VecType &x, VecType &y) const
    {
      MFEM_ASSERT(!this->initial_guess, "JacobiSmoother does not use initial guess!");
      Apply(dinv, x, y);                         // namespace-local kernel dispatch
    }

    // Real path (template <bool Transpose = false>):
    inline void Apply(const Vector &dinv, const Vector &x, Vector &y) {
      // ... Read/Write device-pointer setup ...
      mfem::forall_switch(use_dev, N, [=] (int i) { Y[i] = DI[i] * X[i]; });
    }

The L1 *value* `y = jacobi_smoother(op, x)` is the L0 `y` after `Mult`
returns. The crucial L0 facts the L1 form erases:

- **Destination-arg mutation.** `y` is the output argument; the namespace-
  local `Apply` writes through it via the device-pointer
  `auto *Y = y.Write(use_dev);` then the elementwise update
  `Y[i] = DI[i] * X[i]`. The L1 form returns a fresh value. (Same output-arg
  idiom as [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md)
  and [`chebyshev-smoother-mutation-rotation`](./chebyshev-smoother-mutation-rotation.md)
  — the destination is named in the call's argument list, not on the LHS.)
- **No workspace.** Unlike `chebyshev-smoother` (which scribbles the member
  workspace `d` and the passed workspace `r` every sweep step), Jacobi's
  apply *has no workspace*: it reads `dinv`, reads `x`, writes `y`, and
  returns. No `apply_linop` call, no residual, no direction, no inner state.
  This is the smoother's defining lightness; the L1 form drops nothing on
  the workspace axis because there was no workspace to drop.
- **No `pc_it` outer sweep.** The Jacobi apply is a *single elementwise
  pass*; the L0 `Mult` body has no outer iteration. The sibling
  `chebyshev-smoother`'s outer `for (int it = 0; it < pc_it; it++)` loop has
  no analogue here (the L0 source has no `pc_it` member). At L1 this
  collapses to law 1 (`Linearity in x`); at L0 it manifests as the absence
  of the outer-loop scaffold.
- **Initial-guess assertion (precondition).** `MFEM_ASSERT(!this->initial_guess,
  "JacobiSmoother does not use initial guess!")` @102 is a hard precondition
  on the L0 entry: callers MUST clear `y` (or equivalently set
  `initial_guess = false`) before invocation. At L1 this surfaces as a
  signature precondition (no `initial_guess` parameter — distinct from
  `chebyshev-smoother`, which carries `initial_guess` as a per-call argument
  and absorbs the `false` path as a degenerate case). The Jacobi closure has
  no apply-time branch on initial-guess; callers must respect the
  precondition lexically.
- **Element-type variant axis absorbed via template instantiation.** The two
  `Apply` overloads (`Vector` and `ComplexVector`) are namespace-local
  template functions; the `Mult` dispatcher resolves through the C++ type
  system at instantiation (`template class JacobiSmoother<Operator>;
  template class JacobiSmoother<ComplexOperator>;`). At L1 both overloads
  reduce to the same `op.dinv ⊙ x` action; the complex form is the standard
  elementwise complex multiply.

The complex `Apply<Transpose=true>` branch (lines 61-69) computes the
conjugate-`dinv` apply (the Hermitian-transpose kernel — algebraically
`conj(op.dinv) ⊙ x`). It is **dead code** under the current symmetric wiring:
`MultTranspose` aliases `Mult` (sub-pattern D), not `Apply<true>`, so no
consumer ever instantiates the `Transpose=true` template. Recognition rule
for *potential* non-symmetric sites, not an observed one — same
defined-not-used status as the chebyshev sibling's complex transpose kernels
(`palace/linalg/chebyshev.cpp:101-110, :150-159`).

Justification kind: **structural** — re-bind the L1 output value into the L0
destination buffer `y`; no workspaces to erase; the namespace-local `Apply`
kernel is the elementwise-multiply realisation of `op.dinv ⊙ x`. The
template-instantiation absorption of element-type is the same closure-variant
collapse as sub-patterns at chebyshev.

Citations:
- `palace/linalg/jacobi.cpp:99-104` — `JacobiSmoother<OperType>::Mult(x, y)
  const` — the apply entry point. `MFEM_ASSERT(!this->initial_guess, ...)` @102
  is the no-initial-guess precondition; `Apply(dinv, x, y);` @103 dispatches to
  the namespace-local kernel. The entire per-call action is this one
  dispatch.
- `palace/linalg/jacobi.cpp:30-39` — real `Apply<Transpose>(const Vector
  &dinv, const Vector &x, Vector &y)` — the namespace-local elementwise-
  multiply kernel. The `mfem::forall_switch(use_dev, N, [=]
  MFEM_HOST_DEVICE(int i) { Y[i] = DI[i] * X[i]; });` @38 is the
  single-elementwise-product apply that realises the L1 `op.dinv ⊙ x` action
  (L1 law 1 witness). The `Transpose` template parameter is unused for real
  `dinv` (transpose of a diagonal map is itself).
- `palace/linalg/jacobi.cpp:41-70` — complex `Apply<Transpose>(const
  ComplexVector &dinv, ...)` — the complex elementwise-multiply kernel. The
  forward branch @52-60 computes `(YR, YI) = (DIR·XR − DII·XI, DII·XR +
  DIR·XI)`; the `Transpose = true` branch @61-69 computes the
  conjugate-`dinv` apply `(YR, YI) = (DIR·XR + DII·XI, −DII·XR + DIR·XI)`.
  The latter is the dead-code Hermitian-transpose kernel under symmetric
  wiring.
- `palace/linalg/jacobi.cpp:106-107` — `template class
  JacobiSmoother<Operator>; template class JacobiSmoother<ComplexOperator>;`
  — the element-type variant axis instantiation site.
- `palace/linalg/jacobi.hpp:41` — `void Mult(const VecType &x, VecType &y)
  const override;` — the `Solver<OperType>` base virtual override declaration.
- `palace/linalg/solver.hpp:32-33` — `// Whether or not to use the second
  argument of Mult() as an initial guess. bool initial_guess;` — the base-
  class member that the Jacobi `Mult` asserts negation of.

### Sub-pattern C — opaque spectral-estimate sub-action (`omega == 0.0` only)

    // Inside SetOperator, when omega == 0.0:
    auto lambda_max = GetLambdaMax(comm, op, dinv);
    // GetLambdaMax (namespace-local):
    double GetLambdaMax(MPI_Comm comm, const Operator &A, const Vector &dinv) {
      DiagonalOperator Dinv(dinv);
      ProductOperator DinvA(Dinv, A);                    // DinvA = D⁻¹ · A
      return linalg::SpectralNorm(comm, DinvA, true);    // Hermitian flag
    }

The spectral-radius-minimizing damping estimate. Only the
`omega == 0.0` `SetOperator` branch invokes this sub-action; the default
`omega = 1.0` path and any non-zero externally-supplied `omega` skip it
entirely.

The L0 source defines `GetLambdaMax` as a namespace-local helper with two
overloads (real, complex). The **real** overload @14-20 passes literal
`true` as the Hermitian flag; the **complex** overload @22-28 passes
`A.IsReal()`. Both build the implicit product operator `DinvA = Dinv · A`
(via `DiagonalOperator` + `ProductOperator` wrappers) and dispatch to
`linalg::SpectralNorm(comm, DinvA, hermitian)` for the power-iteration
estimate of the spectral radius of `D⁻¹ · A`.

**The `GetLambdaMax` definition is line-for-line *identical* to the one in
`palace/linalg/chebyshev.cpp:13-27`** (same namespace-local helper,
duplicated in both translation units). This is the same opaque
`spectrum_estimate(A, dinv)` setup sub-action recorded in the chebyshev
sibling's sub-pattern D; promotion of `spectrum_estimate` to a firm L1
operator is the existing open
`matrix-weighted-norm-and-bilinear-form` residual-cohort question, not a new
rough-in proposed here — this theme treats it as opaque.

The substituted optimal `ω` arithmetic in `SetOperator`:

    lambda_min = (sf_max - 1.0) * lambda_max;
    omega      = 2.0 / (lambda_min + lambda_max);
               = 2.0 / (sf_max * lambda_max);            -- simplified

is the L1 law 4 (`Estimated-damping degenerate case`) at the closure level
— the standard Jacobi-iteration optimal damping
`ω* = 2 / (λ_min + λ_max)` over the spectral interval `[λ_min, λ_max]`,
with Palace's convention `λ_min = (sf_max − 1) · λ_max` (Saad, *Iterative
Methods for Sparse Linear Systems*, §4.1).

Justification kind: **structural** — `GetLambdaMax` is an opaque sub-action
of the setup with positively-cited body; the optimal-`ω` arithmetic is
closed-form (the L1 law 4 substitution). The opacity is the same handling
as the chebyshev sibling (sub-pattern D); no per-call branch on damping-mode
survives the closure-commit.

Citations:
- `palace/linalg/jacobi.cpp:14-20` — real `GetLambdaMax(MPI_Comm comm, const
  Operator &A, const Vector &dinv)`: `DiagonalOperator Dinv(dinv);
  ProductOperator DinvA(Dinv, A); return linalg::SpectralNorm(comm, DinvA,
  true);`. The `// Assumes A SPD (diag(A) > 0) to use Hermitian eigenvalue
  solver.` source-comment @16 records the SPD precondition.
- `palace/linalg/jacobi.cpp:22-28` — complex `GetLambdaMax(MPI_Comm comm,
  const ComplexOperator &A, const ComplexVector &dinv)`: same structure,
  Hermitian flag `A.IsReal()` (true Hermitian only when `A` is real-valued
  in its complex storage).
- `palace/linalg/jacobi.cpp:84-89` — the `SetOperator`'s `omega == 0.0`
  branch invoking `GetLambdaMax(comm, op, dinv)` and computing
  `lambda_min = (sf_max - 1.0) * lambda_max`,
  `omega = 2.0 / (lambda_min + lambda_max)`.
- `palace/linalg/chebyshev.cpp:13-27` — the **identical** `GetLambdaMax`
  definition in the sibling translation unit (line-for-line match;
  documented in the chebyshev-smoother L1 entry §Dependencies).
- `palace/linalg/errorestimator.cpp:75-77` — consumer: `// Use eigenvalue
  estimate to compute optimal Jacobi damping parameter. pc =
  std::make_unique<JacobiSmoother<OperType>>(fespaces.GetFinestFESpace().GetComm(),
  0.0);` — the **only** call site that exercises the `omega == 0.0`
  estimated-damping path; the other four Jacobi consumers
  (`ksp.cpp:199`, `floquetcorrection.cpp:65`, `spaceoperator.cpp:640`,
  `timeoperator.cpp:85`) all use the ctor default `omega = 1.0` and skip
  this sub-pattern entirely.

### Sub-pattern D — transpose self-alias under symmetric wiring

    void MultTranspose(const VecType &x, VecType &y) const override { Mult(x, y); }

`MultTranspose` forwards verbatim to `Mult` (one-liner in the header, no
`.cpp` definition). For real `dinv` this is the trivial mathematical
identity `M = Mᵀ` (any diagonal matrix is its own transpose); for complex
`dinv` this aliases the *transpose* (not conjugate-transpose) — the
Hermitian-transpose would require `Apply<Transpose=true>` (the dead-code
sub-pattern B branch). This realises L1 law 5 (`Self-transpose under
symmetric wiring`,
[`L1/jacobi-smoother`](../L1/jacobi-smoother.md) §Algebraic laws). Aligns
with the SPD precondition under which the smoother is consumed
(`palace/linalg/jacobi.cpp:16` `// Assumes A SPD (diag(A) > 0)`).

Justification kind: **algebraic** — the law `transpose = id` (diagonal-map
self-transpose, witnessed in symmetric wiring) justifies the aliasing;
recognition is by the `MultTranspose → Mult` direct forward. The
complex-`dinv` transpose-vs-Hermitian distinction is a non-law caveat
already recorded in the L1 entry §Algebraic laws "Laws that explicitly do
not hold" block, not re-derived here.

Citations:
- `palace/linalg/jacobi.hpp:43` — `void MultTranspose(const VecType &x,
  VecType &y) const override { Mult(x, y); }` — the inline self-alias
  override. The L1 law 5 witness; also the structural source of the
  dead-code-Hermitian-transpose caveat (the `MultTranspose` body is
  `Mult(x, y)`, not `Apply<true>(dinv, x, y)`).

## Applicability conditions

The rewrite preserves semantics when:

1. **No aliasing between `x` and `y`.** `Mult` reads `x` (via `X = x.Read(use_dev)`)
   and writes `y` (via `Y = y.Write(use_dev)`); the elementwise kernel
   `Y[i] = DI[i] * X[i]` is correct iff `x` and `y` are distinct buffers
   (the read of `X[i]` must complete before the write of `Y[i]` at the same
   index, which is guaranteed across distinct buffers but undefined under
   aliasing). The L1 form takes `x` as a value and returns a fresh `y`, so
   the L0 caller must guarantee distinct buffers. Inherited applicability
   shape from [`chebyshev-smoother-mutation-rotation`](./chebyshev-smoother-mutation-rotation.md)
   sub-pattern A.
2. **Caller has zeroed `y` (initial-guess precondition).** The
   `MFEM_ASSERT(!this->initial_guess, ...)` @102 is a hard precondition on
   the `Mult` entry. The L1 form has no `initial_guess` parameter; the L0
   caller must respect the precondition lexically — distinct from
   `chebyshev-smoother`, which carries `initial_guess` as a per-call
   argument and absorbs the `false` path as a degenerate case (L1 law 5
   there). All five Jacobi consumer sites
   (`ksp.cpp:199`, `errorestimator.cpp:75-77`, `floquetcorrection.cpp:65`,
   `spaceoperator.cpp:640`, `timeoperator.cpp:85`) use the smoother
   downstream of a Krylov / multigrid scaffold that respects the precondition.
3. **Closure immutability across calls.** `op = JacobiSmoother[N]`
   (`dinv`, `omega`, `sf_max`) is set once at `SetOperator` and read-only
   across `Mult` calls. There is no per-call control input at L1 (no
   `initial_guess` parameter; no damping-mode runtime tag).
4. **Damping-mode variant is a setup-time ctor-argument choice, not a
   runtime tag.** The three modes (default `ω = 1.0`, fixed `ω ≠ 0`,
   estimated `ω = 0`) are selected by the ctor's `omega` argument
   (`palace/linalg/jacobi.hpp:34`); at L0 they branch in `SetOperator`
   (`palace/linalg/jacobi.cpp:84-93`). At L1 all three collapse to one
   operator parameterised by `op.dinv`'s *committed* damping value — the
   apply does NOT branch on damping mode. The lowering rewrites the setup
   to *commit* the damping at closure-construction time.
5. **Element-type conformance.** `<Operator>` (real) and `<ComplexOperator>`
   (complex) are both instantiated
   (`palace/linalg/jacobi.cpp:106-107`). The action is identical in form —
   one elementwise product — and the per-element kernel dispatches on
   element type via template instantiation. Unlike `chebyshev-smoother`
   (which carries `dinv` real-valued even for complex `A`), Jacobi carries
   `dinv` as the *full element-type of OperType*: a complex `A` yields a
   complex `dinv` via `ComplexVector::Reciprocal()`
   (`palace/linalg/vector.cpp:248-261`) implementing `1/(a+bi) =
   (a−bi)/|a+bi|²`. The lowering preserves this divergence — the closure
   field's element-type matches the operator's.
6. **SPD operator (for the transpose-aliasing sub-pattern D and the
   spectral-estimate sub-pattern C).** The
   `MultTranspose → Mult` self-alias requires operator symmetry (equivalent
   to the `dinv` having no imaginary part contribution to the transpose, OR
   to consumers reading the alias as transpose-not-Hermitian). The
   `GetLambdaMax` spectral-estimate requires `A` SPD (the source-comment
   precondition at line 16) for the Hermitian-eigenvalue-solver path. All
   five consumer sites use the smoother under SPD `A` (Krylov
   preconditioner, multigrid level-smoother, error-estimator preconditioner).
   Under non-symmetric `A` the dead-code Hermitian-transpose kernel
   (`palace/linalg/jacobi.cpp:61-69`) would need to be wired through
   `MultTranspose`, and the spectral estimate would need a non-Hermitian
   eigenvalue solver.
7. **Single-machine scope.** The `comm` / `MPI_Comm` argument and the `Par*`
   spectral-norm machinery (`GetLambdaMax → SpectralNorm`) are read as
   their single-rank equivalents; MPI distribution is out of scope (flagged
   once per CLAUDE.md §Scope).

## Justification kind

- **Sub-pattern A** (construction site) — `structural`. Constructed-operator
  gate closure materialisation; pure-of-inputs modulo opaque
  `spectrum_estimate` (sub-pattern C).
- **Sub-pattern B** (application via `Mult` → `Apply`) — `structural`.
  Output-arg `y` re-bind via the namespace-local elementwise-multiply
  kernel; no workspace erasure (none to drop).
- **Sub-pattern C** (spectral-estimate sub-action) — `structural`. Opaque
  sub-action with positively-cited body; closed-form optimal-`ω` arithmetic
  realising L1 law 4.
- **Sub-pattern D** (transpose self-alias) — `algebraic`. Diagonal-map
  self-transpose law (L1 law 5) under symmetric wiring.

The theme as a whole is `structural` with one algebraic sub-rule (D). A
`lowering-verifier` audit in a later cycle should confirm the four
sub-patterns match the L0 corpus exhaustively (both element-type
instantiations, the dead-code complex transpose kernel as a recognition
rule, the consumer sites).

## Speculative L1 operators

None new for this theme — both the L1 anchor
([`L1/jacobi-smoother`](../L1/jacobi-smoother.md)) and the dependency
[`L1/assemble_diagonal`](../L1/assemble_diagonal.md) are already firm. The
sub-pattern A diagonal-prep chain references two forward-referenced L1
primitives:

- [`reciprocal`](../L1/reciprocal.md) — the elementwise inverse primitive at
  L1 (firm L1 leaf). Witnessed at L0
  by `Vector::Reciprocal()` (real, via the upstream-MFEM `using Vector =
  mfem::Vector` alias at `palace/linalg/vector.hpp:20`) and
  `ComplexVector::Reciprocal()` (`palace/linalg/vector.cpp:248-261`, the full
  complex `1/(a+bi) = (a−bi)/|a+bi|²`). Companion to `assemble_diagonal` in
  the L1 diagonal-preconditioner-apply chain
  [`assemble_diagonal`](../L1/assemble_diagonal.md) →
  [`reciprocal`](../L1/reciprocal.md) →
  [`elementwise_product`](../L1/elementwise_product.md).
- [`elementwise_product`](../L1/elementwise_product.md) — the elementwise
  multiply primitive at L1 (firm L1 leaf). Witnessed at L0 by the
  namespace-local `Apply(dinv, x, y)` kernel (`palace/linalg/jacobi.cpp:38`
  for real, `:52-60` for complex). The shared `concepts/elementwise-product.md`
  concept page defines the data shape.

Both are named in [`L1/assemble_diagonal`](../L1/assemble_diagonal.md)
§Dependencies and [`L1/jacobi-smoother`](../L1/jacobi-smoother.md)
§Dependencies as firm L1 leaves.

The `spectrum_estimate` setup sub-action (the `SpectralNorm`
power-iteration sibling) is the same *existing* open L1 candidate named in
the `chebyshev-smoother` and `matrix_weighted_norm` residual-cohort open
question (`scaffolding/open-questions.md`,
`matrix-weighted-norm-and-bilinear-form`); promotion is out of scope for
this entry and treated as opaque (same handling as the chebyshev sibling
sub-pattern D).

## Evidence

L0 evidence ranges:

- `palace/linalg/jacobi.cpp:14-20` — real `GetLambdaMax` (SPD comment @16,
  `DiagonalOperator Dinv(dinv); ProductOperator DinvA(Dinv, A); return
  linalg::SpectralNorm(comm, DinvA, true);`).
- `palace/linalg/jacobi.cpp:22-28` — complex `GetLambdaMax` (Hermitian flag
  `A.IsReal()`).
- `palace/linalg/jacobi.cpp:30-39` — real `Apply<Transpose>` kernel
  (`Y[i] = DI[i] * X[i]` @38).
- `palace/linalg/jacobi.cpp:41-70` — complex `Apply<Transpose>` kernel
  (forward branch @52-60; dead-code `Transpose=true` Hermitian branch
  @61-69).
- `palace/linalg/jacobi.cpp:74-97` — `SetOperator` body
  (signature @75, `dinv.SetSize(op.Height())` @77, `dinv.UseDevice(true)` @78,
  `op.AssembleDiagonal(dinv)` @79, `dinv.Reciprocal()` @80, `omega == 0.0`
  branch @84-89, damping-fold @90-93, base-contract @95-96).
- `palace/linalg/jacobi.cpp:99-104` — `Mult(x, y) const`
  (`MFEM_ASSERT(!this->initial_guess, ...)` @102, `Apply(dinv, x, y)` @103).
- `palace/linalg/jacobi.cpp:106-107` — element-type variant axis
  instantiations.
- `palace/linalg/jacobi.hpp:19` — `class JacobiSmoother : public
  Solver<OperType>`.
- `palace/linalg/jacobi.hpp:28` — `VecType dinv;`.
- `palace/linalg/jacobi.hpp:31` — `double omega, sf_max;`.
- `palace/linalg/jacobi.hpp:34` — ctor `JacobiSmoother(MPI_Comm comm, double
  omega = 1.0, double sf_max = 1.0)`.
- `palace/linalg/jacobi.hpp:39` — `SetOperator` override decl.
- `palace/linalg/jacobi.hpp:41` — `Mult` override decl.
- `palace/linalg/jacobi.hpp:43` — `MultTranspose` self-alias override
  (`{ Mult(x, y); }`).
- `palace/linalg/chebyshev.cpp:13-27` — sibling-precedent: the line-for-line
  *identical* `GetLambdaMax` definition (sub-pattern C precedent).
- `palace/linalg/solver.hpp:32-33` — `Solver<OperType>::initial_guess`
  base-class member (the `MFEM_ASSERT(!this->initial_guess)` target).
- `palace/linalg/vector.cpp:248-261` — `ComplexVector::Reciprocal()` body
  (the full complex `1/(a+bi) = (a−bi)/|a+bi|²` realising the complex
  variant axis at sub-pattern A).
- `palace/linalg/ksp.cpp:198-200` — consumer:
  `case LinearSolver::JACOBI: pc =
  std::make_unique<JacobiSmoother<OperType>>(comm); break;` (default
  `omega = 1.0` preconditioner-instantiation; principal consumer).
- `palace/linalg/errorestimator.cpp:75-77` — consumer:
  `// Use eigenvalue estimate to compute optimal Jacobi damping parameter.
  pc = std::make_unique<JacobiSmoother<OperType>>(fespaces.GetFinestFESpace().GetComm(),
  0.0);` (the **only** `omega = 0.0` estimated-damping consumer; witnesses
  sub-pattern C's exercise path).
- `palace/linalg/floquetcorrection.cpp:65` — consumer:
  `auto jac = std::make_unique<JacobiSmoother<OperType>>(rt_fespace.GetComm());`
  (default-damping consumer).
- `palace/models/spaceoperator.cpp:640` — consumer:
  `auto jac = std::make_unique<JacobiSmoother<Operator>>(comm);` (default-
  damping real-`OperType` consumer).
- `palace/models/timeoperator.cpp:85` — consumer:
  `auto jac = std::make_unique<JacobiSmoother<Operator>>(comm);` (default-
  damping real-`OperType` consumer; transient-solver path).

L1 anchor:

- `book/src/L1/jacobi-smoother.md` — the firm L1 operator all sub-patterns
  lower from.

L1>L0 sibling precedents (structural template):

- `book/src/L1-L0/chebyshev-smoother-mutation-rotation.md` — the
  closely-parallel constructed-operator-gate sibling. Sub-pattern A
  (construction site) is structurally identical to chebyshev sub-pattern D
  (same `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup chain, same
  `GetLambdaMax` spectral-estimate sub-action); sub-pattern D (transpose
  self-alias) parallels chebyshev sub-pattern C (`MultTranspose2 → Mult2`
  symmetry alias).
- `book/src/L1-L0/assemble-diagonal-mutation-rotation.md` — the
  diagonal-extraction L1>L0 step reused in sub-pattern A's
  `op.AssembleDiagonal(dinv)` call (transitively all four
  representation sub-patterns of `assemble_diagonal` may propagate through
  here, depending on the operator wrapper).

## Caveats

- The complex `Apply<Transpose=true>` kernel
  (`palace/linalg/jacobi.cpp:61-69`) is dead code under symmetric wiring —
  `MultTranspose` aliases `Mult`, not `Apply<true>`. The conjugate-`dinv`
  Hermitian-transpose law is therefore *not realised* by the Palace surface
  even though the source contains the machinery for it. Recorded as a
  recognition rule (sub-pattern B) for potential non-symmetric sites, same
  defined-not-used status as the chebyshev sibling's transpose kernels.
- The `omega == 0.0` estimated-damping mode (sub-pattern C) is exercised by
  exactly one of the five call sites (`errorestimator.cpp:75-77`); the
  other four use the default `omega = 1.0` and skip sub-pattern C entirely.
  The setup-time correctness of sub-pattern C depends on the
  opaque-out-of-scope `spectrum_estimate` sub-action, but the per-call
  *apply* law (sub-pattern B) is identical regardless (L1 law 1 with the
  substituted `ω` absorbed into `dinv`).

## Open questions / caveats

- **Dead-code complex transpose kernel.**
  `palace/linalg/jacobi.cpp:61-69` defines the conjugate-`dinv` Hermitian-
  transpose elementwise kernel; it is unreachable under the symmetric
  `MultTranspose → Mult` wiring. Same defined-not-used status as the
  chebyshev sibling's complex transpose kernels
  (`palace/linalg/chebyshev.cpp:101-110, :150-159`) and the `axpby`
  sibling's `ComplexVector::Subtract` forms.
- **`spectrum_estimate` L1 candidacy.** Whether the `GetLambdaMax →
  SpectralNorm` power-iteration sub-action should be firmed as its own L1
  operator is the open `matrix-weighted-norm-and-bilinear-form` residual-
  cohort question; this theme treats it as opaque.
- **L2 unification candidate: `polynomial_smoother` combinator.** Both
  `jacobi_smoother` and `chebyshev_smoother` lift the *identical*
  diagonal-prep setup chain (sub-pattern A here ≡ chebyshev sub-pattern D)
  and the *identical* `GetLambdaMax` spectral-estimate sub-action
  (sub-pattern C here ≡ chebyshev sub-pattern D opaque). The L2
  unification — Jacobi as the degree-zero (`order = 0`) member of the
  diagonally-scaled-polynomial-smoother family parameterised by chebyshev's
  `order ≥ 1` — is a candidate but not pursued in this theme; the
  unification would obscure the Jacobi apply's identity with the
  underlying L2 elementwise-product primitive, so the case for/against is
  not slam-dunk.
- **MPI / `MPI_Comm` placeholder.** The `comm` argument flows through
  `GetLambdaMax → SpectralNorm`; under MPI it carries the collective
  context. Per CLAUDE.md §Scope, MPI distribution is out of scope; the
  `Par*` machinery is read as its single-rank equivalent. Flagged once
  here.

## Status

`firm` — every sub-pattern is a syntactic identity on fully-specified positive source.

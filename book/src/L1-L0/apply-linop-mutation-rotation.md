# apply-linop-mutation-rotation

The mutation rotation for linear-operator application. Lowers the pure L1
form `apply_linop(A, x) = A · x` into Palace's in-place L0 virtual
`Mult(x, y)` family on the `Operator` / `ComplexOperator` class hierarchies.
Companion to [`axpby-mutation-rotation`](./axpby-mutation-rotation.md):
both lower L1-pure-functional updates into L0 in-place mutation, but where
`axpby` mutates a vector buffer through a free-function or member call,
`apply_linop` mutates the output buffer through a virtual method on the
operator object — and exposes the L1 transpose-mode and accumulate-mode
variant axes as dedicated L0 virtual methods.

## Slug

`apply-linop-mutation-rotation`

## L1 form (LHS)

The pure-functional linear-operator application
([`L1/apply_linop`](../L1/apply_linop.md)):

    y_new = apply_linop(A, x)              -- y_new = A · x

The transpose-mode and accumulate-mode variants are recoverable from this
single L1 form via algebraic identities (per the firm L1 entry's
Semantics and Variant-axes sections):

- transpose:           `apply_linop(Aᵀ, x)`
- hermitian transpose: `apply_linop(Aᴴ, x)`
- accumulate:          `axpby(a, apply_linop(A, x), 1, y_old)`

All five L0 sub-patterns below are realisations of these L1 expressions.

## L0 form (RHS)

Five sub-patterns of the same rewrite, distinguished by (transpose-mode ×
accumulate-mode) of the L0 dispatched virtual method. All sub-patterns
share the same mutation-rotation shape: the L1 output value binds to the
L0 destination argument `y`, the operator becomes the receiver of the
method call, and the input vector `x` becomes the method's first
argument.

### Sub-pattern A — bare forward apply (`Mult`)

    A.Mult(x, y);                          // real path: mfem::Operator::Mult
    A.Mult(x, y);                          // complex path: ComplexOperator::Mult

The textbook in-place forward apply. The destination buffer `y` is
overwritten with `A · x`. The real path inherits the abstract
`mfem::Operator::Mult(const Vector &x, Vector &y) const` from MFEM
(`palace/linalg/operator.hpp:21` — `using Operator = mfem::Operator;`);
the complex path declares its own pure-virtual
`ComplexOperator::Mult(const ComplexVector &x, ComplexVector &y) const`
at `palace/linalg/operator.hpp:54`.

Justification kind: **structural** — re-bind the L1 output value into
the L0 destination buffer. The operator-representation variant axis
(sparse / matrix-free / composition / multigrid / parallel-wrapped) is
absorbed at L1; at L0 the concrete subclass dispatches to its own kernel
(e.g. `BaseProductOperator::Mult` chains two `Mult` calls,
`palace/linalg/operator.hpp:202-206`; `ParOperator::Mult` applies
prolongation, calls the inner operator, applies restriction,
`palace/linalg/rap.cpp:195-234`). The choice of subclass is a transparent
performance trick at L1; the mutation rotation is identical across all
realisations.

Citations:
- `palace/linalg/operator.hpp:21` — real-operator type alias from MFEM.
- `palace/linalg/operator.hpp:54` — `ComplexOperator::Mult` pure-virtual decl.
- `palace/linalg/operator.cpp:428-441` — `SumOperator::Mult` definition
  (representative concrete realisation).
- `palace/linalg/operator.hpp:202-206` — `BaseProductOperator::Mult`
  (`B.Mult(x, z); A.Mult(z, y)` — chained-apply witness of
  operator-composition).
- `palace/linalg/operator.cpp:479-487` — `BaseDiagonalOperator<Operator>::Mult`
  (element-wise diagonal `y[i] = d[i] * x[i]` — matrix-free realisation).
- `palace/linalg/rap.cpp:195-234` — `ParOperator::Mult` (parallel
  prolongation/restriction wrapper).
- `palace/linalg/iterative.cpp:379` — `A->Mult(x, r)` (CG residual call site).
- `palace/linalg/iterative.cpp:443` — `A->Mult(p, z)` (CG inner-loop call site).

### Sub-pattern B — transposed apply (`MultTranspose`)

    A.MultTranspose(x, y);                 // real path: mfem::Operator::MultTranspose
    A.MultTranspose(x, y);                 // complex path: ComplexOperator::MultTranspose

The transposed forward apply. Writes `Aᵀ · x` into `y`. At L1 this is
`apply_linop(Aᵀ, x)` — the transpose-mode variant axis is recoverable via
the algebraic transform `Aᵀ`. The L0 source provides a dedicated virtual
method because the operator's internal representation may permit a more
efficient transpose path (e.g. swapping prolongation and restriction in
`ParOperator::MultTranspose`, `palace/linalg/rap.cpp:236-275`).

Justification kind: **algebraic** — the rewrite is recognised by
`A.MultTranspose(x, y)` ⇒ `y = apply_linop(Aᵀ, x)`. The L0 dedicated
method is the representation-aware specialisation that the L1>L0 lowering
reintroduces.

Citations:
- `palace/linalg/operator.hpp:56` — `ComplexOperator::MultTranspose` decl.
- `palace/linalg/operator.cpp:443-456` — `SumOperator::MultTranspose`.
- `palace/linalg/rap.cpp:236-275` — `ParOperator::MultTranspose` (parallel
  wrapper; restriction/prolongation roles swapped).

### Sub-pattern C — Hermitian-transposed apply (`MultHermitianTranspose`, complex only)

    A.MultHermitianTranspose(x, y);        // complex path only: ComplexOperator only

The conjugate-transposed forward apply for complex operators. Writes
`Aᴴ · x` into `y`. Meaningful only on `ComplexOperator`; on real
operators it collapses to sub-pattern B (`Aᴴ = Aᵀ` in ℝ). At L1 this is
`apply_linop(Aᴴ, x)` — the third value of the transpose-mode variant
axis.

Justification kind: **algebraic** — the rewrite is recognised by
`A.MultHermitianTranspose(x, y)` ⇒ `y = apply_linop(Aᴴ, x)`. Required for
correctness on complex operators in eigenvalue solvers (e.g. SLEPc,
ARPACK paths) and complex-symmetric vs Hermitian distinctions in
preconditioner construction.

Citations:
- `palace/linalg/operator.hpp:58` — `ComplexOperator::MultHermitianTranspose` decl.
- `palace/linalg/operator.hpp:158-165` — `ProductOperatorHelper`
  `MultHermitianTranspose` (operator-composition witness:
  `A.MultHermitianTranspose(x, z); B.MultHermitianTranspose(z, y)`).

### Sub-pattern D — accumulating forward apply (`AddMult`)

    A.AddMult(x, y, a);                    // real path: a defaults to 1.0
    A.AddMult(x, y, a);                    // complex path: a is std::complex<double>

Accumulates `a · A · x` into `y` rather than overwriting. At L1 this is
the composition `axpby(a, apply_linop(A, x), 1, y_old)` — two L1
primitives in sequence. The L0 source provides `AddMult` as a fused
method for two reasons: (i) skips the zero-initialisation of `y` (a
transparent performance trick); (ii) for matrix-free operators, allows
direct accumulation of element contributions into `y` without a separate
temporary (transparent algebraically, load-bearing for memory traffic;
both are L1>L0 concerns).

Justification kind: **algebraic** — the rewrite is recognised by
`A.AddMult(x, y, a)` ⇒ `y = axpby(a, apply_linop(A, x), 1, y_old)`. The
L0 fused method is a transparent performance trick over the L1
composition.

Recognition note: `AddMult` with default `a = 1.0` is the most common
call site (no scaling); the explicit-`a` form composes with `axpby`'s
sub-pattern A (general α). When `a == 1.0` this further specialises via
`axpby-mutation-rotation` sub-pattern B (`y += apply_linop(A, x)`); when
`a == -1.0`, sub-pattern C. The accumulation step inside Palace's
concrete `AddMult` realisations is itself an axpy
(`SumOperator::AddMult` uses `y.Add(a*c, z)`,
`palace/linalg/operator.cpp:464`; `ParOperator::AddMult` uses
`y.Add(a, ty)`, `palace/linalg/rap.cpp:317`) — already cited by the
sister theme `axpby-mutation-rotation`, intentionally not duplicated
here.

Citations:
- `palace/linalg/operator.hpp:60-61` — `ComplexOperator::AddMult` decl
  (default scalar `a = 1.0`).
- `palace/linalg/operator.hpp:133` — `SumOperator::AddMult` decl.
- `palace/linalg/operator.cpp:458-466` — `SumOperator::AddMult` definition
  (the accumulating loop; witness of L0 dispatch `Mult → AddMult` reuse
  pattern, as `SumOperator::Mult` for size>1 zeros `y` then calls
  `AddMult`, `palace/linalg/operator.cpp:439-440`).
- `palace/linalg/operator.hpp:214-218` — `BaseProductOperator::AddMult`
  (operator-composition with accumulating outer apply: `B.Mult(x, z);
  A.AddMult(z, y, a)`).
- `palace/linalg/rap.cpp:277-318` — `ParOperator::AddMult` definition.
- `palace/linalg/operator.cpp:509-519` — `BaseDiagonalOperator<Operator>::AddMult`
  (matrix-free fused accumulation `Y[i] += a * D[i] * X[i]`).

### Sub-pattern E — accumulating transposed / Hermitian applies (`AddMultTranspose`, `AddMultHermitianTranspose`)

    A.AddMultTranspose(x, y, a);           // real and complex paths
    A.AddMultHermitianTranspose(x, y, a);  // complex only

Compositions of sub-patterns B/C and D. At L1 these are
`axpby(a, apply_linop(Aᵀ, x), 1, y_old)` and
`axpby(a, apply_linop(Aᴴ, x), 1, y_old)` respectively. Recognition is by
syntactic match on the method name.

Justification kind: **algebraic** — combined transpose-mode and
accumulate-mode variant-axis rewrites; recognised by syntactic match on
the L0 method name.

Citations:
- `palace/linalg/operator.hpp:63-67` — `ComplexOperator::AddMultTranspose`
  and `AddMultHermitianTranspose` decls.
- `palace/linalg/operator.cpp:468-476` — `SumOperator::AddMultTranspose`.
- `palace/linalg/rap.cpp:320-360` — `ParOperator::AddMultTranspose`.
- `palace/linalg/operator.hpp:167-175` — `ProductOperatorHelper`
  `AddMultHermitianTranspose` (composition witness).
- `palace/linalg/operator.hpp:220-225` — `BaseProductOperator::AddMultTranspose`.

## Applicability conditions

For all five sub-patterns the rewrite preserves semantics when:

1. **No aliasing between `x` and `y`.** Palace's L0 kernels read `x`
   while writing `y`; if `x` and `y` alias, the L0 behaviour is
   ill-defined (most realisations assume distinct buffers; element-wise
   diagonal applies happen to tolerate aliasing while
   `BaseProductOperator::Mult` does not — its workspace `z` separates the
   two halves, but the post-write to `y` from `A.Mult(z, y)` could
   collide with `x` if they alias and `z` aliases `x` too). Palace never
   aliases `Mult` arguments in observed sites; this is an applicability
   condition, not a known failure. Shared with the sister theme.

2. **No observer of the prior `y` value after the call** (sub-pattern A,
   B, C — overwriting variants). For sub-patterns D, E (accumulating
   variants) the prior `y` is consumed, not destroyed; the L1
   `y_old` argument and the L0 destination buffer hold the same logical
   value pre-call.

3. **Conforming shape and element type.**
   `x.Size() == A.Width()` and `y.Size() == A.Height()` (and equality
   `A.Height() == A.Width()` for square operators in iterative solver
   inner loops). Element type matches: either all real (`Vector`,
   `Operator`) or all complex (`ComplexVector`, `ComplexOperator`). Mixed
   real-operator-on-complex-vector requires lifting via
   `ComplexWrapperOperator` (`palace/linalg/operator.hpp:73-113`) — that
   is itself a sub-pattern of A applied to a `ComplexOperator` whose
   internal representation wraps a real operator. The lifting is the
   `complex-from-real-lift` concept, not part of this theme.

4. **Operator `A` is L0-linear (the L0 method is `const` and implements
   a linear map).** Palace's `Operator` virtuals are declared `const`;
   operator-state mutation through `Mult` is not part of the L0
   contract. Workspace mutation through the `mutable` member `z` (e.g.
   `SumOperator::z`, `BaseProductOperator::z`) is permitted by C++
   semantics but does not affect the L1 view — the workspace is private
   to the operator and not observable from outside the call.

5. **Transpose-mode recognition** (sub-patterns B, C). The L1
   re-anchoring requires that `Aᵀ` and `Aᴴ` are well-defined for the
   operator at the L1 algebraic level. For all concrete Palace
   operators this is satisfied; obstruction cases (operators with no
   defined transpose action) would route to `MFEM_ABORT`-style failures
   at L0 — out of scope for this theme.

6. **Accumulate-mode `a` is a runtime scalar** (sub-patterns D, E). For
   `a == 1.0` the sub-pattern interacts with `axpby-mutation-rotation`
   sub-pattern B; for `a == -1.0` with sub-pattern C; for general `a` it
   composes with `axpby-mutation-rotation` sub-pattern A. The
   constant-folding fast paths inside the inner `y.Add(...)` accumulator
   are *already* covered by the sister theme — this theme does not
   re-handle them.

## Justification kind

- **Sub-pattern A** — `structural`. Re-bind L1 output value into L0
  destination buffer; operator-representation axis collapse absorbed in
  L1.
- **Sub-pattern B** — `algebraic`. `A.MultTranspose(x, y)` ⇒
  `y = apply_linop(Aᵀ, x)`.
- **Sub-pattern C** — `algebraic`. `A.MultHermitianTranspose(x, y)` ⇒
  `y = apply_linop(Aᴴ, x)`.
- **Sub-pattern D** — `algebraic`. `A.AddMult(x, y, a)` ⇒
  `y = axpby(a, apply_linop(A, x), 1, y_old)`.
- **Sub-pattern E** — `algebraic`. Combinations of B/C and D under
  syntactic name-match.

The theme as a whole is `structural` with four algebraic sub-rules
covering the two orthogonal L1 variant axes (transpose-mode ×
accumulate-mode).

## Speculative L1 operators

None.

`apply_linop` is the firm L1 form; the five sub-patterns
decompose into existing firm L1 primitives only — `apply_linop` for
forward / transposed / Hermitian-transposed application, `axpby` for the
accumulating-mode composition. No rough-in L1 operator is needed for this
theme.

This is a structural property of the firm L1 cohort: the
variant-axis-collapse design at L1 (transpose-mode and accumulate-mode
collapsed; operator-representation absorbed) means the L1>L0 lowering
operates entirely within existing L1 vocabulary. By contrast, the
obstruction themes (`minres-iteration`, `bicgstab-iteration`) emit
rough-in operators because no L0 anchor exists; here the L0 anchors are
plentiful and the L1 abstractions are firm.

## Coverage

This theme cites the **representative** concrete realisations
(`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`,
`ParOperator`). The full Palace corpus contains many more concrete
realisations (preconditioners under `palace/linalg/{amg,ams,jacobi,
chebyshev,distrelaxation,blockprecond,gmg,hcurl}.{hpp,cpp}`; FE assembly
closures; Jacobian-action operators in transient / nleps drivers); the
cited set is illustrative — sufficient to establish each sub-pattern
recognition rule. Estimated total `Mult`-virtual implementations across
the corpus: ~30-40 (every concrete operator subclass implements at least
`Mult`; many also implement `MultTranspose` and the `AddMult` family).

Further L0 declaration ranges grounding the cited realisations:
`palace/linalg/operator.hpp:116-136` (`SumOperator` declaration),
`palace/linalg/operator.hpp:178-226` (`BaseProductOperator` template),
`palace/linalg/operator.cpp:488-507` (`BaseDiagonalOperator<ComplexOperator>::Mult`
matrix-free realisation, sub-pattern A complex path).

The L1 anchor is `book/src/L1/apply_linop.md` (the firm L1 operator all
five sub-patterns lower from); the sibling lowering theme
`book/src/L1-L0/axpby-mutation-rotation.md` covers the inner-axpy-accumulator
step of sub-patterns D, E (not duplicated here).

## Status

`firm` — all five sub-pattern recognition rules (A structural, B/C/D/E algebraic)
hold via the **firm-on-positive-structure / syntactic-identity escape**: every
sub-rule is a name-match identity over a fully-specified positive
`mfem::Operator::Mult` / `ComplexOperator::Mult`-family method body (operator algebra
read off the source — `operator.cpp:428-520`, `rap.cpp:195-361`,
`operator.hpp:54-226`), NOT a numerically-asserted axiom or a convergence-semantics
claim, so the absence of a dedicated unit test does not gate the laws. The
D/E composition path is the composition of two already-firm syntactic rules
(`apply_linop` + `axpby`, the sister theme `axpby-mutation-rotation` being firm); the
inner accumulator (`y.Add(a*c, z)` `operator.cpp:464`, `y.Add(a, ty)` `rap.cpp:317`)
is covered by the sister theme and intentionally not re-handled here. Both endpoints
are firm (`L1/apply_linop`; L0 ground truth), so `rank(theme) ≤ min(firm, firm) = firm`.

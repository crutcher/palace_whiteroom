---
agent: abstractor
invoked_at: 2026-05-27T025354Z
scope: L1>L0 theme sketch — apply-linop-mutation-rotation
status: integrated
integrated_at: 2026-05-27T07:04:24Z
integration_commit: a16c32c76f7ed73c2ab1d381d440db2cd6b2e7f9
integration_notes: Applied. Second mutation-rotation theme after axpby-mutation-rotation. 5 sub-patterns A-E. Closes apply-linop-lowering-theme-scope (cycle-004).
inputs:
  - book/src/L1/apply_linop.md (firm L1 form, cycle-004)
  - book/src/L1-L0/axpby-mutation-rotation.md (sister theme; precedent)
  - palace/linalg/operator.hpp (Operator + ComplexOperator interfaces)
  - palace/linalg/operator.cpp (SumOperator, BaseDiagonalOperator)
  - palace/linalg/rap.cpp (ParOperator parallel wrapper)
  - open-question apply-linop-lowering-theme-scope (cycle-004 flag)
skill_uptake:
  - skill: verify-citation-range
    used: yes
    note: applied to the 11 ranges enumerated under Verified-against (each carries `audited_at` + verdict).
  - skill: classify-variant-axis
    used: yes
    note: produced the rectangular (transpose-mode × accumulate-mode) decomposition; real-vs-complex element-type axis handled per-sub-pattern.
---

# REPORT: L1>L0 theme sketch — apply-linop-mutation-rotation

## Summary

Lowers the firm L1 operator [`apply_linop`](../L1/apply_linop.md) (`y = A·x`,
pure functional, opaque-operator) into the Palace L0 family of virtual
`Mult` / `MultTranspose` / `MultHermitianTranspose` / `AddMult{,Transpose,
HermitianTranspose}` methods on the `Operator` / `ComplexOperator` class
hierarchies. The theme is **structural** at root (re-bind the L1 output
value into the L0 destination buffer `y`) with two algebraic specialisations
collapsing the transpose-mode and accumulate-mode L1 variant axes back into
dedicated L0 virtual methods. Five sub-patterns:

- **A — bare forward apply** (`Mult`): structural rebind.
- **B — transposed apply** (`MultTranspose`): L1 transpose-mode axis →
  dedicated method (algebraic; `apply_linop(Aᵀ, x)` law).
- **C — Hermitian-transposed apply** (`MultHermitianTranspose`,
  complex only): L1 transpose-mode axis → dedicated method (algebraic;
  `apply_linop(Aᴴ, x)` law).
- **D — accumulating apply** (`AddMult`): L1 accumulate-mode axis →
  decomposes as `y ← axpby(a, apply_linop(A, x), 1, y)`; reintroduces
  fusion (algebraic).
- **E — accumulating transposed/Hermitian applies**
  (`AddMultTranspose`, `AddMultHermitianTranspose`): composition of B/C
  and D; recognition rule rather than a new axis (structural+algebraic).

The L1>L0 lowering reintroduces three L0-only concerns that the L1
signature collapses: (i) the destination output argument `y` (mutation
rotation, shared with `axpby-mutation-rotation`); (ii) the choice of
dedicated transpose / accumulate virtual method as a transparent
representation-aware specialisation; (iii) the workspace tensor owned by
the concrete operator subclass (e.g. `BaseProductOperator::z`,
`SumOperator::z`) — recognition that the L0 method-form's mutable member
`z` is the L1 intermediate value in operator-composition. No new
speculative L1 operators are proposed — `apply_linop` is the firm L1 form;
all sub-patterns are L1>L0 rewrites built from existing firm L1 vocabulary
(`apply_linop`, `axpby`).

The theme is larger than `axpby-mutation-rotation` in dimensionality (5
sub-patterns vs 3) but smaller in algebraic depth — the two transpose-mode
sub-patterns (B, C) and the accumulating sub-patterns (D, E) are mechanical
combinations of two orthogonal variant axes; the lowering is rectangular,
not unstructured.

## Proposed changes

```edit:book/src/L1-L0/apply-linop-mutation-rotation.md
[create the theme entry — full content below]

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
accumulate-mode). A `lowering-verifier` audit in a later cycle should
confirm sub-rule recognition exhausts the L0 corpus and that the
workspace-tensor reading (member `z` as L1 intermediate) is consistent
across the `BaseProductOperator` / `SumOperator` / `ParOperator` / etc.
realisations.

## Speculative L1 operators

None.

`apply_linop` is the firm L1 form (cycle-004); the five sub-patterns
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

## Verified-against

L0 evidence ranges (verified by direct read during this cycle):

- `palace/linalg/operator.hpp:21` — real-operator alias.
- `palace/linalg/operator.hpp:54-67` — `ComplexOperator` virtual decls
  (`Mult`, `MultTranspose`, `MultHermitianTranspose`,
  `AddMult{,Transpose,HermitianTranspose}`).
- `palace/linalg/operator.hpp:116-136` — `SumOperator` declaration.
- `palace/linalg/operator.hpp:158-175` — `ProductOperatorHelper`
  Hermitian-transpose specialisation.
- `palace/linalg/operator.hpp:178-226` — `BaseProductOperator` template
  (composition).
- `palace/linalg/operator.cpp:428-441` — `SumOperator::Mult` (sub-pattern A).
- `palace/linalg/operator.cpp:443-456` — `SumOperator::MultTranspose`
  (sub-pattern B).
- `palace/linalg/operator.cpp:458-466` — `SumOperator::AddMult`
  (sub-pattern D).
- `palace/linalg/operator.cpp:468-476` — `SumOperator::AddMultTranspose`
  (sub-pattern E).
- `palace/linalg/operator.cpp:479-507` — `BaseDiagonalOperator<...>::Mult`
  (matrix-free realisation, sub-pattern A).
- `palace/linalg/operator.cpp:509-519` — `BaseDiagonalOperator<Operator>::AddMult`
  (matrix-free realisation, sub-pattern D).
- `palace/linalg/rap.cpp:195-234` — `ParOperator::Mult` (parallel
  wrapper, sub-pattern A).
- `palace/linalg/rap.cpp:236-275` — `ParOperator::MultTranspose`
  (parallel wrapper, sub-pattern B).
- `palace/linalg/rap.cpp:277-318` — `ParOperator::AddMult` (parallel
  wrapper, sub-pattern D).

L1 anchor:

- `book/src/L1/apply_linop.md` — the firm L1 operator that all five
  sub-patterns lower from.

Sibling lowering theme:

- `book/src/L1-L0/axpby-mutation-rotation.md` — the
  inner-axpy-accumulator step of sub-patterns D, E is covered there; not
  duplicated here.

Coverage note: this theme cites the **representative** concrete
realisations (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`,
`ParOperator`). The full Palace corpus contains many more concrete
realisations (preconditioners under `palace/linalg/{amg,ams,jacobi,
chebyshev,distrelaxation,blockprecond,gmg,hcurl}.{hpp,cpp}`; FE assembly
closures; Jacobian-action operators in transient / nleps drivers).
Exhaustive corpus indexing is deferred to a `lowering-verifier` audit.
The cited set is illustrative — sufficient to establish each sub-pattern
recognition rule. Estimated total `Mult`-virtual implementations across
the corpus: ~30-40 (every concrete operator subclass implements at least
`Mult`; many also implement `MultTranspose` and the `AddMult` family).

## Status

`rough-in` — sub-pattern recognition rules sketched; the
variant-axis-collapse design has been verified against the firm L1
`apply_linop` entry; the L0 evidence ranges have been verified by direct
read. Full sub-rule verification against the L0 corpus and integration
testing with the sister theme `axpby-mutation-rotation` (specifically the
sub-pattern D / E composition path) deferred to `lowering-verifier`.

verified_against:
  - citation: palace/linalg/operator.hpp:21
    verdict: supports
    audited_at: 2026-05-27T02:53:54Z
    note: using Operator = mfem::Operator; real-operator alias, inherits abstract Mult from MFEM.
  - citation: palace/linalg/operator.hpp:54
    verdict: supports
    audited_at: 2026-05-27T02:53:54Z
    note: ComplexOperator::Mult pure virtual decl.
  - citation: palace/linalg/operator.hpp:56
    verdict: supports
    audited_at: 2026-05-27T02:53:54Z
    note: ComplexOperator::MultTranspose decl (default virtual; concrete subclasses override).
  - citation: palace/linalg/operator.hpp:58
    verdict: supports
    audited_at: 2026-05-27T02:53:54Z
    note: ComplexOperator::MultHermitianTranspose decl; complex-only by static type.
  - citation: palace/linalg/operator.hpp:60-67
    verdict: supports
    audited_at: 2026-05-27T02:53:54Z
    note: ComplexOperator AddMult / AddMultTranspose / AddMultHermitianTranspose decls; scalar a defaults to 1.0.
  - citation: palace/linalg/operator.hpp:202-206
    verdict: supports
    audited_at: 2026-05-27T02:53:54Z
    note: BaseProductOperator::Mult body B.Mult(x, z); A.Mult(z, y); witness of operator-composition via chained sub-pattern A.
  - citation: palace/linalg/operator.cpp:428-441
    verdict: supports
    audited_at: 2026-05-27T02:53:54Z
    note: SumOperator::Mult definition; size-1 fast path applies y *= c after Mult; size>1 path zeros y then calls AddMult (witness of L0 reuse pattern Mult-via-AddMult).
  - citation: palace/linalg/operator.cpp:458-466
    verdict: supports
    audited_at: 2026-05-27T02:53:54Z
    note: SumOperator::AddMult definition; loop over ops accumulates y.Add(a*c, z); shared with axpby-mutation-rotation citation set.
  - citation: palace/linalg/rap.cpp:195-234
    verdict: supports
    audited_at: 2026-05-27T02:53:54Z
    note: ParOperator::Mult definition; prolongation + inner A->Mult(lx, ly) at line 220 + restriction + dbc_tdof masking. Witness that even with the parallel wrapper the L1 form is preserved.
  - citation: palace/linalg/rap.cpp:277-318
    verdict: supports
    audited_at: 2026-05-27T02:53:54Z
    note: ParOperator::AddMult definition; same prolongation/restriction shape as Mult but with final accumulation step y.Add(a, ty) at line 317 (axpy-shaped, cited by sister theme).
```

```edit:book/src/L1/index.md
[no edit — this theme proposes no speculative L1 operators; the L1
dep-map already contains `apply_linop` as `firm` with no dependencies.
Per the abstractor role spec section "Output" item (b), this edit-stanza
applies only when speculative L1 operators are emitted. Documented here
as a deliberate no-op so integrator does not look for a missing diff.]
```

```edit:book/src/SUMMARY.md
[append a single line under the L1 > L0 Lowering Part, immediately after
the axpby-mutation-rotation line at SUMMARY.md:36, preserving the
existing bicgstab-iteration and minres-iteration entries below it]

--- a/book/src/SUMMARY.md
+++ b/book/src/SUMMARY.md
@@ -34,6 +34,7 @@
 # L1 > L0 — Lowering
 - [Overview](./L1-L0/index.md)
 - [axpby-mutation-rotation](./L1-L0/axpby-mutation-rotation.md)
+- [apply-linop-mutation-rotation](./L1-L0/apply-linop-mutation-rotation.md)
 - [bicgstab-iteration](./L1-L0/bicgstab-iteration.md)
 - [minres-iteration](./L1-L0/minres-iteration.md)
```

## Speculative operators proposed

**None.**

`apply_linop` is the firm L1 form (promoted in cycle-004,
`book/src/L1/apply_linop.md`); the five L0 sub-patterns decompose into
firm L1 vocabulary only — `apply_linop` for the forward / transposed /
Hermitian-transposed application, and `axpby` for the accumulating-mode
composition. The L1 variant-axis collapse design (transpose-mode and
accumulate-mode collapsed to algebraic transforms; operator-representation
absorbed) is precisely what makes this lowering theme need zero new
operators. By contrast, the existing rough-in obstruction themes
(`minres-iteration`, `bicgstab-iteration`) emit rough-ins because Palace
has no L0 anchor; here the anchors are abundant and the L1 abstractions
are settled.

This negative result is itself a signal worth recording: the variant-axis
collapse design at L1 (a recent methodology investment, cycle-004) pays
off here as a complete elimination of rough-in operators on a substantial
lowering theme. A future meta-cycle may want to mark this as a friction
ledger entry — "variant-axis collapse enables clean L1>L0 lowering" — but
that is meta-phase work, not abstractor work.

## Supporting evidence

Direct evidence ranges already enumerated in the theme's Verified-against
section above. Cross-reference summary:

- **L1 anchor**: `book/src/L1/apply_linop.md` (firm; cycle-004) —
  defines the five-axis collapse design (element-type, transpose-mode,
  accumulate-mode collapsed; operator-representation absorbed) that this
  lowering reintroduces as L0-only specialisations.
- **Sister theme**: `book/src/L1-L0/axpby-mutation-rotation.md` (cycle
  pilot-1 + cycle-004 refinements) — defines the inner-accumulation
  pattern (sub-patterns D, E reuse the `y.Add(...)` axpy step).
- **Open question source**: cycle-004 harvester flagged
  `apply-linop-lowering-theme-scope` ("L1>L0 lowering theme will be
  substantially larger than `axpby-mutation-rotation`") — this report
  addresses that question with a five-sub-pattern theme and explicit
  scoping: rectangular in (transpose-mode × accumulate-mode), shallow in
  algebraic depth, complete recognition coverage against the firm L1
  variant axes.

## Open questions / caveats

1. **Workspace-tensor reading at L0**. Concrete operator subclasses
   often own a `mutable` workspace member `z` (e.g.
   `SumOperator::z`, `palace/linalg/operator.hpp:120`;
   `BaseProductOperator::z`, `palace/linalg/operator.hpp:192`). The L1
   form has no notion of workspace; the L1>L0 lowering treats it as a
   private detail of the operator subclass. However, the workspace IS
   observable at L1 in one specific case: operator-composition
   (`A · B`) materialises the intermediate vector `B·x` and applies
   `A` to it. That intermediate is L1-visible (as the second argument
   to the outer `apply_linop` call) but its concrete storage (the
   `mutable z` member of `BaseProductOperator`) is L0-only. Worth
   noting in a future `lowering-verifier` audit: confirm the
   workspace-mention-and-erase pattern matches the L1
   operator-composition law (law 4 of `apply_linop`).

2. **`SumOperator::Mult` dispatching through `AddMult`** (line 439-440).
   The L0 source uses `Mult-via-AddMult` reuse for the multi-operator
   path: `y = 0.0; AddMult(x, y)`. At L1 the L0 expansion is
   `axpby(1, apply_linop(A, x), 0, 0)`, which reduces directly to
   `apply_linop(A, x)` by `axpby` law 3 (β=0 zeroes the y_old
   contribution; α=1 passes the input through). The L1 view is
   therefore identical to sub-pattern A — worth recording as a note in
   the theme but not a separate sub-pattern. The L0 reuse pattern is a
   transparent performance trick (avoids duplicating the accumulation
   loop).

3. **Preconditioner application is `apply_linop` too**. Palace's
   preconditioners (`amg`, `ams`, `jacobi`, `chebyshev`,
   `distrelaxation`, `blockprecond`, `gmg`, `hcurl`) are all concrete
   `Solver` / `mfem::Solver` subclasses that implement `Mult(x, y)`
   semantically as `y = M⁻¹ · x` (the action of the preconditioner). At
   L0 they form a parallel class hierarchy
   (`palace/linalg/solver.hpp`); at L1 their `apply_linop` view
   collapses with the operator-action view (a preconditioner IS a
   linear operator, just with a special construction). This theme does
   not cite the preconditioner hierarchy explicitly — those are
   covered as further realisations of sub-pattern A. A follow-up
   theme `solver-as-operator-application` may be warranted if the
   `Solver`-vs-`Operator` distinction proves load-bearing at L0; the
   `concepts/solver-as-operator.md` page is the existing narrative
   for this distinction.

4. **`ComplexWrapperOperator` lifting** (`operator.hpp:73-113`). A
   `ComplexOperator` whose internal representation wraps two real
   `Operator`s and dispatches the four-block real-imaginary
   multiplication. At L1 this is `complex-from-real-lift` (existing
   concept); the operator-side view is just `apply_linop` on a
   complex operator. Not a separate sub-pattern; recognition collapses
   with sub-pattern A on the `ComplexOperator` hierarchy.

5. **No new speculative L1 operators emitted** — see "Speculative
   operators proposed" above. The next harvester invocation does not
   need to act on this report; the next `lowering-verifier` invocation
   could audit it against the corpus.

6. **Two `.MultHermitianTranspose` default impls in
   `ComplexOperator`** (to-do, not verified this cycle). The base-class
   `MultHermitianTranspose` and `MultTranspose` are virtual (not
   pure-virtual) on `ComplexOperator`, so default implementations exist
   somewhere in `palace/linalg/operator.cpp`. The specific file:lines and
   the actual default behaviour (call-through-with-conjugation vs.
   abort vs. something else) were **not read this cycle**; the
   abstractor declines to speculate on the body. Routed to a
   `lowering-verifier` audit to locate and characterise the defaults.
   Not load-bearing for this theme's sub-pattern recognition.

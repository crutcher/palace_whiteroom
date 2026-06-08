---
edges:
  reference:
    - concepts/constructed-operators
    - concepts/constructed-operator-factory
    - concepts/solver-as-operator
    - concepts/ksp_solve
    - concepts/variant-absorption
    - L1/eigsolve
    - L1/divfree_projector
    - L1/floquet_correction
    - L1/jacobi-smoother
    - L1/chebyshev-smoother
    - L1/ksp_solve
    - L1-L0/eigsolve-mutation-rotation
---
# nested-constructed-operator-gate

A layer-pattern concept naming the structural shape in which a
[`constructed-operator`](./constructed-operators.md) gate's closure carries **one or
more further constructed-operator gates as sub-fields**. The outer gate's per-call
body invokes the inner gate(s) as opaque operator actions; the inner gate's own
iteration is never spelled out at the outer gate's resolution. This is the
*composition-of-gates* counterpart to [`constructed-operator-factory`](./constructed-operator-factory.md)
(which names the *construction* site of a single gate).

## Background

A *constructed-operator gate* (see [`constructed-operators`](./constructed-operators.md)
and [`solver-as-operator`](./solver-as-operator.md)) is a value materialised at
construction — an opaque handle that internalises one or more variant axes and is
invoked through a uniform operator interface. The basic shape is one gate over raw
operators and tensors: e.g. `chebyshev-smoother`'s closure carries `op.A :
LinearOperator[N, N]`, a **raw** operator (`book/src/L1/chebyshev-smoother.md:58`),
not a gate.

The *nested* shape is one level up: the closure's sub-field is **itself a gate**
(`Solver[A]`, `DivFreeSolver`, …), not a raw operator. The distinguishing test:

- **raw-operator field** → not nesting. `op.A : LinearOperator[N, N]`
  (`chebyshev-smoother`), `apply_linop`'s operand argument. The field is applied as a
  matrix-vector product; there is no inner solve loop.
- **gate field** → nesting. `E.linear : Solver[A]` (`eigsolve`), `P.ksp : Solver[P.M]`
  (`divfree_projector`). The field is itself a construction-bound solver carrying its
  own iteration, preconditioner, tolerances, and variant absorption.

The pattern is structural to the whole constructed-operator family — a solver
absorbs a preconditioner, an eigensolver absorbs an inner linear solver, a projector
absorbs an inner H1 solve — and it is load-bearing across the eigenmode pipeline (see
the transitive-nesting note below), which is why it earns a named concept rather than
ad-hoc per-instance prose.

## The cross-layer fidelity rule

The reason this shape needs a name is a **lowering discipline**: when an L_{n}>L_{n-1}
mutation-rotation theme lowers the outer gate, the inner gate's iteration **stays
interior to the inner gate's OWN lowering theme** and does not leak into the outer
theme. At the outer theme's resolution the inner gate is an **opaque action**:

- `divfree_projector`'s `ksp->Mult(rhs, psi)` is the opaque `K⁻¹` action; its CG
  iteration is interior to [`ksp_solve`](./ksp_solve.md) and does not appear in the
  divfree theme (`book/src/L1-L0/divfree-projector-mutation-rotation.md:108-113`).
- `eigsolve`'s ten `opInv->Mult(b, x)` call sites are each the opaque inner-solve
  action; each "rewrites by the firm `ksp-solve-mutation-rotation` theme"
  (`book/src/L1-L0/eigsolve-mutation-rotation.md:213-258`, the **core sub-pattern** of
  the eigsolve theme) — the inner solve's body is NOT re-narrated inside the eigsolve
  theme.

This is the "composed-not-inherited" remark at `book/src/L1/eigsolve.md:140`: the
outer gate *composes against* the inner gate (delegating to its theme) rather than
*inheriting* its body (re-spelling the iteration). The fidelity claim is that the
outer theme is faithful precisely **because** it treats the inner gate opaquely — the
nested iteration is the inner theme's concern, and the lowering of the whole is the
**composition** of the two adjacent-edge themes, not a single flattened rewrite. A
theme that re-spelled the inner iteration would double-count the rotation and lose the
single-point-of-truth for the inner gate.

## Firm instances

Three FIRM L1 operators exhibit the gate-carrying-gate shape; a fourth site is latent.

- **`eigsolve`** (firm structure) — **two** nested gates. The
  closure `E` binds `E.linear : Solver[A]` (the inner Krylov solver invoked per
  RCI / shell-matrix callback for spectral-transformation modes) and `E.projector :
  Maybe DivFreeSolver[ComplexVector]` (the optional divergence-free projector)
  (`book/src/L1/eigsolve.md:60`). The L1 entry already names the shape in prose: "the
  first L1 operator to compose two layers of constructed-operator absorption"
  (`book/src/L1/eigsolve.md:136`) and "structurally the same nesting pattern …
  composed-not-inherited" (`book/src/L1/eigsolve.md:140`). The theme's **core
  sub-pattern B** lowers each of the ten `opInv->Mult` inner-solve call sites through
  the firm [`ksp_solve`](./ksp_solve.md) theme
  (`book/src/L1-L0/eigsolve-mutation-rotation.md:213-258`). The eigsolve theme is
  `firm (structural)`; its `LinearSolveFailed` sub-part is a *separate*
  partly-constructive status concern about a discarded convergence status, **not**
  about the gate-nesting structure — the nesting (sub-pattern B) is itself firm and
  source-anchored, so `eigsolve` is a clean FIRM instance of this shape independent of
  that caveat.

- **`divfree_projector`** (firm) — **one** nested gate. The
  closure `P` binds `P.ksp : Solver[P.M]` (a CG solver bound to the ε-weighted H1
  mass-like operator `P.M` as both operator and preconditioner target), materialised
  at construction (`book/src/L1-L0/divfree-projector-mutation-rotation.md:193-198`).
  Its per-call `ksp->Mult(rhs, psi)` is the opaque inner H1 solve
  (`book/src/L1-L0/divfree-projector-mutation-rotation.md:108-113`,
  `book/src/L1/divfree_projector.md`).

- **`floquet_correction`** (firm) — **one** nested gate. The closure `F`
  binds `F.ksp : Solver[F.M_RT]` (a CG solver preconditioned by `JacobiSmoother`,
  bound to the RT vector-FE mass operator `F.M_RT` as both operator and
  preconditioner target), materialised at construction
  (`palace/linalg/floquetcorrection.cpp:60-67`). Its per-call `ksp->Mult(rhs, y)`
  is the opaque inner RT mass solve (`book/src/L1-L0/floquet-correction-mutation-rotation.md`
  Sub-pattern A, `book/src/L1/floquet_correction.md`). Structurally isomorphic to
  `divfree_projector` but strictly thinner (no boundary-zeroing, no gradient
  correction, no empty-boundary nullspace pin). Element-type scope-out:
  `<ComplexVector>` only (the first L1 nested-gate instance with a
  deliberately-narrowed element-type scope).

**Transitive nesting (three-deep) — two independent chains.** Both `eigsolve` and
`floquet_correction` close a three-level nested chain, confirming the pattern is
load-bearing across multiple pipelines (not eigsolve-incidental).

**Chain 1 (eigsolve pipeline).** `E.projector : Maybe DivFreeSolver` means the
`divfree_projector` gate is *itself* a sub-field of the `eigsolve` closure — so the
eigsolve and divfree instances are not merely parallel, they are transitively nested:

    eigsolve  ⊃  divfree_projector  ⊃  ksp_solve
      (E)            (E.projector)         (P.ksp)

The eigsolve outer loop carries a divfree projector, which carries its own inner CG
solve.

**Chain 2 (floquet pipeline).** `F.ksp.preconditioner = JacobiSmoother`, and via
[`solver-as-operator`](./solver-as-operator.md) the JacobiSmoother is itself a firm
L1 constructed-operator gate ([`jacobi-smoother`](../L1/jacobi-smoother.md)):

    floquet_correction  ⊃  ksp_solve  ⊃  jacobi-smoother
      (F)                    (F.ksp)        (F.ksp.preconditioner)

The driver-side floquet correction carries an inner CG solve, which carries a
diagonal-preconditioner gate. The fidelity rule applies at each edge of both chains:
each outer theme treats its inner gate opaquely. Two independent three-deep chains
is direct evidence the pattern is load-bearing across multiple pipelines, not
incidental to one.

**Latent site — `ksp_solve` `BaseKspSolver`-as-preconditioner.** `ksp_solve`'s
closure `K` binds a preconditioner `M⁻¹` (`book/src/L1/ksp_solve.md:31`). Via
[`solver-as-operator`](./solver-as-operator.md), a preconditioner **is-an** operator
and may itself be a `Solver`-typed handle (a nested `ksp` used as a preconditioner).
When `K.M⁻¹` is a `Solver`, `ksp_solve` is *also* gate-carrying-gate. The L1
`ksp_solve` entry types `M⁻¹` as a plain `LinearOperator[N, N]` and the
`ksp-solve-mutation-rotation` theme treats the preconditioner opaquely, so this is a
**latent** nesting site, not a confirmed firm instance (no concrete Palace site where a
`BaseKspSolver`'s preconditioner is itself a `BaseKspSolver` has been verified against
L0 source — flagged for a future harvester). The floquet pipeline's
`F.ksp.preconditioner = JacobiSmoother` realises the *non-ksp* form of this latent
site (the preconditioner IS a constructed-operator gate, just a `Smoother`-gate
rather than a `Solver`-gate); a future site with `BaseKspSolver`-as-preconditioner
would be the strict version.

## Relationship to siblings

- [`constructed-operator-factory`](./constructed-operator-factory.md) — **the
  materialisation site** of a single gate (consumes a config record + context, returns
  a typed gate). This page is the **composition** counterpart: a gate whose closure
  *carries* another gate that some factory already materialised. The factory answers
  "where is a gate built?"; nested-gate answers "what happens when a gate's field is
  another gate?".
- [`solver-as-operator`](./solver-as-operator.md) — the type-level rotation that lets
  an inner gate appear as an operator-typed sub-field (`Solver<OperType>` IS-A
  `OperType`), which is precisely what makes the latent `ksp_solve` preconditioner
  site possible.
- [`constructed-operators`](./constructed-operators.md) / [`variant-absorption`](./variant-absorption.md)
  — the absorption motif each gate (inner and outer) realises.

## See also

- [`ksp_solve`](./ksp_solve.md) — the innermost (solver) gate in eigsolve+divfree
  chains; the inner iteration's home theme.
- [`jacobi-smoother`](../L1/jacobi-smoother.md) — the innermost (smoother) gate in the
  floquet chain; the diagonal-preconditioner gate.
- `book/src/L1-L0/eigsolve-mutation-rotation.md` §"Sub-pattern B" — the two-gate
  instance's lowering (delegates to `ksp-solve-mutation-rotation`).
- `book/src/L1-L0/divfree-projector-mutation-rotation.md` §"Sub-pattern A" / §"Sub-pattern C"
  — the one-gate instance's lowering + closure-field materialisation.
- `book/src/L1-L0/floquet-correction-mutation-rotation.md` §"Sub-pattern A" / §"Sub-pattern C"
  — the floquet one-gate instance's lowering + closure-field materialisation; the
  second three-deep chain (floquet → ksp → jacobi-smoother).

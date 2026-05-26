# cg_preconditioning_framework

## Context

Palace's Krylov solvers (CG, GMRES, FGMRES) are composed through a small, layered set of C++ types: an abstract `Operator` / `ComplexOperator` interface; a `Solver<OperType>` shape that declares an approximate inverse is itself an operator; a single `MfemWrapperSolver` adapter that lifts any real `mfem::Solver` to a complex-aware preconditioner; and a `BaseKspSolver` wrapper that binds an `IterativeSolver` to a preconditioner and exposes the two-operator `SetOperators(op, pc_op)` convention. This slice dissects the framework in which CG (and its sibling Krylov methods) consume preconditioning, isolating it from the per-method iteration rules dissected in the `cg`, `gmres`, and `fgmres` slices. The slice exists so subsequent algorithmic slices can refer to the composition shape (constructed-operator factories; `(op, pc_op)` split; complex-from-real lift) by name instead of re-deriving it.

## Background

The composition surface implements the standard *right-* and *left-preconditioned* Krylov framework (Saad 2003, ch. 9): the Krylov method iterates on `A x = b` while a separate operator `M⁻¹` (the preconditioner) accelerates convergence by approximating `A⁻¹`. Palace's variants are:

- **Two-operator split**: the Krylov method runs against the true operator `op` (typically a matrix-free complex `K = a₀M + a₁C + a₂Σ_PEC`), while the preconditioner is constructed against a separate `pc_op` (typically a real-valued assembled approximation `Br + Bi`). This is standard practice for matrix-free Krylov over expensive complex operators (Saad 2003 §10.2; Knyazev 2001 §2 for the analogous preconditioned eigensolver split).
- **Complex-from-real lift**: the preconditioner for a complex `K` is applied component-wise to `{Re, Im}` of the residual via a real solver (BoomerAMG / AMS / sparse-direct), with a conjugate-aware sign flip on the imaginary part. This is the equivalent-real formulation (Day & Heroux 2001).
- **Geometric multigrid composition**: when an FE-space hierarchy is available, a single-level preconditioner (AMG, AMS, sparse-direct, Jacobi) is wrapped as the coarse solve of a `GeometricMultigridSolver` with Chebyshev smoothers per level (Trottenberg/Oosterlee/Schüller 2001 §2 V-cycle; Hiptmair & Xu 2007 for auxiliary-space smoothing).

Palace deviates from textbook framings in one notable way: the LEFT/RIGHT preconditioner-side axis is consumed at a single point (`InitialResidual` in `iterative.cpp`), and the per-step procedure of each Krylov flavour is variant-free in the preconditioner-side axis above that point. See [`variant-absorption`](../../concepts/variant-absorption.md).

## L0 — source facts

All citations are into `reference/palace/`.

### Operator interface

The real operator type is an alias for `mfem::Operator`; the complex operator is an abstract class exposing `{Height, Width, Mult, MultTranspose, MultHermitianTranspose, AddMult*, AssembleDiagonal, Real(), Imag(), IsReal(), IsImag()}` and the real/imag-part accessors that downstream wrappers use to dispatch on equivalent-real block structure. See [palace/linalg/operator.hpp:14-67](../../../../reference/palace/linalg/operator.hpp#L14-L67) (real alias + abstract complex) and [palace/linalg/operator.hpp:69-112](../../../../reference/palace/linalg/operator.hpp#L69-L112) (complex `Mult` family signatures).

### Operator-composition wrappers

A small algebra of typed wrappers around `OperType` is defined in [palace/linalg/operator.hpp:178-226](../../../../reference/palace/linalg/operator.hpp#L178-L226) (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`) and [palace/linalg/operator.hpp:295-357](../../../../reference/palace/linalg/operator.hpp#L295-L357) (`ComplexWrapperOperator`, `BaseMultigridOperator`). `BaseProductOperator::Mult(x, y)` uses a `mutable VecType z` scratch buffer with `B.Mult(x, z); A.Mult(z, y)`. `BaseMultigridOperator::Mult` forwards to `GetFinestOperator().Mult`; the inner levels exist for the preconditioner factory's consumption, not for the top-level `Mult`.

### Solver-as-operator

`Solver<OperType>` derives from `OperType` and adds `SetOperator(op)` (rebind) and an `initial_guess` flag (whether `Mult(x, y)` should treat `y` as a starting iterate). See [palace/linalg/solver.hpp:20-64](../../../../reference/palace/linalg/solver.hpp#L20-L64). This is the type-level statement that an approximate inverse IS-A operator.

### Complex-from-real lift

`MfemWrapperSolver<OperType>` lifts any real `mfem::Solver` (BoomerAMG, AMS, MUMPS, SuperLU, STRUMPACK, hypre direct) to a `Solver<OperType>`-shaped preconditioner. For `OperType = Operator` `Mult` is a passthrough; for `OperType = ComplexOperator` `Mult` runs the real solver on each of `{Re, Im}` and applies a `yi *= -1.0` sign flip on the imaginary part to recover the complex-conjugate-aware action. See [palace/linalg/solver.hpp:66-134](../../../../reference/palace/linalg/solver.hpp#L66-L134) and [palace/linalg/solver.cpp:139-177](../../../../reference/palace/linalg/solver.cpp#L139-L177).

### Iterative-solver preconditioner dispatch

The abstract `IterativeSolver<OperType>` holds a non-owning `B` pointer to the preconditioner; preconditioner application is funnelled through a single inline `ApplyB(B, x, y)` helper that wraps `B->Mult(x, y)` with a `Timer::KSP_PRECONDITIONER` block and a `MFEM_ASSERT(B, ...)` partial-function guard. See [palace/linalg/iterative.hpp:25-110](../../../../reference/palace/linalg/iterative.hpp#L25-L110), [palace/linalg/iterative.cpp:243-250](../../../../reference/palace/linalg/iterative.cpp#L243-L250) (`ApplyB`), and [palace/linalg/iterative.cpp:252-280](../../../../reference/palace/linalg/iterative.cpp#L252-L280) (`InitialResidual`, where LEFT vs RIGHT preconditioning is dispatched).

### Krylov-method factory

`ConfigureKrylovSolver<OperType>(linear, verbose, comm)` returns a `unique_ptr<IterativeSolver<OperType>>` by dispatching on `linear.krylov_solver ∈ {CG, GMRES, FGMRES}`. Restart dim, preconditioner side, and `gs_orthog` are bound at construction for GMRES/FGMRES; tolerances and `initial_guess` come from the same config record. See [palace/linalg/ksp.cpp:25-99](../../../../reference/palace/linalg/ksp.cpp#L25-L99). MINRES, BICGSTAB, DEFAULT abort.

### Preconditioner factory

`MakeWrapperSolver<OperType, T>(linear, args...)` wraps a concrete `mfem::Solver` subclass `T` in an `MfemWrapperSolver`, with `save_assembled` deduced at compile-time from `T` (false for SuperLU/STRUMPACK/MUMPS, true otherwise). See [palace/linalg/ksp.cpp:101-123](../../../../reference/palace/linalg/ksp.cpp#L101-L123).

`ConfigurePreconditionerSolver<OperType>(linear, verbose, comm, fespaces, aux_fespaces)` returns a `unique_ptr<Solver<OperType>>`. It dispatches on `linear.type ∈ {AMS, BOOMER_AMG, SUPERLU, STRUMPACK, STRUMPACK_MP, MUMPS, JACOBI}` to construct an inner preconditioner `pc`. If `fespaces.GetNumLevels() > 1`, `pc` is wrapped as the coarse solve of a `GeometricMultigridSolver<OperType>` with prolongation operators from the FE-space hierarchy and (optionally) discrete-gradient interpolators from `aux_fespaces` for auxiliary-space smoothing. The single-level path returns `pc` directly. See [palace/linalg/ksp.cpp:125-235](../../../../reference/palace/linalg/ksp.cpp#L125-L235). JACOBI does NOT go through `MakeWrapperSolver`; it is constructed directly as `JacobiSmoother<OperType>`.

### KSP wrapper and the (op, pc_op) split

`BaseKspSolver<OperType>` owns a `unique_ptr<IterativeSolver<OperType>> ksp` and a `unique_ptr<Solver<OperType>> pc`, bound in the constructor by `ksp->SetPreconditioner(*pc)`. See [palace/linalg/ksp.hpp:27-76](../../../../reference/palace/linalg/ksp.hpp#L27-L76) and [palace/linalg/ksp.cpp:240-296](../../../../reference/palace/linalg/ksp.cpp#L240-L296). `SetOperators(op, pc_op)` is the *two-operator* convention: `ksp` is bound to the true operator `op`, `pc` to the (possibly distinct, possibly real-approximation) preconditioner-assembly operator `pc_op`. See [palace/linalg/ksp.cpp:274-296](../../../../reference/palace/linalg/ksp.cpp#L274-L296) (the `SetOperators` body) and the `Mult` accumulation path at [palace/linalg/ksp.cpp:298-314](../../../../reference/palace/linalg/ksp.cpp#L298-L314). `SetOperators` contains a single piece of structural intelligence: when `pc_op` is a `BaseMultigridOperator` but the underlying `pc` is NOT a `GeometricMultigridSolver`, the wrapper unwraps `pc_op` to its finest-level operator before calling `pc->SetOperator`.

### Model-layer composition

`BaseKspSolver` is instantiated via one of two routes: (R1) auto-config delegating to `ConfigureKrylovSolver` + `ConfigurePreconditionerSolver`; (R2) direct injection of a pre-built `(ksp, pc)` pair (e.g. `SpaceOperator`'s CG+Jacobi for a boundary-mass solve, `ModeEigensolver`'s complex GMRES + block PC). See [palace/models/spaceoperator.cpp:634-643](../../../../reference/palace/models/spaceoperator.cpp#L634-L643) and [palace/models/modeeigensolver.cpp:460-470](../../../../reference/palace/models/modeeigensolver.cpp#L460-L470). Both routes converge on the same `ksp->SetPreconditioner(*pc)` bind, after which the model calls `SetOperators(op, pc_op)` with two semantically distinct operators (exact complex `K = a₀M + a₁C + a₂Σ_PEC` vs. real-approximation `Br + Bi`).

No unit tests cover `BaseKspSolver`, the `MfemWrapperSolver` complex-from-real lift, or `ConfigurePreconditionerSolver` directly. They are exercised through integration examples in `palace/test/examples/`.

## L1 — invariant statement

### Roles

- **`op : OperType`** — the operator the Krylov method iterates against. Represents `A` in `A x = b`.
- **`pc_op : OperType`** — the operator the preconditioner is constructed against. Distinct from `op` by design; typically a real-valued or coarsened approximation.
- **`pc : Solver<OperType>`** — an approximate inverse, itself an operator (`Solver<OperType>` derives from `OperType`). Calling `pc.Mult(r, z)` realises `z ≈ pc_op⁻¹ r`.
- **`ksp : IterativeSolver<OperType>`** — the Krylov iteration, parameterised by the krylov-method axis (CG / GMRES / FGMRES) and preconditioner-side axis (LEFT / RIGHT). Holds a non-owning pointer to `pc`.

### Invariant

A preconditioned Krylov solve produces `x` satisfying `op · x ≈ b` to the configured tolerance, where the iteration uses `pc` (an approximate inverse built against `pc_op`, not `op`) as its preconditioner. Convergence depends on the spectral relationship between `op` and `pc · pc_op`; correctness of the iteration's stopping test depends only on the residual `b − op · x`. See [`constructed-operators`](../../concepts/constructed-operators.md).

### Procedure

```
build_ksp_solver(linear_config, fespaces, aux_fespaces?):
    ksp ← configure_krylov(linear_config)               // CG | GMRES | FGMRES bound
    pc  ← configure_preconditioner(linear_config,       // AMS | AMG | sparse-direct | Jacobi
                                    fespaces,           //   wrapped in GMG iff fespaces.num_levels > 1
                                    aux_fespaces?)
    bind(ksp, pc)                                       // one-shot ksp.SetPreconditioner(pc)
    return BaseKspSolver{ksp, pc, counters: 0}

set_operators(solver, op, pc_op):
    ksp.SetOperator(op)                                 // Krylov iterates against op
    if pc_op is multigrid_op and pc is not GMG:         // structural adapter
        pc.SetOperator(finest_level(pc_op))             //   unwrap to finest
    else:
        pc.SetOperator(pc_op)                           // preconditioner built against pc_op

solve(solver, x, b):
    y ← ksp.Mult(x, b)                                  // delegates the iteration
    counters.mult       += 1
    counters.mult_it    += ksp.GetNumIterations()
    return y
```

### Variant axes

This slice exposes four orthogonal variant axes; each is absorbed by a constructed operator (see [`constructed-operators`](../../concepts/constructed-operators.md) and [`variant-absorption`](../../concepts/variant-absorption.md)).

1. **Krylov method ∈ {CG, GMRES, FGMRES}** — absorbed by `configure_krylov`. After construction, `ksp.Mult(x, b)` is uniform across choices; the per-method iteration logic lives in the `cg`, `gmres`, `fgmres` slices.
2. **Preconditioner type ∈ {AMS, BOOMER_AMG, SUPERLU, STRUMPACK, STRUMPACK_MP, MUMPS, JACOBI}** — absorbed by `configure_preconditioner` + `MfemWrapperSolver` (for all non-Jacobi cases). After construction, `pc.Mult(r, z)` is uniform; the inner type is hidden behind `Solver<OperType>`. JACOBI is constructed directly as `JacobiSmoother<OperType>`; this is an absorbed sub-case, not a residual axis.
3. **Multigrid composition ∈ {single-level pc, GMG-wrapping-pc}** — absorbed by `configure_preconditioner` based on `fespaces.num_levels`. The output is uniformly typed `unique_ptr<Solver<OperType>>`; the consumer (`BaseKspSolver`) cannot tell whether `pc` is a wrapper around a single-level solver or a multigrid V-cycle. The `SetOperators` `BaseMultigridOperator`-unwrap branch handles the asymmetric case where the model layer provides a multigrid `pc_op` but the config selected a single-level `pc`.
4. **Operand scalar field ∈ {real, complex}** — absorbed at two layers: at the `OperType` template parameter (compile-time), and at `MfemWrapperSolver::Mult` (run-time, where the complex-from-real lift applies a real solver to `{Re, Im}` with a conjugate-aware sign flip).

### Open questions

- **(op, pc_op) split as load-bearing rotation.** Should this slice claim the `(op, pc_op)` split as *the* structural rotation of Palace's KSP composition? Currently the invariant is implicit across `cg`, `gmres`, `divfree`. Hoisting it here would make those slices able to refer to it by name.
- **`BaseProductOperator` scratch reuse at L2.** The scratch `z` is `mutable` and aliased across calls; whether the L2 expansion of `apply_linop` on a product operator should disclose this explicitly or treat it as transparent is an L2-layer decision.
- **Multigrid-pc_op-without-GMG-pc.** Is there a model-layer invariant that should forbid this combination, making the `SetOperators` unwrap defensive rather than structural? Or is it an intended compatibility path?
- **No unit tests.** Coverage is integration-only via `palace/test/examples/`. Acceptable to note as an L0 evidence gap.

## L2 — primitive composition

The L1 procedure unfolds into a composition of named primitives drawn from `concepts/`. The L2 form makes the per-call primitive chain explicit; the variant-axis absorptions identified at L1 (krylov-method, preconditioner-type, multigrid-composition, scalar-field) remain hidden behind the constructed operators and the [`solver-as-operator`](../../concepts/solver-as-operator.md) bundle.

### Primitives in use

- [`apply_linop`](../../concepts/apply_linop.md) — the uniform operator-application primitive `y ← op.Mult(x)`. Used both for the Krylov-method operator `op` and for the preconditioner-as-operator `pc`.
- [`solver-as-operator`](../../concepts/solver-as-operator.md) — the type-level rotation that lets `pc.Mult(r, z)` be called through the same `apply_linop` shape as `op.Mult(x, y)`. The preconditioner is structurally just another operator at L2.
- [`constructed-operator-factory`](../../concepts/constructed-operator-factory.md) — the build-time primitive that consumes a config record and FE-space context and yields a typed operator (here, `ksp` and `pc`). The variant axis is consumed at the factory call; the output is uniform.
- [`complex-from-real-lift`](../../concepts/complex-from-real-lift.md) — the L2 unfolding of `MfemWrapperSolver::Mult` for `OperType = ComplexOperator`: two real solves on `{Re, Im}` with a conjugate-aware sign flip.
- [`finest-level-unwrap`](../../concepts/finest-level-unwrap.md) — the structural-adapter primitive used in `set_operators` to reconcile a multigrid `pc_op` with a non-multigrid `pc`.
- [`counter-update`](../../concepts/counter-update.md) — the bookkeeping primitive that accumulates `mult` and `mult_it` counters after a delegated solve.

### Building blocks

#### `build_ksp_solver` — factory composition

```
build_ksp_solver(linear_config, fespaces, aux_fespaces?):
    ksp ← constructed_operator_factory(
              role: "krylov",
              config: linear_config,
              variants: {method: linear_config.krylov_solver,
                         side:   linear_config.pc_side,
                         orthog: linear_config.gs_orthog,
                         restart: linear_config.max_size})
        // returns IterativeSolver<OperType>

    pc  ← constructed_operator_factory(
              role: "preconditioner",
              config: linear_config,
              variants: {type: linear_config.type,
                         multigrid: fespaces.num_levels > 1,
                         aux: aux_fespaces,
                         scalar_field: OperType})
        // returns Solver<OperType>; internally:
        //   pc_inner ← <AMS | BoomerAMG | sparse-direct | JacobiSmoother>
        //   if JACOBI:        pc ← pc_inner                                   (no wrapper)
        //   elif single-level: pc ← MfemWrapperSolver(pc_inner)               (complex-from-real lift)
        //   else:              pc ← GeometricMultigridSolver(coarse: MfemWrapperSolver(pc_inner),
        //                                                    P: fespaces.prolongations,
        //                                                    G: aux_fespaces.discrete_gradients?)

    ksp.bind_preconditioner(pc)         // one-shot, non-owning pointer install
    return BaseKspSolver{ksp, pc, counters: {mult: 0, mult_it: 0}}
```

The two factory calls are independent. Both produce `Solver<OperType>` or `IterativeSolver<OperType>`; the consumer sees uniform types and dispatches through `apply_linop`. The four variant axes (krylov-method, pc-type, multigrid, scalar-field) are consumed inside the factories and not re-inspected downstream.

#### `set_operators` — operator binding with structural adapter

```
set_operators(solver, op, pc_op):
    solver.ksp.SetOperator(op)
    pc_op_for_pc ← if is_multigrid(pc_op) and not is_multigrid_solver(solver.pc)
                     then finest_level_unwrap(pc_op)
                     else pc_op
    solver.pc.SetOperator(pc_op_for_pc)
```

The `finest_level_unwrap` is the only L2 primitive in this slice that exists purely to bridge an asymmetry between the two factory outputs (multigrid `pc_op` provided by the model layer vs. single-level `pc` selected by the config). It is named here so downstream slices can refer to it by name rather than re-deriving the asymmetry.

#### `solve` — delegated iteration with counter update

```
solve(solver, x_initial, b):
    x_out ← apply_linop(solver.ksp, b)            // ksp.Mult(x_initial, b) under solver-as-operator
    counter_update(solver.counters.mult,    +1)
    counter_update(solver.counters.mult_it, +solver.ksp.GetNumIterations())
    return x_out
```

The per-method iteration body (CG / GMRES / FGMRES) is hidden inside `apply_linop(solver.ksp, b)` — the krylov-method variant axis has been fully absorbed by `build_ksp_solver`'s factory call. The L2 form of the per-method iteration lives in the `cg`, `gmres`, and `fgmres` slices respectively.

#### `apply_preconditioner` (internal, called by the per-method iterations)

```
apply_preconditioner(solver, r, z):
    // Called inside the Krylov iteration whenever it needs B*r. Funnelled through a single site.
    z ← apply_linop(solver.pc, r)
    // For complex OperType + non-multigrid pc, this expands to:
    //   complex-from-real-lift(pc.inner_real_solver, r.Re → z.Re,
    //                                                r.Im → z.Im (with sign flip on Im))
    // For multigrid pc, this expands to the V-cycle body.
    // The caller sees only `z ← apply_linop(pc, r)`.
```

This is the L2 primitive site at which the LEFT vs RIGHT preconditioner-side axis is consumed (per the L0 evidence in `iterative.cpp` `InitialResidual`). The Krylov-method slices' L2 forms reference `apply_preconditioner(solver, r, z)` by name without re-inspecting the variant.

### Mutation pattern

The L2 primitives in this slice are pure-functional at the L2 surface:

- `apply_linop(op, x)` is treated as `y ← op.Mult(x)` returning a fresh result; the L0 evidence shows internal scratch (`BaseProductOperator::Mult`'s `mutable z`) which is an L2-transparent implementation detail of the operator, not of the caller.
- `counter_update` is in-place by signature; the `+= 1` and `+= n` mutation pattern is implicit in the primitive's name.
- `bind_preconditioner` installs a non-owning pointer; the `pc` lifetime is owned by `BaseKspSolver`, not by `ksp`. The L2 form treats this as a one-shot side-effecting bind that establishes a shared-reference invariant for the lifetime of the solver.

### What L2 hides relative to L1

The L1 procedure named `configure_krylov` and `configure_preconditioner` as opaque factory calls. The L2 form rotates this by:

1. **Naming the factory primitive**: both calls are instances of [`constructed-operator-factory`](../../concepts/constructed-operator-factory.md), which is shared with the per-method-slice L2 forms. The L1 form had one factory call per role; the L2 form has one factory primitive with role + variants parameters.
2. **Naming the bind primitive**: `ksp.SetPreconditioner(pc)` is rotated to `ksp.bind_preconditioner(pc)`, exposing it as a one-shot side-effecting primitive distinct from per-iteration `apply_linop` calls.
3. **Naming the unwrap primitive**: the L1 `if pc_op is multigrid_op and pc is not GMG` branch is rotated to a named [`finest-level-unwrap`](../../concepts/finest-level-unwrap.md) primitive, making the structural adapter a citable name for downstream slices.
4. **Exposing the apply-funnel**: the L1 form spoke only of `solve`; the L2 form discloses that the per-iteration preconditioner application (called from inside the Krylov-method L2 forms) is uniformly `apply_linop(solver.pc, r)`. The LEFT/RIGHT side axis is consumed *at the call site inside the iteration*, not at the bind.

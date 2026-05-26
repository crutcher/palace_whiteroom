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

## L3 — tensor-field / global form

The L2 primitives compose into a global form that operates on whole-vector tensor fields. The L3 layer asks: when the per-element iteration is lifted to a global tensor-field operation, what survives, and what (if anything) remains genuinely sequential?

This slice's L3 is unusual: the framework dissected here is **structural plumbing** (factory composition, operator binding, counter accumulation, structural-adapter unwrap), not numerical iteration. The per-element / per-iteration numerical work lives in the `cg`, `gmres`, `fgmres` slices, whose own L3 forms handle their respective tensor-field lifts. The composition surface itself is point-free in the tensor-field sense — it never iterates over vector components.

### Primitive-by-primitive lift

| L2 primitive                          | L3 status                                                 |
|----------------------------------------|-----------------------------------------------------------|
| `apply_linop(op, x)`                   | Already global. `op` acts on whole vectors; no per-element iteration to lift. See [`apply_linop`](../../concepts/apply_linop.md). |
| `apply_linop(pc, r)`                   | Already global, by [`solver-as-operator`](../../concepts/solver-as-operator.md). The preconditioner is an operator; its `Mult` is a whole-vector map. |
| `complex-from-real-lift`               | Global. The lift acts on the `{Re, Im}` whole-vector pair as a single complex-vector tensor-field operation. The sign flip on `Im` is a global `scal(-1, y.Im)`. |
| `constructed-operator-factory`         | **Build-time, not run-time.** The factory runs once per solve session at construction. No tensor-field lift applies — it is not an inner-loop primitive. |
| `bind_preconditioner`                  | **Build-time, not run-time.** One-shot side-effecting pointer install. No tensor-field lift applies. |
| `finest-level-unwrap`                  | **Build-time, not run-time.** Structural-adapter executed once at `set_operators`. No tensor-field lift applies. |
| `counter-update`                       | Scalar accumulation; trivially global (no per-element structure). |

The takeaway: **every L2 primitive in this slice is either already global, or is build-time and outside the scope of the tensor-field lift.** There is no per-element iteration in the framework slice to lift.

### Global form of `solve`

```
solve_global : (Solver, Vec, Vec) → (Vec, Counters)
solve_global(solver, x_initial, b) =
    let x_out = apply_linop(solver.ksp, b)          -- whole-vector iteration delegated to ksp
        n_it  = solver.ksp.GetNumIterations()
    in (x_out, solver.counters ⋄ {mult: +1, mult_it: +n_it})
```

The whole-vector character is inherited from `apply_linop(solver.ksp, b)`: the krylov-method's own L3 form (in `cg`, `gmres`, `fgmres`) defines what tensor-field operations run inside that call. The framework slice does not see them — variant absorption holds at L3 as it did at L2.

### Global form of `apply_preconditioner`

```
apply_preconditioner_global : (Solver, Vec) → Vec
apply_preconditioner_global(solver, r) = apply_linop(solver.pc, r)
```

For `OperType = ComplexOperator` with a non-multigrid `pc`, this expands to:

```
apply_linop(MfemWrapperSolver(real_solver), r) =
    let z_re = apply_linop(real_solver, r.Re)
        z_im = apply_linop(real_solver, r.Im)
    in {Re: z_re, Im: scal(-1, z_im)}
```

Both `apply_linop(real_solver, ·)` calls are whole-vector applications of the real preconditioner; `scal(-1, z_im)` is a whole-vector negation. The complex-from-real lift is a pointwise composition of three global operations on the `{Re, Im}` pair. See [`complex-from-real-lift`](../../concepts/complex-from-real-lift.md).

For `OperType = ComplexOperator` with a multigrid `pc`, the expansion is the V-cycle body, which is the `geometric_multigrid` slice's responsibility (out of scope here).

### Sequential obstruction — none in this slice

The framework slice carries **no sequential obstruction** in the [`sequential-obstruction`](../../concepts/sequential-obstruction.md) sense — every L2 primitive is either build-time (outside the lift) or already global at L2. The sequential obstructions that DO arise in preconditioned Krylov solves (Gauss-Seidel smoothers, triangular solves in ILU, sequentially-reordered preconditioners) live inside the concrete preconditioner types and surface in their respective slices (`jacobi-smoother`, `geometric_multigrid`, `ams`, `amg`), not in the composition surface.

This is itself a structural observation worth recording: **the composition framework is L3-trivial precisely because it dispatches through `apply_linop` uniformly.** The variant-absorption that hides AMS/AMG/sparse-direct/Jacobi behind `Solver<OperType>` at L1 simultaneously hides whatever sequential obstructions those preconditioners carry — they are L3-opaque to this slice.

### Build-time vs. run-time separation

The L3 rotation makes a distinction the L2 form left implicit: **`build_ksp_solver` and `set_operators` are build-time composition, not tensor-field operations.** They construct and bind the operator graph; they do not iterate. Only `solve` and `apply_preconditioner` are run-time, and both are already global at L2.

This separation matters for downstream L4 work: the build-time primitives belong in the **constructor / setup phase** of the L4 [`solve-monad`](../../concepts/solve-monad.md) statement, while the run-time primitives belong in the **monadic body**. The L4 form will carry this stratification explicitly.

### What L3 hides relative to L2

The L2 form named six primitives, three build-time and three run-time. The L3 form rotates this by:

1. **Stratifying build-time from run-time**: the L3 form makes explicit that only `apply_linop` and its expansions (including `complex-from-real-lift`) are tensor-field operations; `constructed-operator-factory`, `bind_preconditioner`, `finest-level-unwrap` are build-time scaffolding that doesn't participate in the lift.
2. **Recording the no-obstruction result**: the framework slice has no `sequential-obstruction` claim because all its run-time primitives are global at L2. This is a first-class negative L3 result per the prompt's L2→L3 guidance: "Where no global form exists ... record an OBSTRUCTION claim. Negative L3 results are first-class output." Here the symmetric positive result — no obstruction — is also first-class.
3. **Preserving variant absorption**: the four variant axes (krylov-method, pc-type, multigrid, scalar-field) remain absorbed at L3. The L3 form does not re-inspect them; whatever per-element iteration each variant unfolds to is delegated to the relevant slice's L3.

## L4 — calculus form

The L3 form left an important structural observation: the framework slice cleanly stratifies into **build-time composition** (`build_ksp_solver`, `set_operators`, `finest-level-unwrap`) and **run-time iteration** (`solve`, `apply_preconditioner`). This stratification is the load-bearing rotation at L4: it maps directly onto the [`solve-monad`](../../concepts/solve-monad.md)'s constructor-vs-body split, and onto the [`state-stratification`](../../concepts/state-stratification.md) discipline that separates operator internal params (built once) from sim state (advanced per iteration) from ephemeral intermediates (per-step scratch).

### State stratification

Following [`state-stratification`](../../concepts/state-stratification.md), the L4 form carries three disjoint state categories:

```ts
// Operator internal params — built once at construction, immutable through the solve.
type KspParams<E> = {
  ksp_method: "CG" | "GMRES" | "FGMRES",
  pc_side: "LEFT" | "RIGHT",
  gs_orthog: "MGS" | "CGS2",
  restart_dim: number,
  tol_rel: number,
  tol_abs: number,
  max_it: number,
  initial_guess: boolean,
};

type PcParams<E> = {
  pc_type: "AMS" | "BOOMER_AMG" | "SUPERLU" | "STRUMPACK" | "STRUMPACK_MP" | "MUMPS" | "JACOBI",
  multigrid: boolean,             // fespaces.num_levels > 1
  aux_smoothing: boolean,         // aux_fespaces present
  scalar_field: "real" | "complex",
};

// The constructed operators themselves (typed handles, internal state opaque).
type Ksp<E>    = IterativeSolver<E> & { params: KspParams<E> };
type Pc<E>     = Solver<E>          & { params: PcParams<E> };

// Sim state — the operators the solver is bound to.
type OpBinding<E> = {
  op:    Op<E>,        // what ksp iterates against
  pc_op: Op<E>,        // what pc is built against (distinct by design)
};

// Bookkeeping — accumulated across calls.
type Counters = {
  mult:    number,     // number of Mult invocations
  mult_it: number,     // total inner iterations
};

// The full solver bundle.
type BaseKspSolver<E> = {
  ksp:      Ksp<E>,
  pc:       Pc<E>,
  binding:  OpBinding<E> | null,   // null before set_operators
  counters: Counters,
};
```

Ephemeral intermediates (per-iteration residuals, search directions, Krylov bases, Givens accumulators) live inside `Ksp<E>`'s internal state and are not surfaced at this layer — they belong to the `cg`, `gmres`, `fgmres` slices' L4 forms.

### Constructor phase (build-time)

The build phase is **pure** in the [`solve-monad`](../../concepts/solve-monad.md) sense — no iteration state flows through it. It is a sequence of constructed-operator-factory calls and a one-shot bind:

```haskell
buildKspSolver :: LinearConfig -> FESpaceHierarchy -> Maybe AuxFESpaces -> BaseKspSolver E
buildKspSolver cfg fes auxFes =
  let ksp = constructedOperatorFactory KrylovRole cfg     -- absorbs ksp_method, pc_side, orthog, restart
      pc  = constructedOperatorFactory PrecondRole cfg fes auxFes
                                                          -- absorbs pc_type, multigrid, aux, scalar_field
      _   = bindPreconditioner ksp pc                     -- one-shot side effect on ksp internals
  in BaseKspSolver { ksp, pc, binding = Nothing, counters = Counters 0 0 }

setOperators :: Op E -> Op E -> BaseKspSolver E -> BaseKspSolver E
setOperators op pc_op s =
  let pc_op' = if isMultigridOp pc_op && not (isMultigridSolver s.pc)
                 then finestLevelUnwrap pc_op
                 else pc_op
      _      = s.ksp `setOpInternal` op
      _      = s.pc  `setOpInternal` pc_op'
  in s { binding = Just (OpBinding op pc_op) }
```

The constructor returns a fully-bound `BaseKspSolver<E>`. The two factory calls are independent; the [`variant-absorption`](../../concepts/variant-absorption.md) of all four variant axes (krylov-method, pc-type, multigrid, scalar-field) completes inside the factories and is not re-inspected downstream.

### Body phase (run-time, monadic)

The body phase runs inside the [`solve-monad`](../../concepts/solve-monad.md). Counter updates thread state monadically; the operator application is delegated to `ksp` whose own L4 form (in the per-method slices) carries the iteration's state:

```haskell
solve :: BaseKspSolver E -> Vec E -> Vec E -> Solve E (Vec E)
solve s x_initial b = do
  x_out <- applyLinop s.ksp b                  -- delegates to ksp's per-method body
  n_it  <- getNumIterations s.ksp
  modifyCounters $ \c -> c { mult    = c.mult    + 1
                           , mult_it = c.mult_it + n_it }
  return x_out

applyPreconditioner :: BaseKspSolver E -> Vec E -> Solve E (Vec E)
applyPreconditioner s r = applyLinop s.pc r
  -- For E = Complex with non-multigrid pc, applyLinop on Pc<Complex> unfolds via
  -- complex-from-real-lift:
  --   applyLinop pc r = do
  --     z_re <- applyLinop pc.inner r.re
  --     z_im <- applyLinop pc.inner r.im
  --     return (Complex z_re (scal (-1) z_im))
```

The `Solve E` monad threads the counter state; vector results are returned pure-functionally at this layer. The per-iteration state (residuals, Krylov bases) is hidden inside `applyLinop s.ksp b` — that call is the boundary at which the framework slice's L4 form hands off to the per-method slice's L4 form.

### What L4 hides relative to L3

The L3 form named the build-time vs run-time stratification as a structural observation. The L4 form rotates this by:

1. **Type-level stratification.** The three state categories (`KspParams`/`PcParams` immutable, `OpBinding` set-once, `Counters` monadically threaded) are distinct types. A consumer cannot accidentally mutate operator params from inside the monadic body, nor can it skip the bind. The [`state-stratification`](../../concepts/state-stratification.md) discipline is enforced by the type system, not by convention.
2. **Constructor/body monadic split.** `buildKspSolver` returns a pure value; `solve` runs in the `Solve E` monad. The build-time primitives (`constructedOperatorFactory`, `bindPreconditioner`, `finestLevelUnwrap`) cannot appear inside the monadic body — the type signatures forbid it. This makes the L3 observation ("build-time primitives are outside the tensor-field lift") a type-level invariant at L4.
3. **Capability typing for the binding.** `binding: OpBinding<E> | null` captures the pre/post-`setOperators` distinction. A `solve` call on a `BaseKspSolver` with `binding = Nothing` is a type error at L4. This formalises the L0 assertion-guard (`MFEM_ASSERT(B, ...)`) as a structural precondition.
4. **Variant absorption carries through.** The four variant axes do not appear in `BaseKspSolver<E>`'s body-phase type. They live inside `KspParams<E>` and `PcParams<E>` as immutable construction-time fields. The body phase has no branching on variant; the polymorphism is fully type-erased at L4.

### Open questions

- **`Solve E` monad shape.** The framework slice does not pin down the full `Solve E` monad — it threads counters and delegates inner state to `ksp`. Whether `Solve E` should be a single monad shared across all Palace iterative solvers, or a per-method family parameterised over the Krylov method, is a calculus-level question for [`solve-monad`](../../concepts/solve-monad.md).
- **Capability typing of `pc_op` distinctness.** ~~The `(op, pc_op)` split is currently a *convention* — nothing in the type prevents `pc_op = op`. Should L4 carry a capability marker distinguishing "true operator" from "pc-assembly operator", or is this load-free flexibility?~~ **Resolved in L4 v0.2 below**: brand-typed `TrueOp<E>` and `PcAssemblyOp<E>` markers added; the role distinction is now a type-level invariant.
- **Build-time vs run-time as a methodology concept.** The stratification observed here recurs in `gmres` (Hessenberg vs iterate), `geometric_multigrid` (level setup vs V-cycle), and almost every operator-algebra construction. A dedicated [`build-time-run-time-stratification`](../../concepts/state-stratification.md) concept may be worth extracting, distinct from `state-stratification` (which is run-time-only).

## L4 v0.2 — capability typing for the (op, pc_op) split

The L4 v0.1 form (above) carried the `(op, pc_op)` distinction as a *naming* convention only: both fields of `OpBinding<E>` were typed `Op<E>`, and nothing in the type prevented `pc_op = op` or, worse, the two being silently swapped. This was flagged in the L4 v0.1 open questions as a capability-typing gap.

The within-L4 rotation here tightens the binding type to disambiguate the two roles by capability marker, without changing the run-time semantics. The rotation is L4→L4 (a self-tightening — see [`rotation`](../../concepts/rotation.md) on within-layer refinement) because it does not change which primitives compose the body phase, only the type at which the binding state is held.

### Capability markers

```ts
// Phantom-typed capability brands on the operator handle. Erased at run time;
// the underlying value is just Op<E>.
type TrueOp<E>      = Op<E> & { readonly __cap: "true" };
type PcAssemblyOp<E> = Op<E> & { readonly __cap: "pc_assembly" };

// Smart constructors brand a raw Op<E> with its intended role.
declare function asTrueOp<E>(o: Op<E>):       TrueOp<E>;
declare function asPcAssemblyOp<E>(o: Op<E>): PcAssemblyOp<E>;

type OpBinding<E> = {
  op:    TrueOp<E>,         // what ksp iterates against
  pc_op: PcAssemblyOp<E>,   // what pc is built against
};
```

The two branded types are nominally distinct. `setOperators` consumes them in role-positional form; passing a `PcAssemblyOp<E>` where a `TrueOp<E>` is expected (or vice-versa) is a type error at L4. The brand discipline is internal to the framework slice — model-layer callers brand the operators at construction time (one call each to `asTrueOp` and `asPcAssemblyOp`) and the brands flow through unchanged.

### `setOperators` under capability typing

```haskell
setOperators :: TrueOp E -> PcAssemblyOp E -> BaseKspSolver E -> BaseKspSolver E
setOperators op pc_op s =
  let pc_op' = if isMultigridOp pc_op && not (isMultigridSolver s.pc)
                 then finestLevelUnwrap pc_op            -- returns PcAssemblyOp E
                 else pc_op
      _      = s.ksp `setOpInternal` op                  -- accepts TrueOp E
      _      = s.pc  `setOpInternal` pc_op'              -- accepts PcAssemblyOp E
  in s { binding = Just (OpBinding op pc_op) }
```

`finestLevelUnwrap` is typed `PcAssemblyOp E -> PcAssemblyOp E` — the brand is preserved across the structural adapter because the unwrapped finest level inherits the pc-assembly role from its multigrid parent. This is the load-bearing observation: the L0 evidence at `palace/linalg/ksp.cpp:274-296` only ever applies the unwrap to `pc_op`, never to `op`, so the brand-preserving signature matches the source.

### What this rotation hides

The L4 v0.1 form left two equally-typed `Op<E>` fields and relied on field-name discipline (`op` vs `pc_op`) to keep the two operators distinct. The L4 v0.2 form rotates this by:

1. **Lifting field-name discipline to type-level discipline.** A caller cannot accidentally pass the true operator where the pc-assembly operator is expected. The bug that the L0 assertion-guards cannot catch (because both are `Operator*` at the C++ layer) is type-rejected at L4.
2. **Naming the brand-preservation invariant of `finestLevelUnwrap`.** The structural adapter is now typed as a `PcAssemblyOp`-endomorphism. Downstream slices that compose with the framework (e.g., a future `divfree` L4 form) can rely on this signature.
3. **Making the (op, pc_op) distinctness a calculus-level fact rather than a slice-level convention.** The L4 v0.1 open question asked whether the split was "load-free flexibility"; v0.2 answers: it is load-bearing enough that brand-typing it catches a class of misuse the L0 type system cannot.

The rotation does NOT add capability state to the run-time `BaseKspSolver<E>`: brands are phantom (zero-runtime). The body-phase signatures of `solve` and `applyPreconditioner` are unchanged; the brand discipline lives entirely in the constructor/setOperators surface.

### What this rotation does NOT yet address

- **Spectral-relationship invariants.** The L1 form noted that convergence depends on the spectral relationship between `op` and `pc · pc_op`. The capability typing here distinguishes the *roles* of `op` and `pc_op` but does not encode any spectral-equivalence invariant between them. That would require a refinement-type or proof-carrying layer beyond the current L4 calculus.
- **`pc_op = op` as a valid configuration.** Some model-layer call sites legitimately pass the same operator for both roles (when the true operator is itself cheap enough to precondition against directly). The brand discipline does NOT forbid `asTrueOp(K)` and `asPcAssemblyOp(K)` being applied to the same underlying `K` — it only forbids passing one brand where the other is expected. This is the intended escape hatch.
- **The `Solve E` monad shape.** Still deferred to [`solve-monad`](../../concepts/solve-monad.md). Capability typing on the binding is orthogonal to the monad-shape question.

The v0.1 open question on capability typing is now resolved (positively: brands ARE worth carrying); the other two v0.1 open questions (`Solve E` monad shape, build-time-vs-run-time as a methodology concept) remain open.

## L4 v0.3 — derived-view hoisting for the (op, pc_op) bundle

The L4 v0.1 and v0.2 forms left a structural ambiguity in `OpBinding<E>` that surfaces once the brand discipline of v0.2 is in place: the `pc_op` field as stored on `OpBinding<E>` is the *raw* operator handed to `setOperators`, but the operator actually bound into `pc` via `setOpInternal` is sometimes the `finestLevelUnwrap(pc_op)` result rather than `pc_op` itself. The two values can diverge by one structural level (a `BaseMultigridOperator` wrapper) whenever the model layer provides a multigrid `pc_op` to a non-multigrid `pc`. A consumer that reads `s.binding.pc_op` and a consumer that reads the operator bound inside `s.pc` will see *different* operators in that branch — a hazard that v0.2's brand typing does not catch (both values carry the `PcAssemblyOp<E>` brand).

The L4→L4 rotation here applies the [`derived-view-hoisting`](../../concepts/derived-view-hoisting.md) discipline: the binding state is restructured so that the stored fields are the *primitive* inputs and the *unwrap-adapted* operators are exposed as derived views computed from them. The rotation is within-layer (L4→L4) because the body-phase primitives and the run-time semantics are unchanged; only the schema of the binding state changes.

### Restructured `OpBinding<E>`

```ts
// Primitive (stored) fields: the operators as the model layer handed them in.
// These are the only fields modified by `setOperators`; everything else is derived.
type OpBinding<E> = {
  op:    TrueOp<E>,            // primitive: as passed by the caller
  pc_op: PcAssemblyOp<E>,      // primitive: as passed by the caller (may be a multigrid wrapper)
};

// Derived view: the operator actually bound into `pc` after the structural adapter.
// Computed from `pc_op` plus the type of `pc`; never stored.
declare function pcBoundOp<E>(
  binding: OpBinding<E>,
  pc:      Pc<E>,
): PcAssemblyOp<E>;
// pcBoundOp(b, pc) =
//   if isMultigridOp(b.pc_op) && !isMultigridSolver(pc) then finestLevelUnwrap(b.pc_op)
//   else b.pc_op
```

The derived view is a *function* of the stored binding plus the solver's `pc` field; it is recomputed on demand and never cached. The L0 evidence at `palace/linalg/ksp.cpp:274-296` shows the unwrap happening exactly once per `SetOperators` call, but at L4 the rotation treats this as a derived-view recomputation rather than a one-shot side effect — the value bound into `pc` is whatever `pcBoundOp` would currently return for the binding-and-pc pair, regardless of how it got there.

### `setOperators` after the hoist

```haskell
setOperators :: TrueOp E -> PcAssemblyOp E -> BaseKspSolver E -> BaseKspSolver E
setOperators op pc_op s =
  let binding'   = OpBinding op pc_op                       -- primitives stored verbatim
      pc_bound   = pcBoundOp binding' s.pc                  -- derived view
      _          = s.ksp `setOpInternal` op
      _          = s.pc  `setOpInternal` pc_bound
  in s { binding = Just binding' }
```

The structural adapter no longer appears as a branch in `setOperators`'s body; it lives entirely inside the `pcBoundOp` derived view's definition. `setOperators` becomes a record-construction plus two `setOpInternal` calls whose arguments are obtained by primitive read (`op`) and derived-view evaluation (`pc_bound`).

### What this rotation hides

The L4 v0.2 form carried the structural adapter as a branch inside `setOperators`, threading the unwrapped operator through a `pc_op'` intermediate and then storing the *original* `pc_op` in the binding. This produced a subtle invariant the type system did not enforce: the value in `s.binding.pc_op` is the model-layer input, but the value bound into `s.pc` may be one structural level deeper. The v0.3 rotation hides this by:

1. **Eliminating the stored-vs-bound divergence.** There is no longer a `pc_op'` intermediate to disagree with the stored `pc_op`. The binding holds exactly the primitive inputs; everything else is recoverable by derived-view evaluation. See [`derived-view-hoisting`](../../concepts/derived-view-hoisting.md) — derived state is recomputed, not cached.
2. **Naming `pcBoundOp` as a first-class derived view.** Downstream consumers (debug introspection, model-layer reconciliation checks, future capability-typed solver compositions) can call `pcBoundOp(binding, pc)` to recover the unwrapped operator without re-implementing the unwrap branch. The structural adapter has exactly one definition site.
3. **Making the v0.2 `finestLevelUnwrap` brand-preservation invariant a derived-view property.** Because `pcBoundOp` is the only path from `(binding, pc)` to the operator bound into `pc`, the `PcAssemblyOp<E>`-endomorphism brand property of `finestLevelUnwrap` is locally checkable inside the derived view's definition — no caller needs to reason about brand preservation across `setOperators`'s body.

### What this rotation does NOT change

- **Run-time semantics.** `setOpInternal` is called with exactly the same operator value as in v0.2; only the route by which that value is computed has been hoisted into a derived view. The C++ source at `palace/linalg/ksp.cpp:274-296` is unchanged in scope.
- **Brand discipline.** The v0.2 `TrueOp<E>` / `PcAssemblyOp<E>` brands are preserved; the rotation is orthogonal to capability typing.
- **The `(op, pc_op)` distinctness escape hatch.** `pc_op = op` (with the same underlying operator double-branded) still works; `pcBoundOp` returns the unbranded `op` in that case (no multigrid wrapper to unwrap).

### Connection to the v0.1 open question on build-time-vs-run-time

The derived-view hoist sharpens the v0.1 open question on extracting a [`build-time-run-time-stratification`](../../concepts/state-stratification.md) concept: `pcBoundOp` is a *build-time* derived view (it changes only when `setOperators` is called or the `pc` type changes, neither of which happens in the monadic body), distinct from per-iteration ephemeral derived views (like the GMRES Krylov-basis-from-Hessenberg case in the `gmres` slice's L4). A future methodology concept could classify derived views by recomputation frequency: build-time (this slice), per-solve (model-layer reconciliation), per-iteration (Krylov internals). For now this is a noted parallel, not an extracted concept.

The v0.1 open question on capability typing was resolved by v0.2; the v0.1 open questions on `Solve E` monad shape and build-time-vs-run-time-as-methodology remain open. v0.3 adds no new open questions.

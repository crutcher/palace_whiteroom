# File — `palace/linalg/iterative.{hpp,cpp}`

A reference note for the L1 `ksp_solve` operator (anticipated cycle-007+) and the L2 [`krylov-step`](../L2/krylov-step.md) entry. The home of Palace's three implemented Krylov solvers — `CgSolver`, `GmresSolver`, `FgmresSolver` — plus the abstract base `IterativeSolver<OperType>` they all share. Sibling to [`ksp-factory-file`](./ksp-factory-file.md) (which is the *construction* side of the same surface) and consumed by [`kspsolver-base-class`](./kspsolver-base-class.md) (the `ksp` field of `BaseKspSolver<OperType>` is one of the three concrete subclasses declared here).

## At a glance

The `.hpp` (279 lines) declares four classes; the `.cpp` (882 lines) defines them plus a handful of free-function helpers in the anonymous namespace. The class hierarchy is shallow but layered:

```text
mfem::Solver         (real-only, MFEM-supplied)
   ^
Solver<OperType>     (templated; palace/linalg/solver.hpp)
   ^
IterativeSolver<OperType>   (abstract base; iterative.hpp:25-115)
   ^      ^      ^
   |      |      |
CgSolver  GmresSolver  FgmresSolver   (concrete; iterative.hpp:117-275)
                         ^
                         |
                         (FgmresSolver further specialises GmresSolver)
```

The `OperType` template parameter is `Operator` (real) or `ComplexOperator` (complex), constrained by the `static_assert` chain inherited from `Solver<OperType>`. Each class therefore yields two concrete instantiations (`CgSolver<Operator>`, `CgSolver<ComplexOperator>`, etc.), all explicitly instantiated at the bottom of `iterative.cpp:873-880`.

## `IterativeSolver<OperType>` — the abstract base

Declared at `iterative.hpp:25-115`. Three categories of state:

- **Configuration** — `comm` (MPI communicator), `print_opts` / `int_width` / `tab_width` (printing), `rel_tol` / `abs_tol` (convergence tolerances), `max_it` (iteration cap), `use_timer` (RAII timing flag).
- **Operator references** — `A` (the system operator, owned externally; `iterative.hpp:49`) and `B` (the optional preconditioner, also owned externally; line 50). Both are raw `const` pointers — `IterativeSolver` doesn't own the operator graph, only references it.
- **Per-solve statistics** — `converged`, `initial_res`, `final_res`, `final_it` (lines 53-55). All declared `mutable` so they can be written by the `const`-method `Mult` body — see [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) for the convention.

The base class declares accessors and mutators for all of the above, plus the central `SetOperator(const OperType &op)` override (`iterative.hpp:87-92`, which just stores `A = &op` and propagates `op.Height()` / `op.Width()` to the inherited `Operator`'s height/width fields) and `SetPreconditioner(const Solver<OperType> &pc)` (line 95, which stores `B = &pc`). The pure-virtual `Mult` is inherited from `Solver<OperType>` (which inherits it from `OperType`) — each concrete subclass overrides it with its solver-specific iteration loop.

## `CgSolver<OperType>` — Preconditioned Conjugate Gradient

Declared at `iterative.hpp:117-150`; `Mult` body at `iterative.cpp:360-486`. Per-solve workspace (declared `mutable`, line 144):

```text
mutable VecType r, z, p;
```

Three vectors — `r` (residual), `z` (preconditioned residual), `p` (search direction). Allocated lazily at the start of each `Mult` call via `SetSize(A->Height())` (lines 369-371) and configured for device storage via `UseDevice(true)` (lines 372-374); the second and subsequent `Mult` calls reuse the storage allocated on the first call. This is a canonical [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) instance.

The body is a textbook PCG implementation: initialise (`r = b - A·x`, `z = B⁻¹·r`, `p = z`, `β = ⟨z, r⟩`, `α = β / ⟨A·p, p⟩`); per-step update (`x += α·p`, `r −= α·A·p`, `z = B⁻¹·r`, `β_new = ⟨z, r⟩`, `p = z + (β_new/β)·p`); convergence test (`res < eps`). The body is the canonical L0 instance of the L2 [`krylov-step`](../L2/krylov-step.md) `Step` kernel: each iteration is one `apply_linop` + two `axpy`-shaped updates + one `dot` for the new `β`, all wrapped in a `for` loop that lifts to the L4 `iterate_while` combinator.

A `CheckDot` helper (defined in the anonymous namespace, `iterative.cpp:21-32`) is called after each `Dot` computation to guard against the preconditioner becoming non-SPD — `(Br, r) ≤ 0` aborts the solve with an explanatory message. This is a load-bearing classification: CG's algebraic precondition (SPD `A`, SPD `B`) is enforced at runtime; non-SPD inputs are caught here rather than silently producing garbage.

## `GmresSolver<OperType>` — Preconditioned GMRES

Declared at `iterative.hpp:152-217`; `Mult` body at `iterative.cpp:543-705`. Workspace is larger because GMRES carries the entire Krylov subspace explicitly:

```text
mutable std::vector<VecType> V;   // Arnoldi basis vectors
mutable VecType r;                // residual
mutable std::vector<ScalarType> H;    // Hessenberg matrix entries (column-major)
mutable std::vector<ScalarType> s, sn;    // Givens-rotation sines + RHS state
mutable std::vector<RealType> cs;     // Givens-rotation cosines
```

The `mutable int max_dim` field (`iterative.hpp:180`) is the restart dimension (`m` in standard GMRES notation); `gs_orthog` selects modified-Gram-Schmidt / classical-Gram-Schmidt / iterated-classical-Gram-Schmidt for the orthogonalisation step (`iterative.hpp:184`); `pc_side` selects left or right preconditioning (line 187).

The `Initialize()` / `Update(j)` protected virtuals (lines 197-198) own the workspace allocation and the per-restart-cycle resizing. They're virtual so `FgmresSolver` can override them to add its `Z` array (flexible-preconditioner basis).

The body's outer structure is the standard restarted GMRES loop: build the Arnoldi basis `V[0..j]` via orthogonalisation against the previous columns, transform the Hessenberg `H[0..j, 0..j]` to upper-triangular by Givens rotations, track the residual via the rotated RHS, restart when `j == max_dim` or convergence. The Arnoldi step itself decomposes as one `apply_linop` (or `apply_linop ∘ pc_apply` depending on `pc_side`) + a `for` loop of `dot` + `axpy` pairs over the existing basis — again the L2 [`krylov-step`](../L2/krylov-step.md) kernel, but with the outer driver consuming a Givens-stream rather than a scalar-recurrence (see the cycle-005 `krylov-step` chapter's §"GMRES-Givens-stream sub-instance" note).

## `FgmresSolver<OperType>` — Flexible GMRES

Declared at `iterative.hpp:219-275`; `Mult` body at `iterative.cpp:733-870`. A thin specialisation of `GmresSolver` that adds one extra workspace array:

```text
mutable std::vector<VecType> Z;   // flexible-preconditioner basis (one per Arnoldi step)
```

The flexible-preconditioner extension records the preconditioned vector at each Arnoldi step (`Z[j] = B⁻¹·V[j]`) rather than only the un-preconditioned basis. This lets the preconditioner be non-constant across iterations (e.g. a nested iterative solver whose tolerance varies per outer step); the cost is `O(m)` extra vectors of storage.

The class overrides `Initialize` / `Update` to allocate and resize the `Z` array alongside the inherited `V` array, then defers everything else to `GmresSolver`'s machinery. The constructor (`iterative.hpp:262-266`) fixes `pc_side = PreconditionerSide::RIGHT` (FGMRES only supports right-preconditioning algebraically); the overridden `SetPreconditionerSide` (`iterative.hpp:268-272`) aborts on any attempt to change this.

## Free-function helpers (anonymous namespace)

Several template helpers in `iterative.cpp` lines 21-325 (the anonymous namespace) factor out element-type-aware primitives:

- **`CheckDot`** (`iterative.cpp:21-32`) — guards `Dot` results against non-positivity in CG (catches non-SPD preconditioner or operator); has separate real and complex specialisations.
- **`ApplyB`** (`iterative.cpp:243-250`) — wraps `B->Mult(x, y)` in an optional `BlockTimer(Timer::KSP_PRECONDITIONER, use_timer)` to attribute preconditioner time separately from the outer KSP time.
- **`InitialResidual`** (`iterative.cpp:252-285`) — computes the initial residual `r = b - A·x` (or its preconditioned form `r = B·(b - A·x)` under `PreconditionerSide::LEFT`); branches on whether the caller supplied an initial guess.
- **`ApplyBA`** (`iterative.cpp:287-305`) — combined preconditioner + operator apply for the GMRES inner step; selects between `B·A·x` and `A·B·x` based on `pc_side`.
- **`OrthogonalizeIteration`** (`iterative.cpp:307-325`) — per-step Gram-Schmidt orthogonalisation against the existing basis; dispatches via `switch` on `Orthogonalization::MGS` / `CGS` / `CGS2` per `gs_orthog`, delegating to `linalg::OrthogonalizeColumnMGS` / `linalg::OrthogonalizeColumnCGS` (defined in `linalg/orthog.hpp`).
- **Sundry small-dense linear-algebra utilities** (`iterative.cpp:34-241`) — Givens-rotation generation (`GeneratePlaneRotation` real + complex), Givens-rotation application (`ApplyPlaneRotation` real + complex), `SafeMin` / `SafeMax` numeric-limit helpers. These feed the GMRES/FGMRES outer driver's small-dense kernel; see the cycle-002 `incremental-least-squares` concept page.

## Notes for higher layers

- **The three concrete `Mult` bodies are the L0 anchors for the L2 [`krylov-step`](../L2/krylov-step.md) entry** — each is a `for` loop over an L2 `krylov-step` kernel composition, wrapped by the convergence test and the per-restart logic. The L1 `ksp_solve` operator (anticipated cycle-007+) collapses the full method body to `ksp_solve(solver, b) → x where A·x = b`; the iterative-vs-direct nature is an opaque property of the `solver` value at L1.
- **Workspace allocation is lazy and reuse-based** — every `mutable` member is `SetSize`-resized at the start of each `Mult` call and persists across calls. The `UseDevice(true)` calls on the workspace vectors keep them GPU-resident when device execution is active. The L1>L0 lowering theme for `ksp_solve` will need to record this (workspace mutation is the canonical [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) instance — preconditions + lifecycle preserved by transparent allocation).
- **`CheckDot` is load-bearing** — non-SPD precondition violation on CG is a load-bearing algebraic constraint, not a transparent optimisation. The L1 form of `ksp_solve(CG, ...)` carries an SPD-precondition contract that `CheckDot` enforces at L0; lifting the contract into the type system is an L4 typing-rule question.
- **The orthogonalisation choice is a variant axis** — `Orthogonalization::MGS` / `CGS` / `CGS2` differ in numerical stability vs collective-communication count (MGS is one `dot` + one `axpy` per existing basis vector and serial; CGS is one block-`dot` then one block-`axpy`, parallel-friendly but less stable; CGS2 reorthogonalises). Currently a member-variable choice; at L1 it's a variant of the GMRES solver value, at L4 it's a parameter of the `solve-monad` constructor for GMRES.
- **`max_dim = -1` is a sentinel meaning "no restart"** — GMRES without a restart cap accumulates the full Krylov subspace for as many iterations as it takes. This is rare in practice (`max_dim` is typically set via `SetRestartDim` from the KSP factory); the sentinel allows the implementation to skip the restart-bookkeeping branch.

## Referenced from

*Forward-declared. The L1 `ksp_solve` operator (queued cycle-007+) and the L4 `solve-monad` concept page will reference this chapter when they reach the per-solver-class detail.*

- [`L2/krylov-step`](../L2/krylov-step.md) — the per-step kernel that the three concrete `Mult` bodies all instantiate.
- [`L0/kspsolver-base-class`](./kspsolver-base-class.md) — the composition class that owns one of these concrete iterative solvers as its `ksp` field.
- [`L0/ksp-factory-file`](./ksp-factory-file.md) — the factory functions (`ConfigureKrylovSolver`) that construct the concrete iterative-solver objects.
- [`L0/apply-linop-overload-set`](./apply-linop-overload-set.md) — the `Operator` / `ComplexOperator` interface whose `Mult` method is the per-step primitive these iterative solvers invoke.
- [`L0/mutable-workspace-pattern`](./mutable-workspace-pattern.md) — sibling reference note for the lazy-allocation / re-use convention that all three concrete subclasses follow.
- [`concepts/solve-monad`](../concepts/solve-monad.md) — the L4 abstraction over the construction-then-apply flow these solvers participate in.
- [`concepts/incremental-least-squares`](../concepts/incremental-least-squares.md) — the small-dense kernel that GMRES/FGMRES consume in their outer driver.

## Evidence (representative)

- `palace/linalg/iterative.hpp:25-115` — `IterativeSolver<OperType>` abstract base class declaration: configuration state (lines 35-58), `SetOperator` override (87-92), `SetPreconditioner` (95), convergence accessors (98-108).
- `palace/linalg/iterative.hpp:53-55` — `mutable` per-solve statistics (`converged`, `initial_res`, `final_res`, `final_it`).
- `palace/linalg/iterative.hpp:117-150` — `CgSolver<OperType>` declaration; workspace `mutable VecType r, z, p` at line 144.
- `palace/linalg/iterative.hpp:152-217` — `GmresSolver<OperType>` declaration; workspace `mutable std::vector<VecType> V` (190) + `mutable VecType r` (191) + Hessenberg + Givens state (192-194).
- `palace/linalg/iterative.hpp:219-275` — `FgmresSolver<OperType>` declaration; additional workspace `mutable std::vector<VecType> Z` (256); right-preconditioning constraint at lines 263-272.
- `palace/linalg/iterative.cpp:21-32` — `CheckDot` helper (non-positivity guard for CG; real and complex specialisations).
- `palace/linalg/iterative.cpp:34-241` — small-dense kernel helpers: `SafeMin` / `SafeMax`, `GeneratePlaneRotation` (real + complex), `ApplyPlaneRotation` (real + complex).
- `palace/linalg/iterative.cpp:243-250` — `ApplyB` helper (preconditioner-only apply with optional timing).
- `palace/linalg/iterative.cpp:252-285` — `InitialResidual` helper (initial residual computation with `PreconditionerSide`-aware branching).
- `palace/linalg/iterative.cpp:287-305` — `ApplyBA` helper (combined preconditioner + operator apply, `pc_side`-aware).
- `palace/linalg/iterative.cpp:307-325` — `OrthogonalizeIteration` helper (MGS / CGS / CGS2 dispatch over `linalg::OrthogonalizeColumn{MGS,CGS}`).
- `palace/linalg/iterative.cpp:360-486` — `CgSolver<OperType>::Mult` definition; workspace lazy-allocation at lines 369-374; initialisation at 376-419; inner loop at 427-464; convergence summary at 470-485.
- `palace/linalg/iterative.cpp:443` — `A->Mult(p, z)` (the per-step `apply_linop` invocation; downstream call site for [`apply-linop-overload-set`](./apply-linop-overload-set.md)).
- `palace/linalg/iterative.cpp:488-516` — `GmresSolver<OperType>::Initialize` definition (workspace pre-allocation).
- `palace/linalg/iterative.cpp:518-541` — `GmresSolver<OperType>::Update(j)` definition (per-step workspace resize).
- `palace/linalg/iterative.cpp:543-705` — `GmresSolver<OperType>::Mult` definition.
- `palace/linalg/iterative.cpp:707-731` — `FgmresSolver<OperType>::Initialize` and `Update(j)` definitions (extend `GmresSolver`'s with `Z` array bookkeeping).
- `palace/linalg/iterative.cpp:733-870` — `FgmresSolver<OperType>::Mult` definition.
- `palace/linalg/iterative.cpp:873-880` — explicit template instantiations for all four classes × both `OperType`s.

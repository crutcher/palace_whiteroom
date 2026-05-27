# Convention — `mutable` workspace members for in-place reuse

A reference note for L1 entries and L1>L0 mutation-rotation themes. Names a pervasive Palace / MFEM C++ convention: operator subclasses and iterative-solver subclasses declare per-instance scratch vectors (and other small state) as `mutable` members so they can be allocated lazily on first use and re-used across subsequent `const`-method calls. The pattern is a transparent performance optimisation that has no L1 semantic content but appears in every L1>L0 lowering theme whose L0 form has more than one step.

## At a glance

C++ requires that `const`-method bodies not modify non-`mutable` members. Palace's operator and solver methods are typically `const` (the operator value itself is logically constant once constructed), but they require temporary storage to compute intermediate values. The idiom resolves the tension by declaring scratch members `mutable`:

```cpp
class SumOperator : public Operator
{
private:
  std::vector<std::pair<const Operator *, double>> ops;
  mutable Vector z;   // <-- workspace, mutable to allow lazy resize in const Mult
public:
  void Mult(const Vector &x, Vector &y) const override;   // <-- const method
  ...
};
```

The `mutable Vector z` member is empty after construction. The `Mult` body's first action is `z.SetSize(y.Size())`; subsequent invocations of `Mult` reuse the already-allocated buffer (MFEM `Vector::SetSize` is a no-op when the requested size equals the current size). This means:

- **Zero allocation cost** on subsequent calls (the buffer persists in the member).
- **No allocation contention** in tight inner loops (the buffer is per-instance, not per-call).
- **Implicit lifetime tied to the owning object** (no manual deallocation needed; destructor handles it).

The pattern is uniform across the codebase. Below are the four primary categories where it appears.

## Category 1 — operator-composition workspaces

Operator subclasses that internally chain sub-operator applications need a vector to hold the intermediate result. The canonical instance is [`BaseProductOperator`](./apply-linop-overload-set.md) (`operator.hpp:178-226`):

```cpp
mutable VecType z;
...
void Mult(const VecType &x, VecType &y) const override
{
  B.Mult(x, z);   // <-- writes the workspace
  A.Mult(z, y);   // <-- reads the workspace
}
```

The workspace `z` carries the `B·x` intermediate. At L1 this composition is the law `apply_linop(A·B, x) = apply_linop(A, apply_linop(B, x))` — the workspace materialises the intermediate `apply_linop(B, x)`, but at L1 that intermediate is the *argument* to the outer `apply_linop`, not a separate storage concern. The L0 workspace mention erases at L1 by the [`output-arg-vs-receiver`](./output-arg-vs-receiver.md) rewrite plus value-naming.

[`SumOperator`](./apply-linop-overload-set.md) (`operator.hpp:116-136`) has the same shape: `mutable Vector z` holds the per-operator partial product before accumulation into `y`. `SumOperator::AddMult` (`operator.cpp:458-466`) demonstrates the lazy-resize idiom:

```cpp
z.SetSize(y.Size());   // lazy alloc / no-op on subsequent calls
for (const auto &[op, c] : ops)
{
  op->Mult(x, z);
  y.Add(a * c, z);
}
```

[`ComplexWrapperOperator`](./apply-linop-overload-set.md) (`operator.hpp:73-113`) has two workspaces (`mutable ComplexVector tx, ty` at line 81) because its `Mult` body does *both* `(Ar - i·Ai) · (Re x + i·Im x)` — two real applies and a sign-correcting combine.

## Category 2 — iterative-solver per-iteration state

The three Krylov solvers in [`linalg-iterative-file`](./linalg-iterative-file.md) hold their per-iteration workspace as `mutable` members of varying complexity:

- `CgSolver` (`iterative.hpp:144`): `mutable VecType r, z, p` — residual, preconditioned residual, search direction.
- `GmresSolver` (`iterative.hpp:190-194`): `mutable std::vector<VecType> V` (Arnoldi basis) + `mutable VecType r` + `mutable std::vector<ScalarType> H` (Hessenberg) + Givens-rotation state (`s, sn, cs`).
- `FgmresSolver` (`iterative.hpp:256`): inherits all of `GmresSolver`'s plus `mutable std::vector<VecType> Z` (flexible-preconditioner basis).

The `IterativeSolver<OperType>` base class itself holds **per-solve statistics** as `mutable` (`iterative.hpp:53-55`):

```cpp
mutable bool converged;
mutable double initial_res, final_res;
mutable int final_it;
```

These are not workspace per se — they are *outputs* of the `Mult` call that the caller reads via the public `GetConverged()` / `GetInitialRes()` / etc. accessors after `Mult` returns. The same `mutable` discipline applies: the public method is `const` (the solver object's *configuration* doesn't change across solves), but the *statistics* do; making them `mutable` lets the body write them.

Lazy allocation here is more elaborate. Each `Mult` body starts with `r.SetSize(A->Height())` etc. (`iterative.cpp:369-374` for CG); GMRES factors the allocation into a virtual `Initialize()` method (`iterative.cpp:488-516`) that's called once per restart cycle. The `UseDevice(true)` calls that accompany the `SetSize` are the GPU-residency annotations — they make the workspace live on the device when device execution is active.

## Category 3 — solver workspaces

[`FloquetCorrSolver`](./apply-linop-overload-set.md) (`floquetcorrection.hpp:49`) has `mutable VecType rhs` — a workspace to hold the right-hand side of the inner linear solve. The pattern recurs in `arpack.hpp:88, 215`, `slepc.hpp:83, 302`, `nleps.hpp:72, 265` — every eigensolver wrapper that needs scratch vectors carries them as `mutable` members.

## Category 4 — assembled-matrix retention

`MfemWrapperSolver` (`solver.hpp:80`) retains the assembled `HypreParMatrix` across `SetOperator` / `Mult` calls:

```cpp
std::unique_ptr<mfem::HypreParMatrix> A;   // assembled matrix retained per SetOperator
```

This is *not* `mutable` because `SetOperator` is not a `const` method (it modifies the solver's bound operator); the assembled matrix lifetime is tied to that of the operator binding. Different sub-pattern from Categories 1-3, but the same underlying logic: the storage is allocated lazily (only when `SetOperator` is called, and not on every `Mult`), and re-used until invalidated.

## Lifecycle semantics

The lifecycle of a `mutable` workspace member is precisely:

1. **Constructed empty.** Default-constructor for the type (`Vector()`, `ComplexVector()`, `std::vector<VecType>()`) — zero-sized.
2. **First-call `SetSize` allocates.** The first `Mult` (or `AddMult`, or `Initialize`) body calls `z.SetSize(N)`; MFEM allocates an `N`-element buffer (possibly on the device if `UseDevice(true)` has been called).
3. **Subsequent-call `SetSize` is a no-op when `N` is unchanged.** Same buffer is reused.
4. **`SetSize(N')` with `N' > N` reallocates.** MFEM reallocates to `N'`. (Common when a solver is reused on a system of different size.)
5. **Owning-object destructor frees.** When the `SumOperator` / `CgSolver` / etc. goes out of scope, the `mutable` member's destructor runs and frees the buffer.

The pattern is **not thread-safe across the `mutable` member**. Two threads invoking `Mult` on the same instance simultaneously would race on the workspace. Palace's threading model assumes one thread per solver instance (operator applies and KSP solves are not internally threaded across `Mult` calls); the workspace lifecycle is single-writer-at-a-time.

## Notes for higher layers

- **L1 view: erase the workspace.** The `mutable` member appears in *no* L1 form. L1 operators are pure functions; intermediate values are named via let-binding or composed via function application. The L1>L0 lowering theme records the workspace mention as a transparent allocation pattern, **not** as a sub-pattern variant.
- **L1>L0 lowering themes acknowledge the workspace once.** The existing [`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md) theme (cycle-005) cites the `BaseProductOperator::Mult` body's `B.Mult(x, z); A.Mult(z, y)` shape and records the workspace `z` as L0-only state separating the two sub-applies. The general L1>L0 rewrite rule: **workspace members named by the L0 body but not appearing in the L1 form are transparent allocations**; they don't constitute separate sub-patterns.
- **Cross-cutting verification.** A future `lowering-verifier` audit (see open question `apply-linop-workspace-tensor-reading-at-L0`, cycle-005) should confirm that the workspace-mention-and-erase rewrite rule is consistently applied across all L1>L0 themes whose L0 forms use `mutable` workspaces.
- **The `mutable` statistics on `IterativeSolver` are a distinct case** — they are *outputs* of the operation, not workspace. The L1 form of `ksp_solve` (anticipated cycle-007+) will need to decide whether the convergence-status output is part of the return value or a side channel; see the cycle-005 entry `solver-as-operator` for the algebraic discussion.
- **GPU-device residency** (`UseDevice(true)` calls accompanying every workspace `SetSize`) is below the L1 abstraction. At L1 vectors live in an unspecified storage; the device-vs-host placement is part of the lowering to MFEM operations, not part of the algebraic semantics.

## Referenced from

*Forward-declared. The L1>L0 lowering themes covering operator-composition-shaped L0 forms will cite this chapter rather than re-stating the lazy-allocation discipline per theme.*

- [`L1-L0/apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md) — explicitly mentions the workspace `z` in the `BaseProductOperator::Mult` discussion; the workspace-mention-and-erase rewrite is one of the lowering rules this chapter formalises.
- [`L0/apply-linop-overload-set`](./apply-linop-overload-set.md) — names the concrete operator subclasses (`SumOperator`, `BaseProductOperator`, `ComplexWrapperOperator`) whose workspaces are Category-1 instances.
- [`L0/linalg-iterative-file`](./linalg-iterative-file.md) — names the concrete iterative solvers (`CgSolver`, `GmresSolver`, `FgmresSolver`) whose workspaces are Category-2 instances.
- [`L0/mfem-wrapper-solver`](./mfem-wrapper-solver.md) — Category-4 instance (the retained `HypreParMatrix`).
- [`L0/output-arg-vs-receiver`](./output-arg-vs-receiver.md) — sibling convention chapter; together they cover the mutation-shape rewriting that L1 forms apply to L0 bodies.
- [`L0/transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md) — the classification scheme; the `mutable` workspace pattern is uniformly transparent.

## Evidence (representative)

Spread across the linalg/ subtree. Representative anchors for each category:

- `palace/linalg/operator.hpp:81` — `ComplexWrapperOperator::tx, ty` (Category 1: complex-operator composition workspaces).
- `palace/linalg/operator.hpp:120` — `SumOperator::z` (Category 1: sum-of-operators workspace).
- `palace/linalg/operator.hpp:192` — `BaseProductOperator::z` (Category 1: operator-composition workspace).
- `palace/linalg/operator.hpp:123-124` — `SumOperator` constructor calling `z.UseDevice(true)` (GPU-residency annotation at construction; lazy `SetSize` on first use).
- `palace/linalg/operator.hpp:199` — `BaseProductOperator` constructor calling `z(B.Height())` (pre-allocates because the size is known at construction; still calls `UseDevice(true)`).
- `palace/linalg/operator.hpp:202-206` — `BaseProductOperator::Mult` body reading and writing `z`.
- `palace/linalg/operator.cpp:418` — `SumOperator(const Operator &op, double a)` constructor calling `z.UseDevice(true)`.
- `palace/linalg/operator.cpp:458-466` — `SumOperator::AddMult` definition with `z.SetSize(y.Size())` lazy-resize on line 460.
- `palace/linalg/operator.cpp:468-476` — `SumOperator::AddMultTranspose` (mirror of `AddMult`).
- `palace/linalg/floquetcorrection.hpp:49` — `FloquetCorrSolver::rhs` (Category 3: solver workspace).
- `palace/linalg/iterative.hpp:53-55` — `IterativeSolver` `mutable` per-solve statistics (`converged`, `initial_res`, `final_res`, `final_it`).
- `palace/linalg/iterative.hpp:144` — `CgSolver::r, z, p` (Category 2: CG workspace).
- `palace/linalg/iterative.hpp:190-194` — `GmresSolver::V, H, s, sn, cs` + `r` (Category 2: GMRES workspace).
- `palace/linalg/iterative.hpp:256` — `FgmresSolver::Z` (Category 2: FGMRES extra workspace).
- `palace/linalg/iterative.cpp:369-374` — `CgSolver::Mult` body lazy-resize + `UseDevice(true)` for `r`, `z`, `p`.
- `palace/linalg/solver.hpp:80` — `MfemWrapperSolver::A` (Category 4: retained assembled matrix; not `mutable`, but same lazy-construction discipline).
- `palace/linalg/arpack.hpp:88` — `mutable ComplexVector x1, y1, z1` (Category 3: ARPACK wrapper workspace).
- `palace/linalg/slepc.hpp:83` — `mutable ComplexVector x1, y1` (Category 3: SLEPc wrapper workspace).
- `palace/linalg/nleps.hpp:72, 265` — `mutable ComplexVector x1, y1` and `mutable ComplexVector rhs` (Category 3: NLEPS wrapper workspaces).

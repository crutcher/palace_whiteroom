# lu-solve-mutation-rotation

The mutation rotation for the small-dense direct linear solve. Lowers the pure L1 form
`x = lu_solve(A, b)` ([`L1/lu_solve`](../L1/lu_solve.md), firm) into Palace's L0 surface — an
**inline Eigen dense factorize-and-solve overwriting the RHS buffer in place**. There is **no
`palace/linalg/lu.cpp`**: `lu_solve` is realized inline at its two L0 use families via Eigen
dense-decomposition method chains — `S.fullPivLu().solve(·)` in the eigensolver deflation
(`palace/linalg/nleps.cpp`) and `Ar.fullPivHouseholderQr().solve(·)` in the ROM online
evaluation (`palace/models/romoperator.cpp`). Unlike the BLAS-1
[`dot`](./dot-mutation-rotation.md) / [`nrm2`](./nrm2-mutation-rotation.md) reductions (whose
result is a returned scalar, no destination buffer), `lu_solve`'s L0 form **does have a
destination buffer** — the RHS argument is overwritten by the solution (`SS = -S.fullPivLu()
.solve(SS)`, `RHSr = Ar.fullPivHouseholderQr().solve(RHSr)`: the destination *is* the RHS). What
the theme records is (1) the expansion of one pure direct-solve step into the L0
**transient-factorization-object + back-substitution** two-step the L1 signature hides, (2) the
in-place RHS-buffer overwrite (the "mutation" the rotation undoes), and (3) the
**factorization-kernel variant axis** (full-pivot LU vs full-pivot Householder QR vs rejected
LDLT) as a *load-bearing numerical* choice. Sibling on the "solve a linear system" axis to
[`ksp-solve-mutation-rotation`](./ksp-solve-mutation-rotation.md) (the large-sparse iterative
counterpart), split by the dense-direct vs sparse-iterative representation/cost distinction.

## Slug

`lu-solve-mutation-rotation`

## L1 form (LHS)

The pure-functional direct solve consumes a read-only dense square matrix and a read-only RHS,
producing a fresh solution; nothing is mutated. The LHS shape (firm; see
[`L1/lu_solve`](../L1/lu_solve.md) §Signature):

    lu_solve :: (A: Matrix[k, k], b: Tensor[k])    -> Tensor[k]       -- single RHS
    lu_solve :: (A: Matrix[k, k], B: Matrix[k, m]) -> Matrix[k, m]    -- multi RHS (column-wise)

    lu_solve(A, b) = the unique x with  A · x = b   (A invertible)

`A` is a **dense, materialized, square** `k×k` matrix (the deflation block `S = λI − H`, or the
ROM matrix `Ar(ω)`); `k` is the small coordinate dimension (deflation rank or ROM basis size —
single to low tens), **not** the large field dimension `N` of
[`apply_linop`](../L1/apply_linop.md) / [`ksp_solve`](../L1/ksp_solve.md). The
**factorization kernel** is a contracted load-bearing variant axis ([`L1/lu_solve`](../L1/lu_solve.md)
§Variant axes): `full-pivot-LU` | `full-pivot-Householder-QR` | `LDLT` | … . The L1 operator is
kernel-agnostic in its *value* (`lu_solve(A, ·) = A⁻¹` in exact arithmetic, law 1) but the kernel
is carried as a contracted parameter with the stability non-law. The transient Eigen
decomposition object, the in-place RHS overwrite, and the pivot/permutation bookkeeping are
**not** in the L1 signature — they are exactly what this lowering exposes.

## L0 form (RHS)

The L1 direct solve lowers into Palace's inline-Eigen surface in two sub-patterns sharing the
same **transient-decomposition-then-back-substitute, in-place over the RHS** skeleton; the
sub-patterns differ in which factorization kernel is invoked and in the call site's structural
role (NLEPS block-elimination vs ROM online evaluation).

The common L0 skeleton, narrated forward from the L1 form:

    -- L1:  x = lu_solve(A, b)              -- pure; A, b read-only; fresh x
    -- L0:  b = A.<kernel>().solve(b);      -- A.<kernel>() builds a TRANSIENT decomposition object;
                                            -- .solve(b) back-substitutes; result OVERWRITES the RHS buffer b

The rewrite L1→L0 introduces three things the L1 signature hides: (i) the **transient
factorization object** `A.<kernel>()` (a value with internal pivot/permutation arrays, rebuilt
per call — Eigen does not cache it across calls in Palace), (ii) the **back-substitution** step
`.solve(·)`, and (iii) the **in-place RHS overwrite** — the L0 destination *is* the RHS argument
(`SS = -...solve(SS)`, `RHSr = ...solve(RHSr)`), so unlike the BLAS-1 reductions there is a real
destination buffer whose pre-call contents (the RHS) are consumed and overwritten by the
post-call contents (the solution).

### Sub-pattern A — NLEPS eigensolver deflation, full-pivot LU (`S.fullPivLu().solve(·)`)

    // palace/linalg/nleps.cpp — inside QuasiNewtonSolver::Solve() (nleps.cpp:351), deflation lambdas
    Eigen::MatrixXcd SS(k, k);                                          // :524  k×k multi-RHS matrix
      for (int i = 0; i < k; i++)
        for (int j = 0; j < k; j++)
          SS(i, j) = linalg::Dot(GetComm(), X[i], X[j]);                // :529  Gram-like block
    const Eigen::MatrixXcd S = eig_opInv * Eigen::MatrixXcd::Identity(k, k) - H;  // :532  S = λI − H
    SS = -S.fullPivLu().solve(SS);                                      // :533  MULTI-RHS solve (in place)
    x2 = SS.fullPivLu().solve(x2);                                      // :534  single-RHS solve (in place)
    const ComplexVector XSx2 = MatVecMult(X, S.fullPivLu().solve(x2));  // :535  single-RHS (nested)
    linalg::AXPY(-1.0, XSx2, x1);                                       // :536  block-elim back-substitute

The deflated NEP carries a `k×k` extended-operator block `S = λI − H` (`H` the projected
Hessenberg of the locked eigenvalues, `nleps.cpp:397`). The block-elimination of the deflated
`2×2` system repeatedly forms `S⁻¹`-applied vectors via `S.fullPivLu().solve(·)`:

1. **`A.fullPivLu()`** — a transient **full-pivot LU** decomposition object built on the dense
   `k×k` `S` (or `SS`). Full pivoting (`Eigen::FullPivLU`) searches both rows and columns for the
   pivot — the numerical-robustness choice (see §The factorization-kernel axis).
2. **`.solve(·)`** — pivoted-LU back-substitution against the RHS. The result is assigned **back
   over the RHS buffer**: `SS = -S.fullPivLu().solve(SS)` (`:533`, the destination `SS` is also
   the RHS), `x2 = SS.fullPivLu().solve(x2)` (`:534`, destination `x2` is the RHS).

Three solve **sites** in `QuasiNewtonSolver::Solve()`, one per deflation lambda:

- **Deflated-solve** (`nleps.cpp:533-535`): the multi-RHS `SS = -S.fullPivLu().solve(SS)` (`:533`,
  `k×k` RHS matrix — witnesses the multi-RHS form, [`L1/lu_solve`](../L1/lu_solve.md) law 4),
  the single-RHS `x2 = SS.fullPivLu().solve(x2)` (`:534`), and the nested
  `S.fullPivLu().solve(x2)` inside `MatVecMult` (`:535`).
- **Residual** (`nleps.cpp:562-563`): `S = lam * I − H` (`:562`, the residual-evaluation `λ`) then
  `S.fullPivLu().solve(vv2)` (`:563`, single-RHS).
- **Jacobian / low-rank-update** (`nleps.cpp:665-667`): `S = eig * I − H` (`:664`), the single-RHS
  `Sv2 = S.fullPivLu().solve(v2)` (`:665`), and the **nested** `S.fullPivLu().solve(Sv2)` (`:667`,
  i.e. `S⁻¹(S⁻¹v2)` — the compositional shape of [`L1/lu_solve`](../L1/lu_solve.md) law 5).

Element type is `Eigen::MatrixXcd` / `Eigen::VectorXcd` (complex) at every site.

Justification kind: **structural** — the rewrite is the syntactic expansion of one pure L1
direct-solve into the L0 transient-decomposition-then-back-substitute two-step; the destination
is the RHS buffer (in-place).

Citations:
- `palace/linalg/nleps.cpp:351` — `int QuasiNewtonSolver::Solve()`, the enclosing function (all
  deflation solve sites are lambdas within it).
- `palace/linalg/nleps.cpp:397` — `Eigen::MatrixXcd H;` — the `k×k` projected Hessenberg (the
  `H` in `S = λI − H`). Grounds the `k` (deflation-rank) axis.
- `palace/linalg/nleps.cpp:524` — `Eigen::MatrixXcd SS(k, k);` — the `k×k` multi-RHS matrix
  (built from `linalg::Dot(X[i], X[j])` inner products, `:526-531`). Grounds the multi-RHS form.
- `palace/linalg/nleps.cpp:532` — `const Eigen::MatrixXcd S = eig_opInv * Eigen::MatrixXcd::
  Identity(k, k) - H;` — the materialized dense square `k×k` coefficient `S = λI − H`. Grounds
  the `A: Matrix[k, k]` dense-materialized shape.
- `palace/linalg/nleps.cpp:533-535` — the deflated-solve site: `SS = -S.fullPivLu().solve(SS)`
  (`:533`, multi-RHS, in place), `x2 = SS.fullPivLu().solve(x2)` (`:534`, single-RHS, in place),
  `const ComplexVector XSx2 = MatVecMult(X, S.fullPivLu().solve(x2))` (`:535`, single-RHS). The
  full-pivot-LU kernel; single + multi RHS; the nested-solve shape.
- `palace/linalg/nleps.cpp:536` — `linalg::AXPY(-1.0, XSx2, x1);` — the block-elimination
  back-substitution that consumes the solve result (lowering context).
- `palace/linalg/nleps.cpp:562-563` — residual lambda: `const Eigen::MatrixXcd S = lam *
  Eigen::MatrixXcd::Identity(k, k) - H;` (`:562`), `const ComplexVector XSvv2 = MatVecMult(X,
  S.fullPivLu().solve(vv2));` (`:563`). Second deflation solve site, single-RHS.
- `palace/linalg/nleps.cpp:664-667` — Jacobian site: `const Eigen::MatrixXcd S = eig *
  Eigen::MatrixXcd::Identity(k, k) - H;` (`:664`), `const Eigen::VectorXcd Sv2 = S.fullPivLu()
  .solve(v2);` (`:665`), `const ComplexVector XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2));`
  (`:667`, nested `S⁻¹(S⁻¹v2)`). Third deflation solve site.

### Sub-pattern B — ROM PROM online evaluation, full-pivot Householder QR (`Ar.fullPivHouseholderQr().solve(·)`)

    // palace/models/romoperator.cpp — RomOperator::SolvePROM (romoperator.cpp:701)
    Ar.resize(V.size(), V.size());                  // :717   Ar is m×m, m = V.size() (ROM basis size)
    RHSr.resize(V.size());                          // :718
    // ... assemble Ar(ω) = Kr + iω Cr − ω² Mr + Vᴴ A2 V  (:720-734) and RHSr(ω) (:737-748) ...
    if constexpr (false) {                          // :754   LDLT branch — DISABLED
      RHSr = Ar.ldlt().solve(RHSr);                 // :757   (rejected: faster, less stable)
      RHSr = Ar.selfadjointView<Eigen::Lower>().ldlt().solve(RHSr);  // :758
    } else {
      // QR solve, for maximal stability. ... numerically poorly conditioned ... Re and Im
      // into separate columns.                     // :762-764  the stability comment
      RHSr = Ar.fullPivHouseholderQr().solve(RHSr); // :765   ACTIVE: full-pivot Householder QR, in place
    }

The projected reduced-order matrix `Ar(ω)` is `m×m` (`m = V.size()`, the ROM basis size,
`romoperator.hpp:188`); the PROM solution at a frequency is `RHSr ← Ar(ω)⁻¹ RHSr(ω)`:

1. **`Ar.fullPivHouseholderQr()`** — a transient **full-pivot Householder QR** decomposition
   object built on the dense `m×m` `Ar`. Chosen "for maximal stability" (`romoperator.cpp:762-764`).
2. **`.solve(RHSr)`** — back-substitution against `RHSr`, the result assigned **back over
   `RHSr`** (`:765`, in place — the destination *is* the RHS).

The **disabled LDLT alternative** (`romoperator.cpp:757-758`, under `if constexpr (false)`,
`:754`) is a faster-but-less-stable kernel the authors rejected for the ROM matrix. Its presence
is the L0 witness that the kernel choice is **load-bearing** (a deliberate stability decision,
not a free swap) — see §The factorization-kernel axis. Element type is `Eigen::MatrixXcd` /
`Eigen::VectorXcd` (complex).

Justification kind: **structural** — same transient-decomposition-then-back-substitute expansion
as Sub-pattern A, with the full-pivot-Householder-QR kernel and a single-RHS `RHSr`; the
destination is the RHS buffer (in-place). The kernel difference is the load-bearing-numerical
residue (next section), not a structural difference in the rewrite.

Citations:
- `palace/models/romoperator.cpp:701` — `void RomOperator::SolvePROM(int excitation_idx, double
  omega, ComplexVector &u)` — the function that assembles and solves the small dense PROM system.
- `palace/models/romoperator.cpp:717` — `Ar.resize(V.size(), V.size());` — `Ar` sized `m×m` with
  `m = V.size()` (ROM basis size). Grounds the `m`-axis instance of the square-`k` shape.
- `palace/models/romoperator.cpp:720-734` — the assembly `Ar(ω) = Kr + iω Cr − ω² Mr + Vᴴ A2 V`:
  the `Vᴴ A2 V` term via `ProjectMatInternal` (`:723`, inside the `has_A2` block opening `:720`),
  then the scalar terms
  `Ar += Kr` (`:729`), `Ar += (1i*omega)*Cr` (`:732`), `Ar += (-omega*omega)*Mr` (`:734`). The
  materialization of the dense complex `Ar` coefficient (lowering context for the `A` argument).
- `palace/models/romoperator.cpp:754` — `if constexpr (false)` — gates the LDLT branch off; the
  QR branch (`else`) is active.
- `palace/models/romoperator.cpp:757-758` — `RHSr = Ar.ldlt().solve(RHSr);` and `RHSr =
  Ar.selfadjointView<Eigen::Lower>().ldlt().solve(RHSr);` — the **disabled** LDLT alternative
  (rejected faster-but-less-stable kernel). Grounds the kernel choice as load-bearing.
- `palace/models/romoperator.cpp:762-764` — the source comment: "QR solve, for maximal
  stability. The small system is cheap to compute but can be numerically poorly conditioned to
  due the splitting of HDM solutions into Re and Im into separate columns." Direct witness that
  the full-pivot-QR kernel is chosen for a **stated numerical-robustness property**.
- `palace/models/romoperator.cpp:765` — `RHSr = Ar.fullPivHouseholderQr().solve(RHSr);` — the
  **active** ROM PROM online solve, full-pivot Householder QR, in place. The second
  factorization-kernel witness (QR, not LU).
- `palace/models/romoperator.hpp:188-189` — `Eigen::MatrixXcd Ar;` / `Eigen::VectorXcd RHSr;` —
  the dense complex PROM matrix and RHS member declarations. Grounds the dense-materialized,
  complex element-type shape contract.

## The factorization-kernel axis

**Kind:** load-bearing-numerical recording

This is the core load-bearing content of the theme. The factorization *kernel* differs across
the two sub-patterns — **full-pivot LU** at NLEPS (`nleps.cpp:533`), **full-pivot Householder
QR** at ROM (`romoperator.cpp:765`), with a **rejected LDLT** at ROM (`:757-758`) — but the
*operation* is identical: solve `A x = b` for a small dense `A` by a numerically-robust direct
factorization. Per the CLAUDE.md taxonomy (`Optimization tricks vs. base algebra`) the kernel is
a **load-bearing numerical trick**, not a transparent performance trick: the *value* `x = A⁻¹b`
is kernel-independent (exact arithmetic, [`L1/lu_solve`](../L1/lu_solve.md) law 1), but the
*floating-point* result and its **conditioning behaviour** on an ill-conditioned small `A` are
kernel-dependent, and the choice is a deliberate, source-documented stability decision.

The property each kernel buys:

| kernel | L0 site | property bought | role |
|---|---|---|---|
| full-pivot LU (`fullPivLu`) | `nleps.cpp:533-535,563,665,667` | general nonsingular solve; full row+column pivoting for rank-revealing robustness | active (NLEPS deflation) |
| full-pivot Householder QR (`fullPivHouseholderQr`) | `romoperator.cpp:765` | maximal stability on a possibly-ill-conditioned matrix (orthogonal factorization; the Re/Im column-splitting of HDM solutions can be poorly conditioned) | active (ROM online) |
| LDLT (`ldlt` / `selfadjointView<Lower>().ldlt`) | `romoperator.cpp:757-758` | SPD/Hermitian-indefinite fast factorization; **rejected** as less stable than QR for the ROM matrix | disabled (`if constexpr (false)`) |

The ROM comment is the decisive witness: "QR solve, **for maximal stability**. The small system
is cheap to compute but can be numerically poorly conditioned … splitting of HDM solutions into
Re and Im into separate columns" (`romoperator.cpp:762-764`). The cost is cheap (small `m`), so
the authors trade nothing of consequence for the QR robustness — and they keep the faster LDLT
**in the source but disabled**, which is exactly the marker of a load-bearing-numerical decision
(a deliberately-not-taken faster path). The lowering therefore **must record which kernel a given
L0 call uses** to reproduce that call's floating-point/conditioning behaviour; the kernel is not
a free choice the rewrite may swap. This mirrors the reduction-tree non-associativity recording
in [`dot-mutation-rotation`](./dot-mutation-rotation.md) §"Reduction tree" — same
load-bearing-numerical discipline, different residue (kernel conditioning here, summation order
there).

The **kernel-conditioning non-law** ([`L1/lu_solve`](../L1/lu_solve.md) §Algebraic laws, the
first "do not hold" bullet): `lu_solve` with the `fullPivLu` kernel and with the
`fullPivHouseholderQr` kernel are algebraically identical (both return `A⁻¹b` in exact
arithmetic) but differ at the bit level and in conditioning behaviour. The lowering carries the
kernel as a contracted parameter, not an absorbed detail.

## The in-place RHS overwrite

*The mutation the rotation undoes.*

Unlike the BLAS-1 reduction themes ([`dot`](./dot-mutation-rotation.md),
[`nrm2`](./nrm2-mutation-rotation.md)) whose L0 result is a returned scalar (no destination
buffer, so the "mutation rotation" is a no-op on the buffer side), `lu_solve`'s L0 form **does
have a destination buffer**: the RHS argument is overwritten by the solution. The witnessed
in-place assignments:

- `SS = -S.fullPivLu().solve(SS)` (`nleps.cpp:533`) — destination `SS` is also the RHS matrix.
- `x2 = SS.fullPivLu().solve(x2)` (`nleps.cpp:534`) — destination `x2` is the RHS vector.
- `RHSr = Ar.fullPivHouseholderQr().solve(RHSr)` (`romoperator.cpp:765`) — destination `RHSr` is
  the RHS vector.

The L1 `x = lu_solve(A, b)` form binds a **fresh** `x` (the RHS `b` is read-only). The rotation
L1→L0 (a) **introduces** the destination = RHS aliasing (the solution overwrites the RHS buffer,
a workspace-reuse trick: the RHS is dead after the solve, so its buffer is reused for the result)
and (b) **introduces** the transient factorization object whose pivot/permutation arrays are
internal Eigen state. The destination-is-RHS aliasing is a **transparent performance trick**
(the value is identical whether the solution lands in a fresh buffer or overwrites the dead RHS);
the kernel choice is the load-bearing residue. Note the sites that do **not** overwrite the RHS —
`const ComplexVector XSx2 = MatVecMult(X, S.fullPivLu().solve(x2))` (`nleps.cpp:535`),
`const Eigen::VectorXcd Sv2 = S.fullPivLu().solve(v2)` (`nleps.cpp:665`) — bind a fresh
destination, structurally identical to the pure L1 form; these confirm the in-place overwrite is
an optional buffer-reuse trick, not intrinsic to the operation.

## Applicability conditions

The rewrite preserves semantics when:

1. **`A` square and (for the contracted semantics) invertible.** `A: Matrix[k, k]`; at every
   Palace site `A` is a deflation block `S = λI − H` (`nleps.cpp:532,562,664`) or the ROM matrix
   `Ar(ω)` (`romoperator.cpp:720-734`), expected invertible at the evaluation point. The
   full-pivot kernels return a particular/least-squares answer for rank-deficient `A`, but that
   is kernel-specific and outside the contracted L1 semantics ([`L1/lu_solve`](../L1/lu_solve.md)
   §Algebraic laws, the "definedness without invertibility" non-law).
2. **`A` is a dense materialized value, not an opaque operator.** The factorization examines and
   permutes `A`'s entries — `A` must be a dense `Eigen::MatrixXcd`, not the opaque
   `LinearOperator[N, N]` of [`apply_linop`](./apply-linop-mutation-rotation.md). This is the
   structural distinction from `ksp_solve`/`apply_linop` (which never read the operator's
   entries). The denseness is what makes a *direct* factorization the right kernel.
3. **The factorization kernel matches the call site's numerical intent.** The kernel is a
   load-bearing numerical choice (NLEPS full-pivot LU, ROM full-pivot QR for stability) — the
   lowering must record which kernel a given L0 call uses to reproduce its conditioning behaviour.
   Not a free swap (§The factorization-kernel axis).
4. **In-place RHS overwrite is permitted only when the RHS is dead after the solve.** The
   destination-is-RHS aliasing (`SS = -S.fullPivLu().solve(SS)`, `RHSr = ...solve(RHSr)`) is a
   transparent buffer-reuse trick valid because the RHS is not read again. A lowering that needs
   the original RHS preserved emits the fresh-destination form (`Sv2 = S.fullPivLu().solve(v2)`,
   `nleps.cpp:665`).
5. **Multi-RHS = column-wise single-RHS over one factorization.** The `k×k` RHS-matrix solve
   `SS = -S.fullPivLu().solve(SS)` (`nleps.cpp:533`) and the single-RHS `x2 = SS.fullPivLu()
   .solve(x2)` (`:534`) are the same operator at two RHS shapes
   ([`L1/lu_solve`](../L1/lu_solve.md) law 4). The factor-once/solve-many structure is a
   transparent performance trick (the source re-factorizes per call, but the value is identical).

## Justification kind

- **Sub-pattern A** (NLEPS, full-pivot LU) — `structural`. Expand one pure L1 direct-solve into
  the L0 transient-`fullPivLu()`-decomposition + `.solve()` back-substitution, in place over the
  RHS; covers single- and multi-RHS and the nested-solve shape.
- **Sub-pattern B** (ROM, full-pivot Householder QR) — `structural`. Same expansion with the
  full-pivot-Householder-QR kernel, single-RHS, in place over `RHSr`; the disabled-LDLT branch is
  the load-bearing-kernel witness.

The theme as a whole is `structural` — the rewrite is the syntactic expansion of the L1 direct
solve into the L0 transient-decomposition-then-back-substitute composition. The one
non-syntactic ingredient is the **factorization-kernel load-bearing-numerical recording** (which
kernel a given call uses, and the conditioning property it buys), read straight off the verified
solve-call sites and the ROM stability comment (`romoperator.cpp:762-764`); it does not change
the structural character of the lowering but must be carried, not absorbed. The
destination-is-RHS aliasing and the factor-once/solve-many batching are transparent performance
tricks nested inside the sub-patterns.

## Speculative L1 operators

**None.** This theme lowers the already-firm L1 [`lu_solve`](../L1/lu_solve.md) operator; it
proposes no new L1 vocabulary. The factorization kernel is a contracted variant axis of the
existing `lu_solve` operator (not a new operator). The L2 NEP-deflation vocabulary that composes
`lu_solve` — the [`deflate`](../L2/deflate.md) / [`gram`](../L2/gram.md) combinators (rough-in) —
is named here only to mark the upward fan-out boundary; it is **not** part of this theme.

## Variant axes

`lu_solve` has the following variant axes at the L1>L0 edge (per `classify-variant-axis`); one is
load-bearing, the rest absorbed (mirrors [`L1/lu_solve`](../L1/lu_solve.md) §Variant axes):

- **factorization kernel** (load-bearing): `full-pivot-LU` (`nleps.cpp:533`) |
  `full-pivot-Householder-QR` (`romoperator.cpp:765`) | `LDLT` (rejected, `romoperator.cpp:757-758`)
  | … . At L0 these are distinct Eigen decomposition method chains; the choice is a stated
  numerical-robustness decision (§The factorization-kernel axis), not a free swap. The L1
  operator is kernel-agnostic in value, kernel-dependent in conditioning.
- **single-RHS vs multi-RHS** (absorbed-as-form): `b: Tensor[k]` | `B: Matrix[k, m]`. Both
  witnessed at NLEPS (`SS` multi-RHS `:533`, `x2`/`v2` single-RHS `:534`/`:665`); same operator,
  two RHS shapes (law 4). Factor-once/solve-many is a transparent performance trick.
- **in-place RHS overwrite vs fresh destination** (absorbed; transparent performance trick):
  `SS = -...solve(SS)` / `RHSr = ...solve(RHSr)` (in place, `:533`/`:765`) vs `Sv2 = ...solve(v2)`
  / `XSx2 = MatVecMult(X, ...solve(x2))` (fresh, `:665`/`:535`). Value-identical; the in-place
  form reuses the dead RHS buffer.
- **element type** (absorbed): `complex` (every Palace site — `Eigen::MatrixXcd` / `VectorXcd`) |
  `real` (permitted-but-unwitnessed). The factorization is element-type-agnostic.

## Status

`firm` — the structural expansion of the L1 `lu_solve` direct solve into the L0 form.

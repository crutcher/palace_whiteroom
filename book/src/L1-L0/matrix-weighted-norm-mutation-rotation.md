# matrix-weighted-norm-mutation-rotation

The mutation rotation for the operator-weighted (energy) norm. Lowers the pure L1 form
`matrix_weighted_norm(x, B) = √(xᴴ B x)` ([`L1/matrix_weighted_norm`](../L1/matrix_weighted_norm.md),
firm) into Palace's L0 `linalg::Norml2(comm, x, B, Bx)` three-step composition
`B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(dot)` (`palace/linalg/operator.cpp:599-619`). It is the
**weighted relative** of [`nrm2-mutation-rotation`](./nrm2-mutation-rotation.md): where `nrm2`
lowers `√⟨x, x⟩` to `std::sqrt(std::abs(Dot(comm, x, x)))`, this theme lowers `√(xᴴ B x)` to the
same shape with the weight `B` introduced by a leading operator-apply into a caller-supplied
workspace `Bx`. The theme **reuses two sibling sub-themes** rather than restating them: the leading
`B.Mult(x, Bx)` is [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md) Sub-pattern
A; the inner `Dot(comm, Bx, x)` is [`dot-mutation-rotation`](./dot-mutation-rotation.md) Sub-pattern
A (the `Mpi::GlobalSum ∘ LocalDot` two-step). What this theme adds is the matrix-weighted machinery:
the **caller-owned destination workspace `Bx`** (overwritten with `B·x`, not just scratch — its
ownership/lifetime/reuse vanish at L1), the **complex element-type real/imaginary `B.Mult` split**,
the outer `std::sqrt`, and the **`MFEM_ASSERT(dot > 0.0)` SPD run-time guard** (classified below).

## Slug

`matrix-weighted-norm-mutation-rotation`

## L1 form (LHS)

The pure-functional energy norm consumes a read-only vector and a read-only SPD operator and
produces a fresh non-negative real scalar; nothing is mutated, and there is no workspace in the
signature. The LHS shape (firm; see [`L1/matrix_weighted_norm`](../L1/matrix_weighted_norm.md)):

    alpha = matrix_weighted_norm(x, B)     -- alpha = √(xᴴ B x), always real, non-negative
                                           -- (real x:    √(xᵀ B x) = √Σ x[i]·(B·x)[i])
                                           -- (complex x: √(xᴴ B x) = √Σ conj(x[i])·(B·x)[i])

The defining identity (L1 algebraic law 8) is `matrix_weighted_norm(x, B)² = xᴴ B x`, which
unfolds into the L1 composition `√(dot(apply_linop(B, x), x))` — two firm L1 primitives
([`L1/apply_linop`](../L1/apply_linop.md), [`L1/dot`](../L1/dot.md)) plus the outer square root.
The element-type axis is collapsed at L1: a single operator
`matrix_weighted_norm :: (Tensor[N], LinearOperator[N, N]) -> Scalar(real)` regardless of whether
`x` is real or complex (`xᴴ B x` is real and non-negative for SPD `B` — L1 laws 1, 8). The MPI
collective is **not** in the L1 signature; the L1 reduction is a single semantic step. The
workspace `Bx` is **not** in the L1 signature; the operator returns a fresh scalar with no
destination buffer.

The SPD precondition on `B` is an explicit L1 **applicability condition** (the L1 form is a norm
iff `B` is SPD; a seminorm if SPSD; ill-defined if indefinite), not a soft guard — see
[`L1/matrix_weighted_norm`](../L1/matrix_weighted_norm.md) §Applicability conditions.

## L0 form (RHS)

The L1 energy norm lowers into the free-function template `linalg::Norml2(comm, x, B, Bx)`
(`palace/linalg/operator.hpp:374`), specialized at `palace/linalg/operator.cpp` for `Vector` (real) and `ComplexVector`
(complex). The body is **the same three-step composition** in both specializations; they differ
only in the element-type plumbing of the leading operator-apply and the form of the SPD guard.

### Sub-pattern A — real specialization (the canonical form)

    template <>
    double Norml2(MPI_Comm comm, const Vector &x, const Operator &B, Vector &Bx)
    {
      B.Mult(x, Bx);                                          // palace/linalg/operator.cpp:602  — step 1
      double dot = Dot(comm, Bx, x);                          // palace/linalg/operator.cpp:603  — step 2
      MFEM_ASSERT(dot > 0.0, "Non-positive vector norm ...");  // palace/linalg/operator.cpp:604-605 — guard
      return std::sqrt(dot);                                  // palace/linalg/operator.cpp:606  — step 3
    }

The three steps the L1 closed form hides, evaluated in order:

1. **`B.Mult(x, Bx)`** — the leading operator-apply. `Bx` (a caller-supplied buffer) is
   **overwritten** with `B·x`; it is a *destination* buffer, not transient scratch. This is exactly
   [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md) **Sub-pattern A** (bare
   forward apply `A.Mult(x, y)`): the L1 value `apply_linop(B, x)` binds to the L0 destination `Bx`,
   `B` becomes the method receiver, `x` the first argument. This theme **inherits** that
   sub-theme — the operator-representation variant axis of `B` (sparse / matrix-free / composition /
   multigrid) is collapsed at L1 per `apply_linop`'s precedent and is not re-handled here.
2. **`Dot(comm, Bx, x)`** — the inner Hermitian inner product `xᴴ (B·x)`. This is
   [`dot-mutation-rotation`](./dot-mutation-rotation.md) **Sub-pattern A** (free-function
   `linalg::Dot(comm, a, b)` = the `Mpi::GlobalSum ∘ LocalDot` two-step). This theme **inherits**
   that sub-theme — the local-then-collective two-step, the MPI collective (single-rank no-op,
   structurally present per CLAUDE.md "Scope"), and the reduction-tree non-associativity are all
   recorded there, not restated. **Conjugation handedness:** Palace's `linalg::Dot(comm, Bx, x)`
   computes `xᴴ (Bx)` (arg-2 conjugated — `dot-mutation-rotation` §"The conjugation asymmetry"),
   which is exactly the L1 `xᴴ B x` with `x` as the conjugated argument; for SPD `B` the value is
   real, so the arg-order is re-order-invisible (the `std::sqrt` below takes a real projection —
   same re-order-invisible case as `nrm2`).
3. **`std::sqrt(dot)`** — the principal (non-negative) real square root. A deterministic,
   correctly-rounded IEEE-754 scalar primitive below the L1 layer's resolution; it contributes no
   non-determinism (which is entirely the compound reduction non-associativity inherited from
   `apply_linop`'s kernel and `Dot`'s reduction).

The `MFEM_ASSERT(dot > 0.0, ...)` (`palace/linalg/operator.cpp:604-605`) is the **SPD run-time guard** —
classified below. There is **no destination buffer for the result**: the L1 scalar lowers to a
return register / stack `double`. The mutation rotation on the *output* side is a no-op (as for
`dot` / `nrm2`); the only buffer mutation is the workspace `Bx` overwrite (step 1), which is the
inherited `apply_linop` rotation.

Justification kind: **structural** — the syntactic expansion of one closed-form L1 step into the
L0 three-step; the destination for the result is the return register, the destination for the
intermediate `B·x` is the caller-owned `Bx`.

Citations:
- `palace/linalg/operator.cpp:599-607` — real specialization: `B.Mult(x, Bx)` (`:602`),
  `double dot = Dot(comm, Bx, x)` (`:603`), `MFEM_ASSERT(dot > 0.0, ...)` (`:604-605`),
  `return std::sqrt(dot)` (`:606`).
- `palace/linalg/operator.hpp:372-374` — `Norml2(comm, x, B, Bx)` template decl with comment
  `// Calculate the vector norm with respect to an SPD matrix B.` (`:372`). The SPD precondition
  stated at L0.
- [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md) Sub-pattern A — the
  inherited `B.Mult(x, Bx)` lowering (operator-apply into a destination buffer).
- [`dot-mutation-rotation`](./dot-mutation-rotation.md) Sub-pattern A — the inherited
  `Dot(comm, Bx, x)` lowering (the `Mpi::GlobalSum ∘ LocalDot` two-step + the arg-2-conjugated
  convention).

### Sub-pattern B — complex specialization (real-operator-on-complex-vector split)

    template <>
    double Norml2(MPI_Comm comm, const ComplexVector &x, const Operator &B, ComplexVector &Bx)
    {
      // For SPD B, xᴴ B x is real.                          // palace/linalg/operator.cpp:612
      B.Mult(x.Real(), Bx.Real());                           // palace/linalg/operator.cpp:613  — step 1a
      B.Mult(x.Imag(), Bx.Imag());                           // palace/linalg/operator.cpp:614  — step 1b
      std::complex<double> dot = Dot(comm, Bx, x);           // palace/linalg/operator.cpp:615  — step 2
      MFEM_ASSERT(dot.real() > 0.0 &&                        // palace/linalg/operator.cpp:616-617 — guard
                  std::abs(dot.imag()) < 1.0e-9 * dot.real(), "...");
      return std::sqrt(dot.real());                          // palace/linalg/operator.cpp:618  — step 3
    }

Structurally identical to Sub-pattern A, with two element-type differences:

- **Step 1 splits into two real applies** (`:613-614`). The L0 `B : Operator` is **real-valued by
  signature** even though `x` is a `ComplexVector`; Palace applies the real `B` componentwise to
  the real and imaginary lanes of `x`, writing into the real and imaginary lanes of `Bx`. This is
  still [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md) Sub-pattern A applied
  twice (once per lane) — equivalently the `ComplexWrapperOperator` lift of a real `B` to a complex
  apply (`apply_linop` §Applicability condition 3, the `complex-from-real-lift`). At L1 this split
  is absorbed by `apply_linop`'s element-type variant axis: the L1 form is just
  `apply_linop(B, x)`. **(Variant-axis note: this real-`B`-on-complex-`x` case is the
  promotion-gate question flagged at [`L1/matrix_weighted_norm`](../L1/matrix_weighted_norm.md)
  §Variant axes — whether L1 admits it as a distinct variant or a uniform rule. This theme records
  it faithfully as the L0 surface; the L1-side resolution is upstream.)**
- **The guard is two-part** (`:616-617`): `dot.real() > 0.0` (the SPD positivity, as in the real
  branch) **and** `std::abs(dot.imag()) < 1.0e-9 * dot.real()` (a **numerical Hermiticity witness**
  — for SPD `B` the form `xᴴ B x` is real, so the imaginary part of the computed `dot` must be
  round-off only). The return is `std::sqrt(dot.real())` (`:618`) — the imaginary part is
  **discarded**, not folded, because the assertion has confirmed it is round-off. This confirms the
  L1 "result is always real" rule is a direct algebraic consequence of `B` being SPD
  ([`L1/matrix_weighted_norm`](../L1/matrix_weighted_norm.md) §Signature).

At L1 Sub-patterns A and B **collapse to one operator** (element-type variant axis absorbed): the
result is real-valued regardless of input element type, and all L1 laws hold uniformly.

Justification kind: **structural** (the three-step expansion) + the value-level algebraic identity
`xᴴ B x ∈ ℝ` for SPD `B` (reconciling the complex-arithmetic `dot` with the real return). The
identity is read straight off the L0 source's own `// For SPD B, xᴴ B x is real.` comment (`:612`)
and the assertion (`:616-617`) — positively anchored, not reconstructed.

Citations:
- `palace/linalg/operator.cpp:609-619` — complex specialization: `// For SPD B, xᴴ B x is real.`
  (`:612`), `B.Mult(x.Real(), Bx.Real())` / `B.Mult(x.Imag(), Bx.Imag())` (`:613-614`),
  `std::complex<double> dot = Dot(comm, Bx, x)` (`:615`), the two-part `MFEM_ASSERT` (`:616-617`),
  `return std::sqrt(dot.real())` (`:618`).

### Sub-pattern C — the `Normalize` consumer (in-place scale by the inverse norm)

    inline double Normalize(MPI_Comm comm, VecType &x, const Operator &B, VecType &Bx)
    {
      double norm = Norml2(comm, x, B, Bx);                  // palace/linalg/operator.hpp:380
      MFEM_ASSERT(norm > 0.0, "Zero vector norm ...");        // palace/linalg/operator.hpp:381
      x *= 1.0 / norm;                                        // palace/linalg/operator.hpp:382
      return norm;
    }

The dominant *consumer* of the weighted norm: `linalg::Normalize(comm, x, B, Bx)`
(`palace/linalg/operator.hpp:377-384`) calls `Norml2` (Sub-pattern A/B), asserts the result positive, then scales
`x` in place by `1/norm`. At L1 this is the composition `scal(1/matrix_weighted_norm(x, B), x)` —
the `x *= 1.0/norm` step is [`scal-mutation-rotation`](./scal-mutation-rotation.md) (inherited, not
restated). It is recorded here as a surface form because it is the M-orthonormalisation primitive
that consumes `Norml2` at every eigensolver backend (the `xscale.get()[i] = 1.0 /
GetEigenvectorNorm(...)` cohort below is the open-coded form of the same compose). The
`MFEM_ASSERT(norm > 0.0)` here is redundant with `Norml2`'s internal `dot > 0.0` guard but documents
the divisor-positivity contract at the call boundary.

Justification kind: **structural** — pure delegation to A/B plus an inherited `scal` step.

Citations:
- `palace/linalg/operator.hpp:377-384` — `Normalize` inline definition: `norm = Norml2(...)`
  (`:380`), `MFEM_ASSERT(norm > 0.0, ...)` (`:381`), `x *= 1.0 / norm` (`:382`).

## The caller-owned workspace `Bx`

**Kind:** the matrix-weighted machinery

The distinguishing feature of this theme over `nrm2-mutation-rotation` is the **workspace `Bx`**.
Unlike `nrm2` / `dot` (no buffer at all — the result is a stack scalar), the weighted norm needs a
materialized `B·x` to feed the inner `Dot`. At L0 this is a **caller-supplied** parameter
`VecType &Bx`, and it is a **destination** buffer (step 1 overwrites it entirely), not transient
scratch:

- **It is caller-owned, not internally allocated.** Contrast the sibling bilinear_form
  `linalg::Dot(comm, x, A, y)` (`palace/linalg/operator.hpp:386-389`, `palace/linalg/operator.cpp:621-639`), which allocates
  its workspace `Ax` internally (`ComplexVector Ax(A.Height())`). `Norml2` instead requires the
  caller to pass `Bx` so it can be **reused across calls** without per-call allocation — the live
  witness is the eigensolver M-orthonormalisation loop, where a single `Bx` (named `y1` at the
  callsite) is reused across every eigenvector (`arpack.cpp:470`, `slepc.cpp:505`, `nleps.cpp:146`:
  `xscale.get()[i] = 1.0 / GetEigenvectorNorm(x1, y1)` inside a `for` loop over `num_eig`). The
  reuse is a transparent performance trick (allocation hoisting); it is algebraically invisible.
- **It disappears at L1.** The L1 operator consumes `x` and `B`, produces a fresh scalar, and names
  no workspace. The `Bx`-as-destination-buffer, its lifetime (caller-scoped, outliving the call),
  and its cross-call reuse are **the L1>L0 lowering's concern** — exactly the
  `mention-and-erase` workspace pattern this layer's index calls out. The lowering must re-introduce
  a `B.Height()`-sized buffer for `B·x`, write it via the inherited `apply_linop` Sub-pattern A
  rotation, and (optionally) hoist its allocation outside any enclosing loop to match Palace's
  reuse.
- **Shape/lifetime contract.** `Bx` is sized `B.Height()` and aliases neither `x` nor the result;
  step 1 writes it, step 2 reads it (and `x`). The square-operator precondition
  (`B.Height() == B.Width() == N`) is enforced implicitly: `Bx` (length `B.Height()`) is dotted
  against `x` (length `N`), so the `Dot` aligned-pass precondition `MFEM_ASSERT(Bx.Size()==x.Size())`
  (inherited from `dot-mutation-rotation` applicability condition 2) forces `B.Height() == N`.

This is the workspace-ownership boundary the stub's "Implied by" provenance named (the three
in-file references in [`L1/matrix_weighted_norm`](../L1/matrix_weighted_norm.md) deferring the
`Bx`-ownership unfold to this theme). It is **resolved**: `Bx` is a caller-owned destination buffer,
materialized in the lowering, erased at L1.

## The `MFEM_ASSERT(dot > 0.0)` SPD guard

**Kind:** classification

Resolves the stub's deferred "the L0 `MFEM_ASSERT`" classification. The guard
`MFEM_ASSERT(dot > 0.0, ...)` (`palace/linalg/operator.cpp:604-605` real; `:616-617` complex) is a **load-bearing
defensive guard**, mirroring (but stronger than) the `std::abs` guard classified in
[`nrm2-mutation-rotation`](./nrm2-mutation-rotation.md) §"The `std::abs` defensive guard". Applying
the CLAUDE.md "Optimization tricks vs. base algebra" framing:

- **In exact arithmetic it is a no-op** for SPD `B` and `x ≠ 0`: `xᴴ B x > 0` strictly (SPD), so
  the assertion never fires. This is why it **disappears at L1** — the algebraic claim "`xᴴ B x > 0`
  for SPD `B`, `x ≠ 0`" (L1 laws 1, 2, 8) subsumes it.
- **In floating point it is load-bearing-defensive**: it guards against a round-off sign-flip on a
  numerically-tiny `xᴴ B x` (which would make `std::sqrt` return `NaN`), and — on a *non-SPD* `B` —
  it is the **run-time witness that the SPD applicability condition has been violated** (the
  assertion fires for an indefinite `B` applied to a vector in its negative cone). It is therefore
  **stronger than `nrm2`'s `std::abs`**: `nrm2` *silently repairs* a tiny-negative self-dot
  (`abs` strips the sign), whereas `Norml2` *aborts* on a non-positive weighted dot — because for
  the weighted form a non-positive value signals a violated SPD precondition, not mere round-off,
  and silent repair would mask an algorithm error.
- **Complex branch — the second clause is a Hermiticity witness** (`:616-617`):
  `std::abs(dot.imag()) < 1.0e-9 * dot.real()` asserts the imaginary part is round-off relative to
  the real part — a numerical (not structural) check that `B` is acting Hermitian-ly. The L0 source
  does **not** verify `B = Bᴴ` directly; this assertion is the proxy. The return discards
  `dot.imag()`.

**Verdict: load-bearing numerical (defensive guard + SPD-violation detector).** It does not change
any result in exact arithmetic, but it is **not erasable** without (a) introducing a `NaN` failure
mode and (b) losing the SPD-precondition run-time witness. Distinct from a transparent performance
trick; consistent with the `nrm2` abs-guard classification and the
[`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md)
"Defensive non-negativity guard" worked example, with the additional SPD-detector role noted.

## Reduction tree

**Kind:** load-bearing-numerical recording

The weighted norm accumulates non-associativity from **two** inherited sources (per
[`L1/matrix_weighted_norm`](../L1/matrix_weighted_norm.md) §Semantics):

1. **`apply_linop(B, x)`'s internal kernel** — a sparse-matrix realisation of `B` and a
   matrix-free realisation of the *same* SPD operator produce bit-different `B·x` (the
   `apply-linop-mutation-rotation` representation axis). Pinned per the concrete `B` subclass.
2. **The inner `Dot(comm, Bx, x)` reduction** — the `dot-mutation-rotation` reduction-tree non-law
   (Hypre per-rank kernel + MPI tree-reduce). Pinned per the `dot` lowering.

The outer `std::sqrt` is deterministic IEEE-754 and contributes none. Bit-identical reproduction of
a specific Palace `Norml2` call requires matching **both** the `B`-representation kernel tree and
the `Dot` reduction tree — not merely the value. (Same discipline as
[`dot-mutation-rotation`](./dot-mutation-rotation.md) §"Reduction tree" and
[`nrm2-mutation-rotation`](./nrm2-mutation-rotation.md), with the extra `apply_linop` layer.)

## Applicability conditions

The rewrite preserves semantics when:

1. **Read-only `x` and `B`.** `Norml2` never writes `x` or mutates `B` (the `B.Mult` virtual is
   `const`); the only buffer mutation is the workspace `Bx` overwrite (the inherited `apply_linop`
   rotation). The result is a returned scalar (no result buffer).
2. **`B` square, SPD (or SPSD with seminorm caveat).** The L0 source enforces positivity at run
   time via `MFEM_ASSERT(dot > 0.0)` (strict — SPD, treating SPSD-zero as an error). The L1 form
   encodes SPD as an applicability condition. Squareness is implicit via the workspace shape
   (`Bx` sized `B.Height()`, dotted against `x` of length `N` ⇒ `B.Height() == N`). For an
   indefinite `B` the rewrite is invalid (the assertion fires; `√(negative)` is undefined).
3. **`B` Hermitian (self-adjoint)** for `xᴴ B x` to be real. Not structurally checked at L0; the
   complex branch's `std::abs(dot.imag()) < 1e-9·dot.real()` assertion is the numerical proxy
   (Sub-pattern B).
4. **Caller-supplied `Bx` of length `B.Height()`, aliasing neither `x` nor the result.** Step 1
   overwrites `Bx` entirely; step 2 reads `Bx` and `x`. Allocation may be hoisted/reused across
   calls (transparent performance trick) — the eigensolver M-orthonormalisation loop does exactly
   this.
5. **Single-rank reading of the collective.** The `MPI_Allreduce` inside the inner `Dot` is a local
   no-op under the in-scope single-machine target (CLAUDE.md "Scope"); structurally present,
   carrying the bit-determinism caveat. Inherited from `dot-mutation-rotation` applicability
   condition 4.
6. **Conjugate-pair re-order is invisible here.** The inner `Dot(comm, Bx, x)` computes
   `xᴴ (B·x)` (arg-2 conjugated); the result is consumed by `std::sqrt` as a **real projection**
   (real branch: a `double`; complex branch: `dot.real()`), so the `xᴴ y = conj(yᴴ x)` re-order is
   invisible (same re-order-invisible case as `nrm2`). No operand-swap is needed.

## Justification kind

- **Sub-pattern A** — `structural`. The three-step expansion `B.Mult → Dot → sqrt`; result to the
  return register, `B·x` to the caller-owned `Bx`.
- **Sub-pattern B** — `structural` + the value-level identity `xᴴ B x ∈ ℝ` for SPD `B` (read off
  the L0 comment + assertion; positively anchored). The real/imaginary `B.Mult` split is the
  `complex-from-real-lift` of the inherited `apply_linop` Sub-pattern A.
- **Sub-pattern C** — `structural`. Pure delegation to A/B plus an inherited `scal` step.

The theme as a whole is `structural`, resting on one algebraic identity (L1 law 8,
`matrix_weighted_norm(x, B)² = xᴴ B x`), two inherited sub-themes (`apply_linop` Sub-pattern A,
`dot` Sub-pattern A), one inherited consumer step (`scal`), and one load-bearing-trick
classification (the SPD `MFEM_ASSERT` guard). The one non-syntactic ingredient — `xᴴ B x` is real
for SPD `B` — is read straight off the L0 source's own comment and assertion (no negative-anchor
reconstruction, no literature inference, no speculative operator), hence `firm` rather than
`partly-constructive`.

## Speculative L1 operators

**None.** This theme lowers the existing L1 [`matrix_weighted_norm`](../L1/matrix_weighted_norm.md)
operator (firm) into existing firm L1 vocabulary — `apply_linop` for the
`B·x` step, `dot` for the inner reduction, `scal` for the `Normalize` consumer. It proposes no new
L1 vocabulary. The sibling **bilinear_form** `linalg::Dot(comm, x, A, y) = yᴴ A x`
(`palace/linalg/operator.hpp:386-389`, `palace/linalg/operator.cpp:621-639`) shares the L0 file block and the same two L1
primitives but with the diagonal restriction lifted (`y ≠ x`) and **internally-allocated** workspace
`Ax` (Category-4 synthetic workspace) rather than caller-supplied `Bx`; it is a **different
operator** ([`L1/bilinear_form`](../L1/bilinear_form.md)) and the subject of a separate forthcoming
theme `bilinear-form-mutation-rotation`. It is named here only to mark the boundary; it is **not**
part of this theme. (The energy norm is the diagonal case `y = x` of the bilinear form, plus the
outer `√` and the SPD applicability condition.)

## Variant axes

`matrix_weighted_norm` has two orthogonal variant axes at the L1>L0 edge (per
`classify-variant-axis`), plus one degenerate collapse:

- **element-type**: `real` | `complex`. At L0 these are the two template specializations of
  `linalg::Norml2<VecType>` (Sub-patterns A and B; `VecType ∈ {Vector, ComplexVector}`,
  `palace/linalg/operator.cpp:599-619`). They differ in the leading-apply plumbing (real: one `B.Mult`; complex:
  the real/imaginary lane split `B.Mult(x.Real(), Bx.Real()); B.Mult(x.Imag(), Bx.Imag())`) and the
  guard form (real: one-part `dot > 0.0`; complex: two-part `dot.real() > 0.0 &&
  |dot.imag()| < 1e-9·dot.real()`). At L1 these **collapse to a single operator** — the result is
  real-valued regardless of input element type (SPD `B` ⇒ `xᴴ B x ∈ ℝ_{≥0}`), and all laws hold
  uniformly.
- **weight-operator-representation of `B`** (the M-weighted / B-weighted axis): the `B` argument may
  be any concrete real `Operator` subclass — a mass matrix `M` (the M-weighted norm), a curl-curl
  mass-weighted operator (the B-weighted norm), a diagonal SPD operator, a multigrid/composition
  operator, etc. At L0 this is the runtime polymorphism of `B.Mult`; at L1 it is collapsed to the
  opaque `LinearOperator[N, N]` per `apply_linop`'s representation-axis absorption. The eigensolver
  callsites pass `*opB` (the mass matrix); when `opB` is null they fall back to the **unweighted**
  `linalg::Norml2(comm, x)` (`arpack.cpp:438-442`, `slepc.cpp:475-479`, `nleps.cpp:114-118`).

Degenerate collapse (the unweighted boundary):

- **`B = I` (identity weight)**: `matrix_weighted_norm(x, I) = nrm2(x)` (L1 law 9). At L0 this is
  literally the eigensolver fallback path: `GetEigenvectorNorm` dispatches to
  `linalg::Norml2(comm, x, *opB, Bx)` when `opB` is non-null, else to the unweighted
  `linalg::Norml2(comm, x)` ([`nrm2-mutation-rotation`](./nrm2-mutation-rotation.md) Sub-pattern A).
  The two themes meet exactly at the identity weight: this theme's three-step
  `B.Mult → Dot → sqrt` with `B = I` reduces (`I·x = x`) to `nrm2`'s `sqrt∘abs∘Dot(x,x)` — the
  weighted theme's `MFEM_ASSERT(dot > 0.0)` replacing `nrm2`'s silent `std::abs` (since for the
  unweighted self-dot the positivity is automatic, while the weighted form must guard it).

No other variant axes — the reduction is unconditionally exhaustive over the length axis `N`, with
no masking or strided variants in the Palace surface. The output-arg-vs-return distinction (the
`Bx` workspace) is not a *variant axis* but the workspace-ownership boundary covered in §"The
caller-owned workspace `Bx`".

## Additional cited L0 ranges

- `palace/linalg/operator.cpp:624` — the sibling bilinear_form `Dot(comm, x, A, y)`'s
  internally-allocated workspace `ComplexVector Ax(A.Height())` (the boundary contrast with the
  caller-supplied `Bx`).
- `palace/linalg/arpack.cpp:433-444` / `palace/linalg/slepc.cpp:470-481` /
  `palace/linalg/nleps.cpp:109-120` — the three `GetEigenvectorNorm` dispatch bodies (weighted
  `Norml2(comm, x, *opB, Bx)` vs the unweighted `opB`-null fallback), the M-orthonormalisation
  callsite cohort.

## Status

`firm` — the structural expansion of the L0 `Norml2(comm, x, B, Bx)` three-step form.

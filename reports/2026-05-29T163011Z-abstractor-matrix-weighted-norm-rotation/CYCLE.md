---
agent: abstractor
invoked_at: 2026-05-29T163011Z
scope: L1>L0 theme promotion (stub→firm) — matrix-weighted-norm-mutation-rotation
status: pending
inputs:
  - book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md (the stub being promoted; "Implied by" provenance)
  - book/src/L1/matrix-weighted-norm.md (the rough-in (test-coverage-bounded) L1 operator)
  - book/src/L1-L0/dot-mutation-rotation.md (firm sibling — inherited inner-Dot sub-theme)
  - book/src/L1-L0/nrm2-mutation-rotation.md (firm sibling — sqrt-of-self-dot precedent + abs-guard classification)
  - book/src/L1-L0/apply-linop-mutation-rotation.md (rough-in sibling — inherited B.Mult sub-theme)
  - reference/palace/palace/linalg/operator.cpp:599-619 (the two Norml2(comm,x,B,Bx) specializations; self-verified via citecheck --anchor)
  - reference/palace/palace/linalg/operator.hpp:372-389 (decls: Norml2, Normalize, bilinear-form Dot boundary; self-verified)
  - reference/palace/palace/linalg/{arpack,slepc,nleps}.cpp (GetEigenvectorNorm callsite cohort; self-verified)
  - book/src/L0/linalg-operator-file.md:30-34 (the L0 file-layout chapter)
integrated_at: 2026-05-29T203000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (cycle-026 dispatch-3). L1>L0 matrix-weighted-norm-mutation-rotation STUB→FIRM (energy norm √(xᴴBx) → linalg::Norml2(comm,x,B,Bx), operator.cpp:599-619; sub-patterns A real/B complex/C Normalize consumer). L1-L0/index firm row inserted (firm-over-rough-in-L1 per eigsolve precedent) + SUMMARY (stub)-suffix dropped. L1>L0 firm themes +1. 4 OQ dispositions incl. 3 NEW carry-forwards (operator.cpp:601 brace-drift on L1 entry :58/:83; Category-4 workspace mislabel; mixed-element-type variant + paired bilinear-form audit). Zero gate hits."

# CYCLE: L1>L0 theme promotion (stub→firm) — matrix-weighted-norm-mutation-rotation

## Summary

The `matrix-weighted-norm-mutation-rotation` stub (materialized 2026-05-28) is promoted to a
**firm** L1>L0 mutation-rotation theme. The L1 energy-norm operator
`matrix_weighted_norm(x, B) = √(xᴴ B x)` lowers forward into Palace's L0
`linalg::Norml2(comm, x, B, Bx)` three-step composition `B.Mult(x, Bx); dot = Dot(comm, Bx, x);
return std::sqrt(dot)` (`palace/linalg/operator.cpp:599-619`, two element-type specializations). The theme is
**structural** (the syntactic expansion of one closed-form L1 step into the L0 three-step) and
**reuses two already-authored sibling sub-themes** rather than restating them: the leading
`B.Mult(x, Bx)` is `apply-linop-mutation-rotation` Sub-pattern A; the inner `Dot(comm, Bx, x)` is
`dot-mutation-rotation` Sub-pattern A (the `Mpi::GlobalSum ∘ LocalDot` two-step). What this theme
adds on top of the inherited pieces is exactly the matrix-weighted machinery: (i) the
**caller-supplied workspace `Bx`** — a *destination* buffer (overwritten with `B·x`), not just
scratch, whose ownership/lifetime/reuse disappears at L1; (ii) the **complex element-type
real/imaginary split** of `B.Mult` (`B` is real-by-signature even when `x` is complex); (iii) the
outer `std::sqrt`; (iv) the **`MFEM_ASSERT(dot > 0.0)` SPD run-time guard** classified as a
load-bearing defensive guard with the property it buys (domain-safety for `sqrt`, plus a numerical
Hermiticity witness on the complex branch). The rewrite carries the M-weighted / B-weighted
variant axis (the operator-representation of `B` is the variant), the element-type axis
(real | complex, collapsed at L1), and the unweighted-degenerate `B = I` collapse to `nrm2`.
All citations self-verified via `tools/citecheck/citecheck.py --anchor` against on-disk
`reference/palace/` (cycle-025 nleps.cpp +1 codemap drift does NOT affect operator.cpp/hpp or
the callsite cohort — all anchors confirmed on the asserted lines). The theme is `firm`: every
claim is positively anchored (no negative-anchor reconstruction); the only constructive ingredient
is the value-level algebraic identity `xᴴ B x ∈ ℝ_{≥0}` for SPD `B`, read off the L0 source's own
assertion. (The upstream L1 operator stays `rough-in (test-coverage-bounded)` — that is its own
promotion gate, not this theme's; a firm lowering of a rough-in L1 operator is consistent, as the
rewrite's structural fidelity is independent of the L1 law-confidence gate, same as
`eigsolve-mutation-rotation` firm over rough-in `L1/eigsolve`.)

## Proposed changes

```edit:book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md
# matrix-weighted-norm-mutation-rotation

The mutation rotation for the operator-weighted (energy) norm. Lowers the pure L1 form
`matrix_weighted_norm(x, B) = √(xᴴ B x)` ([`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md),
rough-in) into Palace's L0 `linalg::Norml2(comm, x, B, Bx)` three-step composition
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
signature. The LHS shape (rough-in; see [`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md)):

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
[`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md) §Applicability conditions.

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
- `palace/linalg/apply-linop-mutation-rotation.md` Sub-pattern A — the inherited `B.Mult(x, Bx)`
  lowering (operator-apply into a destination buffer).  [theme reference, see Verified-against]
- `palace/linalg/dot-mutation-rotation.md` Sub-pattern A — the inherited `Dot(comm, Bx, x)`
  lowering (the `Mpi::GlobalSum ∘ LocalDot` two-step + the arg-2-conjugated convention).
  [theme reference, see Verified-against]

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
  promotion-gate question flagged at [`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
  §Variant axes — whether L1 admits it as a distinct variant or a uniform rule. This theme records
  it faithfully as the L0 surface; the L1-side resolution is upstream.)**
- **The guard is two-part** (`:616-617`): `dot.real() > 0.0` (the SPD positivity, as in the real
  branch) **and** `std::abs(dot.imag()) < 1.0e-9 * dot.real()` (a **numerical Hermiticity witness**
  — for SPD `B` the form `xᴴ B x` is real, so the imaginary part of the computed `dot` must be
  round-off only). The return is `std::sqrt(dot.real())` (`:618`) — the imaginary part is
  **discarded**, not folded, because the assertion has confirmed it is round-off. This confirms the
  L1 "result is always real" rule is a direct algebraic consequence of `B` being SPD
  ([`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md) §Signature).

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

## The caller-owned workspace `Bx` — the matrix-weighted machinery

The distinguishing feature of this theme over `nrm2-mutation-rotation` is the **workspace `Bx`**.
Unlike `nrm2` / `dot` (no buffer at all — the result is a stack scalar), the weighted norm needs a
materialized `B·x` to feed the inner `Dot`. At L0 this is a **caller-supplied** parameter
`VecType &Bx`, and it is a **destination** buffer (step 1 overwrites it entirely), not transient
scratch:

- **It is caller-owned, not internally allocated.** Contrast the sibling bilinear-form
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
in-file references in [`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md) deferring the
`Bx`-ownership unfold to this theme). It is **resolved**: `Bx` is a caller-owned destination buffer,
materialized in the lowering, erased at L1.

## The `MFEM_ASSERT(dot > 0.0)` SPD guard — classification

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

## Reduction tree — load-bearing-numerical recording

The weighted norm accumulates non-associativity from **two** inherited sources (per
[`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md) §Semantics):

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

**None.** This theme lowers the existing L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
operator (rough-in, test-coverage-bounded) into existing firm L1 vocabulary — `apply_linop` for the
`B·x` step, `dot` for the inner reduction, `scal` for the `Normalize` consumer. It proposes no new
L1 vocabulary. The sibling **bilinear-form** `linalg::Dot(comm, x, A, y) = yᴴ A x`
(`palace/linalg/operator.hpp:386-389`, `palace/linalg/operator.cpp:621-639`) shares the L0 file block and the same two L1
primitives but with the diagonal restriction lifted (`y ≠ x`) and **internally-allocated** workspace
`Ax` (Category-4 synthetic workspace) rather than caller-supplied `Bx`; it is a **different
operator** ([`L1/bilinear-form`](../L1/bilinear-form.md)) and the subject of a separate forthcoming
theme `bilinear-form-mutation-rotation`. It is named here only to mark the boundary; it is **not**
part of this theme. (The energy norm is the diagonal case `y = x` of the bilinear form, plus the
outer `√` and the SPD applicability condition.)

## Variant axes

`matrix-weighted-norm` has two orthogonal variant axes at the L1>L0 edge (per
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

## Verified-against

L0 evidence ranges (self-verified via `tools/citecheck/citecheck.py --anchor` against on-disk
`reference/palace/` this invocation — producer-citation self-verification, `verify-citation-range`;
cycle-025 nleps.cpp +1 codemap drift confirmed NOT to affect operator.cpp/hpp or the callsite
cohort, all anchors land on the asserted lines):

- `palace/linalg/operator.cpp:599-607` — real `Norml2` specialization: `B.Mult(x, Bx)` (`:602`),
  `double dot = Dot(comm, Bx, x)` (`:603`), `MFEM_ASSERT(dot > 0.0, ...)` (`:604-605`),
  `return std::sqrt(dot)` (`:606`). **Self-verified.**
- `palace/linalg/operator.cpp:609-619` — complex `Norml2` specialization:
  `// For SPD B, xᴴ B x is real.` (`:612`), `B.Mult(x.Real(), Bx.Real())` /
  `B.Mult(x.Imag(), Bx.Imag())` (`:613-614`), `std::complex<double> dot = Dot(comm, Bx, x)`
  (`:615`), two-part `MFEM_ASSERT` (`:616-617`), `return std::sqrt(dot.real())` (`:618`).
  **Self-verified.**
- `palace/linalg/operator.hpp:372-374` — `Norml2(comm, x, B, Bx)` decl + comment
  `// Calculate the vector norm with respect to an SPD matrix B.` (`:372`). The SPD precondition
  at L0. **Self-verified.**
- `palace/linalg/operator.hpp:377-384` — `Normalize(comm, x, B, Bx)` inline def:
  `norm = Norml2(...)` (`:380`), `MFEM_ASSERT(norm > 0.0, ...)` (`:381`), `x *= 1.0 / norm`
  (`:382`). Sub-pattern C consumer. **Self-verified.**
- `palace/linalg/operator.hpp:386-389` — sibling bilinear-form `Dot(comm, x, A, y)` decl + comment
  `// Compute the bilinear form inner product yᴴ A x ... Allocates workspace internally.`
  (`:386-387`). Cited only to mark the boundary (internally-allocated `Ax` vs caller-supplied `Bx`).
  **Self-verified.**
- `palace/linalg/arpack.cpp:433-444` — `ArpackEigenvalueSolver::GetEigenvectorNorm`: dispatches to
  `linalg::Norml2(comm, x, *opB, Bx)` (`:438`) when `opB` non-null, else unweighted
  `linalg::Norml2(comm, x)` (`:442`). Weighted-norm callsite in M-orthonormalisation.
  **Self-verified.**
- `palace/linalg/arpack.cpp:470` — `xscale.get()[i] = 1.0 / GetEigenvectorNorm(x1, y1);` — the
  reuse-`Bx`-across-eigenvectors loop body (`y1` is the reused `Bx`). **Self-verified.**
- `palace/linalg/slepc.cpp:470-481` — `SlepcEigenvalueSolver::GetEigenvectorNorm`: identical
  pattern, `linalg::Norml2(GetComm(), x, *opB, Bx)` (`:475`; note `GetComm()` not bare `comm`).
  **Self-verified.**
- `palace/linalg/slepc.cpp:505` — `xscale.get()[i] = 1.0 / GetEigenvectorNorm(x1, y1);` (SLEPc
  reuse loop). **Self-verified.**
- `palace/linalg/nleps.cpp:109-120` — `NonLinearEigenvalueSolver::GetEigenvectorNorm`: identical
  pattern, `linalg::Norml2(comm, x, *opB, Bx)` (`:114`). Three-backend consistency confirms the
  M-orthonormalisation role. **Self-verified.**
- `palace/linalg/nleps.cpp:146` — `xscale.get()[i] = 1.0 / GetEigenvectorNorm(x1, y1);` (NLEPS
  reuse loop). **Self-verified.**
- `book/src/L0/linalg-operator-file.md:30-34` — the L0 chapter naming the `linalg::` free-function
  block (the SPD-weighted `Norml2(comm, x, B, Bx)`, the `Normalize`, the sibling bilinear-form
  `Dot(comm, x, A, y)`, `SpectralNorm`). **Self-verified.**

L1 / cross-theme anchors:

- `book/src/L1/matrix-weighted-norm.md` — the L1 operator this theme lowers (rough-in,
  test-coverage-bounded): closed form `√(xᴴ B x)` (`:18-19`), law 8 self-bilinear identity (`:58`),
  SPD applicability conditions (`:72-79`), the workspace-ownership deferral (`:11`, `:99`,
  `:122`), the real-`B`-on-complex-`x` variant-gate question (`:106`).
- `book/src/L1-L0/apply-linop-mutation-rotation.md` — Sub-pattern A (bare `B.Mult(x, Bx)` forward
  apply into a destination buffer) inherited as step 1; the `complex-from-real-lift` for the complex
  branch's real/imaginary split (§Applicability condition 3).
- `book/src/L1-L0/dot-mutation-rotation.md` — Sub-pattern A (`linalg::Dot(comm, Bx, x)` =
  `Mpi::GlobalSum ∘ LocalDot`) inherited as step 2; the arg-2-conjugated convention + the
  re-order-invisible-for-real-projection case (§"The conjugation asymmetry").
- `book/src/L1-L0/nrm2-mutation-rotation.md` — the unweighted relative; the `B = I` degenerate
  collapse meets it exactly, and the `std::abs`-guard classification precedent informs the
  `MFEM_ASSERT`-guard classification here.
- `book/src/L1-L0/scal-mutation-rotation.md` — the `x *= 1.0/norm` step in the `Normalize` consumer
  (Sub-pattern C).
- `book/src/L1/apply_linop.md:50,53-55` — laws 1 (linearity in x), 4/5/6 (composition / sum /
  scalar) underwriting the `B·x` step.
- `book/src/L1/dot.md:43,45` — the arg-1-conjugated L1 convention + the load-bearing
  reduction-tree non-law underwriting the inner reduction.

## Status

`firm` — the rewrite is the structural expansion of the L0 `Norml2(comm, x, B, Bx)` three-step
composition `B.Mult → Dot → sqrt`, exhaustively pinned by direct, self-verified evidence (the two
specializations `palace/linalg/operator.cpp:599-607` / `:609-619`, the decl + SPD comment `palace/linalg/operator.hpp:372-374`,
the `Normalize` consumer `palace/linalg/operator.hpp:377-384`, the three-backend M-orthonormalisation callsite
cohort `arpack.cpp:438,470` / `slepc.cpp:475,505` / `nleps.cpp:114,146`). The two sub-patterns
(A real, B complex), the Sub-pattern C consumer, the element-type and weight-operator variant axes,
the `B = I` degenerate collapse, the caller-owned-workspace boundary, and the SPD-guard
classification are all directly cited. The theme **reuses** the firm/rough-in sibling sub-themes
(`apply_linop` Sub-pattern A, `dot` Sub-pattern A, `scal`) rather than restating them. The one
non-syntactic ingredient — `xᴴ B x ∈ ℝ_{≥0}` for SPD `B` — is positively anchored to the L0
source's own comment (`:612`) and assertion (`:616-617`); **no negative-anchor reconstruction, no
literature inference, no speculative operator** — so `firm` rather than `partly-constructive`.

**Note on the upstream L1 gate.** The L1 operator [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
is `rough-in (test-coverage-bounded)` (its algebraic-law confidence is test-gated). A firm lowering
of a rough-in L1 operator is consistent: the lowering's structural fidelity (does the L1 form
expand into this L0 source?) is independent of the L1 law-confidence gate (are the L1 laws
test-confirmed?). Precedent: [`eigsolve-mutation-rotation`](./eigsolve-mutation-rotation.md) is firm
over the rough-in `L1/eigsolve`. Promoting the L1 operator to firm (its own gate) does not change
this theme's status; it would only strengthen the LHS the theme already lowers.

A `lowering-verifier` audit attaching the `verified_against:` block (per the sibling-theme
convention) confirming the surface-form recognition is exhaustive (no un-cited `Norml2` overload,
the inherited-sub-theme boundaries hold, the `Bx` workspace reading is consistent) is the standard
follow-up, not a status reduction.
```

Insert the new `matrix-weighted-norm-mutation-rotation` row into the §"Theme list" table,
**after** the existing `dot-mutation-rotation` row (the two existing rows below are the
context anchor; only the third row is new — the stub was never listed in this table, only in
SUMMARY.md). The row's L0 anchor uses a `(rough-in)` L1-anchor annotation because the upstream
L1 operator is `rough-in (test-coverage-bounded)`; the **theme itself** is `firm` (a firm
lowering of a rough-in L1 operator, the `eigsolve-mutation-rotation` precedent).

```edit:book/src/L1-L0/index.md
| [scal-mutation-rotation](./scal-mutation-rotation.md) | `L1/scal` (firm) | `palace/linalg/vector.{hpp,cpp}`, `palace/linalg/{iterative,operator,nleps}.cpp` | firm *(structural; 2 element-type overloads; transparent complex imag==0 shape branch)* |
| [dot-mutation-rotation](./dot-mutation-rotation.md) | `L1/dot` (firm) | `palace/linalg/vector.{hpp,cpp}`, `palace/utils/communication.hpp` | firm *(structural; 3 surface forms; conjugate-pair re-order `xᴴ y = conj(yᴴ x)`; tdot type-API-surface-only)* |
| [matrix-weighted-norm-mutation-rotation](./matrix-weighted-norm-mutation-rotation.md) | `L1/matrix-weighted-norm` (rough-in) | `palace/linalg/operator.{hpp,cpp}`, `palace/linalg/{arpack,slepc,nleps}.cpp` | firm *(structural; 2 element-type sub-patterns A real/B complex + Normalize consumer C; reuses apply_linop A `B.Mult(x,Bx)` + dot A `Dot(comm,Bx,x)` + scal; caller-owned destination workspace Bx; SPD `MFEM_ASSERT(dot>0)` load-bearing defensive guard + complex Hermiticity witness; B=I collapses to nrm2)* |
```

SUMMARY.md already carries the entry at line 103 with a `(stub)` suffix; drop the suffix so the
chapter link reflects the promoted status (the `[<slug>](path)` link itself is unchanged):

```edit:book/src/SUMMARY.md
- [matrix-weighted-norm-mutation-rotation](./L1-L0/matrix-weighted-norm-mutation-rotation.md)
```

## Speculative operators proposed

**None.** This is a stub→firm promotion of a lowering theme for an **existing** L1 operator
([`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md), rough-in). The theme decomposes
entirely into existing firm L1 vocabulary — `apply_linop` (the `B·x` step), `dot` (the inner
reduction `xᴴ(B·x)`), `scal` (the `Normalize` consumer's `x *= 1/norm`). No new L1 operators are
needed; harvester has nothing to promote from this theme. (The sibling `bilinear-form` is an
*already-queued* separate rough-in with its own forthcoming theme, not a speculative operator
emitted by this one.)

## Supporting evidence

L0 source (all self-verified via `tools/citecheck/citecheck.py --anchor` against on-disk
`reference/palace/` this invocation; `--scan` bounds-check clean — see Open questions):

- `palace/linalg/operator.cpp:599-607` (real `Norml2`), `:609-619` (complex `Norml2`) — the two
  three-step specializations. Body lines: real `B.Mult` `:602`, `Dot` `:603`, `MFEM_ASSERT`
  `:604-605`, `sqrt` `:606`; complex SPD comment `:612`, lane-split `B.Mult` `:613-614`, `Dot`
  `:615`, two-part `MFEM_ASSERT` `:616-617`, `sqrt(dot.real())` `:618`.
- `palace/linalg/operator.hpp:372-374` (decl + SPD comment), `:377-384` (`Normalize` consumer),
  `:386-389` (sibling bilinear-form boundary).
- `palace/linalg/arpack.cpp:433-444,470` / `slepc.cpp:470-481,505` / `nleps.cpp:109-120,146` — the
  three-backend `GetEigenvectorNorm` M-orthonormalisation callsite cohort (weighted dispatch +
  `Bx`-reuse loop).
- `book/src/L0/linalg-operator-file.md:30-34` — the L0 file-layout chapter.

Sibling themes inherited (not restated): `apply-linop-mutation-rotation` Sub-pattern A,
`dot-mutation-rotation` Sub-pattern A, `scal-mutation-rotation`; relative `nrm2-mutation-rotation`
(the `B = I` degenerate collapse + abs-guard classification precedent).

L1 anchors: `book/src/L1/matrix-weighted-norm.md` (the lowered operator),
`book/src/L1/apply_linop.md:50,53-55`, `book/src/L1/dot.md:43,45`.

## Open questions / caveats

1. **Carry-forward correction for `L1/matrix-weighted-norm.md` (off-by-one on the real-spec body
   span).** The L1 entry cites the real `Norml2` body as `palace/linalg/operator.cpp:601-606` in
   two places (`:58` law 8, `:83` Composition note) and `:600-619` / `:599-619` for the full pair.
   (The Evidence-section citation at `:128` is the *correct* full-span `:599-607` — NOT a drift
   site.) On-disk
   (citecheck-authoritative): the real specialization is `599-607` (`template <>` `:599`,
   signature `:600`, `{` `:601`, body `602-606`, `}` `:607`). The cited `:601-606` starts at the
   opening brace `{` (line 601 is `{`, not `B.Mult`); the body content is `602-606`. **This is a
   change to PROPOSE for the L1 entry, not for me to apply** (the L1 entry is out of an abstractor's
   write-scope and is append-only-after-integration; flagging for a `lowering-verifier` /
   `harvester` follow-up). The complex-spec citations (`:609-619`, assert `:616-617`, split
   `:613-614`) are all correct as cited. Recorded for OQ
   `matrix-weighted-norm-mutation-rotation-l1-l0-theme`.
2. **Pre-existing "Category 4 — synthetic workspace" mislabel** in both
   `book/src/L1/matrix-weighted-norm.md:9` and `book/src/L0/linalg-operator-file.md:33` for the
   sibling bilinear-form `Dot(comm, x, A, y)`. The `mutable-workspace-pattern.md` chapter has only
   4 categories and **Category 4 is "assembled-matrix retention," not "synthetic workspace."** The
   internally-allocated `Ax` of the bilinear form is not one of that chapter's four categories at
   all (it is a per-call fresh allocation, not a retained `mutable` member). This theme does **not**
   rely on that category (the `Norml2` workspace `Bx` is **caller-supplied**, described accurately
   in §"The caller-owned workspace `Bx`"). Flagged as a drive-by cross-reference drift for a
   `same-layer-cross-cutter` / `lowering-verifier` follow-up; not corrected here (out of write-scope
   + not in this theme's focus). New OQ candidate:
   `bilinear-form-workspace-category-4-mislabel`.
3. **Paired firm-promotion gate: `matrix-weighted-norm-mixed-element-type-variant`.** The complex
   branch's real-`B`-on-complex-`x` lane split (Sub-pattern B) is the variant-gate question the L1
   entry flags (`:106`): does L1 admit real-`B`-on-complex-`x` as a distinct element-type variant
   or absorb it into a uniform `apply_linop` rule? This theme records the L0 surface faithfully
   (the two `B.Mult` lane applies) but does not resolve the L1-side variant policy. It is **paired**
   with the `bilinear-form` firm-promotion gate (both share the real-`A`/`B`-on-complex-vector
   plumbing and the same two L1 primitives). Recommend a follow-up `lowering-verifier` pass that
   audits this theme + the (forthcoming) `bilinear-form-mutation-rotation` together for the
   shared element-type-variant resolution, and (separately) audits the upstream
   `L1/matrix-weighted-norm` test/literature coverage gate. OQ:
   `matrix-weighted-norm-mixed-element-type-variant` (paired with `bilinear-form` promotion).
4. **The forward-reference target named in the dispatch scope
   (`book/src/L1-L0/bilinear-form-mutation-rotation.md`) does not yet exist.** The actual current
   forward-references to `matrix-weighted-norm-mutation-rotation` are from the L1 entry and
   `nrm2-mutation-rotation.md` (the bilinear-form *L1 entry* `book/src/L1/bilinear-form.md` exists,
   but no `bilinear-form-mutation-rotation` L1>L0 theme does). This theme is now the live home for
   those references; the `bilinear-form-mutation-rotation` theme remains a separate forthcoming
   work item (the diagonal `y = x` boundary is noted in §"Speculative L1 operators"). No action —
   recorded so the integrator/planner does not expect a `bilinear-form-mutation-rotation` anchor to
   resolve yet.
5. **`slepc.cpp` uses `GetComm()` not bare `comm`** in `GetEigenvectorNorm` (`:475`:
   `linalg::Norml2(GetComm(), x, *opB, Bx)`), whereas arpack/nleps use `comm`. A cosmetic surface
   difference (both resolve to the rank communicator); cited accurately. No semantic consequence
   under single-rank scope.

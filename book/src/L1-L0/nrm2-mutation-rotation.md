---
# Lowering theme (L1>L0), cycle-115 D2 hygiene: previously NO frontmatter (rank prose-inferred
# from `## Status` `firm`). Per graded-stack scheme §5, theme rank = min(endpoint ranks); the L1
# endpoint (`L1/nrm2`) is firm (rank 3), L0 endpoint rank-terminal, so the theme is firm. The
# op->theme edge (`L1/nrm2 →lowers-to→ this theme`, c114) lives on the op side and is NOT re-added.
# This theme carries its OWN outbound `cites-evidence` edges to the L0 `Norml2` one-line
# composition it lowers to (and the `Dot` leaf + collective the chain bottoms out in — the
# inherited dot sub-theme, recorded here as the cited evidence of nrm2's own L0 surface).
# All ranges self-verified on disk via citecheck --anchor this invocation.
rank: firm
edges:
  depends-on:
    - target: palace/linalg/vector.hpp:254-259
      kind: cites-evidence        # Norml2(comm,x) template body = std::sqrt(std::abs(Dot(comm,x,x))) (Sub-pattern A; the load-bearing line)
    - target: palace/linalg/vector.hpp:246-253
      kind: cites-evidence        # the Dot leaf = LocalDot + Mpi::GlobalSum the chain bottoms out in (inherited dot sub-theme)
    - target: palace/utils/communication.hpp:266-270
      kind: cites-evidence        # Mpi::GlobalSum(len,buff,comm) → GlobalOp(...,MPI_SUM,...)
    - target: palace/utils/communication.hpp:246-249
      kind: cites-evidence        # GlobalOp body = MPI_Allreduce(MPI_IN_PLACE,...) — the collective
---

# nrm2-mutation-rotation

The mutation rotation for the BLAS-1 Euclidean-norm reduction. Lowers the pure L1 form
`nrm2(x) = √⟨x, x⟩` into Palace's L0 `linalg::Norml2` one-line composition — a four-stage
chain `Dot → MPI_Allreduce → std::abs → std::sqrt`. Unlike the axpy-shaped themes there is
**no destination buffer**: the L1 result lowers to a return register / stack scalar, so the
"mutation rotation" on the buffer side is essentially a no-op. What the theme records is the
expansion of one pure reduction step into the L0 reduction chain, the reintroduction of the
MPI collective that the L1 signature hides, and the classification of the outer `std::abs`
defensive guard.

## Slug

`nrm2-mutation-rotation`

## L1 form (LHS)

The pure-functional reduction consumes a read-only vector and produces a fresh real scalar;
nothing is mutated. One LHS shape (firm; see [`L1/nrm2`](../L1/nrm2.md)):

    alpha = nrm2(x)                    -- alpha = √⟨x, x⟩, always real, non-negative

The defining identity (L1 algebraic law 8) is `nrm2(x) = √dot(x, x)`, where `dot` is the
firm L1 Hermitian inner product ([`L1/dot`](../L1/dot.md)). The element-type axis is already
collapsed at L1: a single operator `nrm2 :: Tensor[N] -> Scalar(real)` regardless of whether
`x` is real or complex (the Hermitian self-dot is real and non-negative for both — L1 dot
laws 4 and 9). The MPI collective is **not** in the L1 signature; the L1 reduction is a
single semantic step.

## L0 form (RHS)

The L1 reduction lowers into a one-line free-function template plus its method-form and
wrapper conveniences. The body is **the same four-stage chain** in all surface forms; the
forms differ only in which `Dot` leaf is invoked and whether the MPI collective is present.

### Sub-pattern A — free-function template (the canonical form)

    template <typename VecType>
    inline auto Norml2(MPI_Comm comm, const VecType &x)
    {
      return std::sqrt(std::abs(Dot(comm, x, x)));     // vector.hpp:259
    }

The single load-bearing line. It expands the one pure L1 step `√dot(x,x)` into four L0
stages, evaluated inside-out:

1. **`Dot(comm, x, x)`** — the parallel Hermitian self-inner-product. `Dot` itself
   (`vector.hpp:247-252`) is a two-step: `LocalDot(x, x)` (the rank-local sum-of-squares)
   followed by `Mpi::GlobalSum(1, &dot, comm)`. This is the same `dot` lowering theme
   ([`dot-mutation-rotation`](./dot-mutation-rotation.md), forthcoming); `nrm2`'s lowering
   *inherits* the dot MPI-collective sub-theme rather than restating it.
2. **`MPI_Allreduce`** — `Mpi::GlobalSum` (`communication.hpp:267-270`) delegates to
   `GlobalOp(len, buff, MPI_SUM, comm)` (`communication.hpp:246-249`), whose body is
   `MPI_Allreduce(MPI_IN_PLACE, buff, len, ..., MPI_SUM, comm)`. The reduction is in-place
   and broadcast to all ranks. **Single-rank is in scope** (CLAUDE.md "Scope"), so this stage
   lowers to a local no-op (one rank, nothing to reduce), but it is structurally present and
   carries the bit-deterministic-reduction-order trade-off already recorded for `dot`.
3. **`std::abs(...)`** — the **defensive non-negativity guard** (classified below).
4. **`std::sqrt(...)`** — the principal (non-negative) real square root. A deterministic,
   correctly-rounded IEEE-754 scalar primitive; below the L1 layer's resolution. It does not
   contribute to `nrm2`'s non-determinism (which is entirely the reduction-tree
   non-associativity inherited from `Dot`).

Justification kind: **structural** — the rewrite is the syntactic expansion of one pure L1
reduction into the L0 composition; the destination is the return register, not a buffer.

Citations:
- `palace/linalg/vector.hpp:254-259` — `Norml2` template; body line 259 is
  `return std::sqrt(std::abs(Dot(comm, x, x)));`.
- `palace/linalg/vector.hpp:247-252` — `Dot` = `LocalDot` + `Mpi::GlobalSum` (the inner
  two-step the chain bottoms out in).
- `palace/utils/communication.hpp:267-270` — `Mpi::GlobalSum(len, buff, comm)` →
  `GlobalOp(len, buff, MPI_SUM, comm)`.
- `palace/utils/communication.hpp:246-249` — `GlobalOp` body is `MPI_Allreduce(MPI_IN_PLACE,
  buff, len, mpi::DataType<T>(), op, comm)`.

### Sub-pattern B — method-form (real Vector, no MPI)

    double norm1 = vec1.Norml2();                       // mfem::Vector::Norml2()

The MFEM real-vector method computes `√Σ x[i]²` directly with **no MPI collective** (it is a
rank-local serial method). At L1 this is the *same* `nrm2` operator: the method-form is the
single-rank specialisation of sub-pattern A with the collective elided and the leaf fixed to
the real sum-of-squares. (`Vector::Norml2()` is an upstream MFEM method, not Palace source;
it is cited only as the surface form Palace's tests exercise.)

Justification kind: **structural** — identical reduction, collective elided under
single-rank scope.

Citations:
- `test/unit/test-vector.cpp:209-211` — `double norm1 = vec1.Norml2(); CHECK_THAT(norm1,
  WithinRel(std::sqrt(14.0)));` for `vec1 = (1,2,3)`. Confirms `nrm2((1,2,3)) = √14`, the
  real-valued `double` return, and the method-form surface. L0-equivalent semantic
  documentation (CLAUDE.md "Tests as semantic supplement").

### Sub-pattern C — caller-side wrapper

    auto Norml2(MPI_Comm comm) const { return linalg::Norml2(comm, local); }

`ErrorIndicator::Norml2(comm)` (`errorindicator.hpp:43`) is a **transparent wrapper**: it
forwards to the free-function template (sub-pattern A) on the object's `local` member.
Recognition is by the one-line delegating body; it adds no algebra.

Justification kind: **structural** — pure delegation; same chain as sub-pattern A.

Citations:
- `palace/fem/errorindicator.hpp:43` — `auto Norml2(MPI_Comm comm) const { return
  linalg::Norml2(comm, local); }`.

## The `std::abs` defensive guard — classification

Resolves OQ `nrm2-std-abs-defensive-guard-classification`. The outer `std::abs` in
`std::sqrt(std::abs(Dot(comm, x, x)))` is a **load-bearing numerical guard**, not a
transparent performance trick. Applying the CLAUDE.md "Optimization tricks vs. base algebra"
framing:

- It is **a no-op in exact arithmetic.** The Hermitian self-dot `dot(x,x) = Σ |x[i]|²` is
  mathematically real and non-negative for both real (L1 dot law 4) and complex (L1 dot law
  9) inputs, so `abs` of it equals it exactly. This is why it **disappears at L1** — the
  algebraic claim "`dot(x,x)` is non-negative real" subsumes it.
- It is **load-bearing in floating point**, where it performs the *same* sign-strip on both
  element-type paths — both buying the property **domain-safety for `sqrt` (no NaN)**:
  - **Real path** (`Dot` returns `double`): `std::abs(double)` strips a sign that round-off
    in the rank-local-then-collective summation could have flipped negative on a numerically
    zero (or tiny) vector. Without it, `std::sqrt` of a tiny-negative would return `NaN`.
  - **Complex path** (`Dot` returns `std::complex<double>`): for the self-dot `Dot(comm,x,x)`
    the imaginary part is **exactly `0.0`** — `ComplexVector::Dot` (`vector.cpp:264-267`) takes
    the `this == &y` self-aliasing fast path and returns `{re, 0.0}` (the same transparent fast
    path recorded in `L0/transparent-vs-load-bearing-tricks.md:13`). So `std::abs` of the
    `std::complex<double>{re, 0.0}` degenerates to `|re|` — identical to the real-path
    sign-strip, not a residual-imaginary-folding modulus. The complex element type changes only
    *how the leaf `LocalDot` accumulates* (real + imaginary lane sums); by the time `std::abs`
    runs, the argument is already a real-valued `{re, 0.0}`, and the guard's role is exactly the
    real-path sign-strip.
- **Property it buys**: domain-safety / non-negativity invariant for the square root, i.e.
  `nrm2(x) ≥ 0` and never `NaN`, holding across round-off and the real/complex element-type
  split. It does **not** change any result in exact arithmetic, so it is not part of the
  algorithm in the load-bearing-numerical-trick sense (it buys no determinism / condition
  number / IEEE compliance beyond NaN-avoidance), but it is **not erasable** without
  introducing a NaN failure mode — hence load-bearing-defensive, not transparent.

**Verdict: load-bearing numerical (defensive guard).** It matches the existing
[`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md)
"Defensive non-negativity guard" worked example for `linalg::Norml2` (the L1 entry's
referenced-from target). The guard does NOT contradict the L1 algebraic claim — it
*implements* it under floating point.

Note (not a Palace guarantee): the [`concepts/nrm2`](../concepts/nrm2.md) page already records
(§Contract) that `linalg::Norml2` computes the naive `√⟨x,x⟩` and does **not** use BLAS-style
scaled summation, so it inherits any over/underflow risk. The `std::abs` guard defends against
round-off sign-flips, **not** against overflow. This theme's classification is consistent with
that concept-page note and the L0 tricks page; no correction is needed.

## Applicability conditions

The rewrite preserves semantics when:

1. **Read-only `x`.** `nrm2` never writes `x`; the L0 chain only reads it (the `Dot` leaf is
   `const VecType &x`). No aliasing or destination-buffer concern arises (there is no
   destination buffer — the result is a returned scalar). This is the structurally simplest
   BLAS-1 lowering: no in-place-mutation applicability conditions at all.
2. **Single-rank reading of the collective.** The `MPI_Allreduce` stage is read as a local
   no-op under the in-scope single-machine target (CLAUDE.md "Scope"). The L1 form already
   hides the collective; the lowering reintroduces it only as structural record. Multi-rank
   bit-determinism is the same caveat as `dot` and is out of scope.
3. **Element type real or complex, result always real.** The variant axis (below) is
   absorbed entirely by the `Dot` leaf and the meaning of `std::abs`; the surrounding chain
   is element-type-agnostic.
4. **`x` is a value, not a special form.** The leaf `Dot(comm, x, x)` passes `x` twice; there
   is no scalar argument and no constant-folding sub-pattern selection (contrast the
   axpy theme's α-folding). Surface-form selection (A/B/C) is recognition on the call site
   (free function vs MFEM method vs `ErrorIndicator` wrapper), not on argument values.

## Justification kind

- **Sub-pattern A** — `structural`. Expand one pure L1 reduction into the L0
  `sqrt∘abs∘Dot` chain; destination is the return register.
- **Sub-pattern B** — `structural`. Same reduction, MPI collective elided under single-rank.
- **Sub-pattern C** — `structural`. Pure delegation to A.

The theme as a whole is `structural`, resting on one algebraic identity (L1 law 8,
`nrm2(x) = √dot(x,x)`) and one load-bearing-trick classification (the `std::abs` guard,
above). A `lowering-verifier` audit in a later cycle should attach the `verified_against:`
block (per the axpby-theme convention) confirming the surface-form recognition matches the
L0 corpus and that no fourth surface form (e.g. an un-cited overload) is missed.

## Speculative L1 operators

None. This theme lowers the already-firm L1 `nrm2` operator; it proposes no new L1
vocabulary. The B-weighted overload `linalg::Norml2(comm, x, B, Bx) = √(xᴴ B x)`
(`operator.cpp:600-619`, declared `operator.hpp:372-374`) shares the L0 symbol via
overloading but is a **different operator** with a different L1 referent
([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)) — it requires the operator-
application primitive and a workspace `Bx`, and is the subject of a separate forthcoming
theme `matrix-weighted-norm-mutation-rotation`. It is named here only to mark the boundary;
it is **not** part of this theme.

## Verified-against

L0 evidence ranges (self-verified against source 2026-05-29 before emit):

- `palace/linalg/vector.hpp:254-259` — `Norml2` template; body line 259
  `std::sqrt(std::abs(Dot(comm, x, x)));`.
- `palace/linalg/vector.hpp:247-252` — `Dot` = `LocalDot` + `Mpi::GlobalSum`.
- `palace/linalg/vector.hpp:261-269` — `Normalize` uses `Norml2` then asserts `norm > 0.0`
  and scales `x *= 1.0 / norm`; confirms `nrm2` returns a positive real divisor.
- `palace/utils/communication.hpp:267-270` — `Mpi::GlobalSum` → `GlobalOp(.., MPI_SUM, ..)`.
- `palace/utils/communication.hpp:246-249` — `GlobalOp` body `MPI_Allreduce(MPI_IN_PLACE,
  buff, len, mpi::DataType<T>(), op, comm)`.
- `palace/fem/errorindicator.hpp:43` — `ErrorIndicator::Norml2(comm)` wrapper.
- `palace/linalg/iterative.cpp:408` — `beta_rhs = linalg::Norml2(comm, b);` (PCG initial
  RHS norm; convergence-test fan-out).
- `palace/linalg/iterative.cpp:631` — `Hj[j+1] = linalg::Norml2(comm, w); w *= 1.0/Hj[j+1];`
  (GMRES Arnoldi sub-diagonal coefficient + basis-vector normalisation; orthogonalisation
  fan-out).
- `test/unit/test-vector.cpp:209-211` — `vec1.Norml2()` == `√14` for `(1,2,3)`.

L1 anchor:

- `book/src/L1/nrm2.md` — the firm L1 operator this theme lowers (algebraic law 8 is the
  identity the rewrite rests on).

## Status

`firm` — the rewrite is the structural expansion of the one-line L0 `Norml2` definition,
exhaustively pinned by direct evidence (`vector.hpp:259` is a single load-bearing line, inside
the L1 entry's already-correct `255-260` range). The
four-stage chain, the three surface forms, and the variant-axis collapse are all directly
cited. The `std::abs` guard is classified (load-bearing defensive) with the property it
buys stated. No constructive sub-part (no negative-anchor reconstruction): the theme makes
only positively-anchored claims, so `firm` rather than `partly-constructive`. The
`verified_against:` audit block is deferred to a `lowering-verifier` cycle (its authorship,
not the abstractor's).

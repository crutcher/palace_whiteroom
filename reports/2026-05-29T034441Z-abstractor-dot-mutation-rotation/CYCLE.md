---
agent: abstractor
invoked_at: 2026-05-29T034441Z
scope: L1>L0 theme — dot-mutation-rotation (promote stub → firm)
status: integrated
integrated_at: 2026-05-29T06:05:00Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-020 finalize (staging row #2). dot-mutation-rotation PROMOTED stub→firm (Hermitian inner-product mutation-rotation; two variant axes element-type real/complex + tdot unconjugated sibling; closes the cycle-019 nrm2 sub-pattern-A forward-ref nrm2=√∘abs∘dot). Full-file replacement of the stub; L1-L0/index dep-map row appended after nrm2; SUMMARY :82 in-place de-stub. Post-repair citation inline-anchor drifts (:667→:668 ×5, :679→:678 ×3) already fixed in the report before apply; enclosing ranges always correct. Resolves OQ l1-l0-dot-lowering-asymmetry (constituent of blas1-l1-l0-lowering-theme-gap; meta-phase migrates). L1>L0 themes contribute to 12→15. retroactive-budget 0; clean build."
inputs:
  - book/src/L1/dot.md (firm L1 operator; pins arg-1-conjugated convention at :34,:43)
  - book/src/L1-L0/dot-mutation-rotation.md (existing stub, materialized 2026-05-28)
  - book/src/L1-L0/nrm2-mutation-rotation.md (cycle-019 firm sibling; structural model)
  - book/src/L2-L1/inner-product-fold-specialization.md (cycle-019 firm; same conjugate-pair at L2>L1 edge)
  - palace/linalg/vector.cpp:263-267 (ComplexVector::Dot kernel — self-verified)
  - palace/linalg/vector.cpp:269-274 (ComplexVector::TransposeDot kernel — self-verified)
  - palace/linalg/vector.cpp:665-672 (LocalDot(Vector,Vector) — self-verified)
  - palace/linalg/vector.cpp:674-685 (LocalDot(ComplexVector,ComplexVector) — self-verified)
  - palace/linalg/vector.hpp:110-113, :242-244, :246-253 (decls + Dot template — self-verified)
  - palace/utils/communication.hpp:246-249, :266-270 (Mpi::GlobalSum / MPI_Allreduce — self-verified)
  - palace/linalg/iterative.cpp:395 (CG live call site — self-verified)
  - test/unit/test-vector.cpp:206-207 (real dot == 32.0 — self-verified)
---

# CYCLE: L1>L0 theme sketch — dot-mutation-rotation

## Summary

Promote the `dot-mutation-rotation` stub (materialized 2026-05-28) to a **firm** L1>L0
lowering theme. The theme narrates, forward L1 → L0, how the pure L1 Hermitian inner-product
`dot(x, y) = xᴴ y` (firm, `book/src/L1/dot.md`) lowers into Palace's L0 reduction surface:
the local element-kernel `LocalDot` followed by the `Mpi::GlobalSum` / `MPI_Allreduce`
collective (`linalg::Dot` = the two composed), plus the **conjugation asymmetry** — Palace's
`ComplexVector::Dot(y)` / `linalg::Dot(comm, x, y)` compute `yᴴ x` (conjugate **arg-2**),
while the L1 `dot` convention is `xᴴ y` (conjugate **arg-1**); the two are complex conjugates
(`xᴴ y = conj(yᴴ x)`). Like `nrm2-mutation-rotation`, there is **no destination buffer** — the
result lowers to a return register / stack scalar — so the "mutation rotation" is a no-op on
the buffer side; what the theme records is (i) the expansion of one pure reduction step into
the local-then-collective two-step the L1 signature hides, (ii) the conjugate-pair re-order
against the L0 source, and (iii) the pinned reduction tree (load-bearing-numerical residue).
`dot` is the **core** of the `nrm2` lowering (`nrm2 = √∘abs∘dot`, which already cites this
theme forward); promoting it firm closes that forward-reference. Resolves OQ
`l1-l0-dot-lowering-asymmetry`. Justification: **structural** (the rewrite is the syntactic
expansion of one pure L1 reduction into the L0 composition) resting on one value-level
algebraic identity (the conjugate-pair `xᴴ y = conj(yᴴ x)`).

## Theme prose (forward L1 → L0)

The narration below is high→low: LHS is the L1 `dot` form, RHS is the L0 source. The body of
the proposed chapter (in §Proposed changes) is the authoritative version; this section is the
prose walkthrough.

**LHS (L1).** `dot :: (x: Tensor[N], y: Tensor[N]) -> Scalar`, the firm Hermitian
inner-product `dot(x, y) = Σ conj(x[i])·y[i]` (complex) / `Σ x[i]·y[i]` (real), conjugate-
linear in the **first** argument (`book/src/L1/dot.md:33-34,43`). Pure / out-of-place; no
destination buffer; the MPI collective is **not** in the signature; the self-dot fast path
and reduction-tree non-associativity are recorded as L1 claims, not separate operators. The
unconjugated co-defined variant `tdot(x, y) = Σ x[i]·y[i]` (complex-only) shares the reduction
skeleton.

**RHS (L0).** The L1 step lowers into Palace's reduction family, in three surface forms that
share the same local-then-collective skeleton and differ only in which leaf is invoked and
whether the MPI collective is present:

- **Sub-pattern A — free-function template `linalg::Dot(comm, x, y)` (the canonical form).**
  Body (`vector.hpp:248-253`): `auto dot = LocalDot(x, y); Mpi::GlobalSum(1, &dot, comm);
  return dot;`. This is the two-step the L1 signature hides — a rank-local kernel
  (`LocalDot`) followed by the collective (`Mpi::GlobalSum` → `GlobalOp` →
  `MPI_Allreduce(MPI_IN_PLACE, …, MPI_SUM, comm)`, `communication.hpp:246-249,266-270`). The
  doc comment pins the L0 convention: `// Calculate the parallel inner product yᴴ x or yᵀ x`
  (`vector.hpp:246`) — **arg-2 conjugated**. Single-rank is in scope, so the collective
  lowers to a local no-op (one rank, nothing to reduce) but is structurally present and
  carries the bit-deterministic-reduction-order trade-off.

- **Sub-pattern B — method-form `(*this).Dot(y)` (complex, no MPI).** `ComplexVector::Dot`
  (`vector.cpp:263-267`) returns `{Re(x)·Re(y)+Im(x)·Im(y), (this==&y) ? 0.0 :
  Im(x)·Re(y)−Re(x)·Im(y)}` where `*this = x`. This equals `x·conj(y) = yᴴ x` — the receiver
  `*this` is the **linear** operand, the call argument `y` is the **conjugated** one. The
  declaration comment confirms: `// Vector dot product (yᴴ x) …` (`vector.hpp:110-111`). No
  MPI collective (it is a rank-local method); at L1 this is the single-rank specialisation of
  A with the collective elided.

- **Sub-pattern C — real free-function leaf `LocalDot(Vector, Vector)` / `mfem::Vector::
  operator*`.** The real leaf (`vector.cpp:665-672`) is one Hypre `hypre_SeqVectorInnerProd`
  strided pass (with `MFEM_ASSERT(x.Size()==y.Size())` at `:668`). Conjugation is a no-op for
  real element type, so `dot` and `tdot` collapse to the same `Σ x[i]·y[i]` here. The MFEM
  `operator*` is the test-exercised surface (`test/unit/test-vector.cpp:206-207`,
  `vec1 * vec2 == 32.0`).

**The conjugation asymmetry (the load-bearing theme content).** The L1 `dot` convention is
`xᴴ y` (arg-1 conjugated); every L0 surface form computes `yᴴ x` (arg-2 conjugated):
`vector.hpp:110,242,246` doc strings all read `yᴴ x`, and the kernel bodies **agree** with the
docs (`ComplexVector::Dot` body returns `x·conj(y) = yᴴ x`; the complex `LocalDot`,
`vector.cpp:674-685`, has the same `Im = LocalDot(xi,yr) − LocalDot(xr,yi)` arg-2-conjugated
sign). There is **no Palace-internal contradiction** — the asymmetry is between Palace's
`yᴴ x` and the L1 representation's `xᴴ y`. The two are complex conjugates:
`xᴴ y = conj(yᴴ x)`. So the L1 form `dot(x, y)` recovers from the L0 call by **either** the
operand-swap form `linalg::Dot(comm, y, x)` (arg-2 becomes `x`, conjugated → `xᴴ y`) **or** the
outer-conj form `conj(linalg::Dot(comm, x, y))`. For real-projected consumers (`std::real`,
`std::abs`) the re-order is **invisible** (`Re(z)=Re(conj z)`, `|z|=|conj z|`) — e.g. CG's
`β = ⟨r,z⟩` for SPD `B` (`iterative.cpp:395`, `beta = linalg::Dot(comm, z, r)`, used in real
arithmetic). For full-complex-value consumers the re-order is value-bearing. This is the same
conjugate-pair relationship the cycle-019 `inner-product-fold-specialization` theme narrated
at the L2>L1 edge (`book/src/L2-L1/inner-product-fold-specialization.md` §"The conjugate-pair
re-order"); this L1>L0 theme is the **L1-leaf-level** lowering of the same fact, cited there
for consistency.

**Reduction tree (load-bearing-numerical).** Reduction-tree non-associativity is load-bearing
(L1 dot §Semantics). The real leaf pins one Hypre strided pass; the complex leaf pins **four**
real Hypre passes combined into `(Re, Im)` by scalar `±`. Bit-identical reproduction of a
specific Palace call requires matching that tree, not merely the value.

**Self-dot fast path.** `&x == &y` triggers the transparent fast path: `ComplexVector::Dot`
returns imag `0.0` directly (`vector.cpp:266`), the complex `LocalDot` returns imag `0.0`
(`vector.cpp:678`). Transparent at L1 (`xᴴ x` is exactly real); it disappears in the lowering.

## Proposed changes

```edit:book/src/L1-L0/dot-mutation-rotation.md
# dot-mutation-rotation

The mutation rotation for the BLAS-1 inner-product reduction. Lowers the pure L1 form
`dot(x, y) = xᴴ y` ([`L1/dot`](../L1/dot.md), firm) into Palace's L0 reduction surface — the
rank-local element kernel `LocalDot` plus the `Mpi::GlobalSum` / `MPI_Allreduce` collective
(`linalg::Dot` = the two composed), the receiver-vs-argument **conjugation asymmetry**, and
the pinned reduction tree. Like [`nrm2-mutation-rotation`](./nrm2-mutation-rotation.md) (which
this theme is the **core** of — `nrm2 = √∘abs∘dot`, so `nrm2`'s lowering inherits this
`Dot`-collective sub-theme), there is **no destination buffer**: the L1 result lowers to a
return register / stack scalar, so the "mutation rotation" on the buffer side is a no-op. What
the theme records is the expansion of one pure reduction step into the L0 local-then-collective
two-step the L1 signature hides, the **conjugate-pair re-order** between the L1 `xᴴ y`
convention and Palace's L0 `yᴴ x` form, and the reduction-tree non-associativity (load-bearing
numerical). Sibling to the [`axpby`](./axpby-mutation-rotation.md) /
[`axpbypcz`](./axpbypcz-mutation-rotation.md) mutation-rotation themes (the BLAS-1
one-theme-per-operator pattern).

## Slug

`dot-mutation-rotation`

## L1 form (LHS)

The pure-functional reduction consumes two read-only vectors and produces a fresh scalar;
nothing is mutated. The LHS shape (firm; see [`L1/dot`](../L1/dot.md)):

    alpha = dot(x, y)      -- alpha = xᴴ y = Σ conj(x[i])·y[i]   (complex; Hermitian)
                           --       = Σ x[i]·y[i]                (real;   symmetric)
    alpha = tdot(x, y)     -- complex-only: alpha = Σ x[i]·y[i]  (unconjugated bilinear)

The conjugation convention is **conjugate-linear in the first argument**, linear in the
second — the standard mathematical Hermitian inner product `⟨x, y⟩ = xᴴ y`
([`L1/dot`](../L1/dot.md) §Semantics, `:43`). The MPI collective is **not** in the L1
signature; the L1 reduction is a single semantic step. The self-dot fast path
(`&x == &y`) and the reduction-tree non-associativity are recorded as L1 claims, not separate
operators ([`L1/dot`](../L1/dot.md) §Semantics, `:45,:49`).

## L0 form (RHS)

The L1 reduction lowers into Palace's reduction family in three surface forms sharing the
same local-then-collective skeleton; the forms differ only in which leaf is invoked and
whether the MPI collective is present.

### Sub-pattern A — free-function template `linalg::Dot(comm, x, y)` (the canonical form)

    // Calculate the parallel inner product yᴴ x or yᵀ x.   // vector.hpp:246
    template <typename VecType>
    inline auto Dot(MPI_Comm comm, const VecType &x, const VecType &y)
    {
      auto dot = LocalDot(x, y);
      Mpi::GlobalSum(1, &dot, comm);
      return dot;
    }

The two-step the L1 signature hides, evaluated in order:

1. **`LocalDot(x, y)`** — the rank-local reduction. Real input dispatches to a single Hypre
   strided pass (`vector.cpp:665-672`, `hypre_SeqVectorInnerProd`); complex input dispatches
   to the four-real-dot lift (`vector.cpp:674-685`). The leaf computes `yᴴ x` — **arg-2
   conjugated** (see §"The conjugation asymmetry").
2. **`Mpi::GlobalSum(1, &dot, comm)`** — the collective. `Mpi::GlobalSum`
   (`communication.hpp:266-270`) delegates to `GlobalOp(len, buff, MPI_SUM, comm)`
   (`communication.hpp:246-249`), whose body is `MPI_Allreduce(MPI_IN_PLACE, buff, len, …,
   MPI_SUM, comm)`. The reduction is in-place and broadcast to all ranks. **Single-rank is in
   scope** (CLAUDE.md "Scope"), so this stage lowers to a local no-op (one rank, nothing to
   reduce), but it is structurally present and carries the bit-deterministic-reduction-order
   trade-off recorded for `dot`.

Justification kind: **structural** — the rewrite is the syntactic expansion of one pure L1
reduction into the L0 composition; the destination is the return register, not a buffer.

Citations:
- `palace/linalg/vector.hpp:246-253` — `Dot` template; comment `// Calculate the parallel
  inner product yᴴ x or yᵀ x` (`:246`); body `LocalDot(x, y)` + `Mpi::GlobalSum(1, &dot,
  comm)` (`:248-253`).
- `palace/linalg/vector.hpp:242-244` — `LocalDot` decls (real + complex) with comment
  `// Calculate the local inner product yᴴ x or yᵀ x`.
- `palace/utils/communication.hpp:266-270` — `Mpi::GlobalSum(len, buff, comm)` →
  `GlobalOp(len, buff, MPI_SUM, comm)`.
- `palace/utils/communication.hpp:246-249` — `GlobalOp` body `MPI_Allreduce(MPI_IN_PLACE,
  buff, len, mpi::DataType<T>(), op, comm)`.

### Sub-pattern B — method-form `(*this).Dot(y)` (complex, no MPI)

    std::complex<double> ComplexVector::Dot(const ComplexVector &y) const
    {
      return {(Real() * y.Real()) + (Imag() * y.Imag()),
              (this == &y) ? 0.0 : ((Imag() * y.Real()) - (Real() * y.Imag()))};
    }

The complex rank-local kernel, with `*this = x`. It returns `{Re(x)Re(y)+Im(x)Im(y),
Im(x)Re(y)−Re(x)Im(y)} = x·conj(y) = yᴴ x` — the receiver `*this` is the **linear** operand,
the call argument `y` is the **conjugated** one. No MPI collective (rank-local method). At L1
this is the same `dot` operator: the single-rank specialisation of sub-pattern A with the
collective elided and the leaf fixed. The `operator*` alias (`vector.hpp:113`) forwards to
`Dot`. The `this == &y` branch is the transparent self-dot fast path (imag = `0.0` exactly,
since `xᴴ x` is real).

The unconjugated co-defined variant is the method `ComplexVector::TransposeDot`
(`vector.cpp:269-274`): same real part, **negated** imaginary cross-term (`Im(x)Re(y) +
Re(x)Im(y)`), `this==&y` returning `2·Im·Re`. It is the L0 surface for the L1 `tdot`. It has
**zero call sites** in the Palace tree (see §Variant axes).

Justification kind: **structural** — same reduction, MPI collective elided under single-rank;
plus the value-level conjugate-pair identity for the convention reconciliation.

Citations:
- `palace/linalg/vector.cpp:263-267` — `ComplexVector::Dot` body = `x·conj(y) = yᴴ x` with
  the `this==&y` imag = `0.0` self-dot fast path (`:266`).
- `palace/linalg/vector.cpp:269-274` — `ComplexVector::TransposeDot` body = unconjugated
  bilinear, negated imag cross-term, `this==&y` returns `2·Im·Re` (`:272-273`).
- `palace/linalg/vector.hpp:110-113` — declarations + comment `// Vector dot product (yᴴ x)
  or indefinite dot product (yᵀ x) for complex vectors.`; `operator*` aliased to `Dot`.

### Sub-pattern C — real leaf `LocalDot(Vector, Vector)` / `mfem::Vector::operator*` (real)

    double LocalDot(const Vector &x, const Vector &y)
    {
      static hypre::HypreVector X, Y;
      MFEM_ASSERT(x.Size() == y.Size(), "Size mismatch for vector inner product!");
      X.Update(x);  Y.Update(y);
      return hypre_SeqVectorInnerProd(X, Y);
    }

The real rank-local leaf: one Hypre `hypre_SeqVectorInnerProd` strided pass, with the
aligned-pass precondition `MFEM_ASSERT(x.Size() == y.Size())` (`:668`). Conjugation is a no-op
for real element type, so `dot` and `tdot` collapse to the same `Σ x[i]·y[i]` here and there
is no receiver-vs-argument asymmetry. The MFEM `mfem::Vector::operator*` is the
test-exercised surface (`mfem::Vector::operator*` is upstream MFEM, not Palace source; cited
only as the surface form Palace's tests exercise).

Justification kind: **structural** — single Hypre strided reduction; the real path of the same
operator.

Citations:
- `palace/linalg/vector.cpp:665-672` — `LocalDot(Vector, Vector)` via
  `hypre_SeqVectorInnerProd`, with `MFEM_ASSERT(x.Size()==y.Size())` at `:668`.
- `palace/linalg/vector.cpp:674-685` — `LocalDot(ComplexVector, ComplexVector)`: four real
  `LocalDot`s combined into `(Re, Im)`, `Im = LocalDot(xi,yr) − LocalDot(xr,yi)`, with the
  `&x==&y` self-dot fast path returning imag = `0.0` (`:678`).
- `test/unit/test-vector.cpp:206-207` — real-vector dot via `operator*`: `double dot = vec1 *
  vec2; CHECK_THAT(dot, WithinRel(32.0));` (`1·4 + 2·5 + 3·6 = 32`). Direct evidence the real
  form returns `double`. L0-equivalent semantic documentation (CLAUDE.md "Tests as semantic
  supplement").

## The conjugation asymmetry — the core theme content

Resolves OQ `l1-l0-dot-lowering-asymmetry`. The L1 `dot` convention pins **arg-1 conjugated**
(`xᴴ y`, [`L1/dot`](../L1/dot.md):43); every L0 surface form pins **arg-2 conjugated**
(`yᴴ x`). The two are complex conjugates:

    xᴴ y = conj( yᴴ x )

**Where the L0 surface conjugates arg-2 (verified — docs and bodies agree, no
Palace-internal contradiction):**

- Doc strings: `palace/linalg/vector.hpp:110` (method, `// Vector dot product (yᴴ x) …`),
  `:242` (`LocalDot`, `// … local inner product yᴴ x or yᵀ x`), `:246` (free function,
  `// … parallel inner product yᴴ x or yᵀ x`).
- Kernel bodies **agree** with the docs. `ComplexVector::Dot(y)` (`vector.cpp:263-267`)
  returns `{Re(x)Re(y)+Im(x)Im(y), Im(x)Re(y)−Re(x)Im(y)} = x·conj(y) = yᴴ x` — arg-2 `y`
  conjugated. The complex `LocalDot` (`vector.cpp:674-685`) has the same arg-2-conjugated
  `Im = LocalDot(xi,yr) − LocalDot(xr,yi)` sign.

So the asymmetry is **between** Palace's `yᴴ x` and the L1 representation's `xᴴ y`, **not
within** Palace. At L1 the asymmetry between method-form (`receiver.Dot(arg) = argᴴ·receiver`)
and free-function-form is *erased* — the L1 signature names the conjugated argument first
([`L1/dot`](../L1/dot.md):43).

**The lowering's re-order rule.** `linalg::Dot(comm, a, b)` computes `bᴴ a` (arg-2
conjugated). To obtain the L1 form `dot(x, y) = xᴴ y` the lowering calls **either**:

    dot(x, y)  =  xᴴ y  =  linalg::Dot(comm, y, x)          -- operand-swap form (arg-2 = x, conjugated)
                        =  conj( linalg::Dot(comm, x, y) )   -- outer-conj form

**Where the re-order is invisible (and why the two conventions coexist harmlessly).**
Consumers that take a **real projection** — `std::real`, `std::abs` — see no difference, since
`Re(z) = Re(conj z)` and `|z| = |conj z|`. The live witnesses:

- CG's `β = ⟨r, z⟩` for SPD `B` (`palace/linalg/iterative.cpp:395`, `beta = linalg::Dot(comm,
  z, r)`): the coefficient is consumed in a real-arithmetic update; the SPD form is exactly
  real (L1 dot law 9), so `zᴴ r` and `rᴴ z` agree on the real value. (Sibling CG/GMRES sites
  `iterative.cpp:404,444,460` are the same pattern.)
- Norms via `std::abs(linalg::Dot(...))` (`palace/linalg/nleps.cpp:487`) and
  `Norml2(comm, x) = √|Dot(comm, x, x)|` (`palace/linalg/vector.hpp:256-260`, the diagonal
  `y = x` case): the magnitude is convention-blind.

**Where it is observable.** Off-diagonal complex uses that consume the **full complex value**
(not a projection) see the conjugate; the lowering must then emit the operand-swap form to
stay faithful to the L1 `xᴴ y`.

This is the same conjugate-pair relationship the cycle-019
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) theme
narrated at the **L2>L1** edge (§"The conjugate-pair re-order"); this L1>L0 theme is the
**L1-leaf-level** lowering of the same fact. The two are cited together for consistency — the
L2>L1 theme dispatches the L2 fold onto the L1 leaf, this theme lowers the L1 leaf onto the L0
source.

## Reduction tree — load-bearing-numerical recording

Reduction-tree non-associativity is **load-bearing** ([`L1/dot`](../L1/dot.md) §Semantics,
`:45`): floating-point summation is non-associative, so different reduction trees give
different bit-level results. Bit-identical reproduction of a specific Palace call requires
matching that call's pinned tree, not merely the value:

| lowered call | L0 body (verified) | pinned reduction tree |
|---|---|---|
| `dot(x, y)`, real | `vector.cpp:665-672` | single Hypre `hypre_SeqVectorInnerProd` strided pass over `N` |
| `dot(x, y)`, complex | `vector.cpp:674-685` | four real Hypre passes combined into `(Re, Im)` by scalar `±`; `Im` cross-term sign `−` (Hermitian) |
| `tdot(x, y)`, complex | `vector.cpp:269-274` (member) | same four-real-dot decomposition with `Im` cross-term sign `+` |
| any (multi-rank) | `vector.hpp:248-253` | the per-rank kernel **then** the `Mpi::GlobalSum` MPI tree-reduce (folded out under single-rank scope, but the second pinned layer in a multi-rank build) |

(Same discipline as
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
§"Summation-order recording" and [`L1/dot`](../L1/dot.md) §Semantics.)

## Applicability conditions

The rewrite preserves semantics when:

1. **Read-only `x`, `y`.** `dot` never writes either argument; the L0 chain only reads them
   (the `LocalDot` leaf takes `const VecType &`). No aliasing or destination-buffer concern
   arises (there is no destination buffer — the result is a returned scalar). This is the
   structurally simplest BLAS-1 lowering: no in-place-mutation applicability conditions.
2. **Shared length axis (the aligned-pass precondition).** `x, y : Tensor[N]`; Palace enforces
   it with `MFEM_ASSERT(x.Size() == y.Size())` (`palace/linalg/vector.cpp:668`).
3. **Conjugation key matches the algorithm's intent.** Selecting `dot` (Hermitian) vs `tdot`
   (unconjugated) is value-bearing for complex element type — the leaves have different laws
   (`dot` PSD-at-diagonal, `tdot` not, [`L1/dot`](../L1/dot.md) laws 9 vs 13). Real element
   type makes the conjugation a no-op (sub-pattern C). The lowering is not a free choice.
4. **Single-rank reading of the collective.** The `MPI_Allreduce` stage is read as a local
   no-op under the in-scope single-machine target (CLAUDE.md "Scope"); multi-rank
   bit-determinism is the same caveat as for any reduction and is out of scope.
5. **The conjugate-pair re-order is observable for full-complex-value uses.** For a lowered
   call whose result is consumed as a real projection (`std::real` / `std::abs`), the re-order
   is invisible and the direct `linalg::Dot(comm, x, y)` suffices. For a call whose full
   complex value is consumed, the lowering must emit the operand-swap form
   `linalg::Dot(comm, y, x)` (or `conj(linalg::Dot(comm, x, y))`) to recover the L1 `xᴴ y`.

## Justification kind

- **Sub-pattern A** — `structural`. Expand one pure L1 reduction into the L0
  `Mpi::GlobalSum ∘ LocalDot` two-step; destination is the return register.
- **Sub-pattern B** — `structural` (+ the value-level conjugate-pair identity for the
  convention reconciliation). Same reduction, MPI collective elided under single-rank.
- **Sub-pattern C** — `structural`. Single Hypre strided reduction, the real path.

The theme as a whole is `structural` — the rewrite is the syntactic expansion of the L1
reduction into the L0 composition. The one non-syntactic ingredient is the value-level
algebraic identity `xᴴ y = conj(yᴴ x)`, read straight off the verified `ComplexVector::Dot`
body (`vector.cpp:263-267`); it reconciles the L1/L0 convention handedness but does not change
the structural character of the lowering. The four-real-dot fused complex kernel and the Hypre
strided pass are transparent-performance tricks nested inside the leaf; the per-call
reduction-tree split is the load-bearing residue recorded above.

## Speculative L1 operators

**None.** This theme lowers the already-firm L1 [`dot`](../L1/dot.md) operator (which
co-defines `dot` + `tdot`); it proposes no new L1 vocabulary. The M-weighted relative
`linalg::Dot(comm, x, A, y) = yᴴ A x` (`palace/linalg/operator.cpp:621-638`) shares the L0
symbol via overloading but is a **different operator** with a different L1 referent
(`bilinear-form`, rough-in) — it requires the operator-application primitive and a workspace
`Ax`, and is the subject of a separate forthcoming theme. It is named here only to mark the
boundary; it is **not** part of this theme.

## Verified-against

L0 evidence ranges (self-verified via `palace-codemap` read_range / search_text this
invocation — producer-citation self-verification, `verify-citation-range`):

- `palace/linalg/vector.cpp:263-267` — `ComplexVector::Dot` body `{Re(x)Re(y)+Im(x)Im(y),
  Im(x)Re(y)−Re(x)Im(y)} = x·conj(y) = yᴴ x` with `this==&y` imag = `0.0` fast path (`:266`).
  The arg-2-conjugated Palace convention + the conjugate-pair re-order source. **Self-verified.**
- `palace/linalg/vector.cpp:269-274` — `ComplexVector::TransposeDot` body: negated imag
  cross-term, `this==&y` returns `2·Im·Re` (`:272-273`). The unconjugated `tdot` kernel.
  **Self-verified.**
- `palace/linalg/vector.cpp:665-672` — `LocalDot(Vector, Vector)` via single Hypre
  `hypre_SeqVectorInnerProd`, `MFEM_ASSERT(x.Size()==y.Size())` at `:668`. The real leaf + the
  shape precondition. **Self-verified.**
- `palace/linalg/vector.cpp:674-685` — `LocalDot(ComplexVector, ComplexVector)`: four real
  `LocalDot`s combined into `(Re, Im)`, `Im = LocalDot(xi,yr) − LocalDot(xr,yi)`, with `&x==&y`
  self-dot fast path returning imag = `0.0` (`:678`). The complex leaf + the conjugation
  cross-term sign. **Self-verified.**
- `palace/linalg/vector.hpp:110-113` — method-form decls + comment `// Vector dot product
  (yᴴ x) or indefinite dot product (yᵀ x) for complex vectors.`; `operator*` aliased to `Dot`.
  **Self-verified.**
- `palace/linalg/vector.hpp:242-244` — `LocalDot` decls (real + complex) + comment
  `// Calculate the local inner product yᴴ x or yᵀ x`. **Self-verified.**
- `palace/linalg/vector.hpp:246-253` — `Dot` template; comment `// Calculate the parallel
  inner product yᴴ x or yᵀ x` (`:246`); body `auto dot = LocalDot(x, y); Mpi::GlobalSum(1,
  &dot, comm); return dot;` (`:248-253`). The documented arg-2 convention + the
  local-then-collective two-step. **Self-verified.**
- `palace/utils/communication.hpp:266-270` — `Mpi::GlobalSum(len, buff, comm)` →
  `GlobalOp(len, buff, MPI_SUM, comm)`. **Self-verified.**
- `palace/utils/communication.hpp:246-249` — `GlobalOp` body `MPI_Allreduce(MPI_IN_PLACE,
  buff, len, mpi::DataType<T>(), op, comm)`. **Self-verified.**
- `palace/linalg/iterative.cpp:395` — `beta = linalg::Dot(comm, z, r)`: CG's preconditioned
  `(Br, r)` coefficient — the workhorse Hermitian-member live call site consumed in real
  arithmetic (the re-order-invisible case). Sibling sites `:404,:444,:460`. **Self-verified.**
- `test/unit/test-vector.cpp:206-207` — `double dot = vec1 * vec2; CHECK_THAT(dot,
  WithinRel(32.0));` (`1·4 + 2·5 + 3·6 = 32`). Real form returns `double`. **Self-verified.**
- `search_text TransposeDot` over `palace/**/*.cpp` → exactly one hit (`vector.cpp:269`, the
  definition); the only other surface mention is the declaration `vector.hpp:112`. Confirms
  `tdot`'s zero call sites. **Self-verified.**

L1 / cross-theme anchors:

- `book/src/L1/dot.md` — the firm L1 operator this theme lowers: `dot`/`tdot` element-type
  table (`:33-35`), arg-1-conjugated convention (`:43`), self-dot trick (`:49`), variant axes
  (`:89-96`).
- `book/src/L2-L1/inner-product-fold-specialization.md` — the cycle-019 firm sibling that
  narrates the same conjugate-pair re-order at the L2>L1 edge (§"The conjugate-pair re-order");
  cited for consistency. This theme is the L1-leaf-level lowering of that fact.
- `book/src/L1-L0/nrm2-mutation-rotation.md` — the firm sibling whose lowering inherits this
  `Dot`-collective sub-theme (`nrm2 = √∘abs∘dot`).

## Variant axes

`dot` has two orthogonal variant axes at the L1>L0 edge (per `classify-variant-axis`):

- **element-type**: `real` | `complex`. At L0 these are separate leaves: real via
  `mfem::Vector::operator*` / `LocalDot(Vector, Vector)` (`vector.cpp:665-672`, sub-pattern
  C); complex via `ComplexVector::Dot` (`vector.cpp:263-267`, sub-pattern B) and
  `LocalDot(ComplexVector, ComplexVector)` (`vector.cpp:674-685`). The surrounding collective
  chain (sub-pattern A) is element-type-agnostic.
- **conjugation convention** (complex element-type only): `hermitian` (the default `dot` —
  `ComplexVector::Dot`) | `unconjugated` (`tdot` — `ComplexVector::TransposeDot`). The two L0
  kernels differ only in the sign of the imaginary cross-term. **`tdot` is
  type-API-surface-only**: `ComplexVector::TransposeDot` has **zero call sites** in the Palace
  tree (`search_text TransposeDot` over `palace/**/*.cpp` returns only the definition
  `vector.cpp:269`; declaration `vector.hpp:112`). The unconjugated arm is therefore
  structurally firm (a defined kernel differing from `dot` by one sign) but behaviorally
  unexercised; the theme's behavioral weight rests on the `dot` (Hermitian) arm (CG /
  orthogonalization / NLEPS sites). This mirrors the `tdot` note in
  [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
  §"Speculative L1 operators".

No other variant axes — the reduction is unconditionally exhaustive over the length axis `N`,
with no masking or strided variants in the Palace surface.

## Status

`firm` — the rewrite is the structural expansion of the L1 `dot` reduction into the L0
`Mpi::GlobalSum ∘ LocalDot` two-step, exhaustively pinned by direct, self-verified evidence
(the `Dot` template body `vector.hpp:248-253`, the complex kernel `vector.cpp:263-267`, the
real / complex leaves `vector.cpp:665-672` / `:674-685`, the collective
`communication.hpp:246-249,266-270`). The three surface forms (A free-function, B method, C
real leaf), the variant-axis collapse, and the conjugate-pair re-order are all directly cited
with live call-site witnesses for the re-order-invisible case (CG `iterative.cpp:395`). The
conjugation asymmetry is a positively-anchored value-level identity (`xᴴ y = conj(yᴴ x)`, read
straight off the verified `ComplexVector::Dot` body) — no negative-anchor reconstruction, no
literature inference, no speculative operator — so `firm` rather than `partly-constructive`.
The `tdot` type-API-surface-only note is a member-level evidentiary caveat (the dispatch
structure is firm; only the unconjugated arm is behaviorally unexercised), not a status
reduction. A `lowering-verifier` audit attaching the `verified_against:` block (per the
sibling-theme convention) confirming the surface-form recognition is exhaustive is the standard
follow-up, not a status reduction.
```

```edit:book/src/L1-L0/index.md
| [nrm2-mutation-rotation](./nrm2-mutation-rotation.md) | `L1/nrm2` (firm) | `palace/linalg/vector.hpp`, `palace/utils/communication.hpp`, `palace/fem/errorindicator.hpp` | firm *(structural; 3 surface forms; abs-guard classified load-bearing defensive)* |
| [dot-mutation-rotation](./dot-mutation-rotation.md) | `L1/dot` (firm) | `palace/linalg/vector.{hpp,cpp}`, `palace/utils/communication.hpp` | firm *(structural; 3 surface forms; conjugate-pair re-order `xᴴ y = conj(yᴴ x)`; tdot type-API-surface-only)* |
```

De-stub the existing SUMMARY row (the `(stub)` annotation is dropped now the chapter is firm).

```edit:book/src/SUMMARY.md
- [dot-mutation-rotation](./L1-L0/dot-mutation-rotation.md)
```

(Existing line at SUMMARY.md ~:82 reads `- [dot-mutation-rotation (stub)](./L1-L0/dot-mutation-rotation.md)`; the change is to drop the ` (stub)` suffix — the path is unchanged.)

## Speculative operators proposed

**None.** This theme lowers the already-firm L1 `dot` operator (which co-defines `dot` +
`tdot`); both RHS leaves are existing vocabulary. No new L1 vocabulary is introduced, so there
is nothing for the harvester to promote from this theme.

## Supporting evidence

All L0 ranges self-verified this invocation (see §Verified-against in the proposed chapter).
Key load-bearing citations:

- `palace/linalg/vector.cpp:263-267` — `ComplexVector::Dot` body = `yᴴ x` (arg-2 conjugated);
  the conjugate-pair re-order source.
- `palace/linalg/vector.hpp:246-253` — `linalg::Dot` template = `Mpi::GlobalSum ∘ LocalDot`;
  the local-then-collective two-step the L1 signature hides; doc comment `yᴴ x` at `:246`.
- `palace/utils/communication.hpp:246-249` — `MPI_Allreduce(MPI_IN_PLACE, …, MPI_SUM, comm)`.
- `palace/linalg/iterative.cpp:395` — CG `beta = linalg::Dot(comm, z, r)`, the re-order-invisible
  live witness.
- `search_text TransposeDot` over `palace/**/*.cpp` → only the definition `vector.cpp:269`;
  `tdot` has zero call sites.

## Open questions

- **Resolved by this theme: OQ `l1-l0-dot-lowering-asymmetry`.** The conjugation asymmetry
  (Palace L0 `yᴴ x` vs L1 `xᴴ y`) and the MPI-collective two-step are both narrated in the
  firm chapter. Recommend the integrator **close/migrate** this OQ — the deliverables it named
  are landed. (The bit-determinism half is tracked separately under
  `dot-reduction-tree-determinism-survey`, deferred — see below.)

- **Lifting note (reverse direction; working-notes only, NOT in the high→low chapter body).**
  Lifting the L0 `linalg::Dot` call *up* to the L1 `dot` operator is determinate: the L0 call
  IS the L1 reduction with the collective folded in and the convention re-handed. The lift
  loses (a) the pinned reduction tree (the L1 form records non-associativity as a claim, not a
  specific tree) and (b) the L0 arg-order/conjugation handedness (the L1 form pins arg-1). So
  the lift is value-faithful but NOT bit-faithful and NOT handedness-faithful — re-lowering
  recovers the original Palace call only if the reduction tree AND the operand-swap/outer-conj
  re-order are re-applied. This reverse-direction note lives here in working notes per the
  high→low layer-definition discipline; the formal chapter narrates only L1 → L0.

- **Caller-audit follow-up (deferred, not blocking).** A full audit classifying every
  `linalg::Dot` complex call site as "real-projected (re-order invisible)" vs "full-complex
  (re-order observable)" would tighten the re-order story to per-site precision. The cycle-019
  `inner-product-fold-specialization` theme already surfaced two M-weighted witnesses
  (`boundarymodeoperator.cpp:85` invisible, `:90` observable); a `same-layer-cross-cutter` /
  `lowering-verifier` pass extending that classification to the plain-`dot` sites is the
  natural follow-up. Deferred; relatedly OQ `dot-reduction-tree-determinism-survey` covers the
  bit-determinism half.

- **`tdot` type-API-surface-only (member-level caveat, not a status reduction).** Carried into
  the chapter §Variant axes: `ComplexVector::TransposeDot` has zero Palace call sites
  (definition + declaration only, verified). The dispatch *structure* is firm and the `dot`
  arm is behaviorally exercised; only the `tdot` arm's behavioral weight is API-only. No new OQ
  — this mirrors the existing note in `inner-product-fold-specialization` and `L1/dot`.

- **Lowering-verifier audit (standard follow-up).** A later `lowering-verifier` pass should
  attach the `verified_against:` block (per the axpby/nrm2 convention) confirming the three
  surface-form recognition is exhaustive (no un-cited fourth `Dot` overload missed) and the
  reduction-tree table matches the L0 bodies. Not a status reduction — the theme is firm.

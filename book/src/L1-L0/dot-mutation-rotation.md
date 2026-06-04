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

### Sub-pattern D — hook-routed `LocalDot` + batched `Mpi::GlobalSum` (the unfused form)

    // orthog.hpp:29-36 — the canonical InnerProductHelper
    struct IdentityInnerProduct {
      template <typename VecType>
      auto operator()(const VecType &x, const VecType &y) const { return LocalDot(x, y); }
    };
    // orthog.hpp:66-70 — CGS open-codes the two-step with a BATCHED collective
    for (std::size_t j = 0; j < m; j++) { H[j] = dot_op(w, V[j]); }   // m local dots
    Mpi::GlobalSum(m, H, comm);                                       // ONE size-m reduction

Palace's Gram-Schmidt routines (`OrthogonalizeColumnMGS` / `OrthogonalizeColumnCGS`,
`orthog.hpp`) do NOT call the fused `linalg::Dot` (Sub-pattern A). They reach the same
`yᴴ x` reduction through the `InnerProductHelper` template hook, whose canonical
`IdentityInnerProduct::operator()` returns `LocalDot(x, y)` (`orthog.hpp:35`), and the
routine itself applies `Mpi::GlobalSum` over the coefficient buffer. This is the **unfused**
realization of Sub-pattern A's `Mpi::GlobalSum ∘ LocalDot`: the local dot and the collective
are split across the hook boundary so MGS can interleave `w.Add(-H[j], V[j])` per `j`
(`:49-51`, `m` size-1 reductions) and CGS can **batch** the collective into one
`Mpi::GlobalSum(m, H, comm)` across all `m` coefficients (`:68-70`, 1 size-`m` reduction;
CGS2 = two such passes, `:75-88`). Value-identical to Sub-pattern A modulo the reduction-tree
non-law; the batching is the transparent collective-shape trick that motivates the
`L1/orthogonalize` `gs_orthog` variant axis (`book/src/L1/orthogonalize.md:107-110,184-189`).

**Observability note.** Unlike the real-projected CG coefficients, the Gram-Schmidt `H[j]`
is consumed as a **full complex value** (the residual update `w.Add(-H[j], V[j])` and the
Hessenberg-column store), so this is an **unweighted observable** use of the arg-2-conj
convention — the header's own `// Note order is important for complex vectors`
(`orthog.hpp:48`) flags it. It is the first cited unweighted-observable `dot` use OUTSIDE
the SLEPc-NEP deflation cohort (the cycle-020 `linalg::Dot`-caller census,
`book/src/L2-L1/inner-product-fold-specialization.md:301-329`, found only `nleps.cpp` because
it scoped `linalg::Dot` callers and `orthog.hpp` bypasses `linalg::Dot`).

Justification kind: **structural** — the unfused two-step is the same expansion as
Sub-pattern A with the collective lifted out of the per-dot call and (in CGS) batched.

Citations:
- `palace/linalg/orthog.hpp:29-36` — `IdentityInnerProduct`; `return LocalDot(x, y)` at `:35`.
- `palace/linalg/orthog.hpp:46-52` — MGS per-`j` `H[j]=dot_op(w,V[j]); Mpi::GlobalSum(1,&H[j],comm); w.Add(-H[j],V[j])` (m size-1 collectives, interleaved).
- `palace/linalg/orthog.hpp:66-88` — CGS `m` local dots then ONE `Mpi::GlobalSum(m, H, comm)` (`:70`); CGS2 `refine` second pass `:75-88`.
- `palace/linalg/vector.cpp:665-685` — the `LocalDot` real (Hypre) / complex (four-real-dot, `yᴴ x`) kernels the hook resolves to.
- `palace/utils/communication.hpp:266-270` — `Mpi::GlobalSum(len, buff, comm) → GlobalOp(..., MPI_SUM, ...)`.

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
(`bilinear-form`, firm cycle-095) — it requires the operator-application primitive and a workspace
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

```yaml
verified_against:
  - citation: palace/linalg/orthog.hpp:35
    verdict: supports
    audited_at: 2026-05-29T105500Z
    note: IdentityInnerProduct::operator() body `return LocalDot(x, y);` confirmed at :35 (was miscited :34, the operator-body opening brace). Corrected in §Sub-pattern D lines 160 + 183.
  - citation: palace/linalg/orthog.hpp:48
    verdict: supports
    audited_at: 2026-05-29T105500Z
    note: "// Global inner product: Note order is important for complex vectors." re-confirmed at :48.
  - citation: palace/linalg/orthog.hpp:46-52
    verdict: supports
    audited_at: 2026-05-29T105500Z
    note: MGS per-j interleaved size-1 collective block re-confirmed (dot at :49, GlobalSum(1,...) at :50, Add at :51).
  - citation: palace/linalg/orthog.hpp:66-88
    verdict: supports
    audited_at: 2026-05-29T105500Z
    note: CGS m local dots then ONE Mpi::GlobalSum(m, H, comm) at :70; CGS2 refine second pass through :88.
```

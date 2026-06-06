# inner-product-fold-specialization

The conjugation-convention rotation for the BLAS-1 reduce-to-scalar inner-product cohort.
Lowers the L2 reduce-to-scalar fold `inner_product` (`book/src/L2/inner_product.md`,
firm) into its L1 leaf — [`dot`](../L1/dot.md) (Hermitian), the unconjugated `tdot`
(co-defined in [`dot`](../L1/dot.md)), or the M-weighted member realized by
[`bilinear-form`](../L1/bilinear-form.md) (`xᴴ M y`) — by **dispatching on the fold's
per-element kernel (conjugated vs unconjugated), its element type (real vs complex), and
its weight presence (`M = I` vs general / SPD `M`)**. Narrated forward: the one L2 fold
**re-fuses** downward into Palace's bounded family of distinct reduction call shapes
(`ComplexVector::Dot` / `TransposeDot`, the real-vs-complex `linalg::LocalDot`, the
weighted `linalg::Dot(comm, x, A, y)`), and this theme records which call shape each
dispatch selects, the **value-level conjugate-pair re-order** between the L1/L2 `xᴴ y`
convention and Palace's L0 `yᴴ x` form, and **the pinned reduction tree that shape
evaluates in** (the load-bearing-numerical content the L2 entry's IEEE-754 non-law
deferred here).

This is the sibling of [`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md):
that theme dispatches a reduce-to-`Tensor[N]` fold by **arity**; this one dispatches a
reduce-to-`Scalar` fold by **conjugation convention**. The two folds are deliberately not
merged (different result types, different homomorphisms — `inner_product`'s
`(length-concat, ++) → (Scalar, +)` collapses `N`, `linear_combination`'s
`(term-list-concat, ++) → (Tensor[N], +)` keeps `N`); see `book/src/L2/inner_product.md`
§"Sibling fold: linear_combination is not subsumed".

## Slug

`inner-product-fold-specialization`

## L2 form (LHS)

The L2 form is the reduce-to-scalar fold over two aligned tensors (`L2/inner_product`
§Signature), with the optional matrix weight pre-applied to arg-1:

```text
inner_product   :: (x: Tensor[(S: ...)], y: Tensor[S]) -> Scalar
inner_product_M :: (x: Tensor[(S: ...)], M: LinOp[(S: ...), (S: ...)], y: Tensor[S]) -> Scalar

inner_product   x y   = foldl (+) zero (zipWith kernel x y)   -- kernel per the table below
inner_product_M x M y = inner_product (apply_linop M x) y     -- weighted ≡ pre-apply M to arg-1
inner_product   x y   = inner_product_M x I y                 -- plain ≡ M = I
```

The fold is pure / out-of-place: it consumes `x`, `y` (and `M`) and produces a fresh
`Scalar`; there is no destination buffer (the L0 in-place destination is the return
register / a stack scalar). It is **order-agnostic for value** — in exact arithmetic the
result `Σᵢ kernel(xᵢ, yᵢ)` is invariant under permutation of the length axis and under any
reassociation of the accumulation — but **bit-identical reproduction of an L0 reduction
requires matching that reduction's pinned tree** (the IEEE-754 non-law; §"Summation-order
recording" below). The **conjugation-convention axis is the axis this single L2 operator
unifies** (`L2/inner_product` §"L2 vs L1 distinction"); the pinned convention is
arg-1-conjugated:

$$ \text{inner\_product}(x, y) = x^{\mathsf H} y = \textstyle\sum_{i} \overline{x_i}\, y_i,
\qquad \text{inner\_product\_M}(x, M, y) = x^{\mathsf H} M y . $$

The shape precondition `x, y : Tensor[(S: ...)]` (congruence over one shape group `S` of
arbitrary, unknown rank — named shape groups per
[`l4_calculus`](../design/l4_calculus.md) §1.2.1) is the aligned-pass precondition the L0
fused reduction kernels require; at the lowered flat call it reads concretely as a shared
length `N` (Palace's `MFEM_ASSERT(x.Size() == y.Size())`,
`palace/linalg/vector.cpp:668`).

## L1 form (RHS)

The L1 form is the **three distinct leaf primitives**, each mirroring one Palace L0
reduction surface. The conjugation axis lives at one chapter ([`dot`](../L1/dot.md), which
co-defines `dot` and `tdot`); the M-weighted member is the separate
[`bilinear-form`](../L1/bilinear-form.md) chapter. At this RHS the operands are the
**concrete Palace `Vector`s** — genuinely flat rank-1 dof-vectors of length `N` (and `M`
for `bilinear_form`'s domain) — so the `Tensor[N]` / `LinearOperator[M, N]` rendering here
is the literal L0/L1 call shape, NOT the shape-generic `(S: ...)` of the L2 fold above (the
rank-1-ness is real at the lowered call, not an accidental implication):

```text
dot           :: (x: Tensor[N], y: Tensor[N])                          -> Scalar
tdot          :: (x: Tensor[N], y: Tensor[N])                          -> Scalar   -- complex-only
bilinear_form :: (x: Tensor[M], M: LinearOperator[M, N], y: Tensor[N]) -> Scalar

dot(x, y)              = Σᵢ conj(x[i])·y[i]   -- Hermitian (complex) / symmetric (real)
tdot(x, y)             = Σᵢ x[i]·y[i]         -- unconjugated bilinear (complex)
bilinear_form(x, M, y) = xᴴ M y              -- M-weighted; ≡ dot(x, apply_linop(M, y)) as an unfolding
```

At L1 the conjugation value and the weight presence are **fixed per operator**: `dot` is
Hermitian, `tdot` is unconjugated, `bilinear-form` is M-weighted; each mirrors Palace's L0
reduction surface one-to-one (`dot` ← `ComplexVector::Dot` / real `LocalDot`; `tdot` ←
`ComplexVector::TransposeDot`; `bilinear-form` ← `linalg::Dot(comm, x, A, y)`). The
conjugation axis over which L1 has `dot`/`tdot` (and the weight axis over which it has
`dot` vs `bilinear-form`) is exactly the axis the single L2 fold unifies.

The L1 leaves adopt the **same arg-1-conjugated convention** as the L2 fold
([`dot`](../L1/dot.md) §Semantics, "conjugate-linear in the **first** argument", `:43`;
[`bilinear-form`](../L1/bilinear-form.md) §Signature, `bilinear_form(x, M, y) = xᴴ M y`,
`:63`), so the LHS→RHS dispatch is convention-preserving at the L1/L2 representation level;
the *value-level* re-order against the Palace L0 source is §"The conjugate-pair re-order"
below.

## The dispatch rewrite (L2 → L1)

The lowering reads the fold's three family axes and selects the matching L1 leaf. This is a
**resolution refinement plus a kernel-fusion choice**, not an algebraic transformation of
the value (`L2/inner_product` laws 3-7): each selected leaf computes the same value the
fold does (modulo the summation-order non-law below, and modulo the value-level
conjugate-pair re-order against the L0 source).

```text
inner_product   x y    with conjugated   kernel  ⇒  dot(x, y)             -- Hermitian (complex) / symmetric (real)
inner_product   x y    with unconjugated kernel  ⇒  tdot(x, y)            -- unconjugated bilinear (complex-only)
inner_product_M x M y                            ⇒  bilinear_form(x, M, y) -- M-weighted member
inner_product_M x I y                            ⇒  dot(x, y)             -- M = I collapses the weight (law 7)
```

The **selection rule** has three orthogonal dispatch keys, applied independently:

1. **Conjugation key** — the per-element kernel. `kernel = conj(x[i])·y[i]` selects the
   Hermitian leaf (`dot`); `kernel = x[i]·y[i]` selects the unconjugated leaf (`tdot`).
   This is the family's namesake axis. The ONLY per-element difference between the two L0
   kernels is the sign of the imaginary cross-term: `ComplexVector::Dot`
   (`palace/linalg/vector.cpp:263-267`) has `Im = Im(x)·Re(y) − Re(x)·Im(y)`;
   `ComplexVector::TransposeDot` (`palace/linalg/vector.cpp:269-274`) has the **negated**
   cross-term `Im = Im(x)·Re(y) + Re(x)·Im(y)`. Real element type makes the conjugation a
   no-op, so the real path collapses both kernels to `x[i]·y[i]` (one Hypre
   `hypre_SeqVectorInnerProd`, `palace/linalg/vector.cpp:664-672`).

2. **Element-type key** — `real | complex`. At L0 these are separate kernels: the real
   member is a single Hypre strided pass (`palace/linalg/vector.cpp:664-672`); the complex
   member is the **real fold lifted componentwise over `(Re, Im)`** — four real local dots
   combined into a `(Re, Im)` scalar (`palace/linalg/vector.cpp:674-685`):
   `Re = LocalDot(xr,yr) + LocalDot(xi,yi)`, `Im = LocalDot(xi,yr) − LocalDot(xr,yi)`. The
   element-type key is orthogonal to the conjugation key: the conjugation axis is exactly
   the sign of that `Im` cross-term (negate it and the complex leaf is `tdot`).

3. **Weight key** — `M = I` (plain, selects `dot`) vs general / SPD `M` (selects
   `bilinear_form`). The weighted leaf is the composition `inner_product (apply_linop M x) y`
   at L2; at L0 it is `linalg::Dot(comm, x, A, y)` (`palace/linalg/operator.cpp:621-638`),
   which open-codes that composition: allocate a workspace `Ax`, write `Ax = A·x`, then
   reduce `Dot(comm, Ax, y)`. The weight key is orthogonal to conjugation — the weighted
   member is itself conjugate-linear in its (M-applied) arg-1 — and orthogonal to element
   type (two L0 overloads differing only in the weight operator's element type:
   real-`Operator` weight `:621-628` splits `x` into Re/Im and applies `A` to each;
   `ComplexOperator` weight `:631-638` applies `A` to `x` directly).

### The weighted-member workspace (a lowering concern, not L2 algebra)

At L2 the weighted member is the clean composition `inner_product (apply_linop M x) y`
(`L2/inner_product` §Semantics). The lowering reintroduces the **internal workspace `Ax`**
that the L0 weighted `Dot` allocates (`ComplexVector Ax(A.Height())`,
`palace/linalg/operator.cpp:624,634`) — the Category-4 "synthetic workspace" instance of
[`mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md) recorded at
[`bilinear-form`](../L1/bilinear-form.md):39-43. The workspace disappears at L2 (pure
threading) and reappears here as the M-application buffer; it is invisible to the L2 value.

### The diagonal degeneration (`y = x`) — a consumer entry, not a dispatch key

When `y = x` the fold collapses to the norm-squared and triggers the `&x == &y` self-dot
fast path (transparent trick: `palace/linalg/vector.cpp:266` returns imag = `0.0` for the
Hermitian form; `:272-273` returns `2·Im·Re` for `tdot`; `:679` returns imag = `0.0` for
the complex local fold). The fast path is an L0 implementation detail the lowering elides
(algebraically `xᴴ x` is exactly real). The diagonal is the entry point for the
`nrm2` / `matrix-weighted-norm` consumers (`√ ∘ inner_product` at `y = x`,
`palace/linalg/operator.cpp:598-618`), which compose an outer `√` post-step — that
composition is downstream of this lowering, not a dispatch within it.

## The conjugate-pair re-order (the core theme content)

This is the headline value-level reconciliation the L2 entry hands to this theme (per the
cycle-019 `inner_product` harvester, dispatch #1 — `L2/inner_product` §"Conjugation
convention (pinned)", final paragraph; live once dispatch #1 integrates). The L1/L2
representation pins **arg-1 conjugated** (`xᴴ y`); the Palace L0 surface pins **arg-2
conjugated** (`yᴴ x`). The two are **complex conjugates of each other**:

$$ x^{\mathsf H} y = \overline{\,y^{\mathsf H} x\,}. $$

**Where the L0 surface conjugates arg-2 (verified):**

- Doc strings: `palace/linalg/vector.hpp:242,246` (`LocalDot` / free-function `Dot`,
  `// Calculate the … inner product yᴴ x or yᵀ x`); `palace/linalg/operator.hpp:386,391`
  (weighted, `// Compute the bilinear form inner product yᴴ A x`).
- Kernel bodies **agree with the docs** — there is **no Palace-internal contradiction**
  (contra an earlier framing; the contradiction is between Palace's `yᴴ x` and the L1
  representation's `xᴴ y`, not within Palace). `ComplexVector::Dot(y)`
  (`palace/linalg/vector.cpp:263-267`) returns `{Re(x)Re(y)+Im(x)Im(y),
  Im(x)Re(y)−Re(x)Im(y)} = x·conj(y) = yᴴ x` — arg-2 `y` is the conjugated operand. The
  complex local fold (`palace/linalg/vector.cpp:674-685`) has the same
  `Im = LocalDot(xi,yr) − LocalDot(xr,yi)` sign — arg-2 conjugated. The weighted
  free-function (`palace/linalg/operator.cpp:621-628`) builds `Ax = A·x` then returns
  `Dot(comm, Ax, y) = yᴴ(Ax) = yᴴ A x` — arg-2 `y` conjugated.

**The lowering's re-order rule.** The L2 fold `inner_product x y = xᴴ y` lowers to the L0
call by **either** swapping the operand positions **or** wrapping in an outer `conj`:

```text
inner_product x y  =  xᴴ y  =  conj( yᴴ x )  =  conj( linalg::Dot(comm, x, y) )   -- outer-conj form
                            =  yᵀ-conjugated   =  linalg::Dot(comm, y, x)          -- operand-swap form
```

i.e. `linalg::Dot(comm, a, b)` computes `bᴴ a` (arg-2 conjugated), so to obtain the L2
fold's `xᴴ y` the lowering calls **`linalg::Dot(comm, y, x)`** (operand swap: arg-2 becomes
`x`, conjugated, giving `xᴴ y`) or equivalently `conj(linalg::Dot(comm, x, y))`. For the
weighted member, Palace's own shape is `Dot(comm, A·x, y) = yᴴ A x`; recovering the L2
`xᴴ M y` requires the same swap/conj (and, for a Hermitian `M`, `yᴴ M x = conj(xᴴ M y)`,
so the outer `conj` recovers it; for non-Hermitian `M` the operand-swap form is the
faithful one). This is exactly the conjugation-asymmetry reconciliation
[`bilinear-form`](../L1/bilinear-form.md):119-145 records at L1.

**Where the re-order is invisible (and why the two conventions coexist harmlessly in
Palace).** Algorithms that take a **real projection** of the result — `std::real`,
`std::abs` — see no difference, because `Re(z) = Re(conj z)` and `|z| = |conj z|`. The
live witnesses:

- CG's `β = ⟨r, z⟩` for SPD `B` (`palace/linalg/iterative.cpp:395`,
  `beta = linalg::Dot(comm, z, r)`): the coefficient is used in a real-arithmetic update;
  the SPD form is exactly real (law 5), so `zᴴ r` and `rᴴ z` agree on the real value.
- Norms via `std::abs(linalg::Dot(...))` (`palace/linalg/nleps.cpp:487,492`) and
  `Norml2(comm, x) = √|Dot(comm, x, x)|` (`palace/linalg/vector.hpp:256-260`): the
  magnitude is convention-blind.
- Poynting power `Dot(comm, et, *Bttr, et)` at the diagonal
  (`palace/models/boundarymodeoperator.cpp:85`): diagonal `y = x` with Hermitian `Bttr`
  makes the form exactly real (law 5 / law 8).

**Where it is observable.** Off-diagonal complex uses that consume the **full complex
value** (not a projection) see the conjugate. The cross-coupling
`Dot(comm, en, Atn, et)` (`palace/models/boundarymodeoperator.cpp:90`, non-Hermitian
`Atn`) is the witness: `yᴴ A x ≠ conj(xᴴ A y)` in general, so the re-order is value-bearing
there and the lowering must apply the operand-swap form to stay faithful to the L2
`xᴴ M y`. This is the case where the re-order is genuine lowering work, not a no-op.

## Summation-order recording

This is the **load-bearing-numerical content the L2 entry defers to this theme** (per the
cycle-019 `inner_product` harvester, dispatch #1 — `L2/inner_product` §"Algebraic laws",
the IEEE-754 reduction-tree non-law: "Which tree a given lowered call pins is recorded by
the L2>L1 lowering theme"; live once dispatch #1 integrates). The L2 fold is
order-agnostic for *value*; **bit-identical reproduction of any L0 call requires matching
that call's pinned reduction tree.** The trees are read off the verified `vector.cpp` /
`operator.cpp` bodies (single-rank scope — the per-rank kernel; the MPI tree-reduce
`Mpi::GlobalSum`, `palace/linalg/vector.hpp:247-253`, is folded out per CLAUDE.md scope but
is the second pinned layer in a multi-rank build):

| lowered call | L0 body (verified) | pinned reduction tree |
|---|---|---|
| `dot(x, y)`, real | `vector.cpp:664-672` | single Hypre `hypre_SeqVectorInnerProd` strided pass over `N` (one accumulation order, Hypre-internal) |
| `dot(x, y)`, complex | `vector.cpp:674-685` | **four** real Hypre passes (`xr·yr`, `xi·yi`, `xi·yr`, `xr·yi`), each its own Hypre tree, combined into `(Re, Im)` by scalar `±`; the cross-term sign is `−` for `Im` (the Hermitian convention) |
| `tdot(x, y)`, complex | `vector.cpp:269-274` (member) | same four-real-dot decomposition as `dot` with the `Im` cross-term sign **`+`** — the only tree difference from `dot` is that one sign |
| `bilinear_form(x, M, y)` | `operator.cpp:621-628` (real-`A`) / `:631-638` (complex-`A`) | the M-application reduction (the operator's internal SpMV / quadrature tree) **then** the complex four-real-dot reduction of `Dot(comm, Ax, y)` — a **two-stage** pinned tree (the `Ax` workspace is the stage boundary) |

The complex and real trees do **NOT** agree bit-for-bit with a naive single-accumulator
fold: the complex member sums four independent Hypre reductions and combines them by scalar
arithmetic, so its rounding schedule differs from a hypothetical single
`Σ conj(x[i])·y[i]` complex accumulation. The weighted member adds a second non-associative
stage (the operator-apply reduction) ahead of the dot reduction. The canonical order this
theme names is the **L2 fold's `foldl` left-to-right order over the length axis**; a
downstream implementation reproducing a specific Palace call bit-for-bit must pin the tree
in this table (Hypre per-rank kernel + the four-real-dot combination + the M-apply stage),
not merely the value. (Same discipline as
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md)
§"Summation-order recording" and [`dot`](../L1/dot.md) §Semantics.)

## Applicability conditions

The dispatch lowering preserves the L2 value when:

1. **Shared shape group (the aligned-pass precondition).** `x, y : Tensor[(S: ...)]` (the L2
   signature precondition — congruence over one shape group `S`). At the lowered L0 call the
   operands are flat rank-1 `Vector`s, so this congruence is read concretely as a shared
   length `N`; the fused reduction kernels stride over that one flat axis and
   Palace enforces it with `MFEM_ASSERT(x.Size() == y.Size())`
   (`palace/linalg/vector.cpp:668`). For the weighted member, additionally `M`'s codomain
   matches `x`'s axis and `M`'s domain matches `y`'s axis
   ([`bilinear-form`](../L1/bilinear-form.md) §Applicability conditions).

2. **Conjugation key matches the algorithm's intent.** Selecting `dot` (Hermitian) vs
   `tdot` (unconjugated) is value-bearing for complex element type — the two leaves have
   **different laws** (`dot` is PSD-at-diagonal, `tdot` is not; `L2/inner_product` law 5
   vs the `tdot` non-PSD non-law). The lowering must select the leaf whose kernel matches
   the fold's pinned kernel; it is not a free choice.

3. **Element-type conformance.** Element type is one shared `T ∈ {real, complex}` inherited
   unchanged from the leaves; the lowering dispatches to the real Hypre kernel or the
   complex four-real-dot lift of the selected leaf.

4. **Value-preservation vs bit-reproduction (the standard split).** Each selected leaf
   computes the fold's value (modulo the conjugate-pair re-order against the L0 source —
   condition 5). Bit-reproduction of a *specific* Palace call additionally requires (a)
   pinning that call's reduction tree (the table in §"Summation-order recording") and (b)
   applying the operand-swap / outer-`conj` re-order. The lowering is valid under the
   **algorithmic-correctness** reading whenever conditions 1-3 hold; under the
   **bit-reproduction** reading only when the tree and the re-order are matched (the
   load-bearing-vs-transparent classification, CLAUDE.md "load-bearing numerical tricks …
   non-associative reduction orderings … preserve as explicit algebraic claims").

5. **The conjugate-pair re-order is observable for full-complex-value uses.** For a lowered
   call whose result is consumed as a **real projection** (`std::real` / `std::abs`), the
   re-order is invisible and the direct `linalg::Dot(comm, x, y)` suffices. For a call whose
   **full complex value** is consumed (off-diagonal, non-Hermitian, as
   `boundarymodeoperator.cpp:90`), the lowering must emit the operand-swap form
   `linalg::Dot(comm, y, x)` (or `conj(linalg::Dot(comm, x, y))`) to recover the L2 `xᴴ y`.

   **Caller-site conjugation inventory** (every `linalg::Dot` caller across `palace/linalg/`
   and `palace/fem/`, classified invisible/observable — cross-layer-cross-cutter census,
   2026-05-29, answering this theme's own §Open-questions caller-audit item). The convention
   is load-bearing in **exactly one algorithm**: the SLEPc-NEP deflated quasi-Newton in
   `nleps.cpp`, at the four unweighted observable sites below. These four are the bare-`dot`
   leaf's first cited **unweighted** observable witnesses (until now Condition 5's sole cited
   observable site, `boundarymodeoperator.cpp:90`, was a *weighted* `bilinear_form` leaf).
   `palace/fem/` has **zero** `Dot` callers; every `iterative.cpp` CG/PCG coefficient and
   every `std::abs(·)`/`.real()` norm is invisible by real-projection.

```yaml
conjugation_caller_inventory:
  audited_at: 2026-05-29T034441Z
  by: cross-layer-cross-cutter
  scope: every linalg::Dot caller across palace/linalg/ and palace/fem/
  invisible_unweighted:
    - palace/linalg/iterative.cpp:395   # PCG (Br,r), CheckDot SPD-real + abs
    - palace/linalg/iterative.cpp:404   # PCG (Bb,b)
    - palace/linalg/iterative.cpp:444   # PCG (Ap,p), CheckDot SPD-real
    - palace/linalg/iterative.cpp:460   # PCG in-loop (Br,r)
    - palace/linalg/nleps.cpp:487       # std::abs self-norm
    - palace/linalg/nleps.cpp:492       # std::abs self-norm
    - palace/linalg/nleps.cpp:543       # std::abs self-norm
    - palace/linalg/nleps.cpp:696       # std::abs self-norm
    - palace/linalg/nleps.cpp:737       # std::abs self-norm
  invisible_weighted:
    - palace/linalg/operator.cpp:603    # real Norml2 B-weighted, dot>0 assert
    - palace/linalg/operator.cpp:615    # complex Norml2 B-weighted, SPD imag~0 assert + .real()
  observable_unweighted:               # bare dot leaf — convention load-bearing
    - palace/linalg/nleps.cpp:522       # deflation proj X[j]ᴴ x1 -> complex LU solve
    - palace/linalg/nleps.cpp:529       # deflation Gram X[j]ᴴ X[i] -> complex LU solve
    - palace/linalg/nleps.cpp:568       # residual deflation coords X[j]ᴴ vv -> Newton numerator via out-param u2
    - palace/linalg/nleps.cpp:675       # complex eigenvalue Newton ratio -(w0ᴴu + u2_w0)/(w0ᴴw); TWO Dot calls on this line
  observable_weighted:                 # bilinear_form leaf
    - palace/models/boundarymodeoperator.cpp:90   # ComplexWrapperOperator Atn non-Hermitian off-diagonal (wave-1 witness, models/)
  out_of_scope_observable_flagged:
    - palace/models/postoperator.cpp:1759,1760,1795,1796  # port V/I real+imag separately consumed (models/, not audited line-by-line here)
  finding: palace/fem/ has zero Dot callers; the only intra-linalg/ unweighted observable sites are the four nleps.cpp SLEPc-NEP deflation/Newton sites.
```

**Bypass surface (out of the `linalg::Dot`-caller scope, recorded for completeness).** Palace's
Gram-Schmidt routines (`palace/linalg/orthog.hpp`) reach the same unweighted `yᴴ x` reduction
WITHOUT calling `linalg::Dot`: the `InnerProductHelper` hook's `IdentityInnerProduct` calls
`LocalDot(x, y)` directly (`orthog.hpp:34`) and the routine applies `Mpi::GlobalSum` itself
(the unfused two-step; CGS batches it into one size-`m` reduction, `orthog.hpp:68-70`). The
coefficients `H[j]` are **unweighted observable** (consumed in the residual update
`w.Add(-H[j], V[j])`, header flag `// Note order is important for complex vectors` at
`orthog.hpp:48`) — the first unweighted-observable `dot` use outside the `nleps.cpp` deflation
cohort. This surface is enumerated as Sub-pattern D of
[`dot-mutation-rotation`](../L1-L0/dot-mutation-rotation.md); it is not in the
`conjugation_caller_inventory` above because that block is scoped to `linalg::Dot` call sites.

## Justification kind

`algebraic` — the dispatch rule **is** the L2 entry's already-firm laws read as a
lowering. Law 7 (the weighted-member specialization identities
`dot = inner_product_M x I y`, `bilinear_form = inner_product_M x M y`) gives the weight
dispatch directly; the conjugation key is the per-element kernel (the conjugation axis the
L2 fold unifies); the element-type key is the real-vs-complex kernel split (the complex =
real-fold-lifted-componentwise identity, `L2/inner_product` §Semantics). The
**conjugate-pair re-order** (`xᴴ y = conj(yᴴ x)`) is a value-level algebraic identity,
verified directly against the Palace `Dot` (`vector.cpp:263-267`), `TransposeDot`
(`vector.cpp:269-274`), and weighted-`Dot` (`operator.cpp:621-628`) bodies — it is the
core algebraic content of this theme, not an inference. A **reduction-chain** flavour is
present (the fold is a small-step left-fold over `N`), but the governing justification is
the algebraic kernel/weight specialization plus the conjugate-pair identity, so the theme
is classified `algebraic`. The fused reduction kernels (the single Hypre pass / the
four-real-dot lift) are transparent-performance tricks (`L2/inner_product` §"Fusion note")
nested inside each selected leaf; the per-call reduction-tree split is the load-bearing
residue recorded in §"Summation-order recording".

## Speculative L1 operators

**None.** All three RHS leaves are existing vocabulary:
[`dot`](../L1/dot.md) (firm; co-defines `dot` + `tdot`) and
[`bilinear-form`](../L1/bilinear-form.md) (firm, promoted cycle-095; the M-weighted member). The LHS
`L2/inner_product` is firm (harvested this cycle, dispatch #1). This theme proposes no new
operators — it is the lowering edge between existing vocabulary on both sides.

Two evidentiary caveats carry over from the leaves (neither is a status reduction on the
theme — the *dispatch structure* is firm):

- **`tdot` is type-API-surface-only.** `ComplexVector::TransposeDot` has **zero call
  sites** in the Palace tree — `search_text TransposeDot` over `palace/**` returns exactly
  the declaration (`palace/linalg/vector.hpp:112`) and the definition
  (`palace/linalg/vector.cpp:269`), no callers (verified this invocation). The unconjugated
  dispatch arm is therefore structurally firm (a defined kernel differing from `dot` by one
  sign) but behaviorally unexercised; the theme's behavioral weight leans on the `dot`
  (Hermitian — CG / orthogonalization / NLEPS sites) and `bilinear-form` (Poynting +
  cross-coupling sites) arms, both exercised. Mirrors `L2/inner_product` §"tdot".

- **`bilinear-form` is firm at L1** (promoted cycle-095 under the firm-on-positive-structure
  escape; its two surfaced use sites are both complex-`x`-complex-`y`). The M-weighted dispatch
  arm was always firm independent of the leaf's promotion: the arm's structure is firm (the
  composition `inner_product (apply_linop M x) y` lowering to `Dot(comm, A·x, y)` is clean and
  directly verified). The leaf is now firm at L1, strengthening — not gating — this theme.

## Verified-against

L0 evidence ranges (self-verified via `palace-codemap` read_range / search_text this
invocation — producer-citation-drift discipline, `verify-citation-range`
producer-self-verification):

- `palace/linalg/vector.cpp:263-267` — `ComplexVector::Dot` body:
  `{Re(x)Re(y)+Im(x)Im(y), Im(x)Re(y)−Re(x)Im(y)}` with `this==&y` imag=0 fast path
  (`:266`) = `x·conj(y) = yᴴ x`. The Hermitian kernel + the arg-2-conjugated Palace
  convention (the conjugation key + the conjugate-pair re-order source). **Self-verified.**
- `palace/linalg/vector.cpp:269-274` — `ComplexVector::TransposeDot` body: same real part,
  **negated** imaginary cross-term (`Im(x)Re(y) + Re(x)Im(y)`), `this==&y` returns
  `2·Im·Re` (`:272-273`). The unconjugated `tdot` kernel — differs from `Dot` only in the
  imag sign. **Self-verified.**
- `palace/linalg/vector.cpp:664-672` — `LocalDot(Vector, Vector)` via a single Hypre
  `hypre_SeqVectorInnerProd`, with `MFEM_ASSERT(x.Size()==y.Size())` at `:668`. The real
  member's fused kernel + the shape precondition. **Self-verified.**
- `palace/linalg/vector.cpp:674-685` — `LocalDot(ComplexVector, ComplexVector)`: four real
  `LocalDot`s combined into `(Re, Im)`, `Im = LocalDot(xi,yr) − LocalDot(xr,yi)`, with the
  `&x==&y` self-dot fast path returning imag=0 at `:679`. The element-type key (complex =
  real fold lifted) + the conjugation cross-term sign. **Self-verified.**
- `palace/linalg/vector.hpp:240-262` — `LocalDot` / free-function `Dot` decls with
  `// … inner product yᴴ x or yᵀ x` comments (`:242,:246`); the `Dot` template
  `= Mpi::GlobalSum ∘ LocalDot` (`:247-253`); `Norml2(comm,x) = √|Dot(comm,x,x)|`
  (`:256-260`). The documented arg-2 convention + the local-then-collective two-step + the
  norm consumer. **Self-verified.**
- `palace/linalg/operator.cpp:621-628` — weighted `Dot(comm, x, A, y)` real-`Operator`:
  allocates `ComplexVector Ax(A.Height())` (`:624`), `A.Mult(x.Real(), Ax.Real())` /
  `A.Mult(x.Imag(), Ax.Imag())`, then `Dot(comm, Ax, y) = yᴴ A x`. The M-weighted dispatch
  arm + the workspace + the arg-2-conjugated weighted form. **Self-verified.**
- `palace/linalg/operator.cpp:631-638` — weighted `Dot(comm, x, A, y)` `ComplexOperator`:
  `A.Mult(x, Ax)` then `Dot(comm, Ax, y)`. The element-type-of-weight sibling overload.
  **Self-verified.**
- `palace/linalg/operator.cpp:598-618` — `Norml2(comm, x, B, Bx)` real (`:599-606`) +
  complex (`:608-618`): the B-weighted norm `√ Dot(comm, Bx, x)`, with the SPD assertion
  `dot.real() > 0.0 && |dot.imag()| < 1e-9·dot.real()` (`:616`, comment "For SPD B,
  xᴴ B x is real" at `:612`). The `matrix-weighted-norm` consumer + law-5/diagonal
  confirmation. **Self-verified.**
- `palace/linalg/iterative.cpp:393-396` — `beta = linalg::Dot(comm, z, r)` (`:395`): CG's
  preconditioned `(Br, r)` coefficient — the workhorse Hermitian-member live call site
  consumed in real arithmetic (the re-order-invisible case). **Self-verified.**
- `palace/models/boundarymodeoperator.cpp:83-91` — `linalg::Dot(comm, et, *Bttr, et)`
  (`:85`, Poynting power, M-weighted diagonal, Hermitian → real, re-order invisible);
  `linalg::Dot(comm, en, Atn, et)` (`:90`, cross-coupling, M-weighted off-diagonal,
  non-Hermitian `Atn` → full complex value, **re-order observable**). The two live
  M-weighted call sites + the observable-re-order witness. **Self-verified.**
- `search_text TransposeDot` over `palace/**` → exactly two hits (`vector.hpp:112` decl,
  `vector.cpp:269` def). Confirms `tdot`'s zero call sites. **Self-verified.**

L2 / L1 anchors:

- `book/src/L2/inner_product.md` — the L2 reduce-to-scalar fold (LHS). Per the cycle-019
  `inner_product` harvester (dispatch #1, sibling report
  `reports/2026-05-29T024500Z-harvester-inner-product-l2/CYCLE.md`), it pins the
  arg-1 conjugation convention, laws 3-7 + the IEEE non-law, and the four hand-offs
  (a)-(d) — which are this theme's dispatch rule, re-order rule, and summation-order
  deferral. (The link target **already exists on disk as a `stub`** today, so
  `(../L2/inner_product.md)` resolves at build now; dispatch #1 flips it stub → firm —
  it does not create it. The firm-content attributions above are confirmable once
  dispatch #1 integrates, which the wave-2 serial sequencing applies before this theme.)
- `book/src/L1/dot.md` — the firm Hermitian / unconjugated leaf (RHS): `dot` (`:33-34`),
  `tdot` (`:35`), the arg-1-conjugated L1 convention (`:43-44`), the self-dot trick
  (`:49`).
- `book/src/L1/bilinear-form.md` — the firm M-weighted leaf (RHS): `xᴴ M y` (`:63`),
  the conjugation-asymmetry reconciliation (`:119-145`), the workspace `Ax` (`:39-43`).

## Status

`firm` — the L2 LHS is firm (harvested this cycle, dispatch #1), the L1 RHS leaves are
existing vocabulary (`dot`/`tdot` firm; `bilinear-form` firm (cycle-095) and its M-weighted-member
dispatch arm is firm), and the dispatch rule IS the L2 entry's already-firm laws (law 7
weight specialization + the conjugation/element-type kernel keys) read as a lowering. The
**conjugate-pair re-order** (`xᴴ y = conj(yᴴ x)`) and the per-call reduction trees are read
straight off the **verified** Palace bodies (`Dot` `vector.cpp:263-267`; `TransposeDot`
`vector.cpp:269-274`; real / complex `LocalDot` `vector.cpp:664-685`; weighted `Dot`
`operator.cpp:621-638`), with live call-site witnesses for both the re-order-invisible case
(CG `iterative.cpp:395`, Poynting diagonal `boundarymodeoperator.cpp:85`) and the
re-order-observable case (cross-coupling `boundarymodeoperator.cpp:90`). No literature
inference, no negative-anchor reconstruction, no speculative operator. This is the third
chapter under the `book/src/L2-L1/` Part (after
[`chebyshev-iteration-fusion`](./chebyshev-iteration-fusion.md) and
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md));
a `lowering-verifier` audit confirming the dispatch rule + the re-order rule +
summation-order table against the L0 source is the standard follow-up, not a status
reduction.

> **Member-level caveat (not a status reduction).** The `tdot` dispatch arm is carried
> with the `L2/inner_product` type-API-surface-only evidentiary note: `TransposeDot` has
> zero Palace call sites (declaration + definition only, verified). The dispatch
> *structure* is firm and the `dot` + weighted arms are behaviorally exercised; only the
> `tdot` arm's behavioral weight is API-only.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in the high→low chapter
  body).** Lifting an L1 inner-product leaf *up* to the L2 fold is determinate: each leaf
  IS the fold with a fixed kernel/weight (`dot` = conjugated kernel, `tdot` = unconjugated
  kernel, `bilinear_form` = `inner_product_M`), so the lift requires no additional
  structure beyond naming the kernel/weight. The lift loses (a) the pinned reduction tree
  (the L2 fold is order-agnostic) and (b) the L0 arg-order/conjugation handedness (the L2
  fold pins arg-1), so the lift is value-faithful but NOT bit-faithful and NOT
  handedness-faithful — re-lowering recovers the original Palace call only if the
  summation-order table AND the operand-swap re-order are re-applied. This reverse-direction
  note lives here in working notes per the high→low layer-definition discipline; the formal
  chapter narrates only L2 → L1.

- **Carry-forward from `linear-combination-fold-specialization-theme-followups` (OQ;
  surfaced as plan items, NOT folded in — out of this theme's scope).** I reviewed the
  just-landed sibling theme's `## Open questions / caveats` (cycle-018). Its three live
  follow-ups are all sibling-theme-specific or working-note material, none small/in-scope
  for *this* theme:
  - its **lifting note** (reverse direction) — mirrored here for the inner-product fold
    above; no action on the linear_combination theme needed.
  - its **no-dedicated-test caveat** — the linear-combination free functions have no unit
    test; orthogonal to inner_product (the real `inner_product` HAS a test,
    `test/unit/test-vector.cpp:206-207`; the complex/weighted members do not — that caveat
    belongs to `L2/inner_product`, recorded there).
  - its **arity-≥4 chunking note** — arity-specific, no analogue here (the inner-product
    fold has no fixed-arity L1 family; its dispatch is on conjugation/weight, not arity).
  Recommend the integrator/meta-phase treat `linear-combination-fold-specialization-theme-followups`
  as **resolvable on the linear_combination side** (its follow-ups are caveats already in
  that theme, not blockers) — this inner-product theme does not consume any of them.

- **Weighted-member reduction-tree is two-stage (recorded, not over-claimed).** The
  weighted dispatch arm's bit-reproduction requires pinning BOTH the M-application reduction
  (the operator's internal SpMV/quadrature tree — opaque behind `apply_linop`) AND the
  subsequent dot reduction. The summation-order table records this as a two-stage tree but
  does not enumerate the M-apply tree (it is `apply_linop`-internal and matrix-free-
  representation-dependent). A `lowering-verifier` pass that needs the full
  weighted-member bit-reproduction story would pull the M-apply tree from the
  `apply-linop-mutation-rotation` theme. Tracked under the existing OQ
  `apply-linop-lowering-verifier-audit-cohort` (no new OQ needed).

- **Conjugate-pair re-order: which L0-call form does Palace prefer at each site?** This
  theme records the operand-swap form (`linalg::Dot(comm, y, x)`) and the outer-conj form
  (`conj(linalg::Dot(comm, x, y))`) as equivalent recoveries of the L2 `xᴴ y`. Palace's
  *own* call sites all pass operands in the order that yields `yᴴ x` and then either
  project to real (invisible) or consume the conjugate knowingly. A full caller audit
  classifying every `linalg::Dot` site as "real-projected (re-order invisible)" vs
  "full-complex (re-order observable)" would tighten the re-order story to per-site
  precision; deferred as a `lowering-verifier` / `same-layer-cross-cutter` follow-up (small,
  not blocking). Relatedly, OQ `dot-reduction-tree-determinism-survey` (deferred) would
  cover the bit-determinism half.

- **Plan / OQ bookkeeping (recommendation for the integrator).** This theme firms plan
  **Now (active) #2** (`L2-L1/inner-product-fold-specialization`). The OQ
  `inner-product-harvester-formalization-and-conjugation-pinning` is resolved by dispatch #1
  (conjugation pinned) and consumed here (re-order narrated); recommend close/migrate. The
  L2-L1 `index.md` working-note and `L2/index.md` overlay refresh (note the two reduce-to-X
  fold siblings now both have firm specialization themes) are layer-intro-author scope, not
  actioned here.

```yaml
verified_against:
  - citation: palace/linalg/vector.cpp:263-267
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: ComplexVector::Dot = x·conj(y) = yᴴ x; Hermitian kernel + conjugate-pair source. Exact.
  - citation: palace/linalg/vector.cpp:269-274
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: TransposeDot = x·y (unconjugated); real-part sign ALSO flips vs Dot (not only the Im cross-term) — prose nuance, value correct.
  - citation: palace/linalg/vector.cpp:664-672
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: real LocalDot single Hypre pass; MFEM_ASSERT(x.Size()==y.Size()) at :668. Exact.
  - citation: palace/linalg/vector.cpp:674-685
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: complex LocalDot four real dots, Im cross-term '−'; self-dot imag=0 branch at :678 (theme cites :679, off by 1, within fast-path span).
  - citation: palace/linalg/vector.hpp:240-262
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: arg-2-conj doc comments :242,:246 exact; Dot template :247-253; Norml2 :257-260 (comment :255).
  - citation: palace/linalg/operator.cpp:621-628
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: real-Operator weighted Dot body exact; INLINE Ax anchor drift — actual ComplexVector Ax(A.Height()) at :624 not :623.
  - citation: palace/linalg/operator.cpp:631-638
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: ComplexOperator weighted Dot body exact; INLINE Ax anchor drift — actual Ax at :634 not :632.
  - citation: palace/linalg/operator.cpp:598-617
    verdict: partially-supports
    audited_at: 2026-05-29T034441Z
    note: Norml2 SPD-realness consumer present; SPD comment at :612 (theme ALREADY pins :612 — verified, no change); SPD assertion is a single line at :616 (theme says :615-616, but :615 is the dot=Dot(...) line — narrow to :616).
  - citation: palace/linalg/iterative.cpp:395
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: CG beta = linalg::Dot(comm, z, r) exact; real-consumed (re-order invisible). Second site at :460.
  - citation: palace/models/boundarymodeoperator.cpp:85
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: Poynting diagonal Dot(comm, et, *Bttr, et); realness rests on Bttr-Hermitian + diagonal (domain property, not source-asserted here).
  - citation: palace/models/boundarymodeoperator.cpp:90
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: cross-coupling Dot(comm, en, Atn, et); en≠et off-diagonal, Atn ComplexWrapperOperator non-Hermitian → full complex value, re-order observable. Exact.
  - citation: palace/linalg/nleps.cpp:487,492
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: std::abs(linalg::Dot(...)) norm witnesses (magnitude convention-blind). Exact.
  - citation: TransposeDot search_text over palace/**
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: exactly 2 hits — vector.hpp:112 decl + vector.cpp:269 def; zero call sites. tdot type-API-surface-only caveat verified.
  - citation: book/src/L1/dot.md:33-35,43,49
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: dot/tdot kernel rows, arg-1-conj convention, self-dot trick — all present.
  - citation: book/src/L1/bilinear-form.md:39-43,63,119-145
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: xᴴ M y signature, Category-4 workspace, conjugation-asymmetry reconciliation — all present.
coverage_verdict: fully-supported
status_recommendation: keep firm (no status change; semantic content fully supported)
audit_caveat: three inline operator.cpp anchors drifted (Ax :623→:624, :632→:634; SPD assert range :615-616→:616) — citation-correction follow-up, not a status reduction. (SPD comment is ALREADY :612 in the live theme — verified, no change.)
```

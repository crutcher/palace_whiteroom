# dot

The conjugation-axis leaf of the L2 inner-product fold, rendered as its own
fusion-rotation chapter: the mutation-free reduce-to-scalar reduction `α = ⟨x, y⟩` (and
its unconjugated co-variant `tdot`). This is the **leaf floor** under the L3 [`dot`](../L3/dot.md)
field operation — present so the L3 leaf rests on an adjacent L2 parent per the
**Identity-lowerings still require both L levels** invariant, rather than skipping a layer.
It is the same-named specialization of the fold-parent [`inner_product`](./inner_product.md)
(do **NOT** merge — see § "Relation to `inner_product` (fold-parent; do NOT merge)").

## Context

L2 is the fusion-rotation layer (`book/src/L2/index.md`): "Kernel fusion across multiple
algebraic operations is unfolded into composition… Batched specialized BLAS calls are
written as compositions of base primitives." `dot` at L2 is the BLAS-1 inner-product
reduction at that layer — a pure value-producing reduction over the length axis `N`, with
no control flow, no monadic state threading, and no convergence predicate.

This entry is a **thin floor entry**, authored under the 2026-05-31 foundation-first
directive `l2-floor-under-l3-blas1-cohort`. Its purpose is floor *presence*: the firm L3
[`dot`](../L3/dot.md) (the iteration-rotation rendering, consumed inside the `krylov-step`
body) and the firm L1 [`dot`](../L1/dot.md) (the mutation-rotation leaf) sandwich a layer
at which `dot` had no chapter. The L2 entry fills it so the lowering chain L3 → L2 → L1
has a present chapter at every adjacent edge, and the L3 leaf can lower to an adjacent L2
parent rather than non-adjacently to L1.

`dot` is **defined in L2 vocabulary** here (high→low discipline, CLAUDE.md §Methodology
invariants "Layers are defined high→low"): the signature, semantics, and algebraic laws
are stated at the L2 fusion-rotation resolution. The two adjacent rotations — how the L2
form lowers to L1 (where the fused Hypre kernel and the local-then-collective two-step
reappear) and how the L3 form lowers to L2 — are narrated by the separate lowering themes
(`dot`'s L2>L1 edge by the D4-authored theme this cycle; the L3>L2 edge likewise). This
chapter does not define `dot` in terms of L1 primitives.

The companion concept page [`dot`](../concepts/dot.md) carries the BLAS-1 heritage framing;
the L1 entry [`L1/dot`](../L1/dot.md) is authoritative on every factual claim about the
Palace surface (the receiver-vs-argument conjugation asymmetry, the self-dot `&x==&y` fast
path, the complete L0 evidence list). This L2 entry adds **fusion-rotation framing** and
does not duplicate those Palace-surface details.

## Relation to `inner_product` (fold-parent; do NOT merge)

`dot` at L2 is the **conjugation-axis leaf** of the L2 fold-parent
[`inner_product`](./inner_product.md). The relationship is leaf-of-fold, not equality:

- [`inner_product`](./inner_product.md) is the **generalizing reduce-to-scalar fold**
  `foldl (+) zero (zipWith kernel x y)` that unifies `dot` (Hermitian), `tdot`
  (unconjugated), and `bilinear-form` (M-weighted) along the conjugation / element-type /
  weight-presence axes. It is the form `dot` fuses *up* into.
- `dot` (this entry) is the **plain Hermitian / symmetric member at one fixed conjugation
  value** — `inner_product x y` with `M = I` and the Hermitian (arg-1-conjugated) kernel,
  rendered as its own L2 chapter so the L2 floor under the L3 leaf is present.

The recovery is exactly the specialization recorded at
[`inner_product`](./inner_product.md) §Signature:

    dot(x, y)  = inner_product x y          -- Hermitian (complex) / symmetric (real)
    tdot(x, y) = inner_product x y           -- with the unconjugated kernel (complex-only)

**The codomain/fold distinction is load-bearing — do NOT merge** (`book/src/L2/index.md`
§"Fold-cohort boundary"). `inner_product` is the variadic / parametric fold over the
conjugation-element-type-weight family; `dot` is the named leaf at the single plain
conjugation value, with no `M`. Merging the leaf into the fold-parent would erase the
floor-presence the L3 leaf rests on (the L3 [`dot`](../L3/dot.md) lowers to an adjacent
*same-named* L2 parent, not to the generalizing fold). The sibling fold
[`linear_combination`](./linear_combination.md) (reduce-to-`Tensor[N]`, folds the term
axis) is the *other* fold and is unrelated to this leaf except as the do-NOT-merge sibling
of `inner_product`.

## Signature

    dot   :: (x: Tensor[N], y: Tensor[N]) -> Scalar
    tdot  :: (x: Tensor[N], y: Tensor[N]) -> Scalar     -- complex-only variant

Two operators in one chapter because they share the entire reduction skeleton (sum over
`N`) and differ only by the per-element kernel. The L2 signature is identical in shape to
the L1 [`dot`](../L1/dot.md) signature; the rotation L2 → L1 is identity-in-form on the
primitive (the fusion the L2 layer un-does lives at the leaf's *implementation*, recorded
by the L2>L1 lowering theme, not in the signature).

Shape contract (bunsen-style; named axes):

- **`x`** — `Tensor[N]` — read-only; the **conjugated** (arg-1) operand for the Hermitian
  variant (see § "Conjugation convention").
- **`y`** — `Tensor[N]` — read-only; the **linear** (arg-2) operand.
- **result** — `Scalar` — element type per the rule below; `zero` (the additive identity
  of the scalar field) on the empty length axis.
- `x` and `y` share one length axis `N` and one element type `T ∈ {real, complex}`.

Per-element kernel (the conjugation × element-type axes; inherited from the L1 leaf and
the fold-parent's kernel table):

| element type | operator | per-element kernel | form |
|---|---|---|---|
| `real`    | `dot`  | `x[i] · y[i]`        | bilinear symmetric (conjugation a no-op) |
| `complex` | `dot`  | `conj(x[i]) · y[i]`  | Hermitian sesquilinear (arg-1 conjugated) |
| `complex` | `tdot` | `x[i] · y[i]`        | unconjugated bilinear |

## Conjugation convention

`dot` is **conjugate-linear in arg-1, linear in arg-2** (the standard mathematical
Hermitian inner product `⟨x, y⟩ = xᴴ y`), matching the fold-parent
[`inner_product`](./inner_product.md) §"Conjugation convention (pinned)" and the L1 leaf
[`L1/dot`](../L1/dot.md) §Semantics. The L2 entry inherits this convention unchanged so the
leaf and the fold-parent agree.

Palace's L0 surface pins the **opposite** operand — the free-function and its kernels
conjugate **arg-2** (`linalg::Dot(comm, x, y) = yᴴ x`, comment at `palace/linalg/vector.hpp:246`;
kernel body `palace/linalg/vector.cpp:263-267` returns `x·conj(y) = yᴴ x`). The two are
complex conjugates of each other (`xᴴ y = conj(yᴴ x)`). This re-order is the deliberate,
self-consistent L1 mutation-rotation choice recorded at [`L1/dot`](../L1/dot.md) §Semantics
and reconciled in detail at [`inner_product`](./inner_product.md) §"Conjugation convention
(pinned)"; its value-level effect is narrated by the **lowering themes** (the L2>L1 edge),
not re-derived here. For consumers that take a real projection (`std::real`, `std::abs`) of
the result — CG's `β = ⟨r, z⟩` for SPD `B`, norms via `std::abs(linalg::Dot(...))` — the
re-order is invisible (a value and its conjugate agree under projection), which is why both
conventions coexist harmlessly in the Palace call sites.

## Semantics

`dot` reduces the two tensors to a scalar: starting from the additive identity `zero`, it
sums the per-element products `kernel(x[i], y[i])` over the length axis `N`. The result is
`Σᵢ kernel(xᵢ, yᵢ)` — the Hermitian (complex) / symmetric (real) inner product of `x` and
`y`. The unconjugated co-variant `tdot` is the same reduction with the unconjugated kernel.

It is **pure** at L2: it consumes `x`, `y` and produces a fresh scalar; there is no
destination buffer (the L0 in-place destination is the return register / a stack scalar).
The reduction over the length axis `N` collapses `N` to a single scalar — the structural
opposite of [`linear_combination`](./linear_combination.md), which preserves `N`.

The reduction carries an **MPI collective** in the L0 realization
(`LocalDot ∘ Mpi::GlobalSum`, `palace/linalg/vector.hpp:247-253`). The collective is **not**
in the L2 signature (single-rank scope; ranks read as their single-rank equivalents per
CLAUDE.md §Scope). The local-then-collective two-step reappears only in the L2>L1 lowering.

The self-dot fast path `&x == &y` (`palace/linalg/vector.cpp:266` returning imaginary part
`0.0` for the Hermitian form) is a transparent performance trick at L2 — algebraically
`xᴴ x` is exactly real, so eliding the cancellation is equivalent. It disappears in the
L2>L1 lowering.

## Fusion note

The L2 fusion content for `dot` is **the same content the fold-parent
[`inner_product`](./inner_product.md) §"Fusion note" already absorbs**, restricted to the
plain (`M = I`) Hermitian / symmetric leaf — there is no fusion structure unique to the
`dot` leaf beyond the fold-parent's. The fused reduction kernels Palace exposes for the
inner product are:

- the real path — a single Hypre `hypre_SeqVectorInnerProd` strided pass
  (`palace/linalg/vector.cpp:665-672`, with the aligned-pass precondition
  `MFEM_ASSERT(x.Size() == y.Size())` at `:668`);
- the complex path — four real local dots combined into a `(Re, Im)` scalar
  (`palace/linalg/vector.cpp:674-685`), the element-type axis lifted componentwise;
- the local-then-collective two-step `LocalDot ∘ Mpi::GlobalSum`
  (`palace/linalg/vector.hpp:247-253`).

These are the **transparent-performance-trick implementation** of the reduction: a strided
per-element-kernel pass followed by a pinned-tree sum, rather than the unfused
seed-then-accumulate chain. They compute the same value as the unfused fold modulo IEEE-754
summation order (the load-bearing reduction-tree non-law in § "Algebraic laws"). L2 de-fuses
this into the canonical reduction; the L2 `dot` leaf records the fusion as this one note and
**defers the full de-fusion treatment to the fold-parent** (which carries it for the whole
conjugation / element-type / weight family) and to the L2>L1 lowering theme (which pins which
reduction tree each lowered call selects).

## Algebraic laws

The laws below hold and are **inherited unchanged from the L1 leaf** [`L1/dot`](../L1/dot.md)
(equivalently, they are the fold-parent's laws specialized to the plain leaf); the L2 form is
value-thread-isomorphic to the L1 form. Reproduced so the L2 reader does not have to reach to
L1. Absences are deliberate.

**For `dot` over real element-type (bilinear symmetric form):**

1. **Symmetry**: `dot(x, y) = dot(y, x)`.
2. **Bilinearity (left)**: `dot(α·x₁ + x₂, y) = α·dot(x₁, y) + dot(x₂, y)`.
3. **Bilinearity (right)**: `dot(x, α·y₁ + y₂) = α·dot(x, y₁) + dot(x, y₂)`. (Follows from 1 + 2.)
4. **Positive semi-definite at `y = x`**: `dot(x, x) ≥ 0`, with equality iff `x = 0` (exact arithmetic).
5. **Zero in either argument**: `dot(0, y) = dot(x, 0) = 0`.

**For `dot` over complex element-type (Hermitian sesquilinear form, conjugate-linear in arg-1):**

6. **Hermitian symmetry**: `dot(x, y) = conj(dot(y, x))`.
7. **Conjugate-linearity (left)**: `dot(α·x₁ + x₂, y) = conj(α)·dot(x₁, y) + dot(x₂, y)`.
8. **Linearity (right)**: `dot(x, α·y₁ + y₂) = α·dot(x, y₁) + dot(x, y₂)`.
9. **Positive semi-definite at `y = x`**: `dot(x, x) ∈ ℝ` and `dot(x, x) ≥ 0`, with equality
   iff `x = 0` (exact arithmetic). Confirmed by the implementation returning imaginary part
   `0.0` exactly when `&x == &y` (`palace/linalg/vector.cpp:266`).
10. **Zero in either argument**: `dot(0, y) = dot(x, 0) = 0`.

**For `tdot` over complex element-type (unconjugated bilinear form):**

11. **Symmetry**: `tdot(x, y) = tdot(y, x)`.
12. **Bilinearity in each argument** (analogue of laws 2–3 with no conjugation).
13. **Not positive semi-definite**: `tdot(x, x) ∈ ℂ` in general; `tdot(x, x) = 0` does **not**
    imply `x = 0` (e.g. `x = (1, i)` gives `1·1 + i·i = 0`). The explicit absence: `tdot` is
    the indefinite form, distinct from `dot`.

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Associativity of the reduction-tree under IEEE-754 (the load-bearing non-law).** The
  reduction's combining `(+)` is floating-point non-associative: different summation orders
  (different reduction trees) give different bit-level results. Palace pins a specific tree
  (Hypre per-rank kernel + MPI tree-reduce). Per CLAUDE.md "load-bearing numerical tricks…
  non-associative reduction orderings… preserve as explicit algebraic claims", this is
  recorded, not erased: the L2 `dot` is order-agnostic for value, but bit-identical
  reproduction of an L0 reduction requires matching that reduction's pinned tree (which tree
  each lowered call pins is recorded by the L2>L1 lowering theme).
- **Cauchy–Schwarz strictness in floating point**: `|dot(x, y)|² ≤ dot(x, x) · dot(y, y)`
  holds mathematically but can fail by ULP-level amounts due to summation ordering.
- **Distributivity over vector-multiplication structure**: not applicable — `dot` is not a
  binary operator on vectors closing back to vectors; it is a reduction to a scalar.

## Dependencies

- **Fold-parent (do NOT merge):** [`inner_product`](./inner_product.md) (firm) — the
  reduce-to-scalar fold this leaf is the plain Hermitian / symmetric member of. `dot` is the
  conjugation-axis leaf; `inner_product` is its generalizing fold sibling (codomain/fold
  distinction load-bearing, `book/src/L2/index.md` §"Fold-cohort boundary").
- **Same-layer (L2):** none. `dot` is a leaf reduction at L2 — it composes no other L2
  operator; its sub-operations (scalar multiplication, scalar conjugation in the complex
  case, scalar addition) are at or below the L2 resolution.
- **Consumers (L2):** [`krylov-step`](./krylov-step.md) (the per-step body's scalar-stratum
  updates — CG's `α = dot(r, z) / dot(Ap, p)`, GMRES orthogonalization coefficients);
  [`orthogonalize`](./orthogonalize.md) (the `project` stage); [`gram`](./gram.md) (the
  all-pairs `inner_product` entry kernel); [`deflate`](./deflate.md) (coordinate extraction
  `Xᴴv`). These consume `dot`/`inner_product` as the inner-product leaf.
- **Sibling fold (unrelated to this leaf except as `inner_product`'s do-NOT-merge sibling):**
  [`linear_combination`](./linear_combination.md) — reduce-to-`Tensor[N]`, folds the term
  axis.
- **Cross-cutting concept:** [`dot`](../concepts/dot.md) — BLAS-1 heritage framing.
- **L1 anchor:** [`L1/dot`](../L1/dot.md) (firm cycle-002) — authoritative on the Palace
  surface, the receiver-vs-argument conjugation asymmetry, the self-dot fast path, and the
  complete L0 evidence list. The L2 entry does not duplicate those details.

## Variant axes

Inherited unchanged from the L1 leaf:

1. **element-type** (`real` | `complex`) — at L0 these are separate kernels (real via a
   single Hypre `hypre_SeqVectorInnerProd`, `palace/linalg/vector.cpp:665-672`; complex via
   four real local dots lifted into `(Re, Im)`, `palace/linalg/vector.cpp:674-685`); at L2
   one operator parameterized by element type, the complex form the real form lifted
   componentwise.
2. **conjugation convention** (complex element-type only): `hermitian` (the default `dot` —
   `ComplexVector::Dot`, `palace/linalg/vector.cpp:263-267`) | `unconjugated` (`tdot` —
   `ComplexVector::TransposeDot`, `palace/linalg/vector.cpp:269-274`). At L2 these are
   distinct operators (sharing only the reduction skeleton), because the algebraic laws
   differ — `dot` is PSD-at-diagonal, `tdot` is not.

No new variant axes introduced at L2; none merged or split. The weight-presence axis
(`M = I` vs general `M`) that the fold-parent [`inner_product`](./inner_product.md) carries is
**NOT** a variant axis of this leaf — the M-weighted member is the separate fold-parent member
[`bilinear-form`](../L1/bilinear-form.md); `dot` is the `M = I` leaf only. The reduction-tree
(an L0 implementation detail, transparent for value, load-bearing for bit-reproduction) is
recorded in the lowering theme, not as an L2 axis.

## Status

`firm` — the L2 form is value-thread-isomorphic to the firm L1 leaf [`L1/dot`](../L1/dot.md)
(identity-in-form rotation on the primitive); every algebraic law is a standard
sesquilinear / bilinear fact inherited unchanged, with the PSD-at-diagonal law directly
confirmed by the in-source `&x==&y` imag=`0.0` elision (`palace/linalg/vector.cpp:266`), and
the reduction-tree associativity paired as the explicit IEEE non-law per the
load-bearing-numerical-trick discipline. This is a **thin floor entry** authored under the
2026-05-31 foundation-first directive `l2-floor-under-l3-blas1-cohort`: its purpose is floor
*presence* so the firm L3 [`dot`](../L3/dot.md) leaf rests on an adjacent same-named L2
parent (per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L
levels**) rather than skipping a layer to L1. The fusion-rotation content is the
fold-parent [`inner_product`](./inner_product.md)'s; this leaf records it as one deferring
note. No fusion structure unique to the leaf — beyond the fold-parent's — was found.

> **Member-level caveat (not a status reduction; inherited from the L1 leaf / fold-parent).**
> `tdot` is the unconjugated conjugation-axis value with a **type-API-surface-only**
> evidentiary note: `ComplexVector::TransposeDot` has zero Palace call sites (declaration
> `palace/linalg/vector.hpp:112` + definition `palace/linalg/vector.cpp:269` only). The
> reduction *structure* is firm and the Hermitian arm is behaviorally exercised (CG /
> orthogonalization / NLEPS sites); only `tdot`'s behavioral weight is API-only. See the
> fold-parent [`inner_product`](./inner_product.md) § "tdot".

## L2 vs L1 distinction

- **L1**: pure functional reduction `α = dot(x, y)`. Mutation-rotation layer — the L0
  destination buffer is erased (there is none; the result is a returned scalar); the MPI
  collective is folded into the L1>L0 lowering; the receiver-vs-argument asymmetry on the L0
  method form is erased (arg-1 named the conjugated operand by convention).
- **L2**: the same reduction `α = dot(x, y)` rendered as the fusion-rotation leaf. The family
  of fused reduction kernels (the real Hypre strided pass, the complex four-real-dot lift, the
  local-then-collective two-step) is recognized as a kernel-fusion choice and de-fused into the
  canonical reduction; the leaf is the plain (`M = I`) Hermitian / symmetric member of the
  fold-parent [`inner_product`](./inner_product.md). The signature is identical to L1; the
  rotation L2 → L1 is identity-in-form on the primitive (the fusion the L2 layer un-does is at
  the implementation, captured by the L2>L1 lowering theme — not in the signature).

The two layers' entries are value-thread-isomorphic on the primitive itself. The L2 entry
exists for floor presence — so the L3 [`dot`](../L3/dot.md) leaf has an adjacent L2 parent.

## Evidence

The L2 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's
signature); all L0 evidence is transitive through the firm L1 leaf. Direct citations relevant
to this L2 entry (paths relative to `reference/palace/`; L0 ranges self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation):

- [`book/src/L1/dot.md`](../L1/dot.md) (firm cycle-002) — authoritative on the Palace surface,
  the signature, the algebraic laws (inherited unchanged at L2), the variant axes (inherited
  unchanged at L2), and the complete L0 evidence list.
- [`book/src/L2/inner_product.md`](./inner_product.md) (firm cycle-019) — the fold-parent this
  leaf specializes; § "Conjugation convention (pinned)" (the arg-1-conjugated convention +
  the `yᴴ x` ↔ `xᴴ y` reconciliation), § "Fusion note" (the family-level de-fusion this leaf
  defers to), § Signature (the `dot(x,y) = inner_product x y` recovery).
- [`book/src/L2/index.md`](./index.md) § "Fold-cohort boundary" — the load-bearing
  codomain/fold do-NOT-merge distinction between the `inner_product` fold and its leaves.
- [`book/src/L3/dot.md`](../L3/dot.md) (firm cycle-011) — the L3 consumer this floor goes
  under; the iteration-rotation rendering whose adjacent L2 parent this entry supplies.
- [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md)
  § "Applicability conditions" point 3 — the load-bearing statement that the seven BLAS-1
  primitives (including `dot`) are L3-native by signature shape (no per-element loop visible),
  which is what makes the L3>L2 rotation identity-in-form.
- `palace/linalg/vector.hpp:110-113` — `ComplexVector::Dot` decl, comment `// Vector dot
  product (yᴴ x) or indefinite dot product (yᵀ x) for complex vectors.`; `TransposeDot`
  alongside; `operator*` aliased to `Dot`. **Self-verified (anchor `Dot` at :111-113).**
- `palace/linalg/vector.hpp:242-244` — `linalg::LocalDot` decls (real + complex).
  **Self-verified (anchor `LocalDot` at :243-244).**
- `palace/linalg/vector.hpp:247-253` — `linalg::Dot` template = `Mpi::GlobalSum ∘ LocalDot`
  (the local-then-collective two-step). **Self-verified (anchor `GlobalSum` at :251).**
- `palace/linalg/vector.cpp:263-267` — `ComplexVector::Dot` body = `x·conj(y) = yᴴ x`, with
  the `&y==this` imag=`0.0` self-dot fast path at `:266`. The Hermitian kernel + the law-9
  confirmation. **Self-verified (anchor `Dot` at :263; `0.0` at :266).**
- `palace/linalg/vector.cpp:269-274` — `ComplexVector::TransposeDot` body: unconjugated
  bilinear, negated imaginary cross-term — the `tdot` kernel. **Self-verified (anchor
  `TransposeDot` at :269).**
- `palace/linalg/vector.cpp:665-672` — `LocalDot(Vector, Vector)` via a single Hypre
  `hypre_SeqVectorInnerProd` (`:671`), with `MFEM_ASSERT(x.Size()==y.Size())` (`:668`). The
  real-path fused kernel + the aligned-pass precondition. **Self-verified (anchors
  `hypre_SeqVectorInnerProd` at :671, `MFEM_ASSERT` at :668).**
- `palace/linalg/vector.cpp:674-685` — `LocalDot(ComplexVector, ComplexVector)`: four real
  `LocalDot`s combined into `(Re, Im)`, with the `&x==&y` self-dot fast path. The element-type
  axis (complex = real fold lifted). **Self-verified (anchor `LocalDot` at :674,:678,:682-683).**
- `test/unit/test-vector.cpp:206-207` — real-vector dot via `operator*`: `double dot = vec1 *
  vec2; CHECK_THAT(dot, WithinRel(32.0));` (`1·4+2·5+3·6=32`). Direct value-asserting test for
  the real member; L0-equivalent semantic documentation. **Self-verified (anchor `WithinRel`
  at :207).**
- [`book/src/concepts/dot.md`](../concepts/dot.md) — the cross-cutting concept page; BLAS-1
  heritage framing.

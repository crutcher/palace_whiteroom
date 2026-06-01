---
agent: harvester
invoked_at: 2026-06-01T051607Z
scope: L2 operator: dot
status: pending
integrated_at: 2026-06-01T062913Z
integration_commit: c1f7ea3c651e65ed212aa8500c7c8572aaa2ec92
integration_notes: "Applied clean (staging row D1). book/src/L2/dot.md created firm (thin-identity-floor); SUMMARY + L2/index dep-map row. vector.hpp:246 pinpoint kept UNCHANGED (critic citation-validity warning was a -1 read-drift false positive). LOAD-BEARING design-fork dot-l2-leaf-floor-vs-fold-only-design carried to batch-12 meta-phase. L2 firm 9->12 (cohort 3-of-13)."
inputs:
  - book/src/L1/dot.md (firm L1 leaf — authoritative on Palace surface + full L0 evidence)
  - book/src/L1-L0/dot-mutation-rotation.md (firm L1>L0 theme)
  - book/src/L3/dot.md (firm L3 consumer — convention mirror)
  - book/src/L2/inner_product.md (firm L2 fold-parent — cite as fold-parent, do NOT merge)
  - book/src/L2/index.md §"Fold-cohort boundary" (load-bearing codomain/fold distinction)
  - book/src/L3-L2/krylov-step-body-identity.md §"Applicability conditions" point 3 (the seven-primitive L3-native-by-signature statement)
  - L0 anchors (self-verified via citecheck this invocation): vector.hpp:110-113,242-244,247-253; vector.cpp:263-267,269-274,665-672,674-685; test-vector.cpp:206-207
  - directive 2026-05-31 l2-floor-under-l3-blas1-cohort (foundation-first)
---

# CYCLE: Formalize dot at L2

## Summary

Builds the L2 floor entry `book/src/L2/dot.md` — the fusion-rotation (L2) rendering of
the BLAS-1 inner-product leaf — under the 2026-05-31 foundation-first directive
`l2-floor-under-l3-blas1-cohort`. The firm L3 `dot` entry currently records its lowering
to L1 as identity-in-form with **no adjacent L2 parent present** (`book/src/L3/dot.md`
lowers straight to L1, citing the non-adjacent in-line-identity convention). Per the
methodology invariant **Identity-lowerings still require both L levels**, the L3 leaf
should rest on a *present* adjacent L2 parent rather than skip a layer. This entry
supplies that floor: it is a **thin identity-in-form L2 floor entry** whose purpose is
floor *presence*, not bulk. `dot` at L2 is a pure reduce-to-scalar reduction
`α = ⟨x, y⟩`; the fusion-rotation content (the de-fusion of Palace's fused Hypre /
four-real-dot reduction kernels and the local-then-collective two-step into the canonical
fold) is the **fold-parent** [`inner_product`](./inner_product.md)'s job — the L2 `dot`
leaf is the conjugation-axis specialization of that fold rendered as its own L2 chapter,
cited as a leaf-of, NOT merged with, `inner_product` (the codomain/fold distinction at
`book/src/L2/index.md` §"Fold-cohort boundary" is load-bearing).

No fusion content beyond what `inner_product` already absorbs was found — this is a true
thin floor entry. The fusion is one note that defers to the fold-parent; there is no
reduction-tree / collective-topology absorption that is MORE than the fold-parent already
records. The body is value-thread-isomorphic to the L1 leaf; the laws are inherited
unchanged; the L2>L1 and L3>L2 lowering themes (authored separately by D4 this cycle)
narrate the two adjacent rotations.

## Proposed changes

```new:book/src/L2/dot.md
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
```

Insert the new `dot` floor row immediately AFTER the `inner_product` row (so the leaf
sits adjacent to its fold-parent). Anchor on the start of the existing `orthogonalize`
row and prepend the new row before it:

```edit:book/src/L2/index.md
| [`dot`](./dot.md) | `(x: Tensor[N], y: Tensor[N]) -> Scalar` (Hermitian `xᴴ y` / symmetric; `tdot` = unconjugated co-variant) | **Conjugation-axis leaf floor of [`inner_product`](./inner_product.md) (do NOT merge — codomain/fold distinction load-bearing, §"Fold-cohort boundary").** The plain (`M = I`) Hermitian / symmetric member of the reduce-to-`Scalar` fold, rendered as its own L2 chapter so the L3 [`dot`](../L3/dot.md) leaf rests on an adjacent same-named L2 parent (foundation-first directive `l2-floor-under-l3-blas1-cohort`). Same-layer deps: none (leaf). Fusion content deferred to `inner_product` §"Fusion note". L1 anchor: [`dot`](../L1/dot.md) (firm). Consumers: `krylov-step`, `orthogonalize`, `gram`, `deflate`. Concepts: `dot`. | `firm` (harvested cycle-041 wave-1; thin identity-in-form L2 floor entry; value-thread-isomorphic to L1 leaf; laws inherited unchanged; no leaf-unique fusion beyond fold-parent) |
| [`orthogonalize`](./orthogonalize.md) | `(op: OrthogOp, w: Tensor[N], V: Basis[N, m]) → { residual: Tensor[N], coeffs: Tensor[m] }` | **Named composition — `project ▷ subtract`.** L1 leaf it lifts: `orthogonalize` (firm). L1 primitives the stages compose: `dot` (project), `axpy` (subtract). Concepts: `orthogonalization`, `variant-absorption` (`:131`, residual-axis disclosure), `sequential-obstruction`. Consumers: `krylov-step` (level-(b) `op.orthog`), ROM basis-extension. Sibling fold (constituent, not parent): `inner_product` (firm). | `firm` (harvested cycle-019; promoted from stub; the `l2-named-composition-lifts` backlog item / OQ orthogonalize-as-future-L2-firstclass-entry) |
```

Add the chapter entry under the **L2 Part** in `book/src/SUMMARY.md`, immediately after the
`inner_product` line (so the floor leaf sits adjacent to its fold-parent). Anchor on the
existing `inner_product` line and append the new line after it:

```edit:book/src/SUMMARY.md
- [inner_product](./L2/inner_product.md)
- [dot](./L2/dot.md)
```

## Count-ownership note (mandatory)

Per the dispatch directive and friction-ledger `parallel-blind-shared-index-count-divergence`,
this report appends ONLY its own `book/src/L2/index.md` dep-map ROW + `## Status` body + the
`book/src/SUMMARY.md` registration above. It does **NOT** touch the `book/src/L2/index.md`
§"Vocabulary cohort" consolidated **"Firm at L2"** running list / firm-count tally — **D7
(layer-intro-author) owns the L2 tally this cycle.** The integrator must NOT infer a count
update from this report; the `dot` floor row in the dep-map is the only index mutation here.

## Supporting evidence

- **Source of truth (read this invocation):** firm L1 leaf [`book/src/L1/dot.md`](../../book/src/L1/dot.md)
  (the authoritative Palace-surface + L0 evidence list — laws / variant axes / element-type
  table inherited unchanged); firm L1>L0 theme [`book/src/L1-L0/dot-mutation-rotation.md`](../../book/src/L1-L0/dot-mutation-rotation.md)
  (the local-then-collective two-step + conjugation asymmetry); firm L3 consumer
  [`book/src/L3/dot.md`](../../book/src/L3/dot.md) (convention + identity-in-form framing mirrored);
  firm L2 fold-parent [`book/src/L2/inner_product.md`](../../book/src/L2/inner_product.md)
  (§"Conjugation convention (pinned)", §"Fusion note", §Signature recovery — the leaf-of-fold
  relationship); [`book/src/L2/index.md`](../../book/src/L2/index.md) §"Fold-cohort boundary"
  (the load-bearing codomain/fold do-NOT-merge distinction).
- **L0 self-verification (this invocation, `tools/citecheck/citecheck.py --anchor`):** all
  eight cited L0 ranges verified against on-disk `reference/palace/` source — `vector.hpp:110-113`
  (`Dot` at :111-113), `:242-244` (`LocalDot` at :243-244), `:247-253` (`GlobalSum` at :251);
  `vector.cpp:263-267` (`Dot` :263, `0.0` :266), `:269-274` (`TransposeDot` :269), `:665-672`
  (`hypre_SeqVectorInnerProd` :671, `MFEM_ASSERT` :668), `:674-685` (`LocalDot`
  :674/:678/:682-683); `test/unit/test-vector.cpp:206-207` (`WithinRel` :207). Zero drift.
- **Fence-parity self-check:** the `new:book/src/L2/dot.md` body uses 4-space-indented code
  blocks for the signature samples (NOT nested ` ```text ` fences) per the
  `convert-nested-fences-to-indented-code-in-proposed-changes-block` discipline; the closing
  fence sits after the last chapter section (§Evidence). The dep-map and SUMMARY edits are
  separate fenced blocks. No live forward-links to unwritten files (the D4-authored L2>L1 /
  L3>L2 `dot` lowering themes are referenced as plain prose / inline-code, not links).

## Open questions / caveats

- **Floor-presence vs. the L3 leaf's in-line non-adjacent identity note.** The firm L3
  [`dot`](../../book/src/L3/dot.md) §"Lowers to" currently records its lowering as
  identity-in-form **directly to L1** (citing "no `book/src/L3-L1/` directory" and the
  non-adjacent in-line-identity convention). With this L2 floor now present, the L3 leaf's
  adjacent parent IS available, and the D4-authored L3>L2 `dot` theme this cycle supplies the
  adjacent-edge rotation. The L3 entry's §"Lowers to" prose may want a light refresh to point
  at the new adjacent L2 `dot` parent + the L3>L2 theme rather than (only) the non-adjacent L1
  hop. **Out of scope for this harvester** (one operator / one layer; modifying the L3 entry is
  not this dispatch). Flagged for the cycle-planner / a follow-up L3-`dot` re-anchor or the D4
  L3>L2 theme author to reconcile. (Not a defect in this entry — the L2 floor is self-coherent;
  it is a downstream-consistency touch on the L3 entry.)
- **No leaf-unique fusion surplus found.** The dispatch invited authoring a fuller L2 entry if
  genuine fusion-rotation content beyond identity surfaced (a reduction-tree / collective-topology
  absorption MORE than identity). None did: the de-fusion of the Hypre strided kernel, the complex
  four-real-dot lift, and the local-then-collective two-step are **already fully absorbed by the
  fold-parent `inner_product` §"Fusion note"** for the whole conjugation / element-type / weight
  family. The `dot` leaf's fusion is the plain-`M` restriction of that, recorded as one deferring
  note. This is the correct shape for a thin floor entry; no foundation surplus signal to raise.
- **Layer-intro refresh (note only, not actioned).** D7 (layer-intro-author) owns the
  `book/src/L2/index.md` §"Vocabulary cohort" "Firm at L2" running list + the firm-count tally
  this cycle; the new `dot` floor entry should be added to that list and the count incremented by
  D7, NOT by this report (count-ownership convention). The §"Fold-cohort boundary" Working-Note
  may also want a one-line mention that `inner_product`'s leaves now have a present same-named L2
  floor (`dot`) — layer-intro-author's call.

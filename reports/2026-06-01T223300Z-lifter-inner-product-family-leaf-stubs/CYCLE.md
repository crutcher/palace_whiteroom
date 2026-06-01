---
agent: lifter
invoked_at: 2026-06-01T223300Z
scope: inner_product-family leaf reduction-to-stub — L2/dot, L3/dot (specialization-stubs) + L2/nrm2, L3/nrm2 (consumer-stubs)
status: pending
integrated_at: 2026-06-02T010000Z
integration_commit: 9633c134b333932b31f2823c558398fafdaa9750
integration_notes: "cycle-052 D3 — applied clean (dot L2+L3 → specialization-stubs; nrm2 L2+L3 → consumer-stubs, do-NOT-merge, std::abs guard + Norml2 anchor + verbatim Downward consumer note retained); member-vs-consumer gate PASS; no build-repair needed; refactor pass COMPLETE."
inputs:
  - book/src/L2/dot.md (345 ln)
  - book/src/L3/dot.md (162 ln)
  - book/src/L2/nrm2.md (160 ln)
  - book/src/L3/nrm2.md (167 ln)
  - book/src/L2/inner_product.md (firm cycle-050; §"Specializations" :158, §"Consumer (NOT an instance)" :431)
  - book/src/L3/inner_product.md (firm cycle-050; §"Specializations" :133, §"Consumer (NOT an instance)" :319)
---

# CYCLE: Re-anchor inner_product-family leaf chapters to stubs

## Summary

Cycle-052 D3 completes the vocabulary-shift-redirect refactor pass for the `inner_product`-family
leaf chapters by reducing four firm leaf entries to thin stubs that defer to their now-firm
`inner_product` combinator parents (firm cycle-050). The reduction applies **two distinct stub
kinds** by one owner so the member/consumer distinction lands consistently:

- **(i) `dot` → specialization-stubs** (`L2/dot.md` 345→~70 ln, `L3/dot.md` 162→~55 ln). `dot` IS
  a fold member — the `M=I` Hermitian/symmetric specialization of `inner_product`. The stub carries
  a LIVE "specialization of `inner_product`" link up, RETAINS `dot`'s unique L0 anchors + the
  conjugation variant-axis row (Hermitian `dot` vs unconjugated `tdot` — value-bearing for complex
  vectors), and DEFERS all semantics/laws to the combinator (deletes the duplicated body).
- **(ii) `nrm2` → consumer-stubs** (`L2/nrm2.md` 160→~60 ln, `L3/nrm2.md` 167→~55 ln). `nrm2` is the
  **do-NOT-merge carve-out** — NOT a fold member but a CONSUMER (`√ ∘ abs ∘ inner_product` at `y=x`).
  The stub says "consumer of `inner_product`" (NOT "specialization of"), RETAINS the load-bearing
  `std::abs` defensive-guard claim + the `vector.hpp:255-260` `Norml2` anchor, and points at the
  c051 in-line §Downward consumer note (kept verbatim).

All four files are kept on disk (reduce-to-stub, not delete), so every inbound link stays LIVE —
including `L3/nrm2.md → ../L2/nrm2.md`, `L3/nrm2.md → ./dot.md`, the `normalize`/`divfree-projector`/
`ksp_solve`/`orthogonalize`/`chebyshev`/`assemble-diagonal` references, and the four SUMMARY.md rows
(D4-owned). Zero dangling confirmed (see §Supporting evidence). All status stays `firm`. Index
rows/narrative untouched (D4 owns those).

## Proposed changes

### (i-a) L2/dot.md → specialization-stub

```edit:book/src/L2/dot.md
[old]: # dot

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
directive `l2-floor-under-l3-leaf-cohort`. Its purpose is floor *presence*: the firm L3
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
2026-05-31 foundation-first directive `l2-floor-under-l3-leaf-cohort`: its purpose is floor
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
[new]: # dot

> **Specialization-stub (reduced cycle-052 D3, vocabulary-shift-redirect refactor pass).**
> `dot` at L2 is the **`M = I` Hermitian/symmetric specialization** of the fold combinator
> [`inner_product`](./inner_product.md) (firm cycle-050) — the combinator IS the L2 entry for
> the reduce-to-scalar inner-product family; `dot` is a **specialization note** under it
> (per CLAUDE.md §Methodology invariants ⟢ — the combinator is the entry, members are
> specialization notes). This chapter is reduced to the leaf-level facts the combinator does
> not carry: the conjugation variant-axis (`dot` Hermitian-conjugated vs `tdot` unconjugated
> — value-bearing for complex vectors) and `dot`'s unique L0 anchors. Semantics, algebraic
> laws, fusion-rotation framing, and the do-NOT-merge boundary are **deferred** to the
> combinator [`inner_product`](./inner_product.md) §"Specializations" — not re-derived here.

The conjugation-axis specialization of the L2 [`inner_product`](./inner_product.md) combinator:
the mutation-free reduce-to-scalar reduction `α = ⟨x, y⟩` at the Hermitian (complex) /
symmetric (real) kernel value with `M = I`, co-defined with its unconjugated co-variant
`tdot`. Recovered from the combinator at fixed axis-values:

    dot(x, y)  = inner_product x y          -- Hermitian (complex) / symmetric (real)
    tdot(x, y) = inner_product x y          -- with the unconjugated kernel (complex-only)

**Do NOT merge into `inner_product`** — the codomain/fold distinction is load-bearing
(`book/src/L2/index.md` §"Fold-cohort boundary"): `inner_product` is the variadic fold over
the conjugation/element-type/weight family; `dot` is the named leaf at the single plain
conjugation value (`M = I`). The named-specialization presence lets the L3 [`dot`](../L3/dot.md)
lower to an adjacent same-named L2 parent. All semantics, laws, and fusion content are the
combinator's — see [`inner_product`](./inner_product.md) §"Specializations".

## Signature

    dot   :: (x: Tensor[N], y: Tensor[N]) -> Scalar
    tdot  :: (x: Tensor[N], y: Tensor[N]) -> Scalar     -- complex-only variant

Two operators in one chapter because they share the entire reduction skeleton (sum over `N`)
and differ only by the per-element kernel. The signature is the combinator's, read at the
plain (`M = I`) conjugation value. Full shape contract: [`inner_product`](./inner_product.md)
§Signature.

## Conjugation variant-axis (the leaf-level fact, value-bearing for complex vectors)

`dot` is **conjugate-linear in arg-1, linear in arg-2** (`⟨x, y⟩ = xᴴ y`). The conjugation
convention is **value-bearing for complex vectors** and is the one fact this specialization
carries beyond the combinator. The per-element kernel by element-type:

| element type | operator | per-element kernel | form |
|---|---|---|---|
| `real`    | `dot`  | `x[i] · y[i]`        | bilinear symmetric (conjugation a no-op) |
| `complex` | `dot`  | `conj(x[i]) · y[i]`  | Hermitian sesquilinear (arg-1 conjugated) |
| `complex` | `tdot` | `x[i] · y[i]`        | unconjugated bilinear |

The two are distinct operators because the algebraic laws differ: `dot` is PSD-at-diagonal
(`dot(x, x) ≥ 0`, confirmed by the in-source `&x==&y` imag=`0.0` elision at
`palace/linalg/vector.cpp:266`); `tdot` is the indefinite form (`tdot(x, x) = 0` does not imply
`x = 0`, e.g. `x = (1, i)`). The full conjugation-convention reconciliation (Palace's L0
surface pins the **opposite** operand — `linalg::Dot(comm, x, y) = yᴴ x = conj(xᴴ y)`) and the
weight-presence axis (`M = I` here; the M-weighted member is the separate
[`bilinear-form`](../L1/bilinear-form.md)) live at the combinator §"Specializations" and the
genuine L2>L1 [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
theme — not re-derived here.

> **Member-level caveat (inherited; not a status reduction).** `tdot` (`ComplexVector::TransposeDot`)
> has zero Palace call sites (declaration `palace/linalg/vector.hpp:112` + definition
> `palace/linalg/vector.cpp:269` only). The reduction structure is firm and the Hermitian arm is
> behaviorally exercised; only `tdot`'s behavioral weight is API-only. See
> [`inner_product`](./inner_product.md) §"tdot".

## Status

`firm` — specialization-stub. `dot` at L2 is the `M = I` Hermitian/symmetric specialization of
the firm L2 [`inner_product`](./inner_product.md) combinator (firm cycle-050); semantics,
algebraic laws, fusion-rotation framing, and the do-NOT-merge boundary are inherited from the
combinator unchanged. This chapter retains only the conjugation variant-axis (the value-bearing
leaf-level fact) and `dot`'s unique L0 anchors. Originally harvested cycle-041 wave-1 as a thin
L2 floor under the L3 leaf cohort; re-expressed through the combinator and reduced to a
specialization-stub cycle-052 D3 (vocabulary-shift-redirect refactor pass). The named-leaf
presence is retained so the firm L3 [`dot`](../L3/dot.md) lowers to an adjacent same-named L2
parent (CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**).

## Evidence

`dot`'s unique L0 anchors (RETAINED — the conjugation variant-axis and self-dot evidence the
combinator does not carry; paths relative to `reference/palace/`; self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation). All other L0 evidence is the
combinator's / the firm L1 leaf's:

- [`book/src/L2/inner_product.md`](./inner_product.md) (firm cycle-050) — the combinator this
  leaf specializes; §"Specializations" (the conjugation/element-type/weight recovery), §"Fusion
  note", §Signature. All deferred semantics/laws/fusion content lives here.
- [`book/src/L1/dot.md`](../L1/dot.md) (firm cycle-002) — authoritative on the Palace surface,
  the receiver-vs-argument conjugation asymmetry, the self-dot fast path, and the complete L0
  evidence list.
- [`book/src/L3/dot.md`](../L3/dot.md) (firm cycle-011) — the L3 specialization this floor sits
  under.
- `palace/linalg/vector.hpp:110-113` — `ComplexVector::Dot` decl, comment `// Vector dot
  product (yᴴ x) or indefinite dot product (yᵀ x) for complex vectors.`; `TransposeDot`
  alongside. **Self-verified (anchor `Dot` at :111-113).**
- `palace/linalg/vector.cpp:263-267` — `ComplexVector::Dot` body = `x·conj(y) = yᴴ x`, with the
  `&y==this` imag=`0.0` self-dot fast path at `:266` (the PSD-at-diagonal confirmation).
  **Self-verified (anchor `Dot` at :263; `0.0` at :266).**
- `palace/linalg/vector.cpp:269-274` — `ComplexVector::TransposeDot` body: unconjugated
  bilinear, negated imaginary cross-term — the `tdot` kernel. **Self-verified (anchor
  `TransposeDot` at :269).**
- `test/unit/test-vector.cpp:206-207` — real-vector dot via `operator*`: `double dot = vec1 *
  vec2; CHECK_THAT(dot, WithinRel(32.0));` (`1·4+2·5+3·6=32`). Direct value-asserting test.
  **Self-verified (anchor `WithinRel` at :207).**
- [`book/src/concepts/dot.md`](../concepts/dot.md) — the cross-cutting concept page; BLAS-1
  heritage framing.
```

### (i-b) L3/dot.md → specialization-stub

```edit:book/src/L3/dot.md
[old]: # dot

Whole-tensor inner-product reduction at L3: `α = ⟨x, y⟩`. The canonical BLAS-1 reduction primitive rendered as an L3 field operation; the workhorse of Krylov coefficient computation and orthogonalization at the iteration-rotation layer. **`dot` is the Hermitian/symmetric specialization (at `M = I`) of the L3 [`inner_product`](./inner_product.md) combinator**; this entry adds the leaf-level iteration-rotation framing (the conjugation choice, the consuming `krylov-step` context) rather than re-deriving the reduce-to-scalar base form, which is the combinator's (§"Downward to L2 (through inner_product)").

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as `state' = f(state, params)`, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `dot` at L3 is a whole-tensor reduction — its signature `(x: Tensor[N], y: Tensor[N]) -> Scalar` exposes no element loop; the reduction over the length axis `N` is a single semantic step at L3.

`dot` does **not** re-derive the reduce-to-scalar base form: it **speaks through** the L3 [`inner_product`](./inner_product.md) combinator (firm cycle-050), of which it is the conjugation-axis specialization `dot(x, y) = inner_product x y` at the Hermitian (complex) / symmetric (real) kernel value, with `M = I`. The combinator IS the L3 entry for the reduce-to-scalar inner-product family (per CLAUDE.md §Methodology invariants ⟢ — the combinator is the entry, members are specialization notes); this `dot` chapter is the named workhorse specialization the combinator's §"Specializations" points back at (`book/src/L3/inner_product.md:148-152`). It adds the leaf-level facts the family-level combinator does not carry: the value-bearing conjugation choice (below), the `tdot` co-defined unconjugated variant, and the leaf's consumption inside the `krylov-step` body.

The companion concept page [`concepts/dot`](../concepts/dot.md) carries the BLAS-1 heritage framing and the cross-cutting prose treatment; the L1 entry [`L1/dot`](../L1/dot.md) is authoritative on every factual claim about the Palace surface. This L3 entry does not duplicate algebraic-law content; the laws hold uniformly across the chain because the body is identity-in-form through the combinator (§"Downward to L2 (through inner_product)").

The conjugation convention is **value-bearing for complex vectors**: the L1/L2/L3 Hermitian `dot` is conjugate-linear in the first argument (`⟨x, y⟩ = xᴴ y`), carried through unchanged at L3. The L0 free-function asymmetry — `linalg::Dot(comm, x, y) = yᴴ x` per `vector.cpp:674-685`, conjugating the second argument — produces the complex-conjugate value `yᴴ x` (not `xᴴ y`); reconciling that re-order is the genuine translation carried by the KEPT L2>L1 [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) theme (documented at `book/src/L1/dot.md:43, 104-105`), not L3 content. L3 sees the convention pinned at arg-1.

## Signature

    dot   :: Tensor[N] -> Tensor[N] -> Scalar
    tdot  :: Tensor[N] -> Tensor[N] -> Scalar     -- complex-only variant

Two operators in one chapter because they share the entire reduction skeleton (sum over `N`) and differ only by the per-element kernel. The L3 signature is identical to the L1 signature; only the surrounding layer's vocabulary differs.

Shape contract (positional values; bunsen-style named axes; no element loop exposed at L3):

- **`x`** — `Tensor[N]` — read-only whole-tensor argument; the first (conjugated, for Hermitian variant) argument in the Hermitian inner product `xᴴ y`.
- **`y`** — `Tensor[N]` — read-only whole-tensor argument; the second (linear) argument in the Hermitian inner product.
- **result** — `Scalar` — element type follows the L1 rule (real `dot` → real; complex `dot` → complex; complex `tdot` → complex; see [`L1/dot`](../L1/dot.md) §Signature for the full element-type → return-type table).
- `x` and `y` must share the length axis `N` and the element type.

Per-element kernel by element-type (inherited from L1; reproduced for L3 reader coherence):

| element type | `dot(x, y)` returns | per-element kernel |
|---|---|---|
| `real`    | `real`    | `x[i] * y[i]` |
| `complex` | `complex` | `conj(x[i]) * y[i]` *(Hermitian, conjugate-linear in first arg)* |
| `complex` (via `tdot`) | `complex` | `x[i] * y[i]` *(unconjugated bilinear)* |

No element loop is exposed at L3 — the reduction over `i ∈ [0, N)` is a single semantic step in the L3 calculus. This is what makes `dot` L3-native by signature shape (per `book/src/L3-L2/krylov-step-body-identity.md:97`).

## Semantics

Whole-tensor reduction: `dot(x, y) = Σ_{i ∈ [0, N)} kernel(x[i], y[i])` with the per-element kernel from the table above. At L3 this is rendered as a single semantic step — the reduction is **one node in the iteration-rotation calculus**, not a loop.

Conjugation convention (complex `dot`): conjugate-linear in the **first** argument, linear in the second. This matches the standard mathematical Hermitian inner product `⟨x, y⟩ = xᴴ y`. Inherited unchanged from [`L1/dot`](../L1/dot.md) §Semantics.

Reduction-tree non-associativity is **load-bearing** in the CLAUDE.md sense — floating-point summation is non-associative, so different reduction trees produce different bit-level results. Inherited unchanged from L1 as a non-law (see §Algebraic laws below). The trade-offs reappear in the L1>L0 lowering (`apply-linop-mutation-rotation` sister-theme structure; not applicable here because `dot` is a reduction, not a destination-bearing op).

The MPI collective is **not** in the L3 signature — single-rank is in scope per CLAUDE.md §Scope; MPI ranks are read as their single-rank equivalents. The reduction at L3 is a single step; the local-then-collective two-step reappears only in the L1>L0 lowering at L1. L3 sees a global reduction in one step; the lift from L1 to L3 does not introduce or remove MPI structure.

### Iteration-rotation marker

L3 is the iteration-rotation layer, and `dot`'s iteration view is the reduction over the length axis `N`. **The reduction lifts as a whole-tensor operation** — the signature `Tensor[N] -> Tensor[N] -> Scalar` exposes no element loop, and the reduction-tree shape is opaque at L3 (the bit-level non-associativity is a recorded non-law, not a structural element of the L3 form). There is **no sequential obstruction** for `dot` — the reduction over independent length-axis indices is a parallel operation in exact arithmetic; the load-bearing pinned tree at L0 is a floating-point implementation choice, not an algebraic obstruction at L3.

`dot` is **consumed inside** larger L3 forms — most notably the `krylov-step` body (per `book/src/L3/krylov-step.md` §Semantics, the iterate-and-scalar update sub-composition; the L3 form at `book/src/L3-L2/krylov-step-body-identity.md:30-37` shows `dot` in the per-step let-chain). At L3 `dot` is a leaf reduction; the iteration view is what the surrounding `krylov-step` body provides, not what `dot` itself contributes.

## Algebraic laws

The L3 algebraic laws are **inherited unchanged from L1** because the L3 form is value-thread-isomorphic to the L1 form. Inheritance is total: every L1 law for `dot` and `tdot` holds at L3 with the same statement, and every L1 non-law remains a non-law at L3. The laws are reproduced here so the L3 reader does not have to reach to L1 for the listing.

**For `dot` over real element-type (bilinear symmetric form):**

1. **Symmetry**: `dot(x, y) = dot(y, x)`.
2. **Bilinearity (left)**: `dot(α·x₁ + x₂, y) = α·dot(x₁, y) + dot(x₂, y)`.
3. **Bilinearity (right)**: `dot(x, α·y₁ + y₂) = α·dot(x, y₁) + dot(x, y₂)`. (Follows from 1 + 2.)
4. **Positive semi-definite at `y = x`**: `dot(x, x) ≥ 0`, with equality iff `x = 0` (in exact arithmetic).
5. **Zero in either argument**: `dot(0, y) = dot(x, 0) = 0`.

**For `dot` over complex element-type (Hermitian sesquilinear form, conjugate-linear in first arg):**

6. **Hermitian symmetry**: `dot(x, y) = conj(dot(y, x))`.
7. **Conjugate-linearity (left)**: `dot(α·x₁ + x₂, y) = conj(α)·dot(x₁, y) + dot(x₂, y)`.
8. **Linearity (right)**: `dot(x, α·y₁ + y₂) = α·dot(x, y₁) + dot(x, y₂)`.
9. **Positive semi-definite at `y = x`**: `dot(x, x) ∈ ℝ` and `dot(x, x) ≥ 0`, with equality iff `x = 0` (in exact arithmetic).
10. **Zero in either argument**: `dot(0, y) = dot(x, 0) = 0`.

**For `tdot` over complex element-type (unconjugated bilinear form):**

11. **Symmetry**: `tdot(x, y) = tdot(y, x)`.
12. **Bilinearity in each argument** (analogue of laws 2–3 with no conjugation).
13. **Not positive semi-definite**: `tdot(x, x) ∈ ℂ` in general; in particular `tdot(x, x) = 0` does **not** imply `x = 0` (e.g. `x = (1, i)` gives `tdot(x, x) = 1·1 + i·i = 0`). Recorded as the explicit absence: `tdot` is the indefinite form Palace exposes for algorithms that require it, distinct from `dot`.

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Associativity of the reduction-tree** in floating point — different summation orders give different bit-level results. Load-bearing per CLAUDE.md §"Optimization tricks vs. base algebra". The mathematical law `(a + b) + c = a + (b + c)` holds in ℝ / ℂ but not in IEEE-754.
- **Strictness of Cauchy–Schwarz in floating point**: `|dot(x, y)|² ≤ dot(x, x) · dot(y, y)` holds mathematically but can fail by ULP-level amounts due to summation ordering.
- **Distributivity over vector-multiplication structure**: not applicable — `dot` is not a binary operator on vectors closing back to vectors; it's a reduction to a scalar.

## Dependencies

**Same-layer (L3)**: none. `dot` is a leaf reduction at L3 — alongside [`nrm2`](./nrm2.md) it is one of the two BLAS-1 reduction floor primitives at the iteration-rotation layer. Its sub-operations are scalar multiplication, scalar conjugation (complex case only), and scalar addition — all at or below the L3 layer's resolution.

**Consumers (L3)**: [`krylov-step`](./krylov-step.md) — the per-step body's iterate-and-scalar-update sub-composition `krylov_update` consumes `dot` for scalar-stratum updates (CG's `α = dot(r, z) / dot(Ap, p)`; GMRES's orthogonalization coefficients `dot(v_i, w)`; per `book/src/L3-L2/krylov-step-body-identity.md:30-37`).

**Cross-cutting concepts**:

- [`dot`](../concepts/dot.md) — the cross-cutting concept page with BLAS-1 heritage framing.

**Combinator (L3)**: [`inner_product`](./inner_product.md) (firm cycle-050) — the reduce-to-scalar inner-product combinator this entry is the Hermitian/symmetric specialization of; authoritative on the family-level reduce-to-scalar base form, the reduction-monoid-homomorphism law, and the no-sequential-obstruction verdict. This `dot` chapter does not re-derive the base form; it adds the leaf-level conjugation / consuming-context framing.

**Genuine L2>L1 translation**: [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) (firm cycle-019, KEPT cycle-049 D2) — the conjugation/element-type/weight dispatch + the `xᴴ y` ↔ `yᴴ x` re-order + the per-call pinned reduction trees; the home for all `dot`-specialization fusion/re-order content.

**L1 anchor**: [`L1/dot`](../L1/dot.md) (firm cycle-002) — the L1 entry is authoritative on the Palace surface details, the receiver-vs-argument asymmetry on the L0 method form, the self-dot fast path (`&y == this`), and the complete L0 evidence list. This L3 entry does not duplicate those details.

## Variant axes

Inherited unchanged from L1:

1. **element-type** (`real` | `complex`) — at L0 these are separate functions / overloads; at L1 / L3 they collapse to one operator parameterised by element type, with the Hermitian-vs-bilinear distinction handled by the per-element kernel.
2. **conjugation convention** (complex element-type only): `hermitian` (the default `dot`) | `unconjugated` (the separate operator `tdot`). At L1 / L3 these are distinct operators (sharing only the reduction skeleton), because the algebraic laws differ — `dot` is positive semi-definite at `y = x`, `tdot` is not.

No new variant axes introduced at L3. No axes merged or split. The L1 conjugation-convention axis is preserved as the `dot` vs `tdot` distinction; the L1 element-type axis is preserved as element-type parameterization of a single operator.

## Status

`firm` — `dot` is the Hermitian/symmetric specialization (at `M = I`) of the firm L3 [`inner_product`](./inner_product.md) combinator (firm cycle-050); the reduce-to-scalar base form, algebraic laws, and no-sequential-obstruction verdict are inherited unchanged from the combinator (this chapter adds the leaf-level conjugation / consuming-context framing). Variant-axis profile inherited unchanged at two axes (element-type, conjugation-convention). The entry exists as a **layer-coherence anchor** per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** (cycle-009 codification) AND as the named workhorse specialization the combinator's §"Specializations" points back at (CLAUDE.md §Methodology invariants ⟢ — the combinator is the entry, members are specialization notes). Originally harvested cycle-011 wave-1 (BLAS-1 reduction cohort backfill); re-expressed through the `inner_product` combinator cycle-051 (vocabulary-shift-redirect refactor-pass — the two degenerate `dot-body-identity` / `dot-leaf-identity` themes demoted into the combinator's pre-built homes the same cycle).

## Downward to L2 (through inner_product)

L3 `dot` lowers **through the L3 [`inner_product`](./inner_product.md) combinator**, of which it is the Hermitian/symmetric specialization (`dot(x, y) = inner_product x y` at the conjugated kernel, `M = I`). The combinator lowers to L2 [`inner_product`](../L2/inner_product.md) as **identity-in-form on the body** (value-thread-isomorphic reduce-to-scalar reduction; no L3-L2 theme file — the in-line §"Downward to L2" at `book/src/L3/inner_product.md:363-385` is the home, per the cycle-012 non-adjacent-identity convention). There is no separate `dot`-specific L3>L2 theme: the former degenerate `dot-body-identity` theme was a `dot`-named restatement of that body identity and was demoted into the combinator's pre-built §"Downward to L2" home (cycle-051 vocabulary-shift-redirect refactor-pass).

The **genuine** translation in the chain is the KEPT L2>L1 [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) theme — it carries the conjugation/element-type/weight dispatch, the value-level `xᴴ y` ↔ `yᴴ x` re-order (the value-bearing conjugation reconciliation for complex `dot`), and the per-call pinned reduction trees (the load-bearing IEEE-754 non-law). The `dot` specialization is the plain (`M = I`) Hermitian / symmetric member of that fold's conjugation dispatch; bit-reproduction / re-order / reduction-tree concerns are read off the fold-specialization theme, not re-derived here. The MPI collective and the local-then-collective `LocalDot ∘ Mpi::GlobalSum` two-step are L1>L0 lowering content (folded out per single-rank scope); the L3 form sees a single-step whole-tensor reduction.

## Lifts from

`dot` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010 audit verdict at `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"Per-candidate verdict" (2): "leaf primitives don't get L4 rows"). At L4, `dot` appears inside larger composed entries (e.g., `book/src/L4/krylov-step.md` §Semantics) as a let-binding consuming the L3-native primitive surface; it carries no monadic effect, no state-stratification typing, no novel calculus content at L4.

## Evidence

The L3 form is the Hermitian/symmetric specialization of the firm L3 `inner_product` combinator; all L0 evidence is inherited transitively (through the combinator, and through the firm L1 leaf). Direct citations relevant to this L3 entry:

- [`book/src/L3/inner_product.md`](./inner_product.md) (firm cycle-050) — the combinator this entry specializes; authoritative on the family-level reduce-to-scalar base form, the reduction laws (inherited unchanged here), and the no-sequential-obstruction verdict. §"Specializations" (`:148-152`) names this `dot` chapter as the workhorse Hermitian/symmetric specialization.
- [`book/src/L2-L1/inner-product-fold-specialization.md`](../L2-L1/inner-product-fold-specialization.md) (firm cycle-019, KEPT cycle-049 D2) — the genuine L2>L1 translation; the conjugation/element-type/weight dispatch + `xᴴ y` ↔ `yᴴ x` re-order + pinned reduction trees the `dot` specialization's fusion/re-order content is read off.
- [`book/src/L1/dot.md`](../L1/dot.md) (firm cycle-002) — authoritative on Palace surface, signature, algebraic laws (inherited unchanged at L3), variant axes (inherited unchanged at L3), and the complete L0 evidence list (`vector.hpp:110-113`, `vector.hpp:242-253`, `vector.cpp:263-274`, `vector.cpp:665-685`, etc.).
- [`book/src/L3/index.md`](./index.md) line 13 — the L3 vocabulary inventory explicitly names `dot` as an L3 field operation. This L3 entry closes the inventory-vs-content gap noted by the cycle-010 audit.
- [`book/src/L3/krylov-step.md`](./krylov-step.md) §Semantics — the consuming context at L3; the per-step body's iterate-and-scalar update sub-composition consumes `dot` for scalar-stratum updates.
- [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 — the load-bearing statement that the seven L1 primitives (including `dot`) are L3-native by signature shape: "each operates on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step (each L1 primitive is *also* L3-native because its signature has no per-element loop visible)." This is the structural justification for the L3>L1 identity-in-form rotation.
- [`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)" — the L3 body let-chain renders `dot` as an L3-native primitive call identical in shape to its L1 signature.
- [`book/src/concepts/dot.md`](../concepts/dot.md) — the cross-cutting concept page; the BLAS-1 heritage framing.
- `palace/linalg/iterative.cpp:395, 404, 444, 460` — CG using `linalg::Dot` for `β = ⟨z, r⟩` and the α-denominator `⟨z, p⟩`; the consuming context for `dot` at L0, inherited transitively. (Path relative to `reference/palace/`.)
- `test/unit/test-orthog.cpp:157, 219-220, 271, 313-315, 373-376` — `linalg::Dot` used as the orthogonalization-coefficient primitive in MGS and CGS; L0-equivalent semantic documentation per CLAUDE.md §"Tests as semantic supplement", inherited transitively. (Path relative to `reference/palace/`.)
- Cycle-010 audit at [`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`](../../../reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md) §"Per-candidate verdict" (2) — HIGH CONFIDENCE backfill recommendation for the BLAS-1 cohort at L3, including `dot`. This entry is the enactment.

## L3 vs L1 distinction

- **L1**: pure functional reduction `α = dot(x, y)`. Mutation-rotation layer — the L0 destination buffer is erased from the signature (a `dot` returns a scalar; there is no destination buffer to mutate); the MPI collective is folded into the L1>L0 lowering. The receiver-vs-argument asymmetry on the L0 method form is erased (the L1 signature names the conjugated argument first by convention). Reduction-tree non-associativity recorded as a load-bearing algebraic claim.
- **L3**: the Hermitian/symmetric specialization of the `inner_product` combinator, rendered as a whole-tensor reduce-to-scalar field operation `α = dot(x, y)`. Iteration-rotation layer — the surrounding consuming context (the `krylov-step` body) renders the iteration view explicitly as `(K, s) -> (K', s')` value-threading; `dot` itself is consumed as a leaf reduction with no iteration view of its own. The reduce-to-scalar base form is the combinator's; this chapter adds the leaf-level conjugation / consuming-context framing.

The L3 entry exists for layer-coherence — a reader at L3 navigating the `krylov-step` body or the L3 vocabulary inventory must find `dot` defined in L3 vocabulary at L3, per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** — and as the named workhorse specialization the `inner_product` combinator's §"Specializations" points back at (CLAUDE.md §Methodology invariants ⟢).
[new]: # dot

> **Specialization-stub (reduced cycle-052 D3, vocabulary-shift-redirect refactor pass).**
> `dot` at L3 is the **`M = I` Hermitian/symmetric specialization** of the L3 combinator
> [`inner_product`](./inner_product.md) (firm cycle-050) — the combinator IS the L3 entry for
> the reduce-to-scalar inner-product family; `dot` is a **specialization note** under it (per
> CLAUDE.md §Methodology invariants ⟢ — the combinator is the entry, members are
> specialization notes). This chapter is reduced to the leaf-level facts the combinator does
> not carry: the value-bearing conjugation choice (`dot` Hermitian vs `tdot` unconjugated) and
> the leaf's consumption inside the `krylov-step` body. Semantics, algebraic laws, the
> no-sequential-obstruction verdict, and the downward lowering are **deferred** to the
> combinator [`inner_product`](./inner_product.md) §"Specializations" + §"Downward to L2".

Whole-tensor inner-product reduction at L3: `α = ⟨x, y⟩`, rendered as the Hermitian/symmetric
specialization of the L3 [`inner_product`](./inner_product.md) combinator at the conjugated
kernel value with `M = I`:

    dot(x, y)  = inner_product x y          -- Hermitian (complex) / symmetric (real)
    tdot(x, y) = inner_product x y          -- with the unconjugated kernel (complex-only)

The combinator carries the reduce-to-scalar base form, the algebraic laws, and the
no-sequential-obstruction verdict; this `dot` chapter adds only the leaf-level conjugation /
consuming-context framing. **Do NOT merge into `inner_product`** — the named-specialization
presence is what lets a reader navigating the `krylov-step` body or the L3 vocabulary inventory
find `dot` in L3 vocabulary (CLAUDE.md §Methodology invariants **Identity-lowerings still
require both L levels**).

## Signature

    dot   :: Tensor[N] -> Tensor[N] -> Scalar
    tdot  :: Tensor[N] -> Tensor[N] -> Scalar     -- complex-only variant

The combinator's signature read at the plain (`M = I`) conjugation value; identical to the L1
signature. Full shape contract: [`inner_product`](./inner_product.md) §Signature.

## Conjugation variant-axis (the leaf-level fact, value-bearing for complex vectors)

The conjugation convention is **value-bearing for complex vectors** and is the one fact this
specialization carries beyond the combinator. `dot` is **conjugate-linear in the first
argument**, linear in the second (`⟨x, y⟩ = xᴴ y`); `tdot` is the unconjugated co-variant. The
per-element kernel by element-type:

| element type | `dot(x, y)` returns | per-element kernel |
|---|---|---|
| `real`    | `real`    | `x[i] * y[i]` |
| `complex` | `complex` | `conj(x[i]) * y[i]` *(Hermitian, conjugate-linear in first arg)* |
| `complex` (via `tdot`) | `complex` | `x[i] * y[i]` *(unconjugated bilinear)* |

`dot` and `tdot` are distinct operators because their laws differ — `dot` is PSD-at-diagonal
(`dot(x, x) ≥ 0`), `tdot` is the indefinite form (`tdot(x, x) = 0` does not imply `x = 0`). The
L0 free-function asymmetry — `linalg::Dot(comm, x, y) = yᴴ x = conj(xᴴ y)` — and its reconciling
re-order are the genuine translation carried by the KEPT L2>L1
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) theme (firm
cycle-019, KEPT cycle-049 D2; documented at `book/src/L1/dot.md:43, 104-105`), not L3 content.
L3 sees the convention pinned at arg-1.

## Consuming context (the other leaf-level fact)

`dot` is **consumed inside** larger L3 forms — most notably the `krylov-step` body's
iterate-and-scalar update sub-composition (CG's `α = dot(r, z) / dot(Ap, p)`; GMRES's
orthogonalization coefficients `dot(v_i, w)`; per `book/src/L3-L2/krylov-step-body-identity.md:30-37`).
At L3 `dot` is a leaf reduction with no iteration view of its own; the iteration view is what the
surrounding `krylov-step` body provides.

## Status

`firm` — specialization-stub. `dot` at L3 is the `M = I` Hermitian/symmetric specialization of
the firm L3 [`inner_product`](./inner_product.md) combinator (firm cycle-050); the
reduce-to-scalar base form, algebraic laws, no-sequential-obstruction verdict, and downward
lowering are inherited from the combinator unchanged. This chapter retains only the
value-bearing conjugation variant-axis and the consuming-context framing. Originally harvested
cycle-011 wave-1 (BLAS-1 reduction cohort backfill); re-expressed through the combinator
cycle-051 (the degenerate `dot-body-identity` / `dot-leaf-identity` themes demoted into the
combinator's homes the same cycle); reduced to a specialization-stub cycle-052 D3
(vocabulary-shift-redirect refactor pass). The named-leaf presence is retained per CLAUDE.md
§Methodology invariants **Identity-lowerings still require both L levels** and as the named
workhorse specialization the combinator's §"Specializations" points back at (⟢).

## Downward to L2 (through inner_product)

L3 `dot` lowers **through the L3 [`inner_product`](./inner_product.md) combinator** — the
combinator lowers to L2 [`inner_product`](../L2/inner_product.md) as identity-in-form on the body
(in-line §"Downward to L2" at the combinator, per the cycle-012 non-adjacent-identity
convention). There is no separate `dot`-specific L3>L2 theme (the former degenerate
`dot-body-identity` theme was demoted into the combinator's §"Downward to L2" home cycle-051).
The genuine translation in the chain is the KEPT L2>L1
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) theme
(conjugation/element-type/weight dispatch + the `xᴴ y` ↔ `yᴴ x` re-order + per-call pinned
reduction trees). Bit-reproduction / re-order / reduction-tree concerns are read off the
fold-specialization theme, not re-derived here.

## Lifts from

`dot` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010
audit verdict). At L4, `dot` appears inside larger composed entries (e.g.,
`book/src/L4/krylov-step.md` §Semantics) as a let-binding consuming the L3-native primitive
surface.

## Evidence

`dot`'s deferred-to homes + leaf-level anchors (RETAINED). All semantics/laws/lowering evidence
is the combinator's / the firm L1 leaf's:

- [`book/src/L3/inner_product.md`](./inner_product.md) (firm cycle-050) — the combinator this
  entry specializes; §"Specializations" (`:133`) names this `dot` chapter as the workhorse
  Hermitian/symmetric specialization; authoritative on the base form, laws, and
  no-sequential-obstruction verdict (all deferred here).
- [`book/src/L2-L1/inner-product-fold-specialization.md`](../L2-L1/inner-product-fold-specialization.md) (firm cycle-019, KEPT cycle-049 D2) — the genuine L2>L1 translation; the conjugation/element-type/weight dispatch + `xᴴ y` ↔ `yᴴ x` re-order + pinned reduction trees.
- [`book/src/L1/dot.md`](../L1/dot.md) (firm cycle-002) — authoritative on Palace surface,
  signature, algebraic laws, variant axes, and the complete L0 evidence list (`vector.hpp:110-113`,
  `vector.cpp:263-274`, `vector.cpp:665-685`, etc.).
- [`book/src/L3/krylov-step.md`](./krylov-step.md) §Semantics + [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 — the consuming context + the structural justification (`dot` L3-native by signature shape).
- `palace/linalg/iterative.cpp:395, 404, 444, 460` — CG using `linalg::Dot` for `β = ⟨z, r⟩` and the α-denominator `⟨z, p⟩`; the consuming context at L0, inherited transitively. (Path relative to `reference/palace/`.)
- [`book/src/concepts/dot.md`](../concepts/dot.md) — the cross-cutting concept page; BLAS-1 heritage framing.
```

### (ii-a) L2/nrm2.md → consumer-stub

```edit:book/src/L2/nrm2.md
[old]: # nrm2

Euclidean-norm reduction rendered at L2 (the fusion-rotation layer): `α = ‖x‖₂ = √⟨x, x⟩`. The canonical BLAS-1 norm primitive written as the algebraic composition `√ ∘ abs ∘ inner_product` over the length axis, with HPC/SIMD optimization tricks unfolded (here: none to unfold — Palace's `linalg::Norml2` is already the one-line unfolded form). Identity-in-form lowering to L1 [`nrm2`](../L1/nrm2.md); the fusion-rotation work that L2 nominally performs (unfold fused kernels into base-algebra composition) is a **no-op on the buffer side** for this leaf, so the entry exists primarily as a **layer-coherence floor** — present so the firm L3 [`nrm2`](../L3/nrm2.md) rests on an adjacent L2 parent.

## Context

L2 is the **fusion-rotation** layer: each operation is written as a composition of base tensor / operator / quadrature primitives, with cache-blocked loops, SIMD intrinsics, packed formats, and batched specialized BLAS calls **unfolded back into the base algebras** (per [`L2/index`](./index.md) §Context). For `nrm2` there is **no fusion trick to unfold** — Palace's `linalg::Norml2` is a one-line free-function template whose body `std::sqrt(std::abs(Dot(comm, x, x)))` is *already* the base-algebra composition. The L2 rendering therefore adds no decomposition over the L1 form; it adds the **fusion-rotation framing** — naming `nrm2` as the `√ ∘ abs ∘ inner_product` composition in L2 vocabulary — and preserves the one load-bearing numerical trick (the `std::abs` guard) as an explicit algebraic claim.

This entry is a **layer-coherence floor** per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009 meta-phase). The L2 form is value-thread-isomorphic to the L1 form — the rotation L2→L1 is identity-in-form on the primitive's signature; only the surrounding layer's framing differs (fusion-rotation view at L2 vs. mutation-rotation view at L1). The floor exists under the 2026-05-31 foundation-first directive (`l2-floor-under-l3-leaf-cohort`): the firm L3 [`nrm2`](../L3/nrm2.md) (cycle-011) must rest on a *present* adjacent L2 parent, not skip a layer.

The L1 entry [`L1/nrm2`](../L1/nrm2.md) (firm cycle-003) is **authoritative on every factual claim about the Palace surface** — in particular: Palace's `linalg::Norml2` computes the naive `√⟨x, x⟩` via `Dot`, **not** the BLAS scaled-summation algorithm (the [`concepts/nrm2`](../concepts/nrm2.md) page's claim to the contrary is a correction-pending item noted at `book/src/L1/nrm2.md:11`). This L2 entry does not duplicate the L0 evidence list or the algebraic-law derivations; it states the laws (which hold uniformly across L1 / L2 / L3 because the body is identity-in-form across the chain) and cites the L1 entry as the anchor.

### Consumer of `inner_product`, NOT a fold member (load-bearing)

The L2 fold-cohort comprises two reductions sharing a `foldl` skeleton: [`inner_product`](./inner_product.md) folds the **length axis** to a `Scalar`, and [`linear_combination`](./linear_combination.md) folds the **term axis**, keeping `Tensor[N]` (per [`L2/index`](./index.md) §"Fold cohorts"). **`nrm2` is a CONSUMER of `inner_product`, not an instance of it:**

    nrm2(x) = √ (abs (inner_product(x, x)))        -- √ ∘ abs ∘ inner_product at y = x

`nrm2` post-composes the scalar square-root (and the defensive `abs`) onto the `inner_product` fold at the diagonal `y = x`; it does not itself fold. Merging `nrm2` into `inner_product` would be a category error — `inner_product` is the length-axis homomorphism producing `dot(x, x)`; `nrm2` is the scalar map `α ↦ √|α|` applied to that fold's output. The do-NOT-merge boundary is carried in the [`inner_product`](./inner_product.md) dep-map row ("Consumer (NOT an instance): `nrm2` / `matrix-weighted-norm` = `√ ∘ inner_product` at `y=x`") and in [`L2/index`](./index.md) §"Fold-cohort boundary". This entry honors that boundary: it lists `inner_product` under `consumes`, never under "this operator IS a member of the fold".

The B-weighted overload `linalg::Norml2(comm, x, B, Bx) = √(xᴴ B x)` (`palace/linalg/operator.cpp:600-619`, declared `palace/linalg/operator.hpp:372-374`) is **not** part of this operator (per the L1 entry's boundary documentation at `book/src/L1/nrm2.md:13`). It is the operator-weighted energy norm — a separate L2 candidate consuming the M-weighted member of `inner_product` (`inner_product_M(x, M, x) = xᴴ M x`) rather than the plain fold — tracked as rough-in [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1. At L2 the same boundary holds: `nrm2` is the unweighted Euclidean reduction.

## Signature

    nrm2 :: Tensor[N] -> Scalar
    nrm2(x) = √⟨x, x⟩ = √ (abs (inner_product(x, x)))

The L2 signature is identical to the L1 and L3 signatures; only the surrounding layer's framing differs.

Shape contract (bunsen-style, named axis; no element loop exposed at L2 — the fusion rotation erases any inner SIMD/blocked loop):

- **`x`** — `Tensor[N]` — read-only whole-tensor argument.
- **result** — `Scalar` — **always real-valued** (`real`), regardless of whether `x` is real or complex.
- The result is non-negative: `nrm2(x) ≥ 0`.

The "result is always real" rule is load-bearing — it is what makes the element-type axis collapse to a single L2 operator (in contrast to `dot` / `inner_product`, where the result element-type tracks the input). It follows from the fact that `inner_product(x, x) = dot(x, x)` is a non-negative real scalar for both real (L1 dot law 4) and complex (L1 dot law 9) inputs.

No element loop is exposed at L2 — the reduction over `i ∈ [0, N)` is the `inner_product` fold's single semantic step, and the post-composed `abs` and `√` are scalar operations on its output. This is what makes `nrm2` a clean L2 composition by signature shape (the seven BLAS-1 primitives including `nrm2` are L2-native / L3-native because their signatures have no per-element loop visible, per `book/src/L3-L2/krylov-step-body-identity.md:97`).

## Semantics

Fusion-rotation composition with defining identity: `nrm2(x) = √ (abs (inner_product(x, x)))`, the principal (non-negative) square root of the (defensively sign-stripped) Hermitian self-inner-product. At L2 the reduction is the `inner_product` fold over the length axis; `nrm2` post-composes two scalar maps onto it.

For real element-type: `nrm2(x) = √Σ_i x[i]²`.

For complex element-type: `nrm2(x) = √Σ_i |x[i]|² = √Σ_i (re(x[i])² + im(x[i])²)`. The Hermitian self-inner-product `inner_product(x, x) = Σ_i conj(x[i])·x[i] = Σ_i |x[i]|²` is real and non-negative element-wise. Inherited unchanged from [`L1/nrm2`](../L1/nrm2.md) §Semantics.

**The `std::abs` defensive guard is preserved as an explicit load-bearing numerical claim** (L2 discipline: load-bearing numerical tricks survive the fusion rotation as explicit algebraic claims, per [`L2/index`](./index.md) §Semantics). It is a no-op in exact arithmetic (the self-inner-product is non-negative real, so `abs` of it equals it) but **load-bearing in floating point**, where it strips a sign that round-off in the reduction could have flipped negative on a numerically-zero vector, buying **domain-safety for `√` (no NaN)**. The full classification (load-bearing-defensive, property-it-buys = non-negativity invariant for the square root) lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive guard — classification". At L2 it is named as a preserved scalar guard composed onto the fold output; at L1 it is recognized as a floating-point implementation detail that disappears (the algebraic claim that `inner_product(x, x)` is non-negative real subsumes it). Both treatments are consistent: the guard *implements* the non-negativity claim under floating point.

Reduction-tree non-associativity is **load-bearing** — inherited unchanged from the `inner_product` fold (and through it from `dot`). The square root and `abs` are deterministic IEEE-754 scalar operations (correctly rounded), so `nrm2`'s non-determinism is entirely the fold's. Recorded as a non-law (see §Algebraic laws).

The MPI collective is **not** in the L2 signature — single-rank is in scope per CLAUDE.md §Scope. The reduction at L2 is a single fold step; the local-then-collective two-step reappears only in the L1>L0 lowering (at the `inner_product` / `dot` leaf, per [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"L0 form (RHS)").

## Algebraic laws

The L2 algebraic laws are **inherited unchanged from L1** because the L2 form is value-thread-isomorphic to the L1 form. Inheritance is total: every L1 law for `nrm2` holds at L2 with the same statement, and every L1 non-law remains a non-law at L2. The laws are reproduced here so the L2 reader does not have to reach to L1 for the listing.

The laws below hold for both real and complex element-types of `x`; absences are deliberate.

1. **Non-negativity**: `nrm2(x) ≥ 0` for all `x`.
2. **Positive-definite (separation)**: `nrm2(x) = 0` iff `x = 0` (in exact arithmetic). The "iff" direction follows from `dot` law 4 / 9.
3. **Positive homogeneity (absolute scalar)**: `nrm2(α·x) = |α|·nrm2(x)` for any scalar `α` (real or complex). The absolute value is necessary on both sign and complex phase; the norm strips both.
4. **Triangle inequality**: `nrm2(x + y) ≤ nrm2(x) + nrm2(y)`.
5. **Reverse triangle inequality**: `|nrm2(x) − nrm2(y)| ≤ nrm2(x − y)`. (Follows from law 4.)
6. **Cauchy–Schwarz** (relating `nrm2` to `inner_product`): `|inner_product(x, y)| ≤ nrm2(x) · nrm2(y)`, with equality iff `x` and `y` are linearly dependent (in exact arithmetic).
7. **Parallelogram identity**: `nrm2(x + y)² + nrm2(x − y)² = 2·nrm2(x)² + 2·nrm2(y)²`. (Characterizes norms induced by an inner product; holds here because `nrm2` is defined as `√⟨·,·⟩`.)
8. **Self-inner-product identity**: `nrm2(x)² = inner_product(x, x)` (real and complex) — the defining identity, restated. This is the structural link that makes `nrm2` a *consumer* of the `inner_product` fold; CG-style algorithms reuse `inner_product(r, r)` instead of recomputing `nrm2(r)²`.
9. **Zero in argument**: `nrm2(0) = 0`. (Special case of law 2.)
10. **Phase invariance (complex)**: for complex `x` and any unit-modulus complex scalar `e^{iθ}`: `nrm2(e^{iθ}·x) = nrm2(x)`. (Special case of law 3 with `|α| = 1`.)

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Linearity in `x`**: `nrm2(α·x + β·y) ≠ α·nrm2(x) + β·nrm2(y)` in general. `nrm2` is sub-additive (law 4), not additive. This is the defining feature that distinguishes a norm from a linear functional.
- **Strictness of Cauchy–Schwarz in floating point**: law 6 can fail by ULP-level amounts due to summation ordering inside the `inner_product` fold (same load-bearing caveat as the fold). Algorithms that depend on the strict inequality (e.g. orthogonality-loss detection in MGS reorthogonalization) must guard.
- **Bit-determinism across reduction trees**: same load-bearing caveat as the `inner_product` fold — different reduction orders produce different bit-level `nrm2` values. The mathematical laws above hold; their floating-point realizations are exact modulo summation-order noise.
- **`abs`-erasability**: the `std::abs` guard is NOT erasable in floating point without introducing a NaN failure mode on numerically-zero vectors — it is a no-op in exact arithmetic only. (See §Semantics; full classification at the L1>L0 theme.)
- **Multiplicativity over the cross-element kernel**: `nrm2(x ⊙ y) ≠ nrm2(x) · nrm2(y)` in general — not applicable; `nrm2` is a reduction-consumer, not a binary algebra on vectors.

## Dependencies

**Consumes (L2, NOT a parent fold)**: [`inner_product`](./inner_product.md) (firm cycle-019) — `nrm2(x) = √ (abs (inner_product(x, x)))`, the post-composition of two scalar maps (`abs`, `√`) onto the length-axis fold at `y = x`. This is a **consumer** relationship, not membership: `nrm2` is explicitly NOT a member of the fold cohort (do-NOT-merge boundary per [`L2/index`](./index.md) §"Fold-cohort boundary"; the [`inner_product`](./inner_product.md) dep-map row names `nrm2` as a consumer, not an instance). The `inner_product` fold is the **only** L2 dependency; the outer `abs` and `√` are scalar operations below the L2 layer's resolution (deterministic IEEE-754 primitives operating on the single scalar the fold produces).

The fact that `nrm2` factors so cleanly through `inner_product` is exactly the kind of compositional structure the L2 layer is meant to expose at the fusion-rotation level; the L0 form makes the composition syntactically explicit (one line of source at `palace/linalg/vector.hpp:259`), and the L2 form names it as the defining identity (algebraic law 8) with `nrm2` as a downstream consumer of the fold.

**Consumers (L2)**: [`krylov-step`](./krylov-step.md) — the per-step body consumes `nrm2` for the residual-norm readout (CG, MINRES convergence test) and the Arnoldi sub-diagonal scalar (GMRES basis-vector normalization, `H[j+1,j] = nrm2(w)`); the [`krylov-step`](./krylov-step.md) dep-map row lists `nrm2` among its L1 primitives, here rendered at the L2 floor.

**Cross-cutting concepts**: [`nrm2`](../concepts/nrm2.md) — the cross-cutting concept page with BLAS-1 heritage framing (its scaled-summation stability claim is incorrect per the L1 correction-pending note at `book/src/L1/nrm2.md:11`; the L1 entry is authoritative). [`dot`](../concepts/dot.md) — referenced transitively through the `inner_product` fold the defining identity consumes.

**L1 anchor**: [`L1/nrm2`](../L1/nrm2.md) (firm cycle-003) — authoritative on the Palace surface details, the one-line `linalg::Norml2` template definition, the relationship to the B-weighted overload (separately tracked), and the complete L0 evidence list. This L2 entry does not duplicate those details; the L2>L1 rotation is identity-in-form on the primitive itself.

## Variant axes

Inherited unchanged from L1 at **one** axis:

1. **element-type** (`real` | `complex`) — at L0 these are template specializations of `linalg::Norml2<VecType>` (`VecType ∈ {Vector, ComplexVector}`). At L1 / L2 / L3 these **collapse to a single operator** with the same signature `Tensor[N] -> Scalar(real)`, because the result is real-valued regardless of input element type (the Hermitian self-inner-product is real per `dot` law 4 / 9), and the defining identity `nrm2(x) = √ (abs (inner_product(x, x)))` is shared across element types; the element-type dispatch is entirely absorbed by the `inner_product` fold (and through it by `dot`).

This is a stronger collapse than `inner_product`'s element-type axis: `inner_product` retains an element-type-tracking return scalar (real `dot` → real, complex `dot` → complex); `nrm2` does not, because the post-composed `abs` projects the complex self-inner-product `{re, 0.0}` onto its real magnitude before `√`.

No other variant axes at L2:

- **B-weighting**: not a variant of `nrm2` — it is a distinct operator (the operator-weighted energy norm `‖x‖_B = √(xᴴ B x)`) consuming the M-weighted member of `inner_product` (`inner_product_M(x, M, x)`) rather than the plain fold. Tracked as [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1 (rough-in cycle-010 wave-1). The L0 surface uses the same overloaded name `linalg::Norml2`, but the algebraic structure differs (requires an external `B`-application primitive, requires an SPD precondition on `B`, the workspace `Bx` is a load-bearing buffer at L0).
- **Stability variants**: BLAS-style scaled-summation `nrm2` (which avoids overflow/underflow at the cost of extra arithmetic) is **not present** in Palace's `linalg::Norml2` — Palace uses the naive `√⟨x, x⟩` form. Not a variant axis of the L2 operator.

## Status

`firm` — L2 form is value-thread-isomorphic to the L1 form (identity-in-form rotation); the fusion rotation is a no-op for this leaf (no HPC/SIMD trick to unfold — `linalg::Norml2` is already the one-line unfolded composition); algebraic laws inherited unchanged from L1; variant-axis profile inherited unchanged at one axis. The one genuinely-L2 content beyond identity is the fusion-rotation framing (`nrm2` as `√ ∘ abs ∘ inner_product` consumer of the fold, do-NOT-merge boundary honored) and the preservation of the `std::abs` load-bearing numerical guard as an explicit algebraic claim. The entry exists as a **layer-coherence floor** per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** (cycle-009 codification) under the 2026-05-31 foundation-first directive `l2-floor-under-l3-leaf-cohort`: it gives the firm L3 [`nrm2`](../L3/nrm2.md) (cycle-011) a present adjacent L2 parent. Harvested cycle-041 wave-1 (D2) as part of the L2-floor-under-L3-BLAS1-cohort backfill.

## Lowers to

L2 `nrm2` lowers to L1 [`nrm2`](../L1/nrm2.md) as **identity-in-form on the primitive's signature**. The fusion rotation L2→L1 is a no-op on the buffer side (there is no destination buffer for `nrm2` — the result is a returned scalar; per [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) the "mutation rotation" is essentially nothing on the buffer side, and the fusion rotation likewise has no fused kernel to unfold). The L2>L1 rotation is a degenerate identity-in-named-terms lowering, recorded in-line in §"Downward to L1" below rather than as a thin theme file (per the 2026-06-01 vocabulary-shift redirect). The L1>L0 lowering — Palace's `linalg::Norml2` template at `palace/linalg/vector.hpp:255-260` expanding into the four-stage `Dot → MPI_Allreduce → std::abs → std::sqrt` chain — lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md). None of that is L2 content; the L2 form sees a single-step fold consumed by two scalar maps.

### Downward to L1 (consumer identity-in-form; no theme file)

L2 `nrm2` re-fuses downward onto the single L1 leaf [`nrm2`](../L1/nrm2.md) (firm cycle-003) as **identity-in-form on the primitive's signature** — value-thread-isomorphic, with **no dispatch** (one L1 leaf — there is no L1 family to dispatch into, contrast the `dot`/`tdot` inner-product cohort), **no decomposition** (the L2 fusion rotation is a no-op — `linalg::Norml2` is already the one-line unfolded composition), and **no destination-buffer concern** (the result is a returned scalar). What the hop does is two surface adjustments, both value-preserving:

1. **The `inner_product` fold at `y = x` re-fuses to the `dot` leaf at the diagonal.** L2 names the inner reduction as the length-axis `inner_product` fold (firm cycle-019); at L1 the same diagonal self-inner-product is the `dot(x, x)` leaf (the defining identity `nrm2(x) = √dot(x, x)`, L1 algebraic law 8, `book/src/L1/nrm2.md:53`). This is the **consumer's** view of the edge [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) §"The diagonal degeneration (`y = x`)" lowers for the fold itself — that theme names `nrm2` precisely as the consumer entry point (`√ ∘ inner_product` at `y = x`, with the outer `√` a post-step "downstream of this lowering, not a dispatch within it"). The inner `inner_product(x, x) → dot(x, x)` re-fusion is inherited from the inner-product theme; the `nrm2`-specific content is the outer `√ ∘ abs` post-step. **`nrm2` is a CONSUMER of `inner_product`, not a fold member** (do-NOT-merge per [`L2/inner_product`](./inner_product.md) §"Consumer (NOT an instance)" and §"Consumer of `inner_product`, NOT a fold member" above); the namesake "fold" is the one `nrm2` *consumes* at `y = x`, not one it instantiates.
2. **The two scalar post-steps change framing, not value.** At L2 the `abs` guard is **preserved as an explicit load-bearing numerical claim** and the `√` is the principal non-negative real square root composed onto the fold output. At L1 both drop **below the layer's resolution**: the `abs` guard **disappears**, subsumed by the L1 algebraic claim that `dot(x, x)` is non-negative real (so `abs` of it equals it exactly in exact arithmetic), and the `√` is a deterministic IEEE-754 scalar primitive on the leaf's output ([`L1/nrm2`](../L1/nrm2.md) §Dependencies, `:66`). Both treatments are consistent — the guard *implements* the non-negativity claim under floating point; it is a no-op in exact arithmetic and is **NOT erasable in floating point** without introducing a NaN failure mode on numerically-zero vectors. The full load-bearing-defensive classification (property bought = domain-safety / non-negativity invariant for `√`, no NaN) lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive guard — classification", where the guard re-materializes as stage 3 of the four-stage `Dot → MPI_Allreduce → std::abs → std::sqrt` chain.

The mapping is total and trivial on the kernel content: the single L2 `nrm2` form maps to the single L1 `nrm2` leaf, same signature, same value, same defining identity (law 8). The element-type axis is collapsed identically at both layers (one operator, always-real result — the post-composed `abs` projects the complex self-inner-product onto its real magnitude before `√`). This is the **identity-in-form** property; the rotation is at the framing (preserved-`abs` fusion-rotation view at L2 → absorbed-`abs` mutation-rotation view at L1), not on the primitive.

L0 anchor (transitive through L1; verified on-disk this dispatch via `citecheck --anchor Norml2`): `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template; body line 259 is `return std::sqrt(std::abs(Dot(comm, x, x)));`. The one-line unfolded composition that makes the L2>L1 fusion rotation a no-op. (Path relative to `reference/palace/`; full L0 evidence at [`L1/nrm2`](../L1/nrm2.md) §Evidence.)

## Lifts from

L2 `nrm2` lifts from / to L3 [`nrm2`](../L3/nrm2.md) (firm cycle-011) as **identity-in-form**. L3 is the iteration-rotation layer; its `nrm2` is the same whole-tensor reduction with the iteration view of the *surrounding* consuming context (the [`krylov-step`](./krylov-step.md) body's residual-norm readout / Arnoldi sub-diagonal) rendered explicitly. The L3>L2 rotation on the primitive itself is identity-in-form, recorded in-line at the L3 entry's §"Downward to L2" note (no theme file per the 2026-06-01 vocabulary-shift redirect; structurally justified by [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3, which names `nrm2` among the seven primitives that are L2-native / L3-native because each signature has no per-element loop visible). `nrm2` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010 audit verdict); at L4 it appears inside larger composed entries (e.g. `book/src/L4/krylov-step.md` §Semantics, `outputs.residual_norm`) as a let-binding consuming the L3-native primitive surface.

## Evidence

The L2 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's signature); all L0 evidence is transitive through L1. Direct citations relevant to this L2 entry:

- [`book/src/L1/nrm2.md`](../L1/nrm2.md) (firm cycle-003) — authoritative on Palace surface, signature, algebraic laws (inherited unchanged at L2), variant axes (inherited unchanged at L2), the defining identity `nrm2(x) = √dot(x, x)`, the B-weighted-overload boundary, and the complete L0 evidence list.
- [`book/src/L1-L0/nrm2-mutation-rotation.md`](../L1-L0/nrm2-mutation-rotation.md) (firm) — the four-stage L0 chain `Dot → MPI_Allreduce → std::abs → std::sqrt` and the full `std::abs` defensive-guard classification (load-bearing-defensive; property bought = non-negativity invariant for the square root). The L2 entry preserves the guard as an explicit algebraic claim and cites this theme for the classification.
- [`book/src/L2/inner_product.md`](./inner_product.md) (firm cycle-019) — the fold `nrm2` consumes (`√ ∘ abs ∘ inner_product` at `y=x`); the do-NOT-merge boundary (`nrm2` is a consumer, not a member) is carried in this entry's dep-map row.
- [`book/src/L2/index.md`](./index.md) §"Fold-cohort boundary" + line 17 (L2 vocabulary inventory names `nrm2`) — the structural justification for the consumer-not-member framing and the L2-vocabulary home.
- [`book/src/L3/nrm2.md`](../L3/nrm2.md) (firm cycle-011) — the L3 consumer this floor sits under; frontmatter conventions and identity-in-form framing mirrored.
- [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 (`:97`) — the load-bearing statement that the seven L1 primitives (including `nrm2`) are L2-native / L3-native by signature shape. The structural justification for the identity-in-form rotations on both adjacent edges.
- `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template definition: full body (line 259) is `return std::sqrt(std::abs(Dot(comm, x, x)));`. The single load-bearing line; the one-line unfolded composition that makes the L2 fusion rotation a no-op. (Path relative to `reference/palace/`; verified on-disk via `citecheck --anchor Norml2`.)
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template, which uses `Norml2` then asserts `norm > 0.0` and scales `x *= 1.0 / norm`. Confirms `nrm2` returns a positive real used as a divisor. (Path relative to `reference/palace/`; verified on-disk via `citecheck --anchor Normalize`.)
- [`book/src/concepts/nrm2.md`](../concepts/nrm2.md) — the cross-cutting concept page; BLAS-1 heritage framing. (Note: the concept page's stability claim ("Palace uses scaled summation") is incorrect per the L1 correction-pending note at `book/src/L1/nrm2.md:11`; the L1 entry is authoritative.)

## L2 vs L1 distinction

- **L1**: pure functional reduction `α = nrm2(x)`. Mutation-rotation layer — the L0 destination buffer is erased from the signature (there is none — the result is a returned scalar); the MPI collective is folded into the L1>L0 lowering; the `std::abs` guard disappears (subsumed by the algebraic non-negativity claim). The defining identity `nrm2(x) = √dot(x, x)` is stated as algebraic law 8.
- **L2**: fusion-rotation composition `α = nrm2(x)` written as `√ ∘ abs ∘ inner_product` at `y = x`. Fusion-rotation layer — HPC/SIMD tricks unfolded (none here; the L0 form is already unfolded), the `std::abs` load-bearing numerical guard **preserved as an explicit algebraic claim** (not erased as at L1), and `nrm2` framed as a **consumer of the `inner_product` fold** (do-NOT-merge: not a fold member). The signature is identical to L1; the rotation on the primitive is identity-in-form.

The two layers' entries are **value-thread-isomorphic** on the primitive itself. The L2 entry exists for layer-coherence — so the firm L3 [`nrm2`](../L3/nrm2.md) rests on a present adjacent L2 parent — per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** and the 2026-05-31 `l2-floor-under-l3-leaf-cohort` directive.
[new]: # nrm2

> **Consumer-stub (reduced cycle-052 D3, vocabulary-shift-redirect refactor pass).**
> `nrm2` at L2 is a **CONSUMER** of the fold combinator [`inner_product`](./inner_product.md)
> (firm cycle-050) — `nrm2(x) = √ (abs (inner_product(x, x)))`, the `√ ∘ abs ∘ inner_product`
> composition at `y = x`. It is **NOT a fold member** (the do-NOT-merge carve-out): it
> post-composes two scalar maps onto the fold's output, it does not itself fold. Merging it into
> `inner_product` would be a category error. Semantics, algebraic laws, and the consumer-identity
> downward note are deferred to the combinator and the kept in-line §"Downward to L1" below; this
> stub retains only the leaf-level facts the combinator does not carry — the load-bearing
> `std::abs` defensive-guard claim and the `vector.hpp:255-260` `Norml2` L0 anchor.

Euclidean-norm reduction at L2 (the fusion-rotation layer): `α = ‖x‖₂ = √⟨x, x⟩`, written as the
algebraic composition `√ ∘ abs ∘ inner_product` over the length axis. Palace's `linalg::Norml2`
is already the one-line unfolded form (`std::sqrt(std::abs(Dot(comm, x, x)))`,
`palace/linalg/vector.hpp:259`), so the L2 fusion rotation has no fused kernel to unfold; the
entry exists primarily as a **layer-coherence floor** — present so the firm L3
[`nrm2`](../L3/nrm2.md) rests on an adjacent L2 parent.

## Consumer of `inner_product`, NOT a fold member (the do-NOT-merge carve-out)

    nrm2(x) = √ (abs (inner_product(x, x)))        -- √ ∘ abs ∘ inner_product at y = x

`nrm2` post-composes the scalar square-root (and the defensive `abs`) onto the
[`inner_product`](./inner_product.md) fold at the diagonal `y = x`; **it does not itself fold and
is NOT a member of the fold cohort**. Merging `nrm2` into `inner_product` would be a category
error — `inner_product` is the length-axis homomorphism producing `dot(x, x)`; `nrm2` is the
scalar map `α ↦ √|α|` applied to that fold's output. The do-NOT-merge boundary is carried in the
[`inner_product`](./inner_product.md) §"Consumer (NOT an instance)" and in [`L2/index`](./index.md)
§"Fold-cohort boundary"; this entry lists `inner_product` under `consumes`, never as a fold it
instantiates. Semantics and the full algebraic-law listing are deferred to the combinator (which
carries the reduce-to-scalar fold) and the firm L1 leaf [`L1/nrm2`](../L1/nrm2.md) (firm cycle-003,
authoritative on every Palace-surface claim); the consumer-specific downward note is kept in-line
at §"Downward to L1" below.

The B-weighted overload `linalg::Norml2(comm, x, B, Bx) = √(xᴴ B x)` is **not** part of this
operator (per `book/src/L1/nrm2.md:13`) — it is the operator-weighted energy norm, a separate L2
candidate consuming the M-weighted member of `inner_product`, tracked as rough-in
[`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1.

## The `std::abs` defensive guard (the load-bearing leaf-level fact — RETAINED)

**The `std::abs` defensive guard is preserved as an explicit load-bearing numerical claim** (L2
discipline: load-bearing numerical tricks survive the fusion rotation as explicit algebraic
claims, per [`L2/index`](./index.md) §Semantics). It is a no-op in exact arithmetic (the
self-inner-product `inner_product(x, x)` is non-negative real, so `abs` of it equals it) but
**load-bearing in floating point**, where it strips a sign that round-off in the reduction could
have flipped negative on a numerically-zero vector, buying **domain-safety for `√` (no NaN)**. It
is **NOT erasable in floating point** without introducing that NaN failure mode. The full
classification (load-bearing-defensive; property bought = non-negativity invariant for the square
root) lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The
`std::abs` defensive guard — classification", where the guard re-materializes as stage 3 of the
four-stage `Dot → MPI_Allreduce → std::abs → std::sqrt` chain.

## Signature

    nrm2 :: Tensor[N] -> Scalar
    nrm2(x) = √⟨x, x⟩ = √ (abs (inner_product(x, x)))

Result is **always real-valued** and non-negative (`nrm2(x) ≥ 0`), regardless of `x`'s element
type — the element-type axis collapses to a single operator (the post-composed `abs` projects the
complex self-inner-product onto its real magnitude before `√`). Full shape contract +
algebraic-law listing: the combinator [`inner_product`](./inner_product.md) + the firm L1 leaf
[`L1/nrm2`](../L1/nrm2.md).

## Status

`firm` — consumer-stub. `nrm2` at L2 is a CONSUMER of the firm L2 [`inner_product`](./inner_product.md)
combinator (`√ ∘ abs ∘ inner_product` at `y = x`), **not a fold member** (the do-NOT-merge
carve-out). Semantics and algebraic laws are inherited from the combinator / the firm L1 leaf
[`L1/nrm2`](../L1/nrm2.md) unchanged; this chapter retains only the load-bearing `std::abs`
defensive-guard claim and the consumer-identity downward note. The L2 fusion rotation is a no-op
for this leaf (`linalg::Norml2` is already the one-line unfolded composition). The entry exists as
a **layer-coherence floor** per CLAUDE.md §Methodology invariants **Identity-lowerings still
require both L levels** (cycle-009 codification) under the 2026-05-31 foundation-first directive
`l2-floor-under-l3-leaf-cohort`: it gives the firm L3 [`nrm2`](../L3/nrm2.md) (cycle-011) a present
adjacent L2 parent. Harvested cycle-041 wave-1 (D2); reduced to a consumer-stub cycle-052 D3
(vocabulary-shift-redirect refactor pass).

## Downward to L1 (consumer identity-in-form; no theme file)

L2 `nrm2` re-fuses downward onto the single L1 leaf [`nrm2`](../L1/nrm2.md) (firm cycle-003) as
**identity-in-form on the primitive's signature** — value-thread-isomorphic, with **no dispatch**
(one L1 leaf), **no decomposition** (the L2 fusion rotation is a no-op — `linalg::Norml2` is
already the one-line unfolded composition), and **no destination-buffer concern** (the result is a
returned scalar). The hop does two value-preserving surface adjustments:

1. **The `inner_product` fold at `y = x` re-fuses to the `dot` leaf at the diagonal.** L2 names the
   inner reduction as the length-axis `inner_product` fold (firm cycle-019); at L1 the same
   diagonal self-inner-product is the `dot(x, x)` leaf (the defining identity `nrm2(x) = √dot(x, x)`,
   L1 algebraic law 8, `book/src/L1/nrm2.md:53`). This is the **consumer's** view of the edge
   [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) §"The
   diagonal degeneration (`y = x`)" lowers for the fold itself — that theme names `nrm2` precisely
   as the consumer entry point (`√ ∘ inner_product` at `y = x`, the outer `√` a post-step
   "downstream of this lowering, not a dispatch within it"). The inner `inner_product(x, x) →
   dot(x, x)` re-fusion is inherited from the inner-product theme; the `nrm2`-specific content is
   the outer `√ ∘ abs` post-step. **`nrm2` is a CONSUMER of `inner_product`, not a fold member**
   (do-NOT-merge per [`L2/inner_product`](./inner_product.md) §"Consumer (NOT an instance)").
2. **The two scalar post-steps change framing, not value.** At L2 the `abs` guard is **preserved as
   an explicit load-bearing numerical claim** and the `√` is the principal non-negative real square
   root composed onto the fold output. At L1 both drop **below the layer's resolution**: the `abs`
   guard **disappears**, subsumed by the L1 algebraic claim that `dot(x, x)` is non-negative real,
   and the `√` is a deterministic IEEE-754 scalar primitive on the leaf's output. Both treatments
   are consistent — the guard *implements* the non-negativity claim under floating point; full
   classification at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The
   `std::abs` defensive guard — classification".

L0 anchor (transitive through L1; verified on-disk this dispatch via `citecheck --anchor Norml2`):
`palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template; body line 259 is
`return std::sqrt(std::abs(Dot(comm, x, x)));`. The one-line unfolded composition that makes the
L2>L1 fusion rotation a no-op. (Path relative to `reference/palace/`; full L0 evidence at
[`L1/nrm2`](../L1/nrm2.md) §Evidence.)

## Lifts from

L2 `nrm2` lifts from / to L3 [`nrm2`](../L3/nrm2.md) (firm cycle-011) as **identity-in-form**; the
L3>L2 rotation on the primitive is identity-in-form (in-line at the L3 entry's §"Downward to L2").
`nrm2` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010
audit verdict); at L4 it appears inside larger composed entries (e.g.
`book/src/L4/krylov-step.md` §Semantics, `outputs.residual_norm`) as a let-binding.

## Evidence

`nrm2`'s deferred-to homes + retained leaf-level anchors. All semantics/laws evidence is the
combinator's / the firm L1 leaf's:

- [`book/src/L1/nrm2.md`](../L1/nrm2.md) (firm cycle-003) — authoritative on Palace surface,
  signature, algebraic laws, variant axes, the defining identity `nrm2(x) = √dot(x, x)`, the
  B-weighted-overload boundary, and the complete L0 evidence list.
- [`book/src/L1-L0/nrm2-mutation-rotation.md`](../L1-L0/nrm2-mutation-rotation.md) (firm) — the
  four-stage L0 chain `Dot → MPI_Allreduce → std::abs → std::sqrt` and the full `std::abs`
  defensive-guard classification (RETAINED leaf-level fact; the L2 stub preserves the guard as an
  explicit algebraic claim and cites this theme for the classification).
- [`book/src/L2/inner_product.md`](./inner_product.md) (firm cycle-050) — the fold `nrm2`
  CONSUMES (`√ ∘ abs ∘ inner_product` at `y=x`); §"Consumer (NOT an instance)" carries the
  do-NOT-merge boundary.
- [`book/src/L2/index.md`](./index.md) §"Fold-cohort boundary" — the consumer-not-member framing
  and the L2-vocabulary home.
- [`book/src/L3/nrm2.md`](../L3/nrm2.md) (firm cycle-011) — the L3 consumer this floor sits under.
- `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template definition: full body (line 259)
  is `return std::sqrt(std::abs(Dot(comm, x, x)));`. The single load-bearing line — the RETAINED L0
  anchor for the `std::abs` guard. (Path relative to `reference/palace/`; **self-verified via
  `citecheck --anchor Norml2`, anchor at :257 within :255-260** this dispatch.)
- [`book/src/concepts/nrm2.md`](../concepts/nrm2.md) — the cross-cutting concept page; BLAS-1
  heritage framing. (Note: its scaled-summation stability claim is incorrect per the L1
  correction-pending note at `book/src/L1/nrm2.md:11`; the L1 entry is authoritative.)
```

### (ii-b) L3/nrm2.md → consumer-stub

```edit:book/src/L3/nrm2.md
[old]: # nrm2

Whole-tensor Euclidean-norm reduction at L3: `α = ‖x‖₂ = √⟨x, x⟩`. The canonical BLAS-1 norm primitive rendered as an L3 field operation; the workhorse of residual-norm convergence tests, basis-vector normalization, and Arnoldi sub-diagonal coefficients at the iteration-rotation layer. Identity-in-form lowering to L1 [`nrm2`](../L1/nrm2.md); the rotation work is at the surrounding wrapper (the `krylov-step` body or the outer convergence-test consumer), not on the primitive itself.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as `state' = f(state, params)`, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `nrm2` at L3 is a whole-tensor reduction — its signature `(x: Tensor[N]) -> Scalar` exposes no element loop; the reduction over the length axis `N` is a single semantic step at L3 just as it is at L1.

This entry is a **layer-coherence anchor** per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009 meta-phase). The L3 form is value-thread-isomorphic to the L1 form — the rotation L3→L1 is identity-in-form on the primitive's signature; only the surrounding context (the iteration view at L3 vs. the mutation-rotation view at L1) differs. The L3 entry exists because each layer is coherent within itself: a reader navigating L3 (whose index at `book/src/L3/index.md:13` advertises `nrm2` as a field operation in L3 vocabulary) cannot be required to reach down to L1 to find the primitive.

The companion concept page [`concepts/nrm2`](../concepts/nrm2.md) carries the BLAS-1 heritage framing; the L1 entry [`L1/nrm2`](../L1/nrm2.md) is authoritative on every factual claim about the Palace surface (in particular: Palace's `linalg::Norml2` computes the naive `√⟨x, x⟩` via `Dot`, not the BLAS scaled-summation algorithm — the concept page's claim to the contrary is noted as a correction-pending item at `book/src/L1/nrm2.md:11`). This L3 entry adds **iteration-rotation framing** to those — it names `nrm2` as an L3-native whole-tensor reduction consumed inside the surrounding `krylov-step` body's convergence-test readout and Arnoldi sub-diagonal computation — but does not duplicate algebraic-law content; the laws hold uniformly across L1 / L2 / L3 because the body is identity-in-form across the chain.

The B-weighted overload `linalg::Norml2(comm, x, B, Bx)` at `palace/linalg/operator.cpp:600-619` is **not** part of this operator (per the L1 entry's boundary documentation at `book/src/L1/nrm2.md:13`); it is a separate L1 operator candidate (the operator-weighted energy norm, depending on both `dot` and `apply_linop`; tracked as rough-in [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1). At L3 the same boundary holds — `nrm2` is the unweighted Euclidean reduction; the energy-norm primitive is a separate forthcoming L3 candidate.

## Signature

    nrm2 :: Tensor[N] -> Scalar
    nrm2(x) = √⟨x, x⟩

The L3 signature is identical to the L1 signature; only the surrounding layer's vocabulary differs.

Shape contract (positional value; bunsen-style named axis; no element loop exposed at L3):

- **`x`** — `Tensor[N]` — read-only whole-tensor argument.
- **result** — `Scalar` — **always real-valued** (`real`), regardless of whether `x` is real or complex.
- The result is non-negative: `nrm2(x) ≥ 0`.

The "result is always real" rule is load-bearing — it is what makes the element-type axis collapse to a single L3 operator (in contrast to `dot`, where the result element-type tracks the input). It follows from the L1 fact that `dot(x, x)` is a non-negative real scalar for both real (L1 dot law 4) and complex (L1 dot law 9) inputs.

No element loop is exposed at L3 — the reduction over `i ∈ [0, N)` is a single semantic step in the L3 calculus. This is what makes `nrm2` L3-native by signature shape (per `book/src/L3-L2/krylov-step-body-identity.md:97`).

## Semantics

Whole-tensor reduction with defining identity: `nrm2(x) = √dot(x, x)`. This is the principal (non-negative) square root of the Hermitian self-inner-product. At L3 the reduction is rendered as a single semantic step — one node in the iteration-rotation calculus.

For real element-type: `nrm2(x) = √Σ_i x[i]²`.

For complex element-type: `nrm2(x) = √Σ_i |x[i]|² = √Σ_i (re(x[i])² + im(x[i])²)`. The Hermitian self-dot `dot(x, x)` for complex `x` is `Σ_i conj(x[i])·x[i] = Σ_i |x[i]|²`, which is real and non-negative element-wise. Inherited unchanged from [`L1/nrm2`](../L1/nrm2.md) §Semantics.

Reduction-tree non-associativity is **load-bearing** — inherited unchanged from `dot`. The square root itself is a deterministic IEEE-754 operation (correctly rounded), so `nrm2`'s non-determinism is entirely the underlying `dot`'s. Recorded as a non-law (see §Algebraic laws below).

The MPI collective is **not** in the L3 signature — single-rank is in scope per CLAUDE.md §Scope. The reduction at L3 is a single step; the local-then-collective two-step reappears only in the L1>L0 lowering at L1.

### Iteration-rotation marker

L3 is the iteration-rotation layer, and `nrm2`'s iteration view is the reduction over the length axis `N`. **The reduction lifts as a whole-tensor operation** — the signature `Tensor[N] -> Scalar` exposes no element loop, and the reduction-tree shape is opaque at L3 (the bit-level non-associativity is a recorded non-law, not a structural element of the L3 form). There is **no sequential obstruction** for `nrm2` — the reduction over independent length-axis indices is a parallel operation in exact arithmetic; the load-bearing pinned tree at L0 is a floating-point implementation choice, not an algebraic obstruction at L3.

`nrm2` is **consumed inside** larger L3 forms in two distinct roles:

1. **Convergence-test readout in `outputs`** — per `book/src/L3/krylov-step.md` §Semantics, the per-step body's `derived_views K' op` projection typically produces `outputs.residual_norm = sqrt(abs K'.β)` (CG's residual norm, computed via `dot` and inferred via the recurrence) or `outputs.residual_norm = nrm2(K'.r)` (recompute-from-residual variants). The surrounding `iterate_while_L3` outer loop reads `outputs.residual_norm` against the convergence predicate; `nrm2` is a leaf reduction consumed by this projection.
2. **Arnoldi sub-diagonal coefficient** — `H[j+1, j] = nrm2(w)` after orthogonalization (per `palace/linalg/iterative.cpp:631, 810`, the Arnoldi loop's basis-vector normalization). Consumed inside the `op.orthog` closure at the L3 form; surfaces as a scalar field of `K'` in the iterate-and-scalar update.

At L3 `nrm2` is a leaf reduction; the iteration view is what the surrounding `krylov-step` body or outer convergence-test consumer provides, not what `nrm2` itself contributes.

## Algebraic laws

The L3 algebraic laws are **inherited unchanged from L1** because the L3 form is value-thread-isomorphic to the L1 form. Inheritance is total: every L1 law for `nrm2` holds at L3 with the same statement, and every L1 non-law remains a non-law at L3. The laws are reproduced here so the L3 reader does not have to reach to L1 for the listing.

The laws below hold for both real and complex element-types of `x`:

1. **Non-negativity**: `nrm2(x) ≥ 0` for all `x`.
2. **Positive-definite (separation)**: `nrm2(x) = 0` iff `x = 0` (in exact arithmetic). The "iff" direction follows from `dot` law 4 / 9.
3. **Positive homogeneity (absolute scalar)**: `nrm2(α·x) = |α|·nrm2(x)` for any scalar `α` (real or complex). The absolute value is necessary on both sign and complex phase.
4. **Triangle inequality**: `nrm2(x + y) ≤ nrm2(x) + nrm2(y)`.
5. **Reverse triangle inequality**: `|nrm2(x) − nrm2(y)| ≤ nrm2(x − y)`. (Follows from law 4.)
6. **Cauchy–Schwarz** (relating `nrm2` to `dot`): `|dot(x, y)| ≤ nrm2(x) · nrm2(y)`, with equality iff `x` and `y` are linearly dependent (in exact arithmetic).
7. **Parallelogram identity**: `nrm2(x + y)² + nrm2(x − y)² = 2·nrm2(x)² + 2·nrm2(y)²`. (Characterizes norms induced by an inner product; holds here because `nrm2` is defined as `√⟨·,·⟩`.)
8. **Self-dot identity**: `nrm2(x)² = dot(x, x)` (real and complex) — the defining identity, restated. The structural link to `dot` is preserved unchanged at L3.
9. **Zero in argument**: `nrm2(0) = 0`. (Special case of law 2.)
10. **Phase invariance (complex)**: for complex `x` and any unit-modulus complex scalar `e^{iθ}`: `nrm2(e^{iθ}·x) = nrm2(x)`. (Special case of law 3 with `|α| = 1`.)

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Linearity in `x`**: `nrm2(α·x + β·y) ≠ α·nrm2(x) + β·nrm2(y)` in general. `nrm2` is sub-additive (law 4), not additive. This is the defining feature that distinguishes a norm from a linear functional.
- **Strictness of Cauchy–Schwarz in floating point**: law 6 can fail by ULP-level amounts due to summation ordering inside `dot` (same load-bearing caveat as the `dot` operator).
- **Bit-determinism across reduction trees**: same load-bearing caveat as `dot` — different reduction orders produce different bit-level `nrm2` values. The mathematical laws above hold; their floating-point realizations are exact modulo summation-order noise.
- **Multiplicativity over the cross-element kernel**: not applicable — `nrm2` is a reduction, not a binary algebra on vectors.

## Dependencies

**Same-layer (L3)**: [`dot`](./dot.md) — `nrm2(x) = √dot(x, x)`. The dependency is direct and complete: the L0 source defines `Norml2` as a one-line composition `std::sqrt(std::abs(Dot(comm, x, x)))`, and the L3 form preserves this composition by Law 8. The outer `sqrt` and `abs` are scalar operations below the L3 layer's resolution (deterministic IEEE-754 primitives operating on a single scalar produced by `dot`). The dependency on `dot` is the **only** L3 dependency; `nrm2` is otherwise a leaf at L3.

The fact that `nrm2` factors so cleanly through `dot` is exactly the kind of compositional structure the L3 layer is meant to expose at the field-operation level; the L0 form makes the composition syntactically explicit (one line of source at `palace/linalg/vector.hpp:255-260`), and the L3 form preserves the algebraic identity by inheritance.

**Consumers (L3)**: [`krylov-step`](./krylov-step.md) — the per-step body's `derived_views K' op` projection consumes `nrm2` for the residual-norm readout (CG, MINRES) and the Arnoldi sub-diagonal scalar (GMRES). The convergence-test consumer at the surrounding `iterate_while_L3` outer loop reads `outputs.residual_norm` per the [`convergence-test`](../concepts/convergence-test.md) discipline.

**Cross-cutting concepts**:

- [`nrm2`](../concepts/nrm2.md) — the cross-cutting concept page with BLAS-1 heritage framing.
- [`dot`](../concepts/dot.md) — referenced transitively through the defining identity `nrm2(x) = √dot(x, x)`.
- [`convergence-test`](../concepts/convergence-test.md) — the consuming context at the outer `iterate_while_L3` loop.

**L1 anchor**: [`L1/nrm2`](../L1/nrm2.md) (firm cycle-003) — the L1 entry is authoritative on the Palace surface details, the one-line `linalg::Norml2` template definition, the relationship to the B-weighted overload (separately tracked), and the complete L0 evidence list. This L3 entry does not duplicate those details; the L3>L1 rotation is identity-in-form on the primitive itself.

## Variant axes

Inherited unchanged from L1 at **one** axis:

1. **element-type** (`real` | `complex`) — at L0 these are template specializations of `linalg::Norml2<VecType>` (`VecType ∈ {Vector, ComplexVector}`). At L1 / L3 these **collapse to a single operator** with the same signature `Tensor[N] -> Scalar(real)`, because the result is real-valued regardless of input element type (the Hermitian self-dot is real per `dot` law 4 / 9), and the defining identity `nrm2(x) = √dot(x, x)` is shared across element types.

This is a stronger collapse than `dot`'s element-type axis: `dot` retains an element-type-tracking return scalar (real `dot` → real, complex `dot` → complex); `nrm2` does not.

No other variant axes at L3:

- **B-weighting**: not a variant of `nrm2` — it is a distinct operator (the operator-weighted energy norm) tracked as [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1 (rough-in cycle-010 wave-1). The L0 surface uses the same overloaded name `linalg::Norml2`, but the algebraic structure differs (requires an external `B`-application primitive, requires an SPD precondition on `B`, the workspace `Bx` is a load-bearing buffer at L0).
- **Stability variants**: BLAS-style scaled-summation `nrm2` is **not present** in Palace's `linalg::Norml2` — Palace uses the naive `√⟨x, x⟩` form. Not a variant axis of the L3 operator.

## Status

`firm` — L3 form is value-thread-isomorphic to the L1 form (identity-in-form rotation); algebraic laws inherited unchanged; variant-axis profile inherited unchanged at one axis. The entry exists as a **layer-coherence anchor** per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** (cycle-009 codification). Harvested cycle-011 wave-1 as part of the BLAS-1 reduction cohort backfill (sibling dispatch to `apply_linop`, the axpy cohort, `dot`, and `scal` at L3).

## Lowers to

L3 `nrm2` lowers to L1 [`nrm2`](../L1/nrm2.md) as **identity-in-form on the primitive's signature**. There is no L3-L1 lowering theme — no `book/src/L3-L1/` directory currently exists (precedent: cycle-010 `L3/krylov-step.md` records its identity-in-form lowering in-line at the entry, not in a separate theme file). The rotation work for this primitive lives in the surrounding wrapper at the consuming `krylov-step` body or outer convergence-test consumer, captured by [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 (which names `nrm2` among the seven primitives that are "L3-native because [each primitive's] signature has no per-element loop visible").

The L1>L0 lowering of `nrm2` lives at the L1 entry's evidence section (`book/src/L1/nrm2.md` §Evidence) — Palace's `linalg::Norml2` template at `palace/linalg/vector.hpp:255-260` is the one-line composition `std::sqrt(std::abs(Dot(comm, x, x)))`; the `std::abs` outer guard is a load-bearing defensive non-negativity check against floating-point round-off pushing the sum slightly negative; the inner `Dot` carries the MPI_Allreduce. None of this is L3 content; the L3 form sees a single-step whole-tensor reduction.

### Downward to L2 (consumer identity-in-form; no theme file)

L3 `nrm2` lowers to L2 [`nrm2`](../L2/nrm2.md) as **identity-in-form on the primitive's signature**. There is no dedicated L3>L2 theme file: the rotation is a degenerate identity-in-named-terms lowering (the only textual delta is the inner-reduction NAME), so under the 2026-06-01 vocabulary-shift redirect it is recorded here in-line rather than as a thin theme.

- **`nrm2` is a CONSUMER of `inner_product`, not a fold member.** At L2 the defining identity is written through the `inner_product` fold at the diagonal — `nrm2 x = √ (abs (inner_product x x))`, the `√ ∘ abs ∘ inner_product` composition at `y = x`. `nrm2` post-composes two scalar maps (`abs`, then `√`) onto the fold's scalar output; it does NOT itself fold and is NOT a member of the fold cohort. Merging `nrm2` into `inner_product` would be a category error (the do-NOT-merge boundary, carried in the [`inner_product`](../L2/inner_product.md) dep-map row and [`L2/index`](../L2/index.md) §"Fold-cohort boundary"). The L2 entry lists `inner_product` under `consumes`, never as a fold the operator instantiates.
- **The only textual change L3 → L2 is the inner-reduction name.** L3 writes the defining identity through the same-layer `dot(x, x)` leaf (`L3/nrm2` §Dependencies); L2 writes it through the `inner_product(x, x)` fold at the diagonal `y = x`. These denote the same Hermitian self-inner-product value (`dot(x, x) = inner_product(x, x)` at `y = x` — the inner-product fold's diagonal degeneration, [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) §"The diagonal degeneration (`y = x`)"). The signature `Tensor[N] -> Scalar` is identical at both layers; no element loop is exposed at either (the reduction over the length axis is a single semantic step), so the rotation is identity-in-form with **no wrapper to rotate** (`nrm2` is a leaf reduction — there is no `(op, K, s)` tuple or outer loop, strictly simpler than `krylov-step-body-identity`). `nrm2` is L3-native / L2-native by signature shape per [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 (`:97`).
- **The `std::abs` defensive guard is preserved as an explicit load-bearing numerical claim at L2** (it is implicit at L3, subsumed by the non-negativity claim). The guard is a no-op in exact arithmetic but load-bearing in floating point — it strips a sign that round-off in the reduction could have flipped negative on a numerically-zero vector, buying domain-safety for `√` (no NaN). Both framings are consistent (the guard implements the non-negativity invariant); the full classification lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive guard — classification".

L0 anchor (transitive through L1; verified on-disk this dispatch via `citecheck --anchor Norml2`): `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template; body line 259 is `return std::sqrt(std::abs(Dot(comm, x, x)));`. The one-line unfolded composition that makes the L3>L2 rotation identity-in-form. (Path relative to `reference/palace/`; full L0 evidence at [`L1/nrm2`](../L1/nrm2.md) §Evidence.)

## Lifts from

`nrm2` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010 audit verdict at `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"Per-candidate verdict" (2): "leaf primitives don't get L4 rows"). At L4, `nrm2` appears inside larger composed entries (e.g., `book/src/L4/krylov-step.md` §Semantics body — `outputs.residual_norm` computed via `nrm2` or via the recurrence shortcut) as a let-binding consuming the L3-native primitive surface; it carries no monadic effect, no state-stratification typing, no novel calculus content at L4.

## Evidence

The L3 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's signature); all L0 evidence is transitive through L1. Direct citations relevant to this L3 entry:

- [`book/src/L1/nrm2.md`](../L1/nrm2.md) (firm cycle-003) — authoritative on Palace surface, signature, algebraic laws (inherited unchanged at L3), variant axes (inherited unchanged at L3), the defining identity `nrm2(x) = √dot(x, x)`, the B-weighted-overload boundary, and the complete L0 evidence list (`palace/linalg/vector.hpp:255-260`, `palace/linalg/vector.hpp:262-270`, `palace/linalg/operator.hpp:372-374`, `palace/linalg/operator.cpp:600-619`, etc.).
- [`book/src/L1/dot.md`](../L1/dot.md) (firm cycle-002) — the dependency anchor; provides laws 4 / 9 (Hermitian self-dot is non-negative real) on which `nrm2`'s real-valued result and positivity depend.
- [`book/src/L3/dot.md`](./dot.md) (firm cycle-011, sibling dispatch) — the L3 dependency anchor; the defining identity `nrm2(x) = √dot(x, x)` is L3-internal.
- [`book/src/L3/index.md`](./index.md) line 13 — the L3 vocabulary inventory explicitly names `nrm2` as an L3 field operation. This L3 entry closes the inventory-vs-content gap noted by the cycle-010 audit.
- [`book/src/L3/krylov-step.md`](./krylov-step.md) §Semantics — the consuming context at L3; the per-step body's `derived_views` projection consumes `nrm2` for residual-norm readout; the `op.orthog` closure consumes `nrm2` for Arnoldi sub-diagonal coefficients.
- [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 — the load-bearing statement that the seven L1 primitives (including `nrm2`) are L3-native by signature shape. This is the structural justification for the L3>L1 identity-in-form rotation.
- [`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)" — the L3 body let-chain renders `nrm2` as an L3-native primitive call identical in shape to its L1 signature.
- [`book/src/concepts/nrm2.md`](../concepts/nrm2.md) — the cross-cutting concept page; the BLAS-1 heritage framing. (Note: the concept page's stability claim ("Palace uses scaled summation") is incorrect per the L1 entry's correction-pending note at `book/src/L1/nrm2.md:11`; the L1 entry is authoritative.)
- `palace/linalg/iterative.cpp:408, 568, 578, 582, 631, 756, 762, 810` — CG and GMRES iterative solvers using `linalg::Norml2` for: initial right-hand-side norm `β = ‖b‖`, true residual norm `‖r‖`, and Arnoldi sub-diagonal coefficients `H[j+1,j] = ‖w‖`. Direct evidence `nrm2` is the convergence-test and Arnoldi-orthogonalization primitive, inherited transitively. (Paths relative to `reference/palace/`.)
- `test/unit/test-vector.cpp:209-211` — direct test: `double norm1 = vec1.Norml2(); CHECK_THAT(norm1, WithinRel(std::sqrt(14.0)));` for `vec1 = (1, 2, 3)`. L0-equivalent semantic documentation per CLAUDE.md §"Tests as semantic supplement", inherited transitively. (Path relative to `reference/palace/`.)
- Cycle-010 audit at [`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`](../../../reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md) §"Per-candidate verdict" (2) — HIGH CONFIDENCE backfill recommendation for the BLAS-1 cohort at L3, including `nrm2`. This entry is the enactment.

## L3 vs L1 distinction

- **L1**: pure functional reduction `α = nrm2(x)`. Mutation-rotation layer — the L0 destination buffer is erased from the signature; the MPI collective is folded into the L1>L0 lowering. The B-weighted overload is factored out as a separate L1 operator (`matrix-weighted-norm` rough-in). The defining identity `nrm2(x) = √dot(x, x)` is stated as algebraic law 8.
- **L3**: whole-tensor reduction `α = nrm2(x)` rendered as an L3 field operation. Iteration-rotation layer — the surrounding consuming context (the `krylov-step` body's `derived_views` projection, or the Arnoldi sub-diagonal in `op.orthog`) renders the iteration view explicitly as `(K, s) -> (K', s')` value-threading; `nrm2` itself is consumed as a leaf reduction with no iteration view of its own. The signature is identical to L1; the rotation is at the surrounding wrapper, not on the primitive.

The two layers' entries are **value-thread-isomorphic** on the primitive itself. The L3 entry exists for layer-coherence — a reader at L3 navigating the `krylov-step` body or the L3 vocabulary inventory must find `nrm2` defined in L3 vocabulary at L3, per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**.
[new]: # nrm2

> **Consumer-stub (reduced cycle-052 D3, vocabulary-shift-redirect refactor pass).**
> `nrm2` at L3 is a **CONSUMER** of the inner-product fold (`nrm2(x) = √dot(x, x)`, or through
> the L2 [`inner_product`](../L2/inner_product.md) combinator at the diagonal: `√ ∘ abs ∘
> inner_product` at `y = x`) — it is **NOT a fold member** (the do-NOT-merge carve-out): it
> post-composes the scalar `√` (and the defensive `abs`) onto the fold's output, it does not
> itself fold. Semantics, algebraic laws, and the no-sequential-obstruction verdict are deferred
> to the firm L1 leaf [`L1/nrm2`](../L1/nrm2.md) / the combinator; this stub retains the
> consuming-context framing (residual-norm readout, Arnoldi sub-diagonal), the load-bearing
> `std::abs` guard note, and the kept in-line §"Downward to L2" consumer note.

Whole-tensor Euclidean-norm reduction at L3: `α = ‖x‖₂ = √⟨x, x⟩`. The canonical BLAS-1 norm
primitive rendered as an L3 field operation; the workhorse of residual-norm convergence tests,
basis-vector normalization, and Arnoldi sub-diagonal coefficients at the iteration-rotation layer.
Identity-in-form lowering to L1 [`nrm2`](../L1/nrm2.md); the rotation work is at the surrounding
wrapper (the `krylov-step` body or the outer convergence-test consumer), not on the primitive.

## Signature

    nrm2 :: Tensor[N] -> Scalar
    nrm2(x) = √⟨x, x⟩ = √dot(x, x)

Result is **always real-valued** and non-negative (`nrm2(x) ≥ 0`), regardless of `x`'s element
type. Identical to the L1 signature; full shape contract + algebraic-law listing at the firm L1
leaf [`L1/nrm2`](../L1/nrm2.md).

## Consuming context (the leaf-level fact — RETAINED)

`nrm2` is a leaf reduction at L3 with **no iteration view of its own**; the iteration view is what
the surrounding form provides. It is **consumed inside** larger L3 forms in two distinct roles:

1. **Convergence-test readout in `outputs`** — per `book/src/L3/krylov-step.md` §Semantics, the
   per-step body's `derived_views K' op` projection produces `outputs.residual_norm = sqrt(abs K'.β)`
   (CG, inferred via the recurrence) or `outputs.residual_norm = nrm2(K'.r)` (recompute-from-residual
   variants). The surrounding `iterate_while_L3` outer loop reads `outputs.residual_norm` against the
   convergence predicate.
2. **Arnoldi sub-diagonal coefficient** — `H[j+1, j] = nrm2(w)` after orthogonalization (per
   `palace/linalg/iterative.cpp:631, 810`, the Arnoldi loop's basis-vector normalization). Consumed
   inside the `op.orthog` closure.

There is **no sequential obstruction** for `nrm2` — the reduction over independent length-axis
indices is parallel in exact arithmetic; the load-bearing pinned reduction tree at L0 is a
floating-point implementation choice (a recorded non-law), not an algebraic obstruction at L3.

## The `std::abs` defensive guard (load-bearing leaf-level fact)

The defining identity is `nrm2(x) = √dot(x, x)`; the L0 source is the one-line composition
`std::sqrt(std::abs(Dot(comm, x, x)))` (`palace/linalg/vector.hpp:255-260`). The `std::abs` outer
guard is a **load-bearing defensive non-negativity check** against floating-point round-off pushing
the sum slightly negative on a numerically-zero vector (buying domain-safety for `√`, no NaN). It is
implicit at L3 (subsumed by the non-negativity claim) and preserved as an explicit algebraic claim
at L2; the full classification lives at
[`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive
guard — classification". The B-weighted overload `linalg::Norml2(comm, x, B, Bx)` is **not** part of
this operator (tracked as rough-in [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1).

## Status

`firm` — consumer-stub. `nrm2` at L3 is a CONSUMER of the inner-product fold (`√dot(x, x)`; through
the L2 [`inner_product`](../L2/inner_product.md) combinator at the diagonal), **not a fold member**
(the do-NOT-merge carve-out). The L3 form is value-thread-isomorphic to the firm L1 leaf
[`L1/nrm2`](../L1/nrm2.md); semantics, algebraic laws, and variant axes are inherited from L1
unchanged. This chapter retains only the consuming-context framing, the `std::abs` guard note, and
the consumer-identity §"Downward to L2" note. The entry exists as a **layer-coherence anchor** per
CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** (cycle-009
codification). Harvested cycle-011 wave-1 (BLAS-1 reduction cohort backfill); reduced to a
consumer-stub cycle-052 D3 (vocabulary-shift-redirect refactor pass).

## Lowers to

L3 `nrm2` lowers to L1 [`nrm2`](../L1/nrm2.md) as **identity-in-form on the primitive's signature**.
There is no L3-L1 lowering theme (precedent: cycle-010 `L3/krylov-step.md` records its
identity-in-form lowering in-line). The rotation work lives in the surrounding wrapper at the
consuming `krylov-step` body or outer convergence-test consumer, captured by
[`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md)
§"Applicability conditions" point 3 (which names `nrm2` among the seven primitives that are
"L3-native because [each primitive's] signature has no per-element loop visible"). The L1>L0
lowering lives at the L1 entry — Palace's `linalg::Norml2` at `palace/linalg/vector.hpp:255-260`
expands into `std::sqrt(std::abs(Dot(comm, x, x)))`, the `Dot` carrying the MPI_Allreduce. None of
this is L3 content.

### Downward to L2 (consumer identity-in-form; no theme file)

L3 `nrm2` lowers to L2 [`nrm2`](../L2/nrm2.md) as **identity-in-form on the primitive's signature**.
There is no dedicated L3>L2 theme file: the rotation is a degenerate identity-in-named-terms
lowering (the only textual delta is the inner-reduction NAME), so under the 2026-06-01
vocabulary-shift redirect it is recorded here in-line.

- **`nrm2` is a CONSUMER of `inner_product`, not a fold member.** At L2 the defining identity is
  written through the `inner_product` fold at the diagonal — `nrm2 x = √ (abs (inner_product x x))`,
  the `√ ∘ abs ∘ inner_product` composition at `y = x`. `nrm2` post-composes two scalar maps (`abs`,
  then `√`) onto the fold's scalar output; it does NOT itself fold and is NOT a member of the fold
  cohort. Merging `nrm2` into `inner_product` would be a category error (the do-NOT-merge boundary,
  carried in the [`inner_product`](../L2/inner_product.md) §"Consumer (NOT an instance)" and
  [`L2/index`](../L2/index.md) §"Fold-cohort boundary"). The L2 entry lists `inner_product` under
  `consumes`, never as a fold the operator instantiates.
- **The only textual change L3 → L2 is the inner-reduction name.** L3 writes the defining identity
  through the same-layer `dot(x, x)` leaf; L2 writes it through the `inner_product(x, x)` fold at the
  diagonal `y = x`. These denote the same Hermitian self-inner-product value (`dot(x, x) =
  inner_product(x, x)` at `y = x` — the inner-product fold's diagonal degeneration,
  [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) §"The diagonal
  degeneration (`y = x`)"). The signature `Tensor[N] -> Scalar` is identical at both layers; no
  element loop is exposed at either, so the rotation is identity-in-form with **no wrapper to
  rotate** (`nrm2` is a leaf reduction). `nrm2` is L3-native / L2-native by signature shape per
  [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions"
  point 3 (`:97`).
- **The `std::abs` defensive guard is preserved as an explicit load-bearing numerical claim at L2**
  (it is implicit at L3, subsumed by the non-negativity claim). The guard is a no-op in exact
  arithmetic but load-bearing in floating point — it strips a sign that round-off in the reduction
  could have flipped negative on a numerically-zero vector, buying domain-safety for `√` (no NaN).
  Both framings are consistent; the full classification lives at
  [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive
  guard — classification".

L0 anchor (transitive through L1; verified on-disk this dispatch via `citecheck --anchor Norml2`):
`palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template; body line 259 is
`return std::sqrt(std::abs(Dot(comm, x, x)));`. The one-line unfolded composition that makes the
L3>L2 rotation identity-in-form. (Path relative to `reference/palace/`; full L0 evidence at
[`L1/nrm2`](../L1/nrm2.md) §Evidence.)

## Lifts from

`nrm2` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010
audit verdict). At L4, `nrm2` appears inside larger composed entries (e.g.
`book/src/L4/krylov-step.md` §Semantics body — `outputs.residual_norm`) as a let-binding consuming
the L3-native primitive surface.

## Evidence

`nrm2`'s deferred-to homes + retained leaf-level anchors. All semantics/laws evidence is the firm L1
leaf's / the combinator's:

- [`book/src/L1/nrm2.md`](../L1/nrm2.md) (firm cycle-003) — authoritative on Palace surface,
  signature, algebraic laws, variant axes, the defining identity `nrm2(x) = √dot(x, x)`, the
  B-weighted-overload boundary, and the complete L0 evidence list (`palace/linalg/vector.hpp:255-260`,
  `palace/linalg/vector.hpp:262-270`, `palace/linalg/operator.hpp:372-374`, `palace/linalg/operator.cpp:600-619`, etc.).
- [`book/src/L3/dot.md`](./dot.md) (firm cycle-011) — the L3 dependency anchor; the defining
  identity `nrm2(x) = √dot(x, x)` is L3-internal.
- [`book/src/L2/nrm2.md`](../L2/nrm2.md) (firm cycle-041) — the adjacent L2 consumer-stub this lowers
  to; the consumer-not-member framing mirrored.
- [`book/src/L1-L0/nrm2-mutation-rotation.md`](../L1-L0/nrm2-mutation-rotation.md) (firm) — the
  four-stage L0 chain and the full `std::abs` defensive-guard classification (the RETAINED guard's
  home).
- [`book/src/L3/krylov-step.md`](./krylov-step.md) §Semantics + [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 — the consuming context + the structural justification (`nrm2` L3-native by signature shape).
- `palace/linalg/iterative.cpp:408, 568, 578, 582, 631, 756, 762, 810` — CG and GMRES using
  `linalg::Norml2` for the initial RHS norm, true residual norm, and Arnoldi sub-diagonal
  coefficients. Direct evidence `nrm2` is the convergence-test / Arnoldi primitive, inherited
  transitively. (Paths relative to `reference/palace/`.)
- `test/unit/test-vector.cpp:209-211` — direct test: `double norm1 = vec1.Norml2();
  CHECK_THAT(norm1, WithinRel(std::sqrt(14.0)));` for `vec1 = (1, 2, 3)`. L0-equivalent semantic
  documentation, inherited transitively. (Path relative to `reference/palace/`.)
- [`book/src/concepts/nrm2.md`](../concepts/nrm2.md) — the cross-cutting concept page; BLAS-1
  heritage framing. (Note: its scaled-summation stability claim is incorrect per the L1
  correction-pending note at `book/src/L1/nrm2.md:11`; the L1 entry is authoritative.)
```

## Discipline notes

- **Two distinct stub kinds applied by one owner, consistently.** `dot` (L2 + L3) → **specialization-stubs**:
  the stub link is "specialization of `inner_product`" (a fold MEMBER at the `M=I` Hermitian/symmetric
  axis-value), the conjugation variant-axis row (`dot` vs `tdot`) is RETAINED as the value-bearing
  leaf-level fact. `nrm2` (L2 + L3) → **consumer-stubs**: the stub link is "CONSUMER of `inner_product`"
  (`√ ∘ abs ∘ inner_product` at `y=x`, explicitly NOT a fold member — the do-NOT-merge carve-out per
  `L2/index.md` §"Fold-cohort boundary" and the `inner_product` §"Consumer (NOT an instance)"). The
  member/consumer distinction is the load-bearing reason the two reductions get different stub framings;
  applying both from one dispatch keeps the terminology aligned.
- **Retentions honored exactly.** `dot` stubs RETAIN: the conjugation variant-axis row + `dot`'s unique
  L0 anchors (`vector.hpp:110-113`, `vector.cpp:263-267` Hermitian Dot with the `&x==&y` imag=`0.0`
  self-dot at `:266`, `vector.cpp:269-274` TransposeDot/`tdot`, `test-vector.cpp:206-207`). `nrm2` stubs
  RETAIN: the load-bearing `std::abs` defensive-guard claim + the `vector.hpp:255-260` `Norml2` anchor +
  the c051 in-line §"Downward to L1"/§"Downward to L2" consumer note (kept verbatim in substance — the
  consumer-demotion that landed last cycle is preserved as the stub's deferred-to home).
- **All four stay `## Status: firm`** — these are value-thread-isomorphic identity-in-form floors, not
  status reductions. The stub-flip removes duplicated body (semantics/laws now deferred to the
  combinator/L1 leaf), not firmness.
- **Layer-definition discipline (high→low) preserved.** The `dot`/`nrm2` chapters narrate the
  rewrite forward (L2/L3 form → combinator/L1 leaf); the §"Downward to L1"/§"Downward to L2" notes are
  forward (higher→lower). No reverse-direction (lift-upward) prose was introduced into the chapter bodies;
  upward framing stays as the brief §"Lifts from" pointer that was already present.
- **No content correction needed.** This is pure structural rewriting (reduce-to-stub + defer-to-parent);
  no backward conventions, drifted citations, or contradicting claims were found in the four files. The
  `concepts/nrm2.md` scaled-summation incorrectness is already flagged as correction-pending at
  `L1/nrm2.md:11` (not my scope; preserved verbatim in the stubs).
- **Cross-reference to the promoting refactor:** the `inner_product` combinator was promoted to firm L2
  (cycle-050) and propagated up to firm L3 (cycle-050) by the combinator-miner refactor-pass; the
  degenerate `dot-body-identity` / `dot-leaf-identity` themes were demoted into the combinator's homes
  cycle-051. This D3 dispatch completes the leaf-side of that refactor by reducing the four leaf chapters
  to stubs deferring to those now-firm combinator homes.

## Supporting evidence

- **Citation self-verification (`tools/citecheck/citecheck.py --anchor`, this dispatch):** all retained
  L0 anchors verified ON-DISK against `reference/palace/`:
  - `vector.hpp:255-260` anchor `Norml2` → ok, anchor at :257 (nrm2 stubs).
  - `vector.cpp:263-267` anchor `Dot` → ok, anchor at :263; `vector.cpp:266` anchor `0.0` → ok at :266 (dot self-dot PSD).
  - `vector.cpp:269-274` anchor `TransposeDot` → ok at :269 (`tdot` kernel).
  - `vector.hpp:110-113` anchor `Dot` → ok at :111-113 (`ComplexVector::Dot` decl).
- **Deferred-to firm homes (read this dispatch):** `book/src/L2/inner_product.md` (firm cycle-050;
  §"Specializations" :158, §"Consumer (NOT an instance)" :431), `book/src/L3/inner_product.md` (firm
  cycle-050; §"Specializations" :133, §"Consumer (NOT an instance)" :319). The §"Specializations" (for
  `dot`) and §"Consumer (NOT an instance)" (for `nrm2`) sections both exist and carry the deferred body.
- **Inbound-link / zero-dangling sweep (per `skills/deleted-slug-inbound-live-link-sweep` gate):**
  reduce-to-stub KEEPS all four files on disk, so every inbound link stays LIVE. Confirmed inbound
  references resolve to the kept stubs:
  - SUMMARY.md rows :32-33 (`L3/dot`, `L3/nrm2`), :65-66 (`L2/dot`, `L2/nrm2`) — D4-owned, untouched, still resolve.
  - `L3/nrm2.md → ./dot.md` (same-layer dependency) and `L3/nrm2.md → ../L2/nrm2.md` — both kept; the stubs preserve these targets.
  - `L2/normalize.md`, `L2/divfree-projector.md`, `L2/assemble-diagonal.md`, `L3/chebyshev.md`, `L3/ksp_solve.md`, `L3/orthogonalize.md`, `L3/reciprocal.md`, `L3/index.md`, `L2/inner_product.md` — all reference the four leaves by path; all kept → LIVE.
  - All outbound links the stubs emit point at existing files (verified: `inner_product.md`, `L1/dot.md`, `L1/nrm2.md`, `L2-L1/inner-product-fold-specialization.md`, `L1-L0/nrm2-mutation-rotation.md`, `L3-L2/krylov-step-body-identity.md`, the concept pages — all on disk).
  - **Zero dangling.** No file is removed; no inbound link breaks.

## Open questions / caveats

- **Index-row alignment (D4's scope, flagged for coordination, not edited here).** D4 owns the
  `inner_product`-family index rows/narrative. After this stub-flip, the L2/L3 index narratives that still
  describe `dot`/`nrm2` as full thin-floor chapters (e.g. `L3/index.md:15` lists `dot`/`nrm2` among the
  obstruction-free leaves; `L2/index.md` §"Fold-cohort boundary" describes the leaf-vs-fold cohort) should
  read consistently with the combinator-as-entry / member-vs-consumer framing the stubs now carry. The
  stubs themselves cite `L2/index.md` §"Fold-cohort boundary" and the `inner_product` §"Consumer (NOT an
  instance)" as authoritative, so they remain correct regardless; this is a narrative-coherence note for
  D4, not a blocker.
- **`normalize` constituent-floor citations (no action needed, recorded for awareness).** `L2/normalize.md`
  cites `nrm2` and `scal` as *consumed* same-layer constituent floors (lines 102, 163, etc.) and depends on
  `nrm2`'s real-valued-output collapse + `std::abs` guard. The `nrm2` consumer-stub RETAINS exactly those
  facts (the always-real result rule + the `std::abs` guard claim), so `normalize`'s citations remain
  satisfied. No change required to `normalize` (out of D3 scope regardless).
- **No abstractor reread triggered.** The firmed-up `inner_product` combinator signature matches what the
  leaf chapters assumed (`dot(x,y) = inner_product x y`; `nrm2 = √ ∘ abs ∘ inner_product` at `y=x`); the
  stub-flip is pure rewriting, no LHS/RHS shape change, no signature contradiction. No abstractor rerun
  needed.

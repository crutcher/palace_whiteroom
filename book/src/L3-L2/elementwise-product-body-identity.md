# elementwise-product-body-identity

The L3>L2 lowering theme for the Hadamard binary product leaf `elementwise_product`. The rewrite is
**identity-in-form on the body** with **no wrapper rotation** — `elementwise_product` is a leaf
whole-tensor binary field operation, not a step body, so the L3
[`elementwise_product`](../L3/elementwise_product.md) whole-tensor form lowers into the L2
[`elementwise_product`](../L2/elementwise_product.md) floor form by the identity on the primitive
itself. There is no `(op, K, s)`→`IterState` consolidation and no outer-loop dissolution to perform
(the two surface adjustments the sibling [`krylov-step-body-identity`](./krylov-step-body-identity.md)
carries at its wrapper); `elementwise_product` has no wrapper. The body IS the identity. This is the
leaf-primitive analogue of `krylov-step-body-identity`, the direct sibling of
[`scal-body-identity`](./scal-body-identity.md) and [`reciprocal-body-identity`](./reciprocal-body-identity.md),
and — like those — **fold-parent-free** at L2: `elementwise_product` is fork-INDEPENDENT, neither a
member of `inner_product` nor of `linear_combination`.

## Slug

`elementwise-product-body-identity`

> **Filename-convention note (normalized cycle-043).** This chapter uses the **hyphen** spelling
> `elementwise-product-body-identity.md`, matching its hyphenated L2>L1 sibling
> `elementwise-product-leaf-identity.md` and the uniform `-leaf-identity` / `-body-identity`
> theme-slug convention ratified by the batch-12 meta-phase. The underscore operator chapters
> (`L1/L2/L3 elementwise_product.md`) keep the underscore spelling that matches the firm operator
> entries; the theme slugs are hyphenated. This resolves the cycle-042 underscore-vs-hyphen split
> (the theme slug was originally underscored to match the operator chapters; the batch-12
> normalization moved all theme slugs to hyphen).

## Context

The `elementwise_product` lowering relationships span three adjacent layers, all identity-in-form
because `elementwise_product` is a binary elementwise leaf with no iteration view and no kernel fusion:

- **L3 form** ([`L3/elementwise_product`](../L3/elementwise_product.md), firm cycle-038) — the
  whole-tensor binary field operation `elementwise_product :: (Tensor[N], Tensor[N]) -> Tensor[N]`, the
  iteration-rotation rendering. Carries **no iteration view** (leaf primitive, not a step body) and
  **no sequential obstruction** (every element independent under the per-element multiply). The LHS of
  this theme.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/elementwise_product`](../L2/elementwise_product.md), firm cycle-042 D3) — the
  fusion-rotation floor leaf, the base Hadamard-binary-multiply primitive and the diagonal-operator
  apply primitive. **No fold-parent (fork-INDEPENDENT).** The RHS of this theme.
- **L2>L1 form** ([`L2-L1/elementwise-product-leaf-identity`](../L2-L1/elementwise-product-leaf-identity.md),
  firm cycle-042 D10) — the onward edge into the L1 leaf; also identity-in-form.

This theme is the **leaf-primitive counterpart** of the firm
[`krylov-step-body-identity`](./krylov-step-body-identity.md) (cycle-007/009), and the direct sibling
of [`scal-body-identity`](./scal-body-identity.md) and
[`reciprocal-body-identity`](./reciprocal-body-identity.md). The `krylov-step` theme establishes the
pattern "identity-in-form on the kernel **body**, with surface adjustments at the **wrapper**"; its
point-3 applicability condition (`krylov-step-body-identity.md:97`) names the seven BLAS-1 primitives as
L3-native by signature shape ("each operates on whole-tensor inputs with no element-loop exposed at
L2"). `elementwise_product` is the **binary Hadamard** realization of the same classification (it is not
one of the named seven, but it is L3-native by the identical signature criterion —
`(Tensor[N], Tensor[N]) -> Tensor[N]` exposes no per-element loop): the body is the identity, **and
there is no wrapper at all** — `elementwise_product` is not a step body, so the two wrapper adjustments
the `krylov-step` theme carries have no analog here.

The firm L3 entry (`book/src/L3/elementwise_product.md:149` §"Lowers to") currently records its
lowering as direct L3>L1 identity-in-form ("no interposed L2 entry, no L3-L2/L3-L1 theme file") via the
non-adjacent in-line convention, because no L2 `elementwise_product` chapter existed. With the L2
`elementwise_product` floor now present (D3), this theme supplies the **adjacent-edge** L3>L2 rotation
the L3 entry's §"Lowers to" had to skip — so the L3 leaf lowers to an adjacent same-named L2 parent
(per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**) rather than
non-adjacently to L1.

## L3 form (LHS)

The L3 whole-tensor form ([`L3/elementwise_product`](../L3/elementwise_product.md) §Signature, firm
cycle-038):

    elementwise_product :: (a: Tensor[N], b: Tensor[N]) -> Tensor[N]
    elementwise_product(a, b) = a ⊙ b               -- result[i] = a[i] · b[i]

with the conjugate variant (complex element-type only) as a sub-axis:

    elementwise_product_conj(a, b) = ā ⊙ b

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `a, b : Tensor[N]`
share a single length axis and element type, read-only at L3; result `Tensor[N]` of the same axis with
`result[i] = a[i]·b[i]` for every `i ∈ [0, N)`. The operator carries **no iteration view** (leaf binary
field operation, not a step body) and **no sequential obstruction** (every element independent —
embarrassingly parallel, fully GPU-friendly). No L4 wrapper machinery applies (the cross-layer
audit's "L4 candidate CONFIRMED-NOT-NEEDED" verdict for `elementwise_product`,
`book/src/L3/elementwise_product.md:26`).

## L2 form (RHS)

The L2 floor form ([`L2/elementwise_product`](../L2/elementwise_product.md) §Signature, firm cycle-042
D3):

    elementwise_product :: (a: Tensor[N], b: Tensor[N]) -> Tensor[N]
    elementwise_product(a, b) = a ⊙ b

The base Hadamard-binary-multiply leaf in the fusion-rotation vocabulary — a **standalone binary field
operation, fork-INDEPENDENT, NO fold-parent** (neither the length-axis fold `inner_product`
reduce-to-`Scalar` nor the term-axis fold `linear_combination` reduce-to-`Tensor[N]`). The signature is
**textually identical to the L3 form** modulo notation; the body is the same single whole-tensor binary
field operation. The ten algebraic laws and the two variant axes (element-type + conjugation sub-axis)
hold unchanged across the edge (L3 §Algebraic laws ≡ L2 §Algebraic laws — both inherit the L1 leaf's
ten laws). There is **no fold-level fusion note** to carry (no fold-parent, no multi-operation fusion);
the L0 `forall_switch` per-element multiply is already the unfolded single-pass form.

## The rewrite (L3 → L2)

The rewrite is the **identity on the leaf primitive's body**, with **no wrapper adjustment**:

    elementwise_product(a, b)   (L3 whole-tensor field op)   ⇒   elementwise_product(a, b)   (L2 floor leaf)

The body maps trivially — one binding, one primitive, same position, same dataflow:

    | L3 form (`L3/elementwise_product`)             | L2 form (`L2/elementwise_product`)             | Mapping  |
    |------------------------------------------------|------------------------------------------------|----------|
    | `elementwise_product(a, b) = a ⊙ b` (whole-tensor binary field op; no iteration view) | `elementwise_product(a, b) = a ⊙ b` (base Hadamard floor leaf; NO fold-parent) | Identity. Same signature, same single binary field operation. The only framing difference is documentary: L3 frames it in the iteration-rotation vocabulary; L2 frames the same operator as a base fusion-rotation primitive (and the diagonal-operator apply primitive, law 9). No operational adjustment. |
    | conjugate variant `ā ⊙ b`                      | conjugate variant `ā ⊙ b`                      | Identity. Same complex-side conjugation sub-axis. |
    | algebraic laws 1–10                            | algebraic laws 1–10                            | Identity. Inherited unchanged across the chain. |
    | two variant axes: element-type + conjugation   | two variant axes: element-type + conjugation   | Identity. Real/complex collapsed; conjugation sub-axis on the complex side. |
    | no iteration view, no obstruction              | no fold-parent, no fusion                      | Identity. Nothing to rotate (leaf, no loop) and nothing to de-fuse (no fold, the per-element pass is already unfolded). |

The mapping is total and bijective on a single binding — the degenerate maximal case of the
identity-in-form property.

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two surface
adjustments at the wrapper around its kernel body — the L3 `(op, K, s)` positional tuple consolidating
into the L2 `IterState` record, and the L3 tail-recursive outer loop collapsing to the L2
outer-driver-by-role reference. **Neither has an analog for `elementwise_product`**: it is a single
leaf binary field operation, not a step body with an `(op, K, s)` carrier and an outer loop. This is
identical in shape to [`scal-body-identity`](./scal-body-identity.md) and
[`reciprocal-body-identity`](./reciprocal-body-identity.md): the body IS the identity, there is no
wrapper, and (additionally) there is no fold-parent to defer to.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `elementwise_product` endpoints)
when:

1. **`elementwise_product` is treated as a leaf primitive, not decomposed.** `elementwise_product` does
   not decompose into other L3 or L2 primitives — the Hadamard binary multiply is a single field
   operation; its sub-operation (per-element scalar multiplication of two operands) is below both
   layers' resolution. It has **no fold-parent** (fork-INDEPENDENT; D3 establishes this), so — unlike
   the fold-member BLAS-1 body-identity themes (`dot-body-identity` Applicability condition 2,
   `scal-body-identity` §Status) — there is **no leaf-floor-vs-fold-only design presupposition** for
   this theme's RHS (see §Status). (Note the inverse-subsumption sibling relationship
   `scal(α, x) = elementwise_product(broadcast(α, N), x)` is a derived identity, not a fold membership;
   `elementwise_product` *generalises* `scal`.)

2. **The signature is whole-tensor at both layers** — `(Tensor[N], Tensor[N]) -> Tensor[N]` with no
   per-element loop exposed at L2 and no iteration view at L3. This is the `krylov-step-body-identity`
   point-3 condition applied to the standalone `elementwise_product` leaf: its signature has no
   per-element loop visible, so it is L3-native by construction and the rotation is identity-in-form
   rather than a decomposition.

3. **No iteration view, no sequential obstruction, no fold-level fusion.** `elementwise_product` is
   element-local, reduction-free, rank-local; every element is independent. There is no outer loop, no
   carry trajectory, no recurrence — nothing for the L3 iteration rotation to have rotated and nothing
   for the L3>L2 lowering to dissolve. There is also no fold-parent and no multi-operation kernel
   fusion (the L0 `forall_switch` per-element multiply is the unfolded single-pass form).

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the leaf's signature shape `(Tensor[N], Tensor[N]) -> Tensor[N]` is
whole-tensor by construction at both layers — no element loop is exposed at L2, no iteration view at L3.
The L3 vocabulary at this scope demands whole-tensor field operations with no element loop exposed;
`elementwise_product` satisfies this *at L2 already*, so the rotation is the identity. This is the same
structural argument `scal-body-identity` / `reciprocal-body-identity` make (and
`krylov-step-body-identity` point-3 makes for each primitive in the kernel body), here promoted to
dominant because there is no kernel body wrapping the leaf, only the leaf itself.

**Empirical-match (secondary)**: the L3 leaf (firm cycle-038) and the L2 floor (firm cycle-042 D3) were
authored independently as value-thread-isomorphic to the same firm L1 leaf (cycle-019/032/036), and
they agree on every law, both variant axes (element-type + conjugation sub-axis), and the
diagonal-operator-action law 9 by independent transcription. The cycle-036 D2 cross-layer-cross-cutter
L3-cohort-growth audit (`book/src/L3/index.md:41`) classified `elementwise_product` ("Hadamard binary")
as an **(A) identity-in-form** backfill candidate; this theme's L3>L2 edge is the standalone-leaf
realization of that audited classification, now that the L2 floor entry exists for the rotation to
target.

## Speculative L2 operators

**None.** This theme is the identity rotation between firm endpoints: the L3 LHS
([`L3/elementwise_product`](../L3/elementwise_product.md)) is firm (cycle-038), and the L2 RHS
([`L2/elementwise_product`](../L2/elementwise_product.md)) is firm (cycle-042 D3). No new L2 vocabulary
is introduced. `elementwise_product` does not get its own L4 typed-wrapper anchor (the cross-layer "L4
candidate CONFIRMED-NOT-NEEDED" verdict, `book/src/L3/elementwise_product.md:26`), so there is no
upstream L4>L3 theme for `elementwise_product` either; the L3 form is L3-native by signature and this
theme closes its downward edge to the L2 floor.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/elementwise_product.md` (firm cycle-038) — the L3 whole-tensor form (LHS). Signature
  (:34-45), semantics (element-local, reduction-free, rank-local, no iteration view, no sequential
  obstruction), ten algebraic laws (:74-87), the two variant axes (element-type + conjugation sub-axis,
  :124-137), the §"Lowers to" currently recording direct L3>L1 identity via the non-adjacent convention
  (:147-151) — this theme supplies the now-present adjacent L3>L2 edge (downstream-consistency touch on
  the L3 entry flagged in §Open-questions of the authoring report).
- `book/src/L2/elementwise_product.md` (firm cycle-042 D3) — the L2 floor form (RHS). Identical
  signature and ten laws; the standalone Hadamard binary field operation framing + the
  fork-INDEPENDENT / no-fold-parent / design-final determination. (Lands at this cycle's integration
  alongside this theme.)
- `book/src/L3-L2/scal-body-identity.md` + `book/src/L3-L2/reciprocal-body-identity.md` (firm cycle-041
  / cycle-042 D10) — the direct sibling shapes: fold-free leaf body-identity edges, "no wrapper to
  rotate, the body IS the identity". The structure of this theme is inherited from them.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (firm cycle-007/009) — §"Applicability conditions"
  point 3: the L3-native-by-signature-shape classification (no per-element loop visible) that is the
  structural justification for this identity edge. **Self-verified (anchor `L3-native` @97 — confirmed
  by the firm `dot-body-identity` / `scal-body-identity` themes that cite the same line).**

L0 evidence (transitive through the firm L1 leaf; self-verified via `tools/citecheck/citecheck.py
--anchor` this invocation, all `[ok]`; paths relative to `reference/palace/`):

- `palace/linalg/operator.cpp:478-487` — real canonical `BaseDiagonalOperator<Operator>::Mult`, the
  per-element body `Y[i] = D[i] * X[i]` at `:486`. **Self-verified (anchor `Mult` @479; `Y[i] = D[i] *
  X[i]` @486).** Inherited transitively; the leaf's edge is identity, no new L0 claim.
- `palace/linalg/operator.cpp:545-568` — complex conjugate-variant
  `DiagonalOperatorHelper<…>::MultHermitianTranspose`, the two-sign-flip kernel realising `d̄ ⊙ x`.
  **Self-verified (anchor `MultHermitianTranspose` @548).** Witnesses the conjugation sub-axis.

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS
([`L3/elementwise_product`](../L3/elementwise_product.md)) is firm (cycle-038); the L2 RHS
([`L2/elementwise_product`](../L2/elementwise_product.md)) is firm (cycle-042 D3). The body is the
identity rotation on a single leaf binary field operation; **there is no wrapper to rotate** (no
`(op, K, s)`→`IterState` consolidation, no outer-loop dissolution — `elementwise_product` is a leaf,
not a step body) and **no fold-parent to defer fusion to** (fork-INDEPENDENT). The structural
justification (whole-tensor signature, no element loop, no iteration view) is the
`krylov-step-body-identity` point-3 condition specialized to the standalone leaf and promoted to
dominant; the empirical-match anchor is the firm L1/L2/L3 value-thread-isomorphic chain + the
cycle-036 cross-layer (A) identity-in-form classification. No speculative operator, no negative-anchor
reconstruction, no sequential obstruction. The direct sibling of `scal-body-identity` /
`reciprocal-body-identity` — the leaf-primitive counterpart of `krylov-step-body-identity`,
additionally fork-independent.

> **Design-final on the leaf-vs-fold fork (NOT a presupposition).** The batch-12 meta-phase fork
> `dot-l2-leaf-floor-vs-fold-only-design` concerns the L2 *fold-member* BLAS-1 leaves.
> `elementwise_product` has **no fold-parent** (it is the inverse-subsumption *generalisation* of
> `scal`, not a fold member), so its L2 RHS can only ever be a same-named standalone floor — neither
> the (a) fold-only nor the (b) same-named-floor reading re-anchors it. Unlike `dot-body-identity` /
> `scal-body-identity` (whose §Status carries a design-presupposition note), this theme's RHS is
> design-final; the identity claim does not depend on the fork's outcome.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L2 floor leaf *up* to the L3 whole-tensor form is the value-thread-isomorphic identity
  rotation: the L2 signature has no element loop exposed, which is exactly what makes it L3-native by
  construction. No additional structure is required for the lift. This reverse-direction note lives
  here in working notes per the high→low layer-definition discipline; the formal chapter narrates only
  L3 → L2.

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (this
  theme's L3>L2 identity ∘ the L2>L1 `elementwise-product-leaf-identity` identity) is annotated in-line
  at the `elementwise_product` entries per the CLAUDE.md invariant "Identity rotations across
  non-adjacent layers are annotated in-line, not via a dedicated lowering directory" — no
  `book/src/L3-L1/` directory. This theme + the co-dispatched `elementwise-product-leaf-identity`
  compose to capture it. The firm L3 entry's §"Lowers to" still records the historical direct L3>L1
  identity; a downstream-consistency touch re-anchoring it to the now-present adjacent edges is a
  follow-up (flagged in the authoring report).

- **Filename convention (normalized cycle-043).** This theme is now `-`-spelled
  (`elementwise-product-body-identity.md`, matching the hyphenated theme-slug convention) and its
  L2>L1 sibling is likewise `-`-spelled (`elementwise-product-leaf-identity.md`). The batch-12
  meta-phase normalized all theme slugs to the uniform `-leaf-identity` / `-body-identity` hyphen
  convention; the underscore operator chapters are unaffected. Surfaced for the batch-12 meta-phase to
  normalize the operator-chapter / theme-slug / concept-page slug spelling across the artifact.

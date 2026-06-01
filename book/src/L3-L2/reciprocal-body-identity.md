# reciprocal-body-identity

The L3>L2 lowering theme for the elementwise multiplicative-inverse leaf `reciprocal`. The rewrite is
**identity-in-form on the body** with **no wrapper rotation** — `reciprocal` is a leaf whole-tensor
field operation, not a step body, so the L3 [`reciprocal`](../L3/reciprocal.md) whole-tensor form
lowers into the L2 [`reciprocal`](../L2/reciprocal.md) floor form by the identity on the primitive
itself. There is no `(op, K, s)`→`IterState` consolidation and no outer-loop dissolution to perform
(the two surface adjustments the sibling [`krylov-step-body-identity`](./krylov-step-body-identity.md)
carries at its wrapper); `reciprocal` has no wrapper. The body IS the identity. This is the
leaf-primitive analogue of `krylov-step-body-identity`, the direct sibling of
[`scal-body-identity`](./scal-body-identity.md) and [`dot-body-identity`](./dot-body-identity.md), and
— like `scal-body-identity` and unlike the fold-member BLAS-1 leaves — **fold-parent-free**: there is
no fold-parent at L2 for the leaf's fusion content to belong to (there is no fusion to begin with).

## Slug

`reciprocal-body-identity`

## Context

The `reciprocal` lowering relationships span three adjacent layers, all identity-in-form because
`reciprocal` is an elementwise leaf with no iteration view and no kernel fusion:

- **L3 form** ([`L3/reciprocal`](../L3/reciprocal.md), firm cycle-038) — the whole-tensor field
  operation `reciprocal :: Tensor[N] -> Tensor[N]`, the iteration-rotation rendering. Carries **no
  iteration view** (leaf primitive, not a step body) and **no sequential obstruction** (every element
  independent under the per-element reciprocation). Partial at `x[i] = 0`. The LHS of this theme.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/reciprocal`](../L2/reciprocal.md), firm cycle-042 D2) — the fusion-rotation floor
  leaf, the base elementwise multiplicative-inverse primitive. **No fold-parent** (a nonlinear
  self-map, not a member of `inner_product` or `linear_combination`). The RHS of this theme.
- **L2>L1 form** ([`L2-L1/reciprocal-leaf-identity`](../L2-L1/reciprocal-leaf-identity.md), firm
  cycle-042 D10) — the onward edge into the L1 leaf; also identity-in-form.

This theme is the **leaf-primitive counterpart** of the firm
[`krylov-step-body-identity`](./krylov-step-body-identity.md) (cycle-007/009), and the direct sibling
of [`scal-body-identity`](./scal-body-identity.md) (cycle-041). The `krylov-step` theme establishes the
pattern "identity-in-form on the kernel **body**, with surface adjustments at the **wrapper**"; its
point-3 applicability condition (`krylov-step-body-identity.md:97`) names the seven BLAS-1 primitives
as L3-native by signature shape: "each operates on whole-tensor inputs with no element-loop exposed at
L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step."
`reciprocal` is the **elementwise self-map** realization of the same classification (it is not one of
the named seven, but it is L3-native by the identical signature criterion — `Tensor[N] -> Tensor[N]`
exposes no per-element loop): the body is the identity, **and there is no wrapper at all** —
`reciprocal` is not a step body, so the two wrapper adjustments the `krylov-step` theme carries have no
analog here.

The firm L3 entry (`book/src/L3/reciprocal.md:131` §"Lowers to") currently records its lowering as
direct L3>L1 identity-in-form ("no interposed L2 entry, no L3-L2/L3-L1 theme file") via the
non-adjacent in-line convention, because no L2 `reciprocal` chapter existed. With the L2 `reciprocal`
floor now present (D2), this theme supplies the **adjacent-edge** L3>L2 rotation the L3 entry's
§"Lowers to" had to skip — so the L3 leaf lowers to an adjacent same-named L2 parent (per CLAUDE.md
§Methodology invariants **Identity-lowerings still require both L levels**) rather than non-adjacently
to L1.

## L3 form (LHS)

The L3 whole-tensor form ([`L3/reciprocal`](../L3/reciprocal.md) §Signature, firm cycle-038):

    reciprocal :: Tensor[N] -> Tensor[N]
    reciprocal x = (\i -> 1 / x[i])     for i in [0, N)

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `x : Tensor[N]` a
single length axis, read-only at L3; result `Tensor[N]` of the same axis and element type with
`result[i] = 1/x[i]` for every `i ∈ [0, N)` (real `1/x[i]`; complex `z̄/|z|²`). Partial at `x[i] = 0`
(the precondition `x[i] ≠ 0`, recorded once). The operator carries **no iteration view** (leaf field
operation, not a step body) and **no sequential obstruction** (every element independent —
embarrassingly parallel, fully GPU-friendly). No L4 wrapper machinery applies (leaf primitives appear
inside L4 operator bodies as let-bindings, not first-class L4 typed-wrapper anchors — the cross-layer
"L4 candidate CONFIRMED-NOT-NEEDED" verdict for the elementwise / BLAS-1 cohort).

## L2 form (RHS)

The L2 floor form ([`L2/reciprocal`](../L2/reciprocal.md) §Signature, firm cycle-042 D2):

    reciprocal :: Tensor[N] -> Tensor[N]
    reciprocal x = (\i -> 1 / x[i])     for i in [0, N)

The base elementwise multiplicative-inverse leaf in the fusion-rotation vocabulary — a **standalone
elementwise leaf with NO fold-parent** (a nonlinear self-map, `1/(a+b) ≠ 1/a + 1/b`, not a member of
the length-axis fold `inner_product` nor the term-axis fold `linear_combination`). The signature is
**textually identical to the L3 form** modulo notation; the body is the same single whole-tensor field
operation. The eight algebraic laws hold unchanged across the edge (L3 §Algebraic laws ≡ L2 §Algebraic
laws — both inherit the L1 leaf's eight laws). There is **no fold-level fusion note** to carry (no
fold-parent, no multi-operation fusion); the only note either floor records is the transparent
`s = 1/|z|²` complex-intermediate factoring, and at L3 even that drops below the whole-tensor
resolution.

## The rewrite (L3 → L2)

The rewrite is the **identity on the leaf primitive's body**, with **no wrapper adjustment**:

    reciprocal x   (L3 whole-tensor field op)   ⇒   reciprocal x   (L2 floor leaf)

The body maps trivially — one binding, one primitive, same position, same dataflow:

    | L3 form (`L3/reciprocal`)              | L2 form (`L2/reciprocal`)              | Mapping  |
    |----------------------------------------|----------------------------------------|----------|
    | `reciprocal x = (\i -> 1/x[i])` (whole-tensor field op; no iteration view) | `reciprocal x = (\i -> 1/x[i])` (base elementwise floor leaf; NO fold-parent) | Identity. Same signature, same single elementwise field operation. The only framing difference is documentary: L3 frames `reciprocal` as a whole-tensor field op in the iteration-rotation vocabulary; L2 frames the same operator as a base fusion-rotation primitive. No operational adjustment. |
    | partial: `x[i] ≠ 0`                    | partial: `x[i] ≠ 0`                    | Identity. Same partiality precondition. |
    | algebraic laws 1–8                     | algebraic laws 1–8                     | Identity. Inherited unchanged across the chain. |
    | element-type variant axis              | element-type variant axis              | Identity. Real/complex collapsed; result element type tracks input. |
    | no iteration view, no obstruction      | no fold-parent, no fusion              | Identity. Nothing to rotate (leaf, no loop) and nothing to de-fuse (no fold, no multi-op fusion). |

The mapping is total and bijective on a single binding — the degenerate maximal case of the
identity-in-form property.

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two surface
adjustments at the wrapper around its kernel body — the L3 `(op, K, s)` positional tuple consolidating
into the L2 `IterState` record, and the L3 tail-recursive outer loop collapsing to the L2
outer-driver-by-role reference. **Neither has an analog for `reciprocal`**: it is a single leaf field
operation, not a step body with an `(op, K, s)` carrier and an outer loop. This is identical in shape
to [`scal-body-identity`](./scal-body-identity.md): the body IS the identity, there is no wrapper, and
(additionally) there is no fold-parent to defer to.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `reciprocal` endpoints) when:

1. **`reciprocal` is treated as a leaf primitive, not decomposed.** `reciprocal` does not decompose
   into other L3 or L2 primitives — elementwise multiplicative inversion is a single field operation;
   its sub-operation (scalar reciprocation in the element field) is below both layers' resolution. It
   has **no fold-parent** (a nonlinear self-map; D2 establishes this), so — unlike the fold-member
   BLAS-1 body-identity themes (`dot-body-identity` Applicability condition 2,
   `scal-body-identity` §Status) — there is **no leaf-floor-vs-fold-only design presupposition** for
   this theme's RHS (see §Status).

2. **The signature is whole-tensor at both layers** — `Tensor[N] -> Tensor[N]` with no per-element
   loop exposed at L2 and no iteration view at L3. This is the `krylov-step-body-identity` point-3
   condition applied to the standalone `reciprocal` leaf: its signature has no per-element loop
   visible, so it is L3-native by construction and the rotation is identity-in-form rather than a
   decomposition.

3. **No iteration view, no sequential obstruction, no fold-level fusion.** `reciprocal` is
   element-local, reduction-free, rank-local; every element is independent. There is no outer loop, no
   carry trajectory, no recurrence — nothing for the L3 iteration rotation to have rotated and nothing
   for the L3>L2 lowering to dissolve. There is also no fold-parent and no multi-operation kernel
   fusion (the transparent `s = 1/|z|²` factoring is below the whole-tensor resolution at L3).

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the leaf's signature shape `Tensor[N] -> Tensor[N]` is whole-tensor by
construction at both layers — no element loop is exposed at L2, no iteration view at L3. The L3
vocabulary at this scope demands whole-tensor field operations with no element loop exposed;
`reciprocal` satisfies this *at L2 already*, so the rotation is the identity. This is the same
structural argument `scal-body-identity` makes (and `krylov-step-body-identity` point-3 makes for each
primitive in the kernel body), here promoted to dominant because there is no kernel body wrapping the
leaf, only the leaf itself.

**Empirical-match (secondary)**: the L3 leaf (firm cycle-038) and the L2 floor (firm cycle-042 D2) were
authored independently as value-thread-isomorphic to the same firm L1 leaf (cycle-033), and they agree
on every law, the single variant axis (element-type), and the partiality precondition by independent
transcription. The cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit
(`book/src/L3/index.md:41`) classified `reciprocal` as an **(A) identity-in-form** backfill candidate;
this theme's L3>L2 edge is the standalone-leaf realization of that audited classification, now that the
L2 floor entry exists for the rotation to target.

## Speculative L2 operators

**None.** This theme is the identity rotation between firm endpoints: the L3 LHS
([`L3/reciprocal`](../L3/reciprocal.md)) is firm (cycle-038), and the L2 RHS
([`L2/reciprocal`](../L2/reciprocal.md)) is firm (cycle-042 D2). No new L2 vocabulary is introduced.
`reciprocal` does not get its own L4 typed-wrapper anchor (leaf primitives appear inside L4 operator
bodies as let-bindings — the cross-layer "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the
elementwise cohort), so there is no upstream L4>L3 theme for `reciprocal` either; the L3 form is
L3-native by signature and this theme closes its downward edge to the L2 floor.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/reciprocal.md` (firm cycle-038) — the L3 whole-tensor form (LHS). Signature (:31),
  semantics (element-local, reduction-free, rank-local, no iteration view, no sequential obstruction),
  eight algebraic laws (:63-84), the single element-type variant axis (:105-119), the §"Lowers to"
  currently recording direct L3>L1 identity via the non-adjacent convention (:129-135) — this theme
  supplies the now-present adjacent L3>L2 edge (downstream-consistency touch on the L3 entry flagged in
  §Open-questions of the authoring report).
- `book/src/L2/reciprocal.md` (firm cycle-042 D2) — the L2 floor form (RHS). Identical signature and
  eight laws; the standalone elementwise leaf framing + the no-fold-parent / design-final
  determination. (Lands at this cycle's integration alongside this theme.)
- `book/src/L3-L2/scal-body-identity.md` (firm cycle-041) — the direct sibling shape: a fold-free leaf
  body-identity edge, "no wrapper to rotate, the body IS the identity". The structure of this theme is
  inherited from it.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (firm cycle-007/009) — §"Applicability conditions"
  point 3: the L3-native-by-signature-shape classification (no per-element loop visible) that is the
  structural justification for this identity edge. **Self-verified (anchor `L3-native` @97 — confirmed
  by the firm `dot-body-identity` / `scal-body-identity` themes that cite the same line).**

L0 evidence (transitive through the firm L1 leaf; self-verified via `tools/citecheck/citecheck.py
--anchor` this invocation, all `[ok]`; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:248-261` — `ComplexVector::Reciprocal()` body (the closed-form
  `s = 1/(XR²+XI²); XR *= s; XI *= -s` complex kernel). **Self-verified (anchor `Reciprocal` @248).**
  Inherited transitively; the leaf's edge is identity, no new L0 claim.
- `palace/linalg/vector.cpp:257-259` — the three-line per-element kernel. **Self-verified (anchor `XR`
  @257-258).**
- `palace/linalg/vector.hpp:20` — `using Vector = mfem::Vector;` — the real-path alias (real
  element-type case). **Self-verified (anchor `mfem::Vector` @20).**

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS
([`L3/reciprocal`](../L3/reciprocal.md)) is firm (cycle-038); the L2 RHS
([`L2/reciprocal`](../L2/reciprocal.md)) is firm (cycle-042 D2). The body is the identity rotation on a
single leaf field operation; **there is no wrapper to rotate** (no `(op, K, s)`→`IterState`
consolidation, no outer-loop dissolution — `reciprocal` is a leaf, not a step body) and **no
fold-parent to defer fusion to** (a nonlinear self-map). The structural justification (whole-tensor
signature, no element loop, no iteration view) is the `krylov-step-body-identity` point-3 condition
specialized to the standalone leaf and promoted to dominant; the empirical-match anchor is the firm
L1/L2/L3 value-thread-isomorphic chain + the cycle-036 cross-layer (A) identity-in-form classification.
No speculative operator, no negative-anchor reconstruction, no sequential obstruction. The direct
sibling of `scal-body-identity` — the leaf-primitive counterpart of `krylov-step-body-identity`,
additionally fold-free.

> **Design-final on the leaf-vs-fold fork (NOT a presupposition).** The batch-12 meta-phase fork
> `dot-l2-leaf-floor-vs-fold-only-design` concerns the L2 *fold-member* BLAS-1 leaves. `reciprocal`
> has **no fold-parent**, so its L2 RHS can only ever be a same-named standalone floor — neither the
> (a) fold-only nor the (b) same-named-floor reading re-anchors it. Unlike `dot-body-identity` /
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
  theme's L3>L2 identity ∘ the L2>L1 `reciprocal-leaf-identity` identity) is annotated in-line at the
  `reciprocal` entries per the CLAUDE.md invariant "Identity rotations across non-adjacent layers are
  annotated in-line, not via a dedicated lowering directory" — no `book/src/L3-L1/` directory. This
  theme + the co-dispatched `reciprocal-leaf-identity` compose to capture it. The firm L3 entry's
  §"Lowers to" still records the historical direct L3>L1 identity; a downstream-consistency touch
  re-anchoring it to the now-present adjacent edges is a follow-up (flagged in the authoring report).

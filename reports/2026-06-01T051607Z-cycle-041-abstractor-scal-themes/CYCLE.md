---
agent: abstractor
invoked_at: 2026-06-01T051607Z
scope: TWO adjacent thin-identity lowering themes for `scal` — L2>L1 `scal-fold-specialization` + L3>L2 `scal-body-identity` (cycle-041 D6, wave-2)
status: pending
integrated_at: 2026-06-01T062913Z
integration_commit: c1f7ea3c651e65ed212aa8500c7c8572aaa2ec92
integration_notes: "Applied clean (staging row D6). L2-L1/scal-fold-specialization.md + L3-L2/scal-body-identity.md created firm. vector.cpp:207-211 pinpoint kept UNCHANGED. Non-adjacent L3>L1 scal identity stays in-line (no L3-L1/ directory). Third divergent-slug data point (scal-fold-specialization vs dot-leaf-identity) for batch-12 meta-phase. L2>L1 firm 7->10, L3>L2 firm 2->5."
inputs:
  - reports/2026-06-01T051607Z-cycle-041-harvester-L2-scal/CYCLE.md (wave-1 D3; the source-of-truth L2 `scal` floor body — lands at integration alongside these themes)
  - book/src/L1/scal.md (firm cycle-004; L1 leaf RHS for L2>L1)
  - book/src/L3/scal.md (firm cycle-011; L3 whole-tensor LHS for L3>L2)
  - book/src/L2/scal.md (the wave-1 D3 floor entry; L2 RHS for L3>L2 + L2 LHS for L2>L1)
  - book/src/L1-L0/scal-mutation-rotation.md (firm; the onward L1>L0 lowering the L2 pure form abstracts over)
  - book/src/L3-L2/krylov-step-body-identity.md (mirror precedent; classifies `scal` as L3-native at point-3)
  - book/src/L2-L1/linear-combination-fold-specialization.md (fold-parent's own specialization theme; cited as fold-parent, NOT merged)
  - book/src/L2-L1/gram-fold-specialization.md + index.md (sibling `-fold-specialization` slug convention)
  - book/src/L2/linear_combination.md:68 (arity-1 specialization identity `scal(α,x) = linear_combination [(α,x)]`)
  - palace/linalg/vector.cpp:203-227 ; vector.hpp:98-99,262-270 (transitive L0 anchors; self-verified via citecheck --anchor)
---

# CYCLE: TWO adjacent thin-identity lowering themes for `scal` — `scal-fold-specialization` (L2>L1) + `scal-body-identity` (L3>L2)

## Summary

The firm L1 [`scal`](../L1/scal.md) (cycle-004), firm L3 [`scal`](../L3/scal.md)
(cycle-011), and the wave-1 D3 L2 floor [`scal`](../L2/scal.md) (lands this cycle)
together leave **two adjacent lowering edges unwritten**: the L2>L1 edge (how the L2
floor form lowers into the L1 leaf) and the L3>L2 edge (how the L3 whole-tensor form
lowers into the L2 floor form). Both are **identity-in-form** — `scal` is a BLAS-1 leaf
whose signature `Scalar -> Tensor[N] -> Tensor[N]` is textually identical across L1 / L2
/ L3, with no kernel fusion to unfold beyond the degenerate arity-1 single-aligned pass
and no iteration view to dissolve. This dispatch authors the two thin identity themes:

- **`scal-fold-specialization`** (`book/src/L2-L1/scal-fold-specialization.md`) — the
  L2>L1 edge. `scal` is the **arity-1 member of the `linear_combination` fold**; this
  theme is the **degenerate single-term shadow** of the firm
  [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md)
  (cited as fold-parent, **NOT merged** — the fold-cohort boundary at
  `book/src/L2/index.md` §"Fold-cohort boundary" is load-bearing). The fusion-selection
  rotation collapses to the single arity-1 row (`linear_combination [(α, x)] ⇒ scal(α, x)`,
  `linear_combination.md:68`); there is no arity dispatch and no pinned-summation-order
  table (one term ⇒ one rounding, nothing to re-associate). Status `firm`
  (identity-in-form floor edge; both endpoints firm).

- **`scal-body-identity`** (`book/src/L3-L2/scal-body-identity.md`) — the L3>L2 edge.
  Mirrors the firm [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md)
  (which classifies `scal` as L3-native at its point-3 applicability condition), but with
  **no wrapper rotation** — `scal` is a leaf field operation, not a step body, so there
  is no `(op, K, s)`→`IterState` consolidation and no outer-loop dissolution. The body IS
  the identity; there is no wrapper. Status `firm` (identity-in-form on the body; both
  endpoints firm).

Narrated FORWARD (L_{n+1} LHS → L_n RHS), high→low per the layer-definition discipline.
Both themes are built on the **(b) same-named-floor realization** (D3's): `scal` exists
as its own standalone L2 floor entry, cited as the arity-1 fold member but not merged.
**Live design friction surfaced** (§Open questions): the leaf-vs-fold fork is under
batch-12 meta-phase adjudication; if the meta-phase adopts the fold-only reading, both
themes would re-anchor onto `linear_combination` (the L2>L1 edge would fold into
`linear-combination-fold-specialization`'s arity-1 row, and the L3>L2 edge would target
the fold's L2 form). OQ recorded.

**COUNT-OWNERSHIP**: this dispatch appends ONLY its two theme files, two dep-map/theme-list
rows (one per index), and two SUMMARY registrations. It does NOT touch any consolidated
theme-count tally — **D7 owns the tallies this cycle**. Deferred.

## Proposed changes

```new:book/src/L2-L1/scal-fold-specialization.md
# scal-fold-specialization

The degenerate **arity-1** member of the BLAS-1 scalar-weighted-vector-sum
fusion-selection cohort. Lowers the L2 floor primitive [`scal`](../L2/scal.md) into the
L1 leaf [`scal`](../L1/scal.md) via an **identity-in-form** rotation: the signature
`Scalar -> Tensor[N] -> Tensor[N]` is textually identical at both layers, and the single
arity-1 fusion-selection row (`linear_combination [(α, x)] ⇒ scal(α, x)`) carries **no
arity dispatch** and **no pinned-summation-order table** (one term computes one scaled
pass, one rounding per element — there is nothing to re-associate). This theme is the
**single-term shadow** of the firm
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md):
`scal` is the arity-1 member of the [`linear_combination`](../L2/linear_combination.md)
fold, **cited as fold-parent but NOT merged** (the fold-cohort boundary at
`book/src/L2/index.md` §"Fold-cohort boundary" is load-bearing — the leaf keeps its own
one-to-one shape with the L0 `operator*=` symbol that the onward L1>L0 mutation rotation
relies on). The thinnest member of the L2>L1 lowering family.

## Slug

`scal-fold-specialization`

## L2 form (LHS)

The L2 floor form is the standalone leaf scalar-vector-multiply primitive
([`scal`](../L2/scal.md) §Signature):

    scal :: Scalar -> Tensor[N] -> Tensor[N]
    scal α x = α·x

Pure / out-of-place; one scalar `α`, one input tensor `x` of length axis `N`; result of
the same axis `N` with `result[i] = α · x[i]` for every `i ∈ [0, N)`. Element-local,
reduction-free, rank-local. At L2 `scal` is the **base scalar-vector-multiply leaf** —
and **also** the arity-1 member of the variadic [`linear_combination`](../L2/linear_combination.md)
fold (`scal(α, x) = linear_combination [(α, x)]`, `linear_combination.md:68`,
§Algebraic-laws law 6), cited as fold-parent but not merged. The only fusion note the
floor entry carries is the **degenerate arity-1 case of the fold's fusion note**: the
single aligned strided pass computing `α·x[i]` per element is the seed-and-accumulate
fold collapsed to one term (the `foldl` over the singleton `[(α, x)]` reduces to one
scaled accumulate into a zero seed).

## L1 form (RHS)

The L1 leaf form is the mutation-lifted pure-functional rescale
([`scal`](../L1/scal.md) §Signature), mirroring one Palace L0 C++ symbol one-to-one
(`mfem::Vector::operator*=(double)` real / `ComplexVector::operator*=(std::complex<double>)`
complex):

    scal :: (α: Scalar, x: Tensor[N]) -> Tensor[N]
    scal(α, x) = α·x

The L1 signature is **textually identical to the L2 signature** modulo notation
(positional-tuple vs curried arrow). The nine algebraic laws (identity / two absorptions
/ scalar-fusion composition / two distributivities / negation / inverse / field-commutativity)
hold unchanged at both layers (`scal` L1 §Algebraic laws ≡ `scal` L2 §Algebraic laws).
At L1 the term list is **below the layer's resolution** — L1 sees a single fixed-arity
leaf with one scalar and one tensor argument, not a one-element fold.

## The fusion-selection rewrite (L2 → L1)

The lowering is the **arity-1 row** of the fold-specialization selection rule — the
single degenerate case where the term-list length is exactly 1:

    scal α x   ⇒   scal(α, x)            -- arity 1: the identity row

This is the **same arity-1 row** the firm
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md)
already records as `linear_combination [(α, x)] ⇒ scal(α, x)` — viewed there as one row
of the fold's variadic selection table, viewed here as the standalone leaf's own L2>L1
edge. The two views coexist by the fold-cohort boundary: the leaf has its own L2 floor
entry (D3 this cycle), and that floor entry lowers to the L1 leaf directly; the fold's
selection table additionally records this same edge as its arity-1 case. **No
abstraction is imposed and none is removed** — the L2 floor form and the L1 leaf form are
the same operator, written in the same signature, at adjacent layers.

**Why this theme is thinner than its fold-parent.** The
`linear-combination-fold-specialization` theme carries (a) an **arity-dispatch** selection
rule (length-1/2/2/3/≥4 picking `scal`/`axpy`/`axpby`/`axpbypcz` + iterated chain), (b) a
**two-sub-selection** within arity 2 (`axpy` vs `axpby` on the unit-coefficient test), (c)
an **arity-3 → arity-2 fall-through** on the in-source `γ==0` branch, and (d) a
**pinned-summation-order table** (the load-bearing-numerical residue). At arity 1, **all
four collapse to nothing**: there is exactly one term, so no dispatch, no sub-selection,
no fall-through, and the summation order is trivially "one scaled pass, one rounding per
element" — there is no partial-sum schedule to pin because there is no sum (a single
`scal` multiply is not an accumulation). The arity-1 row is **value-exact AND
bit-exact** unconditionally (contrast the fold's arity-≥2 rows, where bit-reproduction
requires matching the pinned order). This is what makes `scal`'s L2>L1 edge
identity-in-form rather than a fusion-selection with a numerical residue.

## Applicability conditions

The identity-in-form rotation is valid (which it is unconditionally for the firm `scal`
endpoints) when:

1. **The L2 form is the standalone `scal` floor leaf** (the arity-1 member of the
   `linear_combination` fold), not the variadic fold itself. If the source form is the
   variadic `linear_combination`, the governing lowering is
   [`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md),
   not this theme — this theme is the single-leaf edge, the fold's arity-1 row factored
   out under the fold-cohort do-NOT-merge boundary.

2. **Single length axis, shared element type.** `x : Tensor[N]` with one length axis; `α`
   and `x` share element type (`real` or `complex`), with a real `α` against a complex
   `x` promoted per [`concepts/scalar-promotion`](../concepts/scalar-promotion.md)
   (the internal `s.imag() == 0.0` branch at `palace/linalg/vector.cpp:207-211`,
   absorbed at construction at L1/L2; not a distinct lowering sub-pattern). Inherited
   unchanged from the L1 leaf.

3. **No kernel fusion to unfold beyond the arity-1 single pass.** `scal` is a leaf — there
   is no multi-operation fused kernel (no `α·x + β·y` pass) to de-fuse. The one fusion
   note (the arity-1 single aligned pass) is the degenerate case of the fold's fusion
   note, and it is transparent-performance (algebraically equal to the unfolded form), so
   it carries no load-bearing-numerical residue at this arity.

## Justification kind

`structural` (dominant) — the rotation re-positions the same operator across the L2/L1
layer boundary with no algebraic restatement of the value: the L2 floor signature and the
L1 leaf signature are textually identical, and the body is the same single scalar-vector
field operation. A secondary `algebraic` flavour is inherited from the fold-parent: the
arity-1 row **is** `linear_combination.md` law 6 (the specialization identity
`scal(α, x) = linear_combination [(α, x)]`) read at the singleton case. Because there is
no arity dispatch and no summation-order residue at arity 1, the governing justification
is the structural identity-in-form on the leaf, not the fold's algebraic selection rule —
hence `structural`, with the fold-membership algebraic identity as the secondary anchor.

This contrasts the fold-parent's `algebraic` classification (whose selection rule IS the
fold's laws 6 + 2 + 5 read as a lowering): at arity 1 those laws degenerate to a single
identity row with no selection to make, so the structural identity dominates.

## Speculative L1 operators

**None.** The L1 RHS leaf [`scal`](../L1/scal.md) is firm (cycle-004), mirroring one
Palace L0 symbol one-to-one; the L2 LHS floor [`scal`](../L2/scal.md) is firm (cycle-041
D3). This theme proposes no new operators — it is the identity-in-form lowering edge
between firm vocabulary on both sides. The fold-parent
[`linear_combination`](../L2/linear_combination.md) is firm (cycle-018); `scal`'s
arity-1 membership is a cited fold-specialization, not a new operator.

## Verified-against

L2 / L1 anchors (firm both sides):

- `book/src/L2/scal.md` (cycle-041 D3 floor) — the L2 floor leaf (LHS). Signature,
  semantics (element-local, reduction-free, rank-local), nine algebraic laws, the
  arity-1 fold-membership identity, two variant axes (element-type + scalar-promotion).
- `book/src/L1/scal.md` (cycle-004 firm) — the L1 leaf (RHS). Identical signature and
  nine laws; the one-to-one L0 `operator*=` symbol shape this edge preserves.
- `book/src/L2/linear_combination.md:68` (cycle-018 firm) — the arity-1 specialization
  identity `scal(α, x) = linear_combination [(α, x)]` (§Signature line 68; §Algebraic-laws
  law 6). The fold-parent membership anchor; cited, NOT merged.
- `book/src/L2-L1/linear-combination-fold-specialization.md` (cycle-018/019 firm) — the
  fold-parent's own specialization theme; this theme is its degenerate arity-1 single-term
  shadow. The arity-1 row there (`linear_combination [(α, x)] ⇒ scal(α, x)`) is the same
  edge this theme records standalone.
- `book/src/L2/index.md` §"Fold-cohort boundary" — the load-bearing do-NOT-merge boundary
  between the leaf and the fold; line 17 names `scal` in the L2 base-primitive vocabulary.
- `scaffolding/decisions/axpby-as-primitive.md` — the fused-leaf decision (keep leaves
  firm, fuse up into the fold, don't merge) governing the leaf-vs-decompose choice.

Onward L1>L0 lowering (the in-place mutation this L2/L1 pure edge abstracts over):

- `book/src/L1-L0/scal-mutation-rotation.md` (firm) — the L1>L0 mutation rotation; the
  in-place `x *= α` receiver-mutating idiom (real Sub-pattern A / complex Sub-pattern B)
  the L2 floor and L1 leaf both abstract over. Confirms no free-function `linalg::Scal`/
  `linalg::Scale` symbol and no scalar-value constant-folding.

Transitive L0 evidence (inherited from the firm L1 leaf; not re-localized — this edge is
identity-in-form, so L0 evidence is transitive through L1):

- `palace/linalg/vector.hpp:98-99` — `ComplexVector::operator*=(std::complex<double> s)`
  declaration (`// Scale all entries by s.`).
- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=` definition; lines
  207-211 the `si == 0.0` two-real-call promotion branch, lines 212-225 the general
  complex `forall_switch` kernel.
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template (the fused
  `nrm2 + scal` construct factoring as `scal(1/nrm2(x), x)`).

## Status

`firm` — identity-in-form L2>L1 floor edge between firm endpoints. The L2 LHS floor
([`scal`](../L2/scal.md)) is firm (cycle-041 D3, firm-on-positive-structure); the L1 RHS
leaf ([`scal`](../L1/scal.md)) is firm (cycle-004); the arity-1 fusion-selection row IS
`linear_combination.md` law 6 read at the singleton case. No arity dispatch, no
sub-selection, no fall-through, no pinned-summation-order residue (one term, one rounding
— value-exact AND bit-exact unconditionally). No speculative operator, no
negative-anchor reconstruction. This is the thinnest member of the L2>L1 lowering family
— the degenerate single-term shadow of the firm
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md),
factored out as the standalone leaf's own edge under the load-bearing fold-cohort
do-NOT-merge boundary.

A standing design fork (under batch-12 meta-phase adjudication) is whether the BLAS-1
leaf cohort should be realized as standalone same-named floors (the **(b)** realization
this theme is built on) or absorbed into the `linear_combination` fold (the **(a)
fold-only** reading). If the meta-phase adopts the fold-only reading, this theme would
re-anchor: the standalone `scal` L2>L1 edge would fold into
`linear-combination-fold-specialization`'s arity-1 row and this file would reduce to a
pointer. The theme is stated against the (b) realization, consistent with the firm L2
floor entry D3 lands this cycle.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter
  body).** Lifting the L1 leaf *up* to the L2 floor is the value-thread-isomorphic
  identity rotation: the L1 signature has no kernel fusion exposed, no destination buffer,
  no MPI collective — exactly the properties that make it L2-native by construction. No
  additional structure is required for the lift. This reverse-direction note lives here in
  working notes per the high→low layer-definition discipline; the formal chapter narrates
  only L2 → L1.

- **Leaf-vs-fold fork (batch-12 meta-phase adjudication).** See §Status; recorded as the
  cross-CYCLE OQ `scal-leaf-vs-linear-combination-fold-realization-fork`.
```

```new:book/src/L3-L2/scal-body-identity.md
# scal-body-identity

The L3>L2 lowering theme for the BLAS-1 leaf `scal`. The rewrite is **identity-in-form on
the body** with **no wrapper rotation** — `scal` is a leaf whole-tensor field operation,
not a step body, so the L3 whole-tensor form lowers into the L2 floor form by the identity
on the primitive itself. There is no `(op, K, s)`→`IterState` consolidation and no
outer-loop dissolution to perform (the two surface adjustments that the sibling
[`krylov-step-body-identity`](./krylov-step-body-identity.md) carries at its wrapper);
`scal` has no wrapper. The body IS the identity. This is the leaf-primitive analogue of
the `krylov-step` body-identity theme, and the thinnest member of the L3>L2 lowering
family.

## Slug

`scal-body-identity`

## Context

The `scal` lowering relationships span three adjacent layers, all identity-in-form
because `scal` is a BLAS-1 leaf with no iteration view and no kernel fusion:

- **L3 form** ([`L3/scal`](../L3/scal.md), firm cycle-011) — the whole-tensor field
  operation `scal :: Scalar -> Tensor[N] -> Tensor[N]`, the iteration-rotation rendering.
  Carries **no iteration view** (leaf primitive, not a step body) and **no sequential
  obstruction** (every element independent under the per-element multiply). The LHS of
  this theme.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/scal`](../L2/scal.md), firm cycle-041 D3) — the fusion-rotation floor
  leaf, the base scalar-vector-multiply primitive and the arity-1 member of the
  `linear_combination` fold. The RHS of this theme.
- **L2>L1 form** ([`L2-L1/scal-fold-specialization`](../L2-L1/scal-fold-specialization.md),
  firm cycle-041 D6) — the onward edge into the L1 leaf; also identity-in-form (the fold's
  arity-1 row).

This theme is the **leaf-primitive counterpart** of the firm
[`krylov-step-body-identity`](./krylov-step-body-identity.md) (cycle-007/009). The
`krylov-step` theme establishes the pattern "identity-in-form on the kernel **body**, with
surface adjustments at the **wrapper**"; its point-3 applicability condition names the
seven L1 primitives — including **`scal`** — as L3-native by signature shape: "each
operates on whole-tensor inputs with no element-loop exposed at L2. This is what makes the
L3>L2 rotation identity-in-form rather than requiring a decomposition step (each L1
primitive is *also* L3-native because its signature has no per-element loop visible)"
(`krylov-step-body-identity.md:97`). This theme is the standalone-leaf realization of that
classification for `scal`: the body is the identity, **and there is no wrapper at all** —
`scal` is not a step body, so the two wrapper adjustments the `krylov-step` theme carries
(the `(op, K, s)`→`IterState` consolidation and the outer-loop-to-driver-by-role
dissolution) have no analog here.

## L3 form (LHS)

The L3 whole-tensor form ([`L3/scal`](../L3/scal.md) §Signature):

    scal :: Scalar -> Tensor[N] -> Tensor[N]
    scal α x = α·x

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `α` a
scalar (`real` or `complex`, or `real` promoted against complex `x`); `x : Tensor[N]` a
single length axis, read-only at L3; result `Tensor[N]` of the same axis with
`result[i] = α · x[i]` for every `i ∈ [0, N)`. The operator carries **no iteration view**
(it is a leaf field operation, not a step body) and **no sequential obstruction** (every
element is independent of every other under the per-element multiply — embarrassingly
parallel, fully GPU-friendly). No L4 wrapper machinery applies (leaf primitives appear
inside L4 operator bodies as let-bindings, not as first-class L4 typed-wrapper anchors —
the cross-layer-cross-cutter "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1
cohort).

## L2 form (RHS)

The L2 floor form ([`L2/scal`](../L2/scal.md) §Signature):

    scal :: Scalar -> Tensor[N] -> Tensor[N]
    scal α x = α·x

The base scalar-vector-multiply leaf in the fusion-rotation vocabulary — **and** the
arity-1 member of the [`linear_combination`](../L2/linear_combination.md) fold
(`scal(α, x) = linear_combination [(α, x)]`, cited NOT merged). The signature is
**textually identical to the L3 form** modulo notation; the body is the same single
whole-tensor field operation. The nine algebraic laws hold unchanged across the edge
(L3 §Algebraic laws ≡ L2 §Algebraic laws — both inherit the L1 leaf's nine module-action
laws). The only fusion note the L2 floor carries is the degenerate arity-1 single-aligned
pass (the arity-1 case of the fold's fusion note); at L3 even that note is absent (L3
exposes no element loop at all).

## Rewrite shape

The rewrite is the **identity on the leaf primitive's body**, with **no wrapper
adjustment**:

    scal α x   (L3 whole-tensor field op)   ⇒   scal α x   (L2 floor leaf)

The body maps trivially — one binding, one primitive, same position, same dataflow:

| L3 form | L2 form | Mapping |
|---|---|---|
| `scal α x = α·x` (whole-tensor field operation; no iteration view) | `scal α x = α·x` (base scalar-vector-multiply floor leaf; arity-1 fold member) | Identity. Same signature, same single field operation. The only framing difference is documentary: L3 frames `scal` as a whole-tensor field operation in the iteration-rotation vocabulary; L2 frames the same operator as a base fusion-rotation primitive (and as the arity-1 fold member). No operational adjustment occurs. |

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two
surface adjustments at the wrapper around its kernel body: (1) the L3 `(op, K, s)`
positional tuple consolidates into the L2 unified `IterState` record (state-hiding), and
(2) the L3 tail-recursive outer loop `iterate_while_L3` collapses to the L2
outer-driver-by-role reference (abstraction-by-role). **Neither has an analog for `scal`**:
`scal` is a single leaf field operation, not a step body with an `(op, K, s)` carrier and
an outer loop. There is no `IterState` (no state record — `scal` is a pure positional
function), and there is no outer driver (no loop folds `scal` calls at the operator
itself; `scal` is *called by* step bodies like `krylov-step`'s `krylov_update`, but those
loops belong to the step body, not to `scal`). The mapping is total and bijective on a
single binding — the degenerate maximal case of the identity-in-form property.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `scal` endpoints)
when:

1. **`scal` is treated as a leaf primitive, not decomposed.** `scal` does not decompose
   into other L3 or L2 primitives — vector-scalar multiplication is a single field
   operation; its sub-operations (scalar multiply, per-element application) are below
   both layers' resolution. The `axpby-as-primitive` decision
   ([`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md))
   keeps the BLAS-1 leaves firm (fuse, don't decompose).

2. **The signature is whole-tensor at both layers** — `Scalar -> Tensor[N] -> Tensor[N]`
   with no per-element loop exposed at L2 and no iteration view at L3. This is exactly the
   `krylov-step-body-identity` point-3 condition specialized to the standalone `scal`
   leaf: `scal`'s signature has no per-element loop visible, so it is L3-native by
   construction and the rotation is identity-in-form rather than a decomposition.

3. **No iteration view, no sequential obstruction.** `scal` is element-local,
   reduction-free, rank-local; every element is independent. There is no outer loop, no
   carry trajectory, no recurrence — so there is nothing for the L3 iteration rotation to
   have rotated and nothing for the L3>L2 lowering to dissolve. The "step
   composition / outer-loop lift" non-law the L3 `scal` entry records (`L3/scal.md`
   §Algebraic laws) is structural inapplicability, not an obstruction.

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the leaf's signature shape `Scalar -> Tensor[N] -> Tensor[N]`
is whole-tensor by construction at both layers — no element loop is exposed at L2, no
iteration view at L3. The L3 vocabulary at this scope demands whole-tensor field
operations with no element loop exposed; `scal` satisfies this *at L2 already*, so the
rotation is the identity. This is a structural argument about the leaf's signature, and it
is the same structural argument the `krylov-step-body-identity` theme makes as its
secondary justification for each primitive in the kernel body (point-3 condition) — here
promoted to dominant because there is no kernel body wrapping the leaf, only the leaf
itself.

**Empirical-match (secondary)**: the cross-layer-cross-cutter identity-in-form audit
(`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`
§"(2) the BLAS-1 cohort") classified the `scal` L3↔L1 rotation as identity-in-form by
inspection of the firm L3>L2 and L4>L3 themes; the firm `krylov-step-body-identity` names
`scal` L3-native at line 97. This theme's L3>L2 edge is the standalone-leaf realization of
that audited classification, now that the L2 floor entry exists (cycle-041 D3) for the
rotation to target. The empirical evidence is observational about the firm artifact's
existing classification of `scal`; the structural signature argument is why it holds.

## Speculative L3 operators

**None.** This theme is the identity rotation between firm endpoints: the L3 LHS
([`L3/scal`](../L3/scal.md)) is firm (cycle-011), and the L2 RHS ([`L2/scal`](../L2/scal.md))
is firm (cycle-041 D3). No new L3 vocabulary is introduced. `scal` does not get its own L4
typed-wrapper anchor (leaf primitives appear inside L4 operator bodies as let-bindings —
the cross-layer-cross-cutter "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1
cohort), so there is no upstream L4>L3 theme for `scal` either; the L3 form is L3-native
by signature and this theme closes its downward edge to the L2 floor.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/scal.md` (cycle-011 firm) — the L3 whole-tensor form (LHS). Signature,
  semantics (element-local, reduction-free, rank-local, no iteration view, no sequential
  obstruction), nine algebraic laws, the leaf-not-step-body §"Iteration-rotation marker",
  two variant axes.
- `book/src/L2/scal.md` (cycle-041 D3 floor) — the L2 floor form (RHS). Identical
  signature and nine laws; the base scalar-vector-multiply leaf framing + the arity-1
  fold-membership identity.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (cycle-007/009 firm) — the mirror
  precedent classifying `scal` (among the seven L1 primitives) as L3-native by signature
  shape at its point-3 applicability condition. The structural justification this theme
  promotes to dominant.

Cross-layer audit (the empirical-match anchor):

- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`
  §"(2) the BLAS-1 cohort" — the HIGH CONFIDENCE classification of the `scal` rotation as
  identity-in-form, the dispatch rationale for the cycle-011 L3 `scal` backfill and (now)
  this L3>L2 edge.

Onward edges (cross-reference, not this theme's content):

- `book/src/L2-L1/scal-fold-specialization.md` (cycle-041 D6) — the onward L2>L1 edge into
  the L1 leaf; also identity-in-form (the fold's arity-1 row). Co-dispatched this cycle.
- `book/src/L1/scal.md` (cycle-004 firm) + `book/src/L1-L0/scal-mutation-rotation.md`
  (firm) — the L1 leaf and its in-place L0 mutation rotation, reached via the onward edge.

Transitive L0 evidence (inherited from the firm L1 leaf; not re-localized — identity-in-form
edge, L0 evidence transitive through L1):

- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=` definition (the complex
  `scal` overload; `si == 0.0` promotion branch at 207-211, general complex kernel at
  212-225).
- `palace/linalg/vector.hpp:98-99,262-270` — `operator*=` declaration + `linalg::Normalize`
  fused `nrm2 + scal` construct.

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS
([`L3/scal`](../L3/scal.md)) is firm (cycle-011); the L2 RHS ([`L2/scal`](../L2/scal.md))
is firm (cycle-041 D3). The body is the identity rotation on a single leaf field
operation; **there is no wrapper to rotate** (no `(op, K, s)`→`IterState` consolidation, no
outer-loop dissolution — `scal` is a leaf, not a step body). The structural justification
(whole-tensor signature, no element loop, no iteration view) is the
`krylov-step-body-identity` point-3 condition specialized to the standalone leaf and
promoted to dominant; the empirical-match anchor is the firm cross-layer audit + the
`krylov-step-body-identity:97` L3-native classification. No speculative operator, no
negative-anchor reconstruction, no sequential obstruction. The thinnest member of the
L3>L2 lowering family — the leaf-primitive counterpart of `krylov-step-body-identity`.

A standing design fork (under batch-12 meta-phase adjudication) is whether the BLAS-1
leaf cohort should be realized as standalone same-named floors (the **(b)** realization
this theme is built on) or absorbed into the `linear_combination` fold (the **(a)
fold-only** reading). If the meta-phase adopts the fold-only reading, the L2 RHS this
theme targets would become the fold's L2 form rather than a standalone `scal` floor, and
this theme would re-anchor accordingly. The theme is stated against the (b) realization,
consistent with the firm L2 floor entry D3 lands this cycle.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter
  body).** Lifting the L2 floor leaf *up* to the L3 whole-tensor form is the
  value-thread-isomorphic identity rotation: the L2 signature has no element loop exposed,
  which is exactly what makes it L3-native by construction. No additional structure is
  required for the lift. This reverse-direction note lives here in working notes per the
  high→low layer-definition discipline; the formal chapter narrates only L3 → L2.

- **Leaf-vs-fold fork (batch-12 meta-phase adjudication).** See §Status; recorded as the
  cross-CYCLE OQ `scal-leaf-vs-linear-combination-fold-realization-fork`.

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1
  identity (this theme's L3>L2 identity ∘ the L2>L1 `scal-fold-specialization` identity)
  is annotated in-line at the `scal` entries per the CLAUDE.md invariant "Identity
  rotations across non-adjacent layers are annotated in-line, not via a dedicated lowering
  directory" — no `book/src/L3-L1/` directory. This theme + the co-dispatched
  `scal-fold-specialization` compose to capture it.
```

**L2>L1 theme-list row** — insert the new `scal-fold-specialization` row **immediately
after** the `linear-combination-fold-specialization` anchor row (so the arity-1 leaf edge
sits beside its fold-parent). The anchor row below is unchanged.

```edit:book/src/L2-L1/index.md
| [linear-combination-fold-specialization](./linear-combination-fold-specialization.md) | `L2/linear_combination` (firm) | `L1/scal` + `axpy` + `axpby` + `axpbypcz` (firm) | firm *(algebraic; arity-dispatch fusion-selection + pinned summation order)* |
| [scal-fold-specialization](./scal-fold-specialization.md) | `L2/scal` (firm, cycle-041 D3) | `L1/scal` (firm leaf, cycle-004) | firm *(structural; identity-in-form floor edge — the degenerate arity-1 single-term shadow of `linear-combination-fold-specialization`; no arity dispatch, no pinned-summation-order residue (one term ⇒ one rounding, value+bit-exact); arity-1 fold member cited NOT merged)* |
```

**Insertion note for integrator (count-ownership):** this dispatch appends ONLY the
`scal-fold-specialization` theme-list row above. It does **NOT** touch the L2-L1/index
§"Vocabulary cohort" firm-list or §"Working Notes" cohort-growth log (the consolidated
tallies) — **D7 owns the L2-L1/index tallies this cycle**.

```edit:book/src/L3-L2/index.md
| [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) | L3 [`ksp_solve`](../L3/ksp_solve.md) §Signature — the value-threaded outer-driver fold `(op, K_0, s_0) -> (s_final, result)` rendered as an **explicit `iterate_while_L3` tail recursion** over [`krylov-step`](../L3/krylov-step.md), carrying the first-class **outer-loop `sequential-obstruction`**. | L2 [`ksp_solve`](../L2/ksp_solve.md) §Signature — the **outer-driver-by-role** composition `(K, b) -> SolveResult` with body = `iterate_while (krylov-step op) s_init predicate` (iteration view erased; obstruction shadows to the §"Algebraic laws" non-mergeability / no-fold-lift non-laws). | `structural` (the iteration-view erasure + obstruction-to-non-law shadow is a layer-surface-shape fact) + secondary `reduction-chain` (the `iterate_while_L3` → `iterate_while`-by-role consolidation re-folds the strawman §3.7 reduction sequence) | `firm` (cycle-021 wave-2 abstractor; the **substantive / non-identity** driver complement of the kernel-body identity theme — `kernel-identity + driver-non-identity = the full per-solver L3>L2 story`) |
| [`scal-body-identity`](./scal-body-identity.md) | L3 [`scal`](../L3/scal.md) §Signature — the whole-tensor field operation `scal :: Scalar -> Tensor[N] -> Tensor[N]`; leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`scal`](../L2/scal.md) §Signature — the base scalar-vector-multiply floor leaf (arity-1 member of `linear_combination`, cited NOT merged); identical signature. | `structural` (whole-tensor signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 condition specialized to the standalone leaf) + secondary `empirical-match` (firm cross-layer identity-in-form audit + `krylov-step-body-identity:97` L3-native classification) | `firm` (cycle-041 D6 abstractor; identity-in-form on the body, **no wrapper to rotate** — the leaf-primitive counterpart of `krylov-step-body-identity`) |
```

**Insertion note for integrator (count-ownership):** insert the `scal-body-identity` row
**immediately after** the `ksp-solve-outer-driver` anchor row (unchanged above). This
dispatch appends ONLY that one theme-list row — it does **NOT** touch any consolidated
L3-L2/index tally (none currently exists in that index; if D7 adds one, the count is D7's).

```edit:book/src/SUMMARY.md
- [linear-combination-fold-specialization](./L2-L1/linear-combination-fold-specialization.md)
- [scal-fold-specialization](./L2-L1/scal-fold-specialization.md)
```

```edit:book/src/SUMMARY.md
- [ksp-solve-outer-driver](./L3-L2/ksp-solve-outer-driver.md)
- [scal-body-identity](./L3-L2/scal-body-identity.md)
```

## Speculative operators proposed

**None** — both themes are identity-in-form lowering edges between firm vocabulary on
both sides. No rough-in operators are introduced.

- `scal-fold-specialization` (L2>L1): L2 LHS [`scal`](../L2/scal.md) firm (cycle-041 D3);
  L1 RHS [`scal`](../L1/scal.md) firm (cycle-004). Fold-parent
  [`linear_combination`](../L2/linear_combination.md) firm (cycle-018), cited NOT merged.
- `scal-body-identity` (L3>L2): L3 LHS [`scal`](../L3/scal.md) firm (cycle-011); L2 RHS
  [`scal`](../L2/scal.md) firm (cycle-041 D3). No L4 anchor (leaf primitive, CONFIRMED-NOT-NEEDED).

## Supporting evidence

**Firm artifact entries (read this invocation):**

- `reports/2026-06-01T051607Z-cycle-041-harvester-L2-scal/CYCLE.md` (wave-1 D3) — the
  source-of-truth L2 `scal` floor body (`book/src/L2/scal.md`, lands at integration
  alongside these themes). Both themes target / source this floor entry.
- `book/src/L1/scal.md` (cycle-004 firm) — the L1 leaf; nine algebraic laws, two variant
  axes, the one-to-one L0 `operator*=` symbol shape.
- `book/src/L3/scal.md` (cycle-011 firm) — the L3 whole-tensor form; leaf-not-step-body
  §"Iteration-rotation marker", no sequential obstruction.
- `book/src/L1-L0/scal-mutation-rotation.md` (firm) — the onward L1>L0 mutation rotation
  (real Sub-pattern A / complex Sub-pattern B).
- `book/src/L3-L2/krylov-step-body-identity.md:97` — the mirror precedent; classifies
  `scal` L3-native by signature shape at its point-3 condition.
- `book/src/L2-L1/linear-combination-fold-specialization.md` (cycle-018/019 firm) — the
  fold-parent's specialization theme; `scal-fold-specialization` is its degenerate
  arity-1 single-term shadow.
- `book/src/L2/linear_combination.md:68` — `scal(α, x) = linear_combination [(α, x)]`
  (the arity-1 fold-membership identity; cited NOT merged).
- `book/src/L2/index.md` §"Fold-cohort boundary" — the load-bearing do-NOT-merge note.
- `book/src/L2-L1/index.md` + `book/src/L3-L2/index.md` — sibling slug + theme-list
  conventions (`-fold-specialization`, `-body-identity`).

**L0 anchors — self-verified 2026-06-01 (citecheck `--anchor`, on-disk source of truth):**

- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=` definition.
  `citecheck --anchor 'operator*='` → `[ok]` (anchor at :203 within range).
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template.
  `citecheck --anchor 'Normalize'` → `[ok]` (anchor at :262,:264 within range).
- `palace/linalg/vector.hpp:98-99` — `operator*=` declaration (inherited from firm L1).

All L0 citations are **transitive through the firm L1 leaf** (both themes are
identity-in-form; no new L0 localization was required). The themes' primary evidence is
the firm L1/L2/L3 artifact entries + the firm fold-parent + the firm `krylov-step`
mirror; the L0 anchors are inherited and re-verified for pinpoint hygiene.

## Open questions / caveats

- **Leaf-vs-fold fork (batch-12 meta-phase adjudication) — surfaced per dispatch
  directive.** Both themes are built on the **(b) same-named-floor realization** (D3's):
  `scal` exists as its own standalone L2 floor entry, cited as the arity-1 member of
  `linear_combination` but NOT merged (fold-cohort boundary load-bearing). The standing
  fork is whether the BLAS-1 leaf cohort should instead be the **(a) fold-only** reading
  (the leaves absorbed into the variadic `linear_combination` fold, no standalone floor
  entries). **If the meta-phase adopts the fold-only reading**, both themes re-anchor:
  (i) `scal-fold-specialization`'s L2 LHS would no longer be a standalone `scal` floor —
  the edge would fold into `linear-combination-fold-specialization`'s arity-1 row and this
  file would reduce to a pointer; (ii) `scal-body-identity`'s L2 RHS would become the
  fold's L2 form rather than a standalone `scal` floor. Recorded as cross-CYCLE OQ
  `scal-leaf-vs-linear-combination-fold-realization-fork` (status: open; trigger:
  batch-12 meta-phase fork verdict). Both themes are consistent with the firm L2 floor
  entry D3 lands this cycle; the re-anchoring is conditional on a meta-phase decision that
  has not yet been made.

- **L0 evidence is transitive, not re-localized.** Both themes are identity-in-form, so
  the L0 evidence chain lives in the firm L1 leaf + the firm L1>L0 mutation rotation; I
  cited the canonical anchors (`vector.cpp:203-227`, `vector.hpp:98-99,262-270`) for
  pinpoint hygiene and self-verified them via citecheck, but did not re-derive the L0
  surface (it is small, fully present, positively cited in the firm L1 entry).

- **Non-adjacent L3>L1 identity stays in-line.** The transitive L3>L1 `scal` identity
  (the `scal-body-identity` L3>L2 identity ∘ the `scal-fold-specialization` L2>L1
  identity) is captured by these two adjacent themes composing; per the CLAUDE.md
  invariant "Identity rotations across non-adjacent layers are annotated in-line, not via
  a dedicated lowering directory" there is no `book/src/L3-L1/` directory and no
  standalone L3>L1 theme. Noted in `scal-body-identity` §Open questions.

- **`fold_parent` frontmatter field (inherited from D3).** The D3 L2 `scal` floor entry
  introduced a `fold_parent` frontmatter field; these themes reference the membership in
  prose (cited NOT merged) and do not depend on the frontmatter convention. If the
  layer-intro-author / meta-phase drops the field, neither theme is affected.

## Count-ownership note (mandatory, per dispatch)

This dispatch appends **only**: (1) `book/src/L2-L1/scal-fold-specialization.md`, (2)
`book/src/L3-L2/scal-body-identity.md`, (3) one L2-L1/index theme-list row (after the
`linear-combination-fold-specialization` anchor), (4) one L3-L2/index theme-list row
(after the `ksp-solve-outer-driver` anchor), (5) two SUMMARY registrations. It does
**NOT** touch any consolidated theme-count tally — the L2-L1/index §"Vocabulary cohort"
firm-list, the §"Working Notes" cohort-growth log, or any D7-owned running total.
**D7 owns the tallies this cycle** (count-ownership partition). Deferred.

# scal-leaf-identity

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

`scal-leaf-identity`

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

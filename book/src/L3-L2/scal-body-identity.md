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
- **L2>L1 form** ([`L2-L1/scal-leaf-identity`](../L2-L1/scal-leaf-identity.md),
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

- `book/src/L2-L1/scal-leaf-identity.md` (cycle-041 D6) — the onward L2>L1 edge into
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
  identity (this theme's L3>L2 identity ∘ the L2>L1 `scal-leaf-identity` identity)
  is annotated in-line at the `scal` entries per the CLAUDE.md invariant "Identity
  rotations across non-adjacent layers are annotated in-line, not via a dedicated lowering
  directory" — no `book/src/L3-L1/` directory. This theme + the co-dispatched
  `scal-leaf-identity` compose to capture it.

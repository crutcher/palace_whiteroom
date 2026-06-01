# axpy-body-identity

The L3>L2 lowering theme for the BLAS-1 leaf `axpy`. The rewrite is **identity-in-form on the body**
with **no wrapper rotation** — `axpy` is a leaf whole-tensor field operation, not a step body, so the
L3 whole-tensor form `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` lowers into the L2 floor
form by the identity on the primitive itself. There is no `(op, K, s)`→`IterState` consolidation and
no outer-loop dissolution to perform (the two surface adjustments that the sibling
[`krylov-step-body-identity`](./krylov-step-body-identity.md) carries at its wrapper); `axpy` has no
wrapper. The body IS the identity. `axpy` is one of the seven BLAS-1 primitives that are **L3-native
by signature shape** (no per-element loop visible at either layer; `krylov-step-body-identity.md:97`),
so the iteration rotation is already complete at the signature level and the L3>L2 body edge is the
identity. This is the arity-2-fold-member analogue of [`scal-body-identity`](./scal-body-identity.md)
(the arity-1 member), and the leaf-primitive counterpart of `krylov-step-body-identity` (which is
identity-in-form on a multi-primitive kernel body, with wrapper adjustments).

## Slug

`axpy-body-identity`

## Context

The `axpy` lowering relationships span three adjacent layers, all identity-in-form because `axpy` is a
BLAS-1 leaf with no iteration view and no leaf-unique kernel fusion:

- **L3 form** ([`L3/axpy`](../L3/axpy.md), firm cycle-011) — the whole-tensor field operation `axpy ::
  Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]`, the iteration-rotation rendering consumed inside the
  `krylov-step` body's iterate-stratum update. Carries **no iteration view** (leaf primitive, not a
  step body) and **no sequential obstruction** (every element independent under the fused per-element
  `α·x[i] + y[i]`). The LHS of this theme.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/axpy`](../L2/axpy.md), firm cycle-043 wave-1 D3) — the fusion-rotation floor leaf,
  the base scalar-vector fused-update primitive and the arity-2 member of the `linear_combination`
  fold (second coeff fixed to 1, cited NOT merged). The RHS of this theme.
- **L2>L1 form** ([`L2-L1/axpy-leaf-identity`](../L2-L1/axpy-leaf-identity.md), firm cycle-043 D6) —
  the onward edge into the L1 leaf; also identity-in-form (the arity-2 shadow of the fold's
  fusion-selection, with all fusion deferred to the fold-parent). Co-authored this cycle.

This theme is the **leaf-primitive counterpart** of the firm
[`krylov-step-body-identity`](./krylov-step-body-identity.md) (cycle-007/009). The `krylov-step` theme
establishes the pattern "identity-in-form on the kernel **body**, with surface adjustments at the
**wrapper**"; its point-3 applicability condition names the seven L1 primitives — including **`axpy`**
— as L3-native by signature shape: "each operates on whole-tensor inputs with no element-loop exposed
at L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition
step (each L1 primitive is *also* L3-native because its signature has no per-element loop visible)"
(`krylov-step-body-identity.md:97`). This theme is the standalone-leaf realization of that
classification for `axpy`: the body is the identity, **and there is no wrapper at all** — `axpy` is
not a step body, so the two wrapper adjustments the `krylov-step` theme carries (the
`(op, K, s)`→`IterState` consolidation and the outer-loop-to-driver-by-role dissolution) have no
analog here.

`axpy` differs from the arity-1 sibling [`scal-body-identity`](./scal-body-identity.md) only in arity:
`axpy` is the arity-2-coeff-1 fold member (one scaled term `α·x` plus one unit-coeff term `y`), `scal`
the arity-1 member (one scaled term). Both are identity-in-form on the body with no wrapper; the
arity-2-vs-arity-1 difference is entirely the fold-parent's content, not this edge's.

## L3 form (LHS)

The L3 whole-tensor form ([`L3/axpy`](../L3/axpy.md) §Signature, firm cycle-011):

    axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]
    axpy α x y = α·x + y

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `α` a scalar
(`real` or `complex`, or `real` promoted against complex `x, y`); `x, y : Tensor[N]` a single shared
length axis, read-only at L3; result `Tensor[N]` of the same axis with `result[i] = α·x[i] + y[i]` for
every `i ∈ [0, N)`. The operator carries **no iteration view** (it is a leaf field operation, not a
step body) and **no sequential obstruction** (every element is independent of every other under the
fused per-element scaled add — embarrassingly parallel, fully GPU-friendly). No L4 wrapper machinery
applies (leaf primitives appear inside L4 operator bodies as let-bindings — e.g. inside
`krylov-step`'s `krylov_update` — not as first-class L4 typed-wrapper anchors; the
cross-layer-cross-cutter "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 cohort).

## L2 form (RHS)

The L2 floor form ([`L2/axpy`](../L2/axpy.md) §Signature, firm cycle-043 wave-1 D3):

    axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]
    axpy α x y = α·x + y

The base scalar-vector fused-update leaf in the fusion-rotation vocabulary — **and** the arity-2
member of the [`linear_combination`](../L2/linear_combination.md) fold (`axpy(α,x,y) =
linear_combination [(α,x),(1,y)]`, second coeff fixed to 1, cited NOT merged). The signature is
**textually identical to the L3 form** modulo notation; the body is the same single whole-tensor fused
field operation. The six algebraic laws hold unchanged across the edge (L3 §Algebraic laws ≡ L2
§Algebraic laws — both inherit the L1 leaf's six affine-vector-update laws). The only fusion note the
L2 floor carries is the arity-2 single-aligned pass (the arity-2 case of the fold's fusion note,
deferred to the fold-parent); at L3 even that note is absent (L3 exposes no element loop at all).

## The rewrite (L3 → L2)

The rewrite is the **identity on the leaf primitive's body**, with **no wrapper adjustment**:

    axpy α x y   (L3 whole-tensor field op)   ⇒   axpy α x y   (L2 floor leaf)

The body maps trivially — one binding, one primitive, same position, same dataflow:

    | L3 form                                  | L2 form                                  | Mapping |
    |------------------------------------------|------------------------------------------|---------|
    | `axpy α x y = α·x + y` (whole-tensor field op; no iteration view) | `axpy α x y = α·x + y` (base scalar-vector fused-update floor leaf; arity-2 fold member) | Identity. Same signature, same single fused field operation. The only framing difference is documentary: L3 frames `axpy` as a whole-tensor field operation in the iteration-rotation vocabulary; L2 frames the same operator as a base fusion-rotation primitive (and the arity-2 fold member). No operational adjustment occurs. |
    | second coeff fixed to 1 (`y` unscaled)   | second coeff fixed to 1 (`y` unscaled)   | Identity. The fixed-1 `y`-coefficient is preserved across the edge. |
    | algebraic laws 1–6                       | algebraic laws 1–6                       | Identity. Inherited unchanged across the chain (affine-vector-update facts + the IEEE summation non-law). |
    | no sequential obstruction                | no sequential obstruction                | Identity. The fused add lifts as a whole-tensor op at both layers; every element independent. |

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two surface
adjustments at the wrapper around its kernel body: (1) the L3 `(op, K, s)` positional tuple
consolidates into the L2 unified `IterState` record (state-hiding), and (2) the L3 tail-recursive
outer loop `iterate_while_L3` collapses to the L2 outer-driver-by-role reference (abstraction-by-role).
**Neither has an analog for `axpy`**: `axpy` is a single leaf field operation, not a step body with an
`(op, K, s)` carrier and an outer loop. There is no `IterState` (no state record — `axpy` is a pure
positional function), and there is no outer driver (no loop folds `axpy` calls at the operator itself;
`axpy` is *called by* step bodies like `krylov-step`'s `krylov_update`, but those loops belong to the
step body, not to `axpy`). The mapping is total and bijective on a single binding — the degenerate
maximal case of the identity-in-form property.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `axpy` endpoints) when:

1. **`axpy` is L3-native by signature shape.** Its signature `Scalar -> Tensor[N] -> Tensor[N] ->
   Tensor[N]` exposes no per-element loop at L2 or L3; the fused scaled add over `N` is a single
   semantic step at both layers. This is the load-bearing condition (per
   `krylov-step-body-identity.md:97`, which names `axpy` among the seven L3-native primitives).
   Satisfied by construction: `axpy` is a leaf field operation.

2. **`axpy` is treated as a leaf primitive, not decomposed.** `axpy` does not decompose into other L3
   or L2 primitives (it is NOT `scal` + tensor-add — it is the *fused* primitive, kept whole per the
   `axpby-as-primitive` fuse-don't-decompose decision
   ([`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md))).
   The de-fused two-pass form is the fold's seed-and-accumulate realization, recorded as the
   fold-parent's fusion note, not as an L3 or L2 decomposition.

3. **The L2 form is the same-named floor leaf** (`book/src/L2/axpy.md`), value-thread-isomorphic to
   the L3 leaf. The leaf-vs-fold fork (`dot-l2-leaf-floor-vs-fold-only-design`) is **resolved keep-(b)**
   (batch-12 meta-phase, per the c042 cross-cutter audit) — the L3 leaf lowers to an adjacent
   same-named L2 floor. Under the superseded (a) fold-only reading, the L3 leaf's adjacent L2 parent
   would be the fold-parent `linear_combination` and this theme's RHS would re-anchor; this condition
   records the resolved design presupposition explicitly.

4. **No iteration view, no sequential obstruction.** `axpy` is element-local, reduction-free,
   rank-local; every element is independent. There is no outer loop, no carry trajectory, no
   recurrence — so there is nothing for the L3 iteration rotation to have rotated and nothing for the
   L3>L2 lowering to dissolve.

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the leaf's signature shape `Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]`
is whole-tensor by construction at both layers — no element loop is exposed at L2, no iteration view at
L3. The L3 vocabulary at this scope demands whole-tensor field operations with no element loop exposed;
`axpy` satisfies this *at L2 already*, so the rotation is the identity. This is a structural argument
about the leaf's signature, and it is the same structural argument the `krylov-step-body-identity`
theme makes as its secondary justification for each primitive in the kernel body (point-3 condition) —
here promoted to dominant because there is no kernel body wrapping the leaf, only the leaf itself.

**Empirical-match (secondary)**: the L3 leaf-floor and the L2 floor leaf were authored independently
(L3 cycle-011, L2 cycle-043 wave-1 D3) as value-thread-isomorphic to the same firm L1 leaf, and they
agree on every law, every variant axis, and every signature row by independent transcription. The
cross-layer-cross-cutter identity-in-form audit
(`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"(2) the
BLAS-1 cohort") classified the `axpy` L3↔L1 rotation as identity-in-form; the firm
`krylov-step-body-identity` names `axpy` L3-native at line 97. This theme's L3>L2 edge is the
standalone-leaf realization of that audited classification, now that the L2 floor entry exists
(cycle-043 D3) for the rotation to target.

## Speculative L2 operators

**None.** Both endpoints are existing vocabulary: the L3 LHS is the firm `axpy` leaf (firm cycle-011),
the L2 RHS is the `axpy` floor leaf (firming cycle-043 wave-1 D3). This theme is the identity edge
between existing chapters; it proposes no new operators. `axpy` does not get its own L4 typed-wrapper
anchor (leaf primitives appear inside L4 operator bodies as let-bindings — the
cross-layer-cross-cutter "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 cohort), so there
is no upstream L4>L3 theme for `axpy` either; the L3 form is L3-native by signature and this theme
closes its downward edge to the L2 floor.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/axpy.md` (cycle-011 firm) — the L3 whole-tensor form (LHS). Signature (`:30-32`),
  semantics (element-local, reduction-free, rank-local, no iteration view, no sequential obstruction;
  §"Iteration-rotation marker" `:62-64`), six algebraic laws (`:70-75`), two non-laws + the IEEE
  summation non-law (`:79-81`), two variant axes (`:101-104`). The §"Lowers to" (`:112-116`) currently
  records identity-in-form to L1 via the non-adjacent convention ("no L2 intermediate because the
  BLAS-1 primitives are L1 leaves not L2 compositions"); this theme supplies the now-present adjacent
  L3>L2 edge (downstream-consistency touch on the L3 entry flagged in §Open-questions of the authoring
  report).
- `book/src/L2/axpy.md` (firming cycle-043 wave-1 D3) — the L2 floor leaf (RHS). Identical signature
  and six laws; the base scalar-vector fused-update leaf framing + the arity-2 fold-membership identity
  (second coeff fixed to 1). (Lands at this cycle's integration alongside this theme.)
- `book/src/L3-L2/krylov-step-body-identity.md:97` (cycle-007/009 firm) — §"Applicability conditions"
  point 3: the load-bearing statement that the seven BLAS-1 primitives (including `axpy`) are L3-native
  by signature shape (no per-element loop visible), which is the structural justification for this
  identity edge. **Self-verified (anchor `L3-native` @97).**
- `book/src/L3-L2/scal-body-identity.md` (cycle-041 D6 firm; the arity-1 sibling precedent) — the
  exact template structure this theme mirrors (leaf-not-step-body framing, no-wrapper-to-rotate, the
  §"Rewrite shape" mapping table), adapted arity-1 → arity-2.

Cross-layer audit (the empirical-match anchor):

- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"(2) the
  BLAS-1 cohort" — the HIGH CONFIDENCE classification of the `axpy` rotation as identity-in-form, the
  dispatch rationale for the cycle-011 L3 `axpy` backfill and (now) this L3>L2 edge.

Onward edges (cross-reference, not this theme's content):

- `book/src/L2-L1/axpy-leaf-identity.md` (cycle-043 D6) — the onward L2>L1 edge into the L1 leaf; also
  identity-in-form (the arity-2 shadow of the fold's fusion-selection, all fusion deferred to the
  fold-parent). Co-dispatched this cycle.
- `book/src/L1/axpy.md` (cycle-002 firm) + `book/src/L1-L0/axpby-mutation-rotation.md` (firm,
  sub-pattern A β=1) — the L1 leaf and its in-place L0 mutation rotation, reached via the onward edge.

Transitive L0 evidence (inherited from the firm L1 leaf; not re-localized — identity-in-form edge, L0
evidence transitive through L1; self-verified via `tools/citecheck/citecheck.py --anchor` this
invocation; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:702-712` — free function `AXPY(double, Vector, Vector)` with the `α == 1.0`
  fast-path at `:704`. **Self-verified (anchor `AXPY` @702; `1.0` @704).**
- `palace/linalg/vector.cpp:276-311` — `ComplexVector::AXPY` definition and the element-wise
  `forall_switch` kernels. **Self-verified (anchor `AXPY` @276-281).**
- `palace/linalg/vector.hpp:115-118,305-307` — `ComplexVector::AXPY` member decl + the free-function
  template `AXPY` decl. **Self-verified (anchor `AXPY` @116-118, @307).**

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS ([`L3/axpy`](../L3/axpy.md)) is
firm (cycle-011); the L2 RHS ([`L2/axpy`](../L2/axpy.md)) is firm-this-cycle (wave-1 D3). The body is
the identity rotation on a single leaf field operation; **there is no wrapper to rotate** (no
`(op, K, s)`→`IterState` consolidation, no outer-loop dissolution — `axpy` is a leaf, not a step body).
The structural justification (whole-tensor signature, no element loop, no iteration view) is the
`krylov-step-body-identity` point-3 condition specialized to the standalone leaf and promoted to
dominant; the empirical-match anchor is the firm cross-layer audit + the
`krylov-step-body-identity:97` L3-native classification. No speculative operator, no negative-anchor
reconstruction, no sequential obstruction. The arity-2-fold-member counterpart of the arity-1
[`scal-body-identity`](./scal-body-identity.md); the thinnest tier of the L3>L2 lowering family
alongside it.

> **Slug convention note.** This theme uses the RATIFIED `-body-identity` slug (batch-12 meta-phase),
> matching `dot-body-identity` / `scal-body-identity` and the cycle-042 standalone-floor cohort.

> **Design-presupposition note (not a status reduction).** This theme presupposes the **(b)
> same-named L2 leaf-floor** RHS (Applicability condition 3). The leaf-vs-fold fork
> (`dot-l2-leaf-floor-vs-fold-only-design`) is **resolved keep-(b)** (batch-12 meta-phase, per the
> c042 cross-cutter audit). Under the superseded (a) fold-only reading, the L2 RHS would re-point from
> the same-named `axpy` leaf to the fold-parent `linear_combination`, weakening the "identity" claim
> (a same-named leaf → a differently-named fold-parent is a weaker identity). The theme is
> self-coherent under the resolved (b) reading it is built on.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L2 floor leaf *up* to the L3 whole-tensor form is the value-thread-isomorphic identity
  rotation: the L2 signature has no element loop exposed, which is exactly what makes it L3-native by
  construction. No additional structure is required for the lift. This reverse-direction note lives
  here in working notes per the high→low layer-definition discipline; the formal chapter narrates only
  L3 → L2.

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (this
  theme's L3>L2 identity ∘ the L2>L1 `axpy-leaf-identity` identity) is annotated in-line at the `axpy`
  entries per the CLAUDE.md invariant "Identity rotations across non-adjacent layers are annotated
  in-line, not via a dedicated lowering directory" — no `book/src/L3-L1/` directory. This theme + the
  co-dispatched `axpy-leaf-identity` compose to capture it.

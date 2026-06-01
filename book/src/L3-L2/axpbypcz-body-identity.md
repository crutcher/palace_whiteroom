# axpbypcz-body-identity

The L3>L2 lowering theme for the fused arity-3 BLAS-1-extended leaf `axpbypcz`. The rewrite is
**identity-in-form on the body** with **no wrapper rotation** — `axpbypcz` is a leaf whole-tensor
field operation, not a step body, so the L3 whole-tensor form lowers into the L2 floor form by the
identity on the primitive itself. There is no `(op, K, s)`→`IterState` consolidation and no
outer-loop dissolution to perform (the two surface adjustments that the sibling
[`krylov-step-body-identity`](./krylov-step-body-identity.md) carries at its wrapper); `axpbypcz`
has no wrapper. The body IS the identity. This is the leaf-primitive analogue of the `krylov-step`
body-identity theme and the arity-3 fold-member sibling of [`scal-body-identity`](./scal-body-identity.md)
(the arity-1 member of the same `linear_combination` fold).

## Slug

`axpbypcz-body-identity`

## Context

The `axpbypcz` lowering relationships span three adjacent layers, all identity-in-form because
`axpbypcz` is a fused BLAS-1-extended leaf with no iteration view and a single fused field
operation:

- **L3 form** ([`L3/axpbypcz`](../L3/axpbypcz.md), firm cycle-011) — the whole-tensor field
  operation `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] ->
  Tensor[N]`, the iteration-rotation rendering. Carries **no iteration view** (leaf primitive, not
  a step body) and **no sequential obstruction** (every element independent under the per-element
  fused combination). The LHS of this theme.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/axpbypcz`](../L2/axpbypcz.md), firming cycle-043 wave-1 D5) — the
  fusion-rotation floor leaf, the base fused three-term linear-combination primitive and the
  arity-3 member of the [`linear_combination`](../L2/linear_combination.md) fold. The RHS of this
  theme.
- **L2>L1 form** ([`L2-L1/axpbypcz-leaf-identity`](../L2-L1/axpbypcz-leaf-identity.md), this cycle
  D8) — the onward edge into the L1 leaf; also identity-in-form (all fusion deferred to the fold's
  arity-3 row).

This theme is the **leaf-primitive counterpart** of the firm
[`krylov-step-body-identity`](./krylov-step-body-identity.md) (cycle-007/009), and the direct
arity-3 sibling of [`scal-body-identity`](./scal-body-identity.md) (the arity-1 fold member,
cycle-041 D6). The `krylov-step` theme establishes the pattern "identity-in-form on the kernel
**body**, with surface adjustments at the **wrapper**"; its point-3 applicability condition names
the seven L1 primitives — including **`axpbypcz`** — as L3-native by signature shape: "each operates
on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2 rotation
identity-in-form rather than requiring a decomposition step (each L1 primitive is *also* L3-native
because its signature has no per-element loop visible)" (`krylov-step-body-identity.md:97`). This
theme is the standalone-leaf realization of that classification for `axpbypcz`: the body is the
identity, **and there is no wrapper at all** — `axpbypcz` is not a step body, so the two wrapper
adjustments the `krylov-step` theme carries (the `(op, K, s)`→`IterState` consolidation and the
outer-loop-to-driver-by-role dissolution) have no analog here.

## L3 form (LHS)

The L3 whole-tensor form ([`L3/axpbypcz`](../L3/axpbypcz.md) §Signature):

    axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpbypcz α x β y γ z = α·x + β·y + γ·z

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `α, β, γ`
scalars (`real` or `complex`, or `real` promoted against complex tensors); `x, y, z : Tensor[N]`
sharing one length axis, read-only at L3 (`z` is the *prior* value when used as a fused update);
result `Tensor[N]` of the same axis with `result[i] = α·x[i] + β·y[i] + γ·z[i]` for every
`i ∈ [0, N)`. The operator carries **no iteration view** (it is a leaf field operation, not a step
body) and **no sequential obstruction** (every element is independent of every other under the
per-element fused combination — embarrassingly parallel, fully GPU-friendly). No L4 wrapper
machinery applies (the L4 candidate for `axpbypcz` is CONFIRMED-NOT-NEEDED per the cycle-010 cohort
audit — leaf primitives appear inside L4 operator bodies as let-bindings, e.g. inside
`krylov-step`'s three-vector slice update, not as first-class L4 typed-wrapper anchors).

## L2 form (RHS)

The L2 floor form ([`L2/axpbypcz`](../L2/axpbypcz.md) §Signature):

    axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpbypcz α x β y γ z = α·x + β·y + γ·z

The base fused three-term linear-combination leaf in the fusion-rotation vocabulary — **and** the
arity-3 member of the [`linear_combination`](../L2/linear_combination.md) fold
(`axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]`, cited NOT merged). The
signature is **textually identical to the L3 form** modulo notation; the body is the same single
fused whole-tensor field operation. The twelve algebraic laws + four non-laws hold unchanged across
the edge (L3 §Algebraic laws ≡ L2 §Algebraic laws — both inherit the L1 leaf's twelve laws and four
non-laws). The only fusion note the L2 floor carries is the arity-3 single-aligned `add(α,x,β,y,z)`
pass / `γ==0` arity-collapse (the arity-3 case of the fold's fusion note); at L3 even that note is
absent (L3 exposes no element loop at all). The output-aliasing in-place/out-of-place variant is the
fold's axis, not the leaf's; this floor is uniformly pure.

## Rewrite shape

The rewrite is the **identity on the leaf primitive's body**, with **no wrapper adjustment**:

    axpbypcz α x β y γ z   (L3 whole-tensor field op)   ⇒   axpbypcz α x β y γ z   (L2 floor leaf)

The body maps trivially — one binding, one primitive, same position, same dataflow:

| L3 form | L2 form | Mapping |
|---|---|---|
| `axpbypcz α x β y γ z = α·x + β·y + γ·z` (whole-tensor field operation; no iteration view) | `axpbypcz α x β y γ z = α·x + β·y + γ·z` (base fused three-term floor leaf; arity-3 fold member) | Identity. Same six-arg signature, same single fused field operation. The only framing difference is documentary: L3 frames `axpbypcz` as a whole-tensor field operation in the iteration-rotation vocabulary; L2 frames the same operator as a base fusion-rotation primitive (and as the arity-3 fold member). No operational adjustment occurs. |

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two surface
adjustments at the wrapper around its kernel body: (1) the L3 `(op, K, s)` positional tuple
consolidates into the L2 unified `IterState` record (state-hiding), and (2) the L3 tail-recursive
outer loop `iterate_while_L3` collapses to the L2 outer-driver-by-role reference
(abstraction-by-role). **Neither has an analog for `axpbypcz`**: `axpbypcz` is a single fused leaf
field operation, not a step body with an `(op, K, s)` carrier and an outer loop. There is no
`IterState` (no state record — `axpbypcz` is a pure positional function), and there is no outer
driver (no loop folds `axpbypcz` calls at the operator itself; `axpbypcz` is *called by* step
bodies like `krylov-step`'s `krylov_update` three-vector slice patterns — Chebyshev, BiCGStab — but
those loops belong to the step body, not to `axpbypcz`). The mapping is total and bijective on a
single binding — the degenerate maximal case of the identity-in-form property.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `axpbypcz` endpoints) when:

1. **`axpbypcz` is treated as a leaf primitive, not decomposed.** `axpbypcz` does not decompose into
   other L3 or L2 primitives — the fused three-term linear combination is a single field operation;
   its sub-operations (three scalar multiplies, two element-wise additions) are below both layers'
   resolution. The `axpby-as-primitive` decision
   ([`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md))
   keeps the BLAS-1 leaves firm (fuse, don't decompose; the decision record explicitly invites the
   `axpbypcz` harvester to mirror the fused-primitive choice). Decomposing it into chained `axpby`
   calls is precisely the choice the decision declines.

2. **The signature is whole-tensor at both layers** —
   `Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` with no
   per-element loop exposed at L2 and no iteration view at L3. This is exactly the
   `krylov-step-body-identity` point-3 condition specialized to the standalone `axpbypcz` leaf:
   `axpbypcz`'s signature has no per-element loop visible (it is named at line 97 among the seven
   L3-native primitives), so it is L3-native by construction and the rotation is identity-in-form
   rather than a decomposition.

3. **No iteration view, no sequential obstruction.** `axpbypcz` is element-local, reduction-free,
   rank-local; every element is independent. There is no outer loop, no carry trajectory, no
   recurrence — so there is nothing for the L3 iteration rotation to have rotated and nothing for the
   L3>L2 lowering to dissolve. The fused statement is preserved (the fusion has algebraic meaning),
   and the `γ==0` arity-collapse / single-aligned-pass fusion content is the fold-parent's concern at
   the L2>L1 edge, not an L3>L2 obstruction.

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the leaf's signature shape
`Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` is whole-tensor by
construction at both layers — no element loop is exposed at L2, no iteration view at L3. The L3
vocabulary at this scope demands whole-tensor field operations with no element loop exposed;
`axpbypcz` satisfies this *at L2 already*, so the rotation is the identity. This is a structural
argument about the leaf's signature, and it is the same structural argument the
`krylov-step-body-identity` theme makes as its secondary justification for each primitive in the
kernel body (point-3 condition, naming `axpbypcz` explicitly at line 97) — here promoted to dominant
because there is no kernel body wrapping the leaf, only the leaf itself.

**Empirical-match (secondary)**: the cross-layer-cross-cutter identity-in-form audit
(`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`
§"(2) the BLAS-1 cohort") classified the `axpbypcz` L3↔L1 rotation as identity-in-form by inspection
of the firm L3>L2 and L4>L3 themes; the firm `krylov-step-body-identity` names `axpbypcz` L3-native
at line 97. This theme's L3>L2 edge is the standalone-leaf realization of that audited
classification, now that the L2 floor entry exists (cycle-043 wave-1 D5) for the rotation to target.
The empirical evidence is observational about the firm artifact's existing classification of
`axpbypcz`; the structural signature argument is why it holds.

## Speculative L3 operators

**None.** This theme is the identity rotation between firm endpoints: the L3 LHS
([`L3/axpbypcz`](../L3/axpbypcz.md)) is firm (cycle-011), and the L2 RHS
([`L2/axpbypcz`](../L2/axpbypcz.md)) is firming (cycle-043 wave-1 D5). No new L3 vocabulary is
introduced. `axpbypcz` does not get its own L4 typed-wrapper anchor (leaf primitives appear inside
L4 operator bodies as let-bindings — the cycle-010 cohort audit "L4 candidate CONFIRMED-NOT-NEEDED"
verdict for the BLAS-1 cohort), so there is no upstream L4>L3 theme for `axpbypcz` either; the L3
form is L3-native by signature and this theme closes its downward edge to the L2 floor.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/axpbypcz.md` (cycle-011 firm) — the L3 whole-tensor form (LHS). Signature,
  semantics (element-local, reduction-free, rank-local, no iteration view, no sequential
  obstruction), twelve algebraic laws, four non-laws, the leaf-not-step-body §"Iteration-rotation
  marker", two variant axes.
- `book/src/L2/axpbypcz.md` (firming cycle-043 wave-1 D5 floor) — the L2 floor form (RHS). Identical
  signature and twelve laws; the base fused three-term linear-combination leaf framing + the arity-3
  fold-membership identity (`axpbypcz(α,x,β,y,γ,z) = linear_combination [(α,x),(β,y),(γ,z)]`).
- `book/src/L3-L2/krylov-step-body-identity.md:97` (cycle-007/009 firm) — the mirror precedent
  classifying `axpbypcz` (among the seven L1 primitives) as L3-native by signature shape at its
  point-3 applicability condition. The structural justification this theme promotes to dominant.
- `book/src/L3-L2/scal-body-identity.md` (cycle-041 D6 firm) — the arity-1 fold-member sibling of the
  same `linear_combination` fold; the structural template this arity-3 edge follows.

Cross-layer audit (the empirical-match anchor):

- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`
  §"(2) the BLAS-1 cohort" — the HIGH CONFIDENCE classification of the `axpbypcz` rotation as
  identity-in-form, the dispatch rationale for the cycle-011 L3 `axpbypcz` backfill and (now) this
  L3>L2 edge.

Onward edges (cross-reference, not this theme's content):

- `book/src/L2-L1/axpbypcz-leaf-identity.md` (this cycle D8) — the onward L2>L1 edge into the L1
  leaf; also identity-in-form (all fusion deferred to the fold's arity-3 row). Co-dispatched this
  cycle.
- `book/src/L1/axpbypcz.md` (cycle-003 firm) + `book/src/L1-L0/axpbypcz-mutation-rotation.md` (firm
  cycle-022) — the L1 leaf and its in-place L0 mutation rotation (4 sub-patterns + the
  mixed-justification `γ==0` algebraic sub-rule), reached via the onward edge.

Transitive L0 evidence (inherited from the firm L1 leaf; not re-localized — identity-in-form edge,
L0 evidence transitive through L1; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:745-758` — real-real `AXPBYPCZ` specialisation with the `γ==0` branch
  (`add(α,x,β,y,z)` fast-path at `:751`; `AXPBY(α,x,γ,z); z.Add(β,y)` slow-path at `:755-756`).
- `palace/linalg/vector.hpp:313-316` — the free-function template `AXPBYPCZ` decl
  (`z = α·x + β·y + γ·z`).

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS
([`L3/axpbypcz`](../L3/axpbypcz.md)) is firm (cycle-011); the L2 RHS
([`L2/axpbypcz`](../L2/axpbypcz.md)) is firming this cycle (wave-1 D5). The body is the identity
rotation on a single fused leaf field operation; **there is no wrapper to rotate** (no
`(op, K, s)`→`IterState` consolidation, no outer-loop dissolution — `axpbypcz` is a leaf, not a step
body). The structural justification (whole-tensor six-arg signature, no element loop, no iteration
view) is the `krylov-step-body-identity` point-3 condition specialized to the standalone leaf
(naming `axpbypcz` at line 97) and promoted to dominant; the empirical-match anchor is the firm
cross-layer audit + the `krylov-step-body-identity:97` L3-native classification. No speculative
operator, no negative-anchor reconstruction, no sequential obstruction. The arity-3 fold-member
counterpart of `scal-body-identity` (arity-1), both leaf members of the `linear_combination` fold.

A standing design fork (`dot-l2-leaf-floor-vs-fold-only-design`; batch-12-resolved, recommended
KEEP-(b) by the cycle-042 cross-cutter audit) is whether the BLAS-1 / linear-combination leaf cohort
should be realized as standalone same-named floors (the **(b)** realization this theme is built on)
or absorbed into the `linear_combination` fold (the **(a) fold-only** reading). Under the fold-only
reading, the L2 RHS this theme targets would re-point from a standalone `axpbypcz` floor to the
fold's arity-3 row. The theme is stated against the (b) realization, consistent with the firm L2
floor entry D5 lands this cycle.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L2 floor leaf *up* to the L3 whole-tensor form is the value-thread-isomorphic identity
  rotation: the L2 signature has no element loop exposed, which is exactly what makes it L3-native by
  construction. No additional structure is required for the lift. This reverse-direction note lives
  here in working notes per the high→low layer-definition discipline; the formal chapter narrates
  only L3 → L2.

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (this
  theme's L3>L2 identity ∘ the L2>L1 `axpbypcz-leaf-identity` identity) is annotated in-line at the
  `axpbypcz` entries per the CLAUDE.md invariant "Identity rotations across non-adjacent layers are
  annotated in-line, not via a dedicated lowering directory" — no `book/src/L3-L1/` directory. This
  theme + the co-dispatched `axpbypcz-leaf-identity` compose to capture it.

- **L3 `axpbypcz` staleness (cycle-044 sweep, NOT here).** The firm L3 `axpbypcz` entry currently
  says the L3→L1 rotation "does not pass through L2 because `axpbypcz` is an L1 leaf, not an L2
  composition" (`L3/axpbypcz.md:106,125`), predating both the L2 floor (D5) and this L3>L2 edge. Now
  that an adjacent same-named L2 floor exists, that prose wants a light refresh (the L3>L2 hop is
  identity-in-form to this floor, then this floor is identity-in-form to L1). Deferred to a cycle-044
  sweep, flagged in the D5 OQ as well; not authored here (this theme is correct as written — it
  lowers the L3 leaf to the L2 floor identity-in-form, exactly as `scal-body-identity` does).

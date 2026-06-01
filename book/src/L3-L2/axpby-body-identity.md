# axpby-body-identity

The L3>L2 lowering theme for the BLAS-1 leaf `axpby`. The rewrite is **identity-in-form on the
body** with **no wrapper rotation** — `axpby` is a leaf whole-tensor field operation (the fused
two-scalar two-vector update `α·x + β·y`), not a step body, so the L3 whole-tensor form lowers into
the L2 floor form by the identity on the primitive itself. There is no `(op, K, s)`→`IterState`
consolidation and no outer-loop dissolution to perform (the two surface adjustments that the sibling
[`krylov-step-body-identity`](./krylov-step-body-identity.md) carries at its wrapper); `axpby` has
no wrapper. The body IS the identity. `axpby` is one of the seven BLAS-1 primitives that are
**L3-native by signature shape** (no per-element loop visible at either layer), so the iteration
rotation is already complete at the signature level and the L3>L2 body edge is the identity. This is
the arity-2 analogue of [`scal-body-identity`](./scal-body-identity.md) (the arity-1 leaf) and
[`dot-body-identity`](./dot-body-identity.md) (the reduce-to-scalar leaf), and the leaf-primitive
counterpart of `krylov-step-body-identity` (which is identity-in-form on a multi-primitive kernel
body); here the identity is on a single leaf.

## Slug

`axpby-body-identity`

## Context

The `axpby` lowering relationships span three adjacent layers, all identity-in-form because `axpby`
is a BLAS-1 leaf with no iteration view and (beyond the deferred arity-2 single-aligned pass) no
kernel fusion:

- **L3 form** ([`L3/axpby`](../L3/axpby.md), firm cycle-011) — the whole-tensor fused field
  operation `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]`, the
  iteration-rotation rendering. Carries **no iteration view** (leaf primitive, not a step body) and
  **no sequential obstruction** (every element independent under the per-element `α·x[i] + β·y[i]`).
  The LHS of this theme. Consumed inside `krylov-step`'s iterate-stratum update.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/axpby`](../L2/axpby.md), firming cycle-043 D4) — the fusion-rotation floor leaf,
  the base fused two-scalar two-vector primitive and the arity-2 member of the `linear_combination`
  fold. The RHS of this theme.
- **L2>L1 form** ([`L2-L1/axpby-leaf-identity`](../L2-L1/axpby-leaf-identity.md), firming cycle-043
  D7) — the onward edge into the L1 leaf; also identity-in-form (the fold's arity-2 row, fusion
  deferred to the fold-parent). Co-dispatched this cycle.

This theme is the **leaf-primitive counterpart** of the firm
[`krylov-step-body-identity`](./krylov-step-body-identity.md) (cycle-007/009). The `krylov-step`
theme establishes the pattern "identity-in-form on the kernel **body**, with surface adjustments at
the **wrapper**"; its point-3 applicability condition names the seven L1 primitives — including
**`axpby`** — as L3-native by signature shape: "each operates on whole-tensor inputs with no
element-loop exposed at L2. This is what makes the L3>L2 rotation identity-in-form rather than
requiring a decomposition step (each L1 primitive is *also* L3-native because its signature has no
per-element loop visible)" (`krylov-step-body-identity.md:97`, which lists `axpby` explicitly among
`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`). This theme is the standalone-leaf
realization of that classification for `axpby`: the body is the identity, **and there is no wrapper
at all** — `axpby` is not a step body, so the two wrapper adjustments the `krylov-step` theme carries
(the `(op, K, s)`→`IterState` consolidation and the outer-loop-to-driver-by-role dissolution) have
no analog here.

## L3 form (LHS)

The L3 whole-tensor form ([`L3/axpby`](../L3/axpby.md) §Signature):

    axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpby α x β y = α·x + β·y

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `α, β` scalars
(`real` or `complex`, or `real` promoted against complex `x, y`); `x, y : Tensor[N]` a single shared
length axis, read-only at L3; result `Tensor[N]` of the same axis with
`result[i] = α·x[i] + β·y[i]` for every `i ∈ [0, N)`. The operator carries **no iteration view** (it
is a leaf field operation, not a step body) and **no sequential obstruction** (every element is
independent of every other under the per-element fused update — embarrassingly parallel, fully
GPU-friendly). No L4 wrapper machinery applies (leaf primitives appear inside L4 operator bodies as
let-bindings, not as first-class L4 typed-wrapper anchors — the cross-layer-cross-cutter "L4
candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 cohort; `L3/axpby.md` §"Lifts from").

## L2 form (RHS)

The L2 floor form ([`L2/axpby`](../L2/axpby.md) §Signature, firming cycle-043 D4):

    axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpby α x β y = α·x + β·y

The base fused two-scalar two-vector leaf in the fusion-rotation vocabulary — **and** the arity-2
member of the [`linear_combination`](../L2/linear_combination.md) fold
(`axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`, `linear_combination.md:70`, cited NOT
merged). The signature is **textually identical to the L3 form** modulo notation; the body is the
same single whole-tensor fused field operation. The nine algebraic laws hold unchanged across the
edge (L3 §Algebraic laws ≡ L2 §Algebraic laws — both inherit the L1 leaf's nine laws). The only
fusion note the L2 floor carries is the arity-2 single-aligned `add(α, x, β, y, y)` pass (the
arity-2 case of the fold's §"Fusion note", deferred to the fold-parent); at L3 even that note is
absent (L3 exposes no element loop at all).

## The rewrite (L3 → L2)

The rewrite is the **identity on the leaf primitive's body**, with **no wrapper adjustment**:

    axpby α x β y   (L3 whole-tensor field op)   ⇒   axpby α x β y   (L2 floor leaf)

The body maps trivially — one binding, one primitive, same position, same dataflow. Every L3 binding
maps to the same L2 binding at the same position:

    | L3 leaf (`L3/axpby`)                              | L2 leaf (`L2/axpby`)                              | Mapping  |
    |---------------------------------------------------|---------------------------------------------------|----------|
    | `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` | `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` | Identity. Same whole-tensor quaternary signature. |
    | `axpby α x β y = α·x + β·y` (whole-tensor field op; no iteration view) | `axpby α x β y = α·x + β·y` (base fused leaf; arity-2 fold member) | Identity. Same single fused field operation. The only framing difference is documentary: L3 frames `axpby` as a whole-tensor field operation in the iteration-rotation vocabulary; L2 frames the same operator as a base fusion-rotation primitive (and the arity-2 fold member). No operational adjustment occurs. |
    | per-element kernel `α·x[i] + β·y[i]`              | per-element kernel `α·x[i] + β·y[i]`              | Identity. Same element-local, reduction-free, rank-local relation. |
    | nine algebraic laws + four non-laws               | nine algebraic laws + four non-laws               | Identity. Inherited unchanged across the chain. |
    | no sequential obstruction                         | no sequential obstruction                         | Identity. Leaf field op at both layers; the pinned summation order of the arity-2 fused pass is an L0 non-law, not an L2/L3 structural element. |

The mapping is total and bijective on the leaf body: every L3 binding has an L2 partner and every L2
binding has an L3 partner. This is the **identity-in-form** property.

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two surface
adjustments at the wrapper around its kernel body: (1) the L3 `(op, K, s)` positional tuple
consolidates into the L2 unified `IterState` record (state-hiding), and (2) the L3 tail-recursive
outer loop `iterate_while_L3` collapses to the L2 outer-driver-by-role reference
(abstraction-by-role). **Neither has an analog for `axpby`**: `axpby` is a single leaf field
operation, not a step body with an `(op, K, s)` carrier and an outer loop. There is no `IterState`
(no state record — `axpby` is a pure positional function), and there is no outer driver (no loop
folds `axpby` calls at the operator itself; `axpby` is *called by* step bodies like `krylov-step`'s
`krylov_update`, but those loops belong to the step body, not to `axpby`). The mapping is total and
bijective on a single binding — the degenerate maximal case of the identity-in-form property.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `axpby` endpoints) when:

1. **`axpby` is L3-native by signature shape.** Its signature
   `Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` exposes no per-element loop at L2 or
   L3; the fused update over the length axis `N` is a single semantic step at both layers. This is
   the load-bearing condition (per `krylov-step-body-identity.md:97`, which names `axpby` among the
   seven L3-native primitives). Satisfied by construction: `axpby` is a leaf field operation.

2. **The L2 form is the same-named leaf-floor** (`book/src/L2/axpby.md`), value-thread-isomorphic to
   the L3 leaf. If the L2 scalar-weighted-vector-sum surface were the fold-only realization (no
   `axpby` leaf at L2 — the wave-1 D2 reading), the L3 leaf's adjacent L2 parent would be the
   fold-parent `linear_combination` (the L3>L2 edge would lower to the fold's arity-2 form, not to a
   same-named L2 `axpby`), and this theme's RHS would re-anchor. This condition records the design
   presupposition explicitly (see this theme's authoring report §Open-questions and the batch-12
   meta-phase OQ `dot-l2-leaf-floor-vs-fold-only-design`).

3. **`axpby` is treated as a leaf primitive, not decomposed.** `axpby` does not decompose into other
   L3 or L2 primitives — the fused `α·x + β·y` pass is a single field operation; its sub-operations
   (two scalar multiplies, one element-wise add) are below both layers' resolution, and the fusion
   preserves the algebraic statement `α·x + β·y` as a primitive linear combination (the
   `axpby-as-primitive` decision,
   [`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md);
   fuse, don't decompose into `scal ∘ axpy`).

4. **No iteration view, no sequential obstruction.** `axpby` is element-local, reduction-free,
   rank-local; every element is independent. There is no outer loop, no carry trajectory, no
   recurrence — so there is nothing for the L3 iteration rotation to have rotated and nothing for the
   L3>L2 lowering to dissolve.

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the leaf's signature shape
`Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` is whole-tensor by construction at both
layers — no element loop is exposed at L2, no iteration view at L3. The L3 vocabulary at this scope
demands whole-tensor field operations with no element loop exposed; `axpby` satisfies this *at L2
already*, so the rotation is the identity. This is the same structural argument the
`krylov-step-body-identity` theme makes as its point-3 condition for each primitive in the kernel
body — here promoted to dominant because there is no kernel body wrapping the leaf, only the leaf
itself.

**Empirical-match (secondary)**: the cross-layer-cross-cutter identity-in-form audit
(`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"(2) the
BLAS-1 cohort") classified the `axpby` L3↔L1 rotation as identity-in-form by inspection of the firm
L3 entry and the firm `krylov-step-body-identity`; the firm `krylov-step-body-identity` names
`axpby` L3-native at line 97. This theme's L3>L2 edge is the standalone-leaf realization of that
audited classification, now that the L2 floor entry exists (cycle-043 D4) for the rotation to target.
The L3 LHS and L2 RHS were authored independently (L3 cycle-011, L2 cycle-043 D4) as
value-thread-isomorphic to the same firm L1 leaf, and they agree on every law and every variant axis
by independent transcription.

## Speculative L2 operators

**None.** This theme is the identity rotation between firm endpoints: the L3 LHS
([`L3/axpby`](../L3/axpby.md)) is firm (cycle-011), and the L2 RHS ([`L2/axpby`](../L2/axpby.md)) is
firming (cycle-043 D4). No new L2 vocabulary is introduced. `axpby` does not get its own L4
typed-wrapper anchor (leaf primitives appear inside L4 operator bodies as let-bindings — the
cross-layer-cross-cutter "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 cohort), so there
is no upstream L4>L3 theme for `axpby` either; the L3 form is L3-native by signature and this theme
closes its downward edge to the L2 floor.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/axpby.md` (cycle-011 firm) — the L3 whole-tensor form (LHS). Signature (`:30-32`),
  semantics (element-local, reduction-free, rank-local, no iteration view, no sequential
  obstruction; `:51-65`), nine algebraic laws (`:67-88`), the leaf-not-step-body
  §"Iteration-rotation marker" (`:63-65`), two variant axes (`:103-110`). The §"Lowers to"
  (`:116-120`) currently records identity-in-form to L1 (no L2 chapter existed); this theme supplies
  the now-present adjacent L3>L2 edge (downstream-consistency touch on the L3 entry's §"Lowers to"
  framing flagged in §Open-questions of the authoring report — the c044 L3-staleness sweep).
- `book/src/L2/axpby.md` (firming cycle-043 D4) — the L2 floor form (RHS): the same-named arity-2
  leaf of `linear_combination`, value-thread-isomorphic to the L1/L3 leaf, laws inherited unchanged.
  (Lands at this cycle's integration alongside this theme.)
- `book/src/L3-L2/krylov-step-body-identity.md:97` (cycle-007/009 firm) — §"Applicability
  conditions" point 3: the load-bearing statement that the seven BLAS-1 primitives (including
  **`axpby`**, named explicitly) are L3-native by signature shape (no per-element loop visible),
  which is the structural justification for this identity edge. **Self-verified (anchor `axpby`
  @97 via `tools/citecheck/citecheck.py`).**
- `book/src/L2/linear_combination.md:70` (cycle-018 firm) — the arity-2 specialization identity
  `axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`. The fold-parent membership anchor; cited,
  NOT merged.
- `book/src/L3-L2/scal-body-identity.md` (cycle-041 firm) + `book/src/L3-L2/dot-body-identity.md`
  (cycle-041 firm) — the sibling L3>L2 body-identity themes this entry's structure mirrors (same
  no-wrapper leaf-primitive analogue of `krylov-step-body-identity`). `scal` is the arity-1 leaf;
  `axpby` is the arity-2 member of the same fold.

Cross-layer audit (the empirical-match anchor):

- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"(2) the
  BLAS-1 cohort" — the HIGH CONFIDENCE classification of the `axpby` rotation as identity-in-form,
  the dispatch rationale for the cycle-011 L3 `axpby` backfill and (now) this L3>L2 edge.

Onward edges (cross-reference, not this theme's content):

- `book/src/L2-L1/axpby-leaf-identity.md` (cycle-043 D7) — the onward L2>L1 edge into the L1 leaf;
  also identity-in-form (the fold's arity-2 row, fusion deferred to the fold-parent). Co-dispatched
  this cycle.
- `book/src/L1/axpby.md` (cycle-003 firm) + `book/src/L1-L0/axpby-mutation-rotation.md` (firm
  cycle-002) — the L1 leaf and its in-place L0 mutation rotation, reached via the onward edge.

Transitive L0 evidence (inherited from the firm L1 leaf; not re-localized — identity-in-form edge,
L0 evidence transitive through L1; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:726-730` — real-real `AXPBY` → MFEM `add(α, x, β, y, y)` (the arity-2
  single-aligned fused pass).
- `palace/linalg/vector.cpp:732-737` — complex-complex `AXPBY` → member form `y.AXPBY(α, x, β)`.
- `palace/linalg/vector.hpp:130-131,309-311` — `ComplexVector::AXPBY` member decl + the free-function
  template `AXPBY` decl.

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS
([`L3/axpby`](../L3/axpby.md)) is firm (cycle-011); the L2 RHS ([`L2/axpby`](../L2/axpby.md)) is
firming (cycle-043 D4). The body is the identity rotation on a single leaf field operation; **there
is no wrapper to rotate** (no `(op, K, s)`→`IterState` consolidation, no outer-loop dissolution —
`axpby` is a leaf, not a step body). The structural justification (whole-tensor quaternary signature,
no element loop, no iteration view) is the `krylov-step-body-identity` point-3 condition specialized
to the standalone leaf and promoted to dominant; the empirical-match anchor is the firm cross-layer
audit + the `krylov-step-body-identity:97` L3-native classification (which names `axpby` explicitly).
No speculative operator, no negative-anchor reconstruction, no sequential obstruction. The arity-2
member of the BLAS-1-leaf L3>L2 cohort — the leaf-primitive counterpart of `krylov-step-body-identity`
alongside `dot-body-identity` (reduce-to-scalar) and `scal-body-identity` (arity-1).

> **Design-presupposition note (not a status reduction).** This theme presupposes the wave-1 **(b)
> same-named leaf-floor** realization of `L2/axpby` (Applicability condition 2). Under the wave-1 D2
> "fold-only" reading (no `axpby` leaf at L2), this theme's RHS would re-anchor to the fold-parent
> `linear_combination` (the arity-2 form). The c042 cross-cutter audit recommends KEEPING leaf-floor
> (b) (`book/src/L2/index.md` §Working-Notes). Surfaced for the batch-12 meta-phase to adjudicate (OQ
> `dot-l2-leaf-floor-vs-fold-only-design`); the theme is self-coherent under the leaf-floor reading it
> is built on.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L2 floor leaf *up* to the L3 whole-tensor form is the value-thread-isomorphic identity
  rotation: the L2 signature has no element loop exposed, which is exactly what makes it L3-native by
  construction. No additional structure is required for the lift. This reverse-direction note lives
  here in working notes per the high→low layer-definition discipline; the formal chapter narrates only
  L3 → L2.

- **Leaf-vs-fold fork (batch-12 meta-phase adjudication).** See §Status design-presupposition note;
  recorded as the cross-CYCLE OQ `dot-l2-leaf-floor-vs-fold-only-design`. `axpby` rides the same fork
  as `dot`/`scal` (fold-parented floor); the c042 cross-cutter audit recommends keeping leaf-floor
  (b).

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (this
  theme's L3>L2 identity ∘ the L2>L1 `axpby-leaf-identity` identity) is annotated in-line at the
  `axpby` entries per the CLAUDE.md invariant "Identity rotations across non-adjacent layers are
  annotated in-line, not via a dedicated lowering directory" — no `book/src/L3-L1/` directory. This
  theme + the co-dispatched `axpby-leaf-identity` compose to capture it.

- **L3/axpby §"Lowers to" staleness (c044 sweep, NOT here).** The firm `book/src/L3/axpby.md`
  (cycle-011) §"Lowers to" (`:116-120`) records identity-in-form straight to L1 ("no L2 intermediate
  because the BLAS-1 primitives are L1 leaves not L2 compositions"), which predates the L2 floor. Now
  that the adjacent L2 `axpby` floor + this L3>L2 edge exist, that framing is stale — the L3 form
  should lower to the present adjacent L2 floor, not skip to L1. This is the same c044 L3-staleness
  sweep item the D4 harvester surfaced (re-anchor the L3 BLAS-1 cohort `lowers_to` framing to the new
  L2 floors); **not in scope here** (modifying the L3 entry is the harvester's job, not the
  abstractor's). Surfaced for the OQ ledger.

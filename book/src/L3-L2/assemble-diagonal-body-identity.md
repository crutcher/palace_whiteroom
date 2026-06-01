# assemble-diagonal-body-identity

The L3>L2 lowering theme for the `assemble_diagonal` operator-to-data diagonal-extraction primitive.
The rewrite is **identity-in-form on the body**: the L3
[`assemble-diagonal`](../L3/assemble-diagonal.md) whole-operator field operation lowers to the L2
[`assemble-diagonal`](../L2/assemble-diagonal.md) fusion-form floor with the same signature, the same
operator-to-data extraction semantics, and the same algebraic laws — value-thread-isomorphic on the
primitive. `assemble_diagonal` is **L3-native by signature shape** (no per-element loop visible at
either layer; the per-row read of the `(i, i)` entries is a single semantic step), so the iteration
rotation is already complete at the signature level and the L3>L2 body edge is the identity. This is
the operator-to-data analogue of [`dot-body-identity`](./dot-body-identity.md) (the BLAS-1-leaf
case); here the L3-native primitive is the operator-to-data sibling of `apply_linop`, not a BLAS-1
reduction. There is **no fold-parent and no wrapper** to carry a surface adjustment — the edge is the
pure identity.

## Slug

`assemble-diagonal-body-identity`

(The `-body-identity` slug matches the cycle-041 [`dot-body-identity`](./dot-body-identity.md) landed
convention for L3>L2 thin-identity edges — identity-in-form on the body — paired with the L2>L1
[`assemble-diagonal-leaf-identity`](../L2-L1/assemble-diagonal-leaf-identity.md) below it; explicitly
NOT the `-fold-specialization` outlier slug.)

## Context

`assemble_diagonal` spans three present chapters — firm L3
[`assemble-diagonal`](../L3/assemble-diagonal.md) (the iteration-rotation rendering, consumed inside
the diagonal-preconditioner-apply setup of the Jacobi / Chebyshev smoother bodies; firm cycle-037),
the L2 [`assemble-diagonal`](../L2/assemble-diagonal.md) floor (harvested cycle-042 wave-1 D4), and
firm L1 [`assemble-diagonal`](../L1/assemble-diagonal.md) (the mutation-rotation leaf). This theme is
the **L3>L2 edge** between the top two; the L2>L1 edge below is
[`assemble-diagonal-leaf-identity`](../L2-L1/assemble-diagonal-leaf-identity.md).

The edge is the **identity-in-form** case. The firm L3 entry already records its lowering as
identity-in-form (`book/src/L3/assemble-diagonal.md` §"Lowers to"); historically it pointed straight
at L1 (no L2 `assemble_diagonal` chapter existed), citing the cycle-012 non-adjacent in-line-identity
convention. With the L2 `assemble_diagonal` floor now present, this theme supplies the
**adjacent-edge** L3>L2 rotation the L3 entry's §"Lowers to" had to skip — so the L3 field operation
can lower to an adjacent same-named L2 parent (per CLAUDE.md §Methodology invariants
**Identity-lowerings still require both L levels**) rather than non-adjacently to L1.

`assemble_diagonal` is **L3-native by signature shape**. The L3>L2
[`krylov-step-body-identity`](./krylov-step-body-identity.md) §"Applicability conditions" point 3
(`krylov-step-body-identity.md:97`) states the load-bearing property for the seven BLAS-1 primitives:
each "operates on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2
rotation identity-in-form rather than requiring a decomposition step (each L1 primitive is *also*
L3-native because its signature has no per-element loop visible)." `assemble_diagonal` is **not** one
of those seven BLAS-1 primitives — it is the **operator-to-data sibling of `apply_linop`** — but it
satisfies the *same* L3-native-by-signature-shape property for the *same* structural reason: its
signature `LinearOperator[N, N] -> Tensor[N]` exposes no element loop, and the per-row read of the
`(i, i)` entries is a single semantic step at both L3 and L2 (the L3 entry's §"Iteration-rotation
marker" records this explicitly — diagonal extraction is a per-row read of operator-intrinsic data
with **no sequential obstruction**, each `result[i]` depending on `A`'s `(i, i)` entry alone). The
iteration rotation is therefore already done at the signature level, and the L3>L2 body edge is the
identity.

## L3 form (LHS)

The L3 form is the whole-operator field operation (`book/src/L3/assemble-diagonal.md` §Signature, firm
cycle-037):

    assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]
    assemble_diagonal A = diag(A)                          -- single semantic step; no element loop

rendered as **one node in the iteration-rotation calculus** (`L3/assemble-diagonal`
§"Iteration-rotation marker"): the per-row read of the operator's `(i, i)` entries lifts as a
whole-operator field operation with **no sequential obstruction** (each `result[i]` depends on `A`'s
`(i, i)` entry alone, with no cross-row recurrence and no carry threaded between rows). This is the
structural distinction from the `partial-obstruction` L3 operators (`chebyshev`, `eigsolve`), whose
bodies lift but whose loops do not: `assemble_diagonal` has **no loop to obstruct** — it is one of the
layer's clean whole-operator field operations, embarrassingly parallel (a sparse-CSR realization reads
`N` stored diagonal entries independently; a matrix-free realization accumulates element-local
contributions, a reduction with no inter-row sequencing). The operator-representation axis is absorbed
into the opaque `LinearOperator` type; the element-type axis is parameterised.

## L2 form (RHS)

The L2 form is the `assemble_diagonal` floor (`book/src/L2/assemble-diagonal.md` §Signature, harvested
cycle-042 wave-1 D4) — the fusion-rotation rendering of the same operator-to-data extraction:

    assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]
    assemble_diagonal A = diag(A)

It is the standalone operator-to-data floor — the operator-to-data sibling of `apply_linop`, belonging
to **no fold cohort** (fork-independent). The L2 form's fusion-rotation content is **degenerate** (no
multi-operation kernel-fusion at the operator-to-data boundary; the representation-specific
diagonal-extraction mechanics are representation-axis-absorbed L0 concerns deferred to the L1>L0
lowering); the floor itself is value-thread-isomorphic to the L3 form on the signature.

## The rewrite (L3 → L2)

The rewrite is the **identity on the body**. Every L3 binding maps to the same L2 binding at the same
position:

    | L3 form (`L3/assemble-diagonal`)         | L2 floor (`L2/assemble-diagonal`)        | Mapping  |
    |------------------------------------------|------------------------------------------|----------|
    | `assemble_diagonal :: LinOp[N,N] -> Ten[N]` | `assemble_diagonal :: LinOp[N,N] -> Ten[N]` | Identity. Same whole-operator signature; no shape change. |
    | `assemble_diagonal A = diag(A)`          | `assemble_diagonal A = diag(A)`          | Identity. Same operator-to-data extraction; `result[i] = Aᵢᵢ`. |
    | square `M = N` precondition              | square `M = N` precondition              | Identity. Same intrinsic-square contract. |
    | opaque `LinearOperator` (representation absorbed) | opaque `LinearOperator` (representation absorbed) | Identity. Same variant-absorption over the representation axis. |
    | per-row read = single semantic step      | per-row read = single semantic step      | Identity. The L3 "single semantic step" IS the L2 single extraction; no element loop at either layer. |
    | no sequential obstruction                | no sequential obstruction                | Identity. Diagonal extraction lifts as a whole-operator op at both layers; no cross-row recurrence. |
    | six algebraic laws + four non-laws       | six algebraic laws + four non-laws       | Identity. Inherited unchanged across the chain (operator-scaling / sum linearity, identity, zero, diagonal round-trip, complex real/imag split + the four non-laws). |

The mapping is total and bijective on the body: every L3 binding has an L2 partner and every L2
binding has an L3 partner. This is the **identity-in-form** property. Unlike
[`krylov-step-body-identity`](./krylov-step-body-identity.md), there is **no wrapper around the body**
to carry a surface adjustment — `assemble_diagonal` is a single leaf field operation, not a kernel
body inside an `IterState` / outer-driver wrapper, and (unlike `dot-body-identity`'s fold leaf) it has
**no fold-parent** either; the L3>L2 edge is the pure identity with no wrapper-level and no fold-level
rotation.

**The load-bearing non-law preserved through the edge (NOT erased).** The matrix-free
high-order-Nedelec (H(curl)) **approximate-diagonal** non-law is carried across this edge unchanged: a
sparse-matrix realization of `A` reads the **exact** stored diagonal, while a matrix-free
high-order-Nedelec realization of the *same* mathematical operator produces an **approximate** diagonal
(face-dof sharing in 3D). Load-bearing per the CLAUDE.md taxonomy — the representation can change the
diagonal *value*, not merely its bit pattern. Both the L3 form (§"Algebraic laws", "Exactness across
representations") and the L2 floor (§"Algebraic laws", non-law) record it as an explicit
positively-anchored non-law; **this rotation does NOT erase it** (the L2 fusion rotation being
degenerate, there is no de-fusion step in which it could be lost). It is sourced from the Palace AMR
convergent-diagonal note (`palace/linalg/rap.cpp:163-164`) and test-witnessed
(`test/unit/test-libceed.cpp:367-376`, relaxing `rtol` to `1.0` for the high-order non-tensor-basis
Nedelec case), both transitive through the L1 home. The concretization of where the approximation
arises (the matrix-free element-accumulation order) lands at the L1>L0 lowering; the non-law is
preserved by reference through this edge.

## Applicability conditions

The identity rewrite is valid when:

1. **`assemble_diagonal` is L3-native by signature shape.** Its signature `LinearOperator[N, N] ->
   Tensor[N]` exposes no per-element loop at L2 or L3; the per-row read of the `(i, i)` entries is a
   single semantic step at both layers with no sequential obstruction. This is the load-bearing
   condition — the *same* L3-native-by-signature-shape property `krylov-step-body-identity.md:97`
   states for the seven BLAS-1 primitives, satisfied here by the operator-to-data sibling of
   `apply_linop` for the same structural reason (no element loop visible). Satisfied by construction:
   `assemble_diagonal` is a per-row operator-introspection read, embarrassingly parallel.

2. **The L2 form is the same-named floor** (`book/src/L2/assemble-diagonal.md`),
   value-thread-isomorphic to the L3 form. Confirmed by construction: the L2 floor is a thin
   identity-in-form entry inheriting the laws unchanged from the firm L1 leaf.

3. **The leaf is value-thread-isomorphic across the edge.** The L3 `assemble_diagonal` field operation
   and the L2 `assemble_diagonal` floor share the signature, the operator-to-data extraction semantics,
   the intrinsic-square `M = N` precondition, the variant-absorption over the representation axis, and
   the six laws + four non-laws (including the load-bearing exact-vs-approximate caveat). Confirmed by
   construction: both chapters inherit the laws unchanged from the firm L1 leaf.

This theme does **not** depend on any fold-design adjudication. Unlike the cycle-041 `dot-body-identity`
edge — whose L2 RHS re-points to the fold-parent `inner_product` under the wave-1 (a) fold-only reading
(OQ `dot-l2-leaf-floor-vs-fold-only-design`) — `assemble_diagonal` has **no fold-parent**, so there is
no fold-only reading to re-anchor its RHS to. The floor is standalone regardless of how the batch-12
meta-phase adjudicates the BLAS-1 fork; this edge is unaffected by it (recorded in §Open-questions of
the authoring report).

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: `assemble_diagonal`'s signature is whole-operator-to-data extraction with no
element loop exposed at either L2 or L3 — the L3-native-by-signature property
(`krylov-step-body-identity.md:97`, the same property the seven BLAS-1 primitives satisfy, satisfied
here by the operator-to-data sibling of `apply_linop`). A primitive that is L3-native by signature
shape rotates L3→L2 as the identity by construction: there is no iteration to rotate (the per-row read
is already a single semantic step at both layers, with no sequential obstruction) and no wrapper or
fold-parent around the leaf to adjust. This is the same structural argument the `dot-body-identity`
theme makes for the `dot` leaf, applied to the operator-to-data `assemble_diagonal` field operation.

**Empirical-match (secondary)**: the L3 form (firm cycle-037) and the L2 floor (firming cycle-042
wave-1 D4) were authored independently as value-thread-isomorphic to the same firm L1 leaf, and they
agree on every law, every non-law, every variant axis, and every signature row by independent
transcription. The identity is observational on the two existing firm/firming chapters.

## Speculative L2 operators

**None.** Both endpoints are existing vocabulary: the L3 LHS is the firm `assemble_diagonal` field
operation (firm cycle-037), the L2 RHS is the `assemble_diagonal` floor (firming cycle-042 wave-1 D4).
This theme is the identity edge between existing chapters; it proposes no new operators. (The same
load-bearing matrix-free approximate-diagonal non-law that the sibling
[`assemble-diagonal-leaf-identity`](../L2-L1/assemble-diagonal-leaf-identity.md) carries applies here
too — the non-law maps identity-in-form, preserved not erased; not a status reduction.)

## Verified-against

L3 / L2 anchors (the two endpoints):

- `book/src/L3/assemble-diagonal.md` (firm cycle-037) — the L3 form (LHS): the whole-operator
  operator-to-data signature (`:34-35`), the iteration-rotation marker / no-sequential-obstruction
  statement (`:54-60`), the six algebraic laws (`:66-71`), the four non-laws including the load-bearing
  exact-vs-approximate caveat (`:73-78`), the variant axes (one orthogonal element-type + one absorbed
  operator-representation, `:100-118`), the §"Lowers to" (`:128-134`) which currently records
  identity-in-form to L1 via the non-adjacent convention. This theme supplies the now-present adjacent
  L3>L2 edge (downstream-consistency touch on the L3 entry flagged in §Open-questions of the authoring
  report).
- `book/src/L2/assemble-diagonal.md` (firming cycle-042 wave-1 D4) — the L2 floor (RHS): the standalone
  operator-to-data floor, value-thread-isomorphic to the L1/L3 form, laws + non-laws inherited
  unchanged, fusion degenerate. (Lands at this cycle's integration alongside this theme.)
- `book/src/L3-L2/dot-body-identity.md` (firm cycle-041) — the `-body-identity` slug + thin-identity
  structure precedent. (`dot` is a fold leaf; this entry is fork-independent — the difference is noted
  in §Context / §"The rewrite".)
- `book/src/L3-L2/krylov-step-body-identity.md:97` — §"Applicability conditions" point 3: the
  load-bearing statement that L3-native-by-signature-shape primitives (no per-element loop visible)
  rotate L3>L2 identity-in-form. `assemble_diagonal` satisfies this property for the same structural
  reason as the seven BLAS-1 primitives named there, though it is the operator-to-data sibling of
  `apply_linop`, not a BLAS-1 member. **Self-verified (anchor `L3-native` @97).**

L0 evidence (transitive through the firm L1 leaf; self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation; paths relative to `reference/palace/`):

- `palace/linalg/hypre.cpp:88` — `HypreCSRMatrix::AssembleDiagonal`'s `hypre_CSRMatrixExtractDiagonal`
  (the **exact** sparse-CSR stored-diagonal read; the embarrassingly-parallel per-row read).
  **Self-verified (anchor `hypre_CSRMatrixExtractDiagonal` @88).** Inherited transitively; the edge is
  identity so no new L0 claim is made here.
- `palace/fem/libceed/operator.cpp:139` — `CeedOperatorLinearAssembleAddDiagonal` (the matrix-free
  element-local accumulation; the source of the high-order-Nedelec approximation). **Self-verified
  (anchor `CeedOperatorLinearAssembleAddDiagonal` @139).**
- `palace/linalg/rap.cpp:163-164` — the AMR `|P|ᵀ dₗ` convergent-diagonal note (the documented source
  of the approximate-diagonal caveat). **Self-verified (anchor `convergent` @163).**
- `test/unit/test-libceed.cpp:367-376` — the diagonal-assembly test relaxing `rtol` to `1.0` for
  high-order 3D Nedelec non-tensor-basis spaces (the test-witnessed load-bearing approximation).
  **Self-verified (anchor `rtol` @371,375).** L0-equivalent semantic documentation per CLAUDE.md
  §"Tests as semantic supplement". The non-law is preserved by reference through this edge.

## Status

`firm` — the L3 LHS is the firm `assemble_diagonal` field operation (cycle-037), the L2 RHS is the
firm-this-cycle floor (D4 wave-1), and the rotation between two value-thread-isomorphic forms with
identical whole-operator signatures is the identity by construction (§"The rewrite (L3 → L2)" table is
total and bijective on the body). `assemble_diagonal` is L3-native by signature shape
(`krylov-step-body-identity.md:97`, satisfied by the operator-to-data sibling of `apply_linop`), so the
iteration rotation is already complete at the signature level, there is **no sequential obstruction**,
and there is **no wrapper and no fold-parent** around the leaf to adjust — the edge is the pure
identity. The load-bearing matrix-free high-order-Nedelec approximate-diagonal non-law is **preserved
through the edge unchanged** (positively anchored — `rap.cpp:163-164` + test-witnessed
`test-libceed.cpp:367-376`), NOT erased. No speculative operator, no negative-anchor reconstruction, no
literature inference — so `firm`, not `partly-constructive`.

> **Fork-independence note (not a status reduction).** Unlike the cycle-041 `dot-body-identity` edge,
> this theme does **not** presuppose any fold-design reading: `assemble_diagonal` is fork-independent
> (NO fold-parent — the operator-to-data sibling of `apply_linop`, not a fold leaf). It is therefore
> **unaffected** by the batch-12 meta-phase adjudication of the BLAS-1 design fork
> `dot-l2-leaf-floor-vs-fold-only-design` (the (a) fold-only reading has no fold-parent to re-point the
> RHS to). The L2 RHS stays the same-named standalone floor regardless. Surfaced so the meta-phase does
> not sweep this edge into the fork.

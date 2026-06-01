---
agent: abstractor
invoked_at: 2026-06-01T063231Z
scope: two adjacent thin-identity lowering themes — assemble-diagonal (L2>L1 leaf-identity + L3>L2 body-identity)
status: pending
inputs:
  - reports/2026-06-01T063231Z-cycle-042-harvester-L2-assemble-diagonal/CYCLE.md (wave-1 D4 — the L2 form source of truth; book/src/L2/assemble-diagonal.md co-lands this cycle, NOT yet on disk)
  - book/src/L1/assemble-diagonal.md (firm — the L1 RHS endpoint; signature, six laws, four non-laws, variant axes, full L0 evidence)
  - book/src/L3/assemble-diagonal.md (firm cycle-037 — the L3 LHS endpoint; identity-in-form rendering, no sequential obstruction)
  - book/src/L2-L1/dot-leaf-identity.md (firm cycle-041 — the -leaf-identity slug + thin-identity structure precedent)
  - book/src/L3-L2/dot-body-identity.md (firm cycle-041 — the -body-identity slug + thin-identity structure precedent)
  - book/src/L3-L2/krylov-step-body-identity.md:97 (the L3-native-by-signature-shape statement)
integrated_at: 2026-06-01T081245Z
integration_commit: 1d6592a
integration_notes: "cycle-042 batch integration (foundation-first L2-floor build); applied clean; see reports/2026-06-01T081245Z-integrator-finalize-cycle-42/CYCLE.md + cycle-042 STAGING row."
---

# CYCLE: two adjacent thin-identity lowering themes — assemble-diagonal (L2>L1 + L3>L2)

## Summary

`assemble_diagonal` (`d = diag(A)`) is the operator-to-data diagonal-extraction primitive with **firm L1**, **firm L3** (cycle-037), and a **firm L2 floor co-landing this cycle** (wave-1 D4). This dispatch authors the two adjacent thin-identity lowering edges that connect those three chapters — the **L2>L1** edge [`assemble-diagonal-leaf-identity`](book/src/L2-L1/assemble-diagonal-leaf-identity.md) and the **L3>L2** edge [`assemble-diagonal-body-identity`](book/src/L3-L2/assemble-diagonal-body-identity.md) — matching the cycle-041 `dot-leaf-identity` / `dot-body-identity` landed slug convention and thin-identity structure. Both edges are **identity-in-form on the primitive**: `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]` is value-thread-isomorphic across both rotations (same signature, same six operator-introspection laws, same four non-laws, same variant-axis profile — one orthogonal element-type + one absorbed operator-representation). The narration is **high→low** (L_{n+1} LHS lowering forward into L_n RHS). The chief structural difference from the `dot` precedents: `assemble_diagonal` is **fork-independent — NO fold-parent** (it is the operator-to-data sibling of `apply_linop`, NOT a fold leaf), so neither theme defers fusion content to a fold-parent — the L2 fusion is **degenerate** (no multi-operation kernel-fusion at the operator-to-data boundary; the representation-specific diagonal-extraction mechanics are representation-axis-absorbed L0 concerns deferred to the L1>L0 lowering). **LOAD-BEARING: the matrix-free high-order-Nedelec approximate-diagonal non-law is preserved by reference through BOTH theme edges** (positively anchored at `rap.cpp:163-164` + test-witnessed `test-libceed.cpp:367-376`); neither rotation erases the approximation. Both themes are `firm`. COUNT-OWNERSHIP: I append only my two theme rows (one per index) + two SUMMARY entries + the two theme bodies; I do NOT touch the consolidated theme-count tallies — D11 owns them; deferred.

## Proposed changes

```new:book/src/L2-L1/assemble-diagonal-leaf-identity.md
# assemble-diagonal-leaf-identity

The L2>L1 lowering theme for the `assemble_diagonal` operator-to-data diagonal-extraction
primitive. The rewrite is **identity-in-form on the leaf**: the L2
[`assemble-diagonal`](../L2/assemble-diagonal.md) floor lowers to the L1
[`assemble-diagonal`](../L1/assemble-diagonal.md) primitive with the same signature, the same
operator-to-data extraction semantics, and the same algebraic laws — value-thread-isomorphic on
the primitive. Unlike the cycle-041 BLAS-1 floor-edges (`dot-leaf-identity` etc.), this leaf has
**no fold-parent** to defer fusion content to: `assemble_diagonal` is the operator-to-data sibling
of `apply_linop`, belonging to no fold cohort. Its L2 fusion content is **degenerate** (no
multi-operation kernel-fusion at the operator-to-data boundary), so this theme records the identity
edge and defers the representation-specific diagonal-extraction mechanics — and the load-bearing
matrix-free approximate-diagonal non-law — to the L1>L0 lowering, **without erasing the
approximation**.

## Slug

`assemble-diagonal-leaf-identity`

(The `-leaf-identity` slug matches the cycle-041 [`dot-leaf-identity`](./dot-leaf-identity.md)
landed convention — an identity-leaf-lowering, NOT a fold→leaf dispatch — explicitly NOT the
`-fold-specialization` outlier slug, since `assemble_diagonal` is fork-independent and has no fold
to specialize.)

## Context

`assemble_diagonal` at L2 is the **floor** entry (`book/src/L2/assemble-diagonal.md`, harvested
cycle-042 wave-1 D4): the standalone operator-to-data diagonal-introspection primitive, rendered as
its own L2 chapter so the firm L3 [`assemble-diagonal`](../L3/assemble-diagonal.md) field operation
rests on an adjacent same-named L2 parent (per CLAUDE.md §Methodology invariants **Identity-lowerings
still require both L levels**) rather than skipping a layer to L1. This theme is the L2>L1 edge of
that floor. The L3>L2 edge above is
[`assemble-diagonal-body-identity`](../L3-L2/assemble-diagonal-body-identity.md).

The edge is the **identity-in-form** case: the L2 `assemble_diagonal` floor and the L1
`assemble_diagonal` leaf are value-thread-isomorphic on the primitive. This is the L2>L1 analogue of
the L3>L2 [`assemble-diagonal-body-identity`](../L3-L2/assemble-diagonal-body-identity.md) theme (the
other thin edge of the same primitive), and a sibling shape to the cycle-041
[`dot-leaf-identity`](./dot-leaf-identity.md) — except `assemble_diagonal` is **fork-independent**
(no fold-parent), so the "defer fusion to the fold-parent" mechanism of `dot-leaf-identity` does not
apply here; the fusion is degenerate and deferred to the L1>L0 lowering instead.

**Why this edge is the identity — and where the L2-layer work goes.** The L2 layer's defining work is
kernel-fusion de-fusion. For `dot`, that work is carried by the fold-parent
`inner-product-fold-specialization`. For `assemble_diagonal` there **is no fold-parent**, and the
operator-to-data boundary carries **no multi-operation kernel-fusion** to de-fuse: the L0 "fusion"
present in the diagonal-extraction realizations is the *representation-specific diagonal-extraction
mechanic* (the sparse-CSR Hypre stored-diagonal read, the matrix-free libCEED element-local
accumulation, the AMR `|P|ᵀ dₗ` prolongation-transpose assembly, the complex real/imag split), which
is below the L2 resolution — an L0 concern surfaced by the L1>L0 lowering, not an L2 composition to
de-fuse. So the L2 fusion content is **degenerate** (the L2 floor records it as one deferring note),
and the `assemble_diagonal` leaf's own L2>L1 edge — the rotation between the L2 floor chapter and the
L1 leaf chapter — is the identity, with the de-fusion treatment (and the load-bearing
exact-vs-approximate caveat) deferred to the L1>L0
[`assemble-diagonal-mutation-rotation`](../L1-L0/assemble-diagonal-mutation-rotation.md) lowering
theme.

## L2 form (LHS)

The L2 form is the `assemble_diagonal` floor (`book/src/L2/assemble-diagonal.md` §Signature,
harvested cycle-042 wave-1 D4) — the mutation-free operator-to-data extraction:

    assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]
    assemble_diagonal A = diag(A)

with the shape contract inherited unchanged from the L1 leaf:

- `A` — `LinearOperator[N, N]` — a **square** linear operator (domain axis `N` equals codomain axis
  `N`). Read-only. The operator-representation axis (sparse-CSR / matrix-free / parallel-wrapped /
  complex-wrapped) is **absorbed** into this opaque type at L2.
- result — `Tensor[N]` — the diagonal vector; `result[i] = Aᵢᵢ = eᵢᵀ A eᵢ` (the mathematical
  definition, NOT an implementation via `N` basis-vector probes).

The L2 form is **pure / out-of-place** (no destination buffer; the result is a fresh `Tensor[N]`).
The **square requirement** `M = N` is intrinsic (a diagonal is only defined where domain and
codomain index sets coincide). The L0 destination buffer `diag`, its sizing `diag.SetSize(height)`,
its `diag = 0.0` zero-init, the representation-specific extraction mechanic, the AMR
absolute-value-prolongation assembly, and the Dirichlet `DiagonalPolicy` BC post-step are NOT in the
L2 signature — they reappear only at the L1>L0 lowering.

## L1 form (RHS)

The L1 form is the firm `assemble_diagonal` leaf primitive (`book/src/L1/assemble-diagonal.md`
§Signature, firm) — identical in signature, semantics, and laws:

    assemble_diagonal :: (A: LinearOperator[N, N]) -> Tensor[N]
    assemble_diagonal(A) = diag(A)

The L1 leaf is the **mutation-rotation** rendering: it already drops the L0 destination buffer `diag`
(along with the sizing, the zero-init, the workspace, and the Dirichlet BC-policy step) from the
signature, and absorbs the operator-representation axis into the opaque `LinearOperator` type. The L1
entry is authoritative on every Palace-surface fact (the `AssembleDiagonal(diag)` virtual-method
family across the real `Operator` / complex `ComplexOperator` hierarchies, the concrete realizations,
the square-precondition enforcement sites, the consuming smoother call sites, the libCEED
diagonal-assembly unit test, the complete L0 evidence list); the L2 form does not duplicate them.

## The rewrite (L2 → L1)

The rewrite is the **identity on the leaf**. Every L2 binding maps to the same L1 binding at the
same position:

    | L2 floor (`L2/assemble-diagonal`)        | L1 leaf (`L1/assemble-diagonal`)         | Mapping  |
    |------------------------------------------|------------------------------------------|----------|
    | `assemble_diagonal :: LinOp[N,N] -> Ten[N]` | `assemble_diagonal :: (A: LinOp[N,N]) -> Ten[N]` | Identity. Same signature shape; the tuple-vs-positional `A` presentation is notational only. |
    | `assemble_diagonal A = diag(A)`          | `assemble_diagonal(A) = diag(A)`         | Identity. Same operator-to-data extraction; `result[i] = Aᵢᵢ`. |
    | square `M = N` precondition              | square `M = N` precondition              | Identity. Same intrinsic-square contract; same enforcement sites (transitive through L1). |
    | opaque `LinearOperator` (representation absorbed) | opaque `LinearOperator` (representation absorbed) | Identity. Same variant-absorption over the representation axis. |
    | six algebraic laws + four non-laws       | six algebraic laws + four non-laws       | Identity. Inherited unchanged (operator-scaling / sum linearity, identity, zero, diagonal round-trip, complex real/imag split + the four non-laws). |

There is **no L2 binding without an L1 partner and no L1 binding without an L2 partner**; the mapping
is total and bijective on the leaf. This is the identity-in-form property.

**The one note (degenerate-fusion deferral).** The L2 layer's defining work is kernel-fusion
de-fusion. For `assemble_diagonal` there is **no fold-parent and no multi-operation kernel-fusion at
the operator-to-data boundary** — the L0 representation-specific diagonal-extraction mechanics (the
sparse-CSR `hypre_CSRMatrixExtractDiagonal` read, `palace/linalg/hypre.cpp:88`; the matrix-free
`CeedOperatorLinearAssembleAddDiagonal` element-local accumulation, `palace/fem/libceed/operator.cpp:139`;
the AMR `|P|ᵀ dₗ` absolute-value-prolongation assembly, `palace/linalg/rap.cpp:174`; the complex
real/imag split, `palace/linalg/operator.cpp:85-96` / `palace/linalg/rap.cpp:467-479`) are
representation-axis-absorbed and surface only at the L1>L0 lowering. So this theme's edge is the
identity, and the representation-selection / zero-init / element-accumulation-order concerns are read
off the L1>L0 [`assemble-diagonal-mutation-rotation`](../L1-L0/assemble-diagonal-mutation-rotation.md)
theme, not re-derived here.

**The load-bearing non-law preserved through the edge (NOT erased).** The matrix-free
high-order-Nedelec (H(curl)) **approximate-diagonal** non-law is carried across this edge unchanged:
a sparse-matrix realization of `A` reads the **exact** stored diagonal, while a matrix-free
high-order-Nedelec realization of the *same* mathematical operator produces an **approximate**
diagonal (face dofs shared across elements in 3D make the element-local summation differ from the
true assembled diagonal). Load-bearing per the CLAUDE.md taxonomy — the representation can change the
diagonal *value*, not merely its bit pattern. Both the L2 floor (§"Algebraic laws", non-law) and the
L1 leaf (§"Algebraic laws", "Exactness across representations") record it as an explicit
positively-anchored non-law; **this rotation does NOT erase it** (the L2 fusion rotation being
degenerate, there is no de-fusion step in which it could be lost). It is sourced from the Palace AMR
convergent-diagonal note (`palace/linalg/rap.cpp:163-164`), the matrix-free element-accumulation site
(`palace/fem/libceed/operator.cpp:139`), and test-witnessed (`test/unit/test-libceed.cpp:367-376`,
relaxing `rtol` to `1.0` for the high-order 3D Nedelec non-tensor-basis case). The concretization of
where the approximation arises (the matrix-free element-accumulation order) lands at the L1>L0
lowering; the non-law is preserved by reference through this edge.

## Applicability conditions

The identity rewrite is valid when:

1. **The L2 `assemble_diagonal` is the floor realization** (`book/src/L2/assemble-diagonal.md`, the
   standalone operator-to-data floor) — value-thread-isomorphic to the L1 leaf. Confirmed by
   construction: `L2/assemble-diagonal` is authored as a thin floor entry whose laws are inherited
   unchanged from `L1/assemble-diagonal` (wave-1 D4 §"Algebraic laws", §Signature).

2. **The leaf is value-thread-isomorphic across the edge.** The L2 `assemble_diagonal` floor and the
   L1 `assemble_diagonal` leaf share the signature, the operator-to-data extraction semantics, the
   intrinsic-square `M = N` precondition, the variant-absorption over the representation axis, and the
   six laws + four non-laws. Confirmed by construction (the L2 floor is a thin identity-in-form entry).

3. **All de-fusion content is the L1>L0 lowering's, and the fusion is degenerate.** There is no
   fold-parent and no multi-operation kernel-fusion at the operator-to-data boundary; the
   representation-specific diagonal-extraction mechanics are L0 concerns absorbed into the
   representation axis and deferred to the L1>L0 lowering (wave-1 D4 §"Fusion note": fusion is
   degenerate, no leaf-unique fusion surplus). The load-bearing approximate-diagonal non-law is
   carried across the edge unchanged, NOT erased.

This theme does **not** depend on any fold-design adjudication. Unlike the cycle-041
`dot-leaf-identity` / `scal-fold-specialization` edges — which presuppose the wave-1 (b) leaf-floor
reading of a *fold-parent*'s surface and re-anchor under the (a) fold-only reading (OQ
`dot-l2-leaf-floor-vs-fold-only-design`) — `assemble_diagonal` has **no fold-parent**, so there is no
fold-only reading to collapse into. The floor is standalone regardless of how the batch-12 meta-phase
adjudicates the BLAS-1 fork; this edge is unaffected by that fork (recorded in §Open-questions of the
authoring report).

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: the L2 `assemble_diagonal` floor's signature shape (`LinearOperator[N, N]
-> Tensor[N]`) is identical to the L1 leaf's signature shape — a whole-operator-to-data extraction
with no element loop exposed at either layer. The rotation between two value-thread-isomorphic leaves
with identical signatures is the identity by construction; the only L2-layer work (kernel-fusion
de-fusion) is **degenerate** for `assemble_diagonal` (no multi-operation fusion at the operator-to-data
boundary; no fold-parent), leaving the leaf's own edge a no-op with a single deferring note.

**Empirical-match (secondary)**: the L1 leaf is firm on direct Palace evidence
(`L1/assemble-diagonal` §Evidence, including the value-asserting diagonal-assembly test
`test/unit/test-libceed.cpp:343-376`, which reproduces the assembled-matrix diagonal to
`rtol = 1.0e-12` in general), and the L2 floor was authored as value-thread-isomorphic to it; the two
forms agree on every law and every variant axis by independent transcription. The identity is
observational on the two existing firm/firming chapters, not derivational.

## Speculative L1 operators

**None.** Both endpoints are existing vocabulary: the L2 LHS is the `assemble_diagonal` floor
(firming cycle-042 wave-1 D4), the L1 RHS is the firm `assemble_diagonal` leaf. This theme is the
identity edge between existing chapters; it proposes no new operators.

One evidentiary caveat carries over unchanged from the leaves (NOT a status reduction on the theme —
the identity structure is firm):

- **The matrix-free high-order-Nedelec approximate diagonal is a load-bearing non-law, not an
  unresolved gap.** It is exhaustively cited at the L1 home and test-witnessed; the identity edge maps
  it identity-in-form (preserved, not erased). No dedicated unit test calls the bare
  `assemble_diagonal` primitive in isolation (the libCEED diagonal-assembly test exercises it through
  the libCEED operator's `AssembleDiagonal`; the smoother sites exercise it through `SetOperator`);
  consistent with the `firm`-on-syntactic-identity-laws verdict (the missing test does not gate
  operator-algebra laws). The identity edge is unaffected either way.

## Verified-against

L2 / L1 anchors (the two endpoints):

- `book/src/L2/assemble-diagonal.md` (firming cycle-042 wave-1 D4) — the L2 floor (LHS): the
  standalone operator-to-data diagonal-extraction floor, value-thread-isomorphic to the L1 leaf, laws
  + non-laws inherited unchanged, fusion degenerate. (The chapter lands at this cycle's integration
  alongside this theme — wave-2 serial sequencing applies D4 before this theme.)
- `book/src/L1/assemble-diagonal.md` (firm) — the L1 leaf (RHS): the signature (`:15-18`), the
  intrinsic-square `M = N` precondition (`:25`), the six algebraic laws (`:47-52`), the four non-laws
  including the load-bearing exact-vs-approximate caveat (`:54-59`), the variant axes (one orthogonal
  element-type + one absorbed operator-representation, `:75-89`), the complete L0 evidence list
  (`:100-119`). Authoritative on every Palace-surface fact.
- `book/src/L2-L1/dot-leaf-identity.md` (firm cycle-041) — the `-leaf-identity` slug + thin-identity
  structure precedent. (`dot` is leaf-of a fold and defers fusion to the fold-parent; this entry is
  fork-independent with degenerate fusion — the differences are noted in §Context / §"The rewrite".)

L0 evidence (transitive through the firm L1 leaf; self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation; paths relative to `reference/palace/`):

- `palace/linalg/hypre.cpp:88` — `HypreCSRMatrix::AssembleDiagonal`'s `hypre_CSRMatrixExtractDiagonal`
  (the **exact** sparse-CSR stored-diagonal read). **Self-verified (anchor
  `hypre_CSRMatrixExtractDiagonal` @88).** Representation-specific mechanic deferred to L1>L0.
- `palace/fem/libceed/operator.cpp:139` — `CeedOperatorLinearAssembleAddDiagonal` (the matrix-free
  element-local accumulation; the source of the high-order-Nedelec approximation). **Self-verified
  (anchor `CeedOperatorLinearAssembleAddDiagonal` @139).**
- `palace/linalg/rap.cpp:163-164` — the AMR `|P|ᵀ dₗ` convergent-diagonal note (the documented source
  of the approximate-diagonal caveat). **Self-verified (anchor `convergent` @163).**
- `test/unit/test-libceed.cpp:367-376` — the diagonal-assembly test relaxing `rtol` to `1.0` for
  high-order 3D Nedelec non-tensor-basis spaces (the test-witnessed load-bearing approximation).
  **Self-verified (anchor `rtol` @371,375).** L0-equivalent semantic documentation per CLAUDE.md
  §"Tests as semantic supplement". Inherited transitively; the leaf's edge is identity so no new L0
  claim is made here — the non-law is preserved by reference.

## Status

`firm` — the L2 LHS is the firm-this-cycle floor (D4 wave-1), the L1 RHS is the firm
`assemble_diagonal` leaf, and the rotation between two value-thread-isomorphic leaves with identical
signatures is the identity by construction (§"The rewrite (L2 → L1)" table is total and bijective on
the leaf). The only L2-layer work — kernel-fusion de-fusion — is **degenerate** for
`assemble_diagonal` (no fold-parent, no multi-operation fusion at the operator-to-data boundary; the
representation-specific diagonal-extraction mechanics are absorbed into the representation axis and
deferred to the L1>L0 lowering). The load-bearing matrix-free high-order-Nedelec approximate-diagonal
non-law is **preserved through the edge unchanged** (positively anchored — `rap.cpp:163-164` +
test-witnessed `test-libceed.cpp:367-376`), NOT erased. No speculative operator, no negative-anchor
reconstruction, no literature inference — so `firm`, not `partly-constructive`.

> **Fork-independence note (not a status reduction).** Unlike the cycle-041 `dot-leaf-identity` /
> `scal-fold-specialization` floor-edges, this theme does **not** presuppose any fold-design reading:
> `assemble_diagonal` is fork-independent (NO fold-parent — the operator-to-data sibling of
> `apply_linop`, not a fold leaf). It is therefore **unaffected** by the batch-12 meta-phase
> adjudication of the BLAS-1 design fork `dot-l2-leaf-floor-vs-fold-only-design` (the (a) fold-only
> reading has nothing to re-anchor this edge to). The floor stays standalone regardless. Surfaced so
> the meta-phase does not sweep this edge into the fork.
```

```new:book/src/L3-L2/assemble-diagonal-body-identity.md
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
```

```edit:book/src/L2-L1/index.md
| [nrm2-fold-specialization](./nrm2-fold-specialization.md) | `L2/nrm2` (firm cycle-041) | `L1/nrm2` (firm cycle-003; single leaf — no L1 family to dispatch) | firm *(structural; thin-identity — BLAS-1-leaf consumer sibling of `inner-product-fold-specialization`; `nrm2` = `√ ∘ abs ∘ inner_product` CONSUMER at `y=x`, NOT a fold member; no dispatch / no decomposition / no destination buffer; `√`/`abs` scalar post-steps drop below L1 resolution + `std::abs` guard preserved-as-claim at L2 → absorbed-by-non-negativity-claim at L1)* |
| [assemble-diagonal-leaf-identity](./assemble-diagonal-leaf-identity.md) | `L2/assemble-diagonal` (firm cycle-042 D4 floor) | `L1/assemble-diagonal` (firm leaf) | firm *(structural; identity-in-form on the operator-to-data leaf — value-thread-isomorphic signature; **fork-INDEPENDENT, NO fold-parent** — the operator-to-data sibling of `apply_linop`, not a fold leaf, so unaffected by the `dot-l2-leaf-floor-vs-fold-only-design` fork; L2 fusion is **degenerate** (no multi-operation kernel-fusion at the operator-to-data boundary; representation-specific diagonal-extraction mechanics absorbed into the representation axis, deferred to L1>L0); **load-bearing matrix-free high-order-Nedelec approximate-diagonal non-law preserved through the edge, NOT erased** — `rap.cpp:163-164` + test-witnessed `test-libceed.cpp:367-376`)* |
```

```edit:book/src/L3-L2/index.md
| [`scal-body-identity`](./scal-body-identity.md) | L3 [`scal`](../L3/scal.md) §Signature — the whole-tensor field operation `scal :: Scalar -> Tensor[N] -> Tensor[N]`; leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`scal`](../L2/scal.md) §Signature — the base scalar-vector-multiply floor leaf (arity-1 member of `linear_combination`, cited NOT merged); identical signature. | `structural` (whole-tensor signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 condition specialized to the standalone leaf) + secondary `empirical-match` (firm cross-layer identity-in-form audit + `krylov-step-body-identity:97` L3-native classification) | `firm` (cycle-041 D6 abstractor; identity-in-form on the body, **no wrapper to rotate** — the leaf-primitive counterpart of `krylov-step-body-identity`) |
| [`assemble-diagonal-body-identity`](./assemble-diagonal-body-identity.md) | L3 [`assemble-diagonal`](../L3/assemble-diagonal.md) §Signature — the whole-operator operator-to-data field operation `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]`; leaf field operation, **no iteration view, no sequential obstruction** (per-row read of `(i,i)` entries, embarrassingly parallel). | L2 [`assemble-diagonal`](../L2/assemble-diagonal.md) §Signature — the standalone operator-to-data floor (the operator-to-data sibling of `apply_linop`, **NO fold-parent**); identical signature; fusion **degenerate**. | `structural` (whole-operator signature, no element loop, no iteration view, no sequential obstruction — the L3-native-by-signature property of `krylov-step-body-identity.md:97` satisfied by the operator-to-data sibling of `apply_linop`, not a BLAS-1 member; **no wrapper and no fold-parent** to rotate) + secondary `empirical-match` (L3 firm cycle-037 + L2 floor cycle-042 D4 independently value-thread-isomorphic to the firm L1 leaf) | `firm` (cycle-042 wave-2 D7 abstractor; identity-in-form on the body — fork-independent operator-to-data analogue of `dot-body-identity`; **load-bearing matrix-free approximate-diagonal non-law preserved through the edge, NOT erased**) |
```

```edit:book/src/SUMMARY.md
- [nrm2-fold-specialization](./L2-L1/nrm2-fold-specialization.md)
- [assemble-diagonal-leaf-identity](./L2-L1/assemble-diagonal-leaf-identity.md)
```

```edit:book/src/SUMMARY.md
- [scal-body-identity](./L3-L2/scal-body-identity.md)
- [assemble-diagonal-body-identity](./L3-L2/assemble-diagonal-body-identity.md)
```

## Speculative operators proposed

**None.** Both themes are identity edges between **existing** vocabulary:

- **L2>L1 edge** (`assemble-diagonal-leaf-identity`): LHS = the `assemble_diagonal` L2 floor (firming
  cycle-042 wave-1 D4), RHS = the firm L1 `assemble_diagonal` leaf. No new L1 operator proposed.
- **L3>L2 edge** (`assemble-diagonal-body-identity`): LHS = the firm L3 `assemble_diagonal` field
  operation (cycle-037), RHS = the `assemble_diagonal` L2 floor (firming cycle-042 wave-1 D4). No new
  L2 operator proposed.

Both endpoints are firm or firming-this-cycle; the abstractor's speculative-operator channel is empty
for both edges (consistent with the cycle-041 `dot-leaf-identity` / `dot-body-identity` precedents,
which likewise proposed no operators).

## Supporting evidence

L2 form source of truth: the wave-1 D4 harvester report
`reports/2026-06-01T063231Z-cycle-042-harvester-L2-assemble-diagonal/CYCLE.md` (proposed
`book/src/L2/assemble-diagonal.md` body — co-lands this cycle; wave-2 serial sequencing applies D4
before these two themes).

Endpoint chapters:

- `book/src/L1/assemble-diagonal.md` (firm) — the L1 RHS of the L2>L1 edge; authoritative on the
  Palace surface, the six laws, the four non-laws (incl. the load-bearing exact-vs-approximate caveat),
  the variant axes, the complete L0 evidence list.
- `book/src/L3/assemble-diagonal.md` (firm cycle-037) — the L3 LHS of the L3>L2 edge; the
  iteration-rotation rendering with no sequential obstruction, identity-in-form to L1.
- `book/src/L2-L1/dot-leaf-identity.md` + `book/src/L3-L2/dot-body-identity.md` (firm cycle-041) — the
  `-leaf-identity` / `-body-identity` slug + thin-identity-structure precedents.

L0 anchors (all self-verified via `tools/citecheck/citecheck.py --anchor` this invocation; paths
relative to `reference/palace/`):

- `palace/linalg/hypre.cpp:88` (`hypre_CSRMatrixExtractDiagonal`) — exact sparse-CSR read.
- `palace/fem/libceed/operator.cpp:139` (`CeedOperatorLinearAssembleAddDiagonal`) — matrix-free
  element-local accumulation (approximation source).
- `palace/linalg/rap.cpp:163-164` (`convergent` note) — AMR convergent-diagonal caveat source.
- `test/unit/test-libceed.cpp:367-376` (`rtol` @371,375) — test-witnessed load-bearing approximation.

## Open questions / caveats

- **Fork-independence (NOT under the `dot-l2-leaf-floor-vs-fold-only-design` fork).** Both themes are
  **fork-independent**: `assemble_diagonal` has NO fold-parent (it is the operator-to-data sibling of
  `apply_linop`, not a fold leaf). Unlike the cycle-041 `dot`/`scal` floor-edges, neither of these
  edges presupposes the wave-1 (b) leaf-floor design reading, and neither re-anchors under the (a)
  fold-only reading — the (a) reading has no fold-parent to collapse `assemble_diagonal` into. The
  batch-12 meta-phase should **not** sweep these two edges into the BLAS-1 fork adjudication. Surfaced
  (and recorded as a §Status fork-independence note in both theme bodies) so the fork's resolution does
  not accidentally touch these standalone-floor edges.

- **Load-bearing non-law preservation (satisfied; flagged for the lowering-verifier).** The matrix-free
  high-order-Nedelec approximate-diagonal non-law is preserved by reference through BOTH theme edges
  (degenerate fusion ⇒ no de-fusion step in which it could be lost). A future lowering-verifier audit
  of either theme should confirm the non-law text + its positive anchors (`rap.cpp:163-164` +
  `test-libceed.cpp:367-376`) survive intact across the rotation — they do as authored; this is the
  load-bearing invariant the dispatch was charged to protect.

- **Downstream-consistency touch on the L3 entry (lifter/repairer domain, NOT edited here per
  dispatch-phase write discipline).** `book/src/L3/assemble-diagonal.md` §"Lowers to" (`:128-134`) and
  §"Downward" (`:28`) currently record the L3>L1 lowering as **identity-in-form with no interposed L2
  entry and no `L3-L2` theme file** (the cycle-037 state, when no L2 `assemble_diagonal` chapter
  existed). With the L2 floor (D4) and this L3>L2 `assemble-diagonal-body-identity` theme now present,
  those passages are stale — the L3 form now lowers to an **adjacent** L2 parent via this theme, not
  non-adjacently to L1. A future lifter/repairer pass on the L3 entry should update §"Lowers to" /
  §"Downward" to cite the now-present adjacent L3>L2 edge (mirroring how the cycle-041 `dot` L3 entry's
  §"Lowers to" was flagged for the same touch by `dot-body-identity`). Filed as a caveat, not a
  proposed-change (one operator/theme per invocation; the L3 entry is out of this dispatch's scope —
  same handling as the `dot-body-identity` precedent).

- **Count-ownership deferred to D11.** Per the dispatch instruction, I appended ONLY my two theme rows
  (one to each index's theme-list table) + two SUMMARY registrations + the two theme bodies. I did NOT
  touch the consolidated theme-count tallies in either index's §"Vocabulary cohort" / §"Working Notes"
  (the L2>L1 "firm 7 → 10" running count, the L3>L2 "firm 2 → 5" / "5-of-18 coverage-gap" count). D11
  owns those tallies and will fold these two new firm rows into the consolidated counts (L2>L1 firm
  → +1; L3>L2 firm → +1, coverage-gap → +1-of-18). Flagged so D11 / integrator knows the count update
  is intentionally absent from this dispatch.

- **`l2-floor-under-l3-blas1-cohort` directive scope (inherited from the D4 harvester OQ; for the
  batch-12 meta-phase).** The 2026-05-31 foundation-first directive is named for the BLAS-1 cohort, but
  the D4 harvester (and transitively these two edges) extends it to the operator-to-data primitive
  `assemble_diagonal` (not BLAS-1). The extension is natural (same "firm L3 leaf should rest on an
  adjacent same-named L2 parent" rationale, same identity-in-form floor shape), but the directive name
  no longer matches its scope. The batch-12 meta-phase may wish to rename it cohort-neutrally (e.g.
  `l2-floor-under-l3-leaf-cohort`). Surfaced for normalization, not blocking (echoes the D4 harvester's
  same OQ).

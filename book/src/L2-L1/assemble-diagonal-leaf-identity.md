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
`dot-leaf-identity` / `scal-leaf-identity` edges — which presuppose the wave-1 (b) leaf-floor
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
> `scal-leaf-identity` floor-edges, this theme does **not** presuppose any fold-design reading:
> `assemble_diagonal` is fork-independent (NO fold-parent — the operator-to-data sibling of
> `apply_linop`, not a fold leaf). It is therefore **unaffected** by the batch-12 meta-phase
> adjudication of the BLAS-1 design fork `dot-l2-leaf-floor-vs-fold-only-design` (the (a) fold-only
> reading has nothing to re-anchor this edge to). The floor stays standalone regardless. Surfaced so
> the meta-phase does not sweep this edge into the fork.

---
agent: lifter
invoked_at: 2026-06-01T195100Z
scope: L3>L2 + L2>L1 degenerate-theme DEMOTE-to-inline — assemble-diagonal
status: integrated
integrated_at: 2026-06-01T222000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: APPLIED clean (cycle-050 D3, CLEAN non-fold demotion). DELETED assemble-diagonal-body-identity (L3>L2) + assemble-diagonal-leaf-identity (L2>L1); folded the load-bearing matrix-free high-order-Nedelec approximate-diagonal non-law verbatim into in-line §"Downward to L2"/§"Downward to L1" notes on L3/L2 assemble-diagonal; SUMMARY rows + dangling index rows removed. NO operator-chapter deletion (standalone, no fold-parent). 1 OQ promoted (d7-count-reconciliation, RESOLVED by D7). Build-relevant yes. refactor-pass ENACTMENT under the 2026-06-01 VOCABULARY-SHIFT REDIRECT.
inputs:
  - book/src/L3-L2/assemble-diagonal-body-identity.md (DELETE)
  - book/src/L2-L1/assemble-diagonal-leaf-identity.md (DELETE)
  - book/src/L3/assemble-diagonal.md (in-line home — §"Downward to L2" note)
  - book/src/L2/assemble-diagonal.md (in-line home — §"Downward to L1" note)
  - book/src/SUMMARY.md (remove two theme lines)
  - book/src/L3-L2/index.md (remove dangling live-link table row — line 21)
  - book/src/L2-L1/index.md (remove dangling live-link table row — line 22)
  - book/src/L3/reciprocal.md (re-anchor plain-text precedent mention)
  # NOTE (repairer cycle-050): book/src/L2-L1/normalize-leaf-identity.md re-anchor (was edit #6b) DROPPED —
  # sibling D6 (demote-normalize) DELETES that whole file this same cycle, so the inbound mention is moot.
  - reports/2026-06-01T190900Z-cross-layer-cross-cutter-refactor-pass-degenerate-lowering-audit/CYCLE.md (the D3 worklist)
---

# CYCLE: Demote `assemble-diagonal` degenerate theme pair to in-line notes

## Summary

Per the cycle-049 D3 degenerate-lowering-audit worklist, the two themes
`L3-L2/assemble-diagonal-body-identity.md` and `L2-L1/assemble-diagonal-leaf-identity.md`
are degenerate identity-in-named-terms lowerings (the §1d smell under the 2026-06-01
VOCABULARY-SHIFT REDIRECT): both rotate `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]`
to itself with **no vocabulary shift** (same signature, same six laws, same four non-laws, same
variant profile, "total and bijective on the body" — their own §"The rewrite" tables). The vocabulary
failed to shift, so per the redirect the lowering becomes an **in-line note, NOT a mirrored entry +
thin theme**. `assemble_diagonal` is a standalone operator-to-data extraction leaf with **NO fold
parent** (the operator-to-data sibling of `apply_linop`), so its L3 and L2 operator entries are NOT
slated for fold-collapse — the demotion lands clean on a standalone entry, touching no held chapter.

This dispatch (a) **deletes** both theme files; (b) adds a §"Downward to L2" note on
`L3/assemble-diagonal.md` and a §"Downward to L1" note on `L2/assemble-diagonal.md` capturing the
deleted themes' content — operator-to-data extraction leaf, identity-in-form across the edge, no
fold-parent, degenerate L2 fusion — and **preserving the one load-bearing fact the themes carried:
the matrix-free high-order-Nedelec approximate-diagonal non-law** (`rap.cpp:163-164` +
test-witnessed `test-libceed.cpp:367-376`); (c) removes the two `SUMMARY.md` lines; (d) removes the
two **dangling live-link** index table rows that would otherwise break `linkcheck2`
(`L3-L2/index.md:21`, `L2-L1/index.md:22`); (e) re-anchors the surviving plain-text inbound slug
mention (`L3/reciprocal.md:150`) off the deleted slug. (A second inbound mention at
`L2-L1/normalize-leaf-identity.md:47` is NOT re-anchored — the sibling D6 dispatch deletes that whole
file this same cycle, so the reference is moot; the re-anchor that was edit #6b is dropped.) All
**consolidated index tallies / cohort-growth counts / prose-bullet cohort lists are DEFERRED to D7**
(the wave-2 count-owner) per the dispatch directive.

## Proposed changes

### 1. Delete the two degenerate theme files

```delete:book/src/L3-L2/assemble-diagonal-body-identity.md
```

```delete:book/src/L2-L1/assemble-diagonal-leaf-identity.md
```

### 2. In-line note on the L3 entry (§"Downward to L2"); re-anchor deleted-slug mentions

The L3 entry's frontmatter `lowers_to` and §"Downward" / §"Lowers to" prose name the now-deleted
`assemble-diagonal-body-identity` L3>L2 theme. Re-anchor each mention to the in-line annotation and
add a focused §"Downward to L2" note capturing the deleted theme's content (operator-to-data leaf,
identity-in-form, no fold-parent, degenerate fusion) with the load-bearing non-law preserved.

```edit:book/src/L3/assemble-diagonal.md
[old]: lowers_to:
  - book/src/L2/assemble-diagonal.md (identity-in-form on the primitive's signature; lowers through the present adjacent L2 floor via the `assemble-diagonal-body-identity` L3>L2 theme — see Lowers-to)
[new]: lowers_to:
  - book/src/L2/assemble-diagonal.md (identity-in-form on the primitive's signature; the L3>L2 edge is a degenerate identity-in-named-terms lowering recorded as an in-line note here — see Lowers-to — not a dedicated theme, per the 2026-06-01 vocabulary-shift redirect)
```

```edit:book/src/L3/assemble-diagonal.md
[old]: - **Downward** to L2/L1: `assemble_diagonal` lowers to the **present adjacent L2 floor** [`assemble-diagonal`](../L2/assemble-diagonal.md) (cycle-042) via the `assemble-diagonal-body-identity` L3>L2 theme, and onward to L1 [`assemble-diagonal`](../L1/assemble-diagonal.md). The rotation is **identity-in-form on the primitive's signature** — L1, L2, and L3 all see `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same non-law set (including the load-bearing exact-vs-approximate caveat), and the same variant-axis profile (one orthogonal element-type axis + one absorbed operator-representation axis). The L2 floor is the standalone (fork-independent) operator-to-data sibling of `apply_linop`; the L3>L2 hop passes through the adjacent floor, mirroring the `apply_linop` floor discipline. The L3>L2 identity-in-form annotation is captured by the adjacent-edge theme per the cycle-012 per-adjacent-edge lowering-directory convention (precedent: `apply_linop`, `dot`, `scal`, `krylov-step`); the transitive L3>L1 identity remains in-line, with no non-adjacent `L3-L1/` lowering directory created.
[new]: - **Downward** to L2/L1: `assemble_diagonal` lowers to the **present adjacent L2 floor** [`assemble-diagonal`](../L2/assemble-diagonal.md) (cycle-042) as **identity-in-form on the primitive's signature**, recorded as the in-line §"Downward to L2" note below (NOT a dedicated L3>L2 theme — the edge is a degenerate identity-in-named-terms lowering demoted to an in-line note per the 2026-06-01 vocabulary-shift redirect), and onward to L1 [`assemble-diagonal`](../L1/assemble-diagonal.md). The rotation is **identity-in-form on the primitive's signature** — L1, L2, and L3 all see `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same non-law set (including the load-bearing exact-vs-approximate caveat), and the same variant-axis profile (one orthogonal element-type axis + one absorbed operator-representation axis). The L2 floor is the standalone (fork-independent) operator-to-data sibling of `apply_linop`. The transitive L3>L1 identity remains in-line, with no non-adjacent `L3-L1/` lowering directory created.
```

Add the dedicated §"Downward to L2" in-line note immediately after the §"Lowers to" section's
opening paragraph. Re-anchor the two `assemble-diagonal-body-identity` mentions in §"Lowers to":

```edit:book/src/L3/assemble-diagonal.md
[old]: L3 `assemble_diagonal` lowers to the **present adjacent L2 floor** [`assemble-diagonal`](../L2/assemble-diagonal.md) (cycle-042) as **identity-in-form on the primitive's signature**, via the `assemble-diagonal-body-identity` L3>L2 theme, and onward to L1 [`assemble-diagonal`](../L1/assemble-diagonal.md). L1, L2, and L3 all see `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same non-law set (including the load-bearing exact-vs-approximate caveat), and the same variant-axis profile (one orthogonal + one absorbed). The L2 floor is the standalone (fork-independent) operator-to-data sibling of `apply_linop` — landed by the cycle-042 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort` — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.
[new]: L3 `assemble_diagonal` lowers to the **present adjacent L2 floor** [`assemble-diagonal`](../L2/assemble-diagonal.md) (cycle-042) as **identity-in-form on the primitive's signature**, recorded by the in-line §"Downward to L2 (in-line note)" below, and onward to L1 [`assemble-diagonal`](../L1/assemble-diagonal.md). L1, L2, and L3 all see `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same non-law set (including the load-bearing exact-vs-approximate caveat), and the same variant-axis profile (one orthogonal + one absorbed). The L2 floor is the standalone (fork-independent) operator-to-data sibling of `apply_linop` — landed by the cycle-042 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort` — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

### Downward to L2 (in-line note)

The L3>L2 edge is a **degenerate identity-in-named-terms lowering** — the L3 whole-operator field
operation `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]` and the L2 floor are
value-thread-isomorphic on the body: same signature, same `assemble_diagonal A = diag(A)`
extraction (`result[i] = Aᵢᵢ`), same intrinsic-square `M = N` precondition, same opaque-`LinearOperator`
representation-axis absorption, same six laws + four non-laws. The vocabulary does not shift across
the edge, so per the 2026-06-01 vocabulary-shift redirect this is recorded **as this in-line note,
NOT as a dedicated L3>L2 theme** (the former `assemble-diagonal-body-identity.md` theme, demoted
cycle-050). There is **no wrapper** (it is a leaf field operation, not a kernel body inside an
`IterState`/outer-driver wrapper) and **no fold-parent** (it is the operator-to-data sibling of
`apply_linop`, belonging to no fold cohort), so there is no surface adjustment and no fold-level
rotation to carry — the edge is the pure identity. `assemble_diagonal` is **L3-native by signature
shape** (the per-row read of the `(i, i)` entries is a single semantic step at both layers; no
element loop is visible, no sequential obstruction — the iteration rotation is already complete at
the signature level), the same property `apply_linop` and the BLAS-1 cohort satisfy.

**Load-bearing non-law preserved through the edge (NOT erased).** The matrix-free
high-order-Nedelec (H(curl)) **approximate-diagonal** non-law carries across this edge unchanged: a
sparse-matrix realization of `A` reads the **exact** stored diagonal, while a matrix-free
high-order-Nedelec realization of the *same* mathematical operator produces an **approximate**
diagonal (face dofs shared across elements in 3D make the element-local summation differ from the
true assembled diagonal). Load-bearing per the CLAUDE.md taxonomy — the representation can change the
diagonal *value*, not merely its bit pattern. Because the L2 fusion content is degenerate there is no
de-fusion step in which the approximation could be lost; the non-law is preserved by reference, NOT
erased. Sourced from the Palace AMR convergent-diagonal note (`palace/linalg/rap.cpp:163-164`),
the matrix-free element-accumulation site (`palace/fem/libceed/operator.cpp:139`), and test-witnessed
(`test/unit/test-libceed.cpp:367-376`, relaxing `rtol` to `1.0` for the high-order 3D Nedelec
non-tensor-basis case) — all transitive through the L1 home. Concretized at the L1>L0
[`assemble-diagonal-mutation-rotation`](../L1-L0/assemble-diagonal-mutation-rotation.md) lowering.
```

```edit:book/src/L3/assemble-diagonal.md
[old]: The L3>L2 identity rotation is captured by the adjacent-edge `assemble-diagonal-body-identity` L3>L2 theme (per the cycle-012 meta-phase per-adjacent-edge lowering-directory convention); the transitive L3>L1 identity (L3>L2 ∘ L2>L1) is annotated in-line, with no `book/src/L3-L1/` directory created. Per the cycle-010 `krylov-step` and cycle-011 BLAS-1 / `apply_linop` precedents this entry captures the in-line identity-rotation discipline for the floor cohort. The substantive rotation in the chain is the L1>L0 [`assemble-diagonal-mutation-rotation`](../L1-L0/assemble-diagonal-mutation-rotation.md) theme — it lowers the L1 pure-functional form into Palace's output-arg-mutating L0 virtual `AssembleDiagonal(diag)` family (the destination sizing `diag.SetSize(height)`, the `diag = 0.0` zero-init, the sparse-CSR `hypre_CSRMatrixExtractDiagonal` read, the matrix-free `CeedOperatorLinearAssembleAddDiagonal` accumulation, the AMR `|P|ᵀ dₗ` absolute-value-prolongation assembly, and the Dirichlet `DiagonalPolicy` BC post-step). The L3>L1 hop is by contrast a layer-coherence rotation (each layer is coherent within itself), not an algebraic one.
[new]: The L3>L2 identity rotation is recorded by the §"Downward to L2 (in-line note)" above (a degenerate identity-in-named-terms edge demoted from a dedicated theme to an in-line note cycle-050 per the 2026-06-01 vocabulary-shift redirect); the transitive L3>L1 identity (L3>L2 ∘ L2>L1) is likewise annotated in-line, with no `book/src/L3-L1/` directory created. The substantive rotation in the chain is the L1>L0 [`assemble-diagonal-mutation-rotation`](../L1-L0/assemble-diagonal-mutation-rotation.md) theme — it lowers the L1 pure-functional form into Palace's output-arg-mutating L0 virtual `AssembleDiagonal(diag)` family (the destination sizing `diag.SetSize(height)`, the `diag = 0.0` zero-init, the sparse-CSR `hypre_CSRMatrixExtractDiagonal` read, the matrix-free `CeedOperatorLinearAssembleAddDiagonal` accumulation, the AMR `|P|ᵀ dₗ` absolute-value-prolongation assembly, and the Dirichlet `DiagonalPolicy` BC post-step). The L3>L1 hop is by contrast a layer-coherence rotation (each layer is coherent within itself), not an algebraic one.
```

### 3. In-line note on the L2 entry (§"Downward to L1"); re-anchor deleted-theme mention

The L2 entry's §Context (line 38) forward-references the now-deleted L2>L1 theme as "the forthcoming
L2>L1 thin-identity theme this cycle's D7 dispatch authors", and the §Signature tail (lines 117-121)
defers to "the L2>L1 lowering theme". Re-anchor both to the in-line note and add a focused
§"Downward to L1" note capturing the deleted theme's content with the load-bearing non-law preserved.

```edit:book/src/L2/assemble-diagonal.md
[old]: `assemble_diagonal` is **defined in L2 vocabulary** here (high→low discipline, CLAUDE.md
§Methodology invariants "Layers are defined high→low"): the signature, semantics, and
algebraic laws are stated at the L2 fusion-rotation resolution. The two adjacent rotations
— how the L2 form lowers to L1 (the forthcoming L2>L1 thin-identity theme this cycle's D7
dispatch authors) and how the L3 form lowers to L2 (the L3>L2 body-identity theme) — are
narrated by the separate lowering themes, not here. This chapter does not define
`assemble_diagonal` in terms of L1 primitives or L0 mechanics.
[new]: `assemble_diagonal` is **defined in L2 vocabulary** here (high→low discipline, CLAUDE.md
§Methodology invariants "Layers are defined high→low"): the signature, semantics, and
algebraic laws are stated at the L2 fusion-rotation resolution. Both adjacent rotations
are **degenerate identity-in-named-terms lowerings** (the vocabulary does not shift across
either edge), so per the 2026-06-01 vocabulary-shift redirect each is recorded as an
**in-line note rather than a dedicated theme**: how the L2 form lowers to L1 is the
§"Downward to L1" note below (demoted from the former `assemble-diagonal-leaf-identity`
L2>L1 theme cycle-050); how the L3 form lowers to L2 is the §"Downward to L2" in-line note
on the L3 [`assemble-diagonal`](../L3/assemble-diagonal.md) entry (demoted from the former
`assemble-diagonal-body-identity` L3>L2 theme cycle-050). This chapter does not define
`assemble_diagonal` in terms of L1 primitives or L0 mechanics.
```

```edit:book/src/L2/assemble-diagonal.md
[old]: The L2 signature is identical in shape to the L1
[`assemble-diagonal`](../L1/assemble-diagonal.md) signature; the rotation L2 → L1 is
identity-in-form on the primitive (the de-fusion the L2 layer un-does lives at the L0
representation's diagonal-extraction *implementation*, recorded by the L2>L1 lowering theme,
not in the signature).
[new]: The L2 signature is identical in shape to the L1
[`assemble-diagonal`](../L1/assemble-diagonal.md) signature; the rotation L2 → L1 is
identity-in-form on the primitive (the de-fusion the L2 layer un-does lives at the L0
representation's diagonal-extraction *implementation*, recorded by the §"Downward to L1"
in-line note below — a degenerate identity-in-named-terms edge, not a dedicated theme — not
in the signature).
```

Add the dedicated §"Downward to L1" in-line note immediately after the §"L2 vs L1 distinction"
section (before §Evidence), so the layer-coherence reader finds the edge in L2 vocabulary:

```edit:book/src/L2/assemble-diagonal.md
[old]: The two layers' entries are value-thread-isomorphic on the primitive itself, sharing
signature, algebraic laws (six), non-laws (four, including the load-bearing exact-vs-approximate
caveat), and variant-axis profile (one orthogonal + one absorbed). The L2 entry exists for
floor presence — so the L3 [`assemble-diagonal`](../L3/assemble-diagonal.md) field operation
has an adjacent L2 parent.
[new]: The two layers' entries are value-thread-isomorphic on the primitive itself, sharing
signature, algebraic laws (six), non-laws (four, including the load-bearing exact-vs-approximate
caveat), and variant-axis profile (one orthogonal + one absorbed). The L2 entry exists for
floor presence — so the L3 [`assemble-diagonal`](../L3/assemble-diagonal.md) field operation
has an adjacent L2 parent.

## Downward to L1 (in-line note)

The L2>L1 edge is a **degenerate identity-in-named-terms lowering** — the L2 floor and the L1
[`assemble-diagonal`](../L1/assemble-diagonal.md) leaf are value-thread-isomorphic on the leaf:
same signature `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]`, same
`assemble_diagonal A = diag(A)` extraction (`result[i] = Aᵢᵢ`), same intrinsic-square `M = N`
precondition, same opaque-`LinearOperator` representation-axis absorption, same six laws + four
non-laws. The vocabulary does not shift across the edge, so per the 2026-06-01 vocabulary-shift
redirect this is recorded **as this in-line note, NOT as a dedicated L2>L1 theme** (the former
`assemble-diagonal-leaf-identity.md` theme, demoted cycle-050).

There is **no fold-parent**: unlike the cycle-041 BLAS-1 floors (`dot` leaf-of `inner_product`,
`scal` member-of `linear_combination`), `assemble_diagonal` is the operator-to-data sibling of
`apply_linop`, belonging to no fold cohort, so there is nothing to defer fusion to. The L2 layer's
defining work — kernel-fusion de-fusion — is **degenerate** here: the operator-to-data boundary
carries no multi-operation kernel-fusion. The L0 "fusion" present in the diagonal-extraction
realizations is the *representation-specific diagonal-extraction mechanic* (the sparse-CSR
`hypre_CSRMatrixExtractDiagonal` read, `palace/linalg/hypre.cpp:88`; the matrix-free
`CeedOperatorLinearAssembleAddDiagonal` element-local accumulation, `palace/fem/libceed/operator.cpp:139`;
the AMR `|P|ᵀ dₗ` absolute-value-prolongation assembly, `palace/linalg/rap.cpp:174`; the complex
real/imag split, `palace/linalg/operator.cpp:85-96` / `palace/linalg/rap.cpp:467-479`) — all
representation-axis-absorbed L0 concerns surfaced by the L1>L0 lowering, not an L2 composition to
de-fuse. So the L2>L1 edge is the identity, with the representation-selection / zero-init /
element-accumulation-order treatment deferred to the L1>L0
[`assemble-diagonal-mutation-rotation`](../L1-L0/assemble-diagonal-mutation-rotation.md) theme.

**Load-bearing non-law preserved through the edge (NOT erased).** The matrix-free
high-order-Nedelec (H(curl)) **approximate-diagonal** non-law carries across this edge unchanged: a
sparse-matrix realization of `A` reads the **exact** stored diagonal, while a matrix-free
high-order-Nedelec realization of the *same* mathematical operator produces an **approximate**
diagonal (face dofs shared across elements in 3D). Load-bearing per the CLAUDE.md taxonomy — the
representation can change the diagonal *value*, not merely its bit pattern. Because the L2 fusion
content is degenerate there is no de-fusion step in which the approximation could be lost; the
non-law is preserved by reference, NOT erased. Sourced from the Palace AMR convergent-diagonal note
(`palace/linalg/rap.cpp:163-164`), the matrix-free element-accumulation site
(`palace/fem/libceed/operator.cpp:139`), the Palace comment naming the matrix-free *approximate*
diagonal at the consumer (`palace/linalg/jacobi.hpp:15-16`), and test-witnessed
(`test/unit/test-libceed.cpp:367-376`, relaxing `rtol` to `1.0` for the high-order 3D Nedelec
non-tensor-basis case) — all transitive through the L1 home.
```

### 4. Remove the two SUMMARY.md lines

```edit:book/src/SUMMARY.md
[old]: - [assemble-diagonal-body-identity](./L3-L2/assemble-diagonal-body-identity.md)
[new]:
```

```edit:book/src/SUMMARY.md
[old]: - [assemble-diagonal-leaf-identity](./L2-L1/assemble-diagonal-leaf-identity.md)
[new]:
```

(Each removal deletes the whole line including its trailing newline; the surrounding SUMMARY entries
are unaffected. Integrator: if the empty-line residue is undesirable, collapse it — the two adjacent
list items remain valid `mdBook` `SUMMARY.md` rows.)

### 5. Remove the two dangling live-link index table rows (build-breakage avoidance only)

Both rows are live-link `[…](./…-identity.md)` table rows that will fail `linkcheck2` once the theme
files are deleted, so they MUST be removed to keep the build green. This is row-level removal only;
the **consolidated tallies, cohort-growth counts, and prose-bullet cohort lists are LEFT for D7** (see
§Discipline notes — these rows are not themselves count lines, but the index's separate count prose
DOES reference them, so D7 must reconcile).

```edit:book/src/L3-L2/index.md
[old]: | [`assemble-diagonal-body-identity`](./assemble-diagonal-body-identity.md) | L3 [`assemble-diagonal`](../L3/assemble-diagonal.md) §Signature — the whole-operator operator-to-data field operation `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]`; leaf field operation, **no iteration view, no sequential obstruction** (per-row read of `(i,i)` entries, embarrassingly parallel). | L2 [`assemble-diagonal`](../L2/assemble-diagonal.md) §Signature — the standalone operator-to-data floor (the operator-to-data sibling of `apply_linop`, **NO fold-parent**); identical signature; fusion **degenerate**. | `structural` (whole-operator signature, no element loop, no iteration view, no sequential obstruction — the L3-native-by-signature property of `krylov-step-body-identity.md:97` satisfied by the operator-to-data sibling of `apply_linop`, not a BLAS-1 member; **no wrapper and no fold-parent** to rotate) + secondary `empirical-match` (L3 firm cycle-037 + L2 floor cycle-042 D4 independently value-thread-isomorphic to the firm L1 leaf) | `firm` (cycle-042 wave-2 D7 abstractor; identity-in-form on the body — fork-independent operator-to-data analogue of `dot-body-identity`; **load-bearing matrix-free approximate-diagonal non-law preserved through the edge, NOT erased**) |
[new]:
```

```edit:book/src/L2-L1/index.md
[old]: | [assemble-diagonal-leaf-identity](./assemble-diagonal-leaf-identity.md) | `L2/assemble-diagonal` (firm cycle-042 D4 floor) | `L1/assemble-diagonal` (firm leaf) | firm *(structural; identity-in-form on the operator-to-data leaf — value-thread-isomorphic signature; **fork-INDEPENDENT, NO fold-parent** — the operator-to-data sibling of `apply_linop`, not a fold leaf, so unaffected by the `dot-l2-leaf-floor-vs-fold-only-design` fork; L2 fusion is **degenerate** (no multi-operation kernel-fusion at the operator-to-data boundary; representation-specific diagonal-extraction mechanics absorbed into the representation axis, deferred to L1>L0); **load-bearing matrix-free high-order-Nedelec approximate-diagonal non-law preserved through the edge, NOT erased** — `rap.cpp:163-164` + test-witnessed `test-libceed.cpp:367-376`)* |
[new]:
```

### 6. Re-anchor the two plain-text inbound slug mentions

Neither is a markdown link (so neither breaks the build), but both name the now-deleted slugs. The
demotion re-anchors them to the in-line notes.

`L3/reciprocal.md:150` cites `assemble-diagonal-body-identity` as the L3>L2 discipline precedent:

```edit:book/src/L3/reciprocal.md
[old]: - `book/src/L3/assemble-diagonal.md` (cycle-037 firm) — the operator-to-data L3 backfill precedent on the same diagonal-preconditioner-apply chain; `reciprocal` is the elementwise step following `assemble_diagonal`. The L3>L2 identity-in-form discipline (through the present adjacent L2 floor via the `assemble-diagonal-body-identity` theme), the adjacent-floor rotation shape, and the firm-on-positive-structure status judgement are inherited from this sibling.
[new]: - `book/src/L3/assemble-diagonal.md` (cycle-037 firm) — the operator-to-data L3 backfill precedent on the same diagonal-preconditioner-apply chain; `reciprocal` is the elementwise step following `assemble_diagonal`. The L3>L2 identity-in-form discipline (through the present adjacent L2 floor, recorded by that entry's in-line §"Downward to L2" note — the degenerate edge was demoted from a dedicated theme to an in-line note cycle-050), the adjacent-floor rotation shape, and the firm-on-positive-structure status judgement are inherited from this sibling.
```

**(Dropped — was edit #6b)** A second plain-text inbound mention of `assemble-diagonal-leaf-identity`
exists at `L2-L1/normalize-leaf-identity.md:47` (a cohort enumeration of cycle-042 standalone-leaf/-gate
edges). This re-anchor is **NOT applied**: the sibling D6 dispatch
(`reports/2026-06-01T195100Z-lifter-demote-normalize/CYCLE.md`, frontmatter line 8 + delete-block
line 48) **DELETES `book/src/L2-L1/normalize-leaf-identity.md` outright this same cycle**, so the
inbound reference is moot regardless of integrator ordering — the whole file is removed, leaving no
dangling reference to the deleted `assemble-diagonal-leaf-identity` slug. (Repairer-dropped per the
critic's cross-dispatch-coordination warning; the build stays green either way.)

## Discipline notes

- **This is a smell-resolution demotion per the 2026-06-01 vocabulary-shift redirect**, not a
  re-architecture. Both deleted themes are degenerate identity-in-named-terms lowerings (their own
  §"The rewrite" tables are "total and bijective on the body", every row mapped `Identity`). The
  vocabulary failed to shift, so the redirect's prescription applies: resolve as an in-line note, NOT
  a mirrored entry + thin theme. The `assemble_diagonal` operator entries themselves stay
  (standalone operator-to-data leaf, NO fold-parent — not slated for fold-collapse), so no held
  chapter is touched and the demotion lands clean.
- **Load-bearing non-law preserved verbatim in both in-line notes.** The matrix-free
  high-order-Nedelec approximate-diagonal non-law is the one load-bearing fact the deleted themes
  carried; both new in-line notes reproduce it explicitly with its full citation set
  (`rap.cpp:163-164` + `operator.cpp:139` + `jacobi.hpp:15-16` + `test-libceed.cpp:367-376`). All four
  L0 citations were **self-verified on-disk this dispatch** via `tools/citecheck/citecheck.py --anchor`
  (all `[ok]`): `rap.cpp:163-164` (anchor `convergent` @163), `test-libceed.cpp:367-376` (anchor
  `rtol` @371,375), `operator.cpp:139` (anchor `CeedOperatorLinearAssembleAddDiagonal` @139),
  `hypre.cpp:88` (anchor `hypre_CSRMatrixExtractDiagonal` @88). These are inherited transitive
  citations through the firm L1 home, not new claims — the edge is identity, so no new L0 claim is
  made; the non-law is preserved by reference.
- **High→low discipline maintained.** The in-line notes are titled "Downward to L2" / "Downward to
  L1" and narrate the rewrite forward (L3→L2, L2→L1), consistent with the layers-defined-high→low
  invariant. No reverse-direction (lift) prose was introduced into the chapter bodies.
- **Index tallies / cohort-growth counts / prose-bullet cohort lists DEFERRED to D7 (the wave-2
  count-owner)** per the dispatch directive. I removed ONLY the two dangling **live-link** table rows
  (`L3-L2/index.md:21`, `L2-L1/index.md:22`) because those would hard-fail `linkcheck2` once the theme
  files are deleted. I did NOT touch:
  - The L3-L2 index cohort-growth/coverage-gap prose (`L3-L2/index.md:66` "firm 15 → 17", `:67`
    "13 of the 17 firm themes" / "4 of the 17") — removing a `-body-identity` theme changes both the
    firm-count (17 → 16) and the thin-identity sub-count (13 → 12) and the coverage-gap denominator
    bookkeeping. **D7 must reconcile.**
  - The L3-L2 index prose bullet (`L3-L2/index.md:49` `assemble-diagonal-body-identity` bullet) — a
    plain-text cohort-list entry, stale but build-safe. **D7 should remove + reconcile the "five
    fork-INDEPENDENT standalone-floor themes" framing at `:47` (now four).**
  - The L2-L1 index prose bullet (`L2-L1/index.md:64` `assemble-diagonal-leaf-identity` bullet) and
    the cohort-growth log (`:78` "10 → 15", "five new same-named L2 floors") — same coupling. **D7
    must reconcile the firm-count and the "five" → "four" cohort framing.**
- **Scope-fenced to assemble-diagonal only.** I deliberately did NOT touch sibling theme references
  that still exist: `reciprocal.md:25,133` mention `reciprocal-body-identity` (a live theme, not in my
  scope); `reciprocal.md` mentions of `assemble-diagonal` as a *precedent operator* (lines 25, 27, 29,
  43, 92, 97, 125, 127, 139, 143, 165) are references to the L3 operator entry (which stays), not to
  the deleted theme — only the one §Evidence bullet at `:150` named the deleted theme slug, and that
  is the only `reciprocal.md` edit. In `normalize-leaf-identity.md` only the `:47` cohort
  enumeration named the deleted slug, but that re-anchor (former edit #6b) is **dropped** because the
  sibling D6 dispatch deletes the whole `normalize-leaf-identity.md` file this same cycle — the
  inbound mention is moot, so no re-anchor is needed.

## Supporting evidence

- The D3 worklist: `reports/2026-06-01T190900Z-cross-layer-cross-cutter-refactor-pass-degenerate-lowering-audit/CYCLE.md`
  (classified both themes DEMOTE-to-inline; noted `assemble-diagonal` has NO fold parent so the
  operator entry is not slated for collapse).
- The two deleted theme files' own §"The rewrite" tables establish the degeneracy (every row
  `Identity`; "total and bijective on the body").
- The in-line homes: `book/src/L3/assemble-diagonal.md` (firm cycle-037) §"Downward"/§"Lowers to"
  already framed the edge as identity-in-form; `book/src/L2/assemble-diagonal.md` (firm cycle-042 D4)
  §"L2 vs L1 distinction"/§"Fusion note" already carried the degenerate-fusion + load-bearing-non-law
  content. The in-line notes consolidate what the deleted themes restated.
- L0 citations self-verified on-disk via `tools/citecheck/citecheck.py --anchor` (all `[ok]`):
  `reference/palace/palace/linalg/rap.cpp:163-164`, `reference/palace/test/unit/test-libceed.cpp:367-376`,
  `reference/palace/palace/fem/libceed/operator.cpp:139`, `reference/palace/palace/linalg/hypre.cpp:88`.

## Open questions / caveats

- **D7 count reconciliation is REQUIRED and is the only cross-dispatch coupling.** Removing the two
  themes drops the L3-L2 firm-theme count by 1 (17 → 16; thin-identity sub-count 13 → 12) and the
  L2-L1 firm-theme count by 1, and converts the cycle-042 "five fork-INDEPENDENT standalone-floor"
  cohort framing to "four" in both index files' prose. I removed the build-breaking live-link rows;
  D7 owns every tally/count/cohort-prose update. If D7's worklist does not already enumerate the
  assemble-diagonal demotion's count impact, surface it: the two index files' cohort-growth logs
  (`L3-L2/index.md:66-67`, `L2-L1/index.md:78`) and the standalone-floor-cohort prose
  (`L3-L2/index.md:47-49`, `L2-L1/index.md:64`) all reference the deleted themes.
- **SUMMARY.md empty-line residue.** My SUMMARY edits replace each theme line with an empty line. If
  the integrator prefers no blank line between the surrounding list items, collapse it at apply time
  — mdBook tolerates the blank line either way (the adjacent `- [...]` rows remain a valid list).
- **No abstractor reread needed.** The demotion is a pure smell-resolution rewrite: the in-line notes
  reproduce the deleted themes' content (signature, identity-in-form, no fold-parent, degenerate
  fusion, load-bearing non-law) without any content decision — the operator entries' existing prose
  already asserted all of it. No signature shifted, no decomposition changed, no new sub-pattern was
  introduced.

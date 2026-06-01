---
agent: lifter
invoked_at: 2026-06-01T210700Z
scope: L3>L2 + L2>L1 theme re-anchor — inner_product/dot family demotion (delete dot-body-identity + dot-leaf-identity; re-express L3/dot through L3/inner_product)
status: integrated
integrated_at: 2026-06-01T22:14:50Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean by integrator-per-report (D2 of cycle-051); finalized cycle-051. dot-{body,leaf}-identity deleted; L3/dot re-expressed through L3/inner_product; 3-way co-edit of KEPT divfree-projector-leaf-identity line 266 (dot- de-link via distinct substring); zero dangling live links to deleted slugs; build exit 0."
inputs:
  - book/src/L3-L2/dot-body-identity.md (DELETE)
  - book/src/L2-L1/dot-leaf-identity.md (DELETE)
  - book/src/L3/dot.md (RE-EXPRESS through L3/inner_product)
  - book/src/L3/inner_product.md (firm combinator home; §"Downward to L2" pre-built — c050)
  - book/src/L2/inner_product.md (firm combinator home; absorption pointers pre-built — c050)
  - book/src/L2-L1/inner-product-fold-specialization.md (KEPT genuine L2>L1 translation)
  - book/src/SUMMARY.md, book/src/L3-L2/index.md, book/src/L2-L1/index.md (D2's own rows)
  - book/src/L3/index.md, book/src/L2/index.md (forward-looking-note de-tense)
  - book/src/L2-L1/divfree-projector-leaf-identity.md (KEPT cross-dispatch file; defensive de-link of inbound live link to deleted dot-leaf-identity — 3-way co-edit with D3/D4, see §(c))
  - book/src/L3-L2/divfree-projector-body-identity.md (DELETED by D4 this cycle; inbound link dies with the file — NO D2 edit, repair-dropped)
---

# CYCLE: Re-anchor inner_product/dot family — demote 2 degenerate themes + re-express L3/dot

## Summary

Cycle-051 D2 enacts the demotion half of the cycle-049/050 `inner_product` replace-and-propagate map for the `dot` sub-family. The firm L3/L2 `inner_product` combinator homes (authored c050) ship pre-built absorption homes — L3/inner_product §"Downward to L2" (lines 363–385) and the L2/inner_product lede note + cycle-049-inversion note (lines 22–29, 472) explicitly name the `dot-body-identity` / `dot-leaf-identity` themes as "the pre-built home [they] demote into at cycle-051." This dispatch: **(a)** deletes the two degenerate identity-in-named-terms theme files `book/src/L3-L2/dot-body-identity.md` (L3>L2) and `book/src/L2-L1/dot-leaf-identity.md` (L2>L1) — their identity-in-form content is already absorbed in the pre-built homes, no new substance added; **(b)** re-expresses `book/src/L3/dot.md` to speak *through* the L3 `inner_product` combinator (`dot` = the Hermitian/symmetric specialization at `M = I`; `tdot` = the unconjugated bilinear specialization), routing the substantive conjugation/weight translation to the KEPT `L2-L1/inner-product-fold-specialization` theme and dropping the L1/L0 base-form re-derivation framing + the dead `dot-body-identity` reference; **(c)/(d)** removes D2's own SUMMARY.md lines + L3-L2/L2-L1 dep-map rows, de-tenses the two forward-looking combinator-home notes, and defensively de-links the inbound live link from the KEPT cross-dispatch `divfree-projector-leaf-identity` file (its sibling `divfree-projector-body-identity` is deleted by D4 this cycle — its inbound link dies with the file, no D2 edit). The consolidated firm-theme TALLY is DEFERRED to D5 per dispatch instruction. No L_n operator is modified beyond the in-scope re-expression of `L3/dot`; the re-expression is a structural rewrite (combinator routing), no new content decisions.

## Proposed changes

### (a) DELETE the two degenerate theme files

```delete:book/src/L3-L2/dot-body-identity.md
```

```delete:book/src/L2-L1/dot-leaf-identity.md
```

Rationale: both are degenerate identity-in-named-terms `-body-identity` / `-leaf-identity` themes (the §1d "vocabulary-failed-to-shift" smell named by `METHODOLOGY-REDIRECT.md`). Their entire content is "the `dot` leaf is value-thread-isomorphic across the edge; the genuine fusion translation is the fold-parent's." That identity-in-form fact is already stated in the pre-built combinator homes:
- L3>L2 identity-in-form: `book/src/L3/inner_product.md` §"Downward to L2" (lines 363–385) — names the body identity-in-form, the no-L3-L2-theme convention, and the demotion provenance.
- L2>L1 genuine translation: the KEPT `book/src/L2-L1/inner-product-fold-specialization.md` (the conjugation/element-type/weight dispatch + `xᴴ y` ↔ `yᴴ x` re-order + pinned reduction tree) — already the substantive home; `dot-leaf-identity` only *deferred* to it.
- The `tdot` type-API-surface-only evidentiary caveat (zero Palace call sites; `vector.hpp:112` decl + `vector.cpp:269` def only) is already carried in both combinator homes (L3/inner_product §"Specializations" `tdot` bullet + §Status member-level caveat; L2/inner_product §"tdot" + §Status member-level caveat). No absorption pointer is missing — nothing new to add.

### (b) RE-EXPRESS book/src/L3/dot.md through the L3/inner_product combinator

Replaces the frontmatter (`lowers_to` pointed at L1 base-form via the non-adjacent convention), the lede, §Context, the §"Lowers to" base-form framing + its dead `dot-body-identity` reference, and the §Evidence / §"L3 vs L1 distinction" base-form re-derivation, with combinator-routed framing. Load-bearing facts preserved verbatim: the conjugation choice is value-bearing for complex vectors (`xᴴ y`, conjugate-linear arg-1); `tdot` is the unconjugated bilinear specialization; the reduction-tree IEEE non-law is load-bearing; no sequential obstruction. High→low: defined in L3 vocabulary *through* the combinator, no L1/L0 base-form re-derivation.

```edit:book/src/L3/dot.md
[old]:
---
layer: L3
operator: dot
firmness: firm
lowers_to:
  - book/src/L1/dot.md (identity-in-form on the primitive's signature; no L3-L1 theme — see Lowers-to)
lifts_from:
  - (none) — `dot` is a leaf primitive; no L4 entry exists (leaf primitives don't get L4 rows per cycle-010 audit verdict)
variant_axes:
  - element-type (real / complex)
  - conjugation-convention (hermitian / unconjugated `tdot` — complex element-type only)
---

# dot

Whole-tensor inner-product reduction at L3: `α = ⟨x, y⟩`. The canonical BLAS-1 reduction primitive rendered as an L3 field operation; the workhorse of Krylov coefficient computation and orthogonalization at the iteration-rotation layer. Identity-in-form lowering to L1 [`dot`](../L1/dot.md); the rotation work is at the surrounding wrapper (the `krylov-step` body), not on the primitive itself.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as `state' = f(state, params)`, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `dot` at L3 is a whole-tensor reduction — its signature `(x: Tensor[N], y: Tensor[N]) -> Scalar` exposes no element loop; the reduction over the length axis `N` is a single semantic step at L3 just as it is at L1.

This entry is a **layer-coherence anchor** per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009 meta-phase). The L3 form is value-thread-isomorphic to the L1 form — the rotation L3→L1 is identity-in-form on the primitive's signature; only the surrounding context (the iteration view at L3 vs. the mutation-rotation view at L1) differs. The L3 entry exists because each layer is coherent within itself: a reader navigating L3 (whose index at `book/src/L3/index.md:13` advertises `dot` as a field operation in L3 vocabulary) cannot be required to reach down to L1 to find the primitive.

The companion concept page [`concepts/dot`](../concepts/dot.md) carries the BLAS-1 heritage framing and the cross-cutting prose treatment; the L1 entry [`L1/dot`](../L1/dot.md) is authoritative on every factual claim about the Palace surface. This L3 entry adds **iteration-rotation framing** to those — it names `dot` as an L3-native whole-tensor reduction consumed inside the surrounding `krylov-step` body — but does not duplicate algebraic-law content; the laws hold uniformly across L1 / L2 / L3 because the body is identity-in-form across the chain.

The L1 conjugation convention (first-argument-conjugation for complex Hermitian `dot`, `⟨x, y⟩ = xᴴ y`) carries through unchanged at L3. The L0 free-function asymmetry — `linalg::Dot(comm, x, y) = yᴴ x` per `vector.cpp:674-685`, conjugating the second argument — is documented at `book/src/L1/dot.md:43, 104-105` and is L1>L0 lowering content, not L3 content.
[new]:
---
layer: L3
operator: dot
firmness: firm
lowers_to:
  - book/src/L2/inner_product.md (dot is the Hermitian/symmetric specialization of the inner_product combinator; identity-in-form on the body — see §"Downward to L2 (through inner_product)")
lifts_from:
  - (none) — `dot` is a reduction specialization; no L4 entry exists (folds/leaves are not first-class L4 vocabulary per cycle-010 audit verdict; the combinator appears inside L4 composed entries like krylov-step §Semantics as a let-binding)
variant_axes:
  - element-type (real / complex)
  - conjugation-convention (hermitian / unconjugated `tdot` — complex element-type only)
---

# dot

Whole-tensor inner-product reduction at L3: `α = ⟨x, y⟩`. The canonical BLAS-1 reduction primitive rendered as an L3 field operation; the workhorse of Krylov coefficient computation and orthogonalization at the iteration-rotation layer. **`dot` is the Hermitian/symmetric specialization (at `M = I`) of the L3 [`inner_product`](./inner_product.md) combinator**; this entry adds the leaf-level iteration-rotation framing (the conjugation choice, the consuming `krylov-step` context) rather than re-deriving the reduce-to-scalar base form, which is the combinator's (§"Downward to L2 (through inner_product)").

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as `state' = f(state, params)`, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `dot` at L3 is a whole-tensor reduction — its signature `(x: Tensor[N], y: Tensor[N]) -> Scalar` exposes no element loop; the reduction over the length axis `N` is a single semantic step at L3.

`dot` does **not** re-derive the reduce-to-scalar base form: it **speaks through** the L3 [`inner_product`](./inner_product.md) combinator (firm cycle-050), of which it is the conjugation-axis specialization `dot(x, y) = inner_product x y` at the Hermitian (complex) / symmetric (real) kernel value, with `M = I`. The combinator IS the L3 entry for the reduce-to-scalar inner-product family (per CLAUDE.md §Methodology invariants ⟢ — the combinator is the entry, members are specialization notes); this `dot` chapter is the named workhorse specialization the combinator's §"Specializations" points back at (`book/src/L3/inner_product.md:148-152`). It adds the leaf-level facts the family-level combinator does not carry: the value-bearing conjugation choice (below), the `tdot` co-defined unconjugated variant, and the leaf's consumption inside the `krylov-step` body.

The companion concept page [`concepts/dot`](../concepts/dot.md) carries the BLAS-1 heritage framing and the cross-cutting prose treatment; the L1 entry [`L1/dot`](../L1/dot.md) is authoritative on every factual claim about the Palace surface. This L3 entry does not duplicate algebraic-law content; the laws hold uniformly across the chain because the body is identity-in-form through the combinator (§"Downward to L2 (through inner_product)").

The conjugation convention is **value-bearing for complex vectors**: the L1/L2/L3 Hermitian `dot` is conjugate-linear in the first argument (`⟨x, y⟩ = xᴴ y`), carried through unchanged at L3. The L0 free-function asymmetry — `linalg::Dot(comm, x, y) = yᴴ x` per `vector.cpp:674-685`, conjugating the second argument — produces the complex-conjugate value `yᴴ x` (not `xᴴ y`); reconciling that re-order is the genuine translation carried by the KEPT L2>L1 [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) theme (documented at `book/src/L1/dot.md:43, 104-105`), not L3 content. L3 sees the convention pinned at arg-1.
```

```edit:book/src/L3/dot.md
[old]:
## Lowers to

L3 `dot` lowers to L1 [`dot`](../L1/dot.md) as **identity-in-form on the primitive's signature**. There is no L3-L1 lowering theme — no `book/src/L3-L1/` directory currently exists (precedent: cycle-010 `L3/krylov-step.md` records its identity-in-form lowering in-line at the entry, not in a separate theme file). The rotation work for this primitive lives in the surrounding wrapper at the consuming `krylov-step` body, captured by [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 (which names `dot` among the seven primitives that are "L3-native because [each primitive's] signature has no per-element loop visible").

The L1>L0 lowering of `dot` lives at the L1 entry's evidence section (`book/src/L1/dot.md` §Evidence) — Palace's `linalg::Dot` template at `palace/linalg/vector.hpp:247-253` composes `LocalDot` with `Mpi::GlobalSum`; the Hypre per-rank reduction kernel at `vector.cpp:665-672` is the local kernel; the MPI_Allreduce is the collective. None of this is L3 content; the L3 form sees a single-step whole-tensor reduction.
[new]:
## Downward to L2 (through inner_product)

L3 `dot` lowers **through the L3 [`inner_product`](./inner_product.md) combinator**, of which it is the Hermitian/symmetric specialization (`dot(x, y) = inner_product x y` at the conjugated kernel, `M = I`). The combinator lowers to L2 [`inner_product`](../L2/inner_product.md) as **identity-in-form on the body** (value-thread-isomorphic reduce-to-scalar reduction; no L3-L2 theme file — the in-line §"Downward to L2" at `book/src/L3/inner_product.md:363-385` is the home, per the cycle-012 non-adjacent-identity convention). There is no separate `dot`-specific L3>L2 theme: the former degenerate `dot-body-identity` theme was a `dot`-named restatement of that body identity and was demoted into the combinator's pre-built §"Downward to L2" home (cycle-051 vocabulary-shift-redirect refactor-pass).

The **genuine** translation in the chain is the KEPT L2>L1 [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) theme — it carries the conjugation/element-type/weight dispatch, the value-level `xᴴ y` ↔ `yᴴ x` re-order (the value-bearing conjugation reconciliation for complex `dot`), and the per-call pinned reduction trees (the load-bearing IEEE-754 non-law). The `dot` specialization is the plain (`M = I`) Hermitian / symmetric member of that fold's conjugation dispatch; bit-reproduction / re-order / reduction-tree concerns are read off the fold-specialization theme, not re-derived here. The MPI collective and the local-then-collective `LocalDot ∘ Mpi::GlobalSum` two-step are L1>L0 lowering content (folded out per single-rank scope); the L3 form sees a single-step whole-tensor reduction.
```

```edit:book/src/L3/dot.md
[old]:
**L1 anchor**: [`L1/dot`](../L1/dot.md) (firm cycle-002) — the L1 entry is authoritative on the Palace surface details, the receiver-vs-argument asymmetry on the L0 method form, the self-dot fast path (`&y == this`), and the complete L0 evidence list. This L3 entry does not duplicate those details; the L3>L1 rotation is identity-in-form on the primitive itself.
[new]:
**Combinator (L3)**: [`inner_product`](./inner_product.md) (firm cycle-050) — the reduce-to-scalar inner-product combinator this entry is the Hermitian/symmetric specialization of; authoritative on the family-level reduce-to-scalar base form, the reduction-monoid-homomorphism law, and the no-sequential-obstruction verdict. This `dot` chapter does not re-derive the base form; it adds the leaf-level conjugation / consuming-context framing.

**Genuine L2>L1 translation**: [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) (firm cycle-019, KEPT cycle-049 D2) — the conjugation/element-type/weight dispatch + the `xᴴ y` ↔ `yᴴ x` re-order + the per-call pinned reduction trees; the home for all `dot`-specialization fusion/re-order content.

**L1 anchor**: [`L1/dot`](../L1/dot.md) (firm cycle-002) — the L1 entry is authoritative on the Palace surface details, the receiver-vs-argument asymmetry on the L0 method form, the self-dot fast path (`&y == this`), and the complete L0 evidence list. This L3 entry does not duplicate those details.
```

```edit:book/src/L3/dot.md
[old]:
## Status

`firm` — L3 form is value-thread-isomorphic to the L1 form (identity-in-form rotation); algebraic laws inherited unchanged; variant-axis profile inherited unchanged at two axes. The entry exists as a **layer-coherence anchor** per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** (cycle-009 codification). Harvested cycle-011 wave-1 as part of the BLAS-1 reduction cohort backfill (sibling dispatch to `apply_linop`, the axpy cohort, and `scal` at L3).
[new]:
## Status

`firm` — `dot` is the Hermitian/symmetric specialization (at `M = I`) of the firm L3 [`inner_product`](./inner_product.md) combinator (firm cycle-050); the reduce-to-scalar base form, algebraic laws, and no-sequential-obstruction verdict are inherited unchanged from the combinator (this chapter adds the leaf-level conjugation / consuming-context framing). Variant-axis profile inherited unchanged at two axes (element-type, conjugation-convention). The entry exists as a **layer-coherence anchor** per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** (cycle-009 codification) AND as the named workhorse specialization the combinator's §"Specializations" points back at (CLAUDE.md §Methodology invariants ⟢ — the combinator is the entry, members are specialization notes). Originally harvested cycle-011 wave-1 (BLAS-1 reduction cohort backfill); re-expressed through the `inner_product` combinator cycle-051 (vocabulary-shift-redirect refactor-pass — the two degenerate `dot-body-identity` / `dot-leaf-identity` themes demoted into the combinator's pre-built homes the same cycle).
```

```edit:book/src/L3/dot.md
[old]:
The L3 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's signature); all L0 evidence is transitive through L1. Direct citations relevant to this L3 entry:

- [`book/src/L1/dot.md`](../L1/dot.md) (firm cycle-002) — authoritative on Palace surface, signature, algebraic laws (inherited unchanged at L3), variant axes (inherited unchanged at L3), and the complete L0 evidence list (`vector.hpp:110-113`, `vector.hpp:242-253`, `vector.cpp:263-274`, `vector.cpp:665-685`, etc.).
[new]:
The L3 form is the Hermitian/symmetric specialization of the firm L3 `inner_product` combinator; all L0 evidence is inherited transitively (through the combinator, and through the firm L1 leaf). Direct citations relevant to this L3 entry:

- [`book/src/L3/inner_product.md`](./inner_product.md) (firm cycle-050) — the combinator this entry specializes; authoritative on the family-level reduce-to-scalar base form, the reduction laws (inherited unchanged here), and the no-sequential-obstruction verdict. §"Specializations" (`:148-152`) names this `dot` chapter as the workhorse Hermitian/symmetric specialization.
- [`book/src/L2-L1/inner-product-fold-specialization.md`](../L2-L1/inner-product-fold-specialization.md) (firm cycle-019, KEPT cycle-049 D2) — the genuine L2>L1 translation; the conjugation/element-type/weight dispatch + `xᴴ y` ↔ `yᴴ x` re-order + pinned reduction trees the `dot` specialization's fusion/re-order content is read off.
- [`book/src/L1/dot.md`](../L1/dot.md) (firm cycle-002) — authoritative on Palace surface, signature, algebraic laws (inherited unchanged at L3), variant axes (inherited unchanged at L3), and the complete L0 evidence list (`vector.hpp:110-113`, `vector.hpp:242-253`, `vector.cpp:263-274`, `vector.cpp:665-685`, etc.).
```

```edit:book/src/L3/dot.md
[old]:
- **L1**: pure functional reduction `α = dot(x, y)`. Mutation-rotation layer — the L0 destination buffer is erased from the signature (a `dot` returns a scalar; there is no destination buffer to mutate); the MPI collective is folded into the L1>L0 lowering. The receiver-vs-argument asymmetry on the L0 method form is erased (the L1 signature names the conjugated argument first by convention). Reduction-tree non-associativity recorded as a load-bearing algebraic claim.
- **L3**: whole-tensor reduction `α = dot(x, y)` rendered as an L3 field operation. Iteration-rotation layer — the surrounding consuming context (the `krylov-step` body) renders the iteration view explicitly as `(K, s) -> (K', s')` value-threading; `dot` itself is consumed as a leaf reduction with no iteration view of its own. The signature is identical to L1; the rotation is at the surrounding wrapper, not on the primitive.

The two layers' entries are **value-thread-isomorphic** on the primitive itself. The L3 entry exists for layer-coherence — a reader at L3 navigating the `krylov-step` body or the L3 vocabulary inventory must find `dot` defined in L3 vocabulary at L3, per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**.
[new]:
- **L1**: pure functional reduction `α = dot(x, y)`. Mutation-rotation layer — the L0 destination buffer is erased from the signature (a `dot` returns a scalar; there is no destination buffer to mutate); the MPI collective is folded into the L1>L0 lowering. The receiver-vs-argument asymmetry on the L0 method form is erased (the L1 signature names the conjugated argument first by convention). Reduction-tree non-associativity recorded as a load-bearing algebraic claim.
- **L3**: the Hermitian/symmetric specialization of the `inner_product` combinator, rendered as a whole-tensor reduce-to-scalar field operation `α = dot(x, y)`. Iteration-rotation layer — the surrounding consuming context (the `krylov-step` body) renders the iteration view explicitly as `(K, s) -> (K', s')` value-threading; `dot` itself is consumed as a leaf reduction with no iteration view of its own. The reduce-to-scalar base form is the combinator's; this chapter adds the leaf-level conjugation / consuming-context framing.

The L3 entry exists for layer-coherence — a reader at L3 navigating the `krylov-step` body or the L3 vocabulary inventory must find `dot` defined in L3 vocabulary at L3, per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** — and as the named workhorse specialization the `inner_product` combinator's §"Specializations" points back at (CLAUDE.md §Methodology invariants ⟢).
```

Note on the L3/dot §"Iteration-rotation marker", §Dependencies "Consumers", §Algebraic laws, §Signature, §"Variant axes" sections: these are NOT edited — they are leaf-level facts (the consuming `krylov-step` context, the conjugation kernel table, the value-bearing conjugation laws) that remain correct and load-bearing and do not reference the deleted slugs. The §"Lifts from" section (no L4 entry) is unchanged (still correct: `dot` carries no L4 calculus content). The §"Iteration-rotation marker" §68 reference to `krylov-step-body-identity.md:30-37` is a live consuming-context reference (NOT to a deleted slug) and is preserved.

### (c) Re-anchor / de-tense inbound references in surviving files

**L3/inner_product.md** — de-tense the forward-looking "demotes into at cycle-051" notes (the demotion is now enacted):

```edit:book/src/L3/inner_product.md
[old]:
  - book/src/L2/inner_product.md (identity-in-form on the body — value-thread-isomorphic to the L2 reduction; no L3-L2 theme, in-line §"Downward to L2"; the pre-built home dot-body-identity demotes into at cycle-051)
[new]:
  - book/src/L2/inner_product.md (identity-in-form on the body — value-thread-isomorphic to the L2 reduction; no L3-L2 theme, in-line §"Downward to L2"; the home the degenerate dot-body-identity theme was demoted into at cycle-051)
```

```edit:book/src/L3/inner_product.md
[old]:
§Methodology invariants "Identity rotations across non-adjacent layers are annotated
in-line"; precedent `book/src/L3/dot.md` §"Lowers to", `book/src/L3/krylov-step.md`). This
section is the **pre-built home** that the degenerate `dot-body-identity` L3>L2
identity-in-named-terms theme demotes into at cycle-051 (combinator-miner refactor-pass
(b.3): "L3>L2 is identity-in-named-terms — no rotation; `dot` is the Hermitian
specialization of the `inner_product` combinator at both layers").
[new]:
§Methodology invariants "Identity rotations across non-adjacent layers are annotated
in-line"; precedent `book/src/L3/dot.md` §"Downward to L2 (through inner_product)",
`book/src/L3/krylov-step.md`). This section is the **home** the degenerate
`dot-body-identity` L3>L2 identity-in-named-terms theme was demoted into at cycle-051
(combinator-miner refactor-pass (b.3): "L3>L2 is identity-in-named-terms — no rotation;
`dot` is the Hermitian specialization of the `inner_product` combinator at both layers";
the `L3-L2/dot-body-identity.md` file was deleted, its identity-in-form content absorbed
here).
```

**L2/inner_product.md** — de-tense the two notes that reference the (now-deleted) themes. These are plain-text backtick references (NOT live `.md` links), so they do not break the build; they are de-tensed for accuracy:

```edit:book/src/L2/inner_product.md
[old]:
> The standalone `L2/dot.md` leaf-floor is collapsed into a §"Specializations" note
> (cycle-050 enactment — see combinator-miner refactor-pass report); the degenerate
> `L3-L2/dot-body-identity` + `L2-L1/dot-leaf-identity` identity-in-named-terms themes
> are demoted to in-line notes (they are vocabulary-failed-to-shift smells, not
> translations). The combinator propagates **up** to a new `L3/inner_product` entry
[new]:
> The standalone `L2/dot.md` leaf-floor is collapsed into a §"Specializations" note
> (cycle-050 enactment — see combinator-miner refactor-pass report); the degenerate
> `L3-L2/dot-body-identity` + `L2-L1/dot-leaf-identity` identity-in-named-terms theme
> files were deleted at cycle-051, their identity-in-form content absorbed into the
> combinator homes (they were vocabulary-failed-to-shift smells, not translations). The
> combinator propagates **up** to a new `L3/inner_product` entry
```

```edit:book/src/L2/inner_product.md
[old]:
`L2/dot.md` leaf-floor collapse + the `L3/inner_product` upward propagation + the
`L3-L2/dot-body-identity` / `L2-L1/dot-leaf-identity` smell-theme demotions are the
cycle-050 enactment (mapped in the refactor-pass report). The combinator's own substantive
[new]:
`L2/dot.md` leaf-floor collapse + the `L3/inner_product` upward propagation are the
cycle-050 enactment (mapped in the refactor-pass report); the
`L3-L2/dot-body-identity` / `L2-L1/dot-leaf-identity` smell-theme files were deleted at
cycle-051 (their identity-in-form content absorbed into the combinator homes). The combinator's own substantive
```

**L3/index.md** — de-tense the dep-map "Downward" cell + the cohort-growth-log forward note (both are plain-text backtick references to the slugs, no live link):

```edit:book/src/L3/index.md
[old]:
| L2 [`inner_product`](../L2/inner_product.md) via in-line §"Downward to L2" (identity-in-form on the body — value-thread-isomorphic to the L2 reduction; no L3-L2 theme file; the pre-built home `dot-body-identity` demotes into at cycle-051). Transitively L2>L1 via the genuine [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) (no `L3-L1/` directory; in-line per cycle-012 non-adjacent-identity convention). |
[new]:
| L2 [`inner_product`](../L2/inner_product.md) via in-line §"Downward to L2" (identity-in-form on the body — value-thread-isomorphic to the L2 reduction; no L3-L2 theme file; the home the degenerate `dot-body-identity` theme was demoted into at cycle-051). Transitively L2>L1 via the genuine [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) (no `L3-L1/` directory; in-line per cycle-012 non-adjacent-identity convention). |
```

```edit:book/src/L3/index.md
[old]:
The L3>L2 edge of each combinator is a degenerate identity-in-named-terms in-line note (the pre-built home the four `{scal,axpy,axpby,axpbypcz}-body-identity` / the `dot-body-identity` themes demote into at cycle-051); the substantive rotation in each chain is the existing firm L2>L1 fold-specialization theme (`linear-combination-fold-specialization` / `inner-product-fold-specialization`, both KEPT cycle-049).
[new]:
The L3>L2 edge of each combinator is a degenerate identity-in-named-terms in-line note (the home the four `{scal,axpy,axpby,axpbypcz}-body-identity` / the `dot-body-identity` themes were demoted into at cycle-051 — those theme files deleted, their identity-in-form content absorbed into the combinator homes); the substantive rotation in each chain is the existing firm L2>L1 fold-specialization theme (`linear-combination-fold-specialization` / `inner-product-fold-specialization`, both KEPT cycle-049).
```

**Inbound LIVE links in cross-dispatch files** (the build-break risk if any survive — `linkcheck2` would hard-fail on a live `.md` link to a deleted slug). Two files carry live `.md` links to D2's deleted `dot-*-identity` slugs:

- **`book/src/L3-L2/divfree-projector-body-identity.md` — DELETED by sibling D4 this cycle** (`reports/2026-06-01T210700Z-lifter-jacobi-divfree-demotion/CYCLE.md` §1, `delete:book/src/L3-L2/divfree-projector-body-identity.md`). The inbound live links it carries to `dot-body-identity` die with the file; **no D2 edit needed** (editing a file another dispatch deletes is moot — and would be a per-report apply failure if D4 applies first). REPAIR-DROPPED from this report (the two `divfree-projector-body-identity.md` edits the report originally carried were removed by the repairer; the premise that this file "survives" was false — it is a D4 delete target).
- **`book/src/L2-L1/divfree-projector-leaf-identity.md` — KEPT** (D4 explicitly preserves it; the L2>L1 step-4 fusion theme survives). Its live link to D2's deleted `dot-leaf-identity` slug WOULD dangle, so de-linking it IS necessary. **Three-way co-edit flag for the integrator:** this KEPT file is touched by D2 (de-link `dot-leaf-identity`, below), D3 (`reports/2026-06-01T210700Z-lifter-nrm2-consumer-demotion/CYCLE.md` — de-link `nrm2-leaf-identity`), AND D4 (re-anchor the `divfree-projector-body-identity` link at line 36). The edits target distinct on-disk lines/substrings EXCEPT line 266, where D2 (drops the `dot-leaf-identity` live link) and D3 (drops the `nrm2-leaf-identity` live link) BOTH edit the same paragraph — D2's `old_string` is a substring of D3's 3-line `old_string`. Integrator must serialize these two line-266 edits (apply one, then re-derive the other's `old_string` against the post-first-edit text). D4's line-36 edit and D2's line-19 edit are on distinct lines (no collision with each other or the line-266 pair). De-link edits below:

```edit:book/src/L2-L1/divfree-projector-leaf-identity.md
[old]:
The `-leaf-identity` slug (matching the cycle-041 [`dot-leaf-identity`](./dot-leaf-identity.md)
[new]:
The `-leaf-identity` slug (matching the cycle-041 `dot-leaf-identity` precedent — that theme deleted cycle-051, its content absorbed into the `inner_product` combinator homes
```

```edit:book/src/L2-L1/divfree-projector-leaf-identity.md
[old]:
value-preserving step-4 fusion, NOT a fold→leaf dispatch across a family. Unlike `dot-leaf-identity`,
[new]:
value-preserving step-4 fusion, NOT a fold→leaf dispatch across a family. Unlike the (deleted cycle-051) `dot-leaf-identity`,
```

```edit:book/src/L2-L1/divfree-projector-leaf-identity.md
[old]:
([`dot-leaf-identity`](./dot-leaf-identity.md) / [`nrm2-leaf-identity`](./nrm2-leaf-identity.md)
[new]:
(`dot-leaf-identity` (deleted cycle-051; absorbed into the `inner_product` combinator homes) / [`nrm2-leaf-identity`](./nrm2-leaf-identity.md)
```

### (d) Remove D2's OWN SUMMARY.md lines + dep-map rows (de-link AND physically remove)

**SUMMARY.md** — remove the two chapter lines for the deleted themes:

```edit:book/src/SUMMARY.md
[old]:
- [dot-body-identity](./L3-L2/dot-body-identity.md)
[new]:
```

```edit:book/src/SUMMARY.md
[old]:
- [dot-leaf-identity](./L2-L1/dot-leaf-identity.md)
[new]:
```

**L3-L2/index.md** — remove the dep-map table row + the bullet for `dot-body-identity`:

```edit:book/src/L3-L2/index.md
[old]:
| [`dot-body-identity`](./dot-body-identity.md) | L3 [`dot`](../L3/dot.md) §Signature — whole-tensor reduce-to-scalar `dot :: Tensor[N] -> Tensor[N] -> Scalar` (+ `tdot` co-variant), single semantic step, no element loop, no sequential obstruction. | L2 [`dot`](../L2/dot.md) §Signature — the same-named conjugation-axis leaf-floor of `inner_product` (the plain `M=I` Hermitian / symmetric member), value-thread-isomorphic signature; fusion content carried by the fold-parent, not the leaf. | `structural` (`dot` is L3-native by signature shape per `krylov-step-body-identity.md:97` — no element loop, so the iteration rotation is already done at the signature level; no wrapper around the leaf) + secondary `empirical-match` (L3 + L2 leaf-floors independently authored value-thread-isomorphic to the firm L1 leaf) | `firm` (cycle-041 wave-2 abstractor; identity-in-form on the single BLAS-1 leaf — the leaf-level analogue of `krylov-step-body-identity`'s multi-primitive-body identity; presupposes the wave-1 D1 leaf-floor `L2/dot`) |
[new]:
```

```edit:book/src/L3-L2/index.md
[old]:
- `dot-body-identity` — the L3 whole-tensor `dot` reduction lowers to the L2 same-named leaf-floor identity-in-form on the body; `dot` is L3-native by signature shape (no element loop), so the iteration rotation is already done at the signature level.
[new]:
```

**L2-L1/index.md** — remove the dep-map table row + the bullet for `dot-leaf-identity`:

```edit:book/src/L2-L1/index.md
[old]:
| [dot-leaf-identity](./dot-leaf-identity.md) | `L2/dot` (firm, cycle-041 leaf-floor) | `L1/dot` (firm; `dot` + `tdot`) | firm *(structural; identity-in-form on the inner-product leaf — value-thread-isomorphic signature; all L2-layer fusion deferred to the fold-parent `inner-product-fold-specialization`; thin floor-edge of the BLAS-1 leaf)* |
[new]:
```

```edit:book/src/L2-L1/index.md
[old]:
- `dot-leaf-identity` — the L2 `dot` leaf-floor lowers to the L1 `dot` primitive identity-in-form on the signature; all L2-layer fusion deferred to the fold-parent `inner-product-fold-specialization` (no leaf-unique fusion surplus). Slug `-leaf-identity` (NOT `-fold-specialization`): the edge is an identity-leaf-lowering, not a fold→leaf dispatch.
[new]:
```

**DEFER the consolidated firm-theme TALLY to D5** per dispatch instruction. The cohort-growth-log count lines in `L2-L1/index.md` (line 73, the `[cycle-050 DEMOTION — firm 21 → 17 ...]` head) and the L2/index.md cycle-041 cohort line (121) are NOT touched by this dispatch — D5 owns the consolidated tally across all cycle-051 demotions (D1 linear_combination family + D2 dot family + any D4/D8 disposition). D2 removes only its own rows/lines; the running count is D5's.

## Discipline notes

- **Pure structural rewrite (combinator routing), not authorship.** The L3/dot re-expression replaces base-form re-derivation framing with combinator-routed framing; no new content decisions. The combinator home (`L3/inner_product`) and the genuine translation (`inner-product-fold-specialization`) both pre-exist and are firm; this dispatch only points the leaf at them. Per the lifter "structural rewrite, not authorship" discipline.
- **Layer-definition discipline high→low preserved.** The re-expressed L3/dot defines `dot` in L3 vocabulary *through* the L3 `inner_product` combinator (a same-layer reference) and references the L2>L1 theme for the genuine translation — it does NOT re-derive an L1/L0 base form. The §"Lowers to" → §"Downward to L2 (through inner_product)" rename + content keeps the rewrite direction high→low (L3 into L2 through the combinator). Friction-ledger `layer-definition-discipline-high-to-low`.
- **Load-bearing facts preserved verbatim:** (i) the conjugation choice is value-bearing for complex vectors (`xᴴ y`, conjugate-linear arg-1; the `yᴴ x` L0 re-order is the complex-conjugate value) — preserved in the new §Context conjugation paragraph + routed to the kept theme; (ii) `tdot` is the unconjugated bilinear specialization (preserved in lede + §Specializations routing + the unchanged §Algebraic-laws laws 11–13 + §Signature kernel table); (iii) the reduction-tree IEEE-754 non-law is load-bearing (preserved — routed to the kept theme; the unchanged §Algebraic-laws "Laws that do not hold" + §"Iteration-rotation marker" carry it); (iv) no sequential obstruction (unchanged §"Iteration-rotation marker"). No laws-section substantive rework was needed — the leaf's laws are inherited unchanged and remain correct, so the §Algebraic laws section is NOT edited (no carry to batch-16 needed on the laws).
- **Pre-built absorption homes — no duplication.** Per scope (a) "thin absorption pointer only if missing — do not duplicate substance": the L3/inner_product §"Downward to L2" + L2/inner_product lede/inversion notes already carry the identity-in-form absorption + the `tdot` caveat; nothing was added, only the deleted theme files' forward-looking-tense references were de-tensed to past-tense statements of fact.
- **Cross-dispatch dangling handled per-report (defensive de-link).** Of the two `divfree-projector-*-identity` files carrying live `.md` links to my deleted slugs: `divfree-projector-body-identity.md` is **DELETED by sibling D4 this cycle** — its inbound link dies with the file, so I do NOT edit it (a moot edit on a doomed file, and a per-report apply failure if D4 applies first; this corrects the report's earlier false "both survive" premise — repair-dropped). `divfree-projector-leaf-identity.md` is **KEPT** (D4 preserves it), so its live link to my deleted `dot-leaf-identity` would dangle and IS de-linked here. That KEPT file is co-edited by D2 (line 19 + line 266), D3 (line 266 — drops the `nrm2-leaf-identity` link), and D4 (line 36 — re-anchors the `body-identity` link); D2's line-266 edit and D3's line-266 edit target the same paragraph (D2's `old_string` is a substring of D3's), requiring integrator serialization — flagged in §(c) and Open questions. The OTHER referencing files (`axpy-body-identity` / `axpby-body-identity` [D1 delete targets], `axpy`/`axpby`/`axpbypcz`-`leaf-identity` [D1 delete targets], `jacobi-smoother-leaf-identity` [D8 DEMOTE-OK delete target]) reference my slugs but are themselves being DELETED by their owning dispatches — their links die with the files, so I do NOT edit them (avoids cross-dispatch edit conflict). See Open questions for the integrator-ordering caveat.
- **Citation self-verification:** all in-book reference anchors I emit were verified on-disk this dispatch — `L3/inner_product.md:148-152` (§Specializations `dot` bullet, anchor `dot` = Hermitian specialization, confirmed); `L3/inner_product.md:363-385` (§"Downward to L2" pre-built home, confirmed); `L1/dot.md:43` (conjugation-convention line, anchor `Conjugation convention`, confirmed) + `:104-105` (L3-vs-L1 distinction lines, confirmed); `vector.cpp:674-685` (the `yᴴ x` complex reduction re-order — carried verbatim from the prior L3/dot:26, an inherited-transitive citation, NOT re-localized here per high→low). No new L0 citations are introduced by the re-expression (it removes base-form re-derivation; all L0 evidence is inherited transitively through the combinator + L1 leaf).

## Supporting evidence

- Pre-built combinator homes (authored cycle-050): `book/src/L3/inner_product.md` §"Downward to L2" (lines 363–385) + §"Specializations" (148–152); `book/src/L2/inner_product.md` lede note (22–29) + cycle-049-inversion note (lines 465–474).
- KEPT genuine L2>L1 translation: `book/src/L2-L1/inner-product-fold-specialization.md` (firm cycle-019, re-audited KEEP cycle-049 D2).
- Provenance of the demotion: combinator-miner refactor-pass cycle-049 D2 (b.3 "L3>L2 is identity-in-named-terms — no rotation"); cycle-050 D2 authored the L3/inner_product upward propagation with the pre-built demotion homes; the `L3/index.md` cohort-growth-log (line 65) + `L2-L1/index.md` cohort-growth-log (line 73, the cycle-050-vs-051 split) name the `dot-body-identity` / `dot-leaf-identity` demotion as cycle-051 work.
- Deleted-slug inbound-link census (grep `book/src/` for both slugs): the KEPT `divfree-projector-leaf-identity.md` de-linked here; the D4-deleted `divfree-projector-body-identity.md` left to D4 (its link dies with the file — no D2 edit); D1/D8 delete-target files left to their owning dispatch.

## Open questions / caveats

- **Three-way co-edit on the KEPT `divfree-projector-leaf-identity.md` — integrator serial-ordering required (build-readiness).** This file is KEPT (D4 preserves it) and is edited by three dispatches this cycle: **D2** (this report — de-link `dot-leaf-identity`: line 19 + line 266), **D3** (`lifter-nrm2-consumer-demotion` — de-link `nrm2-leaf-identity`: line 266), **D4** (`lifter-jacobi-divfree-demotion` §7b — re-anchor the `divfree-projector-body-identity` link: line 36). Line 19 (D2-only) and line 36 (D4-only) are non-colliding. **Line 266 collides**: D2 drops the `dot-leaf-identity` live link, D3 drops the `nrm2-leaf-identity` live link, from the SAME paragraph (D2's `old_string` is a substring of D3's 3-line `old_string`). Integrator must apply one line-266 edit, then re-derive the other's `old_string` against the post-edit text (whichever applies second will not match verbatim). D3's OQ-2 flags the same collision from its side. (The sibling `divfree-projector-body-identity.md` is a D4 delete target — NOT edited by D2; its inbound link dies with the file.)
- **Integrator-ordering caveat for cross-dispatch danglers (defensive, build-readiness).** My deletions strand live links in `axpy-body-identity.md` / `axpby-body-identity.md` (D1) and `jacobi-smoother-leaf-identity.md` (D8) IF those files are NOT also deleted by their owning dispatches before the book rebuild. Per the cycle-050-vs-051 split (`L2-L1/index.md:73`), the `axpy`/`axpby`/`axpbypcz` family is D1 (collapse into `linear_combination`) and `jacobi-smoother-leaf-identity` is D8 DEMOTE-OK — i.e. those files ARE delete targets, so the links die with them. The residual risk is purely an integrator-finalize ordering one: if a referenced file survives unexpectedly, integrator-finalize should defensively de-link the dead reference (per the integrator build-repair authority + skill `revert`-class build-repair). I did NOT edit those files myself to avoid cross-dispatch edit conflict (they may be deleted out from under my edit). Flag for integrator-finalize: after applying D1/D2/D4/D8, grep `book/src/` for `dot-body-identity` / `dot-leaf-identity` live `.md` links and de-link any survivor before `cargo make book`.
- **`L2/dot.md` leaf-floor collapse is NOT in D2 scope.** The L2/inner_product narrative (lines 22–24) describes `L2/dot.md` as "collapsed into a §Specializations note (cycle-050 enactment)" but the file still exists on-disk (22792 bytes, Jun 1 06:34). Whether `L2/dot.md` is physically reduced/deleted is a SEPARATE disposition (the L2-leaf-chapter collapse, distinct from the two THEME files this dispatch deletes). My `dot-leaf-identity` deletion does not strand `L2/dot.md` — the combinator home already carries its absorption pointer. Surfaced for the cohort-wide leaf-disposition convention (OQ `l2-l3-leaf-chapter-disposition-cohort-wide`, named in `L3/index.md:65`); NOT acted on here.
- **No laws-section batch-16 carry needed.** Scope (b) flagged "if the laws section needs substantive (not mechanical) rework, flag + carry to batch-16." It does not: the L3/dot algebraic laws (1–13 + the non-laws) are inherited unchanged and remain correct under the combinator routing (they ARE the combinator's laws, specialized to the Hermitian/bilinear members). The §Algebraic laws section is left untouched. No carry.

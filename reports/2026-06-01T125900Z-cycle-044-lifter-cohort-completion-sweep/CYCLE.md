---
agent: lifter
invoked_at: 2026-06-01T12:59:00Z
scope: L3 cohort-completion sweep — (i) re-anchor 4 NEW-floor L3 entries to present L2 floors + body-identity themes; (ii) l3-index-audit-block-citation-drift index-wide re-pin; (iii) directive-slug residual l2-floor-under-l3-blas1-cohort → l2-floor-under-l3-leaf-cohort prose rename
status: pending
inputs:
  - book/src/L3/axpy.md
  - book/src/L3/axpby.md
  - book/src/L3/axpbypcz.md
  - book/src/L3/normalize.md
  - book/src/L3/index.md
  - book/src/L2/axpy.md
  - book/src/L2/axpby.md
  - book/src/L2/axpbypcz.md
  - book/src/L2/normalize.md
  - book/src/L3-L2/axpy-body-identity.md
  - book/src/L3-L2/axpby-body-identity.md
  - book/src/L3-L2/axpbypcz-body-identity.md
  - book/src/L3-L2/normalize-body-identity.md
  - book/src/L3/jacobi-smoother.md
  - book/src/L3/assemble-diagonal.md
  - book/src/L3/reciprocal.md
  - book/src/L3/elementwise_product.md
  - book/src/L3/divfree-projector.md
  - book/src/L3/orthogonalize.md
  - book/src/L2/dot.md
  - book/src/L2/scal.md
  - book/src/L2/reciprocal.md
  - book/src/L2/elementwise_product.md
  - book/src/L2/nrm2.md
  - book/src/L2/assemble-diagonal.md
  - book/src/L2-L1/nrm2-leaf-identity.md
  - book/src/L3-L2/nrm2-body-identity.md
integrated_at: 2026-06-01T150500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-044 batch integration (FIRST substantive L3>L2 rotation cycle); D1 consolidated lifter cohort-completion sweep — re-anchored axpy/axpby/axpbypcz/normalize L3 entries L3>L1 → L3>L2>L1 (closing 4 staleness OQs) + co-located audit-block citation re-pins + directive-slug rename l2-floor-under-l3-blas1-cohort → -leaf-cohort book-wide (ZERO old-slug remain in book/); applied clean, build exit 0, zero build-repairs; see reports/2026-06-01T150500Z-integrator-finalize-cycle-44/CYCLE.md + cycle-044 STAGING row 1."
---

# CYCLE: L3 cohort-completion sweep (cycle-044 D1)

## Summary

Consolidated cohort-completion sweep — the cycle-043 carry-forward. Three bundled jobs, all
re-anchor / citation-fix / prose-rename (structure stays, vocabulary + citations firm up):

- **(i)** Cycle-043 landed four NEW L2 floors (`L2/axpy`, `L2/axpby`, `L2/axpbypcz`, `L2/normalize`,
  all `firm`) plus their four `L3-L2` body-identity themes (`axpy-body-identity`,
  `axpby-body-identity`, `axpbypcz-body-identity`, `normalize-body-identity`, all `firm`). The four
  firm L3 entries `L3/axpy` / `L3/axpby` / `L3/axpbypcz` (cycle-011) and `L3/normalize` (cycle-039)
  still assert "**no L2 intermediate** … the BLAS-1 primitives are L1 leaves not L2 compositions" /
  "direct L3>L1 hop" / "no interposed L2 entry, no `L3-L2`/`L3-L1` theme file". Those assertions went
  **stale** when the L2 floors + body-identity themes landed. I re-anchor each L3 entry's `lowers_to:`
  frontmatter + §Context-"Downward" + §"Lowers to" (+ §"Lifts from" / §Evidence where they restate the
  no-L2 claim) to route **L3>L2>L1 through the present adjacent L2 floor via the body-identity theme** —
  matching the cycle-042/043 precedent already enacted on the sibling entries (`assemble-diagonal.md:130`,
  `reciprocal.md:131`, `elementwise_product.md:149` all say "the **present adjacent L2 floor** … via the
  `*-body-identity` L3>L2 theme"). The cycle-012 non-adjacent-identity nuance is preserved: the *transitive*
  L3>L1 identity stays in-line, but the *adjacent* L3>L2 edge now goes through the firm body-identity theme,
  and no `L3-L1/` directory is created. The four L3 index dep-map rows (`index.md:24-26,37`) carry the same
  stale "no L2 intermediate" assertion and are re-anchored too.

- **(ii)** `l3-index-audit-block-citation-drift` index-wide re-pin. The cycle-036 D2 cohort-growth
  audit block in `book/src/L3/index.md` MOVED (working-notes consolidation across c037-c040). Its
  current on-disk positions (citecheck-verified): header bullet **:45**, **(A) Identity-in-form
  verdict :46**, **(A) L1-promotion-gated :47**, **(B) Substantive :48**, **(C) NOT-L3-relevant :49**,
  routing sentence :50; the cycle-037 "four (A) backfills remained" note :58; audit-block span **:45-50**.
  Cross-references throughout the L3 entries + index still point at OLD lines (`:38-43`, `:39`, `:40-45`,
  `:41`, `:43-48`, `:44`, `:45`, `:47`, `:53`). citecheck `--anchor` confirms each drift
  (`:41→:46`, `:44→:46`, `:47→:48`, `:53→:58`, `:45→:47`, span `→:45-50`). Re-pinned to correct targets.

- **(iii)** Directive-slug residual. ~25 prose occurrences across 12 chapter bodies still carry the OLD
  directive slug `l2-floor-under-l3-blas1-cohort` in §Status / provenance prose. The slug was ratified to
  `l2-floor-under-l3-leaf-cohort` (slugs/filenames already renamed c043; this is the residual *prose*
  string rename — pure mechanical, not a slug/filename change).

No content-correction (job is a pure re-anchor + citation-fix + prose-rename). No status flips
(all four L3 entries stay `firm`; all touched L2 entries stay `firm`). One OQ surfaced (see below):
the four L3 entries' `lifts_from:`/§"Lifts from" "no L2 intermediate" framing is the same stale claim
as `lowers_to:` — I re-anchor it, but flag that the c043 L2-floor landing should have triggered this
re-anchor as part of that cycle (deferred carry-forward, now closed by this dispatch).

---

## Proposed changes

### Job (i) — re-anchor `L3/axpy` to the present `L2/axpy` floor via `axpy-body-identity`

```edit:book/src/L3/axpy.md
[old]: lowers_to:
  - book/src/L1/axpy.md (identity-in-form rotation on the primitive's signature shape; whole-tensor in / whole-tensor out at both layers; no L2 intermediate because the BLAS-1 primitives are L1 leaves not L2 compositions)
[new]: lowers_to:
  - book/src/L2/axpy.md (present adjacent L2 floor, cycle-043; identity-in-form on the primitive's signature shape, via the `axpy-body-identity` L3>L2 theme; whole-tensor in / whole-tensor out at both layers) → book/src/L1/axpy.md (transitive L3>L1 identity in-line, L3>L2 ∘ L2>L1)
```

```edit:book/src/L3/axpy.md
[old]: No L4 monadic vocabulary appears in the L3 signature (no `Solve`, no `modify`, no `do`-block) — `axpy` is not a calculus combinator at L4. The cohort audit (`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`) verdict for the BLAS-1 cohort at L4 is **CONFIRMED-NOT-NEEDED**: leaf primitives don't get L4 rows. The L3>L1 rotation is direct; no L2 intermediate is required because the BLAS-1 primitives are L1 leaves not L2 compositions (per the L2 entry's §Dependencies — the L2 layer lists `axpy` as an L1 vocabulary item it depends on, not as a standalone L2 row).
[new]: No L4 monadic vocabulary appears in the L3 signature (no `Solve`, no `modify`, no `do`-block) — `axpy` is not a calculus combinator at L4. The cohort audit (`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`) verdict for the BLAS-1 cohort at L4 is **CONFIRMED-NOT-NEEDED**: leaf primitives don't get L4 rows. The adjacent L3>L2 rotation passes through the **present** L2 floor [`axpy`](../L2/axpy.md) (cycle-043) via the firm [`axpy-body-identity`](../L3-L2/axpy-body-identity.md) L3>L2 theme — identity-in-form on the body, no wrapper rotation; onward to L1 [`axpy`](../L1/axpy.md). The L2 floor was backfilled under the foundation-first directive `l2-floor-under-l3-leaf-cohort` so the firm L3 entry rests on a *present* adjacent L2 parent (per **Identity-lowerings still require both L levels**), rather than skipping a layer to L1.
```

```edit:book/src/L3/axpy.md
[old]: L3 `axpy` lowers to L1 [`axpy`](../L1/axpy.md) via the **identity-in-form rotation on the primitive's signature shape**. The two surfaces are textually identical modulo whatever layer-coherence vocabulary differences exist (e.g., L1 uses `Tensor[N]` axis naming with bunsen-style shape contracts; L3 uses the same axis naming). The rotation does not pass through L2 because the BLAS-1 primitives are L1 leaves, not L2 compositions — the L2 layer references `axpy` by its L1 name (per `book/src/L2/krylov-step.md:96`). The cycle-010 cohort audit's verdict for the L2 candidate on `axpy` was **CONFIRMED-NOT-NEEDED-WITH-CAVEAT** (priority #17 may eventually compel L2 entries; deferred until L2 cohort grows).

A thin L3>L1 identity-in-form theme could be authored to ratify the rotation explicitly (analogous to `book/src/L3-L2/krylov-step-body-identity.md` for the krylov-step body); whether to create a `book/src/L3-L1/` directory is a structural-naming question deferred per OQ `l3-l1-directory-naming-structure-policy` (raised by the cycle-010 cohort audit). The current dispatch documents the rotation in-line at the L3 entry's "Lowers to" section, consistent with the cycle-010 `book/src/L3/krylov-step.md` precedent's treatment of its L3>L2 lowering.
[new]: L3 `axpy` lowers to the **present adjacent L2 floor** [`axpy`](../L2/axpy.md) (cycle-043) as **identity-in-form on the primitive's signature shape**, via the firm [`axpy-body-identity`](../L3-L2/axpy-body-identity.md) L3>L2 theme (identity-in-form on the body, no wrapper rotation — `axpy` is a leaf whole-tensor field operation, not a step body), and onward to L1 [`axpy`](../L1/axpy.md). The three surfaces are textually identical modulo layer-coherence vocabulary (L1 / L2 / L3 all see `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same non-law set, and the same variant-axis profile). The L2 floor is the standalone fold-member BLAS-1 leaf — landed by the cycle-043 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort` (mirroring the cycle-041 `dot` / `nrm2` / `scal` floors) — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

The **transitive** L3>L1 identity (L3>L2 ∘ L2>L1, both identity-in-form) is annotated in-line per the cycle-012 non-adjacent-identity convention (lowering directories are per-adjacent-edge only); no `book/src/L3-L1/` directory is created. The substantive rotation in the chain is the L1>L0 [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) sub-pattern A (which covers `axpy` as the β=1 specialisation of `axpby`).
```

```edit:book/src/L3/axpy.md
[old]: - `book/src/L1/axpy.md` (cycle-002 firm) — the L1 form this L3 entry rotates from. Body shape, semantics, six algebraic laws, two non-laws, variant-axis profile.
[new]: - `book/src/L2/axpy.md` (cycle-043 firm) — the present adjacent L2 floor this L3 entry lowers into via the `axpy-body-identity` theme; identity-in-form on the primitive's signature.
- `book/src/L3-L2/axpy-body-identity.md` (cycle-043 firm) — the adjacent L3>L2 body-identity theme; identity-in-form on the body, no wrapper rotation.
- `book/src/L1/axpy.md` (cycle-002 firm) — the L1 form this L3 entry transitively rotates from (L3>L2 ∘ L2>L1). Body shape, semantics, six algebraic laws, two non-laws, variant-axis profile.
```

### Job (i) — re-anchor `L3/axpby` to the present `L2/axpby` floor via `axpby-body-identity`

```edit:book/src/L3/axpby.md
[old]: lowers_to:
  - book/src/L1/axpby.md (identity-in-form rotation on the primitive's signature shape; whole-tensor in / whole-tensor out at both layers; no L2 intermediate because the BLAS-1 primitives are L1 leaves not L2 compositions)
[new]: lowers_to:
  - book/src/L2/axpby.md (present adjacent L2 floor, cycle-043; identity-in-form on the primitive's signature shape, via the `axpby-body-identity` L3>L2 theme; whole-tensor in / whole-tensor out at both layers) → book/src/L1/axpby.md (transitive L3>L1 identity in-line, L3>L2 ∘ L2>L1)
```

```edit:book/src/L3/axpby.md
[old]: No L4 monadic vocabulary; `axpby` is not a calculus combinator at L4. Per the cycle-010 cohort audit, the L4 candidate for `axpby` is **CONFIRMED-NOT-NEEDED** (leaf primitives don't get L4 rows). The L3>L1 rotation is direct; no L2 intermediate is required because `axpby` is an L1 leaf, not an L2 composition (per `book/src/L2/krylov-step.md:96` — the L2 layer references `axpby` by its L1 name).
[new]: No L4 monadic vocabulary; `axpby` is not a calculus combinator at L4. Per the cycle-010 cohort audit, the L4 candidate for `axpby` is **CONFIRMED-NOT-NEEDED** (leaf primitives don't get L4 rows). The adjacent L3>L2 rotation passes through the **present** L2 floor [`axpby`](../L2/axpby.md) (cycle-043) via the firm [`axpby-body-identity`](../L3-L2/axpby-body-identity.md) L3>L2 theme — identity-in-form on the body, no wrapper rotation; onward to L1 [`axpby`](../L1/axpby.md). The L2 floor was backfilled under the foundation-first directive `l2-floor-under-l3-leaf-cohort` so the firm L3 entry rests on a *present* adjacent L2 parent, per **Identity-lowerings still require both L levels**.
```

```edit:book/src/L3/axpby.md
[old]: L3 `axpby` lowers to L1 [`axpby`](../L1/axpby.md) via the **identity-in-form rotation on the primitive's signature shape**. The two surfaces are textually identical modulo layer-coherence vocabulary. The rotation does not pass through L2 because `axpby` is an L1 leaf, not an L2 composition.

A thin L3>L1 identity-in-form theme could be authored to ratify the rotation explicitly; whether to create a `book/src/L3-L1/` directory is a structural-naming question deferred per OQ `l3-l1-directory-naming-structure-policy` (raised by the cycle-010 cohort audit). The current dispatch documents the rotation in-line at the L3 entry's "Lowers to" section, consistent with the cycle-010 `book/src/L3/krylov-step.md` precedent.
[new]: L3 `axpby` lowers to the **present adjacent L2 floor** [`axpby`](../L2/axpby.md) (cycle-043) as **identity-in-form on the primitive's signature shape**, via the firm [`axpby-body-identity`](../L3-L2/axpby-body-identity.md) L3>L2 theme (identity-in-form on the body, no wrapper rotation — `axpby` is a leaf whole-tensor field operation, not a step body), and onward to L1 [`axpby`](../L1/axpby.md). The three surfaces are textually identical modulo layer-coherence vocabulary (L1 / L2 / L3 all see `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` with the same shape contract, the same nine algebraic laws, the same four non-laws, and the same variant-axis profile). The L2 floor is the standalone fold-member BLAS-1 leaf — landed by the cycle-043 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort` — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

The **transitive** L3>L1 identity (L3>L2 ∘ L2>L1, both identity-in-form) is annotated in-line per the cycle-012 non-adjacent-identity convention; no `book/src/L3-L1/` directory is created. The substantive rotation in the chain is the L1>L0 [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md).
```

```edit:book/src/L3/axpby.md
[old]: - `book/src/L1/axpby.md` (cycle-003 firm) — the L1 form this L3 entry rotates from. Body shape, semantics, nine algebraic laws, four non-laws, variant-axis profile.
[new]: - `book/src/L2/axpby.md` (cycle-043 firm) — the present adjacent L2 floor this L3 entry lowers into via the `axpby-body-identity` theme; identity-in-form on the primitive's signature.
- `book/src/L3-L2/axpby-body-identity.md` (cycle-043 firm) — the adjacent L3>L2 body-identity theme; identity-in-form on the body, no wrapper rotation.
- `book/src/L1/axpby.md` (cycle-003 firm) — the L1 form this L3 entry transitively rotates from (L3>L2 ∘ L2>L1). Body shape, semantics, nine algebraic laws, four non-laws, variant-axis profile.
```

### Job (i) — re-anchor `L3/axpbypcz` to the present `L2/axpbypcz` floor via `axpbypcz-body-identity`

```edit:book/src/L3/axpbypcz.md
[old]: lowers_to:
  - book/src/L1/axpbypcz.md (identity-in-form rotation on the primitive's signature shape; whole-tensor in / whole-tensor out at both layers; no L2 intermediate because the BLAS-1 primitives are L1 leaves not L2 compositions)
[new]: lowers_to:
  - book/src/L2/axpbypcz.md (present adjacent L2 floor, cycle-043 D5; identity-in-form on the primitive's signature shape, via the `axpbypcz-body-identity` L3>L2 theme; whole-tensor in / whole-tensor out at both layers) → book/src/L1/axpbypcz.md (transitive L3>L1 identity in-line, L3>L2 ∘ L2>L1)
```

```edit:book/src/L3/axpbypcz.md
[old]: No L4 monadic vocabulary; `axpbypcz` is not a calculus combinator at L4. Per the cycle-010 cohort audit, the L4 candidate for `axpbypcz` is **CONFIRMED-NOT-NEEDED**. The L3>L1 rotation is direct; no L2 intermediate is required.
[new]: No L4 monadic vocabulary; `axpbypcz` is not a calculus combinator at L4. Per the cycle-010 cohort audit, the L4 candidate for `axpbypcz` is **CONFIRMED-NOT-NEEDED**. The adjacent L3>L2 rotation passes through the **present** L2 floor [`axpbypcz`](../L2/axpbypcz.md) (cycle-043 D5) via the firm [`axpbypcz-body-identity`](../L3-L2/axpbypcz-body-identity.md) L3>L2 theme — identity-in-form on the body, no wrapper rotation; onward to L1 [`axpbypcz`](../L1/axpbypcz.md). The L2 floor was backfilled under the foundation-first directive `l2-floor-under-l3-leaf-cohort` so the firm L3 entry rests on a *present* adjacent L2 parent, per **Identity-lowerings still require both L levels**.
```

```edit:book/src/L3/axpbypcz.md
[old]: L3 `axpbypcz` lowers to L1 [`axpbypcz`](../L1/axpbypcz.md) via the **identity-in-form rotation on the primitive's signature shape**. The two surfaces are textually identical modulo layer-coherence vocabulary. The rotation does not pass through L2 because `axpbypcz` is an L1 leaf, not an L2 composition.

A thin L3>L1 identity-in-form theme could be authored to ratify the rotation explicitly; whether to create a `book/src/L3-L1/` directory is deferred per OQ `l3-l1-directory-naming-structure-policy`. The current dispatch documents the rotation in-line at the L3 entry's "Lowers to" section.
[new]: L3 `axpbypcz` lowers to the **present adjacent L2 floor** [`axpbypcz`](../L2/axpbypcz.md) (cycle-043 D5) as **identity-in-form on the primitive's signature shape**, via the firm [`axpbypcz-body-identity`](../L3-L2/axpbypcz-body-identity.md) L3>L2 theme (identity-in-form on the body, no wrapper rotation — `axpbypcz` is a leaf whole-tensor field operation, not a step body), and onward to L1 [`axpbypcz`](../L1/axpbypcz.md). The three surfaces are textually identical modulo layer-coherence vocabulary (L1 / L2 / L3 all see `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` with the same shape contract, the same twelve algebraic laws, the same four non-laws, and the same variant-axis profile). The L2 floor is the standalone fold-member BLAS-1-extended leaf — landed by the cycle-043 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort` — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

The **transitive** L3>L1 identity (L3>L2 ∘ L2>L1, both identity-in-form) is annotated in-line per the cycle-012 non-adjacent-identity convention; no `book/src/L3-L1/` directory is created. The substantive rotation in the chain is the L1>L0 [`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md).
```

```edit:book/src/L3/axpbypcz.md
[old]: - `book/src/L1/axpbypcz.md` (cycle-003 firm) — the L1 form this L3 entry rotates from. Body shape, semantics, twelve algebraic laws, four non-laws, variant-axis profile.
[new]: - `book/src/L2/axpbypcz.md` (cycle-043 D5 firm) — the present adjacent L2 floor this L3 entry lowers into via the `axpbypcz-body-identity` theme; identity-in-form on the primitive's signature.
- `book/src/L3-L2/axpbypcz-body-identity.md` (cycle-043 firm) — the adjacent L3>L2 body-identity theme; identity-in-form on the body, no wrapper rotation.
- `book/src/L1/axpbypcz.md` (cycle-003 firm) — the L1 form this L3 entry transitively rotates from (L3>L2 ∘ L2>L1). Body shape, semantics, twelve algebraic laws, four non-laws, variant-axis profile.
```

### Job (i) — re-anchor `L3/normalize` to the present `L2/normalize` floor via `normalize-body-identity`

```edit:book/src/L3/normalize.md
[old]: lowers_to:
  - book/src/L1/normalize.md (identity-in-form on the operator's signature; no L3-L2/L3-L1 theme — see Lowers-to)
[new]: lowers_to:
  - book/src/L2/normalize.md (present adjacent L2 floor, cycle-043 D10; identity-in-form on the operator's signature, via the `normalize-body-identity` L3>L2 theme; fused composite, fork-INDEPENDENT, no fold-parent) → book/src/L1/normalize.md (transitive L3>L1 identity in-line, L3>L2 ∘ L2>L1)
```

```edit:book/src/L3/normalize.md
[old]: - **Downward** to L1: `normalize` lowers to L1 [`normalize`](../L1/normalize.md) directly, with **no interposed L2 entry and no `L3-L2`/`L3-L1` theme file**. The rotation is **identity-in-form on the operator's signature** — both L1 and L3 see `normalize :: Tensor[N] -> (Scalar, Tensor[N])` with the same shape contract, the same six algebraic laws, the same partiality precondition (`x ≠ 0`), and the same single element-type variant axis. The framing differs: L1 frames `normalize` as the *mutation-rotation* image of the L0 receiver-mutating `linalg::Normalize(comm, x)` free-function idiom (the L1 surface drops the in-place rescale + the returned-by-value norm + the MPI collective folded inside `Norml2`); L3 frames the same operator as a *field operation* in the whole-tensor vocabulary that the iteration-rotation layer composes. The L2 layer hosts no standalone `normalize` entry — it is referenced from L2 compositions (the `orthogonalize` output-normalization step) but does not get a standalone L2 entry when the rotation carries no algebraic novelty; the L3>L1 hop is therefore direct, mirroring the BLAS-1 / `apply_linop` / `scal` L3>L1 discipline. The identity-in-form annotation lives in-line here, per the cycle-012 non-adjacent-identity convention (precedent: `scal`, `dot`, `reciprocal`, `elementwise_product`); no non-adjacent lowering directory is created. The substantive rotation in the chain is the firm L1>L0 [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (cycle-027), which composes the [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) no-buffer reduction with the [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A in-place rescale, plus the returned-scalar binding.
[new]: - **Downward** to L2 then L1: `normalize` lowers to the **present adjacent L2 floor** [`normalize`](../L2/normalize.md) (cycle-043 D10) via the firm [`normalize-body-identity`](../L3-L2/normalize-body-identity.md) L3>L2 theme, and onward to L1 [`normalize`](../L1/normalize.md). The rotation is **identity-in-form on the operator's signature** — L1, L2, and L3 all see `normalize :: Tensor[N] -> (Scalar, Tensor[N])` with the same shape contract, the same six algebraic laws, the same partiality precondition (`x ≠ 0`), and the same single element-type variant axis. The framing differs across layers: L1 frames `normalize` as the *mutation-rotation* image of the L0 receiver-mutating `linalg::Normalize(comm, x)` free-function idiom (the L1 surface drops the in-place rescale + the returned-by-value norm + the MPI collective folded inside `Norml2`); L2 frames it as the *fusion-rotation* floor (the fused `nrm2 ∘ scal` composite, fork-INDEPENDENT, no fold-parent, with two genuine same-layer `consumes` floors `nrm2` + `scal`); L3 frames the same operator as a *field operation* in the whole-tensor vocabulary that the iteration-rotation layer composes. The L2 floor was backfilled under the foundation-first directive `l2-floor-under-l3-leaf-cohort` so the firm L3 entry rests on a *present* adjacent L2 parent (per **Identity-lowerings still require both L levels**), rather than skipping a layer to L1; the **transitive** L3>L1 identity (L3>L2 ∘ L2>L1) is annotated in-line per the cycle-012 non-adjacent-identity convention, no non-adjacent `L3-L1/` directory is created. The substantive rotation in the chain is the firm L1>L0 [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (cycle-027), which composes the [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) no-buffer reduction with the [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A in-place rescale, plus the returned-scalar binding.
```

```edit:book/src/L3/normalize.md
[old]: L3 `normalize` lowers to L1 [`normalize`](../L1/normalize.md) as **identity-in-form on the operator's signature** — **no interposed L2 entry, no `L3-L2`/`L3-L1` theme file**. Both L1 and L3 see `normalize :: Tensor[N] -> (Scalar, Tensor[N])` with the same shape contract, the same six algebraic laws, the same non-law set (partiality, nonlinearity, IEEE-754 caveats), and the same single-orthogonal-axis variant profile (element-type). The L2 layer hosts no standalone `normalize` entry (mirroring the BLAS-1 / `apply_linop` / `scal` / `reciprocal` L2 verdict — composites whose decomposition carries no algebraic novelty are referenced from L2 compositions but do not get standalone L2 entries); the L3>L1 hop is therefore direct.

No `book/src/L3-L1/` directory exists in the artifact; per the cycle-010 `krylov-step`, cycle-011 BLAS-1, and cycle-038 `reciprocal` / `elementwise_product` precedents this entry captures the identity rotation **in-line** (per the cycle-012 meta-phase non-adjacent-identity convention — lowering directories are per-adjacent-edge only). The substantive rotation in the chain is the firm L1>L0 [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (cycle-027) — it lowers the L1 pure-functional `(β, û) = normalize(x)` into Palace's L0 in-place receiver-mutating `linalg::Normalize(comm, x)` (computing `norm = Norml2(comm, x)`, asserting `norm > 0`, rescaling `x *= 1.0/norm` in place, returning `norm` by value), composing the [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) no-buffer reduction with the [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A in-place rescale plus the returned-scalar binding. The L3>L1 hop is by contrast a layer-coherence rotation (each layer is coherent within itself), not an algebraic one.
[new]: L3 `normalize` lowers to the **present adjacent L2 floor** [`normalize`](../L2/normalize.md) (cycle-043 D10) as **identity-in-form on the operator's signature**, via the firm [`normalize-body-identity`](../L3-L2/normalize-body-identity.md) L3>L2 theme (identity-in-form on the body, no wrapper rotation — `normalize` is a fused whole-tensor composite, not a step body, and **fork-independent / fold-parent-free**: it cites its two constituent floors `nrm2` + `scal` as `consumes` same-layer dependencies, never as a fold of which it is a member), and onward to L1 [`normalize`](../L1/normalize.md). L1, L2, and L3 all see `normalize :: Tensor[N] -> (Scalar, Tensor[N])` with the same shape contract, the same six algebraic laws, the same non-law set (partiality, nonlinearity, IEEE-754 caveats), and the same single-orthogonal-axis variant profile (element-type). The L2 floor — landed by the cycle-043 D10 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort`, the fused-composite counterpart of the leaf floors `reciprocal` / `scal` — gives the firm L3 entry a *present* adjacent L2 parent, so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

No `book/src/L3-L1/` directory exists in the artifact; the **transitive** L3>L1 identity (L3>L2 ∘ L2>L1, both identity-in-form) is captured **in-line** per the cycle-012 meta-phase non-adjacent-identity convention (lowering directories are per-adjacent-edge only; precedents: cycle-010 `krylov-step`, cycle-011 BLAS-1, cycle-038 `reciprocal` / `elementwise_product`). The substantive rotation in the chain is the firm L1>L0 [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (cycle-027) — it lowers the L1 pure-functional `(β, û) = normalize(x)` into Palace's L0 in-place receiver-mutating `linalg::Normalize(comm, x)` (computing `norm = Norml2(comm, x)`, asserting `norm > 0`, rescaling `x *= 1.0/norm` in place, returning `norm` by value), composing the [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) no-buffer reduction with the [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A in-place rescale plus the returned-scalar binding. The L3>L2 and L2>L1 hops are by contrast layer-coherence rotations (each layer is coherent within itself), not algebraic ones.
```

```edit:book/src/L3/normalize.md
[old]: **L1 anchor**: [`L1/normalize`](../L1/normalize.md) (firm) — authoritative on the Palace surface details (the `linalg::Normalize` free-function template, the three consumer shapes, the returned-norm load-bearing analysis, the `normalize_B` rough-in note, the complete L0 evidence list). This L3 entry does not duplicate those details; the L3>L1 rotation is identity-in-form on the operator itself.
[new]: **L2 floor / L1 anchor**: [`L2/normalize`](../L2/normalize.md) (firm, cycle-043 D10) is the present adjacent L2 floor this L3 entry lowers into via the firm [`normalize-body-identity`](../L3-L2/normalize-body-identity.md) theme; [`L1/normalize`](../L1/normalize.md) (firm) remains authoritative on the Palace surface details (the `linalg::Normalize` free-function template, the three consumer shapes, the returned-norm load-bearing analysis, the `normalize_B` rough-in note, the complete L0 evidence list). This L3 entry does not duplicate those details; the L3>L2 and (transitive) L3>L1 rotations are identity-in-form on the operator itself.
```

```edit:book/src/L3/normalize.md
[old]: - `book/src/L1/normalize.md` (firm, cycle-026 — firm-on-positive-structure) — the L1 entry whose signature, semantics (the fused `nrm2 + scal` composite, the returned-norm load-bearing analysis), six algebraic laws, single variant axis (element-type), partiality precondition (`x ≠ 0`), and complete L0 evidence chain are transported unchanged to L3. The laws and non-laws cited above are reproduced from the L1 entry's §"Algebraic laws".
[new]: - `book/src/L2/normalize.md` (firm, cycle-043 D10) — the present adjacent L2 floor this L3 entry lowers into via the `normalize-body-identity` theme; the fusion-rotation floor of the fused `nrm2 ∘ scal` composite (fork-INDEPENDENT, no fold-parent), identity-in-form on the operator's signature.
- `book/src/L3-L2/normalize-body-identity.md` (firm, cycle-043 D10) — the adjacent L3>L2 body-identity theme; identity-in-form on the body, no wrapper rotation, no fold-parent.
- `book/src/L1/normalize.md` (firm, cycle-026 — firm-on-positive-structure) — the L1 entry whose signature, semantics (the fused `nrm2 + scal` composite, the returned-norm load-bearing analysis), six algebraic laws, single variant axis (element-type), partiality precondition (`x ≠ 0`), and complete L0 evidence chain are transported unchanged to L3 (transitively, L3>L2 ∘ L2>L1). The laws and non-laws cited above are reproduced from the L1 entry's §"Algebraic laws".
```

The §"Lifts from" stale "no L2 intermediate" claim in `normalize.md` is also re-anchored (the L4 absence is unchanged; only the L1/L2 framing firms):

```edit:book/src/L3/normalize.md
[old]: L1 `normalize` lifts to this L3 entry via the **value-thread-isomorphic** identity rotation: the L1 form's signature has no element loop exposed, no destination buffer, no MPI collective, no iteration view — exactly the properties that make it L3-native by construction. The fused composition lifts cleanly because both constituents are already firm L3-native leaves: the norm reduction [`nrm2`](./nrm2.md) is reduction-clean (no sequential obstruction) and the rescale [`scal`](./scal.md) is element-local. **This L3 entry exists for layer-coherence reasons** — a reader navigating L3 must find `normalize` defined in L3 vocabulary, not have to reach down to L1 to recover the field-operation shape.
[new]: L1 `normalize` lifts to the present L2 floor [`L2/normalize`](../L2/normalize.md) (cycle-043 D10) and onward to this L3 entry via the **value-thread-isomorphic** identity rotation: the L1 form's signature has no element loop exposed, no destination buffer, no MPI collective, no iteration view — exactly the properties that make it L2-/L3-native by construction. The fused composition lifts cleanly because both constituents are already firm L3-native leaves: the norm reduction [`nrm2`](./nrm2.md) is reduction-clean (no sequential obstruction) and the rescale [`scal`](./scal.md) is element-local. **This L3 entry exists for layer-coherence reasons** — a reader navigating L3 must find `normalize` defined in L3 vocabulary, not have to reach down to L2 / L1 to recover the field-operation shape.
```

### Job (i) — re-anchor the four L3 index dep-map rows (`book/src/L3/index.md`)

The `axpy` / `axpby` / `axpbypcz` / `normalize` rows' "Lowers to" cells still assert the direct L3>L1 hop with no L2 intermediate. Re-anchor each to the present adjacent L2 floor via the body-identity theme. (These edits also fold in the job-(ii) audit-block re-pin for the `normalize` row — `:44`→`:46`.)

```edit:book/src/L3/index.md
[old]: | [`axpy`](./axpy.md) | `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, y) -> α·x + y`) | L1 [`axpy`](../L1/axpy.md) for the L1-form anchor; concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). | L1 [`axpy`](../L1/axpy.md) via identity-in-form rotation on the primitive's signature shape (whole-tensor in / whole-tensor out at both layers); no element loop exposed. | `firm` (harvested cycle-011T234525Z; identity-lowering backfill per CLAUDE.md §Methodology invariants; closes cohort portion of OQ `l3-backfill-apply-linop-and-blas1-cohort` HIGH CONFIDENCE) |
[new]: | [`axpy`](./axpy.md) | `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, y) -> α·x + y`) | L2 floor [`axpy`](../L2/axpy.md) (present adjacent floor, cycle-043) via [`axpy-body-identity`](../L3-L2/axpy-body-identity.md); concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). | L2 [`axpy`](../L2/axpy.md) via [`axpy-body-identity`](../L3-L2/axpy-body-identity.md) (identity-in-form on the body, no wrapper rotation), then transitively L1 [`axpy`](../L1/axpy.md) (L3>L2 ∘ L2>L1 identity in-line; no `L3-L1/` directory). | `firm` (harvested cycle-011T234525Z; identity-lowering backfill per CLAUDE.md §Methodology invariants; re-anchored cycle-044 to the present L2 floor landed cycle-043 under `l2-floor-under-l3-leaf-cohort`; closes cohort portion of OQ `l3-backfill-apply-linop-and-blas1-cohort` HIGH CONFIDENCE) |
```

```edit:book/src/L3/index.md
[old]: | [`axpby`](./axpby.md) | `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, β, y) -> α·x + β·y`) | L1 [`axpby`](../L1/axpby.md); concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). Subsumes [`axpy`](./axpy.md) at L3 (β=1) — same subsumption-as-identity discipline as L1. | L1 [`axpby`](../L1/axpby.md) via identity-in-form rotation on the primitive's signature shape. | `firm` (harvested cycle-011T234525Z; identity-lowering backfill) |
[new]: | [`axpby`](./axpby.md) | `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, β, y) -> α·x + β·y`) | L2 floor [`axpby`](../L2/axpby.md) (present adjacent floor, cycle-043) via [`axpby-body-identity`](../L3-L2/axpby-body-identity.md); concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). Subsumes [`axpy`](./axpy.md) at L3 (β=1) — same subsumption-as-identity discipline as L1. | L2 [`axpby`](../L2/axpby.md) via [`axpby-body-identity`](../L3-L2/axpby-body-identity.md) (identity-in-form on the body, no wrapper rotation), then transitively L1 [`axpby`](../L1/axpby.md) (L3>L2 ∘ L2>L1 identity in-line; no `L3-L1/` directory). | `firm` (harvested cycle-011T234525Z; identity-lowering backfill; re-anchored cycle-044 to the present L2 floor landed cycle-043 under `l2-floor-under-l3-leaf-cohort`) |
```

```edit:book/src/L3/index.md
[old]: | [`axpbypcz`](./axpbypcz.md) | `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, β, y, γ, z) -> α·x + β·y + γ·z`) | L1 [`axpbypcz`](../L1/axpbypcz.md); concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). Subsumes [`axpby`](./axpby.md) at L3 (γ=0) and [`axpy`](./axpy.md) (β=1, γ=0) — same subsumption-as-identity discipline as L1. | L1 [`axpbypcz`](../L1/axpbypcz.md) via identity-in-form rotation on the primitive's signature shape. | `firm` (harvested cycle-011T234525Z; identity-lowering backfill) |
[new]: | [`axpbypcz`](./axpbypcz.md) | `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, β, y, γ, z) -> α·x + β·y + γ·z`) | L2 floor [`axpbypcz`](../L2/axpbypcz.md) (present adjacent floor, cycle-043 D5) via [`axpbypcz-body-identity`](../L3-L2/axpbypcz-body-identity.md); concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). Subsumes [`axpby`](./axpby.md) at L3 (γ=0) and [`axpy`](./axpy.md) (β=1, γ=0) — same subsumption-as-identity discipline as L1. | L2 [`axpbypcz`](../L2/axpbypcz.md) via [`axpbypcz-body-identity`](../L3-L2/axpbypcz-body-identity.md) (identity-in-form on the body, no wrapper rotation), then transitively L1 [`axpbypcz`](../L1/axpbypcz.md) (L3>L2 ∘ L2>L1 identity in-line; no `L3-L1/` directory). | `firm` (harvested cycle-011T234525Z; identity-lowering backfill; re-anchored cycle-044 to the present L2 floor landed cycle-043 under `l2-floor-under-l3-leaf-cohort`) |
```

```edit:book/src/L3/index.md
[old]: | [`normalize`](./normalize.md) | `normalize :: Tensor[N] -> (Scalar, Tensor[N])` (fused norm-then-rescale; `x -> (β, x/β)` with `β = nrm2(x)`; the returned norm is load-bearing — Arnoldi sub-diagonal / power-iteration eigenvalue estimate / NEP deflation companion-scale; **partial** at `x=0`; norm output always real). | **Same-layer L3 (fused composite, NOT a leaf)**: [`nrm2`](./nrm2.md) (the norm reduction `β`, result.0 + rescale divisor — supplies the reduction-clean / no-obstruction profile), [`scal`](./scal.md) (the rescale `û = scal(1/β, x)`, result.1 — element-local, reduction-free). Factorisation `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))` is the complete L3-internal decomposition. Concepts: (none new). L1 anchor via [`L1/normalize`](../L1/normalize.md) (identity-in-form on the operator's signature; six laws + the `x≠0` partiality precondition inherited unchanged). | L1 [`normalize`](../L1/normalize.md) directly (no interposed L2 entry, no L3-L2/L3-L1 theme — fused composite whose L1 form is L3-native by signature shape; identity-in-form annotation in-line per cycle-012 non-adjacent-identity convention). Substantive rotation is the L1>L0 [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (composing `nrm2-mutation-rotation` no-buffer reduction + `scal-mutation-rotation` sub-pattern A in-place rescale + returned-scalar binding). | `firm` (harvested cycle-039T215256Z; **sixth and FINAL (A) firm identity-in-form L3 backfill** of the cycle-036 D2 audit verdict at `book/src/L3/index.md:44` — "fused `nrm2 + scal`"; closes the c036 (A) cohort after `assemble-diagonal`+`jacobi-smoother` c037 and `reciprocal`+`elementwise_product`+`divfree-projector` c038; the only **fused composite** of the cohort — genuine same-layer `nrm2`/`scal` deps, unlike the leaf members; carries **NO obstruction** at L3 — the norm sub-step is the parallel `nrm2` reduction, the rescale is embarrassingly-parallel `scal`, no new loop-recurrence beyond the `nrm2` reduction already clean at L3; **firm-on-positive-structure** — L1 home firm-on-positive-structure, laws are syntactic identities on the `linalg::Normalize` closure, missing `test-normalize` does not gate; layer-coherence backfill per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**; OQ `l3-cohort-growth-audit-c036-verdict`) |
[new]: | [`normalize`](./normalize.md) | `normalize :: Tensor[N] -> (Scalar, Tensor[N])` (fused norm-then-rescale; `x -> (β, x/β)` with `β = nrm2(x)`; the returned norm is load-bearing — Arnoldi sub-diagonal / power-iteration eigenvalue estimate / NEP deflation companion-scale; **partial** at `x=0`; norm output always real). | **Same-layer L3 (fused composite, NOT a leaf)**: [`nrm2`](./nrm2.md) (the norm reduction `β`, result.0 + rescale divisor — supplies the reduction-clean / no-obstruction profile), [`scal`](./scal.md) (the rescale `û = scal(1/β, x)`, result.1 — element-local, reduction-free). Factorisation `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))` is the complete L3-internal decomposition. Concepts: (none new). L2 floor via [`L2/normalize`](../L2/normalize.md) (present adjacent floor, cycle-043 D10) through [`normalize-body-identity`](../L3-L2/normalize-body-identity.md); L1 anchor via [`L1/normalize`](../L1/normalize.md) (identity-in-form on the operator's signature; six laws + the `x≠0` partiality precondition inherited unchanged). | L2 [`normalize`](../L2/normalize.md) via [`normalize-body-identity`](../L3-L2/normalize-body-identity.md) (identity-in-form on the body, no wrapper rotation, fork-independent / no fold-parent), then transitively L1 [`normalize`](../L1/normalize.md) (L3>L2 ∘ L2>L1 identity in-line; no `L3-L1/` directory). Substantive rotation is the L1>L0 [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (composing `nrm2-mutation-rotation` no-buffer reduction + `scal-mutation-rotation` sub-pattern A in-place rescale + returned-scalar binding). | `firm` (harvested cycle-039T215256Z; **sixth and FINAL (A) firm identity-in-form L3 backfill** of the cycle-036 D2 audit verdict at `book/src/L3/index.md:46` — "fused `nrm2 + scal`"; re-anchored cycle-044 to the present L2 floor landed cycle-043 D10 under `l2-floor-under-l3-leaf-cohort`; closes the c036 (A) cohort after `assemble-diagonal`+`jacobi-smoother` c037 and `reciprocal`+`elementwise_product`+`divfree-projector` c038; the only **fused composite** of the cohort — genuine same-layer `nrm2`/`scal` deps, unlike the leaf members; carries **NO obstruction** at L3 — the norm sub-step is the parallel `nrm2` reduction, the rescale is embarrassingly-parallel `scal`, no new loop-recurrence beyond the `nrm2` reduction already clean at L3; **firm-on-positive-structure** — L1 home firm-on-positive-structure, laws are syntactic identities on the `linalg::Normalize` closure, missing `test-normalize` does not gate; layer-coherence backfill per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**; OQ `l3-cohort-growth-audit-c036-verdict`) |
```

---

### Job (ii) — `l3-index-audit-block-citation-drift` re-pin

Verified drift map (all confirmed by `tools/citecheck/citecheck.py --anchor` against on-disk; see §Supporting evidence):
`:39→:46`, `:41→:46`, `:44→:46` (the (A) identity-in-form verdict, now line 46);
`:47→:48` (the (B) substantive verdict, now line 48);
`:45→:47` (the (A) L1-promotion-gated matrix-weighted-norm, now line 47);
`:53→:58` (the cycle-037 "four (A) backfills remained" note, now line 58);
span `:38-43` / `:40-45` / `:43-48` → `:45-50` (the audit-block span).

#### `book/src/L3/jacobi-smoother.md`

```edit:book/src/L3/jacobi-smoother.md
[old]: This L3 entry is the **layer-coherence anchor**: a reader at L3 can find `jacobi-smoother` here, in L3 vocabulary, without having to reach down to L1 to recover the constructed-operator-gate apply, and without having to consult a consuming solver's preconditioner slot to see the gate in use. The backfill is the cycle-037 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification; the firm L3 `krylov-step` cycle-010 backfill is the codified precedent). The cycle-036 D2 cross-layer-cross-cutter audit (`book/src/L3/index.md:38-43`) classified this backfill as one of the six (A) firm identity-in-form L3 candidates, naming it the "thinnest constructed-operator gate, one `elementwise_product`" (`book/src/L3/index.md:39`).
[new]: This L3 entry is the **layer-coherence anchor**: a reader at L3 can find `jacobi-smoother` here, in L3 vocabulary, without having to reach down to L1 to recover the constructed-operator-gate apply, and without having to consult a consuming solver's preconditioner slot to see the gate in use. The backfill is the cycle-037 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification; the firm L3 `krylov-step` cycle-010 backfill is the codified precedent). The cycle-036 D2 cross-layer-cross-cutter audit (`book/src/L3/index.md:45-50`) classified this backfill as one of the six (A) firm identity-in-form L3 candidates, naming it the "thinnest constructed-operator gate, one `elementwise_product`" (`book/src/L3/index.md:46`).
```

```edit:book/src/L3/jacobi-smoother.md
[old]: This dispatch (cycle-037) is the **layer-coherence backfill** — the L3 form was previously implicit only in the L1 entry; it now has its own L3 entry per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md, cycle-009 meta-phase). It is the sixth and final (A) firm identity-in-form L3 backfill candidate the cycle-036 D2 cross-layer-cross-cutter audit named at `book/src/L3/index.md:39` ("thinnest constructed-operator gate, one `elementwise_product`"), under OQ `l3-cohort-growth-audit-c036-verdict`.
[new]: This dispatch (cycle-037) is the **layer-coherence backfill** — the L3 form was previously implicit only in the L1 entry; it now has its own L3 entry per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md, cycle-009 meta-phase). It is the sixth and final (A) firm identity-in-form L3 backfill candidate the cycle-036 D2 cross-layer-cross-cutter audit named at `book/src/L3/index.md:46` ("thinnest constructed-operator gate, one `elementwise_product`"), under OQ `l3-cohort-growth-audit-c036-verdict`.
```

```edit:book/src/L3/jacobi-smoother.md
[old]: - `book/src/L3/index.md:39` — the cycle-036 D2 cross-layer-cross-cutter audit verdict naming `jacobi-smoother` as one of the six (A) firm identity-in-form L3 backfill candidates ("thinnest constructed-operator gate, one `elementwise_product`"). This entry is the enactment.
[new]: - `book/src/L3/index.md:46` — the cycle-036 D2 cross-layer-cross-cutter audit verdict naming `jacobi-smoother` as one of the six (A) firm identity-in-form L3 backfill candidates ("thinnest constructed-operator gate, one `elementwise_product`"). This entry is the enactment.
```

#### `book/src/L3/assemble-diagonal.md`

```edit:book/src/L3/assemble-diagonal.md
[old]: This L3 entry is the **layer-coherence anchor**: a reader navigating L3 (the iteration-rotation layer that composes whole-operator and whole-tensor primitives into smoother / solver bodies) can find `assemble_diagonal` here, in L3 vocabulary, without having to reach down to L1 to recover the signature. The backfill is the cycle-037 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification), on the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit's **(A) identity-in-form** verdict (`book/src/L3/index.md:39`): "`assemble-diagonal` ... verdict YES — structurally identical to the firm `apply_linop` opaque-operator-gate precedent, with the exact-vs-approximate caveat absorbed as a representation-aware L1>L0 non-law."
[new]: This L3 entry is the **layer-coherence anchor**: a reader navigating L3 (the iteration-rotation layer that composes whole-operator and whole-tensor primitives into smoother / solver bodies) can find `assemble_diagonal` here, in L3 vocabulary, without having to reach down to L1 to recover the signature. The backfill is the cycle-037 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification), on the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit's **(A) identity-in-form** verdict (`book/src/L3/index.md:46`): "`assemble-diagonal` ... verdict YES — structurally identical to the firm `apply_linop` opaque-operator-gate precedent, with the exact-vs-approximate caveat absorbed as a representation-aware L1>L0 non-law."
```

```edit:book/src/L3/assemble-diagonal.md
[old]: This is the c036 audit's "exact-vs-approximate caveat absorbed as a representation-aware L1>L0 non-law" (`book/src/L3/index.md:39`) — at L3 it is recorded against the absorbed operator-representation axis, surfaced concretely in the L1>L0 lowering.
[new]: This is the c036 audit's "exact-vs-approximate caveat absorbed as a representation-aware L1>L0 non-law" (`book/src/L3/index.md:46`) — at L3 it is recorded against the absorbed operator-representation axis, surfaced concretely in the L1>L0 lowering.
```

```edit:book/src/L3/assemble-diagonal.md
[old]: (The c036 audit lists a candidate firm L3 `jacobi-smoother` constructed-operator gate consuming this chain — `book/src/L3/index.md:39`.)
[new]: (The c036 audit lists a candidate firm L3 `jacobi-smoother` constructed-operator gate consuming this chain — `book/src/L3/index.md:46`.)
```

```edit:book/src/L3/assemble-diagonal.md
[old]: The `reciprocal` and `elementwise_product` that complete the diagonal-preconditioner apply are themselves L3 backfill candidates per the c036 audit's (A) list (`book/src/L3/index.md:39`) — referenced here as plain text, not yet authored.
[new]: The `reciprocal` and `elementwise_product` that complete the diagonal-preconditioner apply are themselves L3 backfill candidates per the c036 audit's (A) list (`book/src/L3/index.md:46`) — now firm (cycle-038).
```

```edit:book/src/L3/assemble-diagonal.md
[old]: The pattern is well-attested via the chain: L1 firm-up (the operator-to-data primitive harvested with full L0 evidence + consuming smoother call sites + the libCEED diagonal-assembly unit test); cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit (`book/src/L3/index.md:38-43`) confirmed the **(A) identity-in-form** backfill verdict ("structurally identical to the firm `apply_linop` opaque-operator-gate precedent").
[new]: The pattern is well-attested via the chain: L1 firm-up (the operator-to-data primitive harvested with full L0 evidence + consuming smoother call sites + the libCEED diagonal-assembly unit test); cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit (`book/src/L3/index.md:45-50`) confirmed the **(A) identity-in-form** backfill verdict ("structurally identical to the firm `apply_linop` opaque-operator-gate precedent").
```

```edit:book/src/L3/assemble-diagonal.md
[old]: - `book/src/L3/index.md:38-43` — the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit; line 39 classifies `assemble-diagonal` as **(A) identity-in-form L3 backfill** ("verdict YES — structurally identical to the firm `apply_linop` opaque-operator-gate precedent, with the exact-vs-approximate caveat absorbed as a representation-aware L1>L0 non-law"). This entry is the enactment of that verdict.
[new]: - `book/src/L3/index.md:45-50` — the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit; line 46 classifies `assemble-diagonal` as **(A) identity-in-form L3 backfill** ("verdict YES — structurally identical to the firm `apply_linop` opaque-operator-gate precedent, with the exact-vs-approximate caveat absorbed as a representation-aware L1>L0 non-law"). This entry is the enactment of that verdict.
```

#### `book/src/L3/reciprocal.md`

```edit:book/src/L3/reciprocal.md
[old]: The backfill is the cycle-038 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification), on the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit's **(A) identity-in-form** verdict (`book/src/L3/index.md:41`): `reciprocal` is listed as the "elementwise self-map" member of the six firm (A) backfills, alongside the cycle-037-landed `assemble-diagonal` and `jacobi-smoother`.
[new]: The backfill is the cycle-038 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification), on the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit's **(A) identity-in-form** verdict (`book/src/L3/index.md:46`): `reciprocal` is listed as the "elementwise self-map" member of the six firm (A) backfills, alongside the cycle-037-landed `assemble-diagonal` and `jacobi-smoother`.
```

```edit:book/src/L3/reciprocal.md
[old]: - `elementwise_product` — the binary elementwise multiply (`(x, y) -> x ⊙ y`); an **(A) firm L3 backfill candidate** per the cycle-036 D2 audit (`book/src/L3/index.md:41`), not yet authored at L3 — referenced here as plain text. The two together — `reciprocal` and `elementwise_product` — complete the diagonal-preconditioner-apply chain `assemble_diagonal → reciprocal → elementwise_product` that [`assemble-diagonal`](./assemble-diagonal.md) §Dependencies and [`jacobi-smoother`](./jacobi-smoother.md) name.
[new]: - `elementwise_product` — the binary elementwise multiply (`(x, y) -> x ⊙ y`); an **(A) firm L3 backfill candidate** per the cycle-036 D2 audit (`book/src/L3/index.md:46`), now firm (cycle-038). The two together — `reciprocal` and `elementwise_product` — complete the diagonal-preconditioner-apply chain `assemble_diagonal → reciprocal → elementwise_product` that [`assemble-diagonal`](./assemble-diagonal.md) §Dependencies and [`jacobi-smoother`](./jacobi-smoother.md) name.
```

```edit:book/src/L3/reciprocal.md
[old]: The pattern is well-attested via the chain: L1 firm-up (the elementwise leaf harvested with full L0 evidence — the complex kernel read in full + the consumer call sites); cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit (`book/src/L3/index.md:40-45`) classified `reciprocal` as an **(A) identity-in-form** backfill ("elementwise self-map", line 41). This dispatch (cycle-038 D1) is the **layer-coherence backfill** — the L3 form was previously implicit in the diagonal-preconditioner-apply chain consumed by the smoother bodies; it now has its own L3 entry per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification). It follows the cycle-037-landed `assemble-diagonal` and `jacobi-smoother` (A)-backfills on the same diagonal-preconditioner-apply chain.
[new]: The pattern is well-attested via the chain: L1 firm-up (the elementwise leaf harvested with full L0 evidence — the complex kernel read in full + the consumer call sites); cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit (`book/src/L3/index.md:45-50`) classified `reciprocal` as an **(A) identity-in-form** backfill ("elementwise self-map", line 46). This dispatch (cycle-038 D1) is the **layer-coherence backfill** — the L3 form was previously implicit in the diagonal-preconditioner-apply chain consumed by the smoother bodies; it now has its own L3 entry per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification). It follows the cycle-037-landed `assemble-diagonal` and `jacobi-smoother` (A)-backfills on the same diagonal-preconditioner-apply chain.
```

```edit:book/src/L3/reciprocal.md
[old]: - `book/src/L3/index.md:40-45` — the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit; line 41 lists `reciprocal` ("elementwise self-map") among the six **(A) identity-in-form** L3 backfills. This entry is the enactment of that verdict.
[new]: - `book/src/L3/index.md:45-50` — the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit; line 46 lists `reciprocal` ("elementwise self-map") among the six **(A) identity-in-form** L3 backfills. This entry is the enactment of that verdict.
```

#### `book/src/L3/elementwise_product.md`

```edit:book/src/L3/elementwise_product.md
[old]: The backfill is the cycle-038 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification), on the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit's **(A) identity-in-form** verdict (`book/src/L3/index.md:41`): "`elementwise_product` (Hadamard binary)" listed among the six (A) firm backfill candidates, four of which (`reciprocal`, `elementwise_product`, `normalize`, `divfree-projector`) remained after the cycle-037 `assemble-diagonal` + `jacobi-smoother` landings (`book/src/L3/index.md:53`).
[new]: The backfill is the cycle-038 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification), on the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit's **(A) identity-in-form** verdict (`book/src/L3/index.md:46`): "`elementwise_product` (Hadamard binary)" listed among the six (A) firm backfill candidates, four of which (`reciprocal`, `elementwise_product`, `normalize`, `divfree-projector`) remained after the cycle-037 `assemble-diagonal` + `jacobi-smoother` landings (`book/src/L3/index.md:58`).
```

```edit:book/src/L3/elementwise_product.md
[old]: The pattern is well-attested via the chain: L1 firm-up (the Hadamard binary primitive harvested with full L0 evidence: the canonical operator-action site, the conjugate variant, the consumer duplicate, the absent free-function symbol); cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit (`book/src/L3/index.md:40-45`) classified `elementwise_product` as an **(A) identity-in-form** backfill ("Hadamard binary", `book/src/L3/index.md:41`); cycle-037 landed the first two of the six (A) backfills (`assemble-diagonal`, `jacobi-smoother`), leaving `reciprocal`, `elementwise_product`, `normalize`, `divfree-projector` (`book/src/L3/index.md:53`).
[new]: The pattern is well-attested via the chain: L1 firm-up (the Hadamard binary primitive harvested with full L0 evidence: the canonical operator-action site, the conjugate variant, the consumer duplicate, the absent free-function symbol); cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit (`book/src/L3/index.md:45-50`) classified `elementwise_product` as an **(A) identity-in-form** backfill ("Hadamard binary", `book/src/L3/index.md:46`); cycle-037 landed the first two of the six (A) backfills (`assemble-diagonal`, `jacobi-smoother`), leaving `reciprocal`, `elementwise_product`, `normalize`, `divfree-projector` (`book/src/L3/index.md:58`).
```

```edit:book/src/L3/elementwise_product.md
[old]: - `book/src/L3/index.md:41` — the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit; lists `elementwise_product` ("Hadamard binary") among the six **(A) identity-in-form L3 backfill candidates**. `book/src/L3/index.md:53` — the cycle-037 status note recording that four of the six (A) backfills remain (`reciprocal`, `elementwise_product`, `normalize`, `divfree-projector`) after the `assemble-diagonal` + `jacobi-smoother` landings. This entry is the enactment of that verdict for `elementwise_product`.
[new]: - `book/src/L3/index.md:46` — the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit; lists `elementwise_product` ("Hadamard binary") among the six **(A) identity-in-form L3 backfill candidates**. `book/src/L3/index.md:58` — the cycle-037 status note recording that four of the six (A) backfills remain (`reciprocal`, `elementwise_product`, `normalize`, `divfree-projector`) after the `assemble-diagonal` + `jacobi-smoother` landings. This entry is the enactment of that verdict for `elementwise_product`.
```

#### `book/src/L3/divfree-projector.md`

```edit:book/src/L3/divfree-projector.md
[old]: constructed-operator-gate siblings). The cycle-036 D2 cross-layer-cross-cutter audit
(`book/src/L3/index.md:41`) classified this backfill as one of the six (A) firm
identity-in-form L3 candidates, naming it "constructed-operator gate, like firm-L3
`ksp_solve`".
[new]: constructed-operator-gate siblings). The cycle-036 D2 cross-layer-cross-cutter audit
(`book/src/L3/index.md:46`) classified this backfill as one of the six (A) firm
identity-in-form L3 candidates, naming it "constructed-operator gate, like firm-L3
`ksp_solve`".
```

```edit:book/src/L3/divfree-projector.md
[old]: candidates the cycle-036 D2 cross-layer-cross-cutter audit named at
`book/src/L3/index.md:41` ("constructed-operator gate, like firm-L3 `ksp_solve`"), under
OQ `l3-cohort-growth-audit-c036-verdict`.
[new]: candidates the cycle-036 D2 cross-layer-cross-cutter audit named at
`book/src/L3/index.md:46` ("constructed-operator gate, like firm-L3 `ksp_solve`"), under
OQ `l3-cohort-growth-audit-c036-verdict`.
```

```edit:book/src/L3/divfree-projector.md
[old]: - `book/src/L3/index.md:41` — the cycle-036 D2 cross-layer-cross-cutter audit verdict
  naming `divfree-projector` as one of the six (A) firm identity-in-form L3 backfill
  candidates ("constructed-operator gate, like firm-L3 `ksp_solve`"). This entry is the
[new]: - `book/src/L3/index.md:46` — the cycle-036 D2 cross-layer-cross-cutter audit verdict
  naming `divfree-projector` as one of the six (A) firm identity-in-form L3 backfill
  candidates ("constructed-operator gate, like firm-L3 `ksp_solve`"). This entry is the
```

#### `book/src/L3/orthogonalize.md`

```edit:book/src/L3/orthogonalize.md
[old]: prediction enacted (`book/src/L3/index.md:47`: "MGS variant has sequential-obstruction at L3
[new]: prediction enacted (`book/src/L3/index.md:48`: "MGS variant has sequential-obstruction at L3
```

```edit:book/src/L3/orthogonalize.md
[old]:   verdict (B) at `book/src/L3/index.md:47`: "`orthogonalize` (MGS variant has
[new]:   verdict (B) at `book/src/L3/index.md:48`: "`orthogonalize` (MGS variant has
```

#### `book/src/L3/normalize.md` (audit-block re-pin — distinct from the job-(i) edits above)

```edit:book/src/L3/normalize.md
[old]: The backfill is the cycle-039 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification), on the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit's **(A) identity-in-form** verdict (`book/src/L3/index.md:44`): "`normalize` (fused `nrm2 + scal`)" listed among the six (A) firm backfill candidates.
[new]: The backfill is the cycle-039 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification), on the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit's **(A) identity-in-form** verdict (`book/src/L3/index.md:46`): "`normalize` (fused `nrm2 + scal`)" listed among the six (A) firm backfill candidates.
```

```edit:book/src/L3/normalize.md
[old]: `matrix-weighted-norm` is one of the two "(A) L1-promotion-gated" operators the c036 D2 audit explicitly held back from L3 dispatch until L1 promotes (`book/src/L3/index.md:45`); `normalize_B` rides the same gate.
[new]: `matrix-weighted-norm` is one of the two "(A) L1-promotion-gated" operators the c036 D2 audit explicitly held back from L3 dispatch until L1 promotes (`book/src/L3/index.md:47`); `normalize_B` rides the same gate.
```

```edit:book/src/L3/normalize.md
[old]: cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit (`book/src/L3/index.md:43-48`) classified `normalize` as an **(A) identity-in-form** backfill ("fused `nrm2 + scal`", line 44).
[new]: cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit (`book/src/L3/index.md:45-50`) classified `normalize` as an **(A) identity-in-form** backfill ("fused `nrm2 + scal`", line 46).
```

```edit:book/src/L3/normalize.md
[old]: - `book/src/L3/index.md:43-48` — the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit; line 44 lists `normalize` ("fused `nrm2 + scal`") among the six **(A) identity-in-form** L3 backfills. This entry is the enactment (and cohort-closer) of that verdict.
[new]: - `book/src/L3/index.md:45-50` — the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit; line 46 lists `normalize` ("fused `nrm2 + scal`") among the six **(A) identity-in-form** L3 backfills. This entry is the enactment (and cohort-closer) of that verdict.
```

#### `book/src/L3/index.md` (self-referential audit-block citations in dep-map rows + working-notes)

The `reciprocal` / `elementwise_product` / `divfree-projector` dep-map rows cite the (A) verdict at the OLD `:41`; the orthogonalize row at the OLD `:47`. Re-pin to `:46` / `:48`. (The `assemble-diagonal` row `:23` and `jacobi-smoother` row `:33` already cite `:46` correctly — no edit. The working-notes c037/c039 bullets at `:58`/`:60` cite `:46`/`:44` — the `:44` references re-pin to `:46`.)

```edit:book/src/L3/index.md
[old]: enacts the cycle-036 D2 L3-cohort-growth audit **(A) identity-in-form** verdict at `book/src/L3/index.md:41` — "elementwise self-map"; the `reciprocal` step of the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner-apply chain
[new]: enacts the cycle-036 D2 L3-cohort-growth audit **(A) identity-in-form** verdict at `book/src/L3/index.md:46` — "elementwise self-map"; the `reciprocal` step of the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner-apply chain
```

```edit:book/src/L3/index.md
[old]: enacts the cycle-036 D2 L3-cohort-growth audit **(A) identity-in-form** verdict at `book/src/L3/index.md:41` — "Hadamard binary"; **carries NO obstruction** at L3
[new]: enacts the cycle-036 D2 L3-cohort-growth audit **(A) identity-in-form** verdict at `book/src/L3/index.md:46` — "Hadamard binary"; **carries NO obstruction** at L3
```

```edit:book/src/L3/index.md
[old]: **(A) firm identity-in-form L3 backfill** of the cycle-036 D2 audit verdict at `book/src/L3/index.md:41`; constructed-operator gate like firm-L3 `ksp_solve` — but **obstruction-carrying BY REFERENCE**
[new]: **(A) firm identity-in-form L3 backfill** of the cycle-036 D2 audit verdict at `book/src/L3/index.md:46`; constructed-operator gate like firm-L3 `ksp_solve` — but **obstruction-carrying BY REFERENCE**
```

```edit:book/src/L3/index.md
[old]: the substantive **(B)** member of the cycle-036 D2 audit verdict at `book/src/L3/index.md:47`; the per-step body lifts whole-tensor for all variants
[new]: the substantive **(B)** member of the cycle-036 D2 audit verdict at `book/src/L3/index.md:48`; the per-step body lifts whole-tensor for all variants
```

```edit:book/src/L3/index.md
[old]: The three are (A) firm identity-in-form backfills of the cycle-036 D2 audit verdict (`book/src/L3/index.md:44`). `divfree-projector`'s distinguishing fact:
[new]: The three are (A) firm identity-in-form backfills of the cycle-036 D2 audit verdict (`book/src/L3/index.md:46`). `divfree-projector`'s distinguishing fact:
```

```edit:book/src/L3/index.md
[old]: (the fused `nrm2 + scal` whole-tensor self-map) lands firm cycle-039, the **sixth and final (A) identity-in-form backfill** of the cycle-036 D2 audit verdict (`book/src/L3/index.md:44`), closing the **c036 (A) cohort at 6-of-6**
[new]: (the fused `nrm2 + scal` whole-tensor self-map) lands firm cycle-039, the **sixth and final (A) identity-in-form backfill** of the cycle-036 D2 audit verdict (`book/src/L3/index.md:46`), closing the **c036 (A) cohort at 6-of-6**
```

```edit:book/src/L3/index.md
[old]: the **first (B) substantive member** of the cycle-036 D2 audit verdict (`book/src/L3/index.md:47`) to land — distinct from the six (A) identity-in-form backfills (closed c039).
[new]: the **first (B) substantive member** of the cycle-036 D2 audit verdict (`book/src/L3/index.md:48`) to land — distinct from the six (A) identity-in-form backfills (closed c039).
```

---

### Job (iii) — directive-slug prose rename `l2-floor-under-l3-blas1-cohort` → `l2-floor-under-l3-leaf-cohort`

Pure mechanical prose string rename (the ratified directive name). 25 occurrences across 12 files. `replace_all` semantics — every occurrence of the literal `l2-floor-under-l3-blas1-cohort` in each file's prose becomes `l2-floor-under-l3-leaf-cohort`. (No slug/filename changes — those were renamed in c043.) Per-file replace-all:

```edit:book/src/L2/dot.md
[replace-all]: l2-floor-under-l3-blas1-cohort
[with]: l2-floor-under-l3-leaf-cohort
```

```edit:book/src/L2/scal.md
[replace-all]: l2-floor-under-l3-blas1-cohort
[with]: l2-floor-under-l3-leaf-cohort
```

```edit:book/src/L2/axpbypcz.md
[replace-all]: l2-floor-under-l3-blas1-cohort
[with]: l2-floor-under-l3-leaf-cohort
```

```edit:book/src/L2/assemble-diagonal.md
[replace-all]: l2-floor-under-l3-blas1-cohort
[with]: l2-floor-under-l3-leaf-cohort
```

```edit:book/src/L3/assemble-diagonal.md
[replace-all]: l2-floor-under-l3-blas1-cohort
[with]: l2-floor-under-l3-leaf-cohort
```

```edit:book/src/L2/elementwise_product.md
[replace-all]: l2-floor-under-l3-blas1-cohort
[with]: l2-floor-under-l3-leaf-cohort
```

```edit:book/src/L3/reciprocal.md
[replace-all]: l2-floor-under-l3-blas1-cohort
[with]: l2-floor-under-l3-leaf-cohort
```

```edit:book/src/L2/nrm2.md
[replace-all]: l2-floor-under-l3-blas1-cohort
[with]: l2-floor-under-l3-leaf-cohort
```

```edit:book/src/L2/reciprocal.md
[replace-all]: l2-floor-under-l3-blas1-cohort
[with]: l2-floor-under-l3-leaf-cohort
```

```edit:book/src/L3/elementwise_product.md
[replace-all]: l2-floor-under-l3-blas1-cohort
[with]: l2-floor-under-l3-leaf-cohort
```

```edit:book/src/L2-L1/nrm2-leaf-identity.md
[replace-all]: l2-floor-under-l3-blas1-cohort
[with]: l2-floor-under-l3-leaf-cohort
```

```edit:book/src/L3-L2/nrm2-body-identity.md
[replace-all]: l2-floor-under-l3-blas1-cohort
[with]: l2-floor-under-l3-leaf-cohort
```

Note: `book/src/L2/assemble-diagonal.md:25` carries the phrase "directive `l2-floor-under-l3-blas1-cohort` (extended this cycle from the BLAS-1 leaf …)". The replace-all renames the slug; the surrounding "extended … from the BLAS-1 leaf cohort to the …" prose is still accurate (the leaf-cohort directive name now matches the broadened scope) and is left unchanged — a bounded rename, not a re-architecture.

---

## Discipline notes

- **Job (i) is a structural re-anchor, not authorship.** The four L3 entries stay `firm`; their
  signatures, laws, variant axes, and semantics are unchanged. Only the *lowering route* changes:
  `direct L3>L1` → `L3>L2 (via body-identity theme) then transitive L3>L1 in-line`. This is exactly the
  precedent already enacted on the sibling entries in c042/c043 (`assemble-diagonal.md:130`,
  `reciprocal.md:131`, `elementwise_product.md:149`, which already read "the **present adjacent L2
  floor** … via the `*-body-identity` L3>L2 theme"). The high→low discipline is preserved: LHS is the
  L3 form, RHS is the L2/L1 form, prose narrates the rewrite forward (L3 into L2 into L1). The
  cycle-012 non-adjacent-identity nuance is honored — the *adjacent* L3>L2 edge goes through the firm
  body-identity theme (a real adjacent-edge theme file now exists), while the *transitive* L3>L1
  identity stays in-line and no `L3-L1/` directory is created.

- **Body-identity theme vocabulary matched to the firm themes on disk.** I transcribed the framing
  from the four firm `L3-L2/*-body-identity.md` headers: "identity-in-form on the body, no wrapper
  rotation", "leaf whole-tensor field operation, not a step body" (axp*), and for `normalize` the
  "fused-composite, fork-INDEPENDENT, no fold-parent, two genuine `consumes` floors (`nrm2`+`scal`)"
  framing (`normalize-body-identity.md` header + `L2/normalize.md:39`). No new content invented.

- **Job (ii) is a citation re-anchor — the deliverable IS the citation.** Every re-pinned
  `index.md:NN` target was self-verified with `tools/citecheck/citecheck.py --anchor` against on-disk
  (not codemap — these are book/ markdown, read directly). The drift is uniform: the audit block moved
  +5 to +7 lines from its old position as the working-notes consolidated across c037-c040. Mapping:
  the (A) identity-in-form verdict 41/44/39 → **46**; the (A) L1-promotion-gated 45 → **47**; the (B)
  substantive 47 → **48**; the cycle-037 "four remain" note 53 → **58**; the audit-block span
  38-43/40-45/43-48 → **45-50**.

- **Bounded prose-correctness touch inside job (ii) re-anchors (recorded per the lifter scope-boundary
  rule).** Two re-anchored sentences carried a now-false tense ("not yet authored at L3" /
  "referenced here as plain text") for `reciprocal` / `elementwise_product`, which BOTH became firm at
  cycle-038. While re-pinning the drifted `:41`→`:46` citation on `assemble-diagonal.md:94` and
  `reciprocal.md:92` I corrected the stale "not yet authored" clause to "now firm (cycle-038)". This
  is directly supported by the on-disk firm entries `book/src/L3/reciprocal.md` and
  `book/src/L3/elementwise_product.md` (both `firmness: firm`), is bounded (a wrong tense-claim on an
  authored sibling, not a decomposition change), and is recorded here. NOT a re-architecture.

- **Job (iii) is a pure mechanical string rename.** The slug `l2-floor-under-l3-blas1-cohort` was
  ratified to `l2-floor-under-l3-leaf-cohort` (the leaf-cohort name; the directive broadened from the
  BLAS-1-leaf cohort to all leaf/fused-composite floors). Slugs/filenames were renamed in c043; this
  closes the residual *prose* occurrences. No semantic change.

## Supporting evidence

- citecheck verification of the audit-block targets (run this dispatch, against on-disk book/):
  - `index.md:46` ✓ anchor `(A) Identity-in-form`; `:41`/`:44`/`:39` → DRIFT, suggested `:46`.
  - `index.md:48` ✓ anchor `(B) Substantive`; `:47` → DRIFT, suggested `:48`.
  - `index.md:47` ✓ anchor `(A) L1-promotion-gated` / `matrix-weighted-norm`; `:45` → DRIFT, suggested `:47`.
  - `index.md:58` ✓ anchor `Four of the six (A) backfills remained after cycle-037`; `:53` → DRIFT, suggested `:58`.
  - `index.md:45` ✓ anchor `Cohort growth candidates audit` (audit-block header / span start).
  - `index.md:46` ✓ anchor `jacobi-smoother` (the (A) list names it on the same line as the verdict).
- Present L2 floors + body-identity themes (job i targets), all `firm` on disk:
  `book/src/L2/{axpy,axpby,axpbypcz,normalize}.md`,
  `book/src/L3-L2/{axpy-body-identity,axpby-body-identity,axpbypcz-body-identity,normalize-body-identity}.md`.
- Sibling precedent already routing L3>L2-via-body-identity: `book/src/L3/assemble-diagonal.md:130`,
  `book/src/L3/reciprocal.md:131`, `book/src/L3/elementwise_product.md:149`.
- L2 floor cycle attributions: `L2/axpy.md:70` (axpy floored this cycle, scal c041), `L2/axpby.md:328`
  (cycle-043 D4), `L2/axpbypcz.md` (cycle-043 D5), `L2/normalize.md:39` (cycle-043 D10, fork-independent
  composite-with-no-fold-parent).
- Stale-slug grep (job iii input): 25 occurrences of `l2-floor-under-l3-blas1-cohort` across 12 files
  (`L2/{dot,scal,axpbypcz,assemble-diagonal,elementwise_product,nrm2,reciprocal}.md`,
  `L3/{assemble-diagonal,reciprocal,elementwise_product}.md`, `L2-L1/nrm2-leaf-identity.md`,
  `L3-L2/nrm2-body-identity.md`).

## Open questions / caveats

- **OQ (carry-forward closure note): `l3-leaf-cohort-l2-floor-reanchor-deferred-from-c043`.** The four
  L3 entries' `lowers_to:` / §Downward / §Lowers-to "no L2 intermediate" assertions were stale the
  moment the c043 L2 floors landed — ideally the re-anchor would have ridden the c043 L2-floor
  dispatch. This dispatch closes the gap; recording it so future L2-floor backfills schedule the
  matching L3-entry re-anchor in the SAME cycle (integrator-per-report or a same-cycle lifter), rather
  than leaving a cross-cycle stale-assertion window. (Suggest the cycle-planner treat "L2 floor lands
  under L_n entry X" as implying "re-anchor L_{n+1}/X §Lowers-to" in the same plan.)

- **No abstractor reread needed.** The firmed-up L2 floors' signatures are identical-in-form to the L3
  signatures (verified: `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` etc. unchanged across
  L1/L2/L3; `normalize :: Tensor[N] -> (Scalar, Tensor[N])` unchanged). The body-identity themes are
  `firm` and use the established `krylov-step-body-identity`-derived framing. The re-anchor is pure
  rewriting — no LHS/RHS shape change, no notation-convention shift, no decomposition change.

- **Scope-bounding honored.** Per the dispatch's "bound it" instruction, job (ii) re-pins ONLY the
  concrete drifted audit-block self-citations (`index.md:NN` referencing the cycle-036 D2 audit block
  and the cycle-037 "four remain" note). I did NOT expand into other L3-entry citations (e.g. the
  `index.md:13` vocabulary-inventory references, which are NOT drifted — line 13 still carries the
  field-operation inventory), nor into unrelated `palace/*` source-line audits. The `index.md:23`
  (assemble-diagonal row) and `index.md:33` (jacobi-smoother row) already cite `:46` correctly — left
  untouched.

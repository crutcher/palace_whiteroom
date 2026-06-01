---
agent: lifter
invoked_at: 2026-06-01T195100Z
scope: L3>L2 + L2>L1 theme demotion — normalize degenerate identity-in-named-terms pair → in-line notes
status: integrated
integrated_at: 2026-06-01T222000Z
integration_commit: 6985e03
integration_notes: APPLIED clean (cycle-050 D6, CLEAN non-fold demotion). DELETED normalize-body-identity (L3>L2) + normalize-leaf-identity (L2>L1) OUTRIGHT (so the D3/D4/D5 de-link survivors inside them vanished as predicted); folded the fused-composite nrm2∘scal identity + linalg::Normalize vector.hpp:262-270 anchor (transitively via §Evidence, bare-path not reference-prefixed) into in-line §"Downward to L2"/§"Downward to L1" notes on L3/L2 normalize; SUMMARY rows + index rows/bullets removed; L3/index normalize-row links re-anchored. CONSTITUENT BOUNDARY HELD — no nrm2/scal entry or theme touched (the constituent re-expression is c051 fold-family work). NO operator-chapter deletion (fused composite, fork-INDEPENDENT no fold-parent). 2 OQs promoted (1 d7-count-reconciliation RESOLVED by D7; 1 planner-routed L2/normalize c044-staleness now doubly-stale). Build-relevant yes. refactor-pass ENACTMENT under the 2026-06-01 VOCABULARY-SHIFT REDIRECT.
inputs:
  - book/src/L3-L2/normalize-body-identity.md (DELETE)
  - book/src/L2-L1/normalize-leaf-identity.md (DELETE)
  - book/src/L3/normalize.md (add §"Downward to L2" in-line note; re-anchor)
  - book/src/L2/normalize.md (add §"Downward to L1" in-line note; re-anchor)
  - book/src/SUMMARY.md (remove 2 lines)
  - book/src/L3-L2/index.md (remove row + cohort-log bullet; tally → D7)
  - book/src/L2-L1/index.md (remove row + cohort-log bullet; tally → D7)
  - book/src/L3/index.md (re-anchor theme-link in normalize row)
---

# CYCLE: Demote `normalize` degenerate theme pair to in-line notes

## Summary

`normalize` is a fused composite (`nrm2 ∘ scal`, returning the load-bearing norm alongside the
unit vector). Its two adjacent-edge lowering themes — `L3-L2/normalize-body-identity.md` and
`L2-L1/normalize-leaf-identity.md` — are **degenerate identity-in-named-terms lowerings**: each is
"identity on the operator's signature, identity on all six laws, identity on the single variant axis,
identity on the partiality precondition," with **no vocabulary shift** across the edge (the same
`normalize :: Tensor[N] -> (Scalar, Tensor[N])` and the same law-6 factorisation at all three layers).
Per the 2026-06-01 VOCABULARY-SHIFT REDIRECT (CLAUDE.md §Methodology invariants ⟢; the cycle-049 D3
worklist classified this pair DEMOTE-to-inline), a degenerate identity-in-named-terms theme is a smell:
the dedicated `-body-identity` / `-leaf-identity` chapters carry no translation, only restatement of the
two endpoints. This dispatch demotes both to **in-line §"Downward to L2" / §"Downward to L1" notes** on
the `normalize` L3 and L2 entries, deletes the two theme files, removes their `SUMMARY.md` lines, removes
their `L3-L2`/`L2-L1` index theme-rows + cohort-log bullets, and re-anchors the inbound links in
`L3/index.md` and the two `normalize` entries. `normalize` is **NOT a fold member** (codomain
`(Scalar, Tensor[N])` is neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`) and has **no fold-parent**,
so this is a **clean demotion — the entry stays a standalone L3/L2 chapter, no collapse-into-fold**. Per
the dispatch directive, the constituent references to `nrm2`/`scal` inside the `normalize` body are left
exactly as-is (their combinator re-expression is the HELD fold-family cycle-051 work), and the
**consolidated index tallies are DEFERRED to D7** (this report edits only the row-level + bullet-level
content; the cohort-count integers are flagged for D7 below).

## Proposed changes

### 1. Delete the two degenerate theme files

```delete:book/src/L3-L2/normalize-body-identity.md
```

```delete:book/src/L2-L1/normalize-leaf-identity.md
```

### 2. `book/src/L3/normalize.md` — frontmatter + §Context + §"Downward to L2" in-line note + re-anchors

**2a. Frontmatter `lowers_to`** — drop the `normalize-body-identity` theme reference; the L3>L2 hop is now an in-line identity note (no theme file), still naming the present adjacent L2 floor.

```edit:book/src/L3/normalize.md
[old]: lowers_to:
  - book/src/L2/normalize.md (present adjacent L2 floor, cycle-043 D10; identity-in-form on the operator's signature, via the `normalize-body-identity` L3>L2 theme; fused composite, fork-INDEPENDENT, no fold-parent) → book/src/L1/normalize.md (transitive L3>L1 identity in-line, L3>L2 ∘ L2>L1)
[new]: lowers_to:
  - book/src/L2/normalize.md (present adjacent L2 floor, cycle-043 D10; identity-in-form on the operator's signature — degenerate identity-in-named-terms, recorded as an in-line §"Downward to L2" note rather than a dedicated theme; fused composite, fork-INDEPENDENT, no fold-parent) → book/src/L1/normalize.md (transitive L3>L1 identity in-line, L3>L2 ∘ L2>L1)
```

**2b. §Context "Downward" bullet (line 27)** — replace the theme-link with the in-line identity description.

```edit:book/src/L3/normalize.md
[old]: - **Downward** to L2 then L1: `normalize` lowers to the **present adjacent L2 floor** [`normalize`](../L2/normalize.md) (cycle-043 D10) via the firm [`normalize-body-identity`](../L3-L2/normalize-body-identity.md) L3>L2 theme, and onward to L1 [`normalize`](../L1/normalize.md). The rotation is **identity-in-form on the operator's signature** — L1, L2, and L3 all see `normalize :: Tensor[N] -> (Scalar, Tensor[N])` with the same shape contract, the same six algebraic laws, the same partiality precondition (`x ≠ 0`), and the same single element-type variant axis. The framing differs across layers: L1 frames `normalize` as the *mutation-rotation* image of the L0 receiver-mutating `linalg::Normalize(comm, x)` free-function idiom (the L1 surface drops the in-place rescale + the returned-by-value norm + the MPI collective folded inside `Norml2`); L2 frames it as the *fusion-rotation* floor (the fused `nrm2 ∘ scal` composite, fork-INDEPENDENT, no fold-parent, with two genuine same-layer `consumes` floors `nrm2` + `scal`); L3 frames the same operator as a *field operation* in the whole-tensor vocabulary that the iteration-rotation layer composes. The L2 floor was backfilled under the foundation-first directive `l2-floor-under-l3-leaf-cohort` so the firm L3 entry rests on a *present* adjacent L2 parent (per **Identity-lowerings still require both L levels**), rather than skipping a layer to L1; the **transitive** L3>L1 identity (L3>L2 ∘ L2>L1) is annotated in-line per the cycle-012 non-adjacent-identity convention, no non-adjacent `L3-L1/` directory is created. The substantive rotation in the chain is the firm L1>L0 [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (cycle-027), which composes the [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) no-buffer reduction with the [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A in-place rescale, plus the returned-scalar binding.
[new]: - **Downward** to L2 then L1: `normalize` lowers to the **present adjacent L2 floor** [`normalize`](../L2/normalize.md) (cycle-043 D10) and onward to L1 [`normalize`](../L1/normalize.md). The L3>L2 hop is a **degenerate identity-in-named-terms lowering** — no vocabulary shift across the edge — so it is recorded as the in-line §"Downward to L2" note below rather than a dedicated `L3-L2/` theme chapter (the `normalize-body-identity` theme that previously stood for it was demoted to this note under the 2026-06-01 VOCABULARY-SHIFT REDIRECT, cycle-050; CLAUDE.md §Methodology invariants ⟢). The rotation is **identity-in-form on the operator's signature** — L1, L2, and L3 all see `normalize :: Tensor[N] -> (Scalar, Tensor[N])` with the same shape contract, the same six algebraic laws, the same partiality precondition (`x ≠ 0`), and the same single element-type variant axis. The framing differs across layers: L1 frames `normalize` as the *mutation-rotation* image of the L0 receiver-mutating `linalg::Normalize(comm, x)` free-function idiom (the L1 surface drops the in-place rescale + the returned-by-value norm + the MPI collective folded inside `Norml2`); L2 frames it as the *fusion-rotation* floor (the fused `nrm2 ∘ scal` composite, fork-INDEPENDENT, no fold-parent, with two genuine same-layer `consumes` floors `nrm2` + `scal`); L3 frames the same operator as a *field operation* in the whole-tensor vocabulary that the iteration-rotation layer composes. The L2 floor was backfilled under the foundation-first directive `l2-floor-under-l3-leaf-cohort` so the firm L3 entry rests on a *present* adjacent L2 parent (per **Identity-lowerings still require both L levels**), rather than skipping a layer to L1; the **transitive** L3>L1 identity (L3>L2 ∘ L2>L1) is annotated in-line per the cycle-012 non-adjacent-identity convention, no non-adjacent `L3-L1/` directory is created. The substantive rotation in the chain is the firm L1>L0 [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (cycle-027), which composes the [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) no-buffer reduction with the [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A in-place rescale, plus the returned-scalar binding.
```

**2c. §"Lowers to" (lines 129–135)** — replace the two paragraphs (which were anchored on the `normalize-body-identity` theme link) with the in-line §"Downward to L2" note. The composite identity (no vocabulary shift) is described in full; the substantive L1>L0 rotation pointer is preserved.

```edit:book/src/L3/normalize.md
[old]: ## Lowers to

L3 `normalize` lowers to the **present adjacent L2 floor** [`normalize`](../L2/normalize.md) (cycle-043 D10) as **identity-in-form on the operator's signature**, via the firm [`normalize-body-identity`](../L3-L2/normalize-body-identity.md) L3>L2 theme (identity-in-form on the body, no wrapper rotation — `normalize` is a fused whole-tensor composite, not a step body, and **fork-independent / fold-parent-free**: it cites its two constituent floors `nrm2` + `scal` as `consumes` same-layer dependencies, never as a fold of which it is a member), and onward to L1 [`normalize`](../L1/normalize.md). L1, L2, and L3 all see `normalize :: Tensor[N] -> (Scalar, Tensor[N])` with the same shape contract, the same six algebraic laws, the same non-law set (partiality, nonlinearity, IEEE-754 caveats), and the same single-orthogonal-axis variant profile (element-type). The L2 floor — landed by the cycle-043 D10 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort`, the fused-composite counterpart of the leaf floors `reciprocal` / `scal` — gives the firm L3 entry a *present* adjacent L2 parent, so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

No `book/src/L3-L1/` directory exists in the artifact; the **transitive** L3>L1 identity (L3>L2 ∘ L2>L1, both identity-in-form) is captured **in-line** per the cycle-012 meta-phase non-adjacent-identity convention (lowering directories are per-adjacent-edge only; precedents: cycle-010 `krylov-step`, cycle-011 BLAS-1, cycle-038 `reciprocal` / `elementwise_product`). The substantive rotation in the chain is the firm L1>L0 [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (cycle-027) — it lowers the L1 pure-functional `(β, û) = normalize(x)` into Palace's L0 in-place receiver-mutating `linalg::Normalize(comm, x)` (computing `norm = Norml2(comm, x)`, asserting `norm > 0`, rescaling `x *= 1.0/norm` in place, returning `norm` by value), composing the [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) no-buffer reduction with the [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A in-place rescale plus the returned-scalar binding. The L3>L2 and L2>L1 hops are by contrast layer-coherence rotations (each layer is coherent within itself), not algebraic ones.
[new]: ## Downward to L2

L3 `normalize` lowers to the **present adjacent L2 floor** [`normalize`](../L2/normalize.md) (cycle-043 D10) as **identity-in-form on the operator's signature** — a **degenerate identity-in-named-terms lowering** with no vocabulary shift across the edge, recorded here as an **in-line note** rather than a dedicated `L3-L2/` theme chapter (the `normalize-body-identity` theme was demoted to this note under the 2026-06-01 VOCABULARY-SHIFT REDIRECT, cycle-050; CLAUDE.md §Methodology invariants ⟢). The rewrite is the identity on the fused composite's body: `normalize` is a fused whole-tensor composite, not a step body, so there is no wrapper to rotate (no `(op, K, s)`→`IterState` consolidation, no outer-loop dissolution — contrast the sibling `krylov-step` lowering) and no genuine kernel fusion to unfold (Palace's `linalg::Normalize` already separates the norm pass from the rescale pass). It is **fork-independent / fold-parent-free**: it cites its two constituent floors `nrm2` + `scal` as `consumes` same-layer dependencies, never as a fold of which it is a member, so this composite's floor stands unchanged regardless of the leaf-vs-fold realisation of `dot`/`scal`/`nrm2`.

L1, L2, and L3 all see `normalize :: Tensor[N] -> (Scalar, Tensor[N])` with the same shape contract, the same six algebraic laws, the same non-law set (partiality at `x ≠ 0`, nonlinearity, IEEE-754 caveats), the same law-6 factorisation `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`, and the same single-orthogonal-axis variant profile (element-type). The framing differs by layer (L3: whole-tensor field operation; L2: fusion-rotation floor naming the `nrm2 ∘ scal` composition); the operator itself is value-thread-isomorphic across the edge. The L2 floor — landed by the cycle-043 D10 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort`, the fused-composite counterpart of the leaf floors `reciprocal` / `scal` — gives the firm L3 entry a *present* adjacent L2 parent, so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

No `book/src/L3-L1/` directory exists in the artifact; the **transitive** L3>L1 identity (L3>L2 ∘ L2>L1, both identity-in-form) is captured **in-line** per the cycle-012 meta-phase non-adjacent-identity convention (lowering directories are per-adjacent-edge only; precedents: cycle-010 `krylov-step`, cycle-011 BLAS-1, cycle-038 `reciprocal` / `elementwise_product`). The substantive rotation in the chain is the firm L1>L0 [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (cycle-027) — it lowers the L1 pure-functional `(β, û) = normalize(x)` into Palace's L0 in-place receiver-mutating `linalg::Normalize(comm, x)` (computing `norm = Norml2(comm, x)`, asserting `norm > 0`, rescaling `x *= 1.0/norm` in place, returning `norm` by value), composing the [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) no-buffer reduction with the [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A in-place rescale plus the returned-scalar binding. The L3>L2 and L2>L1 hops are by contrast layer-coherence rotations (each layer is coherent within itself), not algebraic ones — which is exactly why the L3>L2 edge needs no dedicated theme chapter.
```

**2d. §Dependencies "L2 floor / L1 anchor" (line 107)** — drop the deleted theme link.

```edit:book/src/L3/normalize.md
[old]: **L2 floor / L1 anchor**: [`L2/normalize`](../L2/normalize.md) (firm, cycle-043 D10) is the present adjacent L2 floor this L3 entry lowers into via the firm [`normalize-body-identity`](../L3-L2/normalize-body-identity.md) theme; [`L1/normalize`](../L1/normalize.md) (firm) remains authoritative on the Palace surface details (the `linalg::Normalize` free-function template, the three consumer shapes, the returned-norm load-bearing analysis, the `normalize_B` rough-in note, the complete L0 evidence list). This L3 entry does not duplicate those details; the L3>L2 and (transitive) L3>L1 rotations are identity-in-form on the operator itself.
[new]: **L2 floor / L1 anchor**: [`L2/normalize`](../L2/normalize.md) (firm, cycle-043 D10) is the present adjacent L2 floor this L3 entry lowers into via the in-line identity-in-form §"Downward to L2" note above (no dedicated theme chapter — the degenerate `normalize-body-identity` theme was demoted to that note, cycle-050); [`L1/normalize`](../L1/normalize.md) (firm) remains authoritative on the Palace surface details (the `linalg::Normalize` free-function template, the three consumer shapes, the returned-norm load-bearing analysis, the `normalize_B` rough-in note, the complete L0 evidence list). This L3 entry does not duplicate those details; the L3>L2 and (transitive) L3>L1 rotations are identity-in-form on the operator itself.
```

**2e. §Status (line 127)** — drop the `normalize-body-identity` mention is not present in §Status; no edit needed there. **§Evidence (lines 149–150)** — the `[old]` block spans both §Evidence bullets (the L2-floor bullet at :149, which references the `normalize-body-identity` theme, and the standalone `normalize-body-identity` theme bullet at :150); the `[new]` block emits a **single** rewritten L2-floor bullet — it deletes the now-stale `normalize-body-identity` theme bullet (:150) and re-anchors the L2-floor bullet (:149) to the in-line §"Downward to L2" note. The separate L1-anchor bullet (:151) below them is untouched and already covers the L1 end of the chain.

```edit:book/src/L3/normalize.md
[old]: - `book/src/L2/normalize.md` (firm, cycle-043 D10) — the present adjacent L2 floor this L3 entry lowers into via the `normalize-body-identity` theme; the fusion-rotation floor of the fused `nrm2 ∘ scal` composite (fork-INDEPENDENT, no fold-parent), identity-in-form on the operator's signature.
- `book/src/L3-L2/normalize-body-identity.md` (firm, cycle-043 D10) — the adjacent L3>L2 body-identity theme; identity-in-form on the body, no wrapper rotation, no fold-parent.
[new]: - `book/src/L2/normalize.md` (firm, cycle-043 D10) — the present adjacent L2 floor this L3 entry lowers into via the in-line identity-in-form §"Downward to L2" note (no dedicated theme chapter; the degenerate `normalize-body-identity` theme was demoted to that note under the 2026-06-01 VOCABULARY-SHIFT REDIRECT, cycle-050); the fusion-rotation floor of the fused `nrm2 ∘ scal` composite (fork-INDEPENDENT, no fold-parent), identity-in-form on the operator's signature.
```

**2f. Occurrence coverage.** Confirmed the complete `normalize-body-identity` occurrence set in
`L3/normalize.md` is lines 6 (2a), 27 (2b), 107 (2d), 131 (2c, §"Lowers to" → §"Downward to L2"),
and 149+150 (2e, the two §Evidence bullets) — all handled above. The §"Lifts from" section (line 139ff)
contains no link to the deleted theme; no edit needed there.

### 3. `book/src/L2/normalize.md` — frontmatter + §"Downward to L1" in-line note + re-anchors

**3a. Frontmatter `lowers_to` (line 6)** — drop the D10 L2-L1 theme reference; the L2>L1 hop is now an in-line identity note.

```edit:book/src/L2/normalize.md
[old]:   - book/src/L1/normalize.md (identity-in-form on the operator's signature; the L2>L1 normalize rotation is narrated by the D10 L2-L1 theme — see Lowers-to)
[new]:   - book/src/L1/normalize.md (identity-in-form on the operator's signature — degenerate identity-in-named-terms, recorded as an in-line §"Downward to L1" note rather than a dedicated theme — see Lowers-to)
```

**3b. §"Lowers to" (lines 143–147)** — replace with the in-line §"Downward to L1" note. The forward-reference to the (now-deleted) `L2-L1/normalize` theme is removed; the substantive L1>L0 rotation pointer is preserved.

```edit:book/src/L2/normalize.md
[old]: ## Lowers to

L2 `normalize` lowers to L1 [`normalize`](../L1/normalize.md) as **identity-in-form on the operator's signature**. Both L1 and L2 see `normalize :: Tensor[N] -> (Scalar, Tensor[N])` with the same shape contract, the same six algebraic laws, the same non-law set (partiality, nonlinearity, IEEE-754 caveats), and the same single-orthogonal-axis variant profile (element-type). The fusion rotation L2→L1 is a no-op on the buffer side — there is no fused kernel to unfold (the norm and rescale are already separate passes at L0) and no destination buffer at L2 (the result is a returned pair). The L2>L1 rotation is narrated forward by the **D10 L2-L1 `normalize` lowering theme** this cycle (`book/src/L2-L1/`); this entry cites it for the rotation work and does not restate it. Forward-reference only — that chapter is co-dispatched this cycle; written here as plain text / inline-code, not a live link, per the missing-anchor convention.

The substantive rotation in the chain is the firm L1>L0 [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (cycle-027) — it lowers the L1 pure-functional `(β, û) = normalize(x)` into Palace's L0 in-place receiver-mutating `linalg::Normalize(comm, x)` (computing `norm = Norml2(comm, x)`, asserting `norm > 0`, rescaling `x *= 1.0/norm` in place, returning `norm` by value), composing the [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) no-buffer reduction with the [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A in-place rescale plus the returned-scalar binding. None of that is L2 content; the L2 form sees a single fused composition over its two floors.
[new]: ## Downward to L1

L2 `normalize` lowers to L1 [`normalize`](../L1/normalize.md) as **identity-in-form on the operator's signature** — a **degenerate identity-in-named-terms lowering** with no vocabulary shift across the edge, recorded here as an **in-line note** rather than a dedicated `L2-L1/` theme chapter (the `normalize-leaf-identity` theme was demoted to this note under the 2026-06-01 VOCABULARY-SHIFT REDIRECT, cycle-050; CLAUDE.md §Methodology invariants ⟢). Both L1 and L2 see `normalize :: Tensor[N] -> (Scalar, Tensor[N])` with the same shape contract, the same six algebraic laws, the same non-law set (partiality at `x ≠ 0`, nonlinearity, IEEE-754 caveats), the same law-6 factorisation `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`, and the same single-orthogonal-axis variant profile (element-type). The fusion rotation L2→L1 is a **no-op on the buffer side** — there is no fused kernel to unfold (the norm and rescale are already separate passes at L0) and no destination buffer at L2 (the result is a returned pair); the two same-layer constituent floors (`nrm2` + `scal`) are cited unchanged across the edge, and `normalize` carries no fold-parent to defer fusion to (its codomain `(Scalar, Tensor[N])` is neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`). The operator is value-thread-isomorphic across the edge; only the surrounding layer's framing differs (fusion-rotation view at L2 vs. mutation-rotation view at L1).

The substantive rotation in the chain is the firm L1>L0 [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (cycle-027) — it lowers the L1 pure-functional `(β, û) = normalize(x)` into Palace's L0 in-place receiver-mutating `linalg::Normalize(comm, x)` (computing `norm = Norml2(comm, x)`, asserting `norm > 0`, rescaling `x *= 1.0/norm` in place, returning `norm` by value), composing the [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) no-buffer reduction with the [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A in-place rescale plus the returned-scalar binding. None of that is L2 content; the L2 form sees a single fused composition over its two floors — which is exactly why the L2>L1 edge needs no dedicated theme chapter.
```

**3c. §Context (line 24)** — the §Context paragraph references the D9/D10 floor backfill but not the deleted theme by link; it points to "§Open-questions in this report" which was the harvest report. No `normalize-leaf-identity`/`normalize-body-identity` link occurs in §Context. No edit needed. (Confirmed: the only references to the deleted slugs in `L2/normalize.md` are in §"Lowers to" (3b) — `L2/normalize.md` does not link `normalize-body-identity` either. Verified by grep below.)

### 4. `book/src/SUMMARY.md` — remove the two theme lines

```edit:book/src/SUMMARY.md
[old]: - [normalize-body-identity](./L3-L2/normalize-body-identity.md)
[new]:
```

```edit:book/src/SUMMARY.md
[old]: - [normalize-leaf-identity](./L2-L1/normalize-leaf-identity.md)
[new]:
```

(Each removal deletes the whole line including its trailing newline; the integrator should collapse the
blank — i.e. remove the line entirely. The `[new]:` empty body is the standard line-removal form;
if the integrator prefers, the two lines may be dropped outright.)

### 5. `book/src/L3-L2/index.md` — remove the theme-row + cohort-log bullet (tally → D7)

**5a. Theme-list table row (line 25)** — remove entirely.

```edit:book/src/L3-L2/index.md
[old]: | [`normalize-body-identity`](./normalize-body-identity.md) | L3 [`normalize`](../L3/normalize.md) §Signature — the whole-tensor fused composite `normalize :: Tensor[N] -> (Scalar, Tensor[N])` (`(β, x/β)` where `β = nrm2 x`; partial at `x=0`); fused leaf composite, **no iteration view, no sequential obstruction**. | L2 [`normalize`](../L2/normalize.md) §Signature — the fusion-rotation floor: the fused `nrm2 ∘ scal` composite; **fork-INDEPENDENT, NO fold-parent** (codomain `(Scalar, Tensor[N])`), with two genuine same-layer `consumes` floors (`nrm2` + `scal`); identical signature + six laws + partiality + element-type axis. | `structural` (whole-tensor composite signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 specialized to the fused composite; the norm sub-step is a single `nrm2`-consumer reduction, the rescale is element-local `scal`) + secondary `empirical-match` (firm L1/L2/L3 value-thread-isomorphic chain + cycle-036 D2 (A) "fused `nrm2 + scal`" identity-in-form classification, `L3/index.md:44`) | `firm` (cycle-043 D10 abstractor; identity-in-form on the body, **no wrapper to rotate AND no fold-parent to defer to AND no genuine kernel fusion to unfold** — fused-composite counterpart of `krylov-step-body-identity`, direct sibling of `reciprocal-body-identity`/`scal-body-identity` but a *composite* not a leaf; **design-final on the leaf-vs-fold fork**, on the composite-with-no-fold-parent basis) |
[new]:
```

**5b. Cohort-log bullet (line 54)** — remove the `normalize-body-identity` bullet.

```edit:book/src/L3-L2/index.md
[old]: - `normalize-body-identity` — the L3 whole-tensor fused `normalize` composite lowers to the L2 same-named fusion-rotation floor (the fused `nrm2 ∘ scal` composite, **fork-INDEPENDENT, NO fold-parent**); identity-in-form on the body (six laws + partiality at `x=0` + element-type axis), no wrapper to rotate, no fold-parent to defer to, and no genuine kernel fusion to unfold; a *composite* (two same-layer `consumes` floors `nrm2` + `scal`) not a single leaf — the fused-composite counterpart of the standalone-leaf siblings.
[new]:
```

**5c. Design-fork-ratified bullet (line 75)** — drop only the trailing clause naming `normalize-body-identity` as an edge (the rest of the sentence is about the fork ratification and stays).

```edit:book/src/L3-L2/index.md
[old]: The `normalize-body-identity` edge (cycle-043) and the cycle-042 standalone-floor body-identity edges have **NO fold-parent** and were never reached by the fork — design-final regardless.
[new]: The `normalize` L3>L2 identity (cycle-043, demoted to an in-line §"Downward to L2" note on `book/src/L3/normalize.md` under the 2026-06-01 VOCABULARY-SHIFT REDIRECT, cycle-050) and the cycle-042 standalone-floor body-identity edges have **NO fold-parent** and were never reached by the fork — design-final regardless.
```

**5d. DEFER to D7:** the consolidated theme-count tally for the L3-L2 layer (the "firm N" integer in any cohort-growth count line / header tally). This row-removal drops the L3-L2 firm theme count by 1. **D7 owns the integer adjustment** — I am not editing it here. (Grep located no inline "firm N" total in the L3-L2 cohort-log header that names a count specifically attributable to this row; D7 should confirm against the full L3-L2 census.)

### 6. `book/src/L2-L1/index.md` — remove the theme-row + cohort-log bullet (tally → D7)

**6a. Theme-list table row (line 25)** — remove entirely.

```edit:book/src/L2-L1/index.md
[old]: | [normalize-leaf-identity](./normalize-leaf-identity.md) | `L2/normalize` (firm, cycle-043 D9 floor) | `L1/normalize` (firm cycle-027 operator) | firm *(structural; identity-in-form on the operator's signature — value-thread-isomorphic signature + six laws + partiality non-law at `x=0` + single element-type axis; **fused composite — NOT a leaf** (genuine same-layer `consumes`: `nrm2` + `scal`, cited unchanged across the edge) but **fork-INDEPENDENT, NO fold-parent** (codomain `(Scalar, Tensor[N])` — neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`), so NO fusion to defer (contrast `dot-leaf-identity`) AND **no genuine kernel fusion to unfold** (Palace's `linalg::Normalize` already separates the norm pass from the rescale pass — contrast the one step-4 `AddMult` re-fusion `divfree-projector-leaf-identity` carries); **design-final on the leaf-vs-fold fork**, on the composite-with-no-fold-parent basis; substantive rotation deferred to L1>L0 `normalize-mutation-rotation`)* |
[new]:
```

**6b. Cohort-log bullet (line 69)** — remove the `normalize-leaf-identity` bullet.

```edit:book/src/L2-L1/index.md
[old]: - `normalize-leaf-identity` — the L2 `normalize` floor lowers to the L1 `normalize` operator identity-in-form on the signature; a **fused composite — NOT a leaf** (genuine same-layer `consumes`: `nrm2` + `scal`, cited unchanged) but **fork-INDEPENDENT, NO fold-parent** (codomain `(Scalar, Tensor[N])` — neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`), so NO fusion to defer (contrast `dot-leaf-identity`) AND **no genuine kernel fusion to unfold** (Palace's `linalg::Normalize` already separates the norm pass from the rescale pass — contrast the one step-4 `AddMult` re-fusion `divfree-projector-leaf-identity` carries); design-final on the leaf-vs-fold fork (composite-with-no-fold-parent basis); substantive rotation deferred to L1>L0 `normalize-mutation-rotation`.
[new]:
```

**6c. Cohort growth log (line 78)** — drop only the `normalize-leaf-identity` token from the cycle-043 cohort entry (the surrounding entry covers the `axpy`-family batch and stays). The two replacements below are surgical sub-string edits.

```edit:book/src/L2-L1/index.md
[old]: `axpy-leaf-identity` + `axpby-leaf-identity` + `axpbypcz-leaf-identity` + `normalize-leaf-identity` firm cycle-043 (the **leaf-cohort floor-edge batch** — the L2>L1 thin-identity edges of the four new same-named L2 floors; firm **15 → 19** = 19 firm + 1 partly-constructive; the `axpy`-family three are fold-PARENTED arity-2/2/3 members of `linear_combination` (UNBLOCKED by the batch-12 leaf-floor (b) ratification — RESOLVED, no longer under the §"Design fork"), `normalize-leaf-identity` is the fused-composite edge with NO fold-parent (design-final like the cycle-042 standalone edges); the cycle-043 D1 lifter sweep also normalized `nrm2-fold-specialization`→`nrm2-leaf-identity` + `scal-fold-specialization`→`scal-leaf-identity` (net-zero on counts) so the whole L2>L1 identity-edge cohort is now uniform `-leaf-identity`)
[new]: `axpy-leaf-identity` + `axpby-leaf-identity` + `axpbypcz-leaf-identity` + `normalize-leaf-identity` firm cycle-043 (the **leaf-cohort floor-edge batch** — the L2>L1 thin-identity edges of the four new same-named L2 floors; firm **15 → 19** = 19 firm + 1 partly-constructive; the `axpy`-family three are fold-PARENTED arity-2/2/3 members of `linear_combination` (UNBLOCKED by the batch-12 leaf-floor (b) ratification — RESOLVED, no longer under the §"Design fork"), `normalize-leaf-identity` was the fused-composite edge with NO fold-parent (design-final like the cycle-042 standalone edges) — **DEMOTED to an in-line §"Downward to L1" note on `book/src/L2/normalize.md` under the 2026-06-01 VOCABULARY-SHIFT REDIRECT, cycle-050, as a degenerate identity-in-named-terms lowering**; the cycle-043 D1 lifter sweep also normalized `nrm2-fold-specialization`→`nrm2-leaf-identity` + `scal-fold-specialization`→`scal-leaf-identity` (net-zero on counts) so the whole L2>L1 identity-edge cohort is now uniform `-leaf-identity`)
```

**6d. DEFER to D7:** the cohort-growth count integers in the cycle-043 log entry (the "firm **15 → 19**" tally) reflect the *historical* state at cycle-043 and should arguably be left as the historical record, but the **current consolidated L2-L1 firm-theme total** (wherever D7 maintains it) drops by 1 with this row removal. **D7 owns the integer reconciliation** — I am not retroactively editing the historical "15 → 19" figure, only the descriptive token (6c). D7 should adjust any *current* L2-L1 firm-count tally.

### 7. `book/src/L3/index.md` — re-anchor the `normalize` row's theme link (no row removal)

The L3 `normalize` operator row (line 38) links `normalize-body-identity` twice (in the "Same-layer L3" cell and the "Lowers to" cell). Re-anchor both to the in-line §"Downward to L2" note.

```edit:book/src/L3/index.md
[old]: L2 floor via [`L2/normalize`](../L2/normalize.md) (present adjacent floor, cycle-043 D10) through [`normalize-body-identity`](../L3-L2/normalize-body-identity.md); L1 anchor via [`L1/normalize`](../L1/normalize.md) (identity-in-form on the operator's signature; six laws + the `x≠0` partiality precondition inherited unchanged). | L2 [`normalize`](../L2/normalize.md) via [`normalize-body-identity`](../L3-L2/normalize-body-identity.md) (identity-in-form on the body, no wrapper rotation, fork-independent / no fold-parent), then transitively L1 [`normalize`](../L1/normalize.md) (L3>L2 ∘ L2>L1 identity in-line; no `L3-L1/` directory).
[new]: L2 floor via [`L2/normalize`](../L2/normalize.md) (present adjacent floor, cycle-043 D10) through the in-line §"Downward to L2" identity note on `L3/normalize.md` (no dedicated theme — the degenerate `normalize-body-identity` theme was demoted to that note, cycle-050); L1 anchor via [`L1/normalize`](../L1/normalize.md) (identity-in-form on the operator's signature; six laws + the `x≠0` partiality precondition inherited unchanged). | L2 [`normalize`](../L2/normalize.md) via the in-line §"Downward to L2" identity note (identity-in-form on the body, no wrapper rotation, fork-independent / no fold-parent), then transitively L1 [`normalize`](../L1/normalize.md) (L3>L2 ∘ L2>L1 identity in-line; no `L3-L1/` directory).
```

## Discipline notes

- **Pure demotion, no collapse.** `normalize` stays a standalone L3 entry and a standalone L2 entry. It is
  a fused composite with **no fold-parent** (codomain `(Scalar, Tensor[N])` is neither reduce-to-`Scalar`
  nor reduce-to-`Tensor[N]`; established at both `book/src/L2/normalize.md:34-39,100-107` and
  `book/src/L3/normalize.md:88-93`), so there is no fold to collapse it into — the cleanest demotion case.
  Only the two degenerate adjacent-edge *theme chapters* are removed; the operator entries persist.
- **Constituent references left untouched per dispatch directive.** The `normalize` body's references to
  `nrm2` / `scal` (and their `consumes` frontmatter, §Dependencies, law-6 factorisation) are **not** edited.
  Their re-expression through `inner_product` / `linear_combination` combinators is the HELD fold-family
  cycle-051 work. My in-line notes describe the *composite's* lowering (identity, no vocabulary shift), not
  the constituents' lowering. No `nrm2` / `scal` entry or theme is touched.
- **High→low discipline preserved** (CLAUDE.md §Methodology invariants "Layers are defined high→low").
  The in-line notes are titled §"Downward to L2" / §"Downward to L1" and narrate the rewrite forward
  (L3→L2, L2→L1). The deleted `normalize-body-identity.md` §"Open questions" carried a reverse-direction
  "lifting note (working notes only)"; that note correctly lived in the theme's working-notes section and
  is not migrated into the formal entry body — the entries' existing §"Lifts from" sections already cover
  the upward framing in entry-appropriate terms, and no reverse-direction prose is added to the new notes.
- **Vocabulary-shift smell confirmed.** Both deleted themes are textbook degenerate
  identity-in-named-terms lowerings: every row of their "The rewrite" mapping tables reads "Identity. Same
  signature / same law-6 / same partiality / same axis" (`normalize-body-identity.md:110-117`,
  `normalize-leaf-identity.md:113-121`). No vocabulary shifted across either edge — exactly the smell the
  REDIRECT names. Demotion to in-line notes is the prescribed resolution (the entries remain coherent
  in-layer; the trivial rewrite is a one-paragraph note, not a chapter).
- **Citation handling.** No *new* L0 citations are introduced by the in-line notes — they restate the
  chain (`linalg::Normalize` at `palace/linalg/vector.hpp:262-270`, the partiality `MFEM_ASSERT` at
  `:267`, the in-place rescale at `:268`) already carried by both `normalize` entries' §Evidence sections,
  which are not edited. I re-verified the load-bearing anchor with
  `tools/citecheck/citecheck.py "palace/linalg/vector.hpp:262-270" --anchor 'Normalize'` → `[ok]`
  (anchor at lines 262, 264 within range). The in-line notes carry no pinpoint citation of their own
  beyond the preserved `normalize-mutation-rotation` cross-layer pointer (a `book/src/` path, not an L0
  range).

## Supporting evidence

- Deleted: `book/src/L3-L2/normalize-body-identity.md`, `book/src/L2-L1/normalize-leaf-identity.md`.
- In-line note homes: `book/src/L3/normalize.md` §"Downward to L2" (was §"Lowers to"),
  `book/src/L2/normalize.md` §"Downward to L1" (was §"Lowers to").
- Inbound-link re-anchors: `book/src/L3/index.md:38`, `book/src/L3-L2/index.md:25,54,75`,
  `book/src/L2-L1/index.md:25,69,78`, `book/src/SUMMARY.md:60,104`.
- Grep confirming the full inbound-reference set (7 files; the two theme files self-reference and are
  deleted): `grep -rln "normalize-body-identity\|normalize-leaf-identity" book/src/` →
  `L2-L1/index.md`, `L2-L1/normalize-leaf-identity.md` (deleted), `L3/index.md`, `L3-L2/index.md`,
  `L3-L2/normalize-body-identity.md` (deleted), `L3/normalize.md`, `SUMMARY.md`. All non-deleted
  references handled above.
- Directive: cycle-049 D3 worklist (DEMOTE-to-inline classification for the `normalize` pair) +
  CLAUDE.md §Methodology invariants ⟢ VOCABULARY-SHIFT REDIRECT (2026-06-01; `METHODOLOGY-REDIRECT.md`).
- Precedent shape: the `normalize` pair is the **third thin-identity sub-shape** resolved in this refactor
  pass (the dispatch names it the resolved fused-composite case); the standalone-leaf demotions
  (`reciprocal`, `elementwise_product`, etc.) are sibling cases handled in adjacent dispatches.

## Open questions / caveats

- **D7 coordination — consolidated tallies (DEFERRED, per dispatch directive).** This report removes the
  L3-L2 `normalize-body-identity` theme-row + the L2-L1 `normalize-leaf-identity` theme-row + their
  cohort-log bullets, dropping the **current firm-theme count by 1 in each of the two lowering layers**.
  I did **not** edit any consolidated count integer (the L3-L2 header tally, the L2-L1 current firm total).
  D7 should: (a) decrement the current L3-L2 firm-theme count by 1; (b) decrement the current L2-L1
  firm-theme count by 1; (c) decide whether the *historical* cycle-043 cohort-log figure "firm **15 → 19**"
  in `L2-L1/index.md:78` should be annotated (I left it as historical record and only edited the
  descriptive token per 6c). If D7 prefers a single coordinated tally pass across all of cycle-050's
  demotions, these two decrements fold into that pass.
- **`L2/normalize.md` §Context staleness (pre-existing, not introduced here).** `L2/normalize.md:24`
  references "§Open-questions in this report" (the D9 harvest report) and the L3 §27/§131 "no interposed
  L2 entry" staleness routed to a "c044 sweep". That cross-reference predates this dispatch and is not in
  scope for the demotion; I left it. If the c044 sweep already corrected the L3 §27/§131 notes (it should
  have, since the L2 floor landed), the residual phrasing in `L2/normalize.md:24` and `:151` is a separate
  cleanup — flagging for the planner, not correcting here (out of bounded-demotion scope).
- **No abstractor reread needed.** The demotion is a pure structural rewrite: the firmed-up vocabulary is
  unchanged (the `normalize` composite's signature, laws, and constituents are identical pre/post), and the
  rewrite direction stays high→low. No content decision beyond "this degenerate theme becomes an in-line
  note" was required.

---
agent: lifter
invoked_at: 2026-06-01T195100Z
scope: L3>L2 + L2>L1 degenerate-theme DEMOTE-to-inline — elementwise_product (cycle-050 D4)
status: integrated
integrated_at: 2026-06-01T222000Z
integration_commit: 6985e03
integration_notes: APPLIED clean (cycle-050 D4, CLEAN non-fold demotion). DELETED elementwise-product-body-identity (L3>L2) + elementwise-product-leaf-identity (L2>L1); folded the load-bearing facts (total-bijective-identity-on-single-binding justification + both variant axes element-type+conjugation, fork-INDEPENDENT no-fold-parent) into in-line §"Downward"/"Lowers to" notes on L3/L2 elementwise_product; bounded §3b prose-correction (stale -fusion forward-ref removed) applied; SUMMARY rows removed. De-linked normalize-leaf-identity:12 surviving live link (hard dangling-link gate; idempotent, D6 deletes that file). NO operator-chapter deletion. 1 OQ promoted (d7-count-reconciliation, RESOLVED by D7). NOTE: this report's de-linked dep-map rows (L3-L2 + L2-L1) were physically removed by integrator-finalize as build-repair. Build-relevant yes. refactor-pass ENACTMENT under the 2026-06-01 VOCABULARY-SHIFT REDIRECT.
inputs:
  - book/src/L3-L2/elementwise-product-body-identity.md
  - book/src/L2-L1/elementwise-product-leaf-identity.md
  - book/src/L3/elementwise_product.md
  - book/src/L2/elementwise_product.md
  - book/src/L3-L2/index.md
  - book/src/L2-L1/index.md
  - book/src/L2/index.md
  - book/src/SUMMARY.md
  - book/src/L2-L1/normalize-leaf-identity.md
---

# CYCLE: Re-anchor / DEMOTE elementwise_product degenerate theme pair to in-line notes

## Summary

This is the cycle-050 D4 enactment of the 2026-06-01 VOCABULARY-SHIFT REDIRECT for the
`elementwise_product` lowering pair. Both `L3-L2/elementwise-product-body-identity.md` and
`L2-L1/elementwise-product-leaf-identity.md` are degenerate identity-in-named-terms lowerings — the
operator's signature, all ten algebraic laws, and both variant axes (element-type + conjugation
sub-axis) are textually identical across each edge; the "rewrite" is the total bijective identity on a
single binding (the theme bodies say so explicitly: `body-identity.md:120` "total and bijective on a
single binding — the degenerate maximal case of the identity-in-form property"; `leaf-identity.md:104`
"total and bijective on the leaf"). Per the redirect, a degenerate identity-in-named-terms lowering is
a **smell** to resolve as a **thin in-line note**, not a mirrored entry + thin theme.

`elementwise_product` is a **standalone Hadamard binary leaf with NO fold-parent**
(`L2/elementwise_product.md:9-10` frontmatter `fold_parent: (none) … Fork-INDEPENDENT`), so its
operator entries are NOT slated for collapse-into-a-combinator — the demotion lands clean: delete the
two thin themes, fold their one load-bearing fact (the identity-in-form relationship between the
adjacent floors, with the substantive rotation deferred to the L1>L0
`reciprocal-elementwise-product-mutation-rotation` sub-pattern B) into a §"Downward" note on each
operator entry, re-anchor the operator entries' inbound prose links, drop the two `SUMMARY.md` lines,
neutralize (de-link) the now-dead inbound index-row + sibling-theme links so the build stays green,
and DEFER the index row removal + consolidated tally counts to D7.

No L0 fact carried by either theme is unique to the theme — both themes' L0 evidence
(`operator.cpp:478-487` `Mult` real, `:545-568` `MultHermitianTranspose` conjugate) is already present
verbatim in each operator entry's §Evidence (`L2/elementwise_product.md:453-467`,
`L3/elementwise_product.md:176-178`), re-verified `[ok]` this dispatch via `citecheck --anchor`. The
in-line demotion notes therefore make **no new L0 claim**; they are pure layer-coherence notes.

## Proposed changes

### 1. Delete the two degenerate theme files

```delete:book/src/L3-L2/elementwise-product-body-identity.md
```

```delete:book/src/L2-L1/elementwise-product-leaf-identity.md
```

### 2. L3 operator entry — re-anchor the deleted `elementwise-product-body-identity` references to the in-line note; add §"Downward to L2" demotion note

The L3 entry references the deleted slug by name in three places (frontmatter `:6`, §Context `:28`,
§"Lowers to" `:149` + `:151`). None is a live markdown link (all are inline-code backtick mentions of
the slug), so de-linking is not required — but the prose asserting the rotation is "captured by the
adjacent-edge theme" must be re-anchored to "captured in-line" so it does not point at a deleted file.

#### 2a. Frontmatter `lowers_to`

```edit:book/src/L3/elementwise_product.md
[old]: lowers_to:
  - book/src/L2/elementwise_product.md (identity-in-form on the primitive's signature; lowers through the present adjacent L2 floor via the `elementwise-product-body-identity` L3>L2 theme — see Lowers-to)
[new]: lowers_to:
  - book/src/L2/elementwise_product.md (identity-in-form on the primitive's signature; degenerate identity-in-named-terms edge — recorded in-line at "Lowers to" per the 2026-06-01 vocabulary-shift redirect, no dedicated L3>L2 theme; substantive rotation deferred to the L1>L0 `reciprocal-elementwise-product-mutation-rotation` sub-pattern B)
```

#### 2b. §Context "Downward" bullet (`:28`)

```edit:book/src/L3/elementwise_product.md
[old]: - **Downward** to L2: `elementwise_product` lowers to the **present adjacent L2 floor** [`elementwise_product`](../L2/elementwise_product.md) (cycle-042) via the `elementwise-product-body-identity` L3>L2 theme, and onward to L1 [`elementwise_product`](../L1/elementwise_product.md). The rotation is **identity-in-form on the primitive's signature** — L1, L2, and L3 all see `elementwise_product :: (Tensor[N], Tensor[N]) -> Tensor[N]` with the same shape contract, the same ten algebraic laws, the same non-law set (idempotence, multiplicative inverse, conjugate-variant commutativity), and the same variant-axis profile (one orthogonal element-type axis + one conjugation sub-axis on the complex side). The L2 floor is the standalone (fork-independent) Hadamard binary field operation; the L3>L2 hop is therefore identity-in-form through the adjacent floor, per **Identity-lowerings still require both L levels**, mirroring the cycle-041 `dot` / `nrm2` / `scal` L3>L2 floor discipline. The substantive rotation in the chain is the L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) (sub-pattern B), which lowers the L1 pure-functional `y = a ⊙ b` into Palace's `forall_switch` per-element output-arg kernel `Y[i] = A[i] * B[i]`.
[new]: - **Downward** to L2: `elementwise_product` lowers to the **present adjacent L2 floor** [`elementwise_product`](../L2/elementwise_product.md), and onward to L1 [`elementwise_product`](../L1/elementwise_product.md). The L3>L2 edge is a **degenerate identity-in-named-terms** rotation — L1, L2, and L3 all see `elementwise_product :: (Tensor[N], Tensor[N]) -> Tensor[N]` with the same shape contract, the same ten algebraic laws, the same non-law set (idempotence, multiplicative inverse, conjugate-variant commutativity), and the same variant-axis profile (one orthogonal element-type axis + one conjugation sub-axis on the complex side). Per the 2026-06-01 vocabulary-shift redirect, this degenerate edge is recorded **in-line** (see "Lowers to" below) rather than as a dedicated thin L3>L2 theme — the vocabulary does not shift across the edge, so there is no translation to narrate. The substantive rotation in the chain is the L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) (sub-pattern B), which lowers the L1 pure-functional `y = a ⊙ b` into Palace's `forall_switch` per-element output-arg kernel `Y[i] = A[i] * B[i]`.
```

#### 2c. §"Lowers to" body (`:149` + `:151`) — fold the demoted theme's content in-line

```edit:book/src/L3/elementwise_product.md
[old]: L3 `elementwise_product` lowers to the **present adjacent L2 floor** [`elementwise_product`](../L2/elementwise_product.md) (cycle-042) as **identity-in-form on the primitive's signature**, via the `elementwise-product-body-identity` L3>L2 theme, and onward to L1 [`elementwise_product`](../L1/elementwise_product.md). L1, L2, and L3 all see `elementwise_product :: (Tensor[N], Tensor[N]) -> Tensor[N]` with the same shape contract, the same ten algebraic laws, the same non-law set, and the same variant-axis profile (one orthogonal element-type axis + one conjugation sub-axis). The L2 floor is the standalone (fork-independent) Hadamard binary field operation — landed by the cycle-042 D3 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort`, mirroring the cycle-041 `dot` / `nrm2` / `scal` L2 floors — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

The L3>L2 identity rotation is captured by the adjacent-edge `elementwise-product-body-identity` L3>L2 theme (per the cycle-012 meta-phase per-adjacent-edge lowering-directory convention); the cycle-010 `krylov-step`, cycle-011 BLAS-1 / `apply_linop`, and cycle-037 `assemble-diagonal` / `jacobi-smoother` precedents establish the in-line identity-rotation discipline for the floor cohort. The **substantive** rotation in the chain is the L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) (sub-pattern B) — it lowers the L1 pure-functional `y = a ⊙ b` into Palace's `forall_switch` per-element output-arg kernel (the destination buffer reintroduced, the real single-multiply `Y[i] = A[i] * B[i]` / the complex six-multiply-add / the conjugate two-sign-flip variant, the device dispatch). The L3>L2 and L2>L1 hops are by contrast layer-coherence rotations (each layer is coherent within itself), not algebraic ones.
[new]: L3 `elementwise_product` lowers to the **present adjacent L2 floor** [`elementwise_product`](../L2/elementwise_product.md) as **identity-in-form on the primitive's signature**, and onward to L1 [`elementwise_product`](../L1/elementwise_product.md). L1, L2, and L3 all see `elementwise_product :: (Tensor[N], Tensor[N]) -> Tensor[N]` with the same shape contract, the same ten algebraic laws, the same non-law set, and the same variant-axis profile (one orthogonal element-type axis + one conjugation sub-axis). The L2 floor is the standalone (fork-independent) Hadamard binary field operation, so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

**The L3>L2 edge is a degenerate identity-in-named-terms rotation, recorded in-line (no dedicated theme).** Per the 2026-06-01 vocabulary-shift redirect (`METHODOLOGY-REDIRECT.md`; CLAUDE.md §Methodology invariants ⟢), an identity-in-named-terms lowering whose vocabulary does not shift across the edge is a smell resolved as a thin in-line note, not a mirrored entry + thin theme. The mapping is the **total bijective identity on a single binding** — every L3 binding (the `a ⊙ b` body, each of the ten algebraic laws, both variant axes) maps to the same L2 binding at the same position; there is no wrapper to rotate (`elementwise_product` is a leaf binary field operation, not a step body — no `(op, K, s)` carrier, no outer loop) and no fold-parent to defer fusion to (fork-INDEPENDENT; the L0 `forall_switch` per-element multiply is already the unfolded single-pass form). The structural justification is the `krylov-step-body-identity` point-3 condition (whole-tensor signature, no element loop exposed) specialized to the standalone fork-independent leaf. (Demoted from the former `L3-L2/elementwise-product-body-identity.md` theme, cycle-050 D4.) The **substantive** rotation in the chain is the L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) (sub-pattern B) — it lowers the L1 pure-functional `y = a ⊙ b` into Palace's `forall_switch` per-element output-arg kernel (the destination buffer reintroduced, the real single-multiply `Y[i] = A[i] * B[i]` / the complex six-multiply-add / the conjugate two-sign-flip variant, the device dispatch). The L3>L2 and L2>L1 hops are by contrast layer-coherence rotations (each layer is coherent within itself), not algebraic ones.
```

### 3. L2 operator entry — add §"Downward to L1" demotion note; fold the deleted `elementwise-product-leaf-identity` theme content in-line

The L2 entry's §"Lowers to" (`:387`) already records the L2>L1 edge as identity-in-form in-line and
explicitly states no firm `L2-L1` theme file exists ("No firm `L2-L1/elementwise-product-fusion` theme
file yet exists; this entry captures the identity rotation in-line"). The theme that DID exist
(`elementwise-product-leaf-identity.md`, under the `-leaf-identity` slug, not the `-fusion` slug the L2
prose forward-referenced) was the L2>L1 edge; the L2 §"Lowers to" prose never linked it (only the L2
frontmatter and the §Dependencies forward-reference mention an L2>L1 theme, both as plain text). So the
L2 entry needs only a light touch to record the demotion explicitly + drop the stale `-fusion`
forward-reference.

#### 3a. Frontmatter `lowers_to`

```edit:book/src/L2/elementwise_product.md
[old]:   - book/src/L1/elementwise_product.md (identity-in-form on the primitive's signature; no firm `L2-L1/elementwise-product-fusion` theme yet — leaf binary field operation, no multi-operation kernel fusion to unfold; in-line below at "Lowers to")
[new]:   - book/src/L1/elementwise_product.md (identity-in-form on the primitive's signature; degenerate identity-in-named-terms edge — recorded in-line below at "Lowers to" per the 2026-06-01 vocabulary-shift redirect, no dedicated L2>L1 theme; leaf binary field operation, no multi-operation kernel fusion to unfold; substantive rotation deferred to the L1>L0 `reciprocal-elementwise-product-mutation-rotation` sub-pattern B)
```

#### 3b. §Dependencies "Lowering themes (forthcoming…)" block (`:300-306`) — replace the stale forward-reference with the demotion record

```edit:book/src/L2/elementwise_product.md
[old]: **Lowering themes (forthcoming — plain-text forward-reference, files do not yet exist)**: an
`L2-L1/elementwise-product-fusion` theme (or the identity-in-form annotation folded into the
existing L1>L0 `reciprocal-elementwise-product-mutation-rotation` sub-pattern B) will narrate
how the L2 leaf lowers into the L1 leaf (identity-in-form; no multi-operation kernel fusion to
unfold — only the single per-element multiply pass); the L3>L2 identity rotation for
`elementwise_product` is the iteration-rotation re-erasure recorded in-line at the L3 entry.
Forward-reference only — that L2>L1 theme chapter does not yet exist; do not link.
[new]: **Lowering themes**: both adjacent edges of `elementwise_product` are **degenerate
identity-in-named-terms** rotations recorded **in-line** (no dedicated theme files), per the
2026-06-01 vocabulary-shift redirect (a degenerate identity-in-named-terms lowering is a smell
resolved as a thin in-line note). The L2>L1 edge is recorded in-line at §"Lowers to" below (the L2
leaf lowers into the L1 leaf identity-in-form; no multi-operation kernel fusion to unfold — only the
single per-element `forall_switch` multiply pass, already the unfolded single-pass form); the L3>L2
edge is recorded in-line at the L3 entry's §"Lowers to". The substantive rotation in the chain is the
L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
(sub-pattern B). (The former thin `L2-L1/elementwise-product-leaf-identity` + `L3-L2/elementwise-product-body-identity`
themes were demoted to these in-line notes cycle-050 D4.)
```

#### 3c. §"Lowers to" body (`:387`) — record the demotion explicitly

```edit:book/src/L2/elementwise_product.md
[old]: L2 `elementwise_product` lowers to L1 [`elementwise_product`](../L1/elementwise_product.md)
via an **identity-in-form** rotation: the signature
`(Tensor[N], Tensor[N]) -> Tensor[N]` is textually identical at both layers; the body is the
same Hadamard binary field operation. There is no multi-operation kernel fusion to unfold —
`elementwise_product` is a leaf binary field operation, and the L0 `forall_switch` per-element
multiply is already the unfolded single-pass form (contrast `dot`, which de-fuses a family of
fused reduction kernels into the canonical reduction). No firm `L2-L1/elementwise-product-fusion`
theme file yet exists; this entry captures the identity rotation in-line, following the
cycle-041 `dot` / `scal` floor precedent for in-line identity-rotation annotation. The
**substantive** rotation in the chain is the L1>L0
[`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
(sub-pattern B) — it reintroduces the L0 in-place destination buffer (the real single-multiply
`Y[i] = A[i] * B[i]`, the complex six-multiply-add, the conjugate two-sign-flip variant, and
the device dispatch).
[new]: L2 `elementwise_product` lowers to L1 [`elementwise_product`](../L1/elementwise_product.md)
via a **degenerate identity-in-named-terms** rotation, recorded **in-line** (no dedicated theme) per
the 2026-06-01 vocabulary-shift redirect: the signature `(Tensor[N], Tensor[N]) -> Tensor[N]` is
textually identical at both layers, and the mapping is the total bijective identity on the leaf —
every L2 binding (the `a ⊙ b` body, the ten algebraic laws, both variant axes: element-type +
conjugation sub-axis) maps to the same L1 binding at the same position. There is no multi-operation
kernel fusion to unfold — `elementwise_product` is a leaf binary field operation with **no fold-parent**
(fork-INDEPENDENT; the inverse-subsumption generalisation of `scal`, not a fold member), and the L0
`forall_switch` per-element multiply is already the unfolded single-pass form (contrast `dot`, which
de-fuses a family of fused reduction kernels into the canonical reduction). Because the vocabulary does
not shift across this edge, it is a thin in-line note, not a mirrored theme. (Demoted from the former
`L2-L1/elementwise-product-leaf-identity.md` theme, cycle-050 D4.) The **substantive** rotation in the
chain is the L1>L0
[`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
(sub-pattern B) — it reintroduces the L0 in-place destination buffer (the real single-multiply
`Y[i] = A[i] * B[i]`, the complex six-multiply-add, the conjugate two-sign-flip variant, and
the device dispatch).
```

### 4. SUMMARY.md — remove the two theme lines

```edit:book/src/SUMMARY.md
[old]: - [elementwise-product-body-identity](./L3-L2/elementwise-product-body-identity.md)
[new]:
```

```edit:book/src/SUMMARY.md
[old]: - [elementwise-product-leaf-identity](./L2-L1/elementwise-product-leaf-identity.md)
[new]:
```

### 5. Neutralize the now-dead inbound links so the build stays green (index rows)

These are the live markdown links / index rows that point at the two deleted files. Leaving them as
live links makes `linkcheck2` fail. Per the dispatch directive I do NOT remove the index rows or
rewrite the consolidated tallies (deferred to D7) — I only **de-link** (convert the live link to
plain-text inline-code) the minimum needed to keep the build green. **D7 should remove these rows
entirely and adjust the cohort tallies** (see Discipline notes for the exact rows). (The third de-link,
formerly §5c against `normalize-leaf-identity.md`, was **dropped by the repairer** — the sibling D6
dispatch deletes that whole file this cycle, so the inbound de-link is moot. See §5c below.)

#### 5a. `L3-L2/index.md` dep-map row (`:24`) — de-link the slug cell

The `[old]` / `[new]` strings below are the **whole row** (line 24 in full), so the edit applies
cleanly under both substring and whole-line integrator semantics; only the leading slug cell changes
(live link → plain inline-code + DEMOTED marker), the rest of the row is byte-identical.

```edit:book/src/L3-L2/index.md
[old]: | [`elementwise-product-body-identity`](./elementwise-product-body-identity.md) | L3 [`elementwise_product`](../L3/elementwise_product.md) §Signature — the whole-tensor binary field operation `elementwise_product :: (Tensor[N], Tensor[N]) -> Tensor[N]` (Hadamard `a ⊙ b`); leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`elementwise_product`](../L2/elementwise_product.md) §Signature — the base Hadamard-binary-multiply floor leaf; **fork-INDEPENDENT, NO fold-parent**; identical signature + ten laws + two variant axes (element-type + conjugation sub-axis). | `structural` (whole-tensor binary signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 specialized to the standalone fork-independent leaf) + secondary `empirical-match` (firm L1/L2/L3 value-thread-isomorphic chain + cycle-036 (A) identity-in-form classification) | `firm` (cycle-042 D10 abstractor; identity-in-form on the body, **no wrapper to rotate AND no fold-parent to defer to** — direct sibling of `scal-body-identity`/`reciprocal-body-identity`; **design-final on the leaf-vs-fold fork**) |
[new]: | `elementwise-product-body-identity` *(DEMOTED to in-line note cycle-050 D4 — row pending D7 removal)* | L3 [`elementwise_product`](../L3/elementwise_product.md) §Signature — the whole-tensor binary field operation `elementwise_product :: (Tensor[N], Tensor[N]) -> Tensor[N]` (Hadamard `a ⊙ b`); leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`elementwise_product`](../L2/elementwise_product.md) §Signature — the base Hadamard-binary-multiply floor leaf; **fork-INDEPENDENT, NO fold-parent**; identical signature + ten laws + two variant axes (element-type + conjugation sub-axis). | `structural` (whole-tensor binary signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 specialized to the standalone fork-independent leaf) + secondary `empirical-match` (firm L1/L2/L3 value-thread-isomorphic chain + cycle-036 (A) identity-in-form classification) | `firm` (cycle-042 D10 abstractor; identity-in-form on the body, **no wrapper to rotate AND no fold-parent to defer to** — direct sibling of `scal-body-identity`/`reciprocal-body-identity`; **design-final on the leaf-vs-fold fork**) |
```

#### 5b. `L2-L1/index.md` dep-map row (`:26`) — de-link the slug cell

The `[old]` / `[new]` strings below are the **whole row** (line 26 in full), so the edit applies
cleanly under both substring and whole-line integrator semantics; only the leading slug cell changes.

```edit:book/src/L2-L1/index.md
[old]: | [elementwise-product-leaf-identity](./elementwise-product-leaf-identity.md) | `L2/elementwise_product` (firm, cycle-042 D3 floor) | `L1/elementwise_product` (firm cycle-019/032/036 leaf) | firm *(structural; identity-in-form on the Hadamard binary leaf — value-thread-isomorphic signature + ten laws + two variant axes (element-type + conjugation sub-axis); **fork-INDEPENDENT — NO fold-parent** (a binary field op, neither `inner_product` reduce-to-`Scalar` nor `linear_combination` reduce-to-`Tensor[N]`; the inverse-subsumption generalisation of `scal`), so NO fusion to defer — the L0 `forall_switch` per-element multiply is already unfolded; **design-final on the leaf-vs-fold fork**)* |
[new]: | `elementwise-product-leaf-identity` *(DEMOTED to in-line note cycle-050 D4 — row pending D7 removal)* | `L2/elementwise_product` (firm, cycle-042 D3 floor) | `L1/elementwise_product` (firm cycle-019/032/036 leaf) | firm *(structural; identity-in-form on the Hadamard binary leaf — value-thread-isomorphic signature + ten laws + two variant axes (element-type + conjugation sub-axis); **fork-INDEPENDENT — NO fold-parent** (a binary field op, neither `inner_product` reduce-to-`Scalar` nor `linear_combination` reduce-to-`Tensor[N]`; the inverse-subsumption generalisation of `scal`), so NO fusion to defer — the L0 `forall_switch` per-element multiply is already unfolded; **design-final on the leaf-vs-fold fork**)* |
```

#### 5c. `L2-L1/normalize-leaf-identity.md` — DROPPED (repairer, cycle-050 D4 critique Issue 2)

The original §5c de-linked the dead `elementwise-product-leaf-identity` reference at
`normalize-leaf-identity.md:12`. The sibling D6 dispatch
(`reports/2026-06-01T195100Z-lifter-demote-normalize`) **DELETES the entire
`book/src/L2-L1/normalize-leaf-identity.md` file this cycle** (`delete:` block, D6 CYCLE.md:48). The
inbound de-link is therefore **moot** — D6 removes the whole file, so there is no surviving line to
de-link and no `linkcheck2` exposure from this report's deletions. The §5c edit has been **dropped by
the repairer** to avoid (a) editing a file another in-batch dispatch deletes, and (b) an integrator
ordering hazard if §5c is applied after D6's deletion (the edit would target a non-existent file).
`normalize-leaf-identity.md` remains a D6-owned target; no D4 action is needed against it.

The `L3-L2/index.md:53` and `L2-L1/index.md:68` cohort-list bullets, and the `L2/index.md:118` + `:123`
cohort-narrative mentions, are all **plain inline-code** (no live links) — they do not break the build
and are left for D7's consolidated-tally pass (the slugs are referenced in count narratives D7 owns).

## Discipline notes

- **What changed and why.** The two `elementwise_product` lowering themes were degenerate
  identity-in-named-terms lowerings (signature, ten laws, two variant axes all textually identical
  across each edge; the rewrite tables are total bijective identities on a single binding —
  `body-identity.md:104-121`, `leaf-identity.md:91-105`). Under the 2026-06-01 vocabulary-shift
  redirect, a degenerate identity-in-named-terms lowering is a smell to resolve as a thin in-line note.
  I deleted both theme files and folded their one load-bearing fact — the identity-in-form relationship
  between the adjacent same-named floors, with the substantive rotation deferred downstream to the
  L1>L0 `reciprocal-elementwise-product-mutation-rotation` sub-pattern B — into a §"Lowers to"
  (Downward) note on each operator entry. The L3 entry's §"Lowers to" gains the demoted body-identity
  theme's structural-justification sentence (the `krylov-step-body-identity` point-3 condition
  specialized to the standalone fork-independent leaf, no wrapper / no fold-parent); the L2 entry's
  §"Lowers to" gains the demoted leaf-identity theme's no-fusion-to-defer / fork-independence record.

- **No new L0 claim.** Both themes' L0 evidence (`operator.cpp:478-487` `Mult` real,
  `:545-568` `MultHermitianTranspose` conjugate, paths relative to `reference/palace/`) is already
  present verbatim in each operator entry's §Evidence (`L2/elementwise_product.md:453-467`;
  `L3/elementwise_product.md:176-178`). Re-verified `[ok]` this dispatch via
  `tools/citecheck/citecheck.py --anchor` (`Mult` @479 within 478-487; `MultHermitianTranspose` @548
  within 545-568). The in-line demotion notes cite no L0 themselves — they point at the operator
  entries' existing evidence, which is unchanged.

- **High→low discipline preserved.** All edited prose narrates the rewrite forward (L3 into L2, L2 into
  L1). Reverse-direction lifting notes ("Lifts from") in both operator entries are untouched. No
  inversion introduced.

- **Build-safety vs. defer-to-D7 partition (the load-bearing coordination point).** The dispatch
  directs me to DEFER the index consolidated tallies to D7 and to avoid a dangling row that breaks the
  build. These two directives are in tension for the dep-map rows (`L3-L2/index.md:24`,
  `L2-L1/index.md:26`), which are **live markdown links to the deleted files** — leaving them live
  fails `linkcheck2`. I resolved the tension the minimal way: I **de-link** those two (convert the live
  link to plain inline-code + a "pending D7 removal" marker) so the build stays green, but I do NOT
  remove the rows or touch any count. (The third candidate, the `normalize-leaf-identity.md:12` sibling
  link, was **dropped by the repairer** — the sibling D6 dispatch deletes that whole file this cycle,
  so the de-link is moot; see §5c.) **D7 should, in its consolidated pass:**
  - **Remove** the `L3-L2/index.md:24` dep-map row entirely and the `L3-L2/index.md:53` cohort-list
    bullet for `elementwise-product-body-identity`.
  - **Remove** the `L2-L1/index.md:26` dep-map row entirely and the `L2-L1/index.md:68` cohort-growth-log
    mention of `elementwise-product-leaf-identity` (it appears mid-sentence in the cycle-042 cohort
    narrative — D7 should adjust that narrative to read "the fork-INDEPENDENT standalone-floor-edge
    cohort" minus the demoted member).
  - **Decrement** the L3>L2 firm theme tally (the `body-identity` cohort count) and the L2>L1 firm
    theme tally (the `leaf-identity` cohort count) by 1 each, wherever D7 is reconciling the cycle-050
    demotion-batch counts. The `L2/index.md:118` cycle-043 narrative ("L3>L2 `-body-identity` ×4 → firm
    10 → 14" and "L2>L1 `-leaf-identity` ×4 → firm 15 → 19") and `L2/index.md:123` slug-convention note
    both name these slugs in historical-count prose — D7 owns whether/how to annotate those historical
    narratives (I left them plain inline-code, untouched; they are not live links and do not break the
    build).

- **Slug asymmetry respected.** I used the exact on-disk filenames throughout: the theme slugs are
  hyphenated (`elementwise-product-body-identity`, `elementwise-product-leaf-identity`); the operator
  chapters keep the underscore (`elementwise_product.md`). I did NOT normalize the chapter slug. The L2
  frontmatter's stale forward-reference to a `-fusion` slug (which never matched the actual
  `-leaf-identity` theme file) is replaced by the demotion record, removing a long-standing
  slug-mismatch wrinkle.

- **Bounded prose-correction recorded.** In §3b I removed the L2 entry's stale
  "`L2-L1/elementwise-product-fusion` … forthcoming … files do not yet exist" forward-reference. This
  was a drifted reference: the L2>L1 theme that DID exist used the `-leaf-identity` slug
  (`L2-L1/elementwise-product-leaf-identity.md`), not the `-fusion` slug the L2 prose anticipated, so
  the L2 prose was simultaneously claiming "no theme exists" while a `-leaf-identity` theme did exist.
  The demotion makes the in-line record authoritative and resolves the mismatch. This is a bounded
  fix (replacing a drifted/contradictory forward-reference with the now-correct in-line record),
  supported by the on-disk file listing this dispatch ran (`ls book/src/L2-L1/` showed
  `elementwise-product-leaf-identity.md`, never an `elementwise-product-fusion.md`), and recorded here
  per the lifter prose-correction-boundary discipline.

## Supporting evidence

- `book/src/L3-L2/elementwise-product-body-identity.md` (deleted) — the demoted L3>L2 theme; its
  §"The rewrite (L3 → L2)" table (`:104-121`) is the total-bijective-identity record folded into the L3
  entry's §"Lowers to".
- `book/src/L2-L1/elementwise-product-leaf-identity.md` (deleted) — the demoted L2>L1 theme; its
  §"The rewrite (L2 → L1)" table (`:91-105`) is the total-bijective-identity record folded into the L2
  entry's §"Lowers to".
- `book/src/L3/elementwise_product.md` (firm cycle-038) — the L3 operator entry receiving the in-line
  §"Lowers to" demotion note; its §Evidence (`:176-178`) carries the L0 anchors transitively.
- `book/src/L2/elementwise_product.md` (firm cycle-042 D3) — the L2 operator entry receiving the in-line
  §"Lowers to" demotion note; its §Evidence (`:453-467`) carries the L0 anchors.
- L0 (paths relative to `reference/palace/`, re-verified `[ok]` via `citecheck --anchor` this dispatch):
  `palace/linalg/operator.cpp:478-487` (`Mult` real, per-element `Y[i] = D[i] * X[i]` @486);
  `palace/linalg/operator.cpp:545-568` (`MultHermitianTranspose` conjugate variant @548).
- 2026-06-01 VOCABULARY-SHIFT REDIRECT (`METHODOLOGY-REDIRECT.md`; CLAUDE.md §Methodology invariants ⟢):
  the directive that classifies degenerate identity-in-named-terms lowerings as a smell to resolve as
  thin in-line notes.
- cycle-049 D3 worklist: the report that classified this theme pair DEMOTE-to-inline (per the dispatch
  scope).

## Open questions / caveats

- **D7 coordination (index row removal + tally decrement).** This is the only cross-dispatch dependency.
  I left the dep-map rows in place (de-linked) and all consolidated tallies untouched. D7 must remove
  the two dep-map rows + the two cohort-list bullets and decrement the L3>L2 + L2>L1 firm-theme counts
  by 1 each (exact rows enumerated in Discipline notes). If D7 runs BEFORE this report integrates, the
  de-link edits in §5a/§5b may conflict with D7's row removal — in that case the row removal subsumes
  the de-link and §5a/§5b can be dropped (the integrator should prefer D7's removal). If D7 runs AFTER,
  my de-link keeps the build green in the interim.

- **No abstractor reread needed.** This was a pure structural demotion — no signature shifted, no
  decomposition changed, no new content authored. The operator entries already framed both edges as
  identity-in-form in-line (the L2 §"Lowers to" explicitly said "captures the identity rotation
  in-line"); the demotion makes the in-line record canonical and deletes the redundant thin themes.
  The one bounded prose-correction (stale `-fusion` forward-reference) is recorded above and does not
  rise to a re-architecture.

- **`normalize-leaf-identity.md` is itself a cycle-050 demotion candidate** (it is a thin
  `-leaf-identity` theme for a fork-independent fused composite, structurally the same class as the two
  demoted here). It is NOT in this dispatch's scope; I only de-linked its dead reference to the deleted
  `elementwise-product-leaf-identity`. If `normalize` is demoted in a sibling cycle-050 dispatch, that
  dispatch should clean up the `:12` and `:47` sibling-cohort prose I left as plain inline-code. Flagged
  for the planner / D7, not acted on.

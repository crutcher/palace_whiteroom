---
agent: lifter
invoked_at: 2026-06-01T195100Z
scope: L3>L2 + L2>L1 degenerate-theme DEMOTE-to-inline — reciprocal (cycle-050 D5)
status: integrated
integrated_at: 2026-06-01T222000Z
integration_commit: 6985e03
integration_notes: APPLIED clean (cycle-050 D5, CLEAN non-fold demotion). DELETED reciprocal-body-identity (L3>L2) + reciprocal-leaf-identity (L2>L1); folded the identity relationship + transparent s=1/|z|² complex-intermediate note (vector.cpp:257-259) into in-line §"Downward to L2"/§"Downward to L1" notes on L3/L2 reciprocal; bounded prose-correction (phantom slug reciprocal-elementwise-identity de-staled) applied; intentional L3-vs-L2 §"Lowers to" heading asymmetry preserved; SUMMARY rows removed. De-linked 6 surviving live links to the deleted slugs (2 index rows + 4 inside D6 normalize files; hard dangling-link gate). NO operator-chapter deletion (nonlinear self-map, no fold-parent). 2 OQs promoted (incl. the mandatory post-deletion build-gate, satisfied by finalize's dead-link sweep). NOTE: this report's de-linked dep-map rows physically removed by integrator-finalize as build-repair. Build-relevant yes. refactor-pass ENACTMENT under the 2026-06-01 VOCABULARY-SHIFT REDIRECT.
inputs:
  - book/src/L3-L2/reciprocal-body-identity.md
  - book/src/L2-L1/reciprocal-leaf-identity.md
  - book/src/L3/reciprocal.md
  - book/src/L2/reciprocal.md
  - book/src/SUMMARY.md
  - book/src/L3-L2/index.md
  - book/src/L2-L1/index.md
  - reports/2026-06-01T195039Z-cycle-planner-cycle-050/CYCLE.md
---

# CYCLE: Re-anchor (demote) reciprocal degenerate theme pair to in-line notes

## Summary

Per the cycle-049 D3 degenerate-lowering worklist and the cycle-050 plan (D5), the two
`reciprocal` lowering themes — `L3-L2/reciprocal-body-identity.md` and
`L2-L1/reciprocal-leaf-identity.md` — are **degenerate identity-in-named-terms lowerings**
under the 2026-06-01 VOCABULARY-SHIFT REDIRECT: their entire content is "the body IS the
identity, no wrapper to rotate, no fold-parent to defer to, no kernel fusion to unfold." They
are the canonical smell the redirect names — a mirrored entry + thin theme where the
vocabulary did not shift. `reciprocal` is a **standalone elementwise multiplicative-inverse
leaf with NO fold-parent** (a nonlinear self-map, `1/(a+b) ≠ 1/a + 1/b`), so it is **NOT**
slated for collapse into any combinator (there is no fold for it to belong to) — this is a
**clean demotion**, not a leaf-collapse. This dispatch deletes both theme files, folds their
one load-bearing fact (the identity-in-form relationship + the transparent `s = 1/|z|²`
complex-intermediate note, both already authoritatively cited at L1/L2/L3) into in-line
§"Downward to L2" (on `L3/reciprocal.md`) and §"Downward to L1" (on `L2/reciprocal.md`) notes,
re-anchors the stale theme-name references inside the two leaf chapters, and removes the two
`SUMMARY.md` lines. Per scope, **all index consolidated-tally AND row/bullet edits are deferred
to D7** (the count-ownership writer for the c050 wave) — coordinated below in §Discipline notes.
**No leaf-chapter deletion** (the `reciprocal` L2/L3 entries stay — they are standalone, not
collapsing). The substantive rotation in the chain (the firm L1>L0
`reciprocal-elementwise-product-mutation-rotation`) is untouched.

## Proposed changes

### 1. Delete the two degenerate theme files

```delete:book/src/L3-L2/reciprocal-body-identity.md
```

```delete:book/src/L2-L1/reciprocal-leaf-identity.md
```

### 2. `book/src/L3/reciprocal.md` — add in-line §"Downward to L2" note; re-anchor stale theme-name refs

The L3 entry references the now-deleted `reciprocal-body-identity` theme by name in three
places (frontmatter `lowers_to`, §Context "Downward" bullet, §"Lowers to"). These are
backtick plain-text theme-name mentions (not live `[](./...)` links, so no `linkcheck2`
breakage), but they name a deleted artifact — re-anchor them to the in-line note. The
identity-in-form relationship is preserved; the §"Lowers to" section becomes the in-line home.

Frontmatter `lowers_to` — drop the deleted theme-name; point at the in-line note:

```edit:book/src/L3/reciprocal.md
[old]:   - book/src/L2/reciprocal.md (identity-in-form on the primitive's signature; lowers through the present adjacent L2 floor via the `reciprocal-body-identity` L3>L2 theme — see "Lowers to")
[new]:   - book/src/L2/reciprocal.md (identity-in-form on the primitive's signature; lowers to the present adjacent L2 floor — the degenerate L3>L2 identity is recorded in-line at §"Downward to L2" / §"Lowers to", no dedicated theme file: the vocabulary does not shift across this edge)
```

§Context "Downward" bullet — replace the deleted theme-name reference with the in-line framing:

```edit:book/src/L3/reciprocal.md
[old]: - **Downward** to L2/L1: the L3 form's signature `Tensor[N] -> Tensor[N]` is textually identical to the L2 floor and L1 leaf signatures; all three forms describe pure-functional elementwise reciprocation with no destination buffer in the signature, no per-element loop visible, no reduction, no MPI collective at the L1 / L2 / L3 surface. The L3 → L2 rotation is the identity on the primitive itself. The framing differs: L1 frames `reciprocal` as the *mutation-rotation* image of the L0 receiver-self-overwriting `mfem::Vector::Reciprocal()` / `ComplexVector::Reciprocal()` member-method idiom (the L1 surface drops the receiver-mutation mention); L3 frames the same operator as a *field operation* in the whole-tensor vocabulary that the iteration-rotation layer composes. **The body of `reciprocal` is the identity rotation across this edge.** It lowers to the **present adjacent L2 floor** [`reciprocal`](../L2/reciprocal.md) (cycle-042) via the `reciprocal-body-identity` L3>L2 theme — the rotation carries no algebraic novelty, mirroring the BLAS-1 / `apply_linop` / `assemble-diagonal` L3>L2 floor discipline. The L3>L2 identity-in-form annotation is captured by the adjacent-edge theme per the cycle-012 per-adjacent-edge lowering-directory convention (precedent: `scal`, `dot`, `assemble-diagonal`, `elementwise_product`); the transitive L3>L1 identity remains in-line, with no non-adjacent `L3-L1/` directory created. The **substantive** rotation in the chain is the firm L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) theme.
[new]: - **Downward** to L2/L1: the L3 form's signature `Tensor[N] -> Tensor[N]` is textually identical to the L2 floor and L1 leaf signatures; all three forms describe pure-functional elementwise reciprocation with no destination buffer in the signature, no per-element loop visible, no reduction, no MPI collective at the L1 / L2 / L3 surface. The L3 → L2 rotation is the identity on the primitive itself — **the vocabulary does not shift across this edge**, so it is recorded as an in-line note (§"Downward to L2" below), not a dedicated lowering theme (the degenerate `reciprocal-body-identity` theme was demoted to this note in cycle-050 under the VOCABULARY-SHIFT REDIRECT — a mirrored entry + thin theme with no vocabulary shift is the smell the redirect names). The framing differs: L1 frames `reciprocal` as the *mutation-rotation* image of the L0 receiver-self-overwriting `mfem::Vector::Reciprocal()` / `ComplexVector::Reciprocal()` member-method idiom (the L1 surface drops the receiver-mutation mention); L3 frames the same operator as a *field operation* in the whole-tensor vocabulary that the iteration-rotation layer composes. **The body of `reciprocal` is the identity rotation across this edge.** The **substantive** rotation in the chain is the firm L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) theme.
```

§"Lowers to" — rewrite to the in-line §"Downward to L2" note (the demotion home). Replace the
two paragraphs (the "Lowers to" body) that name the deleted theme:

```edit:book/src/L3/reciprocal.md
[old]: L3 `reciprocal` lowers to the **present adjacent L2 floor** [`reciprocal`](../L2/reciprocal.md) (cycle-042) as **identity-in-form on the primitive's signature**, via the `reciprocal-body-identity` L3>L2 theme, and onward to L1 [`reciprocal`](../L1/reciprocal.md). L1, L2, and L3 all see `reciprocal :: Tensor[N] -> Tensor[N]` with the same shape contract, the same eight algebraic laws, the same non-law set (partiality, nonlinearity, IEEE-754 caveats), and the same single-orthogonal-axis variant profile (element-type). The L2 floor is the standalone (fork-independent) elementwise multiplicative-inverse leaf — landed by the cycle-042 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort`, mirroring the cycle-041 `dot` / `nrm2` / `scal` L2 floors — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

The L3>L2 identity rotation is captured by the adjacent-edge `reciprocal-body-identity` L3>L2 theme (per the cycle-012 meta-phase per-adjacent-edge lowering-directory convention); the transitive L3>L1 identity (L3>L2 ∘ L2>L1) is annotated in-line, with no `book/src/L3-L1/` directory created. The cycle-010 `krylov-step`, cycle-011 BLAS-1 / `apply_linop`, and cycle-037 `assemble-diagonal` precedents establish the in-line identity-rotation discipline for the floor cohort. The substantive rotation in the chain is the firm L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) theme — it lowers the L1 pure-functional form into Palace's L0 in-place receiver-self-overwrite `Reciprocal()` member-method pair (the real upstream `mfem::Vector::Reciprocal()` and the complex `ComplexVector::Reciprocal()` kernel `s = 1/(XR²+XI²); XR *= s; XI *= -s`, the `forall_switch` host/device dispatch, and the no-zero-guard policy). The L3>L2 and L2>L1 hops are by contrast layer-coherence rotations (each layer is coherent within itself), not algebraic ones.
[new]: ### Downward to L2

L3 `reciprocal` lowers to the **present adjacent L2 floor** [`reciprocal`](../L2/reciprocal.md) (cycle-042) as **identity-in-form on the primitive's signature**. L1, L2, and L3 all see `reciprocal :: Tensor[N] -> Tensor[N]` with the same shape contract, the same eight algebraic laws, the same non-law set (partiality, nonlinearity, IEEE-754 caveats), and the same single-orthogonal-axis variant profile (element-type). **The vocabulary does not shift across this edge** — `reciprocal` is a standalone elementwise multiplicative-inverse leaf (no fold-parent, a nonlinear self-map) with no wrapper to rotate and no kernel fusion to unfold — so the L3>L2 relationship is recorded here in-line rather than as a dedicated lowering theme. (The degenerate `reciprocal-body-identity` L3>L2 theme was demoted to this note in cycle-050 under the VOCABULARY-SHIFT REDIRECT; a mirrored entry + thin identity-in-named-terms theme is the smell the redirect names — resolved as the thin in-line note here.) The L2 floor is the standalone (fork-independent) elementwise multiplicative-inverse leaf, so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

The transitive L3>L1 identity (L3>L2 ∘ L2>L1) is likewise annotated in-line, with no `book/src/L3-L1/` directory. The **substantive** rotation in the chain is the firm L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) theme — it lowers the L1 pure-functional form into Palace's L0 in-place receiver-self-overwrite `Reciprocal()` member-method pair (the real upstream `mfem::Vector::Reciprocal()` and the complex `ComplexVector::Reciprocal()` kernel `s = 1/(XR²+XI²); XR *= s; XI *= -s` at `palace/linalg/vector.cpp:257-259`, the `forall_switch` host/device dispatch, and the no-zero-guard policy). The L3>L2 and L2>L1 hops are by contrast layer-coherence relationships (each layer is coherent within itself), not vocabulary-shifting rotations.
```

### 3. `book/src/L2/reciprocal.md` — refresh in-line §"Downward to L1" note (de-stale the deleted theme-name)

The L2 entry already narrates the L2>L1 identity **in-line** (§"Lowers to", lines 351-372) and
its frontmatter `lowers_to` (line 6) already says "no firm `L2-L1/reciprocal-elementwise-identity`
theme yet" — but a `reciprocal-leaf-identity` theme WAS subsequently created (cycle-042 D10) and
is now being deleted by this dispatch. Both the frontmatter note and the §"Lowers to" prose are
**stale** (they predate the theme's creation; they reference a never-created slug
`reciprocal-elementwise-identity`). De-stale them to reflect the now-permanent in-line home.
This is a bounded prose-correction (a drifted/stale claim about a theme file's existence),
supported by the on-disk state (the theme file is being deleted this dispatch; the in-line note
becomes the terminal home).

Frontmatter `lowers_to`:

```edit:book/src/L2/reciprocal.md
[old]:   - book/src/L1/reciprocal.md (identity-in-form; no firm `L2-L1/reciprocal-elementwise-identity` theme yet — the only fusion content is the transparent `s = 1/|z|²` factoring of the complex closed form, not a multi-op kernel fusion; in-line below at "Lowers to")
[new]:   - book/src/L1/reciprocal.md (identity-in-form; no dedicated L2>L1 theme file — the vocabulary does not shift across this edge, so the degenerate identity is recorded in-line below at §"Downward to L1"; the only fusion content is the transparent `s = 1/|z|²` factoring of the complex closed form, not a multi-op kernel fusion)
```

§"Lowers to" — retitle to §"Downward to L1" and de-stale the theme-file paragraph. Replace the
two paragraphs of the §"Lowers to" body:

```edit:book/src/L2/reciprocal.md
[old]: ## Lowers to

L2 `reciprocal` lowers to L1 [`reciprocal`](../L1/reciprocal.md) via an **identity-in-form**
rotation: the signature `Tensor[N] -> Tensor[N]` is textually identical at both layers; the
body is the same elementwise multiplicative-inverse field operation; the eight algebraic laws,
the non-law set (partiality, nonlinearity, IEEE-754 caveats), and the single-orthogonal-axis
variant profile (element-type) all transport unchanged. The only fusion content is the
transparent `s = 1/|z|²` factoring of the complex closed form (§ "Fusion note") — not a
multi-operation kernel fusion to de-fuse — so the rotation carries no algebraic novelty.

No firm `L2-L1/reciprocal-elementwise-identity` theme file yet exists (the D10 dispatch this
cycle authors the L2>L1 lowering theme for `reciprocal`); this entry captures the identity
rotation **in-line**, following the L3 `reciprocal` and L2 `scal` backfill precedents for
in-line identity-rotation annotation (per the cycle-012 meta-phase non-adjacent-identity
convention — lowering directories are per-adjacent-edge only). The substantive rotation in the
chain is the firm L1>L0
[`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
theme — it lowers the L1 pure-functional form into Palace's L0 in-place receiver-self-overwrite
`Reciprocal()` member-method pair (the real upstream `mfem::Vector::Reciprocal()`, the complex
`ComplexVector::Reciprocal()` kernel `s = 1/(XR²+XI²); XR *= s; XI *= -s`, the `forall_switch`
host/device dispatch, and the no-zero-guard policy). The L2>L1 hop is by contrast a
layer-coherence rotation (each layer is coherent within itself), not an algebraic one.
[new]: ## Downward to L1

L2 `reciprocal` lowers to L1 [`reciprocal`](../L1/reciprocal.md) via an **identity-in-form**
relationship: the signature `Tensor[N] -> Tensor[N]` is textually identical at both layers; the
body is the same elementwise multiplicative-inverse field operation; the eight algebraic laws,
the non-law set (partiality, nonlinearity, IEEE-754 caveats), and the single-orthogonal-axis
variant profile (element-type) all transport unchanged. The only fusion content is the
transparent `s = 1/|z|²` factoring of the complex closed form (§ "Fusion note") — not a
multi-operation kernel fusion to de-fuse — so **the vocabulary does not shift across this edge**.

There is **no dedicated `L2-L1/` theme file** for `reciprocal`: a mirrored L2/L1 entry plus a
thin identity-in-named-terms theme is the degenerate smell the 2026-06-01 VOCABULARY-SHIFT
REDIRECT names, so the relationship is recorded here as an in-line note. (The degenerate
`reciprocal-leaf-identity` L2>L1 theme, authored cycle-042 D10, was demoted to this note in
cycle-050.) This follows the in-line identity-rotation discipline for the floor cohort (lowering
directories carry genuine vocabulary-shifting rotations, not identities). The substantive
rotation in the chain is the firm L1>L0
[`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
theme — it lowers the L1 pure-functional form into Palace's L0 in-place receiver-self-overwrite
`Reciprocal()` member-method pair (the real upstream `mfem::Vector::Reciprocal()`, the complex
`ComplexVector::Reciprocal()` kernel `s = 1/(XR²+XI²); XR *= s; XI *= -s` at
`palace/linalg/vector.cpp:257-259`, the `forall_switch` host/device dispatch, and the
no-zero-guard policy). The L2>L1 hop is by contrast a layer-coherence relationship (each layer is
coherent within itself), not a vocabulary-shifting rotation.
```

### 4. `book/src/SUMMARY.md` — remove the two theme lines

```edit:book/src/SUMMARY.md
[old]: - [reciprocal-body-identity](./L3-L2/reciprocal-body-identity.md)
[new]:
```

```edit:book/src/SUMMARY.md
[old]: - [reciprocal-leaf-identity](./L2-L1/reciprocal-leaf-identity.md)
[new]:
```

(Each of the two lines is removed entirely. The surrounding bullet-list lines are unaffected;
the empty-string replacement deletes the line including its newline as a unique-match removal.)

## Discipline notes

- **What changed and why.** Both `reciprocal` lowering themes are content-identical to "the
  body is the identity, nothing rotates" — they are the degenerate identity-in-named-terms
  lowerings the VOCABULARY-SHIFT REDIRECT (CLAUDE.md §Methodology invariants ⟢;
  `METHODOLOGY-REDIRECT.md`) flags as a smell and directs to "resolve as a thin in-line note."
  `reciprocal` has **no fold-parent** (it is a nonlinear elementwise self-map, established by
  the cycle-042 D2 floor harvest: `1/(a+b) ≠ 1/a + 1/b`, not a member of `inner_product` or
  `linear_combination`), so there is no combinator to collapse it into — the clean-demotion
  case (per cycle-050 plan §3 and the cycle-049 D3 worklist §B classification). The operator's
  L2 and L3 standalone entries are retained (NO leaf-chapter deletion); the demotion only
  removes the two thin theme files and folds their one load-bearing fact (the identity
  relationship + the transparent `s = 1/|z|²` complex-intermediate note, both already
  authoritatively recorded at L1/L2/L3) into the leaf chapters' in-line §"Downward to L2" /
  §"Downward to L1" notes.

- **High→low discipline preserved.** The in-line notes narrate the rewrite **forward**
  (L3 → L2, L2 → L1); the reverse-direction "lifts from" content already present in the
  chapters is untouched. No lifting note was introduced into the formal chapter body.

- **Bounded prose-corrections recorded (per the lifter L0-evidence-driven correction
  boundary).** The `L2/reciprocal.md` frontmatter line 6 and §"Lowers to" prose were **stale**:
  they asserted "no firm `L2-L1/reciprocal-elementwise-identity` theme yet" and "the D10
  dispatch this cycle authors the L2>L1 lowering theme" — written before the
  `reciprocal-leaf-identity` theme was created (cycle-042 D10), and naming a slug
  (`reciprocal-elementwise-identity`) that was never the actual filename. Both are corrected to
  the now-terminal in-line-note framing. This is bounded (de-staling a claim about a theme
  file's existence + the now-correct in-line home), supported by the on-disk state this
  dispatch establishes (theme deleted; in-line note is the terminal home), and recorded here
  explicitly — not a silent edit. No decomposition, signature, or law was changed.

- **Citation self-verification.** The single L0 fact preserved in the in-line notes (the complex
  kernel `s = 1/(XR²+XI²); XR *= s; XI *= -s` at `palace/linalg/vector.cpp:257-259`, and the
  `ComplexVector::Reciprocal()` body at `:248-261`) was re-verified on-disk this dispatch via
  `tools/citecheck/citecheck.py --anchor`: `vector.cpp:257-259 --anchor 'XR'` → `[ok]` (anchor
  at lines 257-258 within range); `vector.cpp:248-261 --anchor 'Reciprocal'` → `[ok]` (anchor
  at line 248 within range). Both citations were already present and authoritative in the
  retained L2/L3 chapters; the in-line notes carry no NEW L0 claim (the identity edge makes none).

- **Index edits DEFERRED to D7 (coordination — NOT emitted here).** Per scope ("DEFER both index
  consolidated tallies to D7; prefer leaving index tally edits to D7") and the c050 count-
  ownership partition, I am **not** emitting edits to `book/src/L3-L2/index.md` or
  `book/src/L2-L1/index.md`. D7 owns the consolidated firm-count tallies AND, to avoid an
  edit-collision with the parallel sibling demotions (D4 `elementwise_product`, D6 `normalize`),
  should also make the **row + bullet removals** for `reciprocal` in one pass. The precise
  `reciprocal`-slug locations D7 must remove (verified on-disk this dispatch):
  - `book/src/L3-L2/index.md:23` — the `reciprocal-body-identity` **table row** (remove entire row).
  - `book/src/L3-L2/index.md:52` — the `reciprocal-body-identity` **summary bullet** (remove).
  - `book/src/L2-L1/index.md:24` — the `reciprocal-leaf-identity` **table row** (remove entire row).
  - `book/src/L2-L1/index.md:67` — the `reciprocal-leaf-identity` **summary bullet** (remove).
  - Both index files carry a consolidated firm-count tally (e.g. the `L2-L1/index.md:78` cohort
    growth log "firm 10 → 15" cycle-042 line) that D7 decrements for the cohort-wide c050
    demotion total — left entirely to D7.

- **Sibling-theme inbound references NOT re-anchored here (coordination — they are themselves
  being deleted this cycle).** The deleted `reciprocal` slugs are referenced as live links /
  precedent-prose inside the sibling theme files `L3-L2/elementwise-product-body-identity.md`,
  `L3-L2/normalize-body-identity.md`, `L2-L1/normalize-leaf-identity.md`, and
  `L2-L1/elementwise-product-leaf-identity.md` (10 references total — locations enumerated in
  §Open questions). I am **not** editing those files: D4 (`elementwise_product`) and D6
  (`normalize`) are deleting those very theme files in this same cycle (per the c050 plan), so
  re-anchoring references inside soon-to-be-deleted files would be wasted/conflicting work. This
  is flagged for D4/D6/D7 coordination in §Open questions. If, contrary to the plan, any of those
  four sibling theme files survives c050, the integrator must re-anchor its `reciprocal-*-identity`
  references to the in-line notes (or convert them to plain text) to avoid a `linkcheck2` dead
  link to the deleted slug.

## Supporting evidence

- `reports/2026-06-01T195039Z-cycle-planner-cycle-050/CYCLE.md` — the c050 plan; D5 scope
  ("`reciprocal` demotion … Clean DEMOTE, standalone elementwise leaf, no fold parent"), the
  SAFE-SLICE/HOLD framing, and the D7 count-ownership partition.
- Cycle-049 D3 degenerate-lowering worklist §B (classified the two `reciprocal` themes
  DEMOTE-to-inline, clean, no fold-parent) — referenced by the c050 plan; the originating
  worklist.
- `book/src/L3-L2/reciprocal-body-identity.md` + `book/src/L2-L1/reciprocal-leaf-identity.md`
  (the two deleted themes) — both `firm`, both entirely identity-in-form prose, both explicitly
  "no wrapper to rotate, no fold-parent to defer to."
- `book/src/L3/reciprocal.md` (firm cycle-038) + `book/src/L2/reciprocal.md` (firm cycle-042 D2)
  — the retained standalone leaf chapters receiving the in-line notes; both already carry the
  identity-in-form narration + the transparent `s = 1/|z|²` note authoritatively.
- L0 (verified on-disk this dispatch, `tools/citecheck/citecheck.py --anchor`):
  `palace/linalg/vector.cpp:248-261` (`ComplexVector::Reciprocal()`),
  `palace/linalg/vector.cpp:257-259` (the `s = 1/|z|²` kernel) — both `[ok]`.

## Open questions / caveats

- **D4/D6/D7 coordination on sibling-theme inbound references (the load-bearing caveat).** The
  deleted `reciprocal` slugs are referenced inside four sibling theme files that D4/D6 are
  deleting this same cycle. Exact reference locations (verified on-disk):
  - `L3-L2/elementwise-product-body-identity.md` — lines 12, 49, 129, 167, 204, 235 (live links
    + precedent-prose to `reciprocal-body-identity`). **Being deleted by D4.**
  - `L3-L2/normalize-body-identity.md` — lines 10, 42, 53, 127, 169, 210, 217, 248 (refs to
    `reciprocal-body-identity`). **Being deleted by D6.**
  - `L2-L1/normalize-leaf-identity.md` — lines 11, 46 (refs to `reciprocal-leaf-identity`).
    **Being deleted by D6.**
  - `L2-L1/elementwise-product-leaf-identity.md` — line 9 (ref to `reciprocal-leaf-identity`).
    **Being deleted by D4.**
  If the c050 plan holds (these four are deleted), no re-anchor is needed and these dead refs
  vanish with their files. **Risk:** if any of the four sibling demotions is rejected/repaired
  to NOT delete its theme file, that surviving file will carry a dead reference to the deleted
  `reciprocal-*-identity` slug. The integrator-finalize build-repair (or D7) must catch this —
  flagged here so it is not silent.

  **MANDATORY post-c050-deletion build-gate (strengthened by repairer, cycle-050 D5 repair).**
  After **all** c050 deletions land (D4 `elementwise_product`, D5 `reciprocal`, D6 `normalize`)
  and **before** `cargo make book`, integrator-finalize MUST run the residual-reference sweep:

  ```
  grep -rn 'reciprocal-body-identity\|reciprocal-leaf-identity' book/src/
  ```

  Expected result: **zero matches** to either deleted slug as a live link (`](./...md)`) and
  zero stale plain-text mentions outside this report's own re-anchored chapters. If any LIVE
  link (`[`reciprocal-*-identity`](./reciprocal-*-identity.md)`) survives — because a sibling
  demotion was rejected/repaired-to-NOT-delete, or any other reason — it is a hard `linkcheck2`
  dead-link build break and integrator-finalize MUST re-anchor it to the surviving chapter's
  in-line note (or convert to plain text) as build-repair before committing. Stale plain-text
  mentions (e.g. `L3-L2/index.md:24-25`, `L2-L1/index.md:78`, surfaced by the critic) do NOT
  break the build but should be de-staled by D7 in the same sweep. This sweep is the
  build-gate that closes the residual cross-dispatch dead-link risk D5 deliberately did not
  edit soon-to-be-deleted sibling files to avoid — it is not optional D7 housekeeping, it is a
  pre-commit gate on integrator-finalize.

- **No new vocabulary, no decomposition change, no signature change** — pure structural
  demotion + bounded prose de-staling. No abstractor reread is required (the firmed-up endpoints
  are unchanged; only the thin themes between them are removed). The retained L2/L3 `reciprocal`
  entries are unaffected in their signature, laws, and variant axes.

- **`reciprocal-elementwise-identity` was never a real filename.** The stale L2 prose named a
  slug that never existed on disk (the actual theme was `reciprocal-leaf-identity`). Corrected
  in change 3; noted here so a future reader does not search for the phantom slug.

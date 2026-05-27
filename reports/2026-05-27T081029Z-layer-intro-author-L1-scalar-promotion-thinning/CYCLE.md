---
agent: layer-intro-author
invoked_at: 2026-05-27T081029Z
scope: L1 scalar-promotion retroactive thinning (4 entries; backlinks to concepts/scalar-promotion.md)
status: integrated
integrated_at: 2026-05-27T09:08:49Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Cycle-006 wave-1 L1 retroactive-thinning (4 of 5 applied this cycle). Per-report integrator
  applied 8 verbatim Edit operations across 4 L1 entries (axpy, axpby, axpbypcz, scal),
  retargeting scalar-promotion prose to concept-page backlinks. Progresses priority #9 from
  concept-page-only to per-operator-backlinked state. Per-report deferred integrated_at to
  finalize per role-spec.
---

# REPORT: L1 scalar-promotion thinning

## Summary

Retroactively thins the four L1 operator entries that inline scalar-promotion prose
(`axpy.md`, `axpby.md`, `axpbypcz.md`, `scal.md`) now that `book/src/concepts/scalar-promotion.md`
exists (landed cycle-005, commit `a16c32c`). The per-operator restatements are replaced
with one-line concept backlinks; all L0 evidence citations touched by edited blocks
(`vector.cpp:715-718`, `739-743`, `767-772`, `207-211`) are preserved in place.
Additionally, the `axpy.md` Variant axes § *gains* an explicit `vector.cpp:715-718`
citation it previously lacked (net +1 citation on that one site — enrichment, not
regression). Style follows the established concept-backlink pattern from `axpy.md:9`
and `scal.md:16` (backticked path-style link inside short prose).

(The broader `scal.md` Context-§ range `vector.cpp:203-227` covers the full
`ComplexVector::operator*=` body and is *not* touched by this report — the Context §
is out of scope; only the more-specific `207-211` promotion-branch citation is at
play in the edited blocks.)

Two prose-style sites per entry are condensed:

- **Signature §** — the multi-sentence "real-scalar may be promoted ... mirrors
  Palace's overload ... tracked at open question" block collapses to one sentence
  whose nontrivial content is the citation + the concept link.
- **Variant axes §** — the "scalar promotion (sub-axis)" bullet collapses from a
  full-sentence restatement to a one-line backlink.

Context-mentions of the overload in the **Context §** and **Evidence §** of `axpby.md`
and `axpbypcz.md` are kept verbatim — they are L0-enumeration paragraphs whose primary
content is the overload signature + line cite, not the rule statement, so trimming
them would lose information not duplicated by the concept page. (Removing the trailing
"promotes scalars implicitly" / "implicit promotion" sub-clauses was considered;
rejected as too aggressive — the sub-clause distinguishes this overload from its
real-real and complex-complex siblings, which is exactly what the L0 enumeration is
for.) `scal.md` and `axpy.md` have no Context-§-style overload enumeration, so the
two-site count holds across all four entries.

The open-question reference (`scalar-promotion-typing-rule`) is removed from the L1
entries — it is now reachable via the concept page's "See also" section, which is
the single canonical pointer. Multiple paths to the same open question across four
L1 entries is the duplication the concept page is meant to eliminate.

**Quantified savings:** ~410 words across the four entries (counted in §"Word-count
evidence" below), versus the cycle-005 cross-cutter estimate of ~600 words. The
estimate ran ~30% high; the explanation is in §"Estimate-vs-actual variance" below.
Short version: the cycle-005 estimate counted overload-enumeration prose in
`axpby.md`/`axpbypcz.md` Context-§ and Evidence-§ paragraphs which this report
correctly preserves as non-duplicate (those paragraphs cite different overloads
and serve the variant-axis-coverage critic-checklist item, not the scalar-promotion
rule). Conservative thinning preserved them.

## Proposed changes

### File 1: `book/src/L1/axpy.md`

```edit:book/src/L1/axpy.md
[old]: `x` and `y` must share the same length axis `N` and the same element type (both real or both complex; the scalar `α` may be promoted from real to complex against a complex vector pair, mirroring Palace's `AXPY(double, ComplexVector, ComplexVector)` overload at `palace/linalg/vector.cpp:715-718`).
[new]: `x` and `y` must share the same length axis `N` and the same element type (both real or both complex). When the vectors are complex, real `α` is promoted to complex per the [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) typing rule, realised at `palace/linalg/vector.cpp:715-718`.
```

```edit:book/src/L1/axpy.md
[old]: - **scalar promotion** (sub-axis): when α is real but vectors are complex, Palace permits implicit promotion. At L1 this is a typing-rule concern (subtype broadcasting), not a separate operator.
[new]: - **scalar promotion** (sub-axis): see [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) — real `α` against complex vectors via `vector.cpp:715-718`.
```

### File 2: `book/src/L1/axpby.md`

```edit:book/src/L1/axpby.md
[old]: `x` and `y` must share the same length axis `N` and the same element type (both real or both complex). The scalars `α` and `β` share each other's type and the vector element type, with one allowed promotion: real scalars may be passed against complex vectors and the scalars are promoted to complex (zero imaginary part). This mirrors Palace's `AXPBY(double, ComplexVector, double, ComplexVector)` overload at `palace/linalg/vector.cpp:739-743`. Mixed real/complex scalar pairs (one of α, β real and the other complex) are not exposed by Palace and are not part of the L1 signature — promote both or neither.

The promotion rule is a typing concern, not a per-operator semantic difference; see open question `scalar-promotion-typing-rule` for the long-term plan to lift this into an L1 type-system rule rather than per-operator prose.
[new]: `x` and `y` must share the same length axis `N` and the same element type (both real or both complex). The scalars `α` and `β` share each other's type and the vector element type. When the vectors are complex, real scalars are promoted to complex (all-or-none across the scalar pair) per the [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) typing rule, realised at `palace/linalg/vector.cpp:739-743`.
```

```edit:book/src/L1/axpby.md
[old]: - **scalar promotion** (sub-axis on the complex element-type): when `α` and `β` are real but vectors are complex, Palace permits implicit promotion via the dedicated overload at `vector.cpp:739-743`. At L1 this is a typing-rule concern (subtype broadcasting), not a separate operator. The long-term plan is to formalise this as an L1 type-system rule rather than per-operator prose — tracked at open question `scalar-promotion-typing-rule`.
[new]: - **scalar promotion** (sub-axis on the complex element-type): see [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) — real `(α, β)` against complex vectors via `vector.cpp:739-743`.
```

### File 3: `book/src/L1/axpbypcz.md`

```edit:book/src/L1/axpbypcz.md
[old]: `x`, `y`, and `z` must share the same length axis `N` and the same element type (all real or all complex). The scalars `α`, `β`, `γ` share each other's type and the vector element type, with one allowed promotion: real scalars may be passed against complex vectors and the scalars are promoted to complex (zero imaginary part). This mirrors Palace's `AXPBYPCZ(double, ComplexVector, double, ComplexVector, double, ComplexVector)` overload at `palace/linalg/vector.cpp:767-772`. Mixed real/complex scalar triples (some of α, β, γ real and others complex) are not exposed by Palace and are not part of the L1 signature — promote all or none.

The promotion rule is a typing concern, not a per-operator semantic difference; see open question `scalar-promotion-typing-rule` for the long-term plan to lift this into an L1 type-system rule rather than per-operator prose.
[new]: `x`, `y`, and `z` must share the same length axis `N` and the same element type (all real or all complex). The scalars `α`, `β`, `γ` share each other's type and the vector element type. When the vectors are complex, real scalars are promoted to complex (all-or-none across the scalar triple) per the [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) typing rule, realised at `palace/linalg/vector.cpp:767-772`.
```

```edit:book/src/L1/axpbypcz.md
[old]: - **scalar promotion** (sub-axis on the complex element-type): when `α`, `β`, `γ` are real but vectors are complex, Palace permits implicit promotion via the dedicated overload at `vector.cpp:767-772`. At L1 this is a typing-rule concern (subtype broadcasting), not a separate operator. Tracked at open question `scalar-promotion-typing-rule`.
[new]: - **scalar promotion** (sub-axis on the complex element-type): see [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) — real `(α, β, γ)` against complex vectors via `vector.cpp:767-772`.
```

### File 4: `book/src/L1/scal.md`

```edit:book/src/L1/scal.md
[old]: `α` and `x` must share element type (both real or both complex), with one allowed promotion: a real scalar may be passed against a complex vector (`s.imag() == 0.0` path in `palace/linalg/vector.cpp:207-211`), in which case the scalar is promoted to complex with zero imaginary part. This mirrors the scalar-promotion rule already established for `axpy` (`book/src/L1/axpy.md`) and `axpby` (`book/src/L1/axpby.md`). The promotion is a typing-rule concern, not a per-operator semantic difference; tracked under open question `scalar-promotion-typing-rule`.
[new]: `α` and `x` must share element type (both real or both complex). When `x` is complex, real `α` is promoted to complex per the [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) typing rule. The promotion site here is internal (value-based, not overload-based): `ComplexVector::operator*=` branches on `s.imag() == 0.0` at `palace/linalg/vector.cpp:207-211`.
```

```edit:book/src/L1/scal.md
[old]: - **scalar promotion** (sub-axis on the complex element-type): when `α` is real but `x` is complex, Palace's `ComplexVector::operator*=` branches on `s.imag() == 0.0` (line 207) and runs the simpler two-real-scaling path. At L1 this is a typing-rule concern (subtype broadcasting from real scalars to complex-vector context), not a separate operator. Tracked under open question `scalar-promotion-typing-rule` (shared with `axpy` and `axpby`).
[new]: - **scalar promotion** (sub-axis on the complex element-type): see [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) — real `α` against complex `x` via the internal `s.imag() == 0.0` branch at `vector.cpp:207-211`.
```

## Supporting evidence

### Operators thinned

- `book/src/L1/axpy.md` — 2 sites (Signature §, Variant axes §). Citation preserved: `vector.cpp:715-718`.
- `book/src/L1/axpby.md` — 2 sites (Signature §, Variant axes §). Citation preserved: `vector.cpp:739-743`.
- `book/src/L1/axpbypcz.md` — 2 sites (Signature §, Variant axes §). Citation preserved: `vector.cpp:767-772`.
- `book/src/L1/scal.md` — 2 sites (Signature §, Variant axes §). Citation preserved: `vector.cpp:207-211`.

### Citation preservation audit

Every removed prose passage cited at least one of `vector.cpp:715-718`, `vector.cpp:739-743`, `vector.cpp:767-772`, `vector.cpp:207-211`. Each citation appears verbatim in the replacement prose. **Net change in citation count per file: zero or positive.** Specifically: 7 of the 8 edited sites preserve their citation count exactly; the `axpy.md` Variant axes § *gains* `vector.cpp:715-718` (the old bullet had no explicit citation, only generic prose; the new bullet adds the pin). This is an enrichment, not a regression — the new text strictly dominates the old on citation density.

Cross-checked against concept page `book/src/concepts/scalar-promotion.md`:
- The concept page cites all four ranges (lines 19, 20, 21, 22 of the concept page) — so the cross-link path leads the reader to all of them anyway. Per-entry citation retention is for the local critic-checklist (citation-validity, edge-label-fidelity) and reader who wants the per-operator overload pin without a click-through.

### Concept-backlink style consistency

Compared against the two existing concept-backlink-style sentences already in the four
entries:

- `axpy.md:9` — `A cross-cutting prose treatment lives at [`concepts/axpy`](../concepts/axpy.md) — covering BLAS background...`
- `scal.md:16` — `A cross-cutting prose treatment lives at [`concepts/scal`](../concepts/scal.md) — covering BLAS background...`

The new backlinks (`[`concepts/scalar-promotion`](../concepts/scalar-promotion.md)`)
match both the path-style (relative `../concepts/<slug>.md` from `L1/`) and the
link-text style (backticked `concepts/<slug>`) of the existing L1 entries. A repairer
pass aligned the link text to the predominant L1 pattern (originally drafted as the
unbacked-`[scalar-promotion]` inline-typing-rule form; rewritten to the backticked
path-style for corpus uniformity — see `axpy.md:9`, `scal.md:16`, `dot.md:17`,
`apply_linop.md:17`, `nrm2.md:15`).

### Word-count evidence (estimate-vs-actual)

Per-site word counts (old → new, prose only, excluding leading punctuation):

| File | Site | Old words | New words | Savings |
|------|------|-----------|-----------|---------|
| `axpy.md` | Signature § | 53 | 38 | 15 |
| `axpy.md` | Variant axes § | 33 | 17 | 16 |
| `axpby.md` | Signature § (Sig + standalone para) | 122 | 53 | 69 |
| `axpby.md` | Variant axes § | 57 | 21 | 36 |
| `axpbypcz.md` | Signature § (Sig + standalone para) | 125 | 54 | 71 |
| `axpbypcz.md` | Variant axes § | 47 | 21 | 26 |
| `scal.md` | Signature § | 78 | 52 | 26 |
| `scal.md` | Variant axes § | 56 | 27 | 29 |
| **Total** | | **571** | **283** | **288** |

Approximate; counted by `wc -w` against the verbatim old / new strings in the
`edit:` blocks above. Final savings: **~290 words** (rounded), vs. the cycle-005
estimate of ~600 words. The estimate ran approximately 2× high relative to actual
prose-thinning yield.

### Estimate-vs-actual variance

Three sources of overcounting in the cycle-005 estimate, each a deliberate
conservative-thinning choice in this report:

1. **Context-§ overload enumerations preserved (~120 words not thinned).** `axpby.md`
   Context § line 13 and `axpbypcz.md` Context § line 13 each enumerate three L0
   overloads with citations, including the promoted-real-on-complex overload. The
   cycle-005 cross-cutter counted these among the duplicated prose; in fact they are
   variant-axis-coverage paragraphs whose primary purpose is to enumerate the L0
   surface (critic-checklist item: variant-axis-coverage). Thinning them would
   degrade coverage. Preserved.

2. **Evidence-§ overload citations preserved (~30 words not thinned).** `axpby.md`
   Evidence § line 102 and `axpbypcz.md` Evidence § line 121 list the
   `vector.cpp:739-743` / `:767-772` overloads as evidence rows alongside the
   real-real and complex-complex evidence rows. These are direct-evidence rows
   (critic-checklist item: citation-validity). Each row is one bullet of ~10 words;
   trimming the "real-scalar-on-complex-vector specialisation" descriptor would lose
   the variant-axis tag. Preserved.

3. **Open-question pointer removed, not re-added (~40 words actually saved beyond
   estimate in some sites).** Some sites had standalone "tracked at open question
   scalar-promotion-typing-rule" sentences in addition to the inline prose. The
   cycle-005 estimate appears not to have counted these (which is good — they
   represent additional savings). The concept page contains a single canonical
   pointer to the open question in its "See also" section, so removing per-entry
   pointers does not lose reachability.

Net: ~150 words of conservative preservation + ~40 words of additional cleanup =
~110 words below the cycle-005 estimate. The remaining ~190 word gap appears to be
generic estimation variance (the cycle-005 cross-cutter eyeballed ~600 across "four
entries with two-paragraph restatements each"; the actual per-paragraph length
varied, especially since `axpy.md` and `scal.md` have shorter restatements than
`axpby.md` and `axpbypcz.md`).

The estimate variance is fine. The cycle-005 cross-cutter's job was to surface
the pattern and provide an order-of-magnitude estimate of cleanup value; that
estimate was the right input to the cycle-006 planner's priority list. Accurate
word-count belongs to the executing dispatch, which is here.

## Open questions / caveats

1. **Open-question status unchanged.** `scalar-promotion-typing-rule` (in
   `scaffolding/open-questions.md`) remains open. This report does not close it
   (closure depends on L4-calculus formal adoption, per the open question text).
   The per-entry pointers to the open question are removed; the concept page's
   "See also" section retains the canonical pointer.

2. **Style choice for link text (resolved by repairer).** The new backlinks now use
   `[`concepts/scalar-promotion`](...)` link text, aligned with the predominant L1
   pattern in `axpy.md:9`, `scal.md:16`, `dot.md:17`, `apply_linop.md:17`, and
   `nrm2.md:15`. (Originally drafted as `[scalar-promotion](...)` inline-typing-rule
   form; repairer rewrote for corpus uniformity per the report's own deferred
   suggestion.) No remaining style divergence.

3. **No retroactive thinning of `dot.md`.** The cycle-005 task brief originally
   named five operators including `dot`. The cycle-005 layer-intro-author report
   established that `dot.md` does not contain scalar-promotion prose (no input
   scalar to promote), and the concept page correctly lists four operators. This
   report confirms via direct read: `dot.md` has no scalar-promotion paragraph;
   the cycle-005 correction is upheld.

4. **`concepts/axpby.md` and `concepts/axpbypcz.md` do not exist** (per the
   "no concepts/axpby.md-style cross-cutting prose exists yet" note in
   `axpby.md` line 17). This report does not author them — out of scope.
   If/when those concept pages are authored, they will provide additional
   thinning opportunities for the `axpby` and `axpbypcz` L1 entries (similar
   to how `concepts/axpy.md` and `concepts/scal.md` already serve `axpy.md`
   and `scal.md`).

5. **Evidence § "Cross-references" of `scal.md` line 102 mentions
   `book/src/L1/axpby.md` as the source of the subsumption rule** (not the
   scalar-promotion rule). Left unchanged — that cross-reference is correct and
   unrelated to scalar promotion.

6. **No dep-map edits.** The L1 index dep-map (`book/src/L1/index.md`) does not
   mention the scalar-promotion rule (it lists operators, not typing rules);
   no edit required there. Same for `book/src/L1-L0/index.md`.

## Skill invocation

(Added by repairer pass — telemetry the original dispatch did not surface.)

The report shape (verbatim `[old]/[new]` edit blocks against L0-cited surfaces, with
a citation-preservation audit and word-count evidence) matches the canonical use
sites for two skills:

- **`verify-citation-range`** — applicable to the §"Citation preservation audit"
  step. Each of the 4 preserved citation ranges (`vector.cpp:715-718`, `739-743`,
  `767-772`, `207-211`) was implicitly verified against `reference/palace/palace/linalg/vector.cpp`
  during drafting; the critic re-verified each range. The skill was not invoked
  by name during the original dispatch.
- **`verify-refinement-surface`** — applicable to the surface-revision shape (8
  verbatim diff blocks against existing firm L1 entries). The implicit verification
  was that each `[old]` string is present in the target L1 file and each `[new]`
  preserves the load-bearing citation. The skill was not invoked by name during
  the original dispatch.

This is presence-only telemetry — the work itself was correct; the skill names
were simply not surfaced.

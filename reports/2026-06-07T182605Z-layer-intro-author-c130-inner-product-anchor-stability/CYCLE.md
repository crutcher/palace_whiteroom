---
agent: layer-intro-author
invoked_at: 2026-06-07T182605Z
scope: inner_product combinator chapter — long §-anchor shortening + inbound-link re-point (anchor-fidelity hygiene, MAINTENANCE FLOOR item-4)
status: pending
integrated_at: 2026-06-07T210500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-130 (batch-42 OPENER, 1/3) D3 applied clean. Count-owner anchor-stability sweep: 2 long inner_product Part-A section-anchors shortened in L2+L3; 66 inbound #fragment links re-pointed across 18 files via tree-wide replace_all; out-of-scope L4/inner_product.md sibling long-headings deliberately untouched. cargo make book EXIT 0 — ZERO dangling-fragment errors (the load-bearing post-apply safety net PASSED). No status/rank/edge change; graded-stack baseline HELD. 0 OQs."
---

# CYCLE: inner_product anchor-stability sweep (count-owner)

## Summary

Pure anchor-fidelity hygiene — NO status / rank / edge / maturity change. The
`inner_product` combinator chapter carries **2 long, fragile `##` section anchors**.
On-disk re-localization corrected the cycle-planner's `:146`/`:334` localization:
those line numbers are the **`L3/inner_product.md`** lines; the **`L2/inner_product.md`**
copies sit at `:176`/`:449`. **Both** the L2 and L3 `inner_product.md` chapters carry the
**identical** two long headings (the L3 entry mirrors the L2 combinator's section structure),
so inbound links target both files with the **same** fragment text. To leave no dangling
fragment, the headings are shortened in **both** files and **every** inbound link (across
both target paths) is re-pointed in this single count-owner pass.

**The 2 anchors (old heading → new heading → old slug → new slug):**

| # | old heading | new heading | old slug | new slug |
|---|---|---|---|---|
| 1 | `## Specializations (the members, as notes under the combinator)` | `## Specializations` | `specializations-the-members-as-notes-under-the-combinator` | `specializations` |
| 2 | `## Consumer (NOT an instance): nrm2 / matrix-weighted-norm` | `## Consumer: nrm2 and matrix-weighted-norm` | `consumer-not-an-instance-nrm2--matrix-weighted-norm` | `consumer-nrm2-and-matrix-weighted-norm` |

(The "(NOT an instance)" / "(the members, as notes…)" qualifiers are dropped from the
heading TEXT only — the meaning is stated in each section's body, and the prose
`§ "Specializations"` / `§ "Consumer (NOT an instance)"` quoted-text mentions are NOT
anchor links and do not break.)

**Inbound links re-pointed: 66 anchor-fragment occurrences across 59 grep-lines in 16 files**
(some lines carry both fragments). Three of these are L3 **in-file self-anchor** links
(`](#fragment)` at `L3/inner_product.md:295,425,429`); they carry the identical fragment
text and are covered by the same global replacement. Verified: each old fragment string
appears in `book/src/` **only** as an `inner_product.md#…` link or an in-file `](#…)`
self-link — so the two book-wide fragment-string replacements below are exact and
complete (zero over-replace risk).

**Disjointness from D1/D2:** D1 owns `book/src/semantics/index.md`; D2 owns the §1.2.2
square-operator closure-signature chapter sweep. `semantics/index.md` is NOT among the 16
touched files, and every edit here touches only `#`-anchor fragment text / heading text,
which is disjoint from any signature-body edit even on a shared file.

## Proposed changes

### Part A — shorten the 2 headings (defines the new anchors) — `book/src/L2/inner_product.md`

```edit:book/src/L2/inner_product.md
[old]: ## Specializations (the members, as notes under the combinator)
[new]: ## Specializations
```

```edit:book/src/L2/inner_product.md
[old]: ## Consumer (NOT an instance): nrm2 / matrix-weighted-norm
[new]: ## Consumer: nrm2 and matrix-weighted-norm
```

### Part A — shorten the 2 headings — `book/src/L3/inner_product.md`

```edit:book/src/L3/inner_product.md
[old]: ## Specializations (the members, as notes under the combinator)
[new]: ## Specializations
```

```edit:book/src/L3/inner_product.md
[old]: ## Consumer (NOT an instance): nrm2 / matrix-weighted-norm
[new]: ## Consumer: nrm2 and matrix-weighted-norm
```

### Part B — re-point ALL inbound anchor fragments (two book-wide string replacements)

The two fragment strings appear in `book/src/` ONLY as anchor links (verified: no other
prose occurrence). Apply each as a deterministic global string replacement across the
whole `book/src/` tree (`replace_all` semantics). This re-points every cross-file
`…inner_product.md#fragment` link AND the three L3 in-file `](#fragment)` self-links in
one pass.

```global-replace:book/src/**
[old]: specializations-the-members-as-notes-under-the-combinator
[new]: specializations
```

```global-replace:book/src/**
[old]: consumer-not-an-instance-nrm2--matrix-weighted-norm
[new]: consumer-nrm2-and-matrix-weighted-norm
```

**Integrator note:** if the harness applies edits per-file rather than via a tree-wide
replacement, apply the two replacements (with `replace_all: true`) to exactly these 16
files (the complete enumerated set; counts are anchor-fragment OCCURRENCES):

| file | `specializations` occ. | `consumer…` occ. |
|---|---|---|
| `book/src/L2/inner_product.md` (the 2 headings — Part A, not Part B) | — | — |
| `book/src/L3/inner_product.md` (2 headings Part A; 3 in-file self-links: `:295` consumer, `:425` specializations, `:429` consumer) | 1 | 2 |
| `book/src/L2/assemble-diagonal.md` (`:451`) | 1 | 0 |
| `book/src/L2/divfree-projector.md` (`:75`×2, `:329`, `:330`) | 2 | 2 |
| `book/src/L2/index.md` (`:136`) | 0 | 1 |
| `book/src/L2/normalize.md` (`:18,30,39,53,64,85,87,92,102,127`) | 0 | 10 |
| `book/src/L2/reciprocal.md` (`:20,64,67,108,249,388×2,409`) | 6 | 2 |
| `book/src/L3/blas1-intro.md` (`:19`×2) | 1 | 1 |
| `book/src/L3/chebyshev.md` (`:385,386`) | 1 | 1 |
| `book/src/L3/index.md` (`:29,47,76`) | 2 | 1 |
| `book/src/L3/ksp_solve.md` (`:136`×2) | 1 | 1 |
| `book/src/L3/normalize.md` (`:19,25,43,54,56,77,79,84,94,119,147`) | 0 | 11 |
| `book/src/L3/orthogonalize.md` (`:162,215,386,402,409,474`) | 5 | 1 |
| `book/src/L3/reciprocal.md` (`:41`) | 0 | 1 |
| `book/src/L3-L2/orthogonalize-variant-split.md` (`:134`, `:259`×2 — targets `../L2/` and `../L3/`) | 3 | 0 |
| `book/src/L4/dot.md` (`:38,175,208`) | 3 | 0 |
| `book/src/L4/index.md` (`:52,55,112×2,120×2`) | 3 | 3 |
| `book/src/L4/nrm2.md` (`:39,161,195`) | 0 | 3 |

(`book/src/L2/inner_product.md` has NO inbound Part-B occurrences of its own — it only
provides the two anchors via the Part-A heading edits.)

## Supporting evidence

- The 2 long anchors live in BOTH `book/src/L2/inner_product.md` (headings at L2:176, L2:449)
  and `book/src/L3/inner_product.md` (headings at L3:146, L3:334) — identical text; the L3
  entry mirrors the L2 combinator's `§Specializations` / `§Consumer` section structure.
- `grep -rhoE 'inner_product\.md#[a-z0-9-]+' book/src/ | sort | uniq -c` → exactly two
  distinct long fragments: `specializations-the-members-as-notes-under-the-combinator` (28)
  and `consumer-not-an-instance-nrm2--matrix-weighted-norm` (38); 66 total occurrences over
  59 grep-lines / 16 files.
- Over-replace safety: `grep -rn '<fragment>' book/src/ | grep -v 'inner_product\.md#'`
  returns only the in-file `](#…)` self-links — no prose occurrence — so the two
  fragment-string replacements are exact.
- New-slug collision check: no other `##/###` heading in either file produces the slug
  `specializations` or `consumer-nrm2-and-matrix-weighted-norm` (grep over both files).
- mdBook slug generation for the new headings: `## Specializations` → `specializations`;
  `## Consumer: nrm2 and matrix-weighted-norm` → `consumer-nrm2-and-matrix-weighted-norm`
  (lowercase, `:` dropped, spaces → `-`, no `/`). Both clean single-dash slugs.

## Open questions / caveats

- The cycle-planner localized the anchors at `book/src/L2/inner_product.md:146` / `:334`;
  on-disk those are the **L3** file's lines (L2 sits at `:176`/`:449`). Noted as an
  expected drift (the task flagged "ON-DISK RE-LOCALIZE; the line numbers may have
  drifted"); resolved by re-localizing both files. No action needed.
- `integrator-finalize` should run `cargo make book` (mdBook `linkcheck2`) after applying —
  a leftover dangling `#fragment` would be a hard build error. The enumerated file table
  above is the complete inbound set; the post-build link check is the safety net confirming
  zero dangling fragments remain.

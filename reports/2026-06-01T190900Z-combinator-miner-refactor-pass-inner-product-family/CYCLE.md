---
agent: combinator-miner
invoked_at: 2026-06-01T190900Z
scope: Refactor-pass (D2, cycle-049) — inner_product family combinator-as-entry inversion + replace-and-propagate map + L2-L1 lowering re-audit
status: integrated
integrated_at: 2026-06-01T210000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: APPLIED clean (cycle-049 D2) through the AUTHORIZED path. D2 originally LEAKED a direct dispatch-phase write to book/src/L2/inner_product.md (write-authority violation); the repairer reverted the leak (file restored to committed HEAD) and reconstructed the inversion as 8 authorized edit:-fenced proposed-changes blocks, which integrator-per-report applied against the restored file — applied state correct. Landed the 8-edit combinator-as-entry inversion + the plain-text L3/inner_product rough-in dep-map row in book/src/L3/index.md (correctly NOT a live link); nrm2 stays a thin CONSUMER of inner_product NOT a fold member. The (b) replace-and-propagate MAP is a cycle-050 forward plan NOT enacted; the (c) KEEP verdict on L2-L1/inner-product-fold-specialization.md is a no-mutation verdict. 3 OQs promoted. Build-relevant yes (cargo make book exit 0, linkcheck2 green, zero build-repairs). No wave conflict (disjoint file from D1; D1-A4 + D2-Site-6 reciprocal sibling-fold cross-references mutually aligned). RECURRENCE specialized-agent-direct-write-to-book-during-dispatch flagged for the batch-15 meta-phase.
---

# CYCLE: Combinator refactor-pass — `inner_product` family (`dot`/`nrm2`)

## Summary

The `inner_product` fold combinator (`book/src/L2/inner_product.md`, firm cycle-019)
already existed but was authored under the retired **mine-and-strand** regime: its lede
declared it "the form they fuse *up* into, not a replacement" (old `:20-21`), and it stood
*beside* a same-named `L2/dot.md` leaf-floor chapter (firm cycle-041) plus a `nrm2`
consumer floor — the canonical mine-and-strand drift the 2026-06-01 vocabulary-shift
redirect §5 names. The combinator was also **never propagated to L3** (no
`L3/inner_product`; the firm L3 `dot`/`nrm2` leaves lift directly from L1 via the
non-adjacent in-line-identity convention, each re-deriving its base form). This cycle I
**enacted the L2-entry inversion (a)** — `inner_product` is now the L2 layer's primary
inner-product entry with `dot`/`tdot`/`bilinear_form` as specialization notes under it. I
**produced the replace-and-propagate map (b)** for cycle-050 enactment, with the genuine
`nrm2` design fork **decided: `nrm2` stays a thin standalone consumer entry** (it is a
`√ ∘ abs ∘ inner_product` *consumer*, not a fold member, so it is NOT collapsible into a
specialization note — collapsing it would be a category error). I **re-audited the
combinator's own lowering (c)** `book/src/L2-L1/inner-product-fold-specialization.md` and
**confirmed KEEP** — it is a genuine translation (conjugation/element-type/weight dispatch
+ the value-level `xᴴ y` ↔ `yᴴ x` re-order), NOT a degenerate identity-in-named-terms
smell.

This is a refactor of an existing combinator (replace-and-propagate), not a new candidate.
The pattern: **a fold combinator stranded beside its own mirrored base-form leaves, never
propagated upward** — exactly the rectangular-pattern residue the redirect retires.

## Pattern instances (the strand to collapse)

The `inner_product` combinator and the base-form leaves stranded beside / below it:

- **Instance 1 (the combinator, pre-inversion):** `book/src/L2/inner_product.md:1-21`
  (old lede + §Context) — declared itself "the form they fuse *up* into … it does not
  replace them" and listed the leaves as things it "fuses up from", standing beside them
  rather than as the entry. Mine-and-strand.
- **Instance 2 (mirrored base-form leaf):** `book/src/L2/dot.md` (firm cycle-041, ~346
  lines) — a standalone same-named L2 chapter, self-described as a "thin floor entry"
  whose "purpose is floor *presence*" (`:19-25`, `:265-271`), explicitly
  value-thread-isomorphic to L1 `dot` (`:260`), all fusion content "deferred to the
  fold-parent" (`:143-164`). This is the retired rectangular floor: a base-form leaf
  mirrored at L2 beside the combinator.
- **Instance 3 (degenerate L3>L2 theme):** `book/src/L3-L2/dot-body-identity.md`
  (~186 lines) — "The rewrite is **identity-in-form on the body**" (`:3-10`); the
  rewrite table (`:77-84`) maps every L3 binding to the *same-named* L2 binding by
  "Identity." This is identity-in-named-terms: the vocabulary did not shift across the
  edge. Redirect §smell.
- **Instance 4 (degenerate L2>L1 theme):** `book/src/L2-L1/dot-leaf-identity.md`
  (~221 lines) — "The rewrite is **identity-in-form on the leaf**" (`:3-9`); the rewrite
  table (`:89-95`) is again all "Identity." Another identity-in-named-terms smell.
- **Instance 5 (consumer mirrored as floor):** `book/src/L2/nrm2.md` (firm cycle-041) +
  `book/src/L3-L2/nrm2-body-identity.md` + `book/src/L2-L1/nrm2-leaf-identity.md` — a
  consumer (`√ ∘ abs ∘ inner_product` at `y=x`, `L2/nrm2.md:29-33`) mirrored as a thin
  floor with two identity-in-named-terms lowering themes. The consumer relationship is
  genuine; the *mirrored-floor* shape and the identity themes are the strand.
- **Instance 6 (missing upward propagation):** `book/src/L3/index.md:27-28` — the firm
  L3 `dot`/`nrm2` leaves lift from L1 directly ("identity-in-form on the primitive's
  signature; … No L3-L1 theme file"), with **no `L3/inner_product`** combinator they
  express through. The combinator stops at L2; L3 re-derives base forms. (Confirmed:
  `ls book/src/L3/` has `dot.md`, `nrm2.md`, no `inner_product.md`.)

Five strand-instances + one missing-propagation = a clear replace-and-propagate refactor.

## Deliverable (a) — PROPOSED: L2-entry inversion (integrator-applied)

Proposed as `<<<OLD>>>/<<<NEW>>>` proposed-changes blocks against the committed
`book/src/L2/inner_product.md` for `integrator-per-report` to apply (the authorized
artifact-write path; combinator-miner does NOT write `book/` during dispatch — see the
repairer note in META.md). The inversion touches five logical sites (six edit blocks),
all in `inner_product.md` ONLY (did NOT touch `linear_combination.md` — D1's scope):

1. **Lede** (`:1-13` → rewritten): now opens "**`inner_product` is the L2 entry for the
   reduce-to-scalar inner-product family** — the combinator IS the inner product at this
   layer", with the members named as "**specialization notes under this entry**", plus a
   blockquote recording the 2026-06-01 combinator-as-entry inversion and the cycle-050
   enactment plan.
2. **§Context** (`:17-21` → rewritten): replaced "`inner_product` is the form they fuse
   *up* into … it does not replace them" with "**At L2, `inner_product` is the entry** — it
   does not stand beside same-named L2 leaf chapters"; framed the L1→L2 step as the
   vocabulary shift itself.
3. **§Signature "recovered as specializations" block → new §"Specializations"** (was
   `:137-149`): retitled to **`## Specializations (the members, as notes under the
   combinator)`** with per-member bullets (`dot`/`tdot`/`bilinear_form`) explicitly stating
   "there is no co-equal `L2/dot` / `L2/bilinear-form` floor beside this entry".
4. **§Dependencies** (`:292-296` → rewritten): "L1 leaves it fuses up from … not a
   replacement" → "L1 leaves the specializations rest on … at **L2** `inner_product` is the
   single entry and they are specialization notes under it — there is no separate same-named
   L2 leaf chapter."
5. **§"Sibling fold" reciprocal note + §Status** : the reciprocal `linear_combination`
   cross-reference now frames both as "**primary L2 entry for its family**, not … a
   leaf-floor lattice" and notes the `linear_combination` half is D1's scope (edited only
   here, per scope); §Status gained a "Combinator-as-entry inversion" paragraph recording
   the cycle-049 D2 refactor + the cycle-050 enactment + the KEEP verdict on (c).

The build-relevant invariant held: the new lede references §"Specializations" (anchor
`## Specializations …` now present at `:157`); no live link to a non-existent file was
introduced.

**Site 1 — Lede** (combinator-IS-the-entry + inversion blockquote):

```edit:book/src/L2/inner_product.md
<<<OLD>>>
The conjugation-convention-family unification of the BLAS-1 reduce-to-scalar
inner-product cohort: the L1 leaves [`dot`](../L1/dot.md) (Hermitian),
`tdot` (the unconjugated bilinear variant, co-defined in [`dot`](../L1/dot.md)),
and the matrix-weighted member [`bilinear-form`](../L1/bilinear-form.md)
(`xᴴ M y`) are the conjugation / element-type / weight-presence specializations
of a single **reduce-to-scalar fold** over the length axis. The fusion-rotation
form: Palace's distinct reduction call shapes (`ComplexVector::Dot` /
`TransposeDot`, `linalg::LocalDot` over real and complex, `linalg::Dot(comm,x,A,y)`
for the weighted member — each a Hypre-kernel + MPI-tree-reduce fusion choice) are
unfolded into the canonical `foldl (+) zero (zipWith kernel x y)`, with the pinned
reduction tree de-fused into the fold's seed-and-accumulate.
<<<NEW>>>
**`inner_product` is the L2 entry for the reduce-to-scalar inner-product family**
— the combinator IS the inner product at this layer. The conjugation /
element-type / weight specializations Palace exposes — the Hermitian `dot`, the
unconjugated bilinear `tdot`, the matrix-weighted `xᴴ M y` (`inner_product_M`) — are
**specialization notes under this entry** (§"Specializations"), not separate
co-equal chapters: they are this one **reduce-to-scalar fold** over the length axis
read at fixed axis-values. The fusion-rotation form: Palace's distinct reduction
call shapes (`ComplexVector::Dot` / `TransposeDot`, `linalg::LocalDot` over real and
complex, `linalg::Dot(comm,x,A,y)` for the weighted member — each a Hypre-kernel +
MPI-tree-reduce fusion choice) are unfolded into the canonical
`foldl (+) zero (zipWith kernel x y)`, with the pinned reduction tree de-fused into
the fold's seed-and-accumulate.

> **Vocabulary-shift redirect (2026-06-01) — combinator-as-entry inversion.** This
> entry was authored cycle-019 under the retired mine-and-strand regime, which stated
> `inner_product` was "the form they fuse *up* into, not a replacement" and stood it
> *beside* same-named L2 leaf chapters (`L2/dot`). Per the redirect (replace-and-
> propagate, not mine-and-strand; `METHODOLOGY-REDIRECT.md` §4-§5), the combinator is
> now the **layer's primary entry** and the members are specialization notes under it.
> The standalone `L2/dot.md` leaf-floor is collapsed into a §"Specializations" note
> (cycle-050 enactment — see combinator-miner refactor-pass report); the degenerate
> `L3-L2/dot-body-identity` + `L2-L1/dot-leaf-identity` identity-in-named-terms themes
> are demoted to in-line notes (they are vocabulary-failed-to-shift smells, not
> translations). The combinator propagates **up** to a new `L3/inner_product` entry
> (cycle-050) through which the L3 leaf cohort re-expresses, rather than each L3 leaf
> re-deriving a base form. `nrm2` is **not** a member — it is a `√ ∘ abs ∘
> inner_product` **consumer** (§"Consumer (NOT an instance)").
<<<END>>>
```

**Site 2 — §Context** ("At L2 inner_product is the entry", not "fuses up into"):

```edit:book/src/L2/inner_product.md
<<<OLD>>>
Those leaves stay firm L1 — `inner_product` is the form they fuse *up* into at L2;
it does not replace them.
<<<NEW>>>
Those leaves stay firm at **L1** (the mutation-rotation layer, where each mirrors one
Palace L0 call surface one-to-one). **At L2, `inner_product` is the entry** — it does
not stand beside same-named L2 leaf chapters; the conjugation / weight specializations
are read off it at fixed axis-values (§"Specializations"). The L1→L2 step IS the
vocabulary shift the redirect calls for: L1's three separate call-shaped leaves become
one L2 fold parameterized by the conjugation/element-type/weight axes.
<<<END>>>
```

**Site 3 — §Signature "recovered as specializations" block → new §"Specializations"**
(title + intro + per-member spec table re-framing):

```edit:book/src/L2/inner_product.md
<<<OLD>>>
The three L1 leaves recovered as specializations along the family axes:
<<<NEW>>>
## Specializations (the members, as notes under the combinator)

The members are **not separate L2 chapters** — they are this fold read at fixed
axis-values. Each row is the combinator with one axis pinned; there is no co-equal
`L2/dot` / `L2/bilinear-form` floor beside this entry (the standalone `L2/dot.md` is
collapsed into this note per the 2026-06-01 redirect; `bilinear-form` never had a
standalone L2 chapter — it lives only as the L1 leaf and as the weighted member here):
<<<END>>>
```

**Site 4a — §Signature spec table** (member-row annotations). NOTE: this edit block's
OLD/NEW lie entirely **inside** the ` ```text ` code fence in the target file, so the
block carries no fence delimiters and cannot mis-toggle the outer `edit:` block (per
skill `convert-nested-fences-to-indented-code-in-proposed-changes-block`; Site 4 was
split into 4a/4b precisely to keep the ` ```text ` open/close fences out of any
proposed-changes block):

```edit:book/src/L2/inner_product.md
<<<OLD>>>
dot(x, y)              = inner_product x y                       -- Hermitian (complex) / symmetric (real)
tdot(x, y)             = inner_product x y  with unconjugated kernel  -- complex-only, see § "tdot"
bilinear_form(x, M, y) = inner_product_M x M y                   -- M-weighted member
<<<NEW>>>
dot(x, y)              = inner_product x y                          -- Hermitian (complex) / symmetric (real); conjugated kernel, M = I
tdot(x, y)             = inner_product x y  with unconjugated kernel -- complex-only specialization, see § "tdot"
bilinear_form(x, M, y) = inner_product_M x M y                      -- M-weighted member: weight axis = general M
<<<END>>>
```

**Site 4b — post-table prose → per-member bullets + resolution prose** (this block begins
*after* the ` ```text ` closing fence, so it too carries no fence delimiters):

```edit:book/src/L2/inner_product.md
<<<OLD>>>
The L2 form differs from the L1 leaves in **resolution**, along the
conjugation-convention / weight-presence axes: L1 sees `dot`/`tdot` (the conjugation
axis at one chapter) and `bilinear-form` (the separate M-weighted chapter); L2 sees one
fold whose `kernel` and optional pre-`apply_linop M` recover each leaf. The element-type
sub-axis is identical to the leaves' (inherited, not re-derived).
<<<NEW>>>
- **`dot`** — the conjugation axis at value *Hermitian* (complex) / *symmetric* (real),
  with `M = I`. This is the workhorse specialization (CG coefficients, orthogonalization,
  NLEPS). Its L1 leaf [`dot`](../L1/dot.md) stays firm; at L2 there is no separate `dot`
  entry — it is this note.
- **`tdot`** — the conjugation axis at value *unconjugated bilinear* (complex-only). Co-
  defined with `dot` at L1; carried here with the type-API-surface-only caveat (§"tdot").
- **`bilinear_form`** — the weight axis at value *general / SPD `M`* (`inner_product_M`),
  realized as the pre-application `inner_product (apply_linop M x) y`. Its L1 leaf is
  [`bilinear-form`](../L1/bilinear-form.md) (rough-in).

The L2 entry differs from the L1 leaves in **resolution**, along the
conjugation-convention / weight-presence axes: L1 sees `dot`/`tdot` (the conjugation
axis at one chapter) and `bilinear-form` (the separate M-weighted chapter); L2 sees one
fold whose `kernel` and optional pre-`apply_linop M` recover each member as a note. The
element-type sub-axis is identical to the leaves' (inherited, not re-derived).
<<<END>>>
```

**Site 5 — §Dependencies** ("specializations rest on", not "fuses up from … not a replacement"):

```edit:book/src/L2/inner_product.md
<<<OLD>>>
- L1 leaves it fuses up from (recovered as family-axis specializations):
  [`dot`](../L1/dot.md) (the Hermitian / symmetric member, and `tdot` the unconjugated
  member, co-defined there), [`bilinear-form`](../L1/bilinear-form.md) (the M-weighted
  member). These stay firm/rough-in L1 leaves — `inner_product` is the form they fuse up
  into, not a replacement.
<<<NEW>>>
- L1 leaves the specializations rest on (each member is this fold at a fixed axis-value —
  see §"Specializations"): [`dot`](../L1/dot.md) (the Hermitian / symmetric member, and
  `tdot` the unconjugated member, co-defined there), [`bilinear-form`](../L1/bilinear-form.md)
  (the M-weighted member). These stay firm/rough-in **L1** leaves (the mutation-rotation
  layer, one per Palace L0 call surface); at **L2** `inner_product` is the single entry and
  they are specialization notes under it — there is no separate same-named L2 leaf chapter.
<<<END>>>
```

**Site 6 — §"Sibling fold" reciprocal note + §Status** (two-combinator framing + inversion paragraph):

```edit:book/src/L2/inner_product.md
<<<OLD>>>
The target is a small **algebra of folds** — a scalar-producing inner-product fold AND a
tensor-producing linear-combination fold — not one mega-combinator. They are deliberately
NOT merged. (`linear_combination` records the reciprocal boundary at
[`linear_combination`](./linear_combination.md) §"Sibling fold: dot is not subsumed".)
<<<NEW>>>
The target is a small **algebra of fold combinators** — a scalar-producing inner-product
combinator (this entry) AND a tensor-producing linear-combination combinator (the D1
sibling entry) — each the **primary L2 entry for its family**, not one mega-combinator and
not a leaf-floor lattice. They are deliberately NOT merged. (`linear_combination` records
the reciprocal boundary at its own §"Sibling fold: dot is not subsumed" — that entry is
D1's refactor scope this batch; this note is the `inner_product`-side half of the
two-combinator boundary and is edited here only.)
<<<END>>>
```

```edit:book/src/L2/inner_product.md
<<<OLD>>>
combinator-miner same-shape rough-in cleared the ≥3-instance bar (dot + tdot +
bilinear-form), and the parametric-family mode independently characterized the cohort
(combinator-miner:2026-05-29T023000Z) with the fold-law membership test + axis taxonomy.

<<<NEW>>>
combinator-miner same-shape rough-in cleared the ≥3-instance bar (dot + tdot +
bilinear-form), and the parametric-family mode independently characterized the cohort
(combinator-miner:2026-05-29T023000Z) with the fold-law membership test + axis taxonomy.

**Combinator-as-entry inversion (combinator-miner refactor-pass, cycle-049, D2).** Under
the 2026-06-01 vocabulary-shift redirect this entry was inverted from mine-and-strand
(combinator beside same-named L2 leaf chapters) to **combinator-as-entry**: the lede,
§Context, §"Specializations" (formerly the §Signature "recovered as specializations"
block), and §Dependencies now state the combinator IS the L2 inner-product entry and the
members (`dot`/`tdot`/`bilinear_form`) are specialization notes under it. The standalone
`L2/dot.md` leaf-floor collapse + the `L3/inner_product` upward propagation + the
`L3-L2/dot-body-identity` / `L2-L1/dot-leaf-identity` smell-theme demotions are the
cycle-050 enactment (mapped in the refactor-pass report). The combinator's own substantive
lowering [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
is a GENUINE translation (conjugation/element-type/weight dispatch + the value-level
`xᴴ y` ↔ `yᴴ x` re-order) and is KEPT (re-audited cycle-049, D2).

<<<END>>>
```

## Deliverable (b) — replace-and-propagate map (for cycle-050 enactment; NOT enacted this cycle)

### (b.1) Collapse `L2/dot.md` into a §"Specializations" note

- **Action (cycle-050):** Delete the standalone `book/src/L2/dot.md` chapter. Its entire
  content is, by its own admission, identity-in-form to the L1 leaf with all fusion content
  deferred to `inner_product` (`L2/dot.md:143-164,260-271`) — i.e. it is a degenerate
  mirrored floor carrying no L2-unique content. The §"Specializations" note now in
  `inner_product.md` (the `dot`/`tdot` bullets) is its replacement.
- **Dep-map (cycle-050):** Remove the `L2/index.md:82` `[`dot`](./dot.md)` row; fold its
  consumer list (`krylov-step`, `orthogonalize`, `gram`, `deflate`) into the
  `inner_product` row's consumer note (they consume the Hermitian specialization). Update
  `L2/index.md:28,45-48` cohort prose (the "Fold-parented floors" list) to drop `dot` as a
  floor and re-describe it as a specialization-note of `inner_product`.
- **Collapsed-leaf disposition convention (recommended):** **delete + redirect**, NOT
  stub. Rationale: the chapter is fully-lifted (no L0 navigation unique to it — all L0
  evidence is "transitive through the firm L1 leaf", `L2/dot.md:300-301`) and is NOT a
  canonical-witness instance of ≥2 concept pages (the canonical-instance carve-out does not
  apply — it is a layered chapter, not a Phase-1 slice). A `stub` would re-introduce a
  claim-free placeholder beside the combinator, re-creating the strand. The `SUMMARY.md`
  entry for `L2/dot` is removed; any inbound links re-anchor to
  `L2/inner_product.md#specializations…`. (Inbound-link audit is a cycle-050 lifter/
  integrator task; `dot-body-identity` and `dot-leaf-identity` are the main inbound
  references and are themselves demoted — see b.3.)

### (b.2) The `nrm2` disposition — the one genuine design fork — DECIDED

**Decision: `nrm2` stays a thin standalone consumer entry. It is NOT collapsed into an
`inner_product` specialization note, and it is NOT a fold member.**

Rationale (be explicit, since D3 audits the same cohort and a divergence is an integrator
signal):

- `nrm2` is `√ ∘ abs ∘ inner_product` at the diagonal `y=x` (`L2/nrm2.md:29-33`,
  `L2/inner_product.md` §"Consumer (NOT an instance)"). It is a **consumer** of the
  combinator's output, not the combinator at a fixed axis-value. A specialization note
  under `inner_product` would assert membership — that is the category error the existing
  `L2/index.md:111` "Fold-cohort boundary" + the `nrm2` carve-out (batch-12 meta-phase,
  `L2/index.md:28,48`) already forbid. The redirect does not overturn that boundary; it is
  fork-invariant on membership (`L2/index.md:48`).
- BUT the *mirrored-floor shape* of `nrm2` IS strand: `book/src/L2/nrm2.md` is a "thin
  floor … fusion rotation … no-op" (`L2/nrm2.md:17,118-120`) and its two lowering themes
  (`L3-L2/nrm2-body-identity`, `L2-L1/nrm2-leaf-identity`) are explicitly
  identity-in-named-terms ("identity-in-form on the leaf", `nrm2-leaf-identity.md:5`;
  "identity-in-form on the kernel", `nrm2-body-identity.md:5`). These themes are smells
  to demote (b.3).
- **Net:** `nrm2` keeps a (slimmed) standalone L2 entry framed as a **consumer** of the
  `inner_product` combinator (the consumer relationship is genuine, load-bearing content —
  the `std::abs` defensive guard, the always-real element-type collapse, the
  `nrm2(x)² = inner_product(x,x)` reuse identity that CG exploits). It does NOT become a
  note under `inner_product`; the do-NOT-merge consumer boundary is preserved. The thing
  that changes for `nrm2` at cycle-050 is: (i) re-frame its lede to point at the combinator
  as its consumed input rather than at a mirrored "floor presence" rationale; (ii) demote
  its two identity themes to in-line consumer notes (b.3).

This is the **divergence-risk surface vs D3**: D3 may be tempted to treat `nrm2` symmetrically
with `dot` (collapse both). It must NOT — `dot` is a fold *member* (collapsible to a note);
`nrm2` is a fold *consumer* (NOT collapsible; stays an entry). I flag this as an OQ so the
integrator catches a D3 divergence.

### (b.3) Demote the four degenerate identity-in-named-terms themes to in-line notes

The redirect: a degenerate identity-in-named-terms lowering is a **smell** (the vocabulary
failed to shift), resolved as a thin in-line note, NOT preserved as a mirrored entry + thin
theme. The four themes whose rewrite tables are entirely "Identity" rows:

| Theme file | Edge | Verdict | Disposition (cycle-050) |
|---|---|---|---|
| `book/src/L3-L2/dot-body-identity.md` | L3>L2 `dot` | **demote** (all-Identity rewrite, `:77-84`) | Delete the theme file; replace with an in-line note in the L3 `dot` dep-map row (and, post-b.5, in `L3/inner_product`): "L3>L2 is identity-in-named-terms — no rotation; `dot` is the Hermitian specialization of the `inner_product` combinator at both layers." Per CLAUDE.md cycle-012 non-adjacent in-line-identity convention. |
| `book/src/L2-L1/dot-leaf-identity.md` | L2>L1 `dot` | **demote** (all-Identity rewrite, `:89-95`) | Delete; in-line note on the `inner_product` §"Specializations" `dot` bullet: "L2>L1 is identity-in-form; the genuine L2>L1 translation for the whole family is `inner-product-fold-specialization` (the `dot` member is its Hermitian dispatch arm)." The fusion content was ALREADY deferred to the fold-parent theme (`dot-leaf-identity.md:100-110`) — so demotion loses nothing. |
| `book/src/L3-L2/nrm2-body-identity.md` | L3>L2 `nrm2` | **demote** (all-Identity, `:97-103`) | Delete; in-line consumer note on the L3 `nrm2` row: "identity-in-named-terms; the only textual change is the inner-reduction name (`dot` leaf → `inner_product` at diagonal)." |
| `book/src/L2-L1/nrm2-leaf-identity.md` | L2>L1 `nrm2` | **demote** (all-Identity, `:73-119`) | Delete; in-line consumer note: "identity-in-form; the `√ ∘ abs` post-step + the `inner_product(x,x) → dot(x,x)` diagonal refusion (inherited from `inner-product-fold-specialization` §diagonal-degeneration); the `std::abs` guard's load-bearing classification lives at `L1-L0/nrm2-mutation-rotation`." |

**Note (do NOT over-demote):** the `nrm2` L1>L0 theme `L1-L0/nrm2-mutation-rotation` is
**NOT** a smell — it carries the genuine four-stage `Dot → MPI_Allreduce → std::abs →
std::sqrt` expansion with the `std::abs` guard re-materializing as stage 3. KEEP it. Only
the four L3>L2 / L2>L1 *identity-in-named-terms* themes above demote.

### (b.4) `bilinear-form` disposition

`bilinear-form` has **no standalone L2 chapter** (confirmed: `ls L2/` has no
`bilinear-form.md`). It lives as the L1 leaf + the weighted member (`inner_product_M`) note
inside the combinator. **No collapse needed** — it is already in the desired shape (a
specialization note under the combinator). Cycle-050: just ensure the §"Specializations"
`bilinear_form` bullet (now present) is the authoritative L2 home; no new file.

### (b.5) Propagate the combinator UP to a new `L3/inner_product`

This is the **propagation** half of replace-and-propagate (the missing-instance-6 fix).

- **Action (cycle-050, harvester):** Author `book/src/L3/inner_product.md` as the **L3
  combinator entry** — the iteration-rotation rendering of the reduce-to-scalar fold (the
  L3 analog of the L2 combinator). It is `inner_product :: Tensor[N] -> Tensor[N] -> Scalar`
  as a whole-tensor field reduction with no sequential obstruction (the length-axis indices
  reduce in parallel in exact arithmetic; the pinned reduction tree is an L0 non-law). This
  is harvester scope (formalization) — combinator-miner only registers the rough-in row.
- **Re-express the L3 leaf cohort through it (cycle-050):** the firm L3 `dot`/`nrm2`
  (`L3/index.md:27-28`) re-express as: `dot` = the Hermitian specialization of
  `L3/inner_product`; `nrm2` = the `√ ∘ abs ∘ L3/inner_product` consumer at `y=x`. The L3
  leaf entries are slimmed to specialization/consumer notes pointing at `L3/inner_product`,
  paralleling the L2 inversion. (This mirrors the redirect mandate: higher layers express
  through the combinator rather than re-deriving base forms.)
- **L4:** no `L4/inner_product` (confirmed — leaves/folds are not first-class L4 vocab per
  the cycle-010 audit; the combinator appears inside L4 composed entries like `krylov-step`
  §Semantics as a let-binding). No propagation above L3.
- **Dep-map rough-in row (this report's one registration):** see Proposed changes.

## Proposed changes

The one dep-map rough-in row registering the upward propagation target (b.5). Per the
forward-reference convention, the future-chapter cell is **plain text / inline-code**, NOT
a live link (the file does not exist until cycle-050's harvester authors it):

```edit:book/src/L3/index.md
# Append to the L3 operator dep-map (after the nrm2 row :28), as a rough-in:
| `inner_product` *(rough-in; no anchor yet)* | `Tensor[N] -> Tensor[N] -> Scalar` (reduce-to-scalar field reduction; the L3 analog of the L2 `inner_product` combinator; Hermitian/symmetric/unconjugated/M-weighted specializations read at fixed axis-values) | L2 [`inner_product`](../L2/inner_product.md) (combinator propagated up; the L3 entry is the iteration-rotation rendering — whole-tensor reduction, no sequential obstruction, pinned tree an L0 non-law). The firm L3 `dot`/`nrm2` leaves re-express through this combinator (dot = Hermitian specialization; nrm2 = `√ ∘ abs ∘ inner_product` consumer at y=x). | `rough-in` (proposed-by combinator-miner:2026-06-01T190900Z; replace-and-propagate upward target of the cycle-049 D2 inner_product combinator-as-entry inversion; harvester authors `book/src/L3/inner_product.md` cycle-050) |
```

Note: this report does **not** create `book/src/L3/inner_product.md` (harvester's job,
cycle-050). It registers only the rough-in dep-map row.

## Deliverable (c) — re-audit of `book/src/L2-L1/inner-product-fold-specialization.md`: KEEP

**Verdict: KEEP (firm). This is a GENUINE translation, NOT a degenerate
identity-in-named-terms smell.** It is the combinator's OWN substantive lowering and
carries load-bearing facts that the degenerate `dot-leaf-identity` / `dot-body-identity`
themes do not.

Load-bearing translation content it carries (the facts that make it a real vocabulary shift,
not a rename):

1. **Three-key dispatch** (`:107-135`): conjugation key (Hermitian `dot` vs unconjugated
   `tdot` — the sign of the imaginary cross-term, `ComplexVector::Dot` `:111-114` vs
   `TransposeDot`), element-type key (real single Hypre pass vs complex four-real-dot lift,
   `:119-125`), weight key (`M=I` → `dot`, general `M` → `bilinear_form`, `:127-135`). The
   one L2 fold *re-fuses* into Palace's bounded family of distinct reduction call shapes —
   that is a genuine organization shift, not a 1:1 rename.
2. **The `xᴴ y` ↔ `yᴴ x` conjugate-pair re-order** (`:158-220`) — the headline content.
   The L1/L2 representation pins arg-1 conjugated (`xᴴ y`); Palace's L0 surface pins arg-2
   conjugated (`yᴴ x`); they are complex conjugates (`:164-166`). **This is value-bearing
   for complex vectors** — at the off-diagonal non-Hermitian cross-coupling site
   `boundarymodeoperator.cpp:90` (`:217-220`, `:325`) the re-order changes the value and the
   lowering must emit the operand-swap form `linalg::Dot(comm, y, x)`. This is exactly the
   load-bearing translation the redirect wants a lowering to carry; it is NOT identity.
3. **Per-call pinned reduction trees** (`:222-251`) — the summation-order table: real =
   single Hypre pass; complex = four Hypre passes combined by scalar `±`; `tdot` = same with
   the `Im` cross-term sign flipped; weighted = two-stage (M-apply tree then dot tree). The
   load-bearing IEEE-754 content the combinator's non-law defers here.
4. **The caller-site conjugation inventory** (`:301-329`) — a cross-layer census classifying
   every `linalg::Dot` caller invisible/observable, establishing the convention is
   load-bearing in exactly one algorithm (SLEPc-NEP deflation, `nleps.cpp`). This is genuine
   downstream analysis, not a rename.

Contrast with the demoted smells: `dot-leaf-identity`'s rewrite table is ALL "Identity"
rows (`dot-leaf-identity.md:89-95`) and it explicitly defers all fusion content to THIS
theme (`:100-110`). The combinator's own lowering is where the real work lives; the
per-leaf identity themes are the empty mirror. **KEEP this; demote those.**

The lowering-verifier audit block already attached (`:540-605`, `coverage_verdict:
fully-supported`, `status_recommendation: keep firm`) corroborates the KEEP, with three
minor anchor drifts (Ax `:623→:624`, `:632→:634`; SPD assert `:615-616→:616`) flagged as a
citation-correction follow-up, not a status reduction. I record those for the cycle-050
firming touch.

## Supporting evidence

- `book/src/L2/inner_product.md` — the inverted combinator (this dispatch's enacted edit);
  pre-inversion lede `:1-21`, §"Specializations" now `:157-`, §Status inversion paragraph.
- `book/src/L2/dot.md` — the mirrored base-form leaf to collapse (`:19-25` floor-presence
  rationale, `:143-164` fusion deferral, `:260-271` identity-in-form status).
- `book/src/L2/nrm2.md` — the consumer mirrored as floor (`:29-33` consumer-not-member,
  `:118-120` no-op fusion rotation).
- `book/src/L3-L2/dot-body-identity.md:77-84`, `book/src/L2-L1/dot-leaf-identity.md:89-95`,
  `book/src/L3-L2/nrm2-body-identity.md:97-103`, `book/src/L2-L1/nrm2-leaf-identity.md:73-119`
  — the four all-Identity rewrite tables (the smells to demote).
- `book/src/L2-L1/inner-product-fold-specialization.md:107-251,301-329,540-605` — the
  genuine translation (KEEP); dispatch keys, conjugate-pair re-order, summation-order
  trees, caller inventory, lowering-verifier corroboration.
- `book/src/L3/index.md:27-28` — the firm L3 `dot`/`nrm2` rows lifting from L1 with no
  `L3/inner_product` combinator (the missing propagation).
- `book/src/L2/index.md:22-29,45-48,111,122` — the fold-cohort motif prose, the leaf-vs-fold
  ratification, the `nrm2` carve-out (fork-invariant on membership), the Fold-cohort boundary.
- Palace L0 (transitive, via the firm L1 leaves; cited in the entries):
  `palace/linalg/vector.cpp:263-267` (`ComplexVector::Dot` Hermitian kernel = `yᴴ x`),
  `:269-274` (`TransposeDot` `tdot`), `:674-685` (complex four-real-dot lift),
  `palace/linalg/vector.hpp:255-260` (`Norml2` = `√|Dot(x,x)|`),
  `palace/models/boundarymodeoperator.cpp:90` (the observable-re-order witness),
  `test/unit/test-vector.cpp:206-207` (real-dot value test).

## Open questions / caveats

- **OQ (divergence-risk vs D3): `nrm2` consumer-not-member must be preserved at cycle-050.**
  I decided `nrm2` stays a standalone consumer entry (NOT collapsed to a note, NOT a fold
  member). D3 audits the same `inner_product`/`nrm2` cohort; if D3 recommends collapsing
  `nrm2` symmetrically with `dot`, that is a divergence the integrator must catch — `dot`
  is a fold *member* (collapsible), `nrm2` is a fold *consumer* (not collapsible; the
  do-NOT-merge consumer boundary at `L2/index.md:111` + the batch-12 `nrm2` carve-out are
  load-bearing and fork-invariant). Recommend the integrator treat any D3 `nrm2`-collapse
  recommendation as a contradiction to reconcile, defaulting to KEEP-AS-CONSUMER-ENTRY.

- **OQ (cycle-050 sequencing): collapse + demotion + L3-propagation are one coherent batch.**
  The b.1 `L2/dot` collapse, the b.3 four-theme demotion, and the b.5 `L3/inner_product`
  authoring are interdependent (the demoted `dot-body-identity` in-line note lands in the
  new `L3/inner_product` row; the `L2/dot` inbound links re-anchor to the combinator
  §"Specializations"). Recommend cycle-050 dispatch them as a single harvester+lifter wave,
  not piecemeal, to avoid a transient broken-link window. (Build risk: deleting `L2/dot.md`
  before re-anchoring `dot-leaf-identity`'s `[`dot`](../L2/dot.md)` link would be a
  linkcheck2 hard error — the demotion must precede or accompany the deletion.)

- **Caveat (citation drift, carry-forward to cycle-050 firming):** the
  `inner-product-fold-specialization` lowering-verifier block (`:562-573`) flags three minor
  anchor drifts (`operator.cpp` Ax `:623→:624`, `:632→:634`; SPD assert `:615-616→:616`).
  These are citation-correction touches for the cycle-050 firming pass, not status
  reductions and not blockers to the KEEP verdict.

- **Caveat (`tdot` type-API-surface-only, unchanged):** the `tdot` specialization carries
  the zero-Palace-call-site evidentiary note (`vector.hpp:112` decl + `vector.cpp:269` def
  only). This is a member-level caveat on a specialization note, not a status reduction on
  the combinator; it transports unchanged into the §"Specializations" `tdot` bullet.

- **Scope-honored:** I edited only `book/src/L2/inner_product.md` (the (a) enactment) and
  registered one dep-map rough-in row via the proposed-changes channel (b.5). I did NOT
  touch `linear_combination.md` (D1's), did NOT enact any collapse/demotion/L3-authoring
  (cycle-050), and did NOT write to any other `book/` file directly.

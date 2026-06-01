---
agent: combinator-miner
invoked_at: 2026-06-01T19:09:00Z
scope: Refactor pass (cycle-049 D1) — linear_combination family combinator-as-entry inversion + replace-and-propagate map + L2-L1 lowering re-audit
status: integrated
integrated_at: 2026-06-01T210000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: APPLIED clean (cycle-049 D1). The 4-edit combinator-as-entry inversion of book/src/L2/linear_combination.md landed exactly as scoped; the (b) replace-and-propagate MAP (leaf-collapse, thin-theme demotion, L3/linear_combination authoring, L4-propagation) is a cycle-050 forward plan NOT enacted; the (c) KEEP verdict on L2-L1/linear-combination-fold-specialization.md is a no-mutation verdict. 3 OQs promoted. Build-relevant yes (cargo make book exit 0, linkcheck2 green, zero build-repairs). No wave conflict (disjoint file from D2). FIRST refactor-pass cycle under the 2026-06-01 VOCABULARY-SHIFT REDIRECT.
---

# CYCLE: Combinator refactor — `linear_combination` family (replace-and-propagate)

## Summary

The `linear_combination` fold combinator already exists firm at L2
(`book/src/L2/linear_combination.md`, harvested cycle-018) but was authored under the
retired mine-and-strand regime: it explicitly disclaims replacement ("`linear_combination`
is the form the four leaves fuse *up* into at L2; **it does not replace them**",
`L2/linear_combination.md:19-20`, repeated `:196-197`), and the four arity leaves
(`scal`/`axpy`/`axpby`/`axpbypcz`) stand as separate mirrored L2 chapters under it. The
combinator was **never propagated to L3** — `book/src/L3/linear_combination.md` does not
exist and the L3 leaf cohort references `linear_combination` **zero times** (verified:
`grep -rl linear_combination book/src/L3/` → no hits). The L3 leaves instead each re-derive
the base form as "value-thread-isomorphic to L1" (e.g. `L3/axpy.md:16,22,68`), the canonical
mine-and-strand drift the 2026-06-01 redirect §5 names. The `keep leaf-floor (b)` design
ratified batch-12 (`L2/index.md:28,112`) is precisely the rectangular-floor machinery the
redirect supersedes.

This report delivers the three cycle-049 D1 items: **(a)** ENACTS the L2-entry inversion
(combinator-as-entry; the four leaves become specialization notes under it) as a
proposed-changes block; **(b)** AUTHORS the replace-and-propagate map for cycle-050
enactment (leaf-chapter disposition + thin-theme demotion list + L3-combinator authoring
plan + L4-propagation note); **(c)** RE-AUDITS `L2-L1/linear-combination-fold-specialization.md`
under the translation/smell test and records the **KEEP** verdict — it is the combinator's
own substantive translation (arity-dispatch + the load-bearing pinned summation order), NOT
a degenerate identity-in-named-terms smell.

## Pattern instances

This is a refactor pass on an *already-identified* combinator (the cycle-018 fold), so the
instance evidence is the mine-and-strand stranding, not a fresh family discovery:

- **The combinator exists but disclaims replacement**: `book/src/L2/linear_combination.md:19-20`
  ("it does not replace them") and `:193-197` (Dependencies: "These stay firm L1 leaves —
  `linear_combination` is the form they fuse up into, not a replacement").
- **Four mirrored leaf chapters sit beside it (not under it)**: `book/src/L2/scal.md`,
  `book/src/L2/axpy.md`, `book/src/L2/axpby.md`, `book/src/L2/axpbypcz.md` — each a standalone
  chapter framed as a "base … leaf; arity-N member of `linear_combination` (cited, NOT
  merged)" (`L2/index.md:77-80`).
- **Combinator never propagated to L3**: `book/src/L3/linear_combination.md` absent; the four
  L3 leaf chapters (`L3/{scal,axpy,axpby,axpbypcz}.md`) re-derive the base form as
  "value-thread-isomorphic to the L1 form" with **zero** references to the combinator
  (`L3/axpy.md:16,22,52,68`, mirrored in the three siblings).
- **Eight thin mirrored lowering themes** encode the rectangular floor as named-term renames:
  4× `L3-L2/{scal,axpy,axpby,axpbypcz}-body-identity.md` (each self-describes "The body IS
  the identity", `L3-L2/axpy-body-identity.md:14`) + 4× `L2-L1/{scal,axpy,axpby,axpbypcz}-leaf-identity.md`
  (each "the thinnest member of the L2>L1 lowering family", `L2-L1/scal-leaf-identity.md:16`).
- **The ratified rectangular machinery is explicit**: `L2/index.md:28` ("leaf-vs-fold
  realization RATIFIED (keep leaf-floor (b)), batch-12 meta-phase"), `:112` ("Each firm L3
  leaf gets a same-named L2 floor"). This is the retired pattern.

## Proposed combinator

- **Slug**: `linear_combination` (already firm at L2; this pass re-roles it as the family entry)
- **Layer**: L2 (entry already lands here; this pass ALSO propagates an L3 analog — see map (b))
- **Signature** (unchanged, `L2/linear_combination.md:46-49`):
  `linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]`, `foldl (\acc (a,t) -> acc + scal a t) (zeros N) pairs`.
- **Algebraic intuition** (unchanged): monoid homomorphism `([(Scalar,Tensor[N])], ++, [])
  → (Tensor[N], +, zeros)` (concatenation-homomorphism, law 2); multilinearity in the scalar
  list; empty-list = `zeros[N]` identity; permutation-invariant in exact arithmetic, NOT
  bit-for-bit under IEEE-754 (the load-bearing summation-order non-law).
- **Variant axes** (unchanged): arity (the unification axis), output-aliasing (the FOLD's
  axis), element-type / scalar-promotion.
- **Parameter axis** (parametric family): arity ∈ {1,2,2,3}, recovered as list-length;
  siblings `scal` (arity-1), `axpy` (arity-2, unit 2nd coeff), `axpby` (arity-2 general),
  `axpbypcz` (arity-3).
- **Over-unification guard** (unchanged, do NOT collapse): the sibling fold `inner_product`
  (reduce-to-`Scalar`, conjugation axis) is a DIFFERENT fold — different codomain, different
  combining step. This pass does NOT touch `inner_product.md` (D2's, wave-1 sibling); it edits
  ONLY the reciprocal §"Sibling fold" cross-reference inside `linear_combination.md`.

### What changes vs. cycle-018

Cycle-018 mined the fold and *stranded* it (entry-beside-leaves). This pass enacts
**replace** (the combinator is the entry; leaves are specialization notes under it) at L2 and
spells out **propagate** (author the L3 analog; re-express the L3 cohort through it) for
cycle-050. The signature/laws/evidence are unchanged — only the *role* and *disposition*
change.

## (a) ENACTED THIS CYCLE — L2-entry inversion (proposed-changes)

The edits invert the four "does not replace" framings to "combinator-as-entry; leaves are
specialization notes", and edit the reciprocal sibling-fold note in THIS entry only. Surgical
string replacements (the rest of the firm body — signature, all 7 laws, evidence — is
unchanged).

```edit:book/src/L2/linear_combination.md
<<<OLD>>>
The `axpby-as-primitive` decision
([`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md))
correctly keeps each as a leaf (fuse, don't decompose). `linear_combination` is the
form the four leaves fuse *up* into at L2; it does not replace them.
<<<NEW>>>
The `axpby-as-primitive` decision
([`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md))
keeps the fused scalar-vector update whole at L1 (fuse, don't decompose) — that decision
governs the L1>L0 mutation rotation, where each fixed-arity symbol mirrors one L0 C++ call
one-to-one. **At L2, `linear_combination` is the entry for this family** (vocabulary-shift
redirect 2026-06-01, `CLAUDE.md` §Methodology invariants): the four arity forms `scal` /
`axpy` / `axpby` / `axpbypcz` are **specialization notes under the combinator** (§"Arity
specializations"), not standalone mirrored L2 chapters. This supersedes the cycle-018
"the fold does not replace the leaves" framing and the batch-12 "keep leaf-floor (b)"
ratification (`book/src/L2/index.md`): under the redirect, a same-named base-form floor
mirrored beside the combinator is the retired rectangular pattern. The L1 leaves remain
firm (the L1>L0 one-to-one shape is load-bearing there); what changes is L2's *entry* — the
family speaks through the combinator at L2 and above.
<<<END>>>
```

```edit:book/src/L2/linear_combination.md
<<<OLD>>>
The four fixed-arity specializations (the L1 leaves as derived identities):

```text
scal(α, x)                 = linear_combination [(α, x)]
axpy(α, x, y)              = linear_combination [(α, x), (1, y)]      -- second coeff fixed to 1
axpby(α, x, β, y)          = linear_combination [(α, x), (β, y)]
axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]
```
<<<NEW>>>
### Arity specializations (the family members, as notes under the combinator)

The four arity forms are list-length specializations of the combinator — **specialization
notes, not standalone L2 chapters** (vocabulary-shift redirect). Each is the combinator at a
fixed term-list length:

```text
scal(α, x)                 = linear_combination [(α, x)]              -- arity 1
axpy(α, x, y)              = linear_combination [(α, x), (1, y)]      -- arity 2, second coeff fixed to 1
axpby(α, x, β, y)          = linear_combination [(α, x), (β, y)]      -- arity 2, general
axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)] -- arity 3
```

These names remain useful as *readout labels* for the bounded-arity L0 call shapes (the
L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md)
fusion-selection theme picks the maximal fused L0 leaf per list-length). They are NOT
separate L2 operators with their own algebra — every law below is the combinator's; the
per-arity facts (`axpby` bilinearity, `axpbypcz` trilinearity, etc.) are the multilinearity
law (law 3) read at a fixed list length. The L1 leaf chapters (`book/src/L1/{scal,axpy,axpby,axpbypcz}.md`)
stay firm — they carry the L1>L0 one-to-one symbol shape; the *L2* family entry is this
combinator.
<<<END>>>
```

```edit:book/src/L2/linear_combination.md
<<<OLD>>>
- L1 fixed-arity specializations (the fold's leaves, recovered at each list length):
  [`scal`](../L1/scal.md) (arity 1), [`axpy`](../L1/axpy.md) (arity 2, second coeff 1),
  [`axpby`](../L1/axpby.md) (arity 2), [`axpbypcz`](../L1/axpbypcz.md) (arity 3). These
  stay firm L1 leaves — `linear_combination` is the form they fuse up into, not a
  replacement; the `axpby-as-primitive` decision keeps them as leaves.
<<<NEW>>>
- L1 fixed-arity specializations (the family members, recovered at each list length):
  [`scal`](../L1/scal.md) (arity 1), [`axpy`](../L1/axpy.md) (arity 2, second coeff 1),
  [`axpby`](../L1/axpby.md) (arity 2), [`axpbypcz`](../L1/axpbypcz.md) (arity 3). These
  stay firm **L1** leaves (the L1>L0 one-to-one symbol shape is load-bearing for the
  mutation rotation; `axpby-as-primitive` keeps them fused there). **At L2 and above the
  family speaks through this combinator** — the separate L2 `scal`/`axpy`/`axpby`/`axpbypcz`
  chapters are scheduled to collapse into the §"Arity specializations" notes above
  (cycle-050 refactor; see the replace-and-propagate map in
  `reports/2026-06-01T190900Z-combinator-miner-refactor-pass-linear-combination-family/CYCLE.md`).
<<<END>>>
```

```edit:book/src/L2/linear_combination.md
<<<OLD>>>
A sibling `inner_product` L2 fold capturing `dot` / `tdot` as
conjugation-convention variants is a separate candidate, tracked under OQ
`inner-product-fold-sibling-candidate` (the axis there is conjugation-convention, not
arity). It is deliberately NOT merged into `linear_combination`.
<<<NEW>>>
The sibling [`inner_product`](./inner_product.md) L2 fold (firm cycle-019) captures `dot` /
`tdot` as conjugation-convention variants (the axis there is conjugation-convention, not
arity). It is deliberately **NOT merged** into `linear_combination`: same operand shape
`(Tensor[N], Tensor[N])`-ish, but a different codomain (`Scalar` vs `Tensor[N]`) and a
different combining step (zip-and-reduce-over-`N` vs scale-and-accumulate-over-the-term-list).
The do-NOT-merge boundary is load-bearing and symmetric — recorded here and in
[`inner_product`](./inner_product.md) §"Sibling fold". The two are the small algebra of
folds (one tensor-producing, one scalar-producing), not one mega-combinator.
<<<END>>>
```

Note: this report does **not** create `book/src/L3/linear_combination.md` (that is the
cycle-050 harvester/abstractor propagation work, mapped in (b)) and does **not** delete or
stub the L2 leaf chapters this cycle (the disposition decision is cohort-wide and depends on
the D3 audit — see (b)).

## (b) Replace-and-propagate map (FOR CYCLE-050 ENACTMENT — not enacted this cycle)

The enactment of everything in this section is gated on this map + the D3 cohort-wide audit;
the leaf-collapse / L3-combinator authoring / theme-demotion are explicitly cycle-050.

### (b.1) L2 leaf-chapter disposition

The four chapters `book/src/L2/{scal,axpy,axpby,axpbypcz}.md` collapse into the
§"Arity specializations" notes inside `linear_combination.md` (enacted-skeleton landed in
(a)). **Recommendation: delete-with-SUMMARY-removal, with one redirect-stub exception.**

- **`L2/axpy.md`, `L2/axpby.md`, `L2/axpbypcz.md` → DELETE + remove from `SUMMARY.md`.**
  Their entire substantive content is already the combinator at a fixed arity (the index rows
  `L2/index.md:77,79,80` themselves say "arity-N member of `linear_combination` … cited, NOT
  merged … output-aliasing is the FOLD's axis … all fusion deferred to the fold-parent"). They
  carry **no L2-unique algebra** — every law is the combinator's multilinearity law at a fixed
  length. Keeping them as chapters is the retired rectangular mirror. Their L0 evidence is
  already cited in `linear_combination.md` §Evidence (`:316-345`) and in the L2>L1 theme.
- **`L2/scal.md` → REDUCE-TO-REDIRECT-STUB (do not hard-delete this one yet).** `scal` is
  referenced as a *consumed constituent* by `L2/normalize.md` (`normalize(x) = (nrm2(x),
  scal(1/nrm2(x), x))`, `L2/index.md:56,84`) and as the arity-1 readout by
  `elementwise_product` (`scal(α,x) = elementwise_product(broadcast(α,N), x)`, `L2/index.md:86`).
  Until those consumers are re-pointed at `linear_combination` (the §"Arity specializations"
  `scal` note) or at the elementwise leaf, `scal` needs a resolvable link target. Recommend a
  `status: stub` redirect chapter ("`scal` is the arity-1 specialization of
  [`linear_combination`](./linear_combination.md) — see §Arity specializations") rather than a
  deletion that would dangle the `normalize`/`elementwise_product` links.

**Rationale for delete-over-inline-note**: the §"Arity specializations" notes (landed in (a))
already ARE the inline notes; a separate chapter would duplicate them. The convention is
unsettled cohort-wide, so this is a **recommendation for the meta-phase to ratify** alongside
the parallel `inner_product` / `dot` / `nrm2` decision (D2's cohort) — the two folds should
get the same disposition rule. **Open question for the OQ ledger** (below):
delete-vs-redirect-stub cohort-wide.

### (b.2) Degenerate-smell themes to demote-to-in-line

These eight themes are degenerate identity-in-named-terms lowerings — the redirect's
smell signature (each self-describes "The body IS the identity" / "the thinnest member" /
"all four collapse to nothing"). They are **NOT translations** (no vocabulary shift, no
load-bearing content) and demote to in-line notes:

| theme file | self-description (smell evidence) | disposition |
|---|---|---|
| `L3-L2/scal-body-identity.md` | arity-1 leaf, "the body IS the identity", no wrapper | demote → in-line note in `L3/linear_combination` §"Down to L2" |
| `L3-L2/axpy-body-identity.md` | `:14` "The body IS the identity"; no `IterState`, no outer loop | demote → in-line note |
| `L3-L2/axpby-body-identity.md` | arity-2 sibling, identity-in-form | demote → in-line note |
| `L3-L2/axpbypcz-body-identity.md` | arity-3 sibling, identity-in-form | demote → in-line note |
| `L2-L1/scal-leaf-identity.md` | `:80-87` "all four collapse to nothing … value-exact AND bit-exact" | demote → fold into `linear-combination-fold-specialization` arity-1 row (already there) |
| `L2-L1/axpy-leaf-identity.md` | "arity-2 shadow … all fusion deferred to the fold-parent" | demote → already the fold-spec arity-2 row |
| `L2-L1/axpby-leaf-identity.md` | arity-2 general shadow | demote → already the fold-spec arity-2 row |
| `L2-L1/axpbypcz-leaf-identity.md` | arity-3 shadow | demote → already the fold-spec arity-3 row |

The four `L2-L1/*-leaf-identity.md` themes are **wholly subsumed** by
`L2-L1/linear-combination-fold-specialization.md` (each is "the same arity-N row … viewed
here as the standalone leaf's own edge", `L2-L1/scal-leaf-identity.md:65-71`). Once the L2
leaf chapters collapse (b.1), these themes have no standalone LHS to lower and should be
**deleted with SUMMARY removal**, their content already present as the fold-spec's rows. The
four `L3-L2/*-body-identity.md` themes become in-line notes in the new `L3/linear_combination`
entry (b.3). **Smell, not preserve** — do NOT keep them as mirrored thin themes.

### (b.3) L3-propagation plan (author `L3/linear_combination`)

The combinator was never propagated to L3 (verified absent). Cycle-050 authors
`book/src/L3/linear_combination.md` as the **L3 family entry** (the iteration-rotation-layer
analog of the L2 combinator): a whole-tensor variadic fold over a `[(Scalar, Tensor[N])]`
term list, with the same concatenation-homomorphism / multilinearity laws, **no sequential
obstruction** (the fold is over the term list, element-local in `N` — `L3/axpy.md:58`
already establishes the cohort carries no obstruction). The four L3 leaf chapters
(`L3/{scal,axpy,axpby,axpbypcz}.md`) are then **re-expressed through it** — collapsed into
§"Arity specializations" notes inside `L3/linear_combination.md`, exactly mirroring the L2
disposition (b.1). The L3>L2 edge becomes one theme — the combinator's own identity-or-thin
rotation (the L3 fold = the L2 fold, value-thread-isomorphic) — replacing the four mirrored
`*-body-identity` themes (demoted per b.2). The L3 entry expresses its forms *through* the
combinator rather than re-deriving "value-thread-isomorphic to L1" four times.

This is the **propagate** half of replace-and-propagate: higher layers express the family
through the combinator (or its layer-N analog), not via re-derived base forms. Disposition of
the L3 leaf chapters mirrors (b.1) (delete `axpy`/`axpby`/`axpbypcz`; redirect-stub `scal`
pending consumer re-pointing — note `L3/normalize.md`, `L3/krylov-step.md` consume them).

### (b.4) L4-propagation note

L4 already references base forms by name rather than through the combinator:

- `L4/krylov-step.md:67` — "update primitives are L1 calls — axpy, axpby, axpbypcz, dot,
  nrm2, scal"; `:104` — "`axpy(α, ·, w)` reads it".
- `L4/chebyshev.md:203` — "in-place `axpy`/`scal` on aliased storage".
- `L4-L3/krylov-step-typed-wrapper-dissolution.md` — renders the L3 body let-chain with
  `axpy` by name (`:68`).

Cycle-050 (or later) updates these to express the iterate-stratum / update-primitive group
**through `linear_combination`** (the L4/L3 analog): the krylov-step update is a
`linear_combination` over the basis-correction terms (the GMRES correction sum is exactly a
scalar-weighted term-list, per `L3/axpy.md:75` law 6 "underwrites … unfolding of GMRES
basis-correction sums into axpy chains" — that unfolding IS a `linear_combination`). The
in-place `axpy`/`scal` in `L4/chebyshev.md` are the aliased-output specialization of the
combinator. This is a **lower-priority propagation** (L4 is opaque-wrapper-heavy; the change
is replacing enumerated base-form names with "the combinator at arity-N" where it reads
cleanly) — flag, don't force. NOTE: do NOT rewrite the `dot` / `nrm2` references through
`linear_combination` (those are the sibling `inner_product` fold + its consumer — D2's
cohort).

## (c) RE-AUDIT — `L2-L1/linear-combination-fold-specialization.md`: KEEP (genuine translation)

**Verdict: KEEP, firm, unchanged.** This is the combinator's OWN substantive lowering and is
a genuine translation across vocabularies, NOT a degenerate identity-in-named-terms smell. It
must NOT be demoted with the eight thin themes in (b.2).

Load-bearing facts it carries that no in-line note could absorb:

1. **Arity-dispatch fusion-selection rule** (`:61-101`): reads the fold's term-list *length*
   and selects the **maximal fused L0 leaf** (length 1→`scal`, 2→`axpy`/`axpby`, 3→`axpbypcz`,
   ≥4→iterated `axpbypcz`-into-output chain). This is real translation work — the variadic L2
   fold has no fixed arity; the L1/L0 surface has a bounded fused-kernel family (ceiling
   `axpbypcz`, `vector.hpp:305-316`). The rotation maps unbounded→bounded with a de-fusion at
   the arity-4 boundary. Not a rename.
2. **Two-sub-selection within arity 2** (`:103-115`): `axpy` vs `axpby` disambiguated by the
   literal-`1` second coefficient (drop the `1·y` multiply). A genuine fusion-of-a-multiply
   refinement.
3. **Arity-3 → arity-2 fall-through on the in-source `γ==0` branch** (`:117-137`): read
   directly off `vector.cpp:745-758` (`if (gamma == 0.0) { add(...); }`). Source-grounded
   selection edge, not imposed.
4. **The pinned summation-order table** (`:139-167`) — **THE load-bearing-numerical content**.
   Per `CLAUDE.md` §"Optimization tricks vs. base algebra" / "load-bearing numerical tricks …
   non-associative reduction orderings … preserve as explicit algebraic claims": the L2 fold
   is order-agnostic for value but bit-identical reproduction of any L0 call requires matching
   that call's pinned order. The table records, per lowered call, the exact pinned order
   (`axpby` single fused aligned pass `vector.cpp:726-730`; the `γ≠0` two-pass split
   `:753-756` whose `β·y` is added in a *separate later pass* — a distinct rounding schedule).
   The two arity-3 branches do NOT agree bit-for-bit. **This is the load-bearing residue the
   L2 entry's IEEE-754 permutation non-law explicitly deferred here** (`L2/linear_combination.md:176-178`).
   An in-line note cannot carry this — it is the substantive translation content.

Justification kind is `algebraic` (the selection rule IS the combinator's laws 6+2+5 read as a
lowering) with the summation-order residue as the load-bearing numerical overlay — exactly the
"genuine translation" profile the redirect wants combinators' own lowerings to have. Contrast
the eight thin `*-body-identity` / `*-leaf-identity` themes (b.2), which carry NO arity
dispatch and NO summation-order table (the arity-1 `scal-leaf-identity.md:80-87` itself says
"all four collapse to nothing … there is no sum") — those are the degenerate smell; THIS theme
is their non-degenerate parent.

One forward-consistency note for cycle-050: this theme's §Verified-against (`:271-276`) and
its narration reference the L2 leaf chapters and the four `*-leaf-identity` themes as the
"standalone leaf edges". When those collapse (b.1/b.2), this theme's cross-references should be
re-pointed at the §"Arity specializations" notes (a light touch, not a rewrite — the
substantive selection-rule + summation-order body is unaffected). Recorded as an OQ.

## Proposed changes

The only artifact mutation enacted this cycle is the (a) L2-entry inversion (four surgical
edits to `book/src/L2/linear_combination.md`, in the four ```edit:``` blocks under (a)
above). No dep-map rough-in row is added this cycle: the L2 `linear_combination` entry and
the L2>L1 fold-spec theme already exist firm; the L3-combinator authoring is a cycle-050
harvester rough-in (mapped in b.3, not created here per the one-pattern / harvester-authors-the-file
discipline).

## Supporting evidence

- `book/src/L2/linear_combination.md` (read in full this invocation) — the firm cycle-018
  combinator; `:19-20` + `:193-197` the "does not replace" framing inverted in (a); `:46-49`
  signature; `:65-72` the four arity identities; `:110-189` the seven laws + non-laws (incl.
  `:166-178` the IEEE summation non-law deferring to the L2>L1 theme); `:316-345` L0 evidence.
- `book/src/L2-L1/linear-combination-fold-specialization.md` (read in full) — the (c) KEEP
  target; `:61-101` arity-dispatch; `:103-115` arity-2 sub-selection; `:117-137` `γ==0`
  fall-through; `:139-167` the pinned summation-order table; `:210-226` justification kind.
- `book/src/L3/axpy.md` (read in full) — representative L3 leaf re-deriving base form;
  `:16,22,52,68` "value-thread-isomorphic to L1"; `:58` no sequential obstruction; `:75` law 6
  GMRES-correction-sum-unfolding (the L4-propagation hook); zero `linear_combination` refs.
- `book/src/L3-L2/axpy-body-identity.md` (read in full) — representative degenerate-smell theme;
  `:14` "The body IS the identity"; the thin mirror demoted in (b.2).
- `book/src/L2-L1/scal-leaf-identity.md` (read in full) — `:80-87` "all four collapse to
  nothing … value-exact AND bit-exact"; the wholly-subsumed thin theme (b.2).
- `book/src/L2/index.md:22-28,33,45-58,76-94,111-112` — the fold-cohort boundary + the
  RATIFIED "keep leaf-floor (b)" rectangular machinery the redirect supersedes.
- `book/src/L4/krylov-step.md:67,104`, `book/src/L4/chebyshev.md:203`,
  `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:68` — the L4 base-form-by-name
  references for the (b.4) propagation note.
- Verified absences: `book/src/L3/linear_combination.md` does not exist;
  `grep -rl linear_combination book/src/L3/` → no hits (the never-propagated-to-L3 finding).
- L0 anchors (inherited via the firm combinator, not re-localized this refactor pass):
  `palace/linalg/vector.cpp:702-712,726-730,745-758`, `palace/linalg/vector.hpp:305-316`,
  `palace/linalg/nleps.cpp:343-344`, `palace/models/romoperator.cpp:188-189`,
  `palace/models/timeoperator.cpp:217` — the BLAS-1 surface the family unifies (all
  self-verified at cycle-018, cited in both read entries).

## Open questions / caveats

- **[OQ] L2/L3 leaf-chapter disposition cohort-wide: delete-vs-redirect-stub.** (b.1)/(b.3)
  recommend delete-with-SUMMARY-removal for `axpy`/`axpby`/`axpbypcz` and a redirect-stub for
  `scal` (it has live consumers `normalize`/`elementwise_product`). This convention is
  **unsettled** and should be ratified cohort-wide by the meta-phase alongside the parallel
  D2 `inner_product`/`dot`/`nrm2` decision — the two folds want the same rule. The blocking
  sub-question: do consumers (`normalize`, `elementwise_product`, `krylov-step`, the L3
  `krylov-step` body) get re-pointed at the §"Arity specializations" combinator notes, or does
  a thin redirect-stub remain the link target? Recommend re-point + delete where no consumer
  needs a named link; redirect-stub only for `scal` until its consumers migrate.
- **[OQ] Fork closure.** The batch-12 `dot-l2-leaf-floor-vs-fold-only-design` fork (RATIFIED
  keep-(b), `L2/index.md:33`) is **superseded** by the 2026-06-01 redirect (combinator-as-entry
  = the (a) fold-primary reading the fork called option (a)). The standing OQs
  `scal-leaf-vs-linear-combination-fold-realization-fork` and the index §Working-Notes fork
  entry should be **closed as superseded-by-redirect** by the meta-phase. Flagging so the
  ledger reflects the supersession rather than leaving a ratified-(b) note that now contradicts
  the entry.
- **[OQ] L4 propagation depth.** (b.4) proposes expressing the krylov-step update group and the
  chebyshev in-place `axpy`/`scal` through `linear_combination`. The krylov-correction-sum case
  is clean (law 6 already names it); the chebyshev aliased-`axpy`/`scal` case is the
  output-aliasing specialization and may read more naturally left as a named specialization
  than rewritten through the variadic fold. Recommend the cycle-050+ harvester apply the
  "flag, don't force" solver-as-test-load rule — propagate where it reads cleanly, record a
  finding where it doesn't.
- **Did not touch `inner_product.md`** (D2's wave-1 sibling) — only the reciprocal sibling-fold
  note *inside* `linear_combination.md` (per scope). The symmetric note in `inner_product.md`
  is D2's to update; if D2 does not, a cycle-050 consistency touch should align the two
  sibling-fold notes.
- **`scalar-promotion` upstream dependency unchanged** — the element-type sub-axis still carries
  its open `scalar-promotion-typing-rule` OQ (`concepts/scalar-promotion.md:49`); this refactor
  pass inherits it unchanged and does not close or alter it.

---
agent: lifter
invoked_at: 2026-05-28T214012Z
scope: L3 chebyshev §"Value-threaded form (L3 rendering)" downward prose — vocabulary refresh forM_/foldM → iterate_while_pure (sibling to cycle-015 L4 chebyshev firm enactment)
status: integrated
integrated_at: 2026-05-28T221238Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-016 (per-report position 7, LAST). Surgical 1-sentence downward-prose vocabulary refresh in L3/chebyshev.md §Value-threaded form (forM_/foldM → iterate_while_pure/iterate_while_pure_L3 with step-count predicates); 2 cross-links verified resolve. Status stays partial-obstruction. OQ l3-chebyshev-downward-prose-iterate-while-refresh resolved for named-sentence scope (ledger:2767); NEW companion OQ l3-chebyshev-sibling-formm-foldm-prose-sweep opened for the 5 remaining sibling sites. Retroactive-budget 0. Book build clean (exit 0)."
inputs:
  - book/src/L3/chebyshev.md
  - book/src/L4/chebyshev.md
---

# CYCLE: Re-anchor L3 chebyshev downward prose (forM_/foldM → iterate_while_pure)

## Summary

Cycle-015 promoted `book/src/L4/chebyshev.md` to `firm` by re-anchoring its two
sequential obstructions from the un-anchored `forM_` (outer `pc_it`) / `foldM`
(inner `k`) binds to **nested `iterate_while_pure` folds with step-count
predicates** (combinator-miner cycle-014 route (i): REUSE the firm
`iterate-while` family; the fixed-count-vs-convergence-gated distinction lives in
the *predicate*, not the combinator). The L3 entry's §"Value-threaded form (L3
rendering)" closing paragraph (lines 236–239) still names the superseded L4
`foldM`/`forM_` combinators as the thing the L3 tail recursions are "the L3
rendering of." This dispatch refreshes that one sentence to name the firm L4
vocabulary. **Pure vocabulary refresh — no L3 semantics, no L3 structure, no
other line changes.** The L3 entry stays `partial-obstruction`; only the named
downward-prose sentence at lines 236–239 is touched.

The scope is deliberately the single named-prose target (per dispatch). The L3
file carries five additional `forM_`/`foldM` mentions (lines 46, 55, 96, 475,
480) that also reference the now-superseded L4 combinator names; those are **out
of this dispatch's scope** and flagged in §Open questions for a follow-up
companion refresh (a broader L3-chebyshev `forM_`/`foldM` sweep). Touching them
here would exceed the named-line content-correction boundary.

## Proposed changes

```edit:book/src/L3/chebyshev.md
[old]: The two `if k >= op.order` / `if it > op.pc_it` tail recursions are the L3
rendering of the L4 `foldM`/`forM_` over static index ranges — the iteration
view that L3 makes load-bearing. The body inside `kloop` is the tensor-field
update above; every binding is a whole-tensor field operation.
[new]: The two `if k >= op.order` / `if it > op.pc_it` tail recursions are the L3
rendering of the L4 [`chebyshev`](../L4/chebyshev.md)'s two nested
[`iterate_while_pure`](../L4/iterate-while.md) folds over **step-count
predicates** (`c.k <= op.order - 1` inner, `s.it <= op.pc_it` outer) — the
`iterate_while_pure_L3` tail-recursion lowering image of those bounded folds (per
L4 `chebyshev` §"L4 > L3"), the iteration view that L3 makes load-bearing. The
body inside `kloop` is the tensor-field update above; every binding is a
whole-tensor field operation.
```

The replacement:
- Drops the superseded `foldM`/`forM_` combinator names.
- Names the firm L4 vocabulary (`iterate_while_pure` folds with **step-count
  predicates**), matching the cycle-015 L4 chebyshev firm enactment verbatim:
  the L4 entry renders both obstructions as `iterate_while_pure` folds with
  step-count predicates (`book/src/L4/chebyshev.md:138-145, :155-158, :175-177`),
  and its §"L4 > L3" states these dissolve to "`iterate_while_pure_L3` tail
  recursions over the step-count predicate" matching the L3 `itloop`/`kloop`
  shape (`book/src/L4/chebyshev.md:44-46, :430-432, :530-531`).
- Adds the exact predicate expressions (`c.k <= op.order - 1`,
  `s.it <= op.pc_it`) to anchor "step-count predicate" concretely — these match
  the L3 file's own tail-recursion guards (`if k >= op.order`, `if it >
  op.pc_it`, lines 224/232) by complementation, so the refresh is internally
  consistent with the code block immediately above it.
- Adds the cross-link `[`chebyshev`](../L4/chebyshev.md)` (the L3 entry already
  links L4 chebyshev elsewhere, e.g. line 22/51/397, so this introduces no new
  dangling reference) and `[`iterate_while_pure`](../L4/iterate-while.md)` (the
  canonical firm combinator entry the L4 chebyshev firm form consumes;
  `book/src/L4/iterate-while.md:7` names Chebyshev as a consumer).

No LHS/RHS shape change: the L3 tail-recursion *form* is unchanged (the code
block at lines 211–234 is untouched); only the prose label for what that form is
"the L3 rendering of" is refreshed from the dead L4 combinator names to the firm
ones.

## Discipline notes

This is a **structural rewrite, not authorship** — the theme/entry narrative,
the L3 semantics, the obstruction verdict, and the code block all stay; only the
vocabulary in one named sentence changes (the lifter pure-rewriting pass). The
rewrite direction stays high→low: the sentence narrates "the L3 [tail
recursions] are the L3 rendering of the L4 [folds]" — i.e. how the L4 form lowers
into the L3 form, with the L3 form as the rendering of the L4 source. No
inversion.

**Why name `iterate_while_pure` (the L4 fold) rather than `iterate_while_pure_L3`
(its L3 image) as the primary noun**: the sentence's grammatical object is "the
L4 [combinator]" — it says the L3 tail recursions are "the L3 rendering **of the
L4** [thing]." So the L4-side noun must be the firm L4 fold (`iterate_while_pure`
with step-count predicate), exactly as the old text said "the L4
`foldM`/`forM_`." The refresh additionally notes the L3-side image
(`iterate_while_pure_L3` tail recursion) so the reader sees both ends of the
lowering, matching the L4 entry's own §"L4 > L3" phrasing. This keeps the L3
entry's vocabulary consistent with the now-firm L4 sibling without inventing new
notation.

**Content-correction boundary respected**: the edit is bounded to the named
prose lines (236–239 per dispatch; the actual current location is unchanged —
the file did not drift). It fixes a *vocabulary drift* (the L4 combinator the L3
prose references was renamed/re-anchored upstream cycle-015), supported by the L0
of this refresh which is the firm L4 chebyshev entry I read this dispatch
(`book/src/L4/chebyshev.md`). This is a vocabulary re-anchor, not a re-architect:
no decomposition, sub-pattern, or signature changes. The five sibling
`forM_`/`foldM` mentions elsewhere in the file are NOT touched (out of named
scope) — see Open questions.

**Citation self-verification (producer-emit)**: I verified each cited L4 line
against the file I read this dispatch:
- `book/src/L4/chebyshev.md:8` — "nested `iterate_while_pure` folds with
  **step-count predicates**" (the firm-form lead sentence). ✓ on line.
- `book/src/L4/chebyshev.md:155-158` — outer `iterate_while_pure { it: 1 } (\s
  -> s.it <= op.pc_it) …`. ✓ the `s.it <= op.pc_it` step-count predicate sits
  here.
- `book/src/L4/chebyshev.md:175-177` — inner `iterate_while_pure { r, d, st, k:
  1 } (\c -> c.k <= op.order - 1) …`. ✓ the `c.k <= op.order - 1` step-count
  predicate sits here.
- `book/src/L4/chebyshev.md:44-46` — "the two `iterate_while_pure` folds dissolve
  to the L3 `iterate_while_pure_L3` tail recursions over the step-count
  predicate (`iterate-while.md:193-195`), matching the L3 `itloop`/`kloop`
  shape." ✓ on lines — this is the lowering-image phrasing I mirror.
- `book/src/L4/chebyshev.md:430-432` and `:530-531` — same `iterate_while_pure_L3`
  tail-recursion lowering image, in §"Lowers to" and §"L4 vs L3 distinction".
  ✓ on lines.
- The L3 file's own guards `if k >= op.order` (line 224) and `if it > op.pc_it`
  (line 232) — confirmed the complementary predicates `c.k <= op.order - 1` /
  `s.it <= op.pc_it` are the correct loop-continue forms (the L4 entry uses
  exactly these). ✓ internally consistent.
- Cross-link targets: `../L4/chebyshev.md` already linked at L3 lines 22/51/397
  (no new dangle); `../L4/iterate-while.md` is the firm canonical combinator
  entry (L4 chebyshev cites it as a dep, line 391). ✓ both terminal firm homes,
  not relocated-dangles.

## Supporting evidence

- `book/src/L4/chebyshev.md` (firm, re-anchored cycle-015, lifter
  `reports/2026-05-28T202138Z-lifter-chebyshev-l4-firm-via-iterate-while-reanchor/`):
  the sibling firm enactment establishing the `iterate_while_pure` + step-count-
  predicate vocabulary this L3 prose refresh adopts. §Semantics body (lines
  147–214), §"L4 > L3" (40–53, 426–435), §"L4 vs L3 distinction" (518–532),
  §Status (476–512, the former-`rough-in`-driver closure narrative).
- `book/src/L4/iterate-while.md` (cycle-007 firm) — the canonical iteration
  primitive; `:7` names Chebyshev as a consumer (per L4 chebyshev Evidence line
  556). The firm home the refreshed prose cross-links.
- Cycle-014 combinator-miner verdict (route (i): REUSE `iterate-while`) —
  `reports/2026-05-28T193256Z-combinator-miner-chebyshev-l4-wrapper-iteration-vocabulary-reconcile/`
  (per L4 chebyshev Status line 502): the upstream decision that retired the
  `forM_`/`foldM` rendering in favour of `iterate_while_pure` + step-count
  predicate, which this L3 prose refresh propagates downward.

## Open questions / caveats

- **Five sibling `forM_`/`foldM` mentions remain in `book/src/L3/chebyshev.md`**
  (out of this dispatch's named scope — the dispatch is the single ~236–239
  sentence only):
  - line 46 (§Context): "`chebyshev`'s loops are bounded `forM_`/`foldM` ranges"
  - line 55 (§Upward prose): "the `forM_`/`foldM` binds [are] tail recursions"
  - line 96 (Non-adjacent identity): "the surrounding `forM_`/`foldM` ranges"
  - lines 475, 480 (§"L3 vs L4 distinction"): the L4 side described as surfacing
    obstructions "as `forM_` (outer) and `foldM` (inner) binds" / the L3 side as
    "the `forM_`/`foldM` binds are tail recursions over static ranges"

  These reference the same superseded L4 combinator names and should be refreshed
  to the firm `iterate_while_pure` + step-count-predicate vocabulary for whole-
  entry consistency with the firm L4 sibling. I scoped this dispatch to the one
  named sentence per the dispatch instruction ("the named prose lines only").
  **Recommend a follow-up companion lifter dispatch** (or widening of the OQ
  `l3-chebyshev-downward-prose-iterate-while-refresh` close) to sweep these five
  sibling mentions — each is a pure same-shape vocabulary refresh, identical in
  character to this one. None of them changes L3 semantics. Flagging rather than
  silently widening scope, per the lifter "one theme/sentence per invocation,
  named-line boundary" discipline.

- **No signature/notation-convention shift**: the L4 firm form's signature
  (`apply :: ChebOp E S -> Bool -> Solve (ChebSim E) ()`) and notation (Haskell
  `::` / TS records / `iterate_while_pure` combinator) are unchanged by the
  cycle-015 re-anchor — the only change was the iteration-combinator vocabulary
  inside the body. So this lift stays pure rewriting; no abstractor reread is
  triggered.

- **OQ closed by this dispatch**: `l3-chebyshev-downward-prose-iterate-while-refresh`
  (the named ~236–239 sentence). Note: if the integrator prefers to keep that OQ
  open until the five sibling mentions are also swept, this dispatch closes only
  the named-sentence portion and the OQ can be re-scoped to track the remaining
  five (integrator's call).

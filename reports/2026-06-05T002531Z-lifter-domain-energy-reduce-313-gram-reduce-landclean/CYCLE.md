---
agent: lifter
invoked_at: 2026-06-05T002531Z
scope: L4 within-file land-clean re-anchor — domain_energy_reduce.md:313-316 stale gram_reduce/bilinear-form rough-in narration
status: pending
inputs:
  - book/src/L4/domain_energy_reduce.md
  - book/src/L4/gram_reduce.md
  - book/src/L1/bilinear-form.md
integrated_at: 2026-06-05T002531Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean by integrator-per-report (D3, staging row 3); no repair needed (critic clean). L4/domain_energy_reduce.md:313-316 §Status re-anchored — dropped the post-c095 falsified gram_reduce/bilinear-form rough-in assertion (both rank: firm on disk since c095), recast as the permanent rank-1-vs-rank-2 SHAPE distinction; no frontmatter/rank flip. cargo make book EXIT 0; step-5b rank_violations=0 GATE PASSES; no newly-orphaned node. OQ domain_energy_reduce-313-gram_reduce-bilinear-form-c095-stale-rough-in-narration recommended-CLOSE at batch-31 meta unify."
---

# CYCLE: Re-anchor domain_energy_reduce.md:313-316 (gram_reduce/bilinear-form firm cascade)

## Summary
The `domain_energy_reduce.md` §Status closing parenthetical (`:313-316`) asserts an "off-diagonal
contrast" in which `gram_reduce` "STAYS rough-in this same cycle because its off-diagonal folded primitive
`bilinear-form` is still rough-in." This was true the cycle the verb firmed (c091), but the cascade has
since COMPLETED: `bilinear-form` firmed and `gram_reduce` flipped to firm in cycle-095. The parenthetical
is now falsified on disk. This is a pure within-file prose re-anchor (item-2 land-clean): the stale
"STAYS rough-in" framing is replaced with the post-c095 reality (the cascade is complete; gram_reduce is
firm) while PRESERVING the legitimate rank-1-vs-rank-2 / single-field-vs-family-PAIR scope distinction the
sentence was drawing between `domain_energy_reduce` and `gram_reduce`. No `rank:`/`edges:` frontmatter
flip is needed (this is prose narration, not a status change — `domain_energy_reduce` is already firm), so
no rank-invariant question arises. The whole-file grep confirms `:313-316` is the ONLY stale
gram_reduce/bilinear-form maturity assertion; all other gram_reduce mentions are maturity-free structural
distinctions and all other `rough-in` mentions correctly narrate `domain_energy_reduce`'s OWN promotion
history.

## Paste-inline: c095 firm-flip confirmation (verified on disk this dispatch)

`book/src/L4/gram_reduce.md` frontmatter (lines 1-5):

    ---
    layer: L4
    operator: gram_reduce
    firmness: firm
    rank: firm

`book/src/L1/bilinear-form.md` frontmatter (lines 1-5):

    ---
    layer: L1
    operator: bilinear-form
    firmness: firm
    rank: firm

Both are `firmness: firm` / `rank: firm` on disk. The `:313-316` parenthetical's premise ("gram_reduce
STAYS rough-in", "bilinear-form is still rough-in") is FALSIFIED. The cascade narrated as in-progress is
complete.

## Proposed changes

```edit:book/src/L4/domain_energy_reduce.md
[old]: (The off-diagonal contrast is [`gram_reduce`](./gram_reduce.md), which STAYS rough-in this same cycle
because its off-diagonal folded primitive [`bilinear-form`](../L1/bilinear-form.md) is still rough-in —
the firm-vs-rough-in distinction is which folded primitives are firm: `domain_energy_reduce`'s two are
both firm, `gram_reduce`'s off-diagonal bilinear-form is not.)
[new]: (The structural contrast is the rank-2 family-PAIR [`gram_reduce`](./gram_reduce.md), now also firm
— its off-diagonal folded primitive [`bilinear-form`](../L1/bilinear-form.md) firmed and `gram_reduce`
flipped to firm in the cycle-095 firm-flip-and-cascade wave, so BOTH reductions now rest entirely on firm
folded primitives. The standing distinction between them is therefore NOT maturity but SHAPE:
`domain_energy_reduce` folds two scalar primitives per row over a single field (rank-1 per-domain table),
whereas `gram_reduce` folds an off-diagonal `bilinear-form` `xⱼᵀ K xᵢ` over a family-PAIR grid (rank-2,
with the `symmetric_from_upper` mirror) — the c074 D6 do-NOT-over-unify guard, which is a permanent
shape distinction independent of either verb's firmness.)
```

This re-anchor:
- Drops the falsified "STAYS rough-in" / "is still rough-in" maturity assertion (gram_reduce and
  bilinear-form are both firm on disk as of c095).
- Re-tells the cascade as COMPLETED (both reductions now rest on firm folded primitives).
- PRESERVES the legitimate `domain_energy_reduce`-vs-`gram_reduce` scope distinction the sentence drew —
  now correctly recast as a permanent rank-1-vs-rank-2 / single-field-vs-family-PAIR SHAPE distinction
  (the c074 D6 over-unification guard), which is exactly the distinction §Semantics `:133-139` and
  §Dependencies `:222-223` / `:181-183` already carry, so the re-anchored parenthetical now agrees with
  the rest of the file rather than contradicting the on-disk maturity state.

## Within-file self-consistency sweep (the discipline)

Re-read `domain_energy_reduce.md` end-to-end and grepped `rough-in`/`gram_reduce`/`bilinear-form`. Findings:

- **`:313-316`** — the ONE stale gram_reduce/bilinear-form rough-in assertion. Re-anchored above.
- **`:314`** — the file's ONLY `bilinear-form` mention; it lives inside the `:313-316` parenthetical and
  is re-anchored in the same edit (the new text retains the `bilinear-form` link, now correctly firm).
- All OTHER `gram_reduce` mentions (`:11` edge, `:34`, `:135`, `:139`, `:150`, `:182-183`, `:222-223`,
  `:264`, `:382`, `:395`) carry NO maturity claim — they are rank-1-vs-rank-2 / over-unification-guard /
  sibling-grounding structural distinctions. **Not stale; left untouched.**
- All OTHER `rough-in` mentions (`:212`, `:274`, `:280`, `:282`, `:288`, `:295`, `:402`) correctly narrate
  `domain_energy_reduce`'s OWN promotion history (promoted FROM rough-in TO firm, "former inherited-rough-in
  gate discharged", the `rough-in (test-coverage-bounded)` escape bullet it invoked). These are accurate
  self-history, NOT stale cross-references. **Left untouched.**
- The `matrix-weighted-norm` residues (`:268`/`:374`/`:377` per the dispatch note) were already fixed by
  c097-D6. Confirmed I did not touch them — out of this cohort's scope.

Result: the gram_reduce/bilinear-form cohort is a single-site fix; the file is otherwise self-consistent
with the post-c095 firm state.

## Discipline notes
- **Pure within-file prose re-anchor**, no authorship. The narrative (the §Status warrant that
  `domain_energy_reduce` is firm because both its folded primitives are firm) is preserved verbatim; only
  the closing off-diagonal-contrast parenthetical's now-false maturity premise is corrected, recast as the
  shape distinction it always structurally was.
- **L0-evidence-driven correction, bounded + evidenced + recorded** (the lifter scope-content-correction
  boundary): the correction is directly supported by two L0/disk citations read this dispatch
  (`book/src/L4/gram_reduce.md:4-5` firm, `book/src/L1/bilinear-form.md:4-5` firm), it is bounded (fixing a
  drifted maturity assertion, NOT re-architecting the entry's decomposition or signature), and it is
  recorded here. No decomposition/signature change → no abstractor/harvester reroute.
- **No rank/edges flip.** `domain_energy_reduce` is already `rank: firm` resting on `depends-on:
  L1/participation_ratio` + `L1/matrix-weighted-norm`, both firm on disk — the rank invariant
  `rank(u) ≤ min over depends-on deps` holds unchanged (this edit touches no frontmatter; baseline
  violations 0, no new violation introduced).
- **Within-file conclusion-narration guard (the c093 lifter bullet):** this dispatch IS that guard's
  worked instance — the flipped operator's own file carried a CONCLUSION narration (`:313-316`) that
  contradicted post-cascade reality. Re-anchored in the same pass as the discovery.
- **Cross-file scope note (NOT touched here, flagged for awareness):** the dispatch hard-constraints
  reserve `SUMMARY.md`/`spec/index.md`/`concepts/dependency-map.md` to D1/D2 and the `matrix-weighted-norm`
  residues to the completed c097-D6. I confirmed I touched none of these. If a whole-book grep of
  `gram_reduce`+`rough-in` co-mentions across OTHER files is desired, that is the cross-file firm-promotion
  sweep that belongs to the c095 gram_reduce flip's own land-clean lineage, not this within-file item-2;
  noting it here for the planner, not actioning it (out of this dispatch's within-file scope).

## Supporting evidence
- `book/src/L4/gram_reduce.md:4-5` — `firmness: firm` / `rank: firm` (the c095 flip, on disk).
- `book/src/L1/bilinear-form.md:4-5` — `firmness: firm` / `rank: firm` (the c095 flip, on disk).
- `book/src/L4/domain_energy_reduce.md:313-316` — the stale parenthetical re-anchored.
- `book/src/L4/domain_energy_reduce.md:133-139`, `:181-183`, `:222-223` — the in-file rank-1-vs-rank-2 /
  do-NOT-over-unify SHAPE distinction the re-anchored parenthetical now agrees with.

## Open questions / caveats
- **OQ RESOLVED:** `domain_energy_reduce-313-gram_reduce-bilinear-form-c095-stale-rough-in-narration` —
  closed by this re-anchor. The `:313-316` parenthetical now reflects the post-c095 firm reality of both
  `gram_reduce` and `bilinear-form`, with the legitimate scope distinction preserved as a shape (not
  maturity) distinction. No abstractor reread needed (bounded prose correction, decomposition unchanged).
- No contradiction between the firm gram_reduce signature and what this theme/entry assumed — the entry
  never depended on gram_reduce's maturity, only contrasted it; the contrast survives intact as a shape
  contrast. Pure lift, no reread trigger.

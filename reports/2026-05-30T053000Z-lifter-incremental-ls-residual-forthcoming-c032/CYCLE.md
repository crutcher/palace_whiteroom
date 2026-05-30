---
agent: lifter
invoked_at: 2026-05-30T053000Z
scope: L2>L1 theme prose-currency residual sweep — incremental-least-squares-composition-lowering (4 `forthcoming` `ls_update_column` L1>L0 mentions)
status: pending
integrated_at: 2026-05-30T060748Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied by integrator-per-report at 2026-05-30T055500Z; finalized cycle-032. 4 prose-currency edits at book/src/L2-L1/incremental-least-squares-composition-lowering.md :114/:276/:300/:306 — "forthcoming"→"firm" qualifier flips on `ls_update_column` L1>L0 theme references; site :306 collapses "firm-or-forthcoming-firm vocabulary" → "firm vocabulary". Left 4 historical-quote refs at :15/:145/:204/:541 untouched (correctly-quoted historical references to the L2 entry's deferred-non-law text). Closed OQ `incremental-ls-composition-lowering-residual-forthcoming-mentions-c032` with RESOLVED cycle-032 marker. Theme `## Status: firm` line + signatures + decompositions + applicability conditions + verified-against block all untouched.
inputs:
  - book/src/L2-L1/incremental-least-squares-composition-lowering.md
  - book/src/L1-L0/ls-update-column-mutation-rotation.md  (firm cycle-030, confirmed via grep `## Status` on disk)
  - scaffolding/open-questions.md — OQ `incremental-ls-composition-lowering-residual-forthcoming-mentions-c032` (the c031 D3 routing of this residual)
---

# CYCLE: Re-anchor incremental-least-squares-composition-lowering — residual `forthcoming` prose-currency sweep

## Summary

Bounded prose-currency follow-on to the c031 D3 lifter pass on
`book/src/L2-L1/incremental-least-squares-composition-lowering.md`. The c031 D3 pass upgraded the
three slug-spelled-out `ls_update_column-mutation-rotation` mentions (which were ambiguous between
"forthcoming named theme" and "now-firm named theme" and needed live-link upgrades). This c032 pass
sweeps the four remaining stale-qualifier mentions that wear "forthcoming `ls_update_column` L1>L0
theme" framing (slug-form, NOT the full `-mutation-rotation` slug; no live-link upgrade in scope —
this is qualifier-only prose-currency). On-disk locations match the c031-reported lines exactly (no
drift): `:114`, `:276`, `:300`, `:306`. The target firm theme
`book/src/L1-L0/ls-update-column-mutation-rotation.md` is `firm` on disk (line 750 `## Status`
confirmed via grep this invocation), landed cycle-030 per the OQ. Each of the 4 sites uniformly
drops the obsolete "forthcoming" framing. The four do-not-touch historical mentions at `:15`,
`:145`, `:204`, `:541` are confirmed to wear distinct framings (`forthcoming L2>L1 theme` historical
quote, or — for `:145` — the unrelated `forthcoming general trsv L1 leaf` deferred-draft historical
mention) and are left intact per scope. Theme status stays `firm`; structure unchanged; no new
citations emitted.

## Proposed changes

Four single-edit replacements, one per residual site. Inner code spans are inline `` ` `` (no
multi-line code, no nested fences). Verbatim old/new text for each.

### Site 1 — `:114` (Face 2 prose under §"Face 2 — the de-fused scalar Givens sub-step sequence")

```edit:book/src/L2-L1/incremental-least-squares-composition-lowering.md
[old]: update, deferred to the forthcoming `ls_update_column` L1>L0 theme; **this theme cites the kernel
[new]: update, deferred to the firm `ls_update_column` L1>L0 theme; **this theme cites the kernel
```

### Site 2 — `:276` (Applicability conditions, condition 5 "Leaf-stops-at-L1; kernel L0 deferred")

```edit:book/src/L2-L1/incremental-least-squares-composition-lowering.md
[old]:    in-place 2-vector updates are L1>L0 concerns of the forthcoming `ls_update_column` L1>L0 theme; the
[new]:    in-place 2-vector updates are L1>L0 concerns of the firm `ls_update_column` L1>L0 theme; the
```

### Site 3 — `:300` (Justification kind, closing prose on residue delegation)

```edit:book/src/L2-L1/incremental-least-squares-composition-lowering.md
[old]: scalar-kernel LAPACK scaling is delegated to the kernel pages + the forthcoming `ls_update_column`
[new]: scalar-kernel LAPACK scaling is delegated to the kernel pages + the firm `ls_update_column`
```

### Site 4 — `:306` (§"Speculative L1 operators" lead-in)

The remaining three bullets all already note their firm status (Face 1 `ls_update_column` firm
cycle-029; Face 2 scalar Givens kernel pair firm concept pages; terminal `back_solve` firm
cycle-027 + `linear_combination` firm). With every referenced item firm, the "firm-or-forthcoming-firm"
disjunction is stale; the lead-in collapses to plain "firm vocabulary".

```edit:book/src/L2-L1/incremental-least-squares-composition-lowering.md
[old]: **None proposed by this theme.** The L1 RHS resolves to firm-or-forthcoming-firm vocabulary:
[new]: **None proposed by this theme.** The L1 RHS resolves to firm vocabulary:
```

## On-disk line-number cross-check (c032 invocation vs c031-reported)

Per the OQ-routed scope, expected target lines were `:114`, `:276`, `:300`, `:306` (post-c031-D3
landing). Confirmed by `grep -n "forthcoming" <chapter>` this invocation: lines match **exactly**,
zero drift. The eight-occurrence grep output also enumerates the four do-not-touch historical lines
unchanged at `:15`, `:145`, `:204`, `:541`. Drift table:

| site | c031-reported | on-disk this invocation | drift |
|---|---|---|---|
| Site 1 (Face 2 prose)        | 114 | 114 | 0 |
| Site 2 (Applicability cond.5)| 276 | 276 | 0 |
| Site 3 (Justification kind)  | 300 | 300 | 0 |
| Site 4 (Speculative L1 lead) | 306 | 306 | 0 |
| do-not-touch (historical L2>L1) | 15  | 15  | 0 |
| do-not-touch (forthcoming general `trsv` historical) | 145 | 145 | 0 |
| do-not-touch (historical L2>L1) | 204 | 204 | 0 |
| do-not-touch (YAML verified_against note quoting historical) | 541 | 541 | 0 |

## Do-not-touch confirmation

Each of the four reserved sites is a **distinct framing** (NOT "forthcoming `ls_update_column` L1>L0
theme") and is preserved verbatim per scope:

- **`:15`** — `L2 entry deferred to "the forthcoming L2>L1 theme",` — the chapter intro paragraph
  quoting the L2 entry's deferred-non-law text. The L2 entry's `:278-285` non-law still wears that
  phrasing as historical record (it is the deferral that this very theme picks up); quoting it back
  is correct.
- **`:145`** — `forward-referenced the back-solve target as a forthcoming general` `trsv` `L1 leaf;
  the leaf cycle-027` — this is the **back-solve-target-is-not-general-`trsv`** historical note
  recording the deferred draft's incorrect `trsv` forward-reference. The "forthcoming" qualifier
  here is on `general trsv L1 leaf` (a DIFFERENT, still-blocked operator,
  `scaffolding/open-questions.md:24`), NOT on `ls_update_column` L1>L0 theme. Out of scope.
- **`:204`** — `This is the **load-bearing residue the L2 entry deferred to "the forthcoming L2>L1
  theme"** (L2 entry` — the §"Reduction-path recording" lead picking up the same quoted historical
  deferral as `:15`. Same correct-quote rationale.
- **`:541`** — `the load-bearing residue this theme picks up ("forthcoming L2>L1 theme");` —
  inside the YAML `verified_against` note for citation `book/src/L2/incremental-least-squares.md:278-285`,
  identifying the cited range as the very L2 deferred-non-law passage. Quoted historical, correct.

No edits to any of the four reserved sites.

## Discipline notes

- **Pure prose-currency.** Bounded qualifier flip ("forthcoming" → "firm") on four sites where the
  named L1>L0 theme is now `firm` on disk. No structural change. No new citation emission. No
  re-architecture. The theme's `## Status: firm` line, signatures, fan-down rule, reduction-path
  table, applicability conditions, verified-against block, and OQs are untouched.
- **No live-link upgrade in scope** — all four sites spell `ls_update_column` (the L1 leaf slug),
  NOT the full `ls_update_column-mutation-rotation` L1>L0-theme slug. Per the OQ routing, the c031
  D3 pass already swept the three slug-form-spelled mentions that DID warrant live-link upgrades.
  These four remaining sites are slug-as-prose-noun usage ("the X L1>L0 theme") and the existing
  qualifier `forthcoming` is the only stale element.
- **Why qualifier flip not slug-form expand.** Mechanically, "the firm `ls_update_column` L1>L0
  theme" is the minimal correction (it tells the reader "this theme exists and is firm" while
  preserving the natural-prose noun-phrase). Expanding to a live link
  `[`ls_update_column-mutation-rotation`](../L1-L0/...)` here would inflate every site's noun
  phrase and is unnecessary — the chapter has TWO bona-fide live links to that theme already
  (the c031 D3 landings), so cross-reference resolution is intact without further upgrades.
- **Site 4 doubles as a vocabulary-currency correction.** The §"Speculative L1 operators" lead-in
  collapsed because all three bullets below it are firm; saying "firm-or-forthcoming-firm" is
  promising the reader that one might still be rough-in, which is no longer true. Dropping the
  disjunction to "firm" is the natural consequence of the post-c030/c029/c027 state, NOT a fresh
  content claim — every bullet below already names its `firm cycle-XXX` provenance.
- **Layer-direction discipline maintained.** All four edits are inside the L2>L1 theme prose; none
  invert direction (no high→low ⇒ low→high flip introduced). The "firm `ls_update_column` L1>L0
  theme" framing points forward into the L1>L0 layer correctly (the theme it names is the L1>L0
  fan-down of the L1 leaf, which is the canonical downward continuation).
- **Self-verification.** Each `[old]:` string was confirmed against the on-disk read (lines 110-117
  for Site 1; lines 273-282 for Site 2; lines 297-302 for Site 3; lines 303-310 for Site 4) and is
  unique in the chapter (the `grep -n "forthcoming"` output enumerates all 8 occurrences; the 4
  targeted strings are each verbatim-unique). No new pinpoint citations are emitted (the
  `--anchor` / `--scan` deterministic self-check is not load-bearing here because no new `path:lo-hi`
  appears in the proposed-changes).

## Supporting evidence

- **The OQ routing this dispatch satisfies.** `scaffolding/open-questions.md` entry
  `incremental-ls-composition-lowering-residual-forthcoming-mentions-c032` (routed from c031 D3
  follow-up). The OQ enumerates the four target lines + the four do-not-touch reserved lines
  exactly as confirmed on-disk this invocation.
- **The named-firm target theme.**
  `book/src/L1-L0/ls-update-column-mutation-rotation.md:750` `## Status: firm` — confirmed via
  on-disk grep this invocation. Theme landed cycle-030 (per the OQ, and per the chapter's existing
  §"Open questions / caveats" entry naming the firm L1>L0 theme `(cycle-030)`).
- **The c031 D3 lifter pass.**
  `reports/2026-05-30T010851Z-lifter-incremental-ls-composition-lowering-livelink-upgrade/` (the
  earlier slug-spelled-out live-link upgrades) +
  `reports/2026-05-30T050100Z-lifter-incremental-ls-composition-lowering-prose-currency-rework/`
  (precedent prose-currency rework — same chapter, sibling residue from the c031 batch). Both are
  the structural pattern this dispatch follows: bounded prose-currency, no structural change.

## Open questions / caveats

- None blocking; this is the tail of the c031-routed residue and closes the
  `incremental-ls-composition-lowering-residual-forthcoming-mentions-c032` OQ when applied.
- The chapter's `:541` YAML `verified_against` note still says `"forthcoming L2>L1 theme"`
  intentionally (it is quoting the L2 entry's still-extant historical phrasing). If a future
  L2-side prose-currency pass eventually rewrites the L2 entry's `:278-285` non-law text to drop
  the "forthcoming" framing, this `:541` quote and the `:15` / `:204` chapter-prose quotes would
  all want a synchronised currency pass — flag for a future low-priority sweep, NOT this
  dispatch's scope.
- No abstractor / harvester re-route triggered. Every prose change here is a qualifier-only stale-
  framing flip; no signature, decomposition, or applicability condition is affected.

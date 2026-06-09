---
agent: harvester
invoked_at: 2026-06-09T030336Z
scope: cycle-153 D/E/F de-bulk CLOSER wave, dispatch C4 — E-class directive-date provenance strip (4 L3/L4 operator chapters)
status: pending
inputs:
  - skill finalization-debulk (E-class directive-date rephrase-to-drop-the-date rule)
  - exemplar book/src/L4/krylov_step.md
  - c152 PILOT pattern (critic-verified)
integrated_at: 2026-06-09T031600Z
integration_commit: 90f53b751945f76ee41273e415eaed0d248cf34b
integration_notes: "Applied clean (staging row C4). E-class de-bulked 4 firm operators L3/assemble_diagonal + L3/elementwise_product + L3/linear_combination + L4/assemble_frequency_operator (directive-date framing + 2 process pointers dropped; citation multiset byte-identical HEAD↔WT; all static facts kept). Build EXIT 0; graded-stack baseline HELD EXACTLY; step-5b/5c/5d clean. Part of cycle-153 batch-50 CLOSER — D/E/F campaign COMPLETE, A–F scan clean (D→0)."
---

# CYCLE: c153-C4 E-class directive-date de-bulk — 4 L3/L4 operator chapters

## Summary
De-bulked the `2026-0X-XX` directive-date process-provenance out of 4 firm operator
chapters (3 L3 + 1 L4), applying the `finalization-debulk` E-class rule:
**rephrase-to-drop-the-date** — drop the `2026-06-01` parenthetical/reference (and one
`METHODOLOGY-REDIRECT.md` + CLAUDE.md process pointer) while KEEPING the static
structural fact (the vocabulary-shift / anti-mirror redirect named directly, without
the date). 9 date-references stripped total (3+2+2+2). All edits are prose-only;
no node/edge/rank/status/semantics/slug/anchor change. Every citation, law, non-law,
shape-contract, and cross-link preserved verbatim. Lint baseline HELD EXACTLY.

These are firm-frontmatter operator chapters (`firmness: firm` / `rank: firm`), so no
`## Status` prose sections are present and none were touched. No cycle/batch/RE tags
were present (D-class clean already); RE6/RE references in `linear_combination` are
static refactor-cohort labels, not cycle attributions, and were left intact.

## Per-file results

| File | dates before→after | citations before→after | other process-accounting stripped |
|---|---|---|---|
| `book/src/L3/assemble_diagonal.md` | 3 → 0 | 21 → 21 | none (no cycle/batch/RE tags) |
| `book/src/L3/elementwise_product.md` | 2 → 0 | 7 → 7 | dropped `METHODOLOGY-REDIRECT.md` + `CLAUDE.md §… ⟢` process pointer at the L3>L2 in-line note (line ~147) |
| `book/src/L3/linear_combination.md` | 2 → 0 | 7 → 7 | none (RE6 cohort labels are static, kept) |
| `book/src/L4/assemble_frequency_operator.md` | 2 → 0 | 6 → 6 | none |

All citation counts match before/after — zero citation loss.

## Edits applied (E-class rephrase-to-drop-the-date)

**L3/assemble_diagonal.md** (3 sites):
- §Context "Downward to L2/L1": "demoted to an in-line note per the 2026-06-01 vocabulary-shift redirect" → "…per the vocabulary-shift redirect".
- §"Downward to L2 (in-line note)": "so per the 2026-06-01 vocabulary-shift redirect this is recorded as this in-line note" → "(an identity-in-named-terms lowering, the vocabulary-shift redirect's degenerate-edge smell), so this is recorded as this in-line note" (lifts the date into the static structural reason).
- §"Lowers to" closing: "recorded as an in-line note per the 2026-06-01 vocabulary-shift redirect" → "…per the vocabulary-shift redirect".

**L3/elementwise_product.md** (2 sites):
- §Context "Downward to L2": "Per the 2026-06-01 vocabulary-shift redirect, this degenerate edge…" → "Per the vocabulary-shift redirect, …".
- §"Lowers to" bold lead: "Per the 2026-06-01 vocabulary-shift redirect (`METHODOLOGY-REDIRECT.md`; CLAUDE.md §Methodology invariants ⟢), an identity-in-named-terms lowering…" → "Per the vocabulary-shift redirect, an identity-in-named-terms lowering…" (date + both process pointers dropped; structural fact kept).

**L3/linear_combination.md** (2 sites):
- §intro: "the propagate half of the replace-and-propagate map (vocabulary-shift redirect 2026-06-01)" → "…(vocabulary-shift redirect)".
- §Variant axes operand-category bullet: "Replace-and-propagate extension (2026-06-01 anti-mirror discipline), NOT a mirrored fold" → "Replace-and-propagate extension (anti-mirror discipline), NOT a mirrored fold".

**L4/assemble_frequency_operator.md** (2 sites):
- §intro: "(replace-and-propagate, 2026-06-01 anti-mirror discipline)" → "(replace-and-propagate, anti-mirror discipline)".
- §Context "Relationship to linear_combination": "Per the 2026-06-01 vocabulary-shift redirect this is handled by the existing combinator's operand-category axis" → "Per the vocabulary-shift redirect this is handled by…".

## Safety verification

- **dates**: 3→0, 2→0, 2→0, 2→0 (all 4 files now 0 `2026-0X-XX` references; none load-bearing — all were "per the YYYY-MM-DD redirect" process framing of a static structural fact).
- **citations**: 21→21, 7→7, 7→7, 6→6 — unchanged.
- **rank/status tokens**: all four are `firmness: firm` / `rank: firm` frontmatter entries → no `## Status` prose section exists; none touched. No frontmatter edge/rank/status edits.
- **laws / non-laws / structural facts / coupling facts**: untouched (only the directive-date framing of the L3>L2/L4>L1 identity-rotation coupling prose was rephrased; the coupling claim itself — degenerate identity-in-named-terms, recorded in-line — is preserved as the explicit static reason).
- **No slug/anchor rename, no node/edge/rank/status/semantics move.**

## Lint baseline (HOLD — confirmed exactly)

```
files=392, typed=331, untyped=61, rank_violations=0,
unresolved_depends_on_targets=0, promotion_frontier=11,
detritus=123, true_detritus=51
```
`python3 tools/graded-stack-lint/graded_stack_lint.py --book-src book/src`
post-edit RESULT: `0 rank violation(s), 123 detritus (51 true-detritus / 72 reference-reachable §2g), 61 untyped`.
Matches the pre-edit baseline EXACTLY — prose-only edits, graph unchanged.

## Open questions / caveats
None. All 9 date-references were E-class process framing (rephrased-and-dropped);
none was a governing-directive HEADER blockquote (the only KEEP carve-out), so no
date is load-bearing in these 4 files.

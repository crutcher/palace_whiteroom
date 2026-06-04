---
agent: lifter
invoked_at: 2026-06-04T022000Z
scope: feature>eigenfrequency-qfactor column — stale maturity cross-ref land-clean
status: integrated
integrated_at: 2026-06-04T023456Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-088 D2 (LOW/hygiene). 3 stale prose maturity labels flipped in book/src/feature/eigenfrequency-qfactor.{L4,L1}.md (eigenmode.L4/L1 seed→firm, eigenfreq_qfactor_reduce rough-in(test-coverage-bounded)→firm). ZERO status/count/SUMMARY/dep-map change — only parenthetical prose tokens + 1 OQ append (eigenfrequency-qfactor-column-composes-frontmatter-stale-seed-label, the out-of-scope composes: frontmatter seed residue flagged-not-fixed). Build clean. Zero gate hits."
inputs:
  - book/src/feature/eigenfrequency-qfactor.L4.md
  - book/src/feature/eigenfrequency-qfactor.L1.md
  - book/src/feature/eigenmode.L4.md (referent, firm c085)
  - book/src/feature/eigenmode.L1.md (referent, firm c085)
  - book/src/L4/eigenfreq_qfactor_reduce.md (referent, firm c082)
---

# CYCLE: Re-anchor eigenfreq-qfactor-column-stale-cross-ref-land-clean

## Summary
Pure prose maturity-label re-anchor of 3 confirmed-stale sibling/constituent cross-references in the `eigenfrequency-qfactor` feature column. The referenced entries' OWN frontmatter is already firm on disk; this dispatch only fixes the stale REFERENCE labels that pre-date those promotions. All 3 targets verified on disk (line anchors + stale text match) and all 3 referents verified `firm` in their own frontmatter before flipping. ZERO status/count/SUMMARY/dep-map-tally change — the column's own `status: firm` frontmatter is untouched, no operator counts move. This is the last land-clean residue from the pre-codification cycles (the c087 integrator flagged the `eigenfreq_qfactor_reduce` residual; the whole-book-grep firm-promotion discipline is now codified going forward).

## Verification (done before editing)

| # | Stale-ref site | Current on-disk label | Referent | Referent frontmatter (on disk) | Verdict |
|---|---|---|---|---|---|
| 1 | `book/src/feature/eigenfrequency-qfactor.L4.md:36` | `[`eigenmode.L4`]…(**seed**)` | `book/src/feature/eigenmode.L4.md` | `status: firm` (`eigenmode.L4.md:5`) — flipped firm c085 | FLIP → `(**firm**)` |
| 2 | `book/src/feature/eigenfrequency-qfactor.L4.md:38` | `[`eigenfreq_qfactor_reduce`]…(**rough-in (test-coverage-bounded)**)` | `book/src/L4/eigenfreq_qfactor_reduce.md` | `firmness: firm` (`eigenfreq_qfactor_reduce.md:4`) — firm c082 | FLIP → `(**firm**)` |
| 3 | `book/src/feature/eigenfrequency-qfactor.L1.md:34` | `[`eigenmode.L1`]…(**seed**)` | `book/src/feature/eigenmode.L1.md` | `status: firm` (`eigenmode.L1.md:5`) — flipped firm c085 | FLIP → `(**firm**)` |

All three line anchors matched the current on-disk text (no file drift since the dispatch was written). All three referents are genuinely `firm` on disk — no discrepancy; all 3 flips are warranted.

## Proposed changes

The three edits are surgical, single-token re-anchors. The `old`/`new` fences carry just enough surrounding text to make each replacement unique.

```edit:book/src/feature/eigenfrequency-qfactor.L4.md
[old]: 1. **The eigenmode driver column produces the converged eigenpair family** — [`eigenmode.L4`](./eigenmode.L4.md) (**seed**). The upstream composition root
[new]: 1. **The eigenmode driver column produces the converged eigenpair family** — [`eigenmode.L4`](./eigenmode.L4.md) (**firm**). The upstream composition root
```

```edit:book/src/feature/eigenfrequency-qfactor.L4.md
[old]: 2. **The per-mode scalar-ratio reduction** — [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) (**rough-in (test-coverage-bounded)**). The L4 per-mode scalar-ratio reduction combinator
[new]: 2. **The per-mode scalar-ratio reduction** — [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) (**firm**). The L4 per-mode scalar-ratio reduction combinator
```

```edit:book/src/feature/eigenfrequency-qfactor.L1.md
[old]: 1. **The eigenmode driver column produces the converged eigenpair set** — [`eigenmode.L1`](./eigenmode.L1.md) (**seed**). The upstream composition root
[new]: 1. **The eigenmode driver column produces the converged eigenpair set** — [`eigenmode.L1`](./eigenmode.L1.md) (**firm**). The upstream composition root
```

## Discipline notes
- Pure structural re-anchor: only the parenthetical maturity LABEL on each cross-reference changed (`seed`→`firm` ×2, `rough-in (test-coverage-bounded)`→`firm` ×1). No narrative, signature, decomposition, LHS/RHS, or applicability content touched. The high→low rewrite direction is preserved (untouched).
- Each flip is evidenced by the referent's OWN on-disk frontmatter (the firm `status:` / `firmness:` line, cited per row in the Verification table) — this re-anchors the stale REFERENCE to the now-firm referent, it does not assert any new maturity.
- Scope discipline held: the `eigenfrequency-qfactor` column's own `status: firm` (frontmatter line 5 of both files) is NOT touched; no operator count, SUMMARY.md entry, or dep-map tally is affected by a parenthetical prose label.
- Confirms the column-flip / firm-promotion whole-book-grep discipline (codified this batch): these 3 were exactly the genuinely-stale freeform-prose maturity mentions that `linkcheck2` does not catch.

## Supporting evidence
- Stale sites (current on-disk): `book/src/feature/eigenfrequency-qfactor.L4.md:36`, `:38`; `book/src/feature/eigenfrequency-qfactor.L1.md:34`.
- Firm referents (own frontmatter on disk): `book/src/feature/eigenmode.L4.md:5` (`status: firm`); `book/src/feature/eigenmode.L1.md:5` (`status: firm`); `book/src/L4/eigenfreq_qfactor_reduce.md:4` (`firmness: firm`).
- c087 integrator flagged the `eigenfreq_qfactor_reduce` residual (dispatch brief); c085 flipped the eigenmode columns firm; c082 firmed `eigenfreq_qfactor_reduce` (firm-on-positive-structure escape).

## Open questions / caveats
- **Out-of-scope frontmatter `seed` drift observed (NOT flipped — flagged only).** Both column files carry a matching stale `seed` label in their YAML `composes:` block, pointing at the same now-firm eigenmode column:
  - `book/src/feature/eigenfrequency-qfactor.L4.md:7` — `book/src/feature/eigenmode.L4.md (seed — the producing driver column: …)` — referent is firm (`eigenmode.L4.md:5`).
  - `book/src/feature/eigenfrequency-qfactor.L1.md:7` — `book/src/feature/eigenmode.L1.md (seed — the producing driver column: …)` — referent is firm (`eigenmode.L1.md:5`).

  These are `composes:` FRONTMATTER `seed` annotations, and the dispatch HARD CONSTRAINTS scope me to exactly the 3 PROSE maturity labels and explicitly forbid touching `status:` frontmatter. I treated the whole frontmatter block as off-limits and did NOT flip them. They are genuinely stale by the same evidence (referent firm on disk) and are a natural co-target for a follow-up frontmatter-hygiene pass or the next column-flip dispatch's whole-book grep — flagging here so they are not lost. No build impact (`linkcheck2` does not read these annotation labels).
- No discrepancies found among the 3 in-scope targets: all referents genuinely firm, all 3 flips warranted. Zero status/count/SUMMARY change confirmed.

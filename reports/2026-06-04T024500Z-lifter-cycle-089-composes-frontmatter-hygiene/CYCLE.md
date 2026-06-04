---
agent: lifter
invoked_at: 2026-06-04T024500Z
scope: feature-column composes-frontmatter hygiene re-anchor — eigenfreq-qfactor-column-composes-frontmatter-seed-hygiene
status: integrated
integrated_at: 2026-06-04T030135Z
integration_commit: c05b298
integration_notes: "Applied cycle-089 D2 (LOW/hygiene). 2 stale seed→firm flips in the composes: frontmatter parenthetical of book/src/feature/eigenfrequency-qfactor.{L4,L1}.md (the eigenmode constituent; referent eigenmode.{L4,L1}.md is status: firm on disk c085). The column's OWN status: firm (line 5) is UNTOUCHED; the flip is an inline-parenthetical word only, so YAML structure round-trips unchanged. ZERO status-token / count / SUMMARY / dep-map change; no cascade. RESOLVES the c088-opened OQ eigenfrequency-qfactor-column-composes-frontmatter-stale-seed-label. Build clean (cargo make book + linkcheck2 exit 0; the changed text is inside composes: YAML annotation labels linkcheck2 does not read). Zero gate hits."
inputs:
  - book/src/feature/eigenfrequency-qfactor.L4.md
  - book/src/feature/eigenfrequency-qfactor.L1.md
  - book/src/feature/eigenmode.L4.md
  - book/src/feature/eigenmode.L1.md
  - scaffolding/open-questions.md (OQ eigenfrequency-qfactor-column-composes-frontmatter-stale-seed-label)
---

# CYCLE: Re-anchor eigenfreq-qfactor-column-composes-frontmatter-seed-hygiene

## Summary
The cycle-085 firm-flip of the **eigenmode** feature column (both `eigenmode.L4.md` and `eigenmode.L1.md` now carry `status: firm`) staled the maturity label that the two **eigenfrequency-qfactor** output-product column files carry for their `eigenmode` constituent inside their `composes:` YAML frontmatter. Both files label the eigenmode column `seed` in an inline parenthetical on the `composes:` list entry, but the referent is now `firm` on disk. This is the cycle-088 D2 follow-up: a bounded frontmatter-hygiene re-anchor flipping the two stale `seed` labels to `firm`. No structured `status:`/`maturity:` sub-key is involved — the label is inline-parenthetical prose on the `composes:` list item — so the YAML structure is untouched and round-trips unchanged; only the parenthetical word `seed` becomes `firm`. The column's OWN `status: firm` frontmatter (line 5 of each file) is untouched; no count, SUMMARY.md, or dep-map tally changes.

## Verification (performed first, recorded here)

**1. Exact YAML structure + stale label location.** The `composes:` block is a YAML sequence of plain scalar strings; the maturity label is an **inline parenthetical inside the scalar**, NOT a structured `status:`/`maturity:` sub-key. Confirmed on disk:

- `book/src/feature/eigenfrequency-qfactor.L4.md:7` —
  `  - book/src/feature/eigenmode.L4.md (seed — the producing driver column: supplies the converged eigenpair family)`
- `book/src/feature/eigenfrequency-qfactor.L1.md:7` —
  `  - book/src/feature/eigenmode.L1.md (seed — the producing driver column: supplies the converged EigResult)`

The second `composes:` entry in each file (the `eigenfreq_qfactor_reduce` combinator) is already labelled `firm` and is correct (firm-promoted c082) — left untouched.

**2. Referent is firm on disk (flip warranted).** Confirmed line 5 of each eigenmode column file:
- `book/src/feature/eigenmode.L4.md:5` → `status: firm`
- `book/src/feature/eigenmode.L1.md:5` → `status: firm`

The c085 eigenmode-column firm-flip is on disk, so labelling its constituent reference `firm` in the consuming columns is warranted.

**3. No discrepancy.** The stale `seed` label is exactly where the OQ said (line 7 of each file, `composes:` block). The OQ's "may be a `status:`/`maturity:` sub-key" hedge resolves to: it is an **inline parenthetical**, recorded above for the integrator's exact-match.

**4. Column own-status untouched.** Each eigenfrequency-qfactor file's OWN `status: firm` (line 5) is NOT in scope and is NOT edited. No operator count, SUMMARY.md row, or dep-map tally is touched.

## Proposed changes

```edit:book/src/feature/eigenfrequency-qfactor.L4.md
[old]:   - book/src/feature/eigenmode.L4.md (seed — the producing driver column: supplies the converged eigenpair family)
[new]:   - book/src/feature/eigenmode.L4.md (firm — the producing driver column: supplies the converged eigenpair family)
```

```edit:book/src/feature/eigenfrequency-qfactor.L1.md
[old]:   - book/src/feature/eigenmode.L1.md (seed — the producing driver column: supplies the converged EigResult)
[new]:   - book/src/feature/eigenmode.L1.md (firm — the producing driver column: supplies the converged EigResult)
```

## Discipline notes
Pure frontmatter-hygiene re-anchor: the only token changed in each file is the single word `seed` → `firm` inside the `composes:` list entry's parenthetical for the eigenmode constituent. This is a bounded maturity-token re-anchor of the kind the lifter role-spec covers (the firm-promotion-coupled re-anchor of a stale constituent label, the consuming-column side of the eigenmode c085 promotion). The YAML structure (a sequence of plain scalars) is unchanged — both list entries remain plain scalar strings with identical indentation, so the block round-trips/parses exactly as before; only the parenthetical word differs.

This is the consuming-column residue of the eigenmode firm-promotion — exactly the kind of cross-reference maturity-token drift the firm-promotion whole-book grep guard targets. The eigenmode-column promotion landed c085; this dispatch mops up the two genuinely-stale consuming references in the eigenfrequency-qfactor output-product column. I confirmed (per scope) these two are the residue cycle-088 D2 flagged; this is not a fresh promotion, so no broader grep sweep is mandated for THIS dispatch beyond the two named targets.

No prose-correction beyond the maturity token; no decomposition/signature change; no abstractor reroute needed.

## Supporting evidence
- Stale labels (the deliverable, verbatim above): `book/src/feature/eigenfrequency-qfactor.L4.md:7`, `book/src/feature/eigenfrequency-qfactor.L1.md:7`.
- Firm referent (warrants the flip): `book/src/feature/eigenmode.L4.md:5`, `book/src/feature/eigenmode.L1.md:5` (both `status: firm`, c085).
- OQ: `scaffolding/open-questions.md` — `eigenfrequency-qfactor-column-composes-frontmatter-stale-seed-label` (cycle-088 D2).
- The eigenfreq_qfactor_reduce constituent (the other `composes:` entry) is already-firm-labelled and correct: `book/src/L4/eigenfreq_qfactor_reduce.md` (firm-promoted c082).

## Open questions / caveats
- None. The flip is a 1-token-per-file maturity re-anchor with a firm on-disk referent; no signature/decomposition contradiction surfaced. The column's own `status: firm` and all counts/tallies are out of scope and untouched.
- This OQ (`eigenfrequency-qfactor-column-composes-frontmatter-stale-seed-label`) is resolved by this dispatch's proposed changes — the integrator may close it on integration.

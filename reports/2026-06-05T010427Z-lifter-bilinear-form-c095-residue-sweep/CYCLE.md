---
agent: lifter
invoked_at: 2026-06-05T01:13:35Z
scope: bilinear-form-c095 stale-narration residue sweep (whole-book, EXCLUDING the D2-owned krylov hub + the c098-D3-fixed domain_energy_reduce.md:313)
status: integrated
integrated_at: 2026-06-05T010427Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean by integrator-per-report (cycle-099 staging row 3/3) as a VERIFIED CLEAN NO-OP. D3: whole-book bilinear-form-c095 firm-flip residue sweep found ZERO genuinely-stale instances outside the krylov hub; L2/index.md:89 re-confirmed NON-stale on disk; bookkeeping-only, no artifact edit. Build-relevant: no. Recommended-CLOSE OQ: bilinear-form-c095-residue-sweep-clean-noop-and-L2-index-89-confirmed-non-stale (for batch-31 meta unify)."
inputs:
  - book/src/L4/gram_reduce.md
  - book/src/L1/bilinear-form.md
---

# CYCLE: Re-anchor bilinear-form-c095-residue-sweep — VERIFIED CLEAN NO-OP

## Summary

This is dispatch D3 of cycle-099 (batch-31): the whole-book follow-up to the cycle-095
`bilinear-form` firm-flip cascade, hunting any remaining narration of the form
"`gram_reduce` stays rough-in because `bilinear-form` is rough-in" (or "`bilinear-form`
is rough-in") in NON-krylov-hub files. Both operators are confirmed `firmness: firm` +
`rank: firm` on disk (frontmatter pasted below). I grepped the whole `book/src/` for
the residue class and triaged **every** `gram_reduce`/`bilinear-form` ⨯ `rough-in`
co-mention (12 + 20 raw line hits across 12 files). **EVERY surviving hit is correct
post-cascade narration** — either (a) past-tense promotion/discharge provenance
("promoted rough-in→firm cycle-095", "now also firm", "ENACTED cycle-095"), (b) a
deliberately-historical worked-example / arc-narrative passage in the methodology
chapters (`resolution-ladder.md`, `goal-flow.md`) that frames the `rough-in` state as
an explicitly-closed past arc-point, (c) an immutable OQ-slug identifier
(`matrix-weighted-norm-and-bilinear-form-l1-rough-ins`), (d) the FE-assembly slug-collision
`bilinear-form` (a DIFFERENT operator, explicitly disambiguated), or (e) a `rough-in`
about a different operator (`sparameter_reduce` c075 state, `weak_form_term`,
`L2/product-of-operators`/`sum-of-operators`). **The c098-D3 `domain_energy_reduce.md:313`
fix appears to have been the last genuinely-stale instance.** This is a verified
clean-no-op land — no proposed changes.

## On-disk firmness verification (precondition)

`book/src/L4/gram_reduce.md` frontmatter:

    layer: L4
    operator: gram_reduce
    firmness: firm
    rank: firm
    edges:
      depends-on:
        - L1/matrix-weighted-norm
        - L1/bilinear-form
        - L4/solve_family
      reference:
        - L4/inner_product
        - L4/linear_combination

`book/src/L1/bilinear-form.md` frontmatter:

    layer: L1
    operator: bilinear-form
    firmness: firm
    rank: firm
    edges:
      depends-on:
        - L1/dot
        - L1/apply_linop
        - L1/matrix-weighted-norm
      reference:
        - L1-L0/bilinear-form-mutation-rotation

Both `firm` + `rank: firm`. Rank invariant holds on disk: `gram_reduce`'s
`depends-on` deps (`matrix-weighted-norm` firm c091, `bilinear-form` firm c095,
`solve_family` firm c086) are all `firm`; `bilinear-form`'s deps (`dot`, `apply_linop`,
`matrix-weighted-norm`) are all `firm`. No new rank violation; baseline 0 preserved.
(This is a prose-only sweep — no frontmatter rank flips proposed, so the rank bullet
is a confirm, not an edit.)

## Grep evidence (paste-inline)

### Pattern 1 — `grep -rn 'gram_reduce' ... | grep -i 'rough-in'` (12 line hits)

    book/src/methodology/resolution-ladder.md:114   — worked-example: "nothing above it could exceed rough-in — so gram_reduce and domain_energy_reduce were each capped" → HISTORICAL discharge illustration (file states "completed rank-propagation discharge, not a standing block" :120; "every node ... is now firm" :145). NOT stale.
    book/src/methodology/resolution-ladder.md:134   — "gram_reduce was correctly held at rough-in ... until that last support firmed" → past-tense, "Cycle-095 ... discharged it" follows :136. NOT stale.
    book/src/feature/index.md:51                     — "rough-in" is sparameter_reduce's c075-authored state ("authored c075 D6, `rough-in`"), NOT gram_reduce/bilinear-form. NOT stale.
    book/src/feature/index.md:55                     — narrates the CLOSED cascade ("After the cycle-095 ... ALL FIVE ... have promoted"; "gram_reduce firmed"). NOT stale.
    book/src/methodology/goal-flow.md:215            — blockquoted arc-narrative pre-c091 point ("they correctly STAY seed" AT THAT ARC POINT; discharge narrated :222-264). NOT stale.
    book/src/methodology/goal-flow.md:217            — same arc-point list ("own gram_reduce rough-in"); historical FLOW record. NOT stale.
    book/src/methodology/goal-flow.md:263            — "gram_reduce and bilinear-form were still rough-in" (PAST tense, "at that point") in the batch-29-landed arc record. NOT stale.
    book/src/L4/index.md:32                           — "promoted ... gram_reduce rough-in (test-coverage-bounded) → firm" (cycle-095). Correct firm narration. NOT stale.
    book/src/L4/index.md:50                           — domain_energy_reduce cell, "promoted rough-in→firm cycle-091". Correct. NOT stale.
    book/src/L4/index.md:58                           — "Rough-in at L4 (0) — the rough-in cohort is now genuinely empty: gram_reduce promoted to firm cycle-095". Correct (says cohort EMPTY). NOT stale.
    book/src/L4/index.md:97                           — domain_energy_reduce status cell, "promoted rough-in→firm cycle-091 D3". Correct. NOT stale.
    book/src/L4/index.md:101                          — gram_reduce dep-map cell: status reads `firm`; "promoted rough-in (test-coverage-bounded)→firm cycle-095". Correct. NOT stale.

### Pattern 2 — `grep -rn 'bilinear-form' ... | grep -i 'rough-in'` (20 line hits; non-overlapping subset)

    book/src/L2/index.md:89                           — *** D2-OWNED FILE — NOT INSPECTED, NOT TOUCHED *** (byte-disjoint guard). Flagged in Open questions.
    book/src/L1-L0/index.md:52                        — "rough-in" is weak_form_term; the bilinear-form here is the FE-ASSEMBLY slug-collision (BilinearForm class assembler), explicitly disambiguated ("distinct from BLAS-2 bilinear-form"). NOT the L1/bilinear-form operator. NOT stale.
    book/src/L0/linalg-operator-file.md:88            — "rough-in" is L2/product-of-operators + L2/sum-of-operators; bilinear-form is a bare anchor reference. NOT stale.
    book/src/feature/index.md:55                      — (dup of pattern-1) closed-cascade narration. NOT stale.
    book/src/methodology/resolution-ladder.md:133     — "off-diagonal bilinear-form primitive, still rough-in after c091" → past-state of wave-2 worked example ("Wave 2 (cycle-095) ... discharged it" :136). NOT stale.
    book/src/methodology/goal-flow.md:263             — (dup) past-tense arc record. NOT stale.
    book/src/L4/index.md:32, :58, :101                — (dup) correct firm narration of gram_reduce, citing the folded bilinear-form firm c095. NOT stale.
    book/src/L1/matrix-weighted-norm.md:137           — "the bilinear-form half ... (promoted firm cycle-095, the firm-on-positive-structure escape)"; OQ "now fully answered". Correct. NOT stale.
    book/src/L1/matrix-weighted-norm.md:160           — cites the immutable OQ slug `...-l1-rough-ins`. NOT a maturity assertion. NOT stale.
    book/src/L1/bilinear-form.md:48                    — own file: "is **firm** (promoted from rough-in cycle-095...)". Correct. NOT stale.
    book/src/L1/bilinear-form.md:260                   — own file: cites OQ slug `...-l1-rough-ins`. NOT stale.
    book/src/L1/index.md:31, :44, :68, :77, :102, :114 — all correct firm narration (status cell :114 reads `firm`; :68/:102 read "empty as of cycle-095"; :77 is the FE-assembly slug-collision note). NOT stale.

### Pattern 3 — present-tense residual filter (excluding promot/was/were/firmed/→firm/empty/escape)

    grep 'gram_reduce' | grep rough-in | grep -v <discharge-verbs>  →  goal-flow.md:215, :217 · feature/index.md:51 · resolution-ladder.md:114
    grep -iE '(still|stays|remains|is|are) ... (gram_reduce|bilinear-form) ... rough-in'  →  ZERO hits.

All four pattern-3 survivors are already triaged above (arc-narrative / sparameter_reduce
c075 state / worked-example). No present-tense "stays rough-in" assertion about either
operator exists anywhere in the book.

### Within-file conclusion-narration check (the flipped operators' OWN files)

Per the lifter within-file-residue guard, I read both flipped operators' own files
end-to-end for stale CONCLUSION prose contradicting their firm `## Status`:

- `L4/gram_reduce.md` (`rough-in` at :202, :231, :265) — all past-tense discharge
  narration ("Promoted rough-in→firm by the cycle-095 ... wave"; "the only thing that
  held the verb at rough-in ... which the c095 bilinear-form flip **clears**"). The
  c095-D3 within-file flip was clean. No residue.
- `L1/bilinear-form.md` (`rough-in` at :48, :260, :331, :345, :482) — all past-tense
  ("is **firm** (promoted from rough-in ...)"; "**ENACTED (cycle-095, this dispatch)**")
  or immutable OQ-slug identifiers. The c095-D1 within-file flip was clean. No residue.

### c098-D3 excluded fix (confirmed already-corrected, NOT touched)

`book/src/L4/domain_energy_reduce.md:313` now reads "the rank-2 family-PAIR
`gram_reduce`, **now also firm**" — the c098-D3 land-clean fix is present and correct.
Per scope, not touched.

## Proposed changes

**NONE.** Verified clean no-op. The residue class is empty across all non-excluded
files; the c098-D3 `domain_energy_reduce.md:313` fix was the last genuinely-stale
instance. Every remaining `gram_reduce`/`bilinear-form` ⨯ `rough-in` co-mention is
correct post-cascade narration (promotion provenance, deliberate historical
worked-example/arc-record, immutable OQ-slug, slug-collision disambiguation, or a
`rough-in` about a different operator).

## Discipline notes

- This is a **structural/maturity sweep**, not authorship. I made no content decisions
  and propose no edits. The cascade's prose was already fully re-anchored at land time
  (c095-D1/D3 within-file passes) and by the c098-D3 cross-file land-clean.
- **The methodology chapters (`resolution-ladder.md`, `goal-flow.md`) are
  history-bearing by design** — they narrate the rank invariant via the
  `matrix-weighted-norm`→`gram_reduce`→4-columns cascade AS A COMPLETED worked example,
  framing each `rough-in` state as an explicitly-closed past arc-point ("a completed
  rank-propagation *discharge*, not a standing block"; "every node ... is now firm").
  Re-anchoring those `rough-in` mentions would **destroy a deliberate historical
  record** — they are NOT stale maturity assertions and correctly require no edit. I
  flag this explicitly so a future residue-sweep does not mistake them for drift.
- The whole-book firm-promotion cross-reference grep my role-spec mandates was
  effectively re-run here as the sweep's core deliverable; it confirms the c095
  promotion's prose residue is fully discharged book-wide (modulo the one D2-owned
  L2/index.md line I am byte-disjoint-barred from inspecting — see Open questions).

## Supporting evidence

- `book/src/L4/gram_reduce.md` — `firmness: firm`, `rank: firm`; in-file `rough-in` at
  :202/:231/:265 all past-tense discharge.
- `book/src/L1/bilinear-form.md` — `firmness: firm`, `rank: firm`; in-file `rough-in`
  at :48/:260/:331/:345/:482 all past-tense or OQ-slug.
- `book/src/L4/domain_energy_reduce.md:313` — the c098-D3 fix ("now also firm"),
  confirmed present.
- cycle-095 cascade reports (the `bilinear-form-firm-flip-and-cascade-wave`, D1 +
  D3), referenced throughout the index/methodology provenance prose.

## Open questions / caveats

- **`book/src/L2/index.md:89`** carries a `bilinear-form` ⨯ `rough-in` co-mention. It is
  inside the D2-owned byte-disjoint exclusion set for cycle-099, so I did NOT inspect or
  edit it. **For D2 / the next cycle:** confirm whether `L2/index.md:89` is a genuinely-stale
  maturity assertion about the BLAS-2 `L1/bilinear-form` (now firm) or a correct mention
  (e.g. of the L2 `product-of-operators`/`sum-of-operators` rough-ins, or the FE-assembly
  slug-collision). My pattern-2 triage of the analogous `L1-L0/index.md:52` and
  `L0/linalg-operator-file.md:88` lines found BOTH were non-stale (different operator /
  bare-anchor), so the L2 line is plausibly non-stale too — but it must be verified by the
  hub owner, not assumed.
- No other caveat. The sweep is a clean verified land.

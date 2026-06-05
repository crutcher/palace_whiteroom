---
agent: lifter
invoked_at: 2026-06-04T233724Z
scope: L4 within-file maturity re-anchor — domain_energy_reduce (matrix-weighted-norm c091 firm-flip residue)
status: integrated
integrated_at: 2026-06-04T232852Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean by integrator-per-report (D6); 3 within-file mwn maturity re-anchors (:377/:268/:374 rough-in (test-coverage-bounded) -> firm, firm-on-positive-structure escape; participation_ratio c077 + matrix-weighted-norm c091 both firm). NO node status flip (rank: firm already on disk). Batch finalize cycle-097: cargo make book EXIT 0, step-5b rank_violations=0 (GATE PASS), no newly-orphaned node. retroactive-budget global 0. OQ domain_energy_reduce-377-mwn-stale-rough-in-residue recommended-CLOSE; NEW follow-up domain_energy_reduce-313-gram_reduce-bilinear-form-c095-stale-rough-in-narration logged."
inputs:
  - book/src/L4/domain_energy_reduce.md
  - book/src/L1/matrix-weighted-norm.md
---

# CYCLE: Re-anchor stale matrix-weighted-norm maturity narration in domain_energy_reduce.md

## Summary

Cycle-091 (batch-29 LEAD `matrix-weighted-norm-firm-flip-and-cascade-wave`) promoted
`matrix-weighted-norm` from `rough-in (test-coverage-bounded)` to `firm`. The cascade flipped
`domain_energy_reduce`'s frontmatter `rank: firm`, its `## Status` (`:274`), and its `## Dependencies`
(`:209-212`) to firm, BUT left three within-file CONCLUSION narrations still asserting the OLD
`matrix-weighted-norm` rough-in verdict — the batch-29 `firm-flip-leaves-within-file-stale-narration`
class. This is a pure within-file maturity re-anchor: the file's own firm `## Status`/`## Dependencies`
are the authoritative referent; three lagging sites in the `## Lowers to` and `## Evidence` sections now
contradict them. No frontmatter rank flip (the file is already `firm`); no structural/decomposition
change. Closes OQ `domain_energy_reduce-377-mwn-stale-rough-in-residue`.

## c091 firm-flip confirmation (paste-inline, read on disk this dispatch)

`book/src/L1/matrix-weighted-norm.md` confirms the flip:

- Frontmatter `:4`: `rank: firm`.
- `## Status` `:121-123`:
  > `firm` — promoted from `rough-in (test-coverage-bounded)` by the batch-28 meta-phase GO
  > (`reports/2026-06-04T032609Z-meta-phase-cycle-090/CYCLE.md` §Decisions "go 1"; enacted cycle-091,
  > the batch-29 LEAD `matrix-weighted-norm-firm-flip-and-cascade-wave`). ... **both norm-axiom
  > law-sides are now discharged** ...
- `:128`: "**The basis is the firm-on-positive-structure escape** ... the entry was promoted to `firm`
  cycle-091 (batch-29 LEAD)."

So the `(rough-in (test-coverage-bounded))` assertion on `matrix-weighted-norm` is FALSIFIED on disk;
the correct token is `firm` (promoted cycle-091). Rank invariant: `domain_energy_reduce` (rank firm)
`depends-on` `L1/participation_ratio` (firm c077) and `L1/matrix-weighted-norm` (firm c091) — both deps
read ≥ firm on disk, so `rank(u)=firm ≤ min(firm, firm)` holds; no new rank violation, no frontmatter
edit needed.

## Within-file stale-residue catalog (the batch-29 self-consistency grep)

Re-read `domain_energy_reduce.md` end-to-end. Three sites assert the OLD `matrix-weighted-norm`
rough-in verdict and contradict the file's own firm `## Status`/`## Dependencies`:

1. **`:377`** (Evidence §"Folded L1 primitives") — the scope's named site. Asserts `matrix-weighted-norm`
   is `(rough-in (test-coverage-bounded))`. FALSIFIED by c091; directly contradicts §Dependencies `:209`
   `(firm c091)` and §Status `:286-288` ("BOTH folded primitives now have firm L1 homes").
2. **`:268`** (`## Lowers to`) — `the (firm / rough-in) L1 folded primitives' own L1>L0 rotations`.
   The `(firm / rough-in)` parenthetical encodes participation_ratio-firm + matrix-weighted-norm-rough-in.
   Post-c091 BOTH are firm; this is a stale within-file maturity narration on matrix-weighted-norm.
3. **`:374`** (Evidence §"Supporting test") — `(the rough-in test-gate, §Status point 2)`. Narrates the
   verb's OWN former test-gate as a live "rough-in test-gate", contradicting the firm §Status (`:289-300`,
   which holds the missing per-domain test REDUNDANT under the firm-on-positive-structure escape and the
   verb firm). An Evidence-section conclusion still asserting the old verdict — the batch-29
   within-file class.

Confirmed NOT stale (correct as-is, left untouched): `:212` "former inherited-rough-in gate" (past-tense,
discharged-gate record); `:280`/`:282` "formerly-rough-in"/"to `rough-in`" (past-tense reasoning);
`:288` "least-firm folded primitive" cap (described as removed); `:313-316` gram_reduce "STAYS rough-in"
(a DIFFERENT verb, correctly still rough-in via its `bilinear-form` off-diagonal — though note
`bilinear-form` itself flipped firm c095; that gram_reduce narration is out of this dispatch's scope and
is a separate gram_reduce-cohort follow-up, NOT touched here).

## Proposed changes

### Site 1 — `:377` Evidence §"Folded L1 primitives"

```edit:book/src/L4/domain_energy_reduce.md
[old]: - **Folded L1 primitives:** [`participation_ratio`](../L1/participation_ratio.md) (firm c077 — the
  `energyᵢ/e_total` quotient half; :188-191 disclaims the numerator-energy reduction as "named not authored"
  = THIS verb), [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in (test-coverage-bounded) —
  the `½⟨field, M field⟩` energy-form half).
[new]: - **Folded L1 primitives:** [`participation_ratio`](../L1/participation_ratio.md) (firm c077 — the
  `energyᵢ/e_total` quotient half; :188-191 disclaims the numerator-energy reduction as "named not authored"
  = THIS verb), [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (firm c091 — the
  `½⟨field, M field⟩` energy-form half; promoted by the batch-29 firm-flip-and-cascade wave on the
  firm-on-positive-structure escape).
```

### Site 2 — `:268` `## Lowers to`

```edit:book/src/L4/domain_energy_reduce.md
[old]: (`postoperator.cpp:1033, 1058`) — lives in the field-energy postoperator L0 and the (firm / rough-in) L1
folded primitives' own L1>L0 rotations. This entry records the rotation direction in-line per high→low
discipline; it does not author a theme.
[new]: (`postoperator.cpp:1033, 1058`) — lives in the field-energy postoperator L0 and the (both firm) L1
folded primitives' own L1>L0 rotations. This entry records the rotation direction in-line per high→low
discipline; it does not author a theme.
```

### Site 3 — `:374` Evidence §"Supporting test"

```edit:book/src/L4/domain_energy_reduce.md
[old]: (the rough-in test-gate, §Status point 2).
[new]: (the per-domain test-gate that §Status point 2 holds REDUNDANT under the firm-on-positive-structure
  escape, the verb being firm).
```

## Discipline notes

- **All three edits are bounded prose-maturity re-anchors** — they update lagging maturity narration to
  match the file's own authoritative firm `## Status` (`:274`) + `## Dependencies` (`:209-212`), both of
  which the c091 cascade already firmed. No decomposition, signature, law, or citation-RANGE change. This
  is the batch-29 `firm-flip-leaves-within-file-stale-narration-in-flipped-operators-own-entry` discipline:
  the cross-file whole-book grep re-anchors OTHER files; this re-anchors the flipped verb's OWN file beyond
  its `## Status` line.
- **L0-evidence-driven correction is the same fact, no new claim.** The corrected token (`firm c091`)
  is directly read off `book/src/L1/matrix-weighted-norm.md:4,121-128` (paste-inline above). No positive
  Palace site needed beyond confirming the dependency's own firm Status — this is maturity-token
  bookkeeping, not a new algebraic claim.
- **No frontmatter rank flip.** `domain_energy_reduce.md:4` already reads `rank: firm`; both `depends-on`
  deps are firm on disk; the rank invariant `rank(u) ≤ min over depends-on deps` already holds. The
  baseline `rank_violations == 0` is preserved (no new violation introduced).
- **High→low discipline preserved.** All three edits are within Evidence / Lowers-to prose narrating the
  L4 verb's folded-primitive maturity; no rewrite direction inverted, no L_n-lifts-up note introduced into
  formal chapter content.

## Supporting evidence

- `book/src/L1/matrix-weighted-norm.md:4` (`rank: firm`), `:121-123` (`## Status` firm, promoted c091
  batch-29 LEAD), `:128` (firm-on-positive-structure escape basis) — the c091 firm-flip, read on disk.
- `book/src/L4/domain_energy_reduce.md:209-212` (`## Dependencies`, already firm c091), `:274` (`## Status`
  firm), `:286-288` ("BOTH folded primitives now have firm L1 homes") — the file's own authoritative firm
  narration that the three lagging sites contradict.
- Provenance: cycle-091 cascade (`matrix-weighted-norm-firm-flip-and-cascade-wave`) flipped the structured
  surfaces but missed three within-file conclusion narrations — exactly the batch-29 friction-ledger
  `firm-flip-leaves-within-file-stale-narration` class this land-clean closes.

## Open questions / caveats

- **OQ-resolution (this dispatch):** `domain_energy_reduce-377-mwn-stale-rough-in-residue` is RESOLVED by
  the three proposed edits above — `:377` (the named site) plus the two co-located within-file residues
  (`:268`, `:374`) surfaced by the batch-29 self-consistency grep. The integrator may close the OQ on
  application.
- **Out-of-scope, flagged not touched (per hard constraints):**
  - `book/src/L2/index.md:112,121` `normalize_B`-gate phrasing — judged mildly-stale-in-framing only;
    a separate normalize-cohort follow-up. NOT touched.
  - `domain_energy_reduce.md:313-316` gram_reduce "STAYS rough-in" narration — `gram_reduce`'s
    off-diagonal `bilinear-form` flipped firm c095, so this gram_reduce maturity narration may itself be
    stale, but it concerns a DIFFERENT verb (`gram_reduce`, not the matrix-weighted-norm residue this
    dispatch owns) and belongs to a gram_reduce-cohort land-clean. Flagged here for a follow-up OQ; NOT
    re-anchored in this pass (one-residue-cohort-per-dispatch).
- No abstractor reread needed: the firm `## Status` was authored coherently in the c091 cascade; only the
  three lagging narration tokens drifted. This is a pure rewrite, not authorship.

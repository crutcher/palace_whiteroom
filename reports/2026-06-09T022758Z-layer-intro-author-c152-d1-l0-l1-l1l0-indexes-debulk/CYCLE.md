---
agent: layer-intro-author
invoked_at: 2026-06-09T022758Z
scope: c152 D1 — de-bulk F-class (Working Notes) + E-class (date provenance) on L0/index.md, L1/index.md, L1-L0/index.md
status: integrated
integrated_at: 2026-06-09T025046Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (staging row D1). F/E-class de-bulk of 3 NO-FRONTMATTER-RANK indexes L0/L1/L1-L0 (## Working Notes stripped, ## Reference-note discipline + ## L1 vocabulary conventions LIFTED) + ksp-factory-file.md:62 backlink re-point. Baseline HELD EXACTLY; build EXIT 0; step-5b/5c/5d clean."
---

# CYCLE: c152 D1 — L0 / L1 / L1-L0 layer-index de-bulk

## Summary

Cycle-152 D/E/F de-bulk scale-out wave, dispatch D1. Applied `finalization-debulk` (incl. the
meta-150 `## Origin`/`## Working Notes`/`## Critic's role` adjudication + the directive-date E-class
rule) to the three NO-FRONTMATTER-RANK layer-index files. All edits applied directly on disk per the
de-bulk convention. **Graded-stack lint baseline HELD EXACTLY** (`files=392, typed=331, untyped=61,
rank_violations=0, unresolved_depends_on_targets=0, promotion_frontier=11, detritus=123,
true_detritus=51`). Build-graph untouched (no node/edge/rank/status/semantics move).

These are no-frontmatter-rank index files: the dep-map status tokens are the SOLE rank carriers. All
were preserved byte-exactly (the word-diffs confirm not one dep-map cell was touched).

## Per-file results

### `book/src/L0/index.md` — F-class
- **Stripped:** the `## Working Notes` section's process-workshop bullet ("Negative-result citations …
  get noted in `scaffolding/decisions/` rather than the lowering themes" — a process-channel pointer).
- **Lifted:** the two load-bearing static-discipline bullets (the reference-note cohort 2–4-paragraph
  discipline bound; the L1-`Context`-points-at-convention-chapter rule) + the evidence-pointer bullet,
  re-homed under a non-process heading **`## Reference-note discipline`**. Dropped the process-framing
  "should point at" → "point at".
- **Citations:** 2 → 2 (match). **Markdown links:** 30 → 30 (match).
- **Status tokens:** N/A (L0 is a reference-note index, no firm/rough-in dep-map table).
- **F-class sections remaining:** 0. **Date provenance:** 0.

### `book/src/L1/index.md` — F-class + E-class
- **E-class (date):** line 113 "the identity-in-named-terms smell the `2026-06-01` vocabulary-shift
  redirect warns against" → "the … smell the vocabulary-shift redirect warns against" (date dropped,
  concept named directly).
- **F-class (`## Working Notes`):** this section is almost entirely **load-bearing static
  structural/semantic discipline** (dep-map-records-L1-internal-deps-only; aliasing-first-class;
  MPI-single-rank-scope; constant-fold-transparent-vs-load-bearing; the MINRES/BiCGStab
  obstruction-rough-in fact; the `ksp_solve` first-structured-opaque-arg coupling + concept
  cross-links; the `ksp_solve` L1>L0 decomposition; the `eigsolve` partial-convergence semantic; the
  **three NO-L2-ENTRY warrants** — genuine spec). **KEPT all of it**, re-homed under a non-process
  heading **`## L1 vocabulary conventions`**. **Stripped only the process-framing clauses within
  bullets:**
  - "classified as transparent performance tricks and erased at L1 — but only after the critic
    confirms they are algebraically equivalent" → "are transparent performance tricks, erased at L1
    because they are algebraically equivalent" (critic-process clause out).
  - "Harvester should not attempt promotion until …" → "They are not promotable until …" (producer
    forward-process directive rephrased to static fact).
  - "(per the vocabulary-shift redirect §1d identity-in-named-terms smell …)" → "(the
    identity-in-named-terms smell …)" (redirect-§-process-framing trimmed; the concept stays).
- **Inbound-pointer re-anchor (coupling-lift-aware, the heading rename has 2 inbound prose pointers):**
  1. **In-file** dep-map cell (line 184) `**NO L2 entry by warrant — see Working Notes**` →
     `**… — see L1 vocabulary conventions**`.
  2. **`book/src/L0/ksp-factory-file.md:62`** `## Referenced from` backlink prose label
     `[`L1/index`](../L1/index.md) "Working Notes"` → `"L1 vocabulary conventions"` (the LINK target
     `../L1/index.md` has no fragment, so it stays live; only the stale prose label was updated).
- **Citations:** 136 → 136 (match). **Markdown links:** 254 → 254 (match).
- **Status tokens:** `` `firm` `` × 51 → 51 (match). Every dep-map cell rank-token byte-preserved.
- **F-class sections remaining:** 0. **Date provenance:** 0.

### `book/src/L1-L0/index.md` — F-class
- **Stripped:** the `## Working Notes` section (one bullet: "Themes here are the bridge to source
  citations; every theme entry carries `palace/<file>.cpp:<lines>` evidence"). This is a redundant
  restatement of the `## Context` section's citation-grounding point ("every theme entry carries
  … evidence" is already established there) — no unique load-bearing content, no coupling to lift, no
  citation in the bullet. Removed wholesale.
- **`## Context` UNTOUCHED** (not a target).
- **Citations:** 39 → 39 (match). **Markdown links:** 57 → 57 (match).
- **Status tokens:** all in dep-map table cells (`firm`/`obstruction`/`partly-constructive`),
  byte-preserved — word-diff shows the ONLY change is the `## Working Notes` removal.
- **F-class sections remaining:** 0. **Date provenance:** 0.

## Inbound-anchor check

`grep -rn '<file>#working-notes'` for all three target files → **0 fragment anchors** to any
`## Working Notes` section (matches the c151 pilot finding). Two NON-fragment prose-label pointers to
the L1 "Working Notes" heading were found and re-anchored (the in-file dep-map cell + the
`L0/ksp-factory-file.md` `## Referenced from` backlink); both links are fragment-less so they stay
live, only the prose labels were updated to the new `## L1 vocabulary conventions` heading.

## Lint baseline (HOLD)

```
files scanned:  392
typed nodes:    331
untyped:        61   (warning)
rank violations: 0
unresolved depends-on targets: 0
promotion frontier: 11
detritus: 123 (51 true-detritus / 72 reference-reachable §2g)
```
All metrics match the dispatched baseline EXACTLY. No node/edge/rank/status/semantics move.

## Supporting evidence
- `git diff --word-diff=porcelain` for each of the 3 files confirms changes are limited to: heading
  renames, process-framing-clause strips, the one date drop, the redundant-bullet removal, and the
  inbound-pointer re-anchors. No dep-map row, signature, citation, or cross-link altered.
- `python3 tools/graded-stack-lint/graded_stack_lint.py --book-src book/src` → RESULT: 0 rank
  violation(s), 123 detritus, 61 untyped — baseline held.

## Open questions / caveats
- The `book/src/L0/ksp-factory-file.md:62` backlink edit is a cross-file prose-label fix (outside the
  3 named target files) forced by the L1 heading rename. It is wiring (a stale prose label downstream
  of a renamed section), not constituent-content authoring — flagged here for transparency. If the
  integrator prefers the heading kept verbatim as `Working Notes` to avoid the cross-file touch, the
  alternative is to leave the heading and only strip the in-bullet process framing; the chosen rename
  is the meta-150-preferred "re-home to a non-process heading" disposition.

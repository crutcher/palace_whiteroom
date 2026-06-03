---
agent: lifter
invoked_at: 2026-06-03T14:40:59Z
scope: feature-surface hygiene micro-pass (active-head #8) — two disjoint cosmetic fixes
status: pending
inputs:
  - book/src/feature/driven.L4.md
  - book/src/feature/electrostatic.L1.md
  - book/src/L4/sparameter_reduce.md (on-disk target, 22733 bytes)
  - skills/upgrade-plain-text-ref-to-live-link-when-target-on-disk/SKILL.md
integrated_at: 2026-06-03T153000Z
integration_commit: d11bd2f
integration_notes: |
  cycle-076 (batch-24 position 1/3, LEAD). Applied clean as D2 by integrator-per-report;
  finalized + committed by integrator-finalize. LOW/hygiene micro-pass: ONE load-bearing edit
  (Fix #2) re-tokening the electrostatic.L1.md:65 in-prose self-qualifier seed-(exemplar) ->
  bare seed (frontmatter + Status-opening token already bare, untouched); DISCHARGES OQ
  feature-column-self-status-qualifier-drift-in-prose. Fix #1 (driven.L4.md plain-text ->
  live-link upgrade) NO-OP-BY-DESIGN -- the sparameter_reduce occurrences are code constructs /
  deliberate forward-ref notes; nothing applied to driven.L4.md; closes OQ
  sparameter-reduce-plain-text-to-live-link-upgrade (CLOSED-NO-OP-BY-DESIGN). Disjoint from
  D1's structural surface. cargo make book exit 0, linkcheck2 clean, zero build-repair.
---

# CYCLE: feature-surface hygiene micro-pass

## Summary
A LOW/hygiene micro-pass with two disjoint cosmetic fixes, disjoint from the D1 reorg.
**Fix #2 (the `electrostatic.L1.md:65` prose self-qualifier normalization) is a clean, applied
proposed-changes block** that re-tokens the in-prose `seed (exemplar)` self-qualifier to bare
`seed`, closing OQ `feature-column-self-status-qualifier-drift-in-prose`. **Fix #1 (the
`driven.L4.md` plain-text→live-link upgrade) is a no-op-by-design**: on reading the actual file,
all four `sparameter_reduce` occurrences are either inside a code construct (where a markdown link
does not render) or are deliberate authorship-locus notes (where the skill explicitly permits a
bare mention) — none is a genuine prose live-link candidate, so no edit is proposed for that file.
Per-line judgments documented below.

## Proposed changes

### Fix #2 — `electrostatic.L1.md` prose self-qualifier normalization (APPLIED)

The in-prose self-qualifier `` `seed (exemplar)` `` on line 65 is re-tokened to bare `` `seed` ``,
matching the batch-22-meta-codified uniform feature-column token (the prose names the sub-kind
separately; the qualifier does not belong in the token). This is a PROSE self-qualifier, NOT the
`## Status:` line token — the `## Status:` line already opens with bare `` `seed` `` (line 65 is
the *body* of the Status section, and the drifted qualifier is mid-sentence within it).

```edit:book/src/feature/electrostatic.L1.md
[old]: The entire stage-3 reduction therefore rests on rough-in L1 primitives — consistent with the column being a `seed (exemplar)`, not a firm composition.
[new]: The entire stage-3 reduction therefore rests on rough-in L1 primitives — consistent with the column being a `seed`, not a firm composition.
```

### Fix #1 — `driven.L4.md` plain-text → live-link upgrade (NO-OP BY DESIGN)

No proposed-changes block. Per-line judgment for each of the four `sparameter_reduce` occurrences
(line numbers verified on-disk via `grep -n`; the scope's stated 55/98/140/157 match exactly):

- **Line 55** — `` in  sparameter_reduce es (ports cfg) `` — inside the 4-space-indented
  Haskell-style composition code block (lines 45–55 are all 4-space-indented). Markdown links do
  NOT render inside indented code blocks, and the L4 strawman convention
  (`book/src/design/l4_calculus.md`) is bare pseudo-language inside the fence. A live link here
  would render as raw `[...](...)` markup. **Keep bare** (not a live-link candidate).
- **Line 98** — `` `sparameter_reduce` is NOT authored in this chapter, mirroring how the … `` —
  prose, but a deliberate authorship-locus note. Per skill
  `upgrade-plain-text-ref-to-live-link-when-target-on-disk`, a structural note about
  authorship-locus may legitimately stay a bare-code mention even when the slug is on disk.
  **Keep bare** (the slug being on disk is technically link-valid, but the sentence's job is to say
  the construct is NOT authored here — a live link would invite the reader to expect this chapter's
  authored home).
- **Line 140** — `` `driven = sparameter_reduce ∘ frequency_sweep ∘ fe_assemble(×3)` `` — inside an
  inline-code span (backtick-delimited). Markdown links do NOT render inside inline-code spans; the
  whole expression is one code span (a composition formula). **Keep bare** (not a live-link
  candidate).
- **Line 157** — `` | … | `sparameter_reduce` *(output-product column; not authored here)* | forward-ref | … | `` —
  table cell, deliberate authorship-locus note with explicit `forward-ref` status. **Keep bare**
  (consistent with the `forward-ref` status in the same row; the parenthetical already states "not
  authored here").

NOTE confirmed: the `sparameters.{L4,L1,L0}.md` chapter cross-references are ALREADY live links and
are a different construct (prose chapter pointers, not `sparameter_reduce` combinator mentions) —
no work there, as instructed.

## Discipline notes
- Cosmetic/hygiene only. Touched only `electrostatic.L1.md` line 65 prose (Fix #2). No edit to
  `driven.L4.md` (Fix #1 no-op-by-design). Did NOT touch SUMMARY.md, feature/index.md, or any
  group-intro page (D1 owns those).
- Fix #2 is a PROSE self-qualifier re-token, not a `## Status:` token change (that line already
  reads bare `seed`). Aligns the body prose with the batch-22-meta uniform-token convention
  (CLAUDE.md §FEATURE-SURFACE SPINE "Two sub-kinds": "Both use the uniform `status: seed` token (no
  `(exemplar)` / `(composition-root)` qualifier — the prose names the sub-kind)").
- Fix #1 is recorded as a structural-rewrite judgment, not authorship: the skill is applied
  per-line and the conclusion is that no occurrence is a genuine prose live-link site (3 are inside
  code constructs where links don't render; 1 is a deliberate authorship-locus note already
  carrying `forward-ref` status). This is the skill's "apply judgment per line" guidance landing on
  keep-bare for all four — not a missed upgrade.

## Supporting evidence
- `book/src/feature/electrostatic.L1.md:65` — the prose self-qualifier (Fix #2 target), read this
  dispatch.
- `book/src/feature/driven.L4.md:55,98,140,157` — the four `sparameter_reduce` occurrences (Fix #1
  candidates), all read + classified this dispatch via `grep -n` + full-file read.
- `book/src/L4/sparameter_reduce.md` — on-disk (22733 bytes per scope), the would-be link target.
- CLAUDE.md §Extraction-goal "Two sub-kinds" bullet — the uniform `status: seed` token codification
  (batch-22 meta-phase).

## Open questions / caveats
- **Closes OQ `feature-column-self-status-qualifier-drift-in-prose`** (Fix #2 applied). If other
  feature-column chapters carry the same drifted `seed (exemplar)` / `seed (composition-root)` prose
  self-qualifier mid-body, they would need the same one-line re-token — out of this dispatch's
  single-file scope; flag for a future sweep if a same-layer-cross-cutter finds more. (This pass
  checked only the two files in scope.)
- **Closes the `sparameter-reduce-plain-text-to-live-link-upgrade` hygiene item** as no-op-by-design:
  the upgrade is not applicable because no `driven.L4.md` `sparameter_reduce` occurrence is a
  renderable prose link site. The hygiene item can be marked done (nothing to upgrade), not deferred.
- No citation re-anchors were emitted (no `path:lo-hi` pinpoint changes in either fix), so no
  citecheck `--anchor` self-verification was required; the only edit is a one-token prose change
  with no line-range citation attached.

---
agent: layer-intro-author
invoked_at: 2026-06-09T030411Z
scope: c153 D/E/F de-bulk CLOSER — variant-absorption (last D-class residual) + black-box-vs-accelerated-kernels (E-class)
status: pending
integrated_at: 2026-06-09T031600Z
integration_commit: 90f53b751945f76ee41273e415eaed0d248cf34b
integration_notes: "Applied clean (staging row C3). De-bulked concepts/variant-absorption.md (F+E+D — the D-class D→0, last D-class file; EXTENDED ## Context de-bulk per parent adjudication; LIFTED ## Relationship to rotation) + black-box-vs-accelerated-kernels.md (E). OQ variant-absorption-context-carries-process-tags-vs-do-not-touch-context-carve-out RESOLVED in-cycle. Build EXIT 0; graded-stack baseline HELD EXACTLY; step-5b/5c/5d clean. Part of cycle-153 batch-50 CLOSER — D/E/F campaign COMPLETE, A–F scan clean."
---

# CYCLE: c153-C3 de-bulk — variant-absorption + black-box-vs-accelerated-kernels

## Summary

Applied `finalization-debulk` + the c151/c152 PILOT pattern (exemplar `concepts/rotation.md`)
to the two assigned concept pages. Edits made directly to `book/src/` (this is a
finalization de-bulk dispatch with direct-edit authority per the c153 closer plan, mirroring
the critic-verified c151/c152 pattern). Lint baseline HELD EXACTLY. No node/edge/rank/status
move; no citation or `[link]` dropped except one process-machinery skill pointer.

**Parent adjudication applied in-cycle:** `variant-absorption.md`'s `## Context` was extended
into the de-bulk (slice-era concept-page Context IS a target, per the c151 `rotation.md` pilot),
driving the file to 0 D-class cycle-tags + 0 E-class dates. The OQ
`variant-absorption-context-carries-process-tags-vs-do-not-touch-context-carve-out` is RESOLVED.

## Per-file results

### `book/src/concepts/variant-absorption.md` — D + F + E

**Sections stripped wholesale (F-class):**
- `## Critic's role` (process machinery: `prompts/critic.md` check #9, `revise`/`kind:` verdict routing).
- `## Origin` (pure provenance: "Codified during 2026-05-24 meta-review #2 … `lessons.md` … `episodic.jsonl`").
- `## Working Notes` (3 bullets; one was a load-bearing coupling fact — LIFTED, see below).

The D-class inline cycle-tags vanished with these F-blocks as expected.

**COUPLING-LIFT (rotation relationship):** the `## Working Notes` bullet
*"This concept's relationship to `rotation.md`: variant absorption is necessary for criterion (1)
state hiding …"* + the adjacent boundary-fuzziness fact ("orthogonal variant vs fundamentally
different algorithm … FGMRES is parametrically absorbable … LOBPCG vs Arnoldi is not") were
LIFTED into a new **`## Relationship to rotation`** section (now at line 111, placed where the
old Working Notes had threaded the coupling). The friction-driven-unification meta-observation
bullet (process narrative, no static fact) was dropped.

**E-class dates / inline cycle-tags cleaned in conceptual sections (NOT Context):**
- `## Levels of absorption`: dropped the parenthetical "(Added 2026-05-24 meta-review #3, in
  response to cycles 7+9 friction …)" — pure provenance, no static fact.
- "(a) Invariant-level": "original `variant-absorption.md` test" → "the test (above)".
- "(b) Procedural": "Cycle 9's GMRES (…)" → "GMRES with a `W ∈ {V, Z}` selector …" (kept the
  worked counter-example, dropped the cycle tag).
- "(c) Primitive-sequence": "Cycle 7's GMRES (…)" → "GMRES, where right-fixed-`M` …" (kept the
  worked counter-example); "**Note (added 2026-05-24 meta-review #5):**" → "**Note:**".
- `## Structurally-distinct variants …`: dropped the parenthetical "(Added 2026-05-25
  meta-review #11 after cycle 40 …)" — pure provenance.
- Stale-pointer / process-machinery fixes (broken/obsolete refs):
  - "fails Critic check #9" → "is a silent partial absorption — the failure mode this concept
    exists to catch" (the `Critic check #9` machinery reference is gone).
  - "(per `book/src/spec/index.md` slice-acceptance criterion #1)" → removed the dead pointer
    (the Phase-1 corpus `book/src/spec/` was deleted; this was a broken link).
  - "The Synthesizer applies the [`classify-variant-axis`](../../../skills/…/SKILL.md) skill" →
    removed (process machinery; the only removed `[link]` — a skill pointer OUTSIDE `book/src/`,
    not a citation).
  - `## Anti-pattern`: "Critic check #9 flags this." → dropped the trailing machinery clause.

**Context de-bulk — ADJUDICATED + APPLIED (parent ruling, in-cycle):** the OQ flag below was
adjudicated by the parent: for slice-era CONCEPT pages (this is a "peer concept to
`rotation.md`"), the `## Context` section IS a de-bulk target — exactly as the c151 PILOT folded
`rotation.md`'s `## Context` (definition kept, process narrative stripped). The "DO NOT touch
`## Context`" carve-out targets the 121 per-OPERATOR *orientation* Context sections, NOT
slice-era concept-page process-narrative Context. So the Context was de-bulked, mirroring the
rotation.md pilot:

- **KEPT (load-bearing orientation):** the first paragraph — "A peer concept to `rotation.md`.
  **Variant absorption** is the principle that when a slice has orthogonal axes of algorithmic
  variation … the L1 form must absorb those variants **parametrically** rather than appending
  them as separate paragraphs." AND the closing classification "This concept is **methodology**,
  not a tensor primitive (same kind as `rotation.md`)." The `## Context` heading itself is KEPT.
- **STRIPPED (slice-era process narrative):** the "This concept was extracted during the
  2026-05-24 meta-review #2 (cycles 4–6 enactment) …" sentence + the two
  `- **Cycle 5** …` / `- **Cycle 6** …` back-push bullets + the "The Critic correctly applied
  check #8 … its own check (#9 in `prompts/critic.md`)" paragraph.
- **LIFTED (technical insight judgment):** the Cycle 6 bullet's FGMRES update-basis insight
  (`x_m = x_0 + W_m y_m` with `W_m = V_m` for GMRES, `W_m = Z_m` for FGMRES, `A W_m = V_{m+1} H̄_m`)
  is NOT lost — it is already stated as a static worked example in the concept body
  (`## The parametric-vs-appended test` → "(A) Parametric absorption", and `## Levels of
  absorption` → "(a) Invariant-level"). No separate lift needed; the process bullet was
  redundant with the kept conceptual prose, so it was stripped, not lifted.

**Net: the file is now literally 0 D-class cycle-tags / 0 E-class dates / 0 `prompts/critic`
references.** The conceptual body (Levels (a)/(b)/(c), parametric-vs-appended test, the test,
partial-absorption disclosure, routes-to-full-absorption, structurally-distinct-variants,
resolution paths, Relationship-to-rotation) is fully intact.

- **0 F-sections:** CONFIRMED (`grep '^## (Critic.s role|Origin|Working Notes)$'` → 0).
- **0 D-class cycle-tags / E-class dates / prompts-critic refs (whole file, incl. Context):**
  CONFIRMED — `grep -cE 'cycle-[0-9]|c0[0-9][0-9]|batch-[0-9]|2026-0[0-9]-[0-9]|prompts/critic'`
  → **0**.
- **Citations / links before→after:** 5 `[...](...)` links → 4 (the −1 is the
  `classify-variant-axis` skill pointer, process machinery, not a citation).
  `constructed-operators` cross-refs ×6 preserved, `krylov_step` ×3 preserved, `rotation.md`
  preserved. No source citation (`path:lo-hi`) existed in this methodology page; none lost.
- **Inbound-anchor check:** `grep -rE '#critic-s-role|#origin|#working-notes'` and
  `variant-absorption.md#…` across `book/src/` → 0 inbound anchors to the stripped sections.
  No re-point needed.

### `book/src/concepts/black-box-vs-accelerated-kernels.md` — E

- **E-class:** the single `2026-06-01` directive-date in *"the 2026-06-01 blanket leaf-collapse
  that applied it was an over-correction"* → date dropped, the static fact kept ("the blanket
  leaf-collapse that applied it was an over-correction"). No other dates/cycle-tags present.
- No F-class sections present; nothing stripped.
- **Citations / links before→after:** 25 `[...](...)` links → 25 (all preserved). The 14-edge
  `reference:` frontmatter block intact.
- **Inbound-anchor check:** no `black-box-vs-accelerated-kernels.md#…` anchored inbound links;
  bare-file inbound links (SUMMARY, L3/index, concepts/index, several L4 chapters) untouched —
  no slug/anchor rename.

## Safety / baseline

- **No `rank:` / `## Status` / `status:` in either file** (concept pages; CONFIRMED grep → none).
  No node/edge/rank/status at risk.
- **Lint baseline HELD EXACTLY** (before == after):
  `files=392, typed=331, untyped=61, rank_violations=0, unresolved_depends_on_targets=0,
  promotion_frontier=11, detritus=123, true_detritus=51`.
- No frontmatter `edges:` block modified in either file.

## Open questions / caveats

- `variant-absorption-context-carries-process-tags-vs-do-not-touch-context-carve-out`:
  **RESOLVED in-cycle.** The parent adjudicated: slice-era CONCEPT-page `## Context` (a "peer
  concept to `rotation.md`") IS a de-bulk target — the "DO NOT touch `## Context`" rule targets
  the 121 per-OPERATOR *orientation* Context sections, not slice-era concept-page
  process-narrative Context. The Context was de-bulked mirroring the c151 `rotation.md` pilot
  (orientation definition + methodology classification KEPT; extraction-narrative / Cycle-5/6
  back-push bullets / `prompts/critic.md` paragraph STRIPPED; FGMRES `W_m` insight already
  covered in the concept body, so stripped-not-lifted). Final residue grep = **0**; lint
  baseline HELD EXACTLY. No remaining open questions for this file.

---
name: phase-1-slice-reduction-audit
description: Audit a Phase 1 corpus slice (`book/src/spec/slices/<slice>.md`) for redundancy against firm layered-artifact entries and propose its reduction (stub-and-pointer) or removal. Codifies the four-part template (Section-anchor table / Supersession map / Residual gaps / Proposed changes) established cycle-010 and the START+END boundary-verification + unique-text-anchor refinement that the recurrence-3 line-map defects (cycles 010/011/012) made necessary. Audience: `same-layer-cross-cutter`.
status: active
---

# phase-1-slice-reduction-audit

`book/src/spec/slices/` is the Phase 1 slice corpus (cycles 1–172, pre-structural-redirect). Per the CLAUDE.md §Methodology invariant **Phase 1 corpus reduces as material is lifted**, a slice whose content is fully represented in firm layered entries (L0/L1/L2/L3/L4 + lowering layers) is **reduced** to a stub pointing at the firm entries it has been absorbed into, and eventually removed. This skill is the audit procedure that produces the reduction proposal.

The skill exists because the audit kept producing line-map defects: the cited line ranges drift from the actual section boundaries, and "full reduction" edits orphan content when a sub-slice's START boundary is mis-identified. The procedure below makes the boundary verification mechanical.

## When to invoke

- A `same-layer-cross-cutter`-scoped dispatch targets one or a small batch (2–4) of `book/src/spec/slices/<slice>.md` entries.
- The slice's subject matter overlaps firm layered entries (the lifted forms are stable enough to support reduction).

## Procedure

1. **Enumerate section anchors FIRST — verify BOTH ends.** Run `grep -n "^## " <slice>` AND `grep -n "^# " <slice>` (H1 too — multi-section slices carry intra-slice H1 sub-slices, e.g. a `# Orthogonalization (plane-rotation stream)` H1 mid-file). Emit the result as a fixed **section-anchor table** at the top of the dispatch report: one row per heading, with `heading text | start line | (end line = next heading's start − 1, or EOF)`. **Do NOT grep against a window you *expect* the content to be in** (e.g. `grep "## " | tail`) — that catches the END boundary but misses the START. The cycle-012 HIGH-severity defect was exactly this: a sub-slice scoped as "311-376" when it began at line 225, orphaning ~86 lines.

2. **Build the supersession map — one row per section.** For each section in the anchor table, populate four columns:
   - section name
   - actual line range (from step 1, both ends verified)
   - supersession status: `full` (content fully lives in firm entries) / `partial` (some content lifted, some residual) / `none` (not yet lifted, or load-bearing-and-unliftable)
   - firm-entry pointer(s): the `book/src/L<n>/<slug>.md` (or lowering-theme) anchors that now carry the content.

3. **Residual gaps section.** Enumerate ONLY the `partial` / `none` rows. For each, state precisely what content has NOT been lifted and whether it blocks reduction (a `none` row that is load-bearing — e.g. a negative-result distinction catalog — means the slice cannot be fully reduced; propose partial reduction retaining that section verbatim).

4. **Derive proposed_change line ranges mechanically from the anchor table — not from prose.** A reduction edit's ranges come from step-1's verified anchors, never from the narrative. For a `full reduction` (stub-and-pointer replacing a section or whole slice), the edit's START anchor MUST sit at the section's TRUE first heading (the H1 or `## Context` that introduces it), and the END anchor at the section's last line. For a sub-slice that is a `## Context` + intra-slice H1 + several H2s, the reduction spans from the `## Context` (or the H1) through the last H2 — not from the middle.

5. **Reconciliation step (mandatory before emission).** Re-verify that every `full reduction` edit's START anchor is the section's first heading and END anchor is its last line, and that the narrative's "reduce sections X–Y" matches the proposed_change ranges. **Confirm START-anchor uniqueness with `grep -c`** — for a multi-section sub-slice, prefer a unique-text START anchor (a one-of-a-kind H1 or first `## Context` line) over a line number, and confirm `grep -c "<anchor text>" <slice>` returns 1. If it returns >1, expand the anchor until unique.

6. **Intra-corpus redundancy.** If two slices (or a slice and a sub-slice) describe the SAME algorithm (cycle-012 found `plane_rotation_stream` + the orthog plane-rotation sub-slice are identical), call it out: propose elimination of the duplicate, hoisting any unique invariant into the surviving canonical slice FIRST (sequence the hoist before the elimination so no content is lost).

## Failure modes

- **END-verified, START-not-verified (the recurrence-3 defect).** `grep` run against a tail window catches the section's end but not its head; the reduction edit then orphans the head content beneath a stub. Recovery: ALWAYS grep the whole file for `^#` and `^##`; never window the enumeration.
- **Line-number START anchor on a multi-section sub-slice.** Line numbers drift as upstream sections are edited; a `full reduction` edit anchored on a line number can land mid-section. Recovery: use a unique-text START anchor (H1 / first `## Context` line), `grep -c`-confirmed unique.
- **Narrative/range disagreement.** The prose says "stub section X" but the proposed_change range retains part of X (cycle-010 cg.md). Recovery: the step-5 reconciliation; derive ranges from the anchor table, then check the narrative against them.
- **Reducing a load-bearing `none` section.** A negative-result / load-bearing-distinction section is the artifact, not redundant material; reducing it loses signal. Recovery: classify it `none` in step 2 and retain it verbatim (cycle-011 `polynomial_recurrence_step.md` precedent: "the slice IS the artifact").

## Discipline

- **Verify both boundaries of every section.** START and END. The skill exists because END-only verification caused a HIGH-severity defect.
- **Unique-text anchors over line numbers** for any `full reduction` START anchor; `grep -c`-confirm uniqueness.
- **Ranges derive from the anchor table, never from prose.**
- **Reconcile before emission** — narrative and proposed_change ranges must agree.
- **Sequence hoist-before-eliminate** for intra-corpus redundancy so no unique content is lost.
- **Reduction is monotonic** — the corpus shrinks as the layered surface becomes authoritative; the git history is the historical record (do not preserve slice form "just in case").

## Worked examples

- **Cycle-010 (first instance, cg-chain slices).** Established the four-part template; critic surfaced citation drift + narrative/range disagreement (cg.md section the narrative said to stub but the range retained).
- **Cycle-011 (batch-2).** `orthog.md` / `chebyshev.md` partial reductions + `polynomial_recurrence_step.md` first negative-result slice (`none`, retained verbatim — "the slice IS the artifact"). Ran the `grep -n "^## "` mitigation but still produced ~10 minor off-by-ones (recurrence-2).
- **Cycle-012 (batch-3, HIGH-severity defect that motivated the START-boundary refinement).** The orthog plane-rotation sub-slice scoped as "lines 311-376" (the §Open-questions + the SECOND of two near-duplicate L1 entries) when it begins at line 225 (`## Context` introducing the `# Orthogonalization (plane-rotation stream)` H1) and spans 225-376. The "full reduction" as written would have orphaned ~86 lines. The dispatch DID `grep` — but against a mis-scoped "lines 300+" window, catching the tail not the head. Repaired pre-apply to the full text-anchored 225-376 span. First intra-corpus-redundancy verdict (`plane_rotation_stream` + orthog sub-slice are the same algorithm).

## Cross-references

- CLAUDE.md §Methodology invariants "Phase 1 corpus reduces as material is lifted".
- Friction-ledger `phase-1-corpus-reduction-policy` (cycle-009 meta-phase codification).
- Skill-candidates `phase-1-slice-reduction-audit` (proposed cycle-010, recurrence-3 cycle-012, promoted cycle-012 meta-phase).
- Priority #19 `phase-1-corpus-reduction-audit`.
- Related skill `verify-citation-range` (the per-citation boundary check; this skill is the per-slice section-boundary analog).

## Provenance

- Promoted: cycle-012 meta-phase (batch-2 closure, 2026-05-28).
- Pattern observed: cycle-010 (first instance), cycle-011 (recurrence-2), cycle-012 (recurrence-3 + HIGH-severity START-boundary defect).
- Promotion bar: pattern observed ≥2 cycles (recurrence-3) AND sketch concrete enough to write as SKILL.md AND friction-ledger / skill-candidate entry exists. All three met.

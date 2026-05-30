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

7. **Canonical-instance check — second necessary axis beyond firm-layered-home (added cycle-033 meta-phase).** Before recommending reduction-to-stub or removal, run a **concept-page grep** for the slice's filename + slug:
   ```
   grep -rn "spec/slices/<slice-stem>\|<slice-slug>" book/src/concepts/
   ```
   Triage each hit:
   - **Named §Canonical-instance / "instance of" referent** — the slice is the named canonical-witness instance for a concept page (e.g. `polynomial_recurrence_step` is the canonical instance for the chebyshev polynomial-recurrence concept; `sparse_triangular_solve` is the canonical instance for 3 concept pages). Count these.
   - **Cross-reference / "see also" mention** — a one-line "see `spec/slices/<slice>.md`" reference that COULD be re-anchored to a firm L_n entry. Not a canonical-instance binding.
   - **False positive** — the stem matches an unrelated firm entry (e.g. `chebyshev` matches `L1/chebyshev-smoother.md`). Skip.

   If the **named-canonical-instance count is ≥2** AND the slice carries unique L0 navigation (file:lines anchors) not covered elsewhere in the firm artifact, the audit verdict shifts to **DEFER-by-canonical-instance** — recommend `annotated-and-retained` (status `annotated-and-retained` in the slice frontmatter; cross-link to each canonical-binding concept page in the slice's intro; add the partner firm-layered-entry pointer if any). Do NOT recommend reduction-to-stub or removal regardless of firm-layered-home presence; the canonical-instance bindings would strand. Single canonical-instance reference is recoverable by re-anchoring the concept page; the ≥2 bar reflects that re-anchoring two-or-more concept pages is more expensive than retaining the slice.

   CLAUDE.md §Methodology invariants "Phase 1 corpus reduces as material is lifted" §canonical-instance carve-out + friction-ledger `negative-result-slice-canonical-instance-blocks-reduction`.

## Removal sub-case: non-link prose-reference grep (added cycle-015 meta-phase)

A slice **REDUCTION** (compact to a stub) leaves the file in place, so inbound references — markdown links AND prose mentions — still resolve to a (thinner) file; the mdBook build linkcheck (`cargo make book` exit 0) is a sufficient backstop. A slice **REMOVAL** (`git rm`) deletes the file, so EVERY inbound reference must be re-pointed or struck — and **the build linkcheck only catches the markdown-link subset.** A bare-path or inline-code prose mention (e.g. `` `spec/slices/<slice>.md` `` in prose, or a plain-text path in a narrative sentence) is NOT a markdown link, so the build passes while the reference is stranded pointing at a deleted file.

Cycle-015's chebyshev slice removal FAILED `cross-reference-integrity` critique because exactly this happened: the "complete whole-tree grep" matched markdown links but missed **4 non-link prose references**. The build was clean; the critic's independent grep caught them.

**Before proposing any `git rm` of a slice, run a non-link reference grep (NOT just a markdown-link check):**

1. **Grep the whole book tree + scaffolding for the slice STEM in ALL reference shapes**, not just the `[text](path)` link form:
   ```
   grep -rn "<slice-stem>" book/src/ scaffolding/
   ```
   where `<slice-stem>` is the bare filename (e.g. `chebyshev` for `spec/slices/chebyshev.md`) or the path fragment (`spec/slices/chebyshev`). Use the stem, not the full markdown-link regex — the stem catches links, inline-code, and bare-path prose mentions in one pass.
2. **Triage each hit** into: (a) markdown link `](...<slice>)` — re-point or strike; (b) inline-code `` `...<slice>...` `` — re-point or strike; (c) bare-path prose mention — rewrite the prose to point at the firm layered entry that absorbed the content, or strike if obsolete; (d) false positive (the stem also names a firm entry, e.g. `L1/chebyshev-smoother.md` — leave alone).
3. **Enumerate every (a)/(b)/(c) hit in the removal proposal** with its re-point/strike action, so the integrator-per-report applies them in the same proposed-changes batch as the `git rm`.
4. **State explicitly that the build linkcheck is the markdown-link backstop ONLY** and is insufficient on its own for a removal — the non-link grep is what closes the gap between "no broken markdown link" and "no stranded prose reference."

This sub-case applies to REMOVALS only. Reductions skip it (the file survives). Friction-ledger `slice-removal-non-link-prose-reference-grep-gap`.

## Failure modes

- **END-verified, START-not-verified (the recurrence-3 defect).** `grep` run against a tail window catches the section's end but not its head; the reduction edit then orphans the head content beneath a stub. Recovery: ALWAYS grep the whole file for `^#` and `^##`; never window the enumeration.
- **Line-number START anchor on a multi-section sub-slice.** Line numbers drift as upstream sections are edited; a `full reduction` edit anchored on a line number can land mid-section. Recovery: use a unique-text START anchor (H1 / first `## Context` line), `grep -c`-confirmed unique.
- **Narrative/range disagreement.** The prose says "stub section X" but the proposed_change range retains part of X (cycle-010 cg.md). Recovery: the step-5 reconciliation; derive ranges from the anchor table, then check the narrative against them.
- **Reducing a load-bearing `none` section.** A negative-result / load-bearing-distinction section is the artifact, not redundant material; reducing it loses signal. Recovery: classify it `none` in step 2 and retain it verbatim (cycle-011 `polynomial_recurrence_step.md` precedent: "the slice IS the artifact").
- **REMOVAL strands a non-link prose reference (cycle-015 defect).** A `git rm` of a slice leaves bare-path / inline-code prose mentions pointing at the deleted file; the build linkcheck passes (it only checks markdown links) but the references are stranded. Recovery: run the non-link reference grep (`grep -rn "<slice-stem>" book/src/ scaffolding/`) BEFORE proposing the removal, triage link vs inline-code vs prose, re-point/strike each in the same proposed-changes batch. The build linkcheck is the markdown-link backstop only.

## Discipline

- **Verify both boundaries of every section.** START and END. The skill exists because END-only verification caused a HIGH-severity defect.
- **Unique-text anchors over line numbers** for any `full reduction` START anchor; `grep -c`-confirm uniqueness.
- **Ranges derive from the anchor table, never from prose.**
- **Reconcile before emission** — narrative and proposed_change ranges must agree.
- **Sequence hoist-before-eliminate** for intra-corpus redundancy so no unique content is lost.
- **Reduction is monotonic** — the corpus shrinks as the layered surface becomes authoritative; the git history is the historical record (do not preserve slice form "just in case").
- **REMOVALS require the non-link reference grep** (cycle-015) — before any `git rm`, grep the whole tree for the slice STEM in all reference shapes (link + inline-code + bare-path prose), not just markdown links; the build linkcheck catches only the link subset. Reductions skip this (the file survives).
- **Canonical-instance check before reduction** (cycle-033) — a slice that is the named §Canonical-instance referent of **≥2 concept pages** AND carries unique L0 navigation is **retained-by-design** (status `annotated-and-retained`) even when its firm layered home exists. The firm-layered-home check is necessary but not sufficient; the concept-page-grep is the second axis. Precedents: `polynomial_recurrence_step` (c013), `sparse_triangular_solve` (c031). Friction-ledger `negative-result-slice-canonical-instance-blocks-reduction`.

## Worked examples

- **Cycle-010 (first instance, cg-chain slices).** Established the four-part template; critic surfaced citation drift + narrative/range disagreement (cg.md section the narrative said to stub but the range retained).
- **Cycle-011 (batch-2).** `orthog.md` / `chebyshev.md` partial reductions + `polynomial_recurrence_step.md` first negative-result slice (`none`, retained verbatim — "the slice IS the artifact"). Ran the `grep -n "^## "` mitigation but still produced ~10 minor off-by-ones (recurrence-2).
- **Cycle-012 (batch-3, HIGH-severity defect that motivated the START-boundary refinement).** The orthog plane-rotation sub-slice scoped as "lines 311-376" (the §Open-questions + the SECOND of two near-duplicate L1 entries) when it begins at line 225 (`## Context` introducing the `# Orthogonalization (plane-rotation stream)` H1) and spans 225-376. The "full reduction" as written would have orphaned ~86 lines. The dispatch DID `grep` — but against a mis-scoped "lines 300+" window, catching the tail not the head. Repaired pre-apply to the full text-anchored 225-376 span. First intra-corpus-redundancy verdict (`plane_rotation_stream` + orthog sub-slice are the same algorithm).
- **Cycle-031 (canonical-instance carve-out precedent).** `sparse_triangular_solve` slice-reduction audit. The firm-layered-home check passed (c029 `triangular-solve-obstruction` L1>L0 theme on disk). The auditor surfaced the second axis independently: the slice is the named §Canonical-instance for **3 concept pages**. Verdict: DEFER (retain in full, `annotated-and-retained`). Phase-1 removals stay 9/10. The auditor's §Open-questions item routed the codification ask to the meta-phase, which enacted (a) CLAUDE.md amendment, (b) this skill's step 7, (c) friction-ledger `negative-result-slice-canonical-instance-blocks-reduction`.

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

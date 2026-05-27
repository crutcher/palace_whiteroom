---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T18:21:16Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: pass
repaired_at: 2026-05-27T18:30:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of L4 intro refresh (cycle-008 wave-2 polish)

## Critique

### Checks run

**citation-validity (pass).** Every load-bearing claim in the prose carries a pointer. Strawman §1 (grammar), §3.7 (`iterate_while` small-step), §3.8 (demand pruning) all exist at the cited locations (`book/src/design/l4_calculus.md` lines 22, 150, 186). Palace source citation `reference/palace/palace/linalg/iterative.cpp:427` lands at the PCG main loop's `for (; it < max_it && !converged; it++)` (verified by reading lines 420-445); `:434-441` lands at the `if (!it) { p = z; } else { linalg::AXPBY(...); }` first-iteration branch — both pointers anchor the claimed shapes correctly. L1 precedent citation `book/src/L1/index.md:27-47` lands at the Vocabulary cohort subsection. CLAUDE.md invariants cited inline (L4 strawman in-management, L4/L3 pseudo-language) match the source verbatim.

**surface-or-evidence (pass).** Refresh of a layer intro is firmly in the surface-modification class (rewrite of `book/src/L4/index.md` Semantics + Vocabulary cohort + dep-map). No new operators are introduced; no new algebraic claims are made. The new prose summarises four existing semantic motifs (state-stratification, Solve-monad, value-threaded combinators with demand pruning, variant absorption via OpParams readonly) drawn from the three firm operator entries plus the firm L4>L3 theme. Each motif is anchored on an existing concept page link. The dispatch is appropriately scoped as polish/restructuring without new substantive rotations.

**rotation-quality (pass).** Not applicable in the rotation-introduction sense — this dispatch does not assert a new algebraic/structural rotation between layers. It documents and consolidates existing rotations into the layer's vocabulary. The Form-A vs Form-B "presentation rotation per first-iteration-unrolling" claim is a reference back to the cycle-006 cross-layer-cross-cutter recommendation, not a new claim.

**variant-axis-coverage (pass).** The Vocabulary cohort and dep-map enumerate the three firm L4 operators plus the two L4>L3 themes (firm + rough-in). Form-A vs Form-B distinction is preserved in the krylov-step signature; the with-prev `β = ()` degeneration is preserved with explicit Law 1 callout. No hidden variant branches.

**cross-reference-integrity (warning).** All file references resolve: `../design/l4_calculus.md`, `../concepts/state-stratification.md`, `../concepts/solve-monad.md`, `../concepts/derived-view-hoisting.md`, `../concepts/variant-absorption.md`, `../concepts/first-iteration-unrolling.md`, `./krylov-step.md`, `./iterate-while.md`, `./iterate-while-with-prev.md`, `../L4-L3/krylov-step-typed-wrapper-dissolution.md`, `../L4-L3/gmres-inner-loop-iterate-while-migration.md`, `../L2/krylov-step.md` — all verified to exist. Open-question slugs `iterate-while-l3-rendering-trajectory-accumulation-gap`, `iterate-while-l4-anchor-missing`, `l4-layer-intro-refresh-unblocked-by-first-firm-row` all resolve in `scaffolding/open-questions.md`. Section anchor reference `§"What the L3 form for iterate_while looks like"` in the new dep-map cell resolves to `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:158` (the section title there is `### What the L3 form for \`iterate_while\` looks like` — backticked; the dep-map cell renders without backticks, which is cosmetic and would not break mdbook). One mild concern: the new `Lowers to` cell for the `iterate-while` row points at the dissolution theme's internal section heading via prose ("§\"What the L3 form for iterate_while looks like\"") rather than a fragment-anchor markdown link; the prose pointer is correct but not click-followable from the rendered dep-map.

**edge-label-fidelity (pass).** The new `Lowers to` column carries L4>L3 (and onward L3>L2) cross-layer edges; the prose in each cell describes that exact edge. The krylov-step row cites both the L4>L3 theme (`krylov-step-typed-wrapper-dissolution`) and the L3>L2 hop (identity-in-form per cycle-002). The iterate-while rows cite the dissolution theme's nested L3 rendering plus the rough-in GMRES migration. Labels and prose align.

**plan-kind-consistency (warning).** Declared kind is "intro refresh" (polish/restructuring); content matches that shape on the Semantics-overlay and dep-map edits. However, two sub-issues:

1. The role spec at `.claude/agents/layer-intro-author.md:103` says **"Skip the subsection when the layer has only firm entries (no queue) or only rough-ins (no firm cohort) — the split is only useful when both states coexist."** All three L4 operators are firm; there is no rough-in/obstruction L4 operator. The dispatch keeps the Vocabulary cohort with three subsections (`Firm at L4`, `L4>L3 lowering themes`, `Queued at L4 — none currently`). Caveat 2 acknowledges this tension and defers to integrator preference. Per strict reading of the role spec the subsection is skip-eligible; per the spirit of the spec, the dispatch's adaptation (using the middle slot for L4>L3 themes rather than rough-in L4 operators) is a substantive structural choice that the role spec does not anticipate. The middle subsection `**L4>L3 lowering themes**` diverges from the L1 precedent (which uses the middle slot for rough-in obstruction operators at the *same layer*, not cross-layer themes). The divergence may be defensible — L4 has no rough-in operators, only firm + cross-layer themes — but it is a template-shape decision not flagged in the caveats. (Caveat 2 only discusses the empty `Queued` section, not the new middle section.)

2. The "Format expected" template after the dep-map (lines 91-96 of the new edit) still lists five fields: `Operator slug` / `Signature` / **`Algebraic laws`** / `Direct dependencies` / `Status`. The actual table now has five columns: `Operator` / `Signature` / `Dependencies` / **`Lowers to`** / `Status`. The template lists `Algebraic laws` (absent from the table, both pre- and post-edit) but omits the newly-added `Lowers to` column. This is a pre-existing drift exacerbated by the new column. The template should either be updated to match the actual table or explicitly noted as "format guide for future operators; current rows do not enumerate algebraic laws inline".

**skill-uptake-survey (pass).** No skill explicitly applies to layer-intro authoring polish work. The dispatch follows the L4/L3 pseudo-language conventions cited in CLAUDE.md (no skill exists for that; it is in-prompt discipline). `verify-citation-range` would have been low-value (citations are to existing book pages and the strawman, not Palace source ranges); `classify-variant-axis` does not apply (no new operators).

### Issues found

1. **Vocabulary-cohort skip-eligible per role spec; structural adaptation not flagged.** [`CYCLE.md` §Vocabulary cohort, lines 49-62; `CYCLE.md` §Open questions item 2] The role spec at `.claude/agents/layer-intro-author.md:103` says "Skip the subsection when the layer has only firm entries (no queue) or only rough-ins (no firm cohort)". All three L4 operators are firm; per strict reading the entire Vocabulary cohort subsection is skip-eligible. The dispatch adapted the template by reusing the middle slot for L4>L3 themes (cross-layer) rather than L4 rough-in operators (same-layer, as in the L1 precedent). Caveat 2 only discusses the empty `Queued` section, not this substantive template-shape decision. Severity: medium (structural decision diverging from role-spec template + L1 precedent without explicit caveat or precedent-citation justifying the divergence). Repair candidate: either (a) drop the Vocabulary cohort per role spec, or (b) add a caveat acknowledging that the middle subsection is a layer-N-specific adaptation (firm L4 ops + cross-layer L4>L3 themes, no rough-in L4 ops yet) and that this template variant is not the L1 form.

2. **"Format expected" template diverges from actual dep-map columns.** [`CYCLE.md` proposed-changes block 2, lines 91-96 of the `[new]` payload] The template lists 5 fields including `Algebraic laws` (which is not a column) and omits the new `Lowers to` column (which is now a column). Pre-existing drift on `Algebraic laws` — the old table also had no such column — but the new edit introduces `Lowers to` without updating the template. Severity: low (cosmetic; does not affect mdbook build). Repair candidate: update the template list to match the actual columns (Operator / Signature / Dependencies / Lowers to / Status), or annotate the template as "future-operator guide".

3. **`Lowers to` cell uses prose section-pointer rather than fragment-anchor link.** [`CYCLE.md` proposed-changes block 2, `iterate-while` row's `Lowers to` cell, line 88 of `[new]`] The cell references `[`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"What the L3 form for iterate_while looks like"` — the section exists at line 158 of the target file but the link does not include a fragment anchor (e.g., `#what-the-l3-form-for-iterate_while-looks-like`), so a reader following the link lands at the top of the page rather than at the cited section. Severity: low. Repair candidate: add the fragment anchor to the markdown link if mdbook's anchor-slugification of the section title is predictable.

4. **`krylov-step` row `Status` column carries pre-cycle-008 firmness lineage; cycle-008 wave-1 lifter promotion of the dissolution theme is not surfaced in the dep-map row.** [`CYCLE.md` proposed-changes block 2, krylov-step row, line 87 of `[new]`] The summary (line 13) says the L4>L3 dissolution theme was "promoted to firm cycle-008 wave-1 by the lifter". The new `Lowers to` cell records "L4>L3 firm" inline. The `Status` column for the L4 row only records `firm (harvested cycle-006; promoted from cross-layer-cross-cutter recommendation 2026-05-27T025354Z)` — accurately reflecting the L4 row's own provenance — but a reader scanning the dep-map for "what changed in cycle-008" sees no cycle-008 marker on this row. This is borderline pedantic (the L4 row's own status did not change in cycle-008), but the dep-map is the consumed-by-many shared structure and the firmness of the lowering target is load-bearing for readers using this row to navigate the chain. Severity: low (the prose in the `Lowers to` cell does carry the "L4>L3 firm" annotation; this is a navigation-quality nit, not a fact error).

5. **`gmres-inner-loop-iterate-while-migration` rough-in theme link form is permitted but the rough-in annotation lives only in prose.** [`CYCLE.md` proposed-changes block 2, iterate-while row, line 88 of `[new]`] The cell text is `is the rough-in theme [`gmres-inner-loop-iterate-while-migration`](../L4-L3/gmres-inner-loop-iterate-while-migration.md)` — the prose "is the rough-in theme" carries the firmness annotation; the link itself is bare (no `*(rough-in)*` italics inside or after the link). The friction-ledger entry `rough-in-rows-must-be-plain-text-when-anchor-missing` is correctly identified by caveat 4 as inapplicable (the anchor file does exist). This is not a defect against the existing friction-ledger entry, but the convention for "rough-in cross-references where the anchor exists" is not currently codified anywhere. The Vocabulary cohort subsection (line 60 of `[new]`) does use the explicit `*(rough-in; landed cycle-008 wave-2)*` italics annotation for the same theme reference, so there is intra-report inconsistency between the two locations of the same reference. Severity: low (the prose disambiguates in both locations; only the annotation style differs).

6. **Caveat 2 is well-formed; caveats 1, 3, 4 are well-formed.** All four caveats explicitly route follow-up to cycle-009+ planner or defer to integrator preference; none bury substantive undecided design questions. Caveat 3 in particular correctly flags the L1/L2/L3 dep-map asymmetry without forcing a decision. No issue here — included as a positive finding.

7. **The intro line count remains under the 200-line cap.** The pre-edit `book/src/L4/index.md` is 44 lines; the new edit adds ~50 lines of Semantics-overlay prose, ~15 lines of Vocabulary cohort, ~6 lines of new Working-Notes bullets, and ~2 lines of net column-table widening. Post-edit will sit comfortably under 200. No split into `semantics.md` / `dep-map.md` needed, as the report correctly notes (line 17).

## Repair

### Fixes attempted

1. **Finding**: Vocabulary-cohort skip-eligible per role spec; structural adaptation (middle subsection re-purposed for L4>L3 cross-layer themes) not flagged in caveats.
   **Decision**: repaired
   **Action**: Rewrote caveat 2 in `CYCLE.md` §"Open questions / caveats" to split the issue into (a) subsection-retention-despite-firm-only and (b) middle-slot-re-purposed-for-cross-layer-themes. Both adaptations now explicitly named, with the L1 precedent referenced, the role-spec divergence acknowledged, and three integrator-choice options enumerated (keep / drop middle / promote to template). Added suggested slug `vocabulary-cohort-middle-slot-cross-layer-adaptation` for cycle-009+ planner if precedent-setting is desired. Mechanical caveat-text edit; no content authoring.

2. **Finding**: "Format expected" template lists 5 fields including `Algebraic laws` (not a column) and omits the new `Lowers to` column.
   **Decision**: repaired
   **Action**: Rewrote the "Format expected" list in `CYCLE.md` proposed-changes block 2 to match the actual 5-column table (Operator / Signature / Dependencies / Lowers to / Status), and added a parenthetical note that algebraic laws are recorded inline in each operator's own page (not in the dep-map). Aligns template description with actual column structure.

3. **Finding**: `Lowers to` section pointer not fragment-anchored (`§"What the L3 form for iterate_while looks like"` is prose-only).
   **Decision**: repaired
   **Action**: Replaced the prose section pointer with a fragment-anchored markdown link `[krylov-step-typed-wrapper-dissolution §"..."](../L4-L3/krylov-step-typed-wrapper-dissolution.md#what-the-l3-form-for-iterate_while-looks-like)` in the `iterate-while` row's `Lowers to` cell. Anchor slug derived from mdBook's pulldown-cmark default slugification (lowercase + space-to-hyphen + backticks-stripped; underscores preserved per repo precedent at `book/src/L4/iterate-while-with-prev.md:117` and `book/src/spec/slices/arnoldi_step.md:18`). If the rendered anchor differs the integrator-finalize build will surface it.

4. **Finding**: `krylov-step` row's `Status` column doesn't reflect cycle-008 wave-1 lifter promotion of the dissolution theme; navigation-quality nit since the prose in `Lowers to` does carry "L4>L3 firm" annotation.
   **Decision**: repaired
   **Action**: Surgical edits to the `krylov-step` row: appended "— promoted cycle-008 wave-1 lifter" to the `Lowers to` cell's parenthetical, and appended "; lowering target firmed cycle-008 wave-1" to the `Status` cell's provenance trail. A reader scanning the dep-map for "what changed in cycle-008" now sees the marker on this row.

5. **Finding**: Intra-report annotation-style inconsistency on `gmres-inner-loop-iterate-while-migration` rough-in marker — Vocabulary cohort uses `*(rough-in; landed cycle-008 wave-2)*` italics; dep-map row uses prose `"is the rough-in theme"`.
   **Decision**: repaired
   **Action**: Unified on the italics-suffix form in both locations. In the dep-map `iterate-while` row's `Lowers to` cell, rewrote `is the rough-in theme [link]` → `is [link] *(rough-in; landed cycle-008 wave-2)*`. Also linked the Vocabulary cohort's bare slug `gmres-inner-loop-iterate-while-migration` to its anchor file (permitted per caveat 4 since the anchor exists) so the two locations now match on both annotation style and link form.

### Unrepairable findings

None. All five flagged findings were mechanical/surgical fixes within repair authority (caveat documentation, template description alignment, fragment-anchor addition, status-cell annotation, style unification). Critic's positive finding 6 (caveats well-formed) and observation 7 (line count) required no action.

## Suggested resolution

`ready` — integrator may apply this report's proposed-changes block as written. Notes for the integrator:

- The Vocabulary cohort's middle-slot adaptation (firm L4 + L4>L3 cross-layer themes + queued; instead of L1's firm + same-layer rough-in + queued) is now explicitly documented in caveat 2. Three options are surfaced: keep as-is, drop the middle subsection, or promote the adaptation to the role-spec template. Integrator preference governs; if the choice routes to meta-phase for role-spec promotion, the suggested slug is `vocabulary-cohort-middle-slot-cross-layer-adaptation`.
- The fragment anchor `#what-the-l3-form-for-iterate_while-looks-like` is derived from mdBook's default heading-slugification (verified against repo precedents at `book/src/L4/iterate-while-with-prev.md:117` and the four `gmres.md#fgmres` / `gmres.md#apply_BA` examples that all preserve underscores). If `cargo make book` shows a broken anchor at integrator-finalize, fall back to bare-link form (drop `#what-the-l3-form-for-iterate_while-looks-like`) and leave the prose section pointer as-is.
- No book/ or scaffolding/ writes were performed during repair; all edits are in-place to the report's CYCLE.md.

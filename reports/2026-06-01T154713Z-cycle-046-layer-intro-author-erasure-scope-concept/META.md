---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T16:05:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: pass
repaired_at: 2026-06-01T16:25:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: unrepairable
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "concepts/erasure-scope.md — NEW four-root erasure-scope taxonomy concept page"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing citation was verified against disk. The four substantive theme files all exist and their opening-paragraph anchors say what the page claims: `ksp-solve-outer-driver.md:3` (unconditional single-loop; "the loop is the operator … non-identity" — matches root 1), `orthogonalize-variant-split.md:3-15` (MGS `j`-loop obstructs, CGS/CGS2 lift; variant-conditional — matches root 2), `chebyshev-nested-recurrence.md:3-16` (inner `k`-recurrence + outer `pc_it` sweep, both `iterate_while_pure_L3`; unconditional nested-double-loop — matches root 3), `eigsolve-opaque-eigen-iteration.md:3-22` (SLEPc/ARPACK opaque, marker-only, never re-promotable — matches root 4). The canonical-source anchors into `L3-L2/index.md` are accurate: §Vocabulary-cohort substantive themes occupy 56-61 (line 56 is the substantive-themes header, 58-61 the four substantive bullets), and the §Erasure-scope-taxonomy block occupies 67-71 (line 67 is the taxonomy intro paragraph that states the axis; 68/69/70/71 are the four roots). The report's phrasing "67-71 for the four roots" is a one-line over-broad locator (the four roots are strictly 68-71; 67 is the intro), but the cited range is in-bounds and the section is correctly named — a convenience-locator inaccuracy of one line, not a drift. All eight operator L3/L2 entries cited exist, and the two fold-in concept anchors (`sequential-obstruction.md`, `tensor-field-lift.md`) exist; the §"Sub-kind: out-of-scope-obstruction" sub-anchor in `sequential-obstruction.md` is present at line 50 (range 50-81 in-bounds). No `verified_against:` YAML block is emitted by this report, so that sub-check no-ops. The page is a transcription/cross-reference home, not a source-rotation, so there are no Palace file:line pinpoints to `--anchor`-adjudicate.

**surface-or-evidence — pass.** Not a refinement of an existing operator/theme — this is a NEW cross-cutting concept page that restates an already-RATIFIED taxonomy and forwards per-theme algebraic detail to the four theme files. No rotation_claim is asserted on existing surface; the page adds vocabulary surface (the four-root naming + the renderable-vs-marker distinction) backed by the canonical write-up and the four theme files. Backfill/aggregation shape, allowed.

**rotation-quality — pass (largely no-op).** The page asserts no new algebraic/structural rotation; it names a classifying axis over already-firm L3>L2 themes and restates their (already-landed) rotations by reference. There is no L_{n+1}→L_n compaction claim to evaluate for strict-more-compactness. Not applicable to a taxonomy-home concept page; marked pass.

**variant-axis-coverage — pass (no-op as orthogonal-axis check; substantively complete).** No operator with orthogonal implementation variant axes (preconditioner present/absent, in-place/out-of-place) is being authored, so the classify-variant-axis check no-ops. Worth noting the page IS itself a coverage statement over the erasure-scope axis, and all four roots are populated by firm themes (verified on disk) — the report explicitly scopes out `apply_linop` (transparent lift, no L2 RHS, correctly absent). No hidden branch.

**cross-reference-integrity — pass.** Build-readiness verified three ways. (1) Fence-enclosure: the `edit:book/src/concepts/erasure-scope.md` block spans lines 36-82 and ENCLOSES the full page body — `## The four roots`, `## Renderable vs. marker — the root-4 distinction`, and `## See also` all sit inside the fence before the closing ` ``` ` at line 82. No firm-body-outside-fence defect. (2) Live-link resolution: all 14 distinct live markdown links in the page body were resolved relative to `book/src/concepts/` and every target exists on disk (the two same-dir concept links + twelve `../L3-L2/`, `../L3/`, `../L2/` links). No link points at a not-yet-existing target, so no plain-text-defer is required. The one section reference into `sequential-obstruction.md` (page line 75) uses a bare file link with the section named in prose (no `#fragment`), so no fragment-anchor linkcheck risk. (3) Surgical inserts: the SUMMARY.md `[old]` block (the `nested-constructed-operator-gate` + `eigsolve` lines + blank + `# Design Artifacts`) matches disk lines 250-253 exactly, and the insert appends `erasure-scope` immediately after the last concept row without clobbering the `# Design Artifacts` header. The concepts/index.md `[old]` block matches disk lines 78-79 exactly, and the new `erasure-scope` row inserts alphabetically between `elementwise-product` and `finest-level-unwrap` (correct: "el" < "er" < "fi").

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried as the report's own proposal claim; the page describes the L3>L2 edge family throughout, and every per-root prose block discusses the L3>L2 hop it labels (root 1 ksp_solve L3→L2, root 2 orthogonalize L3→L2, root 3 chebyshev L3→L2, root 4 eigsolve L3→L2) consistently with the theme files. No mismatch.

**plan-kind-consistency — warning.** The page is a cross-cutting concept page (correct kind family); the substantive question is the `kind` column value `layer-pattern` vs `methodology`. Both are real values in `concepts/index.md` (12 `layer-pattern`, 8 `methodology`). The report's two cited siblings (`sequential-obstruction`, `tensor-field-lift`) are both `layer-pattern`, supporting the choice. HOWEVER, `erasure-scope` is structurally an *axis used to classify themes*, and the closest existing analogue of THAT shape — `variant-absorption` — is filed `methodology` (as is `rotation`, `scope-out-obstruction`, `constructed-operators`). So the page sits genuinely between the two: it is layer-edge-specific (favoring `layer-pattern`) but it is a classifying-axis-over-themes (favoring `methodology`, by precedent). The report disclosed this ambiguity explicitly in its Open-questions and reasoned the choice ("about the L3>L2 layer-edge surface shape specifically, not the dissection process in general"), which is defensible. Marked `warning` (not `fail`) because the content shape is correct for a concept page and the classification is reasoned, but the `variant-absorption`-is-`methodology` precedent is a real counter-signal the integrator should adjudicate before applying.

**skill-uptake-survey — pass (telemetry).** The proposed-changes-fence-encloses-full-body-guard skill is the relevant procedure for this report's build-readiness shape; the report does not name it by slug but its "Verification performed" section performs the equivalent check (all four themes + anchors + the two concept anchors verified on disk). Pure presence telemetry, non-blocking — no skill-invocation reference is required of a producer, and the verification was in fact done.

### Issues found

1. **Citation locator one-line over-broad (minor) — CYCLE.md §Summary line 12, §Verification line 30, §Supporting-evidence line 112.** The report cites `L3-L2/index.md` "lines 67-71" "for the four roots." On disk the four roots are lines 68-71; line 67 is the taxonomy *intro* paragraph (it states the axis, not a root). The cited range is in-bounds and the named section (§Erasure-scope-taxonomy) is correct, so this is a convenience-locator imprecision, not a drift. Severity: low (cosmetic).

2. **Kind classification is genuinely ambiguous — CYCLE.md §3 line 100 + Open-questions line 125; insert at concepts/index.md.** `layer-pattern` is defensible (matches the two sibling concepts the page invokes) but `methodology` has a strong precedent: `variant-absorption` — the closest structural analogue (an axis used to classify themes) — is filed `methodology`. The producer flagged this for the critic explicitly. Severity: low-medium; integrator should pick before applying. Not a fail (content shape is a correct concept page either way).

3. **Stray trailing code-fence in CYCLE.md — line 128.** A lone ` ``` ` sits at the end of the file after the "Open questions / caveats" prose (line 127) with no matching opener after the last proposed-changes block closed at line 108. This is a CYCLE.md-level cosmetic artifact only — it does NOT affect any proposed-changes block (all three blocks 36-82 / 86-96 / 102-108 are cleanly balanced and parse correctly). Severity: trivial (report-hygiene; no build impact).

### Notes for downstream

- All disk verifications passed: target file genuinely absent (clean create), 4 theme files + 8 operator entries + 2 concept anchors + 1 sub-anchor all present and accurate, both surgical inserts match disk exactly with correct alphabetical/sectional placement.
- The only non-trivial decision left for the integrator is the kind-column value (issue 2).

## Repair

### Fixes attempted

- **Finding 1 (citation locator one-line over-broad — `L3-L2/index.md` "67–71 for the four roots").**
  - **Decision**: repaired.
  - **Action**: Verified against disk (`book/src/L3-L2/index.md`): line 67 is the §Erasure-scope-taxonomy intro paragraph that states the axis; lines 68–71 are the four roots (68 unconditional-single-loop, 69 variant-conditional-single-loop, 70 unconditional-nested-double-loop, 71 opaque-library). Kept each `67–71` block-range citation (it correctly names the §Erasure-scope-taxonomy *section* span) and tightened the gloss so the "four roots" sub-range is stated as 68–71. Edited five sites in CYCLE.md: §Summary (line 12), §Verification performed (line 30), the page body inside the proposed-changes fence (line 45), the page §See also inside the fence (line 81), and §Supporting evidence (line 112). The §Open-questions caveat (line 127) was left as-is — it lists `(67–71, 56–61)` as section-block references for the drift note, carries no "four roots" gloss.

- **Finding 2 (kind classification `layer-pattern` vs `methodology` — genuinely ambiguous).**
  - **Decision**: unrepairable (integrator adjudication, not a mechanical defect).
  - **Rationale**: This is a judgment call between two real `concepts/index.md` kind values, not a mechanical error. **Reading A (`layer-pattern`, as the producer chose):** the page names how the L3>L2 layer-edge surface works, matching its two invoked sibling concepts `sequential-obstruction` and `tensor-field-lift` (both `layer-pattern`). **Reading B (`methodology`):** the page is structurally an *axis used to classify themes*, and the closest existing analogue of THAT shape — `variant-absorption` — is filed `methodology` (as are `rotation`, `scope-out-obstruction`, `constructed-operators`). The producer disclosed and reasoned the choice (CYCLE.md §3 line 100 + Open-questions line 125). Flipping the kind would be a content decision exceeding repair authority. **Left `layer-pattern` as the producer chose** (CYCLE.md unchanged at the index-insert row line 106 and the rationale); routed to **integrator-per-report** to confirm or change the kind column at apply time. Not a blocker either way — the page body is a correct concept page under both readings.

- **Finding 3 (stray trailing code-fence at CYCLE.md line 128).**
  - **Decision**: repaired.
  - **Action**: Removed the lone trailing ` ``` ` after the §Open-questions prose (it had no matching opener after the third proposed-changes block closed at line 108). Re-verified fence balance: exactly six fences remain forming three balanced proposed-changes pairs (`erasure-scope.md` 36–82, `SUMMARY.md` 86–96, `concepts/index.md` 102–108) — all three blocks the critic checked stay intact and parse.

### Unrepairable findings

- **Finding 2 (kind classification).** Routed to **integrator-per-report** for adjudication at apply time. Both readings stated above; producer's `layer-pattern` left in place as the default. This is a one-token column choice with no build or content-correctness impact — the integrator picks `layer-pattern` (sibling-concept precedent) or `methodology` (classifying-axis precedent) when applying the `concepts/index.md` insert.

## Suggested resolution

`ready`. Two of three findings were mechanical and are repaired (citation-locator gloss tightened to 68–71 for the four roots across five sites; stray trailing fence removed, fence balance re-verified). The one remaining finding (kind classification) is a defensible-either-way one-token column choice the integrator-per-report should pick at apply time — it does not block application and the page body is correct under both readings. No content authoring was required; no follow-up specialized-agent dispatch is needed.

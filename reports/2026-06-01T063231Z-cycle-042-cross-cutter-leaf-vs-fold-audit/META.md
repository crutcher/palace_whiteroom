---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T064500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: warning
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
---

# META: verification of "L2 observation — leaf-vs-fold design fork (D1 leaf-floor vs D2 fold-only)"

## Critique

### Checks run

**citation-validity — warning.** `citecheck --scan` reports 9 ok / 1 failing of the machine-parseable citations. The single `[MISS]` is `open-questions.md:965` (bare filename, no `scaffolding/` prefix) in the §"OQ ledger" supporting-evidence block (CYCLE.md:283) — a path-hygiene drift, NOT a bad line: the SAME line is cited correctly as `scaffolding/open-questions.md:965` elsewhere in the same block, and the scan confirms `:965` is in bounds (file has 998 lines). All other ranges resolve in-bounds. Two **content** line-count claims in the count-delta table are wrong, however, and I record them here rather than under cross-reference because they are quantitative-claim errors, not link breakage: (a) CYCLE.md:79 states `L2/dot.md` is "220 ln" — the on-disk file is **345 lines**; (b) CYCLE.md:81 states `dot-body-identity.md` is "186 ln" — actual is **185 lines** (off-by-one, trivial). The (a) error is load-bearing for the report's central quantitative argument (see surface-or-evidence). Warning, not fail: every cited file and line *exists and is in-range*; the defects are one prefix-drop and two size mis-statements.

**surface-or-evidence — warning.** This is an observation report that mutates no surface; the relevant test is whether the load-bearing factual claims are backed by the cited evidence. Most are, and I confirmed them against the on-disk entries: (1) the **asymmetry claim** (the fork applies to `dot`/`scal` as fold-leaves but NOT to `nrm2` the consumer) is **correct** — `book/src/L2/nrm2.md:27-35` and its frontmatter `consumes:` block explicitly carry "CONSUMER of `inner_product`, NOT a fold member", and `L2/dot.md:41-68` carries the leaf-of-fold do-NOT-merge framing; (2) the **D1-vs-D2 disentanglement** (D2 declined to author a `dot` leaf rather than authoring a rival fold-only `dot`) is supported by `scaffolding/open-questions.md` `l2-no-dot-leaf-floor-but-fold-is-the-l2-surface` (D2's scoping note, which says "no L2 `dot.md` floor exists or is needed", not "a fold-only `dot` was built"). BUT the report's **core quantitative argument is overstated against the actual floor entries**: the Summary (CYCLE.md:22) and §3 (CYCLE.md:107-135) assert the delta files are "≤220 lines of pure cross-reference", "author no substance", "duplicate no adjacent-layer authoring", "+4 *pointer* files, not +4 *content* files". The on-disk `L2/dot.md` is 345 lines and carries **its own substantive content**: a §"Fusion note" (`:141-164`) with three independent L0 source citations (`vector.cpp:665-672`, `:674-685`, `vector.hpp:247-253`) and a full §"Algebraic laws" (`:166-212`) reproducing 13 laws plus a load-bearing IEEE-754 non-associativity non-law. The laws are flagged "inherited unchanged" and the fusion note explicitly defers the *full* de-fusion treatment to the fold-parent — so the report's *direction* (these are thin floors that defer substance, below the duplication-explosion bar) is substantially supported — but the specific framing "author no substance / pure cross-reference / ≤220 lines" is inaccurate: the floors reproduce laws and carry their own L0 anchors. Warning: the verdict survives, one supporting quantitative claim does not.

**rotation-quality — pass.** Not applicable to an observation report. The report asserts no algebraic/structural/reduction rotation of its own; it audits an existing leaf-vs-fold relationship and explicitly notes (CYCLE.md:298-304, Open-questions) that the leaves carry no algebraic content the folds lack — the distinctness it claims is on the layer-coherence axis, correctly NOT framed as a rotation.

**variant-axis-coverage — pass.** The report does not author an operator/theme with variant axes. It correctly *handles* the variant-axis dimension as evidence: it notes (CYCLE.md:141-148) that the fold collapses a variant axis (conjugation / arity) the leaf fixes, and flags (CYCLE.md:240-244) the held arity-family's output-aliasing axis as the fold's, not a leaf axis. No hidden branches; the asymmetry carve-out for `nrm2` is explicit. Not-an-authoring-report, so no coverage obligation.

**cross-reference-integrity — pass.** Every named slug, chapter, theme, decision file, OQ, and report the observation references resolves on disk: `book/src/L2/{dot,scal,nrm2,inner_product,linear_combination}.md`, `book/src/L2-L1/{dot-leaf-identity,scal-fold-specialization}.md`, `book/src/L3-L2/{dot-body-identity,scal-body-identity,nrm2-body-identity}.md`, `book/src/L3/{dot,scal,nrm2}.md`, `scaffolding/decisions/axpby-as-primitive.md`, both cycle-041 harvester report dirs, and the four cited OQ lines all exist. I cross-checked the count-delta *structure* against `book/src/SUMMARY.md` (carries `L2/dot`, `L2/scal`, `L2/nrm2` lines + the L2>L1 and L3>L2 theme lines) and `book/src/L2/index.md` (carries the `dot`/`scal`/`nrm2` dep-map rows :45-47 + the cohort dep-map rows :60/:62/:63): the per-leaf "+1 L2 chapter / +1 L2>L1 theme / +1 dep-map row / +1 SUMMARY line; L3>L2 theme is ±0 re-anchor" decomposition is **structurally accurate** — the L3>L2 body-identity themes do exist under both readings (so ±0 is right), and the L2 chapters + L2>L1 themes + dep-map rows + SUMMARY lines are the genuine adds. The family-wide "+4 files (2 chapters + 2 themes) + 2 dep-map rows" tally is correct at the file-count level (the line-count *annotations* inside the table are the warning above, not a cross-reference defect). No artifact mutation occurred — `git status` is clean and the report writes only its own CYCLE.md.

**edge-label-fidelity — pass.** Not applicable. The report carries no single L_{n+1}→L_n edge label to honor; it discusses multiple edges (L2>L1, L3>L2) and consistently attributes each to its correct layer pair throughout (the dot/scal L2>L1 leaf themes, the L3>L2 body-identity themes, the `nrm2` consumer edge). No mismatched edge framing found.

**plan-kind-consistency — pass.** Declared `same-layer-cross-cutter` observation; content shape matches. It is a single unification-candidate adjudication-input observation, explicitly framed as meta-phase INPUT not a self-enacted decision ("The meta-phase decides; this report supplies the count-delta evidence", CYCLE.md:30; "No follow-up dispatch is needed from THIS observation beyond the meta-phase adjudication", CYCLE.md:218). The §"Consequence" and §"Recommendation" sections are correctly scoped as consequence-of-this-observation and meta-phase-input, and the report explicitly disclaims enacting (CYCLE.md:313-316, "One observation per invocation — I have NOT bundled the held arity-family dispatch decision into a separate observation"). No mis-classification.

**skill-uptake-survey — pass.** The report's shape (count-delta audit of adjacent-layer footprint) implies the cross-cutter / unification-observation skills; no dedicated skill governs a leaf-vs-fold count-delta audit. The report does not cite a skill invocation, but none is mandated for this observation shape. Surfacing-only check; no block.

### Issues found

1. **`L2/dot.md` line-count and "no substance" overstatement** — CYCLE.md Summary (:22), §3 (:107-135), and count-delta table (:79). The report characterizes the delta files as "≤220 lines of pure cross-reference" that "author no substance / duplicate no adjacent-layer authoring / +4 pointer files, not content files". On disk `book/src/L2/dot.md` is **345 lines** and carries a §"Fusion note" (`:141-164`, three independent L0 citations) and a §"Algebraic laws" (`:166-212`, 13 laws + IEEE-754 non-law). The floors *do* defer the full de-fusion treatment to the fold-parent and *do* flag laws as inherited — so the verdict (below the duplication-explosion bar) holds — but the "pure cross-reference / no substance / ≤220 ln" framing is inaccurate and is the load-bearing support for the §3 "NO duplication explosion" conclusion. Severity: medium (verdict survives; supporting claim is wrong and should be softened to "thin floors whose substantive content — fusion note + laws — is deferred-to-or-inherited-from the fold-parent, not independently re-authored").

2. **Count-delta table line-count annotations are stale** — CYCLE.md:79 (`L2/dot.md` "220 ln" → actual 345), CYCLE.md:81 (`dot-body-identity.md` "186 ln" → actual 185). The (a) `L2/dot.md` figure feeds issue 1; the (b) is a trivial off-by-one. The *file-count* deltas (+1/+1/+1/+1 per leaf; +4 files family-wide; ±0 L3>L2) are all correct. Severity: low-to-medium (the 220 figure is load-bearing via issue 1; the 186 is cosmetic).

3. **Citation path-hygiene drift** — CYCLE.md:283, `open-questions.md:965` written without the `scaffolding/` prefix (the same line is correctly prefixed elsewhere in the block). The line itself is valid and in-range. Severity: low (mechanical prefix normalization).

---
repaired_at: 2026-06-01T065200Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: repaired
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

## Repair

### Fixes attempted

- **Finding (Issue 1, medium)**: The "≤220 lines of pure cross-reference / author no substance" framing is inaccurate — on-disk `book/src/L2/dot.md` is 345 lines with a substantive §"Fusion note" + §"Algebraic laws".
  - **Decision**: repaired
  - **Action**: Softened the framing in two load-bearing places. (a) Summary (CYCLE.md §Summary, the "≤220 lines of pure cross-reference / author no substance" sentence): rewritten to "identity-in-form and DEFERS the full de-fusion to the fold-parent, flagging its laws as inherited" — the verdict now rests on the deferral-and-inheritance, not on a false "no substance" claim. (b) §3 ("+4 *pointer* files, not +4 *content* files" passage): rewritten to acknowledge the floors DO carry §"Fusion note" + inherited-unchanged §"Algebraic laws" but as a deferral-and-inheritance restatement rather than independent re-authoring of the fold's de-fusion treatment. The §3 conclusion (NO duplication explosion, below the bar) is preserved; only its support phrasing changed. The §3 bullet for `L2/dot.md` already described the fusion note + inherited laws accurately with correct `:142-164`/`:166-212` citations, so it was left as-is. Mechanical prose softening; no re-analysis — the recommendation (keep leaf-floor (b)) is unchanged.

- **Finding (Issue 2)**: Stale line-count annotations in the count-delta table.
  - **Decision**: repaired
  - **Action**: count-delta table (CYCLE.md §2). `L2/dot.md` row "220 ln" → "345 ln" (+ deferral/inherited annotation); `dot-body-identity.md` row "186 ln" → "185 ln" (off-by-one). The file-count deltas (+1/+1/+1/+1 per leaf; ±0 L3>L2) are correct and unchanged. (Note: the L2>L1 `dot-leaf-identity.md` row also carries a "220 ln" annotation that the critic did not flag; left as-is per the named-annotation scope.)

- **Finding (Issue 3, low)**: Citation path-hygiene drift — `open-questions.md:965` without `scaffolding/` prefix.
  - **Decision**: repaired
  - **Action**: The bare occurrence is at CYCLE.md:68 (the critic's :283 line reference was approximate; :287 already carried the correctly-prefixed form). `open-questions.md:965` → `scaffolding/open-questions.md:965`. Line is valid and in-range; pure prefix normalization.

### Unrepairable findings

None. All three findings are mechanical prose / annotation / path-hygiene fixes within repair authority. No substantive re-analysis was required; the report's recommendation (keep leaf-floor reading (b)) and its NO-duplication-explosion verdict are unchanged.

## Suggested resolution

`ready`. This is an observation report (no surface mutation). The two `warning` checks (citation-validity, surface-or-evidence) were both driven by the same stale `220 ln` / "no substance" framing for `L2/dot.md`; the framing is now softened to rest on deferral-and-inheritance (which the on-disk floor genuinely exhibits) and the line counts corrected. The count-delta evidence the report supplies to the batch-12 meta-phase adjudication stands: file-count deltas were already correct, and the central verdict (leaf-floor (b) below the duplication-explosion bar; genuinely-distinct dual on the "both L levels" axis) is unaffected. Integrator may promote the report's Open questions and the keep-leaf-floor recommendation as meta-phase input as written.

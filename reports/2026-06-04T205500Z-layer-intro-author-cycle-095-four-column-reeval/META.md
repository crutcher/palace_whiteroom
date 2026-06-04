---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T211944Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-04T213000Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of the cycle-095 D4 four-column seed→firm cascade re-evaluation

## Critique

### Checks run

**citation-validity — warning.** Every claim carries a pointer; the load-bearing L0 pinpoints all resolve correctly on disk (verified by `read_range`): `electrostaticsolver.cpp:126` is the off-diagonal `C(i,j) = linalg::Dot(...)`, `:118-119` the diagonal `M_elec->Mult` + `Dot`, `:95` the `PostprocessTerminals` call, `:100` the def; `magnetostaticsolver.cpp:138` the off-diagonal current-normalized Dot, `:135` the inner-`j` loop, `:122` the `M(A.size())` allocation, `:151-152` the `Minv.Invert()`, `:105` call / `:110` def. The constituent-firmness survey table (§Summary `:31-41`) is accurate on disk: `L4/fe_assemble`, `L4/solve_family`, `L4/ksp_solve`, `L1/fe_assemble` all `firmness: firm`; `L1/ksp_solve` §Status firm; `L1/matrix-weighted-norm` §Status firm (c091). `gram_reduce` (firmness `rough-in (test-coverage-bounded)` on disk) and `bilinear-form` (firmness `rough-in` on disk) are the two acknowledged wave-1/D3 forward-references, both correctly framed in §Summary `:42` and confirmed firmed by the D1 and D3 reports (D3's verdict is DISCHARGE→FIRM, read this cycle). The one drift: the capacitance.L4 §composition edit (CYCLE.md `:93`) cites `book/src/L4/gram_reduce.md:255` for "the literal 'positive witness 1' label" — but that label is at `gram_reduce.md:279` (§Evidence), not `:255` (`:253-257` is the narrowed-promotion-route prose, which D3 is replacing wholesale anyway). The label survives D3 (§Evidence at `:279+` is outside D3's `:228-271` replacement range), so the reference target is real but the line number is ~24 lines off. Warning, not fail (the cited content exists; only the pinpoint drifts).

**surface-or-evidence — pass.** This is the feature-surface composition-root kind; the adapted checklist applies. Each column's evidence is the L0 driver-source range + constituent down-links, not a new per-op algebraic claim. The L0 ranges are cited and resolve (`electrostaticsolver.cpp:21-98`/`:100-140`, `magnetostaticsolver.cpp:22-108`/`:110-152`); every down-link resolves to a real constituent chapter; the maturity claims on the down-links match on-disk `## Status` after the within-wave D1/D3 flips. No record is named in a signature without a definition home (these are composition roots over already-defined vocabulary). Pass.

**rotation-quality — pass.** Formally no-op for the feature-surface kind (a composition root rotates nothing — it recomposes already-firm vocabulary outward). The report makes no new algebraic/reduction rotation claim; the reduction algebra lives in the linked `gram_reduce`/`matrix-weighted-norm`/`bilinear-form` chapters. Pass (not applicable).

**variant-axis-coverage — pass.** Formally no-op for the feature-surface kind (the variant axes — unit-weight vs current-normalized, fixed-operator vs per-element — live in the composed constituents, principally `gram_reduce`'s `normalization-weight` axis, which the report correctly attributes to the combinator). The capacitance/inductance `w=1` vs `w=1/(IᵢIⱼ)` distinction is described as the SAME `gram_reduce` combinator at two weight corners, not a hidden branch. Pass (not applicable).

**cross-reference-integrity — warning.** All `[link]` references resolve; all named slugs (constituent ops, sibling columns) exist on disk. The `composes:`→`edges:` migration is faithful to scheme §4(c): vocabulary-op targets → `depends-on`, sibling-column targets → `reference`, `l0_ground_truth:` → `depends-on kind: cites-evidence`, maturity qualifiers dropped. `kind: composes`/`kind: folds`/`kind: cites-evidence` are valid (scheme §2: `kind:` is documentation-only, linters ignore; both bare-string and `{target:, kind:}` forms permitted). The `feature_root: seed` + `rank: firm` SPLIT (scheme §3) is applied to all 12 column-level files. The cascade-coupled whole-`book/src/feature/` sibling-status grep is run and the five D5-partition stale `(seed)` mentions correctly flagged-not-edited. The defect is a **column-count inconsistency** in the `## Chapter-kind status` edit (see Issues #1) plus a **stale spine-root.md group-intro line** the report consciously left (Issue #3). Warning.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge labels in this report (the feature-surface edges are `depends-on`/`reference` typed edges, not lowering-direction labels). The within-column level pointers (L0→L1 `reference`) are correctly directed. Pass.

**plan-kind-consistency — pass.** Declared work is a `seed→firm` rank flip on feature-surface composition-root chapters under the OWN-COMPOSITION rule; the content shape matches (frontmatter SPLIT + status-prose re-anchor + constituent-table maturity updates + index/group-intro narration). No rough-in placeholders in a firm-claimed body. The rank-invariant reasoning (every `depends-on` target firm post-cascade → `rank(column=firm) ≤ min(deps)=firm`) is sound. Pass.

**skill-uptake-survey — pass.** The report's shape (firm-promotion-coupled cascade re-anchor) implies the `firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep` guard, which the report explicitly invokes (§grep, CYCLE.md `:730-750`). The OWN-COMPOSITION / `feature_root:`-split mechanics are sourced to scheme §3/§4(c). Telemetry only; pass.

### Issues found

**Issue #1 — column-count inconsistency in the `## Chapter-kind status` edit (cross-reference-integrity, medium).** CYCLE.md `:706` (the `feature/index.md` `## Chapter-kind status` edit) declares "**`firm` (12 columns)**" and `:710` "**`seed` (1 column)**" — totalling 13. But the on-disk feature spine has exactly **12 columns** (verified: 12 `.L4.md` files — lifecycle + boundary-mode/driven/eigenmode/electrostatic/magnetostatic/transient + capacitance/eigenfrequency-qfactor/energy-fields/inductance/sparameters). The edit's OWN firm enumeration (`:707-709`) lists only **11** firm columns (5 driver-leaf + 5 output-product + 1 spine-ROOT), and `:710-711` lists 1 seed (boundary-mode) → 11 firm + 1 seed = 12, contradicting the "12 firm" header. The correct post-cascade split is **11 firm / 1 seed**. Root cause: the report inherited a pre-existing "13 columns" miscount that lives in the UNEDITED index narration (`feature/index.md:57` "all-13-column re-evaluation", `:61` "all 13 columns") and the report's own §Summary framing; the D4 brief's "12 firm / 1 seed" figure is itself the same off-by-one. The "12 firm" header should read "11 firm", and the two unedited "13 columns"/"all-13-column" index lines (`:57`, `:61`) — which the report owns this cycle as `feature/index.md` SOLE owner — remain stale (they survive into the firm-cascade narration unchanged).

**Issue #2 — citation pinpoint drift on the "positive witness 1" label (citation-validity, low).** CYCLE.md `:93` (capacitance.L4 §composition edit) cites `book/src/L4/gram_reduce.md:255` for "the literal 'positive witness 1' label". The label is actually at `gram_reduce.md:279` (§Evidence, "Electrostatic capacitance Gram (positive witness 1)"); `:255` is the §Status narrowed-promotion-route prose. The target text is real and survives D3's wholesale §Status replacement (D3 replaces `:228-271`; §Evidence begins at `:279`), so this is a line-number drift (~24 lines), not a dead reference.

**Issue #3 — stale spine-root.md group-intro closing line (cross-reference-integrity, low).** `book/src/feature/spine-root.md` closing line reads "Status is `seed` — a feature column promotes past `seed` only once all its composed constituents are firm." This is (a) a stale `seed` status for the lifecycle column, which the report's own `## Chapter-kind status` edit (`:709`) lists as **firm**, and (b) the SUPERSEDED pre-OWN-COMPOSITION promotion rule. The report consciously declines to edit it (CYCLE.md `:767`: "The `spine-root.md` group intro was not touched … no cascade column is in that grouping"). Defensible under the cascade-coupling partition (no cascade column is in the spine-ROOT grouping), but the line is genuinely stale and spine-root.md is a group-intro page in the report's claimed feature-index ownership surface this cycle (parallel to the output-product.md / driver-leaf.md group-intro sibling-status lines the report DID re-anchor). The same supersession the report fixes in those two sibling group-intros is left unfixed here.

**Note (not an issue) — `cites-evidence` L0-edge convention correctly flagged.** The report flags (CYCLE.md `:763`) that the `kind: cites-evidence` `depends-on` edges target `palace/...:lo-hi` ranges, not book slugs, and that the rank linter's slug-resolution (`book/src/<slug>.md`) will NOANC on them unless `cites-evidence` exempts the target — routed as an OQ for the batch-30 meta-phase / D7 baseline-exceptions. This is flagged, not silently mishandled (context (e) satisfied). The `feature_root:`-split-vs-legacy-`status:` dual-form linter question (`:764`) and the D3-forward-reference (b)-fallback (`:765`) are likewise correctly flagged.

## Repair

### Fixes attempted

- **Finding (Issue #1)**: Column-count inconsistency — the `## Chapter-kind status` edit declares "`firm` (12 columns)" + "`seed` (1 column)" = 13, but the on-disk spine has exactly 12 columns and the edit's own firm enumeration lists 11 (5 driver-leaf + 5 output-product + 1 spine-ROOT); the correct split is 11 firm / 1 seed. The pre-existing "13 columns"/"all-13-column" miscount also rides in two unedited-looking index narration lines.
  - **Decision**: repaired.
  - **Action**: Verified the column count on disk directly (`ls book/src/feature/*.md` → 12 column families: boundary-mode, capacitance, driven, eigenfrequency-qfactor, eigenmode, electrostatic, energy-fields, inductance, lifecycle, magnetostatic, sparameters, transient). Fixed the `## Chapter-kind status` header in CYCLE.md `:706` from "`firm` (12 columns)" → "`firm` (11 columns)" (the firm enumeration `:707-709` already correctly lists 11; the `seed` (1 column) line `:710` is correct → 11 + 1 = 12 = true total). ALSO corrected the two pre-existing "13"-count phrasings that fall *inside* D4's own wholesale-replacement edit blocks for `feature/index.md` (D4 sole-owns that file this cycle): CYCLE.md `:698` "all-13-column re-evaluation" → "all-12-column" (the `feature/index.md:57` spine-scope paragraph, fully covered by the replacement) and CYCLE.md `:704` "re-evaluated all 13 columns" → "all 12 columns" (the `feature/index.md:61` chapter-kind paragraph, fully covered by the replacement). Confirmed on disk that index.md `:57`/`:61` lie within the paragraphs these edit blocks replace, so the stale on-disk "13" counts are overwritten by the corrected text on apply. (Files: `reports/<id>/CYCLE.md` §"feature/index.md — the `## Chapter-kind status` split" + the two preceding `feature/index.md` edit blocks.) Mechanical count fix; no substantive column-flip verdict changed.
  - **Note**: did NOT change the on-disk `feature/index.md:55` paragraph beyond what D4's own `:55` edit block already does (that block correctly flips capacitance/inductance to firm); it is in D4's replacement scope.

- **Finding (Issue #2)**: Citation pinpoint drift — capacitance.L4 §composition edit cites `gram_reduce.md:255` for the "positive witness 1" label, but the label is at `:279`.
  - **Decision**: repaired.
  - **Action**: Verified on disk (`grep -n "positive witness 1" book/src/L4/gram_reduce.md` → line 279; `:253-257` is the narrowed-promotion-route §Status prose). Fixed CYCLE.md `:93` `:255` → `:279`. (File: `reports/<id>/CYCLE.md` §"capacitance.L4.md — §"The composition" stage-2 status label".)

- **Finding (Issue #3)**: Stale `spine-root.md` group-intro closing line still says lifecycle is `seed` (and states the superseded pre-OWN-COMPOSITION rule).
  - **Decision**: not-needed (cross-report — out of this D4 repair's edit surface; verified already handled by D5).
  - **Action / cross-check**: Per the c095 partition `spine-root.md` is D5's owned file, NOT D4's (D4 owns `output-product.md` + `driver-leaf.md` group intros, both of which it correctly re-anchored). Editing it from this D4 repair would be a cross-report write. Verified D5's report (`reports/2026-06-04T210500Z-layer-intro-author-cycle-095-feature-root-closure-typing/CYCLE.md`) already re-anchors that exact line: its edit block at `:774` targets `spine-root.md:9`, flipping lifecycle off the stale `seed`/superseded-rule narration. So the line is fixed by D5; no integrator backfill needed, but flagged here as a cross-check (integrator should confirm D5 applies before/with D4 — both layer-intro-author reports serialize cleanly).

### Unrepairable findings

None. Both in-scope warnings (citation pinpoint drift; column-count inconsistency) were mechanical/surgical and repaired in place. Issue #3 is correctly out-of-partition for D4 and already covered by D5.

## Suggested resolution

`ready`. Notes for the integrator:
- The column-count is now consistently 11 firm / 1 seed (boundary-mode the lone seed) across the `## Chapter-kind status` header, its enumeration, and the two `feature/index.md` narrative paragraphs. Account for the full post-cycle state: D4 flips 4 columns firm (capacitance/inductance/electrostatic/magnetostatic); D5 types the remaining non-cascade columns (driven/eigenmode/transient/eigenfrequency-qfactor/sparameters/energy-fields + lifecycle = firm; boundary-mode = seed).
- The on-disk `feature/index.md:63` `## Chapter-kind status` enumeration block currently reads "`firm` (7 columns)" / "`seed` (5 columns)" — D4's `:61`-anchored edit block replaces that whole `## Chapter-kind status` opening + split with the corrected 11-firm/1-seed table. Confirm the integrator applies D4's `## Chapter-kind status` replacement over the on-disk `:61-71` span (the edit block covers the full split), not just the opening paragraph.
- Cross-check: D5's `spine-root.md:9` re-anchor (lifecycle seed→firm) resolves Issue #3; serialize the two layer-intro-author reports so both feature/* writes land in the same cycle.

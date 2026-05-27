---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T182030Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T182530Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: unrepairable
overall_status: ready
follow_up_agent: null
---

# META: critique of L1 intro refresh after constructed-operator-gate L1>L0 theme

## Critique

### Checks run

**citation-validity** — Checked all evidence pointers in Supporting evidence and Open questions / caveats. `book/src/L1-L0/ksp-solve-mutation-rotation.md` exists (cycle-008 wave-1 pass 4, present); slug confirmed on line 1; the four-sub-pattern A/B/C/D scope is confirmed in the file's "L0 form (RHS)" section. `book/src/L1-L0/index.md` row 21 confirms `ksp-solve-mutation-rotation` slug and `rough-in (firmed cycle-008)` status. `book/src/L1/ksp_solve.md` exists (cycle-007 firm) and the report correctly states it is not edited. `scaffolding/open-questions.md:1278-1288` correctly brackets the OQ frontmatter (1278-1284) and body (1286-1288) for `l1-intro-refresh-after-constructed-operator-gate`. Pass.

**surface-or-evidence** — This is a refresh dispatch with three edits to `book/src/L1/index.md`. Edit 1 (Semantics motif-4 closing sentence) and Edit 3 (Working Notes bullet) modify operator/theme surface (the L1 layer-intro text). Edit 2 (dep-map `ksp_solve` row Status parenthetical) modifies dep-map surface. All edits are additive references to already-firm artifacts (cycle-008 `ksp-solve-mutation-rotation` + its three firm sister themes); no new substantive content is asserted, no new rotation_claims are introduced. Rotation claims (timer erase, warning-to-structured-field, counter-to-driver-accumulator, destination-binding) all originate from the cycle-008 L1>L0 theme they reference, not from this refresh. Pass.

**rotation-quality** — Not applicable to a layer-intro refresh; this dispatch does not propose new algebraic / structural / reduction rotations. The four absorption rules summarized in Edit 1 and Edit 3 are quoted from the upstream `ksp-solve-mutation-rotation` theme rather than introduced here. Pass (marked as not applicable per role-spec discipline).

**variant-axis-coverage** — Not applicable to a layer-intro refresh. The variant-axis collapse for `ksp_solve` (CG/GMRES/FGMRES implemented; MINRES/BICGSTAB/DEFAULT obstruction) was settled in cycle-007's harvest and the cycle-008 L1>L0 theme; this refresh does not reopen the axis question. The existing Working Notes bullet on lines 75 (current `index.md`) — preserved untouched — continues to scope the unimplemented-stub cases out. Pass.

**cross-reference-integrity** — All four newly-added wikilinks in the three edits resolve to existing files:
- `../L1-L0/ksp-solve-mutation-rotation.md` — exists (41,933 bytes, cycle-008 wave-1 pass 4).
- `../L1-L0/apply-linop-mutation-rotation.md` — exists.
- `../L1-L0/axpby-mutation-rotation.md` — exists.
- `../L1-L0/axpbypcz-mutation-rotation.md` — exists.

The Edit-3 Working Notes bullet's relative `../L1-L0/...` paths from `book/src/L1/index.md` are correct. Concept/L0 references already-present in the surrounding bullets (`constructed-operator-factory`, `variant-absorption`, `L0/kspsolver-base-class`) are unchanged. Pass.

**edge-label-fidelity** — The report carries an L1>L0 edge label throughout (Summary, motif 4 sentence, dep-map parenthetical, Working Notes bullet). The prose in all three edits discusses exactly the L1→L0 edge: motif-4 names the four outer-composition absorption rules + sister-theme per-step decomposition; dep-map parenthetical points to the L1>L0 theme slug; Working Notes bullet describes the L1>L0 landing. No edge-label/prose mismatch. Pass.

**plan-kind-consistency** — Report declares (implicitly, via Summary phrasing) as a polish-level refresh / observation. Content shape matches: three small surface edits to a layer-intro `index.md`, no new operator/theme entries, no rotation claims, OQ closure. The dispatch shape (`layer-intro-author` refresh) is consistent with the role's broader-cycle-003 scope (layer-intro authoring includes refresh after adjacent-layer landings). Pass.

**skill-uptake-survey** — The report invokes no skills explicitly. The shape (cross-reference verification across L1/index.md, L1-L0/ksp-solve-mutation-rotation.md, L1-L0/index.md, scaffolding/open-questions.md, plus 4 new wikilinks) plausibly fits `verify-citation-range` (each citation `file:line-range` should be confirmed in-range). The skill is not blocking — the Supporting evidence section does perform manual cross-reference verification — but a `skill-selection`-style note explaining why `verify-citation-range` was not invoked (e.g., "single OQ citation, single new theme cross-reference, manual verify adequate") would surface the telemetry. Warning (telemetry only, not blocking).

### Issues found

1. **First-precedent claim verification — `Status`-column parenthetical for L_n→L_n>L_{n-1} cross-link** (CYCLE.md "Open questions / caveats" §2). The report flags Edit 2's choice of parenthetical-in-Status-cell as the first precedent for cross-linking from an L_n dep-map row into its L_n>L_{n-1} theme. **Verification**: the existing precedents in `book/src/L4/index.md:30` (krylov-step row) and `book/src/L2/index.md:23` (krylov-step row) both cross-link to lowering themes, but via the **Dependencies** column ("Lowers to L2 via L4>L3>L2…", "L1: apply_linop, axpy…"), not via the **Status** column. So the report's "first precedent" framing is **narrowly correct** — Status-column parenthetical is novel — but it is **not** the first cross-link from an L_n dep-map row into a lowering theme. The caveat phrasing could be slightly tighter: "first cross-link to live in the Status column rather than the Dependencies column" would be more accurate than "first precedent for cross-linking". Severity: low. Location: CYCLE.md:93-103.

2. **Skill-selection telemetry absent** (CYCLE.md whole). No skill was invoked or explicitly skipped-with-rationale. For a polish-level dispatch this is low-stakes, but a `skill-selection`-style two-line note ("Skills considered: verify-citation-range — skipped, single new cross-reference manually verified") would surface uptake telemetry. Severity: low. Location: CYCLE.md (no Skills-considered section present).

3. **Edit 2 Status-cell punctuation/structure** (CYCLE.md:42-44). The replacement Status cell becomes `firm` (L1>L0: [slug-link], cycle-008)` which embeds a markdown link inside a markdown-table cell with parentheses; this is valid markdown but is visually dense in a narrow Status column. The report's own caveat §2 acknowledges the structural concern (parenthetical-in-Status may need column-split if multiple L1>L0 themes per L1 operator emerge). Not a blocker — currently 1:1 — but worth flagging as a pre-existing-acknowledged shape concern that integrator-finalize's `cargo make book` rendering should be eyeballed for in mdBook output. Severity: low. Location: CYCLE.md:42-44 (the Edit 2 new-string).

4. **Edit 1 sentence length** (CYCLE.md:37-38). The added sentence appended to motif 4 grows the motif-4 paragraph from ~80 words to ~135 words and folds in five distinct bracketed wikilinks + four named absorption rules in a single sentence. The information is correct (all four absorption rules trace to the cycle-008 L1>L0 theme; all four wikilinks resolve), but readability is borderline. Could be split into two sentences (the new wikilink-bearing sentence is self-contained and would read more cleanly as a separate "Lowering" trailing sentence). Severity: low (stylistic, not correctness). Location: CYCLE.md:37-38 (the Edit 1 new-string).

## Repair

### Fixes attempted

- **Finding 1 — "first precedent" caveat is narrowly imprecise** (CYCLE.md:93-103, Open questions / caveats §2).
  - **Decision**: repaired.
  - **Action**: Rewrote the caveat in `CYCLE.md` Open questions / caveats §2 to frame the novelty as "first cross-link to live in the Status column" rather than "first precedent for cross-linking from an L_n dep-map row into its L_n>L_{n-1} theme". Added explicit pointers to the existing Dependencies-column precedents at `book/src/L4/index.md:30` and `book/src/L2/index.md:23` (both krylov-step rows). Underlying dep-map shape choice and downstream concern (parenthetical-in-Status form at risk of duplication if multi-theme-per-operator emerges) preserved.

- **Finding 2 — skill-selection telemetry absent** (CYCLE.md whole).
  - **Decision**: unrepairable.
  - **Rationale**: Adding a Skills-considered section (even a two-line "skills considered: X — skipped because Y" note) is authoring new content, not surgical fix. The critic explicitly noted this is non-blocking ("warning, telemetry only, not blocking"). Defer to `layer-intro-author` role-spec evolution or a future skill-uptake-survey-driven refresh; not a repair-authority task.

- **Finding 3 — Edit 2 Status-cell structural density** (CYCLE.md:42-44).
  - **Decision**: repaired.
  - **Action**: Appended a new caveat bullet to CYCLE.md Open questions / caveats that explicitly flags the parenthetical-in-Status markdown-link form as visually dense and asks integrator-finalize's `cargo make book` render to be eyeballed. Did NOT restructure the dep-map cell itself (would be content-authoring — the report's own caveat §2 acknowledges 1:1 mapping is the agreed shape pending the second L1>L0 theme per operator).

- **Finding 4 — Edit 1 motif-4 sentence length** (CYCLE.md:37-38).
  - **Decision**: repaired.
  - **Action**: Split the long motif-4 sentence into two sentences in the Edit-1 `[new]` block. The "first L1>L0 theme for a structured opaque primary argument" anchor becomes a self-contained sentence; the four-primitive / four-absorption-rule decomposition becomes a separate trailing sentence. All four wikilinks and all four absorption rule names preserved; no semantic change.

### Unrepairable findings

- Finding 2 (skill-selection telemetry): defer to role-spec evolution. No follow-up agent dispatched — the critic check was a non-blocking warning and the absent telemetry is a methodology-level concern, not a content gap. Follow-up agent: null.

## Suggested resolution

`overall_status: ready` — all blocking findings (none from the 8 checks; 3 of 4 low-severity issues) are repaired in-place; the one unrepairable item is a non-blocking telemetry warning. Integrator-per-report may apply the three edits to `book/src/L1/index.md` as-is. Integrator-finalize should eyeball the `cargo make book` mdBook rendering of the dep-map row 8 (`ksp_solve`) Status cell to confirm the parenthetical-in-Status markdown link renders cleanly (per the new caveat). The OQ `l1-intro-refresh-after-constructed-operator-gate` should be marked closed.

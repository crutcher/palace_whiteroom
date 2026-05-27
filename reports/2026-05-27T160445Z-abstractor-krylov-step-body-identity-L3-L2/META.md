---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T16:17:05Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: warning
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: warning
repaired_at: 2026-05-27T16:30:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: repaired
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: unrepairable
overall_status: ready
follow_up_agent: null
---

# META: verification of CYCLE — L3>L2 theme sketch — krylov-step-body-identity

## Critique

### Checks run

**citation-validity** — `pass`. Every cited evidence range was spot-verified:

- `book/src/spec/slices/cg.md:341-362` — Claim 2 "step body lifts as identity" present (verbatim "identity in form" appears at line 360). In-range and accurately characterized.
- `book/src/spec/slices/arnoldi_step.md:178-213` — three uncontested primitives (`apply_BA`, `subdiag_norm`, `normalize`) at lines 184-190 and the MGS-orthog sequential-obstruction at lines 192-213. The report's claim that "the obstruction is below the kernel body" is supported by the cited text (the obstruction is inside the `op.orthog` primitive under MGS variant).
- `book/src/spec/slices/chebyshev.md:354-362` — `innerStep` body present (lines 355-362) with `applyLinop`, `op.scalars k st`, and field-algebra updates. Confirms five-primitive-group shape claim.
- `book/src/spec/slices/gmres.md:459-471` — `inner_loop` body present with `apply_BA`, `orthogonalize`, `ls_update_column`, and the `modify (\s -> s{ it = s.it + 1 })` line. Matches the claim.
- `book/src/L2/krylov-step.md` §Semantics — lines 38-66 contain the body shape the report references; the report's reproduction (lines 91-101 of the proposed CREATE) matches the L2 source textually.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"L3 form (RHS)" — lines 55-89 contain the L3 form the report references as LHS; reproduction in the CREATE block (lines 64-75) is textually faithful, including the `s' = s { it = s.it + 1 }` line.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"Audit of cycle-002 identity-in-form claim" — lines 169-187 contain the audit verdict; the report's "confirmed-with-refinement" characterization is accurate.
- All four OQ slugs (`krylov-step-body-identity-theme-pending-cycle-007`, `krylov-step-l3-identity-in-form-audit-closure-cycle-006`, `iterate-while-l4-anchor-missing`, `iterate-while-l3-rendering-trajectory-accumulation-gap`) resolve in `scaffolding/open-questions.md`.

Citation format follows the in-tree convention (`book/src/...` and `reports/...` paths, not strict `reference/`-relative); CLAUDE.md prescribes `relative/path/file.ext:start-end` *relative to `reference/`* for Palace source. The report cites artifact-internal evidence (slice corpus and L-layer files), which the project routinely renders as `book/src/...` paths. Cycle-006's wrapper-dissolution theme uses the same convention. This is consistent with existing practice — not a citation-validity defect.

**surface-or-evidence** — `pass`. The proposal authors a NEW L3>L2 theme entry (surface creation) AND houses substantive evidence (the cycle-006 audit verdict). It is not a "pure rotation_claim without surface" report — the CREATE block adds a real chapter to `book/src/L3-L2/`, the index gets a new theme-list row, SUMMARY.md gets a chapter entry, and the relevant OQ closes. The justification of `empirical-match` is supported by the cycle-002 evidence + cycle-006 audit re-confirmation.

**rotation-quality** — `warning`. The proposal explicitly declares the body's primitive sequence is identity-in-form across the L3>L2 edge, and the §"Rewrite shape" table is a line-for-line 1:1 mapping. Per the rotation-quality check, "1:1 mappings = fail (not a rotation)" — and the report itself names this as identity. The defense the report offers is that the two declared wrapper-level surface adjustments ((1) `(K, s)` → unified `IterState`; (2) tail-recursive `iterate_while_L3` → outer-driver-by-role) constitute the rotation work, and that these are state-hiding / coarser-substitution / threaded-state-compression-style rotations (which the rotation-quality rubric grants `pass`). Assessment: the IterState consolidation IS a state-hiding rotation (the L3 ephemeral-vs-persistent typing distinction is erased, ephemeral `K` and persistent `s` collapse into one record) and the outer-loop→outer-driver-by-role IS a coarser-substitution / abstraction-by-role rotation. **But**: these rotations live "at the wrapper" by the report's own framing, and the *body* — which is what the theme's name and primary content address — is explicitly the identity. A pure "identity-in-form on the body" theme without independent body-level rotation work is a borderline case for the rotation-quality criterion. The report defends this in Open-questions-caveat 5 ("short by design"). The honest reading: this theme is a **ratification housing**, not a new rotation. Whether that's an acceptable shape for an L3>L2 theme entry is a methodology judgment that exceeds the checklist; flagging as warning so the repairer / integrator can weigh it.

**variant-axis-coverage** — `pass`. The proposal addresses the six known variant axes explicitly in §"Applicability conditions" item 4 ("variant-axis profile is closed at six"), and states that all six are absorbed identically at L2 and at L3 through the `op.*` constructed-operator surfaces. The MGS-orthog sequential obstruction is correctly localised below the body (as a property of the `op.orthog` primitive, not of the `krylov-step` body), and the Form-A/Form-B distinction is addressed in §"L3 form (LHS)". No hidden variant branches.

**cross-reference-integrity** — `pass`. All internal links resolve:

- `../L2/krylov-step.md` — exists, content matches.
- `../L4/krylov-step.md` — exists.
- `../L4-L3/krylov-step-typed-wrapper-dissolution.md` — exists, references match.
- All `../concepts/` references (`state-stratification`, `derived-view-hoisting`, `variant-absorption`, `first-iteration-unrolling`, `sequential-obstruction`) resolve to existing concept pages.
- The `level (b)/(c)` terminology used in caveat 1 ("level-(b)/(c) absorption discipline") matches `concepts/variant-absorption.md`'s three-level taxonomy.
- The OQ slug references resolve.
- The slice corpus paths (`book/src/spec/slices/cg.md`, `arnoldi_step.md`, `chebyshev.md`, `gmres.md`) all exist with the cited content.

**edge-label-fidelity** — `pass`. The proposal carries edge label L3>L2 (per the theme's directory placement and the proposed-changes filename `book/src/L3-L2/krylov-step-body-identity.md`). The prose throughout discusses the L3>L2 edge: the L3 form is the LHS, the L2 form is the RHS, the rotation direction is L3→L2 (with abstraction-direction note in §"Justification kind" confirming L3 is higher-abstraction for this edge and L2 is lower-abstraction). No edge-label / discussion mismatch.

**plan-kind-consistency** — `warning`. The proposal declares status `firm` in both the report frontmatter (implicitly, via the §Status field of the CREATE block: "`firm` — the theme ratifies the cycle-006 audit's confirmed-with-refinement verdict") and in the index theme-list row ("`firm` (cycle-007 abstractor; ratifies cycle-006 audit verdict)"). However, the abstractor agent's typical output shape is `rough-in` or `firm-rough-in`; this theme self-declares `firm` on first emission. The upstream theme `krylov-step-typed-wrapper-dissolution` (cycle-006) is itself `rough-in` per its §Status line 215 (`rough-in` — the theme's rewrite shape is sketched...). Promoting a downstream theme to `firm` while its upstream LHS-source remains `rough-in` is a plan-kind-consistency anomaly: a `firm` theme should not depend on a `rough-in` LHS form for its substantive content. The report's defense is in caveat 5 and §Status ("the substantive verification is the cycle-006 audit"), but the cycle-006 audit was integrated as the audit-section of a `rough-in` theme, not as `firm` content. Flagging as warning — the status declaration may need to be `firm-rough-in` (inheriting the LHS's rough-in status) until the L4>L3 theme is itself promoted to `firm`.

**skill-uptake-survey** — `warning`. The report's shape (theme ratification + line-by-line mapping table + justification-kind selection) is exactly the kind of work the existing skills are designed to support. The report does not reference invocation of:

- `verify-citation-range` — would have applied to the four cited slice-corpus ranges plus the four L-layer-internal references.
- `verify-refinement-surface` — would have applied to whether the proposal is "surface or evidence" (this is a refinement of the existing L3>L2 layer with new theme entry).
- `classify-variant-axis` — would have applied to the §"Applicability conditions" item 4 closure-of-six-axes claim.
- `verify-rotation-citation` — would have applied to the rotation-quality assessment.

No skill invocations are mentioned in the dispatch. This is a telemetry observation, not a blocking finding — the report's content quality is independent of whether the dispatch invoked skills procedurally. But the recurrent pattern of abstractor reports not surfacing skill invocations is worth flagging.

### Issues found

1. **(rotation-quality, severity: medium)** §"Rewrite shape" presents the body-level mapping as a line-for-line 1:1 identity table (lines 115-122 of the CREATE block, 6 rows), with the rotation work explicitly placed "at the wrapper around the body" via the two declared surface adjustments. The rotation-quality rubric grants `pass` for state-hiding / coarser-substitution rotations and `fail` for pure 1:1 renaming. The IterState consolidation (`(K, s)` → unified `IterState`) IS a state-hiding rotation, but it is delimited to the wrapper, and the body itself is named as identity-in-form. The theme's substantive justification leans on the cycle-006 audit, which is the actual rotation analysis; this theme is a structural housing of that verdict. Severity is medium because the report explicitly defends its shape in caveat 5, the upstream audit is real rotation work, and the housing-in-`book/src/L3-L2/` rationale is structural (symmetric coverage of the lowering chain). The flag is to surface this for repairer / integrator weighing, not to recommend rejection.

2. **(plan-kind-consistency, severity: medium)** The status declaration is `firm` on first emission (CYCLE.md frontmatter line 30, CREATE block §Status line 191, index row line 214). The upstream theme `krylov-step-typed-wrapper-dissolution` is `rough-in` per its §Status. A downstream theme that references a rough-in LHS form for its substantive content should not be `firm`; it should be `firm-rough-in` (firm in its own ratification work, rough-in inherited from the LHS-source's current status). Consider downgrading the §Status declaration to `firm-rough-in` or annotating the dependency: "firm-on-ratification; LHS form inherited from the cycle-006 L4>L3 theme's rough-in §"L3 form (RHS)" status".

3. **(plan-kind-consistency, severity: low)** The CYCLE.md frontmatter `status: pending` (line 4) is inconsistent with the §Status field inside the CREATE block declaring `firm` (line 191). The frontmatter is the dispatch-level status (pending integration); the chapter §Status is the content-status. The dual status fields are not in conflict by convention, but the choice to declare `firm` for the chapter while the dispatch is `pending` warrants explicit alignment. Recommend either: (a) the CYCLE.md frontmatter notes that the chapter status is `firm` (or `firm-rough-in` per Finding 2), or (b) the CREATE block's §Status acknowledges the dispatch is `pending` integration.

4. **(skill-uptake-survey, severity: low)** No skill invocations are mentioned in the dispatch despite multiple skills applying to the report's shape (`verify-citation-range`, `verify-refinement-surface`, `classify-variant-axis`, `verify-rotation-citation`). Telemetry only — the report's quality is independent of skill-invocation surfacing. If skill-uptake telemetry is being tracked (per the cycle-006 meta-phase friction-ledger discussion), this is a recurring gap in abstractor reports worth noting.

5. **(rotation-quality, severity: low)** The §"Rewrite shape" item 1 claim that the (K, s) → IterState consolidation is "information-preserving — no field is added, no field is dropped, no field's interpretation changes" is asserted but not independently verified by line-level evidence in this dispatch. The cycle-006 audit confirmed body-level identity-in-form, but the IterState field-by-field correspondence between L3's `(K, s)` pair and L2's unified IterState is a separate consolidation claim. The L2 entry §Signature (lines 14-32 of `book/src/L2/krylov-step.md`) does enumerate the three strata as fields of `IterState`, which supports the report's claim, but the L3 form's `K` fields (`K.<input_field>`, `K.V_prefix`, `K.scalar_state`, `K.k`) are referenced through positional accessors only — the field-by-field mapping is not explicitly tabulated in either the report or the cycle-006 theme. A lowering-verifier follow-up could close this gap; the report's §Status already names this as a cycle-008+ candidate.

6. **(citation-validity, severity: very low)** §"Verified-against" cites `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"L3 form (RHS)" (lines 56-89) — the actual range in the source file is lines 55-89 (the §"L3 form (RHS)" header is at line 55). Off-by-one on the start line. The §"Audit of cycle-002 identity-in-form claim" citation (lines 169-187) matches the source exactly. Minor.

7. **(skill-uptake-survey, severity: very low)** The report includes a §"L3>L2 vs L4>L3 distinction" section (lines 195-204 of the CREATE block) that is a useful comparison aid. This section's content overlaps with the cycle-006 audit's "L4>L3>L2 step-body chain is identity-in-form" framing and could be a candidate for promoting to a small concept page (e.g., `concepts/lowering-chain-labour-division.md`) if the pattern recurs in subsequent lowering-chain themes. Not actionable now — pattern observation only.

## Repair

### Fixes attempted

- **Finding 1 (rotation-quality, medium)**: Body-level mapping is identity-in-form; rotation work is at wrapper-level (IterState consolidation + outer-driver-by-role).
  - **Decision**: repaired (clarifying edit, not substantive re-authoring).
  - **Action**: rewrote the chapter intro paragraph of the CREATE block (`book/src/L3-L2/krylov-step-body-identity.md` opening sentence) to make the body-identity / wrapper-rotation split explicit upfront, naming the two wrapper-level rotations by rotation-quality kind (state-hiding; abstraction-by-role). The defense in caveat 5 ("short by design") is left as-is. The rotation-quality rubric grants `pass` for state-hiding / coarser-substitution rotations; making this explicit in the intro converts the warning from a reading-order issue (reader has to reach caveat 5 to see the defense) into a self-evident framing.
  - **Rationale on not deferring**: the critic explicitly noted the report's defense in caveat 5 is sound (state-hiding IterState consolidation IS a real rotation); the warning was that the body-vs-wrapper distinction needed surfacing earlier. A surgical intro-paragraph edit is mechanical, not substantive authoring.

- **Finding 2 (plan-kind-consistency, medium)**: `firm` declared while upstream `krylov-step-typed-wrapper-dissolution` is `rough-in`.
  - **Decision**: repaired.
  - **Action**: Verified upstream status by reading `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` line 216 — confirmed `rough-in` (not `firm-rough-in` as the CYCLE.md inputs frontmatter line 10 had mischaracterized). Downgraded all four status declarations to `firm-rough-in` with inheritance annotation:
    - CYCLE.md Summary line 30 (Status declaration in summary)
    - CYCLE.md Context bullet line 53 ("L3>L2 firm — this theme" → "L3>L2 firm-rough-in — this theme") with inheritance explanation appended
    - CYCLE.md CREATE block §Status (line 191 of original) — replaced "`firm`" with "`firm-rough-in`" plus full inheritance paragraph explaining the rough-in component is inherited from the upstream L4>L3 theme
    - CYCLE.md proposed index-row edit (line 214 of original) — replaced "`firm` (cycle-007 abstractor; ratifies cycle-006 audit verdict)" with "`firm-rough-in` (cycle-007 abstractor; ratifies cycle-006 audit verdict; `rough-in` inherited from upstream L4>L3 theme whose status is `rough-in`)"
  - **Rationale on not deferring**: the inheritance pattern is exactly what the critic suggested; the source-of-truth for the upstream's status is the upstream file itself (read directly, not interpreted), and the textual edit is mechanical.

- **Finding 3 (plan-kind-consistency, low)**: CYCLE.md frontmatter `status: pending` vs CREATE block §Status `firm`.
  - **Decision**: not-needed (different fields by convention).
  - **Action**: none. The CYCLE.md frontmatter `status: pending` is the dispatch-level status (pre-integration); the §Status field in the CREATE block is the theme/content-level status declaration. The two fields are not in conflict per project convention — the critic acknowledged this in the finding text ("The dual status fields are not in conflict by convention"). Now that the §Status has been updated to `firm-rough-in` per Finding 2, the explicit alignment is: dispatch is `pending` integration; the content being proposed declares itself `firm-rough-in`. No further edit needed.

- **Finding 4 (skill-uptake-survey, low)**: No skill invocations mentioned.
  - **Decision**: unrepairable (telemetry; no actionable fix at the repair level).
  - **Rationale**: this is a recurring pattern across abstractor reports (the critic flagged it as such), addressable only at the meta-phase level by either (a) tightening the abstractor agent prompt to require explicit skill-invocation logging, or (b) building a skill-uptake telemetry harness. Both are out of repair authority.

- **Finding 5 (rotation-quality, low)**: IterState consolidation "information-preserving" claim is asserted but not field-by-field tabulated.
  - **Decision**: not-needed (already flagged by the report itself as a cycle-008+ lowering-verifier follow-up).
  - **Action**: none. The report's §Status section explicitly names a "Lowering-verifier follow-up (cycle-008+ candidate)" — the field-by-field tabulation is the natural scope for that follow-up dispatch. Adding the tabulation now would be substantive authoring (out of repair authority); deferring to lowering-verifier is the right routing.

- **Finding 6 (citation-validity, very low)**: Off-by-one — `wrapper-dissolution` §"L3 form (RHS)" cited as lines 56-89; actual range is 55-89 (header at line 55).
  - **Decision**: repaired.
  - **Action**: Verified by direct read of `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` — §"L3 form (RHS)" header is at line 55, content extends to line 89. Corrected CYCLE.md §"Verified-against" L4/L3 evidence block to cite `lines 55-89` instead of `lines 56-89`. Also corrected the upstream-status mischaracterization adjacent to the citation (the inline note said the form is "the firm-rough-in RHS of that theme" — actual upstream is `rough-in`, not `firm-rough-in`; this is the same mismatch as Finding 2). Updated to "the RHS of that theme (the upstream theme is currently `rough-in` per its §Status line 216)".
  - **Rationale**: mechanical line-range correction with direct source verification.

- **Finding 7 (skill-uptake-survey, very low)**: §"L3>L2 vs L4>L3 distinction" section is a candidate concept-page promotion if pattern recurs.
  - **Decision**: not-needed (pattern observation; not currently actionable).
  - **Rationale**: critic explicitly flagged as "not actionable now — pattern observation only." If the pattern recurs in subsequent lowering-chain themes, a future abstractor or meta-phase can propose the concept-page promotion.

### Unrepairable findings

- **Finding 4 (skill-uptake-survey)** — recurring telemetry gap across abstractor dispatches; meta-phase concern (agent-prompt tightening or telemetry harness), not per-report repair. No follow-up agent at this dispatch level.

## Suggested resolution

`ready` — all rotation-quality and plan-kind-consistency findings have been addressed via mechanical edits: the body-vs-wrapper rotation framing is now surfaced in the chapter intro (Finding 1), the status declarations consistently use `firm-rough-in` with inheritance annotations (Finding 2), and the citation off-by-one is corrected (Finding 6). The unrepairable skill-uptake-survey gap (Finding 4) is telemetry only and does not block integration. Findings 3, 5, 7 are not-needed per the analysis above.

Integrator notes:
- The integrator's per-report apply will write `book/src/L3-L2/krylov-step-body-identity.md` with the updated CREATE block (status: `firm-rough-in`, clarified intro paragraph) and update `book/src/L3-L2/index.md` with the `firm-rough-in` theme-list row.
- When the upstream `krylov-step-typed-wrapper-dissolution` theme is promoted to `firm` (likely on completion of its `lowering-verifier` follow-up), a small follow-up edit can promote this theme to plain `firm` without further audit work — the dependency is purely status-inheritance.
- The cycle-008+ lowering-verifier dispatch on the L3>L2 hop (named in §Status) is the natural place to add the field-by-field IterState correspondence tabulation that Finding 5 surfaces.

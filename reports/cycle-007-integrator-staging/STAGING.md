# cycle-007 integrator-per-report staging log

Append-only per-report integration log for cycle-007 wave-1 + wave-2. Each per-report integrator appends one section below; integrator-finalize reads this log to drive the cycle-end rebuild + commit + housekeeping.

## 2026-05-27T160728Z-layer-intro-author-L0-bootstrap-bundle-3
applied_at: 2026-05-27T17:00:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L0/mfem-wrapper-solver.md (create)
- book/src/L0/linalg-iterative-file.md (create)
- book/src/L0/mutable-workspace-pattern.md (create)
- book/src/L0/index.md (edit — Reference-note cohort: 3 new dep-map rows across Conventions / File overviews / Overload sets and class interfaces, alphabetical-within-grouping)
- book/src/SUMMARY.md (edit — L0 Part: 3 new entries inserted in alphabetical position within each grouping)
- scaffolding/open-questions.md (append — 4 new entries: `mfem-wrapper-solver-l4-complex-from-real-lift-backref`, `iterative-file-helper-citation-granularity`, `eigensolver-wrapper-l0-bundle-4-candidate`, `mutable-workspace-category-4-split-decision`)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0
- bookkeeping incomplete: 0
- SUMMARY.md chapter registration auto-fix: 0 (report explicitly proposed the SUMMARY edits)
- index-placeholder displacement auto-fix: 0 (the existing dep-map sections already had firm rows; the inserts extend the existing alphabetical lists)

Open questions promoted:
- mfem-wrapper-solver-l4-complex-from-real-lift-backref
- iterative-file-helper-citation-granularity
- eigensolver-wrapper-l0-bundle-4-candidate
- mutable-workspace-category-4-split-decision

Build-relevant: yes

Notes:
- All three new L0 chapter files were authored by the layer-intro-author and repaired by the repairer in-place in the report directory (citation-validity FAIL → all 4 scrambled helper citations + missing 5th helper + `OrthogonalizeColumn` → `OrthogonalizeIteration` corrections + `floquetcorrection.hpp:35-65` → `:32-60` range fix + `solver.hpp:84-94` Evidence-bullet clarification + `MfemWrapperSolver` eight-call-sites → eleven-call-sites count fix). The integrator copied the live repaired versions from the report dir into `book/src/L0/`.
- Cross-references verified pre-apply: `concepts/{complex-from-real-lift, solver-as-operator, solve-monad, incremental-least-squares}.md`, `L2/krylov-step.md`, `L1-L0/apply-linop-mutation-rotation.md` all exist.
- Existing L0 sibling chapters (`apply-linop-overload-set.md`, `kspsolver-base-class.md`, `ksp-factory-file.md`, `transparent-vs-load-bearing-tricks.md`, `output-arg-vs-receiver.md`, `linalg-vector-file.md`, `linalg-free-functions.md`, `mfem-vector-types.md`) all present in `book/src/L0/` pre-apply; the three new chapters slot in alongside them.
- Deferred `integrated_at:` to finalize per role-spec (per-report integrator does not touch consumed-report frontmatter; that's integrator-finalize's responsibility).
- No critic/repairer skill issues with this apply — the dispatch was a 6-block proposed-changes set (3 file creates + 2 in-place edits + 0 deletes). Mechanical apply.
- 5 cycle-007 wave-1 reports total; this is per-report dispatch 1 of 5. Wave-2 (lowering-verifier `iterate_while`) is separate per the cycle-007 plan.

---

## 2026-05-27T160711Z-harvester-l1-ksp-solve
applied_at: 2026-05-27T17:30:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/ksp_solve.md (create)
- book/src/L1/index.md (edit — Context section: added 6th bullet on construction-bound solver state; Semantics overlay: 3→4 motifs with new motif 4 "Constructed-operator absorption"; Vocabulary cohort: Firm (7)→Firm (8) with `ksp_solve` row; Operator dep-map: new `ksp_solve` row inserted after `axpbypcz`; Working Notes: new bullet describing `ksp_solve` as first firm L1 operator with structured opaque primary argument)
- book/src/SUMMARY.md (edit — L1 Part: added `[ksp_solve](./L1/ksp_solve.md)` entry after `axpbypcz`, preserving pass-1's L0-Part edits)
- scaffolding/open-questions.md (append — 3 new entries: `ksp-solve-concept-page-signature-update`, `ksp-solve-mutation-rotation-l1-l0-theme`, `l1-intro-refresh-after-constructed-operator-gate`)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate check to integrator-finalize; this report did not modify any prior-cycle slice content)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0 (N/A — L1 operator chapter, not a lowering theme)
- H1 reuses page heading: 0 (chapter H1 `# ksp_solve` distinct from SUMMARY entry text)
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (3 exposed + 1 collapsed axis declared with `palace/linalg/ksp.{hpp,cpp}` citations)
- bookkeeping incomplete: 0
- SUMMARY.md chapter registration auto-fix: 0 (report explicitly proposed the SUMMARY edit)
- index-placeholder displacement auto-fix: 0 (L1/index.md had no placeholder; existing dep-map / cohort / motifs already populated)

Open questions promoted:
- ksp-solve-concept-page-signature-update
- ksp-solve-mutation-rotation-l1-l0-theme
- l1-intro-refresh-after-constructed-operator-gate

Build-relevant: yes

Notes:
- All cross-reference targets verified pre-apply (8 internal book links from the new L1 chapter): `L0/kspsolver-base-class.md`, `L0/ksp-factory-file.md`, `L0/apply-linop-overload-set.md`, `L2/krylov-step.md`, `L1-L0/{minres-iteration,bicgstab-iteration}.md`, `concepts/{ksp_solve,solve-monad,solver-as-operator,constructed-operators,variant-absorption,constructed-operator-factory}.md`, `spec/slices/divfree.md`, and the 4 sibling L1 entries (`apply_linop`, `axpy`, `dot`, `nrm2`). All exist.
- The repairer's three repairs were already baked into the CYCLE.md content I read: (a) the 3 OQ blocks were in canonical YAML+paragraph format ready for direct append; (b) citation `iterative.cpp:544-705` (corrected from the over-reach `544-734`) appears in three places within the L1 chapter (Dependencies §, Evidence §, plus the report's Supporting evidence note); (c) the skill-uptake telemetry paragraphs were present in the Open questions / caveats section. No additional integrator-side translation needed.
- SUMMARY.md edit was non-conflicting with pass-1's edits — pass-1 touched the L0 Part (3 alphabetical inserts: `linalg-iterative-file`, `mfem-wrapper-solver`, `mutable-workspace-pattern`), this pass touched the L1 Part (1 append at end of L1 cohort). Re-read disk at edit time confirmed pass-1's L0 entries are present and undisturbed; the L1 insert leaves them intact.
- L1/index.md edit was non-conflicting with prior in-cycle state — the file had not been touched by pass-1 (which touched only `book/src/L0/index.md`, the 3 new L0 chapter creates, SUMMARY, and open-questions). Re-read disk at edit time confirmed the file was at its pre-cycle-007 state ("Firm (7)", 3 motifs, no `ksp_solve` rows).
- Closes cycle-006 OQ `l1-ksp-solve-firm-up-anchor-ready` per the report's closure note. The OQ closure itself is integrator-finalize's responsibility (per the open-questions ledger update conventions — the per-report integrator promotes new OQs but does not mark closures on existing ones; finalize sees the full set of closures across the cycle).
- Deferred `integrated_at:` and `integration_commit:` to finalize per role-spec (per-report integrator does not touch consumed-report frontmatter; that's integrator-finalize's responsibility per CLAUDE.md §Write-authority partition + cycle-006 friction `integrated-at-write-authority-drift`).
- 5 cycle-007 wave-1 reports total; this is per-report dispatch 2 of 5.

---

## 2026-05-27T160553Z-layer-intro-author-L1-context-thinning-sweep
applied_at: 2026-05-27T18:00:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/axpy.md (edit — Context section: 1-paragraph thinning, replaced inline `y.Add(α, x)` / `y.AXPY(α, x)` member-vs-free-fn enumeration with explicit cross-references into 4 L0 chapters [`linalg-vector-file`, `output-arg-vs-receiver`, `mfem-vector-types`, `transparent-vs-load-bearing-tricks`])
- book/src/L1/dot.md (edit — Context section: 5-bullet → 1-paragraph thinning, cross-refs into 4 L0 chapters [`linalg-vector-file`, `linalg-free-functions`, `mfem-vector-types`, `transparent-vs-load-bearing-tricks`])
- book/src/L1/nrm2.md (edit — Context section: 3-bullet → 1-paragraph thinning, cross-refs into 4 L0 chapters [`linalg-vector-file`, `linalg-free-functions`, `mfem-vector-types`, `transparent-vs-load-bearing-tricks`]; B-weighted aside preserved; stale `apply` → `apply_linop` reference fix in the B-weighted aside)
- book/src/L1/axpby.md (edit — Context section: bullet-enumeration → 1-paragraph thinning, cross-refs into 5 L0 chapters [`linalg-vector-file`, `output-arg-vs-receiver`, `linalg-free-functions`, `mfem-vector-types`, `transparent-vs-load-bearing-tricks`]; supersession provenance paragraph preserved)
- book/src/L1/scal.md (edit — Context section: bullet-enumeration + "no linalg::Scal" paragraph → 1-paragraph thinning, cross-refs into 4 L0 chapters [`linalg-free-functions` for the notable-absence, `output-arg-vs-receiver`, `mfem-vector-types`, `transparent-vs-load-bearing-tricks`])
- book/src/L1/apply_linop.md (edit — Context section: multi-bullet virtual-method-family enumeration → 1-paragraph thinning, cross-refs into 4 L0 chapters [`apply-linop-overload-set`, `output-arg-vs-receiver`, `mfem-vector-types`, `transparent-vs-load-bearing-tricks`]; BaseProductOperator::z workspace mention preserved)
- book/src/L1/axpbypcz.md (edit — Context section: multi-bullet 3-specialisation enumeration → 1-paragraph thinning, cross-refs into 5 L0 chapters [`linalg-vector-file`, `output-arg-vs-receiver`, `linalg-free-functions`, `mfem-vector-types`, `transparent-vs-load-bearing-tricks`])

Gate hits:
- retroactive-budget per-slice: 0 (within-L1 housekeeping, not retroactive cross-slice revision)
- retroactive-budget global: 0 (defer aggregate check to integrator-finalize; this report did not modify any prior-cycle artifact beyond Context-section prose tightening of existing-firm chapters)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0 (all 6 L0 cross-ref targets verified present pre-apply)
- edge-label / prose mismatch: 0 (N/A — within-L1 housekeeping, no L_{n+1}→L_n edge label asserted)
- H1 reuses page heading: 0 (no H1 edits; only `## Context` body)
- append on missing slug: 0 (in-place Context edits on existing slugs)
- variant-axis missing on multi-variant operator: 0 (Variant-axis sections untouched — all out of Context-section scope)
- bookkeeping incomplete: 0 (proposed-changes Files block is self-consistent; no L1/index.md / SUMMARY.md edits proposed because dep-map structure is unaffected by Context-section thinning)
- SUMMARY.md chapter registration auto-fix: 0 (no new chapter creations; all 7 chapters are existing-firm)
- index-placeholder displacement auto-fix: 0 (no index.md edits; L1/index.md is at the post-pass-2 state with `ksp_solve` row + Firm (8) cohort, untouched here)

Open questions promoted:
- (none — sweep is mechanical re-routing of existing material; the stale-forward-declaration follow-up flagged in CYCLE.md is a suggested next-cycle dispatch, not an OQ; the concept-page-nrm2 inconsistency note is preserved within `nrm2.md`'s existing caveat and not promoted)

Build-relevant: yes

Notes:
- All 7 [old] blocks verified to match each L1 chapter's current Context section pre-apply (line-by-line). The repairer's 3 in-report tightenings (citation-chain prose in dot section, shrink-table recount with old 82 / new 37 / ≈ 55% net shrink totals, matrix annotation for the two `—` cells in the apply_linop row) did not affect the 7 [new] blocks — those remained as authored.
- The single load-bearing prose edit beyond pure removal: in `nrm2.md`, the B-weighted-aside paragraph's stale `apply` reference is updated to `apply_linop` (the firm L1 name landed cycle-004/005). This was an explicit micro-improvement in the report's [new] block, not a separate change.
- Cross-reference targets verified pre-apply: all 6 referenced L0 chapters (`linalg-vector-file`, `output-arg-vs-receiver`, `mfem-vector-types`, `transparent-vs-load-bearing-tricks`, `linalg-free-functions`, `apply-linop-overload-set`) present in `book/src/L0/` at the time of apply. All 7 `concepts/<slug>` references in the preserved-paragraph block (`axpy`, `dot`, `nrm2`, `scal`, `apply_linop`) are unchanged from the pre-existing Context sections.
- Citation-chain preservation verified per chapter: every L0 file range removed from each L1 Context section is retained in either (a) the L1 chapter's Evidence section (untouched by this sweep) or (b) the relevant L0 chapter's Evidence-representative block, per the report's per-chapter Citation-chain check paragraphs (which the critic verified at the pass level).
- No L1/index.md or SUMMARY.md edits proposed or made — the dep-map / cohort / motifs structure of `book/src/L1/index.md` is unaffected by Context-section thinning per the report's "No L1-index.md edit required" note. Re-read disk before/after edits confirmed pass-2's L1/index.md state (Firm (8) cohort, `ksp_solve` dep-map row, Working Notes bullet) and pass-2's SUMMARY.md state (L1 Part with `ksp_solve` entry + pass-1's L0 entries) remain undisturbed.
- Stale-forward-declaration follow-up: the report flags that after this sweep integrates, 5 L0 chapters carry `*Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-006 retroactive-thinning sweep (priority #11).*` italic notes that become stale (`output-arg-vs-receiver.md` line 36, `mfem-vector-types.md` line 42, `linalg-free-functions.md` line 47, `transparent-vs-load-bearing-tricks.md` line 34, `apply-linop-overload-set.md` line 55). The report explicitly scopes these out (out of L1-thinning scope); flagging here in Notes for integrator-finalize's roadmap-update consideration and the next cycle's planner — bundlable into one `layer-intro-author` dispatch in cycle-008.
- Deferred `integrated_at:` and `integration_commit:` to finalize per role-spec (per-report integrator does not touch consumed-report frontmatter; CLAUDE.md §Write-authority partition + cycle-006 friction `integrated-at-write-authority-drift`).
- 5 cycle-007 wave-1 reports total; this is per-report dispatch 3 of 5.

---

## 2026-05-27T160550Z-harvester-iterate-while-family-L4
applied_at: 2026-05-27T18:30:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/iterate-while.md (create)
- book/src/L4/iterate-while-with-prev.md (create)
- book/src/L4/index.md (edit — dep-map: replaced 2 rough-in rows for `iterate_while` and `iterate_while_with_prev` with firm rows; `krylov-step` row's Dependencies cell extended to list the two new L4-row dependencies; total firm-row count now 3)
- book/src/SUMMARY.md (edit — L4 Part: added 2 chapter entries `[iterate-while]` and `[iterate-while-with-prev]` after the existing `[krylov-step]` entry)
- scaffolding/open-questions.md (edit — flipped `iterate-while-l4-anchor-missing` from `status: open` → `status: answered` with `answered_at: cycle-007` + `answered_in: reports/2026-05-27T160550Z-...`; appended cycle-007 resolution paragraph to its body; appended cycle-007 status note to body of existing `iterate-while-l3-rendering-trajectory-accumulation-gap` (kept `status: open`); appended 2 new OQs `gmres-inner-loop-iterate-while-migration` and `iterate-while-pure-promotion-decision`)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate check to integrator-finalize; this report only created new L4 chapters, updated L4/index.md dep-map, and updated open-questions/SUMMARY)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0 (all cross-refs from the new chapters point to existing files; `krylov-step-typed-wrapper-dissolution.md` exists cycle-006, `solve-monad.md`/`derived-view-hoisting.md`/`convergence-test.md`/`first-iteration-unrolling.md` all exist in `book/src/concepts/`)
- edge-label / prose mismatch: 0 (the two new chapters are L4 row chapters; §"Lowers to" sections explicitly defer the L4>L3 standalone theme to OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` and acknowledge the existing theme's trajectory-drop gap per the repaired wording)
- H1 reuses page heading: 0 (chapter H1s `# iterate-while` and `# iterate-while-with-prev` distinct from SUMMARY entry text)
- append on missing slug: 0 (open-questions edits modify existing slugs in-place: `iterate-while-l4-anchor-missing` body augmented + frontmatter flipped; `iterate-while-l3-rendering-trajectory-accumulation-gap` body augmented; 2 new slugs appended)
- variant-axis missing on multi-variant operator: 0 (both chapters carry Variant axes §; iterate-while has 3 axes (pure-vs-Solve, extras-vs-no-extras, bootstrap-free-vs-carry-bootstrapped); iterate-while-with-prev has 2 axes with explicit note that the third axis is below this combinator's level)
- bookkeeping incomplete: 0 (proposed-changes Files block is self-consistent; the SUMMARY edit + index.md dep-map edit are coordinated)
- SUMMARY.md chapter registration auto-fix: 0 (report explicitly proposed the SUMMARY edits)
- index-placeholder displacement auto-fix: 0 (L4/index.md had no `(empty — Phase B skeleton.)` placeholder text; the two rough-in rows were already firm-shape rows being promoted to `firm`-status rows with anchor files)

Open questions promoted:
- gmres-inner-loop-iterate-while-migration
- iterate-while-pure-promotion-decision

Open questions augmented (status flips / body additions on existing slugs):
- iterate-while-l4-anchor-missing (cycle-006): status open → answered; answered_at: cycle-007; answered_in: this report dir; cycle-007 resolution paragraph appended to body
- iterate-while-l3-rendering-trajectory-accumulation-gap (cycle-006): status open (unchanged); cycle-007 update paragraph appended to body recording that the L4 trajectory shape is firm but the L3 form still drops the trajectory; routes to cycle-008+ lowering-verifier

Build-relevant: yes

Notes:
- Both new L4 chapter files render the L4 strawman §3.7 small-step semantics in `$$ ... $$` LaTeX math display, with text-fenced signatures using Haskell `::` arrow form + TypeScript record brace form (` ```text ... ``` `) per the user directive 2026-05-27 (L4/L3 pseudo-language convention) and the L4-strawman-in-management invariant. The chapter shape matches the cycle-006 `book/src/L4/krylov-step.md` precedent (Context / Signature / Semantics / Algebraic laws / Variant axes / Status / L4 vs L3 distinction / Evidence sections).
- The `iterate-while-with-prev.md` chapter uses the repaired `(α, β)` closure-argument convention throughout (carry-first, prev-second) — matches both `first-iteration-unrolling.md:34-37` (`\(s, carry) -> ...`) and `cg.md:443` (`\(s, beta_prev) -> ...`). The §Evidence note explicitly records this consistency. Repairer's medium-severity finding #3 fully resolved in the report content I copied verbatim into the L4 chapter.
- The open-questions augmentation pattern (flip-status-with-keys + append-resolution-paragraph for closures; append-status-note for in-progress related work) follows the cycle-006 `krylov-step-l3-row-contingency` resolution schema. The repairer's low-severity finding #7 (resolve-mark schema correction from "resolved-by:" → `status: answered` + `answered_at:` + `answered_in:`) was applied as authored in the report's repaired YAML block.
- Forward-citation precision (repairer's low-severity finding #2): both chapters' §"Lowers to" now explicitly state the existing theme's L3 form at `krylov-step-typed-wrapper-dissolution.md:156-167` drops the trajectory, that the firm L4 form here keeps it (Law 1 / Law 2), and that the OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` tracks the discrepancy with cycle-008+ lowering-verifier as the resolution route. Honest-deferral framing rather than authoritative-anchor framing.
- The `krylov-step` row's Dependencies cell was extended to list the 2 new L4-row dependencies (`iterate-while`, `iterate-while-with-prev`) — this is required by the report's proposed dep-map text and reflects the firm-up: krylov-step Form A's body folds via iterate-while; krylov-step Form B's body uses iterate-while-with-prev. The cell-extension is purely additive (the existing concept-page dependencies are preserved).
- Cross-reference targets verified pre-apply: `book/src/L4/krylov-step.md` (cycle-006), `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (cycle-006), `book/src/concepts/{solve-monad,derived-view-hoisting,convergence-test,first-iteration-unrolling}.md` (all present), `book/src/design/l4_calculus.md` (strawman), `book/src/spec/slices/{cg,gmres}.md` (slice corpus). All targets exist.
- SUMMARY.md edit was non-conflicting with prior in-cycle state — pass-1 (L0-bundle-3) touched L0 Part chapters; pass-2 (ksp_solve) touched L1 Part; pass-3 (L1-context-thinning-sweep) made no SUMMARY edits; this pass touches L4 Part. Re-read disk at edit time confirmed the L0/L1 entries from prior passes are present and undisturbed; the L4 insertion preserves them.
- L4/index.md edit was non-conflicting with prior in-cycle state — no prior pass touched any L4 file. Re-read disk at edit time confirmed the index was at its pre-cycle-007 state with the two rough-in rows still present; the in-place row-replacement is the first L4 modification of this cycle.
- open-questions.md edits were non-conflicting with prior in-cycle state — pass-1 appended 4 OQs (`mfem-wrapper-solver-l4-complex-from-real-lift-backref`, etc.), pass-2 appended 3 OQs (`ksp-solve-concept-page-signature-update`, etc.). This pass modifies 2 existing OQs in-place (in the cycle-006 block) and appends 2 new OQs at end of Open section (before `## Dropped`). Re-read disk at edit time confirmed the prior OQ appends are intact and the in-place edits target the correct cycle-006 lines.
- This dispatch UNBLOCKS wave-2 (lowering-verifier on `iterate_while` L3 trajectory gap): with both L4 anchor files now present and the firm L4 trajectory shape stated, the cycle-007 wave-2 lowering-verifier can dispatch with the OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` as its primary scope and the just-firmed L4 chapters as its read-set. The OQ's "Cycle-007 update" paragraph explicitly hands off the gap to cycle-008+ lowering-verifier (the cycle-007 wave-2 dispatch may opt to address it ahead of cycle-008 if scoped accordingly).
- Closes cycle-006 OQ `iterate-while-l4-anchor-missing` (cleanly answered with `answered_at: cycle-007` + `answered_in:` keys); does NOT close `iterate-while-l3-rendering-trajectory-accumulation-gap` (only augments with status note; gap remains for cycle-008+ lowering-verifier per role-spec deferral). Per cycle-006 friction `integrated-at-write-authority-drift`, the closure record itself (whether finalize subsequently marks anything additional on the cycle-006 OQ as a closure-batch entry) is finalize's responsibility — this per-report integrator only flips the status field and appends body content per the canonical YAML schema; finalize handles cycle-record + integrator-signals.
- Deferred `integrated_at:` and `integration_commit:` to finalize per role-spec (per-report integrator does not touch consumed-report frontmatter; CLAUDE.md §Write-authority partition + cycle-006 friction `integrated-at-write-authority-drift`).
- 5 cycle-007 wave-1 reports total; this is per-report dispatch 4 of 5.

---

## 2026-05-27T160445Z-abstractor-krylov-step-body-identity-L3-L2
applied_at: 2026-05-27T19:00:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3-L2/krylov-step-body-identity.md (create — first firm-rough-in L3>L2 theme; ratifies cycle-006 audit verdict on `krylov-step` body-identity-in-form)
- book/src/L3-L2/index.md (edit — Theme list section: displaced empty `(empty — Phase B skeleton.)` placeholder fenced block with a firm-rough-in theme-list table containing one row for `krylov-step-body-identity`)
- book/src/SUMMARY.md (edit — L3>L2 Part: appended `[krylov-step-body-identity](./L3-L2/krylov-step-body-identity.md)` chapter entry after the Overview line)
- scaffolding/open-questions.md (edit — flipped `krylov-step-body-identity-theme-pending-cycle-007` from `status: open` → `status: closed` with `answered_at: cycle-007` + `answered_in: reports/2026-05-27T160445Z-abstractor-krylov-step-body-identity-L3-L2/CYCLE.md`; appended cycle-007 closure paragraph to its body)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate check to integrator-finalize; this report only created the new L3-L2 theme chapter, displaced the L3-L2/index placeholder with the first firm-rough-in row, added a SUMMARY entry, and updated one OQ slug)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0 (all cross-refs from the new chapter point to existing files: `L4/krylov-step.md`, `L4-L3/krylov-step-typed-wrapper-dissolution.md`, `L2/krylov-step.md`, and the 5 `concepts/{state-stratification, derived-view-hoisting, variant-absorption, first-iteration-unrolling, sequential-obstruction}.md` pages — all verified present pre-apply)
- edge-label / prose mismatch: 0 (the theme is correctly placed at the L3>L2 edge in `book/src/L3-L2/`; LHS prose is L3 form, RHS prose is L2 form, abstraction-direction note at §"Justification kind" confirms L3 → L2 direction)
- H1 reuses page heading: 0 (chapter H1 `# krylov-step-body-identity` distinct from SUMMARY entry text and from the L3-L2 Part heading)
- append on missing slug: 0 (OQ slug `krylov-step-body-identity-theme-pending-cycle-007` existed in `scaffolding/open-questions.md` pre-apply; status flip + body append modify in-place)
- variant-axis missing on multi-variant operator: 0 (N/A — theme is identity-in-form ratification, not an operator; §"Applicability conditions" item 4 explicitly addresses the six-axis closure inherited from the L2/L4 entries)
- bookkeeping incomplete: 0 (proposed-changes Files block is self-consistent; SUMMARY edit + index.md placeholder-displacement + OQ closure all coordinated)
- SUMMARY.md chapter registration auto-fix: 0 (report explicitly proposed the SUMMARY edit)
- index-placeholder displacement auto-fix: applied-discretionarily (the report's proposed REPLACE block targets the L3-L2 index's `(empty — Phase B skeleton.)` placeholder; per cycle-006 friction `index-placeholder-displacement-on-first-firm-row` formalized in the role-spec, the placeholder is genuinely empty and is being properly displaced by the first firm-rough-in theme row; the placeholder-displacement discipline is the report's own framing — no integrator-side rewrite was needed, the displacement is directly applied as proposed; recording as applied-discretionarily for traceability per the role-spec gate enumeration)

Open questions promoted:
- (none — the report's only OQ interaction is the closure of `krylov-step-body-identity-theme-pending-cycle-007`; no new OQs proposed; the four open-questions / caveats in the CYCLE.md §"Open questions / caveats" section are anticipated-critic-defenses (caveat 5), known-orthogonal-OQs (caveat 2 references the existing `iterate-while-l3-rendering-trajectory-accumulation-gap` already on file), or known-and-intentional consequences (caveats 1, 3, 4) — none warrant promotion to the ledger per the report's own dispositions)

Open questions augmented (status flips / body additions on existing slugs):
- krylov-step-body-identity-theme-pending-cycle-007 (cycle-006): status `open` → `closed`; `answered_at: cycle-007`; `answered_in: reports/2026-05-27T160445Z-abstractor-krylov-step-body-identity-L3-L2/CYCLE.md (theme authored as book/src/L3-L2/krylov-step-body-identity.md; ratifies cycle-006 audit)`; cycle-007 closure paragraph appended to body recording the placeholder displacement, justification kind, status inheritance pattern, and the body-vs-wrapper rotation split

Build-relevant: yes

Notes:
- The L3-L2 index placeholder displacement is the first such displacement in the L3-L2 Part — the L3-L2/index.md had only the Phase-B skeleton stub pre-apply (Theme list section containing just the fenced `(empty — Phase B skeleton.)` block). The replacement table inserts the first firm-rough-in row in canonical L3-L2 dep-map shape (Theme | LHS (L3) | RHS (L2) | Justification kind | Status). Verified pre-apply that the placeholder block was the literal Phase-B skeleton text and not a previously-populated row.
- The 4-layer status inheritance pattern was honored throughout the chapter content as authored: upstream `krylov-step-typed-wrapper-dissolution.md` §Status (line 216) is `rough-in` → this theme's §Status is `firm-rough-in` (firm ratification + rough-in LHS inheritance). The index row also declares `firm-rough-in` with explicit inheritance annotation. Promotion to plain `firm` is automatic when the upstream theme is itself promoted.
- The body-vs-wrapper rotation framing surfaces correctly in the chapter intro (per repairer Finding 1 repair): the opening paragraph now explicitly names "two state-hiding / abstraction-by-role rotations at the wrapper around the body" with the (K, s) → unified IterState as state-hiding and the outer-loop → outer-driver-by-role as abstraction-by-role. The §"Rewrite shape" section's 1:1 line-by-line mapping table on the body is correctly defended by the intro framing — the rotation work is at the wrapper, the body is identity, and the rotation-quality rubric grants `pass` for state-hiding / coarser-substitution rotations at the wrapper level.
- The citation `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"L3 form (RHS)" cited as lines 55-89 (corrected from the original 56-89 per repairer Finding 6) — this is the correct line range; the §"L3 form (RHS)" header is at line 55 in the upstream file.
- The L4-L3 upstream theme's `rough-in` status (also referenced in inheritance annotation per Finding 2 repair) was verified at line 216 of `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` — this is the canonical source-of-truth for the upstream status.
- Cross-reference targets verified pre-apply: 5 internal book links from the new L3-L2 chapter (`L4/krylov-step.md`, `L4-L3/krylov-step-typed-wrapper-dissolution.md`, `L2/krylov-step.md`, and 5 `concepts/<slug>.md` pages). All present in the artifact.
- SUMMARY.md edit was non-conflicting with prior in-cycle state — pass-1 (L0-bundle-3) touched L0 Part chapters; pass-2 (ksp_solve) touched L1 Part; pass-3 (L1-context-thinning-sweep) made no SUMMARY edits; pass-4 (iterate-while-family-L4) touched L4 Part with 2 new entries. This pass touches L3>L2 Part with 1 new entry. Re-read disk at edit time confirmed the L0/L1/L4 entries from prior passes are present and undisturbed; the L3>L2 insertion preserves them.
- L3-L2/index.md edit was non-conflicting with prior in-cycle state — no prior pass touched any L3-L2 file. Re-read disk at edit time confirmed the index was at its pre-cycle-007 state (Theme list section containing only the placeholder); the placeholder-displacement REPLACE is the first L3-L2 modification of this cycle.
- open-questions.md edit was non-conflicting with prior in-cycle state — pass-1 appended 4 OQs, pass-2 appended 3 OQs, pass-4 augmented 2 existing OQs in-place + appended 2 new OQs. This pass augments 1 existing OQ in-place (closes `krylov-step-body-identity-theme-pending-cycle-007` in the cycle-006 block). Re-read disk at edit time confirmed the prior OQ appends and pass-4's status flips on `iterate-while-l4-anchor-missing` are intact; the in-place closure-edit targets the correct cycle-006 lines (1212-1221) without touching the adjacent `iterate-while-l3-rendering-trajectory-accumulation-gap` slug (which pass-4 had augmented).
- Closes cycle-006 OQ `krylov-step-body-identity-theme-pending-cycle-007` (cleanly answered with `answered_at: cycle-007` + `answered_in:` keys; closure-paragraph appended to body per cycle-006 schema). Per cycle-006 friction `integrated-at-write-authority-drift`, the closure record itself (whether finalize subsequently marks anything additional as a closure-batch entry on the cycle-006 OQ) is finalize's responsibility — this per-report integrator only flips the status field and appends body content per the canonical YAML schema; finalize handles cycle-record + integrator-signals.
- The four `Open questions / caveats` entries in the CYCLE.md (caveat 1: future Krylov slices may break identity-in-form; caveat 2: known orthogonal `iterate-while-l3-rendering-trajectory-accumulation-gap`; caveat 3: confirmed-decision-from-cycle-006 on no L3 row; caveat 4: known-and-intentional `IterState` consolidation erases ephemeral typing; caveat 5: anticipated critic finding on theme shortness) are all dispositioned as non-promoting per the report's own analysis. No OQ-promotion actions taken — verified against the report's §"Open questions / caveats" item-by-item dispositions.
- Deferred `integrated_at:` and `integration_commit:` to finalize per role-spec (per-report integrator does not touch consumed-report frontmatter; CLAUDE.md §Write-authority partition + cycle-006 friction `integrated-at-write-authority-drift`).
- 5 cycle-007 wave-1 reports total; this is per-report dispatch 5 of 5 — last wave-1 dispatch. Wave-2 (lowering-verifier on `iterate_while` L3 trajectory gap, per the OQ that pass-4 augmented but did not close) is now ready to dispatch; the wave-1 reports' integration is complete pending integrator-finalize.

---

## 2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation
applied_at: 2026-05-27T19:30:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- scaffolding/open-questions.md (edit — augmented existing OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` body with a new **Cycle-007 wave-2 verdict** paragraph recording the audit verdict-(c) closure rationale, key L0/L1 evidence summary, the subsumption of both originally-enumerated candidate resolutions, the new applicability Condition 5, and the explicit gating on cycle-008+ lifter patch for the substantive §3.8-citation patch at `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`; status field left as `open` per user-directive override of the report's proposed `closed` flip; appended new OQ `iterate-while-log-effect-vs-trajectory-channel` (cycle-007, lowering-verifier, status: open) as a standalone entry at end of cycle-007 block before `## Dropped` header)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate check to integrator-finalize; this audit-only dispatch touched no book/ artefacts)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0 (the new OQ's claim about extending `Solve` to a richer effect representation is framed as a question, not a surface claim; the cited Palace L0 ranges in the augmentation paragraph all exist and were cited via existing verified ranges)
- edge-label / prose mismatch: 0 (N/A — audit-only dispatch, no L_{n+1}→L_n edge surface authored)
- H1 reuses page heading: 0 (no chapter creations)
- append on missing slug: 0 (the augmentation targets existing slug `iterate-while-l3-rendering-trajectory-accumulation-gap` which pass-4 already established at lines 1229-1239; the new OQ append uses a fresh slug `iterate-while-log-effect-vs-trajectory-channel`)
- variant-axis missing on multi-variant operator: 0 (N/A — audit-only)
- bookkeeping incomplete: 0 (proposed-changes Files block matches the actual file touched: open-questions.md only; no book/ touches; no SUMMARY edits; no index.md edits)
- SUMMARY.md chapter registration auto-fix: 0 (N/A — no chapter creations)
- index-placeholder displacement auto-fix: 0 (N/A — no index.md edits)

Open questions promoted:
- iterate-while-log-effect-vs-trajectory-channel

Open questions augmented (status flips / body additions on existing slugs):
- iterate-while-l3-rendering-trajectory-accumulation-gap (cycle-006): body augmented with **Cycle-007 wave-2 verdict** paragraph recording audit verdict-(c); status field intentionally left as `open` per user-directive override of the report's proposed `closed` flip — closure becomes appropriate only AFTER the cycle-008+ lifter dispatch lands the §3.8 collapse-rule citation at `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for iterate_while looks like" plus the new Condition 5 at §"Applicability conditions". The augmentation paragraph preserves pass-4's prior "Cycle-007 update" paragraph (which recorded the L4 firming and the still-open L3 gap) and extends rather than overwrites it.

Build-relevant: no

Notes:
- This is an audit-only dispatch — no `book/` artefact edits. The report's Change 1 (OQ closure for `iterate-while-l3-rendering-trajectory-accumulation-gap`) was applied with the user-directive modification: status remains `open`, body augmented with verdict + gating-on-lifter rationale; the canonical YAML status-flip block proposed by the report (with `status: closed`, `answered_at: cycle-007`, `answered_in:`) was NOT applied. Closure occurs in a future cycle after the lifter patch lands.
- Report Change 2 (`verified_against:` YAML block appended to `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`) was DEFERRED per the user-directive scope ("audit-only dispatch — no CREATE/EDIT blocks against book/ artefacts"). The 10-citation `verified_against:` block (lines 184-225 of CYCLE.md) is captured in the report for future application; the audit-trail metadata can be added by the same cycle-008+ lifter dispatch that lands the substantive §3.8-citation patch (Change 3), or by a separate book/ housekeeping dispatch that batches multiple lowering-theme verified-against blocks. The L1-L0 precedent (`book/src/L1-L0/axpby-mutation-rotation.md:173`, `apply-linop-mutation-rotation.md:353`, `bicgstab-iteration.md:64-80`) confirms the trailing-YAML-block placement is the canonical shape; the wrapper-style `## Verified-against` H2 section at `bicgstab-iteration.md` is the stylistic variant; both are acceptable when applied.
- Report Change 3 (substantive patch to `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for iterate_while looks like": cite Law 1 + `concepts/derived-view-hoisting.md` §"Worked example: CG residual norm"; replace 9-line code-block sketch with two-form sketch [pruned vs unpruned]; add Condition 5 to §"Applicability conditions") was DEFERRED per the report's own framing (lines 228-236 of CYCLE.md): "out of lowering-verifier authority — proposed for cycle-008+ lifter dispatch." Routes to a cycle-008+ `lifter` dispatch. Suggested integrator-signal for integrator-finalize: queue this as a cycle-008 priority slate candidate — low-cost single-file edit (no new operator promotion, no new theme), naturally bundlable with any cycle-008 lifter dispatch on `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (e.g., a lifter promoting the theme from `rough-in` to `firm` would naturally subsume this patch and Change 2's `verified_against:` block together).
- The augmentation paragraph at OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` extends pass-4's "Cycle-007 update" paragraph rather than overwriting it. Re-read disk at edit time confirmed pass-4's edit (lines 1229-1239 — the YAML frontmatter, body paragraph, and "Cycle-007 update" paragraph) is intact; the new "Cycle-007 wave-2 verdict" paragraph appended directly after the "Cycle-007 update" paragraph. The chronological accumulation pattern (cycle-006 framing → cycle-007 update → cycle-007 wave-2 verdict) is preserved per the open-questions ledger convention.
- The new OQ `iterate-while-log-effect-vs-trajectory-channel` is appended as the LAST cycle-007 OQ entry, just before the `## Dropped` section heading. The `relates_to:` field cross-references the verdict-(c)-recorded-but-not-yet-closed parent OQ; the question body verbatim mirrors the report's repaired YAML+paragraph block per the critic's Finding 4 repair, with one addition: the relates_to field carries an explicit parenthetical recording the parent OQ's status state so a future reader can locate the relationship without consulting the parent's body in detail.
- Cross-references in the augmentation paragraph verified: `book/src/L4/iterate-while.md` (Law 1), `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (§"What the L3 form for iterate_while looks like"), `book/src/concepts/derived-view-hoisting.md` (§"Worked example: CG residual norm"), `reference/palace/palace/linalg/iterative.hpp:52-55` (four-scalar surface), `reference/palace/palace/linalg/iterative.hpp:97-108` (four getters), `reference/palace/palace/linalg/ksp.cpp:296-310` (sole caller), `reference/palace/palace/linalg/iterative.cpp:420-485` (PCG outer loop), `reference/palace/palace/linalg/iterative.cpp:614-705` (GMRES inner loop), `reference/palace/test/unit/` (no test on KSP residual history) — all consistent with the critic's spot-check (META.md citation-validity check pass).
- Coexistence with prior cycle-007 passes: pass-1 (L0-bundle-3) appended 4 OQs; pass-2 (ksp_solve) appended 3 OQs; pass-3 (L1-context-thinning-sweep) made no OQ edits; pass-4 (iterate-while-family-L4) augmented 2 existing cycle-006 OQs + appended 2 new OQs (`gmres-inner-loop-iterate-while-migration`, `iterate-while-pure-promotion-decision`); pass-5 (krylov-step-body-identity-L3-L2) closed 1 cycle-006 OQ (`krylov-step-body-identity-theme-pending-cycle-007`). This wave-2 pass augments 1 existing cycle-006 OQ (`iterate-while-l3-rendering-trajectory-accumulation-gap`, the same one pass-4 augmented — extending rather than overwriting pass-4's "Cycle-007 update" paragraph) and appends 1 new cycle-007 OQ (`iterate-while-log-effect-vs-trajectory-channel`).
- Deferred `integrated_at:` and `integration_commit:` to finalize per role-spec (per-report integrator does not touch consumed-report frontmatter; CLAUDE.md §Write-authority partition + cycle-006 friction `integrated-at-write-authority-drift`).
- 6 cycle-007 reports total (5 wave-1 + 1 wave-2); this is per-report dispatch 6 of 6 — the wave-2 dispatch. All cycle-007 per-report integration is complete; ready for integrator-finalize.

Suggested integrator-signals (for integrator-finalize to surface to next-cycle planner via `scaffolding/integrator-signals.md`):
- **Suggested cycle-008+ lifter dispatch on `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`**: apply the wave-2 audit's Change 2 (`verified_against:` 10-citation block appended; trailing-YAML-block placement per L1-L0 precedent) and Change 3 (substantive §3.8-citation patch at §"What the L3 form for iterate_while looks like" + Condition 5 at §"Applicability conditions" + two-form sketch [pruned vs unpruned] replacing the current single-`readout` 9-line code block). Low-cost single-file edit. Naturally bundles with any other cycle-008 lifter work on the same theme (e.g., a `rough-in` → `firm` status promotion). Upon application, the parent OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` is then closeable with `status: closed`, `answered_at: cycle-008` (or whichever cycle lands the patch), `answered_in: <dispatch CYCLE.md>`.
- **Possible cycle-008+ lowering-verifier or abstractor follow-up on the orthogonal logging-effect channel**: per new OQ `iterate-while-log-effect-vs-trajectory-channel`. Lower-priority than the §3.8-citation patch; surfaces during meta-phase methodology review of the L4 monad surface (i.e., a cycle-009 meta-phase batch consideration if no per-cycle dispatcher picks it up earlier). Not blocking on anything.

---

---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T16:42:05Z
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
repaired_at: 2026-06-01T17:05:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L4>L3 theme sketch — iterate-while-dissolution"

## Critique

### Checks run

**citation-validity — pass.** `tools/citecheck/citecheck.py --scan CYCLE.md --quiet` reports 41 ok / 0 failing (bounds + path-hygiene clean). The load-bearing pinpoints were `--anchor`-confirmed mechanically: `book/src/L4/iterate-while.md:123-133 --anchor 'Demand-driven trajectory pruning'` (anchor at 123, in range), `book/src/design/l4_calculus.md:186-213 --anchor 'pruning'` (anchors at 186, 201), and `krylov-step-typed-wrapper-dissolution.md:188-198 --anchor 'collapse'` (anchor at 188). I then meaning-read the extraction source: the three extracted forms match disk verbatim — the unpruned `iterate_while_L3` ground form is at `krylov-step-typed-wrapper-dissolution.md:164-171`, the pruned `iterate_while_L3_pruned` at `:176-184`, the collapse-rule `$$...$$` at `:188-198` (the report's claimed ranges), and the cycle-002 identity-in-form audit at `:202-213`. The strawman §3.7 small-step rule sits at `l4_calculus.md:164-171` and the §3.8 pruning rule (the `op_{¬k}` graph-DCE equivalence) at `:201-211` within the cited `:186-213` (matches `iterate-while.md`'s own Law-1 provenance citation). The two Palace L0 consumer-surface citations resolve under the correct double-`palace` path: `reference/palace/palace/linalg/iterative.hpp:52-55` is exactly the four-scalar `converged`/`initial_res`/`final_res`/`final_it` surface, and `reference/palace/palace/linalg/ksp.cpp:296-310` is the sole `Mult` consumption site reading only `GetConverged`/`GetFinalRes`/`GetInitialRes`/`GetNumIterations` (i.e. `final_state`-equivalent quantities, no residual history) — this directly supports the Condition-4 claim that the pruned form is Palace's rendered shape. No `verified_against:` fenced-YAML block is emitted (the report uses a `## Verified-against` prose section, not a YAML round-trip payload), so the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This is a NEW standalone theme (`new:` block) plus surface re-anchor edits to three deferral sites in the existing firm L4 `iterate-while` chapter + dep-map. It is not a refinement-shaped rotation_claim-without-surface: the proposal modifies surface (the new chapter is surface; the three re-anchor `edit:` blocks rewrite existing `iterate-while.md` / `index.md` prose) AND carries the full rotation evidence (strawman §3.7/§3.8, firm L4 Law 1, the parent-theme cycle-002 body-identity audit). The extraction-from-firm-sub-component framing is explicit and well-cited.

**rotation-quality — pass.** This is a genuine L4→L3 rotation, not a degenerate no-op or rename. The L4 LHS (`Solve`-threaded, row-polymorphic `{ state: α, ...e }` step return, demand-prunable `trajectory` accumulator) is strictly more abstract than the L3 RHS (positional `sim` thread, positional tuple step return, explicit list-cons accumulator or outright drop). The rotation hides state (the `Solve = StateT SimState Identity` monad dissolves to a positional `sim`), coarsens the row-polymorphic record to a positional tuple, and threads the loop tail-recursively — all three are real compression/lowering moves, not 1:1 mappings. The forward narration is genuine (LHS named as L4 Form A, RHS as the two tail-recursive value-threaded forms, prose narrated high→low). The trajectory-keeping-unpruned-vs-§3.8-pruned framing is correct: I cross-checked the parent theme's prose, where the original at `iterate-while.md:188` framed the trajectory-drop as "the very gap" (a defect note); this chapter correctly reframes the pruned form as the *image* of Law 1's collapse rule applied to the unpruned ground form under a `final_state`-only consumer (NOT a contradiction of the firm L4 Law 1, which keeps the trajectory in its general statement). This is exactly the cycle-046-critic-flagged mis-framing being corrected, and the correction is sound. The degenerate-extraction concern the report itself flags (Open-questions bullet 1) is real but does not sink the check: the dedicated theme adds genuine layer-coherent content beyond the buried sub-component — the explicit ground-form-vs-collapse-image split, the four-condition applicability section, and the generic-vs-slice-specialised relationship to the gmres/fgmres themes. The body code forms are reproduced verbatim (acknowledged), but the surrounding rotation framing is new and layer-coherent, which is the point of the re-homing per the "each layer is coherent within itself" invariant.

**variant-axis-coverage — pass.** The orthogonal axes are covered or explicitly scoped: the pruned/unpruned axis (Condition 4 selects between the two L3 forms by consumer demand — both forms given), the no-extras `iterate_while_pure` sugar (§"`iterate_while_pure` — the no-extras sugar", the `e = ()` degenerate case), and the bootstrap-free-vs-`iterate-while-with-prev` axis (explicitly scoped out under §"What this lowering does NOT cover", with the `prev`-positional delta noted and the `with-prev` `Lowers to` re-anchor flagged as a follow-up rather than silently dropped). No hidden branches.

**cross-reference-integrity — pass.** Build-readiness fence-parity is clean: `grep -n '^```'` on CYCLE.md yields one `new:` block (25→202) and five paired `edit:` blocks (208/210, 214/216, 220/222, 226/229, 231/234) — even parity throughout. The firm-body guard passes: `## Status` and `## L4 vs L3 distinction` both sit INSIDE the `new:` fence (the body uses 4-space-indented code for the Haskell-style forms and `$$...$$` for math — zero internal ` ``` ` fences, so no nested-fence truncation risk; the cycle-019 fence-truncation defect is absent). All relative `.md` links in the new chapter resolve to on-disk files (verified `L4/iterate-while.md`, `L4/iterate-while-with-prev.md`, `L4/krylov-step.md`, `L3/krylov-step.md`, the three `L4-L3/` siblings, the three `concepts/` pages, `spec/slices/arnoldi_step.md`, `cg.md` all exist) — no forward-ref to a not-yet-existing same-cycle sibling. The re-anchor `edit:` old-strings match disk: §"Lowers to" deferral paragraph at `iterate-while.md:188` begins "The L4>L3 theme for `iterate_while` is not yet authored as a standalone..." and §"L4 vs L3 distinction" closing paragraph at `:218` begins "The two layers' entries share signature shape..." — both pinned exactly by the report's prose. The dep-map full-row replacement targets `L4/index.md:54` (the `iterate-while` row, verified present). SUMMARY + L4-L3-index registration anchors verify: the SUMMARY edit anchors on disk line 17 (`- [fgmres-inner-loop-iterate-while-migration]...`) appending the new line after; the L4-L3 index edit anchors on the `fgmres` row (disk line 17) appending the new row after. Both surgically correct.

**edge-label-fidelity — pass.** Every re-anchored edge points the right direction (L4>L3) at the right theme. The §"Lowers to" prose (Re-anchor 1) and §"L4 vs L3 distinction" prose (Re-anchor 2) both now cite `iterate-while-dissolution` as the L4>L3 lowering; the dep-map "Lowers to" cell (Re-anchor 3) names the same theme with the firm/cycle-047 annotation. The new chapter's own §"Abstraction-direction note" states the rotation direction is L4 → L3, consistent with the prose throughout. The `with-prev` row's edge is correctly NOT touched (out of scope, flagged).

**plan-kind-consistency — pass.** Declared kind is a `firm` L4>L3 theme (extraction + re-homing of an already-firm sub-component). The content shape matches: exhaustive citations against strawman + firm L4 Law 1 + parent-theme audit, no rough-in placeholders, no speculative operators (§"Speculative L4 operators": None — both L4 caps it lowers are firm rows). The `firm` claim is justified by the fully-cited extraction provenance; this is not a mis-classified rough-in.

**skill-uptake-survey — warning.** The report's shape implies several relevant skills, and it references `tools/citecheck` invocation (Open-questions bullet "Citation self-verification" + §Supporting-evidence "Citecheck-confirmed") — good uptake on the citation-verification side. However, the build-readiness fence-parity guard (`proposed-changes-fence-encloses-full-body-guard`) is directly on-point for a NEW firm-chapter `new:` block and is not referenced, and the SUMMARY-insertion shape matches `summary-md-surgical-insert` without mention. This is a pure telemetry surface (non-blocking): the work is fence-clean regardless, but the skill-invocation references are absent for the two guards most relevant to a new-chapter-plus-registration dispatch.

### Issues found

1. **Edit-block format carries only replacement text, not paired old/new (minor, integrator-facing).** CYCLE.md:204-222 — the three `edit:` re-anchor blocks (`iterate-while.md` ×2, `index.md` ×1) carry ONLY the new replacement text; the old-string to replace is identified in the surrounding prose ("Replace the exact on-disk paragraph beginning ..."). I verified each prose-pinned old-string matches disk exactly (§"Lowers to" at `iterate-while.md:188`, §"L4 vs L3 distinction" at `:218`, the `iterate-while` dep-map row at `index.md:54`), so the edits are applyable — but the integrator must read the prose to recover the old-string rather than getting a self-contained old→new pair. Not a defect in correctness; a procedural note that the integrator should not treat these `edit:` blocks as drop-in replace-all payloads.

2. **Degenerate-extraction surface is real and self-flagged (informational).** CYCLE.md:80-116 (§"L3 form (RHS)") reproduces the two L3 code forms and the collapse rule verbatim from `krylov-step-typed-wrapper-dissolution.md:164-198`. The report's own Open-questions bullet 1 flags this and offers the collapsible surface (cite the parent rather than reproduce). The rotation-quality check passes (the new framing IS layer-coherent value-add), but the integrator/meta-phase may wish to decide whether the verbatim code reproduction is the desired self-contained form or whether a cite-to-parent thinning is preferred. Not blocking.

3. **`iterate-while-with-prev` §"Lowers to" left un-re-anchored (correctly out-of-scope; tracked).** CYCLE.md:255 + `iterate-while.md`-sibling — the firm `iterate-while-with-prev.md` cap's §"Lowers to" and its dep-map cell at `index.md:55` still defer to the buried sub-component ("standalone follow-up pending per OQ ..."), now stale relative to the landed dedicated theme. The report correctly scopes this out (one-theme-per-invocation) and files OQ candidate `iterate-while-with-prev-lowers-to-reanchor-to-dedicated-dissolution-theme`. Noted so the integrator/meta-phase ensures the follow-up is captured; this dispatch's own scope is clean.

4. **Two OQ-close recommendations ride on this landing (integrator-facing).** CYCLE.md:253-254 — the report recommends closing `iterate-while-l4-l3-standalone-theme-warranted-lifter-vs-abstractor` (route-b realized) and `iterate-while-l3-rendering-trajectory-accumulation-gap` (reconciled). Both recommendations are well-supported by the verified content (the reconciliation framing is sound per the rotation-quality check). Flagged only so the per-report integrator promotes/closes them deliberately rather than letting them linger.

## Repair

### Fixes attempted

No edits applied to CYCLE.md. The critic returned 7 `pass` + 1 `warning` (skill-uptake-survey telemetry) and four informational "Issues found", none blocking. Each was confirmed in-place against disk and found to need no mechanical repair.

- **Finding 1 — `edit:` blocks carry replacement-text-only with prose-pinned old-strings.**
  - **Decision**: not-needed (confirmed applyable; old-strings unambiguous).
  - **Action**: Independently verified all five proposed-changes anchors against disk. Re-anchor 1 (`iterate-while.md` §"Lowers to" paragraph beginning "The L4>L3 theme for `iterate_while` is not yet authored as a standalone …") matches verbatim through "… this section will be updated to cite it directly." Re-anchor 2 (`iterate-while.md` §"L4 vs L3 distinction" closing paragraph beginning "The two layers' entries share signature shape (modulo wrapper dissolution) …") matches verbatim; the unique opening string is unambiguous (the critic's `:218` line ref is approximate, but the prose pin is the load-bearing matcher and is exact). Re-anchor 3 (the full `iterate-while` dep-map row in `index.md`, opening `| [`iterate-while`](./iterate-while.md) |`) is present and unique (the `iterate-while-with-prev` row has a distinct opening). SUMMARY anchor line (`- [fgmres-inner-loop-iterate-while-migration](./L4-L3/fgmres-inner-loop-iterate-while-migration.md)`) and the L4-L3/index `fgmres` row anchor both match disk verbatim. No old-string is ambiguous or fails to match; no tightening required. Procedural note (integrator reads the prose pin to recover each old-string) stands as the critic recorded it — not a correctness defect.

- **Finding 2 — verbatim L3-code reproduction in §"L3 form (RHS)" (self-flagged collapsible surface).**
  - **Decision**: not-needed (integrator-discretion note, not a defect).
  - **Rationale**: The verbatim reproduction keeps the chapter self-contained and layer-coherent, which is the stated point of the re-homing ("each layer is coherent within itself" invariant). Whether to thin it to a cite-to-parent form is a content decision the integrator/meta-phase may take; it is out of repair authority and not required for application.

- **Finding 3 — `iterate-while-with-prev` §"Lowers to" / `index.md:55` left stale (out of scope).**
  - **Decision**: not-needed (resolved-by-design; tracked).
  - **Rationale**: The report correctly scopes the sibling re-anchor out under one-theme-per-invocation and files OQ candidate `iterate-while-with-prev-lowers-to-reanchor-to-dedicated-dissolution-theme`. The dispatch instruction confirms D2 handles the `with-prev` re-anchor this same cycle. No repair; the follow-up is captured.

- **Finding 4 — skill-uptake-survey warning (`proposed-changes-fence-encloses-full-body-guard` + `summary-md-surgical-insert` not referenced).**
  - **Decision**: not-needed (telemetry only).
  - **Rationale**: Pure skill-invocation telemetry surface, not a content defect. The work is fence-parity-clean and the SUMMARY insertion is surgically correct regardless of whether the skill names were cited. No mechanical repair applies.

### Unrepairable findings

None. No finding required substantive authoring or contradicted artifact content; all four are informational/integrator-discretion/out-of-scope-by-design.

## Suggested resolution

`ready`. Notes for the integrator:
- The three `edit:` re-anchor blocks are replacement-text-only with prose-pinned old-strings — read the surrounding prose ("Replace the exact on-disk paragraph beginning …") to recover each old→new pair; all five anchors verified to match disk exactly this pass.
- Promote/close the two OQs this landing resolves deliberately: `iterate-while-l4-l3-standalone-theme-warranted-lifter-vs-abstractor` (route-b realized) and `iterate-while-l3-rendering-trajectory-accumulation-gap` (reconciled — the unpruned `iterate_while_L3` is what Law 1 keeps; the pruned form is its demand-pruned image).
- Ensure OQ candidate `iterate-while-with-prev-lowers-to-reanchor-to-dedicated-dissolution-theme` is captured (D2 this cycle re-anchors the sibling cap + `index.md:55`).

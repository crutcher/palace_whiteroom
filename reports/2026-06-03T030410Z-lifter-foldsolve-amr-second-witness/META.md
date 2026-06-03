---
verifies: ../REPORT.md
critiqued_at: 2026-06-03T031500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
overall_status: ready
---

# META: verification of "Re-anchor fold_solve — AMR loop as 2nd state-generated witness" (cycle-073 D6)

## Critique

### Checks run

**citation-validity — pass.** `tools/citecheck/citecheck.py --scan` reports `7 ok, 0 failing`. I hand-Read `reference/palace/palace/drivers/basesolver.cpp:150-279` and confirmed every load-bearing pinpoint on disk:
- `:153` is exactly `void BaseSolver::SolveEstimateMarkRefine(std::vector<std::unique_ptr<Mesh>> &mesh) const`, and `:276` is the single-line closing `}` of that function (function body runs `:154-276`, next decl `SaveMetadata` starts `:278`). Range `153-276` is exact — no off-by-one, the close-brace-drift class does not apply.
- The state-generated anchors all verify: `:190` is `while (use_amr && !ExhaustedResources(it, ntdof) && err >= refinement.tol)` (the error-indicator continuation), `:267` is `err = indicators.Norml2(comm)` (the per-iteration error re-evaluation), `:239` is `fine_mesh.GeneralRefinement(marked_elements, -1, refinement.max_nc_levels)` (the refined-mesh per-step input), `:174`/`:266` are the seed/per-step `Solve(mesh)`, `:175` the seed `Norml2`, `:182` `ret |= (it >= refinement.max_it)`, `:184` `ret |= (refinement.max_size > 0 && ntdof > refinement.max_size)`, `:157-162` the TRANSIENT-exclusion warning.
- The report's "Dörfler-thresholded from the error-indicator state" claim for `marked_elements` (cited at `:239`) is supported by `:221-233` on disk: `marked_elements` is built via `utils::ComputeDorflerThreshold(comm, indicators.Local(), refinement.update_fraction)` then `MarkedElements(indicators.Local(), threshold)` — i.e. derived from the current error-indicator state. The "state-generated per-step input" claim is therefore accurately anchored.
- All four `[old]` edit anchors match the on-disk `book/src/L4/fold_solve.md` verbatim (frontmatter `:12`, §Variant axes item 1 `:150`, §Specializations "Both sweeps share…" `:117`, §Evidence SweepAdaptive line `:176`). The SweepAdaptive Evidence line `:176` is reproduced verbatim in Edit 4's `[new]` with the new AMR block appended after it — a clean additive append, no mutation of the existing witness text.
No `verified_against:` block is present (this is a lifter fold-in, not a lowering-verifier audit) — the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This is a refinement-shaped proposal that DOES modify surface (frontmatter axis line, §Variant axes prose, §Specializations prose) AND is framed as additive evidence backfill for an existing firm entry. The surface changes are accompanied by the L0 witness evidence (the `basesolver.cpp` block). It is not a bare rotation_claim. Passes on the surface-AND-evidence branch.

**rotation-quality — pass (not applicable).** The proposal asserts no new algebraic/structural/reduction rotation. It is a pure additive witness fold-in to an already-firm L4 entry — it adds a 2nd witness on an existing variant-axis value, changes no signature/law/status text. There is no L_{n+1}→L_n compaction claim to evaluate; the check no-ops.

**variant-axis-coverage — pass.** The relevant axis (`schedule-source: fixed-list | state-generated`) is the entry's load-bearing axis and is explicitly handled: the edit attaches the AMR loop to the `state-generated` value and the report demonstrates the AMR loop genuinely IS state-generated (loop bound `err >= refinement.tol` re-derived each iteration from `err = indicators.Norml2` at `:267`, per-step input the refined mesh generated from Dörfler-marked error state at `:239`) — the same axis-value shape as the existing SweepAdaptive witness, not a hidden new branch. The report correctly distinguishes the *resource caps* (`it >= max_it` `:182`, `ntdof > max_size` `:184` — which alone would make a *bounded* schedule) from the error-indicator continuation (`:190`/`:267`) that makes it *state-generated*; this is the load-bearing distinction and it is anchored correctly. No combination is left uncovered or hidden.

**cross-reference-integrity — pass.** The OQ slug `fold-solve-greedy-schedule-source-generalization` resolves (`scaffolding/open-questions.md:155,823,924`). The dispatch is the planned realization of the pre-positioned OQ `fold-solve-state-generated-schedule-source-second-witness-amr-loop` (`open-questions.md:921`, c072 D2 → plan Backlog Low, naming this exact `basesolver.cpp:153-276` fold-in). `book/src/L4/fold_solve.md` is wired into `SUMMARY.md:34`. No `[link]`s are introduced by the edits (all additions are prose + bare `file:line` citations). No firm-claim / proposed-changes-fence concern arises (no new `firm` body authored; the entry is already firm and the edits are additive). The four proposed-changes blocks are well-formed single-fence `edit:` blocks.

**edge-label-fidelity — pass.** No lowering edge label is carried (this is an L4 within-layer entry strengthening, not an L_{n+1}→L_n theme). The prose discusses the L4 fold combinator and its L0 witness consistently; no edge-label/prose mismatch possible.

**plan-kind-consistency — pass.** The content shape matches an observation-routed additive fold-in (LOW). Two deliberate non-edits were flagged for confirmation and both are sound:
- *No dedicated combinator proposed for the state-generated schedule.* Correct and consistent with scope + the standing OQ. The report records the 2-witness datapoint and defers the dedicated-combinator mine to a 3rd witness / downstream-consumer pull, citing the genuine divergence of the two witnesses' carry shapes (reduced-basis+error-history vs. refined-mesh+error-indicators) and per-step bodies (PROM greedy sample vs. mesh-refine + full re-solve) as the argument against premature unification. This matches the combinator-miner "replace-and-propagate, not mine-and-strand" discipline and the OQ trigger as written.
- *§Status "2-of-5 pipelines" sentence left unchanged.* Sound. I confirmed on disk (`fold_solve.md:159`) that the Scope sentence counts *pipelines* (transient + driven-PROM). `SolveEstimateMarkRefine` is a `BaseSolver`-level driver-agnostic outer wrapper that calls the per-driver `Solve(mesh)` (`:174`, `:266`) and excludes transient (`:157-162`) — it is NOT a 3rd pipeline, so incrementing the pipeline count would be a category error. The quantity that genuinely moves is the `schedule-source = state-generated` *value's* witness count (1→2), which is exactly what the edits touch. The non-edit is the correct call.
The witness numbering is consistent: on disk §Evidence carries "Fold witness 1 — transient" (`:172`) and "Fold witness 2 — driven-PROM SweepAdaptive" (`:175`); labeling the new block "Fold witness 3" (3rd overall fold witness, 2nd state-generated witness) is the correct next ordinal, and the report's Note explains the distinction clearly.

**skill-uptake-survey — pass.** The report's §Discipline-notes "Citation self-verification" records use of `tools/citecheck/citecheck.py --anchor` for every `basesolver.cpp` pinpoint plus a direct `read_range` confirmation of the `:276` close-brace and a codemap `get_symbol_def` cross-check of the `153-276` range — the expected citation-verification procedure for a citation-only fold-in. Telemetry surfaced; nothing blocking.

### Issues found

None blocking. The report is a clean, surgical, additive fold-in to an already-firm entry; all 8 checks pass.

Two non-blocking observations (telemetry only, not repair candidates):

1. **Witness-block label phrasing is internally consistent but worth a one-line confirmation at integration** (`CYCLE.md` Edit 4 + Note, `:53`/`:56`). The new §Evidence block is "Fold witness 3" while the *section header text* in §Variant axes / §Specializations frames it as the "2nd state-generated witness". Both are correct (3rd overall, 2nd state-generated) and the report's Note `:56` explicitly reconciles them. No drift — flagging only so the integrator does not mistake the "3" for an off-by-one against the "1→2" count in the Summary.

2. **`frontmatter:12` and §Variant-axes:150 both still carry the `(batch-18)` / `(batch-18+)` OQ-vintage tag** (`CYCLE.md` Edit 1 keeps the frontmatter axis line's existing tag implicitly, Edit 2 bumps `(batch-18)`→`(batch-18+)`). This is a deliberate one-token bounded touch the report calls out (Discipline note 4) and is harmless; noting only that the on-disk OQ is now tracked as far as c072/c073, so the "batch-18+" tag is conservative-correct (the OQ is still open). Not an issue — pure provenance hygiene.

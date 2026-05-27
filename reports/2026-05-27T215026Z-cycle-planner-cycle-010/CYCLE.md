---
agent: cycle-planner
invoked_at: 2026-05-27T21:50:26Z
scope: cycle-010 dispatch plan (first primary cycle of meta-batch-2 under 3:1 cadence)
status: pending
meta_batch: batch-2 (cycles 010/011/012; meta-phase fires after cycle-012 finalize)
---

# Cycle 010 dispatch plan

## Goals selected this cycle

**Cycle-010 opens meta-batch-2 with three strategic priorities:**

1. **Priority #20 (identity-lowering-both-levels-backfill): backfill L3 krylov-step entry** — cycle-006's verdict "no L3 row needed for krylov-step" is superseded by the new methodology invariant *Identity-lowerings still require both L levels*. The krylov-step lowering chain (L4→L3→L2 currently firm) is incomplete without an explicit L3 entry using L3 vocabulary. This is the **first target** of priority #20 and the **highest-priority dispatch** this cycle. Single harvester on `book/src/L3/krylov-step.md`.

2. **Priority #20 (identity-lowering-both-levels-backfill): audit other L4/L3/L2/L1 identity-in-form candidates** — after the krylov-step L3 backfill lands, a `cross-layer-cross-cutter` dispatch should audit the current operator cohorts to identify other layers where an identity-in-form rotation lacks an explicit lower-layer entry (e.g., apply_linop, dot, axpy at adjacent layers). This is the **second target** of priority #20.

3. **Priority #17 (lower-layer-shared-vocabulary-priority): advance L1/L2/L3 vocabulary over L4 expansion** — scheduled multiple L1 harvester dispatches for the cycle-008 OQ carry-forwards (`matrix-weighted-norm`, `bilinear-form`, `nrm2_B-weighted-energy-norm`) and the four eigsolve firm-promotion follow-up OQs. These populate the lower layers with reusable shared vocabulary that simplifies higher-layer work.

4. **Priority #19 (phase-1-corpus-reduction-audit): first slice-reduction audit** — schedule a `same-layer-cross-cutter` to audit one or a small batch of Phase 1 slices overlapping the now-firm krylov-step chain, verify which are fully superseded by layered entries, and propose reduction to stubs or removal. This is the **first instance** of the phase-1-corpus-reduction audit pattern.

5. **Pilot retry on MCP codemap tools** — commit `ceb87da` enabled the `mcp__palace-codemap__*` tools in `.claude/settings.json`. The `combinator-miner` MCP pilot retry (blocked 3 cycles by permission-denied) is now feasible. Include explicit agent-instruction snippet directing use of MCP tools for localization, with fallback to Grep/Read if tools are unavailable.

## Dispatches

1. **harvester** — `book/src/L3/krylov-step.md` (identity-lowering backfill)
   - **Scope**: author firm L3 entry for `krylov-step` using L3 vocabulary; the L4>L3 theme `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` already exists and documents the identity-in-form. The L3 entry must be layer-coherent (readable as an L3 operator definition) and should cite the upstream L4 form in its `Lowers to` section.
   - **Deps**: none
   - **Rationale**: priority #20 first target. Cycle-006's "no L3 row needed" verdict (based on identity-in-form) is superseded by CLAUDE.md §Methodology invariants new bullet and updated harvester.md Discipline bullets. L3 is currently empty (placeholder) despite the lowering chain being firm. This backfill is load-bearing for layer coherence — a reader navigating L3 should find krylov-step defined in L3 vocabulary, not have to jump up to L4.

2. **cross-layer-cross-cutter** — identity-lowering-both-levels audit across L4/L3/L2/L1 cohorts
   - **Scope**: survey the current operator landscape (especially L4/L3/L2/L1 boundaries where identity-in-form rotations exist) to identify other layers where an operator's lower-layer form is value-thread-isomorphic to the upper-layer form but **lacks an explicit lower-layer entry**. Candidates to check: `apply_linop` (L4→L3→L2), `dot` (L3→L2→L1), `axpy` (L3→L2→L1), `nrm2` (L3→L2→L1), `axpby` (L3→L2→L1), `scal` (L3→L2→L1). For each gap found, propose a small harvester dispatch to backfill the missing entry.
   - **Deps**: dispatch #1 (krylov-step L3 backfill should land first, so the auditor has the pattern established)
   - **Rationale**: priority #20 second target. This is foundational work for ensuring each layer is internally coherent. The audit surfaces which backfills are needed; proposed harvester dispatches land in cycle-010 or cycle-011 as capacity allows. Expected output: a `proposed_changes` block with a checklist of identity-in-form candidates and recommendations.

3. **harvester** — `matrix-weighted-norm` L1 rough-in
   - **Scope**: author rough-in L1 entry for `matrix-weighted-norm :: (x, B) → √(xᴴ B x)`. This is a bilinear-form-aware BLAS-1 analog extending the `nrm2` vocabulary. Depends on firm `apply_linop` (cycles-004) and `dot` (cycle-002). Rough-in only (no dedicated test coverage flagged in cycle-009 signals; can promote in cycle-011+ if tests are added).
   - **Deps**: none (both dependencies are firm)
   - **Rationale**: priority #17 (lower-layer-shared-vocabulary) + cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` carry-forward. These operators are needed by the AMS preconditioner, curl-curl projector, and multigrid level recurrences; advancing them reduces duplication in downstream L2/L3 work.

4. **harvester** — `bilinear-form` L1 rough-in
   - **Scope**: author rough-in L1 entry for `bilinear-form :: (x, M, y) → xᴴ M y`. Bilinear-form analog to `dot`, extending the BLAS-1 cohort. Depends on firm `apply_linop` and `dot`.
   - **Deps**: none (both dependencies are firm)
   - **Rationale**: priority #17 (lower-layer-shared-vocabulary) + cycle-008 OQ carry-forward. Bundleable with dispatch #3; distinct rough-in entry.

5. **harvester** — `nrm2_B-weighted-energy-norm` L1 rough-in
   - **Scope**: author rough-in L1 entry for energy-norm variant: `nrm2_energy :: (x, B) → √(xᴴ B x)`. This is a variant axis of the weighted-norm family (similar to `matrix-weighted-norm` in dispatch #3, but carrying slightly different semantics as an energy-norm bound). Depends on `apply_linop` and `dot`.
   - **Deps**: dispatch #3 preferred-before, to establish pattern consistency on the weighted-norm family
   - **Rationale**: priority #13 (cycle-006 integrator-signals unblocked this; test-coverage analysis needed to firm vs rough-in decision). Complements the bilinear-form cohort. Can be bundled with #3 and #4 if scope allows, or deferred to cycle-011.

6. **lifter** — `eigsolve` linear-solve-failed status anchor (constructively-introduced sum-type case)
   - **Scope**: resolve cycle-009 OQ `eigsolve-linear-solve-failed-status-anchor` — the `LinearSolveFailed` result status is constructively introduced by the L1 form (not directly anchored to L0). Decision options: (a) drop the case (collapse to `MaxIterReached`); (b) accept constructive introduction with "constructed by the L1 form" annotation; (c) require L1>L0 lowering theme to plumb the case via inner-solver coupling refactor. Recommend option (b) per the harvester's cycle-009 assessment. Small dispatch; mechanical decision & annotation edit to `book/src/L1/eigsolve.md`.
   - **Deps**: none (eigsolve was landed cycle-009 as rough-in; this is a follow-up refinement)
   - **Rationale**: cycle-009 integrator-signals flagged this as "highest-priority of the four eigsolve firm-promotion follow-ups"; smallest-cost (mechanical decision). Unlocks eigsolve firm-promotion pathway.

7. **same-layer-cross-cutter** — Phase 1 corpus reduction audit, first slice batch
   - **Scope**: audit one or a small cohort of `book/src/spec/slices/` entries whose subject matter overlaps the now-firm krylov-step chain. Example candidates: `slices/ksp_solve.md`, `slices/gmres_iteration.md`, `slices/krylov_step_body.md`. For each slice: verify its content is fully represented in firm L0/L1/L2/L3/L4 entries (cite the specific chapters), identify any residual coverage gaps, propose reduction to a stub (pointing at the firm layered entries) or removal if fully superseded. Output a `proposed_changes` block with checklist and reduction recommendations.
   - **Deps**: dispatch #1 (krylov-step L3 backfill should be in place so the auditor can cite the complete chain)
   - **Rationale**: priority #19 (phase-1-corpus-reduction-audit) first target. Per CLAUDE.md §Methodology invariants "Phase 1 corpus reduces as material is lifted", the corpus should shrink monotonically as the layered surface becomes authoritative. The krylov-step chain is now stable enough (fully firm L4>L3>L2>L1>L0) to support reduction of overlapping slices. This is per-cycle audit work, not a meta-phase enactment.

8. **combinator-miner** — MCP pilot retry: `check_stop_into_carry` helper reuse + codemap localization
   - **Scope**: inspect downstream GMRES-family solvers (FGMRES, IRBL, IDR(s), and any others) to identify whether the `check_stop_into_carry` helper pattern (with 3-condition convergence shape + reason-set enum) reoccurs. Use **MCP codemap tools** (`mcp__palace-codemap__search_text`, `get_symbol_def`, `read_range`) as the primary localization method; fall back to Grep/Read if tools are unavailable. The goal is to validate whether MCP tools meaningfully reduce context budget vs vanilla Grep/Read, and whether "second reuse found" criterion is met for helper promotion.
   - **Deps**: none (inspection-only)
   - **Rationale**: cycle-008 rough-in L4>L3 `gmres-inner-loop-iterate-while-migration` theme flagged `check_stop_into_carry` promotion as "defer until second reuse." The MCP tools are now enabled (commit `ceb87da`); this is the **pilot retry** for the 3-cycle permission-denied friction (friction-ledger entry `mcp-codemap-permission-denied-across-batch-1`). The dispatch is a natural fit for MCP use: need to search for convergence-checking patterns across multiple solver files and read specific ranges for comparison. Expected output: list of matching patterns with citations + evidence on whether second reuse is found (routes to lifter in cycle-010 or cycle-011 if reuse confirmed; or defers if not found).
   - **MCP instructions**: **Use MCP codemap tools as primary localization method.** Call `mcp__palace-codemap__search_text` to find convergence-check patterns (search for `Converged|Diverged|MaxIt` enum patterns across `palace/linalg/` files). When a promising match is found, use `get_symbol_def` to find the symbol's definition and `read_range` to inspect the full context. If any tool call returns `Permission to use ... has been denied`, surface it immediately in the report's Open questions section (friction signal for meta-phase); do NOT silently fall back to vanilla Grep — we need visibility on the permission-denied frequency. Fall back to Grep/Read only if you encounter a tool error outside the permission-denied case.

## Overlap analysis

- **Dispatches #1 (krylov-step L3) + #2 (identity-in-form audit)**: No artifact overlap. #1 authors `book/src/L3/krylov-step.md` (new file); #2 inspects and proposes (no edits). **PARALLEL** (prefer #1 slightly-before #2 for pattern establishment).

- **Dispatches #1 + #3 (matrix-weighted-norm)**: No overlap. #1 touches L3; #3 touches L1 + L1/index. **PARALLEL**.

- **Dispatches #1 + #4 (bilinear-form)**: No overlap. Different layers. **PARALLEL**.

- **Dispatches #1 + #5 (nrm2_B-weighted)**: No overlap. Different layers. **PARALLEL**.

- **Dispatches #1 + #6 (eigsolve lifter)**: No overlap. #1 touches L3; #6 touches L1. **PARALLEL**.

- **Dispatches #1 + #7 (slice reduction audit)**: Potential coordination overlap. Both may reference krylov-step chain, but #1 is artifact edit (new L3 entry) and #7 is inspection-only (proposed reductions, not edits). #1 should land first so #7 can cite the complete chain. **SEQUENTIAL** (#1 then #7, or mark as preferred-before).

- **Dispatches #1 + #8 (combinator-miner MCP)**: No overlap. #1 touches L3; #8 is inspection-only. **PARALLEL**.

- **Dispatches #3 (matrix-weighted-norm) + #4 (bilinear-form) + #5 (nrm2_B-weighted)**: All append to `book/src/L1/index.md` dep-map table. Three distinct L1 entries; per-report re-read discipline will handle cleanly (each report reads current state, proposes append). Per integrator-signals cycle-009 note, appending distinct rows to the same table by multiple dispatches is NOT overlapping at the operational level (not modifying the same operator entry). **PARALLEL** all three.

- **Dispatch #2 (identity-in-form audit) + #7 (slice reduction audit)**: Both are inspection-only and may reference overlapping slices/operators (e.g., both might inspect apply_linop or dot across layers). However, audit-scopes are distinct: #2 is cross-layer operator completeness (which L_n entries are missing); #7 is slice-to-layered-entry supersession (which slices can be reduced). Can run in parallel; slight preference for #1 to land before both audits, so they have complete base state. **PARALLEL**.

- **Dispatch #6 (eigsolve lifter) + #3/#4/#5 (L1 harvesters)**: All may append to L1/index. #6 is a refinement to existing `eigsolve` entry (not new); #3/#4/#5 are new entries. Appending distinct rows is parallel-compatible. Per integrator-signals note, this pattern validated cycle-007. **PARALLEL**.

- **Dispatch #8 (combinator-miner MCP)**: Inspection-only; no artifact edits. No overlaps with other dispatches. **PARALLEL**.

**Summary**: All 8 dispatches are **PARALLEL-compatible except for slight preference that #1 lands before #2 and #7** (so audits have complete base state). If slot budget is tight, prioritize #1 → {#2, #7, #8, #3} as one wave, then {#4, #5, #6} as optional wave-2.

## Sequencing schedule

**Wave 1 (parallel)**: dispatches #1, #2, #3, #4, #8
- **Rationale**: #1 (highest priority, new L3 entry) establishes the identity-lowering pattern; #2, #7, #8 are inspection-only and benefit from #1 being in place but can run in parallel with each other; #3/#4 are independent L1 entries; all five are non-blocking.

**Wave 2 (after wave 1 reports land)**: dispatches #5, #6, #7
- **Rationale**: #5 (nrm2_B-weighted) can bundle with #3/#4 or run after as refinement to weighted-norm family (establishes cohort pattern). #6 (eigsolve lifter) is a small refinement to rough-in (no blocking deps). #7 (slice reduction) benefits from #1 landing (complete krylov-step chain established).

**Preferred execution**: All 8 dispatches across 2 waves:
- **Wave 1**: #1, #2, #3, #4, #8 (5 parallel)
- **Wave 2**: #5, #6, #7 (3 parallel after wave-1 finishes)

**Dispatch cap**: 8 dispatches total, well under the 12-dispatch cycle-010 budget. This allocation aggressively pursues priority #20 (both backfill + audit) and #17 (multiple L1 harvesters) while piloting the MCP tools and beginning the phase-1 corpus reduction audit.

## Open questions / caveats

1. **Dispatch #5 (nrm2_B-weighted-energy-norm) firm vs rough-in decision**: Cycle-009 signals did not include test-coverage analysis for this variant. Before authoring, the harvester should check `reference/palace/test/unit/` for Palace test coverage on energy-norms (search for `energy` + `norm` patterns in test names). If test coverage exists, author as firm; if sparse, rough-in with OQ routing for future firm promotion. Recommend **rough-in as safe default**, allowing cycle-011+ refining-tests dispatch to upgrade if test coverage is added.

2. **Dispatch #2 (identity-in-form audit) output format**: This audit is inspection-only. The expected output is a `proposed_changes` section in the CYCLE.md that lists candidates for backfill (e.g., "apply_linop L3 entry is missing", "dot L2 entry may be missing", etc.) with brief rationale. Each candidate should be routable to a cycle-010+ harvester dispatch. No direct edits to the artifact are expected; all backfills are deferred to follow-up dispatches.

3. **Dispatch #7 (Phase 1 corpus reduction) first-time audit**: This is the **first application** of the phase-1-corpus-reduction-audit pattern. Expected output: a `proposed_changes` section with a checklist of slices audited and reduction recommendations. For each slice, cite the L0/L1/L2/L3/L4 entries that supersede it. If a slice has residual coverage (e.g., a variant axis or edge case not yet captured in layered entries), surface as "reduction blocked by OQ: <new-oq-slug>" and append a new entry to open-questions.md. No direct slice edits this dispatch; reduction edits (stub creation, SUMMARY.md updates) happen in follow-up `same-layer-cross-cutter` or `layer-intro-author` dispatches in cycle-010+ as capacity allows.

4. **Dispatch #8 (combinator-miner MCP pilot) permission-denied fallback**: If any MCP tool call returns `Permission to use ... has been denied`, **do NOT silently fall back to Grep/Read.** Instead, surface the permission-denied error in the report's "Open questions / caveats" section **with the exact tool name and error message**. This is critical friction-signal data for meta-phase evaluation of the MCP rollout (cycle-009 meta-phase could not collect this data due to permission barrier; cycle-010 should be the first instance with MCP access). If tools work cleanly, the report should note "MCP tools used successfully; localization effort reduced by ~X% vs vanilla Grep/Read baseline" (estimate based on elapsed context or call counts).

5. **Dispatch #2 and #7 coordination**: Both are audit-scoped and inspection-only. Dispatch #2 audits operator completeness (cross-layer); dispatch #7 audits slice supersession (slice-to-layered-entry mapping). Both should run in the same cycle (cycle-010), and their findings may overlap slightly (e.g., a slice might reference an operator that #2 found to be missing from a lower layer). Integrator should note any cross-dispatch coordination signals in the wave-1 finalize STAGING log. No blocking dependency between them; parallel-OK.

6. **Identity-lowering precedent (dispatch #1 output)**: The krylov-step L3 entry is the **first identity-lowering backfill** under the new methodology invariant. The harvester should author the L3 entry as a **firm** entry (not rough-in), using L3 vocabulary consistent with L2/L1 sibling entries (axpy, dot, nrm2, etc.). The L4>L3 theme (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`) already documents the identity-in-form; the L3 entry should note this via a `Lowers to` section pointing at the L4 form. Expected L3 entry structure: Signature + Semantics + Algebraic laws + Variant axes (inherited from L4 with L3-vocabulary phrasing) + Lowers to (reference to L4 form and L4>L3 theme). Firmness is load-bearing (the entry must live at L3, not be deferred as rough-in).

7. **Cycle-010 is first batch-2 cycle; no meta-phase looming**: Unlike cycle-009 (last cycle before meta-phase aggregation), cycle-010 has a full 3-cycle horizon. Dispatches do not need to rush completeness for batch-1 closure; work can be staged naturally across 010/011/012. This reduces pressure for overly-large scopes. E.g., dispatch #7 (Phase 1 corpus reduction audit) can be a lean first-pass on just the krylov-step-related slices; follow-ups can audit other slices in cycle-011/012.


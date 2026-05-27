---
agent: cycle-planner
invoked_at: 2026-05-27T16:02:10Z
scope: cycle-007 dispatch plan
status: pending
---

# Cycle-007 dispatch plan

## Goals selected this cycle

Cycle-007 is the **first primary cycle of meta-batch-1** under the new 3:1 meta cadence (cycles 007/008/009 batch; meta-phase fires after 009, not after 007). This cycle completes the krylov-step lowering chain (L3>L2 body-identity theme) and unblocks L4 vocabulary completion (iterate_while promotion from rough-in to firm). Priority #11 threshold is now met (8 L0 chapters ≥ 6 required); retroactive-L1-context-thinning sweep becomes eligible. MCP codemap pilot runs on the first harvester dispatch as a bounded experiment, instrumenting tool-call patterns vs vanilla baseline before broad role-spec rollout in cycle-009 meta-phase. L0 bootstrap bundle-3 continues priority #10.

## Dispatches

| # | Agent | Scope | Deps | Rationale |
|---|---|---|---|---|
| 1 | `harvester` | `iterate_while` + `iterate_while_with_prev` @ L4 (+ **MCP codemap pilot**) | none | Closes `iterate-while-l4-anchor-missing` OQ (cycle-006); firms the two L4 dep-map rough-in rows. **Codemap MCP pilot dispatch**: use `mcp__palace-codemap__*` tools for Palace C++ localization (steps e–f of priority #16); instrument tool-call count + time vs vanilla baseline. Rationale for L4: loop combinators span Palace's iterator implementations; rich C++ surface for pilot. |
| 2 | `abstractor` | `krylov-step-body-identity` @ L3>L2 (short single-theme) | none | Closes `krylov-step-body-identity-theme-pending-cycle-007` OQ; symmetric completion of krylov-step lowering chain (L4 firm + L4>L3 theme → cycle-006; L3>L2 theme → cycle-007; L2 firm → cycle-005). Cycle-006 wave-2 auditor confirmed identity-in-form verdict; low-cost emission (~half dispatch). |
| 3 | `layer-intro-author` | Retroactive-L1-context-thinning sweep over 7 L1 operators | none | Closes priority #11 now-eligible threshold (8 L0 reference chapters ≥ 6 required). Sweep `axpy`, `dot`, `nrm2`, `axpby`, `scal`, `apply_linop`, `axpbypcz` replacing inline L0-interpretation prose in "Context" sections with cross-references to L0 chapters. Distinct from cycle-006's scalar-promotion-specific thinning (#9). Cleanup pass; noticeably shrinks L1 entries. |
| 4 | `layer-intro-author` | L0 bootstrap bundle 3 continuation | none | Priority #10 continuation. Bundle 1 (6 chapters) landed cycle-005; bundle 2 (2 chapters) landed cycle-006; total 8. Candidates for bundle 3: `mpi-globalsum-and-collectives`, `par-types-single-rank-reading`, `mutable-workspace-pattern`, `linalg-operator-file`, `linalg-iterative-file`, `mfem-wrapper-solver` (cycle-006 OQ `mfemwrappersolver-l0-coverage-candidate`), `tests-as-semantic-supplement`. Planner discretion on bundling. |
| 5 | `harvester` | `l1-ksp-solve` @ L1 | none | Closes `l1-ksp-solve-firm-up-anchor-ready` OQ (cycle-006). Both concept-page anchor (`solve-monad`, cycle-002) and L0-anchor entry (`kspsolver-base-class`, cycle-006) now exist. Forward-frontier operator at L1 vocabulary tier. |
| 6 | `lowering-verifier` | `iterate_while` L3 trajectory-accumulation reconciliation | 1 | Resolves the L4 trajectory `[readout]` vs L3 single-readout gap flagged by cycle-006 wave-2 abstractor (open question `iterate-while-l3-rendering-trajectory-accumulation-gap`). **Depends on dispatch 1** landing the L4 `iterate_while` entry to audit against. Per-report serial dispatch order ensures wave-1 dispatch 1's L4 entry is live before this wave-2 dispatch runs. |

## Overlap analysis

- **Dispatches 1, 2**: Disjoint files (L4 operator vs L4>L3 theme; no file overlap). **PARALLEL**.
- **Dispatches 1, 3, 4, 5**: All touch L1/index.md for layer-intro work (dispatches 3/5 for dep-map + context edits). Dispatch 3 is retroactive-thinning of existing L1 operator "Context" sections (prose rewrites; Content → L0 backlinks). Dispatch 5 appends a new firm L1 dep-map row. Row-level appends are distinct; per-report serial dispatch order ensures clean merge. Cycle-004+ friction-ledger (entry `wave-conflict-philosophy-scales`) validates same-file row-level edits at 5+ concurrent writers scale. **PARALLEL**.
- **Dispatch 6**: Depends on dispatch 1's L4 `iterate_while` entry landing. Wave-2, sequential after wave-1.
- **Cross-layer disjointness**: L4 + L4>L3 + L3 + L0 + L1 are separate Parts; no shared layer-intro work. **NO FILE-REGION OVERLAP**.

## Sequencing schedule

**Wave 1 (parallel):** Dispatches 1, 2, 3, 4, 5 run in parallel once planner emits.
- Dispatch 1 includes MCP codemap pilot (steps e–f); instrument and surface results to user (step g) after this wave completes, before cycle-009 meta-phase.

**Wave 2 (sequential after wave-1 ready):** Dispatch 6 runs after dispatch 1's L4 entry is live (per-report serial dispatch design; integrator-per-report #1 applies before per-report #6 is dispatched).

**Rationale for parallel-when-in-doubt:** Cycle-004+ friction-ledger philosophy (user directive 2026-05-27, commit 8fc3a07) — mark PARALLEL by default; minor wave-conflict at integration is useful tooling signal. False sequentialization (dispatches that don't actually conflict) costs throughput and hides integration tooling cases that need attention. Both L1 thinning (#3) and L1 harvest (#5) are row-level ops on the same index; per-report serial dispatch handles concurrent writers cleanly at 5+ wave-mate scale (validated cycles 003–004).

## Open questions / caveats

1. **MCP codemap pilot success metrics (cycle-007, step g):** After wave-1 ready, surface to user: (i) did the codemap tools resolve C++ source locations faster/cheaper than vanilla grep+Bash alternatives? (ii) what call patterns emerged? (iii) are role-spec updates (step d, deferred to cycle-009 meta-phase) justified? Currently no data; pilot is the measurement phase. If codemap shows no performance win, defer tool rollout pending future optimization.

2. **L0 bootstrap bundle 3 scope**: Planner listed 7 candidates but did not pre-assign bundling granularity. Dispatch #4 should read `scaffolding/priorities.md` item #10 at invocation time to pick next candidates. Suggest: 2–3 chapters per bundle (cycle-005 = 6, cycle-006 = 2; cycle-007 could be 2–3 to amortize across cycles 007–009). Item `mfem-wrapper-solver` is explicitly named in OQ as future bundle-3 candidate (cycle-006 OQ `mfemwrappersolver-l0-coverage-candidate`); recommend inclusion.

3. **Cycle-007 is cadence-aware under 3:1 meta batching**: Friction-ledger and open-questions entries may be ~3 cycles stale by cycle-009 meta-phase (since meta-phase fires only every 3rd primary cycle, not every cycle). Cycle-007 planner should surface methodology observations discovered this cycle directly to open-questions.md (append-only discipline), not wait for meta-phase. If a pattern emerges (e.g., a role spec recurrently fights its task, a new agent type would simplify work), append to open-questions.md with slug and context; meta-phase will aggregate across the 3-cycle batch.

4. **Session restart and MCP reintegration**: This plan assumes a session restart has occurred (per cycle-007-resume-notes step 2–3). Deferred-tools list should include `mcp__palace-codemap__*` entries at dispatch time (confirming steps a–c of priority #16 completed). If restart has not occurred or codemap tools are not loaded, dispatch #1 (harvester) should fallback to vanilla Bash/Grep and note the gap in CYCLE.md caveats for user escalation.

5. **`iterate_while` complexity via rough-in**: The L4 `iterate_while` was roughed-in with two variant rows in cycle-006 (`iterate_while`, `iterate_while_with_prev` — the latter is the PrevCarry=non-empty variant). The harvester role spec says "one operator per invocation" but these are lexically distinct names at L4. Recommend bundling as a **single dispatch "iterate_while family"** (not two separate dispatches) on the rationale that they form a cohort (conditional carry parameter, same loop-combinator semantics). Precedent: cycle-004 harvester bundle-bundled `axpy` + `axpbypcz` (separate operators, both harvest-able; no precedent for variant-axis bundling, but same-operator multi-variant is handled in a single dispatch by the role spec's "variant-axis absorption at construction" guideline). This dispatch is not a multi-variant single-operator case (two distinct operators), but the semantic grouping (loop combinator family) justifies single invocation.

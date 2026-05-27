---
agent: cycle-planner
invoked_at: 2026-05-27T00:44:11Z
scope: cycle-004 dispatch plan
status: pending
---

# Cycle 004 dispatch plan

## Goals selected this cycle

Firm L1 vocabulary through six core operators (`scal`, `apply_linop`, `axpbypcz`) to unblock krylov-step promotion and L1 layer-intro refresh. Fix concepts/dot.md contradictions routed by cycle-003 cross-cutter. Begin Shared Infrastructure cohort (MINRES, BiCGStab) per user directive 2026-05-27 (raised above per-solver work). Harvest cycles 002–003 forward-frontier work with parallel-when-in-doubt dispatch strategy to stress-test higher capacity (8 dispatches, aiming for 8–12 range).

## Dispatches

| # | Agent | Scope | Deps | Rationale |
|---|---|---|---|---|
| 1 | `layer-intro-author` | `book/src/concepts/dot.md` rewrite to align with L1/dot.md authoritative entry | none | Priority #2. Fixes three cycle-003 cross-cutter-observed contradictions (return-type, nonexistent Dotc, inverted-conjugation, bogus vector.cpp citation). Closes open questions `concepts-dot-return-type-correction` + `concepts-dot-dotc-and-inverted-conjugation`. Role scope broadened cycle-003 meta-phase. |
| 2 | `layer-intro-author` | `book/src/L1/index.md` intro + dep-map prose refresh (4 firm operators now: axpy, dot, nrm2, axpby) | none | Priority #3. Threshold met (≥3 firm L1 operators per pilot-1 trigger). Integrator-signals cycle-003 §Unblocked lists this as tractable. Can co-bundle with dispatch #1 under same role (two outputs). |
| 3 | `harvester` | `scal` at L1 (small primitive; referenced in `axpby` laws 2/3 + `linalg::Normalize`) | none | Priority #4. Open question `scal-primitive-l1-harvest`. Forward-frontier buildup of L1 vocabulary. Row-append to L1 dep-map (non-overlapping with #4, #5 per cycle-003 signals). |
| 4 | `harvester` | `apply_linop` at L1 (operator-application primitive; gates krylov-step + nrm2_B) | none | Priority #5. Substantial L0 surface (`mfem::Operator::Mult`, `palace::ParOperator::Mult`, `linalg::Operator`). Unblocks dispatch #6 (krylov-step harvester). Row-append to L1 dep-map (non-overlapping with #3, #5). |
| 5 | `harvester` | `axpbypcz` at L1 (cycle-003 lowering-verifier confirmed evidence; internal AXPBY+Add composition; `vector.cpp:756`) | none | Priority #7. Open question `axpbypcz-l1-harvest` + `axpby-corpus-coverage-exhaustive-indexing` deferred piece. Row-append to L1 dep-map (non-overlapping with #3, #4). |
| 6 | `harvester` | `krylov-step` L2 promotion (firm: six deliverables per open question `krylov-step-harvester-deliverables`) | 4 | Priority #6. Depends on apply_linop (#4) L1 firmness for stable L1 dep-map. Integrator-signals: "approaches tractable" once apply_linop lands. Foundational L2 primitive. |
| 7 | `harvester` or `slice-author` | MINRES L0→L1 (shared infrastructure: symmetric-indefinite three-term recurrence; Krylov solver sibling to CG, GMRES) | none | Priority #10 (user directive 2026-05-27: Shared Infrastructure raised above per-solver). Roadmap §Shared infrastructure / Krylov solvers. New ground; substantial L0 surface. Candidate for two-step harvest (cycle-004: L0→L1 operator-level + L1 form; cycle-005: integrations into solvers). |
| 8 | `harvester` or `slice-author` | BiCGStab L0→L1 (shared infrastructure: non-symmetric short-recurrence Krylov variant) | none | Priority #11 (user directive). Roadmap §Shared infrastructure / Krylov solvers. Sibling to MINRES (#7); new ground. |

## Overlap analysis

**Same-role sequential bundling (no artifact overlap):**
- Dispatches 1 + 2 both route to `layer-intro-author` but output to distinct files (`book/src/concepts/dot.md` vs `book/src/L1/index.md`). Cycle-003 integrator cleaned two harvesters' same-file dep-map edits via row-level anchoring; same pattern applies to role-pair. **Mark PARALLEL** (planner emits both at dispatch time; role can sequence internally if preferred, or emit sequentially if output coupling exists).

**Dependency edge:**
- Dispatch 6 (`krylov-step` harvester) **depends on dispatch 4** (`apply_linop` harvester). The L1 dep-map must include apply_linop before krylov-step can be promoted with a stable set of L1 deps. Cycle-003 integrator-signals explicitly states "krylov-step harvester can proceed with stable L1 deps once apply_linop lands". **Mark SEQUENTIAL: 6 blocks on 4**.

**Row-level non-overlapping dep-map appends:**
- Dispatches 3, 4, 5 all append rows to `book/src/L1/index.md` dep-map. Per cycle-003 wave-conflict observations, row-level edits with distinct anchors (each appending a new operator row) are zero-friction at integration. Cycle-003 nrm2 + axpby case proves the pattern. **Mark PARALLEL** (conflict-when-in-doubt philosophy; cycle-003 signals show same-file non-overlapping row appends clean up at integration).

**Greenfield slices:**
- Dispatches 7, 8 (MINRES, BiCGStab) are new slices; they output to distinct new operator files. **Mark PARALLEL** (no shared surfaces with each other or existing operators).

**No operator-entry overlaps:** All 8 dispatches propose distinct outputs. Dispatches 3–5 share a table (L1/index.md dep-map) but with distinct row anchors. No two dispatches rewrite the same file or the same operator entry.

## Sequencing schedule

**Wave 1** (parallel, emit all together):
- Dispatch 1: `layer-intro-author` → `concepts/dot.md` rewrite
- Dispatch 2: `layer-intro-author` → `L1/index.md` refresh
- Dispatch 3: `harvester` → `scal` L1
- Dispatch 4: `harvester` → `apply_linop` L1
- Dispatch 5: `harvester` → `axpbypcz` L1
- Dispatch 7: `harvester`/`slice-author` → MINRES L0→L1
- Dispatch 8: `harvester`/`slice-author` → BiCGStab L0→L1

**Wave 2** (after wave-1 reports land and are integrated):
- Dispatch 6: `harvester` → `krylov-step` L2 promotion (unblocked by apply_linop landing in wave-1)

## Open questions / caveats

1. **Scope subdivision for apply_linop** — The integrator-signals cycle-003 note flags apply_linop as having "substantial L0 surface (`mfem::Operator::Mult`, `palace::ParOperator::Mult`, `linalg::Operator`)". Cycle-planner decided not to subdivide (one harvester dispatch per priority spec), but if the specialist encounters a scope balloon during iteration, recommend escalating to a two-dispatch sequence (operator discovery + L1 form) at repair time.

2. **MINRES / BiCGStab role selection** — Dispatches 7–8 list agent as `harvester or slice-author`. The user directive raised Shared Infrastructure priority but did not specify which agent role owns solver-component L0→L1 formalization. Cycle-planner recommends `harvester` (consistent with L1 vocabulary buildup); if the specialist discovers that the algorithm structure is less of a "pure primitive harvest" and more of a "sliced-down solver component", the expert may choose `slice-author` instead. Either role should work for the initial L0→L1 pass.

3. **Wave-1 capacity and integration buffer** — 7 dispatches in wave-1 is on the high end of cycle-003's observed 4-report batch. Integrator reported zero friction, but integration load may climb. No escalation planned; flagging for meta-phase observation in cycle-004 meta report (watch integrator token budget + repair rate).

4. **Concepts/dot rewrite scope** — Dispatch #1 must align with the L1/dot.md target that landed in cycle-002. If cycle-002's L1/dot.md or any upstream L0 citation has drifted since cycle-002 commit, the rewrite may need secondary adjustments. Recommend the specialist re-cite L0 ground-truth at rewrite time (per CLAUDE.md methodology invariant: "every claim carries a citation").

5. **krylov-step promotion blockers** — Dispatch #6 is gated on dispatch #4's integration. If apply_linop repair or integration surfaces unexpected blockers (e.g., tokenization overruns, L0 citation ambiguities), krylov-step may be deferred to cycle-005. Flag for integrator signals.

**Status: ready for dispatch.**

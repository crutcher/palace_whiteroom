---
agent: cycle-planner
invoked_at: 2026-05-27T00:08:44Z
scope: cycle-003 dispatch plan
status: pending
---

# Cycle 003 dispatch plan

## Goals selected this cycle

Bootstrap core L1 vocabulary by harvesting `nrm2` and firming `axpby` into the L1 dep-map, then audit the `axpby-mutation-rotation` lowering theme against full L0 corpus and reconcile long-standing `dot` concept-page contradictions. This sequence advances the immediate backlog (priorities #1–4) without exceeding integrator capacity (4 dispatches, 3 agents).

## Dispatches

| # | Agent | Scope | Deps | Rationale |
|---|---|---|---|---|
| 1 | harvester | `nrm2` at L1 | none | Priority #1: formalize vector-norm operator; provides one of the three remaining core L1 vocabulary items (`nrm2`, `scal`, `apply_linop`). Single operator per role spec. |
| 2 | harvester | `axpby` at L1 (firm) | 1 | Priority #2: promote cycle-002 rough-in (`axpby-mutation-rotation` theme rough-in already landed, now waiting on L1 operator firmness). Dispatch 1 unblocks by populating L1 dep-map; axpby firmness removes rough-in row placeholder. Single operator per role spec. |
| 3 | lowering-verifier | `axpby-mutation-rotation` theme audit | 1 | Priority #3: resolve the three sub-patterns A/B/C against full L0 corpus per open question `axpby-lowering-verifier-audit`. Addresses the pre-integration unrepairable finding from cycle-002 (theme awaits lowering-verifier). Non-overlapping with L1 writes; depends on L1 state firmness for confidence. |
| 4 | same-layer-cross-cutter | `concepts/dot.md` reconciliation | 1 | Priority #4: fix two long-standing contradictions (return-type claim; missing `linalg::Dotc` + inverted conjugation) routed to this agent by cycle-002 harvester. Non-overlapping artifact. Parallel with 2–3 (concept is separate layer from L1 operators). |

## Overlap analysis

**Within-wave overlaps:**
- Dispatches 1 & 2: both append to `book/src/L1/index.md` (dep-map table rows). One writes `nrm2` row; two updates `axpby` row (converts rough-in placeholder to firm entry with link). These **OVERLAP** on the same file region → must be sequential (1 then 2).
- Dispatches 1 & 3: nrm2 writes `book/src/L1/nrm2.md`; lowering-verifier audits `book/src/L1-L0/axpby-mutation-rotation.md` and L0 corpus. No shared artifacts → **non-overlapping**.
- Dispatches 1 & 4: nrm2 at L1 operator; cross-cutter at `book/src/concepts/dot.md`. No shared artifacts → **non-overlapping**.
- Dispatches 2 & 3: axpby writes `book/src/L1/axpby.md` + updates L1/index.md; lowering-verifier reads and audits the L1>L0 theme (expects L1 operator to be firm, but does not write to L1 files). Lowering-verifier consumes the L1 state but does not conflict → **non-overlapping** (3 depends on 2's L1 update for context, not file write).
- Dispatches 2 & 4: axpby at L1; cross-cutter at concepts. No shared artifacts → **non-overlapping**.
- Dispatches 3 & 4: lowering-verifier at L1>L0 theme; cross-cutter at concepts. No shared artifacts → **non-overlapping**.

## Sequencing schedule

**Wave 1 (parallel not applicable; single dispatch):**
- Dispatch 1: `harvester / nrm2 / L1`

**Wave 2 (parallel, after wave-1 report lands):**
- Dispatch 2: `harvester / axpby / L1` (sequential after 1 due to L1/index.md overlap)
- Dispatch 3: `lowering-verifier / axpby-mutation-rotation / L1>L0` (parallel with 2; depends on 1's report for L1 context)
- Dispatch 4: `same-layer-cross-cutter / dot-concepts / concepts` (parallel with 2 & 3)

Alternative: **Collapse wave 2 dispatches 2 & 3 into sequential block if integrator prefers single batch:** dispatch 1 → (dispatch 2 → dispatch 3) → dispatch 4 in parallel with (2 & 3). Current schedule respects the L1/index.md overlap constraint while allowing 3 & 4 to parallelize with the 2-then-3 sequence.

## Open questions / caveats

- **Dispatch 3 scope (lowering-verifier):** Open question `axpby-lowering-verifier-audit` calls for sub-rule exhaustiveness audit on three patterns. Specification is tight (open question lists the two sub-claims to verify). No ambiguity; included dispatch.
- **Dispatch 4 scope (same-layer-cross-cutter):** Two open questions bundled (`concepts-dot-return-type-correction` + `concepts-dot-dotc-and-inverted-conjugation`). Cross-cutter's role covers this. No role-scope friction expected.
- **Dispatch 2 decision tree:** Cycle-002 open question `axpby-axpy-scal-decomposition-decision` asks whether `axpby` is a fused primitive or decomposes to `axpy ∘ scal`. Harvester will need to make this call and record in `scaffolding/decisions/axpby-as-primitive.md`. Plan does not pre-decide; harvester is scoped to author the decision based on evidence.
- **Priority #5 deferral:** `harvester-promote-krylov-step` depends on L1 vocabulary firming. With nrm2 + axpby landing this cycle, the L1 vocab reaches 3 operators (axpy + dot + nrm2) + rough-in (axpby + scal + apply_linop planned). Krylov-step promotion is unblocked for cycle-004 but not dispatched this cycle to avoid overload (4 dispatches per CLAUDE.md guidance is upper end).

---
verifies: ../CYCLE.md
critiqued_at: 2026-06-08T054500Z
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

# META: verification of "Audit eigsolve-impl-realizes-kernel-api-reaudit-lanczos"

## Critique

### Checks run

**citation-validity — pass.** This is the load-bearing axis for an audit-class report. I verified every cited pinpoint independently. The six Palace Hermitian-arm + opaque-loop anchors all land exact under `citecheck --anchor`: `slepc.cpp:607` (`EPS_HEP`), `:613` (`EPS_GHEP`), `:635` (`EPSKRYLOVSCHUR`), `:694` (`EPSSolve`), `arpack.cpp:318` (`naupd`), `:369` (`neupd`) — each `1 ok, 0 failing`, zero drift. The book-internal cites are accurate on disk: `eigsolve.md:4` is `firmness: partial-obstruction`; `:191` (within the §Status block the verified_against entry cites as `:189-195`) carries the `kernel-api` role-label and the explicit "status is UNCHANGED" clause; `eigsolve-impl.md:19-21` is the `reference:`-block `realizes-kernel-api` edge; `:11-12` the `lanczos_step` `folds` `depends-on`; `:24` the semantics USE+LINK note; `:81-83` the `if op.hermitian then lanczos_step else krylov-step` body gate; `:134-136` the §Status with the two-armed promotion route; `lanczos_step.md:5-6` on-disk `roadmap_goal`/`rank: roadmap_goal`. The coupled cross-check is correct: `L1/index.md:179` is the `nleps_deflated_residual` row and `:202` is the `lanczos_step` row, so the report's confirmation of the D2 `:179→:202` fix is right. **YAML round-trip sub-check:** I extracted the proposed `verified_against:` payload and ran it through `yaml.safe_load` — it round-trips cleanly (8 entries, top key `verified_against`), and no `note:` value begins with a leading quote of either kind (first chars: `c`, `l`, `E`×4, `n`×2) — no `ParserError`-signature defect.

**surface-or-evidence — pass.** Adapted for the lowering-verifier audit kind: the report authors NO book content — it only appends a `verified_against:` audit block, which is the canonical retroactive-evidence-backfill shape, not a surface modification. No record is newly named in a signature here (the records in play — `DeflationState`, `NonlinearPencil`, etc. — are referenced from already-defined homes, not introduced), so the record-definition sub-check no-ops. The audit's evidence (Palace anchors + on-disk edge/status facts) backs every verdict.

**rotation-quality — pass (not applicable to audit-class report).** No algebraic/structural/reduction rotation is asserted; the report verifies an existing impl↔api correspondence and explicitly defers the empirical-match (eigenpair-equality) claim to firming. Nothing to grade for compaction/abstraction.

**variant-axis-coverage — pass.** The eigsolve-impl's variant axes (eigen-algorithm, problem-symmetry, spectral-transformation, problem-type, restart-shape) live in the chapter under audit, not in this report. The audit correctly scopes itself to the problem-symmetry Hermitian arm (the c139-lanczos-coupled slice) and explicitly states it is the structural-correspondence + edge-integrity check appropriate at rank 0; it does not silently hide an unaudited branch.

**cross-reference-integrity — pass.** All cross-references resolve: `L3/eigsolve.md`, `L3/eigsolve-impl.md`, `L3/lanczos_step.md`, `L1/index.md`, `L4/eigsolve.md`, and the cited Palace source files all exist and the named line ranges are in-range. The proposed `edit:` block targets `book/src/L3/eigsolve-impl.md` and appends to its existing `verified_against:` YAML; on disk that file is 195 lines and the existing block's last entry (c124-D2) ends at line 194 with the closing fence on line 195 — the append target ("after the c124-D2 entry at line 194") is accurate. No firm-body-inside-fence guard applies (this is an audit append, not a firm-chapter authoring block).

**edge-label-fidelity — pass.** The report carries the `realizes-kernel-api` edge (eigsolve-impl → eigsolve) and the prose discusses exactly that edge: it confirms the edge is `reference`-class (not `depends-on`), at `eigsolve-impl.md:19-21`, and that no `depends-on` to either L3 or L4 kernel-api exists. The edge label and the prose are in agreement.

**plan-kind-consistency — pass.** The declared kind is an audit (lowering-verifier, verdict FULLY-SUPPORTED). The content matches: per-citation verdicts, applicability conditions, a `verified_against:` append, and no new rank/maturity claim. Per the graded-stack rank-invariant + reachability checks, an audit chapter asserts no rank of its own; the report correctly observes the rank-0-on-rank-0 well-foundedness of the audited node (`roadmap_goal` impl resting on `roadmap_goal` lanczos_step, `0 ≤ 0`) and the firm deps (`0 ≤ 3`) without itself making a maturity claim. No mis-classification.

**skill-uptake-survey — pass.** The report's shape (citation re-audit) implies `citecheck --anchor`, and the report explicitly references invoking it on all six Palace anchors with `OK` results (§Per-citation audit, §Supporting evidence). Telemetry: the audit-relevant tooling is surfaced.

### Issues found

None. All eight checks pass. The six Palace anchors land exact under independent `citecheck --anchor` runs; the four DIRECTIVE-3 integrity invariants are verifiable on disk exactly as the report states (reference-class edge at `eigsolve-impl.md:19-21`; `eigsolve.md:4`/`:191` partial-obstruction undowngraded; USE+LINK semantics with no restatement; Hermitian arm consistent with `lanczos_step` staying `roadmap_goal`, promotion correctly not firing); the proposed `verified_against:` YAML round-trips cleanly with no leading-quote violation; and the coupled `L1/index.md:179→:202` cross-check is correct on disk. `overall_status: ready` set (all-pass clean report; no repairer will run).

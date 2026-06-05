---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T073000Z
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
repaired_at: 2026-06-05T074500Z
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

# META: verification of "P1 typed-edge pass — concepts/ cluster B"

## Critique

### Checks run

**citation-validity — pass (load-bearing for config-record).** The only file edit is the `edges:` frontmatter block on `concepts/config-record.md`; its three `depends-on / kind: cites-evidence` ranges were re-verified against L0 source via codemap `read_range`. `palace/utils/iodata.hpp:31-60` shows the `class IoData` body — the five `config::` sub-record members (`ProblemData problem`, `ModelData model`, `DomainData domains`, `BoundaryData boundaries`, `SolverData solver`) + the `Units` helper + the parsing ctors. Confirmed it is the backing aggregate. `palace/utils/labels.hpp:18-26` is exactly `enum class ProblemType : char { DRIVEN, EIGENMODE, ELECTROSTATIC, MAGNETOSTATIC, TRANSIENT, BOUNDARYMODE }` — the driver-selector enum, range exact. `palace/utils/configfile.hpp:57-1026` opens at `struct ProblemData` (first `config::` sub-record, line 57) and the span end at 1026 lands at the close of the `LinearSolverData`/`SolverData` cluster — a sound span-bounds over the config:: sub-record structs. All three citations genuinely back the record-definition. No `verified_against:` block is present in this report, so the YAML round-trip sub-check is not applicable. The edge ranges are pointer edges over citations the page body already carries (re-confirmed: body cites `iodata.hpp:27-61/:54/:60`, `main.cpp:231`, `configfile.hpp`), not new claims.

**surface-or-evidence (record-definition sub-check) — pass.** `config-record` is correctly treated as a record-definition NODE: it has a definition home (the existing `## L0 home`, `## Schema` sections defining fields/types/stratum/L0 backing struct), names the `IoData` data shape ≥2 signatures rest on, and cites the backing C++ struct. This is the proper home, not a "described-only-by-use" gap. The report authors no new per-op surface and makes no new algebraic claim — it is a pure typed-edge/frontmatter pass (a metadata backfill), so the surface-vs-evidence obligation is satisfied (the record's evidence is its already-cited L0 backing struct). The 16 non-nodes assert nothing and add nothing to disk.

**rotation-quality — pass (not applicable to a typed-edge/frontmatter pass).** No algebraic/structural rotation is asserted; this dispatch classifies node-vs-not-a-node and emits one `edges:` block. No rotation claim to grade.

**variant-axis-coverage — pass (not applicable).** No operator with orthogonal variant axes is authored. The config-record page is a data-shape definition with no variant branches.

**cross-reference-integrity — pass (load-bearing for this kind).** All 8 `edges:` targets were confirmed present on disk via `ls`: `concepts/build-time-vs-run-time-stratification.md` and the seven feature columns (`feature/lifecycle.L4`, `electrostatic.L4`, `magnetostatic.L4`, `driven.L4`, `transient.L4`, `eigenmode.L4`, `boundary-mode.L4`). No dangling reference. The three `cites-evidence` targets are raw `palace/...:lines` strings (not link-checked, and verified above as in-range). The body's existing intra-page link (`build-time-vs-run-time-stratification`) also resolves.

**edge-label-fidelity — pass.** The `depends-on`(L0 cites-evidence) vs `reference`(feature roots + sibling concept) split is correct per the scheme. Verified against `graded-stack-scheme.md` §2: "an edge to a feature root is `reference`, never `depends-on`" (lines 97-98, 112-114) and §6 checklist item 2 ("an `l0_ground_truth` / evidence citation is a `depends-on` with `kind: cites-evidence`"). The six driver columns + lifecycle ROOT are feature roots, so `reference` is the correct bucket; the L0 backing struct is the evidence the record rests on, so `depends-on / cites-evidence` is correct. The split is applied exactly as the scheme prescribes.

**plan-kind-consistency — pass.** Declared shape is a graded-stack P1 typed-edge pass: classify 17 concept pages, emit `rank:`+`edges:` only for genuine DAG nodes. Content matches — one node (`config-record`, `rank: firm`), 16 deliberately-classified non-nodes with no frontmatter. The `rank: firm` is consistent with the page's cited backing struct (scheme §5: record-definition node is firm once its L0 backing struct is cited). No mis-classification; the classification table documents each determination with rationale.

**skill-uptake-survey — warning.** The dispatch shape (typed-edge classification, node-vs-not-a-node boundary calls, `rank:`/`edges:` emission per the graded-stack scheme) is exactly the kind of repeated procedure that a `graded-stack-edge-typing` or `concept-node-classification` skill would standardize — and the report itself flags a cross-dispatch convention divergence (D2 no-frontmatter vs D1/D3 reference-only blocks) that a shared skill would have prevented. No skill is referenced as invoked. This is telemetry, not blocking: the campaign is new (P1, first batch) so no skill exists yet; the divergence (see Issues) is the natural signal that one should be proposed. Surfaced for the meta-phase.

### Issues found

1. **Cross-dispatch convention divergence: D2 writes NO frontmatter for non-nodes; siblings D1 (cluster-a) and D3 (cluster-c) write `reference:`-only blocks** (`CYCLE.md` §"Node-status convention applied" + the report's own OQ `graded-stack-concept-node-status-convention`). Confirmed by inspection: `2026-06-05T071838Z-...-cluster-a/CYCLE.md` and `2026-06-05T071837Z-...-cluster-c/CYCLE.md` both emit `reference:` blocks. D2's choice is **scheme-permitted, not a defect**: `graded-stack-scheme.md` §6 checklist item 4 states "a methodology / process / narrative-concept page carries **no** `rank:`/`edges:` (§2d)", and §2d/§5 place narrative-pointer and methodology concept pages outside the subject DAG. So a non-node legitimately carries nothing. The divergence is a real cross-dispatch inconsistency that needs central unification (does a non-node get nothing, or a navigational `reference:`-only block?), but per the scheme as written D2 is the literal-compliant reading. Severity: low / unification-only — flag for meta-phase, NOT a content defect in this report. The report correctly routes it as an OQ.

2. **`config-record` is unreachable-garbage under the reachability GC — finding is real and correctly routed, not fixed** (`CYCLE.md` OQ `config-record-reachability-gap`). Verified against `graded-stack-scheme.md` §2: `reference` edges "carry **no** liveness" (line 105-108), and the reachability GC "marks from every `feature_root: seed` node over `depends-on` edges" (line 159). config-record's only inbound/outbound root edges are `reference`, so it is genuinely unreachable until a consumer adds an inbound `depends-on / kind: uses-record`. The report's diagnosis is correct, and routing the fix to the feature-column typing dispatch (feature columns are out of D2's page set) rather than reaching outside scope is the right call. Severity: informational — a correctly-surfaced cross-node finding, not a defect; the baseline-exception is expected under the audit-first/bounded-baseline-exception adoption model (CLAUDE.md graded-stack directive).

3. **Two borderline non-node calls (`counter-update`, `chebyshev-iteration`) resolved conservatively as non-nodes; flagged for meta-phase reconciliation** (`CYCLE.md` §"Boundary calls" + table rows). `counter-update` is the sole-definition site of an L2 primitive a real node (`L4/preconditioning-framework`) depends on, which under a slightly different unified rule could flip to a node; `chebyshev-iteration` is pre-redirect background with no authoritative-L_n forward. Both calls are defensible under the three-rule convention the report applies and are explicitly flagged as OQ. Severity: low / unification-only — judgment calls correctly surfaced for cross-dispatch reconciliation, not defects.

No citation, edge, cross-reference, or classification defect was found. The single proposed edit is build-safe (frontmatter prepend; mdBook + linkcheck2 ignore frontmatter; no body link syntax added; all targets verified). The warning is the skill-uptake-survey telemetry + the routed divergence/reachability findings, all of which are unification/routing items for the meta-phase rather than content defects in this report.

## Repair

### Fixes attempted

- **Finding**: skill-uptake-survey WARNING — cross-dispatch node-status convention divergence (D2 writes NO frontmatter on the 16 non-node concept pages; siblings D1/D3 write `reference`-only `edges:` blocks on their non-nodes).
  - **Decision**: not-needed (ACCEPT-AND-ROUTE — already routed for meta-phase).
  - **Rationale**: This is NOT repairable-in-place. Both encodings agree on node-status (non-node, no `rank:`, outside the subject DAG) and the critic confirmed D2's choice is scheme-permitted (`graded-stack-scheme.md` §6 checklist item 4: a methodology/process/narrative-concept page carries no `rank:`/`edges:`). The reconciliation is **linter-invariant either way** (a non-node contributes only `reference` edges, which carry no liveness and no rank constraint). Normalizing D2 to match D1/D3 (or vice-versa) would pre-empt the scheme-level encoding decision the planner *deliberately deferred* to batch-close — that decision is meta-phase-owned, not repair authority. **Routing verified**: the divergence is captured as an OQ in two places — (i) D4's infra-reconcile report (`reports/2026-06-05T072504Z-layer-intro-author-p1-concepts-infra-reconcile/CYCLE.md`) created the OQ `graded-stack-concept-nonnode-edges-block-d1d3-vs-d2` (CYCLE.md lines 540-545: states the divergence, both agree on node-status, asks meta-phase to pick one encoding, notes linter-invariance); and (ii) this report's own OQ `graded-stack-concept-node-status-convention` (CYCLE.md lines 176-182). No edit applied; the convention is left for batch-close unification. (A `graded-stack-edge-typing` / `concept-node-classification` skill candidate is the natural downstream signal — meta-phase territory, not appended here as the campaign is P1-first-batch.)

- **Finding**: `config-record` node typing soundness (3 L0 cites + the `depends-on`/`reference` split) — verify, do not author.
  - **Decision**: not-needed (sound; confirmed, no fix).
  - **Rationale**: The critic re-verified all three `depends-on / cites-evidence` ranges against L0 via codemap (`iodata.hpp:31-60` = the `IoData` aggregate with its five `config::` sub-records; `labels.hpp:18-26` = the `ProblemType` driver-selector enum; `configfile.hpp:57-1026` = the config:: sub-record structs). The repairer spot-confirmed the tightest bound — `labels.hpp:18-26` is range-exact `enum class ProblemType : char { DRIVEN, EIGENMODE, ELECTROSTATIC, MAGNETOSTATIC, TRANSIENT, BOUNDARYMODE }`. The split is scheme-correct: L0 backing-struct evidence the record rests on → `depends-on / cites-evidence`; the 7 feature roots + the sibling concept the page serves/cross-links → `reference` (an edge to a feature root is `reference`, never `depends-on`, per scheme §3). `rank: firm` is consistent with the cited backing struct (scheme §5 record sub-case). No defect; no edit.

- **Finding**: `config-record` is unreachable-garbage under the reachability GC (`config-record-reachability-gap`).
  - **Decision**: not-needed (correctly routed, not fixed).
  - **Rationale**: The faithful fix — an inbound `depends-on / kind: uses-record` edge from each consuming feature column → `concepts/config-record` — is out of D2's page set (feature-column typing is another dispatch's scope). Reaching outside scope to add it would be improper; the report routes it to the feature-column typing dispatch. This is an expected bounded baseline-exception under the audit-first / hard-gate-new / tracked-baseline-exception adoption model (CLAUDE.md graded-stack directive). The GC correctly flags it as unreachable until the consumer edge lands. No edit; routing is correct as written.

### Unrepairable findings

None. The single non-pass (skill-uptake-survey warning) is telemetry whose underlying divergence and reachability findings are already routed as OQs for the meta-phase; no `unrepairable` deferral is needed and no follow-up agent is required for this report (the OQ owner is the batch-close meta-phase, not a per-report follow-up agent).

## Suggested resolution

`overall_status: ready`. All 7 critic checks pass; the lone `skill-uptake-survey` warning is non-blocking telemetry plus two correctly-routed cross-node findings (the node-status encoding divergence and the config-record reachability gap), both captured as OQs (`graded-stack-concept-nonnode-edges-block-d1d3-vs-d2`, `graded-stack-concept-node-status-convention`, `config-record-reachability-gap`) for batch-close meta-phase unification. **Integrator notes:** apply the single `edges:` frontmatter block on `concepts/config-record.md` (the one real node, `rank: firm`); it is build-safe (frontmatter prepend; mdBook + linkcheck2 ignore frontmatter; no body link syntax; all 8 book-node targets verified on disk). The 16 non-node pages get no edit — that is the deliberate, scheme-permitted D2 classification, not an omission. Expect the reachability GC to flag `config-record` as unreachable until the feature-column typing dispatch adds the inbound `uses-record` edges; that is the expected tracked baseline-exception, not a build break.

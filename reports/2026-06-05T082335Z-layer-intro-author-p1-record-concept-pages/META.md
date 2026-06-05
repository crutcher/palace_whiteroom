---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T00:00:00Z
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

# META: verification of "type the 6 RECORD concept pages (krylov, op-params, sim-state, step-outputs, prev-carry, solve-result)"

## Critique

### Checks run

**citation-validity (LOAD-BEARING) — pass.** Every `depends-on` `cites-evidence` target was re-verified against `palace/linalg/iterative.{hpp,cpp}` via codemap `read_range` this dispatch. Confirmed exactly: `IterativeSolver` opens at `:26`; `rel_tol, abs_tol` `:41`; `max_it` `:44`; `A`/`B` `:48-49`; mutable solve-statistics `converged/initial_res,final_res/final_it` `:52-54`; accessor surface `GetConverged/…/GetNumIterations` `:97-108`; `class CgSolver` opens `:118` with workspace `mutable VecType r, z, p;` at `:144`; `class GmresSolver` opens `:155` with the `V/r/H/s,sn/cs` workspace block `:189-193`, `Initialize()/Update(int)` decls `:197-198`, GMRES `Mult` `:216`; `class FgmresSolver` opens `:222` with `mutable std::vector<VecType> Z;` `:256`. On the `.cpp` side: `CheckDot` guard `:21-31`; PCG residual proxy `beta = linalg::Dot(comm, z, r)` `:395`, `CheckDot` `:396`, `res = std::sqrt(std::abs(beta))` `:397`; GMRES `beta = std::abs(s[j+1])` `:642`, `CheckDot` `:643`, `converged = (beta < eps)` `:644`. The plane-rotation/Arnoldi Hessenberg sequence backing `prev-carry`'s `H_prev` was confirmed at `:636-644` (`ApplyPlaneRotation`/`Hj[k]`/`s[j]`). Every frontmatter `depends-on` range encloses the field(s) its inline comment names, so each typed edge is anchored on confirmed L0 ground truth. The `cites-evidence` targets are raw L0 source-range paths (not book slugs) — the dofset/config-record precedent for L0 as rank-terminal leaves; correct. The proposed frontmatter YAML round-trips cleanly (`yaml.safe_load` OK; inline `#` comments after `kind:` values are valid YAML comments).

**Constructive-record backing — genuine.** For the 3 constructive records (`step-outputs`, `prev-carry`, `solve-result`) with no single named C++ struct, the per-field `cites-evidence` ranges are real positive backing sites: the inline residual readout (`:393-397`), the GMRES LS-residual readout (`:640-644`), the `CheckDot` breakdown guard (`:21-31`), and the persistent `mutable final_res` statistic (`hpp:26-115`). Each is rank-terminal L0. The report's own §Open-questions caveat 3 correctly flags these as legitimate struct-granularity exceptions for any future linter.

**±1 prose-drift OQ — confirmed real but non-load-bearing.** The report flags (and does NOT edit) that `op-params.md`/`sim-state.md` PROSE cites a few `iterative.hpp` line numbers ±1 off the exact declaration (prose `:42`/`:45`/`:49-50`/`:53-55` vs. on-disk exact `:41`/`:44`/`:48-49`/`:52-54`). This is accurate: the exact lines are `:41`/`:44`/`:48-49`/`:52-54` as I read them. The typed `cites-evidence` edges this dispatch emits anchor on the enclosing region `iterative.hpp:26-115`, which DOES contain all those declarations, so the edge typing is sound regardless of the prose ±1. Routing it to a future citation-audit pass (rather than an out-of-scope body edit) is the right call. This is correctly an OQ, not a critique-fail — the typed edges (the artifact this dispatch produces) are correct.

**surface-or-evidence / record-definition — pass.** All 6 are genuine record-definition pages that define a DATA SHAPE (fields/types/meaning/stratum/L0 home), not behaviour. Each is the cross-cutting (≥2-consumer) definition home: `krylov` (4 consumers), `op-params` (3), `sim-state` (4), and the 3 constructive records each carry ≥2 `reference` consumers in prose + frontmatter (`step-outputs` → krylov-step + 6; `prev-carry` → first-iteration-unrolling + 5; `solve-result` → solve-monad + 6). The record-definition obligation is met by each page's own `## Status` prose. This is a pure-typing dispatch (frontmatter prepend), not a surface change to the record bodies — no rotation_claim is needed.

**rotation-quality — pass (not applicable).** This dispatch asserts no algebraic/structural rotation; it types existing record-definition pages as DAG nodes. No-op.

**variant-axis-coverage — pass (not applicable).** No variant axes are introduced by edge-typing. The CG/GMRES/FGMRES variant axis lives in the `krylov`/`op-params` record bodies (already authored, out of scope here) and is covered there (slice-specific schemas named).

**cross-reference-integrity — pass.** All reference/sibling targets resolve on disk: the 6 record pages, `dofset`/`config-record` (precedent), `solve-monad`, `convergence-test`, `state-stratification`, `variant-absorption`, `constructed-operators`, `constructed-operator-factory`, `first-iteration-unrolling`, `derived-view-hoisting`, and `L4/krylov-step` — all 16 + 1 confirmed present. No dangling edges. Each `[old]` anchor block matches its file's current opening lines exactly (verified lines 1-3 of all 6), and all 6 files begin directly with the H1 (no pre-existing frontmatter), so the prepend is a clean valid-YAML insertion.

**edge-label-fidelity / rank-invariant / reachability — pass.** The `depends-on` (blocking, `cites-evidence` → L0) vs `reference` (free, → consumers/siblings) split is correct and matches the c103 dofset/config-record precedent: a record blocks only on its L0 backing, never on its consumers or sibling records. Rank invariant is well-founded vacuously — every blocking edge targets a rank-terminal L0 source range, so `rank: firm` rests only on `firm`-equivalent ground truth. Records are reached as the `depends-on` targets of their consumer operator chapters (which reach the feature roots), so they are live, not garbage. `tools/graded-stack-lint` will see these as `firm record` nodes whose `depends-on` targets are L0 leaves — consistent.

**plan-kind-consistency — pass.** Declared `kind: record`, `rank: firm` matches content: 6 record-definition pages, each on-disk `## Status` reads `firm` (verified: krylov/op-params/sim-state/step-outputs/prev-carry/solve-result all read `firm`). The constructive records correctly stay `firm` ("the record *shape* is firm"; the open `BreakdownTag` enum is named as the only constructed sub-part and does not lower the shape rank). Correct kind for the dispatch.

**skill-uptake-survey — pass (telemetry).** The dispatch self-verified L0 anchors via codemap `read_range` (appropriate and load-bearing for the edge-anchoring claim). It does not mention running `tools/graded-stack-lint` over the new frontmatter, which would mechanically confirm the rank invariant + reachability post-prepend; that is an integration-time check and its absence here is not blocking (surfaced as telemetry only).

### Issues found

No blocking issues. All 8 checks pass; the report is internally consistent and every load-bearing citation re-verifies against source.

- (informational, already self-flagged) `record-concept-prose-citation-pm1-drift` OQ: the ±1 prose-citation drift in `op-params.md`/`sim-state.md` bodies is real (exact lines `:41`/`:44`/`:48-49`/`:52-54`) but does NOT affect this dispatch's typed edges (which anchor on the enclosing `iterative.hpp:26-115` region). Correctly routed to a future citation-audit pass rather than edited here. Not a defect in the deliverable.
- (informational, already self-flagged) constructive-record `depends-on` granularity (`step-outputs`/`prev-carry`/`solve-result` point `cites-evidence` at per-field source ranges, not a struct decl): verified genuine; legitimate by-design exception for these 3 reified L4 records.

---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T14:55:01Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T15:10:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "plane-rotation concept-page canonical-pointer repoint"

## Critique

### Checks run

**citation-validity — pass.** Every claim in the report carries a citation pointer and each one resolves in-range. I independently verified: the 3 stale-reference rows (`plane-rotation-stream.md:37`, `givens_generate.md:27`, `givens_apply.md:27`) all exist at the exact cited lines and the quoted `[old]` strings are byte-exact matches against the live files. The supporting-evidence pointers also check out: `plane_rotation_stream.md:5` is the canonical-declaration line (verbatim the OQ-source text quoted), `orthog.md:225-235` is the reduction-status stub block (§"Plane-rotation stream (reduced — see `plane_rotation_stream.md`)" with the canonical-entries list at 229-234), and `givens.md:36-58` carries the §"L2 usage shape" already pointing at `plane_rotation_stream.md` (the cited line-40 pointer is present). The adjacent-OQ caveat citations (`givens_generate.md:23`, `givens_apply.md:23` → `gmres.cpp`; `givens.md:33-34` → `iterative.cpp:73-108`/`:227-241`; `orthog.md:227` "likely stale" flag) all resolve.

**surface-or-evidence — pass.** This is not a refinement-shaped operator/theme proposal; it is a surgical cross-reference repoint on concept pages. The proposal modifies surface (3 concrete `[old]/[new]` edit blocks) and is grounded in the reduction that already landed in cycle-012 (the canonical-slice declaration + the `orthog.md` stub). No rotation_claim is asserted and none is needed. Not the rotation-evidence shape this check guards; the surface-modification side is satisfied directly.

**rotation-quality — pass (not applicable).** The report asserts no algebraic/structural/reduction rotation between L-layers; it is a pointer-hygiene maintenance task downstream of an already-completed corpus reduction. No rotation to grade.

**variant-axis-coverage — pass (not applicable).** No operator/theme with orthogonal variant axes is introduced. The repointed pages do mention the stream's invariance-to variants (preconditioned/flexible/restarted), but the report only swaps a link target and changes no variant semantics, so there is no hidden-branch surface.

**cross-reference-integrity — warning.** The headline 3-stale-reference claim is EXACTLY correct for the OQ's declared scope. I grepped `book/src/concepts/` for `spec/slices/orthog`: the matches are `givens_apply.md:27`, `givens_generate.md:27`, `plane-rotation-stream.md:37` (the 3 plane-rotation pointers to repoint), plus `gmres.md:23` and `sequential-obstruction.md:48` (both legitimately Gram-Schmidt/orthogonalization references that stay). The two "left alone" Gram-Schmidt references are correctly classified: `sequential-obstruction.md:44-48` is wholly about MGS sequential dependency and points at the orthog L3 Gram-Schmidt section, which genuinely remains; `givens.md:40` is already on the canonical slice. The repoint targets are confirmed to host the material: `plane_rotation_stream.md` carries the full L0/L1/L2/L3 plane-rotation-stream dissection (§Context, §L0 GMRES/FGMRES call sites lines 51/57, §L1, §L2, §L3) and declares itself canonical at line 5. The warning is NOT about the 3-count — it is one un-surveyed surface the report does not mention: `book/src/concepts/dependency-map.md:188` carries a mermaid graph edge `orthog --> plane-rotation-stream`. After the cycle-012 reduction (orthog.md no longer contains the plane-rotation stream), that node-edge is stale-in-spirit. It is out of the OQ's narrow "Used in"/"primary dissection" scope and is a graph-maintenance surface rather than a slice-pointer link, so it does not invalidate the report's count — but the report's "NOT stale / left alone" enumeration omits it entirely, leaving a reader to assume the concepts directory was exhaustively swept. Surfaced as an issue below.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried; this is a concept-page/slice cross-reference repoint, not a lowering edge.

**plan-kind-consistency — pass.** The content shape (a `layer-intro-author` dispatch touching `book/src/concepts/*.md` cross-reference pointers) matches the role's authority (concept pages are layer-intro-author surface) and the OQ it closes. No rough-in placeholders; the 3 edits are firm and surgical. The report correctly scopes out the adjacent `gmres.cpp`→`iterative.cpp` L0-citation reconciliation as a separate OQ requiring a different skill.

**skill-uptake-survey — warning.** The proposal's shape (exact citation line + range verification of 3 pointers, byte-exact `[old]` strings, confirming the repoint targets actually contain the referenced material) directly implies the `verify-citation-range` skill (per CLAUDE.md the current skill set, extended cycle-012 with an inherited-citation sub-case) and the `summary-md-surgical-insert` skill (surgical edit-block discipline). The report performs verify-citation-range-shaped work (it even names the skill at line 106 when deferring the *adjacent* OQ) but never references invoking it for its own 3 repointed pointers, and does not reference `summary-md-surgical-insert` for the edit-block form. Pure telemetry, non-blocking: the work appears to have been done correctly; the skill invocation is simply not surfaced.

### Issues found

1. **Un-surveyed stale graph edge in dependency-map.md — `book/src/concepts/dependency-map.md:188` (`orthog --> plane-rotation-stream`).** Severity: low. The report's "NOT stale (deliberately left alone)" enumeration (CYCLE.md §"Stale reference list", lines 37-46, and §"Supporting evidence" lines 90-93) presents itself as an exhaustive sweep of orthog references in `concepts/` but does not mention the mermaid graph edge at `dependency-map.md:188`. After the cycle-012 reduction, orthog.md no longer contains the plane-rotation stream, so this graph edge is arguably stale (the dependency it encodes — orthog depends-on/contains plane-rotation-stream — no longer holds). It is outside the OQ's narrow "Used in"/"primary dissection" scope and is a graph-maintenance surface rather than a canonical-anchor pointer, so it does not change the report's exact-3-count verdict. But the omission means the report's "everything else legitimately stays on orthog" framing is incomplete — a reader cannot tell whether the edge was considered-and-kept or missed. The repairer/integrator should decide whether to (a) note it as explicitly out-of-scope in the report's caveat list, or (b) fold the edge into a follow-up dependency-map-maintenance OQ. NOTE: also at dependency-map.md:165/248 there are `plane_rotation_stream --> givens` edges and at :186/187 `plane-rotation-stream --> givens_generate/_apply` — these are the *concept-graph* edges for the canonical node and are correct; only the `orthog --> plane-rotation-stream` edge at :188 is the questionable one.

2. **Skill-invocation telemetry not surfaced for the report's own verification — CYCLE.md §"Supporting evidence" / §"Stale reference list".** Severity: informational. The report does line+range citation verification and target-content confirmation on its 3 pointers (exactly `verify-citation-range`-shaped work) and uses surgical `[old]/[new]` edit blocks (`summary-md-surgical-insert`-shaped), but references `verify-citation-range` only when deferring the adjacent `plane-rotation-givens-l0-citation-range-reconcile` OQ (line 106), never for its own pointers, and never references `summary-md-surgical-insert`. Non-blocking; surfaces a telemetry gap, not a defect — the underlying verification is sound (independently confirmed).

## Repair

### Fixes attempted

- **Finding** (cross-reference-integrity, warning): The report's "NOT stale / left alone" enumeration omits a 4th orthog reference — the mermaid edge `orthog --> plane-rotation-stream` at `book/src/concepts/dependency-map.md:188`, which the critic flagged as stale-in-spirit after the cycle-012 reduction and asked the repairer/integrator to either (a) note as out-of-scope in the caveat list or (b) fold into a follow-up OQ.
  - **Decision**: repaired (surgical caveat addition; NOT a 4th repoint — see rationale).
  - **Action**: Added the edge to CYCLE.md §"Stale reference list" → "NOT stale (deliberately left alone)" with an explicit classification, and added a deferral entry to §"Open questions / caveats" routing it to a future dependency-map-maintenance pass (CYCLE.md §"Stale reference list" + §"Open questions / caveats").
  - **Why no 4th repoint**: On inspection (`dependency-map.md:120-264`), the `dependency-map.md` mermaid blocks are `graph BT` concept-node DAGs whose edges are bare node identifiers (`orthog`, `plane-rotation-stream`, `dot`, `axpy`), NOT `[text](../spec/slices/*.md)` markdown file pointers. The 3 repointed references are canonical-anchor *file links*; line 188 is a *concept-dependency arrow*. It is genuinely stale-in-spirit (orthog no longer contains the stream), but resolving it is a concept-graph modeling decision (delete the edge vs. re-source it, e.g. `gmres --> plane-rotation-stream`), not a mechanical pointer swap. That exceeds surgical repair authority, so it is surfaced + deferred rather than rewritten. The canonical node's own out-edges (`:165/:186/:187/:194/:248`) are already correct — confirmed.

- **Finding** (skill-uptake-survey, warning): Telemetry gap — the report performs `verify-citation-range`- and `summary-md-surgical-insert`-shaped work but does not name those skills for its own 3 pointers.
  - **Decision**: not-needed (telemetry only; non-blocking).
  - **Action**: Acknowledged. The critic independently confirmed the underlying verification is sound; this is a surfacing gap, not a defect, and authoring skill-telemetry prose into a verified report is not a mechanical repair. No edit.

### Unrepairable findings

None. The cross-reference-integrity finding was repaired by surgical caveat addition (the stale graph edge is correctly classified + deferred, not a mechanical file-pointer repoint). The skill-uptake-survey finding is telemetry-only and needs no action.

## Suggested resolution

`ready`. Notes for the integrator:
- The 3 firm `[old]/[new]` repoint blocks are byte-exact and independently citation-verified by the critic; apply as-is. Closes OQ `plane-rotation-concept-page-canonical-pointer-repoint`.
- The added caveat defers the stale concept-graph edge `dependency-map.md:188` (`orthog --> plane-rotation-stream`) to a future dependency-map-maintenance pass (`layer-intro-author` or `same-layer-cross-cutter`). Optionally promote that to an OQ at finalize if the integrator prefers a tracked ledger entry over the in-report caveat.
- The adjacent `gmres.cpp`→`iterative.cpp` L0-citation reconciliation remains the separate, already-named OQ `plane-rotation-givens-l0-citation-range-reconcile` (untouched).

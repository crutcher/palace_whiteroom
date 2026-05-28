---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T000000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T203500Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "Re-anchor l3-krylov-step-cg-md-citation-sweep"

## Critique

One-line per-check: citation-validity **warning** (re-anchors relocate the dangle one hop, not terminating it); surface-or-evidence **pass** (retroactive evidence backfill); rotation-quality **pass** (n/a, pure re-anchor); variant-axis-coverage **pass** (n/a); cross-reference-integrity **pass** (all `[new]` link paths + line targets resolve); edge-label-fidelity **pass**; plan-kind-consistency **pass**; skill-uptake-survey **warning** (no `verify-citation-range` invocation noted).

### Checks run

**citation-validity — warning.** All five dangling-pointer claims verified true: `cg.md` is a 165-line reduced stub (`wc -l` confirms), and every cited range (341-349, 341-362, 103-115, 172-188, 393-425, 208-220, 430-446) exceeds 165, so all genuinely dangle. The grep-confirmed pointer lines (108/129/188/196/204) match the OQ exactly. Re-anchor targets verified in-range: `L3-L2/krylov-step-body-identity.md:125` carries the verbatim Claim-2 quote with `cg.md:341-362` preserved as provenance; `concepts/sequential-obstruction.md` carries the obstruction definition (the report's sub-ranges def 1-16 / MGS 37-48 / Givens 83-112 are accurate); `arnoldi_step.md:194-213` is live (302-line slice; the reduction notice superseded only L0 source-line citations, and §"Combined L3 form"/MGS-obstruction lives at 191-217). The warning: Re-anchor 4 points the L3 pointer at `L4/krylov-step.md §Evidence lines 170-171`, but those exact L4 lines ARE themselves dangling `cg.md:172-188`/`:393-425` pointers, AND are explicitly labeled there "cited transitively via the L2 entry, **not re-anchored here**" (L4 line 176: "Palace's C++ source does not realise the L4 form"). So for the step-body family the re-anchor relocates the dangle one hop rather than terminating it; the terminal firm home is `L2/krylov-step.md:138`, not L4. Re-anchor 5 has the same shape: L4 carries no `cg_solve`-driver citation, so "the `cg_solve` driver in Form A" at L4 is weaker than stated — L2:146 is the real home. The report's own OQ caveat acknowledges this (content lives in L4/L2 vocabulary regardless of their citation hygiene), which is a defensible narrative-home position; hence warning, not fail.

**surface-or-evidence — pass.** Pure retroactive-evidence backfill (re-pointing dangling citations after cycle-009 corpus reduction); no operator/theme surface claim is changed and status stays `firm`. This is the allowed retroactive-evidence framing, not a bare rotation_claim.

**rotation-quality — pass.** Not applicable: no algebraic/structural rotation asserted. Pure citation re-anchor.

**variant-axis-coverage — pass.** Not applicable: no operator-body change; the six variant axes are untouched.

**cross-reference-integrity — pass.** The `[new]` edit strings use `../concepts/sequential-obstruction.md`, which resolves correctly from `book/src/L3/` (verified) and matches the entry's existing link convention (lines 24/93/137). All firm-home line targets resolve. NOTE: the Summary/discipline-notes *prose* writes `../../book/src/concepts/sequential-obstruction.md` (wrong-relative), but that is narrative mention in CYCLE.md, not in the applied `[new]` strings — the actual edits are correct.

**edge-label-fidelity — pass.** Family classification per pointer is correct and corroborated cross-entry: 108/129 → outer-loop sequential-obstruction (`cg.md:341-349` + `arnoldi_step.md:194-213`, matching the identical pairing at `L2/krylov-step.md:9`); 188 → body-identity Claim 2 (`cg.md:341-362` → `L3-L2/...:125`); 196/204 → step-bodies/`cg_solve` driver. No edge-label vs prose mismatch.

**plan-kind-consistency — pass.** Declared as a pure citation re-anchor (observation/lifter re-anchor shape); content matches — only citation pointers in §Iteration-rotation-marker / §Algebraic-laws / §Evidence prose are touched, status `firm` unchanged.

**skill-uptake-survey — warning.** The report's shape (dangling-citation sweep with inherited/lifted-evidence ranges) is exactly the `verify-citation-range` skill's extended "Audit-report / inherited-citation sub-case" (cycle-012). The report demonstrates the verification (grep + `wc -l` + range arithmetic) but does not reference invoking that skill. Telemetry only, non-blocking.

### Issues found

1. **`L3/krylov-step.md` §Evidence, Re-anchor 4 (line 196) — warning.** New target `L4/krylov-step.md §Evidence lines 170-171` is itself a dangling `cg.md:172-188`/`:393-425` citation explicitly self-described as "cited transitively via the L2 entry, not re-anchored here." The re-anchor relocates the dangle one hop instead of terminating it. The terminal firm home is `L2/krylov-step.md:138`. Consider making L2 the primary firm home and demoting the L4 reference to a transitive note.

2. **`L3/krylov-step.md` §Evidence, Re-anchor 5 (line 204) — warning.** The report names "the `cg_solve` driver in Form A" at `L4/krylov-step.md`, but the L4 entry carries no `cg_solve`-driver citation (and states Palace source does not realise the L4 form). `L2/krylov-step.md:146` is the actual firm home for the outer-driver consumer sites; the L4 half of the pointer overclaims.

3. **CYCLE.md Summary / Discipline-notes prose — informational.** Narrative mentions of the concept page use `../../book/src/concepts/sequential-obstruction.md` (wrong-relative); the applied `[new]` edit strings correctly use `../concepts/sequential-obstruction.md`. Prose-only; the artifact edits are unaffected.

4. **Deferred OQ (L4/L2 sibling sweeps) — correctly deferred.** The report flags that `L4/krylov-step.md` (8 `cg.md` refs) and `L2/krylov-step.md` (12 `cg.md` refs) carry the same dangling pointers and routes them to NEW OQs (`l4-krylov-step-cg-md-citation-sweep`, `l2-krylov-step-cg-md-citation-sweep`) rather than touching out-of-scope `book/`. This is the right scoping per the cycle-014 precedent. The dangling counts are confirmed by grep. Issues 1/2 are a direct consequence of these sibling sweeps not yet having run; closing those OQs would terminate the chain.

## Repair

### Fixes attempted

- **Finding (Issue 1 / citation-validity)**: Re-anchor 4 (`L3/krylov-step.md` §Evidence line 196) pointed the step-body family at `L4/krylov-step.md` §Evidence lines 170-171, which are THEMSELVES transitive-dangling `cg.md` pointers explicitly self-labeled "cited transitively via the L2 entry, not re-anchored here" — so the re-anchor relocated the dangle one hop rather than terminating it.
  - **Decision**: repaired
  - **Action**: Rewrote the Re-anchor 4 `[new]` string (`reports/<id>/CYCLE.md` §Proposed-changes Re-anchor 4) to make `book/src/L2/krylov-step.md:138` the **terminal firm home** (it carries all three step-body source ranges `cg.md:103-115`/`:172-188`/`:393-425`, verified by reading L2 line 138), and demoted the `L4/krylov-step.md` §Evidence reference to an explicit transitive restatement ("cites them transitively via the L2 entry; carries no terminal source range of its own"). Confirmed L2:138 content directly. Propagated the same correction into the §Summary (line 25), §Supporting-evidence (L2/L4 bullets), and §Open-questions caveat so the report is internally consistent.

- **Finding (Issue 2 / citation-validity)**: Re-anchor 5 (`L3/krylov-step.md` §Evidence line 204) overclaimed an L4 `cg_solve`-driver citation ("the `cg_solve` driver in Form A" at `L4/krylov-step.md`) that does NOT exist — the L4 entry carries no `cg_solve`-driver source citation and states "Palace's C++ source does not realise the L4 form."
  - **Decision**: repaired
  - **Action**: Rewrote the Re-anchor 5 `[new]` string (`reports/<id>/CYCLE.md` §Proposed-changes Re-anchor 5) to point the outer-driver consumer-site family at `book/src/L2/krylov-step.md:146` as the **terminal firm home** (verified by reading L2 line 146: it carries both `cg.md:208-220` and `:430-446` under §Evidence "Outer-driver consumer sites"), and removed the non-existent L4 `cg_solve`-driver citation, replacing it with an accurate parenthetical (L4 names the driver pattern via `concepts/solve-monad.md` and inherits evidence transitively through L2). Same propagation as above.

- **Finding (Issue 3 / cross-reference-integrity prose path)**: CYCLE.md narrative prose uses wrong-relative `../../book/src/concepts/...`; applied `[new]` edit strings use correct `../concepts/...`.
  - **Decision**: not-needed
  - **Rationale**: Critic confirmed (cross-reference-integrity **pass**) that the applied `[new]` edit strings for Re-anchors 1/2 use the correct `../concepts/sequential-obstruction.md`. The wrong-relative form appears ONLY in CYCLE.md narrative mentions (Summary / Discipline-notes), never inside an applied `[new]` string. My repairs did not touch the Re-anchor 1/2 `[new]` strings. Prose-only, non-load-bearing for the artifact edit — no fix required.

- **Finding (Issue 4 / deferred OQ sibling sweeps)**: L4/L2 carry the same dangling `cg.md` pointers; report routes them to NEW OQs.
  - **Decision**: not-needed
  - **Rationale**: Correctly deferred. Confirmed the L4/L2 sibling-sweep OQ slugs (`l4-/l2-krylov-step-cg-md-citation-sweep`) are NOT yet in `scaffolding/open-questions.md` — which is correct, as they are recommendations the integrator-per-report promotes from §Open-questions, not pre-filed. Re-anchoring L4/L2 would be an out-of-scope `book/` mutation for this L3 dispatch. This dispatch's own OQ `l3-krylov-step-cg-md-citation-sweep` IS present in the ledger.

- **Finding (skill-uptake-survey — warning)**: report demonstrates `verify-citation-range` verification but does not reference invoking the skill.
  - **Decision**: not-needed
  - **Rationale**: Critic marked it telemetry-only, non-blocking. No artifact/report content defect; nothing mechanical to fix.

### Unrepairable findings

None. Both warning-level defects (Issues 1 and 2) were mechanical citation re-targets: the critic identified the exact terminal firm homes (`L2/krylov-step.md:138` and `:146`), which I verified by direct read before re-pointing. No substantive authoring was required — the content claims and `firm` status are unchanged; only the citation target was corrected from a transitive-dangling intermediary (L4) to the terminal source-bearing home (L2).

## Suggested resolution

`ready`. Notes for the integrator:
- All 5 re-anchors now point at terminal firm homes: 108/129 → `concepts/sequential-obstruction.md` + live `arnoldi_step.md:194-213`; 188 → `L3-L2/krylov-step-body-identity.md:125`; 196 → `L2/krylov-step.md:138` (terminal; L4 noted transitive); 204 → `L2/krylov-step.md:146` (terminal; L4 `cg_solve` overclaim removed).
- The L2 target's own `cg.md` pointers still dangle, but that is the separately-routed `l2-krylov-step-cg-md-citation-sweep` follow-up — pointing at L2 as the narrative/terminal home is valid regardless of L2's internal citation hygiene (the source ranges genuinely live in the L2 §Evidence registry).
- When promoting §Open-questions: file the two recommended sibling-sweep OQs (`l4-krylov-step-cg-md-citation-sweep`, `l2-krylov-step-cg-md-citation-sweep`) and mark `l3-krylov-step-cg-md-citation-sweep` answered (answer-link this CYCLE.md), contingent on the 5 re-anchors landing in a clean `cargo make book`.

---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T20:24:00Z
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
repaired_at: 2026-05-29T20:41:00Z
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

# META: verification of "Localize/characterize `trsv` (triangular solve) at L1 — routing decision"

## Critique

### Checks run

**citation-validity — pass.** Ran `tools/citecheck/citecheck.py --scan` over the whole CYCLE.md: **47 ok, 0 failing** (bounds + path-hygiene clean). Then `--anchor`-confirmed all 5 self-declared load-bearing pinpoints — every one returned OK at the exact cited line: `amg.cpp:19` ('l1-symm. GS'), `ams.cpp:162` ('l1-SSOR'), `ams.cpp:173` ('HYPRE_AMSSetSmoothingOptions'), `blockprecond.hpp:25` ('forward solve'), `chebyshev.hpp:82` ('polynomial versus Gauss'). I additionally bounds-checked the b2/b3 anchors (`jacobi.hpp:15-19`, `chebyshev.hpp:23/86`, `distrelaxation.hpp:30`, `strumpack.hpp:21`, `superlu.hpp:22`, `mumps.hpp:21`, `blockprecond.hpp:16-29`) — all in-range. The `densematrix.hpp:24-36` API enumeration is exact: I read the file and confirmed the public surface is precisely `MatrixSqrt`(:24,:26), `MatrixPow`(:28,:30), `SingularValueMax`(:32), `SingularValueMin`(:34), `Mult`(:36) — no `LU`/`Cholesky`/`Solve`/`trsv`, exactly as claimed. Citation format is the canonical `path:line` / `path:lo-hi` plain-text form throughout.

**surface-or-evidence — pass.** This is the load-bearing check for this report, because the routing decision (obstruction-theme vs perpetually-BLOCKED) rests entirely on a **negative finding** ("Palace has no standalone `trsv`"). A negative result must demonstrate the search was exhaustive. The producer reports two codemap searches with explicit terms, and I **independently reproduced both** against `reference/palace/palace/`: (1) `grep -rniE 'trsv|trsm|TriSolve|TriangularSolve|SpTrSV'` → **zero hits**; (2) `grep -rniE 'class …(GaussSeidel|SOR|ILU|IncompleteLU|IC0|Cholesky)…Smoother'` → **zero hits**. I broadened the negative claim to catch a term-casing artifact: a case-insensitive `triangular` sweep returns exactly **8 mentions**, and I inspected every one — all are accounted for by the report's own characterization (`blockprecond.hpp:16,:53` + `modeeigensolver.cpp:448,:528` + `modeeigensolver.hpp:245` = the b4 block-triangular red herring; `romoperator.hpp:132,:203` = upper-triangular R from orthogonalization, same family as the `back_solve` disambiguation the report draws; `geodata.cpp:531` = mesh-face geometry, irrelevant). No standalone scalar/sparse `trsv` primitive is hiding among them. The negative-evidence standard is met: the search is exhaustive across the in-scope tree, the search terms are stated, and every residual `triangular` token is positively accounted-for rather than hand-waved. This is the rare report shape where "no surface change + no rotation_claim" is correct: it is a localization/routing dispatch, not a refinement-shaped proposal, so the surface-or-evidence gate evaluates the negative-evidence quality rather than a surface/rotation pairing — and that quality is strong.

**rotation-quality — pass (not applicable as a rotation claim).** This report asserts no algebraic/structural/reduction rotation; it is a localization characterization concluding the operator does not exist as a firm-L1 candidate. There is no L_{n+1}→L_n compaction claim to evaluate. Marked pass / not applicable to a localization-only report.

**variant-axis-coverage — pass.** The report's domain has natural variant axes (HYPRE relax-type flag values; CPU-vs-GPU smoother defaults; the three direct-solver backends; block-vs-scalar triangular structure) and the report covers each explicitly rather than hiding a branch: relax-type enum values are enumerated for both AMG (`amg.cpp:19`: 8/13/18/16) and AMS (`ams.cpp:162`: 2/4/1/16); the GPU default-flip is called out (`amg.cpp:24`, GS→l1-Jacobi); all three direct-solver wrappers are named (STRUMPACK/SuperLU/MUMPS, b3); and the block-vs-scalar distinction is the entire point of b4. No orthogonal combination is silently dropped.

**cross-reference-integrity — pass.** All cross-references resolve. `book/src/L1/back_solve.md` exists on disk (the firm c027 disambiguation target). `book/src/L3/index.md:7` resolves and carries the claimed text (`--anchor 'triangular solves'` → OK at line 7). The `eigsolve` `partial-obstruction` opaque-library precedent the routing leans on (`L3/index.md:31`, `:45`) is in-bounds and substantively matches (slepc/arpack opaque-loop ownership; no kernel/driver analog). The OQ `l3-vocabulary-inventory-gap` framing (`gemv`/`ksp_solve`/`eigsolve` done, `trsv` the last leaf) is consistent with the L3 index Working Notes (:42, :44-45). No `[link]` is dead; no slug is dangling. The firm-body-inside-fence build-readiness guard is not triggered — this report's "Proposed changes" section is explicitly `None`, so there is no `edit:`/`new:` fenced block making a firm claim to enclose.

**edge-label-fidelity — pass.** The report carries no formal L_{n+1}→L_n edge label on a proposed theme (the follow-on obstruction theme is only *recommended*, not authored). Where it references existing edges (the L3-side `:7` obstruction note; the `eigsolve` `partial-obstruction` precedent) the prose discusses the matching layer relationship. No mismatch. Not applicable to a localization-only report beyond this.

**plan-kind-consistency — pass.** Declared kind is harvester localization-only and the content matches exactly: "Proposed changes: None (localization-only dispatch)", no `book/` edits, no L1 entry authored, dispatch-phase write-guard respected. The routing recommendation in §(c) and §"Open questions" is correctly framed as a **proposal to the planner** ("route to a follow-on `abstractor` obstruction-theme dispatch", "Follow-on dispatch shape (for the planner)"), not an enactment — it does not itself create the obstruction theme or close the OQ, it recommends doing so. Content shape and declared kind agree.

**skill-uptake-survey — warning.** The report's shape implies two relevant skills that exist but go unreferenced. (i) `verify-citation-range` was extended cycle-024 with the mechanical `tools/citecheck/ --anchor`/`--scan` realization, and the report DOES use `citecheck.py --anchor` for self-verification (good uptake on the tool) but does not name the skill. (ii) More substantively, this is a localization dispatch whose entire deliverable is a **negative-evidence routing decision**, and there is no skill referenced for "establish-negative-finding-exhaustiveness" or a routing-decision procedure — there may not be one (see skill-candidate note below). Pure presence/telemetry check, non-blocking; flagged so the meta-phase sees the surfaced gap.

### Issues found

No fail-level or warning-level **content** issues. The report is unusually clean: every load-bearing citation anchor-verifies, the negative finding reproduces independently and is exhaustive, the variant axes are covered, and the plan-kind framing is correct. The items below are minor / telemetry only.

1. **`romoperator.hpp` upper-triangular R-matrix sites not explicitly named in the negative-finding enumeration (telemetry, not a defect).** `reports/.../CYCLE.md:30` and §(b) enumerate the triangular-solve appearances, but the upper-triangular R from ROM/GMRES orthogonalization (`romoperator.hpp:132`, `:203`) is only implicitly covered via the `back_solve` disambiguation in the §"Open questions" caveats. These are correctly NOT a `trsv` primitive (they are the small-dense Hessenberg-R family the `back_solve` leaf already owns), so the conclusion is unaffected — but a follow-on obstruction-theme author might benefit from these sites being named alongside b4 as a second "looks-triangular-but-is-not-a-`trsv`" red herring. Severity: trivial; the report's `back_solve` caveat already gestures at this. Where: `CYCLE.md` §(b4) / §"Open questions / caveats" `back_solve disambiguation` bullet.

2. **Skill-name citations absent (skill-uptake telemetry).** The report uses `citecheck.py --anchor` (the mechanical realization of `verify-citation-range`) but does not name the skill, and uses an ad-hoc exhaustive-negative-search procedure with no skill reference. Severity: informational; surfaces a possible skill-candidate (see below). Where: `CYCLE.md` §"Supporting evidence".

### Note appended to scaffolding/skill-candidates.md

I appended one skill candidate (`establish-negative-finding-exhaustiveness`) — the negative-localization-with-routing shape recurs (the unimplemented-stub / opaque-library obstruction pattern), and this report executed it well by hand (two stated searches + residual-token accounting); crystallizing the procedure would let future "does Palace expose X?" routing dispatches hit a consistent exhaustiveness bar.

## Repair

### Fixes attempted

The critic returned **7 pass + 1 warning**. The single warning is telemetry-only and non-blocking; there are no fail/warning **content** findings. No edit to `CYCLE.md` or any supporting doc was required — this is a localization-only dispatch with `Proposed changes: None`, so there is no artifact-bound content to surgically correct.

- **Finding**: citation-validity — pass (47 ok / 0 failing via `--scan`; all 5 load-bearing anchors `--anchor`-confirmed; `densematrix.hpp:24-36` API enumeration exact).
  - **Decision**: not-needed (passed).
- **Finding**: surface-or-evidence — pass (negative-finding exhaustiveness met; both zero-hit searches independently reproduced; 8 residual `triangular` tokens each positively accounted-for).
  - **Decision**: not-needed (passed).
- **Finding**: rotation-quality — pass / not-applicable (localization-only; no rotation claim).
  - **Decision**: not-needed (passed).
- **Finding**: variant-axis-coverage — pass (HYPRE relax-type enums, CPU↔GPU default-flip, three direct-solver backends, block-vs-scalar all covered).
  - **Decision**: not-needed (passed).
- **Finding**: cross-reference-integrity — pass (all `[link]`s resolve; `back_solve.md`, `L3/index.md:7/:31/:45` in-bounds and substantively matching).
  - **Decision**: not-needed (passed).
- **Finding**: edge-label-fidelity — pass / not-applicable (no formal edge label on a proposed theme; obstruction theme only recommended).
  - **Decision**: not-needed (passed).
- **Finding**: plan-kind-consistency — pass (declared harvester localization-only; content matches; routing framed as a planner proposal, not an enactment).
  - **Decision**: not-needed (passed).
- **Finding**: skill-uptake-survey — warning (telemetry only, explicitly non-blocking). The report uses `citecheck.py --anchor` (the mechanical realization of `verify-citation-range`) but does not name the skill, and the negative-finding-exhaustiveness procedure that is the report's deliverable has no skill yet.
  - **Decision**: not-needed (non-blocking telemetry; not a content defect). Naming a skill in-report or authoring a new skill is substantive/meta-phase territory, not mechanical repair. The critic already filed the candidate `establish-negative-finding-exhaustiveness` (status `proposed`) in `scaffolding/skill-candidates.md:315` — the standing channel for this gap — so the surfaced gap is already routed to the meta-phase. No edit warranted or in scope.

Issue #1 in the critique (the `romoperator.hpp` upper-triangular R-matrix sites not explicitly named in the negative-finding enumeration) is flagged by the critic as "telemetry, not a defect" and trivial — the report's `back_solve` caveat already gestures at it, and the conclusion is unaffected. Naming those additional red-herring sites would be substantive authoring of the negative-finding enumeration (a content decision for a follow-on obstruction-theme author), not a mechanical fix — left untouched.

### Unrepairable findings

None. No finding requires deferral to a follow-up agent; the lone warning is non-blocking telemetry already routed to the meta-phase via the existing skill-candidate.

## Suggested resolution

`overall_status: ready`. The integrator may record the localization outcome with no `book/` edits:

- **Routing recommendation** (CYCLE.md §(c)): `trsv` → **obstruction-theme target** (a follow-on `abstractor` L1>L0 obstruction theme, slug suggestion `triangular-solve-obstruction`, citing (b1)+(b3)+(b4) as negative anchors and connecting to `book/src/L3/index.md:7`). This is a **planner proposal**, not an enactment — the integrator records it; the planner migrates it into the plan as a low-fan-out item (or accepts the existing `L3/index.md:7` line as already-sufficient documentation).
- **OQ-leaf resolution** (CYCLE.md §"Open questions"): the `trsv` leaf of OQ `l3-vocabulary-inventory-gap` closes as **resolved-by-obstruction** rather than left perpetually BLOCKED — the other three leaves (`gemv`/`ksp_solve`/`eigsolve`) are done; `trsv` terminates in an opaque-library obstruction, not a firm operator.

Note for the integrator: this report's negative-evidence quality is strong (both zero-hit searches independently reproduced by the critic; all 5 load-bearing anchors verified) — the localization conclusion is safe to record as-is.

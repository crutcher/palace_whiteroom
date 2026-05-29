---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T154500Z
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
repaired_at: 2026-05-29T155200Z
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

# META: verification of CYCLE concepts/eigsolve (the `book/src/concepts/eigsolve.md` cross-cutting concept page)

## Critique

### Checks run

**citation-validity — pass.** The page makes 13 concrete L0 claims, all carrying `(file:line)` citations. I ran `tools/citecheck/citecheck.py --scan` over the whole report (15 ok / 0 failing — bounds + path-hygiene clean) and then `--anchor` on every load-bearing pinpoint against `reference/palace/`. Every anchor resolved in-range with no drift:
- `eps.hpp:57-74` / `SetOperators` → anchors at 57,60,63,66,69,73 (the three overloads); meaning-read confirms each is `MFEM_ABORT("SetOperators not defined!")` by default — matches the "each `MFEM_ABORT` by default" claim.
- `eps.hpp:119` / `SetShiftInvert`; `eps.hpp:25-29` / `ScaleType`; `eps.hpp:31-42` / `WhichType` — all in-range with anchor present.
- `slepc.cpp:379-394` / `SetShiftInvert` (379) + `STSINVERT` (388); `arpack.cpp:191-194` / `opInv` (193); `slepc.cpp:364-367` / `opInv` (366); `arpack.cpp:579-581` / `opInv` (580); `slepc.cpp:1858` / `opInv` (1858) — all ok.
- `slepc.cpp:694` / `EPSSolve` — meaning-read confirms it is the single opaque `PalacePetscCall(EPSSolve(eps))` call (matches "the whole iteration is one opaque call").
- `arpack.cpp:318` / `naupd` — meaning-read confirms it sits inside `while (true)` under the `// Begin RCI loop.` comment (matches the "reverse-communication-interface (RCI) loop" framing).
- `nleps.cpp:351` / `QuasiNewtonSolver` — ok at exactly 351. NOTE the dispatch-question flag: a sibling report found a codemap +1 drift on `nleps.cpp`; citecheck/on-disk (authoritative) confirms NO drift on this report's cite — `QuasiNewtonSolver` is on line 351 as written.
- `slepc.cpp:711-716` / `gamma` (715) — meaning-read confirms `GetEigenvalue` returns `l * gamma` (the un-transform to original-problem coordinates; matches the coordinate-convention claim).
- `eigensolver.cpp:367` / `Solve` — ok (the `int num_conv = eigen->Solve()` partial-convergence anchor).

**surface-or-evidence — pass (largely no-op).** Not applicable to a concept page in the refinement sense. The page is a navigational/conceptual home that forwards to the authoritative L_n entries and explicitly disclaims restating algebraic laws ("if this page and any L_n entry disagree on a factual claim, the L_n entry wins"). It proposes no surface change to an existing operator/theme and makes no rotation_claim. It is new navigational scaffolding, not a refinement of existing operator text, so the surface-OR-evidence gate is satisfied vacuously.

**rotation-quality — pass (no-op).** The page asserts no algebraic/structural/reduction rotation of its own. It *describes* the L2/L3 shift-invert composition and the L3 partial-obstruction, but those rotations live in (and are owned by) the L2/L3 entries; the concept page only narrates and cross-links them. Nothing to evaluate for compaction here. Not applicable to a concept page.

**variant-axis-coverage — pass.** The eigsolve cohort has a real variant axis (problem-type: linear / quadratic / nonlinear; backend: ARPACK / SLEPc-EPS / SLEPc-PEP / SLEPc-NEP / direct-Newton). The page addresses each: the problem-type tag is named on the `EigSolver[problem]` phantom; the four backends are enumerated in the opaque-library-ownership section and the coordinate-convention caveat; the NEP-interior cohort (the nonlinear body) is linked out as its own cluster. No hidden branch. As a concept page it scopes operator-level axis exhaustiveness OUT to the L_n entries (correctly — that is where the variant axes are formally enumerated). Coverage is adequate for the navigational role.

**cross-reference-integrity — pass (LOAD-BEARING; spot-checked exhaustively).** I confirmed every cross-link target exists on disk. Chain + L0: `L1/eigsolve.md`, `L2/eigsolve.md`, `L3/eigsolve.md`, `L0/eigensolver-wrapper.md` — all EXIST. NEP-interior cohort: `L1/{apply_nonlinear_pencil, nleps_jacobian_action, nleps_eigenvalue_correction, nleps_deflated_residual, nleps_deflated_solve}.md` — all EXIST. L1>L0 themes: `L1-L0/{eigsolve-mutation-rotation, eigsolve-convergence-reason-mapping}.md` — both EXIST. L3 contrast refs: `L3/{krylov-step, ksp_solve, chebyshev}.md` — all EXIST. Concepts siblings: `apply_linop, ksp_solve, solver-as-operator, sequential-obstruction, constructed-operators, variant-absorption, solve-monad, dot` — all EXIST. Relative depths are correct for a page at `book/src/concepts/`: `../L1/`, `../L2/`, `../L3/`, `../L0/`, `../L1-L0/` for layer entries; `./` for concept siblings. The report's on-disk-confirmation claim (CYCLE.md §Supporting evidence) is accurate — no `linkcheck2` missing-target risk. **Wiring verified:** `SUMMARY.md` insertion anchor (`nested-constructed-operator-gate` at line 185, the current last concepts row) matches on-disk; the concepts block there is append-ordered (not alphabetical), so appending after 185 follows precedent. `concepts/index.md` insertion anchor (`[dot]` at 76, `[elementwise-product]` at 77) is exactly contiguous on-disk, and that table IS alphabetical, so the between-rows insertion of `eigsolve` is correctly placed. No existing `eigsolve` row in either file (no duplicate). The build-readiness fence guard (below) is also a cross-reference-integrity precondition and passes.

**edge-label-fidelity — pass (no-op).** No L_{n+1}→L_n edge label is carried by this concept page (it is a `concepts/` page, not a lowering theme). Where it references edges (L2/L3 composition, L3>... obstruction) the prose matches the layer it names. Not applicable in the edge-label sense.

**plan-kind-consistency — pass.** Declared shape is a cross-cutting concept page (navigational/conceptual home), and the content matches: forward-to-L_n-entry framing, opaque-type introduction, composition-seam narration, obstruction narration, cohort cross-links, "L_n entry wins" disclaimer — no algebraic-law restatement, no operator-entry apparatus (no `## Status`/Signature/Algebraic-laws block), consistent with the `dot.md` / `ksp_solve.md` concept-page precedent it cites. Index `Kind` classified `layer-pattern` (matching `ksp_solve` / `solve-monad` / `solver-as-operator`), which is a defensible judgment the report itself flags as a one-token change if a reviewer prefers `algorithm`. Classification is internally consistent.

**skill-uptake-survey — pass (telemetry).** The report surfaces relevant skill invocations: `citecheck.py --anchor` for citation self-verification (§Supporting evidence), the nested-fence guard (`convert-nested-fences-to-indented-code-in-proposed-changes-block`) for the four-backtick outer fence, `summary-md-surgical-insert` for the SUMMARY wiring, and it flags `upgrade-plain-text-ref-to-live-link-when-target-on-disk` as a follow-up for the three chain entries' stale "concepts/eigsolve does not yet exist" prose. Good uptake for a concept-page dispatch.

### Build-readiness (fence-parity) sub-finding

The report uses a four-backtick outer fence on the concept-page proposed-changes block because the body contains a three-backtick `text` fence (the `apply_shift_invert` pseudocode). Fence enumeration via `grep -nE '^\`{3,}'`:
- four-backtick: line 29 (open `` ````edit:book/src/concepts/eigsolve.md ``) → line 233 (close `` ```` ``) = 1 balanced pair.
- three-backtick: 110/115 (`text` pseudocode, NESTED inside the four-backtick block — even parity), 237/243 (SUMMARY edit), 247/255 (index edit) = 3 balanced pairs.
Total even parity, nested fence balanced. I confirmed the FULL concept-page body (through `## See also`, ending line 232) sits INSIDE the four-backtick fence (close at 233); no body content leaks outside the fence. The cycle-019 firm-body-outside-fence defect signature does NOT apply (this is not a firm operator entry, and the body is enclosed regardless). Build-readiness passes.

### Issues found

No blocking issues. Two low-severity observations for the repairer's consideration (neither blocks integration; neither is a linkcheck2 failure):

1. **Cosmetic — awkward inline-code/link construction at the proposed body line 152** (CYCLE.md §"Opaque-library ownership", the rendered concept page). The text is:
   `` `(`[`krylov-step`](../L3/krylov-step.md)`, `[`ksp_solve`](../L3/ksp_solve.md)`)` ``
   The intent is a tuple `(krylov-step, ksp_solve)` with both slugs as links wrapped in inline-code-styled parens. The two link targets resolve (both `L3/krylov-step.md` and `L3/ksp_solve.md` exist), so cross-reference-integrity is unaffected. However the stray ``` `(` ```, ``` `, ` ```, ``` `)` ``` inline-code fragments around the links may render as literal backtick-paren artifacts in mdBook rather than the intended styled tuple. Severity: low (cosmetic rendering, in-spec links). Candidate for a repairer simplification to plain `(krylov-step, ksp_solve)` prose with the two links, dropping the inline-code parens.

2. **Forward-reference hygiene — non-blocking, already flagged by the report.** The three chain entries (L1 §Context, L2 §Dependencies, L3 §Context) still carry prose saying `concepts/eigsolve` "does not yet exist". Once this page lands those become stale-but-harmless plain-text mentions (they say "a future concept page would carry the narrative"). The report correctly scopes editing them OUT (one-page-per-invocation discipline; does not touch L_n operator entries) and flags the opportunistic live-link upgrade for the planner via `upgrade-plain-text-ref-to-live-link-when-target-on-disk`. Recorded here so the integrator/planner has it in view; not a defect in THIS report.

Both the index `Kind=layer-pattern` classification and the SUMMARY append-position are sound (verified against on-disk ordering precedent) — the report's own self-flag on the `Kind` judgment is a courtesy, not an issue.

## Repair

All 8 critic checks graded `pass`; no check-level finding required repair, so every `repairs:` entry is `not-needed`. The critic left two low-severity, non-blocking observations under §Issues found; both are handled below. The frontmatter `verifies:` field was already `../CYCLE.md` (no stale `../REPORT.md` reference to fix).

### Fixes attempted

- **Finding**: Cosmetic — awkward inline-code/link tuple construction at proposed-body line 152 (the `(`krylov-step`, `ksp_solve`)` pair in §"Opaque-library ownership"). Stray `` `(` ``, `` `, ` ``, `` `)` `` inline-code fragments around the two links may render as literal backtick-paren artifacts in mdBook.
  - **Decision**: repaired
  - **Action**: Edited `reports/<id>/CYCLE.md` §"Opaque-library ownership — why L3 is a partial-obstruction" (proposed concept-page body). Replaced the inline-code paren/comma fragments with plain-prose parens and comma, keeping both slug links inline-code-styled: now reads `([krylov-step](../L3/krylov-step.md), [ksp_solve](../L3/ksp_solve.md)) pair`. The rendered tuple `(krylov-step, ksp_solve)` is preserved with both links intact; the literal-artifact render risk is removed. Mechanical cosmetic simplification — meaning unchanged, link targets unchanged (cross-reference-integrity unaffected; both targets exist on-disk per critic). The simplification was obvious and non-meaning-changing, so it cleared the "apply it / else leave it" bar the dispatch set.

- **Finding**: Forward-reference hygiene — the three chain entries (L1 §Context, L2 §Dependencies, L3 §Context) still carry prose saying `concepts/eigsolve` "does not yet exist"; now stale-but-harmless once this page lands.
  - **Decision**: not-needed (for THIS report) — routed to planner as a follow-up, NOT edited here.
  - **Rationale**: Not a defect in this report (the report correctly scopes editing the L_n operator entries OUT under one-page-per-invocation discipline, and itself flags the opportunistic live-link upgrade). Editing the three chain entries is out of repair authority on two counts: (i) it would modify the artifact (`book/src/L{1,2,3}/eigsolve.md`), which the repairer does not touch; (ii) it is the separate `upgrade-plain-text-ref-to-live-link-when-target-on-disk` follow-up the dispatch explicitly told me not to perform. Recorded for the planner below.

### Unrepairable findings

None. (The forward-reference-hygiene observation is a planner follow-up on OTHER entries, not an unrepairable defect in this report — see §Suggested resolution.)

## Suggested resolution

`overall_status: ready`. All 8 checks pass; the one cosmetic finding is repaired in place; no unrepairable findings; `follow_up_agent: null`.

Notes for the integrator/planner:
- **Integrator**: the report is clean and ready to apply as-is. The repaired cosmetic edit only touched the proposed concept-page body inside the four-backtick fence (the `(krylov-step, ksp_solve)` tuple); the fence-parity / build-readiness sub-finding the critic verified is unaffected (no fence lines changed). The SUMMARY append-anchor and concepts/index alphabetical insertion remain as the critic verified them.
- **Planner**: once `book/src/concepts/eigsolve.md` lands, the three chain entries' stale "`concepts/eigsolve` does not yet exist" prose (L1 §Context, L2 §Dependencies, L3 §Context) becomes an opportunistic live-link-upgrade candidate per skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`. This is a separate follow-up dispatch (a lifter/harvester pass on any of the three L_n entries) — out of this concept-page report's scope. The report's §Open questions already flags it; surfacing here so it reaches the plan.

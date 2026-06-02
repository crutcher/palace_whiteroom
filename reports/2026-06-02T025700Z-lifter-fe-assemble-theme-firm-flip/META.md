---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T034500Z
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
repaired_at: 2026-06-02T035500Z
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

# META: verification of D2 lifter firm-flip — fe-operator-assemble-mutation-rotation

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck --scan` on the on-disk theme (15 ok, 0 failing,
bounds-clean) and verified every load-bearing pinpoint via codemap `read_range`. The 3 declared
drift fixes are all correct against source:
- `ProjectBdrCoefficient` is at `laplaceoperator.cpp:238` (report fix `:236`→`:238` ✓).
- `EliminateRHS` is at `:252` (report fix `:253`→`:252` ✓).
- `GetExcitationVector` body runs `:225-252`; `:253` is the closing `}` (range fix `:225-253`→`:225-252` ✓).
- `ParallelProject` newly anchored at `:247` ✓.

The load-bearing rotation citations all hold: `op->AddSubOperator` domain branch at
`bilinearform.cpp:77` ✓, boundary branch at `:97` ✓, `op->Finalize()` at `:104` ✓;
`SetEssentialTrueDofs(...DIAG_ONE)` at `laplaceoperator.cpp:217` (range `:216-217` ✓);
`ParOperator::EliminateRHS` body opens at `rap.cpp:56` (range `:56-82` ✓). The drift fixes match
exactly what the firm `eliminate_rhs` sibling carries (`eliminate_rhs.md:37-39,256-259`:
`:225-252`/`:238`/`:247`/`:252`), corroborating the L0-evidence-driven prose-correction allowance.
No `verified_against:` YAML block present in this report, so that sub-check is n/a.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (status flip on an existing
theme + leg re-anchors). It modifies surface (the theme's `## Status`, banner, leg prose, vocabulary
section, index cell) AND is backed by the L0 rotation evidence (the integrator-fold + BC-elimination
legs, all re-verified above). Not a pure rotation_claim; the surface changes carry their evidence.

**rotation-quality — pass.** The underlying rotation (L1 `fe_assemble` fold `K = Σ_i A(term_i)` +
separable BC-elimination post-compositions ↦ Palace's imperative build-up-then-assemble protocol) is
a genuine vocabulary shift: the L1 form is a pure fold over an immutable term list with no
accumulator/finalize, whereas L0 is a mutable `BilinearForm` container with `AddSubOperator`
accumulation + `Finalize`. State-hiding + threaded-mutation compression — not a 1:1 rename. This
report does not author the rotation (it was authored c053 and re-anchored c055); it flips status,
so rotation-quality is inherited and intact.

**variant-axis-coverage — pass.** The PA/FA variant axis is explicitly handled (theme §Applicability:
"PA/FA is a variant axis, absorbed at L1" — representation-agnostic operator action; the
`pa_order_threshold` dispatch is a perf selector). The single-rank reading of `Par*` types is
explicitly scoped per CLAUDE.md. The BC-elimination separability axis (essential-bc pin vs RHS lift)
is covered as two separable post-compositions, each re-anchored to its firm operator. No hidden
branches.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: `../L1/fe_assemble.md`,
`../L1/eliminate_essential_bc.md`, `../L1/eliminate_rhs.md`,
`./fe-assemble-libceed-boundary-obstruction.md` all exist. Build-readiness fence guard: the report
is a `status: firm` flip, but it is NOT the cycle-019 fence-truncation shape — the firm apparatus
(Status, signature, laws, evidence) already lives in the on-disk theme body and is not being
re-authored; the `edit:` blocks are surgical replacements that fully enclose their `[old]`/`[new]`
payloads inside the fence (verified: 18 fences = 9 balanced `edit:`-block pairs). Every `[old]`
block matches on-disk content verbatim (theme lines 1-7, 12-17, 19-31, 52-63, 99-104, 137-148,
160-161, 208-215; index.md line 32). The firm-flip clean-gate is sound (see Issues for the one
note): all 3 LHS operators are `firmness: firm` with `## Status: firm. PROMOTE — clean.` on disk
(`fe_assemble` c054, `eliminate_essential_bc` c055, `eliminate_rhs` c055); the libCEED leaf is
`obstruction (opaque-library-ownership)` on disk and its own §Status states `fe_assemble` stays
firm — the opaque leaf sits below the fold and does not gate firmness (the `ksp_solve`/inner-Krylov
precedent applies cleanly). `weak_form_term` is correctly carried as a deferred rough-in *input* the
fold quantifies over opaquely, not a firmness gate. The PROMOTE-clean call is correct.

**edge-label-fidelity — pass.** The theme is an L1>L0 edge; all prose narrates the L1→L0 rewrite
(LHS = L1 fold + post-compositions, RHS = L0 build-then-assemble protocol). No edge-label/prose
mismatch. High→low layer-definition discipline preserved (no reverse-direction L0-lifts-to-L1 notes
added).

**plan-kind-consistency — pass.** Declared kind is a firm-flip (lifter re-anchor). Content shape
matches: no rough-in placeholders survive in the `[new]` blocks (the two BC legs are re-anchored to
firm live links; the `## Speculative L1 operators` section is replaced with a "Vocabulary status (all
LHS promoted)" note). The single remaining deferred item (`weak_form_term`) is explicitly framed as
an input, not a firm claim. No mis-classification.

**skill-uptake-survey — warning.** The report's shape implies two relevant skills.
`verify-citation-range` (its mechanical `citecheck --anchor`/`--scan` realization) IS referenced and
invoked (Discipline notes log the `--anchor` outputs for the 3 drift fixes + the full-file `--scan`).
However, the index-cell anti-drift flip (Change 9) plus the firm-flip is exactly the territory the
`proposed-changes-fence-encloses-full-body-guard` build-readiness discipline covers; the report
applies the cycle-056 D2 index-cell guard *by name* but does not reference any skill invocation for
the fence/body-enclosure check. Pure-presence telemetry, non-blocking.

### Issues found

1. **(low / informational) The clean-gate's gate-(a) on-disk re-verification is the critic's, not
   asserted by the report with disk cititations.** The report asserts all 3 LHS operators are firm
   (c054/c055) but cites them by cycle-tag, not by on-disk `## Status` line. I verified on disk: all
   three carry `firmness: firm` frontmatter AND `## Status: firm. PROMOTE — clean.` body
   (`fe_assemble.md:195`, `eliminate_essential_bc.md:212`, `eliminate_rhs.md:204`). The call is
   correct; this is a note that the gate evidence is the critic's confirmation, not a defect.

2. **(low) Stale parenthetical inside the firmed `## Status` body — the dropped libCEED OQ framing.**
   `book/src/L1-L0/...md` §Justification-kind (theme line 128-129, NOT touched by any of the 9
   changes) still reads "The libCEED boundary is the one non-structural seam; it is logged as OQ —
   see §'libCEED boundary'." Change 6 re-anchors the §"libCEED boundary" section to the *settled*
   obstruction (no longer an open OQ), but the §Justification-kind back-reference to it as "logged as
   OQ" is now mildly stale (the boundary is settled-as-(b), not open). Location: theme §Justification
   kind, line 128-129. Severity low — it is a cross-reference to a now-resolved item, not a wrong
   citation; the repairer may wish to soften "logged as OQ" → "documented as
   opaque-library-ownership obstruction" for consistency with the firm framing. Does not block the
   flip.

3. **(informational) `eliminate_essential_bc` and `eliminate_rhs` both declare
   `lowers_to: L1-L0/fe-operator-assemble-mutation-rotation` — but `eliminate_rhs` ALSO declares
   `lowers_to: L1-L0/eliminate-rhs-mutation-rotation` (a not-yet-authored sibling theme).** The
   report's Open-questions §3 correctly surfaces this (the firm operators' §Downward-to-L0 anticipate
   dedicated sibling themes; this theme currently folds both legs inline). No defect — the inline
   narration is fully cited and the split is flagged as an out-of-lifter-scope abstractor decision.
   Noted so the integrator/planner sees the forward-reference is already a real (if unwritten) slug
   in `eliminate_rhs` frontmatter, a candidate for stub-materialization if it recurs.

### Summary

The firm-flip is sound and the clean-gate call (PROMOTE — clean) is correct on all 3 gates,
re-verified against disk: (a) all 3 LHS operators firm; (b) rotation fully + correctly cited at L0
(all pinpoints re-confirmed via codemap, including the 3 drift fixes which match the firm
`eliminate_rhs` sibling exactly); (c) the libCEED leaf is a below-the-fold opaque-library-ownership
obstruction that does not gate firmness, and `weak_form_term` is a deferred input not a gate. The
index-cell anti-drift guard is applied consistently (theme `## Status` + frontmatter + index row all
flipped in one report; the `[old]` index block matches disk verbatim). Fence parity clean (9
balanced pairs), no leaked tool tags, no body re-authoring beyond the firm-flip + leg re-anchors.
The only issues are one low-severity stale §Justification-kind "logged as OQ" back-reference and two
informational notes. No fail-tier findings.

## Repair

### Fixes attempted

- **Finding (low)**: Stale §Justification-kind back-reference (theme lines 128-129, untouched by any
  of D2's 9 changes) still calls the libCEED boundary "logged as OQ — see §'libCEED boundary'", but
  D2's Change 6 settled that boundary as `obstruction (opaque-library-ownership)` (the c055 D5
  annotation). The back-reference is now stale relative to the firm framing.
  - **Decision**: repaired.
  - **Action**: Added **Change 10** to `CYCLE.md` (an `edit:` block on
    `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md` §Justification-kind). The `[old]`
    anchor is byte-exact against the on-disk theme lines 128-129 (verified: "matrix-materialization
    as the fold's action. (The libCEED boundary is the one non-structural seam; / it is logged as OQ
    — see §\"libCEED boundary\".)"). The `[new]` replaces "logged as OQ" with "settled as
    `obstruction (opaque-library-ownership)`" and adds a live link to
    `fe-assemble-libceed-boundary-obstruction.md`, consistent with Change 6's §"libCEED boundary"
    re-anchor. This is a bounded prose-correction within the firm-flip scope (the theme is being
    firm-flipped this cycle; its internal back-refs must be consistent) — mechanical, no content
    authored. Counts against `cross-reference-integrity` (a back-reference to a now-resolved item).

- **Finding (info)**: `eliminate_rhs` frontmatter declares a not-yet-authored
  `eliminate-rhs-mutation-rotation` sibling slug; already surfaced in D2's OQ §3 as a
  stub-materialization candidate if it recurs.
  - **Decision**: not-needed (no fix). Already correctly flagged for the planner/integrator in the
    report's Open-questions §3; an out-of-lifter-scope abstractor split decision, not a defect.

- **Finding (info / skill-uptake warning)**: `proposed-changes-fence-encloses-full-body-guard` not
  referenced by name despite the report applying the cycle-056 D2 index-cell guard.
  - **Decision**: not-needed. Pure-presence telemetry, non-blocking; `verify-citation-range` IS
    invoked by name. No mechanical repair applies.

### Unrepairable findings

None. The two informational findings need no fix; the one low-severity stale back-reference was
repaired mechanically.

## Suggested resolution

`ready`. Note for the integrator: D2's proposed-changes are the firm-flip (theme `status:`
frontmatter + `## Status` body + `L1-L0/index.md` dep-map row status cell, all flipped in one report
per the cycle-056 D2 index-cell guard) + the two BC-elimination leg re-anchors to firm operators +
the 3 bounded citation drift fixes (`:236`→`:238`, `:253`→`:252`, `:225-253`→`:225-252`, all matching
the firm `eliminate_rhs` sibling) + the newly-added Change 10 stale-back-ref fix. The theme
`fe-operator-assemble-mutation-rotation` goes **firm**. The `eliminate-rhs-mutation-rotation` sibling
slug (OQ §3) is a stub-materialization candidate the planner should track if it recurs — no action
this cycle.

---
agent: abstractor
invoked_at: 2026-05-28T213533Z
scope: L1>L0 theme sketch — eigsolve-convergence-reason-mapping (partly-constructive re-verification + cycle-016 audit-record append)
status: integrated
integrated_at: 2026-05-28T221238Z
integration_commit: b54ea1c
integration_notes: "Applied cycle-016 (per-report position 5). Append-only Re-verification (cycle-016 abstractor) subsection + verified_against YAML in eigsolve-convergence-reason-mapping.md; THIRD independent negative-anchor confirmation. Status correctly STAYS partly-constructive (zero materialization re-confirmed; no positive source site reads the reason code). OQ partly-constructive-entry-mechanism-validated-eigsolve-convergence-reason-mapping answered (ledger:2689). Retroactive-budget 0. Book build clean (exit 0)."
inputs:
  - book/src/L1-L0/eigsolve-convergence-reason-mapping.md (cycle-013 authored; cycle-014 audited+integrated, commit 73ecd3e)
  - book/src/L1-L0/eigsolve-mutation-rotation.md (parent theme; Sub-pattern B forwards the reason map here)
  - book/src/L1/eigsolve.md (EigStatus sum-type, 4 variants)
  - palace/linalg/slepc.cpp:687-709 (SlepcEPSSolverBase::Solve)
  - palace/linalg/slepc.cpp:1170-1191 (SlepcPEPSolverBase::Solve)
  - palace/linalg/slepc.cpp:1515-1545 (SlepcNEPSolverBase::Solve)
  - negative anchor: whole-tree search_text EPS_DIVERGED / EPS_CONVERGED / GetConvergedReason / DIVERGED / ConvergedReason / GetConverged
  - reports/2026-05-28T193309Z-lowering-verifier-eigsolve-convergence-reason-mapping-promotion/CYCLE.md (cycle-014 audit)
  - scaffolding/open-questions.md:2689 (carry-forward OQ partly-constructive-entry-mechanism-validated-eigsolve-convergence-reason-mapping)
---

# CYCLE: L1>L0 theme sketch — eigsolve-convergence-reason-mapping (partly-constructive re-verification)

## Summary

The L1>L0 sub-theme `eigsolve-convergence-reason-mapping` — the 8-row
`EPSConvergedReason -> EigStatus` mapping for the SLEPc backend
families — **already exists** on disk
(`book/src/L1-L0/eigsolve-convergence-reason-mapping.md`), was authored
cycle-013, and was audited + integrated in cycle-014 (commit `73ecd3e`,
verdict NEGATIVE-ANCHOR-CONFIRMED → STAYS-PARTLY-CONSTRUCTIVE). The
SUMMARY chapter entry (`book/src/SUMMARY.md:68`) and the L1-L0 dep-map
row (`book/src/L1-L0/index.md:23`) are likewise already present and
correct. This dispatch is therefore **not** a fresh authoring pass: it
is the **third independent confirmation** of the partly-constructive
negative anchor, closing the cycle-014 lowering-verifier carry-forward
OQ (`scaffolding/open-questions.md:2689`).

I independently re-verified, this cycle, via `mcp__palace-codemap__read_range`
and `search_text`:

1. **All three positive citations land exactly** — `EPSGetConverged@695`
   + `EPSConvergedReasonView@699` (print-only, inside `if (print > 0)`,
   fed to `PETSC_VIEWER_STDOUT_`) + `return (int)num_conv@708`
   (EPS); `PEPGetConverged@1178` + `PEPConvergedReasonView@1182` +
   `return (int)num_conv@1191` (PEP); `NEPGetConverged@1525` +
   `NEPConvergedReasonView@1529` (NEP, then eigenpair-ordering, no early
   return — the entry correctly asserts no NEP return-line citation).
2. **The whole-tree negative anchor still holds, zero materialization** —
   `EPS_DIVERGED` → 0 hits; `EPS_CONVERGED` → 0 hits; `GetConvergedReason`
   → 0 hits; `DIVERGED` → 0 hits (covers PEP/NEP enumerators too);
   `ConvergedReason` → exactly the three print-only `*ConvergedReasonView`
   sites `slepc.cpp:{699,1182,1529}`; `GetConverged` → count-readers only
   (`slepc.cpp:{695,1178,1525}` in the three `Solve()` bodies, plus
   `{276,310}` in spectral-estimation helpers — `276` EPS, `310` SVD —
   plus unrelated `ksp.cpp:301` / `iterative.hpp:98`), no
   `*GetConvergedReason` accessor anywhere.
3. **The L1 `EigStatus` sum-type still has exactly 4 variants**
   (`book/src/L1/eigsolve.md:51`), the mapping target is unchanged.

**Verdict: the status correctly STAYS `partly-constructive`.** No
positive Palace source site reads the reason code; the 8-row map remains
a faithful forward-looking reconstruction. This is the
partly-constructive **ENTRY** case behaving as designed: a transient
gate that correctly stays open because the promotion condition (Palace
reading the reason via `EPSGetConvergedReason` and propagating to status)
is genuinely unsatisfied. The single proposed change is an **append-only**
cycle-016 re-verification record to `## Verified-against` — recording the
third independent confirmation of the negative anchor (evidence that the
reconstruction stays faithful over time). I do NOT re-author content, do
NOT change the status, and do NOT touch SUMMARY / index (already present
and correct).

## Proposed changes

The theme file, SUMMARY chapter entry, and L1-L0 dep-map row already
exist (cycle-013/014). Only ONE append-only edit is proposed: a
cycle-016 re-verification YAML block at the end of `## Verified-against`,
following the channel-format convention the cycle-014 audit block uses
(real triple-backtick `yaml` fences in the actual file).

```edit:book/src/L1-L0/eigsolve-convergence-reason-mapping.md
[append under `## Verified-against` — specifically, immediately AFTER the
 closing ``` of the cycle-014 "### Lowering-verifier audit (cycle-014)"
 YAML block (the terminal content of `## Verified-against`, current
 line 310) and BEFORE the "## Status" heading (current line 312) — a new
 re-verification subsection:]

### Re-verification (cycle-016 abstractor)

Independent third confirmation of the negative anchor (the partly-constructive
mechanism's ENTRY case is strengthened by recurring confirmation that no
positive site has appeared). All three positive citations re-read exactly
this cycle via `mcp__palace-codemap__read_range`; all five whole-tree
negative-anchor searches re-run via `search_text`. Result: **status
correctly STAYS partly-constructive** — zero materialization, no positive
Palace source site reads the SLEPc reason code, the 8-row map remains a
faithful forward-looking reconstruction. Promotion remains gated on the
same upstream behaviour change as parent Sub-pattern B (a
`EPSGetConvergedReason` read feeding the outer-loop status); the gate is
unsatisfied, so the partly-constructive status is unchanged.

​```yaml
verified_against:
  - citation: palace/linalg/slepc.cpp:687-709
    verdict: supports
    audited_at: 2026-05-28T213533Z
    note: EPSGetConverged@695 (count), EPSConvergedReasonView@699 (print-only, inside if(print>0), PETSC_VIEWER_STDOUT_), return (int)num_conv@708 — re-read exact this cycle.
  - citation: palace/linalg/slepc.cpp:1170-1191
    verdict: supports
    audited_at: 2026-05-28T213533Z
    note: PEPGetConverged@1178, PEPConvergedReasonView@1182 (print-only), return (int)num_conv@1191 — isomorphic to EPS; re-read exact.
  - citation: palace/linalg/slepc.cpp:1515-1545
    verdict: supports
    audited_at: 2026-05-28T213533Z
    note: NEPGetConverged@1525, NEPConvergedReasonView@1529 (print-only), then eigenpair-ordering (no early return) — re-read exact; no NEP return-line over-claim.
  - citation: "whole-tree negative anchor (EPS_DIVERGED / EPS_CONVERGED / GetConvergedReason / DIVERGED)"
    verdict: supports
    audited_at: 2026-05-28T213533Z
    note: All four searches return zero hits this cycle (third independent confirmation). ConvergedReason returns only the 3 print-only Views {699,1182,1529}; GetConverged returns count-readers only — {695,1178,1525} in the three Solve() bodies, {276,310} in spectral-estimation helpers (276 EPS, 310 SVD) — plus ksp.cpp:301+iterative.hpp:98. Negative anchor RE-CONFIRMED — status STAYS partly-constructive.
  - citation: "SLEPc EPS/PEP/NEP ConvergedReason enums (documented; headers not vendored)"
    verdict: partially-supports
    audited_at: 2026-05-28T213533Z
    note: 8-row diverged count exhaustive over documented SLEPc enum; literature anchor (headers not vendored under reference/), unchanged from cycle-014 — does not weaken the source-confirmed Palace-side negative anchor.
​```
```

(The `​```yaml` fences above are zero-width-space-guarded to keep this
report's own fence parsing clean; the integrator emits **real**
triple-backtick `yaml` fences in the actual file, per the cycle-014
audit block's same convention.)

**No edit to `book/src/SUMMARY.md`** — chapter entry already present at
line 68.

**No edit to `book/src/L1-L0/index.md`** — dep-map row already present at
line 23 with the correct `partly-constructive` status annotation.

**No status change** — the `## Status` section's
`partly-constructive (structural decomposition firm; per-row status
assignment reconstructed)` verdict is correct and stays. The cycle-016
re-verification confirms the gate remains unsatisfied; it does not
promote.

## Partly-constructive sub-part (the 4-point statement)

Per the abstractor §Discipline partly-constructive checklist, the entry
states (already present; re-confirmed correct this cycle):

**(i) Which sub-part is constructive.** The **per-row `EigStatus`
assignment** for the **8 diverged-family rows** is the constructive
sub-part:
- 3 EPS diverged enumerators (`EPS_DIVERGED_ITS` → `MaxIterReached`/`PartialConverged`;
  `EPS_DIVERGED_BREAKDOWN` → `LinearSolveFailed`;
  `EPS_DIVERGED_SYMMETRY_LOST` → `LinearSolveFailed`),
- the `*_CONVERGED_ITERATING` (== 0) in-progress sentinel
  (unreachable post-solve; guard-only),
- 4 NEP-family diverged enumerators (`NEP_DIVERGED_LINEAR_SOLVE` →
  `LinearSolveFailed`; `NEP_DIVERGED_FUNCTION_COUNT` /
  `NEP_DIVERGED_SUBSPACE_EXHAUSTED` / `NEP_DIVERGED_ITS` →
  `MaxIterReached`).
- PEP is isomorphic to EPS (shares the 3 EPS diverged rows,
  **non-additively**).
The **2 converged rows** (`*_CONVERGED_TOL`, `*_CONVERGED_USER`) are
**count-anchored**, NOT constructive — they reuse parent Sub-pattern C's
positively-anchored `num_conv` vs `K_max` discrimination.

**(ii) Negative-anchor citations.** The whole-tree negative anchor,
re-confirmed this cycle: `search_text` for `EPS_DIVERGED` /
`EPS_CONVERGED` / `GetConvergedReason` / `DIVERGED` → all zero hits;
`ConvergedReason` → only the three print-only `*ConvergedReasonView`
sites `palace/linalg/slepc.cpp:{699,1182,1529}`; `GetConverged` →
count-readers only (`palace/linalg/slepc.cpp:{695,1178,1525}` in the
three `Solve()` bodies, plus `{276,310}` in spectral-estimation helpers
— `276` EPS, `310` SVD).
Palace materialises the reason (via the `*ConvergedReasonView` print
calls) but never binds it to a variable, never branches on it, never
returns it. The negative anchor is evidence FOR the reconstruction being
faithful; it does NOT license asserting Palace produces the
reason→status discrimination today.

**(iii) Promotion condition.** One global gate covers all 8 rows
uniformly: promotion to `firm` is contingent on the **same** upstream
behaviour change as parent Sub-pattern B — Palace reading the reason code
via `EPSGetConvergedReason` (currently absent: zero hits) and propagating
it into the outer-loop status derivation. This gate is strictly
**downstream** of the parent Sub-pattern B gate (the reason map only
materialises once the per-callsite inner-solve capture lands). A
`lowering-verifier` audit may UNBLOCK only if it discovers a positive
Palace source site that reads the reason — which the cycle-014 audit and
this cycle-016 re-verification both confirm does NOT exist. Until such a
site appears, the partly-constructive status correctly STAYS. (Note the
distinction from cycle-013's eigsolve EXIT: that promotion fired because
the cycle-012 audit identified mechanical firming edits to apply; here
there are NO firming edits to gate — no positive site — so the gate is
genuinely open.)

## Speculative operators proposed

**None.** This sub-theme refines the status-derivation of the existing
firm L1 form (`book/src/L1/eigsolve.md`); the `EigStatus` sum-type
already carries all four variants. No new vocabulary. (Consistent with
the parent `eigsolve-mutation-rotation`'s "no speculative operators"
verdict.)

## Supporting evidence

L0 evidence ranges (re-read this cycle via `mcp__palace-codemap__read_range`):
- `palace/linalg/slepc.cpp:687-709` — `SlepcEPSSolverBase::Solve`:
  `EPSGetConverged@695`, `EPSConvergedReasonView@699` (print-only),
  `return (int)num_conv@708`.
- `palace/linalg/slepc.cpp:1170-1191` — `SlepcPEPSolverBase::Solve`:
  `PEPGetConverged@1178`, `PEPConvergedReasonView@1182` (print-only),
  `return (int)num_conv@1191`.
- `palace/linalg/slepc.cpp:1515-1545` — `SlepcNEPSolverBase::Solve`:
  `NEPGetConverged@1525`, `NEPConvergedReasonView@1529` (print-only),
  then NEP eigenpair-ordering.

Negative anchor (whole-tree `search_text`, re-run this cycle):
- `EPS_DIVERGED` → 0 hits.
- `EPS_CONVERGED` → 0 hits.
- `GetConvergedReason` → 0 hits.
- `DIVERGED` → 0 hits.
- `ConvergedReason` → 3 hits, all print-only `*ConvergedReasonView`:
  `slepc.cpp:{699,1182,1529}`.
- `GetConverged` → count-readers only:
  `slepc.cpp:{695,1178,1525}` (the three `Solve()` bodies) +
  `slepc.cpp:{276,310}` (spectral-estimation helpers — `276` EPS,
  `310` SVD) + `ksp.cpp:301` + `iterative.hpp:98` (the unrelated
  iterative-solver flag).

L1 anchor:
- `book/src/L1/eigsolve.md:51` — `EigStatus = Converged | PartialConverged
  | MaxIterReached | LinearSolveFailed` (4 variants, unchanged).

Cross-references:
- `book/src/L1-L0/eigsolve-mutation-rotation.md:332-344` — parent theme
  Sub-pattern B forwards the full reason map to this sub-theme.
- `reports/2026-05-28T193309Z-lowering-verifier-eigsolve-convergence-reason-mapping-promotion/CYCLE.md`
  — cycle-014 audit (verdict STAYS-PARTLY-CONSTRUCTIVE; integrated
  commit `73ecd3e`).
- `scaffolding/open-questions.md:2689` — the carry-forward OQ
  (`partly-constructive-entry-mechanism-validated-...`) that this
  re-verification closes.

## Open questions / caveats

- **Carry-forward OQ closure.** This dispatch closes the cycle-014
  lowering-verifier carry-forward OQ
  `partly-constructive-entry-mechanism-validated-eigsolve-convergence-reason-mapping`
  (`scaffolding/open-questions.md:2689`): the ENTRY case (status correctly
  STAYS) is now independently re-confirmed a third time, complementing
  cycle-013's eigsolve EXIT case. The integrator-per-report should mark
  this OQ closed/answered.

- **The literature-anchor caveat is unchanged.** The 8-row enum
  exhaustiveness is checked against SLEPc's **documented** `EPS`/`PEP`/`NEP`
  convergence-reason enums (SLEPc/PETSc headers are NOT vendored under
  `reference/`), so it is a **literature anchor**, distinct from — and not
  weakening — the source-confirmed Palace-side negative anchor that
  underpins the partly-constructive status. Low risk (the enum is stable
  across SLEPc 3.x); would only under-cover if a future SLEPc version adds
  a new `*_DIVERGED_*` code. This is the one residual carry-forward and is
  already recorded in the entry's §Justification kind two-evidence-bases
  distinction. No action required this cycle.

- **No reverse-direction (lift) narration leaked into the formal entry.**
  Per the high→low layer-definition invariant, the entry's
  "Materialisation shape (forward-looking)" section describes a
  not-yet-in-Palace upstream change as the promotion-condition target, not
  as a reverse-direction lift; this re-verification did not alter that
  framing. Confirmed clean.

- **Scope-framing note (not a blocker).** The dispatch scope as written
  ("Author the ... sub-theme ... may be a new file") presumed the file
  might not yet exist; in fact cycle-013 authored it and cycle-014
  audited+integrated it. The correct cycle-016 action is therefore the
  re-verification + audit-record append above, not a re-author. Surfacing
  this so the integrator does not expect a new-file proposed-change.

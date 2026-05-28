---
agent: lowering-verifier
invoked_at: 2026-05-28T193309Z
scope: L1>L0 theme audit — eigsolve-convergence-reason-mapping (partly-constructive promotion gate)
status: integrated
integrated_at: 2026-05-29T003000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-014 position 5/8. Verdict NEGATIVE-ANCHOR-CONFIRMED → STAYS-PARTLY-CONSTRUCTIVE (NOT a promotion). Critic independently re-confirmed zero materialization (EPS_DIVERGED/EPS_CONVERGED/GetConvergedReason all empty; only print-only *ConvergedReasonView at slepc.cpp:699/1182/1529). Applied verified_against YAML + §Justification-kind two-evidence-bases distinction (source-confirmed negative anchor vs literature-anchored 8-row enum) + §Status audit-outcome note to L1-L0/eigsolve-convergence-reason-mapping.md; caveat correctly STAYS. Validates the partly-constructive ENTRY mechanism, complementing cycle-013 eigsolve EXIT. Applied per parent's explicit dispatch override of report META GATED flag. OQ partly-constructive-entry-mechanism-validated-eigsolve-convergence-reason-mapping (cycle-015 meta-phase). Build clean."
inputs:
  - book/src/L1-L0/eigsolve-convergence-reason-mapping.md
  - palace/linalg/slepc.cpp:687-709 (SlepcEPSSolverBase::Solve)
  - palace/linalg/slepc.cpp:1170-1191 (SlepcPEPSolverBase::Solve)
  - palace/linalg/slepc.cpp:1515-1545 (SlepcNEPSolverBase::Solve)
  - negative anchor: whole-tree search_text for EPS_DIVERGED / EPS_CONVERGED / GetConvergedReason / ConvergedReason / DIVERGED
---

# CYCLE: Audit eigsolve-convergence-reason-mapping (promotion gate)

## Summary
Audited the cycle-013 partly-constructive sub-theme `eigsolve-convergence-reason-mapping`
(the `EPSConvergedReason -> EigStatus` map: 2 count-anchored converged rows + 8
partly-constructive diverged-family rows; PEP isomorphic to EPS / non-additive,
NEP additive). The gate question is whether the partly-constructive status is correct
(negative anchor real → faithful forward-looking reconstruction) or whether a positive
materialisation site was missed. **Verdict: NEGATIVE-ANCHOR-CONFIRMED →
STAYS-PARTLY-CONSTRUCTIVE.** The whole-tree negative anchor is real and complete: Palace
PRINTS the reason (three `*ConvergedReasonView` views) and never reads it into a status
(zero `*GetConvergedReason` callsites, zero `EPS_*_DIVERGED/CONVERGED` enumerator
references). The map is therefore a faithful reconstruction with no positive site, exactly
as the entry asserts. The 8-row diverged count HELD as exhaustive — but checked against
SLEPc's DOCUMENTED enum (a literature anchor; SLEPc/PETSc headers are not vendored under
`reference/`), NOT a vendored positive source site. This enum-coverage half is therefore a
literature anchor, not a source anchor; the Palace-side negative anchor underpinning the
partly-constructive status is fully source-confirmed and is unaffected by this. This validates
the partly-constructive ENTRY mechanism (complements cycle-013's eigsolve EXIT) — **flag for
the cycle-015 meta-phase: ENTRY (status correctly STAYS) + EXIT (cycle-013, status promoted)
together demonstrate the partly-constructive gate is a working transient, not an escape hatch.**
No edits required; one verify-against tightening proposed (gated, not enacted).

## Per-citation audit

- **Citation**: `palace/linalg/slepc.cpp:687-709` — `SlepcEPSSolverBase::Solve`
  - **Theme claim**: count read via `EPSGetConverged` at 695; reason PRINT-ONLY via
    `EPSConvergedReasonView` at 699; only `num_conv` escapes via `return (int)num_conv` at 708.
  - **Found** (read_range 687-709 independently): `EPSGetConverged(eps, &num_conv)` at 695;
    `EPSConvergedReasonView(eps, PETSC_VIEWER_STDOUT_(...))` at 699, inside the `if (print > 0)`
    guard, fed straight to a stdout viewer; `RescaleEigenvectors(num_conv)` then
    `return (int)num_conv` at 708. The reason code is never bound to a C++ variable.
  - **Verdict**: supports
  - **Notes**: Lines land exactly. The reason view sits in a print guard and consumes `eps`,
    not a captured reason variable — the print-only characterisation is precise.

- **Citation**: `palace/linalg/slepc.cpp:1170-1191` — `SlepcPEPSolverBase::Solve`
  - **Theme claim**: `PEPGetConverged` at 1178; `PEPConvergedReasonView` at 1182 (print-only);
    `return (int)num_conv` at 1191.
  - **Found** (read_range 1170-1191): identical shape to EPS — `PEPGetConverged` 1178,
    print-guarded `PEPConvergedReasonView` 1182, `RescaleEigenvectors(num_conv)`, return at 1191.
  - **Verdict**: supports
  - **Notes**: Body is value-thread-isomorphic to the EPS body, supporting the entry's
    "same three columns apply to PEP" non-additivity claim.

- **Citation**: `palace/linalg/slepc.cpp:1515-1545` — `SlepcNEPSolverBase::Solve`
  - **Theme claim**: `NEPGetConverged` at 1525; `NEPConvergedReasonView` at 1529 (print-only).
  - **Found** (read_range 1515-1545): `NEPGetConverged(nep, &num_conv)` 1525, print-guarded
    `NEPConvergedReasonView` 1529; then NEP-specific post-processing (`perm`, `NEPGetEigenpair`
    loop). Reason again print-only.
  - **Verdict**: supports
  - **Notes**: The entry cites the NEP `Solve` body without a `return (int)num_conv` line (the
    NEP body diverges after 1529 into eigenpair ordering); the entry correctly does NOT assert a
    NEP return-line citation, so no over-claim. Accurate.

- **Citation** (negative anchor, whole-tree): `EPS_DIVERGED` / `EPS_CONVERGED` /
  `GetConvergedReason` / `DIVERGED` / `ConvergedReason` searches.
  - **Theme claim**: zero materialisation; only the three print-only `*ConvergedReasonView`
    sites; no `*GetConvergedReason` accessor anywhere.
  - **Found** (independent `search_text` this audit):
    - `EPS_DIVERGED` → `{"hits":[]}` (zero)
    - `EPS_CONVERGED` → `{"hits":[]}` (zero)
    - `GetConvergedReason` → `{"hits":[]}` (zero)
    - `DIVERGED` → `{"hits":[]}` (zero — covers PEP/NEP enumerators too)
    - `PEP_DIVERGED|NEP_DIVERGED|PEP_CONVERGED|NEP_CONVERGED` → `{"hits":[]}` (zero)
    - `ConvergedReason` → exactly three hits: `slepc.cpp:{699, 1182, 1529}`, all
      `*ConvergedReasonView` (print-only).
    - `GetConverged` → count-readers ONLY: `slepc.cpp:{276, 310, 695, 1178, 1525}`
      (EPS/SVD/EPS/PEP/NEP) + `ksp.cpp:301` + `iterative.hpp:98` (the iterative-solver
      `bool GetConverged()`, unrelated to SLEPc reason). No `GetConvergedReason` variant.
  - **Verdict**: supports (negative anchor fully confirmed)
  - **Notes**: This is the load-bearing fact. It is real and complete. The entry's
    `DIVERGED → zero hits` claim is even stronger than stated: it confirms the PEP/NEP
    diverged enumerators are equally absent, not just the EPS ones.

## Applicability conditions

- **Condition 1**: `E`'s bound backend is one of the three SLEPc families
  (`SlepcEPSSolverBase` / `SlepcPEPSolverBase` / `SlepcNEPSolverBase`); ARPACK /
  `QuasiNewtonSolver` excluded.
  - **Verifiable**: Yes — the three `Solve()` bodies are the cited SLEPc family sites; the
    `GetConverged` search shows ARPACK has no SLEPc-reason analogue (ARPACK is a separate file
    not in these hits). The SLEPc-family restriction is sound.
  - **Found counter-example?**: No.

- **Condition 2**: Reason-consumption requires an upstream behaviour change — Palace calls
  the print-only `*ConvergedReasonView`, not the variable-binding `*GetConvergedReason`.
  - **Verifiable**: Yes — directly confirmed by the negative anchor (`GetConvergedReason` →
    zero hits) and the positive print-only sites. This is precisely the partly-constructive gate.
  - **Found counter-example?**: No.

- **Condition 3**: Single-rank scope; reason code rank-replicated by SLEPc, no MPI reduction
  introduced.
  - **Verifiable**: Partially — the single-rank reading is a CLAUDE.md scope convention, not a
    source-readable fact; consistent with the `Par*`-as-single-rank rule. No counter-evidence.
  - **Found counter-example?**: N/A (scope convention, not a source claim).

## Algebraic laws (if cited)
N/A — this sub-theme cites no algebraic-law steps; the justification kind is
**structural** (enum partition + per-family isomorphism) with per-row status
**partly-constructive**. No law to discharge on operator signatures.

## Exhaustiveness of the 8-row count (the second gate question)

The entry claims the diverged-family rows are exhaustive over SLEPc's documented
`EPSConvergedReason` / `PEPConvergedReason` / `NEPConvergedReason` enums. SLEPc headers are
NOT vendored under `reference/` (only Palace's `slepc.cpp` names the views), so exhaustiveness
is checked against SLEPc's documented enum, not a vendored positive site (recorded as a caveat).

Against the documented SLEPc convergence-reason enums:
- **EPS**: `EPS_CONVERGED_TOL`, `EPS_CONVERGED_USER` (converged); `EPS_DIVERGED_ITS`,
  `EPS_DIVERGED_BREAKDOWN`, `EPS_DIVERGED_SYMMETRY_LOST` (diverged); `EPS_CONVERGED_ITERATING`
  (in-progress, 0). = 6 codes. Entry covers all 6. EXHAUSTIVE.
- **PEP**: isomorphic to EPS (`PEP_CONVERGED_TOL/USER`, `PEP_DIVERGED_ITS/BREAKDOWN/
  SYMMETRY_LOST`, `PEP_CONVERGED_ITERATING`). Entry treats PEP as non-additive (shares EPS's
  3 diverged rows). Correct.
- **NEP**: `NEP_CONVERGED_TOL/USER`, `NEP_CONVERGED_ITERATING`, plus the four additive
  diverged codes `NEP_DIVERGED_LINEAR_SOLVE`, `NEP_DIVERGED_FUNCTION_COUNT`,
  `NEP_DIVERGED_SUBSPACE_EXHAUSTED`, `NEP_DIVERGED_ITS`. Entry covers all four. EXHAUSTIVE.

Row tally as the entry states it: 2 count-anchored converged rows + **8 partly-constructive
rows** (3 EPS diverged + 1 `*_CONVERGED_ITERATING` sentinel + 4 NEP-family diverged). The
**8-row count HELD.** No SLEPc reason code that a Palace SLEPc solver could encounter is
omitted. (Caveat: verified against the documented enum, not a vendored header — see Open
questions.)

## Proposed changes

**Verdict on the gate: STAYS partly-constructive. The promotion is NOT unblocked.** The
negative anchor is real and complete; there is no missed positive site; the map is correctly
a forward-looking reconstruction. Promotion remains gated on the SAME upstream behaviour change
as parent Sub-pattern B (a `*GetConvergedReason` read feeding the status derivation) — which
has not landed. This is the expected-and-valuable outcome: it validates the partly-constructive
ENTRY mechanism.

No corrective edits are required — the entry is accurate as written. One OPTIONAL tightening is
proposed as GATED (route to a follow-up abstractor/lifter dispatch; do NOT enact here), to
record this audit in the `## Verified-against` section and make the enum-source caveat explicit:

```edit:book/src/L1-L0/eigsolve-convergence-reason-mapping.md
[append a fenced verified_against block at end of the ## Verified-against section]
~~~yaml
verified_against:
  - citation: palace/linalg/slepc.cpp:687-709
    verdict: supports
    audited_at: 2026-05-28T193309Z
    note: EPSGetConverged@695 (count), EPSConvergedReasonView@699 (print-only), return num_conv@708 — all exact.
  - citation: palace/linalg/slepc.cpp:1170-1191
    verdict: supports
    audited_at: 2026-05-28T193309Z
    note: PEPGetConverged@1178, PEPConvergedReasonView@1182 (print-only), return num_conv@1191 — isomorphic to EPS.
  - citation: palace/linalg/slepc.cpp:1515-1545
    verdict: supports
    audited_at: 2026-05-28T193309Z
    note: NEPGetConverged@1525, NEPConvergedReasonView@1529 (print-only); no return-line over-claim.
  - citation: "whole-tree negative anchor (EPS_DIVERGED/EPS_CONVERGED/GetConvergedReason/DIVERGED)"
    verdict: supports
    audited_at: 2026-05-28T193309Z
    note: All four searches return zero hits; ConvergedReason returns only the 3 print-only Views; GetConverged returns count-readers only. Negative anchor CONFIRMED — status STAYS partly-constructive.
  - citation: "SLEPc EPS/PEP/NEP ConvergedReason enums (documented; headers not vendored)"
    verdict: partially-supports
    audited_at: 2026-05-28T193309Z
    note: 8-row diverged count is exhaustive over the documented enum; exhaustiveness checked against SLEPc docs, NOT a vendored positive header site (caveat).
~~~
```

(The `~~~` fences above stand for triple-backtick `yaml` fences in the actual file, per the
role template's channel-format note. If the follow-up dispatch enacts this, emit real
triple-backtick fences.)

## Supporting evidence
- `palace/linalg/slepc.cpp:687-709, 1170-1191, 1515-1545` — read_range-confirmed this audit.
- `palace/linalg/slepc.cpp:{276,310,695,1178,1525}` + `ksp.cpp:301` + `iterative.hpp:98` —
  the complete `GetConverged` callsite set (count-readers only; no reason accessor).
- `book/src/L1/eigsolve.md` — the `EigStatus` sum-type the table maps onto (not re-read this
  audit; the entry's mapping target is internally consistent with the 4 variants it names).
- `book/src/L1-L0/eigsolve-mutation-rotation.md` — parent theme; Sub-pattern B forwards the
  reason map here (not re-read this audit; cross-reference accepted as inherited).

## Open questions / caveats
- **Enum exhaustiveness is verified against SLEPc's DOCUMENTED enum, not a vendored header.**
  SLEPc/PETSc headers are not under `reference/`. If a future SLEPc version adds a new
  `*_DIVERGED_*` code, the table would silently under-cover. Low risk (the enum is stable across
  SLEPc 3.x), but the exhaustiveness claim is a literature anchor, not a vendored-source anchor —
  hence the `partially-supports` verdict on that one row of the proposed verified_against block.
  This does NOT weaken the partly-constructive status (which rests on the Palace-side negative
  anchor, fully confirmed); it is a precision note on the enum-coverage half.
- **Gate is unchanged, promotion correctly NOT unblocked.** Unlike cycle-012's eigsolve audit
  (which UNBLOCKED a gated promotion by identifying firming edits), this audit finds NO positive
  site exists to firm against — the correct verdict is that the partly-constructive status SHOULD
  STAY until an upstream Palace change reads the reason. There are no firming edits to gate; the
  promotion condition is genuinely open. State this clearly for the cycle-015 meta-phase:
  **this is the partly-constructive ENTRY case** (a status that correctly stays), complementing
  cycle-013's eigsolve EXIT case (a status that promoted). Together they validate the
  partly-constructive mechanism as a working transient gate, not a permanent escape hatch.
- **Directionality**: the theme narrates forward (L1 `EigStatus` derivation ← how the L0 SLEPc
  reason WOULD map). The "Materialisation shape (forward-looking)" section describes a
  not-yet-in-Palace upstream change; this is correctly framed as the promotion-condition target,
  not as a reverse-direction lift narration. No direction-of-definition violation.

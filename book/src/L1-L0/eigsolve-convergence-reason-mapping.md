# eigsolve-convergence-reason-mapping

A focused **sub-theme** of the eigsolve L1>L0 family. It carries the full
`EPSConvergedReason -> EigStatus` mapping that
[`eigsolve-mutation-rotation`](./eigsolve-mutation-rotation.md)
Sub-pattern B forwarded to "a future `slepc-convergence-reason-lift`
sub-theme". It elaborates how the SLEPc backend's solver-reason
enumeration would map onto the L1 `EigStatus` sum-type
(`Converged | PartialConverged | MaxIterReached | LinearSolveFailed`) —
including the **diverged-reason** cases the parent only sketched.

This is **not** a standalone rewrite theme; it does not introduce new
LHS/RHS vocabulary. It refines the status-derivation half of the parent
theme's Sub-patterns B (the `LinearSolveFailed` constructive-introduction
for the SLEPc shell-matrix path) and C (result-status flow) for the
specific case where the L0 backend is one of Palace's three SLEPc solver
families (`SlepcEPSSolverBase`, `SlepcPEPSolverBase`, `SlepcNEPSolverBase`).

## Slug

`eigsolve-convergence-reason-mapping`

## What Palace reads vs ignores (the source-anchored boundary)

The single load-bearing source fact: **Palace fetches the converged
*count* but never inspects the converged *reason*.** All three SLEPc
`Solve()` bodies follow the identical shape:

```text
// SlepcEPSSolverBase::Solve()  (palace/linalg/slepc.cpp:687-709)
PalacePetscCall(EPSSolve(eps));
PalacePetscCall(EPSGetConverged(eps, &num_conv));     // <- count READ (line 695)
if (print > 0) {
  Mpi::Print(GetComm(), "\n");
  PalacePetscCall(EPSConvergedReasonView(eps, ...));  // <- reason PRINT-ONLY (line 699)
  Mpi::Print(GetComm(), " Total number of linear systems solved: ...");
}
RescaleEigenvectors(num_conv);
return (int)num_conv;                                 // <- only the count escapes (line 708)
```

Positively anchored facts (read from these exact source sites this cycle):

- The **count** `num_conv` is read via `EPSGetConverged`
  (`palace/linalg/slepc.cpp:695`), `PEPGetConverged`
  (`palace/linalg/slepc.cpp:1178`), `NEPGetConverged`
  (`palace/linalg/slepc.cpp:1525`) — and is the **only** value that flows
  out of `Solve()` (`return (int)num_conv` at
  `palace/linalg/slepc.cpp:708`, `1191`, and the NEP analogue).
- The **reason** is materialised by SLEPc but consumed **only** by a
  print call: `EPSConvergedReasonView` (`palace/linalg/slepc.cpp:699`),
  `PEPConvergedReasonView` (`palace/linalg/slepc.cpp:1182`),
  `NEPConvergedReasonView` (`palace/linalg/slepc.cpp:1529`). The reason
  code is never bound to a C++ variable, never branched on, never
  returned.

**Negative anchor (whole-tree).** A `search_text` for `EPSConvergedReason`,
`EPS_DIVERGED`, `EPS_CONVERGED`, and `ConvergedReason` across the Palace
tree this cycle returns **only** the three print-only `*ConvergedReasonView`
sites above — **zero** references to any `EPS_CONVERGED_*` /
`EPS_DIVERGED_*` enumerator, and **zero** calls to `EPSGetConvergedReason`
(the accessor that would bind the code to a variable). This is the negative
anchor that every reason->status row below is reconstructed against: Palace
does not positively exhibit the reason->status construct, so the table is a
**forward-looking reconstruction**, faithful to SLEPc's documented enum but
not read from a positive Palace source site.

## The mapping table

The L1 `EigStatus` sum-type
([`L1/eigsolve`](../L1/eigsolve.md) §Signature):

```text
EigStatus = Converged | PartialConverged | MaxIterReached | LinearSolveFailed
```

`EPSConvergedReason` is SLEPc's solver-outcome enum (the `PEP`/`NEP`
families carry isomorphic `PEPConvergedReason` / `NEPConvergedReason`
enums with the same converged/diverged partition). The reconstructed
mapping, combined with the positively-anchored `num_conv` count, is:

| `EPSConvergedReason` | sign | `EigStatus` (reconstructed) | row status |
|---|---|---|---|
| `EPS_CONVERGED_TOL` | converged | `Converged` if `num_conv == K_max` else `PartialConverged` | count-anchored |
| `EPS_CONVERGED_USER` | converged | `Converged` if `num_conv == K_max` else `PartialConverged` | count-anchored |
| `EPS_DIVERGED_ITS` | diverged | `MaxIterReached` (or `PartialConverged` if `num_conv > 0`) | partly-constructive |
| `EPS_DIVERGED_BREAKDOWN` | diverged | `LinearSolveFailed` | partly-constructive |
| `EPS_DIVERGED_SYMMETRY_LOST` | diverged | `LinearSolveFailed` | partly-constructive |
| `EPS_CONVERGED_ITERATING` (== 0, in-progress sentinel) | neither | unreachable post-`EPSSolve` (guard only) | partly-constructive |

The same three columns apply to `PEPConvergedReason`
(`PEP_CONVERGED_TOL` / `PEP_CONVERGED_USER` / `PEP_DIVERGED_ITS` /
`PEP_DIVERGED_BREAKDOWN` / `PEP_DIVERGED_SYMMETRY_LOST` /
`PEP_CONVERGED_ITERATING`) and `NEPConvergedReason`
(`NEP_CONVERGED_TOL` / `NEP_CONVERGED_USER` / `NEP_DIVERGED_LINEAR_SOLVE`
/ `NEP_DIVERGED_FUNCTION_COUNT` / `NEP_DIVERGED_SUBSPACE_EXHAUSTED` /
`NEP_DIVERGED_ITS` / `NEP_CONVERGED_ITERATING`). The NEP family adds
`NEP_DIVERGED_LINEAR_SOLVE` — which is the **only diverged enumerator in
any SLEPc family that has a direct, unambiguous mapping to
`LinearSolveFailed`** (it names exactly the inner-solver failure the
parent Sub-pattern B reconstructs) — plus `NEP_DIVERGED_FUNCTION_COUNT` /
`NEP_DIVERGED_SUBSPACE_EXHAUSTED`, which map to `MaxIterReached`
(resource-exhaustion without a clean inner-solve attribution).

### Per-row reconstruction notes

- **Converged rows (`*_CONVERGED_TOL`, `*_CONVERGED_USER`).** These do
  **not** introduce a new constructive caveat: when SLEPc reports a
  converged reason, the discrimination between `Converged` and
  `PartialConverged` is driven entirely by `num_conv` vs `K_max`, which is
  the **already-firm** count-discrimination of parent Sub-pattern C
  (`num_conv == K_max -> Converged`; `0 < num_conv < K_max ->
  PartialConverged`). The reason code merely confirms the count is
  trustworthy; it adds no information the count does not already carry.
  Status: **count-anchored** (the count is positively read; the
  reason->success mapping is the trivial reconstruction).

- **`*_DIVERGED_ITS` (max-iterations).** Maps to `MaxIterReached` when
  `num_conv == 0`, or `PartialConverged` when `num_conv > 0` (SLEPc can
  return both a diverged reason and a partial converged count). This is
  the diverged row that **collapses onto the count semantics** the parent
  Sub-pattern C already produces — the reason code is redundant with
  `num_conv` here. Status: **partly-constructive** (the mapping is sound
  but reconstructed; Palace never reads the reason to make it).

- **`*_DIVERGED_BREAKDOWN`, `*_DIVERGED_SYMMETRY_LOST`,
  `NEP_DIVERGED_LINEAR_SOLVE`.** These map to `LinearSolveFailed`. This is
  precisely the SLEPc-side elaboration the parent Sub-pattern B sketched
  ("the materialisation here would consume the reason code and map the
  `EPS_DIVERGED_BREAKDOWN` / `EPS_DIVERGED_SYMMETRY_LOST` family to
  `LinearSolveFailed` (rather than collapsing all SLEPc-side diverged
  reasons into `MaxIterReached`)", parent lines 296-299). Without the
  reason code, the count-only discrimination of Sub-pattern C would
  mis-classify a breakdown (where `num_conv == 0`) as `MaxIterReached`;
  reading the reason is what distinguishes a genuine
  iteration-cap-reached run from an inner-solver/Lanczos breakdown.
  Status: **partly-constructive** — and this is the row family that
  *motivates* consuming the reason code at all (it is the only
  information the `num_conv` count cannot reconstruct).

- **`NEP_DIVERGED_FUNCTION_COUNT`, `NEP_DIVERGED_SUBSPACE_EXHAUSTED`.**
  Map to `MaxIterReached` (resource exhaustion without a clean
  inner-solve attribution). Status: **partly-constructive**.

- **`*_CONVERGED_ITERATING` (the `0` sentinel).** SLEPc's in-progress
  value; cannot be observed after `EPSSolve` returns. Recorded only as a
  guard/assert target, never a producible `EigStatus`. Status:
  **partly-constructive** (degenerate; unreachable post-solve).

### Materialisation shape (forward-looking)

When (and only when) the upstream behaviour change of parent Sub-pattern B
lands, the SLEPc-path materialisation would, in addition to the per-callsite
inner-solve capture, consume the reason code immediately after the count:

```text
// After (not yet in Palace source; SLEPc-path reason consumption).
//   Replaces the print-only EPSConvergedReasonView at slepc.cpp:699
//   with a reason READ that feeds the status derivation:
EPSConvergedReason reason;
PalacePetscCall(EPSGetConvergedReason(eps, &reason));   // <- the accessor Palace does NOT currently call
EigStatus status = match (reason, num_conv) with
  | (EPS_CONVERGED_TOL,  n) | (EPS_CONVERGED_USER, n) ->
        if n == K_max then Converged else PartialConverged
  | (EPS_DIVERGED_BREAKDOWN, _)
  | (EPS_DIVERGED_SYMMETRY_LOST, _) -> LinearSolveFailed
  | (EPS_DIVERGED_ITS, n) -> if n > 0 then PartialConverged else MaxIterReached
  | (_, n)                -> if n > 0 then PartialConverged else MaxIterReached;
```

This composes with — does not replace — parent Sub-pattern B's
per-callsite inner-solve capture: the per-callsite `inner_failed` flag is
the *direct* `LinearSolveFailed` evidence; the reason-code map is the
*SLEPc-internal* corroboration that resolves the breakdown-vs-max-iter
ambiguity the count alone cannot. For the ARPACK and `QuasiNewtonSolver`
backends there is no `EPSConvergedReason` analogue — those paths rely
solely on the parent Sub-pattern B per-callsite capture — so this
reason-map sub-theme is **SLEPc-family-specific**.

## Applicability conditions

1. **`E`'s bound backend is one of the three SLEPc families**
   (`SlepcEPSSolverBase`, `SlepcPEPSolverBase`, `SlepcNEPSolverBase`).
   For ARPACK / `QuasiNewtonSolver`, this sub-theme does not apply; the
   `LinearSolveFailed` reconstruction for those backends is the parent
   Sub-pattern B per-callsite capture alone.

2. **Reason-consumption requires upstream behaviour change.** Palace
   currently calls `EPSConvergedReasonView` (print-only,
   `palace/linalg/slepc.cpp:699`), not `EPSGetConvergedReason` (the
   variable-binding accessor). The mapping table is a forward-looking
   reconstruction; it materialises only when an upstream refactor reads
   the reason code. This is the same partly-constructive gate as parent
   Sub-pattern B.

3. **Single-rank scope.** Per CLAUDE.md "Scope", the L1 form is
   single-rank. `EPSGetConverged` / `EPSGetConvergedReason` are
   rank-collective in MFEM's `Par*` world but read as single-rank here;
   the reason code is rank-replicated by SLEPc, so no MPI reduction is
   introduced by the reconstruction. Flagged once; otherwise transparent.

## Justification kind

**structural** (the converged/diverged partition + the per-family
isomorphism is a straight enumeration of SLEPc's documented enum) with
the per-row status assignment **partly-constructive** (forward-looking
reconstruction grounded in the whole-tree negative anchor — Palace prints
but never inspects the reason). This mirrors the parent theme's overall
`structural` + Sub-pattern-B-`partly-constructive` shape; this sub-theme
is the SLEPc-specific elaboration of that single partly-constructive
sub-rewrite.

Two distinct evidence bases underpin this entry; the cycle-014
lowering-verifier audit (§Verified-against) keeps them separate:

- The **Palace-side negative anchor** (Palace prints but never reads the
  reason) is a **source anchor** — fully confirmed by whole-tree
  `search_text` against the vendored `reference/palace/` tree. This is what
  grounds the partly-constructive status.
- The **8-row enum exhaustiveness** (that no SLEPc reason code a Palace
  SLEPc solver could encounter is omitted) is a **literature anchor**,
  checked against SLEPc's **documented** `EPS`/`PEP`/`NEP` convergence-reason
  enums — the SLEPc/PETSc headers are **not** vendored under `reference/`,
  so this half is verified against documentation rather than a vendored
  positive source site. It does not strengthen or weaken the
  partly-constructive status (which rests solely on the source-confirmed
  negative anchor); it bounds only the enum-coverage claim.

## Speculative L1 operators

**None.** This sub-theme refines the status-derivation of an existing
firm L1 form ([`eigsolve`](../L1/eigsolve.md)); the `EigStatus` sum-type
already carries all four variants. No new vocabulary.

## Verified-against

L0 evidence ranges (read this cycle via
`mcp__palace-codemap__read_range` / `search_text`):

- `palace/linalg/slepc.cpp:687-709` — `SlepcEPSSolverBase::Solve`:
  `EPSGetConverged` at 695 (count read), `EPSConvergedReasonView` at 699
  (reason PRINT-ONLY), `return (int)num_conv` at 708.
- `palace/linalg/slepc.cpp:1170-1191` — `SlepcPEPSolverBase::Solve`:
  `PEPGetConverged` at 1178, `PEPConvergedReasonView` at 1182
  (print-only), `return (int)num_conv` at 1191.
- `palace/linalg/slepc.cpp:1515-1545` — `SlepcNEPSolverBase::Solve`:
  `NEPGetConverged` at 1525, `NEPConvergedReasonView` at 1529
  (print-only).
- **Negative anchor (whole-tree `search_text`, this cycle):**
  `EPSConvergedReason` -> only `slepc.cpp:699`; `ConvergedReason` ->
  only `slepc.cpp:{699, 1182, 1529}` (all `*ConvergedReasonView`
  print-only); `EPS_DIVERGED` -> **zero hits**; `EPS_CONVERGED` ->
  **zero hits**. No `EPSGetConvergedReason` callsite anywhere. The
  reason->status map is therefore a forward-looking reconstruction with
  no positive Palace source site.

L1 anchor:
- `book/src/L1/eigsolve.md` — the `EigStatus` sum-type the table maps to.

Parent / sibling themes:
- `book/src/L1-L0/eigsolve-mutation-rotation.md` — the parent theme;
  Sub-pattern B forwards the full reason map to this sub-theme (parent
  line 301), Sub-pattern C provides the positively-anchored
  `num_conv`-count discrimination the converged rows reuse.
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` — the firm inner-solve
  theme; `LinearSolveFailed` is the inner-solver failure this map's
  breakdown rows corroborate.

### Lowering-verifier audit (cycle-014)

Verdict: **NEGATIVE-ANCHOR-CONFIRMED → STAYS-PARTLY-CONSTRUCTIVE.** The
whole-tree negative anchor was independently re-run this audit and is real
and complete — Palace PRINTS the reason (the three `*ConvergedReasonView`
sites) and never reads it into a status (zero `*GetConvergedReason`
callsites, zero `EPS_*_DIVERGED/CONVERGED` enumerator references). The map
is therefore a faithful forward-looking reconstruction with no positive
Palace source site, exactly as this entry asserts; the partly-constructive
status correctly **stays** (the promotion is NOT unblocked — no positive
site exists to firm against; promotion remains gated on the same upstream
behaviour change as parent Sub-pattern B). The 8-row diverged count HELD as
exhaustive, but checked against SLEPc's **documented** enum — a **literature
anchor** (SLEPc/PETSc headers are not vendored under `reference/`), NOT a
vendored positive source site. This enum-coverage half is therefore a
literature anchor; it is distinct from, and does not weaken, the Palace-side
negative anchor that underpins the partly-constructive status (which is
fully source-confirmed).

```yaml
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
    note: 8-row diverged count is exhaustive over the documented enum; exhaustiveness checked against SLEPc docs (literature anchor), NOT a vendored positive header site (caveat).
```

## Status

`partly-constructive (structural decomposition firm; per-row status
assignment reconstructed)` — the converged/diverged partition, the
per-family isomorphism (EPS / PEP / NEP), and the print-only negative
anchor are positively cited and exhaustive over the three SLEPc families.
The per-row `EigStatus` assignment is a forward-looking reconstruction
(Palace prints but never inspects the reason code; the entire Palace tree
has zero `EPS_DIVERGED_*` / `EPS_CONVERGED_*` references). Of the rows:
the **2 converged rows are count-anchored** (they reuse parent
Sub-pattern C's positively-anchored `num_conv` discrimination); the
**8 diverged-reason rows are partly-constructive** (3 EPS diverged
enumerators + the `*_CONVERGED_ITERATING` sentinel + 4 NEP-family
diverged enumerators; the PEP family is isomorphic to EPS and shares its
3 rows, non-additively). **One global promotion condition covers all 8
partly-constructive rows uniformly** (they share a single gate; no row
carries a distinct promotion path, so the gate is stated once here rather
than restated per row): promotion to firm is gated on the **same** upstream behaviour
change as parent Sub-pattern B (reading the reason code via
`EPSGetConvergedReason` + propagating to the outer-loop status); a
`lowering-verifier` audit may UNBLOCK the promotion by confirming a
positive Palace source site reads the reason and accepting the
forward-looking shape as a methodology pattern (per the cycle-012
`partly-constructive`-first-class invariant). This sub-theme's gate is
strictly downstream of the parent Sub-pattern B gate: the reason map
only materialises once the per-callsite inner-solve capture lands.

**Cycle-014 audit outcome (§Verified-against):** the status correctly
**STAYS** partly-constructive — the lowering-verifier confirmed the
negative anchor is real and complete and that **no positive site exists**
to firm against, so the promotion is NOT unblocked (unlike cycle-012's
eigsolve audit, which UNBLOCKED a gated promotion by identifying firming
edits; here there are none to gate). The enum-exhaustiveness half of the
verdict is a **literature anchor** (checked vs SLEPc's documented enum;
headers not vendored), distinct from the source-confirmed Palace-side
negative anchor — see §Justification kind.

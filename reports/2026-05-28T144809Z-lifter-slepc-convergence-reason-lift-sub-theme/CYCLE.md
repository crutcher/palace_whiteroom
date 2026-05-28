---
agent: lifter
invoked_at: 2026-05-28T144809Z
scope: L1>L0 eigsolve family — slepc-convergence-reason-lift-sub-theme (full EPSConvergedReason → EigStatus mapping)
status: integrated
integrated_at: 2026-05-28T200000Z
integration_commit: a4d7495
integration_notes: "cycle-013 finalize. New partly-constructive sibling sub-theme eigsolve-convergence-reason-mapping landed (8 diverged-row EigStatus map via real negative anchor — Palace only PRINTS the reason); discharges parent Sub-pattern B forward-pointer. SUMMARY Change-4 re-anchored past the in-cycle orthogonalize row (stale repairer anchor). Promotion = single global gate OQ eigsolve-convergence-reason-mapping-promotion. Clean run."
inputs:
  - book/src/L1-L0/eigsolve-mutation-rotation.md (firm; Sub-pattern B forwards the full reason map to "a future slepc-convergence-reason-lift sub-theme" at line 301)
  - book/src/L1-L0/index.md (theme-list row + status)
  - book/src/L1/eigsolve.md (L1 EigStatus sum-type anchor)
  - reports/2026-05-28T143232Z-abstractor-eigsolve-getconverged-forwarder-fix-and-gated-promotion/CYCLE.md (concurrent wave-1 promotion of parent Sub-pattern B; skimmed for consistency)
  - palace/linalg/slepc.cpp:687-720, 1170-1200, 1515-1545 (the three SLEPc *Solve() bodies; ConvergedReasonView print-only sites)
---

# CYCLE: slepc-convergence-reason-lift-sub-theme

## Summary

This dispatch authors a focused **sibling sub-theme** under the eigsolve
L1>L0 family — `book/src/L1-L0/eigsolve-convergence-reason-mapping.md` —
that carries the full `EPSConvergedReason → EigStatus` mapping table that
the parent `eigsolve-mutation-rotation.md` Sub-pattern B explicitly
forwarded ("a future `slepc-convergence-reason-lift` sub-theme would
carry the full mapping", parent line 301). The new file maps every
SLEPc converged-reason and diverged-reason enumerator to the L1
`EigStatus` sum-type (`Converged | PartialConverged | MaxIterReached |
LinearSolveFailed`), and it precisely separates the **two source-anchored
facts** (Palace fetches `num_conv` via `EPSGetConverged` at slepc.cpp:695,
and prints — never inspects — the reason via `EPSConvergedReasonView` at
slepc.cpp:699) from the **forward-looking reconstruction** (every
reason→status row, materialised from SLEPc's documented enum rather than
read from any positive Palace source site, since the entire Palace tree
contains **zero** `EPS_DIVERGED_*` / `EPS_CONVERGED_*` references).

Because the reason→status materialisation has no positive Palace anchor,
the whole sub-theme inherits the parent Sub-pattern B's
**partly-constructive** character: the structural decomposition (the
mapping table shape, the converged/diverged partition, the print-only
negative anchor) is firm and exhaustively cited, but the per-row status
assignment is a forward-looking reconstruction gated on the same upstream
behaviour change. All **8 diverged-reason rows are partly-constructive**
(3 EPS-level diverged enumerators + the `*_CONVERGED_ITERATING` sentinel
+ 4 NEP-family diverged enumerators; the PEP family is isomorphic to EPS
and shares its 3 rows, non-additively); the 2 converged-reason rows are likewise
reconstructed but trivially collapse onto the already-firm
`num_conv`-count discrimination of parent Sub-pattern C, so they carry no
*new* constructive caveat beyond the count semantics that are positively
anchored.

The print-only pattern is **uniform across all three SLEPc solver
families** — EPS (`EPSConvergedReasonView`, slepc.cpp:699), PEP
(`PEPConvergedReasonView`, slepc.cpp:1182), NEP
(`NEPConvergedReasonView`, slepc.cpp:1529) — so the same mapping table
applies to the linear, polynomial, and nonlinear SLEPc paths; this is
recorded as a single table with a per-family print-site citation.

## Append-vs-new-file decision (justified)

**New sibling file** `book/src/L1-L0/eigsolve-convergence-reason-mapping.md`,
not an appended Sub-pattern to `eigsolve-mutation-rotation.md`. Four reasons:

1. **The parent already named this file.** Parent Sub-pattern B line 301
   forwards to "a future `slepc-convergence-reason-lift` sub-theme" — the
   intended home is a distinct sub-theme, not an inline section.
2. **Edit-collision avoidance.** The concurrent cycle-013 wave-1
   abstractor dispatch
   (`reports/2026-05-28T143232Z-abstractor-eigsolve-getconverged-forwarder-fix-and-gated-promotion/`)
   has *pending, not-yet-applied* proposed-changes against the parent's
   Sub-pattern B snippet, its Justification-kind summary, and its entire
   `## Status` section. Appending a Sub-pattern into those same regions
   would race the wave-1 edits. The sibling file touches the parent only
   via one small, non-colliding cross-reference edit (Change 2 below).
3. **Sub-pattern-name occupancy.** The parent's Sub-pattern C name is
   already taken ("result-status flow"); a new "Sub-pattern C extension"
   would conflict with the existing C. The reason-mapping is naturally a
   SLEPc-specific elaboration of B/C, better as its own focused chapter.
4. **Parent size + firm status.** The parent is 910 lines and firm with
   an embedded machine-readable audit block; a focused sibling keeps each
   chapter coherent within itself (per the layer-coherence invariant) and
   keeps the parent's audit record stable.

## Proposed changes

### Change 1 — new file `book/src/L1-L0/eigsolve-convergence-reason-mapping.md`

```edit:book/src/L1-L0/eigsolve-convergence-reason-mapping.md
NEW FILE:
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
`lowering-verifier` audit may UNBLOCK the promotion by confirming the
enum partition against SLEPc's documented header and accepting the
forward-looking shape as a methodology pattern (per the cycle-012
`partly-constructive`-first-class invariant). This sub-theme's gate is
strictly downstream of the parent Sub-pattern B gate: the reason map
only materialises once the per-callsite inner-solve capture lands.
```

### Change 2 — parent cross-reference (non-colliding; updates the forward-pointer to the now-authored sub-theme)

> NOTE TO integrator-per-report: this is an old->new exact-string replacement
> against `book/src/L1-L0/eigsolve-mutation-rotation.md`. It touches ONLY the
> Sub-pattern B forward-pointer sentence (parent lines ~293-301), which is
> NOT in any region edited by the concurrent cycle-013 wave-1 abstractor
> dispatch (that dispatch's Change 1 edits the materialisation *snippet* at
> lines 262-291; this edit is the *paragraph after* the snippet). If the
> wave-1 changes are applied first, this old-string still matches verbatim.

```edit:book/src/L1-L0/eigsolve-mutation-rotation.md
OLD:
For the SLEPc shell-matrix path, the materialisation has an additional
elaboration: SLEPc internally exposes `EPSConvergedReason` via
`EPSConvergedReasonView` (`palace/linalg/slepc.cpp:699` — currently
*print-only*, never queried). The materialisation here would consume
the reason code and map the `EPS_DIVERGED_BREAKDOWN` /
`EPS_DIVERGED_SYMMETRY_LOST` family to `LinearSolveFailed` (rather than
collapsing all SLEPc-side diverged reasons into `MaxIterReached`).
This is documented but not specified in this theme — a future
`slepc-convergence-reason-lift` sub-theme would carry the full mapping.
NEW:
For the SLEPc shell-matrix path, the materialisation has an additional
elaboration: SLEPc internally exposes `EPSConvergedReason` via
`EPSConvergedReasonView` (`palace/linalg/slepc.cpp:699` — currently
*print-only*, never queried). The materialisation here would consume
the reason code and map the `EPS_DIVERGED_BREAKDOWN` /
`EPS_DIVERGED_SYMMETRY_LOST` family to `LinearSolveFailed` (rather than
collapsing all SLEPc-side diverged reasons into `MaxIterReached`).
The full `EPSConvergedReason` -> `EigStatus` mapping — across all three
SLEPc solver families (EPS / PEP / NEP), with the converged/diverged
partition and per-row reconstruction notes — is carried in the sibling
sub-theme
[`eigsolve-convergence-reason-mapping`](./eigsolve-convergence-reason-mapping.md)
(cycle-013; `partly-constructive`, gated downstream of this Sub-pattern B).
```

### Change 3 — index row for the new sub-theme

```edit:book/src/L1-L0/index.md
OLD:
| [eigsolve-mutation-rotation](./eigsolve-mutation-rotation.md) | `L1/eigsolve` (rough-in) | `palace/linalg/{arpack,slepc,nleps}.cpp`, `palace/linalg/eps.hpp` | firm *(structural; partly-constructive on LinearSolveFailed)* |
NEW:
| [eigsolve-mutation-rotation](./eigsolve-mutation-rotation.md) | `L1/eigsolve` (rough-in) | `palace/linalg/{arpack,slepc,nleps}.cpp`, `palace/linalg/eps.hpp` | firm *(structural; partly-constructive on LinearSolveFailed)* |
| [eigsolve-convergence-reason-mapping](./eigsolve-convergence-reason-mapping.md) | `L1/eigsolve` (`EigStatus` sum-type) | `palace/linalg/slepc.cpp:{699,1182,1529}` (reason print-only) | partly-constructive *(SLEPc reason->EigStatus map; sub-theme of eigsolve-mutation-rotation)* |
```

### Change 4 — SUMMARY.md nav entry for the new chapter

> Added by repairer (cycle-013): the exact surrounding lines were confirmed
> (`book/src/SUMMARY.md:62-64`); this old-string matches verbatim. The new
> sibling line is inserted directly under the parent `eigsolve-mutation-rotation`
> entry in the `# L1 > L0 — Lowering` Part, above `bicgstab-iteration`. Without
> this nav entry the new chapter does not render and `cargo make book` breaks.

```edit:book/src/SUMMARY.md
OLD:
- [eigsolve-mutation-rotation](./L1-L0/eigsolve-mutation-rotation.md)
- [bicgstab-iteration](./L1-L0/bicgstab-iteration.md)
NEW:
- [eigsolve-mutation-rotation](./L1-L0/eigsolve-mutation-rotation.md)
- [eigsolve-convergence-reason-mapping](./L1-L0/eigsolve-convergence-reason-mapping.md)
- [bicgstab-iteration](./L1-L0/bicgstab-iteration.md)
```

## Discipline notes

- **This is a lifter sub-theme, not a new top-level theme.** It refines
  the status-derivation half of the parent eigsolve theme (Sub-patterns
  B + C) for the SLEPc-backend case; it introduces no new LHS/RHS
  vocabulary and no new L1 operators. The parent explicitly named this
  file (line 301), so authoring it discharges a forward-pointer the parent
  left open — consistent with "re-anchor / extend within the existing
  theme family using firm vocabulary".
- **High->low direction preserved.** The sub-theme narrates how the L1
  `EigStatus` discrimination (high) would lower into the SLEPc reason->count
  reconstruction (low). No upward-lift prose entered the chapter; the
  "what would make this firm" upstream-refactor discussion is framed as a
  forward-looking materialisation note (the parent's established
  partly-constructive idiom), which is the chapter-appropriate home for a
  gated reconstruction — not a reverse-direction lift note.
- **Partly-constructive used exactly per the cycle-012 invariant.** The
  status states (i) which sub-part is constructive (the per-row status
  assignment), (ii) its negative anchors (the whole-tree zero-reference
  `search_text` + the print-only sites), and (iii) an explicit promotion
  condition (upstream `EPSGetConvergedReason` consumption + outer-loop
  status propagation, downstream of parent Sub-pattern B's gate). The
  negative anchors are evidence FOR the faithful reconstruction, not a
  positive claim that Palace produces the mapping today.
- **No prose correction performed.** I read the parent carefully; its
  Sub-pattern B forward-pointer was a promise, not an error, so Change 2
  fulfils it rather than correcting it. No L0-evidence-driven prose
  correction was needed or applied.
- **No `book/` mutation performed.** Per the write-authority phase
  boundary, this dispatch emitted proposed-changes only.

## Supporting evidence

- `palace/linalg/slepc.cpp:687-709`, `1170-1191`, `1515-1545` — the three
  SLEPc `*Solve()` bodies (count read; reason print-only; count returned).
- Whole-tree `search_text` (this cycle): `EPS_DIVERGED` -> 0 hits;
  `EPS_CONVERGED` -> 0 hits; `EPSConvergedReason` -> 1 hit (the print-only
  view at 699); `ConvergedReason` -> 3 hits (all `*ConvergedReasonView`
  print-only). The negative anchor for the whole reconstruction.
- `book/src/L1/eigsolve.md` — `EigStatus` sum-type (the target of the map).
- `book/src/L1-L0/eigsolve-mutation-rotation.md` Sub-pattern B (parent
  lines 252-308, forward-pointer at 293-301) + Sub-pattern C
  (count-discrimination, parent lines 381-403).
- `reports/2026-05-28T143232Z-abstractor-eigsolve-getconverged-forwarder-fix-and-gated-promotion/CYCLE.md`
  — the concurrent wave-1 parent promotion; skimmed to confirm Change 2's
  old-string sits outside its edited regions.

## Open questions / caveats

1. **SLEPc enum names are documented-not-source-anchored.** The specific
   enumerator names (`EPS_DIVERGED_BREAKDOWN`, `EPS_DIVERGED_SYMMETRY_LOST`,
   `NEP_DIVERGED_LINEAR_SOLVE`, etc.) come from SLEPc's public enum
   (`slepceps.h` / `slepcnep.h` in the SLEPc distribution), **not** from
   Palace source (Palace references none of them — confirmed zero-hit). Per
   CLAUDE.md "Many symbols resolve into upstream libraries", a
   `lowering-verifier` may want to cross-check the exact enumerator set
   against the installed SLEPc headers under `reference/` (if present) or
   log an upstream-behaviour open question. The mapping *shape*
   (converged->success, breakdown->`LinearSolveFailed`, its->`MaxIterReached`)
   is robust to minor enum-name drift across SLEPc versions; the *exact
   per-version enumerator list* is the part that may need an upstream
   confirmation pass.

2. **`SUMMARY.md` nav entry.** RESOLVED by repairer (cycle-013): Change 4
   now supplies the `SUMMARY.md` nav line under the L1>L0 Part (the exact
   surrounding lines `SUMMARY.md:62-64` were confirmed and the old-string
   matches verbatim). The earlier deferral (lifter could not confirm safe
   surrounding lines) is closed — no deferred `cargo make book` break remains
   from this report.

3. **Count-vs-reason redundancy on the success/its rows.** For
   `*_CONVERGED_TOL` / `*_CONVERGED_USER` / `*_DIVERGED_ITS`, the reason
   code is *redundant* with the `num_conv` count (parent Sub-pattern C
   already discriminates these correctly without it). The reason code is
   load-bearing **only** for the breakdown/symmetry-lost/linear-solve
   family (distinguishing inner-solver failure from clean
   iteration-cap-reached). A future cleanup could note that consuming the
   reason code buys *only* the `LinearSolveFailed` precision and nothing
   on the success/max-iter axis — i.e., the sub-theme's marginal value
   over the count-only Sub-pattern C is exactly the breakdown->
   `LinearSolveFailed` rows. This is captured in the per-row notes but a
   meta-phase may wish to weigh whether the sub-theme should be folded
   back into parent Sub-pattern B once its gate closes (one fewer chapter)
   vs kept separate (SLEPc-specificity). Not blocking.

4. **PEP/NEP enum isomorphism asserted, not exhaustively tabled.** I
   tabled the EPS family fully and asserted the PEP family is isomorphic
   (it is, per SLEPc's parallel `PEPConvergedReason` enum) and the NEP
   family adds `NEP_DIVERGED_LINEAR_SOLVE` / `NEP_DIVERGED_FUNCTION_COUNT`
   / `NEP_DIVERGED_SUBSPACE_EXHAUSTED`. If a `lowering-verifier` wants the
   PEP rows tabled explicitly rather than asserted-isomorphic, that is a
   small expansion; the print-only negative anchor (PEP at 1182, NEP at
   1529) is identical, so no constructive status changes.

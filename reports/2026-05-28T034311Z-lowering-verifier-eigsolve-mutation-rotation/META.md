---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T05:10:00Z
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
repaired_at: 2026-05-28T05:40:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: unrepairable
overall_status: pass-after-repair
follow_up_agent: abstractor
---

# META: verification of "Audit eigsolve-mutation-rotation"

## Critique

This is a `lowering-verifier` audit report (CYCLE.md), not an authoring report. The
critique therefore treats the audit's *findings* as the claims under verification, and
independently re-reads the cited L0 source to confirm/refute them. I re-read the four
load-bearing claims the audit hinges on (the `GetConverged` material finding, the
negative anchor, the un-scaling accessor, the ncv-clamp drift), independently
re-enumerated the ten `opInv->Mult` callsites, and confirmed the sub-pattern-A
attribution finding. All checked source claims reproduce.

### Checks run

**citation-validity — pass.** Every cited L0 range I sampled points to a real,
in-range location, and the substantive claim at each holds:
- `iterative.hpp:98` — `bool GetConverged() const { ... }` on `IterativeSolver`. Confirmed.
- `ksp.hpp` public surface — the audit cites `ksp.hpp:54-69`; the actual `public:` block
  is lines 51-71, and it exposes `NumTotalMult/NumTotalMultIterations/GetRelTol/GetAbsTol/
  SetRelTol/SetAbsTol/SetOperators/Mult` with **no** `GetConverged`; the `ksp` member is
  `protected` (39-41); `GetRelTol()` forwarder is at line 64 (exact); `ComplexKspSolver =
  BaseKspSolver<ComplexOperator>` at 75. Confirmed.
- `ksp.cpp:297-310` — `void BaseKspSolver<OperType>::Mult`, `ksp->Mult` at 300,
  `if (!ksp->GetConverged())` at 301, `Mpi::Warning` 303-306, counters 308-309, void
  return. Confirmed exactly.
- `slepc.cpp:711-716` — `return l * gamma;` at 715. Confirmed.
- `arpack.cpp:513-560` — `SolveInternal` at 552, `RescaleEigenvectors(nev)` at 555,
  `info = 0` at 558, `return num_conv` at 559. Confirmed exactly.
- `arpack.cpp:236-239` (SetWhichEigenpairs = trivial field-set) and the
  switch+`MFEM_ABORT` in `SolveInternal` (switch 279-305, abort at 302-303). Confirmed.
- The ten `opInv->Mult` callsites reproduce exactly under an independent `grep` (574, 580,
  761, 778, nleps 514, slepc 1858, 1965, 1978, 2076, 2159 — no others). Exhaustiveness
  claim confirmed independently.
The only deviations are sub-line-level and the audit itself surfaces them as findings
(see below). Pass.

**surface-or-evidence — pass.** This is a refinement-shaped report against an existing
firm theme. The audit is a *retroactive-evidence-backfill* artifact: its primary product
(Edit 1, the `verified_against:` YAML block) is per-citation verification evidence, which
is exactly the allowed "pure retroactive evidence backfill" shape for a verifier. The two
surface-touching proposals (Edits 2-3) are explicitly deferred to an abstractor reread and
not applied, so they are not the verifier authoring surface — they are flagged corrections
backed by the rotation_claim evidence (the GetConverged finding and the SolveInternal
attribution). Pass.

**rotation-quality — pass (not the verifier's own claim).** The theme under audit asserts
an L1>L0 mutation rotation (opaque `eigsolve(E, control)` → in-place `EigenvalueSolver::
Solve()` + subclass bodies + per-pair accessor extraction). That is a genuine state-hiding
rotation (the L1 form hides the RCI/shell-matrix/Newton orchestration, the mutable
workspace, the per-step `opInv->Mult` convergence-bit discard, and the int-count→sum-type
hoist). The audit does not introduce a new rotation; it verifies the existing one is
faithfully grounded. The status-derivation law-claim (`num_conv` three-way discrimination)
is checked by the audit against `eigensolver.cpp:367-374` and reproduces. Pass.

**variant-axis-coverage — pass.** The eigensolve has dense orthogonal axes (3 backends ×
9 spectrum targets × 2 spectral transformations × 3 problem types, plus sinvert/non-sinvert
per ApplyOp). The audit covers each backend family (ARPACK 4 sites, NLEPS 1, SLEPc 5),
covers both sinvert/non-sinvert branches per callsite, and explicitly verifies the ARPACK
`TARGET_REAL/TARGET_IMAGINARY` MFEM_ABORT stub (scoped out per the unimplemented-stub
policy). The one axis the audit *defers* (per-primitive decomposition of each ApplyOp body
into apply_linop/axpy/dot) is explicitly scoped out as belonging to the sister themes —
not a hidden branch. Pass.

**cross-reference-integrity — pass.** All five book cross-references named in the audit
resolve on disk (`L1-L0/ksp-solve-mutation-rotation.md`, `L1-L0/apply-linop-mutation-
rotation.md`, `L1/eigsolve.md`, `L0/eigensolver-wrapper.md`, `L0/mutable-workspace-
pattern.md`). The named slugs (`ArpackEigenvalueSolver`, `SlepcEigenvalueSolver`,
`QuasiNewtonSolver`, `BaseKspSolver`, `ComplexKspSolver`, `IterativeSolver`) all resolve
to real Palace symbols at the cited locations. Pass.

**edge-label-fidelity — pass.** The audit's declared edge is L1>L0 throughout; the prose
consistently narrates the L1 `eigsolve` form lowering into the L0 `Solve()` + subclass
bodies. The Open-questions §"Directionality (high→low): PASS" assessment is sound — the LHS
is L1, RHS is L0, and the forward-looking `LinearSolveFailed` materialisation is framed as
"how the L1 status case lowers", not as an upward lift. No L_n/L_{n+1} mislabel. Pass.

**plan-kind-consistency — pass.** Declared kind is `lowering-verifier` audit. Content shape
matches: per-citation supports/partially-supports verdicts, an exhaustiveness re-check, a
verified_against block, applicability-condition verification, and explicitly-deferred
surface proposals. No authoring masquerading as audit; no audit masquerading as authoring.
The top-level verdict `confirms-with-refinement` is consistent with the body (4 supports
families + 3 refinements, no contradictions). Pass.

**skill-uptake-survey — warning.** The report's shape implies two relevant skills should
have been invoked but neither invocation is referenced:
(1) `verify-citation-range` — this is a per-citation range-verification audit, the canonical
use of that skill; the report describes the verification but never references the skill's
invocation. (2) `verify-refinement-surface` — the report makes a surface-vs-evidence
determination on a refinement-shaped theme (the partly-constructive promotion gate). This
is a pure telemetry surface, non-blocking, but the absence is worth recording: a citation-
range audit of this density is exactly where `verify-citation-range` uptake should appear.

### Issues found

1. **[material — verified TRUE; informational for repairer] Sub-pattern B materialisation
   snippet would not compile (CYCLE.md §"Sub-pattern B — the GetConverged() accessor",
   lines 183-208; theme book lines 271-291).** The audit's central material finding
   reproduces under independent read: `GetConverged()` exists only on `IterativeSolver`
   (`iterative.hpp:98`), is reached internally via the `protected` `ksp` member, and is
   **not** on the `BaseKspSolver`/`ComplexKspSolver` public surface (`ksp.hpp:51-71`).
   `opInv` at all ten callsites is `ComplexKspSolver`, so `if (!opInv->GetConverged())` as
   written in the theme does not compile; the fix is a one-line public forwarder mirroring
   `GetRelTol()` at `ksp.hpp:64`, OR a `Mult` status-return change. This is not a defect in
   the *audit* — the audit found it correctly. It is recorded here so the repairer/integrator
   tracks that Edit 2 (the snippet correction) is a real, evidence-backed surface fix the
   theme needs, currently deferred to abstractor reread.

2. **[minor — citation precision in the audit's own range label] Public-surface range.**
   The audit labels the `BaseKspSolver` public surface `ksp.hpp:54-69` (lines 185, 194,
   594). The actual `public:` block is `ksp.hpp:51-71`. The cited 54-69 sub-range omits the
   constructors (52-58) and the trailing `Mult` declaration (71) but does contain the
   load-bearing accessors and the `GetRelTol` forwarder, so the claim is in-range and
   substantively correct. Severity: cosmetic. Location: CYCLE.md §"Sub-pattern B —
   GetConverged accessor" and Edit 1 `ksp.hpp:30-72` verified_against entry.

3. **[minor — abort line precision] MFEM_ABORT line numbers.** The audit cites the ARPACK
   `MFEM_ABORT` at "~302-304" / "300-304" (CYCLE.md lines 59, 242, 510; also the theme's own
   `arpack.cpp:300-304` at book lines 148, 526). The actual abort statement spans lines
   302-303 (the `TARGET_REAL`/`TARGET_IMAGINARY` cases at 300-301, abort 302-303, `break`
   304). All variants are in-range; the "~" hedging in the audit is appropriate. The theme's
   own `300-304` is also in-range. Severity: cosmetic.

4. **[minor — confirmed drift, correctly diagnosed] ncv-clamp citation.** The theme's
   applicability-condition 4 cites `arpack.cpp:521-525` for the ncv-clamp; the actual clamp
   `if (ncv > N) { ncv = ...; }` is at 518-520 (with `N = GlobalSize(...)` at 517), and
   522-525 is the `arpack_it` default. The audit flags this and proposes 517-520. The audit's
   correction is sound and its diagnosis ("521-525 is actually the arpack_it default") is
   correct modulo a one-line offset (default is 522-525). This is a real theme-side drift the
   audit caught; recorded as a candidate fix. Location: CYCLE.md applicability-condition 4
   (lines 382-388) and Edit 1 final verified_against entry.

5. **[minor — confirmed; correctly diagnosed] Sub-pattern A attribution.** The theme's prose
   and citation list attribute the per-`WhichType` switch + `MFEM_ABORT` to
   `ArpackEigenvalueSolver::SetWhichEigenpairs` (theme book lines 183-185). Confirmed that
   `SetWhichEigenpairs` (236-239) is a trivial `which_type = type;` field-set; the switch and
   abort live in `SolveInternal` (switch 279-305). The cited range `236-308` spans both, so
   in-range; only the function-name label is imprecise. The audit's Edit 3 correction is
   sound. Location: CYCLE.md §"Sub-pattern A" (lines 53-60, 234-246), Edit 3.

6. **[structural — for integrator attention, not a verifier error] Edit 1 may duplicate an
   existing section.** The theme already carries a prose `## Verified-against` section (book
   lines 638-738). The audit's Edit 1 proposes appending a *second*, machine-readable
   `verified_against:` YAML block at end-of-file. This is a legitimate verifier byproduct
   (per-citation verdict record) but the integrator should decide whether to (a) keep both
   (prose narrative + YAML telemetry), (b) merge, or (c) fold the audit_verdict into the
   existing section. Not a fault in the audit — flagging so the integrator does not blindly
   create a redundant section. Location: CYCLE.md Edit 1 (lines 441-561).

7. **[telemetry — soundness of the conditional promotion verdict] Assessed SOUND.** The
   audit unblocks the partly-constructive → fully-firm promotion of Sub-pattern B
   *conditional on* adopting the corrected snippet (Edit 2). I assess this as a sound verdict
   shape: the theme's own promotion gate (book lines 763-770) offers gate (b) — "a
   lowering-verifier audit that confirms the partly-constructive shape is acceptable" — and
   the audit satisfies exactly that gate. The conditionality is well-placed: it does not
   promote on the *defective* snippet, it promotes on the *corrected* one, and the correction
   is mechanical and evidence-backed (the forwarder pattern already exists on the class). The
   one caveat for the integrator: the verdict couples a *status promotion* (drop the
   partly-constructive caveat) to a *surface edit the verifier did not apply* (Edit 2,
   deferred to abstractor). The integrator should treat the promotion as **gated on Edit 2
   landing**, not as immediately applicable — i.e., do not drop the partly-constructive
   caveat in the same pass that defers the snippet fix. Recorded as a sequencing note, not a
   defect.

### Summary for repairer

No contradictions; no fabricated citations; no direction-of-definition violation. The audit
is materially accurate — all four load-bearing source claims and the ten-callsite
exhaustiveness reproduce under independent read. Issues are: one warning (skill-uptake — no
`verify-citation-range`/`verify-refinement-surface` reference), four cosmetic citation-
precision notes (issues 2-5, all already surfaced or correctly diagnosed by the audit
itself), and two integrator-sequencing notes (issue 6 possible verified_against duplication;
issue 7 promotion-gated-on-deferred-edit coupling). The material finding (issue 1) is a real
theme-surface defect the audit correctly caught and correctly deferred — the repairer should
note it as a confirmed, evidence-backed fix for the abstractor/integrator, not attempt to
apply it (it is content authoring, outside repair authority).

---

## Repair

The critic confirmed the audit is materially accurate (7 pass, 1 warning; all
findings reproduced). This is a `lowering-verifier` audit report (inspection-only —
it does not author theme content). The repairs here are correspondingly light:
align one citation-precision label, confirm no in-report duplication, and sharpen
the conditional-promotion language so the integrator does not auto-promote.

### Fixes attempted

- **Finding (issue 4, ncv-clamp citation precision):** The audit's own range label
  put the ncv-clamp at `arpack.cpp:517-520`; the critic confirmed the clamp
  `if (ncv > N) { ncv = ...; }` is at **518-520** with the N-fetch
  (`N = GlobalSize(...)`) at **517**, and the `arpack_it` default at **522-525**.
  - **Decision:** repaired.
  - **Action:** aligned all three CYCLE.md references — Summary refinement-3
    paragraph (§Summary), applicability-condition 4 (§Applicability conditions),
    and the `verified_against:` YAML entry + `audit_note` (Edit 1). Clamp now
    labelled `518-520`, N-fetch noted at 517, default noted at 522-525. The
    Supporting-evidence coarse consulted-range `513-526` already covers the clamp
    and is left as-is (in-range). This is a small-offset citation alignment within
    repair authority (the original agent's range slipped a line).

- **Finding (issue 6, possible `verified_against` duplication):** The critic
  flagged that Edit 1's machine-readable `verified_against:` YAML block might
  duplicate the theme's existing prose `## Verified-against` section (book lines
  638-738).
  - **Decision:** not-needed (no in-report duplication; the flagged duplication is
    a book-side integrator decision, not a report defect).
  - **Action:** verified via grep that CYCLE.md contains exactly one
    `verified_against:` block (line ~446) and one `audit_verdict:` (line ~547) —
    no duplication inside the report. The concern the critic raised is about
    *applying* Edit 1 to the book (whether to keep both the prose section and the
    YAML telemetry, merge, or fold) — that is an integrator authoring/merge
    decision, outside repair authority and outside the verifier's write surface.
    Routed to the integrator note below.

- **Finding (issue 7, conditional-promotion sequencing):** The critic assessed the
  conditional promotion verdict SOUND but flagged that it couples a status
  promotion (drop the partly-constructive caveat) to a surface edit the verifier
  did not apply (Edit 2, the GetConverged forwarder snippet correction), and that
  the integrator should treat the promotion as gated on Edit 2 landing.
  - **Decision:** repaired (clarification of report language only — mechanical,
    no content authored).
  - **Action:** sharpened three places in CYCLE.md to state explicitly that the
    audit **unblocks but does NOT enact** the promotion, that promotion is **gated
    on a cycle-013 abstractor dispatch applying Edit 2 first**, and that the
    integrator must NOT auto-promote the theme to firm this cycle: (1) the
    §Summary "Promotion outcome" paragraph, (2) the §Open-questions "Sub-pattern B
    promotion verdict" caveat (re-titled "GATED — not enacted this cycle"), and
    (3) the Edit 1 `audit_note` machine-readable telemetry. No content authored —
    the audit's verdict shape is unchanged; only the gating/sequencing is made
    unambiguous so a reader cannot mistake "unblocks" for "promote now".

- **Finding (issue 1, material GetConverged finding):** The audit correctly found
  the Sub-pattern B materialisation snippet (`if (!opInv->GetConverged())`) would
  not compile (GetConverged is not on `BaseKspSolver`'s public surface) and
  correctly deferred the fix (Edit 2) to an abstractor reread.
  - **Decision:** not-needed (no repair — the audit already handled it correctly;
    applying Edit 2 is content authoring outside both the verifier's and the
    repairer's authority).
  - **Action:** none on the report. Recorded for the integrator/abstractor: Edit 2
    is a real, evidence-backed surface fix the theme needs; it is the gating
    precondition for the promotion (see issue 7 above).

### Unrepairable findings

- **skill-uptake-survey (warning):** The report does not reference invocation of
  `verify-citation-range` (canonical for a per-citation range audit of this
  density) or `verify-refinement-surface` (the surface-vs-evidence determination
  on the promotion gate). This is pure telemetry — non-blocking, non-mechanical,
  and cannot be repaired by editing the report (the skills were either invoked
  without reference or not invoked; the repairer cannot retroactively author skill
  uptake). Left as a `warning`. Routed to meta-phase as recurring skill-uptake
  telemetry rather than a per-report defect. No `follow_up_agent` action required
  for this finding specifically.

## Suggested resolution

`overall_status: pass-after-repair`. The audit is materially sound and the three
repairable items (one citation alignment, one no-in-report-duplication
confirmation, one conditional-promotion clarification) are applied. The report is
ready for the integrator with two carried-forward, non-blocking items:

1. **Integrator note — do NOT auto-promote this cycle.** The
   eigsolve-mutation-rotation theme must NOT be promoted from partly-constructive
   to fully-firm in this integration pass. The audit UNBLOCKS promotion but does
   not enact it; promotion is gated on a **cycle-013 `abstractor` dispatch**
   applying Edit 2 (the GetConverged public-forwarder snippet correction, mirroring
   the existing `GetRelTol()` forwarder at `ksp.hpp:64`) to the theme. Drop the
   partly-constructive caveat only AFTER that edit lands. `follow_up_agent:
   abstractor` (cycle-013).

2. **Integrator decision — `verified_against` application shape.** When applying
   Edit 1, decide whether to keep both the existing prose `## Verified-against`
   section and the new machine-readable `verified_against:` YAML block, merge them,
   or fold the `audit_verdict` into the prose. This is a book-side merge decision
   (integrator authority), not a report defect.

The skill-uptake warning is left for meta-phase as telemetry; it does not block
integration.

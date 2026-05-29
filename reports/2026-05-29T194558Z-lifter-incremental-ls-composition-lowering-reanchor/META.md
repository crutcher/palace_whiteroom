---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T201500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: warning
repaired_at: 2026-05-29T203000Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: unrepairable
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Re-anchor incremental-least-squares-composition-lowering"

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck.py --scan` on the report: **43 ok, 1 failing** (44 citations). The single MISS is `META.md:89` (CYCLE.md:569) — a relative cross-reference to the c027 deferred report's own META repair record, which citecheck cannot resolve (it scans only `reference/` + `book/src`). I confirmed the target on disk (`reports/2026-05-29T175529Z-abstractor-incremental-ls-composition-lowering/META.md`) and that line 89/100 carries the option-(a) text the producer quotes — the provenance reference is accurate, not a defect. I then spot-checked the full set of load-bearing L0 pinpoints with `--anchor` against on-disk `reference/palace/`: replay `:634-636`, generate `:638`, apply_rhs `:640`, beta `:642`, back-solve `:652-660`/`:656`/`:659`, V-recon `:666`, right-precond `:674-677`, FGMRES stream `:812-821`/`:813-815`, FGMRES back-solve `:831-840`, Z-recon `:843`, register split `iterative.hpp:193`/`:194`, unitarity `:118` — **every one resolved `[ok]` exact**, including the c026 `iterative.hpp:193-194` +1-brace-drift correction the producer claims was re-confirmed on-disk. The book-internal cross-refs (`back_solve.md:44-61` for the NOT-a-trsv argument, `back_solve.md:109-110` for the j=0 scalar division, L2 entry `:278-285` non-law, back_solve laws 5/6, L2 entry law 1/2/6 + §Variant axes) all resolve and say what is claimed. The producer's self-verification is genuine and well-supported. The warning is for **two stale/incorrect supporting cites that do not gate any positive claim** (see Issues 1 and 2).

**surface-or-evidence — pass.** This is a refinement-shaped proposal (a `rough-in→firm` promotion) but it is delivered as a `new:` block because the theme never integrated in c027 (confirmed: `book/src/L2-L1/incremental-least-squares-composition-lowering.md` is NOT on disk). The proposal modifies surface (the full theme body) AND is grounded in exhaustive self-verified L0 evidence (the §Verified-against block + §"Reduction-path recording" table). Not a pure rotation_claim without surface. Passes.

**rotation-quality — pass.** The theme asserts a genuine L2→L1 fan-down (de-fusion): the single named L2 composition `incremental_least_squares` fans into a fixed scalar-Givens-kernel sequence (replay×j ▷ generate ▷ apply ▷ apply_rhs) + a terminal `back_solve` ▷ `linear_combination` reconstruction. This is a real lowering — one compact named L2 op expands into multiple L1 primitive calls, the L2 form is strictly more compact/abstract than the spelled-out L1 form (correct directionality for a lowering theme). Not a rename, not a 1:1 mapping. The load-bearing residue (fixed non-commutative replay-before-generate ordering + LAPACK scaling, no MPI collective) is correctly identified and pinned. Passes.

**variant-axis-coverage — pass.** Two orthogonal variant axes are present and both are explicitly covered: `op.variant ∈ {real, complex}` (scalar-kernel element-type substitution, Applicability condition 3) and `op.basis_kind ∈ {V, Z}` (GMRES/FGMRES reconstruction-basis selection, condition 4). The producer correctly establishes both are **parametric absorption** (substitution without changing the sub-step sequence/ordering/reduction shape), distinguishing them from the sibling's genuinely-structural MGS/CGS/CGS2 axis (§"Why the sequence is fixed"). Householder is explicitly scoped out per the unimplemented-component policy. No hidden branches. Passes.

**cross-reference-integrity / build-readiness — pass.** Ran the fence-parity guard (`proposed-changes-fence-encloses-full-body-guard` procedure): **6 fence markers, 3 balanced blocks** (`new:` 26-526, `edit:index.md` 537-540, `edit:SUMMARY.md` 546-549) — even parity. Confirmed the firm apparatus (`## Status` at line 440, plus Slug/Signature-form/Algebraic-content/Verified-against) is **fully INSIDE** the `new:` fence (26-526). Confirmed **zero nested code fences** inside the `new:` block (27-525) — all inner code samples are 4-space-indented, exactly as the producer asserts. This is NOT the cycle-019 fence-truncation defect. All `[link]` targets resolve on disk: `back_solve.md`, `incremental-least-squares.md` (L2), `orthogonalize-composition-lowering.md`, `linear_combination.md`, and all six concept pages exist; `ls_update_column` is correctly left **plain-text** (not on disk, forward-ref); the theme's own slug becomes a live link once the `new:` block applies. The index.md edit anchor (row 19, `eigsolve-spectral-transform-composition`) IS the last table row and the new row's 4-column shape matches the header. The SUMMARY edit anchor (`orthogonalize-composition-lowering`, line 56, unique) resolves. Passes (a prose-accuracy error in the surrounding discipline note is logged as Issue 3 — it does not affect the edits themselves).

**edge-label-fidelity — pass.** The theme is labeled `L2>L1` (or `L2 → L1`) throughout and the prose consistently discusses the L2→L1 edge. Every `L1>L0` mention is correctly framed as a forward-reference to the leaves' OWN downstream concern (explicitly deferred — "this theme stops at the L1 leaf"), never conflated with the theme's own edge. No edge-label/prose mismatch.

**plan-kind-consistency — warning.** Declared kind is `firm` L2>L1 theme. The structural decomposition IS firm (the rewrite is recognized and exhaustively cited). However the firm-promotion rests on one judgment call that departs from the cited precedent in a material way (Issue 4): the sibling `orthogonalize-composition-lowering` firm bar the producer invokes has **both** L1 RHS faces resolving to firm on-disk leaves (Face 1 = the firm `orthogonalize` leaf, cycle-012; Face 2 = firm `dot`/`axpy`), whereas in this report the opaque Face-1 leaf (`ls_update_column`) is **not on disk** — only Face 2 + terminal `back_solve` are firm. The producer's promotion hinges on Face 2 alone carrying the firm value (Face 1 co-extensive, "a resolution choice not a value choice"). The reasoning is defensible and the producer flags it transparently as the one non-mechanical decision (body unaffected if reverted to `rough-in` — only `## Status` changes), so this is a warning, not a fail — but the firm bar here is genuinely thinner than the precedent it cites.

**skill-uptake-survey — warning (telemetry, non-blocking).** The report references `verify-citation-range` (self-verification) and `audit-slug-meaning-before-coordinated-cross-report-rename` (deferral cause). Given the report's shape — a `new:` block enclosing a full firm body — the directly-relevant `proposed-changes-fence-encloses-full-body-guard` skill is NOT referenced; and the SUMMARY.md surgical insert does not reference `summary-md-surgical-insert`. Pure presence check; surfaced as telemetry only.

### Issues found

1. **Stale supporting cite `open-questions.md:448`** (CYCLE.md:497, :577; §Open-questions caveat + Discipline-note 2). The producer cites `scaffolding/open-questions.md:24,:448` for the general-`trsv`-BLOCKED claim. `:24` is correct (the `l3-vocabulary-inventory-gap` line, "REMAINING: `trsv` ONLY (BLOCKED, no L1 anchor)"). But `:448` is the **empty "Dropped" section header** ("(none — dropped items are filed under Closed…)") — it carries NO trsv content. The correct companion line is `:498` ("`trsv` — BLOCKED (no firm L1 anchor)"). This `:448` cite is inherited verbatim from the c027 deferred META (which also cited `:24,:448`) and the ledger line content has since shifted. **Severity: low** — the underlying claim (trsv blocked, no positive L0 anchor) is TRUE and well-supported by `:24`/`:498`; only the pointer is wrong. Candidate repair: re-point `:448` → `:498` at both sites (CYCLE.md:497, :577).

2. **Inherited-cite drift in the c027 META quote** (CYCLE.md:569, Discipline-note 1). The producer quotes the c027 repairer's option-(a) at `META.md:89,100`. The quote text is accurate, but note the c027 META at that location cites `back_solve.md:90-107` for the NOT-a-trsv argument, whereas the producer's own body correctly uses `back_solve.md:44-61` (I verified on disk: the "Why this is NOT a general `trsv`" heading is at line 44; `:90-107` drifts −31). The producer landed the **correct** range in its own body — this issue is only that the quoted provenance pointer (`META.md:89,100`) is itself a within-repo reference citecheck flags as a MISS (the file is resolvable by hand but not by the scanner). **Severity: very low** — informational; no false claim. The producer silently corrected the inherited drift, which is good.

3. **Discipline-note mis-states the SUMMARY.md neighbour lines** (CYCLE.md:553-554). The note claims "The `eigsolve-spectral-transform-composition` and `deflate-composition-lowering` SUMMARY lines `:57-58` are unaffected." The actual SUMMARY.md lines 57-58 are `gram-fold-specialization` and `deflate-composition-lowering` (verified on disk); `eigsolve-spectral-transform-composition` is line 59. The insertion still works mechanically (the edit anchors on the unique `orthogonalize-composition-lowering` line 56 and appends after it — the surgical-insert pattern does not depend on the stated neighbour lines), so this is a **prose-accuracy error in the rationale only**, not a build defect. **Severity: low.**

4. **Firm-promotion judgment thinner than the cited sibling precedent** (CYCLE.md §Status :455-464, §Open-questions :473-482, Discipline-note 4 :587-598). The promotion to `firm` cites the sibling `orthogonalize-composition-lowering` firm bar as its template, but the sibling has BOTH L1 RHS faces firm-on-disk (Face 1 `orthogonalize` leaf landed cycle-012; the sibling body literally states "two co-extensive faces … **both firm**"). This report's analogous Face 1 (`ls_update_column`) is NOT on disk — so the "both faces firm" symmetry the sibling enjoyed does not hold here; only Face 2 (de-fused Givens kernels) + terminal `back_solve` + `linear_combination` are firm. The producer's value-carrier argument (Face 2 co-extensive with Face 1, so the opaque-leaf forward-ref is not a value-gate) is internally coherent and transparently flagged, and the de-fused Face 2 IS a complete firm value-path, so the promotion is defensible. But a reviewer applying the sibling bar strictly (both faces firm-on-disk) could hold the theme at `rough-in` until `ls_update_column` lands. The producer explicitly invites this confirm-or-revert and notes the body is unaffected by the decision (only `## Status`). **Severity: medium** — this is the report's single load-bearing judgment call; it is the right thing to surface to the integrator. Not a content defect; a status-bar adjudication.

5. **`skill-uptake-survey` telemetry (non-blocking):** the `proposed-changes-fence-encloses-full-body-guard` and `summary-md-surgical-insert` skills are not referenced despite the report's shape (full-firm-body `new:` block + SUMMARY surgical insert) being exactly their domains. Surfaced as telemetry per the check's pure-presence nature; no action required of this report.

## Repair

### Fixes attempted

- **Finding (citation-validity Issue 1)**: Stale supporting cite `open-questions.md:448` for the general-`trsv`-BLOCKED claim — `:448` is the empty "## Dropped" header (verified on disk: line 448 = `## Dropped`, 449 = the "(none …)" note); the correct companion line is `:498` ("`trsv` — BLOCKED (no firm L1 anchor)…", verified on disk). Inherited verbatim from the c027 deferred META; the ledger content shifted.
  - **Decision**: repaired.
  - **Action**: re-pointed `:24,:448` → `:24,:498` at both occurrences in CYCLE.md (§Open-questions caveat "General `trsv` remains BLOCKED" + Discipline-note 2 "General `trsv` demoted to a forward note"). Mechanical pointer correction; the underlying claim (trsv blocked, no positive L0 anchor) is unchanged and remains supported by `:24`/`:498`.

- **Finding (citation-validity Issue 2)**: Within-repo cross-reference `META.md:89,100` (a quote of the c027 repairer's option-(a)) is a citecheck `MISS` because the scanner only resolves `reference/` + `book/src`.
  - **Decision**: not-needed.
  - **Rationale**: the critic verified the target on disk and confirmed the quote text + provenance pointer are accurate ("very low / informational; no false claim"). This is a deliberate intra-`reports/` provenance reference, not a malformed L0 citation — there is no mechanical cite-format fix to apply, and the reference is correct as-is. The producer also silently corrected the inherited `back_solve.md` drift (`:90-107` → the correct `:44-61`) in its own body, which the critic confirmed exact on disk.

- **Finding (citation-validity Issue 3)**: Discipline-note prose mis-states the SUMMARY.md neighbour lines — claimed `:57-58` are `eigsolve-spectral-transform-composition` + `deflate-composition-lowering`; actual `:57-58` are `gram-fold-specialization` + `deflate-composition-lowering` (verified on disk; `eigsolve-spectral-transform-composition` is `:59`). The SUMMARY `edit:` anchors on the unique line-56 `orthogonalize-composition-lowering` sibling and is mechanically unaffected.
  - **Decision**: repaired.
  - **Action**: corrected the §"`edit:book/src/SUMMARY.md`" rationale prose in CYCLE.md (the parenthetical naming the unaffected neighbour lines) to name `gram-fold-specialization` + `deflate-composition-lowering` at `:57-58` and `eigsolve-spectral-transform-composition` at `:59`. Prose-accuracy fix only; the edit anchor and the surgical-insert mechanics are untouched.

- **Finding (plan-kind-consistency Issue 4)**: The `firm`-promotion judgment is thinner than its cited `orthogonalize-composition-lowering` precedent — the sibling had BOTH L1 RHS faces firm-on-disk, whereas here Face-1 `ls_update_column` is not on disk (only de-fused Face 2 + terminal `back_solve` + `linear_combination` carry firm value).
  - **Decision**: unrepairable.
  - **Rationale**: exceeds repair authority — this is a `## Status`-bar adjudication (`firm` vs `rough-in`), not a mechanical fix. Setting it either way is a content/maturity decision. It is NOT a content defect: the body is fully citecheck-clean and identical regardless of the verdict (the producer states the body is unaffected if reverted to `rough-in` — only `## Status` changes), and the producer transparently flagged it as the report's single non-mechanical decision, explicitly inviting the integrator/critic to confirm-or-revert. Routed to the integrator for status adjudication at integration time (see Suggested resolution); does not block application.

- **Finding (skill-uptake-survey Issue 5)**: `proposed-changes-fence-encloses-full-body-guard` + `summary-md-surgical-insert` skills not referenced despite matching the report's shape.
  - **Decision**: not-needed.
  - **Rationale**: pure-presence telemetry, explicitly flagged non-blocking by the critic; no action required of this report. (The corresponding behaviours were nonetheless exercised: the critic independently ran the fence-parity guard and confirmed even parity / firm-apparatus-inside-fence / zero nested fences, and the SUMMARY surgical insert anchors correctly.)

### Unrepairable findings

- **plan-kind-consistency Issue 4 — `firm` vs `rough-in` status-bar adjudication.** Unrepairable by mechanical means (it is a maturity decision, not a fix), but **does not block** — the critic deemed the promotion defensible and transparently-flagged, and the body is invariant to the decision. Follow-up routing: the **integrator** adjudicates the status bar at integration time (no producer rework needed). `follow_up_agent: null` — there is no missing operator/theme content for a harvester/abstractor to author; the only open decision is the maturity tier, which the integrator owns under the accumulate-surface-with-embedded-friction discipline.

## Suggested resolution

`ready`. The two mechanical cite/prose corrections (Issues 1, 3) are applied in CYCLE.md; Issues 2 and 5 are non-defects (not-needed). The sole non-repaired finding (Issue 4) is a status-bar adjudication, not a content defect — the integrator should apply the report and decide the `firm` vs `rough-in` tier:

- The producer's case for `firm`: the fan-down rule IS the L2 entry's already-firm laws 1/2/6 read as a lowering; the value-carrying faces (de-fused Face 2 + terminal `back_solve` + `linear_combination`) are all firm-on-disk; Face 1 (`ls_update_column`) and Face 2 are co-extensive presentations ("a resolution choice, not a value choice"), so the opaque-leaf plain-text forward-ref is not a value-gate.
- The reviewer-side caution: the cited sibling enjoyed BOTH faces firm-on-disk; a strict reading of that bar would hold the theme at `rough-in` until `ls_update_column` lands.

Either verdict applies cleanly — the body, all L0 evidence, the dep-map row, and the SUMMARY insert are identical; only the `## Status` value and the dep-map status column differ. The producer's §Open-questions "Firm-promotion judgment record" and Discipline-note 4 already carry the explicit confirm-or-revert hook for whichever tier the integrator chooses. The follow-on `ls_update_column` column-streaming-leaf harvest (a small L1 leaf, follow-on harvester target) and the OQ-766 closure are correctly recorded for the meta-phase, not actions for this report.

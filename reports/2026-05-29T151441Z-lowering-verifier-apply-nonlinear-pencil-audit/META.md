---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T161500Z
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
repaired_at: 2026-05-29T162400Z
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

# META: verification of "Audit apply-nonlinear-pencil-mutation-rotation"

## Critique

This is an AUDIT report (lowering-verifier dispatch): it authors no content, it audits an
existing firm L1>L0 theme and proposes a purely-additive `verified_against:` YAML block. The
8-check checklist is adapted accordingly — citation-validity is load-bearing (it IS the audit
product); surface/rotation/variant-axis/edge-label degrade to "does the audit faithfully
characterize the audited theme" rather than "does this report rotate anything."

### Checks run

**citation-validity — pass (LOAD-BEARING, independently re-run).** I re-ran
`tools/citecheck/citecheck.py --scan` on the report's CYCLE.md: **47 ok, 0 failing** (all ranges
in-bounds, all paths resolve to `reference/palace/`). I then independently re-ran `--anchor`
spot-checks on every decisive pinpoint the task flagged plus the rest of the load-bearing set —
all `OK`:
- `:810-811` comment-anchor `P(` lands at line **810**, within the cited range. I read
  `nleps.cpp:805-821` directly: line 810 is `// Compute the i-th eigenpair residual: || P(λ) x ||₂
  = || (K + λ C + λ² M + A2(λ)) x ||₂`. The cycle-024 "off-by-one on an off-by-one"
  re-confirmation **holds** — the wide `810-811` citation is correct and the prior critic
  off-by-one finding remains itself off by one. The OQ ledger (`open-questions.md:294`) already
  records this same cycle-024 verdict; the report is consistent with it.
- Form A body: `opK->Mult(x, r)` @812, `opC->AddMult(x, r, l)` @815 (inside `if (opC)` @813),
  `opM->AddMult(x, r, l * l)` @817, `funcA2` @818, `A2->AddMult(x, r, 1.0)` @819,
  `Norml2(comm, r)` @820 — all anchor-confirmed and visually matched.
- Form B: `BuildParSumOperator` @557 / @498, `A->Mult(vv, rr)` @559, lagged-refresh
  `BuildParSumOperator` @729; Jacobian coeff `2.0 * eig` @655; `funcA2 = A2` @180;
  `rap.cpp` `nullptr`-skip @837; `nleps.hpp:146` class comment; `eps.hpp:70` complex-arg closure
  type. All `OK`. I read `:494-500`, `:554-560`, `:648-657`, `:726-731` source directly — every
  per-line claim matches.
The audit's "24/24 anchors land, zero drift" verdict is **independently reproduced and sound**.
The test-coverage-absence claim is also reproduced: `grep -rE 'QuasiNewton|funcA2|GetResidualNorm|nleps'`
over `reference/palace/test/unit/` returns zero hits.

**surface-or-evidence — pass.** Adapted: this is an audit of a refinement-shaped theme, not a new
refinement. The proposed change is correctly framed as **pure retroactive evidence backfill** (a
`verified_against:` provenance block, no surface edit, no status change) — explicitly allowed. I
spot-checked 3 per-line table rows against source: row `:812` (`opK->Mult` init), row `:817`
(`opM->AddMult(x, r, l*l)` → λ² term), and Form B row `:557-559` (`BuildParSumOperator({1, lam,
lam², 1}, ...)` + `A->Mult(vv, rr)`) — each claimed L0 form maps to its actual source line. No
fabricated mappings.

**rotation-quality — pass (not applicable to audit-kind).** No rotation is asserted by this
report; it audits an already-landed rotation. The audited theme's L1→L0 mutation rotation is not
re-litigated here. Marked pass / N/A.

**variant-axis-coverage — pass.** The audit's "Applicability conditions" section enumerates all
the theme's orthogonal axes (with-C/without-C damping via `Maybe C` and the two `SetOperators`
overloads `:191`/`:221`; complex-only element type; real-arg `A2(|Im λ|)` vs full-complex
polynomial coeffs; single-rank scope; Form-A-vs-Form-B build-form choice) and marks each
verifiable with explicit "Counter-example? No." The with-C/without-C axis is the load-bearing one
and is correctly handled (the `if (opC)` guard @813 + both overload signatures confirmed). No
hidden branches.

**cross-reference-integrity — pass.** The `edit:` target
`book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md` exists on disk and is wired into
`SUMMARY.md:105`. The insert anchor "[append at end of file]" is sound: the file currently ends
with the L1/cross-theme anchors list and carries **no** pre-existing `verified_against:` block
(the only `verified_against` occurrence is at theme line 44 — prose in the Status section
*anticipating* this follow-up, not a block to collide with), so the append is non-duplicative.
The cited L1-operator law lines resolve and support: `apply_nonlinear_pencil.md:63` (law 3 term
decomposition → `:812-819`), `:64` (law 4 coefficient-vector linearity), `:65` (Jacobian
`{0,1,2λ,1}`), status `:98` firm-on-positive-structure — all read and confirmed. The
firm-body-inside-fence build-readiness guard is N/A: this report makes no `firm`-chapter claim
whose body must sit inside the fence (it is an additive YAML block on an already-firm theme).
Fence note: the proposed-changes block uses `~~~` triple-tilde as a stand-in for the inner
triple-backtick fence with an explicit parenthetical instruction to emit backticks (CYCLE.md:238);
this is the standard nested-fence convention and parses cleanly — flagging for integrator
awareness, not as a defect.

**edge-label-fidelity — pass.** The theme is an L1>L0 edge; the report narrates the rewrite
forward (L1 pencil apply = LHS, L0 source forms = RHS) throughout, and its own closing note
(CYCLE.md:276-277) confirms no high→low violation. The edge discussed matches the edge labelled.

**plan-kind-consistency — pass.** Declared as a lowering-verifier audit; content is exactly an
audit (per-citation verification table + applicability-condition review + law cross-check +
additive provenance block, no new operator/theme authored, no status change). Shape matches kind.

**skill-uptake-survey — pass.** The report explicitly invokes the role-spec citecheck mechanism
(`tools/citecheck/citecheck.py --anchor`, 24 anchor checks) and the `verify-citation-range` skill's
mechanical realization — the relevant skill for an audit-of-citations is surfaced. Telemetry
present.

### Issues found

No fail-severity or warning-severity issues. The audit is sound: I independently reproduced the
mechanical verdict (47/47 in-bounds via `--scan`; every load-bearing `--anchor` `OK`; every
per-line source claim matched by direct read). Three low-severity observations for the
repairer/integrator, none blocking:

1. **[low — OQ-closure scope, not a citation defect] The recommended OQ closure is bundled, not
   standalone.** The report (CYCLE.md:260-263) recommends the integrator close OQ
   `apply-nonlinear-pencil-mutation-rotation-lowering-verifier-audit-followup` "on application."
   But in the ledger that slug is **not** a standalone entry — it is one of four slash-joined
   slugs on a single migrated-to-plan line (`open-questions.md:327`), the other three being
   `deflate-composition-...-audit-followup`,
   `gram-fold-specialization-l2-gram-forward-reference-closure-followup`, and
   `orthogonalize-composition-...-boundary-audit` (the batch-6-firm-theme lowering-verifier audit
   bundle). The integrator must close/strike **only this slug's clause**, not the whole line
   (the other three are separate audits that may still be open). Worth flagging so the closure
   is surgical and doesn't prematurely retire the sibling audits. (where: CYCLE.md §"Open
   questions / caveats" line 260-263 vs `scaffolding/open-questions.md:327`.)

2. **[very-low — in-table imprecision, no drift] Jacobian table-row ops-line.** The Jacobian row
   (CYCLE.md:71) reads `opJ = BuildParSumOperator({0, 1, 2·eig, 1}, {opK, opC, opM, opAJ.get()}, true)`
   as "exact at `:655`." The **coefficients** are at 655 (anchor-confirmed); the operator list +
   `true` are on line 656 (the call spans 655-656). The cited pinpoint `:655` is the coeff line
   and is correct; the inline rendering of the full call against a single line number is a
   cosmetic compression, not a citation drift. Same harmless compression appears for the
   `:557-558` / `:498-499` rows where coeffs and ops legitimately split across the two-line range.
   (where: CYCLE.md §"Jacobian build" table, line 71.)

3. **[very-low — provenance completeness] `verified_against:` block omits two audited anchors.**
   The report's per-citation audit covers `:497` and `:728-730` (and `:650-655` for the
   divided-difference closure) in the body tables, but the proposed `verified_against:` YAML lists
   `:496-499` (collapsing `:497`/`:498-499`) and `:729` (collapsing `:728-730`) and does not
   separately enumerate `:650-655`. This is a reasonable range-collapse, not an error — every
   audited anchor is represented by an enclosing range — but a reader cross-referencing the body
   table's 24-row count against the block's 22 entries may notice the collapse. Noting for
   integrator awareness; no action required. (where: CYCLE.md proposed-changes block lines
   153-235 vs per-citation tables lines 41-79.)

The "24/24 cited L0 anchors land" claim (CYCLE.md:81) is accurate as a count of the **distinct
pinpoints the audit checked**; my independent `--scan` counted 47 citation tokens in the report
(it double-counts the same anchors in both the `inputs:` frontmatter and the body), all in-bounds —
no contradiction, just a different denominator (frontmatter-inclusive vs body-distinct).

## Repair

All 8 critic checks are `pass`. The critic logged no fail- or warning-severity findings — only
three low-severity, explicitly-non-blocking observations. No mechanical/surgical repair is
warranted; the report is a sound audit whose mechanical verdict the critic independently
reproduced (47/47 in-bounds via `--scan`, every load-bearing `--anchor` `OK`, every per-line
source claim matched). The `verifies:` frontmatter already reads `../CYCLE.md` (no stale
`../REPORT.md` to fix). `overall_status: ready`.

### Fixes attempted

- **Finding (low / integrator-awareness, IMPORTANT): bundled OQ closure.** The report
  (CYCLE.md:260-263) recommends closing OQ
  `apply-nonlinear-pencil-mutation-rotation-lowering-verifier-audit-followup` on application. In
  the ledger this slug is **not** a standalone entry — it is the **first of four slash-joined
  slugs on a single migrated-to-plan line** (`scaffolding/open-questions.md:327`), the other
  three being `deflate-composition-lowering-mutation-rotation-lowering-verifier-audit-followup`,
  `gram-fold-specialization-l2-gram-forward-reference-closure-followup`, and
  `orthogonalize-composition-lowering-three-way-delegation-boundary-audit` (the batch-6-firm-theme
  lowering-verifier audit bundle).
  - **Decision**: not-needed (no report edit fixes this; it is an integrator-execution concern,
    surfaced here as required).
  - **Rationale**: The report's recommendation is *correct* for its own slug — there is nothing
    in CYCLE.md to repair. The risk lives entirely in how the integrator strikes the OQ line:
    closing the whole `:327` line would prematurely retire three sibling audits, several of which
    ALSO ran this cycle and are independent. Surgically editing the shared OQ line is the
    integrator's authority (`scaffolding/open-questions.md` is integrator-per-report append-only /
    meta-phase unify), not the repairer's. I confirmed `open-questions.md:327` matches the
    critic's description exactly. **Integrator action required: close/strike ONLY the
    `apply-nonlinear-pencil-mutation-rotation-lowering-verifier-audit-followup` clause from the
    `:327` line; leave the other three slugs intact.**

- **Finding (very-low / cosmetic): Jacobian table-row ops-line.** The Jacobian row (CYCLE.md:71)
  renders the full `BuildParSumOperator({0, 1, 2·eig, 1}, {opK, opC, opM, opAJ.get()}, true)` call
  "at `:655`" though the operator list + `true` continue on 656.
  - **Decision**: not-needed.
  - **Rationale**: The cited pinpoint `:655` is the coefficient line and is anchor-confirmed
    correct (`citecheck --anchor` lands `{0.0, 1.0, 2.0*eig, 1.0}` at 655). The inline rendering
    is a harmless one-line compression of a two-line call, not a citation drift. Per the task and
    critic: leave it.

- **Finding (very-low / provenance completeness): `verified_against:` range-collapse.** The
  proposed YAML block lists `:496-499` (collapsing `:497`/`:498-499`) and `:729` (collapsing
  `:728-730`), and does not separately enumerate the `:650-655` divided-difference closure row.
  - **Decision**: not-needed.
  - **Rationale**: Every audited anchor is represented by an enclosing range — a reasonable
    range-collapse, not an omission. Authoring additional enumerated entries would be substantive
    content authoring beyond repair authority, and is unnecessary since coverage is complete. Per
    the task and critic: leave it.

### Unrepairable findings

None. No finding required substantive authoring or contradicted existing artifact content. The
single IMPORTANT item (bundled OQ closure) is an integrator-execution note, not an
unrepairable-content defect — it does not gate `ready`.

## Suggested resolution

`ready`. Notes for the integrator:

1. **Surgical OQ closure (load-bearing).** When closing the recommended OQ, strike ONLY the
   `apply-nonlinear-pencil-mutation-rotation-lowering-verifier-audit-followup` clause from the
   four-slug line at `scaffolding/open-questions.md:327`. Do NOT close the whole line — the other
   three slugs (`deflate-composition-...`, `gram-fold-specialization-...`,
   `orthogonalize-composition-...`) are separate batch-6 audits that may still be open (several
   ran this same cycle). Rewrite the line to drop just this clause, preserving the remaining
   three.
2. **Apply the `verified_against:` block as-is.** It is a purely-additive YAML provenance block
   appended at end of `book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md` (no surface
   edit, no status change). The inner fence is rendered as `~~~` triple-tilde with an explicit
   instruction (CYCLE.md:238) to emit triple-backticks in the actual file — standard nested-fence
   convention.

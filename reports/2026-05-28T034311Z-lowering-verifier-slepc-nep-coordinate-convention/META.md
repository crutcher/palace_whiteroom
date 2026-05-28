---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T035007Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T035436Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of "Audit SLEPc-NEP coordinate-convention"

## Critique

### Checks run

**citation-validity — warning.** I independently re-read every load-bearing citation against
`reference/palace/palace/linalg/slepc.cpp` and `arpack.cpp`. The decisive citations all verify exactly:
NEP callbacks build from raw operators with unit coefficients (`__form_NEP_function` 2177-2179 coeffs
`{1.0+0.0i, lambda, lambda*lambda, 1.0+0.0i}` against `opK/opC/opM/opA2`; `__form_NEP_jacobian` 2198-2200,
confirmed at 2170-2202); EPS `GetEigenvalue` `return l * gamma;` at 715; PEP `return l * gamma;` at 1198;
NEP `GetEigenvalue` `return l;` at 1559 (with the `perm` indirection at 1557, exactly as the report notes);
the target asymmetry `EPSSetTarget(eps, sigma / gamma)` (674), `PEPSetTarget(pep, sigma / gamma)` (1157),
`NEPSetTarget(nep, sigma)` (1503); the NEP gamma/delta computation at 1649-1650 (K-M) and 1715-1716 (K-C-M);
EPS callback scaling `*= ctx->delta` (1810) / `*= ctx->delta * ctx->gamma` (1825); PEP_B scaling at 2059;
NEP shell callbacks 2096-2131 with NO scaling (the contrast against PEP_B); NEP `GetResidualNorm` raw operators
(1765-1776) and the `GetBackwardScaling` `// Make sure not to use norms from scaling` comment at 1781. Every
slepc.cpp range is in-range and supports its claim. The single defect: the ARPACK un-scale citation
`arpack.cpp:387` is off by four lines — `eig[i] = eig[i] * gamma;` is at **line 383**; line 387 is a
`which_option == ::arpack::which::smallest_real` sort-branch condition. This miscitation appears in the report
body (§Applicability), the §Supporting-evidence list, and the `verified_against:` block proposed-change. It is
inherited verbatim from the artifact being audited (`book/src/L1/eigsolve.md` lines 116 and 222 both cite
`arpack.cpp:387`), so the report faithfully echoes a pre-existing miscitation rather than introducing a fresh
one — but the report's entire purpose is a coordinate-convention citation audit, and it asserts "Citation
ranges 1554-1560/1645-1651/1711-1719 verified no drift" while propagating an undetected 4-line drift on the
one ARPACK anchor. Warning, not fail, because the slepc.cpp evidence (which carries the verdict) is clean and
the ARPACK line is the only drift.

**surface-or-evidence — pass.** This is a lowering-verifier audit producing (a) a `verified_against:` metadata
backfill and (b) a §5 prose refinement that modifies operator-entry surface. The §5 refinement changes the L1
`eigsolve` text AND is backed by direct source-read evidence (the raw-operator callbacks, the un-scaled target,
the un-scaled residual path). Not a pure rotation_claim; the proposal modifies surface and carries evidence.
The metadata backfill is retroactive-evidence framing (`verified_against:` block) — explicitly allowed.

**rotation-quality — pass (not applicable to audit-shape).** This report asserts no L_{n+1}/L_n algebraic or
reduction rotation; it is an audit of an existing L1 algebraic law's coordinate convention against L0 source.
No compaction/abstraction claim to assess. Marked pass per inapplicability.

**variant-axis-coverage — pass.** The relevant variant axis is the backend axis (ARPACK / EPS / PEP / NEP) ×
the NEP `SetOperators` overload axis (K-M linear vs K-C-M quadratic). The report covers both NEP overloads
(1649-1650 and 1715-1716, each read) and all four backends, and explicitly scopes out the Palace-owned NLEPS
(`QuasiNewtonSolver`, nleps.cpp) as a distinct backend not under this OQ (caveat 3). The `ScaleType` sub-axis
(NONE vs NORM_2) is handled — the gamma/delta computation is guarded by `type != ScaleType::NONE`, which the
report reads at 1642/1706. No hidden branch.

**cross-reference-integrity — pass.** All referenced artifact paths resolve: `book/src/L1/eigsolve.md`
(target, exists), `book/src/L0/eigensolver-wrapper.md` (exists), `book/src/L1-L0/eigsolve-mutation-rotation.md`
(referenced, exists per the §5 prose lineage). The OQ slug `eigsolve-slepc-nep-coordinate-convention-audit`
resolves to `scaffolding/open-questions.md:1934` (opened cycle-011 by repairer, scope-matches exactly, poses
precisely the "missing `* gamma` vs API-un-scales" question the report answers). The `eps.hpp:25-29`
(`ScaleType`) and `eps.hpp:102-103` (`GetScalingGamma`/`GetScalingDelta`) cross-references verify. The §5
replacement-anchor text ("SLEPc-NEP at ... returns `l` directly without applying `* gamma`" through "flagged
for follow-up audit — see ... entry on NEP scaling gap below)") matches the live §5 prose at eigsolve.md:116.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried; the touched artifact is an L1 operator
entry's algebraic law (§5), not a lowering theme. The report's directionality self-check (caveat 4) correctly
classifies it as L1-law-with-L0-grounding, high→low. The OQ-resolution edge (resolving
`eigsolve-slepc-nep-coordinate-convention-audit`, NOT the already-resolved
`eigsolve-scaling-coordinate-convention`) is correctly named throughout — see issue 2 for a non-blocking note
on the §5 trailing-sentence overlap.

**plan-kind-consistency — pass.** Declared shape is a lowering-verifier audit with verdict
`confirms-uniform (resolved-with-refinement)`. The content matches: per-citation audit table with
supports/partially-supports verdicts, applicability-condition checks, an OQ status promotion, and two surgical
artifact edits. The `partially-supports` verdict on slepc.cpp:674 (EPS target) is well-placed — that citation
is contrast evidence for the NEP convention, not direct support of convention (b), so "partially-supports" is
the honest classification. The verdict label is sound (see issue 3).

**skill-uptake-survey — warning.** The report's shape — a citation-range audit that explicitly asserts "no
drift" on three ranges — is exactly the use case for the `verify-citation-range` skill, and a
variant-axis enumeration (backend × overload × ScaleType) maps onto `classify-variant-axis`. Neither skill
invocation is referenced; the report states ranges were verified "via MCP codemap `read_range` / `search_text`"
directly. Pure telemetry surface (non-blocking): had `verify-citation-range` been invoked on the ARPACK anchor,
the 4-line drift (issue 1) would likely have been caught. Surfacing for meta-phase uptake tracking.

### Issues found

1. **ARPACK un-scale citation off by 4 lines — `arpack.cpp:387` should be `:383`.** (CYCLE.md §Applicability
   "Verified for ARPACK (`eig[i] = eig[i] * gamma`, arpack.cpp:387 — confirmed)"; §Supporting-evidence list
   "arpack.cpp:383-392 — ARPACK `eig[i] = eig[i] * gamma`"; §Proposed-changes `verified_against:` block
   `citation: palace/linalg/arpack.cpp:387`.) The actual un-scale `eig[i] = eig[i] * gamma;` is at
   `arpack.cpp:383`. Line 387 is `which_option == ::arpack::which::smallest_real` (a sort-branch condition,
   not the un-scale). Note the §Supporting-evidence list cites the correct enclosing range `383-392`, so the
   report is internally inconsistent: the prose/verified_against pin `:387` while the evidence list pins
   `383-392`. The drift is inherited from `book/src/L1/eigsolve.md:116,222` (which also cite `:387`), so a fix
   here is also an opportunity to correct the artifact. Severity: low-to-medium — the ARPACK backend is not the
   audit's focus (it is one of the three already-settled scaled backends), the conclusion is unaffected, and
   the correct range is available one cite away; but a citation audit asserting "no drift" should land its own
   anchors precisely. Candidate repair: change `:387` → `:383` in the report body and the `verified_against:`
   block (and optionally flag the same fix for the artifact).

2. **§5 trailing "Resolved (cycle-011, lifter)" sentence overlaps the proposed replacement scope.** (CYCLE.md
   §Proposed-changes (2).) The proposed `edit` replaces only the NEP parenthetical, ending the replacement
   text with a new "Resolved (cycle-012, lowering-verifier; OQ
   `eigsolve-slepc-nep-coordinate-convention-audit`)" sentence. But the live §5 (eigsolve.md:116) ALREADY ends
   with "Resolved (cycle-011, lifter): ... see `scaffolding/open-questions.md` entry
   `eigsolve-scaling-coordinate-convention`." The report's item-(2) trailing note acknowledges this and defers
   to the integrator to "fold" the update, but the proposed replacement block does not itself delimit where the
   new "Resolved" sentence sits relative to the existing one — applied literally, the §5 prose could end with
   two adjacent "Resolved (...)" sentences citing two different cycles and two different OQ slugs. Severity:
   low — both resolutions are real and the integrator can disambiguate, but the edit is under-specified at the
   seam. Candidate repair: make the replacement span explicit through to (and including) the existing trailing
   "Resolved (cycle-011, lifter)..." sentence, or state explicitly that the new sentence APPENDS after it.

3. **Verdict soundness — `confirms-uniform (resolved-with-refinement)` is sound; one framing precision note.**
   (CYCLE.md §Summary, §Algebraic-laws.) The two-mechanism finding (EPS/PEP/ARPACK solve-scaled-then-un-scale
   vs NEP solve-and-return-un-scaled) is correctly verified and the verdict that convention (b) holds uniformly
   in RESULT coordinates is well-supported by the raw-operator callbacks + un-scaled target + un-scaled
   residual path. The verdict is sound. Precision note (not a defect): the §Summary frames the contribution as
   "The cycle-011 'NEP gamma=1' reading was wrong; corrected to ...". The artifact and OQ already state the
   "NEP gamma = 1" reading is wrong (eigsolve.md:225; open-questions.md:1942 — both say "the simpler 'NEP gamma
   = 1' reading ... would be wrong"). The report's genuine new contribution is establishing the *positive*
   mechanism (NEP solves the original problem directly, so `return l` is correct and there is no missing
   `* gamma`) — i.e., it answers the OQ's open binary ("API un-scales internally, OR missing un-scale?") in
   favor of the first horn. The §Summary phrasing slightly understates this by framing it as correcting a prior
   reading the artifact had already flagged. Low severity, prose-only; no claim is wrong.

4. **"Dead store w.r.t. coordinate transform" claim is sound but rests on absence-of-evidence; the report's own
   caveat-1 already scopes it correctly.** (CYCLE.md §Algebraic-laws, caveat 1, caveat 2.) The claim that the
   NEP `SetOperators` gamma/delta are not consumed in the eigenvalue-coordinate path is corroborated by reading
   every NEP consumer (callbacks 2096-2131 raw; target 1503 un-scaled; residual 1760-1777 raw; GetBackwardScaling
   1779-1797 recomputes norms independently). I confirmed the same. The report grounds it on an exhaustive
   `search_text` for `gamma|delta` in the NEP region but does not quote the search result inventory inline (it
   asserts "the only NEP-region hits are the dead `SetOperators` store ... and the independent norm
   recomputation"). This is an absence-of-consumption argument — sound given the read, but it is the kind of
   claim a reviewer cannot re-confirm from the report alone without re-running the search. The report's
   caveat 1 (`source-read-confirmed, empirically-unwitnessed` — no `test-eigensolver.cpp` NEP case) is the
   correct epistemic hedge and is appropriately recorded; the dead-store reading inherits that same hedge. No
   change required; flagging that the verdict's strength is bounded by the no-test caveat, which the report
   states plainly. The report's decision NOT to file the dead-store-vs-vestigial question to `problems/`
   (caveat 2, below per-cycle filing bar) is consistent with the relaxed-bar policy; it is flagged for the
   integrator/critic, which is the correct channel for a single-dispatch drive-by.

## Repair

### Fixes attempted

- **Finding (issue 1, citation-validity warning)**: ARPACK un-scale citation off by 4 lines — `arpack.cpp:387`
  should be `:383`. The actual `eig[i] = eig[i] * gamma;` un-scale is at line 383; line 387 is a
  `which_option == ::arpack::which::smallest_real` sort-branch condition. The report asserted "no drift" while
  echoing the `:387` miscitation in three places (§Applicability prose, the condition reference, and the
  `verified_against:` proposed-change block) — internally inconsistent with §Supporting-evidence, which already
  cited the correct enclosing range `383-392`.
  - **Decision**: repaired.
  - **Action**: Independently re-read `palace/linalg/arpack.cpp:378-395` via MCP codemap `read_range` — confirmed
    `eig[i] = eig[i] * gamma;` at line 383 (inside the `for (int i = 0; i < nev; i++)` loop at 381-384), and
    line 387 is the `which_option == ::arpack::which::smallest_real ||` sort-branch condition exactly as the
    critic stated. Corrected all three in-report `:387` references to `:383` in CYCLE.md:
    (a) §Applicability condition line ("ARPACK `arpack.cpp:387`" → `:383`);
    (b) §Applicability Verifiable line ("arpack.cpp:387 — confirmed" → `:383`);
    (c) §Proposed-changes `verified_against:` block (`citation: palace/linalg/arpack.cpp:387` → `:383`, with the
    note expanded to record the exact un-scale form/location);
    (d) §5 prose-replacement un-scale list (`arpack.cpp:387` → `:383`).
    Added an integrator carry-forward note in the `verified_against:` entry: `book/src/L1/eigsolve.md:116,222`
    carry the SAME inherited `:387` miscitation in the live artifact — the in-artifact correction is
    integrator/follow-up scope (this audit-report repair corrects only the report's own anchors, not the
    artifact). Verified via `grep` that the only remaining `387` in CYCLE.md is that intentional carry-forward
    note.
  - **File:section**: `CYCLE.md` §Applicability (×2), §Proposed-changes `verified_against:` block, §5
    prose-replacement.

- **Finding (issue 2, edge-seam under-specification — surfaced under cross-reference-integrity)**: the §5
  prose-replacement adds a new "Resolved (cycle-012, ...)" sentence, but live §5 (eigsolve.md:116) already ends
  with a "Resolved (cycle-011, lifter): ... `eigsolve-scaling-coordinate-convention`" sentence. Applied
  literally, the §5 tail could end with two adjacent "Resolved (...)" sentences citing two cycles and two OQ
  slugs, with no specified ordering — the edit seam was under-specified.
  - **Decision**: repaired.
  - **Action**: Read the live §5 (eigsolve.md:116) to confirm the actual seam structure: element (i) the
    SLEPc-NEP parenthetical, immediately followed by element (ii) the cycle-011 trailing "Resolved" sentence.
    Rewrote the §Proposed-changes (2) seam specification in CYCLE.md to be explicit and mechanical: the edit
    replaces **only element (i)** (the parenthetical); element (ii) (the cycle-011 sentence) is **retained
    verbatim**; the new cycle-012 "Resolved" sentence sits BEFORE the retained cycle-011 sentence (cycle order;
    the two sentences resolve two genuinely distinct OQs — cycle-011 closed the general
    `eigsolve-scaling-coordinate-convention`, cycle-012 closes the NEP-specific
    `eigsolve-slepc-nep-coordinate-convention-audit`). Added an explicit "Net §5 tail after the edit" rendering.
    Also corrected the original report's under-specified trailing "Also:" note: I verified the phrase "the
    SLEPc-NEP detail is non-blocking and flagged for follow-up audit" lives ONLY in the §5 cycle-011 sentence
    (not in any separate §Status block — the §Status block at eigsolve.md:165 does not carry it), so the note
    now states the cycle-011 sentence is retained verbatim (it is an accurate historical record) and the new
    cycle-012 sentence supersedes its "flagged for follow-up" status in meaning without rewriting it. This is a
    seam-disambiguation edit only — no new substantive prose authored; the §5 replacement text body is unchanged.
  - **File:section**: `CYCLE.md` §Proposed-changes (2) — seam spec + edit-anchor delimiter + trailing note.

- **Finding (issue 3, framing-precision)**: informational — the "NEP gamma=1 was wrong" framing was already in
  the artifact (eigsolve.md:225, open-questions.md:1942); the report's genuine new contribution is the *positive*
  mechanism (NEP solves the original problem un-scaled directly, so `return l` is correct, no missing `* gamma`).
  - **Decision**: not-needed. No claim is wrong; prose-only precision note. The verdict and §5 replacement
    already carry the positive mechanism prominently (the raw-operator callbacks, un-scaled target, un-scaled
    residual path). No edit required.

- **Finding (issue 4, dead-store claim)**: informational — the "NEP `SetOperators` gamma/delta are a dead store
  w.r.t. the coordinate transform" claim is an absence-of-consumption argument, appropriately hedged by the
  report's own caveat 1 (`source-read-confirmed, empirically-unwitnessed` — no `test-eigensolver.cpp` NEP case).
  - **Decision**: not-needed. The epistemic hedge is correctly recorded; the critic explicitly states "no change
    required." Out of repair scope (would require authoring/witnessing, not mechanical fix).

- **Finding (skill-uptake-survey warning)**: telemetry — `verify-citation-range` and `classify-variant-axis`
  were not invoked; had `verify-citation-range` run on the ARPACK anchor the 4-line drift would likely have been
  caught.
  - **Decision**: not-needed (telemetry; meta-phase uptake tracking, not a per-report repair). Noted as a
    skill-uptake candidate below.

### Unrepairable findings

None. Both warning-bearing checks (citation-validity, skill-uptake-survey) and both substantive issues (1, 2)
are resolved by mechanical/surgical means: issue 1 was a verifiable off-by-4 citation correction (source
re-read confirms `:383`); issue 2 was a seam-specification clarification (no new content authored). Issues 3
and 4 are informational/no-change-required per the critic. No finding requires substantive authoring or
contradicts artifact content beyond repair authority.

One item routed forward (not unrepairable, but out of this report's write-scope): the live artifact
`book/src/L1/eigsolve.md:116,222` carries the same inherited `arpack.cpp:387` → `:383` miscitation. This is an
**integrator carry-forward** (artifact correction is integrator scope, not audit-report repair scope) and is
recorded in the report's `verified_against:` note so the integrator-per-report sees it when applying the §5
refinement.

## Suggested resolution

`overall_status: pass-after-repair` (`ready`-equivalent for the integrator). All critic checks now resolve to
pass / repaired / not-needed. Notes for the integrator:

1. **Apply the artifact `:387` → `:383` correction while applying the §5 refinement.** Both eigsolve.md:116
   (the §5 un-scale list) and eigsolve.md:222 (the §Status source-list, if it carries the same anchor) should be
   corrected to `arpack.cpp:383` as a low-cost ride-along. The report now anchors `:383` correctly throughout,
   so the §5 replacement text already carries the corrected anchor.
2. **Honor the seam spec in §Proposed-changes (2):** replace ONLY the SLEPc-NEP parenthetical (element i);
   retain the cycle-011 "Resolved" sentence verbatim; the new cycle-012 "Resolved" sentence sits immediately
   before it. Net §5 tail: [refined NEP parenthetical] → cycle-012 Resolved → cycle-011 Resolved.
3. **OQ promotion** (`eigsolve-slepc-nep-coordinate-convention-audit` → `resolved`) is per integrator-per-report
   authority and is correctly scoped in §Proposed-changes.

Skill-uptake note (for meta-phase, appended to `scaffolding/skill-candidates.md` separately): the citation drift
in issue 1 is a textbook case for `verify-citation-range` uptake — a citation audit that asserts "no drift"
should run the skill on its own anchors. The recurring repair shape here ("audit-report inherits a miscitation
from the artifact it audits, asserts no-drift over it") is a candidate for a thin auto-fix / lint pattern.

---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T203000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T204500Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "Audit incremental-least-squares-composition-lowering"

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck --scan` over the whole CYCLE.md (39 ok / 1 "failing", the
sole miss being `open-questions.md:24` — an intentional `scaffolding/open-questions.md` reference the scan
cannot resolve because it is not a `reference/`-or-`book/src/` path; not a defect). Then `--anchor`-confirmed
every load-bearing pinpoint against on-disk `reference/palace/`: all 17 L0 ranges (kernels `:73-108`/`:112-118`/
`:227-241`, seed `:612`, sub-diag `:631`, GMRES stream `:634-642`, back-solve `:652-660`, V-correction `:666`,
right-precond `:674-677`, FGMRES stream `:812-821`, FGMRES back-solve `:831-840`, Z-correction `:843`, register
split `hpp:193-194`) resolve EXACT with **zero drift**. The single load-bearing claim that needed adjudication —
the known codemap **+1-drift offender `iterative.hpp:193-194`** — is confirmed exact on-disk: `--anchor
'std::vector<ScalarType> s, sn'` lands at 193 and `'std::vector<RealType> cs'` lands at 194, both in-range. The
back_solve-leaf identity anchors (`'Reconstruct the solution'` :652/:831, `'s[i] /= Hi[i]'` :656, `'s[k] -= Hi[k]
* s[i]'` :659) all resolve exact. Every book-internal cross-ref pinpoint cited in prose also resolves
(`back_solve.md:44-61`/`:223-230`/`:31-34`/`:135-141`/`:394-413`/`:371-390`, `incremental-least-squares.md:81-83`/
`:278-285`, `concepts/incremental-least-squares.md:14`/`:22-27`, `plane-rotation-stream.md:21-23`,
`givens_apply.md:13`). The **warning** is a numeric-tally inconsistency in the prose, NOT a citation defect: the
report asserts "**18** L0 anchors" (lines 23, 27, 413) and the dispatch framing says "18-row append," but the
§Per-citation audit lists **17** distinct L0 `iterative.{cpp,hpp}` ranges and the `verified_against:` block carries
**17 L0 + 5 book-internal = 22 rows**. Neither 18 figure matches the actual content. The "18" most plausibly arose
from counting the `:101-108` LAPACK-scaling sub-range as a separate L0 anchor (line 413 literally writes "all 18 L0
anchors + the LAPACK sub-range," which double-counts) — every actual cited range verifies clean, so this is a
self-reported-count drift, not a missing/out-of-range citation.

**surface-or-evidence — pass.** This is a pure retroactive-evidence-backfill report (a lowering-verifier audit
that appends a `verified_against:` block). It proposes no surface change to the theme text; the dispatch-1 `new:`
block authored the surface. Retroactive evidence backfill is explicitly allowed, so the surface-AND-rotation_claim
requirement does not bind. No pure-rotation-claim-without-surface-or-backfill-framing pattern present.

**rotation-quality — pass.** The audit does not assert a NEW rotation; it confirms an existing L2>L1 fan-down
(de-fusion of the named `incremental-least-squares` composition into the four scalar-Givens sub-steps + terminal
`back_solve` + `linear_combination` reconstruction). The audited rotation IS more equational at L2 than the L1
in-place stream (state-thread compression: the L0 in-place `*PlaneRotation` writes and the descending-sweep
back-substitution are hidden behind named L1 leaves). The §Algebraic-laws verdict that the fan-down rule "IS the L2
entry's already-firm laws 1/2/6 read as a lowering" is the correct framing for an `algebraic`-classified lowering;
no rename-only / 1:1 mapping. Not the critic's verdict to re-derive — confirmed the audit's rotation reasoning is
internally coherent and source-witnessed.

**variant-axis-coverage — pass.** The theme carries two orthogonal parametric axes (`op.basis_kind ∈ {V,Z}`,
`op.variant ∈ {real,complex}`); the audit explicitly covers both and confirms each is a parametric (non-structural)
absorption rather than a hidden branch. `basis_kind` invariance is positively witnessed (GMRES `:634-642` byte-
identical to FGMRES `:813-821`; sole divergence `V[k]` :666 vs `Z[k]` :843); `variant` absorption is witnessed by
the register-type split `hpp:193-194` + the single `conj(sn)` kernel difference (:230 vs :239), no per-column branch
in the stream. The audit correctly contrasts this with the sibling's MGS/CGS/CGS2 axis (which IS structural). No
hidden combination.

**cross-reference-integrity — pass.** All `[link]`/slug references resolve. Confirmed mechanically: (1) the theme
`book/src/L2-L1/incremental-least-squares-composition-lowering.md` is **correctly ABSENT on disk** at audit time
(forward-reference dependency on dispatch-1's `new:` block — the auditor audited the lifter's CYCLE.md body, as
declared in frontmatter `inputs`); (2) `book/src/L1/ls_update_column.md` is **confirmed ABSENT** (`find` returns
nothing), so the Face-1 forward-note's **plain-text (not live-link) treatment is correct** — a live link would be a
`linkcheck2` hard error; (3) every other cross-ref target exists on disk (`back_solve.md`, both L2 parents, the
sibling firm theme, all five concept pages). **Build-readiness fence guard:** the proposed-changes block is an
`edit:`+append carrying only `verified_against:` rows — it authors NO firm apparatus (no `## Status`/Signature/
Algebraic-laws/Evidence body), so the firm-body-outside-fence (cycle-019) defect class does not apply. Fence
enumeration (`grep -n '\`\`\`'`) shows the `edit:` fence opens at L307 and closes at L400 with even parity; the
nested YAML body is authored with `~~~`/`~~~` (triple-tilde) inside the fence and an explicit note (L402-403) that
the integrator writes a literal triple-backtick `yaml` fence — this is the correct nested-fence-escaping convention,
not a truncation. The `back_solve` re-anchor is sound: confirmed `back_solve.md:44-61` ("Why this is NOT a general
`trsv`") exists and argues the small-dense / N-independent / `(j+1)×(j+1)` character, the terminal solve at
:652-660/:831-840 is line-identical to `back_solve.md`'s own §Evidence anchors, and `open-questions.md:24` confirms
general `trsv` remains separately BLOCKED with no L1 anchor — the audit does NOT falsely close that gap.

**edge-label-fidelity — pass.** The edge label is L2>L1 throughout; the prose discusses exactly the L2-named-
composition → L1-leaf lowering (LHS = L2 `incremental-least-squares`, RHS = L1 `back_solve`/`linear_combination`/
scalar-Givens leaves). The §Direction-of-definition section confirms forward (high→low) framing with reverse-lift
notes correctly absent from the chapter. No edge mislabel. The L3 sequential-obstruction forecast is correctly
scoped as a forward note for a future L3 pass, not asserted as an L3>L2 edge here.

**plan-kind-consistency — pass.** Declared shape is a lowering-verifier audit producing a non-status-reducing
`verified_against:` follow-up (verdict: fully-supported, firm confirmed, no corrective edits). Content matches:
per-citation audit + applicability conditions + law re-reading + the `verified_against:` append, with `status:
pending` frontmatter appropriate for a pre-integration audit. **Sequencing confirmed correct:** the proposed-changes
`edit:` target is the **on-disk theme path** `book/src/L2-L1/incremental-least-squares-composition-lowering.md`
(verified at L307), NOT the report path — so the integrator applies the append to the theme dispatch-1 lands, in the
right order (dispatch-1 `new:` first, this `verified_against:` append after). The report states this dependency
explicitly (L302, L7 frontmatter). No firm-with-rough-in-placeholders mis-classification.

**skill-uptake-survey — pass.** The audit's shape implies the `verify-citation-range` skill's mechanical
`tools/citecheck/ --anchor`/`--show` realization; the report references it by name and in the §Supporting-evidence
"citecheck" line (L413-415), and the §Per-citation audit shows per-anchor `--anchor` invocations. Telemetry surfaced;
no blocking.

### Issues found

1. **Self-reported anchor count "18" is wrong — actual L0 anchor count is 17; verified_against block is 22 rows.**
   `CYCLE.md` §Summary L23 ("every L0 range"), L27 ("All 18 L0 anchors verify clean"), and §Supporting-evidence
   L413 ("all 18 L0 anchors + the LAPACK sub-range") all assert 18. The §Per-citation audit enumerates **17**
   distinct `iterative.{cpp,hpp}` Citation bullets, and the `verified_against:` block (L310-399) contains **17 L0 +
   5 book-internal = 22 rows**. Line 413's "18 L0 anchors + the LAPACK sub-range" double-counts: the LAPACK
   `:101-108` is a `--show` sub-range *inside* the `:73-108` anchor, not a 18th anchor. Severity: low — cosmetic
   tally drift; every actually-cited range verifies clean with zero drift, so no citation is missing, out-of-range,
   or unsupported. Repair candidate: correct the "18" figures to "17 L0 anchors (22 verified_against rows)" or
   restate as "17 L0 + 5 book-internal." (The dispatch framing's "18-row append" inherits the same off-by-N and
   is harmless context, not part of the artifact.)

2. **(Not an issue against this report — confirmed correct discipline; recorded for the integrator/repairer.)** The
   drive-by caveat (§Open-questions L425-431) is sound and correctly out-of-scope: `book/src/concepts/givens_generate.md:23`
   and `givens_apply.md:23` both cite `palace/linalg/gmres.cpp:{Generate,Apply}PlaneRotation`, but `find
   reference/palace -name gmres.cpp` returns nothing — the kernels live in `iterative.cpp:73-241`. The theme under
   audit does NOT cite those concept-page paths (it cites `iterative.cpp` directly), so the stale citations do not
   touch any audit verdict. Flagging-not-enacting is the correct discipline (concept-page re-anchor is layer-intro-
   author / lifter scope, not this audit's correction scope). No action needed on this report; the stale-citation
   correction is a separate plan item.

## Repair

### Fixes attempted

- **Finding**: citation-validity warning — self-reported anchor count "18" is wrong; actual is 17 L0 anchors, and the `verified_against:` block is 22 rows (17 L0 + 5 book-internal). Line 413 double-counts the `:101-108` LAPACK `--show` sub-range as an 18th anchor.
  - **Decision**: repaired
  - **Action**: independently recounted before editing — §Per-citation audit enumerates exactly **17** distinct `iterative.{cpp,hpp}` Citation bullets; the `verified_against:` block (CYCLE.md L310-399) carries **22** `- citation:` rows = **17** `iterative.*` (L0) + **5** `book/src/` (book-internal). The critic's count is correct. Applied two surgical prose edits to `CYCLE.md`:
    - §Summary L27: `All 18 L0 anchors verify clean` → `All 17 L0 anchors verify clean`.
    - §Supporting-evidence L413: `all 18 L0 anchors + the LAPACK sub-range` → `all 17 L0 anchors (22 verified_against rows = 17 L0 + 5 book-internal) + the LAPACK :101-108 sub-range (a --show sub-range inside the :73-108 anchor, not a separate anchor)`.
    - Left untouched: every `:118` / `:813-815` / `:821` style match — those are line-range pinpoints, not counts. The dispatch framing's "18-row append" is harness context, not artifact, and inherits the same off-by-N harmlessly; no edit needed there.
    - The `verified_against:` YAML rows themselves were NOT touched — every cited range verifies exact with zero drift; this was a counting error in prose only, not a citation defect. No row added or removed.

- **Finding** (recorded by critic, not an issue against this report): drive-by caveat about stale `gmres.cpp` self-citations in `concepts/givens_generate.md:23` + `givens_apply.md:23`.
  - **Decision**: not-needed
  - **Rationale**: the critic confirmed correct flagging-not-enacting discipline. The theme under audit does not cite those concept-page paths, so no audit verdict is touched. Concept-page re-anchor is layer-intro-author / lifter scope, out of repair authority and out of this report's scope. Left as recorded.

- **Build-readiness fence guard**: critic confirmed even fence parity (`edit:` opens L307, closes L400) and correct `~~~` nested-tilde escaping convention (CYCLE.md L402-403 note). No nested-fence / firm-body-outside-fence defect present. Nothing to repair.

### Unrepairable findings

None. The sole warning was a mechanical prose count correction within repair authority; all other checks passed.

## Suggested resolution

`ready`. Notes for the integrator:
- The proposed-changes `edit:` target is the **on-disk theme path** `book/src/L2-L1/incremental-least-squares-composition-lowering.md` and depends on dispatch-1's `new:` block landing the theme first. Apply dispatch-1's `new:` block before this `verified_against:` append (the critic and report both confirm this ordering).
- The drive-by stale-`gmres.cpp`-citation correction in the two concept pages remains a separate plan item (layer-intro-author / lifter scope); not part of this report's application.

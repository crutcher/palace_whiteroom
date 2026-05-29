---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T18:34:00Z
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
repaired_at: 2026-05-29T18:16:08Z
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

# META: verification of "Re-anchor ksp_solve §Semantics materialise_iterate → firm L2 incremental-least-squares"

## Critique

### Checks run

**citation-validity — pass.** `python3 tools/citecheck/citecheck.py --scan` on this CYCLE.md returns `4 ok, 0 failing`, matching the report's claim. The four scanned refs are `book/src/L2/ksp_solve.md:123`, `:83`, `:63` (artifact-internal edit-site line references) and `iterative.cpp:666` (resolved to `reference/palace/palace/linalg/iterative.cpp`, 882 lines, in-bounds). No new L0 line-citation appears inside either `[new]` edit string — both edits add only book-internal relative links (`./incremental-least-squares.md`, plus the pre-existing `./orthogonalize.md`, `./krylov-step.md`, `../concepts/solve-monad.md`). The only `.cpp:NN` references in the report (line 93: `iterative.cpp:666` / `:843`) are discipline-note passthroughs quoting the *target* entry's own §Semantics, not new assertions against `reference/palace/`. No `--anchor` run is applicable — there is no new `path:lo-hi` pinpoint introduced by the edits.

**surface-or-evidence — pass.** This is a pure cite/cross-ref upgrade, not a refinement-shaped proposal: no operator/theme surface text is rewritten in a way that changes semantics. `ksp_solve` stays `firm`; signature, the four phases, predicate, and result extraction are untouched. The check is effectively no-op for this report shape, but I confirmed the §Semantics phase-3 `[new]` prose does not sneak in a semantic change: the added clause ("the `back_solve` output … the coordinate vector `y` reconstructed against the basis `V`/`Z`") draws its vocabulary verbatim from the firm target's own §Signature (`back_solve :: LsqState' -> { y, correction_basis }`, target line 83) and §Semantics (`correction_basis · y`, target line 131). It annotates provenance of the existing `K.V · K.y` correction; it does not alter ksp_solve's behaviour.

**rotation-quality — pass (not applicable).** No algebraic/structural rotation is asserted — this is a citation upgrade between two existing firm L2 entries, not an L_{n+1}→L_n re-expression. No renaming-only or 1:1 mapping is being claimed as a rotation.

**variant-axis-coverage — pass.** No variant-axis change. The §Dependencies parenthetical broadens "GMRES running-QR" → "GMRES/FGMRES running-QR" + adds the `Z·y` (FGMRES) arm alongside `V·y` (GMRES). I confirmed this is alignment, not a hidden new branch: the FGMRES arm is already in this file's solver-method axis and is the target entry's explicit `op.basis_kind = Z` axis (target §Status line 387, §Signature line 130). Both restart arms are named, none hidden.

**cross-reference-integrity — pass (LOAD-BEARING; the central check).** Verified end-to-end:
- Target `book/src/L2/incremental-least-squares.md` exists on-disk, `status: firm` (line 376: "`firm` — the composition is a `replay ▷ generate ▷ apply ▷ apply_rhs` pipeline…"), H1 `# incremental-least-squares` (line 1). The relative link `./incremental-least-squares.md` therefore resolves under linkcheck2.
- Edit-1 `[old]` (the §Dependencies line) is verbatim single-occurrence at `ksp_solve.md:123` (`grep -Fc` = 1); it is a backtick-only plain-text mention carrying the "queued" qualifier, NOT a live link → "not already-satisfied" confirmed.
- Edit-2 `[old]` (the §Semantics phase-3 line) is verbatim single-occurrence at `ksp_solve.md:83` (`grep -Fc` = 1); it currently links only `krylov-step` and `solve-monad`, with no `incremental-least-squares` reference → "not already-satisfied" confirmed.
- **Bidirectionality confirmed.** The target back-links to both upgraded sites: §Consumers (target lines 329–332: "`ksp_solve` … §Semantics phase-3 `materialise_iterate` folds the last partial restart cycle's correction `V·y` / `Z·y` (this composition's back-solve output) …"), §Status (target lines 381–382: "[`ksp_solve`](./ksp_solve.md) `materialise_iterate` consumes"), and §Evidence (target line 507: "the outer-driver consumer; §Semantics phase-3"). After this report the cross-reference is live in both directions.
- No new chapters → SUMMARY.md wiring unaffected.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried; both entries are same-layer (L2) and the cross-reference is a consumer→producer (`ksp_solve` driver → `incremental-least-squares` composition) link, not a lowering edge. The prose discusses exactly that relationship.

**plan-kind-consistency — pass.** Declared shape is a lifter cite/cross-ref upgrade ("pure cite/cross-ref upgrade"); content matches — two surgical `edit:` blocks, no status-line change, no new claims. Consistent with the `upgrade-plain-text-ref-to-live-link-when-target-on-disk` situation and the lifter role's "re-anchor a citation" / "firm up the vocabulary" scope. No firm-operator-with-placeholder mis-classification (nothing is being firmed; both ends were already firm).

**skill-uptake-survey — pass.** The report explicitly references the relevant skill (`upgrade-plain-text-ref-to-live-link-when-target-on-disk`, cycle-024) and the governing convention (`rough-in-forward-reference-must-be-plain-text-not-live-link`) plus the `lifter-scope-content-correction-boundary` allowance for the "queued"-drop. Skill provenance is surfaced.

### Issues found

No blocking issues. The two surgical edits are verified verbatim/single-occurrence, the target is firm-on-disk, the link resolves, and the cross-reference is bidirectional. Minor observations (all non-blocking, none alter the upgrade's correctness):

1. **`--scan` characterization slightly undercounts** — `reports/<id>/CYCLE.md` §Summary / §Discipline-notes (line 102) and §OQ-disposition frame the scan as "only incidental passthrough `iterative.cpp` ranges in the quoted prose." The scan actually bounds-checks 4 refs: the `iterative.cpp:666` passthrough AND three artifact-internal `ksp_solve.md:123 / :83 / :63` line references the report itself cites. All 4 are `ok`/in-bounds, so the result is unaffected — this is a description nicety, not an error. Severity: trivial.

2. **`iterative.cpp:843` not picked up by `--scan`** — the §Discipline-notes line 93 cites `iterative.cpp:666` / `:843`; only `:666` was enumerated by the scanner (the bare `:843` suffix form was not detected as a standalone citation). Both are passthrough quotes from the firm target entry, not new claims, and the sibling `iterative.cpp:666` resolved against an 882-line file (so `:843` is in-bounds). Severity: trivial; no action needed for this report's correctness.

3. **Pre-existing staleness in the target, out of scope** — `book/src/L2/incremental-least-squares.md:13` still self-describes as "the queued second **named-composition** motif" despite the entry being `firm` (line 376). This report correctly drops the "queued" qualifier on the *consumer* side (`ksp_solve.md:123`), but the symmetric staleness on the *producer* side is untouched. This is outside the report's declared scope (it touches only `ksp_solve.md`) and is a candidate for a future lifter/lowering-verifier pass on the target entry. Severity: minor; not this report's defect. Flagging as a drive-by observation for the planner, not a repair item here.

### OQ disposition assessment

The report closes OQ `l2-ksp-solve-materialise-iterate-incremental-least-squares-cite-tightening`. **Justified.** The OQ (`scaffolding/open-questions.md:618–621`, opened cycle-021) is described as a "citation-tightening nicety on the now-firm `L2/ksp_solve` … gated on the `incremental-least-squares` L2 stub firming"; it was marked NOW-ACTIONABLE (`:910`) and echoed in `integrator-signals.md:45` once the target firmed (cycle-026). The gate is satisfied (target `status: firm`), and the report upgrades the only two link-bearing reference sites. The OQ has no residual sub-parts. The report's claim that the line-63 signature comment carries no slug and needs no change is correct (verified: it is the inline `-- fold restart-cycle correction into s.x` comment, no `incremental-least-squares` token). No residual close-blocker.

## Repair

All 8 critic checks graded `pass`. The critic surfaced three non-blocking observations (two trivial scan-characterization niceties, one out-of-scope drive-by). None requires a mechanical repair to this report's correctness; the cite/cross-ref upgrade is verified verbatim/single-occurrence, bidirectional, and target-firm-on-disk. One stale frontmatter pointer was corrected.

### Fixes attempted

- **Finding**: META.md frontmatter `verifies: ../REPORT.md` — stale pointer (the per-dispatch report file was renamed `REPORT.md` → `CYCLE.md` at cycle-004; this dir contains only `CYCLE.md`).
  - **Decision**: repaired.
  - **Action**: rewrote `verifies: ../REPORT.md` → `verifies: ../CYCLE.md` in `reports/<id>/META.md` frontmatter. Mechanical broken-cross-reference-to-renamed-file fix (in repair scope).

- **Finding** (critic note 1): `--scan` characterization slightly undercounts — the report frames the scan as catching only the incidental `iterative.cpp` passthrough, but the scanner also bounds-checked 3 artifact-internal `ksp_solve.md:123 / :83 / :63` line references (all `ok`).
  - **Decision**: not-needed.
  - **Rationale**: critic graded this `trivial`; all 4 scanned refs are in-bounds so the result is unaffected. A description nicety, not an error — no edit improves correctness. (Rewording the §Summary scan prose would be cosmetic authoring, out of repair scope.)

- **Finding** (critic note 2): `iterative.cpp:843` passthrough quote not enumerated by `--scan` (the bare `:843` suffix form wasn't detected as a standalone citation).
  - **Decision**: not-needed.
  - **Rationale**: critic graded this `trivial`; `:843` is a passthrough quote from the firm target entry (not a new claim) and is in-bounds against the 882-line file its sibling `:666` resolved into. No correctness impact.

- **Finding** (critic note 3): pre-existing staleness in the TARGET entry — `book/src/L2/incremental-least-squares.md:13` still self-describes as "the queued second **named-composition** motif" despite the entry being `firm` (target line 376).
  - **Decision**: not-needed (out of scope; surfaced as OQ — see below).
  - **Rationale**: this report touches only `ksp_solve.md`; the symmetric "queued" staleness on the *producer* side is outside the declared scope. Repairing it would require editing the artifact (out of repairer write-authority) and is a content correction on a file this report does not touch. Surfaced as a follow-up OQ for a future lifter/lowering-verifier pass on the target entry, per the critic's drive-by flag.

### Unrepairable findings

None. No finding required substantive authoring or contradicted artifact content; the only actionable item was the mechanical `verifies:` pointer fix.

### Surfaced open question (drive-by, for the planner / a future lifter pass)

- **`incremental-least-squares.md:13` "queued" self-description is stale.** The firm (cycle-026) L2 `incremental-least-squares` entry still opens (`:13`) by calling itself "the queued second **named-composition** motif", contradicting its own `status: firm` (`:376`). This report correctly drops the symmetric "queued" qualifier on the *consumer* side (`ksp_solve.md:123`) but cannot touch the producer side (out of its declared scope). Suggested follow-up: a future `lifter` (or `lowering-verifier`) pass on `book/src/L2/incremental-least-squares.md` drops the "queued" self-description in `:13` (and audits the entry for other pre-firm-maturity self-references), bounded by the `lifter-scope-content-correction-boundary` allowance — exactly the same shape as the consumer-side correction this report applied. The integrator-per-report applying this report may append this to `scaffolding/open-questions.md` as an intake item (e.g. `l2-incremental-least-squares-self-description-still-says-queued-after-firming`).

## Suggested resolution

`overall_status: ready`. The cite/cross-ref upgrade is clean: target firm + on-disk, both `[old]` strings verbatim single-occurrence and not already-satisfied, bidirectional back-links confirmed, no sneaked-in semantic change, `ksp_solve` stays firm, OQ close justified. The only repair applied was the stale `verifies:` frontmatter pointer. The integrator can apply the two `edit:` blocks and close OQ `l2-ksp-solve-materialise-iterate-incremental-least-squares-cite-tightening` as the report specifies. The surfaced `incremental-least-squares.md:13` "queued" staleness is an independent intake item for the planner, not a blocker on this report.

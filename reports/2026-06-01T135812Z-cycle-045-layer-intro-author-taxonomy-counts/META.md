---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T141500Z
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
---

# META: verification of "L3>L2 index — erasure-scope taxonomy + consolidated count tally"

## Critique

### Checks run

**citation-validity — pass.** This is an index/taxonomy-prose report citing only book-internal slugs (no `path:lo-hi` L0 source ranges), so the `citecheck`/`--anchor` mechanical pass is a genuine no-op here (the report says so in OQ#4; the L0 anchors for the four substantive themes were self-verified by D1/D2 in their own dispatches). The one quotable internal pinpoint — the `apply_linop` §"Lowers to" claim at `L3/apply_linop.md:146` — I verified by reading: line 146 reads "L3 `apply_linop` lowers to L1 [`apply_linop`] directly — **no interposed L2 entry, no L3-L2 theme**", and the cycle-010 "CONFIRMED-NOT-NEEDED-WITH-CAVEAT" verdict appears verbatim at lines 30 and 144–160. No `verified_against:` block in this report, so that sub-check is inapplicable.

**surface-or-evidence — pass.** The report modifies surface (two `index.md` §Working-Notes bullets — the tally + the taxonomy note) and is framed as an index/overview refresh with the four-root erasure-scope taxonomy materialized from the c044/c045 OQs. This is layer-shell prose, not a refinement of an operator/theme requiring a rotation_claim; the count + taxonomy framing is appropriate and the surface edits carry their justification.

**rotation-quality — pass (not the report's own subject).** This report does not itself assert a new rotation; it catalogues the four substantive-theme rotations authored by D1/D2/c021/c044. I confirmed the taxonomy's rotation characterizations against the on-disk endpoints: `ksp-solve-outer-driver` (c021, substantive iteration-view erasure, confirmed in its §status), `eigsolve` L3 (partial-obstruction, opaque-library, body identity-in-form to L2 — confirmed `L3/eigsolve.md:19,28,30`), `chebyshev` L3 (partial-obstruction, inner k-recurrence numerical-stability-rooted + outer pc_it sweep — confirmed `L3/eigsolve.md:28`). All four are genuine substantive erasures, distinct from the 13 thin body-identity themes; the taxonomy correctly distinguishes them.

**variant-axis-coverage — pass.** No new operator/theme with orthogonal variant axes is authored here. The taxonomy correctly notes the one variant-conditional case (`orthogonalize-variant-split`, MGS branch vs CGS/CGS2 clean lifts) and characterizes the other three roots as unconditional/opaque-library — variant treatment is accurately attributed, not introduced.

**cross-reference-integrity — pass.** Both `[old]` blocks match the on-disk targets exactly: Edit 1 `[old]` == `index.md:62` (the c044 cohort-growth bullet, firm 14→15); Edit 2 `[old]` == `index.md:63` (the c044 partial-obstruction taxonomy paragraph). The four root slugs all resolve on disk (`ksp-solve-outer-driver.md`, `orthogonalize-variant-split.md` present; `chebyshev-nested-recurrence.md` + `eigsolve-opaque-eigen-iteration.md` land this cycle via D2/D1 — correct forward-reference to sibling cohort landings). `L3/apply_linop` resolves. The build-readiness fence guard: this is an index-prose edit (no firm-chapter body claimed in the fence), so the firm-body-inside-fence guard is inapplicable; fence parity is clean (4 fences = 2 balanced `edit:` blocks, no nested fences).

**edge-label-fidelity — pass.** The report is L3>L2-scoped throughout; every taxonomy root and the tally discuss exactly the L3→L2 edge (or, for `apply_linop`, the by-design L3→L1 direct hop with no L2 RHS, which is correctly framed as the absence of an L3>L2 theme). No mismatched edge labels.

**plan-kind-consistency — pass.** Declared shape is an index-refresh + taxonomy note + count tally (layer-intro-author, sole count-owner). Content matches: two §Working-Notes prose edits, no chapter bodies, no D1/D2 rows/bullets/SUMMARY touched. The count-ownership discipline is correctly applied (D3 counts BOTH cohort landings 15→17, not just one; D1 and D2 each individually deferred the tally and stated their own +1, 15→16, which D3 consolidates — no double-count, no under-count).

**skill-uptake-survey — pass (telemetry).** The report explicitly notes the `citecheck` self-verification pass is a no-op (no L0 ranges) and that D1/D2 ran their own anchor verification — appropriate skill-uptake disclosure for an index-prose dispatch. No surface/rotation skill is implied by this report's shape that goes unreferenced.

### Verification of the brief's six focus points

1. **Count correctness — confirmed.** `grep -c '^| \[\`' book/src/L3-L2/index.md` = 15 firm rows pre-cohort (on disk now). D1 adds `eigsolve-opaque-eigen-iteration`, D2 adds `chebyshev-nested-recurrence` → 17 firm post-cohort. The tally `firm 15 → 17` and `l3-l2-rotation-theme-coverage-gap 15-of-18 → 17-of-18` are arithmetically correct. `deflate-composition-lowering` is not among the 15 on-disk firm rows and is correctly NOT in the firm count.
2. **Denominator reconciliation — confirmed.** `ls book/src/L3/*.md` minus `index` = exactly 18 operator files; `apply_linop` is among them. `L3/apply_linop.md:146` confirms the by-design no-L2-entry / no-L3-L2-theme status with the cycle-010 "CONFIRMED-NOT-NEEDED-WITH-CAVEAT" verdict. So 17-of-18 with `apply_linop` as the by-design non-applicable residual is sound; 17-of-17-applicable is the defensible re-denomination D3 correctly defers to the meta-phase.
3. **Taxonomy accuracy — confirmed.** All four root attributions check out against on-disk endpoints: unconditional-single-loop / `ksp-solve-outer-driver` / c021; variant-conditional-single-loop / `orthogonalize-variant-split` / c044 (verified `partial-obstruction` + variant-conditional in its body); unconditional-nested-double-loop / `chebyshev-nested-recurrence` / c045 D2 (D2 report verdict LAND, root attribution matches); opaque-library / `eigsolve-opaque-eigen-iteration` / c045 D1 (SLEPc EPSSolve / ARPACK naupd RCI confirmed in `L3/eigsolve.md`). The 13-thin-vs-4-substantive split is correct (13 on-disk `*body-identity*.md` files + the 4 substantive = 17).
4. **Count-ownership — confirmed.** D3's two edits touch ONLY `index.md:62`/`:63` (the tally bullet + the taxonomy paragraph). D1 (OQ#3) and D2 (Change 5 NOTE) both explicitly state they did NOT touch the tally and deferred it to D3; their rows/bullets/SUMMARY rows/chapter-body re-anchors are untouched by D3.
5. **Supersede note — confirmed correct.** D2 Change 5 replaces a single SENTENCE inside `index.md:62`; D3 Edit 1 rewrites the ENTIRE bullet at `:62`. Applying both would conflict (D2's target sentence is consumed by D3's whole-bullet rewrite). D3's instruction — apply Edit 1 as authoritative for :62, skip D2 Change 5 — is the correct resolution. The supersede is on the same line and D3 is the sole count-owner.
6. **cross-reference-integrity + fence parity — confirmed** (see check 5 above): `[old]` blocks match exactly, slugs resolve, fences balanced.

### Issues found

No blocking issues. Two minor observations (not defects, surfaced for the integrator/repairer's awareness):

- **(informational, no action) D1/D2 individual-landing arithmetic vs. D3 consolidated tally.** D1's OQ#3 and D2's Change 5 NOTE each state their own single landing as "15 → 16" (each counting itself on top of the 15 pre-cohort). D3 reports "15 → 17" counting BOTH. This is the intended count-ownership discipline (`parallel-blind-shared-index-count-divergence`, cycle-039), not a contradiction — D3 is the sole count-owner and correctly sums both cohort landings. Noting it only because an integrator reading D1/D2 in isolation might momentarily expect "16."
- **(informational, no action) Edit 1/Edit 2 frontmatter `verifies` path.** The report's own frontmatter `status: pending` is normal for a pre-integration report. No issue. (META frontmatter `verifies:` points at `../CYCLE.md` per this repo's CYCLE.md rename convention.)

---
repaired_at: 2026-06-01T142200Z
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

## Repair

### Fixes attempted

The critic returned all 8 checks `pass` with no blocking issues. Nothing was flagged warning/fail, so there is no finding to repair. The two items in the critic's §"Issues found" are explicitly tagged **(informational, no action)** and are not defects — recorded below as informational-no-defect for accountability.

- **Finding**: D1/D2 individual-landing arithmetic ("15 → 16" each) vs. D3's consolidated tally ("15 → 17").
  - **Decision**: not-needed (informational, no defect).
  - **Rationale**: This is the intended count-ownership discipline (`parallel-blind-shared-index-count-divergence`, cycle-039). D3 is the sole count-owner and correctly sums BOTH cohort landings; D1/D2 each correctly deferred the tally and stated only their own +1. No double-count, no under-count, no contradiction. Nothing to fix.

- **Finding**: Edit 1/Edit 2 frontmatter `verifies` path / report `status: pending`.
  - **Decision**: not-needed (informational, no defect).
  - **Rationale**: `status: pending` is normal for a pre-integration report; META `verifies: ../CYCLE.md` is the correct CYCLE.md-rename convention. No issue.

### Unrepairable findings

None. No finding exceeds repair authority because no finding is a defect.

## Suggested resolution

`overall_status: ready` — apply as-is. Notes for the integrator and meta-phase:

**Integrator (per-report):**
- The report carries a same-line supersede the integrator MUST honor: **apply D3 Edit 1** (whole-bullet rewrite of `book/src/L3-L2/index.md:62`, authoritative for the tally bullet) and **skip D2 Change 5** (single-sentence replacement targeting the same `:62`). Applying both would conflict — D2's target sentence is consumed by D3's whole-bullet rewrite. The critic confirmed this resolution (§"Issues found" / focus-point 5). D3 is the sole count-owner per the count-ownership partition.
- The two D3 edits touch ONLY `index.md:62` (tally bullet) and `:63` (taxonomy paragraph); D1/D2 rows, SUMMARY rows, and chapter-body re-anchors are untouched by D3.

**Meta-phase (informational, for ratification — not repair work):**
- The erasure-scope taxonomy is now complete with four roots (unconditional-single-loop, variant-conditional-single-loop, unconditional-nested-double-loop, opaque-library). Consider ratifying it and deciding whether a `book/src/concepts/erasure-scope.md` page is warranted.
- Consider closing the `remaining-substantive-l3-l2-rotations-chebyshev-eigsolve` OQ (the chebyshev + eigsolve substantive rotations land this cycle via D2/D1).
- Consider re-denominating the coverage gap to `17-of-17-applicable` (with `apply_linop` recorded as the by-design non-applicable 18th — no interposed L2 entry, no L3-L2 theme, per the cycle-010 "CONFIRMED-NOT-NEEDED-WITH-CAVEAT" verdict at `L3/apply_linop.md:146`). D3 correctly deferred this re-denomination decision to the meta-phase rather than authoring it.

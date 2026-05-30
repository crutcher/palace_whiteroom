---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T23:58:18Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-30T00:15:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: critique of `triangular-solve-obstruction` L1>L0 obstruction-theme abstractor report

## Critique

### Checks run

**citation-validity — pass.** Mechanical `tools/citecheck/citecheck.py --scan` over CYCLE.md returns 52 ok / 0 failing across all 52 citations. Verified every load-bearing negative anchor with `--anchor`: `jacobi.hpp:19` (`'JacobiSmoother'`) — OK at line 19; the c028 report's `jacobi.hpp:15` site is independently confirmed to drift by +4 (suggested 19), corroborating the report's §Open-questions friction note. `amg.cpp:19/24/29` (`'l1-symm. GS'` / `'relax_type = 18'` / `'HYPRE_BoomerAMGSetRelaxType'`) all anchor exactly. `ams.cpp:158/162/173/179` (`'amg_relax_type'` / `'l1-SSOR'` / `'HYPRE_AMSSetSmoothingOptions'` / `'coarse_relax_type'`) all anchor exactly. Direct-solver wrapper anchors `strumpack.hpp:18/21`, `superlu.hpp:22`, `mumps.hpp:21` all anchor exactly. The blockprecond `:16-29` red-herring range anchors `'Block lower-triangular'` at line 16 within the range. `chebyshev.hpp:23/82` (`'ChebyshevSmoother'` / `'polynomial versus Gauss'`) anchor exactly. `densematrix.hpp:24-36` range scans MatrixSqrt at lines 24 and 26, in range. `L3/index.md:7` text confirmed to contain "certain triangular solves". The `:24` GPU-flip pinpoint is correctly paired with a `'relax_type = 18'` anchor (the assignment line — the `l1-Jacobi` semantic enum text itself sits at line 19, which the report's Supporting-evidence block explicitly notes and rationalizes the anchor choice for; this is good practice, not drift).

**surface-or-evidence — pass.** This is an obstruction theme (cycle-004 minres / bicgstab precedent shape: a NEW file in `book/src/L1-L0/` with no constructive L1 form, plus the index dep-map row and SUMMARY.md row). Surface change IS made (the new file + 2 edits). The negative-finding standard applies: the "no positive site" claim is grounded by (a) two exhaustive whole-tree zero-hit codemap text searches (`trsv|trsm|TriSolve|TriangularSolve|SpTrSV` + the GS/SOR/ILU/IC/Cholesky smoother class regex), independently reproduced by the cycle-028 harvester+critic and re-cited here, plus (b) 17 positive negative-anchor citations (5 categories: small-dense API absence, HYPRE GS/SSOR enums + setter calls, AMS smoother enums + setter, Palace-native GS-free smoothers with the Adams-2003 deliberate-choice citation, external-direct-solver wrappers, plus the blockprecond red-herring). The Adams-2003 + GPU GS→Jacobi flip pair is genuinely load-bearing: it demonstrates the absence is **engineered**, not accidental — that is the kind of positive evidence a strong obstruction theme should carry, and it is present. The bar is met.

**rotation-quality — pass (not applicable in the usual sense).** Obstruction themes do not assert an algebraic rotation — the LHS (L1) is empty by construction and the RHS (L0) is the absence anchor. The report is explicit: "Empty — no constructive L1 form is proposed" / "Empty — no Palace site authors a general triangular-solve." This matches the obstruction-theme precedent and the per-meta-phase obstruction-theme treatment. No rotation to evaluate.

**variant-axis-coverage — pass.** The "Applicability conditions" section enumerates four variant axes / cases for the obstruction's boundary: (1) the general `trsv` (sparse or dense, length-N field) — obstruction applies; (2) the small-dense GMRES/FGMRES back-substitution (the firm `back_solve` sibling) — obstruction does NOT apply, with the dense-small-coordinate / sparse-large-field representation/cost distinction explicitly drawn; (3) the 2×2 block forward solve (`blockprecond.hpp:16-29`) — obstruction does not apply because it is not a triangular-solve primitive at all (red herring); (4) opaque-library-internal triangular sweeps (HYPRE / STRUMPACK / SuperLU / MUMPS) — obstruction applies on the Palace side. Each axis is explicit with a verdict; no hidden branches. The Speculative-operators section additionally explains why none is proposed (no upstream consumer would simplify), which is itself a coverage statement.

**cross-reference-integrity — warning.** All explicit `[link]` references in the new theme body resolve: `../L1/back_solve.md`, `../L1/lu_solve.md`, `./minres-iteration.md`, `./bicgstab-iteration.md` all exist on disk. The forward-reference to `back-solve-mutation-rotation` is correctly PLAIN-TEXT (the target file `book/src/L1-L0/back-solve-mutation-rotation.md` is absent — confirmed via `ls` — and a live link would break `linkcheck2`); the integrator-finalize upgrade-pass is explicitly flagged. The `book/src/L3/index.md:7` cross-reference target text confirmed. SUMMARY.md `[old]` anchor `- [minres-iteration](./L1-L0/minres-iteration.md)` matches line 98 exactly; L1-L0/index.md `[old]` anchor (the `bicgstab-iteration` dep-map row) matches line 40 exactly. Fence parity: 6 ``` markers = 3 balanced blocks; the body apparatus (`## Status` at line 458, `verified_against:` at line 376) sits INSIDE the `new:` block fence (no firm-body-outside-fence defect). **Warning: missing cross-reference to the existing Phase 1 slice `book/src/spec/slices/sparse_triangular_solve.md`** (registered at `book/src/SUMMARY.md:146`), which is **the canonical-instance home for the same negative result** — its annotated-retention header explicitly cites itself as the canonical instance of `concepts/scope-out-obstruction.md` §"Canonical instance" (`:68`) and `concepts/sequential-obstruction.md` §"Sub-kind: out-of-scope-obstruction" (`:53`). The new L1>L0 theme covers the same triangular-solve absence with overlapping L0 anchors (the slice cites `superlu.{hpp,cpp}`, `strumpack.hpp`, `mumps.hpp`, `blockprecond.hpp` — four of the new theme's negative anchors), but the new theme does not reference the slice, the slice's two concept anchors, or the `negative-result-slice` concept page. This creates duplication risk (two retained negative-result records for the same absence) and leaves a stale slice header — the slice's §"Live OQs" still asks whether the negative result has a richer home, which this theme would arguably answer. Not blocking (the new theme stands on its own; the slice is "annotated-and-retained" by policy) but recommend a §"Related" or §"Open questions / caveats" cross-link to (a) the slice and (b) the two concept pages it is the canonical instance of. (This is the "duplication explosion in adjacent layers" CLAUDE.md guards against.)

**edge-label-fidelity — pass.** The theme declares edge `L1>L0`. The new file's directory (`book/src/L1-L0/`), the index.md dep-map row insertion (`book/src/L1-L0/index.md`), and the SUMMARY.md placement (clustered with the other L1>L0 obstructions `bicgstab-iteration` and `minres-iteration`) all match. The prose discusses the L1 (empty — would-be `trsv :: …`) and L0 (absence + opaque-library substrate) sides of the same L1>L0 edge consistently. Verbal asides about L3 (`book/src/L3/index.md:7` cross-ref, the partial-obstruction parallel to `eigsolve`) are presented as cross-layer references / motivation, not as the edge under discussion.

**plan-kind-consistency — pass.** Frontmatter declares `scope: L1>L0 obstruction theme — triangular-solve-obstruction`; the new file's §Justification-kind says `obstruction`; the new file's §Status says `obstruction`; the dep-map row's status cell carries `obstruction *(claim-free; resolves trsv leaf of OQ l3-vocabulary-inventory-gap as resolved-by-obstruction; concrete L0 evidence behind book/src/L3/index.md:7)*`; the §Speculative-operators says "None proposed." All four classification surfaces are mutually consistent and match the precedent obstruction-theme shape (`bicgstab-iteration.md` confirmed to have §Justification-kind + §Status pattern, no YAML frontmatter — consistent with this new theme's no-frontmatter choice). The opaque-library-ownership / enum-only-stub sub-kind distinction (vs cycle-004 precedents) is correctly flagged as a methodology-observation, not a classification deviation.

**skill-uptake-survey — pass.** The report explicitly invokes `tools/citecheck/citecheck.py --anchor` for every load-bearing pinpoint (§Supporting evidence enumerates 16 anchor verifications) and explicitly references `upgrade-plain-text-ref-to-live-link-when-target-on-disk` for the integrator-finalize upgrade pass on `back-solve-mutation-rotation`. The fence-parity / firm-body-inside-fence question is implicitly satisfied (single proposed-changes block per file with body apparatus inside the fence — the `proposed-changes-fence-encloses-full-body-guard` shape is honored). The codemap is correctly used for localization only (per the "codemap is localization-only" invariant). No skill-uptake gap.

### Issues found

1. **[cross-reference-integrity, warning] Missing cross-reference to the existing Phase 1 slice `book/src/spec/slices/sparse_triangular_solve.md`** (CYCLE.md §"Proposed changes" / new file §"Verified-against" / §"Open questions / caveats"). The slice is the registered SUMMARY.md:146 canonical-instance home for the same negative result, anchored to `concepts/scope-out-obstruction.md` §"Canonical instance" (`:68`) and `concepts/sequential-obstruction.md` §"Sub-kind: out-of-scope-obstruction" (`:53`); the new theme's L0 anchors `superlu.{hpp,cpp}` / `strumpack.hpp` / `mumps.hpp` / `blockprecond.hpp` overlap the slice's anchors. Two retained negative-result records covering the same absence without mutual cross-linking is a duplication-risk pattern (the very thing CLAUDE.md §Optimization-tricks and the "duals OK if genuinely distinct" rule guard against). Recommend the new theme add a §"Related" pointer to the slice + the two concept-page canonical-instance sections, and ideally also include them in `verified_against:` as `positive-cross-reference` rows. Severity: warning (the new theme stands on its own + the slice is retained-by-policy, but the link gap should be closed before the artifact accumulates parallel obstruction records).

2. **[citation-validity, informational — no defect]** The `amg.cpp:24` pinpoint uses anchor `'relax_type = 18'` (the assignment line), not the semantic enum text `l1-Jacobi` which sits at `amg.cpp:19`. This is correct per the line content and the report's §Supporting-evidence explicitly explains the anchor choice (matches actual line content; the semantic enum value is supplied by the line-19 comment cited separately as `amg.cpp:19`). No defect — recording so a future critic doesn't re-litigate.

3. **[skill-uptake-survey, informational — no defect]** The §Open-questions §"Justification-kind variant" flag (opaque-library-ownership vs enum-only-stub obstruction sub-kinds) is a useful meta-phase signal but currently sits as a passive note — it is **not** filed as a friction-ledger candidate via `scaffolding/skill-candidates.md`. The report's framing is correct (meta-phase consideration, not an active proposal), but if the sub-kind distinction is load-bearing for the obstruction-theme cohort (3+ themes now after this lands), the abstractor could consider appending a candidate. Severity: informational only — pure presence/telemetry, no action required.

## Repair

### Fixes attempted

- **Finding**: [cross-reference-integrity, warning] Missing cross-reference to the existing Phase 1 slice `book/src/spec/slices/sparse_triangular_solve.md` (registered at `book/src/SUMMARY.md:146`) and the two concept canonical-instance sections it anchors (`concepts/scope-out-obstruction.md:68`, `concepts/sequential-obstruction.md:53`). Two retained negative-result records for the same triangular-solve absence without mutual cross-linking is a duplication-risk pattern.
- **Decision**: repaired
- **Action**: Surgical reference-link additions inside the `new:book/src/L1-L0/triangular-solve-obstruction.md` proposed-changes block in `reports/2026-05-29T234506Z-abstractor-triangular-solve-obstruction/CYCLE.md`. Three coordinated edits:
  1. Added a new §"Related" section to the new theme body (inserted between §"Speculative L1 operators" and §"Verified-against"). The section names the slice + the two concept canonical-instance sections, describes the relationship as "two records cross-link rather than supersede" (slice = Phase-1 canonical-instance record; this theme = layered-artifact home for the post-structural-redirect cohort), and notes the engineered-absence evidence (Adams-2003 + GPU GS→Jacobi flip) is the post-slice addition. All three references are live links — link targets verified on disk (`book/src/spec/slices/sparse_triangular_solve.md`, `book/src/concepts/scope-out-obstruction.md`, `book/src/concepts/sequential-obstruction.md` all exist; relative path `../spec/slices/…` / `../concepts/…` matches precedent — see `minres-iteration.md:24` and `:122`).
  2. Added three `verified_against:` YAML entries (verdict `positive-cross-reference`) to the new file's `verified_against:` list: one for the slice (with `book/src/SUMMARY.md:146` registration note), one for `book/src/concepts/scope-out-obstruction.md:68`, one for `book/src/concepts/sequential-obstruction.md:53`. Each entry mirrors the existing YAML shape for the other 4 `positive-cross-reference` rows already in the list.
  3. Added an §"Open questions / caveats" entry to the CYCLE.md report body (outside the proposed-changes fence) flagging Phase-1-slice-reduction candidacy for `book/src/spec/slices/sparse_triangular_solve.md` as a future same-layer-cross-cutter dispatch (OQ candidate `sparse-triangular-solve-slice-reduction-after-l1l0-theme-lands`). Explicitly NOT enacted in this repair (per the repairer directive: do not enact phase-1-slice reduction; record as a follow-up OQ instead).
- **Rationale (mechanical scope)**: The cross-references are pointers to existing, on-disk content (verified via `ls`). The link targets exist; the relationship between the two records is fully described in the slice's own header (which already names itself as the canonical instance of the two concepts and cites their line numbers). No new substantive content was authored — the §"Related" section is a pointer-and-relationship descriptor synthesised from the slice's own reduction-status header and the new theme's own framing. The YAML entries follow the existing `positive-cross-reference` shape used for `book/src/L3/index.md:7`, `book/src/L1/back_solve.md`, `book/src/L1-L0/minres-iteration.md`, and `book/src/L1-L0/bicgstab-iteration.md` already in the list. Fence parity preserved (6 fence markers = 3 balanced blocks, unchanged from pre-repair count).

Items 2 and 3 (citation-validity informational note and skill-uptake-survey informational note) carry no defect and require no repair action — recorded as `not-needed`.

### Unrepairable findings

None. The single warning finding was surgically addressed.

## Suggested resolution

`ready`. The new theme now cross-links to the existing Phase 1 slice and the two concept pages it anchors, closing the duplication-risk gap the critic identified. Integrator notes:

- Apply the report as-is — the proposed-changes block now includes the §"Related" section and the three additional `verified_against:` YAML rows.
- The new §"Open questions / caveats" entry on Phase-1-slice-reduction candidacy is in the CYCLE.md report body (outside the proposed-changes fence); the integrator should treat it as an OQ-promotion candidate for `scaffolding/open-questions.md` per the standard report-OQ-promotion flow (suggested OQ slug `sparse-triangular-solve-slice-reduction-after-l1l0-theme-lands`, with this theme + the existing slice header as inputs to a future same-layer-cross-cutter dispatch).
- The slice's existing reduction status (`annotated-and-retained`) and its §"Live OQs" remain untouched by this repair — this is a cross-link addition only, not a slice-content edit.

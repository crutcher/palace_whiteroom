---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T13:22:12Z
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
repaired_at: 2026-06-01T13:40:00Z
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

# META: verification of orthogonalize-variant-split (L3>L2 theme, cycle-044)

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` cleared all 15 citations (bounds + path-hygiene). The four load-bearing L0 anchors were confirmed with `--anchor` and Read: `orthog.hpp:46-52` MGS interleave (`w.Add` at :51, inside the `j`-loop), `orthog.hpp:66-74` CGS batched (`GlobalSum` at :70, the single `GlobalSum(m,...)` after all `m` local dots), `orthog.hpp:75-88` CGS2 refine (`dH` at :77/:80/:82/:85/:86), and `iterative.cpp:313-323` `switch (type)` dispatch (at :313). All in-range and content-supporting; +1-drift guard clean. The remaining anchors (`iterative.cpp:630-632`/`809-811` Arnoldi consumers, `test-orthog.cpp:99-120`/`154-159`, `krylov-step-body-identity.md:97`, `sequential-obstruction.md:37-48`) all resolve. One mechanical DRIFT surfaced: `variant-absorption.md:131` cited with literal token `gs_orthog` returns `[DRIFT -122]` (the token `gs_orthog` lives at line 9), BUT line 131 IS the correct line — it is exactly the orthogonalization-family bullet ("MGS/CGS/CGS2 ... absorb at all three levels under residual-axis disclosure for the L2 collective shape"), which is precisely the claim the report attaches to it. The DRIFT is a token-choice artifact (the report's prose describes the line's content, the `gs_orthog` slug just happens not to be the literal on that line); the line is in-range and supports the claim, so this is not a citation miss. No `verified_against:` YAML block in this report (the §Verified-against is prose, not a fenced YAML payload), so the round-trip sub-check is n/a.

**surface-or-evidence — pass.** This is a `new:` theme file (new surface) between two firm endpoints, not a refinement of an existing operator/theme. The proposal adds surface (the whole `orthogonalize-variant-split.md`) and is backed by rotation evidence (L0 source + both firm endpoints + the sibling precedent). Not a pure rotation_claim without surface.

**rotation-quality — pass (load-bearing, confirmed substantive).** The central claim — that this is a genuine non-identity rotation, not a mislabeled identity — is confirmed directly against L0 source. `OrthogonalizeColumnMGS` (`orthog.hpp:46-52`) interleaves `H[j]=dot(w,V[j])` / `GlobalSum(1,&H[j])` / `w.Add(-H[j],V[j])` inside one `j`-loop, with the `w.Add` mutating `w` so it feeds the next iteration's `dot` — a true sequential recurrence (the `partial-obstruction`). `OrthogonalizeColumnCGS` (`orthog.hpp:66-74`) does all `m` dots against the *original* `w`, then a single `GlobalSum(m,H)`, then all `m` `w.Add`s — a batched, recurrence-free statement. This is a real structural difference: the L3 form renders the explicit MGS `jloop` tail recursion + named obstruction; the L2 form erases the iteration view to the `project ▷ subtract` composition and shadows the obstruction to two L2-vocabulary non-laws + the `m×1`/`1×m`/`2×m` residual-axis disclosure. The L2 surface is strictly more compact/abstract (no rendered loop, obstruction expressed only as non-laws). The rotation is correctly narrated FORWARD (high→low, L3→L2) and is correctly scoped as variant-conditional (MGS substantive; CGS/CGS2 clean lifts both sides; per-step body identity-in-form). Not a renaming or 1:1 map. This is a real rotation.

**variant-axis-coverage — pass.** The `gs_orthog ∈ {MGS, CGS, CGS2}` axis is the load-bearing variant axis and is covered exhaustively: a per-arm row in the §Rewrite-shape table for each of MGS/CGS/CGS2 plus the per-step-body and obstruction-shadow rows. Householder is explicitly scoped out (applicability condition 1 + L0 confirmation that `orthog.hpp` defines only `OrthogonalizeColumnMGS`/`OrthogonalizeColumnCGS`, no Householder path) under the unimplemented-component policy. The parametric axes (`dot`-hook, element-type) are stated invariant under the rotation. No hidden branches; the `switch (type)` at `iterative.cpp:313-323` has exactly the three covered cases.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: L3/orthogonalize, L2/orthogonalize, L1/orthogonalize, L2-L1/orthogonalize-composition-lowering, L3/dot, L3/axpy, L2/dot, L2/axpy, L2/index, L3/index, ksp-solve-outer-driver, the three concept pages, l4_calculus, krylov-step-typed-wrapper-dissolution. The named L2 non-laws the report relies on as the MGS-obstruction shadow both exist in `L2/orthogonalize.md` ("Column-order commutativity under MGS" :224, "Stage-fusion across the project/subtract boundary (CGS2)" :233). The four `proposed-changes` edit anchors all resolve in the live files: the `divfree-projector-body-identity` table row (edit1 insert-after), the `normalize-body-identity` cohort bullet at :51 (edit2 insert-after), the cycle-043 "Cohort growth ... (firm 10 → 14;" bullet at :56 (edit3 replace), and the SUMMARY `normalize-body-identity` line at :55 (edit4 insert-after). Build-readiness fence guard: this is a `new:`/`edit:` theme file (not a firm operator chapter asserting Signature+Algebraic-laws+Evidence apparatus), so the firm-body-inside-fence guard targets the theme body — the entire `# orthogonalize-variant-split` body including `## Status` is enclosed inside the `new:` fence (lines 23-453); no body authored outside the fence.

**edge-label-fidelity — pass.** Edge label is L3>L2 throughout; LHS=L3 (the `case op.variant` iteration-rotation form), RHS=L2 (the `project ▷ subtract` composition), narration is forward (high→low) — confirmed by §"L3 form (LHS)", §"L2 form (RHS)", and the §Justification "Abstraction-direction note" ("rotation direction is L3 → L2"). The contrast with `ksp-solve-outer-driver` is accurate: that theme is the unconditional whole-operator-is-the-loop erasure; this one is variant-conditional (MGS branch only). No edge-direction inversion.

**plan-kind-consistency — pass.** Declared kind is a `firm` substantive (non-identity) L3>L2 theme. Content matches: both endpoints are firm (L3 partial-obstruction c040, L2 firm c012), the substantive content is citation-grounded at L0 and both layers, no rough-in placeholders, no speculative L3 vocabulary (correctly "None" in both §Speculative sections). The slug choice `orthogonalize-variant-split` (NOT `-body-identity`) is correct and consistent with the content: the report is explicit that the per-step body IS identity-in-form (shared with the BLAS-1 `-body-identity` cohort) but the theme's load-bearing content is the substantive MGS loop-erasure, so a `-body-identity` slug would mis-name it. This follows the `ksp-solve-outer-driver` substantive-naming precedent (a role/scope-descriptive slug for a substantive theme, not a `-body-identity` slug). Reasonable and consistent.

**skill-uptake-survey — pass.** The report's shape (L0 citation verification) invokes `verify-citation-range`'s mechanical `citecheck --anchor`/`--scan` realization, referenced explicitly in §Supporting-evidence and §Verified-against ("self-verified ... via read_range + citecheck --anchor this dispatch; ... all anchors returned [ok]"). The variant-axis decision references `classify-variant-axis` indirectly via the `variant-absorption` concept page. Telemetry present; no blocking.

### Issues found

1. **(minor, non-blocking) Citation anchor token vs. report prose — `variant-absorption.md:131`.** Report §Verified-against "Cross-cutting concept references" cites `variant-absorption.md (:131)` for "the `gs_orthog` residual-axis disclosure discipline." `citecheck --anchor 'gs_orthog'` reports `[DRIFT -122]` because the literal token `gs_orthog` is at line 9, not 131. However line 131 IS the correct supporting line (the orthogonalization-family bullet on residual-axis disclosure for the L2 collective shape) — the line number is right; only the report's narration uses the slug `gs_orthog` which is not the literal on that line. No correction to the line number is needed; the citation supports the claim. Flagged only for transparency.

2. **(minor, non-blocking) L2 non-law name paraphrase.** In §Rewrite-shape (CGS2 row) and §"Rewrite shape" step (2), the report calls the L2 non-law "stage-fusion across the CGS2 pass boundary," while the actual `L2/orthogonalize.md:233` non-law is titled "Stage-fusion across the project/subtract boundary (CGS2)." Same law, paraphrased title. The §Applicability-conditions and §Verified-against elsewhere quote it correctly. Cosmetic; resolves to the right target.

3. **(informational, correctly self-flagged) L3-entry §"Downward" carry-forward inconsistency.** `L3/orthogonalize.md` §"Downward" (line 408) and the frontmatter `lowers_to` note (line 8) currently state "no `L3-L2/` theme file — in-line per the cycle-012 non-adjacent-identity convention." That statement is now stale for the *substantive loop-erasure* half once this theme file lands (the cycle-012 convention covers identity rotations only; substantive rotations get a dedicated file, per the `ksp-solve-outer-driver` precedent). The report's §Open-questions accurately diagnoses this, correctly scopes the L3-operator-entry edit OUT of abstractor write-authority (harvester/lifter/integrator territory), and flags it for follow-up rather than silently editing it. This is correct handling, not a defect in this report — but the downstream integrator/repairer should be aware the L3 entry's cross-reference will be momentarily stale until a follow-up dispatch points §"Downward" at this new theme for the substantive half (keeping the in-line body-identity note). No action required of this report.

4. **(observation, count-ownership — clean) Sole L3-L2/index tally owner, dual-registration verified.** The report is the sole count-owner for `book/src/L3-L2/index.md` this cycle and performs the full registration: (a) table row added (edit1, after `divfree-projector-body-identity`); (b) §Vocabulary-cohort bullet added (edit2, in a new "Substantive / non-identity" sub-grouping after `normalize-body-identity`); (c) §Working-Notes tally updated firm 14→15 and `l3-l2-rotation-theme-coverage-gap` 14-of-18→15-of-18 (edit3, replacing the cycle-043 bullet); (d) SUMMARY.md row (edit4). Live state confirms the pre-edit baseline: 14 firm theme rows, coverage line at 14-of-18 (index.md:56). The +1 arithmetic is correct (14→15, 15-of-18). Dual-registration (table row + cohort bullet) present per the c043 convention. No count divergence.

## Repair

### Fixes attempted

- **Finding (1)**: Citation anchor token vs. report prose — `variant-absorption.md:131` returns `[DRIFT -122]` because the literal `gs_orthog` token lives at line 9, but line 131 IS the correct supporting line (orthogonalization-family residual-axis-disclosure bullet).
  - **Decision**: not-needed.
  - **Rationale**: The critic confirmed line 131 is in-range and content-supporting; the DRIFT is a token-choice artifact (the report's prose narrates the line's content, the `gs_orthog` slug just isn't the literal token on that line). The line number is correct and the citation supports the claim. Deliberately NOT regressed — changing the line number would break a correct citation; changing the anchor token would author content. No mechanical fix is warranted.

- **Finding (2)**: L2 non-law name paraphrase — report calls the L2 non-law "stage-fusion across the CGS2 pass boundary" at two sites (CYCLE.md:169 prose, :196 §Rewrite-shape CGS2 row), while the canonical `L2/orthogonalize.md:233` non-law is titled "Stage-fusion across the project/subtract boundary (CGS2)."
  - **Decision**: repaired.
  - **Action**: Replaced both paraphrased occurrences with the canonical quoted title "Stage-fusion across the project/subtract boundary (CGS2)" (CYCLE.md §Rewrite-shape step (2) prose line and the §Rewrite-shape table CGS2 row). Verified the canonical title against the live artifact (`book/src/L2/orthogonalize.md:233`). Both edits land inside the `proposed-changes` fence (theme body). Same named law, exact-title match now; §Justification (CYCLE.md:326-327) and §Verified-against already quoted it correctly and were left as-is. Mechanical title-match only; no content change.

- **Finding (3)**: L3-entry §"Downward" carry-forward inconsistency — `L3/orthogonalize.md` §"Downward" (:408) + frontmatter `lowers_to` (:8) state "no `L3-L2/` theme file ... in-line per the cycle-012 non-adjacent-identity convention," which goes stale for the substantive loop-erasure half once this theme file lands.
  - **Decision**: not-needed.
  - **Rationale**: Correctly self-flagged by the report's §Open-questions and correctly scoped OUT of abstractor write-authority (the L3-operator-entry edit is harvester/lifter/integrator territory). The critic notes D4 (this same cycle) reconciles the L3 §"Downward" cross-reference. Not a defect in this report; editing the L3 entry here would (a) exceed repair authority — it's artifact (`book/`) modification, explicitly out of scope — and (b) author cross-reference content. Left for the in-cycle D4 / integrator follow-up.

### Unrepairable findings

None. All findings are either pass (critic), repaired (finding 2), or not-needed (findings 1, 3, 4).

## Suggested resolution

`ready`. Notes for the integrator:
- Finding (2) title-match was applied to CYCLE.md (two occurrences) before integration; the proposed-changes block now quotes the canonical L2 non-law title exactly.
- Finding (3) (L3/orthogonalize §"Downward" + `lowers_to` staleness for the substantive half) is reconciled by D4 in this same cycle per the critic's note — the integrator should confirm D4's edit lands so the L3 entry points §"Downward" at this new `orthogonalize-variant-split.md` for the substantive loop-erasure half while keeping the in-line body-identity note for the identity half. No action needed on this report.
- Finding (1) `gs_orthog` anchor was deliberately NOT regressed — line 131 is the correct supporting line; do not "fix" the line number or anchor token downstream.

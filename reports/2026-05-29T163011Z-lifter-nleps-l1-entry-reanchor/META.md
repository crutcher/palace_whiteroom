---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T16:56:55Z
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
repaired_at: 2026-05-29T17:14:00Z
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

# META: verification of "Re-anchor NLEPS-interior L1 entries (citation-drift correction)"

## Critique

### Checks run

**citation-validity — warning (load-bearing).** This is the central check for a pure re-anchor
pass and I ran it mechanically and exhaustively. `tools/citecheck/citecheck.py --scan` on the report
CYCLE.md returns **34 ok, 0 failing** — matching the report's claim. (Note: `--scan` is bounds-only;
the file is 952 lines so both the OLD and the NEW pinpoints are all in-bounds — a clean scan does
NOT by itself distinguish a drifted pinpoint from a correct one. The load-bearing verification is
`--anchor`, which I ran on a representative subset.) Anchor results:
- **Cluster 1 (six deflation-block anchors).** All six NEW numbers land: `:660-661` (`w1 = T'(l) v1`),
  `:662-663` (`auto A = BuildParSumOperator`), `:664` (`const Eigen::MatrixXcd S = eig`), `:665`
  (`Sv2 = S.fullPivLu().solve(v2)`), `:666` (`XSv2 = MatVecMult(X, Sv2)`), `:667` (`XSSv2 = ...`) —
  all `[ok]`. The corresponding OLD single-line pinpoints genuinely drift `+1`: `:663`→suggested
  `:664`, `:666`→suggested `:667`, etc. I read the on-disk block `nleps.cpp:658-670` directly and
  confirmed the ground truth: the `{` is on `:659`, the two-line `w1=...` comment is on `:660-661`,
  the `BuildParSumOperator` call spans `:662-663`, and `S`/`Sv2`/`XSv2`/`XSSv2` are on
  `:664`/`:665`/`:666`/`:667`. The report's corrected numbers are exactly right.
- **Range-citation caveat (not an error, but noted).** The two range citations `:659-660`→`:660-661`
  (comment) and `:661-662`→`:662-663` (value pencil) both pass `--anchor` in BOTH their old and new
  forms, because the load-bearing anchor token sits on a line inside both ranges. The re-correction
  is nevertheless genuinely right (verified by direct on-disk read: old `:659-660` wrongly includes
  the bare `{` at 659 and truncates the comment's second line at 661; old `:661-662` includes a
  comment line and truncates the call). The report relied on the single-line pinpoint drift + on-disk
  read rather than the range `--anchor` (which would false-pass) — correct discipline.
- **Cluster 2 (two anchors).** Both NEW land and both OLD genuinely drift: `:590` (`while (it <
  nleps_it)`) `[ok]`, OLD `:596` `[DRIFT]` suggested `:590` (−6); `:712` (`alpha *= backtrack_factor`)
  `[ok]`, OLD `:709` `[DRIFT]` suggested `:712` (+3). The claimed-unchanged anchors `:691`
  (`eig + alpha`), `:708` (`eig = eig_trial`) verify `[ok]`.
- **Cluster 3 (vector.cpp sweep).** On-disk `vector.cpp:664-672` read directly: `:667` is
  `static hypre::HypreVector X, Y;`, `:668` is the `MFEM_ASSERT(x.Size()==y.Size(), ...)`. NEW `:668`
  `[ok]`, OLD `:667` `[DRIFT]` suggested `:668`. **The two EXTRA sites beyond the OQ (`:403`,`:553`)
  are confirmed genuine** — all four occurrences (`:59`,`:260`,`:403`,`:553`) cite the identical
  `MFEM_ASSERT(x.Size()==y.Size())` line; `:403` is an Evidence-row mention, `:553` is a
  lowering-verifier `note:` annotation. Not over-reach.
- **Exact-string apply readiness.** Every `[old]` string across all clusters is verbatim-present and
  **single-occurrence** in its target file (verified by `grep -cF` per edit: all return 1). The
  integrator's exact-string apply will match cleanly.
- **The warning** is the one missed drift documented under Issues (line 145 of
  `nleps_jacobian_action.md` — an uncorrected `:659-660` comment-anchor inside the `:649-669`
  Evidence row that the sweep's own scope claims to cover). Everything the report explicitly edits is
  correct; the warning is for an in-scope occurrence the sweep missed, which leaves an intra-file
  inconsistency post-apply.

**surface-or-evidence — pass.** Largely a no-op for this report shape, as the dispatch instructed.
This is a pure citation re-anchor: no operator/theme surface text (signature, semantics, laws,
variant axes, status) changes — only digits inside citation pinpoints. It is not a refinement-shaped
proposal modifying surface, and not a rotation_claim. The report frames itself explicitly as
"bounded citation-drift correction … not the L0-evidence-driven prose-correction sub-case (no claim
is wrong; only line numbers drifted)" (CYCLE.md §Discipline notes). The `firm` status of both L1
entries is preserved and unaltered. Not applicable in the substantive sense; pass.

**rotation-quality — pass.** Not applicable to a re-anchor pass — no algebraic/structural/reduction
rotation is asserted or modified. The L1↔L0 representation relationship is untouched; only the L0
pinpoints that the existing L1 entries cite are corrected. Pass (not applicable).

**variant-axis-coverage — pass.** No variant axes are introduced or modified. The report touches
only citation digits; the existing operators' variant-axis treatments (e.g. the `k=0`/`k>0`
deflation branch, the weighted/unweighted inner-product members) are unchanged. Pass (not
applicable to a re-anchor).

**cross-reference-integrity — pass.** All four edit-target files exist
(`book/src/L1/nleps_jacobian_action.md`, `book/src/L1/nleps_eigenvalue_correction.md`,
`book/src/L2/inner_product.md`, `book/src/L2-L1/inner-product-fold-specialization.md`). All `[link]`
targets named in the new-strings resolve on disk (`./lu_solve.md`, `../L2/linear_combination.md`,
`book/src/L1-L0/nleps-jacobian-action-mutation-rotation.md`). The cross-consistency claim in OQ #1 —
that the theme `nleps-jacobian-action-mutation-rotation.md` already uses the corrected on-disk
numbers — is **verified true**: that theme's Evidence block already cites `:664`/`:665`/`:666`/`:667`
for S/Sv2/XSv2/XSSv2, `:660-661` for the comment, `:662-663` for the value pencil, and `:668`/`:669`
for the AddMults, so after this re-anchor the operator entry and theme agree. No firm-body-inside-
fence concern — this report carries no proposed-changes block authoring a firm chapter body; the
`edit:` blocks are all single-edit citation swaps with balanced fences. Pass.

**edge-label-fidelity — pass.** No edge labels are carried or altered. The vector.cpp sweep touches
an L2 entry and an L2-L1 theme, but only their citation pinpoints; no L_{n+1}→L_n edge claim is
modified. Pass (not applicable).

**plan-kind-consistency — pass.** The dispatch is a lifter re-anchor (citation-drift correction),
which the report's content matches exactly: every edit is a citation-digit swap, no new content, no
status change. The report's self-classification as "a re-anchor, not authorship" is consistent with
its content shape. Pass.

**skill-uptake-survey — pass.** The shape (mechanical citation re-anchor) implies the
`verify-citation-range` skill and its cycle-024 `tools/citecheck/` `--anchor`/`--scan` realization;
the report references and uses `citecheck --anchor` extensively (Cluster confirmations, Discipline
notes, Supporting-evidence batch verification). Telemetry surfaced; pass.

### Issues found

1. **[citation-validity — warning] Missed in-scope drift at `book/src/L1/nleps_jacobian_action.md`
   line 145 (Evidence row).** The `nleps.cpp:649-669` Evidence-block row restates the `w1 = T'(l) v1
   + ...` source comment as being at `:659-660`:
   `comment \`:659-660\` ("w1 = T'(l) v1 + U'(l) v2 = T'(l) v1 + T'(l)XS v2 − T(l)XS^2 v2") names the
   big-space + deflation-coupling decomposition`. This is the **identical drifted comment-anchor**
   the report correctly re-anchors `:659-660`→`:660-661` in three other locations (entry lines 46,
   81, 130 — the Concretely intro, the point-(4) scoping prose, and the Status paragraph). On-disk
   the comment spans `:660-661` (the `{` is at `:659`). The report has no `[old]/[new]` block
   targeting line 145 (confirmed: the string `names the operator; comment \`:659-660\`` is absent from
   any report `[old]`). After the report's edits apply, the same comment will be cited as `:660-661`
   in three places and `:659-660` in this Evidence row — an intra-file inconsistency and a surviving
   drifted pinpoint. The report's own OQ #1 claims the re-anchor was applied "across the entry's
   exec-trace, Semantics, Dependencies, Status, L1-vs-L0, **Evidence**, and cross-reference sections,"
   so this is an in-scope omission, not an out-of-scope occurrence. Severity: low-moderate — it is a
   sub-pointer inside an Evidence row whose enclosing `:649-669` block-range citation is itself
   correct and untouched, so no claim becomes wrong; but it defeats the stated sweep-completeness and
   leaves the entry internally inconsistent on the very anchor the pass exists to fix. Candidate for
   repair: add an `[old]/[new]` block re-anchoring the line-145 inline `:659-660`→`:660-661` (the
   surrounding `:649-669` row range stays as-is).

### Notes for the repairer (non-issues, recorded for confidence)

- All other potentially-drifted pinpoint families were exhaustively cross-checked against report
  coverage and are fully covered: `:663`×4 (lines 63/130/140/153), `:664,:666`×3 (lines 42/130/170),
  `:665,:666`×4 (lines 110/130/164/171), `:661-662`×5 (lines 62/81/123/140/152), `:659-660`×4 (lines
  46/81/130 covered; **145 missed** — the one issue above). Cluster-2 `:596`×1 and `:709`×1 each
  single-occurrence and covered.
- The standalone `:660` on `nleps_jacobian_action.md` line 77 is correctly left unchanged — the
  `w1=...` formula fragment is genuinely on on-disk `:660` (`--show` confirms line 660 is the comment
  line). No over-correction there.
- The `vector.cpp:664-672` range and `nleps.cpp:649-669` / `:688-714` ranges are correct on-disk and
  correctly left untouched.

---

## Repair

### Fixes attempted

- **Finding** (citation-validity — warning): Missed in-scope drift at
  `book/src/L1/nleps_jacobian_action.md:145` — the `:649-669` Evidence-block row restates the `w1=...`
  source comment as `:659-660`, but the same drift is corrected to `:660-661` in three other locations
  in this same file by this report (entry lines 46, 81, 130). Post-apply, line 145 would be left
  citing `:659-660` while three siblings say `:660-661` — an intra-file inconsistency; the report's
  own OQ #1 claims the Evidence section was swept, so this is an in-scope omission.
- **Decision**: repaired.
- **Action**: Added one surgical `[old]/[new]` proposed-changes block to CYCLE.md (after the leading
  per-line Evidence-block edits, before the cross-reference Evidence rows) re-anchoring the
  line-145 inline comment sub-anchor `:659-660` → `:660-661`. The enclosing `:649-669` block-range
  citation on the same row is correct on-disk and left untouched (as the report does throughout).
  - **Before**: ``comment `:659-660` ("w1 = T'(l) v1 + ...") names the big-space + deflation-coupling decomposition``
  - **After**:  ``comment `:660-661` ("w1 = T'(l) v1 + ...") names the big-space + deflation-coupling decomposition``
- **On-disk verification** (`tools/citecheck/citecheck.py --anchor`): the two-line `w1=...` comment
  spans on-disk `:660-661` — `--show` of `:659-661` confirms `:659` is the bare `{`, `:660` is the
  `w1 = T'(l) v1 + ... Scoping T(l)` comment line, `:661` is the comment's second line. The `w1 = T'(l) v1`
  anchor literal `[ok]`-passes BOTH `:660-661` (new) and `:659-660` (old) because the literal sits on
  `:660` inside both ranges (the critic's documented false-pass caveat); the correction is anchored on
  the on-disk read confirming `:659` is the brace (not the comment) and `:661` is the comment's second
  line — matching the three siblings already re-anchored to `:660-661`.
- **Apply-readiness**: the new `[old]` string is verbatim-present and **single-occurrence** in
  `nleps_jacobian_action.md` (`grep -cF` → 1; the leading word `comment` distinguishes line 145 from
  the sibling phrasings at lines 46/81/130). Integrator exact-string apply will match cleanly.
- **Post-repair scan**: `citecheck --scan` on the corrected CYCLE.md → **34 ok, 0 failing** (unchanged
  count — the added block re-cites the same on-disk-correct `:660-661` already present in cluster 1, so
  no new distinct citation tokens are introduced).

Also fixed the stale `verifies: ../REPORT.md` → `verifies: ../CYCLE.md` frontmatter pointer
(pre-rename artifact; the dispatch file is `CYCLE.md`).

### Unrepairable findings

None. The single warning was fully repairable (a mechanical citation-digit swap on an in-scope
occurrence the sweep missed; the correct target was independently confirmable on-disk).

## Suggested resolution

`ready`. All 7 critic `pass` checks stand; the one `warning` (citation-validity) is `repaired`. After
this added block, the `w1=...` comment is cited `:660-661` consistently across all four locations
(entry lines 46, 81, 130, 145), the entry is internally consistent on the very anchor the pass exists
to fix, and the entry agrees with the `nleps-jacobian-action-mutation-rotation.md` theme. Note for the
integrator: the new edit block sits in the Evidence-block edit run of Cluster 1; it is a single-edit
citation-digit swap with balanced fences, same shape as its neighbors.

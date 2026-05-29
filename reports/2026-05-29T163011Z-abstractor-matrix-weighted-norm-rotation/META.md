---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T17:05:00Z
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
repaired_at: 2026-05-29T17:00:19Z
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

# META: verification of "L1>L0 theme promotion (stub→firm) — matrix-weighted-norm-mutation-rotation"

## Critique

### Checks run

**citation-validity — warning.** Ran `tools/citecheck/citecheck.py --scan` on CYCLE.md: **46 ok / 0 failing**, matching the report's claim exactly. The load-bearing `Norml2` body lowering is fully sound: `--anchor` spot-checks confirm every body line on its asserted line — `operator.cpp:602` (`B.Mult`), `:603` (`Dot`), `:604-605` (`MFEM_ASSERT`), `:606` (`sqrt`), `:599` (`template`), `:601` (`{`), `:607` (`}`), and the complex branch `:612` (SPD comment), `:613-614` (lane-split `B.Mult`), `:615` (`Dot`), `:616-617` (two-part assert), `:618` (`sqrt(dot.real())`). I read `operator.cpp:597-639` and `operator.hpp:370-389` directly — the body/decl transcriptions (real spec lines 107-114, complex spec 165-175, Normalize 214-220) are faithful. The weighted callsites `arpack.cpp:438`, `arpack.cpp:470`, `slepc.cpp:475`, `slepc.cpp:505`, `nleps.cpp:114`, `nleps.cpp:146` all anchor correctly, confirming the report's claim that operator.cpp/hpp and the weighted callsite cohort are NOT affected by the cycle-025 nleps +1 drift.

However, **`--anchor` surfaces a recurring +1 drift on the three *unweighted-fallback* callsite citations**, which the report's blanket "all anchors land on the asserted lines / Self-verified" claim did not catch. See Issues 1.

**surface-or-evidence — pass.** This is a refinement-shaped proposal: it modifies surface (replaces the `stub` body with a firm theme body), so the rotation-claim-without-surface failure mode does not apply. The theme is positively-anchored structural lowering, not retroactive-evidence backfill. The firm-over-rough-in decision (firm theme lowering a `rough-in (test-coverage-bounded)` L1 operator) is justified and precedented: I verified `L1-L0/eigsolve-mutation-rotation.md` is indeed treated firm-structural over the rough-in `L1/eigsolve.md`, with `partly-constructive` reserved only for the genuinely-reconstructed `LinearSolveFailed` sub-part. Here there is no reconstructed sub-part — the one non-syntactic ingredient (`xᴴ B x ∈ ℝ_{≥0}` for SPD `B`) is read straight off the L0 source's own `// For SPD B, xᴴ B x is real.` comment (`:612`) and the assertion (`:616-617`), so `firm` (not `partly-constructive`) is the correct status. The structural-fidelity-vs-law-confidence argument is sound.

**rotation-quality — pass.** The theme is declared `structural`, and the rotation is a genuine compaction: one closed-form L1 step `√(xᴴ B x)` expands into the L0 three-step `B.Mult → Dot → sqrt`, narrated forward (L1→L0). It is not a rename or 1:1 map — the L1 form hides the workspace `Bx`, the MPI collective, the element-type lane split, and the SPD guard, all of which the lowering re-materializes. The reuse of two sibling sub-themes (`apply-linop-mutation-rotation` Sub-pattern A for `B.Mult`; `dot-mutation-rotation` Sub-pattern A for the inner `Dot`) rather than restating them is correct and verified against both target files (both exist; the inherited boundaries hold). The genuinely-new content is exactly what the report claims: caller-owned destination `Bx`, complex real/imag lane split, outer `sqrt`, SPD-guard classification, and the Sub-pattern C `Normalize` consumer.

**variant-axis-coverage — pass.** All three axes the dispatch named are covered with no hidden branches: (i) **element-type** real|complex — the two `Norml2` template specializations, collapsed at L1, both authored (Sub-patterns A/B); (ii) **weight-operator-representation** M/B-weighted — collapsed to opaque `LinearOperator[N,N]` per `apply_linop`'s representation axis, with the `*opB`-null fallback to unweighted `nrm2` cited; (iii) **`B = I` degenerate collapse** to `nrm2`, explicitly handled in §Variant axes with the exact meeting-point to `nrm2-mutation-rotation`. The output-arg-vs-return distinction is correctly classified as a workspace-ownership boundary, not a variant axis.

**cross-reference-integrity — pass.** All `[link]` targets resolve: the five sibling themes (`apply-linop`, `dot`, `nrm2`, `scal`, `eigsolve` mutation-rotation), the L1 entries (`matrix-weighted-norm`, `apply_linop`, `dot`, `bilinear-form`), and the L0 entries (`linalg-operator-file`, `transparent-vs-load-bearing-tricks`) all exist on disk. The two index.md context-anchor rows (`:28` scal, `:29` dot) match the report's quoted rows verbatim, and the new row inserts after dot as instructed. The SUMMARY.md de-stub at `:103` is a clean suffix-drop with the link path unchanged. **Build-readiness guard:** ran `grep -n '```'` — exactly 6 fence lines / 3 balanced blocks, even parity. The theme `edit:` block runs `:52→:511` and ENCLOSES the full firm body including `## Status` (`:484`), `## Variant axes`, `## Verified-against`, all `##` sections — this is NOT the cycle-019 fence-truncation defect. Nested code is authored as 4-space-indented blocks (lines 80-82, 107-114, 165-175, 214-220), not nested triple-backtick fences, so there is no nested-fence parity hazard.

**edge-label-fidelity — pass.** The edge label throughout is L1>L0, and the prose consistently discusses that exact edge — the LHS is the L1 energy norm, the RHS is the L0 `Norml2` source, narrated forward per the high→low directive. No edge-label mismatch.

**plan-kind-consistency — pass.** Declared kind is a firm L1>L0 theme (stub→firm promotion); the content shape matches — an exhaustively-cited structural rewrite with no rough-in placeholders, no `partly-constructive` caveats, no unfilled sub-parts. The frontmatter `status: pending` is the pre-integration dispatch state, consistent with a report awaiting critique/integration.

**skill-uptake-survey — pass.** The report references the relevant skills it should: `tools/citecheck/citecheck.py --anchor`/`--scan` (the cycle-024 mechanical citation realization), `verify-citation-range`, `classify-variant-axis`, and the sibling-theme reuse convention. Pure presence check — telemetry only.

### Issues found

1. **(citation-validity, warning) +1 drift on all three unweighted-fallback callsite citations — §Variant axes line 399 and §Verified-against line 443.** The report cites the eigensolver unweighted-fallback `linalg::Norml2(comm, x)` dispatch ranges as `arpack.cpp:438-441`, `slepc.cpp:475-478`, `nleps.cpp:114-117` (line 399), and the arpack pinpoint as `arpack.cpp:441` (line 443: "else unweighted `linalg::Norml2(comm, x)` (`:441`)"). Verified against source: the unweighted call is at **arpack.cpp:442** (`:441` is `else`), **slepc.cpp:479** (`:478` is `{`), **nleps.cpp:118** (`:117` is `{`). Each cited range stops exactly one line short of the fallback call it is describing — the call line is *excluded* from the range. `citecheck --anchor 'Norml2'` on `arpack.cpp:441` returns `[DRIFT] anchor at line 442, +1 outside range`. This is the off-by-one that `--scan` cannot catch (the ranges are in-file and lo≤hi, so they pass bounds-check) but `--anchor` does — exactly the cycle-024 friction case. The drift does NOT touch the load-bearing `Norml2` body lowering (all correct). Severity: low — it is a brace-boundary off-by-one on secondary fallback-path citations, and the *weighted* dispatch lines (`:438`, `:475`, `:114`) are all correct. The report's blanket "all anchors confirmed on the asserted lines / Self-verified" assertion is overstated for these three pinpoints.

2. **(citation-validity, warning) OQ #1 mis-attributes the carry-forward `:601-606` drift sites — Open questions line 568-578.** The report correctly identifies the real carry-forward defect: `L1/matrix-weighted-norm.md` cites the real `Norml2` body as `operator.cpp:601-606` where `:601` is the opening `{` (body is `602-606`) — confirmed real (`:601` anchors to `{`; the entry's `:58` and `:83` both carry `:601-606`). The OQ is correctly scoped as an out-of-scope carry-forward for a future `lowering-verifier`/`harvester` pass, NOT a defect in this report — that scoping is correct. HOWEVER, OQ #1 names the two `:601-606` sites as "`:58`, `:128` Evidence." Verified: `L1/matrix-weighted-norm.md:128` actually cites `operator.cpp:599-607` (the *correct* full-span-with-braces), not `:601-606`. The second `:601-606` instance is at **`:83`**, not `:128`. So the OQ's site list is wrong: it flags a correct citation (`:128`) and misses the actual second drift site (`:83`). The substance of the carry-forward holds (the `:601-606` brace-drift is real at `:58` and `:83`); only the provenance line-references in OQ #1 are inaccurate. Severity: low — a future-work pointer with a slightly-wrong site list; will mildly misdirect the follow-up agent.

3. **(surfaced OQ, informational — not a defect here) Category-4 mislabel confirmed real.** The report flags (OQ #2) that `L1/matrix-weighted-norm.md:9` and `L0/linalg-operator-file.md:33` label the bilinear-form `Dot`'s internally-allocated `Ax` workspace as "Category 4 — synthetic workspace." Verified: `L0/mutable-workspace-pattern.md:82` shows **Category 4 is "assembled-matrix retention,"** and the chapter has only four categories (`:27`), none named "synthetic workspace." So both labels are genuinely wrong. The report correctly does NOT rely on that category (its own `Bx` is described accurately as caller-supplied) and correctly scopes this as a pre-existing drive-by drift for a `same-layer-cross-cutter`/`lowering-verifier` follow-up. Noting here only to confirm the surfaced OQ is well-founded — it is not a defect in this report.

### Notes for the repairer

- Issues 1 and 2 are both inside the report's own prose (the §Variant-axes/§Verified-against fallback pinpoints, and the OQ #1 site list). The fixes are mechanical line-number corrections: `arpack.cpp:438-441`→`:438-442` (or pinpoint `:442`), `slepc.cpp:475-478`→`:475-479`, `nleps.cpp:114-117`→`:114-118`, and OQ #1's "`:58`, `:128`" → "`:58`, `:83`." None touch the load-bearing `Norml2` body lowering, which is correct as-cited.
- Issue 3 is a correctly-scoped surfaced OQ about *other* files; no repair to this report is implied.

## Repair

### Fixes attempted

- **Finding (Issue 1)**: +1 brace-boundary drift on the three *unweighted-fallback* callsite citations (`arpack.cpp:438-441`, `slepc.cpp:475-478`, `nleps.cpp:114-117` in §Variant axes; pinpoint `arpack.cpp:441` in §Verified-against) — each range stops one line short of the actual `Norml2(comm, x)` fallback call.
  - **Decision**: repaired.
  - **Action**: Verified the exact call line for each via `citecheck --anchor 'Norml2(comm, x)'` (and `'Norml2(GetComm(), x)'` for slepc) against on-disk `reference/palace/`: the unweighted call sits at `arpack.cpp:442` (`:441`=`{`, `:440`=`else`), `slepc.cpp:479` (`:478`=`{`), `nleps.cpp:118` (`:117`=`{`). Extended each §Variant-axes range to include the call line — `:438-442` / `:475-479` / `:114-118` (CYCLE.md §Variant axes, the `weight-operator-representation` bullet) — and shifted the §Verified-against arpack pinpoint `:441`→`:442` (CYCLE.md §Verified-against, arpack entry). Mechanical line-number correction; touches only the secondary fallback-path citations, not the load-bearing `Norml2` body lowering (`operator.cpp:599-619`, which was sound). Post-fix: `--anchor` lands on all three (range and pinpoint forms both confirmed `[ok]`), `--scan` unchanged at 46 ok / 0 failing (the +1 extensions stay in-bounds).

- **Finding (Issue 2)**: OQ #1 mis-attributes the two carry-forward `operator.cpp:601-606` brace-drift sites in `book/src/L1/matrix-weighted-norm.md` as "`:58`, `:128`" — but `:128` is the *correct* full-span `:599-607` citation, and the actual second drift site is `:83`.
  - **Decision**: repaired.
  - **Action**: Read `book/src/L1/matrix-weighted-norm.md` to verify: `:58` (law 8) cites `:601-606` (drift), `:83` (Composition note) cites `:601-606` (drift), `:128` (Evidence) cites `:599-607` (correct). Corrected OQ #1's site list (CYCLE.md §Open questions, item 1) to name `:58` (law 8) and `:83` (Composition note), and added a parenthetical noting `:128` is the correct full-span span (not a drift site), so the follow-up `lowering-verifier`/`harvester` pointer is accurate. The carry-forward defect itself (the real `:601-606` brace-drift at `:58`+`:83`) remains correctly scoped as out-of-this-theme; only the provenance line-references were fixed.

- **Finding (Issue 3)**: Category-4 mislabel (`mutable-workspace-pattern.md` Category 4 = "assembled-matrix retention" not "synthetic workspace", flagged via the labels at `L1/matrix-weighted-norm.md:9` + `L0/linalg-operator-file.md:33`).
  - **Decision**: not-needed.
  - **Rationale**: Explicitly scoped by the critic and the dispatch as a correctly-surfaced pre-existing drive-by OQ about *other* files; the report does not rely on the mislabel and the surfaced OQ (`bilinear-form-workspace-category-4-mislabel`) is well-founded. No repair to this report is implied — leave as the surfaced OQ for a `same-layer-cross-cutter`/`lowering-verifier` follow-up.

### Unrepairable findings

None. Both citation-validity issues were mechanical line-number corrections within the report's own prose (in repair scope: "Citation line range off by a small offset"). Issue 3 is a correctly-scoped surfaced OQ, not a defect in this report.

## Suggested resolution

`ready`. Notes for the integrator:

- All three unweighted-fallback callsite citations and the arpack §Verified-against pinpoint now anchor on the `Norml2(comm, x)` call line; `--scan` clean at 46 ok / 0 failing. The load-bearing `Norml2` body lowering (`operator.cpp:599-619` → `B.Mult → Dot → sqrt`) was sound throughout and is unchanged.
- The carry-forward defect in `book/src/L1/matrix-weighted-norm.md` (the real `Norml2` body cited as `operator.cpp:601-606` where `:601`=`{`, body=`602-606`, at `:58` and `:83`) is real but out of this theme's scope — promote OQ #1 (`matrix-weighted-norm-mutation-rotation-l1-l0-theme`) for a `lowering-verifier`/`harvester` follow-up with the now-accurate site list (`:58`, `:83`; `:128` is correct).
- Two further surfaced OQs to promote as-is: `bilinear-form-workspace-category-4-mislabel` (Issue 3 / OQ #2) and `matrix-weighted-norm-mixed-element-type-variant` (OQ #3, paired with the `bilinear-form` firm-promotion gate).

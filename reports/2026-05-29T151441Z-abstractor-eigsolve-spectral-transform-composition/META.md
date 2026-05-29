---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T15:32:59Z
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
repaired_at: 2026-05-29T16:05:00Z
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

# META: verification of L2>L1 theme `eigsolve-spectral-transform-composition`

## Critique

### Checks run

**citation-validity — warning.** Mechanical pass first: `citecheck.py --scan CYCLE.md --quiet` returns `40 ok, 0 failing (40 citations checked)` — every cited range is in-bounds with clean path hygiene. I then ran `--anchor` on all load-bearing pinpoints. Every ARPACK anchor lands exactly (`:579 opM->Mult`, `:580 opInv->Mult`, `:581 gamma`, `:573 opK->Mult`, `:574 opInv->Mult`, `:575 1.0/gamma`, `:586 opProj->Mult`, `:761/:778 opInv->Mult`, `:191-193 opInv`, `:245-246 sinvert`, `:263-358 naupd`); every SLEPc setup/binding/loop anchor lands exactly (`:384 STPRECOND`, `:388 STSINVERT`, `:390 STSetTransform`, `:391 ST_MATMODE_SHELL`, `:392 sigma`, `:364-366 opInv`, `:674 EPSSetTarget`, `:694 EPSSolve`, `:687 Solve`, `:715 gamma`); the `__pc_apply_EPS` face lands exactly (`:1858 opInv->Mult`, `:1861 y1`, `:1865 y1`, `:1870 opProj->Mult`); `__mat_apply_EPS_A0` lands exactly (`:1809 opK->Mult`, `:1810 delta`); and all `modeeigensolver.cpp` wiring anchors land (`:1037`, `:1045`, `:1050`). The L2/L1/L3 cross-reference targets all exist on disk and the cited L2-entry law lines (`L2/eigsolve.md:99/103/105/55-77/163`) are accurate. **The single exception: the `__mat_apply_EPS_A1` pinpoints `slepc.cpp:1817` (`opM->Mult`) and `:1818` (`delta`/`delta*gamma`) DRIFT +7** — citecheck reports `[DRIFT] anchor at line 1824 / 1825`. I confirmed by reading `slepc.cpp:1801-1829`: `:1816` is the A1 function signature, `:1817` is `PetscFunctionBeginUser`; the actual `ctx->opM->Mult(...)` is `:1824` and `ctx->y1 *= ctx->delta * ctx->gamma` is `:1825`. This is NOT the codemap +1 indexing artifact the sibling nleps.cpp report flagged — it is an off-by-7. The check is a `warning` (not `fail`) because the **enclosing range citation `slepc.cpp:1801-1827` is correct and does contain A1's matvec lines** (A1 spans `:1816-1829`; the range trims only the closing `PetscFunctionReturn`/brace at `:1828-1829`), so the load-bearing structural claim is still source-grounded; only the two interior sub-line pinpoints are mis-numbered.

**surface-or-evidence — pass.** This is a new L2>L1 lowering theme (a `new:` chapter), not a refinement of an existing operator/theme. It carries full structural evidence (the de-fusion rewrite read off two positive `ApplyOp`/`__pc_apply_EPS` bodies) and modifies no existing surface beyond append-only index/SUMMARY rows. Not the refinement-without-evidence failure shape.

**rotation-quality — pass.** The proposal asserts a reduction/de-fusion rotation: the L2 single named `▷`-composition `apply_shift_invert` expands downward into an explicit two-stage `apply_linop ▷ ksp_solve ▷ scale_untransform` L1 sequence. This is a genuine compaction direction (the L2 form names one composition; the L1 form spells the explicit dataflow + the per-backend assembly residue), not a 1:1 rename. Both RHS leaves (`apply_linop`, `ksp_solve`) and the tails (`scal`, projector `apply_linop`) are firm on-disk — I confirmed `L1/apply_linop`, `L1/ksp_solve`, `L1/scal` all carry `firm` §Status, and `L2/eigsolve` is `firm` (cycle-023). No speculative operator is introduced (§"Speculative L1 operators" = None, verified against the firm leaf statuses).

**variant-axis-coverage — pass.** The orthogonal axes are explicitly enumerated and each is either covered or scoped: spectral-transformation (`none | shift-invert | shift-invert-precond`) — the no-transform dual and the canonical shift-invert are both lowered (`:573-575` / `:579-581`), precond noted as approximate-inverse inner solve; problem-type (`linear | quadratic | nonlinear`) — linear is canonical, quadratic-PEP is a clean operand-stage variant (`:733-799`), nonlinear NEP is explicitly scoped OUT to the NLEPS-deflation cohort with a recorded "do not over-broaden" caveat; backend-orchestration (`arpack-rci | slepc-st-shell`) — both faces lowered as the same L1 RHS; scaling (`NONE | NORM_2`) — shapes only the `scale_untransform` multiplier. No hidden branches.

**cross-reference-integrity — pass.** All 16 `[link]` targets resolve on disk (L2/L1/L3 entries, sibling L2-L1 themes, the four concept pages). All named slugs exist. The build-readiness fence guard passes cleanly: `grep -n '\`\`\`'` shows exactly 6 fences (even parity) — three balanced proposed-changes blocks (`new:` 25-465, `edit:index` 467-471, `edit:SUMMARY` 473-477). The firm-claimed chapter body (`# eigsolve-spectral-transform-composition` through `## Status` + `## Open questions / caveats`) is fully ENCLOSED inside the `new:` fence (26-464); no `## Status` or firm apparatus sits outside the fence as a report top-level section. The pseudo-language listings inside the `new:` block are all 4-space-indented code, NOT nested ` ``` ` fences — so the cycle-019/024 nested-fence-truncation defect does not apply. The two `edit:` blocks' insert-anchor rows (gram-fold and deflate index rows; gram/deflate SUMMARY rows) match on-disk verbatim (`grep -Fxq` confirmed), and the appended eigsolve row/entry is correctly absent on disk (it is the new append).

**edge-label-fidelity — pass.** The declared edge is L2>L1 throughout. LHS is consistently the L2 `apply_shift_invert = apply_linop(M) ▷ ksp_solve((K−σM)⁻¹)` composition; RHS is consistently the firm L1 leaves; the prose narrates the rewrite forward (L2 → L1) per §"The de-fusion rewrite (L2 → L1)". The boundary reference to the L3 `partial-obstruction` is labeled as a boundary, not mis-stated as the theme's own edge. Direction discipline (high→low, LHS=L2, RHS=L1, reverse-lift note quarantined to working-notes §OQ) is observed.

**plan-kind-consistency — pass.** Declared kind is a `firm` L2>L1 theme. Content shape matches: positive line-for-line source on both backend faces, both RHS leaves firm, no rough-in placeholders, no negative-anchor reconstruction, no literature inference. The `firm` (not `partly-constructive`, not `rough-in`) classification is consistent with the sibling `orthogonalize-composition-lowering` / `gram-fold-specialization` firmness bar and the firm-on-positive-structure precedent. The `structural` justification-kind matches the read-off-positive-source content.

**skill-uptake-survey — pass.** The report's shape (citation-heavy lowering theme) implies `verify-citation-range` / `tools/citecheck/`; §"Verified-against" and §"Supporting evidence" both reference `palace-codemap read_range` + `tools/citecheck/citecheck.py --anchor`/`--scan` self-verification. Telemetry note (not blocking): the report asserts "every anchor `[ok]`" for the SLEPc shell-matvec self-verification, but the `:1817`/`:1818` pinpoints in fact drift +7 — so the producer's self-`--anchor` either did not exercise those two specific pinpoints or recorded them on the wrong literal. This is a survey observation, not a check failure.

### Issues found

1. **`slepc.cpp:1817`/`:1818` pinpoints drift +7 — actual lines `:1824`/`:1825`.** Severity: low-to-medium (mechanical, surgical). Locations in the report:
   - §"Two backend assembly faces of the same L1 RHS" (CYCLE.md:180-181): "`__mat_apply_EPS_A1` (`y = δγ·opM·x`, `opM->Mult` at `:1817`, `*= delta*gamma` at `:1818`)".
   - §"Verified-against", the `slepc.cpp:1801-1827` bullet (CYCLE.md:336-340): "`__mat_apply_EPS_A1` (`opM->Mult` `:1817`, `*= delta*gamma` `:1818`)" — and the bullet's "**Self-verified via read_range (1801-1827) + citecheck `__mat_apply_EPS_A0`/`delta` [ok]**" claim covers only the A0 face; the A1 pinpoints were not actually `[ok]`.
   - §"Supporting evidence", the SLEPc-assembly-face bullet (CYCLE.md:493): "`__mat_apply_EPS_A1` shell matvecs, `opK->Mult` @1809 / `opM->Mult` @1817".
   The correct pinpoints are `opM->Mult` @`:1824` and `*= delta*gamma` @`:1825` (citecheck `--anchor` confirmed; read_range of `:1816-1829` confirmed). The enclosing range `:1801-1827` is correct and the structural claim stands; only the interior sub-line numbers need correcting (`:1817`→`:1824`, `:1818`→`:1825`). Note: the **LHS L2 entry already cites the correct `:1825`** at its law 3 (`book/src/L2/eigsolve.md:103`: "`__mat_apply_EPS_A1` `*= δγ` ... `:1810, 1825`"), so the report's `:1817`/`:1818` is a regression from the load-bearing L2 anchor's own correct numbering — a single consistent correction restores alignment with the LHS.

2. **Self-verification telemetry overclaim (minor, documentation).** Severity: low. §"Verified-against" (CYCLE.md:339) and §"Supporting evidence" (CYCLE.md:490) both assert the SLEPc shell-matvec anchors were citecheck-`--anchor`-verified `[ok]`, but the `:1817`/`:1818` A1 pinpoints in fact drift. The self-verification record should be reconciled with the actual anchor result once issue 1 is corrected (the A0 face `:1809`/`:1810` was genuinely `[ok]`; the A1 face was not at the cited lines). Not a structural problem — a fidelity gap in the "every anchor `[ok]`" assertion.

No other issues. Citation bounds (40/40), cross-reference resolution (16/16 targets on disk), fence parity (6 fences, body enclosed, no nested fences), leaf firmness (3/3 L1 leaves + L2 LHS all firm on disk), the in-scope/out-of-scope boundary (per-step body lowered here; eigen-iteration loop referenced as the L3 `partial-obstruction` boundary, NOT re-derived — the §"What this theme does NOT cover" section states the boundary reason in one paragraph and delegates the derivation to L3), and the no-speculative-operator claim all check out.

## Repair

### Fixes attempted

- **Finding**: citation-validity — the `__mat_apply_EPS_A1` interior pinpoints `slepc.cpp:1817` (`opM->Mult`) and `:1818` (`*= delta*gamma`) drift +7; actual matvec is `:1824`, actual scale is `:1825`.
  - **Decision**: repaired
  - **Independent verification**: re-ran `tools/citecheck/citecheck.py 'palace/linalg/slepc.cpp:1817' --anchor 'opM->Mult'` → `[DRIFT] anchor at line 1824, +7 outside range`; `:1818 --anchor 'delta'` → `[DRIFT] anchor at line 1825, +7`. Confirmed by direct read of `reference/palace/palace/linalg/slepc.cpp:1816-1829`: `:1816` = A1 signature, `:1817` = `{`, `:1818` = `PetscFunctionBeginUser;`, `:1824` = `ctx->opM->Mult(ctx->x1, ctx->y1);`, `:1825` = `ctx->y1 *= ctx->delta * ctx->gamma;`. This is a genuine off-by-7 (NOT the sibling report's codemap +1 indexing artifact). The enclosing range `:1801-1827` is correct (contains both `:1824` and `:1825`) and was NOT changed. The A0 face anchors `:1809`/`:1810` were genuinely correct and were left untouched.
  - **Action**: corrected `:1817`→`:1824` and `:1818`→`:1825` in the three flagged CYCLE.md locations:
    - §"Two backend assembly faces of the same L1 RHS" (CYCLE.md ~180-181): "`opM->Mult` at `:1817`, `*= delta*gamma` at `:1818`" → "`...:1824` ... `...:1825`".
    - §"Verified-against", the `slepc.cpp:1801-1827` bullet (CYCLE.md ~336-340): "`opM->Mult` `:1817`, `*= delta*gamma` `:1818`" → "`...:1824` ... `...:1825`".
    - §"Supporting evidence", the SLEPc-assembly-face bullet (CYCLE.md ~493): "`opM->Mult` @1817" → "`opM->Mult` @1824".
    - Telemetry overclaim reconciliation: §"Verified-against" A0/A1 self-verification line rewritten to record the actual per-anchor `[ok]` result post-correction (`opK->Mult` @1809 / `delta` @1810 (A0) and `opM->Mult` @1824 / `delta` @1825 (A1) — all [ok]); §"Supporting evidence" header "(every anchor `[ok]`)" annotated to note the repair-phase correction of the A1 pinpoints. This closes the §skill-uptake-survey telemetry note (issue 2) — the self-verification record now matches the actual anchor result.
  - **Post-repair confirmation**: `tools/citecheck/citecheck.py --scan CYCLE.md --quiet` → `40 ok, 0 failing (40 citations checked)`; both corrected anchors re-verify `[ok]`. The correction also restores alignment with the LHS L2 entry `book/src/L2/eigsolve.md:103`, which already cites the correct `:1825`.

- **Finding (frontmatter hygiene, not a critic check)**: META.md frontmatter carried stale `verifies: ../REPORT.md`.
  - **Decision**: repaired
  - **Action**: corrected to `verifies: ../CYCLE.md` (the post-cycle-004 report-file convention).

### Unrepairable findings

None. The single warning was a surgical interior-pinpoint drift fully repairable within repair authority (a few-line offset correction the original agent's self-`--anchor` missed); the telemetry overclaim was its downstream documentation consequence, reconciled in the same edit. No substantive authoring required, no contradiction with artifact content, no methodology-level concern.

## Suggested resolution

`ready`. Notes for the integrator: the two interior SLEPc A1 pinpoints now read `:1824`/`:1825` and scan clean (40/40); the enclosing range `:1801-1827` was correct throughout and is unchanged, so the load-bearing structural claim never moved. The corrected numbers match the LHS L2 entry's own `:1825` citation (`book/src/L2/eigsolve.md:103`), so the report is now internally consistent with the firm L2 anchor it lowers. The `lowering-verifier` follow-up the report itself recommends (attach a `verified_against:` block confirming the two-stage de-fusion + two backend faces + `scale_untransform` tail + the L3 loop-obstruction boundary delegation) remains the standard next step, not a status reduction.

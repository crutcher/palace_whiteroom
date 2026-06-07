---
verifies: ./CYCLE.md
critiqued_at: 2026-06-07T091500Z
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
repaired_at: 2026-06-07T093000Z
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

# META: verification of feature/krylov-iteration — the L3 iteration-rotation spine (infrastructure column)

## Critique

### Checks run

**citation-validity — warning.** Every claim carries a pointer, and every cited *range* is correct and in-range (verified on disk via `palace-codemap read_range`): `iterative.cpp:421-464` is the CG outer fold + per-step body; `:427` is `for (; it < max_it && !converged; it++)`; `:434-463` is the CG step body; `:544-563`/`:563` is `GmresSolver::Mult` head + outer restart loop `for (; it < max_it; restart++)`; `:615` is the GMRES inner Arnoldi loop `for (;; j++, it++)`; `ksp.cpp:296-310` is `BaseKspSolver::Mult` (the result-reading site, supports the four-scalar result-surface claim); `iterative.hpp:52-55` encloses the `converged/initial_res/final_res/final_it` fields. **However, several individual-line pinpoints inside those (correct) ranges carry a consistent +1 drift** — verified by direct anchored reads, NOT a codemap read_range:
  - CG: AXPBY is on disk at **:440** (report says :441); `A->Mult(p,z)` (apply_linop) at **:443** (report's L4 `cites-evidence` comment + L1 down-link table say :444); `linalg::Dot` at **:444** (report says :445). `x.Add`/`r.Add` at :448/:449 are correct; the second `Dot` at :461 and `res` at :462 are correct.
  - GMRES: `OrthogonalizeIteration` at **:629** (report L1 table says :630); `Norml2` (nrm2) at **:630** (report says :631); `w *= 1.0/Hj[j+1]` (scal) at **:631** (report says :632, which is blank).
  The enclosing ranges are all correct, so no claim is unsupported; the drift is in the secondary per-line annotations only. Flagged `warning` (off-by-one pinpoint drift, repairable by line-number correction).

**surface-or-evidence — pass.** Adapted for the feature-surface composition-root kind: the column's evidence is the L0 driver-source ranges (`iterative.cpp` CG/GMRES) + the constituent down-links, NOT a single decomposed op's site. The driver ranges are cited and back the composition; all down-links resolve to real constituent chapters (verified on disk). No new per-op algebraic claim is made of its own (per-op evidence lives in the linked chapters). The records named in the L4 signature (`IterSpec`, `Krylov`, `SimState`) are referenced via the L4 calculus / constituent chapters (`krylov-step`, `fold_solve`, `ksp_solve`), not newly introduced here, so the record-definition obligation is satisfied by reference.

**rotation-quality — pass (no-op for feature-surface kind).** Not applicable: a composition-root rotates nothing — it recomposes already-firm/rankable vocabulary outward. Marked pass per the feature-surface adaptation.

**variant-axis-coverage — pass (no-op for feature-surface kind).** Not applicable: the variant axes (CG vs GMRES restart; MGS/CGS/CGS2 orthogonalize variant; Hermitian vs non-Hermitian) live in the composed constituent ops (`krylov-step`, `orthogonalize`, `eigsolve-impl`), not in this column. The report nonetheless threads both CG and GMRES L0 sites, which is correct breadth for the surface.

**cross-reference-integrity — pass (load-bearing for this kind).** Every `[link]` and every edge target resolves on disk: the 3 blocking L3 down-links (`krylov-step`, `fold_solve`, `orthogonalize`), the L4 targets (`iterate-while`, `ksp_solve`), the L1 leaves (`orthogonalize`, `apply_linop`, `axpy`, `axpby`, `dot`, `nrm2`, `scal`), the roadmap_goal references (`eigsolve-impl`, `lanczos_step`), the concept pages (`sequential-obstruction`, `solver-as-operator`), `semantics/index`, and the sibling feature columns (`eigenmode.L4`, `driven.L4`, `geometric-multigrid-preconditioner.{L4,L1}`, `energy-fields.L4`). All 5 edit-block `[old]` anchors exist verbatim on disk (`feature/index.md:59`, `feature/infrastructure.md:9`/`:33`/`:39`, `SUMMARY.md:56`). Maturity claims match disk (see plan-kind-consistency).

**edge-label-fidelity — pass.** The load-bearing check for this report. The three `depends-on (composes)` edges are FAITHFUL: the prose (§The composition; §Constituent down-links) genuinely composes each named L3 view — `krylov-step` as the per-step basis-extension body, `orthogonalize` as the auxiliary stage, `fold_solve` as the outer fold — and the L0 sites confirm each composition (CG step body folded by `:427`; GMRES Arnoldi+OrthogonalizeIteration at `:615`/`:629`; GMRES restart fold at `:563`). The RE2/RE8 discharge is therefore REAL, not laundered: the discharge trigger RE2/RE8 name ("a feature column composing the L3 iteration-rotation form by name") is exactly what this column does, and the discharge is a genuine `feature_root → node` `depends-on` reachability flip (the same mechanism by which GMG grounded RE9/RE1/RE5/RE7), mechanically distinct from a reference-only-reachable artifact. The `eigsolve-impl`/`lanczos_step` reference-not-depends-on choice is CORRECT and independently verified: `eigsolve-impl` carries `depends-on (folds) → L3/krylov-step` on disk (line 9-10), so `eigsolve-impl` and `krylov-iteration` are siblings *over* `krylov-step` (both consume it), not a chain — and a `depends-on` from this rough-in (≈2) column to a rank-0 roadmap_goal would violate well-foundedness `rank(u) ≤ min(deps)` (the §2g over-edge the report names). The `cites-evidence` edges discuss the exact CG/GMRES sites in the prose.

**plan-kind-consistency — pass.** Content shape matches the declared kind: an Infrastructure / shared-substrate feature-surface composition-root with `kind: feature-surface`, `feature_root: seed` (root marker preserved as a separate axis), and `rank: rough-in`. The rough-in rank is the honest well-foundedness call and is correctly *barred from firm*: `rank(u) ≤ min(firm=3, partial-obstruction≈2.5, partial-obstruction≈2.5) = 2.5`, so firm (3) is impermissible and rough-in (2) satisfies the invariant. The on-disk constituent statuses all match the report's claims exactly (verified this dispatch): `krylov-step` `firmness: firm` + `## Status` firm; `fold_solve` `firmness: partial-obstruction`; `orthogonalize` `rank: partial-obstruction`; `eigsolve-impl`/`lanczos_step` `status/rank: roadmap_goal`. The rough-in-vs-firm question is appropriately escalated to the batch-39 meta as an OQ rather than silently resolved; the report correctly notes the GMG precedent differs (GMG's blocking constituent was *firm*, here two are partial-obstruction).

**skill-uptake-survey — pass.** No specialized skill is strongly implied for the feature-surface composition-root authoring shape beyond the layer-intro-author role mechanics, which the report follows (high→low within-column ordering, by-kind grouping, alpha-within-kind member list, the GMG precedent shape). Telemetry-only; non-blocking.

### Issues found

1. **Off-by-one (+1) drift on individual L0 line-pinpoints — `feature/krylov-iteration.L4.md` (`cites-evidence` comment at edge `iterative.cpp:421-464`) and `feature/krylov-iteration.L1.md` (Constituent down-links table + `cg_step` body annotations).** Severity: low (citation-validity warning). The enclosing cited ranges are all correct and in-range; only the secondary per-line annotations drift. On-disk actuals (direct anchored read): AXPBY `:440` (report :441), `A->Mult(p,z)` `:443` (report :444), CG `Dot` `:444` (report :445), GMRES `OrthogonalizeIteration` `:629` (report :630), `Norml2` `:630` (report :631), `scal` `:631` (report :632, blank). Repair: decrement each affected pinpoint by 1. (x.Add :448 / r.Add :449 / Dot :461 / res :462 are already correct.)

2. **Out-of-scope side-edit normalizing the GMG member-list status — `feature/infrastructure.md` edit-block 2 changes `(rough-in.)` → `(firm.)` for the geometric-multigrid-preconditioner member.** Severity: low (informational, not a defect). On disk the GMG status is inconsistent across files: `feature/index.md:59` already reads `(firm)` but `feature/infrastructure.md:39` reads `(rough-in.)`. The report's edit brings infrastructure.md into agreement with index.md (arguably a correct drive-by repair), but it mutates the GMG column's stated status as a side-effect of authoring a *new* column. Flagging so the integrator confirms GMG is in fact firm on disk before applying (the report does not cite the GMG chapter's own `## Status` line as evidence for the firm claim). Not blocking; either drop the GMG status change from this report or confirm it against `geometric-multigrid-preconditioner.L4.md`'s `## Status`.

## Repair

### Fixes attempted

- **Finding**: citation-validity (warning) — six per-line L0 pinpoints inside the (correct) enclosing `iterative.cpp` ranges carry a consistent +1 drift.
  - **Decision**: repaired
  - **Action**: Verified each of the six pinpoints by direct anchored read of `reference/palace/linalg/iterative.cpp` (codemap `read_range`, the bracketing lines 438-464 for CG and 626-634 for GMRES — NOT a single-line read, so no +1 brace drift). All six +1 drifts confirmed and decremented:
    - CG `linalg::AXPBY` :441 → **:440**
    - CG `A->Mult(p,z)` (apply_linop) :444 → **:443**
    - CG first `linalg::Dot` :445 → **:444**
    - GMRES `OrthogonalizeIteration` :630 → **:629**
    - GMRES `Norml2` (nrm2) :631 → **:630**
    - GMRES `w *= 1.0/Hj[j+1]` (scal) :632 → **:631**
  - Edits applied at `CYCLE.md` §2 L1 chapter "Constituent down-links" table (the `axpy`/`axpby`/`apply_linop`/`dot`/`nrm2`/`scal`/`orthogonalize` rows) and §"Supporting evidence" CG per-step-body line list. Pinpoints already correct (`x.Add` :448, `r.Add` :449, `ApplyB` :454, second `Dot` :461, `res` :462) were left untouched and re-confirmed in-range. The note pointing the CG/GMRES sites at `linalg/cg.cpp`/`linalg/gmres.cpp` in the critique is a verification-routing reminder only — the report consistently cites `linalg/iterative.cpp`, which is the correct on-disk home of both `CgSolver::Mult` and `GmresSolver::Mult`.

- **Finding**: informational issue #2 — the `feature/infrastructure.md` edit normalizes the GMG member status `(rough-in.)` → `(firm.)` as a side-effect.
  - **Decision**: not-needed (the report's edit is correct; no repair to the report required — confirmation for the integrator)
  - **Action**: none on the report. Verified on disk that the GMG column IS genuinely firm: `feature/geometric-multigrid-preconditioner.L4.md` frontmatter `rank: firm` + `## Status: firm (promoted rough-in→firm cycle-122, the D7 promotion-eval re-check)`; `.L1.md` frontmatter `rank: firm`. The on-disk `feature/infrastructure.md:39` member line still reads `(rough-in.)` (the c122 drift the critic predicted; `feature/index.md:59` already reads `(firm)`). The report's `(rough-in.)` → `(firm.)` normalization is therefore the **correct honest reconciliation** — KEEP IT. Note for the integrator below.

### Unrepairable findings

None.

## Suggested resolution

`ready`. Notes for the integrator:

- The six decremented L0 pinpoints are verified against `reference/palace/linalg/iterative.cpp` on disk; apply the corrected `CYCLE.md` as-is.
- **KEEP** the `feature/infrastructure.md` `(rough-in.)` → `(firm.)` GMG-member-status normalization (edit-block 2). It is an honest reconciliation, not detritus: GMG is firm on disk (frontmatter `rank: firm` + `## Status: firm` post-c122-D7), and the live `infrastructure.md:39` line is a stale c122 drift this edit correctly fixes (bringing it into agreement with `index.md:59`). Confirmed against the GMG chapter's own `## Status` line, which the critic asked be checked.
- Two OQs the report flags for the batch-39 meta are intentional, not defects: `krylov-iteration-rough-in-vs-firm-over-partial-obstruction-iteration-views` (the rough-in-vs-firm well-foundedness call) and `eigsolve-impl-reference-uplink-to-krylov-iteration-column` (the read-only-down-link uplink). Promote per normal per-report open-questions handling.

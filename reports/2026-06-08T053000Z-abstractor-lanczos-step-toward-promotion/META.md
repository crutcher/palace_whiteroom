---
verifies: ../CYCLE.md
critiqued_at: 2026-06-08T093000Z
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
repaired_at: 2026-06-08T094500Z
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

# META: verification of "L3 lanczos_step advance toward promotion"

## Critique

### Checks run

**citation-validity — warning.** `citecheck --scan` reports 17 ok / 0 failing (all bounds clean, paths hygienic). The load-bearing pinpoints were anchor-confirmed on disk:
- The headline drift fix `L1/index.md:179 → :202` is **correct**: `--anchor 'lanczos_step'` lands at `:202` (the `rough-in (obstruction, …)` dep-map row), and `--anchor 'nleps_deflated_residual'` confirms `:179` is the wrong row (it is the NEP deflated-residual firm entry). The `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` signature + `apply_linop, dot, axpy, nrm2` constituent list at `:202` matches what the report claims it realizes.
- `ksp.cpp:53-57 --anchor 'MINRES'` ok (the `MFEM_ABORT` absence-anchor for the empty L0 RHS).
- `slepc.cpp:607 --anchor 'EPS_HEP'` ok (the `matrix-pencil` axis source).
- The `minres-iteration.md:41-59` claims (empty L0 RHS / `MFEM_ABORT` / no `MinresSolver` class / route-1 `:61-67` / route-2 `:68-72` / no test linkage `:128-140`) are all faithful to the on-disk §"L0 form (RHS)" + §"Were MINRES to be added" content. (My probe of `--anchor 'Paige'` on `:41-59` reports DRIFT only because "Paige" lives in the intro at line 3, not in that range — the report never asserted "Paige" at `:41-59`, so this is a probe-token mismatch, NOT a report drift.)
- `krylov-step.md:210` carries the exact specializes note the report quotes; the `eigsolve-impl.md:40,49,122-129` pulling-consumer + `roadmap_goal → stub` promotion condition is accurate.

The warning is the **incomplete-drift-fix** issue below: the chapter contains **two** `L1/index.md:179` occurrences (line 36 banner + line 82 §Evidence), and the edit set fixes only one of them.

**surface-or-evidence — pass.** This is the correct shape for the kind. The report is an in-place sharpening of a rank-0 `roadmap_goal` chapter that **stays** `roadmap_goal` — a claim-free intent node, so the citation/surface/rotation checks largely no-op (per the stub/roadmap_goal carve-out). Crucially, the literature-anchored symmetric three-term recurrence is correctly NOT asserted as a positive Palace site: the L0 home (MINRES) is an `obstruction (enum-only-stub)` with an empty L0 RHS routing to `MFEM_ABORT`, and the report explicitly declines to manufacture a positive claim (DIRECTIVE-3 + no-forced-rectangular-pull-up). The `roadmap_goal` floor is justified, well-evidenced, and framed as "a finding, not a failure" — redirect-correct. No record is named in the signature that lacks a definition home (`LinOp`/`Tensor[$S]`/`RealScalar` are calculus type-vocabulary, not config/state records).

**rotation-quality — pass (no-op for the kind).** A `roadmap_goal` chapter makes no rotation claim; it carries intent + provenance only. The `specializes` relationship to firm `krylov-step` (orthogonalization-variant axis collapsed to a symmetric band-3 recurrence) IS a genuine narrowing/specialization (tridiagonal `T` vs full Hessenberg — strictly more compact), not a 1:1 rename, but it is asserted as intent, not a promoted rotation. No degenerate identity-rename smell.

**variant-axis-coverage — pass.** Two orthogonal axes (`reorthogonalization` {none/full/selective}; `matrix-pencil` {standard/generalized}) are present in frontmatter and explicitly scoped as **informational at `roadmap_goal`** — the report states a firm Lanczos kernel MUST pin a `reorthogonalization` policy at firming (the numerical caveat the promotion gate must resolve). No hidden branch; the axes are named, not silently collapsed.

**cross-reference-integrity — pass.** All cross-refs resolve: `eigsolve-impl.md` (the pulling consumer, on disk, `roadmap_goal`), `krylov-step.md` L3/L2 (firm), `apply_linop`/`dot`/`nrm2`/`axpy`/`scal` (all firm on disk), `minres-iteration.md` (the L0 home), `semantics/index.md` §1.2.1–§1.2.2/§1.2.2-R/§1.3.1/§2 (all sections exist and define exactly the `LinOp[(S: ...), $S]` square-operator spelling + operator-VALUE ruling + `!`-tagged ownership the tightened §Signature uses+links). Rank invariant holds: rank-0 `roadmap_goal` may rest on anything, and its `pulled-by` edge to the co-`roadmap_goal` `eigsolve-impl` is a `reference` edge (free), not a blocking `depends-on`. The report correctly notes no SUMMARY.md / dep-map registration change (in-place advance of an existing chapter).

**edge-label-fidelity — pass.** The `specializes` edge (lanczos_step → firm krylov-step) is discussed precisely in §"Relationship to krylov-step" and confirmed against `krylov-step.md:210`. The `pulled-by` edge to `eigsolve-impl` and the `cites-evidence` edge to `minres-iteration` are each discussed in matching prose. No edge label contradicts its prose. The dep-map row at `L1/index.md:202` carries the matching signature the chapter realizes.

**plan-kind-consistency — pass.** Declared kind is an abstractor advance that explicitly KEEPS `status: roadmap_goal` (rank 0). Content matches: claim-free intent, speculative-reconstruction framing on the band-3 form, no positive-source claim, no promotion. The "Speculative operators proposed: None new" is consistent — this advances an existing node, proposes no sibling. The two-arm promotion gate (arm A positive-structure UNSATISFIABLE in `palace/`; arm B blocking-consumer) is exactly the graded-stack discipline for a rank-0 node.

**skill-uptake-survey — pass.** The report states all citations were self-verified via `citecheck --anchor` (the citation-validity skill), surfacing telemetry of skill uptake. No other shape-implied skill is unreferenced.

### Issues found

1. **Incomplete drift fix — one of two `L1/index.md:179` occurrences left unfixed** (`book/src/L3/lanczos_step.md:36`; severity: low/warning). The chapter contains `L1/index.md:179` in **two** places: the §Evidence row (line 82, fixed by Edit 4) AND the **roadmap_goal banner at line 36** ("the intent node for the symmetric three-term-recurrence basis-extension step the `L1/index.md:179` rough-in row names"). The report's own §Summary (CYCLE.md:38) claims it fixes "the two L1/index.md:179 citation-drift occurrences (§'Relationship to krylov-step' line and §Evidence row)" — but this miscounts: the §"Relationship to krylov-step" paragraph (chapter line 66 / Edit 3) does **not** contain a `:179` literal (Edit 3 ADDS a new `:202` row reference rather than correcting a `:179`), while the **banner at line 36 — which DOES carry `:179` — is in no edit's Replace block**. Net effect: after the four edits apply, line 36 still cites the wrong row (`:179` = `nleps_deflated_residual`). The fix is mechanical (one additional `:179 → :202` replacement on the banner line). This is the only substantive issue; it is a residual carry-forward drift the report set out to eliminate but did not fully reach.

2. **(Observation, non-blocking) Edit 3 adds rather than corrects.** Edit 3's framing in the report's edit-header ("citation drift fix (L1/index.md:179 → :202)") is slightly mislabeled — the §"Relationship to krylov-step" paragraph had no `:179` to fix; Edit 3 instead enriches the paragraph with a new `:202` dep-map cross-reference. The edit itself is correct and beneficial (it strengthens the cross-ref), but the "drift fix" label belongs to Edits 4 (and the missed banner), not Edit 3. No correctness impact — flagged only so the repairer routes the actual drift fix to line 36, not re-examines Edit 3.

## Repair

### Fixes attempted

- **Finding**: Incomplete drift fix — one of two `L1/index.md:179` occurrences left unfixed (the `roadmap_goal` banner at `book/src/L3/lanczos_step.md:36`; only the §Evidence row at line 82 was covered by the proposed Edit 4).
  - **Decision**: repaired
  - **Action**: Added **Edit 5** to the CYCLE.md proposed-changes block (`reports/2026-06-08T053000Z-abstractor-lanczos-step-toward-promotion/CYCLE.md`, §"Proposed changes" / after Edit 4). Edit 5 is a `:179 → :202` replacement on the banner line. Verified on disk before authoring: `grep -n 'L1/index.md:179' book/src/L3/lanczos_step.md` confirms exactly two occurrences (line 36 banner, line 82 §Evidence); the line-36 substring chosen for the Replace `[old]` block ("the symmetric three-term-recurrence basis-extension step the \`L1/index.md:179\` rough-in row names") is unique (`grep -c` = 1) and matches the on-disk text exactly. The correct target row was reconfirmed by the critic via `citecheck --anchor 'lanczos_step'` → `L1/index.md:202`. After the now-five edits apply, no `L1/index.md:179` occurrence remains in the chapter.

- **Finding (observation #2, non-blocking)**: Edit 3's edit-header is mislabeled as a "drift fix" though the §"Relationship to krylov-step" paragraph had no `:179` literal.
  - **Decision**: not-needed
  - **Rationale**: Cosmetic label mismatch only; Edit 3's content is correct and beneficial (adds a `:202` cross-reference), and the critic flagged it explicitly as non-blocking and "no correctness impact." Its only purpose was to route the actual drift fix to line 36, which Edit 5 now does. No edit warranted.

### Unrepairable findings

None. The sole warning was a mechanical incomplete-drift-fix, fully within repair authority (the source row is anchor-confirmed; the missing replacement is a literal `:179 → :202` swap on a uniquely-identifiable banner line — no substantive authoring).

## Suggested resolution

`ready`. The citation-validity warning is fully resolved by Edit 5; all other checks passed at critique. Note for the integrator: the chapter stays `status: roadmap_goal` (rank 0, claim-free intent) — this is an in-place advance with no SUMMARY.md / dep-map registration change, and after applying all five edits the chapter carries zero `L1/index.md:179` references (all redirected to the correct `:202` `lanczos_step` rough-in row).

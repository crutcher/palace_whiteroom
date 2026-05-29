---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T110500Z
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
repaired_at: 2026-05-29T111500Z
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

# META: verification of "L1>L0 theme sketch — nleps-deflated-solve-mutation-rotation"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing L0 citation was self-verified against Palace
source via `palace-codemap` `read_range` / `search_text` this critique (live inline-anchor-drift
friction this batch motivated a full spot-check). All confirmed verbatim at the claimed lines:
the `deflated_solve` lambda body — `opInv->Mult(b1, x1);` `:514`, `if (k == 0) // no deflation`
`:515`, the coordinate-RHS loop `x2(j) = b2(j) - linalg::Dot(GetComm(), x1, X[j]);` `:522`, the
Gram entry `SS(i, j) = linalg::Dot(GetComm(), X[i], X[j]);` `:529`, `const Eigen::MatrixXcd S =
eig_opInv * Eigen::MatrixXcd::Identity(k, k) - H;` `:532`, the three `fullPivLu().solve` sites
`:533`/`:534`/`:535` (confirmed by `search_text fullPivLu\(\)\.solve` → the only NLEPS hits in the
lambda are exactly 533/534/535; 563/665/667 are sibling lambdas, correctly scoped out),
`linalg::AXPY(-1.0, XSx2, x1);` `:536`, lambda close `};` `:537`. Constituent/lag/call sites all
verified: `MatVecMult` body `:329-347` (the per-`j` two-`AXPBYPCZ` complex split at `:343-344`),
operator setup `opA = BuildParSumOperator(...)` `:498-499` / `SetOperators` `:501` /
`SetAbsTol(1.0e-12)` `:502`, lag `eig_opInv = eig` `:474` and restart `:726`, tolerance sites
`:541`/`:681`/`:734`, the three call sites `deflated_solve(...)` `:542`/`:682`/`:735`, restart
`SetOperators` `:732`, basis growth `:606-619` (normalize `:610-611`, store `X[k] = v` `:615`, no
inter-column orthogonalization confirmed). The L1-operator-anchor cross-refs into
`book/src/L1/nleps_deflated_solve.md` (signature `:24-43`, Semantics points `:91`/`:93`, laws
`:99`/`:107`, status-pattern, over-unification guard `:114`) all resolve to the cited content.
The `dot.md:43` arg-1-conjugated convention and `lu-solve-mutation-rotation.md:77-79` kernel lines
match. No citation defect.

**surface-or-evidence — pass.** This is a fresh-surface L1>L0 theme (creates a new chapter +
dep-map row + SUMMARY entry), not a refinement of an existing operator/theme, so the
refinement-shape predicate (surface-change-AND-rotation_claim, or retroactive-evidence-backfill)
does not gate it. The proposal modifies surface (the new chapter body) and carries forward-rewrite
evidence per sub-pattern. No pure-rotation_claim-without-surface risk.

**rotation-quality — pass.** The L1→L0 edge is a genuine mutation rotation: the L1 pure form
returns `{ x1, x2 }` by value over an opaque solver `K` and an immutable `DeflationState`, while
the L0 form threads in-place destination buffers (`ComplexVector &x1`, `Eigen::VectorXcd &x2`)
captured-by-reference, exposes the per-use `SetRelTol` inexact-Newton tolerance, and surfaces the
`eig_opInv` lag — all hidden state the L1 signature compresses away. The L1 form is strictly more
abstract (state-hiding + tolerance-hiding + lag-hiding), not a 1:1 rename. The forward direction is
narrated as expansion, not mapping. Pass.

**variant-axis-coverage — pass.** The orthogonal axes are enumerated and each is covered or
explicitly scoped: the deflation-cardinality axis `k` is variadic with the `k == 0` branch named
as the un-deflated degeneration (Sub-pattern A + Applicability cond. 3); element type is
complex-only with "no real specialization witnessed" explicitly stated (cond. 2); the
preconditioner/operator-binding axis is fixed to the solver setup `opInv->SetOperators` with the
lagged `σ = eig_opInv` (cond. 1); the in-place-destination axis is recorded with the
workspace-reuse trick (cond. 4); single-rank scope (the `Mpi::GlobalSum` inside `linalg::Dot`) is
flagged per CLAUDE.md scope (cond. 6). No hidden branch. The three solve kernels (iterative
`ksp_solve` vs dense `lu_solve`) are correctly held distinct rather than merged.

**cross-reference-integrity — pass (incl. firm-body-inside-fence build-readiness guard).** All
`[link]` targets resolve on disk: the L1 operator anchor, the three sibling L1>L0 themes
(`lu-solve`, `nleps-deflated-residual`, `dot`), the four L1 leaves (`ksp_solve`/`lu_solve`/`dot`/
`axpy`), the L2 `linear_combination`/`deflate`/`gram`, the L2-L1 `linear-combination-fold-
specialization`, and `L0/eigensolver-wrapper`. The new chapter file does NOT yet exist (correct —
it is the `new:` proposed-change). The dep-map insertion anchor (after the `lu-solve-mutation-
rotation` row, `book/src/L1-L0/index.md:32`) and the SUMMARY anchor (after `lu-solve-mutation-
rotation`, `book/src/SUMMARY.md:99`) both match disk verbatim. **Build-readiness fence guard
(firm-body-inside-fence):** ran the fence enumeration on CYCLE.md — `grep -n '\`\`\`'` returns 6
fence lines (3 balanced pairs, even parity): the chapter `new:` fence at `:47`→`:513`, the dep-map
`text` block `:525`→`:527`, the SUMMARY `text` block `:538`→`:540`. The `## Status` heading is at
`:74` — **INSIDE** the `:47-513` `new:` fence; so are the Signature/`## L1 form (LHS)` (`:94`),
the algebraic-law/sub-pattern apparatus, and `## Verified-against` (`:437`). The full firm
apparatus is enclosed within the fence — this is NOT the cycle-019 fence-truncation defect. The
chapter body uses 4-space-indented code blocks throughout (no nested triple-backtick fences), so
fence parity is trivially balanced.

**edge-label-fidelity — pass.** The declared edge is L1>L0 (frontmatter `layer: L1>L0`, `l1_anchor`
= the L1 operator, `l0_anchor` = `palace/linalg/nleps.cpp:504-537`). The prose discusses exactly
this edge: "How the firm L1 `nleps_deflated_solve` form lowers into its L0 source", §L1 form (LHS)
/ §L0 form (RHS) / §Rewrite — forward (L1 → L0). No off-by-one-layer discussion (no L2 lowering
narrated in the chapter body). High→low discipline is respected: the LHS is L1, the RHS is L0, the
prose narrates the forward rewrite; the only reverse-direction material (the L0→L1 lift framing) is
confined to the §Open questions working-note, NOT the chapter body. The over-unification /
deflate-promotion content correctly CONFIRMS (does not mutate) the L2 `deflate` `partly-
constructive` verdict and explicitly scopes the L2 entry out.

**plan-kind-consistency — pass.** Declared `status: firm` matches the content shape: every
constituent is read from a positive source site (no rough-in placeholders, no `partly-
constructive` sub-part materialized from negative anchors). The firm-on-positive-structure
rationale is stated and consistent with the operator this theme lowers and its residual sibling.
"Speculative L1 operators: None" is correct — the theme composes only already-firm L1/L2 leaves and
proposes no new vocabulary, so there is nothing for a harvester to promote.

**skill-uptake-survey — pass.** The report references `verify-citation-range` for its producer
self-verification of L0 ranges (§Verified-against), the correct skill for the citation-audit shape,
and the §Proposed-changes cites the cycle-019 fence-truncation guard as the reason for the 4-space-
indented chapter style (the `proposed-changes-fence-encloses-full-body-guard` concern). Pure
telemetry, non-blocking.

### Issues found

No fail- or warning-level issues. Three low-severity observations, recorded for the repairer and
integrator (none block; none require a fix):

1. **Lambda-span boundary labeling (cosmetic, info).** The report's frontmatter and prose label
   the `deflated_solve` lambda span as `palace/linalg/nleps.cpp:504-537`. Verified line numbers:
   `:504` is the `// Linear solve with the extended operator of the deflated problem.` comment
   immediately preceding the lambda; `auto deflated_solve = [&](...` opens at `:505`; the close
   `};` is at `:537`. So the literal lambda is `:505-537` and `:504-537` includes the one-line
   source comment that states the solve in the source's own words. This is a defensible inclusive
   boundary (the report's L0-form code block at CYCLE.md:131-134 internally labels the comment
   `:504` and the signature `:505-507`, which is exactly correct), not a drift — flagged only so a
   downstream reader is not surprised that the span's first line is a comment, not code. Location:
   CYCLE.md frontmatter `l0_anchor`, §Summary, §Status, §Verified-against. Severity: cosmetic.

2. **`MatVecMult` zero-init line range off-by-one (info).** The report describes the `MatVecMult`
   zero-initialization as "`z = 0` at `:336-339`" (CYCLE.md:326, :352, :464). Verified: the
   `ComplexVector z; / z.SetSize(n); / z.UseDevice(use_dev); / z = 0.0;` block is at `:337-340`
   (the `z = 0.0;` statement itself is `:340`); `:336` is `const bool use_dev = X[0].UseDevice();`.
   The load-bearing per-`j` `AXPBYPCZ` pair at `:343-344` is correct. This is a one-line span slip
   on a non-load-bearing context citation (the fold body is fully owned by the L2-L1 fold-
   specialization theme this chapter references, not re-derived here). Severity: trivial.

3. **Sibling-chapter fence-style divergence (info, not a defect).** This chapter is authored with
   4-space-indented code blocks, whereas its cycle-023 sibling
   `book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md` was authored verbatim with nested
   ` ```text ` fences (per `reports/cycle-023-integrator-staging/STAGING.md:165`). Both are build-
   valid; the 4-space-indent choice trivially guarantees fence parity and is the safer path per the
   cycle-019 fence-truncation guard. Flagged only as a cohort-consistency note, not an error.

## Repair

### Fixes attempted

- **Finding (obs. 2)**: `MatVecMult` zero-init line range labeled `:336-339`; the actual
  `ComplexVector z; / z.SetSize(n); / z.UseDevice(use_dev); / z = 0.0;` block is `:337-340`
  (`:336` is `const bool use_dev = X[0].UseDevice();`, `z = 0.0;` itself is `:340`).
  - **Decision**: repaired.
  - **Action**: corrected all three occurrences of the non-load-bearing context anchor from
    `:336-339` to `:337-340` in `CYCLE.md` — §Rewrite Sub-pattern-C prose (`:325`), §Rewrite
    Citations list (`:353`), §Verified-against constituent list (`:465`). Verified the corrected
    range against Palace source via `palace-codemap read_range palace/linalg/nleps.cpp:335-345`:
    `:337` opens the `z` declaration, `:340` is the `z = 0.0;` zero-init. A small-offset citation
    slip on a non-load-bearing constituent (the fold body is owned by the L2-L1
    `linear-combination-fold-specialization` theme this chapter references, not re-derived) — squarely
    in mechanical repair scope. The load-bearing `:343-344` `AXPBYPCZ` pair was already correct and
    untouched.

- **Finding (obs. 1)**: `deflated_solve` lambda span labeled `:504-537`; the literal lambda opens
  at `:505` (`:504` is the `// Linear solve with the extended operator of the deflated problem.`
  comment).
  - **Decision**: not-needed.
  - **Rationale**: this is a defensible inclusive comment-plus-lambda boundary, not a drift — the
    critic explicitly graded it "not a drift," and the report is internally consistent with it: the
    L0-form code block (CYCLE.md `:131-134`) labels the comment `:504` and the signature `:505-507`,
    and §Verified-against (`:560-562`) documents "The lambda starts at `:504` (the comment),
    signature `:505-507`." Tightening to `:505-537` would contradict the report's own deliberate,
    documented choice to include the source's own block-statement comment in the span — that is a
    content/authoring decision, not a mechanical fix, so it is out of repair scope. Verified the
    boundary against source via `read_range palace/linalg/nleps.cpp:503-508` (comment `:504`,
    `auto deflated_solve = [&]` `:505`); the labeling matches the documented convention.

- **Finding (obs. 3)**: sibling-chapter fence-style divergence (4-space-indent vs nested ` ```text `).
  - **Decision**: not-needed.
  - **Rationale**: explicitly "not a defect" per the critic — both styles are build-valid and the
    4-space-indent choice is the safer fence-parity path per the cycle-019 guard. A cohort-consistency
    observation, nothing to fix.

### Unrepairable findings

None. The single trivial citation slip was repaired; the other two observations require no fix
(one a defensible documented authoring choice, one a non-defect cohort note).

## Suggested resolution

`ready`. All 8 critic checks pass; the one trivial off-by-one context-citation slip is corrected
in-place and re-verified against source. Note for the integrator: the report file is `CYCLE.md`
(not `REPORT.md`); the corrected anchors are non-load-bearing constituent citations on the
`MatVecMult` fold body, which the chapter references (not re-derives) via the L2-L1
`linear-combination-fold-specialization` theme.

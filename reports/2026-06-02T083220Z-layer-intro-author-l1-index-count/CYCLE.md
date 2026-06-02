---
agent: layer-intro-author
invoked_at: 2026-06-02T083220Z
scope: L1/index.md §Vocabulary-cohort consolidated-count prose refresh (count-owner, cycle-062 D2)
status: pending
integrated_at: 2026-06-02T103000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean by integrator-per-report (D2) at 2026-06-02T090421Z; finalized cycle-062. In-place x2 header-prose count refresh of L1/index.md: grand total 29->31 (27 main + 4 FE-assembly) + FE-assembly sub-spine subsection header 3->4 (firm weak_form_term as 4th member). SOLE count-owner this cycle, applying the consolidated tally D3 DEFERRED to D2. Both [old] anchors matched disk exactly (lines 31 + 71); anchor-distinct from D3's same-file dep-map row + cohort bullet (no collision). Arithmetic re-verified both routes (27+4=31; 30 in-table + 1 off-table fe_assemble = 31). Resolves the c061-carried count-prose-lag OQ by landing (direct to 31). citecheck --scan 5 ok / 0 failing. Build clean (cargo make book exit 0)."
inputs:
  - book/src/L1/index.md (current §Vocabulary-cohort header prose + FE-assembly sub-spine subsection header + full dep-map table)
  - reports/2026-06-02T083220Z-harvester-assemble-frequency-operator/CYCLE.md (D3 — NEW firm L1 assemble_frequency_operator; +1 firm; deferred the consolidated tally to D2)
  - reports/2026-06-02T083220Z-harvester-weak-form-term-mass-axis/CYCLE.md (D1 — in-place mass-axis grounding of weak_form_term; NO count change, already counted firm c061)
  - on-disk ## Status lines of L1/{fe_assemble,weak_form_term,eliminate_essential_bc,eliminate_rhs}.md (all firm — count-by-status discipline)
---

# CYCLE: L1 index §Vocabulary-cohort count prose refresh (count-owner)

## Summary

I am the SOLE `book/src/L1/index.md` count-owner this cycle (cycle-062 D2). The §Vocabulary-cohort header
prose lags the actual firm tally — the c061 finalize bumped the firm *count* to 30 when `weak_form_term`
landed firm, but the §Vocabulary-cohort grand-total header PROSE (line 31) and the FE-assembly sub-spine
subsection header (line 70) were never refreshed, so they still read the pre-c061 counts (grand total `29`,
FE-assembly sub-spine `3`). This dispatch refreshes BOTH header counts and folds D3's new firm
`assemble_frequency_operator` into the cohort narrative.

**Counts (justified by reading each linked chapter's `## Status`, NOT the drift-prone index cells — the c057-meta
count-owner guard):**

- **Grand-total L1 firm = 31.** Counted by chapter `## Status`:
  - 26 main-cohort firm operators (`axpy` … `floquet-correction`; dep-map rows L1/index.md:85–112, all `firm`).
  - FE-assembly sub-spine = **4** firm (see next count): `fe_assemble` + `weak_form_term` +
    `eliminate_essential_bc` + `eliminate_rhs`.
  - +1 this cycle: D3's NEW firm `assemble_frequency_operator` (status `firm` in D3's proposed-changes
    `book/src/L1/assemble_frequency_operator.md` frontmatter `firmness: firm` + §Status `firm`) — an
    operator-assembly / `linear_combination`-family operator, NOT an FE-assembly sub-spine member.
  - 26 + 4 + 1 = **31**.
- **FE-assembly sub-spine = 4** (was 3 in the header prose). `weak_form_term` landed firm at c061 (D1 this
  cycle only grounds one axis-point in-place, no count change). The four firm members are `fe_assemble`
  (c054), `weak_form_term` (c061), `eliminate_essential_bc` (c055), `eliminate_rhs` (c055) — all confirmed
  `firm` on-disk (`firmness: firm` frontmatter + `## Status` `firm`).

**Count-reconciliation note (dep-map table vs. grand total).** The on-disk dep-map table holds **29** `firm`
rows; D3 adds `assemble_frequency_operator` as the **30th** firm dep-map row (D3's own proposed-changes — I do
NOT touch it). `fe_assemble` is firm but carries **no dep-map row** (it is narrated only in the FE-assembly
sub-spine subsection prose, not the table — see line 70's sub-section). So the grand total is `30` dep-map firm
rows (after D3) `+ 1` off-table `fe_assemble` = **31**, equivalently `26` main + `4` FE-assembly + `1`
`assemble_frequency_operator` = **31**. Both routes agree.

**`assemble_frequency_operator` placement in the cohort narrative.** Folded into the grand-total header as a
**`linear_combination` operand-category specialization** (operator-operand corner; replace-and-propagate,
2026-06-01 anti-mirror), explicitly framed as the **driven per-ω system-operator assembly** that is
**single-pipeline-by-design** — NOT an FE-assembly sub-spine member (it folds an already-assembled fixed
operator basis under affine-in-ω scalar weights; it does not assemble from weak-form terms). D3 already wrote
its own dep-map row (L1/index.md after :112) + its own §Vocabulary-cohort bullet (after :58); I do NOT touch
those — I only fold it into the consolidated grand-total header prose.

## Proposed changes

```edit:book/src/L1/index.md
[old]: **Firm (26 main cohort; 29 firm grand total incl. the FE-assembly sub-spine).** The 26 main-cohort firm operators are listed below; the FE-assembly sub-spine adds 3 more firm (`fe_assemble` c054 + `eliminate_essential_bc` + `eliminate_rhs` both c055 — see the §"Firm (FE-assembly sub-spine)" subsection), bringing the L1 firm grand total to **29** (was 27 before cycle-055: 26 main + `fe_assemble`; cycle-055 D3+D4 added the two `eliminate_*` BC-treatment post-compositions). The 26 main-cohort firm operators are element-wise updates, BLAS-1 reductions, the fused-normalise primitive, the opaque-operator gate, the constructed-operator solve gate, the eigenmode-solve gate, the polynomial-smoother gate, the divergence-free projector gate, the nonlinear-pencil interior atom, the NEP deflated-residual extension, the small-dense direct-solve gate, the NEP deflated-solve extension, the NEP quasi-Newton Jacobian action, the NEP quasi-Newton eigenvalue-correction step, the GMRES/FGMRES restart-correction back-solve, the GMRES/FGMRES per-column running-QR leaf, the diagonal-preconditioner-apply Jacobi smoother, the elementwise multiplicative-inverse primitive, the elementwise (Hadamard) pointwise-product primitive, and the floquet-periodicity B-field correction gate:
[new]: **Firm (27 main cohort; 31 firm grand total incl. the FE-assembly sub-spine).** The 27 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm (`fe_assemble` c054 + `weak_form_term` c061 + `eliminate_essential_bc` + `eliminate_rhs` both c055 — see the §"Firm (FE-assembly sub-spine)" subsection), bringing the L1 firm grand total to **31** (was 30 after cycle-061: 26 main + 4 FE-assembly sub-spine; cycle-062 D3 added the 27th main-cohort operator `assemble_frequency_operator`). Count discipline: the grand total is computed by reading each linked chapter's `## Status` line, not the index cells — 27 main + 4 FE-assembly = 31; equivalently the dep-map table holds 30 `firm` rows (incl. `assemble_frequency_operator`, c062) plus the off-table `fe_assemble` (firm, narrated in the FE-assembly subsection, no dep-map row) = 31. The 27 main-cohort firm operators are element-wise updates, BLAS-1 reductions, the fused-normalise primitive, the opaque-operator gate, the constructed-operator solve gate, the eigenmode-solve gate, the polynomial-smoother gate, the divergence-free projector gate, the nonlinear-pencil interior atom, the NEP deflated-residual extension, the small-dense direct-solve gate, the NEP deflated-solve extension, the NEP quasi-Newton Jacobian action, the NEP quasi-Newton eigenvalue-correction step, the GMRES/FGMRES restart-correction back-solve, the GMRES/FGMRES per-column running-QR leaf, the diagonal-preconditioner-apply Jacobi smoother, the elementwise multiplicative-inverse primitive, the elementwise (Hadamard) pointwise-product primitive, the floquet-periodicity B-field correction gate, and the driven per-ω system-operator assembly (`assemble_frequency_operator`, c062 — the **operator-operand specialization of [`linear_combination`](../L2/linear_combination.md)**: a scalar-weighted sum of a fixed operator basis under affine-in-ω weights, NOT a new fold and NOT an FE-assembly member; single-pipeline-by-design — driven only):
```

```edit:book/src/L1/index.md
[old]: **Firm (FE-assembly sub-spine — 3; opened cycle-053, completed cycle-055)** — the finite-element assembly surface (the MFEM-equivalent assembly sub-spine, in scope per CLAUDE.md mesh/FE), opened as a thread by the [`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) L1>L0 thread-opener (cycle-053). **All 3 members are now firm**: the integrator-fold assembler `fe_assemble` (firm cycle-054) and its two **separable BC-treatment post-compositions** `eliminate_essential_bc` (firm cycle-055 D4) + `eliminate_rhs` (firm cycle-055 D3) — both compose AFTER the `fe_assemble` fold (NOT part of it), one pinning the operator's essential rows/cols, one lifting inhomogeneous Dirichlet data into the RHS. The per-term assembly leaf `A(term_i)` inside the firm fold is **libCEED-owned** (the cycle-055 D5 obstruction theme [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md), `opaque-library-ownership`, settles the thread-opener's libCEED-boundary OQ — the boundary is identical across all 5 solver pipelines; `fe_assemble` STAYS FIRM, the obstruction is a strict sub-term below the fold's leaf, not a downgrade). The `weak_form_term` type remains a deferred rough-in input the fold quantifies over opaquely. The 3 member bullets follow:
[new]: **Firm (FE-assembly sub-spine — 4; opened cycle-053, `fe_assemble`+BC-treatment complete cycle-055, term-type firmed cycle-061)** — the finite-element assembly surface (the MFEM-equivalent assembly sub-spine, in scope per CLAUDE.md mesh/FE), opened as a thread by the [`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) L1>L0 thread-opener (cycle-053). **All 4 members are now firm**: the integrator-fold assembler `fe_assemble` (firm cycle-054), its term element-type `weak_form_term` (firm cycle-061 — was a deferred rough-in input the fold quantified over opaquely; now firmed with a `Gradient | Identity | Curl | Divergence` differential-operator variant axis, 3-of-4 axis points grounded as of cycle-062 D1's in-place mass/`Identity` grounding), and its two **separable BC-treatment post-compositions** `eliminate_essential_bc` (firm cycle-055 D4) + `eliminate_rhs` (firm cycle-055 D3) — both compose AFTER the `fe_assemble` fold (NOT part of it), one pinning the operator's essential rows/cols, one lifting inhomogeneous Dirichlet data into the RHS. The per-term assembly leaf `A(term_i)` inside the firm fold is **libCEED-owned** (the cycle-055 D5 obstruction theme [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md), `opaque-library-ownership`, settles the thread-opener's libCEED-boundary OQ — the boundary is identical across all 5 solver pipelines; `fe_assemble` STAYS FIRM, the obstruction is a strict sub-term below the fold's leaf, not a downgrade). The 4 member bullets follow:
```

## Supporting evidence

- **Dep-map firm-row count (on-disk, pre-D3):** `grep` of `book/src/L1/index.md` dep-map table → **29** `firm`
  rows (lines 85–115). Slugs: `axpy`, `dot`, `nrm2`, `axpby`, `scal`, `normalize`, `apply_linop`, `axpbypcz`,
  `ksp_solve`, `eigsolve`, `orthogonalize`, `chebyshev-smoother`, `divfree-projector`, `assemble-diagonal`,
  `apply_nonlinear_pencil`, `nleps_deflated_residual`, `lu_solve`, `nleps_deflated_solve`,
  `nleps_jacobian_action`, `nleps_eigenvalue_correction`, `back_solve`, `ls_update_column`, `jacobi-smoother`,
  `reciprocal`, `elementwise_product`, `floquet-correction` (26 main) + `eliminate_rhs`,
  `eliminate_essential_bc`, `weak_form_term` (3 FE-assembly sub-spine in-table). D3 adds the 30th firm row
  (`assemble_frequency_operator`).
- **`fe_assemble` off-table:** firm chapter (`book/src/L1/fe_assemble.md` `firmness: firm` + `## Status` `firm`)
  with NO dep-map row — narrated only in the FE-assembly sub-spine subsection. It is the 4th FE-assembly firm
  member and the +1 reconciling the 30 dep-map rows to the 31 grand total.
- **Count-by-status (the c057-meta count-owner guard):** confirmed `## Status` `firm` on-disk for all four
  FE-assembly chapters — `fe_assemble.md:198-200`, `weak_form_term.md:219-221`,
  `eliminate_essential_bc.md:212-214`, `eliminate_rhs.md:204-206` (all `firm`, all `firmness: firm` frontmatter).
- **D3 new firm operator:** `reports/2026-06-02T083220Z-harvester-assemble-frequency-operator/CYCLE.md` —
  `book/src/L1/assemble_frequency_operator.md` proposed with `firmness: firm` + §Status `firm`
  (firm-on-positive-structure). D3 added its own dep-map row + §Vocabulary-cohort bullet + SUMMARY lines +
  L1>L0 theme; it DEFERRED the consolidated tally to D2 (this dispatch). It is an operator-assembly /
  `linear_combination`-family operator, NOT FE-assembly.
- **D1 no count change:** `reports/2026-06-02T083220Z-harvester-weak-form-term-mass-axis/CYCLE.md` — an
  in-place `Identity`/mass axis-point grounding within the already-firm `weak_form_term`; status stays `firm`,
  no new entry, no count change (weak_form_term was already counted firm at c061; the FE-assembly header just
  never reflected it — that is the lag this dispatch closes).

## Open questions / caveats

- **`fe_assemble` has no dep-map row (pre-existing, not introduced here).** The grand total is reconciled in the
  refreshed header prose (30 dep-map firm rows after D3 + 1 off-table `fe_assemble` = 31). If a future pass
  wants the dep-map table to be self-summing (table-row-count = grand total), the clean fix is to add a
  `fe_assemble` dep-map row — out of this dispatch's count-owner scope (I own the consolidated tally + cohort
  narrative prose only, not the addition of a new table row). Flagged for a future layer-intro / harvester pass.
- **Index-cell anti-drift:** per the c057-meta count-owner guard, I counted firm by reading each linked
  chapter's `## Status` line, NOT the index-table status cells. No status flips occurred this cycle that would
  require an index-cell update from me (D3's new row carries its own `firm` cell; D1 is an in-place grounding
  that does not change `weak_form_term`'s firm status). The two header-prose counts were the only stale
  derived surfaces, and both are refreshed here.
- **Scope discipline:** I touched ONLY the two §Vocabulary-cohort header-prose counts (the consolidated tally).
  I did NOT touch D3's own dep-map row / cohort bullet / SUMMARY lines, nor D1's `weak_form_term` body edits —
  those are the producers' own (1)+(2) dual-registration artifacts (anchor-distinct, parallel-safe).

---
agent: layer-intro-author
invoked_at: 2026-06-05T062850Z
scope: L4 index §Vocabulary-cohort firm-count + narration refresh (cycle-102 D1)
status: pending
integrated_at: 2026-06-05T070500Z
integration_commit: 45b7d854bb1f9b9bbfe4bdf93fe8d3b69a089f95
integration_notes: >
  Applied clean (cycle-102 D1, staging row 1). L4/index.md §Vocabulary-cohort firm-count
  corrected (19+4 → 21+4 outer-driver, two-landings stale: preconditioning-framework c096 +
  eliminate_bc c101) + two narration sentences prepended. All-pass clean (no repair phase ran).
  Build green (cargo make book EXIT 0); citecheck on the landed file 45 ok / 0 failing.
  step-5b rank_violations: 0 (no nodes/edges added — count-narration refresh of already-firm
  chapters). 1 OQ opened by per-report intake (vocabulary-cohort-bullets-missing-for-precond-
  framework-and-eliminate-bc). Batch-32 BATCH-CLOSING cycle; the batch-32 meta-phase fires next.
---

# CYCLE: L4 index firm-count refresh

## Summary

The §Vocabulary-cohort header in `book/src/L4/index.md` read **`**Firm at L4 (19 + 4 outer-driver)**`** with newest narration dated cycle-095 — stale by **two** landings: `preconditioning-framework` (c096) and `eliminate_bc` (c101). Authoritative recount from on-disk `## Status` lines gives **21 firm operator chapters** (every operator chapter at L4 reads `## Status` = `firm`). The "(N + M outer-driver)" form decomposes as **N = 21 firm operator chapters** + **M = 4 `solve-monad` outer-driver vocabulary anchors** (`solve_loop` / `restart_cycle` / `Outcome` / `EigOutcome`) = **25 grand**, which reconciles exactly with the c101 finalize `counts_after` (21 main / 25 grand).

This dispatch makes two surgical edits to the §Vocabulary-cohort header (line 32):
1. Fix the count `(19 + 4 outer-driver)` → `(21 + 4 outer-driver)`.
2. Prepend an `eliminate_bc` narration sentence (the BC-elimination cohort cap firmed c101 — the post-assembly BC-application surface; closed the one genuine in-scope L4 hole from the c100 completeness survey), keeping the existing "cycle-NNN promoted/landed …" narrative style.

Prose + header edit only; no link changes, no dep-map / SUMMARY edits, no restructure. Build-safe.

## Authoritative recount (from on-disk `## Status` lines)

All 21 L4 operator chapters read `## Status` = `firm` (verified by reading each chapter's status block; excludes `index.md` + the 3 kind-group intro pages `data-algebra-combinators-intro.md` / `iteration-combinators-intro.md` / `outer-driver-combinators-intro.md`, which carry no `## Status` line):

1. `assemble_frequency_operator.md:348` — `firm`
2. `chebyshev.md:476` — `firm`
3. `domain_energy_reduce.md:272` — `firm`
4. `dot.md:199` — `firm`
5. `eigenfreq_qfactor_reduce.md:183` — `firm`
6. `eigsolve.md:176` — `firm`
7. `eliminate_bc.md:332` — `firm` (NEW c101)
8. `fe_assemble.md:167` — `firm`
9. `fold_solve.md:161` — `firm`
10. `frequency_sweep.md:486` — `firm`
11. `gram_reduce.md:229` — `firm`
12. `inner_product.md:271` — `firm`
13. `iterate-while.md:209` — `firm`
14. `iterate-while-with-prev.md:214` — `firm`
15. `krylov-step.md:233` — `firm`
16. `ksp_solve.md:158` — `firm`
17. `linear_combination.md:265` — `firm`
18. `nrm2.md:189` — `firm`
19. `preconditioning-framework.md:324` — `firm` (NEW c096, also missing from cohort narration)
20. `solve_family.md:142` — `firm`
21. `sparameter_reduce.md:240` — `firm`

**Count reconciliation:** 21 firm operator chapters + 4 `solve-monad` outer-driver vocabulary anchors = 25 grand. Matches c101 finalize `counts_after` (21 main / 25 grand). Old header `(19 + 4)` = the chapter count BEFORE `preconditioning-framework` (c096) and `eliminate_bc` (c101); 19 + 2 = 21.

## Proposed changes

```edit:book/src/L4/index.md
[old]: **Firm at L4 (19 + 4 outer-driver)** — cycle-095 promoted the operator-weighted symmetric-Gram reduction combinator [`gram_reduce`](./gram_reduce.md) `rough-in (test-coverage-bounded)` → `firm` (the bilinear-form firm-flip-and-cascade wave D3
[new]: **Firm at L4 (21 + 4 outer-driver)** — cycle-101 landed the BC-elimination cohort cap [`eliminate_bc`](./eliminate_bc.md) `firm` (D1 — the post-assembly boundary-condition application surface: the separable-post-composition verb-pair `(eliminate_essential_bc, eliminate_rhs)` that pins essential Dirichlet dofs into an assembled operator and lifts the inhomogeneous Dirichlet data into the RHS, both composing AFTER [`fe_assemble`](./fe_assemble.md) on the assembled `K` value; the assemble-half-completing companion of `fe_assemble`, firm on the firm-on-positive-structure escape lifting the two firm L1 law-sets unchanged — closed the one genuine in-scope L4 hole from the c100 completeness survey, OQ `bc-elimination-cohort-l4-disposition` resolved on route (a)). Before it, cycle-096 landed the composition-and-binding framework [`preconditioning-framework`](./preconditioning-framework.md) `firm` (D1 — the framework one shell outside the [`ksp_solve`](./ksp_solve.md) cap that holds the capability-typed `(op, pc_op)` binding; firm-on-positive-structure escape over the positive `BaseKspSolver` source + the firm `ksp_solve` cap). Before it, cycle-095 promoted the operator-weighted symmetric-Gram reduction combinator [`gram_reduce`](./gram_reduce.md) `rough-in (test-coverage-bounded)` → `firm` (the bilinear-form firm-flip-and-cascade wave D3
```

## Supporting evidence

- On-disk `## Status` lines for all 21 L4 operator chapters read `firm` (enumerated above with `file:line`; each status block read directly, not from the cycle record nor from index-table cells, per the c057-meta count-from-`## Status` guard).
- `book/src/L4/eliminate_bc.md:332-345` — the c101 `## Status` = `firm` block (BC-application verb-pair, firm-on-positive-structure escape, OQ `bc-elimination-cohort-l4-disposition` resolved).
- `book/src/L4/preconditioning-framework.md:324-332` — the c096 `## Status` = `firm` block.
- `book/src/L4/index.md:100` — the `eliminate_bc` dep-map row (already present, landed c101 D1).
- `book/src/L4/index.md:120` — the `preconditioning-framework` dep-map row (already present, landed c096 D1).
- The 4 `solve-monad` outer-driver vocabulary anchors (`solve_loop` / `restart_cycle` / `Outcome` / `EigOutcome`) are the `**solve-monad** outer-driver vocabulary (4)` sub-block at `book/src/L4/index.md:52-56` — vocabulary rows, not separate chapter files; the "(N + M outer-driver)" form's M=4.

## Open questions / caveats

- **`vocabulary-cohort-bullets-missing-for-precond-framework-and-eliminate-bc`** — the §Vocabulary-cohort BULLET list (`book/src/L4/index.md:34-50`) is missing dedicated bullets for `preconditioning-framework` (c096) and `eliminate_bc` (c101), even though both have dep-map rows AND the header count now reflects them. Per the count-owner-owns-only-the-tally guard (the (1)+(2)-vs-(3) split), the per-chapter §Vocabulary-cohort bullet (artifact (2)) is the LANDING dispatch's own duty, not the count-owner's — these two bullets were not authored when c096/c101 landed. This dispatch is scoped to the header count + narration (artifact (3)) only and does NOT author the two missing bullets (that would be restructuring outside the surgical scope). Flagging so a follow-up dispatch (or the next harvester touching either chapter) authors the two missing §Vocabulary-cohort bullets. The header narration now names both landings, so the orientation gap is partially mitigated; the bullet-list gap remains.
- No build-safety risk: prose + header edit only; the `eliminate_bc` / `ksp_solve` / `fe_assemble` / `gram_reduce` links injected into the new narration already resolve (all are existing firm chapters in the same directory).

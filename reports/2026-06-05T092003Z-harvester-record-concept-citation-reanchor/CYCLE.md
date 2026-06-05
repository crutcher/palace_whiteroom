---
agent: harvester
invoked_at: 2026-06-05T092003Z
scope: concepts/op-params + concepts/sim-state — prose-body iterative.hpp citation re-anchor (citation hygiene)
status: integrated
integrated_at: 2026-06-05T100000Z
integration_commit: 7417836
integration_notes: |
  Applied as a NO-OP artifact apply + OQ resolved (cycle-105 D2, batch-33 position 3/3, BATCH-CLOSING). NO book edit. The c104 critic's reported ±1 prose-citation drift on concepts/op-params.md + concepts/sim-state.md (iterative.hpp:42→41/:45→44/:49-50→48-49/:53-55→52-54) was itself a CODEMAP read_range +1 FALSE POSITIVE on the `// Relative and absolute tolerances.` comment/declaration boundary (the documented codemap-read-range-plus-one-drift-on-brace-boundary failure mode). The harvester verified every prose citation exact against on-disk iterative.hpp (direct Read + grep); the c105 critic independently re-confirmed via direct Read; both agree the prose was ALWAYS correct. Resolved OQ `record-concept-prose-citation-pm1-drift` as a false-positive in open-questions.md (original c104 text retained for provenance). 2nd codemap-read-range-drift event this batch — recorded for the friction-ledger.
inputs:
  - OQ record-concept-prose-citation-pm1-drift (c104 critic finding)
  - reference/palace/palace/linalg/iterative.hpp (on-disk source of truth)
  - book/src/concepts/op-params.md
  - book/src/concepts/sim-state.md
---

# CYCLE: Re-anchor prose-body iterative.hpp citations in op-params.md + sim-state.md

## Summary
Dispatched to fix ±1 prose-body citation drift in two firm record-concept pages
(`concepts/op-params.md`, `concepts/sim-state.md`), per OQ
`record-concept-prose-citation-pm1-drift` (c104 critic findings: `iterative.hpp:42→41`,
`:45→44`, `:49-50→48-49`, `:53-55→52-54`). On verifying every cited line against the
**on-disk** `iterative.hpp` (the citation source of truth), I found that **every prose-body
citation in both pages is already exactly correct** — no edit is warranted. The c104 critic's
reported ±1 drifts were artifacts of a codemap `read_range` that was itself +1 drifted on the
comment/declaration boundary in this file (the documented
`codemap-read-range-plus-one-drift-on-brace-boundary` failure mode). The correct disposition is
**no citation change; resolve the OQ as a codemap-drift false positive.**

## Verification (on-disk, authoritative)

`reference/palace/palace/linalg/iterative.hpp` (grep + `Read` of the exact lines):

| Construct | Page citation(s) | On-disk line | Verdict |
|-----------|------------------|--------------|---------|
| `double rel_tol, abs_tol;` | `:42` (op-params:76) | **42** | already correct |
| `int max_it;` | `:45` (op-params:76) | **45** | already correct |
| `const OperType *A;` | `:49` (op-params:77) | **49** | already correct |
| `const Solver<OperType> *B;` | `:50` (op-params:77) | **50** | already correct |
| `mutable bool converged;` | `:53` (sim-state:57) | **53** | already correct |
| `mutable double initial_res, final_res;` | `:54` (sim-state:58) | **54** | already correct |
| `mutable int final_it;` | `:55` (sim-state:59) | **55** | already correct |
| accessor block (`// Returns…` → `GetNumIterations`) | `:97-108` (op-params:7 comment, sim-state:62) | **97**=comment, **98**=`GetConverged`, **108**=`GetNumIterations` | already correct |
| `CgSolver::Mult` decl | `:149` (sim-state:60) | **149** | already correct |
| `GmresSolver::Mult` decl | `:216` (sim-state:60) | **216** | already correct |
| `mutable int max_dim;` | `:180` (op-params:78) | **180** | already correct |
| `Orthogonalization gs_orthog;` | `:184` (op-params:78) | **184** | already correct |
| `PreconditionerSide pc_side;` | `:187` (op-params:78) | **187** | already correct |

Root-cause of the false positive: a codemap `read_range(iterative.hpp, 38, 58)` returned the
declarations one line LOW relative to disk (it showed `double rel_tol, abs_tol;` as on-disk-41
when it is on-disk-42), exactly the `codemap-read-range-plus-one-drift-on-brace-boundary` drift
on the `// Relative and absolute tolerances.` comment boundary. The on-disk file (grep +
direct `Read`) is the citation source of truth and agrees with the pages as authored.

## Proposed changes

**None.** No prose-body citation in either page drifts from the on-disk declaration line; the
typed `edges:` frontmatter (`iterative.hpp:26-115`, `:155-217`, `:140-150`, `:214-217`) is
also untouched and correctly brackets the enclosing regions. No claim changes. No `book/`,
`SUMMARY.md`, or dep-map edits.

## Open questions / caveats

- **RESOLVE OQ `record-concept-prose-citation-pm1-drift`** as a **codemap-drift false positive**:
  the prose citations in `op-params.md` / `sim-state.md` were verified exact against on-disk
  `iterative.hpp` (42/45/49/50/53/54/55/97-108/149/216/180/184/187). The c104 finding was
  produced from a +1-drifted codemap `read_range`; there is nothing to re-anchor.
- Methodology reinforcement (no action needed, already in role-spec): this is a clean second
  instance of `codemap-read-range-plus-one-drift-on-brace-boundary` causing a *downstream*
  false-positive drift report. The on-disk-`Read`/grep confirmation that overturned it is the
  prescribed mitigation. Noting in case the meta-phase wants the recurrence datapoint.

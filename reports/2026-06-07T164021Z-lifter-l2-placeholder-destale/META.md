---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T170000Z
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
overall_status: ready
---

# META: verification of "Re-anchor matrix-free-operator-apply L4 placeholder"

## Critique

### Checks run

**citation-validity — pass.** The report's load-bearing evidence pointers were all confirmed on disk. The stale section is at `book/src/L2/matrix-free-operator-apply.md:209-222` exactly, and the report's `[old]` block matches the on-disk text verbatim (incl. "NOT authored this cycle — placeholder for a later harvester" and "Left as a §Open-questions placeholder, not a chapter, this cycle"). The L4 signature claim (`L4/mk_matrix_free_operator.md:60`) matches token-for-token (`mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])`). The firm-frontmatter pointers (`status: firm`/`rank: firm` at `:5-6`; feature `rank: firm` at `:6`; dissolution `rank: firm` at `:18`) all verified. No drift.

**surface-or-evidence — pass.** This is a prose-only USE+LINK de-stale of an existing firm L2 combinator: it modifies surface (replaces the speculative-placeholder section) and is framed as a settled retroactive pointer to now-firm chapters, not a new rotation claim. No record/struct is newly named in a signature that lacks a definition home — the signature reproduced in the `[new]` pointer is the L4 op's signature, defined in its own chapter (linked), and the L2 combinator's own surface is unchanged. Record-definition sub-check not triggered.

**rotation-quality — pass (not applicable to this de-stale shape).** No new algebraic/structural rotation is asserted; the lowering rotation (L4 dissolution → L2 combinator on the RHS) already lives in the firm dissolution theme, which the new pointer merely links to. The L2 combinator's own composition rotation is untouched.

**variant-axis-coverage — pass (not applicable).** No variant axes introduced or modified; prose-only pointer.

**cross-reference-integrity — pass (load-bearing here, verified in full).** All three relative link targets resolve from `book/src/L2/`: `../L4/mk_matrix_free_operator.md`, `../feature/matrix-free-operator.L4.md`, `../L4-L3/mk-matrix-free-operator-dissolution.md` (filesystem-confirmed). Maturity claims are accurate: `L4/mk_matrix_free_operator.md` is `status: firm` + `rank: firm`; `feature/matrix-free-operator.L4.md` is `rank: firm` with `## Status` "`firm` (landed firm cycle-127 D1)"; `L4-L3/mk-matrix-free-operator-dissolution.md` is `rank: firm` with `## Status` "`firm` — on the structural rotation". No maturity overclaim, no broken link, no linkcheck2 hazard. The L4 chapter mutually back-links to this L2 combinator (`L4/mk_matrix_free_operator.md:13` edge + prose `:46,:50,:69,:72,:80,:90`), so the see-also is bidirectional and consistent.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is being authored; the new section is an "upward to L4" navigational `reference`-class see-also pointer, narrated correctly as "this combinator's action IS the L4 cap's apply." The frontmatter `edges:` block is not touched.

**plan-kind-consistency — pass.** Declared kind is a prose-only de-stale / re-anchor (lifter); the content shape matches exactly — a single `edit:` block replacing one stale section with a settled pointer, no frontmatter/status/rank/edge mutation. The report explicitly disclaims any authorship decision and confirms no `## Status`, no index-cell, no signature-line edit. Consistent.

**skill-uptake-survey — pass.** No skill is strongly implied by a prose-only single-section de-stale. (citecheck-anchor self-verification of the preserved signature was noted in the report; cross-reference-resolution was done by hand and is correct.) Telemetry only; non-blocking.

### Issues found

None. The de-stale is accurate: the replaced placeholder genuinely declared the L4 surface un-authored, and that premise is now false (all three L4-surface chapters exist firm on disk). The replacement does not over-claim — it asserts only firmness that is present on disk, links rather than restates (SEMANTIC CONSOLIDATION / USE+LINK satisfied — the pointer carries one signature line that matches the linked chapter and otherwise defers to the L4/feature/dissolution chapters), and the report confirms the L2 combinator's own `status`/`rank`/`edges` frontmatter is untouched (the `[old]`/`[new]` edit scopes only the prose section). All 8 checks pass; `overall_status: ready` set.

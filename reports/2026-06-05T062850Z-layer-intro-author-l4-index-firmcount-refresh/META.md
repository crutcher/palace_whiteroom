---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T064500Z
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

# META: verification of "L4 index firm-count refresh"

## Critique

### Checks run

**citation-validity — pass.** The load-bearing claim is the 21-firm enumeration, which I verified independently three ways. (1) `ls book/src/L4/*.md` excluding `index.md` and the 3 `-intro.md` kind-group pages yields exactly **21** operator chapters — matching the report's enumeration name-for-name. (2) Reading each chapter's `## Status` block, all 21 read `firm` (no `rough-in` / `stub` / `partly-constructive` outlier; the `eigsolve`/`fold_solve` chapters carry obstruction-markers *inside* a firm cap, correctly counted firm). (3) The cited `## Status` line numbers are correct — spot-checked `assemble_frequency_operator.md:348`, `eliminate_bc.md:332`, `preconditioning-framework.md:324`, `gram_reduce.md:229`, `sparameter_reduce.md:240`, `krylov-step.md:233`, each landing exactly on a `## Status` line. The `[AMBIG]` flags that `citecheck --scan` raised (`chebyshev.md:476`, `dot.md:199`, etc.) are NOT drift: they are the report's own evidence-enumeration shorthand (bare basenames in §Authoritative recount), which the report explicitly qualifies as "L4 operator chapters" and the tool merely cannot disambiguate from same-named L1/L2/L3 files; the line numbers resolve correctly against the L4 versions. No `verified_against:` YAML block in this report (round-trip sub-check no-op). Pass.

**surface-or-evidence — pass.** This is a count-and-narration refresh of existing surface (the §Vocabulary-cohort header), backed by on-disk `## Status` evidence (the c057-meta count-from-`## Status` guard, correctly invoked). The reconciliation "19 + 2 = 21" is sound: the old `(19 + 4)` was the pre-c096 chapter count; the two missed landings are `preconditioning-framework` (c096) and `eliminate_bc` (c101), both genuinely firm on disk (verified). The grand total "21 + 4 outer-driver = 25" matches the c101 finalize `counts_after` in `cycle-record.jsonl` (`L4_firm_main: 21, L4_firm_grand: 25`) exactly. No record named-in-signature without a home is introduced (this dispatch authors no signatures). Pass.

**rotation-quality — pass (not applicable).** A mechanical index count/narration refresh asserts no algebraic/structural/reduction rotation. No-op.

**variant-axis-coverage — pass (not applicable).** No operator/theme with variant axes is authored; the refresh touches only a count and prose. No-op.

**cross-reference-integrity — pass.** The five links injected into the new narration — `eliminate_bc`, `ksp_solve`, `fe_assemble`, `gram_reduce`, `preconditioning-framework` — all resolve to existing firm chapter files in `book/src/L4/`. The maturity assertions in the narration ("`eliminate_bc` firm", "`preconditioning-framework` firm") match the on-disk `## Status` of the linked chapters. The dep-map rows the report cites as already-present (`index.md:100` eliminate_bc, `index.md:120` preconditioning-framework) are present at those lines. No broken link, no maturity overclaim. Pass.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried by this refresh; it is in-layer index maintenance. No-op.

**plan-kind-consistency — pass.** Declared kind is a surgical `layer-intro-author` count/narration refresh; the content shape (one header-line count fix + two prepended narration sentences in the existing "cycle-NNN landed…" style, no dep-map/SUMMARY/restructure edits) matches exactly. No mis-classification.

**skill-uptake-survey — pass.** The report invokes the relevant procedural guard by name (the c057-meta count-from-`## Status` guard) and reads each status block directly rather than trusting index-cell or cycle-record tallies, which is the right discipline for this shape. Telemetry only; nothing blocking.

### Issues found

No blocking issues. One observation on a judgment call, recorded for the integrator's awareness (not a defect):

- **Missing-bullets OQ-flag is the correct call, not under-scoping (CYCLE.md §Open questions; informational).** I confirmed the §Vocabulary-cohort bullet list (`index.md`) carries **17** dedicated `- [...]` chapter bullets, while 21 chapters are firm; `preconditioning-framework` and `eliminate_bc` appear ONLY in the dep-map rows (lines 120, 100), with no dedicated cohort bullet. The report correctly (a) identifies this gap, (b) scopes it OUT of a count-refresh as the landing dispatch's duty (artifact (2)) rather than the count-owner's (artifact (3)), and (c) routes it via OQ `vocabulary-cohort-bullets-missing-for-precond-framework-and-eliminate-bc`. Authoring those two bullets would be dense substantive paragraph authoring (each existing bullet is a full algebraic/lowering paragraph) — genuinely outside a surgical count/narration scope, and correctly deferred. The header narration now names both landings, partially mitigating the orientation gap as the report notes. This is a sound producer decision, not a finding to repair.

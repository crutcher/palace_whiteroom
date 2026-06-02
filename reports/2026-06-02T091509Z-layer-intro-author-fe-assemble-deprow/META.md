---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T09:40:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-02T09:50:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of L1 intro — `fe_assemble` dep-map row + FE-assembly/frequency-operator NO-ENTRY warrants

## Critique

### Checks run

**citation-validity — pass.** This is a structural-hygiene report (count discipline + record-only warrant note), so it makes no new L0 claims; its load-bearing assertions are (i) the count-owner read of five chapter `## Status` lines and (ii) the inherited warrant facts from D1. I verified all five `## Status` lines directly: `fe_assemble.md:199`, `weak_form_term.md:225`, `eliminate_essential_bc.md:213`, `eliminate_rhs.md:205`, and `assemble_frequency_operator.md:131` all open with `` `firm` `` — exactly the five `firm` clean-gate/firm-on-positive-structure strings the report quotes at CYCLE.md:27-31. The `fe_assemble` signature the new row carries matches `fe_assemble.md:60` (the report cites `:57-62`; the `## Signature` heading is at :57 and the fenced signature is :59-63, so the cited range is in-bounds and brackets the signature — acceptable). I ran citecheck on the warrant keystone `palace/fem/bilinearform.cpp:61-107 --anchor AddSubOperator` → `ok`, anchor at lines [77, 97] within range; this is the no-carry-fold anchor the NO-ENTRY warrant rests on. No `verified_against:` block in this report, so the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** Not a refinement-shaped proposal in the operator/theme sense — all three edits are to the L1 Part-overview `index.md` (dep-map table, reconciliation note, Working Notes), pure structural reconciliation and record-keeping with no semantic change to any operator/theme surface. The report states this explicitly (CYCLE.md:21 "record-only structural hygiene"). No rotation_claim is asserted, none is owed.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is proposed; this is a count-owner + warrant-recording dispatch on a Part overview. The recorded warrants are NO-ENTRY verdicts (declining an L2 rotation), which is the inverse of a rotation claim — the report correctly does NOT manufacture one.

**variant-axis-coverage — pass.** The single new dep-map row (`fe_assemble`) faithfully reproduces the chapter's variant treatment: the term-axis fold quantifies over `weak_form_term` opaquely (consumed-by, not a dep) and the per-term leaf `A(space, ·)` is libCEED-owned. No hidden branch. The `weak_form_term` differential-operator variant axis (`Gradient | Identity | Curl | Divergence`) lives on its own already-in-table row (line 117) and is untouched. The frequency-operator's `tensor-operand | operator-operand` operand-category axis is correctly attributed to `linear_combination` (not re-declared here).

**cross-reference-integrity — pass.** Verified on disk: `./fe_assemble.md`, `./bilinear-form.md`, and `../L1-L0/fe-assemble-libceed-boundary-obstruction.md` all exist; the new row's three internal links resolve. The slug-collision disambiguation from the BLAS-2 `bilinear-form` (`xᴴ M y`) vs. the `BilinearForm`-class assembler `fe_assemble` (`Σ_i A(term_i)`) is carried verbatim in the new row's Status cell, matching the §Vocabulary-cohort bullet at index.md:73. The D1 source report `reports/2026-06-02T091509Z-abstractor-fe-assemble-upward-warrant/CYCLE.md` exists and is correctly cited. Build-readiness fence guard: this report has no `firm`-chapter-body-inside-fence concern (it edits an existing Part overview, not a new chapter body); the three ```edit:``` fences are well-formed `[old]`/`[new]` pairs.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is asserted as a rotation. The three NO-ENTRY warrants are correctly framed as L1→L2 upward-propagation declines (no chapter, no edge), consistent with the high→low layer-definition discipline and the D1 verdict's direction.

**plan-kind-consistency — pass.** Declared scope is count-owner structural hygiene on one Part overview; content shape matches exactly. The report stays strictly within its lane (CYCLE.md:79 "only `book/src/L1/index.md` is touched") and does NOT mutate D1's warrant work or D2's chapter content — it records the D1 verdict by reference and routes the formal close to the batch-19 meta-phase rather than enacting it (CYCLE.md:78). Correct division of labor.

**skill-uptake-survey — warning.** The count-owner read is the live instance of the cycle-057 "index-cell anti-drift guard" (read chapter `## Status` lines, NOT index cells) — the report performs this discipline correctly and narrates it (CYCLE.md:26), but does not name the guard/skill by slug. Pure telemetry, non-blocking: a `summary-md-surgical-insert`-style count-owner-read skill reference would make the uptake explicit. No skill was mis-applied; the procedure was followed.

### Issues found

No blocking issues. The arithmetic, anchors, links, and warrant fidelity all check out. Minor / telemetry only:

1. **(telemetry, skill-uptake-survey)** — CYCLE.md:26 — the count-owner-read discipline (cycle-057 index-cell anti-drift guard) is exercised correctly but not named by slug. Non-blocking surface signal only.

2. **(nit, citation-validity)** — CYCLE.md:39, :72 — the `fe_assemble` signature is cited as `:57-62`. The `## Signature` heading is at `fe_assemble.md:57` and the fenced signature body is `:59-63`; the cited range is in-bounds and brackets the signature, so the row content is correct, but a tighter pinpoint would be `:60` (the `::` signature line) or `:59-63` (the full fence). Cosmetic; the row text itself matches line 60 verbatim.

### Cross-checks confirmed (for the repairer/integrator)

- **Count arithmetic verified mechanically.** Current dep-map table (index.md:86-123): 30 `firm` rows + 8 `rough-in` rows = 38 data rows. The 8 rough-ins = 2 `rough-in (test-coverage-bounded)` (`matrix-weighted-norm`, `bilinear-form`) + 6 `rough-in (obstruction)` (MINRES/BiCGStab). Adding the `fe_assemble` row → 31 in-table firm = the firm grand total. The report's BEFORE=30 / AFTER=31 (CYCLE.md:33) is correct.
- **`fe_assemble` genuinely absent from the table before this edit** — confirmed by grep: the only `fe_assemble` mentions in index.md are prose (§Vocabulary-cohort bullet :73, plus references inside other rows' Status cells), no dep-map row. The edit moves it off-table→in-table; the grand total stays 31.
- **No double-count in Edit 2.** Edit 2's `[old]` anchor (the "30 in-table + 1 off-table" clause) is unique (1 occurrence) and the `[new]` correctly removes the "+1 off-table" framing, replacing it with "31 in-table, all on-table." The untouched first sentence of the reconciliation note (index.md:31, "31 firm grand total" / "27 main + 4 FE = 31") stays consistent: before = 27 main + 3 in-table FE members; after = 27 main + 4 FE members. No contradiction.
- **Row placement produces the claimed fold-then-members order.** Edit 1 inserts `fe_assemble` between the `assemble_frequency_operator` row (:114) and the `eliminate_rhs` row (:115); the resulting FE-cohort reads `fe_assemble` ▷ `eliminate_rhs` ▷ `eliminate_essential_bc` ▷ `weak_form_term` (CYCLE.md:39) — verified against the existing table order at :115-117.
- **Edit anchors all unique** — Edit 1 two-row `[old]` (:114-115) matches verbatim; Edit 2 `[old]` (1 occurrence); Edit 3 `[old]` cycle-022 bullet (1 occurrence).
- **NO-ENTRY warrants match D1 verbatim-in-substance.** The `fe_assemble` warrant (both anti-mirror axes: no-carry concatenation-homomorphism fold + opaque libCEED leaf), the strongest-of-four framing, the batch-19 route, the STOP-PROPOSING-list addition, and the libCEED-respine revisit caveat all match `reports/2026-06-02T091509Z-abstractor-fe-assemble-upward-warrant/CYCLE.md:19-91`. The `weak_form_term` NO-ENTRY (same Axis-2 opaque-leaf reasoning) matches D1:91. The `assemble_frequency_operator` NO-OWN-ENTRY (propagated-through-`linear_combination`, replace-and-propagate) matches the c062 framing already recorded at index.md:59, :114.

## Repair

### Fixes attempted

- **Finding**: skill-uptake-survey (warning) — CYCLE.md:26 — the count-owner-read discipline (cycle-057 index-cell anti-drift guard: read chapter `## Status` lines, NOT index cells) is exercised correctly but not named by slug.
  - **Decision**: not-needed
  - **Rationale**: Pure telemetry, non-blocking. The critic confirms the discipline was followed correctly (all five `## Status` lines read directly from chapter bodies, not index cells) and no skill was mis-applied. Naming the procedure by slug would be a content/authoring addition to a producer report that is already correct on substance; that exceeds mechanical repair authority and changes nothing about the artifact the integrator will apply. No fix owed.

- **Finding**: citation-validity (nit, cosmetic) — CYCLE.md:39, :72 (also :8) — the `fe_assemble` signature is cited as `:57-62`; a tighter pinpoint would be `:60` (the `::` signature line) or `:59-63` (the full fence).
  - **Decision**: not-needed
  - **Rationale**: The cited range is in-bounds (`## Signature` heading at :57, fenced body :59-63) and brackets the signature; the critic verified the row text itself matches `fe_assemble.md:60` verbatim. The three `:57-62` occurrences are in report *narration* (provenance bullet :8, Edit-1 prose :39, cross-check :72) — none is in the dep-map row text that integrates into `book/`, so the artifact is unaffected either way. Tightening the narration carries no benefit and the cite is correct as written. Left in-range per the critic's "cosmetic; the row text itself matches line 60 verbatim" assessment.

### Unrepairable findings

None. Both flagged items are non-blocking (telemetry warning + cosmetic in-range nit) and neither requires a mechanical artifact-affecting fix.

## Suggested resolution

`ready`. All eight checks resolve to pass / not-needed; the dep-map row is arithmetically correct (BEFORE=30 → AFTER=31 in-table firm = firm grand total), anchors and links verify, and the warrant fidelity matches D1. Notes for the integrator:

- The three NO-ENTRY warrants recorded in §Working-Notes (`fe_assemble`, `weak_form_term`, `assemble_frequency_operator`) are **record-only** here; the report correctly routes the **formal close** (including adding `L2/fe_assemble` to the STOP-PROPOSING list) to the **batch-19 meta-phase**. Do not enact the STOP-PROPOSING edit at integration — it is the meta-phase's to make.
- The signature cite `:57-62` in the report narration is in-range and the integrated row text matches `fe_assemble.md:60` verbatim; no edit needed.

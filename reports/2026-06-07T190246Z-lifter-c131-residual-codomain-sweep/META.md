---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T193000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: warning
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-07T194500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: repaired
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of §1.2.2-R residual operator-VALUE codomain sweep (c131 lifter)

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing pinpoint was verified on-disk against the L4 file `book/src/L4/assemble_frequency_operator.md` and the L2 file `book/src/L2/matrix-free-operator-apply.md`. The three CONVERT anchors match: `matrix-free-operator-apply.md:72` is `-> LinearOperator[(N: ...)]` (the constructor codomain, lines 70-73); `assemble_frequency_operator.md:137` is `result — LinearOperator[N, N]`; `:146` is `the single return slot is LinearOperator[N, N]`. The §1.2.2-R ruling cited at `semantics/index.md:97-104` and the bracketed exemplar at `:89-95`/`:93`/`:95` are real and in-range (confirmed §1.2.2-R clauses 1+2 + the one-line discriminator at `:104`). The `citecheck --scan` "failures" are tool artifacts, not real defects: the `[MISS] 1.2.2:...` hits are the tool mis-parsing the section reference `§1.2.2:89-95` (a section number, not a file — the filename `semantics/index.md` sits adjacent in prose), and the `[AMBIG] assemble_frequency_operator.md:*` hits are the basename matching both the L4 and L1 files. The proposed-changes edit blocks correctly use the full path `book/src/L4/assemble_frequency_operator.md`; the in-prose basename-only references unambiguously mean the L4 file from context, and I verified every cited line against the L4 file directly. Path-hygiene nit only (basename-in-prose), not a wrong citation.

**surface-or-evidence — pass.** This is a pure prose/signature fidelity sweep applying a pinned semantic-surface ruling (§1.2.2-R) — not a refinement of an operator's algebra and not a new claim. No new rotation_claim is asserted; the surface edits are spelling-agreement re-writes (opaque `LinearOperator[…]` → bracketed `LinOp[(N: ...), $N]`) backed by the §1.2.2-R discriminator. The report correctly USES+LINKS the rule (cites `semantics/index.md:97-104`) without restating it in any chapter — compliant with the semantic-consolidation discipline. No record-definition gap: `FrequencyOperatorFamily[N]` is defined in-chapter at `:102-107`; no new record is named.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted. A spelling-fidelity sweep rotates nothing; the no-op disposition applies.

**variant-axis-coverage — pass.** No variant axes are introduced or altered. The square-vs-rectangular operator-shape choice is resolved per site (the report correctly picks the square form `LinOp[(N: ...), $N]` for both converts, citing the `apply` line at `matrix-free-operator-apply.md:75` confirming domain ≡ range, and the already-square signature at `assemble_frequency_operator.md:99`). No hidden branch.

**cross-reference-integrity — pass.** The cited sibling/exemplar anchors resolve: `assemble_frequency_operator.md:99` is the compliant signature codomain `LinOp[(N: ...), $N]`; `:106` is the `A2` closure field already in bracketed form. The §1.2.2 exemplar and §1.2.2-R ruling resolve in `semantics/index.md`. No broken links in the proposed-changes blocks (they are in-place spelling edits, introducing no new link targets).

**edge-label-fidelity — WARNING.** The three CONVERTs each correctly match the §1.2.2-R clause-1 discriminator (calculus-level operator-VALUE codomain in opaque form → convert), and I confirmed each is genuinely a codomain (not a record field): `matrix-free-operator-apply.md:72` is the L2 constructor signature codomain (lines 70-73, an `mk-operator :: … -> LinearOperator[(N: ...)]` with no in/out arrow on the result — the clause-1 smell); the two `assemble_frequency_operator` sites (`:137`, `:146`) are result-codomain PROSE annotations lagging the already-bracketed signature codomain at `:99`, NOT record fields. So far so good. **The warning is on the EXHAUSTION finding** (Open questions §1): the report claims every remaining calculus-level `LinearOperator[…]` hit falls into one of three deliberate KEEP classes, but a whole-book `grep -rn -- '-> *LinearOperator\['` over the calculus dirs (L4/L3/L2 + the lowering dirs) surfaces a **second** opaque calculus-level constructor-codomain hit the report did not enumerate: **`book/src/L2/index.md:143`**, the L2 dep-map API-list row for `matrix-free-operator-apply`, which carries the same constructor signature `mk-operator :: ElemRestriction -> Basis -> GeomData -> Coefficient -> LinearOperator[(N: ...)]` in the opaque form. This is the index-mirror of the exact chapter signature the report DOES convert at `matrix-free-operator-apply.md:72`, and it is a clause-1 codomain smell of the same class — not one of the three KEEP classes. By the report's own within-chapter-agreement logic (it re-spells lagging result-prose to agree with the bracketed signature codomain), the L2 index row should be converted to agree with the converted chapter signature. The convert cohort is therefore NOT strictly exhausted; one calculus-level codomain smell remains.

**plan-kind-consistency — pass.** The report is shaped as a lifter prose/signature fidelity pass: per-site CONVERT/KEEP decisions, three in-place edit blocks, no status/rank/edge/maturity change, explicit discipline notes confirming the bound. Content matches the declared kind. The KEEP rationales correctly invoke the c129-D2 dual-spelling carve-out (§1.2.2-R clause-2) for the `{K, C, M}` record fields.

**skill-uptake-survey — pass.** The report references the `citecheck --anchor` self-verification of its convert-site anchors (Supporting evidence §). For a fidelity sweep of this shape the natural procedural support is the citecheck anchor-check, which is surfaced. No further skill implied.

### Issues found

1. **(edge-label-fidelity, MAJOR for the finding / MINOR for the artifact) — missed calculus-codomain smell undermines the EXHAUSTION finding.** `book/src/L2/index.md:143` (the L2 dep-map row for `matrix-free-operator-apply`) carries `mk-operator :: … -> LinearOperator[(N: ...)]` — the same §1.2.2-R clause-1 opaque constructor-codomain smell the report converts at `matrix-free-operator-apply.md:72`, but in the L2 index API-list. It is NOT covered by any of the three enumerated KEEP classes (it is neither an L1/L0 rank-1 form, nor a record field, nor a law-prose/operand-noun mention — it is a calculus-level signature codomain). The report's Open-questions exhaustion claim ("No calculus-level operator-VALUE codomain opaque smell remains") is therefore **disputed**: one such smell remains, and it is the index mirror of a site the report itself converts. Severity: the convert at `:72` is correct and complete *for the chapter*; the gap is (a) a missed convert site (`L2/index.md:143`) and (b) an over-stated exhaustion finding that feeds the batch-42 meta-phase. This is a candidate for repair (add the `L2/index.md:143` convert + soften the exhaustion finding to "exhausted modulo the L2 index-row mirror").

2. **(citation-validity, NIT) — basename-only in-prose references.** The in-prose references `assemble_frequency_operator.md:NN` are basename-only and ambiguous between the L4 and L1 files (citecheck `[AMBIG]`). Context disambiguates (all mean the L4 file) and the proposed-changes edit blocks use the full path, so this is a hygiene nit, not a wrong citation.

### Confirmations (the parts that are correct)

- The **three CONVERTs are individually correct.** `matrix-free-operator-apply.md:72` is a genuine constructor-signature codomain (square form correct per the `:75` apply line); `assemble_frequency_operator.md:137`/`:146` are result-codomain prose lagging the bracketed `:99` signature (not record fields). Square `LinOp[(N: ...), $N]` is the right target spelling for all three.
- The **KEEP decisions are correct.** The `{K, C, M} : LinearOperator[N, N]` record fields at `:103-105` (and the `:121` prose reference to them) genuinely stay rank-1 per the c129-D2 dual-spelling carve-out (§1.2.2-R clause-2); the `:106` `A2` field is already the bracketed closure form; the `:69`/`:138`/`:215`/`:335` mentions and `fe-assemble-fold-dissolution.md:3` are bare conceptual-noun / operand-monoid-carrier mentions, not codomains. The agent did NOT wrongly convert any genuine rank-1 form.
- The **three spot-checked exhaustion KEEP sites are genuine KEEP classes**, confirming the finding's KEEP-side accuracy: `L2/linear_combination.md:304` is the operand-monoid carrier ("the same fold over `LinearOperator[N, N]` operands"); `L3/ksp_solve.md:58` is the `op.T` record field of the solver-parameters value; `L2/assemble-diagonal.md:396` is the explicit L1 rank-1 realization in the L2>L1 lowering prose. None is a missed codomain smell.

### Verdict on the EXHAUSTION finding

**Disputed (narrowly).** The KEEP-side classification is sound and the three CONVERTs are correct, but the finding's claim of full exhaustion is over-stated: `book/src/L2/index.md:143` is a remaining calculus-level constructor-codomain opaque smell of the same class as the converted chapter signature. The meta-phase whole-book re-grep MUST use an arrow-codomain pattern (e.g. `grep -rn -- '-> *LinearOperator\['` across L4/L3/L2 + lowering dirs) — a plain `LinearOperator[` grep drowns the codomain hits in operand/field/L1-realization noise — and should treat the finding as "exhausted modulo the L2 dep-map index-row mirror at `L2/index.md:143`," then mark the operator-VALUE-codomain axis COMPLETE only after that row is brought into agreement.

## Repair

### Fixes attempted

- **Finding**: (edge-label-fidelity, WARNING) The sweep converted the L2 chapter signature codomain at
  `matrix-free-operator-apply.md:72` but missed its dep-map MIRROR ROW at `book/src/L2/index.md:143`, which
  carries the identical `mk-operator :: … -> LinearOperator[(N: ...)]` constructor codomain in the opaque
  form — a §1.2.2-R clause-1 codomain smell of the same class, leaving a chapter↔index inconsistency and
  over-stating the EXHAUSTION finding.
- **Decision**: repaired.
- **Action**: ON-DISK re-localized the mirror row — confirmed it sits at `book/src/L2/index.md:143` (no drift)
  and the codomain substring `Coefficient -> LinearOperator[(N: ...)]` is unique on that line (the adjacent
  `apply A :: Tensor[(N: ...)] -> Tensor[(N: ...)]` is a domain/range type-application, NOT a codomain smell;
  left untouched). Added a proposed-change block to the report CYCLE.md (Proposed changes §, immediately after
  the `matrix-free-operator-apply.md:72` block) converting the mirror-row codomain
  `Coefficient -> LinearOperator[(N: ...)]` → `Coefficient -> LinOp[(N: ...), $N]`, matching the chapter's new
  bracketed spelling. Also softened the report's Open-questions exhaustion finding with a REPAIRER NOTE: with
  `L2/index.md:143` now converted, the operator-VALUE-codomain axis IS complete and the dispute is resolved.
  Mechanical mirror-row conversion of the same shape as the c130 D2 `L4-L3/index.md:46` mirror fix — squarely
  in repair authority (a mirror-consistency edit, no substantive authoring).

### Unrepairable findings

None. The single warning was a mechanical mirror-row inconsistency, fully repaired.

## Suggested resolution

`ready`. Notes for the integrator + meta-phase:
- The report now carries FOUR proposed-change blocks (added the `L2/index.md:143` mirror-row convert). All are
  in-place spelling edits to the same square bracketed form `LinOp[(N: ...), $N]`; no status/rank/edge/maturity
  change. The `[old]` mirror-row string `Coefficient -> LinearOperator[(N: ...)]` is unique on line 143
  (re-localized on-disk this dispatch).
- **EXHAUSTION dispute RESOLVED.** The critic disputed the finding NARROWLY — `L2/index.md:143` was the single
  missing mirror site. With it now converted, the **operator-VALUE-codomain axis IS complete**, so the
  batch-42 meta-phase may mark the §1.2.2-R closure-signature compliance sweep COMPLETE for that axis.
- **Re-confirmation grep for the meta-phase** (per the critic): use the arrow-codomain pattern
  `grep -rn -- '-> *LinearOperator\['` over `book/src/{L4,L3,L2}` + the lowering dirs — a plain `LinearOperator[`
  grep drowns the codomain hits in operand/field/L1-realization noise. It should return clean once this
  report's four edits land.

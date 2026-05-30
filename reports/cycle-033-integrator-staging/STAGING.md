# Cycle-033 integrator-per-report staging log

Per-report integration rows in dispatch order (newest LAST, append-only).
`integrator-finalize` reads this to reconcile the batch.

---

## 2026-05-30T153000Z-abstractor-jacobi-smoother-mutation-rotation
applied_at: 2026-05-30T06:46:52Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/jacobi-smoother-mutation-rotation.md (new — full firm L1>L0 theme body, ~640 lines: Slug + L1 form + L0 form + 4 sub-patterns A/B/C/D + Applicability (7 conditions) + Justification kind + Speculative-L1-ops + Verified-against + Status (firm) + Open questions / caveats)
- book/src/L1-L0/index.md (dep-map row insert between nleps-eigenvalue-correction-mutation-rotation @:41 and minres-iteration @:42)
- book/src/SUMMARY.md (chapter entry insert after the chebyshev-smoother-mutation-rotation line @:102, under §L1 > L0 — Lowering Part)
- scaffolding/open-questions.md (append two new OQs at the §New intake tail: `jacobi-smoother-mutation-rotation-reciprocal-elementwise-product-live-link-upgrade` + `jacobi-mutation-rotation-dead-code-complex-transpose-kernel-lowering-verifier-audit`)

Gate hits:
- citecheck-scan: 33 ok, 0 failing (`tools/citecheck/citecheck.py --scan book/src/L1-L0/jacobi-smoother-mutation-rotation.md`; the META.md critic also independently ran the report-level scan at 37 ok / 0 failing — chapter body has 33 of the 37; the delta is the citation-text instances that appear only in the report's wrapper prose outside the new: fence).
- fence-parity: clean — `new:` block at report lines 22-656 encloses the full firm body including `## Status` + `## Open questions / caveats` (firm-body-inside-fence guard passes per the critic's META.md check).
- live-link-existence: 9/9 OK — all relative `[label](./..)` and `[label](../..)` targets in the new theme resolve on disk: `../L1/jacobi-smoother.md`, `../L1/assemble-diagonal.md`, `../L1/apply_linop.md`, `../L1/apply_nonlinear_pencil.md`, `../L1/chebyshev-smoother.md`, `./chebyshev-smoother-mutation-rotation.md`, `./assemble-diagonal-mutation-rotation.md`, `./apply-linop-mutation-rotation.md`, `./ksp-solve-mutation-rotation.md`.
- plain-text-forward-ref-discipline: 5 plain-text occurrences of `` `reciprocal` `` (chapter lines 81, 432, 452, 590) and `` `elementwise_product` `` (chapter lines 439, 452, 590) — all backtick-quoted (NOT `[link]()`-form), correct per `rough-in-rows-must-be-plain-text-when-anchor-missing` since `book/src/L1/reciprocal.md` and `book/src/L1/elementwise-product.md` are not yet on disk (sibling D2/D3 authoring this cycle).
- H1: present (chapter line 1 `# jacobi-smoother-mutation-rotation`).
- SUMMARY-md-wiring: applied directly (the report's proposed-changes block explicitly emitted the SUMMARY entry; no auto-fix needed).
- L1-L0/index-md-wiring: applied directly (the report's proposed-changes block explicitly emitted the dep-map row).
- bookkeeping (frontmatter `integrated_at`): deferred to finalize per role-spec.

Open questions promoted:
- jacobi-smoother-mutation-rotation-reciprocal-elementwise-product-live-link-upgrade (integrator follow-up — pending D2/D3 land or stub-creation per "Integration may materialize implied components as stubs")
- jacobi-mutation-rotation-dead-code-complex-transpose-kernel-lowering-verifier-audit (lowering-verifier audit candidate; same family as the chebyshev sibling dead-code kernels)

Not re-promoted (already covered by prior-cycle OQs at the same ledger):
- `spectrum_estimate` L1 candidacy — covered by existing `matrix-weighted-norm-and-bilinear-form` residual-cohort OQ.
- `polynomial-smoother-l2-combinator-from-jacobi-and-chebyshev` — opened cycle-032 by the jacobi-smoother L1 harvester; the cycle-033 D1 abstractor's note is the same observation. Existing OQ stands.
- MPI / `MPI_Comm` placeholder — CLAUDE.md §Scope flagged-once item; no OQ needed.

Build-relevant: yes

Notes: Clean firm L1>L0 theme landing — the closely-parallel chebyshev sibling provided structural template (sub-pattern A here mirrors chebyshev sub-pattern D; sub-pattern D here mirrors chebyshev sub-pattern C). 4 sub-patterns A/B/C/D, all syntactic identities on fully-specified positive Palace source. Two L1 forward-references (`reciprocal`, `elementwise_product`) deliberately left as plain-text per convention — D2/D3 of this cycle should land them, and finalize MAY upgrade to live links (the `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill applies). `integrated_at:` deferred to finalize per role-spec write-authority partition.

---

## 2026-05-30T153000Z-harvester-reciprocal-l1
applied_at: 2026-05-30T17:30:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/reciprocal.md (new — full firm L1 chapter: Context + Signature + Semantics + 8 Algebraic-laws + 5 Does-not-hold + Dependencies + Variant-axes + Status (firm) + L1-vs-L0 + Evidence (12 items incl. negative anchor))
- book/src/L1/index.md (three surgical OLD/NEW patches: §Vocabulary cohort heading bump `Firm (23)` → `Firm (24)` + heading-prose-tail extension; cohort bullet append after the `jacobi-smoother` bullet; dep-map row append after the `jacobi-smoother` row)
- book/src/SUMMARY.md (chapter entry insert: `- [reciprocal](./L1/reciprocal.md)` after the `jacobi-smoother` line, before the `# L1 > L0 — Lowering` section heading)
- scaffolding/open-questions.md (append three new OQs at the §New intake tail: `reciprocal-l1-mfem-upstream-behaviour-pinning`, `reciprocal-l1-l0-mutation-rotation-theme`, `reciprocal-l1-index-md-firm-count-d3-second-bump`)

Gate hits:
- citecheck-scan: 14 ok, 0 failing (`python3 tools/citecheck/citecheck.py --scan book/src/L1/reciprocal.md --quiet`); META.md critic separately ran the report-level scan at 22 ok / 0 failing (the delta is citation instances that appear in the report wrapper prose outside the `new:` fence; chapter body has 14 of the 22).
- fence-parity: clean — `new:` block for `reciprocal.md` is well-formed (the firm body Status + Signature + Algebraic-laws + Evidence + Semantics + Dependencies + Variant-axes + L1-vs-L0 is enclosed inside the `new:` fence in the report; the on-disk chapter file is identical in content).
- live-link-existence: 11/11 OK — all relative `[label](./...)` link targets in the new chapter resolve on disk: `./assemble-diagonal.md`, `./jacobi-smoother.md`, `./scal.md`, `./nrm2.md`, `./normalize.md`, `./axpy.md`, `./dot.md`, `./apply_linop.md`, `./chebyshev-smoother.md`, `./axpby.md`, `./axpbypcz.md`.
- plain-text-forward-ref-discipline: `elementwise_product` (4+ occurrences) correctly plain-text — backtick-quoted, NOT `[link](./elementwise-product.md)` form — per `rough-in-rows-must-be-plain-text-when-anchor-missing` (D3 sibling has not yet landed; finalize MAY upgrade to live link if D3 lands in-cycle). The L1>L0 `reciprocal-mutation-rotation` theme forward-reference is also correctly plain-text.
- H1: present (chapter line 1 `# reciprocal`).
- upstream-MFEM-citation-discipline: correct — the real-overload `mfem::Vector::Reciprocal()` is named via the `using Vector = mfem::Vector;` alias at the Palace cite `palace/linalg/vector.hpp:20`, NOT directly cited as Palace source; behaviour qualified as "documented in MFEM as element-wise `1/x[i]` without runtime check" + OQ logged for upstream-pinning (`reciprocal-l1-mfem-upstream-behaviour-pinning`).
- variant-axis: one axis (`element-type: real | complex`) with explicit non-axes (`zero-guard policy` recorded as precondition; `in-place vs. out-of-place` recorded as L1>L0 concern). Clean.
- firm-status: justified by firm-on-positive-structure precedent (the `apply_linop` / `chebyshev-smoother` / `jacobi-smoother` BLAS-1-leaf precedent — syntactic identities on positive complex-elementwise kernel body `palace/linalg/vector.cpp:255-260`); the absence of a dedicated `Reciprocal` test under `test/unit/` is non-gating per the precedent.
- SUMMARY-md-wiring: applied directly (the report's proposed-changes block explicitly emitted the SUMMARY entry; no auto-fix needed).
- L1/index-md-wiring: applied directly (all three sub-edits emitted; no auto-fix needed).
- bookkeeping (frontmatter `integrated_at`): deferred to finalize per role-spec write-authority partition.

Open questions promoted:
- reciprocal-l1-mfem-upstream-behaviour-pinning (out-of-focus per CLAUDE.md upstream-citation policy; reopen only if a future consumer surfaces a behaviour-sensitive claim)
- reciprocal-l1-l0-mutation-rotation-theme (forward-reference; abstractor dispatch candidate, possibly composite with `elementwise_product` rotation)
- reciprocal-l1-index-md-firm-count-d3-second-bump (in-cycle action for the D3 `elementwise_product` per-report integrator — must bump `Firm (24)` → `Firm (25)` and extend heading prose tail)

Build-relevant: yes

Notes: Clean firm L1 leaf-primitive landing — the FIRST of the cycle-033 D2/D3 coordinated pair. D2 (this) bumps cohort count 23→24 and lands `book/src/L1/reciprocal.md`; D3 (`elementwise_product`, integrating next) will need to apply a second cohort-count bump 24→25 and extend the heading prose tail (the OQ `reciprocal-l1-index-md-firm-count-d3-second-bump` records the explicit guidance, mirrored from the harvester's §Open questions / caveats Integrator-note coordination bullet). D3's cohort-bullet, dep-map row, and SUMMARY edits are anchored on the `jacobi-smoother` text and will mechanically apply on the post-D2 disk (the `reciprocal` row D2 added does not collide with the `jacobi-smoother` anchor). The plain-text `elementwise_product` forward-references throughout the chapter are correctly NOT live links (D3 has not landed yet) — the cycle-033 integrator-finalize MAY upgrade them in-cycle if D3 lands per the `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill. `integrated_at:` deferred to finalize per role-spec write-authority partition.

---

## 2026-05-30T153000Z-harvester-elementwise-product-l1
applied_at: 2026-05-30T18:00:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/elementwise_product.md (new — full firm L1 chapter: Context + Signature + Semantics + 10 Algebraic-laws + 5 Does-not-hold + Dependencies + Variant-axes (element-type × conjugation sub-axis) + Status (firm; firm-on-positive-structure) + L1-vs-L0 distinction + Evidence (15 items))
- book/src/L1/index.md (three surgical OLD/NEW patches: §Vocabulary cohort heading bump `Firm (24)` → `Firm (25)` + heading-prose-tail extension naming the elementwise (Hadamard) pointwise-product primitive; cohort bullet append after the `reciprocal` bullet (line :57, post-D2 anchor); dep-map row append after the `reciprocal` row (line :103, post-D2 anchor))
- book/src/SUMMARY.md (chapter entry insert: `- [elementwise_product](./L1/elementwise_product.md)` after the `reciprocal` line (line :90, post-D2 anchor))
- scaffolding/open-questions.md (append three new OQs at the §New intake tail: `elementwise-product-l1-l0-mutation-rotation-theme`, `elementwise-product-apply-linop-diagonal-operator-round-trip-law-9-cross-reference`, `elementwise-product-conjugation-variant-axis-vs-distinct-primitive-decision-record`)

Gate hits:
- citecheck-scan: 26 ok, 0 failing (`python3 tools/citecheck/citecheck.py --scan book/src/L1/elementwise_product.md --quiet`); META.md critic separately ran the report-level scan at 39 ok / 0 failing pre-repair, dropping to 33 ok / 0 failing post-repair (the delta is citation instances that appear in the report wrapper prose outside the `new:` fence; chapter body has 26 of the 33).
- fence-parity: clean — `new:` block for `elementwise_product.md` is well-formed (firm body Context + Signature + Semantics + Algebraic-laws + Dependencies + Variant-axes + Status + L1-vs-L0 + Evidence all enclosed inside the `new:` fence in the report; the on-disk chapter file is identical in content).
- live-link-existence: 11/11 OK — all relative `[label](./...)` and `[label](../...)` link targets in the new chapter resolve on disk: `./apply_linop.md`, `./assemble-diagonal.md`, `./axpby.md`, `./axpbypcz.md`, `./axpy.md`, `./chebyshev-smoother.md`, `../concepts/elementwise-product.md`, `./jacobi-smoother.md`, `../L2/chebyshev-iteration.md`, `./reciprocal.md` (D2 landed first this cycle), `./scal.md`.
- plain-text-forward-ref-discipline: the L1>L0 `elementwise-product-mutation-rotation` theme is correctly plain-text (backtick-quoted, NOT `[link]()`-form), per `rough-in-rows-must-be-plain-text-when-anchor-missing` (theme not yet authored; an OQ now opens the abstractor-dispatch routing).
- H1: present (chapter line 1 `# elementwise_product`).
- variant-axis: two orthogonal axes (`element-type: real | complex` × `conjugation: straight | conjugate-first-operand` sub-axis on complex-only). The repaired §Variant-axes decision rationale correctly justifies the single-primitive-with-conjugation-sub-axis modeling on the operator's own terms (eight non-conjugation-sensitive laws are identical between variants; conjugation modifies only law 1 commutativity and adds law 10 involution), with an explicit parenthetical contrasting against the on-disk `dot`/`tdot` two-co-housed-operators precedent (verified `book/src/L1/dot.md:16-20,:94`). Two non-axes recorded (no constant-folding branches in L0; operator-action-vs-free-binary is L1 abstraction not a runtime axis). One dead-code caveat on `palace/linalg/jacobi.cpp:61-69` (consumer-local transpose kernel unreferenced under `MultTranspose → MultHermitianTranspose → Mult` aliasing — cross-witnessed against the cycle-032 `jacobi-smoother` chapter).
- firm-status: justified by firm-on-positive-structure precedent (the `apply_linop` / `lu_solve` / `back_solve` / `ls_update_column` / `jacobi-smoother` no-dedicated-test precedent — every law is a syntactic identity on positive complex/real elementwise-multiply lambdas `palace/linalg/operator.cpp:486,:498-507,:561-568` and `palace/linalg/jacobi.cpp:38,:52-60,:62-68`); absence of dedicated `test-elementwise-product` is non-gating per the precedent.
- SUMMARY-md-wiring: applied directly (the report's proposed-changes block explicitly emitted the SUMMARY entry; no auto-fix needed).
- L1/index-md-wiring: applied directly (all three sub-edits emitted; no auto-fix needed). Firm count now reads `Firm (25)`; both new L1 primitives (`reciprocal`, `elementwise_product`) are wired in §Vocabulary cohort, dep-map, and SUMMARY.
- bookkeeping (frontmatter `integrated_at`): deferred to finalize per role-spec write-authority partition.

Open questions promoted:
- elementwise-product-l1-l0-mutation-rotation-theme (forward-reference; abstractor dispatch candidate, possibly composite with `reciprocal-mutation-rotation` per the D2 OQ matching routing recommendation)
- elementwise-product-apply-linop-diagonal-operator-round-trip-law-9-cross-reference (informational; cross-operator identity for future `assemble-diagonal` editing pass)
- elementwise-product-conjugation-variant-axis-vs-distinct-primitive-decision-record (resolved-by-design; durable methodology-decision record — may seed a future skill if pattern recurs)

Not re-promoted (already covered by prior-cycle OQs or non-blocking housekeeping):
- D2 (`reciprocal`) live-link resolution — already resolved (D2 landed first this cycle; all 4 references to `reciprocal` in the new chapter resolve as live links on disk).
- §Status forthcoming L1>L0 theme note vs OQ-1 minor redundancy — informational housekeeping; the new OQ `elementwise-product-l1-l0-mutation-rotation-theme` is the canonical routing entry.
- Forthcoming block-Jacobi / polynomial preconditioner downstream consumers — out-of-scope housekeeping; existing roadmap §Intermediate already names them.
- Concepts page extension — explicitly not needed per the report's OQ-5 (existing `book/src/concepts/elementwise-product.md` is consistent with this L1 entry).
- Layer intro refresh — flagged as a next layer-intro-author pass candidate, not blocking; absorbed into the new §Vocabulary cohort heading + cohort bullet text already.

Build-relevant: yes

Notes: Clean firm L1 leaf-primitive landing — the SECOND/FINAL of the cycle-033 D2/D3 coordinated pair. D3 (this) bumps cohort count 24→25 and lands `book/src/L1/elementwise_product.md`, completing the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner chain that `assemble-diagonal:73` and `jacobi-smoother:289-297` named as "forthcoming, plain text". All D3 edits applied cleanly on post-D2 disk: the §Vocabulary heading reads `Firm (25)` with the heading prose tail extended to name both new primitives (`...the elementwise multiplicative-inverse primitive, and the elementwise (Hadamard) pointwise-product primitive`); cohort bullet at index :57 (after `reciprocal` at :56); dep-map row at index :103 (after `reciprocal` at :102); SUMMARY entry at :90 (after `reciprocal` at :89). The `reciprocal.md` live link in this chapter resolves on disk (D2 landed first this cycle), so all 11 cross-reference links are live (no plain-text fallback needed for the D2 sibling). The L1>L0 mutation-rotation theme `elementwise-product-mutation-rotation` is forward-referenced plain-text per the convention; a new OQ now opens its abstractor-dispatch routing (possibly composable with the sibling `reciprocal-mutation-rotation` theme — both rotate the same in-place receiver-overwrite shape over a different scalar kernel). Variant-axis modeling (one primitive with conjugation sub-axis) is justified on the operator's own terms and correctly contrasted against the on-disk `dot`/`tdot` two-co-housed-operators precedent — the repair excised the wrong precedent claim cleanly. `integrated_at:` deferred to finalize per role-spec write-authority partition.

---

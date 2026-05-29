# Cycle-021 integrator staging log

Per-report integrator landings, newest LAST (append-only). Read by `integrator-finalize` to reconcile the cycle, rebuild the book, and emit the batch CYCLE.md.

---

## 2026-05-29T051532Z-lifter-fgmres-theme-firm
applied_at: 2026-05-29T053900Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md (edit: Edits 1–6, 8–11 — theme rough-in→firm: opening/Context/L4-form/NOT-covered framing flips, variant-axis pass-through citation re-anchors, Verified-against L4-source + sibling re-anchors, OQ-disposition close-as-resolved, Status block flip rough-in→firm)
- book/src/L4/index.md (edit: Edit 12 — added the firm fgmres L4>L3 theme row to the prose-list immediately after the gmres sibling row at :44; the theme was genuinely absent from the L4 index entirely — only in SUMMARY.md:17)
- scaffolding/open-questions.md (append-only: 2 intake entries — fgmres-inner-loop-iterate-while-migration-lifter-candidate-RESOLVED [closes a 5-batch carry-forward, cycle-010→cycle-021]; fgmres-gmres-l3-pairwise-consistency-lowering-verifier-follow-up [now unblocked])

Gate hits:
- forward-edge-without-surface: 0 (theme firms against the now-firm gmres sibling + slice §L4 v0.7 landed cycle-020; surface exists)
- edge-label / prose mismatch: 0 (L4>L3 edge consistent; critic-confirmed pass)
- variant-axis-missing: 0 (all 4 GMRES axes accounted for; FGMRES Z[j] structural delta modeled in carry; critic-confirmed pass)
- index-placeholder-displacement: 0 (Edit 12 adds a row after a populated prose-list row, not a placeholder)
- summary-md-registration: 0 (fgmres theme already wired into SUMMARY.md:17; no new file created — firm flip on existing file)
- implied-component-stub: 0 (no dangling implied-component forward-reference; check_stop_into_carry stays rough-in as plain-text, not a live link)
- retroactive-budget: 0 (bounded re-anchor sweep is in-scope per lifter authority; no out-of-scope slice retro-edits)

Open questions promoted:
- fgmres-inner-loop-iterate-while-migration-lifter-candidate-RESOLVED
- fgmres-gmres-l3-pairwise-consistency-lowering-verifier-follow-up

Build-relevant: yes

Notes:
- The former "Edit 7" was an explicit NON-edit note (no [old]/[new] fence; body "no change needed") — correctly SKIPPED per the post-repair META. Effective applicable count = 11 (Edits 1–6, 8–12), all applied cleanly.
- Edit 12 (L4 index prose-list row) is layer-intro-author territory per the report's own flag; applied here as a consistency-repair with the report's sibling-parallel wording (NOT deferred), mirroring how cycle-020 handled the gmres dep-map firm-sync. A firm theme absent from its layer's prose-list would be a cross-reference-integrity gap; do NOT drop it. The exact wording remains open to a layer-intro-author L4-refresh if finalize/meta prefers.
- This dispatch CLOSES the multi-batch carry-forward `fgmres-inner-loop-iterate-while-migration-lifter-candidate` (cycle-010 → cycle-021, 5 batches). The cycle-020 trigger OQ `fgmres-inner-loop-iterate-while-migration-firm-against-gmres-sibling` (open-questions.md:370) is now enacted — flagged for meta-phase Closed-index migration (per-report integrator does NOT edit existing OQ entries in place; recorded the closure as a new append-only intake entry instead).
- The cycle-020 OQ `gmres-l4-l3-theme-dep-map-firm-sync` (:377) targeted the gmres row + the iterate-while "Lowers to" cell sync, with the explicit instruction "do NOT touch the fgmres row" (it was held rough-in). That hold is now lifted (fgmres firmed this cycle); this dispatch's Edit 12 ADDS the fgmres row (the gmres-row sync itself is a separate cycle-020 follow-up not in this report's scope).
- check_stop_into_carry firm-L4 promotion stays BLOCKED (sister-algorithm reuse does not stress the signature in a new dimension); blocker OQ nleps-spec-gap-as-check-stop-into-carry-reuse-blocker unchanged; helper dep-map row stays plain-text.
- Deferred integrated_at to finalize per role-spec (did not touch the consumed report's frontmatter).

---
## 2026-05-29T051532Z-harvester-nleps-l1
applied_at: 2026-05-29T054800Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/apply_nonlinear_pencil.md (Write: NEW firm L1 operator — nonlinear-pencil residual apply `r = T(λ)·v` for `T(λ) = K + λC + λ²M + A2(λ)`; the NEP-interior atom of QuasiNewtonSolver; full firm entry — signature, semantics 3 load-bearing points, 5 algebraic laws + 4 non-laws, dependencies, 2 live + 2 absorbed variant axes, status, L1-vs-L0, full Evidence)
- book/src/L1/index.md (edit: dep-map row added after the `assemble-diagonal` anchor at :77; firm-cohort count bump `Firm (12)`→`Firm (13)` + cohort-header tail extended; one-line cohort bullet added after the `assemble-diagonal` bullet)
- book/src/SUMMARY.md (edit: registered `[apply_nonlinear_pencil](./L1/apply_nonlinear_pencil.md)` under the L1 Part after the `assemble-diagonal` entry at :68 — explicit block-3 register, not an auto-fix)
- scaffolding/open-questions.md (append-only: 4 intake entries — nleps-deferred-l1-primitives-carry-forward [4 deferred NLEPS pieces, fan-out-ordered]; nleps-newton-loop-check-stop-into-carry-reuse-eigsolve-unblock; nonlinear-pencil-opaque-type-concept-page-candidate; eigsolve-l1-apply-nonlinear-pencil-crossref-follow-up)

Gate hits:
- summary-md-registration: 0 (block 3 explicitly registers the new L1 chapter; no auto-fix needed)
- index-placeholder-displacement: 0 (dep-map row appended after a populated row; no placeholder present)
- forward-edge-without-surface: 0 (firm L1 operator read from a clean positive source site `nleps.cpp:807-821` + 4 corroborating sites; surface exists)
- edge-label / prose mismatch: 0 (not a lowering theme; dep-map row column-shape matches the `assemble-diagonal` anchor row; critic-confirmed edge-label-fidelity pass)
- variant-axis-missing: 0 (4 axes classified: damping-present + purpose/coefficient-vector live; A2-representation + L0-build-form absorbed; critic-confirmed pass)
- concept-writes-on-existing-slug: 0 (NEW slug; no existing-slug overwrite)
- retroactive-budget: 0 (no out-of-scope retro-edits; the index count-bump + cohort bullet are in-scope consistency-syncs for the landing operator, mirroring the cycle-021 fgmres-row precedent)
- implied-component-stub: 0 (all cross-references in the new file resolve to existing on-disk files; the deferred NLEPS pieces are speculative follow-ups without converging on-disk references yet — correctly left as OQ entries + plan candidates, NOT stubbed, per the clearly-implied bar)

Open questions promoted:
- nleps-deferred-l1-primitives-carry-forward
- nleps-newton-loop-check-stop-into-carry-reuse-eigsolve-unblock
- nonlinear-pencil-opaque-type-concept-page-candidate
- eigsolve-l1-apply-nonlinear-pencil-crossref-follow-up

Build-relevant: yes

Notes:
- L1/L2 duplication confirmed CLEAN against the sibling `combinator-miner-deflate-gram` report (integration #6 this cycle): this report owns the **L1** pencil-apply primitive only; the sibling owns the **L2** `deflate`/`gram` combinator. The deflation extension `U(λ)v₂` is explicitly DEFERRED in this report (recorded in `nleps-deferred-l1-primitives-carry-forward` as `nleps_deflated_residual`, gated on the L2 combinator shape settling) precisely to avoid pre-committing the L1/L2 boundary — no overlap.
- The two follow-up edits the report flagged as out-of-dispatch (the `eigsolve.md` reverse cross-reference and the deeper `L1/index.md` cohort prose-framing sentence) are NOT blockers for this landing. I applied the mechanical part of the cohort sync (count 12→13 + a thin one-line cohort bullet) as an in-scope consistency-repair for the landing operator (precedent: the cycle-021 wave-1 fgmres-row landing in this same staging log, row 1 Notes — a firm operator absent from its layer's cohort list/count would be a cross-reference-integrity gap). The fuller cohort-framing sentence + the `eigsolve.md` backref are left to a layer-intro-author L1-refresh (OQ `eigsolve-l1-apply-nonlinear-pencil-crossref-follow-up` + plan candidate).
- The 4 deferred NLEPS pieces (deflated-residual → deflated-solve → Jacobian → eigenvalue-correction) are consolidated into ONE carry-forward OQ entry (fan-out-ordered) rather than 4 separate entries, to keep the intake channel compact; each carries a distinct plan candidate name for migration.
- Critic/repair: all 8 checks pass post-repair (3 low-severity citation/label fixes applied by the repairer: intra-range line-pin tightening on `GetResidualNorm`, `eps.hpp:69-74` closure-type claim narrowing, `:729` role-label `preconditioner`→`system-operator`). `firm` status independently ratified by the critic (positive-site structural citation; nonlinearity quarantined in the opaque `A2` closure; `apply_linop`/`chebyshev-smoother` firm-on-structure precedent, NOT the `eigsolve` convergence-semantics rough-in precedent). Fence-guard PASS (body fully enclosed CYCLE.md:24-143).
- Deferred integrated_at to finalize per role-spec (did not touch the consumed report's frontmatter).

---
## 2026-05-29T051532Z-lowering-verifier-axpby-axpbypcz-firm
applied_at: 2026-05-29T055200Z
applied_by: integrator-per-report
status: partially-applied

Files touched:
- book/src/L1-L0/axpby-mutation-rotation.md (edit: Theme-1 axpby FIRM — (a) replaced the raw-YAML-in-prose `verified_against:` block (former lines 173-209) with the re-audited cycle-021 fenced ```yaml block (9 anchors re-confirmed line-exact, timestamps refreshed 2026-05-27→2026-05-29T05:22:35Z, romoperator/drivensolver corpus-census note added); (b) `## Status` body flip rough-in→firm)
- book/src/L1-L0/index.md (edit: dep-map row :18 `axpby-mutation-rotation` rough-in→firm + L0-anchor column expanded to `operator.cpp`,`rap.cpp` + L1-anchor cell `(+ axpby rough-in)`→`(+ axpby/axpbypcz fwd-ref)` + firm-qualifier added)
- scaffolding/open-questions.md (append-only: 5 intake entries — axpbypcz-mutation-rotation-callsite-correction-and-firm [BLOCKER→cycle-022]; blas1-l1-l0-lowering-floor-7-of-8-axpbypcz-remains [floor NOT closed]; axpby-theme-covers-axpy-family-naming; axpby-corpus-coverage-exhaustive-indexing; axpbypcz-mfem-add-alias-safety-carry)

Gate hits:
- retroactive-budget: 0 (the status flip + re-audited verified_against block + dep-map row ARE the lowering-verifier's in-scope audit work product; no out-of-scope slice retro-edits)
- concept-writes-on-existing-slug: 0 (no concept writes; both targets are existing theme files — firm flip + dep-map row, no new slug)
- forward-edge-without-surface: 0 (axpby firms against the firm `L1/axpy` anchor + all L0 source ranges read_range-verified line-exact; surface exists)
- edge-label / prose mismatch: 0 (L1>L0 edge; critic-confirmed edge-label-fidelity pass)
- variant-axis-missing: 0 (sub-pattern A/B/C taxonomy is the variant axis; critic-confirmed pass)
- summary-md-registration: 0 (axpby-mutation-rotation already registered at SUMMARY.md:73 as a plain link — existing theme, no new file; NO `(stub)`/`(rough-in)` label present to drop, so NO SUMMARY edit made/needed)
- index-placeholder-displacement: 0 (dep-map row :18 was a populated `rough-in` row, NOT the `(empty — Phase B skeleton.)` placeholder; replaced an existing row's status, not a placeholder)
- implied-component-stub: 0 (no dangling implied-component forward-reference; the `axpby`/`axpbypcz` fwd-refs in the dep-map L1-anchor cell are plain-text inline-code, not live links; `axpbypcz-mutation-rotation.md` exists on disk and its live-link theme-list row was left unchanged)
- append-on-missing-slug: 0 (both target files exist on disk)

Open questions promoted:
- axpbypcz-mutation-rotation-callsite-correction-and-firm
- blas1-l1-l0-lowering-floor-7-of-8-axpbypcz-remains
- axpby-theme-covers-axpy-family-naming
- axpby-corpus-coverage-exhaustive-indexing
- axpbypcz-mfem-add-alias-safety-carry

Build-relevant: yes

Notes:
- status `partially-applied` is BY DESIGN, not a defect: this is a SPLIT-verdict audit. Theme 1 (`axpby-mutation-rotation`) FIRM was ENACTED in full (3 edits). Theme 2 (`axpbypcz-mutation-rotation`) is GATED — the auditor UNBLOCKED (exact corrections (1)-(6) + a drafted `verified_against:` block + a drafted firm `## Status` body, all in the report's proposed-changes) but did NOT ENACT, per the cycle-012 gated-promotion discipline. I made ZERO edits to `book/src/L1-L0/axpbypcz-mutation-rotation.md` and left its dep-map row at `index.md:19` UNCHANGED (stays `rough-in`). The axpbypcz firming is routed to cycle-022 plan item `axpbypcz-mutation-rotation-callsite-correction-and-firm` (the BLOCKER OQ I promoted) — 3 confirmed call-site classification errors (nleps:343-344 D→A, romoperator:188-189 D→A, slepc:1986 γ≠0→γ=0; critic independently read_range-confirmed all three).
- BLAS-1 L1>L0 lowering floor (`blas1-l1-l0-lowering-theme-gap`) reaches 7/8 firm with this landing (dot/scal/nrm2/assemble-diagonal/axpby firm); it is NOT closed — `axpbypcz` remains rough-in (OQ `blas1-l1-l0-lowering-floor-7-of-8-axpbypcz-remains`). Note for finalize/meta-phase: the existing floor OQ does NOT close this cycle.
- The `verified_against:` block in the source file was raw YAML-in-prose (unfenced); the report's proposed replacement wraps it in a ```yaml fence (consistent with the firm-sibling shape, e.g. scal-mutation-rotation cycle-020). Applied as a fenced block.
- SUMMARY label check (per dispatch): `axpby-mutation-rotation` at SUMMARY.md:73 is a bare `[axpby-mutation-rotation](./L1-L0/axpby-mutation-rotation.md)` link — no maturity label to drop. No SUMMARY edit.
- skill-uptake-survey was the only non-pass (warning, telemetry-only): the report's shape matches `verify-citation-range` (audit/inherited-citation sub-case) + `verify-refinement-surface` but named neither — surfaced for meta-phase skill-uptake tracking, non-blocking.
- Deferred integrated_at to finalize per role-spec (did not touch the consumed report's frontmatter).

---
## 2026-05-29T051532Z-harvester-l2-ksp-solve-firm
applied_at: 2026-05-29T060400Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/ksp_solve.md (edit/full-replace: stub→FIRM L2 operator — the outer-driver composition that wraps the `krylov-step` kernel in a convergence-test / restart `iterate_while` fold. ENTIRE firm body landed: frontmatter `firmness: firm`, `# ksp_solve`, Context + L1-collapse-relationship, Signature [2 inner ```text blocks: type + body composition], 4-phase Semantics, Algebraic laws [4 fold-terminal laws + inherited demand-pruning + 6 explicit non-laws], Dependencies, 6 loop-shaping Variant axes, `## Status` firm, Lowers from [non-identity L1 un-collapse], Lifts to [non-identity L3 iteration-view un-erasure], L2-vs-L1 + L2-vs-L3 distinctions, full Evidence. NOT just an intro — full body verified present, cycle-019 orthogonalize defect avoided.)
- book/src/L2/index.md (edit: dep-map row :53 flipped stub→firm — signature cell now `(K: Solver[A], b: Tensor[N]) → SolveResult[N]` (body ≡ convergence-test iterate_while fold of krylov-step op), prose now "Outer-driver composition" + direct-dep/concepts/non-identity-L2↔L1+L3↔L2 framing + L0 anchors, status cell `firm`)
- book/src/SUMMARY.md (edit: replace-in-place de-stub at :44 — `- [ksp_solve (stub)](./L2/ksp_solve.md)` → `- [ksp_solve](./L2/ksp_solve.md)`; verified current text was exactly `(stub)` before editing; NOT an append — append would have duplicated the TOC link → build error)
- scaffolding/open-questions.md (append-only: 4 intake entries — l3-ksp-solve-citation-drift-463-563-correction [the dispatch-flagged off-by-one drift in the append-only firm L3 entry, CG `:464`→`:463` + GMRES `:564`→`:563`]; l2-index-working-note-staleness-l3-ksp-solve-on-disk [the dispatch-flagged "L3/ksp_solve.md not yet on disk" staleness — it exists now — plus the line-41/72 prose-stub refresh]; l3-l2-ksp-solve-outer-driver-theme-now-unblocked [the gated wave-2 dispatch #3 dependent]; l2-ksp-solve-materialise-iterate-incremental-least-squares-cite-tightening)

Gate hits:
- retroactive-budget: 0 (all edits are this report's own operator promotion + its dep-map row + SUMMARY de-stub; per-slice and global both 0; no out-of-scope slice retro-edits)
- concept-writes-on-existing-slug: 0 (no concept page writes; the operator file is an L2 operator, not a concept slug)
- forward-edge-without-surface: 0 (firm L2 operator backs onto the firm L1/ksp_solve un-collapse + firm L2/krylov-step kernel + firm L3/ksp_solve; surface exists. The sole forward-reference `L3-L2/ksp-solve-outer-driver` is plain-text, NOT a live link — verified absent on disk, correctly the gated wave-2 dispatch #3 job)
- edge-label / prose mismatch: 0 (dep-map row prose matches the entry's L2↔L1 un-collapse + L3↔L2 un-erasure framing; critic-confirmed edge-label-fidelity pass)
- h1-reuses-page-heading: 0 (`# ksp_solve` is the operator name; standard)
- append-on-missing-slug: 0 (all 3 targets exist on disk)
- variant-axis-missing: 0 (6 loop-shaping axes enumerated + complemented against krylov-step's 6 body axes; critic-confirmed variant-axis-coverage pass)
- summary-md-registration: 0 (NOT a new file — the chapter was already registered as a stub; this is a de-stub replace-in-place at :44, no auto-fix needed/applied)
- index-placeholder-displacement: 0 (the dep-map row :53 was a populated `stub` row, NOT the `(empty — Phase B skeleton.)` placeholder; replaced an existing row's content, not a placeholder)
- implied-component-stub: 0 (no dangling clearly-implied forward-reference to stub — `L3-L2/ksp-solve-outer-driver` has a queued owner (wave-2 dispatch #3) and stays a correct plain-text forward-reference, not perpetually-deferred; all 22 live-link targets in the new entry resolve on disk)

Open questions promoted:
- l3-ksp-solve-citation-drift-463-563-correction
- l2-index-working-note-staleness-l3-ksp-solve-on-disk
- l3-l2-ksp-solve-outer-driver-theme-now-unblocked
- l2-ksp-solve-materialise-iterate-incremental-least-squares-cite-tightening

Build-relevant: yes

Notes:
- ORDERING: this landing MUST precede integration #5 (the L3-L2 ksp-solve-outer-driver theme), which depends on this firm L2 entry. Applied here ahead of it per the parent's dispatch ordering.
- overall_status was `ready` (META.md:25); both critic warnings resolved pre-integration (plan-kind-consistency repaired — the SUMMARY block was rewritten by the repairer into an explicit REPLACE-IN-PLACE with named OLD/NEW lines, applied here exactly as a replace, NOT an append; skill-uptake-survey not-needed/telemetry-only).
- The 22 cross-reference live-link targets in the new firm entry were verified to resolve on disk (L2 siblings, L1 primitives, L3/ksp_solve, L3-L2/krylov-step-body-identity, 8 concept pages). No dead links introduced.
- L3-entry citation drift (`:464`→`:463`, `:564`→`:563`) is the harvester's corrected/critic-re-confirmed finding; the firm L3 entry is append-only post-integration so it is NOT edited here — routed to OQ `l3-ksp-solve-citation-drift-463-563-correction` for a future lifter/lowering-verifier pass (the new L2 entry uses the corrected values).
- Deferred integrated_at to finalize per role-spec (did not touch the consumed report's frontmatter).

---
## 2026-05-29T051532Z-abstractor-l3-l2-ksp-solve-outer-driver
applied_at: 2026-05-29T061900Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3-L2/ksp-solve-outer-driver.md (Write: NEW firm L3>L2 theme — the SUBSTANTIVE / NON-IDENTITY outer-driver rotation complementing the kernel-body identity sibling. ENTIRE fenced body landed [CYCLE.md fence :49→:232]: opening blurb, Slug, Context [5-row chain L1→L3>L2], L3 form (LHS) [inner ```text fold block], L2 form (RHS) [inner ```text fold block], Rewrite shape [3 numbered + 5-row mapping table], Applicability conditions [4, incl. the repaired variant-axis arithmetic], Justification kind [structural dominant + reduction-chain secondary + abstraction-direction note], Speculative L3 operators (None), Kernel-identity/driver-non-identity contrast [+ table], Verified-against [L3/L2/sibling/L0/strawman/concept/OQ evidence], Status firm, L3>L2-vs-kernel-theme distinction. Both inner ```text blocks properly nested+closed; no fence truncation.)
- book/src/L3-L2/index.md (edit: dep-map row added after the `krylov-step-body-identity` anchor row at :13 — `ksp-solve-outer-driver`, LHS=L3 ksp_solve explicit iterate_while_L3 fold, RHS=L2 ksp_solve outer-driver-by-role wrap, justification `structural` + secondary `reduction-chain`, status `firm`)
- book/src/SUMMARY.md (edit: registered `[ksp-solve-outer-driver](./L3-L2/ksp-solve-outer-driver.md)` under the `# L3 > L2 — Lowering` Part after the `krylov-step-body-identity` entry at :34 — explicit block-3 register from the report, NOT an auto-fix)
- scaffolding/open-questions.md (append-only: 3 intake entries — l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion-RESOLVED [closed-disposition append for the gated OQ at :356; meta-phase migrates to Closed index w/ answer-link]; l3-l2-ksp-solve-outer-driver-obstruction-shadow-non-law-cross-link-tightening [refinement nicety]; l3-l2-ksp-solve-outer-driver-fgmres-coverage-symmetry-note [completeness note])

Gate hits:
- forward-edge-without-surface: 0 (the RHS L2 ksp_solve is FIRM on disk — `firmness: firm` confirmed, landed integration #4 `harvester-l2-ksp-solve-firm` 060400Z; the immediately-prior staging row. The LHS L3 ksp_solve firm on disk since cycle-020. Surface exists at both endpoints; the ordering precondition is satisfied.)
- edge-label / prose mismatch: 0 (L3>L2 edge throughout: LHS=L3, RHS=L2, forward narration L3→L2 "lowers into"; dep-map row column-shape matches; critic-confirmed edge-label-fidelity pass)
- variant-axis-missing: 0 (theme, not operator — no operator variant matrix; the applicability-condition-4 axis arithmetic was repaired pre-integration `L2 six = four-shared + restart-shape-folded-into-solver-method + two-new`; critic warning→repaired)
- summary-md-registration: 0 (block 3 explicitly registers the NEW chapter under the L3>L2 Part; no auto-fix needed/applied)
- index-placeholder-displacement: 0 (dep-map row appended after a POPULATED row [krylov-step-body-identity], not the `(empty — Phase B skeleton.)` placeholder)
- concept-writes-on-existing-slug: 0 (no concept writes; new file is an L3>L2 theme, not a concept slug)
- h1-reuses-page-heading: 0 (`# ksp-solve-outer-driver` is the theme slug; standard)
- append-on-missing-slug: 0 (block-2 target `L3-L2/index.md` + block-3 target `SUMMARY.md` both exist; block-1 is a NEW Write of a not-yet-existing file — correct)
- implied-component-stub: 0 (all 21 live-link targets in the new theme resolve on disk — verified L3/L2 ksp_solve, krylov-step at L2/L3/L4, the kernel sibling, iterate-while/-with-prev, minres/bicgstab obstruction themes, L2/L3 index, 6 concept pages, l4_calculus strawman; no dangling forward-reference, no stub created)
- retroactive-budget: 0 (all edits are this theme's own NEW file + its dep-map row + SUMMARY register; per-slice and global both 0; no out-of-scope retro-edits)

Open questions promoted:
- l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion-RESOLVED
- l3-l2-ksp-solve-outer-driver-obstruction-shadow-non-law-cross-link-tightening
- l3-l2-ksp-solve-outer-driver-fgmres-coverage-symmetry-note

Build-relevant: yes

Notes:
- ORDERING SATISFIED: this is cycle-021 integration #5, the gated wave-2 dispatch #3. Its RHS reproduces/cites the firm L2 ksp_solve form authored by wave-1 dispatch #2, which landed at integration #4 (immediately-prior staging row, `book/src/L2/ksp_solve.md` flipped stub→firm). I confirmed `firmness: firm` is on disk before applying. The theme's structural claims about the firm L2 form (the §Signature body, the two named §"Algebraic laws" non-laws "Fold-merge / associativity" + "Identity / lift of the fold to a single tensor-field op at L2", the §Semantics phase-2 handoff quote) now land against the firmed L2 entry rather than the claim-free stub. Per META.md §"Suggested resolution" the critic verified every reproduced L2 claim matches dispatch #2's CYCLE.md exactly.
- OQ CLOSURE (META finding 1): the canonical ledger slug `l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion` (`open-questions.md:356`) is RESOLVED by this theme. Per role-spec the per-report integrator does NOT edit existing OQ entries in place — I recorded the closure as a NEW append-only `...-RESOLVED` intake entry (with answer-link `book/src/L3-L2/ksp-solve-outer-driver.md` + an explicit meta-phase Closed-index migration action), mirroring the cycle-021 row-1 fgmres-RESOLVED precedent in this same staging log. The repairer had already corrected the report's earlier dangling-slug placeholder `ksp-solve-l3-l2-theme-pending` → the canonical slug.
- The report's §Open-questions item (1) — the firm L3 entry's off-by-one inner citations (`:464`→`:463`, `:564`→`:563`) — was NOT re-promoted: it is already tracked by dispatch #2 (integration #4 promoted `l3-ksp-solve-citation-drift-463-563-correction`), and the report itself says "Tracked in the OQ ledger by dispatch #2 already; this dispatch re-affirms." Avoided duplicating the intake entry (compact-channel discipline). The firm L3 entry is append-only post-integration; this theme correctly uses the verified `:463`/`:563` lines and does NOT touch the L3 file.
- overall_status was `ready` (META.md:25); all critic warnings resolved pre-integration (citation-validity dangling-slug + variant-axis arithmetic both repaired; cross-reference-integrity/skill-uptake telemetry/sequencing — not-needed). Fence-guard PASS (entire firm theme body enclosed in the `edit:` block CYCLE.md:49-232; both inner ```text form-blocks nested+closed).
- Deferred integrated_at to finalize per role-spec (did not touch the consumed report's frontmatter).

---
## 2026-05-29T051532Z-combinator-miner-deflate-gram
applied_at: 2026-05-29T063400Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/index.md (edit: appended TWO rough-in dep-map rows to the "## Operator dep-map" table after the now-firm `ksp_solve` row at :53 — (1) `gram` *(rough-in; no anchor yet)* = all-pairs `inner_product` fold → `Matrix[k,k]`, Hermitian/PSD, incremental-Gram block law; (2) `deflate` *(rough-in; no anchor yet)* = oblique/Galerkin complementary projector `I − X(XᴴX)⁻¹Xᴴ`, named-composition over `gram`+`lu_solve`+`linear_combination`+`dot`, with the do-NOT-merge over-unification guard vs `orthogonalize`. BOTH forward-refs are plain-text/inline-code spans — `` `gram` `` / `` `deflate` `` — NOT live `[gram](./gram.md)` links; the chapter files do NOT exist on disk, so a live link would be a hard linkcheck2 error.)
- scaffolding/open-questions.md (append-only: 4 intake entries — deflate-needs-small-dense-lu-solve-primitive [LOAD-BEARING firm-promotion blocker — the `k×k` dense `fullPivLu().solve`, candidate L1 `lu_solve` leaf, distinct from iterative `ksp_solve` + triangular `trsv`]; deflate-project-oblique-core-vs-nleps-schur-modification [harvester factoring decision: bare oblique core vs Schur-modified-NLEPS variant axis]; deflate-single-algorithm-concentration-scope-review [scope-risk caveat — all 5 sites in nleps.cpp; promotion gated on a 2nd Gram-LU site OR an explicit NLEPS-scoped verdict]; deflate-vs-orthogonalize-over-unification-guard [the `orthogonalize = deflate|_{gram=I}` specialization edge + do-NOT-erase-`(XᴴX)⁻¹` guard + the gram/deflate two-rows note])

Gate hits:
- rough-in-rows-must-be-plain-text-when-anchor-missing: 0 (BOTH rows use plain-text/inline-code forward-refs as the report's proposed-changes already specified; verified `book/src/L2/gram.md` and `book/src/L2/deflate.md` do NOT exist on disk → no live link introduced → no linkcheck2 break)
- implied-component-stub: 0 (DID NOT stub-materialize gram/deflate — per dispatch + the clearly-implied bar: they are single-algorithm-concentration rough-in candidates [all 5 sites in nleps.cpp, NOT ≥2-converging-references across passes], so the plain-text rough-in row is the correct shape; stub-creation bar NOT met. The `lu_solve` dependency is likewise a speculative candidate L1 leaf → OQ + plan candidate, NOT stubbed.)
- forward-edge-without-surface: 0 (these are SAME-LAYER L2 rough-in rows, not cross-layer forward edges; the constituents they cite — `inner_product`, `linear_combination`, `dot`, `orthogonalize` — are all firm on disk; the one not-yet-vocabulary dep `lu_solve` is correctly flagged as a blocker OQ, not asserted as existing surface)
- edge-label / prose mismatch: 0 (no L_{n+1}→L_n edge label carried; the `orthogonalize = deflate|_{gram=I}` relation is a same-layer cross-reference and the row prose discusses exactly that relation as a do-NOT-merge guard; critic-confirmed edge-label-fidelity pass)
- variant-axis-missing: 0 (rough-in rows, not firm operators; both rows enumerate variant axes in-cell — `gram`: dot-hook {canonical, B-weighted}; `deflate`: plain-vs-Schur-modified-NLEPS, dot-hook, in-place/out-of-place; critic-confirmed variant-axis-coverage pass)
- concept-writes-on-existing-slug: 0 (no concept page writes; rough-in dep-map rows only, no new slug files created)
- index-placeholder-displacement: 0 (rows APPENDED after a POPULATED row [the firm `ksp_solve` row at :53], NOT the `(empty — Phase B skeleton.)` placeholder; the L2 dep-map has no placeholder — it is fully populated)
- append-on-missing-slug: 0 (target `book/src/L2/index.md` exists on disk)
- summary-md-registration: 0 (no new chapter file created — only dep-map rows; nothing to register in SUMMARY.md. The `gram.md`/`deflate.md` chapters are the future harvester's job, registered when authored.)
- retroactive-budget: 0 (the two rough-in rows ARE this report's own proposed-changes; per-slice and global both 0; no out-of-scope retro-edits)

Open questions promoted:
- deflate-needs-small-dense-lu-solve-primitive
- deflate-project-oblique-core-vs-nleps-schur-modification
- deflate-single-algorithm-concentration-scope-review
- deflate-vs-orthogonalize-over-unification-guard

Build-relevant: yes

Notes:
- Re-read `book/src/L2/index.md` FRESH before editing (per dispatch): confirmed integration #4 [`harvester-l2-ksp-solve-firm`, 060400Z] flipped the `ksp_solve` dep-map row at :53 stub→firm, and the cycle-020 L2-refresh restructured the dep-map (two-motif framing: named-compositions + fold-cohorts). The report's proposed-changes anchored on "after the `ksp_solve` stub row (:53)" — that row is now FIRM, but it is still the last row of the table and the correct anchor position; I appended after it. No conflict with the in-cycle ksp_solve firm landing.
- L1/L2 duplication CLEAN against the sibling `harvester-nleps-l1` report (integration #2 this cycle, see its Notes): THIS report owns the **L2** `deflate`/`gram` combinator; the sibling owns the **L1** `apply_nonlinear_pencil` pencil-apply primitive. The sibling explicitly DEFERRED the deflation extension `U(λ)v₂` (its `nleps_deflated_residual` carry-forward, gated on the L2 combinator shape settling) precisely to avoid pre-committing the L1/L2 boundary — no overlap. This L2 combinator IS the shape the sibling was waiting to settle.
- This is a PROPOSAL-only report (`status: pending` frontmatter; combinator-miner rough-in): mutates NO chapter files — only the two rough-in dep-map rows + the OQ ledger. The harvester (later pass, plan candidate `deflate-gram-harvester-firm`) creates `book/src/L2/gram.md` + `book/src/L2/deflate.md`, firms signatures/laws, decides the `project_oblique`-vs-Schur factoring, and AT THAT POINT switches these dep-map cells to live links + registers the chapters in SUMMARY.md. Until then the cells stay plain-text.
- The load-bearing firm-promotion BLOCKER is the `lu_solve` candidate L1 dense-solve primitive (OQ `deflate-needs-small-dense-lu-solve-primitive`, the only piece not already firm for `deflate`). Flagged for cycle-planner/meta-phase migration to the plan as the gating dependency before `deflate` can firm. High fan-out (any small-dense coordinate solve across eigensolver/ROM paths would reuse it).
- The 2 citation reconciliations the dispatch references were applied PRE-integration by the repairer (META.md §Repair findings 1+2: D3 instance-header range `:663-668`→`:664,:666,:667` and reference-anchor `:356-362`→`:354-362`); both are in the report body / supporting-evidence, NOT in the proposed-changes block — the dep-map rows landed verbatim. overall_status `ready`; the sole non-pass was skill-uptake-survey (warning, telemetry-only, non-blocking).
- Deferred integrated_at to finalize per role-spec (did not touch the consumed report's frontmatter).

---
## 2026-05-29T051532Z-same-layer-cross-cutter-orthog-dot-surface
applied_at: 2026-05-29T065100Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/dot-mutation-rotation.md (edit: Proposal 1 — added **Sub-pattern D** "hook-routed `LocalDot` + batched `Mpi::GlobalSum` (the unfused form)" to §"L0 form (RHS)", inserted after Sub-pattern C / before "## The conjugation asymmetry". Includes the IdentityInnerProduct + CGS code sketch, the unfused/MGS-interleave/CGS-batch prose, the Observability note (first unweighted-observable `dot` use outside the SLEPc-NEP deflation cohort), justification kind `structural`, and 5 verified citations. Additive; theme stays `firm`, NO status change.)
- book/src/L2-L1/inner-product-fold-specialization.md (edit: Proposal 2 — added the **"Bypass surface (out of the `linalg::Dot`-caller scope, recorded for completeness)"** paragraph after the `conjugation_caller_inventory` yaml fence (:329) / before "## Justification kind". One paragraph, NO new yaml keys — the block stays scoped to `linalg::Dot` callers; the paragraph cross-links to Sub-pattern D of dot-mutation-rotation. Additive; no status change.)
- scaffolding/open-questions.md (append-only: 2 intake entries — orthog-hpp-localdot-globalsum-unfused-dot-surface-RESOLVED [the report's named OQ, closed in-cycle since Proposal 1 was ENACTED this dispatch; answer-link book/src/L1-L0/dot-mutation-rotation.md Sub-pattern D; closes the cycle-020 census report's flagged "coverage gap of its own"; meta-phase migrates to Closed index]; orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d [deferred abstractor follow-up — the un-authored orthogonalize L1>L0 theme should cite Sub-pattern D rather than re-derive])

Gate hits:
- retroactive-budget: 0 (both edits are this report's own additive proposed-changes to existing firm themes; per-slice and global both 0; no out-of-scope retro-edits)
- concept-writes-on-existing-slug: 0 (no concept writes; both targets are existing theme files — additive Sub-pattern + paragraph, no new slug)
- forward-edge-without-surface: 0 (both edges resolve on disk; the one Markdown link in Proposal 2 `[dot-mutation-rotation](../L1-L0/dot-mutation-rotation.md)` points at an existing file and Sub-pattern D is now present there; no live link to a missing file)
- edge-label / prose mismatch: 0 (Proposal 1 = L1>L0 surface-form inventory, prose discusses the L1→L0 dot lowering; Proposal 2 = L2>L1 census scope note; critic-confirmed edge-label-fidelity pass)
- h1-reuses-page-heading: 0 (no new H1; additive `### Sub-pattern D` heading + a bold-led paragraph, consistent with sibling Sub-patterns A/B/C)
- append-on-missing-slug: 0 (both target files exist on disk)
- variant-axis-missing: 0 (observation report; MGS m×1 / CGS 1×m / CGS2 2×m collective-shape axis fully covered; weighted-vs-unweighted axis explicitly scoped out in a caveat; critic-confirmed variant-axis-coverage pass)
- summary-md-registration: 0 (no new chapter file created — additive edits to two existing registered themes; nothing to register)
- index-placeholder-displacement: 0 (no index dep-map rows touched)
- implied-component-stub: 0 (no dangling clearly-implied forward-reference; the single Markdown cross-link resolves on disk; nothing stubbed)

Open questions promoted:
- orthog-hpp-localdot-globalsum-unfused-dot-surface-RESOLVED
- orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d

Build-relevant: yes

Notes:
- DECISION: APPLIED DIRECTLY (option (a) per the dispatch). The report routed Sub-pattern D to a LIFTER follow-up, but its proposed-changes are well-formed additive `edit:` blocks with citations the repairer reconciled line-exact (the `:34` return / `:29-36` struct off-by-one slip was fixed throughout pre-integration per META.md §Repair finding 3). Deferring a fully-cited additive edit to a firm theme to another cycle is friction; the cross-cutter did the work. Applied both Proposal 1 (load-bearing) and Proposal 2 (the optional cross-reference convenience — improves discoverability, additive, zero risk).
- The `dot-mutation-rotation` theme firmed in cycle-020 and STAYS `firm` — Sub-pattern D is a pure additive surface-form enumeration (verdict (a): an additional call-surface of the existing `dot` operator, NOT a new primitive). No status change to ANY entry; no new files; no SUMMARY.md touch.
- Re-read both target files FRESH before editing (per dispatch). Insertion points confirmed against current disk: Sub-pattern C ends at :144 with `## The conjugation asymmetry` at :146 (no prior in-cycle integrator touched this file); the `conjugation_caller_inventory` yaml fence closes at :329 with `## Justification kind` at :331 (the cycle-020 census authored this block; untouched this cycle).
- Critic NOTE (META finding 2, repaired into the report body): `dot.md:119`'s "linalg::Dot used as orthogonalisation-coefficient primitive" is the TEST-reference path (`test-orthog.cpp` computes reference coefficients via the fused `linalg::Dot` to CHECK orthog.hpp's output) — it does NOT contradict Sub-pattern D's production-bypass claim (the two coexist). The Sub-pattern D prose does not assert otherwise; no conflict introduced.
- The OQ `orthog-hpp-localdot-globalsum-unfused-dot-surface` is recorded RESOLVED (not just Open) because its load-bearing follow-up (Proposal 1) was ENACTED this dispatch — mirroring the cycle-021 row-1 (fgmres-RESOLVED) and row-5 (ksp-solve-outer-driver-RESOLVED) append-only-RESOLVED precedent in this same staging log. Per role-spec the per-report integrator does NOT edit existing OQ entries in place; the cycle-020 census report's flagged coverage-gap OQ (if any open ledger entry exists for it) is closed-by-answer via this new RESOLVED append — flagged for meta-phase Closed-index migration.
- skill-uptake-survey was the only critic non-pass (warning, telemetry-only, non-blocking): the report named `verify-citation-range` but not `classify-variant-axis` / `verify-refinement-surface` despite the (a)/(b)/(c) classification. Surfaced for meta-phase skill-uptake tracking; does not affect the verdict's correctness.
- Deferred integrated_at to finalize per role-spec (did not touch the consumed report's frontmatter).

---
## 2026-05-29T051532Z-harvester-l3-eigsolve
applied_at: 2026-05-29T070300Z
applied_by: integrator-per-report
status: applied

Files touched:
- scaffolding/open-questions.md (append-only: 2 intake entries — l3-eigsolve-blocked-on-l1-firm-and-l2-entry [HIGH-fan-out blocker; carries the routed meta-phase plan-#9 reframe note + the strict 3-step prerequisite chain]; l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog [structural; predicts the eventual L3 linear-EVP verdict = sequential/partial-obstruction, not a clean kernel+driver pair])

Gate hits:
- (none fired — NO `book/` proposed-changes; this is a BLOCKED inventory observation, scaffolding/OQ-only)
- implied-component-stub: 0 (DID NOT materialize an L3 eigsolve stub — per dispatch + role-spec: the report's whole point is the backfill is BLOCKED on missing L1-firm + L2-entry anchors; it is blocked-pending-prerequisites, NOT a clearly-implied ready component. A stub would have no `lowers_to` target [no L2 eigsolve] and would lift `unconfirmed` laws from the rough-in L1 form — both methodology violations. Correctly left as OQ + prerequisite-chain + plan candidates, NOT stubbed.)
- forward-edge-without-surface: 0 (no edge authored; the report DOCUMENTS the missing surface as the blocker, does not assert one)
- retroactive-budget: 0 (no book edits at all; per-slice and global both 0)

Open questions promoted:
- l3-eigsolve-blocked-on-l1-firm-and-l2-entry
- l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog

Build-relevant: no

Notes:
- This is the LAST cycle-021 report (integration #8 of 8). NO `book/` changes — a BLOCKED prerequisite-surface inventory observation (the trsv-style outcome). overall_status was `ready` (META.md:25): the harvester's BLOCKED decision is critic-confirmed sound on all three independent grounds (L1 rough-in / no L2 entry / no krylov-step kernel analog), and the only artifact defect was a cosmetic `naupd` line-ref drift already reconciled pre-integration by the repairer to `:317-318`. NO rebuild needed on account of this report (Build-relevant: no).
- META.md §"Suggested resolution" explicitly instructs: "Do not materialize an L3 `eigsolve` stub from this report." Honored — see implied-component-stub gate note above. The clearly-implied-component bar is NOT met (blocked-pending-prerequisites ≠ clearly-implied-ready; missing both the firm-L1 lift anchor and the L2 lower-to target).
- ROUTED PLAN-CORRECTION (meta-phase action, plan co-ownership — NOT enacted here): the first OQ recommends the meta-phase reframe plan item #9 (`priorities.md:31`) from "next L3 inventory backfill" → "blocked-pending-L1-firm+L2-entry," and surface the prerequisite work (eigsolve-l1-rough-in-to-firm → eigsolve-l2-entry → eigsolve-l3-backfill, in strict order) ahead of it. The per-report integrator does NOT edit `priorities.md` (meta-phase/cycle-planner co-owned); recorded in the OQ for the meta-phase's standing intake→plan migration pass. Finalize: surface this to the batch-5 meta-phase.
- linear-EVP (SLEPc-EPS / ARPACK-EPS, this dispatch's scope) vs nonlinear-EVP (`QuasiNewtonSolver`/`nleps.cpp`, the cycle-021 SIBLING NLEPS dispatch's scope) distinction kept clear in both OQ appends — the linear EVP has no Palace-authored kernel; the nonlinear EVP is the only eigsolve family with a Palace-authored Newton loop and is a separate operator question. (The sibling `harvester-nleps-l1` landed integration #2 this cycle, row 2.)
- Deferred integrated_at to finalize per role-spec (did not touch the consumed report's frontmatter).

---

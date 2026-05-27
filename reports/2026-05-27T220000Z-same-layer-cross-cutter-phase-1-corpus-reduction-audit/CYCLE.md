---
agent: same-layer-cross-cutter
invoked_at: 2026-05-27T22:00:00Z
scope: Phase 1 corpus reduction audit — first-instance batch (krylov-step chain overlap)
status: integrated
integrated_at: 2026-05-27T230802Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied cleanly via integrator-per-report pass 8 of cycle-010 (wave-2 #8; **eighth and final per-report integrator of cycle-010**). **First phase-1 corpus reduction in the artifact** — first concrete realization of CLAUDE.md §Methodology invariants new bullet "Phase 1 corpus reduces as material is lifted" (codified cycle-009 meta-phase; priority #19). 3 slices reduced: gmres.md (1144 → 671 lines, -42%); cg.md (506 → 165 lines, -67%); arnoldi_step.md (330 → 302 lines, -8%); **net 842 lines removed** from audited slice subset. Unique material retained verbatim (gmres L4 v0.2-v0.6 self-rotation history; cg L4 v0.5 first-iteration-unrolling derivation + ratification; arnoldi_step L1/L2/L3/L4 sections unique relative to firm krylov-step chain). 4 routing OQs promoted (`l4-v01-v06-self-rotation-history-lift-target-decision`, `cg-initial-residual-quirk-palace-bug-flag-lift-path`, `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog`, `phase-1-corpus-reduction-remaining-7-slices`). Audit template established and machine-replayable for cycle-011+ batches; remaining 7 slices routed with priority order + batch-size suggestion 2-4 slices per dispatch. Friction signals forwarded: `phase-1-corpus-audit-line-range-arithmetic-brittleness` recurrence-1 (cycle-012 meta-phase watch-item); `phase-1-slice-reduction-audit` skill candidate already filed at `scaffolding/skill-candidates.md:114-115`.
inputs:
  - book/src/spec/slices/ (10 slices total; this dispatch audits 3)
  - book/src/spec/slices/gmres.md (1144 lines)
  - book/src/spec/slices/cg.md (506 lines)
  - book/src/spec/slices/arnoldi_step.md (330 lines)
  - book/src/L1/ksp_solve.md (firm; cycle-007)
  - book/src/L1-L0/ksp-solve-mutation-rotation.md (rough-in; cycle-008)
  - book/src/L2/krylov-step.md (firm; cycle-005)
  - book/src/L4/krylov-step.md (firm; cycle-006)
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (firm; cycle-008)
  - book/src/L3-L2/krylov-step-body-identity.md (firm; cycle-009)
  - book/src/L3/krylov-step.md (firm; cycle-010 wave-1 — pending integration as of this dispatch)
  - book/src/L1-L0/minres-iteration.md (firm; cycle-004)
  - book/src/L1-L0/bicgstab-iteration.md (firm; cycle-004)
  - CLAUDE.md §Methodology invariants ("Phase 1 corpus reduces as material is lifted")
  - scaffolding/priorities.md #19 (phase-1-corpus-reduction-audit)
---

# CYCLE: Phase 1 corpus reduction audit — krylov-step chain overlap (first instance)

## Summary

First-instance execution of priority #19 (`phase-1-corpus-reduction-audit`) under the new methodology invariant "Phase 1 corpus reduces as material is lifted". Audits three slices whose subject matter overlaps the now-fully-firm krylov-step chain (L4 + L4>L3 + L3 + L3>L2 + L2 + L1 ksp_solve + L1>L0 ksp-solve-mutation-rotation): `gmres.md` (1144 lines), `cg.md` (506 lines), and `arnoldi_step.md` (330 lines). Result: **all three slices are blocked from full reduction**, but each has substantial sections that are now redundant with firm entries and warrant partial reduction (stub-with-pointer). Material that remains uniquely in the slices and blocks full reduction: (a) detailed L0 line-range citations and per-method workspace specifications, (b) the deep L4 v0.1–v0.6 self-rotation progression in `gmres.md` (six in-place refinement passes documenting the v0.1→v0.6 derivation of `build_convergence` / `classify_outcome` / `check_stop` / `StopReason`-witness extraction), (c) the orthogonalisation variant-dependent L3 obstruction (MGS sequential / CGS / CGS2 batched) detailed only in `arnoldi_step.md` and `orthog.md`, and (d) the `CheckDot` SPD-guard + initial-residual-quirk findings unique to `cg.md`'s Working Notes. Recommended action per slice: **partial-reduction** — sections of slice content that are explicitly superseded should be stubbed (replaced with one-line pointers to firm entries); sections that contain unique material should be retained with a header note recording their slice-corpus origin. Three new OQs are surfaced for material that needs lifting before full reduction is safe. The first-instance audit template established here is machine-replayable for cycle-011+ on the remaining 7 slices.

## Observation kind

**Variant-axis coverage gap (audit-scoped)** — the slices substantially overlap firm entries but each retains unique material that has NOT yet been lifted to firm entries. The audit surfaces (a) the overlap that should be reduced, (b) the residual material that blocks full reduction, and (c) OQs to close before subsequent reduction passes can complete.

## Specific finding

### Slice 1: `book/src/spec/slices/gmres.md` (1144 lines)

**Audit verdict**: partial-reduction (full-reduction blocked by L4 v0.1–v0.6 self-rotation history + unique L0 line-range table).

**Supersession map** (slice section → firm entries that cover it):
- §"Slice: gmres" (intro, lines 1-3) → covered by [`L1/ksp_solve` §Context, `L1-L0/ksp-solve-mutation-rotation` (intro)].
- §"L0 — cited regions" (L0.1–L0.15, lines 5-34) → **partially** covered by [`L0/ksp-factory-file`, `L0/kspsolver-base-class`, `L0/linalg-iterative-file`, `L1-L0/ksp-solve-mutation-rotation` §"Verified-against" (lines 547-687 of that file)]. The slice's L0.1–L0.15 list is more granular (sub-region labels L0.3a/L0.3b/L0.5/L0.5a/L0.8a/L0.8b/L0.9a/L0.9b/L0.10/L0.11/L0.11a/L0.12/L0.13) than the firm L1>L0 theme's flat citation list. **Unique material** to the slice: the per-restart-cycle drift-warning compare at L0.11a (`iterative.cpp:592-600`, the 10% threshold) and the workspace-allocation pair `Initialize`/`Update` for both GMRES (L0.8a/L0.8b) and FGMRES (L0.9a/L0.9b). The L1>L0 theme cites `Initialize` and `Update` for GMRES but the FGMRES-specific lines 707-718, 721-731 are cited only structurally. The drift-warning is not cited anywhere in firm entries.
- §"L1 — pure-functional dataflow" (state schema, building-block operations, procedure, lines 36-125; header at line 36, ends before §"Open questions" at line 126) → covered by [`L1/ksp_solve` §Signature, §Semantics, §"Algebraic laws", §"Variant axes"]. The slice's `gmres_solve` pseudocode procedure (lines 94-116) is the in-spirit precursor to the firm L1 `ksp_solve(K, b) -> SolveResult` signature; the firm entry absorbs CG/GMRES/FGMRES into the opaque `Solver[A]` type and is strictly more general.
- §"Open questions" (L1, lines 126-134; header at line 126, ends before §L2 at line 135) → **partially** lifted. OQ "drift check 10% threshold" still open; OQ "`CheckDot` NaN/Inf gating" partially covered by `L1-L0/ksp-solve-mutation-rotation` recognition note (lines 252-265). OQ "no dedicated GMRES/FGMRES unit test" survives as a documentation note in `L1/ksp_solve.md` Evidence (no direct test linkage). OQ "MGS sequential / CGS batched / CGS2 refinement" lifted into `arnoldi_step.md` §L3 (slice-level) but not yet into a firm L1/L2 entry for `orthogonalize`.
- §"L2 — primitive composition" (lines 135-242; header at line 135, ends before §L3 at line 243) → covered by [`L2/krylov-step` §Semantics (primitive composition: `apply_BA → orthogonalize → ls_update_column → back_solve → apply_correction`)]. The slice's per-primitive unfoldings (`initial_residual`, `apply_BA`, `orthogonalize`, `ls_update_column`, `back_solve`, `apply_correction`) are the direct precursors to the L2 entry's variant-axis profile. The "Primitive-sequence summary (per inner iteration)" at slice lines 219-228 maps directly to the L2 entry's `apply` + `optional auxiliary` + `iterate-update` + `scalar-update` + `output-readout` five-group decomposition. **Unique material**: the slice's explicit `givens_generate` + `givens_apply` L2 primitive vocabulary (lines 146-147) is *not* in the L2 `krylov-step` entry — that entry stays at the five-group level. The slice's incremental-LS rewrite at lines 180-194 (the load-bearing L1→L2 unfolding) is more concrete than the L2 entry's `ls_update_column` summary.
- §"L3 — global tensor-field form" (lines 243-331; header at line 243, ends before §L4 at line 332) → covered by [`L3/krylov-step` (cycle-010 wave-1, pending integration) + `L3-L2/krylov-step-body-identity`]. The slice's "Obstruction: incremental LS triangularisation" (lines 287-301) is the in-spirit precursor to the sequential-obstruction recording in the L3 entry. The slice's "L3 inner-step shape" (lines 308-318) maps directly to the L3 entry's value-threaded body. **Unique material**: the slice's MGS-vs-CGS-vs-CGS2 L3 lift split (lines 270-277) is referenced from the L3 entry but the detailed allreduce-count tabulation is in `arnoldi_step.md` §"MPI-collective shape" only; this is unique to the slice corpus and not yet lifted.
- §"L4" (v0.1, lines 332-496; header at line 332, ends before §"L4 v0.2" at line 497) → **partially** covered by [`L4/krylov-step`, concepts/`solve-monad`, concepts/`state-stratification`, concepts/`convergence-test`, concepts/`derived-view-hoisting`]. The slice's `SimState` / `OpParams` / `Krylov` typing (lines 360-396) and `gmres_solve` / `solve_loop` / `restart_cycle` / `inner_loop` monadic structure (lines 425-471) are the in-spirit precursors to the firm L4 entry's Form A signature. The slice's `Convergence` value + `build_convergence` helper (lines 343-354) is the canonical evidence for the `convergence-test` concept.
- §"L4 v0.2 — convergence-criterion absorption tightening" (lines 497-632), §"L4 v0.3 — single-cycle inner-loop predicate consolidation" (lines 733-818), §"L4 v0.4 — restart-pivot extraction" (lines 819-905), §"L4 v0.5 — unified classifier with positional sum" (lines 906-1011), §"L4 v0.6 — stop-witness extraction" (lines 1012-1144) → **NOT covered** by firm entries. This is the deep five-iteration v0.1→v0.6 self-rotation progression. The endpoint (v0.6 form: `check_stop` + `StopReason` + `Position` sum type + `classify` total over inputs + `commit_outcome`) survives in `book/src/concepts/convergence-test.md` only schematically; the full derivation showing why each version was tightened (v0.1's `derive_ir` gap → v0.2's `build_convergence` + `should_stop_inner`; v0.2's split-classifier redundancy → v0.3's unified `classify_outcome`; v0.3's dual-commit-site redundancy → v0.4's `commit_outcome`; v0.4's degenerate-classifier asymmetry → v0.5's `Position` sum; v0.5's `error` arm → v0.6's `StopReason` witness) is **unique to the slice**. **This is the load-bearing reason `gmres.md` cannot be fully reduced**: the v0.1→v0.6 progression IS load-bearing methodology evidence for derived-view-hoisting and witness-typed-dispatch as recurring L4 patterns.

**Residual gaps** (blockers for full reduction):
1. The L4 v0.1→v0.6 self-rotation history is unique methodology evidence for derived-view-hoisting and witness-typed-dispatch. **Lifting target**: this should be promoted to a worked-example section of `concepts/derived-view-hoisting.md` and/or `concepts/witness-typed-dispatch.md` (the latter is mentioned in v0.6 §"Open questions" as a candidate concept extraction "may warrant extraction if it recurs in other slices").
2. The L0.11a drift-warning compare (10% threshold at `iterative.cpp:592-600`) is not cited in firm entries. **Lifting target**: an L1>L0 theme touch or a `L0/linalg-iterative-file` annotation noting this observability hook.
3. The `givens_generate` / `givens_apply` primitives exist as firm **concept pages** (`book/src/concepts/givens_generate.md` and `book/src/concepts/givens_apply.md`) but are NOT promoted to firm **L1 operators** — the L2 `krylov-step` entry stays at the five-group decomposition level and does not enumerate the Givens-rotation primitives explicitly because they live inside the `ls_update_column` sub-step. Distinction: concept-page vocabulary exists; firm L1 operator entries do not. **Lifting target**: speculative L1 operators `givens_generate` and `givens_apply` per the unimplemented-Palace-stub policy section of CLAUDE.md (these are implemented and firm material; promotion only if they simplify higher forms).

**Recommended action**: **partial-reduction**.
- Stub sections that are fully superseded: §"Slice: gmres" (intro), §"L1 — pure-functional dataflow" (the entire L1 block, lines 36-125), §"L1 Open questions" (lines 126-134; some entries lifted; mark which OQs are resolved), §"L2 — primitive composition" (lines 135-242 — fully superseded by `L2/krylov-step`), §"L3 — global tensor-field form" (lines 243-331 — superseded by `L3/krylov-step` + `L3-L2/krylov-step-body-identity` once the cycle-010 wave-1 integration lands), §"L4" v0.1 (lines 332-496 — superseded by `L4/krylov-step`).
- Retain: §"L0 — cited regions" (more granular than firm L1>L0 theme; useful evidence overlay), §"L4 v0.2"–§"L4 v0.6" (the unique self-rotation history), the §"Open questions" L4-v0.*-specific subsections.
- Add a header note: "This slice is the historical precursor to the cycle-005/006/007/008/009/010 krylov-step chain. The L1/L2/L3/L4-v0.1 forms have been lifted to firm entries [list]. The L4 v0.1→v0.6 self-rotation history below is preserved as unique methodology evidence pending extraction to concepts/."

### Slice 2: `book/src/spec/slices/cg.md` (506 lines)

**Audit verdict**: partial-reduction (full-reduction blocked by `CheckDot` SPD-guard treatment + initial-residual quirk + first-iteration-unrolling L4 v0.5 derivation + unpreconditioned-as-primary modeling choice).

**Supersession map**:
- §"Context" (lines 3-12) → covered by [`L1/ksp_solve` §Context (the variant-axis collapse across CG / GMRES / FGMRES), `L1-L0/ksp-solve-mutation-rotation` §"Sub-pattern B — inner CG body"].
- §"L0" (lines 13-39) → **partially** covered by [`L1-L0/ksp-solve-mutation-rotation` §"Sub-pattern B" + Verified-against entries for `iterative.cpp:360-486`, `:369-374`, `:377-386`, `:418-419`, `:427-464`, `:443`, `:448-449`, `:484-485`]. **Unique material**: the slice's explicit citation of `CheckDot<T>` at `iterative.cpp:244-250` invoked at lines 396/412/444/461 (line 22 + line 39) is more granular than the firm theme's recognition-note treatment.
- §"L1" (lines 40-96; header at line 40, ends before §L2 at line 97) → covered by [`L1/ksp_solve` §Signature, §Semantics, §"Algebraic laws", §"Variant axes" (krylov-method collapsed)]. The slice's `iterate from (x, r, z, p, beta, beta_prev, res, it)` pseudocode (lines 67-84) is the precursor to the firm `ksp_solve(K, b) -> SolveResult` signature. **Unique material**: the initial-residual quirk treatment in the `!B && initial_guess` branch (line 95 + Working Notes lines 286) — the slice flags the `initial_res = (b·b)^{1/4}` asymmetry as a likely Palace bug. The firm `L1/ksp_solve` entry does not record this finding; the firm L1>L0 theme records the initial-guess threading but not the bug-flag.
- §"L2" (lines 97-122; header at line 97, ends before §L3 at line 123) → covered by [`L2/krylov-step` §Semantics (CG instance), `L2/krylov-step` §"Pattern instances" (CG cited)].
- §"L3" (lines 123-138; header at line 123, ends before §L4 at line 139) → covered by [`L3/krylov-step` (cycle-010 wave-1), `concepts/sequential-obstruction` (CG outer-loop obstruction is the canonical instance)].
- §"L4" v0.1 (single monolithic L4 section, lines 139-282; header at line 139, ends before §"Working Notes" at line 283; the slice's L4 is monolithic, not sub-versioned at v0.1/v0.2/v0.3) → **partially** covered. The L4 form (Form A in `L4/krylov-step` taxonomy) is canonical evidence for `concepts/derived-view-hoisting` (residual-norm hoisting; via the v0.4 derived-view-hoisting self-rotation section at lines 295-340). The v0.5 form (Form B / first-iteration-unrolling) is canonical evidence for `concepts/first-iteration-unrolling`. The firm L4 entry references both concepts and the slice as canonical evidence (Evidence section lines 169-172 of `L4/krylov-step.md`). **Unique material**: the slice's modeling choice "unpreconditioned CG is primary; preconditioned CG is variant" (lines 9, 222) inverts Palace's source structure (always-preconditioned with identity fallback). This modeling rotation is not lifted to a firm entry; it is unique L4 methodology evidence.
- §"L4 v0.4 — derived-view hoisting (self-rotation)" (lines 295-340; header at line 295, ends before §"L2→L3" at line 341) → **NOT covered** as a complete derivation. The endpoint (residual-norm as output-extra, demand-pruned per §3.8) lives in `concepts/derived-view-hoisting.md` and in `L4/krylov-step` Law 1. The slice's explicit "Rejected v0.2-style schema" / "Adopted v0.3/v0.4 schema" contrast (lines 308-316) and the "What this rotation hides" / "General rule" discussion (lines 324-331) is the canonical worked-example derivation; it should be lifted to `concepts/derived-view-hoisting.md` if not already excerpted there.
- §"L2→L3 — rotation claims (retroactive, cycle 116)" (lines 341-367; header at line 341, content through line 366, ends before §"L4 v0.5" at line 368) → covered by [`L3/krylov-step` (cycle-010 wave-1) + `L3-L2/krylov-step-body-identity` (cycle-009)]. The slice's "Claim 1: outer-loop obstruction (negative L3)" and "Claim 2: step body lifts as identity" are the in-spirit precursors to the firm L3 and L3>L2 entries.
- §"L4 v0.5 — first-iteration unrolling (self-rotation)" (lines 368-483; header at line 368, ends before §"L4 v0.5 ... claim ratification" at line 484, plus the "claim ratification" at lines 484-506) → **partially** covered. The endpoint (`first_step` / `steady_step` signatures, `iterate_while_with_prev`) lives in `concepts/first-iteration-unrolling.md` and in `L4/krylov-step` Form B. The slice's derivation showing why v0.4's `if s.it == 0` branch survived from L1 all the way to L4 (lines 376-377), why the closure-captured `beta_prev` is the load-bearing rotation (lines 449-455), and the `forget_beta_prev` projection making the equivalence formal (lines 461-470) is the canonical worked-example derivation.

**Residual gaps** (blockers for full reduction):
1. The initial-residual quirk (`!B && initial_guess` branch returning `(b·b)^{1/4}` instead of `‖b‖₂`) is unique to this slice and is flagged as a likely Palace bug. **Lifting target**: surface as an open question in `scaffolding/open-questions.md` (Palace bug candidate; needs upstream confirmation) and add an annotation to `L1/ksp_solve` Semantics or to `L1-L0/ksp-solve-mutation-rotation` Sub-pattern B with a back-reference.
2. The `CheckDot<T>` partial-function guard treatment (lines 244-250 at `iterative.cpp`, invoked at lines 396/412/444/461) is recognised in the firm L1>L0 theme but not enumerated per-call-site. The slice's explicit list of invocation sites is unique. **Lifting target**: add a `verified_against` row to `L1-L0/ksp-solve-mutation-rotation.md` for each CheckDot call site, or promote to a `L0/linalg-iterative-file` annotation.
3. The "unpreconditioned-as-primary" L4 modeling choice (lines 9, 222) is unique. **Lifting target**: either lift to `L4/krylov-step` (which would broaden its scope) or document as a methodology-section L4 presentation choice in `concepts/state-stratification` (where preconditioned-vs-unpreconditioned modeling choices belong).
4. The cycle-116 retroactive rotation_claim emission (§"L2→L3 — rotation claims (retroactive, cycle 116)", lines 341-367) is historical methodology evidence — the practice of emitting rotation_claim records retroactively to ratify on-disk surface is now codified in the cycle-009 meta-batch-1 closure. This is documentation of the methodology *practice*, not of CG-specific algorithm content. **Lifting target**: methodology-history note in `log/cycle-116.md` or in `scaffolding/decisions/` rather than retention in the slice.

**Recommended action**: **partial-reduction**.
- Stub sections that are fully superseded (entire region replaced by the stub header that hoists unique findings into the header's "Open questions still pending lift" subsection): §"Context", §"L0", §"L1", §"L2", §"L3", §"L4" (the monolithic L4 section), §"Working Notes" (the unique findings — initial-residual quirk; CheckDot enumeration; unit-test-coverage gap; unpreconditioned-as-primary modeling choice — are preserved inside the stub header's "Open questions still pending lift" subsection, not in slice-body prose), §"L4 v0.4 — derived-view hoisting (self-rotation)" (superseded by `concepts/derived-view-hoisting.md` Form A and the v0.5 self-rotation supersedes its rotation derivation; lift target for the worked-example contrast is documented in residual gap 5 below if not already excerpted), §"L2→L3 rotation claims (retroactive)" (move to methodology-history; lines 341-367 included in the stubbed region).
- Retain (in-place, verbatim, lines 367-506): §"L4 v0.5 first-iteration-unrolling (self-rotation)" (header at line 368, body through line 483) + §"L4 v0.5 (cycle 137) claim ratification" subsection (lines 484-506) (methodology-history but inside the slice for v0.5 cross-reference). The leading blank line at 367 is preserved as the separator before the §"L4 v0.5" header.
- Add a header note: "This slice is the cycle-001-era precursor to the firm CG row in the krylov-step chain. The L1/L2/L3 forms are now firm at L1 `ksp_solve` (variant-axis-collapsed) + L2 `krylov-step` + L3 `krylov-step`. The monolithic L4 section is a precursor to `L4/krylov-step` Form A; the L4 v0.4 derived-view-hoisting rotation is captured in `concepts/derived-view-hoisting.md`; the L4 v0.5 first-iteration-unrolling form (retained below) is the canonical evidence for `concepts/first-iteration-unrolling`. Working Notes' unique findings (Palace bug-flag, CheckDot enumeration, unit-test-coverage absence, unpreconditioned-as-primary modeling) are hoisted into the stub header's 'Open questions still pending lift' subsection."

### Slice 3: `book/src/spec/slices/arnoldi_step.md` (330 lines)

**Audit verdict**: partial-reduction (full-reduction blocked by detailed L2 four-primitive composition + the variant-dependent L3 obstruction taxonomy + the FGMRES `Z[j]` teeing-off treatment).

**Supersession map**:
- §"Context" + §"Background" + §"Sources" (lines 1-35) → **partially** covered by [`L2/krylov-step` §"Pattern instances" (arnoldi cited), `L1-L0/ksp-solve-mutation-rotation` §"Sub-pattern C — inner GMRES body"]. **Unique material**: the slice's Saad 2003 textbook citation + the deviation enumeration (lines 16-18) is unique L0 methodology evidence; the slice's `test/unit/test-orthog.cpp:80-170, :234-280` test linkage (line 34) is unique parametric-test evidence that the firm L1>L0 theme does not enumerate.
- §"L0 — palace source" (lines 36-71; header at line 36, body through line 71) → covered by [`L1-L0/ksp-solve-mutation-rotation` §"Sub-pattern C" — workspace at hpp:190-194, inner Arnoldi loop at cpp:615-650, OrthogonalizeIteration at cpp:307-325]. The slice's four-line kernel decomposition (lines 41-47) is the precursor to the L2 entry's primitive-composition decomposition.
- §"L1 — invariants and procedure" (lines 72-120; header at line 72) → covered by [`L2/krylov-step` §Semantics (the arnoldi kernel pattern), `L1/orthogonalize` (NOT yet a firm L1 entry — this is a coverage gap)]. The slice's `arnoldi_step(V, j, T, gs_orthog) -> (V[j+1], H[:,j])` procedure (lines 100-104) is a precursor to a hypothetical firm `L1/orthogonalize` operator that has NOT been promoted. The slice's invariants section (lines 87-96) — input-precondition orthonormality, Arnoldi relation `T·V[j] = Σ H[i,j]·V[i]`, output postcondition, breakdown signal — is unique and not lifted to firm entries.
- §"L2 — primitive composition" (lines 121-177; header at line 121) → **partially** covered by [`L2/krylov-step` §Semantics]. The slice's four-primitive decomposition (apply_BA / orthogonalize / subdiag_norm / normalize) is more granular than the L2 entry's five-group decomposition (the L2 entry's "apply" subsumes apply_BA; "auxiliary" subsumes orthogonalize; "iterate-update" subsumes subdiag_norm + normalize). **Unique material**: the four-primitive ordering rigidity analysis (lines 156-164) is detailed only in the slice.
- §"L3 — tensor-field lift" (lines 178-246; header at line 178) → **partially** covered by [`L3/krylov-step` (cycle-010 wave-1, pending integration)]. **Unique material**: the variant-dependent L3 obstruction taxonomy (CGS / CGS2 lift cleanly; MGS carries sequential obstruction; lines 192-213) is detailed only in this slice and in `orthog.md`. The L3/krylov-step entry references the obstruction at the krylov-step level but does not enumerate the per-`gs_orthog`-variant lift details. The MPI-collective shape tabulation (lines 237-244: MGS = j+2 allreduces; CGS = 2; CGS2 = 3) is unique to this slice.
- §"L4 — calculus form" (lines 247-330) → **partially** covered by [`L4/krylov-step` (the Arnoldi instance is one of the four cited L4 sections per the Evidence list of L4/krylov-step.md:173)]. **Unique material**: the `ArnoldiSimState` / `ArnoldiOpParams` / `ArnoldiStepScratch` typing (lines 257-277) is the per-slice instantiation of the L4 three-stratum split (per L4/krylov-step §"Signature" "The two `OpParams` and `Krylov` records are slice-specific"). The `arnoldiStep :: ArnoldiOp -> SolveM ArnoldiSimState ()` monadic procedure (lines 284-298) is the canonical worked-example for the L4 `krylov-step` body shape applied to Arnoldi.

**Residual gaps** (blockers for full reduction):
1. The `orthogonalize` primitive is referenced as an L1 building-block but no firm `L1/orthogonalize` entry exists. **Lifting target**: harvester dispatch on `L1/orthogonalize` (or `L1/orthogonalize-column` per the slice's signature). This is a speculative L1 operator under the unimplemented-Palace-stub policy — it's implemented and firm material, so promotion criterion is "small AND simplifies higher forms". The variant-axis profile (`gs_orthog ∈ {MGS, CGS, CGS2}`) and the MPI-collective shape table are unique evidence justifying promotion.
2. The variant-dependent L3 obstruction taxonomy (MGS = sequential at L3; CGS = single batched gemv; CGS2 = two batched gemv) is not promoted to firm entries. **Lifting target**: a `concepts/sequential-obstruction` worked-example entry, or a separate `L3>L2/orthogonalize-mgs-sequential-obstruction` theme if one of the variants warrants a dedicated obstruction theme.
3. The `test/unit/test-orthog.cpp:80-170, :234-280` parametric test linkage is unique to this slice. **Lifting target**: a `scaffolding/test-linkages/orthog.md` entry per the standard test-linkage discipline.

**Recommended action**: **partial-reduction**.
- Stub sections that are fully superseded: §"L0 — palace source" (the four-line kernel decomposition is superseded by L2 `krylov-step`'s primitive composition; retain only the lazy-allocation note that documents `iterative.cpp:519-541`).
- Retain: §"Background" (textbook Saad 2003 citation + deviation enumeration), §"Sources" (test linkage), §"L1" (invariants — pending lift of `L1/orthogonalize`), §"L2" (four-primitive decomposition — more granular than L2/krylov-step), §"L3" (variant-dependent obstruction taxonomy — unique), §"L4" (Arnoldi-specific calculus form — slice instantiation of L4/krylov-step pattern; this is one of the four cited L4 sections per L4/krylov-step.md:173).
- Add a header note: "This slice is the precursor to the L2/L4 `krylov-step` entries' Arnoldi-pattern instantiation. The L0 source-line citations and the L2 four-primitive decomposition are superseded; the L1 invariants, L3 variant-dependent obstruction taxonomy, and L4 Arnoldi-specific calculus form are retained pending lift to a firm `L1/orthogonalize` entry and a `concepts/sequential-obstruction` worked-example."

## Recommendation

**Dispatch a triplet of integrator-per-report applications** that materialize the three slices' partial reductions per the audit verdicts above. Subsequent dispatches should handle the residual lift work surfaced as new OQs (see "Open questions" below).

Concretely, the proposed integrator actions per slice are encoded as proposed_changes blocks below.

## Proposed changes

### Proposed change 1: Partial reduction of `book/src/spec/slices/gmres.md`

```edit:book/src/spec/slices/gmres.md
[Replace lines 1-495 (the §"Slice: gmres" intro + §"L0 — cited regions" + §"L1 — pure-functional dataflow" + §"L1 Open questions" + §"L2 — primitive composition" + §"L3 — global tensor-field form" + §"L4" v0.1 sections) with a stub header that points at the firm entries; retain lines 497-1144 (§"L4 v0.2" through §"L4 v0.6") verbatim.

The stub header text:

# Slice: gmres (reduced)

This slice is the historical precursor to the cycle-005/006/007/008/009/010 krylov-step chain. The L1/L2/L3/L4-v0.1 forms below have been lifted to firm entries; this stub points at them and retains the unique material (the L4 v0.1→v0.6 self-rotation history) below.

**Firm entries that supersede this slice's L0/L1/L2/L3/L4-v0.1 content:**

- `book/src/L1/ksp_solve.md` (firm; cycle-007) — the variant-axis-collapsed L1 form. CG / GMRES / FGMRES all share the same `ksp_solve(K, b) -> SolveResult` signature; the per-method body is internal to `K`'s opaque type. This supersedes this slice's §"L1 — pure-functional dataflow".
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` (rough-in; cycle-008) — the mutation rotation theme. Sub-patterns A (outer `BaseKspSolver::Mult`) / B (CG body) / C (GMRES body) / D (FGMRES body) cover the L1>L0 rewrite. This supersedes this slice's §"L0 — cited regions" line-range citations.
- `book/src/L2/krylov-step.md` (firm; cycle-005) — the L2 primitive composition. Five primitive groups (apply, optional auxiliary, iterate-update, scalar-update, output-readout); GMRES instance cited. This supersedes this slice's §"L2 — primitive composition".
- `book/src/L3/krylov-step.md` (firm; cycle-010 wave-1) — the L3 value-threaded form with the sequential-obstruction recorded. This supersedes this slice's §"L3 — global tensor-field form" (the LS-update / back-solve sequential obstructions on small-dense state).
- `book/src/L3-L2/krylov-step-body-identity.md` (firm; cycle-009) — the L3>L2 identity-in-form theme.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (firm; cycle-008) — the L4>L3 typed-wrapper-dissolution theme.
- `book/src/L4/krylov-step.md` (firm; cycle-006) — the L4 typed wrapper Form A / Form B. This supersedes this slice's §"L4" v0.1 (the `SimState` / `OpParams` / `Krylov` typing, `solve_loop` / `restart_cycle` / `inner_loop` monadic structure, `Convergence` value).
- `book/src/L1-L0/minres-iteration.md` + `book/src/L1-L0/bicgstab-iteration.md` (firm; cycle-004) — the obstruction themes covering the unimplemented Krylov methods.

**Unique material retained below**: the L4 v0.2 → v0.3 → v0.4 → v0.5 → v0.6 self-rotation progression. This documents the canonical derivation of `build_convergence` / `classify_outcome` / `check_stop` / `StopReason`-witness extraction. These are load-bearing methodology evidence for `concepts/derived-view-hoisting.md` and a candidate `concepts/witness-typed-dispatch.md` (per v0.6 §"Open questions" line 1144). Pending lift to those concepts, the v0.2-v0.6 sections are retained verbatim.

**Open questions still pending lift (from the now-stubbed §"L1 Open questions"):**
- The L0.11a drift-warning compare (10% threshold at `iterative.cpp:592-600`) is not yet cited in firm entries. This is an observability hook on the LS-proxy-vs-true-residual numerical drift.
- The `givens_generate` / `givens_apply` L2 primitive vocabulary is not promoted as firm L1 operators (the firm L2 `krylov-step` stays at the five-group level and elides Givens-rotation primitives). Promotion criterion: simplifies higher forms — likely yes for the GMRES `ls_update_column` decomposition.

---

(L4 v0.2 — convergence-criterion absorption tightening, starting here, retained verbatim from the original slice...)
```
```

### Proposed change 2: Partial reduction of `book/src/spec/slices/cg.md`

```edit:book/src/spec/slices/cg.md
[Replace lines 1-366 (the §"Context" + §"L0" + §"L1" + §"L2" + §"L3" + §"L4" v0.1-v0.4 + §"Working Notes" + §"L4 v0.4 derived-view hoisting (self-rotation)" + §"L2→L3 rotation claims (retroactive, cycle 116)" sections — the L2→L3 retroactive section at lines 341-366 is moved to methodology-history per the recommended-action narrative) with a stub header; retain lines 367-506 (§"L4 v0.5 first-iteration-unrolling (self-rotation)" + §"L4 v0.5 (cycle 137) claim ratification") verbatim.

The stub header text:

# Slice: cg (reduced)

This slice is the cycle-001-era precursor to the firm CG row in the krylov-step chain. The L1/L2/L3/L4-v0.1-v0.4 forms have been lifted to firm entries; this stub points at them and retains the unique material below.

**Firm entries that supersede this slice's L0/L1/L2/L3/L4-v0.1-v0.4 content:**

- `book/src/L1/ksp_solve.md` (firm; cycle-007) — the variant-axis-collapsed L1 form. CG / GMRES / FGMRES share the same opaque `Solver[A]` type. Supersedes this slice's §"L1".
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` §"Sub-pattern B — inner CG body" (rough-in; cycle-008) — the L1>L0 rewrite for CG. Cites `iterative.cpp:360-486`, `:369-374`, `:377-386`, `:418-419`, `:427-464`, `:443`, `:448-449`, `:484-485`. Supersedes this slice's §"L0".
- `book/src/L2/krylov-step.md` (firm; cycle-005) — the L2 primitive composition. CG instance cited. Supersedes this slice's §"L2".
- `book/src/L3/krylov-step.md` (firm; cycle-010 wave-1) — the L3 value-threaded form. Supersedes this slice's §"L3" and the cycle-116 retroactive rotation_claim section.
- `book/src/L3-L2/krylov-step-body-identity.md` (firm; cycle-009) — the L3>L2 identity-in-form theme.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (firm; cycle-008) — the L4>L3 theme.
- `book/src/L4/krylov-step.md` (firm; cycle-006) Form A — supersedes this slice's §"L4" v0.1-v0.4 (the `CgState` / `cg_step` / `cg_solve` typing).
- `book/src/concepts/derived-view-hoisting.md` — supersedes this slice's §"L4 v0.4 derived-view hoisting (self-rotation)" rotation derivation (the residual-norm hoisting worked example).

**Unique material retained below** (the L4 v0.5 first-iteration-unrolling derivation): the canonical evidence for `concepts/first-iteration-unrolling.md`. The slice's `forget_beta_prev` projection making the v0.4-v0.5 equivalence formal, the `(first_step, steady_step)` signature derivation, and the closure-vs-state-field reasoning are load-bearing methodology evidence.

**Open questions still pending lift (from the now-stubbed §"Working Notes"):**

- The **initial-residual quirk** in the `!B && initial_guess` branch (`iterative.cpp:399-412`): Palace computes `initial_res = (b·b)^{1/4}` rather than `‖b‖₂` due to a `Norml2`-vs-`Dot` asymmetry between the unpreconditioned and preconditioned branches. This is a likely Palace bug; lift target is an annotation in `L1-L0/ksp-solve-mutation-rotation` Sub-pattern B or a `scaffolding/open-questions.md` entry flagging upstream confirmation needed.
- The **`CheckDot` partial-function guard** at `iterative.cpp:244-250` invoked at lines 396/412/444/461: the firm L1>L0 theme recognises CheckDot but does not enumerate per-call-site. Lift target is per-call-site `verified_against` rows.
- The **unpreconditioned-as-primary L4 modeling** choice (preconditioned-CG-as-variant via `forget_z`): inverts Palace's always-preconditioned source structure. Lift target is `concepts/state-stratification` or a presentation-choice note in `L4/krylov-step`.
- The **unit-test coverage gap**: no unit tests under `test/unit/` reference `CgSolver` or `PCG` directly. CG is exercised only via integration tests at `test/examples/`. Lift target is a `scaffolding/test-linkages/cg.md` entry noting the gap.

---

(L4 v0.5 — first-iteration unrolling (self-rotation), starting here, retained verbatim from the original slice...)
```
```

### Proposed change 3: Partial reduction of `book/src/spec/slices/arnoldi_step.md`

```edit:book/src/spec/slices/arnoldi_step.md
[Replace lines 36-71 (§"L0 — palace source" — the four-line kernel decomposition that is fully superseded by L2 `krylov-step`; section spans lines 36 (`## L0 — palace source` header) through 71 (last content line before §"L1" at line 72)) with a stub note; retain lines 1-35 (§"Context", §"Background", §"Sources"), lines 72-120 (§"L1 — invariants and procedure" — header at line 72, ending before §"L2" at line 121), lines 121-177 (§"L2 — primitive composition" — four-primitive decomposition more granular than firm L2/krylov-step's five-group decomposition; ending before §"L3" at line 178), lines 178-246 (§"L3 — tensor-field lift" — variant-dependent obstruction taxonomy unique; ending before §"L4" at line 247), and lines 247-330 (§"L4 — calculus form" — Arnoldi-specific calculus instantiation, one of the four cited L4 sections in L4/krylov-step.md:173). Add a header note at line 1 pointing at firm entries.

The header note (inserted at line 1, after the `# arnoldi_step` line):

> **Reduction status (cycle-010+):** the L0 source-line citations below are superseded by `book/src/L1-L0/ksp-solve-mutation-rotation.md` §"Sub-pattern C — inner GMRES body" (workspace at hpp:190-194; inner Arnoldi loop at cpp:615-650). Retained material: §L1 invariants, §L2 four-primitive decomposition (more granular than firm L2/krylov-step), §L3 variant-dependent obstruction taxonomy (MGS sequential / CGS-CGS2 lift), §L4 Arnoldi-specific calculus form (cited from L4/krylov-step.md:173 as one of the four canonical L4 worked-example sections).
>
> **Pending lift to firm entries**: a firm `L1/orthogonalize` (or `L1/orthogonalize-column`) operator covering the slice's residual-axis-disclosed `gs_orthog ∈ {MGS, CGS, CGS2}` variant; a `concepts/sequential-obstruction` worked-example covering the MGS-only L3 obstruction; a `scaffolding/test-linkages/orthog.md` entry for the `test/unit/test-orthog.cpp:80-170, :234-280` parametric tests.

The replacement for lines 36-71 §"L0 — palace source":

## L0 — palace source

The L0 four-line kernel decomposition (`ApplyBA → OrthogonalizeIteration → Norml2 → in-place scal` at `palace/linalg/iterative.cpp:621-628`) is now firm at `book/src/L1-L0/ksp-solve-mutation-rotation.md` §"Sub-pattern C — inner GMRES body". The lazy-allocation pattern (`Update(j)` at lines 519-541, triggered when `V[j+1].Size() == 0`) and the FGMRES `Z[j]` teeing-off pattern (lines 707-731 + 794-822) are documented there. See also `book/src/L0/linalg-iterative-file.md` for the per-method bodies' L0 anchor chapter.
```
```

## Supporting evidence

- `book/src/spec/slices/gmres.md` (1144 lines; read lines 1-1144 across two reads). The L4 v0.2-v0.6 self-rotation progression spans lines 497-1144; this is unique methodology evidence not lifted to firm entries.
- `book/src/spec/slices/cg.md` (506 lines; read lines 1-506). The L4 v0.5 first-iteration-unrolling derivation spans lines 368-506; this is unique evidence for `concepts/first-iteration-unrolling`. The initial-residual quirk treatment at line 95 + Working Notes line 286 is unique.
- `book/src/spec/slices/arnoldi_step.md` (330 lines; read lines 1-330). The L1 invariants section (lines 87-96), L2 four-primitive decomposition (lines 121-177), L3 variant-dependent obstruction taxonomy (lines 192-213), and L4 Arnoldi-specific calculus form (lines 247-330) are unique. The `test/unit/test-orthog.cpp:80-170, :234-280` parametric test linkage at line 34 is unique.
- `book/src/L1/ksp_solve.md` (144 lines; read in full). Variant-axis-collapsed L1 form with CG / GMRES / FGMRES absorbed into opaque `Solver[A]` type.
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` (788 lines; read in full). Sub-pattern A (outer `BaseKspSolver::Mult`) / B (CG body) / C (GMRES body) / D (FGMRES body) decomposition with `verified_against` rows at lines 547-687 (§"Verified-against" header at line 547, body through line 687, §"Status" at line 688).
- `book/src/L2/krylov-step.md` (172 lines; counted, not fully re-read this dispatch; relies on prior context).
- `book/src/L4/krylov-step.md` (176 lines; read in full). Form A / Form B signatures, evidence list at lines 169-174 citing four canonical slice L4 sections.
- `book/src/L3/` directory (only `index.md` — the firm L3/krylov-step from cycle-010 wave-1 dispatch #1 has a CYCLE.md at `reports/2026-05-27T215300Z-harvester-l3-krylov-step/` but has NOT yet been integrated to `book/src/L3/krylov-step.md` as of this dispatch; the report is pending integration).
- `CLAUDE.md` §Methodology invariants ("Phase 1 corpus reduces as material is lifted", added cycle-009 meta-batch-1).
- `scaffolding/priorities.md` #19 (`phase-1-corpus-reduction-audit`).

## Open questions / caveats

1. **The cycle-010 wave-1 dispatch #1 (`harvester-l3-krylov-step`) has produced a CYCLE.md but has NOT yet been integrated.** The audit verdicts above reference `L3/krylov-step.md` as "firm; cycle-010 wave-1" but the file does NOT exist on disk yet as of this dispatch — only `book/src/L3/index.md` exists (empty placeholder). The proposed_changes for slice reductions assume the L3/krylov-step backfill lands first. If integration order during cycle-010 finalize places the slice reductions before the L3/krylov-step backfill, the reduction proposed_changes for gmres.md / cg.md / arnoldi_step.md should be deferred until L3/krylov-step lands. **Recommendation**: integrator-finalize for cycle-010 should sequence L3/krylov-step before any slice-reduction proposals.

2. **The L4 v0.1→v0.6 self-rotation history in gmres.md is unique methodology evidence pending extraction to concepts/.** Three possible lift targets surfaced:
   - `concepts/derived-view-hoisting.md` (v0.4 commit-layer hoist + v0.6 witness-layer hoist) — likely the cleanest target.
   - A candidate `concepts/witness-typed-dispatch.md` (per v0.6 §"Open questions" line 1144) — promotion criterion is "second instance lands". No second instance has landed yet; defer concept extraction.
   - The slice itself, retained as canonical worked-example evidence — this is the current proposed action.
   **OQ to add to `scaffolding/open-questions.md`**: "Should the L4 v0.1→v0.6 self-rotation derivation in `book/src/spec/slices/gmres.md` lines 497-1144 be lifted to `concepts/derived-view-hoisting.md` as a multi-step worked example, or retained as slice-level methodology evidence? Promotion would unblock further reduction of gmres.md."

3. **The initial-residual quirk in cg.md (likely Palace bug) needs a decision on lift path.** Three options:
   - Annotate `L1/ksp_solve.md` Semantics with the bug-flag.
   - Add a `verified_against` row to `L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B noting the quirk.
   - File as a `scaffolding/open-questions.md` entry flagging upstream confirmation.
   **OQ to add**: "The Palace `!B && initial_guess` branch (`palace/linalg/iterative.cpp:399-412`) computes `initial_res = (b·b)^{1/4}` rather than `‖b‖₂` due to a `Norml2`-vs-`Dot` asymmetry. Likely Palace bug. Where in the firm artifact should this finding live, and should it be confirmed with upstream before being annotated as a firm finding?"

4. **The `L1/orthogonalize` operator is referenced from arnoldi_step.md and orthog.md but is not firm.** Promotion would simplify the L2/krylov-step entry by giving the "auxiliary" stage a concrete L1 operator. Promotion criterion (small AND simplifies higher forms) is plausibly met: orthogonalize is small (one variant-dispatched primitive), and lifting it would let L4/krylov-step Form A reference `op.orthog` as a firm L1 operator type rather than as a slice-level concept. **OQ to add**: "Should a firm `L1/orthogonalize` (or `L1/orthogonalize-column`) operator be promoted from the speculative slice corpus? Promotion would unblock simpler reduction of `arnoldi_step.md` and `orthog.md`."

5. **This first-instance audit covers 3 of 10 slices.** Remaining slices for subsequent cycle audits: `cg_preconditioning_framework.md`, `chebyshev.md`, `divfree.md`, `orthog.md`, `plane_rotation_stream.md`, `polynomial_recurrence_step.md`, `sparse_triangular_solve.md`. Suggested priority for cycle-011+ audits (in rough order of expected supersession overlap):
   - `orthog.md` — overlaps `L1/orthogonalize` (pending promotion); ties into arnoldi_step audit closure.
   - `chebyshev.md` — likely overlaps `L2/krylov-step` polynomial-recurrence variant.
   - `polynomial_recurrence_step.md` — overlaps `L2/krylov-step` polynomial-recurrence variant.
   - `divfree.md` — overlaps `L1/ksp_solve` use pattern (cited as the canonical use site in `L1/ksp_solve` §Evidence).
   - `cg_preconditioning_framework.md` — likely overlaps `L1/ksp_solve` + `L4/krylov-step` Form A.
   - `plane_rotation_stream.md` — likely overlaps `L2/krylov-step` Givens-rotation pattern (could promote `givens_generate` / `givens_apply` as firm L1).
   - `sparse_triangular_solve.md` — likely a low-overlap slice (no firm krylov-chain analog); defer or audit separately.

6. **The audit template established here (Supersession map / Residual gaps / Recommended action / Proposed changes) is machine-replayable.** Subsequent cycle-011+ slice audits should reuse this template directly. The audit per slice is moderately expensive (each slice read in full + cross-reference to ~5-8 firm entries); the per-cycle batch should bound to 2-4 slices to keep dispatches within context budget.

7. **Caveat: no slice file is mutated by this dispatch.** All proposed reductions are encoded as `proposed_changes` blocks for integrator-per-report. The verdicts and supersession maps in this CYCLE.md are inspection-only.

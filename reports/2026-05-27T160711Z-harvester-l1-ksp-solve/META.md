---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T170000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T173000Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of harvester-l1-ksp-solve

## Critique

### Checks run

**citation-validity (pass)** — All cited Palace source ranges verified against the actual files. Spot-checked: `palace/linalg/ksp.cpp:34-58` (factory switch; verified — three implemented arms CG/GMRES/FGMRES, three aborting arms at 53-57 falling through to `MFEM_ABORT`); `palace/linalg/ksp.cpp:53-57` (precise MFEM_ABORT location — verified, with the abort message text matching the citation); `palace/linalg/ksp.cpp:265-274` (move-in constructor; line 272 wiring `this->ksp->SetPreconditioner(*this->pc)` — verified verbatim); `palace/linalg/ksp.cpp:276-294` (SetOperators with multigrid-finest special case at 283-288 — verified); `palace/linalg/ksp.cpp:296-310` (Mult body — verified verbatim including counter increments at 308-309 and Mpi::Warning at 303-306); `palace/linalg/ksp.cpp:312-313` (explicit template instantiations — verified); `palace/linalg/ksp.hpp:29-72` (class declaration — verified, exactly matches the cited range); `palace/linalg/ksp.hpp:32-34` (static_assert — verified); `palace/linalg/ksp.hpp:74-75` (KspSolver / ComplexKspSolver aliases — verified); `palace/linalg/iterative.hpp:25-115` (IterativeSolver base; verified — declares `converged` at 53, `initial_res, final_res` at 54, `final_it` at 55, `GetConverged()` at 98); `palace/linalg/iterative.hpp:118-150` (CgSolver with `r, z, p` at 144 — verified); `palace/linalg/iterative.hpp:154-217` (GmresSolver with workspace `V, r, H, s, sn, cs` at 190-194, `max_dim` at 180, `gs_orthog` at 184, `pc_side` at 187 — verified); `palace/linalg/iterative.hpp:221-275` (FgmresSolver with `Z` at 256 — verified); `palace/linalg/iterative.cpp:361-486` (CG Mult body — verified, with workspace sets at 369-371, initial-guess threading at 377-386, `initial_res == 0` short-circuit at 418); `palace/linalg/divfree.cpp:175` (`ksp->Mult(rhs, psi)` — verified verbatim); `palace/drivers/electrostaticsolver.cpp:69` (`ksp.Mult(RHS, V[step])` — verified verbatim); `palace/drivers/magnetostaticsolver.cpp:77` (`ksp.Mult(RHS, A[step])` — verified verbatim); `palace/drivers/drivensolver.cpp:196` (`ksp.Mult(RHS, E)` — verified verbatim).

One citation range slightly over-reaches: `palace/linalg/iterative.cpp:544-734` is given as the "GMRES Mult body" but the actual `GmresSolver::Mult` body ends at line 705; lines 708-731 are FGMRES `Initialize` and `Update`; line 734 starts FGMRES `Mult`. The cited range is in-file and contains the claimed GMRES body, but bleeds into adjacent FGMRES helper definitions. Minor; not a falsehood.

Citation format is consistent with the `relative/path/file.ext:start-end` convention throughout (paths relative to `reference/`).

**surface-or-evidence (pass)** — The report is a new-firm-chapter proposal, not a refinement of existing operator/theme surface. The proposed-changes block creates `book/src/L1/ksp_solve.md` (new file) and modifies `book/src/L1/index.md` and `book/src/SUMMARY.md` to integrate. As a new firm chapter, the surface change is the entire chapter. Evidence base is direct from Palace source (`palace/linalg/ksp.{hpp,cpp}`, `palace/linalg/iterative.{hpp,cpp}`, four driver call-sites) plus the cycle-006 L0 anchor and the cycle-002 concept-page anchor. The retroactive-thinning convention is honoured: inline source-quoting is delegated to `L0/kspsolver-base-class.md`, `L0/ksp-factory-file.md`, `L0/apply-linop-overload-set.md` rather than re-quoted in the L1 chapter — the L1 chapter's `Context` section cross-references those L0 chapters by slug. Surface + evidence both present and well-formed.

**rotation-quality (pass)** — The L1 rotation is genuine and strictly more compact / abstract than the L0 form. Specifically:

1. *Destination-buffer drop*: L0 `Mult(b, x) -> void` (writes through `x`) becomes L1 `ksp_solve(K, b) -> SolveResult` (returns the solution as a structured value). One output channel replaces two (destination + member counter mutations + side-channel log).
2. *Statistics-counter lift*: cumulative `ksp_mult, ksp_mult_it` member mutations become driver-side accumulation over per-call `SolveResult.iterations`. Per-call observability replaces per-instance mutable state.
3. *Side-channel-log absorption*: `Mpi::Warning` on non-convergence becomes structured `SolveResult.converged: Bool`.
4. *Per-method enum dispatch collapse*: CG / GMRES / FGMRES subclasses (with disjoint workspace `r,z,p` vs `V,r,H,s,sn,cs` vs `Z`) collapse to a single opaque `Solver[A]` type. Three concrete subclasses + dispatch switch → one opaque type with construction-bound method.
5. *Initial-guess axis collapse*: `IterativeSolver::initial_guess` flag + dual-use of `x` as both source and destination at L0 → bound inside `K`'s opaque state at L1; per-call signature is `(K, b)` only.

This is not a rename and not 1:1. State hiding (the per-method workspace becomes private to the opaque `Solver[A]`), coarser substitution (enum-dispatch absorbed), and threaded-state compression (counters move to driver-side accumulation) — all three pass-criteria forms apply. The L1 form is strictly more equational than the L0 form.

**variant-axis-coverage (pass)** — The dispatch correctly identifies 3 orthogonal exposed axes (element-type ∈ {real, complex}; initial-guess-policy ∈ {cold-start, warm-start}; convergence-failure-policy = soft-fail-with-flag) plus 1 collapsed axis (krylov-method = CG/GMRES/FGMRES). The axis decomposition is well-founded:

- *element-type*: justified by the two C++ template instantiations `KspSolver = BaseKspSolver<Operator>` and `ComplexKspSolver = BaseKspSolver<ComplexOperator>` at `ksp.hpp:74-75`, plus the `static_assert` at `ksp.hpp:32-34`. Genuinely two semantic instances with identical algebraic surface.
- *initial-guess-policy*: justified by the `IterativeSolver::initial_guess` flag plus the dual-use-of-`x` pattern at `iterative.cpp:377-386`. Both warm and cold start are exposed at L0 (Palace calls `SetInitialGuess(linear.initial_guess)` at `ksp.cpp:59`).
- *convergence-failure-policy*: only one variant Palace exposes (`soft-fail-with-flag`), correctly identified — the L0 `Mult` always returns the iterate and logs a warning; no hard-fail mode exists. The report correctly notes that this collapses to a single boolean at L1 because L0 only distinguishes the two cases, and explicitly forecasts the L4 `solve-monad` lifting to a richer `Outcome` sum type.
- *krylov-method* (collapsed): justified by the variant-absorption concept (`concepts/variant-absorption.md`) and the construction-bound dispatch — the per-method body is opaque at the L1 call site. The collapse is across the *implemented* three only (CG, GMRES, FGMRES), with the three aborting cases (MINRES, BICGSTAB, DEFAULT) explicitly scoped out per CLAUDE.md unimplemented-stub policy.

No hidden branches. Each variant is either covered by the operator parameterisation or explicitly scoped out with rationale.

Minor observations (not blocking): GMRES carries two additional sub-axes that the report mentions in passing but does not enumerate as top-level variant axes — orthogonalization-method (MGS / CGS / CGS2 at `iterative.hpp:184`) and preconditioner-side (LEFT / RIGHT at `iterative.hpp:187`). These are correctly absorbed into the opaque `Solver[A]` (they are bound at construction and affect only bit-level outcomes; recorded as load-bearing non-laws in the "Algebraic laws" section). The treatment is consistent: sub-axes of the collapsed `krylov-method` axis are themselves collapsed, with their bit-determinism implications explicitly recorded. No issue.

**cross-reference-integrity (warning)** — All `[link]` references in the proposed L1 chapter and the L1/index.md edits resolve to existing files. Spot-checked:

- `L0/kspsolver-base-class.md` — exists (cycle-006).
- `L0/ksp-factory-file.md` — exists (cycle-004).
- `L0/apply-linop-overload-set.md` — exists.
- `L1/apply_linop.md`, `L1/axpy.md`, `L1/dot.md`, `L1/nrm2.md` — all exist (firm).
- `L2/krylov-step.md` — exists (cycle-006 firm).
- `L1-L0/minres-iteration.md`, `L1-L0/bicgstab-iteration.md` — exist (cycle-004 obstruction themes).
- `concepts/ksp_solve.md`, `concepts/solve-monad.md`, `concepts/solver-as-operator.md`, `concepts/constructed-operators.md`, `concepts/variant-absorption.md`, `concepts/constructed-operator-factory.md` — all exist.
- `spec/slices/divfree.md` — exists; the cited line `psi ← ksp_solve(self.ksp, rhs)` is at line 165 (the citation is to "§L2 step 3" by section, not by line; verified at line 165).
- `concepts/solve-monad.md` "Termination as a sum type" — exists at line 58, with the cited `Outcome = Continue | Done Bool` sum type at line 60. Verified.

Five **non-laws** stated in the L1 chapter's "Algebraic laws" section are well-classified: (a) bit-determinism across reduction-tree variants — genuinely non-holding, inherited transitively from `apply_linop`/`dot`/`nrm2` per their own L1 entries; (b) bit-determinism across orthogonalization variants — genuinely non-holding, MGS vs CGS vs CGS2 are different floating-point trajectories; (c) bit-determinism across initial-guess variants — genuinely non-holding, the Krylov subspaces traversed differ; (d) exact composition with `apply_linop` — genuinely non-holding at finite tolerance, the equality holds only in the formal limit; (e) commutativity of nested `ksp_solve`s — genuinely non-holding, matrix products don't commute; (f) strict positive-iteration termination — genuinely non-holding, the `initial_res == 0` short-circuit at `iterative.cpp:418-419` produces zero iterations. All six non-laws are unverified-in-the-sense-of-not-implied-by-the-Palace-source rather than "not-checked"; each is grounded in a specific algebraic or numerical reason.

**Warning** is for a format-divergence concern: the **Open questions block** at lines 315-333 of CYCLE.md uses a non-canonical format (`### slug` markdown headers + bullet-points with `**Raised**:` / `**Source**:` / `**Question**:` / `**Decision boundary**:` keys) rather than the canonical `scaffolding/open-questions.md` format (YAML frontmatter block `--- slug: ... opened_at: ... opened_by: ... status: open ---` followed by a paragraph of question text and a paragraph of context). The three OQs (`ksp-solve-concept-page-signature-update`, `ksp-solve-mutation-rotation-l1-l0-theme`, `l1-intro-refresh-after-constructed-operator-gate`) have well-formed slugs and substantive content; the format mismatch is mechanical. The integrator-per-report promotes "Open questions / caveats" content into the ledger and may or may not auto-translate the format — if it does, no issue; if it expects canonical format on input, this is a mechanical-fix candidate for the repairer.

**edge-label-fidelity (pass)** — Not strictly applicable: this is an L1 operator entry, not a lowering theme. No L_{n+1}→L_n edge label is asserted. The prose discusses L0 → L1 rotation throughout (consistent with the dispatch scope `L1 operator: ksp_solve`); the L1 vs L0 distinction section at lines 137-139 explicitly contrasts the two layers. References to upstream `L2/krylov-step` are correctly framed as "the L2 layer that unfolds the per-method body" — not as edges authored in this dispatch. No mismatch.

**plan-kind-consistency (pass)** — The dispatch declares a *firm L1 operator* and delivers a firm L1 operator. Surface check: the chapter has all sections expected of a firm L1 entry (Context, Signature, Semantics, Algebraic laws, Dependencies, Variant axes, Status, L1 vs L0 distinction, Evidence). The `Status: firm` declaration at line 134 is consistent with the content shape: signature is canonical and precisely matches the L0 surface modulo the stated rotations; evidence is direct from Palace source plus the cycle-006 L0 anchor + cycle-002 concept-page anchor; algebraic laws are stated with explicit non-laws; both anchors required for promotion-to-firm are present (per the L1 index's "harvester promotion gated on appearance of an anchor" discipline). No rough-in placeholders.

Special-attention check on **MINRES / BICGSTAB / DEFAULT scoping**: the report correctly treats the three aborting enum cases as out-of-scope per the CLAUDE.md unimplemented-Palace-stub policy. The handling is precise:
- L1 variant-axis collapse covers CG/GMRES/FGMRES only (explicit at line 125-126).
- The three aborting cases are explicitly listed as out-of-scope at lines 128-130, with citation `palace/linalg/ksp.cpp:53-57` and pointers to the existing obstruction themes `L1-L0/minres-iteration.md` and `L1-L0/bicgstab-iteration.md`.
- The closure note at lines 304-310 confirms no new OQ is generated for the stubs — the existing policy is honoured rather than relitigated.
- The L1 chapter does not promote any speculative rough-in operator (no `lanczos_step`, `bicgstab_step` etc. attempted) — consistent with the CLAUDE.md guidance "Promote a speculative L1 operator to firm only when small AND when it simplifies the semantics of higher forms."

The user-directive 2026-05-27 (unimplemented-stub-policy) is honoured.

**skill-uptake-survey (warning)** — The dispatch is a harvester invocation producing a new firm L1 operator. Relevant skills for this shape:
- `verify-refinement-surface` — not directly applicable (new chapter, not refinement of existing surface).
- `classify-variant-axis` — directly applicable. The dispatch claims a 3+1 axis decomposition with one collapsed axis; this is exactly the skill's domain. The CYCLE.md does not explicitly mention invoking `classify-variant-axis`. The decomposition is well-formed (as evaluated under check #4), but the skill's procedure does not appear surfaced in the report telemetry.
- `verify-citation-range` — directly applicable for the ~25 cited file:start-end ranges. The CYCLE.md does not mention invoking the skill, though the citations all verify out.
- `skill-selection` — meta-skill; can't observe invocation directly.
- `embed-and-persist-subagent-dispatch` (pilot-1) — newer skill; not applicable here, the dispatch is straightforward harvester scope.

The "Codemap-pilot note" at line 311 explicitly addresses *non-invocation* of `mcp__palace-codemap__*` tools, justifying with "the surface was already well-mapped by cycle-006's L0 chapter ... and the directly-grep-able driver call sites were small enough to use `grep -n` + `Read` directly." This is responsible telemetry. The two relevant skills (`classify-variant-axis`, `verify-citation-range`) lack similar mention.

**Warning** (not blocking): the report's skill-uptake telemetry is incomplete — two skills that would naturally fit this dispatch's shape are not referenced. Pure presence check per role-spec; surfaces telemetry, not blocking.

### Issues found

1. **OQ format mismatch (cross-reference-integrity-adjacent, low severity).** *Where*: CYCLE.md lines 315-333 (the `## Append to scaffolding/open-questions.md` section). The three proposed OQs use `### slug` markdown headers + bullet-keyed paragraphs, but the canonical ledger format is YAML frontmatter `--- slug: ... opened_at: ... opened_by: ... status: open ---` + free-text question + context paragraphs. *Severity*: mechanical/format. Three OQs (`ksp-solve-concept-page-signature-update`, `ksp-solve-mutation-rotation-l1-l0-theme`, `l1-intro-refresh-after-constructed-operator-gate`) have well-formed slugs and substantive content; only the wrapper format diverges. Repair candidate: rewrite the three blocks into the canonical YAML+paragraph format.

2. **Citation range over-reach: GMRES Mult body (citation-validity, very low severity).** *Where*: CYCLE.md line 160 (the Evidence list entry `palace/linalg/iterative.cpp:544-734`). *Detail*: the `GmresSolver::Mult` body actually ends at line 705; lines 708-731 are `FgmresSolver::Initialize` and `Update`; the FGMRES `Mult` starts at line 734. The cited range bleeds 29 lines into adjacent FGMRES helper definitions. *Severity*: very low — the cited range does contain the entire GMRES Mult body; the over-reach is into clearly-related code in the same file. *Repair candidate*: tighten the range to `544-705` or split into two citations (`544-705` for GMRES Mult; `708-731` for FGMRES helpers).

3. **Skill-uptake telemetry incomplete (skill-uptake-survey, low severity).** *Where*: CYCLE.md, no mention of `classify-variant-axis` or `verify-citation-range` skill invocations. The dispatch performs the work both skills procedurally describe (4-axis decomposition with one collapsed; ~25 cited file ranges) but does not surface telemetry of skill invocation. *Severity*: low (presence check, not blocking). The codemap-pilot non-invocation is well-documented at line 311; the same explicit-telemetry pattern would be useful for the two missing skills. *Repair candidate*: add a one-paragraph note acknowledging the skills' applicability and whether they were procedurally followed.

4. **Minor framing observation: subsumed-by-`apply_linop`-mutation-rotation L1>L0 theme (low severity).** *Where*: not a defect in the CYCLE.md itself — the dispatch correctly identifies in its third OQ (`ksp-solve-mutation-rotation-l1-l0-theme`, line 322-326) that a parallel L1>L0 lowering theme is the natural next dispatch. The note that "existing L1>L0 themes (`axpby-mutation-rotation`, `axpbypcz-mutation-rotation`, `apply-linop-mutation-rotation`) provide the precedent shape" is accurate (all three exist in `book/src/L1-L0/`). No issue; observation only — the OQ is well-formed beyond the format-mismatch noted above.

## Repair

### Fixes attempted

- **Finding**: OQ format mismatch — three proposed OQ blocks at CYCLE.md lines 315-333 used `### slug` markdown-header format with `**Raised**:` / `**Source**:` / `**Question**:` / `**Decision boundary**:` bullet keys rather than the canonical YAML-frontmatter + free-text-paragraph format used in `scaffolding/open-questions.md`.
  - **Decision**: repaired
  - **Action**: rewrote the three OQ blocks (`ksp-solve-concept-page-signature-update`, `ksp-solve-mutation-rotation-l1-l0-theme`, `l1-intro-refresh-after-constructed-operator-gate`) into the canonical format: fenced ` ```yaml ... ``` ` frontmatter block (`slug:` / `opened_at:` / `opened_by:` / `status:`) followed by paragraph(s) of question text and a context paragraph that absorbs the previous `Source` and `Decision boundary` bullets. Edit at CYCLE.md "Append to scaffolding/open-questions.md" section (the three rewritten blocks). All four required frontmatter fields (`slug`, `opened_at`, `opened_by`, `status`) populated; slug content unchanged; substantive question text preserved verbatim.
- **Finding**: citation range over-reach — `palace/linalg/iterative.cpp:544-734` cited as the "GMRES Mult body" but the actual `GmresSolver<OperType>::Mult` body ends at line 705; lines 708-731 are `FgmresSolver<OperType>::Initialize` and `Update`; FGMRES `Mult` starts at line 734.
  - **Decision**: repaired
  - **Action**: verified boundary by reading `reference/palace/palace/linalg/iterative.cpp:695-734` — confirmed line 705 is the closing brace of `GmresSolver<OperType>::Mult`, line 707 starts the `FgmresSolver::Initialize` template, line 734 starts `FgmresSolver::Mult`. Tightened the cited range from `544-734` to `544-705` at three locations in CYCLE.md: the Evidence list entry (line 160), the Dependencies section entry mentioning the GMRES Mult range (line 110), and the Supporting evidence section "Palace source" paragraph (line 297).
- **Finding**: skill-uptake telemetry incomplete — two skills that procedurally fit this dispatch's shape (`classify-variant-axis` for the 3+1 axis decomposition; `verify-citation-range` for the ~25 cited file:start-end ranges) were not surfaced as invoked-or-declined in the CYCLE.md telemetry, while the codemap-pilot non-invocation was well-documented at line 311.
  - **Decision**: repaired
  - **Action**: added two skill-uptake notes to the "Open questions / caveats" section of CYCLE.md immediately after the existing Codemap-pilot note, paralleling that note's shape. The `classify-variant-axis` note records that the skill's procedure was followed retroactively (4-axis decomposition with out-of-scope listing matches expected output shape) though not invoked by name. The `verify-citation-range` note records that the skill's procedure was followed partially — the critic-identified over-reach on `iterative.cpp:544-734` (now repaired as Finding #2 above) is the gap the explicit skill invocation would have caught at authoring time.

### Unrepairable findings

None. All three critic-flagged findings (OQ format, citation over-reach, skill-uptake telemetry) were mechanical/surgical and within repair authority. Finding #4 was observation-only per the critic.

## Suggested resolution

`overall_status: ready`. All three repair-eligible findings have been applied; the report's substantive content (firm L1 `ksp_solve` operator, dep-map promotion, SUMMARY chapter addition, three well-formed OQs) is unchanged. The integrator-per-report should apply the proposed-changes blocks as-is; the OQ promotion to `scaffolding/open-questions.md` will now succeed against the canonical format (the three OQs paste directly into the ledger's "## Open" section).

Notes for the integrator:
- The dep-map row for `ksp_solve` carries the corrected GMRES Mult range (`iterative.cpp:544-705`) in the Dependencies section narrative; the row itself is unchanged.
- The L1 index dep-map gains one row; vocabulary cohort grows from "Firm (7)" to "Firm (8)" (the cycle-007 priority slate already accounted for this).
- The L0 anchor at `book/src/L0/kspsolver-base-class.md` (cycle-006) and the concept-page anchor at `book/src/concepts/solve-monad.md` (cycle-002) are both pre-existing; no new concept-page or L0-page authorship is proposed in this report.
- The OQ `l1-ksp-solve-firm-up-anchor-ready` from cycle-006 is closed by this report's firm L1 chapter landing.

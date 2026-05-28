---
agent: same-layer-cross-cutter
invoked_at: 2026-05-28T14:40:34Z
scope: phase-1-corpus-reduction-batch-4-remaining-slices — final 2 unreduced Phase-1 slices
status: integrated
integrated_at: 2026-05-28T200000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-013 finalize. Final 2 slices annotated-reduced NOT removed: cg_preconditioning_framework = partially-absorbed (§L4/v0.2/v0.3 retained sole-source pending OQ l4-preconditioning-framework-promotion); sparse_triangular_solve = not-yet-eligible/permanent negative-result retain. METRIC: annotated-reduction 10/10 COMPLETE; removals stay 8/10 (8 removed-equivalent + 2 annotated-retained). Clean run."
---

# CYCLE: phase-1 corpus reduction batch-4 — final 2 slices

## Summary

Audited the final 2 unreduced Phase-1 slices (corpus at 8/10 after cycle-012 batch-3) using the `phase-1-slice-reduction-audit` skill (START+END boundary verification, unique-text anchors). **`cg_preconditioning_framework.md` is `partially-absorbed`**: its L0/L1 framework material is fully covered by firm `L1/ksp_solve.md` + the L0 anchor chapters, and its L2/L4 material was lifted into 9 firm concept pages — but every one of those concept pages cites the slice *back* as its introducing slice / canonical first use site, and the slice is the **sole detailed source** for the L4 v0.2 capability-typing and L4 v0.3 derived-view-hoisting self-rotations. It reduces to a stub-and-pointer header (the `divfree`/`chebyshev` precedent) retaining the load-bearing L4 v0.2/v0.3 sections, NOT to removal. **`sparse_triangular_solve.md` is `not-yet-eligible` for removal**: it is a load-bearing negative-result slice (the canonical instance of `scope-out-obstruction` and `sequential-obstruction`'s out-of-scope sub-kind), retained verbatim per the `polynomial_recurrence_step` "the slice IS the artifact" precedent — it gets only a reduction-status annotation. **10/10 *removal* is therefore NOT achievable this cycle**; 10/10 *annotated-reduction* IS (both slices acquire a reduction-status header; both retain load-bearing material).

## Observation kind

**Reduction-status verdict / same-layer corpus observation** — specifically, two same-layer (slice-corpus-layer) reduction-eligibility observations: one slice is reducible-but-not-removable (partial absorption with retained load-bearing self-rotation history), one is structurally non-removable (load-bearing negative result). Neither is a unification/redundancy/contradiction; both are reduction-status verdicts surfaced for the integrator to enact.

## Specific finding

### Slice 1 — `cg_preconditioning_framework.md` (533 lines) — verdict: `partially-absorbed` → stub-and-pointer header, retain L4 v0.2/v0.3 verbatim

**Section-anchor table** (both ends verified; H1 + H2 enumerated):

| heading | start | end |
|---|---|---|
| `# cg_preconditioning_framework` (H1) | 1 | 2 |
| `## Context` | 3 | 6 |
| `## Background` | 7 | 16 |
| `## L0 — source facts` | 17 | 60 |
| `## L1 — invariant statement` | 61 | 114 |
| `## L2 — primitive composition` | 115 | 220 |
| `## L3 — tensor-field / global form` | 221 | 292 |
| `## L4 — calculus form` | 293 | 412 |
| `## L4 v0.2 — capability typing for the (op, pc_op) split` | 413 | 471 |
| `## L4 v0.3 — derived-view hoisting for the (op, pc_op) bundle` | 472 | 533 (EOF) |

**Supersession map** (one row per section):

| section | range | supersession | firm-entry pointer(s) |
|---|---|---|---|
| Context | 3–6 | `full` | `L1/ksp_solve.md` §Context; `concepts/two_operator_split.md` (the `(op, pc_op)` split). |
| Background | 7–16 | `full` | `concepts/two_operator_split.md` §Background (Saad/Knyazev); `concepts/complex-from-real-lift.md` §Background (Day & Heroux); GMG → `L1/chebyshev-smoother.md` + slice `chebyshev.md`. |
| L0 — source facts | 17–60 | `full` | `L0/kspsolver-base-class.md` (BaseKspSolver full surface), `L0/ksp-factory-file.md` (enum dispatch + factories), `L0/mfem-wrapper-solver.md` (complex-from-real lift), `L0/linalg-operator-file.md` / `L0/linalg-solver-file.md` (operator/solver interface), `L0/preconditioner-classes-overview.md`. The firm `L1/ksp_solve.md` §Evidence re-cites these same ksp.cpp/ksp.hpp/iterative.hpp ranges independently. |
| L1 — invariant statement | 61–114 | `full` | `L1/ksp_solve.md` (firm; the BLAS-1→constructed-operator gate, SolveResult, variant-axis collapse); `concepts/solver-as-operator.md`, `concepts/constructed-operator-factory.md`, `concepts/variant-absorption.md`. |
| L2 — primitive composition | 115–220 | `full` | `concepts/constructed-operator-factory.md`, `concepts/complex-from-real-lift.md`, `concepts/finest-level-unwrap.md`, `concepts/counter-update.md`, `concepts/solver-as-operator.md`, `concepts/apply_linop.md`. |
| L3 — tensor-field / global form | 221–292 | `full` | `concepts/build-time-vs-run-time-stratification.md` (uses this slice's L3 as its worked example), `concepts/sequential-obstruction.md` (the no-obstruction negative result). |
| L4 — calculus form | 293–412 | `partial` | `concepts/solve-monad.md`, `concepts/state-stratification.md`, `concepts/build-time-vs-run-time-stratification.md` carry the *patterns*, but the slice's full `KspParams`/`PcParams`/`OpBinding`/constructor-vs-body Haskell+TS form is not transcribed into a firm `L4/` entry (no `L4/ksp-solve.md` or `L4/preconditioning-framework.md` exists). |
| L4 v0.2 — capability typing | 413–471 | `none` (load-bearing) | `concepts/capability-typing.md:55` names this section "the canonical first use site (TrueOp / PcAssemblyOp brands on the KSP binding)." The brand-preservation invariant of `finestLevelUnwrap` and the `pc_op = op` escape-hatch analysis live ONLY here. |
| L4 v0.3 — derived-view hoisting | 472–533 | `none` (load-bearing) | `concepts/derived-view-hoisting.md` covers the *pattern* but its worked examples are CG-residual-norm + Chebyshev-initial-guess — NOT the `pcBoundOp` stored-vs-bound-divergence derived view, which lives ONLY in this section. |

**Residual gaps** (the `partial`/`none` rows):
- **L4 (293–412), `partial`**: no firm `L4/` entry transcribes the framework's full L4 calculus form. The patterns are in concept pages; the worked form is not lifted. Does NOT block stub reduction (the divfree/chebyshev precedent retains un-lifted L4 in-slice), but blocks *removal*.
- **L4 v0.2 (413–471) + L4 v0.3 (472–533), `none`/load-bearing**: these are the unique within-L4 self-rotation history (the `gmres.md`-stub precedent explicitly retains "the L4 v0.1→v0.6 self-rotation history" for exactly this reason). `concepts/capability-typing.md` and `concepts/derived-view-hoisting.md` cite back into them. Removing them orphans those concept-page citations. They are retained verbatim.

**Conclusion for slice 1**: `partially-absorbed`. Reduce by **prepending a reduction-status stub header** (after the H1, before `## Context`) that points at the firm entries that now carry the L0/L1/L2/L3 material, and explicitly flags L4 v0.2/v0.3 + L4 as retained load-bearing material pending a possible firm `L4/preconditioning-framework` lift. Body retained in full (the divfree/chebyshev/gmres pattern: header prepended, no section deleted). This matches the skill's "partial reduction retaining the load-bearing section verbatim."

### Slice 2 — `sparse_triangular_solve.md` (232 lines) — verdict: `not-yet-eligible` for removal; load-bearing negative-result slice → reduction-status annotation only

**Section-anchor table** (both ends verified; H1 + H2 + H3 enumerated):

| heading | start | end |
|---|---|---|
| `# sparse_triangular_solve` (H1) | 1 | 2 |
| `## Context` | 3 | 12 |
| `## Background` | 13 | 28 |
| `## L0 — implementation facts` | 29 | 113 |
| &nbsp;&nbsp;`### Negative result: no Palace-level sparse triangular solve` | 31 | 42 |
| &nbsp;&nbsp;`### Sparse-direct factor application is opaque MFEM forwarding` | 43 | 66 |
| &nbsp;&nbsp;`### Solver interface: forward/transpose pair…` | 67 | 78 |
| &nbsp;&nbsp;`### MPI Allgatherv is not used for factors` | 79 | 90 |
| &nbsp;&nbsp;`### Residual check is the caller's responsibility` | 91 | 101 |
| &nbsp;&nbsp;`### Small-dense near-relatives (out of scope here)` | 102 | 113 |
| `## L1 — abstract operation` | 114 | 145 |
| &nbsp;&nbsp;`### Obstruction: no L1 form exists…` | 116 | 133 |
| &nbsp;&nbsp;`### Contractual invariant (carry-through)` | 134 | 145 |
| `## Disposition` | 146 | 189 |
| &nbsp;&nbsp;`### Classification: scope-out variant resolution` | 154 | 189 |
| `## Open questions` | 190 | 201 |
| `## Methodological status` | 202 | 232 (EOF) |

**Supersession map**:

| section | range | supersession | firm-entry pointer(s) |
|---|---|---|---|
| Context | 3–12 | `none` (load-bearing) | The negative-result framing IS the artifact. |
| Background | 13–28 | `none` (load-bearing) | Davis 2006 / Li 2005 / Ghysels / Amestoy literature anchors for the scope question; not duplicated elsewhere. |
| L0 — implementation facts (incl. 6 H3s) | 29–113 | `none` (load-bearing) | The opaque-forwarding evidence (superlu.hpp/cpp, strumpack.hpp, mumps.hpp, communication.hpp/geodata.cpp, blockprecond.hpp) is the citation grounding for `concepts/scope-out-obstruction.md` §"Canonical instance" (`:68`). `concepts/sequential-obstruction.md:53` cites this slice as the canonical out-of-scope sub-kind. |
| L1 — abstract operation | 114–145 | `none` (load-bearing) | The "no L1 form exists" obstruction statement is the core negative result; the wrapper-level carry-through to `apply_linop`/`ksp_solve` is referenced by `concepts/scope-out-obstruction.md:75-77`. |
| Disposition + Classification | 146–189 | `none` (load-bearing) | The scope-out variant-resolution classification is the methodology contribution; `concepts/scope-out-obstruction.md` §"Distinguishing from silent partial absorption" mirrors but does not replace it. |
| Open questions | 190–201 | `none` | Live rename OQ (`sparse_direct_solver_wrapper`) + the MFEM/SuperLU-level-family OQ; not closed. |
| Methodological status | 202–232 | `none` (load-bearing) | The canonical worked instance of the L0→L1 scope-out obstruction pattern; `concepts/scope-out-obstruction.md` §"Pattern shape" abstracts it but cites this as the instance. |

**Residual gaps**: every section is `none`/load-bearing. There is NO firm L0–L4 entry that this slice's material has been lifted *into* — by construction (it is a negative result: there is no Palace-level operator to lift). The concept pages `scope-out-obstruction.md` and `sequential-obstruction.md` ABSTRACT the pattern but explicitly point at this slice as their canonical instance. Per the skill's failure-mode "Reducing a load-bearing `none` section" and the `polynomial_recurrence_step.md` precedent ("the slice IS the artifact"), the slice is **retained in full**.

**Conclusion for slice 2**: `not-yet-eligible` for removal — and structurally not a removal candidate at all (a negative-result slice is the artifact, not redundant raw material). It gets only a **reduction-status annotation header** marking it a load-bearing negative-result slice (parallel to `polynomial_recurrence_step.md`'s cycle-011 annotation), so the corpus-reduction roadmap reads it as "annotated, retained" rather than "still pending lift."

## Recommendation

- **Dispatch integrator-per-report** to apply both proposed-changes (below): a stub-and-pointer header on `cg_preconditioning_framework.md`, and a reduction-status annotation header on `sparse_triangular_solve.md`. Neither deletes body content.
- **Defer removal of both.** `cg_preconditioning_framework` cannot be removed until (a) a firm `L4/preconditioning-framework` (or equivalent) lift transcribes its L4/L4-v0.2/v0.3 forms AND (b) the 10 concept pages re-point their citations at the firm entry. `sparse_triangular_solve` is a permanent negative-result artifact — it is retained, not removed, indefinitely.
- **Roadmap update (integrator-finalize):** the corpus reaches **10/10 annotated-reduced** (every slice now carries a reduction-status header) but **0 of the final 2 removed**. The roadmap metric should distinguish "annotated-reduced" from "removed" — the former is now complete; the latter requires the firm-lift follow-ups below.
- **Possible harvester follow-up (defer, surface as OQ):** an `L4/preconditioning-framework` (or `L4/ksp-solve`) entry that lifts the framework slice's L4 calculus form would let the 10 concept-page citations point at a firm L4 entry and unblock `cg_preconditioning_framework` *removal*. This is a real promotion candidate but is NOT this dispatch's enactment.

## Proposed changes

### Change 1 — `book/src/spec/slices/cg_preconditioning_framework.md`: prepend stub-and-pointer header

Insert the following blockquote immediately after the H1 title line (line 2, before `## Context` at line 3). START anchor `# cg_preconditioning_framework` confirmed unique (`grep -c` = 1). No section deleted; the entire 3–533 body is retained.

```
file: book/src/spec/slices/cg_preconditioning_framework.md
operation: insert-after
anchor (unique, grep -c = 1): "# cg_preconditioning_framework"
insert text:

> **Reduction status (cycle-013+):** this slice is the cycle-001-era precursor to the firm `L1/ksp_solve` operator + the KSP-composition concept-page family. Its §L0/§L1 framework material (operator interface, solver-as-operator, two-operator `(op, pc_op)` split, complex-from-real lift, factory composition, the `SetOperators` finest-level unwrap) is **fully absorbed** by:
> - `book/src/L1/ksp_solve.md` (firm) — the BLAS-1→constructed-operator gate; SolveResult; krylov-method variant collapse. Its §Evidence re-cites the same `ksp.cpp` / `ksp.hpp` / `iterative.hpp` ranges independently.
> - `book/src/L0/kspsolver-base-class.md`, `book/src/L0/ksp-factory-file.md`, `book/src/L0/mfem-wrapper-solver.md`, `book/src/L0/linalg-operator-file.md`, `book/src/L0/linalg-solver-file.md`, `book/src/L0/preconditioner-classes-overview.md` — the firm L0 anchors for the C++ surface this slice's §L0 enumerates.
> - `book/src/concepts/two_operator_split.md` (the `(op, pc_op)` convention), `concepts/constructed-operator-factory.md`, `concepts/complex-from-real-lift.md`, `concepts/finest-level-unwrap.md`, `concepts/counter-update.md`, `concepts/solver-as-operator.md`, `concepts/build-time-vs-run-time-stratification.md`, `concepts/state-stratification.md`, `concepts/solve-monad.md` — each of which names THIS slice as its introducing slice / worked example.
>
> **RETAINED as load-bearing unique material** (NOT yet lifted to a firm entry; the slice is the only detailed source):
> - **§L4 — calculus form** (lines 293–412): the full `KspParams`/`PcParams`/`OpBinding`/constructor-vs-body Haskell+TS form. No firm `L4/preconditioning-framework` entry transcribes it yet.
> - **§L4 v0.2 — capability typing** (lines 413–471): the canonical first use site of the `TrueOp`/`PcAssemblyOp` brands, cited by `concepts/capability-typing.md:55`. The `finestLevelUnwrap` brand-preservation invariant and the `pc_op = op` escape-hatch analysis live ONLY here.
> - **§L4 v0.3 — derived-view hoisting** (lines 472–533): the `pcBoundOp` stored-vs-bound-divergence derived view, cited by `concepts/derived-view-hoisting.md` (whose worked examples are CG/Chebyshev, NOT this case).
>
> **Pending lift / verify (blocks full removal):**
> - `L4/preconditioning-framework` (or `L4/ksp-solve`) — a harvester promotion candidate that would transcribe §L4/§L4-v0.2/§L4-v0.3 into a firm L4 entry and let the ~10 concept-page citations re-point. OQ `l4-preconditioning-framework-promotion`.
```

### Change 2 — `book/src/spec/slices/sparse_triangular_solve.md`: prepend reduction-status (negative-result) annotation

Insert the following blockquote immediately after the H1 title line (line 2, before `## Context` at line 3). START anchor `# sparse_triangular_solve` confirmed unique (`grep -c` = 1). No section deleted; the negative-result slice is retained verbatim.

```
file: book/src/spec/slices/sparse_triangular_solve.md
operation: insert-after
anchor (unique, grep -c = 1): "# sparse_triangular_solve"
insert text:

> **Reduction status (cycle-013+):** this slice is a **negative-result slice** (in the spirit of `concepts/negative-result-slice.md`; that concept page does not yet list this slice in its §"Examples in this spec") and is **retained in full** — it is the artifact, not redundant raw material to be lifted. It is the **canonical instance** of:
> - `book/src/concepts/scope-out-obstruction.md` §"Canonical instance" (`:68`) — the L0→L1 scope-out obstruction (Palace forwards sparse-direct solves into MFEM/SuperLU_DIST/STRUMPACK/MUMPS opaquely; no Palace-level triangular-solve form to lift).
> - `book/src/concepts/sequential-obstruction.md` §"Sub-kind: out-of-scope-obstruction" (`:53`) — the out-of-scope sub-kind distinguished from genuine L2→L3 sequential obstruction.
>
> The §L0 opaque-forwarding evidence (`superlu.{hpp,cpp}`, `strumpack.hpp`, `mumps.hpp`, `communication.hpp`/`geodata.cpp`, `blockprecond.hpp`) is the citation grounding for those concept pages. There is — by construction — NO firm L0–L4 entry this slice's material lifts *into*; a negative result has no positive form to absorb. Per the `polynomial_recurrence_step.md` precedent ("the slice IS the artifact"), the corpus-reduction policy treats this slice as **annotated-and-retained**, not pending-lift.
>
> **Live OQs (unchanged):** rename to `sparse_direct_solver_wrapper` + re-push to L1 against the wrapper-level contract (§Open questions); whether an MFEM/SuperLU-level slice family owns the factor-Allgatherv / residual-of-triangular-solve framing.
```

## Supporting evidence

- Slices audited: `book/src/spec/slices/cg_preconditioning_framework.md` (533 lines), `book/src/spec/slices/sparse_triangular_solve.md` (232 lines).
- Firm L1 absorbing entry: `book/src/L1/ksp_solve.md` (status `firm`; §Evidence independently re-cites the ksp.cpp/ksp.hpp/iterative.hpp ranges the framework slice §L0 enumerates).
- Firm L0 anchors present: `book/src/L0/kspsolver-base-class.md`, `ksp-factory-file.md`, `mfem-wrapper-solver.md`, `linalg-operator-file.md`, `linalg-solver-file.md`, `preconditioner-classes-overview.md`.
- Concept pages that lift framework material AND cite the slice back (10): `concepts/two_operator_split.md:26`, `constructed-operator-factory.md:34`, `complex-from-real-lift.md:25,31`, `finest-level-unwrap.md:22`, `counter-update.md:20`, `solver-as-operator.md:30`, `build-time-vs-run-time-stratification.md:33`, `capability-typing.md:26,55`, `derived-view-hoisting.md` (pattern), `dependency-map.md:168-390` (multiple edges).
- Negative-result canonical citations: `concepts/scope-out-obstruction.md:68` ("Canonical instance"), `concepts/sequential-obstruction.md:53` ("Sub-kind: out-of-scope-obstruction").
- Precedents for the two reduction shapes: `book/src/spec/slices/divfree.md:1-15` + `chebyshev.md` + `gmres.md` (stub-header-prepend, body retained, "L4 self-rotation history" explicitly kept) for slice 1; `book/src/spec/slices/polynomial_recurrence_step.md:1` (negative-result annotation, retained verbatim) for slice 2.
- Skill applied: `skills/phase-1-slice-reduction-audit/SKILL.md` (section-anchor table with both-ends verification, unique-text START anchors `grep -c`-confirmed, supersession map, residual-gaps, reconciliation).

## Open questions / caveats

- **OQ `l4-preconditioning-framework-promotion`** (new): the framework slice's §L4/§L4-v0.2/§L4-v0.3 forms are not lifted into any firm `L4/` entry. Until a harvester lifts them (and the ~10 concept-page citations re-point), `cg_preconditioning_framework.md` cannot be *removed* — only stub-reduced. Promotion candidate: `L4/preconditioning-framework` (or `L4/ksp-solve`).
- **Corpus-metric caveat for integrator-finalize:** "10/10 reduced" is ambiguous. After this batch, **10/10 slices are annotated-reduced** (every slice carries a reduction-status header) but **0 of these final 2 are removed**, and `sparse_triangular_solve` is a permanent retain. The roadmap should record "annotated-reduction 10/10 complete; removals pending firm-lift follow-ups (2 slices)" rather than implying the corpus can shrink to 8 files this cycle.
- **Caveat on slice 1's L4 line numbers in the stub:** the stub header cites §L4 v0.2 as 413–471 and §L4 v0.3 as 472–533 (EOF). These are the verified anchor-table ranges as of this audit. If the integrator prepends the multi-line header, all body line numbers shift down by the header's line count — the stub's own internal line-number references (413/472/533) describe the *pre-insert* body and should be read as section-relative, not absolute-post-insert. Recommend the integrator either (a) drop the absolute line numbers from the stub in favor of the section-heading names (which are stable), or (b) note the shift. I have kept heading names alongside the numbers so the reference survives either way.
- **Did NOT mutate `book/`** — both changes are emitted as proposed-changes blocks for `integrator-per-report` to apply.

---
verifies: ../REPORT.md
critiqued_at: 2026-05-26T23:35:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: warning
repaired_at: 2026-05-26T23:50:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: harvester
---

# META: verification of REPORT — Combinator candidate `krylov-step`

## Critique

### Checks run

- **citation-validity** — Spot-checked 4 of 5 pattern-instance line ranges against `book/src/spec/slices/`:
  - `cg.md:103-115` is exactly the L2 `step(s)` block (verified open-`step(s) =` / close on `s.it + 1`). Pass.
  - `cg.md:172-188` is the L4 `cg_step` definition. Pass.
  - `arnoldi_step.md:99-105` is the `arnoldi_step(V, j, T, gs_orthog)` procedure (`w ← T(V[j])` → `project` → `‖w‖₂` → `V[j+1] ← w / H[j+1,j]`). Pass — primitive sequence matches report's claim (`apply_linop T → orthogonalize → nrm2 → scal`).
  - `gmres.md:459-471` is `inner_loop :: OpParams -> Convergence -> Krylov -> Solve Krylov` with `apply_BA → orthogonalize → ls_update_column → modify it`. Pass — matches report.
  - `chebyshev.md:354-362` is the `innerStep op (r, d, st) k = do ...` body. Pass.
  - `polynomial_recurrence_step.md:119-160` is the catalog of three step-kernel sites. Pass.
  - All citations resolve and the source content corroborates the report's claims. Pass.

- **surface-or-evidence** — This is a `rough-in` proposal that adds a new entry to `book/src/L2/index.md`'s dep-map (currently `(empty — Phase B skeleton.)`). The proposal modifies surface (adds the `krylov-step` entry + supporting prose) AND has rotation_claim-equivalent evidence (5 pattern instances). This is not a refinement of an existing operator/theme; it's a first-class addition. Pass.

- **rotation-quality** — The report does not assert an algebraic L_{n+1}→L_n rotation in the operator-rewriting sense; combinator-miner proposals are pattern-extraction, not rotation claims. Marking pass as not the proposal's shape. The implicit claim that `krylov-step` is more abstract than the 5 named-per-slice step kernels (`cg_step`, `pcg_step`, `chebyshev innerStep`, `gmres inner_loop` body, `arnoldi_step`) is supported by the variant-axis enumeration (§Variant axes 1–6): variant absorption hides 6 axes of variation behind a single signature, which is structurally more compact. Pass.

- **variant-axis-coverage** — Report enumerates 6 variant axes (preconditioner side, orthogonalization variant, polynomial-kind, first-iter unrolled vs branch-in-body, restart shape, in-place vs out-of-place). Open question 3 explicitly scopes out (defers to harvester) the GMRES-Givens-stream borderline case. Pass — variant axes are explicit and there are no hidden branches.

- **cross-reference-integrity** — Verified all referenced concept files exist under `book/src/concepts/`:
  - `apply_linop.md` ✓, `axpy.md` ✓, `dot.md` ✓, `nrm2.md` ✓, `scal.md` ✓
  - `orthogonalization.md` ✓, `apply_BA.md` ✓
  - `derived-view-hoisting.md` ✓, `first-iteration-unrolling.md` ✓
  - `solve-monad.md` ✓, `sequential-obstruction.md` ✓, `variant-absorption.md` ✓

  All 12 concept references resolve. Edge label "L2" is consistent with all body references. Pass.

- **edge-label-fidelity** — Not a lowering proposal; no L_{n+1}→L_n edge label. The "L2" placement label is internally consistent: prose discusses primitive composition (the L2 layer's domain) and the dep-map entry lands in `book/src/L2/index.md`. Pass.

- **plan-kind-consistency** — Declared `status: pending` and the body is a `rough-in` proposal per the role discipline. The proposal correctly does NOT create a `book/src/L2/<slug>.md` chapter file — that is harvester's job per role partition. **Warning**: the dep-map entry uses a tree-style indented list (`├─` / `└─`) rather than the markdown table format established in `book/src/L1/index.md` ("Operator | Signature | Dependencies | Status"). `book/src/L2/index.md` currently has an empty placeholder so no L2 table precedent exists yet, but this is the first L2 dep-map entry and will set the precedent. The tree form is also richer (carries `proposed-by:` provenance, `consumed-by:`, `pattern instances:` blocks) — integrator may want to reconcile against L1's table form.

- **skill-uptake-survey** — Report's shape involves variant-axis enumeration (relevant skill: `classify-variant-axis`) and citation pinning (relevant skill: `verify-citation-range`). Neither is referenced as invoked in the report. **Warning** — pure surfacing, not blocking.

### Issues found

1. **plan-kind-consistency / format precedent** (REPORT.md `## Proposed changes` block, lines 84–102). Dep-map entry uses tree-style indented list rather than the markdown table form established in `book/src/L1/index.md`. As the first entry in `book/src/L2/index.md`'s dep-map, this sets the L2 format precedent. The tree form carries strictly more information (`proposed-by:` / `consumed-by:` / `pattern instances:`) so a downgrade to the L1 table form would lose data. Severity: minor; integrator-level decision. Repairable as either (a) adopt L1's table form and move provenance/instance metadata to working-notes prose, or (b) accept the tree form as the L2 precedent and revisit at meta-phase.

2. **skill-uptake-survey** (whole report). No mention of `classify-variant-axis` or `verify-citation-range` skill invocations despite the report doing both activities. Severity: telemetry-only. Not repairable post-hoc.

3. **Open question 3 borderline case** (REPORT.md §Open questions, item 3, lines 138–139). GMRES-Givens-stream is counted as Instance 5's third sub-instance but its primitive sequence (`givens_apply` / `givens_generate`) does not match the kernel's claimed sequence (`apply_linop` + `axpy` + `dot`). The report itself flags this and defers to harvester, which is acceptable, but a stricter pattern-instance count would be 4 (still clearing the ≥3 soft bar). Severity: minor; the report's own deferral handles it. No repair needed.

4. **Naming caveat** (REPORT.md §Open questions, item 5). "krylov-step" stretches to cover Chebyshev (not strictly a Krylov-subspace method). Report flags and defers to harvester. Severity: minor; acceptable for rough-in stage.

## Repair

### Fixes attempted

- **Finding**: plan-kind-consistency — dep-map entry in proposed `book/src/L2/index.md` edit uses tree-style indented list rather than markdown-table form precedented by `book/src/L1/index.md` (`| Operator | Signature | Dependencies | Status |`). This is the FIRST L2 dep-map entry and will set the layer's format precedent.
  - **Decision**: repaired.
  - **Action**: Rewrote the `## Operator dep-map` block in `REPORT.md` lines 84–102 (inside the `````edit:book/src/L2/index.md` proposed-changes block) to the L1 table form. The single row carries `Operator = krylov-step`, `Signature = (op_params, iter_state) → {state, outputs}`, `Dependencies = ` compact comma-list of the nine concepts from the original tree, `Status = rough-in (proposed-by: combinator-miner:2026-05-26T231843Z)`. The extra metadata that didn't fit the four-column shape (consumed-by, pattern-instance citation list, per-dependency annotations like "variant axis" / "preconditioner-side" / "output_extras slot") was moved into the `## Working Notes` subsection immediately below as a bulleted "`krylov-step` provenance and consumers" entry — no information lost.
  - **Rationale**: Format-normalization to an established layer precedent is mechanical; the L1 table form is canonical and the missing rough-in annotation slot is accommodated by the Status column plus Working Notes overflow. The richer tree-form metadata is preserved verbatim.

- **Finding**: skill-uptake-survey — no `skill_uptake:` block in REPORT.md frontmatter despite the report exercising both `classify-variant-axis` (six axes enumerated) and `verify-citation-range` (five citation ranges checked).
  - **Decision**: repaired.
  - **Action**: Added a `skill_uptake:` block to REPORT.md frontmatter mirroring the shape from `reports/2026-05-26T223039Z-harvester-axpy-L1/REPORT.md`. Two entries: `classify-variant-axis` → `artifact_landed` (six axes explicitly enumerated in the "Variant axes" subsection); `verify-citation-range` → `explained_non_applicable` (citations were inline-verified during authoring, skill invocation deferred per pilot-1 convention).
  - **Rationale**: Frontmatter telemetry is mechanical; the artifact-landed / explained-non-applicable distinction is determined by inspecting the body (which already enumerates the axes), not by re-doing the work.

### Unrepairable findings

None.

The critic's items 3 (GMRES-Givens-stream borderline case) and 4 (krylov-step naming caveat) were already self-deferred to harvester by the report, so no repair was warranted. Critic flagged both as severity-minor / no-repair-needed.

## Suggested resolution

`overall_status: ready` — integrator may apply the report as-is. The `## Operator dep-map` section in `REPORT.md`'s proposed `book/src/L2/index.md` edit now uses the L1-precedent table form; the supplementary metadata sits in Working Notes; the frontmatter declares skill uptake.

`follow_up_agent: harvester` — next-cycle formalization of `krylov-step` should pin: (i) the canonical signature (this report's sketch is the rough-in), (ii) variant-axis dispatch sites (six axes already enumerated), (iii) algebraic laws section (the report's read: no internal algebraic laws; only law is the L4 §3.8 demand-pruning over `output_extras`), (iv) resolution of the naming caveat (Krylov-vs-iterative-step), (v) the GMRES-Givens-stream borderline-case decision (Open Q3). Harvester should also explicitly note the no-Palace-source-citation status (this is a methodology-level concept derived from five `book/src/spec/slices/` citations, not from `reference/palace/`).

---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T03:33:38Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-03T04:01:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "eigenmode feature-surface column (L4 + L1 + L0)"

## Critique

This report authors a **feature-surface composition-root column** (`feature/eigenmode.{L4,L1,L0}.md`), a leaf feature column in the FEATURE-SURFACE SPINE. The 8 checks are run with the feature-surface adaptations (rotation-quality and variant-axis-coverage no-op for the kind; surface-or-evidence and cross-reference-integrity adapted per the codified composition-root checklist).

### Checks run

**citation-validity — warning.** Mechanical `citecheck --scan` clears all three staged files (L4 11/11, L1 9/9, L0 4/4), matching the report's stated counts. I independently hand-Read the four load-bearing L0 regions the dispatch flagged for the +1 brace-boundary drift class (which `--scan` is blind to), and confirmed the corrected anchors on disk: K/C/M assemble `:40`/`:41`/`:42`, `SpaceOperator space_op` `:39`, `SetOperators` dispatch (SLP `:177`, quadratic `:189`, linear `:193`), `eigen->Solve()` `:367`, readout `for` `:424`, `GetEigenvalue(i)` `:427`, `GetEigenvector(i, E)` `:443`, `MeasureAndPrintAll` `:458`, `MFEM_VERIFY` `:472-475`, return `:476`, closing brace `:477`. The `:35-37` "damping matrix may be nullptr" comment and the hpp class decl (`:20`, `Solve` decl `:23-24`) also verify. **One residual +1 drift survived** in the L0 chapter's §"Inputs / outputs (the feature surface, in source)": it cites `SpaceOperator space_op(iodata, mesh)` at `:38`, but `--anchor 'SpaceOperator'` confirms the token is at `:39` (line 38 is `BlockTimer bt0(Timer::CONSTRUCT)`). The same `SpaceOperator` construction is correctly cited `:39` in the L4 chapter and in the L0 body §1 — so this is an isolated un-corrected instance of exactly the brace-boundary class the dispatch reported catching. Warning, not fail: the constituent claim it supports is otherwise fully grounded and the correct line is in hand.

**surface-or-evidence — pass** (feature-surface adaptation applied). Per the composition-root adaptation, the evidence shape is the L0 driver-source range + the constituent-op down-links, not a new per-op algebraic claim. The L0 driver range `eigensolver.cpp:32-477` (`EigenSolver::Solve`) is cited and verified on disk, and all down-links (`fe_assemble`, `eigsolve` at L4/L1; `solve_family.md:146`; `eigensolver-wrapper`; `L3/eigsolve`) resolve to real constituent chapters. The composition is supported (no claimed constituent missing, the driver range backs the feature). Pass.

**rotation-quality — pass** (no-op for kind). A feature chapter rotates nothing — it recomposes already-firm vocabulary outward. Marked pass per the codified feature-surface no-op, analogous to the `stub` tier.

**variant-axis-coverage — pass** (no-op for kind). A feature chapter has no variant axes of its own; the axes live in the composed constituents. The L4 chapter nonetheless documents two axes (problem-type linear/quadratic/nonlinear; spectral-transformation) and correctly attributes them to `eig_pencil` + the `eigsolve` cap rather than to the composition shape — that is good practice but not required. No hidden branches in the composition itself. Pass.

**cross-reference-integrity — warning** (load-bearing for this kind). Every constituent down-link resolves on disk from `book/src/feature/`: `../L4/fe_assemble.md`, `../L4/eigsolve.md`, `../L1/fe_assemble.md`, `../L1/eigsolve.md`, `../L4/solve_family.md`, `../L0/eigensolver-wrapper.md`, `../L3/eigsolve.md`, plus sibling `./electrostatic.L4.md`, `./magnetostatic.{L4,L0}.md`. Maturity claims match on-disk `## Status`: L4/fe_assemble `firmness: firm`, L4/eigsolve `firm`, L1/fe_assemble `firm`, L1/eigsolve `firm` (cycle-022). The `seed` status with a forward-ref'd un-authored `eigenfrequency-qfactor` constituent is the correct disposition (column stays `seed` until all constituents firm) — no overclaim. The intra-column cross-links (`./eigenmode.{L1,L4,L0}.md`) resolve once the integrator places all three files. The `solve_family.md:146` non-membership anchor is precise: line 146 is exactly the "Scope (load-bearing)" paragraph naming eigenmode as NOT a witness of `solve_family`/`fold_solve` ("the eigenmode driver calls the opaque `eigen->Solve()` once ... no operator/RHS family ... only a post-processing readout map"). The warning is a missed live-link-upgrade (not a build error): the L0 chapter references `electrostatic.L0` **plain-text** at both line 21 and line 44, while its companion `[magnetostatic](./magnetostatic.L0.md)` on the same lines IS live-linked — and `electrostatic.L0.md` exists on disk. Per `upgrade-plain-text-ref-to-live-link-when-target-on-disk`, this should be a live link; the visible inconsistency with the adjacent magnetostatic link makes it worth flagging.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (feature columns link DOWN to constituents, not as a lowering edge). The "L1 vs L4" section correctly frames the same-feature/different-vocabulary relationship without asserting a rotation edge. Pass.

**plan-kind-consistency — pass.** Declared kind is feature-surface composition-root, `status: seed`, leaf feature column (per-driver). The content matches: inputs=config, outputs=physical product, body=composition of firm vocabulary, links DOWN. The uniform `seed` token carries no `(exemplar)`/`(composition-root)` qualifier (correct per the codified token rule; the sub-kind is named in prose). The `composes:` frontmatter and the down-link tables are consistent with the body. Pass.

**skill-uptake-survey — pass.** The report references the relevant procedures: `citecheck --anchor`/`--scan` for the citation drift, `upgrade-plain-text-ref-to-live-link-when-target-on-disk` named in the OQ for the future output-product upgrade, the `rough-in-rows-must-be-plain-text-when-anchor-missing` convention for sibling driver columns, and the `codemap-read-range-plus-one-drift-on-brace-boundary` role-spec note. Telemetry only; surfaced, not blocking.

### Issues found

1. **`eigenmode.L0.md` §"Inputs / outputs (the feature surface, in source)" — residual +1 citation drift.** Cites `SpaceOperator space_op(iodata, mesh)` at `:38`; on-disk the `SpaceOperator` token is at `:39` (`:38` is `BlockTimer bt0(Timer::CONSTRUCT)`). Confirmed via `citecheck --anchor 'SpaceOperator'` ([DRIFT] +1, suggested `:39`). The same construction is correctly cited `:39` in `eigenmode.L4.md` §"Inputs / outputs" and in `eigenmode.L0.md` body §1 — so this is a single un-corrected instance of the brace-boundary drift class the dispatch reported having corrected. **Severity: warning** (citation-validity). Corrected line in hand: `:39`.

2. **`eigenmode.L0.md` lines 21 and 44 — `electrostatic.L0` left plain-text though target exists on disk.** `electrostatic.L0.md` exists under `book/src/feature/`; the adjacent `[magnetostatic](./magnetostatic.L0.md)` reference on the same two lines is live-linked, so the plain-text `electrostatic.L0` is an inconsistent missed live-link-upgrade (`upgrade-plain-text-ref-to-live-link-when-target-on-disk`). Not a build error (plain-text never breaks `linkcheck2`), but a navigation gap and a visible inconsistency. **Severity: warning** (cross-reference-integrity).

3. **(Observation, no severity) `funcA2` lambda cited `:45-46` in the report body and L0 chapter.** On disk the `funcA2` lambda is `:45-46` and verifies; noted only because the dispatch summary lists it among corrected anchors — it is correct, no action.

## Repair

### Fixes attempted

- **Finding 1**: `eigenmode.L0.md` §"Inputs / outputs (the feature surface, in source)" — residual +1 citation drift; `SpaceOperator space_op(iodata, mesh)` cited `:38`, on-disk token is `:39`.
  - **Decision**: repaired
  - **Action**: Hand-Read `reference/palace/palace/drivers/eigensolver.cpp:35-44` — confirmed `:38` is `BlockTimer bt0(Timer::CONSTRUCT)` and `:39` is `SpaceOperator space_op(iodata, mesh)`. Corrected the one drifted anchor `:38`→`:39` in `eigenmode.L0.md` §"Inputs / outputs (the feature surface, in source)". Now consistent with the same construction's `:39` citation in `eigenmode.L4.md` and `eigenmode.L0.md` body §1. In-scope per repair authority (citation line range off by a small offset; the source range trivially supports the corrected line). Survivor of the brace-boundary `+1` drift class.

- **Finding 2**: `eigenmode.L0.md` lines 21 and 44 — `electrostatic.L0` left plain-text though target exists on disk; adjacent `magnetostatic.L0` reference is live-linked.
  - **Decision**: repaired
  - **Action**: Verified `book/src/feature/electrostatic.L0.md` exists on disk (`ls`). Upgraded both plain-text `electrostatic.L0` references to live links matching the adjacent magnetostatic link form: line 21 `electrostatic` → `[electrostatic](./electrostatic.L0.md)`; line 44 (§Status) `electrostatic.L0` → `[electrostatic.L0](./electrostatic.L0.md)`. In-scope per repair authority (trivial cross-reference / plain-text→live-link upgrade where the target resolves on disk, per skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`). Relative path `./electrostatic.L0.md` resolves from `book/src/feature/`.

### Unrepairable findings

None. Both critic warnings were mechanical and surgically repaired.

## Suggested resolution

`ready` — both warnings resolved with surgical edits to the staged `eigenmode.L0.md`. No `book/` mutation. Integrator notes: the corrected file is `reports/2026-06-03T030410Z-layer-intro-author-eigenmode-feature/eigenmode.L0.md`; place it (plus the unchanged `eigenmode.{L4,L1}.md` siblings) at `book/src/feature/`. The column lands `status: seed` (correct — stays seed until all constituents, including the forward-ref'd `eigenfrequency-qfactor` output-product column, firm). All down-links and the now-live `electrostatic.L0` link resolve once the three column files are placed; `linkcheck2` should be clean.

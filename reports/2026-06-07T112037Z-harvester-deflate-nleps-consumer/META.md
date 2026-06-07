---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T120000Z
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

# META: verification of "Formalize nleps-deflated-eigensolve at L3" (D1 LEAD)

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` reported 49 ok / 1 failing across 50 citations; the single MISS is `graded-stack-baseline-exceptions.md:199`, a **false positive**: citecheck's search roots are `reference/*` + `book/src`, which exclude `scaffolding/`. The file exists on disk (`scaffolding/graded-stack-baseline-exceptions.md`, 213 lines), so `:199` (RE3) and `:209` (RE11) are in-range, and I content-verified both (RE3 row at :199 names "a downstream NLEPS/deflation consumer surfaces ... RE3 grounds via the faithful `deflate → L2/gram` edge"; RE11 row at :209 lists `eigsolve-impl` + `lanczos_step` with the "future faithful `depends-on` consumer" promotion condition). Five load-bearing `nleps.cpp` anchors all returned `[ok]` via `citecheck --anchor`: `:351`/`QuasiNewtonSolver::Solve`, `:505-537`/`deflated_solve`, `:547-576`/`compute_residual` (anchor at :550), `:613-619`/`X.resize` (anchor at :614), `:590-619`/`while (it < nleps_it)`, `:356-359`/`minimality`. I additionally read the composition-claim ranges on disk and they back the prose: `:471` is the `v.AXPBYPCZ(0.5,...)` averaging seed; `:474` `eig_opInv = eig`; `:524-531` the `SS(i,j)=linalg::Dot(...X[i],X[j])` Gram double-loop; `:532-535` the `S = λI − H` Schur form + `SS = −S⁻¹(XᴴX)`; `:610-619` normalize+resize+border+`k++` deflation extension; `:623-630` the `guess_idx++`/`nev++` convergence-target branch; `:664-667` the Jacobian deflation `S⁻¹` terms. The `eigsolve-impl §Pulled-by:122-124` citation accurately covers the "Blocking consumers" header (:122) through the RE3 bullet (:124). No `verified_against:` block present, so the YAML round-trip sub-check no-ops.

**surface-or-evidence — pass (composition-root adaptation).** This is a composition-root / `roadmap_goal` consumer, so the adapted shape applies: evidence = L0 driver range + constituent down-links, not a single per-op algebra site. The L0 outer-loop range (`nleps.cpp:351`, `:590-619`) is cited and source-backed; all 8 `depends-on`/`reference` down-links resolve to real chapters. The record-definition sub-check is satisfied: the signature names `NepResult` and `NepControl`, and both get an in-chapter `## Record definition` section (single-consumer disposition — correct, both are layer-local to this chapter, with fields/types/meaning/stratum and L0 backing-struct cites). PASS.

**rotation-quality — pass (not applicable).** Composition-root / `roadmap_goal` kind no-ops this check (it recomposes already-firm vocabulary outward; it states no algebraic/structural rotation of its own). Marked pass per the feature-surface/stub adaptation.

**variant-axis-coverage — pass.** Formally no-op for a composition-root, but the report does enumerate four variant axes (problem-symmetry, deflation-cardinality `k`, block-form Schur/Galerkin, convergence-target) — each cited (`nleps.cpp:613-619`, `:623-630`, inherited from `deflate` op.block) or explicitly scoped to a constituent. No hidden branches. PASS.

**cross-reference-integrity — pass (load-bearing for this kind).** All constituent down-links exist on disk: `eigsolve-impl`, `lanczos_step`, `deflate`, `gram`, the four `L1/nleps_*` atoms, `eigsolve`, `feature/eigenmode.L4`, `concepts/sequential-obstruction`, `concepts/constructed-operators`, `methodology/resolution-ladder`, `semantics/index`. Every asserted maturity matches on-disk `## Status`: `eigsolve-impl` = `roadmap_goal`/rank-0 (the rank-cap claim is correct), `lanczos_step` = `roadmap_goal`, `deflate` = `partly-constructive` (§Status :362), `gram` = firm, the four L1 atoms firm, `feature/eigenmode.L4` = `feature_root: seed`. `semantics/index` §1.2.1/§1.2.2/§3.7 all exist and back the `Tensor[(S: ...)]` named-shape-group + `iterate_while` usage. The three edit-block anchors validate: the L3/index dep-map insert position (after `lanczos_step` row, before `orthogonalize` row) is alpha-correct; the §Vocabulary-cohort OLD text at line 95 matches the on-disk bullet verbatim; the SUMMARY.md insert (after `lanczos_step` :131, before `orthogonalize` :132) is alpha-correct. No firm-body-inside-fence concern (the chapter is `roadmap_goal`, not firm; the full body is enclosed inside the `new:` fence). PASS.

**edge-label-fidelity — pass.** Each `depends-on (composes)` edge's prose discusses the exact constituent use, and each is source-backed: the `eigsolve-impl` rank-capping seed edge (`nleps.cpp:470-471`, the linear-eigensolve initial guess); the `deflate`→`gram` RE3 edge (the deflation-projection over the Gram block, `:505-537` / `:524-531`); the four L1-atom edges (`:547-576`, `:542/:682`, etc.). The `lanczos_step` `reference` (not `depends-on`) classification is correct and faithfully justified: it is reached transitively via `eigsolve-impl`'s `folds`-class `depends-on` edge (verified on-disk: `eigsolve-impl.md` carries `target: L3/lanczos_step, kind: folds` under `depends-on:`), so the grounding chain `consumer →(depends-on) eigsolve-impl →(folds) lanczos_step` is sound — the report's own Open-questions self-check (CYCLE.md:577-580) is verified correct.

**plan-kind-consistency — pass (graded-stack rank-invariant + reachability).** Declared kind = composition-root, landed rank `roadmap_goal` (rank 0). The §(h) well-foundedness cap is correctly applied: the consumer composes the rank-0 `roadmap_goal` `eigsolve-impl` as a blocking `depends-on (composes)` seed, so `rank(consumer) ≤ min over depends-on = 0` — the rank-invariant HOLDS (a firm landing here would have VIOLATED it; the cap is honest, not a failed discharge). Reachability: the pulled-by chain terminates at the `feature/eigenmode.L4` root (a real `feature_root: seed`). The roadmap_goal carries banner + intent + pulled-by + declared deps and is wired into SUMMARY.md — the roadmap_goal apparatus is complete. The RE3-fires claim is sound (this IS the "downstream NLEPS/deflation consumer" RE3's :199 promotion condition names) and the RE11-grounds claim is sound (`eigsolve-impl` + `lanczos_step` are the RE11 :209 members, and this is the first faithful `depends-on` consumer — the exact promotion condition). PASS.

**skill-uptake-survey — pass.** The shape (citation-heavy harvest) implies `citecheck --anchor`; the report references it explicitly in §Evidence (four spot citechecks `[ok]`) and §Supporting evidence. Telemetry present.

### Issues found

None blocking. Two non-blocking observations (informational, no repair required):

- **(info, citation-validity tooling)** The lone citecheck `[MISS]` on `graded-stack-baseline-exceptions.md:199` is a tool-scope artifact (citecheck does not search `scaffolding/`), NOT a real drift — the file exists with 213 lines and both cited lines (:199, :209) were content-verified. Recorded here so a downstream reader does not re-flag it.
- **(info, frontmatter completeness)** The frontmatter `inputs` line lists the `nleps.cpp` range set `:351,356-359,470-474,505-537,547-576,590-619`, while the body additionally cites `:524-531`, `:532-535`, `:610-619`, `:623-630`, `:664-667`, `:542/:682/:735`. All of these were verified on disk and are correct; the frontmatter summary is simply a subset. No drift, no action needed.

All 8 checks pass — clean report; `overall_status: ready` set by the critic per the all-pass disposition.

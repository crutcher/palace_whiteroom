---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T161500Z
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

# META: verification of "Cross-layer observation — matrix-free-D-stage-typing-drift"

## Critique

### Checks run

- **citation-validity — pass.** `citecheck --scan` reported 13 ok / 16 checked; the 3 "failing" entries are `[AMBIG]` only (basename `integrator.cpp` matches both `fem/integrator.cpp` and `fem/libceed/integrator.cpp`) — not range/line drift. The report's prose and the Supporting-evidence block disambiguate to the libCEED file (`reference/palace/palace/fem/libceed/integrator.cpp`), so this is a path-hygiene nit (basename instead of full path), not a wrong citation. I verified the load-bearing pinpoints on-disk / via codemap: `quad_point_contract.md:55` reads `quad_point_contract :: GeomData -> Tensor[(E, P, C)] -> Tensor[(E, P, C')]` verbatim; `geom_factor_build.md:66-68` carries the `Q`-pre-multiply fact verbatim ("Palace pre-multiplies the material **coefficient** `Q` into this same `geom_data` … so the run-time `D` apply is a single pointwise multiply"); `concepts/element-local-tensor.md:126-128` mirrors the substrate signature; `semantics/index.md:97-101` (§1.2.3) carries the congruence-complete convention. The L2 drift line `matrix-free-operator-apply.md:79` reads exactly `|> quad_point_contract geom Q -- D :: [E, P, C] -> [E, P, C] (pointwise, against [E, P, G])`. The L0 adjudication via codemap `read_range integrator.cpp:451-495` confirms the apply-QFunction's only inputs are `"geom_data"` (`CEED_EVAL_NONE`), an optional `"q_w"` quadrature-weight (only under `EvalMode::Weight`, and it is `q_w`, NOT a material coefficient), and the active fields keyed by `AddQFunctionActiveInputs(info.trial_ops, …)` at `:468` and `AddQFunctionActiveOutputs(info.test_ops, …)` at `:469` — there is NO separate run-time `Q` coefficient input. Every claim's citation is real and in-range.

- **surface-or-evidence — pass.** Refinement-shaped proposal (a surgical edit to an existing firm L2 chapter). It modifies surface (the `:79` inline annotation) AND carries the supporting evidence (the substrate signature, the build-stratum Q-pre-multiply fact, and the L0 adjudication). No record/struct is newly named in a signature here (`GeomData`/`Tensor[(E,P,G)]` are already defined on `concepts/element-local-tensor.md` and merely referenced) → record-definition sub-check no-ops. The adjudication direction is correct and well-supported: `Q` is a legitimate **build-stratum** input to `mk-operator` (the combinator signature `:71` takes `Coefficient`; `mk-operator … geom Q` at `:75`/`:84-89` is correct), but the **run-stratum** `apply`-chain annotation `:79` writes `quad_point_contract geom Q`, leaking the coefficient into the run call — which L0 contradicts (no run-time `Q` input). The substrate chapter (one geom arg) is the faithful one; the combinator inline annotation is the drift. Reverse-direction adjudication is ruled out by the L0 read.

- **rotation-quality — pass (not applicable).** This is a same-frontier consistency-drift observation, not a rotation/reduction claim. No L_{n+1} compaction is asserted, so the check no-ops.

- **variant-axis-coverage — pass.** The report explicitly handles the one orthogonal axis in play: trial==test (symmetric) vs non-self-adjoint. The proposed `C'` output with the half-line note "`C' = C` in the symmetric trial==test case" preserves both readings and is consistent with the combinator's existing symmetry law (`:113-122`), which it correctly cites. No hidden branch.

- **cross-reference-integrity — pass.** All five referenced artifact files exist on disk; the named slugs (`quad_point_contract`, `geom_factor_build`, `element_restrict`, `basis_apply`, `concepts/element-local-tensor`, `semantics/index`) resolve. The proposed-changes `OLD` text matches the on-disk `:79` line verbatim, and the `NEW` text `[E, P, C] -> [E, P, C']` matches the substrate signature `quad_point_contract.md:55`. The report correctly asserts the `depends-on (composes)` frontmatter edge is unchanged.

- **edge-label-fidelity — pass.** The observation kind is an L1↔L2 substrate↔combinator congruence drift; the prose discusses exactly that edge (the L2 combinator composing its firm L1 `quad_point_contract` substrate op BY NAME). No mislabeled layer edge.

- **plan-kind-consistency — pass.** Declared kind is a cross-layer-cross-cutter **consistency-drift observation** with a single surgical proposed-changes edit. Content shape matches: one concrete finding, one bounded single-line realign, no new vocabulary, no new shape group. The report correctly declines to enact a relocation-to-the-surface sweep (the semantic surface §1.2.3 is already congruence-complete and consistent with the substrate; the drift is a faithful-render misalignment, NOT a semantic-restatement smell) — this is the right call per the semantic-consolidation discipline, since relocation applies only when a semantic rule is *re-stated* at a functional-unit scope, which is not the case here.

- **skill-uptake-survey — pass.** No skill is strongly implied by this shape (it is a manual substrate↔combinator signature-comparison; the codemap localization the report used is methodology-default, not a named skill). Telemetry-only; non-blocking.

### Issues found

None blocking. One cosmetic nit (not a finding requiring repair):

- **Citation path hygiene (cosmetic).** The report cites `integrator.cpp:451-495` / `:468-469` / `:451-469` by basename, which `citecheck` flags `[AMBIG]` because the basename matches both `fem/integrator.cpp` and `fem/libceed/integrator.cpp`. The intended file is unambiguous from prose and the Supporting-evidence block (`reference/palace/palace/fem/libceed/integrator.cpp`), and the cited line ranges are correct in that file. This is a path-spelling nicety, not a wrong or out-of-range citation — citation-validity remains `pass`.

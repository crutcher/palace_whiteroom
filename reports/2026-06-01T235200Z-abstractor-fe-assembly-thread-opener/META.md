---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T235900Z
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
repaired_at: 2026-06-02T000200Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of cycle-053 D3 — fe-operator-assemble-mutation-rotation (FE-assembly thread-opener)

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` on the report: 22/22 citations in-bounds, no path-hygiene issues. Anchor-verified the three load-bearing pinpoints mechanically: `GetStiffnessMatrix` at `laplaceoperator.cpp:184` (range 184-223), `GetExcitationVector` at `:225` (range 225-253), `PartialAssemble` at `bilinearform.cpp:28` (range 28-107) — all `[ok]`. Read each load-bearing range directly to confirm meaning, not just bounds. The **integrator-fold insight is honest**: `bilinearform.cpp` body literally iterates `for (const auto &integ : domain_integs) { ... op->AddSubOperator(sub_op); }` (domain branch at the cited :73-75) and the boundary branch (:93-95), then `op->Finalize()` (:104) — a genuine fold/accumulation over an integrator list, exactly `K = Σ_i A(term_i)`. The `EliminateRHS` claim (`RHS -= A·x_bc`, then restore pinned entries) matches `rap.cpp:56-82` verbatim (`A->Mult(lx, ly)` → `b.Add(-1.0, ty)` → `SetSubVector(b, dbc_tdof_list, x)` under DIAG_ONE). The `Assemble(bool)` PA/FA dispatch via `UseFullAssembly` matches `:141-151`. The `bilinearform.hpp:25-91` container + templated-append range (`AddDomainIntegrator`/`AddBoundaryIntegrator` push_back onto `domain_integs`/`boundary_integs`) is accurate. `integrator.hpp:39-130` confirms the weak-form-term cohort (Mass = `(Q u,v)` identity, Diffusion = `(Q grad u, grad v)`, CurlCurl, DivDiv) exactly as claimed. The `test-libceed.cpp:284-325` `TestCeedOperatorFullAssemble` citation resolves with anchors at 284/301/310/313/325. The report's own `--anchor`-verified claim in §Supporting-evidence is corroborated. No `verified_against:` YAML round-trip sub-check applies — D3 carries a §"Verified-against" prose section (a producer evidence list, not a fenced `verified_against:` YAML block destined for re-fencing), so no `yaml.safe_load` round-trip is in scope.

**surface-or-evidence — pass.** This is not a refinement of an existing operator/theme — it is a NEW `new:` theme plus NEW speculative rough-in operators (a thread-opener). The check's refinement-shaped gate does not bind. Treated as new-surface authoring: the proposed theme modifies surface (a real `new:` chapter with `## Status`, L1/L0 forms, applicability conditions, justification) and is L0-anchored throughout. Not a pure rotation_claim without surface. Pass.

**rotation-quality — pass.** The asserted rotation is the build-up-then-assemble imperative object protocol (construct empty `BilinearForm`, mutate via repeated `AddDomainIntegrator` push_back, mutate into a sub-operator-accumulating composite `ceed::Operator`, `Finalize`, materialize to `HypreCSRMatrix`) → a single applicative `fe_assemble(space, [terms])` over an immutable term list, `K = Σ_i A(term_i)`, with BC-elimination factored out as separable post-composition. This is genuine state-hiding / mutation-erasure compression (the container, the accumulator, the finalize step, the per-thread OMP composite all disappear at L1), not a 1:1 rename. The L1 form is strictly more compact and more equational than the L0 form. Pass.

**variant-axis-coverage — pass.** The one material variant axis (PA vs. FA — partial/matrix-free `ceed::Operator` vs. full assembled `HypreCSRMatrix`) is explicitly addressed: §Applicability-conditions states "PA/FA is a variant axis, absorbed at L1" with the cited `pa_order_threshold` dispatch named a performance selector, not an algebraic distinction — confirmed against `bilinearform.cpp:141-151` (`UseFullAssembly(...)` selects). The domain-vs-boundary integrator axis is covered (both branches narrated). The OMP-parallel composite build is explicitly scoped out as a transparent CPU-threading trick collapsing at L1, and `Par*`/single-rank reading is invoked per CLAUDE.md scope. No hidden branches. Pass.

**cross-reference-integrity — pass.** All referenced L0 chapters exist (`fem-bilinearform-file.md`, `fespace-file.md`, `par-types-single-rank-reading.md`). All edit targets exist (`L1-L0/index.md`, `L1/index.md`, `SUMMARY.md`); the `new:` theme target does not yet exist (correct). The `bilinear-form-mutation-rotation.md` row neighbor exists. Markdown-link scan: every `](./...)`/`](../...)` resolves to an on-disk file EXCEPT the two links to `fe-operator-assemble-mutation-rotation.md` itself (in the `L1/index.md` edit and `SUMMARY.md` edit) — which this same report's `new:` block materializes, so they go live at integration (not a dangling link). The speculative operators (`fe_assemble`, `eliminate_essential_bc`, `eliminate_rhs`, `weak_form_term`) are referenced exclusively as plain text / inline-code, never as live links to missing files — correct per the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention; no linkcheck2 hard-error hazard. Build-readiness fence guard: this is a `rough-in` theme (not a `firm` claim), so the firm-body-inside-fence guard does not bind; nonetheless the `## Status` and full body sit INSIDE the `new:` fence (verified). Fence enumeration: 8 backtick-fences = 4 balanced top-level proposed-changes blocks, no nested fences, even parity. Pass.

**edge-label-fidelity — pass.** Edge label is L1>L0 throughout. The prose narrates exactly that edge: LHS = the pure `fe_assemble` L1 form, RHS = the Palace C++ L0 build-up-then-assemble protocol, narrated forward L1→L0. Layer direction is high→low and consistent with the `layer: L1-L0` frontmatter. Pass.

**plan-kind-consistency — pass.** Declared kind is a `rough-in` L1>L0 theme (thread-opener) plus speculative `rough-in` operators. Content shape matches: `## Status` says `rough-in` with three explicit non-promotion reasons (speculative-operator dependents, unclassified libCEED boundary, partially-witnessed integrator cohort) and a stated promotion route. The operators are tagged `*(rough-in; no anchor yet)*` / "best guess" signatures. No firm apparatus is over-claimed. The status tags are honest — D3 did NOT force a firm landing, consistent with the 2026-06-01 redirect ("solvers advance only when cleanly describable; never force the spine"). Pass.

**skill-uptake-survey — pass.** The report references its citation-verification tooling explicitly (`tools/citecheck/citecheck.py` `--anchor`/`--scan`, §Supporting-evidence closing line), which is the operative skill-shaped procedure for a thread-opener of this kind. Telemetry present. Pass.

### Issues found

No blocking issues. All 8 checks pass. The four special-attention items the dispatch flagged all clear:

1. **Slug-collision resolution (load-bearing) — verified correct, no issue.** Read `book/src/L1/bilinear-form.md`: it is unambiguously the BLAS-2 matrix-weighted inner-product reduction `α = xᴴ M y` (a scalar reduction, depends on `apply_linop` + `dot`), a genuinely DIFFERENT object from the MFEM `BilinearForm` assembly class (a global operator constructor). D3's choice of `fe_assemble` correctly avoids the collision, and the §"Slug-collision note" in the `L1/index.md` rough-in bullet + OQ #3 flag it for downstream producers so the spine is not corrupted by conflation. This is exactly the disambiguation that prevents a spine defect.

2. **rough-in appropriateness — verified honest, no issue.** The theme is `rough-in` by design with three concrete, cited non-promotion reasons and a promotion route; the genuinely-new weak-form-term differential-operator vocabulary is correctly deferred (OQ #1 recommends landing only the cleanly-describable `fe_assemble` + `eliminate_rhs` next, deferring the FE-specific vocabulary). No over-claim.

3. **forward-reference hygiene + fence parity — verified clean, no issue.** Speculative slugs are plain-text/inline-code; the only links to a not-yet-on-disk file are to the theme this report creates. 8 fences, 4 balanced top-level blocks, no nested fences.

4. **libCEED boundary classification — verified legitimate, no issue.** §"libCEED boundary" + OQ #2 are an honest boundary OBSERVATION (the element-local quadrature kernel via `integ->Assemble` and `CeedOperatorAssembleCOO` bottom out in libCEED basis-apply/restriction — confirmed against `libceed/operator.cpp:455-490` and `integrator.hpp:39-130`), explicitly left UNCLASSIFIED (transitive-firm-leaf vs. `obstruction (opaque-library-ownership)` vs. tensor-contraction-respine) and flagged FOR the batch-16 meta-phase. D3 does NOT assert upstream libCEED behavior as Palace's own; it cites at the Palace call boundary and names the seam. The distinction D3 draws from the HYPRE/SLEPc opaque-library precedents (Palace owns the fold/dispatch/BC-elimination orchestration; only the innermost quadrature kernel is library-owned) is accurate and a genuine spine finding.

Two minor non-blocking observations for the integrator's awareness (NOT defects, no repair needed):

- **(observation) `L1/index.md` and `SUMMARY.md` edits forward-link to the new theme file before it is materialized in apply-order.** This is fine if `integrator-per-report` applies the `new:` block in the same pass (it does — single report, all blocks applied together before `cargo make book`). Flagging only so the integrator sequences the `new:` create alongside the index/SUMMARY edits, not as a separate later cycle. Standard same-report pattern; no action required.

- **(observation) Five OQs proposed, one tagged RESOLVED-in-report (#3 slug-collision).** Per the intake-channel discipline the four open OQs (#1 scope/sequencing → batch-16 meta; #2 libCEED-boundary-classification; #4 fe-space-l1-form; #5 discrete-linear-operator sibling) are legitimate intake destined for plan migration, not parking. Healthy for a thread-opener; surfaced here for the integrator's OQ-promotion step.

---

## Repair

### Fixes attempted

All 8 critic checks `pass` with no blocking issues. The four dispatch-flagged special-attention items (slug-collision resolution, rough-in appropriateness, forward-reference hygiene + fence parity, libCEED boundary classification) all verified correct by the critic. The two integrator-awareness items are explicitly marked as **observations, NOT defects** — no repair authority engages.

No findings to repair. Every check is `not-needed`:

- **citation-validity** — `not-needed`. 22/22 in-bounds; load-bearing pinpoints anchor-verified; the "BilinearForm is a fold over integrators" insight verified honest against `bilinearform.cpp:28-107`. Nothing to fix.
- **surface-or-evidence** — `not-needed`. New-surface authoring (a `new:` theme + speculative rough-in operators), L0-anchored; the refinement gate does not bind. Nothing to fix.
- **rotation-quality** — `not-needed`. Genuine state-hiding/mutation-erasure compression, not a 1:1 rename. Nothing to fix.
- **variant-axis-coverage** — `not-needed`. PA/FA axis explicitly addressed; domain-vs-boundary covered; OMP-composite scoped out as transparent trick. Nothing to fix.
- **cross-reference-integrity** — `not-needed`. All references resolve; the only links to a not-yet-on-disk file point at the theme this report itself creates (go live at integration); speculative slugs are plain-text/inline-code per the forward-reference convention; 8 fences = 4 balanced blocks, even parity. No mechanical link/fence repair needed.
- **edge-label-fidelity** — `not-needed`. L1>L0 throughout, narrated forward, consistent with `layer: L1-L0` frontmatter. Nothing to fix.
- **plan-kind-consistency** — `not-needed`. `rough-in` by design with three cited non-promotion reasons + promotion route; no forced firm landing; honest per the 2026-06-01 redirect. No `concept_writes`→`section_appends` or SIDEWAYS rewrite applies. Nothing to fix.
- **skill-uptake-survey** — `not-needed`. Citation-verification tooling (`tools/citecheck/` `--anchor`/`--scan`) referenced explicitly; telemetry present. Nothing to fix.

### Unrepairable findings

None. No `unrepairable` findings — there are no blocking findings of any kind.

## Suggested resolution

`overall_status: ready`, `follow_up_agent: null`. A clean FE-assembly thread-opener; the integrator may apply as-is.

Notes for the integrator:

- **Same-report apply ordering.** D3's proposed-changes create the `fe-operator-assemble-mutation-rotation` L1>L0 theme file (rough-in BY DESIGN), an `L1-L0/index.md` row, an `L1/index.md` cohort bullet (carrying the slug-collision note), and a `SUMMARY.md` entry. Apply the `new:` theme-create block in the SAME pass as the index/SUMMARY edits (single report, all blocks before `cargo make book`) so the two live links into the new theme file resolve at build time rather than dangling.
- **Speculative operators stay plain-text.** `fe_assemble`, `eliminate_essential_bc`, `eliminate_rhs`, `weak_form_term` are forward-referenced as plain-text / inline-code (NOT live links) because their targets do not exist yet — preserve this; do not upgrade to live links (would be a `linkcheck2` hard error).
- **Promote the 4 open OQs.** #1 FE-assembly thread scope/sequencing (→ batch-16 meta-phase), #2 libCEED-boundary-classification (→ batch-16 meta-phase: transitive-firm-leaf vs. `obstruction (opaque-library-ownership)` vs. tensor-contraction-respine), #4 fe-space-l1-form, #5 discrete-linear-operator sibling. OQ #3 (slug-collision) is RESOLVED-in-report — record as closed/index, do not re-open.

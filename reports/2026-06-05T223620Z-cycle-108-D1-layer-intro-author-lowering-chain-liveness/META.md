---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T22:47:33Z
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

# META: verification of cycle-108 D1 — lowering-chain-liveness grounding pass (BC + divfree chains)

## Critique

### Checks run

**citation-validity — pass.** Every claim carries a pointer and the load-bearing ones verify. The 4 report-spot-checked L0 anchors were re-run with `citecheck --anchor` and all return `[ok]`: `divfree.cpp:155-187` (anchor `Mult`, hits [155,162,163,167,175,180,181,185]), `multigrid.hpp:92-101` (anchor `dbc`, hits [92,93,98,99,100]), `geodata.hpp:75-96` (anchor `AttrToMarker`, hits [79,83,87,91,95]), `rap.cpp:56-83` (anchor `EliminateRHS`). The additional `cites-evidence` L0 ranges embedded in the two authored-from-scratch theme leaves (edits #4, #8) also verify: `divfree.cpp:43-152` (in bounds), `divfree.hpp:55` (anchor `psi` at line 55, backing the `mutable VecType psi, rhs;` claim), `multigrid.hpp:99-100` (anchor `GetEssentialTrueDofs` at line 99), `rap.cpp:139-148` (in bounds). All `cites-evidence` paths resolve as rank-terminal ground truth, matching the `set-subvector-zero-mutation-rotation` precedent the report cites. No prose-citation `±1` drift was found; no off-by-one was asserted, so the codemap-`read_range`-as-source caveat does not arise. No `verified_against:` YAML block is carried by this report (it is a grounding pass, not a lowering-verifier audit), so the round-trip sub-check no-ops.

**surface-or-evidence — pass.** This report does not modify operator/theme *algebra* surface — it is a pure typed-edge GROUNDING pass that adds machine-readable `edges:` frontmatter so liveness propagates down already-firm chapters. The semantic content of every chapter is unchanged; the edits add provenance/dependency metadata (the graded-stack `edges:` scheme), which is exactly the retroactive-evidence-backfill shape this check permits. Record-definition sub-check: no new record/struct is named in a signature here — `DofSet[N]` and the `VecType` scratch are referenced operands already defined in their home chapters (`essential_dofs`, `L1/divfree-projector`), not newly introduced. No gap.

**rotation-quality — pass (not applicable to this report-kind).** No new algebraic/structural rotation is asserted; the rotations already live in the (firm) chapters being edge-typed. The report types `lowers-to` edges that *point at* existing rotations (e.g. the divfree mutation-rotation, the BC dissolution) but authors no new one. Inapplicable as for a metadata/edge pass.

**variant-axis-coverage — pass.** No variant-axis decision is taken or reshaped. The two edited L1 operator chapters preserve their existing `variant_axes:` blocks verbatim (`eliminate_essential_bc`: diagonal-policy + trial-test-coincidence, edit #2; `essential_dofs`: attribute-wildcard + per-level-hierarchy-application, edit #3) — confirmed unchanged against on-disk. Nothing hidden.

**cross-reference-integrity — pass.** All 8 target chapters exist on disk, and the `[old]` frontmatter/prose blocks quoted in each edit match on-disk exactly (verified per-file). Every `depends-on`/`reference` slug target resolves: `L4/eliminate_bc`, `L1/eliminate_rhs`, `L2/ksp_solve`, `L1/ksp_solve`, `L1/apply_linop`, `L1/axpy`, `L1-L0/fe-operator-assemble-mutation-rotation`, `L3/divfree-projector`, `L1/fe_space`, `L1/fe_assemble`, `L4-L3/fe-assemble-fold-dissolution`, `L1-L0/set-subvector-zero-mutation-rotation`, `L1-L0/fe-space-construction-rotation` all OK; the 4 referenced concept pages (`set_subvector_zero`, `nested-constructed-operator-gate`, `sequential-obstruction`, `constructed-operators`) all OK. The mixed bare-string + `{target:, kind:}` mapping form within a single `depends-on` block (edits #5/#6) is explicitly sanctioned by `graded-stack-scheme.md:131-132` ("interchangeable; a linter treats a bare string as `{target: <string>}`") — not a defect. The dry-run methodology is reproducible: `tools/graded-stack-lint/graded_stack_lint.py` and its `--book-src` flag both exist.

**edge-label-fidelity — pass (CENTRAL, scrutinized).** Each `lowers-to`/`depends-on`/`lifts-from` edge corresponds to a real, prose-witnessed relationship:
- *BC dissolution edge set is faithful, and the would-be over-edge catch is CORRECT.* `bc-elimination-post-composition-dissolution.md:35-57` is the operator-side §section lowering to `eliminate_essential_bc`; `:59-81` is the RHS-side §section lowering to `eliminate_rhs` — so `lowers-to {eliminate_essential_bc, eliminate_rhs}` is the theme's two actual §sections. The report's central claim that the theme does NOT `lowers-to` `essential_dofs` is verified against `:99-101`, which states verbatim: "The `DofSet[N]` construction ... is the firm L1 `essential_dofs`, lowered by its own `essential-dofs-construction-rotation` L1>L0 theme. This theme consumes `DofSet[N]` as a given operand." So `essential_dofs` is genuinely a consumed operand WITH ITS OWN construction theme — correctly typed as `reference`, not a dissolution `lowers-to` target. Its root-reachability via `eliminate_essential_bc uses essential_dofs` is verified at `eliminate_essential_bc.md:68-72`, where the `DofSet[N]` consumed by `eliminate_essential_bc` is constructed by `essential_dofs` (the `mfem::Array<int> dbc_tdof_list` recorded by `SetEssentialTrueDofs`, `rap.cpp:45-46`). This is the faithful-path-or-finding discipline correctly catching an over-edge.
- *divfree chain edges are real, not fabricated.* `L2/divfree-projector lowers-to L1/divfree-projector` is the L2-floor→L1-gate lowering (confirmed: L2 chapter is "the L2 floor under the firm L3", L1 is the "mutation-lifted" gate). The `depends-on` constituents (ksp_solve, apply_linop, axpy) map to the four-step apply prose at `L2/divfree-projector.md:114-135`: step 1 = `apply_linop` (WeakDiv), step 3 = `ksp_solve` (the inner projected-H1 solve, `:124-128`), step 4 = `apply_linop`+`axpy` (Grad correction, `:129-134`); step 2's `set_subvector_zero` is correctly a `reference`. The two theme leaves' `lifts-from`/`lowers-to` endpoints (edits #4, #7, #8) are the themes' own stated LHS/RHS, confirmed in each leaf's opening prose.

**plan-kind-consistency — pass.** The declared kind (a bounded grounding pass scoped to the BC + divfree chains) matches the content; the report ships exactly 8 metadata edits and authors no new algebra. The boundary decision — RESOLVING the carried OQ (every scoped leg was a real, prose-witnessed lowering) while FLAGGING two findings to batch-34 meta-phase (the systematic 10-remaining-L2-L1-theme reachability-cohort gap; the `graded-stack-scheme.md` §5 reachability-vs-well-foundedness clarification) rather than force-fixing them this batch-closing cycle — is the correct boundary. The 10-theme cohort fix is genuinely out of the BC+divfree scope (it touches 10 unrelated L2 chapters), and the convention-asymmetry observation is a methodology-doc concern, which is meta-phase territory per the write-authority partition. Routing both as findings (not silent scope-creep, not parked-without-migration) is in-discipline.

**skill-uptake-survey — pass (telemetry).** The report's shape (citation spot-check) implies `citecheck`, which it invoked (`--anchor`, all `[ok]`); and the dry-run shape implies the graded-stack linter, which it invoked via `--book-src`. No dedicated skill exists for "type a lowering-chain `edges:` block", so no skill-reference gap. Pure presence check; nothing blocking.

### Issues found

None. All 8 checks pass. The central edge-label-fidelity scrutiny confirms the report's load-bearing claim — the `essential_dofs` operand-vs-dissolution-target distinction is correct against the on-disk prose (`bc-elimination-post-composition-dissolution.md:99-101` + `eliminate_essential_bc.md:68-72`), and the divfree-chain `lowers-to` edges correspond to real lowering relationships in the chapter prose rather than fabricated legs. All L0 anchors verify `[ok]` via `citecheck --anchor`, every depends-on edge rests firm-on-firm (well-foundedness holds; `rank_violations` 0 is consistent), and the two findings are routed to the correct boundary (batch-34 meta-phase). This is an all-pass clean report; `overall_status: ready` set by the critic (no repairer will run).

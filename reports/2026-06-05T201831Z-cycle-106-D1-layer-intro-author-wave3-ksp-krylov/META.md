---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T000000Z
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

# META: verification of WAVE-3 op-chapter typed-edge migration (ksp_solve + krylov-step)

## Critique

### Checks run

**citation-validity — pass.** This is a frontmatter-only typed-edge migration; it makes no new operator-semantics / prose / L0 claims. The load-bearing factual assertions are (a) the two `[old]` blocks match on-disk state, (b) the targets resolve, (c) the rank claims hold. I confirmed all three by direct `Read` / on-disk grep (NOT codemap `read_range`). Edit-1's `[old]` block matches `L4/ksp_solve.md` lines 1–15 verbatim (the `consumes:`/`lowers_to:`/`variant_axes:` frontmatter). Edit-2's `[old]` claim — "had NO frontmatter at all, line 1 = `# krylov-step`" — is exactly correct: `L4/krylov-step.md` line 1 is `# krylov-step`, no leading `---`. Both migrated chapters' `## Status` lines read `firm` on disk (ksp_solve:160, krylov-step:235). The §(f) record + reachability claims are mechanically verified below.

**surface-or-evidence — pass.** Frontmatter-only edge migration, no surface (operator/theme text) change — the report explicitly scopes out any prose/semantics change (caveat, lines 247–250), and I confirmed neither `[new]` block touches body text (edit-2 re-emits the `# krylov-step` H1 + lede unchanged after the new frontmatter). This is not a refinement-shaped proposal that modifies surface, nor a rotation_claim; it is graded-stack edge-typing infrastructure. The record-definition sub-check is satisfied trivially: the six `uses-record` targets are ALL existing `concepts/<record>.md` pages already defined on disk (op-params, sim-state, krylov, step-outputs, prev-carry, solve-result) — this report *references* them via edges, it does not name a new undefined record. No definition-home gap.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted. The report explicitly preserves the existing `lowers_to`/lowering relationships as typed `lowers-to` edges without re-characterizing the rotation (ksp_solve's substantive L4>L3 rotation is D3's theme, named but not authored here; krylov-step's L4>L3>L2 chain is likewise only referenced). No rotation claim to grade.

**variant-axis-coverage — pass.** The `variant_axes:` block on ksp_solve is retained verbatim (four coordination-shaping axes); krylov-step's six body axes are unchanged in its body. The migration introduces no new variant branches and hides none — it only adds `edges:` frontmatter. The `restart-shape` axis appears in both chapters and is correctly handled by the existing prose (kernel restart-agnostic / cap owns restart); the migration does not disturb it.

**cross-reference-integrity — pass (load-bearing for this kind).** I verified all 23 distinct edge targets across both `edges:` blocks resolve to existing on-disk files: the 2 L4 ops (krylov-step, iterate-while), L4/index, L3/ksp_solve, L2/krylov-step, and all 13 concept pages. The load-bearing rescue edge `L4/ksp_solve depends-on L4/krylov-step` resolves and is corroborated by ksp_solve's own body (the kernel/driver pairing is asserted throughout §Context/§Signature/§Dependencies). The well-foundedness invariant holds firm/firm: both migrated chapters claim `rank: firm` and their `## Status` lines read `firm`; all six `uses-record` record targets carry `rank: firm` frontmatter (confirmed line-2 of each of the six concept pages); the `lowers-to` targets (L3/ksp_solve, L2/krylov-step) and `folds`/lowers-to peers (iterate-while) read `firm`-per-`## Status` but are untyped (no `rank:` frontmatter) — the report correctly characterizes these as rank-check-skipped (warn-not-fail) and reachability-traversed, which matches the linter's documented behavior (consumes only the blocking bit; a file with no rank/edge frontmatter is counted untyped). No rank violation is introduced. Slug-form check: bare slugs (`L4/krylov-step`, `concepts/op-params`) match the established on-disk edge encoding (verified against `feature/transient.L4.md` / `feature/driven.L4.md` typed blocks).

**edge-label-fidelity — pass.** The `depends-on` vs `reference` partition is faithful per scheme §2/§5 and matches the §(f) `uses-record` spec. `depends-on` carries: the two real folds edges (krylov-step, iterate-while — blocking inner-kernel-fold dependencies the body genuinely invokes), the `lowers-to` lowering edges (depends-on on both endpoints per scheme §5), and the `uses-record` edges to signature-named records. `reference` correctly carries the navigational container `L4/index` (an index → reference, never depends-on) and the non-node narrative-pointer concept pages (solve-monad, state-stratification, etc. — which carry no rank/edges frontmatter, hence no liveness). The `uses-record` classification is faithful: every record target is genuinely named in the respective signature (ksp_solve's `OpParams`/`SimState`; krylov-step's six — `OpParams`, `Krylov`, `SimState`, `StepOutputs`, Form-B `PrevCarry`, plus `SolveResult` as the terminal readout shape — all present in the on-disk §Signature). I cross-checked: krylov-step's `reference` block lists `L2/krylov-step` as a sibling see-also while the blocking dependency is the `depends-on lowers-to L2/krylov-step` edge — a node appearing in BOTH blocks is intentional and scheme-conformant (the blocking edge constrains rank; the bare reference is the navigational duplicate), and the linter consumes only the depends-on bit. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared as a WAVE-3 graded-stack typed-edge migration (frontmatter-only, no semantics change) by a layer-intro-author dispatch. The content shape matches exactly: two `edit:` blocks that replace/prepend frontmatter only, supporting evidence that is edge-classification rationale + linter telemetry. No rough-in placeholders, no mis-classification.

**skill-uptake-survey — pass (telemetry).** The report's shape implies the graded-stack linter procedure, and the report does reference it concretely (`python3 tools/graded-stack-lint/graded_stack_lint.py [--book-src <copy>] [--show-inbound]`) with before/after aggregate + `--show-inbound` rescue output. I confirmed the linter exists at the cited path and uses a custom minimal frontmatter reader (not strict `yaml.safe_load`), which corroborates the plausibility of the reported clean re-run. No skill gap surfaced.

### Issues found

No blocking or warning issues. All 8 checks pass; the graded-stack rank-invariant and reachability additions both pass (firm/firm well-foundedness preserved at 0 violations; the rescue makes krylov-step + the records root-reachable via the already-root-reachable ksp_solve). overall_status set to `ready`.

### Non-blocking observation (out of scope for this report; NOT a finding against it)

The retained `variant_axes:` block on `ksp_solve.md` does not round-trip under strict `yaml.safe_load` — the unquoted scalar `restarted: solve_loop recurses restart_cycle` contains a mid-scalar colon (`mapping values are not allowed here`, on-disk line 12 col 76). **This is PRE-EXISTING on disk** (I confirmed the current on-disk frontmatter already fails strict parse), is NOT introduced by this migration (the block is retained verbatim, untouched), and does not affect either the graded-stack linter (custom minimal reader, edges-only) or the mdBook build (the chapter has rendered for many cycles). It is therefore correctly outside this frontmatter-edges migration's scope. The §(f) `edges:` blocks this report actually authors BOTH round-trip cleanly under strict `yaml.safe_load` (edit-1: 5 depends-on + 8 reference + 4 variant_axes; edit-2: 7 depends-on + 8 reference). Flagging here only as drive-by telemetry for a future touch of that chapter's frontmatter — not as a defect in this report.

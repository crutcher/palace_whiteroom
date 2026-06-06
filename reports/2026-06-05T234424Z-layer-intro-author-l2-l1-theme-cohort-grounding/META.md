---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T235900Z
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
  rank-invariant: warning
  reachability: pass
repaired_at: 2026-06-06T000500Z
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
  rank-invariant: repaired
  reachability: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of graded-stack-l2-l1-theme-cohort-grounding (the bounded reachable-op tranche + Group-B finding)

## Critique

### Checks run

**citation-validity — pass.** Every faithfulness citation in §"Faithfulness confirmations" was spot-checked on disk and supports its `lowers-to` claim:
- `book/src/L2/eigsolve.md:171` — verified; line 171 literally states *"The L2>L1 theme narrating this opening forward is `L2-L1/eigsolve-spectral-transform-composition` (firm, landed cycle-025)."* Backs edge #1 exactly.
- `book/src/L2-L1/ksp-solve-outer-driver-unfold.md:1-21` — verified; the theme head + §Context call it *"the L2>L1 lowering theme for the `ksp_solve` outer-driver composition … the downward edge of the firm L2 `ksp_solve` driver."* Backs edge #2.
- `book/src/L2-L1/krylov-step-kernel-defusion.md:1-12` — verified; the theme expands `krylov-step` into the *"explicit sequence of seven firm L1 leaves (`apply_linop, axpy, axpby, axpbypcz, dot, nrm2, scal`)"* and cites `book/src/L2/krylov-step.md:96`. Backs edge #3 and the leaf list.
- `book/src/L2/krylov-step.md:96` — verified; §Dependencies lists exactly the seven L1 leaves the from-scratch `depends-on` block enumerates. `:101-108` matches the concept-reference list.
- `book/src/L2-L1/linear-combination-fold-specialization.md:1-12` and `book/src/L2-L1/inner-product-fold-specialization.md:1-12` — verified; both theme heads describe the fold→fixed-arity-leaf lowering of their respective L2 op. Back edges #4 and #5. No `verified_against:` YAML block in this report, so that sub-check no-ops.

**surface-or-evidence — pass.** This is a frontmatter-only edge-typing/grounding dispatch with no prose claims; it modifies no operator/theme surface text and asserts no new algebraic claim, so the refinement-shaped-proposal branch does not apply. The record-definition sub-check no-ops: no new record/struct signature is introduced. The evidence shape (theme-prose faithfulness citations + linter delta) is appropriate to the dispatch kind.

**rotation-quality — pass (no-op).** Not applicable: no algebraic/structural rotation is asserted. The dispatch types existing `depends-on` edges; it does not claim any L_{n+1}→L_n compaction of its own.

**variant-axis-coverage — pass (no-op).** Not applicable: a frontmatter edge-typing pass has no variant axes. The host ops' variant axes are untouched.

**cross-reference-integrity — pass.** All edge target slugs resolve on disk: the 5 theme targets (`L2-L1/{eigsolve-spectral-transform-composition, ksp-solve-outer-driver-unfold, krylov-step-kernel-defusion, linear-combination-fold-specialization, inner-product-fold-specialization}.md`) all exist; all 5 host op files (`L2/{eigsolve, ksp_solve, krylov-step, linear_combination, inner_product}.md`) exist; all 7 L1 leaf targets exist; all 10 concept `reference` targets in the from-scratch `krylov-step` block exist (`concepts/{solver-as-operator, derived-view-hoisting, variant-absorption, first-iteration-unrolling, sequential-obstruction, solve-monad, state-stratification, apply_BA, orthogonalization, constructed-operators}.md`). The c108 precedent `book/src/L2/divfree-projector.md:11-17` exists and matches the cited block-mapping `lowers-to` shape. All 5 `[old]` edit anchors match on-disk content uniquely (count==1 each, mechanically confirmed by applying the edits).

**edge-label-fidelity — pass.** Each `lowers-to` edge points from the L2 host op to its genuine L2>L1 lowering theme, and the cited prose discusses that exact edge (the §"Faithfulness confirmations" prose maps each op→theme correctly; spot-checks above confirm). The faithful-path-or-finding split was verified correct on disk: the 5 Group-B themes' host L2 ops (`inner_product`, `chebyshev-iteration`, `gram`, `incremental-least-squares`, `orthogonalize`) are themselves unreachable, so a faithful edge from them cannot flip the theme — correctly routed as a finding, not forced. `deflate`/`deflate-composition-lowering` correctly excluded (STOP-PROPOSING demand-gated list; confirmed at `scaffolding/priorities.md:32,54,95`).

**plan-kind-consistency — pass.** The dispatch declares itself a grounding/edge-typing pass with frontmatter-only edits; content shape matches. The linter delta was independently REPRODUCED (see below): I applied the 5 edits to a scratch copy, ran `python3 tools/graded-stack-lint/graded_stack_lint.py --show-inbound`, and observed exactly the claimed before/after — baseline reachable 102, detritus 157, untyped 60, rank_violations 0; after reachable 107 (+5), detritus 152 (−5), STRONGER GARBAGE 35→34, untyped HOLDS 60, rank_violations HOLDS 0. The 4 Group-A themes flip out of `[garbage?]` with reachable inbound edges; the 5 Group-B themes + deflate + `inner-product-fold-specialization` remain `[garbage?]` as claimed (edit #5's edge-lay correctly non-flipping). I then reverted all 5 files; `git status --short book/` is empty. The +5-not-+4 explanation (the from-scratch `L2/krylov-step` block makes the op itself a typed-and-reachable node) is consistent with the observed delta.

**skill-uptake-survey — pass.** The dispatch is a hand-applied grounding pass mirroring the c108 precedent; the relevant tooling (`graded_stack_lint.py`) is invoked and its delta reported. No omitted skill invocation of note.

**rank-invariant (graded-stack check 9) — warning.** The empirical `rank_violations = 0` is REPRODUCED and holds — the linter raised no violation. However, the report's prose claim *"every depends-on target is firm (rank 3); well-foundedness holds firm→firm throughout"* (CYCLE.md:138, :255-256) is **over-stated for 3 of the 7 L1 leaves in the from-scratch `krylov-step` block.** `book/src/L1/{axpy,axpby,axpbypcz}.md` carry **no frontmatter at all** — no `rank:`/`firmness:` field and no `edges:` block (they begin directly with `# axpy` etc.). The linter's rank histogram classes them under `typed-no-rank` (the histogram shows `typed-no-rank: 80`), NOT `firm`. So while the chapter PROSE describes them as "the firm operator definition", the rank-invariant machinery does not see them as rank-3 nodes; the well-foundedness check passes vacuously over edges whose target has no declared rank, not because the target is provably firm. This is why `rank_violations` HOLDS 0 (the edges are not violations), but the report's "all targets firm (rank 3)" framing is inaccurate for `axpy`/`axpby`/`axpbypcz`. The other 4 leaves (`apply_linop`, `dot`, `nrm2`, `scal`) DO carry `rank: firm`. Severity: low — the empirical result the report relies on is correct and reproduced; only the supporting rationale's blanket "rank 3" assertion is loose. Worth recording because it surfaces a real latent gap (three high-fan-out L1 BLAS leaves carry no typed-edge frontmatter / no rank token), which is the kind of thing a future tranche or the meta-phase should pick up.

**reachability (graded-stack check 10) — pass.** All grounded host ops are reachable from the feature-surface roots over `depends-on` edges (confirmed: the 4 Group-A themes show reachable inbound `<- L2/<op>` in the post-edit lint). The Group-B routing correctly identifies the unreachable-host root cause and the routed OQ (`l2-reduce-orthogonalize-cohort-itself-unreachable-blocks-theme-grounding`) is not a duplicate (absent from `scaffolding/open-questions.md`). The +5 reachability gain (incl. `L2/krylov-step` itself becoming a typed-reachable node) is reproduced.

### Issues found

1. **`rank-invariant` over-claim on 3 L1 leaves (CYCLE.md:138 frontmatter comment; CYCLE.md:255-256 §Verification (ii)).** The report states all `depends-on` targets of the from-scratch `L2/krylov-step` block are "firm (rank 3)" and well-foundedness holds "firm→firm throughout." On disk, `book/src/L1/axpy.md`, `book/src/L1/axpby.md`, and `book/src/L1/axpbypcz.md` carry **no frontmatter and no `rank:` field** — the linter classes them `typed-no-rank`, not `firm`. The empirical `rank_violations = 0` is correct and reproduced (edges to no-rank targets are not violations), but the "all targets rank-3 firm" rationale is inaccurate for these three. Severity: low (does not affect the verified linter result; the chapters' prose does call them firm). Candidate repair: soften the rationale wording to "targets are firm-in-prose; `axpy`/`axpby`/`axpbypcz` carry no rank token yet (typed-no-rank), so the rank-invariant holds vacuously over those edges" — OR (out of frontmatter-only scope, route as finding) note the latent gap that three high-fan-out L1 BLAS leaves lack typed-edge/rank frontmatter.

No other issues. Citations, edge fidelity, cross-references, the faithful-path-or-finding split, the deflate exclusion, and the full linter delta (102→107, detritus 157→152, rank_violations HOLDS 0) all verified and reproduced independently.

## Repair

### Fixes attempted

- **Finding:** `rank-invariant` over-claim — the report's well-foundedness rationale asserts all 7 `depends-on` targets of the from-scratch `L2/krylov-step` block are "firm (rank 3)" with well-foundedness holding "firm→firm throughout" (CYCLE.md:138 frontmatter comment, CYCLE.md:255-256 §Verification (ii)), but `book/src/L1/{axpy,axpby,axpbypcz}.md` carry no frontmatter / no `rank:` token (`typed-no-rank`), not `firm`.
  - **Decision:** repaired.
  - **Action:** Two pre-integration prose edits to CYCLE.md, rationale-only (the `edges:` proposed-change blocks themselves are UNCHANGED — the edges are correct and verified):
    1. CYCLE.md proposed-change #3 frontmatter comment (the `[new]` block for `book/src/L2/krylov-step.md`): softened "All depends-on targets firm (rank 3) … well-foundedness holds firm→firm" → states `apply_linop`/`dot`/`nrm2`/`scal` carry `rank: firm`, while `axpy`/`axpby`/`axpbypcz` are `typed-no-rank` so the invariant holds vacuously over those three edges and `rank_violations` stays 0.
    2. CYCLE.md §Verification (ii): same softening, plus a pointer to the new latent-gap OQ.
  - **Verification of which leaves are firm:** confirmed on disk — `book/src/L1/{apply_linop,dot,nrm2,scal}.md` all carry `rank: firm`; `book/src/L1/{axpy,axpby,axpbypcz}.md` begin directly with `# axpy`/etc., no frontmatter (matching the critic's `typed-no-rank` classification).

### Unrepairable findings

- **Finding (latent gap surfaced by the critic):** three high-fan-out L1 BLAS leaves `axpy`/`axpby`/`axpbypcz` lack typed-edge/rank frontmatter (no `rank:`, no `edges:`).
  - **Decision:** unrepairable (in-place) — routed to intake. This is a future authoring tranche (give the three leaves `rank: firm` + `edges:` frontmatter), NOT a mechanical fix to this report. Authoring frontmatter on artifact files is out of repair authority (artifact writes belong to the integrator; substantive typing belongs to the typing campaign).
  - **Action:** appended OQ `l1-blas-leaves-axpy-family-lack-rank-frontmatter` to `scaffolding/open-questions.md` (slug verified unique), recommending the leaves acquire `rank: firm` + `edges:` in the lazy-tail typing campaign (priorities.md item 2), and noting that until then `depends-on` edges into them hold the rank invariant only vacuously. Routed to the typing campaign, not to a follow-up dispatch this cycle.

## Suggested resolution

`overall_status: ready`. The sole warning was low-severity and mechanically fixable: the empirical `rank_violations = 0` is correct and independently reproduced by the critic, and only the report's supporting rationale wording was loose. The rationale is now softened in-place (rationale prose only — no proposed `edges:` block touched), so the integrator will not propagate an inaccurate "all targets firm (rank 3)" claim. The underlying latent gap is captured as an intake OQ for the typing campaign. No follow-up agent needed; the integrator may apply the report as-is.

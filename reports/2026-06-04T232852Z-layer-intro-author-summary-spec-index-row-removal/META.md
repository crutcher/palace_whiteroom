---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T23:47:01Z
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
repaired_at: 2026-06-04T23:58:00Z
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

# META: verification of "shared-index removal for the 4 c097 slice deletions" (cycle-097 D5)

## Critique

### Checks run

**citation-validity — warning.** Every structural anchor in the proposed-changes blocks was re-verified line-for-line against the live artifact and matches exactly: SUMMARY.md `:294`/`:295`/`:298`/`:300` deleted rows + `:292`/`:293`/`:296`/`:297`/`:299` survivors (Read of `book/src/SUMMARY.md:290-300`); spec/index.md deleted rows `:18`/`:19`/`:21`/`:22` + survivors `:15`/`:16`/`:17`/`:20`/`:23` (Read of full file); and **every one of the 10 dependency-map edit-block `[old]` anchors matches the file verbatim** (Reads of `:150-194`, `:214-264`, `:278-318`, `:347-392`). The one defect is an **inaccurate evidence count**: §Supporting-evidence line 239 (and §Open-questions line 248) assert the snake_case grep "returns 44 hits" and "all 44 snake_case hits are clean removals." The actual count is **61** (`grep -nE '(divfree|cg_preconditioning_framework|plane_rotation_stream)' | grep -v 'plane-rotation-stream|sparse-triangular-solve'` → 61; per-slug: divfree 28, cg_preconditioning_framework 27, plane_rotation_stream 6). The edit blocks themselves are **complete** — I independently tallied removals (divfree 3+4+5+2+6+6+1+1=28, cg_pf 6+6+5+10=27, prs 1+1+4=6 = 61) and every snake_case edge is captured — so the under-count is a stale/wrong tally in the prose evidence, not a coverage gap. Warning (not pass) because a citation-validity check on a removal-only report leans on the asserted hit-count being the audit's completeness witness, and 44≠61 means that witness is wrong even though the underlying removals happen to be exhaustive.

**surface-or-evidence — pass.** Not a refinement-shaped proposal; this is a structural index/GC edit (row + mermaid-edge removal) with no operator/theme surface change and no rotation claim. No record is named in any signature. Pass (not applicable to the removal-only shape).

**rotation-quality — pass.** Not applicable: no algebraic/structural rotation is asserted; this report removes stale index entries and reachability-dead mermaid edges. Marked pass per the no-op convention.

**variant-axis-coverage — pass.** Not applicable: no operator with variant axes; an index-row/edge removal has no variant combinations to cover.

**cross-reference-integrity — warning.** The narrow load-bearing check the dispatch named PASSES: after the proposed removals, NO surviving SUMMARY row or spec-index row points at a deleted file — I confirmed the 5 SUMMARY survivor links (`:292`/`:293`/`:296`/`:297`/`:299`) and 5 spec-index survivors (`:15`/`:16`/`:17`/`:20`/`:23`) all resolve to surviving slice files, and the snake_case-vs-hyphenated disambiguation is correct (the hyphenated `plane-rotation-stream` edges at `:186-193`/`:74-101` and `sparse-triangular-solve:::planned` at `:81`/`:99-101` are genuinely distinct planned-marker/L1-stream nodes and are left intact — verified by grep). HOWEVER, the report's broader claim (§Summary, "so the corpus is consistent and the finalize rebuild stays green") is **not supported by the report's own scope**: there are **18 markdown-link references** of the form `[…](../spec/slices/<deleted>.md)` in files OUTSIDE the three index surfaces this report touches — `book/src/concepts/{constructed-operator-factory,counter-update,solver-as-operator,complex-from-real-lift,build-time-vs-run-time-stratification,two_operator_split,finest-level-unwrap,negative-result-slice,sequential-obstruction,scope-out-obstruction,plane-rotation-stream,givens,givens_apply,givens_generate}.md`, `book/src/L1/ksp_solve.md:131`, and `book/src/L1-L0/triangular-solve-obstruction.md:277`. Once D1–D4 delete the four target files, every one of these 18 becomes a dangling intra-book relative link. `book/book.toml:70-73` excludes only `reference/.*` and `skills/.*` from linkcheck2 — `spec/slices/*.md` links are NOT excluded — so these are real linkcheck2 hits. (Mitigating, not eliminating: `book.toml:61` sets `warning-policy = "warn"`, so these degrade to warnings rather than a hard build failure; the SUMMARY/spec-index removals this report DOES make are the true hard-breakers, since mdBook itself fails on a SUMMARY entry whose file is missing.) The report nowhere mentions these 18 back-references, and per the no-shared-context invariant it is not established within this report's evidence whether D1–D4 (the deleting dispatches) own them. This is the gap to surface: the "rebuild stays green / corpus is consistent" assertion overreaches the report's actual three-file scope.

**edge-label-fidelity — pass.** The mermaid edges removed are exactly those whose source node-id is a deleted snake_case slug; each removed `u --> v` edge has `u` ∈ {divfree, cg_preconditioning_framework, plane_rotation_stream}, and the prose correctly narrates which block each cluster sits in (L1/L2/L3/L4 mermaid blocks at `:128-194`/`:198-264`/`:273-318`/`:327-392`). No edge whose source is a survivor or a hyphenated planned-node is removed. The block-label-to-line-range mapping is accurate.

**plan-kind-consistency — pass.** The report is a structural index-maintenance edit (graded-stack P2 reachability-GC follow-on to slice deletion); the content shape — three proposed-changes targets, removal-only, no new claims — matches that kind. No mis-classification.

**skill-uptake-survey — pass (telemetry).** The shape (phase-1 slice reachability removal) is adjacent to `phase-1-slice-reduction-audit`, but that skill governs *recommending* a slice for reduction (concept-page-grep before reduction), whereas this report is the *downstream index-removal* once deletion is already decided by D1–D4. No skill invocation is expected or missing; surfaced for telemetry only. (Observation: a "slice-deletion shared-index sweep" skill that enumerates ALL inbound links — index rows AND body back-references — would have caught the 18-link gap above; noting, not requiring.)

### Issues found

1. **`cross-reference-integrity` (CYCLE.md §Summary line 19; §Proposed-changes scope) — warning, build-readiness.** 18 markdown links to the 4 deleted slice files exist outside the three index files this report scopes (14 `book/src/concepts/*.md` pages + `book/src/L1/ksp_solve.md:131` + `book/src/L1-L0/triangular-solve-obstruction.md:277`; full list in the check paragraph). After D1–D4 delete the targets these become dangling links; `book.toml:70-73` does not exclude `spec/slices/*.md`, so they are real linkcheck2 hits (downgraded to warnings by `warning-policy = "warn"` at `book.toml:61`, not hard failures). The report's §Summary claim that "the corpus is consistent and the finalize rebuild stays green" overreaches: it is true for the three index surfaces but unverified for these 18 back-references, which the report does not mention and whose ownership (D5 vs. the D1–D4 deleting dispatches) is not established within this report's evidence. Concrete: either these back-references must be repointed/removed by some dispatch this cycle, or the report's green-build claim should be narrowed to its actual three-file scope with the 18 back-references explicitly routed (to D1–D4 or an Open question).

2. **`citation-validity` (CYCLE.md §Supporting-evidence line 239; §Open-questions line 248) — warning, inaccurate count.** The report states the dependency-map snake_case grep "returns 44 hits" and that "all 44 snake_case hits are clean removals." The actual count is 61 (divfree 28 + cg_preconditioning_framework 27 + plane_rotation_stream 6). The removals are nonetheless exhaustive — I tallied the 10 edit blocks to exactly 61 deleted edges, matching the grep — so the defect is a wrong evidence-tally, not a coverage miss. The 44 should read 61 in both places.

### Notes for the repairer/integrator

- The proposed-changes blocks are mechanically sound and apply-safe in isolation: all 10 dependency-map `[old]` anchors, both SUMMARY blocks, and the spec/index two-block split match the live artifact verbatim, and the survivor/hyphenated-node preservation is correct. The two warnings are about (1) a scope/claim mismatch on whole-corpus build-greenness vs. three-file actual scope, and (2) a wrong hit-count in prose — neither blocks application of D5's own edits.
- The §spec-index "no 9→5 count statement to update" reasoning was verified: `book/src/spec/index.md:1-9` carries no integer slice tally (qualitative description + frozen "Status as of 2026-05-26" date only). That sub-claim is accurate.

## Repair

### Fixes attempted

- **Finding 1 — cross-reference-integrity (warning): overreaching whole-corpus green-build claim.** The §Summary asserted "the corpus is consistent and the finalize rebuild stays green," which is true at the cycle level but false as scoped to D5 alone (18 inbound markdown links to the 4 deleted slices live OUTSIDE D5's three index files).
  - **Decision**: repaired.
  - **Action**: Edited CYCLE.md §Summary (`reports/.../CYCLE.md`, §Summary, the "As the single owner …" paragraph). Softened the claim to D5's actual three-file scope: D5 makes the **index/SUMMARY/mermaid** references consistent; the remaining **18 inbound markdown links** (14 `concepts/*.md` + `L1/ksp_solve.md:131` + `L1-L0/triangular-solve-obstruction.md:277`) are explicitly routed to sibling dispatches **D1–D4 this same cycle** (D1 7 cg_preconditioning_framework concept links; D2 `L1/ksp_solve.md` + `L1/divfree-projector.md`; D3 `triangular-solve-obstruction.md:277` self-link + 3 sparse-trisolve anchors; D4 5 plane_rotation_stream concept links). The new prose states the co-landing (integrator applies all proposed-changes before the single finalize `cargo make book`) keeps the rebuild green at the **cycle** level, and explicitly notes D5 alone does not make the whole corpus consistent. This is a mechanical scope-narrowing of an overreaching claim — no substantive content authored; the sibling-dispatch routing was supplied as repair context.

- **Finding 2 — citation-validity (warning): wrong edge tally (44 vs. actual 61).** §Supporting-evidence (~:239) and §Open-questions (~:248) stated the snake_case mermaid grep "returns 44 hits"; the actual count is 61 (divfree 28, cg_preconditioning_framework 27, plane_rotation_stream 6). The removals are still exhaustive (critic independently tallied 61 deleted edges across the 10 edit blocks).
  - **Decision**: repaired.
  - **Action**: Edited CYCLE.md in both locations (`reports/.../CYCLE.md`, §Supporting-evidence "dependency-map.md edges" bullet and §Open-questions "Ambiguous-edge check" bullet). Corrected 44 → 61 and added the per-slug breakdown (divfree 28 / cg_preconditioning_framework 27 / plane_rotation_stream 6) to the evidence bullet. Pure tally correction; the proposed row/edge removals were NOT altered.

### Build-safety confirmation (no edit)

- The critic observed `book/book.toml:61` sets `warning-policy = "warn"` and `book.toml:70-73` excludes only `reference/.*` + `skills/.*` (NOT `spec/slices/*`), so a dangling intra-book link to a deleted slice would surface as a linkcheck2 **warning, not a hard fail**. Since D1–D4 repoint all 18 inbound links this same cycle, the point is moot — recorded here as a build-safety confirmation, not a concern. (The SUMMARY/spec-index removals D5 DOES make are the genuine hard-breakers, since mdBook itself fails on a SUMMARY entry whose file is missing — those are exactly the removals D5 lands.)

### Unrepairable findings

None. Both warnings were mechanical/surgical text corrections within repair authority (an overreaching-claim scope-narrowing with sibling routing supplied, and a wrong-tally correction); the proposed-changes blocks were verified correct + exhaustive by the critic and left untouched.

## Suggested resolution

`ready`. Notes for the integrator:
- All 8 checks now resolve to pass / repaired / not-needed; no deferral needed.
- This report (D5) is the shared-index owner for the cycle-097 first-tranche slice deletions; its three proposed-changes targets (SUMMARY.md, spec/index.md, concepts/dependency-map.md) MUST co-land in the same finalize build as the D1–D4 slice deletions + inbound-link repointings — this is satisfied by the standard integrator flow (all per-report proposed-changes apply before the single `cargo make book`). The softened §Summary now documents that co-landing dependency explicitly.
- The 10 dependency-map `[old]` anchors, both SUMMARY blocks, and the spec/index two-block split were critic-verified verbatim against the live artifact; survivor rows and hyphenated planned-node edges are preserved by design.

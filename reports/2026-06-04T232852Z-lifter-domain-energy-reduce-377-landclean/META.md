---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T234500Z
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

# META: verification of "Re-anchor stale matrix-weighted-norm maturity narration in domain_energy_reduce.md"

## Critique

### Checks run

**citation-validity — pass.** Ran `python3 tools/citecheck/citecheck.py --scan CYCLE.md --quiet` → `6 ok, 0 failing (6 citations checked)`; no bounds or path-hygiene drift. The load-bearing c091 firm-flip evidence was re-read on disk: `book/src/L1/matrix-weighted-norm.md:4` reads `rank: firm`; `:121-123` `## Status` reads "`firm` — promoted from `rough-in (test-coverage-bounded)` ... enacted cycle-091, the batch-29 LEAD `matrix-weighted-norm-firm-flip-and-cascade-wave`"; `:128` carries the "firm-on-positive-structure escape" basis. The report's central premise (matrix-weighted-norm is firm c091) is true on disk. No `verified_against:` block in this report, so the YAML round-trip sub-check no-ops.

**surface-or-evidence — pass.** This is a within-file maturity re-anchor (refinement of existing text) backed by the dependency's on-disk firm Status — retroactive-evidence-driven correction of stale tokens, the allowed shape. Each of the three `[old]` strings was confirmed to exist verbatim at the cited site and to be genuinely stale: `:377` reads `(rough-in (test-coverage-bounded) —` (contradicts the same file's `:209` `(firm c091)` and `:286-288` "BOTH folded primitives now have firm L1 homes"); `:268` reads `(firm / rough-in) L1` (the rough-in half is matrix-weighted-norm, now firm); `:374` reads `(the rough-in test-gate, §Status point 2)` (Status point 2 at `:289-300` explicitly holds the missing per-domain test REDUNDANT under the escape — so "rough-in test-gate" mis-narrates it as live). Each `[new]` wording is accurate against the authoritative in-file Status/Dependencies. No record is newly named in a signature here (the record-definition obligation is already discharged in-chapter at `:227-255` `## Record definition` for `DomainOpMap`), so the record-definition sub-check no-ops.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted; this is a maturity-token re-anchor, not a representational shift. Per the report's own framing and the dispatch note, rotation is N/A.

**variant-axis-coverage — pass (not applicable).** No new operator/theme surface with variant axes is introduced; the file's existing `field-kind`/`element-type` axes (`:13-15`) are untouched. N/A to a prose re-anchor.

**cross-reference-integrity — pass.** All link targets in the touched/quoted prose resolve: `../L1/matrix-weighted-norm.md`, `../L1/participation_ratio.md` both exist with firm status on disk. No `firm`-claim-inside-fence build-readiness concern: the file is already `firm` on disk and the report introduces no new firm body or `## Status` apparatus inside its edit fences — the three `edit:` blocks are single-sentence prose swaps, not a chapter body. Fence parity in the report is balanced. The rank-invariant cross-check holds: `domain_energy_reduce` (rank firm) depends-on `participation_ratio` (firmness firm, c077) and `matrix-weighted-norm` (rank firm, c091) — both deps ≥ firm, so `rank(u)=firm ≤ min(deps)` is preserved and no frontmatter flip is needed, as the report claims.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is asserted (this is a within-file L4-entry re-anchor, not a lowering theme). The report's rank-invariant claim that no `rank:`/`edges:` frontmatter change is needed was independently confirmed: frontmatter `rank: firm` already on disk (`:4`), both depends-on deps firm. Correct.

**plan-kind-consistency — pass.** Declared shape is a land-clean within-file re-anchor (rewrite, not authorship); content matches — three bounded prose-token swaps, no decomposition/signature/law change, explicitly "a pure rewrite, not authorship" (`:147-148`). No firm-operator-with-rough-in-placeholder mis-classification.

**skill-uptake-survey — pass (telemetry).** The report cites running `citecheck.py --anchor` for its own L0 evidence (`:328`) and references the batch-29 `firm-flip-leaves-within-file-stale-narration` self-consistency-grep class as its procedure. No dedicated skill is mandated by this shape; the within-file self-consistency grep is the relevant informal procedure and was applied (the catalog at `:44-66` enumerates stale vs confirmed-not-stale sites). Pure presence note, non-blocking.

### Issues found

None. All three `[old]` anchors match disk verbatim; all three are genuinely stale against the file's own authoritative firm `## Status`/`## Dependencies`; all three `[new]` re-wordings are accurate. The c091 firm-flip is real on disk, the rank invariant is preserved with no frontmatter edit, and citecheck is clean.

The deliberate scoping-out of the `:313-316` gram_reduce "STAYS rough-in" narration is **reasonable, not a miss**. That narration concerns a different verb (`gram_reduce`) gated by its own off-diagonal `bilinear-form` primitive. I independently confirmed `book/src/L1/bilinear-form.md:5` now reads `rank: firm` (promoted c095, `:48`), so that gram_reduce narration is indeed itself now stale — but it is a distinct verb's residue belonging to a separate gram_reduce-cohort land-clean, correctly flagged for a follow-up OQ rather than swept into this single-residue-cohort dispatch (`:139-146`). The one-residue-cohort-per-dispatch boundary is sound and the follow-up is surfaced, not dropped. Likewise the `:212`/`:280`/`:282`/`:288` past-tense "formerly-rough-in" sites are correctly identified as discharged-gate records, not stale assertions.

All 8 checks pass; this clean report carries `overall_status: ready`.

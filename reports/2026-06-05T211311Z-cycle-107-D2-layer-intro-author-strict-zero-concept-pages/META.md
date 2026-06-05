---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T214500Z
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

# META: verification of "strict-zero concept pages → non-node `reference`-only `edges:` blocks" (cycle-107 D2)

## Critique

### Checks run

**citation-validity — pass.** This is a pure-frontmatter typing pass: it adds no prose, no
semantic claims, no source-range citations. The only "citations" are the 45 distinct
`reference` edge slugs and the 15 `[old]` anchors. I existence-verified all 45 distinct
targets on-disk (`book/src/<slug>.md`) — 0 missing of 45. The `--strict` linter run on the
applied scratch tree confirms zero unresolved reference targets (exit 0). The frontmatter is
pure `reference:`-only YAML (no `note:` scalar / `verified_against:` block), so the
YAML-round-trip sub-check is N/A. No citation drift possible (no `file:lines` pinpoints).

**surface-or-evidence — pass.** Not a refinement-shaped proposal (no operator/theme surface
modified, no rotation_claim) and not a record-definition: these are non-node narrative /
literature-background / concept-framing pages, not signature-named records needing a
definition home. The check is structurally inapplicable; the typing adds a machine-readable
see-also graph, not a claim. Marked pass (not-applicable to a non-node frontmatter-typing
report).

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is
asserted — frontmatter typing rotates nothing.

**variant-axis-coverage — pass (not applicable).** No operator with variant axes is touched.

**cross-reference-integrity — load-bearing here, and pass.** Two sub-surfaces verified.
(1) The 15 `[old]` prepend anchors each match the target page's verbatim first heading
(spot-checked all 16, including the non-obvious ones: `chebyshev-iteration → # Chebyshev
iteration`, `erasure-scope → # Concept: erasure-scope`, `constructed-operators → # constructed
operators`, `derived-view-hoisting → # Derived-view hoisting`). Each anchor is unique as the
insertion point (every file begins with `# `, no pre-existing frontmatter — confirmed via
`grep -L '^edges:'` equivalent). (2) All 45 distinct `reference` targets resolve on-disk.
The report's claim that prose-only mentions with no live target (`L2/cg`, `L2/gmres`,
`L2/multigrid`, `lanczos-spectral-estimate`) were NOT manufactured into edges is verified —
those slugs are genuinely absent on-disk, so their omission is correct (no dangling edges).

**edge-label-fidelity — pass.** The classification question for this kind is `reference` vs
`depends-on`. Per the batch-33 ratified non-node convention (`graded-stack-scheme.md` §5
"Non-node concept-page encoding — UNIFIED" + §6 checklist step 4), a non-node narrative /
methodology / literature-background concept page carries **NO `rank:`** and an **`edges:
reference:`-only block** — every see-also link is a `reference` edge because a non-node
asserts no blocking dependency. All 15 blocks are `reference:`-only with no `rank:` —
correct. The no-`rank:` choice is verified against the scheme and against the live sibling
exemplars: `concepts/{dot,axpy,nrm2,scal,apply_linop}` already carry exactly this shape
(`reference:`-only block, no `rank:`), and none carry a `rank:`. The new blocks are
byte-pattern-identical in shape to the ratified siblings.

**plan-kind-consistency — pass.** The declared kind (LOW lazy-tail non-node typing pass,
15 pages) matches the content shape exactly. Three scoping/borderline calls verified correct:
(1) `counter-update` DEFERRED — confirmed on-disk it carries NO `## Status` / Signature /
Algebraic-laws / Evidence apparatus, so deriving a `rank:` would be a guess; the §5
reconciliation ratifies it as a NODE (needs `rank:` + `depends-on`), which is out of scope
for a `reference`-only-block dispatch. Deferring + flagging the OQ
`concepts-counter-update-needs-node-rank-and-depends-on-edges` is the correct conservative
call, not guessing. (2) `chebyshev-iteration` confirmed non-node — no firm apparatus on-disk;
`L2/chebyshev-iteration` + `L3/chebyshev` are the operator homes (distinct files, both exist),
this page is literature-background. (3) D1 disjointness honored — `concepts/dofset` and
`concepts/set_subvector_zero` are NOT among the 15 edited pages.

**skill-uptake-survey — pass.** No skill is specifically implied for non-node frontmatter
typing beyond the scheme convention itself, which the report cites directly
(`graded-stack-scheme.md` §5/§6 + the sibling-page slug convention). Pure telemetry; nothing
to surface.

### Linter / metric independent reproduction

I reproduced the before/after on a scratch copy of `book/src` (NOT the live tree) with all 15
blocks applied via `graded_stack_lint.py`:

- BEFORE (live tree): `0 rank violation(s), 156 detritus, 76 untyped` — **matches the report.**
- AFTER (scratch + 15 blocks): `0 rank violation(s), 170 detritus, 61 untyped` — **matches
  the report exactly.** `--strict` exits 0 with no unresolved targets and no errors.

The counterintuitive `detritus 156→170` (UP) is verified to be a benign reclassification
artifact, NOT a regression. A `comm` of the BEFORE vs AFTER detritus node-sets shows the +14
new detritus entries are **exactly** the 14 newly-typed non-node pages (they move from the
*untyped-detritus* bucket into the *typed-but-non-node-detritus* bucket — the same `[garbage?]`
disposition the pre-existing `concepts/{dot,nrm2,scal,apply_linop,axpy}` reference-only pages
already hold; a non-node carries no liveness by construction). No previously-live node was
orphaned, and no node was newly added as a *node* to the DAG. The report's "bonus" claim is
also confirmed: `concepts/solve-monad` is the 15th page and does NOT appear in the new-detritus
set — it left both lists (became reachable via an inbound navigational edge), which is why the
delta is +14 and not +15. `rank_violations` held at 0 (no `rank:`/`depends-on` introduced).

### Issues found

None. All 8 checks pass. The proposal is a faithful, mechanically-verified application of the
batch-33-ratified non-node concept-page encoding: 15 `reference:`-only / no-`rank:` blocks
whose anchors and 45 targets all resolve on-disk, with the linter invariants reproduced
exactly (untyped 76→61 toward the planner target, rank-violations held at 0, detritus delta a
verified reclassification artifact). The `counter-update` deferral and the D1 exclusion are
both correct conservative calls. Setting `overall_status: ready` (all-pass clean report; no
repairer will run).

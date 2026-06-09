---
verifies: ../CYCLE.md
critiqued_at: 2026-06-09T05:06:00Z
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

# META: verification of cycle-154 D1 batch-51-OPENER hygiene sweep + 61-untyped authoritative classification

## Critique

This is an **audit-class** cross-layer report (no `book/` mutation): a per-batch hygiene sweep (CLEAN BILL 8/8) plus the authoritative partition of the `untyped=61` lint cohort into disposition buckets. The 8 critic checks are applied with the audit/observation-kind adaptations (rotation / surface-evidence / variant-axis largely no-op for a maintenance-sweep observation; the load-bearing checks are citation-validity + cross-reference-integrity + plan-kind-consistency). Every load-bearing claim was reproduced independently on-disk.

### Checks run

**citation-validity — pass.** Every quantitative and locational claim was re-derived, not taken on faith. I reran `graded_stack_lint.py --book-src book/src --json`: the totals block matches the report's baseline EXACTLY (`files:392, typed:331, untyped:61, roots:45, rank_violations:0, unresolved_depends_on_targets:0, promotion_frontier:11, detritus:123, true_detritus:51, reference_reachable:247, expected_unreachable_outside_dag:54`). The `untyped` list is exactly 61 nodes, bucketing on-disk to `{L0/:26, meta-reviews/:26, methodology/:5, navigational(OTHER):4}` — matching the report's (a)=35 (26 meta-reviews + 5 methodology + 4 navigational) and (b)=26 L0 partition with zero discrepancy. The kernel-api edge line-citations resolve: `L1/libceed-quadrature-kernel-impl.md:14`, `L1/multigrid-relaxation-smoother.md:26`, and `L3/eigsolve-impl.md:21,23` all carry the cited `kind: realizes-kernel-api` declaration. The sharding-gate citation `L4/sharding-decompose-reduce.md:4-7` resolves to `rank: roadmap_goal` / `status: roadmap_goal` with a `reference:`-class edge block. `semantics/index.md:3` is the SEMANTIC-CONSOLIDATION governing header; `:24` is `## 0.1 Active-management discipline`. The methodology caveat is accurate: `methodology/graded-stack-scheme.md` lines 74/93/124/148 carry `rank:`/`edges:` tokens INSIDE code-block examples (`rank: obstruction # the kind`, etc.), and the page has no frontmatter rank — correctly classified untyped-by-design.

**surface-or-evidence — pass (audit-class).** No refinement-shaped surface proposal — this is a pure audit/classification observation with no `book/` mutation, so this check no-ops (not applicable to an audit-class sweep). The record-definition sub-check is also inapplicable: the report names no new record/struct in a signature. Evidence framing is sound: the classification is backed by reproduced `--json` output + per-bucket `grep` evidence, all of which I reproduced.

**rotation-quality — pass.** Not applicable to an audit/classification observation — the report asserts no algebraic/structural rotation. Marked pass per the inapplicable-shape convention.

**variant-axis-coverage — pass.** No operator/theme with orthogonal variant axes is proposed. The classification IS exhaustive over its own axis (the 61-node partition is arithmetically complete, 35+26+0=61, with zero uncategorized remainder — I confirmed the lint's untyped list has no member outside the three buckets), which is the analogue of axis-coverage for a partition claim. Pass.

**cross-reference-integrity — pass (load-bearing here).** All cited files/slugs resolve on-disk. The 26 `L0/*.md`, 26 `meta-reviews/*.md`, 5 `methodology/*.md` directory counts all match exactly. The 4 navigational pages (SUMMARY, introduction, design/index, semantics/index) are precisely the lint's residual OTHER bucket. The 3 kernel-api impl→api edges resolve and are reference-class. No dangling reference found.

**edge-label-fidelity — pass.** The report carries no L_{n+1}→L_n lowering edge label of its own; the kernel-api `realizes-kernel-api` edges it AUDITS are correctly described as `reference`-class (navigational, non-blocking), which I confirmed against frontmatter `kind:` declarations and the `unresolved_depends_on_targets:0` / `rank_violations:0` totals (a mis-typed blocking edge would have surfaced there). The DIRECTIVE-1 sharding edge is correctly described as reference-class. Pass.

**plan-kind-consistency — pass.** Declared shape is audit / consistency-sweep observation (`## Observation kind` = "Audit residue / consistency"). The content matches: hygiene checklist verdicts + a residue scan + a classification, no authoring, no `book/` write. The recommendation correctly scopes the c155/c156 convergence as a bounded `tools/` lint-definition touch + a one-line scheme note (NOT a 61-file authoring campaign), which follows directly from the verified (c)=0 finding. Kind and content are consistent.

**skill-uptake-survey — pass (telemetry).** The report references the `finalization-debulk` skill's A–F residue-class scan (meta-50-codified definitions) for the residue scan, and the graded-stack-lint tool for the tripwire — the relevant procedures for this sweep are named. Surfaced as telemetry; non-blocking.

### Load-bearing verification: the (c)=0 claim + the L0 carve-out

**(c)=0 — CONFIRMED, not refuted.** The claim is that NO untyped node is a real record/operator/theme DAG node missing a rank it should carry. I cross-checked the lint's full `--json` untyped list against the three buckets two ways: (i) every one of the 61 falls into `L0/` (26) / `meta-reviews/` (26) / `methodology/` (5) / navigational (4) — zero residual; (ii) a direct regex filter for any untyped node under `L1/`, `L2/`, `L3/`, `L4/`, or a lowering directory (`*-L*`) returns the EMPTY set. There is genuinely no layered operator, no lowering theme, and no record/concept node among the untyped cohort. Convergence is, as claimed, a pure carve-out refinement with no c156 edge-typing/rank-authoring target.

**(b) L0 carve-out — JUSTIFIED.** All 26 `L0/*.md` files: `grep -lE '^## Status'` → none; `grep -lE '^(rank|firmness|edges):'` → none; `grep -lE 'depends-on'` → none. Sampled H1 forms (`L0/linalg-vector-file` = "# File — `palace/linalg/vector.{hpp,cpp}`"; `L0/eigensolver-wrapper` = "# Class — `EigenvalueSolver` and its wrappers"; `L0/mutable-workspace-pattern` = "# Convention — `mutable` workspace members…"; `L0/par-types-single-rank-reading` = "# Convention — `Par*` types…"; `L0/index` = "# L0 — Cited Palace source ranges + reference notes"). All are file/class/convention/overview ground-truth leaf reference notes — none is a record/operator DAG node. The carve-out is correct: rank (constructive-resolution ordering) is vacuous for the ground-truth evidence floor.

**A–F residue scan — CONFIRMED.** I reproduced the per-class greps with the report's regexes/exclusions: A (`^## Verified-against`) = 0, B (`^verified_against:`) = 0, C (`reports/[0-9]` excl meta-reviews) = 0, D (cycle/c###/batch/wave excl meta-reviews+methodology) = 0, F (`^## Origin|Working Notes|Critic`) = 0. E (dates / `meta-review #N` excl meta-reviews+methodology) resolves to the 2 KEEP files (`SUMMARY.md` TOC date-titles; `semantics/index.md:3` governing-header date-attribution) plus the `concepts/dependency-map.md` date-less `meta-review #N` instance. Note: the date-less `meta-review #N` instance is no longer present in the current working tree because the cycle-154 D2 de-bulk (task #9, completed) has already removed it — the report's E=3 correctly reflects the PRE-D2 sweep state and correctly flags that instance as the in-cycle D2 fix (not a new finding). The duplicate `## Concept:` sub-class in `concepts/constructed-operators.md` is likewise already de-duped in the working tree, consistent with the report's "being-fixed-this-cycle" disposition. The E=3 disposition (2 KEEP + 1 KNOWN D2 target) is correct.

**Hygiene verdicts — SUPPORTED.** Tripwire HELD EXACTLY (totals re-derived, `rank_violations:0`, `unresolved_depends_on_targets:0`). The 3 `realizes-kernel-api` edges are reference-class (frontmatter `kind:` + the zero unresolved-depends/zero rank-violation totals corroborate none is a blocking edge). DIRECTIVE-1 holds (sharding node is `roadmap_goal` with reference-only edges; no firm node depends-on it). Semantic surface §0.1 + governing header intact. Promotion frontier 11 (held). `## Context` count 133 (matches; correctly NOT flagged as F-residue).

### Issues found

None. All 8 checks pass. Every load-bearing claim — the lint baseline, the 61-node partition arithmetic (35+26+0=61), the (c)=0 emptiness, the (b) L0 carve-out justification, the A–F scan, and the hygiene/edge-class/DIRECTIVE-1 verdicts — was reproduced independently on-disk with zero discrepancy. The one apparent mismatch (the `concepts/dependency-map.md` E-instance and the duplicate `## Concept:` block not being present in my live grep) is fully explained and consistent: those are the cycle-154 D2 de-bulks the report flagged as "being fixed this cycle," already applied in the working tree (task #9 completed). This is a clean audit-class report; no repairer pass is required.

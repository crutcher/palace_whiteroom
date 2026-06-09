---
agent: general-purpose
scope: c155-lint-untyped-carveout-convergence
cycle: 155
batch: 51
kind: tooling + methodology-note
integrated_at: 2026-06-09T054250Z
integration_commit: PLACEHOLDER_SHA_CYCLE155
integration_notes: |
  Applied clean (1/1 staging row). THE CONVERGENCE enactment of `p1-edge-typing-true-detritus-sweep`
  (the last finite maintenance item). 2 files committed: tools/graded-stack-lint/graded_stack_lint.py
  (OUTSIDE_DAG_PREFIXES += L0/, meta-reviews/; OUTSIDE_DAG_EXACT = {SUMMARY, introduction,
  semantics/index}; untyped count split out untyped_outside_dag_by_design) + book/src/methodology/
  graded-stack-scheme.md (### The outside-DAG-by-design carve-out note). NEW POST-CONVERGENCE
  BASELINE (deliberate accounted move, NOT a regression): untyped 61→0, untyped_outside_dag_by_design
  61 (new key), expected_unreachable_outside_dag 54→106 (+52 carved-out, 0 genuine-DAG added). HARD
  INVARIANTS + the rest HELD EXACTLY (rank_violations 0, unresolved 0, typed 331, files 392, roots 45,
  promotion_frontier 11, detritus 123, true_detritus 51). None of the 3 step-5b block-conditions
  tripped. cargo make book EXIT 0; step-5c KaTeX + step-5d frontmatter-leak clean. `p1-edge-typing-
  true-detritus-sweep` DISCHARGED; finite maintenance backlog now EMPTY.
---

# Cycle-155 — `untyped` carve-out convergence (the `p1-edge-typing-true-detritus-sweep` enactment)

Bounded `tools/graded-stack-lint` refinement + a reader-facing scheme note. Makes the
linter's `untyped` WARNING reflect the cycle-154 D1 classification (critic-confirmed):
the `untyped=61` warning was DOMINATED by legitimately-untyped-by-design pages, NOT
genuine edge-typing debt. The genuine-untyped DAG-node count is **0** ((c)=0, confirmed).

## Proposed changes

### 1. `tools/graded-stack-lint/graded_stack_lint.py`

- **Extended the outside-DAG prefix carve-out** from `("methodology/", "design/")` to
  `("methodology/", "design/", "L0/", "meta-reviews/")`, with a documenting comment block
  (L0 = ground-truth evidence leaf layer, rank vacuous at the base; meta-reviews =
  historical process records).
- **Added an exact-match set** `OUTSIDE_DAG_EXACT = {"SUMMARY", "introduction",
  "semantics/index"}` for the navigational pages not under an outside-DAG prefix, and wired
  it into `is_likely_outside_dag` (the `*/index` pages were already caught structurally;
  `methodology/`+`design/`+their `/index` were already covered).
- **Split the `untyped` count** in `build_summary`: `untyped_all` (rank-and-edge-less
  nodes) is partitioned into `untyped_outside_dag` (by-design) and `untyped` (genuine
  edge-typing debt = `untyped_all − outside_dag`). The headline `untyped` total now counts
  ONLY genuine debt; the by-design set is reported separately as
  `untyped_outside_dag_by_design` (new total key + new list key in the JSON summary).
- **Updated text rendering**: the header now prints both `untyped (WARNING)` (genuine debt)
  and `untyped outside-DAG` (by design, not debt); `--show-untyped` lists genuine debt and
  separately the outside-DAG-by-design set ("outside-DAG (expected untyped BY DESIGN)") — so
  the carved-out pages stay VISIBLE, not silently dropped; the RESULT line shows
  `N untyped debt (+M outside-DAG by design)`.

**Conservatism / future-debt detection preserved.** The carve-out covers ONLY the
by-design prefix/exact set. It does NOT cover any `L1/`/`L2/`/`L3/`/`L4/`/lowering-theme/
`concepts/`/`feature/`/`synthesis/` node — verified by a probe: a temporary untyped
`L1/probe_future_op.md` surfaces in the genuine `untyped` debt list, while a temporary
`L0/probe_l0_note.md` is classified `untyped_outside_dag_by_design`. A future genuine
untyped operator/theme node still warns.

### 2. `book/src/methodology/graded-stack-scheme.md`

Added a `### The outside-DAG-by-design carve-out (expected-untyped pages)` subsection at the
end of §5 (node-status for un-fronted files). Brief, finalized static-state prose (no process
accounting): documents the four-member by-design set (L0 ground-truth leaf / meta-reviews /
methodology+design / navigational), the rationale (rank is over *constructive* resolution,
vacuous at the L0 base the resolution rests on), and the exactness invariant (does not cover
any DAG-node directory, so a future untyped operator still surfaces as debt).

## Before/after lint accounting (`--book-src book/src --json` totals)

| key | before | after | justification |
|---|---|---|---|
| `untyped` | **61** | **0** | All 61 reclassified as outside-DAG-by-design. (c)=0 genuine-untyped → reaches 0 exactly (no residual). |
| `untyped_outside_dag_by_design` | (new) | **61** | New key == the old 61-untyped set EXACTLY (verified set-equality). |
| `expected_unreachable_outside_dag` | 54 | **106** | +52 (reachability axis). The 61 untyped are all unreachable garbage; 9 were ALREADY counted (the `*/index` + `methodology/`+`design/` cases); the other 52 (25 `L0/` + 25 `meta-reviews/` + 2 nav-exact `SUMMARY`/`introduction`) are newly carved in. 52+9 = 61. ZERO genuine-DAG nodes added (verified). |
| `detritus` | 123 | **123** | UNCHANGED — every `L0/`/`meta-reviews/` node is UNTYPED, and detritus already excludes untyped nodes (`not nodes[s].untyped`); there are 0 TYPED detritus nodes under the new prefixes, so no genuine DAG node moved. |
| `true_detritus` | 51 | **51** | UNCHANGED (no DAG node touched). |
| `detritus_reference_reachable_re11_cohort` | 72 | **72** | UNCHANGED. |
| `detritus_no_typed_edges_pre_p1_artifact` | 104 | **104** | UNCHANGED. |
| `detritus_with_typed_edges_stronger_signal` | 19 | **19** | UNCHANGED. |
| `reachable` | 163 | **163** | UNCHANGED. |
| `reference_reachable` | 247 | **247** | UNCHANGED. |
| `stronger_signal_reference_reachable` | 12 | **12** | UNCHANGED. |
| `stronger_signal_true_detritus` | 7 | **7** | UNCHANGED. |

### Hard invariants — ALL HELD

| invariant | required | after | ok |
|---|---|---|---|
| `rank_violations` | 0 | 0 | ✓ |
| `unresolved_depends_on_targets` | 0 | 0 | ✓ |
| `typed` | 331 | 331 | ✓ |
| `files` | 392 | 392 | ✓ |
| `roots` | 45 | 45 | ✓ |
| `promotion_frontier` | 11 | 11 | ✓ |

Lint exit code: **0** (no rank violations), unchanged. `cargo make book`: **EXIT 0**, no
errors, linkcheck clean, no broken link from the scheme-note edit.

## Convergence statement

The `untyped` debt count is now **0**, reflecting the (c)=0 genuine-untyped finding. The
carve-out is exact and accounted: a DELIBERATE baseline MOVE (61 by-design pages excluded
from the debt warning, fully visible under `--show-untyped` and counted under
`untyped_outside_dag_by_design` + `expected_unreachable_outside_dag`), NOT a hold. No
genuine DAG node was carved out; a future untyped operator/theme would still warn.

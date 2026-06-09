---
verifies: ../CYCLE.md
critiqued_at: 2026-06-09T06:05:00Z
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

# META: verification of cycle-155 `untyped` carve-out convergence (lint tooling + scheme note)

## Critique

This is a TOOLING report (`tools/graded-stack-lint/graded_stack_lint.py`) plus a reader-facing
methodology-scheme note (`book/src/methodology/graded-stack-scheme.md`), NOT a standard
book-content (operator/theme/feature) report. Per the critic role-spec, the 8 book checks
no-op or reduce to mechanical sanity for this shape; the load-bearing verification is the
substance of the lint change, which I re-ran independently (re-ran the tool on both old and
new tool states, read the full diff, ran the probe test, rebuilt the book).

### Checks run

- **citation-validity** — no source-citation claims (no `file:lines` Palace pointers); the
  report's load-bearing assertions are lint TOTALS, which I re-derived directly (below). The
  scheme note carries no citations to range-check. The numeric before/after table is the
  "evidence" and it reproduces exactly. **pass** (mechanically reproduced, not hand-asserted).
- **surface-or-evidence** — not a refinement of an operator/theme surface; no record named in a
  signature (a lint-tool refactor + a prose note). Record-definition sub-check N/A. The change
  modifies tool surface AND carries reproduction evidence. **pass** (N/A to tooling kind, noted).
- **rotation-quality** — no algebraic/structural rotation claim. **pass** (not applicable to a
  tooling + scheme-note report).
- **variant-axis-coverage** — the relevant "variant axis" is *which directories are carved out*;
  the change is exhaustive on that axis (4 prefixes + 3 exact + structural `*/index`) and I
  independently confirmed NO genuine-DAG directory leaks in (probe below). **pass**.
- **cross-reference-integrity** — the scheme note adds one `### …` subsection under §5; no new
  cross-links that could dangle; `cargo make book` EXIT 0 and the note produced no
  render/linkcheck warning of its own. **pass**.
- **edge-label-fidelity** — no L_{n+1}→L_n edge label. **pass** (N/A).
- **plan-kind-consistency** — declared `kind: tooling + methodology-note`; content shape matches
  exactly (a `.py` diff + a `.md` subsection). **pass**.
- **skill-uptake-survey** — no skill is implied for a one-off lint carve-out. **pass** (telemetry
  only, non-blocking).

### Independent substance verification (the load-bearing check)

I re-ran every numeric claim against the tool itself (the diff is applied to the working tree,
uncommitted; I ran the new tool, `git stash`-ed the `.py` to run the OLD tool, then popped).

**1. Carve-out PRECISION — the critical safety property (PASS).**
- The new `untyped_outside_dag_by_design` set (61) **set-equals** the OLD untyped set (61)
  EXACTLY — `new − old = ∅`, `old − new = ∅` (verified by direct set difference). Prefix
  breakdown reconciles to 61: **26 `L0/` + 26 `meta-reviews/` (incl `meta-reviews/index`) +
  5 `methodology/` (incl `methodology/index`) + 1 `design/index` + `SUMMARY` + `introduction`
  + `semantics/index` = 61.** (Note: the task-prompt's reconciliation phrasing lists
  `meta-reviews/index` separately AND inside the 26 — that is a double-count in the *prose*,
  not in the tool; the count itself is correct and lands on 61.)
- **NO genuine DAG node carved out** — independently scanned the 61-member carve-out for any
  `L1/`/`L2/`/`L3/`/`L4/`/`L4-L3/`/`L3-L2/`/`L2-L1/`/`L1-L0/`/`concepts/`/`feature/`/`synthesis/`
  member: **empty** (zero genuine-DAG directories present).
- **PROBE reproduced (the future-debt-still-warns proof).** Created `book/src/L1/__probe_critic.md`
  (untyped, no rank/edges) and `book/src/L0/__probe_critic.md`. Result: the L1 probe surfaced in
  the genuine `untyped` debt list (`untyped: 0→1`, in-debt=True, in-carve-out=False); the L0
  probe was classified outside-DAG-by-design (`untyped_outside_dag_by_design: 61→62`,
  in-debt=False, in-carve-out=True). **Confirms a future genuine untyped operator/theme STILL
  warns.** Both probe files DELETED; working tree re-confirmed clean (no `__probe*` anywhere).

**2. Accounting CORRECT (PASS).** New tool: `untyped: 0`, `untyped_outside_dag_by_design: 61`.
Old tool (stashed `.py`): `untyped: 61`, `expected_unreachable_outside_dag: 54`. New tool:
`expected_unreachable_outside_dag: 106` (**+52**, justified — the 52 newly-carved =
25 `L0/` non-index + 25 `meta-reviews/` non-index + `SUMMARY` + `introduction`; the other 9 of
the 61 were already counted under the old `methodology/`+`design/`+`*/index` rule; 52+9=61, ZERO
genuine-DAG nodes added — reproduced the newly-carved set directly). `detritus: 123→123`
UNCHANGED and `true_detritus: 51→51` UNCHANGED in both tool states (the carved nodes were
already untyped, so already excluded from detritus by `not nodes[s].untyped`; 0 typed-detritus
moved). The full UNCHANGED row set (`detritus_reference_reachable_re11_cohort: 72`,
`detritus_no_typed_edges_pre_p1_artifact: 104`, `detritus_with_typed_edges_stronger_signal: 19`,
`reachable: 163`, `reference_reachable: 247`, `stronger_signal_*`) all confirmed UNCHANGED.

**3. HARD INVARIANTS — ALL HELD (PASS).** Re-ran new tool: `rank_violations: 0`,
`unresolved_depends_on_targets: 0`, `typed: 331`, `files: 392`, `roots: 45`,
`promotion_frontier: 11` — all match the required values exactly. Lint exit code **0**, unchanged
(and the same six invariants held identically in the OLD-tool run, confirming the change touched
only the untyped/reachability reporting, not the rank/edge engine).

**4. Carve-out VISIBLE, not silently dropped (PASS).** `--show-untyped` prints the genuine-debt
section ("UNTYPED files: none …") AND separately the labeled outside-DAG section
("outside-DAG (expected untyped BY DESIGN, 61) …") enumerating all 61. The header prints both
`untyped (WARNING): 0` and `untyped outside-DAG: 61`. The RESULT line reads
"0 untyped debt (+61 outside-DAG by design)". Fully visible.

**5. Scheme note (PASS).** `book/src/methodology/graded-stack-scheme.md` §5 gains
`### The outside-DAG-by-design carve-out` — accurate (L0 = ground-truth evidence leaf with
constructive rank vacuous at the base; the by-design 4-member set; the exactness invariant that
no DAG-node directory is covered so a future untyped operator still warns). Prose is finalized
static-state — no `cycle-NNN`/`cN` attributions, no "this dispatch", no process accounting.
`cargo make book` EXIT 0; the note produced no render/linkcheck warning of its own. (The build
log carries pre-existing KaTeX-render warnings and one linkcheck `hint` in OTHER, untouched files
— `L2/index.md` dep-map tables and `concepts/plane-rotation-stream.md`; `git diff` confirms those
files are NOT touched by this report, so they are background noise, not regressions.)

### Issues found

None. Every load-bearing numeric and the critical carve-out-precision safety property were
reproduced independently from the tool. The single prose imprecision (the task-prompt's 61
reconciliation double-counts `meta-reviews/index`) does not affect the tool's count and is not a
report defect. Clean — all 8 checks `pass`; `overall_status: ready`.

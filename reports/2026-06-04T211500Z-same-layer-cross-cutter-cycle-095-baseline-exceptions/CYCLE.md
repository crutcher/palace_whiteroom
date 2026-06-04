---
agent: same-layer-cross-cutter
invoked_at: 2026-06-04T211500Z
scope: L-cross baseline-exception ledger — GRADED-STACK P1 tracked rank-violation exception set (D7, Wave 3, cycle-095)
status: integrated
integrated_at: 2026-06-04T231500Z
integration_commit: efe6872
integration_notes: "cycle-095 D7 (staging position 7/7). Observation/ledger-only: authored scaffolding/graded-stack-baseline-exceptions.md directly (same-layer-cross-cutter scaffolding/ write authority; 14676 bytes). NO book/ mutation. The ledger's predicted end-state (22 baseline -> 21 discharged c095 -> 1 residual O1) is REALIZED on disk; D7 ran the LANDED-state linter and confirmed exactly 1 rank violation == O1 (solve_family->solve-family-map-dissolution). No NEW OQs (headline read_status_line bug + cites-evidence exemption already promoted by D6/D4). Build-relevant: no."
inputs:
  - reports/2026-06-04T204023Z-cycle-planner-cycle-095/CYCLE.md (D7 scope; the 22-violation partition; the "~8 stale + small genuine residual" estimate)
  - scaffolding/decisions/2026-06-04-graded-stack-p1-edge-home.md (the "bounded tracked baseline-exception set, NOT open-ended fix-forward" mandate)
  - METHODOLOGY-GRADED-STACK.md §5 (audit-first / hard-gate-new / bounded-baseline-exceptions adoption protocol)
  - reports/2026-06-04T210500Z-cross-layer-cross-cutter-cycle-095-vocab-frontier-typing/CYCLE.md (D6 — the violation partition + the read_status_line parse-bug root cause)
  - reports/2026-06-04T210500Z-layer-intro-author-cycle-095-feature-root-closure-typing/CYCLE.md (D5 — the feature-column typing; eigsolve/energy-fields consumer-side discharge)
  - reports/2026-06-04T204500Z-harvester-cycle-095-bilinear-form-firm-flip/CYCLE.md (D1) + reports/2026-06-04T205500Z-lowering-verifier-cycle-095-gram-reduce-rejudgment/CYCLE.md (D3) — the cascade
  - book/src/L4-L3/solve-family-map-dissolution.md (the genuine-residual candidate — verified firm-on-disk this cycle)
  - tools/graded-stack-lint/graded_stack_lint.py:310-380 (read_status_line + derive_rank — the parse-bug mechanism)
---

# CYCLE: L-cross observation — GRADED-STACK P1 baseline rank-violation exception set

## Summary

This is **D7, Wave 3** of cycle-095 (the GRADED-STACK P1 launch + bilinear-form cascade). I authored the campaign's tracked baseline-exception ledger `scaffolding/graded-stack-baseline-exceptions.md` (directly — it is a `scaffolding/` deliverable, not a `book/` mutation; see §Proposed changes for the integrator handoff). It records the 22 c094-baseline rank-linter violations as a **discharge-path burn-down**, partitioned into CLEARED-BY-CASCADE (D1–D4), CLEARED-BY-RETYPING (D5/D6), and TRACKED-OPEN, each with cause + promotion condition per the `partly-constructive` pattern the 2026-06-04 decision + `METHODOLOGY-GRADED-STACK.md` §5 mandate.

**The headline finding (sharpens the planner's partition):** the supposed *one* genuine residual — `L4/solve_family → L4-L3/solve-family-map-dissolution` — is **itself a `read_status_line` false positive**, NOT a maturity gap. Verified on disk: `solve-family-map-dissolution.md:185` §Status **leads with** `` `firm` — on the **structural rotation** ``; the theme is firm-on-structure (since c055-era) and carries no frontmatter rank token, so the linter falls to the prose blob-scan, which trips on a "(former) inherited ... `rough-in (test-coverage-bounded)`" *provenance caveat about the LHS cap* (line 187, within the 5-line blob) — the identical bug D6 root-caused on 11 other edges. So **all 22 baseline violations are either real cascade propagation (now discharged) or `read_status_line` artifacts** — there are **zero genuine rank gaps** in the baseline. The distinction that keeps O1 as TRACKED-OPEN rather than CLEARED: no c095 dispatch *types* the theme (it is an untyped lazy-tail lowering node, outside D5's columns / D6's vocabulary frontier / D1–D4's cascade), so the violation persists at the LANDED state until the incremental rollout reaches it. Its promotion condition is mechanical and low-cost: type the theme `rank: firm` (both endpoints firm on disk → invariant holds immediately).

## Observation kind

**Redundancy** (primary, in the cross-cutter taxonomy sense — two representations of the same fact diverging): the prose `## Status` maturity word and the (absent) typed `rank:` token are a redundant pair, and the prose copy has drifted / is mis-parsed for 12 of the 22 baseline violations. The campaign's typed-token migration coalesces the pair to a single authoritative source. Secondary: **Shared sub-pattern** — 12 of 22 violations share ONE root cause (the `read_status_line` blob-scan token-priority defect), making the linter fix a high-fan-out follow-up that retires the whole false-positive class for the untyped tail.

## Specific finding

The 22 c094-baseline rank violations partition as:

- **10 CLEARED-BY-CASCADE** (C1–C10) — real rank propagation: `bilinear-form` firmed (D1) → `gram_reduce` firmed (D3) → the 4 capacitance/inductance/electrostatic/magnetostatic columns firmed (D4). The `L4/gram_reduce → L1/bilinear-form` edge appears twice in the linter output (C2 is a duplicate-edge artifact, not a distinct violation — collapses on D3's single typed `edges:` block).
- **11 CLEARED-BY-RETYPING** (R1–R11) — stale-edge FALSE POSITIVES. Each dep reads `firm` on disk; the linter mis-derived `rough-in*` via the `read_status_line` blob-scan. D5 (feature columns: boundary-mode.L1, eigenmode.L1, energy-fields.L1/.L4) + D6 (vocabulary frontier: L1/eigsolve, L1/normalize, L2/inner_product, L1/matrix-weighted-norm) type these dep/consumer nodes `rank: firm`, clearing them by construction. (The eigsolve + energy-fields consumer edges are two-sided: D5 re-types the consumer column edge to restate no maturity, D6 types the dep node — either side suffices; both land.)
- **1 TRACKED-OPEN** (O1) — `L4/solve_family → L4-L3/solve-family-map-dissolution`. The planner/D6 candidate-genuine residual; **verified this cycle to be ANOTHER `read_status_line` false positive** (theme firm-leading at `:185`, untyped, blob-scan trips on the LHS-cap provenance caveat at `:187`). Carried OPEN only because no c095 dispatch types it; promotion condition = type `solve-family-map-dissolution rank: firm` (next lazy-tail pass; both endpoints firm so it clears immediately).

**Evidence the genuine-residual is a false positive** (the load-bearing on-disk verification):
- `book/src/L4-L3/solve-family-map-dissolution.md:185` — `` `firm` — on the **structural rotation** `` (leading token = firm).
- No `rank:`/`firmness:`/`status:` frontmatter token on the file → `read_status_line` prose-fallback path (confirmed by grep: only `# solve-family-map-dissolution` heading).
- `:187` — "it was previously status `rough-in (test-coverage-bounded)`" — a resolved-and-flagged provenance caveat about the LHS `solve_family` cap, *inside the 5-line blob* the scan reads.
- `tools/graded-stack-lint/graded_stack_lint.py:310-326` `read_status_line` — `blob = " ".join(lines[i+1:i+6])`, scan order puts `rough-in (test-coverage-bounded)` ahead of `firm` → returns the wrong token (the docstring claims first-line-only; the code blob-scans).

## Recommendation

- **Dispatch the batch-30 meta-phase to fix `read_status_line`** (the shared root cause of 12 of 22 baseline "violations", incl. O1). Match only the leading inline-code token on the first non-empty line after `## Status` (project convention: the maturity word is the leading `` `token` ``), not a 5-line blob scan in resolution-priority order. This retires the false-positive class for the *untyped tail* during the incremental rollout (typed nodes already bypass it). Corroborates D6's flag with a 12th instance (O1) the planner had pegged as genuine.
- **Defer O1 to a c096+ lazy-tail typing pass** (type `solve-family-map-dissolution rank: firm` + `edges: depends-on: [L4/solve_family, L4/ksp_solve, L4-L3/ksp-solve-driver-dissolution]`). Pure edge-typing, NOT a re-judgment — both endpoints firm. Natural home: when the rollout reaches the `L4-L3/` lowering-theme directory, OR a co-scheduled lifter touch.
- **integrator-finalize: run the linter on the LANDED state as the mechanical completion check** — expect exactly 1 residual (O1). MORE than O1 ⇒ a D1–D6 proposed-change did not land (re-check per-report integration); FEWER ⇒ O1 got typed by an unanticipated dispatch (close it). Either way the finalize run confirms the residual against this ledger.
- **Defer (record-only):** the C2 duplicate-edge linter artifact — minor; verify finalize doesn't double-count the collapsed `gram_reduce → bilinear-form` edge after D3's single typed block lands.

## Proposed changes

I authored `scaffolding/graded-stack-baseline-exceptions.md` **directly** (per my role spec's allowance and the dispatch brief: it is a `scaffolding/` deliverable, NOT `book/`; the HARD constraint is no-`book/`-mutation, which I respected). **No `book/` proposed-changes blocks** in this report — D7 is observation/ledger only. The integrator should be aware the ledger file already exists on disk (authored this dispatch); it needs no application step, only awareness for the finalize linter-run cross-check described above. If the integrator prefers the ledger routed through staging rather than direct-authored, the content is the on-disk file verbatim — but per the brief I authored it directly and record that here.

## Supporting evidence

- **Pre-typing baseline linter run** (captured this cycle for the record): `python3 tools/graded-stack-lint/graded_stack_lint.py --json` → `rank_violations = 22` (histogram: firm 158, rough-in 26, partly-constructive 8, obstruction 10, partial-obstruction 4, stub 1). Full list quoted in the ledger; matches D6's + the planner's enumeration exactly.
- **Genuine-residual false-positive verification**: `book/src/L4-L3/solve-family-map-dissolution.md:185` (firm-leading §Status), `:187` (the LHS-cap `rough-in (test-coverage-bounded)` provenance caveat in-blob), frontmatter grep (no rank token). `tools/graded-stack-lint/graded_stack_lint.py:310-326` (`read_status_line` blob-scan source, read this cycle).
- **CLEARED-BY-CASCADE provenance**: D1 (`reports/2026-06-04T204500Z-harvester-cycle-095-bilinear-form-firm-flip/CYCLE.md` — bilinear-form→firm), D3 (`reports/2026-06-04T205500Z-lowering-verifier-cycle-095-gram-reduce-rejudgment/CYCLE.md` — gram_reduce→firm), D4 (`reports/2026-06-04T205500Z-layer-intro-author-cycle-095-four-column-reeval/CYCLE.md` — 4 columns).
- **CLEARED-BY-RETYPING provenance**: D6 (`reports/2026-06-04T210500Z-cross-layer-cross-cutter-cycle-095-vocab-frontier-typing/CYCLE.md` Findings 1+2 — L1/normalize, L2/inner_product, L1/matrix-weighted-norm, L1/eigsolve all firm on disk; the read_status_line root cause) + D5 (`reports/2026-06-04T210500Z-layer-intro-author-cycle-095-feature-root-closure-typing/CYCLE.md` §"Stale-edge audit findings" — L1/eigsolve firm `:165`; boundary-mode.L1/eigenmode.L1/energy-fields.L1/.L4 typed edges read live frontmatter).
- **The authored ledger**: `scaffolding/graded-stack-baseline-exceptions.md` (this dispatch).

## Open questions / caveats

- **CYCLE.md write succeeded (no filter block).** This report wrote cleanly to `reports/<id>/CYCLE.md`; no Claude Code subagent Write-filter block encountered (the canonical CYCLE.md filename worked as intended).
- **O1 is the planner's "genuine residual" downgraded to false-positive.** The planner brief told me to "verify on disk: is `solve-family-map-dissolution` genuinely below firm?" — answer: **no, it is firm** (firm-leading §Status, firm-on-structure since c055-era). It violates only because it is untyped + hit by the `read_status_line` bug. I kept it TRACKED-OPEN (not CLEARED) because no c095 dispatch types it, so it persists at LANDED state — but its promotion condition is mechanical typing, not maturity work. If the batch-30 meta-phase prefers, this could instead be recorded as a 12th CLEARED-BY-RETYPING entry pending a one-line c096 typing touch; I chose TRACKED-OPEN to keep the LANDED-state linter expectation honest (it WILL still report this one until typed).
- **The bounded exception set is effectively empty of real gaps.** This is a strong campaign-thesis confirmation: the c094 baseline had ZERO genuine rank violations — 10 were the not-yet-run cascade, 12 were a single linter parse defect. Surface to batch-30 meta-phase: the typed-`rank:`-as-sole-truth migration + the `read_status_line` fix together drive the baseline-exception set to 0. The "bounded tracked baseline-exception set, NOT open-ended fix-forward" mandate is satisfied with a single mechanical-typing item.
- **Linter-run timing caveat (per the brief).** The 22-violation run above is the PRE-typing state (D1–D6 frontmatter is in proposed-changes, not on disk at my dispatch time). The ledger records the analytically-derived post-typing residual (1 = O1) as the expected end-state and explicitly defers the mechanical confirmation to `integrator-finalize`'s LANDED-state linter run. I did NOT re-run the linter post-typing (the typed changes are not on disk to read).
- **C2 duplicate-edge artifact** — recorded in the ledger as minor; flagged for finalize to confirm the collapsed edge isn't double-counted after D3's single typed `edges:` block lands. Not a rank-semantics issue, a linter-output-dedup issue.
- **Direct-authorship of the ledger** — recorded per the brief so the integrator knows the file is already on disk and needs no application (only the finalize cross-check). This is within `scaffolding/` write authority for a dispatch deliverable; no `book/` was touched.

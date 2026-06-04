# GRADED-STACK baseline rank-violation exception set

**Opened:** cycle-095 (batch-30; GRADED-STACK campaign P1), 2026-06-04, by `same-layer-cross-cutter` (D7, Wave 3).

> **⟢ BURN-DOWN COMPLETE — TRACKED-OPEN-1 (O1) DISCHARGED by cycle-096-D3 (annotated by `integrator-finalize` at the cycle-096 finalize, 2026-06-05).** The one residual tracked exception, **O1 = `L4/solve_family → L4-L3/solve-family-map-dissolution`**, is discharged: cycle-096 D3 (lifter) typed `book/src/L4-L3/solve-family-map-dissolution.md` with `rank: firm` + a typed `edges: depends-on [L4/solve_family, L4/ksp_solve, L4-L3/ksp-solve-driver-dissolution, L3/ksp_solve]` block — exactly O1's promotion condition. All four `depends-on` endpoints read firm on disk, so the invariant `rank(theme=3) ≤ min(deps=3)` holds. **The `integrator-finalize` LANDED-state linter run confirms `rank_violations: 0`** (was the expected 1 at c095; cycle-096 cleared it). Additionally, cycle-096 D4 fixed the `read_status_line` prose-fallback parse bug (the root cause of the false-positive class documented below), so even as-yet-untyped tail nodes no longer generate these false positives. **The bounded exception set has burned down to 0 tracked.** This ledger is now a CLOSED historical record of the c094→c096 burn-down; no open tracked exceptions remain. (Per the append-only OQ-ledger discipline, the per-report close-notes in `scaffolding/open-questions.md` are left for the meta-phase to unify; this banner is the finalize cycle-end housekeeping touch.)

**Authority:** the 2026-06-04 user decision `scaffolding/decisions/2026-06-04-graded-stack-p1-edge-home.md` + `METHODOLOGY-GRADED-STACK.md` §5 step-3/4 — "Genuinely-large remediations: enumerate as an **explicit, tracked baseline-exception set with promotion conditions** (the same first-class-transient-gate pattern as `partly-constructive`) — **not** open-ended fix-forward." The rank invariant is a HARD gate for NEW work as of c095; pre-existing violations live HERE with promotion conditions and burn down.

**What this ledger is.** A discharge-path record for the rank-linter (`tools/graded-stack-lint/graded_stack_lint.py`) violations that existed at the c094-finalize baseline (22 of them). It distinguishes three categories so it reads as a burn-down, not a violation dump:
- **CLEARED-BY-CASCADE** — discharged by the c095 bilinear-form→gram_reduce→4-column cascade (D1–D4). Real rank propagation up the DAG; the invariant now holds for these edges.
- **CLEARED-BY-RETYPING** — *stale-edge FALSE POSITIVES*, not real rank gaps. They were artifacts of the linter's `read_status_line` prose fallback (the parse bug below); typing the dep node with an explicit `rank:` token retires them by construction (the typed token wins over the buggy fallback in `derive_rank`).
- **TRACKED-OPEN** — the genuinely-residual exception(s) carried forward with a promotion condition.

**Mechanical completion check (the campaign's audit-first end-state).** The D1–D6 typed frontmatter is in proposed-changes at the time this ledger was authored — it lands at cycle-end. So a linter run BEFORE integration shows the PRE-typing state (the full 22). **`integrator-finalize` runs the linter on the LANDED state** to confirm the residual is exactly the TRACKED-OPEN set below. The analytically-derived post-typing residual (this ledger's expected end-state) is **1** violation — and that one is itself a deferred-typing artifact (see TRACKED-OPEN-1), not a maturity gap.

---

## Context — the `read_status_line` token-priority parse bug (why 12 of the 22 were never real)

`graded-stack-lint-read-status-line-token-priority-bug` (D6 root-caused; flagged for the batch-30 meta-phase). When a DAG node carries no explicit `rank:`/`firmness:`/`status:` frontmatter token, the linter derives its rank from the prose `## Status` section via `read_status_line` (`tools/graded-stack-lint/graded_stack_lint.py:310-326`). That function:

```python
blob = " ".join(lines[i + 1 : i + 6]).lower()       # joins the 5 lines after `## Status` into one blob
for tok in ("partly-constructive", "rough-in (test-coverage-bounded)",
            "rough-in", "roadmap_goal", "obstruction",
            "partial-obstruction", "stub", "firm"):  # `rough-in*` scanned BEFORE `firm`
    if tok in blob:
        return tok
```

It scans a 5-line blob in token-priority order with `rough-in` / `rough-in (test-coverage-bounded)` ahead of `firm`. So any §Status paragraph that **leads with `firm`** but **mentions "rough-in" within 5 lines** — a provenance phrase ("promoted from rough-in"), a disclaimer ("the rough-in framing does not bind"), a sibling note ("an in-chapter rough-in note"), or a "(former) inherited ... `rough-in (test-coverage-bounded)`" caveat — is mis-read as `rough-in`. The node is firm on disk; the linter never reaches the leading `firm` token. (The function's own docstring claims it reads "the first non-empty line" — the implementation does not; it blob-scans.)

**This is the prose `## Status` second-source-of-truth drift the campaign exists to remove.** The fix the campaign installs is exactly the typed `rank:` token: `derive_rank` (`:328-380`) prioritizes an explicit `rank:` token OVER the prose fallback, so a typed dep node bypasses the buggy scan entirely. Every CLEARED-BY-RETYPING entry below is a node whose §Status is firm-leading but trips this scan; the D5/D6 typed `rank: firm` frontmatter clears it. Recommended linter fix (batch-30 meta-phase): match only the leading inline-code token on the first non-empty line after `## Status` (the project convention is the maturity word is the leading `` `token` ``), not a blob scan in resolution-priority order.

**Pre-typing baseline run (for the record):** `python3 tools/graded-stack-lint/graded_stack_lint.py --json` at c095 dispatch time reports `rank_violations = 22` (histogram: firm 158, rough-in 26, partly-constructive 8, obstruction 10, partial-obstruction 4, stub 1). The 22 are partitioned below.

---

## CLEARED-BY-CASCADE (10) — discharged this cycle by the bilinear-form firm-flip-and-cascade-wave (D1–D4)

Real rank propagation: `bilinear-form` firmed (D1) → `gram_reduce` firmed (D3) → the 4 output-product/driver columns firmed (D4). Each edge's `dep_rank` rises to `firm`, so `rank(src) ≤ rank(dep)` now holds.

| # | violating edge (`src → dep`) | baseline gap | cause | discharged by |
|---|---|---|---|---|
| C1 | `L4/gram_reduce → L1/bilinear-form` | firm-tcb (2.5) on rough-in (2) | `bilinear-form` was rough-in | D1 (firm-flip bilinear-form) + D3 (firm-flip gram_reduce) |
| C2 | `L4/gram_reduce → L1/bilinear-form` *(dup edge)* | same | linter emits the edge twice (dep declared in two frontmatter buckets) | D1 + D3 |
| C3 | `feature/capacitance.L0 → feature/capacitance.L1` | firm (3) on rough-in-tcb (2.5) | capacitance.L1 was seed/rough-in pending its bilinear-form readout | D4 (column flip) |
| C4 | `feature/capacitance.L1 → L1/bilinear-form` | rough-in-tcb (2.5) on rough-in (2) | `bilinear-form` was rough-in | D1 + D4 |
| C5 | `feature/electrostatic.L0 → feature/electrostatic.L1` | firm on rough-in-tcb | electrostatic.L1 was seed pending readout | D4 |
| C6 | `feature/electrostatic.L1 → L1/bilinear-form` | rough-in-tcb on rough-in | `bilinear-form` rough-in | D1 + D4 |
| C7 | `feature/inductance.L0 → feature/inductance.L1` | firm on rough-in-tcb | inductance.L1 seed pending readout | D4 |
| C8 | `feature/inductance.L1 → L1/bilinear-form` | rough-in-tcb on rough-in | `bilinear-form` rough-in | D1 + D4 |
| C9 | `feature/magnetostatic.L0 → feature/magnetostatic.L1` | firm on rough-in-tcb | magnetostatic.L1 seed pending readout | D4 |
| C10 | `feature/magnetostatic.L1 → L1/bilinear-form` | rough-in-tcb on rough-in | `bilinear-form` rough-in | D1 + D4 |

> Note on C2: the duplicate `gram_reduce → bilinear-form` edge is a linter artifact (the dep appears in two frontmatter buckets / is re-emitted), not two distinct violations. After D3's typed single `edges: depends-on:` block lands, the duplicate collapses. Flagged as minor for the batch-30 meta-phase alongside the parse bug.

## CLEARED-BY-RETYPING (11) — stale-edge FALSE POSITIVES; the dep is firm on disk; D5/D6 typed-token migration retires them

These are NOT real rank gaps. Each `dep` reads `firm` in its own `## Status`; the linter mis-derived a `rough-in*` rank via the `read_status_line` blob-scan bug above. The D5 (feature columns) / D6 (vocabulary frontier) typed `rank: firm` frontmatter clears each by construction (the typed token bypasses the prose fallback). Recorded as the campaign's audit-first validation: the prose `## Status` is a drifting second source-of-truth; these are linter-fallback artifacts, not exceptions.

| # | violating edge (`src → dep`) | dep's ACTUAL §Status on disk | blob-scan trap phrase | discharged by |
|---|---|---|---|---|
| R1 | `L2/eigsolve → L1/eigsolve` | **firm** (`L1/eigsolve.md:165/167`, c022) | "promoted from `rough-in (test-coverage-bounded)`" (provenance) | D6 (type `L1/eigsolve rank: firm`) |
| R2 | `feature/boundary-mode.L1 → L1/eigsolve` | **firm** | same | D5 (typed col edge reads live frontmatter) + D6 (dep type) |
| R3 | `feature/eigenmode.L1 → L1/eigsolve` | **firm** | same | D5 + D6 |
| R4 | `L2/normalize → L1/normalize` | **firm** (`L1/normalize.md:99`) | "the `eigsolve` rough-in framing does not bind"; "`normalize_B` ... in-chapter **rough-in note**" | D6 (type `L1/normalize rank: firm`) |
| R5 | `L3/normalize → L1/normalize` | **firm** | same | D6 |
| R6 | `L2/nrm2 → L2/inner_product` | **firm** (`L2/inner_product.md:449`) | "a reduce-to-scalar fold over three firm/rough-in L1 leaves" (FIRST line) | D6 (type `L2/inner_product rank: firm`) |
| R7 | `L3/dot → L2/inner_product` | **firm** | same | D6 |
| R8 | `L3/inner_product → L2/inner_product` | **firm** | same | D6 |
| R9 | `L4/domain_energy_reduce → L1/matrix-weighted-norm` | **firm** (`L1/matrix-weighted-norm.md:110`, c091) | "promoted from `rough-in (test-coverage-bounded)`" (provenance) | D6 (type `L1/matrix-weighted-norm rank: firm`) |
| R10 | `feature/energy-fields.L1 → L1/matrix-weighted-norm` | **firm** | same | D5 (typed col edge) + D6 (dep type) |
| R11 | `feature/energy-fields.L4 → L1/matrix-weighted-norm` | **firm** | same | D5 + D6 |

> Verification provenance: dep-side firmness verified on disk this cycle by D5 (`L1/eigsolve` firm — report §"Stale-edge audit findings") and D6 (`L1/normalize`, `L2/inner_product`, `L1/matrix-weighted-norm` all firm — report Findings 1+2). The discharge for R2/R3/R10/R11 is two-sided: D5 re-types the consumer feature-column edge to restate no maturity (so it reads the dep's own frontmatter), and D6 types the dep node firm.

## TRACKED-OPEN (1) — the residual exception carried forward

| # | violating edge (`src → dep`) | linter-reported gap | TRUE disposition | promotion condition |
|---|---|---|---|---|
| **O1** | `L4/solve_family → L4-L3/solve-family-map-dissolution` | firm (3) on rough-in-tcb (2.5) | **stale-edge false positive — but NOT cleared this cycle (the dep theme is untyped tail)** | type `L4-L3/solve-family-map-dissolution` with `rank: firm` |

**O1 analysis (the discovery — sharpens the planner/D6 partition).** The planner and D6 routed `solve_family → solve-family-map-dissolution` to D7 as the candidate "genuine residual" (firm L4 endpoint over a `rough-in (test-coverage-bounded)` theme). **Verified on disk this cycle with the leading-token rule D6 prescribed: it is ALSO a `read_status_line` false positive, NOT a genuine maturity gap.**

- `book/src/L4-L3/solve-family-map-dissolution.md:185` §Status **leads with** `` `firm` — on the **structural rotation** `` (firm since c055-era; the theme asserts a structural identity on the map-shell syntax read off positive source, and it is firm-on-structure independent of any LHS test-coverage question).
- The theme carries **no** `rank:`/`firmness:`/`status:` frontmatter token (`# heading` only) → it is on the `read_status_line` prose fallback.
- Within the 5-line §Status blob, line 187 contains "it was previously status `rough-in (test-coverage-bounded)`" — a *provenance caveat about the LHS cap* (which firmed c086), explicitly framed as "(former) inherited" and resolved. The blob-scan returns `rough-in (test-coverage-bounded)` (the higher-priority token) before reaching the leading `firm`. Identical mechanism to R1–R11.

**Why it is TRACKED-OPEN and not CLEARED-BY-RETYPING:** unlike R1–R11, no c095 dispatch types this node. It is a **lowering theme**, not a vocabulary-frontier leaf (D6's scope) nor a feature column (D5's scope) nor a cascade node (D1–D4). The frontier-first incremental rollout (per the 2026-06-04 decision: "the long tail is lazy — typed as cycles touch those nodes") simply has not reached it. So at the LANDED c095 state, the violation **persists** (the dep is still prose-fallback). It is the one residual the `integrator-finalize` linter run is expected to still report.

**Promotion condition (mechanical, low-cost):** type `book/src/L4-L3/solve-family-map-dissolution.md` with `rank: firm` + a typed `edges:` block (`depends-on: L4/solve_family`, `L4/ksp_solve`, `L4-L3/ksp-solve-driver-dissolution`; per §5 a lowering theme's edge is `depends-on` on both endpoints). On disk both endpoints are firm (`solve_family` c086, `ksp_solve` firm), so the typed `rank: firm` satisfies the invariant immediately and clears O1 by construction — exactly as R1–R11 cleared. This is a **next-cycle lazy-tail typing item** (no maturity work, no re-judgment — pure edge-typing), NOT an open-ended fix-forward and NOT a real rank gap. Suggested home: a c096 lifter/layer-intro-author lazy-tail typing pass, OR fold into the broader L4-L3 theme-typing sub-campaign when the rollout reaches the lowering directories.

> **Discharge note for the meta-phase:** O1 is evidence FOR the campaign thesis, not against it — it is the SAME prose-fallback drift as R1–R11, just on an as-yet-untyped node. It confirms there are **zero genuine rank gaps** in the c094 baseline (every one of the 22 is either real cascade propagation now discharged, or a `read_status_line` false positive). The bounded exception set is therefore **1 deferred-typing artifact**, burning down to 0 the moment the lazy tail reaches the L4-L3 themes. Once the `read_status_line` bug is fixed (batch-30), even untyped tail nodes stop generating these false positives.

---

## Burn-down summary

| category | count | status |
|---|---|---|
| CLEARED-BY-CASCADE | 10 | discharged this cycle (D1–D4) |
| CLEARED-BY-RETYPING | 11 | discharged c095 (D5+D6 typed frontmatter) |
| TRACKED-OPEN | 1 | O1 — **DISCHARGED c096-D3** (typed `solve-family-map-dissolution` `rank: firm`); was a deferred-typing artifact |
| **baseline total** | **22** | **21 discharged c095; 1 discharged c096; 0 tracked remaining — BURN-DOWN COMPLETE** |

**`integrator-finalize` LANDED-state linter result (c095 → c096):** at c095 finalize the run reported exactly 1 rank violation (O1), matching the prediction. At **c096 finalize the run reports `rank_violations: 0`** — O1 was typed by c096-D3 (the anticipated lazy-tail typing dispatch), so the residual closed exactly as the c095 ledger's "if it reports FEWER, O1 was typed by an unanticipated/next dispatch (close O1)" branch predicted. The c094→c096 burn-down (22 → 21 → 0) is complete; the typed subset is clean.

**Open dependencies for next batch (meta-phase intake):**
- `graded-stack-lint-read-status-line-token-priority-bug` — fix the blob-scan (leading-token-only). Retires the false-positive class for the untyped tail during the incremental rollout. (D6-flagged; this ledger is corroborating evidence — 12 of 22 baseline "violations" were this bug, incl. O1.)
- C2 duplicate-edge linter artifact — minor; collapses on D3's single typed `edges:` block, but verify finalize doesn't double-count.
- O1 lazy-tail typing — type `solve-family-map-dissolution rank: firm` next time a cycle touches the L4-L3 theme directory.

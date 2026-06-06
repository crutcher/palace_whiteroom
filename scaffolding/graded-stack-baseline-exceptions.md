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

---

# REACHABILITY baseline-exception set (Axis-2) — opened batch-35 meta-phase (cycle-111)

**Opened:** cycle-111 (batch-35 meta-phase, post-cycle-111 finalize), 2026-06-06, by `meta-phase`.

> **A DISTINCT KIND from the rank-violation set above.** The §above set tracks **Axis-1 (rank/well-foundedness)** violations (now burned down to 0). This set tracks **Axis-2 (reachability/liveness)** exceptions: firm, faithful, correctly-typed nodes that are **unreachable from any feature root** AND for which **no faithful `depends-on` edge exists** to ground them (the §2f GROUND disposition has been ruled out as unfaithful). These are NOT garbage-to-delete — they are real, firm dissections that are *absorbed below the column* or are *currently-unconsumed iteration-views*, correctly off the reachability spine. Per `METHODOLOGY-GRADED-STACK.md` §2f priority order (GROUND → ROUTE-as-detritus → DELETE/baseline-exception), this is the third disposition, applied only after GROUND is ruled out as unfaithful. The precedent shape was set by the c107 BC/divfree clusters (which were GROUNDED, not baseline-excepted, because a faithful edge existed) — these entries are the cases where the faithful edge does NOT exist.

**Authority:** `METHODOLOGY-GRADED-STACK.md` §2f (GROUND-don't-remove, the priority order) + §5 step-3/4 (bounded tracked baseline-exception set with promotion conditions, not open-ended fix-forward). Each entry is the legitimate faithful-path-or-finding outcome routed by cycles 109/110/111 and dispositioned by this meta-phase.

**Disposition family (all the same "absorbed-below-column / firm-but-unconsumed iteration-view" pattern, the c107 BC/divfree absorbed-cluster shape where no faithful edge exists):**

| # | unreachable node(s) | why no faithful column→node edge exists | TRUE disposition | promotion condition |
|---|---|---|---|---|
| RE1 | `L4/chebyshev`, `L3/chebyshev`, `L2/chebyshev-iteration`, `L2/jacobi-smoother`, `L4/preconditioning-framework`, `L2-L1/chebyshev-iteration-fusion` | the preconditioner is **absorbed into the constructed `op.T` = A·M⁻¹** (`L4/ksp_solve.md:26`; `L2/krylov-step.md:57`); the kernel folds `apply_linop op.T`, never naming a concrete chebyshev/jacobi preconditioner as a separable composed verb. The dependency DIRECTION is reversed: `L4/preconditioning-framework` *consumes* `L4/ksp_solve`. Forcing `ksp_solve → preconditioning-framework` would INVERT the real consumer→producer direction (the c108 over-edge catch). | **baseline-exception** — firm preconditioner/smoother vocabulary absorbed into the constructed `op.T`, correctly off the reachability spine. | a future driver/feature column that names a concrete preconditioner as a *separable composed verb* via a faithful `depends-on` path (e.g. a preconditioner-construction feature surface), OR a demand-gated dispatch that surfaces a genuine constituent edge. (OQ `chebyshev-jacobi-preconditioner-leg-absorbed-below-column-baseline-exception`.) |
| RE2 | `L3/orthogonalize` (`partial-obstruction`, c019/c022), `L3-L2/orthogonalize-variant-split` | no faithful reachable depender: the reachability edge runs `L2/orthogonalize ← L3/orthogonalize` (L3 depends-on L2), so grounding `L2/orthogonalize` (done c111) does NOT carry liveness UP to `L3/orthogonalize`. The only root-reachable consumer `L4/krylov-step` **deliberately composes `L2/orthogonalize` DIRECTLY** (no L4 orthogonalize op; the L4→L2 composition is the documented chain). Forcing `L4/krylov-step → L3/orthogonalize` would assert a constituent-use that does not exist (krylov-step composes the L2 surface, not the L3 iteration-view). | **baseline-exception** — the L3 iteration-view (MGS `partial-obstruction` + CGS/CGS2 global-tensor-field lifts) is a real-but-currently-unconsumed dissection: faithful, firm, but no live depender. | a future driver/feature column that composes the L3 (rather than L2) orthogonalize iteration-structural surface (e.g. an eigenmode-ROM basis-extension column naming the iteration-structural L3 form), via a *faithful* future column edge — NOT a forced edge. (OQ `l3-orthogonalize-sub-chain-no-faithful-reachable-depender`.) |
| RE3 | `L2/gram`, `L2-L1/gram-fold-specialization` | `L2/gram` (the all-pairs `XᴴX` over a basis — NLEPS, distinct from `L4/gram_reduce`) is consumed ONLY by `deflate` (`L2/gram.md:25-26`), which is on the STOP-PROPOSING demand-gated FRONTIER list. The c110 D1 decline confirmed `gram_reduce → L4/inner_product` is a SIBLING `reference` not a `composes` edge (critic-verified); `gram_reduce` itself IS reachable. `L2/gram` reaches root only via the gated `deflate`. | **baseline-exception** — correctly garbage until `deflate` is demand-gated on. | `deflate` is demand-gated on (a downstream NLEPS/deflation consumer surfaces), at which point `L2/gram` grounds via the faithful `deflate → L2/gram` edge automatically. (OQ `gram-reduce-inner-product-is-sibling-not-composes-edge-declined`.) |
| RE4 | `L2/incremental-least-squares`, `L2-L1/incremental-least-squares-composition-lowering` | the GMRES running-QR / Givens stream IS a genuine GMRES constituent, but at the L4 chapter altitude it is **absorbed into the krylov-step body** (the LS-residual is a `StepOutputs` derived view, `L4/krylov-step.md:104`) + the `ksp_solve materialise_iterate` tail. There is no separable L4-level `incremental-least-squares` op to point a `composes` edge at; grounding faithfully would require either an L4 op (over-structure for an absorbed derived view) or an altitude-inconsistent `L4/krylov-step → L2/incremental-least-squares` edge (derived-view byproduct, not a folded constituent). | **baseline-exception** — absorbed-below-column derived view, like the preconditioner leg. | a future L2-altitude grounding when the GMRES variant is exercised (a feature/driver column that composes the running-QR stream as a named constituent), via a faithful path. (OQ `gram-reduce-inner-product-is-sibling-not-composes-edge-declined`, the ILS-routed sub-finding.) |
| RE5 | `L3/normalize`, `L3/reciprocal`, `L2/normalize`, `L2/reciprocal`, `L2/nrm2` (the normalize/reciprocal/scal internal-utility chain) | these L2/L3 element-local utility views are firm-on-positive-structure (`L3/normalize.md:129`, `L3/reciprocal.md:127`, `L2/normalize.md:137`) but consumed only by other off-spine internal utilities: `reciprocal` ← jacobi/chebyshev (the RE1 preconditioner leg) + bilinearform; `normalize` ← (the eigsolve/basis-normalization absorbed into the solve body); `L2/nrm2 ← L2/normalize` only (both off-spine). No driver/feature column reaches them via a live `depends-on` path that is not itself in RE1/RE2. | **baseline-exception** — firm internal-utility iteration-views absorbed below the reachable spine (the normalize/reciprocal chain rides the preconditioner + basis-normalization legs, themselves absorbed). | grounding of the consuming leg (RE1 preconditioner leg, or a future basis-normalization feature surface) carries liveness down into this chain automatically via the existing faithful `depends-on` edges; no edit to these nodes needed — they ground transitively when their consumer grounds. (OQ `l3-orthogonalize-sub-chain-no-faithful-reachable-depender`, the normalize/reciprocal-bundled call.) |

**Burn-down note.** Every RE entry has a concrete, non-fix-forward promotion condition: a *future faithful edge* (RE1/RE2/RE4 — a feature column that genuinely names the absorbed verb as a constituent) or a *demand-gate trigger* (RE3 — `deflate`) or *transitive grounding of the consuming leg* (RE5). None is open-ended. The reachability GC will continue to mark these as `STRONGER GARBAGE SIGNAL` members; this ledger is the explicit record that they are TRACKED-BASELINE-EXCEPTION, not unexamined detritus. The `STRONGER GARBAGE SIGNAL` count at batch-35 close is **26** — these 5 cohorts (≈14 nodes) are the dominant ratified subset of that 26; the remainder is the lazy-untyped tail + demand-gated frontier (`deflate`/`deflate-composition-lowering`).

**Re-open / escalate:** if a node in this set is forced reachable by an UNFAITHFUL edge (a critic-missed `depends-on` that asserts a non-existent constituent-use relationship), re-open — the §2f faithful-edge-or-finding guard failed. If the `STRONGER GARBAGE SIGNAL` count CLIMBS without a new ratified RE entry (new typed-but-unreachable nodes accreting), that is a signal a grounding pass was skipped — investigate at the next batch.

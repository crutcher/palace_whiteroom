---
agent: cycle-planner
invoked_at: 2026-06-07T182605Z
scope: cycle-130 dispatch plan
status: pending
---

# Cycle 130 dispatch plan

## Goals selected this cycle

c130 is the FIRST primary cycle of meta-batch-42 (cycles 130/131/132; batch-42 meta fires AFTER c132 finalize). The batch-42 forward direction is RESOLVED (human decision 2026-06-07): the **§1.2.2 / closure-signature POLISH PASS** (memory `project_batch42_direction_polish_pass`). This cycle OPENS the LEAD — bounded consolidation of the EXISTING calculus surface to fully-consistent (the redirect's no-forced-rectangular-pull-up still governs; this is NOT a new-vocabulary frontier). A tight 3-dispatch slate: D1 [LEAD] authors the §1.3 BNF `op-with-params` introducer promotion + pins the §1.2.2 cohort-sweep ruling (the scope-gate); D2 runs the actual whole-book §1.2.2 compliance-cohort sweep over the residual calculus-level opaque `LinearOperator[…]` codomains; D3 is an opportunistic MAINTENANCE-FLOOR hygiene pick (the inner-product anchor-stability count-owner sweep). NO RE fires; the linter baseline is HELD by design (no maturity/rank/edge change).

## Dispatches

### D1 [LEAD] — `layer-intro-author` — semantic-surface §1.3 BNF `op-with-params` promotion + §1.2.2 cohort-sweep RULING — WAVE-1 — deps: none
- **scope**: On `book/src/semantics/index.md`: (a) decide + (if go) add the `op-with-params { p₁ = e₁, … ; λ(x: τ_in). e_body } : Op[τ_in → τ_out]` introducer production to the §1.3 `e ::=` BNF block (`:106-127`) to match the existing §3.5 `apply A e` eliminator — the §1.3.1 prose form (`:163`) is already settled; this promotes the *introduction* form into the grammar (mind the strawman BNF-renumbering the c128 D1 deliberately deferred). (b) Pin the §1.2.2 cohort-sweep RULING D2 consumes: **calculus-level (L4/L3) operator-VALUE codomains in a signature / theme-LHS position** carry the higher-order intent → convert to bracketed `LinOp[(N: ...), $N]` / `Op[…]`; **plain operator-VALUE rank-1 record fields** where N is a genuine flat-dof vector length (the c129 D2 deliberate dual-spelling — `assemble_frequency_operator.md:103-105` `K/C/M`; `divfree-projector` `P.M/P.WeakDiv/P.Grad`; the explicit L1-realization prose in `fe_assemble.md`/`assemble-diagonal.md`) STAY rank-1 per §1.2.2:95 ("at L1/L0 … keep it there"). Prose/BNF only; NO L4-chapter edits. Append the OQ resolution marker for `closure-signature-op-with-params-bnf-promotion` (header-close = meta unify-authority).
- **deps**: none
- **rationale**: The migrated LOW item `closure-signature-op-with-params-bnf-promotion` (priorities item-3) + the scope-gate for D2's compliance-cohort sweep. The semantic surface is `layer-intro-author`-owned (semantic-consolidation discipline). fan-out: MEDIUM (the scope-gate + completes the §1.3.1 BNF rollout). Plan-tag `semantic-consolidation`.

### D2 — `lifter` — whole-book §1.2.2 closure-signature compliance-cohort sweep — WAVE-2 — deps: D1
- **scope**: Reading D1's pinned §1.2.2 ruling, convert the residual calculus-level opaque `LinearOperator[…]` codomains to the bracketed form (USE+LINK §1.2.2/§1.3.1, don't restate the convention): **dissolution-theme LHS** — `book/src/L4-L3/fe-assemble-fold-dissolution.md:30` (`fe_assemble ::`) + `:37` (`assemble_term ::`), both `LinearOperator[N, N]` → `LinOp[(N: ...), $N]`; `book/src/L4-L3/mk-matrix-free-operator-dissolution.md:151` (`mk_matrix_free_operator_L3 ::` codomain `LinearOperator[(N: ...)]` → `LinOp[(N: ...)]`/`Op[…]` per D1's pin). **L4-chapter residual** — `book/src/L4/fe_assemble.md:77` (the `result —` shape-contract line, codomain to match the now-bracketed `:60` signature) + `book/src/L4/frequency_sweep.md:151` (`op_w = … : LinearOperator[N, N]` calculus-level codomain annotation). JUDGE-and-KEEP per D1's ruling the rank-1 record fields. On-disk RE-LOCALIZE each cited line before editing (OQ line numbers have DRIFTED before). Prose/signature FIDELITY — NO status/rank/edge/node-maturity change.
- **deps**: D1 (informational — reads D1's §1.2.2 keep/convert ruling for the per-site decision)
- **rationale**: The LEAD's actual sweep work — `closure-signature-l4-constructor-restatement-compliance-cohort-sweep` + the migrated `closure-signature-residual-compliance-sweep` (priorities items LEAD + 2). fan-out: LOW-MEDIUM (fully-consistent calculus surface; completes the residual cohort). Plan-tag `semantic-consolidation`.

### D3 — `layer-intro-author` — `inner-product-combinator-section-anchor-stability` count-owner sweep — WAVE-1 — deps: none
- **scope**: Shorten the 2 long `inner_product` §-anchors (`book/src/L3/inner_product.md:146` "## Specializations (the members, as notes under the combinator)" → e.g. "## Specializations"; `:334` "## Consumer (NOT an instance): nrm2 / matrix-weighted-norm" → e.g. "## Consumer: nrm2") AND re-point the ~59 inbound `inner_product.md#…` links in ONE count-owner pass (latent-build-fragility retirement — ~30+ inbound depend on the verbatim long anchors). D3 SOLE-OWNS the anchor-shorten + re-point. Prose/anchor FIDELITY — NO status/rank/edge change.
- **deps**: none
- **rationale**: MAINTENANCE FLOOR item-4 (`inner-product-combinator-section-anchor-stability`) — an opportunistic latent-fragility hygiene pick bundled into the polish-pass cycle's spare budget. fan-out: LOW (anchor-stability hygiene). Plan-tag `index-count-hygiene`.

## Overlap analysis

- **D1 ↔ D2**: D2 depends on D1 INFORMATIONALLY (reads D1's pinned §1.2.2 ruling for the per-site keep/convert decision and the canonical bracketed spelling). DISJOINT files — D1 edits ONLY `semantics/index.md`; D2 edits `fe-assemble-fold-dissolution.md`, `mk-matrix-free-operator-dissolution.md`, `fe_assemble.md`, `frequency_sweep.md`. No shared region → sequential by dependency, not by region conflict. **WAVE-2 for D2.**
- **D1 ↔ D3**: both are `layer-intro-author`, but DISJOINT files — D1 = `semantics/index.md`; D3 = `L3/inner_product.md` + the ~59 inbound link files. Verified `semantics/index.md` is NOT among D3's inbound link files (the long inner_product anchors are referenced from L2/L3/L4 chapters, not the semantic surface). → **PARALLEL-safe (both WAVE-1).**
- **D2 ↔ D3**: DISJOINT files. Verified (grep) that NONE of D2's 4 files link the shortened `inner_product` anchors (`#specializations`/`#consumer`) → no cross-report anchor-rename premise inversion. → PARALLEL-safe (D2 is WAVE-2 only because of the D1 dependency, not D3).
- **Consolidated-tally / shared-index collisions**: NONE. No firm-count moves this cycle (pure spelling/anchor fidelity — no status/maturity change). No `feature/index.md` or layer-`index.md` consolidated-tally write. No floor-landing → adjacent-entry re-anchor coupling. No cross-report forward-reference to a not-yet-existing slug (D2 cites on-disk §1.2.2 + the already-swept `fe_assemble.md:60` exemplar; D1 authors no new slug D2/D3 reference).

## Sequencing schedule

- **WAVE-1 (parallel):** D1 [LEAD] (semantic-surface BNF + ruling) ‖ D3 (inner_product anchor sweep).
- **WAVE-2 (after WAVE-1 reports land):** D2 (the cohort sweep, dep D1 — reads D1's §1.2.2 ruling).
- Then: 3 critics (parallel) → repairers (as needed) → `integrator-per-report` ×3 (serial) → ONE `integrator-finalize`.

## Deliverable-presence verification

Paste-inline evidence per the MANDATORY pre-dispatch check (every dispatch resolves to named `book/src/` paths; all are EXISTING-file consolidation edits, not new slugs).

**D1 (semantics/index.md — BNF + ruling):**
1. File existence: `ls book/src/semantics/index.md` → present (surface exists).
2. Maturity / already-discharged: the §1.3 `e ::=` block (`:103-130`) currently has the `apply A e` ELIMINATOR but NO `op-with-params {…}` INTRODUCER production (verified by reading `:106-127`); `grep -c "op-with-params" book/src/semantics/index.md` = 4 (all in §1.3.1 PROSE + the §3.5 reduction + the resolved-note — none in the §1.3 `e ::=` grammar). The BNF-promotion is genuinely OPEN.
3. OQ-ledger RESOLVED-grep: `closure-signature-introduction-form-into-bnf-and-role-discipline-bullet` is SPLIT — the role-bullet half ENACTED batch-41 meta, the BNF-promotion half MIGRATED to the plan (open). NOT resolved.
4. Structural-block: none — semantic-surface authoring is `layer-intro-author`-owned, no gate blocks. OPEN.

**D2 (the cohort sweep — residual opaque codomains):**
1. File existence: all 4 targets present (`fe-assemble-fold-dissolution.md`, `mk-matrix-free-operator-dissolution.md`, `fe_assemble.md`, `frequency_sweep.md`).
2. Maturity / already-discharged: `grep -n "LinearOperator\[N, N\]\|LinearOperator\[(N: ...)\]"` on the dissolution themes returns the 3 LHS sites STILL opaque (`fe-assemble-fold-dissolution.md:30,37`; `mk-matrix-free-operator-dissolution.md:151`); `fe_assemble.md:77` result line + `frequency_sweep.md:151` codomain STILL opaque. The c129 sweep converted the SIGNATURE codomains (`fe_assemble.md:60` is now `LinOp[(N: ...), $N]`) but NOT these theme-LHS / result-line / cross-chapter residuals. Genuinely OPEN.
3. OQ-ledger RESOLVED-grep: `grep -c "closure-signature-l4-constructor-restatement-compliance-cohort-sweep.*RESOLVED\|...CLOSED"` = **0**. NOT resolved (it is in the MIGRATED-to-plan section, open).
4. Structural-block: none — these are calculus-level codomain spellings, not status promotions; no test-coverage / partly-constructive / obstruction gate applies (pure spelling fidelity). OPEN.

**D3 (inner_product anchor sweep):**
1. File existence: `ls book/src/L3/inner_product.md` → present.
2. Maturity / already-discharged: `sed -n '146p;334p'` confirms the 2 long anchors are STILL the verbatim long form ("## Specializations (the members, as notes under the combinator)" / "## Consumer (NOT an instance): nrm2 / matrix-weighted-norm"). `grep -rn "inner_product.md#" book/src/ | wc -l` = 59 inbound links. Genuinely OPEN.
3. OQ-ledger RESOLVED-grep: `inner-product-combinator-section-anchor-stability` is an OPEN MAINTENANCE-FLOOR item (priorities item-4), not closed.
4. Structural-block: none — anchor-rename + inbound re-point is mechanical count-owner hygiene. OPEN.

**STOP-PROPOSING negative-list check**: NONE of D1/D2/D3 scopes match a disqualified slug (`lu_solve`/`back_solve`/`ls-update-column`/`nleps_*`). All three are consolidation/hygiene on existing surfaces, not L3 backfills.

## Standing-gate re-checks (MAINTENANCE FLOOR items 1-4)

- **RE-set re-check (item-1):** NO RE fires this cycle (D1/D3 prose+anchor; D2 signature spelling fidelity — no maturity/rank/edge change). **RE4** stays consumer-gated (no GMRES-variant / driven-solver-GMRES column surfaces c130). **RE11** residual (combinator-primary `correction_step` leaves + AMR reference-verbs + the `mk-matrix-free-operator-dissolution` lowering theme + `libceed-quadrature-kernel-impl`) premises HOLD — NO new deliberate-reference-only-reachable node lands, so any `detritus`/STRONGER climb at finalize would flag the §2g escalate-guard. Baseline HELD by design.
- **DIRECTIVE-1 boundary (MPI/sharding OUT of active scope):** n/a this cycle — no dispatch lifts the MPI-associated version; the polish pass touches only the L4/L3 calculus surface + the inner_product anchors. No boundary violation.
- **Kernel-API/impl integrity (DIRECTIVE 3):** confirmed INTACT on disk pre-dispatch — `libceed-quadrature-kernel-impl.md:23` carries `kind: realizes-kernel-api` (documentation-only label, `reference`-class), `:80` affirms "the `realizes-kernel-api` link is `reference`-class (free, navigational)"; the `fe-assemble-libceed-boundary-obstruction.md:30,32-34` carries the `kernel-api` role-label + the back-link. No dispatch this cycle touches either node → edge stays `reference`-class.
- **Linter baseline (held):** `files=385, typed=324, untyped=61, roots=45, reachable=163, reference_reachable=247, rank_violations=0, unresolved=0, promotion_frontier=10, detritus=122, true_detritus=50`. File count 385 confirmed on disk. c130 holds it UNCHANGED (no node maturity/edge moves).

## Open questions / caveats

- **D1's BNF-renumbering judgment is the one substantive decision.** Adding the `op-with-params` introducer to the §1.3 `e ::=` block is the c128 D1's deliberately-deferred move (it avoided the strawman BNF renumbering). D1 should weigh whether the introducer is worth the renumber cost OR whether the §1.3.1 prose form (already settled) is sufficient and the BNF-promotion should be recorded as a "decided-against, prose form suffices" disposition. Either outcome closes `closure-signature-op-with-params-bnf-promotion` — the planner does not force the add; it is the semantic-surface owner's call (priorities item-3 explicitly says "owner's call").
- **D2's per-site rank-1-vs-bracketed judgment depends entirely on D1's pin.** If D1's §1.2.2 ruling lands a different boundary than the planner's read (calculus-codomain-position → convert; plain-record-field → keep), D2 follows D1's ruling, not this plan's enumeration. The 5 convert-sites enumerated here (3 theme-LHS + 2 L4-chapter) are the planner's pre-localized candidate set; D2 re-localizes on-disk and applies D1's ruling per-site.
- **This is the polish-pass OPENING, not the whole pass.** The LEAD is bounded but may not fully close in one cycle — if D2's sweep surfaces additional residual sites (e.g. L2/L3 prose mentions the planner's scan flagged as Tier-2 keep but D1's ruling reclassifies), those become c131/c132 follow-ups. The slate is deliberately tight (consolidation, not a wide wave) per the batch-42 sizing directive.
- **No friction-ledger escalating-pattern is unaddressed for this slate.** The relevant ledger entries (`reference-only-reachable-firm-nodes-over-counted-as-detritus` addressed §2g; `deleted-slug-frontmatter-edge-gap` addressed — but no deletions this cycle so it does not apply; `semantic-surface-path-drift-in-role-specs-after-relocation` addressed batch-41, the 9-file sweep loaded via restart) are all `addressed`. No new pattern surfaces from this consolidation slate.

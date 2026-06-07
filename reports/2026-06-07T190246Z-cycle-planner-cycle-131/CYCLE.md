---
agent: cycle-planner
invoked_at: 2026-06-07T190246Z
scope: cycle-131 dispatch plan
status: pending
---

# Cycle 131 dispatch plan

## Goals selected this cycle

Cycle-131 is the **SECOND primary cycle of meta-batch-42** (cycles 130/131/132; meta fires AFTER c132). It CONTINUES the human-chosen **§1.2.2 / closure-signature POLISH PASS** that c130 opened. c130 substantially landed the LEAD (D1 pinned the §1.2.2-R ruling + §1.3 `op-with-params` BNF; D2 swept 15 opaque `LinearOperator[…]` calculus codomains to bracketed form; D3 stabilized the inner_product anchors). c131 picks up the **residual §1.2.2-R convert-sites the c130 sweep did NOT reach** — a tight, bounded set: one genuine L2 calculus-level signature codomain (`L2/matrix-free-operator-apply.md:72`) + the within-chapter result-codomain prose in `L4/assemble_frequency_operator.md` that lags its now-bracketed signature. **This is a SINGLE-dispatch slate by genuine extent** — the polish pass is nearly exhausted; the maintenance-floor items (l2-index count, edge-typing on touched nodes, RE-set) are already discharged or no-op (see §Open questions / caveats — this is a real finding for the batch-42 meta). NO new vocabulary; the redirect's no-forced-rectangular-pull-up governs. NO RE fires (pure signature/codomain fidelity; no maturity/rank/edge change).

## Dispatches

**D1 (`lifter`, WAVE-1) — the residual §1.2.2-R calculus-codomain convert sweep (`closure-signature-cohort-sweep-1.2.2-R-scope-gate` residual + `closure-signature-residual-compliance-sweep`).**
Reading the pinned §1.2.2-R ruling (`book/src/semantics/index.md:101-102, :167, :171` — calculus-level L4/L3/L2 opaque operator-VALUE codomain in a signature/return position → CONVERT to bracketed `Op[Tensor[…] → Tensor[…]]` / square `LinOp[(N: ...), $N]`; genuine rank-1 flat-dof form OR plain operator-VALUE record FIELD → KEEP), convert the residual calculus-level opaque `LinearOperator[…]` codomains the c130 sweep did not reach (USE+LINK §1.2.2/§1.3.1, do NOT restate the convention):
- **`book/src/L2/matrix-free-operator-apply.md:72`** — the L2 combinator signature codomain `-> LinearOperator[(N: ...)]` → bracketed. **This is a genuine calculus-level (L2) operator-VALUE codomain in a signature return position** (the §1.2.2-R smell), already in named-shape-group form `(N: ...)`. Convert to `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` to match the cap exemplar `mk_matrix_free_operator.md:60`/`:104` (the verbatim-cap spelling for the operator this combinator IS the apply-chain of), OR the square-op `LinOp[(N: ...), $N]` — pick to match the within-file / cap consistency (the cap uses `Op[Tensor[…] → Tensor[…]]`, so prefer that for cap-fidelity).
- **`book/src/L4/assemble_frequency_operator.md:137`** (the `result — \`LinearOperator[N, N]\` —` shape-contract codomain line) **+ `:146`** (the "the single return slot is `LinearOperator[N, N]`" prose) → bracketed `LinOp[(N: ...), $N]`, mirroring the now-bracketed signature codomain at **`:99`** (`:: FrequencyOperatorFamily[N] -> Scalar -> LinOp[(N: ...), $N]`, already converted c129). This is the **same within-chapter result-codomain-lags-signature residual class** D2 swept in `fe_assemble.md:77` at c130 — the explicit `result —` shape-contract codomain should mirror the chapter's own settled signature spelling.
- **JUDGE-and-KEEP** per the §1.2.2:102 ruling (do NOT convert): the **record FIELDS** `assemble_frequency_operator.md:103-105` (`K/C/M : LinearOperator[N, N]`, the deliberate c129-D2 dual-spelling) + `:121` (the field shape-precondition prose) + `:215`/`:335` (the **law-prose / discussion** mentions — `:214-216` "Result is a `LinearOperator` (apply/assemble duality)" naming the result value's TYPE in a law statement, and `:335` "the operands are opaque `LinearOperator[N, N]`" — running narrative naming the carrier type, NOT a signature codomain). These are KEEP per §1.2.2:102 (plain operator-VALUE record fields / law-narrative, genuine flat-dof). Also KEEP all L1/L0 forms, the `divfree-projector` record fields (L2/L3), and the `assemble-diagonal`/`apply_linop`/`ksp_solve` rank-1 lowering-prose.
- **OPTIONAL one-line fidelity** (fold in IFF clean, owner's call): the intro-prose monoid-carrier mention `book/src/L4-L3/fe-assemble-fold-dissolution.md:3` (`reduces the per-term \`LinearOperator[N,N]\` contributions`) → `LinOp[(N: ...), $N]` to mirror the theme's own now-converted `:30`/`:37` signatures (OQ `fe-assemble-fold-dissolution-intro-prose-monoid-carrier-codomain-consistency`). Bounded one-line; do NOT over-reach. If the running-narrative reading (monoid carrier, not a signature codomain) is preferred, leave it and note so in the report.
- ON-DISK RE-LOCALIZE each line before editing (OQ line numbers have DRIFTED before). Prose/signature FIDELITY — NO status/rank/edge/node-maturity change. Cite §1.2.2-R + the `mk_matrix_free_operator.md:60`/`fe_assemble.md:60` exemplars (USE+LINK, don't restate).
- **deps:** none. **fan-out:** LOW (fully-consistent calculus surface; completes the residual §1.2.2-R cohort; no new vocabulary). Plan-tag `semantic-consolidation`.

## Overlap analysis

Single dispatch — no pairwise overlap. For the record:
- D1 touches `book/src/L2/matrix-free-operator-apply.md` (one signature line), `book/src/L4/assemble_frequency_operator.md` (two result-codomain prose lines), and optionally `book/src/L4-L3/fe-assemble-fold-dissolution.md:3` (one intro-prose line). All three files are disjoint regions; no shared operator name modified; no consolidated index tally touched (no firm-count moves — pure spelling fidelity, NO node maturity moved). No floor-landing→adjacent-entry re-anchor coupling (no floor lands). No cross-report forward-reference to a not-yet-existing slug (D1 cites only on-disk §1.2.2-R + the on-disk cap/`fe_assemble` exemplars). No `feature/index.md` matrix or SUMMARY block touched.

## Sequencing schedule

- **WAVE-1 (single dispatch):** D1.
- ONE `integrator-finalize` at cycle end (rebuild book + commit + push + housekeeping). Waves are dispatch/forward-reference ordering only; there is exactly one finalize per primary cycle.

## Standing-gate re-checks (batch-42, c131)

- **RE-recheck:** NO RE fires this cycle (D1 is pure signature/codomain spelling fidelity — no maturity/rank/edge change → baseline HELD by design). **RE4** stays consumer-gated (no GMRES-variant / driven-GMRES column dispatched c131 — premise HOLDS). **Residual RE11** (deliberate-reference-only-reachable: the libceed-substrate cohort + `correction_step` combinator-primary leaves + AMR reference-verbs + the `mk-matrix-free-operator-dissolution` theme + the kernel-impls) premises HOLD — no new deliberate-reference-only-reachable node is authored, so any `detritus`/STRONGER climb at finalize would flag the §2g escalate-guard (it must NOT climb — baseline HELD by design this cycle). `scaffolding/graded-stack-baseline-exceptions.md` §RE4/§RE11 are the standing references.
- **DIRECTIVE-1 boundary (MPI/sharding OUT of active scope):** n/a this cycle — no MPI-associated-version lift candidate, no `Par*`/distributed/RAP-parallel-assembly dispatch. The sharding-math gated door stays closed (not dispatched).
- **Kernel-API/impl integrity (DIRECTIVE-3):** the `libceed-quadrature-kernel-impl` (kernel-impl) ↔ `fe-assemble-libceed-boundary-obstruction` (kernel-api) `realizes-kernel-api` edge stays `reference`-class on disk — INTACT, untouched this cycle (D1 does not touch either node, does not re-type any impl→API edge). Confirmed pre-dispatch.

## Linter baseline (HELD by c130 finalize — c131 holds it UNCHANGED; D1 moves NO node maturity)

```
files=385  typed=324  untyped=61  roots=45
reachable=163  reference_reachable=247
rank_violations=0  unresolved_depends_on_targets=0  promotion_frontier=10
detritus=122  true_detritus=50
```

The c131 dispatch is pure signature-codomain spelling fidelity (no `status`/`rank`/`edges` mutation in any file), so the baseline is expected to HELD-by-design at finalize. Both step-5b block-conditions trivially PASS (rank_violations stays 0 — nothing changes rank/edge; no node newly orphaned — reachable stays 163). If any total moves, the finalize should investigate (it would indicate an unexpected maturity/edge touch).

## Deliverable-presence verification (paste-inline evidence per dispatch)

**D1 — residual §1.2.2-R convert sweep.** Open by construction in part (the residual convert-sites are explicitly carried forward by the c130 finalize "Next-cycle priorities" + the OPEN OQ `closure-signature-cohort-sweep-1.2.2-R-scope-gate`), but the genuine residual was verified on-disk this plan:

1. **File existence (both convert-target files present):**
   ```
   -rw-rw-r-- 20920 book/src/L2/matrix-free-operator-apply.md
   -rw-rw-r-- 30232 book/src/L4/assemble_frequency_operator.md
   ```
2. **The convert-sites are GENUINELY still opaque on disk (NOT already swept):**
   - `book/src/L2/matrix-free-operator-apply.md:72`:
     ```
       :: ElemRestriction -> Basis -> GeomData -> Coefficient
       -> LinearOperator[(N: ...)]          ← opaque L2 calculus codomain, the §1.2.2-R smell
     ```
   - `book/src/L4/assemble_frequency_operator.md` — signature `:99` ALREADY bracketed (c129), result-prose `:137`/`:146` STILL opaque:
     ```
     :99  :: FrequencyOperatorFamily[N] -> Scalar -> LinOp[(N: ...), $N]    ← already converted
     :137 - result — `LinearOperator[N, N]` — the combined operator `A(ω)`, square on the   ← residual
     :146 the single return slot is `LinearOperator[N, N]`).                                  ← residual
     ```
   These are residuals the c130 D2 sweep did NOT reach (D2's cohort was the 5 L4/L4-L3 dissolution-theme + cap files; the L2 combinator + the `assemble_frequency_operator` result-prose were out of that cohort).
3. **Maturity / already-discharged check:** both files are `firm` on disk (`matrix-free-operator-apply.md:52-54` "`firm` (rank 3)"; `assemble_frequency_operator.md` `firmness: firm`). The D1 deliverable is a **prose/codomain spelling fidelity edit, NOT a promotion** — there is no maturity no-op risk (the convert is fidelity at constant maturity). Both files carry typed `rank: firm` + `edges:` frontmatter already (verified), so a `p1-edge-typing` touch on them would be a NO-OP (this is why no edge-typing dispatch is warranted — see caveats).
4. **OQ-ledger state:** `closure-signature-cohort-sweep-1.2.2-R-scope-gate` is **OPEN** (`scaffolding/open-questions.md:1980`, "scope-gate now pinned" — the residual convert/keep sites are the carried work). `fe-assemble-fold-dissolution-intro-prose-monoid-carrier-codomain-consistency` is **OPEN/optional** (`:1986`). Neither is RESOLVED/CLOSED — the dispatch is open work.
5. **Structural-block check:** NO methodology gate blocks this — it is consolidation of the EXISTING calculus surface to fully-consistent (the chosen batch-42 LEAD), explicitly NOT a forced vocabulary frontier (the redirect's no-forced-rectangular-pull-up does not bite — no new node, no rectangular floor). The §1.2.2-R ruling is on disk (`semantics/index.md:101-102,:167,:171`), so D1 reads-and-applies, no localization loop.

**Items checked and found ALREADY-DISCHARGED / no-op (NOT recruited):**
- `l2-index-prose-vs-dep-map-firm-count-reconcile` (batch-41 item-6) — **DISCHARGED c127 D5.** `book/src/L2/index.md:95` reads "17 firm + 1 `partly-constructive` (`deflate`) = 18 dep-map rows (self-summing)"; the narratives `:166`/`:169` carry the "since revised → current 18 rows; see :95" reconciliation parentheticals. `grep "17 firm + 1"` confirms. No reconcile work remains. NOT recruited.
- `p1-edge-typing-true-detritus-sweep` (maintenance-floor item) — **no-op on the nodes this cycle touches.** Both D1 target files already carry typed `rank: firm` + `edges:` blocks (pasted above). A lazy-tail edge-typing touch is fold-into-cycles-that-touch-UNTYPED nodes; these are typed, so there is nothing to type. NOT recruited (would be padding).
- `mk-matrix-free-dissolution-codomain-spelling-Op-vs-LinOp-uniformity` (OQ `:1992`) — **benign, critic-cleared, optional.** The `:104`/`:370` (`Op[…]`, verbatim-cap) vs `:151` (`LinOp[…]`, derived-product) dual-spelling is principled and internally consistent (both §1.2.2-sanctioned). NOT a defect; left to the meta-phase if a reviewer prefers uniformity. NOT recruited as forced work.

## Open questions / caveats

- **FINDING for the batch-42 meta-phase: the §1.2.2 / closure-signature POLISH PASS is NEARLY EXHAUSTED.** After the c130 sweep (15 codomains) + this c131 residual sweep (3 convert-sites + 1 optional fidelity line), the genuine §1.2.2-R convert cohort bottoms out. The remaining `LinearOperator[…]` occurrences across `book/` (≈150 total) are all KEEP-by-ruling: L1/L0 flat-dof forms, plain operator-VALUE record fields (the deliberate c129-D2 dual-spelling), and law-prose / running-narrative carrier mentions. **The spine is L4-COMPLETE and this batch is the bounded polish + maintenance-floor steady-state, exactly as the c129 capstone recommended.** c132 (the batch-closing cycle) likely has only hygiene / OQ-cleanup left; the batch-42 meta should expect to (a) CLOSE the closure-signature OQ family fully, (b) confirm the polish pass complete, and (c) decide the post-batch-42 direction (the §CENTRAL-ASK candidates: wind-to-maintenance vs the gated sharding-math vs something else the human prioritizes). I am surfacing this now per the cadence note (the meta does not fire until after c132).
- **The two benign uniformity OQs** (`fe-assemble-fold-dissolution-intro-prose-monoid-carrier-codomain-consistency`, `mk-matrix-free-dissolution-codomain-spelling-Op-vs-LinOp-uniformity`) are genuinely optional stylistic-consistency, critic-cleared as non-defects. I folded the first into D1 as an OPTIONAL one-line edit (owner's call); the second I did NOT recruit (principled dual-spelling, leave to meta). If the meta wants a single uniform spelling across the `mk-matrix-free-dissolution` theme, that is a one-line bounded edit for a future cycle.
- **The `divfree-projector` "keep-site" the c130 critic flagged** (no `book/src/L4/divfree-projector.md` exists; its operator-record fields live at L1/L2/L3) is correctly a KEEP per §1.2.2:102 (record fields, genuine flat-dof `LinearOperator[N_h1, N_h1]` etc.). D1's scope does NOT touch it. No action.

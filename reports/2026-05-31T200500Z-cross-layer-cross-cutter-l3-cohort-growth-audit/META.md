---
verifies: ../CYCLE.md
critiqued_at: 2026-05-31T183016Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: pass
repaired_at: 2026-05-31T210000Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: critique of cross-layer-cross-cutter L3-cohort-growth audit (cycle-036 D2)

## Critique

### Checks run

**citation-validity** — `python3 tools/citecheck/citecheck.py --scan` returns 19 ok / 0 failing, so all in-text `path:lines` pointers are in-range. Spot-anchor checks confirm the load-bearing crux: `book/src/L3/index.md:10-16` anchors `whole-tensor` at line 13 (cohort criterion); `book/src/L3/index.md:38` anchors `Cohort growth` at line 38 (deferred-audit note, byte-identical to the proposed-changes "old:" block); `book/src/L1/assemble-diagonal.md:14-19` anchors `LinearOperator` at line 16 (signature `(A: LinearOperator[N, N]) -> Tensor[N]` verified — whole-tensor in, whole-tensor out, no element loop); `book/src/L1/assemble-diagonal.md:37` anchors `approximate` at line 37 ("This is a load-bearing numerical property ... Recorded here as a non-law, not erased" — the report's crux reasoning that the exact-vs-approximate caveat is a representation-aware non-law is directly supported by the L1 entry's own framing); `book/src/L3/apply_linop.md` indeed carries a parallel "Reduction-tree non-associativity" non-law (precedent confirmed). However TWO load-bearing anchor drifts surfaced — see Issues found §1 and §2.

**surface-or-evidence** — pure observation/classification dispatch with retroactive-evidence framing (the verdict against pre-existing L1 entries against the pre-existing L3 cohort criterion); no operator/theme surface text is being changed (only the L3 working-note bullet is replaced with the verdict). The single proposed edit is a working-note refresh, not a refinement of a firm-operator surface; the retroactive-evidence shape is the correct one for a settling-audit. PASS.

**rotation-quality (classification soundness analog)** — the (A)/(B)/(C) assignments are well-reasoned against the L3 membership criteria:
- **(A) `assemble-diagonal`** crux: the report's reasoning — opaque `LinearOperator[N, N]` in, `Tensor[N]` out, no element loop at L3 vocabulary, exact-vs-approximate caveat is a representation-aware **non-law** at L1>L0 (parallel to `apply_linop`'s reduction-tree non-associativity non-law at L3) — is directly supported by both the `book/src/L1/assemble-diagonal.md:37` text ("Recorded here as a non-law, not erased") AND the precedent `book/src/L3/apply_linop.md:59` reference to "Reduction-tree non-associativity" as an explicit non-law. The crux holds; the (A) verdict that reverses the orchestrator's initial caution is sound.
- **(C) the 7 not-L3-relevant** disqualifier ("small-dense coordinate-space axis, NOT the field axis — a categorically different cost-model regime"): consistent with how L3 already absorbs coordinate-space algebra opaquely into `ksp_solve` / `eigsolve` (the inner Hessenberg back-solve at GMRES restart-cycle close, the SLEPc/ARPACK opaque eigen-iteration). The mixed `(N, k)` NLEPS-atom carve-out is also sound — they live "inside" the firm-L3 `eigsolve` `partial-obstruction`, and admitting them as separate L3 rows would re-expose interior coordinate-space algebra that L3 collapses into the outer-driver.
- **(B) the 3 substantive**: each well-distinguished from (A) — `orthogonalize` MGS sequential-obstruction is explicitly noted in `book/src/L1/orthogonalize.md` (CGS/CGS2 lift cleanly, MGS does not); `chebyshev-smoother` subsumption question against the existing firm L3 `chebyshev` is correctly flagged as needing a subsumption check first; `apply_nonlinear_pencil` interior-to-`direct_newton`-variant routing is consistent with `book/src/L1/apply_nonlinear_pencil.md:17` ("This operator is the **interior** of the `eigsolve` gate").

PASS on the classification reasoning. (See Issues §3/§4 for the count-arithmetic separately — the reasoning is sound but the headline integers don't match the enumerated bullets.)

**variant-axis-coverage** — the classification covers each L1 operator's variant axes via the row-level rationale (e.g., `orthogonalize` row 8 distinguishes MGS-variant vs CGS/CGS2-variant; `lu_solve` row 11 distinguishes the small-dense `(k,k)` regime from the field-axis `N` regime; `apply_nonlinear_pencil` row 14 acknowledges the (B)/(C) ambiguity along the eigsolve-orchestration-variant axis). No hidden branches. PASS.

**cross-reference-integrity** — all referenced L1/L3 slugs exist in the artifact (verified `book/src/L3/index.md`, `book/src/L1/assemble-diagonal.md`, `book/src/L1/jacobi-smoother.md`, `book/src/L1/orthogonalize.md`, `book/src/L1/lu_solve.md`, `book/src/L1/apply_nonlinear_pencil.md`, `book/src/L1/nleps_deflated_residual.md`, `book/src/L3/apply_linop.md` etc. — all exist on disk). The single proposed-changes block is fence-enclosed (one fence-pair, lines 136 + 151, well-formed). The "old:" payload is byte-identical to the actual line-38 content in `book/src/L3/index.md`. The "new:" payload is a single-bullet replacement that does NOT touch the surrounding cohort-growth bullets at lines 37, 39-45 (these are the "First firm L3 operator landed cycle-010" / "Second firm L3 operator landed cycle-011" / wave-1 cohort entries that the bullet at :38 is interleaved among) — verified by inspection that the bullet at :38 is structurally independent of its neighbors. The replacement bullet is well-formed (lead-bold + paragraph + nested bullets), preserves the same bullet-level depth, and does not introduce a stray fence or unclosed indent. PASS.

**edge-label-fidelity** — the audit is not an `L_{n+1}>L_n` lowering with an edge label; it is a cohort-membership classification at L3 vs L1. The "L1↔L3 cross-cut" framing in the scope frontmatter is accurate to the actual content (which operates against the L3 cohort criterion at `book/src/L3/index.md:10-16` and the firm L1 inventory). Not applicable to this report-kind shape. PASS.

**plan-kind-consistency** — declared as `cross-layer-cross-cutter` observation. Content shape matches: a coverage-gap classification that (a) settles the long-standing `book/src/L3/index.md:38` deferred-audit note, (b) migrates concrete (A)/(B) candidates to the cycle-037+ planner via OQ `l3-cohort-growth-audit-c036-verdict` (replaces older OQs `l3-vocabulary-inventory-gap` and `l3-backfill-apply-linop-and-blas1-cohort` per the proposed-changes payload), (c) records the (C) "never re-propose" negative list (directly addressing the `cycle-planner-stale-priorities-line-recruitment` recurrence-3 friction), and (d) does NOT author any L3 entry itself (correct — that's follow-up harvester work, queued under §Recommendation point 1-2). The "Open questions / caveats §" §5 explicitly cross-links the audit verdict to the cycle-033 `verify-dispatch-scope-not-already-discharged` skill as the consuming data — appropriate forward-routing. WARNING is downgraded from PASS solely because of the count-arithmetic issue (see Issues §3) which materially affects the verdict the next planner consumes (a "(C) — 8" claim with only 7 bullets, and "(A) — 4" with 6 bullets, blunts the decisiveness of the negative list the audit exists to provide).

**skill-uptake-survey** — the report references the `cycle-planner-stale-priorities-line-recruitment` friction-ledger entry and the cycle-033-promoted `verify-dispatch-scope-not-already-discharged` skill (Open questions §5). It does not name `verify-citation-range` or `phase-1-slice-reduction-audit` skills, but the dispatch shape (cross-layer classification audit) does not directly invoke those. The audit's value-delivery hinges on the negative list being decisive enough to serve `verify-dispatch-scope-not-already-discharged` — adequately referenced. Telemetry only; pure presence check. PASS.

### Issues found

**Issue 1 (citation-validity, citation drift — load-bearing claim)**: `book/src/L1/lu_solve.md:82-83` is cited in the table row 11 (rationale column) AND in §Supporting evidence ("`lu_solve` L1 (small-dense `k`-axis, distinct from large field `N`): `book/src/L1/lu_solve.md:82-83`") as the source for the quoted text "The axis `k` is the small coordinate dimension (deflation rank or ROM basis size — single to low tens), **not** the large field dimension `N` of `apply_linop` / `ksp_solve`". `tools/citecheck/citecheck.py book/src/L1/lu_solve.md:82-83 --anchor "small coordinate"` returns `[DRIFT] anchor at line 69, -13 outside range 82-83`; `grep -n "small coordinate" book/src/L1/lu_solve.md` shows the exact quoted text is at **line 29** (the Shape-contract bullet for `A`), with a partial restatement at line 69. Line 82-83 is the `## Status` block ("`firm` — the operator's structure is read directly from positive Palace source sites ..."), which does NOT carry the small-vs-large axis claim. The cited range supports the operator's `firm` status but not the specific quoted text. Severity: **moderate** — the cited *claim* is fully supported by the file (it appears at line 29), but the *line range* is wrong; a downstream reader who follows the citation lands on the Status block and cannot verify the small-coordinate claim there. The proposed-changes block at line 149 carries this drifted cite (`book/src/L1/lu_solve.md:82-83`) into the artifact verbatim — once integrated, the cite drift lands in `book/src/L3/index.md` permanently. Recommended fix: change `book/src/L1/lu_solve.md:82-83` to `book/src/L1/lu_solve.md:29` (Shape-contract bullet, exact-text source) OR `book/src/L1/lu_solve.md:29,69` (both anchors).

**Issue 2 (citation-validity, citation drift — minor)**: `book/src/L1/apply_nonlinear_pencil.md:22` is cited in row 14 (L1 status column) for the signature. `--anchor "NonlinearPencil"` returns `[DRIFT] anchor at line 23, +1 outside range 22-22, suggested: book/src/L1/apply_nonlinear_pencil.md:23`. The signature block actually spans lines 22-23 (line 22 = bare identifier `apply_nonlinear_pencil`, line 23 = `:: (T: NonlinearPencil[N], ...)`); the report should cite `:22-23` not `:22`. Severity: **minor** — the cited single line is at the start of the signature, but the type token `NonlinearPencil[N]` the report's classification quotes is on line 23. The fix is a one-character change (`:22` → `:22-23`).

**Issue 3 (plan-kind-consistency, count arithmetic mismatch — load-bearing for downstream consumers)**: the §Summary §, the §Recommendation §, AND the proposed-changes payload all carry count-bullet mismatches:
- "(A) Identity-in-form L3 backfill candidates — **4**" (CYCLE.md:63) but the bullets enumerate **6** (assemble-diagonal, reciprocal, elementwise_product, normalize, divfree-projector, jacobi-smoother). Same error in the proposed-changes payload at CYCLE.md:146 ("**(A) Identity-in-form L3 backfill candidates — 4 firm**").
- "(C) NOT L3-relevant — **8**" (CYCLE.md:80) but the bullets enumerate **7** (lu_solve, back_solve, ls-update-column, plus the four NLEPS atoms — 3+4=7). Same in the proposed-changes payload at CYCLE.md:149 ("**(C) NOT L3-relevant — 8** (DO NOT re-propose)") and in the closing sentence at CYCLE.md:89 ("Any future cycle that proposes an L3 backfill for one of these **8** operators is **stale**").
- §Recommendation point 1+2 list 6 high-priority backfills (assemble-diagonal + 5 others), consistent with 6 (A) — but inconsistent with the headline "4". The Recommendation enumeration is the correct count (6); the headlines are off.

Severity: **moderate-to-significant** — this is the audit whose value depends on the verdict being decisive. A future cycle-planner consuming the `book/src/L3/index.md:38` updated bullet (post-integration) will see "(A) — 4" but enumerate 6 names, and "(C) — 8" but enumerate 7 names. The skill `verify-dispatch-scope-not-already-discharged` (cycle-033) the audit is explicitly designed to feed (Open questions §5) checks against the negative list — the count-text mismatch could cause downstream confusion ("is there an 8th (C) operator I'm missing?") undermining the stop-stale-recruitment purpose. Recommended fix: change "(A) — 4" to "(A) — 6" and "(C) — 8" to "(C) — 7", consistently across §Summary §, §Recommendation, the proposed-changes payload, AND the closing-sentence count at line 89.

**Issue 4 (plan-kind-consistency, framing — minor)**: the Summary § opens with "classifying the 18 firm L1 operators that lack an L3 entry" (CYCLE.md:12), but rows 9 (`matrix-weighted-norm`) and 10 (`bilinear-form`) are explicitly *not* firm at L1 — they are `rough-in (test-coverage-bounded)` and `rough-in (lower-layer-shared-vocabulary)` respectively (correctly tagged in the table). So the corpus is 16 firm + 2 rough-in = 18 L1 operators (not 18 *firm*). The same loose framing recurs in §Recommendation point 4 ("L1-promotion-gated") which acknowledges the rough-in status only there. Severity: **minor** — does not affect the verdict, only the precision of the opening framing. Recommended fix: replace "18 firm L1 operators" with "18 L1 operators (16 firm + 2 rough-in, the 2 rough-ins L1-promotion-gated at L3 per cycle-009 precedent)".

**Issue 5 (plan-kind-consistency, OQ replacement claim — verify-by-checking)**: the proposed-changes payload at CYCLE.md:150 asserts that the audit's six (A) backfills are "routed to cycles 036-038+ planner under OQ `l3-cohort-growth-audit-c036-verdict` (replaces the older `l3-vocabulary-inventory-gap` and `l3-backfill-apply-linop-and-blas1-cohort`)". This is a load-bearing OQ-migration claim — the audit is taking authority to retire/replace two existing OQ IDs. The CYCLE.md does not (in this dispatch's authority) actually modify `scaffolding/open-questions.md`; the integrator-per-report path is what would migrate the OQ ledger entries. The "replaces" language is asserted-in-the-artifact-text rather than enacted-in-the-OQ-ledger — at integration, the per-report integrator should be aware that this language commits to an OQ-ledger migration (open the two predecessor OQs to closed/migrated, append the new OQ `l3-cohort-growth-audit-c036-verdict`). Severity: **minor / advisory** — the surface text is consistent with the audit's intent, but the OQ-ledger surgical edits are downstream work; flagging here so the integrator-per-report does not skip it. Recommended fix: none in the report; flag for the integrator-per-report to handle the OQ-ledger migration when applying this edit (or for the repairer to add an explicit "Open questions" stanza that the integrator can mechanically consume).

**Issue 6 (citation-validity, sub-check — table row 1 self-reference)**: row 1's rationale cites `book/src/L3/apply_linop.md:22` as "first L3 op whose body's direct constituent is itself a constructed-solver fold". That string actually appears at `book/src/L3/eigsolve.md`'s row in `book/src/L3/index.md:31` (the eigsolve row, not `apply_linop` row at :22). `apply_linop` is the FIRST L3 op of the BLAS-1 / opaque-operator-gate kind; `eigsolve` is the first L3 op whose body's direct constituent is a constructed-solver fold (i.e., the inner `ksp_solve`). The report appears to have confused the two precedents — `apply_linop`'s relevant property for the `assemble-diagonal` parallel is its opaque-operator-gate + representation-aware non-law, NOT its (non-existent) constructed-solver-fold body. Severity: **minor** — the underlying parallel ((A) assemble-diagonal is structurally identical to (A) apply_linop) is correct; the mis-attributed sub-clause is the precedent-naming. Recommended fix: drop the "first L3 op whose body's direct constituent is itself a constructed-solver fold" parenthetical from row 1 (it belongs to `eigsolve`, not `apply_linop`); replace with a direct reference to `apply_linop`'s opaque-operator-gate + reduction-tree non-associativity non-law precedent.

## Repair

### Fixes attempted

- **Finding (Issue 1, citation-validity)**: `book/src/L1/lu_solve.md:82-83` cited as the source for the "small coordinate dimension ... not the large field dimension N" quoted text, but the quoted text is at line 29 (line 82-83 is the Status block). Lands in the artifact via the proposed-changes payload — must be fixed before integration.
  - **Decision**: repaired
  - **Action**: changed `:82-83` → `:29` in (a) row 11 rationale column at CYCLE.md table; (b) §Supporting evidence; (c) the proposed-changes payload `new:` block. Verified on-disk with `citecheck.py book/src/L1/lu_solve.md:29 --anchor "small coordinate"` (anchor at line 29, in range).

- **Finding (Issue 2, citation-validity)**: `book/src/L1/apply_nonlinear_pencil.md:22` for the signature; the `NonlinearPencil[N]` token is at line 23. Drift of +1.
  - **Decision**: repaired
  - **Action**: changed `:22` → `:22-23` in row 14 (L1 status column) and in §Supporting evidence (NLEPS atoms bullet, added the signature reference). Verified on-disk with `citecheck.py book/src/L1/apply_nonlinear_pencil.md:22-23 --anchor "NonlinearPencil"` (anchor at line 23, in range).

- **Finding (Issue 3, count arithmetic mismatch)**: "(A) — 4" enumerated as 6 bullets; "(C) — 8" enumerated as 7 bullets. The same error in §Summary opening (line 12), §Observation kind (line 16), §Summary §bullets headline counts (lines 63, 80), the proposed-changes payload `new:` block (lines 146, 149), and the closing-sentence count (line 89). Recounted from the table rows: (A) firm = 6 (rows 1, 2, 3, 4, 5, 7), (A) L1-promotion-gated = 2 (rows 9, 10), (B) = 3 (rows 6, 8, 14), (C) = 7 (rows 11, 12, 13, 15, 16, 17, 18). Total 6 + 2 + 3 + 7 = 18 ✓.
  - **Decision**: repaired
  - **Action**: (a) Summary opening §: "4 (A) ... 3 (B) ... 11 (C)" → "**6 (A) firm + 2 (A) L1-promotion-gated** ... **3 (B)** ... **7 (C)**". (b) Observation-kind line: "4 firm L1 operators have a clear identity-in-form L3 entry waiting" → "6 firm L1 operators have a clear identity-in-form L3 entry waiting (... 2 additional `rough-in` L1 operators are gated on L1 promotion to firm)". (c) §Summary headline "(A) — 4" → "(A) — 6 firm". (d) §Summary headline "(C) NOT L3-relevant — 8" → "(C) NOT L3-relevant — 7". (e) Closing-sentence "8 operators" → "7 operators". (f) Proposed-changes payload `new:` block: same edits across "Verdict against the 18 ..." (added the 16 firm + 2 rough-in clarification), "(A) — 4 firm" → "(A) — 6 firm", "(C) — 8" → "(C) — 7", "eight (C) operators" → "seven (C) operators", "Six (A) backfills" → "Six (A) firm backfills". (g) Open-questions caveat about cycle-planner mitigation: "8 (C) operators" → "7 (C) operators". Verified internal consistency across all 7 sites.

- **Finding (Issue 4, framing imprecision)**: "18 firm L1 operators" but 2 are `rough-in`, not firm. Same loose framing in proposed-changes payload.
  - **Decision**: repaired
  - **Action**: replaced "the 18 firm L1 operators that lack an L3 entry" → "the 18 L1 operators (16 firm + 2 `rough-in`, the 2 rough-ins L1-promotion-gated at L3 per cycle-009 precedent) that lack an L3 entry" in §Summary opening (line 12) and in the proposed-changes payload `new:` block (line 145). §Observation-kind line edited to "the 18 L1-without-L3 candidates" (also drops the "firm" loose-framing).

- **Finding (Issue 5, OQ-ledger migration not enacted)**: the proposed-changes payload asserts retirement of `l3-vocabulary-inventory-gap` + `l3-backfill-apply-linop-and-blas1-cohort` but includes no OQ-ledger surgical edits.
  - **Decision**: repaired
  - **Action**: Two-fold. (a) Rewrote the closing assertion in the proposed-changes payload `new:` block to clarify routing authority: "Six (A) firm backfills are routed to cycles 036-038+ planner under OQ `l3-cohort-growth-audit-c036-verdict` (which the integrator-per-report appends to `scaffolding/open-questions.md`, retiring the older `l3-vocabulary-inventory-gap` and `l3-backfill-apply-linop-and-blas1-cohort` OQs as superseded by this verdict)". (b) Appended a new explicit "OQ-ledger migration (FOR INTEGRATOR-PER-REPORT)" stanza to §Open questions / caveats with three mechanically-consumable edits the integrator-per-report should enact: append the new OQ (with the full verdict text inline), mark predecessor-1 as superseded, mark predecessor-2 as superseded. This routes the OQ-ledger work to the agent with the open-questions.md append authority per the role-spec partition (CLAUDE.md §Write-authority).

- **Finding (Issue 6, precedent mis-attribution)**: row 1 cites `book/src/L3/apply_linop.md:22` as "first L3 op whose body's direct constituent is itself a constructed-solver fold"; that property belongs to `eigsolve` (L3 row `:31`), not `apply_linop`. Underlying parallel ((A) assemble-diagonal ≈ (A) apply_linop identity-in-form) holds — only the sub-clause is wrong.
  - **Decision**: repaired
  - **Action**: dropped the mis-attributed parenthetical and rewrote to point at `apply_linop`'s actual relevant property: `book/src/L3/apply_linop.md:22 "first L3 op whose body's direct constituent is itself a constructed-solver fold"` → `book/src/L3/apply_linop.md` describing "representation-aware reduction-tree non-associativity recorded as an explicit non-law ... same opaque-operator-gate + representation-aware non-law pattern". Preserves the load-bearing parallel (the (A) classification crux for assemble-diagonal is unchanged).

### Unrepairable findings

None. All six findings were mechanical or surgical:
- Two were single-character / single-token line-range fixes (Issues 1, 2) with on-disk anchor-verification confirming the corrected lines.
- One was a recount across consistently-named call sites (Issue 3), straightforward bookkeeping per the actual table-row enumeration.
- One was a framing-precision edit using the table's own row-level status tags (Issue 4).
- One was a routing-clarification edit + a follow-up integrator-consumable stanza (Issue 5) — within repairer authority because the OQ-ledger edits are queued for the integrator (the role with the write authority), not authored here.
- One was a precedent-naming substitution where the underlying parallel is correct (Issue 6) — within repairer authority because the load-bearing classification is preserved.

### Re-verification

- `python3 tools/citecheck/citecheck.py --scan reports/2026-05-31T200500Z-cross-layer-cross-cutter-l3-cohort-growth-audit/CYCLE.md` returns **18 ok / 0 failing**.
- Anchor re-checks pass: `lu_solve.md:29 --anchor "small coordinate"` ok; `apply_nonlinear_pencil.md:22-23 --anchor "NonlinearPencil"` ok.
- Counts are internally consistent: 6 (A) firm + 2 (A) L1-promotion-gated + 3 (B) + 7 (C) = 18 across §Summary opening, §Observation kind, §Summary bullet headlines, the proposed-changes payload (both the verdict-against-18 framing and the per-class counts), the closing-sentence stale-list count, and the OQ-caveat cycle-planner-mitigation reference.

## Suggested resolution

**`overall_status: ready`**. The classification is sound (the critic concurred on rotation-quality, surface-or-evidence, variant-axis-coverage, cross-reference-integrity, edge-label-fidelity, skill-uptake-survey — all PASS), and the two flagged WARNING areas (citation-validity, plan-kind-consistency) were entirely mechanical: cite-line drifts the citecheck tool now confirms clean, count arithmetic now consistent across all 7 instance sites, and the OQ-ledger migration explicitly routed to the integrator-per-report (which has the open-questions.md append authority per the role-spec partition).

Notes for the integrator-per-report:
- The proposed-changes block at CYCLE.md:136-151 replaces the one bullet at `book/src/L3/index.md:38` with the verdict bullet. The `old:` payload is byte-identical to the line-38 content; the `new:` payload is internally consistent post-repair.
- The new "OQ-ledger migration (FOR INTEGRATOR-PER-REPORT)" stanza in §Open questions / caveats specifies three mechanical edits to `scaffolding/open-questions.md` (one append, two supersession marks). These are the OQ-ledger surgical edits the proposed-changes block commits to.
- The audit's (C) negative list is the data feed for the cycle-033-promoted `verify-dispatch-scope-not-already-discharged` skill. The c037+ planner should consult the line-38 bullet (post-integration) before proposing any L3 backfill against the 7 named (C) operators.

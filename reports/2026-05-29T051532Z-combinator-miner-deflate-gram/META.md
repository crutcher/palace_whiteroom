---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T060000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-29T064500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Combinator candidate — deflate / gram (deflation-subspace oblique projection)"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing source range was independently `read_range`-verified this invocation. Confirmed: the Gram build `SS(i,j) = linalg::Dot(GetComm(), X[i], X[j])` at `nleps.cpp:526-531` (the report's `gram` G1, claim `gram[i,j] = X[j]ᴴ X[i]` is consistent with the free-function `Dot(comm,a,b) = bᴴa` order); the `deflated_solve` deflation correction block `:520-535` (coord extraction `x2(j) = b2(j) − Dot(comm, x1, X[j])` at `:520-523`, Schur-modify `SS = −S.fullPivLu().solve(SS)` at `:533`, coord solve `:534`, back-projection `MatVecMult` + `AXPY` at `:535-536`); the residual deflation coords at `:561-569` (`rr2(j) = Dot(comm, vv, X[j])` at `:566-569`, back-projection at `:563-565`); the Jacobian deflation terms at `:663-668` (`S = eig·I − H` at `:664`, `XSv2` at `:666`, `XSSv2` at `:667`); and `MatVecMult` as a length-`k` linear_combination at `:329-347`. The literature anchors (Jarlebring 2018, Effenberger 2013, SLEPc-NEP minimality index 1) are present at `:354-362`. The `k==0` early-return (identity element) is at `:515-518`. The CRUX search claims both verified independently: `search_text fullPivLu` returns hits ONLY in `nleps.cpp` (6 sites: `:533,:534,:535,:563,:665,:667`), and `search_text [Dd]eflat` returns hits only in `nleps.cpp` — corroborating the single-algorithm-concentration claim. `get_call_sites MatVecMult` returns exactly the 5 sites claimed (`:535,:563,:666,:667,:788`). The `orthog.hpp:19-89` over-unification target verified (see cross-reference-integrity). All book anchors resolve.

**surface-or-evidence — pass.** Not a refinement of existing surface (no operator/theme text is modified); it is a new-combinator proposal carrying its grounding inline, which is the correct shape for a combinator-miner rough-in. The grounding is sound: (i) the incremental-Gram block law `gram(X ++ Y) = [[Gxx,Gxy],[Gyx,Gyy]]` is a standard, correct consequence of the all-pairs `inner_product` definition and is tied to a real growth site (`nleps.cpp:606-619`, `X.resize(k+1); X[k]=v`); (ii) the oblique-projection characterization `deflate = I − X(XᴴX)⁻¹Xᴴ` is the correct complementary projector for the verified `X·(SS⁻¹·(Xᴴv))` assembly; (iii) the ≥3-instance count (D1 `:520-535`, D2 `:561-569`, D3 `:663-668`) is verified against source.

**rotation-quality — pass.** Not applicable in the strict L_{n+1}→L_n rotation sense (this is a same-layer L2 combinator proposal, not a cross-layer lowering), so the relevant judgment is the requested L2-vs-L1 level decision. That decision is well-argued and correct: neither `gram` (`k²` `dot`s) nor `deflate` (`k` `dot`s + Gram build + LU solve + `k`-term linear_combination) has an atomic L0 reduction/BLAS kernel of its own — they are compositions over `dot`/`inner_product`/`linear_combination`, which is exactly the L2 fusion-rotation role (`book/src/L2/index.md:11`, verified). Palace literally fuses the Gram into a double `for`-loop of `linalg::Dot` (`:526-531`); unfolding that into the named all-pairs fold IS the L2 rotation — strictly more abstract/equational than the L0 loop, not a 1:1 rename. The sibling placement alongside firm `inner_product`/`linear_combination`/`orthogonalize` is sound.

**variant-axis-coverage — pass.** Both instance-counting modes were run and reported. Same-shape mode: ≥3 within `nleps.cpp` (verified). Parametric/variadic-family mode: correctly concludes there is no fixed-arity sibling cohort folding to a variadic parent (unlike the BLAS-1 family); the genuine parametric axis is basis-cardinality `k`, which makes `gram`/`deflate` naturally variadic-in-`k` single combinators — the incremental-Gram block law certifies this is a genuine fold over basis columns, not a coincidental cluster. The per-combinator variant axes (`dot` hook {canonical, B-weighted}; element-type {real, complex} absorbed by `dot`; in-place/out-of-place; plain-oblique vs Schur-modified-NLEPS) are enumerated, and the Hermitian-symmetry-exploitation is correctly scoped out as a transparent perf trick (not a structural axis) — verified that `:526-531` computes all `k²` entries with no triangle-only exploitation. No hidden branches.

**cross-reference-integrity — pass (CRUX).** All references resolve: the append-target `ksp_solve` stub row IS at `book/src/L2/index.md:53`; the do-NOT-merge fold-cohort boundary IS at `index.md:69`; `linear_combination`/`inner_product` rows at `:49`/`:50`; `orthogonalize.md:42-44,74-76` confirm both the stateless-L2-placement argument and the orthonormal-basis precondition; `dot.md:43` confirms the arg-1-conjugated convention and the free-function-vs-method asymmetry the report reconciles; `concepts/trsv.md` exists; the dot-callers census `:198-202` does propose this exact combinator with the conjugation-pinning rationale (provenance chain intact). The two proposed dep-map rows correctly use plain-text/inline-code forward-refs for `gram`/`deflate` (verified `book/src/L2/deflate.md` and `gram.md` do NOT exist) — no live links to missing files. **Over-unification guard is sound.** Verified `orthog.hpp:19-89`: both `OrthogonalizeColumnMGS` (`:41-54`) and `OrthogonalizeColumnCGS` (`:57-89`) do sequential/batched rank-1 subtraction `w.Add(-H[j], V[j])` with NO Gram matrix and NO solve; header `:22` states "Assumes that the input vectors are normalized" (orthonormal precondition). Contrast with `nleps.cpp:606-619` (raw normalized-eigenvector basis, no inter-column orthogonalization → full-rank-but-not-orthonormal → `(XᴴX)⁻¹` load-bearing). The decisive distinguisher (Gram-matrix LU solve) is real and correctly identified. The `orthogonalize = deflate|_{gram=I}` claim is mathematically correct (`XᴴX = I ⟹ X(XᴴX)⁻¹Xᴴ = XXᴴ`) AND framed safely as a specialization edge, NOT an over-merge: the report explicitly keeps the two entries distinct, names the differing algorithm and precondition, and forbids any future unification from erasing the `(XᴴX)⁻¹`. This is the correct related-but-distinct stance.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (same-layer L2 proposal); the `orthogonalize = deflate|_{gram=I}` specialization relation is a same-layer cross-reference edge, and the prose discusses exactly that relation (the over-unification guard table and surrounding text). Not applicable to this report-shape beyond that; consistent where it does apply.

**plan-kind-consistency — pass.** Declared kind matches content: this is a `rough-in` combinator proposal (two `rough-in` dep-map rows, signatures explicitly deferred to the harvester, `lu_solve` dependency flagged-not-resolved, factoring decision deferred). The frontmatter `status: pending` and the rough-in row status cells are consistent with a proposal-only report that mutates no chapter files. The "one pattern per invocation" discipline is respected (proposes the deflate/gram pair from one pattern; explicitly does NOT propose `lu_solve`).

**skill-uptake-survey — warning.** The report's shape implies several relevant skills exist but none is referenced as invoked. `classify-variant-axis` is directly on-point for the both-modes variant/family analysis (§"Instance-counting: both modes"); `propose-rotation`/`verify-rotation-citation` and `verify-citation-range` map to the level-decision and citation-grounding work. The report says ranges were "`read_range`-verified this invocation" (good practice) but cites no skill invocation. Pure telemetry surface — non-blocking — but the variant-axis and citation-range work would have been natural skill-invocation points.

### Issues found

1. **D3 instance-header line range slightly over-wide — `reports/.../CYCLE.md` §"Pattern instances" (Instance D3).** The header cites `nleps.cpp:663-668` for the Jacobian deflation terms, but the actual load-bearing lines are `S = eig·I − H` at `:664`, `Sv2` at `:665`, `XSv2` at `:666`, `XSSv2` at `:667` — `:663` is a comment line and `:668` is `opJ->AddMult(...)`. In-range and not wrong, just one line wide on each side. The §"Supporting evidence" block refines correctly to `:664,:666,:667`. Severity: low (cosmetic range tightening).

2. **Reference-anchor line range off by ~2 — §"Pattern instances" intro.** The intro says "`:356-362` cite the Effenberger 2013 / Jarlebring 2018 references", but `read_range` shows Jarlebring 2018 begins at `:354` and Effenberger 2013 at `:357`. The §"Supporting evidence" block uses the correct `:354-362`. The narrower `:356-362` omits the Jarlebring `:354-355` lines. Severity: low (citation under-shoots by two lines; corrected elsewhere in the same report).

3. **Single-algorithm concentration — cross-algorithm fan-out is forecast, not observed (§"Open questions / caveats", caveat 3).** Independently confirmed: `fullPivLu` and `[Dd]eflat` both return hits ONLY in `nleps.cpp`. The report is appropriately and explicitly honest about this (it does not overclaim fan-out), and grounds the proposal on (a) ≥3 within-nleps instances, (b) one-time conjugation-pinning value for the NLEPS lowering, and (c) the literature anchor. This is warranted for a `rough-in` (not firm) proposal — flagging here as the dominant scope risk the harvester/level-review must weigh, NOT as a defect. If a future scan finds no second Gram-LU site, the report itself anticipates the harvester may keep `deflate` NLEPS-scoped. Severity: low-as-flagged (the caveat is correctly disclosed; the issue is only that promotion-to-firm should remain gated on either a second observed site or an explicit "NLEPS-scoped is acceptable" verdict).

4. **`lu_solve` is a new, unresolved sub-primitive dependency (§"Open questions", OQ `deflate-needs-small-dense-lu-solve-primitive`).** Verified: the `fullPivLu().solve` Gram-LU sites are real and nleps-local. The report flags this appropriately — distinguishes it from iterative `ksp_solve` and triangular `concepts/trsv.md`, proposes a candidate L1 leaf `lu_solve :: (Matrix[k,k], Vec[k]) -> Vec[k]`, explicitly declines to propose it here (one-pattern-per-invocation), and states it blocks `deflate`'s firm promotion but not the rough-in. No defect; surfacing it as the load-bearing dependency the cycle-planner/meta-phase must migrate before `deflate` can firm.

5. **skill-uptake telemetry gap — whole report.** No skill invocation referenced despite `classify-variant-axis` (both-modes analysis) and the citation/rotation-verify skills being on-point. Non-blocking surface only. Severity: informational.

## Repair

### Fixes attempted

- **Finding 1 — D3 instance-header line range over-wide (`:663-668`).**
  - **Decision**: repaired.
  - **Action**: Reconciled the main-prose D3 citation to the evidence-block's refined value `:664,:666,:667` in two places — CYCLE.md §"Pattern instances" (Instance D3 header) and §"Instance-counting: both modes" (same-shape mode recap, where D3 was re-cited as `:663-668`). Verified via `read_range` on `palace/linalg/nleps.cpp:660-668`: `:663` is the `BuildParSumOperator(...)` line (preceded by a comment), `:668` is `opJ->AddMult(XSv2, w, 1.0)`; the load-bearing deflation terms are `S = eig·I − H` (`:664`), `XSv2 = MatVecMult(X, Sv2)` (`:666`), `XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2))` (`:667`) — matching the §"Supporting evidence" block exactly. Mechanical range tightening; no claim altered.

- **Finding 2 — reference-anchor line range under-shoots (`:356-362`).**
  - **Decision**: repaired.
  - **Action**: Reconciled the main-prose reference anchor to `:354-362` in CYCLE.md §"Pattern instances" intro, matching the §"Supporting evidence" block. Verified via `read_range` on `palace/linalg/nleps.cpp:352-363`: the Jarlebring 2018 reference begins at `:354` ("Reference: Jarlebring, Koskela, Mele …"), Effenberger 2013 at `:357`; the prior `:356-362` omitted the Jarlebring `:354-355` lines. Mechanical off-by-two extension; no claim altered.

- **Finding 3 — single-algorithm concentration.**
  - **Decision**: not-needed (correctly disclosed as the dominant scope-risk caveat for a `rough-in`; the critic flagged it as low-as-flagged, not a defect). Left as-is.

- **Finding 4 — `lu_solve` new-sub-primitive dependency (OQ).**
  - **Decision**: not-needed (correctly surfaced as the firm-promotion blocker OQ `deflate-needs-small-dense-lu-solve-primitive`; substantive — for cycle-planner/meta-phase migration, not repair). Left as-is.

- **Finding 5 — skill-uptake telemetry gap.**
  - **Decision**: not-needed (pure telemetry surface, non-blocking; the only `warning` check. Authoring a skill-invocation record after the fact is out of repair scope and would be retroactive telemetry). Left as-is.

### Unrepairable findings

None. The two citation findings were mechanical range reconciliations (main-prose to match the report's own refined evidence-block values, both `read_range`-confirmed). The three remaining findings are informational/OQ — correctly disclosed by the producer, requiring no fix.

## Suggested resolution

`ready`. Both citation ranges reconciled to verified values; no live-link or artifact dependency touched (the proposal mutates no chapter files — only two `rough-in` dep-map rows targeting `book/src/L2/index.md:53`). The skill-uptake `warning` is pure telemetry and non-blocking per the critic. Notes for the integrator: this is a proposal-only report (`status: pending`); apply the two `rough-in` dep-map rows to `book/src/L2/index.md` keeping the `gram`/`deflate` forward-refs as plain-text/inline-code (the chapter files do not exist yet — a live link would be a `linkcheck2` error). The OQ `deflate-needs-small-dense-lu-solve-primitive` should be promoted to the open-questions ledger as the load-bearing firm-promotion blocker for `deflate`.

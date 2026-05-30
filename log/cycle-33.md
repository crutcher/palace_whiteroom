# Cycle 033 — L1 firm +2 (`reciprocal` + `elementwise_product` — diagonal-preconditioner-apply shared-vocabulary cohort CLOSED) + L1>L0 firm theme +1 (`jacobi-smoother-mutation-rotation` — the diagonal-preconditioner-apply lowering) + 4 in-cycle live-link upgrades (BATCH-CLOSING THIRD primary cycle of meta-batch-9; batch-9 meta-phase fires AFTER this finalize commit)

**Date:** 2026-05-30 · **Commit:** see git log · **Status:** clean (3 of 3 dispatched-ready reports applied; zero deferrals; zero rejections; zero build-repairs; thirty-first consecutive clean split-integrator cycle)

**Batch position:** cycle-033 is the **THIRD and BATCH-CLOSING** primary cycle of **meta-batch-9** (cycles 031/032/033). **The batch-9 meta-phase fires AFTER this cycle-033 integrator-finalize commit** (3:1 cadence; cycle counter does NOT reset across batch boundaries). This `log/cycle-33.md` + the `scaffolding/integrator-signals.md` cycle-033 BATCH-CLOSING section are the **primary input** the next-firing meta-phase will read.

(Filename note: a `cycle-033.md` from the slice-vertical era already exists; the layered-flow era reclaims the `cycle-33.md` namespace, per the cycle-020→032 precedent. No file rename was needed this cycle — `log/cycle-33.md` did not exist before.)

## Summary

A **substantive, broad-impact** cycle that lands 3 NEW firm artifacts (one L1>L0 theme + two L1 leaves) and closes the diagonal-preconditioner-apply shared-vocabulary cohort end-to-end. The c033 cycle-planner's **deeper deliverable-presence check** (file + `verified_against:` block presence + RESOLVED-grep + gate-block) WORKED — all 3 ready reports were genuinely-open frontier work, contrasting with the c031/c032 planner-staleness pattern. The batch-9 meta-phase (fires after this commit) inherits the cycle-planner-staleness friction codification + the deeper-check enforcement bullet + the skill `verify-dispatch-scope-not-already-discharged` promotion as priority agenda.

## Headlines

- **HEADLINE 1 — L1 firm 23→25 (+2): the diagonal-preconditioner-apply shared-vocabulary chain CLOSED end-to-end.** Two sibling-pair L1 leaves landed firm:
  - `book/src/L1/reciprocal.md` (firm; the elementwise multiplicative-inverse primitive; `reciprocal :: Tensor[N] → Tensor[N]`; `result[i] = 1/x[i]`; complex `1/(a+bi) = (a-bi)/|a+bi|²` Palace-defined at `palace/linalg/vector.cpp:248-261`; real overload via upstream MFEM `mfem::Vector::Reciprocal()` consumed through the `using Vector = mfem::Vector` alias at `palace/linalg/vector.hpp:20`; 8 algebraic laws + 5 explicit non-laws; partial at `x[i] = 0` (no L0 zero-guard; consumer-side SPD `diag(A) > 0` precondition); 4 consumer sites all on the diagonal-preconditioner chain or FE-assembly multiplicity averaging — `palace/linalg/jacobi.cpp:80`, `palace/linalg/chebyshev.cpp:178,241`, `palace/fem/bilinearform.cpp:278`; firm-on-positive-structure per the BLAS-1-leaf / `apply_linop` no-dedicated-test precedent).
  - `book/src/L1/elementwise_product.md` (firm; the Hadamard pointwise-product primitive; `elementwise_product :: (Tensor[N], Tensor[N]) → Tensor[N]`; `result[i] = a[i] · b[i]`; the **diagonal-operator-action primitive at L1** — law 9: `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`; canonical L0 site `BaseDiagonalOperator<OperType>::Mult` at `palace/linalg/operator.cpp:486` real + `:504-505` complex six-fused-multiply-add + `MultHermitianTranspose` `:564-565` complex-only conjugate variant with three sign flips; 10 algebraic laws + 5 explicit non-laws; **two orthogonal variant axes**: element-type `{Real, Complex}` × conjugation sub-axis `{straight, conjugate-first-operand}` on complex-only — single-primitive-with-conjugation-sub-axis modeling justified on operator-own-terms vs. on-disk `dot`/`tdot` two-co-housed-operators precedent).
  - **Together they close the `assemble_diagonal → reciprocal → elementwise_product` chain** that `book/src/L1/assemble-diagonal.md:73` + `book/src/L1/jacobi-smoother.md:289-297` previously forward-referenced as plain text. L1/index `Firm (24)` → `Firm (25)`; SUMMARY-registered; dep-map rows added; all 11 + 11 live cross-links resolved on disk.

- **HEADLINE 2 — L1>L0 firm theme +1: `jacobi-smoother-mutation-rotation` — the diagonal-preconditioner-apply lowering.** `book/src/L1-L0/jacobi-smoother-mutation-rotation.md` landed firm (~640 lines, 33 citations clean, 4 structural sub-patterns A/B/C/D — sub-pattern A diagonal-prep chain `dinv = AssembleDiagonal(); dinv.Reciprocal(); dinv *= ω` setup-body lift; sub-pattern B `Mult` apply-body lift via the namespace-local `Apply(dinv, x, y)` kernel; sub-pattern C the `omega == 0.0` spectral-radius `GetLambdaMax` adaptive-damping sub-action; sub-pattern D `SetOperator` rebuild-on-operator-change). Lowers cleanly to the cycle-033-landed L1 primitives `reciprocal` + `elementwise_product` + the firm `assemble-diagonal-mutation-rotation` setup chain. The diagonal-preconditioner-apply L1>L0 chain now lowers end-to-end. SUMMARY-registered + L1-L0/index dep-map row added between nleps-eigenvalue-correction-mutation-rotation and minres-iteration. Two follow-up OQs filed: `jacobi-smoother-mutation-rotation-reciprocal-elementwise-product-live-link-upgrade` (RESOLVED in-cycle, see HEADLINE 3) + `jacobi-mutation-rotation-dead-code-complex-transpose-kernel-lowering-verifier-audit` (same family as the chebyshev sibling dead-code kernels; cycle-034+ lowering-verifier audit candidate).

- **HEADLINE 3 — 4 in-cycle live-link upgrades (`upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill).** Per the cycle-022/c024/c029 precedent, `integrator-finalize` upgraded the 4 plain-text references to `reciprocal` / `elementwise_product` in the jacobi-smoother-mutation-rotation theme at chapter lines 81, 432-439, 446-449, 590-600 — now that D2/D3 of THIS cycle landed those L1 leaves on disk. The cleanest interpretation closed not just the bare-backtick→live-link swap but also the meta-prose ("Not yet authored", "recorded here as plain text") that was now stale. Closes OQ `jacobi-smoother-mutation-rotation-reciprocal-elementwise-product-live-link-upgrade` in one cycle (opened c033 D1, resolved c033 finalize).

- **HEADLINE 4 (process) — Cycle-planner deeper-deliverable-presence check WORKED this cycle (contrast c031/c032).** The c033 planner ran the deeper check (file existence + `verified_against:`-block presence + RESOLVED-grep + gate-block) for every dispatch candidate. Result: all 3 dispatched targets were GENUINELY-open frontier work (the jacobi-MR theme had no theme file on disk; `reciprocal` had no L1 chapter; `elementwise_product` had no L1 chapter; none had `verified_against:` blocks; no gate-blocks). This is the c033 contribution to the batch-9 planner-staleness signal-dump: the c031/c032 stale-recruitment friction has a working repair (the deeper check), and the batch-9 meta-phase agenda is to codify this as friction-ledger + skill + role-spec ENFORCEMENT bullet.

## Layer-stack counts (verified on disk this cycle)

| Layer | Count |
|---|---|
| L0 | 22 chapters |
| L1 | **25 firm** (**+2: `reciprocal`, `elementwise_product`**) + 2 rough-in (test-coverage-bounded) + 6 rough-in (obstruction) |
| L1>L0 | 28 theme files = **22 firm (+1: `jacobi-smoother-mutation-rotation`)** + 2 rough-in + 1 partly-constructive + 3 obstruction |
| L2 | 9 firm + 1 partly-constructive + 0 stub |
| L2>L1 | 8 = 7 firm + 1 partly-constructive |
| L3 | 9 firm + 2 partial-obstruction |
| L4 | 4 firm |
| Phase-1 removals | 9/10 (sparse_triangular_solve retained-by-design per c031 DEFER verdict) |

**Batch-9 net**: L1 firm 22→25 (+3 across the batch: jacobi-smoother c032 + reciprocal + elementwise_product c033); L1>L0 firm themes +1 (jacobi-smoother-mutation-rotation c033) + 2 additive `verified_against:` audits (ls-update-column c031, back-solve c032); 7 in-cycle live-link upgrades (3 c031 + 4 c033); Phase-1 corpus stays 9/10; 29th/30th/31st consecutive clean cycles.

## Build

`cargo make book` exit 0 in ~88 seconds, **zero build-repairs**. The 3 NEW chapters (`book/src/L1-L0/jacobi-smoother-mutation-rotation.md`, `book/src/L1/reciprocal.md`, `book/src/L1/elementwise_product.md`) + SUMMARY entries at `:89/:90/:105` + L1/index Firm-count bump 23→25 + L1/index `## Vocabulary cohort` cohort-bullet appends (after `jacobi-smoother` for reciprocal, after `reciprocal` for elementwise_product) + L1/index dep-map row appends (after `jacobi-smoother` for reciprocal, after `reciprocal` for elementwise_product) + L1-L0/index dep-map row insert between nleps-eigenvalue-correction-mutation-rotation and minres-iteration ALL SUMMARY-registered + link-clean + parse-clean. The 4 in-cycle live-link upgrades in jacobi-MR theme resolve (both `../L1/reciprocal.md` + `../L1/elementwise_product.md` targets on disk). Build warnings: only the 3 pre-existing KaTeX `Potential incomplete link` false-positives confined to `design/l4_calculus.md` + `concepts/plane-rotation-stream.md`, NONE introduced this cycle.

## Gate results (safety-net)

- retroactive-budget global: **0** (well under the ≥4 block threshold)
- implied-component-stub-created: 0 (not needed; the harvest-preferred-over-stub decision per c032 OQ was correctly enacted; both L1 primitives landed firm directly)
- **in-cycle-live-link-upgrade: 4** (the jacobi-smoother-mutation-rotation theme `reciprocal` + `elementwise_product` plain-text → live-link upgrades at :81/:432-439/:446-449/:590-600; precedent c022/c024/c029)
- SUMMARY-registration auto-fix: 0
- path-hygiene repair: 0
- yaml-leading-quote-of-either-kind repair: 0 (the c030 codified rule held through batch-9 closing)
- yaml-basename-AMBIG repair: 0
- citation-validity repair: 0
- cross-reference-integrity repair: 0
- staging-completeness: **3/3** rows == 3 dispatched-ready reports (no gap — fourteenth consecutive cycle)
- commit atomicity: single commit + push
- consumed-report frontmatter integrity: 3 `integrated_at` touches

## Open questions promoted (cycle-034+ routing)

- **`jacobi-mutation-rotation-dead-code-complex-transpose-kernel-lowering-verifier-audit`** — abstractor-filed; same family as the chebyshev sibling dead-code kernels (`palace/linalg/jacobi.cpp:61-69` conjugate-`dinv` Hermitian-transpose kernel unreachable under the symmetric `MultTranspose → Mult` wiring). Thin verdict-only lowering-verifier sweep. Low-fan-out housekeeping.
- **`reciprocal-l1-mfem-upstream-behaviour-pinning`** — harvester-filed; out-of-focus per CLAUDE.md upstream-citation policy. Re-open only if a future consumer surfaces a behaviour-sensitive claim (NaN/Inf propagation specifics, alignment, etc.). Low-fan-out.
- **`reciprocal-l1-l0-mutation-rotation-theme`** — harvester-filed; the L1>L0 lowering for the new `reciprocal` leaf. Abstractor dispatch candidate cycle-034+. Possibly composite with `elementwise-product-mutation-rotation` (the two leaves share the in-place-receiver-overwrite L0 mutation shape and differ only in the scalar kernel — natural single-theme co-authoring). Precedent: `ksp-solve-mutation-rotation` thin-theme. Fan-out: medium (the two leaves are consumed across the diagonal-preconditioner cohort).
- **`elementwise-product-l1-l0-mutation-rotation-theme`** — harvester-filed; the L1>L0 lowering for the new `elementwise_product` leaf. Abstractor dispatch candidate cycle-034+. See `reciprocal-l1-l0-mutation-rotation-theme` — composite authoring recommended.
- **`elementwise-product-apply-linop-diagonal-operator-round-trip-law-9-cross-reference`** — harvester-filed; informational; the law 9 identity `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)` becomes a cross-operator identity once `assemble-diagonal` is edited to name it. Cross-reference housekeeping for a future `assemble-diagonal` editing pass.
- **`elementwise-product-conjugation-variant-axis-vs-distinct-primitive-decision-record`** — harvester-filed; resolved-by-design; durable methodology-decision record (the single-primitive-with-conjugation-sub-axis modeling vs. the on-disk `dot`/`tdot` two-co-housed-operators precedent decision was made on operator-own-terms — eight non-conjugation-sensitive laws are identical between variants; conjugation modifies only law 1 commutativity and adds law 10 involution). May seed a future skill if the pattern recurs.

## Open questions closed in-cycle

- **`jacobi-smoother-mutation-rotation-l1-l0`** — RESOLVED (firm theme IS the resolution; cycle-032-routed TOP follow-up discharged).
- **`reciprocal-and-elementwise-product-l1-primitives`** — RESOLVED (firm L1 leaves ARE the resolution; cycle-032-routed stub-or-harvest decision discharged via harvester preference per CLAUDE.md `Lower-level shared vocabulary takes priority`).
- **`jacobi-smoother-mutation-rotation-reciprocal-elementwise-product-live-link-upgrade`** — RESOLVED (4 in-cycle live-link upgrades landed by integrator-finalize per the `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill; closes in one cycle, opened c033 D1 + resolved c033 finalize).

## Routed follow-ups for cycle-034+

- **(`abstractor`, `reciprocal-mutation-rotation` + `elementwise-product-mutation-rotation` L1>L0 themes)** — cycle-034+ candidate; possibly composite single theme; the two leaves share the in-place-receiver-overwrite L0 mutation shape.
- **(`lowering-verifier`, jacobi-MR dead-code complex-Transpose Hermitian-kernel audit)** — cycle-034+ thin verdict-only sweep; same family as the chebyshev sibling dead-code kernels.
- **(`combinator-miner`, `polynomial-smoother` L2 combinator from `jacobi` + `chebyshev` + `richardson`)** — cycle-034+ DEFERRED candidate; awaits a third firm sibling (`richardson` is missing); NOT a c034 dispatch — flagged for future when richardson firms.
- **(cycle-planner ENFORCEMENT — c031/c032/c033 batch-9 signal)** — the deeper deliverable-presence check (file + `verified_against:`-block + RESOLVED-grep + gate-block) is the canonical pattern; the batch-9 meta-phase agenda promotes a skill + role-spec ENFORCEMENT bullet.

## Batch-9 meta-phase agenda (fires AFTER this finalize commit)

- **(a)** adjudicate friction-ledger candidate `cycle-planner-stale-priorities-line-recruitment` — **RECURRENCE NOW IN BOTH c031 AND c032 within batch-9** (strong evidence); c033 demonstrated the **fix** (the deeper deliverable-presence check WORKED — 3/3 genuinely-open); the batch-9 meta-phase should (i) codify the friction-ledger entry with the deeper-check as `addressed-by` repair path, (ii) promote skill `verify-dispatch-scope-not-already-discharged` per the c032 OQ + the c033 working precedent, (iii) consider a cycle-planner role-spec ENFORCEMENT bullet for the hard pre-dispatch check.
- **(b)** carry-forward: friction-ledger candidate `negative-result-slice-canonical-instance-blocks-reduction` (filed c031; needs CLAUDE.md §Phase-1-corpus-reduction amendment + skill checklist line + friction-ledger entry; the `sparse_triangular_solve` precedent + `polynomial_recurrence_step` precedent jointly establish the design-exception class).
- **(c)** evaluate carry-forward routing for c034: (i) `reciprocal-mutation-rotation` + `elementwise-product-mutation-rotation` L1>L0 themes (possibly composite); (ii) jacobi-MR dead-code complex-Transpose Hermitian-kernel lowering-verifier audit; (iii) `polynomial-smoother` L2 combinator awaits richardson sibling (NOT a c034 dispatch — flagged for future).
- **(d)** standing intake→plan migration pass: 6 new OQs filed this cycle (cycle-034+ routing); migrate the actionable ones into `priorities.md` per fan-out.

## Cycle character

THIRD and BATCH-CLOSING primary cycle of meta-batch-9 (cycles 031/032/033; meta-phase fires AFTER this finalize). Thirty-first consecutive clean split-integrator cycle. 3/3 dispatched-ready reports applied clean. NO crash this cycle. Build clean, zero build-repairs, all warnings pre-existing KaTeX false-positives. **Substantive frontier-broadening cycle**: 3 NEW firm artifacts close the diagonal-preconditioner-apply shared-vocabulary cohort end-to-end (1 L1>L0 theme + 2 L1 leaves), demonstrating the cycle-009-codified `Lower-level shared vocabulary takes priority` invariant being actively discharged. **Process signal**: c033's deeper deliverable-presence check WORKED, contrasting cleanly with c031/c032 planner-staleness — this is the c033 contribution to the batch-9 signal-dump, arguing for friction-ledger codification of the friction + skill promotion + role-spec ENFORCEMENT bullet at the batch-9 meta-phase. **Batch-9 net**: L1 firm 22→25 (+3); L1>L0 firm themes +1; +2 additive `verified_against:` audits; +7 in-cycle live-link upgrades; Phase-1 corpus stays 9/10. The batch-9 meta-phase agenda is set, the artifact is build-clean, and the cycle-034+ routing is itemized.

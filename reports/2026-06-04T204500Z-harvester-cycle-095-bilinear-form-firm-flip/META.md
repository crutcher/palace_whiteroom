---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T210000Z
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

# META: verification of cycle-095 D1 — flip `bilinear-form` rough-in→firm (HARD-gate-new typed frontmatter + within-file re-anchor + L1/index count-owner)

## Critique

### Checks run

**citation-validity — pass.** `python3 tools/citecheck/citecheck.py --scan` on the report returns `13 ok, 0 failing`. The load-bearing pinpoints were anchor-confirmed mechanically: `palace/linalg/operator.cpp:621-639 --anchor 'Dot'` → `[ok]` (anchors at 621/628/631/637, in range, exactly as the report states at CYCLE.md:198); `boundarymodeoperator.cpp:85 --anchor 'Bttr'` → `[ok]`; `:90 --anchor 'Atn'` → `[ok]`; `nleps.cpp:675 --anchor 'Dot'` → `[ok]`. The two firm-dependency-law cross-refs in the `verified_against:` block were read on disk and back the report's claims: `dot.md:65-66` are dot's law 6 (Hermitian symmetry) + law 7 (conjugate-linearity-left), correctly cited as the inherited sources for bilinear-form laws 1 and 7; `apply_linop.md:50-55` are apply_linop's laws 1/5/6, correctly cited as the sources for bilinear-form laws 2 and 3. `verified_against:` YAML round-trip sub-check: the block (`bilinear-form.md:473-511`) is left UNTOUCHED by this dispatch (CYCLE.md:204 — explicit), and the report introduces no new fenced/payload YAML, so no round-trip failure surface exists; the existing block was authored c092 and is unchanged.

**surface-or-evidence — pass.** This is a maturity-flip of an existing operator (refinement-shaped) with rotation/firmness evidence: the firm conclusion rests on the c092 `lowering-verifier` DISCHARGE probe (`reports/2026-06-04T065200Z-lowering-verifier-cycle-092-bilinear-form-probe/`) + the named firm-on-positive-structure escape precedents (`apply_linop`, `eigenfreq_qfactor_reduce` c082, `sparameter_reduce` c083, `solve_family` c086, `matrix-weighted-norm` c091). The report does modify surface (the §Status / §Context / §Dependencies conclusion prose + the index cells) and the change is evidence-backed, not a bare claim. Record-definition sub-check: the signature names `Tensor` / `LinearOperator` / `Scalar` — all shared L1 primitive types, no operator-local config/state record introduced; `LinearOperator[M, N]` is defined in `apply_linop`'s chapter and merely referenced here. The obligation correctly no-ops (CYCLE.md:191) — no record named in the signature lacks a definition home.

**rotation-quality — pass (not applicable to a same-layer firm-flip).** The report asserts no L_{n+1}→L_n algebraic/structural rotation of its own; it is an L1-internal maturity promotion. The check no-ops.

**variant-axis-coverage — pass.** The operator's four axes are carried (precision-mode / output-arg-pattern / M-symmetry-property / parallel-wrapper). The material axis (M-symmetry-property) is explicitly covered: laws 7/8 are stated conditionally with both branches positively witnessed on disk (Hermitian `Bttr` `boundarymodeoperator.cpp:85`, non-Hermitian `Atn` `:90`). The one unexercised shape (real-`M`-real-`y` `xᵀ M y`) is explicitly scoped out as "not surfaced by Palace at all" — a deliberate scope-out, not a hidden branch. The narrow-coverage gate is reasoned-redundant under the escape, not silently dropped.

**cross-reference-integrity — pass.** All four typed-edge targets resolve on disk: `book/src/L1/dot.md`, `book/src/L1/apply_linop.md`, `book/src/L1/matrix-weighted-norm.md` (the three `depends-on`), and `book/src/L1-L0/bilinear-form-mutation-rotation.md` (the `reference`). `bilinear-form` is registered at `book/src/SUMMARY.md:176` — confirmed; a flip needs no SUMMARY edit. The rank invariant is mechanically satisfied: all three `depends-on` deps read `firm` on disk — `dot.md:100` `firm`, `apply_linop.md:87` `firm`, `matrix-weighted-norm.md:110` `firm` (promoted c091) — so `rank(bilinear-form=3) ≤ min(3,3,3)` holds; the `reference:` edge to the L1>L0 theme constrains nothing per scheme §2. The typed `rank:`/`edges:` frontmatter is well-formed per `graded-stack-scheme.md` §1 (the `firm` rank token), §2 (the `edges:` block with `depends-on:`/`reference:` buckets, bare-string form ≡ `{target}`), and §4(a) (the `depends_on:` + `lowers_to:`/`lifts_from:` supersession is the documented 1:1 migration). The L1/index count arithmetic is correct against on-disk reality: `index.md:31` currently reads "**31 main cohort; 38 firm grand total**" and "31 main + 4 FE-assembly + 3 FE-space = 38"; the flip to 32 main / 39 grand is the correct +1, and matches the planner estimate the report cites (CYCLE.md:199).

**edge-label-fidelity — pass (not applicable).** No cross-layer edge label is asserted. The one cross-layer pointer is the `reference: L1-L0/bilinear-form-mutation-rotation` navigational edge; the report's prose (CYCLE.md:62, :205) discusses exactly that L1>L0 theme relationship and correctly classifies it `reference` (navigational), not `depends-on` (per scheme §2 a theme pointer is a reference).

**plan-kind-consistency — pass.** The declared kind (firm-flip of an L1 operator) matches the content: the report flips `firmness` to `firm` + `rank: firm`, restates every "rough-in"/"stays rough-in by design"/"firm-promotion-eligible" conclusion as ENACTED, and carries no rough-in placeholders in the promoted entry. The §Status escape-argument numbered points (probe points 1-3) are correctly left as the discharge substrate; only their framing paragraph flips. No mis-classification.

**skill-uptake-survey — pass (telemetry).** The report exercises the citation tooling correctly (`citecheck --anchor 'Dot'` on the load-bearing range, CYCLE.md:198). The firmability basis is the c092 `lowering-verifier` dischargeability probe (the `foundation-blocker-dischargeability-probe` shape promoted this batch); the report references it as the DISCHARGE provenance. No skill whose shape this report implies is left un-invoked.

### Within-file self-consistency re-anchor (task focus (c)) — COMPLETE

Grepping `book/src/L1/bilinear-form.md` for `rough-in | remains open | stays rough | firm-promotion-eligible | below firm` returns 10 hits. Each is accounted for: the four stale-CONCLUSION sites are all covered by a proposed edit — `:4` (frontmatter, edit 1), `:45` ("is a **rough-in** rather than firm", §Context edit), `:255` ("the `bilinear-form` half remains open", §Dependencies edit — the named `:251-257` risk, explicitly discharged at CYCLE.md:84-93), `:323` (§Status opener token, §Status edit), `:368` ("stays `rough-in` ... by design", §Status gate-(c) edit), `:386-387` ("firm-promotion below firm / firm-promotion-eligible", cycle-010 repair-note edit). The three SURVIVING hits are legitimately retained non-conclusions: `:253` and `:468` are the OQ slug name `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` (a proper noun), and `:331` is a citation of the CLAUDE.md `rough-in (test-coverage-bounded)` methodology bullet (naming the escape, not concluding rough-in). The batch-29 zero-within-file-stale-conclusion discipline is satisfied in one pass.

### Issues found

No blocking or warning issues. Two integrator-application notes (NOT check failures — recorded for the integrator-per-report's old_string-fidelity step, well within mechanical-apply scope):

1. **Index sub-list-retirement edit (CYCLE.md:159-163) — old_string is the on-disk `bilinear-form` bullet, not the proposed note text.** On disk the "**Rough-in (test-coverage-bounded)**" sub-list (`index.md:65-67`) contains the full `bilinear-form` bullet as its SOLE member (`matrix-weighted-norm` was already moved out at c091). The report's replacement correctly retires the now-empty list, and its proposed note text (CYCLE.md:162) names BOTH operators accurately, so the resulting prose is correct; the integrator simply matches the on-disk `bilinear-form` bullet (`:67`) as the old_string, not a pre-existing "empty" note. Pre-existing on-disk wrinkle the flip incidentally RESOLVES: the operator sat in the `test-coverage-bounded` sub-list while its §Status / dep-map cell carried the `lower-layer-shared-vocabulary` qualifier — both flip to `firm`, ending the mismatch.

2. **§Status opener edit (CYCLE.md:97-116) spans `:321` through the fence before the "1." numbered list (`~:333`), not only `:321-326`.** The new_string ends at the ` ``` ` fence opening the discharge-argument list, preserving the numbered escape points (probe points 1-3, `:334-366`) verbatim as the report intends (CYCLE.md:206). A clean multi-line block replacement; flagged only so the integrator applies the full block, not a `:321-326`-only slice.

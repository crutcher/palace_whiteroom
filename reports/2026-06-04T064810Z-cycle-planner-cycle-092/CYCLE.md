---
agent: cycle-planner
invoked_at: 2026-06-04T064810Z
scope: cycle-092 dispatch plan
status: pending
---

# Cycle 092 dispatch plan

## Goals selected this cycle

cycle-092 is the **2nd primary cycle of meta-batch-29** (cycles 091/092/093; the batch-29
meta-phase fires after cycle-093's finalize). Substantive forward-frontier work is in scope
(NOT the land-clean cycle — that is c093). The c091 LEAD (matrix-weighted-norm firm-flip +
~30-file cascade) landed clean; the convergent foundation-blocker for the 4 stay-seed
driver/output-product columns (capacitance/inductance/electrostatic/magnetostatic) has now
collapsed onto a **single primitive: `bilinear-form` firming** (the sole residual gate on
`gram_reduce`, the diagonal `matrix-weighted-norm` gate having discharged c091).

This cycle takes the **highest-fan-out next-gate question** — is `bilinear-form` cleanly
firmable, or is its rough-in a genuine ceiling? — and dispatches the **cheap dischargeability
probe FIRST** (the c088/c089 matrix-weighted-norm pattern), NOT a heavy firm-flip wave. The
on-disk investigation (below) shows `bilinear-form`'s rough-in is a **narrow-variant-axis /
law-confidence gate, NOT a structural ceiling** — all three constituents are firm, the laws
are inherited from them, and the firm-on-positive-structure escape is directly applicable. The
probe judges DISCHARGE-vs-CONFIRM-CEILING and does NOT force-firm and does NOT trigger any
cascade; the firm-flip + 4-column unblock cascade is a SEPARATE gated wave (a c093 land-clean
candidate IF the probe DISCHARGEs cheaply, or a batch-30 LEAD).

## On-disk verdict on `bilinear-form` firmability: CLEAN PROBE AVAILABLE (likely DISCHARGE)

Read `book/src/L1/bilinear-form.md` in full + codemap-confirmed every cited L0 anchor. Verdict:
**`bilinear-form`'s rough-in is NOT a structural ceiling — it is the exact `matrix-weighted-norm`
situation, and arguably cleaner.** A scoped `lowering-verifier` dischargeability probe is the
right first move (the c088/c089 pattern). Findings:

1. **WHY rough-in (the EXACT reason, from `book/src/L1/bilinear-form.md:321-346`):** the §Status
   gives exactly ONE gating reason — **"Narrow variant-axis coverage from Palace's two surfaced
   use sites"** (Poynting-power boundary integral; NLEPS Newton denominator), neither exercising
   the real-`M`-real-`y` shape and Cauchy–Schwarz at `y=x` unexercised. This is a
   **law-confidence / test-coverage gate**, structurally analogous to `matrix-weighted-norm`'s
   `rough-in (test-coverage-bounded)` — NOT structural incompleteness, NOT an un-anchored
   constructive sub-part, NOT a fold of something rough-in. The §Status explicitly notes the
   structural signature IS anchored at L0 and the laws inherit cleanly from the firm deps. (An
   earlier alleged SECOND gate — an L0 conjugation comment-vs-impl disagreement — was already
   DISPROVEN and removed `:336-346`; the L0 source is self-consistent, `yᴴ A x` comment matches
   the impl, OQ `bilinear-form-conjugation-convention-anchor` verified it.)

2. **Constituents are ALL firm (a reduction/form is as firm as its least-firm constituent):**
   - `dot` — **firm** (`book/src/L1/dot.md` §Status: "firm — signatures are canonical, evidence
     is direct... standard sesquilinear/bilinear facts modulo FP caveats").
   - `apply_linop` — **firm** (`book/src/L1/apply_linop.md` §Status: "firm — signature is
     canonical... standard properties of linear maps modulo FP caveats").
   - `matrix-weighted-norm` — **firm c091** (its own SPD-restricted `y=x` sibling; the diagonal
     case `bilinear_form(x, M, x)`).
   No constituent blocks. `bilinear-form` depends on `apply_linop` + `dot` (`depends_on:` frontmatter
   `:7-9`), both firm.

3. **The laws qualify for the firm-on-positive-structure escape (SIMPLER than mwn):** laws 1-6
   (`book/src/L1/bilinear-form.md:182-201` — conjugate-linearity in `x`, linearity in `y`,
   operator-side bilinearity, zero-vector/zero-operator annihilation, identity-weight
   specialisation `bilinear_form(x, I, y) = dot(x, y)`) are **pure syntactic-algebraic
   consequences** of the firm `dot` + `apply_linop` linearity — direct identity content, NOT
   norm-axiom theorems. This is materially CLEANER than `matrix-weighted-norm` was: mwn's gating
   laws were inner-product-NORM-axiom THEOREMS (triangle/Cauchy–Schwarz/parallelogram) that the
   c080 D1 audit ruled were NOT syntactic identities (needing the SPD premise + the structure-side
   probe c088 + the FP-side probe c089, two probes). `bilinear-form` has NO norm-axiom theorem
   content — its laws 7/8 (Hermitian symmetry, PSD at `y=x` for SPD `M`) are **conditional**,
   guarded on M-symmetry, WITH on-disk witnesses for both branches (`Bttr` Hermitian + `Atn`
   non-Hermitian, `boundarymodeoperator.cpp:85`/`:90`, both codemap-confirmed this cycle).

4. **L0 structural anchors codemap-confirmed exactly this cycle** (`mcp__palace-codemap__read_range`):
   - `palace/linalg/operator.cpp:621-639` — both overload bodies (real-`A`: split real/imag,
     apply `A` to each, `Dot(comm, Ax, y)`; complex-`A`: `A.Mult(x, Ax)`, `Dot(comm, Ax, y)`).
     **CONFIRMED verbatim.**
   - `palace/linalg/operator.hpp:385-394` — two decls + the `// Compute the bilinear form inner
     product yᴴ A x` comment. **CONFIRMED verbatim.**
   - The two use sites: `boundarymodeoperator.cpp:85` (`linalg::Dot(comm, et, *Bttr, et)` —
     Hermitian) + `:90` (`linalg::Dot(comm, en, Atn, et)` — non-Hermitian). **CONFIRMED.**
   - `get_call_sites`/`search_text` of the matrix-weighted `linalg::Dot(comm,x,A,y)` overload
     across the WHOLE tree returns **exactly 2 hits** (both `boundarymodeoperator.cpp`). The
     "narrow variant-axis coverage" gate is **on-disk-accurate** — exactly 2 call sites exist.
   - `nleps.cpp:675` is the UNWEIGHTED 3-arg `Dot(GetComm(), w, w0)` — the chapter is precise
     ("the surrounding context computes weighted variants by composing apply_linop with dot").
   - **No `test/unit/*` exercises the matrix-weighted `Dot` overload** (codemap-confirmed: the
     `test/unit/*bilinearform.hpp` hits are the FEM `BilinearForm` assembly class, a DIFFERENT
     thing). So the direct-test promotion route is genuinely absent — exactly mirroring mwn's
     gate (a).

**Dischargeability probe shape (the LEAD, D1):** a scoped `lowering-verifier` law-confidence
probe judging whether the firm-on-positive-structure escape APPLIES — laws 1-6 are
syntactic-identity consequences of firm `dot`+`apply_linop` (no positive √/test gate, the
`apply_linop`/`solve_family`/`matrix-weighted-norm` precedent); laws 7/8 are conditional with
both M-symmetry witnesses on-disk; the narrow-coverage gate is the "missing test does not gate
syntactic-identity laws" situation. TWO clean outcomes: **(a) DISCHARGE** — escape applies →
`verified_against:` block + §Status narrows, the verb is firmable → queue the firm-flip +
4-column cascade as a gated c093/batch-30 wave; **(b) CONFIRM-CEILING** — a genuine positive
test the corpus lacks gates law 7/8 (e.g. the non-Hermitian asymmetry needs a witness the 2
sites don't give) → explicit-verdict §Status note, stays rough-in (the ceiling is itself the
load-bearing finding). The probe does NOT force-firm and does NOT trigger the cascade regardless
— the c088/c089 discipline.

## Deliverable-presence verification

Per the MANDATORY paste-inline-evidence procedure. The single named-artifact-slug scope is D1
(`book/src/L1/bilinear-form.md`).

**D1 — `bilinear-form-firmability-dischargeability-probe` (touches `book/src/L1/bilinear-form.md` ONLY):**
1. **File existence:** `ls -la book/src/L1/bilinear-form.md` → `-rw-rw-r-- ... 24177 Jun 3 23:15
   book/src/L1/bilinear-form.md` / `EXIT: 0`. **PASS — file present.**
2. **Maturity / already-discharged:** Status line read on disk = `firmness: rough-in` (frontmatter `:4`)
   + `` `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)` `` (§Status `:323`). The
   probe's deliverable (a firmability VERDICT + `verified_against:` audit OR explicit-ceiling note)
   is NOT at-or-below this maturity — the operator carries ZERO audit blocks. **PASS — not a no-op.**
   `grep -c '^verified_against:' book/src/L1/bilinear-form.md` → `0`. **No prior audit closes it.**
3. **OQ-ledger RESOLVED-grep:** `grep -i 'bilinear-form.*RESOLVED\|bilinear-form.*CLOSED'
   scaffolding/open-questions.md` → the only hits are (i) the `matrix-weighted-norm` cascade
   prose, (ii) the **L1-L0 THEME** `bilinear-form-mutation-rotation-l1-l0-theme-needed-c028`
   RESOLVED c029 (a DIFFERENT artifact — the lowering theme, firm; explicitly notes "the L1
   `bilinear-form` OPERATOR stays rough-in per its own independent gate"), (iii) the
   `fe-assemble-slug-collision-with-bilinear-form` RESOLVED-in-report (a naming disambiguation).
   **NONE closes the L1 `bilinear-form` operator FIRM question.** **PASS — genuinely open.**
4. **Structural-block check:** the gate is `rough-in (lower-layer-shared-vocabulary,
   cycle-010-wave-1)` = a narrow-variant-axis / law-confidence gate (NOT `partial-obstruction`,
   NOT `obstruction (opaque-library-ownership)`, NOT `rough-in (test-coverage-bounded)` with an
   absent-upstream-test hard block). The firm-on-positive-structure escape (CLAUDE.md
   §Methodology invariants, the `rough-in (test-coverage-bounded)` bullet) is the relevant gate
   and it is DISCHARGEABLE by a verifier pass (the `matrix-weighted-norm` c088/c089 →
   batch-28-GO precedent is the exact prior). **PASS — no unchanged methodology block; this is
   precisely the probe class the redirect arc validated.**

**STOP-PROPOSING negative-list check:** `bilinear-form` is NOT on the list (`lu_solve`,
`back_solve`, `ls-update-column`, 4 NLEPS atoms, `apply_nonlinear_pencil` HELD,
`polynomial_smoother`, `L3/solve_family`, `L2/fold_solve`, `L2/fe_assemble`, `weak_form_term`
L2 floor, `map_solve` shared-generalization). `grep -i 'bilinear-form' scaffolding/priorities.md
| grep STOP` → no match. **CLEAR.**

**Framing check (audit-first vs reflexive-harvest):** the probe is correctly framed as an
**audit-first `lowering-verifier` dischargeability probe** (the c088/c089 precedent), NOT a
reflexive `harvester` firm-flip — because the question is "does the escape APPLY" (a
representation/law-confidence judgment at a foundation-blocker), and the two-clean-outcome
discipline (DISCHARGE / CONFIRM-CEILING, no forcing) is the verifier's job. The c091 finalize
suggested a `harvester` "firm-flip / law-confidence pass" — but the redirect-arc lesson
(batch-25→28) is that a SCOPED verifier PROBE is the right FIRST move on a high-fan-out
foundation-blocker, NOT a firm-flip that pre-commits the maturity. Routing to `lowering-verifier`.

## Dispatches

1. **agent:** `lowering-verifier`
   **scope:** `bilinear-form-firmability-dischargeability-probe` — touches `book/src/L1/bilinear-form.md`
   ONLY. A scoped law-confidence probe on the L1 `bilinear-form` operator's promotion-to-firm
   question. Judge whether the **firm-on-positive-structure escape** applies: (i) laws 1-6
   (`:182-201`) are syntactic-identity consequences of the firm constituents `dot`
   (`book/src/L1/dot.md` firm) + `apply_linop` (`book/src/L1/apply_linop.md` firm) + the firm
   `matrix-weighted-norm` diagonal sibling (c091) — the "missing test does not gate
   syntactic-identity laws" situation; (ii) laws 7/8 (`:205-220`, Hermitian symmetry + PSD at
   `y=x`) are CONDITIONAL with both M-symmetry witnesses on-disk (`Bttr` Hermitian
   `boundarymodeoperator.cpp:85` + `Atn` non-Hermitian `:90`, codemap-confirmed); (iii) the
   `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)` narrow-variant-axis gate (§Status
   `:321-335`) is a law-confidence gate, not structural incompleteness. **TWO clean outcomes:**
   (a) **DISCHARGE** — the escape applies (laws are syntactic identities on firm constituents +
   the conditional laws have their witnesses) → append a `verified_against:` block + narrow the
   §Status to the discharge record (verb is firmable; queue the firm-flip-and-cascade as a gated
   c093/batch-30 wave); (b) **CONFIRM-CEILING** — a genuine positive test the 2-site corpus lacks
   gates law 7/8 (record the explicit verdict in §Status; stays rough-in — the ceiling is the
   finding). **HARD CONSTRAINTS:** do NOT flip the verb to `firm` in this dispatch regardless of
   outcome (the probe is the gate-test, the firm-flip is a separate gated wave — the c088/c089
   discipline); do NOT touch the ~26-file `bilinear-form` cross-reference cascade; do NOT touch
   `gram_reduce`/`domain_energy_reduce`/any feature column; do NOT touch the L1>L0 theme (firm);
   touch ONLY the operator's own §Status + (on DISCHARGE) a `verified_against:` YAML block. Cite
   the `matrix-weighted-norm` c088 structure-side + c089 FP-side discharge → batch-28-GO as the
   directly-applicable prior (the convergent-blocker dischargeability-probe pattern), and the
   `apply_linop`/`solve_family`/`eigenfreq_qfactor_reduce` firm-on-positive-structure escape
   precedents. Note that `bilinear-form` is CLEANER than mwn (no norm-axiom theorem content; pure
   linearity laws). L0 anchors codemap-confirmed: `operator.cpp:621-639`, `operator.hpp:385-394`,
   `boundarymodeoperator.cpp:85`/`:90`.
   **deps:** none.
   **rationale:** THE LEAD. The single highest-fan-out next-gate question: `bilinear-form` is the
   sole residual gate on `gram_reduce` → which gates 4 stay-seed columns
   (capacitance/inductance/electrostatic/magnetostatic). The cheap dischargeability probe is the
   redirect-arc-validated first move on a high-fan-out foundation-blocker (batch-25→28
   matrix-weighted-norm precedent). fan-out: HIGH (convergent unblock of 4 stay-seed columns +
   `gram_reduce` firming, gated on outcome (a)).

(No second dispatch. See Open questions / caveats for why a manufactured forward-frontier or
hygiene pick is deliberately omitted — the bottom-up width frontier is genuinely light/gated
[c088/c089/c090 all recorded the same], the firm-flip-and-cascade is correctly a SEPARATE gated
wave not bundled with the probe [the c088/c089 discipline], and a rectangular pull-up is
forbidden by the redirect. A single-dispatch substantive-LEAD cycle is the honest plan; the
c088/c089 two-dispatch shape added a LOW/hygiene lifter only because a concrete stale-cross-ref
residue existed — there is no such residue this cycle, the c091 cascade landed clean per the
c091 finalize signals.)

## Overlap analysis

Single dispatch — no pairwise overlap possible. D1 touches `book/src/L1/bilinear-form.md` ONLY
(its own §Status + an optional `verified_against:` block). It does NOT touch any index
(`L1/index.md`, `L4/index.md`, `feature/index.md`), any reduce-verb
(`gram_reduce`/`domain_energy_reduce`), any feature column, the L1>L0 theme, or SUMMARY — so no
shared-index / shared-tally / dual-registration coordination is needed (the parallel-blind-shared-
index guard does not apply at one dispatch). No new-slug forward-reference (the probe authors no
new chapter/theme).

## Sequencing schedule

**Wave 1 (single dispatch):** D1 (`lowering-verifier` bilinear-form-firmability-dischargeability-probe).

One wave. The downstream pipeline is the standard primary cycle: D1 → critic(D1) → repairer(D1
if warn/fail) → integrator-per-report(D1) → integrator-finalize (ONE, at cycle end: rebuild +
commit + push + housekeeping). No forward-reference ordering needed.

## Open questions / caveats

- **The firm-flip-and-cascade is a SEPARATE gated wave, NOT this cycle.** On D1 outcome (a)
  DISCHARGE, the firm flip of `bilinear-form` + the ~26-file cross-reference re-anchor (the
  `bilinear-form` consumers: `gram_reduce` §Status/Folds-cell, the `inner_product` L2 fold, the
  L0 chapters, the feature-column gate prose, the L1/index dep-map + count headers) + the coupled
  `gram_reduce` firm re-judgment (its SOLE residual gate clears → the firm-on-positive-structure
  escape applies exactly as it did for its reduce-verb siblings `domain_energy_reduce` c091 /
  `eigenfreq_qfactor_reduce` c082 / `sparameter_reduce` c083) + the 4-column re-evaluation
  (capacitance/inductance/electrostatic/magnetostatic flip seed→firm under the OWN-COMPOSITION
  rule once `gram_reduce` firms) is a DEDICATED own-cycle structural wave. This is a **c093
  candidate** (c093 is the batch-29 land-clean cycle — a firm-flip-and-cascade is heavier than
  land-clean discipline normally allows, so the batch-29 meta-phase / the c093 planner should
  judge whether to (i) land the cascade c093 if the probe DISCHARGEs cleanly and the cascade is
  describable as a clean coupled wave [the c091 4-dispatch precedent shows a ~30-file cascade CAN
  land clean], OR (ii) defer it to the **batch-30 LEAD**). I have appended it to the plan as a
  CONDITIONAL candidate gated on D1 outcome (a). NOTE: this is the c091-finalize-flagged
  follow-up ("if the full electrostatic/magnetostatic/capacitance/inductance unblock is wanted,
  the next gate after this cascade is `bilinear-form` firming") — now ACTIVE as the c092 probe.

- **For the batch-29 meta-phase (surfaced, not a dispatch):** if D1 DISCHARGEs, the
  `bilinear-form` firm-flip-and-cascade go/no-go is a natural batch-29 meta-phase decision
  (parallel to how the matrix-weighted-norm firm flip was the batch-28 meta-phase headline). The
  meta-phase should weigh whether to enact it as a c093-bundled wave or a batch-30 LEAD, and
  whether the `gram_reduce`/4-column cascade is cleanly describable in one wave.

- **goal-flow stale-ref note (carried from c091 D2 intake, NOT a c092 dispatch):**
  `methodology/goal-flow.md` (meta-phase-owned) carries stale `matrix-weighted-norm` rough-in
  refs the c091 cascade did not touch (flagged-not-edited per write-scope). The batch-29
  meta-phase goal-flow refresh should fold the c091 cascade + (if it DISCHARGEs) the c092
  `bilinear-form` verdict. Recorded so the meta-phase catches it (OQ
  `goal-flow-mwn-firm-flip-cascade-refresh-stale-rough-in-refs`, c091 D2 intake).

- **Single-dispatch cycle is deliberate, not under-planned.** The bottom-up width frontier is
  genuinely gated/light (the c088/c089/c090 reshapes all recorded the same: the
  firm-on-positive-structure route is exhausted for the all-primitives-firm cohort, and the next
  reduce-verb pass is gated on a foundation primitive). The redirect forbids manufacturing a
  rectangular pull-up to fill a slot. The probe is a genuine substantive forward-frontier LEAD
  (the convergent-blocker dischargeability question), which is the correct 2nd-of-batch pick.

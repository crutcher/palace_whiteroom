---
agent: cycle-planner
invoked_at: 2026-06-01T154713Z
scope: cycle-046 dispatch plan
status: pending
---

# Cycle 046 dispatch plan

## Goals selected this cycle

The L0–L3 foundation campaign (cycles 041–045) is COMPLETE — the stack is substantially rectangular through L0–L3 (L2 9→21, L2>L1 7→19, L3>L2 2→17). Per the uniform-pull-up directive, the climb resumes **UPWARD to L4**, now the lowest incomplete layer (only 4 firm L4 operators + 3 firm L4>L3 themes, all on the Krylov chain). Cycle-046 is a **survey-heavy opening cycle of meta-batch-14**: the LEAD item is a pre-survey whose output determines the specific per-operator L4-cap / L4>L3-theme picks, so its concrete harvester/abstractor dispatches carry to cycle-047. Alongside the survey, two fully-independent Medium items run in parallel: materializing the RATIFIED four-root erasure-scope taxonomy as a concept page (canonical write-up already exists in `L3-L2/index.md` §Working-Notes), and a residual-L2>L1-gap audit now that the L2 floor is at 21.

This is a **3-dispatch, single-wave, fully-parallel** plan. No wave-2 harvester/abstractor picks are pre-committed this cycle: the L4/L4>L3 coverage denominator is genuinely unknown until the survey runs (the existing L4>L3 inventory covers only the Krylov chain; whether the other 14+ firm L3 operators warrant an L4 cap vs. lower directly is a fan-out judgment the survey must produce), so pre-committing per-operator picks would risk recruiting work the survey reveals as a no-op or mis-framed. The survey lands its fan-out ranking; cycle-047 dispatches the top picks against it.

## Dispatches

**D1 — (`combinator-miner`, "L4 + L4>L3 coverage pre-survey: enumerate which of the 18 firm L3 operators have an L4 cap, which lack an L4>L3 rotation theme, and fan-out-rank the specific L4-cap / L4>L3-theme picks under the L4 strawman conventions", deps: none)**
- **rationale**: The LEAD frontier `l4-l3-coverage-and-l4-expansion` (Backlog High; uniform-pull-up). Observation/survey only — NO `book/` mutation. The survey produces the coverage denominator the planner needs to fan-out-rank cycle-047's per-operator picks. Concretely it must: (i) enumerate the 18 firm L3 operators (`book/src/L3/*.md` minus index: apply_linop, assemble-diagonal, axpby, axpbypcz, axpy, chebyshev, divfree-projector, dot, eigsolve, elementwise_product, jacobi-smoother, krylov-step, ksp_solve, normalize, nrm2, orthogonalize, reciprocal, scal); (ii) cross them against the 4 firm L4 operators (`chebyshev`, `iterate-while`, `iterate-while-with-prev`, `krylov-step`) to find which L3 operators have an L4 cap and which do not; (iii) cross them against the 3 firm L4>L3 themes (`krylov-step-typed-wrapper-dissolution`, `gmres-inner-loop-iterate-while-migration`, `fgmres-inner-loop-iterate-while-migration` — all Krylov-chain) to find which firm L3 operators lack an L4>L3 rotation theme (the L4>L3 analog of the just-closed L3>L2 gap); (iv) for each gap, judge **whether an L4 cap is warranted at all** (L4 is "vocabulary, not architecture" per `L4/index.md:7` — a BLAS-1 leaf like `dot`/`scal`/`axpy` may have no distinct L4 vocabulary to add, lowering directly, exactly as `apply_linop` is no-L2-by-design; the survey must distinguish "missing L4 cap = real gap" from "no L4 cap by design"); (v) fan-out-rank the warranted picks (the calculus vocabulary the downstream burn-component effort consumes is highest fan-out). Cite the L4 strawman (`book/src/design/l4_calculus.md`) and the two `iterate-while-l3-rendering-trajectory-accumulation-gap` OQ-noted standalone-L4>L3-theme candidates already flagged in `L4/index.md:54-55` (the `iterate-while` / `iterate-while-with-prev` standalone L4>L3 renderings) as a known near-term candidate. Route `combinator-miner` (recurrent-pattern survey across the L4 cohort) — the active head lists `combinator-miner`/`layer-intro-author` as alternatives; `combinator-miner` is the better fit because the deliverable is a cross-cutting coverage/pattern survey + fan-out ranking, NOT a Part-overview/dep-map authoring touch (which would be the `layer-intro-author` framing, premature before the picks are known). Serves `l4-l3-coverage-and-l4-expansion`.

**D2 — (`layer-intro-author`, "author `book/src/concepts/erasure-scope.md` — the RATIFIED four-root erasure-scope taxonomy; fold in the `concepts/sequential-obstruction.md` opaque-library-rooted-marker-vs-Palace-authored-recurrence distinction", deps: none)**
- **rationale**: Backlog High `erasure-scope-taxonomy-concept-page` (batch-13 meta-phase GO). The four-root taxonomy is RATIFIED and the canonical write-up already exists verbatim in `book/src/L3-L2/index.md` §Working-Notes (lines 67-73): (1) **unconditional-single-loop** (`ksp-solve-outer-driver`), (2) **variant-conditional-single-loop** (`orthogonalize-variant-split`), (3) **unconditional-nested-double-loop** (`chebyshev-nested-recurrence`), (4) **opaque-library** (`eigsolve-opaque-eigen-iteration`). The concept page gives the axis a cross-cutting home adjacent to `concepts/sequential-obstruction.md` + `concepts/tensor-field-lift.md`: one-line semantics per root + forward-citations to the four substantive L3>L2 themes + the operators exhibiting each root. **Fold in** the `concepts-sequential-obstruction-opaque-library-marker-distinction` (c045 D1): a `sequential-obstruction` marker rooted in opaque-library-ownership — no Palace recurrence to render — is distinct from a Palace-authored renderable-then-erased recurrence. Route `layer-intro-author` (concept-page authorship, broadened cycle-003). Single dispatch; verified-ABSENT on disk. Serves `erasure-scope-taxonomy-concept-page`.

**D3 — (`cross-layer-cross-cutter`, "residual-L2>L1-gap audit: sweep the 21 firm L2 operators for any lacking an L2>L1 lowering theme now that the L2 floor is at 21; classify each gap as genuine-missing-theme vs no-L2>L1-theme-by-design", deps: none)**
- **rationale**: Backlog High `residual-l2-l1-gap-audit` (batch-13 meta-phase; foundation hygiene). Observation/audit only — NO `book/` mutation; surfaces gaps + a recommendation, the follow-up authoring rides cycle-047 if warranted. The cross-reference (done as part of this plan's deliverable-presence check) shows 21 firm L2 operators and 20 L2-L1 themes (19 + index); every L2 op has a same-named L2>L1 theme **except `krylov-step`** (no `krylov-step`-stemmed L2-L1 file; `L2/krylov-step.md` describes its L1 decomposition in-line via the body + the krylov-step chain). The audit must determine whether `krylov-step`'s missing L2>L1 theme is a **genuine gap** (warranting a `krylov-step`-L2>L1 theme) or a **by-design no-theme case** analogous to `apply_linop` being no-L2-by-design at the L3>L2 edge — `krylov-step` at L4>L3 already has the firm `krylov-step-typed-wrapper-dissolution` theme, and its L2>L1 story may be the in-line body-composition into L1 primitives (`apply_linop`/`axpy`/`dot`/etc.) rather than a dedicated theme. The audit should also confirm no OTHER L2 op has a silently-missing theme (the suffix-stem cross-check found only `krylov-step`). Route `cross-layer-cross-cutter` (the gap is a cross-layer L2↔L1 coverage observation; the active head lists `same-layer-cross-cutter`/`cross-layer-cross-cutter` as alternatives — `cross-layer-cross-cutter` is the right fit because the deliverable is an L2-vs-L2>L1 coverage-gap observation across an adjacent edge). Serves `residual-l2-l1-gap-audit`.

## Overlap analysis

Pairwise:
- **D1 × D2**: D1 surveys L4 / L4>L3 coverage (observation, no `book/` write); D2 authors `book/src/concepts/erasure-scope.md` (a NEW concepts-page file, no overlap with any L4 artifact). Disjoint artifact regions, disjoint operator names. **NON-OVERLAPPING → parallel.**
- **D1 × D3**: D1 surveys L4 / L4>L3 (observation); D3 audits L2 / L2>L1 coverage (observation). Both are observation-only (no `book/` mutation), touch different layers, name different operators. **NON-OVERLAPPING → parallel.**
- **D2 × D3**: D2 authors a concepts page; D3 is an L2/L2>L1 observation. The erasure-scope taxonomy D2 writes references the four substantive L3>L2 themes (L3-L2 layer), not L2>L1 themes; no shared file region, no shared operator. **NON-OVERLAPPING → parallel.**

All three are independent. D2 is the only artifact-mutating dispatch (one new concepts file); D1 and D3 are observation/survey dispatches that produce CYCLE.md findings + (for D1) a fan-out-ranked pick list for cycle-047. No shared running-count / consolidated-tally landing this cycle (D2's concepts page carries no layer-index tally; the `concepts/index.md` registration is a single new row, not a consolidated aggregate), so the **count-ownership / dual-registration partition does not bind this cycle** — there is no ≥2-parallel-landing-into-a-shared-index situation. (Noted for completeness per the standing convention; not applicable here.)

**Floor-landing → same-cycle re-anchor**: not triggered this cycle. No floor/sibling-entry/L4-cap LANDS this cycle (D1 is survey-only; the L4-cap landings it identifies ride cycle-047, where the floor-landing-reanchor coupling WILL apply — an L4 cap over an L3 operator X implies X's §Upward / §Lowers-from re-anchor must co-schedule in the same cycle as the cap). Flagged forward to the cycle-047 planner in Open questions.

## Sequencing schedule

**Single wave — all three dispatches parallel (wave 1):**
- D1 (`combinator-miner` — L4/L4>L3 pre-survey)
- D2 (`layer-intro-author` — `concepts/erasure-scope.md`)
- D3 (`cross-layer-cross-cutter` — residual-L2>L1-gap audit)

No forward-reference dependencies among the three (D1/D3 are observation; D2 authors a self-contained concepts page citing already-firm L3>L2 themes). One critic + one repairer (if needed) per report, then `integrator-per-report` ×3 (serial), then ONE `integrator-finalize` at cycle end.

## Deliverable-presence verification

Per the MANDATORY pre-dispatch four-step check, with literal pasted command output per dispatch.

**D1 — L4/L4>L3 coverage pre-survey** — *open by construction (survey/observation, no named-artifact-slug deliverable).* This dispatch produces a CYCLE.md survey + fan-out ranking, not a named `book/src/<layer>/<slug>.md` file, so the file-existence / maturity / OQ-RESOLVED-grep steps do not apply to a deliverable slug. The survey's *inputs* are verified present:
```
$ ls book/src/L4/   →  chebyshev.md  index.md  iterate-while.md  iterate-while-with-prev.md  krylov-step.md   (4 firm ops + index)
$ ls book/src/L4-L3/ →  fgmres-inner-loop-iterate-while-migration.md  gmres-inner-loop-iterate-while-migration.md  index.md  krylov-step-typed-wrapper-dissolution.md   (3 firm themes + index)
$ ls book/src/L3/ | grep -v index | wc -l  →  18   (18 firm L3 operators — the survey denominator)
```
Structural-block check: none — the survey is open by construction; the L4 strawman (`book/src/design/l4_calculus.md`) is in-management and available. The `iterate-while-l3-rendering-trajectory-accumulation-gap` OQ (noted at `L4/index.md:54-55`) flags standalone-L4>L3-theme candidates as already-open work — a positive signal the survey has live targets, not a block.

**D2 — `book/src/concepts/erasure-scope.md`** —
1. File existence:
```
$ ls -la book/src/concepts/erasure-scope.md
ls: cannot access 'concepts/erasure-scope.md': No such file or directory     (exit 2 — ABSENT)
```
   → Deliverable ABSENT on disk; authoring is a genuine create, not a no-op.
2. Maturity / already-discharged: N/A (file absent — nothing on disk to be at-or-above the proposed maturity).
3. OQ-ledger RESOLVED-grep:
```
$ grep -i "erasure-scope.*RESOLVED\|erasure-scope.*CLOSED" scaffolding/open-questions.md
→ the three predecessor OQ slugs (substantive-l3-l2-erasure-scope-taxonomy / l3-l2-substantive-erasure-scope-taxonomy /
  l3-l2-erasure-scope-taxonomy-FOUR-root-complete-ratify-plus-concepts-page) are UNIFIED + resolved cycle-045 meta-phase,
  AND the resolution explicitly states: "The concepts/erasure-scope.md page is GO → migrated to plan Backlog High
  erasure-scope-taxonomy-concept-page (layer-intro-author; meta-phase does not write book/)."
```
   → The OQ is RESOLVED, but the resolution **migrates the concept-page authorship INTO the plan as a GO item** — i.e., the page itself is explicitly NOT-yet-authored and is the assigned deliverable. The plan line is NOT stale: it post-dates the closure (batch-13 meta-phase routed the page to the Backlog as near-term work; meta-phase does not write `book/`). This is the correct read of "open by routing": the question is closed, the authoring is the open follow-up.
4. Structural-block check: none. The canonical four-root write-up exists verbatim in `book/src/L3-L2/index.md` §Working-Notes (lines 67-73, confirmed by grep) — the concept page transcribes/cross-references it; no methodology gate blocks. `concepts/sequential-obstruction.md` (the fold-in target) is present (`-rw-rw-r-- 9012 bytes`). **ALL checks pass → recruit.**

**D3 — residual-L2>L1-gap audit** — *open by construction (audit/observation, no named-artifact-slug deliverable).* This dispatch produces a CYCLE.md gap census + recommendation, not a named file. Its *inputs* and the *target gap* are verified:
```
$ ls book/src/L2/ | grep -v index | wc -l    →  21   (21 firm L2 operators)
$ ls book/src/L2-L1/ | grep -v index | wc -l →  19   (19 L2>L1 themes)
# suffix-stem cross-check (L2 op vs L2-L1 theme stems): every L2 op has a same-named L2>L1 theme EXCEPT:
#   krylov-step  →  no `krylov-step`-stemmed file in book/src/L2-L1/  (the candidate residual gap)
$ grep -i "residual-l2-l1\|residual.l2.l1" scaffolding/open-questions.md   →  (no matches — no prior RESOLVED disposition)
```
   → The audit target (the `krylov-step` L2>L1 candidate gap) is genuinely open (no L2-L1 `krylov-step` theme on disk; no OQ-ledger resolution). Audit-class dispatch, no `verified_against:`-block precondition. Structural-block check: none — the audit's job is precisely to classify whether the gap is genuine-missing vs by-design. **Open → recruit.**

All three dispatches recruited: D2 passes all four checks (ABSENT + OQ-migrated-to-plan + canonical-source-present + no block); D1 and D3 are open-by-construction (survey/audit, no named-slug deliverable) with verified inputs and (D3) a verified-open target gap. No dispatch matches the STOP-PROPOSING NEGATIVE LIST (`lu_solve`, `back_solve`, `ls-update-column`, the 4 NLEPS atoms) — none of the three is an L3 backfill. `apply_nonlinear_pencil` stays HELD (not proposed). Framing check (audit-first vs reflexive-harvest): D1 is correctly framed as a survey (not a premature `layer-intro-author` dep-map authoring); D3 is correctly framed as audit-first (no foregone "land a krylov-step L2>L1 theme" conclusion — the audit decides genuine-vs-by-design).

## Open questions / caveats

- **No wave-2 per-operator L4 picks pre-committed this cycle (deliberate).** The active head allowed cycle-046 to ride wave-2 L4-cap/L4>L3-theme picks "if the survey is fast and you want to pre-commit based on the existing L4 inventory." I chose NOT to: the existing L4>L3 inventory covers only the Krylov chain (3 themes, all `krylov-step`/`gmres`/`fgmres`), so the coverage denominator for the other 14+ firm L3 operators — and crucially the **per-operator warranted-vs-by-design judgment** (L4 is vocabulary-not-architecture; many BLAS-1 leaves likely have no distinct L4 vocabulary and lower directly, the L4 analog of `apply_linop` being no-L2-by-design) — is genuinely unknown until D1 runs. Pre-committing risks recruiting no-op or mis-framed picks (the exact deliverable-presence-staleness class the paste-evidence procedure guards against). The survey lands the fan-out ranking; **the cycle-047 planner dispatches the top picks against it.** This keeps the opening cycle clean and honors "audit-first when at a cohort boundary."

- **Floor-landing → same-cycle re-anchor applies at cycle-047, not this cycle.** No L4 cap LANDS this cycle (D1 is survey-only). When cycle-047 lands an L4 cap over an L3 operator X, X's §Upward / §Lowers-from framing (which may currently assert "no L4 cap above me / lowers directly from L4 via the typed-wrapper dissolution") goes stale the moment the cap lands — so the cycle-047 planner must **couple the L4-cap landing with X's adjacent-entry re-anchor in the same cycle** (newly-codified `floor-landing-implies-same-cycle-adjacent-entry-reanchor`), either by extending the L4-cap harvester's proposed-changes to re-anchor X (when mechanical) or co-scheduling a lifter. Flagging forward so the c047 plan builds the coupling in from the start.

- **`krylov-step` L2>L1 gap — likely by-design, but the audit decides.** My deliverable-presence cross-check surfaced `krylov-step` as the sole L2 op lacking a same-named L2>L1 theme. My prior (non-binding on the audit) is that this is **by-design no-theme** analogous to `apply_linop` being no-L2-by-design at L3>L2: `krylov-step` is a composition whose L2>L1 lowering is the in-line decomposition into L1 primitives (`apply_linop`/`axpy`/`dot`/`nrm2`/`scal`, all listed firm in `L2/krylov-step.md:96`), and its cross-layer story is carried by the firm `krylov-step-typed-wrapper-dissolution` (L4>L3) + the krylov-step chain. D3 is framed audit-first precisely so it can return either verdict; if it returns "genuine gap," the `krylov-step`-L2>L1 theme authoring is a clean cycle-047 abstractor pick.

- **D1 / D3 are both observation-only; D2 is the only `book/` mutation this cycle.** This is a low-mutation opening cycle by design (one new concepts file). The substantive forward-frontier authoring (L4 caps, L4>L3 themes, any warranted L2>L1 theme) is fan-out-ranked by the two surveys and lands cycle-047 — the standard survey-then-dispatch cadence for opening a fresh frontier (mirrors the c042 D1 fork-evidence-then-build precedent).

- **No ask-items for the human.** All batch-13 decisions were GO (per the resume notes); no open asks remain. No methodology-adjustment pattern surfaced this cycle that the (already-fired) batch-13 meta-phase missed — the two newly-codified frictions (`index-dual-registration-row-and-own-bullet-vs-consolidated-tally`, `floor-landing-implies-same-cycle-adjacent-entry-reanchor`) are correctly loaded and applied (the latter flagged forward to c047; the former not-applicable this cycle as no ≥2-parallel-shared-index-landing occurs).

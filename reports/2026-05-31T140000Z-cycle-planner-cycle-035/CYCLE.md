---
agent: cycle-planner
invoked_at: 2026-05-31T140000Z
scope: cycle-035 dispatch plan (SECOND primary cycle of meta-batch-10; cycles 034/035/036; meta-phase fires after cycle-036 finalize)
status: pending
---

# Cycle-035 dispatch plan

## Deliverable-presence verification (four-step check per every candidate)

**CYCLE-034 RECURRENCE-1 CONTEXT:** The c034 cycle-planner asserted `ls book/src/L3/krylov-step.md → NOT found` but the file was firm on-disk since c010 (24 cycles). The batch-9-codified MANDATORY pre-dispatch ENFORCEMENT bullet did NOT prevent this wasted dispatch slot. The c034 recurrence is the second-strongest evidence the ENFORCEMENT bullet alone is insufficient — the c035 planner executes a DEEPER four-step check (per cycle-033 working precedent) for EVERY candidate BEFORE finalizing dispatch selection. **Every item below carries explicit per-dispatch verification results.**

### Candidate 1: `richardson` L1 primitive

**Fan-out:** HIGH (would unblock `polynomial-smoother` L2 combinator candidacy — 3-sibling jacobi + chebyshev + richardson; current L2 blockers show c032/c033/c034 cycles all idle waiting for richardson as the third firm sibling).

**Four-step check:**
1. **File existence**: `ls book/src/L1/richardson.md 2>&1` → `No such file or directory`. Genuinely absent. ✓
2. **Status header**: N/A (file does not exist). ✓
3. **`verified_against:` block presence**: N/A. ✓
4. **OQ-RESOLVED grep**: `grep 'richardson.*RESOLVED\|richardson.*CLOSED' scaffolding/open-questions.md` → ZERO hits. No blocking OQ. ✓

**Palace-codemap precondition check (the CRITICAL detail from c034 integrator-signals suggested-next-dispatches):**
- `search_text('Richardson')` across Palace `.hpp` files → ZERO hits.
- `search_text('richardson')` across Palace files → ZERO hits.
- `search_text('Richardson|richardson', glob='**/*.hpp')` → ZERO hits.
- Explicit smoother-enumeration search: `search_text('class.*Smoother')` → hits: `JacobiSmoother`, `ChebyshevSmoother`, `ChebyshevSmoother1stKind`, `DistRelaxationSmoother`. **NO Richardson.**

**VERDICT: STALE PLAN ITEM.** Palace does NOT expose Richardson as a standalone smoother enum. The c034 suggested-dispatch "Pre-grep `palace/linalg/labels.hpp` for Richardson-class enum-or-not before dispatch" was a correct precaution — this plan line is a dead priority that should be RETIRED from the backlog. The polygon-smoother L2 combinator is blocked on a third firm sibling; richardson is NOT viable as that sibling because Palace has never shipped it. The polynomial-smoother combinator remains deferred/contingent in the plan pending (a) a third smoother that Palace DOES expose to be firmed, OR (b) an abstractor verdict that a 2-sibling jacobi+chebyshev-only combinator is defensible. **This plan item WILL NOT be dispatched.**

---

### Candidate 2: `matrix-weighted-norm-mutation-rotation` L1>L0 theme

**Fan-out:** MEDIUM (energy-norm consumers — CG-residual / eigenmode-residual / M-orthonormalization).

**Four-step check:**
1. **File existence**: `ls book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md` → file exists (36952 bytes). ✓
2. **Status header**: `grep "^## Status" book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md` → "## Status"; line 432 reads: "`firm` — the rewrite is the structural expansion...". **STATUS IS `firm`.**
3. **`verified_against:` block presence**: `grep -n "^## verified" book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md` → ZERO hits. **NO `verified_against:` block.** However, the theme is ALREADY `firm`, so the absence is a standard lowering-verifier follow-up (not a firm-promotion gate).
4. **OQ-RESOLVED grep**: `grep 'matrix-weighted-norm-mutation-rotation.*RESOLVED\|matrix-weighted-norm-mutation-rotation.*CLOSED' scaffolding/open-questions.md` → ZERO hits in Closed index.

**VERDICT: ALREADY DISCHARGED.** The theme landed firm (status `firm` on-disk at cycle-008 or earlier per commit history scan). The only pending work is the `verified_against:` block (lowering-verifier standard follow-up), NOT a firm-promotion dispatch. **This plan item WILL NOT be dispatched as an authoring dispatch** — the block audit is already in priorities backlog as a separate line (batch-6 firm-theme audits). If the cycle-035 planner routes a `lowering-verifier` for the audit, it will consume this item; if not, it remains queued.

---

### Candidate 3: `apply-nonlinear-pencil-mutation-rotation` L1>L0 theme (batch-6 firm-theme audit)

**Fan-out:** LOW-MEDIUM (per-line verified_against audit; batch-6 firm-theme audits backlog cohort).

**Four-step check:**
1. **File existence**: `ls book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md` → file exists (28239 bytes). ✓
2. **Status header**: `grep "^## Status" book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md` → line 26 reads: "`firm` — the rewrite is read from a **positive** source site...". **STATUS IS `firm`.**
3. **`verified_against:` block presence**: `grep -A 1 "^## verified_against" book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md` → ZERO hits. **NO `verified_against:` block present.** YAML block is absent; integration's pending audit work.
4. **OQ-RESOLVED grep**: `grep 'apply-nonlinear-pencil.*RESOLVED\|apply-nonlinear-pencil.*CLOSED' scaffolding/open-questions.md` → ZERO hits in Closed index. The plan backlog carries `apply-nonlinear-pencil-mutation-rotation-lowering-verifier-audit-followup`.

**VERDICT: GENUINELY OPEN.** Theme is firm on-disk; the `verified_against:` block is the only missing piece (standard lowering-verifier workflow). This is the canonical audit-dispatch target. **This dispatch IS ELIGIBLE for cycle-035 routing to `lowering-verifier`** — dispatch scope: `apply-nonlinear-pencil-mutation-rotation L1>L0 lowering-verifier audit`.

---

### Candidate 4: `chebyshev-smoother-mutation-rotation` cite-tightening (`:150-159` → `:147-155`)

**Fan-out:** LOW (hygiene; mechanical cite-precision).

**Four-step check:**
1. **File existence**: `ls book/src/L1-L0/chebyshev-smoother-mutation-rotation.md` → file exists. ✓
2. **Status header**: `grep "^## Status" book/src/L1-L0/chebyshev-smoother-mutation-rotation.md` → `firm`. ✓
3. **`verified_against:` block**: File is firm; mechanical edit scope is a citation-range tightening within existing verified_against blocks (not a new block). ✓
4. **OQ-RESOLVED grep**: `grep 'chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten' scaffolding/open-questions.md` → FOUND at line 489: "`chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten` — **NEW (cycle-034 D2)** — citation hygiene...". **OQ is OPEN (not RESOLVED).**

**VERDICT: GENUINELY OPEN.** The OQ filed by c034 D2 audit (verdict-only) documents the precise edit needed: line `:150-159` tighten to `:147-155` (the exact else-block body). This is a mechanical repairer/lifter scope — a straightforward one-cite edit. **This dispatch IS ELIGIBLE for cycle-035 routing to `repairer` or `lifter`** — dispatch scope: "chebyshev-smoother-mutation-rotation `:150-159` → `:147-155` cite-tightening".

---

### Candidate 5: L3 vocabulary inventory (via cycle-033 integrator-signals suggested-next)

**From c034 integrator-signals "Suggested next dispatches":** "(`harvester` or `combinator-miner`, L3 firm operator harvest) — L3 cohort has been static since c020; candidates include the cycle-009 codified `Identity-lowerings still require both L levels` backfills (`apply_linop` L3 entry mirror; etc.). Run deliverable-presence check first."

**Four-step check on a concrete example: `apply_linop` L3 entry (the canonical backfill candidate from the identity-lowerings invariant cycle-009)**
1. **File existence**: `ls book/src/L3/apply_linop.md` → No such file or directory. ✓
2. **Status header**: N/A (does not exist). ✓
3. **`verified_against:` block**: N/A. ✓
4. **OQ-RESOLVED grep**: `grep 'l3-apply.linop\|L3.*apply.linop.*RESOLVED' scaffolding/open-questions.md` → ZERO hits (no explicit OQ; this is the canonical cycle-009 backfill pattern).

**VERDICT: GENUINELY OPEN.** The L3 `apply_linop` entry is a standard identity-lowering per the cycle-009 codified invariant ("Identity-lowerings still require both L levels"). The L2 form (`book/src/L2/apply_linop.md`) is firm; the L3 form should mirror it (identity in form, as with `krylov-step` c010). **This dispatch IS ELIGIBLE for cycle-035 routing to `harvester`** — dispatch scope: "apply_linop L3 identity-lowering harvest (cycle-009 canonical backfill)".

---

## Goals selected this cycle

Cycle-035 operates under the batch-10 opening-cycle burden: the c034 recurrence-1 of `cycle-planner-stale-priorities-line-recruitment` has escalated the criticality of deeper planner-side deliverable-presence checks. This cycle prioritizes (1) **retiring the stale richardson plan line** (Palace does not expose it; not a viable L1 sibling); (2) **landing the apply-nonlinear-pencil-mutation-rotation lowering-verifier audit** (firm theme, missing `verified_against:` block — standard audit workflow); and (3) **mechanical cite-tightening** (chebyshev-smoother hygiene, OQ-documented precision fix). The cycle also opens the canonical L3 `apply_linop` identity-lowering backfill (cycle-009 invariant). **Fan-out is mixed: the audit has medium fan-out (energy-norm consumers); the L3 backfill carries low-medium fan-out (L3 vocabulary inventory closure); the cite-tightening is low (hygiene).** The richardson retirement is a **direct negative result of the planner's deliverable-presence discipline**, which is the intended outcome of the batch-9 codification.

## Dispatches

All dispatches verified genuinely-open per the four-step check above. Sequenced into two waves: wave-1 (lowering-verifier audit) can run immediately; wave-2 (mechanical cites + L3 harvest) depend on wave-1 report to clear any forward-references that might surface.

**Wave 1 (parallel dispatch)**

1. **Agent**: `lowering-verifier`
   **Scope**: `apply-nonlinear-pencil-mutation-rotation` L1>L0 lowering-verifier audit
   **Deps**: none
   **Rationale**: Firm theme missing the standard `verified_against:` block (per sibling-theme convention, `.claude/agents/lowering-verifier.md` workflow). The theme is firm-on-positive-structure; the audit confirms surface-form exhaustiveness. Fan-out: medium (the NLEPS-interior `apply_nonlinear_pencil` L1 op is consumed across 3 NLEPS solver instances; energy-norm-aware implementations may reuse the audit's scope map).

**Wave 2 (parallel dispatch, after wave-1 report lands)**

2. **Agent**: `lifter`
   **Scope**: `chebyshev-smoother-mutation-rotation` `:150-159` → `:147-155` cite-tightening (OQ `chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten`)
   **Deps**: D1 (reference; no blocking dependency — D1's report merely documents the precise line range from the c034 D2 verdict).
   **Rationale**: Mechanical cite-precision edit. OQ filed by c034 D2 audit (verdict-only dispatch); lifter completes the follow-up. Fan-out: low (hygiene). Cite-correction affects only one theme's evidence section.

3. **Agent**: `harvester`
   **Scope**: `apply_linop` L3 identity-lowering harvest (cycle-009 canonical backfill per CLAUDE.md "Identity-lowerings still require both L levels")
   **Deps**: none (independent of D1/D2; can run parallel with D2).
   **Rationale**: L3 vocabulary inventory canonical backfill. The L2 `apply_linop` entry is firm; the L3 form is identity-in-form, requiring both-levels per the cycle-009 invariant. Unblocks the L3-L2 apply-linop lowering-verifier audits queued in the backlog. Fan-out: low-medium (L3 vocabulary inventory closure; enables future L3-L2 theme audits).

## Overlap analysis

**D1 (wave-1) vs. D2 (wave-2):** D1 edits `book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md` (appends `verified_against:` block). D2 edits `book/src/L1-L0/chebyshev-smoother-mutation-rotation.md` (modifies citation range in existing verified_against). **DISJOINT files** — NO overlap. Can run in parallel once D1 lands.

**D1 (wave-1) vs. D3 (wave-2):** D1 edits `book/src/L1-L0/...` (NLEPS theme). D3 creates `book/src/L3/apply_linop.md` (new L3 entry). **DISJOINT files + disjoint layers** — NO overlap. Can run parallel.

**D2 (wave-2) vs. D3 (wave-2):** D2 edits chebyshev L1>L0 theme. D3 creates L3 apply_linop operator. **DISJOINT entirely** — NO overlap. Can run parallel.

**Index file sharing:** None of D1/D2/D3 append to `book/src/L1/index.md` or `book/src/L3/index.md` at scope (D3 appends to L3 index; D1 appends `verified_against:` which is intra-file, not index-touching; D2 edits intra-file cite range). Per the c033 precedent, index-level coordination happens serially at the `integrator-per-report` dispatch level (each report reads the prior report's disk state), so wave-mate coordination is clean as long as no two dispatches in the same wave touch the same index row.

**Result:** All three dispatches are genuinely parallel within their respective waves (D1 in wave-1; D2 and D3 both in wave-2 without overlap). Wave-2 depends on wave-1 report-landing (forward-reference hygiene / ensure any new `verified_against:` blocks land before subsequent edits reference them), but does NOT depend on wave-1's *content* — the dependency is scheduling-only (per-report integrator order).

## Sequencing schedule

**Wave 1:**
- D1: `lowering-verifier` apply-nonlinear-pencil-mutation-rotation audit

**Wave 2 (after D1 lands):**
- D2: `lifter` chebyshev-smoother-mutation-rotation cite-tightening
- D3: `harvester` apply_linop L3 identity-lowering (parallel with D2)

## Open questions / caveats

1. **richardson plan-line retirement** — The c034 integrator-signals recommendation to "Pre-grep `palace/linalg/labels.hpp` for Richardson-class enum-or-not before dispatch" has confirmed richardson is not a viable L1 sibling (Palace never shipped it). The cycle-035 planner recommends retiring this plan line from priorities backlog. The `polynomial-smoother` L2 combinator remains deferred/contingent, waiting for either (a) a third firm smoother that Palace *does* expose, or (b) an abstractor verdict on 2-sibling defensibility. **Action for integrator-finalize:** update `scaffolding/priorities.md` cycle-035 now-section to strike/retire the richardson plan item (mark as abandoned, not genuinely-open).

2. **matrix-weighted-norm-mutation-rotation status redundancy** — This plan item was drafted as a "firm-promotion" candidate; on-disk verification shows it is already firm. The audit (`verified_against:` block) is the outstanding work, already queued in the batch-6 firm-theme-audits backlog cohort. No dispatch selected this cycle; the audit is a future lowering-verifier dispatch (if prioritized). **No action needed** — the plan item's current framing is accurate (queued in backlog, awaiting its audit dispatch).

3. **Batch-10 meta-phase evidence accumulation** — This cycle's planner-verification discipline (per cycle-033 working precedent and c034 recurrence-1 escalation) has identified one retired plan item (richardson) and confirmed two genuinely-open audit/mechanical work items. **Carry-forward for batch-10 meta-phase:** evidence that the deeper planner-side check (four-step per-candidate verification) is working as intended; c035 produced zero wasted-dispatch stale candidates (contrast c034's D3 and c031/c032 recurrences). The skill `verify-dispatch-scope-not-already-discharged` succeeded at the producer side (caught c034 D3); the ENFORCEMENT bullet succeeded at the planner side (filtered the richardson candidate pre-dispatch). Together they break the recurrence pattern. **Candidate summary for meta-phase:** if c036 also shows zero recurrence, the pattern is RESOLVED; if c036 adds a recurrence, the meta-phase should evaluate whether to migrate the skill to a hard planner-side pre-dispatch checklist (rather than rely on prose-discipline enforcement bullet + producer-side catch).

---

**Counts before cycle-035:**
- L1 firm: 25
- L1>L0 firm themes: 23
- L3 firm: 8 (identity-lowerings include krylov-step, BLAS-1 nrm2/axpby/dot/scal, chebyshev, inner-product-fold; apply_linop is the canonical remaining backfill)

**Expected counts after cycle-035 integration:**
- L1 firm: 25 (no new L1 entries this cycle)
- L1>L0 firm themes: 23 (apply-nonlinear-pencil audit does NOT change status; already firm)
- L3 firm: 9 (+1: apply_linop identity-lowering)

---
agent: cycle-planner
invoked_at: 2026-05-31T210135Z
scope: cycle-038 dispatch plan
status: pending
---

# Cycle 038 dispatch plan

Cycle-038 is the SECOND primary cycle of meta-batch-11 (cycles 037/038/039; the batch-11 meta-phase fires AFTER cycle-039, not this cycle). Cycle-037 (commit `b64fedc`, second-clean opus-planner cycle) landed firm L3 `assemble-diagonal` (10th) + `jacobi-smoother` (11th) identity-in-form backfills + a firm `reciprocal-elementwise-product-mutation-rotation` 19-row `verified_against:` audit. Per the c037 finalize hand-off (integrator-signals §Unblocked), the natural cycle-038 follow-frontier is the **4 REMAINING firm (A) identity-in-form L3-backfill candidates** (`reciprocal`, `elementwise_product`, `normalize`, `divfree-projector`).

## Goals selected this cycle

Advance the **L3-cohort-growth (A) identity-in-form backfill** frontier — the highest-confidence, frontier-settled routine work tier after the c036 D2 audit verdict. Dispatch 3 of the 4 remaining (A) L3 backfills as parallel harvester work (`reciprocal`, `elementwise_product`, `divfree-projector`) plus the genuinely-open `floquet-correction-mutation-rotation` `verified_against:` audit. `normalize` (the 4th (A) candidate) is intentionally HELD to cycle-039 as the cohort-closing opener, keeping this wave bounded and avoiding the cross-cohort coupling caveat noted below. This closes 3 more end-to-end L3 chains (the elementwise diagonal-preconditioner leaves + the divergence-free projector) and firms the leaf-lowering evidence for the firm c036 floquet theme.

## Deliverable-presence verification

Per the batch-10 meta-phase PASTE-INLINE-EVIDENCE strengthening of the cycle-planner role-spec bullet + the `verify-dispatch-scope-not-already-discharged` skill (four-step + step-5 STOP-PROPOSING NEGATIVE LIST consult + step-6 audit-first-vs-reflexive-harvest framing). Literal command output pasted per dispatch.

### D1 — `reciprocal` L3 backfill (harvester)

1. **File existence** (`ls book/src/L3/reciprocal.md` — must be ABSENT):
   ```
   ls: cannot access 'book/src/L3/reciprocal.md': No such file or directory
   ```
   → ABSENT. Genuinely open.
2. **L1-home maturity** (`grep -A1 '^## Status' book/src/L1/reciprocal.md`):
   ```
   ## Status

   `firm` — signature is canonical (matches the `Reciprocal()` member-method surface exactly...
   ```
   → L1 home `firm`. Identity-in-form L3 backfill is well-founded (the L1 form is whole-tensor / no-element-loop → L3-native by signature shape, per the BLAS-1 cohort precedent).
3. **OQ-ledger RESOLVED-grep** (`grep 'reciprocal.*RESOLVED\|reciprocal.*CLOSED' scaffolding/open-questions.md` for an L3-scoped closure): no L3-`reciprocal` RESOLVED/CLOSED line. The only `reciprocal`-mentioning OQ line is `assemble-diagonal-l3-reciprocal-elementwise-product-plain-text-forward-refs` (open897:904) which NAMES this exact dispatch as its *Trigger* ("a harvester dispatch on `reciprocal` / `elementwise_product` at L3"). → Dispatch is the trigger, not a re-propose.
4. **Structural-block check**: none. The c036 D2 audit verdict (`book/src/L3/index.md:41`) explicitly classifies `reciprocal` as (A) identity-in-form ("elementwise self-map"). No methodology gate blocks. NOT on the STOP-PROPOSING NEGATIVE LIST.
5. **STOP-PROPOSING consult**: `reciprocal` is NOT on the (C) negative list (`lu_solve`, `back_solve`, `ls-update-column`, 4 NLEPS atoms).
6. **Framing**: identity-in-form harvester (NOT audit-first) is correct — the c036 D2 audit ALREADY ran the cohort classification and settled `reciprocal` as (A) identity-in-form; no representation-dependent caveat remains to re-audit (unlike the c036 `assemble-diagonal` operator-to-data primitive that needed the audit-first reframe — that audit is DONE and its verdict covers `reciprocal`).

### D2 — `elementwise_product` L3 backfill (harvester)

1. **File existence** (`ls book/src/L3/elementwise_product.md` — must be ABSENT):
   ```
   ls: cannot access 'book/src/L3/elementwise_product.md': No such file or directory
   ```
   → ABSENT. Genuinely open.
2. **L1-home maturity** (`grep -A1 '^## Status' book/src/L1/elementwise_product.md`):
   ```
   ## Status

   `firm` — signature is canonical (matches the `BaseDiagonalOperator::Mult` operator-action form...
   ```
   → L1 home `firm`. Identity-in-form L3 backfill well-founded.
3. **OQ-ledger RESOLVED-grep**: no L3-`elementwise_product` RESOLVED/CLOSED line; same `assemble-diagonal-l3-...-plain-text-forward-refs` open OQ NAMES this dispatch as its *Trigger*. → trigger, not re-propose.
4. **Structural-block check**: none. c036 D2 verdict (`book/src/L3/index.md:41`) classifies `elementwise_product` as (A) identity-in-form ("Hadamard binary"). NOT on STOP-PROPOSING list.
5. **STOP-PROPOSING consult**: NOT on the (C) negative list.
6. **Framing**: identity-in-form harvester correct (c036 D2 audit verdict covers it; no fresh audit needed).

### D3 — `divfree-projector` L3 backfill (harvester)

1. **File existence** (`ls book/src/L3/divfree-projector.md` — must be ABSENT):
   ```
   ls: cannot access 'book/src/L3/divfree-projector.md': No such file or directory
   ```
   → ABSENT. Genuinely open.
2. **L1-home maturity** (`grep -A1 '^## Status' book/src/L1/divfree-projector.md`):
   ```
   ## Status

   `firm`.
   ```
   → L1 home `firm`. **Dependency check** — `divfree-projector` is a constructed-operator gate that calls L3 `ksp_solve` internally; verified the L3 dep is firm (`grep -A1 '^## Status' book/src/L3/ksp_solve.md` →  ``firm` — the value-threaded fold ... canonical iteration-rotation form...`). → all downstream L3 deps present + firm.
3. **OQ-ledger RESOLVED-grep** (`grep 'divfree.projector.*RESOLVED\|divfree.projector.*CLOSED' scaffolding/open-questions.md` L3-scoped): no L3-`divfree-projector` RESOLVED/CLOSED line. Tracked open under the parent `l3-cohort-growth-audit-c036-verdict` (line 911 names it among the four remaining (A) candidates).
4. **Structural-block check**: none. c036 D2 verdict classifies `divfree-projector` as (A) ("constructed-operator gate, like firm-L3 `ksp_solve`"). NOT on STOP-PROPOSING list. The c037 finalize signal notes `jacobi-smoother.md §Context` already references `divfree-projector` plain-text (repairer downgrade) — landing it makes that ref live-link-upgrade-eligible at finalize (a benefit, not a block).
5. **STOP-PROPOSING consult**: NOT on the (C) negative list.
6. **Framing**: identity-in-form harvester correct — the apply is identity-in-form (the constructed-operator gate apply maps to the firm-L3 `ksp_solve` precedent); c036 D2 audit verdict covers it.

### D4 — `floquet-correction-mutation-rotation` `verified_against:` audit (lowering-verifier)

1. **File existence** (target theme must be PRESENT and firm): `book/src/L1-L0/floquet-correction-mutation-rotation.md` exists (landed c036).
2. **Audit-deliverable-presence** (`grep -c '^verified_against:' book/src/L1-L0/floquet-correction-mutation-rotation.md`):
   ```
   0
   ```
   → ZERO `verified_against:` blocks on disk. The audit deliverable is genuinely absent → dispatch is NOT a no-op.
3. **Theme maturity** (`awk '/^## Status/...'` → `` `firm`. ``): theme is `firm` → valid lowering-verifier audit target (per-line evidence backfill on a firm theme).
4. **OQ-ledger trigger**: the trigger-gated OQ `floquet-corrector-addmult-aliasing-applicability-audit` (filed c036, integrator-signals §Resolution-implications: "needs-more (NEW) — trigger-gated on a lowering-verifier dispatch on the new theme") NAMES this exact dispatch as its trigger. → dispatch is the trigger, not a re-propose.
5. **STOP-PROPOSING consult**: N/A (not an L3 backfill; an audit dispatch).
6. **Framing**: lowering-verifier per-line `verified_against:` audit is the correct route (firm theme + missing machine-readable evidence block; same shape as the c037 D3 `reciprocal-elementwise-product` audit that landed clean).

**Held (NOT dispatched this cycle, explicit):** `normalize` L3 backfill — the 4th (A) candidate. VERIFIED-OPEN (`ls book/src/L3/normalize.md` → `No such file or directory`; L1 home `firm` — "firm-on-positive-structure"). Held to cycle-039 as the cohort-CLOSING opener to (i) keep this wave at 4 bounded dispatches and (ii) avoid the elementwise-cohort coupling caveat: L1 `normalize` is a fused `nrm2 + scal` that references `nrm2`/`scal` (NOT `reciprocal`/`elementwise_product`), so it does not collide with D1/D2 — but landing it alongside the two elementwise leaves in one wave adds no fan-out and the cohort reads cleaner closed in a dedicated cycle-039 dispatch. Plan updated below.

## Dispatches

1. **agent**: `harvester`
   **scope**: L3 operator backfill — `book/src/L3/reciprocal.md`. Identity-in-form (A) L3 backfill of the firm L1 `reciprocal` (elementwise multiplicative-inverse self-map; firm L1 home `book/src/L1/reciprocal.md`). Template the firm L3 identity-row precedents `book/src/L3/scal.md` (leaf BLAS-1 identity-in-form) + `book/src/L3/assemble-diagonal.md` (c037, operator-introspection leaf). The L3 form is value-thread-isomorphic to the L1 signature (whole-tensor in / whole-tensor out, no element loop). Dep-map row references the L1 anchor `../L1/reciprocal.md` downward (in-line identity-in-form annotation per the cycle-012 non-adjacent-identity convention; no `L3-L2/`/`L3-L1/` theme file). Substantive rotation lives at the firm L1>L0 `reciprocal-elementwise-product-mutation-rotation` sub-pattern A. Append ONE distinct dep-map row to `book/src/L3/index.md` + ONE SUMMARY.md line; leave the running-tally count bump to finalize.
   **deps**: none
   **rationale**: Medium fan-out — closes one more (A) L3 chain end-to-end (the inverse-diagonal leaf of the diagonal-preconditioner-apply chain). Named *Trigger* of open OQ `assemble-diagonal-l3-reciprocal-elementwise-product-plain-text-forward-refs`; landing it (with D2) makes the c037 `assemble-diagonal.md` plain-text forward-refs live-link-upgrade-eligible at finalize. c036 D2 audit (A) verdict.

2. **agent**: `harvester`
   **scope**: L3 operator backfill — `book/src/L3/elementwise_product.md`. Identity-in-form (A) L3 backfill of the firm L1 `elementwise_product` (Hadamard binary `a ⊙ b`; firm L1 home `book/src/L1/elementwise_product.md`, with the conjugation sub-axis on the complex side). Template `book/src/L3/jacobi-smoother.md` (c037, whose apply IS one `elementwise_product` — the thinnest constructed-operator gate, the closest structural sibling) + `book/src/L3/scal.md`. The L3 form is identity-in-form on the L1 signature. Dep-map row references `../L1/elementwise_product.md` downward (in-line identity-in-form annotation). Substantive rotation lives at the firm L1>L0 `reciprocal-elementwise-product-mutation-rotation` sub-pattern B. Append ONE distinct dep-map row + SUMMARY line; tally bump to finalize.
   **deps**: none
   **rationale**: Medium fan-out — closes the Hadamard-binary (A) L3 chain; the elementwise primitive consumed by the firm L3 `jacobi-smoother` apply and the chebyshev smoother. Co-named *Trigger* of the same plain-text-forward-ref OQ as D1.

3. **agent**: `harvester`
   **scope**: L3 operator backfill — `book/src/L3/divfree-projector.md`. Identity-in-form (A) L3 backfill of the firm L1 `divfree-projector` (constructed-operator gate; firm L1 home `book/src/L1/divfree-projector.md`). Template the firm L3 `ksp_solve.md` constructed-solver-fold precedent + `book/src/L3/jacobi-smoother.md` (constructed-operator-gate apply). The apply is identity-in-form; it calls the firm L3 `ksp_solve` internally (dep verified firm on disk). Dep-map row references `../L1/divfree-projector.md` downward + names L3 `ksp_solve` as the internal-solve dependency (live link — `book/src/L3/ksp_solve.md` is firm on disk). Append ONE distinct dep-map row + SUMMARY line; tally bump to finalize.
   **deps**: none
   **rationale**: Medium fan-out — closes the divergence-free projector at L3 (the constructed-operator-gate sibling of `ksp_solve`). The c037 `jacobi-smoother.md §Context` plain-text reference to `divfree-projector` becomes live-link-upgrade-eligible at finalize once this lands. c036 D2 audit (A) verdict.

4. **agent**: `lowering-verifier`
   **scope**: `verified_against:` per-line audit of the firm L1>L0 theme `book/src/L1-L0/floquet-correction-mutation-rotation.md` (4 sub-patterns A/B/C/D; landed firm c036; `verified_against:` count 0 on disk → genuinely open). Emit the fenced ` ```yaml ... ``` ` `verified_against:` block per the lowering-verifier channel-format discipline (no leading quote of either kind in `note:` values — `verified-against-note-no-leading-quote-of-either-kind`). Audit the cited anchors at `palace/linalg/floquetcorrection.cpp:72-79` (Mult, sub-pattern A) / `:80-85` (AddMult, sub-pattern D) / `:30-130` (closure-construction, sub-pattern C) on-disk (codemap is localization-only; `citecheck`/on-disk is the citation source of truth). Resolves the trigger-gated OQ `floquet-corrector-addmult-aliasing-applicability-audit`.
   **deps**: none
   **rationale**: Low/audit fan-out — firms the per-line evidence of the firm c036 floquet theme (the leaf-lowering the future floquet L-stack references downward). Genuinely-open (count 0); same audit shape as the clean c037 D3 `reciprocal-elementwise-product` audit. Non-overlapping write surface (L1>L0, disjoint from the three L3 harvester dispatches).

## Overlap analysis

Pairwise (4 dispatches → 6 pairs):

- **D1 (`reciprocal` L3) × D2 (`elementwise_product` L3)**: Each creates a DISTINCT new file (`L3/reciprocal.md` vs `L3/elementwise_product.md`), appends a DISTINCT dep-map row to `L3/index.md`, and a DISTINCT SUMMARY.md line. Per the cycle-037 wave-conflict precedent (D1/D2 both appended distinct rows to `L3/index.md` cleanly, no collision), appending distinct rows to a shared table is NOT operational overlap → **PARALLEL**. The L1 `reciprocal`/`elementwise_product` cross-reference each other (9×/11×), but at L3 each identity-in-form row references its OWN L1 anchor downward (`../L1/<x>.md`), NOT the sibling L3 entry (confirmed against the jacobi-smoother/scal L3 precedents — L3 identity rows point down to L1, not sideways). So there is no L3-sibling forward-reference between them → no wave-ordering dependency.
- **D1 × D3 (`divfree-projector` L3)**: distinct new file + distinct dep-map row + distinct SUMMARY line. `divfree-projector` L1 does NOT reference the elementwise cohort (verified: `grep` returned empty) — it is a constructed-operator gate calling `ksp_solve`. → **PARALLEL**.
- **D2 × D3**: distinct files/rows/lines; no cross-reference (`elementwise_product` and `divfree-projector` are independent at L1 and L3). → **PARALLEL**.
- **D1/D2/D3 × D4 (floquet audit)**: D4 writes ONLY to `book/src/L1-L0/floquet-correction-mutation-rotation.md` (a `verified_against:` block append). Disjoint write surface from the three L3 chapters + `L3/index.md` + the SUMMARY L3 section. No shared operator names. → **PARALLEL** with all three.

**No genuine overlaps.** No two dispatches modify the same operator entry or rewrite the same theme body. The shared `L3/index.md` dep-map table and the SUMMARY.md L3 section receive DISTINCT-row / DISTINCT-line appends from D1/D2/D3 — operationally non-overlapping per the conflict-tolerance philosophy and the c037 precedent. The running-tally count line in `L3/index.md` (currently "11 firm + 2 partial-obstruction") is a single finalize-time reconciliation (11→14), not a per-report co-edit (the c037 finalize reconciled 9→11 once for all c037 L3 landings — same pattern).

## Sequencing schedule

**Single wave (all parallel).** All four dispatches are non-overlapping per the analysis above.

- **Wave 1 (parallel)**: D1 (`reciprocal` L3), D2 (`elementwise_product` L3), D3 (`divfree-projector` L3), D4 (floquet `verified_against:` audit).

Forward-reference note (for the per-report integrator, NOT a wave-ordering constraint): the c037 `L3/assemble-diagonal.md` §Dependencies + `L3/jacobi-smoother.md` §Context carry plain-text forward-refs to `reciprocal`/`elementwise_product`/`divfree-projector` L3. Once D1/D2/D3 land, those become live-link-upgrade-eligible per `upgrade-plain-text-ref-to-live-link-when-target-on-disk` — applied at integrator-per-report / finalize time, not requiring a separate wave. The pipeline remains: 4 dispatches → 4 critics → repairers → `integrator-per-report` ×4 (serial) → ONE `integrator-finalize` (rebuild + commit + push + the single 11→14 tally bump + the live-link upgrades).

## Open questions / caveats

- **`normalize` held to cycle-039 (cohort-closing opener)**: the 4th and final (A) L3 backfill. VERIFIED-OPEN this cycle (file absent; L1 home firm). Holding it keeps cycle-038 at a clean 4-dispatch wave and lets cycle-039 close the entire (A) cohort in a dedicated dispatch. With `normalize` landed cycle-039, the six (A) firm identity-in-form L3 backfills of the c036 D2 audit (`assemble-diagonal` c037, `jacobi-smoother` c037, `reciprocal`/`elementwise_product`/`divfree-projector` c038, `normalize` c039) are COMPLETE — at which point the `l3-cohort-growth-audit-c036-verdict` parent tracker can close its (A) portion and the planner's L3 follow-frontier shifts to the (B) substantive cohort (`orthogonalize`, `chebyshev-smoother`-subsumption-check, `apply_nonlinear_pencil`-fold) as the next routine tier. I have appended a `normalize` cycle-039-opener note + marked the three c038 picks dispatched in `scaffolding/priorities.md`.
- **(B) substantive cohort is the post-(A) frontier**: once the (A) cohort closes (cycle-039), the next L3 work tier is the 3 (B) candidates. `orthogonalize` L3 would be the third `partial-obstruction` row (MGS sequential-obstruction explicit; CGS/CGS2 lift). These are longer-horizon, NOT quick backfills — flagging for the batch-11 meta-phase (post-c039) re-rank.
- **Process watch (escalating friction)**: `cycle-planner-stale-priorities-line-recruitment` is `escalating` (recurrence 6). c037 was the FIRST clean planner cycle post-haiku→opus escalation (integrator-signals §Integration-tooling-friction PROCESS-SIGNAL-positive). This cycle-038 plan re-verified all 4 dispatches with pasted inline evidence per the batch-10 strengthening — keeping the recurrence from firing. The batch-11 meta-phase (post-c039) needs a 2-of-3 clean-batch confirmation before the friction can be marked structurally addressed; c037 + this c038 plan are 2 clean datapoints if c038 lands clean.
- No methodology-adjustment pattern surfaced this cycle that the (stale-by-up-to-3-cycles) friction-ledger/priorities wouldn't already carry. The L3-cohort-growth frontier is fully settled by the c036 D2 audit verdict; no fresh plan candidate needed beyond the held `normalize` note.

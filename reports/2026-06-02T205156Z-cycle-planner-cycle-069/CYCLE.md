---
agent: cycle-planner
invoked_at: 2026-06-02T205156Z
scope: cycle-069 dispatch plan
status: pending
---

# Cycle 069 dispatch plan

## Goals selected this cycle

Cycle-069 is the THIRD/FINAL primary cycle of meta-batch-21 (the batch-21 meta-phase fires after this finalize). It continues the FE-cohort→L4 lift frontier and the directive-2 combinator/named-verb follow-ons opened by c067's survey and advanced by c068's landings, plus two cheap stale-pointer hygiene re-anchors. Concretely: (1) lift the rank-2 driven `assemble_frequency_operator` to L4 through the now-firm `L4/linear_combination` operator-operand corner (the driven pipeline's ASSEMBLE half reaching L4); (2) rise the kept named abstractions `dot`/`nrm2` to L4 as named verbs through the now-firm `L4/inner_product`; (3) flip the two stale "no L4" pointers on `L3/linear_combination`+`L3/inner_product` and re-anchor the drifted `fe_assemble.md` L1-cap weak-form-term witness lines. **The ranks-3-4 `eliminate_*`→L4 lift DEFERS this cycle** — its degenerate-mirror gate FAILS (verified below: `apply_linop`/`axpy`/`set_essential` have no L4 entries). Per the USER STEER, cycle-069 does NOT act on driven-solve→L4 / `map_solve` (the batch-21 meta-phase decides that reconciliation).

## Deliverable-presence verification

Paste-inline-evidence per the cycle-planner §Discipline mandatory four-step check. All `book/`-path scopes verified on disk this cycle.

### D1 — `book/src/L4/assemble_frequency_operator.md` (NEW L4 chapter)
1. **File existence (verify-ABSENT):**
   ```
   $ ls book/src/L4/assemble_frequency_operator.md
   ls: cannot access 'book/src/L4/assemble_frequency_operator.md': No such file or directory
   ```
   → ABSENT. Open by construction at L4.
2. **Source/gate presence (verify-PRESENT):** the L1 source is firm and the through-combinator is firm:
   ```
   $ ls book/src/L1/assemble_frequency_operator.md → present
   L1/assemble_frequency_operator.md ## Status: `firm` — firm-on-positive-structure (the operator-operand specialization of linear_combination's laws ... rap.cpp:764-787 BuildParSumOperator)
   $ ls book/src/L4/linear_combination.md → present
   L4/linear_combination.md ## Status: `firm` — the L4 form is the calculus-level rendering of the firm L3 ...
   ```
   `L4/linear_combination.md:40` already records the next-pull edge: "The next-pull operator-operand consumer is the driven [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) (c069, GATED on this entry)." Gate cleared.
3. **OQ-ledger RESOLVED-grep:** the rank-2 gate OQ `l4-index-13-of-18-...` is **answered** (c068 D3 corrected `L4/index.md:66`); the rank-2 lift itself is queued, NOT resolved — open.
4. **Structural-block check:** no block. The `linear_combination`-rises gate (the prior structural block) cleared c068. Anti-mirror: this is an L1→L4 lift, NOT an L1→L2 mirror — the NO-L2 warrants do not bar it (priorities.md:119 directive-1 note). NOT on STOP-PROPOSING (that bars `map_solve`, L2 mirrors — not this L4 operator-operand specialization).
   → RECRUIT (warrant-first: judge genuine L4 entry vs thin specialization note).

### D2 — `book/src/L4/dot.md` + `book/src/L4/nrm2.md` (NEW L4 chapters, paired named-verb cohort)
1. **File existence (verify-ABSENT):**
   ```
   $ ls book/src/L4/dot.md book/src/L4/nrm2.md
   ls: cannot access 'book/src/L4/dot.md': No such file or directory
   ls: cannot access 'book/src/L4/nrm2.md': No such file or directory
   ```
   → both ABSENT. Open by construction at L4.
2. **Source/gate presence (verify-PRESENT):** the kept named abstractions are firm below + the through-combinator is firm:
   ```
   $ ls book/src/L3/dot.md → present; ## Status: `firm` — specialization-stub. dot at L3 is the M=I Hermitian/symmetric specialization of inner_product
   $ ls book/src/L3/nrm2.md → present; ## Status: `firm` — consumer-stub. nrm2 at L3 is a CONSUMER of the inner-product fold (√dot(x,x))
   $ ls book/src/L4/inner_product.md → present; ## Status: `firm` — the L4 form is the calculus-level rendering of the firm L3
   ```
   `L4/inner_product.md:35` records both as next-pull notes: "the kept named abstractions `dot`/`nrm2` rise alongside as named verbs (a permitted dual; next-pull `L4/dot`/`L4/nrm2`)." Gate cleared.
3. **OQ-ledger RESOLVED-grep:** `grep 'l4-dot-nrm2-named-verb-next-pull.*RESOLVED\|...CLOSED'` → no matches; the OQ is OPEN (opened_at cycle-068, trigger = "the c069 planner picks L4/dot/L4/nrm2 as next-pull candidates" — firing now).
4. **Structural-block check:** no block. Directive-2 disposition-2 (keep-and-rise) authorizes these as named verbs; the do-NOT-merge over-unification guard is recorded (`nrm2` is a CONSUMER of the fold, not a fold member; `dot` = Hermitian `inner_product` at M=I). NOT on STOP-PROPOSING.
   → RECRUIT (judge: one paired-cohort dispatch authoring both named verbs, since both re-express through the single firm `L4/inner_product` and are tightly coupled; if the author finds either is non-trivial it may split — note for the producer).

### D3 — L3 stale-no-L4 re-anchor: `book/src/L3/linear_combination.md` + `book/src/L3/inner_product.md` (in-place lifter, NO new chapter)
1. **File existence (verify-PRESENT — these are EDITS):**
   ```
   $ ls book/src/L3/linear_combination.md book/src/L3/inner_product.md → both present, both ## Status: `firm`
   ```
2. **Stale-line presence (verify the stale assertions exist on disk):**
   ```
   $ grep -n "no L4\|No \`L4\|cycle-010 audit" book/src/L3/linear_combination.md
   8: - (no L4 entry — the fold is a pure value-producing reduction ... carried up unchanged)
   29: ... there is no L4 entry (the L2 entry's "this is an L2 fold, not an L4 combinator" framing carries up unchanged).
   $ grep -n "no L4\|No \`L4\|cycle-010 audit" book/src/L3/inner_product.md
   8: - (none) — no L4 inner_product (folds/leaves are not first-class L4 vocabulary per the cycle-010 audit verdict ...)
   75: ... No `L4/inner_product`
   76: exists — folds/leaves are not first-class L4 vocabulary (cycle-010 audit); the combinator
   ```
   → 4 stale loci confirmed on disk (2 per entry: frontmatter `lifts_from` + body prose). The L4 entries they deny DID land c068.
3. **OQ-ledger RESOLVED-grep:** `grep 'l3-data-algebra-combinators-stale-no-l4-reanchor.*RESOLVED'` → no matches; OPEN (opened cycle-068; trigger = "a thin lifter re-anchor pass c069 or batch-21 meta" — firing now).
4. **Structural-block check:** none — this is the IDENTICAL routine the `eigsolve` cap (c048) triggered for the seven stale `L3/eigsolve` §Upward assertions. Mechanical pointer flip.
   → RECRUIT.

### D4 — `fe_assemble.md` L1-cap witness-line re-anchor: `book/src/L1/fe_assemble.md` (in-place lifter, NO new chapter)
1. **File existence (verify-PRESENT — EDIT):**
   ```
   $ ls book/src/L1/fe_assemble.md → present; ## Status: `firm`
   ```
2. **Drifted-line presence (verify the pre-drift citations exist on disk):**
   ```
   $ grep -n "laplaceoperator.cpp:191\|curlcurloperator.cpp:179" book/src/L1/fe_assemble.md
   134:   = the permittivity-weighted diffusion operator (`palace/models/laplaceoperator.cpp:191-192`).
   166:  ... ∇/Gradient (electrostatic diffusion, `palace/models/laplaceoperator.cpp:191-192`)
   167:  and ∇×/Curl (magnetostatic curl-curl, `palace/models/curlcurloperator.cpp:179-181`) ...
   ```
   → 3 pre-drift loci confirmed. The c068 D2 dissolution theme re-anchored to the correct lines (`laplaceoperator.cpp:193-196`, `curlcurloperator.cpp:180-181`, `spaceoperator.cpp:278`); the firm L1 cap still carries the +2/+3 stale pre-drift cites (out of D2's append-only write-scope).
3. **OQ-ledger RESOLVED-grep:** `grep 'fe-assemble-l1-cap-weak-form-term-witness-line-drift-reanchor.*RESOLVED'` → no matches; OPEN (opened cycle-068; trigger = "a future lifter / citation-hygiene pass").
4. **Structural-block check:** none. Pure citation hygiene; STRUCTURE unaffected (only witness line numbers). **Close-brace on-disk-Read discipline:** the new END lines (`:193-196`, `:180-181`) are codemap-derived hints from the c068 D2 re-anchor — the producer MUST on-disk-`Read` the `AddDomainIntegrator<...>` call + the closing context before committing the new ranges (the `codemap-read-range-plus-one-drift-on-brace-boundary` recurrence-6 watch; do NOT trust `citecheck --anchor` for the END).
   → RECRUIT.

### #3 `eliminate_essential_bc` / `eliminate_rhs` → L4 (ranks 3-4) — **DEFERRED this cycle (gate FAILS)**
The c067 D2 caveat (1) is a LOAD-BEARING pre-landing gate: "`eliminate_rhs`'s L4 form composes `apply_linop`+`axpy`+`set_essential`; verify primitive-L4-presence before landing, else degenerate L4 mirror."
```
$ ls book/src/L4/apply_linop.md book/src/L4/axpy.md book/src/L4/set_essential.md
ls: cannot access 'book/src/L4/apply_linop.md': No such file or directory
ls: cannot access 'book/src/L4/axpy.md': No such file or directory
ls: cannot access 'book/src/L4/set_essential.md': No such file or directory
$ ls book/src/L4/   # full L4 dir: chebyshev eigsolve fe_assemble fold_solve index inner_product
                    # iterate-while iterate-while-with-prev krylov-step ksp_solve linear_combination solve_family
```
`eliminate_rhs.md:55-57` confirms the composition (`b' = axpy(-1, apply_linop(K, restrict_essential(x_bc)), b)` then `set_essential(b', pin)`); `eliminate_essential_bc.md` is a row/col-zeroing projection on the same `apply_linop`-class object. **NONE of the three composed primitives is at L4** (`axpy` is an accelerated-kernel-stopped-low note under `L4/linear_combination`, not its own chapter; `apply_linop`/`set_essential` absent). Authoring `L4/eliminate_rhs` now would manufacture exactly the degenerate L4 mirror the caveat rejects (identity-skip on absent primitives + a thin composition). **DEFER** — route to the batch-21 meta-phase to decide whether `apply_linop`/`set_essential` should rise (and whether `essential_dofs` gets the thin L4 input-declaration chapter per the `fe-assemble-l4-construction-input-absorb-reopen-on-downstream-demand` re-open trigger). Recorded as a plan candidate (below). Not recruited this cycle.

## Dispatches

- **D1** — agent: `harvester`; scope: **`book/src/L4/assemble_frequency_operator.md`** — lift the firm L1 `assemble_frequency_operator` to L4 **through `L4/linear_combination`'s operator-operand corner** (the operand-category variant axis `tensor-operand | operator-operand`, already extended at L2+L3 in c062; replace-and-propagate, NOT a mirrored `operator_linear_combination` fold). WARRANT-FIRST: judge whether this is a genuine L4 entry (the driven per-ω system operator `A(ω)=K+iωC−ω²M` as the operator-operand specialization of `linear_combination`'s fold, single-pipeline-by-design driven) OR a thin specialization note under `L4/linear_combination` — author per warrant. Re-express through the firm L1 cap's already-on-disk anchors (`drivensolver.cpp:176-180`, `:91-93`, `:175`, `:180`; `spaceoperator.cpp:521-528`; `rap.cpp:764-787` `BuildParSumOperator` — confirmed via codemap this cycle, the scalar-weighted operator-fold the operator-operand `linear_combination` corner names); do NOT re-localize source — the L1 cap is firm-on-positive-structure. This is the driven pipeline's ASSEMBLE half reaching L4 (NOT the solve half — that is the meta-phase's call). **Cite the `disciplined-cross-pipeline-combinator-mining-gate` skill** for the single-pipeline-by-design specialization framing (no 2nd-pipeline discharge owed — the operand-category generality comes from the firm tensor-operand BLAS-1 cohort + this operator-operand witness). Adds its OWN `L4/index` dep-map ROW + §Vocabulary-cohort BULLET (alpha position per directive-3) + SUMMARY L4 insert (alpha position inside the L4 group); **DEFERS the consolidated `L4/index` firm tally to D2 (sole count-owner this cycle).** deps: none.
  - rationale: rank-2 FE-cohort→L4 lift, NOW UNBLOCKED (the `linear_combination`-rises gate cleared c068 D3). Plan-tag `assemble-frequency-operator-l4-lift`. HIGH fan-out (the driven pipeline's assemble-half L4 reach; the per-ω operator the driven sweep needs at the feature surface).

- **D2** — agent: `harvester`; scope: **`book/src/L4/dot.md` + `book/src/L4/nrm2.md`** (paired named-verb cohort) — rise the kept named abstractions to L4 as named verbs through the now-firm `L4/inner_product` (directive-2 disposition-2 keep-and-rise): **`dot`** = Hermitian/symmetric `inner_product` at `M = I` (a named specialization verb); **`nrm2`** = `√ ∘ abs ∘ inner_product` at the diagonal `y = x` — a CONSUMER of the inner-product fold, NOT a fold member (**do-NOT-merge over-unification guard** — `nrm2` does not merge into `inner_product`). Author both as the literature-standard named units (`dot(p, Ap)`, residual `nrm2(r)`) the CG/GMRES descriptions want, kernel tied below (the firm `L3/dot`/`L3/nrm2`), parent combinator `L4/inner_product` cross-referenced as the permitted dual. Re-express through `L4/inner_product` — do NOT re-derive the fold. If the author finds either verb carries non-trivial distinct content warranting separate dispatches, it MAY note the split for a follow-on (judgment per the redirect's one-operator-per-dispatch; the pairing is justified because both are thin re-expressions through one firm combinator). **D2 is the SOLE `L4/index` count-owner this cycle:** it owns the consolidated firm-count tally bump (`10 + 4 outer-driver` → `12 + 4` if D1 lands as a genuine entry + both named verbs land; count from the `## Status` lines of all landed L4 chapters per the c057-meta guard, reconciling D1's + its own landings) + the §"Firm at L4" frontier prose + the `:66` per-case disposition line if it needs a named-verb touch. It adds its OWN 2 dep-map ROWS + 2 §Vocabulary-cohort BULLETs (alpha position) + 2 SUMMARY L4 inserts (alpha position). deps: none (independent of D1 at the chapter level; D1 DEFERS the tally to D2 so the count reconciles in one place).
  - rationale: OQ `l4-dot-nrm2-named-verb-next-pull` trigger fires (planner picks them as next-pull). Plan-tag `l4-dot-nrm2-named-verb-rise`. MEDIUM-HIGH fan-out (the named verbs every Krylov/eigen solver description reuses at the feature surface).

- **D3** — agent: `lifter`; scope: **`book/src/L3/linear_combination.md` + `book/src/L3/inner_product.md`** (in-place re-anchor, NO new chapter) — flip the 4 stale "no L4 entry" loci to point at the now-firm L4 entries: `L3/linear_combination.md:8` (frontmatter `lifts_from`) + `:29` (body prose) → "lifts to [`L4/linear_combination`](../L4/linear_combination.md) (firm cycle-068; identity-in-form on the body, no dedicated L4>L3 theme — the in-line-marker route)"; `L3/inner_product.md:8` (frontmatter) + `:75-76` (§Context prose, the "No `L4/inner_product` exists — folds/leaves are not first-class L4 vocabulary (cycle-010 audit)" assertion) → the parallel "lifts to [`L4/inner_product`](../L4/inner_product.md) (firm cycle-068; ...)". This is the IDENTICAL routine the `eigsolve` cap (c048) triggered for the seven stale `L3/eigsolve` §Upward "no L4 cap" assertions. Both L3 entries stay `firm`; STRUCTURE + laws unaffected (only the upward-cap pointer). deps: none.
  - rationale: OQ `l3-data-algebra-combinators-stale-no-l4-reanchor` trigger fires. Plan-tag `l3-data-algebra-no-l4-reanchor`. LOW fan-out (cheap clean close; removes a factually-stale assertion the c068 landings invalidated).

- **D4** — agent: `lifter`; scope: **`book/src/L1/fe_assemble.md`** (in-place citation-hygiene re-anchor, NO new chapter) — re-anchor the 3 pre-drift weak-form-term witness citations to the c068-D2-verified correct lines: `:134` and `:166` `laplaceoperator.cpp:191-192` → `:193-196` (the `AddDomainIntegrator<DiffusionIntegrator>(epsilon_func)` call `:194` + `BilinearForm k(GetH1Space())` `:193` + `k.Assemble(...)` `:196`); `:167` `curlcurloperator.cpp:179-181` → `:180-181`; add/confirm `spaceoperator.cpp:278` if cited. **Close-brace on-disk-Read discipline (recurrence-6):** the new END lines are codemap-derived hints from the c068 D2 re-anchor — on-disk-`Read` the integrator-call lines + surrounding context to confirm the exact ranges before committing; do NOT trust `citecheck --anchor` for the END (it is blind to range-END off-by-one). `fe_assemble.md` stays `firm`; STRUCTURE unaffected. deps: none.
  - rationale: OQ `fe-assemble-l1-cap-weak-form-term-witness-line-drift-reanchor` trigger fires. Plan-tag `fe-assemble-l1-cap-witness-reanchor`. LOW fan-out (cheap hygiene; the standard codemap +1 boundary drift, the firm cap's only defect is stale line numbers). Could bundle with D3 (both `lifter` re-anchors) but targets a DISJOINT file → kept separate, parallel-safe.

## Overlap analysis

Pairwise (4 dispatches → 6 pairs):

- **D1 × D2** — **POTENTIAL OVERLAP at `book/src/L4/index.md`** (both land new L4 chapters → both touch the L4-index dep-map TABLE + §Vocabulary-cohort cohort, and both bear on the consolidated firm tally) AND **`book/src/SUMMARY.md`** (both insert L4 chapter entries). Resolved by the DUAL-REGISTRATION + count-ownership partition: each producer OWNS (1) its own dep-map ROW(s) (anchor-distinct, alpha-position — parallel-safe) AND (2) its own §Vocabulary-cohort BULLET(s) (anchor-distinct — parallel-safe) AND (3) its own SUMMARY insert(s) (alpha-position, distinct anchors); **D2 (sole count-owner) owns ONLY (4) the consolidated firm tally + frontier prose + any `:66` touch.** D1 DEFERS the tally to D2 explicitly. This is the c068 pattern exactly (D1 deferred the firm tally to D3 the count-owner; reconciled in one place from `## Status` lines). The distinct-row/bullet/SUMMARY-insert writes are NON-overlapping at the operational level → parallel-safe per the §Discipline "distinct dep-map rows are parallel" rule. The single genuine shared-mutable value (the tally) has exactly one owner (D2). **PARALLEL** (the count-ownership partition handles the only true shared region; the SUMMARY alpha-inserts are in distinct anchor regions — per-report integrator serializes the application order regardless, and minor wave conflict at integration is useful signal per the conflict-tolerance philosophy).
- **D1 × D3** — no shared region. D1 lands `L4/assemble_frequency_operator.md` + touches `L4/index`/SUMMARY; D3 edits `L3/linear_combination.md` + `L3/inner_product.md` (L3 chapters, no index/SUMMARY touch — pointer flips inside existing chapters). DISJOINT. **PARALLEL.**
- **D1 × D4** — no shared region. D4 edits `L1/fe_assemble.md` only. DISJOINT. **PARALLEL.**
- **D2 × D3** — no shared region. D2 at L4 + index/SUMMARY; D3 at L3 chapters. DISJOINT. **PARALLEL.**
- **D2 × D4** — no shared region. DISJOINT. **PARALLEL.**
- **D3 × D4** — no shared region. D3 edits two L3 chapters; D4 edits one L1 chapter. DISJOINT. **PARALLEL.** (Both are `lifter` re-anchors but operate on different files; no shared operator name, no shared file region.)

No two dispatches modify the same operator entry or rewrite the same theme body. The only shared mutable derived value (`L4/index` firm tally) is sole-owned by D2.

## Sequencing schedule

**Single wave — all 4 dispatches PARALLEL.** No forward-reference dependency requires staging (D1's `assemble_frequency_operator` already has its forward-reference recorded at `L4/linear_combination.md:40` from c068; D2's `dot`/`nrm2` are recorded as next-pull notes at `L4/inner_product.md:35`; D3/D4 are self-contained re-anchors). The per-report integrator applies the 4 reports serially (artifact writes naturally serialize); the count-ownership partition (D2 sole tally-owner; D1 defers) means the `L4/index` firm count reconciles in one place from the landed `## Status` lines regardless of per-report application order. Forward-reference resolution: D1/D2's new L4 chapters are referenced by the existing `L4/index` and `L4/{linear_combination,inner_product}` next-pull notes — those become live links when the chapters land (per-report integrator wires them); no inter-wave book rebuild needed (one `integrator-finalize` at cycle end).

- **Wave 1 (parallel):** D1, D2, D3, D4.

Pipeline: planner → 4 dispatches (wave 1) → 4 critics → repairers (as needed) → `integrator-per-report` ×4 (serial) → ONE `integrator-finalize`.

## Open questions / caveats

- **`assemble_frequency_operator` warrant (D1) is genuinely open** — the harvester may find it lands as a thin specialization note under `L4/linear_combination` rather than a standalone L4 chapter (the operator-operand specialization may not earn a separate entry). If so, D1 produces no new L4 chapter (the note lands inside `L4/linear_combination`) and the D2 count-owner tally bumps by the named-verbs only. The warrant-first framing handles this — flagged so the integrator does not treat a note-disposition as a missing deliverable.
- **D2 paired-cohort vs split** — I scheduled `dot`+`nrm2` as ONE dispatch (both thin re-expressions through the single firm `L4/inner_product`, tightly coupled, c068 D3 deferred both together). If the producer finds either carries non-trivial distinct content, it may note a split for a follow-on cycle. Acceptable per the redirect's combinator-as-entry / one-substantive-operator discipline (these are two NAMED VERBS over one combinator, not two combinators).
- **#3 `eliminate_*`→L4 DEFERRED with evidence (gate fails)** — routed to the batch-21 meta-phase: the L4-thinness primitives `apply_linop`/`axpy`/`set_essential` are absent from L4 (verified inline above), so `eliminate_rhs`/`eliminate_essential_bc` would land as degenerate L4 mirrors. The meta-phase should decide whether `apply_linop`/`set_essential` rise (and whether `essential_dofs` gets the thin L4 input-declaration chapter per the `fe-assemble-l4-construction-input-absorb-reopen-on-downstream-demand` re-open trigger). Appended as a plan candidate.
- **THREE items the batch-21 meta-phase (fires after this cycle's finalize) MUST pick up:**
  1. **The driven-solve→L4 decision** (OQ `driven-solve-half-l4-completeness-vs-map-solve-single-witness-stop`) — the USER-steered methodology tension: lift driven's solve half to L4 (override the c058 single-witness `map_solve` STOP under the completeness directive) vs record driven-solve-at-L1 as a deliberate scope boundary. Cycle-069 did NOT act on it; the STOP-PROPOSING `map_solve` entry stayed in force this cycle. The meta-phase reconciles the STOP entry with the L4-completeness directive either way.
  2. **The directive-3 mdBook by-kind sub-chapter grouping + global alpha re-sort reorg** (OQ `concepts-list-global-alpha-resort-vs-local-cluster-insert`) — the one-time heavy `book/`-structure pass + the role-spec codification (restart-pending; `.claude/agents/` is meta-phase-owned). Cycle-069 did NOT seed it (forward-frontier cycle; directive-3 reserves the reorg as its own structural wave / the meta-phase).
  3. **The directive-4 `methodology/goal-flow.md` ownership transfer** (OQ `methodology-goal-flow-chapter-ownership-transfers-to-meta-phase-post-seed`) — the v1 seed is on disk (c067 D4, verified present this cycle); the meta-phase adopts it as a standing per-batch refresh target + codifies the target into `meta-phase.md` (restart-pending).
- **No methodology-adjustment pattern surfaced this cycle that the friction-ledger is missing** — the recurring `codemap-read-range-plus-one-drift-on-brace-boundary` (recurrence-6, addressed) is handled by D4's close-brace on-disk-Read discipline; no new escalating pattern observed mid-batch.

## priorities.md updates made this cycle

Appended a `## CYCLE-069 PICKS` block under the batch-21 active head recording D1-D4 as dispatched with paste-evidence pointers, the #3 `eliminate_*`→L4 DEFER-with-gate-evidence, and three fresh plan candidates: (a) `eliminate-star-l4-gate-meta-phase` (the `apply_linop`/`set_essential`-rise + `essential_dofs`-L4-chapter decision, routed to batch-21 meta), (b) the three carried meta-phase items (driven-solve→L4, directive-3 reorg, directive-4 ownership) confirmed as meta-phase-owned. No re-rank of the existing backlog.

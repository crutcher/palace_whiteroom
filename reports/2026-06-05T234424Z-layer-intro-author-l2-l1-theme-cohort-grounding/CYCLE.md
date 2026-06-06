---
agent: layer-intro-author
invoked_at: 2026-06-05T234424Z
scope: cycle-109 D1 — graded-stack L2-L1 theme-cohort grounding (batch-35 LEAD)
status: pending
integrated_at: 2026-06-06T000500Z
integration_commit: aaf36ed
integration_notes: |
  Applied clean by integrator-per-report (staging row status: applied) + finalized cycle-109 (batch-35 position 1/3, the OPENING cycle). All 5 frontmatter-only `edges:` edits landed verbatim to book/src/L2/{eigsolve,ksp_solve,krylov-step,linear_combination,inner_product}.md (the from-scratch `edges:` block on krylov-step + 3 ADD/UPGRADE + 1 cheap edge-lay). cargo make book EXIT 0, linkcheck2 clean (frontmatter-only, every edge target on-disk; no SUMMARY/index insert; only pre-existing benign markdown-table bracket WARNs). Step-5b graded-stack linter on the LANDED tree: rank_violations 0 (GATE PASSES; baseline discharged c096 so any violation would be NEW — none), NO newly-orphaned node, unresolved_depends_on_targets 0; reachable 102→107 (+5; the +5-vs-+4 surplus is L2/krylov-step itself becoming typed-and-reachable), detritus 157→152, STRONGER GARBAGE SIGNAL 35→34, untyped HELD 60, promotion_frontier 8. The 4 Group-A themes flipped out of [garbage?]; the 5 Group-B themes + inner-product-fold + deflate remain [garbage?] (the structured finding). Repair phase ran (one low-severity rank-invariant warning repaired in-place by rationale-only prose softening; the edges: blocks untouched). citecheck: 9 ok / 2 AMBIG on report-PROSE bare-basenames (non-blocking; no prose-claim text lands in book/). OQs promoted: l2-reduce-orthogonalize-cohort-itself-unreachable-blocks-theme-grounding (the Group-B next-tranche blocker), l1-blas-leaves-axpy-family-lack-rank-frontmatter. No firm-count status flips (all frontmatter-only edge-typing). The batch-35 meta-phase fires after cycle-111's finalize, aggregating 109/110/111.
---

# CYCLE: graded-stack-l2-l1-theme-cohort-grounding (the bounded reachable-op tranche + Group-B finding)

## Summary

The batch-35 LEAD: the bounded one-edge-per-theme GROUNDING pass over the L2-L1 lowering-theme cohort,
applying the §(g) GROUND-don't-remove disposition as **faithful-path-or-finding**. The cohort's themes
stay `[garbage?]` because the `lowers-to` edge convention points operator→operator and never
operator→theme, so a lowering theme has no inbound `depends-on` from a reachable node. The fix is to add
a faithful `lowers-to`-kind `depends-on` edge `L2/<op> → L2-L1/<theme>` on each host op (mirroring the
c108 `L2/divfree-projector` block-mapping precedent, `book/src/L2/divfree-projector.md:11-17`).

**On-disk verification confirmed the planner's FAITHFUL-PATH-OR-FINDING split exactly:**
- **4 Group-A themes** (host L2 op itself reachable) → GROUNDED this cycle; all 4 flipped out of `[garbage?]`.
- **1 cheap faithful edge-lay** (`inner_product`) → edge typed (faithful + correct) but does NOT flip its
  theme reachable because `L2/inner_product` is itself `[GARBAGE*]`. Documented, not a failure.
- **5 Group-B themes** (host L2 op itself unreachable) → ROUTED as a structured finding (OQ filed). The
  faithful `lowers-to` is real for all 5, but the one-edge fix cannot flip them; the next tranche is
  grounding the off-spine L2 reduce/orthogonalize/chebyshev cohort.
- **`deflate` / `deflate-composition-lowering`** → NOT TOUCHED (demand-gated FRONTIER member,
  STOP-PROPOSING negative list).

**Linter result (verified by applying the edits, running the lint, then reverting to keep `book/` clean
for the dispatch phase — see §Verification):** `reachable 102 → 107` (+5; **exceeds** the predicted +4
because authoring `L2/krylov-step`'s `edges:` block from scratch also makes `L2/krylov-step` itself a
typed-and-reachable node, not only its theme), `rank_violations` HOLDS **0**, `untyped` HOLDS **60**,
`detritus 157 → 152` (−5). All five edits are **frontmatter-only** (no prose claims).

## Faithfulness confirmations (theme prose / dependency citations)

Each `lowers-to` was confirmed REAL from the theme/host chapter prose before typing:

1. **`L2/eigsolve → L2-L1/eigsolve-spectral-transform-composition`** — confirmed at
   `book/src/L2/eigsolve.md:171` (§"Lowers from"): *"The L2>L1 theme narrating this opening forward is
   `L2-L1/eigsolve-spectral-transform-composition` (firm, landed cycle-025)."* The theme chapter itself
   (`book/src/L2-L1/eigsolve-spectral-transform-composition.md`) is the forward L2→L1 narration of the
   `apply_shift_invert = apply_linop ▷ ksp_solve` body opening/re-collapse. FAITHFUL.

2. **`L2/ksp_solve → L2-L1/ksp-solve-outer-driver-unfold`** — confirmed at
   `book/src/L2-L1/ksp-solve-outer-driver-unfold.md:1-21`: the theme is explicitly *"the L2>L1 lowering
   theme for the `ksp_solve` outer-driver composition … the downward edge of the firm L2 `ksp_solve`
   driver"*, the canonical L2↔L1 edge (kernel-fold composition ⟷ opaque solver-as-operator). FAITHFUL.

3. **`L2/krylov-step → L2-L1/krylov-step-kernel-defusion`** — confirmed at
   `book/src/L2-L1/krylov-step-kernel-defusion.md:1-12`: the theme *"Lowers the firm L2 named composition
   `krylov-step` … into its L1 form by expanding the five-primitive-group step body into the explicit
   sequence of seven firm L1 leaves"*. FAITHFUL. The seven firm L1 leaves typed in the from-scratch
   `depends-on` are the chapter's OWN §Dependencies at `book/src/L2/krylov-step.md:96`
   (`apply_linop, axpy, axpby, axpbypcz, dot, nrm2, scal` — "All firm post-cycle-004"). Concept
   `reference` targets are the chapter's §Dependencies cross-cutting list at
   `book/src/L2/krylov-step.md:101-108`. Well-foundedness: krylov-step firm (rank 3) resting on firm L1
   leaves (rank 3) → holds firm→firm.

4. **`L2/linear_combination → L2-L1/linear-combination-fold-specialization`** (UPGRADE from `reference`)
   — confirmed at `book/src/L2-L1/linear-combination-fold-specialization.md:1-12`: the theme *"Lowers the
   L2 variadic fold `linear_combination` into its L1 fixed-arity leaf … by selecting the maximal fused L1
   primitive that matches the fold's term-list length"*. FAITHFUL. The line currently sits in `reference`
   (`book/src/L2/linear_combination.md:14`) — a navigational `reference` creates NO reachability
   (the c106-D4 lesson); the upgrade to `depends-on lowers-to` is what flips the theme.

5. **`L2/inner_product → L2-L1/inner-product-fold-specialization`** (UPGRADE from `reference`; cheap
   edge-lay) — confirmed at `book/src/L2-L1/inner-product-fold-specialization.md:1-12`: the theme
   *"Lowers the L2 reduce-to-scalar fold `inner_product` … into its L1 leaf — `dot` (Hermitian), the
   unconjugated `tdot` …, or the M-weighted member realized by `bilinear-form`"*. FAITHFUL. **This edge is
   correct but does NOT flip the theme reachable this cycle** because `L2/inner_product` is itself
   `[GARBAGE*]` (its only inbound `depends-on` is from the unreachable `L3/dot` / `L3/inner_product`).
   The edge is laid for when the reduce cohort grounds (next tranche).

## Proposed changes

All edits are YAML-frontmatter-only. The block-mapping edge form (`- target: … / kind: …`) matches the
c108 `L2/divfree-projector` precedent. Verified to parse cleanly (no linter parse error) and to produce
the reachability flips below.

### 1. `book/src/L2/eigsolve.md` — ADD `lowers-to` to existing `depends-on`

```edit:book/src/L2/eigsolve.md
[old]:
  depends-on:
    - L2/ksp_solve
    - L1/apply_linop
  reference:
    - L1/eigsolve
[new]:
  depends-on:
    - L2/ksp_solve
    - L1/apply_linop
    - target: L2-L1/eigsolve-spectral-transform-composition
      kind: lowers-to             # the L2>L1 lowering theme this composition lowers through (theme prose :171)
  reference:
    - L1/eigsolve
```

### 2. `book/src/L2/ksp_solve.md` — ADD `lowers-to` to existing block-mapping `depends-on`

```edit:book/src/L2/ksp_solve.md
[old]:
  depends-on:
    - target: L3/ksp_solve
      kind: lifts-to
    - target: L1/ksp_solve
      kind: lowers-from
[new]:
  depends-on:
    - target: L3/ksp_solve
      kind: lifts-to
    - target: L1/ksp_solve
      kind: lowers-from
    - target: L2-L1/ksp-solve-outer-driver-unfold
      kind: lowers-to             # the L2>L1 lowering theme: kernel-fold composition re-collapses into the L1 opaque operator
```

### 3. `book/src/L2/krylov-step.md` — AUTHOR `edges:` frontmatter block FROM SCRATCH

The file currently begins at line 1 with `# krylov-step` (no frontmatter). Prepend the block (mirrors the
c108 `L2/divfree-projector` from-scratch authoring). The 7 firm L1 leaves are the chapter's own
§Dependencies (`:96`); the concept references are §Dependencies cross-cutting list (`:101-108`).

```edit:book/src/L2/krylov-step.md
[old]:
# krylov-step

Pure-functional step kernel for iterative Krylov-shaped solvers
[new]:
---
layer: L2
operator: krylov-step
# Graded-stack scheme (authored from scratch, batch-35 c109; mirrors the c108 L2/divfree-projector
# from-scratch authoring). This firm L2 fold-kernel rests on its seven firm L1 leaves (depends-on)
# AND lowers through the L2>L1 kernel-defusion theme (lowers-to depends-on; mirrors how L1 ops reach
# their L1>L0 theme). The firm L1 leaf list is the chapter's own §Dependencies (:96). This node firm
# (rank 3). Of the seven L1 leaf targets, apply_linop/dot/nrm2/scal carry rank: firm; axpy/axpby/axpbypcz
# carry no rank token yet (typed-no-rank), so the rank invariant holds vacuously over those three edges
# (a no-rank target cannot be a rank violation) — rank_violations remains 0 either way.
rank: firm
edges:
  depends-on:
    - L1/apply_linop
    - L1/axpy
    - L1/axpby
    - L1/axpbypcz
    - L1/dot
    - L1/nrm2
    - L1/scal
    - target: L2-L1/krylov-step-kernel-defusion
      kind: lowers-to             # the L2>L1 lowering theme this kernel composition lowers through
  reference:
    - concepts/solver-as-operator
    - concepts/derived-view-hoisting
    - concepts/variant-absorption
    - concepts/first-iteration-unrolling
    - concepts/sequential-obstruction
    - concepts/solve-monad
    - concepts/state-stratification
    - concepts/apply_BA
    - concepts/orthogonalization
    - concepts/constructed-operators
---

# krylov-step

Pure-functional step kernel for iterative Krylov-shaped solvers
```

### 4. `book/src/L2/linear_combination.md` — UPGRADE `reference`→`depends-on lowers-to`

REMOVE the `L2-L1/linear-combination-fold-specialization` line from `reference`; ADD it to `depends-on`
as a `lowers-to` edge (a navigational `reference` creates no reachability — c106-D4 lesson).

```edit:book/src/L2/linear_combination.md
[old]:
  depends-on:
    - L1/scal
    - L1/axpy
    - L1/axpby
    - L1/axpbypcz
  reference:
    - concepts/scalar-promotion
    - L2/inner_product
    - L2-L1/linear-combination-fold-specialization
[new]:
  depends-on:
    - L1/scal
    - L1/axpy
    - L1/axpby
    - L1/axpbypcz
    - target: L2-L1/linear-combination-fold-specialization
      kind: lowers-to             # UPGRADED from reference: the L2>L1 lowering theme this variadic fold lowers through (reachability-bearing)
  reference:
    - concepts/scalar-promotion
    - L2/inner_product
```

### 5. `book/src/L2/inner_product.md` — UPGRADE `reference`→`depends-on lowers-to` (cheap edge-lay; does NOT flip reachable)

Same upgrade as #4. State EXPLICITLY (also in the OQ below): faithful + correct, but does NOT flip the
theme reachable this cycle because `L2/inner_product` is itself `[GARBAGE*]`.

```edit:book/src/L2/inner_product.md
[old]:
  depends-on:
    - L1/dot
    - L1/bilinear-form
    - L1/apply_linop
  reference:
    - L2/linear_combination
    - concepts/dot
    - L2-L1/inner-product-fold-specialization
[new]:
  depends-on:
    - L1/dot
    - L1/bilinear-form
    - L1/apply_linop
    - target: L2-L1/inner-product-fold-specialization
      kind: lowers-to             # UPGRADED from reference: faithful L2>L1 lowering theme edge (does NOT flip reachable yet — L2/inner_product is itself unreachable)
  reference:
    - L2/linear_combination
    - concepts/dot
```

## Verification (mandatory — applied edits, ran lint, reverted to clean `book/`)

I applied the 5 edits to `book/`, ran `python3 tools/graded-stack-lint/graded_stack_lint.py
--show-inbound`, recorded the result, then `git checkout`-reverted all 5 files so `book/` is clean for the
dispatch phase (the integrator re-applies from the proposed-changes blocks above). Confirmed
`git status --short book/` is empty post-revert.

**Before (baseline `fd5fabd`, matches planner):**
```
files scanned: 355 ; typed nodes: 295 ; untyped (WARNING): 60 ; feature roots: 36
AXIS 1 — RANK VIOLATIONS: none.  (rank_violations = 0)
AXIS 2 — reachable from roots: 102
DETRITUS: 157
```

**After (5 edits applied):**
```
files scanned: 355 ; typed nodes: 295 ; untyped (WARNING): 60
AXIS 1 — RANK VIOLATIONS: none.  (rank_violations = 0)
AXIS 2 — reachable from roots: 107
DETRITUS: 152   (STRONGER GARBAGE SIGNAL 35→34 ; edge-untyped artifact 122→118)
```

**(i) The 4 Group-A themes flip OUT of `[garbage?]`** — confirmed by grep of the post-edit garbage list:
`eigsolve-spectral-transform-composition`, `krylov-step-kernel-defusion`, `ksp-solve-outer-driver-unfold`,
`linear-combination-fold-specialization` are NO LONGER present. **(reachable 102 → 107, +5)** — the +5
(vs predicted +4) is `L2/krylov-step` itself becoming a typed-and-reachable node when its `edges:` block
is authored from scratch (it is reached via `L4/krylov-step → L3/krylov-step → L2/krylov-step`-style
inbound), in addition to its 4 sibling theme flips.

**(ii) `rank_violations` HOLDS 0** — `AXIS 1 — RANK VIOLATIONS: none.` Every host node is firm (rank 3).
Of the new `depends-on` targets: the theme targets and `apply_linop`/`dot`/`nrm2`/`scal` carry
`rank: firm` (well-foundedness holds firm→firm over those edges); `axpy`/`axpby`/`axpbypcz` carry no rank
token yet (`typed-no-rank`), so the `rank(u) ≤ rank(v)` invariant holds **vacuously** over those three
edges — a no-rank target cannot register a violation — and `rank_violations` stays 0. (The latent gap that
these three high-fan-out L1 BLAS leaves lack `rank:`/`edges:` frontmatter is filed as an OQ; see below.)

**(iii) The 5 Group-B themes + deflate REMAIN `[garbage?]`** (expected; the finding) — confirmed by grep:
`chebyshev-iteration-fusion`, `gram-fold-specialization`, `incremental-least-squares-composition-lowering`,
`inner-product-fold-specialization`, `orthogonalize-composition-lowering` all still `[garbage?]`;
`deflate-composition-lowering` still `[FRONTIER] / [garbage?]` (untouched). `L2/inner_product` still
`[GARBAGE*]` (confirming edit #5's edge-lay did not flip its theme — correct, documented).

No YAML parse errors on the from-scratch `L2/krylov-step` block.

## Supporting evidence

- c108 block-mapping `lowers-to` precedent: `book/src/L2/divfree-projector.md:11-17` (the from-scratch
  `edges:` shape mirrored for `L2/krylov-step`).
- Per-theme faithful-edge table + linter baseline: planner CYCLE
  `reports/2026-06-05T234424Z-cycle-planner-cycle-109/CYCLE.md` (rows 1-10, §Group-B root cause).
- Theme-prose faithfulness citations: enumerated in §Faithfulness confirmations above
  (`eigsolve.md:171`; the four theme chapter heads; `krylov-step.md:96` for the firm L1 leaf list).

## Open questions

### New OQ (Group-B finding — route to the batch-35 meta-phase)

```append:scaffolding/open-questions.md

## OQ: l2-reduce-orthogonalize-cohort-itself-unreachable-blocks-theme-grounding

- **status:** OPEN — filed cycle-109 (batch-35 LEAD D1, the Group-B finding from the L2-L1 theme-cohort
  grounding pass).
- **observation.** The batch-35 LEAD `graded-stack-l2-l1-theme-cohort-grounding` assumed all ~10 L2-L1
  lowering themes are `[garbage?]` for ONE reason: the `lowers-to` edge convention pointed
  operator→operator and never operator→theme. On-disk that holds for the *theme edge*, but for **5 of the
  remaining themes** there is a SECOND, dominating reason — the **upper-endpoint L2 op is ITSELF
  unreachable**. Adding a faithful `L2/<op> →lowers-to→ theme` edge from an unreachable op cannot flip the
  theme: the mark-sweep never reaches the op. The 4 themes whose host op is on-spine were grounded cleanly
  this cycle (reachable 102→107). The 5 blocked themes + their unreachable host ops:
  - `L2-L1/inner-product-fold-specialization` — host `L2/inner_product` is `[GARBAGE*]` (only inbound from
    unreachable `L3/dot`, `L3/inner_product`). The faithful `lowers-to` edge WAS laid this cycle (edit #5),
    correct but non-flipping until the reduce cohort grounds.
  - `L2-L1/chebyshev-iteration-fusion` — host `L2/chebyshev-iteration` `[garbage?]` (only inbound
    `L3/chebyshev`, unreachable).
  - `L2-L1/gram-fold-specialization` — host `L2/gram` `[garbage?]`.
  - `L2-L1/incremental-least-squares-composition-lowering` — host `L2/incremental-least-squares` `[garbage?]`.
  - `L2-L1/orthogonalize-composition-lowering` — host `L2/orthogonalize` `[garbage?]`.
  The faithful `lowers-to` relationship is REAL for all 5 (theme prose confirmed); the one-edge LEAD shape
  simply cannot reach them.
- **root cause.** These L2 reduce / orthogonalize / iteration ops are off-spine: their only inbound
  `depends-on` edges come from L3 ops that are THEMSELVES off-spine (`L3/dot`, `L3/inner_product`,
  `L3/chebyshev`, `L3/orthogonalize`, `L3/gram`, `L3/krylov-step`, … all in the STRONGER GARBAGE
  SIGNAL / detritus set). No driver/feature column reaches the L2/L3 reduce/orthogonalize cohort via a
  live `depends-on` path.
- **recommended next tranche.** Grounding the L2 reduce / orthogonalize / chebyshev cohort — a larger,
  structurally-distinct pass that traces up through the unreachable L3 reduce/iteration cohort (NOT the
  bounded one-edge-per-theme LEAD shape). Once an L2 reduce/orthogonalize op is itself reachable, its
  already-laid (inner_product) or to-be-laid (chebyshev/gram/ils/orthogonalize) theme edge flips it
  automatically. The deeper question is whether the L3 reduce/iteration cohort grounds via (a) a faithful
  `depends-on` edge from a reachable consumer (the GROUND-don't-remove §(g) disposition), or (b) is judged
  absorbed-below-column detritus (the c107 BC/divfree baseline-exception pattern).
- **NOTABLE for the meta-phase to judge (the c107 disposition pattern).** `L2/inner_product` being
  `[GARBAGE*]` while it is a **high-fan-out reduce-to-scalar combinator** is itself notable: a high-reuse
  reduce verb unreachable from any feature root means the reduce cohort (`dot`/`inner_product`/`nrm2` at
  L2/L3) has NO live `depends-on` path from a driver column. This is either (a) a genuine spine gap — a
  driver/output-product column SHOULD `depends-on` a reduce verb somewhere (e.g. the residual-norm /
  energy / gram reductions a solve performs) — to be GROUNDED from the column; OR (b) an expected
  absorbed-below-column situation like the BC/divfree clusters (c107), to be tracked as a
  baseline-exception. The meta-phase should make the ground-from-column-vs-absorbed-detritus call (the
  c107 disposition pattern). Recommended bias: GROUND from the column where a faithful, honestly-typed
  `depends-on` path exists (the reduce verbs are genuine constituents of the solve/postprocess columns),
  per §(g) preference order (GROUND > ROUTE > DELETE).
- **NOT a failed dispatch.** This is the legitimate faithful-path-or-finding outcome: the 4 clean themes
  grounded, the 5 blocked themes routed with the root cause + next-tranche recommendation. `deflate` /
  `deflate-composition-lowering` correctly stay garbage (demand-gated FRONTIER member, STOP-PROPOSING list)
  and are excluded by design, not omitted.
```

## Caveats

- **`deflate` excluded by design.** `L2/deflate.md` / `L2-L1/deflate-composition-lowering.md` are a
  demand-gated FRONTIER member (opaque-library `nleps_deflated_*` deps) on the STOP-PROPOSING negative
  list; the redirect forbids forcing them onto the spine. Not touched. If the meta-phase ever wants the
  deflate theme on-spine, that is a demand-gated trigger, not a grounding pass.
- **The LEAD's "rescues ~10 nodes" estimate is over by ~6.** The dominant cause for 6 of 10 themes was
  not the operator→theme edge convention but the host L2 op being itself unreachable. This cycle delivers
  the clean +5 (4 themes + `L2/krylov-step`) and the structured finding; the residual is the next-tranche
  pass above.
- **No `book/src/L_n/index.md` running-count touched.** Pure edge-typing — no chapter landing, no
  consolidated-tally collision, no `SUMMARY.md` change. Single-dispatch, disjoint 5-file write-set.

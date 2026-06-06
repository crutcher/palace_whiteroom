---
agent: cycle-planner
invoked_at: 2026-06-06T014500Z
scope: cycle-111 dispatch plan (batch-35 BATCH-CLOSING; cycles 109/110/111; batch-35 meta-phase fires AFTER this finalize)
status: pending
---

# Cycle 111 dispatch plan

## Goals selected this cycle

BATCH-CLOSING cycle of meta-batch-35 — discharge the cleanly-groundable carried follow-ups
faithfully, leave the batch-35 meta-phase a clean picture. Two bounded, frontmatter-only,
land-clean graded-stack edge-typing tranches:

- **D1 (THE LEAD) — the orthogonalize lazy-tail chain grounding.** The c110 D1 §(g)
  GROUND-don't-remove fix already made `L2/orthogonalize` root-reachable (via the
  `L4/krylov-step →composes→ L2/orthogonalize` edge). The remaining gap is that
  `L2/orthogonalize` carries **NO frontmatter** (no typed `edges:` block), so its already-firm
  L2>L1 lowering theme `orthogonalize-composition-lowering` (firm content since c022) and its
  firm L1 leaf `L1/orthogonalize` / L1>L0 home `orthogonalize-mutation-rotation` (both firm
  content) are still GC-garbage. Typing `L2/orthogonalize` + `L1/orthogonalize` from-scratch
  (the c109 `L2/krylov-step` / c110 `L1/axpy` templates) flips **+3 reachable**.
- **D2 — the axpy-family L1>L0 theme scheme-completion.** `L1-L0/axpby-mutation-rotation` +
  `L1-L0/axpbypcz-mutation-rotation` carry **NO frontmatter at all** (the linter infers
  `rank=firm` from their `## Status` line and reads them as already-reachable via their firm
  L1 parents' legacy edges, so this is **NOT a reachability flip — it is scheme hygiene**:
  give them explicit typed `edges:` blocks like every other landed lowering theme, matching
  the c110 `L1/axpy` typed scheme). Bounded, mechanical, zero reachability movement.

**Faithful-path-or-finding:** the c110 finding's third candidate (`L3/orthogonalize` /
`L3-L2/orthogonalize-variant-split`) does **NOT** cleanly flip — there is no faithful reachable
depender (the L4 krylov-step deliberately `composes` `L2/orthogonalize` DIRECTLY because no L4
orthogonalize op exists; forcing an `L4/krylov-step → L3/orthogonalize` edge would be UNFAITHFUL,
contradicting the documented L4→L2 lowering chain). The normalize chain
(`L2/nrm2`/`L2/normalize`/`L3/normalize`/`L2/scal`/`L3/scal`/`L2/reciprocal`/`L3/reciprocal`)
likewise has no reachable depender (no feature root reaches the internal `normalize`/`reciprocal`
utilities). BOTH routed as structured findings for the batch-35 meta-phase, NOT forced this cycle.
NB: `L3/nrm2` is **already reachable** (grounded by c110's `L4/krylov-step →composes→ L4/nrm2`
edge); the prompt's "type L3/nrm2" hypothesis is already satisfied — no nrm2 mid-node work needed.

## Linter baseline (REQUIRED pre-dispatch — live, on `eaca075`)

`python3 tools/graded-stack-lint/graded_stack_lint.py --show-inbound`:

```
reachable from roots: 119
RANK VIOLATIONS: none.   (rank_violations = 0)
untyped (WARNING): 60
DETRITUS (140) — typed DAG nodes unreachable from any feature root.
STRONGER GARBAGE SIGNAL (26) — declares typed deps, still unreachable.
RESULT: 0 rank violation(s), 140 detritus node(s), 60 untyped (warning).
```

Confirms the prompt's expected baseline EXACTLY: reachable=119, rank_violations=0,
STRONGER GARBAGE=26, untyped=60.

**The 26 STRONGER-GARBAGE nodes** (declare typed deps, still unreachable):
`L1-L0/set-subvector-zero-mutation-rotation`, `L1/normalize`, `L1/weak_form_term`,
`L2/{axpby,axpbypcz,axpy,elementwise_product,jacobi-smoother,normalize,nrm2,reciprocal,scal}`,
`L3/{assemble-diagonal,axpby,axpbypcz,axpy,chebyshev,elementwise_product,fold_solve,jacobi-smoother,krylov-step,normalize,orthogonalize,reciprocal,scal}`,
`L4/preconditioning-framework`.
(The remaining detritus are `[garbage?]` edge-untypedness artifacts that collapse as P1 types edges.)

**Cluster reachability (programmatic, on the loaded graph — reconciles the inbound map):**
- `L2/orthogonalize` — **REACHABLE** (`L4/krylov-step →composes→ L2/orthogonalize`, c110 D1), `dep=[]` (no typed block).
- `L3/nrm2` — **REACHABLE** (`L4/krylov-step →composes→ L4/nrm2 →depends-on→ L3/nrm2`, c110 D1).
- `L1/orthogonalize` — GARBAGE, `dep=[]`, rank=firm (inferred), no frontmatter.
- `L1-L0/orthogonalize-mutation-rotation` — GARBAGE (exists on disk; the OQ saying "un-authored" is STALE), `dep=[]`.
- `L2-L1/orthogonalize-composition-lowering` — GARBAGE, `dep=[]` (firm content since c022; only the edge is missing).
- `L3/orthogonalize` — GARBAGE, `dep=[L2/orthogonalize ×2]`; **no reachable depender exists** → finding.
- `L3-L2/orthogonalize-variant-split` — GARBAGE, `dep=[]`; flips only if `L3/orthogonalize` is reachable → finding.
- `L1-L0/{axpby,axpbypcz}-mutation-rotation` — **REACHABLE already** (firm L1 parents depend-on them via legacy edges); `untyped=False` (inferred rank); `dep=[]` (no typed block).

## Per-node typing table

| Node | On-disk frontmatter | Typed `edges:` to ADD (faithful) | Flips reachable? | Owner |
|---|---|---|---|---|
| `L2/orthogonalize` | NONE (`# orthogonalize` H1) | `rank: firm`; `depends-on: L1/orthogonalize`, `L1/dot`, `L1/axpy`, `{target: L2-L1/orthogonalize-composition-lowering, kind: lowers-to}`; `reference: L1/orthogonalize` (sibling), `concepts/*` as in body | **YES** — grounds `L2-L1/orthogonalize-composition-lowering` (+1) AND `L1/orthogonalize` (+1) | D1 |
| `L1/orthogonalize` | NONE (`# orthogonalize` H1) | `rank: firm`; `depends-on:` `cites-evidence` L0 (`orthog.hpp:41-53` MGS, `:57-74` CGS, `:75-88` CGS2-refine, `iterative.cpp:307-325` dispatch), `{target: L1-L0/orthogonalize-mutation-rotation, kind: lowers-to}` | **YES** — grounds `L1-L0/orthogonalize-mutation-rotation` (+1) | D1 |
| `L1-L0/axpby-mutation-rotation` | NONE (`# axpby-mutation-rotation` H1) | `rank: firm`; `depends-on:` `cites-evidence` L0 (`vector.cpp:710` real α≠1, `:715-723` complex, `vector.hpp:116-117` decls, `:739-743`/`:745-758` axpby bodies); `reference: L1/axpy`, `L1/axpby`, `L1-L0/dot-mutation-rotation` | NO (already reachable) — scheme hygiene | D2 |
| `L1-L0/axpbypcz-mutation-rotation` | NONE (`# axpbypcz-mutation-rotation` H1) | `rank: firm`; `depends-on:` `cites-evidence` L0 (`vector.cpp:745-758` real body, `:749-751` γ=0 fast-path, `:755-756` γ≠0 slow-path, `vector.hpp:313-316` decl); `reference: L1/axpbypcz` | NO (already reachable) — scheme hygiene | D2 |
| `L3/orthogonalize` | legacy (`layer:`/`firmness:`/`lifts_from:`/`lowers_to:`, NO `edges:`) | — (no faithful reachable depender) | **NO — ROUTE AS FINDING** | D1 finding |
| `L3-L2/orthogonalize-variant-split` | NONE | — (gated on `L3/orthogonalize` reachability) | **NO — ROUTE AS FINDING** | D1 finding |

**Predicted linter delta:** reachable **119 → 122** (+3, all from D1: the three firm-content
orthogonalize-chain nodes), rank_violations **HELD 0** (all new edges firm→firm or firm→L0-evidence;
`L1/orthogonalize` Status=firm inferred-rank), untyped HELD 60 (D2's two themes already non-untyped
via inferred rank; D1's two nodes already non-untyped via Status line — the win is Axis-2 reachability,
not Axis-1 untyped), STRONGER GARBAGE 26 → 23 (the three orthogonalize-chain nodes flip out).

## Deliverable-presence verification (paste-inline-evidence)

`ls` + `## Status` + OQ-RESOLVED-grep + structural-gate, per dispatch:

**D1 targets:**
- `[EXISTS] book/src/L2/orthogonalize.md (421 lines)` — `## Status` (:324) = ``firm`` (read on disk). Deliverable = ADD typed `edges:` (no on-disk block) — NOT a no-op.
- `[EXISTS] book/src/L1/orthogonalize.md (336 lines)` — `## Status` (:219) = ``firm``. Deliverable = ADD typed `edges:` (no on-disk block) — NOT a no-op.
- `[EXISTS] book/src/L2-L1/orthogonalize-composition-lowering.md (485 lines)` — firm content (c022); flip-target, no body edit.
- `[EXISTS] book/src/L1-L0/orthogonalize-mutation-rotation.md` — firm content (OQ "un-authored" is STALE; file on disk); flip-target, no body edit.
- OQ-RESOLVED grep: `orthogonalize-composition-lowering-l2-l1-theme` RESOLVED c022/c023/c025 (the theme is content-firm — this cycle is EDGE-TYPING for reachability, NOT re-authoring; open by construction for the graded-stack axis). `orthogonalize-l2-composition-family-oq-block-stale-landed-work` CLOSED (confirms content firm). No RESOLVED line bars the edge-typing deliverable.
- Structural gate: none blocking — graded-stack §(g) GROUND-don't-remove is the live disposition; faithful firm→firm edges. STOP-PROPOSING: `orthogonalize` is NOT on the disqualified list (`lu_solve`/`back_solve`/`ls-update-column`/`nleps_*`); not a `promotion_frontier` member.

**D2 targets:**
- `[EXISTS] book/src/L1-L0/axpby-mutation-rotation.md (238 lines)` — `## Status` (:226) present. Deliverable = ADD typed `edges:` (NO frontmatter on disk) — NOT a no-op.
- `[EXISTS] book/src/L1-L0/axpbypcz-mutation-rotation.md (414 lines)` — `## Status` (:303) present. Deliverable = ADD typed `edges:` (NO frontmatter on disk) — NOT a no-op.
- OQ: `l1-l0-axpy-family-themes-need-scheme-frontmatter` (c110 D2) OPEN — this dispatch discharges it. No RESOLVED line.
- Structural gate: none. STOP-PROPOSING clear (BLAS-1 themes, not disqualified slugs).

All checks PASS. No STOP-PROPOSING violation. Framing: pure graded-stack edge-typing
(layer-intro-author primary owner of frontmatter scheme), NOT reflexive-harvest.

## Dispatches

1. **agent**: `layer-intro-author`
   **scope**: Graded-stack edge-typing — the orthogonalize lazy-tail chain grounding (FRONTMATTER-ONLY, faithful-path-or-finding). Author from-scratch typed `edges:` frontmatter blocks on (a) `book/src/L2/orthogonalize.md` and (b) `book/src/L1/orthogonalize.md`, using the c109 `book/src/L2/krylov-step.md` (from-scratch L2) and c110 `book/src/L1/axpy.md` (from-scratch L1 leaf) templates. **(a) `L2/orthogonalize`**: `rank: firm`; `edges.depends-on`: `L1/orthogonalize`, `L1/dot`, `L1/axpy` (the firm L1 leaf it lifts + the two firm constituent primitives the `project ▷ subtract` composition genuinely calls — body §:67-131), plus `{target: L2-L1/orthogonalize-composition-lowering, kind: lowers-to}` (the firm L2>L1 lowering theme this composition lowers through — mirrors `L2/krylov-step → L2-L1/krylov-step-kernel-defusion`); `edges.reference`: the `concepts/*` the body cites (do NOT re-derive — copy from body prose). **(b) `L1/orthogonalize`**: `rank: firm`; `edges.depends-on`: `cites-evidence` L0 ranges (`palace/linalg/orthog.hpp:41-53` MGS, `:57-74` CGS, `:75-88` CGS2-refine block, `palace/linalg/iterative.cpp:307-325` dispatch wrapper) + `{target: L1-L0/orthogonalize-mutation-rotation, kind: lowers-to}` (the firm L1>L0 mutation-rotation home). VERIFY all L0 anchor lines on-disk (codemap hints; END lines drift-prone) before citing. **DO NOT edit chapter bodies** (content firm since c019/c022) — frontmatter prepend only. **ROUTE AS FINDING (do NOT force):** `L3/orthogonalize` + `L3-L2/orthogonalize-variant-split` cannot be cleanly flipped — no faithful reachable depender exists (L4 krylov-step `composes` `L2/orthogonalize` DIRECTLY; no L4 orthogonalize op; an `L4→L3/orthogonalize` edge would be UNFAITHFUL). State this as a structured finding (a candidate for the batch-35 meta-phase: is the L3 orthogonalize sub-chain genuine detritus, or does it need a faithful upper grounding the spine doesn't currently supply?). Predicted linter: reachable 119→122 (+3), rank_violations HELD 0.
   **deps**: none

2. **agent**: `layer-intro-author`
   **scope**: Graded-stack edge-typing — the axpy-family L1>L0 theme scheme-completion (FRONTMATTER-ONLY hygiene; discharges OQ `l1-l0-axpy-family-themes-need-scheme-frontmatter`). Author from-scratch typed `edges:` frontmatter blocks on `book/src/L1-L0/axpby-mutation-rotation.md` and `book/src/L1-L0/axpbypcz-mutation-rotation.md` (both currently carry NO frontmatter), matching the c110 `L1/axpy` typed scheme for an L1>L0 lowering-theme leaf: `rank: firm`; `edges.depends-on` = the rank-terminal POSITIVE L0 source via `cites-evidence` (axpby: `palace/linalg/vector.cpp:710` real α≠1, `:715-723` complex AXPY, `:739-743`/`:745-758` axpby bodies, `vector.hpp:116-117` decls; axpbypcz: `palace/linalg/vector.cpp:745-758` real-real body, `:749-751` γ=0 fast-path, `:755-756` γ≠0 slow-path, `vector.hpp:313-316` decl) — VERIFY each on-disk (codemap hints; END lines drift-prone); `edges.reference` = the firm L1 parents (`L1/axpy`+`L1/axpby` for axpby; `L1/axpbypcz` for axpbypcz) + `L1-L0/dot-mutation-rotation` where the body cites it. **This is scheme hygiene, NOT a reachability flip** — both themes are ALREADY reachable (firm L1 parents depend-on them via legacy edges); the win is making the typed-edge graph explicit + scheme-consistent (replacing the inferred-rank/legacy-edge implicit form with the standard typed block). DO NOT edit bodies. Predicted linter: reachable HELD (already reachable), untyped HELD 60, rank_violations HELD 0.
   **deps**: none

## Overlap analysis

- **D1 vs D2**: write-sets are **DISJOINT**. D1 writes `book/src/L2/orthogonalize.md` +
  `book/src/L1/orthogonalize.md` (frontmatter only). D2 writes
  `book/src/L1-L0/axpby-mutation-rotation.md` + `book/src/L1-L0/axpbypcz-mutation-rotation.md`
  (frontmatter only). No shared file. No shared operator-name modification. No consolidated-tally
  collision (per-page frontmatter, not a layer-index cohort count — neither touches any `index.md`).
  No new-slug forward-reference (every `lowers-to`/`depends-on`/`reference`/`cites-evidence` target
  is an EXISTING stable slug or an L0 source range on disk — `L2-L1/orthogonalize-composition-lowering`,
  `L1-L0/orthogonalize-mutation-rotation`, `L1/{orthogonalize,dot,axpy,axpby,axpbypcz}` all verified
  present). → **NON-OVERLAPPING → PARALLEL.**

No other pairs (2 dispatches only).

## Sequencing schedule

**Single wave — D1, D2 parallel.** Disjoint write-sets, no forward-reference dependency, no
shared index/tally. Both are bounded frontmatter-only edits. The per-report integrators apply
serially (artifact writes naturally serialize); `integrator-finalize` runs ONCE at cycle end
(rebuild + commit + push + the step-5b linter re-run verifying reachable 119→122, rank_violations
HELD 0). No multi-wave needed.

## Open questions / caveats

- **D1 routed finding — the L3-orthogonalize sub-chain (`L3/orthogonalize` +
  `L3-L2/orthogonalize-variant-split`) stays detritus.** No faithful reachable depender exists
  (the L4 krylov-step deliberately composes `L2/orthogonalize` directly, no L4 orthogonalize op).
  This is a genuine spine finding for the **batch-35 meta-phase**: either (i) the L3 orthogonalize
  iteration-view (the MGS `partial-obstruction` + CGS/CGS2 lifts) is genuine detritus relative to
  the current feature-root set and should be a tracked baseline-exception, OR (ii) it is a future
  dependency the spine will reach once a driver column composes the L3 (rather than L2)
  orthogonalize surface — in which case it is a GROUND candidate, but NOT via a forced edge this
  cycle. The §(g) priority order (ground → route-as-detritus → baseline-exception) makes this a
  meta-phase judgment, not a primary-cycle force. (Same shape as the c109 Group-B finding +
  the c110 lazy-tail finding — the carried lazy-tail tail is now down to this one sub-chain +
  the normalize/reciprocal chain.)

- **The normalize/reciprocal internal-utility chain** (`L2/nrm2`, `L2/normalize`, `L3/normalize`,
  `L2/scal`, `L3/scal`, `L2/reciprocal`, `L3/reciprocal`, `L1/normalize`) — 8 of the 26
  STRONGER-GARBAGE nodes — has **no reachable depender** (no feature root reaches the internal
  Arnoldi/eigenvalue `normalize`/`reciprocal` utilities; the L4 spine reaches `L4/nrm2`/`L4/dot`
  via krylov-step but not the `normalize` fusion or `reciprocal`). NOT cleanly groundable as
  batch-close work. Flagged for the batch-35 meta-phase's §(g) ground-vs-baseline-exception call:
  is `normalize` an absorbed-below-column constituent (like the c107 BC/divfree pattern) that
  should ground from a column, or a tracked baseline-exception? (Same disposition question as the
  c110 chebyshev/jacobi preconditioner-leg recommendation — bundle the call.)

- **Carry to the batch-35 meta-phase (NOT a forward dispatch):** (i) the c110 D1
  chebyshev/jacobi preconditioner-leg absorbed-below-column baseline-exception RATIFICATION;
  (ii) the `gram` / `incremental-least-squares` routings (c110 D1) — both demand-gated /
  STOP-PROPOSING-adjacent, correctly NOT picked this cycle; (iii) the c110-flagged friction
  candidate `parallel-dispatch-reachability-measurement-contamination` (when ≥2 parallel
  dispatches each move reachability, the per-report integrator must re-measure on the LANDED
  tree, not sum isolated deltas — relevant if the meta-phase wants to codify the
  measure-on-landed-tree convention). **This cycle has only D1 moving reachability (+3); D2 is
  reachability-neutral** — so the measurement-contamination risk is LOW this cycle (single mover),
  but the finalize should still re-measure on the landed tree per the standing convention.

- **Deliberately NO third dispatch.** The remaining STRONGER-GARBAGE / detritus is either
  routed-as-finding (the two chains above) or `promotion_frontier`/demand-gated (STOP-PROPOSING).
  Batch-closing discipline: discharge the cleanly-groundable carried follow-ups (the orthogonalize
  chain + axpy-family scheme), leave the big standing calls (normalize/reciprocal grounding,
  L3-orthogonalize disposition, preconditioner baseline-exceptions) to the batch-35 meta-phase.
  Two bounded, faithful, land-clean dispatches — the right shape for a batch-closing cycle.

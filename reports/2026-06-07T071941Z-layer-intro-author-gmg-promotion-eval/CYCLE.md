---
agent: layer-intro-author
invoked_at: 2026-06-07T071941Z
scope: GMG preconditioner column rough-in→firm promotion-eval (cycle-122 D7)
status: pending
integrated_at: 2026-06-07T071941Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-122 D7. Applied clean. GMG preconditioner column promoted rough-in→FIRM at L4+L1 (feature_root: seed KEPT) + faithful depends-on(composes)→reference re-type of L3/chebyshev + L2/jacobi-smoother iteration-views; RE1 re-stated. 0 gate hits. See reports/cycle-122-integrator-staging/STAGING.md."
---

# CYCLE: geometric-multigrid-preconditioner column rough-in → firm

## Summary

**Verdict: PROMOTE `rank: rough-in` → `firm`** on both `book/src/feature/geometric-multigrid-preconditioner.{L4,L1}.md`, via a **faithful edge re-classification** of the L4 file (the §2g GROUND-faithfully discipline, NOT a forced flip).

The c121 column was held at rough-in by ONE stated gate — its "smoother leg rests on `L3/chebyshev` (partial-obstruction) + the forward-referenced `multigrid-relaxation-smoother` (not yet firm on disk)." Reading the on-disk `## Status` lines this cycle, **both halves of that gate have cleared / were mis-stated**:

- **`L1/multigrid-relaxation-smoother`** is **`firm`** on disk (`firmness: firm`, `rank: firm`, `## Status: \`firm\` — kernel-impl`). It landed firm in c121 (D3). The column prose still calls it "forward-referenced this cycle and not yet firm on disk" — that is **stale**.
- **`L3/chebyshev`** (partial-obstruction) is **NOT a faithful blocking `depends-on`** of the column. It is the L3 **iteration-view** of the same smoother. The faithful blocking constituent is the firm `multigrid-relaxation-smoother`, which itself depends-on **`L1/chebyshev-smoother`** (firm) — NOT `L3/chebyshev` — and documents the `pc_it` Richardson sweep as a **sequential-obstruction that does NOT gate its L1 firm status** (`multigrid-relaxation-smoother.md`: "the outer `pc_it` relaxation-sweep sequential-obstruction … does NOT gate the L1 firm status; at L1 the sweep is a pure `pc_it`-fold parameter"). The L4 file mis-types `L3/chebyshev` and `L2/jacobi-smoother` as blocking `depends-on (composes)`; the **L1 file already correctly types them as `reference`** (sibling iteration-views). The faithful fix is to bring the L4 edges into agreement with the L1 file.

After re-classification, **all blocking `depends-on` constituents are firm** (`fe_space_hierarchy` firm, `multigrid-relaxation-smoother` firm, `reciprocal` firm, `normalize` firm, `preconditioning-framework` firm at L4) → the well-foundedness invariant `rank(u) ≤ min(deps)` permits `firm`. The compositional claim is exhaustively cited (`gmg.cpp:126-205`, verified this cycle), and the column's residual sequential-obstructions (level recursion + `pc_it` Richardson sweep) are the SAME documented sequential-obstructions the firm smoother already absorbs without gating firm — the firm-on-positive-structure + documented-sequential-obstruction discipline that promoted the smoother applies identically to the *compositional* claim here.

`feature_root: seed` is KEPT on both levels (GC-root marker, a separate axis from the resolution ladder).

## On-disk constituent survey (read from `## Status` lines, NOT index cells)

| Constituent | edge class (faithful) | on-disk `## Status` | rank |
|---|---|---|---|
| `L1/fe_space_hierarchy` | `depends-on (composes)` | `firm (firm-on-positive-structure)` | firm |
| `L1/multigrid-relaxation-smoother` | `depends-on (composes)` | `` `firm` — kernel-impl `` | firm |
| `L1/reciprocal` | `depends-on (composes)` | `` `firm` `` | firm |
| `L1/normalize` | `depends-on (composes)` | `` `firm` `` | firm |
| `L4/preconditioning-framework` | `depends-on (composes)` (L4 only) | `` `firm` `` | firm |
| `L3/chebyshev` | **`reference`** (sibling L3 iteration-view) | `` `partial-obstruction` `` | rankless (no `obstruction_resolution`) |
| `L2/jacobi-smoother` | **`reference`** (sibling L2 iteration-view) | `` `firm` `` | firm |
| `L1/chebyshev-smoother` (the smoother's actual dep) | (transitive, via smoother) | `` `firm` `` | firm |

The smoother's own `depends-on` block (read on disk): `L1/chebyshev-smoother`, `L1/apply_linop`, `L1/axpby`, `L1/interpolator` — all firm; `L3/chebyshev` appears only in its *prose* as the parallel L3-lift partial-obstruction finding, NOT as an edge. This confirms `L3/chebyshev` is a sibling iteration-view of the smoother, not a constituent the column depends on.

## Why re-classify rather than leave chebyshev as `depends-on`

Leaving `L3/chebyshev` as a blocking `depends-on (composes)` while flipping the column to firm would be a `firm`-resting-on-rankless-partial-obstruction edge. The linter currently only *warns-not-fails* on it (`rank_check` line 614-615: a rankless dep is skipped — `L3/chebyshev` is `partial-obstruction` with no `obstruction_resolution`, so `derive_rank` returns rank `None`), so the linter would stay EXIT-0 either way — but a firm claim resting on a partial-obstruction iteration-view is an **unfaithful** firm. The §2g forbidden move is exactly "`op →depends-on→ L3-op` when the real relationship is a *lowering*/sibling-view, not a *constituent-use*." The faithful disposition is: the column composes the **smoother** (firm); chebyshev/jacobi are the L2/L3 iteration-views of that smoother → `reference`. This is the L1 file's existing (correct) classification.

## Proposed changes

### 1 — L4 file: re-type the chebyshev / jacobi edges (depends-on → reference) + flip rank

```edit:book/src/feature/geometric-multigrid-preconditioner.L4.md
[old]: feature_root: seed
rank: rough-in
edges:
  depends-on:
    - target: L4/preconditioning-framework
      kind: composes                  # the bind-once preconditioner cap GMG plugs into (firm c096)
    - target: L1/fe_space_hierarchy
      kind: composes                  # GetProlongationOperators() — the level-stack P[l] prolongation GMG restricts/prolongs over (GROUNDS RE9)
    - target: L1/multigrid-relaxation-smoother
      kind: composes                  # D3 kernel-impl: the distributive/Hiptmair relaxation smoother (forward-ref, lands same cycle)
    - target: L3/chebyshev
      kind: composes                  # the per-level Chebyshev polynomial smoother leg (partial-obstruction; GROUNDS RE1)
    - target: L2/jacobi-smoother
      kind: composes                  # the Jacobi (point) smoother leg / diagonal-preconditioner gate (firm)
    - target: L1/reciprocal
      kind: composes                  # dinv.Reciprocal() — diagonal-preconditioner extract (GROUNDS RE7)
    - target: L1/normalize
      kind: composes                  # the normalize/reciprocal scaling chain in the smoother diagonal-precond apply (GROUNDS RE5)
    - target: palace/linalg/gmg.cpp:126-205
      kind: cites-evidence            # GeometricMultigridSolver::Mult + VCycle (the V-cycle recursion body)
    - target: palace/linalg/ksp.cpp:206-234
      kind: cites-evidence            # GMG construction with the prolongation operators + smoother config
  reference:
    - feature/lifecycle.L4
    - feature/eigenmode.L4
[new]: feature_root: seed
rank: firm
edges:
  depends-on:
    - target: L4/preconditioning-framework
      kind: composes                  # the bind-once preconditioner cap GMG plugs into (firm c096)
    - target: L1/fe_space_hierarchy
      kind: composes                  # GetProlongationOperators() — the level-stack P[l] prolongation GMG restricts/prolongs over (GROUNDS RE9)
    - target: L1/multigrid-relaxation-smoother
      kind: composes                  # D3 kernel-impl (firm c121): the distributive/Hiptmair relaxation smoother — the faithful blocking smoother constituent
    - target: L1/reciprocal
      kind: composes                  # dinv.Reciprocal() — diagonal-preconditioner extract (GROUNDS RE7)
    - target: L1/normalize
      kind: composes                  # the normalize/reciprocal scaling chain in the smoother diagonal-precond apply (GROUNDS RE5)
    - target: palace/linalg/gmg.cpp:126-205
      kind: cites-evidence            # GeometricMultigridSolver::Mult + VCycle (the V-cycle recursion body)
    - target: palace/linalg/ksp.cpp:206-234
      kind: cites-evidence            # GMG construction with the prolongation operators + smoother config
  reference:
    - feature/lifecycle.L4
    - feature/eigenmode.L4
    - L3/chebyshev                     # the L3 ITERATION-VIEW of the smoother leg (partial-obstruction; sibling-view, NOT a blocking constituent — GROUNDS RE1 reachability)
    - L2/jacobi-smoother               # the L2 iteration-view / point-smoother leg (firm; sibling-view)
```

### 2 — L4 file: rewrite the "Why this is rough-in" section → "Why this is firm"

```edit:book/src/feature/geometric-multigrid-preconditioner.L4.md
[old]: ## Why this is rough-in (not firm)

Under the OWN-COMPOSITION promotion rule (a column promotes off its current rung when its
OWN composition + directly-owned constituents are at-rank; cross-linked sibling columns are
references, NOT blockers) **and** the well-foundedness invariant `rank(u) ≤ min(deps)`, this
column is **rough-in**, not firm:

- Its directly-owned **smoother leg** rests on [`L3/chebyshev`](../L3/chebyshev.md), which
  is **partial-obstruction** (`chebyshev.md` `## Status`: the per-step body lifts cleanly
  to a whole-tensor expression, but the inner `k`-recurrence and the outer `pc_it`
  Richardson sweep are *witnessed sequential obstructions* — the V-cycle inherits this
  un-liftable iteration in the same way).
- Its [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md) constituent
  is D3's kernel-impl, **forward-referenced this cycle and not yet firm on disk**; the
  well-foundedness invariant caps this column at no more resolved than that constituent.

So `rank(geometric-multigrid-preconditioner) ≤ min(rank(chebyshev), rank(relaxation-smoother))`
holds only at rough-in. The other directly-owned constituents ARE firm
([`preconditioning-framework`](../L4/preconditioning-framework.md),
[`fe_space_hierarchy`](../L1/fe_space_hierarchy.md),
[`jacobi-smoother`](../L2/jacobi-smoother.md), [`reciprocal`](../L1/reciprocal.md),
[`normalize`](../L1/normalize.md)); the column is held at rough-in only by the smoother leg.
**Promotion condition:** the smoother leg firms (D3's `multigrid-relaxation-smoother`
promotes to firm AND the chebyshev partial-obstruction's V-cycle recursion is either lifted
or accepted as a documented sequential-obstruction at the column level) — a c122+ re-check.

This is the clean-gate landing (the redirect's verify-present discipline): the substrate is
cleanly composable BY NAME, but its smoother leg is not yet firm, so the column lands
rough-in rather than forcing a firm claim.
[new]: ## Why this is firm (c122 re-check)

Under the OWN-COMPOSITION promotion rule (a column promotes off its current rung when its
OWN composition + directly-owned constituents are at-rank; cross-linked sibling columns are
references, NOT blockers) **and** the well-foundedness invariant `rank(u) ≤ min(deps)`, this
column is now **firm**. The c121 rough-in landing was gated on one item — "the smoother leg
firms" — and the c122 re-check finds that gate cleared, with one edge re-classification:

- **The faithful blocking smoother constituent is
  [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md), which is now
  `firm` on disk** (kernel-impl, c121 D3; `## Status: \`firm\``). The c121 prose called it
  "forward-referenced, not yet firm" — that was true at authoring time and is now stale.
- **[`L3/chebyshev`](../L3/chebyshev.md) (partial-obstruction) is NOT a blocking
  `depends-on` of this column — it is the L3 *iteration-view* of the smoother**, re-typed to
  `reference` (sibling-view) this cycle. The firm `multigrid-relaxation-smoother` depends on
  the firm [`L1/chebyshev-smoother`](../L1/chebyshev-smoother.md) (the per-level point
  smoother `B`/`B_G`), NOT on `L3/chebyshev`; and it documents the `pc_it` Richardson sweep
  as a **sequential-obstruction that does not gate its L1 firm status** (the sweep is a pure
  `pc_it`-fold parameter at L1). The column inherits exactly that disposition: its V-cycle
  level recursion + `pc_it` Richardson sweep are documented sequential-obstructions, and they
  do not gate the *compositional* firm claim — the same firm-on-positive-structure +
  documented-sequential-obstruction discipline that promoted the smoother itself. (Forcing a
  `column →depends-on→ L3-iteration-view` edge would be the §2g over-edge — the real
  relationship is a sibling-view, so it is a `reference`.)

So every directly-owned **blocking** constituent is firm
([`preconditioning-framework`](../L4/preconditioning-framework.md),
[`fe_space_hierarchy`](../L1/fe_space_hierarchy.md),
[`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md),
[`reciprocal`](../L1/reciprocal.md), [`normalize`](../L1/normalize.md)), and
`rank(geometric-multigrid-preconditioner) = firm ≤ min(deps) = firm` holds. The
chebyshev/jacobi iteration-views remain `reference` cross-links (the drift-guard sibling
pointers; they still GROUND RE1's reachability via this live column).

This is the clean-gate landing matured: the substrate is cleanly composable BY NAME, the
compositional V-cycle algebra is exhaustively cited (`gmg.cpp:126-205`), and all blocking
constituents firmed — so the column promotes to firm without a forced claim.
```

### 3 — L4 file: reconcile the `## Status` section

```edit:book/src/feature/geometric-multigrid-preconditioner.L4.md
[old]: `rough-in` — the first **infrastructure / shared-substrate** feature-surface
composition-root (DIRECTIVE-2 grounded consumer-(1), batch-39 LEAD). The GC-root marker
`feature_root: seed` is preserved (root-role is permanent/categorical, a separate axis from
the resolution ladder). Held at rough-in by the well-foundedness invariant: its smoother leg
rests on [`L3/chebyshev`](../L3/chebyshev.md) (partial-obstruction) + D3's
forward-referenced [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md)
(not yet firm on disk). All other directly-owned constituents are firm. **Promotion
condition:** the smoother leg firms (c122+ re-check). This chapter carries the
*compositional* claim (the GMG preconditioner = this V-cycle composition of these constituent
pieces, GROUNDING RE9/RE1/RE5/RE7 by name), not the constituents' per-op algebraic claims
(those live in the linked chapters). Evidence: `gmg.cpp:126-205` (Mult + VCycle) +
`ksp.cpp:206-234` (construction with the prolongation operators + smoother config) realizing
the composition, plus the firm constituent down-links.
[new]: `firm` (promoted rough-in→firm cycle-122, the D7 promotion-eval re-check) — the first
**infrastructure / shared-substrate** feature-surface composition-root (DIRECTIVE-2 grounded
consumer-(1), batch-39 LEAD). The GC-root marker `feature_root: seed` is preserved (root-role
is permanent/categorical, a separate axis from the resolution ladder). **Why firm:** every
directly-owned **blocking** constituent is firm on disk — `preconditioning-framework` (c096),
`fe_space_hierarchy` (c117), `multigrid-relaxation-smoother` (c121 kernel-impl), `reciprocal`,
`normalize`; the well-foundedness invariant `rank(u) ≤ min(deps) = firm` holds. The
[`L3/chebyshev`](../L3/chebyshev.md) (partial-obstruction) and
[`L2/jacobi-smoother`](../L2/jacobi-smoother.md) constituents are the L2/L3 **iteration-views**
of the smoother, re-typed to `reference` (sibling-view) this cycle — the faithful blocking
smoother dep is the firm `multigrid-relaxation-smoother` (which rests on the firm
[`L1/chebyshev-smoother`](../L1/chebyshev-smoother.md), not `L3/chebyshev`). The V-cycle level
recursion + `pc_it` Richardson sweep are documented sequential-obstructions inherited from the
firm smoother — they do not gate the *compositional* firm claim (firm-on-positive-structure +
documented-sequential-obstruction discipline). This chapter carries the *compositional* claim
(the GMG preconditioner = this V-cycle composition of these constituent pieces, GROUNDING
RE9/RE1/RE5/RE7 by name), not the constituents' per-op algebraic claims (those live in the
linked chapters). Evidence: `gmg.cpp:126-205` (Mult + VCycle) + `ksp.cpp:206-234`
(construction with the prolongation operators + smoother config) realizing the composition,
plus the firm constituent down-links.
```

### 4 — L4 file: fix the stale smoother-status cells in the constituent down-link table

```edit:book/src/feature/geometric-multigrid-preconditioner.L4.md
[old]: | per-level relaxation smoother | [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md) (D3 kernel-impl, forward-ref) | rough-in (D3) | `distrelaxation.cpp:13-36`; `gmg.cpp:42-60` |
| Chebyshev polynomial smoother leg (GROUNDS RE1) | [`L3/chebyshev`](../L3/chebyshev.md) | partial-obstruction | `chebyshev.cpp:160-220`; `gmg.cpp:50-60` |
| Jacobi (point) smoother / diagonal gate | [`L2/jacobi-smoother`](../L2/jacobi-smoother.md) | firm | `chebyshev.cpp:177` (`AssembleDiagonal`) |
[new]: | per-level relaxation smoother (blocking dep) | [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md) (kernel-impl, c121) | firm | `distrelaxation.cpp:13-36`; `gmg.cpp:42-60` |
| Chebyshev polynomial smoother leg — L3 iteration-VIEW (reference; GROUNDS RE1) | [`L3/chebyshev`](../L3/chebyshev.md) | partial-obstruction | `chebyshev.cpp:160-220`; `gmg.cpp:50-60` |
| Jacobi (point) smoother / diagonal gate — L2 iteration-view (reference) | [`L2/jacobi-smoother`](../L2/jacobi-smoother.md) | firm | `chebyshev.cpp:177` (`AssembleDiagonal`) |
```

### 5 — L1 file: flip rank (edges already correctly classified)

```edit:book/src/feature/geometric-multigrid-preconditioner.L1.md
[old]: feature_root: seed
rank: rough-in
edges:
[new]: feature_root: seed
rank: firm
edges:
```

### 6 — L1 file: reconcile the smoother-leg prose (stale forward-ref)

```edit:book/src/feature/geometric-multigrid-preconditioner.L1.md
[old]: 2. **Per-level smoother** — [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md)
   (D3 kernel-impl, forward-ref) / the Chebyshev/Jacobi polynomial smoothers
   ([`L3/chebyshev`](../L3/chebyshev.md) / [`L2/jacobi-smoother`](../L2/jacobi-smoother.md),
   cross-linked as references). The smoother's diagonal-preconditioner setup
[new]: 2. **Per-level smoother** — [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md)
   (kernel-impl, **firm** c121) / the Chebyshev/Jacobi polynomial smoothers
   ([`L3/chebyshev`](../L3/chebyshev.md) / [`L2/jacobi-smoother`](../L2/jacobi-smoother.md),
   cross-linked as references — the L2/L3 iteration-views of the smoother, not blocking deps).
   The smoother's diagonal-preconditioner setup
```

### 7 — L1 file: reconcile the `## Status` section

```edit:book/src/feature/geometric-multigrid-preconditioner.L1.md
[old]: `rough-in` — the L1 pure-function surface of the infrastructure / shared-substrate GMG
preconditioner column. `feature_root: seed` preserved. Held at rough-in by the same
well-foundedness gate as the [L4 surface](./geometric-multigrid-preconditioner.L4.md): the
smoother leg rests on the partial-obstruction [`L3/chebyshev`](../L3/chebyshev.md) + D3's
forward-referenced [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md).
The V-cycle body is the mutation-rotated pure rendering of `gmg.cpp:126-205`; the level
recursion + Richardson sweep are the documented sequential obstructions. Evidence:
`gmg.cpp:126-205`.
[new]: `firm` (promoted rough-in→firm cycle-122) — the L1 pure-function surface of the
infrastructure / shared-substrate GMG preconditioner column. `feature_root: seed` preserved.
Firm on the same well-foundedness basis as the
[L4 surface](./geometric-multigrid-preconditioner.L4.md): all blocking `depends-on`
constituents are firm on disk (`fe_space_hierarchy`, `multigrid-relaxation-smoother` (kernel-impl
c121), `reciprocal`, `normalize`). The [`L3/chebyshev`](../L3/chebyshev.md) (partial-obstruction)
+ [`L2/jacobi-smoother`](../L2/jacobi-smoother.md) cross-links are the L2/L3 iteration-VIEWS of
the smoother (`reference`-class, already so typed here) — sibling-views, not blocking deps. The
V-cycle body is the mutation-rotated pure rendering of `gmg.cpp:126-205`; the level recursion +
`pc_it` Richardson sweep are the documented sequential obstructions inherited from the firm
smoother and do not gate the compositional firm claim. Evidence: `gmg.cpp:126-205`.
```

### 8 — `feature/index.md`: flip the matrix cell rough-in → firm

```edit:book/src/feature/index.md
[old]: | [geometric-multigrid-preconditioner](./geometric-multigrid-preconditioner.L4.md) (rough-in) | [L4 root](./geometric-multigrid-preconditioner.L4.md) | [L1 root](./geometric-multigrid-preconditioner.L1.md) | — |
[new]: | [geometric-multigrid-preconditioner](./geometric-multigrid-preconditioner.L4.md) (firm) | [L4 root](./geometric-multigrid-preconditioner.L4.md) | [L1 root](./geometric-multigrid-preconditioner.L1.md) | — |
```

## Supporting evidence

- **On-disk `## Status` reads (this cycle, authoritative):** `L1/multigrid-relaxation-smoother` = `firm` (kernel-impl); `L1/chebyshev-smoother` = `firm`; `L2/jacobi-smoother` = `firm`; `L1/fe_space_hierarchy` = `firm (firm-on-positive-structure)`; `L1/reciprocal` = `firm`; `L1/normalize` = `firm`; `L4/preconditioning-framework` = `firm`; `L3/chebyshev` = `partial-obstruction` (frontmatter `firmness: partial-obstruction`, NO `obstruction_resolution` → linter-rank None/rankless).
- **Smoother's actual `depends-on` block (on disk):** `L1/chebyshev-smoother`, `L1/apply_linop`, `L1/axpby`, `L1/interpolator` — all firm. `L3/chebyshev` appears only in the smoother's PROSE as the parallel L3-lift partial-obstruction finding, NOT as an edge → confirms it is a sibling iteration-view, not a constituent.
- **Smoother sequential-obstruction disposition (on disk):** "The outer `pc_it` relaxation-sweep sequential-obstruction (non-law NL1) … does NOT gate the L1 firm status (at L1 the sweep is a pure `pc_it`-fold parameter)." The column inherits exactly this.
- **V-cycle citation verified via codemap `read_range` this cycle:** `gmg.cpp:126-142` = `GeometricMultigridSolver::Mult` (the `pc_it` Richardson outer loop, `X.back()=x` … `for(it<pc_it) VCycle(n_levels-1, it>0)` … `y=Y.back()`); `gmg.cpp:172-205` = `VCycle` (presmooth `Mult2` → residual `A->Mult`+`AXPBY(1,-1)` → restrict `RealMultTranspose(*P[l-1])` → recurse `VCycle(l-1)` → prolong-add `RealMult(*P[l-1])`+`Y[l]+=R[l]` → postsmooth `MultTranspose2`). The column body rendering matches the source exactly.
- **Linter mechanics:** `tools/graded-stack-lint/graded_stack_lint.py` `rank_check` skips rankless deps (warn-not-fail, line 614-615), so the firm-on-rankless-chebyshev edge would NOT have failed the linter — but it would be an UNFAITHFUL firm. The re-classification makes the firm claim well-founded in fact, not merely linter-EXIT-0. The faithful classification matches the L1 file's existing `reference`-class typing of chebyshev/jacobi.
- **Discipline applied:** §2g GROUND-faithfully priority order — the would-be over-edge `column →depends-on→ L3-iteration-view` is declined; the faithful relationship is `column →composes→ smoother (firm)` + `column →reference→ chebyshev/jacobi (L2/L3 iteration-views)`. This is faithful-edge-or-finding, and here the faithful edges support firm.

## Open questions / caveats

- **`record-FiniteElementSpaceHierarchy-promote-watch` wording (the OQ named in my dispatch):** the watch's literal trigger was "a 2nd **FIRM** consumer (the GMG preconditioner) lands." The `concepts/FiniteElementSpaceHierarchy.md` page was **already promoted in c121 D2** under the live "≥2 consumers, NOT ≥2 *firm* consumers" rule (the concepts page is on disk, `rank: firm`), and the c121 OQ `record-FiniteElementSpaceHierarchy-promote-watch-wording-reconcile` already scheduled the meta-phase to mark the old watch RESOLVED-by-promotion + reconcile the "2nd FIRM consumer" wording. **My promotion of the GMG column to firm now makes that watch's literal "2nd FIRM consumer" trigger ALSO satisfiable** (GMG is now a firm 2nd consumer) — but this changes nothing operationally: the page already exists and the promotion was already correctly sanctioned at the ≥2-consumers floor. The wording-reconcile remains the meta-phase's already-scheduled action; my flip simply removes the last "but the trigger said FIRM and GMG was rough-in" tension. No edit to the concepts page or the record-watch is in my scope; flagging for the meta-phase that the GMG firm-flip retires that tension.
- **RE1 reachability after re-classification:** moving `L3/chebyshev`/`L2/jacobi-smoother` from `depends-on` to `reference` on the L4 file means the column no longer GROUNDS RE1 *over depends-on edges* — RE1's reachability had been claimed via the L4 `depends-on (composes)` edge to `L3/chebyshev`. After this change the L4 column reaches chebyshev/jacobi only over a `reference` edge (which the reachability GC does NOT traverse). **However:** (a) the L4 `depends-on→ L1/multigrid-relaxation-smoother→ L1/chebyshev-smoother` chain keeps the *L1* chebyshev-smoother reachable; (b) the c122 planner's RE-recheck already classifies RE1 (`L4/chebyshev`, `L3/chebyshev`, `L2/chebyshev-iteration`, `L2/jacobi-smoother`, `L4/preconditioning-framework`) as **GROUNDED but NOT on the STRONGER list** — i.e. the L2/L3 *iteration-views* of chebyshev were already understood to ride the absorbed leg (same shape as RE5/RE7). The honest position is that the L2/L3 chebyshev/jacobi iteration-VIEWS are NOT faithfully reachable over `depends-on` from this column (a column→L3-iteration-view depends-on edge would be the §2g over-edge), exactly like RE2/RE5/RE7/RE8. **Flag for the c123/batch-39 meta:** confirm whether the RE1 "GROUNDED" verdict should be re-stated as "the L1 chebyshev-smoother is grounded via the smoother; the L2/L3 chebyshev iteration-views remain absorbed-below-spine (same disposition as RE5/RE7), needing the L3-iteration-view feature column (item-4b) for a faithful by-name composer." This is a faithful-classification correction, not a regression — the prior `depends-on (composes)` edge to `L3/chebyshev` was the unfaithful over-edge that this re-classification removes. I have NOT altered the RE ledger (out of scope); routing as an OQ for the meta's standing RE-recheck.
- **Re-run the linter after applying:** confirm EXIT 0 / `rank_violations: 0` holds (it should — all blocking deps are firm; the two demoted edges become `reference`, which the rank check ignores) and that `L1/fe_space_hierarchy` + `multigrid-relaxation-smoother` show the inbound `depends-on` from the now-firm GMG column (`--show-inbound`). This is also the `fe-space-hierarchy-concepts-page-re9-c122-linter-confirm` c121-OQ measurement the planner assigned to c122.
- **`pc_it`-fold / level-recursion sequential-obstruction at the column level:** the c121 prose offered an alternative promotion path — "the chebyshev partial-obstruction's V-cycle recursion is either lifted OR accepted as a documented sequential-obstruction at the column level." I took the **accept-as-documented** path (it is the smoother's own disposition, applied identically to the composition). The recursion is NOT lifted to a whole-tensor form (it genuinely is a level-recursive sequential structure); the firm claim is the *compositional* firm-on-positive-structure claim over exhaustively-cited source, with the sequential-obstruction documented — NOT a claim that the V-cycle iteration vectorizes.

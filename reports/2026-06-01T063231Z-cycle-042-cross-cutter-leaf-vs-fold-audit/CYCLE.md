---
agent: same-layer-cross-cutter
invoked_at: 2026-06-01T063231Z
scope: L2 cross-cut — leaf-vs-fold-design-fork-audit
status: pending
integrated_at: 2026-06-01T081245Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-042 batch integration (foundation-first L2-floor build); applied clean; see reports/2026-06-01T081245Z-integrator-finalize-cycle-42/CYCLE.md + cycle-042 STAGING row."
---

# CYCLE: L2 observation — leaf-vs-fold design fork (D1 leaf-floor vs D2 fold-only)

## Summary

Comparing the five same-layer L2 inner-product / linear-combination cohort members
(`dot`, `nrm2`, `scal` floors + `inner_product`, `linear_combination` folds) against
their adjacent-layer (L2>L1, L3>L2) lowering chains and against the L3 anchors, I find that
the cycle-041 wave-1 **leaf-floor reading (b)** does **NOT** cause duplication explosion in
adjacent layers in the methodology's pejorative sense, and that the leaf is a
**genuinely-distinct dual** of the fold — not a redundant restatement of it. The count
delta between the two readings is **+2 chapters and +2 themes** (one L2 leaf chapter + one
L2>L1 theme + one re-anchored L3>L2 theme, per leaf, for `dot` and `scal`), but each of
those leaf floors is *identity-in-form and DEFERS the full de-fusion to the fold-parent,
flagging its laws as inherited* — the
"duplication explosion" the methodology warns against is **duplication of substantive
adjacent-layer authoring**, and these floors do not independently re-author that substance:
they assert identity, carry their laws as inherited-unchanged, and defer the full fusion
treatment to the fold-parent. The reader-reconciliation cost is real but
bounded (each leaf chapter's first paragraph + a do-NOT-merge section point at the fold).
The decisive structural fact is the **methodology invariant "Identity-lowerings still
require both L levels"** (CLAUDE.md): the firm L3 `dot`/`scal` leaves *already exist* and a
reader navigating L3 must find an adjacent same-named L2 parent. I recommend **hybrid /
keep-leaf-floor (b) with a one-line generalization**, framed below as input to the batch-12
meta-phase adjudication. **The meta-phase decides; this report supplies the count-delta
evidence and the distinctness verdict.**

## Observation kind

**Unification candidate** (adjudication input) — the question is whether the leaf operators
`L2/dot`, `L2/scal` should be unified INTO (subsumed by) their fold-parents `inner_product`,
`linear_combination` (the D2 "fold-only" reading), or kept as same-named specializations
cited-but-not-merged (the D1/D3 "leaf-floor" reading). I find they are **genuinely-distinct
duals that should NOT be unified away**, with the caveat that the distinctness rests on the
"both L levels" invariant rather than on intrinsic algebraic novelty.

## Specific finding

### 1. The fork applies to `dot` and `scal` but NOT to `nrm2`

A critical asymmetry the meta-phase must not miss: the three cycle-041 floors are **not**
symmetric under the fork.

- **`dot`** (D1) — the conjugation-axis **leaf-of** `inner_product` (fold-parent). The fork
  applies: under fold-only, `L2/dot` ceases to exist standalone and folds into
  `inner_product`'s conjugation dispatch.
- **`scal`** (D3) — the arity-1 **leaf-of** `linear_combination` (fold-parent). The fork
  applies: under fold-only, `L2/scal` folds into `linear_combination`'s arity-1 row.
- **`nrm2`** (D2) — a **CONSUMER of** `inner_product` (`nrm2 = √ ∘ abs ∘ inner_product` at
  `y=x`), explicitly **NOT a fold member** (`book/src/L2/nrm2.md:27-35`,
  `book/src/L2/inner_product.md:390-404`). **The fork does NOT apply to `nrm2`'s
  membership** — it is a consumer either way; there is exactly one L1 `nrm2` leaf to lower
  onto and `dot(x,x) = inner_product(x,x)` holds at the diagonal regardless. The ONLY thing
  the fork touches for `nrm2` is whether its standalone L2 *floor* exists at all (the
  "both L levels" question), not its fold-membership. (Confirmed by OQ
  `nrm2-l2-floor-rides-...` at `scaffolding/open-questions.md:978`.)

So D2's argument ("the L2 inner-product surface should be the fold ONLY, no same-named
leaf") is really **two claims bundled**: (i) `nrm2` is a consumer-not-member — *correct and
uncontested*; (ii) `dot` should not get a same-named L2 leaf-floor — *the actual fork*. The
batch-12 meta-phase should disentangle these: D1 and D2 are **not** as contradictory as the
OQ framing (`dot-l2-leaf-floor-vs-fold-only-design`, `scaffolding/open-questions.md:965`) suggests — D2
never actually authored a fold-only `dot`; it declined to author a `dot` leaf and asserted
none was needed. The genuine disagreement is narrow: **does the "both L levels" invariant
compel a same-named L2 leaf under a firm L3 leaf, even when an L2 fold-parent already
covers the same value?**

### 2. The count-delta table (the core deliverable)

Tabulating the adjacent-layer chapter/theme/dep-map footprint for the **`dot`** chain under
each reading (the `scal` chain is structurally identical; `nrm2` is fork-invariant):

| Artifact | Leaf-floor (b) — CURRENT | Fold-only (a) | Δ (b − a) |
|---|---|---|---|
| **L2 chapter** `L2/dot.md` | exists (345 ln, identity-in-form floor; laws inherited-unchanged, full de-fusion deferred to fold-parent) | absent (subsumed into `inner_product`) | **+1 chapter** |
| **L2>L1 theme** `dot-leaf-identity.md` | exists (220 ln, identity edge) | absent (edge subsumed into `inner-product-fold-specialization` conjugation dispatch) | **+1 theme** |
| **L3>L2 theme** `dot-body-identity.md` | exists, RHS = `L2/dot` (185 ln) | exists but **re-anchored**: RHS = `inner_product` (fold), OR re-homed as non-adjacent in-line note at `L3/dot` | **±0 file** (re-anchor, not add/remove) |
| **L3 chapter** `L3/dot.md` | unchanged (firm cycle-011) | unchanged; §"Lowers to" re-points to fold-parent | **±0** |
| **L1 chapter** `L1/dot.md` | unchanged (firm cycle-002) | unchanged | **±0** |
| **L2 dep-map row** (`L2/index.md`) | +1 leaf row (`dot` row) | 0 (no leaf row; fold row already present) | **+1 row** |
| **SUMMARY.md line** | +1 (`- [dot](./L2/dot.md)`) | 0 | **+1 line** |
| **Reader reconciliation** | leaf chapter §"Relation to `inner_product`" + first para | none (one fold chapter) | **+1 reconcile site/leaf** |

**Per-leaf net under (b): +1 L2 chapter, +1 L2>L1 theme, +1 dep-map row, +1 SUMMARY line,
+1 reader-reconcile site; the L3>L2 theme is a re-anchor either way (not a net add).**

**Across the family** (`dot` + `scal`, the two leaves the fork actually touches; `nrm2`
contributes its floor under the "both L levels" question independently):

| | Leaf-floor (b) | Fold-only (a) | Δ |
|---|---|---|---|
| L2 leaf chapters | 2 (`dot`, `scal`) | 0 | **+2** |
| L2>L1 leaf themes | 2 (`dot-leaf-identity`, `scal-fold-specialization`) | 0 (subsumed into the two fold themes) | **+2** |
| L3>L2 themes | 2 (`dot-body-identity`, `scal-body-identity`) | 2 (re-anchored RHS → fold) | **±0** |
| L2 dep-map rows | +2 | 0 | **+2** |

So the **total adjacent-layer delta is +4 files (2 chapters + 2 themes) + 2 dep-map rows**
for the two genuine-fork leaves. Note the fold themes
(`inner-product-fold-specialization`, `linear-combination-fold-specialization`) and the
fold chapters (`inner_product`, `linear_combination`) **exist under BOTH readings** — they
are not part of the delta. The delta is purely the *thin identity leaves*.

### 3. Is +4 thin files a "duplication explosion"? — NO

The methodology bar (CLAUDE.md §Process model): "duals OK if genuinely distinct; not OK if
they force **duplication explosion in adjacent layers**." The operative word is
*duplication*. Examining the four delta files:

- `L2/dot.md` (`book/src/L2/dot.md`) — its §"Fusion note" (`:142-164`) explicitly states
  "there is no fusion structure unique to the `dot` leaf beyond the fold-parent's" and
  defers the full de-fusion treatment to `inner_product`. Its §"Algebraic laws"
  (`:166-212`) are stated "inherited unchanged from the L1 leaf." It **duplicates no
  adjacent-layer authoring** — it asserts identity and points.
- `dot-leaf-identity.md` (L2>L1) — the entire §"The rewrite (L2 → L1)" (`:84-110`) is a
  total-bijective identity table + one deferral note ("all fusion content is the
  fold-parent's"). It **authors no rewrite content**; it records a no-op edge.
- `dot-body-identity.md` (L3>L2) — same shape; total-bijective identity table, "no wrapper
  to rotate."
- `scal-body-identity.md` (`book/src/L3-L2/scal-body-identity.md:86-107`) — explicitly "the
  thinnest member of the L3>L2 lowering family," identity on a single binding.

The duplication-explosion failure mode the methodology warns against is when a dual forces
**substantive re-authoring of rewrite themes in the adjacent layers** — e.g. if each leaf
required its OWN de-fusion treatment, its OWN reduction-tree pinning, its OWN conjugation
reconciliation, duplicating what the fold theme says. **That is precisely what these floors
DECLINE to do**: every floor and every leaf theme defers the full fusion treatment to the
fold-parent (`inner-product-fold-specialization` / `linear-combination-fold-specialization`)
and carries its laws as inherited-unchanged rather than re-deriving them. The substantive
content a floor does carry (e.g. `L2/dot.md`'s §"Fusion note" and §"Algebraic laws") is a
deferral-and-inheritance restatement, not an independent re-authoring of the fold's de-fusion
treatment. This is duplication of **chapter scaffolding** (a heading, a signature, a
deferral note, inherited laws), not duplication of **adjacent-layer rewrite substance**. By the methodology's own test, the leaf-floor reading does **not** cross the
"not OK" threshold.

### 4. Are the leaves genuinely-distinct duals of the folds? — YES, on the "both L levels" axis

The leaf and the fold differ on a load-bearing axis that is NOT mere naming:

- **The fold collapses a variant axis the leaf fixes.** `inner_product` unifies the
  conjugation × element-type × weight family (`book/src/L2/inner_product.md:313-346`);
  `dot` is the plain (`M = I`) Hermitian/symmetric member at ONE fixed conjugation value.
  `linear_combination` unifies the arity axis (`book/src/L2/linear_combination.md:214-241`);
  `scal` is the arity-1 member. The leaf is a *named point* on the fold's unification axis —
  the same relationship `axpy`/`axpby` have to `linear_combination` at L1, which the
  `axpby-as-primitive` decision (`scaffolding/decisions/axpby-as-primitive.md`) already
  ratified as "fuse, don't decompose; keep the leaves firm."
- **The L3 leaf demands an adjacent L2 parent.** This is the decisive, non-aesthetic reason.
  The firm L3 `dot` (cycle-011) and firm L3 `scal` (cycle-011) **already exist as standalone
  same-named L3 chapters**. CLAUDE.md "Identity-lowerings still require both L levels" is
  explicit: "a reader navigating L_n should not have to jump up to L_{n+1} to find the
  operator." Under fold-only, the firm L3 `dot` leaf would lower L3>L2 to a *differently-named*
  `inner_product` fold — a non-adjacent-in-name lowering that the "both L levels" invariant
  and the adjacent-edge structural invariant were written to prevent. The leaf-floor reading
  is the one that *honors the existing firm L3 cohort*; the fold-only reading would leave the
  firm L3 `dot`/`scal` resting on a same-named-parent gap.

So the leaf is distinct from the fold along the **layer-coherence axis** (every layer
self-contained, same-named operator present at each level) — a genuine methodological
distinction, even though the leaf carries no algebraic content the fold lacks. This is the
"each layer is coherent within itself" rationale, not a duplication.

### 5. The residual cost the meta-phase should weigh

The leaf-floor reading is NOT free. Two real costs:

- **Reader reconciliation**: a reader landing on `L2/dot` must read the §"Relation to
  `inner_product` (fold-parent; do NOT merge)" section to understand it is a leaf, not a
  rival fold. Multiplied across the cohort this is a recurring "why are there two chapters
  for the same value?" question. The floors mitigate this with prominent do-NOT-merge prose,
  but the cost is non-zero.
- **Scaffolding multiplicity**: +4 files + 2 dep-map rows that must stay in sync with the
  fold-parents (if `inner_product`'s conjugation convention is ever re-pinned, the `dot`
  leaf's inherited-convention prose must follow). This is a maintenance coupling, not a
  duplication of content, but it is a coupling.

These costs are **bounded and one-time-per-leaf**, and they are the same costs the L1 BLAS-1
leaf cohort (`scal`/`axpy`/`axpby`/`axpbypcz` vs `linear_combination`) already pays and that
the project already accepted at L1. The L2 cohort is the consistent extension of an accepted
L1 precedent.

## Recommendation

**Keep the leaf-floor reading (b); ratify it as the cohort-wide convention; add one
generalization sentence.** Framed explicitly as **input to the batch-12 meta-phase
adjudication** (the meta-phase decides go/no-go; this is the evidence):

1. **Adopt (b) leaf-floor as the ratified reading** for the L2 BLAS-1 floor cohort. Reasons,
   in priority order: (i) the firm L3 `dot`/`scal` cohort already exists and the "both L
   levels" + adjacent-edge invariants compel a same-named L2 parent; (ii) the delta is +4
   *pointer* files with zero adjacent-layer rewrite-content duplication — below the
   methodology's "duplication explosion" threshold; (iii) it is the consistent extension of
   the already-accepted L1 `axpby-as-primitive` "keep leaves firm, fuse don't decompose"
   decision; (iv) the leaf-of-fold relation is genuinely distinct on the layer-coherence
   axis.

2. **Disentangle the D1-vs-D2 "contradiction."** The OQ framing overstates it. D2 never built
   a fold-only `dot`; it (correctly) declined to make `nrm2` a fold member and (separately)
   declined to author a `dot` leaf. The meta-phase should record that the only live question
   is "does a firm L3 leaf compel a same-named L2 floor" — and answer YES per invariant.

3. **One-line generalization** the meta-phase may enact into `book/src/L2/index.md`
   §"Fold-cohort boundary" (Working Note): "Each firm L3 BLAS-1 leaf gets a same-named L2
   floor (the 'both L levels' invariant); the floor is cited as a leaf-of / consumer-of the
   relevant fold and defers all fusion content to the fold-parent — it is a layer-coherence
   pointer, not a rival fold." This closes the fork as a *standing convention* so future
   floors (the held `axpy`/`axpby`/`axpbypcz` arity family — see below) don't re-litigate it.

4. **If the meta-phase instead adopts (a) fold-only** (NOT my recommendation): it must
   accept that the firm L3 `dot`/`scal` leaves lower L3>L2 to differently-named fold-parents
   (a same-named-parent gap), re-anchor `dot-body-identity` / `scal-body-identity` RHSs to
   the folds (or re-home as non-adjacent in-line notes per the
   `l3-l1-inline-identity-rotation-convention`), and dissolve `dot-leaf-identity` +
   `scal-fold-specialization` into the two fold themes' dispatch rows. The +4-file saving is
   real but buys a layer-coherence regression on an already-firm L3 cohort.

**No follow-up dispatch is needed from THIS observation beyond the meta-phase adjudication
itself** — the floors and themes are already firm-and-self-coherent under (b); they need a
*decision*, not new authoring. If the meta-phase ratifies (b), a one-line
layer-intro-author touch to `L2/index.md` §"Fold-cohort boundary" enacts the generalization.

## Consequence for the held `axpy` / `axpby` / `axpbypcz` arity family

The same fork governs the **held arity-family floors** — `axpy`/`axpby`/`axpbypcz` are the
arity-2/2/3 leaves of `linear_combination`, exactly as `scal` is the arity-1 leaf. Three
observations for the meta-phase:

- **The fork must be settled BEFORE the arity-family L2 floors are dispatched**, or each of
  the three will re-surface the identical OQ. Ratifying (b) as a standing convention (rec. 3)
  pre-resolves all three: each gets a same-named L2 floor + an L2>L1 fold-specialization
  theme (arity-2/2/3 rows) + an L3>L2 body-identity theme, all deferring fusion to
  `linear-combination-fold-specialization`.
- **The delta scales linearly and stays thin**: +3 more leaf chapters + 3 L2>L1 themes under
  (b), each a pure arity-N pointer into the existing `linear_combination` fold. No new
  adjacent-layer *content* — the fold theme already carries the de-fusion + summation-order
  pinning for the whole arity family (`book/src/L2/linear_combination.md:243-254`). This
  confirms the duplication-explosion verdict holds at family scale: the fold absorbs the
  substance once; the leaves are N thin pointers.
- **One caveat specific to the arity family**: `axpy`/`axpby`/`axpbypcz` carry an
  **output-aliasing variant axis** (`book/src/L2/linear_combination.md:220-228`) that `scal`
  and `dot` lack salience on. The arity-family leaf floors should each note the aliasing axis
  is the fold's, not a leaf-specific axis (consistent with the fold's treatment) — a small
  authoring note, not a fork re-opening.

## Supporting evidence

L2 cohort entries compared:
- `book/src/L2/dot.md` — leaf-floor (b); §"Relation to `inner_product` (fold-parent; do NOT
  merge)" (`:41-68`), §"Fusion note" deferral (`:142-164`), §Status thin-floor (`:258-271`).
- `book/src/L2/scal.md` — arity-1 leaf-floor (b); §Context fold-membership-cited-not-merged
  (`:41-53`), §"Fold-specialization identity" (`:158-167`).
- `book/src/L2/nrm2.md` — **consumer-not-member** (fork-invariant on membership);
  §"Consumer of `inner_product`, NOT a fold member" (`:27-35`).
- `book/src/L2/inner_product.md` — fold-parent; the unification axis (`:313-346`), the
  §"Consumer (NOT an instance): nrm2 / matrix-weighted-norm" boundary (`:390-404`).
- `book/src/L2/linear_combination.md` — fold-parent; the arity unification (`:214-241`),
  §"Sibling fold: dot is not subsumed" (`:256-269`).

Adjacent-layer themes compared:
- `book/src/L2-L1/dot-leaf-identity.md` — identity edge, total-bijective table (`:84-110`),
  §"Applicability conditions" condition 1 (the design-presupposition, `:114-122`), §Status
  "Design-presupposition note" (`:210-216`).
- `book/src/L3-L2/dot-body-identity.md` — identity edge, §"Applicability conditions"
  condition 2 (`:101-106`), §Status "Design-presupposition note" (`:180-185`).
- `book/src/L3-L2/scal-body-identity.md` — "thinnest member" (`:206-218`), §Status standing
  fork note (`:220-226`), §Open-questions leaf-vs-fold fork (`:237-238`).
- `book/src/L3-L2/nrm2-body-identity.md` — fork-invariant (consumer; `dot(x,x) =
  inner_product(x,x)` at diagonal, `:125-131`).

L3 anchors (the "both L levels" driver):
- `book/src/L3/dot.md` (firm cycle-011) — §"Lowers to" currently records non-adjacent
  identity to L1 (`:127-131`); the leaf-floor supplies the now-present adjacent L2 parent.
- `book/src/L3/scal.md` (firm cycle-011), `book/src/L3/nrm2.md` (firm cycle-011).

Cycle-041 wave-1 reports (the D1-vs-D2 framing):
- `reports/2026-06-01T051607Z-cycle-041-harvester-L2-dot/CYCLE.md` — D1 built the leaf-floor;
  §Open-questions "No leaf-unique fusion surplus found" (`:461-467`).
- `reports/2026-06-01T051607Z-cycle-041-harvester-L2-nrm2/CYCLE.md` — D2 argued no `dot`
  leaf needed; §Open-questions "No L2 `dot` floor exists" (`:197`).

OQ ledger:
- `scaffolding/open-questions.md:965` (`dot-l2-leaf-floor-vs-fold-only-design`, the canonical
  fork OQ), `:950` (`l2-no-dot-leaf-floor-but-fold-is-the-l2-surface`, D2's scoping note),
  `:978` (`nrm2-l2-floor-rides-...`, the nrm2 fork-invariance), `:986`
  (`scal-leaf-vs-linear-combination-fold-realization-fork`).

Methodology anchors:
- CLAUDE.md §Methodology invariants "Identity-lowerings still require both L levels" (the
  decisive invariant), "Layers are defined high→low", "Lower-level shared vocabulary takes
  priority".
- CLAUDE.md §Process model "coalesce by use; duals OK if genuinely distinct; not OK if they
  force duplication explosion in adjacent layers" (the test applied).
- `scaffolding/decisions/axpby-as-primitive.md` (the accepted L1 leaf-vs-fold precedent).

## Open questions / caveats

- **The distinctness verdict rests on a methodological axis, not an algebraic one.** I find
  the leaves genuinely distinct from the folds on the *layer-coherence* axis (same-named
  operator present at each level), NOT because the leaf carries algebraic content the fold
  lacks (it does not — every law is inherited). A meta-phase that weights "minimal chapter
  count" over "each layer self-contained" could legitimately reach the opposite verdict. I
  flag this so the meta-phase weighs the two invariants explicitly rather than treating the
  count-delta as decisive.
- **D1-vs-D2 is narrower than "contradiction."** Verify my reading that D2 never authored a
  fold-only `dot` (it declined to author one) before treating the two reports as
  irreconcilable. If correct, the meta-phase's task is ratifying a convention, not breaking a
  tie between two built artifacts.
- **`nrm2` should be carved out of the fork explicitly.** Whatever the meta-phase decides for
  `dot`/`scal`, `nrm2`'s consumer-not-member status is uncontested and correct; only its
  standalone-floor existence rides the "both L levels" question. The meta-phase should state
  this carve-out so a future audit doesn't re-open `nrm2`'s membership.
- **One observation per invocation** — I have NOT bundled the held arity-family dispatch
  decision into a separate observation; the §"Consequence" section is consequence-of-this-
  observation, not a second observation. The arity-family floors are downstream of whatever
  the meta-phase rules here.
- I wrote this CYCLE.md to disk directly per role spec; no filter block encountered.

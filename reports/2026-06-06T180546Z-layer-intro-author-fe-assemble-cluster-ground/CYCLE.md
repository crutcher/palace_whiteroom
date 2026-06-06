---
agent: layer-intro-author
invoked_at: 2026-06-06T180546Z
scope: FE-assemble cluster GROUND — canonical typed `edges:` blocks on L1/fe_assemble + L1/fe_space (frontmatter-only migration + composes grounding)
status: pending
dispatch: cycle-114 D1
integrated_at: 2026-06-06T200000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean by integrator-per-report (staging row D1); no repair-phase warnings carried to finalize. Frontmatter-only edge-grounding: rank: firm + composes->{weak_form_term,fe_space} + lowers-to + cites-evidence on L1/fe_assemble.md + L1/fe_space.md. +5 reachable (3 direct nodes + 2 transitive L1>L0 themes). rank_violations HELD 0, unresolved HELD 0. Build EXIT 0, no finalize build-repair. 2 OQs promoted (fe_collection-own-constituents-future-pass, fe_space-deferred-siblings-still-ungrounded)."
---

# CYCLE: FE-assemble cluster GROUND (L1/fe_assemble + L1/fe_space)

## Summary

Two **frontmatter-only** migrations onto the batch-33-ratified graded-stack scheme, each adding faithful
`composes`-kind `depends-on` grounding edges that flip a firm-but-currently-garbage FE cluster reachable:

- `book/src/L1/fe_assemble.md` — migrate off legacy `firmness: firm` + `lowers_to:` + empty `depends_on: []`
  to `rank: firm` + typed `edges:`. Add `composes` edges to `L1/weak_form_term` (the `[WeakFormTerm]` fold
  element-type) and `L1/fe_space` (the `space:` input); preserve the existing `lowers_to` as a `lowers-to`
  `depends-on` edge.
- `book/src/L1/fe_space.md` — author an `edges:` block from the bare `status: firm` (NO edges today).
  Add a `composes` edge to `L1/fe_collection` (the `collection: FECollection` input), a `cites-evidence`
  edge to the positive L0 ctor (`palace/fem/fespace.hpp:67-75`, already in the chapter's Evidence), and a
  `lowers-to` edge to its L1>L0 theme `L1-L0/fe-space-construction-rotation`.

**No prose body is touched** — frontmatter only. `L1/fe_assemble` is already reachable (inbound from 7
feature columns); the 3 `composes` edges (2 on fe_assemble, 1 on fe_space) route liveness down the chain
`fe_assemble →composes→ {weak_form_term, fe_space} →composes→ fe_collection`, flipping all three reachable
plus the two L1>L0 themes they `lowers-to`.

## Proposed changes

```edit:book/src/L1/fe_assemble.md
[old]:
---
layer: L1
operator: fe_assemble
firmness: firm
lowers_to:
  - L1-L0/fe-operator-assemble-mutation-rotation
lifts_from: []
depends_on: []
variant_axes:
  - assembly-representation
  - term-position
  - trial-test-coincidence
---
[new]:
---
layer: L1
operator: fe_assemble
# Graded-stack scheme (migrated batch-36 c114 off legacy firmness/lowers_to/depends_on frontmatter).
# This firm L1 assembly FOLD composes its two firm L1 inputs — the term-list element type
# `weak_form_term` and the FE-space input `fe_space` — and lowers through its L1>L0 mutation-rotation
# theme (lowers-to depends-on; the c108 §5 L1-op→theme grounding convention, mirroring set_subvector_zero).
# The two `composes` edges flip `weak_form_term` + `fe_space` reachable (both firm-but-currently-garbage);
# `fe_assemble` itself is reachable (inbound from 7 feature columns). Well-foundedness rank(u) <= rank(v):
# this node is firm (rank 3) and both composed inputs carry `rank: firm`. The `lowers_to` edge is preserved
# exactly as the pre-scheme `lowers_to` (the theme `fe-operator-assemble-mutation-rotation` is `status: firm`,
# so rank(op=3) <= rank(theme=3) holds). The variant_axes (assembly-representation / term-position /
# trial-test-coincidence) are documented in the chapter body §Variant axes (the scheme drops the frontmatter
# list; the prose is the home).
rank: firm
edges:
  depends-on:
    - target: L1/weak_form_term
      kind: composes              # the `terms: [WeakFormTerm]` fold element-type (sig :60, :71-72; §Dependencies :163)
    - target: L1/fe_space
      kind: composes              # the `space: FiniteElementSpace[N]` input (sig :60, :68-70)
    - target: L1-L0/fe-operator-assemble-mutation-rotation
      kind: lowers-to             # the L1>L0 mutation-rotation theme (preserved from pre-scheme `lowers_to`)
  reference:
    - L1/bilinear-form             # slug-collision sibling (a DIFFERENT object; do NOT conflate — §Slug-collision)
---
```

```edit:book/src/L1/fe_space.md
[old]:
---
status: firm
harvested_by: harvester:2026-06-02T151056Z-harvester-fe-space
cycle: cycle-064
---
[new]:
---
layer: L1
operator: fe_space
harvested_by: harvester:2026-06-02T151056Z-harvester-fe-space
cycle: cycle-064
# Graded-stack scheme (edges authored from scratch, batch-36 c114; chapter previously carried only
# `status: firm`, NO edges). This firm L1 construction composes its one firm L1 input — the
# `collection: FECollection`, produced by `fe_collection` — and rests on its positive L0 ctor source
# (cites-evidence, rank-terminal ground truth) + lowers through its L1>L0 construction-rotation theme.
# The `composes` edge to `fe_collection` flips it reachable (firm-but-currently-garbage); `fe_space`
# itself flips reachable transitively via `fe_assemble`'s c114 `composes` edge (sibling D1 migration).
# Well-foundedness rank(u) <= rank(v): this node firm (rank 3); `fe_collection` carries `rank: firm`
# (status: firm, cycle-065); the cites-evidence target is rank-terminal L0 ground truth; the lowering
# theme `fe-space-construction-rotation` is `status: firm` (rank 3 <= 3).
rank: firm
edges:
  depends-on:
    - target: L1/fe_collection
      kind: composes              # the `collection: FECollection` input, produced by fe_collection (sig :9/:43; §Variant-axis :89)
    - target: palace/fem/fespace.hpp:67-75
      kind: cites-evidence        # the variadic `FiniteElementSpace(Mesh&, T&&...)` ctor — the (mesh,collection) pairing (Evidence :191-193)
    - target: L1-L0/fe-space-construction-rotation
      kind: lowers-to             # the L1>L0 construction-rotation theme (cycle-064 D3; §Downward :145)
  reference:
    - L1/fe_assemble               # the primary consumer of the constructed space
    - L1/weak_form_term
    - L1/eliminate_essential_bc
    - L1/eliminate_rhs
---
```

## Faithful-edge derivation (verified from signature + prose before writing — faithful-edge-or-finding)

Each edge was read out of the chapter's own signature/prose; none is a number-flipping over-edge.

1. **`L1/fe_assemble →composes→ L1/weak_form_term`** — `weak_form_term` is the **element type of
   `fe_assemble`'s term list**. Verified at:
   - `fe_assemble.md:60` — signature `fe_assemble :: (space: FiniteElementSpace[N], terms: [WeakFormTerm]) -> LinearOperator[N, N]` — `[WeakFormTerm]` is the fold's input list.
   - `fe_assemble.md:71-72` — "`terms` — `[WeakFormTerm]` … Each element is a firm [`weak_form_term`](./weak_form_term.md) — a `(coefficient, differential-operator)` pair (firm cycle-061)."
   - `fe_assemble.md:163` — §Dependencies: "[`weak_form_term`](./weak_form_term.md) (type) — **firm** (cycle-061); … the element type of the term list."
   `composes` is the faithful kind: `fe_assemble` is the fold quantifying over the term list (a constituent-use, not a lowering). The fold treats the term *opaquely* (doesn't crack its internals), but it DOES compose over the list — a `composes` edge, not a `reference`. Confirmed `L1/weak_form_term.md` exists and is `firmness: firm`.

2. **`L1/fe_assemble →composes→ L1/fe_space`** — `fe_space` produces the `space:` input. Verified at:
   - `fe_assemble.md:60` — signature names `space: FiniteElementSpace[N]`.
   - `fe_assemble.md:68-70` — "`space` … the trial/test finite-element space, **constructed by [`fe_space`](./fe_space.md)** … `N = space.GetTrueVSize()` … the axis `fe_space` defines."
   `composes` is faithful: the space is a directly-consumed constituent input. Confirmed `L1/fe_space.md` exists and is `status: firm`.

3. **`L1/fe_space →composes→ L1/fe_collection`** — `fe_space` consumes one `FECollection`. Verified at:
   - `fe_space.md:9` / `fe_space.md:43` — signature `fe_space :: (mesh: Mesh, collection: FECollection) -> FiniteElementSpace[N]` — `collection: FECollection` is a direct input.
   - `fe_space.md:50-52` — "`collection` — `FECollection` — the finite-element collection selecting the basis family + order … At L0 it is the second forwarded ctor argument."
   - `fe_space.md:89` — "the list-producing order-schedule is deferred to the `fe_collection` / `fe_space_hierarchy` follow-on" — names `fe_collection` as the upstream producer of the `collection` input.
   `composes` is faithful: `fe_collection` produces the `[FECollection]` whose entries `fe_space` consumes one-per-level (corroborated by `fe_collection.md:9` "the upstream producer of the `[FECollection]` whose entries `ConstructFiniteElementSpaceHierarchy` feeds one-per-level into [fe_space]"). Confirmed `L1/fe_collection.md` exists and is `status: firm` (cycle-065). NOTE the relationship is a genuine constituent-use (`composes`), NOT a lowering — `fe_collection` is a peer L1 op producing a value `fe_space` takes, not a lower-layer form of `fe_space`.

4. **`L1/fe_assemble →lowers-to→ L1-L0/fe-operator-assemble-mutation-rotation`** — preserved from the
   pre-scheme `lowers_to:` field (`fe_assemble.md` old frontmatter :5-6); the theme is named in-prose at
   `fe_assemble.md:45,278-285` (§Downward to L0). File confirmed present, `status: firm`. Per the c108 §5
   L1-op→theme convention this is a blocking `depends-on (kind: lowers-to)` — it routes liveness DOWN to
   the theme (the theme was already reachable via eliminate_essential_bc/eliminate_rhs, so no NEW rescue
   here, but the migration must preserve it faithfully).

5. **`L1/fe_space →lowers-to→ L1-L0/fe-space-construction-rotation`** — named in-prose at `fe_space.md:38-39`
   and :145-150 (§Downward, "authored cycle-064 D3"). File confirmed present, `status: firm`. This edge
   transitively rescues the theme (it was previously garbage — see standalone delta).

6. **`L1/fe_space →cites-evidence→ palace/fem/fespace.hpp:67-75`** — the positive L0 ctor source, already
   in the chapter's Evidence (`fe_space.md:191-193`: "the variadic `FiniteElementSpace(Mesh &mesh, T &&...args)`
   constructor"). Cheaply read off the existing chapter (per the dispatch's "add the L0 cites-evidence ONLY if
   cheaply read off the existing chapter"). Rank-terminal ground-truth target; satisfies the firm-rests-on-firm
   well-foundedness invariant on the L0 leg. (Not strictly required for the +Δ, but it grounds `fe_space`'s
   `rank: firm` on a positive site per the set_subvector_zero template, and costs nothing — the cite is
   verbatim from the chapter.)

## Standalone linter delta (isolated; D2 contamination stashed out)

D2 runs in parallel on `L1/dot`, `L1/nrm2`, `L1/scal`. To avoid `parallel-dispatch-reachability-measurement-contamination`
I `git stash`-parked D2's three files, confirmed the **clean baseline** matched the dispatch-given baseline
(`reachable=124, detritus=135, STRONGER GARBAGE SIGNAL=24, rank_violations=0`), applied **only my two files**,
and measured:

| metric | clean baseline | + my 2 files | Δ |
|---|---|---|---|
| reachable from roots | 124 | **129** | **+5** |
| detritus | 135 | **130** | **−5** |
| STRONGER GARBAGE SIGNAL | 24 | **23** | **−1** (`weak_form_term`) |
| rank_violations | 0 | **0** | HELD 0 |
| unresolved | 0 | 0 | held |

**+5 (vs. the estimated +3).** The estimate counted the 3 direct targets; the actual +5 also captures the
**two L1>L0 lowering themes** the rescued nodes carry, pulled in transitively:
- `L1/weak_form_term` (direct, was `[GARBAGE*]` — the −1 on STRONGER GARBAGE SIGNAL)
- `L1/fe_space` (direct)
- `L1/fe_collection` (direct, via `fe_space →composes→ fe_collection`)
- `L1-L0/fe-assemble-libceed-boundary-obstruction` (transitive — `weak_form_term`'s own `lowers_to`)
- `L1-L0/fe-space-construction-rotation` (transitive — `fe_space`'s new `lowers-to` edge)

`--show-inbound` confirms the rescue is **measurable**: after my edits the rescued nodes show inbound edges
`L1/weak_form_term <- L1/fe_assemble`, `L1/fe_space <- L1/fe_assemble`, `L1/fe_collection <- L1/fe_space`.

**Tree left clean for my files:** I reverted both my files to pristine git state (`git checkout`); only D2's
three files remain modified (D2 owns those). The authoritative cumulative is the finalize step-5b re-measure.

## Supporting evidence

- `book/src/L1/fe_assemble.md` (firm, cycle-054) — the assembly fold; signature :60, term-list element-type :71-72/:163, fe_space input :68-70, lowering theme :45/:278-285.
- `book/src/L1/fe_space.md` (firm, cycle-064) — the space construction; signature :9/:43, collection input :50-52/:89, L0 ctor Evidence :191-193, lowering theme :38-39/:145-150.
- `book/src/L1/weak_form_term.md` (firm, cycle-061) — the `(coefficient, differential-operator)` term value (`firmness: firm`).
- `book/src/L1/fe_collection.md` (firm, cycle-065) — the `[FECollection]` order schedule (`status: firm`); :9 names fe_space as the consumer.
- `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md` (`status: firm`) — fe_assemble's lowering theme.
- `book/src/L1-L0/fe-space-construction-rotation.md` (`status: firm`) — fe_space's lowering theme.
- Template: `book/src/L1/set_subvector_zero.md:5-19` (rank+edges block-mapping form, lowers-to handling) and `book/src/L2/krylov-step.md:1-34` (from-scratch authoring + composes-list form).

## Open questions / caveats

- **OQ `fe_collection-own-constituents-future-pass`** — `L1/fe_collection` is now reachable (rescued by this
  pass) but its OWN frontmatter is still pre-scheme (`status: firm`, NO typed `edges:`). It is a near-leaf
  (the `ConstructFECollections` order schedule, `multigrid.hpp:22-73`) whose constituents are scalar config
  inputs (order/dim/coarsening policy) + a positive L0 cite — likely a leaf whose only `depends-on` is a
  `cites-evidence` to `palace/fem/multigrid.hpp:22-73`. A future P1 pass should migrate it to the scheme +
  add that L0 cite; until then it is reachable-but-untyped (edge-untyped detritus would NOT re-flag it since
  it is now reachable, but it counts toward the 60 untyped warning). NOT in this dispatch's 2-file scope.
- **OQ `fe_space-deferred-siblings-still-ungrounded`** — `fe_space.md` §Status :181-187 names three deferred
  follow-on siblings (`essential_dofs`, `fe_space_hierarchy`, and the de-Rham interpolator machinery) that
  are NOT yet authored as chapters. They are sibling-pull-gated future vocabulary, not current deps of
  `fe_space`, so correctly NOT edged here (faithful-edge-or-finding: declining a would-be over-edge to an
  unauthored sibling). Flagged for the FE-space-construction front's future fan-out, not this pass.
- **Frontmatter `variant_axes` list dropped** — the scheme's canonical frontmatter (per set_subvector_zero /
  krylov-step) carries no `variant_axes:` field; `fe_assemble`'s three axes live in the chapter body
  §Variant axes (:180-198), which is the authoritative home. The migration comment notes this so a reader
  doesn't read the drop as data loss. Same for `fe_space`'s `harvested_by`/`cycle` provenance — preserved
  (they are not scheme-conflicting), only the maturity token migrates `status: firm` → `rank: firm`.
- **No prose drift** — both migrations are frontmatter-only; no `## Status` line, signature, or body prose is
  touched, so the on-disk firm maturity is unchanged (the chapters were already firm; the migration only
  re-expresses firmness as `rank: firm` + types the edges).

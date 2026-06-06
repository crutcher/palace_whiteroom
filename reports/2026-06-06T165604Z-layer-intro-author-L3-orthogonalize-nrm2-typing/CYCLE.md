---
agent: layer-intro-author
invoked_at: 2026-06-06T165604Z
scope: graded-stack-lazy-tail-typing — typed edges: block (+ rank:) on L3/orthogonalize + L3/nrm2 (D1 LEAD, cycle-112 / batch-36 opener)
status: pending
integrated_at: 2026-06-06T173500Z
integration_commit: eddd7e6b891307e88a343c9062675140357d2535
integration_notes: "Applied clean (D1, batch-36 opener). Frontmatter-only typed rank:+edges: on L3/orthogonalize (rank: partial-obstruction, HELD GARBAGE per RE2) + L3/nrm2 (rank: firm). +1 reachable (faithful L3/nrm2 → L2/nrm2 RE5 transitive-grounding flip), −1 detritus. rank_violations HELD 0, unresolved HELD 0, untyped HELD 60. Build EXIT 0, no finalize build-repair. 3 OQs promoted to the batch-36 meta-phase (re2-shadows-orthogonalize-variant-split-theme, lazy-tail-untyped-no-decrement-for-legacy-edged-files, obstruction-resolution-firm-linter-keying-untested). Cumulative landed-tree linter: files=355, typed=295, untyped=60, roots=36, reachable=123, rank_violations=0, unresolved=0, detritus=136."
---

# CYCLE: L3 lazy-tail typed-edge migration — `orthogonalize` + `nrm2`

## Summary

Frontmatter-only graded-stack P1 lazy-tail typing. Two L3 mid-node chapters that carried only
**legacy** frontmatter (`layer:`/`operator:`/`firmness:`/`lifts_from:`/`lowers_to:`/`variant_axes:`)
are migrated to the batch-33-ratified typed surface: a top-level `rank:` token + a machine-readable
`edges:` block (block-mapping `- target:`/`kind:` form), preserving `variant_axes:`. No chapter
bodies rewritten; no new operator algebra.

- `book/src/L3/orthogonalize.md` → `rank: partial-obstruction` (+ `obstruction_resolution: firm`).
- `book/src/L3/nrm2.md` → `rank: firm`.

**Standalone linter delta (this dispatch's 2 files only, measured then reverted):**

| metric | baseline | after my 2 files | delta |
|---|---|---|---|
| files scanned | 355 | 355 | 0 |
| typed nodes | 295 | 295 | **HELD** (see Finding F1) |
| untyped (WARNING) | 60 | 60 | **HELD — NOT 60→58** (see Finding F1) |
| reachable from roots | 122 | **123** | **+1** (via the `L2/nrm2` flip; see F2) |
| rank_violations | 0 | 0 | **HELD 0** |
| detritus | 137 | 136 | −1 |
| `L3/orthogonalize` reachable? | no (GARBAGE) | **no (GARBAGE)** | **HELD — RE2 honored** ✓ |

Tree reverted to clean baseline after measurement (`reachable=122, detritus=137, rank_violations=0`)
so the integrator applies from the proposed-changes channel below onto a clean tree.

## Proposed changes

```edit:book/src/L3/orthogonalize.md
[old]:
---
layer: L3
operator: orthogonalize
firmness: partial-obstruction
lifts_from:
  - book/src/L2/orthogonalize.md (the named `project ▷ subtract` composition; the L2 per-variant batched/interleaved primitive sequence lifts to this L3 body, with the per-variant collective shape disclosed as the residual axis — see §"Lifts from"; the MGS interleaving is the obstruction, CGS/CGS2 lift)
lowers_to:
  - book/src/L2/orthogonalize.md (per-step `dot`+`axpy` body identity-in-form, annotated in-line per cycle-012; the SUBSTANTIVE loop-structure variant split — MGS `jloop`/CGS-batched-arm collapse into the L2 per-variant sequencing — is the dedicated `orthogonalize-variant-split` L3>L2 theme, cycle-044)
variant_axes:
[new]:
---
layer: L3
operator: orthogonalize
# Graded-stack scheme (authored from scratch, batch-36 c112 lazy-tail typing; migrates the legacy
# layer:/firmness:/lifts_from:/lowers_to:/variant_axes: frontmatter to a typed edges: block). This
# L3 entry is a `partial-obstruction` (rank: partial-obstruction): the per-step `dot`+`axpy` body
# lifts for all three variants AND the CGS/CGS2 loop lifts, but the MGS `j`-loop is a witnessed
# `sequential-obstruction` (§Status). The lifted body is firm (syntactic identities on the
# `orthog.hpp` source, inherited from the firm L1/L2 entries) → obstruction_resolution: firm.
# depends-on: the L2 named composition it lifts-from/lowers-to (`L2/orthogonalize`, firm, the
# `project ▷ subtract` surface — its legacy lifts_from AND lowers_to both name it); the two
# same-layer L3 body primitives the per-step body composes (`L3/dot`, `L3/axpy`, §Dependencies
# :366-374); and the dedicated substantive loop-structure lowering theme
# `L3-L2/orthogonalize-variant-split` (kind: lowers-to — the L3-op-points-at-its-theme rescue edge,
# mirroring the c111 L2/orthogonalize → L2-L1/orthogonalize-composition-lowering surface; this is the
# UPPER endpoint that makes the theme reachable per scheme §5 batch-34). reference: the cross-cutting
# concept pages + the transitive-identity L1 sibling + the two precedent partial-obstruction siblings.
# RE2 baseline-exception (ratified): typing this block is correct hygiene but does NOT flip
# `L3/orthogonalize` reachable — `L4/krylov-step` composes the L2 surface directly, not the L3
# iteration-view, so there is no faithful reachable inbound depender. No forced inbound edge added.
rank: partial-obstruction
obstruction_resolution: firm
edges:
  depends-on:
    - target: L2/orthogonalize
      kind: lowers-to             # the firm L2 `project ▷ subtract` composition; per-step body identity-in-form (legacy lifts_from + lowers_to both name it)
    - target: L3-L2/orthogonalize-variant-split
      kind: lowers-to             # the dedicated SUBSTANTIVE L3>L2 loop-structure variant-split theme (cycle-044); this op is its UPPER endpoint (scheme §5 rescue)
    - target: L3/dot
      kind: composes              # same-layer body primitive: the projection-coefficient inner product H_j = op.dot(w_eff(j), V[j])
    - target: L3/axpy
      kind: composes              # same-layer body primitive: the rank-1 residual update w − H_j·V[j] = axpy(-H_j, V[j], w)
  reference:
    - concepts/sequential-obstruction
    - concepts/tensor-field-lift
    - concepts/variant-absorption
    - concepts/orthogonalization
    - L1/orthogonalize
    - L3/chebyshev
    - L3/eigsolve
variant_axes:
```

```edit:book/src/L3/nrm2.md
[old]:
---
layer: L3
operator: nrm2
firmness: firm
lowers_to:
  - book/src/L1/nrm2.md (identity-in-form on the primitive's signature; no L3-L1 theme — see Lowers-to)
lifts_from:
  - book/src/L4/nrm2.md (firm cycle-069 D2 — the L4 Euclidean-norm verb `nrm2(r)`; the kept named abstraction risen to L4 as a named CONSUMER verb of the `inner_product` combinator at the diagonal `y = x` (`√ ∘ abs ∘ inner_product`), NOT a fold member — the do-NOT-merge guard; `concepts/black-box-vs-accelerated-kernels.md` §2; identity-in-form on the body — value-thread-isomorphic, no dedicated L4>L3 theme, the in-line-marker route)
variant_axes:
[new]:
---
layer: L3
operator: nrm2
# Graded-stack scheme (authored from scratch, batch-36 c112 lazy-tail typing; migrates the legacy
# layer:/firmness:/lowers_to:/lifts_from:/variant_axes: frontmatter to a typed edges: block). This
# L3 entry is a firm consumer-stub (rank: firm; §Status): `nrm2` at L3 is a CONSUMER of the
# inner-product fold (`nrm2(x) = √dot(x, x)`), NOT a fold member (the do-NOT-merge carve-out
# preserved). Its laws are syntactic identities inherited from the firm L1 leaf → firm rests on firm.
# depends-on: the firm L1 leaf it lowers to as identity-in-form (`L1/nrm2`, its legacy lowers_to);
# the adjacent firm L2 consumer-stub it lowers to (`L2/nrm2`, §"Downward to L2", identity-in-form);
# and the same-layer L3 reduce-anchor its defining identity `√dot(x, x)` composes (`L3/dot`, firm,
# §Evidence "the L3 dependency anchor"). All three are firm → rank invariant holds firm→firm.
# reference: the L4 verb it lifts to (`L4/nrm2`, its legacy lifts_from); the inner-product combinator
# it consumes-but-is-NOT-a-member-of (`L2/inner_product` — kept as a navigational reference to honor
# the do-NOT-merge carve-out, the operator→next-layer depends-on being `L2/nrm2`); the concept page.
# This block does NOT force a reachability flip; `L3/nrm2` is already reachable inbound via
# `L3/normalize` + `L4/nrm2` (pre-existing, unchanged).
rank: firm
edges:
  depends-on:
    - target: L1/nrm2
      kind: lowers-to             # the firm L1 leaf; identity-in-form on the primitive's signature, no L3-L1 theme (legacy lowers_to)
    - target: L2/nrm2
      kind: lowers-to             # the adjacent firm L2 consumer-stub; identity-in-form (§"Downward to L2", no theme file)
    - target: L3/dot
      kind: composes              # same-layer reduce-anchor: the defining identity nrm2(x) = √dot(x, x) is L3-internal (§Evidence)
  reference:
    - L4/nrm2
    - L2/inner_product
    - concepts/nrm2
variant_axes:
```

## Faithful-edge derivation (per file, with prose citations)

### `L3/orthogonalize.md` — `rank: partial-obstruction` + `obstruction_resolution: firm`

- **`rank: partial-obstruction`** — directly from `## Status` (`:448`): "`partial-obstruction` —
  the per-step body … lifts cleanly … but the MGS `j`-loop is a witnessed `sequential-obstruction`".
  Per scheme §1 the on-disk `partial-obstruction` maps to `rank: partial-obstruction` (a separate
  kind). `obstruction_resolution: firm` because §Status states the body's algebraic laws are
  "syntactic identities on fully-specified C++ source … inherited from the cycle-012 firm L1/L2
  entries" — i.e. the lifted body is firm. Scheme §1 prescribes `obstruction_resolution` for the
  lifted-body resolution of a `partial-obstruction`.

- **`depends-on: L2/orthogonalize` (kind: lowers-to)** — the legacy `lifts_from:` AND `lowers_to:`
  BOTH name `book/src/L2/orthogonalize.md`; the body §"Downward to L2" (`:80-92`) and §Dependencies
  "Adjacent-layer siblings" (`:394-396`) state the per-step body is identity-in-form to the firm L2
  `project ▷ subtract` composition. `L2/orthogonalize` is `rank: firm` on disk (verified). The
  lowering edge is `depends-on` on the L_n endpoint (scheme §2/§5). `kind: lowers-to` documents it.

- **`depends-on: L3-L2/orthogonalize-variant-split` (kind: lowers-to)** — the legacy `lowers_to:`
  names the `orthogonalize-variant-split` theme in prose, and §"Downward to L2"/§"L3 vs L2
  distinction" (`:411-414`, `:489-492`) state the SUBSTANTIVE loop-structure variant split is the
  "dedicated `orthogonalize-variant-split` L3>L2 theme (cycle-044, the first substantive — non-identity
  — `L3-L2/` theme)". This is the L3-op-points-at-its-theme **rescue** edge (scheme §5 batch-34
  clarification: the theme is reachable only iff its UPPER-endpoint op carries a `lowers-to`
  `depends-on` at it), mirroring the c111 `L2/orthogonalize → L2-L1/orthogonalize-composition-lowering`
  and c109 `L2/krylov-step → L2-L1/krylov-step-kernel-defusion` surfaces. **The brief asked me to
  verify the right surface vs the `L3/dot` template** — `L3/dot` points operator→operator only and
  does NOT carry a theme edge (the `dot-body-identity` theme was DEMOTED into the combinator, so it
  has no live theme to rescue). `orthogonalize` is the opposite case: it HAS a live, substantive,
  non-demoted `L3-L2/` theme that exists as a real file and is currently detritus — so the
  `L2/orthogonalize`/`krylov-step` from-scratch-author surface (theme as a `lowers-to depends-on`)
  is the correct precedent here, NOT the `L3/dot` no-theme surface. (Measured consequence: this edge
  does NOT rescue the theme this cycle — see Finding F3 — because `L3/orthogonalize` is itself
  unreachable per RE2, so the rescue is structurally-correct-but-currently-latent. Recorded as an OQ.)

- **`depends-on: L3/dot`, `L3/axpy` (kind: composes)** — §Dependencies "Same-layer (L3)" (`:366-374`):
  "the per-step body references the L3-native whole-tensor primitives … [`dot`] … the
  projection-coefficient inner product `H_j = op.dot(...)` … [`axpy`] … the rank-1 residual update
  `w − H_j·V[j]` = `axpy(-H_j, V[j], w)`". These `composes` edges are grounded in orthogonalize's OWN
  §Dependencies "Same-layer (L3)" (`:366-374`) naming `dot`+`axpy` as body primitives — the body-primitive
  convention itself is the precedent, NOT a `L3/dot` template (on disk `L3/dot.md` carries no same-layer
  `depends-on`; its only `depends-on` is the next-layer `L2/inner_product`, so it is not a same-layer-op
  precedent). `L3/dot` is `rank: firm`; `L3/axpy` is `firmness: firm` (typed-no-rank → vacuous in the
  rank check). The §Dependencies explicit non-dependencies `nrm2`/`scal` (caller's normalisation,
  `:376-379`) are correctly EXCLUDED — faithful to "they are not dependencies of this operator".

- **`reference:`** — the body's cross-cutting concept links (`concepts/sequential-obstruction`,
  `concepts/tensor-field-lift`, `concepts/variant-absorption`, `concepts/orthogonalization`,
  §Dependencies `:381-390`), the transitive-identity L1 sibling (`L1/orthogonalize` — navigational,
  per the in-line non-adjacent-identity convention, NOT a blocking dep), and the two precedent
  partial-obstruction siblings (`L3/chebyshev`, `L3/eigsolve`, §Context `:50-57`). All `reference`
  (navigational); none constrains rank or carries liveness.

### `L3/nrm2.md` — `rank: firm`

- **`rank: firm`** — `## Status` (`:73`): "`firm` — consumer-stub". Maps to `rank: firm` (scheme §1).

- **`depends-on: L1/nrm2` (kind: lowers-to)** — the legacy `lowers_to:` names `book/src/L1/nrm2.md`;
  §"Lowers to" (`:85`): "L3 `nrm2` lowers to L1 [`nrm2`] as identity-in-form on the primitive's
  signature." `L1/nrm2` is `rank: firm`.

- **`depends-on: L2/nrm2` (kind: lowers-to)** — §"Downward to L2" (`:98`): "L3 `nrm2` lowers to L2
  [`nrm2`] as identity-in-form on the primitive's signature." `L2/nrm2` is `rank: firm`. This is the
  adjacent operator→next-operator lowering (the `L3/dot → L2/inner_product` analogue: `L3/dot` points
  at its adjacent L2 surface; `L3/nrm2`'s adjacent L2 surface is `L2/nrm2`). **This edge is the
  faithful rescue of `L2/nrm2`** (Finding F2): it is a genuine adjacent-layer dependency, so the
  reachability flip is a faithful GROUND, not a forced edge.

- **`depends-on: L3/dot` (kind: composes)** — §Evidence (`:173-174`): "[`L3/dot`] (firm cycle-011) —
  the L3 dependency anchor; the defining identity `nrm2(x) = √dot(x, x)` is L3-internal." §Signature
  (`:34`): `nrm2(x) = √⟨x, x⟩ = √dot(x, x)`. `L3/dot` is `rank: firm`. Same-layer reduce-anchor.

- **`reference:`** — `L4/nrm2` (the legacy `lifts_from:`; the L4 verb it lifts to — navigational,
  upward), `L2/inner_product` (the fold it CONSUMES-but-is-NOT-a-member-of: the do-NOT-merge
  carve-out is explicit at §Status `:73-75` and §"Downward to L2" `:103-110`; kept as `reference`
  rather than `depends-on` precisely to honor the carve-out — the blocking operator→next dependency
  is `L2/nrm2`, and the diagonal-consume goes through the same-layer `L3/dot`), and `concepts/nrm2`
  (the cross-cutting concept page, §Evidence `:188`). All `reference`; do-NOT-merge preserved.

## Findings (for the batch-36 meta-phase)

**F1 — `untyped` HOLDS at 60, NOT 60→58 as the brief expected (the brief's premise is off for
these two files).** Both `L3/orthogonalize` and `L3/nrm2` carried legacy `lowers_to:`/`lifts_from:`
frontmatter, which `graded_stack_lint.py` (lines 525-531) **migrates to `depends-on` edges**. The
`untyped` flag is `rank is None AND not read_any_edge`; with legacy edges present, `read_any_edge` is
True, so both files were already counted as **typed-by-legacy-edge** (`rank=None`, NOT in the
untyped-60). The untyped-60 are all genuinely edge-less files (L0 file-overviews, `meta-reviews/*`,
`methodology/*`, `SUMMARY`, `design/*`, `introduction`). **Consequence for the campaign:** the
lazy-tail "untyped → typed" framing does not apply to L3 mid-nodes that already had legacy
`lowers_to`/`lifts_from`; the real value of typing them is (i) adding the `rank:` token (so they
enter the rank histogram / rank-violation check — `partial-obstruction` count 3→4 in the histogram),
and (ii) replacing the lossy auto-migrated edge set with a deliberately-classified `depends-on` vs
`reference` split. The campaign tracker / D2 prompt should expect `untyped` to HOLD (not decrement)
for any lazy-tail file whose legacy frontmatter already carried `lowers_to`/`lifts_from`/`depends_on`.
If the batch-36 baseline `untyped=60` was predicated on these decrementing, re-baseline accordingly.

**F2 — the measurable rescue is `L2/nrm2` (reachable 122→123, detritus 137→136), NOT a
self-flip.** My `L3/nrm2 → L2/nrm2 (depends-on, lowers-to)` edge makes the already-reachable
`L3/nrm2` (reachable inbound via `L3/normalize` + `L4/nrm2`) point at `L2/nrm2`, which was previously
unreachable (nothing reachable pointed at it). This is a faithful GROUND of a genuine adjacent-layer
dependency (§"Downward to L2"), exactly the disposition-(1) GROUND-don't-remove pattern. It is
honest, citation-grounded, and measurable. Neither `L3/nrm2` nor `L3/orthogonalize` self-flips.

**F3 — `L3-L2/orthogonalize-variant-split` is NOT rescued this cycle, by RE2 design (latent
rescue).** My `L3/orthogonalize → L3-L2/orthogonalize-variant-split (lowers-to)` edge is the
structurally-correct UPPER-endpoint rescue surface (scheme §5), but `L3-L2/orthogonalize-variant-split`
stays `[garbage?]` because its only inbound is from `L3/orthogonalize`, which is itself unreachable
under the **ratified RE2 baseline-exception** (`L4/krylov-step` composes the L2 surface directly, not
the L3 iteration-view, so `L3/orthogonalize` has no faithful reachable inbound depender). The edge is
correct and latent: it will rescue the theme automatically IF/WHEN RE2 is ever lifted (i.e. if a
faithful reachable consumer of the L3 iteration-view of `orthogonalize` is ever authored — e.g. a
firm `L4/orthogonalize` Arnoldi-step-monad surface, currently unauthored per §Open-questions). I did
NOT add a forced inbound edge to flip `L3/orthogonalize` (RE2 forbids it). **This means
`L3-L2/orthogonalize-variant-split` is a genuine RE2-shadowed detritus node** — it shares the
`L3/orthogonalize` unreachability for the same reason. Recommend the batch-36 meta-phase note it
under the RE2 cluster (the theme rides RE2; do NOT separately delete it or force-edge it).

## Open questions / caveats

- **OQ `re2-shadows-orthogonalize-variant-split-theme`** — `L3-L2/orthogonalize-variant-split` is
  detritus for the SAME reason `L3/orthogonalize` is (RE2: no faithful reachable consumer of the L3
  iteration-view). The UPPER-endpoint `lowers-to` rescue edge is now in place (latent). Disposition:
  rides the RE2 cluster; rescued automatically when/if a firm `L4/orthogonalize` lands. Not a delete,
  not a force-edge — a documented RE2-shadowed node. (Flagging per the GROUND-don't-remove priority
  order: this is disposition (1)-attempted-but-blocked-by-ratified-exception, NOT (2) detritus.)
- **OQ `lazy-tail-untyped-no-decrement-for-legacy-edged-files`** (= Finding F1) — re-baseline the
  campaign's `untyped` expectation for lazy-tail files that already carried `lowers_to`/`lifts_from`.
- **`obstruction_resolution` on `partial-obstruction` — confirm the linter reads it.** I wrote
  `obstruction_resolution: firm` per scheme §1. The linter's `rank histogram` shows
  `partial-obstruction: 4` (was 3 before my edit), confirming the `rank:` token is consumed; I did
  not separately verify the linter keys off `obstruction_resolution` for the downstream-satisfaction
  rule (no `firm` consumer currently `depends-on` `L3/orthogonalize`, so the path is untested here).
  Faithful to the scheme regardless; flagging for the rank-linter maintainer.
- **Scope discipline:** frontmatter-only, no body edits, no new algebra (per the brief). The
  `variant_axes:` block is preserved verbatim on both files (it sits AFTER the `edges:` block in the
  proposed new frontmatter). No index/dep-map table edits (those are derived views, not my scope this
  dispatch; D2 owns no shared index this cycle either — disjoint file sets).

## Supporting evidence

- Linter: `tools/graded-stack-lint/graded_stack_lint.py` — baseline `files=355, typed=295,
  untyped=60, reachable=122, rank_violations=0, detritus=137`; after my 2 files (standalone, then
  reverted) `typed=295, untyped=60, reachable=123, rank_violations=0, detritus=136`;
  `L3/orthogonalize` HELD GARBAGE (RE2 ✓), `L2/nrm2` flipped reachable (the +1).
- Templates mirrored: `book/src/L3/dot.md` (the already-typed L3 sibling — operator→next-layer
  `depends-on` + `reference` surface), `book/src/L2/krylov-step.md` (c109 from-scratch block-mapping
  template), `book/src/L2/orthogonalize.md` (c111 — the theme-as-`lowers-to`-`depends-on` rescue
  precedent), `book/src/L2/nrm2.md` (the adjacent L2 consumer-stub edge surface).
- Scheme: `book/src/methodology/graded-stack-scheme.md` §1 (rank token + obstruction sub-field),
  §2 (typed `edges:` block-mapping form), §5 (lowering-theme reachability via UPPER-endpoint
  `lowers-to` edge; navigational vs node encoding).
- Chapter prose citations: as enumerated per-file above (`book/src/L3/orthogonalize.md` §Status,
  §Dependencies, §"Downward to L2"; `book/src/L3/nrm2.md` §Status, §Signature, §"Lowers to",
  §"Downward to L2", §Evidence).

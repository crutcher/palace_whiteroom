---
agent: layer-intro-author
invoked_at: 2026-06-06T17:03:26Z
scope: L3 typed-edge frontmatter migration — scal + linear_combination (graded-stack P1 lazy-tail, batch-36 D2)
status: pending
integrated_at: 2026-06-06T173500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (D2, batch-36). Frontmatter-only typed rank: firm + edges: (bare-slug surface mirroring L3/dot) on L3/scal + L3/linear_combination. ZERO standalone delta — both files carried legacy lowers_to/lifts_from, shim-counted typed before the edit, so untyped HELD (representation upgrade legacy→canonical edges:, not a typed-count change; cross-cutting signal F1). rank_violations HELD 0 (firm-rests-on-firm: both rest on L2/linear_combination firm), unresolved HELD 0. Build EXIT 0, no finalize build-repair. 2 OQs promoted to the batch-36 meta-phase (L3-scal-reachable-via-normalize-grounding, linter-legacy-shim-line-citation-527-532-not-546-547)."
---

# CYCLE: L3 scal + linear_combination typed-edge migration

## Summary

This is dispatch D2 of cycle-112 (batch-36 opener), the `graded-stack-lazy-tail-typing`
LEAD applied to the disjoint `linear_combination`-family L3 mid-node pair. It migrates
two L3 chapters off legacy frontmatter (`firmness:`/`lowers_to:`/`lifts_from:`) onto the
batch-33-ratified graded-stack scheme: a `rank:` token + a typed `edges:` block with
`depends-on:` (blocking) and `reference:` (navigational) lists. **Frontmatter-only** —
no body rewrite, no new operator algebra.

- `book/src/L3/scal.md` — `firmness: firm` → `rank: firm`; `lowers_to`→`depends-on: [L2/linear_combination]`; `lifts_from` + theme → `reference`.
- `book/src/L3/linear_combination.md` — `firmness: firm` → `rank: firm`; `lowers_to`→`depends-on: [L2/linear_combination]`; `lifts_from` + theme → `reference`.

Both mirror the already-typed sibling `book/src/L3/dot.md` surface form exactly: a bare-slug
`depends-on` list (no `kind:` qualifier — `L3/dot` does not use the block-mapping form for its
single L2-op edge) and a bare-slug `reference` list.

## Surface-form decision (mirrors L3/dot, not L2/krylov-step)

`L3/dot` (the typed L3 sibling) uses **bare slugs** in `depends-on` (`- L2/inner_product`)
and `reference` (`- L4/dot`) — NO `{target:, kind:}` block-mapping, NO `kind:` qualifiers.
The task instruction says to follow whatever surface form `L3/dot` uses, and the
operator→operator `lowers-to` convention at the L3 level treats the lowering THEME as a
`reference` target (not a `depends-on lowers-to`). I therefore use the bare-slug form
throughout for both files. (The `{target:, kind: lowers-to}` block-mapping form in
`L2/krylov-step` is reserved there for the L2>L1 *theme* edge it pulls into `depends-on`;
at L3 the lowering theme is a `reference`, so no block-mapping is needed here.)

## Proposed changes

```edit:book/src/L3/scal.md
[old]:
---
layer: L3
operator: scal
firmness: firm
lowers_to:
  - book/src/L2/linear_combination.md (the arity-1 specialization of the firm L3/L2 `linear_combination` fold; `scal(α,x) = linear_combination [(α,x)]`; lowers via the combinator's §"Downward to L2" identity-in-form edge, then the substantive arity-dispatch is the L2>L1 `linear-combination-fold-specialization` theme) → book/src/L1/scal.md (transitive L3>L1 identity in-line; no `L3-L1/` directory)
lifts_from:
  - book/src/L3/linear_combination.md (the family combinator this leaf is the arity-1 specialization of — `scal` speaks through `linear_combination`, not as a re-derived base form, per the 2026-06-01 vocabulary-shift redirect)
variant_axes:
  - element-type (real / complex)
  - scalar-promotion (real-α-against-complex-x via concepts/scalar-promotion)
---
[new]:
---
layer: L3
operator: scal
rank: firm
edges:
  depends-on:
    - L2/linear_combination
  reference:
    - L3/linear_combination
    - L1/scal
    - L2-L1/linear-combination-fold-specialization
variant_axes:
  - element-type (real / complex)
  - scalar-promotion (real-α-against-complex-x via concepts/scalar-promotion)
---
```

```edit:book/src/L3/linear_combination.md
[old]:
---
layer: L3
operator: linear_combination
firmness: firm
lowers_to:
  - book/src/L2/linear_combination.md (the firm L2 fold combinator, cycle-018 / inverted-to-entry cycle-049 D1; identity-in-form across the L3>L2 edge — the L3 whole-tensor fold is value-thread-isomorphic to the L2 fold; see §"Downward to L2") → book/src/L1/{scal,axpy,axpby,axpbypcz}.md (the family members recovered as list-length specializations; substantive rotation is the L2>L1 `linear-combination-fold-specialization` fusion-selection theme)
lifts_from:
  - book/src/L4/linear_combination.md (firm cycle-068; identity-in-form on the body — the L4 calculus combinator is value-thread-isomorphic to this L3 fold, NO dedicated L4>L3 theme file, the eigsolve/chebyshev in-line-marker route — there is no monadic state-threading / Solve-monad / convergence predicate to dissolve across the L4>L3 edge)
variant_axes:
[new]:
---
layer: L3
operator: linear_combination
rank: firm
edges:
  depends-on:
    - L2/linear_combination
  reference:
    - L4/linear_combination
    - L2-L1/linear-combination-fold-specialization
variant_axes:
```

## Faithful-edge derivation (per file, from the chapter's OWN prose + legacy fields)

### `L3/scal.md`

- **`rank: firm`** ← legacy `firmness: firm`, confirmed by the on-disk `## Status` line
  (`scal.md:36`: "`firm` — `scal` is the arity-1 specialization of the firm L3 combinator…").
- **`depends-on: L2/linear_combination`** ← legacy `lowers_to` names exactly the arity-1
  specialization. Prose witnesses:
  - frontmatter `lowers_to: book/src/L2/linear_combination.md` "(the arity-1 specialization …; `scal(α,x) = linear_combination [(α,x)]`…)".
  - body intro (`scal.md:16`): "scal(α, x) = linear_combination [(α, x)]".
  - §Specialization (`scal.md:22`): "routes through the combinator's §\"Downward to L2\" identity edge (`L3/linear_combination.md:107-113`), read at length 1".
  The L3 op lowers to the **L2 op** `linear_combination` — operator→operator. The target
  `L2/linear_combination` is `rank: firm` (`L2/linear_combination.md:4`), so the
  well-foundedness invariant `rank(scal=firm) ≤ rank(L2/linear_combination=firm)` holds.
- **`reference: L3/linear_combination`** ← legacy `lifts_from` (the family combinator this leaf
  is the arity-1 specialization of; `scal.md:8`, body `scal.md:16,20,24`). Per the established
  L3 convention (`L3/dot` puts its `lifts_from` family/up-edge under `reference`, not depends-on),
  this is a navigational `reference`.
- **`reference: L1/scal`** ← the transitive L3>L1 identity endpoint named in the legacy
  `lowers_to` tail and in §Status (`scal.md:36`: "firm L1 endpoint `book/src/L1/scal.md`").
  A non-adjacent (L3→L1) navigational pointer (in-line per the cycle-012 non-adjacent-identity
  convention) — `reference`, not `depends-on` (the adjacent blocking edge is the L2 one).
- **`reference: L2-L1/linear-combination-fold-specialization`** ← the substantive arity-dispatch
  lowering THEME (`scal.md:22`). Per the operator→operator convention at L3, the lowering theme is
  a `reference` target (not a `depends-on lowers-to` here) — the blocking `depends-on` is the L2 op,
  the theme is the navigational pointer to where the substantive de-fusion lives.

### `L3/linear_combination.md`

- **`rank: firm`** ← legacy `firmness: firm`, confirmed by on-disk §Status
  (`linear_combination.md:152`: "`firm` — the L3 whole-tensor variadic-fold signature is canonical at L3…").
- **`depends-on: L2/linear_combination`** ← legacy `lowers_to` (the firm L2 fold combinator,
  cycle-018 / inverted-c049; identity-in-form across the L3>L2 edge). Prose witnesses:
  - frontmatter `lowers_to` line.
  - §"Downward to L2" (`linear_combination.md:108-110`): "The L3 `linear_combination` fold lowers
    to the firm L2 `linear_combination` as **identity-in-form on the combinator's body**".
  - §Dependencies "Upward (L2)" (`linear_combination.md:125`): "the firm L2 `linear_combination`
    combinator … the body this L3 entry is value-thread-isomorphic to".
  Target `L2/linear_combination` is `rank: firm`; invariant holds firm/firm.
- **`reference: L4/linear_combination`** ← legacy `lifts_from` (firm c068; identity-in-form lift,
  no dedicated L4>L3 theme — the in-line-marker route). `linear_combination.md:154-156` §"Lifts from".
  An up-edge → `reference` per the L3/dot convention.
- **`reference: L2-L1/linear-combination-fold-specialization`** ← the substantive L2>L1
  fusion-selection theme (`linear_combination.md:113-114` §"Downward to L2"; §Evidence
  `linear_combination.md:167`). The operator→operator depends-on goes to the L2 op; the theme is
  the navigational `reference`.

### Edges deliberately NOT manufactured (faithful-edge-or-finding)

- I did **NOT** add `depends-on` edges to `L1/scal` / `L1/{scal,axpy,axpby,axpbypcz}` for the
  transitive L3>L1 tails. The legacy `lowers_to` arrows tail to L1 (`… → book/src/L1/…`), but the
  *adjacent blocking* edge at L3 is the L2 op; the L1 endpoints are non-adjacent in-line identity
  references (cycle-012 convention — no `L3-L1/` directory), so they are `reference`, not
  `depends-on`. Forcing an L3→L1 `depends-on` would over-link past the adjacent L2 layer.
- I did **NOT** add a `depends-on … kind: lowers-to` edge to the lowering THEME. At L3 the
  operator→operator convention (confirmed against `L3/dot`, which routes its single op edge to the
  L2 op and reserves no theme edge) makes the theme a `reference`. The block-mapping
  `kind: lowers-to` depends-on form is the L2/krylov-step pattern for pulling an L2>L1 theme into
  depends-on; it is not the L3-leaf pattern.

## Standalone linter delta (measured; reverted to clean tree after)

Method: applied both edits, ran `graded_stack_lint.py --json` / `--show-inbound`, then
`git checkout` reverted both files to leave a clean tree for the integrator (per the
parallel-dispatch measurement-contamination discipline — D1 runs disjoint on
`L3/orthogonalize`+`L3/nrm2`; the authoritative cumulative is the finalize step-5b re-measure).

**Baseline (clean landed tree):** `files=355, typed=295, untyped=60, roots=36, reachable=122, rank_violations=0, unresolved=0`.

**Post-edit (my 2 files only):** `files=355, typed=295, untyped=60, roots=36, reachable=122, rank_violations=0, unresolved=0`.

**My standalone delta: ZERO on every total.** `rank_violations` HOLDS 0; `unresolved` HOLDS 0.

### Finding — the `untyped 60→58` expectation does NOT hold for these two files (representation-upgrade, not typed-count change)

The task expected `untyped 60→58`. It does **not** materialize, and this is correct/expected
once the linter's behavior is examined — **not** a defect in my edit:

- The linter (`graded_stack_lint.py:518-547`) carries a **legacy-frontmatter migration shim**:
  it maps `lowers_to`/`lifts_from`/`lifts_to`/`consumes` to `depends-on` edges, and explicitly
  "their presence counts as 'typed' for the untyped flag" (`:546-547`). The `untyped` flag is
  `rank is None AND no edge read` (`:551`).
- Both `L3/scal` and `L3/linear_combination` carried legacy `lowers_to:` + `lifts_from:` fields,
  so they were **already counted as typed** (NOT in the `untyped` set) before my edit. I verified
  this directly via `--json`: `'L3/scal' in untyped == False` and
  `'L3/linear_combination' in untyped == False` both pre- AND post-edit; `untyped` stayed 60.
- The value of this migration is therefore **representation hygiene** — converting the legacy
  `lowers_to`/`lifts_from` prose-fields into the batch-33-ratified canonical `edges:` block +
  explicit `rank:` token (the scheme the two graded-stack linters and downstream tooling key off),
  shedding the legacy-shim dependence — NOT a typed-count delta. The lazy-tail campaign's
  `untyped→0` goal is served by the *files that have NO frontmatter edges at all*; these two had
  legacy edges, so they were the shim's silent passengers, now made explicit.

This is consistent with the task's own framing ("FROM SCRATCH" was the expected case for files
"that currently carry only LEGACY frontmatter"); the subtlety is that the linter's shim already
absorbed legacy frontmatter as typed, so the *count* doesn't move even though the *representation*
is genuinely upgraded.

### Reachability observation (`--show-inbound`) — do NOT force-flip

Per `--show-inbound` (post-edit, identical to pre-edit since reachability flows over depends-on
FROM roots and I added no inbound edge):

- `L3/linear_combination` is **reachable** (NOT in detritus) — it is reached via
  `L4/linear_combination` (which traces to a feature root). Inbound:
  `L3/{axpby,axpbypcz,axpy}, L4/linear_combination`.
- `L3/scal` is **still detritus** (`[GARBAGE*]`). Its only inbound is `L3/normalize`, itself
  unreachable. I did **NOT** manufacture an inbound edge to force the flip (per task discipline).
  This is a GROUND-candidate for a future pass (see Open questions) — the faithful disposition is
  to ground it via a reachable consumer's `depends-on`, not to delete it or fake an inbound edge.

## Supporting evidence

- Template mirrored: `book/src/L3/dot.md:1-13` (bare-slug `depends-on` + `reference`, `rank:` token);
  `book/src/L2/krylov-step.md:1-25` (the c109 block-mapping template — consulted, not copied, since
  the L3-leaf surface form is `L3/dot`'s bare-slug form).
- Scheme: `tools/graded-stack-lint/graded_stack_lint.py:501-557` (edges parse + legacy migration shim
  + untyped flag definition).
- `L3/scal.md` prose: `:6,8,16,20,22,24,36` (lowering identity, family-combinator up-edge, status).
- `L3/linear_combination.md` prose: `:108-114,125,152,154-156,167` (downward-to-L2 identity,
  upward L2 dependency, status, lifts-from L4, fusion-selection theme).
- `L2/linear_combination.md:4` — target `rank: firm` (well-foundedness anchor).

## Open questions / caveats

- **`untyped 60→58` task expectation mismatch (resolved as finding above).** These two files were
  never in the `untyped` set — the linter's legacy-frontmatter shim already counted `lowers_to`/
  `lifts_from` as typed edges. The migration is a representation upgrade (legacy → canonical
  `edges:`), not a count change. Recommend the finalize step-5b cumulative re-measure expect
  `untyped` UNCHANGED for this dispatch's contribution, and that future lazy-tail dispatch scopes
  distinguish "files with NO frontmatter edges" (which move the count) from "files with legacy
  frontmatter edges" (which are representation-only).
- **`L3/scal` remains detritus — GROUND-candidate, not deleted/forced (out of scope here).**
  `L3/scal`'s only inbound is the unreachable `L3/normalize`. Under the GROUND-don't-remove
  directive (METHODOLOGY-GRADED-STACK §2f), the faithful disposition is to ground `L3/normalize`
  (or `L3/scal`) into a reachable chain via a real consumer's `depends-on` — e.g. whichever
  reachable op composes `normalize`/`scal`. This is beyond the frontmatter-only scope of these 2
  files (it requires typing an *upstream* consumer's edge). Flagging for a future grounding pass:
  `L3-scal-reachable-via-normalize-grounding`. Note `L3/normalize` is itself in D1's adjacent
  family but not in D1's named file set (`L3/orthogonalize`+`L3/nrm2`), so neither this dispatch
  nor D1 grounds it this cycle.
- **No record-definition gaps surfaced** — both chapters are operator entries naming only
  scalars/tensors (no signature-named record needing a definition home).

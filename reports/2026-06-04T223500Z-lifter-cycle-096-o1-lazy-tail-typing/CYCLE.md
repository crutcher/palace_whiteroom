---
agent: lifter
invoked_at: 2026-06-04T22:35:00Z
scope: L4>L3 theme re-anchor — solve-family-map-dissolution (O1 lazy-tail edge-typing)
status: integrated
integrated_at: 2026-06-05T001500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Applied clean (D3, cycle-096 batch-30 position 3/3). Typed book/src/L4-L3/solve-family-map-dissolution.md (had NO frontmatter) with rank: firm + typed edges depends-on [L4/solve_family, L4/ksp_solve, L4-L3/ksp-solve-driver-dissolution, L3/ksp_solve] + 6 reference edges. Pure edge-typing, no body/maturity change. rank-gate PASS (all 4 depends-on endpoints firm on disk). citecheck 9 ok / 0 failing. DISCHARGES O1 (baseline-exceptions TRACKED-OPEN-1) by construction -> rank_violations 1->0 on the landed state. Build clean.
inputs:
  - book/src/L4-L3/solve-family-map-dissolution.md
  - book/src/L4/solve_family.md
  - book/src/L4/ksp_solve.md
  - book/src/L4-L3/ksp-solve-driver-dissolution.md
  - book/src/L3/ksp_solve.md
  - scaffolding/graded-stack-baseline-exceptions.md
  - book/src/methodology/graded-stack-scheme.md
---

# CYCLE: Re-anchor solve-family-map-dissolution (O1 lazy-tail typing)

## Summary

Cycle-096 D3, GRADED-STACK campaign. This is **pure edge-typing**, not a maturity re-judgment:
the lone residual rank violation **O1** (`L4/solve_family → L4-L3/solve-family-map-dissolution`,
linter-reported `dep_rank = rough-in (test-coverage-bounded)`) is a `read_status_line` blob-scan
**false positive** — the theme's §Status (`book/src/L4-L3/solve-family-map-dissolution.md:185`)
**leads with** `` `firm` — on the **structural rotation** ``, but its line-187 "(former) inherited
... `rough-in (test-coverage-bounded)`" provenance caveat trips the linter's
resolution-priority blob scan (the bug documented in the baseline-exceptions ledger §Context).
The theme carries **no** `rank:`/`edges:` frontmatter (the file begins directly at the `# heading`),
so it is on the buggy prose fallback. The fix is the campaign's prescribed remedy: add a typed
`rank: firm` token (which `derive_rank` prioritizes over the prose fallback, bypassing the scan)
plus a typed `edges:` block declaring the lowering edges. All endpoints are **firm on disk**
(verified this dispatch), so the typed `rank: firm` satisfies the rank invariant
(`rank(u) ≤ min over depends-on`) immediately and clears O1 by construction — the linter's
`rank_violations` goes **1 → 0**. No §Status prose change, no LHS/RHS body change, no maturity
re-judgment.

## Endpoint firmness verification (self-verified on disk this dispatch)

| dep slug | file:line | §Status leading token |
|---|---|---|
| `L4/solve_family` | `book/src/L4/solve_family.md:144` | `firm` (c086 firm-on-positive-structure escape) |
| `L4/ksp_solve` | `book/src/L4/ksp_solve.md:160` | `firm` (c048) |
| `L4-L3/ksp-solve-driver-dissolution` | `book/src/L4-L3/ksp-solve-driver-dissolution.md:193` | `firm` (c048) |
| `L3/ksp_solve` | `book/src/L3/ksp_solve.md:167` | `firm` (c020) |

All four resolve to real files (slug-to-`book/src/<slug>.md` convention, confirmed against the
linter's `unresolved_depends_on_targets` list — none of these four appears there). Firm-on-firm
holds for every declared `depends-on` edge.

**Pre-typing linter state (this dispatch's on-disk read):**
```
rank_violations = [ { src: L4/solve_family, src_rank: firm,
                      dep: L4-L3/solve-family-map-dissolution,
                      dep_rank: rough-in (test-coverage-bounded) } ]   # the lone O1
```

## Edge classification (deliberate, per scheme §2 / §5)

Per `graded-stack-scheme.md` §5, a lowering theme's edge is a **`depends-on` on BOTH endpoints**
(the L_{n+1} source entry and the L_n target entry); its rank is validated as
`rank(theme) ≤ min(endpoints)`. Classification:

- **`L4/solve_family`** — the L4 source endpoint (the LHS combinator this theme dissolves).
  Cited as the theme's primary §"Verified-against" L4 source. **`depends-on`** (lowering source endpoint).
- **`L4/ksp_solve`** — the cap the `map` runs; the theme's per-member solve and the whole map-shell
  rest on it (§"L4 form (LHS)" / §"Verified-against"). **`depends-on`**.
- **`L4-L3/ksp-solve-driver-dissolution`** — the sibling per-member-solve theme this theme
  "**composes strictly above**" (it delegates each `ksp_solve op inp` member solve to it). The theme's
  correctness rests on it. **`depends-on`**.
- **`L3/ksp_solve`** — the L3-side target the per-member solve delegates to (there is **no
  `L3/solve_family`**, cycle-057 NO-ENTRY warrant; this theme is itself the authoritative L3-form home
  for the family shell, but its RHS per-member solve renders against `L3/ksp_solve`). Per §5's
  both-endpoints rule this is the nearest L3 target endpoint the theme cites (§"Verified-against"
  L3-source). **`depends-on`** (L3 target endpoint). Firm, so no rank impact.

The three slugs the planner / ledger O1 promotion condition name (`L4/solve_family`, `L4/ksp_solve`,
`L4-L3/ksp-solve-driver-dissolution`) are all `depends-on`. I additionally include `L3/ksp_solve`
as a `depends-on` to honor §5's "both endpoints" rule faithfully (the L3 target endpoint), since the
theme's §"L3 form (RHS)" delegates the per-member solve to it. It is firm, so it cannot introduce a
violation. The concept pages the theme cites (`state-stratification`, `variant-absorption`,
`sequential-obstruction`) are navigational narrative pointers → **`reference`** (they carry no
liveness and constrain no rank; per scheme §5 a narrative-concept page sits outside the subject DAG).
The transitively-delegated sibling themes (`iterate-while-dissolution`,
`krylov-step-typed-wrapper-dissolution`) are reached *through* `ksp-solve-driver-dissolution`, not
directly — listed as `reference` for navigation, not re-declared as direct blocking deps.

## Proposed changes

This is a pure frontmatter prepend. The file currently has NO YAML frontmatter (line 1 is the
`# solve-family-map-dissolution` heading). The edit inserts a `---`-delimited block before that
heading. Frontmatter format copied from the canonical typed node `book/src/L2/nrm2.md`.

```edit:book/src/L4-L3/solve-family-map-dissolution.md
[old]:
# solve-family-map-dissolution

The L4>L3 lowering theme for the [`solve_family`](../L4/solve_family.md) **outer map-shell**
[new]:
---
layer: L4-L3
theme: solve-family-map-dissolution
rank: firm
edges:
  depends-on:
    - L4/solve_family
    - L4/ksp_solve
    - L4-L3/ksp-solve-driver-dissolution
    - L3/ksp_solve
  reference:
    - L4/iterate-while
    - L4-L3/iterate-while-dissolution
    - L4-L3/krylov-step-typed-wrapper-dissolution
    - concepts/state-stratification
    - concepts/variant-absorption
    - concepts/sequential-obstruction
---

# solve-family-map-dissolution

The L4>L3 lowering theme for the [`solve_family`](../L4/solve_family.md) **outer map-shell**
```

## Discipline notes

- **PURE edge-typing — no maturity re-judgment, no §Status prose change, no LHS/RHS body change.**
  The theme's §Status already leads with `firm`; the typed `rank: firm` token merely makes the
  on-disk `## Status` machine-visible to the linter, bypassing the `read_status_line` blob-scan
  false positive (the typed token wins over the prose fallback in `derive_rank`). This is exactly
  the CLEARED-BY-RETYPING mechanism that discharged R1–R11 in the c095 cascade
  (`scaffolding/graded-stack-baseline-exceptions.md`), applied now to the one deferred lazy-tail node.
- **No high→low inversion.** The theme's rotation direction (L4 LHS → L3 RHS, narrated forward) is
  untouched; I only added frontmatter. The reverse-lift notes already in the theme's §"L4 vs L3
  distinction" stay where they are.
- **§5 both-endpoints rule honored.** I added `L3/ksp_solve` (the L3 target endpoint) as a
  `depends-on` beyond the planner/ledger-named three, deliberately, to faithfully type the lowering
  edge on both endpoints per `graded-stack-scheme.md` §5. It is firm, so it cannot create a violation;
  this strengthens the typed-edge audit without risk.
- **Cross-references to harvester/lowering-verifier provenance:** the O1 discharge mechanism is the
  one the c095 D6/D7 reports root-caused (the `read_status_line` token-priority parse bug) and the
  baseline-exceptions ledger TRACKED-OPEN-1 entry records as the promotion condition for this exact node.

## Supporting evidence

- Baseline-exceptions ledger O1 entry + promotion condition: `scaffolding/graded-stack-baseline-exceptions.md`
  (TRACKED-OPEN table; the promotion condition is "type `book/src/L4-L3/solve-family-map-dissolution.md`
  with `rank: firm` + a typed `edges:` block (`depends-on: L4/solve_family`, `L4/ksp_solve`,
  `L4-L3/ksp-solve-driver-dissolution`)").
- Scheme §5 (lowering-theme edge rule) + §2 (typed-edge block) + §1 (`rank:` token mapping):
  `book/src/methodology/graded-stack-scheme.md`.
- Endpoint §Status lines (firm-on-disk, table above): `L4/solve_family.md:144`, `L4/ksp_solve.md:160`,
  `L4-L3/ksp-solve-driver-dissolution.md:193`, `L3/ksp_solve.md:167`.
- Theme §Status leading `firm`: `book/src/L4-L3/solve-family-map-dissolution.md:185`.
- Canonical typed-frontmatter format reference: `book/src/L2/nrm2.md` (`rank: firm` + `edges:
  depends-on:/reference:`).

## Ledger discharge note (for the integrator/meta-phase)

Once this proposed change lands, the **O1 promotion condition is satisfied** and the TRACKED-OPEN-1
entry in `scaffolding/graded-stack-baseline-exceptions.md` can be **marked discharged**: the
`integrator-finalize` linter run on the LANDED state is expected to report `rank_violations = 0`
(the campaign's mechanical batch-closing confirmation gate — the typed subset reaches ZERO genuine
rank gaps). I do not write the ledger myself (it is integrator/meta-phase write-authority); flagging
the discharge here per the dispatch instruction. The burn-down summary's "1 tracked" row moves to
"0 tracked".

## Open questions / caveats

- **D4 interaction (benign, parallel-safe).** The c096 D4 dispatch fixes the `read_status_line`
  token-priority parse bug in the same finalize window. My typed `rank: firm` clears O1 **independent
  of** D4 (the typed token bypasses the prose fallback entirely). If D4 lands first, the prose-fallback
  false positive would also be retired for this node; if my typing lands first, the node is already
  typed and never reaches the fallback. Either ordering drives `rank_violations` to 0 for this edge.
  No file overlap (D4 is `tools/`-only). Recorded as a benign data-point for the finalize linter run,
  matching the planner's D3×D4 overlap analysis.
- **No further L4-L3 sweep performed.** The scope permitted optionally typing another firm-leading
  L4-L3 theme. I confined the change to O1 (the deliverable) — at the time of this dispatch NO L4-L3
  theme carries typed frontmatter yet (the rollout's lazy tail has not reached the lowering
  directories), so a broader sweep would be the start of the deferred L4-L3 theme-typing sub-campaign,
  out of scope for this batch-closing cycle. O1 is the deliverable; the broader L4-L3 typing belongs
  to the deferred batch-31 tranche the planner recorded.
- **Signature unchanged.** The firmed-up `L4/solve_family` signature did not shift the theme's
  LHS/RHS shape (the theme already renders the firm cap's `map (\inp -> ksp_solve op inp) rhss` form);
  no abstractor reread needed — this is pure edge-typing, the cleanest re-anchor class.

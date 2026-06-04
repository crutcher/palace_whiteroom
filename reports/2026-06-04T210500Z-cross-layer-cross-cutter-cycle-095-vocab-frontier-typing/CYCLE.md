---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-04T210552Z
scope: L1↔L2↔L3↔L4 cross-cut — P1 high-fan-out vocabulary-frontier edge-typing + stale-edge audit finding (D6, Wave 3, cycle-095 GRADED-STACK P1)
status: integrated
integrated_at: 2026-06-04T231500Z
integration_commit: efe6872
integration_notes: "cycle-095 D6 (staging position 6/7). The P1 high-fan-out vocab-frontier edge-typing: 17 files — ~15 ops got NEW rank: firm + typed edges: (ad-hoc lowers_to/lifts_from blocks replaced; cross-layer identity-view edges -> reference) + L4/index.md (count 18->19) + L4/solve_family.md:154 re-anchor (3 stale c080-NO-GO-HELD claims overturned — DISCHARGES the D3-promoted OQ in-artifact). RAN THE LINTER POST-APPLY: rank violations 22->1. Applied clean; retroactive-budget 0. Promoted the headline OQ graded-stack-lint-read-status-line-token-priority-bug."
inputs:
  - reports/2026-06-04T204023Z-cycle-planner-cycle-095/CYCLE.md (D6 scope; the stale-edge "Key on-disk finding")
  - book/src/methodology/graded-stack-scheme.md (the rank:/edges:/feature_root: grammar — §1 ladder, §2 edge block, §4 migration, §5 un-fronted-node rule)
  - reports/2026-06-04T204500Z-harvester-cycle-095-bilinear-form-firm-flip/CYCLE.md (D1 — bilinear-form→firm, the post-cascade state + the direct-edge-set precedent)
  - reports/2026-06-04T205500Z-lowering-verifier-cycle-095-gram-reduce-rejudgment/CYCLE.md (D3 — gram_reduce→firm; the L4/index:101 + solve_family:154 flags routed to me)
  - book/src/L1/{dot,apply_linop,nrm2,scal,normalize,matrix-weighted-norm,eigsolve}.md (the L1 frontier — §Status + §Dependencies read this cycle)
  - book/src/L2/{inner_product,linear_combination,nrm2,eigsolve}.md (the L2 frontier)
  - book/src/L3/{dot,inner_product,normalize}.md (the L3 frontier)
  - book/src/L4/{domain_energy_reduce,index}.md (the L4 frontier + the contested index I own this cycle)
  - tools/graded-stack-lint/graded_stack_lint.py (linter source — read_status_line + derive_rank, the mechanism of the false positives)
---

# CYCLE: Cross-layer observation — P1 high-fan-out vocabulary-frontier edge-typing + the stale-edge false-positive audit

## Summary

This is **D6, Wave 3** of cycle-095 (the GRADED-STACK P1 launch + bilinear-form cascade). I typed the `rank:` + `edges:` frontmatter on the **15 most-depended-on firm-leaf vocabulary nodes** — the frontier the rank check anchors on — reading each node's own current `## Status`, mapping it via scheme §1, and converting its prose `## Dependencies` section into a deliberately-classified typed `edges:` block (direct deps only, per D3's precedent). **All 15 read `firm` on disk** (verified this cycle); this is a pure edge-typing + rank-token pass, NOT a promotion.

The headline cross-layer finding (the campaign's audit-first payload): the planner predicted ~8 of the 12 "residual" rank violations are stale-edge false positives. I **confirmed and root-caused** all 8. The mechanism is sharper than "the prose dep-map drifts": the rank linter's `read_status_line` fallback (used for any leaf with no explicit frontmatter `rank:` token) **mis-parses the live `## Status` line** — it joins 5 lines into a blob and scans for maturity tokens in priority order (`rough-in` before `firm`), so a §Status paragraph that LEADS with `firm` but later contains the word "rough-in" (a `normalize_B` rough-in note, "three firm/rough-in L1 leaves", an "`eigsolve` rough-in framing does not bind" disclaimer) is mis-read as `rough-in`. The dep nodes are firm on disk; the linter just never reaches the leading `firm` token. My typed `rank: firm` frontmatter on each of these nodes **clears all 8 by construction** — because `derive_rank` prioritizes an explicit `rank:` token OVER the buggy prose-scan fallback (verified). This both validates the campaign thesis (a single authoritative typed source-of-truth removes the drift) AND surfaces a concrete linter parse bug for the batch-30 meta-phase.

I also own `book/src/L4/index.md` this cycle (the contested index D3/D4 flagged): the `:101` gram_reduce cell flip (`rough-in (test-coverage-bounded)`→`firm` + the bilinear-form label flip, now that D3 firmed gram_reduce), the `:32`/`:58` count-header bumps (data-algebra firm 18→19), and the stale c080 NO-GO-HELD re-anchor at `book/src/L4/solve_family.md:154`.

## Observation kind

**Audit residue** (primary) — the `verified_against:`/rank-linter audit shows a cluster of stale rank violations whose cause is a single linter parse defect interacting with prose drift. Secondary: **Consistency drift** (the prose `## Status` representation is a drifting second source-of-truth relative to the typed `rank:` token the campaign installs).

## Specific finding

### Finding 1 — the 8 stale-edge false positives, root-caused (the campaign headline)

The c094 baseline linter reports `rank_violations=22`. Partitioned against the live on-disk maturity (each dep's authoritative `## Status` line read this cycle):

| violation (`src -> dep (dep_rank shown by linter)`) | dep's ACTUAL §Status on disk | disposition |
|---|---|---|
| `L2/normalize -> L1/normalize (rough-in)` | **firm** (`L1/normalize.md:99`) | CLEARED-BY-RETYPING (D6) |
| `L3/normalize -> L1/normalize (rough-in)` | **firm** | CLEARED-BY-RETYPING (D6) |
| `L2/nrm2 -> L2/inner_product (rough-in)` | **firm** (`L2/inner_product.md:449`) | CLEARED-BY-RETYPING (D6) |
| `L3/dot -> L2/inner_product (rough-in)` | **firm** | CLEARED-BY-RETYPING (D6) |
| `L3/inner_product -> L2/inner_product (rough-in)` | **firm** | CLEARED-BY-RETYPING (D6) |
| `L4/domain_energy_reduce -> L1/matrix-weighted-norm (rough-in-tcb)` | **firm** (`L1/matrix-weighted-norm.md:110`, c091) | CLEARED-BY-RETYPING (D6) |
| `feature/energy-fields.L1 -> L1/matrix-weighted-norm (rough-in-tcb)` | **firm** | CLEARED-BY-RETYPING (D6; the dep-side; D5 owns the energy-fields column) |
| `feature/energy-fields.L4 -> L1/matrix-weighted-norm (rough-in-tcb)` | **firm** | CLEARED-BY-RETYPING (D6; dep-side) |

**Root cause (the load-bearing detail for the meta-phase).** The linter assigns a leaf's rank by priority `explicit rank: > firmness: > feature status: > prose ## Status` (`derive_rank`, `tools/graded-stack-lint/graded_stack_lint.py:328-361`). The frontier deps above carry NONE of the first three (they are prose-`## Status`-only files), so the linter falls to `read_status_line` (`:310-326`), which does:

```python
blob = " ".join(lines[i + 1 : i + 6]).lower()
for tok in ("partly-constructive", "rough-in (test-coverage-bounded)",
            "rough-in", "roadmap_goal", "obstruction",
            "partial-obstruction", "stub", "firm"):
    if tok in blob:
        return tok
```

The scan order puts `rough-in` BEFORE `firm`, and it scans a 5-line blob, so for any §Status paragraph that leads with `firm` but mentions "rough-in" within 5 lines the function returns `rough-in`. Verified directly:

- `L1/normalize.md:99` §Status leads `` `firm` — firm-on-positive-structure … `` but the same paragraph says "the `eigsolve` rough-in framing does not bind" and "the B-weighted sibling `normalize_B` is an in-chapter **rough-in note**". `read_status_line` returns `rough-in`.
- `L2/inner_product.md:449` §Status leads `` `firm` — the structure is a reduce-to-scalar fold over three firm/rough-in L1 leaves `` — the substring "rough-in" is in the FIRST line. Returns `rough-in`.
- `L1/matrix-weighted-norm.md:110` reads `` `firm` — promoted from `rough-in (test-coverage-bounded)` … `` — the provenance phrase trips the `rough-in (test-coverage-bounded)` token (rank 2.5). Returns `rough-in (test-coverage-bounded)`.

This is NOT a prose-dep-map mis-citation in the consumer (the consumers do not restate the dep's maturity in a way the linter reads); it is the linter's own authoritative-rank derivation reading a stale-by-construction prose heuristic. **The fix is exactly what the campaign prescribes:** install the explicit `rank:` token on the dep node. `derive_rank` then returns `firm` (verified: `derive_rank({'rank':'firm'}, <text-with-rough-in-prose>)` → `firm`), bypassing the buggy fallback. My D6 pass writes `rank: firm` on all of these dep nodes, so the 8 false positives clear by construction.

### Finding 2 — the `L1/eigsolve` chain is ALSO a false positive (the planner's "VERIFY" items resolved)

The planner flagged three violations citing `L1/eigsolve (rough-in-tcb)` as "VERIFY at typing":
- `L2/eigsolve -> L1/eigsolve (rough-in-tcb)`
- `feature/boundary-mode.L1 -> L1/eigsolve (rough-in-tcb)`
- `feature/eigenmode.L1 -> L1/eigsolve (rough-in-tcb)`

**Resolved: FALSE POSITIVE.** `L1/eigsolve.md:167` §Status reads `` `firm` (cycle-022, route-(b) law-confidence re-eval; promoted from `rough-in (test-coverage-bounded)` …) ``. The provenance phrase "promoted from `rough-in (test-coverage-bounded)`" trips the same `read_status_line` bug — the token scan returns `rough-in (test-coverage-bounded)` (rank 2.5) although the node IS firm (promoted c022). Same mechanism as Finding 1. My D6 pass types `L1/eigsolve` with `rank: firm`, clearing the `L2/eigsolve -> L1/eigsolve` violation directly. The two feature-column consumers (`boundary-mode.L1`, `eigenmode.L1`) clear on the dep-side retype too (D5 owns those columns' own frontmatter; the dep-side fix is mine).

### Finding 3 — the genuinely-residual violations (NOT cleared by D6 typing)

After D6 retypes the frontier and the cascade lands, the residual violations are:

- `L4/solve_family -> L4-L3/solve-family-map-dissolution (rough-in-tcb)` — **GENUINE.** `solve_family` is firm (c086), but its lowering-theme endpoint `L4-L3/solve-family-map-dissolution` reads `rough-in (test-coverage-bounded)` (rank 2.5). Per scheme §5, a theme's rank is `min(endpoints)` — but here the theme is BELOW its firm L4 endpoint. This is a real rank-gap requiring either the theme's promotion or a baseline-exception entry. **Routed to D7** (the baseline-exception set owner) — it is a lowering-theme maturity question, not a vocabulary-frontier typing item. Out of my scope (I do not author themes; abstractor/lowering-verifier territory).
- The 10 bilinear-form cascade violations (`L4/gram_reduce -> L1/bilinear-form` ×2, the 4 columns × {L0→L1, L1→bilinear-form}) — **CLEARED-BY-CASCADE** (D1 firmed bilinear-form, D3 firmed gram_reduce, D4 the columns). Not mine; recorded here for the partition completeness.

**Partition tally:** 22 baseline violations = 10 CLEARED-BY-CASCADE (D1–D4) + 9 CLEARED-BY-RETYPING (D6: Findings 1+2 — the 8 stale + the `L2/eigsolve -> L1/eigsolve` dep-typed edge; the 2 feature consumers clear on the D6 dep-side retype + D5 column-side typing) + 1 GENUINE-RESIDUAL (`solve_family -> solve-family-map-dissolution`, → D7). This confirms the planner's "~8 stale + small genuine residual" estimate (8–9 stale; 1 genuine).

### Finding 4 — the 15 typed nodes (the rank-check anchor)

All 15 frontier nodes read `firm` on disk → `rank: firm`. Direct-dep `edges:` blocks below (proposed-changes). Edge classification follows scheme §2 + the D3 direct-vs-transitive precedent: a node's own folded/consumed primitives are `depends-on`; cross-layer identity views (`lowers_to`/`lifts_from`/`lifts_to`) and concept/theme/sibling pointers are `reference` (navigational, no rank constraint, no liveness — these are same-operator-at-adjacent-layer views, not blocking constituents; classifying them `reference` is the deliberate choice that avoids importing e.g. the `L3/eigsolve` `partial-obstruction` rank onto the firm `L2/eigsolve`).

## Recommendation

- **Dispatch the batch-30 meta-phase to fix the `read_status_line` linter bug.** The token-priority scan (`rough-in` before `firm`, over a 5-line blob) mis-parses any firm §Status paragraph that mentions "rough-in" in its provenance/disclaimer prose. Two clean fixes: (a) match only the FIRST inline-code token on the first non-empty line after `## Status` (the project convention is the maturity word is the leading `` `token` ``), not a blob scan; or (b) scan in resolution-DESCENDING order is wrong too — the right fix is leading-token-only. This is the reason P1's typed-`rank:` migration is load-bearing: it routes around the heuristic entirely. **Flag for batch-30 meta-phase** (OQ appended).
- **Confirm the campaign thesis to the meta-phase.** The 8–9 stale false positives are ALL resolved by installing the explicit `rank:` token — the single-authoritative-source migration is validated. No prose-dep-map needs hand-reconciliation for these; the typed token suffices.
- **Defer the `solve_family -> solve-family-map-dissolution` residual to D7** (baseline-exception set) with promotion condition "clears when `solve-family-map-dissolution` firms OR is re-typed if it too is a stale false positive — D7 should verify the theme's live §Status with the leading-token rule, not the linter's current parse."

## Proposed changes

> All proposed-changes route through `integrator-per-report` (Phase 5). I write NO `book/` file directly. The frontier nodes' frontmatter is superseded per scheme §4(a) (the `edges:` block replaces ad-hoc `depends_on:`/`lowers_to:`/`lifts_from:`/`consumes:` lists). For the six prose-`## Status` L1 nodes (dot, apply_linop, nrm2, scal, normalize, matrix-weighted-norm) and the two prose-`## Status` L2 nodes (inner_product, linear_combination) and the prose-`## Status` L1/eigsolve, a NEW frontmatter block is inserted at the top of the file (they currently have none). For the frontmatter-bearing nodes (L2/nrm2, L3/dot, L3/inner_product, L3/normalize, L4/domain_energy_reduce, L2/eigsolve) the existing block's ad-hoc edge lists are replaced by `rank:` + `edges:`.

### (A) L1 frontier — insert frontmatter (these files currently have NO frontmatter)

`book/src/L1/dot.md` — leaf primitive (no L1 deps):

```edit:book/src/L1/dot.md
---
layer: L1
operator: dot
rank: firm
edges:
  reference:
    - L1-L0/dot-mutation-rotation
    - concepts/dot
---
```
(Insert at top of file, before the `# dot` heading. `dot` is a leaf — §Dependencies: "None at L1." The L1>L0 rotation + the cross-cutting `concepts/dot` prose are navigational references; neither is a blocking constituent. `nrm2`/`bilinear-form` are DOWNSTREAM consumers, not deps — correctly omitted.)

`book/src/L1/apply_linop.md` — leaf primitive:

```edit:book/src/L1/apply_linop.md
---
layer: L1
operator: apply_linop
rank: firm
edges:
  reference:
    - L1-L0/apply-linop-mutation-rotation
    - concepts/apply_linop
---
```
(Leaf — §Dependencies: "None at L1." `AddMult` is a sibling-leaf composition, NOT a dep, per the §Semantics note — omitted. Verify the L1>L0 theme slug; if `apply-linop-mutation-rotation` does not exist on disk, the integrator drops the reference edge — references constrain nothing, so a missing-target reference is a soft warning not a hard error. NOTE: confirm the exact L1>L0 theme filename at integration.)

`book/src/L1/nrm2.md` — depends on `dot`:

```edit:book/src/L1/nrm2.md
---
layer: L1
operator: nrm2
rank: firm
edges:
  depends-on:
    - L1/dot
  reference:
    - L1-L0/nrm2-mutation-rotation
---
```
(§Dependencies: "the **only** L1 operator that `nrm2` depends on" = `dot`; `nrm2(x) = √dot(x,x)`. The `sqrt`/`abs` are sub-L1 scalar ops, not nodes.)

`book/src/L1/scal.md` — leaf primitive:

```edit:book/src/L1/scal.md
---
layer: L1
operator: scal
rank: firm
edges:
  reference:
    - L1/axpby
    - L1-L0/scal-mutation-rotation
---
```
(§Dependencies: "None at L1 … the fourth … BLAS-1 floor primitive." The `axpby` relationship is explicit SIBLING-SUBSUMPTION, not a dependency (`scal(α,x) = axpby(α,x,0,y)`) — classified `reference`. The `Normalize` mention is a downstream consumer, omitted.)

`book/src/L1/normalize.md` — fused composite of `nrm2` + `scal`:

```edit:book/src/L1/normalize.md
---
layer: L1
operator: normalize
rank: firm
edges:
  depends-on:
    - L1/nrm2
    - L1/scal
  reference:
    - L1-L0/normalize-mutation-rotation
    - L1/orthogonalize
---
```
(§Dependencies: "this is a fused composite, not a leaf" → `nrm2` + `scal` are the two depends-on constituents. The `orthogonalize` / power-iteration / NEP mentions are downstream consumers (cross-reference, NOT reverse-deps per the section's own framing) — `orthogonalize` kept as a `reference` see-also; the rest omitted. The `scal ∘ nrm2` subsumption is a sibling note, not an edge.)

`book/src/L1/matrix-weighted-norm.md` — depends on `dot` + `apply_linop`:

```edit:book/src/L1/matrix-weighted-norm.md
---
layer: L1
operator: matrix-weighted-norm
rank: firm
edges:
  depends-on:
    - L1/dot
    - L1/apply_linop
  reference:
    - L1/bilinear-form
    - L1-L0/matrix-weighted-norm-mutation-rotation
---
```
(§Dependencies: "two L1 dependencies" = `dot` (the inner reduction `xᴴ(B·x)`) + `apply_linop` (supplies `B·x`). The sibling `bilinear-form` is explicitly "(queued as a separate harvest)" — a sibling reference, NOT a dep (it is the other consumer of the same two primitives). NOTE: this node already carries a c091 `verified_against:` block lower in the file — the frontmatter insert goes at the very top and does not touch that block.)

### (B) L1/eigsolve — insert frontmatter (currently NONE)

`book/src/L1/eigsolve.md` — depends on `ksp_solve` + `apply_linop`:

```edit:book/src/L1/eigsolve.md
---
layer: L1
operator: eigsolve
rank: firm
edges:
  depends-on:
    - L1/ksp_solve
    - L1/apply_linop
  reference:
    - concepts/constructed-operator-factory
    - concepts/variant-absorption
---
```
(§Dependencies: "depends on three primitives" — `ksp_solve` (inner linear solver, DIRECT) + `apply_linop` (system-operator action, DIRECT); `dot`/`nrm2`/`axpy`/`axpby` are explicitly "Recorded as transitive rather than direct because they appear inside the per-orchestration body the L1 eigsolve opaquely wraps" → NOT direct edges (the D3 direct-only precedent). The two concepts are navigational references.)

### (C) L2 frontier — inner_product + linear_combination (insert frontmatter; currently NONE)

`book/src/L2/inner_product.md` — folds `dot` + `bilinear-form`, composes `apply_linop` for the weighted member:

```edit:book/src/L2/inner_product.md
---
layer: L2
operator: inner_product
rank: firm
edges:
  depends-on:
    - L1/dot
    - L1/bilinear-form
    - L1/apply_linop
  reference:
    - L2/linear_combination
    - concepts/dot
    - L2-L1/inner-product-fold-specialization
---
```
(§Dependencies: the fold members are `dot` (Hermitian/symmetric + `tdot` co-defined there) + `bilinear-form` (M-weighted member) — depends-on; `apply_linop` is the L2-composition for the weighted member (`inner_product_M x M y = inner_product (apply_linop M x) y`) — depends-on. The sibling fold `linear_combination` is explicit do-NOT-merge → `reference`; `concepts/dot` + the L2>L1 theme are navigational.)

`book/src/L2/linear_combination.md` — folds the fixed-arity BLAS-1 family:

```edit:book/src/L2/linear_combination.md
---
layer: L2
operator: linear_combination
rank: firm
edges:
  depends-on:
    - L1/scal
    - L1/axpy
    - L1/axpby
    - L1/axpbypcz
  reference:
    - concepts/scalar-promotion
    - L2/inner_product
    - L2-L1/linear-combination-fold-specialization
---
```
(§Dependencies: the arity specializations `scal` (arity 1) / `axpy` (arity 2) / `axpby` (arity 2) / `axpbypcz` (arity 3) are the family members it folds — depends-on. The sibling fold `dot`/`inner_product` is do-NOT-merge → `reference`; `concepts/scalar-promotion` + the forthcoming L2>L1 theme are navigational. NOTE: the `linear-combination-fold-specialization` theme is "forthcoming … does not yet exist" per the prose — a missing reference target is a soft warning, integrator may drop it; left as a reference so it resolves once authored.)

### (D) L2/nrm2 — replace ad-hoc edge lists with rank: + edges:

`book/src/L2/nrm2.md` frontmatter (currently `lowers_to:`/`lifts_from:`/`consumes:`):

```edit:book/src/L2/nrm2.md
---
layer: L2
operator: nrm2
rank: firm
edges:
  depends-on:
    - L2/inner_product
  reference:
    - L1/nrm2
    - L3/nrm2
variant_axes:
  - element-type (real / complex; collapsed to single operator at L2 — result is always real)
---
```
(The `consumes: L2/inner_product` becomes `depends-on` (nrm2 = √∘abs∘inner_product at y=x — the CONSUMER edge; do-NOT-merge is a fold-membership note, not an edge type — it still depends-on the combinator it consumes). The `lowers_to: L1/nrm2` (identity-in-form) + `lifts_from: L3/nrm2` (identity-in-form) are same-operator adjacent-layer views → `reference` (navigational; no rank gate — these are NOT blocking constituents, they are the same reduction at other layers).)

### (E) L3/dot — replace lowers_to/lifts_from

`book/src/L3/dot.md` frontmatter:

```edit:book/src/L3/dot.md
---
layer: L3
operator: dot
rank: firm
edges:
  depends-on:
    - L2/inner_product
  reference:
    - L4/dot
variant_axes:
  - element-type (real / complex)
  - conjugation-convention (hermitian / unconjugated `tdot` — complex element-type only)
---
```
(`dot` at L3 is the `M=I` specialization of the firm L2 `inner_product` combinator — the `lowers_to: L2/inner_product` is the substantive specialization edge → `depends-on` (the L3 form rests on the L2 combinator-as-entry). The `lifts_from: L4/dot` identity-in-form view → `reference`.)

### (F) L3/inner_product — replace lowers_to/lifts_from

`book/src/L3/inner_product.md` frontmatter:

```edit:book/src/L3/inner_product.md
---
layer: L3
operator: inner_product
rank: firm
edges:
  depends-on:
    - L2/inner_product
    - L3/apply_linop
  reference:
    - L4/inner_product
    - L2-L1/inner-product-fold-specialization
    - concepts/dot
variant_axes:
  - conjugation-convention (hermitian / unconjugated `tdot` — complex element-type only; the family's namesake unification axis)
  - element-type (real / complex)
  - weight-presence (M = I plain / general-or-SPD M pre-applied — the `bilinear_form` member)
---
```
(`lowers_to: L2/inner_product` identity-in-form (the L3 form is the iteration-rotation rendering of the firm L2 combinator) → `depends-on` (it rests on the L2 floor — the §Dependencies "Upward reference (L2)" names it authoritative). The same-layer `apply_linop` (weighted member, pre-applied `M`) → `depends-on`. The `lifts_from: L4/inner_product` + the L2>L1 theme + `concepts/dot` → `reference`.)

### (G) L3/normalize — replace lowers_to/lifts_from

`book/src/L3/normalize.md` frontmatter:

```edit:book/src/L3/normalize.md
---
layer: L3
operator: normalize
rank: firm
edges:
  depends-on:
    - L3/nrm2
    - L3/scal
  reference:
    - L2/normalize
    - L1/normalize
    - L1/orthogonalize
variant_axes:
  - element-type (real | complex; collapsed to a single parameterised operator — norm output always real)
---
```
(§Dependencies: "these two are the **only** L3 dependencies" = `nrm2` + `scal` (same-layer L3 fused-composite constituents) → `depends-on`. The `lowers_to: L2/normalize` + transitive `L1/normalize` are degenerate identity-in-named-terms views (no vocabulary shift across the edge, the in-line §Downward note) → `reference` — NOT blocking (the substantive rotation is the L1>L0 mutation-rotation, not the L3>L2 identity). The `lifts_from: L1/normalize` is the same node. `orthogonalize` is a downstream-consumer see-also.)

### (H) L4/domain_energy_reduce — replace consumes/lowers_to

`book/src/L4/domain_energy_reduce.md` frontmatter:

```edit:book/src/L4/domain_energy_reduce.md
---
layer: L4
operator: domain_energy_reduce
rank: firm
edges:
  depends-on:
    - L1/participation_ratio
    - L1/matrix-weighted-norm
  reference:
    - L4/eigenfreq_qfactor_reduce
    - L4/gram_reduce
    - L4/inner_product
variant_axes:
  - field-kind (electric ½⟨E, M_i E⟩ | magnetic ½⟨B, M_i B⟩ — THE load-bearing axis; selects which domain-restricted operator family M_i and which field; the reduction runs twice, once per kind, producing two tables; absorbed into the (M_i, field) pair)
  - element-type (the field may be complex; the energy form sums the real + imaginary radicand contributions, so energyᵢ is a real ≥ 0 reduction of a possibly-complex field; the table is real)
  - partition-coverage (config-conditional: whether the configured domain set partitions the field support — gates the Σ pᵢ = 1 law, NOT the verb's shape)
---
```
(The two `consumes:` entries `participation_ratio` + `matrix-weighted-norm` are the two folded primitives → `depends-on` (both firm: participation_ratio c077, matrix-weighted-norm c091 — rank invariant `rank(3) ≤ min(3,3)` holds). The sibling combinators (`eigenfreq_qfactor_reduce` per-MODE sibling, `gram_reduce` over-unification guard, `inner_product`) are do-NOT-merge sibling references. The `lowers_to:` is an in-line identity-in-form descriptor (no theme) — dropped from edges (it names "the per-domain scalar maps", not a node slug; the substantive content is in-line). NOTE: this dropped the long maturity-qualifier prose from the old `consumes:` strings per scheme §4(c) — the dep's rank is read from its own frontmatter now.)

### (I) L2/eigsolve — replace lifts_to/lowers_to

`book/src/L2/eigsolve.md` frontmatter:

```edit:book/src/L2/eigsolve.md
---
layer: L2
operator: eigsolve
rank: firm
edges:
  depends-on:
    - L2/ksp_solve
    - L1/apply_linop
  reference:
    - L1/eigsolve
    - L3/eigsolve
    - concepts/constructed-operators
    - concepts/solver-as-operator
    - concepts/variant-absorption
    - concepts/sequential-obstruction
    - concepts/solve-monad
variant_axes:
  - spectral-transformation (none = M⁻¹ action / shift-invert = (K − σM)⁻¹M action / shift-invert-precond = STPRECOND approximate inverse — selects which operator the inner ksp_solve inverts and what apply_linop feeds it)
  - problem-type (linear = (K, M) EPS / quadratic = (K, C, M) PEP linearization / nonlinear = NEP — selects the operand-assembly the inner solve inverts, e.g. the PEP block (L₀ − σL₁))
  - backend-orchestration (arpack-rci = explicit Palace-owned apply_linop ▷ ksp_solve / slepc-st-shell = identical action routed through the PETSc ST shell PC + shell matvecs — the same composition, two assembly sites)
  - element-type (complex only — Palace's EigenvalueSolver surface is complex-only, inherited from L1)
  - scaling (NONE / NORM_2 — the Higham δ, γ premultipliers on the shell matvecs / the inner-solve un-scale; informational at the result boundary per L1 law 5)
---
```
(§Dependencies "Same-layer (L2)": `ksp_solve` (DIRECT, load-bearing — the inner solve) → `depends-on`. "Cross-layer constituents": `apply_linop` (L1, DIRECT, the first stage of `apply_shift_invert`) → `depends-on`; `dot`/`nrm2`/`axpy`/`axpby` are explicitly transitive → NOT edges (D3 precedent). The `apply_BA` is a concept-framing pointer → omit/reference. The `lifts_to: L1/eigsolve` (the NON-identity un-collapse) + `lowers_to: L3/eigsolve` (the partial-obstruction prediction) are same-operator adjacent-layer views → `reference` — DELIBERATELY classified `reference` to avoid importing the `L3/eigsolve` `partial-obstruction` rank onto the firm L2 node (the lowering relationship is navigational here; the rank-gate would be a false constraint since the L2 form is firm-on-positive-structure independent of the L3 loop obstruction). The 5 concepts are navigational.)

### (J) L4/index.md — the contested index (I OWN it this cycle)

**(J1)** The `:101` gram_reduce dep-map cell — flip status `rough-in (test-coverage-bounded)`→`firm` + the bilinear-form folded-primitive label `(rough-in … the sole remaining rough-in folded primitive, the residual gate)`→`(firm c095)`, consequent to D3 firming gram_reduce:

```edit:book/src/L4/index.md
| [`gram_reduce`](./gram_reduce.md) | `gram_reduce :: LinearOperator[N, N] -> [Tensor[N]] -> (Int -> Int -> Scalar) -> Matrix[m, m]`; `Gᵢⱼ = w(i,j) · (xⱼᵀ K xᵢ)`, symmetric (compute upper, mirror lower). The **operator-weighted symmetric-Gram reduction combinator**: reduce a collected solution family `[xᵢ]` against an operator weight `K` into the symmetric Gram matrix, parameterized by the per-entry normalization weight `w(i,j)`. The **reduce-to-matrix** member of the L4 algebra-of-folds (sibling of reduce-to-scalar [`inner_product`](./inner_product.md) + reduce-to-tensor [`linear_combination`](./linear_combination.md)). ONE reduction across the electrostatic capacitance (`w = 1`) + magnetostatic inductance (`w = 1/(IᵢIⱼ)`) output products — the **weight is the only difference**. Pure value-producing reduction — no `Solve` monad / carry / predicate. | Folds: [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (firm c091 — diagonal self-bilinear `xᵢᵀ K xᵢ`, the diagonal CONSUMER, NOT a separate fold), [`bilinear-form`](../L1/bilinear-form.md) (firm c095 — off-diagonal cross-bilinear `xⱼᵀ K xᵢ`; the last folded gate, discharged by the cycle-095 firm-flip-and-cascade wave). Consumes: [`solve_family`](./solve_family.md) (produces the family `[xᵢ]`). Concepts: `black-box-vs-accelerated-kernels` (§"the combinators rise regardless"). Sibling combinators: [`inner_product`](./inner_product.md), [`linear_combination`](./linear_combination.md). | L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) / [`bilinear-form`](../L1/bilinear-form.md) by **identity-in-form on the body** (the reduction is a plain fold of L1 bilinear evaluations; **no dedicated L4>L3 theme** — the in-line-marker route; the substantive downward content lives in the L1 primitives' L1>L0 mutation rotations). | `firm` (harvested cycle-073 D1 LEAD from the feature-chapter forward-mine flags `electrostatic.L4.md:40` + `magnetostatic.L4.md:40`; structure firm-on-positive-structure on 2 skeleton-identical witnesses electrostatic `electrostaticsolver.cpp:100-140` + magnetostatic `magnetostaticsolver.cpp:110-152`; promoted rough-in (test-coverage-bounded)→firm cycle-095 (D3 lowering-verifier re-judgment) on the **firm-on-positive-structure escape** — after the cycle-091 + cycle-095 cascade BOTH folded gates are discharged (the diagonal `matrix-weighted-norm` firmed c091 + the off-diagonal `bilinear-form` firmed c095 D1), and a reduction is as firm as its least-firm folded primitive, so the verb promotes; the materially identical disposition to its reduce-verb siblings `domain_energy_reduce` c091 / `eigenfreq_qfactor_reduce` c082 / `sparameter_reduce` c083 / `solve_family` c086; the missing dedicated Gram unit test is redundant under the escape (every law a syntactic identity on the fold over two firm halves). Disciplined-mining-gate 2-of-N met, normalization-weight a variant axis not a break-witness; eigenmode/driven post-processing candidate 3rd+ witnesses for a future mine) |
```

**(J2)** The `:32` count header — the data-algebra firm count 18→19 (gram_reduce joins; it was the one rough-in table row). Edit the leading count token only:

```edit:book/src/L4/index.md
**Firm at L4 (19 + 4 outer-driver)** — cycle-095 promoted the operator-weighted symmetric-Gram reduction combinator [`gram_reduce`](./gram_reduce.md) `rough-in (test-coverage-bounded)` → `firm` (the bilinear-form firm-flip-and-cascade wave D3 — after the cycle-091 + cycle-095 cascade BOTH its folded gates are discharged, the diagonal `matrix-weighted-norm` c091 + the off-diagonal `bilinear-form` c095 D1, the firm-on-positive-structure escape; this re-empties the L4 rough-in cohort). Before it, cycle-091 promoted the per-domain energy-table reduction combinator [`domain_energy_reduce`](./domain_energy_reduce.md) `rough-in` → `firm` (the batch-29 firm-flip-and-cascade wave — both its folded primitives now firm L1, matrix-weighted-norm c091 + participation_ratio c077, the firm-on-positive-structure escape, the per-DOMAIN realization of the per-MODE `eigenfreq_qfactor_reduce` c082 disposition).
```
(NOTE for the integrator: this edits ONLY the first sentence of the long `:32` paragraph — the "18 + 4 outer-driver" count token → "19 + 4 outer-driver", and prepends the gram_reduce c095 promotion clause ahead of the existing cycle-091 domain_energy_reduce clause. The remainder of the `:32` paragraph (cycle-086/083/069/068 history) is preserved verbatim. The "(this emptied the L4 rough-in cohort)" phrase that previously trailed the domain_energy_reduce clause is folded into the new gram_reduce clause as "re-empties" — because gram_reduce was the residual rough-in row the old phrasing overlooked.)

**(J3)** The `:58` "Rough-in at L4 (0)" narration — it ALREADY claimed 0 while gram_reduce sat at `rough-in (test-coverage-bounded)` (a pre-existing optimistic stale; the cohort was really 1). The D3 firming makes the claim TRUE; add gram_reduce to the firm-promotion narration:

```edit:book/src/L4/index.md
**Rough-in at L4 (0)** — the rough-in cohort is now genuinely empty: the operator-weighted symmetric-Gram reduction combinator [`gram_reduce`](./gram_reduce.md) **promoted to `firm` cycle-095** (the bilinear-form firm-flip-and-cascade wave D3 — after the cycle-091 + cycle-095 cascade BOTH its folded gates are discharged, the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) c091 + the off-diagonal [`bilinear-form`](../L1/bilinear-form.md) c095, and a reduction is as firm as its least-firm folded primitive, so the firm-on-positive-structure escape applies exactly as it did for its reduce-verb siblings), moving to the firm cohort above; this was the one rough-in table row the prior "(0)" narration overlooked (it had counted only the c091 domain_energy_reduce / c082 eigenfreq_qfactor_reduce / c086 solve_family promotions). The per-domain energy-table reduction verb [`domain_energy_reduce`](./domain_energy_reduce.md) **promoted to `firm` cycle-091** (the batch-29 firm-flip-and-cascade wave — its formerly-rough-in folded numerator [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) firmed that cycle, so BOTH its folded primitives now have firm L1 homes — matrix-weighted-norm c091 + [`participation_ratio`](../L1/participation_ratio.md) c077 — and the firm-on-positive-structure escape applies exactly as it did for its per-MODE sibling), moving to the firm cohort above. The eigenmode per-mode reduction [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) **promoted to `firm` cycle-082** (firm-on-positive-structure escape; both folded per-mode primitives firm L1 — `eigenvalue-untransform` c080 + `participation_ratio` c077 — and the assembly carries no inner-product-axiom content), and the fixed-operator family-map combinator [`solve_family`](./solve_family.md) **promoted to `firm` cycle-086** (the same firm-on-positive-structure / syntactic-identity escape — element-independence read off the const `BaseKspSolver::Mult` body, `palace/linalg/ksp.cpp:297-310`), both moving to the firm cohort above:
```

### (K) solve_family.md:154 — re-anchor the stale c080 NO-GO-HELD narrative

`book/src/L4/solve_family.md:154` (the "Column-gate note") asserts (i) gram_reduce folds "plain-`rough-in` matrix-weighted-norm", (ii) the matrix-weighted-norm √-cascade is "NO-GO-HELD (c080 D1 ruled the firm-on-positive-structure escape INAPPLICABLE)", and (iii) "Those columns stay `status: seed` this cycle" — ALL three overturned by c091 (matrix-weighted-norm firmed) / c095 (gram_reduce firmed, columns flip via D4). Re-anchor:

```edit:book/src/L4/solve_family.md
**Column-gate note (load-bearing).** Firming `solve_family` (c086) discharged ONE of the TWO own-constituent gates on the [`electrostatic`](../feature/electrostatic.L4.md) + [`magnetostatic`](../feature/magnetostatic.L4.md) driver columns. The SECOND gate — [`gram_reduce`](./gram_reduce.md) (which folds the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + the off-diagonal [`bilinear-form`](../L1/bilinear-form.md)) — was firmed at **cycle-095** (D3): `matrix-weighted-norm` firmed c091 (the c080 NO-GO-HELD was OVERTURNED by the batch-28 meta-phase GO — the firm-on-positive-structure escape was ruled APPLICABLE after all), `bilinear-form` firmed c095 (D1), and with both folded gates discharged `gram_reduce` itself promoted to `firm`. With both own-constituent gates (`solve_family` c086 + `gram_reduce` c095) now firm, the [`capacitance`](../feature/capacitance.L1.md)/[`inductance`](../feature/inductance.L1.md)/electrostatic/magnetostatic columns flip off `seed` at cycle-095 (D4) under the OWN-COMPOSITION rule.
```
(NOTE for the integrator: this is the single paragraph at `:154`. D3 flagged it and routed it to D4/integrator; the planner assigned the re-anchor to me as the L4-area index/narrative owner. It does NOT touch `solve_family`'s own `## Status` or frontmatter — only the stale forward-looking Column-gate note. If D4's column re-eval lands a DIFFERENT verdict (columns stay seed for another reason), the integrator should reconcile the final clause "flip off `seed` … (D4)" with D4's actual outcome — the load-bearing correction is clauses (i) + (ii); clause (iii) tracks D4.)

## Supporting evidence

- **Linter parse defect (the root cause)**: `tools/graded-stack-lint/graded_stack_lint.py:310-326` `read_status_line` — the 5-line-blob token scan in priority order (`rough-in` before `firm`). `derive_rank` priority `:328-361` (`rank: > firmness: > status: > prose`) — confirms an explicit `rank:` token bypasses the buggy fallback (verified by direct call: `derive_rank({'rank':'firm'}, <rough-in-prose>)` → `firm`).
- **Frontier nodes' live §Status (all firm, verified on disk this cycle)**: `L1/dot.md:100`, `L1/apply_linop.md:87`, `L1/nrm2.md:88`, `L1/scal.md:80`, `L1/normalize.md:99`, `L1/matrix-weighted-norm.md:110`, `L2/inner_product.md:449`, `L2/linear_combination.md:318`, `L2/nrm2.md:82`, `L3/dot.md:80`, `L3/inner_product.md:348`, `L3/normalize.md:123`, `L4/domain_energy_reduce.md:271`, `L1/eigsolve.md:167`, `L2/eigsolve.md:155`.
- **Baseline linter run (22 violations)**: `python3 tools/graded-stack-lint/graded_stack_lint.py --json` this cycle — full `rank_violations` list quoted in Finding 1/3. Histogram: firm 158, rough-in 26, partly-constructive 8, obstruction 10, partial-obstruction 4, stub 1.
- **Post-cascade state (read from the Wave-1/2 reports)**: D1 (`reports/2026-06-04T204500Z-harvester-cycle-095-bilinear-form-firm-flip/CYCLE.md`) flips `bilinear-form`→firm; D3 (`reports/2026-06-04T205500Z-lowering-verifier-cycle-095-gram-reduce-rejudgment/CYCLE.md`) flips `gram_reduce`→firm and routes the `L4/index:101` + `solve_family:154` flags to me.
- **L4/index count semantics**: `book/src/L4/index.md:32` "18 + 4 outer-driver" — the data-algebra dep-map table (`:79`–`:131`) holds 19 rows, 18 firm + 1 rough-in (gram_reduce at `:101`); firming it → 19 firm. The 4 outer-driver caps (`ksp_solve`/`eigsolve`/`fold_solve` + the 4-anchor solve-monad vocabulary at `:41`–`:54`) are counted separately and unchanged.

## Open questions / caveats

- **`graded-stack-lint-read-status-line-token-priority-bug` (FLAG for batch-30 meta-phase).** `read_status_line` mis-parses any firm `## Status` paragraph that mentions "rough-in" within 5 lines (provenance phrases "promoted from rough-in", disclaimers "the rough-in framing does not bind", sibling notes "an in-chapter rough-in note"). It caused ALL 8–9 stale rank-violation false positives this cycle. The P1 typed-`rank:` migration routes around it (explicit token wins), but the linter should be fixed (match the leading inline-code token on the first non-empty §Status line only, not a blob scan in resolution order) so untyped tail nodes are not mis-ranked during the incremental rollout. This is the concrete confirmation the campaign thesis asked for: the prose `## Status` is an unreliable second source-of-truth for a linter; the typed `rank:` token is the fix.
- **The campaign thesis is VALIDATED.** All 8 stale residual violations (+ the `L1/eigsolve` chain, +1) clear by installing the explicit `rank:` token — no hand-reconciliation of prose dep-maps was needed for any. Surface to batch-30 meta-phase as confirmation that the `edges:`/`rank:`-frontmatter-as-sole-truth migration is correct and that the `read_status_line` fallback is a transitional crutch to retire.
- **`solve_family -> solve-family-map-dissolution` is the sole GENUINE residual** (after cascade + retyping). It is a lowering-theme-maturity gap (firm L4 endpoint above a rough-in-tcb theme), out of my vocabulary-frontier scope → routed to D7 (baseline-exception set). D7 should re-verify the theme's live §Status with the leading-token rule before recording it as genuine vs another `read_status_line` false positive.
- **Reference-target existence caveats** (soft — references constrain nothing, a missing reference is a warning not a hard error): I referenced several L1>L0 theme slugs (`apply-linop-mutation-rotation`, `dot-mutation-rotation`, `nrm2-mutation-rotation`, `scal-mutation-rotation`, `normalize-mutation-rotation`, `matrix-weighted-norm-mutation-rotation`) and two forthcoming L2>L1 theme slugs (`inner-product-fold-specialization`, `linear-combination-fold-specialization`) by their conventional names. The integrator should verify exact filenames on disk; drop any reference whose target file does not exist (the `linear-combination-fold-specialization` theme is explicitly "does not yet exist" per the L2 prose). None of these are `depends-on` edges, so a missing target does not gate any rank.
- **Direct-vs-transitive discipline** (the D3 precedent, applied uniformly): I used the DIRECT dep set on every node and classified all cross-layer `lowers_to`/`lifts_from`/`lifts_to` identity-view edges as `reference`. Rationale: a same-operator adjacent-layer view is navigational, not a blocking constituent — classifying it `depends-on` would import the other layer's rank (e.g. the firm `L2/eigsolve` would inherit a false gate from the `partial-obstruction` `L3/eigsolve`). If the batch-30 meta-phase decides lowering edges SHOULD be `depends-on` (per scheme §4(a) "the lowering edge IS a depends-on on both endpoints" + the `apply_lowering_theme_ranks` machinery), that is a scheme clarification — flagged for awareness. The scheme §5 says THEMES carry the both-endpoint depends-on edges; an OPERATOR's edge to its own adjacent-layer self-view is the ambiguous case I resolved as `reference`.
- **L4/index count-header is the contested-ownership item I own this cycle** (per the brief). I did NOT touch `L1/index.md` (D1-owned) or any feature column (D5/D4-owned) or the cascade nodes' own status (D1/D3/D4). The `solve_family.md:154` re-anchor is a narrative-only edit (no status/frontmatter touch on `solve_family`), routed to me by D3's flag + the planner's L4-index ownership assignment.

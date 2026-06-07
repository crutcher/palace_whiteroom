---
agent: same-layer-cross-cutter
invoked_at: 2026-06-07T200334Z
scope: L4/L3/L2 cross-cut — sharding-MATH probe spine-stability cross-check (lateral/same-layer arm, D2)
status: pending
integrated_at: 2026-06-07T210000Z
integration_commit: 74d7357
integration_notes: "cycle-133 (batch-43 OPENER, 1/3). Applied clean by integrator-per-report — audit-class, NO book mutation. Verdict ALL-GREEN, ZERO-RED: no firm L4/L3/L2 reduce/fold combinator re-roots; the firm reduce primitives already carry the split/concatenation monoid-homomorphism, so partition-restriction is a DERIVED reference-class consumer (reduce∘restrict), NOT a re-root (domain_energy_reduce the precedent). DISCHARGES-GREEN the D1 vertical-arm contingency → COMBINED gate CLEAR; WAVE-2 GREENLIT for c134. Promoted OQ sharding-math-non-destabilization-probe-lateral-arm-verdict. WAVE-2 tripwire recorded: reference-class-only edges to firm roots."
---

# CYCLE: L4/L3/L2 firm-combinator stability set — sharding-MATH decomposition-abstraction

## Summary

Cross-checked the firm L4/L3/L2 reduce/fold combinator cohort against the question D1's
cross-layer probe asks vertically: would a sharding / domain-decomposition abstraction force any
**firm** combinator to RE-ROOT (a rank or liveness regression on a firm node)? The answer from the
lateral arm is **NO firm node is RED** — the entire firm reduce/fold cohort is GREEN
(composable-by-`reference`, no re-root). The decisive finding: the firm reduce primitives **already
carry the exact mathematical content a decomposition abstraction needs** as standing firm laws —
`inner_product`'s split-additivity / shape-concatenation monoid-homomorphism
(`L3/inner_product.md:233-240`), `linear_combination`'s concatenation-homomorphism
(`L3/linear_combination.md:103`), and `gram`/`gram_reduce`'s concatenation-block / map-independence
laws (`L2/gram.md:154-159`, `L4/gram_reduce.md:119`). A partition-of-the-index-set restriction is a
**specialization / consumer** of those existing laws (`sub-domain-reduce = reduce ∘ restrict-to-block`),
expressible as a NEW node with `reference`-class edges to the firm verbs — exactly the
`domain_energy_reduce` precedent, which is itself a firm domain-restricted reduce verb that consumes
the firm primitives without having re-rooted any of them. The graded-stack baseline
(`rank_violations=0`, confirmed this dispatch) is preserved under every composition-by-reference path;
no firm node is touched. This data supports a **CLEAR** verdict on the lateral axis.

## Observation kind

**Shared sub-pattern** — the firm reduce/fold cohort already shares a single primitive
(the split/concatenation **monoid-homomorphism over the index set**) that IS the decomposition
abstraction's mathematical core; the sharding-math lands as a `reference`-class consumer of it, not a
re-rooting of it.

## Specific finding

### The firm reduce/fold cohort and its stability disposition

| firm node | layer | rank | decomposition-relevant standing law | disposition |
|---|---|---|---|---|
| `inner_product` | L4 | firm | split-additivity inherited unchanged (`L4/inner_product.md:147`) | **GREEN** |
| `inner_product` | L3 | firm | split-additivity / shape-concatenation monoid-homomorphism (`L3/inner_product.md:233-240`) | **GREEN** |
| `inner_product` | L2 | firm | authoritative §Algebraic-laws home of the homomorphism | **GREEN** |
| `linear_combination` | L4 | firm | concatenation-homomorphism (`L4` re-expresses through L3) | **GREEN** |
| `linear_combination` | L3 | firm | concatenation-homomorphism, monoid hom `([(α,t)],++,[]) → (Tensor,+,0)` (`L3/linear_combination.md:103`) | **GREEN** |
| `gram` | L2 | firm | concatenation block law (`L2/gram.md:154-159`) | **GREEN** |
| `gram_reduce` | L4 | firm | per-pair map-independence / list-homomorphism, "embarrassingly parallel over pairs" (`L4/gram_reduce.md:119,158`) | **GREEN** |
| `domain_energy_reduce` | L4 | firm | map-independence / concatenation-homomorphism over the DOMAIN set (`L4/domain_energy_reduce.md:147-152`) | **GREEN** (and is the precedent) |

### (1) `domain_energy_reduce` IS the domain-restriction precedent — YES, referenceable by name.

`domain_energy_reduce` (`L4/domain_energy_reduce.md`, firm c091) is a firm L4 verb whose entire
content is a **domain-restricted reduce**: each row folds `energyᵢ = ½⟨field, M_idx field⟩`, "the
[`matrix-weighted-norm`] squared radicand `⟨x, B x⟩` with `B = M_idx` the operator **restricted to one
domain attribute**" (`:57-59`). Its defining law is
"**Map-independence / concatenation-homomorphism** … `domain_energy_reduce (a ++ b) … =
domain_energy_reduce a … ++ domain_energy_reduce b …` — each row depends only on its own domain's
`(idx, M_idx)`; no inter-domain state. **Embarrassingly parallel over domains**" (`:147-152`). It
reaches firm by **referencing** the firm primitives `inner_product`/`matrix-weighted-norm`/
`participation_ratio` (frontmatter `reference:` list `:9-12`, `depends-on: L1/participation_ratio,
L1/matrix-weighted-norm` `:6-8`) — it folds them, it did NOT re-root them. A sub-domain-compose
abstraction is structurally the SAME move: a domain-indexed map of restricted reduces, referenceable
"BY NAME" as the existing domain-restriction precedent. Confirmed YES.

One nuance worth recording for the math: `domain_energy_reduce` explicitly disclaims
unconditional partition-of-unity — `Σ pᵢ = 1` is **config-conditional**, holding "ONLY when the
configured domain set **partitions the field's support**" (`:172-178`). This is *informative* for the
sharding-math: a sound decomposition abstraction must carry the partition precondition as an
**explicit hypothesis** (matching `domain_energy_reduce`'s `partition-coverage` variant axis,
`:16`), not assume it. It is not a re-root risk — it is a law the abstraction must state, which the
precedent already shows how to state.

### (2) Are the firm reduce/fold combinators closed under a partition-of-the-index-set restriction WITHOUT re-rooting? — YES.

This is the central question and the answer is unambiguous YES, because the closure law **already
exists, firm**, on each verb:

- **`inner_product`** — "**Split-additivity / shape-concatenation-homomorphism (the defining law).**
  `inner_product (x₁ ++ x₂) (y₁ ++ y₂) = inner_product x₁ y₁ + inner_product x₂ y₂` … a **monoid
  homomorphism** from `(shape-concatenated tensors, ++)` to `(Scalar, +)` … **This is what licenses
  parallel/blocked evaluation of the reduction**" (`L3/inner_product.md:233-238`). A partition of the
  index set into blocks `S = S₁ ⊔ S₂ ⊔ …` is precisely a `++`-decomposition; the homomorphism says the
  block reduces sum to the whole. The L4 entry carries it up "**unchanged**" (`L4/inner_product.md:147`),
  and the L3 entry records explicitly "**There is NO sequential obstruction** … the reduction over all
  independent positions of the shape group `S` is a parallel operation" (`L3/inner_product.md:206-207`).
- **`linear_combination`** — "**Concatenation-homomorphism (the defining law).**
  `linear_combination (a ++ b) = linear_combination a + linear_combination b` … a monoid homomorphism
  from `([(Scalar,Tensor)], ++, [])` to `(Tensor, +, zeros)`" (`L3/linear_combination.md:103`).
- **`gram` / `gram_reduce`** — "**Concatenation block law.** `gram dot (X ++ Y)` is the `2×2` block
  matrix … the basis-index-axis analogue of `inner_product`'s split-additivity" (`L2/gram.md:154-159`);
  `gram_reduce`'s "**Each grid entry is independent (the upper-triangle `map` is a list homomorphism)**
  … **embarrassingly parallel over pairs**" (`L4/gram_reduce.md:119,158`).

In every case the partition-restriction `restrict-to-block` composed with the verb yields a result the
verb's OWN firm law already describes. The decomposition abstraction is therefore a **derived consumer**
(`sub-domain-reduce := reduce ∘ restrict`) that attaches via `reference`-class edges — navigational,
free, non-rank-constraining, non-liveness-carrying per the graded-stack edge taxonomy (CLAUDE.md
§GRADED RESOLUTION LADDER: "`reference` (navigational, free)"). No `depends-on` edge from a firm node
to the new abstraction is created; the firm nodes' `rank(u) ≤ min(deps)` invariant is untouched.
Closure WITHOUT re-rooting: confirmed YES.

### (3) Any other firm combinator a decomposition-abstraction would touch — surveyed, none RED.

Scanned the broader firm cohort for any combinator whose semantics a decomposition would *force* to
change rather than *consume*:

- **`fold_solve` / `solve_family` / `iterate-while` / `krylov-step`** (firm iteration-structural L4
  combinators) — these thread a `SimState` carry through a stopping predicate/schedule
  (`L4/inner_product.md:50-56` contrasts them as the carry-bearing half). A decomposition that
  block-distributes the *operator-apply inside* a step body composes those step bodies unchanged
  (the apply is itself reference-composed); the iteration structure is agnostic to whether the inner
  reduce is blocked. No re-root: the carry monad is orthogonal to the index-set partition. **GREEN.**
- **`fe_assemble`** (firm L4 fold) — its element-wise assembly is already a per-element map (the
  libCEED quadrature note, `L4/fe_assemble.md`); a mesh-block partition is the same map over a
  sub-mesh. Reference-composable. **GREEN** (no re-root; the impl/API kernel distinction is unaffected).
- The IEEE-754 **non-associativity non-law** (`L3/inner_product.md:267-274`,
  `L3/linear_combination.md:113-117`) is the ONE place to flag for the math, NOT as a re-root but as a
  **caveat the abstraction inherits**: the value-level homomorphism that licenses block reduction is
  exact-arithmetic; bit-identical reproduction across a re-blocked reduction tree is a load-bearing
  numerical concern already deferred to the L2>L1 fusion-selection themes. A sharding abstraction that
  changes the reduction-tree shape changes the pinned summation order — this is documented-but-not-a-law
  at the algebra level and is the correct, already-existing home for the concern. It does not regress a
  firm node; it is a property the new node must carry forward (as `domain_energy_reduce` and the
  primitives already do).

## Recommendation

**Defer to plan as the CLEAR-lateral input to the gated sharding-MATH probe (batch-43 LEAD WAVE-1).**
The lateral stability set is **all-GREEN, zero-RED**: no firm L4/L3/L2 combinator must re-root for a
decomposition-abstraction. The math should be authored as a `roadmap_goal`-class node (or a thin
concept page) that **references** the existing firm homomorphism laws BY NAME
(`inner_product` split-additivity, `linear_combination` concatenation-homomorphism, `gram` block law,
`domain_energy_reduce` as the domain-restriction precedent) rather than re-stating them — the
SEMANTIC-CONSOLIDATION USE+LINK discipline applies: **the homomorphism law lives ONCE on the verbs; the
sharding abstraction USES + LINKS, it does not RE-STATE.** If the probe proceeds:
- Route the abstraction node's authoring to the harvester/abstractor with **`reference`-class-only
  edges to the firm roots** (hard constraint — a `depends-on` edge from any firm node to the new
  abstraction would be the RED tripwire).
- Flag for the meta-phase: the partition-of-unity precondition is a **stated hypothesis**, mirroring
  `domain_energy_reduce`'s `partition-coverage` axis — not an unconditional law.

## Supporting evidence

- `book/src/L4/domain_energy_reduce.md:57-59,147-152,172-178,16` — the firm domain-restricted reduce
  precedent: domain-restricted energy form, map-independence/concatenation-homomorphism law,
  config-conditional partition-of-unity, `partition-coverage` variant axis. Frontmatter `:6-12` —
  `depends-on` + `reference` edge structure (folds firm primitives, re-roots none).
- `book/src/L3/inner_product.md:206-214,233-240,267-274` — no-sequential-obstruction verdict;
  split-additivity / shape-concatenation monoid-homomorphism (the closure-under-partition law);
  IEEE-754 non-associativity non-law (the inherited caveat).
- `book/src/L4/inner_product.md:147` — split-additivity carried up unchanged to L4 (firm).
- `book/src/L3/linear_combination.md:103,113-117` — concatenation-homomorphism defining law; the
  exact-arithmetic permutation-invariance + its IEEE-754 deferred non-law.
- `book/src/L2/gram.md:154-159` — concatenation block law (basis-index analogue of split-additivity).
- `book/src/L4/gram_reduce.md:119,158` — per-pair map-independence / list-homomorphism, embarrassingly
  parallel over pairs.
- `tools/graded-stack-lint/graded_stack_lint.py --book-src book/src` (run this dispatch):
  `RESULT: 0 rank violation(s)` — the baseline invariant the cross-check protects, confirmed intact.

## Open questions / caveats

- **D1 dependency:** this lateral verdict (no firm node re-roots) is the within-spine complement to
  D1's cross-layer verdict (does the *stack* destabilize?). The combined CLEAR/NO-CLEAR gate decision
  rests on BOTH arms; this report supplies only the lateral (firm-node-re-root) data.
- **`reference`-edge-only is the hard tripwire:** the GREEN verdict holds **conditionally on the
  abstraction being authored with `reference`-class edges to firm roots.** If a future author wires a
  `depends-on` edge FROM a firm node TO the (lower-rank) decomposition abstraction, that would itself
  manufacture a rank violation (`rank(firm-node)=3 > rank(roadmap_goal)=0`) — the RED outcome the
  hard-gate forbids. The disposition is GREEN *for the correct edge-typing*; the linter would catch a
  mistyped edge.
- **IEEE-754 reduction-tree pinning** is not a re-root but is the one genuine load-bearing numerical
  caveat a re-blocking decomposition touches; verify the abstraction inherits the existing L2>L1
  fusion-selection deferral rather than asserting a fresh associativity law.
- Citations are line-anchored to current on-disk content this dispatch; no citecheck `--anchor` tool
  run against `reference/palace/` was needed (no NEW L0 claims — this is a within-book firm-cohort
  audit), but the book-internal line refs above were read directly this dispatch.

---
layer: L4
operator: sharding-decompose-reduce
rank: roadmap_goal
status: roadmap_goal
edges:
  reference:
    - L4/domain_energy_reduce
    - L4/inner_product
    - L4/linear_combination
    - L4/gram_reduce
    - L2/gram
intent: >
  The sharding-as-decomposition-abstraction MATH: a rank-agnostic
  `subdomain_reduce = reduce ∘ restrict-to-block` combinator pair (restrict a
  field/operator to an index-set block; recover the global reduction by the firm reduce
  verbs' standing concatenation-homomorphism over a PARTITION of the index set), plus the
  per-sub-domain SOLVE decomposition it generalizes to. The speculative future-direction
  abstraction the batch-43 (C) sharding-MATH gate authorizes — the MATH of decomposition,
  NOT the message-passing.
pulled_by:
  - human batch-43 (C) directive (open the deferred sharding-MATH gate; gated-first, exploratory-only)
  - c133 WAVE-1 hard non-destabilization probe CLEARED (both arms; the firm reduce verbs already carry the homomorphism law)
---

# sharding-decompose-reduce

> **⟢ STATUS: `roadmap_goal` (rank 0) — a claim-free FUTURE-DIRECTION sketch, NOT active
> vocabulary.** This chapter records the sharding-as-decomposition-abstraction MATH the
> batch-43 (C) gate authorizes as an *exploratory* direction. It asserts NO claims; every
> form below is explicitly speculative. It composes firm roots under `reference:` ONLY (no
> `depends-on`) — a rank-0 node may reference firm nodes freely, but a `depends-on` edge
> from this node to a firm (rank-3) node would manufacture a rank violation. MPI/distributed
> mechanics are the deferred-future *mechanism*, cited but NOT lifted (DIRECTIVE-1). This is
> the MATH of decomposition, NOT the message-passing.

The intended **sharding-as-decomposition-abstraction**: split a global tensor-field reduction
(or solve) over a **partition of its index set** into per-block sub-problems, run the firm
reduce/solve verb on each block independently, and recover the global result by the firm
verbs' **standing concatenation-homomorphism**. The core abstraction is the combinator pair

```text
-- SPECULATIVE (roadmap_goal) — restrict a field/operator to one index-set block:
restrict_to_block :: IndexBlock                  -- a block b of a partition P of the index set
                  -> Tensor[(S: ...)]            -- the global field over shape group S
                  -> Tensor[(Sb: ...)]           -- the field restricted to block b (sub-shape Sb ⊑ S)

-- SPECULATIVE (roadmap_goal) — the decomposed reduction over a partition P = {b₀, b₁, …}:
subdomain_reduce :: (Tensor[(Sb: ...)] -> r)     -- a firm reduce verb (inner_product / gram / domain_energy …)
                 -> Partition                    -- P : a partition of the index set into blocks
                 -> Tensor[(S: ...)]             -- the global field
                 -> r                             -- the GLOBAL reduction, recovered homomorphically
subdomain_reduce reduce P field =
  mconcat [ reduce (restrict_to_block b field) | b <- blocks P ]   -- fold the per-block results in r's monoid
```

i.e. **`subdomain_reduce = mconcat ∘ map (reduce ∘ restrict_to_block) ∘ blocks`** — a
partition of the index set is a `++`-decomposition the firm reduce verbs' homomorphism law
**already describes**, so the global result is recovered with no new reduction algebra.

## Context — why this is non-destabilizing (the c133 gate-CLEAR, recorded)

L4 is **vocabulary** (`L4/index.md:7-13`). This roadmap_goal records the sharding-MATH the
batch-43 (C) directive opens, GATED behind the c133 hard non-destabilization probe, which
CLEARED on both arms:

- **Vertical arm (general abstraction non-destabilizing).** The general decomposition-reduce
  abstraction does not re-root the spine: the firm [`domain_energy_reduce`](./domain_energy_reduce.md)
  is the structural PRECEDENT — it is *itself a firm domain-RESTRICTED reduce composing firm
  primitives* (its per-domain numerator `energyᵢ = ½⟨field, M_idx field⟩` is the
  `matrix-weighted-norm`-squared *restricted to one domain attribute*, mapped over the
  configured domain set with no inter-domain state;
  `domain_energy_reduce.md:21-27,147-152`). `subdomain_reduce` is the rank-agnostic
  generalization of exactly that shape: restrict, reduce per block, compose.
- **Lateral arm (ALL-GREEN / ZERO-RED).** The firm reduce primitives ALREADY carry the
  split/concatenation **monoid-homomorphism over the index set** as standing firm laws — so a
  partition-of-the-index-set restriction is a DERIVED consumer, not a re-root:
  - [`inner_product`](./inner_product.md):154-157 — *split-additivity / shape-concatenation-homomorphism*
    (the defining law): `inner_product (x₁ ++ x₂) (y₁ ++ y₂) = inner_product x₁ y₁ + inner_product x₂ y₂`,
    "a monoid homomorphism from `(shape-concatenated tensors, ++)` to `(Scalar, +)`";
  - [`linear_combination`](./linear_combination.md):146-151 — *concatenation-homomorphism*
    (the defining law): `linear_combination (a ++ b) = linear_combination a + linear_combination b`,
    "a monoid homomorphism from `([(Scalar,Tensor)], ++, [])` to `(Tensor[$S], +, zeros)`";
  - [`gram_reduce`](./gram_reduce.md):119-120 — each grid entry independent, "the upper-triangle
    `map` is a list homomorphism" over the family-pair grid (a per-pair map-homomorphism);
  - [`domain_energy_reduce`](./domain_energy_reduce.md):147-152 — the *map-independence /
    concatenation-homomorphism* fold law: `domain_energy_reduce (a ++ b) field e_total =
    domain_energy_reduce a … ++ domain_energy_reduce b …`, "embarrassingly parallel over
    domains".

  The reduce verbs are monoid homomorphisms `(index-concatenated input, ++) → (result, ⊕)`.
  A **partition** `P` of the index set is precisely a `++`-decomposition into disjoint blocks;
  `reduce` over the whole index set equals `mconcat` of `reduce` over each block. The
  homomorphism IS the recovery law — already firm, already stated. `subdomain_reduce` adds NO
  new reduction algebra; it is `reduce ∘ restrict-to-block` plus the existing homomorphic
  recovery.

The combinator is sketched **in L4 vocabulary** (high→low discipline): the speculative forms
are stated in terms of the index-set partition, the per-block restriction, and the firm reduce
verb each invocation closes over — NOT in terms of any C++ partitioning loop.

## Speculative semantics (roadmap_goal — NO claims)

`subdomain_reduce reduce P field` partitions the field's index set into the blocks of `P`,
restricts the field to each block, runs the closed-over firm reduce verb on each restricted
sub-field independently, and folds the per-block results in the verb's result monoid. The
*generalization beyond reduction* — the eventual point of "sharding" — is that the same
restrict/compose shape covers a per-sub-domain **solve** (each block's restricted operator and
RHS form an independent sub-problem; the global state is recovered by composing the per-block
solutions across the partition, with overlap/interface handling supplied by the eventual
mechanism), and a per-sub-domain **assemble** (the firm `fe_assemble` fold over a block-local
element set). These generalizations are SPECULATIVE intent recorded for the accreting working
context, NOT asserted; only the reduction case has the firm homomorphism law in hand today.

The intended structural payoff: a global tensor-field reduction/solve over an index set is
re-expressible as the composition of independent per-block sub-reductions/sub-solves — the
mathematical content of "sharding into component blocks" — with the global result recovered by
a law the spine ALREADY holds firm, so the abstraction sits ON TOP of the firm vocabulary
rather than reshaping it.

## Speculative algebraic laws (roadmap_goal — intent, not asserted)

These are the laws the abstraction WOULD carry; they are stated as the target shape, NOT as
established claims. Each is intended to be a DERIVED consequence of a standing firm law, which
is the whole point of the gate-CLEAR (no NEW algebra):

1. **Homomorphic recovery over a partition (the intended defining law, DERIVED).** For a
   partition `P = {b₀, …, b_{k−1}}` of the index set, `subdomain_reduce reduce P field =
   reduce field` — the per-block results compose (in the verb's result monoid) to the global
   reduction. This is intended to be a DIRECT consequence of the firm concatenation-homomorphism
   (`inner_product.md:154-157`, `linear_combination.md:146-151`,
   `domain_energy_reduce.md:147-152`): a partition is a `++`-decomposition, and the firm verb
   is a monoid homomorphism over `++`. No new reduction algebra — the recovery IS the existing
   homomorphism applied to the partition's blocks.
2. **Block-order / re-partition invariance (intended, DERIVED from monoid commutativity).**
   When the result monoid is commutative (`(Scalar, +)` for `inner_product`/`domain_energy`;
   `(Tensor, +)` for `linear_combination`), the global result is independent of block order
   and of which partition is chosen — any partition recovers the same global reduction. The
   `domain_energy_reduce.md:150-152` "embarrassingly parallel over domains" property is the
   per-domain instance.
3. **Restriction is a partition map (intended).** `restrict_to_block` over the blocks of a
   partition is intended to be a partition of the global shape group `S` into disjoint
   sub-shapes `{Sb}` with `⊎ Sb = S` — the structural precondition the recovery law rests on.

### Laws that explicitly do NOT hold (config-conditional NON-laws — carried, not asserted)

Following how [`domain_energy_reduce.md`](./domain_energy_reduce.md):147-152,172-178 carries
its partition-coverage non-law:

- **Partition-of-unity / disjoint-and-exhaustive coverage is a CONFIG-CONDITIONAL NON-LAW,
  not a structural claim.** The homomorphic-recovery law (law 1) holds ONLY when the blocks
  `{b}` actually PARTITION the index set — disjoint AND exhaustive (`⊎ b = S`). Just as
  `domain_energy_reduce`'s `Σ pᵢ = 1` is config-conditional on the configured domains
  partitioning the field support (`domain_energy_reduce.md:172-178`: overlapping ⇒ double-count,
  partial ⇒ under-count), a sharding decomposition that OVERLAPS blocks double-counts on the
  intersections and a decomposition that LEAVES GAPS under-counts. The abstraction makes NO
  partition-of-unity claim of its own; a coverage precondition gates the recovery law. (For a
  general overlapping domain decomposition — additive Schwarz and friends — the recovery
  requires a partition-of-unity weighting on the overlaps; that weighting is the eventual
  *mechanism*, NOT a structural law of the bare abstraction.)
- **No cross-block state.** The decomposition runs each block independently with no inter-block
  carry (the `domain_energy_reduce.md:147-152` map-independence property generalized). Any
  interface/halo coupling between blocks is supplied by the eventual mechanism (the deferred
  MPI realization), NOT by this abstraction — the bare MATH is the embarrassingly-parallel
  decomposition; the coupling is mechanism.

## Declared dependencies (the well-foundedness target, when this promotes)

As a `roadmap_goal` (rank 0) this node `reference`s the firm roots it composes; it does NOT
`depends-on` them (a rank-0 → rank-3 `depends-on` would violate `rank(u) ≤ min(deps)`). The
firm roots it composes (the eventual `depends-on` set IF/WHEN a real consumer pulls this to a
higher rank and the well-foundedness invariant is re-checked at that rank):

- [`domain_energy_reduce`](./domain_energy_reduce.md) (firm) — the STRUCTURAL MODEL: a firm
  domain-restricted reduce composing firm primitives, the precedent shape `subdomain_reduce`
  generalizes.
- [`inner_product`](./inner_product.md) (firm) — carries the split-additivity /
  shape-concatenation monoid-homomorphism (`:154-157`), the reduce-to-scalar recovery law.
- [`linear_combination`](./linear_combination.md) (firm) — carries the concatenation-homomorphism
  (`:146-151`), the reduce-to-tensor recovery law.
- [`gram_reduce`](./gram_reduce.md) (firm) — the per-pair map-homomorphism reduce (`:119-120`),
  the reduce-to-matrix family-grid case.
- [`gram`](../L2/gram.md) — the L2 Gram form underneath the family-pair reduction.

## Accreting working context (the roadmap_goal's open surface)

- **The deferred-future MECHANISM (cited, NOT lifted — DIRECTIVE-1).** When/if this abstraction
  is realized for actual distributed execution, the realization path is Palace's existing
  MPI/distributed machinery — recorded here as the eventual mechanism, explicitly OUT of active
  scope (the MPI-associated version may be DESTRUCTIVE to the current abstraction spine, so it
  is NOT lifted now):
  - **Mesh / index-set partitioning.** `Partition(IoData &, std::unique_ptr<mfem::Mesh>, MPI_Comm)`
    (`palace/utils/geodata.cpp:262`) builds the distributed mesh from a serial mesh + a
    partitioning; `GetMeshPartitioning(const mfem::Mesh &, int size, …)`
    (`palace/utils/geodata.cpp:3230-3242`) generates the element-to-block assignment (METIS
    `GeneratePartitioning`, `:3239`). This is the mechanism that produces the `Partition P`
    the abstraction is parameterized over — the index-set decomposition the MATH assumes given.
  - **The parallel-assembly / RAP operator.** `class ParOperator : public Operator`
    (`palace/linalg/rap.hpp:24`) and its `R·A·P` Galerkin triple product
    (`palace/linalg/rap.cpp:116-126`, the `hypre_ParCSRMatrixRAPKT` / `hypre_ParCSRMatMat`
    assembly) is the mechanism that realizes a distributed operator over the partition. This is
    the eventual realization of "restrict an operator to a block and compose"; the bare
    abstraction's `restrict_to_block` on operators corresponds to it.
  - **The MPI collectives** (the global reduction's communication leg) are the mechanism behind
    the homomorphic `mconcat` across blocks — the `++ → ⊕` fold the firm verbs' homomorphism
    law describes mathematically, realized as a collective sum/gather. Out of scope per CLAUDE.md
    §Scope (read single-rank); cited here as the eventual realization of law 1's fold.
- **The per-sub-domain SOLVE generalization** (the eventual point beyond reduction). The
  restrict/compose shape is intended to generalize from reduce to solve (additive-Schwarz-style
  domain decomposition as a preconditioner/solver). This is SPECULATIVE — the firm homomorphism
  law in hand today covers the REDUCTION case; the solve case needs the interface/overlap
  handling (partition-of-unity weighting, the deferred mechanism) and is recorded as open intent,
  NOT asserted. A real NLEPS-deflated / domain-decomposition preconditioner consumer would be the
  pull that promotes this from roadmap_goal toward a real rank.
- **Open: the sharding-into-component-blocks future GOAL.** The batch-43 (C) directive records
  sharding-into-component-blocks as a FUTURE GOAL behind a hard spine-non-destabilization gate.
  This chapter is the gated MATH-only sketch; the component-block sharding proper (with the
  destructive MPI lifetime structure) remains a deferred future direction, NOT active work.

## Status

`roadmap_goal` (rank 0) — a claim-free FUTURE-DIRECTION sketch. **This is the
sharding-as-decomposition-abstraction MATH ONLY** — the math of decomposition
(`subdomain_reduce = reduce ∘ restrict-to-block`, recovered by the firm verbs' standing
concatenation-homomorphism over a partition of the index set), NOT the message-passing. It
asserts no claims; the laws above are the intended target shape, derived (when realized) from
firm laws already in the spine. It composes the firm roots under `reference:` ONLY — NEVER
`depends-on` — so it manufactures no rank violation (the baseline `rank_violations=0` holds;
the graded-stack rank linter enforces `rank(u) ≤ min(deps)` over `depends-on` edges only, and a
`reference` edge carries no rank constraint). The deferred MPI/distributed mechanism is cited
as the eventual realization path, NOT lifted (DIRECTIVE-1: lifting the MPI-associated version
may be destabilizing to the abstraction spine). Promotion route: a real single-machine-valid
consumer (a domain-decomposition preconditioner / additive-Schwarz solver leg) pulling the
restrict/compose abstraction by name, at which point the `reference` edges are re-examined for
which become blocking `depends-on` at the consumer's rank and the well-foundedness invariant is
re-checked.

**Pulled-by provenance (the reachability requirement).** This roadmap_goal is pulled by the
human batch-43 (C) directive (open the deferred sharding-MATH gate, gated-first, exploratory)
and authorized by the c133 WAVE-1 hard non-destabilization probe CLEAR (both arms). Its
reference edges reach the firm reduce roots, which are reachable from the feature-surface spine
roots (the output-product columns compose `domain_energy_reduce` / `gram_reduce` /
`inner_product`); the abstraction's eventual blocking consumer (a domain-decomposition solver
leg) would reach the solver-driver roots. Recorded as exploratory future-direction intent per
the gated-first, no-rank/liveness-regression-on-firm-nodes constraint.

## Evidence

All Palace L0 citations self-verified on-disk this dispatch via
`tools/citecheck/citecheck.py --anchor` (against `reference/palace/`). The book cross-references
are to firm sibling chapters' standing laws.

- **Structural model (the firm domain-restricted reduce precedent):**
  [`domain_energy_reduce`](./domain_energy_reduce.md):21-27 (a domain-RESTRICTED SPD energy
  reduction composing firm primitives), :147-152 (the map-independence /
  concatenation-homomorphism fold law — "embarrassingly parallel over domains"), :172-178 (the
  config-conditional partition-of-unity NON-law model this chapter follows).
- **Firm concatenation / split homomorphism laws (the lateral-arm gate-CLEAR basis):**
  [`inner_product`](./inner_product.md):154-157 (split-additivity / shape-concatenation monoid
  homomorphism), [`linear_combination`](./linear_combination.md):146-151
  (concatenation-homomorphism), [`gram_reduce`](./gram_reduce.md):119-120 (per-pair
  map-homomorphism over the family grid).
- **Deferred MPI/distributed MECHANISM (cited as eventual realization path, NOT lifted —
  DIRECTIVE-1):**
  - `palace/utils/geodata.cpp:262` (`Partition(IoData &, std::unique_ptr<mfem::Mesh>, MPI_Comm)`
    — the distributed-mesh builder; the eventual source of the partition `P`),
    `:3230-3242` (`GetMeshPartitioning(const mfem::Mesh &, int size, …)` — METIS
    `GeneratePartitioning` at `:3239`, the element-to-block assignment).
  - `palace/linalg/rap.hpp:24` (`class ParOperator : public Operator` — the distributed-operator
    type), `palace/linalg/rap.cpp:116-126` (the `R·A·P` Galerkin triple product assembly,
    `hypre_ParCSRMatrixRAPKT` / `hypre_ParCSRMatMat` — the eventual operator-restriction-and-compose
    mechanism).
- **Gate provenance:** c133 WAVE-1 hard non-destabilization probe CLEARED (vertical arm:
  general decomposition-reduce non-destabilizing, `domain_energy_reduce` the structural
  precedent; lateral arm: ALL-GREEN/ZERO-RED, the firm reduce verbs already carry the
  homomorphism law). Human batch-43 (C) directive: open the deferred sharding-MATH gate,
  gated-first, exploratory-only (roadmap_goal-class, reference-class edges to firm roots, no
  rank/liveness regression on firm nodes); MPI/distributed STAYS OUT.

```yaml
verified_against:
  - citation: book/src/L4/domain_energy_reduce.md:21-27,147-152,172-178
    verdict: supports
    audited_at: 2026-06-07T203807Z
    note: structural model — a firm domain-RESTRICTED reduce composing firm primitives; carries the map-independence/concatenation-homomorphism fold law + the config-conditional partition-of-unity NON-law this chapter follows
  - citation: book/src/L4/inner_product.md:154-157
    verdict: supports
    audited_at: 2026-06-07T203807Z
    note: firm split-additivity / shape-concatenation monoid-homomorphism — the reduce-to-scalar recovery law a partition's ++-decomposition rides; the lateral-arm gate-CLEAR basis
  - citation: book/src/L4/linear_combination.md:146-151
    verdict: supports
    audited_at: 2026-06-07T203807Z
    note: firm concatenation-homomorphism — the reduce-to-tensor recovery law
  - citation: reference/palace/palace/utils/geodata.cpp:262
    verdict: supports
    audited_at: 2026-06-07T203807Z
    note: Partition(IoData&, unique_ptr<Mesh>, MPI_Comm) — the deferred distributed-mesh builder (eventual source of partition P); cited as MECHANISM, NOT lifted (citecheck --anchor ok)
  - citation: reference/palace/palace/utils/geodata.cpp:3230-3242
    verdict: supports
    audited_at: 2026-06-07T203807Z
    note: GetMeshPartitioning — METIS GeneratePartitioning element-to-block assignment; deferred MECHANISM (citecheck --anchor ok)
  - citation: reference/palace/palace/linalg/rap.hpp:24
    verdict: supports
    audited_at: 2026-06-07T203807Z
    note: class ParOperator — the distributed-operator type; deferred MECHANISM, NOT lifted (citecheck --anchor ok)
  - citation: reference/palace/palace/linalg/rap.cpp:116-126
    verdict: supports
    audited_at: 2026-06-07T203807Z
    note: R·A·P Galerkin triple product assembly (hypre_ParCSRMatrixRAPKT / hypre_ParCSRMatMat) — eventual operator-restrict-and-compose MECHANISM (citecheck --anchor ok)
```

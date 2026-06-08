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
    - L4/ksp_solve
    - L4/fold_solve
    - L4/krylov-step
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

## The SOLVE generalization (the additive-Schwarz decomposition-abstraction — roadmap_goal, NO claims)

The eventual point of "sharding" is not reduction but **solve**: the same restrict / per-block /
compose shape generalizes from a reduce verb to a SOLVE verb. The speculative combinator is

```text
-- SPECULATIVE (roadmap_goal) — restrict an OPERATOR to one index-set block (the operator analog
-- of restrict_to_block; the eventual realization is the RAP Galerkin restriction, DEFERRED mechanism):
restrict_op_to_block :: IndexBlock                       -- a block b of a partition P of the index set
                     -> LinOp[(S: ...), $S]              -- the global square system operator A
                     -> LinOp[(Sb: ...), $Sb]            -- A restricted to block b (sub-shape Sb ⊑ S)

-- SPECULATIVE (roadmap_goal) — the decomposed solve over a partition P = {b₀, b₁, …}:
subdomain_solve :: (LinOp[(Sb: ...), $Sb] -> Tensor[(Sb: ...)] -> Solve (Tensor[$Sb]))
                                                         -- a firm solve verb (ksp_solve / fold_solve / krylov-step)
                 -> Partition                            -- P : a partition of the index set into blocks
                 -> LinOp[(S: ...), $S]                  -- the global system operator A
                 -> Tensor[(S: ...)]                     -- the global RHS
                 -> Solve (Tensor[$S])                   -- the GLOBAL solution, recovered by homomorphic compose
subdomain_solve solve P a rhs =
  compose_partition P                                    -- p.o.u.-weighted compose over the partition (see NON-laws)
    [ solve (restrict_op_to_block b a) (restrict_to_block b rhs) | b <- blocks P ]
```

i.e. **`subdomain_solve = compose_partition ∘ map (solve ∘ restrict-to-block-operator+rhs) ∘ blocks`**
— restrict the operator and RHS to each block, run the firm solve verb on each independent
sub-problem, and recompose the per-block solutions across the partition. The `solve` argument is the
firm solve verb the invocation closes over — [`ksp_solve`](./ksp_solve.md) (the preconditioned-Krylov
outer solve), [`fold_solve`](./fold_solve.md) (the iteration-fold driver), or
[`krylov-step`](./krylov-step.md) (one Krylov step) — each composed BY NAME, none re-rooted.

This is the structural shape of **additive-Schwarz domain decomposition** read as a pure
decomposition-abstraction: the partition `P` supplies the sub-domains, `restrict_op_to_block` /
`restrict_to_block` supply the per-sub-domain sub-problems, the firm solve verb solves each
independently, and `compose_partition` recovers the global state. The combinator is sketched **in L4
vocabulary** (high→low discipline): the speculative forms are stated in terms of the index-set
partition, the per-block operator/RHS restriction, and the firm solve verb each invocation closes
over — NOT in terms of any Palace Schwarz loop (Palace ships none; see §Status).

> **The crucial asymmetry from the reduce case (the honest law-strength, NOT a forced free law).**
> The reduce case (`subdomain_reduce`) rides a law the firm reduce verbs ALREADY hold firm (the
> concatenation-homomorphism), so its recovery is EXACT and FREE. The solve case has **NO analogous
> free law**: `solve (A|_b, rhs|_b)` per block recovers the exact global `solve(A, rhs)` ONLY when `A`
> is **block-diagonal** w.r.t. the partition (zero inter-block coupling). For a general coupled global
> operator, the bare restrict/solve/compose is an **APPROXIMATE** recovery — precisely the
> additive-Schwarz PRECONDITIONER, a convergent OUTER ITERATION, not a one-shot identity. The
> exactness gap IS the inter-block coupling, corrected by overlap + partition-of-unity weighting. This
> asymmetry is carried below as an explicit config-conditional NON-law (mirroring
> [`domain_energy_reduce`](./domain_energy_reduce.md)'s `partition-coverage` / `Σ pᵢ = 1` non-law),
> NOT papered over with a false homomorphic-solve claim.

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

For the SOLVE case specifically, the per-block sub-solves are independent (embarrassingly parallel
over blocks, the same map-independence the reduce case has), but the global RECOVERY is
config-conditional on the operator's block structure: exact for a block-diagonal operator, approximate
(an additive-Schwarz preconditioner / iteration leg) for a coupled operator. `subdomain_solve` sits
ON TOP of the firm solve verbs as an OUTER combinator over the partition — it reshapes none of them; it
calls `ksp_solve` / `fold_solve` / `krylov-step` per block exactly as written, and supplies only the
restrict/compose wrapper. That is the whole-point of the gate-CLEAR: the solve-generalization adds an
outer decomposition layer, NOT new solve algebra inside the firm verbs.

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
4. **Per-block solve independence (the SOLVE-case map-independence, intended).** For a partition
   `P`, the per-block sub-solves `solve (A|_b, rhs|_b)` are mutually independent — no inter-block
   state threads between sub-solves (the `domain_energy_reduce.md:147-152` map-independence property
   carried to the solve case). Embarrassingly parallel over blocks. This is the part the solve case
   DOES share with the reduce case; the part it does NOT is the recovery (law 5, config-conditional).
5. **Block-diagonal exact-recovery (the SOLVE-case recovery, CONFIG-CONDITIONAL — intended, NOT free).**
   `subdomain_solve solve P A rhs = solve A rhs` (the exact global solution) holds ONLY when the global
   operator `A` is **block-diagonal** w.r.t. the partition `P` (zero inter-block coupling) — then each
   block's sub-problem is independent and a trivial `compose_partition` (disjoint concatenation)
   recovers the exact global solve. This is the SOLVE analog of the reduce-case homomorphic recovery
   (law 1) BUT it is NOT a free standing law — it is gated on the operator's block structure (see the
   NON-laws). For a coupled operator the equality becomes an APPROXIMATION (additive-Schwarz
   preconditioner), recovered only in the limit of the outer Schwarz iteration. NO new solve algebra is
   introduced inside the firm verbs; the recovery is the OUTER compose, which is exact only in the
   block-diagonal config.

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
- **SOLVE exact-recovery is a CONFIG-CONDITIONAL NON-LAW (block structure + partition-of-unity), the
  sharper sibling of the reduce-case partition-of-unity non-law.** Just as the reduce case's
  homomorphic recovery (law 1) holds only when the blocks PARTITION the index set, the solve case's
  exact-recovery (law 5) holds only when the global operator is **block-diagonal** w.r.t. the
  partition. The two ways it fails are EXPLICIT preconditions the bare abstraction does NOT claim away:
  - **Inter-block coupling ⇒ approximation, not identity.** A coupled operator (off-block-diagonal
    entries — the generic FE-assembled system, where neighbouring elements share dofs) makes the bare
    restrict/solve/compose an additive-Schwarz PRECONDITIONER: a convergent outer iteration, NOT a
    one-shot exact solve. The abstraction makes NO exact-solve claim for a coupled operator; the
    convergent recovery is the eventual *mechanism* (the outer Schwarz/Krylov iteration wrapping the
    per-block solves — itself one of the firm [`fold_solve`](./fold_solve.md) /
    [`krylov-step`](./krylov-step.md) drivers at the OUTER level), NOT a structural law of the bare
    decomposition.
  - **Overlapping blocks ⇒ partition-of-unity weighting required.** For an OVERLAPPING domain
    decomposition (additive Schwarz proper, where blocks share a halo region for stability), the
    recompose must apply a **partition-of-unity weighting** on the overlaps — `Σ χ_b = 1` over the
    overlap, the χ_b weights summing to one — so the shared dofs are not double-counted. This is the
    EXACT solve-side analog of `domain_energy_reduce`'s `Σ pᵢ = 1` config-conditional non-law
    (`domain_energy_reduce.md:172-178`: overlapping ⇒ double-count, partial ⇒ under-count): an
    overlapping solve decomposition double-counts the halo without the p.o.u. weights, and a gappy
    decomposition leaves dofs unsolved. The bare abstraction makes NO partition-of-unity claim; the
    p.o.u. weighting + overlap halo is the eventual *mechanism* gating the recovery, NOT a structural
    law. `compose_partition` is written to CARRY the p.o.u. weighting as its config parameter precisely
    so the non-law is explicit at the combinator boundary, not hidden.

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
  restrict/compose shape generalizes from reduce to solve as **`subdomain_solve = compose_partition ∘
  map (solve ∘ restrict-to-block-operator+rhs)`** — additive-Schwarz-style domain decomposition (see
  the §"The SOLVE generalization" combinator above), composing the firm solve verbs
  [`ksp_solve`](./ksp_solve.md) / [`fold_solve`](./fold_solve.md) / [`krylov-step`](./krylov-step.md)
  BY NAME. The firm homomorphism law in hand today gives the REDUCTION case a free exact recovery; the
  solve case's recovery is config-conditional (block-diagonal ⇒ exact; coupled ⇒ an approximate
  additive-Schwarz preconditioner needing the outer iteration; overlapping ⇒ needs partition-of-unity
  weighting — the §"Laws that explicitly do NOT hold" non-laws). The interface/overlap handling
  (partition-of-unity χ_b weights, the halo, the convergent outer Schwarz iteration) is the deferred
  *mechanism*, recorded as open intent, NOT asserted. A real single-machine-valid domain-decomposition
  preconditioner consumer (a Schwarz preconditioner / DD solver leg pulling `subdomain_solve` by name)
  would be the pull that promotes this from roadmap_goal toward a real rank — the
  `...solve-generalization-promotion-pull` OQ, which STAYS DEFERRED (no such consumer in flight this
  cycle; this extension is the gated, exploratory MATH-only sketch). Palace ships NO native
  additive-Schwarz / domain-decomposition preconditioner (the only `subdomain`/`overlap` source sites
  are the MPI mesh-partitioning `geodata.cpp:3242` and the wave-port ROM overlap `romoperator.cpp:586`,
  neither a DD solver) — so this solve-generalization is a genuine decomposition-abstraction sketch,
  NOT a lift of existing Palace solver code.
- **Open: the sharding-into-component-blocks future GOAL.** The batch-43 (C) directive records
  sharding-into-component-blocks as a FUTURE GOAL behind a hard spine-non-destabilization gate.
  This chapter is the gated MATH-only sketch; the component-block sharding proper (with the
  destructive MPI lifetime structure) remains a deferred future direction, NOT active work.

## Status

`roadmap_goal` (rank 0) — a claim-free FUTURE-DIRECTION sketch. **This is the
sharding-as-decomposition-abstraction MATH ONLY** — the math of decomposition
(`subdomain_reduce = reduce ∘ restrict-to-block` for the reduce case, and its solve generalization
`subdomain_solve = compose_partition ∘ map (solve ∘ restrict-to-block)` for the additive-Schwarz
solve case), recovered by the firm verbs' standing concatenation-homomorphism (reduce, exact/free) or
by a config-conditional block-diagonal/p.o.u. recovery (solve, approximate-for-coupled), NOT the
message-passing. It asserts no claims; the laws above are the intended target shape — the reduce-case
recovery is derived (when realized) from firm laws already in the spine, and the solve-case recovery is
explicitly config-conditional (block-diagonal exact; coupled ⇒ additive-Schwarz preconditioner;
overlapping ⇒ partition-of-unity weighted), carried as a NON-law in the exact shape
[`domain_energy_reduce`](./domain_energy_reduce.md) carries `Σ pᵢ = 1`. It composes the firm reduce AND
solve roots ([`ksp_solve`](./ksp_solve.md) / [`fold_solve`](./fold_solve.md) /
[`krylov-step`](./krylov-step.md) BY NAME) under `reference:` ONLY — NEVER `depends-on` — so it
manufactures no rank violation (the baseline `rank_violations=0` holds; the graded-stack rank linter
enforces `rank(u) ≤ min(deps)` over `depends-on` edges only, and a `reference` edge carries no rank
constraint). The deferred MPI/distributed mechanism (and the deferred Schwarz outer-iteration /
partition-of-unity mechanism) is cited as the eventual realization path, NOT lifted (DIRECTIVE-1:
lifting the MPI-associated version may be destabilizing to the abstraction spine; Palace ships no
native DD preconditioner to lift in any case). Promotion route: a real single-machine-valid consumer (a
domain-decomposition preconditioner / additive-Schwarz solver leg) pulling the restrict/compose
abstraction by name (the deferred `...solve-generalization-promotion-pull` OQ), at which point the
`reference` edges are re-examined for which become blocking `depends-on` at the consumer's rank and the
well-foundedness invariant is re-checked.

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
- **Firm SOLVE roots (the solve-generalization composes these BY NAME, `reference` only):**
  [`ksp_solve`](./ksp_solve.md) (firm — the preconditioned-Krylov outer solve, the per-block solve
  verb and the outer Schwarz-iteration driver), [`fold_solve`](./fold_solve.md) (firm — the
  iteration-fold solve driver, the outer-iteration leg for the coupled-operator approximate recovery),
  [`krylov-step`](./krylov-step.md) (firm — one Krylov step, the innermost solve primitive). These are
  referenced (NOT depended-on) — the rank-0 node composes them as an outer decomposition combinator and
  re-roots none of them.
- **No native Palace DD-preconditioner (the genuine-abstraction confirmation):** codemap search for
  `Schwarz|overlap|partition.of.unity|subdomain` returns only the MPI mesh-partitioning
  (`geodata.cpp:3242` "partitioning mesh into N subdomains") and the wave-port ROM overlap
  (`romoperator.cpp:586` "ports don't have any overlap") — neither a domain-decomposition solver. The
  solve-generalization is therefore a genuine decomposition-abstraction MATH sketch, not a lift of
  existing Palace solver code.
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

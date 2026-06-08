---
agent: abstractor
invoked_at: 2026-06-08T053000Z
scope: L4 roadmap_goal extension — sharding-decompose-reduce solve-generalization sketch (batch-45 front-4, gated/exploratory)
status: integrated
integrated_at: 2026-06-08T165758Z
integration_commit: 292a301
integration_notes: "cycle-139 (batch-45 OPENER, 1/3). Extended book/src/L4/sharding-decompose-reduce.md (STAYS rank-0 roadmap_goal) with the additive-Schwarz SOLVE-generalization; 3 NEW firm solve roots under reference: ONLY (no depends-on, no rank violation); DIRECTIVE-1 held (MPI cited-not-lifted); honest config-conditional NON-law (solve-case recovery strictly weaker than reduce-case). 2 OQs."
inputs:
  - book/src/L4/sharding-decompose-reduce.md (the batch-43 rank-0 sketch being extended)
  - book/src/L4/domain_energy_reduce.md (the firm domain-restriction precedent + partition-coverage NON-law model)
  - book/src/L4/fold_solve.md, krylov-step.md, ksp_solve.md (firm solve roots, composed BY NAME)
  - book/src/semantics/index.md §1.2.1/§1.2.2/§1.3.1 (L4 notation conventions)
---

# CYCLE: L4 roadmap_goal extension — sharding-decompose-reduce solve-generalization sketch

## Summary

Front-4 of the batch-45 all-fronts campaign ("sharding-math further"). I extend the batch-43 rank-0 `roadmap_goal` chapter `book/src/L4/sharding-decompose-reduce.md` with the **per-sub-domain SOLVE generalization** of its `subdomain_reduce = reduce ∘ restrict-to-block` decomposition-abstraction. The reduce case rides a law the firm reduce verbs ALREADY hold (the concatenation-homomorphism); the solve case is the additive-Schwarz-style shape **`subdomain_solve = compose ∘ map (solve ∘ restrict_to_block)`** — restrict the operator+RHS to each block, run the firm solve verb (`ksp_solve` / `fold_solve` / `krylov-step`) per block independently, and **homomorphically compose** the per-block solutions across the partition.

**The gate CLEARS for the solve case, with a sharper non-law than the reduce case.** The solve-generalization composes the firm reduce/solve roots BY NAME without re-rooting any firm node (it `reference`s them, never `depends-on`). The crucial structural finding — and the reason this is a faithful extension rather than a forced sketch — is that the solve case does **NOT** inherit the reduce case's free homomorphic recovery: a non-overlapping block solve is an EXACT global solve only for a block-diagonal operator, and a global operator with inter-block coupling makes the bare restrict/solve/compose an **approximate** (preconditioner / iteration-leg) recovery, NOT an identity. So the **partition-of-unity weighting + interface/overlap handling is carried as an EXPLICIT config-conditional precondition / NON-law** — mirroring exactly how `domain_energy_reduce` carries its `partition-coverage` axis and `Σ pᵢ = 1` config-conditional non-law (`domain_energy_reduce.md:147-152,172-178`). The bare MATH is the embarrassingly-parallel restrict/solve/compose; the coupling-correction (Schwarz overlap, p.o.u. weights, the convergent outer iteration) is the eventual *mechanism*, not a structural law of the abstraction.

The node **STAYS rank-0 `roadmap_goal`** (exploratory; the `...solve-generalization-promotion-pull` OQ stays deferred — no single-machine-valid domain-decomposition-preconditioner consumer is in flight). MPI/distributed (`rap.{hpp,cpp}` `ParOperator`/RAP, `geodata.cpp` partitioning, MPI collectives) is cited as the deferred-future realization MECHANISM ONLY, never lifted (DIRECTIVE-1). Palace ships **no native additive-Schwarz / domain-decomposition preconditioner** (confirmed by codemap search — the only `subdomain`/`overlap` hits are the MPI mesh-partitioning and the wave-port ROM overlap, neither a DD solver), so the solve-generalization MATH is a genuine decomposition-abstraction sketch, not a lift of existing Palace solver code.

## Gate disposition (all five HARD GATES checked against my own output)

1. **Node STAYS rank-0 `roadmap_goal`.** Frontmatter `rank: roadmap_goal` / `status: roadmap_goal` unchanged. The promotion-pull OQ stays deferred; no DD-preconditioner consumer in flight. ✓
2. **`edges:` lists firm roots under `reference:` ONLY.** The two NEW solve roots (`L4/ksp_solve`, `L4/fold_solve`; `L4/krylov-step` already present transitively via the reduce sketch's references) are added under `reference:`, NEVER `depends-on`. No `depends-on` block exists on this node. `rank_violations` stays 0 (no firm→rank-0 `depends-on` manufactured). ✓
3. **MPI/distributed STAYS OUT (DIRECTIVE-1).** `rap.{hpp,cpp}`, `geodata.cpp` partitioning, MPI collectives cited as deferred-future MECHANISM only (in the accreting-working-context + Evidence sections, flagged "cited, NOT lifted"). The active content is the MATH. ✓
4. **Gate-clear is genuine, not forced.** The solve-generalization is expressible composing the firm roots BY NAME with NO re-rooting / destabilization of any firm node. The place where it does NOT ride a free law (inter-block operator coupling) is recorded HONESTLY as a config-conditional NON-law (not papered over with a false identity claim). This is the faithful extension, not a forced sketch — see §Finding below. ✓
5. **Pseudocode FENCED in ```text blocks** (KaTeX `$`-sigil rule). All speculative forms in the proposed-changes block are in ` ```text ` fences. ✓

## Finding: the gate clears, but the solve case's recovery law is STRICTLY WEAKER than the reduce case's (recorded honestly, not forced)

This is the load-bearing finding, and it is what makes the extension legitimate rather than a forced sketch:

- **Reduce case (batch-43, already in the chapter):** the firm reduce verbs carry the concatenation-homomorphism as a STANDING FIRM LAW (`inner_product.md:154-157`, `linear_combination.md:146-151`, `domain_energy_reduce.md:147-152`). A partition of the index set is a `++`-decomposition; `reduce` over the whole index set EQUALS `mconcat` of `reduce` over the blocks. The recovery is **exact and free** — no new algebra.
- **Solve case (this extension):** there is **no analogous free law**. `solve (A|_b, b|_b)` per block recovers the exact global `solve(A, rhs)` ONLY when `A` is block-diagonal w.r.t. the partition (zero inter-block coupling). For a general global operator with inter-block coupling, the bare restrict/solve/compose is an **APPROXIMATE** recovery — precisely the additive-Schwarz preconditioner, which is a CONVERGENT OUTER ITERATION, not a one-shot identity. The exactness gap is the inter-block coupling, corrected by overlap + partition-of-unity weighting (the Schwarz mechanism).

So the solve-generalization is sketched with its recovery law explicitly **config-conditional** (block-diagonal ⇒ exact; coupled ⇒ approximate, needs the outer iteration), carried as a NON-law in the EXACT shape `domain_energy_reduce` carries `Σ pᵢ = 1`. This is NOT a forced lift: the abstraction composes firm roots by name, the honest law-strength is stated, and nothing firm is re-rooted. Had I claimed a free homomorphic solve-recovery I would have manufactured a false algebraic claim — recording the weaker config-conditional law is the correct disposition and is why the gate CLEARS (the abstraction sits ON TOP of the firm solve vocabulary as an outer combinator, it does not reshape it).

## Proposed changes

Two edits to the existing rank-0 chapter: (1) append the two NEW firm solve roots to the `reference:` edge list; (2) replace the thin "per-sub-domain SOLVE generalization" working-context bullet + extend the speculative-semantics / laws sections with the full additive-Schwarz decomposition-abstraction sketch. No SUMMARY.md / index.md changes (the chapter already exists and is registered; this is a content extension of an existing rank-0 node).

```edit:book/src/L4/sharding-decompose-reduce.md
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
```

(The above replaces the existing `edges: reference:` block — adding `L4/ksp_solve`, `L4/fold_solve`, `L4/krylov-step` as the firm SOLVE roots the solve-generalization composes BY NAME. All under `reference:` — NEVER `depends-on`, so no rank-0→firm `depends-on` is manufactured and `rank_violations` stays 0.)

```edit:book/src/L4/sharding-decompose-reduce.md
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
```

```edit:book/src/L4/sharding-decompose-reduce.md
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
```

```edit:book/src/L4/sharding-decompose-reduce.md
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
```

```edit:book/src/L4/sharding-decompose-reduce.md
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
```

```edit:book/src/L4/sharding-decompose-reduce.md
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
```

```edit:book/src/L4/sharding-decompose-reduce.md
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
```

```edit:book/src/L4/sharding-decompose-reduce.md
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
```

## Speculative operators proposed

These are the rough-in speculative operators the solve-generalization sketch needs; they are recorded INSIDE the rank-0 chapter (as `roadmap_goal` speculative forms, NO claims), NOT promoted. Harvester does NOT pick these up while the node stays rank-0 — they accrete in the working context until a real DD-preconditioner consumer pulls the node off rank-0. Listed here for the record:

- **`subdomain_solve`** — intended signature `(LinOp[(Sb: ...), $Sb] -> Tensor[(Sb: ...)] -> Solve (Tensor[$Sb])) -> Partition -> LinOp[(S: ...), $S] -> Tensor[(S: ...)] -> Solve (Tensor[$S])`. The additive-Schwarz decomposition-abstraction: restrict operator+RHS to each block, run the closed-over firm solve verb per block independently, recompose with partition-of-unity weighting. Recovery config-conditional (block-diagonal exact; coupled approximate). SPECULATIVE — recorded in the rank-0 chapter, not authored.
- **`restrict_op_to_block`** — intended signature `IndexBlock -> LinOp[(S: ...), $S] -> LinOp[(Sb: ...), $Sb]`. The operator analog of the reduce case's `restrict_to_block` (which restricts a field/vector); restricts a square system operator to one block's sub-shape. Its eventual realization is the RAP Galerkin restriction (`rap.cpp:116-126`, DEFERRED mechanism). SPECULATIVE.
- **`compose_partition`** — intended signature `Partition -> [Tensor[(Sb: ...)]] -> Tensor[(S: ...)]` (carrying the p.o.u. weighting as config). The recompose half: assembles the per-block sub-solutions into the global state, applying partition-of-unity weights on overlaps. SPECULATIVE — carries the config-conditional non-law at the combinator boundary.

(All three are recorded as `roadmap_goal` speculative forms in the chapter's accreting working context — they do NOT land as dep-map rough-in rows while the node is rank-0, since promotion is gated on a real consumer pull.)

## Supporting evidence

- **The extended chapter:** `book/src/L4/sharding-decompose-reduce.md` (the batch-43 rank-0 sketch; rank/status `roadmap_goal`, `edges.reference` already lists `domain_energy_reduce` / `inner_product` / `linear_combination` / `gram_reduce` / `gram`).
- **The partition-coverage NON-law model (mirrored for the solve case):** `book/src/L4/domain_energy_reduce.md:147-152` (the map-independence / concatenation-homomorphism fold law), `:172-178` (the `Σ pᵢ = 1` CONFIG-CONDITIONAL non-law — overlapping ⇒ double-count, partial ⇒ under-count; the EXACT shape the solve case's partition-of-unity non-law mirrors); `partition-coverage` variant-axis at `:16`.
- **Firm solve roots composed BY NAME (`reference` only, all `rank: firm` confirmed this dispatch):** `book/src/L4/ksp_solve.md` (firm), `book/src/L4/fold_solve.md` (firm), `book/src/L4/krylov-step.md` (firm).
- **Deferred MPI/distributed + RAP MECHANISM (cited, NOT lifted — DIRECTIVE-1; the existing chapter's set, re-confirmed on-disk this dispatch):**
  - `palace/utils/geodata.cpp:261-262` (`std::unique_ptr<mfem::ParMesh> Partition(IoData &, std::unique_ptr<mfem::Mesh>, MPI_Comm)` — the distributed-mesh builder, eventual source of the partition `P`; confirmed on-disk, signature spans :261-262), `:3230` (`GetMeshPartitioning(const mfem::Mesh &, int size, …)` — METIS element-to-block assignment), `:3242` (`"Finished partitioning mesh into {:d} subdomain{}"` — the MPI sub-domain partitioning, NOT a DD solver).
  - `palace/linalg/rap.hpp:24` (`class ParOperator : public Operator` — the distributed-operator type, eventual realization of `restrict_op_to_block`), `palace/linalg/rap.cpp:116-126` (the `R·A·P` Galerkin triple product, `hypre_ParCSRMatrixRAPKT` / `hypre_ParCSRMatMat` — the eventual operator-restrict-and-compose mechanism).
- **No-native-DD-preconditioner confirmation:** codemap `search_text` for `Schwarz|overlap|partition.of.unity|subdomain` over `**/*.{hpp,cpp}` returns only the MPI mesh-partitioning (`geodata.cpp:3242`) and the wave-port ROM overlap (`romoperator.cpp:586`, `:592` `"should have exactly zero overlap"`) — neither a domain-decomposition solver.
- **L4 notation conventions used:** `book/src/semantics/index.md` §1.2.1 (named shape groups `(S: ...)`/`$S`), §1.2.2 (operator shapes `LinOp[(R: ...), (D: ...)]` / square `LinOp[(S: ...), $S]`), §1.3.1 (closure-returning signatures; the `solve` argument is a closure-typed parameter, grouped in parens `(LinOp[…] -> Tensor[…] -> Solve (…))`). The `Solve` monad codomain per §1.1 `Sim τ` / the solve-monad convention.

## Open questions / caveats

- **`...solve-generalization-promotion-pull` OQ STAYS DEFERRED** (per the hard gate). The node stays rank-0; promotion is gated on a real single-machine-valid domain-decomposition-preconditioner consumer pulling `subdomain_solve` by name, which is NOT in flight this cycle. The three speculative operators (`subdomain_solve` / `restrict_op_to_block` / `compose_partition`) accrete in the chapter's working context, NOT as dep-map rough-in rows.
- **The solve-case recovery is STRICTLY WEAKER than the reduce-case recovery** (the §Finding). The reduce case rides a free standing firm law (the concatenation-homomorphism); the solve case's exact-recovery is config-conditional (block-diagonal only), degrading to an additive-Schwarz APPROXIMATION for coupled operators. I recorded this honestly as a config-conditional NON-law rather than forcing a false free-recovery claim — this is what makes the gate-clear legitimate. A reviewer (lowering-verifier) should confirm the non-law framing is faithful and that no over-strong solve-recovery claim leaked in.
- **The `compose_partition` p.o.u. weighting is sketch-level only.** The exact form of the partition-of-unity weights χ_b (and whether the overlap is algebraic-restricted-additive-Schwarz RAS vs classical additive Schwarz) is left to the eventual mechanism — recorded as open intent in the working context, NOT asserted. This is the solve-side analog of the reduce case leaving the `mconcat` communication to the MPI collectives.
- **Citation note on `Partition(...)`:** the existing chapter cites `geodata.cpp:262`; on-disk the signature opens at `:261` and the `IoData &iodata` / `MPI_Comm comm` parameters span `:261-262`. I cite `:261-262` in my evidence; the existing chapter's `:262` is the second signature line and is in-range (not a defect, but the wider `:261-262` is the precise span). No edit to the existing citation proposed (it is a deferred-mechanism cite, in-range).

---
agent: harvester
invoked_at: 2026-06-07T071941Z
scope: L1 operator: dorfler_mark
status: pending
inputs:
  - reports/2026-06-07T071941Z-cycle-planner-cycle-122/CYCLE.md (row D2)
  - book/src/L1/index.md:193-195 (rough-in AMR estimate/mark vocabulary group; dorfler_mark row :194)
  - book/src/L1-L0/amr-estimate-mark-refine.md (the lowering theme naming dorfler_mark; verified line anchors)
  - palace/utils/dorfler.cpp:14-171 (ComputeDorflerThreshold; read single-rank)
  - palace/drivers/basesolver.cpp:103-115 (MarkedElements: threshold→index-set), :220-233 (the mark-stage caller)
  - palace/utils/configfile.hpp:97-119 (RefinementData; update_fraction θ default 0.7)
  - abstractor:2026-06-07T054924Z-amr-estimate-mark-refine (the proposing report)
  - book/src/semantics/index.md §1.2 (named shape groups; Tensor[N] reserved for flat rank-1 vectors)
integrated_at: 2026-06-07T071941Z
integration_commit: 17cdafe9d9515c72045691b07420fbdfa25af81a
integration_notes: "cycle-122 D2 (FINAL report). Applied clean. L1/dorfler_mark landed FIRM; unresolved_depends_on_targets 1→0; FIRED the amr-estimate-mark-refine theme firm-flip rough-in→firm (both L1 endpoints firm). Flat SUMMARY entry (AMR group-intro deferred to c123). 0 gate hits. See reports/cycle-122-integrator-staging/STAGING.md."
---

# CYCLE: Formalize dorfler_mark at L1

## Summary
`dorfler_mark` is the **mark** verb of Palace's adaptive-mesh-refinement estimate→mark→refine loop:
given a per-element error-indicator vector and a target fraction θ, it selects the **smallest** element
index set whose summed squared error covers at least θ of the total — the Dörfler bulk-marking
criterion `arg min |S| s.t. Σ_{i∈S} e_i² ≥ θ · Σ_i e_i²`. It is currently a rough-in dep-map row
(`book/src/L1/index.md:194`, proposed by the c121 D7 AMR abstractor and named as a lowering endpoint in
the already-on-disk `amr-estimate-mark-refine` theme). This dispatch firms it: a full L1 chapter with
the `Real -> Tensor[N] -> IndexSet[N]` signature, the sort/partial-sum/lower-bound semantics, the
**load-bearing over-mark tie-break** (always choose the lower threshold, over-mark rather than
under-mark, `dorfler.cpp:160-163`), the algebraic laws of the marking map, and the single-rank reading
(the cross-rank threshold bisection is a single-rank degeneracy; the distributed reconciliation is
flagged as a deferred DIRECTIVE-1 future-direction note, not lifted). Firming this — together with
D1's `flux_recovery_estimate` — fires the `amr-estimate-mark-refine` theme firm-flip and discharges
1 of the 6 `unresolved_depends_on_targets`. Firm-on-positive-structure: every law is a syntactic
identity on the fully-read Palace-authored `ComputeDorflerThreshold` + `MarkedElements` bodies, so
the absent dedicated `dorfler.cpp` unit test does not gate firm.

## Proposed changes

```new:book/src/L1/dorfler_mark.md
---
layer: L1
operator: dorfler_mark
rank: firm
edges:
  depends-on:
    # A firm L1 operator's blocking dependencies are its POSITIVE L0 SOURCE (rank-terminal ground
    # truth) via cites-evidence, plus the L1>L0 lowering theme via `lowers-to` (the c108 §5 L1-op→theme
    # grounding convention; precedent: set_subvector_zero.md). The `firm` rank rests on the read-in-full
    # Palace-authored ComputeDorflerThreshold + MarkedElements bodies below; well-foundedness
    # rank(u) ≤ rank(v) holds against rank-terminal evidence AND against the amr theme (rank(op=3) ≤
    # rank(theme=3) once the theme firm-flips this cycle with its two L1 endpoints).
    - kind: cites-evidence
      target: palace/utils/dorfler.cpp:14-171        # ComputeDorflerThreshold: bulk-marking math (read single-rank)
    - kind: cites-evidence
      target: palace/drivers/basesolver.cpp:103-115  # MarkedElements: threshold→index-set ({ i : e[i] >= threshold })
    - kind: cites-evidence
      target: palace/drivers/basesolver.cpp:220-233  # the mark-stage caller (ComputeDorflerThreshold ▷ MarkedElements)
    - kind: cites-evidence
      target: palace/utils/configfile.hpp:97-119      # RefinementData: update_fraction θ (default 0.7) config home
    - kind: lowers-to
      target: L1-L0/amr-estimate-mark-refine          # the L1>L0 lowering theme (sub-pattern B is the mark verb); firm-flips this cycle
  reference:
    - L1/flux_recovery_estimate                        # the AMR estimate verb (sibling; produces the indicator vector this verb marks)
    - L1/nrm2                                           # the indicator-vector reduction the loop also computes (Norml2); sibling, not a dep
    - feature/lifecycle.L4                              # the estimate→mark→refine fold composition home
---

# dorfler_mark

Mutation-lifted Dörfler (bulk) marking: `marked = dorfler_mark(θ, indicators)` returns the
**smallest** set of element indices whose summed squared error covers at least fraction `θ` of the
total squared error —
`arg min |S| such that Σ_{i∈S} e_i² ≥ θ · Σ_i e_i²`. The pure-functional lift of Palace's
`utils::ComputeDorflerThreshold` (which returns the marking *threshold*) composed with the
`MarkedElements` threshold→index-set collection. It is the **mark** verb of the adaptive-mesh-refinement
estimate→mark→refine loop: given the per-element a-posteriori error indicators (produced by
[`flux_recovery_estimate`](./flux_recovery_estimate.md)), it picks which elements to refine.

## Context

`dorfler_mark` is the second verb of Palace's AMR loop body (`SolveEstimateMarkRefine`,
`palace/drivers/basesolver.cpp`). The loop runs `estimate ▷ mark ▷ refine` per adaptation iteration;
this verb sits between [`flux_recovery_estimate`](./flux_recovery_estimate.md) (which produces the
scalar per-element indicator vector) and the MFEM-opaque `refine` leaf (which subdivides the marked
elements). The marker is **driver-agnostic** — it operates only on the scalar indicator vector and the
fraction θ, with no knowledge of the physics that produced the indicators.

The Dörfler criterion (Dörfler, *A convergent adaptive algorithm for Poisson's equation*, SIAM
J. Numer. Anal. 1996) is a **bulk** marking strategy: rather than marking a fixed number or a
fixed fraction of *elements*, it marks the smallest set of elements that together account for at
least a target fraction of the total *error*. This concentrates refinement where the error is, and is
the convergence-guaranteeing choice the cited theory rests on.

The backing Palace code computes the marking in two pieces:

- **`utils::ComputeDorflerThreshold(comm, e, fraction)`** (`palace/utils/dorfler.cpp:14-171`) returns
  a `{ error_threshold, actual_fraction }` pair — the *threshold value* `E` such that the set
  `{ i : e_i ≥ E }` is the smallest set covering ≥ `fraction` of the squared error, and the actual
  fraction that set achieves.
- **`MarkedElements(e, threshold)`** (`palace/drivers/basesolver.cpp:103-115`) collects the index set
  `{ i : e_i ≥ threshold }` into an `mfem::Array<int>`.

At the L1 surface these compose into the single verb `dorfler_mark(θ, indicators) → IndexSet` — the
threshold is an *internal* quantity of the marking (the algorithm's pivot), not part of the L1 result.
The mark-stage caller `palace/drivers/basesolver.cpp:220-233` is exactly this composition:
`ComputeDorflerThreshold(...) ▷ MarkedElements(...)`.

**Single-rank reading (DIRECTIVE-1).** `ComputeDorflerThreshold` carries a cross-rank
threshold-bisection apparatus: each rank computes a different local threshold, and a binary search over
`[min_threshold, max_threshold]` (the per-rank min/max, `Mpi::GlobalMin`/`GlobalMax` at
`dorfler.cpp:66-67`) converges on a common threshold using `Mpi::GlobalSum`-reduced marked-element and
marked-error counts (`:84-85`, `:107-108`). Read single-rank this **degenerates**: `min_threshold ==
max_threshold == error_threshold` (the per-rank min and max of a single value, `:64-67`), so the
bisection loop (`:100-158`) is entered only to confirm the already-exact local threshold and exits
immediately (the `elements.max_marked <= elements.min_marked + 1` termination, `:127`, or the
zero-width `|max_threshold − min_threshold|` tolerance, `:125`). The single-rank marking is therefore
the direct pivot computation `:34-38` followed by `MarkedElements`. The cross-rank reconciliation is a
**deferred distributed concern** (OQ `dorfler-cross-rank-bisection-distributed-note-deferred`), noted
in *Downward to L0*, **not** lifted (DIRECTIVE-1: the MPI-associated version may be destructive to the
spine).

## Signature

    dorfler_mark :: Real -> Tensor[N] -> IndexSet[N]

    dorfler_mark(θ, e) = the smallest S ⊆ {0..N-1} with  Σ_{i∈S} e_i² ≥ θ · Σ_i e_i²,
                         realized as  S = { i : e_i ≥ threshold(θ, e) }

Shape contract (bunsen-style, named axes):

- `θ` — `Real` — the target error fraction in `(0, 1]` (the Dörfler bulk fraction; Palace default
  `0.7`, `palace/utils/configfile.hpp:119`). A construction-time config field read from
  `RefinementData.update_fraction`; see *Record definition*.
- `e` — `Tensor[N]` — the per-element a-posteriori error-indicator vector over the element axis `N`
  (`N = n_elem`, the number of mesh elements). Genuinely rank-1 (a flat per-element scalar vector), so
  `Tensor[N]` is the correct shape per the semantic surface's "reserve `Tensor[N]` for flat rank-1
  vectors at L1" rule (`book/src/semantics/index.md` §1.2) — **not** a named shape group (there is no
  rank-agnostic congruence to assert). All entries `e_i ≥ 0` (they are L2 norms of flux differences).
  Read-only.
- result — `IndexSet[N]` — the marked element index set, a subset of `{0..N-1}` over the element axis
  (the `mfem::Array<int>` the `MarkedElements` loop fills, `palace/drivers/basesolver.cpp:105-114`).
  See *Record definition*.

The empty-mesh case (`N = 0`) yields the empty set (the L0 guards `estimates.size() > 0`,
`dorfler.cpp:35,38`). For `θ → 0⁺` the marked set tends to a single element (the largest indicator);
for `θ = 1` it tends to the whole mesh.

## Semantics

`dorfler_mark(θ, e)` computes the marking in three steps (all single-rank; the abstract criterion is
the first sentence of *Signature*, the steps below are the transparent realization Palace uses):

1. **Sort + cumulative squared error.** Copy `e`, sort ascending (`std::sort`, `dorfler.cpp:20`),
   square the entries (`:24-27`), and form the prefix sum `sum` of the squares (`std::partial_sum`,
   `:28`). `sum.back()` is the total squared error `local_total` (`:35`). The estimate copy is then
   un-squared back to the indicator magnitudes (`:29-31`) for the threshold lookup.
2. **Pivot → threshold.** Find the first prefix-sum position leaving fraction `(1 − θ)` of the total
   squared error *below* it: `pivot = lower_bound(sum, (1 − θ)·local_total)` (`:36`); the
   `error_threshold` is the sorted indicator at that index (`:38`). This is the smallest threshold
   `E` such that the elements with `e_i ≥ E` carry ≥ `θ` of the squared error.
3. **Threshold → index set.** Collect `{ i : e_i ≥ E }` (`MarkedElements`,
   `palace/drivers/basesolver.cpp:103-115`, the `if (e[i] >= threshold) ind.Append(i)` loop
   `:109-112`).

The sort + partial-sum + lower-bound is a **transparent performance shape** over the abstract "select
the smallest index set covering θ of the total squared error" — it is the efficient realization of the
criterion, algebraically equivalent to the set-selection definition, and gets a one-line note rather
than entering the algebra.

**The load-bearing over-mark tie-break.** The fraction generally cannot land exactly — the achievable
fractions are a discrete ladder, one rung per element — so the marking always covers the *larger* number
of elements and the *greater* fraction of the total error, the smallest fraction `≥ θ` rather than the
largest `< θ`. **At single-rank (the reading this entry adopts per DIRECTIVE-1) this over-coverage is
produced by the `std::lower_bound` pivot** (`dorfler.cpp:36`): the pivot is the first prefix-sum position
leaving `(1 − θ)` of the total *below* it, so the chosen threshold is the *largest* `E` whose set still
achieves ≥ θ coverage — i.e. the *smallest* admissible marked set, over-covering by one rung when the
ladder does not land exactly. (The multi-rank bracket selection `error_threshold = min_threshold`
`dorfler.cpp:163` — "always choose the lower threshold value", explanatory comment `:160-162`: "Would
rather over mark than under mark, as Dörfler marking is the smallest set that covers **at least** the
specified fraction of the error" — performs the SAME over-coverage across ranks, but **degenerates to the
identity single-rank** since `min_threshold == max_threshold == error_threshold` there `:64-67`: it
returns the local pivot `:36` already computed. So the single-rank mechanism is the `:36` lower_bound;
`:163` is the multi-rank bracket-selection tie-break.) This is **not** a transparent trick: it is the
load-bearing realization of the `≥ θ` (at-least) direction of the Dörfler predicate. The post-condition
is verified at `:167-169`
(`MFEM_VERIFY(error_marked >= fraction * error.total, "... Dorfler marking predicate failed!")`) — the
returned set provably covers **at least** θ, never less. A different tie-break (choosing the upper
threshold / under-marking) would violate the convergence theory's hypothesis. Preserved as an explicit
algebraic claim (law 4 below).

The L1 form is pure-functional: the same `(θ, e)` yields the same index set, with no in-place mutation.
The L0 source mutates a copied estimate vector in place (sort, square, partial-sum on `std::vector`
copies, `dorfler.cpp:19-31`) and the threshold-bisection scalars; none of that escapes the verb (the
copies are local). The destination `mfem::Array<int>` reservation/append (`basesolver.cpp:105-114`) is
an L0 buffer concern.

## Algebraic laws

The laws below hold; absences are deliberate. `S(θ, e) = dorfler_mark(θ, e)` denotes the marked set,
`tot(e) = Σ_i e_i²` the total squared error, `cov(S, e) = Σ_{i∈S} e_i² / tot(e)` the covered fraction.

1. **Coverage (the defining predicate).** `cov(S(θ, e), e) ≥ θ` — the marked set covers at least
   fraction θ of the total squared error. Positively anchored at the post-condition
   `MFEM_VERIFY(error_marked >= fraction * error.total, ...)` (`dorfler.cpp:167-169`). The result is
   never an under-marking.

2. **Minimality (bulk-marking).** Among all sets `S'` with `cov(S', e) ≥ θ`, `S(θ, e)` is of minimal
   cardinality (it is `{ i : e_i ≥ E }` for the *largest* threshold `E` still achieving coverage —
   the lower-bound pivot `:36` is the first prefix position achieving `(1−θ)` below it). This is the
   Dörfler criterion's "smallest set" requirement; "bulk" marking marks by error mass, not element
   count.

3. **Monotonicity in θ.** For `θ₁ ≤ θ₂`, `S(θ₁, e) ⊆ S(θ₂, e)` — a larger target fraction marks a
   superset (the pivot moves down the sorted prefix sum as `(1−θ)·local_total` decreases, `:36`,
   lowering the threshold and admitting more elements). In particular `S(0⁺, e)` is the
   single-largest-indicator element and `S(1, e)` is the whole (nonzero-indicator) mesh.

4. **Over-mark tie-break (load-bearing).** When no threshold lands `cov = θ` exactly, `S(θ, e)` is the
   larger admissible set — so `cov(S(θ, e), e)` is the smallest achievable fraction `≥ θ`, never the
   largest `< θ`. **At single-rank** this over-coverage is produced by the `std::lower_bound` pivot
   (`:36`): the pivot selects the *largest* threshold `E` still achieving ≥ θ coverage (the smallest
   admissible set, over-covering by one ladder rung), and the post-condition `:167-169` witnesses it.
   (The multi-rank bracket selection `error_threshold = min_threshold` `:163` — "choose the lower
   threshold", comment `:160-162` — does the same over-coverage across ranks but **degenerates to the
   identity single-rank** `min==max==error_threshold` `:64-67`, returning the `:36` pivot.) The
   over-marking is the realization of the `≥` in law 1. (See *Semantics*.) Recorded as load-bearing:
   dropping it (under-marking) would break the convergence hypothesis.

5. **Permutation equivariance.** `dorfler_mark(θ, π·e) = π·dorfler_mark(θ, e)` for any permutation π
   of the element axis — the marking depends only on the *multiset* of indicator values, not the
   element order; permuting the input permutes the marked indices identically. The sort (`:20`) makes
   the threshold permutation-invariant; the threshold→set collection (`basesolver.cpp:109-112`) tracks
   original indices.

6. **Positive-scaling invariance of the marked set.** `dorfler_mark(θ, α·e) = dorfler_mark(θ, e)` for
   any scalar `α > 0` — uniform positive scaling of all indicators leaves the *marked set* unchanged
   (both the per-element squared error and the total scale by `α²`, so the covered fraction at every
   threshold is identical; the threshold itself scales by `α`). The criterion is scale-free in the
   indicators; only their *relative* magnitudes matter.

Laws that explicitly **do not** hold:

- **Not additive / not linear.** `dorfler_mark(θ, e + f) ≠ dorfler_mark(θ, e) ∪ dorfler_mark(θ, f)`
  in general — marking is a nonlinear set-selection on the squared-error distribution, not a linear
  map. Recorded so the verb is not mistaken for a BLAS-1-style elementwise op.
- **No θ-additivity.** `S(θ₁ + θ₂, e) ≠ S(θ₁, e) ∪ S(θ₂, e)` — the fractions do not compose by union
  (law 3 gives nesting, not union-decomposition).
- **No reduction-order non-law of its own (single-rank).** The single-rank marking has no
  load-bearing summation order: the prefix sum `std::partial_sum` (`:28`) is a fixed left-to-right
  scan over the *sorted* squares, deterministic given the input multiset. There is no cross-rank
  reduction at single-rank (the `Mpi::GlobalSum` collectives degenerate). Recorded as an absence so
  the sort/scan order is not read as a load-bearing numerical trick. (The *cross-rank* case — where
  the bisection's reduction order would matter — is the deferred distributed concern, not lifted.)

## Dependencies

(leaf) — `dorfler_mark` depends on no other L1 operator. It consumes a scalar indicator vector and a
fraction and produces an index set; the sort, prefix sum, lower-bound pivot, and threshold→set
collection are atomic at the L1 surface (the in-place sort on the local copy, the device/host buffer
handling, and — at multi-rank — the threshold bisection are L1>L0 / distributed concerns).

It is the **second verb** of the AMR estimate→mark→refine pipeline:

- it **consumes** the indicator vector produced by [`flux_recovery_estimate`](./flux_recovery_estimate.md)
  (the AMR estimate verb; a sibling, *not* a dependency — the dataflow edge is a `reference`, not a
  `depends-on`, since `dorfler_mark` is agnostic to how the indicators were produced);
- its output index set **feeds** the MFEM-opaque `refine` leaf (the third verb;
  `obstruction (opaque-library-ownership)`, narrated in the
  [`amr-estimate-mark-refine`](../L1-L0/amr-estimate-mark-refine.md) theme, *not* a fillable operator).

The loop also computes `err = nrm2(indicators)` ([`nrm2`](./nrm2.md), the `Norml2` reduction) as the
AMR convergence scalar — a sibling reduction over the same vector, not a dependency of this verb.

## Record definition

Two records are named in the signature; both are single-consumer at this verb's surface (the AMR
cohort), defined here in themselves:

- **`IndexSet[N]`** — the marking result type: a set of element indices into the `N = n_elem` axis,
  `{ i : 0 ≤ i < N }`, the marked-for-refinement subset. Produced as `{ i : e_i ≥ threshold }` and
  consumed by `refine`. The L0 home is the `mfem::Array<int>` the `MarkedElements` `ind.Append(i)`
  loop fills (`palace/drivers/basesolver.cpp:105-114`). Run-time stratum (recomputed each adaptation
  iteration). Fields: an unordered collection of distinct `Int` element indices in `[0, N)`; the
  ordering in the backing `Array<int>` is ascending-by-original-index (the `MarkedElements` loop scans
  `i = 0..N-1`) but the *set* semantics are order-free (law 5). This is the same `IndexSet[E]` the
  [`amr-estimate-mark-refine`](../L1-L0/amr-estimate-mark-refine.md) theme names; defined here as the
  positively-anchored home for the verb's result.
- **`θ : Real`** is a scalar, not a record — but its config home is the **`RefinementData`** struct
  (`palace/utils/configfile.hpp:97-119`), the `refinement.*` IoData surface. The field this verb reads
  is `update_fraction` (the Dörfler bulk fraction, default `0.7`, `:117-119`); sibling
  construction-time fields (`tol`/`max_it`/`max_size`/`max_nc_levels`/`nonconformal`) parameterize the
  enclosing AMR loop, not this verb. **Construction-time stratum** (read once, before the loop).
  `RefinementData` is used by ≥2 chapters (this verb, `flux_recovery_estimate`, the
  `amr-estimate-mark-refine` theme, the lifecycle feature column) — its full field-by-field definition
  is a cross-cutting concept home; the `amr-estimate-mark-refine` theme already defines it inline as a
  single-consumer record (§Record definition there). Flagged in Open questions
  (`record-RefinementData-needs-concept-definition-home`) so the cross-cutting page is dispatched; this
  verb references the θ ← `update_fraction` field only.

## Variant axes

- **fraction θ** (parameterized): `θ ∈ (0, 1]`, the bulk target. A continuous parameter, not a
  behavioural variant; the marking shape (sort/pivot/collect) is θ-uniform. Palace default `0.7`
  (`configfile.hpp:119`).
- **rank multiplicity** (absorbed at single-rank; the deferred distributed axis): single-rank the
  marking is the direct pivot + collect; multi-rank it is the cross-rank threshold bisection
  (`dorfler.cpp:64-158`). Read single-rank per DIRECTIVE-1; the bisection is the degenerate
  confirm-the-local-threshold path. The distributed reconciliation is the deferred future-direction
  note (*Downward to L0*), **not** a lifted variant.

There is **no** refinement-vs-coarsening axis on *this* operator. Palace's
`ComputeDorflerCoarseningThreshold` (`dorfler.cpp:173-...`) is the *derefinement* sibling (it marks the
largest set making up θ of the *coarsening opportunities*); it is a distinct verb over a different input
(derefinement opportunities, not error indicators) and is **not** folded into this entry — recorded
here as the sibling shape, flagged in Open questions (`dorfler-coarsening-threshold-sibling-verb`) as a
future AMR-cohort harvest, not in this one-operator scope.

## Status

`firm` — the operator's structure is read directly from **positive** Palace source: the
`ComputeDorflerThreshold` body read in full (`palace/utils/dorfler.cpp:14-171`), the `MarkedElements`
threshold→index-set collection (`palace/drivers/basesolver.cpp:103-115`), the mark-stage caller
composition (`:220-233`), and the θ config home (`palace/utils/configfile.hpp:97-119`). The signature's
shape (fraction + per-element indicator vector → element index set) matches the body exactly; the
algebraic laws (coverage, minimality, θ-monotonicity, over-mark tie-break, permutation equivariance,
positive-scaling invariance) are properties of the Dörfler bulk-marking criterion read off the sorted
prefix-sum + lower-bound pivot, modulo the explicitly-recorded non-additivity / no-θ-additivity /
no-reduction-order non-laws.

This is the **firm-on-positive-structure** decision, exactly as for the BLAS-1 elementwise leaves
([`reciprocal`](./reciprocal.md), [`set_subvector_zero`](./set_subvector_zero.md)): every law is a
**syntactic identity on fully-specified positive source** (set-selection / threshold-pivot facts about
a sorted prefix sum), not a convergence or numerical-tolerance fact. No dedicated `dorfler.cpp` unit
test exists in `reference/palace/test/unit/` (the marking is exercised only indirectly through the AMR
integration path) — but **a missing test does not gate syntactic-identity laws** (the `apply_linop` /
`reciprocal` / `set_subvector_zero` firm-on-positive-structure situation, not the `eigsolve`-convergence
situation): the marking laws do not depend on iteration or convergence, so the absent test does not
reduce law-confidence. Hence `firm`, not `rough-in (test-coverage-bounded)`. (The over-mark tie-break
post-condition is *itself* a positive in-source assertion, `MFEM_VERIFY` at `:167-169`, which is
stronger than a test — the code aborts if the predicate fails.)

Well-foundedness: the `depends-on` edges are (a) `cites-evidence` edges to the **positive L0 source**
(`dorfler.cpp:14-171`, `basesolver.cpp:103-115`, `:220-233`, `configfile.hpp:97-119`), rank-terminal
ground truth, and (b) a `lowers-to` edge to the L1>L0 lowering theme
[`amr-estimate-mark-refine`](../L1-L0/amr-estimate-mark-refine.md) (the c108 §5 L1-op→theme grounding
convention; precedent `set_subvector_zero.md`). The theme firm-flips this cycle once both its L1
endpoints (this verb + D1's `flux_recovery_estimate`) are firm (well-foundedness: a theme is at most as
resolved as its least-resolved endpoint, scheme §5), so after this cycle `rank(op=3) ≤ rank(theme=3)`
holds; the verb's firmness *grounds* on the positive L0 read (not on the theme), and the `lowers-to`
edge routes liveness down to the theme.

Resolves 1 of the 6 `unresolved_depends_on_targets` (the `L1/dorfler_mark` endpoint of
`amr-estimate-mark-refine`). Discharges the `dorfler_mark` half of OQ
`amr-estimate-mark-refine-theme-firmness-gate`.

## Downward to L0

The lowering is the [`amr-estimate-mark-refine`](../L1-L0/amr-estimate-mark-refine.md) L1>L0 theme
(sub-pattern B — mark; this verb's firmness rests on the positive L0 read, cited as `cites-evidence`
deps, with the theme carried as a `lowers-to` `depends-on` edge per the c108 §5 convention). It
narrates how this pure set-selection lowers into Palace's imperative
`ComputeDorflerThreshold` ▷ `MarkedElements`: the in-place sort/square/partial-sum on the copied
estimate vector (`dorfler.cpp:19-31`), the lower-bound pivot (`:36`), the threshold-comparison
index-collection loop (`basesolver.cpp:109-112`), and the over-mark tie-break (`:163`).

**Deferred distributed concern (DIRECTIVE-1 future-direction note; NOT lifted).** At multi-rank the
threshold is not a single local pivot but a value reconciled across ranks: each rank's local pivot
differs (a low-error rank yields a lower threshold, a high-error rank a higher one,
`dorfler.cpp:58-63`), so the common threshold is found by a bisection over `[min_threshold,
max_threshold]` (`:64-158`) using `Mpi::GlobalMin`/`GlobalMax`/`GlobalSum` collectives
(`:66-67`, `:84-85`, `:107-108`, `:124`). This cross-rank reconciliation is **read single-rank
degenerate** (`min == max`, the loop confirms the local threshold) per DIRECTIVE-1 and recorded as a
deferred future direction (OQ `dorfler-cross-rank-bisection-distributed-note-deferred`) — the
MPI-associated version may be destructive to the spine and is **not** lifted now. The
`Mpi::GlobalSum`-reduced marked-error/marked-element accumulation, were it lifted, would introduce a
cross-rank reduction-order dependency (the multi-rank analog of the no-reduction-order non-law above);
that is part of the deferred concern, not this verb's algebra.

## Evidence

- `palace/utils/dorfler.cpp:14-171` — `ComputeDorflerThreshold(MPI_Comm comm, const Vector &e, double
  fraction)`, read in full. Sort `:20`, square `:24-27`, `std::partial_sum` `:28`, un-square `:29-31`,
  total `local_total` `:35`, `lower_bound` pivot `:36`, `error_threshold` `:38`, the `Marked` lambda
  (threshold→count/error) `:40-56`, the single-rank-degenerate per-rank min/max `:64-67`, the
  bisection loop `:100-158`, the tolerances + termination `:123-127`, the **over-mark tie-break**
  `error_threshold = min_threshold` `:163` with the explanatory comment `:160-162`, the post-condition
  `MFEM_VERIFY(error_marked >= fraction * error.total, ...)` `:167-169`, return `:170`. On-disk read
  (codemap `read_range` drifts +1/+3 on this file's comment/brace boundaries — the c121 producer note;
  line numbers above are the **on-disk** values, confirmed by direct `Read` of
  `reference/palace/palace/utils/dorfler.cpp`).
- `palace/drivers/basesolver.cpp:103-115` — `MarkedElements(const Vector &e, double threshold)`: the
  `ind.Reserve(e.Size())` (`:106`), the `for (i ...) if (e[i] >= threshold) ind.Append(i)` loop
  (`:107-113`, the threshold→index-set collection), `return ind` (`:114`). On-disk confirmed.
- `palace/drivers/basesolver.cpp:220-233` — the mark-stage caller: the `marked_elements` lambda calling
  `utils::ComputeDorflerThreshold(comm, indicators.Local(), refinement.update_fraction)` (`:223-224`)
  then `MarkedElements(indicators.Local(), threshold)` (`:225`) — the `dorfler_mark` composition. The
  `θ = refinement.update_fraction` binding (`:224`). On-disk confirmed.
- `palace/utils/configfile.hpp:97-119` — `RefinementData`, the AMR config record; `update_fraction =
  0.7` (`:119`) with the Dörfler comment "The set of marked elements is the minimum set that contains
  update_fraction of the total error" (`:117-118`). The θ config home. On-disk confirmed.
- `palace/utils/dorfler.hpp:21-29` — the `ComputeDorflerThreshold` spec comment "the smallest set to
  achieve sum_{K_E} e² >= fraction * sum e²" (`:21-25`) + the Dörfler 1996 citation (`:26-27`) + the
  declaration (`:28-29`). The criterion stated in Palace's own words. On-disk confirmed.
- `book/src/L1-L0/amr-estimate-mark-refine.md` — the L1>L0 lowering theme (sub-pattern B is this verb);
  firm-flips this cycle with its two L1 endpoints. The downward home.
- `book/src/L1/flux_recovery_estimate.md` — the AMR estimate verb (sibling D1 this cycle); produces the
  indicator vector this verb marks.

```yaml
verified_against:
  - citation: palace/utils/dorfler.cpp:14
    verdict: supports
    audited_at: 2026-06-07T071941Z
    note: ComputeDorflerThreshold(MPI_Comm, const Vector &e, double fraction) signature; on-disk Read confirmed (codemap +1 drift bypassed).
  - citation: palace/utils/dorfler.cpp:20
    verdict: supports
    audited_at: 2026-06-07T071941Z
    note: std::sort(estimates...) ascending sort; on-disk line 20.
  - citation: palace/utils/dorfler.cpp:28
    verdict: supports
    audited_at: 2026-06-07T071941Z
    note: std::partial_sum cumulative squared-error prefix sum; on-disk line 28.
  - citation: palace/utils/dorfler.cpp:36
    verdict: supports
    audited_at: 2026-06-07T071941Z
    note: lower_bound pivot on (1-fraction)*local_total; the threshold-finding pivot AND the single-rank over-mark over-coverage mechanism for law 4 (selects the largest E still achieving >=theta coverage); on-disk line 36.
  - citation: palace/utils/dorfler.cpp:163
    verdict: supports
    audited_at: 2026-06-07T071941Z
    note: error_threshold = min_threshold — the MULTI-RANK over-mark bracket-selection tie-break; comment :160-162 "rather over mark than under mark"; degenerates to identity single-rank (min==max==error_threshold, :64-67) returning the :36 pivot; the single-rank over-coverage mechanism is the :36 lower_bound; on-disk line 163.
  - citation: palace/utils/dorfler.cpp:167
    verdict: supports
    audited_at: 2026-06-07T071941Z
    note: MFEM_VERIFY(error_marked >= fraction * error.total) — the coverage post-condition (law 1); on-disk line 167.
  - citation: palace/drivers/basesolver.cpp:103
    verdict: supports
    audited_at: 2026-06-07T071941Z
    note: MarkedElements(const Vector &e, double threshold) — threshold→index-set; the if(e[i]>=threshold) ind.Append loop :109-112; on-disk line 103.
  - citation: palace/drivers/basesolver.cpp:223
    verdict: supports
    audited_at: 2026-06-07T071941Z
    note: ComputeDorflerThreshold(comm, indicators.Local(), refinement.update_fraction) ▷ MarkedElements — the dorfler_mark composition + θ binding; on-disk lines 223-225.
  - citation: palace/utils/configfile.hpp:119
    verdict: supports
    audited_at: 2026-06-07T071941Z
    note: update_fraction = 0.7 — the Dörfler θ config home in RefinementData; on-disk line 119.
  - citation: book/src/L1-L0/amr-estimate-mark-refine.md
    verdict: positive-cross-reference
    audited_at: 2026-06-07T071941Z
    note: the L1>L0 lowering theme; sub-pattern B is the mark verb; firm-flips this cycle with its two L1 endpoints.
```
```

```edit:book/src/L1/index.md
| [`dorfler_mark`](./dorfler_mark.md) | `Real -> Tensor[N] -> IndexSet[N]` (the Dörfler bulk-marking verb: smallest element index set `{ i : e_i ≥ threshold }` whose summed squared error covers ≥ θ of the total) | (leaf — consumes a per-element indicator vector + fraction θ, produces an index set; `flux_recovery_estimate` produces the indicators, the MFEM-opaque `refine` consumes the result — both `reference`, not deps) | `firm` (AMR mark verb; read single-rank — the cross-rank threshold bisection `palace/utils/dorfler.cpp:64-158` degenerates `min==max`, DIRECTIVE-1 deferred distributed note; L0: whole `ComputeDorflerThreshold` body `palace/utils/dorfler.cpp:14-171` (sort `:20`, partial-sum `:28`, **over-mark lower-bound pivot** `:36` (single-rank over-coverage mechanism; multi-rank bracket-selection tie-break `:163` comment `:160-162` degenerates to identity single-rank `:64-67`), coverage post-condition `MFEM_VERIFY` `:167-169`) + `MarkedElements` threshold→index-set `palace/drivers/basesolver.cpp:103-115` + caller `:220-233` + θ config home `palace/utils/configfile.hpp:97-119`; harvested cycle-122; firm-on-positive-structure, no-dedicated-test caveat non-gating per `set_subvector_zero`/`reciprocal` precedent; laws: coverage, minimality (bulk), θ-monotonicity, over-mark tie-break (load-bearing), permutation-equivariance, positive-scaling invariance; non-laws: not-additive, no-θ-additivity, no-reduction-order (single-rank); L1>L0: [`amr-estimate-mark-refine`](../L1-L0/amr-estimate-mark-refine.md) sub-pattern B) |
```

```edit:book/src/SUMMARY.md
# REPAIRER NOTE (Issue 2, build-clean fallback): the originally-proposed registration nested
# dorfler_mark under a NEW `AMR estimate & mark` group whose intro page
# `./L1/amr-estimate-mark-intro.md` does NOT exist on disk — a hard linkcheck2/mdbook missing-file
# error at rebuild. Authoring a group-intro page is beyond repairer mechanical scope. The safe
# build-clean fallback is a FLAT top-level registration of dorfler_mark.md in the L1 Part list (a
# top-level entry mdbook accepts), pointing only at the on-disk dorfler_mark.md — no broken link.
# Integrator: insert this single line as a top-level entry within the `# L1` Part (after the
# `- [Overview](./L1/index.md)` line / before the first group header is acceptable; alpha-by-leaf is
# not enforceable across the flat-vs-grouped boundary). DEFERRED re-nest: once the
# `amr-estimate-mark-intro.md` group-intro page is authored (c123 layer-intro-author, see OQ
# `SUMMARY group-intro amr-estimate-mark-intro.md needed`), this flat line + D1's flux_recovery_estimate
# flat line both re-nest under the `AMR estimate & mark` group header. D1 (flux_recovery_estimate)
# takes the SAME flat-fallback to avoid the same broken link.
- [dorfler_mark](./L1/dorfler_mark.md)
```

## Operator content
[The full firm chapter is authored inside the `new:book/src/L1/dorfler_mark.md` fenced block above —
signature `dorfler_mark :: Real -> Tensor[N] -> IndexSet[N]`, semantics (sort/partial-sum/lower-bound
pivot/threshold→set), the load-bearing over-mark tie-break, six algebraic laws + three non-laws,
record definitions (`IndexSet[N]`, `θ ← RefinementData.update_fraction`), variant axes, firm-status
justification, downward L0 lowering + deferred distributed note, and the evidence + `verified_against`
block. Not repeated here per the harvester fence-encloses-full-body discipline.]

## Supporting evidence

- The proposing report `abstractor:2026-06-07T054924Z-amr-estimate-mark-refine` authored the
  `amr-estimate-mark-refine` L1>L0 theme (`book/src/L1-L0/amr-estimate-mark-refine.md`), which names
  `dorfler_mark` as a rough-in lowering endpoint with the exact line anchors this harvest confirms
  (sort `:20`, partial-sum `:28`, pivot `:36`, tie-break `:163`, `MarkedElements` `:103-115`, caller
  `:223-224`). The harvest re-verified every anchor against the **on-disk** file (the codemap
  `read_range` drifts +1/+3 on this file's comment/brace boundaries — the c121 producer noted this).
- The planner (`reports/2026-06-07T071941Z-cycle-planner-cycle-122/CYCLE.md` row D2) confirmed the
  source anchors via codemap and scoped the single-rank reading + the deferred distributed note.
- Firm-on-positive-structure precedent: `book/src/L1/set_subvector_zero.md` §Status,
  `book/src/L1/reciprocal.md` — both firm on syntactic-identity laws with no dedicated unit test.

## Open questions / caveats

- **`record-RefinementData-needs-concept-definition-home`** (NEW) — `RefinementData`
  (`palace/utils/configfile.hpp:97-119`) is named by ≥2 chapters (this verb, `flux_recovery_estimate`,
  the `amr-estimate-mark-refine` theme, the lifecycle column). It currently has only a single-consumer
  inline definition in the theme (§Record definition there) and a θ-field reference here. Per the
  record-definition obligation (≥2 consumers → `concepts/<record>.md`), a
  `book/src/concepts/RefinementData.md` page should be authored (layer-intro-author) defining all
  fields (`tol`/`max_it`/`max_size`/`max_nc_levels`/`nonconformal`/`update_fraction`/...) +
  construction-time stratum + the `refinement.*` IoData surface home. Flagged, out of this
  one-operator scope.
- **`dorfler-coarsening-threshold-sibling-verb`** (NEW) — `ComputeDorflerCoarseningThreshold`
  (`palace/utils/dorfler.cpp:173-...`) is the *derefinement* sibling of this verb (marks the largest
  set making up θ of the *coarsening opportunities*; operates on a nonconforming `ParMesh` +
  derefinement-opportunity errors, a distinct input). Not folded into `dorfler_mark` (different input,
  different criterion-direction); flagged as a future AMR-cohort harvest if the coarsening path enters
  active scope (it is gated behind nonconforming derefinement, single-rank-valid but currently not on
  the AMR active front). Out of this one-operator scope.
- **`dorfler-cross-rank-bisection-distributed-note-deferred`** (EXISTING; this harvest confirms the
  single-rank reading) — the cross-rank threshold bisection (`dorfler.cpp:64-158`) is read single-rank
  degenerate per DIRECTIVE-1 and recorded as a deferred future-direction note (*Downward to L0*), NOT
  lifted. The multi-rank reduction-order dependency it would introduce is part of the deferred concern.
- **`amr-estimate-mark-refine-theme-firmness-gate`** (EXISTING) — this harvest discharges the
  `dorfler_mark` half; the theme firm-flips once D1's `flux_recovery_estimate` also lands firm this
  cycle (the two-endpoint well-foundedness gate, scheme §5). The integrator should flip the theme's
  `rank: rough-in` → `firm` (and the `amr-estimate-mark-refine.md` `## Status` lines `:57-69`/`:251`)
  once both endpoints are on disk firm — flagged for the integrator's cross-report finalize (the theme
  edit is NOT in this one-operator scope; D1 and D2 each land their endpoint).
- **SUMMARY group-intro `amr-estimate-mark-intro.md` needed** — the originally-proposed SUMMARY edit
  registered a NEW sub-chapter group `AMR estimate & mark` whose intro page does not yet exist. A new
  mdBook sub-chapter group requires an intro file (the `mesh-construction-intro.md` precedent when
  `build_mesh` opened the mesh group, c117). **REPAIRER-APPLIED (Issue 2):** the SUMMARY edit above was
  changed to the **flat-registration build-clean fallback** — `dorfler_mark.md` is now registered as a
  flat top-level L1 entry pointing only at the on-disk file, avoiding the broken-link to the
  nonexistent group-intro. **Deferred re-nest (c123 layer-intro-author):** author a minimal
  `book/src/L1/amr-estimate-mark-intro.md` group-intro seed (a `stub`-class seed is sufficient — the
  AMR estimate→mark sub-spine introducing `flux_recovery_estimate` + `dorfler_mark`), then re-nest BOTH
  flat lines (this verb + D1's `flux_recovery_estimate`) under the `- [AMR estimate & mark](./L1/amr-estimate-mark-intro.md)`
  group header. The group-intro is a **layer-intro-author** concern; it is NOT required for this
  finalize (the flat fallback keeps `linkcheck2` green without it). D1's `flux_recovery_estimate` takes
  the SAME flat fallback this cycle to avoid the identical broken link.
- **edge-retype follow-up** — `flux_recovery_estimate` (D1) and `dorfler_mark` (this) cross-reference
  each other; once both are on disk firm, the placeholder forward-references resolve to live nodes (the
  `reference` edges are correct — they are dataflow siblings, not `depends-on`). No retype needed; noted
  for completeness.

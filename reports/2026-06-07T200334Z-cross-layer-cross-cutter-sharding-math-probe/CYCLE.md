---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-07T201937Z
scope: L4↔L1 cross-cut — sharding-MATH non-destabilization probe (vertical arm), batch-43 LEAD WAVE-1
status: pending
integrated_at: 2026-06-07T210000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-133 (batch-43 OPENER, 1/3). Applied clean by integrator-per-report — audit-class, NO book mutation. Verdict gate-CLEAR-for-roadmap_goal-sketch (SPLIT-leaning-CLEAR): the general decomposition-reduce abstraction CLEAR (firm domain_energy_reduce precedent), the Dörfler cross-rank bisection NO-CLEAR (pure MPI, stays deferred OQ). Combined with the D2 lateral arm (ALL-GREEN) the WAVE-1 hard gate is CLEAR on both arms → WAVE-2 GREENLIT for c134. Promoted OQ sharding-math-non-destabilization-probe-vertical-arm-verdict. DIRECTIVE-1 MPI boundary intact."
---

# CYCLE: Cross-layer observation — sharding-MATH non-destabilization probe (vertical / cross-layer arm)

## Summary

Vertical (cross-layer) arm of the batch-43 HARD GATE that runs BEFORE any sharding-math lift. The
question: can the **sharding-as-decomposition-abstraction MATH** (domain decomposition / sub-problem
composition as a *mathematical* abstraction on tensor-field problems — NOT the MPI mechanics) be
expressed in the EXISTING L4→L1 spine vocabulary WITHOUT destabilizing the current abstraction spine?
I examined the one concrete on-file candidate the planner named — the Dörfler cross-rank
threshold-bisection reconciliation (`palace/utils/dorfler.cpp:101-166`, OQ
`dorfler-cross-rank-bisection-distributed-note-deferred`) — against the c121 `dorfler_mark` rough-in
that already absorbs its single-rank-degenerate form, and against the firm reduce/domain vocabulary a
CLEAR decomposition-reduce framing would have to compose by name.

**BOTTOM-LINE VERDICT: split, leaning CLEAR for the general abstraction.**
- The **specific Dörfler candidate is NO-CLEAR as a spine-math lift**: its cross-rank bisection is a
  pure **MPI-collective reconciliation** (a `GlobalMin`/`GlobalMax`/`GlobalSum`-driven binary search to
  agree a *single scalar threshold* across ranks). It generalizes to NOTHING in tensor-field algebra —
  the single-rank form is already firm and complete; the multi-rank delta is purely the deferred MPI
  mechanism. It stays the `dorfler-cross-rank-bisection-distributed-note-deferred` future note, NOT
  lifted.
- The **general decomposition-reduce abstraction IS CLEAR**: the firm `L4/domain_energy_reduce`
  ALREADY demonstrates a non-destabilizing domain-restricted-reduce framing — a per-domain `map`-collect
  composing existing firm primitives (`inner_product`, `apply`, `participation_ratio`) via
  `reference`-class sibling edges, with **partition-of-unity recorded as a config-conditional
  precondition (a NON-law), not a structural claim**. A `roadmap_goal`-class sub-domain
  restriction/compose sketch can be authored on top of this precedent WITHOUT re-rooting any firm node.
  This is the WAVE-2 hand-off the c134 planner can act on — **subject to D2's lateral firm-node
  stability set coming back GREEN** (D2 is the same-layer arm auditing exactly that closure).

## Observation kind

**Coverage gap (deferred-future kind) + Audit residue** — a deferred future-direction node (the OQ
sharding-math note) is being probed for liftability; the finding is which part is genuinely
spine-expressible (the decomposition-reduce abstraction) vs which part is irreducibly MPI mechanism
(the cross-rank scalar reconciliation). This is a GROUND-vs-ROUTE disposition call on a deferred node,
per `METHODOLOGY-GRADED-STACK.md` §2f.

## Specific finding

### Finding 1 — the Dörfler cross-rank bisection is purely an MPI-collective concern (NO-CLEAR for that candidate)

The c121 `dorfler_mark` rough-in already drew this boundary precisely, and re-reading the source
confirms it. `ComputeDorflerThreshold` (`palace/utils/dorfler.cpp:14-171`) computes a single-rank local
threshold by a sort + cumulative-squared-error prefix sum + `std::lower_bound` pivot
(`dorfler.cpp:20,28,36`). The **cross-rank apparatus** is:

- each rank computes a *different* local threshold (`dorfler.cpp:58-63` comment: "if a given processor
  has lots of low error elements, their value will be lower …");
- the common threshold is found by a binary search over `[min_threshold, max_threshold]` — the per-rank
  min/max via `Mpi::GlobalMin`/`GlobalMax` (`dorfler.cpp:66-67`);
- the bisection's stopping criteria use `Mpi::GlobalSum`-reduced marked-element and marked-error counts
  (`dorfler.cpp:107-108`, the loop `:100-158`);
- the tie-break `error_threshold = min_threshold` (`dorfler.cpp:163`, comment `:160-162`).

This is, mathematically, **"agree one global scalar (a threshold) across the union of per-rank local
data via reduce-collectives."** That is NOT a tensor-field decomposition abstraction — it is a
**distributed scalar-agreement protocol over a reduction**. There is no sub-domain *restriction
operator*, no *extension/prolongation*, no *partition-of-unity weighting* — the per-rank partition is
the MPI process grid, an artifact of the distribution mechanism, not a mathematical domain
decomposition the algebra would name. Read single-rank it **degenerates to identity** (`min == max ==
error_threshold`, `dorfler.cpp:64-67`); the bisection loop is entered only to confirm the exact local
threshold and exits immediately (`dorfler.cpp:125,127`). The c121 entry's *Downward to L0* already
records this as the deferred distributed concern (`book/src/L1/dorfler_mark.md:325-336`).

**Conclusion for candidate 1:** the cross-rank bisection generalizes to nothing spine-expressible. Were
it lifted, it would introduce a cross-rank reduction-order dependency (the multi-rank analog of the
`dorfler_mark` no-reduction-order non-law, `book/src/L1/dorfler_mark.md:209-214`) — i.e. it would touch
the load-bearing-numerical-trick surface, not the decomposition-abstraction surface. **NO-CLEAR as a
lift; stays the OQ future note.** It is correctly an MPI-collective concern bound to
`linalg/*`/`utils/communication.hpp`, all DIRECTIVE-1-OUT (cited below, NOT lifted).

### Finding 2 — the general decomposition-reduce abstraction has a non-destabilizing precedent already firm in the spine (CLEAR)

The codemap-confirmed fact the planner supplied — `linalg/*` carries NO Schwarz / domain-decomposition
solver primitive; sharding in Palace is purely the `Par*`/`Partition` MPI mechanism — means a CLEAR
spine-math framing cannot come from a Palace source op. It must come from **generalizing existing firm
tensor-field vocabulary.** That generalization already exists, in firm form, as `L4/domain_energy_reduce`:

- Its signature is a **per-domain map over a configured domain set** —
  `domain_energy_reduce :: DomainOpMap -> Field -> Scalar -> [DomainData]`, mapping each domain to a
  **domain-restricted** energy `energyᵢ = ½⟨field, M_idx field⟩` (`book/src/L4/domain_energy_reduce.md:72-85`).
- It is built entirely by **composing existing firm primitives**: `inner_product`, operator `apply`, and
  the firm `participation_ratio` quotient (`book/src/L4/domain_energy_reduce.md:85,153-160`). The
  domain-restricted operator `M_idx` IS the restriction — a per-domain SPD operator selecting that
  sub-domain's contribution (`domainpostoperator.cpp:262-274`, cited at lines 154-156).
- Its defining fold law is **map-independence / concatenation-homomorphism** — "each row depends only on
  its own domain's `(idx, M_idx)`; no inter-domain state … embarrassingly parallel over domains"
  (`book/src/L4/domain_energy_reduce.md:147-152`). This is *exactly* the algebraic shape a
  sub-domain-compose abstraction wants: independent sub-problem results combined by a homomorphic
  collect.
- Critically, **partition-of-unity is recorded as a config-conditional NON-law, not a structural claim**:
  `Σ pᵢ = 1` holds ONLY when the configured domain set partitions the field's support; Palace configures
  domains freely (overlapping / partial-coverage / partitioning), and the verb makes NO partition claim
  (`book/src/L4/domain_energy_reduce.md:172-178`). The entry even names the contrast: "a true
  partition-of-unity reduction where the sum-to-one is structural" (`:178`).

This is the load-bearing precedent: **the spine ALREADY treats domain-restriction as a per-index map
composing firm primitives, with partition/overlap as a precondition axis — NOT as a re-rooting of any
node.** A `roadmap_goal`-class "sub-domain restriction / compose" decomposition-abstraction sketch can
be authored as a *generalization in the same shape* (restrict → solve/reduce per sub-domain → compose
homomorphically, with partition-of-unity as the precondition that makes the compose lossless), wiring to
the firm roots (`domain_energy_reduce`, `inner_product`, `linear_combination`, `gram_reduce`,
`apply_linop`) via **`reference`-class edges** — which, by the graded-stack edge taxonomy, do NOT
constrain those nodes' rank and do NOT carry liveness onto them
(`METHODOLOGY-GRADED-STACK.md`; `book/src/methodology/resolution-ladder.md`). Every firm node stays
firm; `rank_violations=0` and the reachability baseline are preserved by construction.

### Finding 3 — the vertical (cross-layer) check: no L_{n+1}→L_n edge would be inverted or re-rooted

The cross-layer concern specific to this arm: would a decomposition-abstraction force any
**L4→L3→L2→L1 lowering** to re-root or invert direction? It would not, for the same reason the c121
`dorfler_mark` single-rank reading is clean: the decomposition-reduce is a **horizontal map over an
index/domain set at one layer**, composed of vertically-already-grounded primitives. The restriction
operator `M_idx`, the `inner_product`, the `apply` — each already has its own firm L4→L1 lowering;
mapping them over a domain index set adds a `map` combinator at the top, not a new vertical rotation.
The single deferred vertical concern (the cross-rank reduction-order dependency) belongs to the MPI
mechanism (Finding 1), which is DIRECTIVE-1-OUT and stays in the L1>L0 distributed note, not in any
lifted theme.

## HARD-GATE boundary honored and stated

**MPI / distributed itself stays OUT of active scope** (DIRECTIVE-1). The following are CITED as the
deferred-future mechanism ONLY and are explicitly **NOT proposed for lifting as active work**:

- `palace/linalg/rap.{hpp,cpp}` — `ParOperator` / RAP parallel assembly. NOT lifted.
- `palace/utils/geodata.{cpp,hpp}` — `Partition` / mesh-distribution protocol. NOT lifted.
- `palace/utils/communication.hpp:181-425` — the `Mpi::GlobalSum`/`GlobalMin`/`GlobalMax`/`Broadcast`/
  `Allgather` collectives (the Dörfler bisection's `:265-270`, `:251-263`). NOT lifted; under the
  single-rank reading rule these are identity (`book/src/L0/par-types-single-rank-reading.md:47-56`).
- `palace/utils/dorfler.cpp:64-158` — the cross-rank threshold bisection itself. NOT lifted; stays the
  `dorfler-cross-rank-bisection-distributed-note-deferred` future note.

The graded-stack baseline that any CLEAR proposal must preserve is HELD by construction for the WAVE-2
sketch I recommend: it lands as `roadmap_goal` (rank 0) wired by `reference`-class edges to firm roots,
so no firm node is re-rooted/downgraded, `rank_violations=0` holds, and reachability is unchanged (a
rank-0 node resting on references introduces no `depends-on` that could violate `rank(u) ≤ rank(v)`).
A candidate that instead tried to assert `depends-on` FROM a firm node TO the new abstraction (forcing
the firm node's rank down to 0, or making it depend on speculative math) would be a **NO-CLEAR** and is
NOT what I recommend.

## Recommendation

**VERDICT = CLEAR for the general decomposition-reduce abstraction; NO-CLEAR for the specific Dörfler
cross-rank candidate.** Hand to WAVE-2 (c134) with this scope split, **contingent on D2's lateral arm
returning the firm-node stability set GREEN** (D2 audits whether `gram_reduce` / `inner_product` /
`linear_combination` are closed under an index-set-partition restriction without re-rooting — the
closure my Finding 2 asserts at the `map`-composition level; D2 confirms it at the per-combinator level).

- **Dispatch `abstractor` on the `sharding-math-decomposition-abstraction-sketch` (WAVE-2, c134)** — a
  `roadmap_goal`-class sub-domain restriction/compose sketch GENERALIZING the firm
  `L4/domain_energy_reduce` per-domain-map shape (restrict via a sub-domain operator → reduce/solve per
  sub-domain → compose homomorphically; partition-of-unity as the precondition axis), composing the firm
  roots BY NAME via `reference`-class edges. MPI mechanics documented as the deferred mechanism, NOT
  lifted.
- **Do NOT lift the Dörfler cross-rank bisection** — record it (already recorded) as the canonical
  "agree-a-global-scalar-via-reduce-collective" MPI mechanism under the existing OQ note; it is the
  worked example of what the decomposition-abstraction is NOT (it is mechanism, not math).
- **Defer the final go/no-go to the c134 planner pending D2** — if D2 finds any firm combinator that
  would need re-rooting to support an index-set-partition restriction, that combinator's involvement
  flips to NO-CLEAR for the WAVE-2 sketch (the sketch then omits it or stays a thinner note). My
  cross-layer arm finds no vertical obstruction; the lateral closure is D2's call.

## Supporting evidence

- `palace/utils/dorfler.cpp:14-171` — `ComputeDorflerThreshold`; single-rank pivot `:20,28,36`;
  cross-rank min/max `:66-67`; bisection loop `:100-158`; `GlobalSum`-reduced stopping `:107-108`;
  tie-break `:163`; single-rank degeneration `:64-67`.
- `book/src/L1/dorfler_mark.md:69-81` (single-rank reading), `:209-214` (no-reduction-order non-law),
  `:264-268` (rank-multiplicity absorbed axis), `:325-336` (*Downward to L0* deferred distributed
  concern) — the c121 rough-in that already drew the math/mechanism boundary.
- `book/src/L4/domain_energy_reduce.md:72-85` (per-domain restricted-reduce signature), `:147-152`
  (map-independence / concatenation-homomorphism fold law), `:153-160` (composes `inner_product`/`apply`/
  `participation_ratio`), `:172-178` (partition-of-unity = config-conditional NON-law) — the firm
  non-destabilizing precedent.
- `book/src/L0/par-types-single-rank-reading.md:7-21,47-56` — the single-rank reading rule (all
  `Par*`/collectives → identity); the convention that keeps the MPI mechanism out of the algebra.
- `scaffolding/open-questions.md:1790-1793` (`dorfler-cross-rank-bisection-distributed-note-deferred`),
  `:1942` (the demand-gated trigger) — the deferred-future node under probe.
- `scaffolding/priorities.md:32-33,43,47-50` — the batch-43 LEAD framing (WAVE-1 hard gate / WAVE-2
  dep-the-probe / DIRECTIVE-1 boundary).
- Linter baseline to preserve (c132 finalize, re-confirmed c133 dispatch): `files=385, typed=324,
  reachable=163, reference_reachable=247, rank_violations=0` — held by construction for the recommended
  `roadmap_goal`-via-`reference`-edges WAVE-2 sketch.

## Open questions / caveats

- **This is the vertical arm only.** The verdict's CLEAR half asserts the firm primitives are closed
  under an index-set-partition restriction at the `map`-composition level (the `domain_energy_reduce`
  precedent). The **per-combinator closure** (`gram_reduce` / `inner_product` / `linear_combination`
  under restriction) is D2's lateral arm — if D2 returns any RED node, the WAVE-2 scope narrows
  accordingly. The two arms must be read together for the c134 go/no-go.
- **The decomposition-abstraction is exploratory `roadmap_goal`-class, not firm.** Even the CLEAR
  verdict licenses only a rank-0 future-direction sketch composing firm roots by reference — NOT a
  forced rectangular pull-up of the spine, NOT a firm new combinator (the redirect's
  no-forced-rectangular-pull-up still governs). Promotion off rank-0 would require a genuine consumer
  that names the decomposition by use, which does not exist in single-machine scope today.
- **Partition-of-unity is the load-bearing precondition.** The `domain_energy_reduce` `Σpᵢ=1`
  config-conditional non-law (`:172-178`) is the precedent for treating partition-vs-overlap as a
  precondition AXIS, not a structural guarantee — the WAVE-2 sketch must carry the same precondition
  honestly (a sub-domain compose is lossless ONLY under a partition-of-unity; overlapping/partial-coverage
  decompositions double-count / under-cover, exactly as the energy table does). Misstating this as a
  structural identity would be a false-grounding smell.
- **No book mutation performed** (audit-class dispatch, per the DISPATCH-phase write-authority
  partition). This CYCLE.md is the observation/audit report only.

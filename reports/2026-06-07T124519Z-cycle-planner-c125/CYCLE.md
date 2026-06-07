---
agent: cycle-planner
invoked_at: 2026-06-07T124519Z
scope: cycle-125 dispatch plan (batch-40 MIDDLE primary cycle; cycles 124/125/126; batch-40 meta fires after c126)
status: pending
---

# Cycle 125 dispatch plan

## Goals selected this cycle

Continue the lift-through tail (ASK-2 "A then B", batch-40 = the constructive-kernel
layer THEN the 5-driver L4-completeness capstone). c124 firmed the libCEED-substrate
arithmetic half (`basis_apply`+`quad_point_contract` firm) and landed the firm shape
home `concepts/element-local-tensor`; c125 (1) discharges the cheap-but-high-value
**45→47 firm-flip** that the now-firm shape home unblocks (`element_restrict` +
`geom_factor_build` + `libceed-quadrature-kernel-impl` rough-in→firm — completes the
constructive-kernel substrate sub-spine + fires the kernel-impl), then (2) takes the
first deepen-the-layer step of ASK-2 "A": lift the matrix-free FE operator-application
contraction chain `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` into a first-class **L2 combinator** composing
the now-firm substrate over the element-local rank-tensor shape family (the burn/GPU
backend-lowering contraction shape). A small disjoint **hygiene** pick clears the last
stale `design/l4_calculus` path instance + bundles the genuinely-open deferred GMG
sub-picks. Three dispatches, two waves (D2 depends on D1's firm-flip so its L2 rank
rests on firm substrate).

## Deliverable-presence verification

Per-dispatch, paste-inline evidence (skill `verify-dispatch-scope-not-already-discharged`).

**D1 — the 45→47 firm-flip (cross-report rank-propagation).** Targets are the 3 rough-in
nodes; flip is OPEN iff they are still rough-in on disk.
- `ls`/maturity (the firm-flip targets, must be `rough-in` = OPEN):
  ```
  element_restrict: rank: rough-in
  geom_factor_build: rank: rough-in
  libceed-quadrature-kernel-impl: rank: rough-in
  ```
  All three `rough-in` on disk → the flip has NOT been applied → OPEN.
- Shape-home (the dep whose firming unblocks the flip): `concepts/element-local-tensor.md`
  reads `rank: firm` on disk (c124 D5) → the well-foundedness cap on the two D4 ops has
  RISEN to firm; the flip is now warranted (each is firm-on-positive-structure: syntactic
  gather/scatter-add + setup-stratum-purity identities on positive libCEED source — laws
  not test-gated, the firm-on-positive-structure escape applies).
- OQ-ledger RESOLVED-grep: `grep -c 'libceed-substrate-rough-in-to-firm.*RESOLVED' ...` → `0`
  (the followup OQ `libceed-substrate-rough-in-to-firm-flip-and-45-to-47-tally-followup`
  is OPEN, opened c124, explicitly routes the flip to "c125, layer-intro-author/harvester +
  the integrator's cross-report rank-propagation").
- Structural-block check: none. The cap-rises-to-firm is the §(h) well-foundedness
  consequence of D5's firm shape home landing; c124 deliberately did NOT flip
  retroactively-within-D5's-apply (the targets were rough-in at D5 apply time) — c125 is
  the sanctioned cross-report propagation. NOT a test-gated promotion (firm-on-positive-
  structure escape). NOT on the STOP-PROPOSING negative list.

**D2 — the matrix-free operator-apply L2 combinator (ASK-2 "A" deepen-the-layer).** Open by
construction (a fresh L2 combinator with no prior-cycle history).
- `ls` (must be ABSENT = open by construction): `ls book/src/L2/*operator-apply* book/src/L2/*matrix-free*`
  → `ABSENT (open by construction)`. No L2 element-local/contraction op exists; the only
  L2 element-cohort files are `elementwise-gate-floors-intro.md` + `elementwise_product.md`
  (the BLAS pointwise family, unrelated).
- Composition target verified on disk: the L1 `libceed-quadrature-kernel-impl` already
  expresses `A(space,(Q,𝒟)) = Gᵀ ∘ B_𝒟ᵀ ∘ D(Q,geom) ∘ B_𝒟 ∘ G`
  (`L1/libceed-quadrature-kernel-impl.md:102`) over the firm `concepts/element-local-tensor`
  shape family (`Tensor[(E,L)]`/`[(E,P,C)]`/`[(E,P,G)]`, lines :72-76). The L2 lift is the
  iteration/fusion-rotation of that L1 form into the named contraction-chain combinator.
- Structural-block check: D2's L2 combinator resting on the substrate ops needs them firm
  to itself be firm (§(h) well-foundedness: rank(u) ≤ min deps). D1 flips them firm THIS
  cycle → D2 sequenced wave-2 (after D1) so the per-report integrator wires D2 onto the
  firmed substrate and D2 may claim firm; if D1 had not landed first, D2 would cap at
  rough-in. Open, not blocked. Open by construction (no prior-cycle history) — the four-step
  maturity check is N/A for the new file; the dep-firmness check is the live gate, satisfied
  by D1.

**D3 — hygiene bundle (the last stale path + genuinely-open GMG sub-picks).**
- Stale path count: `grep -rl 'design/l4_calculus' book/src/` →
  ```
  book/src/L1/multigrid-relaxation-smoother.md
  count: 1
  ```
  ONE remaining instance (c124 D3/D4 fixed the 4 substrate-op instances). OPEN, trivial
  one-line re-point to `semantics/index.md §1.2.2`.
- vcycle-recursive-combinator: OQ `vcycle-level-recursive-combinator-mining-candidate`
  OPEN (line 1642), `grep -c '...RESOLVED'` → `0`. The V-cycle `vcycle ps bs b0 l` recursion
  is NOT yet named L4 vocabulary (presented in-line in the GMG column). Mining candidate.
- GMG-smoother L3 partial-obstruction home: `ls book/src/L3/*smoother* *relaxation*` →
  `jacobi-smoother.md` + `smoother-intro.md` exist, but NO GMG V-cycle / distributive-
  relaxation L3 partial-obstruction home for the outer `pc_it` sweep. OPEN.
- **EXCLUDED from D3 (gate not fired):** `record-MultigridConfig-needs-definition-home` —
  `grep -rc 'MultigridConfig' book/src/` shows exactly ONE consumer
  (`feature/geometric-multigrid-preconditioner.L4.md`). The OQ's promotion bar is "if a 2nd
  consumer surfaces"; the 2nd consumer has NOT fired → structurally blocked, do NOT propose
  (the gate is unchanged since the line was authored). Stays single-consumer / in-chapter.
- **EXCLUDED (correctly declined c124, no new target):** the interpolator backward-reference-
  note trim — OQ `interpolator-backward-reference-note-trim-target-unidentified` records D7
  found NO stale backward-reference note in `L1/interpolator.md` (all references are faithful
  forward-consumer notes; c123 GROUNDED two inbound edges, the OPPOSITE of a trim). The OQ
  asks the next planner to "specify the exact file:line OR confirm moot." Verdict: **MOOT** —
  no target exists; D7's full read confirmed the file is clean. Recorded moot in priorities;
  NOT dispatched.

## Dispatches

**D1 — `harvester`, the 45→47 libCEED-substrate firm-flip (cross-report rank-propagation).**
- **scope:** Promote `L1/element_restrict`, `L1/geom_factor_build`, and
  `L1/libceed-quadrature-kernel-impl` from `rough-in → firm` on the **firm-on-positive-
  structure escape**, now that their shape-vocabulary home `concepts/element-local-tensor`
  is `firm` on disk (c124 D5). For each of the two D4 substrate ops: confirm the
  `## Status` promotion-route prose ("once `concepts/element-local-tensor` firms, this
  promotes rough-in → firm on the firm-on-positive-structure escape") is satisfied, flip the
  `rank:` frontmatter + the `## Status` line to `firm`, and update the frontmatter comment.
  For `libceed-quadrature-kernel-impl`: it caps at `min(deps)` over its 4 substrate deps;
  once all 4 are firm (basis_apply + quad_point_contract already firm c124; element_restrict
  + geom_factor_build firmed by this dispatch), the consumer re-caps to firm (its laws are
  syntactic-identity composition facts on the positively-read `AssembleCeedOperator`
  pipeline) — flip it firm too. **SOLE-OWNS the `L1/index.md` consolidated tally
  reconciliation**: the index is currently in a DRIFTED state carrying both `45` and `43`
  in different prose passages (the c124 D5 partial-update left stale `43` text from the
  pre-c117 era) — reconcile the firm grand-total to **47** (33 main + 4 FE-assembly +
  5 FE-space + 1 Mesh-construction + **4** libCEED-substrate, was 2), drain the stale `43`
  prose, and move the two flipped ops + the kernel-impl from the rough-in sub-list to the
  firm sub-list (libCEED-substrate sub-spine count 2→4). Closes OQ
  `libceed-substrate-rough-in-to-firm-flip-and-45-to-47-tally-followup`.
- **deps:** none.
- **rationale:** the integrator-signals c124 §Unblocked names this "the clean cross-report
  rank-propagation pick"; the followup OQ routes it explicitly to c125. Cheap + high-value:
  completes the constructive-kernel substrate sub-spine, fires the kernel-impl, and reconciles
  the drifted index tally. Priorities item-2 (`element-local-rank-tensor-front`) firm-flip
  consequence. Plan-tag `constructive-spine-kernels`.

**D2 — `abstractor`, the matrix-free operator-apply L2 contraction-chain combinator (ASK-2 "A").**
- **scope:** Author a new **L2 combinator** lifting the L1
  `libceed-quadrature-kernel-impl`'s `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` element-quadrature
  contraction chain into a first-class, named L2 form (canonical slug
  `book/src/L2/matrix-free-operator-apply.md` — the abstractor may refine the slug; STATE
  the chosen slug in the report) composing the now-firm substrate ops by name
  (`element_restrict` = G/Gᵀ, `basis_apply` = B_𝒟/B_𝒟ᵀ, `quad_point_contract` = D pointwise,
  `geom_factor_build` = the geometry-factor carrier) over the `concepts/element-local-tensor`
  rank-structured shape family (`Tensor[(N: ...)] → Tensor[(E,L)] → Tensor[(E,P,C)] → …`).
  This is the **fusion/iteration rotation** of the L1 kernel-impl into named composition:
  the L2 form is the contraction-chain *fold* (the burn/GPU backend-lowering shape — a
  sequence of tensor contractions over the element-local axes). Classify sum-factorization
  as a **transparent performance trick** (the L1/L2 form is the unfolded contraction; the
  factored evaluation order is a one-line note). Carry the matrix-free-vs-assembled-COO
  duality note (the L1 kernel-impl's `CeedOperatorAssembleCOO` derived-materialization at
  `operator.cpp:483` is the *assembled* alternative; the matrix-free apply is the primary).
  Author the `L2-L1/matrix-free-operator-apply-*` lowering theme IF the L2→L1 rotation is a
  genuine vocabulary shift (NOT if it is identity-in-named-terms — a degenerate lowering is a
  smell; resolve as an in-line note per the redirect). Set `status:` per clean-gate: firm IFF
  the L2 form composes the (D1-firmed) substrate cleanly and its laws are syntactic-identity
  composition facts on positive source; otherwise rough-in with a stated promotion condition.
  Source anchors (codemap-verified): the element-wise apply loop
  `palace/fem/libceed/operator.cpp:174` (`CeedOperatorApplyAdd`), the master assembler
  `palace/fem/libceed/integrator.cpp:423-445` (`AssembleCeedOperator`), the build-operator
  apply `:419`, the geometry-factor build `:340-419`, the basis-eval/pointwise contraction
  `:451-512`.
- **deps:** D1 (D2 composes the substrate ops that D1 flips firm; sequencing D2 after D1 lets
  the per-report integrator wire D2 onto the firmed substrate so D2's L2 rank rests on firm
  deps per §(h) well-foundedness — if D2 ran before D1 landed, it would cap at rough-in).
- **rationale:** the first deepen-the-layer step of ASK-2 "A" (memory
  `project_ask2_forward_direction_batch41`) — "matrix-free FE assembly as first-class L1/L2
  (sum-factorization, geometry factors)…the most burn/GPU-relevant build — matrix-free
  assembly IS the L4 backend-lowering contraction shape." Genuine vocabulary opportunity (no
  L2 element-local/contraction op exists). Priorities item-2 deepened from "firm the
  substrate" into "build the layer." Plan-tag `constructive-spine-kernels`. **fan-out: HIGH.**

**D3 — `combinator-miner`, the GMG/hygiene bundle (stale-path fix + vcycle-combinator + L3-smoother home).**
- **scope:** Three disjoint genuinely-open picks: **(a)** re-point the LAST stale
  `book/src/design/l4_calculus.md §1.2.2` citation in `book/src/L1/multigrid-relaxation-
  smoother.md:113` → the live `book/src/semantics/index.md §1.2.2` (the c124 substring-rewrite
  reached the 4 substrate ops but not this batch-37-era file; cheap one-line drift fix —
  closes the residual of OQ `batch-37-era-stale-design-l4-calculus-path-drift-sweep`).
  **(b)** Evaluate the **V-cycle level-recursive combinator** (`vcycle ps bs b0 l` recursing
  to `l-1`: restrict → recurse → prolong) as a combinator-miner candidate — it is presented
  in-line in the GMG column, not as named L4 vocabulary, and recurs in AMG / auxiliary-space
  transfers (OQ `vcycle-level-recursive-combinator-mining-candidate`). If the level-recursive
  restrict→recurse→prolong pattern is a genuine recurrent combinator, propose it
  (replace-and-propagate, NOT mine-and-strand — wire the GMG column's in-line recursion to
  name it); apply the over-unification guard if it does not cleanly generalize. **(c)** Assess
  whether the GMG **outer `pc_it` smoother-sweep** warrants an **L3 partial-obstruction home**
  (the iteration whose per-step body lifts but whose loop is a witnessed sequential-
  obstruction — the chebyshev/jacobi-smoother L3 cohort precedent `L3/jacobi-smoother.md`);
  author it as a partial-obstruction L3 chapter IF the sweep is a distinct un-liftable loop
  not already covered by `L3/chebyshev` / `L3/jacobi-smoother`, otherwise record WHY it is
  already covered (audit-first; do not manufacture a redundant home). Keep each pick to its
  own file region. **EXCLUDE** `MultigridConfig` (2nd-consumer gate not fired) and the
  interpolator note trim (moot — no target).
- **deps:** none (all three picks touch files disjoint from D1/D2).
- **rationale:** clears the last drifted path instance + the two genuinely-open deferred
  c124 item-5 GMG sub-picks (the integrator c124 §Suggested next dispatches +
  `gmg-vcycle-recursive-combinator` from the c123 signal). LOW fan-out, bundle-able.
  Plan-tag `gmg-amr-hygiene`.

## Overlap analysis

- **D1 ↔ D2:** D1 edits `L1/{element_restrict,geom_factor_build,libceed-quadrature-kernel-
  impl}.md` + the `L1/index.md` firm tally. D2 CREATES `L2/matrix-free-operator-apply.md` +
  appends one `L2/index.md` dep-map row + a `SUMMARY.md` row + (possibly) a new `L2-L1/`
  theme, and adds `reference`/`depends-on` edges TO the L1 substrate ops (it does NOT modify
  the L1 op bodies — it points at them). The ONLY potential shared touch is D2 reading the
  L1 substrate ops' `rank:` to set its own — which is a DEPENDENCY (D2 after D1), not an
  overlapping write. Distinct files / distinct anchors → **SEQUENTIAL by dependency** (D2
  after D1), not by overlap. No shared consolidated-tally (D1 sole-owns the `L1/index.md`
  tally; D2 sole-owns its `L2/index.md` row + `SUMMARY.md` row).
- **D1 ↔ D3:** disjoint. D1 = `L1/{3 substrate ops}.md` + `L1/index.md` tally. D3 =
  `L1/multigrid-relaxation-smoother.md` (path fix) + the GMG feature column / L4 vcycle prose
  + a possible new `L3/` smoother home + `SUMMARY`/`L3/index` rows for any new L3 chapter. No
  shared file, no shared anchor. **PARALLEL.**
- **D2 ↔ D3:** disjoint. D2 = `L2/` + `L2-L1/` + `L2/index` + `SUMMARY` (L2 region). D3 =
  `L1/` + GMG-column + possible `L3/` + `SUMMARY` (L3 region, if it adds an L3 chapter). Both
  may append to `SUMMARY.md` but in DISJOINT Part regions (D2 the `# L2` Part, D3 the `# L3`
  Part) — per the conflict-tolerance philosophy these are distinct-anchor appends, parallel-
  safe (per-report integrator re-reads SUMMARY off disk before each edit). **PARALLEL** (mark
  parallel when in doubt; a mild SUMMARY line-shift is cheaply merged by the per-report
  integrator and surfaces as an integrator-signals data point if it conflicts).

## Sequencing schedule

- **Wave 1 (parallel):** D1 (firm-flip + tally), D3 (hygiene bundle). Disjoint file regions.
- **Wave 2 (after D1's report lands):** D2 (matrix-free L2 combinator) — sequenced after D1
  so the per-report integrator wires D2's `depends-on`/`reference` edges onto the
  firm-on-disk substrate ops and D2's L2 rank rests on firm deps (§(h) well-foundedness).
  D2 may run in the same dispatch wave physically; the ORDERING constraint is that the
  per-report integration of D2 follows D1 so D2's claimed rank reflects the firmed substrate.

One `integrator-finalize` at cycle end (rebuild book + commit + push + housekeeping); the
book is NOT rebuilt between waves.

## RE-discharge re-check (batch-40, on building these consumers)

- **No NEW RE fires/discharges this cycle by construction** — c124 already FIRED RE3 + GROUNDED
  RE11 + DISCHARGED RE6. D1 firm-flips do not move the RE set (the substrate ops are already
  reachable via `libceed-quadrature-kernel-impl` → the `fe_assemble` fold's feature-column
  inbound edges; the flip changes their RANK, not their reachability). D2's L2 combinator adds
  faithful `depends-on` edges from the new L2 node to the now-firm L1 substrate — this further
  GROUNDS the substrate (a second faithful consumer) but does not change the residual RE set
  (RE3 already fired; RE4 still consumer-gated with no c125 consumer; RE6 already discharged).
  The batch-40 meta (after c126) records the RE-set dispositions per the rebuilt graph and
  updates `scaffolding/graded-stack-baseline-exceptions.md` (meta write-territory; the
  per-report integrators FLAG but do not touch it).
- **Standing gates re-confirmed clean:** kernel-API/impl integrity (D1's `libceed-quadrature-
  kernel-impl` KEEPS its `kernel-api` obstruction surface — the firm-flip is on the
  kernel-IMPL node, NOT the kernel-api node; the `realizes-kernel-api` edge stays `reference`-
  class — `lowering-verifier` re-confirms as the impl firms, but NO lowering-verifier dispatch
  is needed this cycle since the c124 D2 audit already confirmed the correspondence FAITHFUL
  and D1 only changes rank). DIRECTIVE-1 (MPI/sharding OUT) — D2 reads the libCEED apply loop
  single-rank (the element-wise apply is by-composition parallel, no MPI lift); D3's GMG/
  smoother picks read RAP/relaxation single-rank.

## Open questions / caveats

- **The L1/index tally is in a genuinely drifted state** (carries both `45` and `43` in
  different prose passages — the c124 D5 partial-update did not drain the pre-c117-era `43`
  text). D1 SOLE-OWNS the reconciliation to 47 and must drain ALL stale-count prose, not just
  bump the headline. Flagged so D1 does not leave a third inconsistent number. (For the
  batch-40 meta: the index-tally prose has accreted multi-era count-history; a one-time
  prose-compaction of the L1/index firm-count narrative may be worth a meta hygiene pick.)
- **D2's L2-L1 lowering theme is conditional** — author it ONLY if the L2→L1 rotation is a
  genuine vocabulary shift; if the L2 contraction-chain form is identity-in-named-terms to the
  L1 kernel-impl (likely, since the L1 form already states the chain), resolve as an in-line
  "Downward to L1" note per the redirect's degenerate-identity-lowering-is-a-smell rule, NOT a
  mirrored theme. The abstractor decides at authoring; flagged so a thin mirror theme is not
  forced.
- **D3 pick (c) is audit-first** — the GMG-smoother L3 partial-obstruction home is authored
  ONLY if the outer `pc_it` sweep is a distinct un-liftable loop not already covered by
  `L3/chebyshev` / `L3/jacobi-smoother`; the combinator-miner records WHY it is covered if so
  (do not manufacture a redundant L3 home). If pick (c) resolves to "already covered," D3
  reduces to picks (a)+(b) only — acceptable (LOW-fan-out hygiene).
- **batch-40 forward shape** — c125 takes the FIRST deepen-the-layer step (the L2 contraction
  combinator). The remaining ASK-2 "A" depth (matrix-free assembly fused with `fe_assemble`'s
  term-fold at L4; the L4 backend-lowering contraction surface) + the "B" 5-driver
  L4-completeness capstone are c126 / batch-41 candidates. The element-local-rank-tensor front
  may carry into batch-41 (a genuine multi-cycle vocabulary shift) — the batch-40 meta (after
  c126) reshapes the head per the A-then-B direction.

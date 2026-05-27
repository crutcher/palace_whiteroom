# Open questions ledger

Cross-cycle ledger of open questions about the target source or methodology. Replaces the old `questions.md` (which stays in place as the archive of seed questions from BOOTSTRAP).

**Format** (one section per question):

```yaml
---
slug: short-kebab-case
opened_at: cycle-NNN | YYYY-MM-DD
opened_by: <agent-name> | human
last_revisited: cycle-NNN | null
status: open | investigating | answered | dropped
answered_at: cycle-NNN  (when status=answered)
answered_in: <commit-sha> | <slice-path> | <ledger-pattern>  (when status=answered)
---
```

Each section: **slug**, **question text** (1–3 sentences), **context** (where this surfaced and why), and **status**.

**Discipline:**
- Any agent appends; never edits existing sections (except status).
- Integrator promotes per-report CYCLE.md "Open questions / caveats" sections into this ledger on landing.
- Meta-phase reviews open questions periodically and may drop stale ones (status `dropped` with reason) or promote into friction-ledger / skill-candidates.
- Cycle-planner reads as a priority input — long-open questions get attention.

## Open

```yaml
---
slug: axpy-l1-l0-three-subpatterns
opened_at: pilot-1
opened_by: harvester
status: open
---
```

The L1>L0 lowering theme for `axpy` will need to cover three sub-patterns observed in the L0 corpus: bare `y.Add(α, x)` / `y.AXPY(α, x)` member call; `α == 1` specialisation to `operator+=` (vector.cpp:704-706); `α == -1` specialisation to `Subtract` (vector.hpp:118). All three lower from the same L1 `axpy`; the theme should note per-constant L0 pattern-match rules. Routes to abstractor when dispatched.

```yaml
---
slug: axpby-axpbypcz-next-harvest
opened_at: pilot-1
opened_by: harvester
status: open
---
```

Palace has `AXPBY` (`y = α·x + β·y`) and `AXPBYPCZ` (`z = α·x + β·y + γ·z`) at `palace/linalg/vector.hpp:130-136`. These are L1-distinct operators worth harvesting. Includes a fusion-vs-decomposition trade-off (should `axpby` be primitive, or `axpy ∘ scal`? Palace fuses at L0). Record decision in `scaffolding/decisions/axpby-as-primitive.md` once made.

```yaml
---
slug: scalar-promotion-typing-rule
opened_at: pilot-1
opened_by: harvester
status: open
---
```

The complex-scalar overload `AXPY(double, ComplexVector, ComplexVector)` (`vector.cpp:715-718`) raises whether the L1 signature should formalise real→complex scalar promotion as a typing rule rather than per-operator prose. Long-term L1 type-system concern; revisit after several real/complex operators are harvested.

```yaml
---
slug: l1-index-refresh
opened_at: pilot-1
opened_by: integrator
status: open
---
```

`book/src/L1/index.md` may want an intro refresh now that the dep-map has one entry (axpy). Should mention populated dep-map and link to the operator. Routes to layer-intro-author. Low priority — defer until ≥3 L1 operators land.

```yaml
---
slug: concepts-dot-return-type-correction
opened_at: cycle-002
opened_by: harvester
status: open
---
```

`book/src/concepts/dot.md:28-30` claims `ComplexVector::Dot` returns a real scalar (`α ← ⟨x, y⟩` real-projected). This is factually wrong: the C++ implementation (`palace/linalg/vector.cpp:263-267`) returns `std::complex<double>`. The real-projection happens at *call sites* via `std::real(...)` or `std::abs(...)`, not inside `Dot`. The L1 entry `book/src/L1/dot.md` now supersedes this claim; concept page needs the correction. Routes to `same-layer-cross-cutter` (or `layer-intro-author` if cycle-planner prefers).

```yaml
---
slug: concepts-dot-dotc-and-inverted-conjugation
opened_at: cycle-002
opened_by: harvester
status: open
---
```

`book/src/concepts/dot.md:17-18` references `linalg::Dotc` and inverts the conjugation role between `Dot` and `TransposeDot`. A full-tree grep of `reference/palace/` finds zero occurrences of `Dotc`. The unconjugated complex form is `ComplexVector::TransposeDot` (method-form only — no free-function `linalg::TransposeDot`). The free-function `linalg::Dot` is conjugated for complex inputs. Concept page needs both corrections: (a) remove `Dotc` reference, (b) fix the inverted conjugation role-assignment between `Dot` (Hermitian) and `TransposeDot` (unconjugated bilinear). Bundled with `concepts-dot-return-type-correction` for the same follow-up.

```yaml
---
slug: l1-l0-dot-lowering-asymmetry
opened_at: cycle-002
opened_by: harvester
status: open
---
```

When the L1>L0 lowering theme for `dot` gets authored, it must record (a) the local-kernel + MPI_Allreduce two-step (single-rank-equivalent though it is per scope) and (b) the receiver-vs-argument conjugation asymmetry on the method form `(*this).Dot(arg) = argᴴ · (*this)` vs the free-function form `linalg::Dot(comm, x, y) = xᴴ y` (which conjugates the first argument). This sign-of-which-arg-is-conjugated trap is exactly the kind of friction the L1>L0 lowering theme should catch. Routes to abstractor.

```yaml
---
slug: dot-reduction-tree-determinism-survey
opened_at: cycle-002
opened_by: harvester
status: open
---
```

`dot` classifies reduction-tree non-associativity as a load-bearing numerical claim (per CLAUDE.md "Optimization tricks vs. base algebra"). Whether Palace claims bit-determinism for any of its dot uses (e.g. CG convergence test, eigenvalue residual norm) is not surveyed. Worth a combinator-miner or cross-cutter pass when it becomes relevant.

```yaml
---
slug: axpby-axpy-scal-decomposition-decision
opened_at: cycle-002
opened_by: abstractor
status: answered
answered_at: cycle-003
answered_in: scaffolding/decisions/axpby-as-primitive.md
---
```

When harvester promotes `axpby` (`y_new = α·x + β·y_old`), the trade-off is: treat `axpby` as a fused primitive (matches L0 shape; one-call lowering) or decompose into `axpy + scal` (cleaner algebra; L0 fusion becomes a transparent performance trick). The `axpby-mutation-rotation` theme (this cycle) is robust to either decision (see Subsumption relation in the theme), but the LHS prose will need a small lift once harvester decides. Record decision in `scaffolding/decisions/axpby-as-primitive.md` once made.

**Answered cycle-003:** harvester chose fused primitive. See `scaffolding/decisions/axpby-as-primitive.md` for full rationale (algebraic, engineering, trade-offs). The fused form matches Palace's L0 shape one-to-one, composes well with the forthcoming `axpbypcz`, and is the form already assumed by the cycle-002 `axpby-mutation-rotation` lowering theme. `axpy` remains in the L1 dep-map as a sibling leaf (subsumption-not-dependency).

```yaml
---
slug: axpby-lowering-verifier-audit
opened_at: cycle-002
opened_by: abstractor
status: open
---
```

The L1>L0 theme `axpby-mutation-rotation` sketches three sub-pattern recognition rules (general α, α==1, α==-1). The theme's Status section calls for a `lowering-verifier` audit to confirm sub-rule recognition matches the L0 corpus exhaustively. Specifically: (a) confirm no L0 site relies on bit-for-bit IEEE behaviour distinguishing `y += x` from `1.0 * x + y` (sub-pattern B caveat); (b) verify the bare-Add no-scalar overload `y.Add(x)` is or is not present in the Palace corpus (theme caveat #4 says no current site uses it). Routes to lowering-verifier.

```yaml
---
slug: krylov-step-layer-placement
opened_at: cycle-002
opened_by: combinator-miner
status: open
---
```

`krylov-step` rough-in is currently placed at L2 (primitive composition). Named step-functions live in L4 prose; the L2 form is the primitive composition; complementary placements. Cross-layer-cross-cutter should examine whether `krylov-step` deserves L2, L4, or both with a lowering edge. Combinator-miner's read: L2 captures primitive composition, L4 captures typed wrapping. Routes to cross-layer-cross-cutter.

```yaml
---
slug: krylov-step-naming-and-borderline-cases
opened_at: cycle-002
opened_by: combinator-miner
status: open
---
```

"krylov-step" stretches to cover Chebyshev (not strictly a Krylov-subspace method per Saad 2003); alternatives `iterative-step-kernel`, `fold-step`, `solver-step` all less precise. Additionally, the GMRES-Givens-stream sub-instance (`polynomial_recurrence_step.md:147-155`) has a different primitive sequence (`givens_apply`/`givens_generate` rather than `apply_linop`+`axpy`+`dot`) — strict reading excludes; broad reading includes. Both questions defer to harvester when `krylov-step` is formalized.

```yaml
---
slug: krylov-step-harvester-deliverables
opened_at: cycle-002
opened_by: combinator-miner
status: open
---
```

When harvester promotes `krylov-step` from rough-in to firm, deliverables include: (i) canonical signature, (ii) variant-axis dispatch sites (six axes already enumerated by combinator-miner), (iii) algebraic laws section (read: no internal algebraic laws — kernel of a fold; only law is L4 §3.8 demand-pruning over `output_extras`), (iv) resolution of the naming caveat (`krylov-step-naming-and-borderline-cases`), (v) the GMRES-Givens-stream borderline-case decision, (vi) explicit no-Palace-source-citation status (methodology-level concept; derived from five `book/src/spec/slices/` citations, not from `reference/palace/`). Harvester deliverable could also include a slice-template for future Krylov/Chebyshev/etc. slices.

```yaml
---
slug: l2-dep-map-format-vs-l1
opened_at: cycle-002
opened_by: integrator
status: open
---
```

The L2 dep-map now uses the same 4-column markdown table as L1 (`Operator | Signature | Dependencies | Status`), with the richer metadata from combinator-miner's original tree-style rough-in moved into Working Notes (per repairer). This sets the L2 layer precedent. Worth meta-phase examination whether the Working-Notes overflow pattern is reusable across L2/L3/L4 or whether a fifth column (e.g. `Notes/Provenance`) would be cleaner.

```yaml
---
slug: concepts-nrm2-stability-claim-correction
opened_at: cycle-003
opened_by: harvester
status: open
---
```

`book/src/concepts/nrm2.md:9` claims Palace uses "scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow". This is **factually wrong**: `palace/linalg/vector.hpp:255-260` shows Palace's `linalg::Norml2` is the naive `√⟨x,x⟩` form (literal one-line `std::sqrt(std::abs(Dot(comm, x, x)))`). Either Palace's `dot` kernel ultimately bottoms out in a Hypre / BLAS routine that scales internally (worth verifying — L1>L0 lowering concern), or Palace is naive and the concept page is simply wrong. Routes to same-layer-cross-cutter (concept-page reconciliation) or layer-intro-author (per cycle-003 follow-up).

```yaml
---
slug: nrm2-B-weighted-energy-norm-harvest
opened_at: cycle-003
opened_by: harvester
status: open
---
```

The L0 surface uses overloading: `linalg::Norml2(comm, x)` (this cycle's firm `nrm2`) and `linalg::Norml2(comm, x, B, Bx)` (operator-weighted norm `‖x‖_B = √(xᴴ B x)` at `operator.cpp:600-619`). At L1 these are distinct operators. The B-weighted form requires an `apply`-style operator-application primitive (not yet in the L1 dep-map), an SPD precondition on `B`, and a workspace `Bx`. Queue a `nrm2_B` or `energy_norm` harvester invocation once `apply` (matrix-vector multiplication) is firm at L1.

```yaml
---
slug: nrm2-std-abs-defensive-guard-classification
opened_at: cycle-003
opened_by: harvester
status: open
---
```

The L0 expression at `vector.hpp:259` is `std::sqrt(std::abs(Dot(comm, x, x)))`. For real `x`, `dot(x,x) = Σ x[i]²` is non-negative in exact arithmetic but can be slightly negative by round-off. For complex `x`, `std::abs(std::complex<double>)` computes modulus, but Hermitian self-dot has `im = 0` exactly. The interpretation as "defensive guard, not semantic projection" needs verification in mixed-precision contexts where the sum might overflow/underflow before reaching `std::abs`. Routes to cross-cutter or critic for confirmation.

```yaml
---
slug: nrm2-lowering-theme-deliverables
opened_at: cycle-003
opened_by: harvester
status: open
---
```

When `nrm2-mutation-rotation` (or analogous L1>L0 lowering theme) is authored, it should: (a) record the `Dot` + `MPI_Allreduce` + `sqrt` chain inheriting the dot lowering's MPI-collective theme; (b) record the `std::abs` defensive guard against round-off-induced sub-zero `dot(x, x)`; (c) record the method-form `Vector::Norml2()` vs free-function `linalg::Norml2(comm, x)` vs wrapper `ErrorIndicator::Norml2(comm)` surface as transparent caller-side conveniences; (d) record the B-weighted overload's existence as a separate-but-overloaded symbol at L0 with a different L1 referent. Routes to abstractor.

```yaml
---
slug: l1-index-refresh-trigger-met
opened_at: cycle-003
opened_by: harvester
status: open
---
```

Pilot-1's `l1-index-refresh` set "≥3 L1 operators" as the threshold for an intro refresh. After cycle-003 the L1 dep-map has 4 firm operators (`axpy`, `dot`, `nrm2`, `axpby`). The trigger is met. Schedule a `layer-intro-author` invocation for the L1 Part overview in cycle-004. Bundles cleanly with the `concepts/dot.md` rewrite (also cycle-004) under the same role.

```yaml
---
slug: scal-primitive-l1-harvest
opened_at: cycle-003
opened_by: harvester
status: open
---
```

`scal :: (β, y) → β·y` is referenced in `axpby` laws 2 and 3 as a future primitive (cosmetic one-line update once it lands). `scal` also appears independently in normalisation (`linalg::Normalize` at `vector.hpp:262-270` does `x *= 1.0 / norm`) and in CG's `p = β·p + z` line. Queue as a harvester target — small primitive, mostly straightforward L0 form, blocks no further work.

```yaml
---
slug: axpbypcz-l1-harvest
opened_at: cycle-003
opened_by: harvester
status: open
---
```

Closes the `axpbypcz` half of `axpby-axpbypcz-next-harvest`. The L0 evidence at `vector.cpp:745-758` shows `AXPBYPCZ` real-path branches on `γ == 0` and delegates to `AXPBY`, confirming the subsumption chain `axpy ≺ axpby ≺ axpbypcz`. Next harvester invocation should mirror the fused-primitive decision for `axpbypcz` for consistency. A new abstractor sketch of `axpbypcz-mutation-rotation` (companion theme) is also pending; cycle-planner may want to schedule both together.

```yaml
---
slug: axpby-corpus-coverage-exhaustive-indexing
opened_at: cycle-003
opened_by: lowering-verifier
status: open
---
```

The cycle-003 lowering-verifier audit confirmed the `axpby-mutation-rotation` theme is **partially-supported** for coverage: the cited set is correct but illustrative (~25 additional axpy-shaped sites exist beyond cited). Exhaustive corpus indexing deferred. Three L0 forms (`ComplexVector::Subtract(α, x)`, `ComplexVector::operator-=`, `linalg::AXPY(complex, ComplexVector, ComplexVector)` specialisation at `vector.cpp:720-724`) are **defined-not-used**. Routes to cross-cutter or a follow-on lowering-verifier for the exhaustive enumeration.

```yaml
---
slug: lowering-verifier-yaml-in-prose-channel-format
opened_at: cycle-003
opened_by: lowering-verifier
status: open
---
```

The cycle-003 lowering-verifier audit embeds machine-readable `verified_against:` YAML inside a prose mdBook chapter, with the report flagging this as a parsing assumption (`cross-layer-cross-cutter` is expected to parse the block by leading keyword). No spec exists in `scaffolding/` or `.claude/agents/`. Meta-phase should decide: (a) fenced YAML code block, (b) explicit channel-format spec, or (c) move to sidecar `.yaml` file. Routes to meta-phase for channel-format decision.

```yaml
---
slug: axpbypcz-internal-sub-pattern-A
opened_at: cycle-003
opened_by: lowering-verifier
status: open
---
```

The free-function `AXPBYPCZ` template at `vector.cpp:756` itself lowers internally via `AXPBY(...); z.Add(beta, y);` (real-Vector path, when γ≠0). This is an L0-internal lowering — not a sub-pattern A site in application code, but a sub-pattern A site within an L0 lowering composition. Out of scope for cycle-003 audit; relevant if the future `axpbypcz-mutation-rotation` theme tries to describe the AXPBY+Add fusion. Routes to whichever cycle authors that theme.

```yaml
---
slug: axpy-test-linkages-deferred
opened_at: cycle-003
opened_by: lowering-verifier
status: open
---
```

The cycle-003 audit was source-only; no test cross-check performed. `reference/palace/test/unit/` does not appear to have a dedicated axpy unit-test. Recommend a follow-up cycle add test-linkage entries under `scaffolding/test-linkages/` if axpy semantics are exercised via solver-level integration tests. Routes to harvester or a test-linkage agent.

```yaml
---
slug: concepts-page-authorship-role-scope
opened_at: cycle-003
opened_by: same-layer-cross-cutter
status: open
---
```

The role-routing table in CLAUDE.md §"The 13 agents" doesn't explicitly assign `concepts/` page authorship to any of the 13 agents. `layer-intro-author` is described as authoring "L_n / L_{n+1}>L_n Part overviews + dep-maps." `concepts/` is a third category (cross-cutting prose, indexed by primitive rather than layer). The cycle-003 same-layer-cross-cutter routed the `concepts/dot.md` rewrite to `layer-intro-author` as closest-existing-fit. Meta-phase should decide: (a) explicitly broaden `layer-intro-author`'s scope to include `concepts/`, (b) add a `concept-page-author` role, or (c) decide that `concepts/` is being absorbed into per-layer chapters and should not receive net-new authorship. Routes to meta-phase.

```yaml
---
slug: concepts-pre-layered-era-sweep
opened_at: cycle-003
opened_by: same-layer-cross-cutter
status: open
---
```

Only `concepts/dot.md` was inspected by the cycle-003 cross-cutter; the same pre-layered-era authorship pattern likely affects other concept pages (e.g. `concepts/axpy.md`, `concepts/nrm2.md`, `concepts/orthogonalization.md`). A sweep is warranted to surface wrong-signature / hallucinated-symbol risks. Cycle-003 nrm2 harvester already flagged `concepts/nrm2.md:9` separately (see `concepts-nrm2-stability-claim-correction`); the cumulative signal suggests the sweep is high-value. Candidate cycle-005 dispatch (after cycle-004 dot rewrite establishes the pattern).

```yaml
---
slug: dot-blas-heritage-framing-salvage
opened_at: cycle-003
opened_by: same-layer-cross-cutter
status: open
---
```

`concepts/dot.md`'s "Background" section ties Palace's dot to BLAS `ddot`/`zdotc` heritage. The framing is partly useful (Palace is BLAS-flavoured); only the factual claims about Palace's actual return type and symbol names are wrong. The cycle-004 rewrite should keep the BLAS-heritage framing while correcting the specifics. Note for the dispatched agent.

```yaml
---
slug: dot-backpointer-staleness-after-rewrite
opened_at: cycle-003
opened_by: same-layer-cross-cutter
status: open
---
```

`L1/dot.md:17` currently contains a warning that the concept page is wrong. If `concepts/dot.md` is corrected in cycle-004 but the back-pointer warning isn't deleted, future readers will be confused. The cycle-004 REPORT should explicitly propose the `L1/dot.md:17` edit as part of the diff for the integrator to apply, or the integrator should remove it as part of the cycle-004 integration.

```yaml
---
slug: concepts-page-word-count-discipline
opened_at: cycle-004
opened_by: layer-intro-author
status: open
---
```

Cycle-004 concept-page rewrite of `concepts/dot.md` came in at ~310 words of prose vs the 200-word target in layer-intro-author's discipline (the target is set for layer intros). Concept pages carry their own structure inline (no dep-map to anchor them) and may legitimately need more. Meta-phase to decide whether the 200-word target applies uniformly or whether concept pages get a separate (higher) target.

```yaml
---
slug: concepts-sweep-cycle-005-candidate
opened_at: cycle-004
opened_by: layer-intro-author
status: open
---
```

The cycle-003 cross-cutter flagged that other concept pages (`concepts/axpy.md`, `concepts/nrm2.md`, `concepts/orthogonalization.md`, …) may share the same pre-layered-era contamination pattern as `concepts/dot.md` (hallucinated symbols, stale citations, wrong return-type framings). After cycle-004 lands the `concepts/dot.md` rewrite as the pattern template, cycle-005 should schedule a sweep dispatch (`same-layer-cross-cutter` over `book/src/concepts/`) to surface analogous defects.

```yaml
---
slug: slice-pages-l2-l3-accuracy-audit
opened_at: cycle-004
opened_by: layer-intro-author
status: open
---
```

The rewritten `concepts/dot.md` preserves links to `../spec/slices/cg.md` and `../spec/slices/gmres.md`. These are pre-layered-era slice documents. Whether the linked slice files themselves accurately describe `dot` usage at L2/L3 was not verified in cycle-004. Routes to a future `same-layer-cross-cutter` on those slice pages.

```yaml
---
slug: layer-intro-refresh-thresholds-l2-l3-l4
opened_at: cycle-004
opened_by: layer-intro-author
status: open
---
```

Pilot-1 set ">=3 firm operators" as the L1 layer-intro refresh threshold. Cycle-004 met it (now 7 firm L1 operators). Question: should the same threshold apply uniformly to L2/L3/L4? Layer-intro-author's recommendation: same threshold for L2 (>=3 firm); for L3/L4 leave the bar at "first firm operator lands" because those layers are not yet populated and the intro establishes structure for subsequent work. Meta-phase to confirm.

```yaml
---
slug: vocabulary-cohort-subsection-as-layer-intro-pattern
opened_at: cycle-004
opened_by: layer-intro-author
status: open
---
```

Cycle-004's L1 intro refresh introduced a "Vocabulary cohort" subsection (Firm / Rough-in / Queued split) that made coverage trajectory visible without restating operator content. Candidate for promotion to a standard sub-section across L_n intros once each layer has firm operators. Routes to meta-phase as a skill or template proposal.

```yaml
---
slug: subsumption-chain-cross-cutting-concept
opened_at: cycle-004
opened_by: layer-intro-author
status: open
---
```

The working note about subsumption-as-identity (`axpy ≺ axpby ≺ axpbypcz`) is currently L1-specific prose. As more layers accumulate subsumption chains (e.g., L2 `krylov-step` variants, L4 monadic-effect chains), this might warrant promotion to a `concepts/subsumption-chain.md` cross-cutting page. Out of scope for cycle-004; flagged for cross-cutter or meta-phase to triage.

```yaml
---
slug: scal-bit-determinism-fusion
opened_at: cycle-004
opened_by: harvester
status: open
---
```

`scal` law 4 (`scal(α, scal(β, x)) = scal(α·β, x)`) is algebraically exact but may differ at the bit level in IEEE-754 (two-pass form rounds twice; fused form rounds once). Recorded as a non-load-bearing transparent trick for Palace's current algorithms; future solvers (e.g. deterministic-reduction CG variants) may upgrade this to load-bearing.

```yaml
---
slug: normalize-as-fused-l1-primitive
opened_at: cycle-004
opened_by: harvester
status: open
---
```

`linalg::Normalize` (`vector.hpp:262-270`) fuses `nrm2` and `scal` and returns the norm alongside the rescaled vector. At L1 currently factors as `(α, x_new) = (1/nrm2(x), scal(1/nrm2(x), x))` — two L1 operators with a shared scalar. Whether to harvest a fused `normalize :: Tensor[N] → (Scalar, Tensor[N])` L1 primitive is open; not necessary for `scal`-as-leaf but would simplify Krylov-solver lowering themes.

```yaml
---
slug: apply-linop-lowering-theme-scope
opened_at: cycle-004
opened_by: harvester
status: open
---
```

The cycle-005 abstractor sketch of `apply-linop-mutation-rotation` will be substantially larger than `axpby-mutation-rotation` because: (i) representation-axis variants (sparse vs matrix-free reduction-order caveats), (ii) transpose-mode representation-aware specialisations, (iii) accumulating-form fusion, (iv) parallel-wrapper prolongation/restriction (out of scope per CLAUDE.md but worth a one-line note). Routes to abstractor.

```yaml
---
slug: addmult-decomposition-bit-equivalence
opened_at: cycle-004
opened_by: harvester
status: open
---
```

`apply_linop` claims `AddMult(A, x, a, y) = axpby(a, apply_linop(A, x), 1, y)`. Mathematically true; bit-equivalent at L0 only for assembled matrix `Mult` followed by `Add`. Matrix-free operators that fuse element-contribution accumulation directly into `y` may produce different floating-point sum order. The L1>L0 lowering theme for `apply_linop` should record this load-bearing caveat in detail.

```yaml
---
slug: addmult-as-more-primitive-form-in-some-subclasses
opened_at: cycle-004
opened_by: harvester
status: open
---
```

In `SumOperator::Mult` (`operator.cpp:439-440`), `Mult` is implemented in terms of `AddMult` rather than the other way around. The L1 entry treats `apply_linop` as primitive and `AddMult` as a composition; this inverts the L0 dispatch for some subclasses. The L1>L0 lowering theme should record both directions.

```yaml
---
slug: assemblediagonal-is-not-apply-linop-variant
opened_at: cycle-004
opened_by: harvester
status: open
---
```

`Operator::AssembleDiagonal` (`operator.hpp:51`) extracts the diagonal of `A` as a vector. Not an `apply_linop` variant — it's a separate operator-shaped construct belonging in a future L1 entry (diagonal extraction or "operator-to-data" primitive). Recorded so it isn't accidentally folded into `apply_linop`'s variant axes.

```yaml
---
slug: floquet-correction-operator-construction-variants
opened_at: cycle-004
opened_by: harvester
status: open
---
```

`palace/linalg/floquetcorrection.{hpp,cpp}` introduces complex-shifted operators for Floquet-periodic eigenmode problems; not surveyed for the `apply_linop` entry. If they expose additional operator-construction variants (beyond sum / product / diagonal / multigrid), the L1>L0 lowering theme would need to absorb them.

```yaml
---
slug: axpbypcz-mutation-rotation-abstractor-target
opened_at: cycle-004
opened_by: harvester
status: open
---
```

Companion L1>L0 theme `axpbypcz-mutation-rotation` (analogous to existing `axpby-mutation-rotation`) is the next abstractor target — must address: (a) the `γ == 0` algebraic-sub-rule (first place in the L1>L0 lowering corpus where a Palace specialisation requires algebraic constant-folding to recognise); (b) the two distinct L0 evaluation orders in the real-real specialisation (one-call vs two-call); (c) the in-place destination rebinding (same as `axpby`). The L1 algebra is firm independent of this — the lowering can proceed in a future cycle.

```yaml
---
slug: axpbypcz-member-method-body-survey
opened_at: cycle-004
opened_by: harvester
status: open
---
```

The complex-complex and real-scalar-on-complex-vector specialisations at `vector.cpp:760-772` both delegate to `z.AXPBYPCZ(α, x, β, y, γ)` (the member form), but the member-method body itself was not read in the cycle-004 invocation. Whether the member form has its own `γ == 0` constant-folding branch or uses a unified kernel is unresolved. Minor follow-up — the L1 algebra is unchanged either way (both branches compute the same value).

```yaml
---
slug: fused-update-chained-collapse-combinator-mining
opened_at: cycle-004
opened_by: harvester
status: open
---
```

The `axpbypcz` Law 12 chained-collapse pattern (`(α₁ + γ₁·α₂, β₁ + γ₁·β₂, γ₁·γ₂)`) generalises the axpby chained-collapse. The pattern (`outer_scalar + outer_self_scalar · inner_scalar` for non-self slots; `outer_self_scalar · inner_self_scalar` for the self-slot) is a candidate combinator-mining target for a "fused-update chained-collapse" L1 → L2 pattern.

```yaml
---
slug: minres-mfem-as-l0-substrate-policy
opened_at: cycle-004
opened_by: abstractor
status: open
---
```

CLAUDE.md's "Scope" section says mesh / FE-space construction (MFEM-equivalent FE assembly) is in scope. It is ambiguous whether this extends to MFEM's Krylov solvers (`mfem::MINRESSolver`, `mfem::BiCGSTAB`, …) as L0 substrate. If yes, the cycle-004 obstruction themes for MINRES/BiCGStab are recoverable — the L1>L0 rewrite would target MFEM source rather than Palace source. If no, the obstruction stands. Routes to meta-phase. **Bundled with `bicgstab-mfem-reanchor-policy`** (same question, two themes).

```yaml
---
slug: bicgstab-mfem-reanchor-policy
opened_at: cycle-004
opened_by: abstractor
status: open
---
```

MFEM ships `mfem::BiCGSTAB`; Palace links MFEM unconditionally but never names it in this context. Methodology question (CLAUDE.md says cite Palace, not vendored upstream): should the obstruction be re-anchored against MFEM headers? Co-pending with `minres-mfem-as-l0-substrate-policy` — same underlying question.

```yaml
---
slug: bicgstab-enum-intent
opened_at: cycle-004
opened_by: abstractor
status: open
---
```

Why does Palace ship a `BiCGSTAB` enum value with only an aborting branch? Stub for planned implementation, or deliberate guard against silent fallback? Worth a one-line answer in `scaffolding/decisions/` or a Palace-upstream issue.

```yaml
---
slug: advertised-but-unimplemented-krylov-solvers-friction
opened_at: cycle-004
opened_by: abstractor
status: open
---
```

Friction-ledger candidate: cycle-004 MINRES + BiCGStab both produce obstruction-themes for advertised-but-unimplemented Krylov solvers. Pattern: `advertised-but-unimplemented-krylov-solvers`. Watch for a third instance (`KrylovSolver::DEFAULT` is the third grouped abort case; the `palace/utils/labels.hpp` enum may have more entries that abort). Routes to meta-phase.

```yaml
---
slug: cycle-planner-grep-before-harvester
opened_at: cycle-004
opened_by: abstractor
status: open
---
```

Cycle-003 integrator-signals listed MINRES as a candidate for **harvester** dispatch; cycle-004 planner dispatched **abstractor** instead. The harvester role would have required a Palace L0 site to extract from; on inspection no such site exists. Useful heuristic for cycle-planner: **before queuing a harvester pass for an algorithm, grep for its presence**; queue abstractor with obstruction-anticipation when grep returns ≤ 3 hits all in enum/labels/config.

```yaml
---
slug: shared-infra-priorities-rescope-after-obstruction
opened_at: cycle-004
opened_by: abstractor
status: open
---
```

The cycle-003 priorities list put MINRES at #10 of shared-infra items, BiCGStab nearby. The implicit assumption was that Palace implements them; with that assumption disconfirmed, those items need re-scoping. Candidates: (a) drop them from shared-infra entirely — they're not Palace infrastructure; (b) reinterpret as "the Krylov layer Palace *would* need" — a forward-looking gap, useful when downstream burn-port work needs symmetric-indefinite / non-symmetric solves. Routes to meta-phase.

```yaml
---
slug: lanczos-as-arnoldi-variant-axis
opened_at: cycle-004
opened_by: abstractor
status: open
---
```

Proposed `lanczos_step` is a clean variant-axis of the planned `arnoldi_step` (symmetry collapses `j`-term recurrence to 2-term). If `arnoldi_step` is harvested first against an affirmative L0 site (GMRES Arnoldi inner body, `iterative.cpp:614-642`), `lanczos_step` may collapse from a separate rough-in into a `variant_of(arnoldi_step, symmetry=true)` row. Worth a same-layer-cross-cutter pass once both are on the dep-map.

```yaml
---
slug: minres-bicgstab-signature-sketches-not-contracts
opened_at: cycle-004
opened_by: abstractor
status: open
---
```

The three speculative MINRES operator signatures and three BiCGStab signatures are written tensor-typed and stateless; in practice MINRES requires the running QR state to thread through `givens_apply_with_residual_min`, and BiCGStab threads a 7-tuple state. Harvester should expect to rework the signature shape when an anchor materialises; the cycle-004 signatures are scaffolding, not contracts.

```yaml
---
slug: subagent-skips-edit-on-explicit-instruction
opened_at: cycle-004
opened_by: integrator
status: open
---
```

Pattern observed in cycle-004: the abstractor subagent (BiCGStab) returned report content as text rather than calling Edit, claiming "harness rule precedence" despite the parent-pre-creates-skeleton workflow being the documented operational pattern. Same pattern as cycle-002 cycle-planner haiku-skip-write behavior, now appearing in an opus tier. Routes to meta-phase for friction-ledger and methodology adjustment.

```yaml
---
slug: krylov-step-speculative-l1-promotion-decision
opened_at: cycle-005
opened_by: harvester
status: answered
answered_at: cycle-005
answered_in: scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md
---
```

The five speculative L1 operators from cycle-004 obstruction themes (`lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min`, `bicgstab_step`, `omega_update`, `stabilisation_update`) — should any be promoted to firm L1 in service of the cycle-005 `krylov-step` L2 harvest? Decision is documented: NO promotion; each is a step-body specialisation of `krylov-step`, not an orthogonal axis that would simplify its semantics. Re-evaluation triggers are catalogued in the decision artifact.

```yaml
---
slug: orthogonalize-as-future-L2-firstclass-entry
opened_at: cycle-005
opened_by: harvester
status: open
---
```

`krylov-step` references `orthogonalize` (via `op.orthog` closure) as a level-(b)-absorbed L2 composition surface, but no firm L2 chapter exists for it. The `orthogonalize` slice (`book/src/spec/slices/orthog.md`) and concept page (`book/src/concepts/orthogonalization.md`) exist; lifting the L2-composition story into a firm L2 entry is a future harvester candidate. Out of scope for cycle-005.

```yaml
---
slug: incremental-least-squares-as-future-L2-firstclass-entry
opened_at: cycle-005
opened_by: harvester
status: open
---
```

GMRES's outer driver consumes the running-QR / Givens-stream composition as a small-dense kernel; it currently lives as a concept page (`book/src/concepts/incremental-least-squares.md`) only. A firm L2 entry for `incremental-least-squares` is a future harvester candidate (sibling to the `orthogonalize` candidate). Out of scope for cycle-005.

```yaml
---
slug: L2-layer-intro-refresh-for-named-compositions
opened_at: cycle-005
opened_by: harvester
status: open
---
```

The L2 layer-intro (`book/src/L2/index.md`) gained its first firm operator chapter (`krylov-step`) in cycle-005, but the Context and Semantics-overlay sections were originally authored for a layer with only primitive operators, not named compositions. A future `layer-intro-author` invocation should refresh the L2 intro to articulate the role of named compositions and to surface the demand-pruning law as a layer-wide algebraic feature.

```yaml
---
slug: L2-named-compositions-have-no-single-L0-citation
opened_at: cycle-005
opened_by: harvester
status: open
---
```

`krylov-step` is a methodology-level concept — no single Palace-source citation, only five Palace-spec-corpus citations (Phase-1 slices). Per the combinator-miner cycle-002 open question, this is a feature, not a bug, of the L2 layer: L2 names compositions that emerged from cross-slice pattern-matching, not from source-line identification. Flagged because future critics may surface this as a citation-validity concern; the explicit no-L0-source status is the L2-named-composition norm.

```yaml
---
slug: krylov-step-naming-stretches-to-chebyshev
opened_at: cycle-005
opened_by: harvester
status: open
---
```

The cycle-002 rough-in flagged "krylov-step" as stretching to cover Chebyshev (which is not strictly Krylov-subspace per Saad 2003). The firm chapter preserves the name on grounds of consistency with the cycle-002 rough-in and the fact that variant-axis absorption makes the naming a *role* description rather than a *family* description. Alternative names (`iterative-step-kernel`, `fold-step`, `solver-step`) were considered and rejected as less precise. Re-naming is left for a future cross-cutter invocation if friction surfaces.

```yaml
---
slug: gmres-givens-stream-as-step-kernel-borderline
opened_at: cycle-005
opened_by: harvester
status: open
---
```

The cycle-002 rough-in flagged `polynomial_recurrence_step.md:147-155` (the GMRES-Givens-stream site) as a borderline `krylov-step` instance. Strict reading excludes (primitive sequence is `givens_apply`/`givens_generate`, not `apply_linop`+`axpy`+`dot`); broad reading includes (the fold-kernel-plus-outer-driver shape matches). The firm `krylov-step` chapter records the Givens-stream case under the polynomial-recurrence-step citation but does *not* claim it as a `krylov-step` instance — it is a sibling pattern at the small-dense / `incremental-least-squares` scope. May be revisited if `incremental-least-squares` is firmed at L2.

```yaml
---
slug: apply-linop-workspace-tensor-reading-at-L0
opened_at: cycle-005
opened_by: abstractor
status: open
---
```

Concrete operator subclasses often own a `mutable` workspace member `z` (e.g. `SumOperator::z`, `palace/linalg/operator.hpp:120`; `BaseProductOperator::z`, `palace/linalg/operator.hpp:192`). The L1 form has no notion of workspace; the L1>L0 lowering treats it as a private detail of the operator subclass. However, the workspace IS observable at L1 in one specific case: operator-composition (`A · B`) materialises the intermediate vector `B·x` and applies `A` to it. That intermediate is L1-visible (as the second argument to the outer `apply_linop` call) but its concrete storage (the `mutable z` member of `BaseProductOperator`) is L0-only. A future `lowering-verifier` audit should confirm the workspace-mention-and-erase pattern matches the L1 operator-composition law (law 4 of `apply_linop`).

```yaml
---
slug: apply-linop-sum-operator-mult-via-addmult-reuse
opened_at: cycle-005
opened_by: abstractor
status: open
---
```

`SumOperator::Mult` (lines 439-440) uses `Mult-via-AddMult` reuse for the multi-operator path: `y = 0.0; AddMult(x, y)`. At L1 the L0 expansion is `axpby(1, apply_linop(A, x), 0, 0)`, which reduces directly to `apply_linop(A, x)` by `axpby` law 3 (β=0 zeroes the y_old contribution; α=1 passes the input through). The L1 view is identical to sub-pattern A — worth recording as a note in the `apply-linop-mutation-rotation` theme but not a separate sub-pattern. The L0 reuse pattern is a transparent performance trick (avoids duplicating the accumulation loop).

```yaml
---
slug: apply-linop-preconditioner-application-coverage
opened_at: cycle-005
opened_by: abstractor
status: open
---
```

Palace's preconditioners (`amg`, `ams`, `jacobi`, `chebyshev`, `distrelaxation`, `blockprecond`, `gmg`, `hcurl`) are all concrete `Solver` / `mfem::Solver` subclasses that implement `Mult(x, y)` semantically as `y = M⁻¹ · x` (the action of the preconditioner). At L0 they form a parallel class hierarchy (`palace/linalg/solver.hpp`); at L1 their `apply_linop` view collapses with the operator-action view (a preconditioner IS a linear operator, just with a special construction). The `apply-linop-mutation-rotation` theme does not cite the preconditioner hierarchy explicitly — those are covered as further realisations of sub-pattern A. A follow-up theme `solver-as-operator-application` may be warranted if the `Solver`-vs-`Operator` distinction proves load-bearing at L0; the `concepts/solver-as-operator.md` page is the existing narrative for this distinction.

```yaml
---
slug: apply-linop-complex-wrapper-operator-lifting
opened_at: cycle-005
opened_by: abstractor
status: open
---
```

`ComplexWrapperOperator` (`operator.hpp:73-113`) — a `ComplexOperator` whose internal representation wraps two real `Operator`s and dispatches the four-block real-imaginary multiplication. At L1 this is `complex-from-real-lift` (existing concept); the operator-side view is just `apply_linop` on a complex operator. Not a separate sub-pattern; recognition collapses with sub-pattern A on the `ComplexOperator` hierarchy. Worth a `lowering-verifier` cross-check to confirm the four-block structure is correctly captured by the existing `complex-from-real-lift` concept narrative.

```yaml
---
slug: apply-linop-complex-operator-default-impls-of-hermitian-transpose
opened_at: cycle-005
opened_by: abstractor
status: open
---
```

The base-class `MultHermitianTranspose` and `MultTranspose` on `ComplexOperator` are virtual (not pure-virtual), so default implementations exist somewhere in `palace/linalg/operator.cpp`. The specific file:lines and the actual default behaviour (call-through-with-conjugation vs. abort vs. something else) were **not read this cycle**; the abstractor declines to speculate on the body. Routed to a `lowering-verifier` audit to locate and characterise the defaults. Not load-bearing for `apply-linop-mutation-rotation` sub-pattern recognition.

```yaml
---
slug: mfem-add-alias-safety
opened_at: cycle-005
opened_by: abstractor
status: open
---
```

`axpbypcz-mutation-rotation` Applicability condition #1 states that the L0 `add(α, x, β, y, z)` kernel is alias-safe when `z` matches one of the inputs (e.g., `timeoperator.cpp:139` writes `rhs1` while reading `rhs1`). This claim is unverified against the MFEM source — the L0 corpus shows the call site relies on the behaviour but no MFEM-side proof has been captured. A future `lowering-verifier` or `cross-layer-cross-cutter` invocation should audit MFEM `Vector::Add` semantics under aliasing and either confirm the claim or escalate as a load-bearing semantic dependency on upstream behaviour. (CLAUDE.md note: "Many symbols resolve into upstream libraries (MFEM, libCEED). Specialized agents cite Palace source, not vendored upstream. If a question requires upstream behaviour, log as open question." — this is exactly that case.)

```yaml
---
slug: mixed-justification-sub-rule-methodology
opened_at: cycle-005
opened_by: abstractor
status: open
---
```

The γ==0 sub-rule in `axpbypcz-mutation-rotation` is labelled "algebraic *and* structural" because the structural-rebind is preserved while the algebraic-collapse (γ=0 → 3→2 vectors) is what triggers the L0 kernel-shape change. The precedent theme `axpby-mutation-rotation` has pure-structural sub-pattern A and pure-algebraic sub-patterns B and C; this mixed framing has no precedent. A `cross-layer-cross-cutter` review should confirm whether the methodology already has a name for this combination — possibly `structural-with-algebraic-trigger` or `algebraic-folding-with-rebind` — and either ratify the framing or propose a primitive concept to capture it (latter would land in `book/src/concepts/`). This is the first mixed-justification sub-rule in the project.

```yaml
---
slug: axpbypcz-gamma-asymmetric-branching-rationale
opened_at: cycle-005
opened_by: abstractor
status: open
---
```

Palace's L0 code branches on `gamma == 0.0` but not on `alpha == 0.0` or `beta == 0.0`, despite the three positions being algebraically symmetric (laws #3, #4, #5 of `axpbypcz.md`). The implementation choice is presumably driven by the empirical observation that γ=0 is the common case (γ is the *prior* z's coefficient, and most call sites are "compute z from x and y, discarding prior z" — i.e., γ=0 — visible in the call-site corpus: 7 of 11 sub-pattern-C and sub-pattern-A surveyed sites pass `0.0` for γ). But this is an inferred rationale; the Palace source carries no comment. A `combinator-miner` or `same-layer-cross-cutter` invocation could confirm whether the asymmetry is by-design (γ=0 is a documented common case) or incidental (an artefact of the implementation history).

```yaml
---
slug: axpbypcz-sub-pattern-B-defined-not-used-corpus-audit
opened_at: cycle-005
opened_by: abstractor
status: open
---
```

Sub-pattern B of `axpbypcz-mutation-rotation` (complex-scalar-on-complex-vector free-function specialisation, `vector.cpp:760-765`) is compiled but not called from the surveyed call-site corpus. Same pattern as the `axpby-mutation-rotation` coverage note (the defined-not-used trampoline form). Treat as a recognition rule for potential call sites; a `lowering-verifier` exhaustive audit should confirm whether sub-pattern B has any caller across the full Palace tree.

```yaml
---
slug: scalar-promotion-mutation-rotation-cross-family-theme
opened_at: cycle-005
opened_by: abstractor
status: open
---
```

The complex member-form `ComplexVector::AXPBYPCZ` body has inner branches on `ai == 0 && bi == 0` (real-α, real-β fast-path) and on `gi == 0` (real-γ fast-path inside the γ≠0 outer branch). These are transparent performance specialisations covered by the L1 `axpbypcz` "scalar promotion" variant sub-axis; they are not separate L1>L0 sub-patterns at the theme level. If a future cycle decides to surface scalar-promotion recognition as a first-class L1>L0 concern (e.g., a separate theme for the implicit-scalar-promotion pattern across the entire BLAS-1 family — `axpy`, `axpby`, `axpbypcz`, `scal`), the inner branches in `vector.cpp:388-455` should be a cited evidence point.

```yaml
---
slug: axpbypcz-gamma-recognition-is-syntactic-not-semantic
opened_at: cycle-005
opened_by: abstractor
status: open
---
```

A runtime γ value that happens to equal zero at runtime lowers to the γ≠0 path at L0 (because the L0 branch is `gamma == 0.0` on the value, not on the type/literal). This means an L2/L3 optimisation that proves γ=0 at a higher layer would need to materialise the literal `0.0` at the L1>L0 boundary to trigger the fast-path — it cannot rely on the L0 runtime branch alone. This is consistent with the precedent `axpby-mutation-rotation` α==1 sub-pattern (also syntactic recognition); flagged here for cross-reference. Not an issue for the present theme — a downstream-lowering observation.

## Investigating

(empty)

## Answered

```yaml
---
slug: axpby-axpbypcz-next-harvest
opened_at: pilot-1
opened_by: harvester
status: answered
answered_at: cycle-004
answered_in: book/src/L1/axpbypcz.md
---
```

Cycle-003 closed the `axpby` half (firm at L1). Cycle-004 harvester closes the `axpbypcz` half: firm L1 operator landed with 12 algebraic laws, subsumption chain `axpy ≺ axpby ≺ axpbypcz` recorded as algebraic-law statement. The fused-primitive decision mirrors `scaffolding/decisions/axpby-as-primitive.md` § "Knock-on effects" (no new decision file authored — the existing forward-statement covers the choice).

```yaml
---
slug: axpbypcz-l1-harvest
opened_at: cycle-003
opened_by: harvester
status: answered
answered_at: cycle-004
answered_in: book/src/L1/axpbypcz.md
---
```

Cycle-004 harvester landed `axpbypcz` firm at L1. Mirrors `axpby` decision; 12 algebraic laws including the novel Law 12 chained-collapse on shared `(x, y)`; two variant axes (element-type, scalar-promotion) plus one internal L0 control-flow axis (γ==0 fast-path) explicitly classified as not-an-L1-variant.

```yaml
---
slug: scal-primitive-l1-harvest
opened_at: cycle-003
opened_by: harvester
status: answered
answered_at: cycle-004
answered_in: book/src/L1/scal.md
---
```

Cycle-004 harvester landed `scal` firm at L1. Nine algebraic laws (module-over-scalar-field axioms plus field-commutativity); single variant axis (element-type, with scalar-promotion sub-axis). Sibling subsumption with `axpby` (β=0). The "no `linalg::Scal`/`Scale` free function" claim verified by grep.

```yaml
---
slug: l1-index-refresh
opened_at: pilot-1
opened_by: integrator
status: answered
answered_at: cycle-004
answered_in: book/src/L1/index.md
---
```

Cycle-004 layer-intro-author refresh landed: new Context bullets grounded in the 4 cycle-002/003 firm operators; expanded Semantics overlay with three motifs; new "Vocabulary cohort" subsection (Firm / Rough-in / Queued split); Working Notes operationalised. Dep-map preserved verbatim then extended per cycle-004 harvester landings (now 7 firm + 6 rough-in obstruction rows).

```yaml
---
slug: l1-index-refresh-trigger-met
opened_at: cycle-003
opened_by: harvester
status: answered
answered_at: cycle-004
answered_in: book/src/L1/index.md
---
```

Trigger met (4 firm at cycle-003, then 7 firm at cycle-004); refresh landed cycle-004.

```yaml
---
slug: concepts-dot-return-type-correction
opened_at: cycle-002
opened_by: harvester
status: answered
answered_at: cycle-004
answered_in: book/src/concepts/dot.md
---
```

Cycle-004 layer-intro-author rewrote `concepts/dot.md`. The return type is now correctly stated in the element-type rule table: real → real, complex (Hermitian or unconjugated) → complex. The "real-projected" rationalisation is removed.

```yaml
---
slug: concepts-dot-dotc-and-inverted-conjugation
opened_at: cycle-002
opened_by: harvester
status: answered
answered_at: cycle-004
answered_in: book/src/concepts/dot.md
---
```

Cycle-004 layer-intro-author rewrote `concepts/dot.md`. All references to the non-existent `linalg::Dotc` are removed. The Hermitian/unconjugated polarity is correctly assigned: `ComplexVector::Dot` is Hermitian (`yᴴ x`), `ComplexVector::TransposeDot` is the unconjugated bilinear form (`yᵀ x`), method-form only.

```yaml
---
slug: dot-backpointer-staleness-after-rewrite
opened_at: cycle-003
opened_by: same-layer-cross-cutter
status: answered
answered_at: cycle-004
answered_in: book/src/L1/dot.md
---
```

Cycle-004 layer-intro-author proposed and integrator applied the softening edit on `L1/dot.md:17`. The "concept page predates this entry and contains an inaccuracy" warning is replaced with a clean back-pointer to the corrected concept page; L1 entry remains authoritative.

```yaml
---
slug: dot-blas-heritage-framing-salvage
opened_at: cycle-003
opened_by: same-layer-cross-cutter
status: answered
answered_at: cycle-004
answered_in: book/src/concepts/dot.md
---
```

Cycle-004 rewrite preserved the BLAS-1 heritage framing (background section ties to `ddot`/`zdotc`/`zdotu`) while correcting the factual specifics. The salvageable framing is intact.

```yaml
---
slug: krylov-step-dual-placement-l2-l4-routing
opened_at: cycle-005
opened_by: cross-layer-cross-cutter
status: open
---
```

Cross-layer-cross-cutter (cycle-005) recommends `krylov-step` belongs at **both L2 and L4** with a lowering edge, not L2-only as currently rough-in'd. L2 names the primitive-composition shape; L4 names the typed wrapper (`state-stratification` / `solve-monad` / `first-iteration-unrolling` idiom) that consumes the kernel role already referenced in concept prose. Follow-up routing (cycle-006 candidate dispatches): **primary** = `harvester` on `krylov-step @ L4` (typed signature in state-stratification idiom, dependencies on L4 concepts, "Lowers to" stub → L2); **secondary** = `abstractor` on L4>L3 lowering theme (typed-wrapper-with-state-monad → value-threaded form — the substantive rotation, with L3>L2 plausibly identity-in-form per combinator-miner); **tertiary** (deferrable, may fold into primary) = `layer-intro-author` on L4 dep-map. Source: `reports/2026-05-27T025354Z-cross-layer-cross-cutter-krylov-step-placement/CYCLE.md` §Recommendation.

```yaml
---
slug: krylov-step-naming-reuse-vs-disambiguation
opened_at: cycle-005
opened_by: cross-layer-cross-cutter
status: open
---
```

If `krylov-step` lands at both L2 and L4 per the dual-placement recommendation, the slug reuse may invite confusion. Cross-cutter's tentative preference is **same-slug-different-layer** (so the lowering edge names itself as `L4>L3 krylov-step` theme; cross-layer reuse is the norm elsewhere in the spec). Alternative: `krylov-step-kernel` (L2) + `krylov-step` (L4), or vice versa. Defer to the L4 harvester — rename only if friction emerges in authoring. Source: `reports/2026-05-27T025354Z-cross-layer-cross-cutter-krylov-step-placement/CYCLE.md` §Open-questions item 1.

```yaml
---
slug: krylov-step-l3-identity-in-form-audit
opened_at: cycle-005
opened_by: cross-layer-cross-cutter
status: open
---
```

The combinator-miner (cycle-002) asserted that the L2→L3 rotation on the `krylov-step` body is identity-in-form, citing `cg.md:352-362` and `arnoldi_step.md:185-188`. This assertion has not been independently audited. If true, the L4>L2 lowering can be a single theme without an explicit L3 entry. If false (e.g., the `Krylov` ephemeral bundle dissolves on the way to L3), an L3 `krylov-step` row would also be warranted. Defer to the L4>L3 abstractor dispatch (cycle-006 secondary follow-up); if non-identity rotations on the body are found, promote to an L3 entry. Source: `reports/2026-05-27T025354Z-cross-layer-cross-cutter-krylov-step-placement/CYCLE.md` §Open-questions item 2.

```yaml
---
slug: state-stratification-as-l4-concept-or-l4-row
opened_at: cycle-005
opened_by: cross-layer-cross-cutter
status: open
---
```

`state-stratification` currently lives only as a concept under `book/src/concepts/state-stratification.md`. If `krylov-step @ L4` becomes the first L4 dep-map entry, the L4 layer-intro-author may also need to promote `state-stratification`, `iterate_while`, and `solve-monad` as L4 rows simultaneously so that `krylov-step @ L4` has firm L4 vocabulary to depend on. Question: should these be batched into the same L4 harvester dispatch (cycle-006 primary), or pre-staged via a `layer-intro-author` dispatch on L4 first? Coordination concern flagged to the L4 harvester / cycle-planner. Source: `reports/2026-05-27T025354Z-cross-layer-cross-cutter-krylov-step-placement/CYCLE.md` §Open-questions item 3.

```yaml
---
slug: scalar-promotion-retroactive-l1-thinning
opened_at: cycle-005
opened_by: layer-intro-author
status: open
---
```

The `scalar-promotion` concept page (landed cycle-005) is purely additive: the four L1 entries (`axpy.md`, `axpby.md`, `axpbypcz.md`, `scal.md`) still carry per-operator scalar-promotion prose. Cycle-006+ retroactive-thinning priority #11 should slot a dispatch to: (a) replace the per-operator promotion-rule paragraphs in those four L1 entries with one-line backlinks `see [scalar-promotion](../concepts/scalar-promotion.md)`; (b) leave the citation evidence in place (each operator's Evidence § keeps its own promoted-overload citation); (c) update the four operators' Variant-axes § "scalar promotion (sub-axis)" bullets to short backlinks rather than full restatements. Note: corrected scope is **four** operators (not five as originally specified in the cycle-005 dispatch brief) — `dot` does not scalar-promote (it returns a scalar; no input α to promote). Estimated context savings ~600 words across the four entries. Source: `reports/2026-05-27T025354Z-layer-intro-author-scalar-promotion-concept/CYCLE.md` §Open-questions item 2.

```yaml
---
slug: scalar-promotion-l4-calculus-formalisation
opened_at: cycle-005
opened_by: layer-intro-author
status: open
---
```

The open question `scalar-promotion-typing-rule` (cycle-pre-005) calls for "lifting this into an L1 type-system rule rather than per-operator prose". The cycle-005 concept page `book/src/concepts/scalar-promotion.md` is the *informal* statement (English + Palace evidence). Formal calculus-level adoption — the L4 typing judgement of the form `Γ ⊢ α : real, Γ ⊢ x : Tensor[complex] ⇒ Γ ⊢ axpy(α, x, y) : Tensor[complex]` with `real ⊑ complex` as a sub-typing relation on scalars — is L4-calculus-design work, not L1-concept-page work. Closure of `scalar-promotion-typing-rule` requires both this concept page (now landing) AND the L4-calculus extension (future cycle, coordinate with L4 harvester / layer-intro-author dispatches). Source: `reports/2026-05-27T025354Z-layer-intro-author-scalar-promotion-concept/CYCLE.md` §Open-questions item 4.

## Dropped

(empty — will accumulate)

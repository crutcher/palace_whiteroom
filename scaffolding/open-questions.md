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

```yaml
---
slug: l0-reference-note-citations-grep-vs-read-discipline
opened_at: cycle-006
opened_by: layer-intro-author
status: open
---
```

The cycle-006 bundle-2 L0 reference notes (`apply-linop-overload-set.md`, `kspsolver-base-class.md`) cite a number of source ranges that were grep-verified at start-lines (function signatures exist) rather than read in full. Specifically `palace/linalg/rap.cpp:236-275` (ParOperator::MultTranspose) and `palace/linalg/operator.cpp:478-507` (BaseDiagonalOperator template specialisations, real + complex). For L0 reference-note discipline (2-4 paragraphs of interpretation + representative citations, no line-by-line transcription) this is sufficient — the cited ranges support only function-presence claims and one-line interpretive descriptions (e.g., "the transpose form swaps prolongation/restriction roles"). However, if a future cross-layer-cross-cutter or lowering-verifier audits these citations to extract algebraic detail or sub-pattern body-shapes, they would need to re-read the bodies in full. Routes to whichever future audit consumes these ranges. Source: `reports/2026-05-27T081050Z-layer-intro-author-L0-bootstrap-bundle-2/CYCLE.md` §Open questions item 2.

```yaml
---
slug: mfemwrappersolver-l0-coverage-candidate
opened_at: cycle-006
opened_by: layer-intro-author
status: open
---
```

`kspsolver-base-class.md` mentions `MfemWrapperSolver` (at `palace/linalg/solver.hpp:70-134`) in its "Notes for higher layers" section as "another `Solver<OperType>` subclass" but does not characterise it in depth. The full preconditioner-side construction surface is currently spread across `palace/linalg/{amg,ams,jacobi,mumps,strumpack,superlu,gmg}.{hpp,cpp}` and routed through `MfemWrapperSolver`. A future bundle-3 (or beyond) candidate L0 reference-note chapter would naturally anchor itself on `MfemWrapperSolver` and cover the preconditioner-class hierarchy in parallel to the way `apply-linop-overload-set.md` covers the `Operator` hierarchy. Routes to cycle-007+ planner as a future L0 bundle candidate. Source: `reports/2026-05-27T081050Z-layer-intro-author-L0-bootstrap-bundle-2/CYCLE.md` §Open questions item 3.

```yaml
---
slug: l1-ksp-solve-firm-up-anchor-ready
opened_at: cycle-006
opened_by: layer-intro-author
status: open
---
```

`kspsolver-base-class.md` references an unbuilt L1 `ksp_solve` operator in its prose and Referenced-from sections (qualified explicitly as "not yet authored — anticipated cycle-007+"). The L0 reference-note chapter is the natural L0 anchor for that future L1 entry; `concepts/ksp_solve.md` already exists as the methodology concept page. Combined, the cycle-007 (or later) planner has two reading-trail entry points (concept + L0 reference) ready to anchor a harvester dispatch that promotes `ksp_solve` from concept to firm L1 operator. Routes to cycle-007+ planner as a harvester-target priority candidate. Source: `reports/2026-05-27T081050Z-layer-intro-author-L0-bootstrap-bundle-2/CYCLE.md` §Open questions item 4.

```yaml
---
slug: mfem-wrapper-solver-l4-complex-from-real-lift-backref
opened_at: cycle-007
opened_by: layer-intro-author
status: open
---
```

`mfem-wrapper-solver.md` (cycle-007 bundle-3) references `complex-from-real-lift` as the L4 concept on the preconditioner side, but the L4 lift theme has not been authored. The reference is forward-looking. When the L4 form of `complex-from-real-lift` is firmed (or the existing `book/src/concepts/complex-from-real-lift.md` is promoted to L4), the back-reference should be added to the chapter's "Referenced from" section. Routes to whichever cycle promotes `complex-from-real-lift` to firm L4. Not blocking the bundle; the chapter's forward-pointer wording is defensive. Source: `reports/2026-05-27T160728Z-layer-intro-author-L0-bootstrap-bundle-3/CYCLE.md` §Open questions item 1.

```yaml
---
slug: iterative-file-helper-citation-granularity
opened_at: cycle-007
opened_by: layer-intro-author
status: open
---
```

`linalg-iterative-file.md` (cycle-007 bundle-3) cites `iterative.cpp:34-241` as "Sundry small-dense linear-algebra utilities" without enumerating each helper at the per-template-overload level. The chapter's "Free-function helpers" section names the five primary anonymous-namespace helpers (`CheckDot`, `ApplyB`, `InitialResidual`, `ApplyBA`, `OrthogonalizeIteration`) explicitly with line ranges, and identifies the small-dense kernel helpers (`SafeMin` / `SafeMax`, `GeneratePlaneRotation` real + complex, `ApplyPlaneRotation` real + complex). The cycle-007 `l1-ksp-solve` harvester may want a more granular per-overload helper enumeration (separating real and complex specialisations) if the small-dense kernel becomes load-bearing for the L1 form; routes to cycle-007+ harvester or a future thinning sweep. Source: `reports/2026-05-27T160728Z-layer-intro-author-L0-bootstrap-bundle-3/CYCLE.md` §Open questions item 2.

```yaml
---
slug: eigensolver-wrapper-l0-bundle-4-candidate
opened_at: cycle-007
opened_by: layer-intro-author
status: answered
answered_at: cycle-008
answered_in: reports/2026-05-27T173523Z-layer-intro-author-L0-bootstrap-bundle-4
---
```

`mutable-workspace-pattern.md`'s Category 3 (solver workspaces) lists the eigensolver-wrapper instances (`arpack.hpp:88, 215`; `slepc.hpp:83, 302`; `nleps.hpp:72, 265`) as grep-verified-only. The eigensolver wrappers themselves have not been read at L0; their workspace usage is documented purely on the basis of grep-located `mutable ComplexVector` members. A future L0 bundle (bundle 4 or beyond) could author a dedicated eigensolver-wrapper reference note that reads these wrappers in full; the workspace pattern reference is sufficient for the cross-cutting concern (the workspace-mention-and-erase rewrite is the same regardless of wrapper specifics) but not for a full eigensolver-side L0 audit. Routes to future L0 bundle. Source: `reports/2026-05-27T160728Z-layer-intro-author-L0-bootstrap-bundle-3/CYCLE.md` §Open questions item 3.

**Cycle-008 closure**: Bundle 4 (`reports/2026-05-27T173523Z-layer-intro-author-L0-bootstrap-bundle-4/`) authored the dedicated `eigensolver-wrapper.md` chapter under `book/src/L0/`. Pre-verification confirmed real surface (not stub-only): `eps.hpp` is a real abstract base; `arpack.cpp` (24 KB), `slepc.cpp` (67 KB), `nleps.cpp` (31 KB) are substantial implementations. The chapter covers all three concrete branches (RCI / shell-matrix / direct-Newton), the 22 virtuals on `EigenvalueSolver`, the `palace/models/modeeigensolver.cpp:1029-1047` dispatch site, and the workspace pattern Category-3 backlinks. Routes from `mutable-workspace-pattern` Category 3 (grep-verified-only eigensolver workspaces) are now backed by full source reading. A follow-up OQ `eigsolve-l1-operator-rough-in-candidate` (opened cycle-008) carries forward the L1 harvester routing.

```yaml
---
slug: mutable-workspace-category-4-split-decision
opened_at: cycle-007
opened_by: layer-intro-author
status: open
---
```

`mutable-workspace-pattern.md`'s Category 4 (`MfemWrapperSolver::A` retained-assembled-matrix) is a slight stretch of the "mutable workspace" name — the `A` member is `std::unique_ptr<mfem::HypreParMatrix>`, not `mutable`, and the lifecycle is tied to `SetOperator` invocations rather than per-`Mult` lazy-resize. The pattern is *related* (lazy allocation, reuse across calls, instance-scoped lifetime) but mechanically different. The chapter calls this out explicitly in its Category 4 prose. If a future cross-cutter (or a critic on this report) thinks Category 4 should be in a sibling chapter rather than this one, the split is clean: extract Category 4 into a new `retained-assembled-matrix-pattern.md` chapter and have `mutable-workspace-pattern.md` link to it. Bundle-3 keeps them together for the workspace-discipline-as-cohort framing; a future cycle could split. Routes to cross-cutter or layer-intro-author follow-up. Source: `reports/2026-05-27T160728Z-layer-intro-author-L0-bootstrap-bundle-3/CYCLE.md` §Open questions item 4.

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
status: answered
answered_at: cycle-006
answered_in: reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/ (audit-section confirms-with-refinement); see closure-note slug `krylov-step-l3-identity-in-form-audit-closure-cycle-006`
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

```yaml
---
slug: l4-row-vs-concept-dependency-convention
opened_at: cycle-006
opened_by: harvester
status: open
---
```

The cycle-006 L4 `krylov-step` row depends on five concept-page entries (`state-stratification`, `solve-monad`, `first-iteration-unrolling`, `derived-view-hoisting`, `convergence-test`) that have not been promoted to firm L4 rows. The L4 layer-intro-author and L4 dep-map currently expect L4 rows to depend on other L4 rows or on L1/L2 rows, not on concept pages — but the convention has never been formally adopted. The cycle-006 entry uses concept-page links and surfaces the question. If integration reveals that L4 rows must depend only on L4 rows (not concepts), a follow-up cycle-007 dispatch (likely `layer-intro-author` on the L4 vocab stack: promote `state-stratification`, `iterate_while`, `solve-monad`, `first-iteration-unrolling` to firm L4 entries with signatures and laws of their own) is needed before the `krylov-step` row can settle. Either resolution (concept-deps OK, or promote-the-vocab) is honoured by the cycle-006 entry's content with no rewrite needed (only the link targets change). Carry-forward of and broader-scope-than `state-stratification-as-l4-concept-or-l4-row` (cycle-005). Source: `reports/2026-05-27T080944Z-harvester-krylov-step-L4/CYCLE.md` §Open-questions item 1.

```yaml
---
slug: iterate-while-l4-anchor-missing
opened_at: cycle-006
opened_by: harvester
status: answered
answered_at: cycle-007
answered_in: reports/2026-05-27T160550Z-harvester-iterate-while-family-L4/ (closes the OQ in favour of the "L4 row" resolution: both `iterate_while` and `iterate_while_with_prev` land as firm L4 rows with their own variant-axis profile and demand-pruning law)
---
```

The cycle-006 L4 `krylov-step` row uses `iterate_while` (and `iterate_while_with_prev` for the first-iteration-unrolled Form B) as load-bearing vocabulary throughout the operator body and §Semantics, but no concept page or L4 row carries either name. The closest existing anchor is `book/src/concepts/solve-monad.md` §"Worked example — GMRES" which writes `inner_loop` as the fold body without naming the fold combinator. **Routes to cycle-007 planner**: either `iterate_while` should land as a concept page (sibling to `solve-monad`) or as an L4 row (the latter is more aggressive — would make `iterate_while` an L4 combinator with its own variant axes around predicate-shape, trajectory-recording, and the Form-A-vs-Form-B `_with_prev` variant). The cycle-006 wave-2 abstractor independently surfaced the same gap and proposed `iterate_while` / `iterate_while_with_prev` as rough-in L4 operators with intended signatures, doubly-flagging this at integration time. Source: `reports/2026-05-27T080944Z-harvester-krylov-step-L4/CYCLE.md` §Open-questions item 2.

**Cycle-007 resolution**: the cycle-007 harvester (`reports/2026-05-27T160550Z-harvester-iterate-while-family-L4/`) firmed both `iterate_while` and `iterate_while_with_prev` as L4 rows (`book/src/L4/iterate-while.md`, `book/src/L4/iterate-while-with-prev.md`), adopting the "L4 row" resolution. Both chapters carry full Signature / Semantics (small-step rules) / Algebraic laws / Variant axes / Status sections; the dep-map at `book/src/L4/index.md` lists three firm rows total (post-this-dispatch). The follow-up trajectory-accumulator-vs-readout-collapse gap is tracked separately by OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`.

```yaml
---
slug: krylov-step-l3-row-contingency
opened_at: cycle-006
opened_by: harvester
status: answered
answered_at: cycle-006
answered_in: reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/ (audit's confirms-with-refinement verdict means the L3-row contingency does not fire; L4 entry's defensive L4>L3>L2 wording stands as-is); see closure-note slug `krylov-step-l3-identity-in-form-audit-closure-cycle-006`
---
```

The cycle-006 L4 `krylov-step` row's "Lowers to" section adopts the combinator-miner cycle-002 assertion that the L3>L2 step-body lowering is identity-in-form, skipping an intermediate L3 `krylov-step` row. If the cycle-006 wave-2 abstractor (`reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md`) audits this assertion and finds non-identity rotation at L3 — for instance, the `Krylov` ephemeral bundle dissolves on the way to L3 in a way that affects the body, not just the surrounding loop — a cycle-007 dispatch will promote an L3 `krylov-step` row and the L4 entry's "Lowers to" section will need a one-line update (split the L4>L2 chain into L4>L3 + L3>L2 with the L3 row interposed). The L4 entry's "Lowers to" wording is **defensive**: it names the chain as L4>L3>L2 even though only the L4 and L2 rows are firm post-cycle-006, anticipating the abstractor's audit. Carry-forward of `krylov-step-l3-identity-in-form-audit` (cycle-005). Source: `reports/2026-05-27T080944Z-harvester-krylov-step-L4/CYCLE.md` §Open-questions item 3.

```yaml
---
slug: l4-layer-intro-refresh-unblocked-by-first-firm-row
opened_at: cycle-006
opened_by: harvester
status: answered
answered_at: cycle-008
answered_in: 2026-05-27T181548Z-layer-intro-author-L4-intro-refresh
---
```

`book/src/L4/index.md` is updated by cycle-006 to carry the first firm operator row (`krylov-step`), but the surrounding intro prose still reflects the empty Phase-B-skeleton state. The "Semantics (overlay)" section says "To be drafted as L4 operators are formalized" — now that one operator is formalized, a `layer-intro-author` follow-up dispatch (cycle-007 candidate) could begin to draft that overlay using the cycle-006 entry's typing discipline (three-stratum state, `Solve` monad effect localisation, `OpParams` `readonly`) as the first concrete anchor. **Routes to cycle-007 planner**: L4 layer-intro refresh is unblocked by the cycle-006 entry. Source: `reports/2026-05-27T080944Z-harvester-krylov-step-L4/CYCLE.md` §Open-questions item 5.

**Cycle-008 closure** (`reports/2026-05-27T181548Z-layer-intro-author-L4-intro-refresh/CYCLE.md`). The L4 intro Semantics-overlay placeholder was replaced with grounded prose describing four recurring semantic motifs across the three firm operators (`krylov-step`, `iterate-while`, `iterate-while-with-prev`): three-stratum state stratification, `Solve` monad with localised `SimState` effect, value-threaded loop combinators with demand-pruned trajectories, and variant absorption via `OpParams` `readonly` typing. A new **Vocabulary cohort** subsection was added between the overlay and the dep-map (following the cycle-004 L1 precedent at `book/src/L1/index.md:27-47`); its middle slot is re-purposed for L4>L3 cross-layer themes (the `krylov-step-typed-wrapper-dissolution` firm theme + the `gmres-inner-loop-iterate-while-migration` rough-in theme) rather than rough-in same-layer operators, because L4 currently has no rough-in operators — this template-shape adaptation is documented in the dispatch's caveat 2 and routed to cycle-009+ meta-phase for potential role-spec promotion under slug `vocabulary-cohort-middle-slot-cross-layer-adaptation` if precedent-setting is desired. The dep-map was extended with a new `Lowers to` column splitting cross-layer L4>L3 theme references out of the previously-overloaded `Dependencies` cell; the column split is L4-specific in this dispatch and could be back-applied to L1/L2/L3 dep-maps for consistency (routed under suggested slug `dep-map-lowers-to-column-back-application`). The cycle-007 planner did not pick this OQ up (cycle-007 wave-1 instead harvested `iterate-while` + `iterate-while-with-prev`); the refresh was deferred to cycle-008 wave-2 as a polish dispatch once the three-operator cohort was stable and the L4>L3 lowering theme had firmed.

```yaml
---
slug: concepts-index-kind-classification-full-audit
opened_at: cycle-006
opened_by: same-layer-cross-cutter
status: open
---
```

The cycle-006 `same-layer-cross-cutter` dispatch fixed two duplicate rows in `book/src/concepts/index.md` (one pure copy-paste at `complex-from-real-lift`, one divergent-kind misclassification at `solver-as-operator` where `layer-pattern` survived and `primitive` was deleted). The dispatch scope was bounded to those two duplicates per the cycle-006 planner's caveat 5. A full pass through the remaining 40 rows cross-referencing each row's `Kind` taxonomy assignment against the concept page's self-description (typically the opening sentence) would catch any other misclassified rows analogous to the `solver-as-operator` divergence. **Routes to cycle-007+ planner**: bounded-scope dispatch candidate (42 rows, each a short page). Suggested dispatch target: `same-layer-cross-cutter` or `layer-intro-author`. Not blocking any forward-frontier work. Source: `reports/2026-05-27T080948Z-same-layer-cross-cutter-concepts-index-duplicates/CYCLE.md` §Open-questions item 3.

```yaml
---
slug: same-layer-cross-cutter-cycle-md-write-failure
opened_at: cycle-006
opened_by: same-layer-cross-cutter
status: open
---
```

The cycle-006 `same-layer-cross-cutter` subagent did not write `CYCLE.md` to its report directory; the parent orchestrator wrote it post-hoc from the subagent's inline final-message text. The subagent cited a system-prompt restriction on writing files matching `report|summary|findings|analysis` patterns. The harvester and layer-intro-author dispatches in the same wave-1 wrote their `CYCLE.md` files successfully, so the restriction is either subagent-class-specific or the same-layer-cross-cutter misread its system prompt. The role spec at `.claude/agents/same-layer-cross-cutter.md:17` also references "Output: REPORT.md" — stale naming relative to the cycle-004 REPORT.md → CYCLE.md rename in CLAUDE.md. **Meta-phase target candidate** with three suggested actions: (a) update role spec to say "CYCLE.md" not "REPORT.md", (b) audit whether `claude-code` subagent file-write filters differ across the 8 specialized agents, (c) consider adding explicit "write to disk yourself" instruction in the role-spec template to prevent recurrence. No content-integrity loss in this instance (verbatim inline output preserved by parent), but unaddressed recurrence risks future content loss if a parent orchestrator is less attentive. Source: `reports/2026-05-27T080948Z-same-layer-cross-cutter-concepts-index-duplicates/CYCLE.md` §Open-questions item 5.

```yaml
---
slug: concepts-index-auxiliary-kind-usage-review
opened_at: cycle-006
opened_by: same-layer-cross-cutter
status: open
---
```

Low-priority adjacent observation from the cycle-006 `concepts-index-duplicates` dispatch (filed as item 2 of that report's Open Questions): the `auxiliary` Kind taxonomy bullet at `book/src/concepts/index.md:60` ("supporting concepts that don't fit the other categories") is used by exactly one row out of 42 (`convergence-test`, currently the only `auxiliary`-kinded concept). This is within taxonomy scope and not actionable now, but worth recording as an "is `auxiliary` still earning its place?" review item for a future concept-sweep cycle. If a future audit finds zero or one auxiliary entries persistently, candidate resolutions are: (a) reclassify `convergence-test` under a more specific kind and retire the `auxiliary` taxonomy bullet, (b) keep `auxiliary` as a documented escape hatch even when underused. Source: `reports/2026-05-27T080948Z-same-layer-cross-cutter-concepts-index-duplicates/CYCLE.md` §Open-questions item 2.

```yaml
---
slug: concepts-axpby-axpbypcz-pages-absent
opened_at: cycle-006
opened_by: layer-intro-author
status: open
---
```

Forward-thinning opportunity flagged by the cycle-006 `L1-scalar-promotion-thinning` dispatch (item 4 of that report's Open Questions). The L1 retroactive-thinning pass left `axpby.md` and `axpbypcz.md` somewhat verbose because no cross-cutting `concepts/axpby.md` and `concepts/axpbypcz.md` pages exist to host their BLAS-background / call-site-usage prose (whereas `concepts/axpy.md` and `concepts/scal.md` do exist and host the corresponding prose for those operators). The cycle-005 thinning pass for `axpy.md` and `scal.md` was effective in part because the concept pages already existed; the cycle-006 thinning pass for `axpby.md` and `axpbypcz.md` had only the `concepts/scalar-promotion.md` page to draw from (a typing-rule concept, not a per-operator concept), so the savings yield was bounded. **Candidate resolution**: a future `layer-intro-author` dispatch authors `concepts/axpby.md` and `concepts/axpbypcz.md` (mirroring the structure of `concepts/axpy.md` and `concepts/scal.md`); a subsequent retroactive-thinning pass on `book/src/L1/axpby.md` and `book/src/L1/axpbypcz.md` can then collapse Context-§ and Evidence-§ prose that is duplicated against those concept pages. Estimated additional savings: ~150-250 words across the two entries (rough order-of-magnitude, mirroring the cycle-006 per-entry yield). Not blocking; cycle-007+ candidate. Source: `reports/2026-05-27T081029Z-layer-intro-author-L1-scalar-promotion-thinning/CYCLE.md` §Open-questions/caveats item 4.

```yaml
---
slug: open-questions-ledger-backreference-audit
opened_at: cycle-006
opened_by: layer-intro-author
status: open
---
```

Housekeeping question surfaced by the cycle-006 `L1-scalar-promotion-thinning` dispatch (critic Finding 5; repairer flagged as unrepairable / deferred). When per-entry pointers to an open question are removed during a retroactive-thinning pass (here: 4 L1 entries previously each contained a pointer to `scalar-promotion-typing-rule`, now removed in favour of the canonical pointer on `concepts/scalar-promotion.md`), it is unclear whether the ledger entry for the open question at `scaffolding/open-questions.md` carries any per-site "referenced-from" backreferences that go stale. Direct inspection of the `scalar-promotion-typing-rule` ledger entry at line 53 shows no such backreference field today — the ledger uses a free-text format without structured per-site backreferences — but the ledger schema may grow such a field, or a future cross-cutter may want to query "where in the artifact is this OQ referenced?" and rely on backreferences. **Candidate resolution**: a future meta-phase or layer-intro-author pass either (a) confirms the ledger format does not require per-site backreferences (close as not-needed), or (b) adds a schema field for backreferences and writes a `tools/` script to maintain it (close as resolved-by-tooling). Non-urgent — the current ledger format is correct and complete without backreferences, this is forward-looking hygiene. Source: `reports/2026-05-27T081029Z-layer-intro-author-L1-scalar-promotion-thinning/META.md` §Critique-Finding-5 and §Repair-unrepairable.

```yaml
---
slug: krylov-step-l3-identity-in-form-audit-closure-cycle-006
opened_at: cycle-006
opened_by: abstractor
status: closure-note
relates_to: krylov-step-l3-identity-in-form-audit (cycle-005), krylov-step-l3-row-contingency (cycle-006)
---
```

The cycle-006 wave-2 abstractor dispatch (`reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"Audit of cycle-002 identity-in-form claim") audits the cycle-005 open question `krylov-step-l3-identity-in-form-audit` and proposes resolution as **confirmed-with-refinement**. The cycle-002 framing ("L2>L3 step-body lift is identity-in-form") is **confirmed as stated** on the L3>L2 edge for the kernel body. The cycle-006 audit refines to: "**L4>L3>L2 step-body chain is identity-in-form on the kernel body's primitive sequence**; the L4>L3 hop is non-identity *at the wrapper level* (records dissolve, monad dissolves, readonly typing demotes, Form A/B presentation collapses), but the body's dataflow chain survives both hops textually unchanged." Evidence re-read for this audit: `book/src/spec/slices/cg.md:341-362` (Claim 2 verbatim "identity in form"), `book/src/spec/slices/arnoldi_step.md:178-213` (uncontested primitives plus localised MGS-orthog obstruction, which is below the step body). **Consequence**: no L3 `krylov-step` row is proposed; the L4 entry transitively lowers to L2 via the cycle-006 L4>L3 wrapper-dissolution theme (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`) plus a one-line L3>L2 body-identity theme to be authored in cycle-007 (see sibling open question `krylov-step-body-identity-theme-pending-cycle-007`). The cycle-006 wave-1 harvester-promoted `krylov-step-l3-row-contingency` is also resolved by the same audit: the contingency triggered by "non-identity rotation at L3 body" did not fire; the defensive L4 entry's "Lowers to" wording (L4>L3>L2 with no interposed L3 row) stands as-is. **Disposition for meta-phase**: mark `krylov-step-l3-identity-in-form-audit` and `krylov-step-l3-row-contingency` as resolved by this closure-note; the cycle-006 audit is the resolution evidence. Source: `reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"Audit of cycle-002 identity-in-form claim" and §"Open questions / caveats" item 1.

```yaml
---
slug: krylov-step-body-identity-theme-pending-cycle-007
opened_at: cycle-006
opened_by: abstractor
status: closed
answered_at: cycle-007
answered_in: reports/2026-05-27T160445Z-abstractor-krylov-step-body-identity-L3-L2/CYCLE.md (theme authored as `book/src/L3-L2/krylov-step-body-identity.md`; ratifies cycle-006 audit)
---
```

The cycle-006 wave-2 abstractor dispatch authored the L4>L3 `krylov-step-typed-wrapper-dissolution` theme and confirmed (with refinement) the cycle-002 identity-in-form claim for the L3>L2 body rewrite. Per the audit's verdict, the L4>L2 chain factors into the cycle-006 L4>L3 hop (wrapper dissolution) plus an L3>L2 hop that is identity-in-form on the body. The L3>L2 hop has NOT been authored as a theme entry under `book/src/L3-L2/`. **Candidate cycle-007 dispatch**: a short `abstractor` invocation authoring `book/src/L3-L2/krylov-step-body-identity.md` (one-line theme: the L3 body produced by `krylov-step-typed-wrapper-dissolution` lowers to L2 by identity-in-form; LHS = L3 form per the cycle-006 theme's RHS, RHS = L2 form per `book/src/L2/krylov-step.md` §Semantics, justification = `empirical-match` per the cycle-002 claim). Low-cost dispatch (single short theme); should be slotted alongside the cycle-007 harvester on the L4 loop-combinator family (see `iterate-while-l4-anchor-missing` cycle-006 OQ) for symmetric completion of the krylov-step lowering chain. The cycle-006 dispatch explicitly scoped this out as "one theme per invocation" — the sibling theme is the natural cycle-007 follow-up. Source: `reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"Open questions / caveats" item 5.

**Cycle-007 closure**: the cycle-007 wave-1 abstractor dispatch (`reports/2026-05-27T160445Z-abstractor-krylov-step-body-identity-L3-L2/`) authored the theme as `book/src/L3-L2/krylov-step-body-identity.md`, displacing the L3-L2 index's `(empty — Phase B skeleton.)` placeholder with the first firm-rough-in theme row. Justification: `empirical-match` (cycle-002 combinator-miner claim; cycle-006 audit confirmed-with-refinement) with secondary `structural`. Status declared `firm-rough-in` with `rough-in` inherited from the upstream L4>L3 theme; promotion to plain `firm` follows automatically when the upstream theme is itself promoted. Body-level mapping is line-for-line identity over six body bindings; the two surface adjustments at the wrapper ((K, s) → unified `IterState`; outer-loop tail-recursion → outer-driver-by-role) are state-hiding / abstraction-by-role rotations explicitly delimited from the body. The L3>L2 hop of the `krylov-step` lowering chain is now structurally housed under `book/src/L3-L2/` for symmetric coverage.

```yaml
---
slug: iterate-while-l3-rendering-trajectory-accumulation-gap
opened_at: cycle-006
opened_by: abstractor
status: answered
answered_at: cycle-008
answered_in: reports/2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close/CYCLE.md
relates_to: iterate-while-l4-anchor-missing (cycle-006)
---
```

The cycle-006 wave-2 abstractor dispatch's §"What the L3 form for `iterate_while` looks like" subsection (within `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`) renders the L3 lowering of `iterate_while` as a tail-recursive value-threading loop returning a single `readout` when `continue = false`. But the L4 `iterate_while` signature given earlier in the same theme is `Step -> carry -> Solve Trajectory` with `Trajectory = [readout]` — the L4 form accumulates readouts across iterations subject to demand-pruning. The L3 tail-recursive form as written drops the trajectory accumulator, which is an actual semantic change in the rotation rather than a wrapper dissolution. **Two candidate resolutions** (deferred to cycle-007): (a) re-render the L3 form with explicit `trajectory` accumulator pass-through (`[readout]` rather than a single `readout`); (b) author an explicit demand-pruning step that justifies the collapse to a single readout when no downstream consumer reads the trajectory. Both are substantive rotation decisions exceeding repair authority. **Routes to cycle-007**: (i) `lowering-verifier` dispatch follow-up — already named in the theme's §Status — should reconcile the L3 rendering with the L4 trajectory shape; or (ii) cycle-007 `harvester` on the L4 loop-combinator family (per the cycle-006 OQ `iterate-while-l4-anchor-missing`) resolves as part of formalising `iterate_while`'s firm signature. The primary content of the cycle-006 dispatch — the four-part wrapper-dissolution theme for `krylov-step` itself — is unaffected by this gap; the sub-issue is on the speculative L4 loop combinator's L3 shape, not on the `krylov-step` body's rotation. Source: `reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md` §"Open questions / caveats" item 8 (added by repairer per critic Finding 3).

**Cycle-007 update**: the cycle-007 harvester on the L4 loop-combinator family (`reports/2026-05-27T160550Z-harvester-iterate-while-family-L4/`) firmed the L4 signature with an explicit trajectory accumulator `[{ ...e }]` and the demand-pruning law (Law 1 of `book/src/L4/iterate-while.md`). The harvester did NOT reconcile the L3 form (which still drops the trajectory per `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for iterate_while looks like" lines 156-167). The gap remains for cycle-008+ lowering-verifier: dispatch on `iterate-while-l4-l3` to author a standalone `book/src/L4-L3/iterate-while-dissolution.md` theme reconciling the L3 rendering with the firm L4 trajectory shape. The cycle-007 harvester explicitly scoped this out per the "one operator per invocation" discipline. Both candidate resolutions enumerated above — (a) trajectory accumulator pass-through; (b) explicit demand-pruning step — remain live options; the cycle-007 harvester did not pick between them.

**Cycle-007 wave-2 verdict (audit verdict-(c); status remains `open` pending cycle-008+ lifter)**: the cycle-007 wave-2 lowering-verifier dispatch (`reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/`) audited the gap against the just-firmed L4 chapters and the Palace KSP consumer surface. **Verdict: (c) — L3 single-readout is correct; L4>L3 lowering needs explicit §3.8 collapse-rule citation.** The audit's key L0/L1 findings: (i) Palace's `IterativeSolver` result-extraction surface materializes exactly four scalars (`converged`, `initial_res`, `final_res`, `final_it`) at `reference/palace/palace/linalg/iterative.hpp:52-55` with four getters at `:97-108`; (ii) the sole caller of that surface is `BaseKspSolver::Mult` at `reference/palace/palace/linalg/ksp.cpp:296-310`, consuming exactly those four scalars (branch on `GetConverged`, ratio in warning via `GetFinalRes()/GetInitialRes()`, sum into counter via `GetNumIterations`); (iii) the PCG outer loop (`iterative.cpp:420-485`) and GMRES inner loop (`:614-705`) retain no per-iteration residual history — per-iteration `res`/`beta` is either printed inline under `print_opts.iterations` or overwritten; (iv) no Palace unit test asserts on per-iteration residual values (`test/unit/` directory has no `test-ksp*`/`test-cg*`/`test-gmres*`). The four scalars are all `final_state`-equivalent (carry fields at termination or pre-loop initialization), so Law 1 of `book/src/L4/iterate-while.md` fires and the trajectory collapses to `[]` — the L3 single-readout form is the §3.8-pruned form of the L4 generality, not a different combinator. Both originally-enumerated candidate resolutions are subsumed: (a) [promote L3 to trajectory] was the wrong direction (would have promoted L3 to a trajectory it does not need); (b) [explicit demand-pruning step] was a less-precise framing of verdict-(c). A new applicability **Condition 5** for the cycle-006 theme surfaces from this audit: *"The downstream consumer observes only `final_state`-equivalent quantities of the `iterate_while` invocation; per Law 1 (§3.8 demand-pruning), the trajectory then prunes to `[]` and the L3 form is the single-readout shape."* The full audit including `verified_against:` evidence-block proposal lives in `reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/CYCLE.md`. **Status remains `open`**: the audit produces evidence + verdict but the substantive patch (cite Law 1 + `concepts/derived-view-hoisting.md` §"Worked example: CG residual norm" at `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for iterate_while looks like"; add Condition 5 to §"Applicability conditions") is out-of-lowering-verifier-authority and routes to a cycle-008+ `lifter` dispatch. Closure becomes appropriate once that lifter patch lands. Orthogonal new OQ `iterate-while-log-effect-vs-trajectory-channel` (cycle-007, opened by lowering-verifier) tracks the unrelated logging-effect channel question.

**Cycle-008 closure** (lifter dispatch `2026-05-27T173217Z`): the cycle-008 lifter dispatch on `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (`reports/2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close/CYCLE.md`) applied the cycle-007 wave-2 audit's three proposed substantive changes: (1) §"What the L3 form for `iterate_while` looks like" was rewritten with a §3.8 preamble citing Law 1 of `book/src/L4/iterate-while.md` and `book/src/concepts/derived-view-hoisting.md` §"Worked example: CG residual norm", plus a two-form sketch (pruned + unpruned) governed by Condition 5 and exhibiting the L3-side image of Law 1 as a $$ ... $$ reduction rule; (2) §"Applicability conditions" gained a new Condition 5 naming the consumer-demand precondition with Palace-specific evidence (`iterative.hpp:52-55` four-scalar surface + `ksp.cpp:296-310` sole caller); (3) a trailing `verified_against:` block was appended carrying the 10-citation audit evidence base; (4) `Status:` was promoted from `rough-in` to `firm`. The OQ is **closed** as `answered` (status: answered, answered_at: cycle-008, answered_in: the cycle-008 lifter dispatch report). The L3>L2 theme `book/src/L3-L2/krylov-step-body-identity.md` is now auto-eligible for `firm-rough-in` → `firm` promotion via status-inheritance (the upstream L4>L3 theme is now firm); this promotion is not applied by this dispatch and is routed as a cycle-009 integrator-signals suggestion. The orthogonal new OQ `iterate-while-log-effect-vs-trajectory-channel` (cycle-007, opened by lowering-verifier) remains open and is unaffected by this closure.

```yaml
---
slug: ksp-solve-concept-page-signature-update
opened_at: cycle-007
opened_by: harvester
status: open
---
```

The early-cycle methodology concept page `concepts/ksp_solve.md` documents `ksp_solve(ksp: KSP, b: Vector) → Vector` (a single solution-vector return). The cycle-007 firm L1 chapter `L1/ksp_solve.md` documents `ksp_solve(K, b) → SolveResult[N]` (a structured return carrying solution + four solve-statistics fields). Should the concept page be updated to match the L1 chapter's `SolveResult` signature, or is it intentional that the concept-page surface is the simpler narrative form?

Precedent from `concepts/nrm2.md` vs `L1/nrm2.md` (cycle-002+ thinning sweep) suggests the concept page should be updated to defer to the L1 chapter on factual claims while preserving the narrative framing. A future dispatch (likely under priority #11 retroactive-context-thinning or a follow-up concept-page sync) could update the concept-page signature line + add a "Solution-vs-result-record" note pointing at the L1 chapter's `SolveResult` definition. Not blocking. Source: `book/src/concepts/ksp_solve.md` vs `book/src/L1/ksp_solve.md` signature.

```yaml
---
slug: ksp-solve-mutation-rotation-l1-l0-theme
opened_at: cycle-007
opened_by: harvester
status: answered
answered_at: cycle-008
answered_in: 2026-05-27T173255Z-abstractor-ksp-solve-mutation-rotation-L1-L0
---
```

The firm L1 `ksp_solve` operator (cycle-007) now exists. The L1>L0 lowering theme that maps `ksp_solve(K, b) → SolveResult` to `BaseKspSolver::Mult(b, x)` + initial-guess threading + workspace allocation + statistics-counter mutation + convergence-warning `Mpi::Warning` logging is a natural next dispatch. Existing L1>L0 themes (`axpby-mutation-rotation`, `axpbypcz-mutation-rotation`, `apply-linop-mutation-rotation`) provide the precedent shape. Should this theme be queued for an `abstractor` or `lifter` dispatch in cycle-008 or later?

cycle-007 priority slate may or may not have this slot; cycle-008 cycle-planner can promote based on whether other L1>L0 work is already in progress. Not blocking. Source: `book/src/L1/ksp_solve.md` firm; no corresponding L1>L0 lowering theme yet.

**Cycle-008 closure** (`reports/2026-05-27T173255Z-abstractor-ksp-solve-mutation-rotation-L1-L0/CYCLE.md`): the cycle-008 wave-1 abstractor authored `book/src/L1-L0/ksp-solve-mutation-rotation.md` as the first firm L1>L0 theme for a constructed-operator-absorption operator. The theme documents 4 sub-patterns (A: workspace allocation; B: initial-guess threading; C: statistics-counter mutation; D: convergence-warning `Mpi::Warning` logging) and outer-loop variants for {CG, GMRES, FGMRES}. The dispatch also displaced the `(empty — Phase B skeleton.)` placeholder in `book/src/L1-L0/index.md` with the first firm dep-map row. Note: the original dispatch wrote directly to `book/` during execution (write-authority violation), repaired post-hoc via Option A revert + supporting-doc co-location + canonical proposed-changes rewrite; pattern tracked under OQ `abstractor-write-authority-violation-cycle-008` for cycle-009 meta-phase aggregation.

```yaml
---
slug: l1-intro-refresh-after-constructed-operator-gate
opened_at: cycle-007
opened_by: harvester
status: answered
answered_at: cycle-008
answered_in: 2026-05-27T181512Z-layer-intro-author-L1-intro-refresh
---
```

The L1 layer-intro `Context` and `Semantics (overlay)` sections previously framed L1 as a BLAS-1-plus-opaque-operator surface. With cycle-007's `ksp_solve` adding the constructed-operator gate (the first L1 operator whose primary argument is a structured opaque value), the layer's semantic motif count grows from 3 to 4. The dep-map and motif list have been updated; should `layer-intro-author` revisit the broader framing in a follow-up dispatch (e.g. add a paragraph in `Context` calling out the constructed-operator absorption as the layer's transition point to upper-layer vocabulary)?

This is a polish-level concern; the current intro is correct and not misleading. cycle-008 or later can queue this if other layer-intro work is happening; otherwise the four-motif structure is self-explanatory. Source: `book/src/L1/index.md` updated to add "Constructed-operator absorption" as the fourth semantic motif.

**Cycle-008 closure**: The cycle-008 `layer-intro-author` refresh dispatch (`2026-05-27T181512Z-layer-intro-author-L1-intro-refresh`) closed the loop with three surgical edits to `book/src/L1/index.md`: (1) appended a closing sentence pair to Semantics-overlay motif 4 naming the firm L1>L0 lowering `ksp-solve-mutation-rotation` (cycle-008) and its four absorption rules + three sister-theme primitives; (2) annotated the dep-map's `ksp_solve` row Status cell with a parenthetical L1>L0 cross-link; (3) appended a Working Notes bullet recording the cycle-008 L1>L0 landing. The "follow-up dispatch (e.g. add a paragraph in `Context`...)" the OQ asked about turned out unnecessary — the cycle-007 Context bullet 6 (added by the harvester at OQ-filing time) already explicitly framed `ksp_solve` as the layer's transition-point to upper-layer vocabulary with the four-axis absorption story; the only remaining polish was the L1>L0 closing-the-loop cross-references, which Edit 1 + Edit 3 supplied. No further L1 intro framing changes warranted by this cycle's landings. Status flipped `open` → `answered`.

```yaml
---
slug: gmres-inner-loop-iterate-while-migration
opened_at: cycle-007
opened_by: harvester
status: answered-by-rough-in-theme
answered_at: cycle-008
answered_in: 2026-05-27T180000Z-abstractor-gmres-inner-loop-iterate-while-migration
relates_to: iterate-while-l4-anchor-missing (cycle-006, answered cycle-007)
---
```

The cycle-007 harvester on the iterate-while family settled the L4 anchor for `iterate_while` (Form A) and `iterate_while_with_prev` (Form B). The cycle-005 GMRES slice's L4 section (`book/src/spec/slices/gmres.md:459-470`) renders `inner_loop` as an inline tail-recursive `Solve`-monad function (`inner_loop op conv K = do ... if conv.satisfied K3.beta || K3.j + 1 == op.max_dim || s.it == op.max_it then pure K3 else inner_loop op conv K3{ j = K3.j + 1 }`) rather than as a call to `iterate_while`. With the L4 row now firm, the GMRES rendering can be migrated to use `iterate_while` directly, surfacing the predicate (`\K -> not (conv.satisfied K.beta) && K.j + 1 < op.max_dim && s.it < op.max_it`) and the step body (`\K -> do { ... ; pure { state: K3{ j = K3.j + 1 }, ... } }`) as separate functions. **Benefits**: matches the CG v0.4 rendering pattern (`cg.md:215-219`); makes the trajectory shape explicit (GMRES extras are `{ residual_norm: Scalar, breakdown_token: BreakdownTag }`); enables Form-B adoption if the cycle-007/008 first-iteration-unrolling analysis on GMRES finds it warranted. **Cost**: a self-rotation v1.0→v1.1 on `gmres.md` §L4; needs a lifter or abstractor dispatch. **Routes to cycle-008+ lifter** on `gmres §L4`. Source: `reports/2026-05-27T160550Z-harvester-iterate-while-family-L4/CYCLE.md` §"Open questions / caveats" item 2.

**Cycle-008 closure** (`reports/2026-05-27T180000Z-abstractor-gmres-inner-loop-iterate-while-migration/CYCLE.md`): the cycle-008 abstractor authored the L4>L3 lowering theme `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` as a **rough-in** capturing (a) the migrated L4 form (LHS) with the witness-into-carry hoist via the speculative `check_stop_into_carry` helper, (b) the corresponding L3 form (RHS) with `Solve` dissolved + `iterate_while` dissolved + trajectory pruned per Law 1, (c) variant-axis pass-through analysis for all four GMRES axes (`pc_side`, `gs_orthog`, `flexible`, `max_dim`), and (d) three design caveats — alternative-combinator (`iterate_while_with_stop_witness`), promotion-criterion for `check_stop_into_carry` (defer until a second slice needs it), and Form-B-vs-Form-A choice (provisional: Form A; GMRES first-iteration is shape-invariant). The theme is **rough-in** because it depends on an upstream gmres.md §L4 v0.6→v0.7 self-rotation that has not been authored; **status flipped to `answered-by-rough-in-theme`** rather than `answered` because the firming will require a subsequent lifter dispatch on `gmres.md §L4` to actually perform the migration. The follow-up OQs surfaced by the rough-in (alternative-combinator choice; helper-promotion decision; Form-B confirmation) are recorded inline in the new theme's §Status and the report's §"Open questions / caveats" — they route to cycle-008+ lifter / cycle-008+ harvester / cycle-008+ combinator-miner respectively, and do not need separate OQ entries because they are scoped to the upstream gmres.md migration which is itself the explicit cycle-008+ follow-up.

```yaml
---
slug: iterate-while-pure-promotion-decision
opened_at: cycle-007
opened_by: harvester
status: open
relates_to: iterate-while-l4-anchor-missing (cycle-006, answered cycle-007)
---
```

The cycle-007 harvester on the iterate-while family settled `iterate_while` and `iterate_while_with_prev` as two firm L4 rows. The strawman §3.7 also names `iterate_while_pure :: α -> (α -> Bool) -> (α -> α) -> α` as a sugar for the no-extras case; this is used by the LBM example (`l4_calculus.md:374-386`). The cycle-007 harvester adopted the sugar inside `book/src/L4/iterate-while.md` §Semantics as a definitional shortcut (`iterate_while_pure a p f ≡ (iterate_while a p (\x -> { state: f(x) })).final_state`) rather than as a separate L4 row. **Two candidate resolutions** (deferred): (a) keep the sugar inside `iterate-while` as a definitional reduction; future slices invoking the no-extras pattern reference the sugar inline. (b) promote `iterate_while_pure` to a third firm L4 row with its own chapter; the chapter would be ~1/3 the size of `iterate-while` since most laws and discipline are identical. **Cost-benefit**: (a) keeps the L4 vocabulary small but spreads the sugar usage across slice-level pseudo-code; (b) gives slice authors a one-line `iterate_while_pure` to reference but adds a row whose primary content is "see `iterate-while` Laws 1-4". **Routes to cycle-008+ harvester or planner**: defer decision until a second non-Krylov slice (e.g., LBM at a future Palace transient solver write-up, or a per-element time-step iteration) actually needs the sugar enough to outweigh the "see also iterate-while" cross-reference cost. Source: `reports/2026-05-27T160550Z-harvester-iterate-while-family-L4/CYCLE.md` §"Open questions / caveats" item 3.

```yaml
---
slug: iterate-while-log-effect-vs-trajectory-channel
opened_at: cycle-007
opened_by: lowering-verifier
status: open
relates_to: iterate-while-l3-rendering-trajectory-accumulation-gap (cycle-006, open — cycle-007 verdict-(c) recorded, closure deferred to cycle-008+ lifter patch)
---
```

The cycle-007 firm L4 `iterate-while.md` / `iterate-while-with-prev.md` model iteration as `Solve = StateT SimState Identity` — a state-monad over `SimState` with no logging effect. Palace's L0 surface (e.g., `reference/palace/palace/linalg/iterative.cpp:422-426` for PCG, `:617-621` for GMRES) emits per-iteration residuals via `Mpi::Print` conditional on `print_opts.iterations`. The audit verdict-(c) resolution of `iterate-while-l3-rendering-trajectory-accumulation-gap` (`reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/CYCLE.md`) closed the return-value trajectory question (single-readout L3 form is correct under §3.8 pruning), but the *logging-channel* observation is independently present in Palace and not currently captured by the L4 calculus. Should `Solve` be extended to a richer effect representation (e.g., `Solve = RWST OpParams (DList LogEntry) SimState Identity`) so the print-when-`print_opts.iterations` behavior becomes a free-monad-style `tell` rather than an out-of-band side-effect? Orthogonal to the trajectory-collapse question — affects effect-modeling discipline, not the trajectory shape. Routes to a cycle-008+ `lowering-verifier` or `abstractor` dispatch (or, more likely, surfaces during meta-phase methodology review of the L4 monad surface). Not blocking. Source: `reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/CYCLE.md` §"Open questions / caveats" item 1.

```yaml
---
slug: eigsolve-l1-operator-rough-in-candidate
opened_at: cycle-008
opened_by: layer-intro-author
status: open
---
```

The new `eigensolver-wrapper` chapter notes that the three concrete branches (ARPACK RCI / SLEPc shell-matrix / Palace's direct-Newton `QuasiNewtonSolver`) realize three distinct orchestration patterns but expose a uniform problem-type axis (linear / quadratic / nonlinear). A future L1 `eigsolve` operator would absorb the orchestration axis as transparent dispatch and expose only the problem-type axis + `ScaleType` + `WhichType` + `SetShiftInvert` mode. The operator is sized similarly to `ksp_solve` (stateful inner loop, configured inner linear solver via `SetLinearSolver`) and is a natural cycle-009+ harvester target. The L4 calculus's `iterate_while` primitive (per `book/src/design/l4_calculus.md`) is the natural composition target for the RCI / shell-matrix branches; the direct-Newton branch composes against the calculus's regular `bind` + inner `solve` primitive. **Test-coverage constraint on the harvester**: there is no dedicated `test-eigensolver.cpp` under `palace/test/unit/` (see `eigensolver-wrapper` chapter §"Test coverage"). The future `L1/eigsolve` harvester will need to lean more heavily on direct source reading + literature anchors (Higham 2008, Lehoucq-Sorensen, Hernandez-Roman-Vidal) than `L1/ksp_solve` did (which had `test-orthog.cpp` as a direct algebra anchor), and the resulting algebraic equivalence claims will accordingly carry weaker test-linkage evidence. Routes to harvester (`L1/eigsolve`) once `L1/ksp_solve` settles. Source: `reports/2026-05-27T173523Z-layer-intro-author-L0-bootstrap-bundle-4/CYCLE.md` §Open questions item 1.

```yaml
---
slug: matrix-weighted-norm-and-bilinear-form-l1-rough-ins
opened_at: cycle-008
opened_by: layer-intro-author
status: open
---
```

The new `linalg-operator-file` chapter notes that the `palace::linalg::` free functions `Norml2(comm, x, B, Bx)` and `Dot(comm, x, A, y)` are matrix-weighted variants of L1's existing `nrm2` and `dot` operators (weighted by an SPD `B` or bilinear-form `A`, respectively). They have not been harvested at L1. Candidate rough-in names: `L1/nrm2_weighted` and `L1/dot_bilinear`. The workspace-internal-allocation pattern in `Dot` (`palace/linalg/operator.cpp:621-639`) is Category 4 of `mutable-workspace-pattern` (synthetic workspace). `SpectralNorm` (`palace/linalg/operator.hpp:398-401`) is power iteration with configurable tolerance — also unharvested. Candidate rough-in name: `L1/power_iterate`. Sized smaller than `eigsolve` (single largest eigenvalue, no eigenvector recovery, no spectral transformation). Routes to cycle-009+ harvester / abstractor. Source: `reports/2026-05-27T173523Z-layer-intro-author-L0-bootstrap-bundle-4/CYCLE.md` §Open questions item 2.

```yaml
---
slug: l0-bundle-5-candidates
opened_at: cycle-008
opened_by: layer-intro-author
status: open
---
```

L0 chapter count after bundle 4 is 14. Remaining candidates from cycle-007 priority #10 not yet authored: (1) `linalg-solver-file` — `palace/linalg/solver.{hpp,cpp}` file overview (companion to `mfem-wrapper-solver`, covering the `Solver<OperType>` base class and the auxiliary preconditioner classes that aren't already named); currently the only file-level coverage of `solver.{hpp,cpp}` is the `mfem-wrapper-solver` chapter's per-class view; the file-level overview would mirror `linalg-operator-file` / `linalg-iterative-file` / `linalg-vector-file`. (2) `tests-as-semantic-supplement` — convention page documenting how `palace/test/unit/` is treated as L0-equivalent semantic evidence per `CLAUDE.md` "Tests as semantic supplement"; cross-cutting; would replace per-chapter restatement of the convention. (3) `preconditioner-classes-overview` — survey of the preconditioner classes not yet covered (`HypreAmsSolver`, `BoomerAMG`, `StrumpackSolver`, `JacobiSmoother`, `ChebyshevSmoother`, `DistRelaxation`, `BlockPreconditioner`, `GeometricMultigrid`); sized to a file-overview chapter; some of these have their own files. Bundle 5 (cycle-009 dispatch) should pick 2-3 of these per the 1-3 chapters/cycle cadence. Recommend `linalg-solver-file` as the highest-priority candidate (closes the file-overview gap on the four `linalg/` anchor files referenced by L1). Routes to future L0 bundle 5 dispatch. Source: `reports/2026-05-27T173523Z-layer-intro-author-L0-bootstrap-bundle-4/CYCLE.md` §Open questions item 3.

### abstractor-write-authority-violation-cycle-008 (opened cycle-008 by repairer)

**Priority**: critical-for-meta (cycle-009 meta-phase aggregation candidate)

**Context**: cycle-008 dispatch
`reports/2026-05-27T173255Z-abstractor-ksp-solve-mutation-rotation-L1-L0/`
authored the L1>L0 `ksp-solve-mutation-rotation` theme by writing
directly to three artefact files:

- `book/src/L1-L0/ksp-solve-mutation-rotation.md` (new file, created directly)
- `book/src/L1-L0/index.md` (modified directly)
- `book/src/SUMMARY.md` (modified directly)

Per CLAUDE.md "Write-authority partition" and
`.claude/agents/abstractor.md:23`, specialized agents (including
abstractor) may write only to `reports/<id>/CYCLE.md + supporting
docs in same dir only`. The integrator-per-report has sole authority
to apply proposed-changes to `book/`.

The dispatch DID also emit `edit:` proposed-changes blocks in CYCLE.md
(lines 82-108) — so the violation was redundant execution, not missing
channel work. The repairer reverted the direct writes via
`git checkout --` + `rm`, moved the theme file content to the report
dir as a co-located supporting doc, and rewrote the proposed-changes
blocks to the canonical `edit:` `[old]:` / `[new]:` fence format
matching the cycle-007 L0 bundle 3 precedent. Per Option A in the
repairer prompt.

**Meta-phase questions for cycle-009 aggregation**:

1. Did multiple abstractor (or other specialized-agent) dispatches in
   the cycle-007 / 008 / 009 batch exhibit the same direct-write
   pattern? If yes, the role-spec wording at
   `.claude/agents/abstractor.md:23` ("The integrator applies (c)") is
   too easy to overlook — the prominent `edit:` fence headers
   elsewhere in the role spec (which use `book/src/...` paths) may be
   priming the agent to actually execute those edits rather than only
   emit them.

2. Should the abstractor role spec hoist the integrator-authority
   reminder above the `edit:` fence examples, or repeat it inside the
   fence header conventions?

3. Should the integrator-per-report add a safety-net gate that detects
   `git status` showing already-modified `book/` files at dispatch
   time? Currently the gate is implicit (the proposed-changes apply
   step would conflict or duplicate).

**Status**: open. Action belongs to cycle-009 meta-phase.

## Dropped

(empty — will accumulate)

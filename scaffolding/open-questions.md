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
status: answered
answered_at: cycle-012
answered_in: book/src/concepts/nrm2.md (§Contract stability bullet)
---
```

`book/src/concepts/nrm2.md:9` claims Palace uses "scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow". This is **factually wrong**: `palace/linalg/vector.hpp:255-260` shows Palace's `linalg::Norml2` is the naive `√⟨x,x⟩` form (literal one-line `std::sqrt(std::abs(Dot(comm, x, x)))`). Either Palace's `dot` kernel ultimately bottoms out in a Hypre / BLAS routine that scales internally (worth verifying — L1>L0 lowering concern), or Palace is naive and the concept page is simply wrong. Routes to same-layer-cross-cutter (concept-page reconciliation) or layer-intro-author (per cycle-003 follow-up).

**Answered cycle-012 (layer-intro-author concept-corrections; applied by integrator-per-report).** Resolved in favour of "Palace is naive and the concept page is simply wrong": the `linalg::Norml2` one-line body is the naïve `√⟨x,x⟩` via `Dot` with no internal scaling. The false stability bullet was replaced with the L1-authoritative description and now forwards to `[L1/nrm2](../L1/nrm2.md)`. This is the cycle-003-vintage original of the same correction tracked by the cycle-011 duplicate of this slug (also closed cycle-012); both are now landed. Source: cycle-012 layer-intro-author dispatch `reports/2026-05-28T034221Z-layer-intro-author-concept-corrections/CYCLE.md` Task 1.

```yaml
---
slug: nrm2-B-weighted-energy-norm-harvest
opened_at: cycle-003
opened_by: harvester
status: partially-answered
last_revisited: cycle-010
---
```

The L0 surface uses overloading: `linalg::Norml2(comm, x)` (this cycle's firm `nrm2`) and `linalg::Norml2(comm, x, B, Bx)` (operator-weighted norm `‖x‖_B = √(xᴴ B x)` at `operator.cpp:600-619`). At L1 these are distinct operators. The B-weighted form requires an `apply`-style operator-application primitive (not yet in the L1 dep-map), an SPD precondition on `B`, and a workspace `Bx`. Queue a `nrm2_B` or `energy_norm` harvester invocation once `apply` (matrix-vector multiplication) is firm at L1.

**Partially answered cycle-010**: The cycle-010 wave-1 harvester landed `book/src/L1/matrix-weighted-norm.md` (`reports/2026-05-27T215334Z-harvester-matrix-weighted-norm-l1/`) as a `rough-in (test-coverage-bounded)` L1 operator covering the SPD operator-weighted Euclidean norm `‖x‖_B = √(xᴴ B x)` at L0 anchor `palace/linalg/operator.cpp:599-619`. The cycle-010 wave-2 #5 harvester sibling dispatch (`reports/2026-05-27T220123Z-harvester-nrm2-B-weighted-energy-norm-l1/`) verified this as a **duplicate target** (case (c) merge-and-rename verdict): the slugs `nrm2_B-weighted-energy-norm`, `nrm2_B`, `nrm2_weighted`, `energy-norm` all name the same operator landed under the canonical slug `matrix-weighted-norm`. Same L0 anchor, same closed-form, same SPD applicability, same dependencies (`dot` + `apply_linop`), same element-type variant axis, same M-orthonormalisation callsite cohort. The energy-norm content of this OQ is therefore landed; the OQ is held `partially-answered` (rather than `answered`) only to track the firm-promotion gate (test coverage) carried forward on the sibling `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` parent ledger. Naming-axis residue (the L1 index `Queued` line and the L0 chapter `linalg-operator-file.md` prose still referencing `nrm2_B` / `nrm2_weighted`) is tracked under the wave-1 sibling's new OQ `matrix-weighted-norm-naming-sweep`.

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

```yaml
---
slug: krylov-step-theme-body-no-l3-row-drift-cycle-013
opened_at: cycle-012
opened_by: lifter
status: open
relates_to: krylov-step-l3-row-contingency (this ledger, answered cycle-006), krylov-step-l3-identity-in-form-audit-closure-cycle-006 (this ledger)
---
```

The L4>L3 theme `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` carries the correct SUPERSEDED annotation at line 218 (the §"Audit of cycle-002 identity-in-form claim" section, recording that the cycle-006 "no L3 row needed" verdict is superseded by the CLAUDE.md §Methodology invariants bullet "Identity-lowerings still require both L levels", with the cycle-010 backfill `book/src/L3/krylov-step.md` enacting it). But two earlier passages in the theme body still phrase the old conclusion as if live: line 20 ("...so **no L3 `krylov-step` row is promoted by this theme**...") and line 220 ("...the assertion holds, the framing is sharpened, **no L3 row needed**"). The critic confirmed both passages present by direct read (true positive). These are internally reconciled by the line-218 SUPERSEDED annotation but read as drift to a fresh reader. The cycle-012 lifter dispatch (`reports/2026-05-28T034235Z-lifter-l4-index-superseded-drift/CYCLE.md`) re-anchored the *L4 index* cross-reference (`book/src/L4/index.md:40`) to the firm `L3/krylov-step.md` entry, resolving the last stale cross-reference in the L4 index, but the theme-body line-20/line-220 residual is outside that single-edit invocation's scope (one theme per invocation; that invocation re-anchored the L4 index). **Recommend a follow-up `lifter` dispatch** on `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` to re-anchor lines 20 and 220 to the firm `L3/krylov-step.md` entry, consistent with the line-218 annotation. Low-cost; not blocking. Routes to cycle-013+ planner.

```yaml
---
slug: plane-rotation-concept-page-canonical-pointer-repoint
opened_at: cycle-012
opened_by: same-layer-cross-cutter
status: open
relates_to: orthog-plane-rotation-stream-sub-slice-batch-3-joint-audit (this ledger, answered cycle-012), phase-1-corpus-reduction-audit (priority-19)
---
```

After the cycle-012 batch-3 reduction of the `orthog.md` plane-rotation sub-slice to a stub-pointer at `plane_rotation_stream.md`, the firm concept pages `book/src/concepts/plane-rotation-stream.md:37` ("primary dissection" → `orthog` slice), `book/src/concepts/givens_generate.md:27` ("Used in" → `orthog` slice), and `book/src/concepts/givens_apply.md:27` ("Used in" → `orthog` slice) cite the `orthog` slice as the canonical plane-rotation dissection / use-site, but the more-complete dissection now lives in `plane_rotation_stream.md` (`concepts/givens.md:40` already correctly cites `plane_rotation_stream`). These three cross-references should be repointed to `plane_rotation_stream.md`. Dispatch `layer-intro-author` to repoint them. Not blocking — the cross-references target the `orthog.md` *file* (not a specific line), so they do not literally dangle, but they now point at a stub for the plane-rotation content. Source: cycle-012 phase-1-corpus-reduction-batch-3 §slice-1 residual gap 3 + §"Open questions / caveats" item 2 (HEADLINE).

```yaml
---
slug: l1-divfree-projector-promotion
opened_at: cycle-012
opened_by: same-layer-cross-cutter
status: open
relates_to: phase-1-corpus-reduction-audit (priority-19), divfree-weakdiv-sign-convention-l0-verify (this ledger)
---
```

A firm `L1/divfree-projector` operator entry (Helmholtz-decomposition projector: `P(y) = y + Grad·K⁻¹(Z_bdr(WeakDiv·y))`) is pending lift. The slice-corpus `book/src/spec/slices/divfree.md` §L1/L2/L3/L4 is currently the only firm divfree definition; it is load-bearing evidence cited by `book/src/L1/ksp_solve.md:131,143`, `book/src/L1/eigsolve.md` (optional `projector` field), `book/src/concepts/apply_linop.md:41-54`, `book/src/concepts/ksp_solve.md:34`, `book/src/concepts/set_subvector_zero.md:27`, and `book/src/L0/eigensolver-wrapper.md:44`. Promotion criterion (small AND simplifies higher forms) is met: divfree is a small 4-step apply over a once-constructed operator, AND lifting would let `L1/eigsolve` reference `DivFreeSolver` as a firm operator type and let the three concept-page use-site citations point at a firm L1 entry rather than the slice. Strong harvester promotion candidate. Source: cycle-012 phase-1-corpus-reduction-batch-3 §slice-2 residual gap 1 + §"Open questions / caveats" item 3 (HEADLINE).

```yaml
---
slug: plane-rotation-givens-l0-citation-range-reconcile
opened_at: cycle-012
opened_by: same-layer-cross-cutter
status: open
relates_to: orthog-plane-rotation-stream-sub-slice-batch-3-joint-audit (this ledger, answered cycle-012)
---
```

The `plane_rotation_stream.md` §L0 citation line ranges (`iterative.cpp:72-108` generate-real / `:226-242` apply) differ by one from the firm `book/src/concepts/givens.md:33-34` ranges (`:73-108` / `:227-241`). A `verify-citation-range` pass should reconcile (likely the firm concept page is canonical and the slice is off-by-one). Minor; non-blocking. Source: cycle-012 phase-1-corpus-reduction-batch-3 §slice-1 residual gap 4 + §"Open questions / caveats" item 4(a).

```yaml
---
slug: divfree-weakdiv-sign-convention-l0-verify
opened_at: cycle-012
opened_by: same-layer-cross-cutter
last_revisited: cycle-015
status: resolved
relates_to: l1-divfree-projector-promotion (this ledger)
---
```

The divfree WeakDiv sign-convention claim — that `MixedVectorWeakDivergenceIntegrator` encodes the negative-divergence sign, making `+Grad·ψ` the correction (not `−Grad·ψ`) — is an unverified L0 reading (slice §"Open questions"). A flipped L0 sign would invert the correction direction at every layer. A `verify-citation-range` / harvester pass should anchor the sign to an L0 integrator citation before a firm `L1/divfree-projector` entry treats `+Grad·ψ` as a load-bearing claim. Source: cycle-012 phase-1-corpus-reduction-batch-3 §slice-2 residual gap 2 + §"Open questions / caveats" item 4(b).

```yaml
---
slug: phase-1-corpus-reduction-batch-4-remaining-slices
opened_at: cycle-012
opened_by: same-layer-cross-cutter
status: open
relates_to: phase-1-corpus-reduction-audit (priority-19), phase-1-corpus-reduction-remaining-7-slices (this ledger)
---
```

After batch-3 (cycle-012: `plane_rotation_stream` + `orthog` plane-rotation sub-slice [joint] + `divfree`), 8 of 10 slice files are audited. Two remain: `book/src/spec/slices/cg_preconditioning_framework.md` (priority #5; likely overlaps `L1/ksp_solve` + `L4/krylov-step` Form A + the chebyshev consumer pattern) and `book/src/spec/slices/sparse_triangular_solve.md` (priority #7; expected low-overlap / out-of-scope-obstruction per `concepts/sequential-obstruction.md` §"Sub-kind: out-of-scope-obstruction" which already cites it). Suggested batch-4: these final two slices via a cycle-013+ `same-layer-cross-cutter`-scoped dispatch per the "Phase 1 corpus reduces as material is lifted" invariant. Source: cycle-012 phase-1-corpus-reduction-batch-3 §"Open questions / caveats" item 8.

```yaml
---
slug: eigsolve-convergence-reason-mapping-promotion
opened_at: cycle-013
opened_by: lifter
status: open
relates_to: eigsolve-mutation-rotation Sub-pattern B gate (this ledger), partly-constructive-to-firm-promotion-route-ratification (this ledger)
---
```

The new sibling sub-theme `book/src/L1-L0/eigsolve-convergence-reason-mapping.md` is `partly-constructive`: its structural decomposition (the converged/diverged partition, the EPS/PEP/NEP per-family isomorphism, the whole-tree print-only negative anchor) is firm and exhaustively cited, but the per-row `EigStatus` assignment is a forward-looking reconstruction. **One global promotion condition covers all 8 partly-constructive diverged rows uniformly** (3 EPS diverged enumerators + the `*_CONVERGED_ITERATING` sentinel + 4 NEP-family diverged enumerators; PEP shares EPS's 3 rows non-additively; the 2 converged rows are count-anchored, not partly-constructive). The shared gate: promotion to firm is contingent on the **same** upstream behaviour change as parent Sub-pattern B — Palace reading the SLEPc reason code via `EPSGetConvergedReason` (it currently only PRINTS via `EPSConvergedReasonView` at `slepc.cpp:{699,1182,1529}`) and propagating it to the outer-loop status. This sub-theme's gate is strictly **downstream** of the parent Sub-pattern B gate (the reason map only materialises once the per-callsite inner-solve capture lands). A `lowering-verifier` audit may UNBLOCK (confirm the enum partition + accept the forward-looking shape per the cycle-012 `partly-constructive`-first-class invariant) without ENACTING. Routed to `lowering-verifier`. Source: cycle-013 slepc-convergence-reason-lift-sub-theme §Status.

```yaml
---
slug: eigsolve-convergence-reason-mapping-slepc-enum-upstream-confirm
opened_at: cycle-013
opened_by: lifter
status: open
relates_to: eigsolve-convergence-reason-mapping-promotion (this ledger)
---
```

Two upstream-confirmation items for the SLEPc reason-mapping sub-theme, both for a `lowering-verifier` pass. (1) **Enum names are documented-not-source-anchored.** The enumerator names (`EPS_DIVERGED_BREAKDOWN`, `EPS_DIVERGED_SYMMETRY_LOST`, `NEP_DIVERGED_LINEAR_SOLVE`, etc.) come from SLEPc's public headers (`slepceps.h` / `slepcnep.h`), NOT from Palace source (Palace references none — confirmed whole-tree zero-hit). Per CLAUDE.md "Many symbols resolve into upstream libraries", cross-check the exact per-version enumerator set against installed SLEPc headers under `reference/` if present, or log an upstream-behaviour note. The mapping *shape* (converged->success, breakdown->`LinearSolveFailed`, its->`MaxIterReached`) is robust to enum-name drift across SLEPc versions; only the exact per-version list needs confirmation. (2) **PEP/NEP isomorphism asserted, not exhaustively tabled.** The EPS family is tabled fully; PEP is asserted isomorphic-to-EPS and NEP adds three enumerators (`NEP_DIVERGED_LINEAR_SOLVE` / `NEP_DIVERGED_FUNCTION_COUNT` / `NEP_DIVERGED_SUBSPACE_EXHAUSTED`). A lowering-verifier wanting the PEP rows tabled explicitly is a small expansion; the print-only negative anchor (PEP at 1182, NEP at 1529) is identical across families, so no constructive status changes. Source: cycle-013 slepc-convergence-reason-lift-sub-theme §"Open questions / caveats" items 1 + 4.

```yaml
---
slug: chebyshev-l4-inner-loop-presentation-carry-st-vs-with-prev
opened_at: cycle-014
opened_by: repairer
last_revisited: cycle-015
status: resolved
relates_to: chebyshev-l4-firm-via-iterate-while-reanchor (this ledger)
---
```

When the cycle-015 firming follow-up (lifter/abstractor) re-anchors `L4/chebyshev.md`'s inner `k`-recurrence loop onto the firm `iterate-while` family, two firm-vocabulary-valid presentations remain to choose between. (a) **Plain `iterate_while_pure` with `st` in the carry** — carry `{ r, d, st, k }`, predicate `\c -> c.k <= op.order - 1`. (b) **`iterate-while-with-prev` threading `st`/`rho_prev` as the closure `prev`** — narrowed carry `{ r, d, k }`, mirroring the CG `beta_prev` recurrence-variable treatment (`iterate-while-with-prev.md:7` names Chebyshev `x_{k-1}`). The combinator-miner recommends the **plain carry-`st` form** as default (4th-kind `st = ()` makes it the degenerate no-prev case, unifying all kinds without a bootstrap step); the with-prev alternative is flagged for `same-layer-cross-cutter` if it wants to unify the `st`-carry with the `beta_prev`-carry under one recurrence-variable-threading note. Source: cycle-014 combinator-miner CYCLE.md §"Open questions / caveats" item 1 + §"Variant axes". Routes to lifter/abstractor (the firming follow-up).

```yaml
---
slug: chebyshev-l4-firm-via-iterate-while-reanchor
opened_at: cycle-014
opened_by: repairer
last_revisited: cycle-015
status: resolved
---
```

Firming follow-up for `L4/chebyshev.md` (cycle-013 rough-in). The cycle-014 combinator-miner decided route (i): the entry's two un-anchored `forM_`/`foldM` binds re-anchor onto the firm `iterate-while` family via `iterate_while_pure` with a **step-count predicate** (`s.it <= bound`), per strawman §6.5 step 5 (`l4_calculus.md:418`) + the canonical-primitive claim (`iterate-while.md:7`). A cycle-015 lifter/abstractor should enact: (1) the body re-anchor of §Signature/§Semantics (the concrete sketch is staged in the combinator-miner CYCLE.md §"Proposed combinator"), (2) the `L4/index.md` dep-map row rewrite — replace the `chebyshev` row's "iteration combinators UNRECONCILED" cell with the `iterate-while`-via-`iterate_while_pure` anchor, and flip Status `rough-in`→`firm`, moving chebyshev into the Firm-at-L4 cohort (count 3→4). The inner-loop presentation choice is the sibling OQ `chebyshev-l4-inner-loop-presentation-carry-st-vs-with-prev`. Source: cycle-014 combinator-miner CYCLE.md §"Proposed changes" (staged-not-applied edit block). Routes to lifter/abstractor.

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
status: partially-answered
partial_answer_at: cycle-009
partial_answer_in: reports/2026-05-27T191929Z-harvester-eigsolve-L1/
---
```

The new `eigensolver-wrapper` chapter notes that the three concrete branches (ARPACK RCI / SLEPc shell-matrix / Palace's direct-Newton `QuasiNewtonSolver`) realize three distinct orchestration patterns but expose a uniform problem-type axis (linear / quadratic / nonlinear). A future L1 `eigsolve` operator would absorb the orchestration axis as transparent dispatch and expose only the problem-type axis + `ScaleType` + `WhichType` + `SetShiftInvert` mode. The operator is sized similarly to `ksp_solve` (stateful inner loop, configured inner linear solver via `SetLinearSolver`) and is a natural cycle-009+ harvester target. The L4 calculus's `iterate_while` primitive (per `book/src/design/l4_calculus.md`) is the natural composition target for the RCI / shell-matrix branches; the direct-Newton branch composes against the calculus's regular `bind` + inner `solve` primitive. **Test-coverage constraint on the harvester**: there is no dedicated `test-eigensolver.cpp` under `palace/test/unit/` (see `eigensolver-wrapper` chapter §"Test coverage"). The future `L1/eigsolve` harvester will need to lean more heavily on direct source reading + literature anchors (Higham 2008, Lehoucq-Sorensen, Hernandez-Roman-Vidal) than `L1/ksp_solve` did (which had `test-orthog.cpp` as a direct algebra anchor), and the resulting algebraic equivalence claims will accordingly carry weaker test-linkage evidence. Routes to harvester (`L1/eigsolve`) once `L1/ksp_solve` settles. Source: `reports/2026-05-27T173523Z-layer-intro-author-L0-bootstrap-bundle-4/CYCLE.md` §Open questions item 1.

**Partially answered cycle-009**: Harvester dispatched at `reports/2026-05-27T191929Z-harvester-eigsolve-L1/`; landed `book/src/L1/eigsolve.md` as `rough-in (test-coverage-bounded, cycle-009)`. Pre-check confirmed no dedicated `test-eigensolver.cpp` exists; rough-in status motivated by narrow indirect coverage (`test-boundarymodeoperator.cpp` only — three `ModeEigenSolver` cases, linear path with `LARGEST_REAL` only). Full closure (promotion to `firm`) is gated on either (a) addition of dedicated test coverage or (b) a future harvester invocation that adds literature-anchored evidence at `ksp_solve`-equivalent confidence. The rough-in operator chapter introduces four follow-up OQs tracking specific rough-in axes: `eigsolve-linear-solve-failed-status-anchor`, `eigsolve-scaling-coordinate-convention`, `eigsolve-initial-space-axis-placement`, `eigsolve-iteration-count-result-field` (see below). Status held `partially-answered` rather than `answered` to keep the firm-promotion follow-up tracked.

```yaml
---
slug: matrix-weighted-norm-and-bilinear-form-l1-rough-ins
opened_at: cycle-008
opened_by: layer-intro-author
status: partially-answered
last_revisited: cycle-010
---
```

The new `linalg-operator-file` chapter notes that the `palace::linalg::` free functions `Norml2(comm, x, B, Bx)` and `Dot(comm, x, A, y)` are matrix-weighted variants of L1's existing `nrm2` and `dot` operators (weighted by an SPD `B` or bilinear-form `A`, respectively). They have not been harvested at L1. Candidate rough-in names: `L1/nrm2_weighted` and `L1/dot_bilinear`. The workspace-internal-allocation pattern in `Dot` (`palace/linalg/operator.cpp:621-639`) is Category 4 of `mutable-workspace-pattern` (synthetic workspace). `SpectralNorm` (`palace/linalg/operator.hpp:398-401`) is power iteration with configurable tolerance — also unharvested. Candidate rough-in name: `L1/power_iterate`. Sized smaller than `eigsolve` (single largest eigenvalue, no eigenvector recovery, no spectral transformation). Routes to cycle-009+ harvester / abstractor. Source: `reports/2026-05-27T173523Z-layer-intro-author-L0-bootstrap-bundle-4/CYCLE.md` §Open questions item 2.

**Partially answered cycle-010**: Harvester dispatched at `reports/2026-05-27T215334Z-harvester-matrix-weighted-norm-l1/`; landed `book/src/L1/matrix-weighted-norm.md` as `rough-in (test-coverage-bounded, cycle-010)` per priority #17 (lower-layer-shared-vocabulary-priority). The harvest covers the `Norml2(comm, x, B, Bx)` (matrix-weighted-norm) half of this OQ. **Residuals remaining open**: (a) the `Dot(comm, x, A, y)` bilinear-form sibling harvest (queued as `bilinear-form-l1-harvest`); (b) the `SpectralNorm` (power-iteration) sibling harvest; (c) the L1>L0 lowering theme `matrix-weighted-norm-mutation-rotation` (queued separately below). Status held `partially-answered` rather than `answered` to keep these residuals tracked.

**Further partially answered cycle-010**: Sibling harvester dispatched at `reports/2026-05-27T215427Z-harvester-bilinear-form-l1/`; landed `book/src/L1/bilinear-form.md` as `rough-in (lower-layer-shared-vocabulary, cycle-010)` per priority #17 (sibling dispatch to matrix-weighted-norm). The harvest covers the `Dot(comm, x, A, y)` (bilinear-form) half of this OQ — residual (a) above. The L1 form `bilinear_form(x, M, y) = xᴴ M y` is the matrix-weighted generalisation of `dot` for arbitrary linear `M` (no SPD requirement). Promotion-to-firm gate is narrow variant-axis coverage (two M-symmetry witnesses but no Cauchy–Schwarz tight case; real-vector case not surfaced by Palace). **Residuals remaining open after both wave-1 sibling landings**: (b) the `SpectralNorm` (power-iteration) sibling harvest; (c) the L1>L0 lowering theme `matrix-weighted-norm-mutation-rotation` (tracked separately as `matrix-weighted-norm-mutation-rotation-l1-l0-theme` below) and the analogous future `bilinear-form-mutation-rotation` L1>L0 theme. Status held `partially-answered` rather than `answered` to keep these residuals tracked.

```yaml
---
slug: l0-bundle-5-candidates
opened_at: cycle-008
opened_by: layer-intro-author
status: answered
answered_at: cycle-009
answered_in: reports/2026-05-27T192051Z-layer-intro-author-L0-bootstrap-bundle-5/
---
```

**Answered cycle-009**: Bundle 5 dispatched and landed 2 of 3 candidates (`mpi-globalsum-and-collectives` + `preconditioner-classes-overview`). `linalg-solver-file` and `tests-as-semantic-supplement` deferred to bundle 6; see `l0-bundle-6-candidates` and `tests-as-semantic-supplement-l0-vs-concepts-decision` below for follow-up tracking. L0 chapter count after bundle 5 is 16.


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

```yaml
---
slug: tests-as-semantic-supplement-l0-vs-concepts-decision
opened_at: cycle-009
opened_by: layer-intro-author
status: open
---
```

The cycle-008 bundle-5 candidate `tests-as-semantic-supplement` (see `l0-bundle-5-candidates` above) was deferred from cycle-009 bundle-5 pending a placement decision. The CLAUDE.md "Tests as semantic supplement" invariant is a **methodology convention** (`palace/test/unit/` is L0-equivalent semantic evidence) rather than a Palace-source convention; arguably it fits `book/src/concepts/` better than `book/src/L0/` (where existing convention chapters anchor Palace / MFEM idioms, not project methodology).

**Question**: Does `tests-as-semantic-supplement` belong in:

1. `book/src/L0/` as a convention chapter (alongside `output-arg-vs-receiver`, `mfem-vector-types`, `par-types-single-rank-reading`, `linalg-free-functions`, `transparent-vs-load-bearing-tricks`, `mutable-workspace-pattern`)?
2. `book/src/concepts/` as a methodology concept (alongside other cross-cutting methodology concepts)?
3. Only in `CLAUDE.md` / `scaffolding/test-linkages/` as already-established meta-instruction, not in the book at all?

The choice affects whether cycle-009+ L0 bundle 6 picks it up as an L0 chapter or whether it routes to a concepts/-bundle dispatch instead. Recommendation per source report: decide before any bundle-6 dispatch picks it up. Routes to cycle-010+ planner triage or to cycle-009 meta-phase. Source: `reports/2026-05-27T192051Z-layer-intro-author-L0-bootstrap-bundle-5/CYCLE.md` §Open questions / caveats §"`tests-as-semantic-supplement` deferred".

```yaml
---
slug: l0-bundle-6-candidates
opened_at: cycle-009
opened_by: layer-intro-author
status: partially-answered
partial_answer_at: cycle-011
---
```

After bundle 5 lands (cycle-009: `mpi-globalsum-and-collectives` + `preconditioner-classes-overview`), the L0 chapter count is **16**. Remaining bundle-6 candidates per the source report's bundle-6 ordering:

1. **`linalg-solver-file`** (highest priority per the original `l0-bundle-5-candidates` recommendation) — file-level overview of `palace/linalg/solver.{hpp,cpp}`, the home of `Solver<OperType>` base class and `MfemWrapperSolver` (already per-class-covered in `mfem-wrapper-solver`). Closes the file-overview gap on the four `linalg/` anchor files referenced by L1 (alongside `linalg-operator-file`, `linalg-iterative-file`, `linalg-vector-file`).
2. **`tests-as-semantic-supplement`** — pending the open question above (`tests-as-semantic-supplement-l0-vs-concepts-decision`) on whether to file as L0 convention or `concepts/` methodology concept.
3. **`mutable-workspace-pattern` Category-5 expansion** — if cycle-008+ work surfaces new workspace-pattern variants not covered by Categories 1-4 in the existing `mutable-workspace-pattern` chapter.

Bundle 6 would form with the same 2-chapters-per-cycle cadence. Routes to cycle-010+ planner. Source: `reports/2026-05-27T192051Z-layer-intro-author-L0-bootstrap-bundle-5/CYCLE.md` §Open questions / caveats §"Bundle 6 candidate ordering".

**Partial answer cycle-011 (layer-intro-author)**: Bundle-6 candidate #1 `linalg-solver-file` landed in cycle-011 wave-2 via `reports/2026-05-27T235650Z-layer-intro-author-l0-linalg-solver-file/`, bringing the L0 chapter count to **17**. The chapter adopts a corrected framing of `Solver<OperType>` as the type-axis root of ALL Palace solvers (preconditioners + iterative + MFEM-wrapped) rather than the dispatch-prompt's narrower "abstract base class for direct solvers" reading; the corrected framing is preserved in §Summary + §"What's not here" + the eight-subclass-family enumeration. The dispatch-prompt framing inaccuracy is **recurrence-2** since cycle-010 (eps.cpp/feast.cpp drift) — surfaced as a finalize STAGING signal for cycle-012 meta-phase methodology codification. Remaining bundle-6 items 2 + 3 still open: item 2 (`tests-as-semantic-supplement`) gated on `tests-as-semantic-supplement-l0-vs-concepts-decision` above; item 3 (`mutable-workspace-pattern` Category-5 expansion) gated on observed workspace-pattern variants. Status held `partially-answered` rather than `resolved` until items 2/3 dispatch or are explicitly dropped. Routes to cycle-012+ planner triage.

```yaml
---
slug: eigsolve-linear-solve-failed-status-anchor
opened_at: cycle-009
opened_by: harvester
status: partially-answered
partial_answer_at: cycle-010
partial_answer_in: reports/2026-05-27T220558Z-lifter-eigsolve-linear-solve-failed-anchor/
---
```

The cycle-009 `L1/eigsolve` rough-in chapter (`book/src/L1/eigsolve.md`) introduces a sum-typed `EigStatus = Converged | PartialConverged | MaxIterReached | LinearSolveFailed`. The first three cases correspond directly to L0 termination evidence at `palace/drivers/eigensolver.cpp:367-374` (the count-return + Mpi::Print pattern). The fourth case — `LinearSolveFailed` — is **constructively introduced by the L1 form and has no direct L0 anchor**: at L0, an inner-solver non-convergence is silent at the eigensolver level (the inner `ksp_solve` emits `Mpi::Warning` per `palace/linalg/ksp.cpp:301-307` but the eigensolver continues with the poorly-converged inverse). The Algebraic-laws §3 in the chapter flags this and §"Laws that explicitly do not hold" notes that treating the four-way `EigStatus` as exhaustive over L0 termination cases is "not a sound L0-grounded claim" until the L1>L0 lowering plumbs the case explicitly. Critic should consider whether to (a) drop the case (collapsing to `MaxIterReached`), (b) accept the constructive introduction with an explicit "constructed by the L1 form" annotation, or (c) require the L1>L0 lowering theme to plumb the case via a refactor of the inner-solver coupling. Harvester recommendation: keep the case but mark it `unconfirmed` until the L1>L0 lowering theme (a future `eigsolve-mutation-rotation` cycle) is harvested. Routes to critic / lifter / lowering-verifier review on the eigsolve rough-in entry, or to the future `eigsolve-mutation-rotation` L1>L0 dispatch (cycle-010+). Source: `reports/2026-05-27T191929Z-harvester-eigsolve-L1/CYCLE.md` §Open questions / caveats item 1.

**Resolved cycle-010 (lifter)**: Dispatched at `reports/2026-05-27T220558Z-lifter-eigsolve-linear-solve-failed-anchor/`. Adopted option (b) — keep the `LinearSolveFailed` variant in `EigStatus` and annotate it as **constructed by the L1 form** with explicit negative-anchor citations. The lifter dispatch verified that all ten eigensolver-side `opInv->Mult` call sites (4 ARPACK + 1 NLEPS + 5 SLEPc shell-matrix: `arpack.cpp:574, 580, 761, 778`; `nleps.cpp:514`; SLEPc shell callbacks at `slepc.cpp:1858, 1965, 1978, 2076, 2159`) invoke `BaseKspSolver<ComplexOperator>::Mult` (`palace/linalg/ksp.cpp:297-310`), which returns `void` and emits only `Mpi::Warning`, and that none of the call sites query `ksp->GetConverged()` after the call — confirming the inner-solver failure is silent at the eigensolver outer loop. The L1 form's `LinearSolveFailed` variant is therefore L1-constructive (introduced to make the inner-linear-solve coupling visible at the L1 surface for downstream L4 monadic-coordination consumers); materialisation defers to the future `eigsolve-mutation-rotation` L1>L0 theme (cycle-010+ abstractor candidate). The cycle-010 lifter applied four edits to `book/src/L1/eigsolve.md` (§Signature callout, §Algebraic-laws §3 row, §"Laws that explicitly do not hold" sum-type-completeness bullet, §Status block) and one evidence-section append. Status: resolved.

```yaml
---
slug: eigsolve-scaling-coordinate-convention
opened_at: cycle-009
opened_by: harvester
status: resolved
resolved_at: cycle-011
resolved_in: reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/
---
```

The cycle-009 `L1/eigsolve` rough-in chapter's Algebraic-law §5 flags two coherent conventions for handling `ScaleType::NORM_2`'s Higham-2008 scaling of `EigResult.eigenvalues`: (a) return scaled eigenvalues (matches L0 `EPSGetEigenvalue` raw return), expose `scaling_gamma` / `scaling_delta` for downstream un-scaling; or (b) un-scale at the L1 boundary, return original-coordinate eigenvalues, drop the `gamma` / `delta` fields. The L0 `GetEigenvalue` virtual already un-scales for SLEPc (`palace/linalg/slepc.cpp:715` returns `l * gamma`); the L0 convention is therefore inconsistent across orchestrations (ARPACK / SLEPc / `QuasiNewtonSolver`). The rough-in chapter adopts convention (a) but flags this for harvester / lifter review. The decision affects the coordinate system of every `EigResult.eigenvalues` consumed by L2 / L4 operators downstream, and aligns with the broader methodology question of where L1 should preserve L0's raw representation vs lift to an "intended caller" view. Routes to harvester / lifter review during firm-promotion. Source: `reports/2026-05-27T191929Z-harvester-eigsolve-L1/CYCLE.md` §Open questions / caveats item 2.

**Resolved cycle-011 (lifter)**: Dispatched at `reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/` (unified resolution of the 3-OQ cluster). Adopted convention (b) — the L1 form returns eigenvalues in the original-problem coordinate system, matching the L0 surface's un-scale-at-accessor convention across the EPS / PEP / NLEPS backends. Direct evidence: ARPACK at `palace/linalg/arpack.cpp:387` (`eig[i] = eig[i] * gamma` inside `SolveInternal` post-`neupd`); SLEPc-EPS at `palace/linalg/slepc.cpp:711-716` (`GetEigenvalue` returns `l * gamma`); SLEPc-PEP at `palace/linalg/slepc.cpp:1194-1203` (same `l * gamma`); NLEPS at `palace/linalg/nleps.cpp:88-93` (returns stored already-un-scaled eigenvalues from linear-eigensolver priming). SLEPc-NEP at `palace/linalg/slepc.cpp:1554-1560` returns `l` directly without applying `* gamma` — the SLEPc-NEP backend manages its own coordinate handling separately from the EPS / PEP un-scale-at-accessor pattern. (Note: `SlepcNEPSolver::SetOperators` at `palace/linalg/slepc.cpp:1645-1651` and `:1711-1719` DOES compute a non-trivial `gamma = std::sqrt(normK / normM)` when `type != ScaleType::NONE`, so the simpler "no Higham scaling for NEP" reading would be wrong; the precise un-scaling convention for the SLEPc-NEP backend is flagged for follow-up audit, but this detail does not affect the broader resolution — the un-scale-at-accessor pattern holds uniformly across EPS / PEP / NLEPS, which is what the L1 form mirrors.) The cycle-009 rough-in chapter's Algebraic-law §5 stated the opposite (incorrectly: "L1 returns scaled"); the cycle-011 lifter rewrites §5 to match L0. The `scaling_gamma` / `scaling_delta` fields remain in `EigResult` as informational (record the operator-norm-derived factors used internally; downstream consumers can inspect operator conditioning or recover residual-in-scaled-coords for diagnostics, but the eigenvalues field is itself in original-problem coordinates). Status: resolved (SLEPc-NEP coordinate-convention detail flagged for follow-up audit as a separate OQ).

```yaml
---
slug: eigsolve-initial-space-axis-placement
opened_at: cycle-009
opened_by: harvester
status: resolved
resolved_at: cycle-011
resolved_in: reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/
---
```

The cycle-009 `L1/eigsolve` rough-in chapter places the `initial_space` field in `EigControl` (per-call), but the L0 `SetInitialSpace` virtual (`palace/linalg/eps.hpp:122`) is a method on the eigensolver value (so construction-bound). The call pattern at `palace/models/modeeigensolver.cpp:472-475` shows the driver setting `initial_space` per `Solve()` invocation (`if (initial_space) eigen->SetInitialSpace(*initial_space);`); the rough-in chapter argues this supports per-call placement. The alternative interpretation is that `initial_space` is a construction parameter the driver re-binds at solve time — both are coherent under the L0 surface. The choice affects whether `EigSolver[problem]` (the opaque construction-bound type) carries `initial_space` or not, and the L2 `eigenmode-pipeline` composition shape downstream. Routes to lifter / lowering-verifier review during firm-promotion. Source: `reports/2026-05-27T191929Z-harvester-eigsolve-L1/CYCLE.md` §Open questions / caveats item 3.

**Resolved cycle-011 (lifter)**: Dispatched at `reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/` (unified resolution of the 3-OQ cluster). Keep `initial_space` in `EigControl` (per-call control); the current rough-in placement is correct. Direct evidence: `SetInitialSpace(const ComplexVector &v)` is a *method* on `EigenvalueSolver` (`palace/linalg/eps.hpp:122`) separate from `SetOperators` / construction, and is invoked between `SetOperators` and `Solve()` at both observed call sites — `palace/drivers/eigensolver.cpp:264` (conditional on user-supplied vs random initial vector) and `palace/models/modeeigensolver.cpp:474` (conditional on the `initial_space` argument to `ModeEigenSolver::Solve()`, which is a re-callable per-call function). The ordering invariant is `SetOperators` first (allocates the per-backend workspace; ARPACK `MFEM_VERIFY(n > 0, ...)` at `palace/linalg/arpack.cpp:253` rejects pre-`SetOperators` invocation; SLEPc analogue at `palace/linalg/slepc.cpp:659-661`), then optional `SetInitialSpace`, then `Solve()`. The construction-side prerequisite is documented at L1 as a precondition on `E`'s opaque type (operators are construction-bound; `initial_space` in `control` is well-defined only against an `E` whose operators are bound) rather than as an axis decision. Status: resolved.

```yaml
---
slug: eigsolve-iteration-count-result-field
opened_at: cycle-009
opened_by: harvester
status: resolved
resolved_at: cycle-011
resolved_in: reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/
---
```

The cycle-009 `L1/eigsolve` rough-in chapter's `EigResult` does not currently carry an `iterations` field (unlike `ksp_solve`'s `SolveResult.iterations`). The L0 `EigenvalueSolver` interface does not expose a per-call iteration count — only the converged eigenpair count (via the `Solve() → int` return). Adding `iterations` to the L1 form would be constructive (similar to `EigStatus::LinearSolveFailed`); the question is whether downstream consumers (e.g., the L2 `eigenmode-pipeline` operator, the L4 monadic composition) need it. The chapter leaves it out for now; harvester promotion to firm should re-evaluate based on downstream demand. Routes to harvester re-evaluation during firm-promotion (cycle-010+); may also surface during L2 `eigenmode-pipeline` harvest as a feedback signal. Source: `reports/2026-05-27T191929Z-harvester-eigsolve-L1/CYCLE.md` §Open questions / caveats item 4.

**Resolved cycle-011 (lifter)**: Dispatched at `reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/` (unified resolution of the 3-OQ cluster). Adopted the cycle-010 `LinearSolveFailed` precedent (option (b)) — add the `iterations : Int` field to `EigResult` with an L1-constructive annotation. Direct evidence: the `EigenvalueSolver` virtual surface (`palace/linalg/eps.hpp:124-140`) does not expose an iteration-count accessor; ARPACK has `iparam[2]` consumed at `palace/linalg/arpack.cpp:342, 350` (printed only, never stored where a caller can retrieve); SLEPc has `EPSGetIterationNumber` / `PEPGetIterationNumber` / `NEPGetIterationNumber` available in the PETSc API but Palace never calls them (zero occurrences across the `palace/` source tree per `mcp__palace-codemap__search_text`); NLEPS's `QuasiNewtonSolver::Solve` has internal Newton-iteration counters at `palace/linalg/nleps.cpp:351-805`, also not exposed. The field is added as L1-constructive (parallel to `EigStatus::LinearSolveFailed` cycle-010) — it pre-positions the iteration-count for downstream L4 monadic-coordination consumers; materialisation defers to the cycle-011 wave-1 `eigsolve-mutation-rotation` L1>L0 theme (Sub-pattern C of `reports/2026-05-27T234730Z-abstractor-eigsolve-mutation-rotation-l1-l0/CYCLE.md`), which would either add a `GetIterations()` virtual + per-backend accessor implementations, or plumb the count through the existing print-side flow. The Algebraic-laws §"Strict positive-iteration termination" non-law bullet is tightened to acknowledge the field is now part of the record but may yield a sentinel value under current L0 instantiations. Status: resolved.

```yaml
---
slug: nleps-spec-gap-as-check-stop-into-carry-reuse-blocker
opened_at: cycle-009
opened_by: combinator-miner
status: open
last_revisited: cycle-010
---
```

The cycle-008 abstractor's promotion criterion for the speculative L4 helper `check_stop_into_carry` (sketched in `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` §Speculative L4 operators) is **"defer until a second slice needs it"** (sourced from `reports/2026-05-27T180000Z-abstractor-gmres-inner-loop-iterate-while-migration/CYCLE.md:71`; also tracked at `iterate-while-l4-l3-gmres-inner-loop-migration` lineage above). The cycle-009 combinator-miner survey (`reports/2026-05-27T192047Z-combinator-miner-check-stop-into-carry-reuse/CYCLE.md`) verified that the **NLEPS Quasi-Newton inner loop** at `reference/palace/palace/linalg/nleps.cpp:589-647` has the same 3-condition stop shape (different `StopReason` set `{Converged, Diverged, MaxIt}` but identical hoist-into-carry structure), and is therefore **the natural second consumer** — but NLEPS has no `book/src/spec/slices/nleps.md` chapter; only L1>L0 mutation-rotation citations at `book/src/L1-L0/axpbypcz-mutation-rotation.md:127-132,294-297`, `book/src/L1-L0/apply-linop-mutation-rotation.md:337`, and `book/src/L1-L0/axpby-mutation-rotation.md:213` reference it. NLEPS is a **non-linear eigenvalue problem driver** (sibling-tier to GMRES, not a sub-component); promoting it to L1+ is a multi-cycle effort (`nleps.cpp` is 952 lines including deflation, Armijo backtracking, line search, and line-search Jacobian construction). This OQ records the dependency: `check_stop_into_carry` helper promotion is blocked on NLEPS being spec'd at L1+ as a separate slice; if NLEPS lands and its inner-loop migration adopts the same hoist pattern, promote the helper at that point. Routes to whichever cycle picks up NLEPS as a harvester target (likely cycle-010+ if eigenmode work prioritizes), with `check_stop_into_carry` promotion as a downstream consequence. Source: `reports/2026-05-27T192047Z-combinator-miner-check-stop-into-carry-reuse/CYCLE.md` §Open questions / caveats item 1.

**Cycle-010 revisit** (`reports/2026-05-27T215535Z-combinator-miner-check-stop-into-carry-mcp-pilot/CYCLE.md`): The MCP-codemap-pilot retry of the `check_stop_into_carry` reuse audit produced a **defer-with-routing** verdict — **GMRES + FGMRES sister-algorithm match found** as a structurally-identical 3-condition twin (`palace/linalg/iterative.cpp:644-649` ↔ `:823-828`, textually identical disjunct). The cycle-010 audit characterizes this as **"the lower edge"** of the second-reuse criterion: both call sites are inside `GmresSolverBase`-shaped iteration in the same translation unit on a single solver-family pair (FGMRES is "GMRES with right-preconditioning allowed to vary per iteration"), so the structural population that would stress the helper's signature in a *new* dimension is unchanged. The cycle-009 verdict (NLEPS is the natural second consumer; the FGMRES twin is variant-absorbed and doesn't count as second-slice under reading (a)) is **refined but not overturned**: the FGMRES twin is acknowledged as a sister-algorithm match (lower-edge reading (b)), but the strong-reuse evidence (a non-`GmresSolverBase` Krylov consumer) the cycle-009 OQ was waiting for is still absent. The cycle-010 audit's recommendation is to **route a lifter dispatch on FGMRES inner-loop migration** in cycle-011 (tracked separately under `fgmres-inner-loop-iterate-while-migration-lifter-candidate`) — this is the pre-formalization step that would verify whether GMRES and FGMRES lower to the same `check_stop_into_carry` callsite shape (if yes, that is the second-reuse formalization; if no, the helper's signature needs revision before promotion). Status held `open` because the cycle-009 NLEPS-dependency framing is still the right blocker for *firm* L4 promotion; the FGMRES route is a pre-promotion validation step, not the second-consumer the OQ describes. Cross-reference: cycle-010 audit also confirmed (independently) the related cycle-009 OQ `variant-absorption-vs-instance-counting-policy` (line 1546) — adopting reading (a) for cycle-009 + reading (b)-lower-edge for cycle-010 is internally consistent and now has two cycles of corroborating evidence for the meta-phase batch-2 codification.

```yaml
---
slug: check-stop-into-carry-parameterization-over-stop-condition
opened_at: cycle-009
opened_by: combinator-miner
status: open
---
```

If `check_stop_into_carry` is eventually promoted (per the NLEPS-spec-gap OQ above), an open design question is whether the helper signature should be the cycle-008-sketched monomorphic shape (`OpParams -> Convergence -> Krylov -> int -> Krylov`, with GMRES-specific `StopReason` baked in) or a parameterised shape (`[StopCondition reason carry] -> OpParams -> Convergence -> Krylov -> int -> Krylov where StopCondition reason carry = (Predicate, Constructor)`) that absorbs the GMRES `{Conv, MaxDim, MaxIt}` and NLEPS `{Converged, Diverged, MaxIt}` reason sets uniformly. The combinator-miner survey's recommendation is that **the parameterised form is over-engineered for a single current call site** — the monomorphic form is appropriate for the rough-in stage, and the parameterised form should be considered *after* the second consumer (NLEPS) lands and shows whether the reason-sum factoring is worth the additional vocabulary. The factoring trade-off mirrors the broader L4 question of when a sum-type parameter should be hoisted into a list-of-condition-handlers vs kept as a closed enumeration. Routes to combinator-miner or lifter dispatch at the time of `check_stop_into_carry` promotion (gated on the NLEPS spec gap above). Source: `reports/2026-05-27T192047Z-combinator-miner-check-stop-into-carry-reuse/CYCLE.md` §Open questions / caveats item 2.

```yaml
---
slug: variant-absorption-vs-instance-counting-policy
opened_at: cycle-009
opened_by: combinator-miner
status: open
---
```

The cycle-008 promotion criterion **"a second slice needs it"** is ambiguous when one L1+ slice absorbs two Palace-source call sites via a variant axis. The cycle-009 `check_stop_into_carry` survey encountered this directly: GMRES and FGMRES are two distinct Palace-source call sites (`reference/palace/palace/linalg/iterative.cpp:615-650` and `:794-828`, textually-identical 3-condition breaks at lines 645 and 824) but are absorbed into the single `book/src/spec/slices/gmres.md` slice via the `op.flexible` variant axis (`gmres.md:3,91,122`). Three coherent readings of "second slice needs it" are: **(a)** distinct L1+ slices (strictest reading — 1 instance for `check_stop_into_carry`); **(b)** distinct Palace-source call sites (2 instances — FGMRES would count as second, immediate promotion); **(c)** distinct algorithmic variants observed in the corpus (2-3 instances depending on whether CG's degenerate 2-condition form is counted). The cycle-009 survey adopted reading (a) to avoid premature promotion, on the basis that reading (b) would suggest the cycle-008 theme should split into two themes (which seems wrong since the theme correctly covers GMRES and FGMRES uniformly via the same `op.flexible` axis). This is a **cross-cutter / meta-phase question**, not a combinator-miner question — the policy should be codified once and applied uniformly to every speculative-combinator promotion criterion that uses "second slice" language. Routes to meta-phase (cycle-009 batch-1 aggregation or later) for explicit codification in the friction-ledger or a methodology-conventions skill. Source: `reports/2026-05-27T192047Z-combinator-miner-check-stop-into-carry-reuse/CYCLE.md` §Open questions / caveats item 3.

```yaml
---
slug: iterate-while-witness-alternative-combinator-design
opened_at: cycle-009
opened_by: combinator-miner
status: open
---
```

The cycle-008 `gmres-inner-loop-iterate-while-migration` theme briefly named option (b) `iterate_while_with_stop_witness` as an alternative-combinator approach to the witness-into-carry hoist (avoiding `check_stop_into_carry` entirely). If `iterate-while` itself were extended to support a witness-carrying variant — `iterate_while_witness :: α -> (α -> Maybe StopReason) -> (α -> Solve { state: α, ...e }) -> Solve { final_state, trajectory, stop: Maybe StopReason }` — the helper would become unnecessary: the predicate would return `Maybe StopReason` directly, the witness would live in the combinator's return rather than the carry, and the hoist would dissolve into the combinator's signature. This is a **separate combinator-miner pattern** (a new L4 row, not a helper inside an existing theme), not the same one the cycle-009 dispatch is about. The choice between `check_stop_into_carry` (helper) and `iterate_while_witness` (extended combinator) is the abstraction-level question the cycle-008 theme's option (b) flagged. Note that the L4 calculus already has multiple iterate-while variants (`iterate_while`, `iterate_while_with_prev`, `iterate_while_pure`), so adding a fourth is not architecturally novel — it would just slot into the existing dep-map. Routes to lifter / combinator-miner dispatch that addresses the witness-vs-carry design choice, likely concurrent with the NLEPS promotion (since the same architectural question affects how NLEPS's stop test would lower). Source: `reports/2026-05-27T192047Z-combinator-miner-check-stop-into-carry-reuse/CYCLE.md` §Open questions / caveats item 4.

```yaml
---
slug: standalone-iterate-while-l4-l3-theme-pending
opened_at: cycle-009
opened_by: combinator-miner
status: open
relates_to: iterate-while-l3-rendering-trajectory-accumulation-gap (cycle-006, closed cycle-008 via lifter on krylov-step-typed-wrapper-dissolution)
---
```

No standalone `book/src/L4-L3/iterate-while-dissolution.md` theme exists yet — the cycle-007 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` was closed in cycle-008 by an inline patch to the `krylov-step-typed-wrapper-dissolution` theme (Condition 5 + Law 1 citation + `verified_against:` block), rather than by authoring a dedicated standalone L4>L3 theme for `iterate-while`. As a consequence, the `iterate-while`-specific L3 rendering (`Solve`-dissolved + trajectory-pruned single-readout form) currently lives inside the krylov-step typed-wrapper-dissolution theme and is repeated by reference in the cycle-008 `gmres-inner-loop-iterate-while-migration` theme. The cycle-009 combinator-miner survey of `check_stop_into_carry` pinned the helper's L3 form to the cycle-008 GMRES-specific theme's §"L3 form" section as a consequence. **Not a blocker** for the cycle-009 defer verdict on `check_stop_into_carry`, but flagging for completeness: if a future cycle promotes `iterate_while_witness` (per the OQ above) or otherwise authors more `iterate-while`-using L4>L3 themes, the standalone dissolution theme may become worth authoring as an extraction-of-shared-language to avoid per-theme repetition of the trajectory-pruning rule. Routes to abstractor or lifter dispatch when the second `iterate-while`-using theme lands. Source: `reports/2026-05-27T192047Z-combinator-miner-check-stop-into-carry-reuse/CYCLE.md` §Open questions / caveats item 5.

```yaml
---
slug: combinator-miner-authority-defer-verdict-status-edit-scope
opened_at: cycle-009
opened_by: combinator-miner
status: open
---
```

The cycle-009 combinator-miner dispatch on `check_stop_into_carry` produced a `defer` verdict (no new L4 dep-map row, no firm-promotion). The original CYCLE.md draft included a candidate append-only edit to the cycle-008 theme file's §Status block to record the survey outcome inside the theme — but on reflection (and confirmed by the cycle-009 critic + repairer), this edit is **technically outside the combinator-miner's stated authority** (the role spec scopes the agent to "just the dep-map entry"). The repaired CYCLE.md §Proposed changes section now carries zero proposed-changes blocks (consistent with the `defer` verdict) and names two natural channels for any future incorporation of the survey outcome into the theme file: (a) an OQ entry referencing the cycle-009 combinator-miner report (this OQ), or (b) a lifter or abstractor dispatch on the cycle-008 theme that re-authors §Status to incorporate the criterion-and-survey-result inline. This OQ flags a broader **authority-scope question for the combinator-miner role**: when a `defer` verdict is produced, should the agent be permitted to author a §Status-block update on the relevant upstream theme as part of the verdict, or should every such update be routed via OQ to a follow-up dispatch (the current strict reading)? The strict reading preserves clean role boundaries but creates a paperwork tax (every defer becomes an OQ); the relaxed reading is more efficient but blurs role authority. Routes to meta-phase (cycle-009 batch-1 aggregation) for explicit codification — likely a small role-spec edit one way or the other. Source: `reports/2026-05-27T192047Z-combinator-miner-check-stop-into-carry-reuse/CYCLE.md` §Open questions / caveats item 6.

```yaml
---
slug: l3-backfill-apply-linop-and-blas1-cohort
opened_at: cycle-010
opened_by: cross-layer-cross-cutter
status: open
relates_to: priority-20-identity-lowering-both-levels-backfill (priorities.md), l3-vocabulary-inventory-gap (this ledger)
---
```

The cycle-010 identity-in-form audit (`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`) surfaced **two HIGH CONFIDENCE L3 backfill candidates** beyond the wave-1 `L3/krylov-step.md` dispatch: **(1) `book/src/L3/apply_linop.md`** as a standalone harvester dispatch, and **(2) the 6-entry BLAS-1 cohort** (`L3/axpy.md`, `L3/dot.md`, `L3/nrm2.md`, `L3/axpby.md`, `L3/axpbypcz.md`, `L3/scal.md`) as a bundled multi-dispatch sequence. Structural rationale: both the L4-L3 typed-wrapper-dissolution theme (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:64-68`) and the L3-L2 body-identity theme (`book/src/L3-L2/krylov-step-body-identity.md:30, 97`) reference these primitives as L3-native by signature shape (whole-tensor / reduction, no element loop exposed). The L3 index (`book/src/L3/index.md:11-14`) already advertises `matvec, axpy, dot, nrm2` as L3 vocabulary but currently no L3 entries exist for them. The rotation L3→L1 is identity-in-form on the primitive's signature; only the stratum-typing-vs-positional surface differs. Suggested bundling: (a) axpy + axpby + axpbypcz (linear-update family), (b) dot + nrm2 (reduction family; nrm2 depends on dot), (c) scal (standalone leaf). Each dispatch follows the wave-1 `L3/krylov-step.md` precedent. **Routes to cycle-011+ planner** for harvester dispatch scheduling (priority #20 second target enactment); audit explicitly recommends `dispatch-harvester-cycle-010-or-011`. Source: `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"Per-candidate verdict" items (1)-(2) + §Recommendation `proposed_changes` blocks 1-2.

```yaml
---
slug: ksp-solve-l2-promotion-non-identity-substantive-gap
opened_at: cycle-010
opened_by: cross-layer-cross-cutter
status: open
relates_to: priority-20-identity-lowering-both-levels-backfill (out-of-scope-for-priority-20)
---
```

The cycle-010 identity-in-form audit surfaced **one MEDIUM CONFIDENCE candidate** that is real coverage gap but **out-of-priority-20-scope**: `book/src/L2/ksp_solve.md` would carry the outer-driver framing (`solve_loop` + `restart_cycle` folding `krylov-step` via an iteration combinator, threading SolveResult statistics) around the L2 `krylov-step` entry. The rotation L2→L1 is **NOT identity-in-form** — at L2 the per-method body is unfolded into an explicit krylov-step fold; at L1 the body is opaque inside `Solver[A]`. Per `book/src/L1/ksp_solve.md:81`: "the L2 `krylov-step` operator is the layer at which they become direct dependencies". This means a missing L2 row would carry substantive content (the outer-loop framing), so this is a real coverage gap, but it would be a **fresh harvester dispatch with new algebraic content, not a mechanical backfill**. Priority #20 explicitly targets identity-in-form backfills; this candidate is out of scope. **Routes to cycle-010+ planner for separate priority consideration** ("ksp_solve L2/L4 promotion" as a distinct priority from the priority #20 identity-in-form sweep). The L3 and L4 candidates for `ksp_solve` similarly defer (L4 would be the typed-wrapper Solve-monad driver; L3 form is value-threaded version of L4 driver; both depend on the L2 form being authored first). Source: `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"Per-candidate verdict" item (3) + §Recommendation `NOT-priority-20-but-real-coverage-gap` block.

```yaml
---
slug: l3-l1-directory-naming-structure-policy
opened_at: cycle-010
opened_by: cross-layer-cross-cutter
status: open
last_revisited: cycle-011
relates_to: l3-backfill-apply-linop-and-blas1-cohort (this ledger), identity-lowerings-still-require-both-l-levels (CLAUDE.md §Methodology invariants)
---
```

The cycle-010 identity-in-form audit flagged a **policy question for the cycle-010+ layer-intro-author / cycle-planner**: should each L3 backfill entry (per the `l3-backfill-apply-linop-and-blas1-cohort` OQ) come with a sibling **thin identity-in-form L3-L1 theme** (analogous to `L3-L2/krylov-step-body-identity.md`) documenting the no-op rotation, OR should the identity rotation be **captured in-line at the L3 entry itself**? **`book/src/L3-L1/` does not currently exist** (confirmed by critic via directory listing); existing lowering-layer directories are `L1-L0/`, `L2-L1/`, `L3-L2/`, `L4-L3/`. Either approach is consistent with the methodology invariant "Identity-lowerings still require both L levels" — the question is one of artifact navigation and structural consistency. The wave-1 sibling dispatch on `L3/krylov-step.md` did NOT create an `L3-L1/` directory (the L3 krylov-step entry's lowering is `L3-L2` to the L2 entry, not `L3-L1` directly — krylov-step is a composition that lives at L2/L3/L4, not L1). The L3 backfill candidates for primitives (apply_linop, BLAS-1 cohort) are a different case: their lowering chain skips L2 (they are primitives, not compositions) and lands directly at L1, making the L3>L1 hop the relevant one. **Routes to cycle-011+ planner** to decide a default before dispatching the L3 backfill harvesters. A small `layer-intro-author` role-spec edit may codify the policy. Source: `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"Open questions / caveats" item 1.

**Cycle-011 partial-precedent update**: the cycle-011 wave-1 harvester dispatch on `book/src/L3/apply_linop.md` (the first primitive-flavored L3 backfill — krylov-step is a composition, not a primitive) **chose the in-line option** — the §"Lowers to" section captures the identity rotation textually; no `L3-L1/apply-linop-identity` theme directory was created. Rationale recorded in the dispatch CYCLE.md §"Open questions / caveats" item 1: (a) creating an `L3-L1/` directory for a single identity rotation would be over-structuring; (b) the in-line treatment makes the layer-coherence argument visible to a reader at the L3 entry without requiring navigation; (c) the wave-1 sibling for `krylov-step` lowers via L3-L2, not L3-L1, so there is no exact precedent yet. **Status remains `open`** because the BLAS-1 bundle (the other HIGH CONFIDENCE backfill candidate per the sibling OQ `l3-backfill-apply-linop-and-blas1-cohort`) may also lower identity-in-form to L1; if 6 in-line identity-rotation sections accumulate across the cohort, the in-line option may become redundant and a thin `L3-L1/` directory may become preferable. Routing note for cycle-012+ planner: revisit this policy after the BLAS-1 cohort lands. Source: cycle-011 harvester dispatch `reports/2026-05-27T234502Z-harvester-l3-apply-linop/CYCLE.md` §"Open questions / caveats" item 1.

**Cycle-011 BLAS-1 cohort partial-precedent update**: the cycle-011 wave-1 cohort-bundle dispatch on `book/src/L3/axpy.md` + `book/src/L3/axpby.md` + `book/src/L3/axpbypcz.md` (the BLAS-1 linear-update cohort — three of the six BLAS-1 candidates) **also chose the in-line option** — each entry's §"Lowers to" section captures the identity rotation textually; no `L3-L1/<op>-identity` theme directory was created. Rationale (consistent with the apply_linop dispatch): mirror the cycle-010 `book/src/L3/krylov-step.md` precedent which handled its lowering in-line, avoid over-structuring for identity rotations, keep the layer-coherence argument visible at the L3 entry. **Cumulative in-line identity-rotation count now stands at 4** (apply_linop, axpy, axpby, axpbypcz) — the OQ's revisit-trigger threshold ("if 6 in-line identity-rotation sections accumulate, a thin `L3-L1/` directory may become preferable") is now 2/3 of the way reached after this cohort. Sibling wave-1 dispatches (#3 `dot` + `nrm2`, #4 `scal`) land the remaining three cohort candidates this cycle; if all three siblings also choose the in-line option, the cumulative count will reach 7 and the revisit will trigger. **Routing note for cycle-012+ planner**: after wave-1 closure, audit the cumulative in-line treatment and decide whether to create a thin `book/src/L3-L1/` directory retroactively, OR codify the in-line convention as the long-term default. Source: cycle-011 harvester dispatch `reports/2026-05-27T234525Z-harvester-l3-blas1-linear-update-cohort/CYCLE.md` §"Open questions / caveats" item 1.

**Cycle-011 BLAS-1 reduction-cohort partial-precedent update**: the cycle-011 wave-1 cohort-bundle dispatch on `book/src/L3/dot.md` + `book/src/L3/nrm2.md` (the BLAS-1 reduction cohort — two of the six BLAS-1 candidates) **also chose the in-line option** — each entry's §"Lowers to" section captures the identity rotation textually; no `L3-L1/<op>-identity` theme directory was created. Rationale identical to the linear-update cohort precedent (mirror cycle-010 `krylov-step` precedent; avoid over-structuring; preserve layer-coherence visibility). **Cumulative in-line identity-rotation count now stands at 6** (apply_linop, axpy, axpby, axpbypcz, dot, nrm2) — the OQ's revisit-trigger threshold ("if 6 in-line identity-rotation sections accumulate, a thin `L3-L1/` directory may become preferable") **is now reached**. One remaining wave-1 sibling dispatch (#4 `scal`) is pending; if `scal` also chooses the in-line option, the cumulative count will reach 7 and the revisit becomes mandatory. The report also surfaces a related sub-question (originally proposed as a new OQ slug `l3-l1-identity-in-form-annotation-policy-formalization`): formalize the in-line vs. dedicated-`L3-L1/`-theme policy as a long-term convention rather than per-cohort precedent. Merged here per the integrator-per-report's policy-merge discretion: the two questions are not separable (the directory-naming-structure question IS the annotation-policy question viewed from the structural side). **Routing note for cycle-012+ planner (urgency upgrade)**: with the cumulative in-line count at the revisit threshold, the cycle-012 meta-phase should treat this OQ as a candidate for closure — either by codifying the in-line convention via a layer-intro-author role-spec edit, or by retroactively introducing a thin `book/src/L3-L1/` directory and back-filling identity-rotation themes. Source: cycle-011 harvester dispatch `reports/2026-05-27T231500Z-harvester-l3-blas1-reduction-cohort/CYCLE.md` §"Open questions / caveats" items 1 + 4.

**Cycle-011 BLAS-1 cohort CLOSURE update (`scal` landing)**: the final cycle-011 wave-1 cohort-bundle dispatch on `book/src/L3/scal.md` (closing the 7-entry BLAS-1 backfill cluster: apply_linop + axpy + axpby + axpbypcz + dot + nrm2 + scal) **also chose the in-line option** — the §"Lowers to" section captures the identity rotation textually; no `L3-L1/scal-identity` theme directory was created. Rationale identical to the prior cohort precedents (mirror cycle-010 `krylov-step` precedent; avoid over-structuring; preserve layer-coherence visibility). **Cumulative in-line identity-rotation count now stands at 7** (apply_linop, axpy, axpby, axpbypcz, dot, nrm2, scal) — **exceeds the OQ's revisit-trigger threshold of 6**. The BLAS-1 cohort closure marks the natural decision point: every primitive-flavored L3 backfill from the cycle-010 audit's HIGH CONFIDENCE recommendations has now chosen the in-line option, establishing a 7-entry uniform precedent. **Routing note for cycle-012 meta-phase (urgency upgrade further)**: this OQ is now a **strong candidate for closure** — codify the in-line convention as the long-term L3>L1 identity-rotation policy via a `layer-intro-author` role-spec edit, OR retroactively introduce a thin `book/src/L3-L1/` directory and back-fill identity-rotation themes (which would mean back-rendering 7 in-line annotations into thin theme files, a non-trivial migration). The simpler path (codify the in-line convention) is the recommended default per the cohort's empirical convergence. Source: cycle-011 harvester dispatch `reports/2026-05-27T234540Z-harvester-l3-scal/CYCLE.md` §"Open questions / caveats" item 1.

```yaml
---
slug: l3-vocabulary-inventory-gap
opened_at: cycle-010
opened_by: cross-layer-cross-cutter
status: open
relates_to: l3-backfill-apply-linop-and-blas1-cohort (this ledger), lower-level-shared-vocabulary-takes-priority (CLAUDE.md §Methodology invariants), priority-17-lower-layer-shared-vocabulary-priority (priorities.md)
---
```

**Latent pattern observation** flagged by the cycle-010 identity-in-form audit: the L3 index (`book/src/L3/index.md:11-14`) advertises whole-tensor primitives (`matvec, axpy, dot, nrm2` as field operations) as L3 vocabulary, but the L3 directory currently contains only `index.md` + (post-wave-1) `krylov-step.md`. Under the methodology invariant **"Identity-lowerings still require both L levels"** (CLAUDE.md, mid-cycle-009), every primitive the L3 index advertises as an L3 field operation should have a corresponding L3 entry, even if the rotation L3→L1 is identity-in-form. The audit's two HIGH CONFIDENCE backfill candidates (apply_linop + 6-entry BLAS-1 cohort, per the `l3-backfill-apply-linop-and-blas1-cohort` OQ) are instances of this broader pattern, but the pattern may extend further as L2/L3/L4 vocabulary grows (e.g., `gemv`, `trsv` if they become firm L1 primitives; the L2 index at `book/src/L2/index.md:17` advertises "axpy, dot, matvec, gemv, trsv, scal, nrm2" — at least gemv/trsv are not yet firm at L1). **Routes to cycle-011+ planner as evidence supporting the broader L3 cohort growth that priority #17 already targets**; the two HIGH CONFIDENCE candidates are the next concrete realization of that policy, but additional cross-layer-cross-cutter audits in subsequent cycles should track the broader gap as more L1 primitives firm up. Source: `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"Latent observation: L3 vocabulary inventory gap" + §Recommendation `latent-pattern-observation` block.

```yaml
---
slug: matrix-weighted-norm-naming-sweep
opened_at: cycle-010
opened_by: harvester
status: open
relates_to: matrix-weighted-norm-and-bilinear-form-l1-rough-ins (this ledger)
---
```

The cycle-010 `matrix-weighted-norm` harvest resolved the canonical L1 slug as `matrix-weighted-norm` per planner directive, but candidate-name residue persists across artifacts. The L0 chapter `book/src/L0/linalg-operator-file.md` (cycle-008) uses `nrm2_weighted` at lines 30-33, 73, 88 as the candidate L1 name; the cycle-008 OQ slug uses `matrix-weighted-norm`; the L1 `index.md` previously used `nrm2_B` in the Queued section (now superseded as of this cycle-010 integration). The L0 chapter is informational on L1 naming (not authoritative), so the misnomer is not blocking, but a future cross-layer cross-cutter sweep should swap the `nrm2_weighted` references in `book/src/L0/linalg-operator-file.md:30-33, 73, 88` for `matrix-weighted-norm` to align. Routes to a future cross-layer-cross-cutter dispatch. Source: `reports/2026-05-27T215334Z-harvester-matrix-weighted-norm-l1/CYCLE.md` §Open questions item 1.

```yaml
---
slug: matrix-weighted-norm-mixed-element-type-variant
opened_at: cycle-010
opened_by: harvester
status: open
relates_to: matrix-weighted-norm-and-bilinear-form-l1-rough-ins (this ledger), apply_linop firm L1 entry (variant-axis precedent)
---
```

The L0 complex specialization of `linalg::Norml2(comm, x, B, Bx)` decomposes `B.Mult(x.Real(), Bx.Real()); B.Mult(x.Imag(), Bx.Imag())` because `B : Operator` is real-valued even when `x` is complex (`palace/linalg/operator.cpp:613-614`). At L1 the cycle-010 rough-in absorbs this into `apply_linop`'s element-type variant axis (per cycle-008's `apply_linop` precedent: the L1 form collapses across operator element-type). But the question remains: should L1 admit the **real-`B`-applied-to-complex-`x`** specialization as a distinct element-type sub-variant — or absorb it uniformly? The SPD precondition interacts with `B`'s element-type non-trivially. This is a firm-promotion gate question: clarifying the variant-axis profile is part of (c) algebraic-law completeness verification. Routes to either a follow-up `matrix-weighted-norm` harvester invocation or a `same-layer-cross-cutter` sweep audit on element-type-variant policy. Source: `reports/2026-05-27T215334Z-harvester-matrix-weighted-norm-l1/CYCLE.md` §Open questions item 2.

```yaml
---
slug: matrix-weighted-norm-mutation-rotation-l1-l0-theme
opened_at: cycle-010
opened_by: harvester
status: open
relates_to: matrix-weighted-norm-and-bilinear-form-l1-rough-ins (this ledger), apply-linop-mutation-rotation firm L1>L0 theme (precedent), ksp-solve-mutation-rotation firm L1>L0 theme (precedent)
---
```

The L1>L0 lowering theme `matrix-weighted-norm-mutation-rotation` is not yet authored. The unfolded composition `√(dot(apply_linop(B, x), x))` (per the L0 source factoring `B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(dot)` at `palace/linalg/operator.cpp:601-606`) belongs in this L1>L0 theme — **not** in the L1 entry (per the post-cycle-009 invariant "Layers are defined high→low; lifting notes go in working notes"). The theme would also formalise the `Bx`-as-caller-supplied-workspace pattern (a sub-case of `mutable-workspace-pattern` Category 2, but with caller-not-class ownership; this is a sub-axis sliding across the bilinear-form sibling boundary). Routes to a future `abstractor` invocation. Sister-theme precedents: `apply-linop-mutation-rotation` (cycle-007), `axpby-mutation-rotation` (cycle-005), `ksp-solve-mutation-rotation` (cycle-008). Source: `reports/2026-05-27T215334Z-harvester-matrix-weighted-norm-l1/CYCLE.md` §Open questions item 3.

```yaml
---
slug: normalize-and-normalize-b-weighted-l1-candidates
opened_at: cycle-010
opened_by: harvester
status: open
relates_to: matrix-weighted-norm-and-bilinear-form-l1-rough-ins (this ledger)
---
```

The L0 source includes both `linalg::Normalize(comm, x)` (unweighted) and `linalg::Normalize(comm, x, B, Bx)` (B-weighted) at `palace/linalg/operator.hpp:376-384`. Both call their respective `Norml2` overload, then scale `x *= 1.0 / norm`. At L1 these compose as `(nrm2 ∘ scal)` and `(matrix-weighted-norm ∘ scal)` respectively, but neither has a firm L1 entry yet. They are L1 composite-utility candidates: small operators that bundle a norm computation with an in-place rescale at L0 but become a non-mutating "normalised-vector" function at L1. Sized small; route to a future harvester (or cross-layer-cross-cutter for the composite-utility cohort question). Worth considering whether the L1 layer should host the composite directly or whether it should be left as an explicit composition at the L2 level. Source: `reports/2026-05-27T215334Z-harvester-matrix-weighted-norm-l1/CYCLE.md` §Open questions item 5.

```yaml
---
slug: test-coverage-bounded-rough-in-nomenclature
opened_at: cycle-010
opened_by: harvester
status: open
relates_to: eigsolve cycle-009 rough-in (precedent), matrix-weighted-norm cycle-010 rough-in
---
```

The cycle-010 `matrix-weighted-norm` harvest lands as `rough-in (test-coverage-bounded)` — the second L1 rough-in of this kind after `eigsolve` (cycle-009). The pattern is identical in spirit: well-anchored signature and algebraic laws, dense callsite evidence, no dedicated direct test. The promotion-to-firm gates are also analogous: (a) direct test coverage, (b) indirect coverage via callsite test outputs, or (c) algebraic-law completeness verification. **Question for cycle-012 meta-phase**: should "test-coverage-bounded rough-in" be canonicalised as a named status tier (with formal gate criteria) in the methodology, or is the current per-entry recording of gates (in each operator's "Status" section) sufficient? The pattern may recur across cycle-011+ harvests of further L1/L2/L3 vocabulary (e.g., apply_linop L3 backfill, BLAS-1 cohort L3 backfill — both flagged as priority #20 follow-ups). Routes to meta-phase consideration. Source: `reports/2026-05-27T215334Z-harvester-matrix-weighted-norm-l1/CYCLE.md` §Open questions item 6.

```yaml
---
slug: bilinear-form-real-vector-coverage-gap
opened_at: cycle-010
opened_by: harvester
status: open
relates_to: matrix-weighted-norm-and-bilinear-form-l1-rough-ins (parent ledger), bilinear-form L1 rough-in (cycle-010)
---
```

Palace's `linalg::Dot(comm, x, A, y)` matrix-weighted overload set is **complex-vector only** — both overloads take `ComplexVector` arguments; there is no `Dot(comm, Vector, Operator, Vector)` overload for real vectors. The L1 `bilinear-form` entry's variant-axis table records this as "the real-`x` / real-`M` / real-`y` case is not surfaced by Palace". **Question**: should the L1 `bilinear-form` operator (a) restrict to complex-only at L1 (matching the Palace surface), (b) cover both real and complex at L1 with the real-only case marked "L1-only; no L0 anchor", or (c) treat the real case as an implicit composition `dot(x, apply_linop(M, y))` recovered from existing L1 operators? Harvester's **recommendation pending firm-promotion**: option (c) — the real case falls out of existing L1 vocabulary without needing a separate operator. The L1 `bilinear-form` covers the matrix-weighted reduction where Palace surfaces it as a distinct L0 free-function (complex case); the real case is recovered by composition. This keeps the L1 cohort minimal and matches the L1 invariant "subsumption-as-identity rather than dependency". Routes to future cross-layer-cross-cutter or layer-intro-author confirmation. Source: `reports/2026-05-27T215427Z-harvester-bilinear-form-l1/CYCLE.md` §Open questions item 2.

```yaml
---
slug: bilinear-form-slug-name-coordination
opened_at: cycle-010
opened_by: harvester
status: open
relates_to: matrix-weighted-norm-and-bilinear-form-l1-rough-ins (parent ledger), matrix-weighted-norm-naming-sweep (sibling L0-naming question), bilinear-form L1 rough-in (cycle-010)
---
```

The cycle-008 OQ that motivates the bilinear-form harvest names `L1/dot_bilinear` as the candidate slug. The L0 file-overview chapter (`book/src/L0/linalg-operator-file.md`, lines 73 and 88) also names `L1/dot_bilinear` as the expected lift target. The cycle-010 dispatch directive used the slug `bilinear-form` (matching the mathematical form name rather than the BLAS-1 family naming). This rough-in landed as `bilinear-form` per the dispatch directive. **Question**: keep `bilinear-form` (mathematical-form naming, matches the sibling-operator `matrix-weighted-norm` dispatched in cycle-010 wave-1), or rename to `dot_bilinear` (BLAS-family naming, matches the cycle-008 OQ and L0 chapter expectations)? Harvester's **recommendation pending firm-promotion**: keep `bilinear-form`. Reasons: (a) `dot_bilinear` is misleading because `dot` already returns a sesquilinear (Hermitian) form on complex input — `bilinear` modifying `dot` would suggest the unconjugated bilinear-form variant `tdot`, not the matrix-weighted generalisation; (b) the sibling-operator naming (`matrix-weighted-norm` for `nrm2_B`, `bilinear-form` for this operator) gives the L1 cohort a coherent mathematical-form vocabulary; (c) the specialisation law `bilinear_form(x, I, y) = dot(x, y)` is more readable than `dot_bilinear(x, I, y) = dot(x, y)`. **Follow-up**: the L0 chapter (`book/src/L0/linalg-operator-file.md`) should be updated to point at the chosen L1 slug after the cycle-010 wave-1 batch settles — this is a one-line annotation, layer-intro-author scope (companion to the sibling `matrix-weighted-norm-naming-sweep` OQ). Routes to future layer-intro-author dispatch or in-batch follow-up. Source: `reports/2026-05-27T215427Z-harvester-bilinear-form-l1/CYCLE.md` §Open questions item 3.

```yaml
---
slug: bilinear-form-variant-axis-test-coverage
opened_at: cycle-010
opened_by: harvester
status: open
relates_to: matrix-weighted-norm-and-bilinear-form-l1-rough-ins (parent ledger), test-coverage-bounded-rough-in-nomenclature (methodology pattern), bilinear-form L1 rough-in (cycle-010)
---
```

Promotion of `bilinear-form` from `rough-in` to `firm` is gated on **variant-axis test coverage**. Currently-anchored variant-axis cells: precision-mode (`double` only, inherited); output-arg-pattern (`return` only, the only L0 form); M-symmetry-property (`hermitian` `Bttr` at `boundarymodeoperator.cpp:85`; `non-symmetric` `Atn` at line 90); parallel-wrapper (both, inherited from `apply_linop`); element-type complex-`x`/complex-`y` only (both overloads use `ComplexVector`); `M` element-type both real (`Operator` at `operator.hpp:388-389`) and complex (`ComplexOperator` at lines 393-394). **Unexercised**: real-`x` / real-`y` cases (per the prior OQ); Cauchy–Schwarz-tight case at `y = x` with non-SPD `M` (only the SPD case has surfaced via Poynting boundary mass `Bttr`); algebraic law 8 (positive semi-definiteness) direct numerical witness. **Resolution path**: either expanded direct test coverage of `linalg::Dot(comm, x, A, y)` under `palace/test/unit/`, or literature-anchored evidence at firm-equivalent confidence (e.g. Higham 2008 §10 inner-product accuracy bounds for the matrix-weighted form). Note: this is the **third test-coverage-bounded L1 rough-in** (after `eigsolve` cycle-009 and `matrix-weighted-norm` cycle-010); the pattern is now well-established and surfaces the methodology question tracked under `test-coverage-bounded-rough-in-nomenclature`. Routes to future harvester revisit or cycle-012 meta-phase methodology consideration. Source: `reports/2026-05-27T215427Z-harvester-bilinear-form-l1/CYCLE.md` §Open questions item 4.

```yaml
---
slug: priority-13-now-landed-as-matrix-weighted-norm
opened_at: cycle-010
opened_by: integrator-per-report
status: routing
relates_to: nrm2-B-weighted-energy-norm-harvest (cycle-003 source OQ, now partially-answered), matrix-weighted-norm-and-bilinear-form-l1-rough-ins (cycle-008 parent ledger, partially-answered), scaffolding/priorities.md #13 (close target)
---
```

**Routing OQ for cycle-011 cycle-planner.** Priority #13 in `scaffolding/priorities.md` (currently reads: "`nrm2_B-weighted-energy-norm-L1` — depends on `apply_linop` (now firm) and `dot` (firm cycle-002). Citation: open question `nrm2-B-weighted-energy-norm-harvest`") is **now landed**: the cycle-010 wave-1 harvester dispatch (`reports/2026-05-27T215334Z-harvester-matrix-weighted-norm-l1/`) landed the operator under the canonical slug `matrix-weighted-norm` at `book/src/L1/matrix-weighted-norm.md` (`rough-in (test-coverage-bounded)`). The cycle-010 wave-2 #5 dispatch (`reports/2026-05-27T220123Z-harvester-nrm2-B-weighted-energy-norm-l1/`) verified the duplication (case (c) merge-and-rename verdict; all 8 critic checks pass).

**Action for cycle-011 planner**: when reading priorities.md alongside this OQ ledger, close priority #13 by either (a) moving it to a "Recently landed" section with cross-reference `landed-as-matrix-weighted-norm (cycle-010 wave-1: 2026-05-27T215334Z-harvester-matrix-weighted-norm-l1)`, or (b) removing the entry entirely and recording the close in cycle-011's plan note. Authority: `scaffolding/priorities.md` is meta-phase + cycle-planner co-edit (per CLAUDE.md §Write-authority partition); integrator-per-report cannot directly edit it, hence this routing OQ.

The cycle-010 cycle-planner already coordinated wave-2 dispatches against priority #13 via the duplicate-detection routing (planner case (a)/(c) recommendation; verified by wave-2 #5 verdict). The remaining firm-promotion gate for `matrix-weighted-norm` (test coverage) is tracked on the parent ledger `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` (status `partially-answered`) and does not block the priority-#13 close.

Source: integrator-per-report cycle-010 wave-2 #5 staging row + dispatch instructions.

```yaml
---
slug: fgmres-inner-loop-iterate-while-migration-lifter-candidate
opened_at: cycle-010
opened_by: combinator-miner
status: answered-by-rough-in-theme
answered_at: cycle-011
answered_by: lifter (reports/2026-05-27T234648Z-lifter-fgmres-inner-loop-iterate-while-migration/)
relates_to: gmres-inner-loop-iterate-while-migration (cycle-007, answered-by-rough-in-theme cycle-008), nleps-spec-gap-as-check-stop-into-carry-reuse-blocker (cycle-009, last-revisited cycle-010), variant-absorption-vs-instance-counting-policy (cycle-009, meta-phase scope), check-stop-into-carry-parameterization-over-stop-condition (cycle-009, helper-signature design)
---
```

**Routing OQ for cycle-011 cycle-planner.** The cycle-010 MCP-pilot combinator-miner audit (`reports/2026-05-27T215535Z-combinator-miner-check-stop-into-carry-mcp-pilot/CYCLE.md`) recommends a **lifter dispatch** on the cycle-008 `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` theme as the cycle-011+ next step, specifically to **re-anchor the theme against an upstream firm `book/src/spec/slices/gmres.md §L4 v0.7` form** (currently still v0.6 inline; located at lines 1012 and 1106 of that slice), then **apply the same migration theme as a separate `fgmres-inner-loop-iterate-while-migration` theme** (or unify both under a parameterized theme). The two FGMRES inner-loop sites at `palace/linalg/iterative.cpp:823-828` (3-condition break inside `FgmresSolver<OperType>::Mult`) are textually identical to the GMRES sites at `:644-649`; the lifter dispatch's verification target is whether **both lowerings produce a structurally identical `check_stop_into_carry` callsite shape** — if they do, that is the second-reuse formalization the cycle-008 promotion criterion was waiting on; if they diverge (e.g., FGMRES's `pc_side` differences leak into the predicate), the helper's signature needs revision before promotion. **Sequencing**: the lifter should be scheduled **before** any harvester on `book/src/L4/check-stop-into-carry.md` (the cycle-010 audit explicitly directs the cycle-planner to NOT schedule a harvester on the helper until either (a) the FGMRES theme is firmed with the helper at the same callsite shape as GMRES, or (b) a genuinely different consumer — e.g. a future literature-anchored MINRES inner loop, or NLEPS once spec'd — is identified). **Cycle-011 dispatch hint**: lifter-on-gmres.md-§L4-v0.6-to-v0.7 is the upstream prerequisite; the FGMRES theme authoring is the downstream act. May be a single lifter dispatch with two themes touched, or two sequential dispatches. Source: cycle-010 combinator-miner audit §Routing recommendation + §Cycle-010-or-011 lifter dispatch scope.

**Cycle-011 closure (lifter dispatch enacted)** (`reports/2026-05-27T234648Z-lifter-fgmres-inner-loop-iterate-while-migration/`): the cycle-011 wave-2 lifter dispatch authored `book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md` as a `rough-in` sister-theme to the cycle-008 GMRES rough-in. Status changed to `answered-by-rough-in-theme` (analogous to the cycle-008 disposition of the GMRES theme): theme is authored against the same speculative `gmres.md §L4 v0.7` upstream; both this theme and its sibling firm when the upstream migration lands and aligns. The cycle-010 audit's "lower-edge second-reuse" reading is preserved in the new theme's §Status — sister-algorithm twinning is recorded as corroborating evidence but does NOT unblock firm L4 promotion of `check_stop_into_carry`. The firm-promotion blocker remains tracked under `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker` (non-`GmresSolverBase` Krylov consumer required). The upstream lifter on `gmres.md §L4 v0.6→v0.7` is NOT yet enacted; it is the natural follow-up. The "may be a single lifter dispatch with two themes touched" alternative from the dispatch hint was NOT taken — cycle-011 wave-2 enacted only the FGMRES sister-theme authoring; the cycle-008 GMRES theme was re-anchor-checked (no firm-status changes since cycle-008 ⇒ no re-anchor needed; see report §Discipline notes "Re-anchoring scope check"). Routes forward: (a) future lifter dispatch on `gmres.md §L4 v0.6→v0.7` self-rotation (still pending; this would firm both sister themes); (b) cycle-012 meta-phase consideration of `variant-absorption-vs-instance-counting-policy` codification (this dispatch is the second data point per CYCLE.md §Open questions / caveats item 5).

```yaml
---
slug: l4-v01-v06-self-rotation-history-lift-target-decision
opened_at: cycle-010
opened_by: same-layer-cross-cutter
status: open
relates_to: phase-1-corpus-reduction-audit (priority-19)
---
```

Should the L4 v0.1→v0.6 self-rotation derivation in `book/src/spec/slices/gmres.md` lines 24-657 (post-reduction; the v0.2 through v0.6 sections retained as unique methodology evidence) be lifted to `concepts/derived-view-hoisting.md` as a multi-step worked example, or retained as slice-level methodology evidence? Three candidate lift targets surfaced during the cycle-010 first-instance phase-1-corpus-reduction-audit (`reports/2026-05-27T220000Z-same-layer-cross-cutter-phase-1-corpus-reduction-audit/CYCLE.md`): (a) `concepts/derived-view-hoisting.md` — likely the cleanest target since v0.4's commit-layer hoist and v0.6's witness-layer hoist are both canonical derived-view-hoisting moves; (b) a candidate `concepts/witness-typed-dispatch.md` (per gmres.md v0.6 §"Open questions") — promotion criterion is "second instance lands"; no second instance has landed yet, so defer concept extraction; (c) the slice itself, retained as canonical worked-example evidence — current state post-reduction. Promotion of (a) or (b) would unblock further reduction of gmres.md down to the stub header alone. Source: cycle-010 phase-1-corpus-reduction-audit, residual gap #1 of slice-1 gmres.md.

```yaml
---
slug: cg-initial-residual-quirk-palace-bug-flag-lift-path
opened_at: cycle-010
opened_by: same-layer-cross-cutter
status: open
relates_to: phase-1-corpus-reduction-audit (priority-19)
---
```

The Palace `!B && initial_guess` branch (`palace/linalg/iterative.cpp:399-412`) computes `initial_res = (b·b)^{1/4}` rather than `‖b‖₂` due to a `Norml2`-vs-`Dot` asymmetry between the unpreconditioned and preconditioned branches. This is a likely Palace bug. Where in the firm artifact should this finding live, and should it be confirmed with upstream before being annotated as a firm finding? Three candidate lift paths: (a) annotate `L1/ksp_solve.md` Semantics with the bug-flag; (b) add a `verified_against` row to `L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B noting the quirk; (c) keep as an OQ pending upstream confirmation. Finding extracted from `book/src/spec/slices/cg.md:95` and Working Notes line 286 in the pre-reduction version (preserved in the cycle-010-reduced stub header's "Open questions still pending lift" subsection). The finding is unique to the cg.md slice; the firm L1>L0 theme recognises CheckDot but does not record this bug-flag. Source: cycle-010 phase-1-corpus-reduction-audit, residual gap #1 of slice-2 cg.md.

```yaml
---
slug: l1-orthogonalize-promotion-from-arnoldi-step-and-orthog
opened_at: cycle-010
opened_by: same-layer-cross-cutter
status: answered
answered_at: cycle-012
answered_in: book/src/L1/orthogonalize.md
relates_to: phase-1-corpus-reduction-audit (priority-19)
---
```

**Closed (cycle-012, integrator-per-report)**: the firm `L1/orthogonalize` operator landed at `book/src/L1/orthogonalize.md` via the cycle-012 wave-1 `harvester:2026-05-28T034130Z-harvester-l1-orthogonalize` dispatch (`pass-after-repair`). The promotion criterion ("small AND simplifies higher forms") is met: the operator is one variant-dispatched primitive (`gs_orthog ∈ {MGS, CGS, CGS2}`) with dependencies `dot` + `axpy` only (normalisation excluded per the L0 header "does not normalize the output" contract). All three variants carry dedicated parametric test coverage (real / complex / B-weighted + empty-basis + a direct `⟨w', V[i]⟩ ≈ 0` substitutability assertion); absorption corrected (by repair) to all-three-levels (a/b/c) under residual-axis disclosure; Householder explicitly scoped out per the unimplemented-component policy. This unblocks the deferred reductions of both `book/src/spec/slices/arnoldi_step.md` (cycle-010 batch-1) and `book/src/spec/slices/orthog.md` (cycle-011 batch-2 partial). Residual follow-ups spun out as their own OQs: `orthogonalize-mutation-rotation-l1-l0-theme` (L1>L0 lowering not yet authored) and `concepts-orthogonalization-coefficient-normalisation-drift` (concept-page refresh).

Should a firm `L1/orthogonalize` (or `L1/orthogonalize-column`) operator be promoted from the speculative slice corpus? Promotion would unblock simpler reduction of `book/src/spec/slices/arnoldi_step.md` and `book/src/spec/slices/orthog.md`. Promotion criterion under the unimplemented-Palace-stub policy is "small AND simplifies higher forms" — both are plausibly met: `orthogonalize` is small (one variant-dispatched primitive with three implementations: MGS sequential / CGS batched / CGS2 batched-with-refine), and lifting it would let `L4/krylov-step.md` Form A reference `op.orthog` as a firm L1 operator type rather than as a slice-level concept. The variant-axis profile (`gs_orthog ∈ {MGS, CGS, CGS2}`) and the MPI-collective shape table (MGS = j+2 allreduces; CGS = 2; CGS2 = 3) are unique evidence justifying promotion. Source: cycle-010 phase-1-corpus-reduction-audit, residual gap #1 of slice-3 arnoldi_step.md + slice-recommendation §"Open questions" item 4.

**Amendment (cycle-011, same-layer-cross-cutter)**: this OQ is now blocking **2 slices** (arnoldi_step.md from cycle-010 batch-1; orthog.md from cycle-011 batch-2) and is referenced by **5 firm entries** (`concepts/orthogonalization.md`, `L2/krylov-step.md`, `L3/krylov-step.md`, `L4/krylov-step.md`, `L1-L0/ksp-solve-mutation-rotation.md`). The orthog.md cycle-011 batch-2 partial-reduction is gated on this promotion — the unique L1 invariants (read-only `V_basis` / mutated `w` / written `H` / routine-owns-reduction `dot_op`) and MPI-collective shape disclosure (MGS: m reductions of size 1; CGS: 1 of size m; CGS2: 2 of size m) are retained in the orthog.md L2/L3/L4 sections pending firm L1. Priority weight raised: high-confidence harvester candidate for batch-2-or-3. Source: cycle-011 phase-1-corpus-reduction-batch-2 §"Open questions" item 2.

```yaml
---
slug: phase-1-corpus-reduction-remaining-7-slices
opened_at: cycle-010
opened_by: same-layer-cross-cutter
status: open
relates_to: phase-1-corpus-reduction-audit (priority-19)
---
```

The cycle-010 first-instance phase-1-corpus-reduction-audit (`reports/2026-05-27T220000Z-same-layer-cross-cutter-phase-1-corpus-reduction-audit/CYCLE.md`) covered 3 of 10 slices (gmres.md, cg.md, arnoldi_step.md). The remaining 7 slices for cycle-011+ batch audits, in suggested priority order (by expected supersession overlap with firm entries): (1) `orthog.md` — overlaps `L1/orthogonalize` (pending promotion); ties into arnoldi_step audit closure; (2) `chebyshev.md` — likely overlaps `L2/krylov-step` polynomial-recurrence variant; (3) `polynomial_recurrence_step.md` — overlaps `L2/krylov-step` polynomial-recurrence variant; (4) `divfree.md` — overlaps `L1/ksp_solve` use pattern (cited as the canonical use site in `L1/ksp_solve` §Evidence); (5) `cg_preconditioning_framework.md` — likely overlaps `L1/ksp_solve` + `L4/krylov-step` Form A; (6) `plane_rotation_stream.md` — likely overlaps `L2/krylov-step` Givens-rotation pattern (could promote `givens_generate` / `givens_apply` as firm L1); (7) `sparse_triangular_solve.md` — likely a low-overlap slice (no firm krylov-chain analog); defer or audit separately. Suggested batch size: 2-4 slices per audit dispatch to keep the dispatch within context budget. The audit template established in cycle-010 (Supersession map / Residual gaps / Recommended action / Proposed changes per slice) is machine-replayable for cycle-011+ replay. Source: cycle-010 phase-1-corpus-reduction-audit §"Open questions" item 5.

```yaml
---
slug: l3-index-matvec-naming-vs-apply_linop-slug
opened_at: cycle-011
opened_by: harvester
status: answered
answered_at: cycle-012
answered_in: book/src/L3/index.md (§Semantics (overlay))
relates_to: l3-vocabulary-inventory-gap (this ledger), l3-backfill-apply-linop-and-blas1-cohort (this ledger)
---
```

The L3 index (`book/src/L3/index.md:13`) advertises whole-tensor primitives using the casual name "matvec" alongside "axpy, dot, nrm2 as field operations". The cycle-011 wave-1 firm L3 entry for the matvec primitive uses the formal slug **`apply_linop`** (inherited from the L1 entry's slug per the layer-coherence invariant + identity-in-form rotation). The two names refer to the same primitive — `apply_linop` is the matvec generalisation that subsumes square and rectangular operators, real and complex element types, all operator representations. The current divergence is benign: the new L3 entry's first paragraph makes the equivalence explicit, and a reader navigating from the L3 index's "matvec" prose to the `apply_linop` dep-map row will recognise the linkage. **Routing note for cycle-012+ planner**: if uniformity is desired, a future `lifter` dispatch could touch up the L3 index's prose to use the formal slug (`matvec → apply_linop`), or alternatively the L3 entry could expose an "also known as: matvec" annotation. Low-priority cleanup; not blocking any current work. Similar naming gaps may surface as the BLAS-1 cohort lands (the L3 index's "axpy, dot, nrm2" prose vs the formal slugs `axpy.md`, `dot.md`, `nrm2.md` — these align exactly, but the broader "matvec → apply_linop" pattern is the one that needs the alias annotation). Source: cycle-011 harvester dispatch `reports/2026-05-27T234502Z-harvester-l3-apply-linop/CYCLE.md` §"Open questions / caveats" item 4.

**Answered (cycle-012, layer-intro-author L3-index-refresh; applied by integrator-per-report).** The refresh of `book/src/L3/index.md` §"Semantics (overlay)" adopted the **`matvec (apply_linop)`** parenthetical form — the casual name "matvec" is retained (so the existing back-references from `apply_linop.md:20,24,150,173` and `scal.md:26,49,137` to the index's "matvec ... as field operations" advertisement remain valid) and the formal slug `apply_linop` is parenthesized inline with the framing "the linear-operator-application generalisation of 'matvec'". This matches the `apply_linop` entry's own framing (`apply_linop.md:24`: "`apply_linop` is the matvec generalisation") and satisfies both alternatives the OQ proposed (the casual name survives AND the formal slug is present with the equivalence stated). The naming is now consistent across the index and the entry; the divergence is reconciled. Source: cycle-012 layer-intro-author dispatch `reports/2026-05-28T020000Z-layer-intro-author-l3-index-refresh/CYCLE.md` §"Open questions / caveats".

```yaml
---
slug: concepts-nrm2-stability-claim-correction
opened_at: cycle-011
opened_by: harvester
status: answered
answered_at: cycle-012
answered_in: book/src/concepts/nrm2.md (§Contract stability bullet)
relates_to: l3-backfill-apply-linop-and-blas1-cohort (this ledger), l3-vocabulary-inventory-gap (this ledger)
---
```

The concept page `book/src/concepts/nrm2.md` line 9 carries an incorrect stability claim: "Stability: production implementations use scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow when computing `√Σ|x_i|²`." This contradicts the firm L1 entry's finding at `book/src/L1/nrm2.md:11`: "Note: the concept page claims Palace uses 'scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow'. This is **not** what `linalg::Norml2` actually does — it computes the naive `√⟨x, x⟩` via `Dot`." The L1 entry is authoritative; the concept page should be corrected. The cycle-011 wave-1 L3 backfill of `nrm2` (`book/src/L3/nrm2.md`) carries the same correction-pending note in §Context (referencing the L1 entry's note), which keeps the L3 entry internally consistent but leaves the concept page's text uncorrected. **Out of scope for harvester** — the concept page is owned by layer-intro-author / cross-cutter, not harvester. **Routing note for cycle-012+ planner**: dispatch a layer-intro-author or same-layer-cross-cutter touch-up on `book/src/concepts/nrm2.md:8-9` to correct the stability claim. The correction can be either (a) remove the incorrect claim and replace with the L1-authoritative description ("Palace's `linalg::Norml2` computes the naive `√⟨x, x⟩` via `Dot`; the BLAS scaled-summation algorithm is not used"), or (b) reframe the claim as a generic BLAS heritage note while explicitly noting Palace's deviation. Low-priority cleanup; not blocking any current work. Source: cycle-011 harvester dispatch `reports/2026-05-27T231500Z-harvester-l3-blas1-reduction-cohort/CYCLE.md` §"Open questions / caveats" item 2.

**Answered cycle-012 (layer-intro-author concept-corrections; applied by integrator-per-report).** The false stability bullet at `book/src/concepts/nrm2.md:9` was replaced (option (a) — the L1-authoritative description) with: "Palace's `linalg::Norml2` computes the naïve `√⟨x, x⟩` via `Dot` (one-line body `std::sqrt(std::abs(Dot(comm, x, x)))`); it does **not** use scaled summation. There is no Palace-level overflow/underflow guarantee — Palace inherits whatever the underlying `dot` reduction provides. BLAS-style scaled-summation `nrm2` ... is **not present** in Palace." The bullet now forwards the citation to the authoritative `[L1/nrm2](../L1/nrm2.md)`. The correction matches the firm L1 entry's finding verbatim (`L1/nrm2.md:11, :84, :97`; `palace/linalg/vector.hpp:255-260`). This also closes the cycle-003-vintage duplicate of this slug (`opened_at: cycle-003`, same ledger) — both are the same correction, now landed. Source: cycle-012 layer-intro-author dispatch `reports/2026-05-28T034221Z-layer-intro-author-concept-corrections/CYCLE.md` Task 1.

```yaml
---
slug: scal-mutation-rotation-l1-l0-theme
opened_at: cycle-011
opened_by: harvester
status: open
relates_to: l3-backfill-apply-linop-and-blas1-cohort (this ledger)
---
```

No firm `book/src/L1-L0/scal-mutation-rotation.md` theme exists. The L1 entry `book/src/L1/scal.md` sketches the L1>L0 lowering content in §"L1 vs L0 distinction" and §Evidence (the in-place mutation via `mfem::Vector::operator*=` / `ComplexVector::operator*=`, the real-imag-shape branch erasure at `ComplexVector::operator*=` lines 207-211, the `Normalize` fused construct combining `nrm2 + scal` at `palace/linalg/vector.hpp:262-270`), but no dedicated mutation-rotation theme has been authored. The cycle-011 wave-1 L3 backfill of `scal` (`book/src/L3/scal.md`) inherits this gap — the L3 → L1 → L0 chain reaches firm coverage only down to L1; the L1 → L0 hop is currently informal. **This is not a new gap introduced by the L3 backfill** — the same gap exists at L1; it predates cycle-011. **Routing note for cycle-012+ planner**: dispatch an `abstractor` or `lifter` on this theme — analogous to the firm `axpby-mutation-rotation` and `axpbypcz-mutation-rotation` themes that have already landed at L1>L0 (`book/src/L1-L0/axpby-mutation-rotation.md`, `book/src/L1-L0/axpbypcz-mutation-rotation.md`). The theme should cover the destination-buffer mutation pattern, the real-imag branch erasure (transparent specialisation), and the `Normalize` fused-construct decomposition. Low-priority; the cohort closure makes the gap newly visible. Source: cycle-011 harvester dispatch `reports/2026-05-27T234540Z-harvester-l3-scal/CYCLE.md` §"Open questions / caveats" item 4.

```yaml
---
slug: l3-index-semantics-overlay-blas1-cohort-prose-refresh
opened_at: cycle-011
opened_by: harvester
status: answered
answered_at: cycle-012
answered_in: book/src/L3/index.md (§Semantics (overlay))
relates_to: l3-vocabulary-inventory-gap (this ledger), l3-index-matvec-naming-vs-apply_linop-slug (this ledger)
---
```

The L3 index's `## Semantics (overlay)` prose (`book/src/L3/index.md:11-15`) currently lists only "matvec, axpy, dot, nrm2 as field operations" as the L3 vocabulary; the closed BLAS-1 cohort (apply_linop + axpy + axpby + axpbypcz + dot + nrm2 + scal) is now fully reflected in the dep-map table below but the §"Semantics (overlay)" prose has not been updated. `scal`, `axpby`, `axpbypcz`, and `apply_linop` are implied by the cohort closure but not literally named in the inventory line. **Out of scope for harvester** — the index `Semantics (overlay)` prose is owned by `layer-intro-author`, not harvester. **Routing note for cycle-012+ planner**: dispatch a `layer-intro-author` refresh on `book/src/L3/index.md` to bring the §"Semantics (overlay)" prose into alignment with the closed BLAS-1 cohort's full inventory (or alternatively reframe the prose as describing the *kind* of primitives — "BLAS-1 whole-tensor primitives, linear operator application, reductions" — rather than enumerating specific names). Related to the broader `l3-vocabulary-inventory-gap` OQ but more concrete: the gap is now closed in the dep-map but not in the inventory prose. Low-priority cleanup. Source: cycle-011 harvester dispatch `reports/2026-05-27T234540Z-harvester-l3-scal/CYCLE.md` §"Open questions / caveats" item 5.

**Answered (cycle-012, layer-intro-author L3-index-refresh; applied by integrator-per-report).** The refresh of `book/src/L3/index.md` §"Semantics (overlay)" took the OQ's suggested *kind*-of-primitives reframing AND named the full closed BLAS-1 cohort inline. The whole-tensor-field-operations bullet now reads: matvec (`apply_linop`), the linear-update family (`axpy`, `axpby`, `axpbypcz`, `scal`), and the reductions (`dot`, `nrm2`) — all 8 firm L3 operators (the 7 BLAS-1 cohort + `apply_linop`) are now named, cross-checked against the dep-map table (`index.md:19-28`); the composition operator `krylov-step` is named in the field-transitions bullet. The reframing as "kinds of primitives" with concrete slugs named inline means future cohort members (`gemv`, `trsv`) absorb without further prose churn. The dep-map/prose gap is closed. Note: the broader `l3-vocabulary-inventory-gap` OQ remains open (it tracks *which additional* operators warrant L3 backfill beyond the closed cohort — `gemv`/`trsv`/`ksp_solve`/`eigsolve` candidates). Source: cycle-012 layer-intro-author dispatch `reports/2026-05-28T020000Z-layer-intro-author-l3-index-refresh/CYCLE.md` §"Open questions / caveats".

```yaml
---
slug: slepc-convergence-reason-lift-sub-theme
opened_at: cycle-011
opened_by: abstractor
status: open
relates_to: eigsolve-mutation-rotation (book/src/L1-L0/), eigsolve-iteration-count-result-field (this ledger, cycle-009)
---
```

SLEPc internally exposes a richer convergence-reason enum (`EPSConvergedReason`) than what `BaseKspSolver::Mult` surfaces; the SLEPc code in Palace prints it via `EPSConvergedReasonView` at `palace/linalg/slepc.cpp:699` but never queries it programmatically. The cycle-011 wave-2 firm theme `book/src/L1-L0/eigsolve-mutation-rotation.md` Sub-pattern C records the per-status mapping at narrative-level but does not enumerate the full reason → `EigStatus` mapping. A future `slepc-convergence-reason-lift` sub-theme (cycle-012+ candidate) would carry the full table, including the `EPS_DIVERGED_BREAKDOWN` / `EPS_DIVERGED_SYMMETRY_LOST` → `LinearSolveFailed` mapping that the partly-constructive materialisation in Sub-pattern B references. **Routing note for cycle-012+ planner**: dispatch an `abstractor` or `lifter` for the sub-theme; the firm parent theme records the gap as an explicit sub-theme candidate, so the dispatch can scope cleanly. Out of scope for the cycle-011 wave-2 firm theme. Source: cycle-011 abstractor dispatch `reports/2026-05-27T234730Z-abstractor-eigsolve-mutation-rotation-l1-l0/CYCLE.md` §"Open questions / caveats" item 3.

```yaml
---
slug: eigsolve-driver-side-double-solve-composition
opened_at: cycle-011
opened_by: abstractor
status: open
relates_to: eigsolve-mutation-rotation (book/src/L1-L0/), L1/eigsolve, L2/index.md
---
```

`palace/drivers/eigensolver.cpp:377-407` shows a higher-level composition where the linear eigensolve's result (a `unique_ptr<EigenvalueSolver> eigen` plus its `num_conv`) is consumed as initial guesses by a subsequent `QuasiNewtonSolver` refinement (`qn = make_unique<QuasiNewtonSolver>(... std::move(eigen), num_conv, ...)`). The composition then re-invokes `Solve()` on the refined eigen-solver. The L1 `eigsolve` form does not capture this composition — it is a higher-level monadic-bind pattern over two `eigsolve` invocations with the first's result threaded as initial-condition for the second. This composition is more naturally an L2 / L4 monadic-composition pattern, **out of scope** for the L1>L0 mutation-rotation theme `book/src/L1-L0/eigsolve-mutation-rotation.md`. **Routing note for cycle-012+ planner**: dispatch a `same-layer-cross-cutter` at L2 or an `abstractor` at L4 to formalise this composition pattern as an L2/L4 candidate (the pattern is `eigsolve >>= refine_eigsolve` or similar bind-shape). The cycle-011 wave-2 firm theme explicitly excluded this from its scope per the one-theme-per-invocation discipline. Source: cycle-011 abstractor dispatch `reports/2026-05-27T234730Z-abstractor-eigsolve-mutation-rotation-l1-l0/CYCLE.md` §"Open questions / caveats" item 4.

```yaml
---
slug: eigsolve-mutation-rotation-lowering-verifier-followup
opened_at: cycle-011
opened_by: abstractor
status: open
relates_to: eigsolve-mutation-rotation (book/src/L1-L0/)
---
```

The cycle-011 wave-2 firm theme `book/src/L1-L0/eigsolve-mutation-rotation.md` is recognised at the **structural level**: the four sub-pattern recognition rules are sketched at section level; the per-backend ARPACK / SLEPc / `QuasiNewtonSolver` bodies are cited at section level; the ten `opInv->Mult` callsites are exhaustively cited per cycle-010 lifter; the per-pair extraction rewrite and the status sum-type derivation are structurally complete. **Full per-step sub-rewrite verification** — i.e., walking each line of each backend's body and confirming the per-step kernel decomposes into the cited sister-theme primitives — is deferred to a `lowering-verifier` cycle. This is the same approach as `ksp-solve-mutation-rotation`'s cycle-008 firm-promotion: the theme stands on structural-level coverage; per-line verification is a follow-up audit. **Routing note for cycle-012+ planner**: dispatch a `lowering-verifier` on `book/src/L1-L0/eigsolve-mutation-rotation.md` to walk each backend body and confirm: (i) the four-stage setup absorption (Sub-pattern A) is consistent with per-backend `SetType` / `SetProblemType` / `SetExtraSystemMatrix` / `SetPreconditionerUpdate` sub-axis bindings; (ii) the ten `opInv->Mult` callsites are exhaustive across the Palace corpus (re-verify by `search_text`); (iii) the per-pair extraction rewrite is consistent across the three backend orchestrations (each backend's `GetEigenvalue` / `GetEigenvector` / `GetError` returns values in the same coordinate convention modulo the Higham scaling factor). Source: cycle-011 abstractor dispatch `reports/2026-05-27T234730Z-abstractor-eigsolve-mutation-rotation-l1-l0/CYCLE.md` §"Open questions / caveats" item 5.

```yaml
---
slug: eigsolve-slepc-nep-coordinate-convention-audit
opened_at: cycle-011
opened_by: repairer
status: answered
answered_at: cycle-012
answered_in: book/src/L1/eigsolve.md (§5 + Verified-against block)
resolution: resolved-with-refinement
relates_to: eigsolve-scaling-coordinate-convention (resolved cycle-011), eigsolve-mutation-rotation (book/src/L1-L0/)
---
```

**Resolved cycle-012 (lowering-verifier, `reports/2026-05-28T034311Z-lowering-verifier-slepc-nep-coordinate-convention/`), verdict resolved-with-refinement.** The audit answers the open binary ("does the SLEPc NEP API un-scale internally so `return l` is correct, OR is there a missing `* gamma`?") in favour of the first horn: **NEP solves the original (un-scaled) problem directly, so `return l` is correct and there is no missing `* gamma`.** Decisive evidence: the NEP function/jacobian callbacks (`__form_NEP_function` / `__form_NEP_jacobian` at `slepc.cpp:2170-2202`) build `A(λ) = K + λC + λ²M + A2(Im{λ})` and its Jacobian from the **raw** operators with unit/`λ`/`λ²` coefficients (no `δ` premultiplier, no `γ`-reparametrization); the spectral target is set un-scaled (`NEPSetTarget(nep, sigma)` at `:1503`, contrast `EPSSetTarget(eps, sigma / gamma)` at `:674`, `PEPSetTarget(pep, sigma / gamma)` at `:1157`); the NEP residual path (`GetResidualNorm` / `GetBackwardScaling` at `:1760-1798`) recomputes operator norms independently and deliberately does not reuse the scaling-time `gamma`/`delta` (the `// Make sure not to use norms from scaling` comment at `:1781`). Consequently the `gamma`/`delta` that `SlepcNEPSolver::SetOperators` computes (`:1649-1650` linear, `:1715-1716` quadratic) are an **effectively-dead store w.r.t. the eigenvalue-coordinate transform**. The refinement: un-scale-at-accessor convention (b) holds **uniformly across all four backends in RESULT coordinates**, but via two distinct mechanisms — ARPACK / EPS / PEP solve-scaled-then-un-scale (`* gamma` at the accessor), SLEPc-NEP solve-and-return-un-scaled. §5 prose updated to state the per-backend mechanism precisely and drop the "pending audit" flag; the cycle-011 "Resolved" sentence (which flagged the NEP detail for follow-up) is retained verbatim, the cycle-012 "Resolved" sentence sits before it (the two close distinct OQs). Caveat: conclusion rests on source-read of the control flow, `empirically-unwitnessed` (no `test-eigensolver.cpp` NEP case) — see the low-priority OQ `eigsolve-nep-coordinate-convention-empirical-witness`.

The cycle-011 lifter dispatch on the `eigsolve` OQ cluster (`reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/`) resolved `eigsolve-scaling-coordinate-convention` by adopting convention (b) — L1 returns un-scaled eigenvalues, matching the L0 un-scale-at-accessor convention uniformly across the EPS / PEP / NLEPS backends. The cycle-011 critic + repairer identified an isolated SLEPc-NEP edge case that does NOT affect the broader resolution but warrants follow-up audit: `SlepcNEPSolverBase::GetEigenvalue(i)` at `palace/linalg/slepc.cpp:1554-1560` returns `l` directly without applying `* gamma`, BUT `SlepcNEPSolver::SetOperators` at `palace/linalg/slepc.cpp:1645-1651` (linear-K-M overload) AND `:1711-1719` (K-C-M overload) both compute `gamma = std::sqrt(normK / normM)` when `type != ScaleType::NONE` — the same Higham-norm scaling pattern as EPS / PEP. So the L0 behaviour is: NEP computes a non-trivial gamma at `SetOperators`, but its `GetEigenvalue` accessor does NOT apply `* gamma` — this is a genuine asymmetry in the L0 surface, NOT explained by the simpler "NEP gamma = 1" reading (which would be wrong). Open question: does the SLEPc NEP API itself un-scale before returning eigenpairs to the Palace wrapper (so the Palace `GetEigenvalue` returning `l` directly is correct), or is there a missing `* gamma` un-scale that would manifest as scaled eigenvalues being passed to callers? Recommended target: cycle-012+ `lifter` / `lowering-verifier` / harvester-NEP dispatch on `palace/linalg/slepc.cpp:1554-1719` (the `SlepcNEPSolverBase` constructor + `SetOperators` overloads + `GetEigenvalue` body). Provenance: cycle-011 repairer at `reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/META.md` §Repair Finding 1 (NEP-gamma overclaim repaired by softening prose; the genuine asymmetry surfaced as this follow-up OQ).

```yaml
---
slug: orthog-plane-rotation-stream-sub-slice-batch-3-joint-audit
opened_at: cycle-011
opened_by: same-layer-cross-cutter
status: answered
answered_at: cycle-012
answered_in: book/src/spec/slices/orthog.md (plane-rotation sub-slice reduced to stub), book/src/spec/slices/plane_rotation_stream.md (partial-reduction + hoisted invariant)
relates_to: phase-1-corpus-reduction-audit (priority-19), phase-1-corpus-reduction-remaining-7-slices (this ledger), l1-orthogonalize-promotion-from-arnoldi-step-and-orthog (this ledger)
---
```

The plane-rotation-stream sub-slice in `book/src/spec/slices/orthog.md` lines 313-464 overlaps `book/src/spec/slices/plane_rotation_stream.md` (deferred to batch-3 of the phase-1-corpus-reduction-audit per the cycle-010 priority order). Both slices have unique material: `orthog.md` lines 313-464 contain a per-step driver decomposition (steps (i)-(iv): replay, generate, apply, propagate-to-RHS) + two near-duplicate L1 entries (lines 364-398 and lines 405-464) that should be merged. The eventual structural split into `orthog/gram_schmidt.md` + `orthog/plane_rotation.md` is flagged in the slice corpus' Open questions at `orthog.md:407` and `:449-450` but pending. Batch-3 of the audit should perform the joint reduction — audit `plane_rotation_stream.md` together with `orthog.md` lines 313-464 to decide where the canonical home for plane-rotation-stream L0/L1/L2/L3/L4 content lives. Doing the reduction unilaterally on either slice risks creating a stale stub in one slice that points at content that has been moved to the other. Source: cycle-011 phase-1-corpus-reduction-batch-2 §"Open questions" item 1.

**Answered cycle-012** by the same-layer-cross-cutter dispatch `reports/2026-05-28T034141Z-same-layer-cross-cutter-phase-1-corpus-reduction-batch-3/CYCLE.md` (status `ready`, pass-after-repair). The joint audit's verdict: the `orthog.md` plane-rotation sub-slice is a strictly-less-complete duplicate of `plane_rotation_stream.md` (the actually-more-complete dissection IS the long-recorded `orthog/plane_rotation.md` split product). The integrator (this cycle) reduced the full `orthog.md` plane-rotation sub-slice (the `## Context` / `# Orthogonalization (plane-rotation stream)` block through EOF, line range corrected in repair from the originally-mis-stated 311-376 to the true 225-376, text-anchored) to a single stub-pointer at `plane_rotation_stream.md`, **eliminating both near-duplicate L1 entries** (resolving the batch-2 "should be merged" finding via elimination, not in-file merge). The one unique fragment — the formal least-squares-residual invariant formerly at `orthog.md:350` — was **hoisted first** into `plane_rotation_stream.md` §L1 §"Invariant" (proposed change 2A applied before the reduction per the repairer's sequencing note), so nothing was lost. `plane_rotation_stream.md` was partial-reduced in the same pass (L0-primitives / L1-procedure / L2-primitives stubbed against the firm Givens concept-page family; §L0 call-sites / §L0 negative-result / §L2 stream-operations-bridge / the entire §L3 retained as the canonical detailed obstruction source). **Residual follow-ups spun out** to cycle-012 OQs: `plane-rotation-concept-page-canonical-pointer-repoint` (the three firm concept pages still cite the `orthog` slice as canonical — `layer-intro-author` follow-up) and `plane-rotation-givens-l0-citation-range-reconcile` (the one-off `iterative.cpp` line-range discrepancy — `verify-citation-range` follow-up). The HIGH-severity line-map defect (the audit's own grep verified the END boundary but not the START boundary) is flagged for the cycle-012 meta-phase as a severity escalation of the `phase-1-slice-reduction-audit` skill-candidate / `phase-1-corpus-audit-line-range-arithmetic-brittleness` friction.

```yaml
---
slug: l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion
opened_at: cycle-011
opened_by: same-layer-cross-cutter
status: answered
answered_at: cycle-012
answered_in: book/src/L1/chebyshev-smoother.md, book/src/L2/chebyshev-iteration.md
relates_to: phase-1-corpus-reduction-audit (priority-19), phase-1-corpus-reduction-remaining-7-slices (this ledger)
---
```

A firm `L1/chebyshev-smoother` operator entry (and possibly `L2/chebyshev-iteration`) is pending lift. The slice corpus' `book/src/spec/slices/chebyshev.md` §L1 and §L2 are currently the only firm Chebyshev definition in the artifact; they are cited as canonical evidence by `L2/krylov-step.md:140, :142` and `L4/krylov-step.md` §Variant axes list-item 3 (polynomial-kind at line 141, absorbed at level (c) into `op.scalars`). Promotion criterion under the unimplemented-Palace-stub policy is "small AND simplifies higher forms" — both plausibly met: the operator is a Richardson sweep over polynomial recurrence (small), and lifting would let `L2/krylov-step` variant axis (3) point at a concrete L2 row (simplifies higher forms). The `chebyshev.md` partial-reduction is gated on this promotion — the slice's L1/L2/L3/L4 content is retained pending firm L1/L2 entries. Source: cycle-011 phase-1-corpus-reduction-batch-2 §slice-2 residual gaps #1-2.

**Answered cycle-012** by the harvester dispatch `reports/2026-05-28T034154Z-harvester-chebyshev-l1-l2/CYCLE.md` (status `pass-after-repair`). Both rows landed firm: `book/src/L1/chebyshev-smoother.md` (the third constructed-operator gate at L1, and the first that is a fixed-degree polynomial *action* rather than a solve-to-convergence; variant 4th-/1st-kind absorbed into `op.scalars`) and `book/src/L2/chebyshev-iteration.md` (the explicit degree-`order` three-term polynomial recurrence, the concrete L2 entry behind `L2/krylov-step` variant-axis 3). The firm-without-dedicated-test decision (multigrid-integration coverage only) was surfaced for integrator ratification and **ratified keep-firm** by the cycle-012 integrator: every law is a verified-exact syntactic identity on fully-specified source, chebyshev is a bounded fixed-degree polynomial action with closed-form coefficients and live integration coverage, and the `eigsolve` rough-in precedent does not bind (that rough-in was driven by literature-inferred convergence semantics absent here). **Residuals spun out** to four new cycle-012 OQs: `chebyshev-slice-rho_0-coefficient-correction` (the slice's `:160` `rho_0` error persists until reduction), `spectrum_estimate-l1-rough-in-opacity` (the opaque setup dependency lacks a firm L1 entry), `l3-l4-chebyshev-rows-eligible` (L3/L4 rows still block full `chebyshev.md` reduction), and `chebyshev-l1-l0-and-l2-l1-lowering-themes` (the forward lowering themes are abstractor candidates). The L1/L2 promotion this OQ specifically asked for is complete; full slice reduction remains gated on the L3/L4 rows (tracked in `l3-l4-chebyshev-rows-eligible`).

```yaml
---
slug: concepts-state-stratification-four-stratum-extension
opened_at: cycle-011
opened_by: same-layer-cross-cutter
status: answered
answered_at: cycle-012
answered_in: book/src/concepts/state-stratification.md (§Worked example — Chebyshev smoother: a fourth stratum)
relates_to: phase-1-corpus-reduction-audit (priority-19), l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion (this ledger)
---
```

The `book/src/spec/slices/chebyshev.md` §L4 (lines 290-442) establishes a fourth state stratum (scalar-recurrence — per-call ephemeral but threaded across `k`-iterations) beyond the three documented in `book/src/concepts/state-stratification.md` (sim / operator-internal / ephemeral). Specifically the `ChebOp<E, S>` parameterized closure type with `Kind4 :: ChebOp<E, Unit>` and `Kind1 :: ChebOp<E, { rho_prev: E }>` encodes the scalar-recurrence stratum as a type parameter — unique methodology evidence for the "constructed-operator absorbs variant at level (c)" pattern. Should this be lifted as a firm extension to the state-stratification concept (four-stratum split), OR as a sub-kind of operator-internal stratum (the slice's framing: the scalar-recurrence stratum is per-call ephemeral but threaded across iterations, distinguishing it from both pure ephemeral and pure operator-internal strata)? Routing: cycle-012+ layer-intro-author / same-layer-cross-cutter dispatch on `concepts/state-stratification.md` to extend with the four-stratum worked example. Source: cycle-011 phase-1-corpus-reduction-batch-2 §slice-2 residual gap #3.

**Answered cycle-012 (layer-intro-author concept-corrections; applied by integrator-per-report).** Resolved the "four-stratum split vs. sub-kind-of-operator-internal" question in favour of the **four-stratum split**: a new §"Worked example — Chebyshev smoother (slice: chebyshev, L4): a fourth stratum" was appended to `concepts/state-stratification.md` introducing the **scalar-recurrence stratum** as its own category (per-call ephemeral but threaded across the inner `k`-iterations within a single `apply` call — `rho_prev` carried by the inner `foldM`'s `ScalarState`). The extension argues the fourth stratum is distinct from both operator-internal params (does not persist across `apply` calls) and ordinary ephemerals (genuinely cross-iteration data-dependent), made visible at the type level via `ChebOp<E, S>` (`Unit` for 4th-kind, `{ rho_prev: E }` for 1st-kind), and adds a stratum-placement check plus the "three-way split suffices when no inner-loop-threaded scalar" condition (GMRES Givens-register case). Cited to `chebyshev.md:298, :300-321` (the report's currently-correct line numbers; the ledger's older "290-442" range had drifted). Source: cycle-012 layer-intro-author dispatch `reports/2026-05-28T034221Z-layer-intro-author-concept-corrections/CYCLE.md` Task 2.

```yaml
---
slug: concepts-derived-view-hoisting-control-flow-boundary-extension
opened_at: cycle-011
opened_by: same-layer-cross-cutter
status: answered
answered_at: cycle-012
answered_in: book/src/concepts/derived-view-hoisting.md (§Worked example: Chebyshev initial-guess branch (control-flow boundary))
relates_to: phase-1-corpus-reduction-audit (priority-19), l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion (this ledger)
---
```

The `book/src/spec/slices/chebyshev.md` §L4 "Initial-guess shape: branch vs. derived view" section (lines 419-436) is unique methodology evidence for `derived-view-hoisting` applied at the **control-flow boundary** (as distinct from the state-shape boundary that's the typical case for derived-view-hoisting). The slice argues why `initial_guess: Bool` is a per-call argument rather than a constructed-operator variant axis — the branch lives at the control-flow boundary, not the state-shape boundary. The existing `book/src/concepts/derived-view-hoisting.md` worked examples are all state-shape-boundary applications. Lifting target: extend the concept page with the control-flow-boundary worked example, clarifying that derived-view-hoisting can be applied at either boundary. Routing: cycle-012+ layer-intro-author / same-layer-cross-cutter dispatch on `concepts/derived-view-hoisting.md`. Source: cycle-011 phase-1-corpus-reduction-batch-2 §slice-2 residual gap #4.

**Answered cycle-012 (layer-intro-author concept-corrections; applied by integrator-per-report).** A new §"Worked example: Chebyshev initial-guess branch (control-flow boundary)" was inserted into `concepts/derived-view-hoisting.md` (before §"When the rotation applies"), pairing the existing CG state-shape-boundary example with the new control-flow-boundary case. The extension shows the `initial_guess = false` path as the algebraic specialization of the `true` path under `y_in = 0` (a degenerate-case absorption, not a residual variant axis), contrasts the **bad** option (promote `initial_guess` to a constructed-operator variant, inflating the closure-type lattice to four) against the **good** option (keep it a per-call argument), and surfaces the categorical distinction between a per-call flag and a constructed-operator variant — tying back to the [`variant-absorption`](./variant-absorption.md) discipline (avoid over-absorbing). Cited to `chebyshev.md:416-433` (the report's currently-correct line numbers; the ledger's older "419-436" had drifted). Source: cycle-012 layer-intro-author dispatch `reports/2026-05-28T034221Z-layer-intro-author-concept-corrections/CYCLE.md` Task 3.

```yaml
---
slug: concepts-negative-result-slice-partial-positive-sub-pattern-extension
opened_at: cycle-011
opened_by: same-layer-cross-cutter
status: answered
answered_at: cycle-012
answered_in: book/src/concepts/negative-result-slice.md (§Partial-positive sub-pattern)
relates_to: phase-1-corpus-reduction-audit (priority-19), phase-1-corpus-reduction-remaining-7-slices (this ledger)
---
```

The `book/src/spec/slices/polynomial_recurrence_step.md` §L1↔L1 self-tightening section (lines 162-191) is unique methodology evidence for the "**partial-positive-within-a-negative-result-slice**" pattern — a slice that is cross-family negative (no shared kernel between Chebyshev / GMRES / eigenvalue-tracking) AND within-family partially positive (4-of-5-axes-shared between 4th-kind and 1st-kind Chebyshev; refactor potential as `ChebyshevSmootherBase<ScalarGenerator>`). The dedicated falsification criterion subsection (lines 183-191) is also structurally required per `concepts/negative-result-slice.md` §"Falsification criterion (required structural element)". Lifting target: extend `book/src/concepts/negative-result-slice.md` with a "Partial-positive sub-pattern" subsection citing this slice's self-tightening section as the canonical worked example. Until lifted, the polynomial_recurrence_step.md self-tightening section is retained in full (the cycle-011 batch-2 reduction does NOT touch this section). Routing: cycle-012+ layer-intro-author / same-layer-cross-cutter dispatch on `concepts/negative-result-slice.md`. Source: cycle-011 phase-1-corpus-reduction-batch-2 §slice-3 residual gap #4.

**Answered cycle-012 (layer-intro-author concept-corrections; applied by integrator-per-report).** A new §"Partial-positive sub-pattern" subsection was inserted into `concepts/negative-result-slice.md` (between §"Examples in this spec" and §"Falsification criterion (required structural element)"). It documents the outer (cross-family) negative scope coexisting with a nested (within-family) partial-positive scope, kept honest by explicit scoping; gives the `polynomial_recurrence_step` §"L1↔L1 self-tightening" as the canonical worked example (cross-family negative across Chebyshev/GMRES/eigentracking; within-Chebyshev 4-of-5-axes agreement → `ChebyshevSmootherBase<ScalarGenerator>` parametric unification); and codifies a four-point discipline (state the cross-family negative first; scope the within-family positive explicitly; give the partial positive its own falsification criterion; do not promote on a single within-family case). Placement immediately before §"Falsification criterion" is deliberate (the partial-positive's own falsification surface specializes the section that follows). Cited to `polynomial_recurrence_step.md:170-199` (the report's currently-correct line numbers; the ledger's older "162-191" had drifted). Source: cycle-012 layer-intro-author dispatch `reports/2026-05-28T034221Z-layer-intro-author-concept-corrections/CYCLE.md` Task 4.

```yaml
---
slug: orthogonalize-mutation-rotation-l1-l0-theme
opened_at: cycle-012
opened_by: harvester
status: open
relates_to: l1-orthogonalize-promotion-from-arnoldi-step-and-orthog (this ledger, answered cycle-012), scal-mutation-rotation-l1-l0-theme (this ledger)
---
```

No firm `book/src/L1-L0/orthogonalize-mutation-rotation.md` theme exists. The cycle-012 firm `L1/orthogonalize` operator (`book/src/L1/orthogonalize.md`) firms the pure-functional L1 form `(w', H) = orthogonalize(w, V, variant)`, but the L1>L0 mutation-rotation theme — the rewrite narrated forward from L1 to L0 covering (a) the in-place `w` overwrite (`w.Add(-H[j], V[j])`), (b) the raw-pointer `H` write into the caller's Hessenberg-column buffer, and (c) the per-variant collective shape (MGS: `m` reductions of size 1; CGS: 1 of size `m`; CGS2: 2 of size `m`) materialising as `Mpi::GlobalSum` calls — has not been authored. The retained L2 section of the `orthog` slice (`book/src/spec/slices/orthog.md`) is the raw material. **Out of scope for harvester** — L1>L0 theme authoring is `abstractor` / `lifter` territory. **Routing note for cycle-012+ planner**: dispatch an `abstractor` on `orthogonalize-mutation-rotation` — analogous to the firm `ksp-solve-mutation-rotation`, `axpby-mutation-rotation`, and `axpbypcz-mutation-rotation` themes already landed at L1>L0. The theme should narrate the destination-buffer mutation pattern, the raw-pointer coefficient write, the variant-dispatched collective-shape disclosure, and the `dot_op` inner-product-hook substitution. Source: cycle-012 harvester dispatch `reports/2026-05-28T034130Z-harvester-l1-orthogonalize/CYCLE.md` §"Open questions / caveats" item 2 (L1>L0 lowering theme not yet authored).

```yaml
---
slug: concepts-orthogonalization-coefficient-normalisation-drift
opened_at: cycle-012
opened_by: harvester
status: open
relates_to: l1-orthogonalize-promotion-from-arnoldi-step-and-orthog (this ledger, answered cycle-012), concepts-nrm2-stability-claim-correction (this ledger)
---
```

The concept page `book/src/concepts/orthogonalization.md` carries a coefficient/normalisation contradiction with the firm `L1/orthogonalize` entry. The concept page's first concept block (`orthogonalization.md:3`) defines the output coefficient vector as `h = (h_0, …, h_{j+1})` "with `h_{j+1} = ‖w'‖`", folding the normalisation sub-diagonal into the coefficient vector. The firm L1 entry (`book/src/L1/orthogonalize.md` §Context, §Signature) is authoritative: `orthogonalize` returns the **length-`m`** coefficient vector `H[0..m-1]` only; `‖w'‖` is the *caller's* `nrm2` step (witnessed at `palace/linalg/iterative.cpp:631-632, 810-811`: `Hj[j+1] = Norml2(...); w *= 1/Hj[j+1]`), excluded by the L0 header's "does not normalize the output" contract (`orthog.hpp:18-23`). The critic additionally found the concept page is **internally inconsistent**: its second stacked concept block (`orthogonalization.md:29-30`) defines `h_{0..j-1}` and `w' = w − Σ h_i v_i` with **no** normalisation fold-in — so the page contradicts both the L1 entry and itself. **Out of scope for harvester** — concept pages are `layer-intro-author` / cross-cutter territory. **Routing note for cycle-012+ planner**: dispatch a `layer-intro-author` or `same-layer-cross-cutter` refresh on `book/src/concepts/orthogonalization.md:3, :29-30` to (a) remove the `h_{j+1} = ‖w'‖` fold-in from the first block (or reframe it as the caller's separate `nrm2` step), and (b) reconcile the two stacked concept blocks so the coefficient-vector length is consistent. The firm L1 entry is authoritative on the boundary in the meantime. Low-priority cleanup; not blocking any current work. Source: cycle-012 harvester dispatch `reports/2026-05-28T034130Z-harvester-l1-orthogonalize/CYCLE.md` §"Open questions / caveats" item 4 + critic META.md §cross-reference-integrity issue 3.

```yaml
---
slug: chebyshev-slice-rho_0-coefficient-correction
opened_at: cycle-012
opened_by: harvester
status: open
relates_to: l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion (this ledger, answered cycle-012), phase-1-corpus-reduction-remaining-7-slices (this ledger)
---
```

The Phase-1 slice `book/src/spec/slices/chebyshev.md:160` carries a **load-bearing numerical-coefficient error** that the firm cycle-012 Chebyshev entries do NOT inherit. The slice states the 1st-kind initial `rho_0 = delta / (2*theta)`. The L0 source is `rhop = delta / theta` (`palace/linalg/chebyshev.cpp:282`) — **no factor of 2**. The discrepancy is isolated to the `rho_0` initialiser: the slice's `alpha_0 = 1/theta` matches the source (`:281`). The critic independently confirmed the source value via `read_range`. The firm `L1/chebyshev-smoother` and `L2/chebyshev-iteration` entries use the **correct source value** (`δ/θ`); the erroneous `delta/(2*theta)` line persists only in the as-yet-unreduced slice. **Routing note**: when `book/src/spec/slices/chebyshev.md` is further reduced (this cycle-012 firm landing unblocks that reduction per `l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion`), correct or drop the erroneous `:160` line so the wrong coefficient does not survive into the (eventually authoritative) reduced slice. Not editable by this harvester (slice is not its authority; one-operator discipline). Source: cycle-012 harvester dispatch `reports/2026-05-28T034154Z-harvester-chebyshev-l1-l2/CYCLE.md` §"Open questions / caveats" item 1 + critic META.md §citation-validity (rho_0 discrepancy CONFIRMED).

```yaml
---
slug: spectrum_estimate-l1-rough-in-opacity
opened_at: cycle-012
opened_by: harvester
status: open
relates_to: l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion (this ledger, answered cycle-012), matrix-weighted-norm-and-bilinear-form-l1-rough-ins (this ledger)
---
```

The setup-side `spectrum_estimate(A, dinv)` sub-action is cited as an **opaque L1 dependency** of the firm `L1/chebyshev-smoother` but has no firm L1 entry of its own. At L0 it is `GetLambdaMax(comm, A, dinv) → linalg::SpectralNorm(comm, DinvA, hermitian)` (`palace/linalg/chebyshev.cpp:13-27`) — the power-iteration (SLEPc-backed when configured) dominant-eigenvalue estimate of `D⁻¹ A`. It is the `linalg::SpectralNorm` power-iteration sibling tracked under the cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` residual cohort. **Routing note for cycle-012+ planner**: a future harvester on `spectrum_estimate` (the `SpectralNorm` power-iteration primitive) would let `chebyshev-smoother`'s setup dependency point at a concrete L1 entry rather than naming it opaque; it would also serve the matrix-weighted-norm cohort. Source: cycle-012 harvester dispatch `reports/2026-05-28T034154Z-harvester-chebyshev-l1-l2/CYCLE.md` §"Open questions / caveats" item 2.

```yaml
---
slug: l3-l4-chebyshev-rows-eligible
opened_at: cycle-012
opened_by: harvester
status: open
relates_to: l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion (this ledger, answered cycle-012), phase-1-corpus-reduction-remaining-7-slices (this ledger)
---
```

The cycle-012 firm landing fired the L1 (`chebyshev-smoother`) and L2 (`chebyshev-iteration`) Chebyshev rows, but the slice `book/src/spec/slices/chebyshev.md` also carries firm **L3** (partial-obstruction; `chebyshev.md:229-440`) and **L4** (calculus; the L4 form is already drafted in the slice with `ChebOp<E, S>` typing and `foldM`/`forM_` monadic shape) Chebyshev content. Per the **identity-lowerings still require both L levels** invariant and the **lower-layer shared vocabulary takes priority** directive (CLAUDE.md §Methodology invariants), `L3/chebyshev-iteration` and `L4/chebyshev-smoother` are eligible future harvester targets. **The slice cannot fully reduce until L3/L4 are also lifted** — this blocks full `chebyshev.md` reduction. **Routing note for cycle-012+ planner**: schedule a harvester on `L3/chebyshev-iteration` (sequential-obstruction partial-obstruction form; the `k`-recurrence and `pc_it`-sweep sequentiality recorded in the L2 non-laws are its root) and on `L4/chebyshev-smoother` (the `ChebOp<E, S>` monadic-wrapper form). Out of scope for this 2-operator dispatch. Source: cycle-012 harvester dispatch `reports/2026-05-28T034154Z-harvester-chebyshev-l1-l2/CYCLE.md` §"Open questions / caveats" item 3.

```yaml
---
slug: chebyshev-l1-l0-and-l2-l1-lowering-themes
opened_at: cycle-012
opened_by: harvester
status: open
relates_to: l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion (this ledger, answered cycle-012), orthogonalize-mutation-rotation-l1-l0-theme (this ledger)
---
```

The cycle-012 firm landing fired the L1 and L2 Chebyshev *operator* rows; the forward **lowering themes** between them are not yet authored — both are `abstractor` candidates. (1) `L1-L0/chebyshev-smoother-mutation-rotation` — the `Mult2` output-arg / workspace mutation rotation: the in-place `y` overwrite, the scribbled `r`/`d` workspaces, the construction-bound `lambda_max`/`theta`/`delta` reads, and the `SetOperator`/`Mult2` split. Analogous to the firm `ksp-solve-mutation-rotation` / `axpby-mutation-rotation` / `axpbypcz-mutation-rotation` themes. (2) `L2-L1/chebyshev-iteration-fusion` — the `ApplyOrder0`/`ApplyOrderK` element-fusion theme: narrates the de-fusion of the HPC element-fused kernels (one elementwise pass `d ← sd·d + sr·dinv·r`) into the base `scal`/`elementwise_product`/`axpby` composition, classifying the fusion as a transparent performance trick (with the bit-determinism non-law called out as load-bearing for reproduction). **Out of scope for harvester** — L1>L0 and L2>L1 theme authoring is `abstractor`/`lifter` territory. The firm L1 entry references the forthcoming L1>L0 theme in prose without linking a non-existent file. Source: cycle-012 harvester dispatch `reports/2026-05-28T034154Z-harvester-chebyshev-l1-l2/CYCLE.md` §"Open questions / caveats" item 5.

```yaml
---
slug: eigsolve-getconverged-forwarder-fix-and-gated-promotion
opened_at: cycle-012
opened_by: lowering-verifier
status: open
relates_to: orthogonalize-mutation-rotation-l1-l0-theme (this ledger), partly-constructive theme-status codification (cycle-012 meta-phase; recurrence-2)
---
```

The cycle-012 `lowering-verifier` audit of the `eigsolve-mutation-rotation` L1>L0 theme (`book/src/L1-L0/eigsolve-mutation-rotation.md`) returned **confirms-with-refinement** and **UNBLOCKS but does NOT enact** the Sub-pattern B partly-constructive → fully-firm promotion. The promotion is **GATED on a cycle-013 `abstractor` dispatch** applying the Sub-pattern B materialisation-snippet correction first (audit Edit 2, NOT applied by the verifier per role discipline): the snippet currently reads `if (!opInv->GetConverged())`, but `GetConverged()` is **not** on `opInv`'s type (`ComplexKspSolver = BaseKspSolver<ComplexOperator>`) public surface — it exists only on `IterativeSolver` (`iterative.hpp:98`), reached internally via the protected `ksp` member inside `BaseKspSolver::Mult` (`ksp.cpp:301`). The fix is a one-line public forwarder on `BaseKspSolver` mirroring the existing `GetRelTol()` forwarder at `ksp.hpp:64` (`bool GetConverged() const { return ksp->GetConverged(); }`), OR changing `Mult` to return status instead of `void`. The audit Edit 2 also tightens the prose immediately after the snippet to make the required forwarder explicit. **Fold into the same cycle-013 abstractor dispatch (audit Edit 3, also NOT applied by the verifier): Sub-pattern A function-name attribution fix** — the per-`WhichType` switch with the `MFEM_ABORT` for unimplemented TARGET_REAL/TARGET_IMAGINARY is attributed in the theme prose + citation list to `ArpackEigenvalueSolver::SetWhichEigenpairs`, but it actually lives in `ArpackEigenvalueSolver::SolveInternal` (the `SetWhichEigenpairs` body at `arpack.cpp:236-239` is a trivial `which_type = type` field-set; the switch + abort are in `SolveInternal` at ~280-307, abort at ~302-304). The cited range 236-308 covers both, so the citation is in-range; only the function-name label is imprecise. **Required sequence**: (1) the cycle-013 abstractor applies Edit 2 (GetConverged forwarder snippet/prose correction) and Edit 3 (Sub-pattern A attribution label fix) to the theme; (2) ONLY THEN is the `partly-constructive` caveat dropped and the theme `## Status` promoted to fully-firm per the theme's own promotion gate (b). The integrator did NOT auto-promote the theme this cycle — the `## Status` line remains `firm (structural; partly-constructive on Sub-pattern B ...)`. The ncv-clamp citation-drift (theme applicability-condition 4 cited `arpack.cpp:521-525`; actual clamp `if (ncv > N) {...}` is at 518-520 with `N=GlobalSize(...)` at 517 and the `arpack_it` default at 522-525) was already corrected in the audit's appended machine-readable `verified_against:` block (`citation: palace/linalg/arpack.cpp:518-520`); the abstractor may additionally align the inline applicability-condition-4 prose if it touches that paragraph. Source: cycle-012 lowering-verifier dispatch `reports/2026-05-28T034311Z-lowering-verifier-eigsolve-mutation-rotation/CYCLE.md` §"Proposed changes" Edits 2-3 + §"Open questions / caveats" "Sub-pattern B promotion verdict (GATED)" + critic META.md issues 1, 5, 7. (Audit + this OQ were authored in cycle-012; the gated follow-up `abstractor` dispatch is routed to cycle-013, the next primary cycle.)

```yaml
---
slug: eigsolve-nep-coordinate-convention-empirical-witness
opened_at: cycle-012
opened_by: lowering-verifier
status: open
priority: low
relates_to: eigsolve-slepc-nep-coordinate-convention-audit (this ledger, answered cycle-012)
---
```

Low-priority empirical-witness gap surfaced by the cycle-012 SLEPc-NEP coordinate-convention audit (`reports/2026-05-28T034311Z-lowering-verifier-slepc-nep-coordinate-convention/`). The audit's verdict (NEP solves the original un-scaled problem directly; `return l` is correct; the NEP `SetOperators` gamma/delta are a dead store w.r.t. the coordinate transform; convention (b) holds uniformly across all four backends) rests on **direct source-read of the control flow** — the raw-operator function/jacobian callbacks (`slepc.cpp:2170-2202`), the un-scaled `NEPSetTarget(nep, sigma)` (`:1503`), and the un-scaled residual path (`:1760-1798`) — plus an exhaustive `search_text` for `gamma|delta` in the NEP region confirming the only hits are the dead `SetOperators` store and the independent `GetBackwardScaling` norm recomputation. There is **no `test-eigensolver.cpp` NEP case** that constructs a known-eigenvalue NEP and asserts the returned eigenvalue is in original-problem coordinates; the reading is `source-read-confirmed, empirically-unwitnessed`. Recommended (low-priority): if a future harvester firms up a `SlepcNEPSolver` L0 entry, or if a dedicated `test-eigensolver.cpp` NEP case lands, upgrade the §5 NEP convention claim from source-read-confirmed to empirically-witnessed. Related latent question (not separately filed, below the per-cycle problems-bar): *why* does NEP compute gamma/delta at all if they are unused — genuinely dead (vestigial copy-adaptation from `SlepcPEPSolver::SetOperators`) vs. latent (intended for a future `NEPSetScale`-style wiring never completed)? Either reading leaves the current coordinate-convention verdict unchanged. Source: cycle-012 lowering-verifier dispatch §"Open questions / caveats" items 1-2.

```yaml
---
slug: partly-constructive-to-firm-promotion-route-ratification
opened_at: cycle-013
opened_by: integrator-per-report
last_revisited: null
status: open
relates_to: eigsolve-getconverged-forwarder-fix-and-gated-promotion (this ledger, answered cycle-013), partly-constructive theme-status codification (cycle-012 meta-phase)
route_to: cycle-015 meta-phase
---
```

**The first live `partly-constructive` → `firm` promotion landed cycle-013; the methodology route it invoked needs the cycle-015 meta-phase to consciously ratify the mechanism (do not let the precedent be silently inherited).** Cycle-013 promoted `book/src/L1-L0/eigsolve-mutation-rotation.md` Sub-pattern B from `firm (structural; partly-constructive on Sub-pattern B LinearSolveFailed materialisation)` to `firm (structural)`. The critic (META.md Issue 2, MEDIUM) and repairer (`unrepairable`, escalated) flagged that this is the **first live exercise** of the `partly-constructive` → `firm` mechanism the cycle-012 meta-phase codified, and the promotion rests on an **interpretive adjudication** that should be ratified by integrator/meta-phase rather than baked in by a producer (abstractor) dispatch. The integrator-per-report **applied the promotion as a deliberate, flagged decision** (per the accumulate-surface-with-embedded-friction invariant: needs-revision is NOT reject → the diff applies) and routes the methodology-route question forward. Two points the cycle-015 meta-phase must ratify or refine, so the precedent is set on the record for every future `partly-constructive` → `firm` promotion:

1. **The "firm = no open promotion condition + structural decomposition confirmed" reading of the invariant's "Do NOT mark such an entry `firm`" clause.** After this pass the constructive sub-part `LinearSolveFailed` STILL has only negative-anchor support (Palace's `void`-returning `Mult` at `ksp.cpp:297-310` is unchanged; the forward-looking-reconstruction note stays in prose). The CLAUDE.md invariant's motivating condition "(i) a constructive sub-part has only negative-anchor support" remains true; only condition "(ii) an open promotion condition remains" is argued closed. The report dissolves the literal "Do NOT mark firm" clause by reading "firm" as "no open promotion condition + structure confirmed." Defensible, but interpretive — ratify or refine.

2. **Reconciliation of the two promotion routes.** The CLAUDE.md invariant enumerates a "**per-line** lowering-verifier audit" (an evidence-upgrade route) as the promotion path; the theme's own `## Status` gate option (b) — the one actually invoked — is "a lowering-verifier audit that confirms the partly-constructive **shape is acceptable as a methodology-level pattern**" (a methodology-acceptance route). The cycle-012 audit did the latter (confirmed structure + identified firming edits + supported the meta-phase codification), not a per-line evidence-upgrade of `LinearSolveFailed` to a positive site. The meta-phase should reconcile these two routes.

The protocol itself worked cleanly as a TWO-dispatch pattern — (i) cycle-012 lowering-verifier confirmed + identified the exact firming edits (UNBLOCK), (ii) the cycle-013 abstractor applied the edits + dropped the gate (ENACT), with the audit's literal gate satisfied (Edit 2 / GetConverged forwarder snippet APPLIED this pass, not deferred). The meta-phase may wish to note this two-dispatch protocol as the canonical precedent. Cosmetic residual (does not affect the verdict): the ncv-clamp full `if`-block is `arpack.cpp:518-521` (the audit YAML phrased it `518-520`, assignment-inclusive/brace-exclusive) — both defensible; the integrator cited `518-521` for the full block in applicability-condition 4. Source: cycle-013 abstractor dispatch `reports/2026-05-28T143232Z-abstractor-eigsolve-getconverged-forwarder-fix-and-gated-promotion/CYCLE.md` §"Promotion judgment" + §"Open questions / caveats" items 1-2 + META.md Issue 2 / Unrepairable findings.

```yaml
---
slug: eigsolve-mutation-rotation-embedded-audit-yaml-resolution-marker
opened_at: cycle-013
opened_by: integrator-per-report
last_revisited: null
status: open
priority: low
relates_to: eigsolve-getconverged-forwarder-fix-and-gated-promotion (this ledger, answered cycle-013)
---
```

**Historical-record hygiene (low priority, optional cleanup):** after the cycle-013 promotion, `book/src/L1-L0/eigsolve-mutation-rotation.md` carries a `firm (structural)` `## Status` section but the embedded cycle-012 lowering-verifier audit YAML block (the `### Machine-readable audit record` section) still carries the pre-fix `partially-supports` entries on `ksp.hpp:30-72` and `arpack.cpp:236-308`, plus the now-superseded ncv-clamp `518-520` phrasing, with no `resolved cycle-013` cross-link. A reader hitting the YAML first may read the gate as still-open. The cycle-013 abstractor (Open Question #3) deliberately left the audit YAML untouched to avoid falsifying the historical audit record — a reasonable choice. Optional future cleanup: append a single one-line `resolved cycle-013` marker (a header line on the audit block, or a note on the three affected YAML entries) so the firm status and the embedded audit do not appear to conflict. Not blocking; flagged for a future cleanup dispatch or the cycle-015 meta-phase. Source: cycle-013 abstractor dispatch §"Open questions / caveats" item 3 + critic META.md Issue 3.

```yaml
---
slug: divfree-weakdiv-sign-convention-l0-verify
opened_at: cycle-013
opened_by: harvester
last_revisited: cycle-015
status: resolved
relates_to: divfree-projector L1 entry (book/src/L1/divfree-projector.md, harvested cycle-013), book/src/spec/slices/divfree.md:135-140 (slice precursor flag), divfree-projector-status-adjudication (this ledger, cycle-013)
---
```

**The additive `+Grad·ψ` correction in `divfree_project` (and the idempotence law `P∘P=P` and the divergence-free output characterization that depend on it) is contingent on an UNVERIFIED reading of the `MixedVectorWeakDivergenceIntegrator` internal sign convention.** `book/src/L1/divfree-projector.md` step 4 (`palace/linalg/divfree.cpp:177-186`, `Grad->AddMult(ψ, y, 1.0)`, `+1.0`) is *additive*, yet the in-`.cpp` intent comment (`palace/linalg/divfree.cpp:177`, `// Compute the irrotational portion of y and subtract.`) says *subtract*, and the class-doc characterizes the output as divergence-free (`palace/linalg/divfree.hpp:28-31`, `Gᵀ M x = 0`) while the `Mult` declaration comment (`palace/linalg/divfree.hpp:63-66`) says "irrotational portion … ∇×y=0" — the complementary subspace. These three statements (additive code, "subtract" comment, divergence-free class-doc) are reconcilable **only if** `WeakDiv` (built from `MixedVectorWeakDivergenceIntegrator`, `palace/linalg/divfree.cpp:113`) internally carries the negating sign, i.e. `WeakDiv ≈ −(divergence)` so that `Grad·ψ = −(irrotational part of y)` and `y + Grad·ψ` removes the irrotational part. That sign lives in the MFEM-vendored integrator, **below the L0 scope boundary** — it is NOT confirmed from a positive Palace source site. Resolving it requires a `verify-citation-range` pass on the `MixedVectorWeakDivergenceIntegrator` definition. This is the **promotion condition** that would lift `book/src/L1/divfree-projector.md` from `partly-constructive` to `firm` (see `divfree-projector-status-adjudication` below). Source: cycle-013 harvester dispatch `reports/2026-05-28T143548Z-harvester-l1-divfree-projector-promotion/CYCLE.md` §"Open questions / caveats" item 1 + critic META.md Issues 2-3.

```yaml
---
slug: divfree-projector-l1-l0-lowering-verifier-followup
opened_at: cycle-013
opened_by: harvester
last_revisited: null
status: open
relates_to: divfree-weakdiv-sign-convention-l0-verify (this ledger, cycle-013), divfree-projector L1 entry (book/src/L1/divfree-projector.md), future L1-L0/divfree-projector-mutation-rotation theme
---
```

**The future `L1-L0/divfree-projector-mutation-rotation` theme must carry a `lowering-verifier` audit that resolves the three-way `irrotational`/`subtract`/additive-code contradiction by anchoring the `WeakDiv` sign.** The `divfree_project` L1 entry adopts the class-doc divergence-free reading (`palace/linalg/divfree.hpp:28-31`) and reads the `Mult`-declaration comment (`palace/linalg/divfree.hpp:63-66`, "irrotational portion … ∇×y=0") and the in-apply comment (`palace/linalg/divfree.cpp:177`, "subtract") as describing the *removed* component rather than the output. The discrepancy does not change the L1 signature or laws but is a documentation-fidelity caveat whose resolution is folded into the WeakDiv-sign OQ above (resolving the sign resolves the contradiction — the additive `+1.0` + "subtract" + divergence-free output are mutually consistent IFF `WeakDiv` negates). The `lowering-verifier` (not the harvester or the integrator) is the role that adjudicates the sign when the L1>L0 theme is authored; this OQ tracks that follow-up. The two OQs (sign + contradiction) are linked: resolving `divfree-weakdiv-sign-convention-l0-verify` resolves this one. Source: cycle-013 harvester dispatch §"Open questions / caveats" item 2 ("Header-comment vs class-doc characterization (NEW)" + "Third in-`.cpp` anchor (added on repair)") + critic META.md Issue 2.

```yaml
---
slug: divfree-projector-status-adjudication
opened_at: cycle-013
opened_by: integrator-per-report
last_revisited: null
status: open
relates_to: divfree-weakdiv-sign-convention-l0-verify (this ledger, cycle-013), divfree-projector L1 entry (book/src/L1/divfree-projector.md), partly-constructive theme-status codification (cycle-012 meta-phase), partly-constructive-to-firm-promotion-route-ratification (this ledger, cycle-013)
route_to: cycle-015 meta-phase (informational — second live partly-constructive instance)
---
```

**Cycle-013 integrator-per-report adjudicated `book/src/L1/divfree-projector.md` as `partly-constructive` (NOT the harvester's argued `firm`); this is the SECOND live `partly-constructive` instance and is recorded for the cycle-015 meta-phase alongside the eigsolve promotion-route ratification.** The harvester argued `firm` on the grounds that the sign convention is "a property of the constructed operators, not a reconstructed sub-part." The critic (META.md Issue 4, MEDIUM) and repairer (`unrepairable`, escalated for status adjudication) flagged that the idempotence law `P∘P=P` and the divergence-free output characterization both *depend on* the unverified `WeakDiv ≈ Gᵀ M` sign reading, whose promotion condition (a `verify-citation-range` / `lowering-verifier` pass on `MixedVectorWeakDivergenceIntegrator`) matches the cycle-012 `partly-constructive` mold exactly. **Adjudication reasoning:** per the cycle-012-codified invariant, a *load-bearing* sub-law (here idempotence, which the harvester itself lists among the laws justifying firmness) that is contingent on an *unresolved reading* rather than a *positive source confirmation* is `partly-constructive`, not plain `firm`. The dispatch directed the integrator to lean `partly-constructive` unless the report's evidence showed the sign is confirmed from a positive source site — and the report's own Evidence + Open-Questions explicitly state the sign is read from the integrator's internal convention, below the L0 scope boundary, and is *unverified*. The structure being fully read satisfies the "firm in structural decomposition" half but NOT the "constructive sub-part has positive support" half. Applied as `partly-constructive` with: (i) constructive sub-part = the idempotence law `P∘P=P` (+ divergence-free output characterization); (ii) negative anchor = no positive Palace site exhibits the `WeakDiv` sign, only the integrator internals; (iii) promotion condition = `divfree-weakdiv-sign-convention-l0-verify` resolved via verify-citation-range on `MixedVectorWeakDivergenceIntegrator`, folded into the `divfree-projector-l1-l0-lowering-verifier-followup` audit. This second live instance (after cycle-013's eigsolve-mutation-rotation Sub-pattern B) is informational input for the `partly-constructive-to-firm-promotion-route-ratification` cycle-015 meta-phase review: it exercises the *entry-into* `partly-constructive` (a producer argued `firm`, the integrator adjudicated down), complementing the eigsolve case which exercised the *exit-from* (`partly-constructive` → `firm` promotion). The dep-map row in `book/src/L1/index.md` and the entry's `## Status` section both carry the `partly-constructive` status + named sub-part + promotion condition. Source: cycle-013 harvester dispatch §"Status" (argued firm) + critic META.md Issue 4 + repairer Unrepairable findings (Issue 4 escalation) + integrator-per-report adjudication.

```yaml
---
slug: chebyshev-l4-wrapper-iteration-vocabulary-reconcile
opened_at: cycle-013
opened_by: repairer
last_revisited: null
status: open
relates_to: book/src/L4/chebyshev.md (§Status — rough-in wrapper caveat), book/src/L4/iterate-while.md (line 7 — canonical iteration primitive, names Chebyshev as consumer), book/src/L4/iterate-while-with-prev.md, book/src/design/l4_calculus.md (§6 bounded-loop → iterate_while_pure), book/src/L4/index.md (chebyshev dep-map row + Rough-in-at-L4 cohort), book/src/spec/slices/chebyshev.md:289,325,396-397 (the promoted pre-redirect forM_/foldM)
route_to: combinator-miner (alternatively lifter) — cycle-013+ follow-up dispatch; firming condition for the L4 chebyshev entry (rough-in → firm)
---
```

**[REPAIRER-OPENED, cycle-013 — OQ 6] The L4 `chebyshev` entry renders its two sequential obstructions as `forM_` (outer `pc_it`) and `foldM` (inner `k`) binds, which are un-anchored at L4 and compete with the firm canonical `iterate-while` family. This is the firming condition: the L4 chebyshev entry landed `rough-in` (firm at the body, rough-in at the wrapper); it promotes to `firm` once the wrapper iteration vocabulary is reconciled.** `forM_`/`foldM` have no L4 dep-map row and no concept page; `iterate-while.md:7` declares itself the "canonical iteration primitive at L4" and **explicitly names Chebyshev as one of its consumers**, and the strawman §6 maps bounded loops to `iterate_while_pure` with a step-count predicate. The `forM_`/`foldM` rendering is a faithful verbatim promotion of the cycle-001-era pre-redirect slice §L4 (`book/src/spec/slices/chebyshev.md:289, 325, 396-397`), but the promotion did NOT reconcile the slice's combinators against the now-firm `iterate-while`/`iterate-while-with-prev` family (both cycle-007 firm). The repairer downgraded the entry `firm` → `rough-in` because the reconciliation is substantive re-authoring (re-expressing the bounded `forM_`/`foldM` — including the `foldM` 3-tuple `(r, d, st)` accumulator with embedded `modifyY` effects — in terms of the `iterate-while` family requires re-deriving the monadic body shape, not a mechanical name swap), which exceeds repair authority. **Follow-up dispatch (combinator-miner or lifter)** should EITHER (i) re-express the bounded loops via `iterate_while_pure` / `iterate-while-with-prev` with step-count predicates (strawman-conformant; reuses canonical vocabulary), OR (ii) anchor `forM_`/`foldM` as their own firm L4 rows with a justification for a second iteration vocabulary alongside `iterate-while`. On reconciliation, the entry firms, the index row + Rough-in-at-L4 cohort note are updated (the entry moves into "Firm at L4", bumping the count to 4), the wrapper caveat is dropped, and the `iterate-while.md:7` "Chebyshev reduces to iterate_while" claim is satisfied or explicitly amended. The L3 `chebyshev` entry's `forM_`/`foldM` references render as tail recursions over static ranges and are NOT the concern (L3 has no `iterate-while` row to compete with) — re-touch only if the follow-up changes the L4 wrapper shape. Source: cycle-013 harvester dispatch §"Open questions / caveats" item 6 (repairer-opened) + critic META.md Issue 1 + repairer Unrepairable findings.

```yaml
---
slug: chebyshev-l4-l3-dedicated-theme-file
opened_at: cycle-013
opened_by: harvester
last_revisited: null
status: open
relates_to: book/src/L4/chebyshev.md, book/src/L3/chebyshev.md, book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (the wrapper-dissolution shape precedent)
route_to: lowering-verifier (low priority; cycle-013+ planner / OQ ledger)
---
```

**[OQ 1] L4>L3 chebyshev theme file (not authored).** The cycle-013 dispatch annotates the L4>L3 wrapper-dissolution **in-line** in both the L4 and L3 chebyshev entries (it is the same value-thread-isomorphic-body shape the `krylov-step-typed-wrapper-dissolution` theme catalogs). If the lowering-verifier wants a dedicated audit anchor for the chebyshev edge specifically (e.g., to confirm the `forM_`/`foldM`-to-tail-recursion dissolution is information-preserving and the `Read`/`ReadWrite` demotion is faithful), a thin `book/src/L4-L3/chebyshev-typed-wrapper-dissolution.md` could be added in a later cycle. Low-priority — not blocking, because the krylov-step theme establishes the wrapper-dissolution shape and the chebyshev body is identity-in-form on the same vocabulary. Note this OQ may merge with / be reshaped by the OQ-6 wrapper-vocabulary reconciliation (if the wrapper shape changes, the dedicated theme would document the reconciled form). Source: cycle-013 harvester dispatch §"Open questions / caveats" item 1.

```yaml
---
slug: chebyshev-phase1-slice-reduction
opened_at: cycle-013
opened_by: harvester
last_revisited: null
status: open
relates_to: book/src/spec/slices/chebyshev.md (the slice to reduce), book/src/L1/chebyshev-smoother.md, book/src/L2/chebyshev-iteration.md, book/src/L3/chebyshev.md, book/src/L4/chebyshev.md, book/src/concepts/chebyshev-iteration.md, skills/phase-1-slice-reduction-audit, book/src/concepts/state-stratification.md, book/src/concepts/derived-view-hoisting.md
route_to: same-layer-cross-cutter (cycle-013+ slice-reduction audit, using skills/phase-1-slice-reduction-audit); concept-page extensions to layer-intro-author
---
```

**[OQ 2] Phase-1 slice reduction unblocked for `chebyshev`.** With the L3 and L4 chebyshev rows landed (this cycle), all four layered representations of the Chebyshev smoother are firm / partial-obstruction (L1 cycle-012, L2 cycle-012, L3+L4 cycle-013). The slice `book/src/spec/slices/chebyshev.md` is now fully represented in the layered artifact. Per the CLAUDE.md invariant **Phase 1 corpus reduces as material is lifted**, a follow-up `same-layer-cross-cutter`-scoped dispatch (using `skills/phase-1-slice-reduction-audit`) should verify START+END boundary coverage and reduce the slice to a stub pointing at the firm layered entries (`L1/chebyshev-smoother`, `L2/chebyshev-iteration`, `L3/chebyshev`, `L4/chebyshev`, `concepts/chebyshev-iteration`). **Residual coverage check**: the slice's §L4 four-stratum worked example (sim / operator-internal / ephemeral / scalar-recurrence) and the control-flow-boundary derived-view example were flagged at the slice's reduction-status header (lines 13-14) as candidate extensions to `concepts/state-stratification.md` and `concepts/derived-view-hoisting.md`; the L4 entry references both but does not author the concept-page extensions (that is layer-intro-author's domain). The slice-reduction audit must note this so the concept extensions are not lost on reduction. Caveat: the L4 chebyshev entry is `rough-in` pending OQ 6 — the slice-reduction audit should confirm the slice §L4's forM_/foldM treatment is not needed as a residual reference before fully reducing (or reduce to a stub that survives the OQ-6 reconciliation). Source: cycle-013 harvester dispatch §"Open questions / caveats" item 2.

```yaml
---
slug: partial-obstruction-status-codification
opened_at: cycle-013
opened_by: harvester
last_revisited: null
status: open
relates_to: book/src/L3/chebyshev.md (first firm layered L3 entry to carry partial-obstruction), book/src/spec/slices/*.md §L3 sections (informal prior use), partly-constructive theme-status codification (cycle-012 meta-phase), book/src/concepts/sequential-obstruction.md
route_to: cycle-015 meta-phase (methodology-note — candidate first-class status value alongside firm/rough-in/obstruction/partly-constructive)
---
```

**[OQ 3] `partial-obstruction` status precedent.** The L3 chebyshev entry is marked `partial-obstruction` (body lifts, loop does not). This is distinct from the cycle-012-codified `partly-constructive` status (firm structure + a negative-anchor-backed constructive sub-part). `partial-obstruction` is the honest L3 verdict for a fixed-degree smoother and is the status the slice's §L3 header already used informally ("partial obstruction"). If the meta-phase wants `partial-obstruction` codified alongside `firm`/`rough-in`/`obstruction`/`partly-constructive` as a first-class L3 status value, that is a methodology note for the cycle-015 meta-phase — flagged here, not enacted. (It is already in use informally at the slice level and at `book/src/spec/slices/*` §L3 sections; `book/src/L3/chebyshev.md` is the first firm *layered* L3 entry to carry it.) Source: cycle-013 harvester dispatch §"Open questions / caveats" item 3.

```yaml
---
slug: chebyshev-l3-l4-layer-intro-refresh
opened_at: cycle-013
opened_by: harvester
last_revisited: null
status: open
relates_to: book/src/L3/index.md (intro lines 1-16), book/src/L4/index.md (vocabulary-cohort prose lines 30-43), book/src/L3/chebyshev.md, book/src/L4/chebyshev.md
route_to: layer-intro-author (cycle-013+ follow-up)
---
```

**[OQ 4] Layer-intro refresh (note for layer-intro-author).** The L3 `index.md` intro (`book/src/L3/index.md:1-16`) and the L4 `index.md` vocabulary-cohort prose (`book/src/L4/index.md` Semantics-overlay + cohort) will want a refresh now that the chebyshev rows have landed: the L3 intro should mention that the layer now carries its first partial-obstruction operator (not just clean lifts + the krylov-step non-lift), and the L4 cohort prose should note the bounded-`forM_`/`foldM` iteration shape (currently rough-in, pending OQ 6) alongside the `iterate-while` family. The harvester deferred this per the "do not update layer intros" discipline; the integrator added the dep-map rows + a "Rough-in at L4" cohort note + an L3 Working-Notes bullet this cycle, but the narrative intro/overlay prose refresh is layer-intro-author's domain. Source: cycle-013 harvester dispatch §"Open questions / caveats" item 4.

```yaml
---
slug: dependency-map-orthog-plane-rotation-stale-edge-prune
opened_at: cycle-013
opened_by: layer-intro-author
last_revisited: null
status: open
relates_to: book/src/concepts/dependency-map.md:188 (mermaid concept-DAG edge `orthog --> plane-rotation-stream`), book/src/spec/slices/orthog.md (post-cycle-012-reduction scope = block Gram-Schmidt only), book/src/spec/slices/plane_rotation_stream.md (canonical plane-rotation-stream slice)
route_to: layer-intro-author or same-layer-cross-cutter (dependency-map-maintenance pass)
---
```

**[OQ 5] Stale concept-graph edge `orthog --> plane-rotation-stream` (dependency-map maintenance).** `book/src/concepts/dependency-map.md:188` carries a mermaid concept-DAG dependency arrow `orthog --> plane-rotation-stream`. After cycle-012's phase-1 corpus-reduction batch-3 the `orthog` slice no longer contains the plane-rotation stream (reduced to a stub pointing at `plane_rotation_stream.md`), so this edge is **stale-in-spirit** — the dependency it encodes (orthog depends-on/contains the plane-rotation stream) no longer holds. This is distinct from the three canonical-anchor *file pointers* repointed this cycle (`plane-rotation-stream.md:37`, `givens_generate.md:27`, `givens_apply.md:27`): line 188 is a bare-node concept-graph arrow, NOT a `[text](../spec/slices/*.md)` markdown link, so resolving it is a concept-graph modeling decision (delete the edge vs. re-source it, e.g. `gmres --> plane-rotation-stream`), not a surgical pointer swap. Deferred to a future dependency-map-maintenance pass that audits `orthog`'s out-edges against the post-reduction concept graph. The canonical node's own out-edges (`dependency-map.md:165/186/187/194/248`) are already correct. Repairer-flagged + critic-flagged (cross-reference-integrity warning), explicitly held out of the clean pointer-swap scope. Source: cycle-013 layer-intro-author dispatch §"Open questions / caveats" (repairer-added) + critic Issue 1.

```yaml
---
slug: plane-rotation-givens-l0-citation-range-reconcile
opened_at: cycle-013
opened_by: layer-intro-author
last_revisited: null
status: open
relates_to: book/src/concepts/givens_generate.md:23, book/src/concepts/givens_apply.md:23 (cite palace/linalg/gmres.cpp:GeneratePlaneRotation/:ApplyPlaneRotation — likely stale), book/src/concepts/givens.md:33-34 (cites palace/linalg/iterative.cpp:73-108/:227-241), book/src/spec/slices/plane_rotation_stream.md:7 (names this OQ), book/src/spec/slices/orthog.md:227 (flags former gmres.cpp L0 citations likely stale)
route_to: layer-intro-author or harvester via verify-citation-range (codemap get_symbol_def on GeneratePlaneRotation/ApplyPlaneRotation)
---
```

**[OQ 6] Givens L0 citation-range reconcile (`gmres.cpp` → `iterative.cpp`).** The two `givens_*` concept pages cite the plane-rotation primitives at `palace/linalg/gmres.cpp:GeneratePlaneRotation` / `:ApplyPlaneRotation` (`givens_generate.md:23`, `givens_apply.md:23`), but the firm `givens.md:33-34` cites them at `palace/linalg/iterative.cpp:73-108` / `:227-241` and `plane_rotation_stream.md` cites `iterative.cpp:72-108` / `:226-242`. Palace appears to have moved the primitives into `iterative.cpp` (`orthog.md:227` already flags "the former L0 citations here pointed at `gmres.cpp` (likely stale)"). This is a citation-range/file reconciliation — distinct from this cycle's slice-pointer repoint — needing a `verify-citation-range` pass (codemap `get_symbol_def` on `GeneratePlaneRotation` / `ApplyPlaneRotation` to confirm the current file + line range). Named at `plane_rotation_stream.md:7`; left untouched by the cycle-013 surgical repoint to keep that a clean pointer swap. Source: cycle-013 layer-intro-author dispatch §"Open questions / caveats" item 1.

```yaml
---
slug: l4-preconditioning-framework-promotion
opened_at: cycle-013
opened_by: same-layer-cross-cutter
last_revisited: null
status: open
relates_to: book/src/spec/slices/cg_preconditioning_framework.md (§L4 lines 293–412, §L4 v0.2 lines 413–471, §L4 v0.3 lines 472–533 — retained load-bearing), book/src/concepts/capability-typing.md:55, book/src/concepts/derived-view-hoisting.md, book/src/L1/ksp_solve.md (firm), book/src/concepts/dependency-map.md:168-390 (27 cg_preconditioning_framework edges)
route_to: harvester (L4/preconditioning-framework or L4/ksp-solve lift candidate)
---
```

**[OQ] `L4/preconditioning-framework` (or `L4/ksp-solve`) firm-lift to unblock `cg_preconditioning_framework` removal.** The framework slice's §L4 calculus form (the full `KspParams`/`PcParams`/`OpBinding`/constructor-vs-body Haskell+TS form, lines 293–412), §L4 v0.2 capability-typing (the `TrueOp`/`PcAssemblyOp` brand machinery + `finestLevelUnwrap` brand-preservation invariant + `pc_op = op` escape-hatch, lines 413–471), and §L4 v0.3 derived-view-hoisting (the `pcBoundOp` stored-vs-bound-divergence derived view, lines 472–533) are NOT transcribed into any firm `L4/` entry — the slice is the sole detailed source, and `concepts/capability-typing.md:55` + `concepts/derived-view-hoisting.md` cite back INTO these sections. As of cycle-013 the slice is **stub-reduced (annotated-reduced) but NOT removable**: removal is blocked until (a) a firm `L4/preconditioning-framework` (or `L4/ksp-solve`) entry transcribes §L4/§L4-v0.2/§L4-v0.3 AND (b) the ~10 concept-page citations re-point at the firm entry. This is a real harvester promotion candidate (would let the framework slice finally delete) but was NOT this dispatch's enactment. Source: cycle-013 same-layer-cross-cutter dispatch §"Open questions / caveats" item 1.

```yaml
---
slug: negative-result-slice-examples-reciprocal-membership
opened_at: cycle-013
opened_by: same-layer-cross-cutter
last_revisited: null
status: open
relates_to: book/src/concepts/negative-result-slice.md:46 (§"Examples in this spec" — currently lists only polynomial_recurrence_step), book/src/spec/slices/sparse_triangular_solve.md (cycle-013 reduction-status header names the concept "in the spirit of" but membership is one-directional), book/src/concepts/scope-out-obstruction.md:68, book/src/concepts/sequential-obstruction.md:53 (the load-bearing reciprocal citations that DO hold)
route_to: layer-intro-author or same-layer-cross-cutter (optional concept-page Examples-row append)
---
```

**[OQ] One-directional `negative-result-slice` family attribution for `sparse_triangular_solve`.** The cycle-013 reduction-status header on `sparse_triangular_solve.md` classifies the slice as a negative-result slice "in the spirit of `concepts/negative-result-slice.md`," but that concept page's §"Examples in this spec" (`:46`) currently lists ONLY `polynomial_recurrence_step` and does not mention `sparse_triangular_solve` (the slice does not back-reference the concept either). The repairer deliberately softened the stub wording from "(`...negative-result-slice.md` family)" to "in the spirit of ... (that concept page does not yet list this slice)" to avoid overstating a one-directional membership; the genuinely load-bearing reciprocal citations (`scope-out-obstruction.md:68`, `sequential-obstruction.md:53`) DO hold and carry the retention verdict, so the classification is sound. The optional follow-up: add a parallel `sparse_triangular_solve` row to `negative-result-slice.md` §"Examples in this spec" to make the membership reciprocal (the `polynomial_recurrence_step` precedent has reciprocal citation). Authoring into the concept page is outside this slice-scoped dispatch; deferred as low-priority concept-page hygiene. Source: cycle-013 same-layer-cross-cutter critic Issue I1 + repairer decision.

```yaml
---
slug: orthogonalize-mutation-rotation-lowering-verifier-audit
opened_at: cycle-013
opened_by: abstractor
last_revisited: null
status: open
relates_to: book/src/L1-L0/orthogonalize-mutation-rotation.md (firm/structural), book/src/L1/orthogonalize.md (firm L1 operator, inner-product-hook variant axis), palace/linalg/orthog.hpp:25-37 (IdentityInnerProduct / InnerProductHelper dot_op hook), palace/models/romoperator.cpp:51-66 (ROM B-weighted dot_op consumer)
route_to: lowering-verifier
---
```

**[OQ] `orthogonalize-mutation-rotation` lowering-verifier audit — exhaustiveness + B-weighted-hook invariance.** The firm L1>L0 theme `orthogonalize-mutation-rotation` (cycle-013) lands `firm`/`structural`, but two recognition-set claims should be confirmed by a `lowering-verifier` pass. (a) **Exhaustiveness of the L0 corpus scan**: the `get_call_sites` results in the report show the two free functions (`OrthogonalizeColumnMGS` / `OrthogonalizeColumnCGS`) are reached ONLY via the two dispatch wrappers (`OrthogonalizeIteration` in iterative.cpp, `OrthogonalizeColumn` in romoperator.cpp) plus the test harness — so the variant axis is the only L0 entry path and the sub-pattern recognition is closed; the audit should confirm this and check whether any `linalg::AXPY`/`Add` site elsewhere should be cross-referenced as an orthogonalisation fragment (none expected — encapsulated in `orthog.hpp`). (b) **B-weighted inner-product hook invariance**: the ROM path threads a `dot_op` other than `IdentityInnerProduct` (`romoperator.cpp:59-65`); the theme treats this as a substitution of the firm `dot` dependency per the L1 entry's inner-product-hook variant axis — the verifier should confirm the B-weighted `dot_op` does not change the loop structure (it should not — it only swaps the kernel inside `dot_op(w, V[j])`). Source: cycle-013 abstractor §"Open questions / caveats" items 4–5.

```yaml
---
slug: orthogonalize-mutation-rotation-audit-confirmed-rom-consumer-residual
opened_at: cycle-014
opened_by: lowering-verifier
last_revisited: null
status: open
relates_to: book/src/L1-L0/orthogonalize-mutation-rotation.md (firm/structural, audit CONFIRMS-WITH-REFINEMENT cycle-014), orthogonalize-mutation-rotation-lowering-verifier-audit (this ledger, ANSWERED cycle-014 — both claims confirmed), palace/models/romoperator.cpp:51-66 (ROM dispatch wrapper, NOT the consumer)
route_to: lowering-verifier (future ROM greedy-loop consumer audit)
---
```

**[OQ] `orthogonalize-mutation-rotation` lowering-verifier audit ANSWERED (CONFIRMS-WITH-REFINEMENT, `firm` upheld) — one residual ROM-consumer audit-scope caveat.** The cycle-013 audit-request OQ `orthogonalize-mutation-rotation-lowering-verifier-audit` (above) is **answered cycle-014**: both claims confirmed. (a) **Exhaustiveness — confirmed closed.** The `Orthogonalization` enum has exactly 3 variants (`labels.hpp:165-170`); `get_call_sites` returns MGS→3 + CGS→6, every non-test site inside one of the two production dispatch switches (`OrthogonalizeIteration` `iterative.cpp:316/319/322`, `OrthogonalizeColumn` `romoperator.cpp:59/62/65`) + 3 test-harness sites; CGS2 is `OrthogonalizeColumnCGS(...,true)`, not a fourth free function. No unaccounted L0 variant. (b) **B-weighted hook invariance — confirmed.** The ROM `dot_op` only swaps the kernel inside `dot_op(w, V[j])`; the loop structure is unchanged. Refinement R1 (CGS2 dispatch cite `:321-323`→`:322`) + the `verified_against:` evidence block were applied to the theme cycle-014. **Residual (this OQ, low priority):** applicability condition 1 ("no observer of prior `w` after the call") was proven lexically only for GMRES (`iterative.cpp:630-632`) and FGMRES (`:809-811`); the **ROM greedy-sampling consumer** (the loop that calls `romoperator.cpp:OrthogonalizeColumn`) was NOT audited for prior-`w` discard — `romoperator.cpp:51-66` is the dispatch wrapper, not the consumer. Not a defect (the theme scopes its lexical proof to GMRES/FGMRES); a future `lowering-verifier` pass on the ROM greedy loop could extend condition-1 coverage to the third call family. Source: cycle-014 lowering-verifier report §"Open questions / caveats" item 2 + §Recognition-set closure.

```yaml
---
slug: orthogonalize-mutation-rotation-l2-krylov-step-lift-notes
opened_at: cycle-013
opened_by: abstractor
last_revisited: null
status: open
relates_to: book/src/L1-L0/orthogonalize-mutation-rotation.md (reverse-direction lift notes, kept out of formal theme content per high→low discipline), book/src/L2/krylov-step.md (downstream L2 consumer), palace/linalg/iterative.cpp:307-325 (OrthogonalizeIteration forwards j+1), palace/models/romoperator.cpp:51-66 (ROM OrthogonalizeColumn forwards j), palace/linalg/orthog.hpp:75-88 (CGS2 dH scratch)
route_to: lifter (downstream L2 krylov-step consumer of orthogonalize)
---
```

**[OQ] `orthogonalize-mutation-rotation` reverse-direction lift notes for a downstream L2 `krylov-step` consumer.** Two reverse-direction (L0→L1) lift notes were deliberately quarantined out of the formal theme content per the layers-defined-high→low discipline; recorded here as working notes for whatever L2 `krylov-step` lift consumes this theme. (a) **`m` argument off-by-one between consumers**: GMRES/FGMRES forward `j + 1` (orthogonalise against leading `j+1` columns; `iterative.cpp:307-325`), ROM forwards `j` (`romoperator.cpp:51-66`). This is a caller convention, not a property of the lowered operator (the L1 `V` is already the appropriately-sliced basis); a downstream L2 lift should slice `V` at the L1 boundary and not re-thread the `j`/`j+1` choice through the lowering. (b) **CGS2 `dH` scratch is a workspace mention-and-erase**: the lift from L0→L1 must recognise `dH` (`orthog.hpp:75-88`) as a transient (it is summed into `H` and discarded); a naive lift might surface it as a second output. The forward (L1→L0) direction in the theme content correctly treats it as L0-internal scratch. Also: if a future cross-cutter renames the L1 operator `orthogonalize` → `orthogonalize-column`, this theme slug should track it (naming-parallel note). Source: cycle-013 abstractor §"Open questions / caveats" items 1–3.

```yaml
---
slug: chebyshev-lowering-themes-lowering-verifier-followup
opened_at: cycle-013
opened_by: abstractor
last_revisited: null
status: open
relates_to: book/src/L1-L0/chebyshev-smoother-mutation-rotation.md, book/src/L2-L1/chebyshev-iteration-fusion.md, palace/linalg/chebyshev.cpp:188-220, palace/linalg/chebyshev.cpp:261-293, palace/linalg/chebyshev.cpp:68-78, palace/linalg/chebyshev.cpp:112-123
route_to: lowering-verifier
---
```

**[OQ] Chebyshev lowering-theme exhaustiveness audits (both themes, standard follow-up, NOT status reductions).** The two cycle-013 firm chebyshev lowering themes each land `firm` but carry a standard lowering-verifier follow-up. (a) **L1>L0 `chebyshev-smoother-mutation-rotation`**: confirm the four sub-patterns (A application via `Mult2`, B `Mult`→`Mult2` forwarding, C `MultTranspose2 → Mult2` transpose alias, D `SetOperator` closure-field construction) match the L0 corpus exhaustively across both polynomial kinds (`ChebyshevSmoother` 4th / `ChebyshevSmoother1stKind` 1st) × both element types (`<Operator>` real / `<ComplexOperator>` complex) × the consumer forwarding sites (`gmg.cpp:52-59`, `distrelaxation.cpp:21-36`). (b) **L2>L1 `chebyshev-iteration-fusion`**: confirm the per-degree-step fusion against both `Mult2` bodies (`chebyshev.cpp:188-220` 4th, `:261-293` 1st) and the element-kernel sub-fusion (`ApplyOrder0` `:68-78`, `ApplyOrderK` `:112-123`). Neither is a status reduction; both are firm with standard audit follow-ups. Source: cycle-013 abstractor §"Open questions / caveats (cross-theme)" item (lowering-verifier follow-ups).

```yaml
---
slug: chebyshev-dead-code-complex-transpose-kernels
opened_at: cycle-013
opened_by: abstractor
last_revisited: null
status: open
relates_to: book/src/L1-L0/chebyshev-smoother-mutation-rotation.md (sub-pattern C), palace/linalg/chebyshev.cpp:101-110, palace/linalg/chebyshev.cpp:150-159, book/src/L1-L0/axpby-mutation-rotation.md (ComplexVector::Subtract defined-not-used precedent)
route_to: lowering-verifier
---
```

**[OQ] Chebyshev dead-code complex conjugate-transpose kernels (defined-not-used).** `palace/linalg/chebyshev.cpp:101-110` and `:150-159` define conjugate-`dinv` transpose elementwise kernels that are unreachable under the symmetric `MultTranspose2 → Mult2` wiring (sub-pattern C of `chebyshev-smoother-mutation-rotation` aliases transpose to forward under in-scope SPD `A`). They are recognition rules for *potential* non-symmetric transpose sites, not observed ones — same defined-not-used status as the `axpby-mutation-rotation` `ComplexVector::Subtract` forms. Flag for the `lowering-verifier` to record as a recognition-rule-for-potential-site (not an active lowering path). Source: cycle-013 abstractor §"Open questions / caveats" (L1>L0 theme sub-pattern C) + cross-theme item.

```yaml
---
slug: krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep
opened_at: cycle-013
opened_by: integrator-per-report
last_revisited: cycle-014
status: answered
answered_in: cycle-014
answer: The cycle-014 lifter sweep (reports/2026-05-28T193413Z-lifter-krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep/CYCLE.md) re-anchored all 8 dangling cg.md pointers in book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (theme lines 98/109/126/200/204/210/231/233) to their firm homes — body-identity (Claim 2; lines 109/126/204/210/231) → L3-L2/krylov-step-body-identity.md:125; outer-loop sequential-obstruction (Claim 1; lines 98/200/233) → L3/krylov-step.md §Algebraic-laws + concepts/sequential-obstruction.md. Historical cg.md ranges retained as parenthetical provenance. Theme stays firm; build clean (cargo make book exit 0). The SIBLING residual — the SAME dangling cg.md pointers in the DISTINCT L3 operator entry book/src/L3/krylov-step.md (lines 108/129/188/196/202/204) — is the explicitly-separate follow-up OQ l3-krylov-step-cg-md-citation-sweep (cycle-015 lifter); this theme-side OQ does NOT hold open for it.
relates_to: book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (lines 98, 109, 126, 200, 204, 210, 218, 231, 233), book/src/spec/slices/cg.md (reduced stub, 165 lines), book/src/L3-L2/krylov-step-body-identity.md
route_to: dedicated citation-re-anchor dispatch (lifter or same-layer-cross-cutter)
---
```

**[OQ] Theme-wide dangling `cg.md` citation sweep on `krylov-step-typed-wrapper-dissolution`, plus the line-218 "transitive to L2" relic.** The cycle-013 "no-l3-row-drift" lifter re-anchored only the two in-scope theme-body residuals (lines 20, 220); it did NOT touch the pre-existing theme-wide dangling pointers, which are out of that report's narrow scope. `book/src/spec/slices/cg.md` is now a 165-line reduced stub (cycle-009 corpus reduction), so the `cg.md:341-362` / `:351-362` / `:347-350` / `:341-349` ranges still cited at theme lines **98, 109, 126, 200, 204, 210, 231, 233** no longer exist — that body-identity content was lifted into the firm `book/src/L3-L2/krylov-step-body-identity.md` (the faithful current home; it reproduces the verbatim "identity in form" quote and attributes it to the now-reduced `cg.md:341-362` at its line 125). A dedicated citation-re-anchor sweep should re-point each dangling `cg.md` range to the firm L3-L2 theme, keeping `arnoldi_step.md:178-213` (still in-range/valid). The sweep should ALSO bring the **line-218 §Audit relic** "The L4 entry lowers transitively to the L2 entry via this theme ..." into line with the "L4>L3>L2>L1 no-skipped-rows" vocabulary the cycle-013 re-anchor established (critic Issue 2 / repairer deferred drive-by — embedded inside the already-SUPERSEDED §Audit block, not a live contradiction, but a transitive-skip framing relic). Source: cycle-013 lifter report critic Issue 1 (pre-existing theme-wide) + Issue 2 (line-218 relic), repairer "Drive-by observations / deferred to OQ".

```yaml
---
slug: krylov-step-l3-identity-in-form-audit-already-answered-note
opened_at: cycle-013
opened_by: integrator-per-report
last_revisited: null
status: informational
relates_to: scaffolding/open-questions.md (slug krylov-step-l3-identity-in-form-audit, lines ~1134-1139), book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:220
---
```

**[OQ] Note: `krylov-step-l3-identity-in-form-audit` is ALREADY answered (cycle-006) — do NOT double-close.** The cycle-013 "no-l3-row-drift" lifter's Re-anchor 2 firms the historical "no L3 row needed" tail of OQ `krylov-step-l3-identity-in-form-audit`'s disposition prose at theme:220. That OQ slug already carries `answered_in: reports/2026-05-27T081913Z-abstractor-...` (cycle-006) per `scaffolding/open-questions.md` (~lines 1134-1139). The re-anchored disposition prose is therefore **firming a historical record, not enacting a fresh closure** — the integrator/finalize OQ-handling MUST treat this slug as already-answered and NOT re-close or re-open it. Recorded informationally so finalize does not mistake the disposition-prose firming for a closure action. Source: cycle-013 lifter report critic Issue 3 + repairer "Drive-by observations" + Suggested-resolution note (1).

```yaml
---
slug: l0-bundle-6-candidates
discovery_update_at: cycle-013
discovery_update_by: layer-intro-author
status: partially-answered
relates_to: scaffolding/open-questions.md (slug l0-bundle-6-candidates, lines ~1539-1555), book/src/L0/linalg-orthog-file.md, book/src/L0/index.md
---
```

**Discovery update cycle-013 (layer-intro-author)** — bundle-6 candidates #2 and #3 nominated concretely after a citation-pressure survey of all 28-uncovered-vs-covered `palace/linalg/` files (`reports/2026-05-28T144815Z-layer-intro-author-L0-bundle-6-candidates-discovery-and-ranking/`):

- **#2 `linalg-rap-file`** (`palace/linalg/rap.{hpp,cpp}`, 1231 lines) — HIGHEST citation pressure of any uncovered `linalg/` file (5 firm L1/L3 entries + 18 line-level citations across the two `*-mutation-rotation` L1>L0 themes); currently only ad-hoc coverage inside `apply-linop-overload-set.md` (one bullet + 3 evidence lines). A dedicated file overview closes the operator-hierarchy file-gap the way `linalg-iterative-file` closed the solver-hierarchy gap. **NOT authored cycle-013** (file is large + carries the single-rank-reading subtlety on prolongation/restriction collapse — warrants its own full harvest-style read). **This is the next ranked bundle-6 candidate; routes to cycle-014+ as a full bundle-author dispatch.** Suggested chapter outline (anchor ranges to chunk): `ParOperator` class (`rap.hpp:24-121`) + its `Mult`/`MultTranspose`/`AddMult` bodies (`rap.cpp:195-234`, `236-275`); `ComplexParOperator` class (`rap.hpp:124-222`) + its `Mult`/`MultHermitianTranspose` bodies (`rap.cpp:481-517` ff.); the `RestrictionMatrixMult`/`RestrictionMatrixMultTranspose` prolongation-restriction pair (`rap.hpp:46-47, 145-146`); the single-rank-reading collapse note (prolongation/restriction → identity, BC-tdof masking the only L1 residue) per `apply-linop-overload-set.md:31`. **Single-rank-reading caveat**: keep the L0 chapter faithful to the *parallel* source (document what Palace's code does); do NOT pre-collapse the prolongation/restriction in the L0 reference note — that collapse is an L1>L0 lowering concern, cross-linked to `par-types-single-rank-reading`. Same discipline boundary `apply-linop-overload-set` already observes.
- **#3 `linalg-orthog-file`** (`palace/linalg/orthog.hpp`, 93 lines, header-only) — MED-HIGH pressure (firm `L1/orthogonalize` + 2 concept pages); small + bounded + already line-range-mapped by the firm L1 entry. **LANDED cycle-013** (this report) — `book/src/L0/linalg-orthog-file.md` created, registered in `L0/index.md` + `SUMMARY.md` (with `palace/` path prefix). The integrator safety-gated the authored chapter as in-scope authored content (discovery→authoring stretch, defensible per the critic: small file, ranges pre-verified by the firm `L1/orthogonalize.md`; the MGS range was repaired 39-55→41-53 and codemap-confirmed at integration time). No collision with the position-6 cycle-013 wave-1 `book/src/L1-L0/orthogonalize-mutation-rotation.md` theme (different file/Part; MGS range now consistent 41-53 across both).

Lower-pressure deferrals surfaced for future scheduling: `divfree.{hpp,cpp}` (thin firm pressure — 1 citation from `L1/ksp_solve`); the direct-solver trio `mumps`/`strumpack`/`superlu` (only `spec/slices/` slice-era pressure; the direct-solver detail is already routed through `mfem-wrapper-solver`). `densematrix`, `hypre`, `errorestimator`, `floquetcorrection`, `hcurl`, `petsc` have NIL firm citation pressure and are not scheduled. Bundle-6 item #2 from the *original* OQ (`tests-as-semantic-supplement`) remains gated on `tests-as-semantic-supplement-l0-vs-concepts-decision` (placement: L0-convention vs `concepts/`-methodology) — a *decision* block, not a discovery gap, so not re-nominated here. After #3 lands the L0 chapter count is integrator-finalize-re-derived (the report's "18" is a roadmap housekeeping figure, not load-bearing — finalize should re-count). Status held `partially-answered` (item #2 `linalg-rap-file` open as next candidate; original item 2 `tests-as-semantic-supplement` decision-gated; item 3 `mutable-workspace-pattern` Category-5 expansion still open). Source: `reports/2026-05-28T144815Z-layer-intro-author-L0-bundle-6-candidates-discovery-and-ranking/CYCLE.md` §Open questions / caveats.

```yaml
---
slug: concepts-orthogonalization-coefficient-normalisation-drift
closure_confirmed_at: cycle-013
closure_confirmed_by: integrator-per-report
status: answered
relates_to: scaffolding/open-questions.md (slug concepts-orthogonalization-coefficient-normalisation-drift, lines ~2159-2167), book/src/concepts/orthogonalization.md, book/src/L1/orthogonalize.md:331-335
---
```

**Closed cycle-013 (integrator-per-report).** The cycle-013 `same-layer-cross-cutter` concept-audit dispatch (`reports/2026-05-28T1447Z-same-layer-cross-cutter-concepts-orthogonalization-coefficient-normalisation-drift/`) rewrote `book/src/concepts/orthogonalization.md` to align it to the firm `L1/orthogonalize` contract, resolving every drift point this OQ flagged: (a) the line-3 `h_{j+1} = ‖w'‖` normalisation fold-in was removed — the page now states `H` is the **length-`m`** projection coefficients only, and the sub-diagonal `H[m] = ‖w'‖` is explicitly the caller's `nrm2` step (not produced by the operator); (b) the duplicate second concept block (old lines 26-63), including its contradictory "`w` may be mutated; `h_coeffs` is a length-`j` vector" L0-leak signature, was collapsed into a single coherent page; (c) the three mutually-inconsistent coefficient lengths (`j+2` / `j+1` / `j`) are resolved to the one correct length-`m` convention. The page now carries an authoritative-definition blockquote pointing at `L1/orthogonalize` + the forward lowering `L1-L0/orthogonalize-mutation-rotation` (both verified present). This also discharges the L1 entry's own pre-flag of this exact drift (`book/src/L1/orthogonalize.md:331-335`). Status flips `open` → `answered`; the original `status: open` block above (lines ~2159-2167) is left in place per append-only — finalize/ledger maintenance reconciles the header field. Source: this report's CYCLE.md proposed-changes + META.md §"Verification notes" (a)–(d).

```yaml
---
slug: concepts-orthogonalization-spec-slices-link-survival
opened_at: cycle-013
opened_by: integrator-per-report
status: open
relates_to: book/src/concepts/orthogonalization.md, book/src/spec/slices/orthog.md, phase-1-corpus-reduction (this ledger)
---
```

**[OQ] The refreshed `concepts/orthogonalization.md` links `../spec/slices/orthog.md` (the cycle-011 partially-reduced slice) for the retained L2/L3/L4 unfolding — keep the anchor alive if that slice is later stub-reduced.** The cycle-013 concept-page rewrite points its "L2 / L3 placement" section at `spec/slices/orthog`. If a future `phase-1-slice-reduction-audit` reduces `orthog.md` to a stub (the slice is already partially-reduced cycle-011), the stub must retain the file path so this concept-page link survives (`cargo make book` would break otherwise). Flagging so a future slice-reduction dispatch keeps the path-level anchor and re-points the prose to the surviving firm L2/L3/L4 homes if/when they exist. Low priority; not blocking. Source: cycle-013 concept-audit report §"Open questions / caveats" item 3.

```yaml
---
slug: concepts-sequential-obstruction-variant-absorption-drift-spot-check
opened_at: cycle-013
opened_by: integrator-per-report
status: open
relates_to: book/src/concepts/sequential-obstruction.md, book/src/concepts/variant-absorption.md, book/src/L1/orthogonalize.md, concepts-pre-layered-contamination-sweep (this ledger, lines ~335/379)
---
```

**[OQ] The cycle-013 orthogonalization concept-audit was scoped to ONE page vs the firm L1 entry; it did NOT audit `concepts/sequential-obstruction.md` or `concepts/variant-absorption.md` for parallel drift.** Both are referenced by the firm `L1/orthogonalize` entry and by the refreshed `concepts/orthogonalization.md` (the MGS sequential-obstruction-at-L3 note + the all-three-level variant-absorption-under-residual-axis-disclosure note). A future `same-layer-cross-cutter` could spot-check both against the firm entry the way this dispatch did for `orthogonalization.md` — verifying the sequential-obstruction characterization and the variant-absorption residual-axis framing still match the firm L1/L3 vocabulary post-cycle-012/013 firming. Folds naturally into the broader pre-layered-era concept-page contamination sweep already tracked in this ledger (~lines 335/379). Low priority; not blocking. Source: cycle-013 concept-audit report §"Open questions / caveats" item 4 (scope discipline).

```yaml
---
slug: bundle-6-l0-file-overview-next-ranking
opened_at: cycle-014
opened_by: repairer
last_revisited: null
status: open
relates_to: book/src/L0/linalg-rap-file.md, book/src/L0/linalg-solver-file.md, palace/fem/bilinearform.{hpp,cpp}, palace/linalg/hypre.{hpp,cpp}, palace/fem/fespace.{hpp,cpp}
---
```

**[OQ] Bundle-6 L0 file-overview next-candidate ranking after `linalg-solver-file` (#1) and `linalg-rap-file` (#2) land.** The cycle-014 `linalg-rap-file` layer-intro-author dispatch surfaced the three highest-value remaining L0 file-overview gaps observed while localizing `rap.{hpp,cpp}`: (i) **`palace/fem/bilinearform.{hpp,cpp}`** — `BilinearForm::FullAssemble` is the matrix-free→assembled bridge that `ParOperator::ParallelAssemble` directly calls (`rap.cpp:101`), the obvious next anchor as FE-assembly material reaches the frontier; (ii) **`palace/linalg/hypre.{hpp,cpp}`** — `hypre::HypreCSRMatrix` (the `A` storage type `ParallelAssemble` dynamic-casts to, `rap.cpp:92`) plus the Hypre triple-product helpers; (iii) **`palace/fem/fespace.{hpp,cpp}`** — the `FiniteElementSpace` prolongation/restriction-matrix source `P` and `R` come from. **Proposed bundle-6 #3 ranking: `fem/bilinearform` first** (direct `ParallelAssemble` callee, bridges to the next FE-assembly frontier), then `linalg/hypre`, then `fem/fespace`. Recorded for the cycle-014/015 planner. Ranking suggestion, not a blocker. Source: cycle-014 `linalg-rap-file` report §OQ-B (promoted from CYCLE.md by repairer).

```yaml
---
slug: l3-krylov-step-cg-md-citation-sweep
opened_at: cycle-014
opened_by: repairer
last_revisited: cycle-015
status: answered
relates_to: book/src/L3/krylov-step.md, book/src/spec/slices/cg.md (cycle-009 reduced stub), book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
---
```

**[OQ] The firm L3 entry `book/src/L3/krylov-step.md` carries the same dangling `cg.md:NNN-MMM` reduced-slice pointers — needs a sibling lifter (recommended cycle-015).** While the cycle-014 lifter sweep re-anchored the L4>L3 theme `krylov-step-typed-wrapper-dissolution.md` (8 dangling `cg.md` pointers → firm homes; OQ `krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep` closed in full for the theme file), it found the firm L3 operator entry `book/src/L3/krylov-step.md` *itself* still cites the now-out-of-range reduced-slice ranges at its lines 108 (`cg.md:341-349`), 129 (`cg.md:341-349`), 188 (`cg.md:341-362`), 196 (`cg.md:103-115`, `:172-188`, `:393-425`), and 202/204 (`cg.md:208-220`, `:430-446`). These dangle for the same cycle-009-reduction reason (`cg.md` is a 165-line stub). They are in a different file (an L3 operator entry, not the L4>L3 theme) so re-anchoring them was correctly out-of-scope for the cycle-014 theme dispatch (touching them would be an unscoped dispatch-phase `book/` mutation). **Reflexivity note**: the cycle-014 theme re-anchors 1/4/8 designate `L3/krylov-step.md` §Algebraic-laws as the *firm narrative home* for the outer-loop-obstruction family — that designation is valid (the obstruction claim lives there in L3 vocabulary regardless of the target's own citation hygiene), but the sibling sweep should follow to fully close the loop. Recommend a cycle-015 lifter scope `l3-krylov-step-cg-md-citation-sweep` applying the cycle-013/014 lifted-evidence annotation convention verbatim. Low priority; not blocking; the theme-side closure stands on its own. Source: cycle-014 lifter report (`reports/2026-05-28T193413Z-lifter-krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep/CYCLE.md`) §"Open questions / caveats" item 1 + critic Issue 2 (correctly-deferred) + repairer promotion.

```yaml
---
slug: chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep
opened_at: cycle-014
opened_by: repairer
last_revisited: cycle-015
status: resolved
relates_to: book/src/L1/chebyshev-smoother.md, book/src/L2/chebyshev-iteration.md, book/src/L1-L0/chebyshev-smoother-mutation-rotation.md, book/src/L2-L1/chebyshev-iteration-fusion.md, palace/linalg/chebyshev.{cpp,hpp}
---
```

**[OQ] Chebyshev L1/L2 anchor entries carry pre-cycle-013 element-kernel ranges + the brace-start `Mult2` range — full carry-forward sweep needed.** The cycle-014 `lowering-verifier` audit of the two firm chebyshev lowering themes (`reports/2026-05-28T193325Z-lowering-verifier-chebyshev-lowering-themes-lowering-verifier-followup/`), per the cycle-014 critic + repairer, confirmed inherited citation drift in the **anchor entries** (NOT the lowering themes, which carry the cycle-013-repaired ranges). A follow-up abstractor/lifter must sweep ALL of:
- **Element-kernel ranges** `ApplyOrder0 :69-78` → `:68-78` and `ApplyOrderK :114-123` → `:112-123` (the `:69`/`:114` starts are one line inside the signatures `:68`/`:112`). Critic-confirmed sites: **`book/src/L2/chebyshev-iteration.md` lines 35, 143, 245, 247 (FOUR sites)** and **`book/src/L1/chebyshev-smoother.md` lines 245, 247**. Sweep must hit all six, not just an §Evidence block.
- **`Mult2` range** `:191-220` → `:190-220` in both anchors (the `:191` start is the opening brace; the signature is `:190`, verified via `read_range :185-200`; close `:220`).
- (Theme-side, already corrected in this report's proposed-changes: smoother theme `Mult2 :188-220`→`:190-220`, `SetOperator :169-186`→`:169-188`, `:232-259`→`:232-258`, `hpp:43`→`:44`; fusion theme `:188-220`→`:190-220`.)

Bounded citation-range correction per `lifter-scope-content-correction-boundary`; no status change (themes + anchors stay `firm`; the verdicts L1>L0 CONFIRMS-WITH-REFINEMENT / L2>L1 CONFIRMS / fusion-sound stand). Skill-candidate `audit-report-inherited-miscitation-lint` precedent. Source: cycle-014 lowering-verifier report §Open-questions item 1 (promoted by repairer) + cycle-014 critic Issues 1–3.

**[RESOLUTION — cycle-015, integrator-per-report position 3]** RESOLVED by the cycle-015 lifter carry-forward sweep (`reports/2026-05-28T202219Z-lifter-chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep/`). The 7 verified citation corrections landed across the two firm anchor entries: **`book/src/L2/chebyshev-iteration.md`** (5 sites — `ApplyOrder0 :69-78`→`:68-78`, `ApplyOrderK :114-123`→`:112-123` at the kernel-prose / law-3 / two Evidence cites; 4th-kind `Mult2 :191-220`→`:190-220` in §Status) and **`book/src/L1/chebyshev-smoother.md`** (2 sites — `Mult2 :191-220`→`:190-220` in §Context lead-prose + §Evidence). The producer + critic both re-verified each corrected range against L0 `palace/linalg/chebyshev.cpp` via `read_range`; the sweep did not itself drift. The OQ's literal "4+2" prediction is **reconciled to the verified 7-site set** (5 L2 + 2 L1, 3 distinct drifted anchors): the L1 entry carries NO element-kernel anchors (those are L2 detail), and the 1st-kind `Mult2 :261-293` was confirmed genuinely undrifted and correctly left unchanged. No status/law/signature change (both entries stay `firm`). Deferred to integrator-finalize: formal `status:` field flip to `resolved` on this YAML block. The unaudited sibling Evidence cites (`:49-66`, `:194-219`, `:215-217`, etc.) were OQ-scoped out and remain as-is — appropriately deferred, not missed. Resolution-note format used because open-questions.md is append-only (per role-spec / write-authority partition).

```yaml
---
slug: divfree-projector-partly-constructive-to-firm-enactment
opened_at: cycle-014
opened_by: integrator-per-report
last_revisited: cycle-015
status: resolved
relates_to: book/src/L1/divfree-projector.md, palace/fem/integrator.hpp:217, palace/fem/integ/mixedvecgrad.cpp:202, palace/fem/integ/mixedvecgrad.cpp:142, divfree-weakdiv-sign-convention-l0-verify
---
```

**[OQ] `divfree-projector` is UNBLOCKED (cycle-014) for `partly-constructive`→`firm`; cycle-015 enacts the 5 firming edits + drops the caveat.** The cycle-014 `lowering-verifier` audit (`reports/2026-05-28T2115Z-lowering-verifier-divfree-weakdiv-sign-convention-l0-verify/`, verdict **UNBLOCK-PROMOTION**) refuted the cycle-013 "out-of-scope MFEM-vendored integrator" premise: `MixedVectorWeakDivergenceIntegrator` is **Palace-owned, libCEED-backed** (`palace/fem/integrator.hpp:218-226`), its bilinear form is documented in Palace source as `a(u, v) = -(Q u, grad v)` (`palace/fem/integrator.hpp:217`), and the negating sign is the explicit `-1.0` coefficient at `palace/fem/integ/mixedvecgrad.cpp:202` (contrast the non-negated `MixedVectorGradientIntegrator`, `palace/fem/integ/mixedvecgrad.cpp:142`, no `-1.0`; cross-validated at `test/unit/test-libceed.cpp:905-916`). The `WeakDiv ≈ -Gᵀ M` reading is **positively anchored in scope** — the idempotence sub-law's contingency is resolved at the evidence level. The cycle-014 per-report integrator updated ONLY the `## Status` note (UNBLOCKED, promotion-pending) and did NOT drop the `partly-constructive` caveat. This mirrors the cycle-013 eigsolve gated-promotion→cycle-013-enactment pattern; here divfree UNBLOCK(cycle-014)→enactment(cycle-015). **The cycle-015 enactment dispatch (abstractor on `divfree-projector`) applies the 5 firming edits below, THEN flips `## Status` → `firm` and closes the parent OQ `divfree-weakdiv-sign-convention-l0-verify`.** Anchors below are repairer-corrected (`mixedvecgrad.cpp:202`, not `:203`). The clean 5-edit block (preserve verbatim):

- **Edit 1 (REQUIRED) — add the positive sign anchor to §Signature + §Evidence.** In the `P.WeakDiv` signature bullet (after the `divfree.cpp:111-116` citation) append: the integrator's bilinear form is `a(u, v) = -(ε u, ∇v)` for `u ∈ H(curl)`, `v ∈ H1` (`palace/fem/integrator.hpp:217`), materialized as an explicit `-1.0` coefficient in the assemble body (`palace/fem/integ/mixedvecgrad.cpp:202`) — contrast the non-negated `MixedVectorGradientIntegrator` (`palace/fem/integ/mixedvecgrad.cpp:142`, no `-1.0`); thus `WeakDiv = -Gᵀ` (ε-weighted), a positive Palace source site. In §Evidence append: `palace/fem/integrator.hpp:217` (`a(u,v) = -(Q u, grad v)` doc), `palace/fem/integ/mixedvecgrad.cpp:202` (the `-1.0`), `palace/fem/integ/mixedvecgrad.cpp:142` (sibling, no `-1.0`), `palace/fem/integrator.hpp:218-226` (Palace-owned class, NOT MFEM-vendored), `palace/linalg/divfree.hpp:51` (`(Gᵀ M G) y = x` conceptual normal-equations form), `test/unit/test-libceed.cpp:905-916` (cross-validation vs MFEM, L0-equivalent test).
- **Edit 2 (REQUIRED) — rewrite the idempotence Caveat to "confirmed".** Replace the "Caveat (added on repair)" paragraph in the Idempotence bullet: the identification of `WeakDiv` with the (negated) `Gᵀ M` is now anchored (`palace/fem/integrator.hpp:217` + `palace/fem/integ/mixedvecgrad.cpp:202`), so the derivation is unconditional in exact arithmetic; holds modulo `ksp` tolerance (`palace/linalg/divfree.cpp:140,142`). Remove the `partly-constructive` tag from the law header.
- **Edit 3 (REQUIRED) — rewrite §Status to firm.** Change `partly-constructive` → `firm`; remove the constructive-sub-part / negative-anchor / promotion-condition block; state the sign reading was audited (cycle-014) and positively anchored at `integrator.hpp:217` + `mixedvecgrad.cpp:202`; soften the no-dedicated-unit-test note (cite `test-libceed.cpp:905-916` integrator cross-validation as supporting test evidence); remove the UNBLOCKED note (it becomes moot once `firm`).
- **Edit 4 (REQUIRED — substantive) — irrotational/divfree doc-tension Semantics note.** Add one sentence: the apply overwrites `y` with `y + Grad·ψ`, so the net mutated `y` is the divergence-free remainder (class doc `divfree.hpp:29`), while the `Mult` doc comment `divfree.hpp:64-66` ("the irrotational portion ... `∇×y=0`") is stale/misleading relative to the implemented behavior (the `+1.0` add nets to subtraction via the WeakDiv `-1.0`). File breadcrumb OQ `divfree-mult-doc-irrotational-vs-divfree-stale`. Does NOT change L1 semantics.
- **Edit 5 (anchor hygiene, carry-forward) — tighten three off-by-one anchors.** `:141`→`:142` for "abs-tol = machine epsilon" (two occurrences: Idempotence bullet + abs-tol note parenthetical; confirmed `SetAbsTol` is `:142`); `divfree.hpp:68-72`→`:67-71` for the out-of-place `Mult(x,y)` body (`Mult(x,y)` decl opens `:67`); `divfree.hpp:28-31`→`:27-30` for the class-doc block (literal `Gᵀ M x = 0` is `:29`; low priority).

Source: cycle-014 `lowering-verifier` report §Proposed changes (Edits 1-5) + META.md repair §"Gated firming edits preserved" (`:203`→`:202` corrected). NOT a blocker; gated enactment for cycle-015.

```yaml
---
slug: partly-constructive-entry-mechanism-validated-eigsolve-convergence-reason-mapping
opened_at: cycle-014
opened_by: integrator-per-report
last_revisited: cycle-016
status: answered
answered_at: cycle-016
answered_in: reports/2026-05-28T213533Z-abstractor-eigsolve-convergence-reason-mapping/, reports/2026-05-28T221238Z-integrator-finalize-cycle-016/CYCLE.md
relates_to: book/src/L1-L0/eigsolve-convergence-reason-mapping.md, book/src/L1-L0/eigsolve-mutation-rotation.md, cycle-012 partly-constructive-first-class invariant
---
```

**[OQ] The `partly-constructive` ENTRY case is now validated — flag for the cycle-015 meta-phase's assessment of the partly-constructive mechanism.** The cycle-014 `lowering-verifier` audit of `eigsolve-convergence-reason-mapping` (`reports/2026-05-28T193309Z-lowering-verifier-eigsolve-convergence-reason-mapping-promotion/`, verdict **NEGATIVE-ANCHOR-CONFIRMED → STAYS-PARTLY-CONSTRUCTIVE**, critic-re-confirmed: zero materialization — `EPS_DIVERGED`/`EPS_CONVERGED`/`GetConvergedReason` all empty; only print-only `*ConvergedReasonView` at `slepc.cpp:{699,1182,1529}`) demonstrates the **ENTRY** case of the partly-constructive gate: a status that **correctly STAYS** because no positive source site exists to firm against (the promotion condition is genuinely open, not closeable yet). This complements **cycle-013's eigsolve EXIT case** (parent Sub-pattern B `LinearSolveFailed`, a partly-constructive status that PROMOTED). Together, ENTRY (status correctly stays) + EXIT (status promoted) demonstrate the `partly-constructive` gate is a **working transient, not a permanent escape hatch** — the cycle-012 `partly-constructive`-first-class invariant behaving as designed in both directions. Distinct from cycle-012's eigsolve audit, which UNBLOCKED a gated promotion by identifying firming edits; here there are NO firming edits to gate (no positive site). One residual carry-forward: the 8-row enum exhaustiveness is a **literature anchor** (checked vs SLEPc's documented enum; SLEPc/PETSc headers not vendored under `reference/`) — distinct from, and not weakening, the source-confirmed Palace-side negative anchor; low risk (enum stable across SLEPc 3.x), would only under-cover if a future SLEPc version adds a `*_DIVERGED_*` code. Recommend the cycle-015 meta-phase weigh this ENTRY+EXIT pairing in its assessment of the partly-constructive mechanism. Source: cycle-014 lowering-verifier report §Summary + §Open-questions items 1-2 + critic independent-confirmation statement.

```yaml
---
slug: chebyshev-slice-l4-full-removal
opened_at: cycle-014
opened_by: integrator-per-report
last_revisited: cycle-015
status: resolved
relates_to: book/src/spec/slices/chebyshev.md, book/src/L4/chebyshev.md, book/src/L2/krylov-step.md, book/src/L3/krylov-step.md, book/src/L3/apply_linop.md, book/src/L3-L2/krylov-step-body-identity.md, book/src/L2/index.md, chebyshev-l4-firm-via-iterate-while-reanchor
---
```

**[OQ] `book/src/spec/slices/chebyshev.md` §L4 (now the sole retained section) cannot be removed until the firm `krylov-step` citations re-point AND `L4/chebyshev` firms.** The cycle-014 `same-layer-cross-cutter` slice-reduction audit (`reports/2026-05-28T193754Z-same-layer-cross-cutter-chebyshev-phase1-slice-reduction/`, verdict **`partially-absorbed`**) reduced §L1/§Consumers/§Open-questions/§Concept-references/§L2/§L3 to stub-and-pointer (those are fully absorbed by the firm/landed chebyshev cohort: `L1/chebyshev-smoother` + `L2/chebyshev-iteration` firm cycle-012, `L3/chebyshev` partial-obstruction cycle-013, `L1-L0`/`L2-L1` themes firm cycle-013 and confirmed by the sibling cycle-014 lowering-verifier audit) but **RETAINED §L4 verbatim**. Full §L4 removal is gated on two distinct sub-blockers, neither a content gap:

- **(a) Citation re-point.** The firm `book/src/L2/krylov-step.md` (a DISTINCT operator that factors chebyshev as one of its five canonical kernel+driver pattern instances) cites slice §L4 line ranges directly: `chebyshev.md:354-362` (innerStep body, at krylov-step lines 7/79/85/140), `:355-362` (op.scalars, line 58), `:308-323` (ChebOp<E,S>, line 118), `:330-353` (apply/forM_-foldM, line 148), `:421-436` (initial-guess derived-view, line 77). Also `L2/index.md:35`, `L3/krylov-step.md:198,:206`, `L3/apply_linop.md:188`, `L3-L2/krylov-step-body-identity.md:127` cite `:354-362`/`:330-353`. A lifter dispatch on `krylov-step` (+ those siblings) must re-anchor these onto the now-firm-content `L4/chebyshev.md` anchors (`apply`, `innerStep`, `ChebOp<E,S>`, the `initial_guess` derived-view §) — precedent: the cycle-014 `lifter-krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep` cross-operator sweep. **Sequencing constraint (load-bearing):** these citations are line-anchored to the (now-reduced) slice; they MUST re-point in the SAME batch as any §L4 stub, or they drift.
- **(b) `L4/chebyshev` firming.** The `L4/chebyshev` entry is `rough-in` (its `forM_`/`foldM` wrapper vocabulary is queued for the cycle-015 `iterate-while` re-anchor per OQ `chebyshev-l4-firm-via-iterate-while-reanchor`). Until it firms, the slice §L4 is the most-stable detailed source for the `forM_`/`foldM` rendering that `krylov-step` cites.

Route the §L4 removal to a **re-run of this slice-reduction audit post-cycle-015** (after both (a) and (b) close), then reduce §L4 to stub-and-pointer and eventually delete the slice per the monotonic-corpus-reduction invariant. Mirrors the `cg_preconditioning_framework` §L4-retention precedent (chebyshev is one step further: its L4 entry EXISTS but is rough-in + citation-blocked). Corpus note: chebyshev.md remains as a §L4-only slice after cycle-014 — this is a PARTIAL reduction, NOT a removal; do not record it as a corpus removal. Also note `spec/index.md:19` + `SUMMARY.md:100` carry slice TOC/metadata that the partial reduction does not invalidate (the file persists); full removal (later cycle) updates both. Source: cycle-014 same-layer-cross-cutter report §Verdict + §Open-questions item 1 + §Recommendation 2-3.

```yaml
---
slug: divfree-projector-partly-constructive-to-firm-enactment-RESOLUTION
opened_at: cycle-015
opened_by: integrator-per-report
last_revisited: cycle-015
status: resolved
resolved_at: cycle-015
resolved_in: reports/2026-05-28T2300Z-abstractor-divfree-projector-partly-constructive-to-firm-enactment/
relates_to: divfree-projector-partly-constructive-to-firm-enactment (this ledger, cycle-014), book/src/L1/divfree-projector.md, divfree-weakdiv-sign-convention-l0-verify
---
```

**[OQ resolution] `divfree-projector-partly-constructive-to-firm-enactment` — RESOLVED (cycle-015).** The cycle-015 abstractor enactment dispatch applied all 5 firming edits to `book/src/L1/divfree-projector.md` and the per-report integrator landed them: (Edit 1) the positive sign anchors (`palace/fem/integrator.hpp:217` + `palace/fem/integ/mixedvecgrad.cpp:202`, contrast sibling `:142`) added to the `P.WeakDiv` §Signature bullet; (Edit 2) the Idempotence law rewritten to unconditional-in-exact-arithmetic, dropping the `partly-constructive` law-header tag and the "Caveat (added on repair)" paragraph, with the `:141`→`:140,142` abs-tol off-by-one corrected; (Edit 3) the Non-law sign-convention bullet re-anchored to "positively re-derived from Palace source"; (Edit 4) the irrotational/divfree doc-tension Semantics note; (Edit 5) `## Status` flipped `partly-constructive` → **`firm`**, dropping the constructive-sub-part / negative-anchor / promotion-condition block and the UNBLOCKED blockquote; plus §Evidence append of the 6 sign/test anchors. L1 index dep-map cell flipped `partly-constructive` → `firm`, and the Vocabulary cohort firm count bumped **10 → 11** with the divfree-projector firm bullet appended. **This completes the first full `partly-constructive` ENTRY→EXIT lifecycle traversal** (entered cycle-013 via integrator-adjudication-down-from-argued-firm, UNBLOCKED cycle-014 by the lowering-verifier audit, exits firm cycle-015) — clean evidence for the batch-3 meta-phase that `partly-constructive` is a *transient gate*, not a permanent escape hatch. The deferred non-load-bearing anchor-hygiene off-by-ones (`divfree.hpp:68-72`→`:67-71`, `:28-31`→`:27-30`) remain open for a later lifter/repairer pass — tracked, not a blocker. integrator-finalize does the formal status-field close on the parent OQ. Source: cycle-015 abstractor dispatch §Proposed changes (Edits 1-8) + critic META.md (`overall_status: ready`, firm flip fully warranted).

```yaml
---
slug: divfree-weakdiv-sign-convention-l0-verify-RESOLUTION
opened_at: cycle-015
opened_by: integrator-per-report
last_revisited: cycle-015
status: resolved
resolved_at: cycle-015
resolved_in: reports/2026-05-28T2300Z-abstractor-divfree-projector-partly-constructive-to-firm-enactment/
relates_to: divfree-weakdiv-sign-convention-l0-verify (this ledger, cycle-013), reports/2026-05-28T2115Z-lowering-verifier-divfree-weakdiv-sign-convention-l0-verify/, book/src/L1/divfree-projector.md
---
```

**[OQ resolution] `divfree-weakdiv-sign-convention-l0-verify` — RESOLVED (consumed cycle-015).** The cycle-014 `lowering-verifier` audit (verdict UNBLOCK-PROMOTION) positively anchored the `WeakDiv ≈ -Gᵀ M` sign in Palace-owned source: the integrator's bilinear form `a(u,v) = -(Q u, grad v)` (`palace/fem/integrator.hpp:217`), the explicit `-1.0` coefficient at `palace/fem/integ/mixedvecgrad.cpp:202`, the non-negated sibling `MixedVectorGradientIntegrator` at `palace/fem/integ/mixedvecgrad.cpp:142`, cross-validated against MFEM at `test/unit/test-libceed.cpp:905-916`. The `MixedVectorWeakDivergenceIntegrator` is Palace-owned, libCEED-backed (`palace/fem/integrator.hpp:218-226`) — the cycle-013 "below-the-L0-boundary, MFEM-vendored" framing was a mislocalization. The cycle-015 divfree enactment consumes this resolution (the sign anchors are now cited directly in the firm `divfree-projector` entry). The off-by-one `:203`→`:202` drift flagged in cycle-014 is confirmed corrected (the `-1.0` is exactly `:202`; `:203` is the `AssembleCeedOperator` call). integrator-finalize does the formal status-field close. Source: cycle-014 lowering-verifier report + cycle-015 abstractor dispatch §Anchor re-confirmation (re-`read_range` of both load-bearing anchors).

```yaml
---
slug: divfree-mult-doc-irrotational-vs-divfree-stale
opened_at: cycle-015
opened_by: integrator-per-report
last_revisited: null
status: open
relates_to: book/src/L1/divfree-projector.md, palace/linalg/divfree.hpp:64-66, palace/linalg/divfree.hpp:28-31, divfree-weakdiv-sign-convention-l0-verify
---
```

**[OQ] The `DivFreeSolver::Mult` doc comment (`palace/linalg/divfree.hpp:64-66`, "the irrotational portion ... satisfying ∇ × y = 0") is stale/misleading relative to the implemented divergence-free behavior — a Palace-internal documentation inconsistency.** The class doc (`palace/linalg/divfree.hpp:28-31`) defines the projection target as **divergence-free** (`Gᵀ M y' = 0`); the apply overwrites `y` with `y + Grad·ψ`, and because `WeakDiv` carries the negating `-1.0` sign (`palace/fem/integ/mixedvecgrad.cpp:202`), the net effect *removes* the gradient (irrotational) part, yielding the divergence-free remainder. The `Mult` member doc-comment describing the OUTPUT as "the irrotational portion ... ∇×y=0" therefore contradicts both the class doc and the actual computed result — it appears to describe the *removed* component as if it were the output. This is a documentation-fidelity caveat in Palace source, NOT an L1 semantic ambiguity (the firm `divfree-projector` entry adopts the class-doc divergence-free reading, recorded in-line by the cycle-015 Edit 4 Semantics note). Surfaced/recommended-for-filing by the cycle-014 lowering-verifier audit and the cycle-015 abstractor dispatch (§Open questions item 3); does NOT block the firm promotion. Candidate disposition: a future lifter/lowering-verifier pass on the `divfree-projector-mutation-rotation` L1>L0 theme notes the stale comment as a documentation-only discrepancy with no semantic consequence, OR a `problems/` drive-by flags it upstream. Source: cycle-015 abstractor dispatch §Open questions item 3 + Edit 4 + cycle-014 audit recommendation.

**[OQ resolution] `chebyshev-l4-firm-via-iterate-while-reanchor` — RESOLVED (cycle-015).** The cycle-015 lifter (`reports/2026-05-28T202138Z-lifter-chebyshev-l4-firm-via-iterate-while-reanchor/`) enacted the cycle-014 combinator-miner route (i): both un-anchored `forM_` (outer `pc_it`) / `foldM` (inner `k`) binds in `book/src/L4/chebyshev.md` `apply` are re-expressed as nested `iterate_while_pure` folds with **step-count predicates** (`s.it <= op.pc_it` outer, `c.k <= op.order - 1` inner), the loop counter folded into the carry — reusing the firm `iterate-while` family (strawman §6.5 step 5, `l4_calculus.md:418`; `run_lbm` precedent `:382-385`). The body re-anchor + the 18 prose sites naming `forM_`/`foldM` + the §Status flip `rough-in`→`firm` + the `L4/index.md` dep-map row rewrite + cohort move (Rough-in 1→0; **Firm 3→4**) all landed. The un-anchored-vocabulary blocker — the sole reason for the cycle-013 repairer downgrade — is closed. integrator-finalize does the formal status-field close. Source: cycle-015 lifter CYCLE.md Changes 1-19.

**[OQ resolution] `chebyshev-l4-inner-loop-presentation-carry-st-vs-with-prev` — RESOLVED-AND-CLOSED (cycle-015).** The inner `k`-recurrence presentation question (scalar-recurrence state `st`/`rho_prev` riding in the `iterate_while_pure` carry `{ r, d, st, k }` vs. threaded as the `iterate-while-with-prev` closure `prev` parameter) is resolved to the **plain `iterate_while_pure` carry-`st` form**: the 4th-kind's `st = ()` makes the carry-`st` form the degenerate no-prev case, unifying both polynomial kinds without a bootstrap step (the with-prev form would require a `first_step` the 4th-kind does not need). The cycle-014 combinator-miner both STAGED the carry-`st` sketch AND recommended it as default, so the cycle-015 lifter enacting it is within lifter discipline (not a fresh content choice). Recorded in `book/src/L4/chebyshev.md` §Variant axes + §Status. A residual same-layer-cross-cutter watch-item (unify this `st`-carry with the CG `beta_prev`-carry under one recurrence-variable-threading note) is a separate sideways emission, NOT a change to this entry — non-blocking. Source: cycle-015 lifter CYCLE.md Changes 11-12 + Discipline notes.

```yaml
---
slug: l3-chebyshev-downward-prose-iterate-while-refresh
opened_at: cycle-015
opened_by: integrator-per-report
last_revisited: cycle-016
status: resolved
resolved_at: cycle-016
resolved_in: reports/2026-05-28T214012Z-lifter-l3-chebyshev-prose-refresh/
relates_to: book/src/L3/chebyshev.md, book/src/L4/chebyshev.md, chebyshev-l4-firm-via-iterate-while-reanchor, chebyshev-slice-l4-full-removal, l3-chebyshev-sibling-formm-foldm-prose-sweep
---
```

**[OQ] `book/src/L3/chebyshev.md:236-238` carries stale upward-pointing prose naming the now-superseded L4 `foldM`/`forM_` combinators.** After the cycle-015 lifter re-anchored `book/src/L4/chebyshev.md` to `iterate_while_pure` folds with step-count predicates (closing `chebyshev-l4-firm-via-iterate-while-reanchor`), the L3 entry's prose describing its `itloop`/`kloop` tail recursions as "the L3 rendering of the L4 `foldM`/`forM_`" now names L4 vocabulary that no longer exists in the L4 entry. The L4>L3 image is in fact cleaner: both loops now lower to `iterate_while_pure_L3` per `iterate-while.md:193-195`, matching the L3 `itloop`/`kloop` the cycle-013 L3 entry already renders. The fix is a surgical one-line prose refresh in `L3/chebyshev.md` to name `iterate_while_pure`/`iterate_while_pure_L3` instead of `foldM`/`forM_`; **no L3 semantics change.** This is harmless to the cycle-015 firm flip (the stale prose is a downward-pointing cross-reference in a *different file* that the pure-re-anchor dispatch correctly scoped out — it touched only `L4/chebyshev.md` + `L4/index.md`). Routes to a follow-up cross-layer touch (lifter on `L3/chebyshev` OR a cross-layer-cross-cutter sweep). Source: cycle-015 critic Issue 2 (out-of-scope observation), promoted by repairer to the report's OQ section (item 5), promoted here by integrator-per-report.

```yaml
---
slug: l4-krylov-step-cg-md-citation-sweep
opened_at: cycle-015
opened_by: lifter
last_revisited: cycle-016
status: answered
answered_at: cycle-016
answered_in: reports/2026-05-28T214500Z-lifter-l4-krylov-step-cg-sweep/
relates_to: book/src/L4/krylov-step.md, book/src/spec/slices/cg.md (cycle-009 reduced stub), book/src/L2/krylov-step.md, l3-l2-body-identity-cg-md-citation-sweep
---
```

**[OQ] The firm L4 entry `book/src/L4/krylov-step.md` carries the same dangling `cg.md:NNN-MMM` reduced-slice pointers — needs a sibling lifter (recommended cycle-016).** The cycle-015 lifter sweep that re-anchored the firm L3 operator entry `book/src/L3/krylov-step.md` (5 dangling `cg.md` pointers → firm homes; OQ `l3-krylov-step-cg-md-citation-sweep` closed for the L3 file) found, while locating the terminal firm homes for its Re-anchors 4/5, that the firm L4 operator entry `book/src/L4/krylov-step.md` *itself* still cites now-out-of-range reduced-slice ranges at its lines 14 (`cg.md:352-362`), 82 (`cg.md:393-425`), 96 (`cg.md:325-339`), 133 (`cg.md:352-362`), 150 (`cg.md:172-188`, `:393-425`), 170 (`cg.md:172-188`), 171 (`cg.md:393-425`) — 8 `cg.md` references. These dangle for the same cycle-009-reduction reason (`cg.md` is a 165-line stub). They are in a different file (an L4 operator entry, not the L3 entry just swept), so re-anchoring them was correctly out-of-scope for the cycle-015 L3 dispatch (touching them would be an unscoped `book/` mutation). **Note**: the cycle-015 L3 Re-anchor 4 deliberately points the L3 step-body pointer at `L2/krylov-step.md:138` as the TERMINAL firm home (not at L4:170-171, which are themselves transitive-dangling) — so the L3 sweep does not depend on the L4 sweep landing first. Recommend a cycle-016 lifter scope `l4-krylov-step-cg-md-citation-sweep` applying the cycle-013/014/015 lifted-evidence annotation convention verbatim. Low priority; not blocking. Source: cycle-015 lifter report (`reports/2026-05-28T202234Z-lifter-l3-krylov-step-cg-md-citation-sweep/CYCLE.md`) §"Open questions / caveats" item 1 + critic Issue 4 (correctly-deferred) + integrator-per-report promotion (position 4).

```yaml
---
slug: l2-krylov-step-cg-md-citation-sweep
opened_at: cycle-015
opened_by: lifter
last_revisited: cycle-016
status: answered
answered_at: cycle-016
answered_in: reports/2026-05-28T213650Z-lifter-l2-krylov-step-cg-sweep/
residual: 2 live-slice citations (cg.md:27-141 / :86-106 at §Evidence 138/146) await a future full cg.md stub removal re-point; routed to phase-1-slice-reduction-audit
relates_to: book/src/L2/krylov-step.md, book/src/spec/slices/cg.md (cycle-009 reduced stub)
---
```

**[OQ] The firm L2 entry `book/src/L2/krylov-step.md` carries the same dangling `cg.md:NNN-MMM` reduced-slice pointers — needs a sibling lifter (recommended cycle-016).** The cycle-015 L3 lifter sweep designated `book/src/L2/krylov-step.md` §Evidence as the TERMINAL firm home for its Re-anchors 4 (line 138, step bodies) and 5 (line 146, outer-driver consumer sites) — a valid designation because the source ranges genuinely live in the L2 §Evidence registry in L2 vocabulary, regardless of L2's own citation hygiene. But that same L2 entry *itself* still cites now-out-of-range reduced-slice ranges at its lines 7 (`cg.md:103-115`, `:172-188`, `:393-425`), 9 (`cg.md:341-349`), 67 (`cg.md:288`), 69 (`cg.md:172-188`, `:393-425`), 77 (`cg.md:325-339`), 79 (`cg.md:103-115`), 81 (`cg.md:103-115`), 116 (`cg.md:228-257`), 119 (`cg.md:172-188`, `:393-425`), 138 (`cg.md:103-115`, `:172-188`, `:393-425`), 146 (`cg.md:208-220`, `:430-446`), 172 (`cg.md:288`) — 12 `cg.md` references. These dangle for the same cycle-009-reduction reason. They are in a different file (an L2 operator entry), so re-anchoring them was out-of-scope for the cycle-015 L3 dispatch. **The L2 entry being the terminal home for the L3 sweep's Re-anchors 4/5 does NOT depend on closing this OQ** — pointing the L3 pointer at L2:138/:146 as the narrative/terminal home is correct regardless; this OQ closes the chain fully (L2's own pointers terminate at firm L0 anchors or are annotated as lifted from the reduced slice). Recommend a cycle-016 lifter scope `l2-krylov-step-cg-md-citation-sweep` applying the cycle-013/014/015 lifted-evidence annotation convention verbatim. Low priority; not blocking. Source: cycle-015 lifter report (`reports/2026-05-28T202234Z-lifter-l3-krylov-step-cg-md-citation-sweep/CYCLE.md`) §"Open questions / caveats" item 1 + critic Issue 4 (correctly-deferred) + integrator-per-report promotion (position 4).

**[RESOLUTION — cycle-015, integrator-per-report position 4]** OQ `l3-krylov-step-cg-md-citation-sweep` (opened cycle-014, above) RESOLVED IN FULL for the L3 file by the cycle-015 lifter sweep (`reports/2026-05-28T202234Z-lifter-l3-krylov-step-cg-md-citation-sweep/`). All 5 dangling `cg.md` pointer lines in `book/src/L3/krylov-step.md` re-anchored to terminal firm homes: lines 108/129 → firm [`sequential-obstruction`](../../book/src/concepts/sequential-obstruction.md) concept page + live `arnoldi_step.md:194-213` (CG provenance `cg.md:341-349` retained as a parenthetical lifted-evidence note); line 188 → firm `L3-L2/krylov-step-body-identity.md:125` (verified — carries the verbatim Claim-2 quote with `cg.md:341-362` provenance); line 196 → firm `L2/krylov-step.md:138` (verified — carries the three CG step-body ranges; the repairer corrected this from the producer's transitive-dangling L4:170-171 target); line 204 → firm `L2/krylov-step.md:146` (verified — carries the `cg_solve` outer-driver consumer sites; the repairer removed the non-existent L4 `cg_solve`-driver citation). Cross-reference-integrity gate passed: all 4 distinct firm-home targets read and confirmed to contain the claimed content; all 5 OLD strings matched disk byte-for-byte at dispatch-time re-read; `cg.md` re-confirmed 165-line stub (all 341+ ranges genuinely out-of-range). The entry's `firm` status is unchanged (pure citation re-anchor). The residual L4/L2 sibling sweeps are now filed as the two NEW OQs immediately above (`l4-`/`l2-krylov-step-cg-md-citation-sweep`), cycle-016 follow-ups. Deferred to integrator-finalize: formal `status:` field flip to `answered` (answered_in this CYCLE.md) on the `l3-krylov-step-cg-md-citation-sweep` YAML block. Resolution-note format used because open-questions.md is append-only (per role-spec / write-authority partition).

```yaml
---
slug: bundle-6-l0-libceed-operator-file-next-candidate
opened_at: cycle-015
opened_by: layer-intro-author
last_revisited: cycle-016
status: resolved
resolved_at: cycle-016
resolved_in: reports/2026-05-28T213513Z-layer-intro-author-l0-libceed-operator/
relates_to: book/src/L0/fem-libceed-operator-file.md, book/src/L0/fem-bilinearform-file.md, scaffolding/open-questions.md (slug bundle-6-l0-file-overview-next-ranking), palace/fem/libceed/operator.cpp
---
```

**[OQ] Bundle-6 #5 L0 file-overview next-candidate: `palace/fem/libceed/operator.cpp`.** The cycle-015 `fem-bilinearform-file` layer-intro-author dispatch (bundle-6 #4, landed this cycle) found that *both* of its assembly bodies forward directly into `palace/fem/libceed/operator.cpp`: `ceed::CeedOperatorFullAssemble` (verified def `libceed/operator.cpp:455`) materializes the `hypre::HypreCSRMatrix` from a partially-assembled `ceed::Operator`, and `ceed::CeedOperatorCoarsen` (verified def `libceed/operator.cpp:525`) does the multigrid operator-coarsening reused by the FE-space-hierarchy `Assemble` overload. That file also holds the `ceed::Operator` base class this chapter's `PartialAssemble` constructs. It is the **direct callee** the `fem-bilinearform-file` chapter defers to for the actual matrix-materialization + operator-coarsening algebra — the obvious **bundle-6 #5 candidate**. Assess its size first (it may warrant a focused-subset chapter rather than a full-file overview). **Alternative #5 candidate: `palace/fem/fespace.{hpp,cpp}`** (the `FiniteElementSpace` / `FiniteElementSpaceHierarchy` types `fem-bilinearform-file` takes by reference, providing `GetCeedElemRestriction` / `GetCeedBasis` / `GetVSize`) — the input-side anchor where `libceed/operator.cpp` is the output-side anchor; ranking leans toward `libceed/operator.cpp` (tighter coupling to the assembly algebra), with `fespace` a larger, more foundational surface better scheduled once more FE-frontier L1 work pulls on it. Recorded for the cycle-016 planner; ranking suggestion, not a blocker. Source: cycle-015 `fem-bilinearform-file` report (`reports/2026-05-28T202225Z-layer-intro-author-fem-bilinearform-file/CYCLE.md`) §"Open questions / caveats" §bundle-6 ranking + §Supporting evidence (callee def-lines `libceed/operator.cpp:455,525` confirmed via codemap); integrator-per-report promotion (position 5).

```yaml
---
slug: chebyshev-slice-l4-full-removal
opened_at: cycle-014
opened_by: same-layer-cross-cutter
last_revisited: cycle-015
status: resolved
relates_to: book/src/L4/chebyshev.md, book/src/L2/krylov-step.md, book/src/spec/slices/chebyshev.md (removed)
---
```

**[RESOLUTION — cycle-015, integrator-per-report position 6]** OQ `chebyshev-slice-l4-full-removal` RESOLVED IN FULL. The cycle-014 two-part removal gate is closed: (a) all inbound §L4 + provenance citations to `book/src/spec/slices/chebyshev.md` re-pointed onto the firm chebyshev cohort, and (b) `book/src/L4/chebyshev.md` flipped `rough-in`→`firm` by the cycle-015 wave-1 lifter (position 2). The slice `book/src/spec/slices/chebyshev.md` was REMOVED this cycle (`git rm`), with its `SUMMARY.md` TOC line (R-20) and `spec/index.md` status-table row (R-21) also removed. **18 citation re-points applied** (the report's 13 originals R-1..R-19 minus the 2 TOC removals + R-1b/R-13b/R-23/R-24 repairer-added + one integrator-discretionary transitive-narrative fix at `L2/chebyshev-iteration.md:30`). Class-A §L4 line-range citations re-pointed onto stable `L4/chebyshev.md` section anchors (§Semantics `innerStep`/`apply`, §Signature `scalars`/`ChebOp E S`, §"Initial-guess shape"); Class-B already-dangling §L1/§L2/§L3 provenance citations (R-14/15/16) converted to git-history provenance form; Class-C prose/structural pointers re-pointed to the firm sibling or removed. **Corpus removals: 8/10 → 9/10.** Cross-reference-integrity gate passed: final whole-`book/`-tree grep confirms ZERO markdown links to the removed slice (the build-breaking class is empty) and all remaining `spec/slices/chebyshev.md` mentions are intentional provenance/historical prose (R-14/15/16/23/24 + the L4 §Evidence provenance fixup + frozen meta-reviews). **OQ-1 residual CLOSED in-cycle**: the report deferred the `L4/chebyshev.md` §Status/§Evidence self-citations (write-conflict with the wave-1 lifter's same-line rewrites); since both reports landed before this position, the §Status self-cites (`:289`/`:325`/`:396-397`) were already converted by the wave-1 lifter's Change 11 (grep confirms none remain), and I folded the §Evidence self-cite (`chebyshev.md:287-439` at `L4/chebyshev.md:575`) into git-history provenance form as a post-apply fixup (the report explicitly offered this option). OQ-2 (`meta-reviews/2026-05-24-cycles-10-12.md:24` frozen historical record) and OQ-4 (`spec/index.md` "Highest layer = L4" progress fact now carried by the firm `L4/chebyshev.md`) left as-is per their leave-frozen dispositions. OQ-3 (build-backstop) deferred to integrator-finalize's `cargo make book`. Deferred to integrator-finalize: formal `status:` field flip + `integrated_at`/`integration_commit` frontmatter on the consumed report. Resolution-note format used because open-questions.md is append-only (per role-spec / write-authority partition). Source: cycle-015 same-layer-cross-cutter report (`reports/2026-05-28T202756Z-same-layer-cross-cutter-chebyshev-slice-l4-full-removal/`).

```yaml
---
slug: l4-chebyshev-residual-formm-foldm-prose-cleanup
opened_at: cycle-015
opened_by: integrator-finalize
last_revisited: cycle-016
status: resolved
resolved_at: cycle-016
resolved_in: reports/2026-05-28T214020Z-lifter-l4-chebyshev-prose-cleanup/
relates_to: book/src/L4/chebyshev.md, chebyshev-l4-firm-via-iterate-while-reanchor (this ledger, resolved cycle-015), l3-chebyshev-downward-prose-iterate-while-refresh (this ledger), l3-chebyshev-sibling-formm-foldm-prose-sweep (this ledger)
---
```

**[OQ] Three stale `forM_`/`foldM` mentions remain in `book/src/L4/chebyshev.md` evidence/dependency prose (~lines 368/382/547) outside the cycle-015 re-anchor blocks — surgical prose refresh for cycle-016.** The cycle-015 lifter (`chebyshev-l4-firm-via-iterate-while-reanchor`, RESOLVED) re-anchored the `apply` body from `forM_`/`foldM` onto nested `iterate_while_pure` folds and flipped the entry `rough-in`→`firm`, but scoped its 19 proposed-change blocks precisely to the body + the §Status/dep-map + the directly-affected prose. Three narrative/dependency-prose mentions of the now-superseded `forM_`/`foldM` vocabulary remain UNTOUCHED: the §Dependencies `state-stratification` bullet (~L368, "scalar-recurrence stratum S threaded by `foldM`"), the §Dependencies `sequential-obstruction` bullet (~L382, "surfacing as `forM_` (outer) and `foldM` (inner) binds"), and the §Evidence L3 bullet (~L547, "this entry's `forM_`/`foldM` binds inherit"). These are descriptive prose, NOT body/status/law content — harmless to the firm flip, but they name L4 vocabulary the entry no longer uses. (Distinct from the INTENTIONAL historical-narrative `forM_`/`foldM` strings in the new §Status + dep-map Status cell, which read "the obstructions WERE rendered as un-anchored forM_/foldM" — those stay.) The fix is a surgical 3-site prose refresh naming `iterate_while_pure`/`iterate_while_pure_L3`; no semantics change. Sibling to the L3-side `l3-chebyshev-downward-prose-iterate-while-refresh` OQ (same cycle-016 follow-up family). Also note `L4/krylov-step.md` + `L2/krylov-step.md` carry dangling `cg.md` pointers (sibling cg.md sweeps already filed as cycle-016 OQs `l4-`/`l2-krylov-step-cg-md-citation-sweep`). Low priority; not blocking. Source: cycle-015 lifter STAGING note + cycle-015 integrator-finalize signals item 4.

**[RESOLUTION — cycle-016, integrator-per-report position 6]** OQ `l4-chebyshev-residual-formm-foldm-prose-cleanup` RESOLVED IN FULL. The cycle-016 lifter (`lifter-l4-chebyshev-prose-cleanup`, READY) refreshed exactly the three named descriptive-prose sites in `book/src/L4/chebyshev.md` from the superseded `forM_`/`foldM` vocabulary onto the canonical `iterate_while_pure`: (1) §Dependencies `state-stratification` bullet — "scalar-recurrence stratum `S` threaded by `foldM`" → "threaded through the inner `iterate_while_pure` carry"; (2) §Dependencies `sequential-obstruction` bullet — "surfacing as `forM_` (outer) and `foldM` (inner) binds" → "the two nested `iterate_while_pure` folds (outer `pc_it` sweep, inner `k`-recurrence) with step-count predicates"; (3) §Evidence L3 bullet — "this entry's `forM_`/`foldM` binds inherit" → "this entry's two `iterate_while_pure` folds inherit". The four INTENTIONAL historical-narrative occurrences (the §Status reconcile narrative "the obstructions WERE rendered as un-anchored `forM_`/`foldM`" + the §Evidence Provenance slice-supersession note) are correctly left VERBATIM per this OQ's explicit "those stay" instruction — post-apply grep confirms exactly four `forM_`/`foldM` mentions remain, all in the historical-narrative class. Pure vocabulary refresh — NO semantics/structure/status change (entry stays `firm`); no new citations emitted, no link altered. The OLD anchor strings for all three edits matched disk byte-for-byte on fresh re-read (no in-cycle file overlap — reports 1-5 touched distinct files). The sibling L3-side `l3-chebyshev-downward-prose-iterate-while-refresh` OQ remains a SEPARATE open cycle-016 follow-up (the L3 entry `book/src/L3/chebyshev.md` still carries `forM_`/`foldM` at 6 sites — out of this one-entry dispatch's scope). Deferred to integrator-finalize: formal `status:` field flip → `resolved` + `last_revisited: cycle-016`. Resolution-note format used because open-questions.md is append-only (per role-spec / write-authority partition). Source: cycle-016 lifter report (`reports/2026-05-28T214020Z-lifter-l4-chebyshev-prose-cleanup/`).

```yaml
---
slug: divfree-l1-entry-apply-close-and-reltol-line-drift
opened_at: cycle-016
opened_by: abstractor
last_revisited: null
status: open
relates_to: book/src/L1/divfree-projector.md, book/src/L1-L0/divfree-projector-mutation-rotation.md, palace/linalg/divfree.cpp
---
```

**[OQ] The firm L1 entry `book/src/L1/divfree-projector.md` carries off-by-one citation drifts in its apply-close-brace and CG rel-tol pins — needs a harvester/repairer pass on the firm L1 entry (recommended cycle-016+).** The cycle-016 abstractor authoring the `divfree-projector-mutation-rotation` L1>L0 theme (`reports/2026-05-28T1500Z-abstractor-divfree-projector-L1-L0/`) independently re-verified the L0 source via codemap `read_range` and found two off-by-one drifts in the *firm* L1 operator entry `book/src/L1/divfree-projector.md` (confirmed by the critic against the actual files): (a) the apply `Mult(VecType &y)` is cited as `palace/linalg/divfree.cpp:155-186`, but the close brace is `:187` (the L1 entry undershoots by one — cited at L1 entry lines 14/122/237/301); (b) the CG rel-tol set `SetRelTol(tol)` is at `palace/linalg/divfree.cpp:141`, but the L1 entry cites `:140` (which is actually `SetInitialGuess(false)`); the abs-tol `:142` is correct (L1 entry line 179). The theme cites the *corrected* ranges; the abstractor did NOT edit the firm L1 entry (out of abstractor authority) and filed this OQ — the desired behaviour under batch-3's producer-citation-drift friction. **FOLD-IN (per cycle-015 staging note + critic Issue 4 + cycle-016 dispatch):** the same firm L1 entry carries an *inherited dangling* `(see Variant axes)` pointer at its **line 43** — the L1 entry has no `## Variant axes` heading (its headers are Context / Signature / Semantics / Algebraic laws / Dependencies / Status / Evidence). The theme's propagation of this dangling anchor was repaired in-theme (re-pointed to the L1 §Signature element-type note); the L1-entry-internal dangling pointer remains. Both defects are firm-L1-entry citation/anchor hygiene on the same file — fold them into one harvester/repairer pass (modifying the L1 operator entry is harvester authority, not abstractor). Also note the cycle-015 enactment's carry-forward anchor hygiene on the same file (`divfree.hpp:68-72`→`:67-71`, `:28-31`→`:27-30`, tracked under the enactment OQ) — the natural co-located pass closes all of these together. Low severity (the prose is otherwise exact; no load-bearing claim affected). NEW this cycle. Source: cycle-016 abstractor report §"Open questions" item 1 + §"Open questions / caveats" + critic Issue 4 + repairer Unrepairable-findings; integrator-per-report promotion (position 1).

```yaml
---
slug: divfree-mult-doc-irrotational-vs-divfree-stale
opened_at: cycle-013
opened_by: harvester
last_revisited: cycle-016
status: open
relates_to: book/src/L1/divfree-projector.md, book/src/L1-L0/divfree-projector-mutation-rotation.md, palace/linalg/divfree.hpp
---
```

**[OQ] (CARRIED from L1 entry, cycle-013; re-surfaced cycle-016.)** The `Mult` doc comment `palace/linalg/divfree.hpp:63-66` says the output is "the Nedelec dofs of the irrotational portion ... satisfying ∇ × y = 0" (irrotational), but the implemented + L1 + class-doc semantics are **divergence-free** (`Gᵀ M y' = 0`, class doc `palace/linalg/divfree.hpp:28-31`). This is a pre-existing Palace-internal documentation inconsistency, NOT a defect in the `divfree-projector-mutation-rotation` theme (the rewrite honours the *implemented* divergence-free semantics). The `lowering-verifier` should NOT treat the stale comment as a citation against the divergence-free claim. Re-surfaced by the cycle-016 abstractor while authoring the L1>L0 theme (it cites `divfree.hpp:63-66` in sub-pattern B, flagging the stale comment in-line). Documentation inconsistency in Palace, not a theme defect; informational, not blocking. Source: cycle-016 abstractor report §"Open questions" item 2 + sub-pattern B citation note; integrator-per-report promotion (position 1).

```yaml
---
slug: divfree-closure-nesting-constructed-gate-carrying-constructed-gate
opened_at: cycle-016
opened_by: abstractor
last_revisited: null
status: open
relates_to: book/src/L1-L0/divfree-projector-mutation-rotation.md, book/src/L1/divfree-projector.md, book/src/L1/ksp_solve.md, book/src/concepts/constructed-operator-factory.md
---
```

**[OQ] Closure-nesting structural shape: a constructed-operator gate carrying another constructed-operator gate as a sub-field (`P.ksp : Solver[P.M]`).** The cycle-016 `divfree-projector-mutation-rotation` L1>L0 theme is the **first L1>L0 mutation-rotation whose closure carries another constructed-operator gate as a sub-field**: the projector closure `P` (with fields `M`, `WeakDiv`, `Grad`, `bdr_tdof_list_M`, `ksp`) holds `P.ksp`, itself a [`ksp_solve`](../../book/src/L1/ksp_solve.md) constructed-operator gate bound to `P.M` (`SetOperators(*M, *M)`). The CG iteration is interior to `ksp_solve` (the standard Krylov sequential obstruction) and does not leak into the projector theme — at the theme's resolution `ksp->Mult(rhs, psi)` is the opaque `K⁻¹` action. Worth a `cross-layer-cross-cutter` note on whether this nesting recurs across the L1 op set (it does not in the *current* set — no other L1 op carries a constructed gate as a closure sub-field) and whether the pattern warrants a named concept (sibling to [`constructed-operator-factory`](../../book/src/concepts/constructed-operator-factory.md)). NEW this cycle; informational, not blocking. Source: cycle-016 abstractor report §"Open questions" item 3 + §"Open questions / caveats" item 2 (sub-pattern A "inner solve is itself a constructed-operator gate") + sub-pattern C `P.ksp` materialisation; integrator-per-report promotion (position 1).

```yaml
---
slug: l3-l2-body-identity-cg-md-citation-sweep
opened_at: cycle-016
opened_by: lifter
last_revisited: null
status: open
relates_to: book/src/L3-L2/krylov-step-body-identity.md, book/src/spec/slices/cg.md
---
```

**[OQ] The firm L3>L2 theme `book/src/L3-L2/krylov-step-body-identity.md` carries its OWN dangling `cg.md` provenance pointer — needs a sibling lifter (recommended cycle-016+).** The cycle-016 lifter sweep that re-anchored the firm L4 operator entry `book/src/L4/krylov-step.md` (`l4-krylov-step-cg-md-citation-sweep`, RESOLVED below) designated `book/src/L3-L2/krylov-step-body-identity.md` §Verified-against (line 125) as the TERMINAL firm home for its Re-anchors 1/4 (the combinator-miner cycle-002 Claim 1/2 body-identity assertion) — a valid designation because the Claim-2 quote genuinely lives there at line 125 in firm L3>L2 vocabulary (original slice line 360), regardless of that theme's own citation hygiene. But that same firm theme *itself* still cites the now-out-of-range reduced-slice range at its **line 125** (`cg.md:341-362`, the body-identity provenance) — plus a `gmres.md:459-471` co-pointer at lines 125-128 that is out-of-scope-for-a-cg-sweep (gmres.md is a 671-line live slice; that range resolves). The `cg.md:341-362` range dangles for the same cycle-009-reduction reason (`cg.md` is a 165-line stub). They are in a different file (an L3>L2 theme entry, not the L4 operator entry just swept), so re-anchoring them was correctly out-of-scope for the cycle-016 L4 dispatch (touching them would be an unscoped `book/` mutation). **The L3-L2 theme being the terminal home for the L4 sweep's Re-anchors 1/4 does NOT depend on closing this OQ** — pointing the L4 pointer at the theme's §Verified-against §section (which holds the claim in firm L3>L2 vocabulary) is correct regardless; this OQ closes the chain fully (the theme's own provenance pointer is re-anchored or annotated as lifted from the reduced slice). A one-pointer `cg.md` sweep (line 125) plus the out-of-scope `gmres.md` co-pointer note. Recommend a lifter scope `l3-l2-body-identity-cg-md-citation-sweep` applying the cycle-013/014/015/016 lifted-evidence annotation convention verbatim. Low priority; not blocking. NEW this cycle. Source: cycle-016 lifter report (`reports/2026-05-28T214500Z-lifter-l4-krylov-step-cg-sweep/CYCLE.md`) §"Open questions / caveats" item 1 + critic Issue 1/2 (correctly-deferred) + integrator-per-report promotion (position 2).

**[RESOLUTION — cycle-016, integrator-per-report position 2]** OQ `l4-krylov-step-cg-md-citation-sweep` (opened cycle-015, ledger line 2780, above) RESOLVED IN FULL for the L4 file by the cycle-016 lifter sweep (`reports/2026-05-28T214500Z-lifter-l4-krylov-step-cg-sweep/`). All 7 dangling `cg.md:NNN-MMM` range-pointer lines in `book/src/L4/krylov-step.md` re-anchored to terminal firm homes across 6 edit blocks (the 1 bare-filename mention at line 126 correctly left untouched): lines 14/133 (combinator-miner cycle-002 Claim 1/2 body-identity, `cg.md:352-362`) → firm `L3-L2/krylov-step-body-identity.md` §Verified-against + live `arnoldi_step.md:185-188` co-anchor; line 96 (residual-norm hoisting, `cg.md:325-339`) → firm `concepts/derived-view-hoisting.md` §"Worked example: CG residual norm" lines 14-19 (the one genuinely citation-clean terminal home); lines 82/152/171 (CG L4-v0.5 Form B, `cg.md:393-425`) → the RETAINED-live reduced-stub material at `cg.md:27-141` (`cg_first_step` `:52`, `cg_steady_step` `:69`, driver `:95-108`) + firm `L2/krylov-step.md` §Evidence line 138 + `concepts/first-iteration-unrolling.md`; lines 152/170 (CG L4 Form A, `cg.md:172-188`) → firm `L2/krylov-step.md` §Evidence line 138 (the L4 entry's own §Evidence line 176 already declares L2 the transitive narrative anchor). Cross-reference-integrity gate: all 4 NEW `[link]` targets resolve from `book/src/L4/`; the 6 OLD strings matched disk byte-for-byte at dispatch-time re-read; `cg.md` re-confirmed 165-line stub (all `172+` ranges genuinely out-of-range; all `:27-141`/`:52`/`:69`/`:95-108` live anchors in-range). The entry's `firm` status is unchanged (pure citation re-anchor; no signature/semantics/law/variant-axis change). Bounded incidental: Re-anchor 4's trailing future-tense clause (line 133) was firm-up to past-tense reflecting the landed L3>L2 theme + cycle-010 L3 row (the same edit replaced the dangling citation anchoring that stale clause; leaving a half-edited sentence would be incoherent). **Two-hop-to-dangle structural fact** recorded (critic cross-reference-integrity warning, repairer not-needed): two of the four firm-home targets (`L2/krylov-step.md:138`, `L3-L2/krylov-step-body-identity.md:125`) carry their OWN dangling `cg.md` ranges one hop down — NOT a defect in the re-anchors (they point at the firm SECTION holding the claim in firm vocabulary, the correct claim-home semantics, per the cycle-015 precedent at ledger line 2804); the residuals are routed to sibling sweeps (`l2-krylov-step-cg-md-citation-sweep` already open at ledger line 2793; `l3-l2-body-identity-cg-md-citation-sweep` opened NEW immediately above). Deferred to integrator-finalize: formal `status:` field flip to `answered` (answered_in this CYCLE.md) on the `l4-krylov-step-cg-md-citation-sweep` YAML block (ledger line 2780). Resolution-note format used because open-questions.md is append-only (per role-spec / write-authority partition).

**[RESOLUTION — cycle-016, integrator-per-report position 3]** OQ `l2-krylov-step-cg-md-citation-sweep` (opened cycle-015, ledger line 2793, above) ANSWERED for the L2 file by the cycle-016 lifter sweep (`reports/2026-05-28T213650Z-lifter-l2-krylov-step-cg-sweep/`). All 12 dangling `cg.md:NNN-MMM` reduced-slice pointers in `book/src/L2/krylov-step.md` re-anchored to terminal firm homes across 12 edit blocks, plus a repair-added 13th edit closing a sibling `iterative.cpp:244-250` CheckDot mislabel at §Evidence line 171. Mapping: line 7 (CG kernel pattern, `cg.md:103-115`/`:172-188`/`:393-425`) → this entry's §Evidence + firm `L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B (`iterative.cpp:360-486`) + live `cg.md:27-141`; line 9 (sequential-obstruction, `cg.md:341-349`) → firm [`sequential-obstruction`](../../book/src/concepts/sequential-obstruction.md) concept page + `book/src/L3/krylov-step.md` §"Iteration-rotation marker" + live `arnoldi_step.md:194-213`; line 67 (CheckDot breakdown, `cg.md:288` + drifted `iterative.cpp:244-250`) → `iterative.cpp:21-32` (CheckDot real :22/complex :28, called :396/:410/:445/:461) — the `:244-250` was the `ApplyB` helper, drift-corrected; line 69 (first-iteration branch, `cg.md:172-188`/`:393-425`/`:381-391`) → `concepts/first-iteration-unrolling.md` + L0 branch `iterative.cpp:434-441` + live `cg.md:27-141`/`:120-133` (the `forget_beta_prev` projection at :129); line 77 (residual-norm hoisting, `cg.md:325-339`) → firm `concepts/derived-view-hoisting.md` §"Worked example: CG residual norm"; lines 79/81 (primitive enumeration / state-stratum independence, `cg.md:103-115`) → L0 inner loop `iterative.cpp:427-464` (one `A->Mult(p,z)` at :443, `Dot` at :444, axpy at :448-449) via Sub-pattern B; line 116 (preconditioner present/absent, `cg.md:228-257`) → L0 `if (B) ApplyB else z=r` branch in `:427-464` + threading `:377-386` + `L1/ksp_solve.md` Variant axes; line 119 (first-iteration variant, `cg.md:172-188`/`:393-425`) → L0 `iterative.cpp:434-441` + live `cg.md:39-106`; line 138 (slice step bodies) → firm `L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B + live `cg.md:27-141`; line 146 (outer-driver, `cg.md:208-220`/`:430-446`) → live `cg.md:86-106` + L0 `ksp.cpp:296-310` wrapping `iterative.cpp:427-464`; line 171 (repair-added, drifted `iterative.cpp:244-250` CheckDot) → `iterative.cpp:21-32`; line 172 (CheckDot tests, `cg.md:288`) → `iterative.cpp:21-32` + Sub-pattern B coverage note. Cross-reference-integrity gate: all NEW `[link]` targets resolve from `book/src/L2/`; all 13 OLD strings matched disk byte-for-byte at dispatch-time re-read; `cg.md` re-confirmed 165-line stub (all `172+` dangling ranges genuinely out-of-range; all `:27-141`/`:86-106`/`:39-106`/`:120-133` live anchors in-range). The entry's `firm` status is unchanged (pure citation re-anchor + 1 bounded drifted-citation correction; no signature/semantics/law/variant-axis change). The post-apply L2 file is now self-consistent: every `CheckDot` citation resolves to `iterative.cpp:21-32`. **Partial-residual flagged (NOT a defect):** §Evidence lines 138/146 intentionally RETAIN the live-slice citations `cg.md:27-141` / `:86-106` — these are the live retained v0.5 / `cg_solve`-driver material (canonical methodology evidence for `concepts/first-iteration-unrolling.md` per the stub header line 16; NO firmer home exists while the slice is live). If a future cycle fully removes the `cg.md` stub (lifting the v0.5 derivation into `concepts/first-iteration-unrolling.md` proper), these two citations will need a follow-on re-point to the concept page. Routed to the eventual slice-removal audit (see `phase-1-slice-reduction-audit` skill); NOT actionable now. Hence ANSWERED (not RESOLVED-IN-FULL): the dangling-pointer cohort is fully terminated, but two live-slice citations remain dependent on a future slice-removal. Deferred to integrator-finalize: formal `status:` field flip (→ `answered`, answered_in this CYCLE.md) on the `l2-krylov-step-cg-md-citation-sweep` YAML block (ledger line 2793). Resolution-note format used because open-questions.md is append-only (per role-spec / write-authority partition).

**[RESOLUTION — cycle-016, integrator-per-report position 4]** OQ `bundle-6-l0-libceed-operator-file-next-candidate` (opened cycle-015, ledger line 2808, above) RESOLVED IN FULL by the cycle-016 layer-intro-author dispatch (`reports/2026-05-28T213513Z-layer-intro-author-l0-libceed-operator/`). The bundle-6 #5 candidate `palace/fem/libceed/operator.{hpp,cpp}` is now an authored firm L0 file chapter `book/src/L0/fem-libceed-operator-file.md` (new file landed this cycle), registered in `SUMMARY.md` under the L0 Part after `fem-bilinearform-file`. The chapter documents the `ceed::Operator` composite-operator wrapper + `SymmetricOperator` subclass, the matrix-free apply surface (`Mult`/`AddMult`/`MultTranspose`/`AddMultTranspose`/`AssembleDiagonal`), the `CeedOperatorFullAssemble` COO→CSR materialization (`operator.cpp:455-523`) with its load-bearing `set`-vs-accumulate axis, and `CeedOperatorCoarsen` multigrid coarse-operator construction (`operator.cpp:525-585`), with a `test/unit/test-libceed.cpp:284-345` PA/FA-equivalence witness. The two deliberate plain-text forward references in `fem-bilinearform-file.md` (prose @61-66 + Evidence row @158) were retired to live `[`fem-libceed-operator-file`](./fem-libceed-operator-file.md)` links now that the anchor exists. The `fespace.{hpp,cpp}` alternative candidate noted in the original OQ remains a larger, more-foundational surface for a later FE-frontier-driven dispatch (not opened as a standalone OQ — it was a ranking alternative within this OQ, now satisfied by the chosen `libceed/operator.cpp` candidate). Critic: citation-validity pass (dense L0 citations spot-verified against live source via codemap; ~1-line prose/subtree drift is informational/non-blocking, Issue 2). Deferred to integrator-finalize: formal `status:` field flip (→ `resolved`/`answered`, answered_in this CYCLE.md) on the `bundle-6-l0-libceed-operator-file-next-candidate` YAML block (ledger line 2808). Resolution-note format used because open-questions.md is append-only (per role-spec / write-authority partition).

**[RESOLUTION — cycle-016, integrator-per-report position 5]** OQ `partly-constructive-entry-mechanism-validated-eigsolve-convergence-reason-mapping` (opened cycle-014, ledger line 2689, above) CLOSED/ANSWERED by the cycle-016 abstractor re-verification (`reports/2026-05-28T213533Z-abstractor-eigsolve-convergence-reason-mapping/`). The dispatch is the **third independent confirmation** of the partly-constructive negative anchor for `book/src/L1-L0/eigsolve-convergence-reason-mapping.md` (complementing the cycle-013 authoring + cycle-014 lowering-verifier audit, commit `73ecd3e`). All three positive citations re-read exactly this cycle via `mcp__palace-codemap__read_range` (`EPSGetConverged@695`/`EPSConvergedReasonView@699`/`return num_conv@708`; PEP `@1178`/`@1182`/`@1191`; NEP `@1525`/`@1529`, no early return); all five whole-tree negative-anchor searches re-run via `search_text` — `EPS_DIVERGED`/`EPS_CONVERGED`/`GetConvergedReason`/`DIVERGED` all zero hits, `ConvergedReason` only the 3 print-only `*ConvergedReasonView` Views `slepc.cpp:{699,1182,1529}`, `GetConverged` count-readers only (`{695,1178,1525}` in the three `Solve()` bodies + `{276,310}` in spectral-estimation helpers [276 EPS, 310 SVD] + unrelated `ksp.cpp:301`/`iterative.hpp:98`); no `*GetConvergedReason` accessor anywhere. The L1 `EigStatus` sum-type still has exactly 4 variants (`book/src/L1/eigsolve.md:51`). **Verdict: status correctly STAYS `partly-constructive`** — zero materialization, no positive Palace source site reads the SLEPc reason code, the 8-row map remains a faithful forward-looking reconstruction; promotion remains gated on the same unsatisfied upstream behaviour change as parent Sub-pattern B (a `EPSGetConvergedReason` read feeding outer-loop status). This is the partly-constructive **ENTRY** case behaving as designed (a transient gate correctly staying open) — together with cycle-013's eigsolve **EXIT** case (parent Sub-pattern B `LinearSolveFailed`, which PROMOTED), ENTRY + EXIT demonstrate the cycle-012 partly-constructive-first-class invariant working in both directions. The single artifact change landed: an append-only `### Re-verification (cycle-016 abstractor)` subsection (with a `verified_against` YAML block) under `## Verified-against` in the theme file, between the cycle-014 audit block and `## Status`; NO status change, NO SUMMARY/index edit. One residual carry-forward (unchanged, recorded in the entry's §Justification): the 8-row enum exhaustiveness is a **literature anchor** (vs SLEPc's documented enum; SLEPc/PETSc headers not vendored under `reference/`), distinct from and not weakening the source-confirmed Palace-side negative anchor; low risk (enum stable across SLEPc 3.x). Deferred to integrator-finalize: formal `status:` field flip (→ `answered`, answered_in this CYCLE.md, last_revisited cycle-016) on the `partly-constructive-entry-mechanism-validated-eigsolve-convergence-reason-mapping` YAML block (ledger line 2689). Resolution-note format used because open-questions.md is append-only (per role-spec / write-authority partition).

**[RESOLUTION — cycle-016, integrator-per-report position 7]** OQ `l3-chebyshev-downward-prose-iterate-while-refresh` (opened cycle-015, ledger line 2767, above) RESOLVED for its named-sentence scope by the cycle-016 lifter dispatch (`reports/2026-05-28T214012Z-lifter-l3-chebyshev-prose-refresh/`). The §"Value-threaded form (L3 rendering)" closing paragraph in `book/src/L3/chebyshev.md` (lines 236–239) was refreshed from the superseded L4 `foldM`/`forM_` vocabulary onto the firm `iterate_while_pure` family: "the L3 rendering of the L4 `foldM`/`forM_` over static index ranges" → "the L3 rendering of the L4 [`chebyshev`](../L4/chebyshev.md)'s two nested [`iterate_while_pure`](../L4/iterate-while.md) folds over **step-count predicates** (`c.k <= op.order - 1` inner, `s.it <= op.pc_it` outer) — the `iterate_while_pure_L3` tail-recursion lowering image of those bounded folds (per L4 `chebyshev` §"L4 > L3")". The two predicate expressions match the L3 file's own tail-recursion guards (`if k >= op.order`, `if it > op.pc_it`, lines 224/232) by complementation, and the L4 firm body (`book/src/L4/chebyshev.md:155-158, :175-177`) verbatim. Pure vocabulary refresh — NO L3 semantics/structure/status change (entry stays `partial-obstruction`); the code block at lines 211–234 is untouched. Two cross-link targets verified present: `../L4/chebyshev.md` (firm cycle-015) and `../L4/iterate-while.md` (firm cycle-007) — the iterate-while link is a genuinely new inbound link to a firm terminal home, not a relocated dangle. The OLD anchor string matched disk byte-for-byte on fresh re-read (no in-cycle file overlap — reports 1-6 touched distinct files; report 6 touched the L4 sibling `book/src/L4/chebyshev.md`, not this L3 entry). **Scope decision (integrator, per the producer's offer):** this OQ is RESOLVED for the named ~236–239 sentence only; the five sibling `forM_`/`foldM` mentions remaining elsewhere in the same L3 file (lines 46, 55, 96, 475, 480) are tracked by a NEW follow-up OQ `l3-chebyshev-sibling-formm-foldm-prose-sweep` (immediately below) rather than re-scoping this OQ — preserving the cycle-015 named-sentence intent of this slug. Deferred to integrator-finalize: formal `status:` field flip (→ `resolved`, answered_in this CYCLE.md, last_revisited cycle-016) on the `l3-chebyshev-downward-prose-iterate-while-refresh` YAML block (ledger line 2767). Resolution-note format used because open-questions.md is append-only (per role-spec / write-authority partition).

```yaml
---
slug: l3-chebyshev-sibling-formm-foldm-prose-sweep
opened_at: cycle-016
opened_by: integrator-per-report
last_revisited: null
status: open
relates_to: book/src/L3/chebyshev.md, l3-chebyshev-downward-prose-iterate-while-refresh (this ledger, resolved cycle-016 named-sentence scope), l4-chebyshev-residual-formm-foldm-prose-cleanup (this ledger, resolved cycle-016)
---
```

**[OQ] Five sibling `forM_`/`foldM` mentions remain in `book/src/L3/chebyshev.md` outside the cycle-016 named-sentence refresh — companion prose sweep.** The cycle-016 lifter (`l3-chebyshev-downward-prose-iterate-while-refresh`, resolved above) refreshed exactly the one named §"Value-threaded form (L3 rendering)" closing sentence (lines 236–239) onto `iterate_while_pure`, per its named-line dispatch scope. The producer (and critic, independently opening all five) flagged five further mentions of the now-superseded L4 `foldM`/`forM_` vocabulary still in the same L3 file: line 46 (§Context, "`chebyshev`'s loops are bounded `forM_`/`foldM` ranges"), line 55 (§Upward, "the `forM_`/`foldM` binds → tail recursions"), line 96 (§Non-adjacent identity, "the surrounding `forM_`/`foldM` ranges"), and lines 475/480 (§"L3 vs L4 distinction", outer-`forM_`/inner-`foldM` + "the `forM_`/`foldM` binds are tail recursions"). Each is a pure same-shape vocabulary refresh, identical in character to the named-sentence one already landed and to the L4-side sweep `l4-chebyshev-residual-formm-foldm-prose-cleanup` (resolved cycle-016 report 6) — none changes L3 semantics. (Note: line numbers will drift by the named-sentence edit's net +4 lines; the cycle-016 L4 report's grep listed the L3 sites as 46/55/96/237/475/479 pre-its-own-frame — re-grep `forM_\|foldM` in `book/src/L3/chebyshev.md` at dispatch time to relocate.) The fix is a surgical multi-site prose refresh naming `iterate_while_pure`/`iterate_while_pure_L3` + step-count predicates; whole-entry consistency with the now-firm L4 sibling. Low priority; not blocking. Routes to a follow-up companion lifter dispatch on `book/src/L3/chebyshev.md`. Source: cycle-016 lifter report (`reports/2026-05-28T214012Z-lifter-l3-chebyshev-prose-refresh/`) §Open questions + critic META.md §"Five deferred sibling sites" + integrator-per-report position 7 scope decision.

```yaml
---
slug: blas1-variadic-linear-combination-fold-unification
opened_at: cycle-016
opened_by: human (user, post-cycle-016)
last_revisited: null
status: open
relates_to: book/src/L1/axpy.md, book/src/L1/axpby.md, book/src/L1/axpbypcz.md, book/src/L1/scal.md, book/src/L1/dot.md, scaffolding/decisions/axpby-as-primitive.md, book/src/concepts/scalar-promotion.md, book/src/L2/index.md, .claude/agents/combinator-miner.md, .claude/agents/same-layer-cross-cutter.md
---
```

**[OQ — HUMAN-RAISED] The BLAS-1 axpy family (`scal`/`axpy`/`axpby`/`axpbypcz`) is unrecognized as fixed-arity specializations of one variadic linear-combination fold; the combinator-miner's instance-counting heuristic is arity-blind, which is the proximate cause.** User observation (post-cycle-016): the generic form `[(a, t)] → Σ aᵢ·tᵢ` — i.e. `linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N] = foldl (\acc (a,t) -> acc + a*t) zeros` — is the natural base for the whole family: `scal=[(α,x)]`, `axpy=[(α,x),(1,y)]`, `axpby=[(α,x),(β,y)]`, `axpbypcz=[(α,x),(β,y),(γ,z)]`; the in-place mutation variants are the case where one `tᵢ` **aliases the output** (orthogonal to arity); the fusion (single aligned pass over compatible-shape tensors) is the *implementation* of the fold, with `all tᵢ : Tensor[N]` (shape-compatibility) as its precondition. This unified form is **absent at every layer** — the family is represented 3× at fixed arity (L1 leaves, L1>L0 themes, the BLAS-1 L3 identity cohort) and unified 0×. Root-cause analysis (Claude, confirmed against artifact): **(1) the `combinator-miner` is effectively fixed-arity-blind** — its spec (`.claude/agents/combinator-miner.md`) detects "≥3 instances of a recurrent pattern," which fires on a *literally-repeated code shape* (how `krylov-step` was mined) but NOT on a *parametric family whose instances differ only in arity* (axpy/axpby/axpbypcz look like 3 different operators, not 3 instances of one); the spec has zero notion of arity/variadic/fold/parametric-family. **(2) The `axpby-as-primitive` decision (cycle-003) pre-committed to fixed-arity leaves** — its "alternatives considered" axis was fuse-vs-decompose-into-smaller-pieces (`axpby = axpy∘scal`), never generalize-over-arity; its knock-on note tells the `axpbypcz` harvester to "mirror this decision (fuse, don't decompose)," which reads as *keep separate*. **(3) The unification belongs upward at L2/L4** (the fusion + iteration rotations, where Palace's specific call-shape is meant to dissolve), but "fusion erased at L2" was realized as "write each op as base algebra *in place*," not "recognize the family as one fold"; L1 correctly mirrors Palace's three distinct C++ symbols (`AXPY`/`AXPBY`/`AXPBYPCZ`) so 3 firm L1 entries is right *for the L1>L0 rotation* — the variadic abstraction fell in the gap. **(4) No `same-layer-cross-cutter` was ever pointed at the family for unification** — `scalar-promotion` already unified these four along the *element-type* axis (real ⊑ complex), proving the cohort is recognized, but nobody unified the *arity* axis. **Nuance (do not over-unify):** `dot` is a *different* fold (`foldl (+) 0 (zipWith (*) x y)` — reduce-to-scalar, not scalar-weighted tensor sum); the target is a small **algebra of folds** (a tensor-producing linear-combination fold; a scalar-producing inner-product fold), not one mega-combinator. **Two-pronged fix (proposed; routes to batch-4 meta-phase after cycle-018 + a cycle-017 dispatch):** (a) extend the `combinator-miner` spec with an explicit "parametric/variadic-family" detection mode — operators that differ only in arity (number of (scalar, tensor) terms) are candidates for a fold/variadic combinator, distinct from the literal-recurrent-shape heuristic; (b) dispatch a `combinator-miner` (or `same-layer-cross-cutter`) specifically at the BLAS-1 family to propose `linear_combination` as an L2 combinator (a fold), with `scal`/`axpy`/`axpby`/`axpbypcz` as fixed-arity specializations and the in-place forms as output-aliasing, plus a sibling note distinguishing the inner-product fold (`dot`). Priority: see priorities.md §Now (added cycle-016). NOT blocking current work; this is a vocabulary-unification opportunity the methodology currently cannot surface on its own.

## Dropped

(empty — will accumulate)

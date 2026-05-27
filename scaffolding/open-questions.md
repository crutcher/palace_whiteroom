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
- Integrator promotes per-report REPORT.md "Open questions / caveats" sections into this ledger on landing.
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
status: open
---
```

When harvester promotes `axpby` (`y_new = α·x + β·y_old`), the trade-off is: treat `axpby` as a fused primitive (matches L0 shape; one-call lowering) or decompose into `axpy + scal` (cleaner algebra; L0 fusion becomes a transparent performance trick). The `axpby-mutation-rotation` theme (this cycle) is robust to either decision (see Subsumption relation in the theme), but the LHS prose will need a small lift once harvester decides. Record decision in `scaffolding/decisions/axpby-as-primitive.md` once made.

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

## Investigating

(empty)

## Answered

(empty — will accumulate)

## Dropped

(empty — will accumulate)

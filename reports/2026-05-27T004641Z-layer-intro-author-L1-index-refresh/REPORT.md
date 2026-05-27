---
agent: layer-intro-author
invoked_at: 2026-05-27T00:46:41Z
scope: refresh book/src/L1/index.md intro + dep-map prose
status: integrated
integrated_at: 2026-05-27T01:00:00Z
integration_commit: b8332b98300205740c4be4a9b1a2b30a2743dee3
integration_notes: Applied. L1/index.md full refresh; dep-map preserved verbatim per role discipline, then extended cleanly with 9 new rows from cycle-004 harvesters and abstractors. Closes l1-index-refresh and l1-index-refresh-trigger-met.
inputs:
  - .claude/agents/layer-intro-author.md
  - book/src/L1/index.md
  - book/src/L1/axpy.md
  - book/src/L1/dot.md
  - book/src/L1/nrm2.md
  - book/src/L1/axpby.md
  - book/src/L4/index.md
  - book/src/L2/index.md
  - scaffolding/open-questions.md (l1-index-refresh-trigger-met)
skill_uptake:
  - skill: classify-variant-axis — not invoked (no variant-axis claims in scope; prose-only refresh).
  - skill: verify-citation-range — not invoked (no new citations introduced; existing operator chapters retain authority).
  - skill: verify-refinement-surface — not invoked (single file edit, no cross-layer surface changes).
  - skill: plan-sideways-concept-emission — not invoked (no concept emissions in scope).
  - skill: skill-selection — invoked implicitly: none of the active skills are load-bearing for an intro refresh; the work is shell-document curation.
---

# REPORT: Refresh L1 layer intro

## Summary

Refresh `book/src/L1/index.md` to reflect the cycle-002/003 firm-operator landings (`axpy`, `dot`, `nrm2`, `axpby`). The current intro still reads as if the layer is in early bottom-up sweep state; the Working-Notes line "L1 is what `abstractor` produces in early bottom-up sweeps (L0 → L1)" is stale now that all four entries are `firm` and were authored by `harvester` directly. Rewrite:

- **Context**: tighten the four-bullet rotation summary using concrete grounding from the firm operators (cite the actual member-method → free-function rotation pattern; cite the reduction-tree-non-associativity load-bearing-trick discipline).
- **Semantics (overlay)**: expand the one-line placeholder into a short paragraph naming the three semantic motifs visible across the four firm operators (element-wise pure update; mutation-free reduction with load-bearing reduction-tree non-associativity; subsumption chains as algebraic identities rather than new operators).
- **New "Vocabulary cohort" subsection** between Semantics and the dep-map: lists the 4 firm operators with one-line roles, plus the queued next-up primitives (`scal`, `axpbypcz`, `apply_linop`, `nrm2_B`) with their open-question slugs. Makes coverage trajectory visible without restating operator content.
- **Working Notes**: drop the stale "early bottom-up sweep" line; replace with two operational notes (subsumption-as-identity discipline; MPI single-rank scope reminder applies uniformly across L1 reductions).

Dep-map table is preserved **verbatim**: operator rows are harvester-authored content and not within this role's authority.

## Proposed changes

```edit:book/src/L1/index.md
[old]: # L1 — Mutation-lifted forms

Source operations re-expressed as pure functions: explicit input set, output set; in-place mutation and aliasing patterns either erased (workspace/scratch buffers) or made explicit (semantically-meaningful aliasing). The **mutation rotation** layer.

## Context

L1 is the closest pure-functional layer to the source. Structure follows the source loop; what changes is:
- `x.Add(α, y)` → `x_{k+1} = x_k + α·y`
- `A.Mult(x, y)` (writes into `y`) → `y = A·x` (no destination buffer mention)
- Iterative loop mutating iterate in place → functional unfold `state_{k+1} = step(state_k)`
- Reused workspace `tmp` → omitted (the COW backend handles allocation)

## Semantics (overlay)

L1 vocabulary mirrors the source operations but with pure-functional binding. Shape contracts are declared at boundaries (per the bunsen `contracts::unpack_shape_contract!` style).

## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`axpy`](./axpy.md) | `(α, x, y) → α·x + y` | (leaf) | `firm` |
| [`dot`](./dot.md) | `(x, y) → ⟨x, y⟩` (hermitian for complex) | (leaf) | `firm` |
| [`nrm2`](./nrm2.md) | `(x) → √⟨x,x⟩` | `dot` | `firm` |
| [`axpby`](./axpby.md) | `(α, x, β, y) → α·x + β·y` | (leaf; subsumes `axpy`) | `firm` |

## Working Notes

- L1 is what `abstractor` produces in early bottom-up sweeps (L0 → L1).
- Aliasing-aware patterns where aliasing is semantically meaningful (not just buffer reuse) are first-class L1 content.
[new]: # L1 — Mutation-lifted forms

Source operations re-expressed as pure functions: explicit input set, output set; in-place mutation and aliasing patterns either erased (workspace/scratch buffers) or made explicit (semantically-meaningful aliasing). The **mutation rotation** layer.

## Context

L1 is the closest pure-functional layer to the source. Structure follows the source loop; what changes is:

- **In-place vector updates → fresh-value updates.** `y.Add(α, x)` and `y.AXPBY(α, x, β)` (mutating member methods) become `y_new = axpy(α, x, y_old)` and `y_new = axpby(α, x, β, y_old)`. The L0 destination buffer disappears from the signature; the L1>L0 lowering reintroduces it.
- **Receiver-vs-argument asymmetry → first-class conjugation argument.** `ComplexVector::Dot` is a method on `*this`, making the receiver the linear argument and the call argument the conjugated one. At L1 the method-form / free-function-form distinction is erased: `dot` is sesquilinear in fixed argument order (first argument conjugated).
- **Operator-application mutation → pure operator-as-function.** `A.Mult(x, y)` (writes into `y`) → `y = A·x` (no destination buffer mention). Pattern recurs in `apply_BA`, residuals, and B-weighted norms.
- **Pinned reduction tree → reduction as a single semantic step.** L0 `dot` and `nrm2` are layered as `Hypre per-rank kernel + MPI_Allreduce`; L1 names the reduction as one step and records floating-point reduction-tree non-associativity as a **load-bearing** algebraic claim (per `CLAUDE.md` "Optimization tricks vs. base algebra"), not as separate operators.
- **Iterative loop mutating iterate in place → functional unfold** `state_{k+1} = step(state_k)`. Workspace `tmp` is omitted (the COW backend handles allocation).

## Semantics (overlay)

L1 vocabulary mirrors the source operations but with pure-functional binding. Three semantic motifs recur across the firm operators:

1. **Element-wise pure update** (`axpy`, `axpby`) — element-local, reduction-free, every output element depends on exactly one input element from each tensor argument. Algebraic laws are linear-combination facts; constant-folding branches at L0 (e.g., `axpy`'s `α == 1.0` fast path) are transparent performance tricks that disappear at L1.
2. **Mutation-free reduction** (`dot`, `nrm2`) — reduction over the length axis to a scalar. Reduction-tree non-associativity is load-bearing and recorded as an explicit non-law; the MPI collective is folded into the L1>L0 lowering, not the L1 signature.
3. **Subsumption-as-identity rather than dependency** — when one operator is a specialisation of another (`axpy(α, x, y) = axpby(α, x, 1, y)`), both stay in the L1 dep-map as siblings; the relationship is captured by an algebraic law in the subsuming operator, not by a dep-map edge.

Shape contracts are declared at boundaries (per the bunsen `contracts::unpack_shape_contract!` style). Single-rank is in scope per `CLAUDE.md`; MPI collectives appear only in lowering themes.

## Vocabulary cohort

**Firm (4)** — element-wise updates and BLAS-1 reductions:

- [`axpy`](./axpy.md) — vector-scalar fused update; canonical BLAS-1 leaf.
- [`dot`](./dot.md) — Hermitian inner-product reduction (real / complex; `tdot` for unconjugated bilinear).
- [`nrm2`](./nrm2.md) — Euclidean norm; defined as `√dot(x, x)`.
- [`axpby`](./axpby.md) — fused two-scalar two-vector update; subsumes `axpy` and pure-scaling as algebraic identities.

**Queued (open questions)** — small primitives that bottom-out remaining L0 patterns referenced by the firm cohort:

- `scal :: (β, y) → β·y` — pure scaling; cosmetic restatement of `axpby` laws 2 and 3, plus the divisor in `linalg::Normalize`. Slug: `scal-primitive-l1-harvest`.
- `axpbypcz :: (α, x, β, y, γ, z) → α·x + β·y + γ·z` — three-vector generalisation completing the subsumption chain `axpy ≺ axpby ≺ axpbypcz`. Slug: `axpby-axpbypcz-next-harvest`.
- `apply_linop :: (A, x) → A·x` — pure operator-as-function; consumed by L2 `krylov-step` rough-in and by the B-weighted norm.
- `nrm2_B :: (x, B) → √(xᴴ B x)` — energy norm; depends on `dot` and `apply_linop`. Recorded as a boundary in `nrm2`'s entry; deferred to a separate harvest.

## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`axpy`](./axpy.md) | `(α, x, y) → α·x + y` | (leaf) | `firm` |
| [`dot`](./dot.md) | `(x, y) → ⟨x, y⟩` (hermitian for complex) | (leaf) | `firm` |
| [`nrm2`](./nrm2.md) | `(x) → √⟨x,x⟩` | `dot` | `firm` |
| [`axpby`](./axpby.md) | `(α, x, β, y) → α·x + β·y` | (leaf; subsumes `axpy`) | `firm` |

## Working Notes

- The dep-map records **L1-internal** dependencies only. Subsumption chains (`axpy ≺ axpby ≺ axpbypcz`) are stated as algebraic laws in the subsuming operator's entry, not as dep-map edges — both operators stay as siblings in the table.
- Aliasing-aware patterns where aliasing is semantically meaningful (not just buffer reuse) are first-class L1 content; transparent buffer reuse is an L1>L0 lowering concern.
- MPI single-rank scope (per `CLAUDE.md` "Scope") applies uniformly across L1 reductions: the L1 signature never includes a communicator; the L1>L0 lowering reintroduces `MPI_Allreduce` and records bit-deterministic-reduction-order trade-offs.
- Constant-folding fast paths at L0 (e.g., `axpy`'s `α == 1.0` branch, `dot`'s self-dot `&x == &y` branch) are classified as transparent performance tricks and erased at L1 — but only after the critic confirms they are algebraically equivalent to the unfolded form. Load-bearing numerical tricks (the pinned reduction tree) are preserved as explicit non-laws.
```

## Supporting evidence

**Operators currently harvested at this layer** (all `firm`, cycle-002/003):

- `book/src/L1/axpy.md` — cycle-001 (pilot-1).
- `book/src/L1/dot.md` — cycle-002.
- `book/src/L1/nrm2.md` — cycle-003.
- `book/src/L1/axpby.md` — cycle-003.

**Cross-references to adjacent layers**:

- **Up (L2)**: `book/src/L2/index.md` has one rough-in (`krylov-step`) that lists `axpy`/`axpby`, `dot`, `nrm2`, and `apply_linop` as dependencies — three of the four firm L1 operators plus one queued primitive. The L2 dep-map effectively reads against the L1 firm + queued cohort listed in the new "Vocabulary cohort" subsection, which keeps the cross-layer surface coherent.
- **Down (L0)**: L0 is `reference/palace/` source; each L1 operator's `Evidence` section carries the citation set directly. No L0 `index.md` to keep in sync.
- **Lowering**: `book/src/L1-L0/axpby-mutation-rotation.md` (cycle-002 theme) covers `axpy`'s and `axpby`'s sub-patterns under one rotation; `nrm2` and `dot` lowerings remain to be authored as themes. The new Working-Notes bullet about MPI single-rank scope flags the dot/nrm2 lowering shape implicitly.

**Trigger satisfaction** (per `scaffolding/open-questions.md` slug `l1-index-refresh-trigger-met`): the >=3-firm-operator threshold set by pilot-1's `l1-index-refresh` decision is met (4 firm). Refresh scheduled for cycle-004; this report is that refresh.

## Open questions / caveats

1. **Layer-intro-refresh trigger threshold for L2 / L3 / L4** — pilot-1 set ">=3 firm operators" for L1. L2 currently has 1 rough-in (`krylov-step`); L3 and L4 are empty. Question: should the same threshold apply uniformly, or do upper layers warrant a different bar (e.g., L4 is vocabulary-only and may warrant an early-skeleton refresh once the calculus strawman seeds settle)? File as new open question if not already tracked. **Recommendation**: same threshold for L2 (>=3 firm); for L3 / L4 leave the bar at "first firm operator lands" because the layers are not yet populated and the intro establishes structure for subsequent work.

2. **Vocabulary-cohort subsection as a layer-intro pattern** — the "Firm / Queued" split made the coverage trajectory visible without restating operator content. If this works well, it should become a standard sub-section across L_n intros once each layer has firm operators. Worth proposing as a skill or template at meta-phase.

3. **Subsumption-chain discipline note** — the working note about subsumption-as-identity (`axpy < axpby < axpbypcz`) is currently L1-specific prose. As more layers accumulate subsumption chains (e.g., L2 `krylov-step` variants, L4 monadic-effect chains), this might warrant promotion to a `concepts/subsumption-chain.md` cross-cutting page. Out of scope for this invocation; flag for cross-cutter or meta-phase to triage.

4. **`scal` open question** — the queued primitive list references `scal-primitive-l1-harvest` (open question filed by harvester at cycle-003). When `scal` lands, the `axpby` entry's laws 2 and 3 get a cosmetic rewrite and the Vocabulary-cohort "Queued" list shrinks by one. No re-write of the intro is needed at that point — only the cohort subsection's bullet list.

5. **Dep-map entries do not currently annotate firm-vs-rough-in** beyond the `Status` column; format is fine. Noted that L2's single rough-in row uses an inline `(proposed-by: combinator-miner:<timestamp>)` annotation. If we want a unified annotation discipline across L_n intros, propose at meta-phase. Out of scope here.

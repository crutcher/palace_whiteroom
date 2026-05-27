# Decision: `axpby` is a fused primitive at L1 (not decomposed as `axpy ∘ scal`)

**Captured:** cycle-003 (2026-05-27).
**Status:** decided — `axpby` lands as a leaf primitive at L1.
**Origin:** open question `axpby-axpby-scal-decomposition-decision` (opened by cycle-002 abstractor, then routed to cycle-003 harvester via `axpby-axpbypcz-next-harvest`).
**Decided by:** harvester (cycle-003, dispatch 2).

## The question

When `axpby` (`y_new = α·x + β·y_old`) is promoted from rough-in to firm at L1, two formulations are available:

1. **Fused primitive.** `axpby :: (α, x, β, y) → α·x + β·y` is a leaf L1 operator. `axpy` is recoverable as the β=1 specialisation: `axpy(α, x, y) ≡ axpby(α, x, 1, y)`.
2. **Decomposed.** `axpby` is a derived combinator, defined as `axpy(α, x, scal(β, y))` (which requires lifting `scal` as a separate L1 primitive). `axpby` would not appear in the L1 dep-map as a leaf; instead a small note in `axpy`'s use sites references the composition.

## Alternatives considered

- **(1) Fused primitive (chosen).** Matches Palace's L0 shape one-to-one: `ComplexVector::AXPBY` (member, `vector.hpp:131`), free-function template `AXPBY` (`vector.hpp:311`), and three explicit specialisations at `vector.cpp:726-743`. The L1→L0 lowering for `axpby` is a single call; the algebraic identity `axpby(α, x, 1, y) = axpy(α, x, y)` is stated as a subsumption law, not enforced as an L1 dependency.
- **(2) Decomposed as `axpy ∘ scal`.** Cleaner algebraic vocabulary (fewer primitives), and `scal` is needed independently anyway (it appears in normalisation, in CG's `p = β·p + z` line, etc.). The cost is that the L0 fusion (`add(α, x, β, y, y)` at `vector.cpp:729`; the MFEM in-place 5-arg form) becomes a transparent performance trick at L1>L0, and the L1>L0 lowering must recognise the composition pattern instead of pattern-matching the L1 form directly.
- **(3) Both — record duplication.** Carry `axpby` as a primitive AND as a derived composition; the abstractor's `axpby-mutation-rotation` theme uses the primitive form, while L2/L3 unfolding-rotation themes (when they appear) use the decomposed form. Rejected: violates the "duplication explosion in adjacent layers" guard from `feedback_multi_formulation_exploration.md`. The two formulations are not genuinely distinct algebraic objects; they're the same value computed two ways.

## Recommendation: (1) Fused primitive

## Rationale

### Algebraic

- The subsumption `axpy(α, x, y) ≡ axpby(α, x, 1, y)` is a clean, easily-stated law. It means `axpy` does not become orphaned at L1 — both stay in the dep-map, and the L1>L0 lowering theme `axpby-mutation-rotation` (already landed in cycle-002) naturally subsumes `axpy`'s lowering as the β=1 sub-case.
- The fused form composes well with `axpbypcz` (`z = α·x + β·y + γ·z`), the next harvester target: `axpbypcz` reduces to `axpby` when γ=0 (matching the real-path L0 dispatch at `vector.cpp:749-752`). If `axpby` is itself a composition, `axpbypcz`'s algebra fragments into three nested compositions, increasing surface for no benefit.
- Bilinearity in the scalar pair `(α, β)` is a cleaner law statement on the fused form than on the composition — the composition's bilinearity only emerges after unfolding the inner `scal(β, y)`.

### Engineering

- **Single-call L0 lowering.** Palace fuses at L0 because the two-pass form (`y *= β; y += α·x`) costs an extra vector pass and an extra memory round-trip. The L1>L0 lowering recognises the fused L1 form and emits one call. With the decomposed form, the lowering would need to recognise the `axpy ∘ scal` pattern and rewrite it into the fused L0 call — equivalent in outcome but a stronger pattern-matching obligation on the lowering author.
- **The L0 corpus uses `AXPBY` directly.** Survey of Palace shows direct `AXPBY` uses (e.g. in CG's iteration update at `iterative.cpp` — to be confirmed by lowering-verifier). These are not currently expressed in Palace as `y *= β; y += α·x` — Palace authors chose the fused form. The L1 vocabulary should mirror this engineering choice.
- **Matches the cycle-002 abstractor's theme.** The L1>L0 theme `axpby-mutation-rotation` already assumes the fused L1 form (see `book/src/L1-L0/axpby-mutation-rotation.md` and the abstractor's report § "Speculative operators proposed"). Choosing the decomposed form would force a theme-level retraction.

### Trade-offs accepted

- `scal` still needs to land as its own L1 primitive eventually (it has independent uses — normalisation, the `x *= 1.0/norm` line in `vector.hpp:268`). When it lands, `axpby` does not become its composition; it stays a primitive, with `scal` joining as a sibling leaf. This is one extra dep-map row vs. the decomposed alternative, but no extra algebraic surface — the dep-map is a registry, not a derivation graph.
- The β=0 case (`axpby(α, x, 0, y) = scal(α, x)` if we squint; more precisely it discards `y` entirely and copies `α·x`) is an algebraic identity that requires `scal` to exist for a clean statement. Until `scal` lands, the identity is stated as `axpby(α, x, 0, y) = α·x` (treating "scalar-times-vector" as a primitive operation that does not require an L1 operator name to denote).

## Knock-on effects

- The L1 `axpby.md` entry includes the subsumption law as Law #1 in its algebraic-laws section.
- The L1 dep-map row for `axpby` annotates dependencies as `(leaf; subsumes axpy)` — the `subsumes axpy` parenthetical signals that the algebraic relation exists but does not make `axpy` a dependency of `axpby` (both are leaves).
- The abstractor's `axpby-mutation-rotation` theme (`book/src/L1-L0/axpby-mutation-rotation.md`) does not need retraction; its current shape already assumes the fused L1 form. The "Subsumption relation" paragraph in that theme is now load-bearing: it documents the harvester's chosen formulation.
- The future `axpbypcz` harvester invocation can mirror this decision (fuse, don't decompose) for consistency.

## What would change the decision

- If a future cycle finds an L0 site that uses the two-pass form (`y *= β; y += α·x`) and is *load-bearing* for numerical reasons (e.g. a deterministic-reduction guarantee that the fused form would break), the algebraic primitive at L1 might need to be the decomposed form so the load-bearing two-pass is preserved. No such site is known today.
- If `scal` ends up needing extensive algebraic-law treatment (beyond a one-line "scalar-vector multiply" entry), the cost calculus shifts toward decomposition. Currently `scal` is sufficiently trivial that promoting it to a separate primitive is a small bookkeeping cost.

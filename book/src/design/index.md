# Design Artifacts

Design artifacts are documents that *inform* the spec but are not the spec itself: drafts of the L4 calculus, methodology refinements, layer-design rationales, and similar materials.

These are written **whole**, iterated as design proposals, and may be revised non-monotonically — a different lifecycle from the layered-spec chapters, which grow monotonically with friction-driven push-back at lower layers.

## Current artifacts

- The **L4 calculus & spec semantics (active-management surface)** lives in its own top-level `# Semantic surface` Part — at [`book/src/semantics/index.md`](../semantics/index.md). It is the single home for the spec's semantic rules / defs / abstractions (shape semantics + named shape groups, the L4/L3 pseudo-language notation invariant, monad / ownership / reduction-rule conventions, the calculus grammar).

## Future artifacts (planned but not yet drafted)

- The **burn-realization spec** — a separate downstream artifact (not a layer in the stack) describing what burn would need to provide to realize the L4 calculus. To be drafted after the L4 strawman stabilizes.

# L4 — Iteration & step combinators

The iteration-structural vocabulary at L4: the value-threaded loop combinators and the typed-wrapper step kernels that fold inside them. Every iterative algorithm at L4 reduces to one or more of these folds.

- [`iterate-while`](./iterate-while.md) and [`iterate-while-with-prev`](./iterate-while-with-prev.md) are the two members of the strawman §3.7 loop family — a tail-recursive value-threading fold and its carry-bootstrapped (first-iteration-unrolled) variant; the with-prev form degenerates to the plain form when the bootstrap carry `β = ()`.
- [`krylov-step`](./krylov-step.md) is the first firm step-body shape: a typed-wrapper Krylov step against the three-stratum state record, Form A consuming `iterate-while`, Form B consuming `iterate-while-with-prev`.
- [`chebyshev`](./chebyshev.md) is the fixed-degree polynomial smoother — inner-product-free and convergence-test-free, both bounded loops re-expressed as `iterate_while_pure` folds with step-count predicates (the fixed-count-vs-convergence distinction lives in the predicate, not the combinator).

These combinators are demand-pruned: per-step extras pile into a `trajectory` list that the §3.8 derived-view-hoisting rule drops when no downstream consumer reads it. Chapters are alphabetical within this group.

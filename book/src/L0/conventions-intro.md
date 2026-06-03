# Conventions

Cross-cutting Palace / MFEM idioms that L1 operator entries reference rather than
re-state inline. Each convention chapter names one recurring idiom — a mutation
convention, a type duality, a wrapping pattern, or an optimisation-trick
classification — in 2–4 paragraphs of interpretation plus representative citations.
No line-by-line source duplication.

These are the "what does this L0 citation actually mean" notes: an L1 entry citing
`A.Mult(x, y)` or `linalg::AXPY` or a `mutable Vector z` workspace points at the
matching convention chapter here for the idiom, and keeps its own body focused on
the operator's algebra.

See the [L0 overview](./index.md) §Reference-note cohort for how this cohort sits
alongside the file overviews and the overload-set / class-interface chapters.

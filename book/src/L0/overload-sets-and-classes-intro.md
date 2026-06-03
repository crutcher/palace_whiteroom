# Overload sets & class interfaces

Multi-overload and multi-subclass Palace surfaces referenced by L1 / L2 / L4 entries.
Where a single L_n operator collapses many C++ overloads (the `Mult` / `MultTranspose`
/ `AddMult` family) or composes a class hierarchy (the `BaseKspSolver`, MFEM-wrapped
`Solver`, eigensolver, and preconditioner families), the L0 anchor is the overload set
or the class interface as a whole — these chapters are those anchors.

Each chapter names the surface (overload family or class hierarchy), enumerates its
concrete members, and ties it to the higher-layer entries it grounds — `apply_linop`'s
overload collapse, the `solve-monad` composition class, the eigensolve / preconditioner
compositions. They are the navigation hubs for the "one L_n verb, many L0 methods"
relationships.

See the [L0 overview](./index.md) §Reference-note cohort for the full per-surface
descriptions.

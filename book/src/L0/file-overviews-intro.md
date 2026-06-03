# File overviews

At-a-glance overviews of the Palace source files L1 / L2 / L4 entries reference
repeatedly. Each chapter is a file-level navigation hub: what the file houses (its
key classes / free functions / families), the load-bearing duals it carries, and a
handful of representative citations — enough orientation that an operator entry can
point here for "where does this live" instead of re-deriving the file's shape.

The cohort spans the two primary source regions the layered artifact dissects:
`palace/linalg/` (Krylov solvers, preconditioners, smoothers, orthogonalisation,
vector/operator primitives) and `palace/fem/` (finite-element assembly, FE-space
construction, libCEED operators), plus the `palace/utils/communication.hpp` MPI
collectives file.

See the [L0 overview](./index.md) §Reference-note cohort for the full per-file
descriptions and the cross-links into the convention and overload-set / class-interface
cohorts.

# Introduction

The **Palace Whiteroom** is the research-artifact home for an *incremental impedance-matching* specification of the algorithms in [AWS Labs Palace](https://github.com/awslabs/palace) — a parallel finite-element electromagnetic simulator written in C++/HPC — lifted into a language-agnostic, formally-defined graph-evaluation calculus.

The work is part of a broader methodology being developed in the **bunsen** project for lifting traditional C/Fortran tensor-field simulators into representations that fit immutable-tensor, monadic, graph-evaluated host environments. **No port is produced as part of this work.** A separate downstream effort will use the spec to incrementally build burn components; that effort is out of scope here.

This book is the public-facing rendering of the spec. Operational guidance for agents working on the spec lives in `CLAUDE.md` at the repository root. The original phased build spec for the agent system (`BOOTSTRAP.md`) is now a compacted history-stub, with its full text preserved in git history.

## How to read the stack

The specification grows as a **stack of four layers above the cited source**:

- **L0** — cited Palace/MFEM source ranges.
- **L1** — *mutation rotation*. Source operations re-expressed as pure functions.
- **L2** — *fusion rotation*. L1 unfolded into composition of base algebraic primitives.
- **L3** — *iteration rotation*. L2 re-expressed as global tensor-field ops where possible.
- **L4** — a formal graph-evaluation calculus capturing ownership distinctions and monadic coordination of state evolution.

The stack is a **research artifact**, not a target. It is built per-slice, depth-first, with friction at the upper layers pushing structural changes back to the lower layers. See [Methodology — Overview](./methodology/overview.md) for the full process model.

## How to navigate

- [Concepts](./concepts/index.md) — shared primitives and abstract concepts referenced across multiple slices.
- [Design Artifacts](./design/index.md) — methodology drafts that are not the spec itself but inform it. The **L4 calculus strawman** lives here.
- [Meta-Reviews](./meta-reviews/index.md) — records of out-of-cycle friction-integration passes.

Out-of-band agent concerns (role conflicts, framing concerns, tooling gaps) accumulate in the `problems/` directory at the repo root, not in this book.

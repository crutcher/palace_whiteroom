# Specification — Slice Status

The specification grows as a set of **slices** (one per algorithm / routine / coherent piece of Palace), each pushed depth-first through the four-layer stack L1 → L2 → L3 → L4 above the cited L0 source.

This index is maintained by the Synthesizer after every push. It is the **first place to read** to see where the work is.

## Status table

| Slice | Highest layer | Last touched | Status notes |
|-------|---------------|--------------|--------------|
| [CG](./slices/cg.md) | L4 (slice v0.2; against L4 calculus v0.3) | 2026-05-23 | First slice. Negative L3 result for the outer loop (genuine algorithmic sequentiality); positive L3 for per-step body. v0.2 restructure: unpreconditioned CG primary, preconditioned variant; pure-function algorithm (no `Sim`); `residual_norm` as record output pruned per L4 §3.8 when unconsumed. |

## Slice conventions

- **Granularity**: one slice per coherent algorithm or routine.
- **File shape**:
  - Small / medium slices → single file: `book/src/spec/slices/<snake_case_slice_name>.md`, with consistent `## L0` / `## L1` / `## L2` / `## L3` / `## L4` section headings.
  - **Genuinely large slices** → subdirectory **from the start**: `book/src/spec/slices/<slice_name>/`. Split into per-layer files (`l0.md`, `l1.md`, …) or per-aspect files (`overview.md`, `state_types.md`, `step.md`, `convergence.md`, …) per Synthesizer's judgment. The subdirectory should have an `index.md` that orients the reader and links to the per-piece files.
  - Reach for the subdirectory shape when the single-file form would exceed ~400 lines or any L-section would become book-chapter-sized. Splitting after-the-fact is more disruptive than planning multi-file from the start.
- **Per-slice section headings**: each slice file uses the headings `## L0` / `## L1` / `## L2` / `## L3` / `## L4` consistently. Within each, sub-headings as needed.
- **L0 citations**: plain text `reference-relative/path/file.ext:start-end`, e.g., `palace/linalg/cg.cpp:42-67`. Editors with line-aware navigation (VS Code, etc.) resolve these directly against the local clones under `reference/`.
- **Optional agent-facing sections** (may appear on any slice file):
  - **`## Context`** — at the top, after the title: a short paragraph orienting a fresh reader. Why this slice exists, what it covers, what to know before reading the layered content.
  - **`## Working Notes`** — at the bottom, after L4: a loose-form section for issues, todos, ongoing needs, breadcrumbs for the next agent. The place to leave "I noticed X but didn't address it" without forcing it into the question ledger or `problems/`.

## Recommended file template

```markdown
# <slice name>

## Context
(optional — short orientation paragraph)

## L0
- `palace/path/file.cpp:start-end` — what this range is.
- ...

## L1
...

## L2
...

## L3
...

## L4
...

## Working Notes
(optional — todos, open questions tied to this slice, breadcrumbs)
```

## Push history

The full push history (forward / back / sideways) is in the episodic log (`episodic.jsonl` at the repo root once the agent loop is running). This page summarizes only the *current* state.

---
kind: navigational-container (feature group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - feature/lifecycle.L4
    - feature/lifecycle.L1
    - feature/lifecycle.L0
---

# Feature surfaces — spine ROOT (lifecycle)

The **spine-ROOT** grouping holds the single top-level composition root of the feature spine: the **lifecycle** column. It is a **meta-feature** — the sub-kind whose stage-(2) constituents are *other feature columns* plus driver-agnostic firm vocabulary, NOT vocabulary ops directly. Where a leaf feature column (a driver or an output product) composes firm L4/L1 ops into one user-facing feature, the lifecycle column composes the *leaf columns themselves* — it is the `main` → `BaseSolver` dispatch root under which every per-feature column hangs.

The spine reads top-down: this ROOT first, then the driver-leaf columns it dispatches into, then the output-product columns those drivers feed. A reader entering here sees "what does Palace *do* end-to-end (config → mesh → assemble → solve → postprocess → output), and which driver does each `ProblemType` branch select?"; a reader entering a leaf column sees one branch in isolation.

- [`lifecycle`](./lifecycle.L4.md) — the `main` → `BaseSolver` top-level composition root: config-load → mesh → per-`ProblemType` driver dispatch → solution → postprocess → output. Levels: [L4 composition-root](./lifecycle.L4.md) · [L1 composition-root](./lifecycle.L1.md) · [L0 ground-truth surface](./lifecycle.L0.md).

The within-column level ordering is **high→low** (L4 → L1 → L0), the deliberate FEATURE-SURFACE exception to alpha-within-cohort ordering. The lifecycle ROOT is `firm` under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers): its directly-owned driver-agnostic composition — the mesh-build scaffold + the firm [`fold_solve`](../L4/fold_solve.md) state-generated adaptive estimate-mark-refine fold — is firm, and the per-`ProblemType` dispatch is over the per-driver **sibling feature columns**, which are references, NOT blocking constituents (the spine-ROOT meta-feature sub-kind: stage-(2) constituents are *other feature columns*).

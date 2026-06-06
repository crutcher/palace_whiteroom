---
agent: layer-intro-author
invoked_at: 2026-06-06T001708Z
scope: type the 3 high-fan-out L1 BLAS leaves (axpy / axpby / axpbypcz) — rank + edges frontmatter
status: pending
integrated_at: 2026-06-06T013000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied clean by integrator-per-report (staging row 2/2). Frontmatter prepend (rank:firm + edges block) on book/src/L1/{axpy,axpby,axpbypcz}.md; files previously carried no frontmatter. Standalone contribution +2 reachable (axpby/axpbypcz themes left detritus); TRUE CUMULATIVE reachable=119. untyped HELD 60 (linter prose-Status fallback already ranked them firm). rank_violations HELD 0. Resolves c109 repairer OQ l1-blas-leaves-axpy-family-lack-rank-frontmatter (meta-phase to unify). Build EXIT 0, linkcheck2 clean. Committed in cycle-110 finalize atomic commit.
---

# CYCLE: L1 BLAS-leaf typing (axpy family)

cycle-110 (batch-35, cycle 2/3), dispatch D2. Plan item 2 `graded-stack-lazy-tail-typing`;
closes OQ `l1-blas-leaves-axpy-family-lack-rank-frontmatter` (filed by the c109 repairer).

## Summary

Adds an explicit `rank: firm` token + a typed `edges:` block to the three high-fan-out L1
BLAS leaves `book/src/L1/{axpy,axpby,axpbypcz}.md`, which previously carried **no frontmatter
at all**. The typing makes their firm-in-prose status machine-checkable and types their
`depends-on` edges so the lowering-theme tail becomes reachable.

**Frontmatter-only — no prose claim changed.** Each block mirrors the
`book/src/L1/scal.md` / `book/src/L1/apply_linop.md` / `book/src/L1/set_subvector_zero.md`
convention (read first): a `firm` L1 leaf's *blocking* `depends-on` is its **rank-terminal
POSITIVE L0 SOURCE** (via `kind: cites-evidence`), which is what well-founds the `firm` rank
(the `set_subvector_zero` repairer precedent, c104); the `lowers-to` edge to the L1>L0 theme
sits under `depends-on` (the `divfree-projector` precedent); siblings + concept narrative are
`reference`.

### Correction to the OQ premise (recorded honestly)

The OQ / dispatch premise was that these files are **`typed-no-rank`** and that inbound
`depends-on` edges into them "hold the rank invariant only VACUOUSLY." On survey this is
**partly mistaken**: all three chapters carry a prose `## Status` line reading `` `firm` ``,
and the linter has a **prose-`## Status` rank fallback** (`graded_stack_lint.py:425-437`,
priority `rank:` > `firmness:` > feature `status:` > prose `## Status`). So in the BASELINE
they were **already ranked `firm`** (counted in the firm histogram, NOT in the untyped-60) and
**already reachable** via their inbound edges from reachable L2 consumers. Consequently:

- `untyped` does **NOT** drop 60→57 (the dispatch's predicted delta) — it **HOLDS at 60**,
  because these files were never in the untyped set (prose-firm gave them a rank; the
  *missing* thing was the `edges:` block / outbound typed edges, not the rank).
- The real win is on **Axis 2 (reachability)**: typing the outbound `depends-on`
  `lowers-to` edges pulled the previously-detritus L1>L0 themes
  `L1-L0/{axpby,axpbypcz}-mutation-rotation` into the reachable set.

**[repairer correction, c110] Reachability attribution fixed.** An earlier draft of this
section credited D2 with the whole reduce-chain cascade; that was a measurement contamination
(D2's verification ran with D1's parallel `book/src/L4/krylov-step.md` write present in the
working tree). D2's **TRUE STANDALONE** reachability contribution is **reachable 107→109 (+2),
detritus −2**, rescuing ONLY the two `lowers-to` themes `L1-L0/axpby-mutation-rotation` and
`L1-L0/axpbypcz-mutation-rotation`. The reduce-chain nodes are D1's cascade, not D2's. See the
corrected table + node list below.

This is the correct, honest disposition (the GROUND-don't-remove spirit, §2f): the edges were
genuinely missing and the nodes were genuine dependencies; typing the faithful
citation-grounded edges grounds the chain. The OQ is still **resolved** — the three leaves now
carry explicit `rank:` + `edges:` frontmatter (no longer relying on the prose fallback), which
is exactly what the OQ asked for; only the predicted *metric* (the untyped count) was wrong.

## Before / after linter numbers

`python3 tools/graded-stack-lint/graded_stack_lint.py` (and `--show-inbound`):

`python3 tools/graded-stack-lint/graded_stack_lint.py` (and `--show-inbound`), **D2's three
edits applied ALONE on a clean tree** (the corrected, isolated measurement):

| metric | BASELINE | AFTER (D2 alone) | delta |
|---|---|---|---|
| `rank_violations` | 0 | 0 | **HELD 0** |
| `reachable from roots` | 107 | **109** | **+2** |
| `detritus` | 152 | **150** | **−2** |
| `untyped (warning)` | 60 | 60 | HELD (see OQ-premise correction above) |
| firm histogram | 201 | 201 | HELD (already prose-firm) |

**Nodes that LEFT detritus → newly reachable (2, zero regressions):**
`L1-L0/axpby-mutation-rotation`, `L1-L0/axpbypcz-mutation-rotation` — the two themes my
`lowers-to` edges point at directly. **Nodes that ENTERED detritus: NONE.**

**[repairer correction, c110]** The earlier draft of this table reported +12 / −12 and listed
ten additional reduce-chain nodes (`L2/inner_product`,
`L2-L1/inner-product-fold-specialization`, `L2/orthogonalize`,
`L3/{apply_linop,dot,inner_product,nrm2}`, `L4/{dot,inner_product,nrm2}`) as newly reachable.
That was a **contaminated reading**: D2's verification ran while D1's parallel
`book/src/L4/krylov-step.md` write was present in the working tree, so D1's reduce-cohort
grounding cascade leaked into D2's column. Frontmatter typing of the axpy *leaves* cannot
rescue the dot/nrm2/inner_product reduce chain — nothing in that chain points INTO the axpy
family; the leaves are downstream of L2 consumers, not the reduce verbs. Those ten nodes are
**D1's** rescue and remain detritus under D2 alone.

**The true CUMULATIVE reachable (after BOTH D1 and D2 land) must be re-measured by the
integrator at apply time** — it is NOT simply the sum of the two columns (the cohorts may
overlap), so trust neither D2's old +12 nor an arithmetic D1+D2 add; re-run the linter on the
post-apply tree.

**`--show-inbound` confirms the rescued themes now show inbound edges (the rescue is MEASURABLE):**
```
L1-L0/axpby-mutation-rotation     <-  L1/axpby, L1/axpy
L1-L0/axpbypcz-mutation-rotation  <-  L1/axpbypcz
```
And the inbound `depends-on` edges INTO the axpy family (now firm→firm rests, no longer
vacuous, since each leaf is explicitly `rank: firm` resting on rank-terminal L0 cites):
```
L1/axpy      <-  L1/divfree-projector, L1/eliminate_rhs, L2/axpy, L2/krylov-step, L2/linear_combination
L1/axpby     <-  L2/axpby, L2/krylov-step, L2/linear_combination
L1/axpbypcz  <-  L2/axpbypcz, L2/krylov-step, L2/linear_combination
```

(Verification method: applied all three edits to working tree, ran the linter + `--show-inbound`
+ `--json` detritus diff, then `git checkout` reverted all three files. `git status` on my
write-set `book/src/L1/{axpy,axpby,axpbypcz}.md` is clean; the only `book/` modification is
`L4/krylov-step.md`, which is **D1's disjoint parallel write — NOT mine, not touched**.)

## Proposed changes

Each block is a frontmatter prepend onto a file that currently begins with its `# <name>`
H1 (no existing frontmatter). All `cites-evidence` L0 ranges below were re-verified with
`citecheck --anchor` against on-disk source (all `[ok]`); the ranges mirror each chapter's own
`## Evidence` section verbatim.

```edit:book/src/L1/axpy.md
[old]:
# axpy

Mutation-lifted vector-scalar fused update: `y_new = α·x + y_old`. The canonical BLAS-1 primitive at L1.
[new]:
---
layer: L1
operator: axpy
rank: firm
# Graded-stack scheme (cycle-110, D2): firm-in-prose BLAS-1 leaf — fully-specified
# positive L0 source + syntactic-identity laws (the firm-on-positive-structure escape).
# The blocking depends-on is the rank-terminal POSITIVE L0 SOURCE (cites-evidence),
# which is what makes the `firm` rank well-founded (the set_subvector_zero precedent).
# The lowers-to edge points at the axpby-mutation-rotation theme, which covers axpy's
# sub-patterns as the β=1 specialisation (there is NO standalone axpy-mutation-rotation).
edges:
  depends-on:
    - target: palace/linalg/vector.cpp:702-712
      kind: cites-evidence        # free-function AXPY(double,Vector,Vector) + α==1.0 fast-path
    - target: palace/linalg/vector.cpp:715-723
      kind: cites-evidence        # AXPY(complex,ComplexVector,ComplexVector) overload
    - target: palace/linalg/vector.hpp:115-118
      kind: cites-evidence        # ComplexVector::AXPY / Add member decl
    - target: palace/linalg/vector.hpp:305-307
      kind: cites-evidence        # free-function template AXPY decl
    - target: L1-L0/axpby-mutation-rotation
      kind: lowers-to             # axpy's lowering = β=1 specialisation in the axpby theme
  reference:
    - L1/axpby
    - L1/axpbypcz
    - L1/scal
    - L2/linear_combination
    - concepts/axpy
    - concepts/scalar-promotion
---

# axpy

Mutation-lifted vector-scalar fused update: `y_new = α·x + y_old`. The canonical BLAS-1 primitive at L1.
```

```edit:book/src/L1/axpby.md
[old]:
# axpby

Mutation-lifted fused two-scalar two-vector update: `y_new = α·x + β·y_old`.
[new]:
---
layer: L1
operator: axpby
rank: firm
# Graded-stack scheme (cycle-110, D2): firm-in-prose fused BLAS-1 leaf — matches three
# Palace L0 entry points exactly, syntactic-identity laws (firm-on-positive-structure).
# Blocking depends-on = rank-terminal POSITIVE L0 SOURCE (cites-evidence) → well-founds
# the `firm` rank. The lowers-to edge points at the axpby-mutation-rotation theme.
edges:
  depends-on:
    - target: palace/linalg/vector.cpp:726-730
      kind: cites-evidence        # AXPBY(double,Vector,double,Vector) → MFEM add(...)
    - target: palace/linalg/vector.cpp:732-737
      kind: cites-evidence        # AXPBY(complex,...) → member form
    - target: palace/linalg/vector.cpp:739-743
      kind: cites-evidence        # AXPBY(double,ComplexVector,...) real-scalar-on-complex
    - target: palace/linalg/vector.hpp:130-131
      kind: cites-evidence        # ComplexVector::AXPBY member decl
    - target: palace/linalg/vector.hpp:309-311
      kind: cites-evidence        # free-function template AXPBY decl
    - target: L1-L0/axpby-mutation-rotation
      kind: lowers-to             # the L1>L0 lowering theme this leaf lowers to
  reference:
    - L1/axpy
    - L1/axpbypcz
    - L1/scal
    - L2/linear_combination
    - concepts/scalar-promotion
---

# axpby

Mutation-lifted fused two-scalar two-vector update: `y_new = α·x + β·y_old`.
```

```edit:book/src/L1/axpbypcz.md
[old]:
# axpbypcz

Mutation-lifted fused three-scalar three-vector update: `z_new = α·x + β·y + γ·z_old`.
[new]:
---
layer: L1
operator: axpbypcz
rank: firm
# Graded-stack scheme (cycle-110, D2): firm-in-prose fused BLAS-1-extended leaf — matches
# three Palace L0 entry points exactly, syntactic-identity laws (firm-on-positive-structure).
# Blocking depends-on = rank-terminal POSITIVE L0 SOURCE (cites-evidence) → well-founds
# the `firm` rank. The lowers-to edge points at the axpbypcz-mutation-rotation theme.
edges:
  depends-on:
    - target: palace/linalg/vector.cpp:745-758
      kind: cites-evidence        # AXPBYPCZ(double,...) real-real with γ==0 branch
    - target: palace/linalg/vector.cpp:760-765
      kind: cites-evidence        # AXPBYPCZ(complex,...) → member form
    - target: palace/linalg/vector.cpp:767-772
      kind: cites-evidence        # AXPBYPCZ(double,ComplexVector,...) real-scalar-on-complex
    - target: palace/linalg/vector.hpp:133-136
      kind: cites-evidence        # ComplexVector::AXPBYPCZ member decl
    - target: palace/linalg/vector.hpp:313-316
      kind: cites-evidence        # free-function template AXPBYPCZ decl
    - target: L1-L0/axpbypcz-mutation-rotation
      kind: lowers-to             # the L1>L0 lowering theme this leaf lowers to
  reference:
    - L1/axpy
    - L1/axpby
    - L1/scal
    - L2/linear_combination
    - concepts/scalar-promotion
---

# axpbypcz

Mutation-lifted fused three-scalar three-vector update: `z_new = α·x + β·y + γ·z_old`.
```

## Supporting evidence — citation provenance

Every `cites-evidence` and `lowers-to` target below was verified on disk (citecheck `--anchor`
all `[ok]`; lowering themes confirmed present via `ls book/src/L1-L0/`). The L0 ranges are
transcribed verbatim from each chapter's existing `## Evidence` section.

**axpy** (`cites-evidence` → POSITIVE L0 source, the rank-terminal ground truth):
- `palace/linalg/vector.cpp:702-712` — free-function `AXPY(double, Vector, Vector)` with the `α == 1.0` fast-path branch.
- `palace/linalg/vector.cpp:715-723` — `AXPY(complex, ComplexVector, ComplexVector)` overload (scalar-promotion site at :715-718).
- `palace/linalg/vector.hpp:115-118` — `ComplexVector::AXPY` / `Add` member decl.
- `palace/linalg/vector.hpp:305-307` — free-function template `AXPY` decl.
- `lowers-to` → `L1-L0/axpby-mutation-rotation` — **EXISTS on disk.** There is **no** standalone
  `axpy-mutation-rotation.md`; the `axpby-mutation-rotation` theme covers axpy's sub-patterns A/B/C
  as its β=1 specialisation (confirmed: the theme body §"Sub-pattern A — bare axpy", and the theme
  is named in `axpy.md`'s own L1>L0 prose). The theme is `firm`-in-prose (no `rank:` frontmatter
  yet — pre-scheme), so this `lowers-to` edge is currently a depends-on into a typed-no-rank node
  (linter `continue`s, warn-not-fail, no rank violation; the rescue value is the reachability flip).

**axpby** (`cites-evidence`):
- `palace/linalg/vector.cpp:726-730` — `AXPBY(double, Vector, double, Vector)` → MFEM `add(α,x,β,y,y)`.
- `palace/linalg/vector.cpp:732-737` — `AXPBY(complex, ComplexVector, complex, ComplexVector)` → member form.
- `palace/linalg/vector.cpp:739-743` — `AXPBY(double, ComplexVector, ...)` real-scalar-on-complex (promotion site).
- `palace/linalg/vector.hpp:130-131` — `ComplexVector::AXPBY` member decl.
- `palace/linalg/vector.hpp:309-311` — free-function template `AXPBY` decl.
- `lowers-to` → `L1-L0/axpby-mutation-rotation` — **EXISTS on disk**, `firm`-in-prose.

**axpbypcz** (`cites-evidence`):
- `palace/linalg/vector.cpp:745-758` — `AXPBYPCZ(double, ...)` real-real with the `γ == 0` branch.
- `palace/linalg/vector.cpp:760-765` — `AXPBYPCZ(complex, ...)` → member form.
- `palace/linalg/vector.cpp:767-772` — `AXPBYPCZ(double, ComplexVector, ...)` real-scalar-on-complex (promotion site).
- `palace/linalg/vector.hpp:133-136` — `ComplexVector::AXPBYPCZ` member decl.
- `palace/linalg/vector.hpp:313-316` — free-function template `AXPBYPCZ` decl.
- `lowers-to` → `L1-L0/axpbypcz-mutation-rotation` — **EXISTS on disk**, `firm`-in-prose.

### Edge-classification notes
- The `scaffolding/decisions/axpby-as-primitive.md` decision record (referenced in-prose by
  `axpby.md` / `axpbypcz.md`) is **NOT** added as an edge target: the linter resolves slugs to
  `book/src/<slug>.md`, and that decision lives outside `book/src/`. It stays an in-prose
  reference only (correct — it is not a DAG node).
- `L2/linear_combination` is a `reference` (a sibling/consumer cross-link, navigational), not a
  `depends-on`: the leaves do not *depend on* their L2 consumer. (The blocking direction is the
  reverse — `L2/linear_combination → L1/axpy` etc., which already exists inbound.)
- Sibling leaves + `concepts/*` are `reference` per the scheme (sibling cross-links + concept
  narrative pointers carry no liveness).

## Open questions / caveats

- **OQ-premise metric correction (not a defect, recorded for the meta-phase):** the dispatch
  predicted `untyped` 60→57; the true effect is `untyped` HOLDS 60, and D2-alone `reachable`
  +2 / `detritus` −2 (corrected from the earlier contaminated +12/−12 reading — see the
  repairer correction in §"Before / after linter numbers"). Cause: the linter's prose-`## Status` rank fallback already ranked these
  three `firm`, so they were never `untyped` — they lacked outbound *typed edges*, not a rank.
  Suggest the meta-phase note in the friction ledger that **"lacks rank frontmatter" should be
  checked against the prose-`## Status` fallback** before predicting an untyped-count delta
  (a prose-`## Status: firm` chapter with no frontmatter is firm-typed, just edge-untyped).
- **The two `lowers-to` target themes (`L1-L0/{axpby,axpbypcz}-mutation-rotation`) are
  themselves still pre-scheme** (`firm`-in-prose, no `rank:`/`edges:` frontmatter). They are
  now *reachable* (my edges rescued them from detritus) but `typed-no-rank`. A future
  lazy-tail-typing tranche should add their `rank: firm` + `edges:` blocks (lowering themes
  `depends-on` both their L1 form and their L0 source per the scheme §5 lowering-edge rule);
  until then the `lowers-to` depends-on edges into them are warn-not-fail (not a rank
  violation). Flag: `l1-l0-axpy-family-themes-need-scheme-frontmatter`.
- Write-set hygiene confirmed: `git status` on `book/src/L1/{axpy,axpby,axpbypcz}.md` is clean
  (verification edits reverted via `git checkout`); the lone `book/` modification
  `book/src/L4/krylov-step.md` is D1's disjoint parallel write and was not touched by this
  dispatch.

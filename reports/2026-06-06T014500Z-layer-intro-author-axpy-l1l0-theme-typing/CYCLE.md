---
agent: layer-intro-author
invoked_at: 2026-06-06T014500Z
scope: cycle-111 D2 — type the two axpy-family L1>L0 lowering-theme leaves (frontmatter-only scheme hygiene)
status: pending
integrated_at: 2026-06-06T021500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-111 D2, report 2 of 2 (FRONTMATTER-ONLY scheme hygiene). Applied verbatim per the 2 ## Proposed changes anchor-prepend blocks — from-scratch edges: blocks on book/src/L1-L0/axpby-mutation-rotation.md + book/src/L1-L0/axpbypcz-mutation-rotation.md (both had a BARE H1, zero pre-existing frontmatter; disjoint from D1). Reachability-NEUTRAL (both themes already reachable via inbound reference edges, confirmed by --show-inbound). Producer correctly DECLINED a dispatch-suggested reference: L1-L0/dot-mutation-rotation (don't-manufacture discipline). TRUE CUMULATIVE (both D1+D2): reachable 122, detritus 137, STRONGER GARBAGE 26, rank_violations 0, untyped 60. All per-report gates PASS/N/A; all-pass clean critic-set (no repairer pass). RESOLVES OQ l1-l0-axpy-family-themes-need-scheme-frontmatter (meta-phase to unify/close). Carry-forward body note: pre-existing prose mislabel at axpby-mutation-rotation.md:25-26 deferred to a future body pass. cargo make book EXIT 0, linkcheck2 clean. Batch-35 BATCH-CLOSING cycle."
---

# CYCLE: L1-L0 axpy-family theme typed-edge frontmatter (scheme hygiene)

## Summary

Authored from-scratch typed `edges:` frontmatter blocks on the two L1>L0
axpy-family lowering themes (`book/src/L1-L0/axpby-mutation-rotation.md`,
`book/src/L1-L0/axpbypcz-mutation-rotation.md`), which previously carried **no
frontmatter**. Each block follows the c110 `L1/axpy.md` typed-scheme convention
for an L1>L0 lowering-theme leaf: `rank: firm`, blocking `depends-on` edges to
the rank-terminal POSITIVE L0 source via `cites-evidence`, and navigational
`reference` edges to the firm L1 parents.

This is **scheme hygiene, NOT a reachability flip** — both themes were already
reachable from their firm L1 parents via legacy edges (confirmed below). The win
is making the typed-edge graph explicit + scheme-consistent. Effect (holding
D1's parallel orthogonalize edits constant): all linter numbers HELD —
reachable, detritus, untyped, and rank_violations unchanged.

FRONTMATTER-ONLY: no chapter bodies were edited. Discharges OQ
`l1-l0-axpy-family-themes-need-scheme-frontmatter` (filed c110 D2).

## Proposed changes

### `book/src/L1-L0/axpby-mutation-rotation.md` — PREPEND frontmatter

Insert the following frontmatter block at the top of the file, immediately
before the existing `# axpby-mutation-rotation` heading (the file currently has
NO frontmatter):

```yaml
---
layer: L1-L0
theme: axpby-mutation-rotation
rank: firm
# Graded-stack scheme (cycle-111, D2): L1>L0 lowering-theme leaf, typed from scratch
# (discharges OQ `l1-l0-axpy-family-themes-need-scheme-frontmatter`). The theme is a
# firm mutation-rotation: structural + transparent-trick rewrites over fully-specified
# positive L0 source. The blocking depends-on edges are the rank-terminal POSITIVE L0
# SOURCE (cites-evidence) the rewrite rests on, which makes the `firm` rank well-founded.
# The firm L1 parents (axpy/axpby) reach this theme via their own legacy depends-on
# edges; here they are recorded as `reference` see-also (this is scheme hygiene, NOT a
# reachability flip — the theme was already reachable from those parents).
edges:
  depends-on:
    - target: palace/linalg/vector.cpp:710
      kind: cites-evidence        # real path `y.Add(alpha, x)` (α≠1 branch)
    - target: palace/linalg/vector.cpp:715-723
      kind: cites-evidence        # complex AXPY overloads (ComplexVector)
    - target: palace/linalg/vector.cpp:739-743
      kind: cites-evidence        # AXPBY real-x→ComplexVector member body
    - target: palace/linalg/vector.cpp:745-758
      kind: cites-evidence        # AXPBYPCZ real-real body (the 3-vector generalisation)
    - target: palace/linalg/vector.hpp:116-117
      kind: cites-evidence        # ComplexVector::AXPY decl + Add alias
  reference:
    - L1/axpy
    - L1/axpby
---
```

### `book/src/L1-L0/axpbypcz-mutation-rotation.md` — PREPEND frontmatter

Insert the following frontmatter block at the top of the file, immediately
before the existing `# axpbypcz-mutation-rotation` heading (the file currently
has NO frontmatter):

```yaml
---
layer: L1-L0
theme: axpbypcz-mutation-rotation
rank: firm
# Graded-stack scheme (cycle-111, D2): L1>L0 lowering-theme leaf, typed from scratch
# (discharges OQ `l1-l0-axpy-family-themes-need-scheme-frontmatter`). Firm mutation
# rotation: structural rewrites + a transparent γ==0 constant-folding sub-rule over
# fully-specified positive L0 source. The blocking depends-on edges are the rank-terminal
# POSITIVE L0 SOURCE (cites-evidence) the rewrite rests on, which makes the `firm` rank
# well-founded. The firm L1 parent (axpbypcz) reaches this theme via its own legacy
# depends-on edge; recorded here as `reference` see-also — scheme hygiene, NOT a
# reachability flip (the theme was already reachable from that parent).
edges:
  depends-on:
    - target: palace/linalg/vector.cpp:745-758
      kind: cites-evidence        # real-real free-function body (with γ==0 branch)
    - target: palace/linalg/vector.cpp:749-751
      kind: cites-evidence        # γ==0 fast-path calling MFEM add(α,x,β,y,z)
    - target: palace/linalg/vector.cpp:755-756
      kind: cites-evidence        # γ≠0 slow-path AXPBY(...); z.Add(...)
    - target: palace/linalg/vector.hpp:313-316
      kind: cites-evidence        # free-function template AXPBYPCZ decl
  reference:
    - L1/axpbypcz
    - L1/axpby
    - L1/axpy
---
```

## Citation verification (each `cites-evidence` target, verified on-disk)

All ranges confirmed against `reference/palace/palace/linalg/vector.{cpp,hpp}`
via direct on-disk `Read` (codemap END lines are drift-prone; these are the real
on-disk ranges).

**axpby theme:**

| Citation | On-disk content | Verdict |
|---|---|---|
| `vector.cpp:710` | `y.Add(alpha, x);` — the α≠1 `else` branch of real `AXPY(double,Vector,Vector)` | ✓ exact |
| `vector.cpp:715-723` | `AXPY(double, ComplexVector, ComplexVector)` (715-718) + `AXPY(complex, ComplexVector, ComplexVector)` (720-724); 715-723 covers both overload bodies through the second `y.AXPY(alpha, x);` | ✓ (both complex AXPY overloads) |
| `vector.cpp:739-743` | `AXPBY(double alpha, const ComplexVector &x, double beta, ComplexVector &y)` body `{ y.AXPBY(alpha, x, beta); }` (the real-x→ComplexVector AXPBY overload) | ✓ exact |
| `vector.cpp:745-758` | `AXPBYPCZ(double,Vector,double,Vector,double,Vector)` real-real body, incl. the γ==0/γ≠0 branch — the 3-vector generalisation the axpby theme names as the parent of axpby | ✓ exact. NOTE: this range is the AXPBYPCZ real-real body, NOT an AXPBY body. The theme body (line 26) cites it as the "free-function template" generalisation; the cite is faithful to what the chapter rests on, though the body prose mislabels it "member form" (a body-content issue, out of this frontmatter-only scope — flagged below). |
| `vector.hpp:116-117` | `void AXPY(std::complex<double> alpha, const ComplexVector &x);` (116) + `void Add(...) { AXPY(alpha, x); }` alias (117) | ✓ exact |

**axpbypcz theme:**

| Citation | On-disk content | Verdict |
|---|---|---|
| `vector.cpp:745-758` | `AXPBYPCZ(double,...,Vector &z)` real-real body, opens `template <>`+sig at 745-747, body 748-758 with the `if (gamma == 0.0)` branch | ✓ exact |
| `vector.cpp:749-751` | `if (gamma == 0.0)` (749) `{` (750) `add(alpha, x, beta, y, z);` (751) — the γ==0 fast-path calling MFEM `add` | ✓ exact |
| `vector.cpp:755-756` | `AXPBY(alpha, x, gamma, z);` (755) `z.Add(beta, y);` (756) — the γ≠0 slow-path | ✓ exact |
| `vector.hpp:313-316` | `// Addition z = alpha * x + beta * y + gamma * z.` (313) + `template <typename VecType, typename ScalarType>` (314) + `void AXPBYPCZ(...)` decl (315-316) | ✓ exact |

## `reference` edge justification (faithful-edge discipline)

- **axpby theme** `reference: L1/axpy, L1/axpby` — both are the firm L1 parents
  this theme is the lowering for; both are cross-linked in the theme body
  (`L1/axpy` at lines 16, 170; the axpby LHS shape, now firm as `L1/axpby`, at
  lines 20-23). Confirmed `L1/axpby.md` carries `rank: firm`.
- **axpbypcz theme** `reference: L1/axpbypcz, L1/axpby, L1/axpy` — `L1/axpbypcz`
  is the primary firm L1 parent (body lines 25, 194); `L1/axpby` + `L1/axpy` are
  the firm cross-linked siblings the body names as the related operators (lines
  298, 301). Confirmed `L1/axpbypcz.md` carries `rank: firm`.
- **`L1-L0/dot-mutation-rotation` NOT added** — the prompt suggested a
  `reference` to `dot-mutation-rotation` "where the body cites it", but
  `grep dot-mutation` over BOTH theme files returns nothing: neither body cites
  it. Per the faithful-edge / don't-manufacture-an-edge discipline, I declined
  to add a `reference` edge for a relationship the chapter does not actually
  carry. (If a future body edit introduces a dot-rotation cross-link, the edge
  should be added then.)

## Linter results (isolated effect)

D1 ran in parallel editing `L2/orthogonalize.md` + `L1/orthogonalize.md`
(DISJOINT from my `L1-L0/axpb*` files). To isolate MY effect I diffed the linter
with my two edits applied vs `git stash`-reverted, holding the rest of the tree
constant.

| metric | before my edits | after my edits | delta |
|---|---|---|---|
| reachable from roots | 119 | 119 | **HELD** |
| detritus nodes | 140 | 140 | **HELD** |
| untyped (warning) | 60 | 60 | **HELD** |
| rank violations | 0 | 0 | **HELD 0** |
| typed nodes | 295 | 295 | HELD (themes were already counted as nodes via legacy prose edges) |
| rank histogram | unchanged | unchanged | HELD |

My contribution is **reachability-neutral scheme hygiene** exactly as the prompt
predicted: the typed `edges:` blocks make explicit the graph that was already
implicit via legacy prose dep-map edges (the themes already showed inbound edges
`L1/axpby, L1/axpy → axpby-theme` and `L1/axpbypcz → axpbypcz-theme` in
`--show-inbound`, both before and after).

**D1-attribution note (per prompt):** my very first baseline lint (before D1's
edits landed in the tree) read reachable 122; the current isolated baseline
reads 119. That 122→119 shift is **D1's** orthogonalize-subtree effect, NOT
mine — I do not claim it. My isolated effect is the HELD row above.

`--show-inbound` confirmation (after my edits):
```
L1-L0/axpby-mutation-rotation     <-  L1/axpby, L1/axpy
L1-L0/axpbypcz-mutation-rotation  <-  L1/axpbypcz
```

## Book cleanliness

Applied → linted → reverted. `git status book/` is clean (my two files
reverted; D1's write-set untouched). Frontmatter emitted as proposed-changes
only, per the dispatch-phase write-authority partition.

## Open questions / caveats

- **OQ `l1-l0-axpy-family-themes-need-scheme-frontmatter` RESOLVED** by this
  dispatch (both axpy-family L1>L0 themes now have typed scheme frontmatter,
  pending integration of the proposed-changes blocks above).
- **Body-prose mislabel in `axpby-mutation-rotation.md` (lines 25-26)** — the
  body calls `vector.cpp:739-743` the "member form" and `vector.cpp:745-758`
  the "free-function template" of `AXPBYPCZ`. On-disk, `739-743` is the
  `AXPBY(double, ComplexVector, ...)` overload (a member-delegating AXPBY, not
  AXPBYPCZ) and `745-758` is the AXPBYPCZ real-real free-function body. This is
  a body-content accuracy issue, OUT of this frontmatter-only scope — flagging
  for a future harvester/lowering-verifier body pass; the frontmatter
  `cites-evidence` comments above use the accurate on-disk labels.

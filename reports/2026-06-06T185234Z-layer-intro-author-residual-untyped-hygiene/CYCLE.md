---
agent: layer-intro-author
invoked_at: 2026-06-06T185234Z
scope: graded-stack residual untyped hygiene (D2, cycle-115) — type 4 reachable-but-pre-scheme nodes
status: pending
integrated_at: 2026-06-06T211500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-115 D2. Applied clean (staging row 1). Frontmatter-only typed-edge hygiene on book/src/L1/fe_collection.md (rank:firm + edges:) + frontmatter-PREPEND on book/src/L1-L0/{dot,nrm2,scal}-mutation-rotation.md (each had NO frontmatter). +1 reachable (132->133): the fe_collection->L1-L0/fe-collection-construction-rotation lowers-to edge rescued that theme from baseline detritus; detritus 127->126. rank_violations HELD 0, unresolved HELD 0, untyped HELD 60. Promoted OQ graded-stack-prose-status-inference-masks-untyped. Build EXIT 0, no build-repair. All per-report gates PASS/N-A. citecheck 20 ok/0 failing."
---

# CYCLE: residual untyped typed-edge hygiene (L1/fe_collection + 3 BLAS-1 L1>L0 themes)

## Summary

FRONTMATTER-ONLY typed-edge hygiene for the four c114-grounded, already-reachable,
pre-scheme nodes named in the D2 dispatch. Each gains an explicit `rank: firm` + a typed
`edges:` block (scheme §5/§6 block-mapping form), replacing the linter's *prose-inferred*
rank with declared, faithful edges:

1. `book/src/L1/fe_collection.md` — `rank: firm` + `depends-on` (`cites-evidence` →
   the L0 `ConstructFECollections` template; `lowers-to` → its L1>L0 theme) + `reference`
   → `L1/fe_space` (consumer relationship).
2–4. `book/src/L1-L0/{dot,nrm2,scal}-mutation-rotation.md` — these carry **NO YAML
   frontmatter at all** (they start directly at the `#` heading). Each gains a
   frontmatter block with `rank: firm` + `depends-on` `cites-evidence` edges to the core
   L0 source each theme lowers to. Per the dispatch constraint I do **NOT** re-add the
   op→theme `depends-on` (`L1/op →lowers-to→ theme`, which landed c114 on the op side);
   these get their OWN outbound `cites-evidence` edges to L0 only.

**Key measurement finding (honest delta) [metric narrative CORRECTED by repairer
cycle-115, per critic Issue 1]:** the move does NOT move `untyped` or `rank_violations`,
but it is NOT reachability-neutral — it is reachability-**beneficial**: `reachable 132→133`
(+1), `detritus 127→126` (−1). All four nodes already register `rank=3.0` and
`untyped=False` in the linter because `derive_rank` falls back to the prose `## Status`
line (`read_status_line`) when frontmatter lacks `rank:`/`status:` — the three themes'
`## Status` sections lead with `` `firm` ``, and `fe_collection` carries `status: firm`.
So they were never in the linter's `untyped` LIST to begin with (that list is the 60
genuinely-rankless L0-file-overview / meta-review / methodology pages) — hence `untyped`
does not drop. This is a genuine **representation upgrade** (declared typed edges replace
prose inference). The reachability +1 arises because `fe_collection`'s new outbound
`depends-on` `lowers-to → L1-L0/fe-collection-construction-rotation` edge RESCUES that
theme (a baseline-detritus node) into the live set: reachability is a forward mark-sweep
FROM the roots, so the outbound `depends-on` from an already-reachable node (`fe_collection`)
pulls its target live. The producer's original narrative reasoned about inbound-to-root
edges (none added) and so mispredicted neutrality. `rank_violations` HOLDS 0, `unresolved`
HOLDS 0. See §Standalone linter delta.

## Proposed changes

### 1. `book/src/L1/fe_collection.md`

Replace the frontmatter block (insert `rank:` + `edges:` ahead of the closing `---`).

```edit:book/src/L1/fe_collection.md
[old]:
---
status: firm
harvested_by: harvester:2026-06-02T160332Z-harvester-fe-collection
cycle: cycle-065
---
[new]:
---
status: firm
harvested_by: harvester:2026-06-02T160332Z-harvester-fe-collection
cycle: cycle-065
# Graded-stack scheme (cycle-115 D2 hygiene; chapter previously carried only `status: firm`,
# NO typed edges — the rank was prose-inferred from `## Status`). This firm L1 schedule operator
# is a leaf in L1 vocabulary (a pure enumeration producing a `[FECollection]` list; no L1 op is
# invoked — §Dependencies), so it carries no `composes` edge. It rests on its positive L0 source
# (the whole `ConstructFECollections` template body, cites-evidence, rank-terminal ground truth)
# and lowers through its L1>L0 construction-rotation theme. The producer->consumer relation to
# `fe_space` (which consumes one of the produced collections) is navigational, NOT a dependency
# (§Dependencies: "a consumed-by relation ... not a dependency") -> `reference`.
# Well-foundedness rank(u) <= rank(v): this node firm (rank 3); the cites-evidence target is
# rank-terminal L0 ground truth; the lowering theme `fe-collection-construction-rotation` is
# typed `rank: firm` (this cycle, D2) so 3 <= 3 holds.
rank: firm
edges:
  depends-on:
    - target: palace/fem/multigrid.hpp:22-73
      kind: cites-evidence        # ConstructFECollections<FECollection> whole template body; close brace verified on disk at :73 (return fecs; at :72, } at :73)
    - target: L1-L0/fe-collection-construction-rotation
      kind: lowers-to             # the L1>L0 construction-rotation theme (cycle-065 D3; §Downward :175-180)
  reference:
    - L1/fe_space                  # producer->consumer: each produced FECollection is a per-level fe_space input (§Dependencies; NOT a depends-on)
---
```

### 2. `book/src/L1-L0/dot-mutation-rotation.md`

Prepend a frontmatter block (the file currently starts at the `# dot-mutation-rotation`
heading with no frontmatter).

```edit:book/src/L1-L0/dot-mutation-rotation.md
[old]:
# dot-mutation-rotation

The mutation rotation for the BLAS-1 inner-product reduction. Lowers the pure L1 form
[new]:
---
# Lowering theme (L1>L0), cycle-115 D2 hygiene: this file previously had NO frontmatter at
# all — its rank was prose-inferred from the `## Status` `firm` token. Per graded-stack
# scheme §5 a theme's rank = min(endpoint ranks); the L1 endpoint (`L1/dot`) is firm (rank 3)
# and the L0 endpoints are rank-terminal ground truth, so the theme is firm. Per the D2
# dispatch constraint the op->theme edge (`L1/dot →lowers-to→ this theme`) lives on the L1
# op side (landed c114) and is NOT re-added here; this theme carries only its OWN outbound
# `cites-evidence` edges to the L0 reduction surface it lowers to (the `Dot` template, the
# real/complex `LocalDot` leaves, and the `Mpi::GlobalSum`/`GlobalOp` collective). All ranges
# self-verified on disk via citecheck --anchor this invocation.
rank: firm
edges:
  depends-on:
    - target: palace/linalg/vector.hpp:246-253
      kind: cites-evidence        # the `Dot(comm,x,y)` template = LocalDot + Mpi::GlobalSum two-step (Sub-pattern A)
    - target: palace/linalg/vector.cpp:263-267
      kind: cites-evidence        # ComplexVector::Dot body = x·conj(y) = yᴴ x, this==&y self-dot fast path (Sub-pattern B; the conjugate-pair source)
    - target: palace/linalg/vector.cpp:665-672
      kind: cites-evidence        # real LocalDot(Vector,Vector) via hypre_SeqVectorInnerProd (Sub-pattern C)
    - target: palace/linalg/vector.cpp:674-685
      kind: cites-evidence        # complex LocalDot four-real-dot lift, Im = LocalDot(xi,yr)−LocalDot(xr,yi)
    - target: palace/utils/communication.hpp:266-270
      kind: cites-evidence        # Mpi::GlobalSum(len,buff,comm) → GlobalOp(...,MPI_SUM,...)
    - target: palace/utils/communication.hpp:246-249
      kind: cites-evidence        # GlobalOp body = MPI_Allreduce(MPI_IN_PLACE,...) — the collective
---

# dot-mutation-rotation

The mutation rotation for the BLAS-1 inner-product reduction. Lowers the pure L1 form
```

### 3. `book/src/L1-L0/nrm2-mutation-rotation.md`

Prepend a frontmatter block.

```edit:book/src/L1-L0/nrm2-mutation-rotation.md
[old]:
# nrm2-mutation-rotation

The mutation rotation for the BLAS-1 Euclidean-norm reduction. Lowers the pure L1 form
[new]:
---
# Lowering theme (L1>L0), cycle-115 D2 hygiene: previously NO frontmatter (rank prose-inferred
# from `## Status` `firm`). Per graded-stack scheme §5, theme rank = min(endpoint ranks); the L1
# endpoint (`L1/nrm2`) is firm (rank 3), L0 endpoint rank-terminal, so the theme is firm. The
# op->theme edge (`L1/nrm2 →lowers-to→ this theme`, c114) lives on the op side and is NOT re-added.
# This theme carries its OWN outbound `cites-evidence` edges to the L0 `Norml2` one-line
# composition it lowers to (and the `Dot` leaf + collective the chain bottoms out in — the
# inherited dot sub-theme, recorded here as the cited evidence of nrm2's own L0 surface).
# All ranges self-verified on disk via citecheck --anchor this invocation.
rank: firm
edges:
  depends-on:
    - target: palace/linalg/vector.hpp:254-259
      kind: cites-evidence        # Norml2(comm,x) template body = std::sqrt(std::abs(Dot(comm,x,x))) (Sub-pattern A; the load-bearing line)
    - target: palace/linalg/vector.hpp:246-253
      kind: cites-evidence        # the Dot leaf = LocalDot + Mpi::GlobalSum the chain bottoms out in (inherited dot sub-theme)
    - target: palace/utils/communication.hpp:266-270
      kind: cites-evidence        # Mpi::GlobalSum(len,buff,comm) → GlobalOp(...,MPI_SUM,...)
    - target: palace/utils/communication.hpp:246-249
      kind: cites-evidence        # GlobalOp body = MPI_Allreduce(MPI_IN_PLACE,...) — the collective
---

# nrm2-mutation-rotation

The mutation rotation for the BLAS-1 Euclidean-norm reduction. Lowers the pure L1 form
```

### 4. `book/src/L1-L0/scal-mutation-rotation.md`

Prepend a frontmatter block.

```edit:book/src/L1-L0/scal-mutation-rotation.md
[old]:
# scal-mutation-rotation

The mutation rotation for the BLAS-1 vector-scalar rescale. Lowers the pure L1
[new]:
---
# Lowering theme (L1>L0), cycle-115 D2 hygiene: previously NO frontmatter (rank prose-inferred
# from `## Status` `firm`). Per graded-stack scheme §5, theme rank = min(endpoint ranks); the L1
# endpoint (`L1/scal`) is firm (rank 3), L0 endpoint rank-terminal, so the theme is firm. The
# op->theme edge (`L1/scal →lowers-to→ this theme`, c114) lives on the op side and is NOT
# re-added. This theme carries its OWN outbound `cites-evidence` edges to the L0 in-place
# receiver-mutating member overloads it lowers to (the complex `ComplexVector::operator*=`
# definition + its declaration). The real path is `mfem::Vector::operator*=(double)` — upstream
# MFEM, not Palace source — so it is named in prose, not cited as a Palace L0 edge.
# All ranges self-verified on disk via citecheck --anchor + direct Read of the close brace.
rank: firm
edges:
  depends-on:
    - target: palace/linalg/vector.cpp:203-227
      kind: cites-evidence        # ComplexVector::operator*= definition; si==0.0 two-real-call branch (:207-211) + general complex forall_switch kernel (:212-225); close brace verified on disk at :227
    - target: palace/linalg/vector.hpp:98-99
      kind: cites-evidence        # ComplexVector &operator*=(std::complex<double> s); decl + `// Scale all entries by s.` comment
---

# scal-mutation-rotation

The mutation rotation for the BLAS-1 vector-scalar rescale. Lowers the pure L1
```

## Faithful-citation derivation

Every `cites-evidence` range was pulled from the theme/chapter prose and **re-verified on
disk this invocation** (`citecheck --anchor` for in-range anchor presence + direct `Read`
for the close-brace END line, since `--anchor` does not validate the upper bound):

| edge target | anchor | citecheck | END close-brace verified |
|---|---|---|---|
| `multigrid.hpp:22-73` | `ConstructFECollections` @25 | ok | `}` at :73 on disk (return fecs; :72) — planner-flagged END, **no drift** |
| `vector.hpp:246-253` (Dot tmpl) | `Dot` @248,250 | ok | `}` at :253 (codemap) |
| `vector.hpp:254-259` (Norml2 tmpl) | `Norml2` @257 | ok | `}` at :259 |
| `vector.cpp:263-267` (ComplexVector::Dot) | `ComplexVector::Dot` @263 | ok | `}` at :267 |
| `vector.cpp:665-672` (real LocalDot) | `LocalDot` @665 | ok | — |
| `vector.cpp:674-685` (complex LocalDot) | `LocalDot` @674,678,682,683 | ok | — |
| `vector.cpp:203-227` (operator*=) | `ComplexVector` @203 | ok | `}` at :227 verified by direct on-disk Read |
| `vector.hpp:98-99` (operator*= decl) | — | (decl, read_range confirmed) | n/a |
| `communication.hpp:266-270` (GlobalSum) | `GlobalSum` @267 | ok | `}` at :270 |
| `communication.hpp:246-249` (GlobalOp) | `GlobalOp` @246 | ok | `}` at :249 |
| `L1-L0/fe-collection-construction-rotation` | (book node) | exists on disk | n/a |
| `L1/fe_space` | (book node) | exists on disk | n/a |

The `multigrid.hpp` END is the one the planner flagged for brace-boundary drift: the
on-disk close brace of `ConstructFECollections` is **line 73** (`std::reverse` :70,
`return fecs;` :72, `}` :73). The chapter's existing `:22-73` is exact — no END
adjustment needed.

**Edges deliberately NOT added (faithful-edge-or-finding):**
- The three themes get **no** `lowers-to L1/<op>` back-edge — the dispatch is explicit that
  the op→theme `depends-on` lives on the op side (c114). Adding the back-edge would
  duplicate the relationship and is outside the D2 scope.
- `nrm2` theme does not cite the `vector.cpp` `LocalDot` leaves directly (it lowers to the
  one-line `Norml2` template + inherits the dot collective); I cite the `Dot` leaf
  (`vector.hpp:246-253`) it bottoms out in, matching the theme's own §"Sub-pattern A"
  citation set, rather than restating the full dot leaf set (that is dot's theme).
- `scal` real path (`mfem::Vector::operator*=(double)`) is **upstream MFEM, not Palace
  source** (the theme says so explicitly) — not cited as a Palace L0 `cites-evidence`
  edge; only the Palace-owned complex `ComplexVector::operator*=` def + decl are cited.

## Standalone linter delta

Baseline (clean tree, confirmed this invocation):
`files=355, typed=295, untyped=60, roots=36, reachable=132, detritus=127, rank_violations=0, unresolved=0`.

**Measured pre-state of the four nodes (probed via the linter's own `build_graph`):** all
four ALREADY register `untyped=False, rank=3.0, reachable (not detritus)`. The linter's
`derive_rank` falls back to the prose `## Status` line when frontmatter lacks
`rank:`/`status:` (`read_status_line`, anchored on the leading `firm` token), so:
- `L1/fe_collection` — `status: firm` frontmatter → rank 3.0 (already typed-for-untyped-flag).
- `L1-L0/{dot,nrm2,scal}-mutation-rotation` — no frontmatter, but `## Status` leads with
  `` `firm` `` → rank 3.0.

None of the four is in the JSON `untyped` LIST (that list is the 60 genuinely-rankless
pages: 26 L0 file-overviews, 26 meta-reviews, 4 methodology, 2 design, 1 introduction, 1
SUMMARY). The `grep -L "^edges:"` pre-check correctly shows they lack a frontmatter
`edges:` block — but the linter does not count a prose-`## Status`-ranked node as
`untyped`, so authoring the explicit edges does NOT move `untyped`. It IS, however,
reachability-beneficial (see correction below):

**Post-edit (CORRECTED by repairer cycle-115 — critic measured the applied edits;
integrator should confirm):**
`files=355, typed=295, untyped=60, roots=36, reachable=133, detritus=126, rank_violations=0, unresolved=0`.
`rank_violations` HOLDS 0 (every new edge is firm→firm or
firm→rank-terminal-L0). `unresolved` HOLDS 0 (both book-node targets exist on disk:
`L1/fe_space`, `L1-L0/fe-collection-construction-rotation`; L0 `:lo-hi` cites are
ground-truth, not book nodes). `untyped` does NOT drop (the four were never in the list).
`reachable 132→133` (+1), `detritus 127→126` (−1): `fe_collection`'s new outbound
`depends-on` `lowers-to → L1-L0/fe-collection-construction-rotation` edge RESCUES that
theme (a baseline-detritus node) into the live set. The original prediction of `reachable`
HELD was a reasoning error (inbound-to-root vs the forward-from-root mark-sweep) — a
beneficial delta, not a regression.

**Disposition: I did NOT apply the edits** (FRONTMATTER-ONLY proposed-changes per
dispatch discipline — no direct `book/` writes in Phase 2). The tree is clean for the
integrator. The standalone delta above is a *prediction from the verified pre-state*, not
a measured post-state, because applying would violate the write-authority partition.

**Net value of the item:** the upgrade is real — it replaces the linter's *prose
inference* (fragile: a `## Status` reword that drops the leading `firm` token would
silently un-rank the node) with *declared, faithful typed edges* + explicit `rank: firm`.
It closes `graded-stack-residual-untyped-hygiene`. The framing "untyped may drop
slightly" in the dispatch is **not borne out** on the `untyped` count — these nodes were
already rank-inferred, so on that axis the win is representational robustness. There IS,
however, a count move on the OTHER axis: `reachable 132→133` / `detritus 127→126` (the
fe_collection→fe-collection-construction-rotation rescue; see corrected delta above).
(Contrast the genuinely-rankless 60: those WOULD drop `untyped` when typed.)

## Open questions / caveats

- `oq:graded-stack-prose-status-inference-masks-untyped` — the linter's `derive_rank`
  prose-`## Status` fallback means a node with a firm `## Status` but no frontmatter
  `rank:`/`edges:` reports as **typed (rank 3)** and is **invisible to the `untyped`
  warning**, even though it carries zero declared graph edges. This is why the four D2
  targets did not show as untyped despite `grep -L "^edges:"` flagging them. Two readings:
  (a) intended (the prose status IS the rank signal during P1 rollout); (b) a blind spot
  (a chapter can have zero declared edges yet never surface for typing). The
  `graded-stack-residual-untyped-hygiene` item targeted exactly these prose-ranked-but-
  edge-less nodes — suggesting (b) is the maintenance concern. Flagging for the meta-phase:
  consider a separate linter signal `ranked-but-edgeless` (rank set, zero declared
  `depends-on`/`reference` edges, not a genuine leaf) so this residual class is
  enumerable rather than hidden inside the typed count. The D2 four are now cleared
  regardless.
- The `scal` theme's real path is upstream MFEM (`mfem::Vector::operator*=(double)`), so
  scal's only Palace L0 `cites-evidence` edges are the complex overload. This is faithful
  (the theme says the real path is not Palace source) but means scal's edge set is
  thinner than dot/nrm2 — expected, not a gap.
- No `record-<name>-needs-definition-home` flags: none of the four names an
  as-yet-undefined record (FECollection is MFEM-owned-read-as-given per the chapter; the
  BLAS-1 themes operate on `Tensor[N]` flat vectors, no record).

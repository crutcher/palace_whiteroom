---
agent: combinator-miner
invoked_at: 2026-06-07T120000Z
scope: RE6 combinator-arity-notes refactor — eliminate the 8 axpy/scal arity leaves into the linear_combination combinator (replace-and-propagate)
status: pending
integrated_at: 2026-06-07T112037Z
integration_commit: 331a5ed
integration_notes: "cycle-124 (batch-40 opener) D6. Applied clean. RE6 DISCHARGED — the 8 scal/axpy/axpby/axpbypcz arity-leaf standalone nodes (L2+L3) ELIMINATED into linear_combination #arity-specializations (delete-not-ground): per-arity unique-L0 anchors folded in, 8 chapters git rm'd, SUMMARY + L2/L3 index dep-maps de-registered, ~90 inbound links re-pointed. 1 OQ promoted (inner-product-family-re-style-elimination-candidate). NOTE: D6's body/index re-point sweep MISSED two FRONTMATTER depends-on edges (L3/normalize->L3/scal, L3/orthogonalize->L3/axpy) — repaired at finalize (re-pointed to L3/linear_combination; lint-invisible to linkcheck2, caught by graded-stack unresolved_depends_on_targets). RE6 disposition flagged for the batch-40 meta baseline-exceptions update."
---

# CYCLE: Combinator candidate — RE6 axpy/scal arity-leaf elimination into `linear_combination`

## Summary

This is the **RE6 combinator-arity-notes refactor** (a replace-and-propagate execution, not a
fresh combinator discovery — the `linear_combination` combinator is already firm at L2 (c018,
inverted-to-entry c049) and L3 (c050)). The 8 BLAS-1 arity-specialization leaves
`L2/{scal,axpy,axpby,axpbypcz}` + `L3/{scal,axpy,axpby,axpbypcz}` currently survive as
**standalone DAG nodes** (SUMMARY entries + index dep-map rows + their own files), even though
they were already reduced to thin specialization-stubs cycles 051/052. They are the
`scal ≺ axpy ≺ axpby ≺ axpbypcz` arity-1/2/2/3 readouts of the single variadic fold
`linear_combination :: [(Scalar, Tensor[(S: ...)])] -> Tensor[$S]`. RE6's promotion condition
is to **ELIMINATE them off-spine** (the higher-value disposition: delete the nodes, not ground
them) — DEMOTE each into an `## Arity specializations` table row INSIDE the combinator chapter
at its own layer, preserving every unique L0 anchor, then de-register the standalone chapter
(SUMMARY + index dep-map) and re-point every inbound link to the combinator's
`#arity-specializations` section. The two combinator chapters already carry a
`### Arity specializations` section (L2 `:94`, L3 `:53`) listing the four members as readout
labels; this refactor MOVES the leaves' unique-L0-anchor payload INTO those sections and
deletes the eight files. Net: 8 standalone nodes → 0; the combinator is the sole family entry.
**Layer placement is unchanged** — the demotion is purely within each layer (L2 leaves → L2
combinator section; L3 leaves → L3 combinator section); no leaf moves layer.

This is a **parametric-family** disposition (parameter axis = **arity**; combining step =
`acc + scal a t`; identity = `zeros[$S]`; unifying fold-law = concatenation-homomorphism
`lc (p ++ q) = lc p + lc q`, the law that makes the four arities one operator —
`L2/linear_combination.md:160-169` law 2). **Over-unification guard (PRESERVED):** the
`inner_product`/`dot`/`nrm2` siblings (reduce-to-`Scalar`, different codomain + combining step)
are **NOT in RE6 scope** and **NOT touched** — they remain standalone in the same SUMMARY/index
groups. RE6 is scoped to the 4 `linear_combination` members only (the scope verbatim names
exactly `L2/axpy`, `L2/axpby`, `L2/axpbypcz`, `L2/scal` + the 4 L3 siblings).

## Pattern instances

The arity family + its unique-L0-anchor payload (the content to fold into the combinator):

- **L2 arity-1 `scal`** (`book/src/L2/scal.md`) — unique L0: `vector.hpp:98-99`
  (`operator*=` decl), `vector.cpp:207-211` (the `si==0.0` real fast-path / promotion site
  inside `vector.cpp:203-227`), `vector.hpp:262-270` (`linalg::Normalize` fused `nrm2+scal`).
  The only family member whose L0 surface is a receiver-mutating `*=` member, not a free
  function.
- **L2 arity-2 `axpy`** (`book/src/L2/axpy.md`) — unique L0: `vector.hpp:115-118`
  (`ComplexVector::AXPY` + `Add`/`Subtract` aliases decl), `vector.cpp:276-311`
  (`ComplexVector::AXPY` def + element-wise kernels), `vector.cpp:714-718`
  (real-α-on-complex forwarding overload, scalar-promotion anchor), `vector.cpp:720-724`
  (complex-α overload). Second coefficient fixed to 1.
- **L2 arity-2 `axpby`** (`book/src/L2/axpby.md`) — unique L0: `vector.hpp:130-131`
  (`ComplexVector::AXPBY` member decl), `vector.cpp:732-737` (complex-complex specialisation),
  `vector.cpp:739-743` (real-scalar-on-complex promotion anchor). General second coefficient.
- **L2 arity-3 `axpbypcz`** (`book/src/L2/axpbypcz.md`) — unique L0: `vector.hpp:133-136`
  (`ComplexVector::AXPBYPCZ` member decl), `vector.cpp:745-758` (real-real incl. the `γ==0`
  arity-collapse branch `:749-751` + the `γ≠0` two-call split `:755-756`),
  `vector.cpp:760-765` (complex-complex specialisation), `vector.cpp:767-772`
  (real-scalar-on-complex promotion anchor). Maximal fixed-arity L0 symbol.
- **L3 arity-1 `scal`** (`book/src/L3/scal.md`) — same receiver-mutating `*=` surface as L2
  `scal` PLUS additional live consumer call sites: `vector.cpp:203-227` (`operator*=` def incl.
  `:206-211` shape branch), `vector.hpp:98-99`, `vector.hpp:262-270` (`Normalize`),
  `iterative.cpp:632, 811` (GMRES Arnoldi normalisation), `operator.cpp:661, 673`
  (`Normalize` sites), `nleps.cpp:486-491` (eigenvector normalisation).
- **L3 arity-2 `axpy`** (`book/src/L3/axpy.md`) — `vector.cpp:276-311` (`ComplexVector::AXPY`),
  `vector.cpp:702-712` (free-function `AXPY` incl. the load-bearing `α==1.0` fast-path),
  `vector.cpp:715-718` (promotion site), `vector.hpp:115-118`, `vector.hpp:305-307`.
- **L3 arity-2 `axpby`** (`book/src/L3/axpby.md`) — `vector.cpp:726-730` (real-real MFEM
  fused `add(α,x,β,y,y)`), `vector.cpp:732-737` (complex-complex), `vector.cpp:739-743`
  (promotion), `vector.hpp:130-131`, `vector.hpp:309-311`. The no-fast-path member.
- **L3 arity-3 `axpbypcz`** (`book/src/L3/axpbypcz.md`) — `vector.cpp:745-758` (real-real
  incl. `γ==0` `:749-751`), `vector.cpp:760-765` (complex-complex), `vector.cpp:767-772`
  (promotion), `vector.hpp:133-136`, `vector.hpp:313-316`.

All anchors verified present in the leaf chapters this dispatch (the leaves were self-verified
on-disk via `tools/citecheck` at cycle-052; no re-localization claim is made — this is an
in-layer move of already-verified anchors, the propagate-half discipline).

## Proposed combinator

- **Slug**: `linear_combination` (ALREADY FIRM at L2 + L3 — no new chapter; this refactor
  ELIMINATES the 8 leaf nodes into the existing combinator's `## Arity specializations` section).
- **Layer**: unchanged — L2 leaves fold into `L2/linear_combination` §"Arity specializations";
  L3 leaves into `L3/linear_combination` §"Arity specializations". No cross-layer move.
- **Parameter axis**: **arity** (term-list length 1/2/2/3). Siblings: `scal` (len 1),
  `axpy` (len 2, trailing coeff fixed to 1), `axpby` (len 2, both free), `axpbypcz` (len 3).
- **Combining step**: `acc + scal a t`; **identity** `zeros[$S]` (the fold seed).
- **Unifying fold-law**: concatenation-homomorphism `lc (p ++ q) = lc p + lc q`
  (`L2/linear_combination.md:160-169` law 2) — the law that makes the four arities one operator
  (`axpbypcz`'s 3-list = `axpby` 2-list ++ `scal` 1-list).
- **Over-unification guard (do NOT subsume)**: `dot`/`nrm2`/`inner_product` — reduce-to-`Scalar`,
  different codomain + combining step (zip-and-reduce-over-`S` vs scale-and-accumulate-over-the-
  term-list). NOT in RE6 scope; left standalone.

## Proposed changes

The integrator executes the following. It is split into five mechanical groups: (A) fold-in to
the combinator sections, (B) delete the 8 files, (C) SUMMARY.md de-registration, (D) index
dep-map row drops + narrative edits, (E) inbound-link re-pointing. The canonical re-point
anchors are `../L2/linear_combination.md#arity-specializations` and
`../L3/linear_combination.md#arity-specializations` (intra-Part: `./linear_combination.md#...`).

> **Anchor note (warning-policy=warn).** `book/book.toml` sets `warning-policy = "warn"` for
> linkcheck2, so a fragment-anchor mismatch is a WARNING, not a hard error; only a link to a
> **missing file** is the hard exit-101 error. To make the `#arity-specializations` fragment
> resolve cleanly, the integrator SHOULD shorten the two existing section headings to a clean
> anchor while folding in (group A): change
> `### Arity specializations (the family members, as notes under the combinator)` →
> `### Arity specializations` in BOTH `L2/linear_combination.md` (`:94`) and
> `L3/linear_combination.md` (`:53`). (The parenthetical is preserved as the first sentence of
> the section body, which both sections already carry.) This yields the mdBook anchor
> `#arity-specializations`. If the integrator prefers to leave the headings unchanged, re-point
> links to the bare file (`./linear_combination.md`) with no fragment — also valid, since the
> hard requirement is only that no link targets a deleted file.

### (A) Fold the leaves' unique L0 anchors INTO the combinator `## Arity specializations` sections

Both combinator sections already enumerate the four members as a code block of readout-label
identities. ADD, immediately after that code block, a **per-arity L0-anchor table** so no leaf
anchor is orphaned by the deletion. (This is the "fold its concrete arity body + its L0 callsite
anchors into a `## Arity specializations` row" requirement.)

```edit:book/src/L2/linear_combination.md
[In the §"Arity specializations" section, after the readout-label code block (after line 105,
before line 107 "These names remain useful…"), INSERT the per-arity unique-L0-anchor table
folded in from the deleted L2 leaves. The table preserves EVERY anchor from the four deleted
L2 leaf chapters' §Evidence:]

**Per-arity unique L0 surface** (folded in from the eliminated L2 arity-leaf chapters,
cycle-124 RE6 refactor — the bounded-arity L0 call shapes each readout label names; the
combinator's generic free-function-surface anchors `vector.hpp:305-316` do not pinpoint these
at the per-arity resolution):

| Arity | Readout | Unique L0 anchors (paths relative to `reference/palace/`) |
|---|---|---|
| 1 | `scal(α,x)` | `linalg/vector.hpp:98-99` (`ComplexVector::operator*=` decl, "Scale all entries by s."); `linalg/vector.cpp:203-227` (`operator*=` def) incl. `:207-211` (`si==0.0` real fast-path / scalar-promotion site); `linalg/vector.hpp:262-270` (`linalg::Normalize` fused `nrm2+scal` consumer). Receiver-mutating `*=` member idiom — the only family member NOT a free function. |
| 2 (coeff-1) | `axpy(α,x,y)` | `linalg/vector.hpp:115-118` (`ComplexVector::AXPY` + `Add`/`Subtract` aliases decl); `linalg/vector.cpp:276-311` (`ComplexVector::AXPY` def + element-wise kernels); `linalg/vector.cpp:714-718` (real-α-on-complex forwarding overload — scalar-promotion sub-axis); `linalg/vector.cpp:720-724` (complex-α overload → member `ComplexVector::AXPY`). |
| 2 (general) | `axpby(α,x,β,y)` | `linalg/vector.hpp:130-131` (`ComplexVector::AXPBY` member decl, receiver-mutating); `linalg/vector.cpp:732-737` (complex-complex specialisation → member); `linalg/vector.cpp:739-743` (real-scalar-on-complex promotion site). |
| 3 | `axpbypcz(α,x,β,y,γ,z)` | `linalg/vector.hpp:133-136` (`ComplexVector::AXPBYPCZ` member decl); `linalg/vector.cpp:745-758` (real-real, incl. the `γ==0` arity-collapse fast-path `:749-751` → `add(α,x,β,y,z)` — the exact algebraic content of law 5, and the `γ≠0` split `:755-756`); `linalg/vector.cpp:760-765` (complex-complex → member); `linalg/vector.cpp:767-772` (real-scalar-on-complex promotion site). |

(All anchors carried in from the eliminated L2 leaf chapters where they were self-verified
on-disk via `tools/citecheck` at cycle-052; this RE6 pass moves them in-layer into the
combinator, no re-localization claim.)
```

```edit:book/src/L3/linear_combination.md
[In the §"Arity specializations" section, after the readout-label code block (after line 62,
before line 64 "These names remain useful…"), INSERT the per-arity unique-L0-anchor table
folded in from the deleted L3 leaves. The L3 table additionally preserves the L3 leaves'
unique LIVE-CONSUMER call sites (the `scal` chapter carried several the L2 leaf did not):]

**Per-arity unique L0 surface + live consumer sites** (folded in from the eliminated L3
arity-leaf chapters, cycle-124 RE6 refactor):

| Arity | Readout | Unique L0 anchors + live consumer sites (relative to `reference/palace/`) |
|---|---|---|
| 1 | `scal(α,x)` | Surface: `linalg/vector.hpp:98-99` (`operator*=` decl); `linalg/vector.cpp:203-227` (def) incl. `:206-211` (`s.imag()==0.0` shape branch / promotion); `linalg/vector.hpp:262-270` (`linalg::Normalize`). Consumers: `linalg/iterative.cpp:632, 811` (GMRES Arnoldi normalisation); `linalg/operator.cpp:661, 673` (`Normalize` sites); `linalg/nleps.cpp:486-491` (eigenvector normalisation). Receiver-mutating `*=` member — distinct from the free-function family surface. |
| 2 (coeff-1) | `axpy(α,x,y)` | `linalg/vector.cpp:276-311` (`ComplexVector::AXPY`); `linalg/vector.cpp:702-712` (free-function `AXPY` incl. the **load-bearing `α==1.0` fast-path** — the one constant-fold branch distinguishing `axpy`); `linalg/vector.cpp:715-718` (promotion site); `linalg/vector.hpp:115-118`, `:305-307` (decls). |
| 2 (general) | `axpby(α,x,β,y)` | `linalg/vector.cpp:726-730` (real-real MFEM single-aligned `add(α,x,β,y,y)` fused pass); `linalg/vector.cpp:732-737` (complex-complex); `linalg/vector.cpp:739-743` (promotion); `linalg/vector.hpp:130-131`, `:309-311` (decls). No L0 constant-fold branch (distinguishes it from `axpy`). |
| 3 | `axpbypcz(α,x,β,y,γ,z)` | `linalg/vector.cpp:745-758` (real-real incl. `γ==0` arity-collapse `:749-751`); `linalg/vector.cpp:760-765` (complex-complex); `linalg/vector.cpp:767-772` (promotion); `linalg/vector.hpp:133-136`, `:313-316` (decls). |

(Anchors carried in from the eliminated L3 leaf chapters, self-verified on-disk at cycle-052;
this RE6 pass moves them in-layer, no re-localization claim. The `axpby-as-primitive` decision
`scaffolding/decisions/axpby-as-primitive.md` — `axpby`/`axpbypcz` are fused primitives, not
`scal∘axpy` decompositions — is carried by the combinator already and unaffected.)
```

> The combinator chapters' existing §"Dependencies" prose that says the L2/L3 leaf chapters are
> "scheduled to collapse into the §Arity specializations notes" (L2 `:236-244`) / "reduced to
> specialization-stubs cycle-052, files KEPT on disk" (L3 `:29`, `:64`, `:120`) MUST be reworded
> by the integrator from the reduce-to-stub framing to the **eliminated** framing: e.g. L2
> `:241-244` "the separate L2 `scal`/`axpy`/`axpby`/`axpbypcz` chapters are scheduled to
> collapse…" → "the separate L2 arity chapters were **eliminated cycle-124 (RE6)**, their unique
> L0 anchors folded into §Arity specializations above"; L3 `:29`/`:64`/`:120` "reduced to
> specialization-stubs cycle-052 (… files KEPT on disk …)" → "eliminated cycle-124 (RE6), unique
> L0 anchors folded into §Arity specializations above". The L3 frontmatter `reference` /
> dependency narrative that links `[`scal`](./scal.md)` etc. (L3 `:120`) drops those links (the
> members are now in-chapter sections, not separate files).

### (B) Delete the 8 standalone leaf files

```delete
book/src/L2/scal.md
book/src/L2/axpy.md
book/src/L2/axpby.md
book/src/L2/axpbypcz.md
book/src/L3/scal.md
book/src/L3/axpy.md
book/src/L3/axpby.md
book/src/L3/axpbypcz.md
```

### (C) SUMMARY.md de-registration — remove the 8 sub-chapter lines

```edit:book/src/SUMMARY.md
[REMOVE these 8 lines (the dot/inner_product/nrm2/linear_combination lines in both groups STAY —
neither group goes empty: L3 BLAS-1 keeps dot/inner_product/linear_combination/nrm2; L2 stubs
group keeps dot/nrm2):]
- line 106:   "  - [axpby](./L3/axpby.md)"        REMOVE
- line 107:   "  - [axpbypcz](./L3/axpbypcz.md)"  REMOVE
- line 108:   "  - [axpy](./L3/axpy.md)"          REMOVE
- line 113:   "  - [scal](./L3/scal.md)"          REMOVE
- line 154:   "  - [axpby](./L2/axpby.md)"        REMOVE
- line 155:   "  - [axpbypcz](./L2/axpbypcz.md)"  REMOVE
- line 156:   "  - [axpy](./L2/axpy.md)"          REMOVE
- line 159:   "  - [scal](./L2/scal.md)"          REMOVE
```

> The L2 group heading "Fold-family specialization / consumer stubs" (`SUMMARY.md:153`) is now a
> `dot`/`nrm2`-only group (those are `inner_product` specialization/consumer stubs, NOT RE6
> scope). The integrator MAY leave the heading as-is (still accurate for `dot`/`nrm2`) — no
> rename required by RE6.

### (D) Index dep-map row drops + group-intro + narrative edits

**`book/src/L2/index.md`:**
```edit:book/src/L2/index.md
- DROP the 4 dep-map rows in §"Fold-family specialization / consumer stubs": `axpby` (:112),
  `axpbypcz` (:113), `axpy` (:114), `scal` (:117). KEEP `dot` (:115) + `nrm2` (:116) — NOT RE6
  scope. The group section + its `dot`/`nrm2` rows remain.
- The `linear_combination` dep-map row (:106) §Dependencies cell currently lists "L1 fixed-arity
  specializations: `scal`/`axpy`/`axpby`/`axpbypcz`" — those are L1 references (the L1 leaves
  STAY firm), leave unchanged; it does NOT reference the deleted L2 leaves, no edit needed there.
- §"Elementwise & gate floors" inline references that link the DELETED L2 `scal`:
  `normalize` row (:137) "[`scal`](./scal.md) (û = scal(1/β, x); the rescale, arity-1
  *member-of* `linear_combination`)" → re-point to
  "[`scal`](./linear_combination.md#arity-specializations) (the arity-1 *member-of*
  `linear_combination`)". `elementwise_product` row (:135) names `scal` in inline-code only
  (no link) — leave as-is.
- §Working-Notes narrative bullets that name the leaves (e.g. :155 "scal/axpy/axpby/axpbypcz are
  arity-1/2/2/3 specialization-stubs", :164 the "Fold-family leaf cohort — REDUCED to
  combinator-pointer stubs" bullet, :165 cohort narrative): reword "reduced to
  specialization-stubs / files KEPT on disk" → "eliminated cycle-124 (RE6); unique L0 anchors
  folded into the combinator §Arity specializations". These bullets carry inline-code leaf names
  (no live links). The `dot`/`nrm2` mentions in those bullets STAY (still stubs).
- **CORRECTION (critic Issue 1 — `:161` carries THREE LIVE LINKS, was wrongly classified
  "no dangling-link risk").** The cycle-043 leaf-cohort-floor-batch Working-Notes bullet at
  `book/src/L2/index.md:161` contains LIVE markdown links `[`axpy`](./axpy.md)`,
  `[`axpby`](./axpby.md)`, `[`axpbypcz`](./axpbypcz.md)` (in the "(i) the **fold-PARENTED**
  arity-family leaves of `linear_combination` — …" clause). These are NOT inline-code only.
  RE-POINT all three to `[`axpy`](./linear_combination.md#arity-specializations)` /
  `[`axpby`](./linear_combination.md#arity-specializations)` /
  `[`axpbypcz`](./linear_combination.md#arity-specializations)` (preserve the link TEXT as the
  readout label; only retarget) AND reword the bullet's "reduced to specialization-stubs / held
  floors" framing → "eliminated cycle-124 (RE6); unique L0 anchors folded into the combinator
  §Arity specializations". Without this re-point, three links to deleted files survive →
  hard `linkcheck2` exit-101.
```

**`book/src/L3/index.md`:**
```edit:book/src/L3/index.md
- DROP the 4 dep-map rows in §"BLAS-1 vocabulary": `axpby` (:39), `axpbypcz` (:40), `axpy`
  (:41), `scal` (:46). KEEP `dot` (:42), `inner_product` (:43), `linear_combination` (:44),
  `nrm2` (:45) — NOT RE6 scope.
- The `linear_combination` dep-map row (:44) §Dependencies cell links the deleted leaves:
  "Same-layer L3 BLAS-1 leaves [`scal`](./scal.md)/[`axpy`](./axpy.md)/[`axpby`](./axpby.md)/
  [`axpbypcz`](./axpbypcz.md) (the arity-1/2/2/3 specializations … collapsed cycle-051 …
  reduced to specialization-stubs cycle-052)" → reword to
  "the arity-1/2/2/3 specializations (`scal`/`axpy`/`axpby`/`axpbypcz`, inline-code) recovered
  as term-list length — folded into §Arity specializations cycle-124 (RE6)" with the links
  removed (inline-code only).
- The retained-operator dep-map rows that link the deleted L3 leaves in their §Dependencies /
  §"Lowers to" cells MUST re-point (see group E for the full per-link list): `chebyshev` (:67)
  deps cell names `axpy, axpby, axpbypcz, scal` (inline-code, no link — leave); `divfree-projector`
  (:68) §Dependencies links `[`axpy`](./axpy.md)` → re-point; `krylov-step` (:78) deps cell names
  `axpy, axpby, axpbypcz, scal` inline-code (no link — leave); `eigsolve-impl` (:76) +
  `lanczos_step` (:80) deps cells name `axpy`/`scal` inline-code (no link — leave).
- **CORRECTION (critic Issues 2/3/4 — THREE retained-operator dep-map rows carry LIVE LINKS to
  deleted L3 leaves, omitted from the enumeration above).** These MUST re-point to
  `./linear_combination.md#arity-specializations` (preserve the link TEXT as the readout label):
  - `elementwise_product` dep-map row (`:52`) §Dependencies cell — `Sibling-subsumes
    [`scal`](./scal.md) (`scal(α,x)=elementwise_product(broadcast(α,N),x)`)` → re-point the
    `[`scal`](./scal.md)` to `[`scal`](./linear_combination.md#arity-specializations)`.
  - `normalize` dep-map row (`:53`) §Dependencies cell — `[`scal`](./scal.md) (the rescale
    `û = scal(1/β, x)`, result.1 …)` → re-point to
    `[`scal`](./linear_combination.md#arity-specializations)`.
  - `orthogonalize` dep-map row (`:81`) §Dependencies cell — `[`axpy`](./axpy.md) (the residual
    update `w − H_j·V[j]` …)` → re-point to `[`axpy`](./linear_combination.md#arity-specializations)`.
  Without these three re-points, three links to deleted files survive → hard `linkcheck2`
  exit-101. (Verified live on-disk this repair pass at `book/src/L3/index.md:52`, `:53`, `:81`.)
- §"L3 expresses" narrative line :26 "the linear-update family (`axpy`, `axpby`, `axpbypcz`,
  `scal`)" is inline-code (no link) — reword to "the linear-update family
  (`linear_combination`, with `scal`/`axpy`/`axpby`/`axpbypcz` as its arity specializations)"
  for combinator-primary framing; not link-critical.
- §Semantics line :29 obstruction-spectrum narrative links `[`scal`](./scal.md)` → re-point to
  `[`scal`](./linear_combination.md#arity-specializations)`.
```

**Group-intro pages (navigational containers):**
```edit:book/src/L2/fold-family-stubs-intro.md
- Frontmatter `reference:` list (:7-13): REMOVE `L2/axpby`, `L2/axpbypcz`, `L2/axpy`, `L2/scal`.
  KEEP `L2/dot`, `L2/nrm2`.
- Body: REMOVE the four `linear_combination` specialization bullets (:28-31). KEEP the
  `inner_product` `dot`/`nrm2` bullets (:33-39). Reword the intro prose (:18-26) + the
  "All six firm" closing (:41) from six → two stubs; add a one-line note that the four
  `linear_combination` arity members were ELIMINATED cycle-124 (RE6) into
  [`linear_combination` §Arity specializations](./linear_combination.md#arity-specializations).
```

```edit:book/src/L3/blas1-intro.md
- Frontmatter `reference:` list (:7-15): REMOVE `L3/axpby`, `L3/axpbypcz`, `L3/axpy`, `L3/scal`.
  KEEP `L3/dot`, `L3/inner_product`, `L3/linear_combination`, `L3/nrm2`.
- Body (:24): the `linear_combination` bullet lists "[`scal`](./scal.md) (arity-1),
  [`axpy`](./axpy.md) … reduced to combinator-pointer stubs cycle-052" → reword to name the
  arity members inline-code and state they are folded into §Arity specializations cycle-124
  (RE6), links removed. The `inner_product`/`dot`/`nrm2` bullet (:25) STAYS unchanged.
  "All eight carry no sequential obstruction" (:27) → "All carry no sequential obstruction".
```

### (E) Inbound-link re-pointing (every link resolving to a DELETED file)

The hard requirement: no surviving link targets one of the 8 deleted files. The following are
ALL such links (verified by grep this dispatch; links inside `L1/*` and `concepts/*` files that
read `[`scal`](./scal.md)` resolve to `L1/scal.md` / `concepts/scal.md` which are NOT deleted —
those are EXCLUDED and must NOT be touched). Re-point each to the combinator's §Arity
specializations: intra-L2-Part → `./linear_combination.md#arity-specializations`;
intra-L3-Part → `./linear_combination.md#arity-specializations`; cross-Part (the L3-L2 theme)
→ the explicit `../L2/...` / `../L3/...` combinator path.

**L2-Part files (→ `./linear_combination.md#arity-specializations`):**
- `book/src/L2/reciprocal.md` — `[`scal`](./scal.md)` at lines 21, 65, 69, 121, 192, 218, 250,
  388, 409 (line 409 is the bare-code `[`book/src/L2/scal.md`](./scal.md)` cohort-template
  reference — re-point AND change the code-span text to `book/src/L2/linear_combination.md`).
- `book/src/L2/normalize.md` — `[`scal`](./scal.md)` at lines 18, 30, 39, 64, 84, 87, 103, 111,
  127, 141. (Also the frontmatter `lowers_to`/dep note at :11 "book/src/L2/scal.md (û = …)" —
  re-point to `book/src/L2/linear_combination.md`.)
- `book/src/L2/divfree-projector.md` — `[`scal`](./scal.md)` at lines 76, 330.
- `book/src/L2/elementwise_product.md` — `[`scal`](./scal.md)` at line 269; AND line 445 bare
  reference `book/src/L2/scal.md` (floor-cohort-template prose) → re-point/retext to
  `book/src/L2/linear_combination.md`.

**L3-Part files (→ `./linear_combination.md#arity-specializations`):**
- `book/src/L3/normalize.md` — `[`scal`](./scal.md)` at lines 19, 25, 54, 76, 79, 95, 119, 147.
- `book/src/L3/reciprocal.md` — `[`scal`](./scal.md)` at lines 23, 71, 81; `[`axpy`](./axpy.md)`,
  `[`axpby`](./axpby.md)`, `[`axpbypcz`](./axpbypcz.md)` at line 81 (the four-member cohort link
  line — re-point all four to `./linear_combination.md#arity-specializations`).
- `book/src/L3/orthogonalize.md` — `[`axpy`](./axpy.md)` at lines 216, 405; `[`scal`](./scal.md)`
  at line 409.
- `book/src/L3/chebyshev.md` — `[`axpy`](./axpy.md)`+`[`axpby`](./axpby.md)` at line 378;
  `[`scal`](./scal.md)` at line 380; `[`axpbypcz`](./axpbypcz.md)` at line 381.
- `book/src/L3/divfree-projector.md` — `[`axpy`](./axpy.md)` at line 365.
- `book/src/L3/elementwise_product.md` — `[`scal`](./scal.md)` at lines 22, 105.
- `book/src/L3/ksp_solve.md` — `[`axpy`](./axpy.md)`+`[`axpby`](./axpby.md)`+
  `[`axpbypcz`](./axpbypcz.md)`+`[`scal`](./scal.md)` at line 136 (re-point all four).
- `book/src/L3/linear_combination.md` — `[`scal`](./scal.md)`+`[`axpy`](./axpy.md)`+
  `[`axpby`](./axpby.md)`+`[`axpbypcz`](./axpbypcz.md)` at line 120 (this is the §Dependencies
  cell handled in group D — drop links, keep inline-code names). Also the frontmatter `reference`
  block has no leaf-file edges (it references `L4/linear_combination` + the L2-L1 theme) — no
  frontmatter edit beyond group A's reword.

**Cross-Part (L3-L2 theme):**
- `book/src/L3-L2/orthogonalize-variant-split.md` — `[`axpy`](../L3/axpy.md)` at line 134;
  `[`L3/axpy`](../L3/axpy.md)` at line 259; `[`L2/axpy`](../L2/axpy.md)` at line 260. Re-point
  134+259 → `(../L3/linear_combination.md#arity-specializations)`; 260 →
  `(../L2/linear_combination.md#arity-specializations)`. (Preserve the link TEXT `axpy` /
  `L3/axpy` / `L2/axpy` as readout labels; only the targets change.)

> **EXCLUDED — must NOT be touched** (these `[`scal`](./scal.md)` / `[`axpy`](./axpy.md)` links
> resolve to NON-deleted files): every such link inside `book/src/L1/*` (resolves to the firm
> `L1/<leaf>.md`), inside `book/src/concepts/*` (resolves to `concepts/scal.md`/`concepts/axpy.md`
> which exist, or to `concepts/axpby.md`/`concepts/axpbypcz.md` which do not exist — but those
> concept files contain NO such links, verified). Specifically DO NOT touch: `L1/normalize.md`,
> `L1/reciprocal.md`, `L1/orthogonalize.md`, `L1/eliminate_rhs.md`, `L1/divfree-projector.md`,
> `L1/eigsolve.md`, `L1/floquet-correction.md`, `L1/ksp_solve.md`, `L1/elementwise_product.md`,
> `L1/apply_nonlinear_pencil.md`, `L1/nleps_deflated_solve.md`,
> `L1/nleps_eigenvalue_correction.md`, `L1/multigrid-relaxation-smoother.md`, `L1/index.md`,
> `concepts/*`, `concepts/index.md`, `concepts/tensor-field-lift.md`,
> `concepts/build-time-vs-run-time-stratification.md`, `concepts/complex-from-real-lift.md`,
> `concepts/black-box-vs-accelerated-kernels.md`. (These reference the L1 leaves / concept pages,
> which stay firm per RE6: "the L1 leaves remain firm — the L1>L0 one-to-one shape is
> load-bearing there".)

### Post-edit verification (integrator runs)

After applying A–E, the integrator MUST confirm zero remaining links to the deleted files
before `cargo make book`:

```text
grep -rn -E '\((\.\./)?(L2|L3)/(axpy|axpby|axpbypcz|scal)\.md' book/src/   # expect: no hits
grep -rn -E '\]\(\./(axpy|axpby|axpbypcz|scal)\.md' book/src/L2 book/src/L3 # expect: no hits
```

(Any hit is a dangling link to a deleted file = hard linkcheck2 exit-101 — re-point before build.)

## Supporting evidence

- **Combinator firmness + existing arity sections**: `book/src/L2/linear_combination.md`
  (firm c018; §"Arity specializations" `:94-119`; law 2 concatenation-homomorphism `:160-169`;
  §Dependencies collapse-schedule note `:236-244`); `book/src/L3/linear_combination.md`
  (firm c050; §"Arity specializations" `:53-64`; reduce-to-stub provenance `:29`, `:64`, `:120`).
- **The 8 leaf chapters' unique L0 anchors** (the fold-in payload), each self-verified on-disk
  at cycle-052: `book/src/L2/{scal,axpy,axpby,axpbypcz}.md` §Evidence;
  `book/src/L3/{scal,axpy,axpby,axpbypcz}.md` §Evidence. The L0 sites span
  `palace/linalg/vector.{hpp,cpp}` (decls + defs + the `γ==0` arity-collapse `vector.cpp:749-751`,
  the `α==1.0` fast-path `vector.cpp:702-712`, the promotion overloads) + live consumer sites
  `iterative.cpp:632,811`, `operator.cpp:661,673`, `nleps.cpp:486-491`.
- **RE6 disposition**: the scope verbatim ("DISCHARGES RE6 by ELIMINATING the off-spine leaves
  rather than grounding them — the higher-value disposition per RE6's promotion-condition row") +
  memory `project_lift_through_deferred_in_scope` (RE6 = "the axpy-family arity leaves … the
  combinator-arity-notes refactor"). Redirect combinator-miner re-mandate: replace-and-propagate,
  combinator-is-the-entry, leaves-are-specialization-notes (`.claude/agents/combinator-miner.md`
  §VOCABULARY-SHIFT-REDIRECT).
- **Inbound-link census**: grep of `book/src/` this dispatch (full per-link enumeration in
  group E); the EXCLUDED-files list verified by resolving each `./` link against its containing
  Part directory.
- **linkcheck2 config**: `book/book.toml` `[output.linkcheck2]` `warning-policy = "warn"`
  (fragment mismatch = warning; missing-file = hard error).

## Open questions / caveats

- **Heading-anchor normalization is integrator's call.** Group A recommends shortening the two
  `### Arity specializations (…)` headings to `### Arity specializations` so `#arity-specializations`
  resolves cleanly. If the integrator declines, re-point links to the bare
  `./linear_combination.md` (no fragment) — both satisfy the hard no-dangling-file requirement;
  the fragment is a navigability nicety, not a build gate (warning-policy=warn).
- **`dot`/`nrm2` are deliberately OUT of scope** (over-unification guard) — they are
  `inner_product` siblings, a DIFFERENT fold. They stay standalone in the same SUMMARY/index
  groups. A future `inner_product`-family RE-style refactor (the `dot`/`nrm2` analog of RE6)
  could eliminate them the same way, but that is NOT RE6 and is not proposed here.
- **The 4 L1 leaves (`L1/{scal,axpy,axpby,axpbypcz}.md`) STAY firm and untouched** — the
  L1>L0 one-to-one symbol shape is load-bearing for the mutation rotation. RE6 eliminates only
  the L2 + L3 standalone nodes. Many EXCLUDED links point at these L1 leaves; the integrator must
  honor the EXCLUDED list precisely (a `[`scal`](./scal.md)` inside an L1 file is correct and
  must NOT be redirected).
- **Volume / mechanicality.** ~90 inbound links across ~16 files plus 8 deletions + 2 SUMMARY
  groups + 2 index dep-maps + 2 group-intros. The edit is large but mechanical; the per-file
  per-line enumeration in group E is exhaustive against this dispatch's grep. The integrator's
  post-edit grep (above) is the safety net — any residual hit is a hard build error and must be
  cleared before `cargo make book`.
- **No new DAG node, no rank/liveness change to the combinator.** The combinator was already
  firm and root-reachable; eliminating its specialization leaves does not change its rank or
  reachability (the leaves were rank-3 nodes depending UP on the combinator — removing dependents
  never affects a node's own rank/liveness). RE6 strictly shrinks the node count.

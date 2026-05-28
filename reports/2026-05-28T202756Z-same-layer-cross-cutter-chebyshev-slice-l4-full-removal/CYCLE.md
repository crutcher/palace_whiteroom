---
agent: same-layer-cross-cutter
invoked_at: 2026-05-28T20:27:56Z
scope: L-corpus cross-cut — chebyshev-slice-l4-full-removal (Phase-1 slice reduction audit, batch 9/10)
status: integrated
integrated_at: 2026-05-29T0030Z
integration_commit: 1af0c3d
integration_notes: "Applied cycle-015 (per-report position 6, final). book/src/spec/slices/chebyshev.md REMOVED via git rm; 18 inbound citations re-pointed onto firm L1/L4 chebyshev entries; SUMMARY.md + spec/index.md de-registrations applied. Corpus removals 8/10->9/10. OQ chebyshev-slice-l4-full-removal resolved (status flipped by per-report integrator). Build linkcheck (cargo make book exit 0) confirms ZERO stranded markdown links to removed slice — remaining mentions are intentional provenance/historical prose (L3/index.md, frozen meta-reviews). Critique caught 4 non-link prose refs missed by the producer grep; repairer fixed pre-apply."
---

# CYCLE: chebyshev slice §L4 full-removal audit — re-point inbound §L4 citations onto firm `L4/chebyshev.md`, then remove the slice

## Summary

`book/src/spec/slices/chebyshev.md` is the last partially-reduced Phase-1 slice:
cycle-014 absorbed its §L1/§L2/§L3/§Consumers/§Open-questions into the firm
chebyshev cohort and reduced them to pointers, but **retained §L4 verbatim**
(lines 43-196) under a two-part gate: (a) the firm `book/src/L2/krylov-step.md`
cites the slice's §L4 line ranges as canonical pattern-instance evidence, and
(b) `book/src/L4/chebyshev.md` was `rough-in`. **Blocker (b) is resolved** — the
cycle-015 wave-1 lifter
(`reports/2026-05-28T202138Z-lifter-chebyshev-l4-firm-via-iterate-while-reanchor/`)
re-anchored `L4/chebyshev.md` to `iterate_while_pure` and flips it `firm`. I
audited every inbound citation to the slice across the **entire `book/src/` tree**
(not just `krylov-step.md`), verified that every §L4 pattern-instance the
citations rely on is present in the now-firm `L4/chebyshev.md`, and re-pointed
each onto a **stable section-name anchor** in `L4/chebyshev.md` (preferring
section anchors over line numbers, since the wave-1 re-anchor just shifted
`L4/chebyshev.md`'s line numbers). With every inbound §L4 citation cleanly
re-pointed and the two-part gate closed, I propose **FULL REMOVAL** of the slice
+ its three TOC/index entries. **Verdict: FULL-REMOVAL** (corpus removals 8/10 →
9/10). One adjacent finding (three sibling-entry provenance citations to
already-removed §L1/§L2/§L3 ranges, broken by the cycle-014 reduction itself) is
folded into the re-point set so removal strands nothing.

## Observation kind

**Redundancy** — the retained slice §L4 is a verbatim duplicate of the now-firm
`book/src/L4/chebyshev.md` §Semantics/§Signature/§Initial-guess content; the
inbound citations point at the duplicate. Once the citations re-point onto the
authoritative firm entry, the duplicate is removable. (This is a Phase-1
slice-reduction audit per the CLAUDE.md "Phase 1 corpus reduces as material is
lifted" invariant + the `phase-1-slice-reduction-audit` skill, not a new
unification.)

## Specific finding

### Inbound-citation inventory (complete; whole `book/src/` tree)

I grepped the full markdown source tree (excluding the rendered `book/book/html/`
build output and the slice's own self-references). The cycle-014 critic estimated
"7 sites in `L2/krylov-step.md`"; the actual current state across the tree is
**12 inbound references in 9 files**, in three classes:

**Class A — §L4 line-range citations (point at the RETAINED §L4 block; MUST re-point).**
Note: all these ranges (`:354-362`, `:355-362`, `:330-353`, `:308-323`,
`:421-436`, `:287-439`, `:289`, `:325`, `:396-397`) are the **pre-cycle-014
(439-line) line numbers**; the slice is now 196 lines, so they are *already stale*
even before removal. Each re-points to a stable `L4/chebyshev.md` section anchor:

| Citing site | old range | content needed | `L4/chebyshev.md` anchor (verified present) |
|---|---|---|---|
| `L2/krylov-step.md:7` (Context) | `chebyshev.md:354-362` | innerStep / polynomial-recurrence kernel | §Semantics `innerStep` (the `foldM`/inner `iterate_while_pure` body) |
| `L2/krylov-step.md:58` (Semantics, aux stage) | `chebyshev.md:355-362` | `op.scalars (k, st)` closure call | §Signature `scalars` field + §Semantics `op.scalars` |
| `L2/krylov-step.md:77` (Law 1) | `chebyshev.md:421-436` | derived-view treatment of `initial_guess`-as-control | §"Initial-guess shape: branch vs derived view" |
| `L2/krylov-step.md:79` (Law 2) | `chebyshev.md:354-362` | per-step `apply_linop` count = 1 per `k` | §Semantics `innerStep` (`ad <- applyLinop op.A d`) |
| `L2/krylov-step.md:85` (non-law, non-commutativity) | `chebyshev.md:354-362` | scalar-generator depends on `k` + prior apply | §Semantics `innerStep` |
| `L2/krylov-step.md:118` (variant axis 3) | `chebyshev.md:308-323` | `ChebOp<E,S>` type making variant a type-level distinction | §Signature `ChebOp E S` field (distinct closure types `Unit`/`{rho_prev}`) |
| `L2/krylov-step.md:140` (Evidence) | `chebyshev.md:354-362` | innerStep kernel folded by inner loop | §Semantics `innerStep` |
| `L2/krylov-step.md:148` (Evidence, outer driver) | `chebyshev.md:330-353` | `apply` with outer + inner bounded loops | §Semantics `apply` body |
| `L3/apply_linop.md:188` (Evidence) | `chebyshev.md:354-362` | `apply_linop` in the recurrence body | §Semantics `innerStep` (`applyLinop op.A d`) |
| `L3/krylov-step.md:198` (Evidence) | `chebyshev.md:354-362` | innerStep body | §Semantics `innerStep` |
| `L3/krylov-step.md:206` (Evidence, outer driver) | `chebyshev.md:330-353` | `apply`; loops dissolve to tail recursions at L3 | §Semantics `apply` body + §"Lowers to" L4>L3 |
| `L3-L2/krylov-step-body-identity.md:127` (Verified-against) | `chebyshev.md:354-362` | innerStep five-primitive-group body | §Semantics `innerStep` |
| `L2/index.md:35` (pattern-instance list) | `spec/slices/chebyshev.md:354-362` | innerStep pattern instance | §Semantics `innerStep` of `L4/chebyshev.md` |
| `L4/chebyshev.md:412`, `:489` (self §Status/§Evidence) | `chebyshev.md:289,325,396-397` / `:287-439` | the slice §L4 this entry promotes | **Handled by wave-1 lifter** — see ordering note |

The `L4/chebyshev.md:412`/`:489` self-citations are the *provenance* citations
inside the entry that promotes the slice §L4. The wave-1 lifter's Change 11
(rewrites §Status) and Change 15 (rewrites the §Evidence slice bullet `:287-439`)
already touch these; **after** the wave-1 re-anchor lands they should be converted
to git-history provenance (the slice no longer exists on disk). I flag this as an
ordering dependency, not a separate re-point (see Open questions).

**Class B — sibling-entry provenance citations to ALREADY-REMOVED ranges (broken
by the cycle-014 reduction; MUST re-point so removal strands nothing).**
These point at §L1/§L2/§L3 ranges that cycle-014 *already deleted* (the slice is
now pointer-prose for those sections). They are **already dangling** — removal
only makes the dangling target a missing file instead of a missing line range.
Honest fix per the corpus-reduction invariant ("the slice form is not preserved
as historical record once its content lives in the layered surface; the git
history is the historical record"): drop the line range, re-point provenance to
git history / the firm sibling.

| Citing site | dead range | fix |
|---|---|---|
| `L1/chebyshev-smoother.md:341` | `chebyshev.md:34-116` (§L1, removed cycle-014) | drop range; provenance → git history |
| `L2/chebyshev-iteration.md:266` | `chebyshev.md:122-228` (§L2, removed cycle-014) | drop range; provenance → git history |
| `L3/chebyshev.md:520` | `chebyshev.md:229-285` (§L3, removed cycle-014) | drop range; provenance → git history |

(Note `L2/chebyshev-iteration.md:264` ALSO cites `L2/krylov-step.md:7` which
catalogs `chebyshev.md:354-362` — that is a citation to `krylov-step.md`, not to
the slice; once `krylov-step.md:7` re-points (Class A row 1) this transitive
mention reads correctly. No edit needed at `:264` beyond the krylov-step re-point;
I update its prose for consistency below.)

**Class C — prose / structural references (NOT L0-evidence citations; re-point to
firm sibling or drop the link on removal).**

| Citing site | reference | disposition |
|---|---|---|
| `SUMMARY.md:101` | `[Chebyshev smoother](./spec/slices/chebyshev.md)` (mdBook TOC) | **remove the TOC line** |
| `spec/index.md:19` | slice status-table row | **remove the row** |
| `L0/preconditioner-classes-overview.md:102` | `[spec/slices/chebyshev](...)` "structurally similar to" pointer | re-point to firm `L1/chebyshev-smoother.md` |
| `spec/slices/polynomial_recurrence_step.md:30,41` | two slice-to-slice forward-pointers to chebyshev §L2 §"Apply primitives" (a section cycle-014 already removed) | re-point to firm `L2/chebyshev-iteration.md` (§"Apply primitives" is absorbed there) |
| `meta-reviews/2026-05-24-cycles-10-12.md:24` | historical narrative ("`chebyshev.md` does not exist on disk") | **leave as-is** — frozen historical meta-review record, not a live citation |

### Content-presence verification (the gate's hard requirement)

For each Class-A §L4 pattern-instance I confirmed the content is present in the
now-firm `L4/chebyshev.md` (read pre-re-anchor; the wave-1 re-anchor preserves all
this content, only changing `forM_`/`foldM` → `iterate_while_pure` framing):

- **innerStep / polynomial-recurrence kernel** — `L4/chebyshev.md` §Semantics
  lines 152-160 (`innerStep`: `modifyY`, `applyLinop op.A d`, `r' = r .-. ad`,
  `op.scalars k st`, `t = dinv .*. r'`, `d' = sd.*d .+. sr.*t`). PRESENT (and
  post-re-anchor the same body lives inside the inner `iterate_while_pure`).
- **`op.scalars (k, st)` closure** — §Signature `scalars` field (lines 85-89) +
  §Semantics call sites (lines 144, 157). PRESENT.
- **derived-view of `initial_guess`** — §"Initial-guess shape: branch vs derived
  view" (lines 223-239). PRESENT (full degenerate-case-absorption argument).
- **`ChebOp<E,S>` type-level variant distinction** — §Signature `ChebOp E S`
  field (lines 72-89: "distinct closure types `ChebOp E Unit` vs
  `ChebOp E { rho_prev: E }`, not a single union"). PRESENT.
- **`apply` outer + inner bounded loops** — §Semantics `apply` body (lines
  133-161). PRESENT.

**No Class-A citation needs content that is absent from `L4/chebyshev.md`.** The
re-points are clean; nothing is stranded.

## Recommendation

**Dispatch integrator-per-report to apply the proposed-changes below — FULL
REMOVAL of `book/src/spec/slices/chebyshev.md`** + the 13 citation re-points + the
3 TOC/index removals. Corpus-removal delta: **8/10 → 9/10**. Closes OQ
`chebyshev-slice-l4-full-removal`.

**Ordering dependency (load-bearing):** these proposed-changes MUST be applied
**after** the cycle-015 wave-1 lifter re-anchor
(`reports/2026-05-28T202138Z-lifter-chebyshev-l4-firm-via-iterate-while-reanchor/`)
lands, because (a) the Class-A re-points anchor onto `L4/chebyshev.md` section
names that the wave-1 lifter's `firm` entry must already exist for, and (b) the
wave-1 lifter's Change 11/Change 15 already rewrite the `L4/chebyshev.md` §Status /
§Evidence self-citations to the slice §L4 — those rewrites still name the slice
`:287-439`; this dispatch's Change R-14 converts them to git-history provenance
*after* removal. If integrator-finalize sequences this report before the wave-1
lifter report, the Class-A anchors will point at a `rough-in` entry (still
correct content, but the §Status framing differs). Recommend integrator-per-report
order: wave-1 lifter FIRST, then this report.

## Proposed changes

> All `[old]`/`[new]` blocks are exact-string replacements. Section-anchor
> citations use the chapter-relative form `book/src/L4/chebyshev.md` + the section
> name (mdBook renders `## Section` as a stable `#section` fragment); I cite the
> section name in prose rather than a raw line range, per the dispatch instruction
> to prefer stable anchors over the just-shifted line numbers.

### Change R-1 — `L2/krylov-step.md:7` (Context pattern-instance list)

```edit:book/src/L2/krylov-step.md
[old]:
CG (`cg.md:103-115, :172-188, :393-425`), GMRES (`gmres.md:459-471`), Chebyshev (`chebyshev.md:354-362`), Arnoldi (`arnoldi_step.md:99-105, :285-298`), and the three polynomial-recurrence sites cataloged at `polynomial_recurrence_step.md:119-160` all factor into the same kernel-plus-driver shape.
[new]:
CG (`cg.md:103-115, :172-188, :393-425`), GMRES (`gmres.md:459-471`), Chebyshev (`book/src/L4/chebyshev.md` §Semantics `innerStep` — the polynomial-recurrence kernel), Arnoldi (`arnoldi_step.md:99-105, :285-298`), and the three polynomial-recurrence sites cataloged at `polynomial_recurrence_step.md:119-160` all factor into the same kernel-plus-driver shape.
```

### Change R-2 — `L2/krylov-step.md:58` (Semantics, auxiliary stage)

```edit:book/src/L2/krylov-step.md
[old]:
Chebyshev: `op.scalars (k, scalar_state)` per `chebyshev.md:355-362`.
[new]:
Chebyshev: `op.scalars (k, scalar_state)` per `book/src/L4/chebyshev.md` §Signature `scalars` field + §Semantics `op.scalars` calls.
```

### Change R-3 — `L2/krylov-step.md:77` (Law 1, derived-view witness)

```edit:book/src/L2/krylov-step.md
[old]:
Witnessed at cg.md:325-339 (the residual-norm hoisting), chebyshev.md:421-436 (the derived-view treatment of `initial_guess`-as-control), and gmres.md:471-489 (the LS-residual proxy).
[new]:
Witnessed at cg.md:325-339 (the residual-norm hoisting), `book/src/L4/chebyshev.md` §"Initial-guess shape: branch vs derived view" (the derived-view treatment of `initial_guess`-as-control), and gmres.md:471-489 (the LS-residual proxy).
```

### Change R-4 — `L2/krylov-step.md:79` (Law 2, primitive-count)

```edit:book/src/L2/krylov-step.md
[old]:
Witnessed by the per-slice primitive-call enumeration at cg.md:103-115, arnoldi_step.md:99-105, chebyshev.md:354-362.
[new]:
Witnessed by the per-slice primitive-call enumeration at cg.md:103-115, arnoldi_step.md:99-105, `book/src/L4/chebyshev.md` §Semantics `innerStep` (one `applyLinop op.A d` per `k`).
```

### Change R-5 — `L2/krylov-step.md:85` (non-law, non-commutativity)

```edit:book/src/L2/krylov-step.md
[old]:
This is true even for the polynomial-recurrence variants (chebyshev.md:354-362) where the closed-form scalar-generator looks "swappable" with the axpy chain: it depends on `k` and the residual, both of which require the prior apply.
[new]:
This is true even for the polynomial-recurrence variants (`book/src/L4/chebyshev.md` §Semantics `innerStep`) where the closed-form scalar-generator looks "swappable" with the axpy chain: it depends on `k` and the residual, both of which require the prior apply.
```

### Change R-6 — `L2/krylov-step.md:118` (variant axis 3, polynomial-kind)

```edit:book/src/L2/krylov-step.md
[old]:
Witnessed at chebyshev.md:308-323 (the `ChebOp<E, S>` parameter making the variant a type-level distinction).
[new]:
Witnessed at `book/src/L4/chebyshev.md` §Signature `ChebOp E S` field (the `S` scalar-state type parameter — `Unit` for 4th-kind, `{ rho_prev: E }` for 1st-kind — making the variant a type-level distinction via distinct closure types).
```

### Change R-7 — `L2/krylov-step.md:140` (Evidence, innerStep)

```edit:book/src/L2/krylov-step.md
[old]:
- `book/src/spec/slices/chebyshev.md:354-362` (Chebyshev L4 `innerStep` — the polynomial-recurrence kernel folded by `foldM` over `[1..order-1]`).
[new]:
- `book/src/L4/chebyshev.md` §Semantics `innerStep` (the polynomial-recurrence kernel folded by the inner `iterate_while_pure` step-count loop over `[1..order-1]`; firm cycle-015, absorbing the former `chebyshev.md:354-362` slice §L4).
```

### Change R-8 — `L2/krylov-step.md:148` (Evidence, outer driver)

```edit:book/src/L2/krylov-step.md
[old]:
- `book/src/spec/slices/chebyshev.md:330-353` (Chebyshev `apply` with `forM_ [1..pc_it]` outer and `foldM ... [1..order-1]` inner).
[new]:
- `book/src/L4/chebyshev.md` §Semantics `apply` (the outer `pc_it` + inner `k` bounded loops, rendered as nested `iterate_while_pure` step-count folds; firm cycle-015, absorbing the former `chebyshev.md:330-353` slice §L4).
```

### Change R-9 — `L3/apply_linop.md:188` (Evidence, matvec instance)

```edit:book/src/L3/apply_linop.md
[old]:
- `book/src/spec/slices/chebyshev.md:354-362` — Chebyshev L4 `innerStep`; `apply_linop` in the polynomial-recurrence body.
[new]:
- `book/src/L4/chebyshev.md` §Semantics `innerStep` — `apply_linop` (`applyLinop op.A d`) in the polynomial-recurrence body (firm cycle-015, absorbing the former `chebyshev.md:354-362` slice §L4).
```

### Change R-10 — `L3/krylov-step.md:198` (Evidence, innerStep)

```edit:book/src/L3/krylov-step.md
[old]:
- `book/src/spec/slices/chebyshev.md:354-362` (Chebyshev L4 `innerStep`).
[new]:
- `book/src/L4/chebyshev.md` §Semantics `innerStep` (firm cycle-015, absorbing the former `chebyshev.md:354-362` slice §L4).
```

### Change R-11 — `L3/krylov-step.md:206` (Evidence, outer driver)

```edit:book/src/L3/krylov-step.md
[old]:
- `book/src/spec/slices/chebyshev.md:330-353` (Chebyshev `apply`; at L3 the `forM_` and `foldM` dissolve to tail recursions).
[new]:
- `book/src/L4/chebyshev.md` §Semantics `apply` (firm cycle-015, absorbing the former `chebyshev.md:330-353` slice §L4; at L3 the two `iterate_while_pure` folds dissolve to `iterate_while_pure_L3` tail recursions per `L3/chebyshev.md`).
```

### Change R-12 — `L3-L2/krylov-step-body-identity.md:127` (Verified-against)

```edit:book/src/L3-L2/krylov-step-body-identity.md
[old]:
- `book/src/spec/slices/chebyshev.md:354-362` — the Chebyshev `innerStep` body. The five-primitive-group shape is the same as the L2 entry's; no rewrite needed for the L3>L2 rotation.
[new]:
- `book/src/L4/chebyshev.md` §Semantics `innerStep` — the Chebyshev `innerStep` body (firm cycle-015, absorbing the former `chebyshev.md:354-362` slice §L4). The five-primitive-group shape is the same as the L2 entry's; no rewrite needed for the L3>L2 rotation.
```

### Change R-13 — `L2/index.md:35` (pattern-instance list)

```edit:book/src/L2/index.md
[old]:
    - `spec/slices/chebyshev.md:354-362`
[new]:
    - `book/src/L4/chebyshev.md` §Semantics `innerStep` (firm cycle-015; absorbed the former `spec/slices/chebyshev.md:354-362`)
```

### Change R-14 — `L2/chebyshev-iteration.md:264-267` (Evidence — krylov-step catalog mention + removed §L2 provenance)

```edit:book/src/L2/chebyshev-iteration.md
[old]:
- `book/src/L2/krylov-step.md:7` — catalogs `chebyshev.md:354-362` as one of the
  five polynomial-recurrence pattern instances `krylov-step` factors.
- `book/src/spec/slices/chebyshev.md:122-228` — the cycle-001-era L2 slice
  content this entry promotes.
[new]:
- `book/src/L2/krylov-step.md:7` — catalogs `book/src/L4/chebyshev.md`
  §Semantics `innerStep` as one of the five polynomial-recurrence pattern
  instances `krylov-step` factors.
- Provenance: the cycle-001-era §L2 slice content this entry promotes lived at
  the now-removed `book/src/spec/slices/chebyshev.md` §L2 (439-line form,
  `:122-228`); the slice was reduced and removed cycle-015 once its material
  became authoritative here (git history is the record per CLAUDE.md §Methodology
  invariants "Phase 1 corpus reduces as material is lifted").
```

### Change R-15 — `L1/chebyshev-smoother.md:341` (removed §L1 provenance)

```edit:book/src/L1/chebyshev-smoother.md
[old]:
- `book/src/spec/slices/chebyshev.md:34-116` — the cycle-001-era L1 slice
  content this entry promotes (with the `rho_0` correction noted above).
[new]:
- Provenance: the cycle-001-era §L1 slice content this entry promotes lived at
  the now-removed `book/src/spec/slices/chebyshev.md` §L1 (439-line form,
  `:34-116`); the slice was reduced and removed cycle-015 once its material became
  authoritative here, with the `rho_0` correction noted above (git history is the
  record per CLAUDE.md §Methodology invariants "Phase 1 corpus reduces as material
  is lifted").
```

### Change R-16 — `L3/chebyshev.md:520-523` (removed §L3 provenance)

```edit:book/src/L3/chebyshev.md
[old]:
- `book/src/spec/slices/chebyshev.md:229-285` — the cycle-001-era §L3
  "tensor-field form (partial obstruction)" this entry promotes (the tensor-field
  body, the `k` and `pc_it` sequential obstructions, the what-lifts-vs-what-does-not
  table).
[new]:
- Provenance: the cycle-001-era §L3 "tensor-field form (partial obstruction)"
  this entry promotes (the tensor-field body, the `k` and `pc_it` sequential
  obstructions, the what-lifts-vs-what-does-not table) lived at the now-removed
  `book/src/spec/slices/chebyshev.md` §L3 (439-line form, `:229-285`); the slice
  was reduced and removed cycle-015 once its material became authoritative here
  (git history is the record per CLAUDE.md §Methodology invariants "Phase 1
  corpus reduces as material is lifted").
```

### Change R-17 — `L0/preconditioner-classes-overview.md:102` (structural pointer)

```edit:book/src/L0/preconditioner-classes-overview.md
[old]:
polynomial recurrence (`ChebyshevSmoother`, structurally similar to [`spec/slices/chebyshev`](../spec/slices/chebyshev.md)), or composition of others
[new]:
polynomial recurrence (`ChebyshevSmoother`, lifted at [`L1/chebyshev-smoother`](../L1/chebyshev-smoother.md)), or composition of others
```

### Change R-18 — `polynomial_recurrence_step.md:30` (slice-to-slice forward-pointer)

```edit:book/src/spec/slices/polynomial_recurrence_step.md
[old]:
> Forward-pointer: the file-local `ApplyOrder0` / `ApplyOrderK` helpers are also enumerated as the canonical Chebyshev L2 primitive composition at `book/src/spec/slices/chebyshev.md` §L2 §"Apply primitives" (in the per-call apply procedure). The anonymous-namespace / translation-unit-private framing here is unique to this slice (and is load-bearing evidence for the non-promotion to a shared kernel).
[new]:
> Forward-pointer: the file-local `ApplyOrder0` / `ApplyOrderK` helpers are also enumerated as the canonical Chebyshev L2 primitive composition at `book/src/L2/chebyshev-iteration.md` (firm; the per-call apply procedure / `sweep`). The anonymous-namespace / translation-unit-private framing here is unique to this slice (and is load-bearing evidence for the non-promotion to a shared kernel).
```

### Change R-19 — `polynomial_recurrence_step.md:41` (slice-to-slice forward-pointer)

```edit:book/src/spec/slices/polynomial_recurrence_step.md
[old]:
> Forward-pointer: the per-variant scalar-coefficient sequences are also enumerated as the canonical Chebyshev `scalars(op, k)` generator at `book/src/spec/slices/chebyshev.md` §L2 §"Apply primitives" (which factors both the 4th-kind closed-form and the 1st-kind `rho_k` three-term recurrence). The "no shared scalar generator is factored out" framing here is unique to this slice.
[new]:
> Forward-pointer: the per-variant scalar-coefficient sequences are also enumerated as the canonical Chebyshev `scalars(op, k)` generator at `book/src/L2/chebyshev-iteration.md` (firm; which factors both the 4th-kind closed-form and the 1st-kind `rho_k` three-term recurrence). The "no shared scalar generator is factored out" framing here is unique to this slice.
```

### Change R-1b — `L2/krylov-step.md:172` (L0/source-side tests — no-tests coverage-gap fact) [repairer-added cycle-015; critic FAIL miss #1]

This is a **live** "no direct unit tests on Chebyshev step kernels" coverage-gap
claim (not slice-provenance). The same fact carries on the firm
`L1/chebyshev-smoother.md:260` ("there is no dedicated unit test under
`reference/palace/test/unit/` — behaviour is exercised only through multigrid
integration"). The `cg.md`/`gmres.md` siblings still exist on disk, so only the
chebyshev range is stale; re-point that one mention onto the firm L1 status.

```edit:book/src/L2/krylov-step.md
[old]:
- Per cg.md:288, gmres.md:128, chebyshev.md:99-100: no direct unit tests on CG / GMRES / Chebyshev step kernels (integration tests only) — coverage gap inherited from the rough-in; not introduced by this firm-up.
[new]:
- Per cg.md:288, gmres.md:128, and `book/src/L1/chebyshev-smoother.md:260` (no dedicated unit test under `reference/palace/test/unit/`; behaviour exercised only through multigrid integration): no direct unit tests on CG / GMRES / Chebyshev step kernels (integration tests only) — coverage gap inherited from the rough-in; not introduced by this firm-up.
```

### Change R-13b — `L2/index.md:31` (Consumed-by §L4 prose list) [repairer-added cycle-015; critic FAIL miss #2]

The report re-pointed the pattern-instance list at `:35` (R-13) but missed the
sibling "Consumed-by" §L4 prose at `:31`. The `cg.md`/`gmres.md`/`arnoldi_step.md`
slices still exist; only the chebyshev §L4 mention is stale (the slice §L4 is
removed; content now at firm `L4/chebyshev.md`). Re-point that one mention,
matching how R-13 re-points the `:35` sibling.

```edit:book/src/L2/index.md
[old]:
  - **Consumed-by**: L4 `iterate_while` + `solve-monad` outer driver (cg.md §L4, gmres.md §L4, chebyshev.md §L4, arnoldi_step.md §L4).
[new]:
  - **Consumed-by**: L4 `iterate_while` + `solve-monad` outer driver (cg.md §L4, gmres.md §L4, `book/src/L4/chebyshev.md` §Semantics (firm cycle-015; absorbed the former chebyshev §L4), arnoldi_step.md §L4).
```

### Change R-23 — `L3/index.md:29` (chebyshev row, trailing status note — inline-code slice path) [repairer-added cycle-015; critic FAIL miss #3]

NOTE: the markdown LINK `[chebyshev](./chebyshev.md)` earlier in this same row
resolves to the FIRM `L3/chebyshev.md` and is correctly UNTOUCHED. Only the
trailing inline-code-prose slice path `book/src/spec/slices/chebyshev.md` (in the
`partial-obstruction` status parenthetical) is stale after R-22. Re-point the
prose to "now-removed" framing referencing the firm cohort, consistent with the
report's Class-B honest-fix treatment.

```edit:book/src/L3/index.md
[old]: unblocks full reduction of `book/src/spec/slices/chebyshev.md`) |
[new]: unblocked full reduction of the Phase-1 slice (`book/src/spec/slices/chebyshev.md`, removed cycle-015; material now authoritative across the firm `L1`–`L4` chebyshev cohort)) |
```

### Change R-24 — `L3/index.md:41` (Working Notes, first-firm-L3-partial-obstruction bullet — inline-code slice path) [repairer-added cycle-015; critic FAIL miss #4]

Same stale inline-code-prose slice path in the cycle-013 narrative bullet. Re-point
to "removed cycle-015" framing.

```edit:book/src/L3/index.md
[old]: Landing this row + the L4 `chebyshev` row unblocks full reduction of the Phase-1 slice `book/src/spec/slices/chebyshev.md`.
[new]: Landing this row + the L4 `chebyshev` row unblocked full reduction of the Phase-1 slice `book/src/spec/slices/chebyshev.md` (removed cycle-015; material now authoritative across the firm `L1`–`L4` chebyshev cohort).
```

### Change R-20 — `SUMMARY.md:101` (mdBook TOC — REMOVE the slice line)

```edit:book/src/SUMMARY.md
[old]:
  - [Chebyshev smoother](./spec/slices/chebyshev.md)
  - [Arnoldi step](./spec/slices/arnoldi_step.md)
[new]:
  - [Arnoldi step](./spec/slices/arnoldi_step.md)
```

### Change R-21 — `spec/index.md:19` (slice status-table — REMOVE the chebyshev row)

```edit:book/src/spec/index.md
[old]:
| [chebyshev](./slices/chebyshev.md) | L4 | 2026-05-26 | L4 form: ChebOp<E,S> closure with variant-typed scalar state, Solve-monad apply with forM_/foldM sequential obstructions; capability-typed ChebSim, initial_guess as per-call Bool (not a variant axis). |
| [plane rotation stream](./slices/plane_rotation_stream.md) | L3 | 2026-05-26 | L3 negative result: replay-prefix loop is class-(a) sequential obstruction (shared boundary slot read-after-write); per-step extend/apply triple lifts trivially. Canonical small-N obstruction case. |
[new]:
| [plane rotation stream](./slices/plane_rotation_stream.md) | L3 | 2026-05-26 | L3 negative result: replay-prefix loop is class-(a) sequential obstruction (shared boundary slot read-after-write); per-step extend/apply triple lifts trivially. Canonical small-N obstruction case. |
```

### Change R-22 — REMOVE the slice file

```remove:book/src/spec/slices/chebyshev.md
(Full file removal. §L1/§L2/§L3/§Consumers/§Open-questions were reduced to
pointers cycle-014; §L4 (lines 43-196) is verbatim-absorbed by the now-firm
`book/src/L4/chebyshev.md` §Semantics/§Signature/§Initial-guess; all 13 inbound
§L4 + provenance citations re-pointed by Changes R-1..R-19; the 3 TOC/index
entries removed by Changes R-20..R-21. The firm chebyshev cohort —
`L1/chebyshev-smoother.md`, `L2/chebyshev-iteration.md`, `L3/chebyshev.md`,
`L4/chebyshev.md`, `L1-L0/chebyshev-smoother-mutation-rotation.md`,
`L2-L1/chebyshev-iteration-fusion.md` — is the authoritative surface; git history
is the historical record per CLAUDE.md §Methodology invariants "Phase 1 corpus
reduces as material is lifted".)
```

### Note for the L4/chebyshev.md self-citation (ordering, NOT a separate change here)

The wave-1 lifter's Change 11 (§Status) and Change 15 (§Evidence) already rewrite
`L4/chebyshev.md`'s references to the slice §L4. After this report's R-22 removal,
those two self-references (`chebyshev.md:289,325,396-397` in §Status,
`chebyshev.md:287-439` in §Evidence) name a file that no longer exists. **A
follow-up touch is needed** to convert them to git-history provenance (same
treatment as Changes R-14..R-16). I do NOT emit that edit here because (a) it
edits the very lines the wave-1 lifter is rewriting this cycle (write-conflict
risk if both reports' edits target the same span), and (b) the post-re-anchor text
of those §Status/§Evidence lines is not yet on disk for me to write an exact
`[old]` match against. Surfaced as Open Question 1.

## Supporting evidence

- `book/src/spec/slices/chebyshev.md:1-41` — the cycle-014 reduction header
  documenting the two-part removal gate (§L4 retain rationale, the krylov-step
  citation list, OQ `chebyshev-slice-l4-full-removal`); `:43-196` — the retained
  §L4 block being removed.
- `book/src/L4/chebyshev.md` §Signature (lines 54-122), §Semantics (124-173),
  §"Initial-guess shape" (223-239), §Variant axes — the firm content each Class-A
  citation re-points onto (read pre-wave-1-re-anchor; content preserved by the
  re-anchor).
- `reports/2026-05-28T202138Z-lifter-chebyshev-l4-firm-via-iterate-while-reanchor/CYCLE.md`
  — the wave-1 re-anchor flipping `L4/chebyshev.md` `rough-in`→`firm` (blocker (b)
  closure); Changes 11/15 touch the §Status/§Evidence slice self-citations (the
  ordering dependency + OQ 1).
- `book/src/L2/krylov-step.md:7,58,77,79,85,118,140,148` — the eight Class-A
  krylov-step citation sites (the blocker (a) sites).
- `book/src/L1/chebyshev-smoother.md:341`, `L2/chebyshev-iteration.md:266`,
  `L3/chebyshev.md:520` — the three Class-B already-dangling provenance citations
  to removed §L1/§L2/§L3 ranges.
- `book/src/SUMMARY.md:101`, `book/src/spec/index.md:19` — the two TOC/index
  entries removed.
- CLAUDE.md §Methodology invariants "Phase 1 corpus reduces as material is
  lifted"; `skills/phase-1-slice-reduction-audit` (START `## L4 — calculus form`
  + END EOF boundary verified: §L4 is the file's terminal section, line 43 → EOF).

## Open questions / caveats

1. **`L4/chebyshev.md` §Status/§Evidence self-citations to the removed slice
   (ordering follow-up, NOT a blocker on removal).** After R-22, the wave-1
   lifter's post-re-anchor §Status (`chebyshev.md:289,325,396-397`) and §Evidence
   (`chebyshev.md:287-439`) lines name a non-existent file. These need conversion
   to git-history provenance (same as R-14..R-16). I deliberately did NOT emit the
   edit (write-conflict with the wave-1 lifter's same-line rewrites + post-rewrite
   text not yet on disk). **Recommend**: integrator-per-report applies the wave-1
   lifter FIRST, then this report, then a one-line repairer/follow-up touch
   converts the two L4-self-citations to provenance form. If integrator prefers,
   fold it into this report's application as a post-apply fixup. This is the only
   residual citation after R-1..R-21; it does not strand a *reader* (the content
   is in the same file), only a now-dead file-path string.

2. **`meta-reviews/2026-05-24-cycles-10-12.md:24` deliberately left as-is.** It is
   a frozen historical meta-review record narrating a cycle-12-era diff-apply
   failure ("`chebyshev.md` does not exist on disk"); it is not a live citation and
   editing it would falsify the historical record. Flagging that the meta-reviews
   tree will, in general, contain dangling slice-path mentions after corpus
   reduction — these are intentional history, not citation rot. (Same disposition
   the cg.md / other reductions took.)

3. **Build-verification gate.** integrator-finalize's `cargo make book` will catch
   any mdBook broken-link from a missed re-point. I believe the inventory is
   complete (whole-tree grep, both `.md:NNN` line-range and `.md)` markdown-link
   forms), but the build is the backstop. If `mdbook-linkcheck` (or equivalent)
   flags a residual `spec/slices/chebyshev.md` link I missed, that is the signal to
   re-open before commit — do NOT force the commit past a broken-link failure.

4. **`spec/index.md` "Highest layer = L4" provenance.** The removed status-table
   row recorded the slice reached L4. That progress fact is now fully carried by
   the firm `L4/chebyshev.md` entry (in `L4/index.md`'s firm cohort, 3→4 per the
   wave-1 lifter). No information is lost by removing the row. Noting for the
   record in case a roadmap-progress audit wants the cross-check.

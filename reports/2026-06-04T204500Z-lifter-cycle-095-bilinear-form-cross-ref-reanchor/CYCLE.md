---
agent: lifter
invoked_at: 2026-06-04T204500Z
scope: L1 bilinear-form firm-flip — whole-book cross-reference re-anchor of stale rough-in co-mentions
status: integrated
integrated_at: 2026-06-04T231500Z
integration_commit: efe6872
integration_notes: "cycle-095 D2 (staging position 2/7). Whole-book bilinear-form firm-flip cross-ref re-anchor: 14 sites / 11 files, all stale 'bilinear-form rough-in' narration ->firm c095; theme files' OWN ## Status VERDICTs untouched (HARD constraint satisfied, verified on disk). Applied clean, all 13 blocks verbatim; retroactive-budget 0. Promoted 2 OQs (the meta-owned stale-narration + the mwn-mutation-rotation within-theme residue)."
inputs:
  - reports/2026-06-04T204023Z-cycle-planner-cycle-095/CYCLE.md
  - book/src/L1/bilinear-form.md (the operator D1 flips rough-in→firm this cycle)
  - book/src/L2/inner_product.md
  - book/src/L2/index.md
  - book/src/L2-L1/index.md
  - book/src/L2-L1/inner-product-fold-specialization.md
  - book/src/L2-L1/gram-fold-specialization.md
  - book/src/L3/inner_product.md
  - book/src/L3/index.md
  - book/src/L0/linalg-operator-file.md
  - book/src/L1-L0/index.md
  - book/src/L1-L0/dot-mutation-rotation.md
  - book/src/L1-L0/bilinear-form-mutation-rotation.md
  - book/src/L1/blas1-elementwise-intro.md
  - book/src/L1/matrix-weighted-norm.md
---

# CYCLE: Re-anchor — bilinear-form firm-flip whole-book cross-reference sweep

## Summary

Cycle-095 D1 (Wave 1, parallel) flips the L1 `bilinear-form` operator
`rough-in (test-coverage-bounded)` → `firm` (the firm-on-positive-structure escape; DISCHARGE
landed c092). This report is the coupled whole-`book/src/` cross-reference re-anchor
(`firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep` discipline): every
GENUINE consumer co-mention asserting the bilinear-form OPERATOR is `rough-in` is re-anchored to
`firm`, in the SAME pass, so no stale "bilinear-form is rough-in" narration survives the flip.

I enumerated the full `grep -rn 'bilinear-form' book/src | grep -i 'rough-in'` set (47 raw hits
across 41 files), judged each against the genuine-maturity-claim test (a hit is genuinely-stale
**iff** it asserts the bilinear-form OPERATOR's OWN maturity at the `rough-in` token — NOT a
nav-link, a citation-line, an OQ-slug name, a `bilinearform.cpp` FE slug-collision reference, or
an unrelated rough-in mention), and re-anchored the genuine cluster: **14 file-sites across 11
files** (L2 inner_product + L2 index + the two L2-L1 fold-specialization themes + L2-L1 index +
L3 inner_product + L3 index + L0 linalg-operator-file + the L1>L0 dot/bilinear-form themes +
L1>L0 index + blas1 intro + matrix-weighted-norm sibling-OQ note). I left ~12 non-maturity hits
untouched (enumerated below) and flagged 4 out-of-scope stale sites (2 meta-phase-owned
methodology pages, 2 D3/D4-coupled L4 gram_reduce-gate narratives) as coordination/OQ-intake.

No structural rewrites — vocabulary/maturity labels only. The theme files' OWN `## Status` lines
are NOT touched (per HARD constraint); only their references to the bilinear-form operator's
maturity are re-anchored.

## Proposed changes

### 1. L2/inner_product.md — Specializations note (`:178-180`)

```edit:book/src/L2/inner_product.md
[old]: - **`bilinear_form`** — the weight axis at value *general / SPD `M`* (`inner_product_M`),
  realized as the pre-application `inner_product (apply_linop M x) y`. Its L1 leaf is
  [`bilinear-form`](../L1/bilinear-form.md) (rough-in).
[new]: - **`bilinear_form`** — the weight axis at value *general / SPD `M`* (`inner_product_M`),
  realized as the pre-application `inner_product (apply_linop M x) y`. Its L1 leaf is
  [`bilinear-form`](../L1/bilinear-form.md) (firm, promoted cycle-095).
```

### 2. L2/index.md — inner_product dep cell (`:89`)

```edit:book/src/L2/index.md
[old]: L1 leaves it fuses up from: `dot` (Hermitian), `tdot` (unconjugated; firm but type-API-surface only — zero Palace call sites), `bilinear-form` (M-weighted member, rough-in).
[new]: L1 leaves it fuses up from: `dot` (Hermitian), `tdot` (unconjugated; firm but type-API-surface only — zero Palace call sites), `bilinear-form` (M-weighted member, firm — promoted cycle-095).
```

### 3. L2-L1/index.md — gram + inner-product fold-specialization dep cells (`:17`, `:19`)

```edit:book/src/L2-L1/index.md
[old]: | [gram-fold-specialization](./gram-fold-specialization.md) | `L2/gram` (firm, cycle-022) | `L1/dot` (firm; per-cell Hermitian hook) + `L1/bilinear-form` (rough-in, B-weighted hook) | firm
[new]: | [gram-fold-specialization](./gram-fold-specialization.md) | `L2/gram` (firm, cycle-022) | `L1/dot` (firm; per-cell Hermitian hook) + `L1/bilinear-form` (firm cycle-095, B-weighted hook) | firm
```

```edit:book/src/L2-L1/index.md
[old]: | [inner-product-fold-specialization](./inner-product-fold-specialization.md) | `L2/inner_product` (firm) | `L1/dot` (firm; `dot` + `tdot`) + `L1/bilinear-form` (rough-in, M-weighted member) | firm
[new]: | [inner-product-fold-specialization](./inner-product-fold-specialization.md) | `L2/inner_product` (firm) | `L1/dot` (firm; `dot` + `tdot`) + `L1/bilinear-form` (firm cycle-095, M-weighted member) | firm
```

### 4. L2-L1/inner-product-fold-specialization.md — Speculative-L1 + Verified-against + Status (`:366`, `:382-386`, `:451`, `:457`)

Note: the theme's own `## Status` VERDICT (`firm`, `:456`) is NOT changed — only the
operator-maturity reference within the leaf-list is re-anchored.

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[old]: [`dot`](../L1/dot.md) (firm; co-defines `dot` + `tdot`) and
[`bilinear-form`](../L1/bilinear-form.md) (rough-in; the M-weighted member). The LHS
[new]: [`dot`](../L1/dot.md) (firm; co-defines `dot` + `tdot`) and
[`bilinear-form`](../L1/bilinear-form.md) (firm, promoted cycle-095; the M-weighted member). The LHS
```

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[old]: - **`bilinear-form` is rough-in at L1** (narrow variant-axis coverage — its two surfaced
  use sites are both complex-`x`-complex-`y`). The M-weighted dispatch arm does not depend
  on its promotion: the arm's structure is firm (the composition
  `inner_product (apply_linop M x) y` lowering to `Dot(comm, A·x, y)` is clean and
  directly verified). The leaf's rough-in status lives at L1; it does not gate this theme.
[new]: - **`bilinear-form` is firm at L1** (promoted cycle-095 under the firm-on-positive-structure
  escape; its two surfaced use sites are both complex-`x`-complex-`y`). The M-weighted dispatch
  arm was always firm independent of the leaf's promotion: the arm's structure is firm (the
  composition `inner_product (apply_linop M x) y` lowering to `Dot(comm, A·x, y)` is clean and
  directly verified). The leaf is now firm at L1, strengthening — not gating — this theme.
```

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[old]: - `book/src/L1/bilinear-form.md` — the rough-in M-weighted leaf (RHS): `xᴴ M y` (`:63`),
[new]: - `book/src/L1/bilinear-form.md` — the firm M-weighted leaf (RHS): `xᴴ M y` (`:63`),
```

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[old]: existing vocabulary (`dot`/`tdot` firm; `bilinear-form` rough-in but its M-weighted-member
[new]: existing vocabulary (`dot`/`tdot` firm; `bilinear-form` firm (cycle-095) and its M-weighted-member
```

### 5. L2-L1/gram-fold-specialization.md — leaf-list + caveat + Verified-against + Status (`:297`, `:312`, `:382`, `:389`)

Theme's own `## Status` VERDICT (`firm`, `:388`) unchanged; only operator-maturity references
re-anchored.

```edit:book/src/L2-L1/gram-fold-specialization.md
[old]: - RHS leaves are the sibling scalar theme's leaves: [`dot`](../L1/dot.md) (firm; co-defines `dot`
  + `tdot`) and [`bilinear-form`](../L1/bilinear-form.md) (rough-in; the B-weighted hook member).
[new]: - RHS leaves are the sibling scalar theme's leaves: [`dot`](../L1/dot.md) (firm; co-defines `dot`
  + `tdot`) and [`bilinear-form`](../L1/bilinear-form.md) (firm, promoted cycle-095; the B-weighted hook member).
```

```edit:book/src/L2-L1/gram-fold-specialization.md
[old]: - **`bilinear-form` is rough-in at L1** (narrow variant-axis coverage). The B-weighted-hook Gram
  arm (`G = XᴴBX`) does not depend on its promotion: the arm's structure is firm (each cell is the
[new]: - **`bilinear-form` is firm at L1** (promoted cycle-095). The B-weighted-hook Gram
  arm (`G = XᴴBX`) was always firm independent of the leaf's promotion: the arm's structure is firm (each cell is the
```

```edit:book/src/L2-L1/gram-fold-specialization.md
[old]: - `book/src/L1/bilinear-form.md` — the rough-in B-weighted per-cell leaf (RHS): `xᴴ M y` (`:63`).
[new]: - `book/src/L1/bilinear-form.md` — the firm B-weighted per-cell leaf (RHS): `xᴴ M y` (`:63`).
```

```edit:book/src/L2-L1/gram-fold-specialization.md
[old]: vocabulary (`dot`/`tdot` firm; `bilinear-form` rough-in but its B-weighted-hook dispatch arm is
[new]: vocabulary (`dot`/`tdot` firm; `bilinear-form` firm (cycle-095) and its B-weighted-hook dispatch arm is
```

### 6. L3/inner_product.md — bilinear_form member note (`:164-168`)

```edit:book/src/L3/inner_product.md
[old]: - **`bilinear_form`** — the weight axis at value *general / SPD `M`* (`inner_product_M`),
  realized as the pre-application `inner_product (apply_linop M x) y`. It has no standalone
  L3 chapter (its L1 leaf `bilinear-form` is rough-in, L1-promotion-gated at L3 per the
  cycle-036 D2 audit (A) L1-promotion-gated list, `book/src/L3/index.md:48`); at L3 it is
  this weighted-member note.
[new]: - **`bilinear_form`** — the weight axis at value *general / SPD `M`* (`inner_product_M`),
  realized as the pre-application `inner_product (apply_linop M x) y`. It has no standalone
  L3 chapter (its L1 leaf `bilinear-form` is firm, promoted cycle-095 — formerly the cycle-036
  D2 audit (A) L1-promotion-gated member, now an identity-in-form L3 backfill candidate like
  its `matrix-weighted-norm` cohort-sibling; see `book/src/L3/index.md`); at L3 it is
  this weighted-member note.
```

### 7. L3/index.md — cohort-growth audit (A) L1-promotion-gated bullet (`:91`)

The bilinear-form line moves from "(A) L1-promotion-gated" to a discharged-promotion note,
mirroring the exact in-line treatment the same line already gives `matrix-weighted-norm`
(promoted c091, "no longer L1-promotion-gated") without renumbering the `:90` firm-backfill
cohort count — bounded.

```edit:book/src/L3/index.md
[old]:   - **(A) L1-promotion-gated — 1**: `bilinear-form` — `rough-in` at L1; do NOT dispatch L3 work until L1 promotes (ride the same promotion cycle, cycle-009 meta-phase precedent). (`matrix-weighted-norm` was the second member of this cohort; it promoted to `firm` at L1 cycle-091 and is now an identity-in-form L3 backfill candidate alongside the (A) firm cohort above — no longer L1-promotion-gated.)
[new]:   - **(A) L1-promotion-gated — 0** (both members now promoted): `bilinear-form` promoted to `firm` at L1 cycle-095 (the firm-on-positive-structure escape; DISCHARGE c092) and is now an identity-in-form L3 backfill candidate alongside the (A) firm cohort above — no longer L1-promotion-gated. (`matrix-weighted-norm` was the other member of this cohort; it promoted to `firm` at L1 cycle-091 and is likewise an identity-in-form L3 backfill candidate.) This sub-cohort is now empty; both ride the (A) firm-backfill route.
```

### 8. L0/linalg-operator-file.md — natural-L0-anchor bullet (`:73`)

```edit:book/src/L0/linalg-operator-file.md
[old]: Both are harvested at L1 (cycle-008 / cycle-010); `matrix-weighted-norm` is now `firm` (promoted cycle-091), `bilinear-form` remains `rough-in`. The unweighted forms remain the separate
[new]: Both are harvested at L1 (cycle-008 / cycle-010); `matrix-weighted-norm` is now `firm` (promoted cycle-091) and `bilinear-form` is now `firm` (promoted cycle-095). The unweighted forms remain the separate
```

### 9. L1-L0/dot-mutation-rotation.md — boundary-marker reference (`:305`)

```edit:book/src/L1-L0/dot-mutation-rotation.md
[old]: symbol via overloading but is a **different operator** with a different L1 referent
(`bilinear-form`, rough-in) — it requires the operator-application primitive and a workspace
[new]: symbol via overloading but is a **different operator** with a different L1 referent
(`bilinear-form`, firm cycle-095) — it requires the operator-application primitive and a workspace
```

### 10. L1-L0/bilinear-form-mutation-rotation.md — intro + LHS-shape operator references + upstream-L1-gate note

The theme's own `## Status` VERDICT (`firm`, `:550`) is NOT touched. Only references to the
bilinear-form OPERATOR's maturity are re-anchored: the intro (`:4`), the LHS-shape parenthetical
(`:31`), and the "Note on the upstream L1 gate" prose (`:569-579`) which describes the operator's
now-superseded rough-in status.

```edit:book/src/L1-L0/bilinear-form-mutation-rotation.md
[old]: form `bilinear_form(x, M, y) = xᴴ M y` ([`L1/bilinear-form`](../L1/bilinear-form.md), rough-in
test-coverage-bounded) into Palace's L0 `linalg::Dot(comm, x, A, y)` three-step composition
[new]: form `bilinear_form(x, M, y) = xᴴ M y` ([`L1/bilinear-form`](../L1/bilinear-form.md), firm
cycle-095) into Palace's L0 `linalg::Dot(comm, x, A, y)` three-step composition
```

```edit:book/src/L1-L0/bilinear-form-mutation-rotation.md
[old]: LHS shape (rough-in test-coverage-bounded; see [`L1/bilinear-form`](../L1/bilinear-form.md)):
[new]: LHS shape (the firm L1 operator, promoted cycle-095; see [`L1/bilinear-form`](../L1/bilinear-form.md)):
```

```edit:book/src/L1-L0/bilinear-form-mutation-rotation.md
[old]: **Note on the upstream L1 gate.** The L1 operator [`bilinear-form`](../L1/bilinear-form.md) is
`rough-in (test-coverage-bounded)` (its variant-axis coverage and algebraic-law confidence are
narrow). A firm lowering of a rough-in L1 operator is consistent: the lowering's structural
fidelity (does the L1 form expand into this L0 source?) is independent of the L1 entry's
promotion gates (test coverage + the real-`x`/real-`M`/real-`y` variant). Precedent:
[`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md) was firm
over `L1/matrix-weighted-norm` while the latter was rough-in (it has since promoted to firm at
cycle-091, which did not change the theme's firm status — it only strengthened the LHS the theme
lowers); [`eigsolve-mutation-rotation`](./eigsolve-mutation-rotation.md) remains firm over the
still-rough-in `L1/eigsolve`. Promoting an L1 operator to firm (its own gate) does not change a
lowering theme's status; it would only strengthen the LHS the theme already lowers.
[new]: **Note on the upstream L1 leaf.** The L1 operator [`bilinear-form`](../L1/bilinear-form.md) is
now `firm` (promoted cycle-095 under the firm-on-positive-structure escape; DISCHARGE c092). This
theme was already `firm` while the L1 leaf was `rough-in (test-coverage-bounded)`, which is the
consistent case: the lowering's structural fidelity (does the L1 form expand into this L0 source?)
is independent of the L1 entry's own promotion gates. The L1 promotion only **strengthens** the
LHS this theme lowers — it does not change the theme's firm status. Precedent for the firm-theme-
over-then-rough-in-leaf pattern:
[`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md) was firm
over `L1/matrix-weighted-norm` while the latter was rough-in (it promoted to firm at cycle-091,
which did not change the theme's firm status); [`eigsolve-mutation-rotation`](./eigsolve-mutation-rotation.md)
remains firm over the still-rough-in `L1/eigsolve`. Promoting an L1 operator to firm (its own
gate) does not change a lowering theme's status; it only strengthens the LHS the theme already lowers.
```

### 11. L1-L0/index.md — bilinear-form-mutation-rotation row, L_n-form cell (`:28`)

The theme-row's L1-operator cell carries the operator's maturity. The theme's structural-firm
verdict in the rightmost cell is unchanged; only the L1-operator maturity is re-anchored.

```edit:book/src/L1-L0/index.md
[old]: | [bilinear-form-mutation-rotation](./bilinear-form-mutation-rotation.md) | `L1/bilinear-form` (rough-in test-coverage-bounded) | `palace/linalg/operator.{hpp,cpp}`, `palace/models/boundarymodeoperator.cpp` | firm
[new]: | [bilinear-form-mutation-rotation](./bilinear-form-mutation-rotation.md) | `L1/bilinear-form` (firm, cycle-095) | `palace/linalg/operator.{hpp,cpp}`, `palace/models/boundarymodeoperator.cpp` | firm
```

### 12. L1/blas1-elementwise-intro.md — matrix-weighted reductions note (`:7`)

```edit:book/src/L1/blas1-elementwise-intro.md
[old]: `matrix-weighted-norm` is `firm` (promoted cycle-091 under the firm-on-positive-structure escape — both norm-axiom law-sides discharged c088/c089); `bilinear-form` remains `rough-in (test-coverage-bounded)` pending dedicated coverage of its `linalg::` weighted overload.
[new]: `matrix-weighted-norm` is `firm` (promoted cycle-091 under the firm-on-positive-structure escape — both norm-axiom law-sides discharged c088/c089); `bilinear-form` is now `firm` too (promoted cycle-095 under the same firm-on-positive-structure escape; DISCHARGE c092).
```

### 13. L1/matrix-weighted-norm.md — sibling-OQ note (`:124`)

The motivating OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` is now FULLY answered
(both halves promoted: mwn c091, bilinear-form c095). Re-anchor the prose claiming the
bilinear-form half "remains open".

```edit:book/src/L1/matrix-weighted-norm.md
[old]: The cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` is **partially answered** by this entry (the matrix-weighted-norm half); the bilinear-form half is the sibling rough-in queued separately. The OQ should be updated to `partially-answered` status by the integrator, with the bilinear-form half remaining open.
[new]: The cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` is now **fully answered**: the matrix-weighted-norm half by this entry (promoted firm cycle-091) and the bilinear-form half by its sibling [`bilinear-form`](./bilinear-form.md) (promoted firm cycle-095, the firm-on-positive-structure escape). The OQ may be closed by the integrator.
```

## Discipline notes

**What I changed and why.** D1 flips the `bilinear-form` operator to `firm` this cycle; per the
`firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep` discipline, a maturity
promotion stales every chapter/index/theme that mentions the operator's OLD token the moment it
lands, and `linkcheck2` does NOT catch maturity-token prose drift. I ran the whole-`book/src/`
grep, judged each hit by the genuine-maturity test, and re-anchored the 14 genuine consumer
co-mentions in 11 files (this pass), so no stale "bilinear-form is rough-in" narration survives
the flip.

**Re-anchor only, no structural rewrites.** Every edit is a vocabulary/maturity-label change
(`rough-in`→`firm` with a `cycle-095` provenance tag). No LHS/RHS shapes, no decompositions, no
signatures changed. The bilinear-form operator's signature is unchanged by the flip (the flip is a
maturity promotion under the firm-on-positive-structure escape, not a re-architecture), so the
themes' rewrite directions and structures are untouched.

**Theme `## Status` lines preserved (HARD constraint).** For both L1>L0 themes
(`bilinear-form-mutation-rotation.md` `firm`; the two L2-L1 fold-specialization themes `firm`) I
did NOT touch the theme's own `## Status` VERDICT. I re-anchored only the references to the
bilinear-form OPERATOR's maturity that appear WITHIN those files — including the
`bilinear-form-mutation-rotation.md` "Note on the upstream L1 gate" prose (`:569-579`), which
explicitly narrated the operator as `rough-in (test-coverage-bounded)` and is now stale. This is a
reference-to-operator-maturity re-anchor, distinct from the theme's own status, and follows the
exact precedent the note itself cites (the mwn-mutation-rotation note already records "it has since
promoted to firm at cycle-091, which did not change the theme's firm status").

**L3 cohort-count bounded.** At `L3/index.md:91` I moved bilinear-form out of "(A)
L1-promotion-gated" but did NOT renumber the `:90` "(A) firm-backfill — 6" cohort count — I
mirrored the in-line treatment the same line already applies to `matrix-weighted-norm` (promoted
c091, described as a backfill candidate without bumping the `:90` count). I updated the
L1-promotion-gated sub-count `1`→`0` (now empty) since that count is local to the bullet I edited
and is unambiguously stale. No cross-file count surface touched.

**Bounded prose-correction recorded (L1-evidence-driven).** None required beyond the maturity
re-anchors — all edits are maturity-label propagation downstream of the D1 flip, not corrections of
wrong claims against L0. (One adjacent stale claim noticed but OUT OF SCOPE: see Open questions.)

## Supporting evidence

- D1 dispatch (this cycle, Wave 1, parallel): flips `book/src/L1/bilinear-form.md`
  `firmness: rough-in`→`firm` + §Status; the firm-on-positive-structure escape, DISCHARGE landed
  c092 (planner report `:33`, `:86`).
- Planner report `reports/2026-06-04T204023Z-cycle-planner-cycle-095/CYCLE.md` §D2 (`:88`) — this
  dispatch's scope + HARD constraints.
- The firm-on-positive-structure escape precedent chain (CLAUDE.md §"Two rough-in qualifiers"):
  `apply_nonlinear_pencil`, `eigenfreq_qfactor_reduce` c082, `sparameter_reduce` c083,
  `solve_family` c086, `matrix-weighted-norm` c091.
- mwn cascade precedent (the structurally-identical batch-29 LEAD
  `matrix-weighted-norm-firm-flip-and-cascade-wave`, ~30-file cascade): the model this re-anchor
  pass mirrors.

## Open questions / caveats

- **OQ-intake (meta-phase-owned, do NOT edit): `methodology/goal-flow.md:263`** —
  "(`gram_reduce` and `bilinear-form` stay `rough-in`; four columns stay `seed`)" is a c091-batch
  historical narrative that becomes stale on this cycle's bilinear-form flip (and on the coupled
  D3 gram_reduce re-judgment / D4 column re-eval). This is the reader-facing Methodology GOAL+FLOW
  chapter, meta-phase-owned per CLAUDE.md — flagged for the batch-30 meta-phase refresh, NOT edited
  here.
- **OQ-intake (meta-phase-owned, do NOT edit): `methodology/resolution-ladder.md:130-136`** — the
  worked rank-ladder illustration narrates "`gram_reduce` did not promote, because it folds the
  off-diagonal `bilinear-form` primitive, which is still `rough-in` … The next leaf to firm
  (`bilinear-form`, probe discharged cycle-092) is the convergent blocker whose flip will let that
  rank wave continue upward". This forward-looking illustration is realized by THIS cycle's flip
  and becomes stale. `resolution-ladder.md` is the reader-facing graded-stack mirror
  (meta-phase territory) — flagged for the batch-30 meta-phase, NOT edited here. (If the parent
  judges `resolution-ladder.md` is producer-editable, this and the `goal-flow.md` site are clean
  re-anchors to `firm`/"promoted cycle-095" — but I defer to the meta-phase ownership per the HARD
  constraint's spirit.)
- **Coordination (D3/D4-coupled, NOT edited): `L4/index.md:101` + `L4/solve_family.md:154`.** Both
  carry bilinear-form `rough-in` mentions embedded in the `gram_reduce`-gate / column-gate
  narrative whose correctness depends on D3's gram_reduce re-judgment and D4's column re-eval THIS
  cycle. `L4/index.md` is the L4 Part index (a count/dep-cell surface not assigned to D2);
  `solve_family.md:154`'s "Column-gate note" further says gram_reduce is "convergently blocked on
  the matrix-weighted-norm √-cascade NO-GO-HELD (c080)", which is itself stale post-c091. Editing
  these would race D3/D4. **Recommend:** D3 re-anchors the bilinear-form label in `L4/index.md:101`
  (the gram_reduce row) as part of its gram_reduce verdict; the `solve_family.md:154` gate-note
  re-anchor (bilinear-form firm + the stale c080 NO-GO-HELD framing) is best handled by whoever
  re-judges the solve_family/gram_reduce column-gate narrative (D3/D4 coordination or a c096
  follow-up). Flagged so it is not left for a later cycle to discover.
- **Adjacent stale claim OUT OF SCOPE (not bilinear-form):
  `L1-L0/matrix-weighted-norm-mutation-rotation.md:317`** — describes `matrix-weighted-norm` as
  "(rough-in, test-coverage-bounded)", but mwn FIRMED c091. This is a residual from the c091
  cascade that the c091 sweep missed (a `matrix-weighted-norm`-maturity drift, NOT a
  bilinear-form one), so it is outside this dispatch's scope. Flagged as OQ-intake for a
  `matrix-weighted-norm` land-clean follow-up (the mwn cascade's WITHIN-theme residue, the
  `firm-flip-leaves-within-file-stale-narration` class).
- **Non-maturity hits left untouched (verified NOT genuine maturity claims):**
  `L0/linalg-operator-file.md:88` (rough-in refers to L2 product/sum-of-operators, not
  bilinear-form), `L1-L0/index.md:52` (the `bilinearform.cpp` FE slug-collision, a DIFFERENT
  object), `L1-L0/bilinear-form-mutation-rotation.md:215` (overload-naming, no maturity),
  `L2/dot.md:57` / `L2/gram.md:244` / `L2/folds-intro.md:14` /
  `L0/mpi-globalsum-and-collectives.md:119` (nav-links, no maturity), `L1/matrix-weighted-norm.md:147`
  (OQ-slug name), `L1/fe_assemble.md:24/29/33/272` + `L1/eliminate_essential_bc.md:242` +
  `L1/chebyshev-smoother.md:211` (FE slug-disambiguation / OQ-name references).

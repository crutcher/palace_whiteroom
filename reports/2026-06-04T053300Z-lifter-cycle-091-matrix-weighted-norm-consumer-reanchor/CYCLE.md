---
agent: lifter
invoked_at: 2026-06-04T053300Z
scope: L1>L0 + vocabulary-spine consumer maturity re-anchor — matrix-weighted-norm firm-flip cascade (cycle-091 D2)
status: pending
integrated_at: 2026-06-04T080000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-091 D2 (batch-29 LEAD cascade). 12-file / 21-block consumer re-anchor of stale matrix-weighted-norm VERB labels → firm across the vocabulary-spine / L0 / L1-L0 themes; bilinear-form PRESERVED at rough-in everywhere (maturity-preservation invariant held on disk). Promoted OQ goal-flow-mwn-firm-flip-cascade-refresh-stale-rough-in-refs. Applied clean by integrator-per-report; build clean (cargo make book exit 0)."
inputs:
  - reports/2026-06-04T053300Z-cycle-planner-cycle-091/CYCLE.md
  - book/src/L1/matrix-weighted-norm.md (verb own §Status :110 — rough-in on disk; D1 flips to firm)
  - book/src/L1/normalize.md
  - book/src/L2/normalize.md
  - book/src/L3/normalize.md
  - book/src/L3/nrm2.md
  - book/src/L3/index.md
  - book/src/L1/blas1-elementwise-intro.md
  - book/src/L1/chebyshev-smoother.md
  - book/src/L0/linalg-operator-file.md
  - book/src/L0/mpi-globalsum-and-collectives.md
  - book/src/L1-L0/normalize-mutation-rotation.md
  - book/src/L1-L0/bilinear-form-mutation-rotation.md
  - book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md
  - book/src/L1-L0/index.md
  - book/src/L1/bilinear-form.md
---

# CYCLE: Re-anchor matrix-weighted-norm consumer maturity labels (cycle-091 D2)

## Summary

Cycle-091 (the batch-29 LEAD `matrix-weighted-norm-firm-flip-and-cascade-wave`) flips the L1 verb `matrix-weighted-norm`
from `rough-in (test-coverage-bounded)` → `firm` (D1 owns the verb's own §Status `:110` + the L1/L4 index count-owners).
This D2 dispatch re-anchors the **vocabulary-spine + L0 + L1-L0-theme consumer maturity LABELS** that go stale on that
flip — the ~13-file cluster the plan assigned to D2. Each edit below flips ONLY a stale `matrix-weighted-norm` VERB
maturity assertion to `firm`; references to the already-firm L1>L0 THEME `matrix-weighted-norm-mutation-rotation` are
NOT touched, and every `bilinear-form` rough-in label co-mentioned on a shared line is PRESERVED (bilinear-form is the
residual gate keeping `gram_reduce` rough-in — flipping it would be a forcing).

A second-order judgment runs through the `normalize_B` rough-in-note prose (`L1/normalize`, `L2/normalize`,
`L3/normalize`, `L1-L0/normalize-mutation-rotation`): `normalize_B` is held a rough-in note for **two** independent
reasons — (1) the fused B-Normalize is **defined-but-uncalled** (zero 4-arg callsites), and (2) the **inherited
test-coverage bound** from `matrix-weighted-norm`. The cascade LIFTS reason (2) but reason (1) STANDS, so `normalize_B`
STAYS a rough-in note. The re-narration removes the now-discharged inherited-bound clause and leaves the no-live-consumer
reason as the sole basis. `normalize` itself is `firm` throughout and unchanged.

## Reference classification (the three-class triage, applied on disk)

I grepped `matrix-weighted-norm` across the D2 cluster and classified every hit:

- **(FLIP — verb maturity label):** `L3/index.md:91`, `L3/nrm2.md:68`, `L1/blas1-elementwise-intro.md:7`,
  `L0/linalg-operator-file.md:73`, `L1-L0/index.md:39`, `L1-L0/normalize-mutation-rotation.md:305`,
  `L1-L0/bilinear-form-mutation-rotation.md:575`, `L1-L0/matrix-weighted-norm-mutation-rotation.md:26`,`:412`,`:447-453`,
  plus the `normalize_B` inherited-bound prose in `L1/normalize.md:88`,`:95`,`:99`,`:117`, `L2/normalize.md:41`,`:112`,`:139`,
  `L3/normalize.md:98`,`:125`, and `L1/bilinear-form.md:253` (joint-OQ narration — mwn half resolved).
- **(KEEP — already-firm THEME ref `matrix-weighted-norm-mutation-rotation`):** all `*-mutation-rotation.md` LINK targets
  (`normalize-mutation-rotation.md:14`,`:197`,`:300`,`:385`,`:405`; `bilinear-form-mutation-rotation.md:8`,`:91`,`:104`,
  `:258`,`:313`,`:451`,`:493`,`:531`,`:574`-link, etc.) — these point at the THEME (own §Status firm `:432`), NOT touched.
- **(KEEP — bilinear-form rough-in, co-mentioned):** `L1-L0/index.md:28` (bilinear-form-mutation-rotation row, its own
  L1 op rough-in); `L0/linalg-operator-file.md:73` bilinear-form half; `L3/index.md:91` bilinear-form half;
  `L1/bilinear-form.md:4`,`:321` (own status, out of my cluster — bilinear-form own-entry); the `gram_reduce` /
  `bilinear-form` co-mentions — all PRESERVED rough-in.
- **(NO-OP — OQ-slug reference, not a maturity claim):** `L1/chebyshev-smoother.md:211` names the OQ
  `matrix-weighted-norm-and-bilinear-form` as the residual-cohort tracker for a DIFFERENT operator (`spectrum_estimate` /
  `SpectralNorm`). The OQ SLUG name is a navigational identifier, not an assertion that mwn is rough-in. NOT changed
  (see §Discipline notes). `L0/mpi-globalsum-and-collectives.md:119` is a pure forward-target LINK (no maturity token) —
  NOT changed.

## Proposed changes

### 1. `book/src/L3/index.md` — split the L1-promotion-gated cohort line

mwn is no longer L1-promotion-gated (it firmed c091); bilinear-form STAYS gated. Surgical split.

```edit:book/src/L3/index.md
[old]:   - **(A) L1-promotion-gated — 2**: `matrix-weighted-norm` and `bilinear-form` — both `rough-in` at L1; do NOT dispatch L3 work until L1 promotes (ride the same promotion cycle, cycle-009 meta-phase precedent).
[new]:   - **(A) L1-promotion-gated — 1**: `bilinear-form` — `rough-in` at L1; do NOT dispatch L3 work until L1 promotes (ride the same promotion cycle, cycle-009 meta-phase precedent). (`matrix-weighted-norm` was the second member of this cohort; it promoted to `firm` at L1 cycle-091 and is now an identity-in-form L3 backfill candidate alongside the (A) firm cohort above — no longer L1-promotion-gated.)
```

### 2. `book/src/L3/nrm2.md` — re-anchor the rough-in co-mention

```edit:book/src/L3/nrm2.md
[old]:this operator (tracked as rough-in [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1).
[new]:this operator (tracked as firm [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1, promoted cycle-091).
```

### 3. `book/src/L1/blas1-elementwise-intro.md` — split the joint mwn/bilinear-form rough-in claim

mwn firms; bilinear-form STAYS rough-in. The line claims BOTH `rough-in (test-coverage-bounded)` — split it.

```edit:book/src/L1/blas1-elementwise-intro.md
[old]:The two matrix-weighted reductions (`matrix-weighted-norm` `‖x‖_B = √(xᴴBx)`, `bilinear-form` `xᴴMy`) are the `M`-weighted generalisations of `nrm2` / `dot`; both are `rough-in (test-coverage-bounded)` pending dedicated coverage of the `linalg::` weighted overloads.
[new]:The two matrix-weighted reductions (`matrix-weighted-norm` `‖x‖_B = √(xᴴBx)`, `bilinear-form` `xᴴMy`) are the `M`-weighted generalisations of `nrm2` / `dot`. `matrix-weighted-norm` is `firm` (promoted cycle-091 under the firm-on-positive-structure escape — both norm-axiom law-sides discharged c088/c089); `bilinear-form` remains `rough-in (test-coverage-bounded)` pending dedicated coverage of its `linalg::` weighted overload.
```

### 4. `book/src/L0/linalg-operator-file.md` — split the joint harvest-maturity claim

`:73` says "Both are now harvested at L1 (... `rough-in`)" covering mwn AND bilinear-form. Split: mwn firm, bilinear-form rough-in.

```edit:book/src/L0/linalg-operator-file.md
[old]:- **The `linalg::` free functions are the natural L0 anchor for L1's matrix-weighted norm and bilinear-form operators.** `Norml2(comm, x, B, Bx)` lifts to L1's [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md); `Dot(comm, x, A, y)` lifts to L1's [`bilinear-form`](../L1/bilinear-form.md). Both are now harvested at L1 (cycle-008 / cycle-010, `rough-in`); the unweighted forms remain the separate [`nrm2`](../L1/nrm2.md) / [`dot`](../L1/dot.md) operators.
[new]:- **The `linalg::` free functions are the natural L0 anchor for L1's matrix-weighted norm and bilinear-form operators.** `Norml2(comm, x, B, Bx)` lifts to L1's [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md); `Dot(comm, x, A, y)` lifts to L1's [`bilinear-form`](../L1/bilinear-form.md). Both are harvested at L1 (cycle-008 / cycle-010); `matrix-weighted-norm` is now `firm` (promoted cycle-091), `bilinear-form` remains `rough-in`. The unweighted forms remain the separate [`nrm2`](../L1/nrm2.md) / [`dot`](../L1/dot.md) operators.
```

### 5. `book/src/L1-L0/index.md` — re-anchor the theme-row L1-operator maturity cell

Row `:39` annotates the matrix-weighted-norm-mutation-rotation theme's lowered L1 op as `(rough-in)`. The THEME stays
firm (the `firm *(structural; ...)*` cell is untouched); only the lowered-op maturity tag flips. The bilinear-form row
`:28` is PRESERVED.

```edit:book/src/L1-L0/index.md
[old]:| [matrix-weighted-norm-mutation-rotation](./matrix-weighted-norm-mutation-rotation.md) | `L1/matrix-weighted-norm` (rough-in) |
[new]:| [matrix-weighted-norm-mutation-rotation](./matrix-weighted-norm-mutation-rotation.md) | `L1/matrix-weighted-norm` (firm) |
```

### 6. `book/src/L1-L0/normalize-mutation-rotation.md` — lift the inherited-bound clause (`:304-306`) + firm-claim note (`:413-414`)

Reason (2) (inherited test-coverage bound) is now discharged; reason (1) (no live consumer) STANDS → `normalize_B`
STAYS a rough-in note. Re-narrate `:304-306` to drop the discharged clause; update the closing firm-claim note `:412-414`.

```edit:book/src/L1-L0/normalize-mutation-rotation.md
[old]:- **Inherited test-coverage bound.** `normalize_B`'s norm constituent
  [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is `rough-in (test-coverage-bounded)`;
  a fused `normalize_B` cannot be firmer than its constituent.
[new]:- **No remaining constituent-maturity gate.** `normalize_B`'s norm constituent
  [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is now `firm` (promoted cycle-091),
  so the earlier inherited test-coverage bound is discharged. `normalize_B` nonetheless stays a
  rough-in note on the **no-live-consumer** ground above (the fused B-Normalize is defined-but-dead),
  not on any constituent-maturity ground.
```

```edit:book/src/L1-L0/normalize-mutation-rotation.md
[old]:inference, no speculative operator** — so `firm` rather than `partly-constructive`. The B-weighted
sibling `normalize_B` is an in-chapter rough-in note (no fused Palace site + inherited
`matrix-weighted-norm` test-coverage bound), not part of the firm claim.
[new]:inference, no speculative operator** — so `firm` rather than `partly-constructive`. The B-weighted
sibling `normalize_B` is an in-chapter rough-in note (no live consumer of the fused Palace site;
the `matrix-weighted-norm` test-coverage bound it formerly inherited is discharged at cycle-091),
not part of the firm claim.
```

### 7. `book/src/L1-L0/bilinear-form-mutation-rotation.md` — re-anchor the precedent line (`:574-575`)

The "firm theme over a rough-in L1 operator" precedent cites mwn as rough-in. mwn is now firm — the precedent still
holds via `eigsolve` (firm theme over rough-in `L1/eigsolve`); re-anchor the mwn clause to firm so it no longer asserts
mwn rough-in. bilinear-form's OWN rough-in framing (the subject of this line) is PRESERVED.

```edit:book/src/L1-L0/bilinear-form-mutation-rotation.md
[old]:[`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md) is firm
over the rough-in `L1/matrix-weighted-norm`; [`eigsolve-mutation-rotation`](./eigsolve-mutation-rotation.md)
is firm over `L1/eigsolve`. Promoting the L1 operator to firm (its own gate) does not change this
theme's status; it would only strengthen the LHS the theme already lowers.
[new]:[`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md) was firm
over `L1/matrix-weighted-norm` while the latter was rough-in (it has since promoted to firm at
cycle-091, which did not change the theme's firm status — it only strengthened the LHS the theme
lowers); [`eigsolve-mutation-rotation`](./eigsolve-mutation-rotation.md) remains firm over the
still-rough-in `L1/eigsolve`. Promoting an L1 operator to firm (its own gate) does not change a
lowering theme's status; it would only strengthen the LHS the theme already lowers.
```

### 8. `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md` — re-anchor the in-theme verb-maturity prose (`:26`, `:412-414`, `:447-453`)

The theme's own §Status (`:432`, firm) is NOT touched. Three prose references narrate the LHS L1 op as rough-in — flip them.

```edit:book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md
[old]:signature. The LHS shape (rough-in; see [`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md)):
[new]:signature. The LHS shape (firm; see [`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md)):
```

```edit:book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md
[old]:- `book/src/L1/matrix-weighted-norm.md` — the L1 operator this theme lowers (rough-in,
  test-coverage-bounded): closed form `√(xᴴ B x)` (`:18-19`), law 8 self-bilinear identity (`:58`),
[new]:- `book/src/L1/matrix-weighted-norm.md` — the L1 operator this theme lowers (firm, promoted
  cycle-091): closed form `√(xᴴ B x)` (`:18-19`), law 8 self-bilinear identity (`:58`),
```

```edit:book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md
[old]:**Note on the upstream L1 gate.** The L1 operator [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
is `rough-in (test-coverage-bounded)` (its algebraic-law confidence is test-gated). A firm lowering
of a rough-in L1 operator is consistent: the lowering's structural fidelity (does the L1 form
expand into this L0 source?) is independent of the L1 law-confidence gate (are the L1 laws
test-confirmed?). Precedent: [`eigsolve-mutation-rotation`](./eigsolve-mutation-rotation.md) is firm
over the rough-in `L1/eigsolve`. Promoting the L1 operator to firm (its own gate) does not change
this theme's status; it would only strengthen the LHS the theme already lowers.
[new]:**Note on the upstream L1 gate (now discharged).** The L1 operator [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
promoted to `firm` at cycle-091 (both norm-axiom law-sides discharged c088/c089 under the
firm-on-positive-structure escape). This theme was already `firm` while the L1 operator was still
rough-in — a firm lowering of a rough-in L1 operator is consistent, since the lowering's structural
fidelity (does the L1 form expand into this L0 source?) is independent of the L1 law-confidence gate
(are the L1 laws test-confirmed?). The L1 promotion did not change this theme's status; it only
strengthened the LHS the theme already lowers. The standing precedent for the firm-theme-over-
rough-in-L1 pattern is now [`eigsolve-mutation-rotation`](./eigsolve-mutation-rotation.md), firm
over the still-rough-in `L1/eigsolve`.
```

### 9. `book/src/L1/normalize.md` — lift the inherited-bound clause from the `normalize_B` rough-in note (`:88`, `:95`, `:99`, `:117`)

Reason (2) discharged, reason (1) stands → `normalize_B` STAYS a rough-in note (no live consumer). The matrix-weighted-norm
link-target `[matrix-weighted-norm](./matrix-weighted-norm.md) (rough-in)` parentheticals at `:13`,`:87`,`:117` and the
inherited-bound prose at `:88`,`:95`,`:99` flip to firm.

```edit:book/src/L1/normalize.md
[old]:and the underlying reduction [`matrix-weighted-norm`](./matrix-weighted-norm.md) (rough-in), but the fused B-Normalize is **uncalled**
[new]:and the underlying reduction [`matrix-weighted-norm`](./matrix-weighted-norm.md) (firm), but the fused B-Normalize is **uncalled**
```

```edit:book/src/L1/normalize.md
[old]:2. **Inherited test-coverage bound.** `normalize_B`'s norm component is `matrix-weighted-norm`, which is `rough-in (test-coverage-bounded)` (no dedicated test on the SPD-weighted overload — `book/src/L1/matrix-weighted-norm.md:108-110`, `book/src/L1/index.md:80`). A fused `normalize_B` cannot be firmer than its norm constituent.
[new]:2. **No remaining constituent-maturity gate.** `normalize_B`'s norm component `matrix-weighted-norm` promoted to `firm` (cycle-091, firm-on-positive-structure escape — `book/src/L1/matrix-weighted-norm.md` §Status), discharging the inherited test-coverage bound. `normalize_B` nonetheless remains a rough-in note on reason (1) above (no live consumer of the fused operator), not on any constituent-maturity ground.
```

```edit:book/src/L1/normalize.md
[old]:Its laws mirror `normalize`'s with `nrm2` → `matrix_weighted_norm` (unit output is B-unit: `matrix_weighted_norm(û, B) = 1`), conditioned on `B` SPD. Until a callsite surfaces, `normalize_B` is tracked as a queued candidate inheriting the `matrix-weighted-norm` promotion gate, NOT a firm operator.
[new]:Its laws mirror `normalize`'s with `nrm2` → `matrix_weighted_norm` (unit output is B-unit: `matrix_weighted_norm(û, B) = 1`), conditioned on `B` SPD. Until a callsite surfaces, `normalize_B` is tracked as a queued candidate gated SOLELY on the missing live consumer (its `matrix-weighted-norm` norm constituent is now firm), NOT a firm operator.
```

```edit:book/src/L1/normalize.md
[old]:The B-weighted sibling `normalize_B` is an in-chapter **rough-in note** (no fused Palace site + inherited `matrix-weighted-norm` test-coverage bound), not part of the firm claim.
[new]:The B-weighted sibling `normalize_B` is an in-chapter **rough-in note** (no live consumer of the fused Palace site; its `matrix-weighted-norm` test-coverage bound is discharged at cycle-091), not part of the firm claim.
```

```edit:book/src/L1/normalize.md
[old]:`book/src/L1/scal.md` (firm; `û = scal(1/β, x)`, law 8 round-trip), `book/src/L1/matrix-weighted-norm.md` (rough-in; the `normalize_B` norm constituent),
[new]:`book/src/L1/scal.md` (firm; `û = scal(1/β, x)`, law 8 round-trip), `book/src/L1/matrix-weighted-norm.md` (firm, promoted cycle-091; the `normalize_B` norm constituent),
```

### 10. `book/src/L2/normalize.md` — re-anchor the two `normalize_B` inherited-bound references (`:41`, `:112`, `:139`)

```edit:book/src/L2/normalize.md
[old]:its norm constituent [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is `rough-in (test-coverage-bounded)`. Per the L1 entry's boundary documentation (`book/src/L1/normalize.md:83-95`), `normalize_B` is an L1 **rough-in note**, not a firm operator and not an L2 floor candidate.
[new]:its norm constituent [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is now `firm` (promoted cycle-091), so `normalize_B`'s remaining gate is the absent live consumer of the fused B-Normalize, not a constituent-maturity gate. Per the L1 entry's boundary documentation (`book/src/L1/normalize.md:83-95`), `normalize_B` is an L1 **rough-in note** (no-live-consumer ground), not a firm operator and not an L2 floor candidate.
```

```edit:book/src/L2/normalize.md
[old]:the fused B-Normalize (`palace/linalg/operator.hpp:377-384`) is defined-but-uncalled and its norm constituent [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is `rough-in (test-coverage-bounded)`. Tracked as plain text here, not a live link, since no L2 `normalize_B` chapter exists.
[new]:the fused B-Normalize (`palace/linalg/operator.hpp:377-384`) is defined-but-uncalled (the load-bearing gate); its norm constituent [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is now `firm` (promoted cycle-091). Tracked as plain text here, not a live link, since no L2 `normalize_B` chapter exists.
```

```edit:book/src/L2/normalize.md
[old]:The B-weighted sibling `normalize_B` is **not** part of this firm claim (it is an L1-entry rough-in note, L1-promotion-gated via `matrix-weighted-norm`).
[new]:The B-weighted sibling `normalize_B` is **not** part of this firm claim (it is an L1-entry rough-in note, gated on the missing live consumer of the fused B-Normalize; its `matrix-weighted-norm` constituent is firm as of cycle-091).
```

### 11. `book/src/L3/normalize.md` — re-anchor the `normalize_B` inherited-bound + L1-promotion-gated references (`:98`, `:125`)

```edit:book/src/L3/normalize.md
[old]:the fused B-Normalize (`palace/linalg/operator.hpp:377-384`) is defined-but-uncalled and its norm constituent `matrix-weighted-norm` is `rough-in (test-coverage-bounded)`. `matrix-weighted-norm` is one of the two "(A) L1-promotion-gated" operators the c036 D2 audit explicitly held back from L3 dispatch until L1 promotes (`book/src/L3/index.md:47`); `normalize_B` rides the same gate. Tracked as plain text here, not a live link, because no L3 `normalize_B` chapter exists.
[new]:the fused B-Normalize (`palace/linalg/operator.hpp:377-384`) is defined-but-uncalled (the load-bearing gate); its norm constituent `matrix-weighted-norm` is now `firm` (promoted cycle-091). `matrix-weighted-norm` was one of the two "(A) L1-promotion-gated" operators the c036 D2 audit held back from L3 dispatch until L1 promotes (`book/src/L3/index.md`); with its L1 promotion that gate is discharged, and `normalize_B`'s sole remaining gate is the absent live consumer. Tracked as plain text here, not a live link, because no L3 `normalize_B` chapter exists.
```

```edit:book/src/L3/normalize.md
[old]:The B-weighted sibling `normalize_B` is **not** part of this firm claim (it is an L1-entry rough-in note, L1-promotion-gated at L3 via `matrix-weighted-norm`).
[new]:The B-weighted sibling `normalize_B` is **not** part of this firm claim (it is an L1-entry rough-in note, gated on the missing live consumer of the fused B-Normalize; its `matrix-weighted-norm` constituent is firm as of cycle-091).
```

### 12. `book/src/L1/bilinear-form.md` — re-anchor the joint-OQ narration (`:253`), preserving the bilinear-form half

This line co-narrates the OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins`. The mwn half is now resolved; the
bilinear-form half stays open. The OQ slug name itself is unchanged (it is the OQ identifier). bilinear-form's own status
(`:4`,`:321`) is NOT in my cluster and is PRESERVED.

```edit:book/src/L1/bilinear-form.md
[old]:Future `nrm2_B`-weighted operator (cycle-010 wave-1 sibling dispatch #5,
addressing cycle-008 OQ `nrm2-B-weighted-energy-norm-harvest` and the
sibling OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins`) will likely
depend on `bilinear-form` via `nrm2_B(x, B) = √bilinear_form(x, B, x)` when
`B` is SPD (law 8). That is the L1 statement of the energy norm.
[new]:Future `nrm2_B`-weighted operator (cycle-010 wave-1 sibling dispatch #5,
addressing cycle-008 OQ `nrm2-B-weighted-energy-norm-harvest` and the
sibling OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` — whose
`matrix-weighted-norm` half is now resolved (the verb promoted to `firm` at
cycle-091); the `bilinear-form` half remains open) will likely
depend on `bilinear-form` via `nrm2_B(x, B) = √bilinear_form(x, B, x)` when
`B` is SPD (law 8). That is the L1 statement of the energy norm.
```

## Discipline notes

- **Structural rewrite, not authorship.** Every edit flips a stale `matrix-weighted-norm` VERB maturity assertion
  (`rough-in (test-coverage-bounded)` / `rough-in`) to `firm`, on the basis of the D1 verb flip (verb own §Status
  `book/src/L1/matrix-weighted-norm.md:110`, currently `rough-in (test-coverage-bounded)` on disk, flips to `firm` this
  cycle). No content decisions beyond the maturity re-anchor and the bounded `normalize_B` reason-set re-narration
  (below, which is directly supported by the on-disk prose).

- **`bilinear-form` PRESERVED at rough-in everywhere it co-occurs.** Three joint-claim lines (`L3/index.md:91`,
  `L1/blas1-elementwise-intro.md:7`, `L0/linalg-operator-file.md:73`) asserted BOTH verbs rough-in; each edit SPLITS the
  claim, flipping only the mwn half and leaving bilinear-form `rough-in`. The bilinear-form-mutation-rotation theme
  (`:574-575`) keeps its bilinear-form rough-in framing; `L1-L0/index.md:28` (bilinear-form row) is untouched;
  `L1/bilinear-form.md:4`/`:321` (own status — outside my cluster) untouched. `bilinear-form` stays the residual gate
  keeping `gram_reduce` rough-in (D3's call).

- **`normalize_B` reason-set re-narration (bounded prose correction, evidenced).** The `normalize_B` rough-in note
  (`L1/normalize.md:83-95`, `L2/normalize.md:41`/`:112`/`:139`, `L3/normalize.md:98`/`:125`,
  `L1-L0/normalize-mutation-rotation.md:286-306`/`:412-414`) is held by TWO independent reasons: (1) the fused
  B-Normalize is **defined-but-uncalled** (zero 4-arg callsites — `L1/normalize.md:87`,
  `L1-L0/normalize-mutation-rotation.md:293-303`), and (2) the **inherited test-coverage bound** from
  `matrix-weighted-norm`. The cascade discharges reason (2) but reason (1) STANDS, so `normalize_B` correctly STAYS a
  rough-in note. I removed the discharged inherited-bound clause and left the no-live-consumer reason as the sole basis.
  This is a bounded re-narration (not a status change — `normalize_B` stays a rough-in note; `normalize` itself stays
  firm), directly supported by the on-disk two-reason structure I read. NO re-architecting, NO signature change.

- **OQ-slug NO-OP — `L1/chebyshev-smoother.md:211`.** This line names the OQ `matrix-weighted-norm-and-bilinear-form`
  as the residual-cohort tracker for a DIFFERENT, still-speculative operator (`spectrum_estimate` / `SpectralNorm`
  power-iteration sibling). The OQ slug is a navigational identifier, not an assertion that mwn is rough-in. The OQ
  itself (`matrix-weighted-norm-and-bilinear-form-l1-rough-ins`) is now only PARTIALLY resolved (mwn half closed,
  bilinear-form half open), so the slug reference remains valid. Left unchanged.

- **Theme `## Status` lines NOT touched.** `matrix-weighted-norm-mutation-rotation.md` §Status (`:432`, firm),
  `normalize-mutation-rotation.md` §Status, `bilinear-form-mutation-rotation.md` §Status — all already firm, all
  untouched. I edited only the PROSE references to the verb's maturity within those theme bodies (`:26`/`:412`/`:447-453`,
  `:305`/`:413-414`, `:575`), per the D2 scope.

- **Layer-definition discipline (high→low).** All edits are maturity-label re-anchors; no rewrite direction was inverted.
  The L1>L0 themes continue to narrate L1→L0 (LHS L1, RHS L0); the verb-maturity prose is metadata about the LHS, not a
  reversed lowering narration.

- **firm-promotion-coupled whole-book grep (the batch-29 ~30-file-scale exercise).** I ran
  `grep -rn 'matrix-weighted-norm' book/src` and triaged all 56 hits into the three classes (§Reference classification
  above). My D2 cluster's genuine-maturity-label subset is the 13 files edited here. Hits NOT in my edit set are either
  (KEEP) theme-link targets / bilinear-form co-mentions, (NO-OP) OQ-slug or pure-link references, or owned by D1
  (`L1/index.md`, `L4/index.md`) / D3 (reduce-verbs) / D4 (feature columns). See §Open questions for the goal-flow flag.

## Supporting evidence

- D1 verb-flip basis: `book/src/L1/matrix-weighted-norm.md:108-115` — §Status `rough-in (test-coverage-bounded)` with
  norm-axiom law-sides (4/6/7) structure-side discharged c088 (`:115`) and FP-side discharged c089 (`:115`); the
  firm-on-positive-structure escape (the `apply_linop`/`eigenfreq_qfactor_reduce`/`sparameter_reduce`/`solve_family`
  precedent) licenses the firm flip D1 enacts this cycle.
- Plan: `reports/2026-06-04T053300Z-cycle-planner-cycle-091/CYCLE.md` — D2 scope + per-file checklist (lines 85-94),
  three-reference-class triage (lines 18-21), hard constraints (bilinear-form preserved; no index/feature/reduce-verb
  writes; goal-flow OQ-flag-only).
- `normalize_B` two-reason structure: `book/src/L1/normalize.md:85-95` (reasons 1+2 enumerated),
  `book/src/L1-L0/normalize-mutation-rotation.md:286-306` (same two reasons; the uncalled-fused-operator reason at
  `:293-303`).
- bilinear-form preserved-at-rough-in evidence: `book/src/L1/bilinear-form.md:4` (`firmness: rough-in`), `:321`
  (`rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)`) — outside my cluster, confirms the gate stands.

## Open questions / caveats

- **`book/src/methodology/goal-flow.md` — OQ-intake flag (meta-phase-owned, NOT edited by D2).** Per the plan
  (lines 94, 150, 173), goal-flow is meta-phase-owned and D2 must NOT edit it. I greped it for stale
  `matrix-weighted-norm` rough-in references:

  ```
  $ grep -n 'matrix-weighted-norm' book/src/methodology/goal-flow.md
  175:> NOT yet apply to `gram_reduce` / `domain_energy_reduce` — their folded `matrix-weighted-norm`
  177:> gated behind the `matrix-weighted-norm` √-entry-point cascade whose norm-axiom laws genuinely
  218:> `domain_energy_reduce` + `matrix-weighted-norm` rough-in), `boundary-mode` (own waveguide-mode
  223:> single convergent foundation-blocker: the `matrix-weighted-norm` √-entry-point cascade**, which
  232:> scoped dischargeability probes the prior batch queued BOTH discharged the `matrix-weighted-norm`
  249:> LEAD; firming `matrix-weighted-norm` is the convergent foundation-unblock for the downstream
  ```

  **OQ-intake note for the batch-29 meta-phase (goal-flow is meta-phase-owned — D2 did NOT edit it).** `goal-flow.md`
  carries stale `matrix-weighted-norm` rough-in references that go stale on the c091 firm flip — notably `:175-177` (the
  cascade-not-yet-discharged framing for `gram_reduce`/`domain_energy_reduce`), `:218` ("`domain_energy_reduce` +
  `matrix-weighted-norm` rough-in"), `:223`/`:232`/`:249` (the "single convergent foundation-blocker" / "firming
  `matrix-weighted-norm` is the convergent foundation-unblock" framing, now ENACTED this cycle rather than queued).
  These should be refreshed at batch close when the meta-phase regenerates goal-flow (the chapter is a synthesized,
  non-authoritative mirror — the c091 firm flip + cascade outcome IS the refresh trigger). I did NOT edit it (write-
  authority partition: goal-flow is meta-phase-owned). Note: `:175-177`/`:218` co-mention `gram_reduce` /
  `domain_energy_reduce` whose own status is D3's call this cycle, so the goal-flow refresh should read D3's verdict
  (gram_reduce predicted STAYS rough-in on the bilinear-form residual gate; domain_energy_reduce a JUDGE) — another
  reason to leave it to the meta-phase batch-refresh rather than re-anchor it piecewise now.

- **`normalize_B` stays a rough-in note (NOT promoted).** This dispatch does NOT promote `normalize_B`; it only removes
  the now-discharged inherited-bound reason. `normalize_B`'s promotion remains gated on a live consumer of the fused
  B-Normalize surfacing (`palace/linalg/operator.hpp:377-384`, currently zero 4-arg callsites). If a future cycle wants
  to revisit `normalize_B`, the gate is now SINGLE (no-live-consumer), no longer joint.

- **No abstractor reread needed.** Every edit is a pure maturity-label re-anchor or a bounded reason-set re-narration
  directly supported by on-disk prose. No firmed-up signature contradicts what any theme assumed (the verb's signature
  is unchanged by the firm flip; only its maturity tier changes).

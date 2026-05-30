---
agent: abstractor
invoked_at: 2026-05-29T20:59:45Z
scope: L1>L0 + L1 prose correction — normalize_B "no fused B-Normalize" defect (F1 from cycle-028 audit)
status: pending
integrated_at: 2026-05-30T004013Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-029 (staging row 5). PROSE-ONLY correction (no Status changes, no new files, no SUMMARY edits, no dep-map edits). 3 edits to L1-L0/normalize-mutation-rotation.md + 4 paired edits to L1/normalize.md: §Speculative-L1-operators rough-in note no fused → exists but uncalled (both files); §promotion-gate find that the function exists → find a positive callsite (both files; gate STAYS open but bar tightens — mere existence now explicitly insufficient). Both files Status verified unchanged at firm. 1 path-hygiene repair at land-time: 3 bare-basename operator.hpp references → palace/linalg/operator.hpp full path against sibling palace/fem/libceed/operator.hpp ambiguity (mechanical-token substitution). 2 OQs promoted (closure-record for c028 OQ + follow-up F1-row staleness at :466-469). RESOLVES the c028-opened OQ normalize_B-note-says-no-fused-B-Normalize-but-uncalled-fused-operator-exists. NO repair needed (overall_status: ready)."
inputs:
  - book/src/L1-L0/normalize-mutation-rotation.md (firm theme; lines 283-293 + 51 prose claim + `verified_against:` F1 row at :466-469)
  - book/src/L1/normalize.md (firm L1 op; lines 13 + 83-95 rough-in note)
  - reports/2026-05-29T194558Z-lowering-verifier-normalize-mutation-rotation-audit/CYCLE.md (F1 finding, Edit 3 routing)
  - reference/palace/palace/linalg/operator.hpp:377-384 (the fused B-weighted Normalize free function; on-disk verified)
  - grep survey: zero 4-arg Normalize(comm, x, B, Bx) callsites in palace/ (only 2-arg unweighted)
---

# CYCLE: L1>L0 + L1 prose correction — normalize_B "no fused B-Normalize" defect

## Summary

Cycle-028's lowering-verifier audit of `normalize-mutation-rotation` (Edit 3 routing,
F1 finding, `verified_against:` row `palace/linalg/operator.hpp:377-384` verdict
`does-not-support`) flagged a content defect in the `normalize_B` rough-in note that
spans two firm files. The defect: both files claim **"Palace has NO fused
`linalg::Normalize`-with-`B` free function"** — but `palace/linalg/operator.hpp:377-384`
IS exactly that: a fused B-weighted `Normalize(comm, x, B, Bx)` free function,
structurally identical to the unweighted `vector.hpp:264` (reduction → guard → rescale
→ return). The theme is internally inconsistent (line 290-293 cites that very range as
the weighted-`Normalize` consumer while line 285-287 + line 51 deny the function
exists). The defensible fact is the function is **defined-but-uncalled** — zero 4-arg
`Normalize(comm, x, B, Bx)` callsites in the tree (grep-verified across `palace/`).

This dispatch is a **prose-only correction** (NO `## Status` changes; firm cores of
both files unaffected). The two edits: (a) rewrite the "does not exist" framing to
"exists but uncalled" in both files; (b) tighten the `normalize_B` promotion-gate
wording — the gate STAYS OPEN (rough-in → firm still needs a positive *call site*; the
definition alone does not promote it), but the gate's stated condition shifts from
"find that the function exists" to "find a positive *call* site of the fused B-Normalize
(or an inline B-weighted rescale)". The verifier explicitly noted (Open questions /
"F1 promotion-side note") that "the gate is really 'a *callsite* of the fused
B-`Normalize` (or an inline B-rescale) plus the `matrix-weighted-norm` test-coverage
promotion' — a slightly different gate than written." This dispatch realises that
tightening.

The transport convention used in the proposed-changes blocks below: outer fence is
`` ``` ``; nested yaml/code samples use 4-space-indented blocks (NOT nested ` ``` `
fences) to avoid the firm-body-outside-fence truncation defect (friction-ledger
`firm-chapter-body-authored-outside-proposed-changes-fence`).

## On-disk verification (this invocation)

Confirmed before emitting:

- `palace/linalg/operator.hpp:377-384` IS the fused B-weighted `Normalize`:
  - `:373-374` forward-declares `Norml2(MPI_Comm comm, const VecType &x, const Operator &B, VecType &Bx)`.
  - `:376` comment "Normalize the vector with respect to an SPD matrix B."
  - `:378` `inline double Normalize(MPI_Comm comm, VecType &x, const Operator &B, VecType &Bx)`.
  - `:380` `double norm = Norml2(comm, x, B, Bx);` (B-weighted reduction binding).
  - `:381` `MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!");` (partiality guard).
  - `:382` `x *= 1.0 / norm;` (in-place rescale).
  - `:383` `return norm;` (returned norm).
  - Four-step composition identical to `vector.hpp:264` modulo the extra `(B, Bx)` reduction args.
- `citecheck --anchor` (this invocation):
  - `operator.hpp:377-384 --anchor 'Normalize(MPI_Comm comm, VecType &x, const Operator &B'` → 378 ok
  - `operator.hpp:377-384 --anchor 'Norml2(comm, x, B, Bx)'` → 380 ok
  - `operator.hpp:377-384 --anchor 'x *= 1.0 / norm'` → 382 ok
- 4-arg callsite grep across `reference/palace/palace/` (`*.cpp`/`*.hpp`/`*.h`):
  zero 4-arg `Normalize(comm, x, B, Bx)` invocations. The only `Normalize` calls
  with non-2-arg signatures are `waveportoperator.cpp:120,693` — an unrelated
  `GridFunction`-tuple `Normalize` with a different signature (not the linalg one).
  The fused B-Normalize at `operator.hpp:378` has zero call sites.

These two facts pin the correction: the function EXISTS (positively anchored) and is
UNCALLED (negatively anchored via exhaustive grep).

## Proposed changes

### Edit 1 — `book/src/L1-L0/normalize-mutation-rotation.md`: rewrite the "does not exist" prose

Two passes: (1.A) the `## Speculative L1 operators` rough-in note at lines 283-293
(the principal "no fused" claim + the internally-inconsistent `operator.hpp:377-384`
reference); (1.B) the chapter-intro line 51 (the parallel claim in the L0 form §RHS
discussion); (1.C) the promotion-gate tightening (lines 298-301).

```edit:book/src/L1-L0/normalize-mutation-rotation.md
[at lines 283-293, replace the bulleted item "No fused Palace site."]
old:
- **No fused Palace site.** Palace has **no** `linalg::Normalize`-with-`B` free function;
  the sole `Normalize` overload (`vector.hpp:264`) takes no `B`. The header comment
  ("...possibly with respect to an SPD matrix B", `vector.hpp:262`) is aspirational. The
  B-weighted reduction exists ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md), via
  `linalg::Norml2(comm, x, B, Bx)`, `palace/linalg/operator.cpp:599-619`) but its callsites are
  error-norm / eigenvector-norm computations that **do not rescale** — they feed residual
  ratios, not an in-place normalise. (Contrast: the `Normalize`-with-`B` *inline* form
  `x *= 1.0/norm` after a weighted `Norml2` IS the consumer Sub-pattern C of
  [`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md)
  at `palace/linalg/operator.hpp:377-384` — but that is the weighted-norm theme's consumer, not a fused
  `normalize_B` operator.)
new:
- **Fused B-Normalize exists but has no callsite.** Palace ships a fused B-weighted
  free function `Normalize(comm, x, B, Bx)` at `palace/linalg/operator.hpp:377-384`
  (def `:378`, B-weighted reduction `:380`, partiality guard `:381`, rescale `:382`,
  return `:383`) — structurally identical to the unweighted `linalg::Normalize` at
  `palace/linalg/vector.hpp:262-270` (the four-step composition reduction → guard →
  rescale → return), differing only by threading `(B, Bx)` into the inner `Norml2`.
  The header comment at `vector.hpp:262` ("...possibly with respect to an SPD
  matrix B") is realised by this `operator.hpp:378` overload, not by the unweighted
  `vector.hpp:264`. **However, the fused B-Normalize is uncalled**: a grep across
  `palace/` for 4-arg `Normalize(comm, x, B, Bx)` invocations finds **zero**
  callsites. So the fused operator is defined-but-dead. The B-weighted *reduction*
  `linalg::Norml2(comm, x, B, Bx)` ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md),
  `palace/linalg/operator.cpp:599-619`) IS used at error-norm / eigenvector-norm
  callsites (`arpack.cpp:438`, `slepc.cpp:475`, `nleps.cpp:114`) but they feed
  residual ratios and do **not** rescale. The `Normalize`-with-`B` consumer site of
  [`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md)
  *is* this very `operator.hpp:377-384` fused overload — but it is recorded there as
  the *definition* of the B-weighted fused shape, not a callsite. So `normalize_B`
  has **no live consumer in the tree**: definition exists, callsite does not.
```

```edit:book/src/L1-L0/normalize-mutation-rotation.md
[at line 51, replace within the L0 form (RHS) §intro the parenthetical clause about the weighted Normalize site]
old:
The L1 pair lowers into the free-function template `linalg::Normalize(comm, x)`
new:
The L1 pair lowers into the unweighted free-function template `linalg::Normalize(comm, x)`
(the fused B-weighted overload `Normalize(comm, x, B, Bx)` at `palace/linalg/operator.hpp:377-384`
exists but is uncalled — see the `normalize_B` rough-in note below)
```

```edit:book/src/L1-L0/normalize-mutation-rotation.md
[at lines 298-301, replace the promotion-gate sentence]
old:
If/when an inline B-weighted-normalise site surfaces (a `scale = Norml2(comm, v, B, Bv);
v *= 1.0/scale` pattern distinct from the unweighted `nleps.cpp:610-611`), `normalize_B`
would promote to a firm sibling inheriting the `matrix-weighted-norm` promotion gate.
Until then it is tracked as a queued candidate, not part of this theme's firm claim.
new:
If/when a positive *callsite* of the fused B-Normalize surfaces — either a direct
4-arg `Normalize(comm, v, B, Bv)` invocation OR an inline B-weighted-rescale shape
(`scale = Norml2(comm, v, B, Bv); v *= 1.0/scale`, distinct from the unweighted
`nleps.cpp:610-611`) — `normalize_B` would promote to a firm sibling inheriting the
`matrix-weighted-norm` promotion gate. The mere *existence* of the fused free function
at `palace/linalg/operator.hpp:378` does NOT promote it: a defined-but-dead operator
has no live algebraic-law evidence beyond the syntactic identity to the unweighted core.
Until a callsite surfaces, `normalize_B` is tracked as a queued candidate, not part of
this theme's firm claim.
```

### Edit 2 — `book/src/L1/normalize.md`: parallel correction to the rough-in note

The firm L1 operator entry carries the same defect at line 13 (the chapter-intro one-
liner) and lines 87-88 (the rough-in note item 1). Same direction of fix.

```edit:book/src/L1/normalize.md
[at line 13, replace the chapter-intro paragraph about the B-weighted sibling]
old:
The B-weighted sibling `normalize_B` (rescale by the energy norm `√(xᴴ B x)`) is recorded below as a **rough-in note**, not a separate firm operator — Palace has the B-weighted reduction [`matrix-weighted-norm`](./matrix-weighted-norm.md) (rough-in) but **no** fused `Normalize`-with-`B` free function; B-weighted normalisation is always spelled inline, and the only inline B-energy rescale sites use the *unweighted* norm.
new:
The B-weighted sibling `normalize_B` (rescale by the energy norm `√(xᴴ B x)`) is recorded below as a **rough-in note**, not a separate firm operator — Palace ships a fused B-weighted `Normalize(comm, x, B, Bx)` free function (`palace/linalg/operator.hpp:377-384`) and the underlying reduction [`matrix-weighted-norm`](./matrix-weighted-norm.md) (rough-in), but the fused B-Normalize is **uncalled** (zero 4-arg callsites in the tree), and the only inline B-energy contexts (`arpack.cpp:438`, `slepc.cpp:475`, `nleps.cpp:114`) call the reduction for residual-ratio computations that do not rescale. So `normalize_B` has the L1 algebraic form but no live consumer.
```

```edit:book/src/L1/normalize.md
[at lines 87-88, replace the rough-in-note item 1 "No fused Palace site"]
old:
1. **No fused Palace site.** Palace has no `linalg::Normalize`-with-`B` free function. The header comment at `palace/linalg/vector.hpp:262` ("Normalize the vector, possibly with respect to an SPD matrix B") is **aspirational/documentary** — the sole `Normalize` overload (`:264`) takes no `B`. The B-weighted reduction exists ([`matrix-weighted-norm`](./matrix-weighted-norm.md) = `linalg::Norml2(comm, x, B, Bx)`, `palace/linalg/operator.cpp:600-619`), but its call sites (`palace/linalg/arpack.cpp:438`, `palace/linalg/slepc.cpp:475`, `palace/linalg/nleps.cpp:114`) are **error-norm / eigenvector-norm computations that do not rescale** — they feed `GetError` / residual ratios, not an in-place normalise.
new:
1. **Fused B-Normalize defined but uncalled.** Palace ships a fused B-weighted `Normalize(comm, x, B, Bx)` at `palace/linalg/operator.hpp:377-384` (def `:378`, B-weighted reduction `:380`, partiality guard `:381`, rescale `:382`, return `:383`) — structurally identical to the unweighted `vector.hpp:264` modulo threading `(B, Bx)` into the inner `Norml2`. The header comment at `palace/linalg/vector.hpp:262` ("Normalize the vector, possibly with respect to an SPD matrix B") is realised by the `operator.hpp:378` overload, not by the unweighted `vector.hpp:264`. **However, the fused B-Normalize is uncalled**: a grep across `palace/` for 4-arg `Normalize(comm, x, B, Bx)` invocations finds zero callsites. The B-weighted *reduction* `linalg::Norml2(comm, x, B, Bx)` ([`matrix-weighted-norm`](./matrix-weighted-norm.md), `palace/linalg/operator.cpp:600-619`) IS used at three callsites (`palace/linalg/arpack.cpp:438`, `palace/linalg/slepc.cpp:475`, `palace/linalg/nleps.cpp:114`) but they are **error-norm / eigenvector-norm computations that do not rescale** — they feed `GetError` / residual ratios, not an in-place normalise.
```

```edit:book/src/L1/normalize.md
[at line 90, replace the promotion-gate sentence (immediately before the signature block)]
old:
If/when an inline B-weighted normalise site surfaces (a `scale = Norml2(comm, v, B, Bv); v *= 1/scale` pattern, distinct from the unweighted nleps.cpp:610-611), `normalize_B` promotes to a firm sibling with signature:
new:
If/when a positive *callsite* of the fused B-Normalize surfaces — either a direct 4-arg `Normalize(comm, v, B, Bv)` invocation OR an inline B-weighted-rescale shape (`scale = Norml2(comm, v, B, Bv); v *= 1/scale`, distinct from the unweighted `nleps.cpp:610-611`) — `normalize_B` promotes to a firm sibling with signature:
```

```edit:book/src/L1/normalize.md
[at line 95, append a closing sentence to the rough-in section paragraph (just before "## Status")]
old:
Its laws mirror `normalize`'s with `nrm2` → `matrix_weighted_norm` (unit output is B-unit: `matrix_weighted_norm(û, B) = 1`), conditioned on `B` SPD. Until then it is tracked as a queued candidate inheriting the `matrix-weighted-norm` promotion gate, NOT a firm operator.
new:
Its laws mirror `normalize`'s with `nrm2` → `matrix_weighted_norm` (unit output is B-unit: `matrix_weighted_norm(û, B) = 1`), conditioned on `B` SPD. Until a callsite surfaces, `normalize_B` is tracked as a queued candidate inheriting the `matrix-weighted-norm` promotion gate, NOT a firm operator. The mere existence of the fused operator at `palace/linalg/operator.hpp:378` does not promote it — a defined-but-dead operator carries no live algebraic-law evidence beyond the syntactic identity to the unweighted core (which the unweighted `normalize` already records).
```

## Status changes

**None.** Per the dispatch brief: `## Status` lines in both files are NOT modified.

- `book/src/L1-L0/normalize-mutation-rotation.md` `## Status`: stays `firm` (the firm
  unweighted core is unaffected — the correction is on the non-firm `normalize_B` note).
- `book/src/L1/normalize.md` `## Status`: stays `firm` (firm-on-positive-structure
  precedent unchanged; the rough-in `normalize_B` note remains a rough-in note).
- `normalize_B` itself: stays rough-in (gate stays OPEN; the tightening shifts the
  gate's stated condition from "find that the function exists" to "find a positive
  *call* site", but does not close the gate).

## Speculative operators proposed

**None.** This dispatch is a prose-only correction; it introduces no new L1 vocabulary.
The `normalize_B` rough-in note remains a rough-in note (not promoted to a separate
chapter), and the existing rough-in dep-map row in `book/src/L1/index.md` (if any) is
unaffected.

## Supporting evidence

On-disk reads (this invocation, primary source):

- `reference/palace/palace/linalg/operator.hpp:370-389` — read: the fused B-weighted
  `Normalize(comm, x, B, Bx)` template (`:378`), with reduction `:380`, guard `:381`,
  rescale `:382`, return `:383`. Structurally identical to `vector.hpp:262-270`
  modulo the `(B, Bx)` extra args threaded into the reduction.
- `citecheck` (this invocation, deterministic anchor verification):
  - `palace/linalg/operator.hpp:377-384 --anchor 'Normalize(MPI_Comm comm, VecType &x, const Operator &B'` → 378 ok
  - `palace/linalg/operator.hpp:377-384 --anchor 'Norml2(comm, x, B, Bx)'` → 380 ok
  - `palace/linalg/operator.hpp:377-384 --anchor 'x *= 1.0 / norm'` → 382 ok
- `grep -rn "Normalize(" reference/palace/palace/ --include="*.cpp" --include="*.hpp" --include="*.h"`
  excluding 2-arg `Normalize(comm, x)` and the `MPI_Comm`-positional declaration
  pattern — surfaces only `waveportoperator.cpp:120,693` (an unrelated
  `GridFunction`-tuple `Normalize`, different signature) and the unweighted
  `Normalize(comm, u)` calls at `operator.cpp:661,673`. **No 4-arg
  `Normalize(comm, ?, B, ?)` callsite exists in the tree.**

Cross-references (already-firm anchors confirming the framing):

- `reports/2026-05-29T194558Z-lowering-verifier-normalize-mutation-rotation-audit/CYCLE.md`
  §"Edit 3 (F1, correctness fix to the `normalize_B` note) — GATED, routed to abstractor"
  (lines 331-354) — the verifier's routed-edit specification this dispatch realises.
  Also §"F1 promotion-side note" (lines 388-395) — the verifier's recommendation that
  the abstractor "also tighten the `normalize_B` promotion condition wording", which
  edit 1 (gate tightening) and edit 2 (parallel L1 gate tightening) implement.
- `book/src/L1-L0/normalize-mutation-rotation.md:466-469` — the verifier's existing
  `verified_against:` row for `operator.hpp:377-384` (verdict `does-not-support`, the
  F1 finding documented in-yaml). This dispatch resolves the routed correction.

## Open questions / caveats

- **Verifier `verified_against:` block (`book/src/L1-L0/normalize-mutation-rotation.md:466-473`) — leave intact.**
  The verifier's per-citation audit ledger records the F1 finding as
  `does-not-support` against `operator.hpp:377-384` with a precise diagnostic note.
  That row is a *historical audit record* (not a live claim); after this prose
  correction lands, the diagnostic note still accurately describes the WAS-state
  (the audit AS-OF 2026-05-29T19:45:58Z). I do NOT propose changing the
  `verified_against:` row. A future lowering-verifier re-audit cycle COULD upgrade
  the verdict to `supports` (now that the surrounding prose matches the source),
  but that is a verifier dispatch, not an abstractor one.

- **No `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md` edits proposed.**
  The verifier cohort confirms `operator.hpp:377-384` is the fused B-weighted
  `Normalize` definition; the matrix-weighted-norm theme cites the same range as a
  consumer site (cycle-026). That citation is not in conflict with this correction
  (the matrix-weighted-norm theme is correctly using the range as a *definition*
  site for its own Sub-pattern C, not asserting a non-existent function). No
  cross-theme edits needed.

- **L1>L0 dep-map / SUMMARY.md — no edits proposed.** This is a prose-only
  correction. No file is created, deleted, or renamed; no slug or status changes;
  no SUMMARY.md chapter additions; no dep-map row additions.

- **`normalize_B` promotion gate is now slightly looser AND slightly more correct.**
  Before: "find an inline B-weighted-rescale site". After: "find a callsite of the
  fused B-Normalize OR an inline B-weighted-rescale site". The gate accepts a
  superset of evidence (a 4-arg `Normalize(comm, v, B, Bv)` callsite would now
  qualify, where before the gate's stated phrasing wouldn't have explicitly named
  that case). This is a strict improvement: the gate matches the actual L0 surface.

- **OQ ledger.** The cycle-028 OQ
  `normalize_B-note-says-no-fused-B-Normalize-but-uncalled-fused-operator-exists`
  (the audit's `integration_notes:` named the route) is RESOLVED by this dispatch
  once integrated. The integrator-per-report SHOULD close it in
  `scaffolding/open-questions.md` (append-only close marker) when applying this
  report. I do NOT propose the OQ-ledger close-edit here (integrator's authority).

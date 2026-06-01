---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-01T195100Z
scope: VERIFY-body audit of the 2 gated constructed-operator-gate theme pairs (divfree-projector, jacobi-smoother) before cycle-051 demotion
status: integrated
integrated_at: 2026-06-01T222000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: APPLIED clean (cycle-050 D8, observation-only — NO book/ mutation). VERIFY-body audit of the 2 gated constructed-operator-gate theme pairs. Verdicts feed c051 enactment: jacobi-smoother-body-identity (L3>L2) DEMOTE-OK + jacobi-smoother-leaf-identity (L2>L1) DEMOTE-OK + divfree-projector-body-identity (L3>L2) DEMOTE-OK + divfree-projector-leaf-identity (L2>L1) KEEP-substantive (the one genuine fusion rotation — step-4 apply_linop ▷ axpy de-fuse/re-fuse to Grad->AddMult, divfree.cpp:185/:180-181). OVERTURNS the c049 D3 head-only classification for one pair; corrects the degenerate-cohort denominator 18→17. Load-bearing orphan-avoidance constraint promoted for c051 (the divfree L3>L2 demotion must keep the L2 floor + KEPT L2>L1 fusion theme reachable from the L3 entry). 3 OQs promoted. Build-relevant no (scaffolding-only). refactor-pass ENACTMENT under the 2026-06-01 VOCABULARY-SHIFT REDIRECT.
---

# CYCLE: Cross-layer observation — verify-body classification of the 2 cycle-049-D3-gated pairs

## Summary

The cycle-049 D3 degenerate-lowering audit read only the HEADS of the four constructed-operator-gate
themes for `divfree-projector` and `jacobi-smoother` and flagged them "verify-body-before-demoting."
Reading all four themes **in full**, plus all four L3/L2 endpoint entries, the verdict splits **three
DEMOTE-OK / one KEEP-substantive**:

- `jacobi-smoother-body-identity` (L3>L2) — **DEMOTE-OK**.
- `jacobi-smoother-leaf-identity` (L2>L1) — **DEMOTE-OK**.
- `divfree-projector-body-identity` (L3>L2) — **DEMOTE-OK**.
- `divfree-projector-leaf-identity` (L2>L1) — **KEEP-substantive**. It carries **exactly one genuine
  fusion rotation** (the step-4 `Grad->AddMult` apply-accumulate de-fuses at L2 into
  `apply_linop(P.Grad, ψ) ▷ axpy` and re-fuses at L1). That is a real fusion-rotation translation, not
  an identity-in-named-terms lowering, so it must stay off the cycle-051 demotion worklist.

The load-bearing reason `divfree-projector-body-identity` is still DEMOTE-OK while
`divfree-projector-leaf-identity` is KEEP: the four-step composition `WeakDiv → Z → ksp_solve → Grad`
is **explicit at ALL THREE layers (L1, L2, L3)** — it is NOT structure that L3 exposes and L2 collapses
(the scenario the dispatch warned to watch for). The composition-erasure the dispatch hypothesized does
not exist; the L3>L2 edge is a genuine same-named-terms identity. The ONE genuine vocabulary shift in
the whole projector chain (de-fuse/re-fuse of the fused MFEM `AddMult` idiom) lives entirely on the
L2>L1 edge.

## Observation kind

**Consistency drift / degenerate-cohort denominator correction** — a verify-body audit confirming the
cycle-049 D3 head-only classification for 3 of the 4 gated themes and **overturning it for 1**
(`divfree-projector-leaf-identity` is a genuine fusion-rotation translation, not a degenerate identity).
The degenerate-cohort "18" denominator (established by the cycle-049 D3 audit
`reports/2026-06-01T190900Z-cross-layer-cross-cutter-refactor-pass-degenerate-lowering-audit/CYCLE.md:80-93`,
§"(1c) SCOPE-BOUNDARY: the degenerate cohort is 18, not 12") drops by one to **17** for the cycle-051
demotion-enactment plan.

## Specific finding

### Pair 1 — `jacobi-smoother`: BOTH themes DEMOTE-OK

The Jacobi apply is **one elementwise product** `jacobi_smoother op x = op.dinv ⊙ x = (ω · diag(A)⁻¹) ⊙ x`,
and that body is **textually identical at L1, L2, and L3** (modulo `Field`/`Tensor` notational spelling):

- L3 `book/src/L3/jacobi-smoother.md:38` — `jacobi_smoother op x = op.dinv ⊙ x`; §Semantics: "a **single
  whole-tensor elementwise multiplication** — no `apply_linop` call, no residual recomputation, no
  `dot`/`nrm2` reduction, no sweep" (`L3/jacobi-smoother.md:59`).
- L2 `book/src/L2/jacobi-smoother.md:96` — `jacobi_smoother op x = op.dinv ⊙ x`; §"Negative fusion
  observation" (`L2/jacobi-smoother.md:160`): there is **no fused multi-operation kernel to unfold** —
  the L2 fusion-rotation work is a no-op.
- L1 form (cited in both themes) — same signature, same single-elementwise-product apply.

**`jacobi-smoother-body-identity` (L3>L2)** — `book/src/L3-L2/jacobi-smoother-body-identity.md`. The
rewrite table (data row `:112`) is a single-row identity: `jacobi_smoother op x = op.dinv ⊙ x` ⇒
`jacobi_smoother op x = op.dinv ⊙ x`, "Identity. Same signature, same single elementwise-product field
operation. … No operational adjustment occurs." The theme itself states "**The body IS the identity**"
(`:11`) and "there is no wrapper to rotate" (`:114`). This is a textbook §1d degenerate
identity-in-named-terms lowering (no vocabulary shift). → **DEMOTE-OK.**

**`jacobi-smoother-leaf-identity` (L2>L1)** — `book/src/L2-L1/jacobi-smoother-leaf-identity.md`. The
rewrite table (data rows `:104-107`) is row-for-row "Identity" — same signature, same apply, same variant
absorption, same six laws + three non-laws. The only "note" is the **negative** fusion observation
(`:112-114`): "there is **nothing to defer** … the L2 form is identical to the L1 form because there is
nothing to de-fuse." The theme explicitly says "The rewrite is the **identity on the gate**" (`:99`) and
the mapping is "total and bijective on the gate" (`:110`). No vocabulary shift. → **DEMOTE-OK.**

### Pair 2 — `divfree-projector`: L3>L2 DEMOTE-OK, L2>L1 KEEP-substantive

The four-step composition `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad` is **explicit at all three layers**:

- L3 §Semantics (`book/src/L3/divfree-projector.md:200-219`) lists the four steps as whole-tensor field
  operations, including step 4 already written as "an `apply_linop`-shaped apply **fused with** an
  `axpy`-shaped accumulate … via `Grad->AddMult(ψ, y, 1.0)`" (`:216-219`).
- L2 §Semantics (`book/src/L2/divfree-projector.md:114-134`) lists the **same four steps**, but with
  step 4 flagged as "**the one fused kernel the L2 layer un-folds**" (`:131-133`) and §"Fusion note"
  (`:174-186`) de-fusing it into `y' = axpy(1.0, apply_linop(P.Grad, ψ), y)`.
- L1 (cited) — step 4 in the **fused** form `Grad->AddMult(ψ, y, 1.0)`.

**`divfree-projector-body-identity` (L3>L2)** — `book/src/L3-L2/divfree-projector-body-identity.md`.
The rewrite table (`:91-100`) maps every L3 binding to the same-position L2 binding "Identity," and step
4 is explicitly "Identity (at this resolution). … the step-4 **fusion** treatment (de-fuse / re-fuse) is
the L2>L1 edge's content, NOT this edge's" (`:97`). Because the four-step composition is explicit at
**both** L3 and L2 (no structure exposed at one layer and collapsed at the other), the L3>L2 edge is a
genuine same-named-terms identity. The composition-erasure the dispatch warned to watch for **does not
occur at this edge** — L2 does NOT collapse the four-step structure; it keeps all four steps and only
de-fuses step 4 (which is the L2>L1 edge's concern). → **DEMOTE-OK.**

**`divfree-projector-leaf-identity` (L2>L1)** — `book/src/L2-L1/divfree-projector-leaf-identity.md`.
This is **NOT** a degenerate identity. The rewrite table (`:107-115`) is "Identity" on steps 1/2/3 and
the entire algebraic profile, but **step 4 is a genuine rotation** (`:113`):

> `step 4 axpy(1.0, apply_linop(P.Grad, ψ), y)` → `step 4 Grad->AddMult(ψ, y, 1.0)` — **RE-FUSION (the
> one genuine rotation).** The de-fused `apply_linop ▷ axpy` pair re-fuses into the single fused
> apply-and-accumulate; the intermediate `g = P.Grad · ψ` is re-absorbed (no materialization).

The theme's own opening states the rewrite is "**mostly identity-in-form on the gate, with exactly one
genuine fusion rotation**" (`:3-4`), and §"Justification kind" calls step 4 "a **structural fusion
rotation**" that is "the canonical L2>L1 rotation content (kernel fusion is unfolded at L2, re-fused at
L1)" (`:178-182`). This is a real translation across the L2↔L1 vocabulary boundary (de-fused base-algebra
composition ⇄ fused MFEM apply-accumulate idiom), positively anchored at `palace/linalg/divfree.cpp:185`
(real) / `:180-181` (complex). It is **not** an identity-in-named-terms lowering — the LHS (`apply_linop`
+ `axpy`, two base primitives) and the RHS (`AddMult`, one fused call) say genuinely different things in
different vocabularies. → **KEEP-substantive.**

This matches the existing kept-substantive L2>L1 fusion-rotation cohort (e.g.
`chebyshev-iteration-fusion`, `deflate-composition-lowering`) rather than the BLAS-1 `-leaf-identity`
degenerate cohort. Note the asymmetry is internally consistent: the projector's whole lowering chain
contains exactly one fusion, and it sits on the L2>L1 edge (where fusion lives), leaving the L3>L2 edge
a pure identity.

## Recommendation

- **cycle-051 demotion-enactment plan**: demote 3 of the 4 — `jacobi-smoother-body-identity`,
  `jacobi-smoother-leaf-identity`, `divfree-projector-body-identity` (collapse to in-line identity notes
  per the §1d degenerate-lowering treatment, alongside the 4 already-clean non-fold pairs).
- **KEEP `divfree-projector-leaf-identity` off the demotion worklist** — it is a genuine
  fusion-rotation translation (the one fusion in the projector chain). It stays a standalone L2>L1 theme.
- **Drop the degenerate-cohort denominator from 18 to 17** for the cycle-051 plan and the batch-15
  meta-phase intake (one of the head-only-flagged themes turned out substantive on body audit). The
  "18" source is the cycle-049 D3 audit
  `reports/2026-06-01T190900Z-cross-layer-cross-cutter-refactor-pass-degenerate-lowering-audit/CYCLE.md:80-93`
  (§"(1c) SCOPE-BOUNDARY: the degenerate cohort is 18, not 12"); the two verify-body-gated pairs it
  named are `divfree-projector` + `jacobi-smoother` (`:88`, `:92`).
- The divfree L3>L2 demotion has a downstream-consistency consequence: when
  `divfree-projector-body-identity` collapses to an in-line note, the L3 entry's `lowers_to` frontmatter
  + §"Lowers to" (currently routing through the adjacent L2 floor via the named theme) need the in-line
  identity-annotation treatment — but the L2 floor + the L2>L1 fusion theme must remain reachable so the
  one genuine rotation is not orphaned. (Surfaced for the cycle-051 integrator, not enacted here.)

## Supporting evidence

Themes (read in full this invocation):
- `book/src/L3-L2/jacobi-smoother-body-identity.md` — single-row identity rewrite table (data row `:112`);
  "The body IS the identity" (`:11`); "no wrapper to rotate" (`:114`).
- `book/src/L2-L1/jacobi-smoother-leaf-identity.md` — row-for-row identity table (data rows `:104-107`); negative
  fusion observation (`:112-114`); "identity on the gate … total and bijective" (`:99-110`).
- `book/src/L3-L2/divfree-projector-body-identity.md` — identity rewrite table (`:91-100`); step 4
  explicitly "Identity (at this resolution)" with fusion deferred to L2>L1 (`:97`); four-step composition
  "explicit at both layers" (`:46-51`).
- `book/src/L2-L1/divfree-projector-leaf-identity.md` — "mostly identity-in-form … with exactly one
  genuine fusion rotation" (`:3-4`); step-4 RE-FUSION row (`:113`); "structural fusion rotation … the
  canonical L2>L1 rotation content" (`:178-182`).

Endpoint entries (read in full):
- `book/src/L3/jacobi-smoother.md` — apply `op.dinv ⊙ x` (`:38`); single elementwise multiplication,
  no obstruction (`:59`, `:65`).
- `book/src/L2/jacobi-smoother.md` — apply `op.dinv ⊙ x` (`:96`); §"Negative fusion observation"
  (`:160`).
- `book/src/L3/divfree-projector.md` — four-step composition with step 4 already fused-shaped
  (`:200-219`).
- `book/src/L2/divfree-projector.md` — four-step composition with step 4 de-fused (`:114-134`, §"Fusion
  note" `:174-186`).

L0 anchors (transitive through firm L1; cited by the themes, spot-confirmed against
`reference/palace/`):
- `palace/linalg/jacobi.cpp:38` — `Y[i] = DI[i] * X[i]` (the single Jacobi elementwise-multiply kernel).
- `palace/linalg/divfree.cpp:155-187` — `DivFreeSolver<VecType>::Mult` four-step apply.
- `palace/linalg/divfree.cpp:185` / `:180-181` — `Grad->AddMult(ψ, y, 1.0)` the fused step-4
  apply-accumulate (the one genuine rotation's positive anchor).

## Open questions / caveats

- **OQ (denominator):** the degenerate-cohort count used by the cycle-051 demotion plan and the
  batch-15 meta-phase should be recorded as **17, not 18** — `divfree-projector-leaf-identity` is
  substantive. The "18" was established by the cycle-049 D3 audit
  `reports/2026-06-01T190900Z-cross-layer-cross-cutter-refactor-pass-degenerate-lowering-audit/CYCLE.md:80-93`
  (§"(1c)"); if the "18" was load-bearing in any prior planning arithmetic, that arithmetic needs the
  −1 correction.
- **Caveat (not a status reduction, inherited):** both projector themes carry the `Mult` per-method
  doc-inversion OQ `divfree-mult-doc-irrotational-vs-divfree-stale` (`palace/linalg/divfree.hpp:64-66`
  inverted vs. class doc `:28-31`). Orthogonal to the demote/keep verdict — both endpoints carry the
  divergence-free semantics regardless.
- **Caveat:** I did not re-run citecheck on the cited L0 ranges; the themes' `verified-against` blocks
  record per-line `--anchor` self-verification from their authoring cycles, and I confirmed the
  load-bearing distinction (single-elementwise-product vs. four-step-with-one-fusion) by reading the L3
  and L2 entry bodies directly. The classification verdict does not depend on a fresh citecheck — it
  depends on the body structure, which is unambiguous in the entries.
- **OQ (boundary case for the §1d smell rule):** `divfree-projector-body-identity` is a degenerate
  identity even though its body is a four-step composition (not a single leaf). This is a useful witness
  that "degenerate identity-in-named-terms" is about **no vocabulary shift across the edge**, NOT about
  body simplicity — a multi-step composition can still be a degenerate identity if both layers spell it
  identically. The cycle-051 demotion treatment should preserve the four-step composition in the
  in-line note (it is not a one-liner like the BLAS-1 leaves).

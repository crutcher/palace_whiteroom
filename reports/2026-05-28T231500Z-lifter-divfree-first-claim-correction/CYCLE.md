---
agent: lifter
invoked_at: 2026-05-28T231500Z
scope: L1>L0 theme content-correction — divfree-projector-mutation-rotation "first"/"no other op" nesting-gate claims
status: integrated
integrated_at: 2026-05-29T030000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-018 finalize — divfree-projector-mutation-rotation.md 'first nested-gate instance' claim corrected to 'third' (eigsolve-mutation-rotation cycle-011 is the prior + richer instance; divfree is the 3rd); firm unchanged; prong (b) of OQ nested-constructed-operator-gate-concept-and-divfree-correction (resolved) + OQ divfree-closure-nesting-constructed-gate-carrying-constructed-gate (answered->resolved)."
inputs:
  - book/src/L1-L0/divfree-projector-mutation-rotation.md
  - reports/2026-05-28T220000Z-cross-layer-cross-cutter-closure-nesting-gate/CYCLE.md
  - reports/2026-05-28T231017Z-layer-intro-author-nested-gate-concept/CYCLE.md
  - book/src/L1-L0/eigsolve-mutation-rotation.md (sub-pattern B, the prior richer instance)
  - book/src/L1/eigsolve.md (closure carries two nested gates; prose-names the pattern)
  - book/src/concepts/nested-constructed-operator-gate.md (concept page created THIS cycle)
---

# CYCLE: Re-anchor divfree-projector-mutation-rotation — correct "first" / "no other op" nesting-gate claims

## Summary

The firm L1>L0 theme `book/src/L1-L0/divfree-projector-mutation-rotation.md`
(landed cycle-016, `b54ea1c`) claims in two places to be the **first** L1>L0
mutation-rotation whose closure carries another constructed-operator gate as a
sub-field, and that the closure-nesting shape is **shared with no other current
L1 op**. The cycle-017 cross-layer-cross-cutter audit (critic VERIFIED-SOUND,
`reports/2026-05-28T220000Z-cross-layer-cross-cutter-closure-nesting-gate/`)
refuted both: the firm `eigsolve-mutation-rotation` theme (landed cycle-011,
`8bb16b7`, five cycles before divfree) is the prior and **richer** instance —
its closure `E` carries TWO nested gates (`E.linear : Solver[A]` and
`E.projector : Maybe DivFreeSolver[ComplexVector]`), and `E.projector` is the
divfree projector itself, so the nesting is transitively three-deep (eigsolve ⊃
divfree ⊃ ksp). Divfree is the **third** instance, not the first.

This dispatch makes a **bounded content-correction** (within the lifter
content-correction boundary, `.claude/agents/lifter.md` §Discipline + CLAUDE.md
friction-ledger `lifter-scope-content-correction-boundary`): the two inaccurate
claims at `:108-113` (sub-pattern A bullet) and `:457-464` (Open-questions item)
are corrected to position divfree accurately as the third instance and to
reference (a) the new `nested-constructed-operator-gate` concept page (created
this cycle by the layer-intro-author dispatch, exists at build time) and (b) the
eigsolve precedent (`eigsolve-mutation-rotation` sub-pattern B; `eigsolve.md:136`,
`:60`, `:140`). The correction is surgical — the theme's structure, rotation,
sub-patterns, and the legitimate fact that `P.ksp` IS a nested constructed-
operator gate are all preserved; only the FALSE uniqueness/primacy framing is
removed. This is NOT re-architecting (no decomposition, signature, or sub-pattern
change), so it stays within the lifter boundary. Addresses OQ
`nested-constructed-operator-gate-concept-and-divfree-correction` prong b.

## Proposed changes

### 1. Sub-pattern A bullet — correct the "first" claim (current `:108-113`)

```edit:book/src/L1-L0/divfree-projector-mutation-rotation.md
[old]:- **Inner solve is itself a constructed-operator gate.** `ksp->Mult(rhs, psi)`
  (step 3) is the [`ksp_solve`](../L1/ksp_solve.md) inner H1 solve. Its CG
  iteration is interior to `ksp_solve` and does not leak into this theme; here
  it is the opaque `K⁻¹` action. This is the first L1>L0 mutation-rotation whose
  closure carries *another* constructed-operator gate as a sub-field
  (`P.ksp : Solver[P.M]`).
[new]:- **Inner solve is itself a constructed-operator gate.** `ksp->Mult(rhs, psi)`
  (step 3) is the [`ksp_solve`](../L1/ksp_solve.md) inner H1 solve. Its CG
  iteration is interior to `ksp_solve` and does not leak into this theme; here
  it is the opaque `K⁻¹` action — the
  [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
  fidelity rule (the inner gate's iteration stays interior to its own lowering
  theme). This theme's closure carries *another* constructed-operator gate as a
  sub-field (`P.ksp : Solver[P.M]`) — the
  [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
  shape. It is **not the first** such case: the firm
  [`eigsolve-mutation-rotation`](./eigsolve-mutation-rotation.md) theme (landed
  cycle-011) is the prior and richer instance, whose closure `E` carries **two**
  nested gates (`E.linear : Solver[A]` and `E.projector : Maybe
  DivFreeSolver[ComplexVector]` — the latter being this projector itself,
  [`L1/eigsolve`](../L1/eigsolve.md) §Shape contract `E`), so the nesting is
  transitively three-deep (eigsolve ⊃ divfree ⊃ ksp). Divfree is the **second**
  gate-carrying L1>L0 theme (after eigsolve), carrying the **third** nested gate
  overall (after eigsolve's two, `E.linear` + `E.projector`).
```

### 2. Open-questions item — correct the "no other current L1 op" claim (current `:457-464`)

```edit:book/src/L1-L0/divfree-projector-mutation-rotation.md
[old]:- **Inner `ksp_solve` is a nested constructed-operator gate.** `P.ksp :
  Solver[P.M]` means this theme's closure carries another L1 constructed-operator
  as a sub-field — the first such case in the L1>L0 mutation-rotation family.
  The CG iteration is interior to [`ksp_solve`](../L1/ksp_solve.md) and is the
  standard Krylov sequential obstruction; it does not leak into this theme. A
  cross-layer-cross-cutter pass may want to note the closure-nesting pattern
  (constructed gate carrying a constructed gate) as a recurring structural shape
  shared with no other current L1 op.
[new]:- **Inner `ksp_solve` is a nested constructed-operator gate.** `P.ksp :
  Solver[P.M]` means this theme's closure carries another L1 constructed-operator
  as a sub-field — an instance of the
  [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
  shape. The CG iteration is interior to [`ksp_solve`](../L1/ksp_solve.md) and is
  the standard Krylov sequential obstruction; it does not leak into this theme
  (the concept's cross-layer fidelity rule). This is **not** a shape unique to
  this theme: the firm [`eigsolve-mutation-rotation`](./eigsolve-mutation-rotation.md)
  theme (sub-pattern B, `book/src/L1-L0/eigsolve-mutation-rotation.md:213-258`;
  the **core sub-pattern** of that theme, lowering ten `opInv->Mult` inner-solve
  call sites through the firm `ksp-solve-mutation-rotation` theme) is the prior
  (cycle-011) and richer instance — its closure carries **two** nested gates
  (`E.linear`, `E.projector`; [`L1/eigsolve`](../L1/eigsolve.md) §Shape contract
  `E` at `:60`, prose-named "the first L1 operator to compose two layers of
  constructed-operator absorption" at `book/src/L1/eigsolve.md:136`, and
  "composed-not-inherited" at `:140`). Divfree is the **second** gate-carrying
  theme (after eigsolve), carrying the **third** nested gate overall (one gate
  of its own, after eigsolve's two). Because `E.projector` is this projector itself, the two confirmed
  instances are transitively nested three-deep (eigsolve ⊃ divfree ⊃ ksp). See
  the [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
  concept page for the full instance index, the latent `ksp_solve`-preconditioner
  site, and the fidelity rule.
```

## Discipline notes

**Content-correction, not authorship — bounded + evidenced + recorded** per
`.claude/agents/lifter.md` §Discipline ("L0-evidence-driven prose correction is
in-scope when bounded + evidenced + recorded"; here the supporting evidence is
firm artifact content + a VERIFIED-SOUND cross-cutter audit rather than a raw L0
citation, but the same boundary applies — fixing a factually-wrong claim, not
re-architecting):

- **What changed**: removed the false "first" (sub-pattern A bullet) and "first
  such case … shared with no other current L1 op" (Open-questions item)
  uniqueness/primacy framing. Replaced with accurate positioning as the **third**
  gate-carrying-gate instance (after eigsolve's two nested gates), plus live
  references to the `nested-constructed-operator-gate` concept page and the
  eigsolve precedent.
- **What is preserved (legitimate structural content)**: the gate-nesting IS a
  real and notable feature of divfree — the corrections keep that, only removing
  the false claim that divfree is the FIRST/ONLY instance. The rotation,
  sub-patterns A–D, justification kinds, citations, and applicability conditions
  are untouched. No decomposition / signature / sub-pattern change → within the
  lifter boundary (NOT a re-architecting re-route).
- **Why bounded**: the edit touches exactly the two flagged passages; it does not
  alter the theme's LHS (L1 form) or RHS (L0 form), and it does not invert the
  high→low rewrite direction (the correction is purely about cross-theme
  provenance, narrated in the existing forward orientation).
- **Cross-references to the promoting/refuting reports**: the cycle-017
  cross-layer-cross-cutter audit
  (`reports/2026-05-28T220000Z-cross-layer-cross-cutter-closure-nesting-gate/CYCLE.md`,
  critic VERIFIED-SOUND, §Specific finding + §Recommendation follow-up #1)
  established the refutation and routed this prong-b correction to a
  lifter/harvester dispatch; this cycle's layer-intro-author dispatch
  (`reports/2026-05-28T231017Z-layer-intro-author-nested-gate-concept/CYCLE.md`,
  prong a) creates the `nested-constructed-operator-gate` concept page the
  corrected passages now link.

**Citation self-verification (lifter §Discipline "Self-verify every citation
against source BEFORE emitting it").** Each citation emitted in the corrected
passages was read against its source line this dispatch:

- `book/src/L1/eigsolve.md:60` — READ: `E` "additionally binds the inner linear
  solver (`linear : Solver[A]` …), the optional divergence-free projector
  (`projector : Maybe DivFreeSolver[ComplexVector]`)". CONFIRMED — two nested
  gates on the asserted line; `E.projector` is the DivFreeSolver itself.
- `book/src/L1/eigsolve.md:136` — READ verbatim: "**This is the second L1
  operator (after `ksp_solve` itself depending on `apply_linop`) whose primary
  dependency is itself a constructed-operator type**, making `eigsolve` the first
  L1 operator to compose two layers of constructed-operator absorption."
  CONFIRMED on the asserted line.
- `book/src/L1/eigsolve.md:140` — READ: "This is structurally the same nesting
  pattern as preconditioner application inside an iterative solver —
  composed-not-inherited." CONFIRMED on the asserted line.
- `book/src/L1-L0/eigsolve-mutation-rotation.md:213-258` — READ: "### Sub-pattern
  B — inner-solve mutation-rotation … This is the **core sub-pattern** of the
  theme … ten `opInv->Mult(b, x)` call sites … Each `opInv->Mult(b, x)` rewrites
  by the firm `ksp-solve-mutation-rotation` theme." CONFIRMED — the range opens at
  `:213` with the Sub-pattern B heading and the ten call sites are enumerated
  through `:258`.

The concept-page link target
(`book/src/concepts/nested-constructed-operator-gate.md`) is created THIS cycle
by the layer-intro-author prong-a dispatch; per the dispatch directive and
lifter §Discipline a live link is OK since the file exists at build time. This is
its TERMINAL firm home (a freshly-authored concept page, not a relocated
dangle).

## Supporting evidence

- `reports/2026-05-28T220000Z-cross-layer-cross-cutter-closure-nesting-gate/CYCLE.md`
  — VERIFIED-SOUND audit refuting the "first"/"no other op" claims; §Specific
  finding lists the exact divfree lines (`:108-113`, `:457-464`) and the eigsolve
  precedent; §Open questions follow-up #2 routes this prong-b correction.
- `reports/2026-05-28T231017Z-layer-intro-author-nested-gate-concept/CYCLE.md` —
  prong-a dispatch creating `book/src/concepts/nested-constructed-operator-gate.md`
  (the link target).
- `book/src/L1-L0/eigsolve-mutation-rotation.md:213-258` — the prior richer
  (two-gate) instance's core sub-pattern B; the inner-solve gate delegated to the
  firm `ksp-solve-mutation-rotation` theme.
- `book/src/L1/eigsolve.md:60,136,140` — the eigsolve closure's two nested gates +
  the prose-named "first to compose two layers of constructed-operator
  absorption" + "composed-not-inherited".
- Provenance (inherited from the VERIFIED-SOUND cross-cutter audit, not
  independently re-run): `8bb16b7` (cycle-011, eigsolve theme) predates `b54ea1c`
  (cycle-016, divfree theme) by five cycles.

## Open questions / caveats

- **Append-only after `integrated_at:`**. This theme's frontmatter is already
  set (landed cycle-016). Per CLAUDE.md §Methodology invariants "Reports are
  append-only after integration" and the cross-cutter's note (follow-up #1: "this
  should be a scoped correction dispatch, not a free edit"), this is exactly that
  scoped correction dispatch — the integrator applies the two proposed-changes
  blocks; no other content is touched.
- **OQ `closure-nesting-constructed-gate-carrying-constructed-gate` should be
  ANSWERED** (cross-cutter follow-up #3) — its "does not recur" premise is refuted
  by the eigsolve precedent. That OQ-ledger update is an integrator / separate
  concern, surfaced here for routing, not enacted by this lifter dispatch (the
  ledger append is integrator-per-report authority).
- **No re-architecting required**. The firmed-up vocabulary (the concept page) did
  NOT change the theme's signature, decomposition, or rotation — only the
  cross-theme provenance framing was wrong. So this stays a pure bounded
  content-correction within the lifter boundary; no abstractor reread is needed.
- **The `eigsolve` theme carries a `partly-constructive` `LinearSolveFailed`
  sub-part** — but that is a SEPARATE status concern about a discarded inner-solve
  convergence status, NOT about the gate-nesting structure (sub-pattern B is itself
  firm and source-anchored). So citing `eigsolve` as the prior FIRM instance of the
  gate-carrying-gate shape is sound, independent of that caveat (confirmed against
  the cross-cutter §Open questions resolution-disposition note and the concept-page
  dispatch §Firm instances).

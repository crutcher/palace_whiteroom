---
agent: abstractor
invoked_at: 2026-05-31T14:15:00Z
scope: L1>L0 annotation — CG initial-residual quirk (Norml2-vs-Dot asymmetry, likely-Palace-bug recognition-rule caveat) into `ksp-solve-mutation-rotation` Sub-pattern B
status: applied
inputs:
  - book/src/L1-L0/ksp-solve-mutation-rotation.md (firm theme; CG Sub-pattern B, lines 159-295)
  - book/src/spec/slices/cg.md:20 (slice working-note seed)
  - reference/palace/palace/linalg/iterative.cpp:398-411 (the quirky branch — L0 source)
  - reference/palace/palace/linalg/vector.hpp:257-260 (`linalg::Norml2` definition — the asymmetry's mechanical cause)
  - scaffolding/open-questions.md:30 (OQ `cg-initial-residual-quirk-palace-bug-flag-lift-path`)
integrated_at: 2026-05-31T18:01:20Z
integration_commit: a0b4d99
integration_notes: |
  cycle-035 D2 — applied by integrator-per-report at 2026-05-31T15:55:00Z (staging row 2); housekept by integrator-finalize at 2026-05-31T18:01:20Z. Two surgical additive edits applied to book/src/L1-L0/ksp-solve-mutation-rotation.md CG Sub-pattern B: (1) new Recognition note (likely-Palace-bug Norml2-vs-Dot initial-residual asymmetry; section header explicitly hedges "likely Palace bug; upstream confirmation pending") at lines 267-318, IMMEDIATELY AFTER the existing CheckDot Recognition note and BEFORE the Citations: block; (2) 2 new Citations: rows at lines 358-368 for iterative.cpp:398-411 + vector.hpp:257-260. Theme stays firm — additive caveat only; no laws/signatures/operators/status changes. OQ cg-initial-residual-quirk-palace-bug-flag-lift-path NARROWED: lift portion CLOSED on landing; narrower sub-OQ cg-initial-residual-quirk-upstream-confirmation-pending retained for bug-vs-intentional classification (out-of-scope for this project — requires Palace maintainer answer; Trigger: upstream issue filed or git blame iterative.cpp:408). Citecheck 26 ok / 0 failing; both new citations anchor-verified (initial_guess at 398; Norml2 at 257). No book rebuild here; finalize ran cargo make book exit 0 in 90.81s. Single commit covering all 3 cycle-035 reports + housekeeping.
---

# CYCLE: L1>L0 annotation — CG initial-residual quirk (Norml2-vs-Dot asymmetry, likely-Palace-bug recognition-rule caveat)

## Summary

The Phase-1 `cg.md` slice recorded a `Norml2`-vs-`Dot` asymmetry in `CgSolver<OperType>::Mult`'s `initial_guess` branch (`palace/linalg/iterative.cpp:398-411`) as a likely Palace bug: the `B`-preconditioned arm uses `linalg::Dot(comm, p, b)` (where `p = B·b`) and squares-roots once, yielding `‖b‖_B`; the `!B` unpreconditioned arm uses `linalg::Norml2(comm, b)` (which **already** square-roots-of-dot internally — see `vector.hpp:257-260`) and then squares-roots **again** at `iterative.cpp:411`, yielding `(b·b)^{1/4}` rather than the intended `‖b‖₂`. I verified the slice's claim end-to-end against on-disk source: the asymmetry is real, mechanical, and reduces to a missing `linalg::Dot(comm, b, b)` (or equivalent `* Norml2(comm, b)`) on the `!B` line. This dispatch adds a **surgical Recognition note** to the firm L1>L0 `ksp-solve-mutation-rotation` theme's CG Sub-pattern B and appends two `Citations:` rows documenting the asymmetric call sites; the firm-theme status is unchanged (the annotation is additive and the existing laws are not touched). The OQ flag for upstream confirmation stays open under a narrowed scope ("file an upstream issue / confirm with Palace maintainers"), since the bug-vs-intentional-quirk classification ultimately needs an upstream answer this project cannot produce.

## Proposed changes

```edit:book/src/L1-L0/ksp-solve-mutation-rotation.md
<<<OLD
Recognition note: a `CheckDot` helper
(`palace/linalg/iterative.cpp:21-32`, called at lines 396, 410, 445, 461)
guards against the preconditioner becoming non-SPD or the operator
becoming non-positive-definite — `(Br, r) ≤ 0` or `(Ap, p) ≤ 0` aborts
the solve with an explanatory error message. This is a **load-bearing
algebraic precondition** of CG (CG requires SPD `A` and SPD
preconditioner `B`); the check is not transparent. At L1 the SPD
contract lives on `K`'s opaque type as a precondition not visible in the
signature — the `Solver[A]` type tag elides the SPD requirement, but
constructing `K` with `KrylovSolver::CG` carries the obligation.
Violating the obligation at runtime trips the `CheckDot` abort. Lifting
the SPD precondition into the type system is an L4 typing-rule question;
see [`mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md)
notes-for-higher-layers §3 and [`L1/ksp_solve`](../L1/ksp_solve.md)
"L1 vs L0 distinction" for the discussion.
===NEW
Recognition note: a `CheckDot` helper
(`palace/linalg/iterative.cpp:21-32`, called at lines 396, 410, 445, 461)
guards against the preconditioner becoming non-SPD or the operator
becoming non-positive-definite — `(Br, r) ≤ 0` or `(Ap, p) ≤ 0` aborts
the solve with an explanatory error message. This is a **load-bearing
algebraic precondition** of CG (CG requires SPD `A` and SPD
preconditioner `B`); the check is not transparent. At L1 the SPD
contract lives on `K`'s opaque type as a precondition not visible in the
signature — the `Solver[A]` type tag elides the SPD requirement, but
constructing `K` with `KrylovSolver::CG` carries the obligation.
Violating the obligation at runtime trips the `CheckDot` abort. Lifting
the SPD precondition into the type system is an L4 typing-rule question;
see [`mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md)
notes-for-higher-layers §3 and [`L1/ksp_solve`](../L1/ksp_solve.md)
"L1 vs L0 distinction" for the discussion.

Recognition note (initial-residual `Norml2`-vs-`Dot` asymmetry —
**likely Palace bug; upstream confirmation pending**): the
`initial_guess`-branch initial-residual computation at
`palace/linalg/iterative.cpp:398-411` exhibits a structural asymmetry
between the preconditioned (`B`) and unpreconditioned (`!B`) arms that
makes the L1 `initial_res` field's reconstruction quirky in the
`!B && initial_guess` case. The two arms write `beta_rhs` differently
before the shared `initial_res = std::sqrt(std::abs(beta_rhs));`
collapse at line 411:

    // B (preconditioned) arm — iterative.cpp:401-405
    ApplyB(B, b, p, this->use_timer);
    beta_rhs = linalg::Dot(comm, p, b);     // = (B·b, b) = ⟨b, b⟩_B

    // !B (unpreconditioned) arm — iterative.cpp:406-409
    beta_rhs = linalg::Norml2(comm, b);     // = ‖b‖₂ = sqrt(|b·b|)

The mechanical cause is `linalg::Norml2`'s body at
`palace/linalg/vector.hpp:257-260`:

    template <typename VecType>
    inline auto Norml2(MPI_Comm comm, const VecType &x)
    {
      return std::sqrt(std::abs(Dot(comm, x, x)));
    }

`Norml2` **already** square-roots-of-dot internally, so on the `!B` arm
`beta_rhs = sqrt(|b·b|)` rather than the symmetry-consistent `b·b` the
`B` arm produces. Then line 411 takes a **second** square root —
`initial_res = sqrt(|beta_rhs|) = sqrt(sqrt(|b·b|)) = (b·b)^{1/4}` —
where the algorithm's intent (the `B` arm reconstructs as
`sqrt(⟨b, b⟩_B) = ‖b‖_B`, and in the `B == identity` limit this should
collapse to `‖b‖₂ = (b·b)^{1/2}`) demands `initial_res = ‖b‖₂`. The
two arms therefore disagree at `B == identity` by a missing inner
square root: the `!B` arm produces the fourth root of `b·b`, not the
square root. The downstream consumer is `eps = std::max(rel_tol *
initial_res, abs_tol);` at line 417 — the convergence tolerance is
quirky-scaled in the `!B && initial_guess` case, biasing
relative-tolerance convergence for cold-vs-warm-start asymmetrically.
The bug does not affect the unpreconditioned cold-start case (line 415
falls through to `initial_res = res;` where `res = sqrt(|b·b|) = ‖b‖₂`
correctly via the line-395-396 path), and does not affect the
preconditioned warm-start case (the `B` arm computes the intended
`‖b‖_B`). It affects **only** `!B && initial_guess`. The faithful L1>L0
recognition rule is: the `!B && initial_guess` branch's `initial_res`
field is `(b·b)^{1/4}` as written, not `‖b‖₂`; L1 consumers that
interpret `initial_res` as `‖b‖₂` are reading the L1 abstraction's
intended semantics rather than the L0 reality. **This is recorded as a
likely Palace bug** (the symmetric form, by analogy with the `B` arm
and the consistent `iterative.cpp:395-396` unpreconditioned cold-start
`res` computation, would be `beta_rhs = linalg::Dot(comm, b, b);` at
line 408); upstream confirmation that the asymmetry is unintentional is
pending. The corresponding warm-vs-cold initial-residual computation in
`GmresSolver` is factored into the `InitialResidual` helper
(`palace/linalg/iterative.cpp:252-285`, called at
`iterative.cpp:566-567`, noted in Sub-pattern C) which uses a different
internal control flow and is **not** affected by this asymmetry — the
bug is local to `CgSolver<OperType>::Mult`. See OQ
`cg-initial-residual-quirk-palace-bug-flag-lift-path` (narrowed to
upstream-confirmation; the lift annotation now lives here in the firm
artifact).
>>>
```

```edit:book/src/L1-L0/ksp-solve-mutation-rotation.md
<<<OLD
- `palace/linalg/iterative.cpp:484-485` — `final_res = res;
  final_it = it;` — the `mutable`-state write-out that the outer
  `BaseKspSolver::Mult` reads via `GetFinalRes()` /
  `GetNumIterations()`.
===NEW
- `palace/linalg/iterative.cpp:484-485` — `final_res = res;
  final_it = it;` — the `mutable`-state write-out that the outer
  `BaseKspSolver::Mult` reads via `GetFinalRes()` /
  `GetNumIterations()`.
- `palace/linalg/iterative.cpp:398-411` — `initial_guess`-branch
  `initial_res` computation; the `B` arm uses `linalg::Dot(comm, p, b)`
  at line 404 (where `p = B·b`), the `!B` arm uses
  `linalg::Norml2(comm, b)` at line 408 — the asymmetric form
  documented in the "initial-residual `Norml2`-vs-`Dot` asymmetry"
  recognition note above (likely Palace bug; upstream confirmation
  pending).
- `palace/linalg/vector.hpp:257-260` — `linalg::Norml2` definition:
  `std::sqrt(std::abs(Dot(comm, x, x)))`. The internal square root is
  the mechanical cause of the `initial_res = (b·b)^{1/4}` outcome on
  the `!B && initial_guess` branch (line 411 takes the second square
  root over `beta_rhs`).
>>>
```

## Insertion-point rationale

The new Recognition note sits **immediately after** the existing `CheckDot` Recognition note (which ends at theme line 265) and **before** the `Citations:` block (starting line 267). Rationale:

- Both Recognition notes are about the **CG inner body** (Sub-pattern B); grouping them is the existing structural convention in the theme (each sub-pattern's prose ends with Recognition notes, then a Citations list).
- The `CheckDot` note discusses a load-bearing algebraic precondition (SPD); the new note discusses a load-bearing algebraic *quirk* (the asymmetric `initial_res` reconstruction). The two notes are sibling caveats, both about how the L1 form's claimed semantics relate to what L0 actually does.
- Two `Citations:` rows are appended (line 411's neighbourhood + `vector.hpp:257-260` for the `Norml2` definition) so the annotation's cited evidence is in the theme's standard evidence-block format.
- The existing `initial_res` mentions at theme lines 239-241 and 276 are kept — they are correct as-is (they describe the `mutable`-state write-out pattern and the zero-residual short-circuit, neither of which the asymmetry contradicts). The new note adds a layer on top, not a replacement.

## Verification (each citation self-checked against on-disk source pre-emit)

Mechanical pass:

```
$ python3 tools/citecheck/citecheck.py palace/linalg/iterative.cpp:398-411 --anchor 'initial_guess'
[ok  ] palace/linalg/iterative.cpp:398-411  (anchor lit: 'initial_guess')
       anchor at line(s) [398] within range 398-411

$ python3 tools/citecheck/citecheck.py palace/linalg/iterative.cpp:404-404 --anchor 'Dot'
[ok  ] palace/linalg/iterative.cpp:404-404  (anchor lit: 'Dot')

$ python3 tools/citecheck/citecheck.py palace/linalg/iterative.cpp:408-408 --anchor 'Norml2'
[ok  ] palace/linalg/iterative.cpp:408-408  (anchor lit: 'Norml2')

$ python3 tools/citecheck/citecheck.py palace/linalg/iterative.cpp:411-411 --anchor 'initial_res'
[ok  ] palace/linalg/iterative.cpp:411-411  (anchor lit: 'initial_res')

$ python3 tools/citecheck/citecheck.py palace/linalg/vector.hpp:257-260 --anchor 'Norml2'
[ok  ] palace/linalg/vector.hpp:257-260  (anchor lit: 'Norml2')
```

Semantic pass (read for meaning, not just bounds): the on-disk content at `palace/linalg/iterative.cpp:401-405` is `if (B) { ApplyB(B, b, p, this->use_timer); beta_rhs = linalg::Dot(comm, p, b); }` (with `ScalarType beta_rhs;` declared on line 400, just above the cited range) — confirms `B` arm uses `Dot(p, b)` with `p = B·b`. The on-disk content at `palace/linalg/iterative.cpp:406-409` is `else { beta_rhs = linalg::Norml2(comm, b); }` — confirms `!B` arm uses `Norml2(b)`. The on-disk content at `palace/linalg/vector.hpp:259` is `return std::sqrt(std::abs(Dot(comm, x, x)));` — confirms `Norml2` internally square-roots. The composition therefore yields `initial_res = sqrt(|sqrt(|b·b|)|) = (b·b)^{1/4}` on the `!B && initial_guess` branch.

Cross-check against the line-395-396 `res` computation (theme already cites these as `iterative.cpp:418-419` short-circuit context): line 395 `beta = linalg::Dot(comm, z, r);` then line 397 `res = std::sqrt(std::abs(beta));` produces `res = sqrt(|⟨z, r⟩|) = sqrt(|(Br, r)|) = ‖r‖_B` on the unpreconditioned cold-start path (where `z = r = b`, `B == I`, so `res = sqrt(|b·b|) = ‖b‖₂`). This is the **symmetric** form: one `Dot`, one `sqrt`. The `initial_res` `!B` branch breaks this symmetry by using `Norml2` (which is itself `sqrt(Dot(...))`) where `Dot` should have been used. The bug is local and surgical: replace `linalg::Norml2(comm, b)` with `linalg::Dot(comm, b, b)` at line 408 to restore symmetry. (This bug-fix sketch is informational; we do not propose modifying Palace.)

## Speculative operators proposed

None. This dispatch is a recognition-rule caveat annotation on existing firm material; no new vocabulary is introduced. The annotation cites only operators already present in the theme (`linalg::Dot`, `linalg::Norml2`, `ApplyB`) and the existing L1 `initial_res` field semantics — no rough-in additions.

## Supporting evidence

L0 source citations (all self-verified above):

- `palace/linalg/iterative.cpp:398-411` — the `initial_guess`-branch `initial_res` computation (the quirky branch).
- `palace/linalg/iterative.cpp:404-404` — `beta_rhs = linalg::Dot(comm, p, b);` (the `B` arm, the symmetric form).
- `palace/linalg/iterative.cpp:408-408` — `beta_rhs = linalg::Norml2(comm, b);` (the `!B` arm, the asymmetric form — the bug site).
- `palace/linalg/iterative.cpp:411-411` — `initial_res = std::sqrt(std::abs(beta_rhs));` (the shared collapse line; second square root applied uniformly to both arms).
- `palace/linalg/iterative.cpp:395-397` — comparison-point: `beta = linalg::Dot(comm, z, r); ... res = std::sqrt(std::abs(beta));` — the symmetric one-`Dot`-one-`sqrt` form that the `!B` `initial_res` branch should have mirrored.
- `palace/linalg/iterative.cpp:417-417` — `eps = std::max(rel_tol * initial_res, abs_tol);` — the downstream consumer whose semantics is quirky-scaled in the `!B && initial_guess` case.
- `palace/linalg/vector.hpp:257-260` — `linalg::Norml2` definition (the mechanical cause).

Phase-1 evidence:

- `book/src/spec/slices/cg.md:20` — the slice's working-note seed that motivated this lift.

Firm theme (insertion target):

- `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B (theme lines 159-295); insertion after `CheckDot` Recognition note (theme line 265), `Citations:` rows append after existing final-state write-out citation (theme line 295).

OQ ledger:

- `scaffolding/open-questions.md:30` — `cg-initial-residual-quirk-palace-bug-flag-lift-path` (currently plan Backlog Low). After this lift lands, the OQ narrows to "upstream confirmation needed that the asymmetry is unintentional" — the lift annotation itself is no longer pending; only the upstream confirmation is. Integrator may either close the OQ (marking the lift complete with a narrower upstream-confirmation sub-OQ if desired) or leave it open with a status update to reflect the narrowed scope.

## Open questions / caveats

1. **Upstream-confirmation status of the bug classification.** The Recognition note calls this a "likely Palace bug" based on the analytic argument (the `B` arm's computation collapses to `‖b‖_B` and should equal `‖b‖₂` at `B == identity`; the `!B` arm produces `(b·b)^{1/4}` instead). This is a structural argument from algorithmic intent + cross-arm consistency, not an upstream-confirmed bug report. The annotation correctly hedges with "likely" and "upstream confirmation pending." A genuinely unintentional bug would expect the symmetric fix (replace `Norml2` with `Dot` at line 408); a deliberate-but-undocumented design choice (perhaps to dampen relative-tolerance convergence in cold-start cases?) would expect either a comment in source explaining the asymmetry (there is none) or a regression test pinning the behaviour (none found in `test/unit/`; CG is exercised only via integration tests per the `cg.md:23` test-coverage-gap working note). The narrowed OQ that remains is "file an upstream issue with Palace maintainers (or check git blame for the asymmetry's introduction commit) to confirm the bug-vs-intentional classification." This is out-of-scope for the project but should stay tracked.

2. **Downstream impact magnitude.** The annotation describes the quirk's structural effect but does not quantify the numerical impact on convergence iteration counts. For `‖b‖₂ ≈ 1`, the quirk is benign (`(b·b)^{1/4} ≈ 1` too); for `‖b‖₂ ≪ 1` (small RHS), the quirky `initial_res` is **larger** than the correct value, so `eps = rel_tol * initial_res` is artificially **looser**, causing earlier (less-strict) convergence than intended; for `‖b‖₂ ≫ 1` (large RHS), the quirky `initial_res` is **smaller**, so `eps` is artificially **tighter**, causing later (more-iterations) convergence. The asymmetry is bounded but not negligible across the RHS-magnitude axis. The annotation does not include this analysis (it would be inferential and not L0-anchored); a future cycle could add it as an extended note if useful, but the recognition rule itself is complete without it.

3. **GMRES/MINRES/BiCGStab analogues.** The annotation notes that `GmresSolver`'s `InitialResidual` helper (`iterative.cpp:252-285`) is **not** affected. I did not separately audit MINRES + BiCGStab for the same asymmetry, but both ship as `obstruction` themes in the firm artifact (`book/src/L1-L0/minres-iteration.md`, `bicgstab-iteration.md` — cycle-004; status `obstruction (enum-only-stub)` per the cycle-030 sub-kind codification), so the asymmetry question does not arise at the firm-theme level for those methods (the obstruction theme records the absence of an implementation, not its details). If MINRES/BiCGStab are ever promoted upstream, the audit would need to revisit their analogous `initial_res` computations.

4. **The annotation's "B == identity" framing is informal.** The argument that the two arms should agree at `B == identity` uses "identity" loosely — Palace's preconditioner-side null check is `if (B)`, where `B` is a `const Solver<OperType> *` pointer (null when no preconditioner is configured at the factory). There is no `B = identity Solver` path in normal Palace use — the `B` and `!B` branches are exhaustive over the configuration enum. So the "two arms should agree at the limit" framing is the **algorithmic-intent** argument, not a runtime-comparable claim. This is consistent with the Recognition note's hedging ("the symmetric form, by analogy with…") and does not weaken the bug classification, but a reader expecting a side-by-side runtime equality check should know the framing is intent-based, not behavioural.

## Direction-discipline note

This is an L1>L0 theme annotation, narrated **forward**: it documents how the L1 `ksp_solve` form's `result.initial_res` field lowers to the L0 source's `initial_res` `mutable`-member assignment, including the quirky branch. The recognition rule is a faithful reconstruction of what Palace actually does on the `!B && initial_guess` branch — it is **not** a status reduction of the firm theme (the theme stays `firm`; the laws on the L1 `ksp_solve` entry remain unmodified). The "likely Palace bug" flag is a **caveat on the recognition rule's relationship to algorithmic intent**, not a claim that the L0 form is incorrect to document. Negative-anchor sub-kind (per the cycle-012 `partly-constructive` invariant): N/A — this annotation does NOT use negative anchors to materialize a constructed sub-part; it documents an exact positive L0 site, just one whose semantics is algorithmically suspect. The whole edit is additive prose + two appended `Citations:` rows; no laws change, no signatures change, no operators are added, no status is downgraded.

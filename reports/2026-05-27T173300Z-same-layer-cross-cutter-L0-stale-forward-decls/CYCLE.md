---
agent: same-layer-cross-cutter
invoked_at: 2026-05-27T17:33:00Z
scope: L0 cross-cut — stale "Forward-declared" italic notes in 5 reference chapters (post-cycle-007 thinning sweep housekeeping)
status: integrated
integrated_at: 2026-05-27T18:35:15Z
integration_commit: PLACEHOLDER_SHA
integration_notes: cycle-008 pass 1 (wave-1). Housekeeping cleanup; 5 L0 files edited (stale forward-decl notes removed + 1 backlink added). Zero gate hits. No new OQs.
---

# CYCLE: L0 observation — 5 stale forward-declaration italic notes

## Summary

Five L0 reference chapters (`output-arg-vs-receiver`, `mfem-vector-types`, `linalg-free-functions`, `transparent-vs-load-bearing-tricks`, `apply-linop-overload-set`) contain italic forward-declaration notes inside their `Referenced from` blocks announcing that the cycle-006 retroactive-thinning sweep will populate inline-citation backlinks from the L1 operator pages. The cycle-007 thinning sweep (dispatch `2026-05-27T160553Z-layer-intro-author-L1-context-thinning-sweep`, integrated) has landed; the L1 `Context` paragraphs now contain the cross-references the L0 chapters were forward-declaring. The italic notes are now stale — they describe future work that has already happened. The actual `Referenced from` bullet lists below the italic notes are already accurate and need no change in 4 of the 5 chapters; the 5th (`apply-linop-overload-set.md`) needs one new bullet for `L1/ksp_solve` added in cycle-007.

## Observation kind

**Redundancy** (degenerate form — a self-deprecating annotation that no longer applies). Not a unification candidate, contradiction, or shared sub-pattern; just five identical stale notices waiting to be retired.

## Specific finding

Five L0 chapters carry the stale italic note:

| File | Line | Note (paraphrased) |
|---|---|---|
| `book/src/L0/output-arg-vs-receiver.md` | 36 | `*Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-006 retroactive-thinning sweep (priority #11).*` |
| `book/src/L0/mfem-vector-types.md` | 42 | (identical text) |
| `book/src/L0/linalg-free-functions.md` | 47 | (identical text) |
| `book/src/L0/transparent-vs-load-bearing-tricks.md` | 34 | (identical text) |
| `book/src/L0/apply-linop-overload-set.md` | 55 | `*The L1 / L1>L0 entries below already cite this overload set inline. The retroactive-thinning sweep (priority #11) will replace those inline citations with backlinks here.*` |

The cycle-007 sweep added cross-references from the L1 chapters to each of these L0 reference chapters per the matrix at `reports/2026-05-27T160553Z-layer-intro-author-L1-context-thinning-sweep/CYCLE.md:244` (the "L1 operator × L0 reference" table). Concrete back-reference targets confirmed by `grep` over `book/src/L1/*.md`:

- `output-arg-vs-receiver` ← cited from `L1/axpy.md:7`, `L1/axpby.md:7`, `L1/axpbypcz.md:7`, `L1/scal.md:7`, `L1/apply_linop.md:7` (5 L1 operators).
- `mfem-vector-types` ← cited from `L1/axpy.md:7`, `L1/axpby.md:7`, `L1/axpbypcz.md:7`, `L1/scal.md:7`, `L1/dot.md:7`, `L1/nrm2.md:7`, `L1/apply_linop.md:7` (7 L1 operators).
- `linalg-free-functions` ← cited from `L1/axpy.md:7`, `L1/axpby.md:7`, `L1/axpbypcz.md:7`, `L1/dot.md:7`, `L1/nrm2.md:7`, `L1/scal.md:7` (6 L1 operators; `apply_linop` deliberately not — deliberate omission per cycle-007 open-question #4).
- `transparent-vs-load-bearing-tricks` ← cited from `L1/axpy.md:7`, `L1/scal.md:7`, `L1/dot.md:7`, `L1/nrm2.md:7`, `L1/axpby.md:7`, `L1/axpbypcz.md:7`, `L1/apply_linop.md:7` (7 L1 operators).
- `apply-linop-overload-set` ← cited from `L1/apply_linop.md:7` and `L1/ksp_solve.md:7, 137` (2 L1 operators; `ksp_solve` back-reference is new and not yet in the existing `Referenced from` list at lines 57-62).

**For 4 of the 5 chapters** (`output-arg-vs-receiver`, `mfem-vector-types`, `linalg-free-functions`, `transparent-vs-load-bearing-tricks`), the `Referenced from` bullet list immediately under the stale italic note already enumerates exactly the right L1 operators. The bullet lists were authored in cycle-005/006 with the planned sweep in mind (per cycle-007 sweep report line 254). The italic note is the only stale element.

**For the 5th chapter** (`apply-linop-overload-set.md`), the existing `Referenced from` list (lines 57-62) names `L1/apply_linop`, `L1-L0/apply-linop-mutation-rotation`, `concepts/constructed-operators`, `concepts/complex-from-real-lift`, `L0/ksp-factory-file`, `L0/kspsolver-base-class`. It does NOT name `L1/ksp_solve` — but `L1/ksp_solve.md:7` and `L1/ksp_solve.md:137` now back-reference this L0 chapter (the cycle-006 `ksp_solve` author wired in the cross-reference because the iterative solvers dispatch into the `Mult` overload family per step). One new bullet for `L1/ksp_solve` is needed alongside removing the stale italic note.

## Recommendation

**Defer methodology/follow-up dispatches** — direct application via integrator-per-report is sufficient. The 5 edits are mechanical (remove a one-line italic note in 4 files; remove an italic note + add a bullet in the 5th). No follow-up combinator-miner / harvester / layer-intro-author dispatch is warranted.

**Flag (not dispatch) a candidate convention**: a future L0 reference chapter is born "forward-declared" (its backlinks point into L1 chapters that don't yet cite it), and the integrator-finalize step or a future layer-intro-author dispatch should rewrite the italic note once the backlinks are wired. The current ad-hoc approach (author writes a stale prophetic note; same-layer-cross-cutter retires it later) works for 5 chapters but would be tedious at 50. A shared template ("Referenced from" sections start with a `**Status**: forward-declared / wired` line that gets flipped during integration) is **not worth a dispatch yet** — wait until at least one more L0/L1 sweep cycle generates the same pattern (skill-candidates entry not yet warranted; cycle-009+ if it recurs).

## Proposed changes

### Change 1 — `book/src/L0/output-arg-vs-receiver.md`

Remove the stale italic line (line 36) and the blank line above it; preserve the `## Referenced from` heading and the bullet list below.

```edit
file: book/src/L0/output-arg-vs-receiver.md
old:
## Referenced from

*Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-006 retroactive-thinning sweep (priority #11).*

- [`L1/axpy`](../L1/axpy.md) — receiver `y.Add(α, x)` vs output-arg `linalg::AXPY(α, x, y)`.
new:
## Referenced from

- [`L1/axpy`](../L1/axpy.md) — receiver `y.Add(α, x)` vs output-arg `linalg::AXPY(α, x, y)`.
```

### Change 2 — `book/src/L0/mfem-vector-types.md`

Remove the stale italic line (line 42) and the blank line above it; preserve the bullet list.

```edit
file: book/src/L0/mfem-vector-types.md
old:
## Referenced from

*Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-006 retroactive-thinning sweep (priority #11).*

- [`L1/axpy`](../L1/axpy.md), [`L1/axpby`](../L1/axpby.md), [`L1/axpbypcz`](../L1/axpbypcz.md), [`L1/scal`](../L1/scal.md) — element-type axis collapse.
new:
## Referenced from

- [`L1/axpy`](../L1/axpy.md), [`L1/axpby`](../L1/axpby.md), [`L1/axpbypcz`](../L1/axpbypcz.md), [`L1/scal`](../L1/scal.md) — element-type axis collapse.
```

### Change 3 — `book/src/L0/linalg-free-functions.md`

Remove the stale italic line (line 47) and the blank line above it; preserve the bullet list.

```edit
file: book/src/L0/linalg-free-functions.md
old:
## Referenced from

*Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-006 retroactive-thinning sweep (priority #11).*

- [`L1/axpy`](../L1/axpy.md), [`L1/axpby`](../L1/axpby.md), [`L1/axpbypcz`](../L1/axpbypcz.md) — `linalg::AXPY` / `linalg::AXPBY` / `linalg::AXPBYPCZ` free-function-template wrappers over method-form.
new:
## Referenced from

- [`L1/axpy`](../L1/axpy.md), [`L1/axpby`](../L1/axpby.md), [`L1/axpbypcz`](../L1/axpbypcz.md) — `linalg::AXPY` / `linalg::AXPBY` / `linalg::AXPBYPCZ` free-function-template wrappers over method-form.
```

### Change 4 — `book/src/L0/transparent-vs-load-bearing-tricks.md`

Remove the stale italic line (line 34) and the blank line above it; preserve the bullet list.

```edit
file: book/src/L0/transparent-vs-load-bearing-tricks.md
old:
## Referenced from

*Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-006 retroactive-thinning sweep (priority #11).*

- [`L1/axpy`](../L1/axpy.md) — `α == 1.0` fast path (transparent).
new:
## Referenced from

- [`L1/axpy`](../L1/axpy.md) — `α == 1.0` fast path (transparent).
```

### Change 5 — `book/src/L0/apply-linop-overload-set.md`

Remove the stale italic line (line 55); add a new bullet for `L1/ksp_solve` (per cycle-006 author's wired back-reference).

```edit
file: book/src/L0/apply-linop-overload-set.md
old:
## Referenced from

*The L1 / L1>L0 entries below already cite this overload set inline. The retroactive-thinning sweep (priority #11) will replace those inline citations with backlinks here.*

- [`L1/apply_linop`](../L1/apply_linop.md) — collapses the entire overload set to one operator parameterised by element type.
- [`L1-L0/apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md) — the L1>L0 lowering theme that reintroduces the destination-buffer mention and selects between the `Mult` and `AddMult` forms per sub-pattern.
- [`concepts/constructed-operators`](../concepts/constructed-operators.md) — narrative for the `BaseProductOperator` / `SumOperator` family.
- [`concepts/complex-from-real-lift`](../concepts/complex-from-real-lift.md) — narrative for the `ComplexWrapperOperator` real-imag block formulation.
- [`L0/ksp-factory-file`](./ksp-factory-file.md) — uses `Operator` / `ComplexOperator` as the `OperType` template parameter throughout the KSP construction surface.
- [`L0/kspsolver-base-class`](./kspsolver-base-class.md) — the `BaseKspSolver<OperType>` wraps an operator of this hierarchy and exposes a `Mult` of the same interface shape.
new:
## Referenced from

- [`L1/apply_linop`](../L1/apply_linop.md) — collapses the entire overload set to one operator parameterised by element type.
- [`L1/ksp_solve`](../L1/ksp_solve.md) — the iterative solvers dispatch into the `Mult` family per step (cited in the `ksp_solve` Context and Evidence sections).
- [`L1-L0/apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md) — the L1>L0 lowering theme that reintroduces the destination-buffer mention and selects between the `Mult` and `AddMult` forms per sub-pattern.
- [`concepts/constructed-operators`](../concepts/constructed-operators.md) — narrative for the `BaseProductOperator` / `SumOperator` family.
- [`concepts/complex-from-real-lift`](../concepts/complex-from-real-lift.md) — narrative for the `ComplexWrapperOperator` real-imag block formulation.
- [`L0/ksp-factory-file`](./ksp-factory-file.md) — uses `Operator` / `ComplexOperator` as the `OperType` template parameter throughout the KSP construction surface.
- [`L0/kspsolver-base-class`](./kspsolver-base-class.md) — the `BaseKspSolver<OperType>` wraps an operator of this hierarchy and exposes a `Mult` of the same interface shape.
```

## Supporting evidence

- `book/src/L0/output-arg-vs-receiver.md:34-42` — stale forward-decl note + accurate bullet list.
- `book/src/L0/mfem-vector-types.md:40-46` — same shape.
- `book/src/L0/linalg-free-functions.md:45-52` — same shape.
- `book/src/L0/transparent-vs-load-bearing-tricks.md:32-42` — same shape.
- `book/src/L0/apply-linop-overload-set.md:53-62` — variant note text + 6-bullet list (missing `L1/ksp_solve`).
- `book/src/L1/axpy.md:7` — Context paragraph citing `L0/output-arg-vs-receiver`, `L0/mfem-vector-types`, `L0/transparent-vs-load-bearing-tricks`.
- `book/src/L1/axpby.md:7` — Context paragraph citing `L0/output-arg-vs-receiver`, `L0/linalg-free-functions`, `L0/mfem-vector-types`, `L0/transparent-vs-load-bearing-tricks`.
- `book/src/L1/axpbypcz.md:7` — Context paragraph citing the same 4 L0 chapters.
- `book/src/L1/scal.md:7` — Context paragraph citing `L0/linalg-free-functions`, `L0/output-arg-vs-receiver`, `L0/mfem-vector-types`, `L0/transparent-vs-load-bearing-tricks`.
- `book/src/L1/dot.md:7` — Context paragraph citing `L0/linalg-free-functions`, `L0/mfem-vector-types`, `L0/transparent-vs-load-bearing-tricks`.
- `book/src/L1/nrm2.md:7` — Context paragraph citing `L0/linalg-free-functions`, `L0/mfem-vector-types`, `L0/transparent-vs-load-bearing-tricks`.
- `book/src/L1/apply_linop.md:7` — Context paragraph citing `L0/apply-linop-overload-set`, `L0/output-arg-vs-receiver`, `L0/mfem-vector-types`, `L0/transparent-vs-load-bearing-tricks`.
- `book/src/L1/ksp_solve.md:7, 137` — Context paragraph + Evidence section citing `L0/apply-linop-overload-set` (the new back-reference target).
- `reports/2026-05-27T160553Z-layer-intro-author-L1-context-thinning-sweep/CYCLE.md:244` — the operator × L0-reference matrix; line 256-260 explicitly flags the 5 stale forward-decls for this follow-up dispatch.

## Open questions / caveats

- None of the 5 forward-declarations are obsolete-but-misleading (i.e., no L0 chapter's promised back-reference failed to materialize). The cycle-007 sweep delivered on every promise made by the cycle-005/006 bullet lists; the only outstanding discrepancy is the missing `L1/ksp_solve` bullet in `apply-linop-overload-set.md` (Change 5 adds it).
- The integrator should NOT re-run the citation-validity gate over the bullet lists in the 4 untouched chapters — those bullets are unchanged. The new bullet in Change 5 cites `../L1/ksp_solve.md` (existing file) with no source-range claim, so no citation check applies.
- The candidate "Referenced from status convention" mentioned in Recommendation is **not** filed as a skill-candidate or open-question in this dispatch — observation-only flag, deferred until pattern recurs. If a cycle-009+ same-layer-cross-cutter dispatch observes the same shape again, that's the trigger to promote.
- mdBook will rebuild cleanly after Change 5 because the new `[L1/ksp_solve](../L1/ksp_solve.md)` link target already exists in the SUMMARY.md / file tree (the chapter has been firm since cycle-006).

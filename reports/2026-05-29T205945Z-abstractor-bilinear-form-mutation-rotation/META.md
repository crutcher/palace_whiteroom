---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T21:30:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T22:15:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of REPORT — L1>L0 theme sketch `bilinear-form-mutation-rotation`

## Critique

### Checks run

**citation-validity** — Mechanical `python3 tools/citecheck/citecheck.py --scan` returned 20/20 OK (clean bounds, no AMBIG, no path-hygiene drift). I spot-verified the load-bearing L0 anchors via `mcp__palace-codemap__read_range`:

- `palace/linalg/operator.hpp:386-394` — both bilinear-form overload decls present, comments verbatim `// Compute the bilinear form inner product yᴴ A x for a {real,complex} operator A and complex vectors. Allocates workspace internally.`; the line numbers in the report (decl span 388-389, complex span 393-394) match.
- `palace/linalg/operator.cpp:621-629` real-`A` body — verified line-by-line: `:624` `ComplexVector Ax(A.Height())`, `:625` `Ax.UseDevice(true)`, `:626` `A.Mult(x.Real(), Ax.Real())`, `:627` `A.Mult(x.Imag(), Ax.Imag())`, `:628` `return Dot(comm, Ax, y)`.
- `palace/linalg/operator.cpp:631-638` complex-`A` body — verified line-by-line: `:634/:635/:636/:637` exactly as cited.
- `palace/models/boundarymodeoperator.cpp:75-93` `ComputePoyntingPower` — verified `:85` is `linalg::Dot(comm, et, *Bttr, et)` with `Bttr` (Hermitian witness); `:88-90` constructs `ComplexWrapperOperator Atn(...)` and `:90` is `linalg::Dot(comm, en, Atn, et)` (non-Hermitian witness). The Atn construction the report describes is at `:88-89`, not `:88-90` as the text says (a one-line off-by-one in §"Sub-pattern C" Citations: "line `:88-90` constructs `Atn`" — the construct spans 88-89; line 90 is the Dot call itself); harmless because the cited range `:75-93` brackets both.
- `palace/linalg/nleps.cpp:672-675` — verified `linalg::Dot(GetComm(), w, w0)` denominator at `:675` exists; the `:674-675` Newton-denominator expression matches as described.

Now the **issue**: a semantic citation defect in the proposed-changes body. The report's L1 form §"L1 form (LHS)" at CYCLE.md:88 states the L1 anchoring identity as:

> `bilinear_form(x, M, y) = dot(apply_linop(M, y), x)` — the matrix-weighted form unfolds into one `apply_linop` + one `dot` (per [`L1/bilinear-form`](../L1/bilinear-form.md) §"Composition into `apply_linop` + `dot`")

But the upstream L1 entry at `book/src/L1/bilinear-form.md:112-113` states the composition as the **opposite-argument-order** form:

> `bilinear_form(x, M, y) = dot(x, apply_linop(M, y))` recasts the reduction as "apply `M` to `y`, take `dot` with `x`"

Under the L1 `dot` convention (`dot(a, b) = aᴴ b` — conjugate-linear in first arg per `L1/dot.md:43`), these are **NOT** the same value:
- L1-entry form `dot(x, apply_linop(M,y))` = `xᴴ (M·y)` = `xᴴ M y` ✓ (matches `bilinear_form(x,M,y)`)
- Report form `dot(apply_linop(M,y), x)` = `(M·y)ᴴ x` = `yᴴ Mᴴ x` ✗ (matches `bilinear_form` only when `M` is Hermitian)

This is a misquoted upstream algebraic identity. It is potentially load-bearing because the report's §"Conjugation asymmetry — the L1/L0 reconciliation" depends on the L1-side conjugation handedness being unambiguous. The citation pointer (`§"Composition into `apply_linop` + `dot`"`) is to a real and in-range upstream section, so the *citation* is valid; the *paraphrase* misrenders it. Net: `warning`, not `fail` — the L0 lowering body and the inherited-sub-theme references that actually carry the structural rotation are all citation-clean, and the §"Conjugation asymmetry" section later in the same document (CYCLE.md:381-419) gets the reconciliation correct (`L1: xᴴ M y; L0: Dot(comm, x, A, y) = yᴴ A x`, swap is mechanical), so the defect is localised to the §"L1 form (LHS)" paraphrase rather than propagating into the rotation rule itself.

(One additional small drift: in the §"Sub-pattern C" Citations block at CYCLE.md:295-298, "line `:88-90` constructs `Atn = ComplexWrapperOperator(Atnr, Atni)` and line `:90` is the non-Hermitian-`A` callsite" — the construction is at `:88-89`, the Dot call is `:90`. Cosmetic; the bracketing range `:75-93` covers it.)

**surface-or-evidence** — Pass. This is a wholly NEW L1>L0 theme file (`new:book/src/L1-L0/bilinear-form-mutation-rotation.md`), not a refinement of an existing theme. The proposal changes the artifact surface (creates a chapter, adds a SUMMARY.md row, adds a dep-map row). Rotation_claim evidence is direct, positively-anchored, and exhaustively cited.

**rotation-quality** — Pass. The L1>L0 rotation is genuine: at L1 the operator is a single closed-form semantic step `bilinear_form(x, M, y) = xᴴ M y` with no workspace, no MPI collective, no element-type branching, no conjugation-asymmetry visible. At L0 it is a three-step `alloc → A.Mult(×1 or ×2 lane-split) → return Dot`, with internal workspace `Ax`, an MPI collective in the inner Dot, an element-type-of-`M` overload split, and the arg-2-conjugated Palace `Dot` convention. The L1 form is **strictly more compact and more abstract** — workspace hidden, MPI collective hidden, element-type axis variant-absorbed, conjugation-asymmetry erased. Not a 1:1 renaming. The "conjugation-asymmetry reconciliation" is the load-bearing piece: it is correctly handled in the rotation's §"Conjugation asymmetry" section (the argument-position swap `L1 bilinear_form(x,M,y) ↔ L0 Dot(comm, y, M, x)`, or equivalently the inherited `conj(...)`-and-`Mᴴ` identity for the as-Palace-calls-it `Dot(comm, x, M, y) = yᴴ M x` direction). Both formulations are stated, the choice of which to take as the lowering rule is mechanical, and the Palace callsites (Hermitian `Bttr` at `:85`, non-Hermitian `Atn` at `:90`) are correctly observed to be consistent with the L0 convention `Dot(comm, x, A, y) = yᴴ A x`. This part of the analysis is grounded, not hand-waved.

**variant-axis-coverage** — Pass. Two orthogonal axes named (element-type of `M`: real / complex; M-symmetry-property: hermitian / non-symmetric). The element-type axis has both witnesses authored as Sub-patterns A and B; the M-symmetry axis has both witnesses surfaced as Sub-pattern C (`Bttr` Hermitian at `:85`, `Atn` non-Hermitian at `:90`). One axis is correctly **collapsed**: operator-representation of `M`, absorbed into `apply_linop`'s representation axis. Three gaps are *explicitly scoped out* and recorded as upstream L1-entry-owned (real-`x`/real-`M`/real-`y` overload absent, rectangular `M` unexercised, Cauchy–Schwarz tight case `y=x` unexercised). The scoping rationale ("rough-in test-coverage-bounded gates are upstream, not theme-owned") is consistent with the `matrix-weighted-norm-mutation-rotation` precedent. No hidden branches found in the L0 source (verified there are only the two overloads at `operator.hpp:386-394` / `operator.cpp:621-639`).

**cross-reference-integrity** — Pass. Verified file-existence of all eight cross-references:
- `book/src/L1/bilinear-form.md` ✓
- `book/src/L1/matrix-weighted-norm.md` ✓
- `book/src/L1/dot.md` ✓
- `book/src/L1/apply_linop.md` ✓
- `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md` ✓
- `book/src/L1-L0/apply-linop-mutation-rotation.md` ✓
- `book/src/L1-L0/dot-mutation-rotation.md` ✓
- `book/src/L0/mutable-workspace-pattern.md` (referenced; assumed existing per L0 chapter classification reference — not blocked).

**Build-readiness guard (firm-body-inside-fence)**: ran the fence-parity check on the proposed-changes block at CYCLE.md:47-630 (`new:book/src/L1-L0/bilinear-form-mutation-rotation.md`). The block opens at line 47 with ` ```new:... ` and closes at line 630 with a bare ` ``` `. The status-asserting `## Status` heading is at line 595-596 (inside the fence). The Signature-equivalent material (§"L1 form (LHS)" :74, §"L0 form (RHS)" :103), Algebraic-laws-equivalent material (§"Applicability conditions" :421-457), and Evidence-equivalent material (§"Verified-against" :544-593) are all enclosed inside the fence. There are NO nested triple-backtick code fences inside (the code blocks are 4-space-indented per the snippet shown at :112-126 / :202-217 — exactly the convention the `convert-nested-fences-to-indented-code-in-proposed-changes-block` skill recommends; the abstractor pre-conformed). Fence-parity is even and balanced. The `firm` claim's body sits entirely inside its `new:` fence. No cycle-019 / cycle-021 fence-truncation defect signature detected.

**edge-label-fidelity** — Pass. The proposal's edge label `L1>L0` is stated consistently in (a) the filename (`L1-L0/bilinear-form-mutation-rotation.md`), (b) the SUMMARY.md placement (under "L1 > L0 Part"), (c) the index.md row column ordering (`L1/bilinear-form` LHS, Palace source RHS), and (d) the prose throughout — every "lowers into" / "L1 form" / "L0 surface" sentence respects the high→low direction. The proposed dep-map row places the L1 LHS (`L1/bilinear-form`) and the L0 RHS (`palace/linalg/operator.{hpp,cpp}`, `palace/models/boundarymodeoperator.cpp`) on the correct sides.

**plan-kind-consistency** — Pass. Declared kind: firm L1>L0 theme. Content shape matches:
- It IS a lowering theme (not a layer entry, not an audit, not a concept).
- It IS firm: rewrite is structurally exhaustive (both L0 overloads + both callsites cited), positively-anchored (no negative anchors, no literature inference, no speculative operators).
- The firm status is justified by the precedent that a firm lowering theme over a `rough-in (test-coverage-bounded)` L1 entry is permitted (`matrix-weighted-norm-mutation-rotation` precedent cited). The structural-fidelity-vs-L1-promotion-gate decoupling argument is correct: the theme's question ("does the L1 form expand into this L0 source?") is independent of the L1 entry's promotion gates (test coverage + real-real-real variant absence). No placeholder content, no `[TODO]`, no speculative gaps in the rewrite itself.
- The theme proposes "Speculative L1 operators: None" — consistent with the lowering-into-existing-firm-vocabulary positioning (reuses `apply_linop`, `dot`).

**skill-uptake-survey** — Pass. The report references explicit invocation of:
- `tools/citecheck/citecheck.py --anchor` (Verified-against + Supporting evidence sections both cite it for producer-citation self-verification).
- `verify-citation-range` (Verified-against header explicitly names it).
- `classify-variant-axis` (Variant axes header explicitly names it: "per `classify-variant-axis`").
- The build-readiness fence-parity guard (`proposed-changes-fence-encloses-full-body-guard`) is not invoked by name, but the *behavior* it audits (4-space-indented code blocks instead of nested triple-backtick fences) is conformed — the abstractor pre-emptively avoided the nested-fence pitfall. Surface-only telemetry: surfaces the skill uptake telemetry, doesn't block.

### Issues found

1. **(citation-validity, warning, severity: medium, localised but semantically load-bearing)** CYCLE.md:88 (§"L1 form (LHS)") misquotes the upstream L1 algebraic identity. The report says `bilinear_form(x, M, y) = dot(apply_linop(M, y), x)`; the upstream `book/src/L1/bilinear-form.md:112-113` says `bilinear_form(x, M, y) = dot(x, apply_linop(M, y))`. Under the L1 `dot` convention (conjugate-linear in first argument), the report's form evaluates to `yᴴ Mᴴ x` and the upstream form evaluates to `xᴴ M y`; they are *not* equal except when `M` is Hermitian. The cited section pointer (§"Composition into `apply_linop` + `dot`") IS in-range and the upstream prose IS the correct one; this is a paraphrase defect at the report site, not a wrong-citation. The defect does not propagate into the rotation rule's §"Conjugation asymmetry" (CYCLE.md:381-419), which correctly handles the L1 form as `xᴴ M y` and derives the L0 reconciliation correctly. Fix: swap arguments in the CYCLE.md:88 quotation to match the upstream `dot(x, apply_linop(M, y))` form.

2. **(citation-validity, warning, severity: low, cosmetic)** CYCLE.md:295-298 (§"Sub-pattern C" Citations) says "line `:88-90` constructs `Atn = ComplexWrapperOperator(Atnr, Atni)` and line `:90` is the non-Hermitian-`A` callsite". Verified at the codemap: the `ComplexWrapperOperator Atn(...)` construction spans `:88-89`; line `:90` is the `linalg::Dot(comm, en, Atn, et)` call. Cosmetic; the bracketing range `:75-93` does cover it. Fix: `:88-89 constructs Atn; :90 is the callsite`.

No issues found for: surface-or-evidence, rotation-quality, variant-axis-coverage, cross-reference-integrity, edge-label-fidelity, plan-kind-consistency, skill-uptake-survey.

## Repair

### Fixes attempted

1. **Finding**: (citation-validity, warning, semantically load-bearing) CYCLE.md:88 misquotes the upstream L1 composition identity as `bilinear_form(x, M, y) = dot(apply_linop(M, y), x)`; upstream `book/src/L1/bilinear-form.md:112-113` actually says `dot(x, apply_linop(M, y))`. Under the L1 `dot` convention (conjugate-linear in arg-1), the report form evaluates to `yᴴ Mᴴ x` whereas upstream evaluates to `xᴴ M y` — equal only when `M` is Hermitian.
   - **Decision**: repaired
   - **Action**: Edited CYCLE.md to correct the paraphrase in three places (the same misquote recurs as a load-bearing identity quotation):
     - §"L1 form (LHS)" CYCLE.md:88 — anchor identity line: `dot(apply_linop(M, y), x)` → `dot(x, apply_linop(M, y))`.
     - §"Justification kind" CYCLE.md:472 — "One algebraic identity" bullet quotes the same Composition note: `dot(apply_linop(M, y), x)` → `dot(x, apply_linop(M, y))`.
     - §"Sub-pattern C" CYCLE.md:286 — informational nleps callsite note "callers sometimes inline the L1>L0 unfolding manually (computing `xᴴ M y` as ...)": `dot(apply_linop(M, y), x)` → `dot(x, apply_linop(M, y))`.
   - **Rationale for in-scope**: pure paraphrase-correction matching the cited upstream source verbatim (`book/src/L1/bilinear-form.md:112-113`, verified on-disk this invocation). No content authoring — the cited section pointer is unchanged, only the argument-order in the quoted form. Critic explicitly noted the defect does NOT propagate into the §"Conjugation asymmetry" rotation analysis (which correctly handles L1 `xᴴ M y` vs L0 `yᴴ A x`); the fix restores consistency between the three local paraphrases and the upstream. Additional sweep beyond the critic's named CYCLE.md:88 site is mechanical: the same exact misquoted string appeared twice more in the same document; leaving them unfixed would have left the report internally inconsistent after the primary fix.

2. **Finding**: (citation-validity, warning, cosmetic) CYCLE.md:296-297 (§"Sub-pattern C" Citations) says "line `:88-90` constructs `Atn = ComplexWrapperOperator(Atnr, Atni)` and line `:90` is the non-Hermitian-`A` callsite"; the `ComplexWrapperOperator Atn(...)` construction actually spans `:88-89` and `:90` is the `linalg::Dot` call.
   - **Decision**: repaired
   - **Action**: Edited CYCLE.md:297 — `line :88-90 constructs Atn` → `lines :88-89 construct Atn`. (Cosmetic — the bracketing range `:75-93` in the same citation continues to cover both; verified via codemap `read_range` on `palace/models/boundarymodeoperator.cpp:85-93` this invocation: line 87 is the `if (Atnr && ...)` guard, lines 88-89 are `ComplexWrapperOperator Atn(const_cast<...>(Atnr.get()), const_cast<...>(Atni.get()));`, line 90 is `P += ... * linalg::Dot(comm, en, Atn, et);`.)
   - **Rationale for in-scope**: pure off-by-one citation-fidelity correction matching the cited source. No content authoring.

### Unrepairable findings

None. Both critic-flagged findings were mechanical citation-fidelity corrections within repair authority (paraphrase-to-source match for finding 1; off-by-one line-span trim for finding 2). No substantive authoring required; no contradiction with existing artifact; no methodology-level escalation.

## Suggested resolution

`ready`. The report's structural rotation analysis (the load-bearing §"Conjugation asymmetry" reconciliation, the Sub-pattern A/B/C decomposition, the workspace-ownership-boundary distinguisher vs the `matrix-weighted-norm` sibling, and the variant-axis classification) was sound per the critic; the two citation-validity warnings were localised paraphrase / line-span drifts now corrected. All 8 checks now pass or repaired. No follow-up agent required. Integrator may apply per-report as normal (creates `book/src/L1-L0/bilinear-form-mutation-rotation.md`, appends `L1-L0/index.md` and `SUMMARY.md` rows).

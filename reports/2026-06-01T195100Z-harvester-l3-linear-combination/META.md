---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T20:05:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-01T20:18:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize linear_combination at L3" (cycle-050 D1)

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` on the report: 18 ok, 0 failing (bounds + path-hygiene clean). Then verified the load-bearing inherited L0 pinpoints against live Palace source via codemap `read_range`:
- `palace/linalg/vector.cpp:702-712` — `AXPY(double, Vector, Vector)` with the `alpha == 1.0` fast-path (`y += x` else `y.Add(alpha, x)`). Exact match for the "arity-2-coeff-1 `axpy` leaf" claim.
- `palace/linalg/vector.cpp:726-730` — `AXPBY(double, Vector, double, Vector)` → `add(alpha, x, beta, y, y)`. Exact match for the "arity-2 fusion witness / single aligned in-place linear-combine" claim.
- `palace/linalg/vector.cpp:745-758` — `AXPBYPCZ` real-real body; `if (gamma == 0.0) { add(alpha, x, beta, y, z); }` sits at `:749-751`. Exact match for law-5 (zero-coefficient term-drop) and the `:749-751` sub-pinpoint.
- `palace/linalg/vector.hpp:305-316` — the three free-function template decls `AXPY`/`AXPBY`/`AXPBYPCZ` with the documented `y += alpha*x` / `y = alpha*x + beta*y` / `z = alpha*x + beta*y + gamma*z` comments. Exact match.
The inheritance-not-re-localization framing is honest: every L0 range the report cites is present verbatim in the firm L2 entry's §Evidence (`book/src/L2/linear_combination.md:344-373`, each marked "Self-verified"), and the report fabricates **no** new L0 claim — it adds no source range the L2 entry did not already self-verify. The `nleps.cpp:343-344` / `romoperator.cpp:188-189` γ=1 accumulate-into sites are likewise carried from the L2 entry's variant-axis section (`:251-253`). The `verified_against:` YAML round-trip sub-check is not applicable (this is a harvester report, no `verified_against:` block emitted).

**surface-or-evidence — pass.** Not a refinement of an existing entry: this is a `new:` operator entry (`book/src/L3/linear_combination.md` does not exist on disk — confirmed). The accompanying `edit:` blocks touch the L3 index dep-map (own-row append) and SUMMARY.md (chapter registration) — surface additions wiring the new entry in, not modifications to other entries' claims. The propagate-half / replace-and-propagate framing is correctly an in-layer rendering grounded in the firm L2 combinator + the firm `L3/axpy.md` cohort precedent, not a fresh-evidence claim. No bare rotation_claim without surface.

**rotation-quality — pass (with a noted nuance).** The report's central rotation claim is **identity-in-form** across the L3>L2 edge (the L3 fold is value-thread-isomorphic to the L2 fold), which it states explicitly and repeatedly (§Context, §"Downward to L2", §"L3 vs L2 distinction"). This is the licensed identity-lowering shape under the "Identity-lowerings still require both L levels" invariant, NOT a claimed compaction rotation — so the "must be strictly more compact" bar does not apply (an identity-in-form L3↔L2 edge is the precedent shape for the whole BLAS-1 cohort, `L3/axpy.md`, `L3-L2/axpy-body-identity.md:3-14`). The *substantive* rotation in the chain is correctly attributed downward to the L2>L1 `linear-combination-fold-specialization` fusion-selection theme (length→maximal-fused-leaf de-fusion), which the entry references rather than restating. The one genuine compaction this entry does perform — the **arity** unification (four fixed-arity leaves → one variadic fold) — is the L2 combinator's, carried up; the report is careful to call arity "the unification axis, not a remaining variant," which is the correct framing. No renaming-only / 1:1 smell.

**variant-axis-coverage — pass.** The variant axes are enumerated and each is dispositioned: **arity** (the unification axis, explicitly not a remaining variant — recovered as term-list length); **output-aliasing** (in-place vs out-of-place — explicitly scoped out of the L3 algebra as an L3>L2>L1 lowering concern, pure/out-of-place at L3, with the γ=1 accumulate-into sites cited); **element-type** (real|complex with the `real ⊑ complex` scalar-promotion sub-axis, inherited unchanged incl. its open `scalar-promotion-typing-rule` upstream OQ); **fusion-order** (explicitly an L0 implementation detail, NOT an L3 axis, routed to the L2>L1 theme). No hidden branches — the axis profile matches the firm L2 entry's `:240-267` one-for-one. (Skill `classify-variant-axis` not invoked, but the coverage is complete; see skill-uptake note.)

**cross-reference-integrity — pass.** All live `[link]` targets resolve on disk: `../L2/linear_combination.md`, `../concepts/scalar-promotion.md`, `../concepts/tensor-field-lift.md`, `../concepts/sequential-obstruction.md`, `../L2-L1/linear-combination-fold-specialization.md`, `../L3-L2/axpy-body-identity.md`, `./scal.md`, `./axpy.md`, `./axpby.md`, `./axpbypcz.md`, `./krylov-step.md` (all verified present). The `inner_product` reference is correctly **plain-text inline-code, not a live link** — `book/src/L3/inner_product.md` is absent on disk (confirmed), and `book/src/L3/index.md:29` carries it as a `rough-in (no anchor yet)` row; a live link would be a hard `linkcheck2` error, so plain-text is the build-safe form per the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention. Build-readiness fence guard: enumerated all fences (`grep -n '```'`) — `new:` block 23→198 (with two balanced nested `text` fences 57/60 + 77/82 inside), `edit:index` 200→207, `edit:SUMMARY` 209→216; even parity, balanced nesting. The firm apparatus (`# linear_combination` :39, `## Signature` :55, `## Semantics` :86, `## Algebraic laws` :102, `## Status` :171, `## Evidence` :179) is **fully INSIDE** the `new:` fence — no cycle-019 fence-truncation defect. The SUMMARY edit OLD/NEW (`- [scal](./L3/scal.md)` → +`- [linear_combination]...`) matches SUMMARY.md:34 exactly; the index edit OLD matches `L3/index.md:30` exactly.

**edge-label-fidelity — pass.** The entry carries the L3>L2 edge label (§"Downward to L2", `lowers_to:` frontmatter). The prose at that edge discusses exactly the L3→L2 relationship (value-thread-isomorphic fold body, identity-in-form, the four `*-body-identity` themes' demotion target). The downward L2>L1 attribution and the transitive L3>L1 in-line annotation are both correctly labeled (no `L3-L1/` directory, per the cycle-012 non-adjacent-identity convention). No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind is `firm` operator. The content shape matches a firm entry: full signature + shape contract, seven stated algebraic laws (each a syntactic identity or standard linear-combination fact carried from the firm L2 combinator), a §Status that justifies firm-without-dedicated-test via the inherited L2 caveat + the `chebyshev`-precedent bar, and a closed variant-axis profile. No rough-in placeholders inside the firm body. The "no sequential obstruction" claim is justified: the fold is over a finite, statically-known term list (typically length 1–3), each step element-local in `N` with no loop-carried recurrence over the field axis — matching the obstruction-free BLAS-1-leaf profile (`L3/axpy.md:58`), correctly distinguished from a fold-over-a-trajectory. The §"Iteration-rotation marker" honestly records that the iteration view lives at *consuming* compositions (`krylov-step`'s basis-correction sum), not at the fold itself. Dual-registration is correctly handled: D1 added ONLY its own `L3/index.md` dep-map row and explicitly DEFERRED the consolidated running-count tally to D7 (verified against the index — the cycle-040 §Working-Notes bullet is "THE SINGLE AUTHORITATIVE L3 COUNT TALLY" and the report writes no competing count; the "16 firm" figure appears only as a note-for-D7 in §Open-questions, not as an artifact edit).

**skill-uptake-survey — warning (non-blocking; telemetry only).** The report's shape implies several relevant skills, none of which is referenced by invocation. (i) `classify-variant-axis` would back the variant-axis disposition; (ii) `verify-citation-range` (esp. the cycle-021 "Sibling-slice / inherited-precedent re-anchor sub-case" and cycle-024 `tools/citecheck` realization) is the canonical procedure for an *inherited-citation* report and is exactly on-point here, yet the report does not cite running it; (iii) `proposed-changes-fence-encloses-full-body-guard` is implied by the nested-fence `new:` block. The §Open-questions does correctly name `upgrade-plain-text-ref-to-live-link-when-target-on-disk` as the forward path for the `inner_product` reference, so skill-awareness is partial. This is a pure presence check — the work is sound regardless; flagging the telemetry gap only.

### Issues found

1. **(low / telemetry) Skill-uptake gap — `reports/.../CYCLE.md` §Evidence + §"Variant axes".** The report performs an inherited-citation verification and a variant-axis enumeration without referencing `verify-citation-range` (inherited-citation sub-case) or `classify-variant-axis`. No correctness impact — both were independently re-verified clean during this critique — but the invocation telemetry is absent. Candidate for a one-line skill-reference, not a substantive fix.

2. **(low / build-robustness, not a defect) Nested `text` fences inside the `new:` block.** The `new:book/src/L3/linear_combination.md` block (lines 23–198) contains two nested ```text fences (57/60 signature, 77/82 arity specializations). Parity is even and the firm body is fully enclosed (verified), so this is NOT the cycle-019 fence-truncation defect. Noting it only because nested same-language fences inside a proposed-changes block are the known trigger for the integrator-side truncation that the `convert-nested-fences-to-indented-code-in-proposed-changes-block` skill exists to repair; the integrator-per-report should apply that conversion at apply-time if its parser is fence-greedy. Mirrors the firm L2 source entry's own structure, so no authoring change is warranted.

No citation-validity, surface, rotation, variant-axis, cross-reference, edge-label, or plan-kind issues found. The inherited-L0 framing is faithful (zero fabricated source claims), the no-sequential-obstruction claim is justified, the §"Downward to L2" demotion-home note is present and correctly identity-in-form, the dual-registration deferral to D7 is clean, and the plain-text `inner_product` forward-reference correctly avoids a `linkcheck2` hard error.

## Repair

### Fixes attempted

- **Finding**: (low / telemetry) skill-uptake gap — `verify-citation-range` (inherited-citation sub-case) and `classify-variant-axis` not referenced by invocation; `proposed-changes-fence-encloses-full-body-guard` implied by the nested-fence `new:` block.
  - **Decision**: repaired
  - **Action**: Appended a "## Skill-uptake (telemetry; appended at repair)" section to `reports/.../CYCLE.md` recording which skills were/were not invoked by name (`verify-citation-range`, `classify-variant-axis`, `proposed-changes-fence-encloses-full-body-guard` — none invoked by name; `upgrade-plain-text-ref-to-live-link-when-target-on-disk` named in §Open-questions). Pure telemetry note; no content change. This is the mechanical "record skill uptake" fix in repair scope.

- **Finding**: (low / build-robustness, not a defect) nested `text` fences inside the `new:book/src/L3/linear_combination.md` block (57/60, 77/82).
  - **Decision**: not-needed
  - **Action**: Re-confirmed the critic's finding — enumerated fences: `new:` block opens at 23, two balanced nested `text` pairs (57/60 signature, 77/82 arity specializations), block closes at 198; even parity, firm body fully enclosed. This is NOT the cycle-019 fence-truncation defect. The structure mirrors the firm L2 source entry; no authoring change is warranted. The advisory is for the integrator-per-report to apply `convert-nested-fences-to-indented-code-in-proposed-changes-block` at apply-time if its parser is fence-greedy — that is an integrator-side decision, not a repair-authority edit.

### Unrepairable findings

None. Both flagged findings were low-severity (one telemetry, one advisory-not-a-defect); the telemetry gap was repaired with a skill-uptake note and the fence advisory required no edit (re-confirmed sound).

## Suggested resolution

`ready` — clean report. The skill-uptake telemetry note is now recorded; the nested-fence structure is re-confirmed balanced and the firm body fully enclosed (no truncation risk). Note for the integrator-per-report: the `new:` block carries two nested `text` fence pairs (57/60, 77/82); if the apply-time fence parser is greedy, apply `convert-nested-fences-to-indented-code-in-proposed-changes-block` — otherwise the block applies as-is. No follow-up agent required.

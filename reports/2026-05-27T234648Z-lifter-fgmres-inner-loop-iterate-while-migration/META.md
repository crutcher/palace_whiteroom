---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T23:55:00Z
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
repaired_at: 2026-05-27T23:59:30Z
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
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of `fgmres-inner-loop-iterate-while-migration` lifter dispatch

## Critique

### Checks run

**citation-validity** — warning. The three primary cited source ranges resolve as follows. (a) `iterative.hpp:222-270` — line 222 is `class FgmresSolver` and line 270 is the first line of the `MFEM_VERIFY` inside the `SetPreconditionerSide` override; the closing `};` is at line 275. The cited range covers all load-bearing structural content (subclass declaration, `using` block, `Z` member, constructor with `pc_side = RIGHT` pinning, override entry); the missing 5 trailing lines are the verify message and closing brace. Reasonable. (b) `iterative.cpp:823-828` — line 823 is `converged = (beta < eps);` and lines 824–828 are the 3-condition `if (...) { it++; break; }` block. The combinator-miner cycle-010 audit also uses `:823-828` for this exact range; consistent. (c) `iterative.cpp:805-819` (Verified-against §) is **slightly mis-bounded**: line 805 is blank (the assignment `ApplyBA(...)` starts at line 806); line 819 is the final `ApplyPlaneRotation`. Tight range would be `:806-819`. Same minor issue at `:820-822` — the report's prose says the range covers `beta = std::abs(s[j + 1]); CheckDot(beta, ...); converged = (beta < eps);` but the actual line correspondences are `:821` beta-assign, `:822` CheckDot, `:823` converged. Line 820 is blank, and `converged = (beta < eps);` is at `:823`, which is **outside** the cited `:820-822` range. The "converged" claim in the prose at line 191 of CYCLE.md is therefore unsupported by the `:820-822` citation as quoted (the converged assignment lands one line below the cited range). Range should be `:821-823`. (d) `iterative.cpp:794-833` (top-of-Verified-against) — line 794 is the `for (;; j++, it++)` opening; line 833 lands in the *solution reconstruction* block (`ScalarType *Hi = H.data() + i * (max_dim + 1);`) which is **outside the inner Arnoldi loop**. The inner loop closes at line 829 (the `}` of the for-loop body). The cited range over-reaches by 4 lines into reconstruction. Tight range would be `:793-829` or `:794-829`. (e) `iterative.cpp:773-782` (FGMRES drift-warning compare in §Open questions / caveats) — verified: lines 772–780 are the `else if (beta > 0.0 && ...)` block with the print; the report says `:773-782` which over-reaches by 2 lines (line 781 is `beta = true_beta;`, line 782 is `if (beta < eps)` — outside the warning block). Tight range would be `:772-780`. (f) `iterative.cpp:756-765` (FGMRES `InitialResidual` + `true_beta` policy) — verified to match the source between InitialResidual call and the eps computation. (g) `iterative.hpp:263-266` for the constructor `pc_side = PreconditionerSide::RIGHT` pinning — verified at exact lines. (h) `iterative.hpp:268-272` for `SetPreconditionerSide` override — verified (line 268 is the override signature, line 272 is the closing `}`). (i) Cross-reference cites to `scaffolding/open-questions.md:1536-1538` and OQ slugs all resolve correctly. Net assessment: line-range slop on 3 of the L0 cites (`:805-819` blank-line, `:820-822` missing the converged line, `:794-833` over-reach, `:773-782` over-reach). Each is a small mechanical fix (±1–4 lines). None contradict the substantive claims; the citation evidence still strongly supports the report's structural arguments. Marking warning rather than fail because the claims are real and verifiable at correct ranges.

**surface-or-evidence** — pass. The report authors a NEW theme file (`book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md`) with full surface content (the theme entry is a complete L4>L3 lowering chapter with LHS, RHS, applicability conditions, justification kind, etc.), plus extends `SUMMARY.md` and `L4-L3/index.md` with surface entries. This is rough-in operator-shape surface authoring, not pure rotation_claim. Explicitly does NOT modify the cycle-008 GMRES theme (re-anchoring is scoped to "no change needed" with discipline-note rationale in §Discipline notes). The dispatch is correctly framed as new-surface authoring, not refinement.

**rotation-quality** — pass. The L4>L3 rotation is identical-in-shape to the sibling GMRES theme — the `Solve` monad dissolves to explicit state threading; `iterate_while` becomes a tail-recursive worker; trajectory accumulator prunes to nothing under Law 1; `stop_reason` rides in the carry. The FGMRES specialisation adds two **strictly-compactifying** variant collapses: (a) `pc_side` drops out of the closure-captured `op` because the constructor pinning makes it structurally fixed; (b) the `if op.flexible then K { Z = K.Z `with` (K.j, z) } else K` branch collapses to the unconditional capture form. Both are compaction moves at the L4 level, not 1:1 renames. The rotation is a genuine structural simplification of the GMRES form under sub-classing-induced parameter pinning.

**variant-axis-coverage** — pass. The report enumerates four GMRES variant axes (`pc_side`, `gs_orthog`, `flexible`, `max_dim`) and explicitly states the FGMRES disposition for each: `pc_side → RIGHT` (collapsed; constructor-pinned), `flexible → true` (collapsed; constructor-pinned), `gs_orthog` (free; passes through unchanged), `max_dim` (free; absorbed in `check_stop_into_carry`). The applicability conditions §6 explicitly states that future relaxation of either pinned axis would specialise back to the GMRES sibling's branched form. Scoping is clean: `restart_cycle`-level concerns (true-residual policy, drift-warning compare) are surfaced and explicitly out-of-scope.

**cross-reference-integrity** — pass. Verified the following resolve: `book/src/L4/iterate-while.md` exists; `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` exists; `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` exists; `book/src/L4/index.md` exists; `book/src/concepts/derived-view-hoisting.md` exists; `book/src/concepts/sequential-obstruction.md` exists; `book/src/concepts/variant-absorption.md` exists; `book/src/concepts/solve-monad.md` exists; `book/src/spec/slices/gmres.md` exists; OQ slugs `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker` (line 1528), `fgmres-inner-loop-iterate-while-migration-lifter-candidate` (line 1760), `variant-absorption-vs-instance-counting-policy` (line 1553), `gmres-inner-loop-iterate-while-migration` (cycle-007), `iterate-while-l3-rendering-trajectory-accumulation-gap` (cycle-006) all resolve in the open-questions ledger or are referenced in the sibling theme. The SUMMARY.md insertion edit is well-formed (correct `[old]`/`[new]` block bracketing the existing 4 entries, adding the new entry as a 5th bullet). The L4-L3/index.md table edit appends a row at the end of the existing 2-row table.

**edge-label-fidelity** — pass. The theme edge label is `L4>L3`. The LHS section explicitly carries L4 vocabulary (`iterate_while`, `Solve` monad, `Maybe StopReason`, typed carry record, extras-record return shape). The RHS section explicitly carries L3 vocabulary (positional tuple threading, tail-recursive worker, dissolved monad, trajectory pruned to `[]`). The prose narrates the rewrite forward (LHS → RHS) per the high→low directive. Direction discipline is honoured throughout — no lifting-direction descriptions in the formal chapter content; the §Status block's "the upstream gmres.md §L4 v0.6→v0.7 self-rotation" is correctly named as the upstream L4-internal self-rotation (not an L3→L4 lift) the theme depends on.

**plan-kind-consistency** — pass. Declared as `lifter` dispatch authoring an L4>L3 theme at `rough-in` status. Content shape matches: a structural L4>L3 lowering theme with full LHS/RHS, applicability conditions (5 inherited + 1 FGMRES-specific = 6 total per §Applicability conditions), justification kind (`structural` + `reduction-chain` + `empirical-match`), and the rough-in qualifier explicitly attributed to the same upstream dependency as its sibling. The dispatch correctly does NOT re-anchor the cycle-008 GMRES theme — §Discipline notes "Re-anchoring scope check" walks through each L4 vocabulary reference (`iterate_while`, `iterate-while-with-prev`, `Solve`, `Krylov`, `Maybe StopReason`, `check_stop_into_carry`) and concludes no firm-status changes since cycle-008 ⇒ no re-anchor needed. The `check_stop_into_carry` defer verdict (sister-algorithm twinning at lower-edge; no firm promotion) is correctly preserved — §Speculative L4 operators reaffirms the rough-in dep-map row text and routes firm promotion through OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`.

**skill-uptake-survey** — pass. The report cites the cycle-010 MCP-pilot combinator-miner audit (`reports/2026-05-27T215535Z-combinator-miner-check-stop-into-carry-mcp-pilot/CYCLE.md`) as upstream evidence and "MCP verification reads" (line 274) for `iterative.cpp:614-650`, `:734-836`, `iterative.hpp:222-270`. The MCP codemap server tool surface (the `palace-codemap` MCP server listed in instructions) is the relevant skill — its use is acknowledged for source localization. No explicit `verify-citation-range` skill invocation is named, but the citation discipline shows up in the report's substance (each L0 cite has line ranges). Survey is informational; not blocking.

### Issues found

1. **Citation range `:805-819` is one line off at the start** (CYCLE.md §Verified-against, line 192). Line 805 is blank; the body sequence starts at `ApplyBA(...)` on line 806. Tight range: `:806-819`. Severity: low (mechanical).

2. **Citation range `:820-822` does not contain the `converged = (beta < eps);` assignment** (CYCLE.md §Verified-against, line 191). The prose claims this range covers `beta = std::abs(s[j + 1]); CheckDot(beta, ...); converged = (beta < eps);`, but the actual line correspondences are `:821` beta-assign, `:822` CheckDot, `:823` converged. The cited range is missing line 823. Tight range: `:821-823`. Severity: low-to-medium (the substantive claim about converged is real, but the citation as quoted doesn't reach it).

3. **Citation range `:794-833` over-reaches into solution reconstruction** (CYCLE.md §Verified-against, line 190). The inner Arnoldi for-loop closes at line 829; lines 831-833 are the solution-reconstruction back-substitution block, which the report explicitly scopes OUT of `inner_loop` (§"What this lowering does NOT cover" item 2). Tight range: `:793-829` or `:794-829`. Severity: low (mechanical).

4. **Citation range `:773-782` over-reaches the drift-warning compare** (CYCLE.md §Open questions / caveats §FGMRES outer-loop scoping note, line 294). The drift-warning compare is at lines 772–780; lines 781–782 are `beta = true_beta;` followed by the convergence test, which is outside the warning block. Tight range: `:772-780`. Severity: low (mechanical; the cite is in a forward-reference scoping note, not load-bearing for the theme).

5. **`iterative.hpp` `SetPreconditionerSide` line range slight mis-bound** (CYCLE.md §Context, line 42). The report says `iterative.hpp:268-272`, but line 268 is the override signature opener; line 272 is the closing brace of the `MFEM_VERIFY`. The `}` closing the override method is on line 273. Tight range: `:268-273`. Severity: trivial (off-by-one at end).

6. **Nested-backtick rendering risk inside `text`-fenced code blocks** (CYCLE.md §L4 form, line 86; §L3 form, line 126; §What does NOT change, line 143; §"FGMRES-specific simplifications" bullet 1, line 105). The expressions `K { Z = K.Z `with` (K.j, z) }` use literal backticks inside a fenced `text` block. mdBook's CommonMark renderer treats these as literal characters inside the fence (which is the intent), so this is non-issue in the rendered book. However, if anything in the integrator pipeline post-processes the code blocks or tries to extract operator names, the backticks could trip a tokeniser. Severity: trivial (cosmetic; documenting for follow-on awareness).

7. **The L4-L3/index.md table edit re-emits the GMRES row verbatim** (CYCLE.md §"L4-L3/index.md theme table update", lines 253 → 255). The edit's `[old]` and `[new]` blocks contain the unchanged GMRES row verbatim — only the FGMRES row is added. This is correct edit-block behaviour, but it bloats the diff context. The integrator will see a no-op replacement on the GMRES row plus an append. Severity: trivial (style; the edit is functionally correct).

8. **Applicability conditions §6 cites the sibling §"Applicability conditions" by reference for conditions 1-5 without restating** (CYCLE.md §Applicability conditions, lines 162). This is a deliberate choice (the §"Applicability conditions" header on the new theme is short — one sentence pointing at the sibling, then condition 6). A future divergence in the sibling's conditions 1-5 will silently propagate (or fail to propagate) here. The report itself notes this is the "sister theme" pattern. Not a verification failure — the conditions are correctly identified — but it's a maintenance fragility worth flagging for the lowering-verifier follow-up. Severity: low (documentation discipline).

9. **The §Speculative L4 operators dep-map row text restates the rough-in annotation but does not propose an L4 dep-map edit** (CYCLE.md §Speculative L4 operators, lines 180-182). The text says "In the L4 [dep-map](../L4/index.md), this would still be annotated as..." with the annotation given as a row in prose form. No explicit edit-block to `book/src/L4/index.md` is proposed. This appears intentional (no change is needed — the cycle-008 abstractor's existing dep-map row should already carry the correct rough-in annotation), but the prose is ambiguous about whether an edit is or is not proposed. Suggest clarifying as "no edit needed; the existing dep-map row's annotation remains correct" or similar. Severity: low (clarity).

## Repair

### Fixes attempted

- **Finding 1**: `:805-819` should be `:806-819` (line 805 blank).
  - **Decision**: repaired.
  - **Action**: edited CYCLE.md §Verified-against bullet 3 — `iterative.cpp:805-819` → `iterative.cpp:806-819`. Verified via `mcp__palace-codemap__read_range` that line 805 is the blank line between `Update(j); }` and `ApplyBA(...)` (which starts on line 806), and that line 819 is `ApplyPlaneRotation(s[j], s[j + 1], cs[j], sn[j]);` — the last line of the per-step body sequence.

- **Finding 2**: `:820-822` doesn't contain `converged = (beta < eps);` — should be `:821-823`.
  - **Decision**: repaired.
  - **Action**: edited CYCLE.md §Verified-against bullet 2 — `iterative.cpp:820-822` → `iterative.cpp:821-823`. Verified that line 820 is blank, line 821 is `beta = std::abs(s[j + 1]);`, line 822 is `CheckDot(beta, ...);`, line 823 is `converged = (beta < eps);` — the three-statement sequence the prose actually names.

- **Finding 3**: `:794-833` over-reaches into solution reconstruction — should be `:794-829`.
  - **Decision**: repaired.
  - **Action**: edited CYCLE.md §Verified-against bullet 1 — `iterative.cpp:794-833` → `iterative.cpp:794-829`. Also patched the matching reference in §Context paragraph 2 — `iterative.cpp:794-833` → `iterative.cpp:794-829`. Verified that line 829 is the closing `}` of the inner-loop for-body and that line 831's `// Reconstruct the solution` comment opens the reconstruction block (explicitly out-of-scope per §"What this lowering does NOT cover" item 2).

- **Finding 4**: `:773-782` over-reaches drift-warning compare — should be `:772-780`.
  - **Decision**: repaired.
  - **Action**: edited CYCLE.md in two places — §Open questions / caveats §"FGMRES outer-loop scoping note" and §L3 form §"What does NOT change in the rotation" §"What this lowering does NOT cover" (the second `iterative.cpp:773-782` reference inside the same scoping note bullet). Both `iterative.cpp:773-782` → `iterative.cpp:772-780`. Verified that lines 772-780 span the `else if (beta > 0.0 && std::abs(beta - true_beta) > 0.1 * true_beta && print_opts.warnings)` block including the `Mpi::Print` call (line 780 ends with `)`); line 781 is `beta = true_beta;` (outside the warning block).

- **Finding 5**: `iterative.hpp:268-272` off-by-one — should be `:268-273`.
  - **Decision**: repaired.
  - **Action**: edited CYCLE.md §Verified-against bullet 4 — `(line 268-272)` → `(line 268-273)`. Also added the explicit `iterative.hpp:268-273` citation to §Context paragraph 1 where the `SetPreconditionerSide` override is described (previously the line range was only given in the §Verified-against bullet). Verified that line 268 is the `void SetPreconditionerSide(const PreconditionerSide side) override` signature opener and line 273 is the closing `}` of the override method (line 272 is the closing brace of the `MFEM_VERIFY` arg list, not the method).

- **Finding 6**: Nested backticks inside `text` fences.
  - **Decision**: not-needed.
  - **Rationale**: critic noted this is "non-issue in the rendered book" — mdBook's CommonMark renderer treats inner backticks as literal characters inside a fenced code block, which is the intended notation (the Haskell-style infix-as-backticks `K { Z = K.Z `with` (K.j, z) }`). Touching them would risk altering the intended notation in a way that affects rendering. Flagged as cosmetic-only.

- **Finding 7**: L4-L3/index.md edit re-emits GMRES row verbatim.
  - **Decision**: not-needed.
  - **Rationale**: per role-spec edit-block semantics, the `[old]`/`[new]` block surrounding the GMRES row is the well-formed pattern for "append-after-GMRES-row"; modifying it to be a pure append-block would require a different bracketing pattern that the integrator currently doesn't have first-class support for. The diff bloat is a one-row repetition and is correct as authored.

- **Finding 8**: Applicability conditions §6 cites sibling §1-5 without restating.
  - **Decision**: not-needed.
  - **Rationale**: this is a deliberate authorial choice (the report's §Discipline notes explicitly addresses the sister-theme pattern); restating would expand the theme file by ~30 lines duplicating sibling content. The maintenance fragility is real but flagging it is a `lowering-verifier` follow-up concern, not a mechanical repair. The critic itself marked this as "documentation discipline" severity-low.

- **Finding 9**: §Speculative L4 operators ambiguous about L4 dep-map edit.
  - **Decision**: not-needed.
  - **Rationale**: substantive prose clarification (authoring or rewriting prose) exceeds repair authority. The current prose is interpretable as "no edit needed; the existing row remains correct" — that's the right reading per the cycle-010 audit. A future abstractor or the integrator can clarify if needed.

### Unrepairable findings

None. All warning findings either resolved or correctly classified as cosmetic/structural (not-needed).

## Suggested resolution

`pass-after-repair`. All five mechanical citation-range fixes applied; integrator may apply the proposed changes block as-is. The four "not-needed" findings (cosmetic backticks, edit-block style, sibling-conditions reference, dep-map prose) are informational and don't block application.

The substantive content of the report — the L4>L3 sister-theme authoring, the variant-axis collapse story, the `check_stop_into_carry` lower-edge "second reuse" corroboration — is preserved unchanged. The citation evidence now resolves at tight line ranges.

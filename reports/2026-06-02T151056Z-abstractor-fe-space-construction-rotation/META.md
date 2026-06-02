---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T16:20:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-02T16:35:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of L1>L0 theme fe-space-construction-rotation

## Critique

### Checks run

**citation-validity — warning.** Verified every load-bearing pinpoint via `palace-codemap` `read_range`:
- `palace/fem/fespace.hpp:67-75` (ctor): line 67 = `template <typename... T>`, line 68 = `FiniteElementSpace(Mesh &mesh, T &&...args)`, line 69 = init list `: fespace(&mesh.Get(), ...)`, line 70 = `{`, 71 = `ResetCeedObjects()`, 72-74 = `UseDevice(true)`, 75 = closing `}`. So `67-75` correctly encloses the full ctor declaration (template-line → closing brace). **In-range, correct.**
- `palace/fem/fespace.hpp:93-103` (dof accessors): line 93 = `GetVDim`, 96 = `GetTrueVSize`, 102 = `GetProlongationMatrix`, 103 = `GetRestrictionMatrix`. The report's sub-pinpoints (`GetTrueVSize` `:96`, `GetProlongationMatrix`/`GetRestrictionMatrix` `:102-103`) are **exact**. In-range, correct.
- `palace/fem/multigrid.hpp:90` = `std::make_unique<FiniteElementSpace>(*mesh[coarse_mesh_l], fecs[0].get())` — confirmed verbatim inside `ConstructFiniteElementSpaceHierarchy`. The report's body transcription drops `.get()` on `fecs[0]` (`fecs[0]` vs source `fecs[0].get()`); the Verified-against block (line 186) ALSO drops it, but the §Summary (line 22) likewise. Minor transcription elision, not a line-range drift.
- `palace/models/spaceoperator.cpp` de-Rham sites: `:47` ND, `:49` H1, `:51` RT all confirmed at member-init; `:75` confirmed as the `std::make_unique<mfem::L2_FECollection>(..., mfem::FiniteElement::INTEGRAL)` line inside the 2-D branch (`:73-79` body). All four exact. The source comment at `:70-72` confirms the INTEGRAL-map rationale verbatim ("Must use INTEGRAL map type so the discrete interpolator recognizes this as the curl target space"), so the load-bearing 2-D-curl claim is directly source-grounded.
- `book/src/L0/fespace-file.md` anchors: `:154-158` carries the "The dof structure is MFEM's; the lift reads it as given." bullet (the report's quoted phrase is verbatim) with `fespace.hpp:93-103` cited at `:156`; `:159-164` and `:165-169` fall in the libCEED-cache / de-Rham-complex bullets. In-range.

The warning is the **D2/D3 ctor line-range disagreement** (flagged below), not a drift in D3's own citation.

**surface-or-evidence — pass.** This is a NEW L1>L0 theme (lowering surface), not a refinement of an existing operator/theme. It introduces new surface (`L1-L0/fe-space-construction-rotation.md`) with structural justification grounded in positive L0 anchors. Not a pure rotation_claim; the surface-or-evidence gate is satisfied by the new-surface arm.

**rotation-quality — pass.** Genuine vocabulary translation, not a degenerate mirror/rename. LHS is a pure value `fe_space :: (mesh, collection) -> FiniteElementSpace[N]` (referentially-transparent pairing naming a true-dof-indexed space); RHS is an imperative C++ ctor forwarding `(&mesh.Get(), args...)` into `mfem::ParFiniteElementSpace` plus `ResetCeedObjects()` cache-init and device placement. The translation crosses semantic organizations (value-naming → object-construction-with-side-effecting-cache-init), and the named **construction-lowers / dof-bookkeeping-MFEM-owned split** is the substantive content — not a 1:1 named-term echo. State-hiding (the dof bookkeeping is collapsed into the opaque index axis `N`) is present, which is the pass signature.

**variant-axis-coverage — pass.** The de-Rham family is the declared variant axis and all four cases are covered with per-case L0 instantiation sites (H1@49, ND@47, RT@51, L2@75), each mapped to its FECollection subclass and map type. The 2-D L2-curl INTEGRAL-map special case is explicitly called out as a load-bearing variant (not hidden) and source-confirmed at `:75` with the `:70-72` rationale comment. No hidden branches. The hierarchy-producing form and the collection order-schedule are explicitly scoped out (deferred `fe_space_hierarchy` / `fe_collection` siblings), not silently dropped.

**cross-reference-integrity — warning.** The construction-lowers / MFEM-owned split is correct and the firmness is justified by documentation-not-reconstruction (see (c) verdict in findings). Sibling-theme live-links all resolve: `fe-assemble-libceed-boundary-obstruction.md`, `weak-form-term-rotation.md`, `fe-operator-assemble-mutation-rotation.md` all exist on disk. The index.md edit anchors on the `weak-form-term-rotation` row, which I confirmed exists verbatim — the parallel-safe insert will apply cleanly. The SUMMARY anchor is textual (after the `weak-form-term-rotation` line) and resolves; the stated line number "149" is slightly stale (cosmetic). **The warning:** the forward-ref live-link `[`L1/fe_space`](../L1/fe_space.md)` (used in the chapter body AND in the proposed index.md row) targets a file that does NOT yet exist on disk — it is D2's same-cycle entry. This is per the cross-report forward-reference convention and D3 flagged it explicitly, but a live `[...](../L1/fe_space.md)` link to a missing file is a hard `linkcheck2` build error if D2 does not land in the same integration batch. Integrator must sequence D2 before/with D3, or down-convert to plain-text per the rough-in-forward-reference convention.

**edge-label-fidelity — pass.** Edge is L1>L0, forward-narrated. LHS is L1 `fe_space` (the pure value), RHS is L0 (the concrete ctor + source sites). The prose narrates exactly this edge throughout ("lowers FORWARD into the concrete Palace FiniteElementSpace object construction"); §"L1 form (LHS)" and §"L0 form (RHS)" are correctly labeled. No mismatch.

**plan-kind-consistency — pass.** Declared `firm` (L1>L0 theme). Content shape matches: positively-anchored construction rewrite (ctor + 4 collection sites + coarse-seed), documented library boundary (not a constructive sub-part), no rough-in placeholders. The firm-on-positive-structure precedent (cf. `weak-form-term-rotation`, `fe-operator-assemble-mutation-rotation`) is correctly invoked — the MFEM-owned dof boundary is a witnessed library-ownership boundary read-as-given, not a `partly-constructive` constructed sub-part, so `firm` (not `partly-constructive`) is the right tier.

**skill-uptake-survey — warning.** The report cites "verified via codemap read_range" repeatedly but does not reference invoking `verify-citation-range` (or its mechanical `tools/citecheck/` realization) for the citation pinpoints, nor `classify-variant-axis` for the 4-case de-Rham axis. Both skills are directly relevant to this theme's shape (citation-heavy + explicit variant axis). Pure telemetry surface — non-blocking; the underlying citations independently verify correct.

### Issues found

1. **[warning] D2/D3 ctor line-range disagreement — `palace/fem/fespace.hpp` ctor** (CYCLE.md §Summary L19-22, §L0-form L82, §Verified-against L181, index.md row, throughout). D3 cites the ctor as `:67-75`; the dispatch note records D2 using `:66-74` for the same ctor. Codemap confirms **D3's `67-75` is the more accurate range**: line 67 = `template <typename... T>`, 75 = the closing `}`. D2's `66-74` starts at `public:` (line 66, an access specifier, not part of the ctor) and ends at line 74 (`ly.UseDevice(true);`), truncating before the closing brace at 75. The integrator should reconcile D2 and D3 to ONE range when both land — recommend `67-75` (D3's). Severity: low (both overlap the ctor body; this is a boundary-tightness disagreement, not a wrong-region citation), but flagged per dispatch instruction for integrator reconciliation.

2. **[warning] Forward-ref live-link to not-yet-existing `book/src/L1/fe_space.md`** (CYCLE.md proposed chapter L46, L67, L194; index.md row L226; SUMMARY untouched). The link `[`L1/fe_space`](../L1/fe_space.md)` is a live Markdown link to D2's same-cycle entry, which is not on disk at critique time. If D2 does not land in the same integration batch, this is a hard `linkcheck2` build break. D3 flagged this in its own Open-questions (L212-214) and it follows the cross-report forward-reference convention, but it is a build-ordering dependency the integrator must honor (sequence D2 with/before D3, or down-convert to plain-text). Severity: low-to-medium (build-gating only if D2 slips).

3. **[info] `fecs[0]` vs `fecs[0].get()` transcription elision** (CYCLE.md §Summary L22 implicitly, §L0-form L93, §Verified-against L186). The `multigrid.hpp:90` body transcription writes `fecs[0]` where the source has `fecs[0].get()`. Line range is correct; only the inline code-snippet drops the `.get()`. Cosmetic — does not affect the rewrite claim. (The §Supporting-evidence L255 transcription DOES include `.get()`, so it's an internal inconsistency too.)

4. **[info] Stale SUMMARY anchor line number** (CYCLE.md L231). The proposed SUMMARY insert says "after the existing `weak-form-term-rotation` line (line 149)"; the textual anchor is correct but the line number is slightly off (the row sits one line below the stated position). Textual-anchor insert is unaffected; cosmetic.

5. **[info] skill-uptake telemetry** — no explicit `verify-citation-range` / `classify-variant-axis` invocation referenced despite a citation-heavy + explicit-variant-axis shape. Non-blocking; citations independently verify clean.

---

## Repair

### Fixes attempted

- **Finding (1): citation-validity warning — D2/D3 ctor line-range disagreement on `palace/fem/fespace.hpp` ctor.** The dispatch instruction directed me to change every `:67-75` for this ctor to `:66-74` (to match D2's `fe_space.md`), on the stated basis that line 74 = closing brace and line 75 = destructor.
  - **Decision: not-needed** (D3's `:67-75` is already the accurate range; the requested `:66-74` would be strictly worse).
  - **Action: none applied** to the ctor range — re-verified against source via `palace-codemap read_range` before touching it:
    - line 64 = `BuildDiscreteInterpolator`, line **66 = `public:`** (access specifier — NOT part of the ctor),
    - line **67 = `template <typename... T>`** (start of ctor),
    - line 68 = `FiniteElementSpace(Mesh &mesh, T &&...args)`, 69 = init-list, 70 = `{`, 71–74 = body (`ResetCeedObjects()` / `tx`/`lx`/`ly.UseDevice(true)`),
    - line **75 = `}`** (closing brace of the ctor),
    - line **76 = `virtual ~FiniteElementSpace()`** (the destructor).
  - **Rationale for not applying the requested fix:** the dispatch reasoning was off-by-one. The destructor is at **76**, not 75; the ctor's closing brace is at **75**, not 74. So the full ctor (template-line → closing brace) is exactly `:67-75` — which is what D3's CYCLE.md and the critic's own `read_range` verification both already carry. Applying `:66-74` would (a) prepend `public:` (line 66, not part of the ctor) and (b) drop the closing brace (line 75) — introducing a citation error rather than fixing one. Per repair discipline (mechanical/surgical, never author an incorrect citation), I left D3's `:67-75` in place. The D2/D3 disagreement should be **reconciled toward `:67-75` (D3's), NOT D2's `:66-74`** — D2's `fe_space.md` is the entry that needs the correction at integration, which is out of this report's modify-scope.

- **Finding (2): cross-reference-integrity warning — forward-ref live-link `../L1/fe_space.md`.**
  - **Decision: not-needed** (resolved-by-construction; explicitly by-design per dispatch).
  - **Rationale:** standard same-cycle cross-report forward-reference. D2's `book/src/L1/fe_space.md` lands this cycle; the live link resolves at the single `integrator-finalize` build. Do NOT down-convert to plain-text. **Integrator-ordering note:** apply D2's `fe_space.md` before/with D3 so `../L1/fe_space.md` is on disk for the finalize `linkcheck2` pass; both resolve at the one finalize build.

- **Finding (3): skill-uptake-survey warning — telemetry-only.**
  - **Decision: not-needed.** Pure telemetry; the underlying citations independently verify clean. No artifact change.

- **Finding (4a): info nit — `fecs[0]` vs source `fecs[0].get()` snippet elision.**
  - **Decision: repaired** (trivial transcription fix to match source).
  - **Action:** CYCLE.md §Verified-against — changed `fecs[0]` → `fecs[0].get()` to match `palace/fem/multigrid.hpp:90` and the §L0-form (L93) / §Supporting-evidence (L255) transcriptions (which already carry `.get()`). Line range was already correct; this only aligns the inline snippet.

- **Finding (4b): info nit — stale SUMMARY anchor line number ("line 149").**
  - **Decision: not-needed** (cosmetic; textual anchor unaffected).
  - **Rationale:** the SUMMARY insert anchors on the textual `weak-form-term-rotation` line, which is correct and unambiguous; the parenthetical "(line 149)" is advisory only and does not affect the textual-anchor insert. Left as-is.

### Unrepairable findings

None. No finding required substantive authoring or exceeded repair authority. The one finding that requested an edit (the ctor range) was verified against source and found to be already correct — applying the requested change would have introduced an error, so it was correctly declined as `not-needed`.

## Suggested resolution

`overall_status: ready`. Notes for the integrator:

1. **Ctor range is `:67-75` (correct as-is).** Codemap-verified: ctor spans template-line 67 → closing brace 75; destructor is line 76; `public:` is line 66. If reconciling the D2/D3 disagreement, **converge BOTH on `:67-75`** — correct D2's `book/src/L1/fe_space.md` (which carries `:66-74`), not D3. D3 needs no change.
2. **Forward-reference ordering:** apply D2's `book/src/L1/fe_space.md` before/with D3 so the live link `../L1/fe_space.md` resolves at the single finalize `linkcheck2` build. Do not down-convert to plain-text.
3. One trivial transcription fix was applied to D3's §Verified-against (`fecs[0]` → `fecs[0].get()`).

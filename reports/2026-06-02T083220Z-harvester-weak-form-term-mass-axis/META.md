---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T084500Z
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
repaired_at: 2026-06-02T085200Z
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

# META: verification of "Ground the Identity/mass axis point of weak_form_term at L1 (in-place)"

## Critique

### Checks run

**citation-validity — pass.** All load-bearing citations were verified against the on-disk source via `palace-codemap` `read_range`/`search_text`:
- `palace/models/spaceoperator.cpp:278` → `a.AddDomainIntegrator<VectorFEMassIntegrator>(*f);` — CONFIRMED the integrator class is `VectorFEMassIntegrator` (NOT `MassIntegrator`/`MassVectorIntegrator`), coefficient `*f`.
- `palace/models/spaceoperator.cpp:438` → `std::unique_ptr<OperType> SpaceOperator::GetMassMatrix(...)` — CONFIRMED.
- `palace/models/spaceoperator.cpp:260` → `void AddIntegrators(BilinearForm &a, ...)` signature line — CONFIRMED (the fold function).
- `palace/models/spaceoperator.cpp:459` → `mr = AssembleOperator(GetNDSpace(), nullptr, &fr, ...)` — CONFIRMED (the `nullptr` is the `df`/curl-slot argument; routes the pure-mass branch).
- `palace/fem/integrator.hpp:39-42` → `BilinearFormIntegrator` base + `const MaterialPropertyCoefficient *Q` slot — CONFIRMED (the variant-invariant coefficient slot).
- `palace/fem/integrator.hpp:68-69` → MassIntegrator comment (`:68`) + class decl (`:69`) — CONFIRMED.
- The mass term IS `(Q, Identity)`: the integrator wrapper comments are literally `a(u, v) = (Q u, v)` (no derivative operator on `u`), confirming the identity differential operator. The branch at `:278` is reached when only `f` (mass coeff) is present, distinct from the fused `CurlCurlMassIntegrator` at `:264`. CONFIRMED.
- Corroborating consumer sites all confirmed real `VectorFEMassIntegrator` instantiations: `modeeigensolver.cpp:62`, `domainpostoperator.cpp:38`, `romoperator.cpp:424` (search_text returned all three at the cited lines).
- `DivDivIntegrator` absence in `palace/models/*.cpp` — CONFIRMED (`search_text` returns zero hits), grounding the "no in-scope solver-K witness" pending-pull claim for the Divergence point.

One minor descriptive (not citation-range) drift, see Issues #1.

**surface-or-evidence — pass.** This is a refinement-shaped proposal that BOTH modifies surface (the variant-axis prose, the Evidence list, the Status paragraph of `book/src/L1/weak_form_term.md`) AND carries grounding evidence (the `GetMassMatrix`/`AddIntegrators`/`VectorFEMassIntegrator` witness chain). It is not a pure rotation_claim; it moves the Identity axis point from "named pending-pull sibling" to "grounded specialization with an L0 witness," which is exactly the surface+evidence shape. Pass.

**rotation-quality — pass (not a rotation proposal).** This is an L1-internal axis-point grounding, not an inter-layer rotation claim. No L_{n+1}→L_n compaction is asserted; the entry remains an inert pair constructor at L1. The check is structurally inapplicable to an in-place specialization-note edit; marked pass with that scope note. The "SAME BilinearForm-fold differing only in the integrator slot" framing is a witness-equivalence observation, not a rotation claim.

**variant-axis-coverage — pass.** The differential-operator axis (`Gradient | Identity | Curl | Divergence`) is the primary variant axis and is handled explicitly: 3-of-4 now grounded (Gradient/electrostatic, Curl/magnetostatic, Identity/mass — this dispatch), with `Divergence`/div-div explicitly scoped out as a pending-pull sibling carrying a cited absence (`search_text` zero-hit) rather than a hidden branch. The combined `df+f` → `CurlCurlMassIntegrator` fused branch is NOT hidden — it is explicitly addressed in §Supporting evidence and correctly carved out as a distinct additive-sum term, with the pure-mass `:278` branch (`nullptr` curl slot via `:459`) identified as the clean `(Q, Identity)` witness. This fused-vs-pure distinction is accurate per the source read (the `if (df && ... && f && ...)` guard at `:264` vs. the else-branch `:278`). No hidden branch; pass.

**cross-reference-integrity — pass.** All three `edit:` SEARCH blocks match the current `book/src/L1/weak_form_term.md` content exactly and uniquely (verified by reading the target file: the variant-axis block lines 180-191, the Evidence Identity lines 263-266, the Status witness-count sentence 228-229). No new chapter, no new dep-map row, no SUMMARY line, no new lowering theme is created — confirmed by the report's explicit assertions AND by the edit being purely in-place within an existing firm chapter. All referenced slugs (`fe_assemble`, `fe-operator-assemble-mutation-rotation`, `fe-assemble-libceed-boundary-obstruction`) already exist as live links in the file. Build-readiness fence guard is not applicable (no firm-chapter-body-inside-fence; this is an in-place edit-block, not a `new:` body). Pass.

**edge-label-fidelity — pass (no edge label).** This is an L1-internal edit; it carries no L_{n+1}→L_n edge label. Not applicable; pass.

**plan-kind-consistency — pass.** The declared shape (in-place specialization-note edit, combinator-primary per the 2026-06-01 redirect §1: differential-operator variants are specialization notes under the term abstraction, NOT new mirrored entries) matches the content exactly. The status stays `firm` (unchanged), and the term-abstraction algebraic laws are correctly noted as witness-independent — verified against the file: laws 1-4 are pair-constructor/bilinearity facts that do not reference any specific witness, so adding a grounded mass witness genuinely does not perturb them. No mis-classification; this is correctly NOT a new entry. Pass.

**skill-uptake-survey — warning.** The report's shape (citation grounding via `palace-codemap` + `tools/citecheck/citecheck.py --anchor`) implies the `verify-citation-range` skill (whose cycle-024 mechanical realization is exactly the `citecheck --anchor`/`--scan` path). The report references `citecheck.py --anchor` invocations directly in §Supporting evidence (`[citecheck ok]` tags, anchor results) but does not name the `verify-citation-range` skill by slug. This is a surfacing-only warning (the check is non-blocking, pure telemetry): the procedure WAS followed, only the skill-name attribution is absent. No action implied for the integrator.

### Issues found

1. **Descriptive off-by-one in the `VectorFEMassIntegrator` line attribution (minor, §Supporting evidence + new Evidence note).** The report's §Supporting evidence final bullet states the `:79-80` range brackets "comment + class decl (citecheck anchored the class name at `:69` / `:80`)" and the proposed Evidence-block REPLACE line 79 says "comment `:79`, class decl `:80`". Source verification: the `VectorFEMassIntegrator` *comment* is at line `:78` and the *class declaration* is at line `:79` (line `:80` is `protected:`). So the descriptive parenthetical is off by one (comment is `:78` not `:79`; class is `:79` not `:80`). NOTE: the CITED RANGE `:79-80` is NOT itself out-of-range — it still encloses the class declaration (`:79`) — so this is not a citation-validity fail, only an inaccurate human-readable description of which line holds what. The existing file's own Evidence citation `palace/fem/integrator.hpp:79-80` is unchanged by this edit and remains a valid (if slightly loose) range. Severity: low / cosmetic. Location: CYCLE.md §Supporting evidence (last bullet) and the §"Operator content" Evidence list parenthetical "(comment `:79`)". The MassIntegrator `:68-69` attribution (comment `:68`, class `:69`) IS correct — only the `VectorFEMass` one drifted.

2. **Corroborating-witness coefficient is not a generic mass coefficient at one named site (informational, §Summary + Evidence).** The report names `modeeigensolver.cpp:62` as an additional `VectorFEMassIntegrator` consumer "witness" for the mass term; source confirms the instantiation but its coefficient is `muinv_func` (inverse permeability), not a generic mass coefficient `Q`. This does not undermine the claim — the report explicitly designates `GetMassMatrix`/`:278` as the canonical pure-`(Q, I)` witness and treats the others as "corroborating, not individually re-verified line-by-line," and the corroboration being claimed is the *integrator-slot fold shape* (which holds — it IS a `VectorFEMassIntegrator` domain fold), not coefficient purity. Flagged only so the integrator/next-reader knows the named corroborators vary in coefficient role; no correction required. Severity: informational. Location: CYCLE.md §Summary + new Evidence consumer-site list.

3. **(non-issue, recorded for completeness) The "two witnesses" → "multiple witnesses" Status edit is internally consistent.** The third SEARCH/REPLACE softens "two witnesses differing in EXACTLY the integrator slot" to "multiple witnesses," consistent with the new 3-grounded count. The SEARCH block matches the file uniquely. No issue.

---

## Repair

### Fixes attempted

- **Finding #1 (citation-validity)**: Descriptive off-by-one in the `VectorFEMassIntegrator` line attribution — report says comment `:79` / class decl `:80`; source shows comment `:78` / class decl `:79` (the cited range `:79-80` still encloses the class decl, so it is NOT a citation-range fail — only the inline parenthetical drifted).
  - **Decision**: repaired
  - **Action**: Verified actual source via `palace-codemap read_range palace/fem/integrator.hpp:66-82` — confirmed `VectorFEMassIntegrator` comment is at `:78`, class decl at `:79`, `protected:` at `:80` (and `MassIntegrator` class decl at `:69`, matching the critic). **Determined the off-by-one does NOT land in the artifact**: the three `edit:` proposed-changes blocks (CYCLE.md lines 32-105) do not contain the `:79`/`:80` parenthetical — the Evidence-block REPLACE (lines 75-88) reads "(the integrator the mass witness instantiates)" with no line attribution. The drift appears only in (a) the §"Operator content" recap (CYCLE.md:148-149) and (b) §Supporting evidence discussion prose (CYCLE.md:166-168) — neither is parsed into `book/`. Corrected both report-side references to `:78` (comment) / `:79` (class decl) for internal report accuracy, with a note that the cited `:79-80` range encloses the class decl. This is the "citation line range off by a small offset" repairable category, applied surgically and pre-integration.

- **Finding #2 (informational, no fix)**: Corroborator `modeeigensolver.cpp:62` uses `muinv_func` not a generic mass `Q`.
  - **Decision**: not-needed
  - **Rationale**: Critic flagged as informational-only; the corroboration claimed is the integrator-slot fold-shape (which holds — it IS a `VectorFEMassIntegrator` domain fold), not coefficient purity. The canonical pure-`(Q, I)` witness is `GetMassMatrix`/`:278`, which is unaffected. No correction required.

- **Finding (skill-uptake-survey warning)**: `verify-citation-range` skill procedure followed (via `citecheck --anchor`) but not named by slug.
  - **Decision**: not-needed
  - **Rationale**: Critic marked this non-blocking telemetry-only ("No action implied for the integrator"). Procedure was followed; only the name attribution is absent. Not a repair-authority item.

### Unrepairable findings

None. The sole substantive finding (#1) was mechanically repairable (verified line offset, surgical edit). Findings #2 and the skill-uptake-survey warning are informational/telemetry-only and require no edit.

## Suggested resolution

`ready`. The report's three `edit:` proposed-changes blocks are clean — the off-by-one never reached the artifact-landing text, and the report-side recap/prose drift has been corrected. Integrator can apply the three in-place `book/src/L1/weak_form_term.md` edits as-is. The `VectorFEMassIntegrator` Evidence citation `palace/fem/integrator.hpp:79-80` is an existing (unchanged) range and remains valid — it encloses the class decl at `:79`.

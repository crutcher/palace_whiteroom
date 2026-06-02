---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T081500Z
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
repaired_at: 2026-06-02T082600Z
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

# META: verification of harvester firm L1 `weak_form_term` entry (cycle-061 D1)

## Critique

### Checks run

**citation-validity — warning.** `citecheck --scan` over the full report: **28 ok, 0 failing** (bounds + path-hygiene clean). Anchor-checked every load-bearing pinpoint. Confirmed-OK: `laplaceoperator.cpp:191-194 --anchor DiffusionIntegrator` (anchor at 194), `:191 --anchor epsilon_func` (at 191), `curlcurloperator.cpp:170-181 --anchor CurlCurlIntegrator` (at 181), `integrator.hpp:39-42 --anchor MaterialPropertyCoefficient` (at 42), `bilinearform.hpp:53-57 --anchor AddDomainIntegrator` (at 54), and the four integrator doc-comment anchors `:68-69`/`:100-101`/`:111-112`/`:122-123` (all OK on `Q u`/`grad u`/`curl u`/`div u`). `read_range` on both K-build sites confirms the substantive claim — the magnetostatic and electrostatic K-builds use the **identical `BilinearForm`-fold differing only in the integrator slot** (`AddDomainIntegrator<CurlCurlIntegrator>(muinv_func)` vs `<DiffusionIntegrator>(epsilon_func)`). **One DRIFT, repeated:** the `muinv_func` declaration is cited as `palace/models/curlcurloperator.cpp:179-180` in three places (CYCLE.md:79, :316, :427) but the authoritative citecheck line-map places the `MaterialPropertyCoefficient muinv_func(...)` declaration at **177-178** (anchor `muinv_func` first matches line 178; range `:179-180 --anchor muinv_func` returns `[DRIFT -1]`, suggested `:178-179`). The `AddDomainIntegrator<CurlCurlIntegrator>(muinv_func)` line is correctly cited at `:181`. So the integrator-site pin (`:181`) is correct; the coefficient-declaration pin (`:179-180`) is off by ~2 lines (the actual decl is 177-178). This is a real `warning` (the integrator pin and the substantive claim are unaffected; only the secondary coefficient-decl line-range drifts). I leave the corrected range to the repairer: `:179-180` → `:177-178` (or `:178` for the anchor line). No `verified_against:` YAML block in this report — that sub-check is not applicable.

**surface-or-evidence — pass.** The report is a new firm L1 operator entry PLUS a refinement (`edit:`/`edit-to:` on the already-firm `fe_assemble.md`). For the refinement: it modifies surface (the opaque-`WeakFormTerm` rough-in note → live link to `weak_form_term`) and is grounded — but it is a **reference-upgrade**, not an algebraic-claim change to `fe_assemble`'s fold (the edit-to text explicitly states "the fold's structure and laws are unchanged… the term remains an opaquely-folded input"). This is precisely the redirect's replace-and-propagate discipline (combinator/abstraction firmed, its consumer's opaque-input note re-anchored, not stranded). The `edit:` source blocks both match the live `fe_assemble.md` text verbatim (lines 69-71 and 158-166 — verified). Not a pure-rotation-without-surface case; passes.

**rotation-quality — pass.** The entry asserts the identity-lowers / kernel-opaque split: the term's **IDENTITY** (`(coefficient, diff_op)` pair) is Palace-readable at the `AddDomainIntegrator<T>(Q)` instantiation site and lowers trivially to the `(T, Q)` template/runtime slots; the term's **KERNEL** (`A(space, ·)`, the per-element quadrature realization) is the libCEED opaque boundary (`fe-assemble-libceed-boundary-obstruction`, `opaque-library-ownership`, cycle-055). This is a genuine vocabulary shift, not a rename: L0 carries the differential operator in the C++ *type system* (template parameter selecting a `BilinearFormIntegrator` subclass) + a mutable heap-owned `push_back` container; L1 re-expresses it as a first-class `DifferentialOperator` enumeration value in an inert immutable record, hiding the template-dispatch + `make_unique`/`push_back`/owned-container threading into the lowering. State-hiding + type-to-value coarsening = a real rotation. Passes.

**variant-axis-coverage — pass.** This is the focus check and the scoping is correct. The **differential-operator** primary axis has two points GROUNDED by in-scope solver-K witnesses (`Gradient`/electrostatic-diffusion, `Curl`/magnetostatic-curl-curl) and two named as **pending-pull SIBLINGS, explicitly NOT speculatively authored** (`Identity`/mass, `Divergence`/div-div) — each with its integrator wrapper cited and an explicit pull-condition. This is the redirect's pull-only clean-gate honored exactly: the grounded cases are covered, the ungrounded cases are *named on the axis but scoped out* (not hidden, not over-authored). The **div-div negative anchor is verified**: codemap `search_text DivDivIntegrator` confirms `AddDomainIntegrator<DivDivIntegrator>` appears ONLY in `test/unit/test-libceed.cpp:1384`, NEVER in any `palace/models/*.cpp` K-build — so the "no in-scope solver-K witness / possible spine-coverage finding" framing is accurate, not an unjustified gap. The two sub-axes (coefficient-rank scalar/matrix; term-position domain/boundary) are each covered with a variant-invariance argument (`Q`-on-base-class is uniform across `diff_op`) and citations. The mixed/rectangular integrators are explicitly carved out (square-pairing scope) with law-3 backing and adjacency citations. No hidden branches. Passes.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: `fe_assemble.md`, `eliminate_essential_bc.md`, `fe-operator-assemble-mutation-rotation.md`, `fe-assemble-libceed-boundary-obstruction.md` all exist. Both `edit:` anchor texts (`fe_assemble.md:69-71`, `:158-166`) and the index `edit:` anchors (the `fe_assemble`-FIRM bullet line 72, the `eliminate_essential_bc` dep-map row line 113) and the SUMMARY anchors (lines 114-115) all match live file text — verified. Build-readiness fence guard: 29 fences (odd parity = the documented nested-`text`-fence pattern, NOT a defect). The `new:book/src/L1/weak_form_term.md` block opens at line 35 and closes at line 342; the full firm apparatus (`## Signature` :92, `## Semantics` :117, `## Algebraic laws` :147, `## Status` :254, `## Evidence` :293) sits INSIDE the fence, with three nested `text` fences (93/97, 123/125, 131/136) all paired inside. The "Operator content" section (line 382) explicitly confirms the body is authored inside the proposed-changes block — this is the correct nested-fence authoring, not the cycle-019 fence-truncation defect. Dual-registration (own dep-map row + own cohort bullet) is present and partition-correct. Passes.

**edge-label-fidelity — pass.** The entry carries no L_{n+1}→L_n edge label of its own (it is a leaf L1 entry; `lowers_to` points at the existing `fe-assemble-libceed-boundary-obstruction` theme and the §"Downward to L0" prose narrates the L1→L0 identity-lowers / kernel-opaque split forward, consistent with the declared direction). No misdirected edge. Passes.

**plan-kind-consistency — pass.** Declared kind is firm L1 operator; content shape matches — full Signature with shape contracts, Semantics, four stated algebraic laws + three explicit non-laws, Dependencies, Variant axes, Status, L1-vs-L0, Evidence. No rough-in placeholders in the firm body. The `firm` vs `rough-in (test-coverage-bounded)` call (focus-d) is correct: the four laws (coefficient-linearity/scaling, coefficient-additivity, diff-op-discreteness, symmetry-for-symmetric-Q) are bilinearity/pair identities on a fully-specified positive `(Q, 𝒟)` structure read from the instantiation site — syntactic-identity laws on a read closure, the `fe_assemble`/`apply_linop` firm-on-positive-structure precedent. The no-dedicated-`weak_form_term`-test caveat is correctly non-gating (and the entry even points at `TestCeedOperatorFullAssemble` as future `empirical-match` evidence for the realization `A`, not for the pair-constructor laws). `firm` is the right tier, not `rough-in (test-coverage-bounded)`. Passes.

**skill-uptake-survey — pass.** The report references its citation-verification mechanically (citecheck `--anchor`/`--scan` self-verification in §Supporting evidence) and applies the redirect's pull-only clean-gate + replace-and-propagate discipline explicitly. The shape (firm operator promotion with surface re-anchor) implies `verify-citation-range` / `verify-rotation-citation` / `propose-rotation` — the citation-range procedure is evidenced; rotation-citation is implicitly satisfied by the §Downward narration. Telemetry only; passes.

### Issues found

1. **citation-validity (warning) — `muinv_func` coefficient-declaration line drift.** CYCLE.md:79, :316, :427 cite `palace/models/curlcurloperator.cpp:179-180` for the `MaterialPropertyCoefficient muinv_func(...)` declaration. Authoritative citecheck line-map places that declaration at **177-178** (anchor `muinv_func` first matches line 178; `:179-180 --anchor muinv_func` → `[DRIFT -1]`, suggested `:178-179`). The companion `AddDomainIntegrator<CurlCurlIntegrator>(muinv_func)` pin at `:181` is **correct**, and the substantive same-fold-differs-only-in-integrator claim is unaffected. Repair: change the three `:179-180` muinv_func-declaration references to `:177-178` (the integrator-site `:181` references stay). Note the parallel electrostatic claim `epsilon_func` at `:191` is verified correct, so this drift is isolated to the magnetostatic coefficient-decl pin. Severity: low (secondary line-range; integrator pin and claim intact), but it is a real `warning` per the line-map.

No other issues. Citations (modulo the one drift), pull-justification, variant-axis scoping, firm-status call, rotation split, cross-references, and fence-readiness all check out.

## Repair

### Fixes attempted

- **Finding**: citation-validity (warning) — `muinv_func` coefficient-declaration line drift; cited `palace/models/curlcurloperator.cpp:179-180`, off from the authoritative line-map.
  - **Decision**: repaired
  - **Action**: Verified the declaration range by `mcp__palace-codemap__read_range` on `palace/models/curlcurloperator.cpp:174-183`. The `MaterialPropertyCoefficient muinv_func(...)` statement occupies **lines 178-179** (178: `MaterialPropertyCoefficient muinv_func(mat_op.GetAttributeToMaterial(),`; 179: `mat_op.GetCurlCurlInvPermeability());`); the `k.AddDomainIntegrator<CurlCurlIntegrator>(muinv_func)` integrator-site is at 181. This confirms the critic's citecheck `--anchor` suggested range `:178-179` (the critique prose's "177-178" is a transcription slip in the prose; the `--anchor` suggestion `:178-179` and the direct `read_range` both agree on 178-179). Applied the verified range to the four declaration-specific references in CYCLE.md (which land in the `book/src/L1/weak_form_term.md` proposed-changes body, so the corrected citation reaches the artifact):
    - line 79 (`weak_form_term.md` §Semantics witness pair): span start corrected `:179-181` → `:178-181` (span covers declaration start through integrator site; integrator pin 181 preserved).
    - line 239 (§Variant-axes coefficient-rank): `:179-180` → `:178-179`.
    - line 316 (§Evidence magnetostatic witness): `(:179-180)` → `(:178-179)`.
    - line 427 (CYCLE.md §Supporting-evidence citecheck note): `:179-180` → `:178-179`.
  - **Untouched (by design)**: the `:181` integrator-site pins, the `:191` electrostatic `epsilon_func` pin (verified correct), and the `:170-181` `GetStiffnessMatrix` full-function spans (start 170, integrator-bounded end 181 — both boundaries unaffected by the declaration drift).

### Unrepairable findings

None. The single warning was a mechanical line-range drift fully within repair authority (citation line range off by a small offset). All other checks passed from the critic.

## Suggested resolution

`ready`. Integrator note: the citation correction lands inside the `new:book/src/L1/weak_form_term.md` proposed-changes body and the report's own evidence/citecheck notes, so the firm L1 `weak_form_term` entry and its `fe_assemble.md` re-anchor refinement apply with a clean magnetostatic coefficient-declaration pin (`:178-179`).

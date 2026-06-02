---
verifies: ./CYCLE.md
critiqued_at: 2026-06-02T081500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-02T082000Z
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

# META: verification of L1>L0 theme weak-form-term-rotation (cycle-061 D2)

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` (18 ok / 3 failing of 21). All 5 of D2's own load-bearing anchors verified at the byte level via `read_range`: `bilinearform.hpp:53-57` is the `AddDomainIntegrator<T>` body `domain_integs.push_back(std::make_unique<T>(std::forward<U>(args)...))` (and `:59-63` is the sibling `AddBoundaryIntegrator`, exact); `integrator.hpp:39-42` is `class BilinearFormIntegrator` with `const MaterialPropertyCoefficient *Q` landing exactly at :42; `laplaceoperator.cpp:191-194` is `epsilon_func` + `AddDomainIntegrator<DiffusionIntegrator>(epsilon_func)` with the call at :194 inside `GetStiffnessMatrix` (method at :184); `curlcurloperator.cpp:179-181` is `muinv_func` + `AddDomainIntegrator<CurlCurlIntegrator>(muinv_func)` with the call at :181 inside `GetStiffnessMatrix` (method at :171). Wrapper doc-comments verified: DiffusionIntegrator `a(u,v) = (Q grad u, grad v)` at :100, CurlCurlIntegrator at :111, MassIntegrator `(Q u, v)` at :69, VectorFEMassIntegrator at :80, DivDivIntegrator `(Q div u, div v)` at :122 — all match the cited ranges. The abstractor's `--anchor [ok]` claims are all corroborated. **The 3 citecheck failures are NOT D2 defects** — confirmed: `integrator.hpp:58-61` (AMBIG basename), `libceed/operator.cpp:483` and `:487-488` (MISS) all appear ONLY inside the `fe-assemble-libceed-boundary-obstruction` row, which is reproduced byte-identically in both the `edit:` block (line 257) and the `edit-to:` block (line 260) as unchanged edit-anchor context, and they exist verbatim in the live `book/src/L1-L0/index.md` (pre-existing c055 citations). D2 introduces no new failing citation. The `verified_against:` frontmatter is fenced YAML and round-trips cleanly under `yaml.safe_load` (no leading-quote scalar issue).

**surface-or-evidence — pass.** Not a refinement of an existing operator/theme; this is a NEW L1>L0 lowering theme (`new:` block) carrying its own structural evidence (two grounded source witnesses + the base-class-slot factorization). The surface (theme text) and the rotation_claim (the translation) are co-present and source-grounded. Applicable and satisfied.

**rotation-quality — pass.** The lowering is a genuine vocabulary translation, not a degenerate identity-in-named-terms rename. The non-degeneracy witness is concrete and source-verified: the L1 pure pair's two slots map onto two STRUCTURALLY-DISTINCT L0 carriers — `diff_op` → the compile-time C++ template parameter `T` (a `BilinearFormIntegrator` subclass selected in the type system), `coefficient` → a runtime `MaterialPropertyCoefficient` argument forwarded to the constructor and held on the shared base-class slot `const MaterialPropertyCoefficient *Q` (:42). A pure inert pair value lowers into a template-type-plus-runtime-arg dispatch that heap-allocates (`make_unique<T>`) and mutates a container (`push_back` onto `domain_integs`). The semantic organization genuinely shifts (value → type-system + runtime + heap-ownership); this is the redirect's "translation across vocabularies," not a mirror. The base-class uniformity of `Q` across all variants is correctly identified as the structural ground for the `(coefficient, differential-operator)` factorization (coefficient slot variant-invariant; diff-op slot is the variant axis) — and that uniformity is verified at :42.

**rotation-quality / identity-lowers-vs-kernel-opaque split (focus c) — pass.** The split is correct and the firmness is justified. The term IDENTITY (which `Q`, which `𝒟`) IS Palace-readable at the `AddDomainIntegrator<T>(Q)` instantiation site (`T` names the diff-op, the runtime arg names the coefficient) and lowers cleanly HERE — both witnesses show the correspondence read directly off the source. The integrator KERNEL (`Assemble` quadrature contraction) is correctly routed to the sibling `fe-assemble-libceed-boundary-obstruction` (c055, opaque-library-ownership) and explicitly does NOT lower through this theme. The firm-on-positive-structure justification holds: every claim is read from a positive source site; the identity-translation is a syntactic correspondence, so the absence of a `weak_form_term` unit test does not gate it (correctly analogized to `fe_assemble` and the firm L1 `weak_form_term`). The opaque kernel is the term's argument's classification, independent of the term-identity translation — the reasoning is sound and the firm verdict is warranted.

**variant-axis-coverage — pass.** The variant axes are exhaustively enumerated and each is either grounded or explicitly scoped. Differential-operator axis: `Gradient`/diffusion (Case 1, grounded), `Curl`/curl-curl (Case 2, grounded), `Identity`/mass and `Divergence`/div-div named as pending-pull with their wrapper citations (`:68-69`/`:79-80`, `:122-123`) and explicitly NOT authored (matching D1's pull-only scoping; div-div carries D1's negative anchor — no model-operator instantiates it). Term-position sub-axis (domain vs. boundary `AddBoundaryIntegrator`, `:59-63`) named and noted as same-translation. Mixed/rectangular pairing axis (`MixedVector*Integrator`, `:197,229,250`) explicitly carved out of scope, mirroring the L1 entry. No hidden branches.

**cross-reference-integrity — warning.** The named siblings on disk resolve: `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md`, `fe-operator-assemble-mutation-rotation.md`, `book/src/L1/fe_assemble.md` all exist; the SUMMARY edit-anchor and the index obstruction-row edit-anchor are each unique (count=1), so the surgical inserts will apply cleanly. **The single warning:** the live forward-reference target `book/src/L1/weak_form_term.md` does NOT exist on disk yet — it is D1's output (`new:book/src/L1/weak_form_term.md`), produced in the SAME wave/cycle (identical timestamp `2026-06-02T075145Z`, D1 LEAD). The report uses live links `[...](../L1/weak_form_term.md)` (and `[...](../../book/src/L1/weak_form_term.md)` in the CYCLE preamble), which is the expected dual-registration pattern for an intra-cycle harvester/abstractor pair, BUT it imposes an integration ORDERING constraint: D1 must be applied before D2 or `mdbook build` linkcheck2 will hard-fail on the dead link. This is benign-by-design for same-cycle dual registration, not a content defect — flagging it so the integrator orders D1→D2 (and as a guard in case D1 is rejected/deferred, in which case this link must fall back to plain-text).

**edge-label-fidelity — pass.** Edge label is `layer_from: L1` / `layer_to: L0`; LHS sections are L1 (`## L1 form (LHS)`, the pure pair), RHS sections are L0 (`## L0 form (RHS)`, `AddDomainIntegrator<T>(Q)`), and the prose narrates the rewrite FORWARD from L1 into L0 throughout ("lowers that record FORWARD into its concrete Palace L0 instantiation"). The discussed edge matches the declared edge exactly; high→low direction is correct per the invariant.

**plan-kind-consistency — pass.** Declared `status: firm`, `justification_kind: structural`, kind = L1>L0 lowering theme. Content shape matches: a complete forward-narrated rewrite with two exhaustively-cited grounded witnesses, an explicit applicability scope, and a named-but-deferred pending-pull section (not rough-in placeholders standing in for missing core content — the deferred items are genuinely out-of-pull, correctly scoped, not gaps in the firm claim). No mis-classification.

**skill-uptake-survey — pass.** The report references its mechanical citation procedure (`citecheck --anchor` + `read_range`, per the verify-citation-range mechanical realization) throughout §Verified-against and §Supporting evidence. For a theme proposing a single surgical SUMMARY/index insert with unique anchors, no further skill invocation is implied. Telemetry only.

### Issues found

1. **cross-reference-integrity (warning) — live forward-ref to same-cycle sibling not yet on disk.** Location: CYCLE.md §Summary (line 20, `../../book/src/L1/weak_form_term.md`), the `new:` block body (lines 61, 78, 84-host, 88, 139, 218, 223, 249) and frontmatter `l1_form:` (line 49), plus the index `edit-to:` row (line 261) — all reference `book/src/L1/weak_form_term.md`, which is D1's output (`new:book/src/L1/weak_form_term.md`, same wave, D1 LEAD) and does not exist on disk at critique time. Severity: low / procedural. The links are correct in form and resolve once D1 lands; the only requirement is integration ORDERING (D1 before D2). Repair candidate ONLY if D1 is not integrated this cycle (then these must fall back to plain-text per `rough-in-forward-reference-must-be-plain-text-not-live-link`); otherwise no action needed. Not a defect of D2's content.

(No other issues. All 5 of D2's own load-bearing citations verify exactly; the 3 citecheck-scan failures are pre-existing c055 citations inside the unchanged edit-anchor context, confirmed identical in `edit:`/`edit-to:` and present verbatim in the live index — the abstractor's pre-flag is accurate. The rotation is a genuine non-degenerate vocabulary translation; the identity-lowers/kernel-opaque split and the firm verdict are correctly reasoned and source-grounded.)

## Repair

### Fixes attempted

- **Finding**: cross-reference-integrity (warning) — live forward-ref `book/src/L1/weak_form_term.md` (CYCLE §Summary L20, `new:` block bodies, frontmatter `l1_form:` L49, index `edit-to:` row L261) does not exist on disk at critique time; it is D1's same-wave output (`new:book/src/L1/weak_form_term.md`, identical timestamp `2026-06-02T075145Z`, D1 LEAD).
  - **Decision**: not-needed (resolved-by-construction).
  - **Rationale**: This is the standard same-cycle forward-reference / dual-registration pattern for an intra-cycle harvester/abstractor pair. D1 authored `book/src/L1/weak_form_term.md` this cycle and it lands first in the serial integrator order (D1 LEAD applied before D2). The live links `[...](../L1/weak_form_term.md)` are correct in form and resolve at finalize-rebuild once D1's file is on disk. Downgrading to plain-text would be the *wrong* repair (it would strand a link that D1 makes live this cycle) — per `rough-in-forward-reference-must-be-plain-text-not-live-link`, plain-text is the fallback ONLY when the target won't materialize this cycle, which is not the case here. No content surgery applied.

- **Finding** (subsumed, citation-validity context): 3 `citecheck.py --scan` flags — `integrator.hpp:58-61` (AMBIG), `libceed/operator.cpp:483` + `:487-488` (MISS).
  - **Decision**: not-needed.
  - **Rationale**: Confirmed by the critic as PRE-EXISTING c055 citations living only inside the unchanged `fe-assemble-libceed-boundary-obstruction` anchor-context row, reproduced byte-identically in both the `edit:` (L257) and `edit-to:` (L260) blocks (edit == edit-to) and present verbatim in the live `book/src/L1-L0/index.md`. D2 introduces no new failing citation; this is not a D2 defect and there is nothing to repair.

### Unrepairable findings

None. The sole warning is benign-by-design (same-cycle dual registration) and resolves by integrator ordering; the scan flags are pre-existing verbatim context, not D2 changes.

## Suggested resolution

`overall_status: ready`. Integrator note (ORDERING CONSTRAINT, carried from the critic):

- Apply **D1 (`new:book/src/L1/weak_form_term.md`, LEAD) before D2** in the serial per-report order so the live link `book/src/L1/weak_form_term.md` resolves at the `cargo make book` finalize-rebuild. D1 and D2 share the timestamp `2026-06-02T075145Z`; D1 is the LEAD.
- Guard (only if D1 is rejected/deferred this cycle — not expected): the live references to `book/src/L1/weak_form_term.md` in D2 would then need to fall back to plain-text per `rough-in-forward-reference-must-be-plain-text-not-live-link` to avoid a `linkcheck2` hard-fail. Under the expected D1→D2 ordering, no such fallback is needed.
- The SUMMARY edit-anchor and the index obstruction-row edit-anchor are both unique (count=1), so the surgical inserts apply cleanly.

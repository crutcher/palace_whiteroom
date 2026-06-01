---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T200900Z
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
repaired_at: 2026-06-01T201500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: repaired
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize inner_product at L3"

## Critique

### Checks run

**citation-validity — warning.** The report is a high→low layer-coherence backfill whose L0 anchors are explicitly *inherited, not re-localized* (CYCLE.md:443-446, :609-618) — so I checked (a) that the inherited L0 ranges actually resolve in the firm L2 parent, and (b) that the report's OWN load-bearing pinpoint citations (the ones it emits in its prose / supporting-evidence) are in-range and on-anchor. The inherited L0 anchors all resolve in `book/src/L2/inner_product.md` §Evidence (`vector.cpp:263-267`, `:269-274`, `:664-672`, `operator.cpp:598-617`, `:621-638`, `vector.hpp:247-253`, `test-vector.cpp:206-207`). Two own-pinpoint drifts surface (see Issues): (1) the report reproduces the complex-reduction anchor as `palace/linalg/vector.cpp:664-685` (CYCLE.md:453) while the L2 parent it inherits from cites `:664-672` — an inherited-citation range overstatement; (2) the supporting-evidence pinpoint `book/src/L3/nrm2.md:27-33` (CYCLE.md:566) is mis-attributed — that range in L3/nrm2.md is the §Signature block, not "the `√ ∘ abs ∘ inner_product` CONSUMER framing + do-NOT-merge boundary" the report ascribes to it (the consumer framing in L3/nrm2.md is at :15/:67/:99; the §"Consumer … NOT a fold member" do-NOT-merge section at `:27-33` is in *L2*/nrm2.md, which the very next bullet (CYCLE.md:568) cites correctly). All other own-pinpoints verified in-range and on-anchor: `L3/dot.md:64-68` and `:66` (§"Iteration-rotation marker", carrying the verbatim no-sequential-obstruction verdict the report reproduces), `:127-131` (§"Lowers to"), `L3-L2/krylov-step-body-identity.md:97` (point 3, the seven-primitives L3-native justification), `L3/index.md:12/:15/:29/:48/:62`. No `verified_against:` block in this report (harvester, not lowering-verifier) — the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** Not a refinement of an existing operator's surface — this is a `new:` firm operator entry (the L3 propagation of the firm L2 combinator). The "modify surface OR retroactive-evidence-backfill" gate applies to refinement-shaped proposals; a new layer-coherence entry that inherits its evidence from a firm parent is the legitimate identity-lowering-backfill shape (CLAUDE.md §Methodology invariants "Identity-lowerings still require both L levels"). The entry carries its own L3-native framing (iteration-rotation marker, no-sequential-obstruction verdict) as new surface and a complete inherited-evidence list. Pass.

**rotation-quality — pass.** The declared L3>L2 relationship is *identity-in-form* (value-thread-isomorphic; §"Downward to L2", CYCLE.md:417-431), explicitly NOT claimed as a rotation, and correctly routed to an in-line annotation with no `L3-L2/` theme file per the cycle-012 non-adjacent-identity convention. An identity-in-form claim is not subject to the "must be strictly more compact" rotation bar — that bar applies to asserted rotations. The genuine rotation in the chain (the L2>L1 `inner-product-fold-specialization`, carrying the conjugation re-order + pinned-tree IEEE non-law) is correctly named as the substantive translation and deferred-to, not restated. Pass. (Note: this matches the vocabulary-shift-redirect smell-test — the report does not author a thin mirrored L3>L2 theme; it pre-builds the in-line home the degenerate `dot-body-identity` demotes into at c051.)

**variant-axis-coverage — pass.** Three orthogonal variant axes declared in frontmatter and §"Variant axes": conjugation-convention (hermitian/`tdot`), element-type (real/complex), weight-presence (`M=I` / general-or-SPD-`M`). Each is covered: the conjugation×element-type kernel table (CYCLE.md:164-168) is exhaustive over the {real, complex-hermitian, complex-tdot} cells; the weight axis is the `inner_product_M` / `bilinear_form` member with its own signature and law 7. The diagonal degeneration (`y=x`) is explicitly scoped OUT as a consumer entry point, not a variant axis (CYCLE.md:367-368); the reduction-tree is explicitly scoped OUT as an L0 detail, not an L3 axis. No hidden branch. `tdot`'s type-API-surface-only evidentiary caveat is carried as a member-level note, not a silently-dropped cell. Pass.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: `L2/inner_product.md`, `L2-L1/inner-product-fold-specialization.md`, `L3/dot.md`, `L3/nrm2.md`, `L3/apply_linop.md`, `L3/krylov-step.md`, `L3-L2/krylov-step-body-identity.md`, `concepts/dot.md`, `concepts/sequential-obstruction.md` all present. The L3/index.md row-upgrade (Edit 2) replaces the plain-text `inner_product *(rough-in; no anchor yet)*` row at :29 with a live link `[`inner_product`](./inner_product.md)` — this is correct ONLY because the same dispatch authors the target file (Edit 1, `new:book/src/L3/inner_product.md`); the live link will NOT dangle post-integration. The Edit 2 `<<<OLD>>>` block matches `book/src/L3/index.md:29` verbatim; the Edit 3 SUMMARY.md `<<<OLD>>>` block matches `book/src/SUMMARY.md:32-34` verbatim (dot/nrm2/scal contiguous). Build-readiness fence guard (firm-body-inside-fence): the firm apparatus (`## Status` :393, `## Signature` :138, `## Algebraic laws` :264, `## Evidence` :441) sits INSIDE the `new:` fence (opens :58, closes :498) — no fence-truncation defect. Pass.

**edge-label-fidelity — pass.** The frontmatter `lowers_to:` and the §"Downward to L2" both name the L3>L2 edge, and the prose discusses exactly that edge (L3 form → L2 reduction, identity-in-form). The transitive L3>L1 is correctly framed as L3>L2-identity ∘ L2>L1-substantive, with no spurious `L3-L1/` directory. `lifts_from: (none)` is consistent with the §Context "no L4 inner_product" discussion. No edge-label/prose mismatch. Pass.

**plan-kind-consistency — pass.** Declared kind is a firm L3 operator entry. Content shape matches: full signature, kernel table, conjugation convention, specializations, semantics, 7 algebraic laws + 3 non-laws, dependencies, variant axes, consumer boundary, status, downward, evidence. No rough-in placeholders in the firm body. The `firm` status is justified as the iteration-rotation rendering of a firm L2 parent with inherited laws + a member-level `tdot` caveat that is correctly framed as "not a status reduction" (consistent with the `firm` verdict, not a `partly-constructive` mis-classification). Consolidated tally correctly DEFERRED to D7 (no running count written into the entry or index — verified). Pass.

**skill-uptake-survey — pass (telemetry).** The report's shape (inherited-citation backfill, fence-parity-sensitive proposed-changes) implies `verify-citation-range` (Audit-report / inherited-citation sub-case) and `proposed-changes-fence-encloses-full-body-guard` are relevant. The report self-documents (CYCLE.md:613) that it deliberately did NOT re-run `citecheck` on the inherited L0 ranges (consistent with high→low discipline — they are not re-emitted as load-bearing pinpoints). This is a defensible non-invocation, but it is exactly the choice that let the two own-pinpoint drifts (Issue 1, Issue 2) through unverified — the inherited-citation sub-case of `verify-citation-range` would have caught the `:664-685` vs `:664-672` range mismatch against the L2 parent. Surfaced as telemetry, non-blocking.

### Issues found

1. **Inherited-citation range overstatement: `vector.cpp:664-685` vs parent's `:664-672`.** CYCLE.md:453 (Evidence section) reproduces the complex/real-reduction L0 anchor as `palace/linalg/vector.cpp:664-685`, but the firm L2 parent it inherits from cites `:664-672` consistently (`book/src/L2/inner_product.md:198, :363, :388, :520`). Since this report's stated discipline is "inherit, do not re-localize," the inherited range must match the parent. Severity: low-moderate — the anchor is not re-emitted as a load-bearing pinpoint (it is referenced as "the L2 entry's evidence list"), so it does not gate a claim, but it is an internal inconsistency against the cited authority and would mislead a reader who follows it to L0. Location: CYCLE.md §Evidence, line 453.

2. **Mis-attributed supporting-evidence pinpoint: `L3/nrm2.md:27-33`.** CYCLE.md:566 cites `book/src/L3/nrm2.md:27-33` as "the `√ ∘ abs ∘ inner_product` CONSUMER framing + do-NOT-merge boundary." That range in `L3/nrm2.md` is the §Signature block (`nrm2 :: Tensor[N] -> Scalar` / `nrm2(x) = √⟨x, x⟩`). The L3 nrm2 entry's consumer framing lives at :15 / :67 / :99 and has no dedicated do-NOT-merge §section. The `:27-33` range that IS the §"Consumer … NOT a fold member (load-bearing)" do-NOT-merge section belongs to *L2*/nrm2.md — which the report cites correctly on the very next line (CYCLE.md:568). The most likely fix is to drop or re-anchor the L3 pinpoint (e.g. point at `L3/nrm2.md:99` §"Consumers" or :15). Severity: moderate — this is the citation backing the load-bearing nrm2-stays-consumer boundary, one of the dispatch's special-attention items; the boundary itself is correct and well-supported (the L2 citation and the entry's own §"Consumer (NOT an instance)" at :373-391 are sound), but the L3-side pinpoint is wrong. Location: CYCLE.md §Supporting evidence, line 566.

3. **Duplicate `new:`/`edit:` fence blocks may double-parse at integration.** The §"Proposed changes" overview (CYCLE.md:40-54) uses the same ```` ```new:book/src/L3/inner_product.md ```` / ```` ```edit:... ```` fence syntax for its *preview* blocks (lines 42-44, 46-48, 50-52, each containing only a `[placeholder]`) as the real proposed-changes blocks below (Edit 1 :58-498, Edit 2 :505-511, Edit 3 :518-529). An integrator that parses proposed-changes by fence-tag could match the placeholder block (`[full firm chapter body — see "Operator content" below]`) for `new:book/src/L3/inner_product.md` instead of (or in addition to) the real body at :58. The prose disambiguates ("Full edit bodies are in the fenced blocks below", :54), but the machine-readable fence tags collide. Severity: moderate — a build-readiness hazard, not a content defect; the safe form is to neutralize the preview fences (non-`new:`/`edit:` info-string, or non-fenced) so only the real blocks carry the parseable tags. Location: CYCLE.md:42-52.

4. **(minor) `tdot` weighted-cell coverage asymmetry — not a gap, noted for completeness.** The kernel table (CYCLE.md:164-168) covers conjugation×element-type but the weight axis interacts only with the Hermitian/real members in the signature (`inner_product_M`); there is no `tdot_M` cell. This is correctly implied to be out of scope (Palace exposes no unconjugated weighted form; `tdot` is type-API-surface-only with zero call sites), but the entry does not state the `tdot × weight` combination is scoped out explicitly. Severity: very low — the variant-axis-coverage check passes (the omission is consistent with the inherited L2 profile and the zero-call-site `tdot` caveat); flagged only so the repairer can decide whether a one-line "no unconjugated weighted member in Palace" scope-out is worth adding. Location: CYCLE.md §"Variant axes" / §Signature.

## Repair

### Fixes attempted

- **Finding 1 (citation-validity, low-moderate)**: Inherited-citation range overstatement — D2 reproduced the real/complex reductions as a single `vector.cpp:664-685`, but the firm L2 parent (`book/src/L2/inner_product.md:196-198, :363-364, :388-389, :520-523`) cites the real reduction at `:664-672` (single Hypre `hypre_SeqVectorInnerProd`) and the complex reduction at `:674-685` (four `LocalDot`s) as two distinct ranges.
  - **Decision**: repaired.
  - **Action**: CYCLE.md §Evidence line 452 — rewrote `:664-685 real/complex reductions` to `:664-672 real reduction / :674-685 complex reduction`, faithfully reproducing the parent's split rather than collapsing to a single overstated span. Verified both ranges with `citecheck --anchor`: `:664-672` anchors `hypre_SeqVectorInnerProd` (line 671); `:674-685` anchors `LocalDot` (lines 674/678/682/683). Both in-bounds against `reference/palace/palace/linalg/vector.cpp`.

- **Finding 2 (citation-validity, moderate)**: Mis-attributed pinpoint — D2 cited `L3/nrm2.md:27-33` for the `√ ∘ abs ∘ inner_product` consumer + do-NOT-merge boundary, but that range in `L3/nrm2.md` is the §Signature block (`nrm2 :: Tensor[N] -> Scalar`). The do-NOT-merge §section at `:27-33` belongs to `L2/nrm2.md` (verified: §"Consumer of `inner_product`, NOT a fold member (load-bearing)").
  - **Decision**: repaired.
  - **Action**: CYCLE.md §Supporting evidence line 566 — re-anchored the L3-side pinpoint to `book/src/L3/nrm2.md:67` (the L3 leaf-reduction consumer-role line, verified in-bounds; confirmed by read to carry "`nrm2` is a leaf reduction; the iteration view is what the surrounding `krylov-step` body or outer convergence-test consumer provides") and added a clarifying note that the L3 entry has no dedicated do-NOT-merge §section — that section is at L2, cited (correctly) on the next line (`L2/nrm2.md:27-33`, whose attribution I also tightened to name the §title).

- **Finding 3 (build-readiness, moderate)**: Duplicate `new:`/`edit:` fence double-parse hazard — the §"Proposed changes" preview blocks (CYCLE.md:42-52) reused the same parseable `new:`/`edit:` fence info-strings as the real proposed-changes blocks, so a fence-tag-matching integrator could double-parse and apply the `[placeholder]` preview body (or apply twice).
  - **Decision**: repaired.
  - **Action**: CYCLE.md §"Proposed changes" — collapsed the three preview fenced blocks into a single plain ` ``` ` fence (no `new:`/`edit:` info-string, content rewritten as `new → path` / `edit → path` arrow notation) and prefixed an explicit "Preview only (NOT parseable … the integrator MUST skip these)" banner. Verified post-edit with `grep '^```new:\|^```edit:'`: exactly three parseable blocks remain — the real `new:book/src/L3/inner_product.md` (full firm body, line 60), `edit:book/src/L3/index.md` (line 511), `edit:book/src/SUMMARY.md` (line 524). No double-parse hazard remains. This was the gating fix for build-readiness.

- **Finding 4 (variant-axis, very low)**: `tdot × weight` combination not explicitly scoped out.
  - **Decision**: repaired (trivial scope-out, accurate from the existing prose — Palace exposes no unconjugated weighted member; `tdot` is type-API-surface-only / zero call sites).
  - **Action**: CYCLE.md §"Variant axes" axis-3 (weight presence) — appended a one-line scope-out: the `tdot × weight` cell is scoped out (no `tdot_M`), since `inner_product_M` conjugates arg-1 and `tdot` has zero call sites; the weight axis interacts only with the Hermitian/real conjugation values. No new claim introduced — restates the inherited L2 profile.

### Unrepairable findings

None. All four findings were mechanical/surgical (citation pinpoint corrections faithful to the cited L2 parent, fence-tag neutralization, a one-line scope-out restating existing prose). No substantive content was authored or altered: the L3 operator body, the no-sequential-obstruction verdict, the nrm2-consumer boundary, the §"Downward to L2" identity-in-form annotation, and the dual-registration deferral to D7 were left untouched per the critique's clean assessment.

## Suggested resolution

`ready`. The two citation pinpoints now match the on-disk authority (the firm L2 parent's split real/complex reduction ranges, and the correct L3-vs-L2 attribution of the consumer/do-NOT-merge framing), and the duplicate-fence double-parse hazard is neutralized — only the three intended proposed-changes blocks parse. Integrator notes: (a) the consolidated `L3/index.md:62` count tally is DEFERRED to D7 by design (this report writes only its own dep-map row, Edit 2); (b) the L3 `dot`/`nrm2` leaf re-expression slim + `dot-body-identity` theme demotion is cycle-051 scope — this dispatch introduces no transient broken-link risk (the leaves stay firm with their existing lowerings).

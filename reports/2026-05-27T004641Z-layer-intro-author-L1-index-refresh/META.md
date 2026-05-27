---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T00:55:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
---

# META: verification of L1 index refresh

## Critique

### Checks run

- **citation-validity**: New prose cites `CLAUDE.md` sections and grounds claims in the four firm operator chapters (which carry the file:line evidence). No new L0 citations introduced; existing operator authority preserved. Pass.
- **surface-or-evidence**: Surface modification (index.md prose) framed as curation of already-firm operator content; not a refinement-shaped proposal requiring new rotation evidence. Pass.
- **rotation-quality**: Not applicable — no new rotation claim authored; report curates existing rotation language. Pass (n/a).
- **variant-axis-coverage**: No variant-axis claims in scope; operator-level axes remain in operator chapters. Pass (n/a).
- **cross-reference-integrity**: Verified `axpy.md`, `dot.md`, `nrm2.md`, `axpby.md`, `L2/index.md` (krylov-step row), and open-question slugs `l1-index-refresh-trigger-met`, `scal-primitive-l1-harvest`, `axpby-axpbypcz-next-harvest`, `scalar-promotion-typing-rule` — all resolve. Pass.
- **edge-label-fidelity**: Prose discusses L1 (with explicit L1>L0 deferrals where lowering belongs); references to L2 `krylov-step` consumer match the actual L2 index row. Pass.
- **plan-kind-consistency**: Declared as intro refresh / shell-document curation; content matches (no new operator rows, no firm/rough-in mis-classification). Pass.
- **skill-uptake-survey**: Front-matter explicitly enumerates the 5 active skills and justifies non-invocation per skill. Pass.

### Issues found

- **Minor — Context bullet 4 phrasing** (REPORT §Proposed changes, new Context list, "Pinned reduction tree" bullet): says L1 "records floating-point reduction-tree non-associativity as a **load-bearing** algebraic claim". The firm `dot.md` (Algebraic laws, "Laws that explicitly do not hold") and `nrm2.md` record it as an **explicit non-law / load-bearing caveat**, not a positive algebraic claim. Wording is slightly inverted from how the operator chapters frame it (a load-bearing recorded non-law, not a recorded law). Severity: low.
- **Minor — Vocabulary cohort `nrm2_B` slug missing** (REPORT §Proposed changes, Vocabulary cohort "Queued"): `nrm2_B` is listed without an open-question slug, whereas the other three queued primitives carry slugs. The `nrm2.md` "B-weighted overload" boundary paragraph notes it as forthcoming but does not link a slug; if no slug is filed, the cohort entry is silently undertracked. Severity: low.
- **Minor — `apply_linop` slug also missing** (same subsection): listed without a tracking slug; consumers (L2 krylov-step row) reference it as a dep, so a tracking entry would close the loop. Severity: low.
- **Cosmetic — Open-questions caveat #1** asks whether the same threshold should apply to L2/L3/L4 and recommends inline, but does not propose filing as a new open question (the report says "if not already tracked"). The integrator/meta-phase channel would benefit from an explicit slug here. Severity: cosmetic.

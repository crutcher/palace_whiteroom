---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T031500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-29T033000Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: repaired
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of L2>L1 `inner-product-fold-specialization` (stub → firm)

## Critique

### Checks run

**citation-validity — pass.** Every L0 range was independently re-read via `palace-codemap` `read_range` / `search_text` (no self-verification trust). All 11 ranges check out:
- `vector.cpp:263-274` — `ComplexVector::Dot` (`:263-267`) body is `{Re(x)Re(y)+Im(x)Im(y), (this==&y)?0.0:(Im(x)Re(y)−Re(x)Im(y))}`; `TransposeDot` (`:269-274`) has the **negated** cross-term (`Im(x)Re(y)+Re(x)Im(y)`) and the `2·Im·Re` self-dot return at `:272-273`. Exactly as cited.
- `vector.cpp:664-685` — real `LocalDot` is one `hypre_SeqVectorInnerProd` with `MFEM_ASSERT(x.Size()==y.Size())` at `:667`; complex `LocalDot` (`:674-685`) is the four-real-dot lift with `Im = LocalDot(xi,yr) − LocalDot(xr,yi)` and the `&x==&y` imag=0 fast path at `:679`. Matches.
- `operator.cpp:598-618` — `Norml2(...,B,Bx)` real (`:599-606`) + complex (`:608-618`); the SPD comment "For SPD B, xᴴ B x is real" is at `:612`, the assertion `dot.real() > 0.0 && std::abs(dot.imag()) < 1.0e-9 * dot.real()` at `:615-616`. Exact.
- `operator.cpp:621-638` — real-`Operator` weighted `Dot` allocates `ComplexVector Ax(A.Height())` at `:623`, applies `A` to Re/Im, returns `Dot(comm, Ax, y)`; `ComplexOperator` overload (`:631-638`) applies `A` to `x` directly. Matches.
- `vector.hpp:240-262` — `// Calculate the … inner product yᴴ x or yᵀ x` comments at `:242` (LocalDot) and `:246` (free-function `Dot`); the `Dot = Mpi::GlobalSum ∘ LocalDot` template at `:247-253`; `Norml2 = √|Dot(comm,x,x)|` at `:256-260`. Exact.
- `operator.hpp:386,391` — the `yᴴ A x` weighted doc comments land **exactly** on `:386` (real-`A`) and `:391` (complex-`A`). (Verified explicitly because a line-off was plausible; it is correct.)
- `iterative.cpp:395` — `beta = linalg::Dot(comm, z, r)` exactly, with the `(Br, r)` PCG note at `:396`. Matches the re-order-invisible CG witness.
- `boundarymodeoperator.cpp:85,90` — Poynting diagonal `linalg::Dot(comm, et, *Bttr, et)` at `:85` and cross-coupling `linalg::Dot(comm, en, Atn, et)` (non-Hermitian `Atn`) at `:90`. Exact.
- `nleps.cpp:487,492` (cited in the re-order-invisible witness list) — `std::abs(linalg::Dot(GetComm(), c, c))` at `:487`, `…(v, v)` at `:492`. Both magnitude-projected. Correct.
- `tdot` zero-call-sites — `search_text TransposeDot` over `palace/**` returns exactly two hits: the decl (`vector.hpp:112`) and the def (`vector.cpp:269`). Zero callers confirmed.
- L1 anchors: `dot.md` kernel table `:33-34`/`:35`, arg-1-conjugated convention `:43`, self-dot trick `:49`; `bilinear-form.md` `xᴴ M y` at `:63`, conjugation reconciliation `:119-145`, "no L0 ambiguity" `:155-158`. All resolve in-range.

**surface-or-evidence — pass.** This is a stub→firm promotion of an existing theme home — it modifies surface (the full theme body) and is fully evidence-grounded, not a pure rotation_claim. The three-key dispatch (conjugation kernel / element-type / weight-presence) is each tied to a verified L0 site: the conjugation key to the one-sign difference between `Dot`/`TransposeDot` (`vector.cpp:263-274`), the element-type key to the real-Hypre-pass-vs-four-real-dot split (`:664-685`), the weight key to law-7 plus the open-coded `Ax`-workspace `Dot(comm,x,A,y)` (`operator.cpp:621-638`). The where-invisible-vs-observable claim is grounded in live witnesses: real-projection invisibility at CG `iterative.cpp:395`, `nleps.cpp:487,492`, Poynting diagonal `boundarymodeoperator.cpp:85`; full-complex observability at the non-Hermitian cross-coupling `boundarymodeoperator.cpp:90`. Each leg of the claim has a positive site.

**rotation-quality (CRUX) — pass.** Direction is correctly high→low (one L2 fold LHS → bounded family of L1 leaf call shapes RHS, forward-narrated "re-fuses downward"). It is a genuine rotation, not a 1:1 rename: one L2 `inner_product` fold resolves into three L0 reduction surfaces (real Hypre pass, complex four-real-dot lift, weighted two-stage `Ax` reduction) — the L2 form is strictly more compact (state-hiding: the `Ax` workspace and the reduction tree are absorbed at L2 and reintroduced here). The core conjugate-pair reconciliation is **sound** and I re-derived it independently: `ComplexVector::Dot(y)` body `= (ac+bd, bc−ad) = x·conj(y) = yᴴ x` (receiver = arg-1, the conjugated-arg-2 = `y`); the free-function `linalg::Dot(comm,a,b) = bᴴ a` (arg-2 conjugated, confirmed by the complex-`LocalDot` `Im` sign); so to recover the L1/L2 `xᴴ y` the lowering calls `Dot(comm,y,x)` or `conj(Dot(comm,x,y))`, and the identity `xᴴ y = conj(yᴴ x)` holds exactly. The non-Hermitian-`M` caveat (operand-swap is the faithful form; outer-`conj` only recovers `xᴴ M y` for Hermitian `M`) is correct and matches the non-Hermitian `Atn` witness. The reconciliation is consistent with the corrected `bilinear-form.md:119-145,:155-158` framing — both now assert the L0 source is self-consistent and the contradiction is L0-vs-L1-representation, not L0-internal; the report explicitly echoes this ("contra an earlier framing", `:263-265`). Justification kind `algebraic` is appropriate: the dispatch IS law-7 weight specialization + the kernel-sign keys read as a lowering, plus the value-level conjugate-pair identity verified against the bodies; the reduction-chain flavour is correctly noted as secondary, with the load-bearing residue isolated in the summation-order table.

**variant-axis-coverage — pass.** The three orthogonal dispatch keys map correctly to L1 leaves: conjugation → `dot`(Hermitian)/`tdot`(unconjugated), element-type → real-Hypre vs complex-four-real-dot, weight → `dot` (M=I, law 7) vs `bilinear-form` (general/SPD M). Orthogonality is argued per-axis and the M=I collapse is handled. Both evidentiary caveats are carried explicitly and correctly scoped as member-level (not theme-status) reductions: `tdot` is API-surface-only (zero call sites, verified), and `bilinear-form` is rough-in at L1 with its M-weighted-member arm noted as structurally firm and not gating the theme. No hidden branches; the diagonal `y=x` degeneration and the weighted-member workspace are correctly scoped out as a consumer-entry and a lowering-concern respectively.

**cross-reference-integrity — warning.** All `[link]` targets resolve as files-on-disk: `../L2/inner_product.md`, `../L1/dot.md`, `../L1/bilinear-form.md`, `./linear-combination-fold-specialization.md`, `./chebyshev-iteration-fusion.md`, and the `../L0/*` references all exist in `book/src/`. The warning is on the report's **mischaracterization of the wave-2 ordering hazard**, not a broken link: the Verified-against section (`:480`) and Status (`:489`) frame `book/src/L2/inner_product.md` as "live in `book/` only after dispatch #1 integrates; the integrator resolves the link." That is inaccurate — the file **already exists on disk as a `stub`** (materialized 2026-05-28; `book/src/L2/inner_product.md:3`), so the `mdbook`/`linkcheck2` link `(../L2/inner_product.md)` resolves at build time regardless of dispatch-#1 ordering. The actual ordering hazard the report worried about does not exist; the link is safe by virtue of the pre-existing stub, not by integrator post-resolution. Net effect on the build is benign (no dead link), but the rationale is wrong and should be corrected so a downstream reader does not believe an integrator link-fix step is required here. Secondary sub-issue: the report's detailed claims about *what the L2 entry pins* (arg-1-conjugated `xᴴ y`, laws 3-7, the four hand-offs (a)-(d), the IEEE non-law deferral) reference content NOT present in the on-disk `inner_product.md` stub — that content is dispatch-#1's not-yet-integrated firm body. These are effectively forward-references to a sibling report's pending content; the L0-grounded reconciliation stands on its own verified evidence, but the "as the L2 entry pins" attributions cannot be confirmed against the live artifact at critique time (no-shared-context: I do not read dispatch #1).

**edge-label-fidelity — pass.** The theme carries the L2>L1 edge label throughout, and the prose discusses exactly that edge (L2 `inner_product` fold → L1 `dot`/`tdot`/`bilinear-form`). The dep-map row append target is correct: `book/src/L2-L1/index.md:14` is the `linear-combination-fold-specialization` row (verified), and the new row is appended after it; the row's `L2 anchor`/`L1 anchor`/`status` columns match the table schema (`:11-14`). Forward-narration (LHS = L2, RHS = L1) respects the high→low layer-definition discipline; the reverse-direction lifting note is correctly quarantined to §"Open questions / caveats" as working-note material.

**plan-kind-consistency — pass.** Declared kind is a `firm` theme; the content shape matches — exhaustively cited dispatch rule, verified conjugate-pair identity, summation-order table, applicability conditions, no rough-in placeholders in the structural core. The three proposed-changes blocks are well-formed and mutually consistent: (a) `edit:book/src/L2-L1/inner-product-fold-specialization.md` full rewrite stub→firm, (b) one dep-map row append at `index.md:14`, (c) SUMMARY.md de-stub at `:49`. I verified `SUMMARY.md:49` is exactly `- [inner-product-fold-specialization (stub)](./L2-L1/inner-product-fold-specialization.md)`, so the replace-from/replace-to pair is accurate. The `firm`-with-member-level-caveat shape (the `tdot` API-only note) is the correct maturity tier — not `partly-constructive` (no constructed-from-negative-anchor sub-part) and not down-graded for the rough-in leaf.

**skill-uptake-survey — warning.** The report references `verify-citation-range` (producer-self-verification sub-case) in its Verified-against header and the MCP-first localization path, and names the standard `lowering-verifier` follow-up. Pure presence check (non-blocking): the report's shape — a rotation lowering with a value-level reconciliation — implies `verify-rotation-citation` and/or `propose-rotation` and (given the three orthogonal dispatch keys) `classify-variant-axis` would have been natural to invoke, but none is referenced by name. Surfaced as telemetry only; the underlying verification was clearly done (all ranges check out), so this is a citation-hygiene-of-skill-invocation note, not an evidence gap.

### Issues found

1. **[low — cross-reference-integrity] Inaccurate wave-2 ordering rationale.** `CYCLE.md` Verified-against `:480` and Status `:489` claim `book/src/L2/inner_product.md` is live "only after dispatch #1 integrates; the integrator resolves the link." The file already exists on disk as a `stub` (`book/src/L2/inner_product.md:3`), so the link resolves at build time now. No dead link results, but the stated rationale is wrong — there is no integrator link-fix step required for this reference. Candidate repair: re-word to "the link target exists as a stub today (resolves at build); dispatch #1 promotes the stub→firm, after which the *content* attributions below are confirmable."

2. **[low — citation-validity / surface-or-evidence] L2-entry attributions reference not-yet-integrated content.** The report repeatedly attributes specific firm content to `L2/inner_product` (arg-1-conjugated convention pin, "laws 3-7", "law 5", "law 7", "law 8", the IEEE non-law deferral, the four hand-offs (a)-(d), §"Conjugation convention (pinned)", §"Sibling fold…"). The on-disk `inner_product.md` is a claim-free stub — none of those laws/sections exist there yet (they are dispatch-#1's pending firm body). The L0-grounded core (the conjugate-pair identity and the dispatch keys) is independently verified and stands, but the "as the L2 entry's law N states" cross-citations are forward-references to a sibling report's unintegrated content and cannot be confirmed against the live artifact at critique time. Candidate repair: gate these attributions on dispatch-#1 integration (the integrator should apply this theme only after the inner_product L2 entry firms), or soften to "the L2 entry (firming this cycle, dispatch #1) pins…".

3. **[informational — skill-uptake-survey] Rotation/variant skills not referenced by name.** Given the rotation + three-orthogonal-axis shape, `verify-rotation-citation` / `propose-rotation` / `classify-variant-axis` would be the natural invocations; only `verify-citation-range` and the MCP path are named. Telemetry only — the verification work was evidently performed.

Nothing rejecting. The conjugate-pair reconciliation (the crux) is mathematically sound, L0-verified, and consistent with the corrected `bilinear-form` framing; all 11 L0 ranges are accurate; the proposed-changes are well-formed with correct target lines. The two `low` issues both concern the wave-2 sibling-ordering dependency on dispatch #1 — they bear on *when* the integrator applies this theme and *how the L2-side attributions are worded*, not on the L0-grounded content's validity.

## Repair

### Fixes attempted

- **Finding 1** [cross-reference-integrity, warning]: Inaccurate wave-2 ordering rationale — CYCLE.md framed `book/src/L2/inner_product.md` as live "only after dispatch #1 integrates; the integrator resolves the link", but the file already exists on disk as a `stub` so the link resolves at build now.
  - **Decision**: repaired
  - **Action**: Verified `book/src/L2/inner_product.md:3` reads `Status: stub` (file exists on disk). Re-worded the Verified-against L2 anchor bullet (CYCLE.md §Verified-against, formerly ~`:476-480`): the link target **already exists on disk as a `stub`** today so `(../L2/inner_product.md)` resolves at build now; dispatch #1 flips it stub → firm, it does not create it. Removed the false "the integrator resolves the link" claim. (Did not alter the link form — the existing live link is build-safe against the on-disk stub.)

- **Finding 2** [citation-validity / surface-or-evidence, folded into the warning]: L2-entry attributions ("laws 3-7", the four hand-offs (a)-(d), §"Conjugation convention (pinned)", the IEEE non-law deferral) reference content NOT present in the claim-free on-disk stub — it is dispatch-#1's not-yet-integrated firm body.
  - **Decision**: repaired
  - **Action**: Softened the three load-bearing forward-attributions to credit the sibling report rather than the live artifact:
    (i) §Verified-against L2 anchor bullet — attributions now prefixed "Per the cycle-019 `inner_product` harvester (dispatch #1, sibling report `reports/2026-05-29T024500Z-harvester-inner-product-l2/CYCLE.md`)" and gated "confirmable once dispatch #1 integrates, which the wave-2 serial sequencing applies before this theme".
    (ii) §"The conjugate-pair re-order" header — "the L2 entry hands to this theme" now reads "per the cycle-019 `inner_product` harvester, dispatch #1 … live once dispatch #1 integrates".
    (iii) §"Summation-order recording" header — same "per the cycle-019 `inner_product` harvester, dispatch #1 … live once dispatch #1 integrates" gate on the IEEE-non-law deferral.
    The Summary opening already attributed "firmed in dispatch #1"; remaining in-body `§"..."` references are downstream of these now-attributed source points, not independent live-artifact claims. The L0-grounded core (conjugate-pair identity + the three dispatch keys) is independently verified and untouched.
  - **Rationale for ready (not unrepairable)**: per wave-2 serial sequencing the integrator applies dispatch #1 before dispatch #2, so the attributed content WILL be live at integration; this is a wording/provenance fix (credit the sibling report, gate on integration order), not substantive re-authoring.

- **Finding 3** [skill-uptake-survey, informational/telemetry]: `verify-rotation-citation` / `propose-rotation` / `classify-variant-axis` not referenced by name; only `verify-citation-range` + the MCP path are named.
  - **Decision**: not-needed
  - **Action**: Telemetry only; the critic confirmed the underlying verification was performed (all 11 ranges check out). Naming-hygiene of skill invocation is not a content defect and is out of repair scope (would be authoring, not mechanical). No edit.

### Unrepairable findings

None. Both warnings were rationale/provenance-wording issues fixed surgically; the informational skill-telemetry note needs no fix.

## Suggested resolution

`ready`. The crux (conjugate-pair reconciliation) passed and is L0-verified; the two warnings were mechanical wording fixes now applied. **Integrator note:** apply this theme (dispatch #2) **after** the `inner_product` L2 harvester (dispatch #1) per the wave-2 serial sequencing — the corrected forward-attributions become confirmable live-artifact content at that point (dispatch #1 flips `book/src/L2/inner_product.md` stub → firm). The link `(../L2/inner_product.md)` is build-safe regardless (on-disk stub already resolves). No follow-up agent required.

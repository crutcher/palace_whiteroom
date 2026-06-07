---
agent: lowering-verifier
invoked_at: 2026-06-07T02:27:59Z
scope: L1>L0 theme audit — interpolator-construction-rotation (citation over-range hygiene)
status: pending
inputs:
  - book/src/L1-L0/interpolator-construction-rotation.md
  - book/src/L1/interpolator.md
  - palace/fem/interpolator.cpp:282-310 (cited evidence — the over-range under audit)
  - palace/fem/interpolator.hpp:50-56 (decls)
integrated_at: 2026-06-07T034500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "D2 cycle-119. Applied clean (staging row D2, status applied). Citation over-range hygiene: interpolator.cpp:282-310 → :282-306 at 4 sites across book/src/L1-L0/interpolator-construction-rotation.md + book/src/L1/interpolator.md, plus a verified_against: YAML block append. Pure citation-range correction — no edge/status/node change; graded-stack rank+reachability UNCHANGED. cargo make book EXIT 0, no build-repair. Step-5b all HELD vs c118 baseline. OQ interpolator-cpp-282-310-over-range-fixed RESOLVED-by-landing (producer self-appended; closure is meta-phase authority). Methodology note carried: citecheck --anchor/--scan do NOT catch a range-END over-run; only an on-disk close-brace read does."
---

# CYCLE: Audit interpolator-construction-rotation — citation over-range hygiene

## Summary
Scoped audit-and-fix hygiene pass on the c118-landed `interpolator-construction-rotation` theme.
c118 D3's repairer corrected the report narrative for the second `InterpolateFunction`
(point-list overload) body citation but left the **artifact** blocks carrying the over-range
`palace/fem/interpolator.cpp:282-310`. I verified on-disk via palace-codemap `read_range` +
`citecheck --anchor` that the point-list `InterpolateFunction` body **closes at `:306`** (the
`}` on line 306; `ComputeLineIntegral` starts at `:308`), so `:282-310` over-runs by 4 lines
(307 blank, 308–310 = `ComputeLineIntegral` signature + opening brace). The correct range is
**`:282-306`**, confirming the planner's value. The over-range appears at **4 sites across 2
files**. All other citations in both files are clean (54 total checked across the two files, 0
bounds failures; the 7 adjacent co-cited interpolator.cpp anchors all anchor-verify clean).
Verdict: **partially-supported → fixed** (the cited evidence supports the claim once the range is
narrowed to the actual function body; the as-shipped over-range is a precise-anchor defect, not a
content defect). No content re-authoring; range correction only.

## Per-citation audit

### Citation 1 — point-list InterpolateFunction body (the over-range)
- **Citation (as shipped, 4 sites):** `palace/fem/interpolator.cpp:282-310`
  - `book/src/L1-L0/interpolator-construction-rotation.md:181` (decls list, point-list body)
  - `book/src/L1-L0/interpolator-construction-rotation.md:238` (GSLIB obstruction-anchors line)
  - `book/src/L1/interpolator.md:208` (L1 op decls list, point-list body)
  - `book/src/L1/interpolator.md:329` (L1 op obstruction-anchors line)
- **Theme claim:** this range is the body of the point-list `InterpolateFunction` overload
  (`void InterpolateFunction(const mfem::Vector &xyz, const mfem::GridFunction &U, mfem::Vector &vals, ...)`).
- **Found (on disk, palace/fem/interpolator.cpp):**
  - `:282` — `void InterpolateFunction(const mfem::Vector &xyz, const mfem::GridFunction &U,`
  - `:283` — `                         mfem::Vector &vals, mfem::Ordering::Type ordering)`
  - `:284` — `{`
  - `:285` — `#if defined(MFEM_USE_GSLIB)`
  - `:304` — `  MFEM_ABORT("InterpolateFunction requires MFEM_USE_GSLIB!");`
  - `:305` — `#endif`
  - `:306` — `}`  ← **closing brace of the point-list `InterpolateFunction` body**
  - `:307` — (blank)
  - `:308` — `double ComputeLineIntegral(const mfem::Vector &p1, const mfem::Vector &p2,`  ← next function
  - `:309`–`:310` — `ComputeLineIntegral` continuation + `{`
- **Verdict:** **partially-supports** as shipped (`:282-310` over-runs the function body by 4 lines
  into `ComputeLineIntegral`). **supports** at the corrected range `:282-306`.
- **Notes:** `citecheck --anchor 'InterpolateFunction'` on `:282-306` resolves the anchor at lines
  [282, 304] within range — the signature line and the GSLIB-absent `MFEM_ABORT` message line. This
  is a *semantic* over-range (function-body boundary), not a bounds violation, which is why the
  `--scan` bounds check passed the as-shipped citation; the defect is caught only by reading the
  body boundary (close-brace END line on disk), per the role-spec "range-END / close-brace
  off-by-one needs a direct on-disk Read" discipline.

### Adjacent co-cited anchors (cross-checked, no fix needed)
Cross-checked the other interpolator.cpp anchors co-cited in the same obstruction-anchor lines, since
a body-boundary slip often co-occurs with sibling drift. All clean:
- `:133-280` `InterpolateFunction` (GridFunction overload body) — anchor-ok.
- `:190` / `:293` `FindPointsGSLIB` — anchor-ok at both.
- `:278` / `:304` / `:108` / `:363` `MFEM_ABORT` (GSLIB-absent fallbacks) — anchor-ok at all four.
- `:282` first line of point-list body — anchor-ok (start line is correct; only the END drifted).

## Applicability conditions
This is a hygiene pass on an `obstruction (opaque-library-ownership)` theme — there are no
algebraic lowering applicability conditions to re-walk. The single auditable condition:
- **Condition:** the cited range delimits the Palace-owned point-list `InterpolateFunction` body
  (the marshalling around the opaque GSLIB engine), not adjacent functions.
- **Verifiable:** yes — read the function-body boundary on disk (`read_range` 278–315 + close-brace
  confirm at 306). **Found counter-example:** yes — as-shipped `:282-310` includes `ComputeLineIntegral`
  signature lines 308–310. Corrected to `:282-306`.

## Algebraic laws (if cited)
N/A — obstruction theme; no algebraic-justification steps cited.

## Proposed changes

Four range corrections, `:282-310` → `:282-306`, across two artifact files, plus one fenced
`verified_against:` block appended to the theme. (No content/prose changes.)

```edit:book/src/L1-L0/interpolator-construction-rotation.md
[site 1 — line 181, decls list point-list body]
- replace:
  — point-list interpolation (`interpolator.hpp:56`; body `interpolator.cpp:282-310`).
- with:
  — point-list interpolation (`interpolator.hpp:56`; body `interpolator.cpp:282-306`).

[site 2 — line 238, GSLIB obstruction-anchors line]
- replace:
  GridFunction `:52`, point-list `:56`), `palace/fem/interpolator.cpp:133-280` + `:282-310`
- with:
  GridFunction `:52`, point-list `:56`), `palace/fem/interpolator.cpp:133-280` + `:282-306`

[site 3 — append verified_against block at end of file (after the last "GSLIB facility dedicated obstruction theme" bullet)]

~~~yaml
verified_against:
  - citation: palace/fem/interpolator.cpp:282-306
    verdict: supports
    audited_at: 2026-06-07T02:27:59Z
    note: point-list InterpolateFunction body; corrected from over-range :282-310 which ran 4 lines into ComputeLineIntegral (starts :308); close-brace confirmed on disk at :306
  - citation: palace/fem/interpolator.cpp:133-280
    verdict: supports
    audited_at: 2026-06-07T02:27:59Z
    note: GridFunction-overload InterpolateFunction body; anchor-verified clean
~~~
```

```edit:book/src/L1/interpolator.md
[site 4 — line 208, L1 op decls list point-list body]
- replace:
  `palace/fem/interpolator.cpp:282-310`).
- with:
  `palace/fem/interpolator.cpp:282-306`).

[site 5 — line 329, L1 op obstruction-anchors line]
- replace:
  `palace/fem/interpolator.cpp:133-280` + `:282-310` (`InterpolateFunction` bodies),
- with:
  `palace/fem/interpolator.cpp:133-280` + `:282-306` (`InterpolateFunction` bodies),
```

(The `~~~` triple-tilde above represents the triple-backtick fence delimiter in the actual file —
emit triple-backticks when applying. The YAML block parses clean under
`python3 -c "import yaml; yaml.safe_load(...)"` — mechanically verified before shipping; no `note:`
value begins with a quote of either kind.)

## Supporting evidence
- `palace/fem/interpolator.cpp:278-315` (palace-codemap `read_range`) — function-body boundary:
  point-list `InterpolateFunction` body `:282-306`, `ComputeLineIntegral` begins `:308`.
- `tools/citecheck/citecheck.py "palace/fem/interpolator.cpp:282-306" --anchor 'InterpolateFunction' --show`
  → `[ok]`, anchor at lines [282, 304] within range.
- `citecheck --scan book/src/L1-L0/interpolator-construction-rotation.md` → 27 ok, 0 failing.
- `citecheck --scan book/src/L1/interpolator.md` → 27 ok, 0 failing.
- 7 adjacent interpolator.cpp anchors (`:133-280`, `:190`, `:293`, `:278`, `:304`, `:108`, `:363`)
  → all anchor-ok.

## Open questions / caveats
- **citecheck does not catch semantic body over-range.** `--scan` bounds-checks only (370-line file;
  `:282-310` is in-bounds) and `--anchor` confirms the anchor token is *within* the range, not that
  the END is the function's close brace — both passed the as-shipped over-range. The defect surfaced
  only by reading the close-brace END line on disk. This is the worked instance of the role-spec
  "`--anchor` alone does NOT discharge a range-END / close-brace off-by-one" discipline; no tooling
  change proposed (the on-disk END-read is the established guard), but noting it as the reason the
  c118 finalize shipped the over-range despite a clean `--scan`.
- No direction-of-definition violation, no rank violation: theme is `obstruction
  (opaque-library-ownership)`; both endpoints are the L1 op entry (already obstruction-disposed) and
  L0 source — rank-consistent.
- No other citation drift found in either file.

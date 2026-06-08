---
agent: lifter
invoked_at: 2026-06-08T180000Z
scope: L4 land-clean citation dir-prefix hygiene — sharding-decompose-reduce-citation-prefix-hygiene
status: integrated
integrated_at: 2026-06-08T181500Z
integration_commit: 9ae9dbc840c43dc12f51f623ed1362c3b74c7d99
integration_notes: |
  Applied clean by integrator-per-report (cycle-141 staging row 1/1). Finalize (cycle-141) rebuilt book (cargo make book EXIT 0, 0 build-repairs), step-5c KaTeX $-sigil assertion PASS (class=katex in <pre> = 0 across 392 HTML), step-5b graded-stack linters both block-conditions PASS (rank_violations 0, no newly-orphaned node), all graded-stack totals HELD EXACTLY vs c140 by design (body-prose citation-prefix text edit + within-chapter verified_against yaml append moves no node/edge/rank). Node STAYS rank-0 roadmap_goal. DISCHARGES the c140-flagged below-bar citation-prefix-hygiene caveat. BATCH-CLOSING 3/3 of meta-batch-45; the batch-45 meta-phase fires next (separate dispatch/commit).
inputs:
  - book/src/L4/sharding-decompose-reduce.md
  - reference/palace/palace/utils/geodata.cpp:3242
  - reference/palace/palace/models/romoperator.cpp:586
---

# CYCLE: Re-anchor sharding-decompose-reduce-citation-prefix-hygiene

## Summary
The c140 D1 audit of `book/src/L4/sharding-decompose-reduce.md` flagged (below forced-fix bar, left to land-clean-lifter discretion; see the chapter's own discharge note at `:484` "content correct, path under-qualified") that 3 body-prose bare-basename source citations omit their directory prefix. This is a pure anchor-prefix hygiene touch: the content was already confirmed correct by c140; only the dir-prefix on three inline-code body-prose citations is corrected. The node STAYS rank-0 `roadmap_goal`; no status/rank/edge change; no body-semantics/law/signature touched. I re-anchored to the chapter's already-established body-prose convention (the full `palace/` prefix used at `:295`/`:297`/`:400`), NOT the shorter `models/`/`utils/` form, so the three corrected citations match the rest of the chapter body — codemap-confirmed canonical paths `palace/utils/geodata.cpp` and `palace/models/romoperator.cpp` agree with that convention.

The three affected occurrences:
- `:326` — bare `geodata.cpp:3242` and bare `romoperator.cpp:586` (one line, both)
- `:394` — bare `geodata.cpp:3242`
- `:395` — bare `romoperator.cpp:586`

Citecheck against on-disk source confirms both anchors exact:
- `palace/utils/geodata.cpp:3242` → `[ok]` anchor "partitioning mesh" (the `Mpi::Print("Finished partitioning mesh into {:d} subdomain{}...")` site)
- `palace/models/romoperator.cpp:586` → `[ok]` anchor "overlap" (the `// Check that the ports don't have any overlap.` comment)

I checked the rest of the chapter: lines 295/297/400 (body prose) and 429/433/473/481 (yaml `verified_against` citations) are ALREADY correctly dir-prefixed — left untouched. The only bare-basename body-prose citations in the chapter are the three at 326/394/395; no others need correcting.

## Proposed changes

```edit:book/src/L4/sharding-decompose-reduce.md
[old]:   are the MPI mesh-partitioning `geodata.cpp:3242` and the wave-port ROM overlap `romoperator.cpp:586`,
[new]:   are the MPI mesh-partitioning `palace/utils/geodata.cpp:3242` and the wave-port ROM overlap `palace/models/romoperator.cpp:586`,
```

```edit:book/src/L4/sharding-decompose-reduce.md
[old]:   (`geodata.cpp:3242` "partitioning mesh into N subdomains") and the wave-port ROM overlap
  (`romoperator.cpp:586` "ports don't have any overlap") — neither a domain-decomposition solver. The
[new]:   (`palace/utils/geodata.cpp:3242` "partitioning mesh into N subdomains") and the wave-port ROM overlap
  (`palace/models/romoperator.cpp:586` "ports don't have any overlap") — neither a domain-decomposition solver. The
```

Optional discharge-note append (lifter discretion — INCLUDED): a THIRD `verified_against:` yaml block recording the hygiene fix, separate fence per the existing 2-block convention. Insert immediately after the existing second yaml block's closing fence at `:485`.

```edit:book/src/L4/sharding-decompose-reduce.md
[old]:     note: no-native-DD-preconditioner claim confirmed (no Schwarz anywhere in palace; only overlap site is the wave-port ROM check); chapter cites bare romoperator.cpp:586 omitting the models/ dir prefix — content correct, path under-qualified
```
[new]:     note: no-native-DD-preconditioner claim confirmed (no Schwarz anywhere in palace; only overlap site is the wave-port ROM check); chapter cites bare romoperator.cpp:586 omitting the models/ dir prefix — content correct, path under-qualified

```yaml
verified_against:
  - citation: book/src/L4/sharding-decompose-reduce.md:326,394,395
    verdict: supports
    audited_at: 2026-06-08T180000Z
    note: c141 land-clean dir-prefix hygiene — the 3 body-prose bare-basename citations (geodata.cpp:3242 / romoperator.cpp:586) re-anchored to the chapter's full palace/-prefixed body convention (palace/utils/geodata.cpp:3242, palace/models/romoperator.cpp:586), matching :295/:297/:400; discharges the c140 :484 path-under-qualified note
  - citation: reference/palace/palace/utils/geodata.cpp:3242
    verdict: supports
    audited_at: 2026-06-08T180000Z
    note: citecheck --anchor "partitioning mesh" ok — anchor exact at :3242 (Mpi::Print N-subdomain partition-finished site); confirms re-anchored path resolves on disk
  - citation: reference/palace/palace/models/romoperator.cpp:586
    verdict: supports
    audited_at: 2026-06-08T180000Z
    note: citecheck --anchor "overlap" ok — anchor exact at :586 (the wave-port ROM "ports don't have any overlap" check comment); confirms re-anchored path resolves on disk
```
```

NOTE TO INTEGRATOR: the third edit appends a NEW separate ```yaml fence immediately after the existing block's closing ``` at the current `:485`. The `[new]` content above retains the existing `:484` note line verbatim, then a blank line, then the new fenced yaml block. All three yaml blocks in the file round-trip as clean YAML (no leading-quote-scalar; the new block's `note:` values are plain scalars).

## Discipline notes
- **Bounded prose-correction, evidenced + recorded.** This is the narrowest possible land-clean: only the dir-prefix on 3 inline-code body-prose citations. No body-semantics line, law, signature, or pseudocode touched; no edge moved/re-typed; `status: roadmap_goal` / rank-0 unchanged (per the hard constraints). These are inline-code citations in narrative prose, NOT in an indented pseudocode block — no KaTeX `$`-sigil fence hazard, no fence introduced.
- **Convention choice.** The dispatch named `models/romoperator.cpp` / `utils/geodata.cpp` as the codemap-canonical forms; I used the FULL `palace/`-prefixed form (`palace/models/...`, `palace/utils/...`) because that is the chapter's OWN established body-prose convention (`:295`/`:297`/`:400` all use `palace/utils/geodata.cpp`). Matching the in-chapter convention keeps the body internally consistent; the canonical paths agree (codemap root-relative `palace/utils/geodata.cpp` and `palace/models/romoperator.cpp`).
- **Self-verified both anchors before emitting** (citecheck `--anchor`, on-disk read): `palace/utils/geodata.cpp:3242` ↔ "partitioning mesh" `[ok]`; `palace/models/romoperator.cpp:586` ↔ "overlap" `[ok]`. Both are terminal source homes (Palace L0), not relocated-dangle targets.
- Discharges the c140 audit residue recorded in the chapter's own `verified_against` block at `:484`.

## Supporting evidence
- c140 audit residue: `book/src/L4/sharding-decompose-reduce.md:481-484` (the `partially-supports` note flagging the under-qualified `romoperator.cpp:586` path).
- On-disk anchor confirmation: `palace/utils/geodata.cpp:3242` (Mpi::Print N-subdomain partition site), `palace/models/romoperator.cpp:586` (wave-port ROM overlap-check comment).

## Open questions / caveats
None. The fix is mechanical and content-preserving; the c140 audit already confirmed the surrounding content correct, so no abstractor reread is implicated.

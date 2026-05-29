# citecheck

Mechanical citation-range checker for the Palace dissection. Validates
`path:lo-hi` (or `path:N`) citations against the local `reference/` source
checkout (and the `book/src/` artifact for intra-book cross-references).

**Why it exists.** Friction-ledger `producer-citation-drift-verify-not-self-invoked`
recurred as a stable 3-cycle pattern across batch-5 (cycles 019/020/021):
pinpoint citations land ±1–2 lines off while the wide range stays correct. The
drift is always caught downstream (critic / repairer / lowering-verifier
re-reads) but costs a repair round each time and occasionally produces
critic↔repairer↔verifier disagreement. This tool is the **recurrence-4
enactment** of the batch-3 ASK: a deterministic line-map the producer, critic,
repairer, and verifier all share, so a citation is mechanically confirmed to
point where (and at what) it claims before integration.

**What it is / isn't.** It is a *lint*: it confirms a citation resolves, is
in-bounds, and — with an anchor — points at the expected token, reporting drift
with a suggested corrected range. It is *not* a semantic checker: it cannot
confirm the cited lines *mean* what the prose claims. Pair it with reading.

No third-party dependencies — Python 3.10+ stdlib only, **no venv required**.

## Usage

```bash
# Run from anywhere; the repo root (the dir holding reference/) is auto-detected.
python3 tools/citecheck/citecheck.py <args>
```

### Bounds check (one or more inline citations)
```bash
python3 tools/citecheck/citecheck.py palace/linalg/orthog.hpp:18-90 \
                                     palace/linalg/vector.cpp:259
```
Reports `OK` / `OOB` (out of bounds) / `MISS` (no such file) / `AMBIG` (a bare
basename matching several files — use a full path).

### Anchor drift check (the pinpoint-drift catch)
Give the token the citation is supposed to point at; the tool finds where it
actually is and flags drift with a suggested range:
```bash
python3 tools/citecheck/citecheck.py palace/linalg/vector.cpp:667 \
        --anchor 'MFEM_ASSERT(x.Size() == y.Size()'
# [DRIFT] palace/linalg/vector.cpp:667 ... anchor at line 668, +1 outside range
#         suggested: palace/linalg/vector.cpp:668
```
`--regex` treats the anchor as a regular expression. `--show` prints the cited
source lines for eyeball verification.

### Scan a CYCLE.md / markdown file (pre-integration bounds lint)
Extracts every `path:lo-hi` token and bounds-checks each (drift needs anchors,
which prose doesn't carry — so scan is a bounds + path-hygiene lint):
```bash
python3 tools/citecheck/citecheck.py --scan reports/<id>/CYCLE.md --quiet
```
`--quiet` prints only failing citations. Exit code is non-zero if any citation
fails — use it as a pre-integration gate.

### Batch mode (citations + anchors)
One citation per line, optional `<TAB>anchor` (prefix `re:` for a regex);
`#` comments and blank lines skipped. `-` reads stdin:
```bash
printf 'palace/linalg/orthog.hpp:35\tLocalDot\n' | \
  python3 tools/citecheck/citecheck.py --batch -
```

### JSON output
`--json` emits a machine-readable array (status, resolved path, anchor lines,
suggested correction) for downstream tooling / agent consumption.

## Path resolution

Citation paths resolve, in order, against: the repo root directly (so
`book/src/L2/index.md` works), then `reference/palace`, `reference/bunsen`,
`reference/burn`, `reference`, and `book/src`. Palace source citations
(`palace/linalg/foo.cpp`, `test/unit/bar.cpp`) resolve under `reference/palace/`.

Bare basenames (`vector.cpp:259`) — the shorthand agents use in prose after
giving the full path once — resolve by unique-match search over a basename
index. A basename matching multiple files (`operator.cpp` → `linalg/` vs
`fem/libceed/`; `dot.md` → `L1/`/`L3/`/`concepts/`) returns `AMBIG`: that is a
real citation-hygiene signal — write the full path.

Override the primary source root with `--ref-root`, or the repo root with
`--project-root`.

## Statuses

| status | meaning |
|--------|---------|
| `OK`    | file resolves; range in bounds; (if anchor given) anchor within range |
| `DRIFT` | anchor found, but outside the cited range — suggested range emitted |
| `OOB`   | range out of file bounds (off the end, or `lo > hi`) |
| `MISS`  | no file resolves for the path |
| `AMBIG` | bare basename matches multiple files — use a full path |
| `NOANC` | anchor given but not present anywhere in the file (wrong file, or anchor text drifted) |

## Suggested integration points

- **Producers** (harvester / abstractor / lifter / layer-intro-author): run
  `--scan` on your own CYCLE.md before emitting, and `--anchor` on the
  load-bearing pinpoints, to self-verify (the producer self-verify Discipline
  bullets). A clean scan is the mechanical half of `verify-citation-range`.
- **Critic / lowering-verifier**: `--anchor` the citations under audit instead
  of re-reading by hand — the tool is the shared authoritative line-map that
  prevents critic↔repairer↔verifier line-number disagreement.
- **Integrator (pre-apply)**: `--scan` the report as a bounds + path-hygiene
  gate; `AMBIG`/`MISS`/`OOB` are blocking, `DRIFT` routes to a repairer fix.

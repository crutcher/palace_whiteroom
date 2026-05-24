# palace-whiteroom-orchestrator

Per-cycle and meta-cycle agent loop. BOOTSTRAP.md Phase 5.

Calls the five role agents (Planner, Explorer, Synthesizer, Critic, Meta-Critic) via the Anthropic Python SDK, talks to the Phase 1 codemap MCP server over stdio for source navigation, and commits one git commit per cycle. Reads `config.toml` at repo root for model assignment, token budgets, and meta-cycle cadence.

## Setup

```bash
cd orchestrator
python -m venv .venv
. .venv/bin/activate
pip install -e .
```

Requires:

- Python 3.11+ (uses `tomllib` built-in).
- `ANTHROPIC_API_KEY` env var set (for the four Opus-class roles and the Haiku Planner).
- `mcp/codemap/target/release/palace-codemap` built (`cd mcp/codemap && cargo build --release` from repo root).

## Run

```bash
# One cycle, then exit. The minimum exercise of the loop.
python -m orchestrator --one-cycle

# Continuous run; meta-reviews fire automatically every N cycles
# (per config.toml's meta_review_every_n_cycles).
python -m orchestrator --continuous

# Dry-run: exercise the plumbing without making real API calls.
# Uses canned per-role responses; useful for verifying file I/O,
# diff application, commit logic, MCP wiring without spending tokens.
python -m orchestrator --one-cycle --dry-run

# Force-fire a meta-review (independent of the cycle counter).
python -m orchestrator --meta-review
```

The loop pauses on meta-review trigger and writes `meta-review-pending.md` to the repo root with the proposed refinement plan. Approval is **file-based**: edit the marker at the bottom of `meta-review-pending.md` to `APPROVAL: APPROVED` (or `REJECTED`) and re-invoke the orchestrator — it picks up where it left off.

## Architecture

```
orchestrator/
├── __init__.py
├── __main__.py    — `python -m orchestrator`
├── cli.py         — Click-based CLI
├── config.py      — Loads config.toml
├── schemas.py     — Loads + validates against schemas/*.json
├── state.py       — File I/O: questions, lessons, episodic.jsonl, LOG.md,
│                    book/src/, git commit
├── log_entry.py   — Formats and prepends LOG.md entries
├── mcp_client.py  — MCP stdio client for the codemap server
├── roles.py       — call_planner / call_explorer / call_synthesizer /
│                    call_critic / call_meta_critic — each role's Anthropic
│                    API call with prompt loading + response parsing
└── loop.py        — run_normal_cycle + run_meta_review + main_loop
```

## Hard invariants (per BOOTSTRAP.md)

- All five roles run in **separate API calls with separate system prompts and isolated contexts**. No conversation reuse.
- Critic sees the Synthesizer's claims and cited source, **never the Synthesizer's chain-of-thought**.
- Meta-Critic sees meta-cycle inputs and prior meta-review records, **never the per-cycle agents' chains-of-thought**.
- `read_range` is the only source-returning MCP tool. Explorer must navigate first.
- **Commit every cycle, pass or fail.** Git history is the audit trail.
- The normal loop **pauses fully** during meta-review. No new cycles between trigger-fire and enactment.

## Token cost ballpark

Rough per-cycle estimate (Opus 4.7 pricing; Haiku for Planner):

- Planner: ~2k tokens (Haiku — cheap).
- Explorer: ~10-20k input + 2-5k output (Opus — most expensive single call).
- Synthesizer: ~10-15k input + 2-5k output (Opus).
- Critic: ~10-15k input + 2-5k output (Opus).

A single cycle is roughly $0.30-1.00. A 10-cycle continuous run is ~$5-10. Meta-reviews are similar to a single Opus call.

Watch `episodic.jsonl` for `tokens_in` / `tokens_out` per cycle; the Meta-Critic flags drift over the friction window.

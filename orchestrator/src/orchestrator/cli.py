"""Click CLI for the orchestrator."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import click

from .config import load_config
from .loop import main_loop
from .schemas import load_schemas
from .state import State


def _resolve_repo_root() -> Path:
    """Walk up from CWD looking for config.toml; or use the env override."""
    override = os.environ.get("PALACE_WHITEROOM_ROOT")
    if override:
        return Path(override).resolve()
    cwd = Path.cwd().resolve()
    for ancestor in [cwd, *cwd.parents]:
        if (ancestor / "config.toml").is_file() and (ancestor / "BOOTSTRAP.md").is_file():
            return ancestor
    raise click.ClickException(
        "Could not find palace-whiteroom repo root. Run from inside the repo "
        "or set PALACE_WHITEROOM_ROOT."
    )


@click.command()
@click.option("--one-cycle", is_flag=True, help="Run a single cycle, then exit.")
@click.option("--continuous", is_flag=True, help="Run cycles until interrupted or meta-review pause.")
@click.option("--meta-review", "meta_only", is_flag=True, help="Force-fire a meta-review independent of the cycle counter.")
@click.option("--dry-run", is_flag=True, help="Mock the Anthropic API; exercise plumbing without spending tokens.")
def main(one_cycle: bool, continuous: bool, meta_only: bool, dry_run: bool) -> None:
    if sum([one_cycle, continuous, meta_only]) != 1:
        raise click.ClickException(
            "Pick exactly one of --one-cycle, --continuous, --meta-review."
        )

    repo_root = _resolve_repo_root()
    config_path = repo_root / "config.toml"
    cfg = load_config(config_path)
    schemas = load_schemas(repo_root)
    state = State(repo_root=repo_root)

    client = None
    if not dry_run:
        try:
            from anthropic import Anthropic
        except ImportError:
            raise click.ClickException("anthropic SDK not installed; install via `pip install -e .`")
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise click.ClickException(
                "ANTHROPIC_API_KEY not set. Either export it or pass --dry-run."
            )
        client = Anthropic()

    mcp_binary = repo_root / "mcp/codemap/target/release/palace-codemap"
    if not dry_run and not mcp_binary.is_file():
        raise click.ClickException(
            f"MCP codemap binary not found at {mcp_binary}. "
            "Run `cd mcp/codemap && cargo build --release` first, or use --dry-run."
        )

    try:
        main_loop(
            cfg=cfg,
            state=state,
            schemas=schemas,
            client=client,
            mcp_binary=mcp_binary if not dry_run else None,
            config_path=config_path,
            one_cycle=one_cycle,
            meta_only=meta_only,
            dry_run=dry_run,
        )
    except KeyboardInterrupt:
        click.echo("interrupted", err=True)
        sys.exit(130)


if __name__ == "__main__":
    main()

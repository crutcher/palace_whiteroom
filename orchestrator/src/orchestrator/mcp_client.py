"""Async MCP stdio client wrapping the Phase 1 codemap server.

Usage:

    async with CodemapClient(binary_path, config_path) as cmc:
        tools = await cmc.list_tools()
        result = await cmc.call_tool("list_files", {"glob": "palace/linalg/*.cpp"})

The MCP session lifetime is bounded by the async-context-manager; the codemap
binary is spawned on `__aenter__` and torn down on `__aexit__`.
"""

from __future__ import annotations

import json
from contextlib import AsyncExitStack
from pathlib import Path
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class CodemapClient:
    def __init__(self, binary_path: Path, config_path: Path) -> None:
        self.binary_path = binary_path
        self.config_path = config_path
        self._stack: AsyncExitStack | None = None
        self._session: ClientSession | None = None

    async def __aenter__(self) -> "CodemapClient":
        self._stack = AsyncExitStack()
        params = StdioServerParameters(
            command=str(self.binary_path),
            args=["--config", str(self.config_path)],
        )
        read, write = await self._stack.enter_async_context(stdio_client(params))
        self._session = await self._stack.enter_async_context(ClientSession(read, write))
        await self._session.initialize()
        return self

    async def __aexit__(self, *_exc: Any) -> None:
        if self._stack is not None:
            await self._stack.aclose()
        self._stack = None
        self._session = None

    @property
    def session(self) -> ClientSession:
        if self._session is None:
            raise RuntimeError("CodemapClient not initialized — use `async with` to enter")
        return self._session

    async def list_tools(self) -> list[dict[str, Any]]:
        """Return the 7 tools in Anthropic-API tool format.

        Anthropic's `tools=` parameter wants {name, description, input_schema}.
        The MCP `list_tools` response carries `name`, `description`, and
        `inputSchema` (camelCase) — we rekey to snake_case for Anthropic.
        """
        result = await self.session.list_tools()
        out: list[dict[str, Any]] = []
        for tool in result.tools:
            out.append({
                "name": tool.name,
                "description": tool.description or "",
                "input_schema": tool.inputSchema or {"type": "object", "properties": {}},
            })
        return out

    async def call_tool(self, name: str, arguments: dict) -> Any:
        """Invoke an MCP tool and return its result as a Python value.

        rmcp wraps non-text return types in JSON; for text the result is a
        single TextContent with `.text`. We decode JSON when the text looks
        like JSON; otherwise return the raw string.
        """
        result = await self.session.call_tool(name, arguments)
        if result.isError:
            raise RuntimeError(f"MCP tool {name} returned error: {result.content}")
        # Result content is a list of content blocks; for our codemap tools
        # there's always one TextContent.
        if not result.content:
            return None
        first = result.content[0]
        text = getattr(first, "text", None)
        if text is None:
            return first  # unknown content type — let caller introspect
        # Try to decode as JSON; the rmcp Json<T> return wraps everything that's
        # not a plain string.
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return text

"""MCP server for plantfyi."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from plantfyi.api import PlantFYI

mcp = FastMCP("plantfyi")


@mcp.tool()
def search_plantfyi(query: str) -> dict[str, Any]:
    """Search plantfyi.com for content matching the query."""
    with PlantFYI() as api:
        return api.search(query)

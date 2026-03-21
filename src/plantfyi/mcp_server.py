"""MCP server for plantfyi — AI assistant tools for plantfyi.com.

Run: uvx --from "plantfyi[mcp]" python -m plantfyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PlantFYI")


@mcp.tool()
def list_families(limit: int = 20, offset: int = 0) -> str:
    """List families from plantfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from plantfyi.api import PlantFYI

    with PlantFYI() as api:
        data = api.list_families(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No families found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_family(slug: str) -> str:
    """Get detailed information about a specific family.

    Args:
        slug: URL slug identifier for the family.
    """
    from plantfyi.api import PlantFYI

    with PlantFYI() as api:
        data = api.get_family(slug)
        return str(data)


@mcp.tool()
def list_climate_zones(limit: int = 20, offset: int = 0) -> str:
    """List climate_zones from plantfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from plantfyi.api import PlantFYI

    with PlantFYI() as api:
        data = api.list_climate_zones(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No climate_zones found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_plant(query: str) -> str:
    """Search plantfyi.com for plant families, species, and climate zones.

    Args:
        query: Search query string.
    """
    from plantfyi.api import PlantFYI

    with PlantFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()

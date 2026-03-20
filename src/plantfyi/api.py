"""HTTP API client for plantfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install plantfyi[api]``

Usage::

    from plantfyi.api import PlantFYI

    with PlantFYI() as api:
        items = api.list_climate_zones()
        detail = api.get_climate_zone("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class PlantFYI:
    """API client for the plantfyi.com REST API.

    Provides typed access to all plantfyi.com endpoints including
    list, detail, and search operations.

    Args:
        base_url: API base URL. Defaults to ``https://plantfyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://plantfyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_climate_zones(self, **params: Any) -> dict[str, Any]:
        """List all climate zones."""
        return self._get("/api/v1/climate-zones/", **params)

    def get_climate_zone(self, slug: str) -> dict[str, Any]:
        """Get climate zone by slug."""
        return self._get(f"/api/v1/climate-zones/" + slug + "/")

    def list_comparisons(self, **params: Any) -> dict[str, Any]:
        """List all comparisons."""
        return self._get("/api/v1/comparisons/", **params)

    def get_comparison(self, slug: str) -> dict[str, Any]:
        """Get comparison by slug."""
        return self._get(f"/api/v1/comparisons/" + slug + "/")

    def list_countries(self, **params: Any) -> dict[str, Any]:
        """List all countries."""
        return self._get("/api/v1/countries/", **params)

    def get_country(self, slug: str) -> dict[str, Any]:
        """Get country by slug."""
        return self._get(f"/api/v1/countries/" + slug + "/")

    def list_distributions(self, **params: Any) -> dict[str, Any]:
        """List all distributions."""
        return self._get("/api/v1/distributions/", **params)

    def get_distribution(self, slug: str) -> dict[str, Any]:
        """Get distribution by slug."""
        return self._get(f"/api/v1/distributions/" + slug + "/")

    def list_families(self, **params: Any) -> dict[str, Any]:
        """List all families."""
        return self._get("/api/v1/families/", **params)

    def get_family(self, slug: str) -> dict[str, Any]:
        """Get family by slug."""
        return self._get(f"/api/v1/families/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_glossary_categories(self, **params: Any) -> dict[str, Any]:
        """List all glossary categories."""
        return self._get("/api/v1/glossary-categories/", **params)

    def get_glossary_category(self, slug: str) -> dict[str, Any]:
        """Get glossary category by slug."""
        return self._get(f"/api/v1/glossary-categories/" + slug + "/")

    def list_guide_series(self, **params: Any) -> dict[str, Any]:
        """List all guide series."""
        return self._get("/api/v1/guide-series/", **params)

    def get_guide_sery(self, slug: str) -> dict[str, Any]:
        """Get guide sery by slug."""
        return self._get(f"/api/v1/guide-series/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_orders(self, **params: Any) -> dict[str, Any]:
        """List all orders."""
        return self._get("/api/v1/orders/", **params)

    def get_order(self, slug: str) -> dict[str, Any]:
        """Get order by slug."""
        return self._get(f"/api/v1/orders/" + slug + "/")

    def list_plants(self, **params: Any) -> dict[str, Any]:
        """List all plants."""
        return self._get("/api/v1/plants/", **params)

    def get_plant(self, slug: str) -> dict[str, Any]:
        """Get plant by slug."""
        return self._get(f"/api/v1/plants/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> PlantFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

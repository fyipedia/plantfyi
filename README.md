# plantfyi

[![PyPI version](https://agentgif.com/badge/pypi/plantfyi/version.svg)](https://pypi.org/project/plantfyi/)
[![Python](https://img.shields.io/pypi/pyversions/plantfyi)](https://pypi.org/project/plantfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.org/project/plantfyi/)

Python API client for the world's plant taxonomy and botanical data. Access 379,774 plant species across 734 families and 50 orders, with taxonomic classification, climate zone mapping, geographic distribution, and species comparison data — all through a clean REST API with zero core dependencies.

Extracted from [PlantFYI](https://plantfyi.com/), a botanical reference platform cataloging the plant kingdom with taxonomy aligned to the [APG IV](https://en.wikipedia.org/wiki/APG_IV_system) classification system, distribution data from [WCSP](https://wcsp.science.kew.org/) and [POWO](https://powo.science.kew.org/), and cultivation guides used by botanists, horticulturists, and plant enthusiasts worldwide.

> **Explore plant data at [plantfyi.com](https://plantfyi.com/)** — browse [plants](https://plantfyi.com/plants/), [families](https://plantfyi.com/families/), [orders](https://plantfyi.com/orders/), [climate zones](https://plantfyi.com/climate-zones/), and [distribution data](https://plantfyi.com/distributions/).

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/plantfyi/main/demo.gif" alt="plantfyi demo — plant taxonomy lookup, family browsing, and botanical search in Python" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You Can Do](#what-you-can-do)
  - [Plant Taxonomy and APG IV](#plant-taxonomy-and-apg-iv)
  - [Plant Families](#plant-families)
  - [Climate Zones and Cultivation](#climate-zones-and-cultivation)
  - [Geographic Distribution](#geographic-distribution)
  - [Species Comparison](#species-comparison)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [API Reference](#api-reference)
- [Learn More About Plants](#learn-more-about-plants)
- [Nature FYI Family](#nature-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

## Install

```bash
pip install plantfyi                # Core (zero deps)
pip install "plantfyi[cli]"         # + Command-line interface (typer, rich)
pip install "plantfyi[mcp]"         # + MCP server for AI assistants
pip install "plantfyi[api]"         # + HTTP client for plantfyi.com API
pip install "plantfyi[all]"         # Everything
```

Or run instantly without installing:

```bash
uvx --from plantfyi plantfyi search "orchid"
```

## Quick Start

```python
from plantfyi.api import PlantFYI

with PlantFYI() as api:
    # Search across all plant species
    results = api.search("sunflower")
    print(results)

    # Get detailed information for a specific plant
    plant = api.get_plant("helianthus-annuus")
    print(plant["name"])  # Helianthus annuus

    # Browse plant families — 734 families
    families = api.list_families()
    print(families["count"])  # 734

    # Explore climate zones for cultivation
    zones = api.list_climate_zones()
    print(zones["count"])
```

## What You Can Do

### Plant Taxonomy and APG IV

The plant kingdom contains approximately 379,774 known species, organized into 50 orders and 734 families. Modern plant classification follows the **APG IV** (Angiosperm Phylogeny Group IV, 2016) system, which uses molecular phylogenetic data rather than morphology alone to determine evolutionary relationships.

| Division | Orders | Species | Description |
|----------|--------|---------|-------------|
| **Angiosperms** (flowering plants) | 64 | ~370,000 | Produce flowers and enclosed seeds |
| **Gymnosperms** (conifers, etc.) | 4 | ~1,000 | Naked seeds, no flowers |
| **Ferns and Allies** | 4 | ~10,500 | Spore-producing vascular plants |
| **Mosses and Liverworts** | — | ~20,000 | Non-vascular, spore-producing |

The APG IV system groups flowering plants into **monocots** (grasses, orchids, palms — one seed leaf) and **eudicots** (roses, oaks, sunflowers — two seed leaves), with several basal lineages like water lilies and magnolias.

```python
from plantfyi.api import PlantFYI

with PlantFYI() as api:
    # Browse all 50 plant orders
    orders = api.list_orders()
    for order in orders["results"][:5]:
        print(f"{order['name']}")

    # Get details for a specific order
    order = api.get_order("rosales")
    print(order["name"])  # Rosales (roses, elms, figs, hemp)
```

Learn more: [Plant Species](https://plantfyi.com/plants/) · [Plant Orders](https://plantfyi.com/orders/) · [Botanical Glossary](https://plantfyi.com/glossary/)

### Plant Families

The 734 plant families represent distinct evolutionary lineages sharing common ancestry. Some families are enormously diverse while others contain only a handful of species. The largest families alone account for over half of all flowering plant species.

| Family | Common Name | Species | Key Features |
|--------|-------------|---------|-------------|
| **Asteraceae** | Daisy/Composite | ~32,000 | Composite flower heads (sunflowers, daisies) |
| **Orchidaceae** | Orchid | ~28,000 | Complex flowers, mycorrhizal dependence |
| **Fabaceae** | Legume/Pea | ~20,000 | Nitrogen fixation, pod fruits |
| **Poaceae** | Grass | ~12,000 | Hollow stems, cereal crops (wheat, rice) |
| **Rubiaceae** | Coffee | ~13,500 | Opposite leaves, includes coffee and quinine |
| **Lamiaceae** | Mint | ~7,000 | Square stems, aromatic oils (basil, lavender) |
| **Rosaceae** | Rose | ~4,800 | Fruits (apple, cherry, strawberry) |
| **Brassicaceae** | Mustard/Cabbage | ~3,700 | Cruciform flowers, glucosinolates |
| **Solanaceae** | Nightshade | ~2,700 | Alkaloids (tomato, potato, tobacco) |
| **Cactaceae** | Cactus | ~1,700 | Succulence, spines, CAM photosynthesis |

```python
from plantfyi.api import PlantFYI

with PlantFYI() as api:
    # Browse all 734 plant families
    families = api.list_families()
    print(families["count"])  # 734

    # Get details for a specific family
    orchid = api.get_family("orchidaceae")
    print(orchid["name"])  # Orchidaceae
```

Learn more: [Plant Families](https://plantfyi.com/families/) · [Guides](https://plantfyi.com/guides/)

### Climate Zones and Cultivation

Plant distribution is primarily governed by climate — temperature range, precipitation, frost dates, and photoperiod. The USDA Plant Hardiness Zone system divides regions into zones based on minimum winter temperature, while the Koppen climate classification maps global climate patterns that determine which plants can thrive where.

| Hardiness Zone | Min Winter Temp | Example Plants |
|---------------|-----------------|----------------|
| **Zone 3** (-40 to -34C) | Siberian iris, birch, spruce |
| **Zone 5** (-29 to -23C) | Roses, lilacs, apple trees |
| **Zone 7** (-18 to -12C) | Camellias, crape myrtle, figs |
| **Zone 9** (-7 to -1C) | Citrus, bougainvillea, palms |
| **Zone 11** (4 to 10C) | Tropical orchids, plumeria, mangoes |

Plants also differ in photosynthesis pathways — **C3** (most plants, temperate), **C4** (grasses, tropical crops like corn and sugarcane), and **CAM** (succulents, cacti) — each adapted to different light and water conditions.

```python
from plantfyi.api import PlantFYI

with PlantFYI() as api:
    # Browse climate zones
    zones = api.list_climate_zones()
    for z in zones["results"][:5]:
        print(z["name"])

    # Get details for a specific climate zone
    zone = api.get_climate_zone("tropical-rainforest")
    print(zone["name"])  # Tropical Rainforest
```

Learn more: [Climate Zones](https://plantfyi.com/climate-zones/) · [Guides](https://plantfyi.com/guides/)

### Geographic Distribution

PlantFYI maps plant species to their native and introduced ranges across countries and botanical regions. Understanding plant distribution reveals biogeographic patterns — why certain families dominate in specific regions (e.g., Proteaceae in Australia and South Africa, cacti in the Americas).

```python
from plantfyi.api import PlantFYI

with PlantFYI() as api:
    # Browse distribution data
    distributions = api.list_distributions()
    print(distributions["count"])

    # Browse plants by country
    countries = api.list_countries()
    brazil = api.get_country("brazil")
    print(brazil["name"])  # Brazil — highest plant diversity on Earth
```

Learn more: [Plant Distributions](https://plantfyi.com/distributions/) · [Countries](https://plantfyi.com/countries/)

### Species Comparison

PlantFYI provides side-by-side comparisons of similar or commonly confused plant species, covering morphological differences, growing conditions, uses, and geographic overlap.

```python
from plantfyi.api import PlantFYI

with PlantFYI() as api:
    # Browse plant comparisons
    comparisons = api.list_comparisons()
    for comp in comparisons["results"][:3]:
        print(comp["name"])

    # Get a specific comparison
    comp = api.get_comparison("basil-vs-thai-basil")
    print(comp["name"])
```

Learn more: [Plant Comparisons](https://plantfyi.com/glossary/) · [Botanical Guides](https://plantfyi.com/guides/)

## Command-Line Interface

```bash
pip install "plantfyi[cli]"

plantfyi search "lavender"     # Search across all plant species
```

## MCP Server (Claude, Cursor, Windsurf)

Add plant data to any AI assistant that supports [Model Context Protocol](https://modelcontextprotocol.io/).

```bash
pip install "plantfyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "plantfyi": {
            "command": "uvx",
            "args": ["--from", "plantfyi[mcp]", "python", "-m", "plantfyi.mcp_server"]
        }
    }
}
```

## REST API Client

```python
from plantfyi.api import PlantFYI

with PlantFYI() as api:
    plants = api.list_plants()            # Browse all 379,774 species
    families = api.list_families()        # Browse 734 families
    orders = api.list_orders()            # Browse 50 orders
    results = api.search("bamboo")        # Full-text search
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/plants/` | List all plants |
| GET | `/api/v1/plants/{slug}/` | Plant detail |
| GET | `/api/v1/orders/` | List all orders |
| GET | `/api/v1/families/` | List all families |
| GET | `/api/v1/climate-zones/` | List climate zones |
| GET | `/api/v1/distributions/` | List distributions |
| GET | `/api/v1/countries/` | List countries |
| GET | `/api/v1/comparisons/` | List comparisons |
| GET | `/api/v1/glossary/` | List glossary terms |
| GET | `/api/v1/guides/` | List guides |
| GET | `/api/v1/search/?q={query}` | Search across all content |

```bash
curl -s "https://plantfyi.com/api/v1/plants/?limit=3"
```

Full API documentation at [plantfyi.com/developers/](https://plantfyi.com/developers/).
OpenAPI 3.1.0 spec: [plantfyi.com/api/openapi.json](https://plantfyi.com/api/openapi.json).

## API Reference

| Function | Description |
|----------|-------------|
| `PlantFYI()` | Create API client (`base_url`, `timeout`) |
| `list_plants(**params)` | List all plant species |
| `get_plant(slug)` | Get plant detail |
| `list_orders(**params)` | List all orders |
| `get_order(slug)` | Get order detail |
| `list_families(**params)` | List all families |
| `get_family(slug)` | Get family detail |
| `list_climate_zones(**params)` | List climate zones |
| `get_climate_zone(slug)` | Get climate zone detail |
| `list_distributions(**params)` | List distributions |
| `list_countries(**params)` | List countries |
| `list_comparisons(**params)` | List comparisons |
| `list_glossary(**params)` | List glossary terms |
| `list_guides(**params)` | List guides |
| `search(query)` | Search across all content |

## Learn More About Plants

- **Browse**: [Plant Species](https://plantfyi.com/plants/) · [Families](https://plantfyi.com/families/) · [Orders](https://plantfyi.com/orders/)
- **Reference**: [Climate Zones](https://plantfyi.com/climate-zones/) · [Distributions](https://plantfyi.com/distributions/) · [Countries](https://plantfyi.com/countries/)
- **Guides**: [Glossary](https://plantfyi.com/glossary/) · [Guides](https://plantfyi.com/guides/)
- **API**: [REST API Docs](https://plantfyi.com/developers/) · [OpenAPI Spec](https://plantfyi.com/api/openapi.json)

## Nature FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem — living organisms, wildlife, and natural history.

| Package | PyPI | Description |
|---------|------|-------------|
| speciesfyi | [PyPI](https://pypi.org/project/speciesfyi/) | 49,112 species, 17,982 taxa, 846 ecoregions — [speciesfyi.com](https://speciesfyi.com/) |
| birdfyi | [PyPI](https://pypi.org/project/birdfyi/) | 11,251 birds, 40 orders, 258 families — [birdfyi.com](https://birdfyi.com/) |
| fishfyi | [PyPI](https://pypi.org/project/fishfyi/) | 78 fish species, 48 orders, 188 families — [fishfyi.com](https://fishfyi.com/) |
| **plantfyi** | [PyPI](https://pypi.org/project/plantfyi/) | **379,774 plants, 734 families, 50 orders — [plantfyi.com](https://plantfyi.com/)** |
| dinofyi | [PyPI](https://pypi.org/project/dinofyi/) | 6,142 dinosaurs, 15 periods, 198 countries — [dinofyi.com](https://dinofyi.com/) |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies — [colorfyi.com](https://colorfyi.com/) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 emojis — [emojifyi.com](https://emojifyi.com/) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats — [symbolfyi.com](https://symbolfyi.com/) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings — [unicodefyi.com](https://unicodefyi.com/) |
| fontfyi | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata & CSS — [fontfyi.com](https://fontfyi.com/) |
| **plantfyi** | [PyPI](https://pypi.org/project/plantfyi/) | — | Plant taxonomy & cultivation — [plantfyi.com](https://plantfyi.com/) |
| speciesfyi | [PyPI](https://pypi.org/project/speciesfyi/) | — | Species taxonomy & biodiversity — [speciesfyi.com](https://speciesfyi.com/) |
| birdfyi | [PyPI](https://pypi.org/project/birdfyi/) | — | Bird species encyclopedia — [birdfyi.com](https://birdfyi.com/) |
| fishfyi | [PyPI](https://pypi.org/project/fishfyi/) | — | Fish species & marine biology — [fishfyi.com](https://fishfyi.com/) |
| dinofyi | [PyPI](https://pypi.org/project/dinofyi/) | — | Dinosaur paleontology & fossil record — [dinofyi.com](https://dinofyi.com/) |

## Embed Widget

Embed [PlantFYI](https://plantfyi.com) widgets on any website with [plantfyi-embed](https://widget.plantfyi.com):

```html
<script src="https://cdn.jsdelivr.net/npm/plantfyi-embed@1/dist/embed.min.js"></script>
<div data-plantfyi="entity" data-slug="example"></div>
```

Zero dependencies · Shadow DOM · 4 themes (light/dark/sepia/auto) · [Widget docs](https://widget.plantfyi.com)

## Recently Updated (v0.1.2)

Latest content state on [https://plantfyi.com](https://plantfyi.com):
- [Homepage](https://plantfyi.com)
- [Developer documentation](https://plantfyi.com/developers/)
- [Sitemap (full content index)](https://plantfyi.com/sitemap.xml)

Version bumped 2026-05-27 as part of the FYIPedia [SEO recovery refresh](https://github.com/dobestan).

## License

MIT

# plantfyi

Plant taxonomy and cultivation API client — [plantfyi.com](https://plantfyi.com)

## Install

```bash
pip install plantfyi
```

## Quick Start

```python
from plantfyi.api import PlantFYI

with PlantFYI() as api:
    results = api.search("rose")
    print(results)
```

## License

MIT

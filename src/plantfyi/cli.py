"""Command-line interface for plantfyi."""

from __future__ import annotations

import json

import typer

from plantfyi.api import PlantFYI

app = typer.Typer(help="PlantFYI — Plant taxonomy and cultivation API client.")


@app.command()
def search(query: str) -> None:
    """Search plantfyi.com."""
    with PlantFYI() as api:
        result = api.search(query)
        typer.echo(json.dumps(result, indent=2))

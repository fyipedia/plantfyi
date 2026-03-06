"""Basic tests for plantfyi."""

from plantfyi import __version__


def test_version() -> None:
    assert __version__ == "0.1.0"

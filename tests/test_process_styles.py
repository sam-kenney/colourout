"""Test the :meth:`process_styles` function."""
from __future__ import annotations

import pytest

from colourout.process_styles import process_styles
from colourout.styles import Styles


def test_process_styles_all_strings() -> None:
    """Test the the function with :class:`str` parameters."""
    assert process_styles(["BLUE", "BOLD", "UNDERLINE"]) == [
        "\033[34m",
        "\033[1m",
        "\033[4m",
    ]


def test_process_styles_all_enums() -> None:
    """Test the function with :class:`Colour` objects."""
    assert process_styles([Styles.BLUE, Styles.GREEN, Styles.UNDERLINE]) == [
        "\033[34m",
        "\033[32m",
        "\033[4m",
    ]


def test_process_styles_mixed() -> None:
    """Test the function with :class:`str` and :class:`Colour` objects."""
    assert process_styles(["BLUE", Styles.RED, "UNDERLINE"]) == [
        "\033[34m",
        "\033[31m",
        "\033[4m",
    ]


def test_process_styles_invalid() -> None:
    """Test that a :class:`KeyError` is raised with invalid input."""
    with pytest.raises(KeyError):
        process_styles(["BLUE", "BOLD", "UNDERLINE", "INVALID"])

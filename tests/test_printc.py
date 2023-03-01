"""Test the :meth:`printc` function."""
from __future__ import annotations

import sys

import pytest

from colourout.printc import printc


def test_printc_no_args(capsys: pytest.CaptureFixture) -> None:
    """Test the function with no parameters."""
    printc(file=sys.stdout)
    captured = capsys.readouterr()
    assert captured.out == "\033[0m\033[0m\n"


def test_printc_with_output_text(capsys: pytest.CaptureFixture) -> None:
    """Test the function with one parameter."""
    printc("Hello, world!")
    captured = capsys.readouterr()
    assert captured.out == "\033[0mHello, world!\033[0m\n"


def test_printc_with_output_text_and_styles(capsys: pytest.CaptureFixture) -> None:
    """Test the function with one parameter and styles."""
    printc("Hello, world!", styles=["BLUE", "ITALIC"])
    captured = capsys.readouterr()
    assert captured.out == "\033[34m\033[3mHello, world!\033[0m\n"


def test_printc_with_multiple_output_text(capsys: pytest.CaptureFixture) -> None:
    """Test the function with multiple parameters."""
    printc("Hello,", "world!")
    captured = capsys.readouterr()
    assert captured.out == "\033[0mHello, world!\033[0m\n"


def test_printc_with_multiple_output_text_and_styles(
    capsys: pytest.CaptureFixture,
) -> None:
    """Test the function with multiple parameters and styles."""
    printc("Hello,", "world!", styles=["BLUE", "ITALIC"])
    captured = capsys.readouterr()
    assert captured.out == "\033[34m\033[3mHello, world!\033[0m\n"


def test_printc_with_multiple_output_text_and_styles_and_sep(
    capsys: pytest.CaptureFixture,
) -> None:
    """Test the function with multiple parameters and styles and a separator."""
    printc("Hello,", "world!", sep=" ", styles=["BLUE", "ITALIC"])
    captured = capsys.readouterr()
    assert captured.out == "\033[34m\033[3mHello, world!\033[0m\n"


def test_printc_with_multiple_output_text_and_styles_and_sep_and_end(
    capsys: pytest.CaptureFixture,
) -> None:
    """Test the function with multiple parameters and styles and a separator."""
    printc("Hello,", "world!", sep=" ", end=" ", styles=["BLUE", "ITALIC"])
    captured = capsys.readouterr()
    assert captured.out == "\033[34m\033[3mHello, world!\033[0m "


def test_printc_with_bg_colour(capsys: pytest.CaptureFixture) -> None:
    """Test the function with a background colour."""
    printc("Hello, world!", styles=["BLUE", "BG_YELLOW"])
    captured = capsys.readouterr()
    assert captured.out == "\033[34m\033[43mHello, world!\033[0m\n"

"""Test the :meth:`eprintc` function."""
from __future__ import annotations

import pytest

from colourout.eprintc import eprintc


def test_eprintc_no_args(capsys: pytest.CaptureFixture) -> None:
    """Test the function with no parameters."""
    eprintc()
    captured = capsys.readouterr()
    assert captured.err == "\033[0m\033[0m\n"


def test_eprintc_with_output_text(capsys: pytest.CaptureFixture) -> None:
    """Test the function with one parameter."""
    eprintc("Hello, world!")
    captured = capsys.readouterr()
    assert captured.err == "\033[0mHello, world!\033[0m\n"


def test_eprintc_with_output_text_and_styles(capsys: pytest.CaptureFixture) -> None:
    """Test the function with one parameter and styles."""
    eprintc("Hello, world!", styles=["BLUE", "ITALIC"])
    captured = capsys.readouterr()
    assert captured.err == "\033[34m\033[3mHello, world!\033[0m\n"


def test_eprintc_with_multiple_output_text(capsys: pytest.CaptureFixture) -> None:
    """Test the function with multiple parameters."""
    eprintc("Hello,", "world!")
    captured = capsys.readouterr()
    assert captured.err == "\033[0mHello, world!\033[0m\n"


def test_eprintc_with_multiple_output_text_and_styles(
    capsys: pytest.CaptureFixture,
) -> None:
    """Test the function with multiple parameters and styles."""
    eprintc("Hello,", "world!", styles=["BLUE", "ITALIC"])
    captured = capsys.readouterr()
    assert captured.err == "\033[34m\033[3mHello, world!\033[0m\n"


def test_eprintc_with_multiple_output_text_and_styles_and_sep(
    capsys: pytest.CaptureFixture,
) -> None:
    """Test the function with multiple parameters and styles and a separator."""
    eprintc("Hello,", "world!", sep=" ", styles=["BLUE", "ITALIC"])
    captured = capsys.readouterr()
    assert captured.err == "\033[34m\033[3mHello, world!\033[0m\n"


def test_eprintc_with_multiple_output_text_and_styles_and_sep_and_end(
    capsys: pytest.CaptureFixture,
) -> None:
    """Test the function with multiple parameters and styles and a separator."""
    eprintc("Hello,", "world!", sep=" ", end=" ", styles=["BLUE", "ITALIC"])
    captured = capsys.readouterr()
    assert captured.err == "\033[34m\033[3mHello, world!\033[0m "


def test_eprintc_with_bg_colour(capsys: pytest.CaptureFixture) -> None:
    """Test the function with a background colour."""
    eprintc("Hello, world!", styles=["BLUE", "BG_YELLOW"])
    captured = capsys.readouterr()
    assert captured.err == "\033[34m\033[43mHello, world!\033[0m\n"

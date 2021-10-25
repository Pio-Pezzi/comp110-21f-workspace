"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730414104"


def test_invert_empty() -> None:
    """Checks emply list!"""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_invert_all_single() -> None:
    """Checks only a singled valued list."""
    a: dict[str, str] = {
        "a": "purple"
    }
    assert invert(a) == {"purple": "a"}


def test_invert_ideal() -> None:
    """Checks the ideal case."""
    a: dict[str, str] = {
        "a": "blue",
        "b": "red",
        "c": "purple"
    }
    assert invert(a) == {
        "blue": "a",
        "red": "b",
        "purple": "c"
    }


def test_favorite_color_empty() -> None:
    """Tests empty dictionary!"""
    a: dict[str, str] = {}
    assert favorite_color(a) == ""


def test_favorite_color_sigular() -> None:
    """Tests if there is only one color."""
    a: dict[str, str] = {"Dave": "red", "James": "red", "Parker": "red"}
    assert favorite_color(a) == "red"


def test_favorite_color_once() -> None:
    """Tests if every color appears just once."""
    a: dict[str, str] = {"Dave": "red", "James": "purple", "Parker": "greem"}
    assert favorite_color(a) == "red"


def test_count_empty() -> None:
    """Tests an empty list."""
    b = []
    assert count(b) == {}


def test_count_only() -> None:
    """Tests when there is only one repeated item in the list."""
    a = ["a", "a", "a"]
    assert count(a) == {"a": 3}


def test_count_unique() -> None:
    """Tests when there is only one repeated item in the list."""
    a = ["a", "b", "c"]
    assert count(a) == {"a": 1, "b": 1, "c": 1}
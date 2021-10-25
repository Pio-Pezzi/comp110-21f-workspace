"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"


def test_only_evens_empty() -> None:
    """Test what happens for an empty list!"""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_odds() -> None:
    """Test if there are only odds."""
    xs: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(xs) == []


def test_only_odds() -> None:
    """Test if there are only evens!"""
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == xs


def test_sub_lower() -> None:
    """Test if top bound is less than 0."""
    xs: list[int] = [2, 4, 6, 8]
    x: int = -1
    assert sub(xs, 1, x) == []


def test_sub_range() -> None:
    """Tets a use case."""
    xs: list[int] = [2, 4, 6, 8]
    assert sub(xs, 1, 3) == [2, 4]


def test_sub_range_again() -> None:
    """Tests a use case."""
    xs: list[int] = [2, 4, 6, 8]
    assert sub(xs, 1, 3) == [2, 4]


def test_concat_empty() -> None:
    """Tests for empty lists!"""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == 0


def test_concat_repeat() -> None:
    """Tests for empty lists!"""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [1, 2, 3]
    assert concat(xs, ys) == [1, 2, 3, 1, 2, 3]


def test_concat_half() -> None:
    """Tests if one list is empty!"""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = []
    assert concat(xs, ys) == xs
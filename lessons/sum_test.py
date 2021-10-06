"""Tests for the sum function."""


from lessons.sum import sum


def test_sum_empty() -> None:
    xs: list[float] = []
    assert sum([]) == 0.0

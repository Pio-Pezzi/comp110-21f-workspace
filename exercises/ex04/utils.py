"""List utility functions."""

__author__ = "730414104"


def all(haystack: list[int], needle: int) -> bool:
    """Sorts through a list and indicates if they are all the same!"""
    if len(haystack) == 0:
        return False
    else:
        i: int = 0
        while len(haystack) > i:
            if haystack[i] != needle:
                return False
            i = 1 + i
        return True


def is_equal(first: list[int], second: list[int]) -> bool:
    """Check if two lists are deeply the same."""
    if len(first) == len(second):
        i: int = 0
        while len(first) > i:
            if first[i] != second[i]:
                return False
            i += 1
        return True
    else:
        return False


def max(input: list[int]) -> int:
    """Find max of a list!"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        i: int = 0
        max: int = input[0]
        while len(input) > i:
            if max < input[i]:
                max = input[i]
            i += 1
    return max
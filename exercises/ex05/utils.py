"""List utility functions part 2."""

__author__ = "123456789"


def only_evens(numbers: list[int]) -> list[int]:
    """Gives even numbers of the list."""
    output: list[int] = []
    i: int = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            output.append(numbers[i])
        i += 1

    return output


def sub(numbers: list[int], front: int, back: int) -> list[int]:
    """Gives a subset of a list!"""
    output: list[int] = []
    if front < 0:
        front = 0

    if back > len(numbers):
        back = len(numbers)

    if back < 1 or front > len(numbers) or len(numbers) == 0:
        return output

    i: int = 0

    while i < back - front:
        take: int = front + i
        output.append(numbers[take])
        i += 1

    return output


def concat(first: list[int], second: list[int]) -> list[int]:
    """Combines two lists!"""
    i: int = 0
    output: list[int] = []

    if len(first) < 1:
        i = 0
    else:
        while i < len(first):
            output.append(first[i])
            i += 1
    i = 0

    if len(second) < 1:
        i = 0
    else:
        while i < len(second):
            output.append(second[i])
            i += 1

    return output
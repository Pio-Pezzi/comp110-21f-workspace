"""Practice with dictionaries."""


__author__ = "730414104"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""
    for key in a:
        for check in a:
            if a[key] == a[check]:
                if key != check:
                    raise KeyError("You done goofed")

    b: dict[str, str] = {}

    for key in a:
        b[a[key]] = key

    return b


def favorite_color(a: dict[str, str]) -> str:
    """Pics out most popular favorite color!"""
    first: int = 0
    second: int = 0
    winner: str = ""
    for key in a:
        for count in a:
            if a[key] == a[count]:
                second += 1
        if second > first:
            first = second
            winner = a[key]
        second = 0
    
    return winner


def count(a: list[str]) -> dict[str, int]:
    """Shows how many times an item appeared in a list."""
    i: int = 0
    b: dict[str, int] = {}
    for key in a:
        for count in a:
            if key == count:
                i += 1
            b[key] = i
        i = 0
    
    return b
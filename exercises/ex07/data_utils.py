"""Utility functions."""

__author__ = "730414104"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings   
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
        
    # Close the file when we're done, to free its resources    
    file_handle.close()
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(data: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Gives the reader a good idea of the data."""
    summary: dict[str, list[str]] = {}
    for key in data:
        listnew: list[str] = []
        i: int = 0
        if len(data[key][0]) < n:
            n = len(data[key][0])
        while i < n:
            listnew.append(data[key][i])
            i += 1
        summary[key] = listnew
    return summary


def select(data: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Selects the  data you care about!"""
    summary: dict[str, list[str]] = {}
    for key in names:
        summary[key] = data[key]

    return summary


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concats a dictionary."""
    summary: dict[str, list[str]] = {}

    for key in first:
        summary[key] = first[key]

    for key in second:
        if key in summary:
            summary[key] = summary[key] + second[key]
        else:
            summary[key] = second[key]
            
    return summary


def count(data: list[str]) -> dict[str, int]:
    """Tells you how many times an item is in a list."""
    summary: dict[str, int] = {}
    for key in data:
        if key in summary:
            summary[key] = summary[key] + 1
        else:
            summary[key] = 1

    return summary
"""Example of a function that processes a list!"""

def main() -> None:
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kris", names))

def contains(needle: str, haystack: list[str]) -> bool:
    """Returns true if needle is found in haystack, False otherwise!"""
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
             # Test if item stored in index is equal to needle
            #return true if so
            return True

    # other wise return false after testing each item
    return False

if __namme__ == "__main__":
        main()
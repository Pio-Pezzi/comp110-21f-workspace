"""Drawing forests in a loop."""

__author__ = "730414104S"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

repeat: int = int(input("Depth: "))
i = 0
list: str = ""

while i <= repeat:
    list = list + TREE
    print(list)
    i = 1 + i

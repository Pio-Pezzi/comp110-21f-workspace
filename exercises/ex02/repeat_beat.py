"""Repeating a beat in a loop."""

__author__ = "730414104"


beat: str = input("What kinda beat do you want? ")
repeat: int = int(input("How many times do you want it repeated? "))
statement: str = ""
i = 0

if repeat <= 0:
    print("No beat...")
else:
    while i < repeat:
        statement: str = statement + beat + " "
        i += 1

print(statement + beat)
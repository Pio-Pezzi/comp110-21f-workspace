"""Counting letters in a string."""

__author__ = "730414104"


word: str = input("What word would you like to search? ")
letter: str = input("what letter would you like to search for? ")
i = 0
appearance = 0

while i < len(word):
    check = word[i]
    if check == letter:
        appearance += 1
    i += 1

print("your letter has appeared " + str(appearance) + " time(s)")
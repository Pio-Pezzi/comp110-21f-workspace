"""Counting letters in a string."""

__author__ = "730414104"

letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")

i = 0
appearance = 0

while i < len(word):
    check = word[i]
    if check == letter:
        appearance += 1
    i += 1

count = str(appearance)
print("Count: " + count)
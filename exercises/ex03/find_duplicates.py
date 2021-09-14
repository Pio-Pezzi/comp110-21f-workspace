"""Finding duplicate letters in a word."""

__author__ = "730414104"


word: str = input("Enter a word: ")
i = 0
letter: int = 0
counter: int = 0

while i < len(word):
    check = word[i]
    while letter < len(word):
        if word[letter] == check:
            counter += 1
        letter += 1
    letter = 0
    i += 1
if counter > len(word):
    print("Found duplicate: True")
else:
    print("Found duplicate: False")
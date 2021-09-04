"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730414104"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

number = randint(1, 4)
print("your fortune cookie says... ")

if number == 1:
    print("Your days will be filled with joy!")
elif number == 2:
    print("The rest of your life will be filled with pain and misery :( ")
elif number == 3:
    print("There is a suprise in your life coming, and it is coming fast")
else: 
    print("You will capture the blue flag, and live a life few men dare to dream")

print("Now go spread the positive vibes!")
"""Show how numerical operators work!"""

__author__ = "730414104"

left_hand_side: str = input("right-hand side: ")
right_hand_side: str = input("left-hand side: ")

first = int(left_hand_side)
second = int(right_hand_side)
exponential = first ** second
division = first / second
int_division = first // second
modulo = first % second

print(left_hand_side + " ** " + right_hand_side + " is " + str(exponential))
print(left_hand_side + " / " + right_hand_side + " is " + str(division))
print(left_hand_side + " // " + right_hand_side + " is " + str(int_division))
print(left_hand_side + " % " + right_hand_side + " is " + str(modulo))
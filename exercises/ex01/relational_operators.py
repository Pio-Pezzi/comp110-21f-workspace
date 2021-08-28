"""Personal Practice for independant coding!"""

__author__ = "730414104"

right_side: str = input("right hand side: ")
left_side: str = input("left hand side: ")

first = int(right_side)
second = int(left_side)
less_than = str(first < second)
greater_or_equal_to = str(first >= second)
equals = str(first == second)
not_equal = str(first != second)

print(right_side + " < " + left_side + " is " + less_than)
print(right_side + " >= " + left_side + " is " + greater_or_equal_to)
print(right_side + " == " + left_side + " is " + equals)
print(right_side + " != " + left_side + " is " + not_equal)

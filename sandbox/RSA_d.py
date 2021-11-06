"""Finds modulo inverse for HW 5."""

import math
# Part B
c: int = 7653
p: int = 101
q: int = 113
i: int = 0

while i < 16:
    answer = (6 * i) % 16
    
    print(f"{i} = {answer}")
    i += 1

k: int = 0
y: int = 0


        
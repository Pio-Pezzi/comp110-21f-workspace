"""Performs the Euclidean Algorithim!"""

a: int = 67890 
b: int = 12345
r: int = 2
table: dict[int, list[int]] = {}

while r > 0:
    r = a - ((a // b) * b)
    table[r] = [a, b]
    a = b
    b = r
    
print(table)
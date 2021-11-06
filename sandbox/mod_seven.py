"""Mode z"""

states: dict[int, int] = {}
i = 0
while i < 16:
    states[i] = (7 ** i) % 15
    i += 1

print(states)
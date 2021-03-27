import math
max=1.0
while not(math.isinf(max*2)):
    max = max*2
print(f"El mayor punto flotante (antes de que se produzca el overflow) es: {max}")

min = 1.0
while not(min/2 == 0):
    min = min/2
print(f"El mayor punto flotante (antes de que se produzca el underflow) es: {min}")

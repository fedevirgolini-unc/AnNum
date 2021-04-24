import random

def SonReciprocos(x, y):
    return x*y == 1

for _ in range(100):
    x = 1 + random.random()
    y = 1/x
    if not SonReciprocos(x, y):
        print(x)
#a) Escribir un programa que calcule el factorial de 6

def factorialde(x):
    fact = 1
    assert(x>0)
    while x>0:
        fact = x * fact
        x = x-1
    return fact

import math
x = int(input("Ingrese un numero: "))

#a) Escribir un programa que calcule el factorial de 6

def factorialde(x):
    fact = 1
    assert(x>0)
    while x>0:
        fact = x * fact
        x = x-1
    return fact

print(f"usando la funcion definida, el factorial de {x} es: {factorialde(x)}")

#b) importar math utilizar funcion conveniente para esto :)

print(f"usando la libreria math, el factorial de {x} es: {math.factorial(x)}")

#c) Ya se cumplió este punto en item a ;)
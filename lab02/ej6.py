from ej5 import ripf

def fun_lab2ej6(x):
    return 2 ** (x-1)

x0 = float(input("Ingrese un punto inicial: "))
hx = ripf(fun_lab2ej6, x0, 1e-5, 100)
print(hx[-1])
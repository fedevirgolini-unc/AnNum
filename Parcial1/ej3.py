from Algo_Horner import horn
from ej2 import busqueda_ceros

def polinomio(x):
    f = horn([1, 0, 1, -5], x)
    df = horn([3, 0, 1], x)
    return f, df

busqueda_ceros(polinomio, 10.0, -10.0, 1e-6, 15)
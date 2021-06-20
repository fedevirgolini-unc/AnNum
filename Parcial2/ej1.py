import numpy as np
from numpy.core.function_base import linspace
from scipy import linalg
from Algo_Horner import horn
import matplotlib.pyplot as plt
from Alg_soleg import soleg
from Alg_Lagrange import ilagrange

def ivander(x, y, z):

    if len(x) != len(y):
        print("Las listas x e y deben tener la misma longitud")
        return None

    #creamos la matriz de tamaño correspondiente:
    mvander = np.zeros((len(x), len(x)))

    #rellenamos la matriz
    for fila_i in range(len(x)):
        for columna_i in range(len(x)):
            mvander[fila_i, columna_i] = x[fila_i] ** columna_i
    
    #resolvemos el sistema asociado: mvander * w = y
    coef = soleg(mvander, y)

    #invertimos el vector coef para poder utilizarlo con horner
    coef = np.flip(coef)
    
    #creamos y llenamos el vector resultante
    w = []
    for i in z:
        w.append(horn(coef, i))
     
    return w


x = np.linspace(0, 2*np.pi, 55)
y = np.sin(x)
z = np.linspace(0, 2*np.pi, 100)

sol_ivander = ivander(x,y,z)
sol_lagrange = ilagrange(x, y, z)

plt.plot(z, sol_ivander, "*", label="Solucion ivander", color = 'r')
plt.plot(z, sol_lagrange, "+", label="Solucion Lagrange", color = 'g')
plt.plot(x, y, label="sen(x)", color = 'b')

plt.title("Ejercicio 1")
plt.ylabel("Eje Y")
plt.xlabel("Eje X")
plt.legend()
plt.show()
import matplotlib.pyplot as plt
import numpy as np
from Algo_Newton import rnewton
from ej3 import polinomio

x = np.linspace(-2, 4, 100)
y = [polinomio(xi)[0] for xi in x]

hx, hf = rnewton(polinomio, 10.0, 1e-6, 15)

plt.plot(x, y, label='Polinomio')
plt.plot(hx, hf, '*', label='puntos generados')

plt.title("Primer parcial - Ejercicio 4")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.xlim(-2, 4)
plt.legend()
plt.show()
from ej1 import rbisec
from ej3 import rnewton
from ej5 import ripf
from math import exp
import matplotlib.pyplot as plt
import numpy as np

def lab2ej7bisec(x):
    fun_auxiliar = lambda y: y - exp(-(1-x*y)**2)
    hx, hf = rbisec(fun_auxiliar, [0, 1.5], 1e-5, 100)
    return hx[-1]

def lab2ej7newton(x):
    fun_auxiliar = lambda y: (y - exp(-(1-x*y)**2), 1-exp(-(1-x*y)**2)*(-2*(1-x*y)*(-x)))
    hx, hf = rnewton(fun_auxiliar, 0.9, 1e-5, 100)
    return hx[-1]

def lab2ej7ipf(x):
    fun_auxiliar = lambda y : exp(-(1-x*y)**2)
    hx = ripf(fun_auxiliar, 1, 1e-5, 100)
    return hx[-1]

#Gráfico utilizando los diferentes métodos
fig, ax = plt.subplots(1, 3)
ax[0].set_title("Bisección")
ax[1].set_title("Newton")
ax[2].set_title("Punto fijo")

x = np.linspace(0, 1.5, 100)
y0 = []
y1 = []
y2 = []
for xi in x:
    y0.append(lab2ej7bisec(xi))
    y1.append(lab2ej7newton(xi))
    y2.append(lab2ej7ipf(xi))

ax[0].plot(x, y0)
ax[1].plot(x, y1)
ax[2].plot(x, y2)
plt.show()
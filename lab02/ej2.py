from ej1 import rbisec
from math import tan
import matplotlib.pyplot as plt
import numpy as np

#inciso a)-----------------------------------------------------------------------------------------------

def fun_lab2ej2a(x):
    return tan(x)-2*x

#Se necesitaron 16 iteraciones para llegar al resultado

#inciso b)-----------------------------------------------------------------------------------------------

def fun_lab2ej2b(x):
    return x**2-3

#La aproximacion resultante fue: 1.7320480346679688

#inciso c)-----------------------------------------------------------------------------------------------

#Creamos la figura en la que mostraremos los dos gráficos
fig, (ax1, ax2) = plt.subplots(1, 2)

#funcion fun_lab2ej2a
ax1.axhline(color='black')
ax1.set_title("fun_lab2ej2a con método de bisección en [0.8, 1.4]")
#graficamos la función
puntos1 = np.linspace(0.8, 1.4, 20)
evals1 = []
for idx in puntos1:
    evals1.append(fun_lab2ej2a(idx))
ax1.plot(puntos1, evals1)
#graficamos los puntos obtenidos por el método
hx1, hf1 = rbisec(fun_lab2ej2a, [0.8, 1.4], 1e-5, 100)
ax1.plot(hx1, hf1, '*')


#funcion fun_lab2ej2b
ax2.axhline(color='black')
ax2.set_title("fun_lab2ej2b con método de bisección en [1, 2]")
#graficamos la función
puntos2 = np.linspace(1, 2, 20)
evals2 = fun_lab2ej2b(puntos2)
ax2.plot(puntos2, evals2)
#graficamos los puntos obtenidos por el método
hx2, hf2 = rbisec(fun_lab2ej2b, [1, 2], 1e-5, 100)
ax2.plot(hx2, hf2, '*')

#Finalmente mostramos el gráfico obtenido
plt.show()
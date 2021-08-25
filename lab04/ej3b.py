import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt("./lab04/Datos/datos3b.dat")

y_tranf = x/y

A, B = np.polyfit(x, y_tranf, 1)

fun_lab04_ej3b = lambda x: x/(A*x-B)

x_plot = np.linspace(0, 20, 500)
f_plot = fun_lab04_ej3b(x_plot)

plt.plot(x, y, "x", label="Puntos dados")
plt.plot(x_plot, f_plot, label="Función aproximada")

plt.legend()
plt.grid()
plt.show()
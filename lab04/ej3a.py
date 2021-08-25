import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt("./lab04/Datos/datos3a.dat")

x_transf = np.log(x)
y_tranf = np.log(y)

a1, a0 = np.polyfit(x_transf, y_tranf, 1)

C = np.exp(a0)
A = a1

fun_lab04_ej3a = lambda x: C * (x ** A)

x_plot = np.linspace(1, 5, 150)
f_plot = fun_lab04_ej3a(x_plot)

plt.plot(x, y, "x", label="Puntos dados")
plt.plot(x_plot, f_plot, label="Función aproximada")

plt.legend()
plt.grid()
plt.show()
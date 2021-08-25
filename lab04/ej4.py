import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt("./lab04/Datos/covid_italia.csv", delimiter=",")
y = datos[:, 1]
x = np.arange(len(y))

y_tranf = np.log(y)

a1, a0 = np.polyfit(x, y_tranf, 1)

b = a1
a = np.exp(a0)

fun_lab04_ej4 = lambda x: a * np.exp(b * x)

f_plot = fun_lab04_ej4(x)

plt.plot(x, y, "x", label="Casos por dia")
plt.plot(x, f_plot, label="Aproximación de curva")
plt.legend()
plt.grid()
plt.show()
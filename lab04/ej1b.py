import numpy as np
import matplotlib.pyplot as plt

fun_lab04_ej1b = lambda x: (3/4) * x - (1/2)

x = np.linspace(0, 10, 20)
y = fun_lab04_ej1b(x)

y_desviado = y + np.random.rand(20)

coef = np.polyfit(x, y_desviado, 1)

aprox_plot = np.polyval(coef, x)

###---Gráfico---###
plt.plot(x,y, label="Función dada")
plt.plot(x, y_desviado, "o", label="Puntos desviados")
plt.plot(x, aprox_plot, label="Nueva aproximación")

plt.legend()
plt.grid()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

fun_lab04_ej2a = lambda x: np.arcsin(x)

x = np.linspace(0, 1, 50)
y = fun_lab04_ej2a(x)

fig = plt.figure()
axes = []

for n in range(6):
    #aproximamos con polinomio de grado n
    coef = np.polyfit(x, y, n)
    y_aprox = np.polyval(coef, x)

    #Graficamos lo obtenido
    axes.append(fig.add_subplot(2, 3, n+1))
    axes[-1].plot(x, y, label="Función dada")
    axes[-1].plot(x, y_aprox, label=f"Aproximación de grado {n}")
    axes[-1].grid()
    plt.legend()

plt.show()
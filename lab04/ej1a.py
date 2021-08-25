import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt("./lab04/Datos/datos1a.dat")

x = datos[:,0]
y = datos[:,1]

m = len(x)
sum_xi = sum(x)
sum_yi = sum(y)
sum_xi2 = sum(x ** 2)
sum_yixi = sum(x * y)

a0 = (sum_xi2 * sum_yi - sum_yixi * sum_xi) / (m * sum_xi2 - sum_xi ** 2)
a1 = (m * sum_yixi - sum_xi * sum_yi) / (m * sum_xi2 - sum_xi ** 2)

print(f"a0 = {a0}, a1 = {a1}")

aprox = lambda x: a0 + a1 * x

x_plot = np.linspace(0, 6, 60)
aprox_plot = aprox(x_plot)

plt.plot(x_plot, aprox_plot, label="Aproximación generada")
plt.plot(x, y, "o", label="Puntos dados")

plt.legend()
plt.grid()
plt.show()
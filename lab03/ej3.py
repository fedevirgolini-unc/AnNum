from ej2 import inewton
from ej1 import ilagrange
import matplotlib.pyplot as plt

def fun_lab03_ej3(x):
    return (1/x)

lista_i = list(range(1, 5))
lista_x = [(24/25) + (j/25) for j in lista_i]
lista_f = [fun_lab03_ej3(x) for x in lista_i]

f_plot = [fun_lab03_ej3(x) for x in lista_x]
p_plot = inewton(lista_i, lista_f, lista_x)


plt.plot(lista_x, f_plot, label="función f")
plt.plot(lista_x, p_plot, label="polinomio interpolante")

plt.grid()
plt.legend()
plt.show()
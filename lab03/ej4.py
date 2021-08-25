import matplotlib.pyplot as plt
from math import cos, pi
from ej2 import inewton

def fun_lab03_ej4(x):
    return(1/(1 + 25 * (x ** 2)))

a = -1
b = 1
h = (b-a)/199
lista_x = [-1 + h*i for i in range(200)]

f_plot = [fun_lab03_ej4(x) for x in lista_x]

fig = plt.figure()
axes = []

for n in range(1, 16):
    #interpolamos pn
    list_pn = [((2 * (i - 1)) / n) - 1 for i in range(1, n+2)]
    list_fpn = [fun_lab03_ej4(x) for x in list_pn]
    pn_plot = inewton(list_pn, list_fpn, lista_x)

    #interpolamos qn
    list_qn = [cos( ((2*i + 1) / (2*n+2)) * pi) for i in range(n+1)]
    list_fqn = [fun_lab03_ej4(x) for x in list_qn]
    qn_plot = inewton(list_qn, list_fqn, lista_x)

    #Graficamos lo obtenido
    axes.append(fig.add_subplot(5, 3, n))
    axes[-1].plot(lista_x, pn_plot, label="pn")
    axes[-1].plot(lista_x, qn_plot, label="qn")
    axes[-1].plot(lista_x, f_plot, label="f(x)")
    axes[-1].grid()

plt.legend()
plt.show()
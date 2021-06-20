import numpy as np
from Alg_solLU import sollu

g = 9.

k = 10

m1 = 2
m2 = 3
m3 = 2.5

w = np.array([g*m1, g*m2, g*m3])

#notemos que 0 = 2k(x2 - x1) + m1 * g - k * x1 es semejante a:
#3k * x1 - 2k * x2 = m1 * g

#notemos que 0 = k(x3 - x2) + m2 * g - 2k (x2 - x1) es semejante a:
#-2k * x1 + 3k *x2 - k * x3 = m2 * g

#notemos que 0 = m3 * g - k(x3 - x2) es semejante a:
#-k * x2 + k * x3 = m3 * g 

#por lo que ya podemos armar la matriz para resolver nuestro problema

K = np.array([[3*k, -2*k, 0], [-2*k, 3*k, -k], [0, -k, k]])

x = sollu(K, w)

#de esta forma en el vector x contendrá los valores de x1, x2 y x3
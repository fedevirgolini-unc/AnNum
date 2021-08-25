from ej1 import ilagrange
from ej2 import inewton
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

x_interp = np.arange(-3, 4)
f_interp = [1, 2, 5, 10, 5, 2, 1]
list_x = np.linspace(-3, 3, 100)

pnewton_plot = inewton(x_interp, f_interp, list_x)
plagrange_plot = ilagrange(x_interp, f_interp, list_x)
pscipy = interp1d(x_interp, f_interp, kind="quadratic")
pscipy_plot = pscipy(list_x)

plt.plot(list_x, pnewton_plot, label="Newton")
plt.plot(list_x, plagrange_plot, label="Lagrange")
plt.plot(list_x, pscipy_plot, label="Scipy")

plt.legend()
plt.grid()
plt.show()
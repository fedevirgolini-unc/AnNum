import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

datos = np.loadtxt("./lab03/datos_aeroCBA.dat")

filas, columnas = datos.shape
temp_media_anual = []

anios = datos[:,0]
temps = datos[:,1]

not_nan = ~np.isnan(temps)

#Elimino los datos que son nan
temps_interp = temps[not_nan]
anios_interp = anios[not_nan]

polinomio = interp1d(anios_interp, temps_interp, kind="cubic", fill_value="extrapolate")

anios_plot = np.arange(1957, 2018)
temp_plot = polinomio(anios_plot)

plt.plot(anios_plot, temp_plot)
plt.plot(anios_interp, temps_interp, "o")
plt.grid()
plt.show()
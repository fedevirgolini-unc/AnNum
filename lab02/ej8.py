from math import sin, cos, tan
from ej3 import rnewton

#reever! no anda xd, ya lo vi de vuelta pero no se que le pasa xd; te recomiendo revisar las derivadas, el error no es muy grande ;)

def lab2ej8(x):
    return (tan(x))/(x**2)

def der_lab2ej8(x):
    f = (x - sin(2*x)) / (cos(x)**2 * x**3)
    df = (-x**2*sin(2*x)+2*x*cos(x)**2+2*x*cos(2*x)*cos(x)**2+sin(2*x)**2*x-3*sin(2*x)*cos(x)**2) / (x**4 * cos(x)**4)
    return f, df

def min_fun_lab2ej8():
    """
    Esta función calcula el mínimo de la función f(x)=(tan(x))/x**2 en el intervalo (0, pi/2)mediante el cálculo de la raíz de su derivada
    (utilizando el método de Newton).
    """
    hx, hf =  rnewton(der_lab2ej8, 2, 1e-5, 100)
    raiz = hx[-1]
    min = lab2ej8(raiz)
    return raiz

print(min_fun_lab2ej8())
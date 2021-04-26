from ej1 import rsecante
from Algo_Newton import rnewton


def busqueda_ceros(fun, x0, x1, err, mit):
    """
    Esta función implementa tanto el método de la secante como el método de Newton \
        para encontrar raices de fun y arroja a su vez algunos datos de los algoritmos aplicados
    Entradas:
        -fun: es una función que dado x retorna f(x), df(x)
        -x0: primer punto inicial (punto inicial para método de Newton)
        -x1: segundo punto inicial
        -err: es la tolerancia deseada del error
        -mit: es en número máximo de iteraciones permitidas
    Al finalizar, la función imprime:
        -Cero obtenido por el método de la secante
        -Cero obtenido por el método de Newton
        -Cantidad de iteraciones realizadas por el método de la secante
        -Cantidad de iteraciones realizadas por el método de Newton
        -Punto en el que el valor absoluto de la función es menor

    """
    #definimos una funcion auxiliar que solo devuelva un valor (f(x)) para poder utilizarlo en el algoritmo de la secante
    fun_auxiliar = lambda x : fun(x)[0]

    #aplicamos ambos métodos
    hxs, hfs = rsecante(fun_auxiliar, x0, x1, err, mit)
    hxn, hfn = rnewton(fun, x0, err, mit)

    #calcularemos los datos que serán impresos
    cero_sec = hxs[-1]
    cero_nwt = hxn[-1]
    it_sec = len(hxs)
    it_nwt = len(hxn)
    if abs(hfs[-1]) < abs(hfn[-1]):
        mejor_cero = hxs[-1]
    else:
        mejor_cero = hxn[-1]

    #imprimimos los resultados obtenidos
    print(f"Cero obtenido por el método de la secante: {cero_sec}")
    print(f"Cero obtenido por el método de Newton: {cero_nwt}")
    print()
    print(f"Cantidad de iteraciones realizadas por el método de la secante: {it_sec}")
    print(f"Cantidad de iteraciones realizadas por el método de Newton: {it_nwt}")
    print()
    print(f"Punto en el que el valor absoluto de la función es menor: {mejor_cero}")
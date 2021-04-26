from ej3 import rnewton

def auxiliar(x, a):
    f = x**3 - a
    df = 3*(x**2)
    return f, df

def aproxcubo(a):
    """
    Esta función calcula una aproximación de la raiz cúbica del número ingrasado
    Entradas:
        -a: valor real positivo
    Salidas:
        -aprox: aproximación de la raiz de a con un error menor a 10e-6
    """
    fun_fija = lambda x: auxiliar(x, a)
    hx, hf = rnewton(fun_fija, a, 10e-6, 100)
    return hx[len(hx)-1]
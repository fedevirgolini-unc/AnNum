def rnewton(fun, x0, err, mit):
    """
    Implementa ennmétodo de Newton para hallar una raíz de una función f partiendo de un punto inicial x0
    Entradas:
        -fun: es una función que dedo x retorna f(x) y f'(x)
        -x0: es un punto inicial en R
        -err: es la tolerancia deseada del error
        -mit: es el número máximo de iteraciones permitidas
    Salidas:
        -hx: es una lista que representa el histórico de puntos generados
        -hf: es el histórico de los respectivos valores funcionales
    """
    #creamos las listas vacías que serán la salida
    hx = []
    hf = []

    xn = x0
    f, df = fun(xn)

    if abs(f) < err:
        return hx, hf
    
    for it in range(mit):
        xn1 = xn - f/df
        f, df = fun(xn1)
        hx.append(xn1)
        hf.append(f)
        if abs((xn1 - xn)/xn1) < err or abs(f) < err:
            print("Llegamos a un cero!")
            break
        elif df == 0:
            print("Una derivada es cero. no es posible continuar")
        else:
            xn = xn1

    return hx, hf
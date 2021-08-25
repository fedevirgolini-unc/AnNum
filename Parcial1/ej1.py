def rsecante(fun, x0, x1, err, mit):
    """
    Implementa el método de la secante (variante sin derivada de Newton)
    Entradas:
        -fun: es una función que dado x retorna f(x)
        -x0: primer punto inicial
        -x1: segundo punto inicial
        -err: es la tolerancia deseada del error
        -mit: es en número máximo de iteraciones permitidas
    Salidas:
        -hx: es el historial de puntos medios
        -hf: es el historial de los respectivos valoras funcionales
    """

    hx =[]
    hf = []

    a = x0
    b = x1

    fa = fun(a)
    fb = fun(b)

    for it in range(mit):
        if abs(fa) < abs(fb):
            a, b = b, a
            fa, fb = fb, fa
        
        s = (b - a) / (fb - fa)
        b, fb = a, fa
        
        a = a - fa*s
        fa = fun(a)

        hx.append(a)
        hf.append(fa)

        if abs(fa) < err:
            print("Encontramos un cero!")
            break

    return hx, hf
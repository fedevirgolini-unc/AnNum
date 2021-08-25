def ripf(fun, x0, err, mit):
    """
    Implementa el método de iteración de punto fijo para hallar un punto fijo
    Entrada:
        -fun: es una función que dado x retorna f(x)
        -x0: es un punto en R
        -err: es la tolerancia deseada del error
        -mit: es el número máximo de iteraciones
    Salida:
        -hx: lista de histórico de puntos generados
    """
    hx = []
    p0=x0
    for it in range(mit):
        p = fun(p0)
        hx.append(p)
        if abs(p-p0) < err:
            print("Encontramos un cero!")
            break
        else:
            p0 = p

    return hx
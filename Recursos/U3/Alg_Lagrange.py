def ilagrange(x, y, z):
    """
    Esta función evalúa el polinomio interpolante p usando la forma de Lagrange.
    Entradas:
        -x: Vector que contiene los x donde se desea interpolar el polinomio
        -y: Vector que contiene los respectivos y donde se desea interpolar el polinomio
        -z: Vector que contiene los puntos en donde se desea evaluar el polinomio
    Salidas:
        -w: Vector con los valores del polinomio interpolante evaluado en los puntos solicitados
    """
    if len(x) != len(y):
        print("El vector x e y tienen distinta longitud")
        return

    w = []
    n = len(x)

    for z_i in z:
        w_i = 0.0

        for idx in range(n):
            l_i = 1.0
            for idj in range(n):
                if idj != idx:
                    l_i = l_i * (z_i - x[idj]) / (x[idx] - x[idj])
            
            w_i = w_i + y[idx] * l_i

        w.append(w_i)

    return w
def calc_dif_div(x, y):
    dif_div = y.copy()
    n = len(dif_div) - 1
    m = 0

    while n > m:
        for id in range(n, m, -1):
            dif_div[id] = (dif_div[id] - dif_div[id-1]) / (x[id] - x[id - (m+1)])
        m = m + 1

    return dif_div




def inewton(x, y, z):
    """
    Esta función evalúa el polinomio interpolante p usando la forma de Newton.
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
    
    n = len(x)
    w = []

    dif_div = calc_dif_div(x, y)

    for z_i in z:
        w_i = 0.0

        for idx in range(n):
            prod = 1.0

            for idj in range(idx):
                prod = prod * (z_i - x[idj])

            w_i = w_i + dif_div[idx] * prod

        w.append(w_i)

    return w
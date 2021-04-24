def rbisec(fun, I, err, mit):
    """
    Esta funcion aplica el método de bisección
    Se le deben pasar 4 parámetros:
        -fun: es una función que dado x retorna f(x)
        -I: (=[a, b]) es un intervalo en R
        -err: es la tolerancia deseada del error
        -mit: es el número máximo de iteraciones permitidas
    La funcion finaliza en la k-esima iteración si |f(x_k)|<err o si k>mit
    los argumentos de salida son: (hx,hf) donde
        -hx = [x_1, x_2, ... x_N] es una lista que representa el historial de puntos medios
        -hf = [f(x_1), f(x_2), ... f(x_N)] el historial de los respectivos valores fincionales
    """
    #creamos nuestras listas de salidas vacías
    hx = []
    hf = []
    #asumimos que I es una lista con al menos 2 elementos
    a = I[0]
    b = I[1]
    #checkeamos que el intervalo dado sea correcto
    if a >= b:
        print("el intervalo I no está ordenado, intentar nuevamente")
        return (kx, hf)
    #checkeamos que f(a) y f(b) tienen diferente signo
    if fun(a) * fun(b) >= 0:
        print("la funcion en los extremos del intervalo I tienen el mismo signo, intentar nuevamente")
        return (kx, hf)
    
    #Ya hechos los checkeos, empezamos con el algoritmo propiamente dicho
    for it in range(mit):
        #Calculamos el punto medio y evaluamos la funcion en dicho punto
        c = (a+b) / 2
        func = fun(c)
        #Agregamos c y func a las listas de salida
        hx.append(c)
        hf.append(func)
        #vemos si el punto calculado es lo suficientemente pequeño para considerarlo un cero
        if abs(func) < err:
            print("Llegamos a un cero!")
            break
        #Vemos que extremo del intervalo debemos cambiar
        if func * fun(a) < 0:
            b = c
        else:
            a = c

    return (hx, hf)


def horn(coefs, x):
    """
    Implementación del algoritmo de Horner.
    Entradas:
        -coef: es un vector con los coeficientes del polinomio de mayor a menor grado
        -x: es el valos de la coriable independiente
    Salidas:
        -valor: resultado de evaluar el polinomio en x
    """
    valor = 0
    for i in coefs:
        valor = i + x*valor
    return valor